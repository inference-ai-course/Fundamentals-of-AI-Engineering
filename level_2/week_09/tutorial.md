# Level 2 — Week 9 Tutorials

## Overview

Week 9 is about hardening and ops:

- tracing/observability
- rate limiting
- basic security posture
- cost controls

Underlying theory you should internalize this week:

- observability exists to connect symptoms to causes (logs explain events; traces explain time)
- percentiles (p50/p95) matter more than averages for user experience
- retries and agents amplify load; rate limits and budgets reduce blast radius

## Navigation

- [01 — Observability package (logs, request IDs, traces)](01_observability_tracing.md)
- [02 — Rate limiting + retry policies](02_rate_limiting_retry_policies.md)
- [03 — Ops checklist (what to monitor, how to debug)](03_ops_checklist.md)

## Recommended order

1. Read 01 and make latency debuggable.
2. Read 02 and control abuse/cost.
3. Read 03 and write the ops checklist.

## What “done” looks like

- Every request has a `request_id` in logs and in responses.
- You can answer “where did time go?” for `/chat`:
  - retrieval latency
  - model latency
  - total latency
- Expensive endpoints are rate-limited.
- Retries are bounded and use exponential backoff.
- You have a written runbook (ops checklist) that explains how to debug common failures.

## References

- OpenTelemetry docs: https://opentelemetry.io/docs/
- W3C Trace Context: https://www.w3.org/TR/trace-context/
- HTTP 429: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429
