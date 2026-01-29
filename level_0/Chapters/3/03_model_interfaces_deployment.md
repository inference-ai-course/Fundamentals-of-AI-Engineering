# Part 3: Model Interfaces and Deployment

## Overview

**The Reality Check:** Training an AI model takes hours or days. Deploying it incorrectly can waste months of work.

You've built an amazing model or found the perfect one on HuggingFace. Now what? Do you call OpenAI's API and pay per token? Run it locally on your laptop? Deploy to AWS with GPU instances? Use Ollama for development and vLLM for production?

**Wrong choice = Slow inference, high costs, or complete failure under load.**

This section teaches you to make informed deployment decisions based on:
- **Performance requirements** (latency, throughput)
- **Cost constraints** (API fees vs infrastructure costs)
- **Control needs** (proprietary APIs vs self-hosted)
- **Scale expectations** (100 users vs 1 million users)

---

## The Deployment Landscape

### Your Options at a Glance

```
┌──────────────────────────────────────────────────────────────┐
│                    DEPLOYMENT OPTIONS                        │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│ 1. Cloud APIs (OpenAI, Anthropic, Cohere)                   │
│    ⚡ Fast to start | 💰 Pay per token | 🔒 Proprietary    │
│    → Best for: Prototyping, low-volume apps                 │
│                                                              │
│ 2. HuggingFace Inference API                                 │
│    ⚡ Easy setup | 💰 Free tier + paid | 🔓 Open models    │
│    → Best for: Medium-volume, open-source preferences        │
│                                                              │
│ 3. Local Inference (Ollama)                                  │
│    ⚡ Medium speed | 💰 Hardware cost only | 🔓 Full control│
│    → Best for: Development, privacy-sensitive, offline       │
│                                                              │
│ 4. High-Performance (vLLM, TensorRT-LLM)                     │
│    ⚡ Very fast | 💰 Infrastructure cost | 🔓 Full control  │
│    → Best for: Production, high-volume, latency-critical    │
└──────────────────────────────────────────────────────────────┘
```

### Decision Framework

**Ask yourself:**

1. **Volume?**
   - Low (< 1K requests/day) → Cloud API or HuggingFace
   - Medium (1K-100K/day) → HuggingFace or self-hosted
   - High (> 100K/day) → Self-hosted (vLLM)

2. **Latency Requirements?**
   - Best effort (< 5s) → Any option
   - Real-time (< 1s) → vLLM with GPU
   - Streaming needed → vLLM or cloud API

3. **Privacy/Security?**
   - Public data → Cloud APIs fine
   - Sensitive data → Self-hosted only
   - Compliance (HIPAA, GDPR) → Self-hosted, audited

4. **Budget?**
   - Prototype ($0-100/mo) → HuggingFace free tier
   - Startup ($100-1K/mo) → Cloud APIs or small GPU
   - Production (> $1K/mo) → Optimize based on volume

---

## Learning Objectives

By the end of this section, you'll be able to:

- ✅ **Install** and operate local inference engines (Ollama, vLLM)
- ✅ **Use** OpenAI-compatible interfaces across multiple providers
- ✅ **Compare** throughput, latency, and resource usage scientifically
- ✅ **Implement** authentication, security, and monitoring for production
- ✅ **Build** scalable systems with proper failover and error handling
- ✅ **Choose** the right deployment strategy for your requirements

---

## 3.1 Understanding Model Interfaces

### The OpenAI-Compatible Standard

**Why this matters:** Write code once, deploy anywhere.

The OpenAI API has effectively become the "HTTP of AI." Just as HTTP provided a standard protocol for web servers to communicate regardless of their underlying tech stack (Apache, Nginx, IIS), the OpenAI API specification provides a standard way for applications to talk to LLMs.

This standardization has fueled an ecosystem of middleware. Libraries like LangChain, AutoGPT, and thousands of other tools were built expecting this specific JSON schema. By adopting this standard, open-source projects like vLLM and Ollama instantly made themselves compatible with this vast ecosystem. You can take a complex agent built for GPT-4 and run it on a local Llama 3 model simply by changing a single URL string.

