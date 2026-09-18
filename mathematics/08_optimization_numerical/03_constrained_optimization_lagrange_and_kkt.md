# Tối ưu có ràng buộc, Lagrange multipliers và KKT

Unconstrained optimization hỏi point nào minimize `f(x)`. Nhưng practical problems gần như luôn có constraints: budget giới hạn, probabilities phải sum thành 1, resources không âm, latency dưới threshold. Constrained optimization (제약 최적화) tìm best point trong feasible set thay vì toàn space.

## Equality constraint và geometry của tangent space

Xét

```math
\min f(x,y)
```

subject to

```math
g(x,y)=c.
```

Feasible points nằm trên level curve của `g`. Tại optimum nằm trên smooth constraint curve, ta không thể giảm `f` bằng cách di chuyển theo bất kỳ tangent direction hợp lệ nào.

Gradient `\nabla g` vuông góc constraint curve. Nếu gradient `\nabla f` có component tangent khác 0, ta có thể đi theo tangent direction để giảm/tăng `f`. Vì vậy tại constrained local optimum thường cần

```math
\nabla f=\lambda\nabla g.
```

`\lambda` là Lagrange multiplier.

## Lagrangian

Define

```math
\mathcal L(x,\lambda)=f(x)+\lambda(g(x)-c).
```

Stationary conditions:

```math
\nabla_x\mathcal L=0,
```

```math
g(x)=c.
```

Ta solve variables và multiplier cùng nhau.

Ví dụ maximize area `A=xy` của rectangle với perimeter fixed `2x+2y=P`.

Constraint:

```math
x+y=P/2.
```

Lagrangian:

```math
\mathcal L=xy+\lambda(P/2-x-y).
```

Partial derivatives:

```math
\frac{\partial\mathcal L}{\partial x}=y-\lambda=0,
```

```math
\frac{\partial\mathcal L}{\partial y}=x-\lambda=0.
```

Suy ra `x=y`. Với fixed perimeter, square maximize area.

## Ý nghĩa của multiplier như shadow price

Trong nhiều optimization problems, multiplier `\lambda` đo sensitivity của optimal objective khi constraint resource thay đổi một chút.

Nếu budget constraint nới thêm 1 unit và optimum value cải thiện khoảng `\lambda` units, `\lambda` là marginal value của resource — shadow price trong economics/operations research.

## Inequality constraints

Bây giờ có

```math
g_i(x)\le0.
```

Một inequality có thể active tại optimum (`g_i(x)=0`) hoặc inactive (`g_i(x)<0`). Nếu inactive, locally nó không ép solution; multiplier tương ứng nên bằng 0.

Đây dẫn tới complementary slackness.

## KKT conditions

Với minimization có equality constraints `h_j(x)=0` và inequalities `g_i(x)\le0`, Lagrangian thường viết

```math
\mathcal L(x,\lambda,\nu)
=f(x)+\sum_i\lambda_i g_i(x)+\sum_j\nu_j h_j(x).
```

Karush–Kuhn–Tucker conditions gồm:

1. Stationarity:

```math
\nabla_x\mathcal L=0.
```

2. Primal feasibility:

```math
g_i(x)\le0,\qquad h_j(x)=0.
```

3. Dual feasibility:

```math
\lambda_i\ge0.
```

4. Complementary slackness:

```math
\lambda_i g_i(x)=0.
```

Last condition nói mỗi inequality hoặc slack (`g_i<0`) và multiplier zero, hoặc active (`g_i=0`) và multiplier có thể positive.

KKT là necessary under constraint qualifications và trở thành sufficient cho global optimum trong important convex settings.

## Convexity thay đổi toàn bộ độ khó logic

Nếu objective convex và feasible set convex, mọi local minimum là global minimum. Với differentiable convex problem và suitable regularity, KKT conditions characterize optimum mạnh mẽ.

Nếu nonconvex, KKT point có thể chỉ là local candidate, saddle-like constrained point hoặc không global.

## Projection như constrained optimization

Projection của point `v` lên set `C` giải

```math
\min_{x\in C}\|x-v\|^2.
```

Nếu `C` là linear subspace, solution là orthogonal projection. Nếu `C` là convex set, projection vẫn có unique geometry dưới common assumptions.

Projected gradient descent thực hiện gradient step rồi project trở lại feasible set.

## Probability simplex

Probability vector phải thỏa

```math
p_i\ge0,
```

```math
\sum_i p_i=1.
```

Đây là simplex — một convex feasible set. Maximum entropy, mixture weights và many ML problems optimize trên simplex.

Softmax parameterization là một cách map unconstrained logits thành strictly positive probabilities sum to 1, tức encode constraints bằng transformation thay vì optimizer explicit.

## Knowledge Connection

Lagrange multipliers nối gradients với geometry level sets. KKT nối inequalities với active-set logic. Duality nối optimization với economics và bounds. Regularization có thể được nhìn như constraint hoặc penalty dưới certain correspondences.

## Mental Model

> Unconstrained optimum có “không còn hướng nào để đi xuống”. Constrained optimum tinh tế hơn: có thể vẫn tồn tại hướng giảm objective, nhưng mọi hướng đó đi ra ngoài feasible set. Multipliers đo lực/sensitivity của các walls đang chặn solution.

## Common Misconceptions

Lagrange method không tự động cho global optimum. Multiplier không luôn có economic meaning nếu units/model không support interpretation. KKT conditions cần regularity assumptions và sign conventions phải nhất quán. Penalty method với coefficient hữu hạn không hoàn toàn giống hard constraint trong mọi problem.
