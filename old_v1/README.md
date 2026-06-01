# Foundational Course (Foundation) Overview & 8-Week Plan

## Positioning

**Foundational Course** is designed for learners who need to build GenAI/LLM engineering fundamentals from 0 to 1. The emphasis is on **concept intuition + Python hands-on practice + reproducible small project delivery**.

## Target Learners

*   Complete beginners (non-technical background) who want to transition into AI/data/application development
*   Developers with a technical background but without a systematic AI foundation (want to fill in ML/LLM fundamentals and engineering habits)

## Prerequisites

*   Can do basic CLI operations (install dependencies, run scripts, read logs)
*   Has basic programming concepts (variables, conditionals, loops, functions). If not, complete Python crash course before starting (Including data structures & Algorithm questions on Leetcode, some OOP concepts and practice).

## Self-learn Navigation (Pre-study)

Foundational Course assumes Self-learn is complete. Use these as the canonical fundamentals reference:

*   [Self-learn schedule](self_learn/Schedule.md)
*   Chapters:
    *   [Chapter 1: Tool Preparation](self_learn/Chapters/1/Chapter1.md)
    *   [Chapter 2: Python and Environment Management](self_learn/Chapters/2/Chapter2.md)
    *   [Chapter 3: AI Engineering Fundamentals](self_learn/Chapters/3/Chapter3.md)
    *   [Chapter 4: Hugging Face Platform and Local Inference](self_learn/Chapters/4/Chapter4.md)
    *   [Chapter 5: Resource Monitoring and Containerization](self_learn/Chapters/5/Chapter5.md)

## For Learners Without an Engineering Background

If you have never used Git, testing frameworks, or production-style logging, Foundational Course is still designed to be approachable:

*   Git is helpful but not required at the beginning (a zipped project folder is an acceptable submission format).
*   Automated tests are introduced gradually; early on, a clear manual test checklist is acceptable.
*   The course emphasizes "runnable code + reproducible outputs" over advanced engineering patterns.

## Onboarding Checklist (Week 0)

Before Week 1, learners should be able to complete these steps end-to-end:

*   Install Python 3.10+ and confirm `python --version`
*   Create and activate a virtual environment (venv/conda are both fine)
*   Install dependencies from `requirements.txt` (or `pyproject.toml`) and run a script successfully
*   Use Git for clone/commit/pull (or have a clear alternative for submitting code)
*   Set environment variables for secrets via `.env` (do not hardcode API keys)
*   (Optional) Install Ollama and run one local model once

If any of the above steps fail, the learner should be able to provide:

*   The exact command they ran
*   The full error output
*   Their OS/Python version

## How to Ask for Help (Required)

When you ask for help (from instructors, classmates, or online), follow this procedure:

1. Reproduce the issue at least once (do not guess).
2. Copy/paste the exact command you ran and the full output.
3. Identify what you expected vs what happened.
4. Do a quick search first (official docs / error message / GitHub issues).
5. Make a minimal reproduction if possible (smallest script/input that still fails).
6. Share what you already tried (so others do not repeat your steps).

Why this procedure works:

- It turns debugging from "opinions" into evidence.
- It minimizes back-and-forth questions (others can run the same command and see the same failure).
- It helps you learn faster because you practice isolating variables.

A strong help request example (copy/paste style):

```text
Goal: Run Week 2 baseline training script and save artifacts.
Context: foundational_course/week_02 Part 01, running train.py.

Command:
  python train.py --input data.csv --label_col label --seed 42

Expected:
  Script prints metrics and creates artifacts/run_.../metrics.json

Actual:
  ValueError: label_col not found: label

Environment:
  OS: Ubuntu 22.04
  Python: 3.11.6
  requirements.txt: pandas==2.2.3, scikit-learn==1.5.2

What I tried:
  - Opened data.csv and saw the column is named `target`, not `label`.
  - Re-ran with --label_col target and it worked.
  - Remaining question: should we standardize on `label` or allow configurable label columns?
```

Notice how this request includes a reproducible command, the full error, and the smallest relevant detail (the column name). That's what makes it easy to help.

Required items in every help request:

*   Goal: what you are trying to do
*   Context: which assignment / which step
*   Exact command(s) + full output (not screenshots only)
*   Your environment: OS, Python version, dependency file (`requirements.txt` or `pyproject.toml`)
*   Relevant code snippet(s) (the smallest piece that shows the issue)
*   What you tried + what changed

## Essential Engineering Tools (Beginner Primer)

You do not need to master these on Day 1, but you should recognize what they are and why they matter:

*   **IDE (VS Code)**: where you edit code, run/debug, and manage projects.
*   **Git**: version control (save checkpoints, collaborate, roll back changes).
*   **SSH**: secure remote access to servers (common for deployment and remote GPUs).
*   **Linux commands**: basic terminal skills to run scripts, inspect files, and read logs.
*   **Docker**: packages an app + dependencies so it runs consistently on different machines.

## How to Search and Read Technical Docs

Practical habits that prevent getting stuck:

