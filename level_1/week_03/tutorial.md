# Level 1 — Week 3 Tutorials

## Pre-study (Level 0)

Level 1 assumes Level 0 is complete. If you need a refresher:

- [Pre-study index (Level 1 → Level 0)](../PRESTUDY.md)
- [Level 0 — Chapter 3: AI Engineering Fundamentals](../../level_0/Chapters/3/Chapter3.md)

## Overview

These tutorials expand Week 3 into practical LLM engineering skills:

- tokens + context windows (why long inputs fail)
- prompts as contracts
- strict JSON outputs
- validation + retry/repair patterns

## Navigation

- [01 — Tokens and context windows (practical intuition)](01_tokens_context.md)
- [02 — Prompts as API contracts (design patterns)](02_prompt_contracts.md)
- [03 — Structured outputs: JSON parsing + validation + retry/repair](03_structured_outputs_validation.md)

## Recommended order

1. Read 01 for the mental model (this prevents many “why did the model ignore me?” issues).
2. Read 02 and write prompts as specs.
3. Read 03 and implement validation + repair.

Use [practice.ipynb](practice.ipynb) for additional hands-on work.

Why this order works:

1. **Tokens/context first**
    - Many failures look like “the model is dumb”, but are actually context overflow or truncation.
    - What to verify: you can estimate whether your input will fit (prompt + context + output).

2. **Prompt contracts second**
    - Treat the prompt like an API spec: define inputs, outputs, and constraints.
    - What to verify: your prompt includes explicit output requirements (e.g., exact JSON keys, allowed values).

3. **Validation + repair third**
    - LLMs are probabilistic; you need a deterministic wrapper (parse/validate/retry) for reliability.
    - What to verify: invalid JSON triggers a retry/repair path with a hard retry limit.
