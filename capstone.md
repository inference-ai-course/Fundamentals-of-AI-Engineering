# Fundamentals Course Capstone: Intelligent Data Analysis Script

Deliver a reproducible Python project that reads CSV data and produces a structured report via **traditional statistics + LLM explanations**. This is the required Week 6 MVP for the beginner program and should demonstrate **data profiling + structured LLM calls + reproducible project delivery**.

Pick a topic that is interesting to you, but keep the same I/O contract: **CSV in -> `report.json` + `report.md` out**.

*   Sales / revenue analysis (orders, customers, products)
*   Marketing campaign analysis (impressions, clicks, conversion)
*   Customer support analysis (tickets, categories, resolution time)
*   HR / recruiting analysis (applications, funnel stages, time-to-hire)
*   Operations / quality analysis (defects, incidents, on-call tickets)
*   Education / learning analytics (quiz scores, completion, engagement)

If you do not have access to real data, use public datasets or generate synthetic data with a clear schema.

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

*   **Reliability**: timeout or max wait setting, a bounded retry/repair attempt, and clear error messages
*   **Reproducibility**: provide an environment file (`requirements.txt` or `pyproject.toml`) and a README
*   **Maintainability**: organize code into modules (e.g., data/llm/report/utils)
*   **Testability**: at least 3 checks (normal input, empty/missing columns, oversized/invalid data). Automated tests are preferred, but a manual test checklist or a simple `smoke_test.py` is acceptable.

## Suggested Project Structure (Example)

*   `analyze.py` (CLI entrypoint)
*   `src/`
    *   `data_profile.py`
    *   `sampling.py`
    *   `llm_client.py`
    *   `report_builder.py`
*   `tests/`
*   `README.md`

## What to Complete

*   Source code repository (or a directory)
*   One-command run instructions in README:
    *   `python analyze.py --input data.csv --out output/`
*   Output samples (the `output/` directory contains at least one successful run)
*   `postmortem.md`: document one key issue you encountered (e.g., unstable outputs/timeouts/large data) and how you solved it

## Acceptance Criteria

*   Runs reliably on small-to-medium CSV files; failures must have understandable error messages
*   Stable LLM output schema: `report.json` fields should not drift across runs
*   Includes beginner-friendly reliability controls; logs or saved notes can pinpoint which stage failed (data processing / model call / output writing)
*   Report must include at least:
    *   Data overview
    *   Anomalies and risk notes
    *   At least 3 actionable recommendations

## Stretch Goals (Optional)

*   Add simple visualizations (charts + auto-embedded into the report)
*   Support multiple data sources (CSV + Excel)
*   Switchable backends for local inference vs hosted APIs (unified interface)
*   Add caching: reuse LLM results when the input data hash matches
