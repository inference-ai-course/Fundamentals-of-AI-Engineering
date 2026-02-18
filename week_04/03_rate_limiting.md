# Week 4 — Part 03: Rate limiting + graceful degradation

## Overview

Rate limits protect providers and enforce fair usage.

Your client should behave gracefully:

- pause and retry
- or degrade (fallback model, smaller prompt, cached response)

---

## Pre-study (Self-learn)

Foundations Course assumes Self-learn is complete. If you need a refresher on production constraints and graceful failure handling:

- [Pre-study index (Foundations Course → Self-learn)](../PRESTUDY.md)
- [Self-learn — Chapter 5: Resource Monitoring and Containerization](../self_learn/Chapters/5/Chapter5.md)

Why it matters here (Week 4):

- Treat 429s as normal: the client should recover predictably (wait/backoff) or degrade.
- Your capstone will be more stable if rate limiting is handled centrally in the client.

---

## HTTP 429

429 means “Too Many Requests”.

Your behavior should be:

- respect the `Retry-After` header if present
- otherwise backoff and retry

Graceful degradation options (choose based on your product):

- return a clear “busy, try later” message
- fall back to a cheaper/faster model
- reduce prompt size / requested output length
- serve a cached result if correctness allows

---

## Understanding rate limit types

Providers typically enforce multiple rate limits:

1. **Requests per minute (RPM)**: e.g., 60 requests/min
2. **Tokens per minute (TPM)**: e.g., 90,000 tokens/min
3. **Concurrent requests**: e.g., max 10 simultaneous requests

You can hit any of these independently.

**Example scenario**:
- Limit: 60 RPM, 90k TPM
- You send 30 requests with 4k tokens each in 1 minute
- Total: 30 requests (OK), 120k tokens (EXCEEDS LIMIT)
- Result: 429 error before hitting the request limit

---

## Detecting and handling 429

### Basic 429 handling

```python
import requests
import time

def call_with_429_handling(prompt: str, max_retries: int = 3) -> str:
    for attempt in range(max_retries + 1):
        try:
            response = requests.post(
                "https://api.example.com/v1/chat",
                json={"prompt": prompt},
                timeout=30.0
            )
            
            if response.status_code == 429:
                # Check for Retry-After header
                retry_after = response.headers.get("Retry-After")
                
                if retry_after:
                    wait_time = int(retry_after)
                    print(f"Rate limited. Waiting {wait_time}s (from Retry-After header)")
                else:
                    # No header, use exponential backoff
                    wait_time = min(2 ** attempt, 60)
                    print(f"Rate limited. Waiting {wait_time}s (exponential backoff)")
                
                if attempt < max_retries:
                    time.sleep(wait_time)
                    continue
                else:
                    raise Exception("Rate limit exceeded after retries")
            
            response.raise_for_status()
            return response.json()["text"]
            
        except requests.RequestException as e:
            if attempt < max_retries:
                time.sleep(2 ** attempt)
            else:
                raise
    
    raise Exception("Failed after all retries")
```

### Parsing Retry-After header

The `Retry-After` header can be:
- Seconds: `Retry-After: 60`
- HTTP date: `Retry-After: Wed, 21 Oct 2026 07:28:00 GMT`

```python
from datetime import datetime
from email.utils import parsedate_to_datetime

def parse_retry_after(retry_after_header: str) -> float:
    """
    Parse Retry-After header to seconds.
    
    Returns:
        Seconds to wait
    """
    try:
        # Try as integer (seconds)
        return float(retry_after_header)
    except ValueError:
        # Try as HTTP date
        retry_date = parsedate_to_datetime(retry_after_header)
        now = datetime.now(retry_date.tzinfo)
        delta = (retry_date - now).total_seconds()
        return max(0, delta)
```

---

## Client-side rate limiting

Prevent hitting rate limits by throttling requests yourself:

### Simple token bucket

```python
import time
from collections import deque

class RateLimiter:
    """
    Simple token bucket rate limiter.
    """
    def __init__(self, requests_per_minute: int):
        self.requests_per_minute = requests_per_minute
        self.min_interval = 60.0 / requests_per_minute
        self.last_request_time = 0.0
    
    def wait_if_needed(self) -> None:
        """
        Block until enough time has passed since last request.
        """
        now = time.time()
        time_since_last = now - self.last_request_time
        
        if time_since_last < self.min_interval:
            sleep_time = self.min_interval - time_since_last
            time.sleep(sleep_time)
        
        self.last_request_time = time.time()

# Usage
limiter = RateLimiter(requests_per_minute=60)

for prompt in prompts:
    limiter.wait_if_needed()
    response = call_api(prompt)
```

### Sliding window rate limiter

More accurate for bursty traffic:

