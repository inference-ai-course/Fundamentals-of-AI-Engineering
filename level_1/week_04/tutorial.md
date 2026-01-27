# Level 1 — Week 4 Tutorials

## Overview

This week you engineer LLM API calls like a production system:

- timeouts
- retries + backoff
- rate limit handling
- caching (cost + latency)
- logging (debuggability)

## Navigation

- [01 — Timeouts + failure modes](01_timeouts_failures.md)
- [02 — Retries, backoff, and idempotency](02_retries_backoff_idempotency.md)
- [03 — Rate limiting + graceful degradation](03_rate_limiting.md)
- [04 — Caching + observability (logging)](04_caching_logging.md)
- [05 — A reusable `llm_client.py` skeleton](05_llm_client_skeleton.md)

## Recommended order

1. Read 01–04 for the mental models.
2. Implement 05 and use it as a base for your capstone.

Use [practice.ipynb](practice.ipynb) for extra hands-on work.

Why this order works:

1. **Mental models first**
    - Reliability features interact: retries without timeouts can hang forever; retries without backoff can cause storms.
    - What to verify: you can explain what happens on timeout vs 429 vs 5xx, and what your client should do in each case.

2. **Client skeleton second**
    - The reusable client is where engineering habits live (timeouts, retries, logging, caching).
    - What to verify: you can force a failure (bad key, forced timeout) and your client exits with a clear error and useful logs.
