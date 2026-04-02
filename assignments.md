# Fundamentals of AI Engineering: Assignments & Assessment

## Overview

This 6-week course uses a progressive assessment structure that builds from tool exploration to hands-on programming practice, culminating in a complete LLM application project.

| Component | Weight | Week Due |
|-----------|--------|----------|
| Week 1: Agent Tools Experience Report | 10% | Week 1 |
| Week 2: AI-Assisted Programming Practice Report | 10% | Week 2 |
| Week 3: Local Inference & API Engineering Report | 15% | Week 3 |
| Week 4: Data Profiling Report | 10% | Week 4 |
| Week 5: ML Experiment Comparison Report | 10% | Week 5 |
| Week 6: LLM Application Project | 25% | Week 6 |
| Participation | 20% | Ongoing |
| **Total** | **100%** | |

---

## Submission Guidelines

All submissions must follow this structure for consistency and ease of grading:

### Required Submission Structure

```
submission-weekN/
├── README.md                 # How to run, what to expect
├── requirements.txt          # Python dependencies
├── src/                      # Source code
├── tests/                    # Unit tests (even if minimal)
├── output/                   # Sample outputs
└── report.md                 # Your written report
```

### README.md Requirements

Your README must include:

*   **Environment setup**: Python version, how to install dependencies
*   **How to run**: Exact commands to reproduce your work
*   **Expected outputs**: What the reader should see
*   **Failure case notes**: At least one pitfall you encountered and how you fixed it

### Definition of Done Checklist

Before submitting, verify:

*   [ ] A clean run works on a new machine after following your README
*   [ ] Inputs/outputs are explicit (paths, formats, schemas documented)
*   [ ] Errors are readable (not just stack traces without context)
*   [ ] At least one failure case is documented with the fix
*   [ ] All code runs without modification on instructor's test environment

### Submission Format

*   **Preferred**: GitHub repository link
*   **Alternative**: Zipped folder uploaded to the course LMS
*   **Naming**: `submission-weekN-[your-name].zip` or repository named `ai-eng-weekN-[your-name]`

---

## Academic Integrity & AI Tool Usage Policy

### AI Tool Usage Declaration

This course explicitly encourages the use of AI tools (LLMs, code assistants, etc.) as part of the learning process. However, **full transparency is required**:

*   **You must declare** which AI tools you used for each assignment
*   **Document prompts**: Include representative prompts that were key to your solution
*   **Annotate AI-generated sections**: Clearly mark which parts of your code/report were AI-assisted
*   **Explain your understanding**: For AI-generated code, add comments explaining how it works

**Example declaration format:**

```markdown
## AI Tool Declaration

*   **Tool used**: Claude (Anthropic) via web interface
*   **Key prompts**:
    *   "Explain how to implement retry logic with exponential backoff in Python"
    *   "Review this function for error handling issues: [code]"
*   **AI-assisted sections**:
    *   Lines 15-30 in `client.py`: retry logic implementation
    *   Section 3 of report.md: summary of inference approaches
*   **My contributions**: Problem decomposition, testing strategy, integration, debugging
```

### Academic Integrity Guidelines

*   **Allowed**: Using AI tools to learn, generate starting points, debug, and explain concepts
*   **Allowed**: Collaborating with classmates on concepts and approaches
*   **Not allowed**: Submitting work you do not understand
*   **Not allowed**: Copying solutions from classmates without attribution
*   **Not allowed**: Using solutions from previous course offerings

Violations will be handled according to institutional academic integrity policies.

---

## Late Submission Policy

| Submission Time | Penalty |
|-----------------|---------|
| On time | No penalty |
| Up to 24 hours late | -10% |
| 24-48 hours late | -20% |
| 48-72 hours late | -30% |
| More than 72 hours late | Not accepted without prior arrangement |

**Extensions**: Requests for extensions must be made at least 48 hours before the deadline and require documentation (illness, family emergency, etc.).

---

## How to Get Help

### Before Asking

1.  Check the course [README.md](README.md) for common issues
2.  Review your error message carefully—often the solution is in the output
3.  Search the course discussion forum for similar questions

### Required Information for Help Requests

When requesting help (via office hours, discussion forum, or email), include:

*   **The exact command you ran** + **full output** (as text, not screenshots)
*   **Your OS and Python version**: `python --version` and `uname -a` or `ver`
*   **A minimal code snippet** that reproduces the problem
*   **What you already tried** and what happened

### Help Channels

*   **Discussion Forum**: Post questions here first (allows peer learning)
*   **Office Hours**: Schedule via course calendar
*   **Email**: For private matters only; include "[AI-ENG]" in subject

