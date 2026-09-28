# Dimensionality Reduction: giữ cấu trúc (structure / 구조) quan trọng trong không gian nhỏ hơn

> **Mạch đọc:** Đặt **Dimensionality Reduction: giữ cấu trúc (structure / 구조) quan trọng trong không gian nhỏ hơn** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Tại sao dimension cao gây khó?** sang **PCA từ variance perspective**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Dimensionality Reduction (차원 축소 / giảm chiều) tìm một biểu diễn (representation / 표현) có ít dimensions hơn nhưng vẫn giữ phần cấu trúc (structure / 구조) quan trọng của dữ liệu (data / 데이터). “Quan trọng” có thể nghĩa giữ variance, khoảng cách cục bộ (local / 로컬), neighborhood, separability hoặc thông tin (information / 정보) phục vụ downstream tác vụ (task / 작업).

Không có một định nghĩa universal về biểu diễn (representation / 표현) tốt. Mỗi phương thức (method / 메서드) bảo tồn một thuộc tính (property / 속성) khác nhau, vì vậy cần hiểu mục tiêu (objective / 목표) thay vì chỉ nhìn plot đẹp.

## Tại sao dimension cao gây khó?

High-dimensional dữ liệu (data / 데이터) thường có:

- computation/bộ nhớ (memory / 메모리) chi phí (cost / 비용) lớn;
- noise/redundancy giữa features;
- distance concentration;
- visualization khó;
- mẫu (sample / 표본) density thấp;
- overfitting rủi ro (risk / 위험) cao với finite dữ liệu (data / 데이터).

Nhưng dimension cao không tự động xấu. Nếu thông tin (information / 정보) useful thực sự high-dimensional, ép xuống quá thấp sẽ mất tín hiệu (signal / 신호).

## PCA từ variance perspective

Principal thành phần (component / 컴포넌트) phân tích (analysis / 분석) tìm orthogonal directions giữ variance lớn nhất.

Sau khi center dữ liệu (data / 데이터) ma trận (matrix / 행렬) `X`, covariance:

\[
\Sigma=\frac1nX^TX
\]

Principal components là eigenvectors của covariance ma trận (matrix / 행렬). First thành phần (component / 컴포넌트):

\[
v_1=\arg\max_{\|v\|=1}Var(Xv)
\]

Các thành phần (component / 컴포넌트) sau orthogonal với previous components và maximize remaining variance.

Projection xuống `k` dimensions:

\[
Z=XW_k
\]

trong đó columns của `W_k` là top eigenvectors.

## PCA và reconstruction

PCA cũng có interpretation khác: trong các tuyến tính (linear / 선형) `k`-dimensional subspaces, nó minimize squared reconstruction lỗi (error / 오류).

Nếu reconstruct:

\[
\hat X=ZW_k^T
\]

PCA chọn subspace làm:

\[
\|X-\hat X\|_F^2
\]

nhỏ nhất.

Variance maximization và reconstruction minimization là hai mặt của cùng bài toán.

## SVD liên kết (connection / 연결)

Nếu centered ma trận (matrix / 행렬):

\[
X=U\Sigma V^T
\]

thì right singular vectors trong `V` tương ứng principal directions. SVD thường được dùng thực tế vì numerical properties tốt.

Điều này nối PCA với low-rank approximation và tuyến tính (linear / 선형) Algebra.

## Explained Variance

Explained variance ratio giúp chọn `k`:

\[
ratio_j=\frac{\lambda_j}{\sum_i\lambda_i}
\]

Cumulative explained variance 95% không có nghĩa giữ 95% “meaning”; nó giữ 95% variance theo tuyến tính (linear / 선형) covariance cấu trúc (structure / 구조).

Low-variance direction vẫn có thể cực quan trọng cho classification nếu mục tiêu (target / 대상) tín hiệu (signal / 신호) nằm ở đó.

## Tính năng (feature / 기능) scaling trước PCA

PCA nhạy quy mô (scale / 규모) vì variance nhạy units. Nếu tính năng (feature / 기능) một có variance hàng triệu chỉ do đơn vị đo, nó có thể dominate components.

Standardization cần quyết định theo ngữ nghĩa (semantics / 의미론), không auto apply mọi trường hợp.

## t-SNE

t-SNE chủ yếu dành cho visualization cục bộ (local / 로컬) neighborhoods. Nó xây xác suất (probability / 확률) distributions biểu diễn pairwise similarity rồi tìm low-dimensional points giảm KL divergence giữa high/low-dimensional neighborhood distributions.

Điểm cần nhớ:

- cục bộ (local / 로컬) neighborhood thường đáng tin hơn toàn cục (global / 전역) distances;
- khoảng cách giữa hai distant clusters trên plot không nhất thiết meaningful;
- cluster kích thước (size / 크기)/shape có thể distorted;
- kết quả (result / 결과) phụ thuộc perplexity, initialization và random seed.

