# Provider Selection and Failover Strategies

## Introduction

Choosing the right inference provider and implementing robust failover mechanisms are crucial for building reliable AI applications. This guide covers provider selection strategies, performance optimization, and resilience patterns.

## Understanding Provider Architecture

### Provider Ecosystem

```
┌─────────────────────────────────────────────────────┐
│           Hugging Face Inference API                │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐         │
│  │Provider 1│  │Provider 2│  │Provider 3│  ...    │
│  │  (AWS)   │  │ (Azure)  │  │  (GCP)   │         │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘         │
│       │             │             │                │
└───────┼─────────────┼─────────────┼────────────────┘
        │             │             │
        ▼             ▼             ▼
   ┌────────┐   ┌────────┐   ┌────────┐
   │ Model  │   │ Model  │   │ Model  │
   │Instance│   │Instance│   │Instance│
   └────────┘   └────────┘   └────────┘
```

### Provider Characteristics

Different providers offer varying:

1. **Performance**
   - Latency (response time)
   - Throughput (requests per second)
   - Consistency (variance in response times)

2. **Availability**
   - Uptime percentage
   - Geographic distribution
   - Maintenance windows

3. **Cost**
   - Per-request pricing
   - Token-based pricing
   - Subscription models

4. **Features**
   - Supported models
   - Maximum context length
   - Streaming support
   - Batch processing

## Provider Selection Strategies

### Strategy 1: Automatic Selection (`provider="auto"`)

**How it works:**
- Platform dynamically selects the best available provider
- Based on current load, availability, and performance metrics
- Automatic failover if selected provider fails

**Code Example:**
```python
from huggingface_hub import InferenceClient
import os

client = InferenceClient(token=os.getenv("HF_TOKEN"))

response = client.text_to_image(
    prompt="A futuristic cityscape at sunset",
    model="stabilityai/stable-diffusion-2-1",
    provider="auto"  # Automatic provider selection
)
```

**When to use:**
- Development and prototyping
- Applications where latency variance is acceptable
- When you want maximum availability
- For load balancing across providers

**Pros:**
- ✅ Highest availability
- ✅ Automatic load balancing
- ✅ No manual provider management
- ✅ Built-in failover

**Cons:**
- ❌ Less predictable latency
- ❌ Harder to debug issues
- ❌ Variable costs
- ❌ Less control over infrastructure

### Strategy 2: Explicit Provider Selection

**How it works:**
- You specify exactly which provider to use
- Direct connection to that provider
- No automatic failover (you must implement it)

**Code Example:**
```python
response = client.text_to_image(
    prompt="A futuristic cityscape at sunset",
    model="stabilityai/stable-diffusion-2-1",
    provider="aws-inference-1"  # Explicit provider
)
```

**When to use:**
- Production applications with strict SLAs
- When you need predictable performance
- For cost optimization (choosing cheapest provider)
- When debugging provider-specific issues

**Pros:**
- ✅ Predictable performance
- ✅ Easier debugging
- ✅ Cost control
- ✅ Compliance requirements (data locality)

**Cons:**
- ❌ No automatic failover
- ❌ Manual provider management
- ❌ Potential for lower availability
- ❌ Need to monitor provider health

### Strategy 3: Hybrid Approach

**How it works:**
- Try explicit provider first
- Fall back to `provider="auto"` on failure
- Best of both worlds

**Code Example:**
```python
def inference_with_hybrid_strategy(client, prompt, model, preferred_provider):
    """Try preferred provider, fall back to auto"""
    try:
        # Try preferred provider first
        response = client.text_to_image(
            prompt=prompt,
            model=model,
            provider=preferred_provider,
            timeout=10
        )
        return response, preferred_provider
    except Exception as e:
        print(f"Preferred provider failed: {e}")
        # Fall back to auto
        response = client.text_to_image(
            prompt=prompt,
            model=model,
            provider="auto",
            timeout=15
        )
        return response, "auto"

# Usage
response, used_provider = inference_with_hybrid_strategy(
    client=client,
    prompt="A serene mountain landscape",
    model="stabilityai/stable-diffusion-2-1",
    preferred_provider="aws-inference-1"
)
print(f"Used provider: {used_provider}")
```

## Implementing Failover

### Basic Failover Pattern

