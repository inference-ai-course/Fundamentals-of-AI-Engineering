# Week 2 — AI Prompts for Learning Python

## Overview

Week 1 taught general AI prompting. Week 2 applies the same habits to Python: ask for explanations, run code, read errors, debug, and verify results.

The goal is not to let AI do everything. The goal is to use AI as a tutor while you stay responsible for running the code and checking the result.

## Prompt Pattern 1: Explain Before Editing

Use this when reading a function from `code_templates/`.

```text
I am new to Python. Explain this function in simple language.

Please include:
- what the inputs are
- what the output is
- what each line does
- one example call and result

Code:
[paste function here]
```

Follow-up:

```text
Now ask me 2 short questions to check whether I understood this function.
Do not give the answers until I try.
```

## Prompt Pattern 2: Learn By Changing One Thing

Use this after you understand a function.

```text
I understand the basic function. Suggest one small beginner-friendly change I can make myself.

Requirements:
- do not rewrite the whole file
- explain exactly where the change goes
- tell me how to run or test it afterward
```

## Prompt Pattern 3: Run Code And Interpret Output

Use this when you can run a script but do not understand the output.

```text
I ran this command:
[paste command]

It printed:
[paste output]

Explain what happened in beginner-friendly language.
Tell me whether the output proves the function worked.
```

## Prompt Pattern 4: Debug From The Full Error

Use this when code fails. Always paste the full traceback, not just the last line.

```text
I am debugging Python as a beginner.

Goal:
[what you tried to do]

Command I ran:
[paste command]

Full error:
[paste traceback]

Please help me:
1. identify the first error I should fix
2. explain why it happened
3. suggest the smallest fix
4. tell me how to verify the fix
```

## Prompt Pattern 5: Tutor Mode / Learn Mode

Use this with ChatGPT, Claude, Cursor, Copilot Chat, or Claude Code Learning output style.

```text
Act as a Python tutor. Do not just give me the final answer.

When I paste code:
- explain the idea briefly
- ask me to predict the output
- give me one small TODO to complete
- help me verify the result after I run it
```

If you have Claude Code, the Learning output style is useful for this because it encourages learn-by-doing and may ask you to complete small `TODO(human)` sections. If you do not have Claude Code, use the tutor prompt above in any AI chat tool.

## Required Week 2 Prompt Log

Save at least 5 useful prompts in `ai_python_learning_log.md`.

For each prompt, record:

- Tool used: ChatGPT, Claude, Cursor, Copilot Chat, Claude Code, or another tool
- Task: explain, run, modify, debug, or verify
- Prompt used
- What the AI helped with
- What you personally ran or checked

## Example Log Entry

```markdown
## Prompt 1: Debug a syntax error

- Tool used: Claude
- Task: debug
- Prompt:
  "I ran python debugging_practice.py and got this full error..."
- AI helped with:
  It explained that a function definition needs a colon.
- I verified:
  I added the colon, reran the script, and got the next error.
```
