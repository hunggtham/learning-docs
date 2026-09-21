# Tối ưu có ràng buộc, Lagrange multipliers và KKT: geometry của feasible directions

Unconstrained optimization hỏi:

```math
\min_x f(x).
```

Nhưng phần lớn bài toán thực tế chỉ cho phép một subset của space:

```text
budget ≤ limit
probabilities sum to 1
resources ≥ 0
risk ≤ threshold
latency ≤ SLA
```

Constrained optimization vì vậy không hỏi “điểm thấp nhất của toàn landscape ở đâu?”, mà hỏi:

> Trong **feasible set** được phép, point nào tốt nhất?

Mental flow:

```text
objective
→ feasible set
→ feasible directions
→ active constraints
→ multipliers
→ KKT
→ duality / sensitivity
```

## 1. Feasible set quan trọng ngang objective

Problem:

```math
\min_x f(x)
```

subject to:

```math
g_i(x)\le0,
\qquad
h_j(x)=0.
```

Feasible set:

```math
\mathcal F
=
\{x:g_i(x)\le0,\;h_j(x)=0\}.
```

Optimization chỉ được di chuyển bên trong `\mathcal F`.

Một point có gradient khác zero vẫn có thể là constrained optimum nếu mọi downhill direction đều vi phạm constraints.

## 2. Equality constraint và tangent geometry

Xét:

```math
\min f(x)
```

subject to:

```math
g(x)=c.
```

Feasible movement local nằm trong tangent space của level set.

Gradient constraint:

```math
\nabla g
```

vuông góc tangent directions.

Tại regular constrained optimum, directional derivative của `f` theo mọi feasible tangent direction phải zero. Do đó:

```math
\nabla f
```

không có tangent component và phải nằm trong normal span:

```math
\nabla f=\lambda\nabla g.
```

Đây là geometric origin của Lagrange multiplier.

## 3. Lagrangian

Với equality:

```math
h(x)=0,
```

define:

```math
\mathcal L(x,\nu)=f(x)+\nu h(x).
```

First-order candidate conditions:

```math
\nabla_x\mathcal L=0,
```

```math
h(x)=0.
```

Multiplier `\nu` là coefficient needed để combine constraint normal với objective gradient.

## 4. Worked example: fixed perimeter rectangle

Maximize:

```math
A(x,y)=xy
```

subject to:

```math
2x+2y=P.
```

Equivalent:

```math
h(x,y)=x+y-P/2=0.
```

Lagrangian:

```math
\mathcal L
=xy+\nu(P/2-x-y).
```

Stationarity:

```math
y-\nu=0,
```

```math
x-\nu=0.
```

Thus:

```math
x=y.
```

Constraint gives square.

Theorem/method gives candidate; global maximum conclusion còn dựa geometry/concavity/feasible domain.

## 5. Multiplier như sensitivity / shadow price

Suppose constraint:

```math
h(x)=b.
```

Optimal value:

```math
V(b).
```

Under suitable regularity/sign convention, multiplier relates to:

```math
\frac{dV}{db}.
```

Interpretation: nếu resource bound được nới nhẹ, optimal objective thay đổi khoảng bao nhiêu?

Operations research/economics gọi đây là shadow price.

Units phải được kiểm tra: multiplier có unit “objective per constraint-unit”.

## 6. Inequality constraint khác equality ở chỗ có thể inactive

Consider:

```math
g(x)\le0.
```

At optimum:

```text
g(x)<0 → constraint inactive/slack
g(x)=0 → constraint active
```

Nếu inactive, nó không chặn local movement; multiplier tương ứng nên zero trong KKT structure.

## 7. Lagrangian với inequalities

For minimization:

```math
\mathcal L(x,\lambda,\nu)
=
f(x)
+
\sum_i\lambda_i g_i(x)
+
\sum_j\nu_jh_j(x),
```

với convention:

```math
g_i(x)\le0.
```

Then inequality multipliers require:

```math
\lambda_i\ge0.
```

Sign convention đổi nếu constraint được viết direction khác.

## 8. KKT conditions

