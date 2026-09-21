# Taylor series và local approximation: derivatives như local polynomial information

Derivative bậc một cho slope. Derivative bậc hai cho curvature. Higher derivatives mô tả các lớp local behavior ngày càng tinh hơn.

Taylor approximation gom toàn bộ information này thành một polynomial quanh một expansion point `a`.

Mental flow:

```text
function
→ local value
→ local slope
→ local curvature
→ higher-order shape
→ polynomial approximation
→ remainder/error
```

Taylor không phải chỉ là một công thức series. Nó là framework trả lời:

> Nếu chỉ biết local derivatives tại một point, ta có thể reconstruct hoặc approximate function quanh đó đến mức nào?

## 1. Bắt đầu từ linearization

Với differentiable function:

```math
f(a+h)
\approx
f(a)+f'(a)h.
```

Đây là first-order Taylor approximation.

Nó nói rằng sufficiently close to `a`, nonlinear function nhìn gần như affine.

Error first-order thường nhỏ hơn order `h` dưới suitable smoothness; nếu có second derivative bounded, error thường scale như `O(h^2)`.

## 2. Vì sao quadratic term có hệ số 1/2?

Muốn polynomial

```math
P_2(x)=c_0+c_1(x-a)+c_2(x-a)^2
```

match function value, slope và curvature tại `a`.

Conditions:

```math
P_2(a)=f(a)
```

cho

```math
c_0=f(a).
```

Derivative:

```math
P_2'(x)=c_1+2c_2(x-a)
```

nên

```math
c_1=f'(a).
```

Second derivative:

```math
P_2''(x)=2c_2
```

nên

```math
c_2=\frac{f''(a)}{2!}.
```

Factorial không xuất hiện bí ẩn; nó bù cho việc differentiate power nhiều lần.

## 3. General Taylor polynomial

Taylor polynomial bậc `n` quanh `a`:

```math
P_n(x)
=
\sum_{k=0}^{n}
\frac{f^{(k)}(a)}{k!}
(x-a)^k.
```

Nó là unique polynomial degree ≤ `n` có cùng derivatives tới order `n` với `f` tại `a`.

Đây là characterization quan trọng hơn việc chỉ nhớ formula.

## 4. Taylor series khác Taylor polynomial

Taylor polynomial luôn finite:

```math
P_n(x).
```

Taylor series là infinite formal expansion:

```math
\sum_{k=0}^{\infty}
\frac{f^{(k)}(a)}{k!}(x-a)^k.
```

Để viết

```math
f(x)=\text{Taylor series}
```

cần chứng minh remainder → 0 trong region đang xét.

Smoothness `C^\infty` alone chưa đủ.

## 5. Smooth nhưng không analytic

Một classic example:

```math
f(x)=
\begin{cases}
e^{-1/x^2},&x\ne0\\
0,&x=0.
\end{cases}
```

Function này infinitely differentiable tại 0 và mọi derivatives tại 0 đều bằng 0.

Taylor series quanh 0 vì vậy là zero series:

```math
0+0x+0x^2+\cdots
```

nhưng function không zero khi `x\ne0`.

Do đó:

```text
infinitely differentiable ≠ analytic
```

Analytic nghĩa function locally equals its convergent power series.

## 6. Lagrange remainder cho error estimate

Dưới suitable conditions:

```math
R_n(x)
=
f(x)-P_n(x)
=
\frac{f^{(n+1)}(\xi)}{(n+1)!}
(x-a)^{n+1}
```

cho một `\xi` giữa `a` và `x`.

Nếu

```math
|f^{(n+1)}(t)|\le M
```

trên interval, thì

```math
|R_n(x)|
\le
\frac{M}{(n+1)!}|x-a|^{n+1}.
```

Đây là bridge từ symbolic approximation sang certified error.

## 7. e^x là ideal Taylor function

Vì mọi derivatives của `e^x` đều là `e^x`, tại 0:

```math
f^{(k)}(0)=1.
```

Do đó:

```math
e^x
=
1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots.
```

Factorial denominator làm terms shrink rất nhanh cho fixed `x`, nên radius of convergence là infinite.

## 8. sin và cos: derivative cycle tạo coefficient pattern

Derivatives cycle:

```text
sin → cos → -sin → -cos → sin
```

Tại 0 cho:

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

Small-angle approximations:

```math
\sin x\approx x
```

```math
\cos x\approx1-\frac{x^2}{2}.
```

Angles phải tính bằng radians để derivatives có form chuẩn này.

## 9. ln(1+x) và finite radius

Around 0:

```math
\ln(1+x)
=
x-\frac{x^2}{2}+\frac{x^3}{3}-\cdots
```

