# Eigenvalues và eigenvectors: những hướng không đổi dưới transformation

Eigenvector (Eigenvector / 고유벡터) của matrix `A` là nonzero vector `v` sao cho transformation không đổi direction của nó, chỉ scale:

```math
Av=\lambda v
```

`λ` là eigenvalue (고유값).

## Tại sao đây là câu hỏi tự nhiên?

Một generic vector sau transformation có thể rotate, shear và scale. Nếu tìm được directions chỉ scale, transformation trở nên dễ hiểu hơn nhiều. Eigenvectors là natural axes của operator.

## Characteristic equation

Từ

```math
Av=\lambda v
```

suy ra

```math
(A-\lambda I)v=0.
```

Muốn có nonzero solution, matrix `A-λI` phải singular:

```math
\det(A-\lambda I)=0.
```

Equation này cho eigenvalues. Sau đó solve null space để tìm eigenvectors.

## Diagonalization

Nếu có đủ independent eigenvectors, đặt chúng thành columns matrix `P`:

```math
A=PDP^{-1}
```

với `D` diagonal chứa eigenvalues.

Then powers:

```math
A^n=PD^nP^{-1}
```

và `D^n` chỉ raise từng diagonal element. Repeated transformation trở nên đơn giản.

## Dynamic systems

Discrete system:

```math
x_{k+1}=Ax_k
```

cho

```math
x_k=A^kx_0.
```

Trong eigenbasis, mỗi component scale theo `λ_i^k`. Nếu `|λ|<1`, component decays; `|λ|>1` grows; negative/complex eigenvalues tạo flips/oscillations tùy context.

## Markov chains/PageRank intuition

Transition matrix repeated application có steady-state vector liên quan eigenvalue 1 dưới conventions thích hợp. PageRank cũng là eigenvector-like fixed-point problem với damping modifications.

## PCA

Covariance matrix symmetric nên có orthogonal eigenvectors. Eigenvectors với largest eigenvalues chỉ directions variance lớn nhất. PCA project data lên những directions đó để dimensionality reduction.

## Symmetric matrices

Real symmetric matrices có real eigenvalues và orthonormal eigenbasis. Đây là spectral theorem, rất quan trọng vì covariance/Hessian thường symmetric.

## Mental Model

> Eigenvectors là directions mà transformation “nhận ra như trục tự nhiên” và chỉ scale. Đổi sang eigenbasis có thể biến transformation phức tạp thành diagonal scaling độc lập theo từng mode.

## Common Misconceptions

Không phải mọi matrix diagonalizable. Eigenvector không thể là zero vector. Largest eigenvalue không tự động là “feature quan trọng nhất” ngoài context cụ thể.
