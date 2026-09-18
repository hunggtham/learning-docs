# Đường tròn, conic sections và quỹ tích

Một cách mạnh để hiểu geometry là không bắt đầu từ hình vẽ mà từ **quỹ tích (Locus / 자취)**: tập hợp tất cả các điểm thỏa một điều kiện. Khi condition là distance tới một point, line hoặc pair of points, các đường cong quen thuộc như circle, parabola, ellipse và hyperbola xuất hiện tự nhiên.

## Circle là tập điểm cách tâm một khoảng không đổi

Cho center

```math
C=(h,k)
```

và radius `r`. Một point `P=(x,y)` nằm trên circle khi

```math
CP=r.
```

Dùng distance formula:

```math
\sqrt{(x-h)^2+(y-k)^2}=r.
```

Bình phương hai vế:

```math
(x-h)^2+(y-k)^2=r^2.
```

Phương trình circle không phải một formula tùy ý; nó chỉ là Pythagorean distance viết thành constraint.

## Tangent và radius

Tangent tại một point trên circle vuông góc với radius đi qua point đó. Có thể hiểu qua optimization: tangent direction là direction mà first-order change của distance-squared constraint bằng zero.

Đặt

```math
F(x,y)=(x-h)^2+(y-k)^2-r^2.
```

Gradient

```math
\nabla F=(2(x-h),2(y-k))
```

hướng theo radius và vuông góc với level curve `F=0`. Đây là bridge tự nhiên sang multivariable calculus.

## Parabola: cùng khoảng cách tới focus và directrix

Parabola (Parabola / 포물선) là locus của points có distance tới một focus bằng distance tới một directrix.

Cho focus `(0,p)` và directrix `y=-p`. Với point `(x,y)`:

```math
\sqrt{x^2+(y-p)^2}=|y+p|.
```

Bình phương và simplify:

```math
x^2+(y-p)^2=(y+p)^2
```

```math
x^2=4py.
```

Standard equation xuất hiện từ distance definition. Reflective property của parabola giải thích vì sao parabolic antennas và reflectors có thể tập trung parallel rays vào focus trong ideal geometric model.

## Ellipse: tổng khoảng cách tới hai foci không đổi

Ellipse (Ellipse / 타원) là locus của points `P` sao cho

```math
PF_1+PF_2=2a.
```

Trong coordinate system phù hợp, standard form là

```math
\frac{x^2}{a^2}+\frac{y^2}{b^2}=1,
\qquad a>b>0.
```

Focal distance `c` thỏa

```math
c^2=a^2-b^2.
```

Quantity

```math
e=\frac ca
```

gọi là eccentricity. Circle là special case `e=0`; ellipse có `0<e<1`.

Planetary orbit trong Kepler idealization là ellipse với central body ở một focus, không phải ở geometric center. Đây là một example quan trọng về việc geometric parameter có physical meaning khi model assumptions thích hợp.

## Hyperbola: hiệu khoảng cách không đổi

Hyperbola (Hyperbola / 쌍곡선) thỏa

```math
|PF_1-PF_2|=2a.
```

Standard form:

```math
\frac{x^2}{a^2}-\frac{y^2}{b^2}=1.
```

Nó có asymptotes

```math
y=\pm\frac ba x.
```

Hyperbolic geometry xuất hiện trong localization problems dựa trên difference of arrival times: difference khoảng cách tới hai sensors tạo một hyperbola. Nhiều sensor pairs intersect để estimate source position.

## Conic sections từ một unified quadratic equation

General second-degree equation

```math
Ax^2+Bxy+Cy^2+Dx+Ey+F=0
```

có thể represent conics tùy coefficients và non-degeneracy conditions. Rotation/translation coordinates có thể loại cross terms hoặc recenter equation.

Discriminant-like quantity

```math
B^2-4AC
```

help classify: negative thường ellipse-type, zero parabola-type, positive hyperbola-type, dưới assumptions thích hợp.

Deep connection ở đây là quadratic forms. Matrix

```math
Q=
\begin{bmatrix}
A&B/2\\
B/2&C
\end{bmatrix}
```

encode quadratic part. Eigenvectors của `Q` cho principal axes. Vì vậy việc “xoay trục để bỏ `xy`” thực chất là diagonalization của symmetric matrix.

## Bézier và conic thinking trong graphics

Computer graphics không chỉ dùng conics; curves thường được represent parametrically. Nhưng circle/ellipse vẫn là primitive quan trọng trong vector graphics và CAD. Một lesson rộng hơn là lựa chọn representation: implicit form tốt cho inside/outside tests và constraints; parametric form tốt để generate points theo path.

## Knowledge Connection

Conics nối Pythagorean distance với algebra, optimization và linear algebra. Circle là level set; gradient cho normal. General conic là quadratic form; coordinate rotation là eigenbasis change. Parabola nối tới projectile path trong ideal constant-gravity model, dù physical derivation của projectile là từ kinematics chứ không phải focus/directrix definition.

## Mental Model

> Conic sections là geometry của distance constraints. Circle giữ một distance; parabola cân hai loại distance; ellipse giữ tổng; hyperbola giữ hiệu. Standard equations chỉ là các distance rules sau khi chọn coordinate system thuận tiện.

## Common Misconceptions

Projectile path là parabola chỉ dưới assumptions như constant gravity và bỏ air resistance. Ellipse không phải “circle bị kéo” về mặt definition, dù affine scaling circle tạo ellipse. Hyperbola graph `y=1/x` có hyperbolic shape nhưng không nên đồng nhất mọi rational curve với geometric hyperbola mà không xét equation/coordinate transform.
