# Fundamentals of AI Engineering - 6-Week Beginner Program

## Course Overview

The **Fundamentals of AI Engineering** course is designed for students with non-technical backgrounds, featuring a three-stage progressive teaching model: **"Agent Tools Introduction + AI-Assisted Learning + Technical Practice"**. The course emphasizes **conceptual intuition + AI-assisted practice + reproducible project delivery**.

### Course Highlights

- **Zero Programming Barrier in Weeks 1-2**: Start with Agent tools to build AI usage intuition
- **AI-Assisted Learning**: Use Cursor, ChatGPT, and other tools throughout to accelerate learning
- **Lowered Technical Barriers**: Bridge programming gaps through AI-powered tools
- **Progressive Depth**: Gradually advance from tool usage to technical implementation

## Target Students

- **Complete Beginners**: Individuals with no programming experience who want to transition into AI/Data Analytics
- **Tech Professionals**: Developers with some technical background but lacking systematic AI/ML foundations
- **Tool Users**: Professionals already using AI tools at work who want to deepen their understanding of underlying principles

## Prerequisites

### Weeks 1-2 (No Programming Required)

- Ability to use a web browser to access websites
- Ability to install and open software (e.g., browsers, editors)
- Basic computer operation skills

### Week 3+ (Introductory Programming)

- Basic CLI operations (installing dependencies, running scripts, viewing logs)
- Fundamental programming concepts (variables, conditions, loops, functions) or willingness to learn quickly with AI assistance

## Learn AI with AI Philosophy

The core feature of this course is **"Learn AI with AI"**:

1. **Weeks 1-2**: Learn to use AI Agent tools (Cursor, ChatGPT, Kilo, etc.)
2. **Weeks 3+**: Use AI tools to assist programming learning
   - Ask AI to explain code
   - Ask AI to help debug errors
   - Ask AI to generate code templates
   - Ask AI to answer technical questions

**Core Principle**: AI is your learning accelerator, not a replacement. You don't need to become a programming expert, but you need to learn how to collaborate with AI.

## Pre-Course Navigation

The course provides optional pre-study materials to help students prepare in advance:

- [Pre-Study Materials](PRESTUDY.md) - Preparation before Week 1
- [Course Syllabus](SYLLABUS.md) - Detailed 6-week schedule
- [Assignment Requirements](assignments.md) - Weekly evaluation criteria

### Self-Study References (Optional)

If you want to build a foundation in advance, you can refer to the following materials:

- [Self-Study Schedule](self_learn/Schedule.md)
- Chapters:
  - [Chapter 1: Tool Preparation](self_learn/Chapters/1/Chapter1.md)
  - [Chapter 2: Python and Environment Management](self_learn/Chapters/2/Chapter2.md)
  - [Chapter 3: AI Engineering Basics](self_learn/Chapters/3/Chapter3.md)
  - [Chapter 4: Hugging Face Platform and Local Inference](self_learn/Chapters/4/Chapter4.md)
  - [Chapter 5: Resource Monitoring and Containerization](self_learn/Chapters/5/Chapter5.md)

## Course Duration

- **Total Duration**: 6 weeks
- **Weekly Hours**: 5 hours (Recommended: 3 hours instruction + 2 hours practice)
- **Learning Rhythm**:
  - Session 1 (2 hours): Core concepts and examples
  - Session 2 (2 hours): Hands-on practice and exercises
  - Session 3 (1 hour): Q&A and review

## Learning Outcomes

Upon completing this course, you will be able to:

### 1. Proficiently Use AI Agent Tools

**What it means**: You can select appropriate AI tools for different types of problems and determine when to use AI vs. when to do it yourself.

**Proof**: Showcase 3 different AI task cases you completed during Weeks 1-2.

### 2. Use AI-Assisted Programming to Learn Python

**What it means**: You can read, modify, and debug code with AI tools, without needing to learn all programming details from scratch.

**Proof**: Showcase your code reading and modification exercises completed in Week 2.

### 3. Understand and Practice Local Inference and API Engineering

**What it means**: You can run Ollama local models, understand the differences between local and cloud-based approaches, and implement reliable LLM clients (including timeout, retry, and rate limiting).