```python
from typing import List, Optional
import time

def inference_with_failover(
    client,
    prompt: str,
    model: str,
    providers: List[str],
    timeout: int = 30
) -> tuple:
    """
    Try multiple providers in sequence until one succeeds.
    
    Returns:
        (response, provider_used)
    """
    last_error = None
    
    for provider in providers:
        try:
            print(f"Trying provider: {provider}")
            start_time = time.time()
            
            response = client.text_to_image(
                prompt=prompt,
                model=model,
                provider=provider,
                timeout=timeout
            )
            
            elapsed = time.time() - start_time
            print(f"✓ Success with {provider} ({elapsed:.2f}s)")
            return response, provider
            
        except Exception as e:
            print(f"✗ Failed with {provider}: {type(e).__name__}")
            last_error = e
            continue
    
    # All providers failed
    raise Exception(f"All providers failed. Last error: {last_error}")

# Usage
providers = ["aws-inference-1", "azure-inference-1", "auto"]
response, used_provider = inference_with_failover(
    client=client,
    prompt="A peaceful garden",
    model="stabilityai/stable-diffusion-2-1",
    providers=providers
)
```

### Advanced Failover with Circuit Breaker

```python
from datetime import datetime, timedelta
from enum import Enum

class CircuitState(Enum):
    CLOSED = "closed"      # Normal operation
    OPEN = "open"          # Failing, don't try
    HALF_OPEN = "half_open"  # Testing if recovered

class CircuitBreaker:
    """
    Circuit breaker pattern for provider failover.
    Prevents repeated calls to failing providers.
    """
    
    def __init__(
        self,
        failure_threshold: int = 3,
        timeout_duration: int = 60,
        success_threshold: int = 2
    ):
        self.failure_threshold = failure_threshold
        self.timeout_duration = timeout_duration
        self.success_threshold = success_threshold
        
        self.failure_count = 0
        self.success_count = 0
        self.state = CircuitState.CLOSED
        self.last_failure_time = None
    
    def call(self, func):
        """Execute function with circuit breaker protection"""
        
        # Check if circuit should transition from OPEN to HALF_OPEN
        if self.state == CircuitState.OPEN:
            if (datetime.now() - self.last_failure_time).seconds >= self.timeout_duration:
                self.state = CircuitState.HALF_OPEN
                self.success_count = 0
            else:
                raise Exception(f"Circuit breaker OPEN for provider")
        
        try:
            result = func()
            self._on_success()
            return result
        except Exception as e:
            self._on_failure()
            raise e
    
    def _on_success(self):
        """Handle successful call"""
        self.failure_count = 0
        
        if self.state == CircuitState.HALF_OPEN:
            self.success_count += 1
            if self.success_count >= self.success_threshold:
                self.state = CircuitState.CLOSED
                print("Circuit breaker CLOSED (recovered)")
    
    def _on_failure(self):
        """Handle failed call"""
        self.failure_count += 1
        self.last_failure_time = datetime.now()
        
        if self.failure_count >= self.failure_threshold:
            self.state = CircuitState.OPEN
            print(f"Circuit breaker OPEN (too many failures)")

# Usage
class ProviderManager:
    def __init__(self, client):
        self.client = client
        self.breakers = {}  # provider -> CircuitBreaker
    
    def get_breaker(self, provider: str) -> CircuitBreaker:
        if provider not in self.breakers:
            self.breakers[provider] = CircuitBreaker()
        return self.breakers[provider]
    
    def inference(self, prompt: str, model: str, providers: List[str]):
        """Try providers with circuit breaker protection"""
        for provider in providers:
            breaker = self.get_breaker(provider)
            
            try:
                def call():
                    return self.client.text_to_image(
                        prompt=prompt,
                        model=model,
                        provider=provider
                    )
                
                response = breaker.call(call)
                return response, provider
                
            except Exception as e:
                print(f"Provider {provider} failed: {e}")
                continue
        
        raise Exception("All providers failed")

# Example usage
manager = ProviderManager(client)
response, used = manager.inference(
    prompt="A sunset over mountains",
    model="stabilityai/stable-diffusion-2-1",
    providers=["provider-1", "provider-2", "auto"]
)
```

## Performance Monitoring and Comparison

### Benchmarking Providers

