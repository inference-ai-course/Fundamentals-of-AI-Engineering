# ML Experiment Comparison Report

**Total runs analyzed:** 4

## Summary Statistics

- **Average n_train:** 130.0
- **Average accuracy:** 0.875
- **Average f1_macro:** 0.8761
- **Average train_seconds:** 0.0129
- **Average n_val:** 32.5
- **Best n_train:** 160 (run: run_20260210_073210)
- **Best accuracy:** 0.9666666666666667 (run: run_20260210_073204)
- **Best f1_macro:** 0.9665831244778612 (run: run_20260210_073204)
- **Best train_seconds:** 0.017902612686157227 (run: run_20260210_084244)
- **Best n_val:** 40 (run: run_20260210_073210)

## Individual Runs

### run_20260210_073204

**Configuration:**
- input_csv: sample_iris.csv
- label_col: label
- max_iter: 500
- random_state: 42
- test_size: 0.2

**Metrics:**
- accuracy: 0.9667
- f1_macro: 0.9666
- n_train: 120
- n_val: 30
- train_seconds: 0.0169

### run_20260210_073210

**Configuration:**
- input_csv: sample_synthetic.csv
- label_col: label
- max_iter: 500
- random_state: 42
- test_size: 0.2

**Metrics:**
- accuracy: 0.6000
- f1_macro: 0.6046
- n_train: 160
- n_val: 40
- train_seconds: 0.0072

### run_20260210_084244

**Configuration:**
- input_csv: test_iris.csv
- label_col: label
- max_iter: 500
- random_state: 42
- test_size: 0.2

**Metrics:**
- accuracy: 0.9667
- f1_macro: 0.9666
- n_train: 120
- n_val: 30
- train_seconds: 0.0179

### run_20260210_084248

**Configuration:**
- input_csv: test_iris2.csv
- label_col: label
- max_iter: 1000
- random_state: 42
- test_size: 0.2

**Metrics:**
- accuracy: 0.9667
- f1_macro: 0.9666
- n_train: 120
- n_val: 30
- train_seconds: 0.0096

## Improvements Over Time

- **run_20260210_073210** → **run_20260210_084244**: accuracy 0.6 → 0.9666666666666667
