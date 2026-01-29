# Week 7 — Part 01: CLI design (argparse) + good defaults

## Overview

Your CLI is an interface like an API.

A good CLI:

- makes correct usage easy
- makes incorrect usage obvious
- documents itself via `--help`

---

## Pre-study (Level 0)

Level 1 assumes Level 0 is complete. If you need a refresher on Python modules, exceptions, and CLI-adjacent habits:

- [Pre-study index (Level 1 → Level 0)](../PRESTUDY.md)
- [Level 0 — Modules and exception handling](../../level_0/Chapters/2/02_modules_exceptions.md)

Why it matters here (Week 7):

- A stable CLI makes demos, smoke tests, and README instructions repeatable.
- Good defaults and clear errors reduce “support time” and speed up debugging.

## Minimum CLI checklist

- descriptive help text
- sensible defaults
- explicit inputs/outputs
- clear error when input file missing

---

## Example `argparse` pattern

```python
import argparse


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Run capstone pipeline end-to-end")
    p.add_argument("--input", required=True, help="Input CSV")
    p.add_argument("--output_dir", default="output", help="Where to write artifacts")
    p.add_argument("--model", default="gpt-4o-mini", help="Model name")
    p.add_argument("--seed", type=int, default=42)
    return p
```

Practical tips:

- keep flag names consistent across scripts (`--input`, `--output_dir`, `--seed`)
- choose defaults that make “copy/paste from README” work
- include enough info in `--help` that a teammate can run without opening code

---

## Self-check

- Can a teammate run `python run_capstone.py --help` and understand how to use it?

---

## References

- Python `argparse`: https://docs.python.org/3/library/argparse.html
- Click: https://click.palletsprojects.com/
