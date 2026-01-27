# Week 9 — Part 01: Observability and tracing

## Overview

- Logs + request IDs answer: “what happened?”
- Traces answer: “where did time go?”

Instrument:

- retrieval queries
- model calls
- agent steps

---

## Underlying theory: SLIs, SLOs, and why observability exists

### SLIs (what you measure)

An SLI (service level indicator) is a measurable quantity like:

- request latency
- error rate
- availability

### SLOs (what you promise)

An SLO is a target on an SLI, for example:

- 99% of `/chat` requests complete within 2 seconds
- error rate under 1% over a day

You don’t need full SRE practice for the course, but you should think in these terms because it forces clarity.

### Why percentiles (p50/p95) matter

Average latency hides tail problems.

- p50 tells you the typical case
- p95 tells you whether a meaningful fraction of users are suffering

In LLM systems, tail latency is common (network calls + retries + variable model times), so percentiles are more informative than means.

---

## Minimum observability package

- structured logs including request_id + component
- key counters:
  - ingestion docs/chunks
  - retrieval top_k and context length
  - model calls count
  - refusal rate

---

## Minimum log fields (practical)

Log at least:

- `request_id`
- `path`
- `status_code`
- `latency_ms`
- `component` (ingest/search/chat/agent)

For chat/RAG specifically:

- `top_k`
- `n_chunks_returned`
- `context_chars` or `context_tokens`
- `model_name`

---

## Tracing mental model

A trace is a tree of spans:

- root span: the HTTP request
- child span: retrieval
- child span: model call
- child span: citation validation

Even if you don’t deploy a full tracing backend, logging span durations gives you 80% of the value.

Theory intuition:

- a trace decomposes total latency into span costs
- the slowest path through dependent spans is the critical path

This is how you decide whether to optimize retrieval, model calls, or validation.

---

## References

- OpenTelemetry Python: https://opentelemetry.io/docs/languages/python/
- W3C trace context: https://www.w3.org/TR/trace-context/
- Logging in Python: https://docs.python.org/3/library/logging.html
