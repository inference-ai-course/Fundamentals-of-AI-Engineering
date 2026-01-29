# Core Concepts and Theory

## Introduction

This document provides detailed explanations of the fundamental concepts you'll encounter when working with Hugging Face inference providers. Understanding these concepts is essential for building robust, scalable AI applications.

## Hugging Face Libraries in Practice

Before diving into inference providers, let's explore practical examples using key Hugging Face libraries.

### Using Transformers for Different Tasks

**Question Answering:**
```python
from transformers import pipeline

# Create QA pipeline
qa_pipeline = pipeline("question-answering")

context = """
Hugging Face is a company that develops tools for building applications using 
machine learning. It is most notable for its Transformers library, which provides 
APIs to use pre-trained models for NLP tasks.
"""

question = "What is Hugging Face most notable for?"

result = qa_pipeline(question=question, context=context)
print(f"Answer: {result['answer']}")
print(f"Confidence: {result['score']:.2%}")
```

**Named Entity Recognition:**
```python
from transformers import pipeline

ner = pipeline("ner", grouped_entities=True)

text = "Hugging Face Inc. is based in New York City and was founded by Clément Delangue."
entities = ner(text)

for entity in entities:
    print(f"{entity['word']}: {entity['entity_group']} ({entity['score']:.2%})")
# Output:
# Hugging Face Inc.: ORG (99.8%)
# New York City: LOC (99.9%)
# Clément Delangue: PER (99.7%)
```

**Zero-Shot Classification:**
```python
from transformers import pipeline

classifier = pipeline("zero-shot-classification")

text = "This tutorial teaches you about Hugging Face libraries"
candidate_labels = ["education", "politics", "sports", "technology"]

result = classifier(text, candidate_labels)

for label, score in zip(result['labels'], result['scores']):
    print(f"{label}: {score:.2%}")
# Output:
# education: 87.3%
# technology: 8.2%
# ...
```

### Working with Datasets

**Data Preprocessing:**
```python
from datasets import load_dataset
from transformers import AutoTokenizer

# Load dataset
dataset = load_dataset("glue", "mrpc", split="train")

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Tokenize function
def tokenize_function(examples):
    return tokenizer(
        examples["sentence1"],
        examples["sentence2"],
        padding="max_length",
        truncation=True
    )

# Apply tokenization
tokenized_dataset = dataset.map(tokenize_function, batched=True)

print(f"Original columns: {dataset.column_names}")
print(f"Tokenized columns: {tokenized_dataset.column_names}")
```

**Dataset Filtering and Mapping:**
```python
from datasets import load_dataset

dataset = load_dataset("imdb", split="train")

# Filter positive reviews
positive_reviews = dataset.filter(lambda x: x["label"] == 1)

# Add text length column
def add_length(example):
    example["text_length"] = len(example["text"])
    return example

dataset_with_length = dataset.map(add_length)

print(f"Average review length: {sum(dataset_with_length['text_length']) / len(dataset_with_length):.0f} chars")
```

### Advanced Tokenization

**Custom Tokenizer Training:**
```python
from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace

# Initialize tokenizer
tokenizer = Tokenizer(BPE(unk_token="[UNK]"))
tokenizer.pre_tokenizer = Whitespace()

# Train on custom data
trainer = BpeTrainer(special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"])

files = ["training_data.txt"]
tokenizer.train(files, trainer)

# Use the tokenizer
output = tokenizer.encode("Hello, how are you?")
print(f"Tokens: {output.tokens}")
print(f"IDs: {output.ids}")
```

### Model Fine-Tuning with PEFT

**Complete LoRA Example:**
```python
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer
from peft import LoraConfig, get_peft_model, TaskType
from datasets import load_dataset

# Load model and tokenizer
model_name = "gpt2"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token

# Configure LoRA
peft_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=8,
    lora_alpha=32,
    lora_dropout=0.1,
    target_modules=["c_attn", "c_proj"]
)

# Apply PEFT
model = get_peft_model(model, peft_config)
model.print_trainable_parameters()

# Load and prepare dataset
dataset = load_dataset("imdb", split="train[:1000]")

def tokenize(examples):
    return tokenizer(examples["text"], truncation=True, padding="max_length", max_length=128)

tokenized_dataset = dataset.map(tokenize, batched=True)

# Training arguments
training_args = TrainingArguments(
    output_dir="./lora-gpt2",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    save_steps=100,
    logging_steps=10
)

# Train
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset
)

trainer.train()
```

### Evaluation Metrics

