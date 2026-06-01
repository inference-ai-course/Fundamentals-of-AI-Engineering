# Course Materials Update Summary

**Date**: 2026-04-02
**Status**: ✅ Completed

---

## Overview

Successfully implemented the course materials update plan, which included:
1. Week number reference updates in all notebooks and markdown files
2. Addition of bidirectional links between paired .md and .ipynb files
3. Special replacements (capstone → project, cross-week references)

---

## Changes Summary

### Files Modified
- **Total files**: 49 files
- **Notebooks (.ipynb)**: 19 files
- **Markdown (.md)**: 19 files  
- **Other files**: 11 files (READMEs, tutorials, SYLLABUS.md)

### Phase 1: Week Reference Updates

The week reference updates were mostly already completed in previous work sessions. My script identified and updated:

- **Notebooks updated**: 5 files (week_03 parts 04-08, and special cases)
- **Markdown files updated**: 1 file (week_06/05_pipeline_design.md)

**Update mappings applied**:
| Directory | Old Week | New Week | Part Updates |
|-----------|----------|----------|--------------|
| week_03   | Week 4/5 | Week 3   | Parts 01-08 unified |
| week_04   | Week 1   | Week 4   | Parts 01-02 |
| week_05   | Week 2   | Week 5   | Parts 01-03 |
| week_06   | Week 3/6 | Week 6   | Parts 01-06 unified |

**Special replacements**:
- "capstone" → "project" (in week_06/05_pipeline_design and week_03/06_rate_limiting)
- "Week 6 capstone" → "Week 6 project"
- Cross-week references in week_03/08_llm_client_skeleton updated

### Phase 2: Bidirectional Links Added

Successfully added bidirectional links to all 19 file pairs:

**In Notebooks**:
- Added link to markdown file at the end of first markdown cell
- Format: `📖 **配套教程**: [filename.md](./filename.md) - 理论详解与学习目标`

**In Markdowns**:
- Added link to notebook file after Overview section
- Format: `💻 **配套练习**: [filename.ipynb](./filename.ipynb) - 交互式代码实践`

**Example**:

Notebook (01_tokens_context.ipynb):
```
## Learning Objectives
- Understand tokenization basics
- Measure token counts in prompts
- Design prompts for context window constraints

📖 **配套教程**: [01_tokens_context.md](./01_tokens_context.md) - 理论详解与学习目标
```

Markdown (01_tokens_context.md):
```
## Overview

When working with LLMs, the most common "mysterious failures" are actually context budget failures.

---

💻 **配套练习**: [01_tokens_context.ipynb](./01_tokens_context.ipynb) - 交互式代码实践
```

---

## File Pairs Updated

All 19 pairs received bidirectional links:

1. week_03/01_local_inference_setup
2. week_03/02_ollama_http_client
3. week_03/03_benchmarking_script
4. week_03/04_timeouts_failures
5. week_03/05_retries_backoff
6. week_03/06_rate_limiting
7. week_03/07_caching_logging
8. week_03/08_llm_client_skeleton
9. week_04/01_environment_setup
10. week_04/02_data_profiling_script
11. week_05/01_training_loop
12. week_05/02_reproducibility_package
13. week_05/03_compare_runs_report
14. week_06/01_tokens_context
15. week_06/02_prompt_contracts
16. week_06/03_structured_outputs_validation
17. week_06/04_openai_compatible_api
18. week_06/05_pipeline_design
19. week_06/06_sampling_compression

---

## Validation

✅ All notebooks are valid JSON (verified with json.load())
✅ All markdown files are readable
✅ Bidirectional links added to all 19 pairs
✅ Backup created in `.backup_20260402_135403/` directory

---

## Git Statistics

```
49 files changed, 408 insertions(+), 205 deletions(-)
```

---

## Tools Created

1. `update_course_materials.py` - Week reference update script
2. `add_bidirectional_links.py` - Bidirectional link addition script

---

## Next Steps (Recommended)

1. Review changes in `git diff`
2. Open notebooks in Jupyter to verify rendering
3. Test bidirectional links navigation
4. Commit changes (if requested)

---

## Content Division Strategy (Implemented)

**Markdown files** now serve as:
- Authority for course structure, learning objectives, and theory
- Link to notebooks for interactive code practice

**Notebook files** now serve as:
- Authority for executable code and interactive exercises
- Link to markdown for detailed theory explanations

This creates a clear separation of concerns:
- **Markdown** = Theory & Concepts
- **Notebook** = Code & Practice

---

**Completed**: 2026-04-02T13:53:20-07:00