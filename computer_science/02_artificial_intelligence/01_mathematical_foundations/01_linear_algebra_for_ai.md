# Tuyến tính (linear / 선형) Algebra cho Artificial Intelligence

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Linear algebra cho AI**. Route đi từ scalar/vector/matrix/tensor → vector spaces/inner products → linear maps/eigenstructure → matrix factorization → representation and batch computation, để hình học nối với phép tính model.

Tuyến tính (linear / 선형) Algebra (선형대수 / đại số tuyến tính) là ngôn ngữ dùng để biểu diễn nhiều đại lượng cùng lúc và mô tả cách chúng được biến đổi. Trong AI hiện đại, một mẫu (sample / 표본) hiếm khi chỉ là một số. Một ảnh có hàng trăm nghìn điểm ảnh (pixel / 픽셀), một câu trở thành hàng chục hoặc hàng nghìn đơn vị từ (token / 토큰), một embedding có hàng trăm đến hàng nghìn dimension, còn một neural mạng (network / 네트워크) có thể xử lý hàng nghìn mẫu (sample / 표본) song song trong một batch. tuyến tính (linear / 선형) Algebra giúp gom các quantity này thành véc-tơ (vector / 벡터), ma trận (matrix / 행렬) và tensor để computation có thể được mô tả rõ ràng và chạy hiệu quả trên hardware.

Điểm quan trọng nhất không phải học thuộc phép nhân ma trận. Ta cần nhìn ma trận (matrix / 행렬) như một **transformation giữa các spaces**, véc-tơ (vector / 벡터) như một **biểu diễn (representation / 표현)**, và dot sản phẩm (product / 제품) như một phép đo **alignment**. Khi mô hình tư duy (mental model / 사고 모델) này rõ, nhiều công thức trong Machine học tập (learning / 학습), embeddings và Transformer trở nên tự nhiên hơn.

Xem bản đồ tổng quan: [Mathematics for AI](./00_mathematics_for_ai.md).

## Scalar, véc-tơ (vector / 벡터), ma trận (matrix / 행렬) và tensor

Một **scalar (스칼라)** là một giá trị đơn, ví dụ temperature `23.5`, học tập (learning / 학습) tỷ lệ (rate / 비율) `0.001`, hoặc mất mát (loss / 손실) `2.3`.

Một **véc-tơ (vector / 벡터)** là một ordered danh sách (list / 목록) các số. Nếu khách hàng được biểu diễn bằng tuổi, thu nhập và số lần mua hàng, ta có thể viết:

\[
\mathbf{x}=\begin{bmatrix}31\\4200\\7\end{bmatrix}
\]

Véc-tơ (vector / 벡터) này không phải chính khách hàng. Nó là một biểu diễn (representation / 표현) được chọn để giữ những properties ta cho là relevant với tác vụ (task / 작업).

Một **ma trận (matrix / 행렬)** là bảng số hai chiều. Nếu mỗi row là một mẫu (sample / 표본) và mỗi column là một tính năng (feature / 기능):

\[
X=\begin{bmatrix}
31 & 4200 & 7\\
28 & 3500 & 3\\
45 & 6700 & 12
\end{bmatrix}
\]

thì `X` có shape `3 × 3`.

Một **tensor (텐서)** trong Deep học tập (learning / 학습) thường được dùng theo nghĩa practical là array nhiều chiều. Ví dụ batch ảnh RGB có shape:

```text
batch × height × width × channels
32 × 224 × 224 × 3
```

Trong PyTorch convention thường gặp `N × C × H × W`, trong khi một số khung phần mềm (framework / 프레임워크) hoặc format khác dùng `N × H × W × C`. Shape không phải chi tiết nhỏ; rất nhiều bug ML đơn giản là tensor có đúng values nhưng sai axis.

> **Chuyển mạch:** Trong **Tuyến tính (linear / 선형) Algebra cho Artificial Intelligence**, **Véc-tơ (vector / 벡터) không gian (space / 공간): biểu diễn (representation / 표현) sống ở đâu?** tiếp nhận điểm tựa từ **Scalar, véc-tơ (vector / 벡터), ma trận (matrix / 행렬) và tensor** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Addition và scalar multiplication** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Véc-tơ (vector / 벡터) không gian (space / 공간): biểu diễn (representation / 표현) sống ở đâu?

