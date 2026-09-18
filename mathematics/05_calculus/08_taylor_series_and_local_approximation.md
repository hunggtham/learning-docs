# Taylor series và local approximation

Derivative không chỉ đo slope. Một chuỗi các derivatives tại một point có thể encode ngày càng nhiều local shape của function. Taylor approximation xây polynomial từ chính information đó.

## Từ linearization tới quadratic approximation

First-order approximation quanh `a`:

```math
f(x)\approx f(a)+f'(a)(x-a).
```

Ta muốn polynomial bậc hai có cùng value, first derivative và second derivative với `f` tại `a`:

```math
P_2(x)=c_0+c_1(x-a)+c_2(x-a)^2.
```

Matching:

```math
P_2(a)=c_0=f(a),
```

```math
P_2'(a)=c_1=f'(a),
```

```math
P_2''(a)=2c_2=f''(a).
```

nên

```math
c_2=\frac{f''(a)}{2!}.
```

General Taylor polynomial:

```math
P_n(x)=
\sum_{k=0}^{n}
\frac{f^{(k)}(a)}{k!}(x-a)^k.
```

Factorial xuất hiện vì derivative thứ `k` của `(x-a)^k` tại `a` bằng `k!`.

## Taylor series

Nếu infinite expansion actually converges to function:

```math
f(x)=
\sum_{k=0}^{\infty}
\frac{f^{(k)}(a)}{k!}(x-a)^k.
```

Đó là Taylor series. Khi `a=0`, gọi Maclaurin series.

Nhưng infinitely differentiable không tự động đảm bảo Taylor series equals function. Taylor representation cần convergence + equality conditions; smoothness alone không đủ.

## e^x

Với `f(x)=e^x`, mọi derivatives đều `e^x`, tại 0 đều bằng 1:

```math
e^x
=
1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots.
```

Đây là lý do exponential dễ tính bằng polynomial approximations.

## Sine và cosine

Derivatives của sine/cosine cycle, cho:

```math
\sin x
=
x-\frac{x^3}{3!}+\frac{x^5}{5!}-\cdots
```

```math
\cos x
=
1-\frac{x^2}{2!}+\frac{x^4}{4!}-\cdots.
```

Với small `x`:

```math
\sin x\approx x,
```

```math
\cos x\approx1-\frac{x^2}{2}.
```

Small-angle approximation phải dùng radians; nếu dùng degrees, derivative scaling khác.

## Error term

Lagrange remainder cho một form error:

```math
R_n(x)
=
\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}
```

cho một `ξ` giữa `a` và `x` dưới suitable conditions.

Nó cho biết error phụ thuộc higher derivative, distance tới expansion point và factorial denominator.

Taylor polynomial thường tốt nhất local quanh `a`, không uniformly tốt arbitrarily xa.

## Differential equations và linearization

Nonlinear system gần equilibrium có thể approximate bởi linear terms; Jacobian đóng vai trò first-order Taylor approximation. Đây là lý do linear algebra xuất hiện khi phân tích stability của nonlinear dynamics.

## Machine learning và second-order methods

Loss quanh parameter vector `θ`:

```math
L(\theta+\Delta)
\approx
L(\theta)
+
\nabla L^T\Delta
+
\frac12\Delta^TH\Delta.
```

Gradient là first-order Taylor data; Hessian là second-order. Newton methods chọn step dựa trên quadratic local model.

## Numerical computing

Nhiều math-library implementations evaluate functions bằng polynomial/rational approximations trên reduced domains, dù production algorithms sophisticated hơn raw Taylor series. Core principle vẫn là replace expensive function bằng approximation với controlled error.

## Knowledge Connection

Taylor nối derivative với polynomial, local approximation, numerical methods, physics perturbation, optimization và error propagation. Nó giải thích vì sao nhiều nonlinear phenomena trông linear ở sufficiently small scale: first-order term dominate khi displacement nhỏ.

## Mental Model

> Taylor expansion xây “local polynomial DNA” của function từ derivatives tại một point. Bậc 1 capture slope; bậc 2 capture curvature; higher orders capture finer local structure. Approximation mạnh vì polynomial dễ tính và dễ phân tích.

## Common Misconceptions

Taylor series không phải lúc nào cũng converge tới original function. Nhiều terms hơn không luôn tốt nếu evaluate numerically badly hoặc outside useful range. Small-angle `sin x≈x` dùng radians và chỉ tốt khi `|x|` nhỏ.
