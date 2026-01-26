# Week 7 — Part 03: Error handling that teaches the user what to do

## Overview

Good error messages reduce support burden.

A good error message contains:

- what went wrong
- where it happened
- what to try next

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

---

## Self-check

- If a beginner runs your project wrong, does the error message teach them what to do?

---

## References

- Python errors/exceptions: https://docs.python.org/3/tutorial/errors.html
