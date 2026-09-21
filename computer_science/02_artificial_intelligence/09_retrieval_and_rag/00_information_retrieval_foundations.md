# Information Retrieval Foundations

**Information Retrieval (IR / 정보 검색 / truy xuất thông tin)** nghiên cứu cách tìm những document hoặc item liên quan từ một collection lớn dựa trên một query. RAG hiện đại dựa trực tiếp trên IR, vì trước khi LLM có thể trả lời dựa trên external knowledge, system phải tìm đúng evidence.

## Retrieval không phải Database Lookup

Database lookup thường có key hoặc predicate chính xác:

```sql
SELECT * FROM policy WHERE policy_id = 'A-102';
```

Information retrieval xử lý query mơ hồ hơn:

```text
"quy định hoàn tiền khi hủy dịch vụ"
```

Không có exact key rõ ràng. System phải estimate relevance giữa query và documents.

## Corpus, Query, Relevance

Một retrieval problem có:

```text
Corpus D = {d1, d2, ..., dn}
Query q
Relevance score s(q, d)
```

System rank documents theo score.

Điểm khó là **relevance không phải property tuyệt đối của document**. Nó phụ thuộc query, user intent, time và task.

Một document nói đúng chủ đề nhưng không chứa answer cụ thể có thể topical relevant nhưng answer-irrelevant.

## Boolean Retrieval

Cách đơn giản nhất dùng term matching:

```text
refund AND cancellation
```

Boolean retrieval rất precise khi vocabulary ổn định, nhưng brittle với synonym, morphology và natural-language query.

Nó vẫn hữu ích trong enterprise search vì filter constraints thường deterministic:

```text
product = eKYC
AND version = current
AND language = ko
```

Modern retrieval thường kết hợp semantic ranking với metadata filters.

## Inverted Index

Search engine không scan mọi document cho mỗi query. Nó xây **inverted index (역색인)**:

```text
term → list of documents containing term
```

Ví dụ:

```text
refund → [doc2, doc8, doc20]
cancel → [doc2, doc3, doc20]
```

Query chỉ cần inspect postings lists liên quan.

Đây là foundation của lexical search như BM25.

## Term Frequency và Document Frequency

Một term xuất hiện nhiều trong document có thể quan trọng cho document đó, nhưng term phổ biến trong gần mọi document mang ít discriminative value.

TF-IDF captures intuition:

\[
TFIDF(t,d)=TF(t,d)\cdot IDF(t)
\]

với:

\[
IDF(t)=\log\frac{N}{df(t)}
\]

`df(t)` là số documents chứa term.

Rare informative terms được weight cao hơn common words.

## BM25

BM25 là lexical ranking function rất mạnh. Simplified form:

\[
score(q,d)=\sum_{t\in q} IDF(t)\cdot \frac{tf(t,d)(k_1+1)}{tf(t,d)+k_1(1-b+b\frac{|d|}{avgdl})}
\]

Nó thêm saturation cho term frequency và length normalization.

Mental model:

> Một term quan trọng nếu nó match query, hiếm trong corpus và xuất hiện đủ mạnh trong document, nhưng repetition không được reward vô hạn.

BM25 vẫn competitive trong enterprise RAG, đặc biệt cho product codes, IDs, legal terms và exact names.

## Precision và Recall trong Retrieval

**Precision** hỏi: trong items retrieved, bao nhiêu thực sự relevant?

\[
Precision=\frac{Relevant\ Retrieved}{Retrieved}
\]

**Recall** hỏi: trong tất cả relevant items, retrieve được bao nhiêu?

\[
Recall=\frac{Relevant\ Retrieved}{All\ Relevant}
\]

RAG thường ưu tiên recall ở first-stage retrieval rồi dùng reranker để tăng precision.

Nếu correct evidence không vào candidate set, LLM phía sau không thể sử dụng nó.

## Ranking Metrics

### Recall@k

Có relevant document trong top `k` không?

### MRR

Mean Reciprocal Rank reward relevant result xuất hiện sớm:

\[
RR=\frac{1}{rank_{first\ relevant}}
\]

### nDCG

Normalized Discounted Cumulative Gain cho phép graded relevance và discount rank thấp.

RAG retrieval eval không nên chỉ đo final answer, vì final model có thể đoán đúng dù retrieval sai.

## Query Intent

Một query có thể là:

- navigational: tìm document cụ thể;
- factual: tìm fact;
- exploratory: nghiên cứu topic;
- transactional: tìm information để hành động.

Retrieval strategy nên khác nhau. Query “API response code EKYC001” cần exact lexical match hơn query “lỗi xác thực khuôn mặt thường do đâu?”.

## Vocabulary Mismatch

Lexical search fail khi query và document dùng different words:

```text
query: "nghỉ việc"
document: "chấm dứt hợp đồng lao động"
```

Dense retrieval giải một phần bằng learned semantic representations.

Nhưng semantic retrieval có thể fail exact identifiers. Vì vậy hybrid retrieval rất quan trọng.

## Document Granularity

Search whole document có thể quá coarse; search sentence quá fine. RAG thường index chunks.

Granularity trade-off:

```text
small chunk → precise match nhưng thiếu context
large chunk → đủ context nhưng noisy và tốn tokens
```

Chunking là retrieval design, không chỉ preprocessing convenience.

## Query Expansion

System có thể expand query bằng synonyms, aliases hoặc generated alternatives.

Ví dụ:

```text
"신분증 진위 확인"
→ ID verification
→ identity document authenticity
→ 신분증 검증
```

Expansion tăng recall nhưng có thể introduce drift.

## Filters và Metadata

Metadata filters rất powerful:

```text
version=current
country=KR
product=mobile_banking
access_level<=user_clearance
```

Embedding similarity không nên replace explicit constraints.

## Retrieval as Candidate Generation

Modern search thường two-stage:

```text
fast retriever → top 100 candidates
expensive reranker → top 5–10
```

First stage optimize recall/latency. Reranker optimize fine relevance.

## IR và RAG

RAG pipeline fundamentally asks:

```text
Can we retrieve evidence needed to answer q?
Can generator use that evidence faithfully?
```

Hai questions cần eval riêng.

## Mental Model

> Information Retrieval là **search over imperfect relevance**, không phải exact lookup. RAG quality bị giới hạn bởi evidence candidate set trước khi LLM bắt đầu generate.

## Common Misconceptions

### “Vector search thay thế search engine truyền thống”

Không. Lexical search vẫn rất mạnh cho exact terms/IDs.

### “Top cosine similarity = correct evidence”

Similarity chỉ là retrieval signal, không semantic truth.

### “LLM có thể bù retrieval kém”

Nó có thể guess, nhưng đó làm grounded system kém đáng tin hơn.

## Knowledge Connection

IR nối [NLP Information Retrieval](../07_natural_language_processing/08_search_and_information_retrieval.md), [Embeddings](../08_large_language_models/02_embeddings_and_semantic_space.md) và RAG architecture.

Xem tiếp: [Sparse and Dense Retrieval](./01_sparse_and_dense_retrieval.md).