**The power of standardization:**
```python
# Same code works with ALL these providers:
client = OpenAI(api_key="...", base_url="...")

# Just change the base_url:
base_url = "https://api.openai.com/v1"           # OpenAI
base_url = "https://api-inference.huggingface.co/v1"  # HuggingFace
base_url = "http://localhost:11434/v1"           # Ollama (local)
base_url = "http://localhost:8000/v1"            # vLLM (local)
```

**What this means:**
- ✅ Write code once, switch providers without rewriting
- ✅ A/B test different providers easily
- ✅ Implement failover (if OpenAI down, use HuggingFace)
- ✅ Migrate from cloud to self-hosted seamlessly

### Anatomy of the Interface

**Every OpenAI-compatible API has:**

It is crucial to distinguish between the two main endpoints you will encounter:
1.  **Completions (`/v1/completions`)**: The "raw" mode. You feed it a string, and it predicts the next tokens. Useful for code autocompletion or creative writing.
2.  **Chat Completions (`/v1/chat/completions`)**: The "structured" mode. You provide a list of messages with roles (`system`, `user`, `assistant`). This has become the industry standard because it allows for instruction tuning, context management, and safer outputs.

**Common Components:**

1. **Authentication**
   ```python
   api_key="your_secret_key"  # Validates identity
   ```

2. **Endpoint URL**
   ```python
   base_url="https://api.provider.com/v1"  # Where to send requests
   ```

3. **Standard Methods**
   ```python
   client.chat.completions.create()    # Chat/conversation
   client.completions.create()         # Text completion
   client.embeddings.create()          # Vector embeddings
   ```

4. **Common Parameters**
   ```python
   model="gpt-3.5-turbo"     # Which model to use
   temperature=0.7            # Creativity level
   max_tokens=150             # Output length limit
   ```

**The beauty:** Master this once, use it everywhere.

#### Core API Structure

```python
# Universal client pattern that works with multiple providers
from openai import OpenAI

# OpenAI
client = OpenAI(api_key="your-openai-key")

# HuggingFace Inference API
client = OpenAI(
    api_key="your-hf-token",
    base_url="https://api-inference.huggingface.co/v1"
)

# Local Ollama
client = OpenAI(
    api_key="ollama",  # Ollama doesn't require authentication
    base_url="http://localhost:11434/v1"
)

# Local vLLM
client = OpenAI(
    api_key="vllm",  # vLLM doesn't require authentication
    base_url="http://localhost:8000/v1"
)
```

#### Standard Request Format

```python
def create_chat_completion(client, messages, model="gpt-3.5-turbo", **kwargs):
    """Create chat completion with universal parameters."""
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=kwargs.get('temperature', 0.7),
        max_tokens=kwargs.get('max_tokens', 150),
        top_p=kwargs.get('top_p', 1.0),
        frequency_penalty=kwargs.get('frequency_penalty', 0),
        presence_penalty=kwargs.get('presence_penalty', 0),
        stop=kwargs.get('stop', None),
        stream=kwargs.get('stream', False)
    )
    return response
```

## 3.2 HuggingFace Inference Providers

### HuggingFace Inference API

HuggingFace is the "GitHub of AI," hosting hundreds of thousands of models. They offer two primary ways to run these models:

1.  **Serverless Inference API**: A free-to-start, shared infrastructure. It allows you to test models immediately without setting up servers. However, it has rate limits and "cold starts" (latency spikes while the model loads into memory).
2.  **Inference Endpoints**: Dedicated, paid infrastructure. You rent specific GPUs (e.g., an A10G) that stay always-on for your application. This guarantees low latency and security but costs money per hour, regardless of traffic.

#### Basic Usage

```python
from huggingface_hub import InferenceClient

# Initialize client
client = InferenceClient(
    token="your-hf-token",
    model="microsoft/DialoGPT-medium"
)

# Text generation
response = client.text_generation(
    "Hello, how are you?",
    max_new_tokens=50,
    temperature=0.7
)

# Chat completion (OpenAI-compatible)
response = client.chat_completion(
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ],
    max_tokens=50,
    temperature=0.7
)
```

### Inference Providers and Failover

