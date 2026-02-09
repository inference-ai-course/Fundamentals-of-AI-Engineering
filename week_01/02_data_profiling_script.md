# Week 1 — Part 02: Data profiling script (CSV -> JSON/Markdown)

## Overview

In AI/ML/LLM projects, most pain starts with data issues:

- wrong column names
- unexpected types
- empty files
- missing values

A **data profiling script** makes these issues visible early.

You will build `data_profile.py` that:

- reads a CSV
- validates basic assumptions
- computes a few useful stats
- writes reproducible outputs to `output/`

---

## Pre-study (Self-learn)

Foundamental Course assumes Self-learn is complete. If you need a refresher on modules, file I/O, exceptions, or JSON:

- [Pre-study index (Foundamental Course → Self-learn)](../PRESTUDY.md)
- [Self-learn — Modules and exception handling](../../self_learn/Chapters/2/02_modules_exceptions.md)

---

## Output contract (what your script guarantees)

Given the same input CSV, the script should always produce:

- `output/profile.json` (machine-readable)
- `output/profile.md` (human-readable)

And it should fail with **clear errors** for:

- missing file
- empty file
- missing required columns (optional extension)

This is a small example of **defensive programming**:

- validate early (fail fast)
- error messages should teach the user what to fix
- outputs should be deterministic so that diffs are meaningful

---

## Implementation: `data_profile.py`

Create `data_profile.py`:

```python
import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path

from typing import Dict, List

import pandas as pd


@dataclass
class Profile:
    rows: int
    cols: int
    columns: List[str]
    dtypes: Dict[str, str]
    missing_by_column: Dict[str, int]


def load_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    if path.stat().st_size == 0:
        raise ValueError(f"Input file is empty: {path}")

    return pd.read_csv(path)


def make_profile(df: pd.DataFrame) -> Profile:
    missing = df.isna().sum().to_dict()
    dtypes = {col: str(dtype) for col, dtype in df.dtypes.to_dict().items()}

    return Profile(
        rows=int(df.shape[0]),
        cols=int(df.shape[1]),
        columns=list(df.columns),
        dtypes=dtypes,
        missing_by_column={k: int(v) for k, v in missing.items()},
    )


def profile_to_markdown(p: Profile) -> str:
    lines = []
    lines.append("# Data Profile")
    lines.append("")
    lines.append(f"- Rows: {p.rows}")
    lines.append(f"- Columns: {p.cols}")
    lines.append("")
    lines.append("## Columns")
    lines.append("")
    lines.append("| column | dtype | missing |")
    lines.append("|---|---|---:|")
    for col in p.columns:
        lines.append(f"| {col} | {p.dtypes.get(col, '')} | {p.missing_by_column.get(col, 0)} |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Profile a CSV and write reproducible outputs")
    parser.add_argument("--input", required=True, help="Path to input CSV")
    parser.add_argument("--output_dir", default="output", help="Directory to write outputs")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    df = load_csv(input_path)
    p = make_profile(df)

    (output_dir / "profile.json").write_text(json.dumps(asdict(p), indent=2, sort_keys=True))
    (output_dir / "profile.md").write_text(profile_to_markdown(p))

    print(f"Wrote: {(output_dir / 'profile.json').as_posix()}")
    print(f"Wrote: {(output_dir / 'profile.md').as_posix()}")


if __name__ == "__main__":
    main()
```

Two details above matter for reproducibility:

- `sort_keys=True` makes JSON output stable (so two runs can be byte-for-byte identical)
- writing to a single `output_dir` makes the project easier to test and share

---

## How to run

```bash
python data_profile.py --input your_data.csv --output_dir output
```

Then open:

- `output/profile.md`
- `output/profile.json`

---

## Reproducibility checks

Run twice with the same input and confirm:

- JSON keys are sorted (we used `sort_keys=True`)
- outputs are identical across runs

If you later add timestamps, random samples, or “top N” operations, be careful: those can break determinism unless you explicitly control ordering and randomness.

---

## Extensions (recommended)

### 1) Required columns

Add a flag like:

- `--required_columns colA,colB`

Then fail with a clear message if any are missing.

Why this matters: you are turning vague assumptions into explicit *preconditions*. If the preconditions do not hold, everything downstream is unreliable.

### 2) Numeric summaries

For numeric columns compute:

- min/max/mean

Interpretation (light intuition):

- mean estimates the “typical” value: $\mu = \frac{1}{n}\sum_{i=1}^n x_i$
- min/max catch obvious outliers or wrong units

### 3) Frequent values

For categorical columns compute:

- top 5 values

Practical implication: frequent-value tables often reveal data quality bugs (e.g., “N/A”, “unknown”, “-”, whitespace-only strings).

---

## Common pitfalls

- **CSV delimiter mismatch**
  - Symptom: one giant column.
  - Fix: try `pd.read_csv(path, sep=';')`.

- **Encoding issues**
  - Fix: try `encoding='utf-8'` or `encoding='latin-1'`.

- **Outputs go to random locations**
  - Fix: always write to a single folder like `output/`.

- **Non-deterministic column ordering or summaries**
  - Symptom: diffs look noisy even when the data didn’t change.
  - Fix: sort column names where appropriate, and be consistent about ordering in markdown tables.

---

## Self-check

- If the input file is missing, do you get a clear error?
- If the file is empty, do you fail early?
- If you send this folder to a teammate, can they run it?

---

## References

- Pandas getting started: https://pandas.pydata.org/docs/getting_started/index.html
- Pandas I/O: https://pandas.pydata.org/docs/user_guide/io.html
