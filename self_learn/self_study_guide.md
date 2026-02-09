# Self-learn Self-Study Guide

**Target Audience:** Complete beginners to AI engineering with little to no programming experience  
**Duration:** 8 weeks (flexible pacing)  
**Time Commitment:** 8-12 hours per week

---

## How to Use This Guide

This guide provides **step-by-step navigation** through the Self-learn curriculum. It tells you:
- **What to read** each week (chapter sections)
- **Where to practice** (specific Jupyter notebooks and labs)
- **How to verify** you're ready to move forward
- **What to build** as weekly proof of learning

**All coding exercises are in the chapter materials** — this guide simply shows you the path through them.

---

## Your Weekly Study Loop

Follow this pattern every week:

### 1️⃣ Read & Understand (30-40% of time)
- Read the assigned chapter sections
- Take notes on key concepts
- Don't worry if you don't understand everything — it will click when you practice

### 2️⃣ Practice & Code (50-60% of time)
- Open the chapter's Jupyter notebooks
- Run every code example yourself
- Complete all practice exercises in the notebooks
- Experiment by changing parameters and seeing what happens

### 3️⃣ Build & Verify (10-20% of time)
- Complete the weekly deliverable project
- Self-assess using the checkpoint questions
- Commit your work to Git
- Move to next week only when checkpoints pass

**Golden Rule:** Type all code yourself. No copy-paste. This is how you learn.

---

## Week 1: Development Tools and Environment Setup

**Goal:** Set up a professional development environment and learn essential tools

