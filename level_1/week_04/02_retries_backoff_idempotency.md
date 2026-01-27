# Week 4 — Part 02: Retries, backoff, and idempotency

## Overview

Retries are for **transient** failures.

Backoff prevents you from making overload worse.

Idempotency ensures retries do not cause duplicate side effects.

---

## Underlying theory: retries are a control policy under uncertainty

If a single attempt succeeds with probability $q$, then with up to $R$ retries (so $R+1$ total attempts), the probability of eventual success is:

$$
P(\text{success}) = 1 - (1-q)^{R+1}
$$

Retries increase success probability, but they also increase load and cost.

This is why backoff and caps exist: you want to improve success rate *without* amplifying overload.

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
