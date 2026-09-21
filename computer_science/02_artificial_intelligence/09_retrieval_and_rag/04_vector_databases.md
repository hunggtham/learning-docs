# Vector Databases trong RAG

**Vector Database (벡터 데이터베이스)** là data system được thiết kế để lưu, index và truy vấn vectors cùng metadata ở scale production. Nó không chỉ là một ANN algorithm. Production vector DB thường phải giải đồng thời persistence, filtering, updates, multi-tenancy, replication, access control và observability.

## Record Model

Một indexed record thường có dạng:

```json
{
  "id": "chunk_123",
  "vector": [0.01, -0.42, ...],
  "text": "...",
  "metadata": {
    "document_id": "policy_v5",
    "tenant_id": "A",
    "version": 5,
    "language": "ko"
  }
}
```

Trong nhiều systems, raw text có thể ở object store/database khác và vector DB chỉ lưu pointer + metadata.

## Source of Truth

Vector DB không nên mặc định là authoritative source. Thường source of truth là document store, CMS, relational DB hoặc object storage.

Pipeline:

```text
Source of Truth
→ ingestion
→ parse/chunk
→ embedding
→ vector index
```

Nếu vector record corrupt/lost, system nên có khả năng rebuild từ source.

## CRUD và Reindexing

Create/update document không chỉ là update một row. Một document có thể tạo nhiều chunks. Update content có thể làm chunk boundaries thay đổi.

Safe pattern thường dùng immutable versioned chunks:

```text
new document version
→ generate new chunks/index
→ atomically mark new version active
→ retire old version
```

Điều này giảm window nơi search mix old/new chunks.

## Metadata Filters

Metadata hỗ trợ constraints mà vector similarity không encode reliable:

```text
product
version
region
language
created_at
security_scope
tenant
```

Filter semantics nên được design như database query, không phải optional prompt hint.

## Multi-Tenancy

Nếu nhiều customers dùng same vector infra, tenant isolation rất quan trọng.

Hai designs:

```text
shared index + strict tenant filter
separate namespace/index per tenant
```

Shared index efficient nhưng filter bug có thể leak cross-tenant data. Separate indexes isolate tốt hơn nhưng operational overhead lớn.

## Authorization

User access có thể phụ thuộc group/document ACL. Retrieval layer phải filter trước khi evidence tới LLM.

Không được retrieve secret chunk rồi yêu cầu LLM “đừng tiết lộ”. Khi secret đã vào context, security boundary đã bị vi phạm.

## Consistency

Vector DB update có thể asynchronous. Sau write, query ngay có thể chưa thấy record tùy consistency model.

Application cần biết:

```text
strong/read-after-write?
eventual consistency?
index refresh interval?
```

Đặc biệt important cho knowledge updates và deletion.

## Deletion Semantics

Delete source document cần propagate tới chunks/index/cache. Nếu chỉ delete text nhưng vector vẫn searchable, model có thể expose stale/deleted content.

Data lineage cần track:

```text
source_id → chunk_ids → embedding version → index records
```

## Index Versioning

Khi upgrade embedding model, new vectors không compatible với old space. Good architecture tạo new index version:

```text
index_v1 = embedding_model_A
index_v2 = embedding_model_B
```

Backfill, shadow evaluate, switch traffic, then retire old index.

## Hybrid Search

Nhiều vector databases support sparse/BM25 + dense vector query. Nếu không, application có thể query separate lexical engine và vector engine rồi fuse rankings.

“Vector database” không có nghĩa system chỉ nên dùng vectors.

## Storage Layout

Raw float vectors large. Systems có thể store compressed representations in index và full vectors separately for reranking/reconstruction.

Trade-offs depend on:

- corpus size;
- query rate;
- memory budget;
- update frequency;
- recall requirement.

## Replication và High Availability

Production search needs replicas/shards. Replica lag, leader failover và index rebuild time ảnh hưởng availability.

RAG architecture nên có fallback khi vector service unavailable: lexical search, cached answer, graceful error hoặc no-answer — không fabricate.

## Backups

Nếu index rebuildable from source, backup strategy có thể focus source + pipeline config. Nhưng rebuild billion-vector index có thể mất nhiều thời gian, nên index snapshots vẫn valuable.

## Observability

Monitor không chỉ CPU/RAM. Retrieval-specific metrics:

```text
query latency p50/p95/p99
zero-result rate
filter selectivity
index size
freshness lag
ANN recall sample
top-k score distribution
embedding/version mix
```

Score distribution shift có thể signal query distribution change hoặc model mismatch.

## Cost Model

Vector DB cost gồm memory, storage, compute, network và embedding ingestion cost.

Large `d`, many chunks và aggressive replicas tăng cost nhanh.

Chunking strategy therefore has direct infrastructure economics.

## Managed vs Self-Hosted

Managed services reduce operations but may introduce data residency/vendor lock-in. Self-hosted gives control but requires index tuning, scaling, backups and upgrades.

Decision should come from security/SLA/team capability, not trend.

## SQL Databases with Vector Extensions

Relational databases increasingly support vector columns/indexes. Với corpus vừa và metadata joins quan trọng, keeping vectors in existing DB can simplify architecture.

Dedicated vector DB hữu ích khi vector search scale/latency/features dominate.

Không cần thêm new database chỉ vì RAG tutorial dùng một cái.

## Cache

Embedding cache tránh recompute duplicate query vectors. Retrieval-result cache useful cho repeated stable queries nhưng invalidation hard when knowledge changes.

Cache key cần include model/index/filter versions.

## Disaster Scenario: Mixed Embedding Versions

Nếu ingestion job upgrade embedding model nhưng query service vẫn model cũ, vectors share dimension maybe same nhưng semantic space khác. Search silently fails.

Metadata/version checks nên prevent mixing incompatible embeddings.

## Mental Model

> Vector DB là **search-oriented data infrastructure** cho learned representations. Semantic relevance đến từ embedding/retrieval model; correctness, security và freshness đến từ data/system architecture xung quanh.

## Common Misconceptions

### “Vector DB là requirement của mọi RAG”

Không. Small corpus có thể brute-force; SQL/Elasticsearch may suffice.

### “Lưu vector rồi không cần source document nữa”

Sai. Vector là lossy representation và không phải provenance source.

### “Tenant filter trong prompt là đủ”

Không. Authorization phải enforced trước retrieval/context assembly.

## Knowledge Connection

Vector database kết nối ANN search, database systems, security và data engineering.

Xem tiếp: [RAG Fundamentals](./05_rag_fundamentals.md).