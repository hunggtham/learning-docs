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

> Inverted index làm cho việc lấy các tài liệu chứa term trở nên khả thi trên corpus lớn. Boolean retrieval sử dụng chính postings list đó để biểu diễn các điều kiện AND, OR và NOT.

## Boolean Retrieval

Queries combine terms:

```text
AI AND safety
transformer NOT electrical
```

Precise but no ranking by graded relevance and vocabulary mismatch problematic.

> Boolean retrieval lọc chính xác nhưng không xếp hạng mức độ phù hợp. TF-IDF bổ sung trọng số cho term dựa trên tần suất trong tài liệu và độ hiếm trong toàn corpus.

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

> TF-IDF là baseline thưa và dễ giải thích, nhưng chưa chuẩn hóa đầy đủ ảnh hưởng của độ dài tài liệu và tần suất lặp. BM25 điều chỉnh hai yếu tố đó để tạo ranking thực dụng hơn.

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

> BM25 xử lý tốt từ khóa hiếm và tên chính xác, nhưng vẫn phụ thuộc vào overlap bề mặt. Khi truy vấn và tài liệu dùng từ khác nhau cho cùng ý, vocabulary mismatch xuất hiện.

## Vocabulary Mismatch

Truy vấn (query / 쿼리) `car repair` may need document `automobile maintenance`. Lexical overlap weak.

Dense retrieval uses learned embeddings to capture ngữ nghĩa (semantic / 의미적) quan hệ (relation / 관계).

> Vocabulary mismatch là động lực cho dense retrieval: thay vì chỉ so khớp term, hệ thống so sánh các biểu diễn học được. Cách này đưa bài toán từ postings list sang khoảng cách trong không gian vector.

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

> Dense retrieval cho phép tìm theo ngữ nghĩa nhưng cần truy vấn hàng triệu vector với chi phí chấp nhận được. Approximate nearest neighbor dùng chỉ mục gần đúng để đổi một phần recall lấy tốc độ.

## Approximate Nearest Neighbor

Chính xác (exact / 정확한) scan millions vectors expensive. ANN indexes approximate top neighbors.

Dùng chung (common / 공통) concepts:

- HNSW đồ thị (graph / 그래프) tìm kiếm (search / 검색);
- IVF coarse partitions;
- sản phẩm (product / 제품) Quantization compression;
- flat chính xác (exact / 정확한) tìm kiếm (search / 검색) baseline.

ANN has recall/độ trễ (latency / 지연 시간)/bộ nhớ (memory / 메모리) sự đánh đổi (trade-off / 트레이드오프). “véc-tơ (vector / 벡터) cơ sở dữ liệu (database / 데이터베이스)” wraps indexing, filtering, persistence, siêu dữ liệu (metadata / 메타데이터) and operations around these mechanisms.

> ANN là họ kỹ thuật; HNSW minh họa rõ cách một đồ thị nhiều tầng dẫn đường tới các láng giềng gần. Hiểu trực giác này giúp đọc các tham số recall và latency như đánh đổi hệ thống.

## HNSW intuition

Hierarchical Navigable Small World đồ thị (graph / 그래프) connects vectors; tìm kiếm (search / 검색) greedily navigates from coarse upper layers to dense lower tầng (layer / 계층).

Hyperparameters điều khiển (control / 제어) đồ thị (graph / 그래프) degree/construction/tìm kiếm (search / 검색) breadth. Higher tìm kiếm (search / 검색) effort improves recall but increases độ trễ (latency / 지연 시간).

> HNSW và các ANN index tối ưu truy hồi dense, còn lexical retrieval vẫn mạnh với mã, tên và thuật ngữ hiếm. Hybrid retrieval kết hợp hai nguồn ứng viên trước khi chấm điểm đắt hơn.

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

> Hybrid retrieval mở rộng recall bằng cách trộn tín hiệu lexical và dense, nhưng danh sách ứng viên vẫn chưa được đọc sâu theo cặp query–document. Reranking đảm nhiệm bước chấm điểm chính xác hơn trên tập nhỏ.

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

> Reranking dành compute cho vài chục ứng viên nên có thể dùng cross-encoder, nhưng vẫn bị giới hạn bởi cách query được diễn đạt. Query expansion thử thêm các cách diễn đạt để giảm bỏ sót.

## Truy vấn (query / 쿼리) Expansion

Add synonyms/related terms to cầu nối (bridge / 브리지) mismatch. Classical pseudo-relevance phản hồi (feedback / 피드백) uses top docs terms.

Hiện đại (modern / 현대적) LLM can rewrite/expand truy vấn (query / 쿼리), but may drift intent. Original truy vấn (query / 쿼리) should remain and expansion evaluated.

> Query expansion có thể bù khác biệt từ vựng, nhưng rewrite sai sẽ làm lệch ý định ban đầu. Sau khi truy hồi được nhiều kết quả, chunking quyết định đơn vị nào được lập chỉ mục và gửi đi.

## Chunking

RAG retrieval often indexes passages, not whole documents.

Sự đánh đổi (trade-off / 트레이드오프):

- small chunk → precise, less ngữ cảnh (context / 맥락);
- large chunk → more ngữ cảnh (context / 맥락), diluted embedding/relevance;
- overlap → preserve boundaries but duplicate results/chi phí (cost / 비용).

Chunk should preserve ngữ nghĩa (semantic / 의미적) units: headings, paragraphs, tables/mã (code / 코드) blocks when possible.

