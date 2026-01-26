# Week 4 — Part 02: Retries, backoff, and idempotency

## Overview

Retries are for **transient** failures.

Backoff prevents you from making overload worse.

Idempotency ensures retries do not cause duplicate side effects.

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

---

## Backoff

Backoff is "wait a bit longer each retry".

Even a simple exponential backoff helps:

- 0.5s
- 1s
- 2s

Always cap retries.

---

## Idempotency

Even if you are “just calling an LLM”, idempotency is a core concept:

- If you later add writes (saving to DB, charging, creating tickets), retries can duplicate effects.

Best practice: generate a request id and log it; use idempotency keys where supported.

---

## References

- Tenacity: https://tenacity.readthedocs.io/
- Stripe idempotency concept: https://stripe.com/docs/idempotency
