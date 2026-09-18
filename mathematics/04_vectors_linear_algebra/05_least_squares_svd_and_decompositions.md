# Least squares, SVD và matrix decompositions

Khi system `Ax=b` không có exact solution, ta cần notion “best approximate solution”. Least squares (최소제곱법) chọn `x` minimize squared residual norm:

```math
\min_x\|Ax-b\|_2^2
```

## Geometry của least squares

`Ax` luôn nằm trong column space của `A`. Nếu `b` không nằm trong column space, ta tìm point `Ax` gần `b` nhất. Residual

```math
r=b-Ax
```

ở optimum orthogonal với column space:

```math
A^Tr=0
```

nên

```math
A^T(b-Ax)=0
```

và normal equations:

```math
A^TAx=A^Tb.
```

Đây là projection geometry, không chỉ formula regression.

## Linear regression

Design matrix `X`, parameters `β`, target `y`:

```math
y\approx X\beta
```

least squares solve:

```math
\min_\beta\|X\beta-y\|^2
```

Prediction là projection của `y` lên column space của `X`.

## Vì sao không luôn dùng normal equations?

`X^TX` có thể condition number squared relative to `X`, làm numerical issues tệ hơn. QR hoặc SVD thường ổn định hơn.

Toán lý thuyết và implementation numerical cần phân biệt.

## SVD

Singular Value Decomposition:

```math
A=U\Sigma V^T
```

với `U,V` orthogonal (hoặc unitary complex case), `Σ` diagonal-like chứa nonnegative singular values.

Interpretation:

1. `V^T` đổi coordinates vào input directions đặc biệt;
2. `Σ` scale từng direction;
3. `U` rotate sang output directions.

Mọi matrix có SVD, kể cả rectangular/non-diagonalizable.

## Rank từ singular values

Exact rank là number of nonzero singular values. Trong numerical data, tiny singular values chỉ directions rất yếu và có thể bị noise dominate.

Low-rank approximation giữ top `k` singular values:

```math
A_k=U_k\Sigma_kV_k^T
```

và là best rank-k approximation theo common norms như Frobenius/2-norm (Eckart–Young theorem).

## Compression

Image matrix có thể approximate bằng low-rank SVD. Thay lưu all pixels matrix, lưu `U_k,Σ_k,V_k`, nếu structure low-rank đủ mạnh.

Recommender systems và latent factor models dùng related idea: observed high-dimensional interactions được explained bởi small latent dimensions.

## PCA relation

Nếu centered data matrix `X`, PCA directions liên quan right singular vectors của `X`; singular values encode variance scales. SVD thường là numerical method để compute PCA mà không cần form covariance matrix explicitly.

## Other decompositions

LU factorization hữu ích solve repeated square systems. QR factorization dựa orthonormal columns và dùng least squares. Cholesky dùng symmetric positive-definite matrices và rất hiệu quả.

Decomposition là strategy chung: factor operator khó thành product của operators có structure dễ xử lý.

## Mental Model

> Matrix decomposition là đổi một transformation phức tạp thành chuỗi operations đơn giản. SVD nói mọi linear map = rotate coordinates → scale orthogonal directions → rotate again. Least squares là projection khi target nằm ngoài reachable subspace.

## Common Misconceptions

Least squares không đảm bảo causal model hoặc robust với outliers. SVD không chỉ dành cho square matrices. Tiny singular values có thể làm inverse problems unstable, vì inversion chia cho số rất nhỏ và amplify noise.