**Comprehensive Evaluation:**
```python
import evaluate
import numpy as np

# Load multiple metrics
accuracy = evaluate.load("accuracy")
precision = evaluate.load("precision")
recall = evaluate.load("recall")
f1 = evaluate.load("f1")

# Predictions and references
predictions = np.array([0, 1, 1, 0, 1, 1, 0, 1])
references = np.array([0, 1, 0, 0, 1, 1, 1, 1])

# Compute all metrics
results = {
    "accuracy": accuracy.compute(predictions=predictions, references=references),
    "precision": precision.compute(predictions=predictions, references=references, average="binary"),
    "recall": recall.compute(predictions=predictions, references=references, average="binary"),
    "f1": f1.compute(predictions=predictions, references=references, average="binary")
}

for metric, value in results.items():
    print(f"{metric.capitalize()}: {value[metric]:.3f}")
```

### Building Interactive Demos with Gradio

**Advanced Gradio Interface:**
```python
import gradio as gr
from transformers import pipeline

# Load multiple models
sentiment_analyzer = pipeline("sentiment-analysis")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
translator = pipeline("translation_en_to_fr", model="t5-base")

def analyze_text(text, task):
    if task == "Sentiment Analysis":
        result = sentiment_analyzer(text)[0]
        return f"{result['label']}: {result['score']:.2%}"
    
    elif task == "Summarization":
        summary = summarizer(text, max_length=130, min_length=30)[0]
        return summary['summary_text']
    
    elif task == "Translation (EN→FR)":
        translation = translator(text)[0]
        return translation['translation_text']

# Create interface
demo = gr.Interface(
    fn=analyze_text,
    inputs=[
        gr.Textbox(lines=5, placeholder="Enter text here..."),
        gr.Radio(["Sentiment Analysis", "Summarization", "Translation (EN→FR)"], 
                 label="Task", value="Sentiment Analysis")
    ],
    outputs=gr.Textbox(label="Result"),
    title="Multi-Task NLP Demo",
    description="Analyze sentiment, summarize, or translate text",
    examples=[
        ["This is an amazing tutorial!", "Sentiment Analysis"],
        ["Hugging Face provides tools for NLP. It has transformers library.", "Summarization"]
    ]
)

demo.launch(share=True)
```

## 1. Inference Providers

### What Are Inference Providers?

**Inference providers** are backend services that execute machine learning models to generate predictions or outputs. In the Hugging Face ecosystem, providers represent different computational backends that can run the same model with varying performance characteristics.

### Key Characteristics

- **Unified Interface**: All providers are accessed through a consistent API, regardless of the underlying infrastructure
- **Dynamic Selection**: The platform can automatically choose the best available provider
- **Geographic Distribution**: Providers may be located in different regions for latency optimization
- **Specialized Hardware**: Different providers may use CPUs, GPUs, or specialized accelerators

### Provider Types

1. **Cloud Providers**
   - Managed by Hugging Face or third-party services
   - Scalable and highly available
   - Pay-per-use billing model
   - Examples: AWS, Azure, GCP-based endpoints

2. **Community Providers**
   - Contributed by the community
   - May have usage limits or quotas
   - Often free for experimentation

3. **Dedicated Providers**
   - Private deployments for enterprise use
   - Custom SLAs and performance guarantees
   - Enhanced security and compliance

### Provider Selection Strategies

#### Automatic Selection (`provider="auto"`)

```python
# The platform selects the best available provider
response = client.text_to_image(
    prompt="A serene mountain landscape",
    provider="auto"  # Automatic selection
)
```

**Advantages:**
- Automatic failover if a provider is unavailable
- Load balancing across multiple backends
- Optimized for current availability and performance

**Disadvantages:**
- Less predictable latency
- Harder to debug provider-specific issues
- May incur varying costs

#### Explicit Selection

```python
# Specify a particular provider
response = client.text_to_image(
    prompt="A serene mountain landscape",
    provider="aws-inference-1"  # Explicit selection
)
```

**Advantages:**
- Predictable performance characteristics
- Easier debugging and monitoring
- Cost control and budgeting

**Disadvantages:**
- No automatic failover
- Manual handling of provider unavailability
- Potential for suboptimal selection

## 2. Authentication and Billing

### Authentication Mechanisms

#### API Tokens

Hugging Face uses **token-based authentication** for API access:

- **Read Tokens**: Access public models and datasets
- **Write Tokens**: Upload models, create repositories
- **Fine-grained Tokens**: Scoped permissions for specific resources

#### Token Management Best Practices

1. **Environment Variables**
   ```bash
   export HF_TOKEN="hf_your_token_here"
   ```

2. **Configuration Files**
   ```python
   # ~/.huggingface/token (automatically read by libraries)
   ```

3. **Secret Management Systems**
   - AWS Secrets Manager
   - Azure Key Vault
   - HashiCorp Vault

### Security Considerations

❌ **Never do this:**
```python
# Hardcoded token - INSECURE!
client = InferenceClient(token="hf_abc123xyz")
```

✅ **Always do this:**
```python
import os
# Load from environment
token = os.getenv("HF_TOKEN")
client = InferenceClient(token=token)
```

### Billing Models

