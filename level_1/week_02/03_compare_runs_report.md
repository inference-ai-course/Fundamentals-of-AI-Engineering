# Week 2 — Part 03: Comparing runs + writing a short report

## Overview

A useful experiment comparison changes **one variable** at a time.

This makes improvement explainable.

---

## Pre-study (Level 0)

Level 1 assumes Level 0 is complete. If you need a refresher on evaluation metrics (accuracy/precision/recall/F1):

- [Pre-study index (Level 1 → Level 0)](../PRESTUDY.md)
- [Level 0 — Evaluation metrics](../../level_0/Chapters/4/02_core_concepts.md)

Why it matters here (Week 2):

- You will compare two runs; only change **one variable** so the comparison is explainable.
- Use the saved artifacts (`metrics.json`, `val_report.txt`) as evidence in your report.

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

Also ask:

- did errors move around (e.g., fewer false negatives but more false positives)?
- is the improvement large enough to matter, or likely just noise from the split?

---

## Step 4: Write `report.md`

A good Level 1 report is short and structured:

- **Goal**: what you tried to improve
- **Change**: exactly what you changed
- **Result**: metrics before/after
- **Interpretation**: why you think it changed
- **Failure retrospective**: one run that didn’t work + what you learned
- **Next experiment**: one clear idea

Two rules that make reports “engineering-grade”:

- always include the exact commands (so the run is reproducible)
- always point to the artifact folders that back up your metric claims

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

Optional (recommended) addition:

- **Risk / caveat**: one sentence about what might be misleading (small dataset, imbalance, label noise, etc.)

---

## Common pitfalls

- **Pitfall: you changed code and parameters together**
  - Fix: keep the code stable while comparing parameters.

- **Pitfall: you only report one metric**
  - Fix: include at least accuracy and F1 (when classification is non-trivial).

- **Pitfall: you compare runs that used different data splits**
  - Fix: keep the same seed when comparing hyperparameters; if you later change the split, treat it as a separate experiment question.

---

## References

- Model evaluation: https://scikit-learn.org/stable/modules/model_evaluation.html
- F1 score: https://en.wikipedia.org/wiki/F1_score
