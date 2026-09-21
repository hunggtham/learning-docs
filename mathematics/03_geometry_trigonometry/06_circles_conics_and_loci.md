# Đường tròn, conic sections và quỹ tích: geometry của distance constraints

Quỹ tích (locus / 자취) là tập hợp mọi điểm thỏa một điều kiện. Cách nhìn này mạnh hơn việc học riêng từng phương trình circle, parabola, ellipse hay hyperbola, vì nó trả lời câu hỏi bản chất: **đường cong này tồn tại vì constraint nào?**

Một conic có thể được nhìn đồng thời theo ba lớp:

```text
geometric constraint
→ algebraic equation
→ transformed coordinate representation
```

Khi ba lớp này được nối với nhau, standard forms không còn là công thức phải ghi nhớ.

## 1. Circle: giữ một distance không đổi

Cho tâm

```math
C=(h,k)
```

và bán kính `r`. Điểm `P=(x,y)` thuộc circle khi

```math
CP=r.
```

Dùng distance formula:

```math
\sqrt{(x-h)^2+(y-k)^2}=r,
```

nên

```math
(x-h)^2+(y-k)^2=r^2.
```

Đây là phương trình đường tròn (circle / 원) vì nó chỉ encode một distance constraint.

### Worked example

Circle tâm `(2,-1)`, radius `3`:

```math
(x-2)^2+(y+1)^2=9.
```

Điểm `(5,-1)` nằm trên circle vì distance tới center bằng 3.

## 2. Level set và normal vector

Viết

```math
F(x,y)=(x-h)^2+(y-k)^2-r^2.
```

Circle là level set

```math
F(x,y)=0.
```

Gradient:

```math
\nabla F=(2(x-h),2(y-k)).
```

Gradient hướng theo radius. Vì gradient vuông góc với level curve, tangent tại một điểm trên circle vuông góc với radius.

Đây là bridge trực tiếp tới multivariable calculus: geometry của tangent/normal xuất hiện từ gradient của constraint.

## 3. Parabola: cân bằng distance tới point và line

Parabola (포물선) là locus của các điểm có distance tới focus bằng distance tới directrix.

Cho focus `(0,p)` và directrix `y=-p`. Với `P=(x,y)`:

```math
\sqrt{x^2+(y-p)^2}=|y+p|.
```

Bình phương:

```math
x^2+(y-p)^2=(y+p)^2.
```

Simplify:

```math
x^2=4py.
```

Như vậy standard form đến từ distance definition, không phải từ việc “nhớ dạng parabola”.

### Reflective property

Trong ideal geometry, ray song song với axis của parabola phản xạ qua tangent và đi qua focus. Đây là lý do parabolic reflector xuất hiện trong antenna, telescope và satellite dish.

Điểm quan trọng là application này phụ thuộc thêm physical law về reflection; geometric shape cung cấp structure, physics cung cấp mechanism.

## 4. Ellipse: tổng hai distance không đổi

Ellipse (타원) là locus của các điểm `P` sao cho

```math
PF_1+PF_2=2a.
```

Trong principal coordinates:

```math
\frac{x^2}{a^2}+\frac{y^2}{b^2}=1,
\qquad a\ge b>0.
```

Focal distance:

```math
c^2=a^2-b^2.
```

Eccentricity:

```math
e=\frac ca,
```

với

```text
circle: e=0
ellipse: 0<e<1
```

Eccentricity đo degree mà conic lệch khỏi circle-like geometry.

### Kepler connection

Trong ideal two-body model, planetary orbit là ellipse với central body ở một focus. Nhưng đây là consequence của inverse-square dynamics, không phải chỉ vì “ellipse trông giống orbit”. Geometry và physical dynamics cần được phân biệt.

## 5. Hyperbola: hiệu hai distance không đổi

Hyperbola (쌍곡선) thỏa

```math
|PF_1-PF_2|=2a.
```

Standard form:

```math
\frac{x^2}{a^2}-\frac{y^2}{b^2}=1.
```

Asymptotes:

```math
y=\pm\frac ba x.
```

Asymptote không phải một phần của hyperbola. Nó mô tả direction mà curve tiến gần khi `|x|` lớn.

### Localization example

Nếu hai sensors đo chênh lệch thời gian đến của một signal, chênh lệch distance tới hai sensors gần như cố định. Locus khả dĩ là hyperbola. Nhiều sensor pairs cho nhiều hyperbolas; intersection cho estimate source position.

Đây là ví dụ đẹp về geometry → inverse problem.

## 6. Một definition thống nhất bằng eccentricity

Một cách unified hơn dùng focus `F`, directrix `L` và eccentricity `e`:

