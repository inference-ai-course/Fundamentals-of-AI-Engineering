# Week 6 — Part 04: End-to-end capstone runner (one command)

## Overview

Your capstone should run with **one command**.

That means:

- clear CLI flags
- predictable outputs
- stable artifact locations

---

## Underlying theory: the runner is your system’s public interface

From Week 1, reproducibility is an interface. The runner is the concrete version of that idea:

- given inputs and config, it produces outputs in predictable locations

You can treat it like a function contract:

$$
\text{outputs} = r(\text{input},\ \text{config})
$$

Practical implication:

- if the runner is stable, testing and demos become easy
- if the runner requires manual steps, failures become non-reproducible

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
