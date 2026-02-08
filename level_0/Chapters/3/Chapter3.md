# Chapter 3: AI Engineering Fundamentals - Function Calling, Prompt Engineering, and Model Interfaces

## Overview

This chapter covers essential AI engineering concepts for working with modern language models and AI systems. You'll learn how to create reliable, structured interactions with AI models through function calling, master prompt engineering techniques, and understand different model interfaces and deployment options.

## Learning Path

### Part 1: Function Calling and Structured Outputs

**[📄 Read Documentation](./01_function_calling_structured_outputs.md)** | **[💻 Open Lab Notebook](./01_function_calling_structured_outputs_lab.ipynb)**

Learn to create reliable, machine-readable responses from AI models using JSON schemas, function definitions, and structured output constraints. Master the tool calling paradigm that enables AI models to interact with external systems and APIs.

**Key Concepts:**
- Function/tool calling with JSON Schema
- Structured output generation
- Cross-provider compatibility
- Reliability and validation techniques

### Part 2: Vibe Coding Workshop — AI-Assisted Development

**[📄 Read Workshop Guide](./02_prompt_engineering_evaluation.md)** | **[💻 Open Lab Notebook](./02_prompt_engineering_evaluation_lab.ipynb)**

Learn to use AI as a pair programmer through hands-on practice. Instead of studying prompt engineering theory, you'll build a tested CLI app using a repeatable 5-step workflow: spec → scaffold → test → iterate → review.

**Why This Approach:**
- **Practical**: Learn by doing, not by reading about prompts
- **Transferable**: Same workflow applies to any coding task
- **Quality-Focused**: Tests and reviews keep AI output reliable
- **Efficient**: Ship in hours what would take days manually

**The 5-Step Vibe Coding Loop:**
1. **Spec Prompt**: Requirements + constraints + acceptance tests
2. **Scaffold Prompt**: Project structure + minimal stubs
3. **Test Prompt**: Generate pytest tests from spec
4. **Patch Loop**: Test failure → minimal fix → verify
5. **Review/Refactor**: Checklist → targeted improvements

**What You'll Build:**
A production-ready CLI app (Learning Assistant) with:
- Multiple commands with argument parsing
- JSON persistence and validation
- Comprehensive test coverage
- Clear project structure

**Key Skills:**
- Writing prompts that constrain AI behavior
- Requesting minimal diffs (not rewrites)
- Using tests to drive iteration
- AI-assisted code review

### Part 3: Model Interfaces and Deployment

**[📄 Read Documentation](./03_model_interfaces_deployment.md)** | **[💻 Open Lab Notebook](./03_model_interfaces_deployment_lab.ipynb)**

Explore different ways to interact with AI models, from cloud APIs to local inference endpoints. Understand the trade-offs between various deployment options (Cloud vs. Local) and learn to build robust AI applications using industry-standard interfaces.

**Key Concepts:**
- **OpenAI-Compatible Standard**: Write code once, run anywhere
- **HuggingFace Inference**: Serverless APIs vs Dedicated Endpoints
- **Local Inference**: Quantization with Ollama for consumer hardware
- **High-Performance Serving**: PagedAttention with vLLM for production
- **Architecture**: Load balancing, security, and monitoring strategies

## Prerequisites

- Python 3.10+ installed
- Basic understanding of Python programming
- Familiarity with JSON and APIs
- Completion of Chapter 2: Python and Environment Management

## Technology Requirements

- **Python**: 3.10 or higher
- **PyTorch**: 2.6.0 or higher
- **CUDA**: 12.4 or higher (for GPU acceleration)
- **Key Libraries**: transformers, huggingface_hub, openai, requests

## Chapter Structure

Each part includes:
- **Conceptual explanations** with real-world examples
- **Hands-on coding exercises** in Jupyter notebooks
- **Practical labs** with step-by-step implementation
- **Assessment checkpoints** to verify understanding
- **Common pitfalls and solutions**

## Learning Outcomes

By the end of this chapter, you will be able to:

1. **Design and implement** function calling systems with proper JSON schema validation
2. **Create reliable prompts** that produce consistent, structured outputs
3. **Evaluate and optimize** model performance across different parameters and providers
4. **Deploy and manage** AI models using various interfaces (Ollama, vLLM, HuggingFace)
5. **Build production-ready** AI applications with proper error handling and monitoring

## Getting Started

Choose your learning path based on your experience level:

- **Beginners**: Start with Part 1 and progress sequentially
- **Experienced developers**: Focus on specific sections based on your needs
- **Hands-on learners**: Jump directly to the practical exercises and labs

Each section builds upon previous concepts, but can also be studied independently for specific skills.

---

*This chapter emphasizes practical, industry-relevant skills using open-source tools and platforms like HuggingFace, moving away from proprietary solutions toward more accessible and customizable alternatives.*
