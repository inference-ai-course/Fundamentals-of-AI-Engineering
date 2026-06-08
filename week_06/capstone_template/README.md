# Capstone Template: Job Posting Skill Analyzer

This is a scaffold for the Week 6 capstone. It is intentionally incomplete.

Target pipeline:

```text
CSV input -> data profile -> compressed summary -> real LLM interpretation -> report.json + report.md
```

## What You Must Complete

Look for `TODO` comments in:

- `analyze.py`
- `src/data_profile.py`
- `src/compression.py`
- `src/llm_interpretation.py`
- `src/report_builder.py`

The template should not run end-to-end until you complete those TODOs.

## Setup

Create an environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Configure your real LLM provider. The exact environment variable depends on your provider and classroom setup.

Example:

```bash
export OPENAI_API_KEY="your-key-here"
```

## Target Run Command

After completing the TODOs, your project should support:

```bash
python analyze.py --input ../data/sample_job_postings.csv --out output
```

This command is a target, not proof that the untouched template is complete. For the final project, replace the sample path with your prepared Kaggle subset or documented self-collected job postings CSV.

## Expected Outputs

Your completed project should write:

```text
output/
  profile.json
  compressed_input.json
  llm_prompt.txt
  llm_raw_response.txt
  report.json
  report.md
```

## LLM Output to Report Mapping

`src/llm_interpretation.py` asks the LLM for:

- `summary`
- `insights`
- `recommendations`
- `risk_notes`

`src/report_builder.py` should map those fields into the final `report.json` like this:

- `llm_interpretation.summary` <- `summary`
- `llm_interpretation.insights` <- `insights`
- `recommendations` <- `recommendations`
- `risk_notes` <- `risk_notes`

Keep the top-level report keys stable even if your chosen theme adds extra fields inside `llm_interpretation`.

## Job Posting Skill Analyzer Requirements

Your CSV should include at least:

```text
job_title,job_description
```

Helpful optional columns include:

```text
job_id,company,location,job_skills,posted_date,source
```

You may use a public Kaggle dataset such as [LinkedIn Job Postings (2023 - 2024)](https://www.kaggle.com/datasets/arshkon/linkedin-job-postings), or you may collect a small CSV yourself as an advanced option. The larger [1.3M Linkedin Jobs & Skills (2024)](https://www.kaggle.com/datasets/asaniczka/1-3m-linkedin-jobs-and-skills-2024) dataset is also acceptable if you create a small subset first. If you collect data yourself, only collect public pages that allow access, follow website terms, avoid login-gated pages, do not scrape LinkedIn directly unless your instructor explicitly approves a compliant source, rate-limit requests, and save the result as a local CSV before analysis.

For this theme, ask the LLM for job-specific fields such as:

- `common_skills`
- `common_tools`
- `role_clusters`
- `learning_priorities`
- `beginner_learning_path`
- `portfolio_project_ideas`

Map those fields inside `llm_interpretation` while preserving the required top-level report schema:

- `llm_interpretation.common_skills` <- `common_skills`
- `llm_interpretation.common_tools` <- `common_tools`
- `llm_interpretation.role_clusters` <- `role_clusters`
- `llm_interpretation.learning_priorities` <- `learning_priorities`
- `llm_interpretation.beginner_learning_path` <- `beginner_learning_path`
- `llm_interpretation.portfolio_project_ideas` <- `portfolio_project_ideas`

Do not send full job descriptions in bulk to the LLM. Compress them first with title counts, skill hints, shortened representative descriptions, and any useful data quality notes.

## Required Final Evidence

- The final run must call a real LLM.
- Save the prompt and raw/validated LLM response.
- Do not send the full CSV to the LLM.
- Preserve the required top-level keys in `report.json`.
- Document AI Agent Coding Tool use in `prompts.md` or `ai_usage.md`.

## Suggested AI Agent Prompts

```text
Explain the TODOs in this project before writing code.
Which file should I complete first and why?
```

```text
Help me complete build_profile().
Keep the output keys stable and explain how I should test it.
```

```text
Help me add a real LLM call.
Ask me which provider I am using before writing provider-specific code.
```

```text
Review my report.json output against the required schema.
Tell me what is missing before suggesting edits.
```
