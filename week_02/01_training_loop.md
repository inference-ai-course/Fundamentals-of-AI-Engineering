# Week 2 — Part 01: The ML training loop (split → train → evaluate → save)

## Overview

This is the smallest ML workflow that is still “real engineering”:

1. Load data
    - What it means: read inputs into a consistent table (rows = examples, columns = features).
    - What to verify: you can print row/column counts and confirm the label column exists.
2. Split train/validation
    - What it means: separate “data you learn from” vs “data you test on”.
    - What to verify: the split is reproducible (fixed seed) and train/val are disjoint.
3. Train a baseline model
    - What it means: start with a simple model to prove the pipeline works end-to-end.
    - What to verify: training completes and you can serialize the model.
4. Evaluate on validation
    - What it means: estimate performance on unseen data.
    - What to verify: metrics are computed on validation, not on training.
5. Save artifacts
    - What it means: save evidence (config + metrics + model/report) so results are explainable later.
    - What to verify: artifacts are written into a per-run folder so reruns don’t overwrite.

Even if you later focus on LLMs, this disciplined loop is the basis for:

- evaluating prompt changes
- comparing model/provider changes
- measuring improvements

---

## Pre-study (Self-learn)

Foundamental Course assumes Self-learn is complete. If you need a refresher on evaluation mindset and metrics:

- [Pre-study index (Foundamental Course → Self-learn)](../PRESTUDY.md)
- [Self-learn — Evaluation metrics (accuracy/precision/recall/F1)](../../self_learn/Chapters/4/02_core_concepts.md)

Why it matters here (Week 2):

- You will compare runs using saved artifacts; metrics must be computed on a hold-out split.
- Small metric changes can come from split randomness; controlling seed + saving config makes results explainable.

---

## Implementation: `train.py` (baseline classifier)

This script assumes you have a CSV with:

- feature columns
- a label column (e.g. `label`)

### Dependencies

`requirements.txt` example:

```txt
pandas==2.2.3
scikit-learn==1.5.2
joblib==1.4.2
```

Why these pieces exist:

- `scikit-learn` gives a clean split/train/eval workflow
- `joblib` persists trained models so you can re-load them later
- pinning versions reduces “works yesterday, breaks today” failures

### Code

```python
import argparse
import json
import time
from dataclasses import asdict, dataclass
from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


@dataclass
class TrainConfig:
    input_csv: str
    label_col: str
    test_size: float
    random_state: int
    max_iter: int


def main() -> None:
    parser = argparse.ArgumentParser(description="Train a reproducible baseline classifier")
    parser.add_argument("--input", required=True, help="Input CSV")
    parser.add_argument("--label_col", required=True, help="Label column name")
    parser.add_argument("--test_size", type=float, default=0.2)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--max_iter", type=int, default=500)
    parser.add_argument("--artifacts_dir", default="artifacts")
    args = parser.parse_args()

    cfg = TrainConfig(
        input_csv=args.input,
        label_col=args.label_col,
        test_size=float(args.test_size),
        random_state=int(args.seed),
        max_iter=int(args.max_iter),
    )

    df = pd.read_csv(cfg.input_csv)
    if cfg.label_col not in df.columns:
        raise ValueError(f"label_col not found: {cfg.label_col}")

    y = df[cfg.label_col]
    X = df.drop(columns=[cfg.label_col])

    X_train, X_val, y_train, y_val = train_test_split(
        X,
        y,
        test_size=cfg.test_size,
        random_state=cfg.random_state,
        stratify=y if y.nunique() > 1 else None,
    )

    numeric_cols = [c for c in X_train.columns if pd.api.types.is_numeric_dtype(X_train[c])]
    categorical_cols = [c for c in X_train.columns if c not in numeric_cols]

    numeric_pipe = Pipeline(steps=[("imputer", SimpleImputer(strategy="median"))])
    categorical_pipe = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_pipe, numeric_cols),
            ("cat", categorical_pipe, categorical_cols),
        ]
    )

    model = LogisticRegression(max_iter=cfg.max_iter)
    clf = Pipeline(steps=[("preprocess", preprocessor), ("model", model)])

    t0 = time.time()
    clf.fit(X_train, y_train)
    train_seconds = time.time() - t0

    y_pred = clf.predict(X_val)

    metrics = {
        "accuracy": float(accuracy_score(y_val, y_pred)),
        "f1_macro": float(f1_score(y_val, y_pred, average="macro")) if y_val.nunique() > 1 else None,
        "train_seconds": float(train_seconds),
        "n_train": int(len(X_train)),
        "n_val": int(len(X_val)),
    }

    run_id = time.strftime("run_%Y%m%d_%H%M%S")
    out_dir = Path(args.artifacts_dir) / run_id
    out_dir.mkdir(parents=True, exist_ok=True)

    (out_dir / "config.json").write_text(json.dumps(asdict(cfg), indent=2, sort_keys=True))
    (out_dir / "metrics.json").write_text(json.dumps(metrics, indent=2, sort_keys=True))
    (out_dir / "val_report.txt").write_text(classification_report(y_val, y_pred))
    joblib.dump(clf, out_dir / "model.joblib")

    print(json.dumps(metrics, indent=2))
    print(f"Saved artifacts to: {out_dir}")


if __name__ == "__main__":
    main()
```

What makes this “engineering” (not just a notebook experiment):

- **explicit config** (`TrainConfig` saved to `config.json`)
- **metric traceability** (`metrics.json` + `val_report.txt`)
- **model persistence** (`model.joblib`)
- **per-run folder** so you can compare runs without overwriting

---

## How to run

```bash
python train.py --input data.csv --label_col label --seed 42
```

---

## What “done” looks like

You have a folder like:

- `artifacts/run_.../config.json`
- `artifacts/run_.../metrics.json`
- `artifacts/run_.../val_report.txt`
- `artifacts/run_.../model.joblib`

If those exist and your script prints metrics, you have a baseline.

If you later improve features or models, you should always be able to answer:

- “Which exact run produced this metric?”
- “What config produced that run?”
- “Can I re-load the model and reproduce predictions?”

---

## References

- scikit-learn getting started: https://scikit-learn.org/stable/getting_started.html
