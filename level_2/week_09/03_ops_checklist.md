# Week 9 — Part 03: Ops checklist (what to monitor, how to debug)

## Overview

An ops checklist is your “runbook”.

It should answer:

- what can fail
- what to monitor
- how to debug
- how to control cost

---

## Underlying theory: error budgets and leading indicators

If you set an SLO like “99% success”, you are implicitly allowing a 1% error budget.

You can treat the error budget as a signal:

- if you are burning budget fast, you stop shipping changes and stabilize

For course projects, the same idea applies:

- if error rate spikes during a demo, prioritize safe fallbacks (clarify/refuse)

Leading indicators to watch for RAG systems:

- retrieval hit rate drops
- refusal rate spikes (often indicates index/filters broken)
- context size spikes (often indicates runaway packing)
- 429/timeout rates spike (often indicates retry storms)

---

## Template

```md
# Ops checklist

## What to monitor

- latency (p50/p95)
- error rate
- model calls / cost
- refusal rate

## Where failures happen

- ingest
- search
- chat
- agent

## Debug procedure

1. **Find `request_id`**
    - Start from the user-visible failure (HTTP response, CLI output) and locate the request identifier.
    - If you do not have a `request_id`, add one. Debugging without it becomes guessing.

2. **Inspect logs by component**
    - Split logs by stage: ingest → search/retrieve → chat/generate → validate.
    - Look for the first error in the trace, not the last error in the cascade.

3. **Check retrieval hits**
    - Confirm retrieval returned any chunks.
    - If hits are empty, the safest behavior is to clarify/refuse rather than hallucinate.

4. **Check model errors**
    - Separate “provider failed” (timeouts/429/5xx) from “model answered but invalid” (bad JSON, missing citations).
    - If 429 rates spike, reduce concurrency and ensure retries have backoff.

## Cost controls

- token caps
- context caps
- rate limits
```

---

## Add a “first response” playbook

When something is wrong in a demo or production-ish run:

1. Identify the failing endpoint and capture the `request_id`.
2. Check the HTTP status code (4xx vs 5xx).
3. For `/chat` failures:
    - check retrieval returned chunks
    - check model call succeeded
    - check citation validation
4. Decide the safest fallback (clarify/refuse) instead of hallucinating.

Example “triage” outcomes:

- If retrieval returns zero hits for known in-KB questions, suspect ingestion/indexing or metadata filters.
- If retrieval hits exist but the answer is wrong, suspect context assembly (ordering, truncation, missing chunk text).
- If the answer is correct but citations are missing, suspect citation enforcement and output validation.

Principle:

- always identify which stage failed first: retrieve → generate → validate

---

## References

- Python logging: https://docs.python.org/3/library/logging.html
- Google SRE book: https://sre.google/sre-book/table-of-contents/
