# Search và Information Retrieval trong NLP

**Truy xuất thông tin (Information Retrieval — IR / 정보 검색)** trả lời câu hỏi: với một query, trong một tập dữ liệu lớn, tài liệu hoặc đoạn văn nào liên quan nhất? Đây là nền trực tiếp của công cụ tìm kiếm và RAG.

IR khác phân loại ở chỗ đầu ra thường là **một thứ hạng trên corpus lớn**. Hệ thống cần tạo tập ứng viên rất nhanh trước, sau đó mới dùng mô hình chính xác nhưng đắt hơn để chấm điểm và xếp hạng lại.

## Inverted Index

Cấu trúc dữ liệu cốt lõi của tìm kiếm từ khóa là **chỉ mục đảo (inverted index)**:

```text
term → danh sách tài liệu / vị trí chứa term
```

Ví dụ:

```text
"transformer" → [doc2, doc10, doc42]
```

Query không cần quét mọi tài liệu. Inverted index làm sparse retrieval có thể mở rộng tới corpus rất lớn. Nếu lưu cả vị trí token, hệ thống còn hỗ trợ tìm cụm từ hoặc khoảng cách giữa các từ.

## Boolean Retrieval

Query có thể kết hợp từ bằng toán tử logic:

```text
AI AND safety
transformer NOT electrical
```

Cách này chính xác về điều kiện nhưng không tự tạo thứ hạng relevance mềm và dễ gặp vấn đề khi query dùng từ khác tài liệu.

## TF-IDF

Một term có giá trị khi xuất hiện nhiều trong tài liệu nhưng hiếm trên toàn corpus:

\[
TFIDF(t,d)=TF(t,d)IDF(t)
\]

với dạng IDF đơn giản:

\[
IDF(t)=\log\frac{N}{DF(t)}
\]

Query và document có thể được biểu diễn thành vector thưa rồi so bằng cosine similarity.

## BM25

BM25 là baseline lexical ranking rất mạnh:

\[
score(q,d)=\sum_{t\in q}IDF(t)
\frac{f(t,d)(k_1+1)}
{f(t,d)+k_1(1-b+b|d|/avgdl)}
\]

Nó bổ sung hai trực giác quan trọng: tần suất lặp lại một term có lợi nhưng lợi ích giảm dần; tài liệu dài được chuẩn hóa để không thắng chỉ vì chứa nhiều từ hơn.

Term hiếm trong corpus thường được trọng số cao hơn. BM25 vẫn đặc biệt mạnh với tên chính xác, mã, identifier và thuật ngữ hiếm.

## Vocabulary Mismatch

Query `car repair` có thể cần tài liệu chứa `automobile maintenance`. Nếu chỉ dựa vào trùng từ, relevance sẽ thấp dù nghĩa gần nhau.

Dense retrieval giải quyết một phần bằng embedding học được.

## Dense Retrieval

Bi-encoder tạo vector độc lập:

\[
q=f_\theta(query),\quad d=g_\theta(document)
\]

và chấm điểm:

\[
s(q,d)=q^Td
\]

Document embedding có thể được tính trước. Khi query đến, hệ thống chỉ cần tạo query vector rồi tìm láng giềng gần nhất.

Cách này đánh đổi khả năng khớp từ chính xác lấy hình học ngữ nghĩa đã học.

## Approximate Nearest Neighbor

Quét chính xác hàng triệu vector rất tốn chi phí. **Approximate Nearest Neighbor (ANN)** tìm gần đúng top neighbor để đổi một phần recall lấy tốc độ và bộ nhớ.

Các khái niệm phổ biến gồm:

- HNSW: tìm kiếm trên đồ thị nhiều tầng;
- IVF: chia không gian thành các vùng thô;
- Product Quantization: nén vector;
- flat search: baseline tìm chính xác.

“Vector database” thường đóng gói các cơ chế chỉ mục này cùng metadata, filtering, persistence và vận hành.

## Trực giác về HNSW

**Hierarchical Navigable Small World (HNSW)** xây đồ thị vector theo nhiều tầng. Tìm kiếm bắt đầu ở tầng thưa để di chuyển nhanh đến vùng phù hợp, rồi xuống tầng dày hơn để tinh chỉnh kết quả.

Các hyperparameter điều khiển số cạnh và độ rộng tìm kiếm. Mở rộng tìm kiếm thường tăng recall nhưng cũng tăng latency.

## Hybrid Retrieval

Lexical và dense retrieval có ưu thế bổ sung:

```text
BM25  → từ khóa chính xác, mã, tên hiếm
Dense → paraphrase và tương đồng ngữ nghĩa
```

Hệ thống lai có thể hợp nhất candidate hoặc thứ hạng. **Reciprocal Rank Fusion (RRF)** dùng:

\[
RRF(d)=\sum_r\frac1{k+rank_r(d)}
\]

nên không cần hiệu chỉnh trực tiếp các thang điểm rất khác nhau giữa retriever.

## Reranking

Retriever tầng đầu ưu tiên tốc độ và recall. Cross-encoder reranker đọc chung query và document rồi cho điểm relevance chính xác hơn.

Một pipeline điển hình:

```text
corpus hàng triệu tài liệu
→ BM25 / dense lấy top 100
→ cross-encoder rerank
→ top 5–20
```

Cấu trúc cascade này chỉ dành compute đắt tiền cho một tập candidate nhỏ.

