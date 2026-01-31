# Full-Stack AI Engineer Syllabus (Progressive Track)

This syllabus follows a **sequential progression** approach. It develops four core pillars (concepts, coding, meta-learning, system design) in stages. Instead of spreading effort evenly across every stage, each level focuses on the right skills at the right time based on the learning curve.

---

## Progression Overview

| Level | Focus Pillars | Key Goal |
| :--- | :--- | :--- |
| **Level 0** | **Development tools + Python basics + AI fundamentals** | Prepare the environment and foundational skills for AI engineering. |
| **Level 1** | **AI fundamentals + Python practice** | Build the foundation: understand principles, write Python, and reliably call APIs. |
| **Level 2** | **System design + AI application engineering** | Build systems: master RAG/agents and ship quickly with AI-assisted coding (Vibe Coding). |
| **Level 3** | **Fine-tuning + meta-learning** | Optimize deeply: master fine-tuning/evaluation and become capable of research-grade self-learning and problem solving. |

### Key Terms (Quick Glossary)

*   **RAG**: Retrieval-Augmented Generation (retrieve context, then generate an answer).
*   **Agent / agent workflow**: a multi-step process where an LLM uses tools and state to complete tasks.
*   **SFT**: Supervised Fine-Tuning (fine-tune on instruction-response pairs).
*   **RLHF**: Reinforcement Learning from Human Feedback (preference optimization methods).
*   **DPO**: Direct Preference Optimization (a simpler preference-optimization method).
*   **LoRA / QLoRA**: parameter-efficient fine-tuning (QLoRA uses quantization to reduce training VRAM).

### Delivery Format

*   Each level is designed as **8 weeks** (can be expanded to **10 weeks** or extended to **12 weeks**).
*   **5 class hours per week** (recommended split: 3 hours lecture/discussion + 2 hours lab/workshop).
*   Each level ends with one assessable Capstone/Project.

---

## Level 0: Canonical Fundamentals (Start Here for Beginners)

**Use Level 0 as the canonical source for fundamentals.** Level 1+ assumes Level 0 is complete.

*   **Overview**: [level_0/README.md](level_0/README.md)
*   **Self-Study Guide**: [level_0/self_study_guide.md](level_0/self_study_guide.md) — Beginner-friendly 8-week plan
*   **Schedule**: [level_0/Schedule.md](level_0/Schedule.md)
*   **Chapters**:
    *   [Chapter 1: Tool Preparation](level_0/Chapters/1/Chapter1.md)
    *   [Chapter 2: Python and Environment Management](level_0/Chapters/2/Chapter2.md)
    *   [Chapter 3: AI Engineering Fundamentals](level_0/Chapters/3/Chapter3.md)
    *   [Chapter 4: Hugging Face Platform and Local Inference](level_0/Chapters/4/Chapter4.md)
    *   [Chapter 5: Resource Monitoring and Containerization](level_0/Chapters/5/Chapter5.md)

---

## Level 1: The Foundation

**Core pillars**: `1. AI Concepts` & `2. AI Engineering (Basics)`  
**Focus**: Build intuition about data and models, and become comfortable with the Python data ecosystem.

**Target audience**: Complete beginners; or developers who want to systematically fill AI fundamentals.  
**Exit criteria**:
*   Independently complete a small Python project with config, logging, and error handling.
*   Explain train/validation/overfitting and common metrics, and run basic experiment comparisons.
*   Reliably call at least one hosted LLM API and one local inference setup.

### File Structure (Level 1)
*   [overview.md](level_1/overview.md)
*   [weekly_plan_8w.md](level_1/weekly_plan_8w.md)
*   [assignments.md](level_1/assignments.md)
*   [capstone.md](level_1/capstone.md)

### Module 1.1: Data & Machine Learning Foundations
*   **Goal**: Understand how machines learn.
*   **Content**:
    *   **Python AI stack**: Use NumPy (tensors intuition) and Pandas (data processing) effectively.
    *   **Traditional ML concepts**: Loss functions, gradient descent, overfitting/generalization, train/validation splits (*foundation for understanding LLM training later*).
    *   **Practice**: Implement a simple linear regression or finish a classification task with scikit-learn.
    *   **Meta skill (basics)**: Learn to use official docs effectively (docs reading).

