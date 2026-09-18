# Eigenvalues và eigenvectors: những directions tự nhiên của linear transformation

Một matrix không chỉ là bảng số. Khi matrix `A` tác động lên vector, nó có thể scale, rotate, shear hoặc combine nhiều effects cùng lúc. Một cách rất mạnh để hiểu transformation là tìm những directions đặc biệt mà transformation không làm đổi direction, chỉ thay đổi magnitude và có thể đảo hướng.

Một nonzero vector `v` là **eigenvector (고유벡터)** của `A` nếu

```math
Av=\lambda v,
```

trong đó `λ` là **eigenvalue (고유값)** tương ứng.

Equation này nói rằng `v` là direction mà transformation hành xử đơn giản nhất: sau transformation, vector vẫn nằm trên cùng line với vector ban đầu.

## Vì sao eigenvectors là câu hỏi tự nhiên?

Giả sử `A` biến đổi cả không gian. Với một arbitrary vector, output có thể khó hiểu. Nhưng nếu tìm được basis gồm eigenvectors, mọi component theo từng eigenvector chỉ bị nhân với một scalar riêng.

Thay vì một transformation phức tạp, ta có nhiều independent one-dimensional scalings.

Đó là lý do eigen decomposition xuất hiện trong dynamic systems, PCA, Markov chains, differential equations, graph algorithms và stability analysis.

## Từ `Av = λv` đến characteristic equation

Ta rewrite

```math
Av=\lambda v
```

thành

```math
(A-\lambda I)v=0.
```

Muốn có nonzero solution `v`, matrix `A-λI` phải singular. Vì vậy

```math
\det(A-\lambda I)=0.
```

Equation này gọi là **characteristic equation**.

Polynomial

```math
p_A(\lambda)=\det(A-\lambda I)
```

là characteristic polynomial. Roots của polynomial là eigenvalues.

## Ví dụ 2×2

Cho

```math
A=\begin{bmatrix}2&1\\1&2\end{bmatrix}.
```

Ta solve

```math
\det(A-\lambda I)
=
\det\begin{bmatrix}2-\lambda&1\\1&2-\lambda\end{bmatrix}
=(2-\lambda)^2-1.
```

Do đó

```math
(2-\lambda)^2=1,
```

nên eigenvalues là

```math
\lambda_1=3,\qquad \lambda_2=1.
```

Với `λ=3`, solve

```math
(A-3I)v=0
```

cho direction

```math
v_1\propto\begin{bmatrix}1\\1\end{bmatrix}.
```

Với `λ=1`,

```math
v_2\propto\begin{bmatrix}1\\-1\end{bmatrix}.
```

Hai eigenvectors trực giao vì matrix symmetric.

## Eigenspace

Với eigenvalue `λ`, tất cả eigenvectors tương ứng cùng zero vector tạo thành null space

```math
E_\lambda=\ker(A-\lambda I).
```

Đây là **eigenspace (고유공간)**.

Một eigenvalue có thể có nhiều linearly independent eigenvectors. Dimension của eigenspace gọi là **geometric multiplicity**.

## Algebraic multiplicity và geometric multiplicity

Nếu eigenvalue `λ` xuất hiện `k` lần như root của characteristic polynomial, `k` là **algebraic multiplicity**.

Geometric multiplicity là

```math
\dim\ker(A-\lambda I).
```

Luôn có

```math
1\le \text{geometric multiplicity}
\le \text{algebraic multiplicity}.
```

Nếu tổng số independent eigenvectors đủ bằng dimension của space, matrix diagonalizable.

## Diagonalization

Nếu `A` có `n` independent eigenvectors `v_1,...,v_n`, đặt chúng làm columns của `P`:

```math
P=[v_1\ v_2\ \cdots\ v_n].
```

Gọi

```math
D=\operatorname{diag}(\lambda_1,\dots,\lambda_n).
```

Ta có

```math
AP=PD
```

và do `P` invertible,

```math
A=PDP^{-1}.
```

Đây không phải chỉ là trick algebra. `P^{-1}` đổi coordinates từ standard basis sang eigenbasis, `D` scale từng eigen-coordinate độc lập, rồi `P` đổi trở lại original basis.

## Powers của matrix

Từ

```math
A=PDP^{-1}
```

suy ra

```math
A^k=PD^kP^{-1}.
```

Vì `D` diagonal,