Một véc-tơ (vector / 벡터) không chỉ là danh sách (list / 목록) numbers. Khi ta nói:

\[
\mathbf{x}\in\mathbb{R}^d
\]

ta nói `x` là một điểm (point / 지점) trong véc-tơ (vector / 벡터) không gian (space / 공간) `d` chiều.

Nếu embedding mô hình (model / 모델) map một sentence thành véc-tơ (vector / 벡터) 768 chiều, sentence đó được biến thành một điểm (point / 지점) trong `R^768`. Nhưng hình học (geometry / 기하학) trong không gian (space / 공간) này chỉ có ý nghĩa vì huấn luyện (training / 학습) mục tiêu (objective / 목표) đã tạo cấu trúc (structure / 구조). Không có huấn luyện (training / 학습) phù hợp, hai câu cùng nghĩa không tự nhiên trở thành hai véc-tơ (vector / 벡터) gần nhau.

Đây là nguyên lý quan trọng:

> hình học (geometry / 기하학) của embedding không gian (space / 공간) không phải meaning “có sẵn”; nó là cấu trúc (structure / 구조) được học từ mục tiêu (objective / 목표) và dữ liệu (data / 데이터).

> **Chuyển mạch:** Ở chặng này của **Tuyến tính (linear / 선형) Algebra cho Artificial Intelligence**, **Addition và scalar multiplication** tiếp nhận điểm tựa từ **Véc-tơ (vector / 벡터) không gian (space / 공간): biểu diễn (representation / 표현) sống ở đâu?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dot sản phẩm (product / 제품): từ phép nhân tới alignment** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Addition và scalar multiplication

Hai operations cơ bản của véc-tơ (vector / 벡터) không gian (space / 공간) là cộng véc-tơ (vector / 벡터) và nhân scalar.

\[
\mathbf{a}+\mathbf{b}
\]

có thể được hiểu là combine displacement hoặc combine tín hiệu (signal / 신호) component-wise.

\[
c\mathbf{x}
\]

Quy mô (scale / 규모) magnitude của véc-tơ (vector / 벡터).

Trong neural mạng (network / 네트워크), residual liên kết (connection / 연결):

\[
\mathbf{y}=F(\mathbf{x})+\mathbf{x}
\]

sử dụng véc-tơ (vector / 벡터) addition để giữ một direct thông tin (information / 정보) đường dẫn (path / 경로). Đây là example cho thấy một thao tác (operation / 연산) rất cơ bản của tuyến tính (linear / 선형) Algebra trở thành architectural thành phần nguyên thủy (primitive / 기본 요소) trong Deep học tập (learning / 학습).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tuyến tính (linear / 선형) Algebra cho Artificial Intelligence**, **Dot sản phẩm (product / 제품): từ phép nhân tới alignment** tiếp nhận điểm tựa từ **Addition và scalar multiplication** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Norm: véc-tơ (vector / 벡터) lớn đến mức nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dot sản phẩm (product / 제품): từ phép nhân tới alignment

Với hai véc-tơ (vector / 벡터):

\[
\mathbf{a},\mathbf{b}\in\mathbb{R}^d
\]

dot sản phẩm (product / 제품) là:

\[
\mathbf{a}^T\mathbf{b}=\sum_{i=1}^{d}a_i b_i
\]

Công thức này có hai interpretation quan trọng.

Thứ nhất, nó là weighted sum. Nếu `w` là weight và `x` là tính năng (feature / 기능) véc-tơ (vector / 벡터):

\[
z=\mathbf{w}^T\mathbf{x}
\]

mỗi tính năng (feature / 기능) được nhân với weight tương ứng rồi cộng lại. tuyến tính (linear / 선형) regression, logistic regression và neural-network neuron đều xây từ idea này.

Thứ hai, dot sản phẩm (product / 제품) liên hệ với angle:

\[
\mathbf{a}^T\mathbf{b}=\|\mathbf{a}\|\|\mathbf{b}\|\cos\theta
\]

Khi hai véc-tơ (vector / 벡터) cùng hướng, dot sản phẩm (product / 제품) lớn dương. Khi gần vuông góc, dot sản phẩm (product / 제품) gần 0. Khi ngược hướng, nó âm.