```python
class HuggingFaceProviderManager:
    def __init__(self, token, preferred_providers=None):
        self.token = token
        self.preferred_providers = preferred_providers or ["auto"]
        self.client = InferenceClient(token=token)
    
    def chat_completion_with_failover(self, messages, model, max_retries=3):
        """Attempt chat completion with provider failover."""
        for attempt in range(max_retries):
            try:
                # Try with specified providers
                for provider in self.preferred_providers:
                    try:
                        response = self.client.chat_completion(
                            messages=messages,
                            model=model,
                            provider=provider,
                            max_tokens=150
                        )
                        return response
                    except Exception as e:
                        print(f"Provider {provider} failed: {e}")
                        continue
                
                # Fallback to auto selection
                response = self.client.chat_completion(
                    messages=messages,
                    model=model,
                    provider="auto",
                    max_tokens=150
                )
                return response
                
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                if attempt == max_retries - 1:
                    raise
                time.sleep(2 ** attempt)  # Exponential backoff
        
        raise Exception("All providers failed")
```

### Model Selection and Optimization

```python
class ModelOptimizer:
    def __init__(self, client):
        self.client = client
        self.model_performance_cache = {}
    
    def select_optimal_model(self, task_type, requirements):
        """Select the best model based on task and requirements."""
        model_candidates = self.get_model_candidates(task_type)
        
        for model in model_candidates:
            if self.meets_requirements(model, requirements):
                return model
        
        # Fallback to default
        return self.get_default_model(task_type)
    
    def get_model_candidates(self, task_type):
        """Get list of suitable models for task type."""
        models = {
            'chat': [
                "microsoft/DialoGPT-medium",
                "facebook/blenderbot-400M-distill",
                "google/flan-t5-base"
            ],
            'code': [
                "codellama/CodeLlama-7b-Instruct-hf",
                "WizardLM/WizardCoder-15B-V1.0",
                "Salesforce/codegen-350M-mono"
            ],
            'summarization': [
                "facebook/bart-large-cnn",
                "google/pegasus-xsum",
                "microsoft/DialoGPT-medium"
            ]
        }
        return models.get(task_type, models['chat'])
    
    def benchmark_model(self, model, test_prompts):
        """Benchmark model performance."""
        results = {
            'model': model,
            'latency': [],
            'token_count': [],
            'quality_score': []
        }
        
        for prompt in test_prompts:
            start_time = time.time()
            
            response = self.client.text_generation(
                prompt,
                model=model,
                max_new_tokens=100
            )
            
            latency = time.time() - start_time
            token_count = len(response.split())
            
            results['latency'].append(latency)
            results['token_count'].append(token_count)
            results['quality_score'].append(self.assess_quality(response))
        
        return self.summarize_benchmark(results)
```

## 3.3 Local Inference with Ollama

### Ollama Installation and Setup

Ollama has revolutionized local inference by packaging the complexity of lower-level libraries like `llama.cpp` into a single, user-friendly binary.

Under the hood, Ollama uses **Quantization**. Standard models are released in 16-bit or 32-bit floating-point precision, which requires massive amounts of RAM (e.g., 14GB+ for a 7B model). Ollama automatically uses models compressed to 4-bit integer precision (GGUF format), allowing a 7B parameter model to run comfortably on a laptop with just 8GB of RAM, with negligible loss in intelligence.

```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Start Ollama service
ollama serve

# Pull models
ollama pull llama2
ollama pull mistral
ollama pull codellama

# List available models
ollama list
```

### Ollama API Integration

