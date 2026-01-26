# Week 3 — Part 02: Prompts as API contracts

## Overview

A strong prompt is not “clever wording”. It’s a **specification**.

If you treat the model like a service, your prompt is the API contract.

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

---

## Common failure modes (and how contracts help)

- Vague prompt → vague output
- “Return JSON” without schema → almost-JSON
- No refusal conditions → hallucinated values

---

## Self-check

- Does your prompt define *exact keys*?
- Does it forbid extra text?
- Does it define what to do when info is missing?

---

## References

- Prompt engineering guide: https://www.promptingguide.ai/
- Anthropic cookbook: https://github.com/anthropics/anthropic-cookbook
