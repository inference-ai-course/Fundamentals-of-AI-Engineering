# Week 6 — Part 03: Chunking long text + synthesizing summaries

## Overview

When text is too long for the context window:

1. **Split into chunks**
    - Goal: create pieces that are small enough to fit comfortably in the model context along with instructions and output budget.
    - What to verify: each chunk is non-empty and you can trace a chunk back to its position in the original document (chunk index or character offsets).
    - Practical tip: if the document has strong cross-paragraph references, add overlap between chunks (otherwise “boundary facts” get lost).
2. **Process each chunk**
    - Goal: produce a stable intermediate representation per chunk.
    - What to verify: per-chunk outputs follow a consistent structure so you can combine them later.
    - Example per-chunk schema (simple and robust):
      - `summary_bullets`: 3–5 bullets
      - `key_entities`: list of entities
      - `open_questions`: what is unclear/missing
3. **Synthesize a final summary**
    - Goal: merge the per-chunk outputs into one coherent answer.
    - What to verify: the synthesis step references evidence from the chunk summaries and does not invent new facts.
    - Practical tip: synthesis works better when chunk outputs are short (bounded) and consistent.

Even without a framework, you should understand the pattern.

---

## Pre-study (Self-learn)

Foundamental Course assumes Self-learn is complete. If you need a refresher on context limits and workflow patterns:

- [Pre-study index (Foundamental Course → Self-learn)](../PRESTUDY.md)
- [Self-learn — Chapter 3: AI Engineering Fundamentals](../../self_learn/Chapters/3/Chapter3.md)

Why it matters here (Week 6):

- Chunking is a practical strategy when inputs exceed the context window.
- Use overlap and a synthesis step when cross-chunk references matter.

## Simple chunking utility

```python
from typing import List


def chunk_text(text: str, chunk_size: int = 2000) -> List[str]:
    chunks = []
    i = 0
    while i < len(text):
        chunks.append(text[i : i + chunk_size])
        i += chunk_size
    return chunks
```

Note: chunking by character count is a simple starter, but tokens are what matter for LLM limits. Character chunking can still work for Foundamental Course as long as you keep chunks comfortably small.

---

## Chunking with overlap

Overlap prevents losing information at chunk boundaries:

```python
from typing import List


def chunk_text_overlap(text: str, chunk_size: int = 2000, overlap: int = 200) -> List[str]:
    """
    Split text into overlapping chunks.
    
    Args:
        text: Input text
        chunk_size: Target chunk size in characters
        overlap: Number of characters to overlap between chunks
    
    Returns:
        List of text chunks with overlap
    """
    if len(text) <= chunk_size:
        return [text]
    
    chunks = []
    start = 0
    
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        
        # Move to next chunk with overlap
        start = end - overlap
        
        # Prevent infinite loop on last chunk
        if start + chunk_size >= len(text) and len(chunks) > 1:
            break
    
    return chunks


# Example usage
text = "A" * 10000  # Long text
chunks = chunk_text_overlap(text, chunk_size=2000, overlap=200)
print(f"Created {len(chunks)} chunks with overlap")
```

**When to use overlap:**
- Cross-sentence references are important
- Entities/concepts span chunk boundaries
- Narrative flow matters

**Overlap size guidance:**
- 10% of chunk_size for general text
- 20-30% for dense technical text

---

## Sentence-aware chunking

Avoid breaking mid-sentence:

```python
import re
from typing import List


def chunk_by_sentences(text: str, max_chunk_size: int = 2000) -> List[str]:
    """
    Chunk text at sentence boundaries.
    """
    # Simple sentence split (can be improved with spaCy/NLTK)
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    chunks = []
    current_chunk = []
    current_size = 0
    
    for sentence in sentences:
        sentence_len = len(sentence)
        
        if current_size + sentence_len > max_chunk_size and current_chunk:
            # Save current chunk
            chunks.append(" ".join(current_chunk))
            current_chunk = []
            current_size = 0
        
        current_chunk.append(sentence)
        current_size += sentence_len + 1  # +1 for space
    
    # Don't forget last chunk
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    
    return chunks
```

---

## Per-chunk processing pattern

```python
from typing import List, Dict
import json


def process_chunk(chunk_text: str, chunk_idx: int, call_llm) -> Dict:
    """
    Extract structured info from a single chunk.
    """
    prompt = f"""
Extract key information from this text chunk.

Return ONLY valid JSON with these keys:
- summary_bullets: list of 3-5 bullet points
- key_entities: list of important entities (people, places, organizations)
- main_topics: list of 2-4 main topics

Chunk {chunk_idx + 1}:
{chunk_text}
"""
    
    response = call_llm(prompt)
    
    try:
        data = json.loads(response)
        data["chunk_idx"] = chunk_idx
        return data
    except json.JSONDecodeError:
        return {
            "chunk_idx": chunk_idx,
            "error": "Failed to parse JSON",
            "raw_response": response[:200],
        }


def process_all_chunks(chunks: List[str], call_llm) -> List[Dict]:
    """
    Process all chunks and collect results.
    """
    results = []
    
    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i+1}/{len(chunks)}...")
        result = process_chunk(chunk, i, call_llm)
        results.append(result)
    
    return results
```

