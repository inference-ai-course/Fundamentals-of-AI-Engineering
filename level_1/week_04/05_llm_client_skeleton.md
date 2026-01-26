# Week 4 — Part 05: A reusable `llm_client.py` skeleton

## Overview

Your goal is a single module you can reuse across projects that provides:

- timeouts
- retries + backoff
- basic rate limit handling
- basic caching
- logging

This is a Level 1 skeleton (provider-agnostic). You can adapt it to OpenAI/Anthropic/etc.

---

## Skeleton design

We’ll define:

- a request payload (model + prompt + settings)
- a stable cache key
- a `call()` method

---

## Example code

```python
import hashlib
import json
import logging
import time
from dataclasses import asdict, dataclass
from typing import Any

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class LLMRequest:
    model: str
    prompt: str
    temperature: float = 0.0


class SimpleMemoryCache:
    def __init__(self) -> None:
        self._store: dict[str, str] = {}

    def get(self, key: str) -> str | None:
        return self._store.get(key)

    def set(self, key: str, value: str) -> None:
        self._store[key] = value


def make_cache_key(req: LLMRequest) -> str:
    raw = json.dumps(asdict(req), sort_keys=True)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


class LLMClient:
    def __init__(self, cache: SimpleMemoryCache | None = None) -> None:
        self._cache = cache or SimpleMemoryCache()

    def _provider_call(self, req: LLMRequest, timeout_s: float) -> str:
        raise NotImplementedError("Implement provider-specific HTTP/API call")

    def call(self, req: LLMRequest, timeout_s: float = 30.0, max_retries: int = 2) -> str:
        cache_key = make_cache_key(req)
        cached = self._cache.get(cache_key)
        if cached is not None:
            logger.info("llm_cache_hit", extra={"model": req.model})
            return cached

        last_err: Exception | None = None
        for attempt in range(max_retries + 1):
            t0 = time.time()
            try:
                text = self._provider_call(req, timeout_s=timeout_s)
                logger.info(
                    "llm_call_ok",
                    extra={"model": req.model, "latency_s": time.time() - t0, "attempt": attempt},
                )
                self._cache.set(cache_key, text)
                return text
            except Exception as e:
                last_err = e
                logger.warning(
                    "llm_call_failed",
                    extra={"model": req.model, "latency_s": time.time() - t0, "attempt": attempt},
                )
                if attempt < max_retries:
                    time.sleep(min(2 ** attempt, 4))

        raise RuntimeError(f"LLM call failed after retries: {last_err}")
```

---

## Next steps

- Implement `_provider_call()` using your chosen provider SDK.
- Add structured output validation from Week 3.
- Use this client in Week 6 capstone pipeline.

---

## References

- Python logging: https://docs.python.org/3/library/logging.html
- Tenacity (for more robust retries): https://tenacity.readthedocs.io/
