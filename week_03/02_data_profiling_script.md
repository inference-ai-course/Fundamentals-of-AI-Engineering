# Week 3 - Part 02: Data Profiling Script (CSV -> JSON/Markdown)

## Overview

In AI, ML, and LLM projects, many failures start with data issues:

- wrong column names
- unexpected types
- empty files
- missing values
- duplicate rows

A data profiling script makes these issues visible before downstream code depends on the data.

You will build a small script that:

- reads a CSV file
- validates basic assumptions
- computes required data quality statistics
- writes reproducible outputs to `output/profile.json` and `output/profile.md`

## Learning Objectives

By the end of this lesson, you should be able to:

- Treat a CSV file path as untrusted input.
- Use imports, functions, and a dataclass to organize a small script.
- Raise clear errors for missing or empty files.
- Convert pandas and NumPy values into JSON-safe Python values.
- Produce stable output files that can be compared across runs.

## Output Contract

Given the same input CSV, the script should always produce:

- `output/profile.json`: machine-readable profile data
- `output/profile.md`: human-readable summary

The profile must include:

- row and column counts
- column names
- dtypes
- missing values by column
- duplicate row count
- numeric min, max, and mean
- top categorical values

The script should fail early with clear errors for:

- missing input file
- empty input file
- missing required columns, if you implement the optional extension

## Script Mental Model

A Python script is easier to reason about when each function has one job:

- `load_csv(path)`: validate the boundary and load the CSV.
- `make_profile(df)`: compute data quality facts.
- `profile_to_markdown(profile)`: turn the facts into a readable report.
- `main()`: parse command-line arguments and connect the steps.

This structure makes the code easier to test and easier to debug with AI assistance.

## Implementation: `data_profile.py`

Create `data_profile.py` with this implementation:

```python
import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, List, Optional

import pandas as pd


@dataclass
class Profile:
    rows: int
    cols: int
    columns: List[str]
    dtypes: Dict[str, str]
    missing_by_column: Dict[str, int]
    duplicate_rows: int
    numeric_summary: Dict[str, Dict[str, Optional[float]]]
    categorical_top_values: Dict[str, Dict[str, int]]


def load_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    if path.stat().st_size == 0:
        raise ValueError(f"Input file is empty: {path}")
    return pd.read_csv(path)


def clean_number(value) -> Optional[float]:
    if pd.isna(value):
        return None
    return float(value)


def make_profile(df: pd.DataFrame) -> Profile:
    missing = df.isna().sum().to_dict()
    dtypes = {col: str(dtype) for col, dtype in df.dtypes.to_dict().items()}
    numeric_summary = (
        df.select_dtypes(include="number")
        .agg(["min", "max", "mean"])
        .round(4)
        .to_dict()
    )
    categorical_top_values = {
        col: {
            str(value): int(count)
            for value, count in df[col].fillna("<MISSING>").value_counts().head(5).items()
        }
        for col in df.select_dtypes(exclude="number").columns
    }

    return Profile(
        rows=int(df.shape[0]),
        cols=int(df.shape[1]),
        columns=list(df.columns),
        dtypes=dtypes,
        missing_by_column={col: int(count) for col, count in missing.items()},
        duplicate_rows=int(df.duplicated().sum()),
        numeric_summary={
            col: {stat: clean_number(value) for stat, value in stats.items()}
            for col, stats in numeric_summary.items()
        },
        categorical_top_values=categorical_top_values,
    )


def profile_to_markdown(profile: Profile) -> str:
    lines = []
    lines.append("# Data Profile")
    lines.append("")
    lines.append(f"- Rows: {profile.rows}")
    lines.append(f"- Columns: {profile.cols}")
    lines.append(f"- Duplicate rows: {profile.duplicate_rows}")
    lines.append("")
    lines.append("## Columns")
    lines.append("")
    lines.append("| column | dtype | missing |")
    lines.append("|---|---|---:|")
    for col in profile.columns:
        dtype = profile.dtypes.get(col, "")
        missing = profile.missing_by_column.get(col, 0)
        lines.append(f"| {col} | {dtype} | {missing} |")
    lines.append("")

    if profile.numeric_summary:
        lines.append("## Numeric Summary")
        lines.append("")
        lines.append("| column | min | max | mean |")
        lines.append("|---|---:|---:|---:|")
        for col, stats in profile.numeric_summary.items():
            lines.append(
                f"| {col} | {stats.get('min', '')} | {stats.get('max', '')} | {stats.get('mean', '')} |"
            )
        lines.append("")

    if profile.categorical_top_values:
        lines.append("## Top Categorical Values")
        lines.append("")
        for col, values in profile.categorical_top_values.items():
            lines.append(f"### {col}")
            for value, count in values.items():
                lines.append(f"- {value}: {count}")
            lines.append("")

    return "\n".join(lines)


def require_columns(df: pd.DataFrame, required: List[str]) -> None:
    missing = [col for col in required if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Profile a CSV and write reproducible outputs")
    parser.add_argument("--input", required=True, help="Path to input CSV")
    parser.add_argument("--output_dir", default="output", help="Directory to write outputs")
    parser.add_argument("--required_columns", default="", help="Optional comma-separated required columns")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    df = load_csv(input_path)
    if args.required_columns:
        required = [col.strip() for col in args.required_columns.split(",") if col.strip()]
        require_columns(df, required)

    profile = make_profile(df)
    json_text = json.dumps(asdict(profile), indent=2, sort_keys=True)

    (output_dir / "profile.json").write_text(json_text, encoding="utf-8")
    (output_dir / "profile.md").write_text(profile_to_markdown(profile), encoding="utf-8")

    print(f"Wrote: {(output_dir / 'profile.json').as_posix()}")
    print(f"Wrote: {(output_dir / 'profile.md').as_posix()}")


if __name__ == "__main__":
    main()
```

## How to Run

```bash
python data_profile.py --input your_data.csv --output_dir output
```

Then open:

- `output/profile.md`
- `output/profile.json`

## Reproducibility Checks

Run twice with the same input and confirm:

- JSON keys are sorted because the script uses `sort_keys=True`.
- Outputs are written to the same output directory.
- Results do not include timestamps or random samples.

## Required Data Quality Note

After generating the profile, write at least 3 findings in `report.md`.

Examples:

- Missing values: which column has the most missing data?
- Duplicates: are duplicate rows present?
- Numeric ranges: do min and max values look reasonable?
- Frequent values: are there suspicious categories such as `unknown`, `N/A`, or blank values?

Keep each finding short and evidence-based. Point to the exact field in `profile.json` or section in `profile.md` that supports the finding.

## Common Pitfalls

- CSV delimiter mismatch: one giant column usually means the file may use a delimiter such as `;`.
- Encoding issues: try an explicit encoding only after you see the error.
- Outputs go to unclear locations: always write to one directory such as `output/`.
- Non-deterministic output: avoid timestamps and uncontrolled random samples in required artifacts.

## References

- Pandas getting started: https://pandas.pydata.org/docs/getting_started/index.html
- Pandas I/O: https://pandas.pydata.org/docs/user_guide/io.html
- Python `json`: https://docs.python.org/3/library/json.html
- Python `argparse`: https://docs.python.org/3/library/argparse.html
