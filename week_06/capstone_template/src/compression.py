"""Compression TODOs for the capstone template."""

from __future__ import annotations

from typing import Any


def compress_profile(profile: dict, df: Any) -> dict:
    """Create a compact representation for the LLM.

    Expected keys:
    - dataset_shape
    - selected_columns
    - important_profile_facts
    - sample_rows
    - token_budget_note

    Constraints:
    - do not include the full CSV
    - use deterministic sampling
    - include enough facts for the LLM to reason about the dataset
    """
    # TODO: sample a small number of rows with a fixed seed.
    # TODO: include top categories and numeric ranges from the profile.
    # TODO: estimate or describe why the compressed object is small enough.
    raise NotImplementedError("TODO: implement compress_profile()")
