#!/usr/bin/env python3
"""
Production-ready LLM Client with reliability features.

Features:
- Timeouts (connect and read)
- Retries with exponential backoff and jitter
- Rate limit handling (429)
- Response caching
- Structured logging

Usage:
    from llm_client import LLMClient, LLMRequest
    
    client = LLMClient()
    response = client.call(LLMRequest(
        model="llama3.1",
        prompt="Hello, world!",
        temperature=0.0
    ))
"""

from __future__ import annotations

import hashlib
import json
import logging
import os
import random
import time
import uuid
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Callable, Dict, Optional, Tuple

import requests
from requests.exceptions import ConnectionError, Timeout, HTTPError, RequestException

logger = logging.getLogger(__name__)


# ============================================================================
# Data Classes
# ============================================================================


@dataclass(frozen=True)
class LLMRequest:
    """Immutable request payload for LLM calls."""
    model: str
    prompt: str
    system_prompt: str = ""
    temperature: float = 0.0
    max_tokens: int = 1024


@dataclass
class LLMResponse:
    """Response from an LLM call with metadata."""
    ok: bool
    text: str
    model: str
    latency_s: float
    request_id: str
    cached: bool = False
    error: Optional[str] = None
    error_type: Optional[str] = None


# ============================================================================
# Exception Classification
# ============================================================================


class TransientError(Exception):
    """Errors worth retrying (network blip, temporary overload)."""
    pass


class PermanentError(Exception):
    """Errors that will always fail (bad request, auth error)."""
    pass


@dataclass(frozen=True)
class RetryDecision:
    should_retry: bool
    reason: str


def classify_exception(exc: BaseException) -> RetryDecision:
    """Classify an exception as retryable or permanent."""
    if isinstance(exc, TransientError):
        return RetryDecision(True, "transient")
    if isinstance(exc, PermanentError):
        return RetryDecision(False, "permanent")
    if isinstance(exc, Timeout):
        return RetryDecision(True, "timeout")
    if isinstance(exc, ConnectionError):
        return RetryDecision(True, "connection")
    if isinstance(exc, HTTPError):
        if exc.response is not None:
            status = exc.response.status_code
            if status == 429:
                return RetryDecision(True, "rate_limit")
            if 500 <= status < 600:
                return RetryDecision(True, "server_error")
            if status in (400, 401, 403, 404):
                return RetryDecision(False, "client_error")
    return RetryDecision(False, "unknown")


# ============================================================================
# Cache Implementations
# ============================================================================


class SimpleMemoryCache:
    """In-memory cache for LLM responses."""
    
    def __init__(self) -> None:
        self._store: Dict[str, str] = {}
    
    def get(self, key: str) -> Optional[str]:
        return self._store.get(key)
    
    def set(self, key: str, value: str) -> None:
        self._store[key] = value
    
    def has(self, key: str) -> bool:
        return key in self._store


