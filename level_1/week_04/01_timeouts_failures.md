# Week 4 — Part 01: Timeouts and failure modes

## Overview

A timeout is the simplest reliability feature:

- Without a timeout, your program can hang forever.
- With a timeout, you turn “unknown waiting” into a controlled failure.

---

## Why requests fail in real systems

Common failure types:

- DNS issues
- network drops
- provider overload
- slow responses
- malformed responses

Your code should assume *some* requests will fail.

---

## Timeout rules of thumb

- Always set a timeout.
- Use different timeouts for connect vs read if your client supports it.
- Make the timeout configurable.

---

## References

- Requests timeouts: https://requests.readthedocs.io/en/latest/user/quickstart/#timeouts