**Proof**: Submit Week 3's LLM client code and model comparison report.

### 4. Master Data Processing Fundamentals

**What it means**: You can use pandas to read, clean, and analyze data, and generate data profiling reports.

**Proof**: Submit Week 4's data profiling report (JSON + Markdown format).

### 5. Complete ML Training Experiments and LLM Application Projects

**What it means**: You can train machine learning models, design prompts, and complete an end-to-end AI application project.

**Proof**:
- Week 5's model comparison experiment report
- Week 6's LLM application project (with demonstration)

## Assessment Method

| Week | Assessment Content | Weight |
|------|-------------------|--------|
| Week 1 | Agent Tool Experience Report | 10% |
| Week 2 | AI-Assisted Programming Practice Report | 10% |
| Week 3 | Local Inference and API Engineering Report | 15% |
| Week 4 | Data Profiling Report | 10% |
| Week 5 | ML Experiment Comparison Report | 10% |
| Week 6 | LLM Application Project + Demo | 25% |
| Participation | Attendance, discussion, peer review | 20% |

## Technology Stack

### Weeks 1-2 (Tool Usage Phase)

- **AI Chat Tools**: ChatGPT / Claude
- **AI Editor**: Cursor
- **AI Programming Assistants**: Kilo, GitHub Copilot Chat

### Weeks 3-6 (Technical Practice Phase)

- **Programming Language**: Python 3.10+ (3.11 recommended)
- **Core Libraries**: `numpy`, `pandas`, `scikit-learn`, `matplotlib`/`seaborn`
- **Engineering Tools**: `pytest`, `python-dotenv`, structured logging
- **LLM**: Cloud API (OpenAI/Anthropic) + Local Inference (Ollama)

---

# 6-Week Teaching Plan

## Week 1: Agent Tools Introduction - Using AI Without Writing Code

**Learning Objectives**:
- Understand what AI Agent tools are
- Master basic usage of Cursor, Kilo, ChatGPT/Claude, and other tools
- Experience "driving AI to complete tasks with natural language"
- Build intuitive understanding of AI capabilities

**Teaching Content**:
- **Session 1 (2h)**: Agent Tools Overview and Demo
  - What is an AI Agent? (Concept explanation + analogies)
  - Introduction to mainstream Agent tools: Cursor, Kilo, ChatGPT/Claude, GitHub Copilot Chat
  - Live demo: Using natural language to make AI complete simple tasks

- **Session 2 (2h)**: Hands-On Experience
  - Students register for/install tools
  - Practice tasks: Write articles with ChatGPT, explain projects with Cursor, complete commands with Kilo
  - Share most successful AI collaboration experiences

- **Session 3 (1h)**: Discussion and Reflection
  - Advantages and limitations of Agent tools
  - When to use AI vs. when to do it yourself
  - Share usage tips and prompt insights

**Deliverables**:
- Complete 3 different types of Agent tool experience tasks
- Write an "Agent Tool Usage Insights" report

**Resources**: [week_01/README.md](week_01/README.md)

---

## Week 2: IDE + Agent Practice - Starting to Work with Code

**Learning Objectives**:
- Use AI assistants in IDE environments
- Learn to have AI help you read and modify code
- Understand the "AI-assisted programming" workflow
- Initial exposure to Python code without requiring independent writing

**Teaching Content**:
- **Session 1 (2h)**: IDE + AI Environment Setup
  - Install VS Code or Cursor
  - Configure GitHub Copilot / Cursor AI
  - Learn basic IDE operations: opening files, running terminal, viewing output
  - AI-assisted programming workflow introduction

- **Session 2 (2h)**: Code Reading and Modification Practice
  - Use provided Python project templates
  - Task 1: Have AI explain what each code segment does
  - Task 2: Propose modification requirements and have AI help you change the code
  - Task 3: Run the code and observe results

- **Session 3 (1h)**: Problem-Solving Workshop
  - Common errors and how to debug with AI
  - What to do when AI gives incorrect answers
  - Students showcase code modifications they completed with AI assistance

**Deliverables**:
- Complete code explanation exercises (explain at least 5 functions)
- Complete code modification tasks (at least 3 modifications)
- Write an "AI-Assisted Programming Insights" report

