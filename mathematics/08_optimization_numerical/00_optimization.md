# Tối ưu hóa: objective, feasible set và geometry của trade-off

Tối ưu hóa (optimization / 최적화) không bắt đầu bằng gradient descent hay Lagrange multiplier. Nó bắt đầu bằng một modeling question:

> Ta được phép thay đổi điều gì, đang cố làm tốt điều gì, và constraints nào định nghĩa một solution hợp lệ?

Một optimizer cực mạnh vẫn có thể cho kết quả vô dụng nếu objective đo sai goal hoặc feasible set bỏ sót constraint quan trọng. Vì vậy optimization là sự kết hợp của **modeling + mathematical structure + computation**.

## Cấu trúc tối thiểu của một optimization problem

General form:

```math
\min_x f(x)
```

subject to

```math
g_i(x)\le0,
```

```math
h_j(x)=0.
```

`x` là decision variable. `f` là objective. Constraints xác định feasible set.

Một point có objective rất tốt nhưng violate constraint không phải solution.

## Worked modeling example — portfolio allocation đơn giản

Giả sử weights `w_i` của assets phải sum to one:

```math
\sum_iw_i=1.
```

Nếu long-only:

```math
w_i\ge0.
```

Expected return:

```math
\mu^Tw.
```

Variance risk:

```math
w^T\Sigma w.
```

Một mean-variance formulation có thể là

```math
\min_w
\frac12w^T\Sigma w-\lambda\mu^Tw
```

subject to budget/position constraints.

Parameter `\lambda` encodes trade-off preference. Mathematics không tự quyết định investor nên chấp nhận risk bao nhiêu; objective embeds that choice.

## Local optimum và global optimum

`x^*` là local minimum nếu nó tốt hơn points đủ gần.

Nó là global minimum nếu

```math
f(x^*)\le f(x)
```

cho mọi feasible `x`.

Nonconvex problems có thể có nhiều local minima và saddle points. First-order methods often reason locally; global guarantees cần extra structure.

## Convexity: structure biến local thành global

Function `f` convex nếu

```math
f(tx+(1-t)y)
\le
_tf(x)+(1-t)f(y),
\qquad 0\le t\le1.
```

Correct notation:

```math
f(tx+(1-t)y)
\le
 t f(x)+(1-t)f(y).
```

Geometrically, chord giữa hai graph points nằm above graph.

Nếu feasible set convex và objective convex, every local minimum is global. Đây là lý do convexity cực kỳ valuable: local conditions trở thành global certificates.

Strict convexity còn giúp uniqueness under suitable conditions.

## First-order convexity condition

Nếu `f` differentiable và convex:

```math
f(y)
\ge
f(x)+\nabla f(x)^T(y-x).
```

Tangent hyperplane nằm dưới graph everywhere.

Nếu

```math
\nabla f(x^*)=0,
```

then

```math
f(y)\ge f(x^*)
```

cho mọi `y`; stationary point là global minimum.

Đây là proof idea behind “gradient zero is enough” trong convex unconstrained optimization.

## Second-order viewpoint

Nếu twice differentiable, convexity liên hệ Hessian:

```math
H_f(x)\succeq0
```

trên convex domain.

Positive-semidefinite Hessian nghĩa curvature không downward theo bất kỳ direction nào.

Conditioning của Hessian quyết định optimization geometry. Nếu eigenvalues chênh lớn, level sets elongated và vanilla gradient descent có thể zig-zag/chậm.

## Gradient descent được derive từ local linear model

Taylor first-order:

```math
f(x+\Delta)
\approx
f(x)+\nabla f(x)^T\Delta.
```

Muốn giảm `f` với fixed small step norm, chọn direction opposite gradient:

```math
\Delta=-\eta\nabla f(x).
```

Update:

```math
x_{k+1}=x_k-\eta\nabla f(x_k).
```

Learning rate `\eta` không phải cosmetic hyperparameter. Quá lớn có thể overshoot/diverge; quá nhỏ convergence rất chậm.

## Worked quadratic example — learning rate và curvature

Cho

```math
f(x)=\frac12ax^2,
\qquad a>0.
```

Gradient:

```math
f'(x)=ax.
```

Gradient descent:

```math
x_{k+1}
=(1-\eta a)x_k.
```

Converge khi

```math
|1-\eta a|<1,
```

suy ra

```math
0<\eta<\frac2a.
```

Curvature `a` giới hạn stable step size. Trong many dimensions, largest Hessian eigenvalue đóng role tương tự.

## Constraints thay đổi geometry của allowable movement

Unconstrained optimum có thể move mọi direction. Constrained optimum chỉ được move trong feasible directions.

Với equality constraint

```math
g(x)=0,
```

feasible tangent directions `d` thỏa locally

```math
\nabla g(x)^Td=0.
```

Nếu objective gradient có component tangent, ta còn có thể improve. Tại smooth constrained optimum, gradient objective phải nằm trong span constraint normals.

Đó là intuition của Lagrange multipliers.

## Lagrange multipliers: alignment của normals

Optimize `f(x)` subject to

```math
g(x)=c.
```

At regular constrained optimum:

```math
\nabla f(x^*)
=
\lambda\nabla g(x^*).
```

Multiplier `\lambda` còn có shadow-price interpretation: under suitable conditions, nó đo sensitivity của optimal objective với small relaxation/tightening constraint.