valid trong convergence region phù hợp.

Singularity tại `x=-1` giới hạn radius quanh 0.

Deep connection:

> Radius of convergence thường bị giới hạn bởi nearest singularity trong complex plane.

Ngay cả khi đang học real calculus, complex analysis giải thích sâu hơn tại sao power series dừng ở đâu.

## 10. Local approximation quality phụ thuộc distance tới center

Taylor polynomial quanh `a` thường tốt nhất gần `a`.

Term error chứa factor:

```math
|x-a|^{n+1}.
```

Đi xa center làm error grow nhanh nếu không tăng degree hoặc đổi center.

Numerical libraries thường dùng **range reduction**:

```text
reduce input to small region
→ approximate accurately there
→ transform result back
```

thay vì dùng một Taylor polynomial quanh 0 cho mọi input.

## 11. Taylor theorem giải thích derivative meaning sâu hơn

First-order:

```math
f(a+h)=f(a)+f'(a)h+O(h^2)
```

under enough smoothness.

Second-order:

```math
f(a+h)
=
f(a)+f'(a)h
+\frac12f''(a)h^2
+O(h^3).
```

Notation `O(h^k)` nói error scale no faster than constant times `|h|^k` near zero.

Taylor vì vậy là formal language của “local behavior by orders of smallness”.

## 12. Why linearization works so often

Nếu `h` small:

```text
h       >> h² >> h³ >> ...
```

về magnitude.

Do đó first nonzero low-order terms dominate.

Đây là lý do:

- small perturbations thường gần linear;
- error propagation dùng derivatives;
- local stability dùng Jacobian;
- small-angle physics dùng low-order expansions.

## 13. Multivariable Taylor expansion

Cho scalar function `f:\mathbb R^n\to\mathbb R`:

```math
f(x+\Delta)
\approx
f(x)
+
\nabla f(x)^T\Delta
+
\frac12\Delta^TH(x)\Delta.
```

Gradient là first-order sensitivity vector.

Hessian là second-order curvature matrix.

Quadratic form

```math
\Delta^TH\Delta
```

cho curvature theo direction `\Delta`.

## 14. Optimization: stationary point + Hessian

Tại critical point:

```math
\nabla f(x_*)=0.
```

Taylor local model:

```math
f(x_*+\Delta)
\approx
f(x_*)+
\frac12\Delta^TH\Delta.
```

Nếu Hessian positive definite → local bowl → strict local minimum.

Nếu negative definite → local maximum.

Nếu indefinite → saddle.

Second derivative test là consequence của quadratic Taylor geometry.

## 15. Newton's method đến từ quadratic/local linear model

Để solve scalar equation

```math
f(x)=0,
```

first-order Taylor quanh `x_n`:

```math
0
\approx
f(x_n)+f'(x_n)(x_{n+1}-x_n).
```

Solve:

```math
x_{n+1}
=
x_n-
\frac{f(x_n)}{f'(x_n)}.
```

Newton method không phải formula ngẫu nhiên; nó tìm zero của local tangent approximation.

Trong optimization, Newton step từ quadratic model:

```math
\Delta=-H^{-1}\nabla f.
```

## 16. Error propagation là first-order Taylor

Nếu

```math
y=f(x)
```

và measurement error `\Delta x` small:

```math
\Delta y
\approx
f'(x)\Delta x.
```

Multivariable:

```math
\Delta y
\approx
\nabla f^T\Delta x.
```

Nếu input uncertainty covariance `\Sigma_x`, linearized output variance:

```math
\operatorname{Var}(y)
\approx
\nabla f^T\Sigma_x\nabla f.
```

Taylor approximation là foundation của uncertainty propagation.

## 17. Physics: small oscillation approximation

Pendulum equation:

```math
\theta''+
\frac gL\sin\theta=0.
```

For small angle:

```math
\sin\theta\approx\theta.
```

System becomes linear:

```math
\theta''+
\frac gL\theta=0.
```

Nonlinear pendulum locally behaves like harmonic oscillator.

Assumption is not “pendulum equation simplified magically”; it is a Taylor truncation valid for small `|\theta|`.

## 18. Relativity/engineering style perturbation intuition

Expressions như

```math
(1+x)^\alpha
```

for small `x`:

```math
(1+x)^\alpha
\approx
1+\alpha x
+
\frac{\alpha(\alpha-1)}2x^2+\cdots.
```

This converts nonlinear multiplicative expressions into manageable polynomial corrections.

Perturbation methods across physics/engineering build on this logic.

## 19. AI: local loss geometry

Near parameter `\theta`:

```math
L(\theta+\Delta)
\approx
L(\theta)
+
\nabla L^T\Delta
+
\frac12\Delta^TH\Delta.
```

