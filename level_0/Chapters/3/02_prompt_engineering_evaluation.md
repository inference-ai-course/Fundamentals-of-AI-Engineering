# Part 2: Vibe Coding Workshop — AI-Assisted Development

## Introduction: Learn Prompting by Building

**The problem with traditional prompt engineering courses:** They teach you theory before practice. You study temperature settings, few-shot learning, and system prompts—then struggle to apply them to real code.

**This workshop flips that model.**

You'll build a production-ready CLI app using AI as a pair programmer. Through this hands-on process, you'll learn effective prompting **implicitly**—by doing, iterating, and seeing what works.

### What You'll Build

A **Learning Assistant CLI** that:
- Tracks study sessions (topic, hours, date)
- Recommends next topics based on progress
- Outputs structured JSON for machine processing
- Includes comprehensive test coverage
- Has proper error handling and validation

### What You'll Learn (By Doing)

Instead of lectures on prompt engineering, you'll discover:
- **Spec-driven prompting**: How constraints guide AI output
- **Incremental iteration**: Small, testable changes beat big rewrites
- **Test-driven development**: Failing tests as precise prompts
- **Quality control**: AI-assisted code review

By the end, you'll have:
1. A working CLI app (your portfolio project)
2. An AI collaboration log (documenting your workflow)
3. Practical prompting skills (learned through building)

---

## Section 1: The Vibe Coding Philosophy

### Why "Vibe Coding"?

**Vibe coding** means using AI to handle scaffolding, boilerplate, and repetitive patterns—freeing you to focus on architecture, logic, and quality. It's not about letting AI write everything; it's about **strategic delegation**.

**The mental model:**
- **You**: Product owner, architect, reviewer
- **AI**: Junior developer who needs clear specs and iterative feedback

### When to Use AI vs. Write Manually

| Use AI For | Write Manually |
|------------|----------------|
| Project scaffolding (files, structure) | Critical security logic |
| Boilerplate (argparse setup, schema definitions) | Complex algorithms requiring deep thought |
| Test generation from specs | Business logic edge cases |
| Code review checklists | Performance-critical sections |
| Documentation and README files | Debugging complex state issues |

### The 5-Step Vibe Coding Loop

This workshop teaches a repeatable workflow:

```
1. SPEC     → Write requirements, constraints, acceptance tests
2. SCAFFOLD → Request minimal project structure
3. TEST     → Generate pytest tests from spec
4. PATCH    → Iterate: test failure → minimal fix → verify
5. REVIEW   → AI-assisted review + targeted refactors
```

Each step builds on the last. By the end, you have a tested, reviewed, production-ready deliverable.

### Quality Guardrails

**Critical rule:** Never trust AI output without verification.

Your guardrails:
- **Tests**: Every feature has tests (happy path + failure cases)
- **Code review**: AI reviews its own code (with your oversight)
- **Incremental changes**: Request minimal diffs, not rewrites
- **Verification loop**: Run tests after every AI change

**Remember:** AI is a tool, not a replacement for your judgment.

---

## Section 2: Step 1 — The Spec Prompt

### Why Specs Matter

A good spec is a contract between you and the AI. It defines:
- **What to build** (features, commands, inputs/outputs)
- **What NOT to build** (non-goals, scope boundaries)
- **How to verify success** (acceptance tests)

**Bad spec:**
```
Build a CLI for the learning assistant
```

**Good spec:**
```markdown
## Feature: Learning Assistant CLI

### Commands
1. `track <topic> <hours>` - Log study session
2. `status` - Show progress (JSON output)
3. `recommend` - Suggest next topic
4. `export <filename>` - Export data to JSON

### Requirements
- Data persisted in data.json
- status and export output valid JSON
- Input validation with helpful errors
- Each command has --help text

### Non-goals
- No web UI (CLI only)
- No external APIs (local data only)
- No fancy TUI (plain text output)

### Acceptance Tests
1. `status` on empty data → {"total_hours": 0, "topics": []}
2. `track python 2.5` → data.json updated correctly
3. `track invalid` → helpful error message
4. `recommend` after tracking → relevant suggestion
5. `export out.json` → valid JSON file created
```

### Anatomy of a Good Spec

**1. Commands Section**
List each command with:
- Name and arguments
- Brief description (one line)
- Expected input format

