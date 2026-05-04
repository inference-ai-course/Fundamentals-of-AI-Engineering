# Week 6: AI-Assisted CSV Data Analyzer Capstone

Week 6 integrates the course into one small project: read a CSV file, profile the data, compress or sample what matters, call a **real LLM** for structured interpretation, and write both JSON and Markdown reports.

The required MVP is intentionally fixed:

```text
CSV input -> data overview -> sampled/compressed summary -> real LLM interpretation -> report.json + report.md
```

## Topic Choices

Default: build a general CSV data analyzer.

Recommended concrete themes:

1. **Customer Feedback / Support Ticket Analyzer**
   - Good for tickets, reviews, surveys, or support messages.
   - LLM value: themes, urgent issues, customer risks, recommended actions.

2. **Product Review Insight Reporter**
   - Good for product/app/course reviews.
   - LLM value: positive themes, negative themes, feature requests, product risks.

Other CSV topics are allowed if they keep the same input/output contract.

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

Useful Week 4 references:

- [../week_04/01_tokens_context.md](../week_04/01_tokens_context.md)
- [../week_04/02_prompt_contracts.md](../week_04/02_prompt_contracts.md)
- [../week_04/03_structured_outputs_validation.md](../week_04/03_structured_outputs_validation.md)

Optional/advanced:

- [../week_04/09_openai_compatible_api.md](../week_04/09_openai_compatible_api.md)

## Template Workflow

Use `capstone_template/` as a scaffold, not as a finished answer. It includes file structure, function signatures, expected keys, and TODO comments.

Target command after you complete the TODOs:

```bash
python analyze.py --input ../data/sample_sales.csv --out output
```

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

## Self-check Questions

- Can someone run your project from the README without hidden steps?
- Did your final run call a real LLM?
- Does `report.json` keep the same top-level shape across runs?
- What data did you send to the LLM, and what did you intentionally not send?
- What is one failure case your project handles clearly?