> Chunk nhỏ tăng độ chính xác cục bộ nhưng dễ mất ngữ cảnh; chunk lớn giữ nhiều ngữ cảnh nhưng làm loãng tín hiệu. Parent–child retrieval tách đơn vị matching khỏi đơn vị context được trả về.

## Parent–Child Retrieval

Chỉ mục (index / 인덱스) small child chunks for precise matching but return larger parent section for ngữ cảnh (context / 맥락).

```text
small chunk embedding → match
parent section         → send LLM
```

This separates retrieval granularity from generation ngữ cảnh (context / 맥락) granularity.

> Parent–child retrieval giải quyết độ hạt của nội dung, nhưng chưa quyết định ai được phép thấy tài liệu nào. Metadata filtering đưa quyền, phiên bản và phạm vi nghiệp vụ vào trước hoặc trong truy hồi.

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

> Metadata filter có thể loại tài liệu không hợp lệ ngay cả khi chúng rất giống về ngữ nghĩa. Sau đó, freshness xác định liệu những tài liệu còn lại có phản ánh trạng thái hiện tại hay không.

## Freshness

Chỉ mục (index / 인덱스) cập nhật (update / 업데이트) chuỗi xử lý (pipeline / 파이프라인) determines kiến thức (knowledge / 지식) freshness. New document must be parsed, chunked, embedded, indexed and propagated.

Tìm kiếm (search / 검색) hệ thống (system / 시스템) should nhánh học (track / 트랙) document phiên bản (version / 버전) and deletion. “RAG has real-time kiến thức (knowledge / 지식)” only if ingestion is real-time enough.

> Freshness là thuộc tính của pipeline ingestion và deletion, không phải lời hứa tự động của RAG. Để đo relevance trên pipeline đó, cần các nhãn phản ánh phán đoán và hành vi người dùng.

## Relevance Labels

Huấn luyện (training / 학습)/evaluation query-document relevance can be:

- human judgments;
- click logs;
- synthetic pairs;
- implicit hành vi (behavior / 동작).

Click dữ liệu (data / 데이터) has position/exposure độ lệch (bias / 편향). Documents not shown cannot be clicked, creating vòng phản hồi (feedback loop / 피드백 루프).

> Relevance labels cung cấp mục tiêu cho huấn luyện và đánh giá, nhưng click log chịu position bias và feedback loop. Retrieval metrics biến các nhãn ấy thành các con số như recall, MRR và NDCG.

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

> Retrieval metrics cho biết bằng chứng có lọt vào top-k hay không, nhưng chưa đảm bảo câu trả lời cuối cùng dùng đúng bằng chứng. Vì vậy cần tách retrieval quality khỏi answer quality.

## Retrieval vs Answer chất lượng (quality / 품질)

Good retrieval doesn't guarantee answer; LLM may ignore/misread ngữ cảnh (context / 맥락).

Bad retrieval caps answer chất lượng (quality / 품질). Therefore evaluate separately:

```text
retrieval quality
context quality
generation faithfulness
end-to-end answer correctness
```

> Answer quality phụ thuộc cả việc truy hồi, lắp context và khả năng bám nguồn của generator. Nhìn toàn bộ chuỗi giúp chuyển từ metric riêng lẻ sang thiết kế multi-stage system.

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

> Multi-stage search phân bổ chi phí theo tầng: mở rộng ứng viên trước, lọc và rerank sau, rồi mới lắp context. Mental model dạng funnel dưới đây tóm tắt vì sao thứ tự ấy quan trọng.

## Mô hình tư duy (mental model / 사고 모델)

> Retrieval is a funnel: cheap broad methods maximize chance relevant bằng chứng (evidence / 증거) survives early stages; expensive precise methods improve thứ tự (ordering / 순서) later.

> Mental model funnel nhấn mạnh rằng mỗi tầng bảo vệ recall hoặc cải thiện precision ở một mức chi phí khác nhau. Các ngộ nhận sau đây thường xuất hiện khi chỉ nhìn vào một tầng.

## Dùng chung (common / 공통) Misconceptions

### “Dense retrieval replaces BM25”

Hybrid often wins because chính xác (exact / 정확한) lexical signals remain important.

### “véc-tơ (vector / 벡터) DB understands documents”

It indexes vectors/siêu dữ liệu (metadata / 메타데이터); ngữ nghĩa (semantic / 의미적) chất lượng (quality / 품질) comes from embedding/huấn luyện (training / 학습)/chunking.

### “Cosine highest document should go directly to LLM”

Similarity ≠ relevance/authority/freshness; reranking/filtering help.

### “If RAG answer wrong, LLM is hallucinating”

Nguyên nhân gốc (root cause / 근본 원인) may be retrieval miss, bad chunk, stale chỉ mục (index / 인덱스) or ngữ cảnh (context / 맥락) assembly.

> Các ngộ nhận cho thấy vector database, embedding và LLM không tự thay thế query understanding, freshness, filtering hay đánh giá. Các liên kết cuối file đưa những phần này về các owner tài liệu để tiếp tục học và kiểm chứng.

## Liên kết kiến thức (knowledge connection / 지식 연결)

IR connects [k-NN](../04_machine_learning/07_knn_and_distance_based_learning.md), [Contextual Embeddings](./04_contextual_embeddings.md), classical [Search](../02_search_reasoning_and_planning/00_state_space_and_search.md) and directly prepares `09_retrieval_and_rag/`.

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
