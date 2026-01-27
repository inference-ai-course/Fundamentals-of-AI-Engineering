# Week 6 — Part 02: Sampling and compression for tabular data

## Overview

You usually cannot send a full dataset to an LLM.

Instead you send a compressed representation:

- descriptive stats
- missingness summary
- a small sample of rows
- detected anomalies

---

## Underlying theory: you are fitting information into a fixed budget

The model has a fixed context window, so your input must satisfy a budget constraint.

From Week 3, a simplified budget looks like:

$$
C \ge T_{\text{prompt}} + T_{\text{table}} + T_{\text{output}}
$$

If your table is large, $T_{\text{table}}$ dominates. Compression reduces $T_{\text{table}}$ by replacing raw rows with summaries.

You can think of this as an information bottleneck:

- raw data is high detail but too large
- summaries are smaller but may lose rare edge cases

Practical implication: good compression keeps *the facts that matter for the task* (distributions, missingness, anomalies) while dropping redundant detail.

---

## Example: compress a dataframe

```python
import json
from dataclasses import dataclass

import pandas as pd


@dataclass
class CompressedTable:
    shape: tuple[int, int]
    columns: list[str]
    dtypes: dict[str, str]
    missing: dict[str, int]
    sample_rows: list[dict]


def compress_table(df: pd.DataFrame, sample_n: int = 8, seed: int = 42) -> CompressedTable:
    sample = df.sample(n=min(sample_n, len(df)), random_state=seed) if len(df) > 0 else df
    return CompressedTable(
        shape=(int(df.shape[0]), int(df.shape[1])),
        columns=list(df.columns),
        dtypes={c: str(t) for c, t in df.dtypes.to_dict().items()},
        missing={c: int(v) for c, v in df.isna().sum().to_dict().items()},
        sample_rows=sample.to_dict(orient="records"),
    )


def to_json(ct: CompressedTable) -> str:
    return json.dumps(
        {
            "shape": ct.shape,
            "columns": ct.columns,
            "dtypes": ct.dtypes,
            "missing": ct.missing,
            "sample_rows": ct.sample_rows,
        },
        indent=2,
        sort_keys=True,
    )
```

Why the design choices matter:

- sampling uses a `seed` so results are stable across runs
- `sort_keys=True` produces deterministic JSON (diff-friendly)
- a structured object (`CompressedTable`) makes it easier to evolve the contract later

Calibration tip:

- start with a small `sample_n` (e.g., 5–10)
- if the LLM misses important patterns, add targeted summaries (top values, numeric ranges, anomaly counts) rather than dumping more rows blindly

---

## Self-check

- If your dataset has 1M rows, does your compressed representation remain small?
- If you re-run with the same seed, is the sample stable?

---

## References

- Pandas sampling: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sample.html
