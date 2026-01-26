# Week 2 — Part 03: Comparing runs + writing a short report

## Overview

A useful experiment comparison changes **one variable** at a time.

This makes improvement explainable.

---

## Step 1: Run baseline

```bash
python train.py --input data.csv --label_col label --seed 42 --max_iter 200
```

---

## Step 2: Run one controlled variant

Change a single parameter:

```bash
python train.py --input data.csv --label_col label --seed 42 --max_iter 1000
```

You now have two run folders under `artifacts/`.

---

## Step 3: Compare the outputs

Compare:

- `metrics.json`
- `val_report.txt`
- training time

Ask:

- Did accuracy improve?
- Did F1 improve?
- Did runtime increase?

---

## Step 4: Write `report.md`

A good Level 1 report is short and structured:

- **Goal**: what you tried to improve
- **Change**: exactly what you changed
- **Result**: metrics before/after
- **Interpretation**: why you think it changed
- **Failure retrospective**: one run that didn’t work + what you learned
- **Next experiment**: one clear idea

Example template:

```md
# Experiment report

## Goal

## Baseline

- command:
- metrics:

## Variant

- command:
- metrics:

## What changed and why

## One failure + lesson

## Next experiment
```

---

## Common pitfalls

- **Pitfall: you changed code and parameters together**
  - Fix: keep the code stable while comparing parameters.

- **Pitfall: you only report one metric**
  - Fix: include at least accuracy and F1 (when classification is non-trivial).

---

## References

- Model evaluation: https://scikit-learn.org/stable/modules/model_evaluation.html
- F1 score: https://en.wikipedia.org/wiki/F1_score