```python
import time
from collections import deque

class SlidingWindowRateLimiter:
    """
    Tracks requests in a sliding time window.
    """
    def __init__(self, max_requests: int, window_seconds: float):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = deque()  # Timestamps of recent requests
    
    def wait_if_needed(self) -> None:
        """
        Wait until we're under the rate limit.
        """
        now = time.time()
        
        # Remove requests outside the window
        while self.requests and self.requests[0] < now - self.window_seconds:
            self.requests.popleft()
        
        # If at limit, wait
        if len(self.requests) >= self.max_requests:
            oldest = self.requests[0]
            sleep_time = (oldest + self.window_seconds) - now
            if sleep_time > 0:
                time.sleep(sleep_time)
            
            # Clean up again after sleeping
            now = time.time()
            while self.requests and self.requests[0] < now - self.window_seconds:
                self.requests.popleft()
        
        # Record this request
        self.requests.append(time.time())

# Usage
limiter = SlidingWindowRateLimiter(max_requests=60, window_seconds=60.0)

for prompt in prompts:
    limiter.wait_if_needed()
    response = call_api(prompt)
```

---

## Graceful degradation strategies

### Strategy 1: Fallback to cheaper model

```python
def call_with_fallback(prompt: str) -> str:
    """
    Try expensive model, fall back to cheaper one on 429.
    """
    try:
        return call_api(prompt, model="gpt-4")
    except RateLimitError:
        print("GPT-4 rate limited, falling back to GPT-3.5")
        return call_api(prompt, model="gpt-3.5-turbo")
```

### Strategy 2: Serve cached result

```python
import hashlib
import json

cache = {}

def call_with_cache_fallback(prompt: str) -> str:
    """
    On rate limit, return cached result if available.
    """
    cache_key = hashlib.md5(prompt.encode()).hexdigest()
    
    try:
        result = call_api(prompt)
        cache[cache_key] = result
        return result
    except RateLimitError:
        if cache_key in cache:
            print("Rate limited, serving cached result")
            return cache[cache_key]
        else:
            raise Exception("Rate limited and no cache available")
```

### Strategy 3: Queue and batch

```python
from queue import Queue
from threading import Thread
import time

class BatchProcessor:
    """
    Queue requests and process with rate limiting.
    """
    def __init__(self, requests_per_minute: int):
        self.queue = Queue()
        self.limiter = RateLimiter(requests_per_minute)
        self.results = {}
        
        # Start background processor
        self.worker = Thread(target=self._process_queue, daemon=True)
        self.worker.start()
    
    def _process_queue(self):
        while True:
            request_id, prompt = self.queue.get()
            self.limiter.wait_if_needed()
            
            try:
                result = call_api(prompt)
                self.results[request_id] = {"status": "success", "result": result}
            except Exception as e:
                self.results[request_id] = {"status": "error", "error": str(e)}
    
    def submit(self, request_id: str, prompt: str):
        """
        Add request to queue.
        """
        self.queue.put((request_id, prompt))
    
    def get_result(self, request_id: str, timeout: float = 60.0):
        """
        Block until result is ready.
        """
        deadline = time.time() + timeout
        while time.time() < deadline:
            if request_id in self.results:
                return self.results[request_id]
            time.sleep(0.1)
        
        raise TimeoutError(f"Result not ready after {timeout}s")
```

---

## Monitoring rate limit usage

Track your usage to avoid surprises:

```python
import logging

logger = logging.getLogger(__name__)

class RateLimitMonitor:
    """
    Track rate limit hits and usage patterns.
    """
    def __init__(self):
        self.total_requests = 0
        self.rate_limit_hits = 0
    
    def record_request(self, success: bool, rate_limited: bool):
        self.total_requests += 1
        if rate_limited:
            self.rate_limit_hits += 1
        
        rate = (self.rate_limit_hits / self.total_requests * 100) if self.total_requests > 0 else 0
        
        logger.info(
            "rate_limit_stats",
            extra={
                "total_requests": self.total_requests,
                "rate_limit_hits": self.rate_limit_hits,
                "rate_limit_percentage": rate
            }
        )
        
        # Alert if rate limit hit rate is high
        if rate > 10:
            logger.warning(
                "high_rate_limit_rate",
                extra={"rate_limit_percentage": rate}
            )
```

---

## Self-check

- Can you handle 429 errors gracefully without crashing?
- Do you respect the `Retry-After` header when present?
- Have you implemented client-side throttling to avoid rate limits?
- Can your system degrade gracefully (cache/fallback/queue)?

---

## References

- HTTP 429: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429
- Token bucket algorithm: https://en.wikipedia.org/wiki/Token_bucket
- OpenAI rate limits: https://platform.openai.com/docs/guides/rate-limits
