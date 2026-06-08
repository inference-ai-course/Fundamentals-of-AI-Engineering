# Week 6: Job Posting Skill Analyzer Capstone

Week 6 integrates the course into one small project: read a CSV of job postings, profile the data, compress or sample what matters, call a **real LLM** for structured interpretation, and write both JSON and Markdown reports about skills and learning priorities.

The required MVP is intentionally fixed:

```text
CSV input -> data overview -> sampled/compressed summary -> real LLM interpretation -> report.json + report.md
```

## How the skill analysis works

The "analysis" — identifying skills, clustering roles, ranking what to learn —
happens in the **LLM stage**. Every earlier stage exists to gather and compress
*skill-relevant evidence* so the model can reason over it cheaply and the same
way every run:

| Stage | Role in the skill analysis |
|-------|-----------------------------|
| **Load** | Read the CSV. `job_description` holds most skill signal; `job_skills` is explicit but often empty. |
| **Profile** | Context: top job titles, missing values, counts. |
| **Compress** | Cheap, deterministic **skill evidence**: title/location counts, sampled `job_skills`, keyword frequency hints, and short truncated descriptions. Never the full CSV. |
| **LLM** | The real analysis: extract skills/tools, cluster roles, rank learning priorities, build a beginner path, propose projects — grounded in the evidence. |
| **Report** | Map the model's skill fields into `report.json` under `llm_interpretation`, with stable top-level keys. |

Walkthrough: [03_skill_analysis.md](03_skill_analysis.md) (lab notebook runs the
whole flow offline on the real sample).

## Main Project

Build a **Job Posting Skill Analyzer**.

Your project should analyze job descriptions to identify:

- common technical skills
- common tools, platforms, and frameworks
- repeated role patterns or job families
- beginner learning priorities
- suggested beginner learning paths
- portfolio project ideas
- risks and limitations in the dataset

Helpful columns:

```text
job_id,job_title,company,location,job_description,job_skills,posted_date,source
```

Your CSV should include at least `job_title` and `job_description`.

## Data Source Options

Choose one data path:

1. **Use a public Kaggle dataset** such as [LinkedIn Job Postings (2023 - 2024)](https://www.kaggle.com/datasets/arshkon/linkedin-job-postings). The larger [1.3M Linkedin Jobs & Skills (2024)](https://www.kaggle.com/datasets/asaniczka/1-3m-linkedin-jobs-and-skills-2024) dataset is also acceptable if you create a small subset first.
2. **Collect job postings yourself** as an optional advanced path. Only collect public pages that allow access, follow website terms, avoid login-gated pages, do not scrape LinkedIn directly unless your instructor explicitly approves a compliant source, rate-limit requests, and save the result as a CSV before analysis.

For the MVP, analyze about 50-100 rows. The analyzer should always start from a saved local CSV, not from live scraping.

## What You Should Be Able to Do

By the end of this week, you should be able to:

- Reuse Week 3 data profiling ideas.
- Reuse Week 4 structured prompts, real LLM calls, timeout/retry or repair, and output validation.
- Use Week 5 data/ML intuition to explain patterns and risks.
- Produce stable `report.json` and readable `report.md` outputs.
- Demo the project and explain one design decision.

## Main Materials

Capstone-required:

- [../capstone.md](../capstone.md)
- [simplified_project.md](simplified_project.md)
- [capstone_template/](capstone_template/)
- [01_pipeline_design.md](01_pipeline_design.md)
- [02_sampling_compression.md](02_sampling_compression.md)
- [03_skill_analysis.md](03_skill_analysis.md)

Theme examples:

- [Job posting skill analyzer schema](capstone_template/theme_examples/job_posting_schema.md)

Useful Week 4 references:

- [../week_04/01_tokens_context.md](../week_04/01_tokens_context.md)
- [../week_04/02_prompt_contracts.md](../week_04/02_prompt_contracts.md)
- [../week_04/03_structured_outputs_validation.md](../week_04/03_structured_outputs_validation.md)
- [../week_04/08_llm_client_skeleton.md](../week_04/08_llm_client_skeleton.md)

Optional/advanced:

- [../week_04/09_openai_compatible_api.md](../week_04/09_openai_compatible_api.md)

## Template Workflow

Use `capstone_template/` as a scaffold, not as a finished answer. It includes file structure, function signatures, expected keys, and TODO comments.

Target command after you complete the TODOs:

```bash
python analyze.py --input ../data/sample_job_postings.csv --out output
```

`sample_job_postings.csv` is a small classroom sample. For a stronger final project, use a prepared Kaggle subset or a documented self-collected CSV.

The template is not expected to pass this command before you implement the missing pieces.

## MVP Requirements

Your completed project should:

- Accept a CSV file path.
- Compute data overview statistics:
  - column types
  - missing values
  - duplicate rows
  - basic numeric/categorical summaries
  - simple anomaly hints
- Avoid sending the full dataset to the LLM.
- Make a real LLM call using a structured prompt.
- Save the prompt and raw/validated LLM output.
- Add beginner-friendly timeout/retry or repair handling.
- Write `report.json` with stable top-level fields.
- Write `report.md` for human readers.
- Include setup and one-command run instructions.

Mock responses are allowed only while debugging. They are not enough for final submission.

## What to Complete

| File or Folder | Description |
|----------------|-------------|
| Source code | CLI script or small modular project |
| `output/report.json` | Machine-readable final report |
| `output/report.md` | Human-readable final report |
| `README.md` | Setup, API key/provider notes, and one-command run instructions |
| `requirements.txt` or `pyproject.toml` | Dependencies |
| sample input or dataset link | Dataset used for the successful run |
| `postmortem.md` | One issue encountered and how it was handled |
| `prompts.md` or `ai_usage.md` | Prompt and AI Agent Coding Tool usage notes |

## AI Agent Coding Tool Use

You may use Cursor, Kilo, Copilot Chat, ChatGPT, Claude, or similar tools to complete the template. Record:

- What prompt you used.
- Which suggestion you accepted.
- Which suggestion you rejected or changed.
- What you personally tested or verified.

## Stretch Goals

These are optional:

- Add charts to the Markdown report.
- Support Excel input.
- Support both hosted API and Ollama.
- Add caching based on input file hash.
- Add a CLI flag for different report styles.

## Optional Alternate Themes

If your instructor approves a different text-heavy CSV topic, you may adapt the same pipeline to customer feedback or product reviews. Keep the same input/output contract and report schema.

## Self-check Questions

- Can someone run your project from the README without hidden steps?
- Did your final run call a real LLM?
- Does `report.json` keep the same top-level shape across runs?
- What data did you send to the LLM, and what did you intentionally not send?
- What is one failure case your project handles clearly?
