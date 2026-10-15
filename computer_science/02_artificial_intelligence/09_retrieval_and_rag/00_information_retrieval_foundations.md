# Thông tin (information / 정보) Retrieval Foundations

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Information retrieval foundations**. Route đi từ corpus/document collection → query representation → inverted or vector index → relevance scoring → ranking metrics, để retrieval được phân biệt với lookup bằng mục tiêu tìm đúng tài liệu.

**thông tin (information / 정보) Retrieval (IR / 정보 검색 / truy xuất thông tin)** nghiên cứu cách tìm những document hoặc item liên quan từ một collection lớn dựa trên một truy vấn (query / 쿼리). RAG hiện đại dựa trực tiếp trên IR, vì trước khi LLM có thể trả lời dựa trên bên ngoài (external / 외부) kiến thức (knowledge / 지식), hệ thống (system / 시스템) phải tìm đúng bằng chứng (evidence / 증거).

## Retrieval không phải cơ sở dữ liệu (database / 데이터베이스) Lookup

Cơ sở dữ liệu (database / 데이터베이스) lookup thường có key hoặc predicate chính xác:

```sql
SELECT * FROM policy WHERE policy_id = 'A-102';
```

Thông tin (information / 정보) retrieval xử lý truy vấn (query / 쿼리) mơ hồ hơn:

```text
"quy định hoàn tiền khi hủy dịch vụ"
```

Không có chính xác (exact / 정확한) key rõ ràng. hệ thống (system / 시스템) phải estimate relevance giữa truy vấn (query / 쿼리) và documents.

Retrieval bắt đầu bằng việc xác định collection, truy vấn và tiêu chí relevance; Boolean retrieval biến những khái niệm đó thành phép lọc rõ ràng.

## Corpus, truy vấn (query / 쿼리), Relevance

Một retrieval bài toán (problem / 문제) có:

```text
Corpus D = {d1, d2, ..., dn}
Query q
Relevance score s(q, d)
```

Hệ thống (system / 시스템) rank documents theo score.

Điểm khó là **relevance không phải thuộc tính (property / 속성) tuyệt đối của document**. Nó phụ thuộc truy vấn (query / 쿼리), người dùng (user / 사용자) intent, thời gian (time / 시간) và tác vụ (task / 작업).

Một document nói đúng chủ đề nhưng không chứa answer cụ thể có thể topical relevant nhưng answer-irrelevant.

Boolean matching cho ta tập ứng viên và các ràng buộc chính xác, nhưng cần một cấu trúc chỉ mục để không phải quét toàn bộ corpus mỗi lần.

## Boolean Retrieval

Cách đơn giản nhất dùng term matching:

```text
refund AND cancellation
```

Boolean retrieval rất precise khi vocabulary ổn định, nhưng brittle với synonym, morphology và natural-language truy vấn (query / 쿼리).

Nó vẫn hữu ích trong enterprise tìm kiếm (search / 검색) vì filter các ràng buộc (constraints / 제약조건들) thường deterministic:

```text
product = eKYC
AND version = current
AND language = ko
```

Hiện đại (modern / 현대적) retrieval thường kết hợp ngữ nghĩa (semantic / 의미적) ranking với siêu dữ liệu (metadata / 메타데이터) filters.

Inverted index làm truy vấn lexical nhanh; từ các postings lists, ta cần trọng số để phân biệt term phổ biến với term có sức phân biệt cao.

## Inverted chỉ mục (index / 인덱스)

Tìm kiếm (search / 검색) engine không scan mọi document cho mỗi truy vấn (query / 쿼리). Nó xây **inverted chỉ mục (index / 인덱스)**:

```text
term → list of documents containing term
```

Ví dụ:

```text
refund → [doc2, doc8, doc20]
cancel → [doc2, doc3, doc20]
```

Truy vấn (query / 쿼리) chỉ cần inspect postings lists liên quan.

Đây là foundation của lexical tìm kiếm (search / 검색) như BM25.

TF và DF cung cấp trực giác về độ quan trọng của term; BM25 dùng trực giác đó cùng length normalization để xếp hạng tài liệu.

## Term Frequency và Document Frequency

