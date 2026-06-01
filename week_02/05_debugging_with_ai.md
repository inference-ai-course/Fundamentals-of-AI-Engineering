# Week 2 — Part 05: Debugging Common Errors with AI

## Overview

Errors are inevitable when working with code. This section teaches you to use AI to understand and fix errors efficiently.

---

## What is Debugging?

### The debugging process

```
Error occurs → Understand error → Find cause → Fix → Verify
```

### AI accelerates debugging

| Traditional debugging | AI-assisted debugging |
|----------------------|----------------------|
| Read error message → Search docs → Trial and error | Paste error → AI explains → AI suggests fix |
| Hours of investigation | Minutes to understand |

---

## Types of Errors You'll Encounter

### Syntax errors

**What they are:** Code doesn't follow language rules.

**Example:**
```python
def add_numbers(a, b)
    return a + b  # Missing colon after def
```

**Error message:**
```
SyntaxError: expected ':'
```

**How AI helps:**
```
This code has a syntax error. What's wrong?
[paste code]
```

---

### Runtime errors

**What they are:** Code runs but fails during execution.

**Example:**
```python
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

calculate_average([])  # Empty list
```

**Error message:**
```
ZeroDivisionError: division by zero
```

**How AI helps:**
```
This gives "ZeroDivisionError: division by zero". 
What's wrong and how do I fix it?
```

---

### Type errors

**What they are:** Wrong type of data used.

**Example:**
```python
def add_numbers(a, b):
    return a + b

add_numbers("hello", 5)  # String + number
```

**Error message:**
```
TypeError: can only concatenate str (not "int") to str
```

**How AI helps:**
```
This gives TypeError. What's wrong?
```

---

### Logic errors

**What they are:** Code runs but produces wrong result.

**Example:**
```python
def calculate_average(numbers):
    return sum(numbers) * len(numbers)  # Should divide, not multiply
```

**No error message, but wrong output.**

**How AI helps:**
```
This function should calculate average, but returns wrong values.
Can you check if the logic is correct?
```

---

## The Debugging Workflow with AI

### Step 1: Identify the error

- What is the error message?
- When does it occur?
- What were you trying to do?

### Step 2: Ask AI

**Prompt template:**
```
I got this error: [error message]
Here's the code: [paste code]
What's wrong and how do I fix it?
```

### Step 3: Review AI's analysis

**Check:**
- Does AI correctly identify the cause?
- Does the explanation make sense?
- Is the suggested fix appropriate?

### Step 4: Apply fix

- Use Cmd+K to apply suggested fix
- Or manually make the change

### Step 5: Verify

- Run the code again
- Check if error is gone
- Test edge cases

---

## Practical Debugging Examples

### Example 1: Syntax error

**Code:**
```python
def greet(name)
    print("Hello, " + name)
```

**Error:**
```
SyntaxError: expected ':'
```

**Ask AI:**
```
This code gives "SyntaxError: expected ':'".
What's wrong?
```

**AI response:**
```
The function definition is missing a colon.
It should be: def greet(name):
```

**Fix:** Add colon, verify.

---

### Example 2: Runtime error

**Code:**
```python
numbers = [1, 2, 3, 4, 5]
for i in range(10):
    print(numbers[i])
```

**Error:**
```
IndexError: list index out of range
```

**Ask AI:**
```
This gives IndexError. 
The list has 5 items but I'm looping to 10.
What's wrong?
```

**AI response:**
```
You're trying to access indices 0-9, but the list 
only has indices 0-4. Either:
1. Loop to 5: range(5)
2. Or use len(numbers): range(len(numbers))
```

**Fix:** Use `range(len(numbers))`, verify.

---

### Example 3: Logic error

**Code:**
```python
def is_even(number):
    return number % 2 == 1  # Wrong check
```

**Behavior:** Returns True for odd numbers, False for even.

**Ask AI:**
```
This function should return True for even numbers.
But it returns True for odd numbers.
What's wrong?
```

**AI response:**
```
The logic is inverted. number % 2 == 1 checks for odd.
For even, use: number % 2 == 0
```

**Fix:** Change to `number % 2 == 0`, verify.

---

## Recommended Debugging Practice Order

## Before You Debug: Environment Checklist

Debugging practice starts after environment setup. Before running broken code, verify that normal code runs:

```bash
cd week_02
python --version
python run_template_examples.py
```

Use this rule:

- If `python --version` fails, you have an environment/path problem.
- If `run_template_examples.py` fails, return to `06_python_environment_setup.md` or ask AI about the setup error.
- If normal code runs but a debugging exercise fails, that is the intended Python bug to investigate.

This separation matters: beginners should not confuse a broken environment with a broken program.

Start with isolated exercises before the mixed challenge:

1. `02_debugging_with_ai_lab.ipynb` - notebook cells for first exposure.
2. `debugging_exercises/sample_runtime_debugging_walkthrough.md` - detailed AI coding tool sample.
3. `debugging_exercises/debug_02_runtime.py` - required runtime-error practice.
4. `debugging_exercises/debug_03_logic.py` - required logic-error practice.
5. `debugging_exercises/debug_01_syntax.py` - optional syntax practice.
6. `debugging_exercises/debug_04_data_lists.py` - optional list/dictionary practice for Week 3 readiness.
7. `debugging_exercises/debug_05_pandas_intro.py` - optional pandas/data practice after environment setup.
8. `code_templates/debugging_practice.py` - optional mixed challenge with many bugs in one file.