Karush–Kuhn–Tucker conditions:

### Stationarity

```math
\nabla f(x^*)
+
\sum_i\lambda_i^*\nabla g_i(x^*)
+
\sum_j\nu_j^*\nabla h_j(x^*)
=0.
```

### Primal feasibility

```math
g_i(x^*)\le0,
```

```math
h_j(x^*)=0.
```

### Dual feasibility

```math
\lambda_i^*\ge0.
```

### Complementary slackness

```math
\lambda_i^*g_i(x^*)=0.
```

## 9. Complementary slackness là active-set logic

For each inequality:

```text
constraint slack → multiplier = 0
multiplier > 0 → constraint must be active
```

This captures which walls actually support the optimum.

It is one of the most useful conceptual parts of KKT.

## 10. Worked example: one-sided bound

Minimize:

```math
f(x)=(x-3)^2
```

subject to:

```math
x\le1.
```

Write:

```math
g(x)=x-1\le0.
```

Unconstrained minimum `x=3` infeasible. Feasible optimum is boundary `x=1`.

Lagrangian:

```math
\mathcal L=(x-3)^2+\lambda(x-1).
```

Stationarity at `x=1`:

```math
2(1-3)+\lambda=0
```

so:

```math
\lambda=4>0.
```

Positive multiplier reflects active constraint blocking descent toward `x=3`.

## 11. Constraint qualification: vì sao KKT không automatic?

KKT necessity requires regularity assumptions.

If constraint gradients degenerate or feasible geometry pathological, multipliers may fail to exist even at optimum.

Examples of constraint qualifications include LICQ and Slater's condition in convex settings.

Lesson:

> KKT is a theorem with assumptions, not a universal algebra recipe.

## 12. Convexity makes KKT much stronger

If:

```text
f convex
g_i convex
h_j affine
```

then feasible set convex.

Under suitable regularity, any KKT point is global optimum.

For nonconvex problem, KKT point may be only local candidate or saddle-like constrained stationary point.

## 13. Slater's condition intuition

For convex inequality problem, existence of a strictly feasible point:

```math
g_i(x)<0
```

for all inequalities often provides strong duality via Slater's condition.

Strict interior feasibility prevents certain boundary pathologies.

## 14. Dual function

Lagrangian dual function:

```math
q(\lambda,\nu)
=
\inf_x\mathcal L(x,\lambda,\nu).
```

For minimization, dual function gives lower bounds on primal optimum for dual-feasible multipliers.

Thus dual problem searches best lower bound:

```math
\max_{\lambda\ge0,\nu}q(\lambda,\nu).
```

## 15. Weak duality

For any primal feasible `x` and dual feasible `(\lambda,\nu)`:

```math
q(\lambda,\nu)\le f(x).
```

Therefore:

```text
dual optimum ≤ primal optimum
```

for minimization.

This bound holds very generally.

## 16. Strong duality

Under suitable convexity/regularity:

```text
dual optimum = primal optimum
```

Dual variables then gain strong sensitivity/economic interpretation.

Duality gap zero becomes both theoretical guarantee and numerical stopping signal in algorithms.

## 17. Equality constraint example via geometry

Minimize distance from origin:

```math
f(x,y)=x^2+y^2
```

subject to line:

```math
x+y=1.
```

Constraint gradient:

```math
(1,1).
```

Objective gradient:

```math
(2x,2y).
```

At optimum they align:

```math
(2x,2y)=\lambda(1,1),
```

so `x=y`; constraint gives:

```math
x=y=1/2.
```

This is orthogonal projection of origin onto the line.

## 18. Projection as constrained optimization

Projection onto convex set `C`:

```math
\min_{x\in C}\frac12\|x-v\|^2.
```

For linear subspace, solution satisfies orthogonality.

For closed convex set, Euclidean projection is unique.

This links constrained optimization directly with inner-product geometry.

## 19. Projected gradient descent

For simple convex feasible set:

```math
x_{k+1}
=\Pi_C(x_k-\eta\nabla f(x_k)).
```

Algorithm alternates:

```text
gradient step toward lower objective
→ project back into feasible set
```

Useful when projection is cheap.

## 20. Penalty method

Replace hard constraint with penalty:

```math
f(x)+\rho\,\phi(g(x)).
```

Large violation increases objective.

But finite penalty does not always exactly enforce hard constraint.

Very large `\rho` can cause poor conditioning.

## 21. Barrier method

For inequality `g(x)<0`, logarithmic barrier:

```math
-\mu\log(-g(x))
```

blows up near boundary.

Interior-point methods solve sequence of barrier problems as `\mu→0`.

This is fundamentally different from projected methods: stay interior instead of stepping outside then projecting.

## 22. Probability simplex

Probability vector:

```math
p_i\ge0,
\qquad
\sum_i p_i=1.
```

Feasible set is simplex.

Many ML problems optimize weights/probabilities on simplex.

Softmax:

```math
p_i=\frac{e^{z_i}}{\sum_je^{z_j}}
```

parameterizes strictly positive interior points automatically.

Encoding constraints via parameterization can simplify optimization but may change geometry/conditioning.

## 23. Regularization vs constraints

Problems:

```math
\min f(x)+\lambda R(x)
```

and

```math
\min f(x)
\quad\text{s.t. }R(x)\le c
```

can correspond under suitable convexity and parameter relation, but not universally one-to-one for every `\lambda,c`.

Penalty and constraint are two views of trade-off, not always identical implementations.

## 24. L1 geometry và sparsity

Constraint:

```math
\|x\|_1\le c
```

has diamond-like geometry with corners aligned to coordinate axes.

Quadratic loss contours touching these corners often produce zero coordinates.

This geometric intuition helps explain why L1 regularization promotes sparsity.

## 25. Portfolio optimization connection

Classical setup:

```math
\min_w w^T\Sigma w
```

subject to:

```math
1^Tw=1
```

and possibly:

```math
\mu^Tw\ge r_0,
\qquad
w\ge0.
```

This combines quadratic objective with equality/inequality constraints.

KKT/duality make the structure transparent.

## 26. Resource allocation / shadow price

Suppose objective is profit and constraint is CPU capacity.

Multiplier on capacity constraint estimates marginal improvement if capacity increases one unit.

A high shadow price says resource is binding/valuable; zero multiplier says extra resource is not locally useful under current optimum/model.

## 27. Second-order conditions

First-order KKT identifies stationary candidates.

Second-order constrained analysis examines Hessian of Lagrangian restricted to feasible tangent directions.

Positive curvature on feasible directions supports local minimum classification.

This is constrained analogue of Hessian tests.

## 28. Active-set methods

Algorithms may guess which inequalities are active, solve equality-constrained subproblem, then update active set.

KKT complementary slackness provides theoretical logic behind active-set computation.

## 29. Nonconvex caution

Neural/network/control problems often nonconvex.

KKT conditions can still generate candidates, but:

```text
KKT satisfied ≠ global optimum
```

Global guarantees need additional structure.

## 30. Units and scaling matter

If one constraint uses dollars ~`10^6` and another normalized probability ~`1`, poorly scaled problem can cause numerical difficulty.

Rescaling variables/constraints may improve conditioning without changing underlying feasible set meaning.

## Knowledge Connection

```text
gradient geometry
→ tangent/normal spaces
→ Lagrange multipliers
→ KKT active constraints
→ duality / shadow prices
→ convex optimization algorithms
```

Inner products explain projection. Linear algebra supplies null/tangent spaces. Finance uses covariance quadratic objectives. AI uses simplex constraints, regularization and projected/proximal methods.

## Mental Model

> Constrained optimum is a point where all useful downhill directions are blocked by feasible geometry. Multipliers quantify which walls block movement and how valuable relaxing those walls would be.

## Common Misconceptions

Lagrange/KKT do not automatically give global optima. KKT needs constraint qualifications. Multiplier sign depends on constraint convention. Penalty is not identical to hard constraint in every setup. Shadow-price interpretation requires correct model/units and regularity. Strong duality is not universal outside suitable convex settings.
