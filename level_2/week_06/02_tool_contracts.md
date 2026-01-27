# Week 6 — Part 02: Tool contracts (schemas, validation, failure modes)

## Overview

Tools are mini-APIs.

A tool contract must define:

- name
- input schema
- output schema
- failure modes

This makes tool calls safer and easier to debug.

---

## Underlying theory: tools are typed functions

You can think of a tool as a function with a type signature:

$$
f: X \rightarrow Y
$$

Where:

- $X$ is the input schema (valid JSON shape + constraints)
- $Y$ is the output schema

Schema validation is “type checking” for agents.

### Preconditions and postconditions

For reliability, define:

- preconditions: what must be true before executing the tool
- postconditions: what the tool guarantees on success

Example for `search`:

- preconditions: `query` non-empty, `top_k` within bounds
- postconditions: `hits` is a list, each hit has `chunk_id` and `score`

This makes tool failures legible and recoverable.

---

## Failure mode taxonomy (what agents need to distinguish)

- invalid input (agent bug) → do not retry, fix arguments
- transient failure (timeouts, 429) → bounded retry with backoff
- permanent failure (401/403, missing index) → stop or escalate
- empty result (valid but unhelpful) → choose a different action (reformulate query, ask user)

## Tool contract template

- Tool: `search`
  - input: `{query: str, top_k: int, filters?: dict}`
  - output: `{hits: [...], errors?: ...}`

- Tool: `summarize`
  - input: `{text: str, style: str}`
  - output: `{summary: str}`
 
---
 
## Example: JSON Schema for a tool
 
A tool schema is just a machine-readable contract.
 
```json
{
  "name": "search",
  "description": "Retrieve top-k chunks for a query",
  "input_schema": {
    "type": "object",
    "properties": {
      "query": {"type": "string", "minLength": 1},
      "top_k": {"type": "integer", "minimum": 1, "maximum": 50},
      "filters": {"type": ["object", "null"]}
    },
    "required": ["query"]
  }
}
```
 
Why this matters:
 
- you can validate inputs before executing
- you can generate documentation
- you can build safer agent prompts (“call tools only with valid JSON”)

---

## Validation rule

Validate inputs **before** running tool code.

If invalid:

- fail fast
- return a clear error
 
Treat “invalid tool input” as a normal failure mode, not an exception.
Agents should be able to recover from it.

---

## References

- JSON Schema: https://json-schema.org/
- OpenAI structured outputs: https://platform.openai.com/docs/guides/structured-outputs
