# Code Templates for Week 2

This directory contains Python code templates for practicing AI-assisted programming.

## Files

| File | Purpose | Difficulty |
|------|---------|------------|
| `simple_math.py` | Basic mathematical functions | Easy |
| `text_processing.py` | String manipulation functions | Easy |
| `data_processing.py` | List/number processing functions | Medium |
| `debugging_practice.py` | Code with intentional bugs for debugging practice | Medium |

## How to Use These Templates

### For Reading Practice (Part 03)

1. Open a file in Cursor
2. Ask AI to explain each function
3. Document your understanding

**Example prompts:**
```text
"What does this function do?"
"Explain each line of this function"
"What is the purpose of [keyword]?"
```

### For Modification Practice (Part 04)

1. Copy the file you want to edit into `modified_code/`
2. Read and understand a function first
3. Ask AI to make specific modifications
4. Review and apply changes only in the copied file
5. Test the modified code

**Example prompts:**
```text
"Add error handling for empty input"
"Add comments explaining each line"
"Change the return value for edge cases"
```

### For Debugging Practice (Part 05)

1. Copy `debugging_practice.py` to `modified_code/debugging_practice_fixed.py`
2. Try to run a syntax check on the copied file (expect errors)
3. Ask AI to help identify and fix errors
4. Document at least one complete fix

**Example prompts:**
```text
"This gives error [error message]. What's wrong?"
"How do I fix this?"
"Why did that fix work?"
```

## Learning Objectives

After practicing with these templates, you should be able to:

- Explain at least 5 functions using AI assistance
- Complete 2-3 small modifications with AI help
- Debug at least 1 error with AI guidance and verification

## Tips

1. **Start simple**: Begin with `simple_math.py` before `data_processing.py`
2. **Read first**: Always understand code before modifying
3. **Copy before changes**: Keep original templates unchanged
4. **Test frequently**: Run code after each modification
5. **Take notes**: Document what you learn

## Useful Commands

Run these from the Week 2 folder after creating `modified_code/`:

```bash
python --version
python -B -m py_compile modified_code/simple_math.py
python -B -m py_compile modified_code/data_processing.py
python -B -m py_compile modified_code/debugging_practice_fixed.py
```

The original `debugging_practice.py` intentionally does not pass syntax checking at first. Fix the copied file one issue at a time.
