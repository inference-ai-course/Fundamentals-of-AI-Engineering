# Week 3 — Part 02: Prompts as API contracts

## Overview

A strong prompt is not “clever wording”. It’s a **specification**.

If you treat the model like a service, your prompt is the API contract.

---

## Pre-study (Level 0)

Level 1 assumes Level 0 is complete. If you need a refresher on prompt engineering fundamentals, guardrails, and evaluation mindset:

- [Pre-study index (Level 1 → Level 0)](../PRESTUDY.md)
- [Level 0 — Prompt engineering and evaluation](../../level_0/Chapters/3/02_prompt_engineering_evaluation.md)
- [Level 0 — Structured outputs and schemas](../../level_0/Chapters/3/01_function_calling_structured_outputs.md)

Why it matters here (Week 3):

- Treat prompts as specs so you can write a deterministic parser/validator.
- If you can’t validate the output shape, the contract is not concrete enough.

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