Transformer attention sử dụng dot sản phẩm (product / 제품) giữa truy vấn (query / 쿼리) và Key để tạo score. Dense retrieval cũng thường dùng dot sản phẩm (product / 제품) để ranking embeddings.

> **Chuyển mạch:** Trong **Tuyến tính (linear / 선형) Algebra cho Artificial Intelligence**, **Norm: véc-tơ (vector / 벡터) lớn đến mức nào?** tiếp nhận điểm tựa từ **Dot sản phẩm (product / 제품): từ phép nhân tới alignment** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Distance và similarity không giống nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Norm: véc-tơ (vector / 벡터) lớn đến mức nào?

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

> **Chuyển mạch:** Ở chặng này của **Tuyến tính (linear / 선형) Algebra cho Artificial Intelligence**, **Distance và similarity không giống nhau** tiếp nhận điểm tựa từ **Norm: véc-tơ (vector / 벡터) lớn đến mức nào?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ma trận (matrix / 행렬) là tuyến tính (linear / 선형) transformation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

bỏ qua quy mô (scale / 규모) và tập trung vào direction.

Ví dụ hai embeddings cùng direction nhưng một véc-tơ (vector / 벡터) dài gấp đôi sẽ có cosine similarity bằng 1, dù Euclidean distance khác 0.

Trong véc-tơ (vector / 벡터) tìm kiếm (search / 검색), chọn chỉ số (metric / 지표) phải phù hợp với cách embedding mô hình (model / 모델) được trained. Không nên mặc định cosine luôn tốt hơn dot sản phẩm (product / 제품) hoặc Euclidean distance.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tuyến tính (linear / 선형) Algebra cho Artificial Intelligence**, **Ma trận (matrix / 행렬) là tuyến tính (linear / 선형) transformation** tiếp nhận điểm tựa từ **Distance và similarity không giống nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Affine transformation và độ lệch (bias / 편향)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ma trận (matrix / 행렬) là tuyến tính (linear / 선형) transformation

Phép nhân ma trận (matrix multiplication / 행렬 곱셈) dễ bị hiểu như thao tác bảng số. mô hình tư duy (mental model / 사고 모델) hữu ích hơn là:

\[
W:\mathbb{R}^{n}\rightarrow\mathbb{R}^{m}
\]

với:

\[
\mathbf{y}=W\mathbf{x}
\]

Ma trận (matrix / 행렬) `W` biến biểu diễn (representation / 표현) `n` chiều thành biểu diễn (representation / 표현) `m` chiều.

Nếu:

\[
W\in\mathbb{R}^{m\times n},\quad \mathbf{x}\in\mathbb{R}^{n}
\]

thì:

\[
\mathbf{y}\in\mathbb{R}^{m}
\]

Shape lập luận (reasoning / 추론) rất quan trọng trong Deep học tập (learning / 학습). Nếu dimension không match, multiplication không defined.

### Phép nhân ma trận (matrix multiplication / 행렬 곱셈) là composition

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

Nhiều tuyến tính (linear / 선형) transformations liên tiếp collapse thành một tuyến tính (linear / 선형) transformation duy nhất. Đây là lý do neural mạng (network / 네트워크) cần **nonlinearity**. Nếu bỏ activation functions, ngăn xếp (stack / 스택) 100 tuyến tính (linear / 선형) layers về mặt expressiveness vẫn chỉ tương đương một tuyến tính (linear / 선형) tầng (layer / 계층).

> **Chuyển mạch:** Trong **Tuyến tính (linear / 선형) Algebra cho Artificial Intelligence**, **Affine transformation và độ lệch (bias / 편향)** tiếp nhận điểm tựa từ **Ma trận (matrix / 행렬) là tuyến tính (linear / 선형) transformation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Batch computation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Affine transformation và độ lệch (bias / 편향)

Trong ML ta thường có:

\[
\mathbf{y}=W\mathbf{x}+\mathbf{b}
\]

Đây là **affine transformation**, không hoàn toàn tuyến tính (linear / 선형) theo strict mathematical definition vì có độ lệch (bias / 편향) term.

