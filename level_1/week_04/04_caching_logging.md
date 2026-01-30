# Week 4 — Part 04: Caching and observability (logging)

## Overview

Two practical realities of LLM APIs:

- calls can be expensive
- failures are hard to debug without logs

Caching reduces cost/latency.

Logging makes failures diagnosable.

---

## Pre-study (Level 0)

Level 1 assumes Level 0 is complete. If you need a refresher on production constraints, observability, and operational habits:

- [Pre-study index (Level 1 → Level 0)](../PRESTUDY.md)
- [Level 0 — Chapter 5: Resource Monitoring and Containerization](../../level_0/Chapters/5/Chapter5.md)

Why it matters here (Week 4):

- Caching reduces cost/latency during iteration, but incorrect cache keys can create silent wrong answers.
- Logging is how you debug failures without guessing.

---

## Caching

Cache when:

- the same request repeats
- you are iterating on downstream code

Cache key must include everything that changes output:

- model name
- system prompt
- user prompt
- temperature
- max_tokens
- any other parameters that affect output

Common cache pitfalls:

- forgetting system prompt / tool context in the key
- caching when temperature is high (outputs are intentionally stochastic)
- caching errors (you accidentally “remember” a failure)

---

## Cache key design

### Bad cache key (insufficient)

```python
import hashlib

def make_cache_key_bad(prompt: str) -> str:
    # WRONG: only hashes prompt, ignores model/temperature/etc
    return hashlib.md5(prompt.encode()).hexdigest()
```

**Problem**: Same prompt with different models/settings gets same cache key.

### Good cache key (complete)

```python
import hashlib
import json
from dataclasses import dataclass, asdict

@dataclass(frozen=True)
class LLMRequest:
    model: str
    prompt: str
    temperature: float = 0.0
    max_tokens: int = 500
    system_prompt: str = ""

def make_cache_key(req: LLMRequest) -> str:
    """
    Create deterministic cache key from all parameters.
    """
    # Convert to dict and sort keys for stability
    data = json.dumps(asdict(req), sort_keys=True)
    return hashlib.sha256(data.encode()).hexdigest()
```

**Why this works**:
- Includes all parameters that affect output
- Deterministic (same inputs → same key)
- Collision-resistant (SHA-256)

---

## Cache implementations

### In-memory cache (simple)

```python
from typing import Dict, Optional

class SimpleCache:
    """
    In-memory cache with no eviction.
    """
    def __init__(self):
        self._store: Dict[str, str] = {}
    
    def get(self, key: str) -> Optional[str]:
        return self._store.get(key)
    
    def set(self, key: str, value: str) -> None:
        self._store[key] = value
    
    def clear(self) -> None:
        self._store.clear()

# Usage
cache = SimpleCache()
key = make_cache_key(request)

cached = cache.get(key)
if cached:
    return cached

result = call_api(request)
cache.set(key, result)
```

**Limitations**: 
- No size limit (can grow indefinitely)
- Lost on restart
- Not shared across processes

### LRU cache with size limit

```python
from collections import OrderedDict
from typing import Optional

class LRUCache:
    """
    Least Recently Used cache with size limit.
    """
    def __init__(self, max_size: int = 1000):
        self.max_size = max_size
        self._store: OrderedDict[str, str] = OrderedDict()
    
    def get(self, key: str) -> Optional[str]:
        if key not in self._store:
            return None
        
        # Move to end (mark as recently used)
        self._store.move_to_end(key)
        return self._store[key]
    
    def set(self, key: str, value: str) -> None:
        if key in self._store:
            # Update existing
            self._store.move_to_end(key)
        else:
            # Evict oldest if at capacity
            if len(self._store) >= self.max_size:
                self._store.popitem(last=False)
        
        self._store[key] = value
```

### File-based cache (persistent)

```python
import json
from pathlib import Path
from typing import Optional

class FileCache:
    """
    Persistent file-based cache.
    """
    def __init__(self, cache_dir: str = ".cache"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
    
    def _get_path(self, key: str) -> Path:
        return self.cache_dir / f"{key}.json"
    
    def get(self, key: str) -> Optional[str]:
        path = self._get_path(key)
        if not path.exists():
            return None
        
        try:
            data = json.loads(path.read_text())
            return data.get("response")
        except (json.JSONDecodeError, KeyError):
            return None
    
    def set(self, key: str, value: str) -> None:
        path = self._get_path(key)
        data = {"response": value}
        path.write_text(json.dumps(data, indent=2))
```

**Benefits**: Survives restarts, shareable across processes.

---

## Cache invalidation strategies

### Time-based expiration

```python
import time
from typing import Dict, Optional, Tuple

class ExpiringCache:
    """
    Cache with TTL (time to live).
    """
    def __init__(self, ttl_seconds: float = 3600):
        self.ttl_seconds = ttl_seconds
        self._store: Dict[str, Tuple[str, float]] = {}  # key -> (value, timestamp)
    
    def get(self, key: str) -> Optional[str]:
        if key not in self._store:
            return None
        
        value, timestamp = self._store[key]
        
        # Check if expired
        if time.time() - timestamp > self.ttl_seconds:
            del self._store[key]
            return None
        
        return value
    
    def set(self, key: str, value: str) -> None:
        self._store[key] = (value, time.time())
```

### Manual invalidation