```python
import requests
import json
from typing import List, Dict, Any, Optional, Union

class OllamaClient:
    """A robust client for the Ollama local inference API."""
    
    def __init__(self, base_url: str = "http://localhost:11434"):
        self.base_url = base_url.rstrip('/')
        self.api_generate = f"{self.base_url}/api/generate"
        self.api_chat = f"{self.base_url}/api/chat"
        self.api_tags = f"{self.base_url}/api/tags"
    
    def list_models(self) -> List[Dict[str, Any]]:
        """List available models on the local Ollama instance."""
        try:
            response = requests.get(self.api_tags, timeout=5)
            response.raise_for_status()
            return response.json().get('models', [])
        except requests.RequestException as e:
            print(f"Error listing models: {e}")
            return []

    def generate_text(
        self, 
        model: str, 
        prompt: str, 
        options: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        Generate text using a specific model.
        
        Args:
            model: Name of the model (e.g., 'llama2')
            prompt: Input text
            options: Additional generation parameters
        """
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False,
            "options": options or {}
        }
        
        try:
            response = requests.post(
                self.api_generate, 
                json=payload, 
                timeout=60
            )
            response.raise_for_status()
            return response.json().get('response', "")
        except requests.RequestException as e:
            raise RuntimeError(f"Ollama generation failed: {e}")

    def chat_completion(
        self, 
        model: str, 
        messages: List[Dict[str, str]], 
        options: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Send a chat request to the model.
        
        Args:
            model: Model name
            messages: List of message dicts [{'role': 'user', 'content': '...'}]
            options: Generation options
        """
        payload = {
            "model": model,
            "messages": messages,
            "stream": False,
            "options": options or {}
        }
        
        try:
            response = requests.post(
                self.api_chat, 
                json=payload, 
                timeout=60
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"Ollama chat failed: {e}")
```

### Ollama Performance Optimization

```python
class OllamaOptimizer:
    def __init__(self, client):
        self.client = client
    
    def optimize_model_loading(self, model_name, gpu_layers=None):
        """Optimize model loading for specific hardware."""
        options = {
            "num_gpu": gpu_layers or self.detect_optimal_gpu_layers(model_name),
            "num_thread": self.get_optimal_thread_count(),
            "context_length": 4096  # Adjust based on available memory
        }
        
        return options
    
    def detect_optimal_gpu_layers(self, model_name):
        """Detect optimal number of GPU layers based on available VRAM."""
        # This is a simplified example - in practice, you'd detect actual GPU memory
        import psutil
        import subprocess
        
        try:
            # Try to detect GPU memory (NVIDIA)
            result = subprocess.run(['nvidia-smi', '--query-gpu=memory.total', '--format=csv,noheader,nounits'], 
                                  capture_output=True, text=True)
            vram_mb = int(result.stdout.strip()) if result.returncode == 0 else 0
            
            # Rough estimation - actual layers depend on model size
            if vram_mb > 8000:  # 8GB+ VRAM
                return 35
            elif vram_mb > 4000:  # 4GB+ VRAM
                return 20
            else:
                return 10
                
        except:
            return 0  # CPU only
    
    def get_optimal_thread_count(self):
        """Get optimal thread count for CPU inference."""
        return min(psutil.cpu_count(logical=False), 8)  # Cap at 8 physical cores
    
    def benchmark_ollama_model(self, model_name, test_prompts):
        """Benchmark Ollama model performance."""
        results = {
            'model': model_name,
            'total_latency': 0,
            'token_throughput': [],
            'memory_usage': [],
            'responses': []
        }
        
        for prompt in test_prompts:
            start_time = time.time()
            
            response = self.client.generate_text(model_name, prompt)
            
            latency = time.time() - start_time
            token_count = len(response.split())
            
            results['total_latency'] += latency
            results['token_throughput'].append(token_count / latency)
            results['responses'].append(response)
            
            # Monitor memory usage if possible
            memory_mb = self.get_memory_usage()
            if memory_mb:
                results['memory_usage'].append(memory_mb)
        
        return self.summarize_benchmark(results)
```

## 3.4 High-Performance Inference with vLLM

### vLLM Installation and Setup

While Ollama optimizes for *usability* on consumer hardware, vLLM optimizes for *throughput* on production server hardware.

The secret sauce of vLLM is **PagedAttention**. Traditional attention mechanisms waste huge amounts of GPU memory due to fragmentation and over-reservation. vLLM manages attention key-value (KV) cache memory like an operating system manages virtual memory—breaking it into non-contiguous pages. This allows vLLM to batch many more simultaneous requests than standard HuggingFace Transformers code, often increasing throughput by 24x.

