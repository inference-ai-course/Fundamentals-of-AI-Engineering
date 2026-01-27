# Week 2 — Part 01: Vector DB fundamentals + minimal metadata schema
 
 ## Overview
 
 A vector DB stores:
 
 - embedding vectors (numbers)
 - ids
 - metadata
 - often raw text (for debugging + citations)
 
 It does not “understand documents”. It retrieves **chunks** based on **vector similarity**.
 
 Your goal this week is not to pick the “best DB”. Your goal is to define a **reliable retrieval contract**:
 
 - you can ingest the same data twice without duplicates
 - you can retrieve and explain why a chunk was retrieved
 - you can trace a retrieved chunk back to its origin (document + location)
 
 ---
 
 ## Mental model: what retrieval actually does
 
 1. You take a text chunk and compute an embedding vector, e.g. `v = embed(text)`.
 2. At query time, you compute `q = embed(query)`.
 3. You retrieve the nearest vectors to `q` under a distance function.
 
 What to verify (so this is debuggable, not magic):
 
 - **During ingestion**: record the embedding model name and ensure every stored vector has a stable `chunk_id` and traceable metadata.
 - **During query**: log the query text, `top_k`, any filters, and the returned `chunk_id` + `doc_id/source` + score.
 - **When debugging**: given a retrieved `chunk_id`, you should be able to locate the original text location (file/url + section/page + chunk index).
 
 Key implication:
 
 - the DB returns what is *numerically close*, not what is *semantically correct*.
 - your job is to design chunking + metadata + query construction so “close” corresponds to “useful”.
 
 ---
 
 ## Embeddings 101 (what is an embedding vector?)
 
 ### Definition (math)
 
 An embedding model is a function:
 
 $$
 f: \text{Text} \rightarrow \mathbb{R}^d
 $$
 
 That maps a piece of text (query or chunk) into a vector of real numbers of dimension $d$.
 
 - $d$ is often a few hundred to a few thousand.
 - Each coordinate is not “human interpretable”; the vector is meaningful as a whole.
 
 ### What the vector represents
 
 The embedding model is trained so that **semantically related texts** end up with vectors that are “close” under a chosen similarity/distance function.
 
 Practical meaning:
 
 - If two texts talk about the same concept, their embeddings should point in similar directions.
 - If they are unrelated, they should be farther apart.
 
 Important caveat:
 
 - embeddings are not perfect “semantic truth”; they reflect the training data/objective of the embedding model.
 
 ---
 
 ## Why similarity search is needed (why not keyword search?)
 
 Keyword search fails when:
 
 - the query uses different wording (synonyms/paraphrase)
 - the query is short and ambiguous
 - the document uses domain terms and the user uses lay terms
 
 Embeddings help because they support **approximate semantic matching**:
 
 - “How do I start the API?” can retrieve chunks about `uvicorn` and `/health` even if the exact words don’t match.
 
 In practice, many production systems use **hybrid retrieval** (BM25 + vectors), but starting with vectors is fine for this course.
 
 ---
 
 ## Dimensionality and geometry (what does “close” mean?)
 
 You can think of embedding vectors as points in a high-dimensional space.
 
 - Cosine similarity compares the **angle** between points (direction).
 - L2 distance compares the **straight-line distance** between points.
 
 In high dimensions, intuition can break ("curse of dimensionality"), which is why real vector DBs use specialized indexing algorithms.
 
 ---
 
 ## Approximate Nearest Neighbor (ANN) intuition
 
 A naïve search compares the query vector to every stored vector (slow at scale).
 
 Vector DBs use ANN indexes (conceptually):
 
 - build a data structure over vectors
 - search it to find “good candidates” quickly
 - return the best approximate neighbors
 
 Practical implication:
 
 - results may not be exact nearest neighbors
 - retrieval is usually good enough and much faster
 
 ---
 
 ## Practical usage tips (avoid common mistakes)
 
 - Use the same embedding model for:
   - document chunks
   - queries
 - Keep `chunk_id` and source metadata stable so you can debug retrieval.
 - Do not set “score thresholds” blindly.
   - thresholds depend on the embedding model and distance metric
   - calibrate using labeled in-KB vs out-of-KB questions
 - Keep a small “retrieval sanity set”:
   - 10 queries that should reliably retrieve known chunks
 
 ---
 
 ## Distance functions (what “similarity” means)
 
 Common options:
 
 - **Cosine similarity** (angle between vectors)
 - **Dot product** (often equivalent if vectors are normalized)
 - **L2 / Euclidean distance**
 
 ---
 
 ## Cosine similarity (math + intuition)
 
 ### Definition
 
 Given two vectors $\mathbf{x}$ and $\mathbf{y}$, cosine similarity is:
 
 $$
 \cos(\theta) = \frac{\mathbf{x} \cdot \mathbf{y}}{\|\mathbf{x}\|_2\,\|\mathbf{y}\|_2}
 $$
 
 Where:
 
 - $\mathbf{x} \cdot \mathbf{y} = \sum_i x_i y_i$ is the dot product
 - $\|\mathbf{x}\|_2 = \sqrt{\sum_i x_i^2}$ is the L2 norm
 
 ### What it means
 
 - Cosine similarity measures how aligned two vectors are.
 - It depends on the **angle** between vectors, not their magnitudes.
 - Range:
   - $+1$: same direction (very similar)
   - $0$: orthogonal (unrelated in the embedding space)
   - $-1$: opposite direction (rare in many embedding spaces, but possible)
 
 ### Why it is useful for embeddings
 
 Embeddings often encode semantic meaning in the **direction** of the vector. Cosine similarity is a simple way to compare direction without letting “vector length” dominate the score.
 
 ### Practical interpretation
 
 - “Higher cosine similarity” means “the embedding model thinks these texts are more semantically related”.
 - You typically use cosine similarity to:
   - rank top-k retrieved chunks
   - set thresholds for refusal/clarification logic (but thresholds must be calibrated)
 
 ---
 
 ## Dot product (math + when it matches cosine)
 
 Dot product is:
 
 $$
 \mathbf{x} \cdot \mathbf{y} = \sum_i x_i y_i
 $$
 
 Relationship to cosine similarity:
 
 - If $\|\mathbf{x}\|_2 = 1$ and $\|\mathbf{y}\|_2 = 1$ (both vectors are L2-normalized), then:
   - $\mathbf{x} \cdot \mathbf{y} = \cos(\theta)$
 
 
 Practical implication:
 
 - Many systems normalize embeddings, so “dot product” and “cosine similarity” behave similarly.
 - If embeddings are not normalized, dot product mixes:
   - direction similarity
   - magnitude effects
 
 ---
 
 ## L2 (Euclidean) distance
 
 L2 distance is:
 
 $$
 d(\mathbf{x}, \mathbf{y}) = \|\mathbf{x} - \mathbf{y}\|_2 = \sqrt{\sum_i (x_i - y_i)^2}
 $$
 
 Interpretation:
 
 - Smaller distance means vectors are closer.
 - Distances are not bounded like cosine similarity; the scale depends on the embedding model.
 
 ---
 
 ## Why normalization matters (practical)
 
 If your embeddings are normalized to unit length:
 
 - cosine similarity and dot product become equivalent
 - scores are easier to reason about across runs
 
 If they are not normalized:
 
 - scores can drift due to magnitude differences
 - thresholds become less stable
 
 The safe habit:
 
 - record whether embeddings are normalized
 - record which distance metric your vector DB uses
 - calibrate any refusal/clarify thresholds using a labeled set
 
 In practice:
 
 - choose what your library defaults to
 - be consistent across ingestion and query
 - record the embedding model name and distance metric in your run notes
 
 ---
 
 ## What to store: ids vs metadata vs documents
 
 Think of a vector store entry as:
 
 - **id**: the stable primary key for upsert/dedup (often your `chunk_id`)
 - **document**: the human-readable text you’ll later pass to the LLM (the chunk)
 - **metadata**: fields you filter on and fields you log for debugging
 
 If you do not store the raw chunk text anywhere, you can still retrieve IDs—but you can’t easily debug or produce citations.
 
 ---
 
 ## Minimal schema (start simple)
 
 Store at least:
 
 - `doc_id`
 - `chunk_id`
 - `source`
 - `text`
 
 Optionally:
 
 - `version`
 - `embedding_model`
 - `page` / `section` / `url`
 - `created_at`
 
 Practical rule:
 
 - anything you might later want to filter by should be metadata
 - anything you might later want to cite should be recoverable via metadata
 
 ---
 
 ## Example metadata: “minimum that stays debuggable”
 
 A minimal metadata payload that works well for most course projects:
 
 ```json
 {
   "doc_id": "fastapi_docs",
   "chunk_id": "fastapi_docs#00012",
   "source": "docs",
   "url": "https://fastapi.tiangolo.com/",
   "section": "Middleware",
   "embedding_model": "text-embedding-3-small"
 }
 ```
 
 Notes:
 
 - `chunk_id` should be unique and stable across re-ingestion.
 - `doc_id` groups chunks from the same document.
 - `url` gives you a user-facing citation.
 
 ---
 
 ## Concrete example: minimal Chroma usage (local)
 
 This is a *minimal* end-to-end example showing what you store and what you get back.
 
 ```python
 import chromadb
 
 client = chromadb.PersistentClient(path="./chroma")
 collection = client.get_or_create_collection(name="kb")
 
 # In a real system you would compute embeddings with an embedding model.
 # Here we assume you already have vectors (lists of floats).
 ids = ["chunk_001", "chunk_002"]
 documents = [
     "FastAPI is a modern, fast web framework for building APIs with Python.",
     "OpenAPI is a specification for describing REST APIs in a machine-readable format."
 ]
 metadatas = [
     {"doc_id": "fastapi", "chunk_id": "fastapi#001", "source": "docs", "url": "https://fastapi.tiangolo.com/"},
     {"doc_id": "openapi", "chunk_id": "openapi#002", "source": "docs", "url": "https://spec.openapis.org/oas/latest.html"},
 ]
 embeddings = [
     [0.1, 0.2, 0.3],
     [0.0, 0.1, 0.4],
 ]
 
 collection.upsert(ids=ids, documents=documents, metadatas=metadatas, embeddings=embeddings)
 
 results = collection.query(query_embeddings=[[0.1, 0.2, 0.25]], n_results=2)
 print(results["ids"])
 print(results["documents"])
 print(results["metadatas"])
 ```
 
 What to notice:
 
 - retrieval returns **documents + metadatas** — that’s what you’ll pass to chat later.
 - you can log `ids` / `chunk_id` / `url` and immediately debug what was returned.
 
 ---
 
 ## What to optimize first
 
 In early RAG systems, quality is usually limited by:
 
 - chunking strategy
 - metadata
 - query construction
 
 Not the DB choice.
 
 ---
 
 ## Debugging checklist (non-negotiable)
 
 When retrieval looks wrong, you should be able to answer:
 
 - what query text was embedded?
 - what filters were applied?
 - what `chunk_id` values were returned?
 - what `doc_id/source/url` did they come from?
 - what was the score / distance?
 
 If you can’t answer those quickly, add the missing fields to metadata/logs.
 
 ---
 
 ## References
 
 - Chroma docs: https://docs.trychroma.com/
 - FAISS (Facebook AI Similarity Search): https://github.com/facebookresearch/faiss
 - Milvus docs: https://milvus.io/docs
 - pgvector: https://github.com/pgvector/pgvector
 - Pinecone RAG overview: https://www.pinecone.io/learn/retrieval-augmented-generation/
 - OpenAI embeddings guide: https://platform.openai.com/docs/guides/embeddings
 - Sentence-Transformers: https://www.sbert.net/
 - Cosine similarity (definition): https://en.wikipedia.org/wiki/Cosine_similarity
 - Dot product (definition): https://en.wikipedia.org/wiki/Dot_product
 - Euclidean distance (definition): https://en.wikipedia.org/wiki/Euclidean_distance
 - BM25 (keyword retrieval): https://en.wikipedia.org/wiki/Okapi_BM25
 - Approximate nearest neighbor (ANN): https://en.wikipedia.org/wiki/Nearest_neighbor_search#Approximate_nearest_neighbor