*   **Theory / Tutorial**:
    *   Data representations: scalar/vector/matrix/tensor; common data types and missing values.
    *   Training loop: data splitting, feature intuition, training/validation, metric selection (Accuracy/F1/ROC-AUC).
    *   Minimal reproducible experiments: fix random seeds, record configs, compare baselines.
*   **Lab (hands-on)**:
    *   Train a binary classifier with `scikit-learn` and output a confusion matrix and classification report.
    *   Visualize distributions and correlations with `matplotlib`/`seaborn`.
*   **Homework**:
    *   Submit `train.py`: parameterized data path and hyperparameters; print metrics and save model artifacts.
    *   Submit `report.md`: explain metric choices and one failed experiment + iteration.

### Module 1.2: LLM Basics & API Engineering
*   **Goal**: From principles to reliable API usage.
*   **Content**:
    *   **LLM concepts**: Transformer intuition, tokenization, context window.
    *   **Prompt engineering**: Understand the fundamentals of zero-shot, CoT (Chain-of-Thought), and system prompts.
    *   **Practice**: Use OpenAI/Anthropic APIs to build scripts for summarization and extraction.
    *   **Practice**: Set up local inference with Ollama and compare model behavior.

*   **Theory / Tutorial**:
    *   Inference modes: chat completions and tool calling basics and limitations.
    *   Cost & reliability: retries, timeouts, rate limits, idempotency, caching, logging.
    *   Structured prompting: input/output schema, constrained outputs, error recovery.
*   **Lab (hands-on)**:
    *   Implement `llm_client.py`: timeouts, retries, logs, rate limiting, and a simple cache.
    *   Compare local models via Ollama: quality/latency (treat local "cost" as time/resources).
*   **Homework**:
    *   Submit a CLI tool: `summarize --input <file> --output <file> --format json`.
    *   Submit tests covering at least 3 error cases (empty input, too-long input, invalid model output format).

### Level 1 Capstone: Intelligent Data Analysis Script
*   **Task**: Build a Python script that reads CSV data and uses an LLM to generate a data analysis report.
*   **Evaluation**: Python fundamentals, API reliability, prompt design.

*   **Deliverables**:
    *   Reproducible setup: `requirements.txt` or `pyproject.toml` + `README`.
    *   `analyze.py`: supports input CSV path, output directory, optional column selection and sampling.
    *   Report output includes at minimum: overview, anomaly hints, potential correlations, actionable recommendations.
*   **Acceptance criteria**:
    *   Runs reliably on CSV files up to 10MB (failures must have clear error messages).
    *   LLM calls include retries/timeouts; logs can pinpoint failures.
    *   Report format is stable and machine-parseable (e.g., JSON + human-readable Markdown).

---

## Level 2: The Builder

**Core pillars**: `4. System Design` & `2. AI Engineering (Advanced)`  
**Focus**: Build real systems using existing models, emphasizing architecture and AI-assisted development.

**Target audience**: Junior/mid-level engineers with some development experience; or Level 1 graduates.  
**Exit criteria**:
*   Design and implement an end-to-end RAG system (including evaluation/monitoring considerations).
*   Implement at least one agent workflow (planning/tool use/state management/failure recovery).
*   Use AI-assisted coding to decompose requirements into modules, then review and refactor code.

### File Structure (Level 2)
*   [overview.md](level_2/overview.md)
*   [weekly_plan_10w.md](level_2/weekly_plan_10w.md)
*   [assignments.md](level_2/assignments.md)
*   [capstone.md](level_2/capstone.md)