```bash
# Install vLLM with CUDA support
pip install vllm

# For specific CUDA version
pip install vllm --extra-index-url https://download.pytorch.org/whl/cu124

# Start vLLM server
python -m vllm.entrypoints.openai.api_server \
    --model microsoft/DialoGPT-medium \
    --tensor-parallel-size 1 \
    --gpu-memory-utilization 0.9 \
    --max-model-len 4096 \
    --port 8000
```

### vLLM Client Integration

```python
class VLLMClient:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url
        self.client = OpenAI(
            api_key="vllm",  # vLLM doesn't require authentication
            base_url=f"{base_url}/v1"
        )
    
    def generate_with_vllm(self, prompt, model, **kwargs):
        """Generate text using vLLM with optimized parameters."""
        response = self.client.completions.create(
            model=model,
            prompt=prompt,
            max_tokens=kwargs.get('max_tokens', 150),
            temperature=kwargs.get('temperature', 0.7),
            top_p=kwargs.get('top_p', 1.0),
            top_k=kwargs.get('top_k', -1),
            frequency_penalty=kwargs.get('frequency_penalty', 0),
            presence_penalty=kwargs.get('presence_penalty', 0),
            stop=kwargs.get('stop', None),
            stream=kwargs.get('stream', False),
            best_of=kwargs.get('best_of', 1),
            use_beam_search=kwargs.get('use_beam_search', False)
        )
        
        return response
    
    def chat_with_vllm(self, messages, model, **kwargs):
        """Chat completion with vLLM optimization."""
        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=kwargs.get('max_tokens', 150),
            temperature=kwargs.get('temperature', 0.7),
            top_p=kwargs.get('top_p', 1.0),
            frequency_penalty=kwargs.get('frequency_penalty', 0),
            presence_penalty=kwargs.get('presence_penalty', 0),
            stop=kwargs.get('stop', None),
            stream=kwargs.get('stream', False)
        )
        
        return response
    
    def benchmark_vllm_performance(self, test_prompts, model):
        """Benchmark vLLM performance metrics."""
        results = {
            'model': model,
            'total_requests': len(test_prompts),
            'successful_requests': 0,
            'total_latency': 0,
            'throughput_per_second': [],
            'token_counts': []
        }
        
        start_time = time.time()
        
        for prompt in test_prompts:
            request_start = time.time()
            
            try:
                response = self.generate_with_vllm(prompt, model, max_tokens=100)
                results['successful_requests'] += 1
                
                latency = time.time() - request_start
                results['total_latency'] += latency
                
                # Count tokens (approximate)
                token_count = len(response.choices[0].text.split())
                results['token_counts'].append(token_count)
                results['throughput_per_second'].append(token_count / latency)
                \n            except Exception as e:
n                print(f"Request failed: {e}")
n        \n        total_time = time.time() - start_time\n        results['total_time'] = total_time\n        results['overall_throughput'] = results['successful_requests'] / total_time\n        \n        return results
```

### vLLM Advanced Configuration

```python
class VLLMConfig:
    def __init__(self):
        self.default_config = {
            'tensor_parallel_size': 1,
            'gpu_memory_utilization': 0.9,
            'max_model_len': 4096,
            'dtype': 'auto',
            'quantization': None,
            'seed': 0,
            'swap_space': 4,
            'enforce_eager': False,
            'max_context_len_to_capture': 8192,
            'block_size': 16,
            'max_num_batched_tokens': 4096,
            'max_num_seqs': 256,
            'max_paddings': 256
        }
    
    def get_optimized_config(self, model_name, hardware_specs):
        """Get optimized configuration based on hardware."""
        config = self.default_config.copy()
        
        # Adjust based on GPU memory
        if hardware_specs.get('gpu_memory_gb', 0) > 24:
            config['gpu_memory_utilization'] = 0.95
            config['max_model_len'] = 8192
            config['tensor_parallel_size'] = 2
        elif hardware_specs.get('gpu_memory_gb', 0) > 12:
            config['gpu_memory_utilization'] = 0.9
            config['max_model_len'] = 4096
        else:
            config['gpu_memory_utilization'] = 0.8
            config['max_model_len'] = 2048
        
        # Adjust based on CPU cores
        if hardware_specs.get('cpu_cores', 0) > 16:
            config['max_num_seqs'] = 512
            config['max_num_batched_tokens'] = 8192
        
        return config
    
    def create_deployment_script(self, model_name, config, port=8000):
        """Create deployment script for vLLM server."""
        script = f"""#!/bin/bash
# vLLM deployment script for {model_name}

python -m vllm.entrypoints.openai.api_server \\
    --model {model_name} \\
    --tensor-parallel-size {config['tensor_parallel_size']} \\
    --gpu-memory-utilization {config['gpu_memory_utilization']} \\
    --max-model-len {config['max_model_len']} \\
    --dtype {config['dtype']} \\
    --port {port} \\
    --host 0.0.0.0 \\
    --allow-credentials \\
    --allowed-origins ["*"] \\
    --api-key vllm-secret-key

echo "vLLM server started on port {port}"
"""
        return script
```