**Resources**: [week_02/README.md](week_02/README.md)

---

## Week 3: Local Inference and API Engineering

**Learning Objectives**:
- Set up local Python development environment
- Install and run Ollama local models
- Understand the difference between local inference vs. cloud API
- Master LLM API reliability engineering (timeout, retry, rate limiting)
- Be able to call local and cloud models
- Implement reliable LLM clients

**Teaching Content**:
- **Session 1 (2h)**: Environment Setup and Local Inference
  - Python environment installation (using Anaconda for simplicity)
  - Virtual environment concepts and creation
  - Install Ollama
  - Download and run local models (llama3.2:1b)
  - Interact with models via command line

- **Session 2 (2h)**: API Calls and Reliability Engineering
  - Local inference vs. cloud API comparison
  - API failure modes: timeout, rate limiting, errors
  - Implement timeout settings and retry strategies
  - Add caching and logging
  - Build a simple LLM client

- **Session 3 (1h)**: Integration Practice
  - Unified interface: local and cloud models using the same calling method
  - Model comparison experiments (local vs. cloud quality, speed)
  - Troubleshooting and optimization

**Deliverables**:
- Successfully run Ollama local model
- Implement reliable LLM client (supporting local + cloud)
- Complete model comparison experiment report

**Resources**: [week_03/README.md](week_03/README.md)

---

## Week 4: Data Processing Fundamentals

**Learning Objectives**:
- Understand the importance of data for AI
- Learn to use pandas for basic data processing
- Be able to generate data profiling reports
- Master CSV data reading, cleaning, and analysis

**Teaching Content**:
- **Session 1 (2h)**: The Relationship Between Data and AI
  - Why data quality determines AI effectiveness
  - Pandas basics: reading CSV, viewing data
  - Data types and basic statistics
  - Practice: Load a dataset and view basic information

- **Session 2 (2h)**: Data Cleaning and Exploration
  - Handling missing values
  - Identifying outliers
  - Data distribution analysis
  - Generate data profiles (JSON/Markdown output)

- **Session 3 (1h)**: Data Report Workshop
  - Students generate reports using their own datasets
  - Share data discoveries
  - Discussion: How data issues affect AI models

**Deliverables**:
- Complete a data profiling report
- Clean a real dataset
- Write a data quality analysis report

**Resources**: [week_04/README.md](week_04/README.md)

---

## Week 5: ML Training Loop

**Learning Objectives**:
- Understand the basic machine learning workflow
- Master the concept of train/validation split
- Be able to train a basic classification model
- Learn to compare results from different experiments

**Teaching Content**:
- **Session 1 (2h)**: ML Fundamentals
  - What is training? What is inference?
  - Train/Validation/Test split
  - Overfitting and underfitting (intuitive explanation)
  - Basic evaluation metrics: accuracy, F1 score

- **Session 2 (2h)**: Train Your First Model
  - Train a classifier using scikit-learn
  - Save models and experiment configurations
  - Evaluate model performance
  - Run multiple experiments and compare results

- **Session 3 (1h)**: Experiment Comparison Workshop
  - Change parameters and observe performance changes
  - Write experiment comparison reports
  - Discussion: Under what conditions do models perform better?

**Deliverables**:
- Train at least 2 different models
- Complete model comparison report
- Explain experiment design decisions

**Resources**: [week_05/README.md](week_05/README.md)

---

## Week 6: LLM Application Practice

**Learning Objectives**:
- Understand Token and context window concepts
- Master basic prompt engineering techniques
- Apply Pipeline thinking to integrate knowledge from Weeks 1-5
- Complete a simplified end-to-end project
- Course review and outlook

**Teaching Content**:
- **Session 1 (2h)**: LLM Basics and Prompt Engineering
  - Tokenization introduction and context window limitations
  - Prompt design best practices
  - Structured prompts and JSON output
  - Introduction to validation and retry mechanisms

- **Session 2 (2h)**: End-to-End Project Practice
  - Project introduction: Data Analysis Assistant (simplified version)
  - Use provided project templates
  - Data sampling and compression (using Week 4 skills)
  - Build prompts to call LLM (using Week 3 skills)
  - Generate reports (JSON + Markdown)