### Module 2.1: Vibe Coding & AI-Assisted Development
*   **Goal**: Shift from "handwriting every line" to "designing logic and letting AI generate scaffolding".
*   **Content**:
    *   **Tooling**: Become proficient with Cursor/Windsurf.
    *   **Vibe Coding**: Specify requirements in natural language to generate code scaffolding.
    *   **Practice**: Build a simple CRUD web app with AI assistance within 1 hour.

*   **Theory / Tutorial**:
    *   From requirements to code: specify "interfaces/data models/error codes/edge cases/acceptance tests".
    *   Quality control for AI-assisted coding: minimal diffs, tests first, constraints before generation.
    *   Code review checklist: readability, testability, dependency isolation, configuration, security.
*   **Lab (Hands-on)**:
    *   Implement CRUD with FastAPI or Flask; add input validation and error handling.
    *   Add `pytest` tests and CI for critical logic (align to existing CI if present).
*   **Homework**:
    *   Submit an "AI collaboration log": constraints you gave, generated output, your fixes and rationale.

### Module 2.2: RAG System Design & Implementation
*   **Goal**: Address hallucinations and knowledge freshness.
*   **Content**:
    *   **System design**: RAG pipeline (ETL -> Embedding -> Vector DB -> Retrieval -> Generation).
    *   **Practice**: Use LangChain/LlamaIndex with ChromaDB/Milvus.
    *   **Advanced**: Hybrid search and re-ranking (rerank) implementation.

*   **Theory / Tutorial**:
    *   Chunking strategies and tradeoffs: size, overlap, structured docs (headings/tables/code blocks).
    *   Retrieval quality intuition: recall/precision; when you need rerank.
    *   Anti-hallucination patterns: citations, refusal, insufficient-context detection.
*   **Lab (Hands-on)**:
    *   Build a "course handout Q&A" RAG: ingestion, embeddings, retrieval, answering with citations.
    *   Add rerank (optional) and compare quality/latency.
*   **Homework**:
    *   Implement an offline evaluation script: given QA pairs, output hit rate/citation coverage/failure cases.

### Module 2.3: Agent Workflows & Multi-Agent Systems
*   **Goal**: Give AI the ability to act.
*   **Content**:
    *   **Design patterns**: ReAct, Reflection, Planning.
    *   **Framework usage**: State management with LangGraph or CrewAI.
    *   **Practice**: Build an "automated research report agent" with search, web fetching, and writing tools.

*   **Theory / Tutorial**:
    *   Tool contracts: input/output schema, retries, timeouts, and fallback.
    *   State machine thinking: nodes, edges, memory, and observability.
    *   Security & compliance: tool allowlists, sensitive data handling, prompt-injection basics.
*   **Lab (Hands-on)**:
    *   Implement a "research task" workflow: question -> plan -> search -> summarize -> conclude.
    *   Add failure recovery: switch paths or output a clear failure report when a tool is unavailable.
*   **Homework**:
    *   Produce a workflow design doc: node responsibilities, I/O, exception paths, testing strategy.

### Level 2 Capstone: Vertical Domain Assistant System
*   **Task**: Build an end-to-end web application (e.g., a legal assistant).
*   **Evaluation**: Complete RAG pipeline, agent tool use, modular code structure, front-end/back-end separation.

*   **Suggested scope**:
    *   A clear domain (law/medical/education/finance, etc.) with a controlled knowledge base.
    *   Must include: chat UI, RAG Q&A, citations, feedback buttons (good/bad), admin data ingestion.
*   **Deliverables**:
    *   Architecture diagram and API documentation (REST/JSON).
    *   Runnable demo (local or containerized) with one-command startup instructions.
    *   A minimal evaluation set and evaluation script (reproduces claimed outcomes).
*   **Acceptance criteria**:
    *   For in-KB questions, answers must include citations traceable to source snippets.
    *   For out-of-KB questions, trigger refusal/clarification instead of making things up.
    *   Clear structure: ingestion, retrieval, generation, API, and front-end layers separated.

---

## Level 3: The Expert

**Core pillars**: `1. AI Concepts (Advanced)` & `3. Meta-Learning`  
**Focus**: Open the black box with fine-tuning, evaluation, and low-level optimization, and build the ability to solve unknown problems.

