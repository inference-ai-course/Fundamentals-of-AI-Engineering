# Sample Walkthrough: Debug A Runtime Error With AI

This walkthrough shows one complete AI-assisted debugging workflow. It uses only the first bug in `debug_02_runtime.py`.

After reading this sample, complete the remaining runtime and logic bugs yourself.

## Goal

Debug this problem:

- File: `debugging_exercises/debug_02_runtime.py`
- Case: `average([])`
- Error type: runtime error
- Expected safe behavior: an empty list should not crash the program

## Before Debugging: Confirm Your Environment

Do this before running the debugging sample. The point of this walkthrough is to debug Python code, not to debug environment setup.

From the repository root, enter Week 2:

```bash
cd week_02
```

Confirm Python runs:

```bash
python --version
```

If your instructor asked you to use `.venv`, activate it first. Then run the normal-code checkpoint:

```bash
python run_template_examples.py
```

This command should print several successful function outputs, such as:

```text
add_numbers(2, 3) = 5
calculate_average([10, 20, 30]) = 20.0
```

If `run_template_examples.py` fails because Python, paths, or packages are not set up, stop here and return to [Week 2 — Python Environment Setup](../06_python_environment_setup.md).

Only continue once normal code can run.

## Step 1: Run The File

From `week_02/`, run:

```bash
python debugging_exercises/debug_02_runtime.py
```

You should see an error similar to:

```text
Case 1: empty average
Traceback (most recent call last):
  File ".../debug_02_runtime.py", line 38, in <module>
    main()
  File ".../debug_02_runtime.py", line 28, in main
    print(average([]))
  File ".../debug_02_runtime.py", line 11, in average
    return sum(numbers) / len(numbers)
ZeroDivisionError: division by zero
```

Copy the full traceback. Do not copy only the last line.

## Step 2: Ask A Browser AI Tool

Use ChatGPT, Claude, or another chat tool:

```text
I am debugging Python as a beginner.

Goal:
Calculate the average of a list safely.

Command I ran:
python debugging_exercises/debug_02_runtime.py

Full error:
[paste the full traceback]

Please explain:
1. where the error starts
2. why division by zero happened
3. the smallest safe fix
4. how I should verify the fix
```

What you should expect AI to identify:

- `main()` calls `average([])`.
- `numbers` is an empty list.
- `len(numbers)` is `0`.
- `sum(numbers) / len(numbers)` becomes `0 / 0`, which raises `ZeroDivisionError`.

## Step 3: Use An IDE AI Tool

In Cursor, VS Code Copilot Chat, or a similar AI editor:

1. Open `debugging_exercises/debug_02_runtime.py`.
2. Highlight this function:

   ```python
   def average(numbers):
       return sum(numbers) / len(numbers)
   ```

3. Ask:

   ```text
   Explain why this function fails for an empty list.
   Suggest the smallest beginner-friendly fix.
   Do not rewrite the whole file.
   ```

4. Review the suggestion before applying it.

Do not blindly accept a large rewrite. This bug needs only a small guard.

## Step 4: Claude Code Learning-Style Prompt

If you use Claude Code or another agentic coding tool, ask it to teach instead of solving everything:

```text
Use a learning style. Do not fix the whole file for me.

Look at debugging_exercises/debug_02_runtime.py.
Help me understand only the first error from average([]).
Give me one TODO to complete manually, then tell me how to verify it.
```

The useful learning behavior is:

- AI explains the traceback.
- AI points to the small change.
- You make the edit.
- AI helps you verify.

## Step 5: Apply The Minimal Fix

For this course, use the same beginner-friendly style as earlier templates: return `None` when the input cannot produce a valid result.

Change:

```python
def average(numbers):
    return sum(numbers) / len(numbers)
```

To:

```python
def average(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)
```

This is a small, clear fix:

- normal lists still return an average
- empty lists return `None`
- the function no longer divides by zero

## Step 6: Verify

Before rerunning the whole file, test the function in isolation:

```bash
python - <<'PY'
from debugging_exercises.debug_02_runtime import average

print("average([10, 20, 30]) =", average([10, 20, 30]))
print("average([]) =", average([]))
PY
```

Expected output:

```text
average([10, 20, 30]) = 20.0
average([]) = None
```

Then rerun:

```bash
python debugging_exercises/debug_02_runtime.py
```

The first bug should be fixed. The script will then continue to the next bug. That is expected.

## Step 7: Write Your Debugging Record

Use this format:

```markdown
## Debugging Record: Runtime Error

- File: debugging_exercises/debug_02_runtime.py
- Command: python debugging_exercises/debug_02_runtime.py
- Error: ZeroDivisionError: division by zero
- Cause: average([]) tried to divide by len([]), which is 0
- AI prompt: [paste your prompt]
- Fix applied: added an empty-list guard that returns None
- Verification:
  - average([10, 20, 30]) returned 20.0
  - average([]) returned None
```

## What To Do Next

Do not use this walkthrough as an answer key for the whole file.

Continue with:

- `debug_02_runtime.py` Case 2: list index bug
- `debug_02_runtime.py` Case 3: `None` indexing bug
- `debug_03_logic.py`: logic errors with expected vs actual output
