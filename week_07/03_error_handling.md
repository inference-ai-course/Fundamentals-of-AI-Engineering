# Week 7 — Part 03: Error handling that teaches the user what to do

## Overview

Good error messages reduce support burden.

A good error message contains:

- what went wrong
- where it happened
- what to try next

---

## Pre-study (Self-learn)

Foundamental Course assumes Self-learn is complete. If you need a refresher on exceptions and debugging patterns:

- [Pre-study index (Foundamental Course → Self-learn)](../PRESTUDY.md)
- [Self-learn — Modules and exception handling](../../self_learn/Chapters/2/02_modules_exceptions.md)

Why it matters here (Week 7):

- Errors are part of your product surface: they should tell the user what to do next.
- Prefer short, actionable user-facing errors; log deeper details separately.

---

## Practical pattern

```python
from pathlib import Path


def require_file(path: str) -> Path:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(
            f"Input file not found: {p}. "
            "Check the path, or run with --help to see expected inputs."
        )
    if p.stat().st_size == 0:
        raise ValueError(f"Input file is empty: {p}. Provide a non-empty CSV.")
    return p
```

Practical tip: keep “user-facing” errors short and actionable. If you also want a stack trace for debugging, log the exception separately.

---

## Error message anatomy

Good error messages have 3 parts:

1. **What went wrong** (specific)
2. **Where it happened** (context)
3. **What to do** (actionable)

### Bad example
```python
raise ValueError("Invalid input")
# Error: Invalid input
```

**Problems:**
- Which input?
- What makes it invalid?
- How to fix?

### Good example
```python
raise ValueError(
    f"Invalid CSV delimiter: got '{delimiter}', expected ',' or ';'. "
    f"File: {input_path}. "
    f"Fix: Check the file format or specify --delimiter."
)
```

**Provides:**
- Specific value that was wrong
- What was expected
- How to fix

---

## Custom exception hierarchy

```python
class CapstoneError(Exception):
    """Base exception for capstone pipeline."""
    pass


class InputValidationError(CapstoneError):
    """Input validation failed."""
    pass


class DataQualityError(CapstoneError):
    """Data quality checks failed."""
    pass


class LLMCallError(CapstoneError):
    """LLM API call failed."""
    pass


# Usage
def load_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise InputValidationError(
            f"Input file not found: {path}\n"
            f"Expected: CSV file\n"
            f"Fix: Check file path or run with --help"
        )
    
    df = pd.read_csv(path)
    
    if len(df) == 0:
        raise DataQualityError(
            f"CSV is empty: {path}\n"
            f"Expected: At least 1 row\n"
            f"Fix: Provide a non-empty dataset"
        )
    
    return df
```

**Benefits:**
- Can catch by category: `except InputValidationError`
- Clear error types in logs
- Can handle different errors differently

---

## Context managers for cleanup

```python
import sys
from contextlib import contextmanager


@contextmanager
def pipeline_stage(stage_name: str):
    """
    Wrap a pipeline stage with error context.
    """
    print(f"Starting: {stage_name}")
    try:
        yield
        print(f"✓ Completed: {stage_name}")
    except Exception as e:
        print(f"✗ Failed: {stage_name}", file=sys.stderr)
        print(f"  Error: {e}", file=sys.stderr)
        raise


# Usage
with pipeline_stage("Load CSV"):
    df = pd.read_csv(input_path)

with pipeline_stage("Profile data"):
    profile = compute_profile(df)

with pipeline_stage("LLM call"):
    result = call_llm(compressed_data)
```

**Output on failure:**
```
Starting: Load CSV
✓ Completed: Load CSV
Starting: Profile data
✓ Completed: Profile data
Starting: LLM call
✗ Failed: LLM call
  Error: ConnectionError: Cannot connect to API
```

---

## Validation with clear errors