**2. Requirements Section**
Technical constraints:
- Data storage (files, formats)
- Output formats (JSON, text, etc.)
- Validation rules
- Error handling expectations

**3. Non-goals Section**
Explicitly state what you're NOT building:
- Prevents scope creep
- Keeps AI focused
- Saves iteration time

**4. Acceptance Tests Section**
5-10 concrete test scenarios:
- Happy path (normal usage)
- Edge cases (empty data, invalid inputs)
- Error cases (missing files, bad arguments)

### Example: Full Spec for Learning Assistant

```markdown
## Feature: Learning Assistant CLI

### Commands
1. `recommend` - Suggest next study topic based on progress
   - Reads from data.json
   - Returns topic name and reason
   
2. `track <topic> <hours> [date]` - Log study session
   - topic: string (required)
   - hours: float (required, must be > 0)
   - date: ISO format YYYY-MM-DD (optional, defaults to today)
   
3. `status` - Show overall progress as JSON
   - Outputs: total_hours, topics (list with name + hours)
   - Must be valid JSON (machine-parseable)
   
4. `quiz <topic>` - Generate practice questions
   - topic: string (required)
   - Returns 3-5 questions related to topic
   
5. `export <filename>` - Export all data to JSON file
   - filename: path to output file
   - Creates file with all session data

### Requirements
- **Data storage**: All data in `data.json` (JSON format)
- **Persistence**: Changes persist across runs
- **Validation**: 
  - Hours must be positive numbers
  - Dates must be valid ISO format
  - Topic names must be non-empty strings
- **Error messages**: Clear, actionable (not "error" or generic messages)
- **Help text**: Each command has `--help` flag
- **Exit codes**: 0 for success, 1 for user error, 2 for system error

### Non-goals
- ❌ No web interface (CLI only)
- ❌ No external APIs or LLM calls yet (Week 5 content)
- ❌ No fancy terminal UI (plain text is fine)
- ❌ No user authentication (single-user local app)
- ❌ No database (JSON file is sufficient)

### Acceptance Tests
1. **Empty state**: Run `status` with no data.json → `{"total_hours": 0, "topics": []}`
2. **Track session**: Run `track python 2.5` → data.json created/updated with entry
3. **Invalid hours**: Run `track python -1` → Error: "Hours must be positive"
4. **Status after tracking**: Track 2 sessions → `status` shows correct totals
5. **Recommend logic**: After tracking python → `recommend` suggests related topic
6. **Export**: Run `export output.json` → Valid JSON file created
7. **Quiz generation**: Run `quiz python` → Returns 3-5 questions
8. **Missing topic**: Run `track "" 2` → Error: "Topic name required"
9. **Invalid date**: Run `track python 2 invalid-date` → Error: "Date must be YYYY-MM-DD"
10. **Help text**: Run `track --help` → Shows usage and examples
```

### Exercise: Write Your Spec

Before moving forward, write your own spec. You can:
- **Option A**: Use the Learning Assistant example above
- **Option B**: Choose a different CLI tool (task tracker, note manager, flashcard app)

**Your spec must include:**
- [ ] 3-5 commands with arguments
- [ ] Requirements section with constraints
- [ ] Non-goals section (at least 3 items)
- [ ] 8-10 acceptance tests

**Time: 10-15 minutes**

**Checkpoint:** Does your spec answer: "If I hand this to someone, could they build it without asking questions?"

---

## Section 3: Step 2 — The Scaffold Prompt

### Request Structure, Not Implementation

**Common mistake:** Asking AI to "write the code" results in a 500-line monolithic file.

**Better approach:** Request a project structure first, then implement incrementally.

### Project Structure Template

For a CLI app, a good structure is:

```
learning_assistant/
├── README.md              # Setup and usage
├── requirements.txt       # Dependencies
├── data.json             # Data file (template)
├── src/
│   ├── __init__.py
│   ├── cli.py            # Argparse entrypoint
│   ├── commands.py       # Command implementations
│   ├── storage.py        # Data persistence
│   └── schemas.py        # JSON schemas
└── tests/
    ├── __init__.py
    ├── test_commands.py  # Command tests
    ├── test_storage.py   # Storage tests
    └── fixtures/
        └── sample_data.json
```

### The Scaffold Prompt

**Goal:** Get AI to create this structure with minimal stubs, not full implementations.

**Example prompt:**

