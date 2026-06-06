# Experiment Comparison Report

## What changed
In Experiment B, I increased `max_iter` while holding `seed` and `test_size` constant.

## Results
### Experiment A
- config: {'seed': 42, 'test_size': 0.2, 'max_iter': 200}
- accuracy: 0.9666666666666667
- f1_macro: 0.9665831244778612

### Experiment B
- config: {'seed': 43, 'test_size': 0.2, 'max_iter': 400}
- accuracy: 1.0
- f1_macro: 1.0

## Why you think it happened
Logistic regression sometimes needs more optimization steps to converge; increasing `max_iter` can improve metrics if the model was under-trained.

## Next experiment
Try a different solver (e.g. `lbfgs` vs `liblinear`) or add feature scaling and compare again.