**Target audience**: Senior developers; or Level 2 graduates who want to go deeper into models, evaluation, and optimization.  
**Exit criteria**:
*   Independently complete a reproducible fine-tuning experiment and prove whether it improved via evaluation.
*   Handle common deployment performance/stability issues (latency, throughput, VRAM, concurrency).
*   Use meta-learning methods to reproduce the core demo of an unfamiliar paper/open-source project.

### File Structure (Level 3)
*   [overview.md](level_3/overview.md)
*   [weekly_plan_10w.md](level_3/weekly_plan_10w.md)
*   [assignments.md](level_3/assignments.md)
*   [capstone.md](level_3/capstone.md)

### Module 3.1: Fine-Tuning in Practice
*   **Goal**: Customize models beyond hosted API limitations.
*   **Content**:
    *   **Theory**: Understand SFT (Supervised Fine-Tuning) and RLHF at a high level.
    *   **Stack**: LoRA/QLoRA fundamentals and VRAM optimization.
    *   **Practice**: Prepare a custom dataset (e.g., medical QA) and fine-tune Llama 3 with Unsloth/Llama-Factory.

*   **Theory / Tutorial**:
    *   Data engineering: instruction formats, deduplication, leakage, split strategies, quality gates.
    *   Choosing fine-tuning strategies: full fine-tuning vs LoRA; when preference optimization (e.g., DPO) is needed.
    *   Reproducible training: config-driven runs, seeds, logs, checkpoints, rollback.
*   **Lab (Hands-on)**:
    *   Train a LoRA adapter and compare inference with/without merging.
    *   Build a "data audit script": length distribution, duplication, potential sensitive content.
*   **Homework**:
    *   Submit an experiment log: hyperparameters, data version, training curves, failed experiment postmortem.

### Module 3.2: Evaluation, Quantization, and Inference Optimization
*   **Goal**: Make models faster, better, and cheaper.
*   **Content**:
    *   **Evaluation**: Build an automated LLM-as-a-Judge pipeline (Ragas/DeepEval).
    *   **Optimization**: Quantization (GGUF/AWQ/GPTQ) and faster inference deployment with vLLM.
    *   **Practice**: Compare objective metrics before/after fine-tuning, then quantize and deploy on lower-VRAM hardware.

*   **Theory / Tutorial**:
    *   Evaluation design: offline benchmarks, online A/B, human spot checks; avoid prompt "gaming".
    *   Performance profiling: throughput/latency/VRAM/concurrency; bottleneck analysis (tokenization, KV cache, IO).
    *   Deployment strategies: batching, streaming, rate limits, circuit breakers, and monitoring (p95/p99).
*   **Lab (Hands-on)**:
    *   Run concurrency load tests with `vLLM` (or equivalent), record latency distributions, and analyze bottlenecks.
    *   Run at least one quantization comparison: quality regression vs VRAM/speed gains.
*   **Homework**:
    *   Submit an evaluation + load testing report: methods, metrics, conclusions, next-step recommendations.

### Module 3.3: Advanced Meta-Learning (Exploring the Unknown)
*   **Goal**: Go beyond tutorials and handle frontier technologies independently.
*   **Content**:
    *   **Source reading**: Read `transformers` or vLLM source code to understand key internals.
    *   **Paper to code**: Pick a recent arXiv paper and reproduce its core demo with AI-assisted reading.
    *   **Debugging**: Solve a complex CUDA or out-of-memory (OOM) issue via logs and documentation-driven reasoning, not just copy-pasting from search.

*   **Method / Playbook**:
    *   How to read source: entrypoint -> core data structures -> key branches -> performance hotspots.
    *   Debugging method: minimal reproduction, binary search, logs/assertions, controlled experiments.
    *   Documentation search: reverse-engineer keywords from errors; prioritize official docs > RFC/specs > issues > blogs.
*   **Homework**:
    *   Submit an "Issue Dossier": symptoms, reproduction steps, investigation process, root cause, fix, and regression tests.

