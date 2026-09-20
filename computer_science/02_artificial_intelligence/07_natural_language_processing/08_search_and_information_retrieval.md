# Search và Information Retrieval trong NLP

Information Retrieval (IR / 정보 검색 / truy xuất thông tin) trả lời câu hỏi: với một query, trong một collection lớn, documents/passages nào relevant nhất? Đây là nền trực tiếp của search engine và RAG.

IR khác classification ở chỗ output là **ranking over large corpus**. System cần candidate generation cực nhanh rồi scoring/reranking chính xác hơn.

## Inverted Index

Lexical search core data structure:

```text
term → postings list of documents/positions
```

Ví dụ:

```text
"transformer" → [doc2, doc10, doc42]
```

Query không scan mọi documents. Inverted index makes sparse retrieval scalable.

Positions enable phrase/proximity search.

## Boolean Retrieval

Queries combine terms:

```text
AI AND safety
transformer NOT electrical
```

Precise but no ranking by graded relevance and vocabulary mismatch problematic.

## TF-IDF

Term important if frequent in document but rare corpus-wide.

\[
TFIDF(t,d)=TF(t,d)IDF(t)
\]

IDF often:

\[
IDF(t)=\log\frac{N}{DF(t)}
\]

Sparse document/query vectors can use cosine similarity.

## BM25

BM25 is strong lexical ranking baseline:

\[
score(q,d)=\sum_{t\in q}IDF(t)
\frac{f(t,d)(k_1+1)}
{f(t,d)+k_1(1-b+b|d|/avgdl)}
\]

It introduces term-frequency saturation and document-length normalization.

Important intuition:

- repeated term helps but diminishing returns;
- long document gets normalization;
- rare query terms matter more.

BM25 remains highly competitive for exact names, codes, identifiers and rare terminology.

## Vocabulary Mismatch

Query `car repair` may need document `automobile maintenance`. Lexical overlap weak.

Dense retrieval uses learned embeddings to capture semantic relation.

## Dense Retrieval

Bi-encoder:

\[
q=f_\theta(query),\quad d=g_\theta(document)
\]

score:

\[
s(q,d)=q^Td
\]

Precompute document embeddings. Query vector performs nearest-neighbor search.

This trades exact lexical matching for learned semantic geometry.

## Approximate Nearest Neighbor

Exact scan millions vectors expensive. ANN indexes approximate top neighbors.

Common concepts:

- HNSW graph search;
- IVF coarse partitions;
- Product Quantization compression;
- flat exact search baseline.

ANN has recall/latency/memory trade-off. “Vector database” wraps indexing, filtering, persistence, metadata and operations around these mechanisms.

## HNSW intuition

Hierarchical Navigable Small World graph connects vectors; search greedily navigates from coarse upper layers to dense lower layer.

Hyperparameters control graph degree/construction/search breadth. Higher search effort improves recall but increases latency.

## Hybrid Retrieval

Lexical and dense methods have complementary strengths.

```text
BM25: exact keyword, code, rare names
Dense: paraphrase, semantic similarity
```

Hybrid combine scores/candidates. Reciprocal Rank Fusion (RRF):

\[
RRF(d)=\sum_r\frac1{k+rank_r(d)}
\]

avoids raw score calibration across retrievers.

## Reranking

First-stage retriever optimizes recall + speed. Cross-encoder reranker jointly reads query/document and assigns relevance score.

Pipeline:

```text
Corpus millions
→ BM25/dense retrieve top 100
→ cross-encoder rerank
→ top 5–20
```

This cascade concentrates expensive computation on small candidate set.

## Query Expansion

Add synonyms/related terms to bridge mismatch. Classical pseudo-relevance feedback uses top docs terms.

Modern LLM can rewrite/expand query, but may drift intent. Original query should remain and expansion evaluated.

## Chunking

RAG retrieval often indexes passages, not whole documents.

Trade-off:

- small chunk → precise, less context;
- large chunk → more context, diluted embedding/relevance;
- overlap → preserve boundaries but duplicate results/cost.

Chunk should preserve semantic units: headings, paragraphs, tables/code blocks when possible.

## Parent–Child Retrieval

Index small child chunks for precise matching but return larger parent section for context.

```text
small chunk embedding → match
parent section         → send LLM
```

This separates retrieval granularity from generation context granularity.

## Metadata Filtering

Relevance is not only text similarity. Need constraints:

```text
user permission
date range
language
document type
project/customer
version/status
```

Metadata filtering before/within ANN is critical enterprise RAG. Retrieving unauthorized document is security failure even if model never quotes it.

## Freshness

Index update pipeline determines knowledge freshness. New document must be parsed, chunked, embedded, indexed and propagated.

Search system should track document version and deletion. “RAG has real-time knowledge” only if ingestion is real-time enough.

## Relevance Labels

Training/evaluation query-document relevance can be:

- human judgments;
- click logs;
- synthetic pairs;
- implicit behavior.

Click data has position/exposure bias. Documents not shown cannot be clicked, creating feedback loop.

## Retrieval Metrics

Recall@K:

\[
\frac{relevant\ docs\ retrieved\ in\ topK}{all\ relevant\ docs}
\]

MRR focuses first relevant rank:

\[
MRR=\frac1N\sum_q\frac1{rank_q}
\]

NDCG handles graded relevance and rank discounts.

For RAG, **retrieval recall** often critical: if correct evidence never retrieved, generator cannot ground answer from it.

## Retrieval vs Answer Quality

Good retrieval doesn't guarantee answer; LLM may ignore/misread context.

Bad retrieval caps answer quality. Therefore evaluate separately:

```text
retrieval quality
context quality
generation faithfulness
end-to-end answer correctness
```

## Search as Multi-Stage System

Modern architecture:

```text
Query understanding/rewrite
↓
Candidate retrieval (lexical + dense)
↓
Metadata/filter
↓
Reranking
↓
Diversity/deduplication
↓
Context assembly
↓
Answer / result UI
```

Optimizing only embedding model ignores most system.

## Mental Model

> Retrieval is a funnel: cheap broad methods maximize chance relevant evidence survives early stages; expensive precise methods improve ordering later.

## Common Misconceptions

### “Dense retrieval replaces BM25”

Hybrid often wins because exact lexical signals remain important.

### “Vector DB understands documents”

It indexes vectors/metadata; semantic quality comes from embedding/training/chunking.

### “Cosine highest document should go directly to LLM”

Similarity ≠ relevance/authority/freshness; reranking/filtering help.

### “If RAG answer wrong, LLM is hallucinating”

Root cause may be retrieval miss, bad chunk, stale index or context assembly.

## Knowledge Connection

IR connects [k-NN](../04_machine_learning/07_knn_and_distance_based_learning.md), [Contextual Embeddings](./04_contextual_embeddings.md), classical [Search](../02_search_reasoning_and_planning/00_state_space_and_search.md) and directly prepares `09_retrieval_and_rag/`.