Độ lệch (bias / 편향) cho phép đầu ra (output / 출력) shift khỏi origin. Không có độ lệch (bias / 편향), đầu vào (input / 입력) zero luôn map về zero với pure tuyến tính (linear / 선형) map.

Một fully connected neural-network tầng (layer / 계층) về cơ bản là affine transform theo sau bởi activation:

\[
\mathbf{h}=\phi(W\mathbf{x}+\mathbf{b})
\]

> **Chuyển mạch:** Ở chặng này của **Tuyến tính (linear / 선형) Algebra cho Artificial Intelligence**, **Batch computation** tiếp nhận điểm tựa từ **Affine transformation và độ lệch (bias / 편향)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Transpose** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Batch computation

Nếu có `B` samples và mỗi mẫu (sample / 표본) có `d` features, ta gom thành ma trận (matrix / 행렬):

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

thay vì vòng lặp (loop / 루프) qua từng mẫu (sample / 표본).

Đây là liên kết (connection / 연결) trực tiếp giữa tuyến tính (linear / 선형) Algebra và GPU computing: hiện đại (modern / 현대적) accelerators cực kỳ tối ưu cho large phép nhân ma trận (matrix multiplication / 행렬 곱셈).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tuyến tính (linear / 선형) Algebra cho Artificial Intelligence**, **Transpose** tiếp nhận điểm tựa từ **Batch computation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Basis và coordinate hệ thống (system / 시스템)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Ma trận (matrix / 행렬) kết quả chứa pairwise dot-product score giữa mỗi truy vấn (query / 쿼리) đơn vị từ (token / 토큰) và mỗi key đơn vị từ (token / 토큰).

Shape lập luận (reasoning / 추론):

```text
Q       : n × d_k
K^T     : d_k × n
QK^T    : n × n
```

Chỉ cần nhìn shape đã thấy attention đang tạo relationship giữa mọi pair đơn vị từ (token / 토큰) trong chuỗi (sequence / 시퀀스).

> **Chuyển mạch:** Trong **Tuyến tính (linear / 선형) Algebra cho Artificial Intelligence**, **Basis và coordinate hệ thống (system / 시스템)** tiếp nhận điểm tựa từ **Transpose** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tuyến tính (linear / 선형) independence, rank và redundant thông tin (information / 정보)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Basis và coordinate hệ thống (system / 시스템)

Một véc-tơ (vector / 벡터) được biểu diễn bằng coordinates relative to một basis. Trong 2D tiêu chuẩn (standard / 표준) basis:

\[
\mathbf{e}_1=(1,0),\quad \mathbf{e}_2=(0,1)
\]

và:

\[
\mathbf{x}=x_1\mathbf{e}_1+x_2\mathbf{e}_2
\]

Trong Machine học tập (learning / 학습), tính năng (feature / 기능) dimensions hoặc latent dimensions cũng có thể được xem như coordinate axes, nhưng axis của learned latent không gian (space / 공간) thường không có ngữ nghĩa (semantic / 의미적) label đơn giản như “tuổi” hay “thu nhập”. Meaning có thể được phân tán (distributed / 분산) trên nhiều dimensions.

Điều này giải thích vì sao interpret một neuron hoặc một embedding dimension riêng lẻ thường khó.

> **Chuyển mạch:** Ở chặng này của **Tuyến tính (linear / 선형) Algebra cho Artificial Intelligence**, **Tuyến tính (linear / 선형) independence, rank và redundant thông tin (information / 정보)** tiếp nhận điểm tựa từ **Basis và coordinate hệ thống (system / 시스템)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Eigenvectors và eigenvalues** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tuyến tính (linear / 선형) independence, rank và redundant thông tin (information / 정보)

Một set vectors **linearly independent** nếu không véc-tơ (vector / 벡터) nào có thể được tạo từ combination tuyến tính của các véc-tơ (vector / 벡터) còn lại.

**Rank (계수 / rank)** của ma trận (matrix / 행렬) phản ánh số direction độc lập mà ma trận (matrix / 행렬) giữ lại hoặc tạo ra.

Nếu ma trận (matrix / 행렬) projection có rank thấp, thông tin (information / 정보) bị compress vào subspace nhỏ hơn.

Low-rank cấu trúc (structure / 구조) xuất hiện trong AI ở nhiều nơi:

