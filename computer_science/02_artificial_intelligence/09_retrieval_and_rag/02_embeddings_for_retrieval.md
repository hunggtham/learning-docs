# Embedding cho truy xuất

**Truy xuất bằng embedding (embedding retrieval)** biến query và document thành vector sao cho hình học của không gian vector phản ánh mức liên quan hữu ích. Điểm quan trọng là embedding không có ý nghĩa “tự nhiên”; ý nghĩa của khoảng cách đến từ objective và dữ liệu huấn luyện.

## Từ văn bản tới vector

Một encoder tạo:

\[
z=f_\theta(text)\in\mathbb{R}^d
\]

Query và document được encode thành `q`, `d`. Retrieval dùng mức tương đồng:

\[
s(q,d)=q^Td
\]

hoặc cosine similarity:

\[
\cos(q,d)=\frac{q^Td}{\|q\|\|d\|}
\]

Nếu vector đã được chuẩn hóa L2, xếp hạng bằng dot product và cosine là tương đương.

## Vector đang biểu diễn điều gì?

Embedding có thể mã hóa sự tương đồng chủ đề, intent, tương đương ngữ nghĩa hoặc relevance theo tác vụ tùy cách huấn luyện. Một general sentence embedding không nhất thiết tối ưu cho truy xuất question→answer.

Ví dụ:

```text
query: "How do I reset my password?"
positive doc: "Password recovery steps"
```

Dữ liệu huấn luyện nên chứa các cặp query–document tương tự để geometry phản ánh đúng retrieval intent.

## Pooling

Transformer tạo biểu diễn theo token. Để có một vector cho toàn đoạn văn, encoder cần một chiến lược **pooling** như:

- CLS token;
- mean pooling;
- weighted pooling;
- learned pooling.

Pooling ảnh hưởng chất lượng retrieval. Mean pooling đơn giản nhưng có thể làm loãng token quan trọng trong chunk dài.

## Chuẩn hóa vector

Embedding thường được chuẩn hóa:

\[
\hat z=\frac{z}{\|z\|}
\]

để score ổn định hơn. Tuy nhiên không phải mọi model đều được huấn luyện với cùng giả định; cần theo đúng hướng dẫn của embedding model.

## Số chiều

Vector nhiều chiều có capacity lớn hơn nhưng làm tăng dung lượng và chi phí index. Với `N` vector dimension `d` kiểu float32:

\[
storage\approx N\cdot d\cdot 4\ bytes
\]

Một triệu vector × 1536 chiều cần khoảng 6.1 GB chỉ cho raw vector, chưa tính index và metadata.

Giảm chiều hoặc index đã lượng tử hóa có thể giảm chi phí.

## Prefix cho Query và Document

Một số embedding model được huấn luyện với prefix như:

```text
query: ...
passage: ...
```

Prefix không chỉ để trang trí; nó báo vai trò cho mô hình trong huấn luyện bất đối xứng. Bỏ prefix có thể làm giảm hiệu quả.

## Embedding theo chunk

RAG thường embedding chunk thay vì cả document. Vector của chunk phải giữ đủ context cục bộ để query có thể match.

Nếu chunk chỉ chứa một row của bảng mà mất header, embedding có thể mất semantics. Pipeline ingestion có thể thêm tiêu đề section hoặc metadata document trước khi embedding.

## Metadata trong embedding và metadata làm filter

Có thể nối metadata vào text trước khi embedding:

```text
Title: Refund Policy
Product: Card
Content: ...
```

Tuy nhiên constraint xác định như access level, tenant hoặc version vẫn nên dùng filter. Không nên dựa vào vector geometry để cưỡng chế authorization.

## Hard Negative

Fine-tune retriever thường cần **hard negative**. Ví dụ query hỏi policy cho `credit card`, còn negative là policy gần như giống hệt nhưng dành cho `debit card`.

