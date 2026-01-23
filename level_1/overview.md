# Level 1 (Foundation) Overview

## Positioning

**Level 1** is designed for learners who need to build GenAI/LLM engineering fundamentals from 0 to 1. The emphasis is on **concept intuition + Python hands-on practice + reproducible small project delivery**.

## Target Learners

*   Complete beginners (non-technical background) who want to transition into AI/data/application development
*   Developers with a technical background but without a systematic AI foundation (want to fill in ML/LLM fundamentals and engineering habits)

## Prerequisites

*   Can do basic CLI operations (install dependencies, run scripts, read logs)
*   Has basic programming concepts (variables, conditionals, loops, functions). If not, complete a 1-week Python crash course before starting.

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

## Key Terms (Quick Glossary)

*   **CLI**: Command-line interface (a terminal where you run commands).
*   **Virtual environment (venv/conda)**: An isolated Python environment so dependencies do not conflict.
*   **Dependency management**: Installing and pinning packages so a project runs consistently.
*   **`.env`**: A file for environment variables (commonly used for secrets like API keys).
*   **`requirements.txt` / `pyproject.toml`**: files that declare project dependencies.
*   **README**: the first file people read; should explain setup, how to run, and expected outputs.
*   **pytest**: a Python testing framework used to run automated tests.
*   **LLM**: Large language model.
*   **Hosted API**: A cloud model endpoint you call over HTTP (usually needs an API key).
*   **Timeout / retry**: Reliability controls for network calls (stop waiting after a limit; try again on failure).
*   **Structured output / JSON schema**: A fixed output format that code can reliably parse.
*   **Local inference (Ollama)**: Running a model locally on your machine instead of via a hosted API.

## Duration & Weekly Hours

*   **10 weeks** (can be compressed to 8 weeks or extended to 12 weeks)
*   **5 class hours per week** (recommended: 3 hours lecture/discussion + 2 hours lab/workshop)

## Pillar Coverage

*   **AI Concepts (Basics)**: train/validation/overfitting, loss functions and metrics, Transformers/tokens/context window
*   **AI Engineering (Basics)**: Python data stack, traditional ML mini-experiments, production-minded LLM API usage, local inference (Ollama)
*   **Meta-Learning (Intro)**: read the “usage” section of official docs; create minimal reproductions and do basic debugging
*   **System Design (Intro)**: modularize scripts (config/data/model/report/logging) and use clear interfaces

## Learning Outcomes

After completing Level 1, you should be able to:

1. Explain key fundamentals of traditional ML and LLMs, and choose a reasonable baseline approach for a task
2. Complete a reproducible ML mini-experiment in Python (data split, training, evaluation, saving artifacts)
3. Reliably call at least one hosted LLM API with basic production practices (timeouts, retries, logging, rate limiting, simple caching)
4. Run local inference (Ollama) and compare model output quality and performance differences
5. Deliver a runnable Capstone project with a README, environment setup, and reproducible run steps

## Recommended Tech Stack (Level 1)

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

## Document Navigation

*   Weekly plan: see [weekly_plan_10w.md](weekly_plan_10w.md)
*   Assignments: see [assignments.md](assignments.md)
*   Capstone: see [capstone.md](capstone.md)
