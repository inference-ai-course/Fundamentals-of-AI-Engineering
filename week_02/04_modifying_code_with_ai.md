# Week 2 — Part 04: Modifying Code with AI Help

## Overview

After understanding code, the next skill is modifying it. You'll learn to request changes, review AI's suggestions, and apply them safely.

---

## The Modification Workflow

### Pattern for modifications

```text
1. Understand: Read the code first (use Part 03 skills)
2. Specify: Describe exactly what change you want
3. Review: Check AI's suggested change
4. Apply: Accept the change (Cmd+K or manual)
5. Verify: Test that it works
```

### Why understanding first matters

| Without understanding | With understanding |
|----------------------|-------------------|
| Blindly accept changes | Know what you're changing |
| Can't verify correctness | Can check if change makes sense |
| Risk of breaking code | Lower risk, informed decisions |

**Always read first.** Use Part 03 skills before Part 04.

---

## Types of Modifications

### Type 1: Adding comments

**Prompt:**
```text
Add comments explaining what this function does.
```

**Result:**
```python
def calculate_average(numbers):
    # Calculate the average of a list of numbers
    # Returns 0 if the list is empty
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0
    return total / count
```

### Type 2: Adding error handling

**Prompt:**
```text
Add error handling for when numbers contains non-numeric values.
```

**Result:**
```python
def calculate_average(numbers):
    try:
        total = sum(numbers)
        count = len(numbers)
        if count == 0:
            return 0
        return total / count
    except TypeError:
        return "Error: List contains non-numeric values"
```

### Type 3: Changing behavior

**Prompt:**
```text
Change this to return None instead of 0 for empty lists.
```

**Result:**
```python
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        return None  # Changed from 0
    return total / count
```

### Type 4: Adding new functionality

**Prompt:**
```text
Add a function that finds the maximum value in a list.
```

**Result:**
```python
def find_max(numbers):
    if not numbers:
        return None
    return max(numbers)
```

---

## Using Cursor's Inline Edit (Cmd+K)

### The inline edit workflow

1. **Select code**: Highlight the function/lines you want to modify
2. **Press Cmd+K**: Inline edit panel appears
3. **Describe change**: Type what you want
4. **Review**: AI shows the change (highlighted)
5. **Accept or reject**: Click "Accept" or "Reject"

### Example: Adding a comment

1. Copy `code_templates/simple_math.py` to `modified_code/simple_math.py`
2. Open `modified_code/simple_math.py`
3. Select the `add_numbers` function
3. Press Cmd+K
4. Type: "Add a comment explaining what this function does"
5. Review the highlighted change
6. Click "Accept" to apply

### Tips for inline edit

| Tip | Why |
|-----|-----|
| **Select precisely** | AI only modifies selected code |
| **Be specific** | "Add comment" vs "Add comment about parameters" |
| **Review carefully** | Check the highlighted change before accepting |
| **Save before** | Easy to undo if you saved |

---

## Using AI Chat for Modifications

### When to use chat vs inline

| Use Chat | Use Inline |
|----------|------------|
| Multiple changes across file | Single function/section |
| Planning changes first | Quick, focused edit |
| Need discussion before edit | Clear what you want |
| Want to see full context | Specific modification |

### Chat workflow

1. Open AI chat (Cmd+L)
2. Describe your goal
3. Ask AI to generate the change
4. Review the suggested code
5. Copy/paste or ask AI to apply

**Example:**
```text
I want to add error handling to calculate_average.
Can you show me the modified code?
```

AI generates the modified version. You review and apply.

---

## Practical Exercises

Before starting, create your working copy:

```bash
mkdir -p modified_code
cp code_templates/simple_math.py modified_code/simple_math.py
cp code_templates/data_processing.py modified_code/data_processing.py
```

Edit only files inside `modified_code/`.

### Exercise 1: Add comments (10 minutes)

1. Open `modified_code/simple_math.py`
2. Select the `add_numbers` function
3. Press Cmd+K
4. Type: "Add comments explaining each line"
5. Review and accept
6. Verify the comments make sense

### Exercise 2: Add error handling (15 minutes)

1. Open `modified_code/data_processing.py`
2. Find `calculate_average`
3. Ask AI (chat): "Add error handling for when numbers is not a list"
4. Review AI's suggestion
5. Apply the change (Cmd+K or paste)
6. Test: What happens with invalid input?

### Exercise 3: Change behavior (10 minutes)

1. Open `modified_code/simple_math.py`
2. Find one simple function, such as `multiply_numbers`
3. Ask AI: "Add a clear comment and one simple input check to this function. Keep the original behavior for normal numbers."
4. Review the change
5. Apply
6. Test the function with normal input

### Exercise 4: Add a new function (15 minutes)

1. Open `modified_code/data_processing.py`
2. Ask AI: "Add a function called find_median that finds the middle value"
3. Review the generated function
4. Add it to the file
5. Test with example input

---

## Reviewing Changes: What to Check

### Before accepting

| Aspect | Check |
|--------|-------|
| **Correctness** | Is the logic right? |
| **Completeness** | Did AI do everything you asked? |
| **Style** | Does it match existing code style? |
| **Safety** | Does it handle errors? |
| **No side effects** | Won't break other code? |

### After applying

| Check | How |
|-------|-----|
| **Syntax** | No red underlines in editor |
| **Run** | Execute the code |
| **Test cases** | Try different inputs |
| **Edge cases** | Empty list, zero, negative, etc. |

### Example verification commands

From your Week 2 working folder:

```bash
python -B -m py_compile modified_code/simple_math.py
python -B -m py_compile modified_code/data_processing.py
```

Then run one small function call:

```bash
cd modified_code
python -c "from simple_math import add_numbers; print(add_numbers(2, 3))"
python -c "from data_processing import calculate_average; print(calculate_average([2, 4, 6]))"
```

Record the command and observed output in `report.md`.

---

## Common Pitfalls

### Pitfall 1: Changing without understanding

**Symptom**: You modify code you don't understand.

**Risk**: Break functionality, create bugs.

**Fix**: Always use Part 03 skills first.

### Pitfall 2: Vague modification requests

**Symptom**: "Fix this" gives unexpected changes.

**Fix**: Be specific:
- "Add error handling for empty input"
- "Change return value from 0 to None"
- "Add comment at line 5"

### Pitfall 3: Not testing changes

**Symptom**: Accept change, assume it works.

**Risk**: Code fails later.

**Fix**: Always run and test after modifying.

### Pitfall 4: Not reviewing AI suggestions

**Symptom**: Accept without checking.

**Risk**: Incorrect or incomplete changes.

**Fix**: Review highlighted change carefully before accepting.

---

## Practice: Code Modification Exercise

By end of this section, complete:

- 2-3 successful small modifications:
  1. Add comments to a function
  2. Add error handling
  3. Optional: change behavior or add a small new function

For each, document:
- What you asked AI
- What change was made
- How you verified it works
- Whether you accepted, edited, or rejected the AI suggestion

---

## Self-check

- Can you use Cmd+K for inline editing?
- Can you specify modifications clearly?
- Can you review changes before accepting?
- Can you test modifications after applying?
- Have you completed 2-3 small modifications in copied files?

---

## References

- Part 03: Reading code (do this first)
- Cursor shortcuts: Cmd+K for inline edit
- `code_templates/`: Practice files