---

## Assignment Details

---

### Week 1: Agent Tools Experience Report (10%)

**Deadline**: End of Week 1 (Sunday 11:59 PM)

#### Goal/Objective

Explore and evaluate AI agent tools (such as Kilo, Cursor, Claude Code, or similar) to understand their capabilities, limitations, and effective usage patterns for software engineering tasks.

#### Requirements

1.  **Select and install** one or more AI agent tools
2.  **Complete at least 3 hands-on tasks** using the tool:
    *   Task 1: Code generation (e.g., write a utility function)
    *   Task 2: Code review/debugging (e.g., fix a provided buggy script)
    *   Task 3: Refactoring or documentation (e.g., improve code structure)
3.  **Document your experience** including successes, failures, and surprises
4.  **Compare**: How does this tool differ from simple chat interfaces?

#### Deliverables

| File | Description |
|------|-------------|
| `report.md` | 2-3 page experience report with structured sections |
| `src/` | Code files created or modified during your exploration |
| `output/screenshots/` | Screenshots demonstrating tool interactions |
| `README.md` | Setup instructions for anyone wanting to reproduce |

#### Assessment Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Tool exploration depth | 25% | Demonstrated thorough exploration of capabilities |
| Task completion | 25% | All 3 tasks completed with evidence |
| Critical analysis | 30% | Thoughtful evaluation of strengths/weaknesses |
| Documentation quality | 15% | Clear, well-organized report |
| AI declaration | 5% | Proper attribution of AI assistance |

#### Report Structure

Your `report.md` should include:

1.  **Tool Overview**: What you chose and why
2.  **Setup Experience**: Installation and configuration notes
3.  **Task Descriptions**: What you attempted and how
4.  **Results**: What worked, what didn't
5.  **Reflection**: Key learnings about effective AI collaboration
6.  **Comparison**: How agent tools differ from other AI interfaces

---

### Week 2: AI-Assisted Programming Practice Report (10%)

**Deadline**: End of Week 2 (Sunday 11:59 PM)

#### Goal/Objective

Develop practical skills in AI-assisted programming by completing a non-trivial coding task using LLM assistance strategically, while maintaining code quality and understanding.

#### Requirements

1.  **Select a programming challenge** from the provided list or propose your own (requires approval)
2.  **Implement the solution** using AI assistance throughout the process
3.  **Document your workflow**: How you structured prompts, iterated, and validated
4.  **Include tests**: Unit tests for your implementation
5.  **Reflect on the process**: What patterns made AI assistance effective or ineffective

**Suggested Challenge Options**:

*   Build a CLI tool that processes CSV files with configurable transformations
*   Create a web scraper with rate limiting and error handling
*   Implement a simple API client with authentication and retry logic
*   Build a data pipeline that reads, transforms, and validates data

#### Deliverables

| File | Description |
|------|-------------|
| `report.md` | 2-3 page report on your AI-assisted development process |
| `src/` | Complete, working implementation |
| `tests/` | Unit tests with reasonable coverage |
| `README.md` | Usage instructions |
| `prompts.md` | Log of key prompts used (for transparency) |

#### Assessment Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Code functionality | 25% | Solution works correctly for intended use case |
| Code quality | 20% | Clean, readable, well-structured code |
| Test coverage | 15% | Tests exist and verify key functionality |
| Process documentation | 25% | Clear explanation of AI collaboration approach |
| Reflection quality | 10% | Thoughtful insights on effective patterns |
| AI declaration | 5% | Proper attribution and prompt documentation |

---

### Week 3: Local Inference & API Engineering Report (15%)

**Deadline**: End of Week 3 (Sunday 11:59 PM)

#### Goal/Objective

Build practical skills in setting up local inference (Ollama) and designing robust API clients for LLM services, understanding trade-offs between local and cloud-based approaches.

#### Requirements

1.  **Set up Ollama** locally and run at least 2 different models
2.  **Build an LLM client module** (`llm_client.py`) with:
    *   Timeout handling
    *   Retry logic with exponential backoff
    *   Error handling and graceful degradation
    *   Basic caching mechanism
    *   Logging of requests/responses
3.  **Compare local vs. API inference**:
    *   Test the same prompts on local (Ollama) and cloud (OpenAI/Anthropic) models
    *   Measure and document latency differences
    *   Evaluate output quality on a small benchmark
4.  **Write a comparison report** analyzing trade-offs

#### Deliverables

