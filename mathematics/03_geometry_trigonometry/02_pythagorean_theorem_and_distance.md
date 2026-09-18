# Định lý Pythagoras và ý tưởng khoảng cách

Định lý Pythagoras (Pythagorean theorem / 피타고라스 정리) nói trong right triangle với legs `a,b` và hypotenuse `c`:

```math
c^2=a^2+b^2
```

Điểm quan trọng không chỉ là formula tính cạnh. Nó encode geometry của perpendicular directions và trở thành nền của Euclidean distance, vector norm và least squares.

## Vì sao bình phương xuất hiện?

Một proof hình học dùng area. Xét square lớn cạnh `a+b`, chứa bốn right triangles giống nhau và một square trung tâm cạnh `c`.

Area theo whole square:

```math
(a+b)^2
```

Area theo decomposition:

```math
4\left(\frac12ab\right)+c^2=2ab+c^2
```

Equate:

```math
a^2+2ab+b^2=2ab+c^2
```

nên

```math
a^2+b^2=c^2
```

Squares xuất hiện vì proof so sánh areas; sâu hơn, squared length là additive cho orthogonal components trong Euclidean inner-product geometry.

## Converse

Nếu ba positive lengths thỏa

```math
a^2+b^2=c^2
```

thì triangle có angle đối diện `c` là right angle. Vì vậy relation không chỉ consequence của right triangle; nó characterize rightness.

## Distance trong coordinate plane

Difference vector giữa hai points có orthogonal components `Δx,Δy`. Pythagorean theorem cho

```math
d^2=(\Delta x)^2+(\Delta y)^2
```

nên

```math
d=\sqrt{(\Delta x)^2+(\Delta y)^2}
```

Trong 3D thêm `(Δz)^2`; trong n-dimensional Euclidean space sum tất cả squared coordinate differences.

## Norm và inner product

Vector length:

```math
\|\mathbf v\|_2=\sqrt{v_1^2+\cdots+v_n^2}
```

được gọi L2 norm. Nếu vectors orthogonal `u·v=0`, thì

```math
\|u+v\|^2=\|u\|^2+\|v\|^2.
```

Đây chính là Pythagoras generalized.

## ML distance

Feature vectors có thể dùng Euclidean distance, nhưng scale của features quan trọng. Nếu age range 0–100 còn income range 0–1,000,000, income dominate distance trừ khi normalize/standardize hoặc chọn metric khác.

Do đó “distance” luôn gắn với representation và metric assumptions.

## Screen distance và game development

Khoảng cách 2D để collision/radius check thường:

```math
\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}
```

Nếu chỉ compare với radius `r`, có thể tránh square root:

```math
(\Delta x)^2+(\Delta y)^2\le r^2
```

vì square root monotonic với non-negative values. Đây là example algebraic reasoning dẫn tới computational optimization nhỏ nhưng phổ biến.

## Mental Model

> Pythagoras nói năng lượng hình học của các directions vuông góc cộng theo bình phương. Euclidean distance chỉ là Pythagoras applied cho coordinate differences; vector norm và least squares là các extensions của cùng idea.

## Common Misconceptions

Formula chỉ áp trực tiếp cho right triangle/orthogonal components trong Euclidean geometry. Euclidean distance không luôn là metric phù hợp cho data. Bình phương distance đôi khi đủ cho comparison và tránh unnecessary square root.
