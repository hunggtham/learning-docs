# k-Nearest Neighbors và Distance-Based Learning

k-Nearest Neighbors (k-NN / k-최근접 이웃 / k láng giềng gần nhất) dựa trên một intuition rất tự nhiên: những điểm gần nhau trong một representation space thường có output giống nhau. Thay vì học một parametric function rõ ràng, k-NN giữ training data và đưa ra prediction dựa trên các neighbors gần nhất khi inference.

Điểm mạnh của k-NN là làm rõ một principle rộng hơn nhiều: **mọi distance-based method chỉ tốt khi geometry của representation thực sự mang meaning**.

## Classification bằng neighborhood

Cho query point `x`. Ta tính distance từ `x` tới tất cả training points, chọn `k` điểm gần nhất rồi dùng majority vote.

Với Euclidean distance:

\[
d(\mathbf x,\mathbf z)=\sqrt{\sum_j(x_j-z_j)^2}
\]

Nếu `k=5` và 4/5 neighbors thuộc class A, prediction là A.

Regression tương tự, nhưng thường lấy mean hoặc weighted mean của targets neighbors.

## Vì sao feature scaling quan trọng?

Giả sử feature 1 là tuổi `0–100`, feature 2 là annual income `0–100,000,000`. Euclidean distance gần như bị income dominate.

Standardization hoặc domain-specific normalization vì vậy không phải cosmetic preprocessing; nó định nghĩa lại geometry mà algorithm dựa vào.

## Distance metric là inductive bias

Euclidean distance giả định straight-line geometry hợp lý. Manhattan distance:

\[
d_1(x,z)=\sum_j|x_j-z_j|
\]

có geometry khác. Cosine similarity tập trung vào direction:

\[
cos(x,z)=\frac{x^Tz}{\|x\|\|z\|}
\]

Trong text/embedding retrieval, cosine hoặc dot product thường hợp lý hơn raw Euclidean vì semantic representation được train theo geometry khác.

Chọn distance tức là chọn khái niệm “giống nhau”.

## Chọn k

`k` nhỏ làm boundary linh hoạt nhưng nhạy noise; `k` lớn làm prediction mượt hơn nhưng có thể wash out local structure.

Đây là một biểu hiện cụ thể của bias–variance trade-off.

- `k=1`: low bias, high variance.
- `k` lớn: higher bias, lower variance.

`k` nên được chọn bằng validation, không bằng rule cố định.

## Weighted k-NN

Neighbors gần hơn có thể được weight cao hơn:

\[
w_i=\frac{1}{d(x,x_i)+\epsilon}
\]

Regression prediction:

\[
\hat y=\frac{\sum_iw_iy_i}{\sum_iw_i}
\]

Weighted voting giúp giảm việc neighbor ở rìa có influence ngang neighbor cực gần.

## Curse of Dimensionality

Trong high-dimensional space, intuitive notion “gần” bắt đầu suy yếu. Volume tăng cực nhanh, data trở nên sparse và nearest/farthest distances có thể concentrate.

Để duy trì neighborhood density khi dimension tăng, lượng data thường phải tăng rất mạnh.

Đây là lý do raw k-NN trên hàng nghìn noisy features thường tệ. Representation learning hoặc dimensionality reduction có thể tạo space compact hơn nơi local distance meaningful.

## Computational cost

Training gần như chỉ là lưu data, nhưng inference naive cần so query với `n` samples:

\[
O(nd)
\]

cho `d` dimensions.

Large-scale nearest-neighbor systems dùng indexing structures hoặc Approximate Nearest Neighbor (ANN): KD-tree, ball tree, HNSW, IVF, product quantization...

Modern vector database và semantic retrieval thực chất kế thừa bài toán này ở quy mô lớn.

## k-NN và RAG

Trong Retrieval-Augmented Generation, query được embed thành vector; retriever tìm vectors gần nhất trong corpus. Conceptually:

```text
Query
  ↓ embedding
Query vector
  ↓ nearest-neighbor search
Relevant vectors/documents
  ↓ context
LLM
```

Đây không nhất thiết là k-NN classification, nhưng cùng core problem: nearest-neighbor retrieval trong learned representation space.

Điểm critical là embedding model quyết định geometry. Vector database chỉ search theo geometry đã có; nó không tự hiểu semantic.

## Local learning và non-parametric modeling

k-NN là **non-parametric** theo nghĩa số effective degrees of freedom có thể tăng cùng dataset, không phải “không có hyperparameter”.

Model không nén toàn bộ data thành fixed-size parameter vector như linear regression. Prediction được xây local từ stored examples.

## Decision boundary

Với `k=1`, boundary tương ứng Voronoi cells quanh training points. Boundary có thể rất jagged và fit noise.

Tăng `k` làm boundary smoother.

Geometric view này cho thấy rõ trade-off giữa local fidelity và robustness.

## Missing values, categorical variables và mixed distance

Euclidean distance trên one-hot categorical data có thể không phản ánh domain similarity. Mixed-type datasets đôi khi cần Gower distance hoặc custom metric.

Nếu missing values được impute không phù hợp, neighborhood cũng bị distort.

Distance-based learning vì vậy phụ thuộc mạnh vào preprocessing semantics.

## Mental Model

> k-NN không “học công thức”; nó đặt câu hỏi: trong representation space này, những examples nào đủ giống query để dùng làm evidence?

## Common Misconceptions

### “k-NN không cần training nên rất nhanh”

Training nhẹ nhưng inference có thể đắt, nhất là dataset lớn.

### “Euclidean distance là lựa chọn tự nhiên nhất”

Không có distance universal. Metric phải phù hợp representation và task.

### “High-dimensional embedding dùng nearest neighbor nên curse of dimensionality không còn”

Learned embedding có thể tạo useful low-dimensional manifold, nhưng high-dimensional search vẫn có trade-off về recall, index, memory và distance behavior.

### “Vector DB tạo semantic search”

Vector DB chủ yếu index/search vectors. Semantic quality phần lớn đến từ embedding model, chunking và retrieval design.

## Knowledge Connection

k-NN nối [Linear Algebra](../01_mathematical_foundations/01_linear_algebra_for_ai.md), [Dimensionality Reduction](./12_dimensionality_reduction.md) và sau này [Vector Search/RAG](../09_retrieval_and_rag/03_vector_search.md).

Xem tiếp: [Decision Trees](./08_decision_trees.md), một family học rule partition thay vì dựa vào geometric distance.