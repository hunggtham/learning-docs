# Retrieval, xếp hạng và xếp hạng lại

Một hệ thống retrieval tốt thường không cố dùng một model duy nhất để vừa tìm toàn corpus vừa đánh giá relevance rất chi tiết. Kiến trúc phổ biến là **xếp hạng nhiều tầng (multi-stage ranking)**: retriever tầng đầu tạo candidate set nhanh, sau đó reranker đắt hơn tinh chỉnh thứ tự.

## Tạo tập ứng viên

Mục tiêu của tầng đầu thường ưu tiên **recall**:

```text
hàng triệu chunk
→ retrieve top 50–200 candidate
```

Sparse, dense hoặc hybrid retriever phù hợp vì có thể search nhanh.

Nếu evidence đúng không xuất hiện trong candidate set, reranker phía sau không thể cứu.

## Xếp hạng lại

Reranker chấm query và candidate bằng tương tác sâu hơn.

Cross-encoder:

```text
[query ; chunk] → Transformer → relevance score
```

Nó đọc query và chunk cùng lúc nên hiểu khớp tinh hơn bi-encoder.

Chi phí tăng gần theo số candidate × độ dài document, vì vậy thường chỉ dùng sau first-stage retrieval.

## Các dạng relevance

Reranker có thể cần phân biệt:

```text
mức liên quan chủ đề
mức liên quan trực tiếp tới câu trả lời
độ mới
độ có thẩm quyền
phạm vi truy cập của người dùng
```

Một document cùng chủ đề nhưng là version cũ không nên xếp trên document hiện hành có thẩm quyền.

Một số yếu tố như quyền, version và authority thường phù hợp với metadata hoặc business rule hơn là để reranker tự suy ra.

## Hợp nhất kết quả lai

Kết quả sparse và dense có thể hợp nhất bằng RRF hoặc learned fusion.

Ví dụ:

```text
BM25 top 50
Dense top 50
→ union
→ reranker
→ top 8 chunk cho context
```

Union tăng recall; reranker giải quyết xung đột thứ hạng.

## Viết lại Query

Trước retrieval, query có thể được rewrite để:

- giải quyết đại từ và lịch sử hội thoại;
- mở rộng abbreviation;
- dịch ngôn ngữ;
- phân rã câu hỏi nhiều phần.

Bản thân rewrite cũng phải được đánh giá vì có thể làm mất qualifier quan trọng.

## Phân rã Query

Câu hỏi:

```text
"So sánh phí và điều kiện hủy của gói A và B"
```

có thể tách thành:

```text
phí của A
điều kiện hủy của A
phí của B
điều kiện hủy của B
```

Sau đó retrieve từng subquery rồi tổng hợp. Cách này hữu ích cho câu hỏi nhiều khía cạnh.

## Retrieval nhiều bước

Một số câu hỏi cần chuỗi bằng chứng:

```text
entity A → relation → entity B → property của B
```

Query ban đầu có thể không chứa term cần cho bước hai. **Multi-hop retrieval** dùng evidence bước trước để tạo query tiếp theo.

Khi đó retrieval bắt đầu gần với agentic search.

## Huấn luyện Reranker

Dữ liệu huấn luyện cần query, positive chunk và hard negative. Hard negative nên hợp lý nhưng sai, chẳng hạn:

```text
cùng sản phẩm, sai version
cùng policy, sai quốc gia
cùng chủ đề, thiếu điều kiện quan trọng
```

Những ví dụ này dạy các ranh giới tinh tế có giá trị trong production.

## Rank và hiệu chỉnh Score

Reranker score thường chỉ có ý nghĩa để sắp thứ tự trong cùng một query, không tự động là xác suất relevance tuyệt đối.

Nếu dùng threshold để abstain, cần calibration trên dữ liệu có nhãn.

## Đa dạng hóa kết quả

Top result có thể toàn bản gần trùng của cùng một paragraph. **Maximal Marginal Relevance (MMR)** cân bằng relevance và diversity:

