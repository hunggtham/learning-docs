# Nền tảng truy xuất thông tin

**Truy xuất thông tin (Information Retrieval — IR / 정보 검색)** nghiên cứu cách tìm các tài liệu hoặc item liên quan từ một collection lớn dựa trên query. RAG hiện đại dựa trực tiếp trên IR, vì trước khi LLM có thể trả lời bằng tri thức bên ngoài, hệ thống phải tìm đúng bằng chứng.

## Retrieval không phải tra cứu cơ sở dữ liệu

Database lookup thường có khóa hoặc predicate chính xác:

```sql
SELECT * FROM policy WHERE policy_id = 'A-102';
```

Information Retrieval xử lý những query mơ hồ hơn, chẳng hạn:

```text
"quy định hoàn tiền khi hủy dịch vụ"
```

Không có exact key rõ ràng; hệ thống phải ước lượng **mức liên quan (relevance)** giữa query và tài liệu.

## Corpus, Query và Relevance

Một bài toán retrieval có:

```text
Corpus D = {d1, d2, ..., dn}
Query q
Điểm liên quan s(q, d)
```

Hệ thống xếp hạng tài liệu theo score.

Điểm khó là relevance không phải thuộc tính tuyệt đối của document. Nó phụ thuộc query, ý định người dùng, thời gian và tác vụ.

Một tài liệu nói đúng chủ đề nhưng không chứa đáp án cụ thể có thể liên quan về chủ đề nhưng không đủ để trả lời.

## Boolean Retrieval

Cách đơn giản nhất dùng khớp term:

```text
refund AND cancellation
```

Boolean retrieval rất chính xác khi vocabulary ổn định nhưng dễ thất bại với synonym, morphology và natural-language query.

Nó vẫn hữu ích trong enterprise search vì filter constraint thường mang tính xác định:

```text
product = eKYC
AND version = current
AND language = ko
```

Hệ thống hiện đại thường kết hợp semantic ranking với metadata filter.

## Chỉ mục đảo

Search engine không quét toàn bộ document cho mỗi query mà xây **chỉ mục đảo (inverted index / 역색인)**:

```text
term → danh sách document chứa term
```

Ví dụ:

```text
refund → [doc2, doc8, doc20]
cancel → [doc2, doc3, doc20]
```

Query chỉ cần đọc những posting list liên quan. Đây là nền tảng của lexical search như BM25.

## Tần suất term và tần suất document

Một term xuất hiện nhiều trong document có thể quan trọng với document đó, nhưng term xuất hiện trong gần mọi document lại ít khả năng phân biệt.

TF-IDF biểu diễn trực giác này:

\[
TFIDF(t,d)=TF(t,d)\cdot IDF(t)
\]

với:

\[
IDF(t)=\log\frac{N}{df(t)}
\]

`df(t)` là số document chứa term.

Các term hiếm nhưng có tính thông tin được gán trọng số cao hơn từ phổ biến.

## BM25

BM25 là một hàm xếp hạng lexical rất mạnh. Dạng rút gọn:

\[
score(q,d)=\sum_{t\in q} IDF(t)\cdot \frac{tf(t,d)(k_1+1)}{tf(t,d)+k_1(1-b+b\frac{|d|}{avgdl})}
\]

Nó thêm saturation cho term frequency và chuẩn hóa theo độ dài document.

Mô hình tư duy:

> Một term quan trọng khi nó khớp query, hiếm trong corpus và xuất hiện đủ mạnh trong document, nhưng việc lặp lại không được thưởng vô hạn.

BM25 vẫn rất cạnh tranh trong enterprise RAG, đặc biệt với product code, ID, thuật ngữ pháp lý và tên chính xác.

## Precision và Recall trong Retrieval

**Precision** hỏi: trong các item đã retrieve, bao nhiêu item thực sự relevant?

\[
Precision=\frac{Relevant\ Retrieved}{Retrieved}
\]

**Recall** hỏi: trong toàn bộ item relevant, hệ thống retrieve được bao nhiêu?

\[
Recall=\frac{Relevant\ Retrieved}{All\ Relevant}
\]

RAG thường ưu tiên recall ở retrieval tầng đầu rồi dùng reranker để tăng precision.

