# Level 2 — Week 7: Agent Design Patterns (Planning, Guardrails, and Multi-Step Tasks)

## What you should be able to do by the end of this week

- Apply agent patterns: planning depth control, role prompting, self-check/rewrite.
- Add guardrails: tool allowlists, refusal conditions, budget limits.
- Debug agents using trace-style logs (step-by-step decisions).

Practice notebook: [practice.ipynb](practice.ipynb)

## Key Concepts (with explanations + citations)

### 1) Planning depth control

**Mental model**:

- Plans can be too shallow (miss steps) or too deep (waste tokens/time).
- Use checkpoints: stop after N steps or when confidence is low.

**Planning patterns to demonstrate**:

- Fixed plan:
  - generate a plan once, then execute
- Re-planning:
  - update the plan after tool outputs
- Budgeted planning:
  - cap plan length and step count to avoid runaway loops

Citations:

- https://python.langchain.com/docs/
- https://docs.llamaindex.ai/en/stable/

### 2) Guardrails

**Mental model**:

- Tool allowlists: the model can only call approved tools.
- Budget limits: cap steps, time, and cost to prevent runaway loops.
- Refusal conditions: do not execute risky actions without user approval.

**Guardrails to implement first (order matters)**:

- Allowlist:
  - hard-code allowed tool names
- Step cap:
  - stop after N steps
- Timeout cap:
  - stop after T seconds
- Budget cap:
  - stop after estimated cost/token budget

**Prompt-injection reality (teach with one demo)**:

- Retrieved text can contain instructions that try to override your system.
- Rule: retrieved documents are data, not instructions.

Citations:

- https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
- https://owasp.org/www-project-top-10-for-large-language-model-applications/

### 3) Debugging agents with traces

**Mental model**:

- Trace each step: plan, tool call inputs, tool outputs, decision.
- This makes failures diagnosable instead of mysterious.

**What a good trace contains**:

- `request_id`
- `step_index`
- `model_input_summary` (not necessarily full prompt)
- `tool_call`
- `tool_result`
- `decision`

**How to use traces in teaching**:

- Ask students to explain:
  - why the agent chose a tool
  - why it stopped
  - what went wrong and how to fix

Citations:

- https://docs.python.org/3/library/logging.html
- https://opentelemetry.io/docs/languages/python/

## Common pitfalls

- Infinite loops (no step/budget caps).
- Adding multi-agent too early without a stable single-agent baseline.

## Workshop / Implementation Plan

- Add a guardrail (allowlist + step cap + budget cap).
- Add a trace view (print step-by-step actions and outputs).
- Run 3 demo tasks and capture logs.

## Figures (Comprehensive Overviews — Leave Blank)

### Figure A: System architecture overview


### Figure B: Data and control flow (ingestion -> retrieval -> generation -> evaluation)


## Self-check questions

- Can you debug the agent by reading step traces?
- Do guardrails prevent risky tool calls?