- PCA tìm principal subspace;
- low-rank approximation nén ma trận (matrix / 행렬);
- LoRA fine-tuning biểu diễn parameter cập nhật (update / 업데이트) bằng sản phẩm (product / 제품) của hai low-rank matrices;
- ma trận (matrix / 행렬) factorization được dùng trong recommender các hệ thống (systems / 시스템들).

LoRA dùng idea:

\[
\Delta W=BA
\]

với rank `r` nhỏ hơn nhiều dimension gốc. Thay vì train toàn bộ `W`, ta train hai matrices nhỏ `A` và `B`, giảm số parameter cần cập nhật (update / 업데이트).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tuyến tính (linear / 선형) Algebra cho Artificial Intelligence**, **Eigenvectors và eigenvalues** tiếp nhận điểm tựa từ **Tuyến tính (linear / 선형) independence, rank và redundant thông tin (information / 정보)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Singular giá trị (value / 값) Decomposition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Eigenvectors và eigenvalues

Với square ma trận (matrix / 행렬) `A`, nếu:

\[
A\mathbf{v}=\lambda\mathbf{v}
\]

thì `v` là eigenvector và `λ` là eigenvalue.

Interpretation: `v` là direction đặc biệt mà transformation `A` không đổi hướng, chỉ quy mô (scale / 규모) bởi `λ`.

Eigen decomposition quan trọng trong spectral methods, Markov chains, đồ thị (graph / 그래프) phân tích (analysis / 분석) và PCA-related intuition.

Không phải mọi ma trận (matrix / 행렬) đều có decomposition đơn giản trên real numbers, nên trong practical ML ta thường dùng Singular giá trị (value / 값) Decomposition tổng quát hơn.

> **Chuyển mạch:** Trong **Tuyến tính (linear / 선형) Algebra cho Artificial Intelligence**, **Singular giá trị (value / 값) Decomposition** tiếp nhận điểm tựa từ **Eigenvectors và eigenvalues** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **PCA: tìm directions giải thích variance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Singular giá trị (value / 값) Decomposition

Mọi real ma trận (matrix / 행렬) `A` có thể được factorize:

\[
A=U\Sigma V^T
\]

Trong đó `U` và `V` chứa orthonormal directions, còn diagonal entries của `Σ` là singular values.

Mô hình tư duy (mental model / 사고 모델):

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

> **Chuyển mạch:** Ở chặng này của **Tuyến tính (linear / 선형) Algebra cho Artificial Intelligence**, **PCA: tìm directions giải thích variance** tiếp nhận điểm tựa từ **Singular giá trị (value / 값) Decomposition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Projection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## PCA: tìm directions giải thích variance

Principal thành phần (component / 컴포넌트) phân tích (analysis / 분석) tìm các orthogonal directions có variance lớn nhất trong centered dữ liệu (data / 데이터).

Nếu covariance ma trận (matrix / 행렬) là:

\[
C=\frac{1}{n}X^TX
\]

thì principal components liên hệ với eigenvectors của `C` hoặc right singular vectors của `X`.

PCA không “tìm tính năng (feature / 기능) quan trọng theo mọi nghĩa”. Nó tối ưu variance reconstruction dưới tuyến tính (linear / 선형) các giả định (assumptions / 가정들). Direction có variance lớn chưa chắc là direction tốt nhất cho classification.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tuyến tính (linear / 선형) Algebra cho Artificial Intelligence**, **Projection** tiếp nhận điểm tựa từ **PCA: tìm directions giải thích variance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Least squares và normal equation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Projection

Projection một véc-tơ (vector / 벡터) `x` lên đơn vị (unit / 단위) véc-tơ (vector / 벡터) `u`:

\[
proj_{\mathbf{u}}(\mathbf{x})=(\mathbf{x}^T\mathbf{u})\mathbf{u}
\]

Projection giúp hiểu dimensionality reduction, least squares và attention-like weighted combination.

Trong least squares, ta có thể nhìn prediction như projection của mục tiêu (target / 대상) véc-tơ (vector / 벡터) lên column không gian (space / 공간) của thiết kế (design / 설계) ma trận (matrix / 행렬).

