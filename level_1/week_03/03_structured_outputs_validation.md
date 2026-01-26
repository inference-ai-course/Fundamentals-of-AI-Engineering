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

---

## Step 1: Define a schema (Pydantic)

Install:

```bash
pip install pydantic
```

Schema:

```python
from pydantic import BaseModel


class Extracted(BaseModel):
    person: str | None
    company: str | None
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

    last_error: str | None = None

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

---

## Common pitfalls

- Asking for JSON but not banning extra text
- Not separating parse failure vs schema failure
- No retry cap

---

## References

- JSON Schema: https://json-schema.org/
- Python `json`: https://docs.python.org/3/library/json.html
- Pydantic: https://docs.pydantic.dev/latest/
- Tenacity (retry patterns): https://tenacity.readthedocs.io/
