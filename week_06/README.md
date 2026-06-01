# Week 6: Capstone - Intelligent Data Analysis Script

Week 6 integrates the course into one small project: read a CSV file, profile the data, compress or sample what matters, ask an LLM for structured insights, and write both JSON and Markdown reports.

The required MVP is intentionally fixed:

```text
CSV input -> data overview -> sampled/compressed summary -> LLM interpretation -> report.json + report.md
```

## Pre-study (Optional Refresher)

Self-learn is optional. Use these only if you want extra background:

- [Pre-study guide](../PRESTUDY.md)
- [Self-learn - Chapter 3: AI Engineering Fundamentals](../self_learn/Chapters/3/Chapter3.md)
- [Self-learn - Chapter 4: Hugging Face Platform and Local Inference](../self_learn/Chapters/4/Chapter4.md)

## What You Should Be Able to Do

By the end of this week, you should be able to:

- Build a reproducible CSV analysis workflow.
- Reuse Week 3 data profiling ideas.
- Reuse Week 4 structured prompt and reliability ideas.
- Use Week 5 ML/data intuition to explain patterns and risks.
- Produce stable `report.json` and readable `report.md` outputs.
- Demo the project and explain one design decision.

## Tutorials

Capstone-required materials:

- [simplified_project.md](simplified_project.md)
- [05_pipeline_design.md](05_pipeline_design.md)
- [06_sampling_compression.md](06_sampling_compression.md)
- [../capstone.md](../capstone.md)

Useful Week 4 references:

- [01_tokens_context.md](01_tokens_context.md)
- [02_prompt_contracts.md](02_prompt_contracts.md)
- [03_structured_outputs_validation.md](03_structured_outputs_validation.md)

Optional/advanced:

- [04_openai_compatible_api.md](04_openai_compatible_api.md)

## MVP Requirements

Your project should:

- Accept a CSV file path.
- Compute data overview statistics:
  - column types
  - missing values
  - duplicate rows
  - basic numeric/categorical summaries
  - simple anomaly hints
- Avoid sending the full dataset to the LLM.
- Use a structured prompt for insights, recommendations, and risk notes.
- Write `report.json` with stable fields.
- Write `report.md` for human readers.
- Include setup and one-command run instructions.

## Suggested Project Structure

```text
analyze.py
src/
  data_profile.py
  sampling.py
  llm_client.py
  report_builder.py
tests/ or smoke_test.py
output/
README.md
requirements.txt
postmortem.md
prompts.md
```

## What to Complete

- Source code or notebook/script.
- `output/report.json`.
- `output/report.md`.
- README with one-command run instructions.
- Sample input or link to dataset.
- `postmortem.md` documenting one issue and how it was handled.
- AI usage and prompt documentation.

## Stretch Goals

These are optional:

- Add charts to the Markdown report.
- Support Excel input.
- Support both hosted API and Ollama.
- Add caching based on input file hash.
- Add a CLI flag for different report styles.

## Self-check Questions

- Can someone run your project from the README without hidden steps?
- Does `report.json` keep the same shape across runs?
- What data did you send to the LLM, and what did you intentionally not send?
- What is one failure case your project handles clearly?