```
Using the spec above, create a Python CLI project with this structure:

learning_assistant/
├── README.md (setup instructions + usage examples)
├── requirements.txt (argparse, jsonschema, pytest)
├── data.json (empty template: {"sessions": [], "stats": {}})
├── src/
│   ├── __init__.py (empty)
│   ├── cli.py (argparse setup with 5 subcommands)
│   ├── commands.py (stub functions for each command)
│   ├── storage.py (load_data() and save_data() stubs)
│   └── schemas.py (JSON schema definitions)
└── tests/
    ├── __init__.py (empty)
    ├── test_commands.py (empty test functions with docstrings)
    └── fixtures/
        └── sample_data.json (example data for tests)

Requirements:
1. Generate ONLY the file structure and minimal stubs
2. Do NOT implement full command logic yet
3. Add TODO comments where logic goes
4. Include docstrings explaining each function's purpose
5. cli.py should parse arguments and call command functions
6. Keep each function under 10 lines (stubs only)
```

### What This Prompt Does

**Explicit constraints:**
- "ONLY the file structure" → prevents over-implementation
- "minimal stubs" → keeps it simple
- "TODO comments" → marks where you'll iterate later
- "under 10 lines" → forces AI to stay minimal

**Why this works:**
- You get a runnable skeleton
- Files are organized logically
- Easy to verify structure without reading 500 lines
- Sets you up for incremental iteration

### Example Scaffold Output

After running this prompt, you should get:

**src/cli.py:**
```python
import argparse
from commands import track_session, get_status, get_recommendation, generate_quiz, export_data

def main():
    parser = argparse.ArgumentParser(description="Learning Assistant CLI")
    subparsers = parser.add_subparsers(dest='command')
    
    # track command
    track_parser = subparsers.add_parser('track', help='Log study session')
    track_parser.add_argument('topic', help='Study topic')
    track_parser.add_argument('hours', type=float, help='Hours spent')
    track_parser.add_argument('--date', help='Date (YYYY-MM-DD)')
    
    # status command
    subparsers.add_parser('status', help='Show progress as JSON')
    
    # TODO: Add recommend, quiz, export parsers
    
    args = parser.parse_args()
    
    # TODO: Route to command functions
    
if __name__ == '__main__':
    main()
```

**src/commands.py:**
```python
def track_session(topic, hours, date=None):
    """Log a study session to data.json."""
    # TODO: Validate inputs
    # TODO: Load current data
    # TODO: Append new session
    # TODO: Save data
    pass

def get_status():
    """Return progress statistics as JSON."""
    # TODO: Load data
    # TODO: Calculate total hours
    # TODO: Return JSON string
    pass

# TODO: Implement get_recommendation, generate_quiz, export_data
```

**src/storage.py:**
```python
import json

DATA_FILE = 'data.json'

def load_data():
    """Load data from data.json."""
    # TODO: Handle missing file
    # TODO: Parse JSON
    pass

def save_data(data):
    """Save data to data.json."""
    # TODO: Write JSON with formatting
    pass
```

### Verifying the Scaffold

**Checkpoint questions:**
- [ ] Are all files created?
- [ ] Does the project structure make sense?
- [ ] Are functions stubbed (not fully implemented)?
- [ ] Do docstrings explain what each part does?
- [ ] Can you see where each command will be implemented?

If yes to all → move to Step 3 (Test Generation).

If no → refine your scaffold prompt with more constraints.

### Exercise: Generate Your Scaffold

**Task:** Use your spec from Step 1 to generate a project scaffold.

**Prompt template:**
```
Using my spec, create a [PROJECT_NAME] CLI with this structure:
[paste structure template]

Requirements:
- Generate file structure with minimal stubs
- Do NOT implement full logic
- Add TODO comments
- Include docstrings
- Keep functions under 10 lines
```

**Time: 10 minutes**

**Deliverable:** A project folder with stubbed files

---

## Section 4: Step 3 — The Test Prompt

### Tests as Executable Specs

Your acceptance tests from Step 1 become pytest test functions. Instead of implementing features first and testing later, **generate tests first**. This gives you:
- Clear targets (what counts as "done")
- Immediate feedback (tests fail until implementation is correct)
- Precise prompts (failing tests tell AI exactly what to fix)

### Anatomy of a Good Test

