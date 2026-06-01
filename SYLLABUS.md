# AI Engineering Fundamentals - Course Syllabus

## Course Information

| Attribute | Details |
|-----------|---------|
| **Course Name** | AI Engineering Fundamentals |
| **Version** | v2.2 (6-Week Beginner Program) |
| **Duration** | 6 weeks |
| **Weekly Hours** | 5 hours recommended |
| **Delivery Method** | In-person instruction + hands-on workshops |
| **Target Students** | AI beginners; no programming background required before the course |

## Course Introduction

AI Engineering Fundamentals is designed for students who are new to AI tools, programming, and applied AI development. The course uses a staged learning path:

**Agent Tools Introduction -> AI-Assisted Python Setup and Code Practice -> Data Processing -> LLM Workflows -> ML Baselines -> Capstone**

Week 1 requires no programming. Students learn how to use AI tools, ask useful questions, and review AI-generated answers. In Week 2, students begin guided Python execution with AI assistance: environment setup, running code, reading code, small edits, and debugging. Starting in Week 3, students use that prepared environment for data processing, LLM calls, simple ML experiments, and a capstone.

### Core Philosophy

**"Learn AI with AI"** - AI tools should accelerate learning, but students still need to verify outputs, explain their work, and understand the workflow they practice.

## Learning Objectives

Upon completing this course, students will be able to:

1. Use mainstream AI tools such as ChatGPT, Claude, Cursor, Kilo, or Copilot Chat for practical tasks.
2. Use AI tools to learn Python, create a clean environment, run code, modify small scripts, and debug errors.
3. Generate reproducible CSV profiling reports with pandas.
4. Design structured prompts, request JSON-like outputs, and add basic reliability controls to LLM calls.
5. Train and compare two lightweight ML baseline runs.
6. Build and demo an intelligent data analysis script that turns CSV input into JSON and Markdown reports.

## Weekly Schedule

### Week 1: Agent Tools Introduction

**Theme:** Using AI Without Writing Code

#### Learning Objectives

- Understand what AI agent tools are and what they can/cannot do.
- Practice basic prompting and follow-up questions.
- Compare chat tools and agent/editor tools for everyday tasks.

#### Sessions

- Agent tools overview: ChatGPT, Claude, Cursor, Kilo, Copilot Chat.
- Hands-on tool practice: writing, summarizing, explaining, and planning tasks.
- Reflection: when to trust AI, when to verify, and how to document AI usage.

#### What to Complete

- 3 AI tool experience cases.
- Representative prompts or screenshots/interaction notes.
- Short reflection report.

#### Resources

- [week_01/README.md](week_01/README.md)
- [slides/week_01.md](slides/week_01.md)

### Week 2: AI-Assisted Python Setup + Code Practice

**Theme:** Learning Python With AI, Then Running and Debugging Code

#### Learning Objectives

- Open a project in VS Code or Cursor.
- Reuse Week 1 prompt patterns for Python learning.
- Create and activate a Python virtual environment.
- Install dependencies and verify `pandas`.
- Run simple Python scripts or notebooks.
- Use AI to explain simple Python files.
- Make small guided code modifications.
- Debug one provided error with AI assistance.

#### Sessions

- IDE setup and basic navigation.
- AI tutor workflows: ChatGPT, Claude, Cursor, Copilot Chat, and optional Claude Code Learning style.
- Python environment setup: `.venv`, `pip`, `requirements.txt`, and notebook kernels.
- Run-code lab using template functions and optional notebooks.
- Code reading with AI using `week_02/code_templates/`.
- Small modifications and debugging workshop.

#### What to Complete

- AI Python learning prompt log.
- Environment verification output.
- Code run evidence from scripts or notebooks.
- Explanation notes for at least 5 functions.
- 2-3 small code modifications based on provided templates.
- One debugging record: error, AI prompt, fix, and verification.

#### Resources

- [week_02/README.md](week_02/README.md)
- [slides/week_02.md](slides/week_02.md)

### Week 3: Data Processing + Reproducible Outputs

**Theme:** The Foundation of AI - Data and Reproducibility

#### Learning Objectives

- Activate and verify the Week 2 Python environment.
- Load CSV files with pandas.
- Generate stable data profiling outputs.

#### Sessions

- Week 2 environment preflight: active Python, `pandas`, and output location.
- Data profiling: row counts, column types, missing values, duplicates, simple statistics, and Markdown/JSON output.
- Workshop: run the profiler on a provided or student-selected CSV.

#### What to Complete

- A runnable data profiling script.
- `profile.json` and `profile.md` sample outputs.
- A short data quality note explaining at least 3 findings.
- Manual test checklist is acceptable; automated tests are optional.

#### Resources

