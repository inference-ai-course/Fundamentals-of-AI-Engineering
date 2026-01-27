# Week 7 — Part 03: Error handling that teaches the user what to do

## Overview

Good error messages reduce support burden.

A good error message contains:

- what went wrong
- where it happened
- what to try next

---

## Underlying theory: errors are part of your product surface

When something fails, the error message becomes the user experience.

You can think of your program as an interface that returns either:

- a result
- or an explainable failure

Practical failure taxonomy (Level 1):

- **input errors** (missing/empty file, missing columns)
- **config errors** (missing API key)
- **external errors** (timeouts, rate limits)
- **output/parse errors** (invalid JSON from model)

Good errors point to the next action (fix input, set env var, retry later) instead of just crashing.

---

## Practical pattern

```python
from pathlib import Path


def require_file(path: str) -> Path:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(
            f"Input file not found: {p}. "
            "Check the path, or run with --help to see expected inputs."
        )
    if p.stat().st_size == 0:
        raise ValueError(f"Input file is empty: {p}. Provide a non-empty CSV.")
    return p
```

Practical tip: keep “user-facing” errors short and actionable. If you also want a stack trace for debugging, log the exception separately.

---

## Self-check

- If a beginner runs your project wrong, does the error message teach them what to do?

---

## References

- Python errors/exceptions: https://docs.python.org/3/tutorial/errors.html
