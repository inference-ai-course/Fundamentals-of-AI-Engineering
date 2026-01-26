# Level 1 — Week 2: The ML Training Loop + Reproducible Baselines

## What you should be able to do by the end of this week

- Explain why we split data into train/validation.
- Train a baseline model, evaluate it, and save artifacts.
- Compare two runs and write a short failure retrospective.

Tutorials:
 
- [tutorial.md](tutorial.md)
- [01_training_loop.md](01_training_loop.md)
- [02_reproducibility_package.md](02_reproducibility_package.md)
- [03_compare_runs_report.md](03_compare_runs_report.md)

Practice notebook: [practice.ipynb](practice.ipynb)

## Key Concepts (with explanations + citations)

### 1) The ML training loop (split -> train -> evaluate -> save)

**Mental model**:

- Training is an optimization process: the model adjusts parameters to reduce a loss.
- Evaluation is how you check if the model generalizes beyond the training set.
- Saving artifacts (model + config + metrics) is what makes experiments reproducible.

Citations:

- scikit-learn: getting started (training/eval workflow): https://scikit-learn.org/stable/getting_started.html

### 2) Train/validation split and overfitting

**Why this is non-trivial**:

- A model can score very well on training data by memorizing patterns/noise.
- What you care about is performance on **unseen** data.

**Rule of thumb**:

- If training score keeps improving but validation score stalls or worsens, you may be overfitting.

If the math feels heavy, focus on the core idea of **generalization**.

Citations:

- scikit-learn: cross-validation (concepts): https://scikit-learn.org/stable/modules/cross_validation.html
- Google ML Crash Course — generalization: https://developers.google.com/machine-learning/crash-course/generalization/video-lecture

### 3) Metrics: Accuracy vs F1

**Mental model**:

- Accuracy answers: “How often am I correct overall?”
- F1 answers: “How good am I at finding positives without too many false positives/negatives?”

**When accuracy misleads**:

- If one class dominates (class imbalance), a dumb model can get high accuracy.

Citations:

- scikit-learn model evaluation: https://scikit-learn.org/stable/modules/model_evaluation.html
- F1 score explanation: https://en.wikipedia.org/wiki/F1_score

### 4) Reproducibility basics (seeds, parameters, artifacts)

**Mental model**:

- Two sources of “uncontrolled variance”:
  - random initialization/splitting
  - changing code/config without recording it

**Minimum reproducibility package**:

- fixed `random_state` / seed
- parameterized script flags (data path, model type, seed)
- saved artifacts:
  - trained model
  - metrics
  - the config used

Citations:

- scikit-learn pitfalls: controlling randomness: https://scikit-learn.org/stable/common_pitfalls.html#controlling-randomness
- scikit-learn model persistence: https://scikit-learn.org/stable/model_persistence.html

## Common pitfalls

- Evaluating on training data.
- Changing multiple variables at once (you can’t tell what caused improvement).
- Not saving the exact config that produced the metrics.

## Workshop / Implementation Plan

- Implement `train.py`:
  - load data
  - split train/validation
  - train a baseline classifier
  - print metrics
  - save artifacts
- Run 2 experiments:
  - change one hyperparameter OR switch models
- Write `report.md`:
  - what you changed
  - what happened
  - one failed run + your next experiment idea

## Figures (Comprehensive Overviews — Leave Blank)

### Figure A: The ML training loop (split -> train -> evaluate -> save)


### Figure B: Overfitting intuition (training vs validation curves)


## Self-check questions

- Can you explain overfitting without using equations?
- If someone runs your command twice, will results be identical or explainably close?
- Can you point to the saved artifact that proves your reported metric?
