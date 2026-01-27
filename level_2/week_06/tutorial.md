# Level 2 — Week 6 Tutorials

## Overview

Week 6 introduces **agents**:

- agent loop (plan → act → observe → decide)
- explicit state
- tool contracts
- reliability behaviors (timeouts/retries/fallbacks)

## Navigation

- [01 — Agent loop + explicit state model](01_agent_loop_state.md)
- [02 — Tool contracts (schemas, validation, failure modes)](02_tool_contracts.md)
- [03 — Reliability behaviors + step logs (traceability)](03_reliability_step_logs.md)
- [04 — Minimal Agent v1 blueprint (2 tools)](04_agent_v1_blueprint.md)

## Recommended order

1. Read 01 and model state.
2. Read 02 and define tool schemas.
3. Read 03 and make behavior observable.
4. Implement 04.

Why this order works:

1. **State model first**
    - Agents are hard to debug when state is implicit. Make state a first-class object.
    - What to verify: your `state` includes task, plan, steps, and final.

2. **Tool schemas second**
    - Tools are APIs; without schemas/validation, you get garbage-in/garbage-out.
    - What to verify: invalid tool inputs fail fast with clear errors.

3. **Observability third**
    - Step logs let you answer: “what did the agent do, and why did it stop?”
    - What to verify: each tool call is logged with inputs, outputs, and error status.

4. **Blueprint last**
    - After contracts and logging exist, a minimal agent loop is straightforward and testable.
    - What to verify: you can show a successful trace and a trace that hits a stop condition.

## What “done” looks like

- You can explain the agent loop in your own words.
- You have an explicit `state` object that contains:
  - the task
  - the plan
  - a list of steps (tool call inputs/outputs)
  - the final answer
- You have hard stop conditions (max steps, time budget, retry limits).
- You can show a trace for:
  - a successful run
  - a failure run (and where it stopped)

## References

- OpenAI tool/function calling (concept): https://platform.openai.com/docs/guides/function-calling
- JSON Schema: https://json-schema.org/
- Tenacity (retries): https://tenacity.readthedocs.io/
