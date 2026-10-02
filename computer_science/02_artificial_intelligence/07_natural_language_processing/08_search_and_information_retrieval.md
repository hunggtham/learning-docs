# Tìm kiếm (search / 검색) và thông tin (information / 정보) Retrieval trong NLP

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Search và information retrieval trong NLP**. Route đi từ inverted index → Boolean retrieval → TF-IDF/BM25 → dense retrieval/reranking → relevance and latency evaluation, để truy hồi được đọc cùng representation và query intent.

Thông tin (information / 정보) Retrieval (IR / 정보 검색 / truy xuất thông tin) trả lời câu hỏi: với một truy vấn (query / 쿼리), trong một collection lớn, documents/passages nào relevant nhất? Đây là nền trực tiếp của tìm kiếm (search / 검색) engine và RAG.

IR khác classification ở chỗ đầu ra (output / 출력) là **ranking over large corpus**. hệ thống (system / 시스템) cần candidate generation cực nhanh rồi scoring/reranking chính xác hơn.

## Inverted chỉ mục (index / 인덱스)

Lexical tìm kiếm (search / 검색) cốt lõi (core / 핵심) cấu trúc dữ liệu (data structure / 자료구조):

```text
term → postings list of documents/positions
```

Ví dụ:

```text
"transformer" → [doc2, doc10, doc42]
```

Truy vấn (query / 쿼리) không scan mọi documents. Inverted chỉ mục (index / 인덱스) makes sparse retrieval scalable.

Positions enable phrase/proximity tìm kiếm (search / 검색).

