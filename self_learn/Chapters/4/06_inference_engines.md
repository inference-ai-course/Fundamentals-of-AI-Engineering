# Inference Engines: Ollama and vLLM

## Introduction

This guide covers two popular local inference engines for running large language models: **Ollama** and **vLLM**. Both enable you to deploy LLMs on your own hardware, but they serve different use cases and have distinct performance characteristics.

## Overview Comparison

| Feature | Ollama | vLLM |
|---------|--------|------|
| **Ease of Use** | ⭐⭐⭐⭐⭐ Simple CLI | ⭐⭐⭐ Requires configuration |
| **Performance** | ⭐⭐⭐ Good | ⭐⭐⭐⭐⭐ Excellent (10-20x faster) |
| **Memory Efficiency** | ⭐⭐⭐ Standard | ⭐⭐⭐⭐⭐ PagedAttention |
| **Setup Time** | ⭐⭐⭐⭐⭐ Minutes | ⭐⭐⭐ More involved |
| **Best For** | Development, prototyping | Production, high throughput |
| **Multi-GPU** | ❌ Limited | ✅ Full support |
| **Batching** | ⭐⭐ Basic | ⭐⭐⭐⭐⭐ Continuous batching |

---

# Part 1: Ollama

## What is Ollama?

**Ollama** is a lightweight, user-friendly tool for running large language models locally. It's designed to make running LLMs as easy as running Docker containers.

### Key Features

- ✅ **Simple CLI**: Easy-to-use command-line interface
- ✅ **Model Library**: Access to popular open-source models
- ✅ **Automatic GPU**: Detects and uses available GPUs
- ✅ **REST API**: Standard HTTP interface
- ✅ **OpenAI Compatible**: Works with OpenAI client libraries
- ✅ **Cross-Platform**: Runs on Linux, macOS, and Windows

### What Ollama Handles

- Model downloading and management
- Automatic GPU acceleration
- REST API server
- OpenAI-compatible endpoints
- Model quantization and optimization

## Installation

### Linux

```bash
# Download and install
curl -fsSL https://ollama.com/install.sh | sh

# Verify installation
ollama --version
```

### macOS

```bash
# Using Homebrew
brew install ollama

# Or download from https://ollama.com/download
```

### Windows

