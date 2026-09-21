# Linear Algebra cho Artificial Intelligence

Linear Algebra (선형대수 / đại số tuyến tính) là ngôn ngữ dùng để biểu diễn nhiều đại lượng cùng lúc và mô tả cách chúng được biến đổi. Trong AI hiện đại, một sample hiếm khi chỉ là một số. Một ảnh có hàng trăm nghìn pixel, một câu trở thành hàng chục hoặc hàng nghìn token, một embedding có hàng trăm đến hàng nghìn dimension, còn một neural network có thể xử lý hàng nghìn sample song song trong một batch. Linear Algebra giúp gom các quantity này thành vector, matrix và tensor để computation có thể được mô tả rõ ràng và chạy hiệu quả trên hardware.

Điểm quan trọng nhất không phải học thuộc phép nhân ma trận. Ta cần nhìn matrix như một **transformation giữa các spaces**, vector như một **representation**, và dot product như một phép đo **alignment**. Khi mental model này rõ, nhiều công thức trong Machine Learning, embeddings và Transformer trở nên tự nhiên hơn.

Xem bản đồ tổng quan: [Mathematics for AI](./00_mathematics_for_ai.md).

## Scalar, vector, matrix và tensor

Một **scalar (스칼라)** là một giá trị đơn, ví dụ temperature `23.5`, learning rate `0.001`, hoặc loss `2.3`.

Một **vector (벡터)** là một ordered list các số. Nếu khách hàng được biểu diễn bằng tuổi, thu nhập và số lần mua hàng, ta có thể viết:

\[
\mathbf{x}=\begin{bmatrix}31\\4200\\7\end{bmatrix}
\]

Vector này không phải chính khách hàng. Nó là một representation được chọn để giữ những properties ta cho là relevant với task.

Một **matrix (행렬)** là bảng số hai chiều. Nếu mỗi row là một sample và mỗi column là một feature:

\[
X=\begin{bmatrix}
31 & 4200 & 7\\
28 & 3500 & 3\\
45 & 6700 & 12
\end{bmatrix}
\]

thì `X` có shape `3 × 3`.

Một **tensor (텐서)** trong Deep Learning thường được dùng theo nghĩa practical là array nhiều chiều. Ví dụ batch ảnh RGB có shape:

```text
batch × height × width × channels
32 × 224 × 224 × 3
```

Trong PyTorch convention thường gặp `N × C × H × W`, trong khi một số framework hoặc format khác dùng `N × H × W × C`. Shape không phải chi tiết nhỏ; rất nhiều bug ML đơn giản là tensor có đúng values nhưng sai axis.

## Vector space: representation sống ở đâu?

Một vector không chỉ là list numbers. Khi ta nói:

\[
\mathbf{x}\in\mathbb{R}^d
\]

ta nói `x` là một point trong vector space `d` chiều.

Nếu embedding model map một sentence thành vector 768 chiều, sentence đó được biến thành một point trong `R^768`. Nhưng geometry trong space này chỉ có ý nghĩa vì training objective đã tạo structure. Không có training phù hợp, hai câu cùng nghĩa không tự nhiên trở thành hai vector gần nhau.

Đây là nguyên lý quan trọng:

> Geometry của embedding space không phải meaning “có sẵn”; nó là structure được học từ objective và data.

## Addition và scalar multiplication

Hai operations cơ bản của vector space là cộng vector và nhân scalar.

\[
\mathbf{a}+\mathbf{b}
\]

có thể được hiểu là combine displacement hoặc combine signal component-wise.

\[
c\mathbf{x}
\]

scale magnitude của vector.

Trong neural network, residual connection:

\[
\mathbf{y}=F(\mathbf{x})+\mathbf{x}
\]

sử dụng vector addition để giữ một direct information path. Đây là example cho thấy một operation rất cơ bản của Linear Algebra trở thành architectural primitive trong Deep Learning.

## Dot product: từ phép nhân tới alignment

Với hai vector:

\[
\mathbf{a},\mathbf{b}\in\mathbb{R}^d
\]

dot product là:

\[
\mathbf{a}^T\mathbf{b}=\sum_{i=1}^{d}a_i b_i
\]

Công thức này có hai interpretation quan trọng.

Thứ nhất, nó là weighted sum. Nếu `w` là weight và `x` là feature vector:

\[
z=\mathbf{w}^T\mathbf{x}
\]

mỗi feature được nhân với weight tương ứng rồi cộng lại. Linear regression, logistic regression và neural-network neuron đều xây từ idea này.

