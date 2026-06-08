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
    #
    # Job-skill theme: the LLM identifies the skills, but it can only reason over
    # the evidence you put here. Besides sampled rows, add cheap, deterministic
    # SKILL EVIDENCE so the model has something to ground its answer on:
    #   - top_job_titles (role distribution)
    #   - existing job_skills strings, if the column is populated
    #   - keyword frequency hints: count how many postings mention each known
    #     skill (e.g. python, sql, tableau) — cheap, explainable, and compact
    #   - a few truncated representative job_description samples
    # See 03_skill_analysis.md for the full evidence -> prompt -> report flow.
    raise NotImplementedError("TODO: implement compress_profile()")