- [week_03/README.md](week_03/README.md)
- [slides/week_03.md](slides/week_03.md)

### Week 4: LLM Fundamentals + API Reliability

**Theme:** Structured LLM Calls That Code Can Use

#### Learning Objectives

- Explain tokens, context windows, and why long inputs fail.
- Write prompts as contracts with explicit input and output expectations.
- Parse and validate structured outputs.
- Add beginner-friendly timeout, retry, and logging practices.
- Turn a Week 3 data profile into structured insight JSON without requiring an API key.

#### Sessions

- LLM basics: tokens, context, prompt structure, JSON output.
- Structured outputs: parsing, validation, and repair prompts.
- API reliability: timeout, bounded retry/repair, saved raw responses, and basic logging.
- Offline profile-to-insights demo using Week 3 `profile.json`.

#### What to Complete

- A structured-output demo that returns parseable JSON for Week 3 `profile.json` and at least 2 additional small test inputs or simulated responses.
- Reliability notes covering timeout/max wait, bounded retry/repair, and saved raw responses.
- A short reliability reflection: one failure mode and how you handled it.
- Hosted API, Ollama, provider setup, rate limiting, caching, and full client skeletons are optional extensions.

#### Resources

- [week_04/README.md](week_04/README.md)
- [slides/week_04.md](slides/week_04.md)

### Week 5: ML Training Loop

**Theme:** Understanding the Machine Learning Workflow

#### Learning Objectives

- Explain train/validation splits and overfitting in plain language.
- Train a simple baseline model.
- Save metrics and compare two runs.

#### Sessions

- ML fundamentals: training, inference, validation, and metrics.
- Guided scikit-learn baseline.
- Run comparison and short report writing.

#### What to Complete

- Two lightweight baseline runs.
- Saved configs/metrics or a simple comparison table.
- Short report explaining what changed, what happened, and one next step.

#### Resources

- [week_05/README.md](week_05/README.md)
- [slides/week_05.md](slides/week_05.md)

### Week 6: Capstone - AI-Assisted CSV Data Analyzer

**Theme:** CSV In, AI-Assisted Report Out

#### Learning Objectives

- Combine data profiling, sampling/compression, and real LLM interpretation.
- Produce stable JSON and Markdown reports.
- Explain design decisions and demo a reproducible run.

#### Sessions

- Capstone MVP walkthrough: CSV -> profile -> sampled summary -> real LLM interpretation -> report.
- Implementation workshop using provided templates and prior-week components.
- Demo, reflection, and next learning path.

#### What to Complete

- A reproducible script or small project that accepts a CSV input.
- `report.json` and `report.md` outputs.
- Evidence of a real LLM call, including saved prompt and raw/validated response.
- Short demo or walkthrough.
- `postmortem.md` or reflection documenting one issue and fix.

#### Resources

- [week_06/README.md](week_06/README.md)
- [slides/week_06.md](slides/week_06.md)
- [capstone.md](capstone.md)

## Study Tips

- Treat AI as a collaborator: ask it to explain, but verify the result.
- Keep every week runnable: commands, inputs, outputs, and environment notes matter.
- Prefer small working examples over large unfinished projects.
- Document prompts that changed your work meaningfully.

## FAQ

**Q: I have no programming experience. Can I still take this course?**
Yes. Week 1 requires no programming. Week 2 introduces guided Python execution with AI assistance, and students are not expected to write independent programs from scratch.

**Q: Do I need to finish self_learn before Week 1?**
No. `self_learn/` is optional reference material for students who want extra practice.

**Q: Do I need ChatGPT Plus or paid APIs?**
No paid subscription is required for the course design. Week 4's required demo runs offline with mock responses; hosted APIs, instructor-provided APIs, and local inference are optional extensions.

**Q: Is the final project open-ended?**
The required MVP is fixed: CSV input -> `report.json` + `report.md`. Extra UI, Excel support, multi-backend LLM support, and caching are stretch goals.

## Course Changelog

### v2.2 (2026-05-11)

- Moved Python environment setup and first code-running practice into Week 2.
- Added Week 2 AI Python tutor prompts, code-running evidence, and debugging evidence.
- Changed Week 3 to assume the Week 2 environment and focus on data profiling.

### v2.1 (2026-05-04)

- Moved data processing to Week 3.
- Moved LLM fundamentals and simplified API reliability to Week 4.
- Kept Week 5 focused on lightweight ML baselines.
- Unified Week 6 around the intelligent data analysis capstone.
- Clarified that `self_learn/` and `old_v1/` are optional references.

### v2.0 (2026-04-01)

- Compressed the original 8-week course to 6 weeks.
- Added Week 1-2 AI agent tools introduction.
- Lowered the programming barrier for beginners.

---

**Last Updated:** 2026-05-11
**Version:** v2.2