Download the installer from [ollama.com/download](https://ollama.com/download) and run it.

## Core CLI Commands

### 1. Pull Models

```bash
# Pull a specific model
ollama pull llama3.2

# Pull specific version/size
ollama pull llama3.2:3b
ollama pull mistral:7b
ollama pull codellama:13b
```

**Available Models:**
- `llama3.2` - Meta's Llama 3.2 (3B, 7B)
- `mistral` - Mistral 7B
- `codellama` - Code-specialized Llama
- `phi3` - Microsoft's Phi-3
- `gemma` - Google's Gemma
- More at [ollama.com/library](https://ollama.com/library)

### 2. List Models

```bash
ollama list
```

### 3. Run Models (Interactive)

```bash
ollama run llama3.2

# Interactive commands:
# /bye - Exit
# /clear - Clear history
# /show - Show model info
```

### 4. Start API Server

```bash
ollama serve
# Server starts on http://localhost:11434
```

### 5. Remove Models

```bash
ollama rm llama3.2
```

## REST API

### Generate Completion

```python
import requests

url = "http://localhost:11434/api/generate"
payload = {
    "model": "llama3.2",
    "prompt": "Explain quantum computing",
    "stream": False
}

response = requests.post(url, json=payload)
result = response.json()
print(result["response"])
```

### Chat Completion

```python
url = "http://localhost:11434/api/chat"
payload = {
    "model": "llama3.2",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is Python?"}
    ],
    "stream": False
}

response = requests.post(url, json=payload)
result = response.json()
print(result["message"]["content"])
```

### Streaming

```python
import json

payload = {
    "model": "llama3.2",
    "messages": [{"role": "user", "content": "Tell me a story"}],
    "stream": True
}

response = requests.post(url, json=payload, stream=True)

for line in response.iter_lines():
    if line:
        chunk = json.loads(line)
        if "message" in chunk:
            print(chunk["message"]["content"], end="", flush=True)
```

## OpenAI-Compatible API

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"  # Required but not used
)

response = client.chat.completions.create(
    model="llama3.2",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
)

print(response.choices[0].message.content)
```

## Configuration

### Environment Variables

```bash
# Change server host/port
export OLLAMA_HOST=0.0.0.0:11434

# Set model storage location
export OLLAMA_MODELS=/path/to/models

# Disable GPU
export OLLAMA_GPU=0

# Set number of GPUs
export OLLAMA_NUM_GPU=2
```

### Modelfile Customization

```dockerfile
# Modelfile
FROM llama3.2

# Set temperature
PARAMETER temperature 0.8

# Set context window
PARAMETER num_ctx 4096

# Set system prompt
SYSTEM You are a helpful coding assistant.
```

Load custom model:
```bash
ollama create my-assistant -f Modelfile
ollama run my-assistant
```

## Performance Considerations

**Memory Requirements:**
- 3B model: 4-6GB VRAM
- 7B model: 8-12GB VRAM
- 13B model: 16-20GB VRAM

**Best Practices:**
- Use 3B-7B models for development
- Use 7B-13B models for production
- Monitor GPU usage with `nvidia-smi`
- Implement error handling and timeouts

---

# Part 2: vLLM

## What is vLLM?

**vLLM** (Very Large Language Model) is a high-performance inference engine optimized for throughput and memory efficiency. It's designed for production deployments with many concurrent requests.

### Key Features

- ✅ **High Throughput**: 10-20x faster than naive implementations
- ✅ **Memory Efficient**: PagedAttention reduces memory waste by ~40%
- ✅ **Continuous Batching**: Maximizes GPU utilization
- ✅ **Multi-GPU**: Tensor and pipeline parallelism
- ✅ **OpenAI API**: Drop-in replacement for OpenAI
- ✅ **Streaming**: Real-time token streaming

### What vLLM Provides

- **PagedAttention**: Efficient KV cache management
- **Continuous Batching**: Dynamic request batching
- **Optimized Kernels**: Custom CUDA kernels for speed
- **Tensor Parallelism**: Multi-GPU support
- **OpenAI Compatibility**: Standard API interface

## Installation

### Prerequisites

- Python 3.10+
- CUDA 12.4+
- PyTorch 2.6.0+
- 8GB+ VRAM

### Install vLLM

```bash
# Install from PyPI
pip install vllm>=0.6.0

# Or with specific CUDA version
pip install vllm --extra-index-url https://download.pytorch.org/whl/cu124

# Verify
python -c "import vllm; print(vllm.__version__)"
```

## Running vLLM

### Method 1: Python API (Offline Mode)

```python
from vllm import LLM, SamplingParams

# Initialize model
llm = LLM(
    model="meta-llama/Llama-3.2-3B-Instruct",
    tensor_parallel_size=1,
    gpu_memory_utilization=0.9
)

# Define sampling
sampling_params = SamplingParams(
    temperature=0.7,
    top_p=0.9,
    max_tokens=512
)

# Generate
prompts = ["Explain quantum computing in simple terms."]
outputs = llm.generate(prompts, sampling_params)

for output in outputs:
    print(output.outputs[0].text)
```

### Method 2: OpenAI-Compatible Server

```bash
# Start server
python -m vllm.entrypoints.openai.api_server \
    --model meta-llama/Llama-3.2-3B-Instruct \
    --port 8000 \
    --host 0.0.0.0 \
    --gpu-memory-utilization 0.9
```

Server available at: `http://localhost:8000/v1`

### Method 3: Docker

```bash
docker pull vllm/vllm-openai:latest

docker run --gpus all \
    -p 8000:8000 \
    --ipc=host \
    vllm/vllm-openai:latest \
    --model meta-llama/Llama-3.2-3B-Instruct
```

## Using the API

### With OpenAI Client

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="EMPTY"
)

response = client.chat.completions.create(
    model="meta-llama/Llama-3.2-3B-Instruct",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is machine learning?"}
    ],
    temperature=0.7,
    max_tokens=500
)

print(response.choices[0].message.content)
```

### Streaming

```python
response = client.chat.completions.create(
    model="meta-llama/Llama-3.2-3B-Instruct",
    messages=[{"role": "user", "content": "Write a short story"}],
    stream=True
)

for chunk in response:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

## Advanced Configuration

### Server Parameters

```bash
python -m vllm.entrypoints.openai.api_server \
    --model meta-llama/Llama-3.2-3B-Instruct \
    --port 8000 \
    --gpu-memory-utilization 0.9 \
    --max-model-len 4096 \
    --max-num-seqs 256 \
    --tensor-parallel-size 1 \
    --enable-prefix-caching \
    --quantization awq
```

### Key Parameters

| Parameter | Description | Default | Recommendation |
|-----------|-------------|---------|----------------|
| `--gpu-memory-utilization` | GPU memory fraction | 0.9 | 0.85-0.95 |
| `--max-model-len` | Max sequence length | Model default | Set based on use case |
| `--max-num-seqs` | Max concurrent sequences | 256 | Higher for throughput |
| `--tensor-parallel-size` | Number of GPUs | 1 | Match available GPUs |
| `--enable-prefix-caching` | Cache common prefixes | False | True for repeated prompts |

## Performance Optimization

### 1. PagedAttention (Automatic)