Một term xuất hiện nhiều trong document có thể quan trọng cho document đó, nhưng term phổ biến trong gần mọi document mang ít discriminative giá trị (value / 값).

TF-IDF captures intuition:

\[
TFIDF(t,d)=TF(t,d)\cdot IDF(t)
\]

với:

\[
IDF(t)=\log\frac{N}{df(t)}
\]

`df(t)` là số documents chứa term.

Rare informative terms được weight cao hơn dùng chung (common / 공통) words.

BM25 tạo ranking lexical mạnh, nhưng chất lượng retrieval còn phải đo bằng việc lấy đúng và đủ bằng chứng trong top-k.

## BM25

BM25 là lexical ranking hàm (function / 함수) rất mạnh. Simplified form:

\[
score(q,d)=\sum_{t\in q} IDF(t)\cdot \frac{tf(t,d)(k_1+1)}{tf(t,d)+k_1(1-b+b\frac{|d|}{avgdl})}
\]

Nó thêm saturation cho term frequency và length normalization.

Mô hình tư duy (mental model / 사고 모델):

> Một term quan trọng nếu nó match truy vấn (query / 쿼리), hiếm trong corpus và xuất hiện đủ mạnh trong document, nhưng repetition không được reward vô hạn.

BM25 vẫn competitive trong enterprise RAG, đặc biệt cho sản phẩm (product / 제품) codes, IDs, legal terms và chính xác (exact / 정확한) names.

Precision và recall mô tả hai mặt của candidate retrieval; các ranking metrics dưới đây cho biết vị trí và mức độ relevant được ưu tiên ra sao.

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

Nếu correct bằng chứng (evidence / 증거) không vào candidate set, LLM phía sau không thể sử dụng nó.

Metrics chỉ có ý nghĩa khi gắn với intent của query; một navigational query và một exploratory query cần chiến lược retrieval khác nhau.

## Ranking Metrics

### Recall@k

Có relevant document trong top `k` không?

### MRR

Mean Reciprocal Rank reward relevant kết quả (result / 결과) xuất hiện sớm:

\[
RR=\frac{1}{rank_{first\ relevant}}
\]

### nDCG

Normalized Discounted Cumulative Gain cho phép graded relevance và discount rank thấp.

RAG retrieval eval không nên chỉ đo final answer, vì final mô hình (model / 모델) có thể đoán đúng dù retrieval sai.

Query intent quyết định loại bằng chứng cần tìm, nhưng cùng một ý định có thể dùng từ khác với document; đó là vocabulary mismatch.

## Truy vấn (query / 쿼리) Intent

Một truy vấn (query / 쿼리) có thể là:

- navigational: tìm document cụ thể;
- factual: tìm fact;
- exploratory: nghiên cứu topic;
- transactional: tìm thông tin (information / 정보) để hành động.

Retrieval chiến lược (strategy / 전략) nên khác nhau. truy vấn (query / 쿼리) “API phản hồi (response / 응답) mã (code / 코드) EKYC001” cần chính xác (exact / 정확한) lexical match hơn truy vấn (query / 쿼리) “lỗi xác thực khuôn mặt thường do đâu?”.

Vocabulary mismatch thúc đẩy semantic retrieval, nhưng cách chia document cũng quyết định bằng chứng có vừa một candidate hay không.

## Vocabulary Mismatch

Lexical tìm kiếm (search / 검색) thất bại (fail / 실패) khi truy vấn (query / 쿼리) và document dùng different words:

```text
query: "nghỉ việc"
document: "chấm dứt hợp đồng lao động"
```

Dense retrieval giải một phần bằng learned ngữ nghĩa (semantic / 의미적) representations.

Nhưng ngữ nghĩa (semantic / 의미적) retrieval có thể thất bại (fail / 실패) chính xác (exact / 정확한) identifiers. Vì vậy hybrid retrieval rất quan trọng.

Document granularity tạo trade-off giữa độ chính xác và context; query expansion là một cách tăng recall khi từ khóa ban đầu quá hẹp.

## Document Granularity

Tìm kiếm (search / 검색) whole document có thể quá coarse; tìm kiếm (search / 검색) sentence quá fine. RAG thường chỉ mục (index / 인덱스) chunks.

