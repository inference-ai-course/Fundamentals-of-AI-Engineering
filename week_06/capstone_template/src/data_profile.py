"""Data profiling TODOs for the capstone template."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd


def load_csv(csv_path: Path) -> pd.DataFrame:
    """Load a CSV file and return a dataframe.

    Expected behavior:
    - raise a clear error if the path does not exist
    - raise a clear error if the CSV is empty or unreadable
    - return a pandas DataFrame
    """
    # TODO: implement CSV loading and beginner-friendly error messages.
    raise NotImplementedError("TODO: implement load_csv()")


def build_profile(csv_path_or_df: Any) -> dict:
    """Build traditional data profiling fields.

    Expected top-level keys:
    - row_count
    - column_count
    - columns
    - dtypes
    - missing_values
    - duplicate_rows
    - numeric_summary
    - categorical_summary
    - anomaly_hints
    """
    # TODO: accept either a DataFrame or a path, then compute the required fields.
    # TODO: keep values JSON-serializable (convert numpy values to Python ints/floats).
    raise NotImplementedError("TODO: implement build_profile()")