*   Prefer official docs for installation and quickstarts; use GitHub issues for specific error messages.
*   Search with concrete keywords:
    *   library name + error message (or a key phrase from the traceback)
    *   library name + "quickstart" / "examples" / "API reference"
    *   "python" + task + "minimal example"
*   Learn the structure of typical docs pages:
    *   Installation / Requirements
    *   Quickstart / Tutorial
    *   Examples
    *   API Reference
    *   FAQ / Troubleshooting
*   Using AI is encouraged, but include the source link and ask targeted questions (e.g., "Explain this traceback" or "What is the minimal change needed?").

## Debug / Test / Deploy (Basic Workflow)

You will practice this loop repeatedly in Foundational Course:

*   **Debug**: read the full error, isolate the failing line, simplify inputs, add prints/logs, and confirm the fix by re-running.
*   **Test**: define 3+ test cases (normal + edge + failure), and run them after every change (manual checklist is acceptable early).
*   **Deploy**: make the project runnable from a clean environment using README steps, configure secrets via `.env`, and verify a basic health run (script completes or API endpoint responds).

## Key Terms (Quick Glossary)

*   **CLI**: Command-line interface (a terminal where you run commands).
*   **Virtual environment (venv/conda)**: An isolated Python environment so dependencies do not conflict.
*   **Dependency management**: Installing and pinning packages so a project runs consistently.
*   **`.env`**: A file for environment variables (commonly used for secrets like API keys).
*   **`requirements.txt` / `pyproject.toml`**: files that declare project dependencies.
*   **README**: the first file people read; should explain setup, how to run, and expected outputs.
*   **pytest**: a Python testing framework used to run automated tests.
*   **Train/validation split**: splitting data into training vs evaluation portions to avoid fooling yourself.
*   **Overfitting**: when a model memorizes training data but performs poorly on new data.
*   **LLM**: Large language model.
*   **Tokenization**: converting text into tokens that a model can process.
*   **Context window**: the maximum number of tokens a model can consider at once.
*   **Transformer**: the neural network architecture behind most modern LLMs.
*   **Hosted API**: A cloud model endpoint you call over HTTP (usually needs an API key).
*   **Timeout / retry**: Reliability controls for network calls (stop waiting after a limit; try again on failure).
*   **Structured output / JSON schema**: A fixed output format that code can reliably parse.
*   **Local inference (Ollama)**: Running a model locally on your machine instead of via a hosted API.

## Duration & Weekly Hours

*   **8 weeks** (can be expanded to 10 weeks or extended to 12 weeks)
*   **5 class hours per week** (recommended: 3 hours lecture/discussion + 2 hours lab/workshop)

## Pillar Coverage

*   **AI Concepts (Basics)**: train/validation/overfitting, loss functions and metrics, Transformers/tokens/context window
*   **AI Engineering (Basics)**: Python data stack, traditional ML mini-experiments, production-minded LLM API usage, local inference (Ollama)
*   **Meta-Learning (Intro)**: read the "usage" section of official docs; create minimal reproductions and do basic debugging
*   **System Design (Intro)**: modularize scripts (config/data/model/report/logging) and use clear interfaces

## Learning Outcomes

After completing Foundational Course, you should be able to:

1. Explain key fundamentals of traditional ML and LLMs, and choose a reasonable baseline approach for a task
    - What this means: you can explain train/validation/overfitting and tokens/context in plain language.
    - What to demonstrate: given a task, you can justify a baseline (simple model or simple prompt + validation).
2. Complete a reproducible ML mini-experiment in Python (data split, training, evaluation, saving artifacts)
    - What this means: you can rerun the same command and get consistent artifacts (config + metrics + model file).
    - What to demonstrate: you can point to the exact run folder that produced the reported metric.
3. Reliably call at least one hosted LLM API with basic production practices (timeouts, retries, logging, rate limiting, simple caching)
    - What this means: your code fails fast on timeouts/429s and produces actionable logs instead of hanging.
    - What to demonstrate: a forced failure case (invalid key / timeout) with a clear error and request/run identifier.
4. Run local inference (Ollama) and compare model output quality and performance differences
    - What this means: you can run a local model end-to-end and measure latency distribution (not just one run).
    - What to demonstrate: a small benchmark comparison across 2 models or 2 quantizations.
5. Deliver a runnable Capstone project with a README, environment setup, and reproducible run steps
    - What this means: a teammate can follow your README on a fresh machine and reproduce outputs without "magic steps".
    - What to demonstrate: one-command run that produces `report.json` + `report.md` in a predictable location.

## Recommended Tech Stack (Foundational Course)

*   Python 3.10+ (recommended 3.11)
*   Core libraries: `numpy`, `pandas`, `scikit-learn`, `matplotlib`/`seaborn`
*   Engineering: `pytest`, `python-dotenv` (or equivalent), structured logging (any reasonable implementation)
*   LLM: hosted API (OpenAI/Anthropic/equivalent) + local inference via Ollama