> **Chuyển mạch:** Trong **Tuyến tính (linear / 선형) Algebra cho Artificial Intelligence**, **Least squares và normal equation** tiếp nhận điểm tựa từ **Projection** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Embeddings: vectors có nghĩa như thế nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Least squares và normal equation

Tuyến tính (linear / 선형) regression muốn minimize:

\[
\|X\mathbf{w}-\mathbf{y}\|_2^2
\]

Nếu các giả định (assumptions / 가정들) cho phép và ma trận (matrix / 행렬) invertible phù hợp, solution có dạng:

\[
\mathbf{w}=(X^TX)^{-1}X^T\mathbf{y}
\]

Trong practice không nên trực tiếp tính ma trận (matrix / 행렬) inverse nếu có numerical phương thức (method / 메서드) tốt hơn như QR decomposition hoặc SVD. Đây là điểm nối sang [Numerical Computation](./07_numerical_computation.md).

> **Chuyển mạch:** Ở chặng này của **Tuyến tính (linear / 선형) Algebra cho Artificial Intelligence**, **Embeddings: vectors có nghĩa như thế nào?** tiếp nhận điểm tựa từ **Least squares và normal equation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Attention như một bài toán tuyến tính (linear / 선형) Algebra** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Embeddings: vectors có nghĩa như thế nào?

Embedding (임베딩) biến discrete đối tượng (object / 객체) như đơn vị từ (token / 토큰), sản phẩm (product / 제품), người dùng (user / 사용자) hoặc document thành dense véc-tơ (vector / 벡터).

Giả sử vocabulary có `V` tokens và embedding dimension là `d`, embedding bảng (table / 테이블) có shape:

\[
E\in\mathbb{R}^{V\times d}
\]

Đơn vị từ (token / 토큰) ID chọn một row của `E`.

Trong LLM, embedding ban đầu không phải final meaning. Qua các Transformer layers, hidden states được contextualize: cùng một đơn vị từ (token / 토큰) có thể có biểu diễn (representation / 표현) khác tùy ngữ cảnh (context / 맥락).

Ngữ nghĩa (semantic / 의미적) hình học (geometry / 기하학) hình thành vì huấn luyện (training / 학습) mục tiêu (objective / 목표) buộc mô hình (model / 모델) tổ chức representations theo cách hữu ích để predict hoặc discriminate.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tuyến tính (linear / 선형) Algebra cho Artificial Intelligence**, **Attention như một bài toán tuyến tính (linear / 선형) Algebra** tiếp nhận điểm tựa từ **Embeddings: vectors có nghĩa như thế nào?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **High-dimensional hình học (geometry / 기하학)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Attention như một bài toán tuyến tính (linear / 선형) Algebra

Scaled dot-product attention:

\[
Attention(Q,K,V)=softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V
\]

Nếu đầu vào (input / 입력) hidden states:

\[
X\in\mathbb{R}^{n\times d_{mô hình (model / 모델)}}
\]

thì:

\[
Q=XW_Q,\quad K=XW_K,\quad V=XW_V
\]

Các weight matrices học ba projections khác nhau của cùng hidden trạng thái (state / 상태).

`QK^T` tạo ma trận (matrix / 행렬) `n × n` chứa pairwise tính tương thích (compatibility / 호환성). Softmax normalize từng row thành weights. Nhân với `V` tạo weighted mixture của giá trị (value / 값) vectors.

Tuyến tính (linear / 선형) Algebra cho ta thấy attention không phải “mô hình (model / 모델) nhìn vào từ quan trọng” theo nghĩa anthropomorphic. Nó là learned transformations + pairwise dot products + normalized weighted aggregation.

