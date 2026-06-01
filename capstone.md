# Fundamentals Course Capstone: AI-Assisted CSV Data Analyzer

Deliver a reproducible Python project that reads CSV data, builds a compact data summary, calls a **real LLM**, and writes a structured report.

The required I/O contract is fixed:

```text
CSV input -> data profiling -> sampled/compressed summary -> real LLM interpretation -> report.json + report.md
```

This capstone is still a **data analyzer**. The goal is not advanced statistics or a full analytics product. The goal is to show that you can combine data profiling, prompt contracts, LLM reliability controls, and reproducible project delivery.

## Topic Choices

You may use a general CSV dataset, but these two themes are strongly recommended because they make the LLM interpretation more meaningful:

1. **Customer Feedback / Support Ticket Analyzer**
   - Example columns: `ticket_id`, `created_at`, `customer_segment`, `channel`, `message`, `rating`
   - Useful LLM outputs: common themes, urgent issues, customer risks, recommended actions

2. **Product Review Insight Reporter**
   - Example columns: `review_id`, `product`, `rating`, `review_text`, `date`, `region`
   - Useful LLM outputs: positive themes, negative themes, feature requests, product risks

Other topics are allowed if they keep the same CSV input and report output contract.

## MVP Scope

- **Input**: CSV file path.
- **Data profiling**:
  - Column types.
  - Missing values.
  - Duplicate rows.
  - Basic numeric and categorical summaries.
  - Simple anomaly hints.
- **Compression**:
  - Do not send the full CSV to the LLM.
  - Send a compact summary: schema, row/column counts, selected stats, top categories, representative samples, and anomaly hints.
- **Real LLM interpretation**:
  - Use a structured prompt.
  - Save the prompt and raw response.
  - Validate the expected fields.
  - Use timeout/retry or a repair attempt.
  - Mock responses are allowed for local debugging only; they do **not** satisfy the final capstone requirement.
- **Output**:
  - `output/report.json`
  - `output/report.md`

## Target `report.json` Skeleton

Students may add theme-specific details, but the final JSON should preserve these top-level fields:

```json
{
  "metadata": {},
  "dataset_summary": {},
  "data_quality": {},
  "compression_summary": {},
  "llm_interpretation": {},
  "recommendations": [],
  "risk_notes": [],
  "errors_or_warnings": []
}
```

For customer feedback or support tickets, `llm_interpretation` may include `themes`, `urgent_issues`, and `customer_risks`.

For product reviews, `llm_interpretation` may include `positive_themes`, `negative_themes`, and `feature_requests`.

## Template

Use the starter scaffold in:

```text
week_06/capstone_template/
```

The template is intentionally incomplete. It gives file structure, function signatures, expected keys, and TODO comments. You must complete the profiling, compression, real LLM call, validation, and report-building logic.

You may use AI Agent Coding Tools such as Cursor, Kilo, Copilot Chat, ChatGPT, or Claude to help complete the TODOs, but you must document what prompts you used and what you personally verified.

## Suggested Final Project Structure

```text
analyze.py
src/
  data_profile.py
  compression.py
  llm_interpretation.py
  report_builder.py
output/
README.md
requirements.txt or pyproject.toml
postmortem.md
prompts.md or ai_usage.md
```

## What to Complete

| File or Folder | Description |
|----------------|-------------|
| Source code | CLI script or small modular project |
| `output/report.json` | Machine-readable final report with stable top-level fields |
| `output/report.md` | Human-readable final report |
| `README.md` | Setup, API key/provider notes, and one-command run instructions |
| `requirements.txt` or `pyproject.toml` | Dependencies |
| sample input or dataset link | Dataset used for the successful run |
| `postmortem.md` | One issue encountered and how it was handled |
| `prompts.md` or `ai_usage.md` | Prompt and AI Agent Coding Tool usage notes |

## Acceptance Criteria

- A reviewer can run the project on a small-to-medium CSV using the README.
- The run performs a real LLM call and saves evidence of the prompt/raw response.
- The project avoids sending the full dataset to the LLM.
- `report.json` preserves the required top-level schema across runs.
- `report.md` includes a readable overview, data quality notes, LLM-generated interpretation, recommendations, and risk notes.
- Failures have understandable error messages.

## Stretch Goals (Optional)

These are optional and should not replace the MVP:

- Add charts to the Markdown report.
- Support Excel input.
- Support both hosted API and Ollama backends.
- Add caching based on input file hash.
- Add a CLI flag for different report styles.
