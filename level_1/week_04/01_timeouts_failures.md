# Week 4 — Part 01: Timeouts and failure modes

## Overview

A timeout is the simplest reliability feature:

- Without a timeout, your program can hang forever.
- With a timeout, you turn “unknown waiting” into a controlled failure.

---

## Underlying theory: you are bounding tail latency

Real systems do not have a single “latency”. They have a latency *distribution*.

- most requests are fast
- a small fraction are slow (the tail)
- some never return (stuck connections, blackholed packets, server bugs)

A timeout is a policy that sets an upper bound on how long you are willing to wait:

$$
\text{wait time} \le \tau
$$

Practical implication:

- you are choosing a tradeoff between **user experience** (fail fast) and **success rate** (wait longer)
- even if 99% of requests succeed, the remaining 1% can freeze your whole script if you do not bound it

---

## Why requests fail in real systems

Common failure types:

- DNS issues
- network drops
- provider overload
- slow responses
- malformed responses

Your code should assume *some* requests will fail.

Useful failure taxonomy:

- **connect failures** (DNS, TCP connect)
- **read timeouts** (server accepted but is too slow)
- **application errors** (4xx/5xx responses)
- **corrupt/malformed responses** (partial payloads, invalid JSON)

---

## Timeout rules of thumb

- Always set a timeout.
- Use different timeouts for connect vs read if your client supports it.
- Make the timeout configurable.

Practical approach (Level 1):

- start with a conservative timeout (e.g., 30s)
- log timeouts distinctly from other failures
- if timeouts happen often, decide whether to:
  - reduce prompt size
  - switch models
  - increase timeout
  - add retries with backoff

---

## References

- Requests timeouts: https://requests.readthedocs.io/en/latest/user/quickstart/#timeouts
