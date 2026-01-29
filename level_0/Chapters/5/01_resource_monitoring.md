# Resource Monitoring and Troubleshooting

**Duration**: 2 hours  
**Prerequisites**: Python 3.10+, PyTorch 2.6.0+, CUDA 12.4+

---

## Table of Contents

1. [Introduction](#introduction)
2. [System Resource Monitoring](#system-resource-monitoring)
3. [Common Errors and Solutions](#common-errors-and-solutions)
4. [Logging and Debugging](#logging-and-debugging)
5. [Performance Profiling](#performance-profiling)
6. [Retry Strategies and Error Handling](#retry-strategies-and-error-handling)
7. [Best Practices](#best-practices)

---

## Introduction

Resource monitoring and troubleshooting are critical skills for developing and deploying AI systems. This guide covers essential techniques for monitoring GPU, CPU, and memory resources, diagnosing common errors, and implementing robust error handling strategies.

### Why Resource Monitoring Matters

- **Performance Optimization**: Identify bottlenecks in your AI pipeline
- **Cost Management**: Avoid wasting computational resources
- **Reliability**: Detect issues before they cause failures
- **Debugging**: Understand system behavior during errors

---

## System Resource Monitoring

### GPU Monitoring

#### Using nvidia-smi

The NVIDIA System Management Interface (nvidia-smi) is the primary tool for monitoring GPU resources.

**Basic Usage**:
```bash
# Display current GPU status
nvidia-smi

# Continuous monitoring (update every 1 second)
nvidia-smi -l 1

# Monitor specific metrics
nvidia-smi --query-gpu=timestamp,name,temperature.gpu,utilization.gpu,utilization.memory,memory.total,memory.free,memory.used --format=csv -l 1
```

**Key Metrics**:
- **GPU Utilization**: Percentage of time GPU kernels are executing
- **Memory Utilization**: Percentage of memory bandwidth being used
- **Memory Usage**: Total, used, and free GPU memory
- **Temperature**: GPU temperature (watch for thermal throttling)
- **Power Draw**: Current power consumption

#### Using Python Libraries

**pynvml (Python NVIDIA Management Library)**

**Documentation:** https://pypi.org/project/nvidia-ml-py/

```python
import pynvml

# Initialize NVML
pynvml.nvmlInit()

# Get device count
device_count = pynvml.nvmlDeviceGetCount()

# Query GPU 0
handle = pynvml.nvmlDeviceGetHandleByIndex(0)

# Get GPU name
name = pynvml.nvmlDeviceGetName(handle)

# Get memory info
mem_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
print(f"Total memory: {mem_info.total / 1024**3:.2f} GB")
print(f"Used memory: {mem_info.used / 1024**3:.2f} GB")
print(f"Free memory: {mem_info.free / 1024**3:.2f} GB")

# Get utilization
utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)
print(f"GPU Utilization: {utilization.gpu}%")
print(f"Memory Utilization: {utilization.memory}%")

# Cleanup
pynvml.nvmlShutdown()
```

**PyTorch GPU Monitoring**:
```python
import torch

# Check CUDA availability
print(f"CUDA Available: {torch.cuda.is_available()}")
print(f"CUDA Version: {torch.version.cuda}")
print(f"PyTorch Version: {torch.__version__}")

# Get device information
if torch.cuda.is_available():
    device_count = torch.cuda.device_count()
    print(f"Number of GPUs: {device_count}")
    
    for i in range(device_count):
        print(f"\nGPU {i}: {torch.cuda.get_device_name(i)}")
        print(f"Memory Allocated: {torch.cuda.memory_allocated(i) / 1024**3:.2f} GB")
        print(f"Memory Reserved: {torch.cuda.memory_reserved(i) / 1024**3:.2f} GB")
        print(f"Max Memory Allocated: {torch.cuda.max_memory_allocated(i) / 1024**3:.2f} GB")
```

### CPU Monitoring

**Using psutil**

**Documentation:** https://psutil.readthedocs.io/

```python
import psutil

# CPU usage per core
cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
print(f"CPU Usage per core: {cpu_percent}")

# Overall CPU usage
print(f"Overall CPU Usage: {psutil.cpu_percent(interval=1)}%")

# CPU frequency
cpu_freq = psutil.cpu_freq()
print(f"CPU Frequency: {cpu_freq.current:.2f} MHz")

# Number of cores
print(f"Physical cores: {psutil.cpu_count(logical=False)}")
print(f"Logical cores: {psutil.cpu_count(logical=True)}")
```

### Memory Monitoring

**System Memory**:
```python
import psutil

# Get memory information
mem = psutil.virtual_memory()
print(f"Total Memory: {mem.total / 1024**3:.2f} GB")
print(f"Available Memory: {mem.available / 1024**3:.2f} GB")
print(f"Used Memory: {mem.used / 1024**3:.2f} GB")
print(f"Memory Usage: {mem.percent}%")

# Swap memory
swap = psutil.swap_memory()
print(f"Swap Total: {swap.total / 1024**3:.2f} GB")
print(f"Swap Used: {swap.used / 1024**3:.2f} GB")
```

### Disk I/O Monitoring

```python
import psutil

# Disk usage
disk = psutil.disk_usage('/')
print(f"Total Disk: {disk.total / 1024**3:.2f} GB")
print(f"Used Disk: {disk.used / 1024**3:.2f} GB")
print(f"Free Disk: {disk.free / 1024**3:.2f} GB")
print(f"Disk Usage: {disk.percent}%")

# Disk I/O statistics
disk_io = psutil.disk_io_counters()
print(f"Read Count: {disk_io.read_count}")
print(f"Write Count: {disk_io.write_count}")
print(f"Read Bytes: {disk_io.read_bytes / 1024**3:.2f} GB")
print(f"Write Bytes: {disk_io.write_bytes / 1024**3:.2f} GB")
```

---

## Common Errors and Solutions

### 1. Authentication Failures

**Problem**: Cannot access remote resources, APIs, or private repositories.

**Common Causes**:
- Expired or invalid API tokens
- Incorrect credentials
- Missing environment variables
- Insufficient permissions

**Solutions**:
```python
import os
from huggingface_hub import login

# Check if token exists
hf_token = os.getenv("HF_TOKEN")
if not hf_token:
    raise ValueError("HF_TOKEN environment variable not set")

# Login to Hugging Face
login(token=hf_token)

# Verify authentication
from huggingface_hub import whoami
try:
    user_info = whoami()
    print(f"Logged in as: {user_info['name']}")
except Exception as e:
    print(f"Authentication failed: {e}")
```

**Best Practices**:
- Use environment variables for sensitive credentials
- Implement token refresh mechanisms
- Log authentication attempts (without exposing credentials)
- Use secure secret management tools

### 2. Port Conflicts

**Problem**: Service cannot start because port is already in use.

**Detection**:
```python
import socket

def check_port(port):
    """Check if a port is available"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('localhost', port))
    sock.close()
    return result != 0  # True if port is available

# Check if port 8000 is available
if check_port(8000):
    print("Port 8000 is available")
else:
    print("Port 8000 is in use")
```

**Solutions**:
```bash
# Find process using a port (Linux)
lsof -i :8000

# Kill process by port
kill -9 $(lsof -t -i:8000)

# Or use fuser
fuser -k 8000/tcp
```

**Python Solution**:
```python
import subprocess

def find_available_port(start_port=8000, max_attempts=100):
    """Find an available port starting from start_port"""
    for port in range(start_port, start_port + max_attempts):
        if check_port(port):
            return port
    raise RuntimeError("No available ports found")

# Use dynamic port assignment
port = find_available_port()
print(f"Using port: {port}")
```

### 3. Dependency and Version Issues

**Problem**: Package version conflicts, missing dependencies, or incompatible versions.

**Detection**:
```python
import sys
import torch
import warnings

def check_dependencies():
    """Check if dependencies meet requirements"""
    issues = []
    
    # Check Python version
    if sys.version_info < (3, 10):
        issues.append(f"Python 3.10+ required, found {sys.version}")
    
    # Check PyTorch version
    torch_version = tuple(map(int, torch.__version__.split('.')[:2]))
    if torch_version < (2, 6):
        issues.append(f"PyTorch 2.6.0+ required, found {torch.__version__}")
    
    # Check CUDA version
    if torch.cuda.is_available():
        cuda_version = torch.version.cuda
        cuda_major = int(cuda_version.split('.')[0])
        if cuda_major < 12:
            issues.append(f"CUDA 12.4+ required, found {cuda_version}")
    else:
        warnings.warn("CUDA not available")
    
    return issues

# Run dependency check
issues = check_dependencies()
if issues:
    for issue in issues:
        print(f"❌ {issue}")
else:
    print("✅ All dependencies meet requirements")
```

**Solutions**:
- Use virtual environments (venv, conda)
- Pin exact versions in requirements.txt
- Use dependency management tools (poetry, pipenv)
- Document system requirements clearly

### 4. GPU/CUDA Mismatch

**Problem**: PyTorch cannot find CUDA, or CUDA version mismatch.

**Common Errors**:
```
RuntimeError: CUDA error: no kernel image is available for execution on the device
RuntimeError: Found no NVIDIA driver on your system
AssertionError: Torch not compiled with CUDA enabled
```

**Diagnostic Script**:
```python
import torch
import subprocess

def diagnose_cuda():
    """Comprehensive CUDA diagnostics"""
    print("="*50)
    print("CUDA Diagnostics")
    print("="*50)
    
    # Check PyTorch CUDA
    print(f"\n1. PyTorch Configuration:")
    print(f"   PyTorch Version: {torch.__version__}")
    print(f"   CUDA Available: {torch.cuda.is_available()}")
    print(f"   CUDA Version (PyTorch): {torch.version.cuda}")
    print(f"   cuDNN Version: {torch.backends.cudnn.version()}")
    
    # Check NVIDIA Driver
    print(f"\n2. NVIDIA Driver:")
    try:
        result = subprocess.run(['nvidia-smi'], capture_output=True, text=True)
        print(result.stdout.split('\n')[2])  # Driver version line
    except FileNotFoundError:
        print("   ❌ nvidia-smi not found - NVIDIA driver may not be installed")
    
    # Check CUDA Toolkit
    print(f"\n3. CUDA Toolkit:")
    try:
        result = subprocess.run(['nvcc', '--version'], capture_output=True, text=True)
        print(result.stdout.split('\n')[-2])  # Version line
    except FileNotFoundError:
        print("   ❌ nvcc not found - CUDA toolkit may not be installed")
    
    # Check GPU devices
    if torch.cuda.is_available():
        print(f"\n4. GPU Devices:")
        for i in range(torch.cuda.device_count()):
            print(f"   GPU {i}: {torch.cuda.get_device_name(i)}")
            print(f"   Compute Capability: {torch.cuda.get_device_capability(i)}")
    
    print("="*50)

diagnose_cuda()
```

**Solutions**:
- Install matching CUDA version for PyTorch
- Update NVIDIA drivers
- Reinstall PyTorch with correct CUDA version:
  ```bash
  pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
  ```

### 5. Out of Memory (OOM) Errors

**Problem**: GPU or system memory exhausted.

**Detection and Prevention**:
```python
import torch
import gc

def get_gpu_memory_usage():
    """Get current GPU memory usage"""
    if torch.cuda.is_available():
        allocated = torch.cuda.memory_allocated() / 1024**3
        reserved = torch.cuda.memory_reserved() / 1024**3
        return allocated, reserved
    return 0, 0

def clear_gpu_memory():
    """Clear GPU memory cache"""
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
        torch.cuda.synchronize()

# Monitor memory during training
class MemoryMonitor:
    def __init__(self):
        self.max_allocated = 0
    
    def update(self):
        if torch.cuda.is_available():
            current = torch.cuda.max_memory_allocated() / 1024**3
            self.max_allocated = max(self.max_allocated, current)
            return current
        return 0
    
    def reset(self):
        if torch.cuda.is_available():
            torch.cuda.reset_peak_memory_stats()
        self.max_allocated = 0

# Usage
monitor = MemoryMonitor()
# ... training code ...
print(f"Max GPU memory: {monitor.update():.2f} GB")
```

**Solutions**:
- Reduce batch size
- Use gradient accumulation
- Enable mixed precision training (FP16/BF16)
- Use gradient checkpointing
- Clear cache periodically

---

## Logging and Debugging

### Structured Logging

**Best Practices**:
```python
import logging
import sys
from datetime import datetime

# Configure logging
def setup_logger(name, log_file=None, level=logging.INFO):
    """Setup logger with file and console handlers"""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Format
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler (optional)
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger

# Usage
logger = setup_logger('training', 'training.log')
logger.info("Training started")
logger.warning("Learning rate adjusted")
logger.error("Out of memory error")
```

### Context Logging for Training

```python
import torch
from contextlib import contextmanager
import time

@contextmanager
def log_time(logger, operation):
    """Context manager for timing operations"""
    start = time.time()
    try:
        yield
    finally:
        duration = time.time() - start
        logger.info(f"{operation} took {duration:.2f} seconds")

# Usage
logger = setup_logger('training')

with log_time(logger, "Data loading"):
    # Load data
    pass

with log_time(logger, "Model forward pass"):
    # Forward pass
    pass
```

---

## Performance Profiling

### PyTorch Profiler

```python
import torch
import torch.profiler as profiler

def train_step(model, data, target):
    output = model(data)
    loss = torch.nn.functional.cross_entropy(output, target)
    loss.backward()
    return loss

# Profile training
with profiler.profile(
    activities=[
        profiler.ProfilerActivity.CPU,
        profiler.ProfilerActivity.CUDA,
    ],
    record_shapes=True,
    profile_memory=True,
    with_stack=True
) as prof:
    for _ in range(10):
        train_step(model, data, target)

# Print profiler results
print(prof.key_averages().table(sort_by="cuda_time_total", row_limit=10))

# Export trace for visualization
prof.export_chrome_trace("trace.json")
```

### Memory Profiling

```python
from torch.profiler import profile, ProfilerActivity

with profile(
    activities=[ProfilerActivity.CPU, ProfilerActivity.CUDA],
    profile_memory=True,
    record_shapes=True
) as prof:
    # Your code here
    model(input_data)

print(prof.key_averages().table(
    sort_by="self_cuda_memory_usage", 
    row_limit=10
))
```

---

## Retry Strategies and Error Handling

### Exponential Backoff

```python
import time
import random
from functools import wraps

def retry_with_backoff(max_retries=3, base_delay=1, max_delay=60, exponential_base=2):
    """Decorator for retrying functions with exponential backoff"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    retries += 1
                    if retries >= max_retries:
                        raise
                    
                    # Exponential backoff with jitter
                    delay = min(base_delay * (exponential_base ** retries), max_delay)
                    jitter = random.uniform(0, delay * 0.1)
                    sleep_time = delay + jitter
                    
                    print(f"Attempt {retries} failed: {e}")
                    print(f"Retrying in {sleep_time:.2f} seconds...")
                    time.sleep(sleep_time)
            
            return None
        return wrapper
    return decorator

# Usage
@retry_with_backoff(max_retries=5)
def download_model(model_name):
    from transformers import AutoModel
    return AutoModel.from_pretrained(model_name)
```

### Circuit Breaker Pattern

```python
from enum import Enum
import time

class CircuitState(Enum):
    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"

class CircuitBreaker:
    def __init__(self, failure_threshold=5, timeout=60):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.failures = 0
        self.last_failure_time = None
        self.state = CircuitState.CLOSED
    
    def call(self, func, *args, **kwargs):
        if self.state == CircuitState.OPEN:
            if time.time() - self.last_failure_time > self.timeout:
                self.state = CircuitState.HALF_OPEN
            else:
                raise Exception("Circuit breaker is OPEN")
        
        try:
            result = func(*args, **kwargs)
            self.on_success()
            return result
        except Exception as e:
            self.on_failure()
            raise e
    
    def on_success(self):
        self.failures = 0
        self.state = CircuitState.CLOSED
    
    def on_failure(self):
        self.failures += 1
        self.last_failure_time = time.time()
        if self.failures >= self.failure_threshold:
            self.state = CircuitState.OPEN

# Usage
breaker = CircuitBreaker(failure_threshold=3, timeout=30)

def call_api():
    return breaker.call(some_api_call)
```

---

## Best Practices

### 1. Monitoring Checklist

- [ ] Set up GPU monitoring for all training jobs
- [ ] Log resource utilization at regular intervals
- [ ] Monitor temperature and power consumption
- [ ] Track memory usage trends
- [ ] Set up alerts for resource exhaustion

### 2. Error Handling Checklist

- [ ] Implement retry logic for network operations
- [ ] Use circuit breakers for external services
- [ ] Log all errors with full context
- [ ] Implement graceful degradation
- [ ] Set up error alerting

### 3. Performance Optimization

- [ ] Profile code before optimization
- [ ] Focus on bottlenecks identified by profiling
- [ ] Monitor memory leaks
- [ ] Use mixed precision when possible
- [ ] Implement efficient data loading

### 4. Production Readiness

- [ ] Comprehensive error handling
- [ ] Structured logging
- [ ] Resource monitoring
- [ ] Health checks
- [ ] Graceful shutdown

---

## Summary

This chapter covered essential techniques for monitoring and troubleshooting AI systems:

1. **Resource Monitoring**: GPU, CPU, memory, and disk monitoring using various tools
2. **Common Errors**: Authentication failures, port conflicts, dependency issues, GPU mismatches, OOM errors
3. **Logging**: Structured logging and debugging techniques
4. **Profiling**: Performance and memory profiling with PyTorch
5. **Error Handling**: Retry strategies, exponential backoff, circuit breakers

Practice these concepts in the accompanying Jupyter notebook: [resource_monitoring_practice.ipynb](./01_resource_monitoring_practice.ipynb)

---

## Additional Resources

- [PyTorch Profiler Documentation](https://pytorch.org/tutorials/recipes/recipes/profiler_recipe.html)
- [NVIDIA NVML Documentation](https://developer.nvidia.com/nvidia-management-library-nvml)
- [psutil Documentation](https://psutil.readthedocs.io/)
- [Python Logging Best Practices](https://docs.python.org/3/howto/logging.html)