> **Chuyển mạch:** Trong **Tìm kiếm (search / 검색) và thông tin (information / 정보) Retrieval trong NLP**, **Boolean Retrieval** tiếp nhận điểm tựa từ **Inverted chỉ mục (index / 인덱스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **TF-IDF** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Boolean Retrieval

Queries combine terms:

```text
AI AND safety
transformer NOT electrical
```

Precise but no ranking by graded relevance and vocabulary mismatch problematic.

> **Chuyển mạch:** Ở chặng này của **Tìm kiếm (search / 검색) và thông tin (information / 정보) Retrieval trong NLP**, **TF-IDF** tiếp nhận điểm tựa từ **Boolean Retrieval** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **BM25** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## TF-IDF

Term important if frequent in document but rare corpus-wide.

\[
TFIDF(t,d)=TF(t,d)IDF(t)
\]

IDF often:

\[
IDF(t)=\log\frac{N}{DF(t)}
\]

Sparse document/truy vấn (query / 쿼리) vectors can use cosine similarity.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tìm kiếm (search / 검색) và thông tin (information / 정보) Retrieval trong NLP**, **BM25** tiếp nhận điểm tựa từ **TF-IDF** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vocabulary Mismatch** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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
- rare truy vấn (query / 쿼리) terms matter more.

BM25 remains highly competitive for chính xác (exact / 정확한) names, codes, identifiers and rare terminology.

> **Chuyển mạch:** Trong **Tìm kiếm (search / 검색) và thông tin (information / 정보) Retrieval trong NLP**, **Vocabulary Mismatch** tiếp nhận điểm tựa từ **BM25** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dense Retrieval** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vocabulary Mismatch

Truy vấn (query / 쿼리) `car repair` may need document `automobile maintenance`. Lexical overlap weak.

Dense retrieval uses learned embeddings to capture ngữ nghĩa (semantic / 의미적) quan hệ (relation / 관계).

> **Chuyển mạch:** Ở chặng này của **Tìm kiếm (search / 검색) và thông tin (information / 정보) Retrieval trong NLP**, **Dense Retrieval** tiếp nhận điểm tựa từ **Vocabulary Mismatch** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Approximate Nearest Neighbor** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dense Retrieval

Bi-encoder:

\[
q=f_\theta(query),\quad d=g_\theta(document)
\]

score:

\[
s(q,d)=q^Td
\]

Precompute document embeddings. truy vấn (query / 쿼리) véc-tơ (vector / 벡터) performs nearest-neighbor tìm kiếm (search / 검색).

This trades chính xác (exact / 정확한) lexical matching for learned ngữ nghĩa (semantic / 의미적) hình học (geometry / 기하학).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tìm kiếm (search / 검색) và thông tin (information / 정보) Retrieval trong NLP**, **Approximate Nearest Neighbor** tiếp nhận điểm tựa từ **Dense Retrieval** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **HNSW intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Approximate Nearest Neighbor

Chính xác (exact / 정확한) scan millions vectors expensive. ANN indexes approximate top neighbors.

Dùng chung (common / 공통) concepts:

- HNSW đồ thị (graph / 그래프) tìm kiếm (search / 검색);
- IVF coarse partitions;
- sản phẩm (product / 제품) Quantization compression;
- flat chính xác (exact / 정확한) tìm kiếm (search / 검색) baseline.

ANN has recall/độ trễ (latency / 지연 시간)/bộ nhớ (memory / 메모리) sự đánh đổi (trade-off / 트레이드오프). “véc-tơ (vector / 벡터) cơ sở dữ liệu (database / 데이터베이스)” wraps indexing, filtering, persistence, siêu dữ liệu (metadata / 메타데이터) and operations around these mechanisms.

> **Chuyển mạch:** Trong **Tìm kiếm (search / 검색) và thông tin (information / 정보) Retrieval trong NLP**, **HNSW intuition** tiếp nhận điểm tựa từ **Approximate Nearest Neighbor** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hybrid Retrieval** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## HNSW intuition

Hierarchical Navigable Small World đồ thị (graph / 그래프) connects vectors; tìm kiếm (search / 검색) greedily navigates from coarse upper layers to dense lower tầng (layer / 계층).

Hyperparameters điều khiển (control / 제어) đồ thị (graph / 그래프) degree/construction/tìm kiếm (search / 검색) breadth. Higher tìm kiếm (search / 검색) effort improves recall but increases độ trễ (latency / 지연 시간).

> **Chuyển mạch:** Ở chặng này của **Tìm kiếm (search / 검색) và thông tin (information / 정보) Retrieval trong NLP**, **Hybrid Retrieval** tiếp nhận điểm tựa từ **HNSW intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Reranking** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tìm kiếm (search / 검색) và thông tin (information / 정보) Retrieval trong NLP**, **Reranking** tiếp nhận điểm tựa từ **Hybrid Retrieval** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Truy vấn (query / 쿼리) Expansion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reranking

First-stage retriever optimizes recall + speed. Cross-encoder reranker jointly reads truy vấn (query / 쿼리)/document and assigns relevance score.

Chuỗi xử lý (pipeline / 파이프라인):

```text
Corpus millions
→ BM25/dense retrieve top 100
→ cross-encoder rerank
→ top 5–20
```

This cascade concentrates expensive computation on small candidate set.

> **Chuyển mạch:** Trong **Tìm kiếm (search / 검색) và thông tin (information / 정보) Retrieval trong NLP**, **Truy vấn (query / 쿼리) Expansion** tiếp nhận điểm tựa từ **Reranking** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chunking** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Truy vấn (query / 쿼리) Expansion

Add synonyms/related terms to cầu nối (bridge / 브리지) mismatch. Classical pseudo-relevance phản hồi (feedback / 피드백) uses top docs terms.

Hiện đại (modern / 현대적) LLM can rewrite/expand truy vấn (query / 쿼리), but may drift intent. Original truy vấn (query / 쿼리) should remain and expansion evaluated.

> **Chuyển mạch:** Ở chặng này của **Tìm kiếm (search / 검색) và thông tin (information / 정보) Retrieval trong NLP**, **Chunking** tiếp nhận điểm tựa từ **Truy vấn (query / 쿼리) Expansion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Parent–Child Retrieval** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chunking

RAG retrieval often indexes passages, not whole documents.

Sự đánh đổi (trade-off / 트레이드오프):

- small chunk → precise, less ngữ cảnh (context / 맥락);
- large chunk → more ngữ cảnh (context / 맥락), diluted embedding/relevance;
- overlap → preserve boundaries but duplicate results/chi phí (cost / 비용).

Chunk should preserve ngữ nghĩa (semantic / 의미적) units: headings, paragraphs, tables/mã (code / 코드) blocks when possible.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tìm kiếm (search / 검색) và thông tin (information / 정보) Retrieval trong NLP**, **Parent–Child Retrieval** tiếp nhận điểm tựa từ **Chunking** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Siêu dữ liệu (metadata / 메타데이터) Filtering** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Parent–Child Retrieval

Chỉ mục (index / 인덱스) small child chunks for precise matching but return larger parent section for ngữ cảnh (context / 맥락).

```text
small chunk embedding → match
parent section         → send LLM
```

This separates retrieval granularity from generation ngữ cảnh (context / 맥락) granularity.

> **Chuyển mạch:** Trong **Tìm kiếm (search / 검색) và thông tin (information / 정보) Retrieval trong NLP**, **Parent–Child Retrieval** nêu điều cần giải thích; **Siêu dữ liệu (metadata / 메타데이터) Filtering** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Freshness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Siêu dữ liệu (metadata / 메타데이터) Filtering

Relevance is not only văn bản (text / 텍스트) similarity. Need các ràng buộc (constraints / 제약조건들):

```text
user permission
date range
language
document type
project/customer
version/status
```

Siêu dữ liệu (metadata / 메타데이터) filtering before/within ANN is trọng yếu (critical / 중요) enterprise RAG. Retrieving unauthorized document is bảo mật (security / 보안) thất bại (failure / 실패) even if mô hình (model / 모델) never quotes it.

> **Chuyển mạch:** Ở chặng này của **Tìm kiếm (search / 검색) và thông tin (information / 정보) Retrieval trong NLP**, **Siêu dữ liệu (metadata / 메타데이터) Filtering** nêu điều cần giải thích; **Freshness** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Relevance Labels** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Freshness

Chỉ mục (index / 인덱스) cập nhật (update / 업데이트) chuỗi xử lý (pipeline / 파이프라인) determines kiến thức (knowledge / 지식) freshness. New document must be parsed, chunked, embedded, indexed and propagated.

Tìm kiếm (search / 검색) hệ thống (system / 시스템) should nhánh học (track / 트랙) document phiên bản (version / 버전) and deletion. “RAG has real-time kiến thức (knowledge / 지식)” only if ingestion is real-time enough.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tìm kiếm (search / 검색) và thông tin (information / 정보) Retrieval trong NLP**, **Freshness** cho ta quy tắc; **Relevance Labels** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Retrieval Metrics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Relevance Labels

Huấn luyện (training / 학습)/evaluation query-document relevance can be:

- human judgments;
- click logs;
- synthetic pairs;
- implicit hành vi (behavior / 동작).

Click dữ liệu (data / 데이터) has position/exposure độ lệch (bias / 편향). Documents not shown cannot be clicked, creating vòng phản hồi (feedback loop / 피드백 루프).

> **Chuyển mạch:** Trong **Tìm kiếm (search / 검색) và thông tin (information / 정보) Retrieval trong NLP**, **Relevance Labels** cho ta quy tắc; **Retrieval Metrics** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Retrieval vs Answer chất lượng (quality / 품질)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

For RAG, **retrieval recall** often trọng yếu (critical / 중요): if correct bằng chứng (evidence / 증거) never retrieved, generator cannot ground answer from it.

> **Chuyển mạch:** Ở chặng này của **Tìm kiếm (search / 검색) và thông tin (information / 정보) Retrieval trong NLP**, **Retrieval vs Answer chất lượng (quality / 품질)** tiếp nhận điểm tựa từ **Retrieval Metrics** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tìm kiếm (search / 검색) as Multi-Stage hệ thống (system / 시스템)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Retrieval vs Answer chất lượng (quality / 품질)

Good retrieval doesn't guarantee answer; LLM may ignore/misread ngữ cảnh (context / 맥락).

Bad retrieval caps answer chất lượng (quality / 품질). Therefore evaluate separately:

```text
retrieval quality
context quality
generation faithfulness
end-to-end answer correctness
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tìm kiếm (search / 검색) và thông tin (information / 정보) Retrieval trong NLP**, **Tìm kiếm (search / 검색) as Multi-Stage hệ thống (system / 시스템)** tiếp nhận điểm tựa từ **Retrieval vs Answer chất lượng (quality / 품질)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tìm kiếm (search / 검색) as Multi-Stage hệ thống (system / 시스템)

Hiện đại (modern / 현대적) kiến trúc (architecture / 아키텍처):

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

Optimizing only embedding mô hình (model / 모델) ignores most hệ thống (system / 시스템).

> **Chuyển mạch:** Trong **Tìm kiếm (search / 검색) và thông tin (information / 정보) Retrieval trong NLP**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Tìm kiếm (search / 검색) as Multi-Stage hệ thống (system / 시스템)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Retrieval is a funnel: cheap broad methods maximize chance relevant bằng chứng (evidence / 증거) survives early stages; expensive precise methods improve thứ tự (ordering / 순서) later.

> **Chuyển mạch:** Ở chặng này của **Tìm kiếm (search / 검색) và thông tin (information / 정보) Retrieval trong NLP**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Dense retrieval replaces BM25”

Hybrid often wins because chính xác (exact / 정확한) lexical signals remain important.

### “véc-tơ (vector / 벡터) DB understands documents”

It indexes vectors/siêu dữ liệu (metadata / 메타데이터); ngữ nghĩa (semantic / 의미적) chất lượng (quality / 품질) comes from embedding/huấn luyện (training / 학습)/chunking.

### “Cosine highest document should go directly to LLM”

Similarity ≠ relevance/authority/freshness; reranking/filtering help.

### “If RAG answer wrong, LLM is hallucinating”

Nguyên nhân gốc (root cause / 근본 원인) may be retrieval miss, bad chunk, stale chỉ mục (index / 인덱스) or ngữ cảnh (context / 맥락) assembly.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tìm kiếm (search / 검색) và thông tin (information / 정보) Retrieval trong NLP**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

IR connects [k-NN](../04_machine_learning/07_knn_and_distance_based_learning.md), [Contextual Embeddings](./04_contextual_embeddings.md), classical [Search](../02_search_reasoning_and_planning/00_state_space_and_search.md) and directly prepares `09_retrieval_and_rag/`.

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