```math
D^k=\operatorname{diag}(\lambda_1^k,\dots,\lambda_n^k).
```

Repeated transformation vì vậy được hiểu qua powers của eigenvalues.

## Dynamic systems

Discrete linear system

```math
x_{k+1}=Ax_k
```

cho

```math
x_k=A^kx_0.
```

Nếu decompose initial state theo eigenvectors,

```math
x_0=c_1v_1+\cdots+c_nv_n,
```

thì

```math
x_k=c_1\lambda_1^kv_1+\cdots+c_n\lambda_n^kv_n.
```

Mỗi eigenmode evolve độc lập.

Nếu `|λ|<1`, mode decay. Nếu `|λ|>1`, mode grow. Nếu `λ=-1`, sign alternate. Nếu `λ` complex, mode thường encode rotation/oscillation.

## Spectral radius

**Spectral radius (스펙트럴 반지름)** là

```math
\rho(A)=\max_i|\lambda_i|.
```

Trong nhiều linear iterative systems, spectral radius quyết định long-term growth hoặc convergence.

Ví dụ nếu method có error update

```math
e_{k+1}=Ae_k,
```

thì `ρ(A)<1` thường là central condition để error decay asymptotically.

## Complex eigenvalues

Một real matrix có thể có complex eigenvalues. Ví dụ rotation matrix

```math
R=\begin{bmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{bmatrix}
```

có eigenvalues

```math
e^{i\theta},\qquad e^{-i\theta}.
```

Trong real plane không có nonzero direction giữ nguyên dưới nontrivial rotation, nhưng khi mở rộng sang complex space, rotation được representation như multiplication bởi complex phases.

Điều này nối eigenanalysis với complex numbers và oscillation.

## Defective matrices

Không phải matrix nào cũng diagonalizable.

Ví dụ

```math
A=\begin{bmatrix}1&1\\0&1\end{bmatrix}
```

có characteristic polynomial

```math
(1-\lambda)^2,
```

nên eigenvalue `1` có algebraic multiplicity 2. Nhưng

```math
A-I=\begin{bmatrix}0&1\\0&0\end{bmatrix}
```

có null space dimension 1. Chỉ có một independent eigenvector.

Matrix như vậy gọi là **defective** và không diagonalizable.

## Jordan form intuition

Khi matrix không diagonalizable, ta vẫn có thể đưa nó về Jordan form trên complex numbers dưới broad conditions.

Một Jordan block có dạng

```math
J=\begin{bmatrix}
\lambda&1&0&\cdots\\
0&\lambda&1&\cdots\\
\vdots&&\ddots&1\\
0&\cdots&0&\lambda
\end{bmatrix}.
```

Extra ones trên superdiagonal encode failure to have enough eigenvectors.

Jordan form quan trọng về theory, dù numerically thường không stable để compute trực tiếp.

## Symmetric matrices và spectral theorem

Nếu `A` là real symmetric,

```math
A=A^T,
```

thì mọi eigenvalues đều real và tồn tại orthonormal eigenbasis.

Ta có

```math
A=Q\Lambda Q^T
```

với `Q` orthogonal.

Đây là **spectral theorem**.

Nó đặc biệt quan trọng vì covariance matrices và Hessians của sufficiently smooth scalar functions là symmetric.

## Positive definite matrices

Một symmetric matrix `A` positive definite nếu

```math
x^TAx>0
```

cho mọi `x≠0`.

Với symmetric `A`, điều này tương đương mọi eigenvalues đều positive.

Nếu tất cả eigenvalues nonnegative, matrix positive semidefinite.

Điều này liên hệ trực tiếp với convexity của quadratic functions và covariance structure.

## Rayleigh quotient

Cho symmetric `A`, define

```math
R_A(x)=\frac{x^TAx}{x^Tx}.
```

Rayleigh quotient cho effective scaling của quadratic form theo direction `x`.

Ta có

```math
\lambda_{min}\le R_A(x)\le\lambda_{max}.
```

Maximum Rayleigh quotient đạt tại eigenvector của largest eigenvalue; minimum đạt tại eigenvector của smallest eigenvalue.

Đây là foundation của PCA, spectral methods và optimization algorithms.

## PCA

Covariance matrix

```math
\Sigma=\frac1nX^TX
```

là symmetric positive semidefinite.

