# Week 4 — Part 03: Rate limiting + graceful degradation

## Overview

Rate limits protect providers and enforce fair usage.

Your client should behave gracefully:

- pause and retry
- or degrade (fallback model, smaller prompt, cached response)

---

## Pre-study (Level 0)

Level 1 assumes Level 0 is complete. If you need a refresher on production constraints and graceful failure handling:

- [Pre-study index (Level 1 → Level 0)](../PRESTUDY.md)
- [Level 0 — Chapter 5: Resource Monitoring and Containerization](../../level_0/Chapters/5/Chapter5.md)

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

## References

- HTTP 429: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429