Thứ hai, dot product liên hệ với angle:

\[
\mathbf{a}^T\mathbf{b}=\|\mathbf{a}\|\|\mathbf{b}\|\cos\theta
\]

Khi hai vector cùng hướng, dot product lớn dương. Khi gần vuông góc, dot product gần 0. Khi ngược hướng, nó âm.

Transformer attention sử dụng dot product giữa Query và Key để tạo score. Dense retrieval cũng thường dùng dot product để ranking embeddings.

## Norm: vector lớn đến mức nào?

Một **norm (노름 / chuẩn)** đo magnitude.

L2 norm:

\[
\|\mathbf{x}\|_2=\sqrt{\sum_i x_i^2}
\]

L1 norm:

\[
\|\mathbf{x}\|_1=\sum_i |x_i|
\]

Norm không chỉ dùng để đo distance. Regularization thường penalty parameter magnitude:

\[
J(\theta)=L(\theta)+\lambda\|\theta\|_2^2
\]

L2 regularization discourages extremely large weights. L1 regularization có xu hướng tạo nhiều coefficient bằng hoặc gần 0, liên quan tới sparsity.

## Distance và similarity không giống nhau

Euclidean distance:

\[
d(\mathbf{a},\mathbf{b})=\|\mathbf{a}-\mathbf{b}\|_2
\]

đo khoảng cách tuyệt đối.

Cosine similarity:

\[
\cos(\theta)=\frac{\mathbf{a}^T\mathbf{b}}{\|\mathbf{a}\|\|\mathbf{b}\|}
\]

bỏ qua scale và tập trung vào direction.

Ví dụ hai embeddings cùng direction nhưng một vector dài gấp đôi sẽ có cosine similarity bằng 1, dù Euclidean distance khác 0.

Trong vector search, chọn metric phải phù hợp với cách embedding model được trained. Không nên mặc định cosine luôn tốt hơn dot product hoặc Euclidean distance.

## Matrix là linear transformation

Matrix multiplication dễ bị hiểu như thao tác bảng số. Mental model hữu ích hơn là:

\[
W:\mathbb{R}^{n}\rightarrow\mathbb{R}^{m}
\]

với:

\[
\mathbf{y}=W\mathbf{x}
\]

Matrix `W` biến representation `n` chiều thành representation `m` chiều.

Nếu:

\[
W\in\mathbb{R}^{m\times n},\quad \mathbf{x}\in\mathbb{R}^{n}
\]

thì:

\[
\mathbf{y}\in\mathbb{R}^{m}
\]

Shape reasoning rất quan trọng trong Deep Learning. Nếu dimension không match, multiplication không defined.

### Matrix multiplication là composition

Nếu:

\[
\mathbf{h}=W_1\mathbf{x}
\]

và:

\[
\mathbf{y}=W_2\mathbf{h}
\]

thì:

\[
\mathbf{y}=W_2W_1\mathbf{x}
\]

Nhiều linear transformations liên tiếp collapse thành một linear transformation duy nhất. Đây là lý do neural network cần **nonlinearity**. Nếu bỏ activation functions, stack 100 linear layers về mặt expressiveness vẫn chỉ tương đương một linear layer.

## Affine transformation và bias

Trong ML ta thường có:

\[
\mathbf{y}=W\mathbf{x}+\mathbf{b}
\]

Đây là **affine transformation**, không hoàn toàn linear theo strict mathematical definition vì có bias term.

Bias cho phép output shift khỏi origin. Không có bias, input zero luôn map về zero với pure linear map.

Một fully connected neural-network layer về cơ bản là affine transform theo sau bởi activation:

\[
\mathbf{h}=\phi(W\mathbf{x}+\mathbf{b})
\]

## Batch computation

Nếu có `B` samples và mỗi sample có `d` features, ta gom thành matrix:

\[
X\in\mathbb{R}^{B\times d}
\]

Với weight:

\[
W\in\mathbb{R}^{d\times h}
\]

cả batch được transform cùng lúc:

\[
H=XW
\]

thay vì loop qua từng sample.

Đây là connection trực tiếp giữa Linear Algebra và GPU computing: modern accelerators cực kỳ tối ưu cho large matrix multiplication.

## Transpose

Transpose đổi rows thành columns:

\[
A^T_{ij}=A_{ji}
\]

Trong attention, nếu:

\[
Q,K\in\mathbb{R}^{n\times d_k}
\]

thì:

\[
QK^T\in\mathbb{R}^{n\times n}
\]