A good test has:
1. **Descriptive name**: `test_track_session_creates_entry` (not `test1`)
2. **Docstring**: Explains what behavior is being tested
3. **Arrange-Act-Assert structure**: Setup → Execute → Verify
4. **Single concern**: Tests one thing, not multiple features

**Example:**
```python
def test_status_empty_data():
    """
    Given: No existing data.json file
    When: User runs 'status' command
    Then: Returns {"total_hours": 0, "topics": []}
    """
    # Arrange: Clean state
    if os.path.exists('data.json'):
        os.remove('data.json')
    
    # Act: Run status command
    result = get_status()
    
    # Assert: Check output
    assert result == '{"total_hours": 0, "topics": []}'
```

### The Test Generation Prompt

**Goal:** Convert your acceptance tests into pytest functions.

**Example prompt:**
```
Using the acceptance tests from my spec, generate pytest test functions for the Learning Assistant CLI.

Test file: tests/test_commands.py

Requirements:
1. One test function per acceptance test
2. Use descriptive names (test_<feature>_<scenario>)
3. Include Given-When-Then docstrings
4. Use Arrange-Act-Assert structure
5. Import necessary modules (json, os, pytest)
6. Create fixture for sample data (tests/fixtures/sample_data.json)
7. Add parametrize for edge cases where applicable

Generate tests for:
- test_status_empty_data()
- test_track_session_creates_entry()
- test_track_session_invalid_hours()
- test_status_after_tracking()
- test_recommend_logic()
- test_export_creates_file()
- test_quiz_generation()
- test_track_empty_topic_name()
- test_track_invalid_date_format()
- test_help_text_available()
```

### Example Test Output

**tests/test_commands.py:**
```python
import pytest
import json
import os
from datetime import date
from src.commands import track_session, get_status, get_recommendation, generate_quiz, export_data
from src.storage import load_data, save_data

@pytest.fixture
def clean_data_file():
    """Ensure clean state before each test."""
    if os.path.exists('data.json'):
        os.remove('data.json')
    yield
    if os.path.exists('data.json'):
        os.remove('data.json')

@pytest.fixture
def sample_data():
    """Sample data for testing."""
    return {
        "sessions": [
            {"topic": "python", "hours": 2.5, "date": "2024-03-15"},
            {"topic": "javascript", "hours": 1.5, "date": "2024-03-16"}
        ]
    }

def test_status_empty_data(clean_data_file):
    """
    Given: No existing data.json file
    When: User runs 'status' command
    Then: Returns {"total_hours": 0, "topics": []}
    """
    result = get_status()
    expected = {"total_hours": 0, "topics": []}
    assert json.loads(result) == expected

def test_track_session_creates_entry(clean_data_file):
    """
    Given: Clean data file
    When: User tracks a session with valid inputs
    Then: data.json is created with the session entry
    """
    track_session("python", 2.5)
    
    data = load_data()
    assert len(data["sessions"]) == 1
    assert data["sessions"][0]["topic"] == "python"
    assert data["sessions"][0]["hours"] == 2.5

@pytest.mark.parametrize("hours", [-1, 0, -10.5])
def test_track_session_invalid_hours(clean_data_file, hours):
    """
    Given: User provides negative or zero hours
    When: track_session is called
    Then: Raises ValueError with helpful message
    """
    with pytest.raises(ValueError, match="Hours must be positive"):
        track_session("python", hours)

def test_status_after_tracking(clean_data_file):
    """
    Given: Two sessions tracked
    When: User runs 'status'
    Then: Returns correct total hours and topic breakdown
    """
    track_session("python", 2.5)
    track_session("javascript", 1.5)
    
    result = json.loads(get_status())
    assert result["total_hours"] == 4.0
    assert len(result["topics"]) == 2

def test_track_empty_topic_name(clean_data_file):
    """
    Given: User provides empty string as topic
    When: track_session is called
    Then: Raises ValueError
    """
    with pytest.raises(ValueError, match="Topic name required"):
        track_session("", 2.0)

# TODO: Implement remaining tests
```

### Running Tests (Expecting Failures)

After generating tests, run them:

```bash
$ pytest tests/test_commands.py -v
```

**Expected output:**
```
test_status_empty_data FAILED
test_track_session_creates_entry FAILED
test_track_session_invalid_hours FAILED
...
```

**This is good!** Failing tests mean:
1. Your tests work (they can detect unimplemented features)
2. You have clear targets for Step 4 (patch loop)
3. You know exactly what to prompt AI to fix