| File | Description |
|------|-------------|
| `src/llm_client.py` | Production-minded LLM client implementation |
| `src/benchmark.py` | Script to run comparison tests |
| `report.md` | Detailed comparison report (3-4 pages) |
| `output/benchmark_results.json` | Structured results from your tests |
| `tests/test_llm_client.py` | Unit tests for client functionality |
| `README.md` | Setup and usage instructions |

#### Assessment Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Client implementation | 25% | Robust, well-engineered client with all required features |
| Test quality | 15% | Comprehensive tests including failure simulation |
| Comparison methodology | 15% | Systematic approach to comparing local vs. cloud |
| Analysis depth | 25% | Thoughtful analysis of trade-offs and use cases |
| Documentation | 10% | Clear setup instructions and findings |
| AI declaration | 5% | Proper attribution of AI assistance |
| Code quality | 5% | Clean, maintainable code |

#### Report Requirements

Your comparison report must address:

1.  **Setup complexity**: What was required for each approach
2.  **Performance**: Latency, throughput, resource usage
3.  **Quality**: Output comparison on your test tasks
4.  **Cost**: Direct and indirect costs
5.  **Best-fit scenarios**: When to use each approach
6.  **Risks and limitations**: What can go wrong with each

---

### Week 4: Data Profiling Report (10%)

**Deadline**: End of Week 4 (Sunday 11:59 PM)

#### Goal/Objective

Apply data profiling techniques using both traditional tools (Pandas) and AI-assisted approaches to understand datasets and communicate findings effectively.

#### Requirements

1.  **Select a dataset** (minimum 1000 rows, 5 columns) or use the provided dataset
2.  **Implement a data profiling script** that generates:
    *   Missing value statistics
    *   Numeric column distributions (mean, median, std, percentiles)
    *   Categorical column value counts
    *   Anomaly detection (your own rules or statistical methods)
    *   Correlation analysis for numeric columns
3.  **Use AI assistance** strategically for:
    *   Generating profiling code structure
    *   Interpreting results
    *   Suggesting visualizations
4.  **Produce a summary report** with key findings and recommendations

#### Deliverables

| File | Description |
|------|-------------|
| `src/profiler.py` | Data profiling script |
| `output/profile_report.html` or `.md` | Generated profiling report |
| `report.md` | Written analysis and recommendations (2 pages) |
| `data/` | Dataset used (or link if too large) |
| `README.md` | How to run the profiler |
| `requirements.txt` | Dependencies |

#### Assessment Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Profiler functionality | 25% | Script runs successfully, produces all required outputs |
| Analysis completeness | 25% | All required statistics and metrics included |
| Insight quality | 20% | Meaningful observations and recommendations |
| Report clarity | 15% | Clear, well-structured findings |
| Code quality | 10% | Clean, documented code |
| AI declaration | 5% | Proper attribution |

---

### Week 5: ML Experiment Comparison Report (10%)

**Deadline**: End of Week 5 (Sunday 11:59 PM)

#### Goal/Objective

Design, execute, and compare machine learning experiments to understand how different approaches affect model performance, using both traditional ML and AI-assisted analysis.

#### Requirements

1.  **Select a dataset** suitable for classification or regression
2.  **Design at least 2 comparative experiments**:
    *   Experiment 1: Compare two different model types (e.g., Random Forest vs. Logistic Regression)
    *   Experiment 2: Compare two hyperparameter configurations or feature engineering approaches
3.  **Implement reproducible training pipeline** with:
    *   Train/validation/test split
    *   Cross-validation
    *   Metric tracking
    *   Model artifact saving
4.  **Run experiments** and collect results
5.  **Analyze results** including:
    *   Statistical significance of differences
    *   Failure case analysis (where did models fail?)
    *   Iteration suggestions

#### Deliverables

| File | Description |
|------|-------------|
| `src/train.py` | Parameterized training script |
| `src/compare.py` | Experiment comparison and visualization |
| `output/experiments/` | Results, metrics, and model artifacts |
| `report.md` | Experiment report with findings (3-4 pages) |
| `README.md` | Reproduction instructions |
| `requirements.txt` | Dependencies |

#### Assessment Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Experiment design | 20% | Well-structured, meaningful comparisons |
| Reproducibility | 20% | Clear instructions, consistent results |
| Implementation | 20% | Clean, working training pipeline |
| Analysis depth | 25% | Thoughtful interpretation of results |
| Documentation | 10% | Clear report and README |
| AI declaration | 5% | Proper attribution |

#### Report Structure

Your report should include:

1.  **Experiment Design**: What you compared and why
2.  **Methodology**: Data splits, metrics, validation approach
3.  **Results**: Tables, charts, and key findings
4.  **Analysis**: Interpretation of what the results mean
5.  **Failure Retrospective**: One failed experiment or unexpected result and what you learned
6.  **Next Steps**: What you would try next

