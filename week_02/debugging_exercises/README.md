# Week 2 Debugging Exercises

These exercises help you practice debugging one problem at a time. Start here before using `code_templates/debugging_practice.py`, which is a mixed challenge with many errors in one file.

## Recommended Order

Required practice:

1. `../02_debugging_with_ai_lab.ipynb` - first exposure in notebook cells.
2. `sample_runtime_debugging_walkthrough.md` - detailed AI coding tool sample using `debug_02_runtime.py` Case 1.
3. `debug_02_runtime.py` - required runtime-error practice. Do Case 2 and Case 3 yourself.
4. `debug_03_logic.py` - required logic-error practice.

Optional/stretch practice:

5. `debug_01_syntax.py` - syntax and indentation errors.
6. `debug_04_data_lists.py` - list and dictionary mistakes useful for Week 3.
7. `debug_05_pandas_intro.py` - pandas/data debugging after your environment works.
8. `../code_templates/debugging_practice.py` - final mixed challenge.

## Exercise Map

| File | Status | Error type | Why AI coding tools help | Verification target |
|---|---|---|---|---|
| `sample_runtime_debugging_walkthrough.md` | Sample | Runtime | Shows browser AI, IDE AI, and learning-style workflows | `average([])` no longer crashes |
| `debug_02_runtime.py` | Required | Runtime | Tracebacks give AI concrete evidence | Case 2 and Case 3 fixed after the sample |
| `debug_03_logic.py` | Required | Logic | Expected-vs-actual output gives AI a target | Printed outputs match expected values |
| `debug_01_syntax.py` | Optional | Syntax | AI can explain syntax rules from short examples | All cases print expected results |
| `debug_04_data_lists.py` | Optional | Data structures | AI can reason from simple list/dict examples | Missing counts, keys, and totals are correct |
| `debug_05_pandas_intro.py` | Optional | Data/pandas | AI can connect errors to Week 3 data work | Missing columns, string numbers, and missing values handled |
| `../code_templates/debugging_practice.py` | Optional mixed challenge | Mixed | AI helps fix one issue at a time | File can run after progressive fixes |

## How To Run

From `week_02/`:

```bash
python --version
python run_template_examples.py
```

The normal-code checkpoint should succeed before you start debugging. If it fails, return to `../06_python_environment_setup.md`.

Then run the debugging exercises:

```bash
python debugging_exercises/debug_02_runtime.py
python debugging_exercises/debug_03_logic.py
```

For the optional pandas file:

```bash
python debugging_exercises/debug_05_pandas_intro.py
```

If pandas is missing, return to `../06_python_environment_setup.md`.

## Sample First, Exercises Second

Read `sample_runtime_debugging_walkthrough.md` once before starting the required scripts. It assumes your environment works and demonstrates the workflow using only the first bug from `debug_02_runtime.py`.

Then complete your own debugging records for:

- one remaining runtime error from `debug_02_runtime.py`
- one logic error from `debug_03_logic.py`

## AI Debugging Prompt

Use this prompt after each failure or wrong output:

```text
I am debugging Python as a beginner.

Goal:
[what the exercise is trying to do]

Command I ran:
[paste command]

Full error or wrong output:
[paste full traceback or output]

Please help me:
1. identify the first problem to fix
2. explain why it happened
3. suggest the smallest fix
4. tell me how to verify the fix
```

## Debugging Record Format

For each required debugging task, write:

```markdown
## Debugging Record

- File:
- Command:
- Error or wrong output:
- AI prompt:
- AI explanation:
- Fix applied:
- Verification:
```

## What Counts As Verification?

Good verification means:

- the original failing command now runs, or
- the wrong output now matches the expected output, and
- you tested at least one normal case after the fix.
