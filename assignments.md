# Foundamental Course Assignments & Assessment

## Submission Guidelines (Recommended)

Each assignment submission should include:

*   How to run (README with environment setup and commands)
*   Key output examples (screenshots or sample output files)
*   Failure case notes (at least one pitfall you encountered and how you fixed it)

If you need help, follow the required procedure in [Foundamental Course overview](overview.md#how-to-ask-for-help-required) and include:

*   The exact command you ran + full output
*   Your OS/Python version
*   A minimal code snippet/input that reproduces the problem
*   What you tried already

To make grading and debugging easier for beginners, use a consistent structure:

*   `README.md`
*   `requirements.txt` or `pyproject.toml`
*   `src/` (or a small number of top-level scripts)
*   `tests/` (even if minimal)
*   `output/` (sample outputs that match your README commands)

If you are not comfortable with Git yet, submitting a zipped folder is acceptable as long as it contains the items above.

Definition of done (quick checklist):

*   A clean run works on a new machine after following your README
*   Inputs/outputs are explicit (paths, formats, schemas)
*   Errors are readable (not just stack traces without context)
*   At least one failure case is documented with the fix

## Assignment List (Suggested: 6 assignments + 1 Capstone)

### A1: Data Profiling Script

*   **Goal**: Get comfortable with Pandas/data cleaning and build the habit of reproducible outputs
*   **Requirements**:
    *   Input: CSV path
    *   Output: missing-value stats, numeric column distributions, anomaly hints (your rule), saved to `output/`
*   **Acceptance**: Clear error messages for invalid inputs (empty file/missing columns)

### A2: Minimal Traditional ML Training Loop

*   **Goal**: Master train/validation/evaluate/save
*   **Requirements**: `train.py` is parameterized (data path, model type, random seed)
*   **Acceptance**: Print metrics (at least one of Accuracy/F1) + save model artifacts

### A3: Comparative Experiments + Failure Retrospective

*   **Goal**: Build baseline comparison thinking
*   **Requirements**:
    *   Compare two hyperparameter sets or two models
    *   Write `report.md`: one failed experiment and how you would iterate
*   **Acceptance**: Reproducible runs (re-running the same command yields explainable variance)

### A4: Structured Prompt Outputs (JSON Schema)

*   **Goal**: Move from “prompts” to “API contracts”
*   **Requirements**: Implement an information extraction task with JSON output; retry/repair invalid outputs
*   **Acceptance**: Cover at least 3 edge inputs (short text/long text/noisy text)

### A5: Production-Minded LLM Client

*   **Goal**: Reliably call models
*   **Requirements**: Implement `llm_client.py` (timeouts, retries, logging, simple caching)
*   **Acceptance**: Includes unit tests (preferred) or a clear manual test checklist; can simulate failures and validate retry behavior

### A6: Local Inference Comparison and Conclusions

*   **Goal**: Understand the value and limitations of local inference
*   **Requirements**: Use Ollama to compare 2–3 models on the same task (quality/latency); submit a comparison report
*   **Acceptance**: Conclusions must include “best-fit scenarios” and “risks/limitations”

---

## Quizzes & In-Class Activities (Optional)

*   Bi-weekly 10-minute quizzes: concept checks (train/validation, overfitting, tokens, context window)
*   Code walkthroughs: each learner explains one key module from an assignment (I/O and error handling)

---

## Capstone

See [capstone.md](capstone.md) for Capstone requirements.
