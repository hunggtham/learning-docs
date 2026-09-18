# Gradient descent, learning rate và geometry của optimization

Gradient descent (경사하강법) là iterative method dùng gradient để giảm differentiable objective. Nó là nền của training nhiều machine-learning models nhưng không phải magic rule bảo đảm global optimum trong mọi landscape.

## Derivation from local linear model

Gần `x`:

```math
f(x+\Delta)\approx f(x)+\nabla f(x)^T\Delta
```

Với step length nhỏ cố định, dot product nhỏ nhất khi `Δ` ngược direction gradient. Vì vậy chọn

```math
x_{k+1}=x_k-\eta\nabla f(x_k)
```

với learning rate `η>0`.

Gradient direction là steepest ascent theo Euclidean norm; negative gradient steepest descent local.

## Learning rate

`η` quá lớn có thể overshoot hoặc diverge. Quá nhỏ cho convergence chậm. Appropriate scale phụ thuộc curvature và conditioning.

Với quadratic

```math
f(x)=\frac12x^TAx-b^Tx
```

positive definite `A`, eigenvalues của `A` mô tả curvature theo principal directions. Large condition number tạo narrow valley; một global step size phải đủ nhỏ cho steep direction nên zig-zag/chậm ở flat direction.

## Convex functions

Nếu `f` differentiable convex:

```math
f(y)\ge f(x)+\nabla f(x)^T(y-x)
```

Tangent plane là global under-estimator. Nếu `∇f(x*)=0`, convexity cho `x*` global minimum.

Strong convexity cung cấp stronger curvature lower bound và convergence guarantees tốt hơn.

## Stochastic gradient descent

Full gradient qua toàn dataset expensive. SGD dùng gradient estimate từ one sample/minibatch:

```math
\hat g_k\approx\nabla f(x_k)
```

Noise làm path rung nhưng giảm cost mỗi update và có thể hữu ích trong large-scale training.

## Momentum

Momentum tích lũy direction updates để smooth oscillations và accelerate consistent directions. Một form:

```math
v_{k+1}=\beta v_k+g_k
```

```math
x_{k+1}=x_k-\eta v_{k+1}
```

Adam thêm adaptive scaling dựa trên moving moments của gradients. Các optimizers thay dynamics, không thay objective itself.

## Saddles và non-convex landscapes

Neural networks tạo non-convex objectives. Gradient zero có thể là saddle. High-dimensional geometry thường có nhiều saddle directions.

Practical success phụ thuộc initialization, architecture, normalization, optimization algorithm và data; không thể suy từ one-dimensional picture đơn giản.

## Regularization

Optimization objective có thể thêm penalty:

```math
L(\theta)+\lambda R(\theta)
```

L2 penalty tạo shrinkage; L1 khuyến khích sparsity. `λ` encode trade-off fit vs complexity, không phải “free accuracy”.

## Mental Model

> Gradient descent liên tục xây local linear picture và bước ngược hướng tăng mạnh nhất. Tốc độ và stability phụ thuộc geometry của surface — đặc biệt curvature, conditioning và noise — chứ không chỉ công thức update.

## Common Misconceptions

Gradient descent không đảm bảo global minimum cho arbitrary non-convex function. Learning rate lớn hơn không nghĩa học nhanh hơn. Adam/SGD là optimization methods, không tự giải quyết data leakage, bad objective hay poor model specification.

## Worked Example: learning rate trên một quadratic

Với

```math
f(x)=\frac12ax^2,
\qquad a>0
```

gradient `ax`. Update:

```math
x_{k+1}=x_k-\eta ax_k=(1-\eta a)x_k
```

Do đó

```math
x_k=(1-\eta a)^kx_0
```

Convergence về 0 cần

```math
|1-\eta a|<1
```

hay

```math
0<\eta<\frac2a
```

Nếu learning rate quá lớn, magnitude multiplier ≥1 và iterations oscillate/diverge. Formula đơn giản này cho thấy learning rate liên hệ curvature `a`, không phải một hyperparameter hoàn toàn tùy ý.

## Feature scaling connection

Nếu objective có curvature rất khác theo axes, gradient descent đi zig-zag. Standardizing features hoặc preconditioning thay geometry để directions có comparable scale, thường giúp optimization. Vì vậy data scaling có tác động toán học lên landscape, không chỉ cosmetic preprocessing.
