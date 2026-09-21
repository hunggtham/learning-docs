# Ứng dụng của đạo hàm: shape, approximation, sensitivity và optimization

Biết tính đạo hàm chỉ là bước đầu. Sức mạnh thật sự đến khi ta dùng derivative để **đọc behavior của một function**, xây approximation, kiểm tra sensitivity và tìm optimum dưới constraints.

Một function có thể complicated globally nhưng derivative cho local information tại từng point. Nếu ghép những local clues lại, ta hiểu shape của toàn bộ graph.

## Sign của derivative cho biết direction của movement

Nếu

```math
f'(x)>0
```

trên một interval, `f` tăng ở đó. Nếu

```math
f'(x)<0,
```

`f` giảm.

Lý do intuitive: derivative là local slope. Positive slope nghĩa step nhỏ theo `x` tạo positive first-order change.

Nhưng statement formal cần assumptions phù hợp như differentiability trên interval. Ta không nên biến sign rule thành shortcut tách rời theorem.

## Critical point chỉ là candidate

Critical point thường là nơi

```math
f'(x)=0
```

hoặc derivative không tồn tại nhưng function vẫn defined.

Đây là nơi first-order behavior đặc biệt, nhưng không tự động là max/min.

Ví dụ

```math
f(x)=x^3
```

có

```math
f'(0)=0,
```

nhưng 0 không là local max hay min. Function vẫn tăng xuyên qua point đó.

## First derivative test: nhìn sign change thay vì chỉ nhìn zero

Nếu derivative đổi từ positive sang negative, function chuyển từ tăng sang giảm, nên có local maximum.

Nếu đổi từ negative sang positive, có local minimum.

Nếu không đổi sign, critical point có thể là flat inflection hoặc higher-order behavior.

Đây là reasoning robust hơn việc chỉ solve `f'=0`.

## Second derivative: slope itself đang thay đổi ra sao?

Second derivative

```math
f''(x)
```

là derivative của slope.

Nếu `f''>0`, slope đang tăng: graph concave up. Nếu `f''<0`, slope đang giảm: graph concave down.

Tại critical point `x_0` với

```math
f'(x_0)=0,
```

nếu

```math
f''(x_0)>0,
```

local quadratic model có curvature upward, nên thường là local minimum. Nếu `f''<0`, local maximum.

Nếu `f''=0`, test inconclusive. `x^4` tại 0 vẫn là minimum dù second derivative zero.

## Taylor viewpoint: vì sao second derivative test hoạt động?

Near `x_0`:

```math
f(x_0+h)
\approx
f(x_0)+f'(x_0)h+
\frac12f''(x_0)h^2.
```

Tại critical point, first-order term vanish:

```math
f(x_0+h)-f(x_0)
\approx
\frac12f''(x_0)h^2.
```

Vì `h^2\ge0`, sign của `f''` quyết định local curvature first nonzero order. Đây là reason behind test, không phải rule arbitrary.

## Inflection point không phải chỉ là nơi `f''=0`

Inflection point cần **change of concavity**.

`f''(x_0)=0` chỉ là candidate. Ví dụ

```math
f(x)=x^4
```

có `f''(0)=0` nhưng concavity vẫn upward hai phía, nên không có inflection.

Trong khi

```math
f(x)=x^3
```

đổi concavity quanh 0, nên 0 là inflection point.

## Optimization: phần khó thường là modeling, không phải differentiation

Một optimization problem cần ít nhất:

- decision variables;
- objective;
- feasible domain/constraints.

Derivative chỉ giúp sau khi model được viết đúng.

### Worked example — fixed perimeter rectangle

Perimeter fixed `P`:

```math
2x+2y=P.
```

Constraint cho

```math
y=\frac P2-x.
```

Area:

```math
A(x)=x\left(\frac P2-x\right).
```

Derivative:

```math
A'(x)=\frac P2-2x.
```

Critical point:

```math
x=\frac P4.
```

Then

```math
y=\frac P4.
```

Second derivative

```math
A''(x)=-2<0
```

confirms local maximum, và feasible interval cho thấy đây cũng là global maximum.

Learning point: constraint reduced a two-variable problem thành one-variable objective.

## Boundary matters

Trong constrained domain, optimum có thể nằm ở boundary dù derivative không zero.

Ví dụ maximize

```math
f(x)=x
```

trên `[0,1]`. Không có interior critical point; global maximum là `x=1`.

Do đó practical optimization workflow là:

```text
identify domain
→ find interior critical candidates
→ include boundaries / nondifferentiable points
→ compare objective values or use structural theorem.
```

## Local vs global optimum

Derivative tests thường local. Một function nonconvex có nhiều local minima.

