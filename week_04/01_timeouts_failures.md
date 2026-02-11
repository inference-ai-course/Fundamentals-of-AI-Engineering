# Week 4 — Part 01: Timeouts and failure modes

## Overview

A timeout is the simplest reliability feature:

- Without a timeout, your program can hang forever.
- With a timeout, you turn “unknown waiting” into a controlled failure.

---

## Pre-study (Self-learn)

Foundamental Course assumes Self-learn is complete. If you need a refresher on reliability/operations and debugging practices:

- [Pre-study index (Foundamental Course → Self-learn)](../PRESTUDY.md)
- [Self-learn — Chapter 5: Resource Monitoring and Containerization](../self_learn/Chapters/5/Chapter5.md)

Why it matters here (Week 4):

- Timeouts are the simplest way to prevent a single bad request from freezing your whole script.
- A timeout turns “unknown waiting” into a controlled, debuggable failure.

---

## Why requests fail in real systems

Common failure types:

- DNS issues
- network drops
- provider overload
- slow responses
- malformed responses

Your code should assume *some* requests will fail.

Useful failure taxonomy:

- **connect failures** (DNS, TCP connect)
- **read timeouts** (server accepted but is too slow)
- **application errors** (4xx/5xx responses)
- **corrupt/malformed responses** (partial payloads, invalid JSON)

---

## Timeout rules of thumb

- Always set a timeout.
- Use different timeouts for connect vs read if your client supports it.
- Make the timeout configurable.

Practical approach (Foundamental Course):

- start with a conservative timeout (e.g., 30s)
- log timeouts distinctly from other failures
- if timeouts happen often, decide whether to:
  - reduce prompt size
  - switch models
  - increase timeout
  - add retries with backoff

---

## Code examples

### Basic timeout with requests

```python
import requests

try:
    response = requests.get(
        "https://api.example.com/v1/completions",
        timeout=30.0  # 30 second timeout
    )
    response.raise_for_status()
except requests.Timeout:
    print("Request timed out after 30 seconds")
except requests.RequestException as e:
    print(f"Request failed: {e}")
```

### Separate connect and read timeouts

```python
import requests

try:
    response = requests.post(
        "https://api.example.com/v1/chat",
        json={"prompt": "..."},
        timeout=(5.0, 60.0)  # (connect timeout, read timeout)
    )
except requests.ConnectTimeout:
    print("Failed to connect within 5 seconds")
except requests.ReadTimeout:
    print("Server didn't respond within 60 seconds")
```

**Why separate timeouts?**
- Connect timeout: catches DNS/network issues quickly (should be short: 3-10s)
- Read timeout: allows model processing time (can be longer: 30-120s)

### Configurable timeout wrapper

```python
import os
import requests
from typing import Optional

def call_llm_api(prompt: str, timeout_s: Optional[float] = None) -> str:
    timeout = timeout_s or float(os.getenv("LLM_TIMEOUT", "30.0"))
    
    try:
        response = requests.post(
            "https://api.example.com/v1/chat",
            json={"prompt": prompt},
            timeout=timeout,
            headers={"Authorization": f"Bearer {os.getenv('API_KEY')}"}
        )
        response.raise_for_status()
        return response.json()["text"]
    except requests.Timeout:
        raise TimeoutError(f"LLM API call timed out after {timeout}s")
    except requests.RequestException as e:
        raise RuntimeError(f"LLM API call failed: {e}")
```

---

## Troubleshooting timeouts

### Scenario 1: Intermittent timeouts

**Symptom**: Some requests timeout, others succeed.

**Diagnosis**:
```python
import time

t0 = time.time()
try:
    response = call_llm_api(prompt, timeout_s=30.0)
    print(f"Success in {time.time() - t0:.2f}s")
except TimeoutError:
    print(f"Timeout after {time.time() - t0:.2f}s")
```

**Common causes**:
- Provider load varies (peak hours)
- Prompt complexity varies (longer prompts = longer processing)
- Network congestion

**Fix**: Add retries with backoff (see Part 02).

---

### Scenario 2: All requests timeout

**Symptom**: Every request hits the timeout.

**Diagnosis**: Check if timeout is too aggressive.

```python
# Try with progressively longer timeouts
for timeout in [10, 30, 60, 120]:
    print(f"Testing with {timeout}s timeout...")
    try:
        response = call_llm_api(prompt, timeout_s=timeout)
        print(f"Success at {timeout}s")
        break
    except TimeoutError:
        print(f"Failed at {timeout}s")
```

**Common causes**:
- Timeout too short for model/prompt combination
- Provider API is down
- Network path is broken

**Fix**: 
- Increase timeout if model legitimately needs more time
- Check provider status page
- Try from different network

---

### Scenario 3: Hanging requests (no timeout set)

**Symptom**: Script hangs indefinitely.

**Problem**: No timeout configured.

**Bad code**:
```python
response = requests.post(url, json=payload)  # Can hang forever!
```

**Fix**:
```python
response = requests.post(url, json=payload, timeout=30.0)  # Always set timeout
```

---

## Timeout selection guide

| Use case | Connect timeout | Read timeout | Total |
|----------|----------------|--------------|-------|
| Quick chat completion | 3s | 15s | 18s |
| Standard completion | 5s | 30s | 35s |
| Long-form generation | 5s | 90s | 95s |
| Embedding/classification | 3s | 10s | 13s |

**Adjust based on**:
- Model speed (GPT-3.5 vs GPT-4)
- Prompt length (longer = slower)
- Output length (more tokens = more time)
- Provider SLA (check their typical latency)

---

## Logging timeouts for analysis

```python
import logging
import time

logger = logging.getLogger(__name__)

def call_llm_with_logging(prompt: str, timeout_s: float = 30.0) -> str:
    t0 = time.time()
    try:
        response = requests.post(
            url,
            json={"prompt": prompt},
            timeout=timeout_s
        )
        latency = time.time() - t0
        logger.info(
            "llm_call_success",
            extra={
                "latency_s": latency,
                "prompt_len": len(prompt),
                "timeout_s": timeout_s
            }
        )
        return response.json()["text"]
    except requests.Timeout:
        latency = time.time() - t0
        logger.error(
            "llm_call_timeout",
            extra={
                "latency_s": latency,
                "prompt_len": len(prompt),
                "timeout_s": timeout_s
            }
        )
        raise
```

This logging helps you:
- Identify which prompts are slow
- Tune timeouts based on data
- Detect provider degradation

---

## Self-check

- Can you demonstrate that your code times out rather than hanging?
- Can you explain the difference between connect and read timeouts?
- Have you logged timeout events to help debugging?

---

## References

- Requests timeouts: https://requests.readthedocs.io/en/latest/user/quickstart/#timeouts
- OpenAI API timeouts: https://platform.openai.com/docs/guides/rate-limits