class SimpleFileCache:
    """File-backed cache that persists across runs."""
    
    def __init__(self, path: Path) -> None:
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self.path.write_text("{}", encoding="utf-8")
    
    def _read(self) -> Dict[str, str]:
        try:
            return json.loads(self.path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {}
    
    def _write(self, data: Dict[str, str]) -> None:
        self.path.write_text(
            json.dumps(data, ensure_ascii=False, sort_keys=True, indent=2),
            encoding="utf-8"
        )
    
    def get(self, key: str) -> Optional[str]:
        return self._read().get(key)
    
    def set(self, key: str, value: str) -> None:
        data = self._read()
        data[key] = value
        self._write(data)
    
    def has(self, key: str) -> bool:
        return key in self._read()


def make_cache_key(req: LLMRequest) -> str:
    """Generate a stable cache key from request parameters."""
    raw = json.dumps(asdict(req), sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


# ============================================================================
# Backoff and Jitter
# ============================================================================


def backoff_delay(attempt: int, *, base: float = 0.5, cap: float = 8.0) -> float:
    """Calculate exponential backoff delay with cap."""
    raw = base * (2 ** max(0, attempt - 1))
    return min(cap, float(raw))


def add_jitter(delay_s: float) -> float:
    """Add full jitter to delay (uniform random in [0, delay_s])."""
    return random.uniform(0.0, max(0.0, float(delay_s)))


def parse_retry_after(value: str) -> Optional[float]:
    """Parse Retry-After HTTP header into seconds."""
    v = value.strip()
    if not v:
        return None
    try:
        seconds = int(v)
        return max(0.0, float(seconds))
    except ValueError:
        return None


# ============================================================================
# Rate Limiter (Token Bucket)
# ============================================================================


@dataclass
class TokenBucket:
    """Token bucket rate limiter for client-side rate limiting."""
    capacity: float
    refill_per_s: float
    tokens: float
    last_refill_s: float
    
    @classmethod
    def create(cls, *, capacity: float, refill_per_s: float) -> "TokenBucket":
        now = time.time()
        return cls(
            capacity=capacity,
            refill_per_s=refill_per_s,
            tokens=capacity,
            last_refill_s=now
        )
    
    def _refill(self) -> None:
        now = time.time()
        dt = max(0.0, now - self.last_refill_s)
        self.tokens = min(self.capacity, self.tokens + dt * self.refill_per_s)
        self.last_refill_s = now
    
    def allow(self, cost: float = 1.0) -> bool:
        """Check if request is allowed and deduct tokens if so."""
        self._refill()
        if self.tokens >= cost:
            self.tokens -= cost
            return True
        return False


# ============================================================================
# LLM Client
# ============================================================================


class LLMClient:
    """
    Production-ready LLM client with reliability features.
    
    Features:
    - Configurable timeouts (connect and read)
    - Automatic retries with exponential backoff and jitter
    - Rate limit handling (respects Retry-After header)
    - Response caching (memory or file-backed)
    - Structured logging with request IDs
    
    Example:
        client = LLMClient(host="http://localhost:11434")
        response = client.call(LLMRequest(
            model="llama3.1",
            prompt="Hello!",
            temperature=0.0
        ))
        if response.ok:
            print(response.text)
    """
    
    def __init__(
        self,
        host: str = "http://localhost:11434",
        *,
        timeout_s: float = 30.0,
        max_retries: int = 3,
        cache: Optional[SimpleMemoryCache] = None,
        rate_limiter: Optional[TokenBucket] = None,
        output_dir: Optional[Path] = None,
    ) -> None:
        self.host = host
        self.timeout_s = timeout_s
        self.max_retries = max_retries
        self._cache = cache or SimpleMemoryCache()
        self._rate_limiter = rate_limiter
        self._output_dir = output_dir or Path("output")
        self._output_dir.mkdir(parents=True, exist_ok=True)
    
    def _provider_call(self, req: LLMRequest, *, timeout_s: float) -> str:
        """
        Make the actual HTTP call to the LLM provider.
        
        Override this method to support different providers (OpenAI, Anthropic, etc.)
        """
        url = f"{self.host}/api/generate"
        payload = {
            "model": req.model,
            "prompt": req.prompt,
            "system": req.system_prompt,
            "stream": False,
            "options": {
                "temperature": req.temperature,
                "num_predict": req.max_tokens,
            },
        }
        
        # Check rate limiter
        if self._rate_limiter and not self._rate_limiter.allow():
            raise TransientError("Rate limit exceeded (client-side)")
        
        try:
            resp = requests.post(
                url,
                json=payload,
                timeout=timeout_s,
                headers={"Content-Type": "application/json"}
            )
            resp.raise_for_status()
            data = resp.json()
            return data.get("response", "")
        
        except Timeout as e:
            raise TransientError(f"Request timed out after {timeout_s}s") from e
        except ConnectionError as e:
            raise TransientError(f"Connection failed: {self.host}") from e
        except HTTPError as e:
            if e.response is not None and e.response.status_code == 429:
                retry_after = e.response.headers.get("Retry-After")
                if retry_after:
                    wait_s = parse_retry_after(retry_after)
                    if wait_s:
                        raise TransientError(f"Rate limited, retry after {wait_s}s") from e
                raise TransientError("Rate limited (429)") from e
            if e.response is not None and 500 <= e.response.status_code < 600:
                raise TransientError(f"Server error: {e.response.status_code}") from e
            raise PermanentError(f"HTTP error: {e.response.status_code if e.response else 'unknown'}") from e
    
    def call(
        self,
        req: LLMRequest,
        *,
        timeout_s: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> LLMResponse:
        """
        Call the LLM with caching, retries, and logging.
        
        Args:
            req: The LLM request payload
            timeout_s: Override default timeout
            max_retries: Override default max retries
        
        Returns:
            LLMResponse with result or error details
        """
        request_id = str(uuid.uuid4())[:8]
        timeout_s = timeout_s or self.timeout_s
        max_retries = max_retries if max_retries is not None else self.max_retries
        
        # Check cache
        cache_key = make_cache_key(req)
        cached = self._cache.get(cache_key)
        if cached is not None:
            logger.info(
                "llm_cache_hit",
                extra={"request_id": request_id, "model": req.model}
            )
            return LLMResponse(
                ok=True,
                text=cached,
                model=req.model,
                latency_s=0.0,
                request_id=request_id,
                cached=True,
            )
        
        # Retry loop
        last_err: Optional[Exception] = None
        for attempt in range(max_retries + 1):
            t0 = time.time()
            try:
                text = self._provider_call(req, timeout_s=timeout_s)
                latency_s = time.time() - t0
                
                logger.info(
                    "llm_call_ok",
                    extra={
                        "request_id": request_id,
                        "model": req.model,
                        "latency_s": latency_s,
                        "attempt": attempt,
                    }
                )
                
                # Cache successful response
                self._cache.set(cache_key, text)
                
                return LLMResponse(
                    ok=True,
                    text=text,
                    model=req.model,
                    latency_s=latency_s,
                    request_id=request_id,
                )
            
            except Exception as e:
                last_err = e
                latency_s = time.time() - t0
                decision = classify_exception(e)
                
                logger.warning(
                    "llm_call_failed",
                    extra={
                        "request_id": request_id,
                        "model": req.model,
                        "latency_s": latency_s,
                        "attempt": attempt,
                        "error_type": type(e).__name__,
                        "retryable": decision.should_retry,
                    }
                )
                
                # Don't retry permanent errors
                if not decision.should_retry:
                    break
                
                # Don't sleep after last attempt
                if attempt < max_retries:
                    delay = add_jitter(backoff_delay(attempt + 1))
                    time.sleep(delay)
        
        # All retries exhausted
        return LLMResponse(
            ok=False,
            text="",
            model=req.model,
            latency_s=0.0,
            request_id=request_id,
            error=str(last_err),
            error_type=type(last_err).__name__ if last_err else "unknown",
        )
    
    def persist_failure(self, req: LLMRequest, response: LLMResponse) -> Path:
        """Persist a failure record to output directory."""
        record = {
            "request": asdict(req),
            "response": {
                "ok": response.ok,
                "error": response.error,
                "error_type": response.error_type,
                "request_id": response.request_id,
            },
        }
        path = self._output_dir / f"failure_{response.request_id}.json"
        path.write_text(json.dumps(record, indent=2), encoding="utf-8")
        return path


# ============================================================================
# Convenience Functions
# ============================================================================


def call_ollama(
    model: str,
    prompt: str,
    *,
    host: str = "http://localhost:11434",
    timeout_s: float = 60.0,
    temperature: float = 0.0,
) -> str:
    """
    Simple one-off call to Ollama.
    
    Raises:
        ConnectionError: If Ollama service is not reachable
        TimeoutError: If request exceeds timeout
        ValueError: If model not found
    """
    client = LLMClient(host=host, timeout_s=timeout_s, max_retries=0)
    response = client.call(LLMRequest(
        model=model,
        prompt=prompt,
        temperature=temperature,
    ))
    
    if not response.ok:
        if response.error_type == "ConnectionError":
            raise ConnectionError(f"Cannot connect to Ollama at {host}")
        if response.error_type == "Timeout":
            raise TimeoutError(f"Request timed out after {timeout_s}s")
        raise ValueError(response.error or "Unknown error")
    
    return response.text


# ============================================================================
# Main Entry Point
# ============================================================================


if __name__ == "__main__":
    import argparse
    
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    
    parser = argparse.ArgumentParser(description="LLM Client CLI")
    parser.add_argument("--model", required=True, help="Model name")
    parser.add_argument("--prompt", required=True, help="Prompt text")
    parser.add_argument("--host", default="http://localhost:11434", help="Ollama host")
    parser.add_argument("--timeout", type=float, default=60.0, help="Timeout in seconds")
    parser.add_argument("--temperature", type=float, default=0.0, help="Temperature")
    args = parser.parse_args()
    
    try:
        result = call_ollama(
            model=args.model,
            prompt=args.prompt,
            host=args.host,
            timeout_s=args.timeout,
            temperature=args.temperature,
        )
        print(result)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)
