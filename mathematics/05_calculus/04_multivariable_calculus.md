# Giải tích nhiều biến: từ nhiều partial derivatives đến local linear maps

Giải tích nhiều biến (multivariable calculus / 다변수 미적분학) bắt đầu khi một output phụ thuộc đồng thời vào nhiều inputs. Temperature phụ thuộc vị trí trong không gian, profit phụ thuộc price/cost/demand, neural-network loss phụ thuộc hàng triệu parameters. Khi đó một slope duy nhất không đủ; ta cần mô tả **sensitivity theo mọi direction**.

Intuition quan trọng nhất là: derivative trong nhiều biến không chỉ là một list partial derivatives. Nó là **best local linear transformation** mô tả cách small input perturbation biến thành output perturbation.

## Partial derivative: hỏi từng coordinate một

Với

```math
f(x,y),
```

partial derivative theo `x` giữ `y` fixed:

```math
\frac{\partial f}{\partial x}.
```

Tương tự cho `y`.

Ví dụ

```math
f(x,y)=x^2y+3y.
```

Ta có

```math
\frac{\partial f}{\partial x}=2xy,
```

```math
\frac{\partial f}{\partial y}=x^2+3.
```

Mỗi partial derivative là sensitivity theo một coordinate axis. Nhưng real perturbation thường không đi đúng theo axis; vì vậy ta cần gradient và directional derivative.

## Gradient: gói các coordinate sensitivities thành một vector

Với scalar-valued function

```math
f:\mathbb R^n\to\mathbb R,
```

gradient là

```math
\nabla f(x)
=
\begin{bmatrix}
\partial f/\partial x_1\\
\vdots\\
\partial f/\partial x_n
\end{bmatrix}.
```

Nếu perturb input bởi small vector `\Delta x`, first-order change là

```math
\Delta f
\approx
\nabla f(x)^T\Delta x.
```

Đây là multivariable version của

```math
\Delta y\approx f'(x)\Delta x.
```

## Vì sao gradient chỉ hướng steepest ascent?

Directional derivative theo unit vector `u`:

```math
D_uf(x)=\nabla f(x)\cdot u.
```

Theo Cauchy–Schwarz:

```math
\nabla f\cdot u
\le
\|\nabla f\|\|u\|.
```

Với `\|u\|=1`, maximum đạt khi `u` cùng direction với gradient. Vì vậy gradient là direction tăng nhanh nhất theo Euclidean metric; negative gradient là steepest local decrease.

Đây là proof idea của gradient descent geometry.

## Level sets và vì sao gradient vuông góc contour

Level set là set points thỏa

```math
f(x)=c.
```

Nếu ta move tangent theo level set, value của `f` không đổi first-order, nên directional derivative bằng zero:

```math
\nabla f\cdot u=0.
```

Do đó gradient perpendicular với tangent directions của level set.

Trong 2D, gradient normal với contour line. Trong 3D, gradient normal với level surface.

Đây là foundation của Lagrange multipliers: tại constrained optimum, objective gradient phải align với constraint normal nếu không còn feasible first-order improvement direction.

## Worked example — gradient của quadratic bowl

Cho

```math
f(x,y)=x^2+4y^2.
```

Gradient:

```math
\nabla f=(2x,8y).
```

Tại `(1,1)`:

```math
\nabla f(1,1)=(2,8).
```

Function tăng mạnh hơn theo `y` direction vì curvature/scaling lớn hơn. Negative gradient `(-2,-8)` là steepest Euclidean descent direction local.

Nếu features `x,y` có units/scales rất khác nhau, geometry của “steepest” cũng bị ảnh hưởng. Đây là lý do feature scaling và preconditioning matter trong optimization.

## Jacobian: derivative của vector-valued function

Nếu

```math
F:\mathbb R^n\to\mathbb R^m,
```

thì derivative tại point là matrix Jacobian:

```math
J_F(x)
=
\begin{bmatrix}
\partial F_1/\partial x_1&\cdots&\partial F_1/\partial x_n\\
\vdots&\ddots&\vdots\\
\partial F_m/\partial x_1&\cdots&\partial F_m/\partial x_n
\end{bmatrix}.
```

Local linearization:

```math
F(x+\Delta x)
\approx
F(x)+J_F(x)\Delta x.
```

Đây là statement trung tâm: Jacobian là local linear map từ input perturbations sang output perturbations.

## Chain rule trở thành matrix composition

Nếu

```math
F=G\circ H,
```

thì

```math
J_F(x)
=
J_G(H(x))J_H(x).
```

Meaning: local perturbation đi qua `H` trước, rồi qua `G`. Matrix multiplication xuất hiện vì local linear maps compose exactly like linear transformations.

Backpropagation là efficient organization của chain rule để tránh forming huge full Jacobians không cần thiết.

## Gradient, Jacobian và matrix-calculus conventions

Gradient có thể được viết row hoặc column tùy convention. Trong library này ưu tiên gradient column vector khi nói geometry:

```math
\nabla f\in\mathbb R^n.
```

Khi đọc papers/frameworks, phải check convention. Nhiều bugs notation đến từ assume shapes mà không verify.

## Hessian: curvature theo nhiều directions

Với scalar `f`, Hessian là matrix second derivatives:

```math
H_f(x)
=
\left[
\frac{\partial^2 f}{\partial x_i\partial x_j}
\right].
```

Second-order local model:

```math
f(x+\Delta)
\approx
f(x)
+
\nabla f(x)^T\Delta
+
\frac12\Delta^T H_f(x)\Delta.
```

Gradient cho tilt; Hessian cho local curvature.

Nếu Hessian positive definite tại a critical point, quadratic term positive mọi nonzero direction, nên có strict local minimum dưới smoothness phù hợp.

Nếu Hessian indefinite, có directions up và down: saddle point.

## Eigenvalues của Hessian và optimization geometry

Hessian symmetric khi mixed partials behave well. Its eigenvectors give principal curvature directions; eigenvalues give curvature strengths.

Nếu eigenvalues vary by orders of magnitude, loss landscape elongated. Gradient descent phải dùng learning rate nhỏ enough cho steep direction, nên progress theo flat direction chậm. Đây là condition-number intuition trong optimization.

## Constrained optimization và Lagrange multipliers

Muốn optimize `f(x)` dưới equality constraint

```math
g(x)=c,
```

tại smooth interior constrained optimum, feasible tangent directions nằm orthogonal với `\nabla g`. Để không còn first-order feasible improvement, `\nabla f` cũng phải normal với tangent space:

```math
\nabla f=\lambda\nabla g.
```

Lagrange multiplier không phải trick algebra; nó encode alignment of normals.

## Multiple integrals: accumulation trong nhiều dimensions

Double integral

```math
\iint_R f(x,y)\,dA
```

accumulates density over area. Triple integral accumulates over volume.

Nếu `f` là mass density kg/m², then integral over area gives mass kg. Units tiếp tục là sanity check.

## Change of variables và Jacobian determinant

Khi đổi coordinates, infinitesimal area/volume bị scale. Nếu

```math
x=T(u),
```

thì local volume scaling là

```math
|\det J_T(u)|.
```

Do đó

```math
\int f(x)\,dx
=
\int f(T(u))|\det J_T(u)|\,du.
```

Polar coordinates:

```math
x=r\cos\theta,
\qquad
y=r\sin\theta.
```

Jacobian determinant là `r`, nên

```math
dA=r\,dr\,d\theta.
```

Factor `r` không phải formula cần nhớ riêng; nó là local area expansion khi radial coordinate tăng.

## Probability connection — transformations của random variables

Nếu random vector `X` được transform thành `Y=T(X)`, density transformation cũng cần Jacobian determinant. Same geometry xuất hiện trong probability, normalizing flows và Bayesian computation.

Đây là connection sâu: change-of-variables theorem trong integration và density transformation là cùng mathematical structure.

## Physics connection — scalar và vector fields

Temperature `T(x,y,z)` là scalar field; gradient chỉ direction temperature tăng nhanh nhất.

Velocity field `v(x,y,z)` là vector field; its Jacobian contains local deformation information. Divergence và curl được xây từ derivatives của vector fields và nối sang fluid dynamics, electromagnetism và vector calculus.

## AI connection — loss landscapes và backpropagation

Loss

```math
L(\theta_1,\ldots,\theta_n)
```

là scalar function trên parameter space. Gradient gives local first-order sensitivity. Hessian captures curvature but full Hessian quá lớn cho modern networks, nên algorithms dùng Hessian-vector products, approximations hoặc adaptive first-order methods.

Automatic differentiation computes exact chain-rule derivatives của implemented computation graph up to floating-point effects; nó không phải numerical finite differencing.

## Finance connection — multi-factor sensitivity

Portfolio value có thể depend on rates, FX, volatility, equity levels. Gradient vector captures first-order exposures; Hessian captures cross-effects và convexity-like second-order risks.

Nhưng local Greeks/sensitivities không thay thế scenario analysis cho large shocks, vì Taylor approximation có validity range.

## Differentiability không chỉ là “mọi partial derivative tồn tại”

Một function có thể có all partial derivatives tại point nhưng vẫn không differentiable ở đó. Differentiability yêu cầu tồn tại một single linear map approximation cho **mọi small directions đồng thời**.

Đây là lý do Jacobian/local-linear-map viewpoint mạnh hơn việc coi multivariable calculus là “take partials one by one”.

## Assumptions và failure modes

Gradient depends on coordinate scaling and metric. Rescaling a variable changes numerical gradient components dù underlying physical problem same. Optimization methods often need normalization/preconditioning.

Hessian-based classification cần smoothness và local context; positive semidefinite but not definite can be inconclusive.

Jacobian linearization chỉ accurate locally. Large perturbations require nonlinear terms or repeated re-linearization.

## Mental Model

> Multivariable calculus asks how a small vector perturbation flows through a system. Gradient is the scalar-output sensitivity vector; Jacobian is the local linear transformation for vector outputs; Hessian is the curvature operator describing how first-order sensitivity itself changes. Integration and Jacobian determinants describe how small pieces of area/volume transform and accumulate.

## Common Misconceptions

**“Gradient là chỉ hướng function lớn nhất globally.”** Nó chỉ steepest local direction under the chosen metric.

**“Có partial derivatives là differentiable.”** Không đủ; cần a coherent local linear approximation.

**“Jacobian determinant chỉ là correction factor để nhớ.”** Nó là local volume scaling của coordinate transformation.

**“Hessian positive semidefinite luôn nghĩa strict minimum.”** Không; semidefinite can be inconclusive without additional structure.

**“Backpropagation là một numerical approximation.”** Nó là chain rule/automatic differentiation trên computation graph, khác finite differences.