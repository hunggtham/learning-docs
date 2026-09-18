# Toán số: approximation, conditioning và stability

Toán số (Numerical mathematics / 수치해석) nghiên cứu cách giải problems toán học trên finite-precision computers. Một formula có thể exact về lý thuyết nhưng computation thực tế vẫn inaccurate nếu problem ill-conditioned hoặc algorithm unstable.

## Hai loại error quan trọng

Truncation/discretization error xuất hiện khi thay ideal infinite/continuous process bằng finite approximation. Rounding error xuất hiện vì floating-point chỉ biểu diễn finite set numbers.

Total error là interaction của hai nguồn, không phải cứ tăng iterations/giảm step là tốt vô hạn.

## Conditioning của problem

Conditioning hỏi output thật nhạy đến input perturbation đến đâu. Nếu tiny input error tạo huge output change, problem ill-conditioned dù algorithm hoàn hảo.

Ví dụ solve `Ax=b` với nearly singular `A`; small data noise có thể thay solution mạnh.

Condition number formalizes sensitivity trong specific norms.

## Stability của algorithm

Algorithm stable nếu computational errors không bị amplify quá mức so với inherent conditioning. Ill-conditioned problem và unstable algorithm là hai issues khác nhau.

Một backward-stable algorithm cho answer đúng chính xác của một nearby perturbed problem; đây là tiêu chuẩn mạnh trong numerical linear algebra.

## Root finding: bisection

Nếu continuous `f` có opposite signs tại endpoints `[a,b]`, Intermediate Value Theorem guarantee ít nhất một root. Bisection chọn midpoint và giữ half interval vẫn bracket sign change.

Interval width halve mỗi iteration:

```math
\frac{b-a}{2^k}
```

nên để error ≤ε cần roughly logarithmic number steps:

```math
k\gtrsim\log_2\frac{b-a}{\varepsilon}
```

Bisection robust nhưng convergence linear.

## Newton method

```math
x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}
```

có quadratic convergence near simple root under suitable conditions, nhưng không bracket root và có thể fail.

Trade-off: bisection dùng less local information nhưng strong guarantee; Newton dùng derivative và có thể rất nhanh nhưng fragile.

## Interpolation

Given data points, interpolation tìm function đi qua points. High-degree global polynomial interpolation có thể oscillate (Runge phenomenon); piecewise splines thường stable/local hơn.

Approximation choice nên match desired smoothness và data structure, không chỉ degree cao nhất có thể.

## Numerical linear algebra

Solve `Ax=b` bằng Gaussian elimination/LU, least squares bằng QR/SVD. Explicit inverse thường unnecessary và less stable/efficient.

Iterative methods như conjugate gradient tận dụng large sparse structure. Complexity không chỉ matrix size; sparsity và conditioning matter.

## Floating point

IEEE floating point roughly dạng

```math
(-1)^s\times m\times2^e
```

với finite significand. Relative spacing tăng theo magnitude. Operations round to nearest representable numbers.

Associativity có thể fail numerically:

```text
(a+b)+c != a+(b+c)
```

vì intermediate rounding khác.

## Reproducibility

Parallel reductions có thể sum theo order khác và tạo last-bit differences. Scientific/ML pipelines cần distinguish deterministic exact reproducibility và statistically equivalent outcomes.

## Mental Model

> Numerical analysis hỏi ba tầng: problem có nhạy không, approximation có error bao nhiêu, và algorithm trên floating point có khuếch đại error không. “Máy tính cho số” mới chỉ là bước đầu của reliability.

## Common Misconceptions

More decimal digits printed không nghĩa more accurate. Explicit matrix inverse không phải default solver. Smaller discretization step không luôn better. Mathematical equivalence không đảm bảo floating-point equivalence.
