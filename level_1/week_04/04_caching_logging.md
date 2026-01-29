# Week 4 — Part 04: Caching and observability (logging)

## Overview

Two practical realities of LLM APIs:

- calls can be expensive
- failures are hard to debug without logs

Caching reduces cost/latency.

Logging makes failures diagnosable.

---

## Pre-study (Level 0)

Level 1 assumes Level 0 is complete. If you need a refresher on production constraints, observability, and operational habits:

- [Pre-study index (Level 1 → Level 0)](../PRESTUDY.md)
- [Level 0 — Chapter 5: Resource Monitoring and Containerization](../../level_0/Chapters/5/Chapter5.md)

Why it matters here (Week 4):

- Caching reduces cost/latency during iteration, but incorrect cache keys can create silent wrong answers.
- Logging is how you debug failures without guessing.

---

## Caching

Cache when:

- the same request repeats
- you are iterating on downstream code

Cache key must include everything that changes output:

- model name
- system prompt
- user prompt
- temperature

Common cache pitfalls:

- forgetting system prompt / tool context in the key
- caching when temperature is high (outputs are intentionally stochastic)
- caching errors (you accidentally “remember” a failure)

---

## Logging (minimum viable request log)

A minimal request log should include:

- request id
- model
- latency
- success/failure
- failure location (network vs parsing vs validation)

Two extra fields that help later:

- prompt length (or token estimate)
- retry attempt count

---

## References

- `functools.lru_cache`: https://docs.python.org/3/library/functools.html#functools.lru_cache
- Python logging: https://docs.python.org/3/library/logging.html
