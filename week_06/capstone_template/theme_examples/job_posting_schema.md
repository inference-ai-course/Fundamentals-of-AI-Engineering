# Project Schema: Job Posting Skill Analyzer

Use this for the Week 6 capstone. Your CSV should contain job postings, role descriptions, or hiring requirements.

## Helpful Input Columns

```text
job_id,job_title,company,location,job_description,job_skills,posted_date,source
```

Your dataset does not need exactly these names, but it should include at least `job_title` and `job_description`.

## Data Source Options

Choose one data path:

1. **Use a public Kaggle dataset** such as [LinkedIn Job Postings (2023 - 2024)](https://www.kaggle.com/datasets/arshkon/linkedin-job-postings). For the MVP, use a small subset of about 50-100 rows. The larger [1.3M Linkedin Jobs & Skills (2024)](https://www.kaggle.com/datasets/asaniczka/1-3m-linkedin-jobs-and-skills-2024) dataset is also acceptable if you create a small subset first.
2. **Collect job postings yourself** as an optional advanced path. Only collect public pages that allow access, follow website terms, avoid login-gated pages, do not scrape LinkedIn directly unless your instructor explicitly approves a compliant source, rate-limit requests, and save the result as a CSV before analysis.

Do not make live scraping part of the analyzer pipeline. The project should still start from a saved CSV file.

Example command:

```bash
python analyze.py --input ../data/sample_job_postings.csv --out output
```

For the final project, replace the sample path with your prepared Kaggle subset or documented self-collected CSV.

## Prompt Adaptation

Ask the LLM to focus on:

- common technical skills
- common tools, platforms, and frameworks
- role clusters or repeated job families
- beginner learning priorities
- suggested beginner learning path
- portfolio project ideas
- risks and limitations in the dataset

## Compression Notes

Job descriptions can be long. Do not send every full description to the LLM. Include compact evidence such as:

- top job titles
- top locations or remote/on-site counts
- existing `job_skills` values, if present
- keyword frequency hints
- shortened representative descriptions
- a few unusual or edge-case postings

## Theme-Specific `llm_interpretation` Fields

You may include:

```json
{
  "common_skills": [],
  "common_tools": [],
  "role_clusters": [],
  "learning_priorities": [],
  "beginner_learning_path": [],
  "portfolio_project_ideas": []
}
```

Keep the main `report.json` top-level schema unchanged.