Different providers have different billing structures:

1. **Per-Request Pricing**
   - Charged per API call
   - Varies by model size and complexity

2. **Token-Based Pricing**
   - Charged per input/output token
   - Common for language models

3. **Compute-Time Pricing**
   - Charged per second of computation
   - Common for image/video generation

4. **Subscription Models**
   - Fixed monthly fee
   - Includes quota of requests or tokens

## 3. OpenAI-Compatible Interfaces

### What is OpenAI Compatibility?

Many inference services expose an **OpenAI-compatible API**, which means they implement the same request/response format as OpenAI's API. This enables:

- **Code Portability**: Write once, run anywhere
- **Library Compatibility**: Use existing OpenAI client libraries
- **Standardization**: Consistent patterns across providers

### Standard API Patterns

#### Chat Completions

```python
# OpenAI-style chat format
response = client.chat.completions.create(
    model="meta-llama/Llama-3.2-3B-Instruct",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is machine learning?"}
    ],
    temperature=0.7,
    max_tokens=500
)
```

#### Completions

```python
# Text completion format
response = client.completions.create(
    model="gpt2",
    prompt="Once upon a time",
    max_tokens=100
)
```

### Benefits of Standardization

1. **Vendor Independence**: Switch providers without rewriting code
2. **Ecosystem Compatibility**: Use tools built for OpenAI API
3. **Learning Transfer**: Skills apply across multiple platforms
4. **Testing Flexibility**: Easy to compare providers

## 4. Connecting to Local Endpoints via HTTP

### Local Inference Architecture

```
┌─────────────┐      HTTP/REST      ┌──────────────────┐
│   Client    │ ──────────────────> │  Local Server    │
│  (Python)   │ <────────────────── │  (Ollama/vLLM)   │
└─────────────┘      JSON           └──────────────────┘
                                              │
                                              ▼
                                        ┌──────────┐
                                        │  Model   │
                                        │  (GPU)   │
                                        └──────────┘
```

### HTTP Client Configuration

#### Using Requests Library

```python
import requests

url = "http://localhost:11434/api/chat"
payload = {
    "model": "llama2",
    "messages": [{"role": "user", "content": "Hello!"}]
}

response = requests.post(url, json=payload)
result = response.json()
```

#### Using OpenAI-Compatible Client

```python
from openai import OpenAI

# Point to local endpoint
client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="not-needed"  # Local servers often don't require auth
)

response = client.chat.completions.create(
    model="local-model",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Advantages of Local Endpoints

1. **Privacy**: Data never leaves your infrastructure
2. **Cost**: No per-request charges after initial setup
3. **Latency**: Reduced network overhead
4. **Customization**: Full control over model and configuration
5. **Offline Operation**: No internet dependency

### Challenges

1. **Hardware Requirements**: Need sufficient GPU/CPU resources
2. **Maintenance**: Responsible for updates and monitoring
3. **Scalability**: Limited by local hardware capacity
4. **Setup Complexity**: More initial configuration required

## 5. Failover and Timeout Strategies

### Implementing Failover

```python
from huggingface_hub import InferenceClient
import time

def inference_with_failover(prompt, providers):
    """Try multiple providers in sequence"""
    for provider in providers:
        try:
            client = InferenceClient(provider=provider)
            response = client.text_to_image(prompt)
            return response
        except Exception as e:
            print(f"Provider {provider} failed: {e}")
            continue
    raise Exception("All providers failed")

# Usage
providers = ["provider-1", "provider-2", "auto"]
result = inference_with_failover("A sunset", providers)
```

### Timeout Configuration

```python
import requests

# Set appropriate timeouts
response = requests.post(
    url,
    json=payload,
    timeout=(5, 30)  # (connect timeout, read timeout)
)
```

**Timeout Guidelines:**
- **Text Generation**: 10-30 seconds
- **Image Generation**: 30-60 seconds
- **Video Generation**: 60-300 seconds

### Retry Logic with Exponential Backoff

```python
import time
from typing import Callable, Any

def retry_with_backoff(
    func: Callable,
    max_retries: int = 3,
    base_delay: float = 1.0
) -> Any:
    """Retry with exponential backoff"""
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            delay = base_delay * (2 ** attempt)
            print(f"Retry {attempt + 1}/{max_retries} after {delay}s")
            time.sleep(delay)
```

## Summary

Understanding these core concepts enables you to:

- Choose appropriate inference providers for your use case
- Implement secure authentication and manage costs effectively
- Write portable code using OpenAI-compatible interfaces
- Connect to both cloud and local endpoints seamlessly
- Build resilient applications with proper failover and timeout handling

## Next Steps

- Proceed to **[Authentication and Security](03_authentication_security.md)** for detailed credential management
- Review **[Provider Selection Guide](04_provider_selection.md)** for choosing the right provider
- Practice with the Jupyter notebooks