Gradient descent uses first-order local information.

Newton/quasi-Newton/preconditioning use curvature information more directly.

Sharp/flat directions correspond roughly to large/small Hessian eigenvalues locally.

## 20. Finance: delta-gamma approximation

For nonlinear portfolio value `V(S)`:

```math
\Delta V
\approx
V'(S)\Delta S
+
\frac12V''(S)(\Delta S)^2.
```

Finance terminology:

```text
Delta  → first derivative sensitivity
Gamma  → second derivative curvature
```

Again, this is just second-order Taylor approximation.

## 21. Taylor vs polynomial interpolation

Taylor polynomial chooses coefficients from derivatives at one point.

Interpolation polynomial chooses coefficients to match values at several points.

Both produce polynomials but encode different information.

Taylor is local derivative matching; interpolation is multi-point value matching.

## 22. Taylor vs Fourier

Taylor basis:

```text
1, (x-a), (x-a)², ...
```

is local polynomial structure.

Fourier basis:

```text
sin(kx), cos(kx)
```

captures global frequency structure.

A periodic function may be represented much more naturally by Fourier series than Taylor series.

Representation should match structure.

## 23. Asymptotic expansion may be useful even if series diverges

Not every useful expansion is convergent.

An asymptotic series may satisfy:

```text
first few terms improve approximation as parameter → limit
```

while infinite series itself diverges.

This matters in advanced physics/numerical analysis: usefulness of truncation does not always require convergence of infinite expansion.

## 24. Numerical danger: more terms can make result worse

In exact arithmetic, adding Taylor terms within convergence region tends toward function.

In floating point:

- large intermediate terms may cancel;
- factorial/powers may overflow/underflow;
- rounding accumulates;
- evaluation order matters.

Horner form often evaluates polynomial more stably/efficiently:

```math
c_0+x(c_1+x(c_2+\cdots)).
```

## 25. Range reduction example for e^x

Instead of approximate huge `x` directly, write:

```math
x=k\ln2+r
```

with small `r`.

Then:

```math
e^x=2^ke^r.
```

Approximate `e^r` where `r` small.

This illustrates engineering principle:

```text
mathematical identity
+ local approximation
+ numerical representation
```

## 26. Worked example: approximate e^0.1

Third-order Maclaurin:

```math
P_3(x)
=1+x+\frac{x^2}{2}+\frac{x^3}{6}.
```

At `x=0.1`:

```math
P_3(0.1)
=1+0.1+0.005+0.0001667
\approx1.1051667.
```

True value roughly `1.105170...`, so error is only a few millionths.

Reason approximation works well: `x` is small and factorial denominator suppresses higher terms.

## 27. Worked example: when sin x ≈ x fails

At `x=0.1 rad`:

```math
\sin(0.1)\approx0.09983
```

close to `0.1`.

At `x=2 rad`:

```math
\sin2\approx0.909
```

far from `2`.

Approximation is local. Same formula used outside its validity region becomes a modeling error.

## 28. Proof idea behind Taylor theorem

Full proof may use repeated Mean Value Theorem or integral remainder.

Core idea:

1. build polynomial matching derivatives at `a`;
2. subtract it from `f`;
3. resulting error function has many derivatives vanishing at `a`;
4. Mean Value-type arguments force error to contain high power `(x-a)^{n+1}`.

Factorial and higher derivative emerge naturally from repeated differentiation.

## 29. Analyticity and complex singularities

For many familiar analytic functions, Taylor radius around `a` equals distance to nearest singularity in complex plane.

Example:

```math
f(x)=\frac1{1+x^2}.
```

As real function smooth everywhere, but complex singularities at

```math
z=\pm i.
```

Distance from 0 is 1, so Maclaurin radius is 1.

Complex analysis explains convergence limits that real graph alone does not reveal.

## Knowledge Connection

```text
derivatives
→ local polynomial model
→ Taylor theorem
→ error/remainder
→ numerical approximation
→ Newton methods
→ Hessian optimization
→ uncertainty propagation
→ perturbation physics
→ delta-gamma finance
→ analytic functions / complex singularities
```

## Mental Model

> Taylor expansion is a **local information compressor**. Derivatives at one point become polynomial coefficients. First order records slope, second order curvature, higher orders finer shape. The approximation is useful only together with its **center, order and error regime**.

## Common Misconceptions

`C^\infty` does not imply analytic. More Taylor terms are not automatically numerically better. A Taylor approximation valid near one center need not work far away. `sin x\approx x` assumes radians and small `x`. Taylor polynomial and Taylor series are different objects. A convergent Taylor series must still be shown to converge to the original function, not merely converge to something.