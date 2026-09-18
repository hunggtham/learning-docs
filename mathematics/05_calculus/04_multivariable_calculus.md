# Giải tích nhiều biến: gradient, Jacobian và Hessian

Real systems thường có nhiều inputs. Loss của neural network phụ thuộc hàng triệu parameters; temperature phụ thuộc coordinates; business profit phụ thuộc price, demand, cost. Multivariable calculus mở rộng local change từ một direction sang nhiều directions.

## Partial derivative

Với

```math
f(x,y)
```

partial derivative theo `x` giữ `y` fixed:

```math
\frac{\partial f}{\partial x}
```

và vice versa.

Ví dụ

```math
f(x,y)=x^2y+3y
```

thì

```math
f_x=2xy
```

```math
f_y=x^2+3
```

Mỗi partial là sensitivity theo một coordinate direction.

## Gradient

Gradient:

```math
\nabla f=
\begin{bmatrix}
\partial f/\partial x_1\\
\vdots\\
\partial f/\partial x_n
\end{bmatrix}
```

chỉ direction steepest increase local; negative gradient steepest decrease trong Euclidean metric.

Directional derivative theo unit vector `u`:

```math
D_uf=\nabla f\cdot u
```

Dot product projects gradient onto requested direction.

## Level sets

Level set `f(x,y)=c` là contour. Gradient perpendicular với level set (khi gradient nonzero). Vì movement tangent không đổi `f` first-order, directional derivative tangent bằng zero, nên tangent orthogonal gradient.

Đây là nền của Lagrange multipliers.

## Jacobian

Nếu vector-valued function

```math
F:\mathbb R^n\to\mathbb R^m
```

Jacobian matrix:

```math
J_{ij}=\frac{\partial F_i}{\partial x_j}
```

là best local linear transformation:

```math
F(x+\Delta x)\approx F(x)+J(x)\Delta x
```

Derivative một biến là scalar; gradient/Jacobian là higher-dimensional versions của local linearization.

## Chain rule dạng matrix

Nếu `F=G∘H`, local linear maps compose:

```math
J_F=J_GJ_H
```

Backpropagation là efficient repeated multiplication/application của these local derivatives theo computational graph.

## Hessian

Hessian của scalar function:

```math
H_{ij}=\frac{\partial^2f}{\partial x_i\partial x_j}
```

capture local curvature. Near point:

```math
f(x+\Delta)
\approx f(x)+\nabla f^T\Delta+\frac12\Delta^TH\Delta
```

Gradient là first-order slope; Hessian second-order shape.

## Multiple integrals

Double integral:

```math
\iint_R f(x,y)dA
```

accumulates density over area. Triple integral over volume. Change of variables introduces Jacobian determinant vì coordinate transformation scale local area/volume.

Polar coordinates:

```math
dA=r\,dr\,d\theta
```

factor `r` chính là local area scaling.

## Mental Model

> Multivariable derivative không chỉ là nhiều slopes. Nó là local linear map. Gradient là derivative của scalar output; Jacobian của vector output; Hessian mô tả cách local linear behavior itself thay đổi.

## Common Misconceptions

Gradient phụ thuộc metric/coordinate interpretation. Partial derivatives tồn tại không luôn đủ để guarantee differentiability. Hessian positive definite tại critical point cho strict local minimum under suitable smoothness, nhưng không tự động global minimum.