Matrix kết quả chứa pairwise dot-product score giữa mỗi query token và mỗi key token.

Shape reasoning:

```text
Q       : n × d_k
K^T     : d_k × n
QK^T    : n × n
```

Chỉ cần nhìn shape đã thấy attention đang tạo relationship giữa mọi pair token trong sequence.

## Basis và coordinate system

Một vector được biểu diễn bằng coordinates relative to một basis. Trong 2D standard basis:

\[
\mathbf{e}_1=(1,0),\quad \mathbf{e}_2=(0,1)
\]

và:

\[
\mathbf{x}=x_1\mathbf{e}_1+x_2\mathbf{e}_2
\]

Trong Machine Learning, feature dimensions hoặc latent dimensions cũng có thể được xem như coordinate axes, nhưng axis của learned latent space thường không có semantic label đơn giản như “tuổi” hay “thu nhập”. Meaning có thể được distributed trên nhiều dimensions.

Điều này giải thích vì sao interpret một neuron hoặc một embedding dimension riêng lẻ thường khó.

## Linear independence, rank và redundant information

Một set vectors **linearly independent** nếu không vector nào có thể được tạo từ combination tuyến tính của các vector còn lại.

**Rank (계수 / rank)** của matrix phản ánh số direction độc lập mà matrix giữ lại hoặc tạo ra.

Nếu matrix projection có rank thấp, information bị compress vào subspace nhỏ hơn.

Low-rank structure xuất hiện trong AI ở nhiều nơi:

- PCA tìm principal subspace;
- low-rank approximation nén matrix;
- LoRA fine-tuning biểu diễn parameter update bằng product của hai low-rank matrices;
- matrix factorization được dùng trong recommender systems.

LoRA dùng idea:

\[
\Delta W=BA
\]

với rank `r` nhỏ hơn nhiều dimension gốc. Thay vì train toàn bộ `W`, ta train hai matrices nhỏ `A` và `B`, giảm số parameter cần update.

## Eigenvectors và eigenvalues

Với square matrix `A`, nếu:

\[
A\mathbf{v}=\lambda\mathbf{v}
\]

thì `v` là eigenvector và `λ` là eigenvalue.

Interpretation: `v` là direction đặc biệt mà transformation `A` không đổi hướng, chỉ scale bởi `λ`.

Eigen decomposition quan trọng trong spectral methods, Markov chains, graph analysis và PCA-related intuition.

Không phải mọi matrix đều có decomposition đơn giản trên real numbers, nên trong practical ML ta thường dùng Singular Value Decomposition tổng quát hơn.

## Singular Value Decomposition

Mọi real matrix `A` có thể được factorize:

\[
A=U\Sigma V^T
\]

Trong đó `U` và `V` chứa orthonormal directions, còn diagonal entries của `Σ` là singular values.

Mental model:

```text
input coordinates
    ↓ V^T
rotate/change basis
    ↓ Σ
scale important directions
    ↓ U
rotate into output space
```

Nếu chỉ giữ top `k` singular values, ta có low-rank approximation:

\[
A\approx U_k\Sigma_kV_k^T
\]

Điều này giúp compression, denoising và dimensionality reduction.

## PCA: tìm directions giải thích variance

Principal Component Analysis (PCA / 주성분 분석) tìm các orthogonal directions có variance lớn nhất trong centered data.

Nếu covariance matrix là:

\[
C=\frac{1}{n}X^TX
\]

thì principal components liên hệ với eigenvectors của `C` hoặc right singular vectors của `X`.

PCA không “tìm feature quan trọng theo mọi nghĩa”. Nó tối ưu variance reconstruction dưới linear assumptions. Direction có variance lớn chưa chắc là direction tốt nhất cho classification.

## Projection

Projection một vector `x` lên unit vector `u`:

\[
proj_{\mathbf{u}}(\mathbf{x})=(\mathbf{x}^T\mathbf{u})\mathbf{u}
\]

Projection giúp hiểu dimensionality reduction, least squares và attention-like weighted combination.

Trong least squares, ta có thể nhìn prediction như projection của target vector lên column space của design matrix.

## Least squares và normal equation

Linear regression muốn minimize:

\[
\|X\mathbf{w}-\mathbf{y}\|_2^2
\]

Nếu assumptions cho phép và matrix invertible phù hợp, solution có dạng:

\[
\mathbf{w}=(X^TX)^{-1}X^T\mathbf{y}
\]

Trong practice không nên trực tiếp tính matrix inverse nếu có numerical method tốt hơn như QR decomposition hoặc SVD. Đây là điểm nối sang [Numerical Computation](./07_numerical_computation.md).

