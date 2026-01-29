# Week 4 — Part 02: Retries, backoff, and idempotency

## Overview

Retries are for **transient** failures.

Backoff prevents you from making overload worse.

Idempotency ensures retries do not cause duplicate side effects.

---

## Pre-study (Level 0)

Level 1 assumes Level 0 is complete. If you need a refresher on reliability/operations and failure handling:

- [Pre-study index (Level 1 → Level 0)](../PRESTUDY.md)
- [Level 0 — Chapter 5: Resource Monitoring and Containerization](../../level_0/Chapters/5/Chapter5.md)

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

- 0.5s
- 1s
- 2s

Always cap retries.

If your system has multiple layers (your code retries + provider retries), be careful: retries can multiply.

---

## Idempotency

Even if you are “just calling an LLM”, idempotency is a core concept:

- If you later add writes (saving to DB, charging, creating tickets), retries can duplicate effects.

Best practice: generate a request id and log it; use idempotency keys where supported.

Mental model:

- “idempotent” means “doing it twice has the same effect as doing it once”
- you implement this by deduplicating using a stable key (request id / idempotency key)

---

## References

- Tenacity: https://tenacity.readthedocs.io/
- Stripe idempotency concept: https://stripe.com/docs/idempotency
