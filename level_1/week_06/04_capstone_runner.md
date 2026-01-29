# Week 6 — Part 04: End-to-end capstone runner (one command)

## Overview

Your capstone should run with **one command**.

That means:

- clear CLI flags
- predictable outputs
- stable artifact locations

---

## Pre-study (Level 0)

Level 1 assumes Level 0 is complete. If you need a refresher on reproducibility and pipeline contracts:

- [Pre-study index (Level 1 → Level 0)](../PRESTUDY.md)
- [Level 0 — Chapter 2: Python and Environment Management](../../level_0/Chapters/2/Chapter2.md)
- [Level 0 — Chapter 3: AI Engineering Fundamentals](../../level_0/Chapters/3/Chapter3.md)

Why it matters here (Week 6):

- A one-command runner is the practical test of reproducibility for your capstone.
- Stable inputs/config → predictable artifact locations makes demos and smoke tests feasible.

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

Failure-mode design tip:

- write intermediate artifacts *before* the LLM call
- if the LLM call fails, your run still leaves evidence (profile + compressed input) for debugging

---

## Self-check

- Can you run from a fresh folder after following README steps?
- If the model call fails, do you still get intermediate outputs?

---

## References

- Python `argparse`: https://docs.python.org/3/library/argparse.html
