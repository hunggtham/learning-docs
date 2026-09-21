# Embeddings for Retrieval

**Embedding retrieval** biến query và document thành vectors sao cho geometry của vector space phản ánh relevance hữu ích. Điều quan trọng là embedding không có meaning “tự nhiên”; meaning của distance đến từ training objective và data.

## From Text to Vector

Một encoder tạo:

\[
z=f_\theta(text)\in\mathbb{R}^d
\]

Query và document được encode thành `q`, `d`. Retrieval dùng similarity:

\[
s(q,d)=q^Td
\]

hoặc cosine similarity:

\[
\cos(q,d)=\frac{q^Td}{\|q\|\|d\|}
\]

Nếu vectors được L2-normalize, dot product và cosine ranking giống nhau.

## What Does the Vector Represent?

Embedding có thể encode topical similarity, intent, semantic equivalence hoặc task-specific relevance tùy training. Một general sentence embedding model không nhất thiết tối ưu cho question→answer retrieval.

Ví dụ:

```text
query: "How do I reset my password?"
positive doc: "Password recovery steps"
```

Training nên đưa query-document positive pair kiểu này để geometry phản ánh retrieval intent.

## Pooling

Transformer tạo token representations. Để có one vector cho whole text, encoder cần pooling:

- CLS token;
- mean pooling;
- weighted pooling;
- learned pooling.

Pooling strategy ảnh hưởng retrieval quality. Mean pooling simple nhưng có thể dilute key token trong long chunk.

## Normalization

Embedding normalization thường giúp score stable:

\[
\hat z=\frac{z}{\|z\|}
\]

Nhưng không phải mọi model được train với same assumption. Documentation của embedding model cần được follow.

## Dimensionality

Dimension lớn cho capacity cao hơn nhưng tăng storage/index cost. Nếu có `N` vectors dimension `d` float32:

\[
storage\approx N\cdot d\cdot 4\ bytes
\]

1 triệu vectors × 1536 dimensions ≈ 6.1 GB chỉ cho raw vectors, chưa tính index/metadata.

Dimension reduction hoặc quantized index có thể giảm cost.

## Query/Document Prefixes

Một số embedding models được train với prefixes như:

```text
query: ...
passage: ...
```

Prefix không cosmetic; nó signal role trong asymmetric training. Bỏ prefix có thể giảm performance.

## Chunk Embedding

RAG thường embed chunks thay whole documents. Chunk vector phải represent enough local semantic context để query match.

Nếu chunk chỉ chứa một table row không header, embedding mất semantics. Ingestion có thể prepend section title/document metadata trước embedding.

## Metadata in Embedding vs Metadata as Filter

Có thể concatenate metadata vào text trước embedding:

```text
Title: Refund Policy
Product: Card
Content: ...
```

Nhưng deterministic constraints như access level, tenant hoặc version nên vẫn dùng filters. Không nên hy vọng vector geometry enforce authorization.

## Hard Negatives

Retriever fine-tuning cần hard negatives. Ví dụ query hỏi policy cho `credit card`, negative là nearly identical policy cho `debit card`.

Model học distinction critical mà general semantic similarity dễ bỏ qua.

## In-Batch Negatives

Trong contrastive training, other positives trong same batch thường dùng làm negatives. Efficient nhưng có risk false negatives nếu two queries share relevant docs.

Batch composition ảnh hưởng learning signal.

## Matryoshka / Truncatable Embeddings

Một số models train để prefix dimensions vẫn usable, cho phép truncate vector để trade quality for storage/latency. Đây là architecture/training property, không áp dụng arbitrary cho mọi embedding vector.

## Multilingual Embeddings

Multilingual embedding maps semantically similar text across languages vào common space:

```text
"hoàn tiền"
"refund"
"환불"
```

có thể gần nhau.

Nhưng cross-language retrieval cần eval riêng vì language imbalance trong training có thể tạo quality gap.

## Code Embeddings

Code search có semantics khác prose. Function signature, identifiers và behavior matter. Domain-specific code embedding model thường tốt hơn generic text embedding.

## Similarity Thresholds

Một common mistake là hard-code `cosine > 0.8 = relevant`. Score distribution depends model, corpus và query type.

Threshold phải calibrate trên labeled retrieval data.

Top-k ranking thường more portable than absolute threshold, nhưng abstention/use-no-evidence decisions vẫn cần calibration.

## Embedding Drift

Khi đổi embedding model, old and new vectors thường không nằm trong same space. Query encoded bằng new model không nên search old vectors unless model explicitly compatible.

Migration cần re-embed corpus hoặc dual-index transition.

## Versioning

Store metadata:

```text
embedding_model_version
chunker_version
source_version
created_at
```

Nếu retrieval regression xảy ra, team cần biết index được tạo bằng pipeline nào.

## Privacy

Embedding không nên được assume irreversible. Vector có thể leak semantic/content information. Access control cho vector DB cần giống source data sensitivity.

## Evaluation

Embedding quality nên đo retrieval task:

```text
Recall@k
MRR
nDCG
hard-negative discrimination
multilingual slices
```

Visualization đẹp của vectors không đủ evidence production quality.

## Mental Model

> Embedding là **learned coordinate system cho một retrieval objective**. Distance có meaning vì model được train để relevant things align, không vì vector tự mang semantic truth.

## Common Misconceptions

### “Embedding giống database hash của sentence”

Không. Similar inputs can be near, and vector is lossy representation.

### “Higher dimension luôn better”

Không. Cost tăng và useful signal phụ thuộc training.

### “Metadata filter có thể thay bằng embedding”

Không cho security/version constraints.

## Knowledge Connection

Xem [Linear Algebra](../01_mathematical_foundations/01_linear_algebra_for_ai.md), [LLM Embeddings](../08_large_language_models/02_embeddings_and_semantic_space.md), và tiếp theo [Vector Search](./03_vector_search.md).