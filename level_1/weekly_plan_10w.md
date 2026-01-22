# Level 1 (Foundation) 10-Week Plan (5 class hours/week)

## Weekly Teaching Rhythm (Recommended)

*   **3 class hours lecture/discussion**: concepts + examples + common pitfalls
*   **2 class hours lab/workshop**: get the code running in class + reserve time for debugging

You can also use a 2+1+2 format:

*   Session 1 (2 hours): core concepts and examples
*   Session 2 (1 hour): short quiz/recap/code walkthrough
*   Session 3 (2 hours): lab/workshop

---

## 10-Week Baseline Plan

### Week 1: Environment Setup & Data Processing Basics

*   **Lecture (3h)**: Python environment, dependency management, script structure, exceptions and logging intuition; Pandas read/write/clean
*   **Workshop (2h)**: read CSV -> clean missing values -> basic stats -> export report (Markdown/JSON)
*   **Deliverable**: a runnable `data_profile.py` + README

### Week 2: The ML Training Loop (0 to 1)

*   **Lecture (3h)**: train/validation split, overfitting/generalization, meaning of losses and metrics
*   **Workshop (2h)**: `scikit-learn` binary classification: split -> train -> metrics -> save model
*   **Deliverable**: `train.py` (parameterized) + `report.md` (metric explanation + one failed experiment)

### Week 3: Features, Baselines, and Reproducible Experiments

*   **Lecture (3h)**: feature intuition, scaling/missing handling, cross-validation; random seeds and experiment logging
*   **Workshop (2h)**: compare 2 models or 2 hyperparameter sets; output a comparison table and failure cases
*   **Deliverable**: an `experiments/` folder (config-driven runs)

### Week 4: LLM Fundamentals (Intuition)

*   **Lecture (3h)**: tokenization, context window, Transformer intuition; what inference is and why hallucinations happen
*   **Workshop (2h)**: compare prompt structures for the same task (zero-shot/structured output/examples)
*   **Deliverable**: `prompt_playground.py` (input file -> structured output)

### Week 5: Prompt Engineering (Controllable Outputs)

*   **Lecture (3h)**: system prompts, constrained outputs, error recovery; from “writing prompts” to “writing API contracts”
*   **Workshop (2h)**: define an output schema (JSON) for an extraction task and implement validation + retries
*   **Deliverable**: `extract.py` + schema validation and recovery

### Week 6: LLM API Engineering (Reliability & Cost)

*   **Lecture (3h)**: timeouts, retries, rate limiting, idempotency, caching; minimum observability set
*   **Workshop (2h)**: implement `llm_client.py` (timeouts/retries/simple cache/structured logs)
*   **Deliverable**: reusable LLM client module + unit tests

### Week 7: Local Inference (Ollama) and Model Comparison

*   **Lecture (3h)**: boundaries of local inference (speed/VRAM/capability/context); why local matters
*   **Workshop (2h)**: install and call Ollama; compare 2–3 models on the same task for quality/latency
*   **Deliverable**: `benchmark_local_llm.py` + written conclusions

### Week 8: Integrate LLMs into the Data Analysis Pipeline

*   **Lecture (3h)**: sampling, long-text splitting, input compression; from “scripts” to reusable pipelines
*   **Workshop (2h)**: implement CSV -> profiling -> LLM explanation -> report generation
*   **Deliverable**: a Capstone prototype (main flow runs end-to-end)

### Week 9: Capstone Engineering & Quality

*   **Lecture (3h)**: CLI design, config management (env/config files), error codes and explainable failures
*   **Workshop (2h)**: add tests, handle edge cases, stabilize outputs (JSON + Markdown)
*   **Deliverable**: Capstone submission-ready version

### Week 10: Capstone Demo & Retrospective (Preparing for Level 2)

*   **Lecture (3h)**: retrospective: what breaks most often; how to prepare for RAG/agents
*   **Workshop (2h)**: project demo and code walkthrough; refactor once based on feedback
*   **Deliverable**: final Capstone delivery + retrospective notes

---

## 8-Week Compression Guidance

If you need to compress to 8 weeks, keep the three main threads unchanged: **training loop + LLM engineering + Capstone**.

*   **Merge Week 2 & Week 3**: de-emphasize cross-validation details; keep reproducibility and comparisons
*   **Merge Week 4 & Week 5**: teach LLM intuition + controllable prompting in one week
*   Capstone: start a 2-week sprint from Week 7 (Week 7–8)

---

## 12-Week Expansion Guidance

If you extend to 12 weeks, strengthen engineering fundamentals and evaluation awareness:

*   Add 1 week: **Software engineering basics** (structured logging, configuration, testing, Makefile/task runners)
*   Add 1 week: **LLM output evaluation** (error taxonomies, small human-labeled set, simple consistency checks)
*   Add 1 Capstone week: implement a **feedback loop** (user feedback -> prompt/pipeline iteration)
