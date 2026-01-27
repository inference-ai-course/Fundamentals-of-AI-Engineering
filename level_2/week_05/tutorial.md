# Level 2 — Week 5 Tutorials

## Overview

Week 5 is about **quality iteration with evidence**.

You will:

- change one variable at a time
- run a minimal evaluation set (10–20 items)
- record failures and before/after metrics

## Navigation

- [01 — Controlled iteration (one variable at a time)](01_controlled_iteration.md)
- [02 — Minimal eval set design (10–20 items)](02_eval_set_design.md)
- [03 — Reproducible `eval_rag.py` outputs + failure analysis](03_eval_script_failure_analysis.md)

## Recommended order

1. Read 01 and set up a run-id + config artifact discipline.
2. Read 02 and build the eval set.
3. Read 03 and produce before/after evidence.

## What “done” looks like

- You have a baseline run (run id + config + outputs).
- You changed exactly one variable (e.g., chunk size) and reran evaluation.
- You can show:
  - metrics before/after
  - 3–5 concrete failure examples before/after
- You recorded at least one “regression” you introduced (so you learn rollback discipline).

## References

- Stanford IR book (evaluation): https://nlp.stanford.edu/IR-book/
- Twelve-Factor mindset (config discipline): https://12factor.net/