## Assessment (Suggested)

*   Homework: 40%
*   Labs/Workshops: 20%
*   Capstone: 40%

## Exit Criteria

*   Independently complete a small Python project with configuration, logging, and error handling
*   Explain train/validation/overfitting and common metrics, and provide at least one experiment comparison
*   Reliably call at least one hosted LLM API and one local inference option

---

# 8-Week Teaching Plan

## Weekly Teaching Rhythm (Recommended)

*   **3 class hours lecture/discussion**: concepts + examples + common pitfalls
*   **2 class hours lab/workshop**: get the code running in class + reserve time for debugging

You can also use a 2+1+2 format:

*   Session 1 (2 hours): core concepts and examples
*   Session 2 (1 hour): short quiz/recap/code walkthrough
*   Session 3 (2 hours): lab/workshop

## Weekly Curriculum

### Week 1: Environment Setup & Data Processing Basics

*   **Lecture (3h)**: Python environment, dependency management, script structure, exceptions and logging intuition; Pandas read/write/clean
*   **Workshop (2h)**: read CSV -> clean missing values -> basic stats -> export report (Markdown/JSON)
*   **Deliverable**: a runnable `data_profile.py` + README
*   Resources: [week_01/README.md](week_01/README.md)

### Week 2: The ML Training Loop + Reproducible Baselines

*   **Lecture (3h)**: train/validation split, overfitting/generalization, meaning of losses and metrics; random seeds and experiment logging
*   **Workshop (2h)**: `scikit-learn` classification: split -> train -> metrics -> save model; compare 2 settings/models
*   **Deliverable**: `train.py` (parameterized) + `report.md` (metric explanation + one failed experiment) + minimal `experiments/`
*   Resources: [week_02/README.md](week_02/README.md)

### Week 3: LLM Fundamentals + Prompt Engineering

*   **Lecture (3h)**: tokenization, context window, Transformer intuition; hallucinations; prompts as API contracts
*   **Workshop (2h)**: structured JSON output + validation + retries/repair; compare prompt variants
*   **Deliverable**: `extract.py` (schema-driven) + at least 3 edge input tests
*   Resources: [week_03/README.md](week_03/README.md)

### Week 4: LLM API Engineering (Reliability & Cost)

*   **Lecture (3h)**: timeouts, retries, rate limiting, idempotency, caching; minimum observability set
*   **Workshop (2h)**: implement `llm_client.py` (timeouts/retries/simple cache/structured logs)
*   **Deliverable**: reusable LLM client module + unit tests
*   Resources: [week_04/README.md](week_04/README.md)

### Week 5: Local Inference (Ollama) and Model Comparison

*   **Lecture (3h)**: boundaries of local inference (speed/VRAM/capability/context); why local matters
*   **Workshop (2h)**: install and call Ollama; compare 2-3 models on the same task for quality/latency
*   **Deliverable**: `benchmark_local_llm.py` + written conclusions
*   Resources: [week_05/README.md](week_05/README.md)

### Week 6: Capstone Prototype (End-to-End Flow)

*   **Lecture (3h)**: sampling, long-text splitting, input compression; from scripts to pipelines
*   **Workshop (2h)**: implement CSV -> profiling -> LLM explanation -> report generation
*   **Deliverable**: Capstone prototype (main flow runs end-to-end)
*   Resources: [week_06/README.md](week_06/README.md)

### Week 7: Capstone Engineering & Quality

*   **Lecture (3h)**: CLI design, config management (env/config files), error codes and explainable failures
*   **Workshop (2h)**: add tests, handle edge cases, stabilize outputs (JSON + Markdown)
*   **Deliverable**: Capstone submission-ready version
*   Resources: [week_07/README.md](week_07/README.md)

### Week 8: Capstone Demo & Retrospective (Preparing for Level 2)

*   **Lecture (3h)**: retrospective: what breaks most often; how to prepare for RAG/agents
*   **Workshop (2h)**: project demo and code walkthrough; refactor once based on feedback
*   **Deliverable**: final Capstone delivery + retrospective notes
*   Resources: [week_08/README.md](week_08/README.md)

## 10-Week Expansion Guidance

If you expand back to 10 weeks, add depth without changing the core arc:

*   Split Week 2 into "training loop" and "comparative experiments"
*   Split Week 3 into "LLM fundamentals" and "structured prompting + validation"

## 12-Week Expansion Guidance

If you extend to 12 weeks, strengthen engineering fundamentals and evaluation awareness:

*   Add 1 week: **Software engineering basics** (structured logging, configuration, testing, Makefile/task runners)
*   Add 1 week: **LLM output evaluation** (error taxonomies, small human-labeled set, simple consistency checks)
*   Add 1 Capstone week: implement a **feedback loop** (user feedback -> prompt/pipeline iteration)

---

## Document Navigation

*   Pre-study reference: see [PRESTUDY.md](PRESTUDY.md)
*   Assignments: see [assignments.md](assignments.md)
*   Capstone: see [capstone.md](capstone.md)