Không nên dùng t-SNE 2D plot như proof rằng dữ liệu (data / 데이터) “thực sự có 7 clusters”.

## UMAP

UMAP dùng ideas từ manifold học tập (learning / 학습)/topology và nearest-neighbor graphs để giữ cục bộ (local / 로컬) cấu trúc (structure / 구조), thường quy mô (scale / 규모) tốt và preserve một phần toàn cục (global / 전역) organization hơn t-SNE trong nhiều cases.

Nhưng UMAP vẫn là nonlinear projection với hyperparameters (`n_neighbors`, `min_dist`, metric). Plot đẹp không loại bỏ need for quantitative kiểm tra hợp lệ (validation / 검증).

## Autoencoder

Autoencoder học nonlinear compression:

\[
x\xrightarrow{Encoder}z\xrightarrow{Decoder}\hat x
\]

train để minimize reconstruction mất mát (loss / 손실):

\[
L(x,\hat x)
\]

Latent `z` có dimension nhỏ hơn và được học từ dữ liệu (data / 데이터).

Khác PCA, autoencoder có thể learn nonlinear ánh xạ (mapping / 매핑). Nhưng nếu sức chứa (capacity / 용량) quá lớn, latent biểu diễn (representation / 표현) không nhất thiết disentangled hoặc semantically useful.

Autoencoder dẫn sang biểu diễn (representation / 표현) học tập (learning / 학습) và Variational Autoencoder.

## Supervised dimensionality reduction

PCA không dùng labels. Nếu mục tiêu prediction, supervised biểu diễn (representation / 표현) có thể giữ target-relevant directions tốt hơn.

Tuyến tính (linear / 선형) Discriminant phân tích (analysis / 분석) (LDA) tìm projection tăng between-class separation so với within-class variation dưới các giả định (assumptions / 가정들) nhất định.

Neural biểu diễn (representation / 표현) học tập (learning / 학습) là phiên bản linh hoạt hơn: hidden biểu diễn (representation / 표현) được optimized cùng downstream mục tiêu (objective / 목표).

## Tính năng (feature / 기능) Selection khác Dimensionality Reduction

Tính năng (feature / 기능) selection chọn subset original features.

Dimensionality reduction thường tạo new features/components là combinations/transforms của originals.

Tính năng (feature / 기능) selection dễ interpret hơn; transformed dimensions có thể compact nhưng khó giải thích.

## Curse vs Blessing of Dimensionality

Dimension cao gây sparsity và distance problems, nhưng cũng có thể làm classes linearly separable hơn trong rich representations. Deep học tập (learning / 학습) thường cố tạo high-dimensional biểu diễn (representation / 표현) nơi tác vụ (task / 작업) trở nên dễ hơn rồi compress ở những nơi cần.

Vì vậy mục tiêu không phải “càng ít dimensions càng tốt”, mà là **biểu diễn (representation / 표현) có hình học (geometry / 기하학) phù hợp tác vụ (task / 작업) với tài nguyên (resource / 자원) ngân sách (budget / 예산) hợp lý**.

## Embeddings và latent spaces

Embedding chính là dimensional biểu diễn (representation / 표현) của discrete/complex objects như words, documents, users hoặc images.

Một document có raw vocabulary dimension hàng trăm nghìn có thể thành véc-tơ (vector / 벡터) 768 dimensions. Đây vừa là compression vừa là learned ngữ nghĩa (semantic / 의미적) hình học (geometry / 기하학).

Sau đó retrieval/clustering/classification hoạt động trong embedding không gian (space / 공간).

## Mô hình tư duy (mental model / 사고 모델)

```text
Original high-dimensional observations
        ↓ choose what structure matters
Projection / learned encoder
        ↓
Compact representation
        ↓
Visualization / retrieval / clustering / prediction / compression
```

## Dùng chung (common / 공통) Misconceptions

### “PCA giữ thông tin (information / 정보) nhiều nhất”

PCA giữ variance nhiều nhất trong tuyến tính (linear / 선형) projection sense, không phải mọi task-relevant thông tin (information / 정보).

### “t-SNE/UMAP thấy cluster thì cluster thật”

Projection có thể tạo/nhấn mạnh separation. Cần validate trong original/appropriate tính năng (feature / 기능) không gian (space / 공간).

### “Dimensionality reduction luôn improve mô hình (model / 모델)”

Không. Nó có thể remove useful tín hiệu (signal / 신호).

### “Embedding dimension thấp hơn raw dữ liệu (data / 데이터) nên embedding chỉ là compression”

Embedding còn thay đổi biểu diễn (representation / 표현) hình học (geometry / 기하학) để encode task-relevant relations.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Xem [Linear Algebra for AI](../01_mathematical_foundations/01_linear_algebra_for_ai.md), [Clustering](./11_clustering.md) và sau này [Representation Learning](../05_neural_networks/08_representation_learning.md), [Embeddings](../08_large_language_models/02_embeddings_and_semantic_space.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 what is machine learning](./00_what_is_machine_learning.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
