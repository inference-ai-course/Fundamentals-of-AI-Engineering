# Week 5: The ML Training Loop + Lightweight Baselines

## Pre-study (Self-learn)

Self-learn is optional. If you want a refresher:

- [Pre-study index (Foundations Course → Self-learn)](../PRESTUDY.md)
- [Self-learn — Chapter 2: Python and Environment Management](../self_learn/Chapters/2/Chapter2.md)

## What you should be able to do by the end of this week

- Explain why we split data into train/validation.
- Train a baseline model, evaluate it, and save artifacts.
- Compare two lightweight baseline runs and write a short reflection.

### The ML training loop

```mermaid
flowchart TD
  A[Load data] --> B[Split train/val]
  B --> C[Train model on train]
  C --> D[Predict on val]
  D --> E[Compute metrics]
  E --> F[Save artifacts]
  F --> G[Compare runs]

  F --> F1[config.json]
  F --> F2[metrics.json]
  F --> F3[model.joblib]
  F --> F4[val_report.txt]
```

Tutorials:
 
- [tutorial.md](tutorial.md)
- [01_training_loop.md](01_training_loop.md)
- [02_reproducibility_package.md](02_reproducibility_package.md)
- [03_compare_runs_report.md](03_compare_runs_report.md)

Exercises are included at the end of each notebook.

## Key Concepts (Self-learn refresher)

Self-learn is optional. If you want a refresher for this week:

- Reproducible environments, dependencies, and basic Python project habits:
  - ../self_learn/Chapters/2/Chapter2.md
- Evaluation mindset and metrics (accuracy/precision/recall/F1):
  - ../self_learn/Chapters/4/02_core_concepts.md

### Overfitting intuition (training vs validation curves)

```mermaid
flowchart TD
  A[Training begins] --> B[Both train & val metrics improve]
  B --> C[Val metric peaks — best generalization]
  C --> D[Train metric keeps improving]
  C --> E[Val metric starts declining]
  D --> F[Growing gap = overfitting signal]
  E --> F
  F --> G[Mitigation: stop early / regularize / simplify]
```

### Logistic regression intuition

Logistic regression is a simple baseline classifier that learns a curve for turning input features into a probability.

```mermaid
flowchart LR
  A[Data point: feature values] --> B[Weighted sum: w*x + b]
  B --> C[Sigmoid curve]
  C --> D[Probability between 0 and 1]
  D --> E{Above threshold?}
  E -->|Yes| F[Predict class 1]
  E -->|No| G[Predict class 0]
```

Before training, the curve may sit in the wrong place and classify many points badly. During training, the model changes its weight and bias so the curve moves toward the observed data. In the Week 5 notebook, `matplotlib` is used to draw:

- labeled data points from two classes
- the logistic curve before learning
- the learned curve after fitting `LogisticRegression`
- the decision threshold that turns probability into a class label

That picture is the core machine-learning idea: the program does not receive the final rule directly; it adjusts a rule from examples.

### LLM training as the same loop at larger scale

```mermaid
flowchart LR
  A[Raw text and instruction data] --> B[Clean and tokenize]
  B --> C[Pretraining]
  C --> D[Supervised fine-tuning]
  D --> E[Evaluation]
  E --> F[Preference tuning / alignment]
  F --> G[Deployment and inference]
  G --> H[Monitoring and feedback]
  H --> B
```

LLM training is larger and more expensive than the Week 5 baseline, but the discipline is the same: prepare data, train, evaluate, save evidence, compare runs, and iterate.

## Common pitfalls

- Evaluating on training data.
- Changing multiple variables at once (you can’t tell what caused improvement).
- Not saving the exact config that produced the metrics.

## Workshop / Implementation Plan

- Use the provided `train.py` workshop script:
  - load data
  - split train/validation
  - train a baseline classifier
  - print metrics
  - save artifacts
- Run 2 lightweight baseline experiments:
  - change one hyperparameter OR switch models OR change one feature choice
- Generate comparison reports under `reports/`:
  - what you changed
  - what happened
  - one next experiment idea

Example starter commands:

```bash
python train.py --input sample_iris.csv --label_col label --seed 42 --max_iter 200
python train.py --input sample_iris.csv --label_col label --seed 42 --max_iter 1000
python compare_runs.py --artifacts_dir artifacts --output_dir reports
```

## Deliverables

- At least two folders like `artifacts/run_.../`, each containing `config.json`, `metrics.json`, `val_report.txt`, and `model.joblib`.
- A comparison report such as `reports/comparison_report.md`.
- A short reflection explaining the one change you made, what happened, and one next experiment.

Cross-validation, statistical significance testing, complex visualization, and multi-model systems are optional advanced work, not required for Week 5.

## Why This Matters for Learning AI

The training loop is the beating heart of machine learning. Every ML system — from a simple spam filter to a state-of-the-art image classifier — follows the same fundamental cycle: load data, train, evaluate, iterate. Understanding this loop deeply is what separates someone who *uses* AI tools from someone who *builds* them.

### Train/validation splits prevent self-deception

If you evaluate a model on the same data it was trained on, it will look artificially good — like a student who memorizes test answers without understanding the material. The train/validation split forces you to measure how well your model *generalizes* to data it has never seen. As [Lightly.ai](https://www.lightly.ai/blog/train-test-validation-split) explains, *"The true measure of a machine learning model is how well it can generalize and make accurate predictions on completely unseen data in real-world scenarios."*

This concept is so fundamental that [Wikipedia's ML article](https://en.wikipedia.org/wiki/Training,_validation,_and_test_data_sets) states: *"The standard machine learning practice is to train on the training set and tune hyperparameters using the validation set, where the validation process selects the model with the lowest validation loss."*

### Baselines give you a reference point

You can't know if a fancy model is "good" unless you compare it to something simple. A baseline model (e.g., logistic regression, majority-class predictor) sets the floor. If your complex deep learning model barely beats a baseline, you know something is wrong — or that the problem is harder than expected.

### Saving artifacts makes experiments trustworthy

Every experiment should produce saved artifacts: the config that was used, the metrics that resulted, and the trained model itself. Without these, you're relying on memory and screenshots — which is how results get lost or misreported. According to [AIMultiple](https://research.aimultiple.com/reproducible-ai/), *"A lack of reproducibility blurs the line between scientific production and marketing"* — saving artifacts is how you stay on the science side.

### References

- [Train Test Validation Split: Best Practices & Examples (Lightly.ai)](https://www.lightly.ai/blog/train-test-validation-split)
- [Training, validation, and test data sets (Wikipedia)](https://en.wikipedia.org/wiki/Training,_validation,_and_test_data_sets)
- [Reproducible AI: Why it Matters (AIMultiple, 2026)](https://research.aimultiple.com/reproducible-ai/)

## Self-check questions

- Can you explain overfitting without using equations?
- If someone runs your command twice, will results be identical or explainably close?
- Can you point to the saved artifact that proves your reported metric?