## Embeddings: vectors có nghĩa như thế nào?

Embedding (임베딩) biến discrete object như token, product, user hoặc document thành dense vector.

Giả sử vocabulary có `V` tokens và embedding dimension là `d`, embedding table có shape:

\[
E\in\mathbb{R}^{V\times d}
\]

Token ID chọn một row của `E`.

Trong LLM, embedding ban đầu không phải final meaning. Qua các Transformer layers, hidden states được contextualize: cùng một token có thể có representation khác tùy context.

Semantic geometry hình thành vì training objective buộc model tổ chức representations theo cách hữu ích để predict hoặc discriminate.

## Attention như một bài toán Linear Algebra

Scaled dot-product attention:

\[
Attention(Q,K,V)=softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V
\]

Nếu input hidden states:

\[
X\in\mathbb{R}^{n\times d_{model}}
\]

thì:

\[
Q=XW_Q,\quad K=XW_K,\quad V=XW_V
\]

Các weight matrices học ba projections khác nhau của cùng hidden state.

`QK^T` tạo matrix `n × n` chứa pairwise compatibility. Softmax normalize từng row thành weights. Nhân với `V` tạo weighted mixture của value vectors.

Linear Algebra cho ta thấy attention không phải “model nhìn vào từ quan trọng” theo nghĩa anthropomorphic. Nó là learned transformations + pairwise dot products + normalized weighted aggregation.

## High-dimensional geometry

Trong dimension cao, trực giác 2D có thể gây sai. Một số phenomena quan trọng:

- số lượng directions tăng rất nhanh;
- data thường sparse trong ambient space;
- nearest neighbors có thể trở nên khó phân biệt nếu representation không tốt;
- norms và pairwise distances có thể concentrate;
- cần rất nhiều data nếu muốn cover space trực tiếp.

Representation Learning cố tìm latent space nơi task-relevant structure trở nên compact hơn.

Đây là connection với **manifold hypothesis**: high-dimensional observations có thể nằm gần một lower-dimensional structured manifold, dù hypothesis này không phải universal theorem cho mọi dataset.

## Broadcasting và shape semantics

Framework Deep Learning cho phép **broadcasting**: một tensor nhỏ được conceptually mở rộng để operation với tensor lớn.

Ví dụ bias:

```text
H: B × d
b: d
H + b
```

`b` được cộng vào mỗi row.

Broadcasting rất tiện nhưng cũng dễ tạo silent bug nếu dimension accidentally align. Vì vậy khi debug model, luôn kiểm tra shape và meaning của từng axis, không chỉ kiểm tra code chạy được.

## Mental Model

Có thể nén chapter này thành:

```text
Vector  = representation / point / direction
Matrix  = transformation giữa representations
Dot product = alignment hoặc weighted combination
Norm    = magnitude
Distance/similarity = geometry của representation space
Rank    = số direction độc lập
SVD/PCA = tìm structure và low-dimensional approximation
Tensor  = cách đóng gói nhiều dimensions để computation chạy hàng loạt
```

## Common Misconceptions

### “Embedding dimension nào cũng mang một meaning riêng”

Không nhất thiết. Learned representations thường distributed: một concept có thể được encode qua combination của nhiều dimensions.

### “Cosine similarity cao nghĩa là hai item chắc chắn cùng nghĩa”

Không. Similarity chỉ meaningful relative to embedding model, training objective và domain. Out-of-domain data có thể làm geometry kém đáng tin.

### “Matrix multiplication chỉ là công thức tính toán”

Cách hiểu sâu hơn là composition của transformations giữa vector spaces. Đây là mental model quan trọng để hiểu neural networks và attention.

### “Dimension càng nhiều càng tốt”

Dimension lớn tăng representational capacity nhưng tăng memory, compute và có thể làm learning khó hơn. Effective representation quan trọng hơn ambient dimension đơn thuần.

## Knowledge Connection

Linear Algebra nối trực tiếp tới Neural Networks, Computer Vision, NLP, Recommendation, Graph Learning và LLM. Khi học một architecture mới, hãy hỏi bốn câu:

1. tensor đang biểu diễn gì;
2. shape của từng axis là gì;
3. matrix nào đang transform space nào sang space nào;
4. metric hoặc dot product đang encode relationship gì.

Xem tiếp: [Probability for AI](./02_probability_for_ai.md), [Calculus for AI](./04_calculus_for_ai.md), và sau này `Transformer` trong `06_deep_learning_architectures/`.