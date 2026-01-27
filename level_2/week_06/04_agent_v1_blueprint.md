# Week 6 — Part 04: Minimal Agent v1 blueprint (2 tools)

## Overview

A minimal agent should:

- plan a small sequence
- call 2 tools
- capture all intermediate results
- stop safely

---

## Suggested Agent v1 workflow

Tools:

- `search` (retrieve chunks)
- `write_answer` (generate grounded answer with citations)

Steps:

1. Plan: decide to search, then answer.
2. Call `search`.
3. Call `write_answer` with the retrieved chunks.
4. Validate citations.
5. Return final.

---

## Correctness invariants (what makes this an agent, not a demo)

- Every tool call is recorded in `state.steps` (inputs + outputs + errors).
- The agent never assumes a tool succeeded.
  - it checks for errors/empty results and chooses a safe next action.
- If the agent returns an answer with citations, those citations must be traceable to retrieved chunks.

---

## Minimal decision rule (stop vs clarify)

Before calling `write_answer`, decide whether retrieval is “good enough”.

Example rule (conceptual):

- if `hits` is empty → `mode=clarify`
- else → continue to `write_answer`

Later you can incorporate score thresholds (Week 4) and eval-driven tuning (Week 5).

## Minimal blueprint (code-shaped)

This is intentionally framework-agnostic. The point is the structure.

```python
def agent_run(task: str) -> dict:
    state = {
        "task": task,
        "plan": ["search", "write_answer"],
        "steps": [],
        "final": None,
    }

    # Step 1: search
    search_in = {"query": task, "top_k": 5}
    search_out = tool_search(search_in)
    state["steps"].append({"tool": "search", "input": search_in, "output": search_out})

    # Step 2: write grounded answer
    answer_in = {"question": task, "chunks": search_out.get("hits", [])}
    answer_out = tool_write_answer(answer_in)
    state["steps"].append({"tool": "write_answer", "input": answer_in, "output": answer_out})

    # Step 3: validate and finish
    state["final"] = answer_out
    return state
```

If you can log and inspect `state`, you can debug agent behavior.

---

## Self-check

- Do you cap steps?
- Can you show logs for a failure and recovery?

---

## References

- OpenAI function calling: https://platform.openai.com/docs/guides/function-calling
