# Week 2 — Part 02: AI-Assisted Programming Workflow

## Overview

Before diving into specific skills, understand the overall workflow of AI-assisted programming. This pattern applies to reading, modifying, and debugging code.

---

## The Core Pattern

### Ask → Review → Apply → Verify

```text
1. ASK:    Describe what you want to AI
2. REVIEW: Check AI's suggestion/response
3. APPLY:  Use the suggestion (if appropriate)
4. VERIFY: Test that it works as expected
```

### Why this pattern matters

You never blindly accept AI output. Each step is essential:

| Step | Why it matters |
|------|----------------|
| **ASK** | Quality of prompt determines quality of response |
| **REVIEW** | AI can make mistakes; you must check |
| **APPLY** | You decide whether to use the suggestion |
| **VERIFY** | Testing confirms it actually works |

---

## Detailed Workflow

### Step 1: ASK (The Prompt)

**Good prompts are specific and contextual:**

| Element | Example |
|---------|---------|
| **What** | "Explain this function" |
| **Context** | "I'm new to Python" |
| **Format** | "Use simple terms, step by step" |
| **Goal** | "So I can understand what it returns" |

**Combined:**
```text
Explain this function step by step in simple terms.
I'm new to Python. Focus on what it returns and why.
```

### Step 2: REVIEW (The Check)

**What to check:**

| Aspect | What to look for |
|--------|------------------|
| **Accuracy** | Is the explanation correct? |
| **Completeness** | Did AI address your question? |
| **Clarity** | Is the response understandable? |
| **Safety** | Does the suggestion have risks? |

**If review fails: Iterate**

```text
That explanation was too technical. 
Can you explain it with an analogy?
```

### Step 3: APPLY (The Action)

**Actions depend on task:**

| Task | Apply action |
|------|--------------|
| **Understanding** | Accept explanation, take notes |
| **Modification** | Accept code change, or paste manually |
| **Debugging** | Try suggested fix |

**You control this step:** You decide whether to use AI's suggestion.

### Step 4: VERIFY (The Test)

**Verification methods:**

| Task | Verify by |
|------|-----------|
| **Understanding** | Can you explain it to someone else? |
| **Modification** | Run the code, check output |
| **Debugging** | Run code, confirm error is fixed |

**If verification fails: Debug**

```text
The code change didn't work. 
Here's the error: [error message]
What should I do?
```

---

## Iteration: The Key to Success

### Why iteration matters

First prompts rarely give perfect results. Iteration improves output:

```text
1st attempt: "Explain this function"
→ Result: Too technical

2nd attempt: "Explain in simpler terms"
→ Result: Better but incomplete

3rd attempt: "Focus on what it returns, with an example"
→ Result: Good!
```

### Iteration patterns

| Pattern | When to use |
|---------|-------------|
| **Clarify** | "I meant X, not Y" |
| **Simplify** | "That's too complex, use simpler terms" |
| **Focus** | "Focus only on X" |
| **Format** | "Format as a bullet list" |
| **Example** | "Give me a concrete example" |

---

## Common Workflow Mistakes

### Mistake 1: Skipping REVIEW

**Symptom**: You apply AI suggestions without checking.

**Risk**: Incorrect code, misunderstood explanations.

**Fix**: Always review before applying. Ask: "Does this make sense?"

### Mistake 2: Skipping VERIFY

**Symptom**: You assume code works without testing.

**Risk**: Code fails later, hard to debug.

**Fix**: Always test after changes. Run the code.

### Mistake 3: No iteration

**Symptom**: You accept first response even if it's not right.

**Risk**: Missed opportunity for better results.

**Fix**: Iterate. Ask for adjustments until satisfied.

### Mistake 4: Over-trusting AI

**Symptom**: You assume AI is always correct.

**Reality**: AI makes mistakes. You must verify.

**Fix**: Treat AI as a helpful assistant, not an expert.

---

## Workflow Examples

### Example 1: Understanding a function

```text
[ASK] "Explain what this function does:
def calculate_average(numbers):
    return sum(numbers) / len(numbers)"

[REVIEW] AI explains it divides sum by count.
Check: Is that correct? Yes.

[APPLY] Accept explanation. Take notes.

[VERIFY] Can you explain it to someone else?
"I understand: it takes a list, adds all numbers, 
divides by how many numbers there are."
```

### Example 2: Modifying code

```text
[ASK] "Add error handling to this function 
for when the list is empty."

[REVIEW] AI suggests:
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

Check: Is this correct? Yes. Is this what I want? Yes.

[APPLY] Use Cmd+K to apply, or paste manually.

[VERIFY] Test:
calculate_average([]) → returns 0 (correct!)
calculate_average([1, 2, 3]) → returns 2 (correct!)
```

### Example 3: Debugging

```text
[ASK] "This code gives an error: 'division by zero'. 
Here's the code: [paste code]. What's wrong?"

[REVIEW] AI identifies: len(numbers) is 0 for empty list.

[APPLY] Use suggested fix (add check for empty list).

[VERIFY] Run code with empty list — no error now.
```

---

## Tips for Efficient Workflow

### Tip 1: Work on copied files

AI might make unexpected changes. Copy files from `code_templates/` into `modified_code/` before editing, then save your current state before asking for modifications.

### Tip 2: Use specific prompts

| Vague | Specific |
|-------|----------|
| "Fix this" | "Add error handling for empty input" |
| "Explain" | "Explain line by line in simple terms" |
| "Improve" | "Make it faster by removing the loop" |

### Tip 3: Keep the conversation focused

One topic per conversation. New topic → new chat.

### Tip 4: Learn from AI explanations

Don't just accept — try to understand. Ask follow-up questions.

### Tip 5: Test frequently

Don't wait until the end to test. Test after each change.

### Tip 6: Record evidence

Each time you use AI for a meaningful step, record:

```text
Task:
Prompt:
AI suggestion:
Accepted or rejected:
Verification command/output:
```

These notes become your `prompts.md`, `report.md`, and `debugging_record.md`.

---

## Self-check

- Can you explain the "Ask → Review → Apply → Verify" pattern?
- Do you understand why each step matters?
- Can you iterate on a response that's not quite right?
- Do you know what to check during REVIEW?
- Do you know how to VERIFY a code change?

---

## References

- Week 1: Prompt patterns (for better ASK)
- Part 03: Reading code (APPLY for understanding)
- Part 04: Modifying code (APPLY for changes)
- Part 05: Debugging (VERIFY and iterate)