### Exercise: Generate Your Tests

**Task:** Generate pytest tests for your spec.

**Checklist:**
- [ ] One test per acceptance test
- [ ] Fixtures for clean state and sample data
- [ ] Descriptive names and docstrings
- [ ] Parametrize for similar edge cases
- [ ] All tests fail initially (expected)

**Time: 15 minutes**

---

## Section 5: Step 4 — The Patch Loop

### Using Test Failures as Prompts

This is where vibe coding shines. Instead of vague "make it work" requests, you give AI **precise, objective feedback**: a failing test.

**The pattern:**
1. Run tests → Get failure
2. Copy test code + traceback
3. Prompt AI: "Fix this specific failure with minimal changes"
4. Apply fix
5. Run tests again → Verify
6. Repeat for next failure

### Anatomy of a Patch Prompt

**Bad patch prompt:**
```
Fix the code
```

**Good patch prompt:**
```
This test is failing:

[paste test code]

Traceback:
[paste full traceback]

Fix the `get_status()` function in src/commands.py to:
1. Handle missing data.json file (return empty structure)
2. Return valid JSON string (not a dict)
3. Keep changes minimal (< 15 lines)
4. Do NOT modify other functions
```

### Example: Patch Round 1

**Failing test:**
```python
def test_status_empty_data(clean_data_file):
    result = get_status()
    expected = {"total_hours": 0, "topics": []}
    assert json.loads(result) == expected
```

**Traceback:**
```
E   FileNotFoundError: [Errno 2] No such file or directory: 'data.json'
```

**Patch prompt:**
```
This test is failing because get_status() tries to load data.json which doesn't exist.

Test code:
def test_status_empty_data(clean_data_file):
    result = get_status()
    expected = {"total_hours": 0, "topics": []}
    assert json.loads(result) == expected

Error:
FileNotFoundError: [Errno 2] No such file or directory: 'data.json'

Fix src/commands.py get_status() to:
1. Check if data.json exists before loading
2. If missing, return '{"total_hours": 0, "topics": []}'
3. If exists, load and calculate totals
4. Return JSON string (not dict)
5. Keep changes under 10 lines
```

**AI output:**
```python
def get_status():
    """Return progress statistics as JSON."""
    if not os.path.exists('data.json'):
        return '{"total_hours": 0, "topics": []}'
    
    data = load_data()
    total_hours = sum(session['hours'] for session in data.get('sessions', []))
    topics = list({session['topic'] for session in data.get('sessions', [])})
    
    return json.dumps({"total_hours": total_hours, "topics": topics})
```

**Verify:**
```bash
$ pytest tests/test_commands.py::test_status_empty_data -v
test_status_empty_data PASSED ✓
```

### Example: Patch Round 2

**Failing test:**
```python
def test_track_session_invalid_hours(clean_data_file, hours=-1):
    with pytest.raises(ValueError, match="Hours must be positive"):
        track_session("python", hours)
```

**Traceback:**
```
E   Failed: DID NOT RAISE <class 'ValueError'>
```

**Patch prompt:**
```
Test expects ValueError when hours are negative, but function doesn't validate.

Test code:
def test_track_session_invalid_hours(clean_data_file):
    with pytest.raises(ValueError, match="Hours must be positive"):
        track_session("python", -1)

Error: Test expected ValueError but none was raised

Fix src/commands.py track_session() to:
1. Add input validation at the start
2. Raise ValueError if hours <= 0
3. Include message "Hours must be positive"
4. Do NOT change the rest of the function logic
5. Keep changes under 5 lines
```

**AI output:**
```python
def track_session(topic, hours, date=None):
    """Log a study session to data.json."""
    # Validation
    if not topic or topic.strip() == "":
        raise ValueError("Topic name required")
    if hours <= 0:
        raise ValueError("Hours must be positive")
    
    # Rest of implementation...
```

**Verify:**
```bash
$ pytest tests/test_commands.py::test_track_session_invalid_hours -v
test_track_session_invalid_hours PASSED ✓
```

### Patch Loop Best Practices

**1. One failure at a time**
Don't try to fix 10 tests at once. Fix one, verify, move to next.

**2. Request minimal changes**
Explicitly say "under 10 lines" or "modify only this function"

**3. Always verify**
Run the specific test after each fix before moving on

**4. Keep context small**
Paste only the relevant test + error, not your entire codebase

