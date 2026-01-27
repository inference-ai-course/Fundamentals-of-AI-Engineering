# Week 3 — Part 02: Prompts as API contracts

## Overview

A strong prompt is not “clever wording”. It’s a **specification**.

If you treat the model like a service, your prompt is the API contract.

---

## Underlying theory: prompts define preconditions and postconditions

In software engineering, a contract describes:

- **preconditions**: what inputs are valid
- **postconditions**: what outputs must look like

For LLMs, prompts play a similar role:

- the prompt defines the task and constraints
- your parser/validator enforces the postconditions

Useful mindset: treat an LLM call like a typed function.

Example (conceptually):

$$
\texttt{extract}: \texttt{str} \rightarrow \{\texttt{person}: \texttt{str|null},\ \texttt{company}: \texttt{str|null}\}
$$

The model is not guaranteed to respect the type. Your job is to *make the type checkable*.

---

## Contract template

A useful contract includes:

- **Role**: what the model is doing
- **Task**: what to produce
- **Input format**: what you will provide
- **Output schema**: exact JSON keys and types
- **Constraints**:
  - no extra keys
  - no markdown
  - no commentary
- **Refusal conditions**: when to output an error object

---

## Example: extraction contract

Input: unstructured text

Output: strict JSON

```text
You are an information extraction engine.

Task:
Extract a person and company name from the input.

Output format:
Return ONLY valid JSON with exactly these keys:
{
  "person": string | null,
  "company": string | null
}

Constraints:
- No markdown
- No additional keys
- Use null if not found

Input:
"<TEXT>"
```

Why the contract is structured this way:

- “Return ONLY valid JSON” tries to eliminate ambiguous prose
- “exactly these keys” makes it possible to validate reliably
- “Use null if not found” prevents hallucinated values from looking like real facts

---

## Common failure modes (and how contracts help)

- Vague prompt → vague output
- “Return JSON” without schema → almost-JSON
- No refusal conditions → hallucinated values

Additional common failures:

- too many constraints at once (the model drops one)
- conflicting instructions across system/developer/user messages
- hidden formatting requirements (e.g., “no markdown”) not explicitly stated

Practical implication: if you can’t write a validator for the output, your contract is not concrete enough.

---

## Self-check

- Does your prompt define *exact keys*?
- Does it forbid extra text?
- Does it define what to do when info is missing?

---

## References

- Prompt engineering guide: https://www.promptingguide.ai/
- Anthropic cookbook: https://github.com/anthropics/anthropic-cookbook
