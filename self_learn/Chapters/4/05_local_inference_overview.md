# Local Inference Endpoints — Ollama and vLLM

## Overview

This section covers local inference deployment using two popular frameworks: **Ollama** and **vLLM**. You'll learn how to run large language models on your own hardware, compare performance characteristics, and build production-ready local inference services.

**Duration:** 6 hours

## Learning Objectives

By the end of this section, you will be able to:

1. **Install and Operate Ollama**
   - Use Ollama CLI commands (pull, run, list, serve)
   - Access Ollama's REST API and OpenAI-compatible endpoints
   - Understand memory and throughput considerations

2. **Install and Run vLLM**
   - Deploy vLLM in offline and service modes
   - Configure the OpenAI-compatible server
   - Optimize for throughput and latency

3. **Compare Performance**
   - Benchmark Ollama vs vLLM for your use cases
   - Measure tokens/second, latency, and memory usage
   - Select the appropriate tool for your requirements

## Prerequisites

- Python 3.10 or higher
- CUDA 12.4 or higher (for GPU acceleration)
- PyTorch 2.6.0 or higher
- At least 8GB VRAM for smaller models (16GB+ recommended)
- Basic understanding of REST APIs and HTTP servers

## Section Structure

This section includes:

1. **[Inference Engines](06_inference_engines.md)** - Complete guide to Ollama and vLLM

## Coding Practice

Jupyter notebooks for hands-on learning:

- **[Ollama Practice](05_ollama_practice.ipynb)** - Install and test Ollama

## Suggested Learning Path

1. **Ollama Basics** (90-120 minutes)
   - Read Ollama documentation
   - Install and configure Ollama
   - Complete Ollama practice notebook
   - Test REST and OpenAI-compatible APIs

2. **vLLM Basics** (90-120 minutes)
   - Read vLLM documentation
   - Install and configure vLLM
   - Complete vLLM practice notebook
   - Start OpenAI-compatible server

3. **Performance Analysis** (60-90 minutes)
   - Run benchmarking notebook
   - Compare throughput and latency
   - Analyze memory usage
   - Document findings

4. **Production Considerations** (60 minutes)
   - Review deployment best practices
   - Plan scaling strategies
   - Implement monitoring
   - Consider security implications

## Assessment Checkpoints

You should be able to demonstrate:

- ✅ Install and start both Ollama and vLLM
- ✅ Pull and run models using CLI commands
- ✅ Send requests to REST APIs using Python
- ✅ Use OpenAI-compatible clients with local endpoints
- ✅ Measure and compare throughput (tokens/second)
- ✅ Measure and compare latency (response time)
- ✅ Monitor memory usage during inference
- ✅ Explain trade-offs between Ollama and vLLM
- ✅ Choose the appropriate tool for specific use cases

## Common Pitfalls to Avoid

- **Port Conflicts**: Ensure services use different ports or stop existing services
- **Model Size**: Choose models that fit in available VRAM/RAM
- **Resource Monitoring**: Track GPU/CPU usage during tests
- **API Compatibility**: Verify OpenAI-compatible payload formats
- **Timeout Configuration**: Set appropriate timeouts for model loading
- **Concurrent Requests**: Understand batching and throughput limits

## Hardware Recommendations

### Minimum Requirements
- **CPU**: 4+ cores
- **RAM**: 16GB
- **GPU**: 8GB VRAM (for 7B models)
- **Storage**: 50GB free space

### Recommended Setup
- **CPU**: 8+ cores
- **RAM**: 32GB+
- **GPU**: 16GB+ VRAM (for 13B models)
- **Storage**: 100GB+ SSD

### Optimal Setup
- **CPU**: 16+ cores
- **RAM**: 64GB+
- **GPU**: 24GB+ VRAM (for 30B+ models)
- **Storage**: 500GB+ NVMe SSD

## Model Size Guide

| Model Size | VRAM Required | Example Models | Use Case |
|------------|---------------|----------------|----------|
| 1-3B | 4-6GB | Llama-3.2-3B, Phi-3-mini | Testing, mobile |
| 7B | 8-12GB | Llama-3.1-7B, Mistral-7B | General purpose |
| 13B | 16-20GB | Llama-2-13B | High quality |
| 30B+ | 24GB+ | Llama-3.1-70B (quantized) | Production |

## Additional Resources

- [Ollama Official Documentation](https://github.com/ollama/ollama)
- [vLLM Documentation](https://docs.vllm.ai/)
- [Model Quantization Guide](https://huggingface.co/docs/transformers/quantization)
- [GPU Memory Optimization](https://huggingface.co/docs/transformers/perf_train_gpu_one)

## Next Steps

After completing this section:
- Build a local chatbot application
- Deploy a production inference service
- Explore model quantization techniques
- Implement load balancing for multiple GPUs