Why this order works: isolated files let you run one category of problem at a time. The mixed challenge is useful after students already know how to capture errors, ask AI, apply fixes, and verify.

Before doing the required runtime exercise, read the sample walkthrough:

- [Sample Runtime Debugging Walkthrough](debugging_exercises/sample_runtime_debugging_walkthrough.md)

It shows how to use browser AI, IDE AI, and Claude Code Learning-style prompts for the first `debug_02_runtime.py` bug. The remaining runtime and logic bugs are left for student practice.

## Hands-on Exercises

### Exercise 1: Fix syntax errors (10 minutes)

1. Open `debugging_exercises/debug_01_syntax.py`
2. Run the code (see errors)
3. For each error, ask AI:
   ```
   What's wrong with this code?
   [paste problematic section]
   ```
4. Apply fixes
5. Run and verify

### Exercise 2: Fix runtime errors (15 minutes)

1. Open `debugging_exercises/debug_02_runtime.py`
2. Run it from `week_02/`:
   ```bash
   python debugging_exercises/debug_02_runtime.py
   ```
3. Fix one error at a time
4. Ask AI to explain each error
5. Apply suggested fixes
6. Test with normal and edge-case inputs

### Exercise 3: Find logic errors (15 minutes)

1. Open `debugging_exercises/debug_03_logic.py`
2. Run it from `week_02/`:
   ```bash
   python debugging_exercises/debug_03_logic.py
   ```
3. Compare expected vs actual output
4. Ask AI to explain each wrong result
5. Apply suggested fixes
6. Verify correct behavior

### Exercise 4: Week 3 readiness debugging (optional)

Use:

```bash
python debugging_exercises/debug_04_data_lists.py
```

This file practices list and dictionary bugs that resemble Week 3 data profile work.

### Exercise 5: Pandas debugging preview (optional)

Use this only after `python -c "import pandas as pd; print(pd.__version__)"` works:

```bash
python debugging_exercises/debug_05_pandas_intro.py
```

This file previews pandas issues such as missing columns, string numbers, and missing values.

### Exercise 6: Mixed challenge (optional)

1. Open `code_templates/debugging_practice.py`
2. Fix the first syntax errors so the file can load.
3. Continue fixing runtime and logic errors one at a time.
4. Ask AI:
   ```
   This function should do X, but it does Y.
   Can you check the logic?
   ```
5. Apply fixes
6. Verify correct behavior

---

## When AI Gets It Wrong

### AI might not solve everything

| Situation | What to do |
|-----------|------------|
| AI's fix doesn't work | Iterate: "That fix didn't work. Try another approach." |
| AI doesn't understand error | Provide more context: describe what you were trying to do |
| Multiple errors | Fix one at a time: "First, help me fix the syntax error" |

### Debugging fallbacks

If AI can't solve:
1. **Search**: Look up error message online
2. **Simplify**: Isolate the problematic code
3. **Ask differently**: Describe your goal, not just the error

---

## Common Pitfalls

### Pitfall 1: Not providing error message

**Symptom:** "This doesn't work" — vague request.

**Fix:** Include:
- Exact error message
- What you were trying to do
- The problematic code

### Pitfall 2: Applying fix without understanding

**Symptom:** Fix works, but you don't know why.

**Fix:** Ask AI:
```
Why did that fix work? 
Explain what caused the error.
```

### Pitfall 3: Not testing after fix

**Symptom:** Error gone, but new problems emerge.

**Fix:** Test thoroughly:
- Original case that failed
- Other edge cases
- Normal cases

---

## Debugging Tips

### Tip 1: Read error messages

Error messages often tell you the problem:
- `SyntaxError`: Check syntax
- `TypeError`: Check data types
- `IndexError`: Check list/array access
- `ZeroDivisionError`: Check division operations

### Tip 2: Isolate the problem

If code is complex, find the specific line:
```
The error occurs at line X.
Here's that line: [paste line]
```

### Tip 3: Provide context

```
I'm trying to calculate the average of numbers.
When I pass an empty list, I get ZeroDivisionError.
Here's the code: [paste]
```

### Tip 4: Test in small steps

After fixing, test incrementally:
- First: Does it run without errors?
- Then: Does it give correct output?
- Finally: Does it handle edge cases?

---

## Practice: Debugging Exercise

Complete at least 2 debugging tasks:

1. Fix a runtime error from `debugging_exercises/debug_02_runtime.py`.
2. Find and fix a logic error from `debugging_exercises/debug_03_logic.py`.

Optional extra practice:

- Fix one syntax error from `debugging_exercises/debug_01_syntax.py`.
- Fix one pandas/data issue from `debugging_exercises/debug_05_pandas_intro.py`.
- Attempt the mixed challenge in `code_templates/debugging_practice.py`.

For each, document:
- Error message (if any)
- What you asked AI
- AI's explanation
- The fix you applied
- How you verified

---

## Self-check

- Can you identify different types of errors?
- Can you provide useful error context to AI?
- Can you review AI's suggested fix?
- Can you test fixes thoroughly?
- Have you completed at least 2 debugging tasks?

---

## References

- `code_templates/debugging_practice.py`: Practice file with errors
- `debugging_exercises/`: Isolated debugging scripts
- Python error types: [Python docs](https://docs.python.org/3/tutorial/errors.html)
