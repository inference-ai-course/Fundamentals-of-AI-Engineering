# Week 3 — Part 03: Structured outputs (JSON) — parse + validate + retry/repair

## Overview

Models can produce:

- valid JSON
- almost-JSON (single quotes, trailing commas, extra prose)

Downstream code needs a **pass/fail** signal.

So we implement:

1. ask for strict JSON
2. parse it
3. validate schema
4. if invalid, retry with a repair prompt (capped)

A concrete example of the target output shape:

```json
{"person": "Ada Lovelace", "company": null}
```

The important engineering point: downstream code should never need to “guess” if the output is valid. It should be able to fail fast or proceed.

---

## Pre-study (Self-learn)

Foundations Course assumes Self-learn is complete. If you need a refresher on structured outputs, schemas, and validation mindset:

- [Pre-study index (Foundations Course → Self-learn)](../PRESTUDY.md)
- [Self-learn — Structured outputs and schemas](../self_learn/Chapters/3/01_function_calling_structured_outputs.md)

Why it matters here (Week 3):

- Treat LLM output as untrusted text until it passes parse + schema validation.
- Validation gives downstream code a deterministic pass/fail boundary.

---

## Step 1: Define a schema (Pydantic)

Install:

```bash
pip install pydantic
```

Schema:

```python
from typing import Optional

from pydantic import BaseModel


class Extracted(BaseModel):
    person: Optional[str]
    company: Optional[str]
```

---

## Step 2: Parse + validate

```python
import json
from pydantic import ValidationError


def parse_and_validate(model_text: str) -> Extracted:
    data = json.loads(model_text)
    return Extracted.model_validate(data)
```

This will fail in two different ways:

- `json.loads` fails → not JSON
- `model_validate` fails → wrong schema

That separation helps debugging.

Example failures you should expect during development:

- Parse failure (not JSON):
  - model output contains extra text like `Here is the JSON:` or uses single quotes.
- Schema failure (wrong shape):
  - model returns `{"name": "..."}` instead of `{"person": "..."}`.

A practical habit that helps: save the raw model output to disk (e.g., `output/llm_raw.txt`) whenever parsing/validation fails, so you can inspect what the model actually produced.

Practical implication:

- if parsing fails, your prompt/formatting constraints are the issue
- if schema validation fails, your prompt/spec is incomplete or the model is hallucinating keys/types

---

## Step 3: Retry/repair loop

Below is a provider-agnostic design.

You supply `call_llm(prompt: str) -> str`.

```python
def extract_with_repair(text: str, call_llm, max_retries: int = 2) -> Extracted:
    base_prompt = (
        "You are an information extraction engine.\n"
        "Return ONLY valid JSON with keys person, company.\n"
        "Use null when unknown.\n\n"
        f"Input:\n{text}\n"
    )

    last_error = None  # type: Optional[str]

    prompt = base_prompt
    for attempt in range(max_retries + 1):
        raw = call_llm(prompt)
        try:
            return parse_and_validate(raw)
        except (json.JSONDecodeError, ValidationError) as e:
            last_error = str(e)
            prompt = (
                "Your previous output was invalid.\n"
                "Fix it and return ONLY valid JSON with keys person, company.\n"
                f"Invalid output was:\n{raw}\n\n"
                f"Validation/parsing error:\n{last_error}\n"
            )

    raise ValueError(f"Failed to extract valid JSON after retries. Last error: {last_error}")
```

Why the repair prompt includes the invalid output and the error:

- the invalid output is concrete evidence of what went wrong
- the error message is a compact “diff target” (what must be fixed)

This pattern is the simplest version of an **inner correction loop**.

---

## Why cap retries

Retries are for transient failures and formatting drift.

If you retry forever:

- you waste money
- you can get stuck

A cap forces you to:

- fall back
- return a clear error
- log the incident

Also, retries can amplify load and cost. Even a small retry rate changes expected spend:

$$
\mathbb{E}[\text{attempts}] = 1 + p + p^2 + \cdots + p^{R} = \frac{1-p^{R+1}}{1-p}
$$

where $p$ is the probability an attempt fails and $R$ is the max retries.

---

## Common pitfalls

- Asking for JSON but not banning extra text
- Not separating parse failure vs schema failure
- No retry cap

- Mixing business logic with parsing/validation
  - Fix: keep “call model”, “parse JSON”, and “validate schema” as separate steps so you can test/debug each one.

---

## References

- JSON Schema: https://json-schema.org/
- Python `json`: https://docs.python.org/3/library/json.html
- Pydantic: https://docs.pydantic.dev/latest/
- Tenacity (retry patterns): https://tenacity.readthedocs.io/