Reduces memory waste by ~40% through efficient KV cache management.

### 2. Continuous Batching (Automatic)

Dynamically batches requests for maximum throughput.

### 3. Prefix Caching

```python
llm = LLM(
    model="meta-llama/Llama-3.2-3B-Instruct",
    enable_prefix_caching=True  # Cache repeated system prompts
)
```

### 4. Multi-GPU Inference

```python
# Tensor parallelism - split model across GPUs
llm = LLM(
    model="meta-llama/Llama-3.1-70B-Instruct",
    tensor_parallel_size=2,  # Use 2 GPUs
    gpu_memory_utilization=0.9
)
```

```bash
# Server with multi-GPU
python -m vllm.entrypoints.openai.api_server \
    --model meta-llama/Llama-3.1-70B-Instruct \
    --tensor-parallel-size 2
```

### 5. Quantization

```bash
# AWQ quantization (recommended)
python -m vllm.entrypoints.openai.api_server \
    --model TheBloke/Llama-2-7B-AWQ \
    --quantization awq
```

## Sampling Parameters

```python
from vllm import SamplingParams

# Deterministic
deterministic = SamplingParams(temperature=0.0, max_tokens=512)

# Creative
creative = SamplingParams(temperature=0.9, top_p=0.95, top_k=50, max_tokens=1024)

# Balanced
balanced = SamplingParams(temperature=0.7, top_p=0.9, max_tokens=512)
```

---

# Comparison and Selection Guide

## When to Use Ollama

✅ **Best for:**
- Rapid prototyping
- Local development
- Learning and experimentation
- Simple deployments
- Single-user applications
- Quick model testing

✅ **Advantages:**
- Extremely easy setup (minutes)
- Simple CLI interface
- Automatic model management
- Cross-platform support
- Good for beginners

❌ **Limitations:**
- Lower throughput than vLLM
- Limited batching capabilities
- Less optimization options
- Single-GPU focus

## When to Use vLLM

✅ **Best for:**
- Production deployments
- High-throughput applications
- Multi-user services
- Batch processing
- Performance-critical applications
- Multi-GPU setups

✅ **Advantages:**
- 10-20x higher throughput
- Efficient memory usage (PagedAttention)
- Continuous batching
- Multi-GPU support
- Advanced optimization

❌ **Limitations:**
- More complex setup
- Requires more configuration
- Steeper learning curve
- Higher memory requirements

## Performance Comparison

| Metric | Ollama | vLLM |
|--------|--------|------|
| **Throughput** | ~20-50 tokens/s | ~200-500 tokens/s |
| **Latency** | Medium | Low |
| **Memory Efficiency** | Standard | High (PagedAttention) |
| **Concurrent Users** | 1-5 | 10-100+ |
| **Setup Time** | 5 minutes | 30-60 minutes |

## Decision Matrix

```
Need quick setup? ──────────────────────> Ollama
Need maximum performance? ──────────────> vLLM
Learning/experimenting? ────────────────> Ollama
Production deployment? ─────────────────> vLLM
Single user? ───────────────────────────> Ollama
Multiple concurrent users? ─────────────> vLLM
Limited GPU resources? ─────────────────> Ollama
Multiple GPUs available? ───────────────> vLLM
```

## Hybrid Approach

You can use both:
1. **Development**: Use Ollama for rapid iteration
2. **Testing**: Benchmark with both engines
3. **Production**: Deploy with vLLM for performance
4. **Fallback**: Keep Ollama as a backup option

---

# Troubleshooting

## Ollama Issues

**Server Not Starting:**
```bash
lsof -i :11434  # Check port
pkill ollama    # Kill process
ollama serve    # Restart
```

**Out of Memory:**
```bash
ollama pull llama3.2:3b  # Use smaller model
OLLAMA_GPU=0 ollama run llama3.2  # Use CPU
```

## vLLM Issues

**Out of Memory:**
```bash
python -m vllm.entrypoints.openai.api_server \
    --model meta-llama/Llama-3.2-3B-Instruct \
    --gpu-memory-utilization 0.7 \
    --max-model-len 2048
```

**CUDA Errors:**
```bash
nvidia-smi  # Check CUDA
pip uninstall vllm
pip install vllm --extra-index-url https://download.pytorch.org/whl/cu124
```

---

# Next Steps

- Complete **[Ollama Practice Notebook](05_ollama_practice.ipynb)**
- Explore vLLM with hands-on exercises
- Run performance benchmarks
- Choose the right engine for your use case
- Deploy to production

## Additional Resources

- [Ollama Documentation](https://github.com/ollama/ollama)
- [vLLM Documentation](https://docs.vllm.ai/)
- [Model Library](https://ollama.com/library)
- [Performance Benchmarks](https://blog.vllm.ai/)
