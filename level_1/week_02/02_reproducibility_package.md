# Week 2 — Part 02: Reproducibility package (seeds, configs, artifacts)

## Overview

Reproducibility means:

- If you run the same command twice, results are identical (or explainably close).
- If your teammate runs your command, they can reproduce your metrics.

In practice, reproducibility is a *package* of habits.

---

## Underlying theory: results must be traceable to inputs

Treat an experiment outcome like a function:

$$
\text{metric} = h(\text{code}, \text{data}, \text{config}, \text{seed}, \text{environment})
$$

Reproducibility is the discipline of recording these inputs so you can:

- reproduce the metric
- explain differences when the metric changes
- debug failures without guessing

Important nuance: even with a fixed seed, some systems are not perfectly deterministic (multithreading, GPU kernels). In Level 1, the goal is mostly **traceability** and **reasonable stability**.

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

Practical implication:

- if you change the seed, metrics may change even if code and data are identical
- if you do not control the seed, you can accidentally “improve” just by getting a lucky split

---

## 2) Parameterize runs

Avoid “magic values” in code.

Instead expose them as flags:

- `--seed`
- `--test_size`
- `--max_iter`

This turns runs into explicit, shareable commands.

Think of the command line as a compact, human-readable “experiment record” you can paste into a report.

---

## 3) Save artifacts every run

Minimum artifacts to save:

- `config.json` (what you intended to run)
- `metrics.json` (what happened)
- `model.joblib` (the trained model)

This is the bridge between:

- experimentation
- and real engineering

Because it creates an audit trail:

- config answers “what did I try?”
- metrics answer “what happened?”
- model answers “can I reproduce predictions later?”

---

## 4) Add a run id (so you can compare)

A run id is just a unique folder per run.

A timestamp-based approach is good enough for Level 1:

```python
run_id = time.strftime("run_%Y%m%d_%H%M%S")
```

If you later run multiple experiments quickly, timestamps can collide. A simple fix is adding a random suffix (or using a UUID), but timestamps are fine for Level 1.

---

## Common pitfalls

- **Pitfall: you overwrite your model each run**
  - Fix: per-run folders.

- **Pitfall: you don’t know what settings produced a metric**
  - Fix: save `config.json`.

- **Pitfall: you can’t reproduce**
  - Fix: make sure you pinned dependencies and recorded run commands in a `report.md`.

- **Pitfall: you treat a single metric as truth**
  - Explanation: metrics are estimates from a finite validation sample.
  - Fix: keep comparisons controlled, and interpret small changes cautiously.

---

## Self-check

- If you re-run with the same seed, are metrics identical?
- Can you point to an artifacts folder that proves your metric?

---

## References

- Controlling randomness: https://scikit-learn.org/stable/common_pitfalls.html#controlling-randomness
- Model persistence: https://scikit-learn.org/stable/model_persistence.html