Nếu bằng chứng đúng không lọt vào candidate set, LLM phía sau không thể sử dụng nó.

## Metric xếp hạng

### Recall@k

Đo khả năng item relevant xuất hiện trong top `k`.

### MRR

**Mean Reciprocal Rank (MRR)** thưởng việc kết quả relevant đầu tiên xuất hiện sớm:

\[
RR=\frac{1}{rank_{first\ relevant}}
\]

### nDCG

**Normalized Discounted Cumulative Gain (nDCG)** cho phép relevance nhiều mức và giảm trọng số khi kết quả xuất hiện ở vị trí thấp.

RAG retrieval eval không nên chỉ đo câu trả lời cuối, vì generator đôi khi có thể đoán đúng dù retrieval sai.

## Ý định query

Một query có thể mang tính:

- điều hướng: tìm document cụ thể;
- factual: tìm fact;
- khám phá: nghiên cứu chủ đề;
- giao dịch: tìm thông tin để hành động.

Chiến lược retrieval nên khác nhau. Query `API response code EKYC001` cần exact lexical match hơn câu `lỗi xác thực khuôn mặt thường do đâu?`.

## Lệch từ vựng

Lexical search thất bại khi query và document dùng từ khác nhau:

```text
query: "nghỉ việc"
document: "chấm dứt hợp đồng lao động"
```

Dense retrieval giải quyết một phần bằng biểu diễn ngữ nghĩa học được.

Ngược lại semantic retrieval có thể yếu với identifier chính xác. Vì vậy hybrid retrieval rất quan trọng.

## Độ mịn của document

Tìm toàn document có thể quá thô; tìm từng câu có thể quá nhỏ. RAG thường index **chunk**.

Đánh đổi:

```text
chunk nhỏ → khớp chính xác nhưng dễ thiếu context
chunk lớn → đủ context nhưng nhiều nhiễu và tốn token
```

Chunking là quyết định retrieval chứ không chỉ là tiện ích tiền xử lý.

## Mở rộng query

Hệ thống có thể mở rộng query bằng synonym, alias hoặc các cách diễn đạt thay thế được sinh tự động.

Ví dụ:

```text
"신분증 진위 확인"
→ ID verification
→ identity document authenticity
→ 신분증 검증
```

Mở rộng query tăng recall nhưng cũng có thể làm ý định bị trôi (query drift).

## Filter và Metadata

Metadata filter rất mạnh:

```text
version=current
country=KR
product=mobile_banking
access_level<=user_clearance
```

Embedding similarity không nên thay thế constraint tường minh.

## Retrieval như bước tạo candidate

Search hiện đại thường dùng hai tầng:

```text
retriever nhanh → top 100 candidate
reranker đắt hơn → top 5–10
```

Tầng đầu ưu tiên recall và latency; reranker tối ưu mức liên quan tinh hơn.

## IR và RAG

RAG thực chất phải trả lời hai câu hỏi riêng:

```text
Có retrieve được bằng chứng cần thiết cho q không?
Generator có sử dụng bằng chứng đó trung thực không?
```

Hai câu hỏi phải được đánh giá riêng.

## Mô hình tư duy

> Information Retrieval là **tìm kiếm dưới relevance không hoàn hảo**, không phải tra cứu chính xác. Chất lượng RAG đã bị giới hạn bởi candidate evidence trước khi LLM bắt đầu sinh.

## Những hiểu lầm thường gặp

### “Vector search thay thế hoàn toàn search engine truyền thống”

Không. Lexical search vẫn rất mạnh với exact term và ID.

### “Cosine similarity cao nhất là bằng chứng đúng”

Similarity chỉ là tín hiệu retrieval, không phải sự thật ngữ nghĩa.

### “LLM có thể bù retrieval kém”

Mô hình có thể đoán, nhưng điều đó làm hệ thống grounded kém đáng tin hơn.

## Liên kết kiến thức

IR nối [NLP Information Retrieval](../07_natural_language_processing/08_search_and_information_retrieval.md), [Embeddings](../08_large_language_models/02_embeddings_and_semantic_space.md) và kiến trúc RAG.

Xem tiếp: [Sparse and Dense Retrieval](./01_sparse_and_dense_retrieval.md).