> **Chuyển mạch:** Trong **Tuyến tính (linear / 선형) Algebra cho Artificial Intelligence**, **High-dimensional hình học (geometry / 기하학)** tiếp nhận điểm tựa từ **Attention như một bài toán tuyến tính (linear / 선형) Algebra** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Broadcasting và shape ngữ nghĩa (semantics / 의미론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## High-dimensional hình học (geometry / 기하학)

Trong dimension cao, trực giác 2D có thể gây sai. Một số phenomena quan trọng:

- số lượng directions tăng rất nhanh;
- dữ liệu (data / 데이터) thường sparse trong ambient không gian (space / 공간);
- nearest neighbors có thể trở nên khó phân biệt nếu biểu diễn (representation / 표현) không tốt;
- norms và pairwise distances có thể concentrate;
- cần rất nhiều dữ liệu (data / 데이터) nếu muốn cover không gian (space / 공간) trực tiếp.

Biểu diễn (representation / 표현) học tập (learning / 학습) cố tìm latent không gian (space / 공간) nơi task-relevant cấu trúc (structure / 구조) trở nên compact hơn.

Đây là liên kết (connection / 연결) với **manifold hypothesis**: high-dimensional observations có thể nằm gần một lower-dimensional structured manifold, dù hypothesis này không phải universal theorem cho mọi dataset.

> **Chuyển mạch:** Ở chặng này của **Tuyến tính (linear / 선형) Algebra cho Artificial Intelligence**, **Broadcasting và shape ngữ nghĩa (semantics / 의미론)** tiếp nhận điểm tựa từ **High-dimensional hình học (geometry / 기하학)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Broadcasting và shape ngữ nghĩa (semantics / 의미론)

Khung phần mềm (framework / 프레임워크) Deep học tập (learning / 학습) cho phép **broadcasting**: một tensor nhỏ được conceptually mở rộng để thao tác (operation / 연산) với tensor lớn.

Ví dụ độ lệch (bias / 편향):

```text
H: B × d
b: d
H + b
```

`b` được cộng vào mỗi row.

Broadcasting rất tiện nhưng cũng dễ tạo silent bug nếu dimension accidentally align. Vì vậy khi gỡ lỗi (debug / 디버그) mô hình (model / 모델), luôn kiểm tra shape và meaning của từng axis, không chỉ kiểm tra mã (code / 코드) chạy được.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tuyến tính (linear / 선형) Algebra cho Artificial Intelligence**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Broadcasting và shape ngữ nghĩa (semantics / 의미론)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

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

> **Chuyển mạch:** Trong **Tuyến tính (linear / 선형) Algebra cho Artificial Intelligence**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Embedding dimension nào cũng mang một meaning riêng”

Không nhất thiết. Learned representations thường phân tán (distributed / 분산): một concept có thể được encode qua combination của nhiều dimensions.

### “Cosine similarity cao nghĩa là hai item chắc chắn cùng nghĩa”

Không. Similarity chỉ meaningful relative to embedding mô hình (model / 모델), huấn luyện (training / 학습) mục tiêu (objective / 목표) và lĩnh vực (domain / 도메인). Out-of-domain dữ liệu (data / 데이터) có thể làm hình học (geometry / 기하학) kém đáng tin.

### “phép nhân ma trận (matrix multiplication / 행렬 곱셈) chỉ là công thức tính toán”

Cách hiểu sâu hơn là composition của transformations giữa véc-tơ (vector / 벡터) spaces. Đây là mô hình tư duy (mental model / 사고 모델) quan trọng để hiểu neural networks và attention.

### “Dimension càng nhiều càng tốt”

Dimension lớn tăng representational sức chứa (capacity / 용량) nhưng tăng bộ nhớ (memory / 메모리), compute và có thể làm học tập (learning / 학습) khó hơn. Effective biểu diễn (representation / 표현) quan trọng hơn ambient dimension đơn thuần.

> **Chuyển mạch:** Ở chặng này của **Tuyến tính (linear / 선형) Algebra cho Artificial Intelligence**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Tuyến tính (linear / 선형) Algebra nối trực tiếp tới Neural Networks, Computer Vision, NLP, Recommendation, đồ thị (graph / 그래프) học tập (learning / 학습) và LLM. Khi học một kiến trúc (architecture / 아키텍처) mới, hãy hỏi bốn câu:

1. tensor đang biểu diễn gì;
2. shape của từng axis là gì;
3. ma trận (matrix / 행렬) nào đang transform không gian (space / 공간) nào sang không gian (space / 공간) nào;
4. chỉ số (metric / 지표) hoặc dot sản phẩm (product / 제품) đang encode relationship gì.

Xem tiếp: [Probability for AI](./02_probability_for_ai.md), [Calculus for AI](./04_calculus_for_ai.md), và sau này `Transformer` trong `06_deep_learning_architectures/`.

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