```python
class VersionedCache:
    """
    Cache with version-based invalidation.
    """
    def __init__(self):
        self._store: Dict[str, str] = {}
        self.version = 0
    
    def invalidate_all(self) -> None:
        """
        Clear cache by incrementing version.
        """
        self.version += 1
        self._store.clear()
    
    def get(self, key: str) -> Optional[str]:
        versioned_key = f"{self.version}:{key}"
        return self._store.get(versioned_key)
    
    def set(self, key: str, value: str) -> None:
        versioned_key = f"{self.version}:{key}"
        self._store[versioned_key] = value
```

---

## Logging (minimum viable request log)

A minimal request log should include:

- request id
- model
- latency
- success/failure
- failure location (network vs parsing vs validation)

Two extra fields that help later:

- prompt length (or token estimate)
- retry attempt count

---

## Logging implementation

### Structured logging setup

```python
import logging
import json
from datetime import datetime

class JSONFormatter(logging.Formatter):
    """
    Format logs as JSON for easy parsing.
    """
    def format(self, record: logging.LogRecord) -> str:
        log_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
        }
        
        # Include extra fields
        if hasattr(record, "request_id"):
            log_data["request_id"] = record.request_id
        if hasattr(record, "model"):
            log_data["model"] = record.model
        if hasattr(record, "latency_s"):
            log_data["latency_s"] = record.latency_s
        
        return json.dumps(log_data)

# Setup
logger = logging.getLogger("llm_client")
logger.setLevel(logging.INFO)

handler = logging.FileHandler("llm_requests.jsonl")
handler.setFormatter(JSONFormatter())
logger.addHandler(handler)
```

### Request logging wrapper

```python
import time
import uuid
import logging

logger = logging.getLogger("llm_client")

def call_with_logging(request: LLMRequest) -> str:
    """
    Call LLM API with comprehensive logging.
    """
    request_id = str(uuid.uuid4())
    t0 = time.time()
    
    logger.info(
        "llm_request_start",
        extra={
            "request_id": request_id,
            "model": request.model,
            "prompt_len": len(request.prompt),
            "temperature": request.temperature,
        }
    )
    
    try:
        result = call_api(request)
        latency = time.time() - t0
        
        logger.info(
            "llm_request_success",
            extra={
                "request_id": request_id,
                "model": request.model,
                "latency_s": latency,
                "response_len": len(result),
            }
        )
        
        return result
    
    except Exception as e:
        latency = time.time() - t0
        
        logger.error(
            "llm_request_failed",
            extra={
                "request_id": request_id,
                "model": request.model,
                "latency_s": latency,
                "error_type": type(e).__name__,
                "error_msg": str(e),
            }
        )
        raise
```

### Analyzing logs

```python
import json
from pathlib import Path
from collections import Counter

def analyze_logs(log_file: str = "llm_requests.jsonl"):
    """
    Analyze LLM request logs for insights.
    """
    logs = []
    for line in Path(log_file).read_text().splitlines():
        logs.append(json.loads(line))
    
    # Success rate
    total = len([l for l in logs if "llm_request" in l.get("message", "")])
    successes = len([l for l in logs if l.get("message") == "llm_request_success"])
    success_rate = (successes / total * 100) if total > 0 else 0
    
    print(f"Success rate: {success_rate:.1f}% ({successes}/{total})")
    
    # Average latency
    latencies = [l["latency_s"] for l in logs if "latency_s" in l]
    if latencies:
        avg_latency = sum(latencies) / len(latencies)
        print(f"Average latency: {avg_latency:.2f}s")
    
    # Error types
    errors = [l["error_type"] for l in logs if "error_type" in l]
    if errors:
        print("\nTop errors:")
        for error_type, count in Counter(errors).most_common(5):
            print(f"  {error_type}: {count}")
```

---

## Combined cache + logging example

```python
import logging
import time
import uuid
from typing import Optional

logger = logging.getLogger("llm_client")

class CachedLLMClient:
    """
    LLM client with caching and logging.
    """
    def __init__(self, cache: Optional[SimpleCache] = None):
        self.cache = cache or SimpleCache()
    
    def call(self, request: LLMRequest) -> str:
        request_id = str(uuid.uuid4())
        cache_key = make_cache_key(request)
        
        # Check cache
        cached = self.cache.get(cache_key)
        if cached:
            logger.info(
                "llm_cache_hit",
                extra={
                    "request_id": request_id,
                    "model": request.model,
                    "cache_key": cache_key[:16],
                }
            )
            return cached
        
        # Cache miss - make API call
        logger.info(
            "llm_cache_miss",
            extra={
                "request_id": request_id,
                "model": request.model,
            }
        )
        
        t0 = time.time()
        try:
            result = call_api(request)
            latency = time.time() - t0
            
            logger.info(
                "llm_request_success",
                extra={
                    "request_id": request_id,
                    "model": request.model,
                    "latency_s": latency,
                }
            )
            
            # Store in cache
            self.cache.set(cache_key, result)
            
            return result
        
        except Exception as e:
            latency = time.time() - t0
            
            logger.error(
                "llm_request_failed",
                extra={
                    "request_id": request_id,
                    "model": request.model,
                    "latency_s": latency,
                    "error": str(e),
                }
            )
            raise
```

---

## Self-check

- Does your cache key include all parameters that affect output?
- Can you measure your cache hit rate?
- Do your logs include enough information to debug failures?
- Can you trace a specific request through your logs using request_id?

---

## References

- `functools.lru_cache`: https://docs.python.org/3/library/functools.html#functools.lru_cache
- Python logging: https://docs.python.org/3/library/logging.html
