# k-Nearest Neighbors và Distance-Based học tập (learning / 학습)

> **Mạch đọc:** Đặt **k-Nearest Neighbors và Distance-Based học tập (learning / 학습)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Classification bằng neighborhood** sang **Vì sao tính năng (feature / 기능) scaling quan trọng?**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


k-Nearest Neighbors (k-NN / k-최근접 이웃 / k láng giềng gần nhất) dựa trên một intuition rất tự nhiên: những điểm gần nhau trong một biểu diễn (representation / 표현) không gian (space / 공간) thường có đầu ra (output / 출력) giống nhau. Thay vì học một parametric hàm (function / 함수) rõ ràng, k-NN giữ dữ liệu huấn luyện (training data / 학습 데이터) và đưa ra prediction dựa trên các neighbors gần nhất khi suy luận (inference / 추론).

Điểm mạnh của k-NN là làm rõ một principle rộng hơn nhiều: **mọi distance-based phương thức (method / 메서드) chỉ tốt khi hình học (geometry / 기하학) của biểu diễn (representation / 표현) thực sự mang meaning**.

## Classification bằng neighborhood

Cho truy vấn (query / 쿼리) điểm (point / 지점) `x`. Ta tính distance từ `x` tới tất cả huấn luyện (training / 학습) points, chọn `k` điểm gần nhất rồi dùng majority vote.

Với Euclidean distance:

\[
d(\mathbf x,\mathbf z)=\sqrt{\sum_j(x_j-z_j)^2}
\]

Nếu `k=5` và 4/5 neighbors thuộc lớp (class / 클래스) A, prediction là A.

Regression tương tự, nhưng thường lấy mean hoặc weighted mean của targets neighbors.

## Vì sao tính năng (feature / 기능) scaling quan trọng?

Giả sử tính năng (feature / 기능) 1 là tuổi `0–100`, tính năng (feature / 기능) 2 là annual income `0–100,000,000`. Euclidean distance gần như bị income dominate.

Standardization hoặc domain-specific normalization vì vậy không phải cosmetic preprocessing; nó định nghĩa lại hình học (geometry / 기하학) mà thuật toán (algorithm / 알고리즘) dựa vào.

## Distance chỉ số (metric / 지표) là inductive độ lệch (bias / 편향)

Euclidean distance giả định straight-line hình học (geometry / 기하학) hợp lý. Manhattan distance:

\[
d_1(x,z)=\sum_j|x_j-z_j|
\]

có hình học (geometry / 기하학) khác. Cosine similarity tập trung vào direction:

\[
cos(x,z)=\frac{x^Tz}{\|x\|\|z\|}
\]

Trong văn bản (text / 텍스트)/embedding retrieval, cosine hoặc dot sản phẩm (product / 제품) thường hợp lý hơn raw Euclidean vì ngữ nghĩa (semantic / 의미적) biểu diễn (representation / 표현) được train theo hình học (geometry / 기하학) khác.

Chọn distance tức là chọn khái niệm “giống nhau”.

## Chọn k

`k` nhỏ làm ranh giới (boundary / 경계) linh hoạt nhưng nhạy noise; `k` lớn làm prediction mượt hơn nhưng có thể wash out cục bộ (local / 로컬) cấu trúc (structure / 구조).

Đây là một biểu hiện cụ thể của độ lệch (bias / 편향)–variance sự đánh đổi (trade-off / 트레이드오프).

- `k=1`: low độ lệch (bias / 편향), high variance.
- `k` lớn: higher độ lệch (bias / 편향), lower variance.

`k` nên được chọn bằng kiểm tra hợp lệ (validation / 검증), không bằng quy tắc (rule / 규칙) cố định.

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

Trong high-dimensional không gian (space / 공간), intuitive notion “gần” bắt đầu suy yếu. Volume tăng cực nhanh, dữ liệu (data / 데이터) trở nên sparse và nearest/farthest distances có thể concentrate.

Để duy trì neighborhood density khi dimension tăng, lượng dữ liệu (data / 데이터) thường phải tăng rất mạnh.

Đây là lý do raw k-NN trên hàng nghìn noisy features thường tệ. biểu diễn (representation / 표현) học tập (learning / 학습) hoặc dimensionality reduction có thể tạo không gian (space / 공간) compact hơn nơi cục bộ (local / 로컬) distance meaningful.

## Computational chi phí (cost / 비용)

Huấn luyện (training / 학습) gần như chỉ là lưu dữ liệu (data / 데이터), nhưng suy luận (inference / 추론) naive cần so truy vấn (query / 쿼리) với `n` samples:

\[
O(nd)
\]

cho `d` dimensions.

Large-scale nearest-neighbor các hệ thống (systems / 시스템들) dùng indexing structures hoặc Approximate Nearest Neighbor (ANN): KD-tree, ball cây (tree / 트리), HNSW, IVF, sản phẩm (product / 제품) quantization...

