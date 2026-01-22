# Level 3 Assignments & Assessment

## Submission Requirements (Strongly Recommended)

Each assignment submission must include:

*   **Experiment configuration** (config files and/or CLI arguments)
*   **Data version information** (source, splits, hash/version, change notes)
*   **Results and evidence** (metrics, failure cases, curves)
*   **Reproduction instructions** (how to reproduce comparable results with the same steps)

## Assignment List (Suggested: 6 assignments + 1 Capstone)

### C1: Experiment Template + Baseline Evaluation

*   **Goal**: build a reproducible experimentation skeleton
*   **Requirements**: provide a unified run entry (scripts/Makefile/task runner are all fine) and run a baseline evaluation
*   **Acceptance**: a third party can reproduce comparable results by following the README

### C2: Data Audit + Quality Gates

*   **Goal**: avoid “garbage in, garbage out”
*   **Requirements**: a data audit script: length distributions, duplication rate, outliers, sensitive-data strategy notes
*   **Acceptance**: output an audit report + at least 5 blocked/flagged examples

### C3: LoRA/QLoRA Fine-Tuning Experiment

*   **Goal**: complete one reproducible fine-tuning run
*   **Requirements**: training + export adapters + inference validation; record hyperparameters and training curves
*   **Acceptance**: provide base vs tuned comparisons (at least 20 examples)

### C4: Evaluation Script + Failure-Case-Driven Iteration

*   **Goal**: improve with evidence
*   **Requirements**: comparative evaluation (base vs tuned); output metrics + failure cases; iterate once based on failure cases
*   **Acceptance**: must show before/after evidence (improved metrics and/or fewer failure cases)

### C5: Quantization Comparison Report

*   **Goal**: master the quality–performance–cost tradeoff
*   **Requirements**: choose one quantization path and record quality changes and performance gains
*   **Acceptance**: report includes “best-fit scenarios” and “risks/limitations”

### C6: Inference Service Load Test + Bottleneck Analysis

*   **Goal**: make the model usable in production
*   **Requirements**: deploy an inference service; load test to produce throughput/latency distributions; propose bottlenecks and improvements
*   **Acceptance**: must include p95/p99 latency and at least one concrete optimization action (even a parameter tuning is fine)

### C7 (Meta-Learning): Issue Dossier

*   **Goal**: prove you can solve unfamiliar complex problems
*   **Requirements**: pick one real issue (OOM/CUDA/performance/dependency conflicts/framework bugs, etc.) and complete: reproduce -> locate -> fix/workaround -> regression
*   **Acceptance**: document includes minimal reproduction and regression validation steps

---

## Capstone

See [capstone.md](capstone.md) for Capstone requirements.