Finance, economics và operations research dùng interpretation này để price scarce resources.

## Inequality constraints và KKT

For

```math
g_i(x)\le0,
```

KKT conditions include:

- primal feasibility;
- dual feasibility `\lambda_i\ge0`;
- stationarity;
- complementary slackness

```math
\lambda_i g_i(x)=0.
```

Complementary slackness means inactive constraint (`g_i<0`) has zero multiplier; positive multiplier can appear only when constraint binds.

KKT can be necessary under constraint qualifications; in convex problems with suitable conditions it often becomes sufficient.

## Duality: optimization nhìn từ prices/certificates

Primal problem chooses decisions. Dual problem often assigns multipliers/prices to constraints.

Weak duality gives bound: dual objective cannot beat primal optimum in wrong direction. Strong duality under suitable convex conditions means bounds meet exactly.

Dual variables help sensitivity analysis and prove optimality, not only compute answers.

## Linear programming: extreme-point geometry

Linear program:

```math
\min c^Tx
```

subject to linear constraints.

Feasible region là polyhedron. Linear objective contours là parallel hyperplanes. If finite optimum exists, an optimum can be found at an extreme point/face.

Simplex exploits this geometry by moving across vertices; interior-point methods travel through interior using different computational strategy.

## Discrete optimization: calculus không còn đủ

Nếu variables integer/binary, feasible set is disconnected.

Examples:

- scheduling;
- routing;
- knapsack;
- assignment;
- facility location.

Derivative may describe continuous relaxation but cannot directly choose discrete combinatorial state.

Methods include dynamic programming, branch-and-bound, cutting planes, relaxations, heuristics và approximation algorithms.

## Dynamic programming và Bellman principle

Sequential optimization has state `s`, action `a`, transition and future value.

Bellman idea:

```math
V(s)
=
\min_a
\{c(s,a)+V(s')\}
```

in deterministic simplified form.

Optimal solution has optimal substructure: once first decision chosen, remaining policy must itself be optimal for resulting state.

This connects optimization with control, reinforcement learning and shortest-path algorithms.

## Multi-objective optimization và Pareto frontier

Real systems rarely optimize only one metric. Cost, latency, reliability, fairness, return and risk may conflict.

A solution is Pareto optimal if no objective can improve without worsening at least one other.

Weighted-sum objective

```math
\min_x
\sum_kw_kf_k(x)
```

encodes preferences but can hide trade-off structure. Choosing weights is a policy/business decision, not purely mathematical deduction.

## Robust optimization: optimize when parameters are uncertain

If model parameters uncertain, optimizing nominal estimate can produce fragile solution.

Robust optimization asks for performance across an uncertainty set. Stochastic optimization optimizes expected/risk-sensitive objective over distributions.

This is important in portfolio allocation, supply chains, control and ML distribution shift.

## AI connection — training is optimization under model assumptions

Neural-network training minimizes empirical loss:

```math
\min_\theta
\frac1n\sum_{i=1}^n\ell(f_\theta(x_i),y_i).
```

But low training loss does not guarantee generalization. Optimization objective is proxy for desired real-world performance.

Regularization, validation and data distribution assumptions sit outside pure optimization geometry.

SGD uses noisy gradient estimates to trade computation per step against variance.

## Physics connection — energy minimization

Stable equilibria often minimize potential energy. Variational principles formulate physical laws as optimization over functions/paths.

This connects calculus of variations, PDEs, mechanics and optimal control.

## Finance connection — return, risk, constraints

Portfolio optimization makes trade-offs explicit but is highly sensitive to estimates of expected returns/covariance. Optimizer can amplify estimation noise by exploiting uncertain directions.

Thus robust constraints, shrinkage and regularization are not afterthoughts; they respond to model uncertainty.

## “Optimizer’s curse” và objective misspecification

If objective imperfectly represents desired outcome, stronger optimizer may exploit loopholes more aggressively.

Examples include recommendation systems maximizing engagement proxies, schedules minimizing mean latency while hurting tail latency, or portfolios chasing unstable estimated alpha.

Optimization does exactly what objective/constraints say, not what author vaguely intended.

## Assumptions và failure modes

Gradient methods assume differentiability or usable generalized gradients. Convex guarantees require convexity. KKT requires constraint qualifications for necessity and stronger structure for sufficiency.

Numerical scaling matters: badly scaled variables/constraints harm solver performance. Model parameters may be uncertain. Discrete problems can be computationally hard despite simple-looking objectives.

## Mental Model

> Optimization is geometry of choice under constraints. The objective defines what “better” means; feasible set defines where movement is allowed; derivatives describe local improvement; convexity tells when local information is globally trustworthy; dual variables price constraints; dynamic programming extends the same idea through time. The optimizer is only as meaningful as the model it is asked to optimize.

## Common Misconceptions

**“Optimization means take derivative and set zero.”** That handles only a narrow smooth unconstrained class.

**“Local minimum is good enough because optimizer found it.”** Depends on nonconvex landscape and problem goals.

**“Convex means function looks like a bowl in 2D only.”** Convexity is a high-dimensional inequality/geometry property.

**“KKT conditions always prove global optimum.”** Not without conditions such as convexity and constraint qualifications.

**“Best objective value means best real-world decision.”** Only if objective and constraints correctly encode real goal and uncertainty.