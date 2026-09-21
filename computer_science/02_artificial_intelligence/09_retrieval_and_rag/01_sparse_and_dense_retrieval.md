# Truy xuất thưa và truy xuất dày đặc

Hệ thống truy xuất hiện đại thường dùng hai nhóm chính: **truy xuất thưa (sparse retrieval)** dựa trên sự trùng khớp term và **truy xuất dày đặc (dense retrieval)** dựa trên biểu diễn vector học được. Hai cách tiếp cận không phải “thế hệ mới thay thế thế hệ cũ”; chúng mã hóa relevance theo hai giả định khác nhau.

## Biểu diễn thưa

Trong sparse retrieval, document và query được biểu diễn trong không gian vocabulary rất lớn, nhưng hầu hết chiều bằng `0`.

Ví dụ vocabulary:

```text
[refund, cancel, account, ekyc, passport, ...]
```

Một document chỉ kích hoạt những term xuất hiện trong nó. BM25 là ví dụ điển hình.

### Điểm mạnh

Sparse retrieval rất mạnh khi exact token mang nhiều ý nghĩa:

```text
mã lỗi EKYC_4021
product ID
số điều luật
thuật ngữ kỹ thuật hiếm
tên người / công ty
```

Nó cũng minh bạch hơn vì có thể chỉ ra term nào đã khớp.

### Điểm yếu

Nó gặp vấn đề **lệch từ vựng (vocabulary mismatch)**:

```text
query: "người dùng không đăng nhập được"
document: "authentication failure"
```

Nếu không chia sẻ term, lexical score có thể thấp dù quan hệ ngữ nghĩa cao.

## Biểu diễn dày đặc

Dense retriever dùng encoder để ánh xạ query và document thành vector:

\[
q=f_q(text),\quad d=f_d(text)
\]

Mức tương đồng có thể dùng:

\[
s(q,d)=q^T d
\]

hoặc cosine similarity.

Mô hình được huấn luyện để cặp relevant gần nhau hơn cặp không relevant.

## Bi-Encoder

Query và document được encode độc lập:

```text
query → encoder → vector q
document → encoder → vector d
```

Vector document có thể tính trước, nên retrieval nhanh bằng vector index.

Đây là kiến trúc phổ biến cho first-stage dense retrieval.

## Huấn luyện contrastive

Dense retriever thường được huấn luyện với cặp dương `(q,d+)` và các negative `d-`.

Objective kiểu softmax:

\[
P(d^+\mid q)=\frac{e^{s(q,d^+)}}{\sum_j e^{s(q,d_j)}}
\]

Mô hình học một geometry nơi document relevant có score cao hơn.

## Lấy mẫu negative

Negative quyết định retriever học được ranh giới nào.

Random negative thường quá dễ vì document hoàn toàn khác topic. **Hard negative** như tài liệu giống về lexical hoặc semantic nhưng chứa đáp án sai buộc mô hình học khác biệt tinh hơn.

Nếu negative set chứa **false negative**, tức tài liệu thực ra relevant, tín hiệu huấn luyện bị nhiễu.

## Cross-Encoder

Cross-encoder đưa query và document vào cùng một mô hình:

```text
[query ; document] → Transformer → relevance score
```

Cách này cho phép tương tác token-level sâu nên thường chính xác hơn bi-encoder, nhưng không thể precompute độc lập document representation. Chi phí quá cao để chấm hàng triệu document.

Vì vậy cross-encoder thường đóng vai trò **reranker** sau bước retrieval ứng viên.

## Late Interaction

Các kiến trúc **late interaction** giữ nhiều vector token cho query và document rồi thực hiện tương tác chi tiết hơn trong lúc scoring, trong khi vẫn cho phép pre-index phần lớn thông tin document.

Chúng nằm giữa bi-encoder và cross-encoder về chi phí và chất lượng.

## Truy xuất lai

**Hybrid retrieval** kết hợp sparse và dense:

\[
score=\alpha score_{dense}+(1-\alpha)score_{sparse}
\]