Mô hình nhờ đó học khác biệt quan trọng mà semantic similarity tổng quát dễ bỏ qua.

## In-Batch Negative

Trong contrastive training, positive của sample khác trong cùng batch thường được dùng làm negative. Cách này hiệu quả về compute nhưng có nguy cơ **false negative** nếu hai query thật sự cùng relevant với một document.

Cách tạo batch vì vậy ảnh hưởng tín hiệu học.

## Embedding có thể cắt ngắn

Một số model được huấn luyện theo kiểu Matryoshka để phần prefix dimension vẫn dùng được, cho phép giảm chiều nhằm đổi chất lượng lấy storage hoặc latency.

Đây là thuộc tính phải được huấn luyện; không thể mặc định cắt mọi embedding vector mà không mất cấu trúc.

## Embedding đa ngôn ngữ

Multilingual embedding có thể ánh xạ các biểu thức tương đương:

```text
"hoàn tiền"
"refund"
"환불"
```

vào vùng gần nhau trong cùng không gian.

Nhưng truy xuất xuyên ngôn ngữ cần được đánh giá riêng vì mất cân bằng dữ liệu có thể tạo khoảng cách chất lượng giữa các ngôn ngữ.

## Embedding cho code

Code search có semantics khác prose. Function signature, identifier và behavior đều quan trọng. Embedding model chuyên cho code thường phù hợp hơn generic text embedding.

## Ngưỡng similarity

Một lỗi phổ biến là hard-code kiểu `cosine > 0.8 = relevant`. Phân bố score phụ thuộc model, corpus và loại query.

Ngưỡng phải được calibration trên dữ liệu retrieval có nhãn.

Top-k ranking thường dễ chuyển hơn absolute threshold, nhưng quyết định abstain hoặc “không có bằng chứng” vẫn cần calibration.

## Embedding drift

Khi thay embedding model, vector cũ và mới thường không còn nằm trong cùng không gian. Query bằng model mới không nên tìm trực tiếp trên vector cũ trừ khi nhà thiết kế bảo đảm compatibility.

Migration cần re-embed corpus hoặc duy trì hai index trong giai đoạn chuyển đổi.

## Versioning

Nên lưu metadata:

```text
embedding_model_version
chunker_version
source_version
created_at
```

Nếu retrieval regression xảy ra, team cần biết index được tạo bằng pipeline nào.

## Quyền riêng tư

Không nên giả định embedding là không thể đảo ngược. Vector có thể làm lộ thông tin ngữ nghĩa hoặc nội dung. Quyền truy cập vector database nên tuân cùng mức nhạy cảm với source data.

## Đánh giá

Chất lượng embedding nên được đo bằng retrieval task:

```text
Recall@k
MRR
nDCG
khả năng phân biệt hard negative
các lát cắt đa ngôn ngữ
```

Visualization vector đẹp không phải bằng chứng đủ cho chất lượng production.

## Mô hình tư duy

> Embedding là **hệ tọa độ được học cho một retrieval objective**. Khoảng cách có ý nghĩa vì mô hình được huấn luyện để đưa các item relevant lại gần nhau, không phải vì vector tự mang “sự thật ngữ nghĩa”.

## Những hiểu lầm thường gặp

### “Embedding giống hash của câu”

Không. Input tương tự có thể nằm gần nhau và vector là một biểu diễn mất mát.

### “Nhiều chiều hơn luôn tốt hơn”

Không. Chi phí tăng còn tín hiệu hữu ích phụ thuộc cách huấn luyện.

### “Có thể thay metadata filter bằng embedding”

Không với constraint về bảo mật, tenant hoặc version.

## Liên kết kiến thức

Xem [Linear Algebra](../01_mathematical_foundations/01_linear_algebra_for_ai.md), [LLM Embeddings](../08_large_language_models/02_embeddings_and_semantic_space.md), và tiếp theo [Vector Search](./03_vector_search.md).