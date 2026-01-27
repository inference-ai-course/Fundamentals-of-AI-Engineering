# Level 2 — Week 7 Tutorials

## Overview

Week 7 extends agents with design patterns and guardrails:

- planning depth control
- guardrails (allowlist, budgets)
- trace-style logs for debugging
- one multi-step task capability (research report / reviewer / self-check)

## Navigation

- [01 — Planning patterns (fixed plan vs replanning)](01_planning_patterns.md)
- [02 — Guardrails (allowlists, budgets, refusal conditions)](02_guardrails.md)
- [03 — Trace-style debugging (how to read agent traces)](03_trace_debugging.md)

## Recommended order

1. Read 01 and implement a step cap.
2. Read 02 and restrict tool usage.
3. Read 03 and make traces interpretable.

## What “done” looks like

- Your agent has a max step cap and a time budget.
- Your agent uses a tool allowlist and rejects unknown tools.
- Retrieved content is treated as data (not instructions).
- You can show a trace for:
  - a normal run
  - a run that hits a guardrail (step cap / timeout / refusal)

## References

- OWASP LLM Top 10: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- OpenAI safety guide: https://platform.openai.com/docs/guides/safety
