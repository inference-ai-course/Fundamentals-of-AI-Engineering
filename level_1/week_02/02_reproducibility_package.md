# Week 2 — Part 02: Reproducibility package (seeds, configs, artifacts)

## Overview

Reproducibility means:

- If you run the same command twice, results are identical (or explainably close).
- If your teammate runs your command, they can reproduce your metrics.

In practice, reproducibility is a *package* of habits.

---

## 1) Control randomness

Typical sources of randomness:

- train/val split
- model initialization
- data shuffling

In scikit-learn, the minimum is setting `random_state` in splitting functions.

Example:

```python
train_test_split(X, y, random_state=42)
```

---

## 2) Parameterize runs

Avoid “magic values” in code.

Instead expose them as flags:

- `--seed`
- `--test_size`
- `--max_iter`

This turns runs into explicit, shareable commands.

---

## 3) Save artifacts every run

Minimum artifacts to save:

- `config.json` (what you intended to run)
- `metrics.json` (what happened)
- `model.joblib` (the trained model)

This is the bridge between:

- experimentation
- and real engineering

---

## 4) Add a run id (so you can compare)

A run id is just a unique folder per run.

A timestamp-based approach is good enough for Level 1:

```python
run_id = time.strftime("run_%Y%m%d_%H%M%S")
```

---

## Common pitfalls

- **Pitfall: you overwrite your model each run**
  - Fix: per-run folders.

- **Pitfall: you don’t know what settings produced a metric**
  - Fix: save `config.json`.

- **Pitfall: you can’t reproduce**
  - Fix: make sure you pinned dependencies and recorded run commands in a `report.md`.

---

## Self-check

- If you re-run with the same seed, are metrics identical?
- Can you point to an artifacts folder that proves your metric?

---

## References

- Controlling randomness: https://scikit-learn.org/stable/common_pitfalls.html#controlling-randomness
- Model persistence: https://scikit-learn.org/stable/model_persistence.html
