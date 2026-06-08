# Week 6 — Capstone Template Completion Guide

This guide explains how to complete the capstone template without turning it into a copy-paste solution. The Week 6 project is a **Job Posting Skill Analyzer** built on a reusable CSV-to-report pipeline:

```text
CSV input -> data profiling -> compressed summary -> real LLM interpretation -> report.json + report.md
```

The provided template gives structure, function signatures, TODOs, and expected outputs. You must fill in the implementation.

## What the Template Is

The template is a scaffold:

- It shows the files a small project should have.
- It names the main functions and their input/output contracts.
- It leaves key logic as TODOs.
- It gives prompts you can use with an AI Agent Coding Tool.

The template is **not** a finished project and should not run end-to-end until you complete it.

## What You Must Complete

### Stage 1: Data Profiling

File: `capstone_template/src/data_profile.py`

Complete:

- CSV loading or dataframe handling.
- Row and column counts.
- Column names and data types.
- Missing value counts.
- Duplicate row count.
- Basic numeric summaries.
- Basic categorical summaries.
- Simple anomaly hints.

AI Agent prompt idea:

```text
Help me complete build_profile() for a beginner capstone.
First explain the expected input/output contract, then suggest code.
Do not remove the required top-level keys.
```

### Stage 2: Compression

File: `capstone_template/src/compression.py`

Complete:

- A compact summary for the LLM.
- Deterministic sample rows.
- Selected numeric and categorical summaries.
- Token-budget estimate or note.

Do not send the full CSV to the LLM.

AI Agent prompt idea:

```text
Help me implement compress_profile(profile, df).
The output should be compact enough for an LLM and should not include the full dataset.
Use a fixed random seed for sampling.
```

### Stage 3: Real LLM Interpretation

File: `capstone_template/src/llm_interpretation.py`

Complete:

- Structured prompt assembly.
- Real LLM API call.
- Timeout/retry or repair attempt.
- Raw response saving.
- Basic output validation.

Mock responses may help local debugging, but the final submission must include a successful real LLM run.

AI Agent prompt idea:

```text
Help me add a real LLM call to call_llm().
Keep the response JSON-shaped, save the raw response, and add clear error handling.
Ask me what provider/API style I am using before writing provider-specific code.
```

### Stage 4: Report Building

File: `capstone_template/src/report_builder.py`

Complete:

- `output/report.json` with stable top-level keys.
- `output/report.md` with a readable summary.
- Recommendations and risk notes from the LLM result.
- Errors or warnings surfaced clearly.

AI Agent prompt idea:

```text
Help me complete build_json_report() and build_markdown_report().
Keep the JSON top-level schema stable and make the Markdown readable for a nontechnical reviewer.
```

## Main Project: Job Posting Skill Analyzer

- Analyze job descriptions to identify common skills, tools/platforms, role patterns, and beginner learning priorities.
- Use a CSV with at least `job_title` and `job_description`.
- Helpful columns include `job_id`, `job_title`, `company`, `location`, `job_description`, `job_skills`, `posted_date`, and `source`.
- Ask the LLM for common skills, common tools, role clusters, learning priorities, beginner learning path suggestions, portfolio project ideas, and limitations.

Choose one data path:

1. **Use a public Kaggle dataset** such as [LinkedIn Job Postings (2023 - 2024)](https://www.kaggle.com/datasets/arshkon/linkedin-job-postings). Use a small subset of about 50-100 rows for the MVP. The larger [1.3M Linkedin Jobs & Skills (2024)](https://www.kaggle.com/datasets/asaniczka/1-3m-linkedin-jobs-and-skills-2024) dataset is also acceptable if you create a small subset first.
2. **Collect job postings yourself** as an optional advanced path. Only collect public pages that allow access, follow website terms, avoid login-gated pages, do not scrape LinkedIn directly unless your instructor explicitly approves a compliant source, rate-limit requests, and save the result as a CSV before analysis.

Do not make live scraping part of the analyzer pipeline. The analyzer should still start from a local CSV file.

Suggested Markdown report sections for this theme:

- Dataset overview.
- Data quality notes.
- Most common roles.
- Common technical skills.
- Common tools and platforms.
- Learning priorities.
- Suggested beginner learning path.
- Portfolio project ideas.
- Risks and limitations.

The project is job-posting-specific, but it still keeps the same report contract.

## Target Output Schema

Your final `report.json` should preserve these top-level fields:

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

Map the validated LLM response into that schema consistently:

- `summary` and `insights` belong inside `llm_interpretation`.
- `recommendations` becomes the top-level `recommendations` list.
- `risk_notes` becomes the top-level `risk_notes` list.
- Any parse failures, repair attempts, or missing-data cautions belong in `errors_or_warnings`.

## Target Command

After completing the TODOs, your project should support a command like:

```bash
python analyze.py --input ../data/sample_job_postings.csv --out output
```

For the final project, replace the sample path with your prepared Kaggle subset or documented self-collected job postings CSV. This is the target command, not a guarantee that the untouched template already works.

## Minimum Validation Checklist

- [ ] The project accepts a CSV path.
- [ ] The project does not send the full CSV to the LLM.
- [ ] The final run calls a real LLM.
- [ ] The prompt and raw/validated LLM response are saved.
- [ ] `output/report.json` exists and preserves the required top-level keys.
- [ ] `output/report.md` exists and is readable.
- [ ] README includes setup, API key/provider notes, and one-command run instructions.
- [ ] `prompts.md` or `ai_usage.md` explains AI Agent Coding Tool use.
- [ ] `postmortem.md` documents one real issue and fix.
- [ ] For job postings, the README documents whether the CSV came from Kaggle or self-collection.

## References

- Week 3: Data profiling.
- Week 4: Structured prompts, real LLM calls, timeout/retry, and validation.
- Week 5: Data/ML interpretation intuition.
- Week 6: Pipeline design and sampling/compression.
