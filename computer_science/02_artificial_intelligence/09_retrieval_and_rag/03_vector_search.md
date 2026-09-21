# Vector Search: từ Nearest Neighbor tới ANN Index

Khi corpus có hàng triệu embedding vectors, naive search so sánh query với mọi vector có cost:

\[
O(Nd)
\]

với `N` vectors và dimension `d`. Exact brute-force có thể ổn với corpus nhỏ hoặc GPU batch, nhưng scale lớn thường cần **Approximate Nearest Neighbor (ANN / 근사 최근접 이웃)**.

ANN hy sinh một phần exactness để giảm latency/memory cost.

## Exact Nearest Neighbor

Given query `q`, tìm:

\[
\arg\max_d s(q,d)
\]

Nếu dùng cosine/dot product, exact search compute score với toàn bộ corpus.

Exact search useful cho baseline vì cho upper bound recall của index. Nếu ANN recall thấp hơn nhiều exact search, index config có vấn đề.

## Why Approximation Works

RAG thường không cần exact mathematically nearest vector; cần candidate set relevant. Nếu index trả almost-nearest vectors với recall cao nhưng nhanh hơn 100x, trade-off rất đáng giá.

Quality metric của ANN thường là **recall against exact nearest neighbors**, khác retrieval relevance recall. Hai layers cần phân biệt:

```text
ANN recall: index có tìm được vector neighbors exact không?
Retrieval recall: những neighbors đó có chứa relevant evidence không?
```

## HNSW

**Hierarchical Navigable Small World (HNSW)** xây graph nhiều tầng. Search bắt đầu ở sparse upper layers để move nhanh gần query region, sau đó refine ở dense lower layer.

Mental model:

```text
highway layer → đi xa nhanh
local roads   → tìm neighbor gần
```

Important parameters thường gồm:

- `M`: số connections per node;
- `efConstruction`: search breadth khi build;
- `efSearch`: search breadth khi query.

Higher values thường improve recall nhưng tăng memory/build/query cost.

HNSW mạnh cho low-latency dynamic search nhưng index memory có thể lớn.

## IVF

**Inverted File Index (IVF)** cluster vector space thành coarse cells bằng centroids. Query chỉ search một số nearest clusters.

```text
all vectors
→ cluster into cells
→ query selects nprobe cells
→ exact/quantized search within selected cells
```

`nprobe` lớn → recall cao hơn, latency lớn hơn.

IVF phù hợp large-scale search và thường kết hợp Product Quantization.

## Product Quantization

**PQ** compress vector bằng chia dimensions thành subspaces và quantize mỗi subvector bằng codebook.

Thay lưu float vector đầy đủ, index lưu compact codes. Distance được approximate từ lookup tables.

Trade-off:

```text
memory ↓
cache efficiency ↑
accuracy ↓ somewhat
```

PQ rất quan trọng khi billions vectors hoặc memory cost dominate.

## Scalar Quantization

Float32 vector có thể quantize sang int8/float16. Simpler hơn PQ và giữ accuracy tốt trong many settings.

Nhưng quantization effect cần benchmark trên actual embedding distribution.

## Metric Choice

ANN index phải match similarity used by embedding model:

```text
cosine similarity
inner product
L2 distance
```

Nếu vectors normalized, cosine và inner product ranking equivalent. Nếu không, magnitude affects inner product.

Sai metric có thể degrade retrieval nghiêm trọng.

## Filtering Problem

Enterprise RAG cần filters:

```text
tenant_id = X
access_level <= current_user
version = current
language = ko
```

Filter có thể apply pre-filter hoặc post-filter.

**Post-filter**: ANN retrieve top-k rồi remove unauthorized/nonmatching items. Nếu nhiều items bị remove, result count/recall giảm.

**Pre-filter**: restrict candidate space trước/within search. Implementation phức tạp hơn nhưng correctness tốt hơn.

Security filters không được best-effort.

## Index Build vs Update

Một số indexes optimized batch build, others dynamic insert/delete tốt hơn. Knowledge base có frequent updates cần consider update semantics.

Deletion đôi khi là tombstone + background rebuild, không immediate physical removal.

Nếu legal deletion requirement nghiêm ngặt, cần hiểu storage/index lifecycle.

## Freshness

Index có thể lag source database. Pipeline:

```text
source update
→ ingestion event
→ parse/chunk
→ embed
→ index update
```

Latency giữa source và search là **freshness lag**. RAG “latest” chỉ tốt nếu ingestion SLA tốt.

## Sharding

Large corpus có thể shard by tenant, language, region hoặc hash. Query fan-out across shards rồi merge rankings.

Semantic sharding giảm search space nhưng risk route sai query.

## Replication

Read-heavy vector search cần replicas để scale throughput/high availability. Index version synchronization trở thành operational concern.

## Top-k và efSearch

Top-k là số results user wants. `efSearch`/search breadth là internal candidate exploration. Muốn top-10 không có nghĩa internal search chỉ inspect 10 nodes.

Recall tuning cần separate these knobs.

## Batch Search

Embedding queries có thể batch, và vector engines có SIMD/GPU acceleration. Throughput workload khác low-latency single-query workload.

Benchmark phải match traffic pattern.

## Index Recall Benchmark

Procedure:

```text
sample queries
→ brute-force exact top-k
→ ANN top-k
→ compare overlap
```

Nếu ANN recall@10 = 0.98, 98% exact neighbors recovered on average. Nhưng still need semantic relevance evaluation.

## High-Dimensional Geometry

In high dimensions, distance distributions can concentrate. Good learned embeddings try create useful local structure, but ANN algorithms still face curse of dimensionality.

Better representation often improves search more than endlessly tuning index.

## Vector Search vs Vector Database

Vector search là algorithm/index problem. **Vector database** adds persistence, metadata, CRUD, filtering, replication, transactions/consistency, APIs và operations.

Không nên coi HNSW = vector database.

## Mental Model

> ANN index là **performance layer** quanh embedding geometry. Nó không tạo semantic quality; nó cố tìm gần đúng những neighbors mà embedding space đã định nghĩa.

## Common Misconceptions

### “Approximate search làm RAG hallucinate”

ANN approximation có thể miss evidence, nhưng root cause phải tách ANN recall khỏi retriever/model quality.

### “HNSW luôn tốt nhất”

Không. Memory, scale, update pattern và hardware khác nhau làm IVF/PQ/brute-force đôi khi tốt hơn.

### “Filter sau search luôn ổn”

Không nếu filter selective hoặc security-critical.

## Knowledge Connection

Vector search dựa [High-dimensional Linear Algebra](../01_mathematical_foundations/01_linear_algebra_for_ai.md) và [Embeddings](./02_embeddings_for_retrieval.md).

Xem tiếp: [Vector Databases](./04_vector_databases.md).