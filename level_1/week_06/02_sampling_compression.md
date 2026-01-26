# Week 6 — Part 02: Sampling and compression for tabular data

## Overview

You usually cannot send a full dataset to an LLM.

Instead you send a compressed representation:

- descriptive stats
- missingness summary
- a small sample of rows
- detected anomalies

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

---

## Self-check

- If your dataset has 1M rows, does your compressed representation remain small?
- If you re-run with the same seed, is the sample stable?

---

## References

- Pandas sampling: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sample.html
