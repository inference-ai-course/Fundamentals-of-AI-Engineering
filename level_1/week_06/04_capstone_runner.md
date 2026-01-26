# Week 6 — Part 04: End-to-end capstone runner (one command)

## Overview

Your capstone should run with **one command**.

That means:

- clear CLI flags
- predictable outputs
- stable artifact locations

---

## Suggested CLI

Example interface:

```bash
python run_capstone.py --input data.csv --output_dir output --model <MODEL_NAME>
```

---

## Output contract

The command should write:

- `output/report.json`
- `output/report.md`

Optionally:

- `output/profile.json`
- `output/compressed_input.json`

Those intermediate artifacts make debugging faster.

---

## Self-check

- Can you run from a fresh folder after following README steps?
- If the model call fails, do you still get intermediate outputs?

---

## References

- Python `argparse`: https://docs.python.org/3/library/argparse.html
