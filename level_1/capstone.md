# Level 1 Capstone: Intelligent Data Analysis Script

## Project Goal

Deliver a reproducible Python project that reads CSV data and produces a structured report via **traditional statistics + LLM explanations**. This Capstone should demonstrate **basic ML/data intuition + production-minded LLM calls + software engineering fundamentals**.

## MVP Scope

*   **Input**: CSV file path
*   **Processing**:
    *   Data overview: column types, missing values, duplicates, basic statistics
    *   Anomaly hints: simple rules are fine (IQR / Z-score / custom thresholds)
    *   Sampling & compression: avoid sending the entire dataset to the model
    *   LLM interpretation: use structured prompts to generate “insights + recommendations + risk notes”
*   **Output**:
    *   `report.json` (machine-readable, stable schema)
    *   `report.md` (human-readable)

## Non-Functional Requirements

*   **Reliability**: timeouts, retries, and clear error messages
*   **Reproducibility**: provide an environment file (`requirements.txt` or `pyproject.toml`) and a README
*   **Maintainability**: organize code into modules (e.g., data/llm/report/utils)
*   **Testability**: at least 3 test cases (normal input, empty/missing columns, oversized/invalid data). Automated tests are preferred, but a manual test checklist or a simple `smoke_test.py` is acceptable.

## Suggested Project Structure (Example)

*   `analyze.py` (CLI entrypoint)
*   `src/`
    *   `data_profile.py`
    *   `sampling.py`
    *   `llm_client.py`
    *   `report_builder.py`
*   `tests/`
*   `README.md`

## Deliverables

*   Source code repository (or a directory)
*   One-command run instructions in README:
    *   `python analyze.py --input data.csv --out output/`
*   Output samples (the `output/` directory contains at least one successful run)
*   `postmortem.md`: document one key issue you encountered (e.g., unstable outputs/timeouts/large data) and how you solved it

## Acceptance Criteria

*   Runs reliably on CSV files up to 10MB; failures must have understandable error messages
*   Stable LLM output schema: `report.json` fields should not drift across runs
*   Includes retries/timeouts; logs can pinpoint which stage failed (data processing / model call / output writing)
*   Report must include at least:
    *   Data overview
    *   Anomalies and risk notes
    *   At least 3 actionable recommendations

## Rubric (Suggested)

*   Engineering quality (structure/readability/runnability/tests): 40%
*   Reliability and failure handling (timeouts/retries/logging/edge cases): 30%
*   Report quality (structure, reasonable insights, actionable recommendations): 30%

## Stretch Goals

*   Add simple visualizations (charts + auto-embedded into the report)
*   Support multiple data sources (CSV + Excel)
*   Switchable backends for local inference vs hosted APIs (unified interface)
*   Add caching: reuse LLM results when the input data hash matches