```math
\frac{\text{distance}(P,F)}{\text{distance}(P,L)}=e.
```

Từ đó:

```text
e < 1 → ellipse
 e = 1 → parabola
 e > 1 → hyperbola
```

Circle có thể xem như limiting/special symmetric case.

Cách này cho thấy các conics không phải bốn families hoàn toàn tách rời; chúng là các regimes của cùng một distance-ratio idea.

## 7. General quadratic equation

General conic equation:

```math
Ax^2+Bxy+Cy^2+Dx+Ey+F=0.
```

Quadratic part được encode bởi symmetric matrix

```math
Q=
\begin{bmatrix}
A & B/2\\
B/2 & C
\end{bmatrix}.
```

Viết compact:

```math
x^TQx+d^Tx+F=0.
```

Đây là bridge trực tiếp từ analytic geometry sang quadratic forms trong linear algebra.

## 8. Vì sao rotation loại được cross term `xy`?

Symmetric matrix `Q` có orthogonal eigenbasis. Nếu đổi coordinates sang eigenvectors của `Q`, matrix trở thành diagonal:

```math
Q=P\Lambda P^T.
```

Trong rotated coordinates, quadratic part không còn mixed term `xy`.

Vì vậy “rotate axes to simplify conic” thực chất là **diagonalize a symmetric quadratic form**.

Đây là cùng structure xuất hiện trong PCA, covariance ellipses và Hessian analysis.

## 9. Classification bằng `B^2-4AC`

Under non-degenerate real conditions:

```text
B² - 4AC < 0 → ellipse-type
B² - 4AC = 0 → parabola-type
B² - 4AC > 0 → hyperbola-type
```

Nhưng đây không phải complete classification nếu không xét linear/constant terms và degeneracy. Equation có thể collapse thành pair of lines, a point hoặc empty set.

Rule chỉ có meaning khi assumptions được nói rõ.

## 10. Parametric, implicit và matrix representations

Một circle có implicit form:

```math
x^2+y^2=r^2.
```

Parametric form:

```math
x=r\cos t,
\qquad
y=r\sin t.
```

Implicit representation tốt cho constraints, inside/outside tests và level-set reasoning. Parametric representation tốt cho rendering, animation và path traversal.

Representation choice là một engineering decision, không chỉ notation preference.

## 11. Conics và optimization

Ellipse

```math
x^TQx\le1
```

với positive-definite `Q` mô tả an ellipsoidal feasible set.

Trong statistics, covariance matrix tạo confidence ellipses. Trong optimization, quadratic constraints/objectives tạo ellipsoidal geometry. Trong machine learning, Mahalanobis distance cũng tạo level sets dạng ellipse/ellipsoid.

## 12. Conics và second-order local models

Taylor approximation bậc hai gần critical point:

```math
f(x+\Delta)
\approx
f(x)+\frac12\Delta^TH\Delta.
```

Level sets của quadratic form `\Delta^TH\Delta` thường là ellipses/hyperbolas tùy eigenvalue signs.

Do đó conic geometry không chỉ là school geometry; nó là local geometry của multivariable functions.

## Worked example: classify và rotate intuition

Xét

```math
5x^2+4xy+2y^2=1.
```

Quadratic matrix:

```math
Q=
\begin{bmatrix}
5&2\\
2&2
\end{bmatrix}.
```

`Q` symmetric và positive definite, nên level set là ellipse. Cross term chỉ nói axes của ellipse không aligned với original coordinate axes. Eigenvectors của `Q` cho principal axes.

## Knowledge Connection

Conics nối nhiều chapter:

```text
Pythagorean distance
→ locus
→ quadratic equation
→ quadratic form
→ eigenvectors / axis rotation
→ Hessian geometry
→ covariance ellipse
→ optimization constraints
```

Trong Physics, conics xuất hiện trong orbital mechanics và optics. Trong AI/Data, ellipsoids xuất hiện trong covariance geometry và Gaussian contours. Trong Finance, quadratic risk models có level sets dạng ellipsoid khi covariance matrix positive definite.

## Mental Model

> Conic sections là geometry của distance constraints và quadratic forms. Standard equation chỉ là representation thuận tiện sau khi chọn coordinate system phù hợp.

## Common Misconceptions

Ellipse không chỉ là “circle bị kéo” về definition, dù affine transform của circle tạo ellipse. Projectile path chỉ là parabola dưới assumptions như constant gravity và negligible air resistance. `B²-4AC` không đủ để classify mọi degenerate case. Hyperbola `xy=1` vẫn là conic dù không ở standard axis-aligned form; đổi coordinates có thể làm structure rõ hơn.
