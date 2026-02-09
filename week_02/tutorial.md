# Foundamental Course — Week 2 Tutorials

## Pre-study (Self-learn)

Foundamental Course assumes Self-learn is complete. If you need a refresher:

- [Pre-study index (Foundamental Course → Self-learn)](../PRESTUDY.md)
- [Self-learn — Chapter 2: Python and Environment Management](../../self_learn/Chapters/2/Chapter2.md)

## Overview

These tutorials expand Week 2 into a step-by-step, reproducible baseline ML workflow.

## Navigation

- [01 — The ML training loop (split → train → evaluate → save)](01_training_loop.md)
- [02 — Reproducibility package (seeds, configs, artifacts)](02_reproducibility_package.md)
- [03 — Comparing runs + writing a short report](03_compare_runs_report.md)

## Recommended order

1. Read 01 and get a baseline run working.
2. Read 02 and make your artifacts reproducible.
3. Read 03 and practice controlled comparisons.

Use [practice.ipynb](practice.ipynb) for extra hands-on work.

Why this order works:

1. **Baseline first**
    - A baseline run proves the whole loop works end-to-end (load → split → train → eval → save).
    - What to verify: you can produce an `artifacts/run_.../metrics.json` and re-run without overwriting.

2. **Reproducibility second**
    - Once it runs, make it repeatable: same command should produce explainably similar results.
    - What to verify: your run saves a config (seed, split settings) and you can point to the exact run that produced a metric.

3. **Comparisons third**
    - Only compare experiments after you’ve controlled variables; otherwise you can’t learn from results.
    - What to verify: you change one thing at a time (e.g., `max_iter`, model type, or one feature).