Granularity sự đánh đổi (trade-off / 트레이드오프):

```text
small chunk → precise match nhưng thiếu context
large chunk → đủ context nhưng noisy và tốn tokens
```

Chunking là retrieval thiết kế (design / 설계), không chỉ preprocessing convenience.

Expansion có thể tăng recall nhưng cũng kéo theo drift; metadata filters giúp giữ lại những ràng buộc mà similarity không thể bảo đảm.

## Truy vấn (query / 쿼리) Expansion

Hệ thống (system / 시스템) có thể expand truy vấn (query / 쿼리) bằng synonyms, aliases hoặc generated alternatives.

Ví dụ:

```text
"신분증 진위 확인"
→ ID verification
→ identity document authenticity
→ 신분증 검증
```

Expansion tăng recall nhưng có thể introduce drift.

Filters giới hạn corpus theo thuộc tính rõ ràng; sau đó retriever có thể tạo candidate set để reranker và generator xử lý.

## Filters và siêu dữ liệu (metadata / 메타데이터)

Siêu dữ liệu (metadata / 메타데이터) filters rất powerful:

```text
version=current
country=KR
product=mobile_banking
access_level<=user_clearance
```

Embedding similarity không nên replace tường minh (explicit / 명시적) các ràng buộc (constraints / 제약조건들).

Candidate generation tách chi phí tìm rộng khỏi chi phí xếp hạng sâu; IR và RAG vì thế phải được đánh giá ở cả retrieval lẫn generation.

## Retrieval as Candidate Generation

Hiện đại (modern / 현대적) tìm kiếm (search / 검색) thường two-stage:

```text
fast retriever → top 100 candidates
expensive reranker → top 5–10
```

First stage optimize recall/độ trễ (latency / 지연 시간). Reranker optimize fine relevance.

RAG không chỉ hỏi có tìm được tài liệu hay không, mà còn hỏi generator có dùng bằng chứng đó trung thực không; mô hình tư duy dưới đây tóm tắt ranh giới này.

## IR và RAG

RAG chuỗi xử lý (pipeline / 파이프라인) fundamentally asks:

```text
Can we retrieve evidence needed to answer q?
Can generator use that evidence faithfully?
```

Hai questions cần eval riêng.

Mô hình tư duy xem retrieval là tìm kiếm theo relevance không hoàn hảo và candidate set là giới hạn đầu tiên của RAG; các ngộ nhận sau đây thường bỏ qua giới hạn đó.

## Mô hình tư duy (mental model / 사고 모델)

> thông tin (information / 정보) Retrieval là **tìm kiếm (search / 검색) over imperfect relevance**, không phải chính xác (exact / 정확한) lookup. RAG chất lượng (quality / 품질) bị giới hạn bởi bằng chứng (evidence / 증거) candidate set trước khi LLM bắt đầu generate.

Các ngộ nhận đều nhầm semantic similarity với truth hoặc cho rằng LLM có thể sửa mọi candidate set; phần liên kết kiến thức đặt các ranh giới này vào lộ trình tiếp theo.

## Dùng chung (common / 공통) Misconceptions

### “véc-tơ (vector / 벡터) tìm kiếm (search / 검색) thay thế tìm kiếm (search / 검색) engine truyền thống”

Không. Lexical tìm kiếm (search / 검색) vẫn rất mạnh cho chính xác (exact / 정확한) terms/IDs.

### “Top cosine similarity = correct bằng chứng (evidence / 증거)”

Similarity chỉ là retrieval tín hiệu (signal / 신호), không ngữ nghĩa (semantic / 의미적) truth.

### “LLM có thể bù retrieval kém”

Nó có thể guess, nhưng đó làm grounded hệ thống (system / 시스템) kém đáng tin hơn.



## Liên kết kiến thức (knowledge connection / 지식 연결)

IR nối [NLP Information Retrieval](../07_natural_language_processing/08_search_and_information_retrieval.md), [Embeddings](../08_large_language_models/02_embeddings_and_semantic_space.md) và RAG kiến trúc (architecture / 아키텍처).

Xem tiếp: [Sparse and Dense Retrieval](./01_sparse_and_dense_retrieval.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
