# Week 6 — Part 02: Sampling and compression for tabular data

## Overview

You usually cannot send a full dataset to an LLM.

Instead you send a compressed representation:

- descriptive stats
- missingness summary
- a small sample of rows
- detected anomalies

---

## Pre-study (Level 0)

Level 1 assumes Level 0 is complete. If you need a refresher on context limits and AI engineering workflow:

- [Pre-study index (Level 1 → Level 0)](../PRESTUDY.md)
- [Level 0 — Chapter 3: AI Engineering Fundamentals](../../level_0/Chapters/3/Chapter3.md)

Why it matters here (Week 6):

- You must fit decision-relevant information into a bounded context window.
- Good compression keeps distributions/missingness/anomalies while staying small and stable across reruns.

---

## Example: compress a dataframe

```python
import json
from dataclasses import dataclass
from typing import Any, Dict, List, Tuple

import pandas as pd


@dataclass
class CompressedTable:
    shape: Tuple[int, int]
    columns: List[str]
    dtypes: Dict[str, str]
    missing: Dict[str, int]
    sample_rows: List[Dict[str, Any]]


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
