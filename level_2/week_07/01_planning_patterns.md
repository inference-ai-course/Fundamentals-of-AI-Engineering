# Week 7 — Part 01: Planning patterns (fixed plan vs replanning)

## Overview

Plans can be:

- too shallow (miss steps)
- too deep (waste tokens/time)

You need depth control.

---

## Underlying theory: planning is search under a budget

You can think of planning as choosing a sequence of actions that reduces uncertainty until you can answer.

- actions are tool calls or “write final answer”
- each action has a cost (latency, tokens, risk)

If a plan has steps $a_1, \ldots, a_T$, you can think in terms of a simple budgeted objective:

$$
\max_{a_{1:T}} \; \mathrm{Utility}(a_{1:T}) \quad \text{s.t.} \quad \mathrm{Cost}(a_{1:T}) \le B
$$

You don’t need to solve this optimally; the point is that:

- deeper planning increases cost
- shallow planning increases failure probability

So “depth control” is the core engineering problem.

---

## Decomposition intuition (why plans help)

Many tasks are easier if you decompose:

- What must I know to answer?
- Which tool can provide that?
- What is the next unknown after I observe tool output?

This is why planning often improves tool-use reliability: it turns an unstructured prompt into explicit intermediate goals.

## Patterns

- Fixed plan: plan once then execute
- Replanning: update after tool outputs
- Budgeted planning: cap plan length and steps

---

## Fixed plan template

Works best when the task is predictable.

```text
1. Identify required information
2. Call tools to gather it
3. Synthesize answer
4. Self-check against requirements
```

Failure mode: if tool output surprises you, the plan becomes wrong.

When to prefer fixed plans:

- tasks with predictable tool outputs
- small number of tools
- low branching factor (not many possible next steps)

---

## Replanning template

After each tool call:

- update what you know
- update remaining steps
- stop early if task is done

This pattern prevents wasted steps.

When to prefer replanning:

- tool outputs often change what you should do next
- you need conditional logic (if hits empty → clarify)
- you want early stopping when the evidence is sufficient

---

## Budgeted planning template

Decide budgets up front:

- max_plan_steps: e.g., 5
- max_tool_calls: e.g., 6
- max_runtime_seconds: e.g., 30

If the budget is hit, switch to:

- ask the user for clarification
- or return best-effort partial output + what is missing

This is how you prevent runaway agents.

Practical heuristic:

- pick budgets so worst-case cost is acceptable
- prefer “best effort + ask user” over silently looping

---

## References

- OpenAI function calling: https://platform.openai.com/docs/guides/function-calling

---

## Self-check

- Does your agent stop after N steps?
- Does it ask user when confidence is low?
