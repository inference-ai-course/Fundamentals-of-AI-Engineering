# Week 7 — Part 03: Error handling that teaches the user what to do

## Overview

Good error messages reduce support burden.

A good error message contains:

- what went wrong
- where it happened
- what to try next

---

## Pre-study (Level 0)

Level 1 assumes Level 0 is complete. If you need a refresher on exceptions and debugging patterns:

- [Pre-study index (Level 1 → Level 0)](../PRESTUDY.md)
- [Level 0 — Modules and exception handling](../../level_0/Chapters/2/02_modules_exceptions.md)

Why it matters here (Week 7):

- Errors are part of your product surface: they should tell the user what to do next.
- Prefer short, actionable user-facing errors; log deeper details separately.

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