**5. Log your iterations**
Document each prompt → fix → verify cycle in your AI log

### Exercise: Complete 3 Patch Rounds

**Task:** Fix 3 failing tests using the patch loop.

**Required documentation:**
For each round, log:
- Test name
- Error/traceback
- Prompt you used
- AI's fix
- Verification result (pass/fail)

**Time: 20-30 minutes**

---

## Section 6: Step 5 — Review and Refactor

### AI-Assisted Code Review

Once your tests pass, use AI to review the code for issues you might have missed. This is **not** about rewriting everything—it's about catching specific problems.

### The Review Prompt

**Goal:** Get a checklist of potential issues, not vague "make it better" advice.

**Example prompt:**
```
Review the Learning Assistant CLI codebase for the following issues.
Provide a numbered checklist with specific line numbers/functions.

Focus areas:
1. **Security**: 
   - Are file paths validated?
   - Any injection risks in user inputs?
   - Safe JSON parsing?

2. **Error Handling**:
   - Do all commands have try/except?
   - Are error messages user-friendly?
   - Are exceptions logged?

3. **Configuration**:
   - Are file paths hardcoded? Should they be configurable?
   - Any magic numbers that should be constants?

4. **Code Quality**:
   - Any duplicate logic?
   - Functions too long (> 30 lines)?
   - Missing docstrings?

Codebase:
[paste src/cli.py, src/commands.py, src/storage.py]

Provide checklist format:
- [Category] Issue description (file:function:line)
```

### Example Review Output

**AI checklist:**
```
Security Issues:
1. [Security] File path in export_data() not validated - user can write anywhere (commands.py:export_data:45)
2. [Security] No input sanitization for topic names - could contain special characters (commands.py:track_session:12)

Error Handling:
3. [Error] load_data() doesn't handle malformed JSON (storage.py:load_data:8)
4. [Error] Generic exception in track_session - too broad (commands.py:track_session:20)

Configuration:
5. [Config] Hardcoded 'data.json' path should be constant or env var (storage.py:5, commands.py:15)
6. [Config] No logging configured - hard to debug issues (all files)

Code Quality:
7. [Quality] Duplicate JSON loading logic in commands.py (lines 15, 28, 42)
8. [Quality] get_recommendation() function is 45 lines - split into helper functions (commands.py:60-105)
```

### Applying Fixes One at a Time

**Don't fix everything at once.** Pick high-priority items and fix incrementally.

**Example: Fix #5 (hardcoded path)**

**Refactor prompt:**
```
Issue: Hardcoded 'data.json' path in storage.py and commands.py

Fix:
1. Add DATA_FILE constant in src/storage.py
2. Replace all 'data.json' strings with DATA_FILE
3. Add environment variable support (default to 'data.json')
4. Update imports in commands.py

Keep changes minimal. Do NOT refactor other logic.
```

**Verify after each fix:**
```bash
$ pytest tests/  # All tests should still pass
```

### When to Stop Refactoring

**Stop when:**
- All high-priority issues are fixed
- Tests still pass
- Code is readable and maintainable

**Don't:**
- Over-engineer (adding unnecessary abstractions)
- Break working code for "cleanliness"
- Spend hours on micro-optimizations

### Exercise: Review and Fix 3 Issues

**Task:** Get AI review, pick 3 issues, fix them.

**Required:**
- [ ] Run AI review prompt
- [ ] Prioritize issues (security > errors > config > style)
- [ ] Fix 3 issues (one at a time)
- [ ] Run tests after each fix
- [ ] Document in AI log

**Time: 20 minutes**

---

## Section 7: The AI Collaboration Log

### Why Document Your Workflow

The AI collaboration log is **not busywork**—it's proof that you:
1. Used AI strategically (not just copy-paste)
2. Iterated based on feedback (tests, reviews)
3. Made thoughtful decisions (what to accept, what to modify)

It's also a learning tool: reviewing your log shows you which prompts worked and which didn't.

### What to Include

**For each major step (Spec, Scaffold, Test, Patch rounds, Review):**
1. **Prompt** you gave AI (verbatim)
2. **Output** AI generated (code snippets or summaries)
3. **Verification** how you tested/checked it
4. **Changes** what you modified or rejected

### Log Template

**File: `ai_log.md`**