## 3.5 Deployment Architecture and Best Practices

### Production Deployment Patterns

```python
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Union
from enum import Enum
import json

class ScalingStrategy(Enum):
    MANUAL = "manual"
    AUTO_CPU = "auto_cpu"
    PREDICTIVE = "predictive"

@dataclass
class SecurityConfig:
    """Security configuration settings."""
    api_key_rotation_days: int = 90
    rate_limit_per_user: int = 100
    allowed_origins: List[str] = field(default_factory=lambda: ["*"])
    enable_audit_logging: bool = True

@dataclass
class InferenceNodeConfig:
    """Hardware and engine configuration for a single node."""
    model_name: str
    engine: str = "vllm"
    gpu_memory_gb: int = 24
    tensor_parallel_size: int = 1
    max_batch_size: int = 32
    
@dataclass
class ProductionSystemConfig:
    """Configuration for a production-grade inference system."""
    service_name: str
    primary_node: InferenceNodeConfig
    replica_count: int = 2
    scaling_strategy: ScalingStrategy = ScalingStrategy.AUTO_CPU
    security: SecurityConfig = field(default_factory=SecurityConfig)
    
    def generate_deployment_manifest(self) -> Dict[str, Any]:
        """
        Generate a deployment configuration (simplified Kubernetes-style).
        """
        return {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "metadata": {"name": self.service_name},
            "spec": {
                "replicas": self.replica_count,
                "strategy": {
                    "type": self.scaling_strategy.value
                },
                "template": {
                    "spec": {
                        "containers": [{
                            "name": "inference-server",
                            "image": f"{self.primary_node.engine}:latest",
                            "resources": {
                                "limits": {
                                    "nvidia.com/gpu": self.primary_node.tensor_parallel_size
                                }
                            },
                            "env": [
                                {"name": "MODEL_NAME", "value": self.primary_node.model_name},
                                {"name": "MAX_BATCH_SIZE", "value": str(self.primary_node.max_batch_size)},
                                {"name": "API_KEY_ROTATION", "value": str(self.security.api_key_rotation_days)}
                            ]
                        }]
                    }
                }
            }
        }

# Usage Example
if __name__ == "__main__":
    config = ProductionSystemConfig(
        service_name="chat-inference-prod",
        primary_node=InferenceNodeConfig(
            model_name="meta-llama/Llama-3-70b-Instruct",
            tensor_parallel_size=4,  # Requires 4 GPUs
            max_batch_size=64
        ),
        replica_count=3,
        scaling_strategy=ScalingStrategy.PREDICTIVE
    )

    print(json.dumps(config.generate_deployment_manifest(), indent=2))
```

## 3.6 Performance Comparison and Benchmarking

### Comprehensive Benchmarking Framework

When benchmarking LLMs, looking at just "seconds per request" is misleading. You must measure two distinct metrics:

1.  **Time to First Token (TTFT):** The latency between sending the request and seeing the first word appear. This determines the "snappiness" of the UI.
2.  **Inter-Token Latency (ITL) / Throughput:** How fast the rest of the words generate. This determines how long the user waits for the full answer.

A system might have great throughput (fast generation) but terrible TTFT (slow queuing), which feels sluggish to the user.

