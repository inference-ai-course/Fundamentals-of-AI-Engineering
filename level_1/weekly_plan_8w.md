# Level 1 (Foundation) 8-Week Plan (5 class hours/week)

## Weekly Teaching Rhythm (Recommended)

*   **3 class hours lecture/discussion**: concepts + examples + common pitfalls
*   **2 class hours lab/workshop**: get the code running in class + reserve time for debugging

You can also use a 2+1+2 format:

*   Session 1 (2 hours): core concepts and examples
*   Session 2 (1 hour): short quiz/recap/code walkthrough
*   Session 3 (2 hours): lab/workshop

## Level 0 Navigation (Pre-study)

Level 1 assumes Level 0 is complete. Use these as the canonical fundamentals reference:

*   [Level 0 schedule](../level_0/Schedule.md)
*   Chapters:
    *   [Chapter 1: Tool Preparation](../level_0/Chapters/1/Chapter1.md)
    *   [Chapter 2: Python and Environment Management](../level_0/Chapters/2/Chapter2.md)
    *   [Chapter 3: AI Engineering Fundamentals](../level_0/Chapters/3/Chapter3.md)
    *   [Chapter 4: Hugging Face Platform and Local Inference](../level_0/Chapters/4/Chapter4.md)
    *   [Chapter 5: Resource Monitoring and Containerization](../level_0/Chapters/5/Chapter5.md)


---

## 8-Week Core Plan

Weekly concept notes (self-study + citations):

*   Week 1: [week_01/README.md](week_01/README.md) | [week_01/practice.ipynb](week_01/practice.ipynb)
*   Week 2: [week_02/README.md](week_02/README.md) | [week_02/practice.ipynb](week_02/practice.ipynb)
*   Week 3: [week_03/README.md](week_03/README.md) | [week_03/practice.ipynb](week_03/practice.ipynb)
*   Week 4: [week_04/README.md](week_04/README.md) | [week_04/practice.ipynb](week_04/practice.ipynb)
*   Week 5: [week_05/README.md](week_05/README.md) | [week_05/practice.ipynb](week_05/practice.ipynb)
*   Week 6: [week_06/README.md](week_06/README.md) | [week_06/practice.ipynb](week_06/practice.ipynb)
*   Week 7: [week_07/README.md](week_07/README.md) | [week_07/practice.ipynb](week_07/practice.ipynb)
*   Week 8: [week_08/README.md](week_08/README.md) | [week_08/practice.ipynb](week_08/practice.ipynb)

### Week 1: Environment Setup & Data Processing Basics

*   **Lecture (3h)**: Python environment, dependency management, script structure, exceptions and logging intuition; Pandas read/write/clean
*   **Workshop (2h)**: read CSV -> clean missing values -> basic stats -> export report (Markdown/JSON)
*   **Deliverable**: a runnable `data_profile.py` + README

### Week 2: The ML Training Loop + Reproducible Baselines (Merged)

*   **Lecture (3h)**: train/validation split, overfitting/generalization, meaning of losses and metrics; random seeds and experiment logging
*   **Workshop (2h)**: `scikit-learn` classification: split -> train -> metrics -> save model; compare 2 settings/models
*   **Deliverable**: `train.py` (parameterized) + `report.md` (metric explanation + one failed experiment) + minimal `experiments/`

### Week 3: LLM Fundamentals + Prompt Engineering (Merged)

*   **Lecture (3h)**: tokenization, context window, Transformer intuition; hallucinations; prompts as API contracts
*   **Workshop (2h)**: structured JSON output + validation + retries/repair; compare prompt variants
*   **Deliverable**: `extract.py` (schema-driven) + at least 3 edge input tests

### Week 4: LLM API Engineering (Reliability & Cost)

*   **Lecture (3h)**: timeouts, retries, rate limiting, idempotency, caching; minimum observability set
*   **Workshop (2h)**: implement `llm_client.py` (timeouts/retries/simple cache/structured logs)
*   **Deliverable**: reusable LLM client module + unit tests

### Week 5: Local Inference (Ollama) and Model Comparison

*   **Lecture (3h)**: boundaries of local inference (speed/VRAM/capability/context); why local matters
*   **Workshop (2h)**: install and call Ollama; compare 2–3 models on the same task for quality/latency
*   **Deliverable**: `benchmark_local_llm.py` + written conclusions

### Week 6: Capstone Prototype (End-to-End Flow)

*   **Lecture (3h)**: sampling, long-text splitting, input compression; from scripts to pipelines
*   **Workshop (2h)**: implement CSV -> profiling -> LLM explanation -> report generation
*   **Deliverable**: Capstone prototype (main flow runs end-to-end)

### Week 7: Capstone Engineering & Quality

*   **Lecture (3h)**: CLI design, config management (env/config files), error codes and explainable failures
*   **Workshop (2h)**: add tests, handle edge cases, stabilize outputs (JSON + Markdown)
*   **Deliverable**: Capstone submission-ready version

### Week 8: Capstone Demo & Retrospective (Preparing for Level 2)

*   **Lecture (3h)**: retrospective: what breaks most often; how to prepare for RAG/agents
*   **Workshop (2h)**: project demo and code walkthrough; refactor once based on feedback
*   **Deliverable**: final Capstone delivery + retrospective notes

---

## 10-Week Expansion Guidance

If you expand back to 10 weeks, add depth without changing the core arc:

*   Split Week 2 into “training loop” and “comparative experiments”
*   Split Week 3 into “LLM fundamentals” and “structured prompting + validation”

---

## 12-Week Expansion Guidance

If you extend to 12 weeks, strengthen engineering fundamentals and evaluation awareness:

*   Add 1 week: **Software engineering basics** (structured logging, configuration, testing, Makefile/task runners)
*   Add 1 week: **LLM output evaluation** (error taxonomies, small human-labeled set, simple consistency checks)
*   Add 1 Capstone week: implement a **feedback loop** (user feedback -> prompt/pipeline iteration)
