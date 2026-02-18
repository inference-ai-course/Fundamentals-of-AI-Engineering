# Week 4 — Part 02: Retries, backoff, and idempotency

## Overview

Retries are for **transient** failures.

Backoff prevents you from making overload worse.

Idempotency ensures retries do not cause duplicate side effects.

---

## Pre-study (Self-learn)

Foundations Course assumes Self-learn is complete. If you need a refresher on reliability/operations and failure handling:

- [Pre-study index (Foundations Course → Self-learn)](../PRESTUDY.md)
- [Self-learn — Chapter 5: Resource Monitoring and Containerization](../self_learn/Chapters/5/Chapter5.md)

Why it matters here (Week 4):

- Retries improve success rate, but they also increase load and cost; caps + backoff prevent retry storms.
- Treat retries as a policy: only retry failures that are likely transient.

---

## What to retry

Good candidates:

- network timeouts
- HTTP 429 / 503
- occasional malformed JSON (if you have a repair loop)

Bad candidates:

- invalid API key
- "model not found"
- deterministic schema mismatch caused by your prompt

Rule of thumb:

- retry **transient** failures (timeouts, overload, intermittent formatting)
- do not retry **permanent** failures (bad credentials, invalid request)

---

## Backoff

Backoff is "wait a bit longer each retry".

A common policy is exponential backoff:

$$
t_k = \min(t_{\max},\ t_0\cdot 2^k)
$$

where $k$ is the retry attempt number.

Practical implication:

- if a provider is overloaded, immediate retries can worsen the overload
- backoff spreads retry traffic over time

Even a simple exponential backoff helps:

- Attempt 0: 0.5s wait
- Attempt 1: 1s wait
- Attempt 2: 2s wait
- Attempt 3: 4s wait (or cap at max, e.g., 4s)

Always cap retries.

If your system has multiple layers (your code retries + provider retries), be careful: retries can multiply.

### Code example: simple exponential backoff

```python
import time
from typing import Callable, TypeVar

T = TypeVar('T')

def retry_with_backoff(
    func: Callable[[], T],
    max_retries: int = 3,
    base_delay: float = 0.5,
    max_delay: float = 4.0
) -> T:
    """
    Retry a function with exponential backoff.
    
    Args:
        func: Function to retry (should raise on failure)
        max_retries: Maximum number of retry attempts
        base_delay: Initial delay in seconds
        max_delay: Maximum delay cap in seconds
    
    Returns:
        Result of func()
    
    Raises:
        Last exception if all retries exhausted
    """
    last_exception = None
    
    for attempt in range(max_retries + 1):
        try:
            return func()
        except Exception as e:
            last_exception = e
            
            if attempt < max_retries:
                delay = min(base_delay * (2 ** attempt), max_delay)
                print(f"Attempt {attempt + 1} failed. Retrying in {delay}s...")
                time.sleep(delay)
            else:
                print(f"All {max_retries + 1} attempts failed.")
    
    raise last_exception
```

### Usage example

```python
import requests

def call_api():
    response = requests.post(
        "https://api.example.com/v1/chat",
        json={"prompt": "Hello"},
        timeout=30.0
    )
    response.raise_for_status()
    return response.json()

# Retry with backoff
try:
    result = retry_with_backoff(call_api, max_retries=3)
    print(f"Success: {result}")
except Exception as e:
    print(f"Failed after retries: {e}")
```

### Backoff with jitter

To prevent "retry storms" (many clients retrying at the same time), add randomness:

```python
import random
import time

def retry_with_jitter(
    func: Callable[[], T],
    max_retries: int = 3,
    base_delay: float = 0.5,
    max_delay: float = 4.0
) -> T:
    last_exception = None
    
    for attempt in range(max_retries + 1):
        try:
            return func()
        except Exception as e:
            last_exception = e
            
            if attempt < max_retries:
                delay = min(base_delay * (2 ** attempt), max_delay)
                # Add jitter: +/- 25% randomness
                jitter = delay * 0.25 * (2 * random.random() - 1)
                actual_delay = delay + jitter
                time.sleep(actual_delay)
    
    raise last_exception
```

**Why jitter helps**: If 100 clients all hit rate limit at the same time and retry with identical backoff, they all retry together again, perpetuating the overload.

### Using Tenacity library (production-grade)

For production, use a battle-tested library:

```bash
pip install tenacity
```

```python
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import requests

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=0.5, max=4),
    retry=retry_if_exception_type((requests.Timeout, requests.ConnectionError))
)
def call_api_with_tenacity():
    response = requests.post(
        "https://api.example.com/v1/chat",
        json={"prompt": "Hello"},
        timeout=30.0
    )
    response.raise_for_status()
    return response.json()
```

This automatically handles:
- Exponential backoff
- Selective retry (only specific exceptions)
- Logging
- Stop conditions

---

## Idempotency

Even if you are "just calling an LLM", idempotency is a core concept:

- If you later add writes (saving to DB, charging, creating tickets), retries can duplicate effects.

Best practice: generate a request id and log it; use idempotency keys where supported.

Mental model:

- "idempotent" means "doing it twice has the same effect as doing it once"
- you implement this by deduplicating using a stable key (request id / idempotency key)

### Code example: request ID tracking

```python
import uuid
import logging

logger = logging.getLogger(__name__)

def call_llm_with_request_id(prompt: str) -> dict:
    request_id = str(uuid.uuid4())
    
    logger.info(
        "llm_request_start",
        extra={"request_id": request_id, "prompt_preview": prompt[:50]}
    )
    
    try:
        # Make API call
        response = make_api_call(prompt)
        
        logger.info(
            "llm_request_success",
            extra={"request_id": request_id}
        )
        
        return {"request_id": request_id, "response": response}
    
    except Exception as e:
        logger.error(
            "llm_request_failed",
            extra={"request_id": request_id, "error": str(e)}
        )
        raise
```

**Benefits**:
- If a retry happens, you can trace both attempts using the request_id
- If you later save to DB, you can use request_id to prevent duplicates
- Debugging is easier ("which exact request failed?")

### Idempotency keys with providers

Some providers support explicit idempotency:

```python
import requests
import uuid

def call_with_idempotency_key(prompt: str):
    idempotency_key = str(uuid.uuid4())
    
    response = requests.post(
        "https://api.example.com/v1/chat",
        json={"prompt": prompt},
        headers={
            "Authorization": "Bearer YOUR_KEY",
            "Idempotency-Key": idempotency_key  # Provider deduplicates on this
        },
        timeout=30.0
    )
    
    return response.json()
```

If the request is retried with the same idempotency key, the provider returns the cached result instead of re-processing.

### Practical scenario: database writes

```python
import sqlite3
import uuid

def save_llm_result_idempotent(prompt: str, response: str, request_id: str):
    """
    Save LLM result to database, but only once per request_id.
    """
    conn = sqlite3.connect("results.db")
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            "INSERT INTO llm_results (request_id, prompt, response) VALUES (?, ?, ?)",
            (request_id, prompt, response)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        # request_id already exists (unique constraint)
        print(f"Result for request_id {request_id} already saved (idempotent)")
    finally:
        conn.close()
```

This prevents duplicate entries even if retries happen

---

## References

- Tenacity: https://tenacity.readthedocs.io/
- Stripe idempotency concept: https://stripe.com/docs/idempotency
