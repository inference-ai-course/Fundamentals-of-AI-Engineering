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

## Output contract (what your script guarantees)

Given the same input CSV, the script should always produce:

- `output/profile.json` (machine-readable)
- `output/profile.md` (human-readable)

And it should fail with **clear errors** for:

- missing file
- empty file
- missing required columns (optional extension)

---

## Implementation: `data_profile.py`

Create `data_profile.py`:

```python
import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path

import pandas as pd


@dataclass
class Profile:
    rows: int
    cols: int
    columns: list[str]
    dtypes: dict[str, str]
    missing_by_column: dict[str, int]


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

---

## Extensions (recommended)

### 1) Required columns

Add a flag like:

- `--required_columns colA,colB`

Then fail with a clear message if any are missing.

### 2) Numeric summaries

For numeric columns compute:

- min/max/mean

### 3) Frequent values

For categorical columns compute:

- top 5 values

---

## Common pitfalls

- **CSV delimiter mismatch**
  - Symptom: one giant column.
  - Fix: try `pd.read_csv(path, sep=';')`.

- **Encoding issues**
  - Fix: try `encoding='utf-8'` or `encoding='latin-1'`.

- **Outputs go to random locations**
  - Fix: always write to a single folder like `output/`.

---

## Self-check

- If the input file is missing, do you get a clear error?
- If the file is empty, do you fail early?
- If you send this folder to a teammate, can they run it?

---

## References

- Pandas getting started: https://pandas.pydata.org/docs/getting_started/index.html
- Pandas I/O: https://pandas.pydata.org/docs/user_guide/io.html
