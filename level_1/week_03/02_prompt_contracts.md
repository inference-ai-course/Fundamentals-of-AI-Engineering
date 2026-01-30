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

### Example inputs and expected outputs

**Input 1**: "Ada Lovelace worked at the Analytical Engine Company."

**Expected output**:
```json
{"person": "Ada Lovelace", "company": "Analytical Engine Company"}
```

**Input 2**: "The project was completed successfully."

**Expected output**:
```json
{"person": null, "company": null}
```

**Input 3**: "John from Acme Corp sent an email."

**Expected output**:
```json
{"person": "John", "company": "Acme Corp"}
```

---

## Common failure modes (and how contracts help)

### Failure 1: Vague prompt → vague output

**Bad prompt**:
```text
Extract names from this text.
```

**Model output** (unpredictable):
```
The person is Ada Lovelace and the company is Analytical Engine Company.
```

or

```json
{"names": ["Ada Lovelace", "Analytical Engine Company"]}
```

or

```
- Ada Lovelace
- Analytical Engine Company
```

**Problem**: No output format specified, so the model guesses.

**Fix**: Use the contract above with exact schema.

---

### Failure 2: "Return JSON" without schema → almost-JSON

**Weak prompt**:
```text
Extract person and company. Return JSON.
```

**Model output** (common failures):
```json
{
  'person': 'Ada Lovelace',  // Single quotes (invalid JSON)
  'company': 'Analytical Engine Company',
}  // Trailing comma (invalid JSON)
```

or

```markdown
Here is the JSON:
{"person": "Ada Lovelace", "company": "Analytical Engine Company"}
```

**Problem**: Model adds markdown wrapper or uses JavaScript-style syntax.

**Fix**: Add "No markdown" and "ONLY valid JSON" constraints.

---

### Failure 3: No refusal conditions → hallucinated values

**Input**: "The meeting was productive."

**Weak prompt output**:
```json
{"person": "Unknown", "company": "Unknown"}
```

**Problem**: Model invents placeholder values instead of using `null`.

**Fix**: Explicitly state "Use null if not found" in the contract.

---

### Failure 4: Too many constraints at once

**Overloaded prompt**:
```text
Extract person, company, date, location, sentiment, entities, topics, and keywords.
Return JSON with no markdown, no extra keys, use null for missing values,
ensure dates are in ISO format, locations are geocoded, sentiment is -1 to 1...
```

**Problem**: Model drops some constraints or gets confused.

**Fix**: Start simple, test, then add constraints incrementally.

---

### Failure 5: Conflicting instructions

**System message**: "Be conversational and helpful."

**User prompt**: "Return ONLY JSON, no extra text."

**Model output**:
```
Here's the information you requested:
{"person": "Ada Lovelace", "company": null}
I hope this helps!
```

**Problem**: System message encourages prose, user prompt forbids it.

**Fix**: Align system and user instructions. For extraction, system should be task-focused, not conversational.

---

## Iterative contract improvement

Start simple, test, refine:

**Version 1** (too vague):
```text
Extract names from the text.
```

Test → fails (format inconsistent).

**Version 2** (better):
```text
Extract person and company names. Return JSON.
```

Test → fails (markdown wrapper, invalid syntax).

**Version 3** (explicit):
```text
Extract person and company. Return ONLY valid JSON.
No markdown. Keys: person, company. Use null if missing.
```

Test → works most of the time, occasional extra keys.

**Version 4** (final):
```text
You are an information extraction engine.

Task: Extract a person and company name from the input.

Output format:
Return ONLY valid JSON with exactly these keys:
{"person": string | null, "company": string | null}

Constraints:
- No markdown
- No additional keys
- Use null if not found

Input: "<TEXT>"
```

Test → reliable.

---

## Contract validation checklist

Before deploying a prompt, verify:

- [ ] Does it specify exact output keys?
- [ ] Does it forbid extra text/markdown?
- [ ] Does it define behavior for missing data?
- [ ] Can you write a schema validator (e.g., Pydantic)?
- [ ] Have you tested with edge cases (empty input, all nulls)?

Practical implication: if you can't write a validator for the output, your contract is not concrete enough.

---

## Self-check

- Does your prompt define *exact keys*?
- Does it forbid extra text?
- Does it define what to do when info is missing?

---

## References

- Prompt engineering guide: https://www.promptingguide.ai/
- Anthropic cookbook: https://github.com/anthropics/anthropic-cookbook
