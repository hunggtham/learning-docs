# Least squares, SVD và matrix decompositions: projection, approximation và structure

Trong nhiều bài toán thực tế, equation

```math
Ax=b
```

không có exact solution. Không phải vì algebra thất bại, mà vì model và data thường chứa noise, measurement error hoặc nhiều constraints hơn unknowns. Khi `b` nằm ngoài column space của `A`, câu hỏi đúng không còn là “giải chính xác”, mà là:

> Trong tất cả outputs mà `A` có thể tạo ra, output nào gần `b` nhất?

Câu hỏi đó dẫn tới least squares (phương pháp bình phương tối thiểu / 최소제곱법), projection geometry và cuối cùng là QR, SVD, PCA, low-rank approximation và inverse problems.

## Từ exact solving đến best approximation

Ta muốn chọn `x` minimize residual

```math
r=b-Ax.
```

Nếu dùng Euclidean norm, objective là

```math
\min_x \|Ax-b\|_2^2.
```

Square không chỉ để “tránh dấu âm”. Nó tạo objective smooth, liên hệ trực tiếp với Euclidean geometry và Gaussian-noise likelihood.

`Ax` luôn nằm trong column space của `A`. Do đó least squares đang tìm point trong column space gần `b` nhất.

## Vì sao residual phải orthogonal?

Gọi `\hat x` là optimum và

```math
\hat b=A\hat x.
```

Nếu residual

```math
r=b-\hat b
```

còn có component dọc theo column space, ta có thể move `\hat b` một chút theo direction đó và đến gần `b` hơn. Vì vậy tại nearest point, residual phải perpendicular với mọi column của `A`:

```math
A^Tr=0.
```

Thay `r=b-A\hat x`:

```math
A^T(b-A\hat x)=0,
```

suy ra normal equations:

```math
A^TA\hat x=A^Tb.
```

Đây là proof idea từ projection, không phải một formula xuất hiện ngẫu nhiên.

## Worked example — fit một đường thẳng

Giả sử data:

```text
x: 0, 1, 2
y: 1, 2, 2
```

Ta muốn fit

```math
y\approx \beta_0+\beta_1x.
```

Design matrix:

```math
X=
\begin{bmatrix}
1&0\\
1&1\\
1&2
\end{bmatrix},
\qquad
y=
\begin{bmatrix}
1\\2\\2
\end{bmatrix}.
```

Không có line nào đi qua cả ba points chính xác, nên solve `X\beta=y` impossible. Least squares tìm projection của `y` lên column space của `X`.

Normal equations:

```math
X^TX\beta=X^Ty.
```

Ta có

```math
X^TX=
\begin{bmatrix}
3&3\\
3&5
\end{bmatrix},
\qquad
X^Ty=
\begin{bmatrix}
5\\6
\end{bmatrix}.
```

Giải ra

```math
\beta_0=\frac76,\qquad \beta_1=\frac12.
```

Line fit là

```math
\hat y=\frac76+\frac12x.
```

Điểm quan trọng là geometry: predicted vector `X\hat\beta` là closest vector trong model subspace.

## Least squares không đồng nghĩa “model đúng”

Optimization chỉ trả lời: trong model family đã chọn, parameter nào minimize squared error? Nó không chứng minh relation thật sự linear, không chứng minh causality và không bảo vệ khỏi outliers.

Nếu residual structure có pattern, model có thể misspecify. Nếu variance thay đổi theo input, ordinary least squares assumptions về uncertainty cần xem lại. Nếu features gần collinear, coefficients có thể unstable dù predictions vẫn tương đối ổn.

## Vì sao normal equations không phải default numerical method?

Normal equations rất đẹp về theory nhưng có weakness numerical:

```math
\kappa(A^TA)\approx \kappa(A)^2,
```

trong common 2-norm setting.

Nghĩa là conditioning có thể tệ lên đáng kể. Do đó production numerical code thường solve least squares bằng QR hoặc SVD thay vì explicitly forming `A^TA`.

Đây là ví dụ quan trọng của distinction:

```text
mathematically equivalent ≠ numerically equally reliable.
```

## QR decomposition: xây orthogonal coordinates cho column space

Nếu

```math
A=QR,
```

với columns của `Q` orthonormal và `R` upper triangular, thì

```math
\|Ax-b\|_2
=
\|QRx-b\|_2.
```

Orthogonality của `Q` giúp tách problem thành projection plus triangular solve. QR tránh việc squaring condition number như normal equations và thường là workhorse cho dense least squares.

Householder reflections là implementation phổ biến vì stable hơn classical Gram–Schmidt trong finite precision.

## SVD: mọi linear map như rotate → scale → rotate

Singular Value Decomposition viết

```math
A=U\Sigma V^T.
```

Interpretation:

1. `V^T` đổi input sang orthonormal directions đặc biệt;
2. `\Sigma` scale mỗi direction bằng singular value;
3. `U` đổi sang orthonormal output directions.

SVD tồn tại cho mọi real matrix, kể cả rectangular và matrices không diagonalizable.

Nếu singular values là

```math
\sigma_1\ge\sigma_2\ge\cdots\ge0,
```

thì chúng cho biết transformation mạnh yếu thế nào theo các orthogonal directions.

## Rank, near-rank và numerical rank

Exact algebra nói rank là số nonzero singular values. Nhưng measured data hiếm khi có exact zeros; noise biến zero thành tiny nonzero values.

Vì vậy numerical rank phụ thuộc tolerance và problem scale. Một singular value rất nhỏ nghĩa direction đó gần bị collapse. Inversion theo direction ấy sẽ divide by số rất nhỏ và amplify noise.