Eigenvectors của `Σ` chỉ principal directions của data. Eigenvalues đo variance theo các directions đó.

PCA chọn eigenvectors tương ứng với largest eigenvalues để giữ directions chứa nhiều variance nhất.

Điều này không có nghĩa “largest eigenvalue luôn là feature quan trọng nhất”. Interpretation chỉ đúng trong context covariance và PCA objective.

## SVD và eigen decomposition

Với general matrix `A`, SVD luôn tồn tại:

```math
A=U\Sigma V^T.
```

Right singular vectors là eigenvectors của

```math
A^TA,
```

left singular vectors là eigenvectors của

```math
AA^T.
```

Squared singular values là eigenvalues tương ứng.

SVD robust hơn eigen decomposition cho rectangular matrices và nhiều numerical tasks.

## Markov chains

Nếu transition matrix `P` dùng row-vector convention, stationary distribution `π` thỏa

```math
\pi=\pi P.
```

Vì vậy `π` là left eigenvector với eigenvalue 1.

Repeated multiplication bởi transition matrix damp nhiều modes khác nhau; long-run behavior thường dominated bởi eigenvalue magnitude lớn nhất, đặc biệt eigenvalue 1 trong ergodic chains.

## Graph spectral methods

Graph Laplacian

```math
L=D-A
```

trong đó `D` là degree matrix và `A` adjacency matrix, có eigenstructure encode connectivity của graph.

Số zero eigenvalues liên quan số connected components. Eigenvector tương ứng với second-smallest eigenvalue, gọi là Fiedler vector, được dùng trong spectral clustering và graph partitioning.

## Differential equations

Linear ODE system

```math
\frac{dx}{dt}=Ax
```

có solution

```math
x(t)=e^{At}x(0).
```

Nếu `A` diagonalizable,

```math
e^{At}=Pe^{Dt}P^{-1},
```

và each mode evolve như

```math
e^{\lambda_i t}.
```

Real part của eigenvalue quyết định growth/decay; imaginary part quyết định oscillation frequency.

## Power iteration

Nếu một matrix có unique dominant eigenvalue theo magnitude và initial vector có component theo dominant eigenvector, repeated multiplication

```math
x_{k+1}=Ax_k
```

rồi normalize sẽ hướng tới dominant eigenvector.

Đây là **power iteration**.

Algorithm giải thích trực giác vì sao repeated transformation làm dominant mode lấn át các modes nhỏ hơn.

## Numerical sensitivity

Eigenvalues của symmetric matrices thường numerically well-behaved hơn eigenvalues của highly non-normal matrices.

Một matrix có eigenvalues nhìn ổn định vẫn có thể có transient amplification nếu eigenvectors gần linearly dependent. Vì vậy eigenvalues không phải toàn bộ story trong stability analysis.

Conditioning của eigenproblem quan trọng khi dùng eigenvalues từ floating-point computation.

## Mental Model

Hãy xem linear transformation như một machine trộn nhiều directions. Eigenvectors là những directions mà machine không trộn với directions khác; nó chỉ scale. Khi một eigenbasis tồn tại, ta đổi coordinates để nhìn machine như nhiều independent scalar multipliers.

Eigenvalues sau đó trở thành “growth factors” của các natural modes. Repeated dynamics, covariance geometry, graph diffusion và differential equations đều dùng cùng structure này.

## Common Misconceptions

Eigenvector không thể là zero vector. Không phải every matrix diagonalizable. Repeated eigenvalue không đồng nghĩa có nhiều independent eigenvectors tương ứng.

Largest eigenvalue không luôn “quan trọng nhất” nếu chưa xác định problem. Trong PCA nó liên quan maximum variance; trong dynamics magnitude lớn có thể dominate long-term behavior; trong optimization Hessian eigenvalues encode curvature.

Complex eigenvalues của real matrix không phải lỗi. Chúng thường encode rotations và oscillations.

## Liên kết kiến thức

Nên đọc cùng [Determinant, rank, null space và inverse](./07_determinant_rank_nullspace_and_inverse.md), [SVD và decompositions](./05_least_squares_svd_and_decompositions.md), [Stochastic processes và Markov chains](../06_probability_statistics/11_stochastic_processes_markov_chains_and_time_series.md), [Differential equations](../05_calculus/05_differential_equations.md) và [Optimization](../08_optimization_numerical/00_optimization.md).