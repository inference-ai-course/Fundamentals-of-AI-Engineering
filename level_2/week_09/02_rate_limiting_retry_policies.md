# Week 9 — Part 02: Rate limiting + retry policies

## Overview

Rate limiting protects the service and controls cost.

Retry is not free:

- retries amplify load

Use:

- bounded retries
- exponential backoff
- idempotency where possible

---

## Underlying theory: retries amplify load

If your system issues $n$ attempts per user request on average, then your downstream load multiplies by $n$.

Simple approximation:

$$
\text{effective QPS} \approx \text{incoming QPS} \cdot \mathbb{E}[\text{attempts}]
$$

So a “small” retry policy can create large load spikes during outages.

This is why you must combine:

- bounded retries
- backoff
- rate limits

---

## Rate limiting intuition (token bucket mental model)

One common model is a token bucket:

- tokens refill at rate $r$ (requests/second)
- bucket capacity $b$ allows short bursts
- each request consumes 1 token

Practical implication:

- you can allow bursts while still enforcing an average rate
- you can rate limit expensive endpoints more aggressively (`/ingest`, agent loops)

## What to rate limit first

- `/chat`
- `/ingest`
- agent endpoints

---

## Minimal retry policy (write it down)

Decide these values explicitly:

- max_attempts: e.g., 3
- base_delay_ms: e.g., 200
- max_delay_ms: e.g., 2000
- retryable_errors: timeouts, 429, transient 5xx

Do not retry:

- validation errors (4xx)
- deterministic failures (e.g., “no chunks found”)

---

## Exponential backoff + jitter

Backoff prevents retry storms. Jitter prevents synchronized retries.

---

## References

- HTTP 429: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429
- Retry-After header: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After
- Exponential backoff + jitter (AWS): https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/