hoặc hợp nhất thứ hạng bằng Reciprocal Rank Fusion.

Hybrid thường robust với corpus doanh nghiệp vì query ngữ nghĩa và identifier chính xác cùng tồn tại.

## Reciprocal Rank Fusion

Nếu hai retriever có thang score khác nhau, cộng trực tiếp khó hiệu chỉnh. **RRF** kết hợp theo vị trí xếp hạng:

\[
RRF(d)=\sum_r \frac{1}{k+rank_r(d)}
\]

Cách này không yêu cầu raw score của các retriever nằm trên cùng một thang.

## Trôi ngữ nghĩa

Dense retriever có thể trả về document rất giống về chủ đề nhưng sai chi tiết cần trả lời.

Ví dụ query hỏi `refund within 7 days`, nhưng retriever trả policy `refund within 30 days` vì hai đoạn gần nhau về semantic.

Reranking, metadata và filter theo thời gian cần xử lý những khác biệt tinh này.

## Điểm mù với exact match

Embedding model có thể làm mượt các chuỗi hiếm. Mã lỗi `E1012` và `E1013` có thể có vector gần nhau dù ý nghĩa vận hành khác hoàn toàn.

Sparse retrieval nên được giữ để bảo toàn tín hiệu exact token.

## Truy xuất đa ngôn ngữ

Multilingual embedding có thể ánh xạ biểu thức tương đương trong tiếng Hàn, tiếng Anh và tiếng Việt vào vùng gần nhau. Điều này rất hữu ích với knowledge base đa ngôn ngữ.

Tuy nhiên chất lượng không đồng đều giữa ngôn ngữ. Enterprise eval cần kiểm tra cặp ngôn ngữ thật của hệ thống.

## Thích ứng theo domain

Embedding model tổng quát có thể không hiểu abbreviation nội bộ. Fine-tune retriever hoặc thêm training pair từ query domain có thể cải thiện geometry.

Trong nhiều trường hợp, metadata hoặc lexical alias là giải pháp đơn giản hơn và đáng tin hơn.

## Query encoder và Document encoder

Hai phía có thể dùng chung trọng số hoặc dùng encoder bất đối xứng. Query thường ngắn còn document dài, nên huấn luyện bất đối xứng có thể tối ưu cho vai trò khác nhau.

## Số lượng candidate

Top `k` quá nhỏ làm bỏ sót bằng chứng; top `k` quá lớn làm reranker và generator quá tải.

Nên chọn `k` dựa trên đường recall của retrieval và budget downstream thay vì chọn tùy ý.

## Sparse retrieval được học

Một số phương pháp dùng neural model để học trọng số term thưa, vẫn giữ hiệu quả inverted index nhưng có khả năng mở rộng ngữ nghĩa tốt hơn BM25 cổ điển.

Điểm cần nhớ: sparse/dense không hoàn toàn đồng nghĩa classical/neural.

## Mô hình tư duy

```text
Sparse → "có cùng từ hoặc identifier không?"
Dense  → "có cùng pattern ý nghĩa không?"
Hybrid → "dùng cả bằng chứng lexical và semantic geometry"
```

## Những hiểu lầm thường gặp

### “Dense luôn tốt hơn BM25”

Không, đặc biệt với corpus kỹ thuật có identifier chính xác.

### “Cosine similarity so sánh trực tiếp được giữa mọi embedding model”

Không. Phân bố score phụ thuộc mô hình, training và normalization.

### “Hybrid chỉ cần cộng hai score”

Raw score có thể không tương thích; cần normalization hoặc RRF.

## Liên kết kiến thức

Dense retrieval dựa trực tiếp vào [Embeddings](../08_large_language_models/02_embeddings_and_semantic_space.md). Sparse retrieval dựa trên inverted index và IR. RAG tốt thường kết hợp nhiều tín hiệu retrieval.

Xem tiếp: [Embeddings for Retrieval](./02_embeddings_for_retrieval.md).