---

## Synthesis pattern (concrete)

```python
def synthesize_summaries(chunk_results: List[Dict], call_llm) -> Dict:
    """
    Combine per-chunk summaries into final report.
    """
    # Collect all bullets
    all_bullets = []
    all_entities = set()
    all_topics = set()
    
    for result in chunk_results:
        if "summary_bullets" in result:
            all_bullets.extend(result["summary_bullets"])
        if "key_entities" in result:
            all_entities.update(result["key_entities"])
        if "main_topics" in result:
            all_topics.update(result["main_topics"])
    
    # Create synthesis prompt
    synthesis_input = {
        "n_chunks": len(chunk_results),
        "all_bullets": all_bullets,
        "all_entities": list(all_entities),
        "all_topics": list(all_topics),
    }
    
    prompt = f"""
Synthesize a final summary from these per-chunk extractions.

Input:
{json.dumps(synthesis_input, indent=2)}

Return ONLY valid JSON with:
- executive_summary: 2-3 sentence overview
- key_points: 5-7 most important points
- entities_mentioned: top 10 entities
- overall_themes: 3-5 main themes

Focus on removing redundancy and highlighting the most important information.
"""
    
    response = call_llm(prompt)
    return json.loads(response)
```

---

## Full example: chunk + process + synthesize

```python
from typing import List, Dict
import json


class ChunkingSynthesizer:
    """
    Complete chunking + synthesis pipeline.
    """
    def __init__(self, call_llm, chunk_size: int = 2000, overlap: int = 200):
        self.call_llm = call_llm
        self.chunk_size = chunk_size
        self.overlap = overlap
    
    def run(self, long_text: str) -> Dict:
        """
        Process long text through chunking and synthesis.
        """
        # Step 1: Chunk
        print("Step 1: Chunking...")
        chunks = chunk_text_overlap(long_text, self.chunk_size, self.overlap)
        print(f"Created {len(chunks)} chunks")
        
        # Step 2: Process each chunk
        print("Step 2: Processing chunks...")
        chunk_results = []
        for i, chunk in enumerate(chunks):
            result = process_chunk(chunk, i, self.call_llm)
            chunk_results.append(result)
            
            # Save intermediate results
            with open(f"output/chunk_{i:02d}.json", "w") as f:
                json.dump(result, f, indent=2)
        
        # Step 3: Synthesize
        print("Step 3: Synthesizing...")
        final_summary = synthesize_summaries(chunk_results, self.call_llm)
        
        # Save final output
        with open("output/synthesis.json", "w") as f:
            json.dump(final_summary, f, indent=2)
        
        return {
            "n_chunks": len(chunks),
            "chunk_results": chunk_results,
            "synthesis": final_summary,
        }


# Usage
# synthesizer = ChunkingSynthesizer(call_llm=my_llm_function)
# result = synthesizer.run(very_long_document)
```

---

## Token-aware chunking (advanced)

For precise token budgeting, use a tokenizer:

```python
try:
    import tiktoken
    HAS_TIKTOKEN = True
except ImportError:
    HAS_TIKTOKEN = False


def chunk_by_tokens(text: str, max_tokens: int = 1500, model: str = "gpt-4") -> List[str]:
    """
    Chunk text by token count (requires tiktoken).
    """
    if not HAS_TIKTOKEN:
        # Fallback to character-based estimate
        chars_per_token = 4
        return chunk_text(text, chunk_size=max_tokens * chars_per_token)
    
    enc = tiktoken.encoding_for_model(model)
    tokens = enc.encode(text)
    
    chunks = []
    for i in range(0, len(tokens), max_tokens):
        chunk_tokens = tokens[i:i + max_tokens]
        chunk_text = enc.decode(chunk_tokens)
        chunks.append(chunk_text)
    
    return chunks
```

---

## Practical chunking decision tree

```
Is text < 2000 chars?
├─ Yes → Send as-is
└─ No
   ├─ Is structure important (e.g., code, tables)?
   │  └─ Yes → Use sentence/paragraph-aware chunking
   └─ No → Use simple chunking with 10-20% overlap
   
Are cross-chunk references critical?
├─ Yes → Increase overlap to 30%
└─ No → Use minimal overlap (10%)

Can afford per-chunk API calls?
├─ Yes → Process chunks individually + synthesize
└─ No → Compress aggressively first, then chunk if still too large
```

---

## Practice notebook

For hands-on chunking and synthesis exercises, see:
- **[03_chunking_synthesis.ipynb](./03_chunking_synthesis.ipynb)** - Interactive chunking strategies
- **[practice.ipynb](./practice.ipynb)** - Extended exercises

---

## Self-check

- Can you chunk a 10k character document into manageable pieces?
- Does your chunking preserve sentence boundaries?
- Can you synthesize per-chunk results into a coherent final summary?
- Have you tested with documents that have strong cross-paragraph references?

---

## References

- LangChain text splitters (reference): https://python.langchain.com/docs/how_to/#text-splitters
- tiktoken (OpenAI tokenizer): https://github.com/openai/tiktoken
- spaCy sentence segmentation: https://spacy.io/usage/linguistic-features#sbd
