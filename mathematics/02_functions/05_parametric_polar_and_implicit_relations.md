# Quan hệ ẩn, tham số và tọa độ cực

Không phải mọi geometric object hoặc process được mô tả tốt bằng dạng `y=f(x)`. Một circle chẳng hạn thất bại vertical-line test nếu cố coi toàn bộ circle là một single-valued function của `x`. Điều đó không có nghĩa circle “không thể dùng toán”; chỉ có nghĩa representation `y=f(x)` không phù hợp.

## Implicit relation

Thay vì isolate output, ta có thể viết relation:

```math
F(x,y)=0.
```

Circle tâm origin radius `r`:

```math
x^2+y^2-r^2=0.
```

Equation này mô tả constraint giữa coordinates mà không chọn `x` hay `y` làm privileged input.

Implicit representation hữu ích khi object có symmetry hoặc khi solving explicitly tạo nhiều branches.

## Implicit differentiation

Nếu `F(x,y)=0` và locally `y` có thể được xem như function của `x`, differentiate theo `x`:

```math
F_x+F_y\frac{dy}{dx}=0.
```

Nếu `F_y\neq0`,

```math
\frac{dy}{dx}=-\frac{F_x}{F_y}.
```

Với circle:

```math
2x+2y\frac{dy}{dx}=0,
```

nên

```math
\frac{dy}{dx}=-\frac{x}{y}.
```

Điều kiện `F_y\neq0` nhắc ta rằng representation local `y(x)` có thể breakdown tại vertical tangents.

## Parametric representation

Một curve có thể được sinh bằng parameter `t`:

```math
x=x(t),\qquad y=y(t).
```

Circle có representation tự nhiên:

```math
x=r\cos t,
```

```math
y=r\sin t.
```

Khi `t` chạy từ `0` tới `2\pi`, point đi một vòng circle.

Parameter không nhất thiết là time, nhưng trong motion problems nó thường là time. Khi đó derivative vector

```math
\frac{dr}{dt}
=
\begin{bmatrix}
x'(t)\\y'(t)
\end{bmatrix}
```

là velocity.

Nếu `x'(t)\neq0`, slope của curve là

```math
\frac{dy}{dx}=\frac{dy/dt}{dx/dt}.
```

Đây là chain rule dưới representation tham số.

## Arc length

Trong một small time `dt`, displacement xấp xỉ

```math
ds\approx\sqrt{(dx)^2+(dy)^2}.
```

Với `dx=x'(t)dt`, `dy=y'(t)dt`:

```math
ds\approx\sqrt{x'(t)^2+y'(t)^2}\,dt.
```

Do đó length từ `t=a` tới `b`:

```math
L=\int_a^b\sqrt{x'(t)^2+y'(t)^2}\,dt.
```

Pythagoras + calculus tạo formula này; không cần xem nó như rule độc lập.

## Polar coordinates

Cartesian coordinates mô tả point bằng horizontal/vertical components `(x,y)`. Polar coordinates (극좌표) dùng distance tới origin và angle:

```math
(r,\theta).
```

Conversion:

```math
x=r\cos\theta,
```

```math
y=r\sin\theta.
```

và

```math
r^2=x^2+y^2.
```

Polar representation tự nhiên cho rotational symmetry. Circle tâm origin chỉ là

```math
r=R.
```

thay vì quadratic equation.

## Area element trong polar coordinates

Một tiny polar cell có radial thickness `dr` và angular width `d\theta`. Arc length theo angular direction xấp xỉ

```math
r\,d\theta.
```

Nên area element:

```math
dA=r\,dr\,d\theta.
```

Factor `r` là Jacobian determinant của coordinate transformation. Xa origin, cùng angular change quét arc dài hơn.

## Khi nào representation tốt thay đổi bài toán

Một circle trong Cartesian là quadratic constraint; trong polar là constant radius. Một line qua origin trong polar là constant angle. Spiral có thể rất đơn giản:

```math
r=a\theta.
```

Trong graphics, robotics và navigation, chọn coordinate frame phù hợp có thể biến complicated equations thành simple ones.

## Knowledge Connection

Parametric curves nối functions với motion và vector calculus. Implicit equations nối constraints với level sets/gradients. Polar coordinates nối trigonometry với Jacobian/change of variables. Computer graphics dùng parametric curves cho Bézier/splines; robotics dùng multiple coordinate systems và transformations liên tục.

## Mental Model

> Một object toán học không bị ràng buộc vào một representation. `y=f(x)`, implicit equation, parametric curve và polar coordinates có thể mô tả cùng geometry từ các viewpoints khác nhau. Chọn representation làm structure quan trọng trở nên đơn giản nhất.

## Common Misconceptions

Parameter `t` không nhất thiết là x-coordinate hay time. Polar coordinates không unique: `(r,\theta)` và `(r,\theta+2k\pi)` cùng point, và negative `r` có thể được reinterpreted bằng angle shift. `dy/dx=(dy/dt)/(dx/dt)` cần chú ý khi `dx/dt=0`.

## Liên kết kiến thức

Nên đọc sau [Function Concept](./00_function_concept.md), [Coordinate Geometry](../03_geometry_trigonometry/01_coordinate_geometry.md) và [Trigonometry](../03_geometry_trigonometry/04_trigonometry.md). Formula arc length và implicit differentiation dùng trực tiếp [Derivatives](../05_calculus/01_derivatives.md) và [Integrals](../05_calculus/03_integrals_and_accumulation.md).

Khi chuyển sang nhiều chiều, cùng ý tưởng representation/coordinate change phát triển thành [Multivariable Calculus](../05_calculus/04_multivariable_calculus.md), [Vector Calculus](../05_calculus/09_vector_calculus.md) và [Matrix Calculus/Jacobian](../04_vectors_linear_algebra/09_matrix_calculus_jacobian_hessian_and_autodiff.md). Geometry của implicit conics được đào sâu trong [Circles, Conics and Loci](../03_geometry_trigonometry/06_circles_conics_and_loci.md).
