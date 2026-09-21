# k-Nearest Neighbors và học dựa trên khoảng cách

**k-Nearest Neighbors (k-NN / k-최근접 이웃 / k láng giềng gần nhất)** dựa trên một trực giác rất tự nhiên: các điểm gần nhau trong một không gian biểu diễn thường có đầu ra tương tự nhau. Thay vì học một hàm tham số rõ ràng, k-NN giữ lại dữ liệu huấn luyện và tạo dự đoán dựa trên những láng giềng gần nhất tại thời điểm suy luận.

Điểm quan trọng của k-NN không chỉ nằm ở chính thuật toán này. Nó giúp làm rõ một nguyên lý rộng hơn: **mọi phương pháp dựa trên khoảng cách chỉ hoạt động tốt khi hình học của không gian biểu diễn thật sự phản ánh ý nghĩa của bài toán**.

## Phân loại bằng vùng lân cận

Với một điểm truy vấn `x`, ta tính khoảng cách từ `x` tới các điểm trong training set, chọn `k` điểm gần nhất rồi dùng bỏ phiếu đa số.

Khoảng cách Euclid:

\[
d(\mathbf x,\mathbf z)=\sqrt{\sum_j(x_j-z_j)^2}
\]

Nếu `k=5` và 4 trong 5 láng giềng thuộc lớp A, dự đoán sẽ là A.

Với bài toán hồi quy, cách làm tương tự nhưng đầu ra thường là trung bình hoặc trung bình có trọng số của target từ các láng giềng.

## Vì sao scale của feature rất quan trọng?

Giả sử feature thứ nhất là tuổi trong khoảng `0–100`, còn feature thứ hai là thu nhập năm trong khoảng `0–100,000,000`. Nếu dùng Euclidean distance trực tiếp, khoảng cách gần như bị feature thu nhập chi phối hoàn toàn.

Vì vậy standardization hoặc normalization theo domain không phải bước tiền xử lý mang tính “trang trí”; nó trực tiếp định nghĩa lại hình học mà thuật toán dựa vào.

## Metric khoảng cách chính là một thiên lệch quy nạp

Euclidean distance giả định hình học đường thẳng là phù hợp với ý nghĩa của bài toán.

Khoảng cách Manhattan:

\[
d_1(x,z)=\sum_j|x_j-z_j|
\]

định nghĩa một hình học khác.

Cosine similarity tập trung vào hướng của vector:

\[
cos(x,z)=\frac{x^Tz}{\|x\|\|z\|}
\]

Trong retrieval văn bản hoặc embedding, cosine similarity hoặc dot product thường phù hợp hơn Euclidean distance thô vì representation đã được huấn luyện để mang ý nghĩa theo một hình học khác.

Nói cách khác, **chọn metric khoảng cách chính là chọn định nghĩa “hai điểm giống nhau tới mức nào”**.

## Chọn giá trị k

`k` nhỏ làm ranh giới quyết định linh hoạt hơn nhưng nhạy với nhiễu.

`k` lớn làm dự đoán mượt hơn nhưng có thể làm mất cấu trúc cục bộ.

Đây là một biểu hiện cụ thể của sự đánh đổi bias–variance:

```text
k = 1      → bias thấp, variance cao
k lớn hơn  → bias tăng, variance giảm
```

Không có một giá trị `k` chuẩn cho mọi bài toán. Nên chọn bằng validation trên dữ liệu đại diện.

## k-NN có trọng số

Có thể cho láng giềng gần hơn trọng số lớn hơn:

\[
w_i=\frac{1}{d(x,x_i)+\epsilon}
\]

Trong hồi quy:

\[
\hat y=\frac{\sum_iw_iy_i}{\sum_iw_i}
\]

Cách này tránh tình trạng một điểm nằm sát query và một điểm nằm gần rìa neighborhood có ảnh hưởng ngang nhau.

## Lời nguyền số chiều

Trong không gian nhiều chiều, trực giác về “gần” bắt đầu suy yếu. Thể tích không gian tăng rất nhanh, dữ liệu trở nên thưa và khoảng cách từ một điểm tới láng giềng gần nhất hoặc xa nhất có thể trở nên ít khác biệt hơn.

Đây là **lời nguyền số chiều (curse of dimensionality)**.

Để duy trì mật độ neighborhood tương tự khi số chiều tăng, lượng dữ liệu thường phải tăng rất mạnh.

Vì vậy k-NN trực tiếp trên hàng nghìn feature nhiễu thường hoạt động kém. Representation learning hoặc dimensionality reduction có thể tạo một không gian gọn hơn nơi khoảng cách cục bộ mang nhiều ý nghĩa hơn.

