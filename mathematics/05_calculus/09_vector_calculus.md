# Vector calculus: gradient, divergence, curl và field integrals

Multivariable calculus nghiên cứu functions nhiều biến; vector calculus đi thêm một bước bằng cách nghiên cứu scalar fields và vector fields trải trên space. Đây là ngôn ngữ của fluid flow, electromagnetism, heat, gradients và conservation laws.

## Scalar field và vector field

Scalar field gán một scalar cho mỗi point:

```math
T(x,y,z)
```

có thể là temperature field.

Vector field gán vector cho mỗi point:

```math
F(x,y,z)
=
(P,Q,R)
```

có thể là velocity field của fluid hoặc force field.

## Gradient

Với scalar field `f`:

```math
\nabla f
=
\begin{bmatrix}
f_x\\f_y\\f_z
\end{bmatrix}.
```

Gradient chỉ direction steepest increase và magnitude là maximum directional derivative local.

Nếu move theo unit vector `u`, change rate:

```math
D_uf=\nabla f\cdot u.
```

Gradient perpendicular với level surfaces `f=constant`, vì movement tangent level surface không đổi `f` first-order.

## Divergence

Với

```math
F=(P,Q,R),
```

divergence:

```math
\nabla\cdot F
=
\frac{\partial P}{\partial x}
+
\frac{\partial Q}{\partial y}
+
\frac{\partial R}{\partial z}.
```

Trực giác: local net outflow density. Positive divergence giống source; negative giống sink.

Nếu fluid incompressible với velocity field `v`, một common condition:

```math
\nabla\cdot v=0.
```

Nhưng zero divergence không có nghĩa field zero; chỉ local net expansion/compression zero.

## Curl

Curl:

```math
\nabla\times F
```

đo local rotational tendency. Trong 3D:

```math
\nabla\times F
=
\begin{bmatrix}
R_y-Q_z\\
P_z-R_x\\
Q_x-P_y
\end{bmatrix}.
```

Paddle-wheel intuition: đặt tiny wheel trong flow; curl liên quan axis và tendency nó spin.

## Conservative fields và potential

Nếu

```math
F=\nabla\phi
```

cho scalar potential `φ`, field gọi conservative. Line integral giữa two points không phụ thuộc path trong suitable simply-connected domain:

```math
\int_C F\cdot dr
=
\phi(B)-\phi(A).
```

Và

```math
\nabla\times(\nabla\phi)=0.
```

Reverse implication cần domain conditions; holes có thể phá global potential dù local curl zero.

## Line integral

Với curve `r(t)`, line integral của vector field:

```math
\int_C F\cdot dr
=
\int_a^b
F(r(t))\cdot r'(t)dt.
```

Trong mechanics, đây là work của force field along path.

Dot product chỉ lấy component force theo motion direction.

## Flux và surface integral

Flux qua surface `S`:

```math
\iint_S F\cdot n\,dS
```

đo amount of field passing through surface. `n` là unit normal; dot product chọn normal component.

## Divergence theorem

Divergence theorem:

```math
\iiint_V \nabla\cdot F\,dV
=
\iint_{\partial V}F\cdot n\,dS.
```

Total sources/sinks bên trong volume bằng net outward flow xuyên boundary. Đây là conservation principle cực kỳ sâu: what is created inside must account for what exits boundary.

## Stokes' theorem

Stokes' theorem nối curl trên surface với circulation quanh boundary:

```math
\iint_S (\nabla\times F)\cdot n\,dS
=
\oint_{\partial S}F\cdot dr.
```

Nó tổng quát Green's theorem và liên hệ local rotation với global circulation.

## Một pattern thống nhất: derivative inside ↔ integral on boundary

Fundamental Theorem of Calculus:

```math
\int_a^b f'(x)dx=f(b)-f(a).
```

Divergence theorem và Stokes theorem có cùng structure: integrate derivative-like quantity over region ↔ integrate original field over boundary.

Đây là một trong những unifying ideas sâu nhất của calculus.

## Knowledge Connection

Gradient là nền của optimization và backpropagation. Divergence/curl xuất hiện trong fluid dynamics và Maxwell equations. Line/surface integrals dùng trong mechanics và electromagnetism. Trong differential geometry, các theorems này được thống nhất hơn nữa bởi generalized Stokes theorem.

## Mental Model

> Gradient hỏi scalar field dốc về đâu; divergence hỏi field đang phình ra hay co vào; curl hỏi field đang xoáy thế nào. Integral gom local behavior thành global effect, và các integral theorems nói global boundary behavior được quyết định bởi local derivatives bên trong.

## Common Misconceptions

Gradient là vector dù function output là scalar. Divergence không phải magnitude của field; constant uniform field có divergence 0. Curl 0 không luôn đảm bảo global conservative behavior nếu domain có holes. Flux phụ thuộc orientation của normal; đổi orientation đổi dấu.
