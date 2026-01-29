# Week 4 — Part 01: Timeouts and failure modes

## Overview

A timeout is the simplest reliability feature:

- Without a timeout, your program can hang forever.
- With a timeout, you turn “unknown waiting” into a controlled failure.

---

## Pre-study (Level 0)

Level 1 assumes Level 0 is complete. If you need a refresher on reliability/operations and debugging practices:

- [Pre-study index (Level 1 → Level 0)](../PRESTUDY.md)
- [Level 0 — Chapter 5: Resource Monitoring and Containerization](../../level_0/Chapters/5/Chapter5.md)

Why it matters here (Week 4):

- Timeouts are the simplest way to prevent a single bad request from freezing your whole script.
- A timeout turns “unknown waiting” into a controlled, debuggable failure.

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
