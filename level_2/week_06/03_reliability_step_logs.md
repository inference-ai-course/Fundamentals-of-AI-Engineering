# Week 6 — Part 03: Reliability + step logs (traceability)

## Overview

Agents amplify failures:

- more calls
- more chances to hang
- more hidden state

So reliability is non-negotiable.

---

## Reliability rules

- all network calls have timeouts
- retries are bounded + backoff
- tool failures have fallbacks
- every step is logged

Practical warning:

- retries without a cap can create infinite loops
- retries without backoff can create thundering herds

---

## Underlying theory: retries trade latency for success probability

If each independent attempt succeeds with probability $p$, then after $n$ attempts the probability of at least one success is:

$$
P(\text{success by } n) = 1 - (1-p)^n
$$

This is why limited retries can dramatically improve reliability.

But retries also increase load and can worsen outages, which is why backoff and caps matter.

---

## Exponential backoff intuition (why it helps)

A common schedule is:

$$
\text{delay}_k = \min(\text{cap}, \text{base} \cdot 2^k)
$$

Where $k$ is the retry index.

Why it helps:

- it reduces request rate during outages
- it gives downstream systems time to recover

### Jitter (randomness) prevents synchronization

If many clients retry on the same schedule, they can synchronize and repeatedly spike traffic.
Random jitter breaks synchronization so retries spread out over time.

## Step log fields

Log each step as a structured object:

- request_id
- step_index
- tool
- input
- output
- error
- latency

---

## Step log example (JSON)

```json
{
  "request_id": "...",
  "step_index": 2,
  "tool": "search",
  "input": {"query": "...", "top_k": 5},
  "output": {"hits": [{"chunk_id": "...", "score": 0.82}]},
  "error": null,
  "latency_ms": 183
}
```

Keep step logs machine-readable. It makes debugging and later evaluation much easier.

---

## Bounded retry pattern (concept)

- retry only on transient failures (timeouts, 429, network errors)
- do not retry on invalid inputs
- after the last retry, fall back or stop with a clear error

---

## References

- Tenacity: https://tenacity.readthedocs.io/
- Requests timeouts: https://requests.readthedocs.io/en/latest/user/quickstart/#timeouts
- W3C trace context: https://www.w3.org/TR/trace-context/
- Exponential backoff (AWS): https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/
