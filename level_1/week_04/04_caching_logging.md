# Week 4 — Part 04: Caching and observability (logging)

## Overview

Two practical realities of LLM APIs:

- calls can be expensive
- failures are hard to debug without logs

Caching reduces cost/latency.

Logging makes failures diagnosable.

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

---

## Logging (minimum viable request log)

A minimal request log should include:

- request id
- model
- latency
- success/failure
- failure location (network vs parsing vs validation)

---

## References

- `functools.lru_cache`: https://docs.python.org/3/library/functools.html#functools.lru_cache
- Python logging: https://docs.python.org/3/library/logging.html
