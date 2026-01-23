# Level 3 (Deep Optimization & Expert Track) 8-Week Plan (5 class hours/week)

## Weekly Teaching Rhythm (Recommended)

*   **2 class hours**: principles and design tradeoffs (why we do it, and where the boundaries are)
*   **1 class hour**: case study (open-source implementations, production incident retrospectives, paper ideas)
*   **2 class hours**: experiment/deployment workshop (run it, record it, compare it, find bottlenecks)


---

## 8-Week Core Plan

### Week 1: Reproducibility, Experiment Template, and Baselines

*   **Lecture (3h)**: experiment logging standards, data versions and leakage, training logs and rollback; minimal controlled experiment design
*   **Workshop (2h)**: build an experiment template: configs + log directories + result summarization; run a baseline evaluation
*   **Deliverable**: an `experiments/` template (can run one baseline inference evaluation)

### Week 2: Data Audit + SFT Setup (SFT/LoRA/QLoRA) (Merged)

*   **Lecture (3h)**: SFT and alignment intuition; LoRA/QLoRA efficiency and boundaries; data formats and leakage risks
*   **Workshop (2h)**: prepare instruction data format (instruction/input/output); implement a data audit script; build the training config
*   **Deliverable**: data audit report + training config ready to run

### Week 3: SFT Run + Initial Validation (Merged)

*   **Lecture (3h)**: hyperparameters, overfitting signals, checkpoint strategy; common training failures
*   **Workshop (2h)**: run one LoRA/QLoRA fine-tune; export adapters; validate via inference samples
*   **Deliverable**: a complete experiment record (configs, curves, samples, failure points)

### Week 4: Evaluation + One Iteration (Merged)

*   **Lecture (3h)**: evaluation design (benchmark/controls/blind tests); risks and calibration for LLM-as-a-Judge; failure-case iteration loop
*   **Workshop (2h)**: build `eval_compare.py`; compare base vs tuned; iterate once based on failure cases (data/template/rerun)
*   **Deliverable**: `eval_compare.py` + failure case analysis + before/after notes

### Week 5: Quantization + Regression

*   **Lecture (3h)**: differences between GGUF/AWQ/GPTQ; quantization error and task sensitivity
*   **Workshop (2h)**: run one quantization comparison; record quality regression + VRAM/speed gains
*   **Deliverable**: quantization comparison report (gains and tradeoffs)

### Week 6: Inference Service + Load Testing

*   **Lecture (3h)**: throughput/latency/p95/p99; batching, KV cache, streaming output; rate limiting and circuit breakers
*   **Workshop (2h)**: deploy an inference service (vLLM or equivalent) + write a load test script; produce latency distributions
*   **Deliverable**: load test results + initial bottleneck analysis

### Week 7: Production Readiness + Meta-Learning Dossier (Merged)

*   **Lecture (3h)**: minimum observability set (logs/metrics/tracing); incident replay; fallback strategies; debugging playbooks (OOM/perf)
*   **Workshop (2h)**: add health checks/metrics/retries/fallbacks; complete one issue dossier from reproduction to regression
*   **Deliverable**: “minimum viable production” notes + Issue Dossier

### Week 8: Capstone Defense (Enterprise End-to-End Solution)

*   **Lecture (3h)**: presenting “quality evidence + performance evidence + risk notes”; writing a technical proposal
*   **Workshop (2h)**: final defense and walkthrough: reproduce pipeline, rerun evaluation, reproduce load testing
*   **Deliverable**: final Capstone delivery + retrospective and next-step roadmap

---

## 10-Week Expansion Guidance

If you expand back to 10 weeks:

*   Split Week 2 into “data audit” and “SFT setup + training config”
*   Split Week 4 into “evaluation build” and “iteration / preference optimization (optional)”

---

## 12-Week Expansion Guidance

*   Add 1 week: **Data quality and alignment risks** (bias, sensitive content, red-teaming, compliance)
*   Add 1 week: **Deep performance profiling** (profiling, GPU utilization, batching strategies, KV cache tuning)
*   Add 1 Capstone week: **replay-based evaluation** and **failure-case-driven data iteration**