### 📖 What to Read
- [Chapter 1: Tool Preparation](./Chapters/1/Chapter1.md) — Read all sections
- Pay special attention to:
  - Shell/Command Line Fundamentals (you'll use this daily)
  - Git basics (version control is essential)
  - Conda environment management (avoid "it works on my machine" problems)

### 💻 Where to Practice
Complete all exercises in these Chapter 1 materials:
- `01_shell_command_line.md` — Practice file navigation, creating directories, basic commands
- `02_git_version_control.md` — Initialize repos, make commits, view history
- `04_conda_environment_management.md` — Create environments, install packages, export configs
- `05_jupyter_interactive_computing.ipynb` — Run notebook cells, understand kernels

**All coding exercises are in these files.** Work through them in order.

### ✅ Checkpoints

**Before moving to Week 2, can you do these without looking up commands?**
- [ ] Navigate directories and create files/folders using shell
- [ ] Create and activate a conda environment from scratch
- [ ] Initialize a Git repository and make meaningful commits
- [ ] Launch Jupyter and connect it to your conda environment
- [ ] Explain to someone why we need Git, Conda, and Jupyter

### 📦 Weekly Deliverable

**Build: "My Development Environment" repository**

Create a Git repository containing:
1. `README.md` — Describe your setup (OS, tools installed, versions)
2. `environment.yml` — Exported conda environment
3. `week1_practice.ipynb` — A simple notebook proving everything works
4. `.gitignore` — Exclude temporary files

**Success test:** A friend could clone your repo and recreate your exact environment.

**Time estimate:** 1-2 hours for the deliverable (after completing chapter exercises)

---

## Week 2: Python Fundamentals and Environment Management

**Goal:** Build a solid Python foundation with hands-on coding practice

### 📖 What to Read
- [Chapter 2: Python and Environment Management](./Chapters/2/Chapter2.md) — Read all parts
- This is the longest chapter. Break it into sessions:
  - **Session 1:** Python Basics - Concepts (variables, data types, control flow)
  - **Session 2:** Functions, modules, and packages
  - **Session 3:** File I/O and JSON handling
  - **Session 4:** Environment management deep dive

### 💻 Where to Practice
Complete all exercises in these Chapter 2 materials (in order):
- `01_python_fundamentals.md` — Core Python concepts
- `02_python_basics_interactive.ipynb` — **20+ coding exercises** (spend most of your time here)
- `03_conda_advanced.md` — Mixed conda/pip workflows
- `04_hands_on_labs.ipynb` — JSON processing project, debugging scenarios

**Focus on the interactive notebook** — type every exercise yourself, experiment with variations.

### ✅ Checkpoints

**Before moving to Week 3, can you do these without looking at examples?**
- [ ] Write a function that takes parameters and returns a value
- [ ] Use lists and dictionaries to store and retrieve data
- [ ] Read from and write to JSON files
- [ ] Add try/except error handling to your code
- [ ] Create and export a reproducible conda environment
- [ ] Read a Python traceback and identify the error

### 📦 Weekly Deliverable

**Build: "Study Tracker" CLI application**

Create a Python script that:
1. Tracks study sessions in a JSON file (topic, hours, date)
2. Calculates total hours and progress percentage
3. Allows adding new sessions via command line
4. Handles errors gracefully (missing file, invalid input)
5. Saves data persistently

**Success test:** 
- Run the script multiple times — data persists
- Try to break it with bad input — it recovers gracefully
- Code is clean and well-commented

**Time estimate:** 2-3 hours (apply what you learned from chapter exercises)

---

## Week 3: AI Engineering Fundamentals - Function Calling

**Goal:** Understand how to make AI systems produce structured, reliable outputs

### 📖 What to Read
- [Chapter 3: AI Engineering Fundamentals](./Chapters/3/Chapter3.md) — **Part 1 only**
- Focus: Function calling and structured outputs
- Key concepts:
  - Why structured outputs matter (consistency, validation)
  - JSON Schema basics
  - Tool/function calling patterns
  - Cross-provider compatibility

### 💻 Where to Practice
Complete exercises in these Chapter 3 Part 1 materials:
- `01_function_calling_structured_outputs.md` — Core concepts and examples
- `01_function_calling_structured_outputs.ipynb` — Hands-on exercises with schemas and validation

**The notebook contains all the coding exercises.** Work through them sequentially.

### ✅ Checkpoints

**Before moving to Week 4, can you explain these concepts?**
- [ ] What is structured output and why does it matter for AI systems?
- [ ] How does JSON Schema define data contracts?
- [ ] What is function calling in the context of LLMs?
- [ ] How do you validate structured outputs?
- [ ] Why are structured outputs more reliable than free-form text?

### 📦 Weekly Deliverable

**Build: "Learning Assistant Simulator"**

Create a Python program with:
1. 3-5 tool functions that return structured JSON (progress tracking, recommendations, etc.)
2. Input validation using schemas
3. A simple interface to select and call tools
4. Output validation to ensure responses match expected format
5. Error handling for invalid inputs

**Success test:**
- All outputs are valid JSON matching defined schemas
- Invalid inputs produce helpful error messages
- Demonstrates function calling pattern clearly

**Time estimate:** 2-3 hours

---

## Week 4: Vibe Coding Workshop — Shipping the Learning Assistant CLI

**Goal:** Transform your Week 3 simulator into a tested CLI app using AI as a pair programmer

### 📖 What to Read
- [Chapter 3: AI Engineering Fundamentals](./Chapters/3/Chapter3.md) — **Part 2 only**
- Focus: Vibe coding workflow (learn prompting by building)
- Key concepts you'll learn by doing:
  - Writing specs that constrain AI output (requirements + non-goals + acceptance tests)
  - Requesting scaffolding (structure first, implementation second)
  - Using tests to drive AI iteration (failing test → patch → verify)
  - AI-assisted code review (checklists, not rewrites)

### 💻 Where to Practice
Complete Chapter 3 Part 2 materials:
- `02_prompt_engineering_evaluation.md` — Step-by-step vibe coding workshop
- `02_prompt_engineering_evaluation_lab.ipynb` — Hands-on exercises with the 5-step loop

**The materials walk you through:**
1. Writing a feature spec (10 min)
2. Requesting project scaffolding (10 min)
3. Generating tests from the spec (15 min)
4. Patch loop: test failures → AI fixes (20 min)
5. AI-assisted review + refactor (15 min)

### ✅ Checkpoints

**Before moving to Week 5, verify you can:**
- [ ] Write a 10-line spec with requirements, non-goals, and acceptance tests
- [ ] Request a project structure (not a single-file rewrite)
- [ ] Ask AI to generate pytest tests for your spec
- [ ] Use test failures as prompts (paste traceback + request minimal fix)
- [ ] Request a code review checklist (security, errors, config, quality)
- [ ] Explain what makes a good vs bad prompt for AI pair programming

### 📦 Weekly Deliverable

**Build: "Learning Assistant CLI (Vibe-Coded)"**

Upgrade your Week 3 simulator into a CLI app with:

**Required features:**
1. CLI with 3–5 subcommands (examples: `recommend`, `track`, `status`, `quiz`, `export`)
2. Data persistence (JSON file storage)
3. At least one command outputs **strict JSON** (machine-parseable, schema-validated)
4. Input validation with helpful error messages
5. `pytest` tests (>= 5 tests, covering happy path + 3+ failure cases)
6. Project structure (separate modules: cli, commands, storage, schemas)
7. README with setup instructions and usage examples

**Required artifact:**
- **AI Collaboration Log** (`ai_log.md`) documenting:
  - Spec prompt (what constraints you gave)
  - Scaffold prompt (structure you requested)
  - 3+ test-driven patches (test failure → prompt → fix → verify)
  - 1+ review/refactor cycle (checklist → applied changes)

**Success test:**
```bash
# Fresh environment test
$ python -m venv test_env
$ source test_env/bin/activate
$ pip install -r requirements.txt
$ python -m pytest tests/  # All tests pass
$ python src/cli.py status  # Valid JSON output
$ python src/cli.py track python 2.5  # Persists data
$ python src/cli.py recommend  # Returns suggestion
```

**Evaluation criteria:**
- [ ] All commands work without crashes
- [ ] Tests pass and cover failure cases
- [ ] JSON output is schema-valid
- [ ] AI log shows clear workflow (not just "AI wrote everything")
- [ ] Code structure is clean (not a 500-line file)

**Time estimate:** 3–4 hours (mostly iteration and testing)

---

## Week 5: Model Interfaces and Cloud Deployment

**Goal:** Deploy AI models using cloud infrastructure and APIs

### 📖 What to Read
- [Chapter 3: AI Engineering Fundamentals](./Chapters/3/Chapter3.md) — **Part 3 only**
- [Chapter 4: Hugging Face Platform and Local Inference](./Chapters/4/Chapter4.md) — **Part 1 only**
- Focus: Cloud-based model deployment
- Key concepts:
  - OpenAI-compatible interfaces
  - HuggingFace Inference API
  - Authentication and API keys (security!)
  - Provider selection and failover

### 💻 Where to Practice
Complete exercises in these materials:
- `03_model_interfaces_deployment.md` — Model interface concepts
- `03_model_interfaces_deployment.ipynb` — API client practice
- `Chapter 4/01_huggingface_overview.md` — Hugging Face platform overview
- `Chapter 4/01_huggingface_inference.ipynb` — Deploy models on HF infrastructure

**Focus areas:** API authentication, retry logic, error handling, multi-provider failover.

### ✅ Checkpoints

**Before moving to Week 6, verify you can:**
- [ ] Set up API authentication securely
- [ ] Implement retry logic with exponential backoff
- [ ] Handle common API errors gracefully
- [ ] Use environment variables for configuration
- [ ] Explain the trade-offs: cloud vs local inference
- [ ] Test your code with mock APIs

### 📦 Weekly Deliverable

**Build: "Resilient AI Client Library"**

Create a Python package with:
1. Multi-provider support (OpenAI, HuggingFace, or mock)
2. Automatic retry logic with exponential backoff
3. Failover between providers
4. Secure authentication via environment variables
5. Request/response logging
6. Clean error messages

**Success test:**
- Test with at least one real API or Ollama locally
- Demonstrate failover (disable primary provider)
- All operations logged clearly
- Clean, documented API

**Time estimate:** 3-4 hours

---

## Week 6: Local Inference and Resource Management

**Goal:** Run AI models locally and monitor system resources

### 📖 What to Read
- [Chapter 4: Hugging Face Platform and Local Inference](./Chapters/4/Chapter4.md) — **Part 2 only**
- [Chapter 5: Resource Monitoring and Containerization](./Chapters/5/Chapter5.md) — **Part 1 only**
- Focus: Local model inference and system monitoring
- Key concepts:
  - Ollama setup and usage
  - vLLM for high-performance inference
  - CPU/GPU/memory monitoring
  - Performance profiling and optimization

### 💻 Where to Practice
Complete exercises in these materials:
- `Chapter 4/02_local_inference.md` — Ollama and vLLM setup guides
- `Chapter 4/02_local_inference.ipynb` — Run models locally, benchmark performance
- `Chapter 5/01_resource_monitoring.md` — Monitoring concepts
- `Chapter 5/01_resource_monitoring.ipynb` — Build monitoring tools, profile code

**Focus areas:** Installing Ollama, measuring inference speed, tracking resource usage, identifying bottlenecks.

### ✅ Checkpoints

**Before moving to Week 7, verify you can:**
- [ ] Monitor CPU, memory, and disk usage programmatically
- [ ] Install and run Ollama locally
- [ ] Benchmark inference performance
- [ ] Profile Python code performance
- [ ] Explain local vs cloud trade-offs
- [ ] Identify and diagnose resource bottlenecks

### 📦 Weekly Deliverable

**Build: "Local AI Benchmarking Suite"**

Create a benchmarking tool that:
1. Tests 2+ Ollama models with standardized prompts
2. Measures latency, throughput, memory usage
3. Monitors system resources during inference
4. Generates comparison report
5. Saves results to JSON for historical tracking

**Success test:**
- At least 2 models tested
- All key metrics captured
- Clear performance comparison generated
- Results persist for trend analysis

**Time estimate:** 3-4 hours

---

## Week 7: Containerization and Production Deployment

**Goal:** Package AI applications in Docker for reproducible deployment

### 📖 What to Read
- [Chapter 5: Resource Monitoring and Containerization](./Chapters/5/Chapter5.md) — **Part 2 only**
- Focus: Docker containerization for AI applications
- Key concepts:
  - Docker fundamentals (images, containers, Dockerfiles)
  - Multi-stage builds for smaller images
  - Docker Compose for multi-service apps
  - GPU support in containers
  - Environment-based configuration

### 💻 Where to Practice
Complete exercises in Chapter 5 Part 2 materials:
- `02_dockerization.md` — Docker concepts and best practices
- `02_dockerization.ipynb` — Hands-on containerization exercises

**The materials cover:** Writing Dockerfiles, building images, docker-compose, health checks, production deployment patterns.

### ✅ Checkpoints

**Before moving to Week 8, verify you can:**
- [ ] Write a Dockerfile from scratch
- [ ] Build and run Docker images
- [ ] Use docker-compose for multi-container apps
- [ ] Pass configuration via environment variables
- [ ] Implement health check endpoints
- [ ] Explain when to use containers vs bare metal

### 📦 Weekly Deliverable

**Build: "Production-Ready AI Service Container"**

Create a Dockerized AI service with:
1. Your AI client from Week 5 packaged in Docker
2. REST API with endpoints (generate, health, metrics, models)
3. docker-compose setup (app + Ollama)
4. Health checks and logging
5. Environment-based configuration
6. Clear README with deployment steps

**Success test:**
- Entire stack starts with one command
- Services communicate correctly
- Health checks pass
- Configuration via `.env` file works
- Someone else can deploy using your README

**Time estimate:** 4-5 hours

---

## Week 8: Capstone Project - Build Your AI Application

**Goal:** Integrate all learned concepts into a complete AI application

### Project Requirements

Build an AI-powered application that demonstrates:
1. ✅ **Development Environment** - Git, Conda, proper project structure
2. ✅ **Python Skills** - Clean code, error handling, configuration management
3. ✅ **AI Integration** - Function calling, structured outputs, validation
4. ✅ **Prompt Engineering** - Effective prompts with evaluation
5. ✅ **Deployment** - Cloud or local inference with failover
6. ✅ **Monitoring** - Resource tracking and performance metrics
7. ✅ **Containerization** - Docker packaging for reproducibility

### Project Ideas

#### Option 1: AI Study Buddy (Recommended for Beginners)
An intelligent study assistant that:
- Generates personalized study plans
- Creates practice questions from topics
- Tracks progress and suggests next steps
- Provides explanations for concepts
- Estimates time to completion

**Tech stack:** Python CLI/Web UI, Ollama, JSON storage

#### Option 2: Code Explainer Service
A service that:
- Accepts code snippets via API
- Explains what the code does (line by line or overview)
- Identifies potential bugs or improvements
- Suggests better alternatives
- Rates code complexity

**Tech stack:** FastAPI, Ollama/OpenAI, Docker

#### Option 3: Document Q&A System
A system that:
- Ingests text documents (markdown, txt)
- Answers questions about document content
- Cites sources in responses
- Handles multiple documents
- Tracks query history

**Tech stack:** Python, embeddings (basic), Ollama, Docker

#### Option 4: Custom Project
Design your own AI application that:
- Solves a real problem you have
- Uses at least 3 different prompts/functions
- Includes all required technical elements
- Can be demonstrated in 5-10 minutes

### Deliverables

#### 1. Source Code Repository
```
project/
├── README.md              # Clear setup and usage instructions
├── requirements.txt       # All dependencies
├── .env.example          # Configuration template
├── Dockerfile            # Container definition
├── docker-compose.yml    # Multi-service setup
├── src/
│   ├── __init__.py
│   ├── main.py          # Entry point
│   ├── ai_client.py     # AI integration
│   ├── prompts.py       # Prompt templates
│   └── utils.py         # Helper functions
├── tests/
│   ├── test_ai_client.py
│   └── test_prompts.py
├── data/                 # Sample data
└── docs/
    └── architecture.md   # System design
```

#### 2. Documentation

**README.md must include:**
- Project description and features
- Installation instructions (step-by-step)
- Usage examples
- Configuration options
- Troubleshooting guide
- Architecture diagram (can be ASCII art)

#### 3. Demonstration

Prepare a 5-10 minute demo showing:
1. **Setup** - How easy it is to get started
2. **Core Features** - 2-3 main capabilities
3. **AI Integration** - Show structured outputs, validation
4. **Error Handling** - Demonstrate graceful failures
5. **Monitoring** - Show metrics, logs, or resource usage

### Evaluation Criteria

**Technical Implementation (40%)**
- [ ] All core concepts integrated correctly
- [ ] AI produces structured, validated outputs
- [ ] Proper error handling and retries
- [ ] Resource monitoring included
- [ ] Docker containerization works

**Code Quality (20%)**
- [ ] Clean, readable Python code
- [ ] Proper project structure
- [ ] Configuration via environment
- [ ] Comments and docstrings
- [ ] No hardcoded secrets

**Functionality (20%)**
- [ ] Solves a real problem
- [ ] Core features work reliably
- [ ] User experience is smooth
- [ ] Error messages are helpful

**Documentation (20%)**
- [ ] Clear README with examples
- [ ] Setup instructions work
- [ ] Architecture is explained
- [ ] Code is well-commented
- [ ] Demo is well-prepared

### Timeline

**Week 8 Breakdown:**

**Days 1-2: Planning and Setup**
- Choose project idea
- Design architecture
- Set up repository structure
- Create project plan

**Days 3-5: Core Implementation**
- Implement AI integration
- Build core features
- Add error handling
- Write tests

**Days 6-7: Polish and Documentation**
- Dockerize application
- Write documentation
- Test deployment
- Prepare demo

### Success Checklist

Before submitting, verify:
- [ ] Code runs on a fresh machine following README
- [ ] Docker container builds and runs successfully
- [ ] All AI outputs are validated and structured
- [ ] Error handling is robust
- [ ] Documentation is complete
- [ ] Demo is prepared and tested
- [ ] Git repository is clean and organized
- [ ] No secrets committed to Git

---

## Learning Path Variations

### Fast Track (4 Weeks)
For those with programming experience:
- **Week 1:** Skim tools (2-3 hours), deep dive Python (5-6 hours)
- **Week 2:** Complete Weeks 3-4 (AI fundamentals and prompting)
- **Week 3:** Complete Weeks 5-6 (deployment and local inference)
- **Week 4:** Complete Weeks 7-8 (Docker and capstone)

### Extended Pace (12 Weeks)
For those needing more practice time:
- Weeks 1-2: Tools and Python (2 weeks each)
- Weeks 3-6: One AI concept per week
- Weeks 7-8: Deployment (2 weeks total)
- Weeks 9-12: Capstone with iterations

### Part-Time (16 Weeks)
For those studying 4-6 hours per week:
- Double the time for each week
- Focus on one major concept at a time
- Take breaks between major milestones

---

## Study Tips

### Daily Practice
- **Morning:** Read concepts (30-45 min)
- **Afternoon:** Code exercises (1-2 hours)
- **Evening:** Review and commit progress (15-30 min)

### When You Get Stuck
1. **Read error messages carefully** - They tell you what's wrong
2. **Print/log intermediate values** - See what's happening
3. **Simplify** - Comment out code until something works
4. **Search** - Google the exact error message
5. **Take a break** - Come back with fresh eyes
6. **Ask for help** - Community forums, study groups

### Progress Tracking
Keep a learning journal:
```markdown
# Week 1 - Day 3
**Time spent:** 2.5 hours
**Topics:** Git basics, branching
**Completed:**
- Created first repo
- Made 5 commits
- Resolved merge conflict
**Struggles:**
- Git merge was confusing
- Need to practice more
**Tomorrow:**
- Complete conda exercises
- Start Jupyter notebook
```

### Resource Management
- **Don't copy-paste blindly** - Type code yourself to learn
- **Experiment** - Change parameters and see what happens
- **Break down problems** - One small step at a time
- **Build incrementally** - Don't try to write everything at once
- **Test frequently** - Run code after every small change

---

## Additional Resources

### Documentation
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Git Documentation](https://docs.github.com/get-started/using-git/about-git)
- [Docker Getting Started](https://docs.docker.com/get-started/)
- [Ollama Documentation](https://github.com/ollama/ollama)

### Community
- [Python Discord](https://discord.com/invite/python)
- [r/learnpython](https://reddit.com/r/learnpython)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/python)

### Practice Platforms
- [Python Exercises](https://www.w3schools.com/python/python_exercises.asp)
- [LeetCode (Easy)](https://leetcode.com/problemset/all/?difficulty=Easy)
- [Exercism Python Track](https://exercism.org/tracks/python)

---

## Completion Certificate

After finishing Week 8, you will have:
- ✅ Built a complete AI application from scratch
- ✅ Deployed it using Docker
- ✅ Demonstrated professional development practices
- ✅ Created a portfolio project

**Next Steps:**
- Foundamental Course: Advanced AI Engineering (API development, RAG systems)
- Level 2: Production AI Systems (vector databases, scalable architectures)
- Level 3: AI Engineering Specializations

**Congratulations on your AI engineering journey!** 🎉
