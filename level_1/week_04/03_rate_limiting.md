# Week 4 — Part 03: Rate limiting + graceful degradation

## Overview

Rate limits protect providers and enforce fair usage.

Your client should behave gracefully:

- pause and retry
- or degrade (fallback model, smaller prompt, cached response)

---

## HTTP 429

429 means “Too Many Requests”.

Your behavior should be:

- respect the `Retry-After` header if present
- otherwise backoff and retry

---

## References

- HTTP 429: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429