\[
MMR=\lambda Sim(q,d)-(1-\lambda)\max_{d'\in S}Sim(d,d')
\]

Cách này hữu ích khi câu hỏi cần nhiều khía cạnh, nhưng có thể làm giảm chất lượng nếu user chỉ cần một fact chính xác duy nhất.

## Chọn Context

Sau rerank, không nên luôn lấy top-k một cách mù quáng. Context builder có thể cân nhắc:

```text
relevance
đa dạng nguồn
version / authority
ngân sách token
mức trùng lặp
neighbor context
```

Đây là một bài toán chọn có ràng buộc.

## Hiệu ứng Lost-in-the-Middle

LLM có thể sử dụng long context không đồng đều. Evidence quan trọng nằm giữa nhiều distractor có thể bị khai thác kém.

Thứ tự context vì vậy quan trọng. Có thể đặt evidence mạnh nhất sớm hoặc nhóm theo từng subquestion.

## Loại bản trùng

Near-duplicate chunk lãng phí token và có thể khiến mô hình hiểu sai rằng một fact được nhiều nguồn độc lập xác nhận.

Candidate set nên được dedup bằng content hash hoặc semantic similarity khi phù hợp.

## Ưu tiên độ mới

Với corpus nhạy thời gian, ranking có thể kết hợp relevance với freshness:

\[
score = relevance + \alpha \cdot freshness
\]

Tuy nhiên document mới nhất chưa chắc authoritative. Nếu có metadata trạng thái version, nó thường là tín hiệu tốt hơn.

## Ưu tiên nguồn có thẩm quyền

Hệ thống có thể định nghĩa hierarchy rõ:

```text
quy định chính thức > internal wiki > ghi chú chat
```

Nên mã hóa authority bằng metadata thay vì kỳ vọng embedding model tự suy ra.

## Chi phí Reranking

Nếu 100 candidate × 1000 token đều đi qua cross-encoder, latency có thể chi phối pipeline. Có thể giảm bằng:

```text
giảm số candidate
rút ngắn chunk
dùng reranker nhỏ hơn
batch scoring
late interaction
cache query lặp
```

Quality/cost curve phải được đo thực tế.

## Reranking bằng LLM

LLM có thể rerank bằng cách đọc query và candidate summary. Nó xử lý tiêu chí tinh tế nhưng đắt và có thể có position bias.

Phù hợp hơn khi candidate ít và giá trị tác vụ cao, đồng thời cần ID và thứ tự đầu vào ổn định.

## Độ tin cậy của Retrieval

Top score thấp hoặc phân bố score phẳng có thể báo không có evidence tốt. Hệ thống có thể mở rộng search, fallback sang lexical retrieval, hỏi làm rõ hoặc abstain.

Cách này tốt hơn ép mô hình luôn phải trả lời.

## Đánh giá Offline

Cần cặp query → relevant chunk/document có nhãn. Metric phổ biến:

```text
Recall@k
MRR
nDCG
Precision@k
```

Nên đo từng tầng:

```text
recall của first-stage retriever
nDCG sau rerank
recall của context cuối
```

## Mô hình tư duy

> Retrieval pipeline giống một funnel: **mở rộng recall ở đầu, tăng độ chính xác ở giữa, áp ràng buộc context ở cuối**.

## Những hiểu lầm thường gặp

### “Reranker có thể sửa lỗi retriever bỏ sót evidence”

Không nếu evidence chưa vào candidate set.

### “Top-k càng lớn càng tốt”

Không. Nhiễu và token cost cũng tăng.

### “Document mới nhất luôn đúng nhất”

Không nếu đó là draft hoặc nguồn ít thẩm quyền hơn.

## Liên kết kiến thức

Ranking nối metric IR, cross-encoder NLP, optimization và context engineering.

Xem tiếp: [Advanced RAG](./08_advanced_rag.md).