Nếu function convex trên convex domain, local minimum trở thành global minimum. Đây là reason convexity quan trọng trong optimization: nó nâng local reasoning thành global guarantee.

## Sensitivity và error propagation

Local linearization:

```math
\Delta y\approx f'(x)\Delta x.
```

Nếu input uncertainty khoảng `\sigma_x`, first-order output uncertainty roughly scales với `|f'(x)|`.

Trong multi-input systems, gradient/Jacobian thay derivative scalar.

Điều này nối calculus với numerical conditioning và experimental uncertainty.

## Marginal quantities

Nếu cost `C(q)` phụ thuộc production quantity:

```math
C'(q)
```

là marginal cost: local cost increase per additional unit around current `q`.

Nếu revenue `R(q)`:

```math
R'(q)
```

là marginal revenue.

Profit

```math
\Pi(q)=R(q)-C(q)
```

có derivative

```math
\Pi'(q)=R'(q)-C'(q).
```

Interior optimum candidate thỏa

```math
R'(q)=C'(q).
```

Meaning: tăng thêm một unit không còn tạo marginal gain vượt marginal cost.

Đây là economic interpretation của first-order condition.

## Elasticity: sensitivity không phụ thuộc units

Derivative absolute phụ thuộc unit scale. Elasticity dùng

```math
E(x)=\frac{x}{f(x)}f'(x).
```

để đo approximate percentage output change per 1% input change.

Nếu demand `Q(p)` theo price `p`, price elasticity giúp compare sensitivity giữa products có scale khác nhau.

## Newton's method: dùng tangent để tìm root

Muốn solve

```math
f(x)=0,
```

linearize quanh current guess `x_n`:

```math
f(x)
\approx
f(x_n)+f'(x_n)(x-x_n).
```

Set approximation bằng zero:

```math
0=f(x_n)+f'(x_n)(x_{n+1}-x_n),
```

suy ra

```math
x_{n+1}
=
x_n-rac{f(x_n)}{f'(x_n)}.
```

Method nhanh gần a simple root nhưng không globally guaranteed. Small derivative, poor initial guess hoặc multiple roots có thể gây failure.

## Worked Newton example

Tìm `\sqrt2` bằng root của

```math
f(x)=x^2-2.
```

Then

```math
f'(x)=2x.
```

Newton update:

```math
x_{n+1}
=
\frac12\left(x_n+\frac2{x_n}\right).
```

Starting `x_0=1.5`:

```math
x_1\approx1.41667,
```

```math
x_2\approx1.41422.
```

Fast convergence comes from local quadratic error reduction under suitable conditions.

## Physics connection — equilibrium và stability

Potential energy `U(x)` tạo force

```math
F(x)=-U'(x).
```

Equilibrium thỏa `U'(x)=0`. Nếu `U''(x)>0`, potential local minimum, thường stable equilibrium. Nếu `U''<0`, local maximum, thường unstable.

Optimization language và physics stability share same curvature structure.

## AI connection — gradient-based learning

Training minimizes loss `L(\theta)`. In one dimension, derivative gives local descent direction. In many dimensions, gradient generalizes it.

But a zero gradient does not guarantee good model: it may be local minimum, saddle point, flat region hoặc numerical plateau.

Second-order curvature explains why same learning rate behaves differently across directions.

## Finance connection — local Greeks

Option Greeks là derivatives của price theo market variables. Delta là first derivative theo underlying; gamma là second derivative. They quantify local sensitivity, not exact finite move behavior for arbitrary price jumps.

Again, derivative means local response, not global prediction.

## Assumptions và failure modes

Derivative-based optimization assumes enough smoothness. Nonsmooth objectives require subgradients hoặc other methods.

Stationary point classification can fail if only low-order derivatives vanish. Constraints can invalidate unconstrained conclusions. Real-world objectives may be noisy, discrete hoặc nonstationary, so symbolic calculus may only approximate operational decision-making.

## Mental Model

> Derivative applications are about reading a local landscape. First derivative tells which way the terrain slopes; second derivative tells how the slope bends; constraints tell where movement is allowed. Optimization is not “set derivative to zero” but a structured search over feasible candidates using local geometry plus global assumptions.

## Common Misconceptions

**“`f'=0` nghĩa optimum.”** Chỉ là candidate.

**“Second derivative zero nghĩa inflection.”** Không; concavity phải thực sự change.

**“Tìm interior critical points là đủ.”** Boundary và nondifferentiable points có thể chứa global optimum.

**“Newton method luôn nhanh.”** Nó nhanh khi local assumptions tốt; otherwise có thể diverge hoặc converge tới root không mong muốn.

**“Derivative sensitivity là causal effect.”** Nó là sensitivity trong model; causality cần assumptions/data khác.