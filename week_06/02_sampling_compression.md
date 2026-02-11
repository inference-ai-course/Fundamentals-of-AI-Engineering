# Week 6 — Part 02: Sampling and compression for tabular data

## Overview

You usually cannot send a full dataset to an LLM.

Instead you send a compressed representation:

- descriptive stats
- missingness summary
- a small sample of rows
- detected anomalies

---

## Pre-study (Self-learn)

Foundamental Course assumes Self-learn is complete. If you need a refresher on context limits and AI engineering workflow:

- [Pre-study index (Foundamental Course → Self-learn)](../PRESTUDY.md)
- [Self-learn — Chapter 3: AI Engineering Fundamentals](../self_learn/Chapters/3/Chapter3.md)

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

## Advanced compression: categorical summaries

For categorical columns with many unique values, sample rows may miss important categories:

```python
def compress_with_categories(df: pd.DataFrame, top_k: int = 5) -> dict:
    """
    Add top categories for categorical columns.
    """
    categorical_summaries = {}
    
    for col in df.select_dtypes(include=['object', 'category']).columns:
        value_counts = df[col].value_counts()
        categorical_summaries[col] = {
            "top_values": value_counts.head(top_k).to_dict(),
            "n_unique": int(df[col].nunique()),
            "n_missing": int(df[col].isna().sum()),
        }
    
    return categorical_summaries


# Usage
cat_summary = compress_with_categories(df, top_k=5)
compressed["categorical_summaries"] = cat_summary
```

**Why this helps:**
- Reveals dominant categories
- Shows cardinality (n_unique)
- Identifies potential data quality issues (e.g., many "Unknown" values)

---

## Numeric summaries with distribution info

For numeric columns, basic stats can reveal outliers and distributions:

```python
def compress_numeric_stats(df: pd.DataFrame) -> dict:
    """
    Compute robust numeric statistics.
    """
    numeric_stats = {}
    
    for col in df.select_dtypes(include=['number']).columns:
        series = df[col].dropna()
        
        if len(series) > 0:
            numeric_stats[col] = {
                "mean": float(series.mean()),
                "median": float(series.median()),
                "std": float(series.std()),
                "min": float(series.min()),
                "max": float(series.max()),
                "q25": float(series.quantile(0.25)),
                "q75": float(series.quantile(0.75)),
                "n_missing": int(df[col].isna().sum()),
            }
    
    return numeric_stats


# Usage
num_stats = compress_numeric_stats(df)
compressed["numeric_stats"] = num_stats
```

**Interpretation guide:**
- Large `std` vs `mean` ratio → high variance
- `median` very different from `mean` → skewed distribution
- `min`/`max` far from quartiles → potential outliers

---

## Token budget estimation

Compressed representation should fit comfortably in context:

```python
import json


def estimate_tokens(obj: dict, chars_per_token: float = 4.0) -> int:
    """
    Rough token estimate for JSON object.
    """
    json_str = json.dumps(obj)
    return int(len(json_str) / chars_per_token)


# Check token budget
compressed = compress_table(df, sample_n=10)
estimated_tokens = estimate_tokens(compressed)
print(f"Compressed representation: ~{estimated_tokens} tokens")

# Rule of thumb: keep under 2000 tokens for comfortable prompt assembly
if estimated_tokens > 2000:
    print("WARNING: Compressed input may be too large")
    print("Consider reducing sample_n or removing verbose fields")
```

**Context budget allocation:**
- System prompt: ~100-200 tokens
- Task instructions: ~50-100 tokens
- Compressed data: <2000 tokens
- Output budget: ~500-1000 tokens
- **Total**: Should stay well under model's context limit

---

## Smart sampling strategies

### Strategy 1: Stratified sampling

Ensure rare categories are represented:

```python
def stratified_sample(df: pd.DataFrame, strata_col: str, n_per_stratum: int = 2) -> pd.DataFrame:
    """
    Sample evenly across categories.
    """
    return df.groupby(strata_col, group_keys=False).apply(
        lambda x: x.sample(n=min(n_per_stratum, len(x)), random_state=42)
    )


# Usage
if "category" in df.columns:
    sample = stratified_sample(df, strata_col="category", n_per_stratum=2)
else:
    sample = df.sample(n=10, random_state=42)
```

### Strategy 2: Include edge cases

Sample both typical and extreme values:

```python
def sample_with_extremes(df: pd.DataFrame, numeric_col: str, n_typical: int = 5, n_extremes: int = 2) -> pd.DataFrame:
    """
    Sample typical rows plus extremes.
    """
    # Typical: random sample
    typical = df.sample(n=n_typical, random_state=42)
    
    # Extremes: highest and lowest values
    extremes = pd.concat([
        df.nlargest(n_extremes, numeric_col),
        df.nsmallest(n_extremes, numeric_col)
    ])
    
    return pd.concat([typical, extremes]).drop_duplicates()
```

---

## Full compression example

```python
from dataclasses import dataclass, asdict
import json
import pandas as pd
from typing import Dict, List, Any


@dataclass
class RichCompression:
    """
    Comprehensive compressed representation.
    """
    shape: tuple
    dtypes: Dict[str, str]
    missing_summary: Dict[str, int]
    numeric_stats: Dict[str, Dict[str, float]]
    categorical_summaries: Dict[str, Dict[str, Any]]
    sample_rows: List[Dict[str, Any]]
    warnings: List[str]


def compress_table_rich(df: pd.DataFrame, sample_n: int = 8) -> RichCompression:
    """
    Create rich compressed representation with warnings.
    """
    warnings = []
    
    # Check for potential issues
    if len(df) == 0:
        warnings.append("Dataset is empty")
    if len(df.columns) == 0:
        warnings.append("Dataset has no columns")
    if df.isna().sum().sum() > len(df) * len(df.columns) * 0.5:
        warnings.append("More than 50% of values are missing")
    
    # Compress
    sample = df.sample(n=min(sample_n, len(df)), random_state=42) if len(df) > 0 else df
    
    return RichCompression(
        shape=(len(df), len(df.columns)),
        dtypes={c: str(t) for c, t in df.dtypes.to_dict().items()},
        missing_summary={c: int(v) for c, v in df.isna().sum().to_dict().items()},
        numeric_stats=compress_numeric_stats(df),
        categorical_summaries=compress_with_categories(df),
        sample_rows=sample.to_dict(orient="records"),
        warnings=warnings,
    )


# Usage
compressed = compress_table_rich(df, sample_n=5)
compressed_json = json.dumps(asdict(compressed), indent=2)

# Check size
print(f"Compressed to ~{estimate_tokens(asdict(compressed))} tokens")
```

---

## Practice notebook

For hands-on compression exercises and token budgeting, see:
- **[02_sampling_compression.ipynb](./02_sampling_compression.ipynb)** - Interactive compression techniques
- **[practice.ipynb](./practice.ipynb)** - Extended exercises

---

## Self-check

- If your dataset has 1M rows, does your compressed representation remain small?
- If you re-run with the same seed, is the sample stable?
- Can you estimate token count before sending to LLM?
- Does your compression preserve important patterns (distributions, categories, outliers)?

---

## References

- Pandas sampling: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sample.html
- Pandas describe: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html
- Token counting (tiktoken): https://github.com/openai/tiktoken