---

### Week 6: LLM Application Project (25%)

**Deadline**: End of Week 6 (Sunday 11:59 PM)

#### Goal/Objective

Design and build a complete LLM-powered application that demonstrates integration of concepts learned throughout the course, including structured outputs, error handling, and user interaction.

#### Requirements

1.  **Build a complete application** that:
    *   Takes user input (text, file, or API)
    *   Processes it using an LLM (local or cloud)
    *   Produces structured output (JSON schema validation)
    *   Has error handling and retry logic
    *   Includes a user interface (CLI, web, or API)

2.  **Suggested Project Ideas**:
    *   Document analyzer: Extract structured information from PDFs/documents
    *   Code review assistant: Analyze code for common issues
    *   Data transformation tool: Convert unstructured data to structured format
    *   Question-answering system: Answer questions from a knowledge base
    *   Content generator: Generate structured content from prompts

3.  **Technical Requirements**:
    *   Structured output with JSON schema
    *   Retry/repair for invalid outputs
    *   Timeout and error handling
    *   Logging for debugging
    *   Unit tests
    *   Documentation

4.  **Final Report** including:
    *   Architecture overview
    *   Design decisions and trade-offs
    *   Testing strategy
    *   Deployment considerations

#### Deliverables

| File | Description |
|------|-------------|
| `src/` | Complete application source code |
| `tests/` | Comprehensive test suite |
| `report.md` | Project report (4-6 pages) |
| `README.md` | Setup, usage, and architecture documentation |
| `requirements.txt` or `pyproject.toml` | Dependencies |
| `output/demo/` | Screenshots, demo video, or sample outputs |
| `ARCHITECTURE.md` | (Optional) Detailed design documentation |

#### Assessment Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Functionality | 25% | Application works as specified, handles edge cases |
| Code quality | 20% | Clean, maintainable, well-organized code |
| Structured output handling | 15% | Proper JSON schema, validation, retry logic |
| Error handling | 10% | Graceful failure modes, informative errors |
| Testing | 10% | Comprehensive test coverage |
| Documentation | 10% | Clear README, architecture explanation |
| Innovation/scope | 5% | Appropriate complexity and creativity |
| AI declaration | 5% | Proper attribution |

#### Project Report Structure

Your final report should include:

1.  **Executive Summary**: What you built and why
2.  **Problem Statement**: The problem your application solves
3.  **Architecture**: High-level design and component interactions
4.  **Implementation Details**: Key technical decisions
5.  **Testing Strategy**: How you verified correctness
6.  **Challenges & Solutions**: Obstacles encountered and how you resolved them
7.  **Future Work**: What you would add with more time
8.  **Reflection**: Key learnings from the project

---

## Participation (20%)

Participation is assessed throughout the course and includes:

| Component | Weight | Description |
|-----------|--------|-------------|
| In-class activities | 8% | Engagement in discussions, exercises, code reviews |
| Discussion forum | 6% | Asking questions, answering peers, sharing resources |
| Peer feedback | 4% | Providing constructive feedback on classmates' work |
| Progress check-ins | 2% | Regular updates and communication |

### In-Class Activities

*   Code walkthroughs: Explaining your approach to exercises
*   Pair programming: Collaborative problem-solving sessions
*   Discussion: Contributing to technical discussions

### Discussion Forum Expectations

*   Ask questions when stuck (after trying yourself)
*   Answer peers' questions when you can help
*   Share interesting resources or discoveries
*   Provide constructive feedback on others' project ideas

---

## Summary Timeline

| Week | Assignment | Due | Weight |
|------|------------|-----|--------|
| 1 | Agent Tools Experience Report | Sunday Week 1 | 10% |
| 2 | AI-Assisted Programming Practice Report | Sunday Week 2 | 10% |
| 3 | Local Inference & API Engineering Report | Sunday Week 3 | 15% |
| 4 | Data Profiling Report | Sunday Week 4 | 10% |
| 5 | ML Experiment Comparison Report | Sunday Week 5 | 10% |
| 6 | LLM Application Project | Sunday Week 6 | 25% |
| 1-6 | Participation | Ongoing | 20% |

---

## Questions?

If you have questions about assignments, grading, or need clarification:

1.  Check this document and the course README first
2.  Search the discussion forum for similar questions
3.  Post in the discussion forum for general questions
4.  Attend office hours for detailed discussions
5.  Email for private matters (include "[AI-ENG]" in subject)