Hiện đại (modern / 현대적) véc-tơ (vector / 벡터) cơ sở dữ liệu (database / 데이터베이스) và ngữ nghĩa (semantic / 의미적) retrieval thực chất kế thừa bài toán này ở quy mô lớn.

## k-NN và RAG

Trong Retrieval-Augmented Generation, truy vấn (query / 쿼리) được embed thành véc-tơ (vector / 벡터); retriever tìm vectors gần nhất trong corpus. Conceptually:

```text
Query
  ↓ embedding
Query vector
  ↓ nearest-neighbor search
Relevant vectors/documents
  ↓ context
LLM
```

Đây không nhất thiết là k-NN classification, nhưng cùng cốt lõi (core / 핵심) bài toán (problem / 문제): nearest-neighbor retrieval trong learned biểu diễn (representation / 표현) không gian (space / 공간).

Điểm trọng yếu (critical / 중요) là embedding mô hình (model / 모델) quyết định hình học (geometry / 기하학). véc-tơ (vector / 벡터) cơ sở dữ liệu (database / 데이터베이스) chỉ tìm kiếm (search / 검색) theo hình học (geometry / 기하학) đã có; nó không tự hiểu ngữ nghĩa (semantic / 의미적).

## Cục bộ (local / 로컬) học tập (learning / 학습) và non-parametric modeling

k-NN là **non-parametric** theo nghĩa số effective degrees of freedom có thể tăng cùng dataset, không phải “không có hyperparameter”.

Mô hình (model / 모델) không nén toàn bộ dữ liệu (data / 데이터) thành fixed-size parameter véc-tơ (vector / 벡터) như tuyến tính (linear / 선형) regression. Prediction được xây cục bộ (local / 로컬) từ stored examples.

## Quyết định (decision / 결정) ranh giới (boundary / 경계)

Với `k=1`, ranh giới (boundary / 경계) tương ứng Voronoi cells quanh huấn luyện (training / 학습) points. ranh giới (boundary / 경계) có thể rất jagged và fit noise.

Tăng `k` làm ranh giới (boundary / 경계) smoother.

Geometric view này cho thấy rõ sự đánh đổi (trade-off / 트레이드오프) giữa cục bộ (local / 로컬) fidelity và robustness.

## Missing values, categorical variables và mixed distance

Euclidean distance trên one-hot categorical dữ liệu (data / 데이터) có thể không phản ánh lĩnh vực (domain / 도메인) similarity. Mixed-type datasets đôi khi cần Gower distance hoặc custom chỉ số (metric / 지표).

Nếu missing values được impute không phù hợp, neighborhood cũng bị distort.

Distance-based học tập (learning / 학습) vì vậy phụ thuộc mạnh vào preprocessing ngữ nghĩa (semantics / 의미론).

## Mô hình tư duy (mental model / 사고 모델)

> k-NN không “học công thức”; nó đặt câu hỏi: trong biểu diễn (representation / 표현) không gian (space / 공간) này, những examples nào đủ giống truy vấn (query / 쿼리) để dùng làm bằng chứng (evidence / 증거)?

## Dùng chung (common / 공통) Misconceptions

### “k-NN không cần huấn luyện (training / 학습) nên rất nhanh”

Huấn luyện (training / 학습) nhẹ nhưng suy luận (inference / 추론) có thể đắt, nhất là dataset lớn.

### “Euclidean distance là lựa chọn tự nhiên nhất”

Không có distance universal. chỉ số (metric / 지표) phải phù hợp biểu diễn (representation / 표현) và tác vụ (task / 작업).

### “High-dimensional embedding dùng nearest neighbor nên curse of dimensionality không còn”

Learned embedding có thể tạo useful low-dimensional manifold, nhưng high-dimensional tìm kiếm (search / 검색) vẫn có sự đánh đổi (trade-off / 트레이드오프) về recall, chỉ mục (index / 인덱스), bộ nhớ (memory / 메모리) và distance hành vi (behavior / 동작).

### “véc-tơ (vector / 벡터) DB tạo ngữ nghĩa (semantic / 의미적) tìm kiếm (search / 검색)”

Véc-tơ (vector / 벡터) DB chủ yếu chỉ mục (index / 인덱스)/tìm kiếm (search / 검색) vectors. ngữ nghĩa (semantic / 의미적) chất lượng (quality / 품질) phần lớn đến từ embedding mô hình (model / 모델), chunking và retrieval thiết kế (design / 설계).

## Liên kết kiến thức (knowledge connection / 지식 연결)

k-NN nối [Linear Algebra](../01_mathematical_foundations/01_linear_algebra_for_ai.md), [Dimensionality Reduction](./12_dimensionality_reduction.md) và sau này [Vector Search/RAG](../09_retrieval_and_rag/03_vector_search.md).

Xem tiếp: [Decision Trees](./08_decision_trees.md), một family học quy tắc (rule / 규칙) partition thay vì dựa vào geometric distance.

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 what is machine learning](./00_what_is_machine_learning.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