```python
class InferenceBenchmark:
    def __init__(self):
        self.results = {}
        self.test_prompts = self.load_test_prompts()
    
    def load_test_prompts(self):
        """Load diverse test prompts for benchmarking."""
        return [
            "Write a short story about artificial intelligence.",
            "Explain quantum computing in simple terms.",
            "What are the benefits of renewable energy?",
            "How does machine learning work?",
            "Describe the process of photosynthesis.",
            "What are the key principles of software engineering?",
            "Explain the difference between SQL and NoSQL databases.",
            "How do neural networks learn?",
            "What is the importance of data structures?",
            "Describe a sustainable city of the future."
        ]
    
    def benchmark_all_engines(self):
        """Benchmark all available inference engines."""
        engines = [
            ('openai', self.benchmark_openai),
            ('huggingface', self.benchmark_huggingface),
            ('ollama', self.benchmark_ollama),
            ('vllm', self.benchmark_vllm)
        ]
        
        for engine_name, benchmark_func in engines:
            try:
                print(f"Benchmarking {engine_name}...")
                results = benchmark_func()
                self.results[engine_name] = results
            except Exception as e:
                print(f"Failed to benchmark {engine_name}: {e}")
                self.results[engine_name] = {'error': str(e)}
        
        return self.generate_comparison_report()
    
    def benchmark_openai(self):
        """Benchmark OpenAI API."""
        from openai import OpenAI
        client = OpenAI()
        
        results = {
            'latencies': [],
            'token_counts': [],
            'throughput': [],
            'cost_estimates': []
        }
        
        for prompt in self.test_prompts:
            start_time = time.time()
            
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150
            )
            
            latency = time.time() - start_time
            token_count = response.usage.total_tokens
            
            results['latencies'].append(latency)
            results['token_counts'].append(token_count)
            results['throughput'].append(token_count / latency)
            results['cost_estimates'].append(token_count * 0.002 / 1000)  # Approximate cost
        
        return self.summarize_results(results)
    
    def benchmark_huggingface(self):
        """Benchmark HuggingFace Inference API."""
        from huggingface_hub import InferenceClient
        client = InferenceClient()
        
        results = {
            'latencies': [],
            'token_counts': [],
            'throughput': []
        }
        
        for prompt in self.test_prompts:
            start_time = time.time()
            
            response = client.text_generation(
                prompt,
                model="microsoft/DialoGPT-medium",
                max_new_tokens=150
            )
            
            latency = time.time() - start_time
            token_count = len(response.split())
            
            results['latencies'].append(latency)
            results['token_counts'].append(token_count)
            results['throughput'].append(token_count / latency)
        
        return self.summarize_results(results)
    
    def benchmark_ollama(self):
        """Benchmark Ollama local inference."""
        client = OllamaClient()
        
        results = {
            'latencies': [],
            'token_counts': [],
            'throughput': [],
            'memory_usage': []
        }
        
        for prompt in self.test_prompts:
            start_time = time.time()
            
            response = client.generate_text("llama2", prompt)
            
            latency = time.time() - start_time
            token_count = len(response.split())
            
            results['latencies'].append(latency)
            results['token_counts'].append(token_count)
            results['throughput'].append(token_count / latency)
            results['memory_usage'].append(self.get_memory_usage())
        
        return self.summarize_results(results)
    
    def benchmark_vllm(self):
        """Benchmark vLLM local inference."""
        client = VLLMClient()
        
        results = {
            'latencies': [],
            'token_counts': [],
            'throughput': [],
            'memory_usage': []
        }
        
        for prompt in self.test_prompts:
            start_time = time.time()
            
            response = client.generate_with_vllm(
                prompt,
                "microsoft/DialoGPT-medium",
                max_tokens=150
            )
            
            latency = time.time() - start_time
            token_count = len(response.choices[0].text.split())
            
            results['latencies'].append(latency)
            results['token_counts'].append(token_count)
            results['throughput'].append(token_count / latency)
            results['memory_usage'].append(self.get_memory_usage())
        
        return self.summarize_results(results)
    
    def summarize_results(self, results):
        """Summarize benchmarking results."""
        summary = {}
        
        for metric, values in results.items():
            if values and isinstance(values[0], (int, float)):
                summary[metric] = {
                    'mean': np.mean(values),
                    'median': np.median(values),