```python
from typing import List
import pandas as pd


def validate_csv_schema(
    df: pd.DataFrame,
    required_columns: List[str],
    file_path: Path
) -> None:
    """
    Validate CSV has required columns.
    """
    missing = [col for col in required_columns if col not in df.columns]
    
    if missing:
        raise InputValidationError(
            f"Missing required columns in {file_path}:\n"
            f"  Missing: {', '.join(missing)}\n"
            f"  Found: {', '.join(df.columns.tolist())}\n"
            f"  Required: {', '.join(required_columns)}\n"
            f"\n"
            f"Fix: Ensure your CSV has all required columns."
        )


def validate_data_quality(df: pd.DataFrame, file_path: Path) -> None:
    """
    Check basic data quality.
    """
    # Check for completely empty columns
    empty_cols = [col for col in df.columns if df[col].isna().all()]
    
    if empty_cols:
        raise DataQualityError(
            f"Empty columns in {file_path}:\n"
            f"  Columns: {', '.join(empty_cols)}\n"
            f"  These columns have no data.\n"
            f"\n"
            f"Fix: Remove empty columns or add data."
        )
    
    # Check if dataset is too small
    if len(df) < 3:
        raise DataQualityError(
            f"Dataset too small: {len(df)} rows\n"
            f"  Minimum: 3 rows\n"
            f"\n"
            f"Fix: Provide a larger dataset."
        )
```

---

## Error recovery patterns

### Pattern 1: Retry with degraded mode

```python
def call_llm_with_fallback(prompt: str) -> str:
    """
    Try main model, fall back to simpler model on error.
    """
    try:
        return call_llm(prompt, model="gpt-4")
    except LLMCallError as e:
        print(f"Warning: GPT-4 failed ({e}), trying GPT-3.5...")
        return call_llm(prompt, model="gpt-3.5-turbo")
```

### Pattern 2: Partial success

```python
def process_batch(items: List[str]) -> dict:
    """
    Process items, collect both successes and failures.
    """
    results = {"successes": [], "failures": []}
    
    for i, item in enumerate(items):
        try:
            result = process_item(item)
            results["successes"].append({"index": i, "result": result})
        except Exception as e:
            results["failures"].append({"index": i, "error": str(e)})
    
    # Report summary
    print(f"Processed {len(results['successes'])}/{len(items)} items")
    if results["failures"]:
        print(f"Failures: {len(results['failures'])}")
    
    return results
```

### Pattern 3: Save state before risky operation

```python
def process_with_checkpoint(data: pd.DataFrame, output_dir: Path):
    """
    Save intermediate state before LLM call.
    """
    # Save checkpoint
    checkpoint = output_dir / "checkpoint.parquet"
    data.to_parquet(checkpoint)
    print(f"Saved checkpoint: {checkpoint}")
    
    try:
        # Risky operation
        result = call_expensive_llm(data)
        return result
    except Exception as e:
        print(
            f"Error: {e}\n"
            f"Checkpoint saved at: {checkpoint}\n"
            f"You can resume from this checkpoint."
        )
        raise
```

---

## Logging vs user errors

```python
import logging
import sys

logger = logging.getLogger(__name__)


def load_and_validate(path: Path) -> pd.DataFrame:
    """
    Load with dual error reporting: user-facing + detailed logs.
    """
    logger.info(f"Loading CSV from: {path}")
    
    try:
        df = pd.read_csv(path)
        logger.info(f"Loaded {len(df)} rows, {len(df.columns)} columns")
        
    except FileNotFoundError:
        # User-facing error (simple)
        print(
            f"Error: File not found: {path}\n"
            f"Fix: Check the file path.",
            file=sys.stderr
        )
        # Detailed log (for debugging)
        logger.error(f"FileNotFoundError loading {path}", exc_info=True)
        raise
    
    except pd.errors.ParserError as e:
        # User-facing error
        print(
            f"Error: Cannot parse CSV: {path}\n"
            f"This may be a delimiter or encoding issue.\n"
            f"Fix: Try opening in a text editor to check format.",
            file=sys.stderr
        )
        # Detailed log
        logger.error(f"CSV parse error: {e}", exc_info=True)
        raise
    
    return df
```

---

## Practice notebook

For hands-on error handling exercises, see:
- **[03_error_handling.ipynb](./03_error_handling.ipynb)** - Interactive error patterns
- **[practice.ipynb](./practice.ipynb)** - Extended exercises

---

## Self-check

- If a beginner runs your project wrong, does the error message teach them what to do?
- Can you catch errors by category (validation vs quality vs API)?
- Do your error messages include the specific value that was wrong?
- Have you tested error paths (not just happy path)?

---

## References

- Python errors/exceptions: https://docs.python.org/3/tutorial/errors.html
- Python logging: https://docs.python.org/3/library/logging.html
- Context managers: https://docs.python.org/3/library/contextlib.html
