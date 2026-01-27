# Week 7 — Part 03: Trace-style debugging

## Overview

If you cannot explain why the agent chose a tool, you don’t control it.

Traces make behavior diagnosable.

---

## Underlying theory: a trace is a causal explanation

An agent step is a decision made from inputs.

If you cannot explain a decision, you cannot control or improve the system.

You can think of each step as:

$$
\text{decision}_t = \pi(s_t)
$$

Where $s_t$ is the state (task, plan, retrieved evidence summaries, error history).

So a trace must record enough of $s_t$ to explain why $\pi$ chose that decision.

---

## What a good trace contains

- request_id
- step_index
- tool call
- tool result
- decision

Optionally:

- model_input_summary

Practical rule:

- if you cannot reproduce the decision from the trace, the trace is missing critical fields

---

## Trace example (shape)

```json
{
  "request_id": "...",
  "steps": [
    {
      "step_index": 1,
      "plan": ["search", "write_answer"],
      "decision": "call_search"
    },
    {
      "step_index": 2,
      "tool": "search",
      "input": {"query": "...", "top_k": 5},
      "output_summary": "5 hits"
    },
    {
      "step_index": 3,
      "decision": "write_answer_with_citations"
    }
  ]
}
```

Make traces easy to read:

- keep `output_summary` short
- store full outputs separately if needed

---

## How to use traces

Ask:

- what was the plan?
- what did the tool return?
- why did the agent choose the next step?
- why did it stop?

---

## Common trace-based diagnoses

- repeated tool call with same input → missing “already tried” state
- invalid tool inputs → schema not enforced or constraints not in the prompt
- early stopping with insufficient evidence → weak stop criteria
- long tail latency → retry/backoff misconfigured or tool timeout too high

---

## References

- OpenTelemetry Python: https://opentelemetry.io/docs/languages/python/
- Python logging: https://docs.python.org/3/library/logging.html
- W3C trace context: https://www.w3.org/TR/trace-context/