- **Session 3 (1h)**: Project Showcase and Course Review
  - Student project demonstrations (3-5 minutes each)
  - Course highlights review
  - Learning path recommendations (Level 2 preview)
  - Closing ceremony

**Deliverables**:
- Design 2-3 effective prompt templates
- Complete simplified data analysis project
- Project demonstration and reflection

**Resources**: [week_06/README.md](week_06/README.md)

---

## Learning Path

After completing this course, you can continue:

### Level 2: RAG and Advanced Agent Systems

- **Weeks 1-2**: RAG fundamentals (vector databases, embeddings, retrieval strategies)
- **Weeks 3-4**: Agent system design (tool usage, planning, multi-agent collaboration)
- **Weeks 5-6**: Production-grade deployment (FastAPI, monitoring, evaluation)
- **Weeks 7-8**: Advanced topics (multimodal, fine-tuning, optimization)

### Practical Recommendations

1. **Continue using AI tools**: Make Cursor, ChatGPT your daily assistants
2. **Practice hands-on**: Write a small demo for every concept you learn
3. **Join communities**: Participate in AI learning communities and share your projects
4. **Read documentation**: Learn to read official documentation—this is the most important skill

---

## Core Knowledge Areas

### AI Concepts (Fundamentals)
- Train/validation/overfitting
- Loss functions and evaluation metrics
- Transformer, Token, context window
- Prompt engineering basics

### AI Engineering (Fundamentals)
- Python data stack
- Traditional ML experiments
- Production-grade LLM API usage
- Local inference (Ollama)

### Meta-Learning (Introduction)
- Reading official documentation
- Creating minimal reproducible cases
- Basic debugging capabilities

### System Design (Introduction)
- Modular scripts
- Clear interface design
- Configuration management

---

## How to Ask for Help

When you encounter problems (asking instructors, classmates, or online), please follow this process:

1. **Reproduce the problem**: Reproduce it at least once (don't guess)
2. **Provide complete information**:
   - Goal: What are you trying to do
   - Context: Which assignment/step
   - Complete commands and output (don't screenshot)
   - Your environment: operating system, Python version, dependency versions
   - Relevant code snippets (minimal examples)
   - What you have already tried

3. **Search first**:
   - Official documentation
   - Error messages
   - GitHub issues

4. **Use AI**: Ask ChatGPT/Cursor questions with complete context

**Why this works**:
- Changes debugging from "guessing" to "evidence"
- Reduces back-and-forth communication (others can run the same commands and see the same results)
- Helps you learn faster (practice isolating variables)

---

## Key Terms Quick Reference

- **CLI**: Command Line Interface (terminal)
- **Virtual Environment**: Isolated Python environment to avoid dependency conflicts
- **Dependency Management**: Installing and pinning package versions to ensure project reproducibility
- **`.env`**: Environment variables file for storing secrets like API keys
- **`requirements.txt`**: File declaring project dependencies
- **README**: Project documentation file, should include setup, running, and expected output
- **pytest**: Python testing framework
- **Train/validation split**: Dividing data into training and evaluation portions
- **Overfitting**: Model memorizes training data but performs poorly on new data
- **LLM**: Large Language Model
- **Token**: Minimum processing unit of text
- **Context Window**: Maximum number of tokens a model can process at once
- **Transformer**: Neural network architecture for modern LLMs
- **Hosted API**: Cloud-based model endpoint (usually requires API key)
- **Timeout/retry**: Reliability controls for network calls
- **Structured output**: Fixed-format output (e.g., JSON)
- **Local inference**: Running models locally (rather than cloud API)

---

## Document Navigation

- **Course Syllabus**: [SYLLABUS.md](SYLLABUS.md) - Detailed 6-week schedule
- **Pre-Study Materials**: [PRESTUDY.md](PRESTUDY.md) - Pre-course preparation
- **Assignment Requirements**: [assignments.md](assignments.md) - Evaluation criteria
- **Original Course Archive**: [old_v1/](old_v1/) - Original 8-week course content

---

**Course Version**: v2.0 (6-Week Course)  
**Last Updated**: 2026-04-01  
**Major Changes**: Compressed from 8 weeks to 6 weeks, added Agent tools introduction, lowered technical barriers
