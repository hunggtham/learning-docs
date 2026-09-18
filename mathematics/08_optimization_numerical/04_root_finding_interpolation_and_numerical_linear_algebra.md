# Root finding, interpolation và numerical linear algebra

Nhiều equations không có closed-form solution hữu ích. Máy tính vì thế không “biết đáp án chính xác rồi in ra”; nó tạo một sequence approximations và kiểm soát error, convergence, conditioning.

## Root finding là solve `f(x)=0`

Phương trình tổng quát có thể rewrite thành root problem:

```math
f(x)=0.
```

### Bisection

Nếu `f` continuous trên `[a,b]` và `f(a),f(b)` trái dấu, Intermediate Value Theorem đảm bảo ít nhất một root trong interval.

Bisection chọn midpoint

```math
m=\frac{a+b}{2}
```

rồi giữ half interval còn sign change.

Sau `n` iterations, interval width là

```math
\frac{b-a}{2^n}.
```

Convergence chậm nhưng robust khi assumptions đúng.

### Newton's method

Linearize quanh current guess `x_n`:

```math
f(x)\approx f(x_n)+f'(x_n)(x-x_n).
```

Đặt approximation bằng 0:

```math
0=f(x_n)+f'(x_n)(x_{n+1}-x_n).
```

Suy ra

```math
x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}.
```

Near a simple root và với conditions tốt, convergence thường quadratic. Nhưng derivative nhỏ, initial guess xấu hoặc geometry phức tạp có thể khiến divergence.

Newton không “luôn nhanh hơn”; nó đổi robustness lấy tốc độ local.

## Fixed-point iteration

Rewrite equation thành

```math
x=g(x)
```

và iterate

```math
x_{n+1}=g(x_n).
```

Near fixed point `x^*`, nếu

```math
|g'(x^*)|<1,
```

mapping locally contracts distances và iteration có xu hướng converge. Đây là instance của contraction principle.

## Interpolation

Cho points `(x_i,y_i)`, interpolation tìm function đi qua points exactly. Polynomial interpolation dùng polynomial degree at most `n-1` qua `n` distinct x-values.

Lagrange form:

```math
P(x)=\sum_{i=1}^{n}y_iL_i(x),
```

với

```math
L_i(x)=\prod_{j\ne i}\frac{x-x_j}{x_i-x_j}.
```

Mỗi basis polynomial `L_i` bằng 1 tại `x_i` và 0 tại các nodes khác.

Nhưng high-degree polynomial qua equally spaced points có thể oscillate mạnh gần endpoints — Runge phenomenon. Splines xử lý bằng piecewise low-degree polynomials với smoothness constraints.

## Interpolation khác regression

Interpolation ép model qua mọi data point, phù hợp khi values được coi gần exact. Regression cho phép residuals và tìm trend/model khi observations noisy.

Overfitting xuất hiện khi ta dùng flexibility quá cao để fit noise như signal.

## Solving linear systems numerically

Gaussian elimination có complexity roughly `O(n^3)` cho dense `n\times n` systems. Nhưng implementation trực tiếp không phải toàn bộ câu chuyện.

Pivoting giúp tránh chia cho pivot quá nhỏ. LU factorization tách

```math
A=LU
```

để reuse solve cho nhiều right-hand sides.

QR factorization rất hữu ích cho least squares. Cholesky efficient khi matrix symmetric positive definite:

```math
A=LL^T.
```

## Condition number

Cho invertible matrix `A`, condition number theo norm phù hợp:

```math
\kappa(A)=\|A\|\|A^{-1}\|.
```

Nó đo worst-case amplification của relative input perturbations vào solution.

Nếu `\kappa` lớn, ngay cả algorithm stable cũng không thể tạo nhiều accurate digits hơn data cho phép. Đây là distinction giữa problem conditioning và algorithm stability.

## Floating-point arithmetic

Real numbers vô hạn precision không thể stored exact nói chung. IEEE floating point dùng finite significand/exponent.

Ví dụ decimal `0.1` không có finite binary representation, nên equality checks như

```text
0.1 + 0.2 == 0.3
```

có thể false trong nhiều languages.

Sai số rounding nhỏ nhưng có thể accumulate hoặc bị amplified bởi subtraction of nearly equal numbers, ill-conditioning, long iterative processes.

## Residual khác error

Với approximate solution `\hat x` cho

```math
Ax=b,
```

residual là

```math
r=b-A\hat x.
```

Error thực là

```math
e=x-\hat x.
```

Residual nhỏ không luôn đảm bảo error nhỏ nếu problem ill-conditioned.

## Knowledge Connection

Bisection dựa trên continuity. Newton dựa trên derivative/Taylor. Interpolation nối polynomial basis với approximation. Matrix factorizations nối linear algebra với numerical stability. Condition number formalize sensitivity — một concept cũng xuất hiện trong optimization và statistical estimation.

## Mental Model

> Numerical mathematics không hỏi “công thức chính xác là gì?” mà hỏi “với finite computation và finite precision, ta tạo approximation nào, convergence ra sao, và error đáng tin tới mức nào?”

## Common Misconceptions

Nhiều decimal digits in output không có nghĩa nhiều digits đúng. Newton có thể diverge. Interpolation qua mọi point không đồng nghĩa prediction tốt. Residual nhỏ khác solution error nhỏ. Tính explicit inverse thường không phải cách tốt để solve linear system.