Đây là core intuition của ill-conditioned inverse problems.

## Pseudoinverse: inverse khi inverse thật không tồn tại

Moore–Penrose pseudoinverse dùng SVD:

```math
A^+=V\Sigma^+U^T,
```

trong đó nonzero singular values được reciprocal.

Least-squares solution minimum-norm có thể viết

```math
\hat x=A^+b.
```

Nếu system underdetermined, có infinitely many exact solutions; pseudoinverse chọn solution có smallest Euclidean norm. Nếu system inconsistent, nó cho least-squares fit.

Nhưng tiny singular values gây amplification, nên practical inverse problems thường cần regularization thay vì blindly using every reciprocal.

## Regularization: chấp nhận bias để giảm variance

Ridge regression solve

```math
\min_x \|Ax-b\|_2^2+\lambda\|x\|_2^2.
```

Normal equations trở thành

```math
(A^TA+\lambda I)x=A^Tb.
```

Term `\lambda I` làm weak directions bớt nguy hiểm. Ta cố ý bias solution toward smaller norm để giảm sensitivity to noise.

Trong SVD coordinates, ridge không invert tiny singular values một cách hung hăng; nó damp chúng. Đây là cách nhìn geometric/numerical rõ hơn việc chỉ gọi regularization là “chống overfitting”.

## Low-rank approximation

Giữ top `k` singular values:

```math
A_k=U_k\Sigma_kV_k^T.
```

Eckart–Young theorem nói đây là best rank-`k` approximation theo Frobenius norm và spectral norm.

Meaning: nếu matrix thật sự có dominant low-dimensional structure, ta có thể bỏ weak directions với minimum possible reconstruction error trong class rank-`k`.

## PCA relation

Với centered data matrix `X`, PCA directions là eigenvectors của covariance matrix, nhưng compute trực tiếp qua SVD thường tốt hơn:

```math
X=U\Sigma V^T.
```

Columns của `V` là principal directions trong feature space; squared singular values liên hệ với explained variance.

PCA vì vậy là một change-of-basis problem: tìm orthogonal axes theo thứ tự variance decreasing.

## Compression và recommender systems

Image matrix thường có correlated structure, nên rank thấp có thể approximate tốt. Recommender systems cũng assume user-item interactions có latent factors nhỏ hơn observed dimension rất nhiều.

Nhưng low-rank assumption là model assumption. Nếu data không có low-rank structure, compression hoặc latent-factor interpretation sẽ kém.

## Finance connection — factor models

Return matrix có thể được approximate bằng vài common factors:

```math
R\approx FB^T.
```

Đây là low-rank idea. PCA có thể tìm statistical factors, nhưng statistical principal directions không tự động có economic meaning. Một direction maximize variance chưa chắc là factor có interpretation causal.

## AI connection — embeddings và low-rank parameterization

Large matrices trong neural networks có thể được approximated hoặc adapted bằng low-rank factors. LoRA-style ideas khai thác giả định rằng useful update nằm trong subspace dimension nhỏ hơn full parameter space.

SVD cũng giúp hiểu why low-rank representations compress information, nhưng trained low-rank adapters không đơn giản là “SVD của model”. Structure và optimization path khác nhau.

## Matrix decompositions là strategy chung

LU, QR, Cholesky, eigendecomposition và SVD không phải các tricks rời rạc. Ý tưởng chung là factor một operator khó thành product của operators có structure dễ xử lý.

- LU: triangular systems, useful cho repeated solves;
- Cholesky: symmetric positive-definite matrices, nhanh và efficient;
- QR: orthogonalization và least squares;
- eigendecomposition: natural invariant directions khi possible;
- SVD: universal orthogonal input/output directions.

Chọn decomposition phụ thuộc matrix structure và task, không có một decomposition “tốt nhất” cho mọi problem.

## Failure modes và assumptions

Squared loss nhạy với outliers vì residual lớn bị square. Robust regression có thể dùng L1/Huber losses.

SVD trên raw features bị ảnh hưởng mạnh bởi scale. Nếu một feature đo bằng thousands và feature khác bằng units, variance geometry có thể chủ yếu phản ánh units. Standardization cần dựa trên domain meaning, không áp dụng máy móc.

Low-rank truncation có thể xóa weak nhưng meaningful signal. “Small singular value” chỉ nói weak linear direction relative to chosen scaling, không nói business importance bằng zero.

## Mental Model

> Least squares là projection: khi target nằm ngoài reachable subspace, chọn reachable point gần nhất. QR xây coordinates ổn định cho subspace đó. SVD bóc một linear map thành orthogonal input directions, independent scaling strengths và orthogonal output directions. Tiny singular values là directions gần mất thông tin; regularization quyết định không cố phục hồi chúng quá mức.

## Common Misconceptions

**“Least squares fit tốt nghĩa model đúng.”** Không. Nó chỉ tối ưu trong model family và loss đã chọn.

**“Normal equations là cách chuẩn nhất để code regression.”** Chúng tốt để derive theory nhưng QR/SVD thường preferable numerically.

**“SVD chỉ dùng cho square matrices.”** Sai. SVD tồn tại cho rectangular matrices và chính đó là một ưu điểm lớn.

**“PCA tìm các features quan trọng nhất.”** PCA tìm directions có variance lớn nhất, không trực tiếp tìm causal hoặc predictive importance.

**“Tiny singular values nên luôn xóa.”** Không. Threshold là modeling/numerical decision dựa trên noise, scale và purpose.