```python
import time
from typing import Dict, List
from dataclasses import dataclass
from statistics import mean, stdev

@dataclass
class ProviderMetrics:
    provider: str
    latencies: List[float]
    success_count: int
    failure_count: int
    
    @property
    def avg_latency(self) -> float:
        return mean(self.latencies) if self.latencies else 0
    
    @property
    def std_latency(self) -> float:
        return stdev(self.latencies) if len(self.latencies) > 1 else 0
    
    @property
    def success_rate(self) -> float:
        total = self.success_count + self.failure_count
        return (self.success_count / total * 100) if total > 0 else 0

def benchmark_providers(
    client,
    prompts: List[str],
    model: str,
    providers: List[str]
) -> Dict[str, ProviderMetrics]:
    """
    Benchmark multiple providers with the same prompts.
    
    Returns:
        Dictionary mapping provider name to metrics
    """
    results = {p: ProviderMetrics(p, [], 0, 0) for p in providers}
    
    for provider in providers:
        print(f"\nBenchmarking {provider}...")
        
        for i, prompt in enumerate(prompts, 1):
            try:
                start = time.perf_counter()
                
                response = client.text_to_image(
                    prompt=prompt,
                    model=model,
                    provider=provider,
                    timeout=30
                )
                
                latency = time.perf_counter() - start
                results[provider].latencies.append(latency)
                results[provider].success_count += 1
                
                print(f"  Prompt {i}/{len(prompts)}: {latency:.2f}s ✓")
                
            except Exception as e:
                results[provider].failure_count += 1
                print(f"  Prompt {i}/{len(prompts)}: Failed ({type(e).__name__}) ✗")
            
            # Small delay between requests
            time.sleep(1)
    
    return results

def print_benchmark_results(results: Dict[str, ProviderMetrics]):
    """Print formatted benchmark results"""
    print("\n" + "="*70)
    print("BENCHMARK RESULTS")
    print("="*70)
    
    for provider, metrics in results.items():
        print(f"\nProvider: {provider}")
        print(f"  Success Rate:    {metrics.success_rate:.1f}%")
        print(f"  Avg Latency:     {metrics.avg_latency:.2f}s")
        print(f"  Std Deviation:   {metrics.std_latency:.2f}s")
        print(f"  Successful:      {metrics.success_count}")
        print(f"  Failed:          {metrics.failure_count}")

# Usage example
prompts = [
    "A serene mountain landscape",
    "A futuristic city at night",
    "A peaceful garden with flowers"
]

providers_to_test = ["aws-inference-1", "auto"]

results = benchmark_providers(
    client=client,
    prompts=prompts,
    model="stabilityai/stable-diffusion-2-1",
    providers=providers_to_test
)

print_benchmark_results(results)
```

## Timeout Configuration

### Recommended Timeouts by Task

| Task Type | Connect Timeout | Read Timeout | Total Timeout |
|-----------|----------------|--------------|---------------|
| Text Generation (short) | 5s | 10s | 15s |
| Text Generation (long) | 5s | 30s | 35s |
| Image Generation | 5s | 45s | 50s |
| Video Generation | 10s | 120s | 130s |
| Embedding | 5s | 10s | 15s |

### Implementing Timeouts

```python
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def create_session_with_retries(
    retries: int = 3,
    backoff_factor: float = 0.3,
    status_forcelist: tuple = (500, 502, 504)
):
    """Create requests session with retry logic"""
    session = requests.Session()
    
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    
    return session

# Usage
session = create_session_with_retries()

response = session.post(
    url="https://api-inference.huggingface.co/models/...",
    json=payload,
    headers=headers,
    timeout=(5, 30)  # (connect, read)
)
```

## Cost Optimization

### Choosing Cost-Effective Providers

```python
from typing import Dict

# Provider pricing (example - check actual pricing)
PROVIDER_COSTS = {
    "aws-inference-1": 0.02,      # $ per request
    "azure-inference-1": 0.025,
    "gcp-inference-1": 0.018,
    "auto": 0.022  # Average cost
}

def select_cheapest_provider(
    providers: List[str],
    costs: Dict[str, float] = PROVIDER_COSTS
) -> str:
    """Select the cheapest available provider"""
    available = [p for p in providers if p in costs]
    if not available:
        return "auto"
    return min(available, key=lambda p: costs[p])

# Usage
providers = ["aws-inference-1", "azure-inference-1", "gcp-inference-1"]
cheapest = select_cheapest_provider(providers)
print(f"Selected provider: {cheapest} (${PROVIDER_COSTS[cheapest]}/request)")
```

## Summary and Best Practices

### Provider Selection Decision Tree

```
Start
  │
  ├─ Need predictable latency? ──YES──> Use explicit provider
  │                                      + Implement manual failover
  │
  ├─ Need maximum availability? ──YES──> Use provider="auto"
  │                                      + Accept latency variance
  │
  ├─ Need cost optimization? ──YES──> Benchmark providers
  │                                   + Select cheapest with acceptable performance
  │
  └─ Production deployment? ──YES──> Use hybrid strategy
                                     + Circuit breaker pattern
                                     + Comprehensive monitoring
```

### Checklist

- ✅ Understand your latency requirements
- ✅ Benchmark providers for your specific use case
- ✅ Implement failover for production applications
- ✅ Configure appropriate timeouts
- ✅ Use circuit breakers to prevent cascading failures
- ✅ Monitor provider performance continuously
- ✅ Consider cost vs. performance trade-offs
- ✅ Document provider selection rationale

## Next Steps

- Practice provider comparison in the Jupyter notebooks
- Implement failover strategies in your own projects
- Explore advanced optimization techniques
