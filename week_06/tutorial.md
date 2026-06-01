# Week 6 Tutorials: AI-Assisted CSV Data Analyzer Capstone

## Pre-study (Optional Refresher)

Self-learn is optional. If you want extra background:

- [Pre-study guide](../PRESTUDY.md)
- [Self-learn - Chapter 3: AI Engineering Fundamentals](../self_learn/Chapters/3/Chapter3.md)
- [Self-learn - Chapter 4: Hugging Face Platform and Local Inference](../self_learn/Chapters/4/Chapter4.md)

## Overview

Week 6 integrates prior work into one reproducible project:

```text
CSV input -> data overview -> sampled/compressed summary -> real LLM interpretation -> report.json + report.md
```

The default topic is a general CSV data analyzer. Recommended concrete themes are customer feedback/support tickets and product reviews.

## Main Navigation

- [Simplified project](simplified_project.md)
- [Capstone template](capstone_template/)
- [Pipeline design](01_pipeline_design.md)
- [Sampling and compression](02_sampling_compression.md)
- [Capstone requirements](../capstone.md)

## Useful References

- [Tokens and context windows](../week_04/01_tokens_context.md)
- [Prompt contracts](../week_04/02_prompt_contracts.md)
- [Structured outputs and validation](../week_04/03_structured_outputs_validation.md)

## Recommended Order

1. Review the required MVP in `capstone.md`.
2. Choose the general data analyzer path or one recommended theme.
3. Inspect `capstone_template/` and identify the TODOs.
4. Build the CSV data overview stage.
5. Add sampling/compression before the LLM call.
6. Add structured real LLM interpretation.
7. Write `report.json` and `report.md`.
8. Prepare a short demo, `prompts.md` or `ai_usage.md`, and `postmortem.md`.
