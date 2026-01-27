# Week 4 — Part 03: Rate limiting + graceful degradation

## Overview

Rate limits protect providers and enforce fair usage.

Your client should behave gracefully:

- pause and retry
- or degrade (fallback model, smaller prompt, cached response)

---

## Underlying theory: rate limiting is a capacity allocation policy

You can think of a provider as having finite capacity. Rate limiting enforces a maximum request rate per user.

A common conceptual model is a token bucket:

- a bucket has capacity $B$
- tokens refill at rate $r$ tokens/second
- each request spends tokens

If there are not enough tokens, requests are rejected or delayed.

Practical implication:

- bursts may succeed, but sustained high QPS will hit limits
- your client must treat 429s as normal and recover gracefully

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
