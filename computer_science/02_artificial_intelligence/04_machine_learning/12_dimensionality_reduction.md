# Dimensionality Reduction: giữ structure quan trọng trong không gian nhỏ hơn

Dimensionality Reduction (차원 축소 / giảm chiều) tìm một representation có ít dimensions hơn nhưng vẫn giữ phần structure quan trọng của data. “Quan trọng” có thể nghĩa giữ variance, khoảng cách local, neighborhood, separability hoặc information phục vụ downstream task.

Không có một định nghĩa universal về representation tốt. Mỗi method bảo tồn một property khác nhau, vì vậy cần hiểu objective thay vì chỉ nhìn plot đẹp.

## Tại sao dimension cao gây khó?

High-dimensional data thường có:

- computation/memory cost lớn;
- noise/redundancy giữa features;
- distance concentration;
- visualization khó;
- sample density thấp;
- overfitting risk cao với finite data.

Nhưng dimension cao không tự động xấu. Nếu information useful thực sự high-dimensional, ép xuống quá thấp sẽ mất signal.

## PCA từ variance perspective

Principal Component Analysis (PCA / 주성분 분석) tìm orthogonal directions giữ variance lớn nhất.

Sau khi center data matrix `X`, covariance:

\[
\Sigma=\frac1nX^TX
\]

Principal components là eigenvectors của covariance matrix. First component:

\[
v_1=\arg\max_{\|v\|=1}Var(Xv)
\]

Các component sau orthogonal với previous components và maximize remaining variance.

Projection xuống `k` dimensions:

\[
Z=XW_k
\]

trong đó columns của `W_k` là top eigenvectors.

## PCA và reconstruction

PCA cũng có interpretation khác: trong các linear `k`-dimensional subspaces, nó minimize squared reconstruction error.

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

## SVD connection

Nếu centered matrix:

\[
X=U\Sigma V^T
\]

thì right singular vectors trong `V` tương ứng principal directions. SVD thường được dùng thực tế vì numerical properties tốt.

Điều này nối PCA với low-rank approximation và Linear Algebra.

## Explained Variance

Explained variance ratio giúp chọn `k`:

\[
ratio_j=\frac{\lambda_j}{\sum_i\lambda_i}
\]

Cumulative explained variance 95% không có nghĩa giữ 95% “meaning”; nó giữ 95% variance theo linear covariance structure.

Low-variance direction vẫn có thể cực quan trọng cho classification nếu target signal nằm ở đó.

## Feature scaling trước PCA

PCA nhạy scale vì variance nhạy units. Nếu feature một có variance hàng triệu chỉ do đơn vị đo, nó có thể dominate components.

Standardization cần quyết định theo semantics, không auto apply mọi trường hợp.

## t-SNE

t-SNE chủ yếu dành cho visualization local neighborhoods. Nó xây probability distributions biểu diễn pairwise similarity rồi tìm low-dimensional points giảm KL divergence giữa high/low-dimensional neighborhood distributions.

Điểm cần nhớ:

- local neighborhood thường đáng tin hơn global distances;
- khoảng cách giữa hai distant clusters trên plot không nhất thiết meaningful;
- cluster size/shape có thể distorted;
- result phụ thuộc perplexity, initialization và random seed.

Không nên dùng t-SNE 2D plot như proof rằng data “thực sự có 7 clusters”.

## UMAP

UMAP dùng ideas từ manifold learning/topology và nearest-neighbor graphs để giữ local structure, thường scale tốt và preserve một phần global organization hơn t-SNE trong nhiều cases.

Nhưng UMAP vẫn là nonlinear projection với hyperparameters (`n_neighbors`, `min_dist`, metric). Plot đẹp không loại bỏ need for quantitative validation.

## Autoencoder

Autoencoder học nonlinear compression:

\[
x\xrightarrow{Encoder}z\xrightarrow{Decoder}\hat x
\]

train để minimize reconstruction loss:

\[
L(x,\hat x)
\]

Latent `z` có dimension nhỏ hơn và được học từ data.

Khác PCA, autoencoder có thể learn nonlinear mapping. Nhưng nếu capacity quá lớn, latent representation không nhất thiết disentangled hoặc semantically useful.

Autoencoder dẫn sang Representation Learning và Variational Autoencoder.

## Supervised dimensionality reduction

PCA không dùng labels. Nếu mục tiêu prediction, supervised representation có thể giữ target-relevant directions tốt hơn.

Linear Discriminant Analysis (LDA) tìm projection tăng between-class separation so với within-class variation dưới assumptions nhất định.

Neural representation learning là phiên bản linh hoạt hơn: hidden representation được optimized cùng downstream objective.

## Feature Selection khác Dimensionality Reduction

Feature selection chọn subset original features.

Dimensionality reduction thường tạo new features/components là combinations/transforms của originals.

Feature selection dễ interpret hơn; transformed dimensions có thể compact nhưng khó giải thích.

## Curse vs Blessing of Dimensionality

Dimension cao gây sparsity và distance problems, nhưng cũng có thể làm classes linearly separable hơn trong rich representations. Deep Learning thường cố tạo high-dimensional representation nơi task trở nên dễ hơn rồi compress ở những nơi cần.

Vì vậy mục tiêu không phải “càng ít dimensions càng tốt”, mà là **representation có geometry phù hợp task với resource budget hợp lý**.

## Embeddings và latent spaces

Embedding chính là dimensional representation của discrete/complex objects như words, documents, users hoặc images.

Một document có raw vocabulary dimension hàng trăm nghìn có thể thành vector 768 dimensions. Đây vừa là compression vừa là learned semantic geometry.

Sau đó retrieval/clustering/classification hoạt động trong embedding space.

## Mental Model

```text
Original high-dimensional observations
        ↓ choose what structure matters
Projection / learned encoder
        ↓
Compact representation
        ↓
Visualization / retrieval / clustering / prediction / compression
```

## Common Misconceptions

### “PCA giữ information nhiều nhất”

PCA giữ variance nhiều nhất trong linear projection sense, không phải mọi task-relevant information.

### “t-SNE/UMAP thấy cluster thì cluster thật”

Projection có thể tạo/nhấn mạnh separation. Cần validate trong original/appropriate feature space.

### “Dimensionality reduction luôn improve model”

Không. Nó có thể remove useful signal.

### “Embedding dimension thấp hơn raw data nên embedding chỉ là compression”

Embedding còn thay đổi representation geometry để encode task-relevant relations.

## Knowledge Connection

Xem [Linear Algebra for AI](../01_mathematical_foundations/01_linear_algebra_for_ai.md), [Clustering](./11_clustering.md) và sau này [Representation Learning](../05_neural_networks/08_representation_learning.md), [Embeddings](../08_large_language_models/02_embeddings_and_semantic_space.md).