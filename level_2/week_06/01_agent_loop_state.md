# Week 6 — Part 01: Agent loop and explicit state

## Overview

An agent is not a single prompt.

It is a controller that loops:

- plan
- call tool
- observe output
- decide next step

---

## Underlying theory: an agent is a policy over state

You can model an agent as a loop that maintains a state $s_t$ and chooses an action $a_t$.

- state $s_t$: what the agent currently knows (task, plan, tool results)
- action $a_t$: either “call a tool with arguments” or “stop and answer”

Conceptually:

$$
s_{t+1} = \mathrm{Update}(s_t, a_t, o_t)
$$

Where $o_t$ is the observation (tool output or error).

This framing matters because most agent bugs are *state bugs*:

- missing or corrupted state → repeated calls
- forgotten constraints → invalid tool inputs
- untracked errors → infinite loops

---

## State machine intuition (why stop conditions are mandatory)

If you view agent execution as a finite state machine, then each step should move the system forward:

- PLAN → TOOL_CALL → OBSERVE → DECIDE → (repeat)

Stop conditions are the “accepting states”:

- DONE (final answer)
- NEEDS_USER (clarify)
- FAILED (bounded failure)

Without explicit stop states, the loop can run forever.

## Minimum state to make explicit

- task
- plan (list of steps)
- steps[] (tool calls with inputs/outputs/errors)
- final output

---

## Why explicit state matters

Without explicit state, agents fail in ways that are hard to debug:

- “it forgot what it already tried”
- “it repeated the same tool call”
- “it hallucinated a tool result”

If state is explicit and logged, you can replay what happened.

Practical invariant:

- every tool output that influences decisions must be stored in state
- the final answer should be explainable from state (especially citations)

---

## Example state model (minimal)

```python
from dataclasses import dataclass, field

@dataclass
class Step:
    tool: str
    tool_input: dict
    tool_output: dict | None = None
    error: str | None = None
    latency_ms: int | None = None

@dataclass
class AgentState:
    task: str
    plan: list[str] = field(default_factory=list)
    steps: list[Step] = field(default_factory=list)
    final: str | None = None
```

This is enough to build and debug an agent loop.

---

## Minimal agent loop (pseudocode)

```text
state = {task, plan, steps=[], final=null}
plan = model.plan(task)
for step in plan:
  if stop_conditions: break
  tool_call = model.choose_tool(step)
  result = run_tool(tool_call)
  state.steps.append({tool_call, result})
final = model.write_final_answer(state)
return final
```

---

## Must-have stop conditions

- max steps reached
- tool fails repeatedly
- confidence low → ask user

Also consider:

- time budget exceeded
- repeated identical tool call detected
- tool output too large (truncate and continue safely)

---

## References

- LangChain docs: https://python.langchain.com/docs/
- LlamaIndex docs: https://docs.llamaindex.ai/en/stable/
- OpenAI function calling: https://platform.openai.com/docs/guides/function-calling
