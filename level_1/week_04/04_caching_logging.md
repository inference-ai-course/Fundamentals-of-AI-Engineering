# Week 4 — Part 04: Caching and observability (logging)

## Overview

Two practical realities of LLM APIs:

- calls can be expensive
- failures are hard to debug without logs

Caching reduces cost/latency.

Logging makes failures diagnosable.

---

## Underlying theory: caching is memoization of a pure-ish function

If your LLM call were a pure function:

$$
y = f(x)
$$

then caching would be memoization: store $f(x)$ so repeated calls return instantly.

LLM calls are only “pure-ish” because settings affect output. So your cache key must include every input that can change the result.

Practical implication: incorrect cache keys cause **silent wrong answers**, which are worse than visible failures.

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