## Mở rộng Query

Có thể thêm từ đồng nghĩa hoặc term liên quan để giảm vocabulary mismatch. Pseudo-relevance feedback cổ điển dùng những term thường gặp trong top document.

LLM hiện đại có thể viết lại hoặc mở rộng query, nhưng cũng có nguy cơ làm lệch intent. Nên giữ query gốc và đánh giá expansion trên dữ liệu thật.

## Chunking

RAG thường lập chỉ mục đoạn nhỏ thay vì cả tài liệu.

Sự đánh đổi:

- chunk nhỏ → khớp chính xác hơn nhưng ít ngữ cảnh;
- chunk lớn → nhiều ngữ cảnh nhưng relevance có thể bị pha loãng;
- overlap → giữ thông tin qua biên nhưng tăng trùng lặp và chi phí.

Khi có thể nên giữ đơn vị ngữ nghĩa tự nhiên như heading, paragraph, table và code block.

## Parent–Child Retrieval

Có thể index child chunk nhỏ để tìm chính xác nhưng trả lại parent section lớn hơn cho generator:

```text
embedding chunk nhỏ → tìm khớp
parent section       → đưa vào LLM
```

Thiết kế này tách kích thước đơn vị truy xuất khỏi kích thước context dùng để sinh.

## Metadata Filtering

Relevance không chỉ là tương đồng văn bản. Hệ thống enterprise còn phải lọc theo:

```text
quyền người dùng
khoảng thời gian
ngôn ngữ
loại tài liệu
project / customer
version / trạng thái
```

Filtering quyền truy cập phải xảy ra đúng chỗ trong retrieval. Việc truy xuất được tài liệu không có quyền đã là lỗi bảo mật ngay cả khi LLM cuối cùng không trích dẫn nó.

## Độ mới của chỉ mục

Kiến thức trong search chỉ mới bằng pipeline ingestion. Tài liệu mới phải được parse, chunk, embed, index và đồng bộ tới các node phục vụ truy vấn.

Hệ thống cũng phải xử lý version và deletion. “RAG có kiến thức thời gian thực” chỉ đúng nếu toàn bộ ingestion/index pipeline đủ nhanh.

## Nhãn Relevance

Dữ liệu query–document có thể đến từ đánh giá con người, click log, cặp tổng hợp hoặc hành vi ngầm.

Click log có thiên lệch vị trí và phơi nhiễm: tài liệu không được hiển thị thì không thể được click. Vì vậy dữ liệu hành vi phản ánh policy của search system, không phải relevance trung lập.

## Metric truy xuất

Recall@K:

\[
\frac{relevant\ docs\ retrieved\ in\ topK}{all\ relevant\ docs}
\]

MRR tập trung vị trí của kết quả liên quan đầu tiên:

\[
MRR=\frac1N\sum_q\frac1{rank_q}
\]

NDCG hỗ trợ relevance nhiều mức và giảm trọng số theo vị trí.

Trong RAG, **retrieval recall** thường rất quan trọng: nếu bằng chứng đúng không lọt vào candidate, generator không thể grounded vào nó.

## Retrieval Quality và Answer Quality

Truy xuất tốt không bảo đảm câu trả lời đúng vì LLM vẫn có thể bỏ qua hoặc đọc sai context. Nhưng truy xuất kém đặt một trần rất thấp cho chất lượng trả lời.

Do đó nên đánh giá riêng:

```text
chất lượng retrieval
chất lượng context
độ trung thành của generation
độ đúng end-to-end
```

## Search như một hệ thống nhiều tầng

Kiến trúc hiện đại có thể gồm:

```text
hiểu / viết lại query
↓
retrieval ứng viên (lexical + dense)
↓
metadata / permission filter
↓
reranking
↓
đa dạng hóa / loại trùng
↓
lắp ráp context
↓
answer hoặc UI kết quả
```

Chỉ tối ưu embedding model sẽ bỏ qua phần lớn các nguyên nhân ảnh hưởng chất lượng thực tế.

## Mô hình tư duy

> Retrieval là một cái phễu: tầng đầu rẻ và rộng cố giữ bằng chứng đúng sống sót; tầng sau đắt và chính xác hơn cải thiện thứ hạng trước khi dữ liệu đi vào bước trả lời.

## Những hiểu lầm thường gặp

### “Dense Retrieval thay thế BM25”

Không. Hybrid thường mạnh vì exact lexical signal vẫn rất quan trọng.

### “Vector DB hiểu tài liệu”

Không. Nó lưu và tìm vector/metadata; chất lượng ngữ nghĩa chủ yếu đến từ embedding, chunking và dữ liệu huấn luyện.

### “Document có cosine cao nhất nên luôn đưa thẳng vào LLM”

Không. Similarity không đồng nghĩa relevance, authority, freshness hay permission; filtering và reranking vẫn cần.

### “RAG trả lời sai thì chắc chắn LLM hallucinate”

Không. Nguyên nhân có thể là retrieval miss, chunk sai, index cũ hoặc context assembly kém.

## Liên kết kiến thức

Information Retrieval nối [k-NN](../04_machine_learning/07_knn_and_distance_based_learning.md), [Contextual Embeddings](./04_contextual_embeddings.md), [Search](../02_search_reasoning_and_planning/00_state_space_and_search.md) và chuẩn bị trực tiếp cho `09_retrieval_and_rag/`.