## Chi phí tính toán

Phần “training” của k-NN gần như chỉ là lưu dữ liệu. Nhưng suy luận ngây thơ phải so query với `n` mẫu:

\[
O(nd)
\]

với `d` là số chiều.

Ở quy mô lớn, hệ thống tìm kiếm láng giềng sử dụng các chỉ mục hoặc thuật toán **Approximate Nearest Neighbor (ANN)** như KD-tree, ball tree, HNSW, IVF hoặc product quantization.

Vector database và semantic retrieval hiện đại thực chất kế thừa cùng bài toán nearest-neighbor search ở quy mô lớn hơn.

## k-NN và RAG

Trong Retrieval-Augmented Generation, query thường được chuyển thành embedding rồi hệ truy xuất tìm các vector gần nhất trong corpus:

```text
Query
  ↓ embedding
Vector truy vấn
  ↓ tìm láng giềng gần nhất
Vector / tài liệu liên quan
  ↓ đưa vào context
LLM
```

Đây không nhất thiết là k-NN classification, nhưng cùng dựa trên bài toán lõi: tìm các điểm gần query trong một không gian biểu diễn đã học.

Điểm quan trọng là embedding model quyết định hình học của không gian. Vector database chỉ lập chỉ mục và tìm kiếm trên hình học đó; nó không tự tạo ra “ý nghĩa ngữ nghĩa”.

## Học cục bộ và mô hình phi tham số

k-NN được gọi là **phi tham số (non-parametric)** vì độ phức tạp hiệu dụng của mô hình có thể tăng cùng lượng dữ liệu, không phải vì “không có hyperparameter”.

Khác với Linear Regression, k-NN không nén toàn bộ training set thành một vector tham số cố định. Dự đoán được xây dựng cục bộ từ chính các example đã lưu.

## Ranh giới quyết định

Với `k=1`, ranh giới quyết định tương ứng với các ô Voronoi xung quanh từng training point. Ranh giới này có thể rất ngoằn ngoèo và bám sát noise.

Khi tăng `k`, ranh giới thường mượt hơn.

Cách nhìn hình học này làm rõ sự đánh đổi giữa khả năng bám sát cấu trúc cục bộ và độ bền trước nhiễu.

## Dữ liệu thiếu, feature phân loại và khoảng cách hỗn hợp

Euclidean distance trên dữ liệu one-hot không phải lúc nào cũng phản ánh similarity thực tế giữa các category.

Với dataset trộn nhiều kiểu dữ liệu, đôi khi cần metric như Gower distance hoặc một hàm khoảng cách tùy chỉnh theo domain.

Nếu missing value được impute không phù hợp, vị trí của điểm trong không gian cũng bị méo và neighborhood trở nên sai.

Vì vậy các phương pháp dựa trên khoảng cách phụ thuộc đặc biệt mạnh vào ý nghĩa của bước tiền xử lý.

## Mô hình tư duy

> k-NN không học một công thức tổng quát; nó hỏi: trong không gian biểu diễn hiện tại, những example nào đủ giống query để dùng làm bằng chứng cho dự đoán?

## Các hiểu lầm thường gặp

### “k-NN không cần training nên rất nhanh”

Training nhẹ, nhưng inference có thể rất đắt khi dataset lớn.

### “Euclidean distance là lựa chọn tự nhiên nhất”

Không có metric khoảng cách nào tốt cho mọi representation và mọi task.

### “Embedding nhiều chiều dùng nearest neighbor nên curse of dimensionality không còn”

Không. Learned embedding có thể tạo manifold hữu ích hơn, nhưng high-dimensional search vẫn có trade-off về recall, index, memory và hành vi khoảng cách.

### “Vector database tự tạo semantic search”

Không. Vector database chủ yếu lập chỉ mục và tìm kiếm vector. Chất lượng semantic search phụ thuộc rất nhiều vào embedding model, chunking và thiết kế retrieval.

## Liên kết kiến thức

k-NN nối [Đại số tuyến tính](../01_mathematical_foundations/01_linear_algebra_for_ai.md), [Giảm chiều](./12_dimensionality_reduction.md) và phần [Vector Search/RAG](../09_retrieval_and_rag/03_vector_search.md) phía sau.

Xem tiếp: [Decision Tree](./08_decision_trees.md), một họ mô hình học các quy tắc chia không gian thay vì dựa trực tiếp vào khoảng cách hình học.