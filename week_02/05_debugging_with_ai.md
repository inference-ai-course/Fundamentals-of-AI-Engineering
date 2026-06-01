# Week 2 — Part 05: Debugging Common Errors with AI

## Overview

Errors are inevitable when working with code. This section teaches you to use AI to understand and fix errors efficiently.

---

## What is Debugging?

### The debugging process

```text
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
```text
SyntaxError: expected ':'
```

**How AI helps:**
```text
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
```text
ZeroDivisionError: division by zero
```

**How AI helps:**
```text
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
```text
TypeError: can only concatenate str (not "int") to str
```

**How AI helps:**
```text
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
```text
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
```text
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
```text
SyntaxError: expected ':'
```

**Ask AI:**
```text
This code gives "SyntaxError: expected ':'".
What's wrong?
```

**AI response:**
```text
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
```text
IndexError: list index out of range
```

**Ask AI:**
```text
This gives IndexError. 
The list has 5 items but I'm looping to 10.
What's wrong?
```

**AI response:**
```text
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
```text
This function should return True for even numbers.
But it returns True for odd numbers.
What's wrong?
```

**AI response:**
```text
The logic is inverted. number % 2 == 1 checks for odd.
For even, use: number % 2 == 0
```

**Fix:** Change to `number % 2 == 0`, verify.

---

## Hands-on Exercises

`code_templates/debugging_practice.py` is intentionally broken. Running the original file should fail, starting with a syntax error. That is the point of the exercise.

Work on a copied file:

```bash
mkdir -p modified_code
cp code_templates/debugging_practice.py modified_code/debugging_practice_fixed.py
```

Use this command after each fix:

```bash
python -B -m py_compile modified_code/debugging_practice_fixed.py
```

When syntax errors are fixed, you can run small function calls to check behavior:

```bash
cd modified_code
python -c "from debugging_practice_fixed import greet; greet('AI Engineer')"
```

### Exercise 1: Fix syntax errors (10 minutes)

1. Open `modified_code/debugging_practice_fixed.py`
2. Run the syntax check command above and read the first error
3. For each error, ask AI:
   ```text
   What's wrong with this code?
   [paste problematic section]
   ```
4. Apply fixes
5. Run the syntax check again and verify the error is gone

### Exercise 2: Fix runtime errors (15 minutes)

1. Open `modified_code/debugging_practice_fixed.py`
2. Find functions that cause runtime errors
3. Ask AI to explain each error
4. Apply suggested fixes
5. Test with various inputs

### Exercise 3: Find logic errors (15 minutes)

1. Open `modified_code/debugging_practice_fixed.py`
2. Find functions that run but give wrong results
3. Ask AI:
   ```text
   This function should do X, but it does Y.
   Can you check the logic?
   ```
4. Apply fixes
5. Verify correct behavior

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
```text
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
```text
The error occurs at line X.
Here's that line: [paste line]
```

### Tip 3: Provide context

```text
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

## Deliverable: Debugging Exercise

Complete at least 1 debugging record:

1. Choose one syntax, runtime, or logic error from `debugging_practice_fixed.py`
2. Use AI to understand the cause
3. Apply a fix in the copied file
4. Verify with a command or function call

For the record, document:
- Error message (if any)
- What you asked AI
- AI's explanation
- The fix you applied
- How you verified

Optional extension: fix additional runtime or logic errors and add them to the same file.

---

## Self-check

- Can you identify different types of errors?
- Can you provide useful error context to AI?
- Can you review AI's suggested fix?
- Can you test fixes thoroughly?
- Have you completed at least 1 debugging record?

---

## References

- `code_templates/debugging_practice.py`: Practice file with errors
- Python error types: [Python docs](https://docs.python.org/3/tutorial/errors.html)