### Level 3 Capstone: Enterprise Private Model Solution
*   **Task**: Complete the full lifecycle from data cleaning -> fine-tuning -> evaluation -> quantization -> high-concurrency deployment.
*   **Evaluation**: Evidence of model quality improvement, inference performance optimization report, and documented problem-solving process for unfamiliar issues.

*   **Deliverables**:
    *   A reproducible pipeline: data versioning -> training -> evaluation -> export -> deployment (scripts/Makefile/CI).
    *   A "quality evidence pack": baseline comparison, eval results, failure case analysis, bias/risk notes.
    *   A "performance & cost report": throughput/latency/resource usage/concurrency strategy and limits.
*   **Acceptance criteria**:
    *   Evaluation is reproducible: same code/data versions yield results within explainable variance.
    *   Deployment is usable: health checks, basic monitoring, error handling, and fallback strategies.
    *   Meta-learning is demonstrated: at least one systematic "unknown issue" resolution record with evidence.

---

## Beginner Scaffolding Resources

### Level 0 Resources
*   Onboarding for complete beginners who need development tools and Python basics
*   Self-study guide with hands-on exercises and weekly deliverables

### Level 1 Resources
*   Onboarding checklist: [Level 1 overview -> Onboarding Checklist](level_1/overview.md#onboarding-checklist-week-0)
*   Terms glossary: [Level 1 overview -> Key Terms](level_1/overview.md#key-terms-quick-glossary)
*   Submission template: [Level 1 assignments -> Recommended Submission Template](level_1/assignments.md#recommended-submission-template)

### Level 2 Resources
*   Bridge checklist: [Level 2 overview -> Beginner Bridge](level_2/overview.md#beginner-bridge-if-level-2-feels-too-steep)
*   Terms glossary: [Level 2 overview -> Key Terms](level_2/overview.md#key-terms-quick-glossary)
*   Definition of done: [Level 2 assignments -> Definition of Done](level_2/assignments.md#definition-of-done-level-2)

### Level 3 Resources
*   Terms glossary: [Level 3 overview -> Key Terms](level_3/overview.md#key-terms-quick-glossary)

---

## Placement (Tracks)

| Audience | Recommended Start | Entry Criteria (Suggested) | Target Path |
| :--- | :--- | :--- | :--- |
| **Complete beginners (non-technical)** | Level 0 | None — start from tool setup and Python basics | Level 0 -> Level 1 -> Level 2 -> Level 3 |
| **Some programming experience** | Level 1 | Basic CLI usage; can write simple Python scripts (vars/loops/functions); can read the "usage" section of English docs | Level 1 -> Level 2 -> Level 3 |
| **Junior developers (technical background)** | Level 1 or Level 2 | Familiar with at least one of Git/HTTP/SQL; can finish a small web/script project | Level 1 (fast-track) -> Level 2 -> Level 3 |
| **Senior developers (experienced)** | Level 2 or Level 3 | Comfortable with system design and engineering; can debug independently; has production delivery experience | Level 2 (fill in LLM/RAG/agents) -> Level 3 (deep optimization) |

---

## Graduation Competency Matrix

After completing all levels, learners should demonstrate the following four competencies:

| Pillar | Graduation Requirements (Observable Behaviors) |
| :--- | :--- |
| **1. AI Concepts** | Explain key ML/LLM training & inference concepts (loss/generalization/tokens/context/alignment) and choose appropriate fine-tuning/evaluation strategies for a task |
| **2. AI Engineering (Coding)** | Use Python and mainstream OSS stacks to implement inference, RAG, agents, fine-tuning, evaluation, and deployment (with reproducible environments and scripted pipelines) |
| **3. Meta-Learning** | Read source code/docs to find key APIs; debug with logs and minimal reproducible cases; build a learning plan and ship validation demos for new topics |
| **4. System Design + AI-Assisted Delivery** | Decompose requirements into architecture/modules; use agent workflows and AI-assisted coding effectively; deliver end-to-end deployable AI projects |
