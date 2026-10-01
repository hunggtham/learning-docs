# Dimensionality Reduction: giữ cấu trúc (structure / 구조) quan trọng trong không gian nhỏ hơn

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Dimensionality Reduction: giữ cấu trúc (structure / 구조) quan trọng trong không gian nhỏ hơn**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Tại sao dimension cao gây khó?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **PCA từ variance perspective** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

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

> **Chuyển mạch:** Trong **Dimensionality Reduction: giữ cấu trúc (structure / 구조) quan trọng trong không gian nhỏ hơn**, **PCA từ variance perspective** tiếp nhận điểm tựa từ **Tại sao dimension cao gây khó?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **PCA và reconstruction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Dimensionality Reduction: giữ cấu trúc (structure / 구조) quan trọng trong không gian nhỏ hơn**, **PCA và reconstruction** tiếp nhận điểm tựa từ **PCA từ variance perspective** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SVD liên kết (connection / 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dimensionality Reduction: giữ cấu trúc (structure / 구조) quan trọng trong không gian nhỏ hơn**, sau nội dung của **PCA và reconstruction**, **SVD liên kết (connection / 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Explained Variance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SVD liên kết (connection / 연결)

Nếu centered ma trận (matrix / 행렬):

\[
X=U\Sigma V^T
\]

thì right singular vectors trong `V` tương ứng principal directions. SVD thường được dùng thực tế vì numerical properties tốt.

Điều này nối PCA với low-rank approximation và tuyến tính (linear / 선형) Algebra.

> **Chuyển mạch:** Trong **Dimensionality Reduction: giữ cấu trúc (structure / 구조) quan trọng trong không gian nhỏ hơn**, **Explained Variance** tiếp nhận điểm tựa từ **SVD liên kết (connection / 연결)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tính năng (feature / 기능) scaling trước PCA** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Explained Variance

Explained variance ratio giúp chọn `k`:

\[
ratio_j=\frac{\lambda_j}{\sum_i\lambda_i}
\]

Cumulative explained variance 95% không có nghĩa giữ 95% “meaning”; nó giữ 95% variance theo tuyến tính (linear / 선형) covariance cấu trúc (structure / 구조).

Low-variance direction vẫn có thể cực quan trọng cho classification nếu mục tiêu (target / 대상) tín hiệu (signal / 신호) nằm ở đó.

> **Chuyển mạch:** Ở chặng này của **Dimensionality Reduction: giữ cấu trúc (structure / 구조) quan trọng trong không gian nhỏ hơn**, **Tính năng (feature / 기능) scaling trước PCA** tiếp nhận điểm tựa từ **Explained Variance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **t-SNE** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tính năng (feature / 기능) scaling trước PCA

PCA nhạy quy mô (scale / 규모) vì variance nhạy units. Nếu tính năng (feature / 기능) một có variance hàng triệu chỉ do đơn vị đo, nó có thể dominate components.

Standardization cần quyết định theo ngữ nghĩa (semantics / 의미론), không auto apply mọi trường hợp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dimensionality Reduction: giữ cấu trúc (structure / 구조) quan trọng trong không gian nhỏ hơn**, **t-SNE** tiếp nhận điểm tựa từ **Tính năng (feature / 기능) scaling trước PCA** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **UMAP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## t-SNE

t-SNE chủ yếu dành cho visualization cục bộ (local / 로컬) neighborhoods. Nó xây xác suất (probability / 확률) distributions biểu diễn pairwise similarity rồi tìm low-dimensional points giảm KL divergence giữa high/low-dimensional neighborhood distributions.

Điểm cần nhớ:

- cục bộ (local / 로컬) neighborhood thường đáng tin hơn toàn cục (global / 전역) distances;
- khoảng cách giữa hai distant clusters trên plot không nhất thiết meaningful;
- cluster kích thước (size / 크기)/shape có thể distorted;
- kết quả (result / 결과) phụ thuộc perplexity, initialization và random seed.

Không nên dùng t-SNE 2D plot như proof rằng dữ liệu (data / 데이터) “thực sự có 7 clusters”.

> **Chuyển mạch:** Trong **Dimensionality Reduction: giữ cấu trúc (structure / 구조) quan trọng trong không gian nhỏ hơn**, **UMAP** tiếp nhận điểm tựa từ **t-SNE** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Autoencoder** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## UMAP

UMAP dùng ideas từ manifold học tập (learning / 학습)/topology và nearest-neighbor graphs để giữ cục bộ (local / 로컬) cấu trúc (structure / 구조), thường quy mô (scale / 규모) tốt và preserve một phần toàn cục (global / 전역) organization hơn t-SNE trong nhiều cases.

Nhưng UMAP vẫn là nonlinear projection với hyperparameters (`n_neighbors`, `min_dist`, metric). Plot đẹp không loại bỏ need for quantitative kiểm tra hợp lệ (validation / 검증).

> **Chuyển mạch:** Ở chặng này của **Dimensionality Reduction: giữ cấu trúc (structure / 구조) quan trọng trong không gian nhỏ hơn**, **Autoencoder** tiếp nhận điểm tựa từ **UMAP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Supervised dimensionality reduction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dimensionality Reduction: giữ cấu trúc (structure / 구조) quan trọng trong không gian nhỏ hơn**, **Supervised dimensionality reduction** tiếp nhận điểm tựa từ **Autoencoder** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tính năng (feature / 기능) Selection khác Dimensionality Reduction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Supervised dimensionality reduction

PCA không dùng labels. Nếu mục tiêu prediction, supervised biểu diễn (representation / 표현) có thể giữ target-relevant directions tốt hơn.

Tuyến tính (linear / 선형) Discriminant phân tích (analysis / 분석) (LDA) tìm projection tăng between-class separation so với within-class variation dưới các giả định (assumptions / 가정들) nhất định.

Neural biểu diễn (representation / 표현) học tập (learning / 학습) là phiên bản linh hoạt hơn: hidden biểu diễn (representation / 표현) được optimized cùng downstream mục tiêu (objective / 목표).

> **Chuyển mạch:** Trong **Dimensionality Reduction: giữ cấu trúc (structure / 구조) quan trọng trong không gian nhỏ hơn**, **Tính năng (feature / 기능) Selection khác Dimensionality Reduction** tiếp nhận điểm tựa từ **Supervised dimensionality reduction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Curse vs Blessing of Dimensionality** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tính năng (feature / 기능) Selection khác Dimensionality Reduction

Tính năng (feature / 기능) selection chọn subset original features.

Dimensionality reduction thường tạo new features/components là combinations/transforms của originals.

Tính năng (feature / 기능) selection dễ interpret hơn; transformed dimensions có thể compact nhưng khó giải thích.

> **Chuyển mạch:** Ở chặng này của **Dimensionality Reduction: giữ cấu trúc (structure / 구조) quan trọng trong không gian nhỏ hơn**, **Curse vs Blessing of Dimensionality** tiếp nhận điểm tựa từ **Tính năng (feature / 기능) Selection khác Dimensionality Reduction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Embeddings và latent spaces** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Curse vs Blessing of Dimensionality

Dimension cao gây sparsity và distance problems, nhưng cũng có thể làm classes linearly separable hơn trong rich representations. Deep học tập (learning / 학습) thường cố tạo high-dimensional biểu diễn (representation / 표현) nơi tác vụ (task / 작업) trở nên dễ hơn rồi compress ở những nơi cần.

Vì vậy mục tiêu không phải “càng ít dimensions càng tốt”, mà là **biểu diễn (representation / 표현) có hình học (geometry / 기하학) phù hợp tác vụ (task / 작업) với tài nguyên (resource / 자원) ngân sách (budget / 예산) hợp lý**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dimensionality Reduction: giữ cấu trúc (structure / 구조) quan trọng trong không gian nhỏ hơn**, **Embeddings và latent spaces** tiếp nhận điểm tựa từ **Curse vs Blessing of Dimensionality** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Embeddings và latent spaces

Embedding chính là dimensional biểu diễn (representation / 표현) của discrete/complex objects như words, documents, users hoặc images.

Một document có raw vocabulary dimension hàng trăm nghìn có thể thành véc-tơ (vector / 벡터) 768 dimensions. Đây vừa là compression vừa là learned ngữ nghĩa (semantic / 의미적) hình học (geometry / 기하학).

Sau đó retrieval/clustering/classification hoạt động trong embedding không gian (space / 공간).

> **Chuyển mạch:** Trong **Dimensionality Reduction: giữ cấu trúc (structure / 구조) quan trọng trong không gian nhỏ hơn**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Embeddings và latent spaces** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Original high-dimensional observations
        ↓ choose what structure matters
Projection / learned encoder
        ↓
Compact representation
        ↓
Visualization / retrieval / clustering / prediction / compression
```

> **Chuyển mạch:** Ở chặng này của **Dimensionality Reduction: giữ cấu trúc (structure / 구조) quan trọng trong không gian nhỏ hơn**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “PCA giữ thông tin (information / 정보) nhiều nhất”

PCA giữ variance nhiều nhất trong tuyến tính (linear / 선형) projection sense, không phải mọi task-relevant thông tin (information / 정보).

### “t-SNE/UMAP thấy cluster thì cluster thật”

Projection có thể tạo/nhấn mạnh separation. Cần validate trong original/appropriate tính năng (feature / 기능) không gian (space / 공간).

### “Dimensionality reduction luôn improve mô hình (model / 모델)”

Không. Nó có thể remove useful tín hiệu (signal / 신호).

### “Embedding dimension thấp hơn raw dữ liệu (data / 데이터) nên embedding chỉ là compression”

Embedding còn thay đổi biểu diễn (representation / 표현) hình học (geometry / 기하학) để encode task-relevant relations.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dimensionality Reduction: giữ cấu trúc (structure / 구조) quan trọng trong không gian nhỏ hơn**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Xem [Linear Algebra for AI](../01_mathematical_foundations/01_linear_algebra_for_ai.md), [Clustering](./11_clustering.md) và sau này [Representation Learning](../05_neural_networks/08_representation_learning.md), [Embeddings](../08_large_language_models/02_embeddings_and_semantic_space.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
