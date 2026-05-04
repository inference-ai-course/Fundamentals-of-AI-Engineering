# Week 2 — Part 03: Reading Code with AI Help

## Overview

Learning to read code is the foundation of AI-assisted programming. You'll use AI to understand existing code without needing to learn every detail yourself.

---

## Why Read Code First?

### The learning sequence

```text
Read → Understand → Modify → Create
```

Before you can modify or create code, you need to understand what exists.

### AI changes the equation

| Traditional approach | AI-assisted approach |
|---------------------|----------------------|
| Learn syntax → Read code → Understand | Ask AI → Understand → Learn syntax gradually |

You don't need to master programming first. AI helps you understand code now.

---

## Reading Code Workflow

### The pattern for understanding

```text
1. Identify: What file/function do you want to understand?
2. Ask: Prompt AI to explain
3. Review: Check if explanation makes sense
4. Iterate: Ask follow-up questions
5. Apply: Take notes, build understanding
```

### Key prompts for reading

| Prompt type | Example |
|-------------|---------|
| **Overview** | "What does this file do overall?" |
| **Line-by-line** | "Explain each line of this function" |
| **Concept** | "What is a 'variable' in this code?" |
| **Purpose** | "Why is this function written this way?" |
| **Example** | "Give an example of how this is used" |

---

## Practical Examples

### Example 1: Understanding a simple function

**File: `code_templates/simple_math.py`**

```python
def add_numbers(a, b):
    return a + b
```

**Prompts to use:**

```text
"What does this function do?"
```
→ AI: "It takes two numbers (a and b) and returns their sum."

```text
"Explain each part: 'def', 'return', 'a + b'"
```
→ AI explains each keyword/syntax element.

```text
"Give an example of using this function"
```
→ AI: "add_numbers(3, 5) would return 8"

---

### Example 2: Understanding a more complex function

**File: `code_templates/data_processing.py`**

```python
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0
    return total / count
```

**Prompts to use:**

```text
"Explain what this function does step by step"
```

```text
"Why is there an 'if count == 0' check?"
```

```text
"What happens if I call this with an empty list?"
```

```text
"Explain 'sum' and 'len' — what do they do?"
```

---

### Example 3: Understanding a file structure

**File: `code_templates/data_processing.py` (full file)**

**Prompts to use:**

```text
"List all functions in this file and what each does"
```

```text
"Which function is the most important?"
```

```text
"How do these functions relate to each other?"
```

---

## Prompt Strategies

### Strategy 1: Start broad, then narrow

```text
Broad: "What does this file do?"
→ AI gives overview

Narrow: "Explain the first function in detail"
→ AI explains specific function

More narrow: "What does line 3 do?"
→ AI explains specific line
```

### Strategy 2: Ask about unfamiliar terms

```text
"What does 'def' mean?"
"What is a 'variable'?"
"What does 'return' do?"
```

AI can teach you syntax as you encounter it.

### Strategy 3: Ask for examples

```text
"Show me an example of calling this function"
"What input would I give to get output X?"
```

Examples make abstract concepts concrete.

### Strategy 4: Ask about purpose

```text
"Why is this written this way?"
"What problem does this solve?"
"When would I use this?"
```

Understanding purpose helps you remember.

---

## Hands-on Exercises

### Exercise 1: Explain a simple function (10 minutes)

1. Open `code_templates/simple_math.py`
2. Ask AI: "What does the function `add_numbers` do?"
3. Ask: "Explain the keyword 'def'"
4. Ask: "What does 'return' mean?"
5. Ask: "Give an example of using this function"

**Goal**: Understand all parts of a simple function.

### Exercise 2: Explain a complex function (15 minutes)

1. Open `code_templates/data_processing.py`
2. Ask AI: "Explain `calculate_average` step by step"
3. Ask: "What does `sum(numbers)` do?"
4. Ask: "What does `len(numbers)` do?"
5. Ask: "Why check if count == 0?"
6. Ask: "What would happen without that check?"

**Goal**: Understand all parts, including error handling.

### Exercise 3: Explain multiple functions (15 minutes)

1. Open `code_templates/data_processing.py`
2. Ask AI: "List all functions and summarize each"
3. Pick one function and ask for detailed explanation
4. Ask: "How do these functions work together?"

**Goal**: Understand a file with multiple functions.

---

## Common Pitfalls

### Pitfall 1: Accepting without understanding

**Symptom**: AI explains, you accept, but don't actually understand.

**Fix**: Test your understanding:
- Can you explain it to someone else?
- Can you predict what the code does for a specific input?

### Pitfall 2: Too technical explanations

**Symptom**: AI uses terms you don't understand.

**Fix**: Ask for simpler explanation:
```text
"That's too technical. Explain it as if teaching 
someone with no programming background."
```

### Pitfall 3: Not asking follow-up questions

**Symptom**: You stop after one explanation that's incomplete.

**Fix**: Keep asking:
- "What does X mean?"
- "Can you give an example?"
- "Why is it done this way?"

### Pitfall 4: Not saving what you learned

**Symptom**: You understand now, but forget later.

**Fix**: Take notes. Create a learning journal.

---

## Tips for Building Understanding

### Tip 1: Create explanations in your own words

After AI explains, write your own summary:

```text
"Calculate_average: 
1. Add all numbers together (sum)
2. Count how many numbers (len)
3. If no numbers, return 0 (special case)
4. Otherwise, divide sum by count"
```

### Tip 2: Track unfamiliar terms

Keep a list of terms to learn:

```text
Terms I encountered:
- def: defines a function
- return: gives back a value
- sum: adds all items in a list
- len: counts items in a list
```

### Tip 3: Test with examples

Predict output, then verify:

```text
calculate_average([2, 4, 6])
Prediction: (2+4+6) / 3 = 4
Test: Run code, check result
```

---

## Practice: Code Explanation Exercise

By end of this section, complete:

- Explain at least 5 functions from `code_templates`
- For each function:
  - What it does (overall)
  - Key syntax/keywords used
  - An example of using it
- Save the final explanations in `report.md`
- Save the prompts that helped you in `prompts.md`

Suggested table for `report.md`:

```markdown
| File | Function/code block | My explanation | Example input/output | AI prompt used |
|------|---------------------|----------------|----------------------|----------------|
| code_templates/simple_math.py | add_numbers | | | |
```

---

## Self-check

- Can you explain at least 5 functions from the templates?
- Can you identify unfamiliar syntax and ask AI about it?
- Can you ask for simpler explanations when needed?
- Can you write your own summary of what a function does?
- Can you predict what a function returns for given input?

---

## References

- `code_templates/simple_math.py`: Simple functions to start with
- `code_templates/data_processing.py`: More complex functions
- Week 1 prompt patterns: For better prompts