```markdown
# AI Collaboration Log - Learning Assistant CLI

## Step 1: Spec Prompt
**Date:** 2024-03-15

**Prompt:**
[paste your spec prompt]

**Output:**
Generated spec with 5 commands, 10 acceptance tests

**Verification:**
Reviewed spec - clear and specific enough for implementation

**Changes:**
Added 2 more edge cases to acceptance tests

---

## Step 2: Scaffold Prompt
**Date:** 2024-03-15

**Prompt:**
[paste scaffold prompt]

**Output:**
```
learning_assistant/
├── README.md
├── src/
│   ├── cli.py (25 lines)
│   ├── commands.py (40 lines, stubs)
│   ├── storage.py (15 lines, stubs)
```

**Verification:**
- All files created ✓
- Functions are stubs (not full implementations) ✓
- Structure matches template ✓

**Changes:**
- Added schemas.py manually (AI forgot it)
- Fixed import statement in cli.py (had syntax error)

---

## Step 3: Test Generation
**Date:** 2024-03-15

**Prompt:**
[paste test generation prompt]

**Output:**
Generated 8 test functions with fixtures

**Verification:**
```bash
$ pytest tests/ -v
8 failed (expected)
```

**Changes:**
- Fixed parametrize syntax in test_track_invalid_hours
- Added missing import for pytest

---

## Step 4: Patch Loop

### Round 1: test_status_empty_data
**Prompt:**
[paste patch prompt with test + traceback]

**AI Fix:**
```python
def get_status():
    if not os.path.exists('data.json'):
        return '{"total_hours": 0, "topics": []}'
    # ...
```

**Verification:**
```bash
$ pytest tests/test_commands.py::test_status_empty_data
PASSED ✓
```

**Changes:**
Accepted as-is

### Round 2: test_track_session_invalid_hours
[repeat structure]

---

## Step 5: Review and Refactor

**Review Prompt:**
[paste review prompt]

**AI Checklist:**
1. [Security] File path validation missing
2. [Error] Malformed JSON handling
3. [Config] Hardcoded paths
...

**Fixes Applied:**
1. Issue #1 - Added path validation in export_data()
2. Issue #3 - Created DATA_FILE constant
3. Issue #5 - Added try/except in load_data()

**Verification:**
All tests still pass after refactoring

---

## Final Stats
- Total prompts: 12
- AI-generated lines kept as-is: ~60%
- Modified after AI generation: ~30%
- Written manually: ~10%
- Test coverage: 95%
- Time spent: 3.5 hours
```

### Exercise: Complete Your AI Log

**Task:** Document your entire workflow.

**Sections required:**
- [ ] Spec prompt
- [ ] Scaffold prompt
- [ ] Test generation
- [ ] 3+ patch rounds
- [ ] Review cycle
- [ ] Final stats

**Time: 15 minutes**

---

## Section 8: Production Best Practices

### When NOT to Use AI

AI is powerful but not appropriate for everything.

**Avoid AI for:**
- **Security-critical code**: Authentication, encryption, access control
- **Complex algorithms**: AI can hallucinate logic errors
- **Performance-critical paths**: Hot loops, data structure design
- **Debugging state issues**: AI doesn't have runtime context

**Use AI for:**
- Boilerplate and scaffolding
- Test generation
- Documentation
- Code review checklists
- Refactoring suggestions

### Verification Culture

**Golden rule:** Never merge AI code without verification.

**Your verification checklist:**
- [ ] Tests pass (happy path + edge cases)
- [ ] Manual testing (run the CLI yourself)
- [ ] Code review (read every line AI generated)
- [ ] Security check (no injection risks, path validation)
- [ ] Performance check (no obvious inefficiencies)

### Incremental Iteration

**Philosophy:** Small, verified changes beat big rewrites.

Each AI interaction should:
1. Change < 20 lines of code
2. Have a clear verification step
3. Not break existing tests
4. Be documented in your AI log

**Anti-pattern:** "Rewrite the entire app to be better"
**Better:** "Extract duplicate logic in lines 15, 28, 42 into a helper function"

### Code Review Checklist

Use this for human or AI review:

**Security:**
- [ ] User inputs are validated before use
- [ ] File paths are validated (no arbitrary writes)
- [ ] No SQL injection risks (if using databases)
- [ ] Secrets not hardcoded

**Error Handling:**
- [ ] All external calls wrapped in try/except
- [ ] Error messages are user-friendly
- [ ] Errors are logged for debugging

