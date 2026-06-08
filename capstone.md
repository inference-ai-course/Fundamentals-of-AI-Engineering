# Fundamentals Course Capstone: Job Posting Skill Analyzer

Deliver a reproducible Python project that reads a CSV of job postings, builds a compact data summary, calls a **real LLM**, and writes a structured skills and learning-priority report.

The required I/O contract is fixed:

```text
CSV input -> data profiling -> sampled/compressed summary -> real LLM interpretation -> report.json + report.md
```

This capstone is still a **data analyzer**. The goal is not advanced labor-market research, web scraping, or a full career platform. The goal is to show that you can combine data profiling, text compression, prompt contracts, LLM reliability controls, and reproducible project delivery.

## Main Project Theme

Build a **Job Posting Skill Analyzer**.

Analyze job descriptions to identify:

- common technical skills
- common tools, platforms, and frameworks
- repeated role patterns or job families
- beginner learning priorities
- suggested beginner learning paths
- portfolio project ideas
- risks and limitations in the dataset

Helpful CSV columns:

```text
job_id,job_title,company,location,job_description,job_skills,posted_date,source
```

Your CSV should include at least `job_title` and `job_description`.

## Job Posting Data Source Options

Use one of these data paths:

### Option A: Use a public Kaggle dataset

Use a public job postings dataset such as:

- [LinkedIn Job Postings (2023 - 2024)](https://www.kaggle.com/datasets/arshkon/linkedin-job-postings)
- [1.3M Linkedin Jobs & Skills (2024)](https://www.kaggle.com/datasets/asaniczka/1-3m-linkedin-jobs-and-skills-2024)

For the MVP, use a small subset of about 50-100 rows. Your CSV should include at least `job_title` and `job_description`. If the full dataset is large, create a smaller CSV before running the analyzer.

### Option B: Collect job postings yourself

This is optional and more advanced. If you collect postings yourself:

- Only collect public pages that allow access.
- Follow website terms and classroom guidance.
- Avoid login-gated, paywalled, or protected pages.
- Do not scrape LinkedIn directly unless your instructor explicitly approves a compliant source.
- Rate-limit requests and keep the dataset small.
- Save the collected data as a local CSV before running the analyzer.

Do not make live scraping part of the main analyzer pipeline. The capstone project should still consume a saved CSV file.

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

For job postings, `llm_interpretation` should include `common_skills`, `common_tools`, `role_clusters`, `learning_priorities`, `beginner_learning_path`, and `portfolio_project_ideas`.

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
| sample input or dataset link | Kaggle dataset link, prepared subset, or documented self-collected CSV |
| `postmortem.md` | One issue encountered and how it was handled |
| `prompts.md` or `ai_usage.md` | Prompt and AI Agent Coding Tool usage notes |

## Acceptance Criteria

- A reviewer can run the project on a small-to-medium CSV using the README.
- The run performs a real LLM call and saves evidence of the prompt/raw response.
- The project avoids sending the full dataset to the LLM.
- `report.json` preserves the required top-level schema across runs.
- `report.md` includes a readable overview, data quality notes, LLM-generated interpretation, recommendations, and risk notes.
- Failures have understandable error messages.
- The README documents whether the data came from Kaggle or a self-collected CSV.
- The analysis avoids sending full job descriptions in bulk to the LLM.

## Stretch Goals (Optional)

These are optional and should not replace the MVP:

- Add charts to the Markdown report.
- Support Excel input.
- Support both hosted API and Ollama backends.
- Add caching based on input file hash.
- Add a CLI flag for different report styles.
