# Week 7 — Part 01: CLI design (argparse) + good defaults

## Overview

Your CLI is an interface like an API.

A good CLI:

- makes correct usage easy
- makes incorrect usage obvious
- documents itself via `--help`

---

## Underlying theory: a CLI is a contract over user behavior

Users (including “future you”) will misuse your tool. A CLI contract reduces ambiguity by making:

- valid usage explicit (required flags, clear help)
- invalid usage fast-failing (clear errors)
- outputs predictable (stable locations, stable schemas)

Good defaults are not just convenience; they are a *policy* that encodes the “safe/typical” way to run your system.

Practical implication:

- if the CLI is stable, demos/tests become repeatable
- if the CLI changes unpredictably, your README and users break

---

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