**Testing:**
- [ ] All features have tests
- [ ] Tests cover edge cases and failures
- [ ] Tests run fast (< 5 seconds total)

**Code Quality:**
- [ ] Functions under 30 lines
- [ ] Clear names (no `foo`, `temp`, `data2`)
- [ ] Docstrings on all public functions
- [ ] No duplicate logic

---

## Appendix: Prompt Engineering Concepts (Optional Reading)

This section covers traditional prompt engineering concepts briefly. These are useful background knowledge but not required for the vibe coding workshop.

### System Prompts and Role Design

**What:** A system prompt defines the AI's behavior, tone, and constraints before any user input.

**Example:**
```
You are a senior Python developer reviewing code for security issues.
Focus on: input validation, SQL injection, path traversal.
Output format: Numbered list with file:line references.
```

**When useful:** When you need consistent behavior across many AI interactions.

### Few-Shot Learning

**What:** Providing 2-5 examples of desired input/output pairs to show the pattern.

**Example:**
```
Convert these function names to snake_case:

getUserData → get_user_data
calculateTotalPrice → calculate_total_price
isValidEmail → is_valid_email

Now convert: fetchAPIResponse →
```

**When useful:** Complex formatting or domain-specific transformations.

### Parameter Tuning (Temperature, Top_p)

**Temperature (0.0 - 2.0):**
- **0.0-0.3**: Deterministic, consistent (good for code, data extraction)
- **0.5-0.8**: Balanced creativity
- **1.0+**: High creativity, less reliable

**Top_p (0.0 - 1.0):**
- Controls diversity by limiting token choices
- Usually set to 0.9-1.0 and tune temperature instead

**For vibe coding:** Use temperature 0.1-0.3 for code generation.

### Structured Outputs and Validation

**What:** Requesting AI output in a specific format (JSON, YAML, Markdown tables).

**Example:**
```
Return your analysis as JSON with these fields:
{
  "issues": [{"severity": "high|medium|low", "description": "..."}],
  "summary": "..."
}
```

**When useful:** When output needs to be parsed by code, not just read by humans.

---

## Next Steps

### Week 5 Preview

In Week 5, you'll add real LLM API calls to your CLI:
- Integrate OpenAI or Ollama
- Make `recommend` use actual AI logic
- Add `quiz` generation with GPT-4
- Handle API errors and rate limits

Your Week 4 CLI becomes the foundation for a real AI-powered app.

### Level 2 Connection

Level 2's "Vibe Coding & AI-Assisted Development" module expands on this workshop:
- **Larger scale:** Multi-file refactors, database migrations
- **Advanced patterns:** Agents, tool use, RAG integration
- **Production focus:** CI/CD for AI-generated code, monitoring
- **Quality at scale:** Automated reviews, regression detection

### Resources

**Tools:**
- **Cursor**: AI-first code editor (cursor.sh)
- **GitHub Copilot**: AI pair programmer
- **Windsurf**: AI coding assistant

**Further Reading:**
- *Building LLM Apps* by Google: Prompt engineering patterns
- *The Pragmatic Programmer*: General software craft (applies to AI-assisted work)
- OpenAI Cookbook: Advanced prompting techniques

---

## Summary

You've learned the **5-step vibe coding loop**:

1. **Spec** → Define requirements, constraints, acceptance tests
2. **Scaffold** → Request minimal project structure
3. **Test** → Generate pytest tests from spec
4. **Patch** → Iterate with failing tests as prompts
5. **Review** → AI-assisted code review + refactors

**Key takeaways:**
- Prompting is learned by doing, not theory
- Constraints and acceptance tests guide AI output
- Tests drive iteration (fail → fix → verify)
- Always verify AI output (never trust blindly)
- Document your workflow in an AI collaboration log

**What makes this different from just "using AI":**
- You control the process (not AI)
- Every output is verified (tests, review, manual checks)
- Incremental changes (not big rewrites)
- Documented workflow (shows learning and judgment)

**For your Week 4 deliverable:**
- Working CLI with 3-5 commands
- Comprehensive test coverage
- AI collaboration log
- Clean, reviewed code

This workflow applies to any coding project, not just CLIs. Use it for web apps, data pipelines, automation scripts—anywhere you want AI to accelerate development while maintaining quality.

---

**End of Part 2: Vibe Coding Workshop**
