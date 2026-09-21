# Hình học tọa độ: từ không gian hình học đến representation bằng số

Hình học tọa độ (analytic geometry / 해석기하학) không đơn giản là “hình học có công thức”. Ý tưởng cốt lõi là chọn một hệ tọa độ để **mã hóa vị trí bằng numbers**, rồi dùng algebra xử lý những câu hỏi vốn mang tính geometric.

Điểm quan trọng là phải phân biệt:

> geometric object là object; coordinates chỉ là representation của object trong một frame đã chọn.

Một point ngoài đời không thay đổi khi ta đổi origin, xoay axes hay chuyển từ world coordinates sang camera coordinates. Chỉ description bằng số thay đổi.

## 1. Vì sao coordinates hữu ích?

Không dùng coordinates, ta có thể nói hai đoạn thẳng bằng nhau, hai góc vuông hay một point nằm trên circle. Nhưng khi gán point thành

```math
P=(x,y),
```

những quan hệ đó trở thành equations có thể tính, solve và generalize.

Ví dụ, “P cách origin đúng 5 units” trở thành

```math
x^2+y^2=25.
```

Geometry được chuyển thành algebra mà không mất meaning hình học.

## 2. Cartesian coordinates là một choice, không phải truth tuyệt đối

Trong 2D, Cartesian system dùng hai perpendicular axes. Một point được represent bởi ordered pair

```math
(x,y).
```

`x` và `y` là signed displacements theo chosen basis directions.

Trong 3D:

```math
(x,y,z).
```

Trong `n` dimensions:

```math
(x_1,\ldots,x_n).
```

Ta không cần visualize `n=1000`; algebra của coordinates vẫn hoạt động.

Điều này mở đường từ geometry sang vectors, feature spaces và state spaces.

## 3. Point và vector: cùng numbers, khác concept

Point `P=(3,4)` là một **location** trong chosen coordinate system.

Vector

```math
v=(3,4)
```

có thể là displacement từ một point tới point khác.

Nếu

```math
P=(1,2),\qquad Q=(4,6),
```

thì displacement

```math
Q-P=(3,4).
```

Ta có thể cộng vector vào point:

```math
P+v=Q.
```

Nhưng “cộng hai points” không luôn có geometric meaning độc lập với chosen origin. Phân biệt point/vector trở nên quan trọng trong affine geometry, graphics và robotics.

## 4. Distance formula đến từ orthogonal decomposition

Giữa

```math
P=(x_1,y_1)
```

và

```math
Q=(x_2,y_2),
```

difference vector là

```math
\Delta=(x_2-x_1,\ y_2-y_1).
```

Hai coordinate directions vuông góc, nên Pythagoras cho

```math
d(P,Q)^2
=(x_2-x_1)^2+(y_2-y_1)^2.
```

Do đó

```math
d(P,Q)
=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}.
```

Trong `n` dimensions:

```math
d(x,y)=\sqrt{\sum_{i=1}^{n}(x_i-y_i)^2}.
```

Đây chính là Euclidean norm của difference vector.

### Assumption quan trọng

Formula trên assume coordinate axes là orthonormal trong Euclidean geometry. Nếu coordinates không orthogonal, hoặc geometry không Euclidean, metric formula thay đổi.

## 5. Midpoint và affine combinations

Midpoint giữa `P` và `Q` là

```math
M=\frac{P+Q}{2}.
```

Trong coordinates:

```math
M=
\left(
\frac{x_1+x_2}{2},
\frac{y_1+y_2}{2}
\right).
```

Cách derive sâu hơn dùng parameterized segment:

```math
L(t)=P+t(Q-P),\qquad 0\le t\le1.
```

`t=0` cho `P`, `t=1` cho `Q`, còn `t=1/2` cho midpoint.

Expression

```math
(1-t)P+tQ
```

là affine combination. Đây là nền của interpolation trong graphics, animation và geometry processing.

## 6. Slope là ratio của directional change

Với hai points,

```math
m=\frac{\Delta y}{\Delta x}
```

nếu `\Delta x\ne0`.

Slope không phải property “magic” của line; nó là ratio giữa hai components của direction vector.

Nếu direction vector là

```math
v=(a,b),
```

thì

```math
m=\frac ba
```

khi `a\ne0`.

Vertical line có `a=0`; slope representation `b/a` undefined, nhưng direction vector vẫn hoàn toàn hợp lệ.

Điều này cho thấy vector representation tổng quát hơn slope.

## 7. Equation của line từ hai viewpoints

### Direction viewpoint

Line qua `P` với direction `v`:

```math
L(t)=P+tv.
```

Đây là parametric form.

### Normal-vector viewpoint

Nếu `n=(A,B)` vuông góc line, thì mọi point `x=(x,y)` trên line thỏa

```math
n\cdot(x-P)=0.
```

Khai triển cho

```math
Ax+By+C=0.
```

General form mạnh vì vertical lines không cần special case.

Direction form và normal form là hai representations của cùng line.

## 8. Distance từ point tới line là projection

Line

```math
Ax+By+C=0
```

có normal vector

```math
n=(A,B).
```

Với point `P=(x_0,y_0)`, signed distance theo normal direction tỷ lệ với

```math
Ax_0+By_0+C.
```

Normalize bởi length của normal:

```math
d=
\frac{|Ax_0+By_0+C|}{\sqrt{A^2+B^2}}.
```

Đây không phải formula tách rời. Nó là projection của displacement lên unit normal.

Nó nối coordinate geometry trực tiếp với dot product và projection trong linear algebra.

## 9. Circle là locus từ distance constraint

Circle center `C=(h,k)` radius `r` được định nghĩa là set points `P=(x,y)` sao cho

```math
d(P,C)=r.
```

Square hai phía:

```math
(x-h)^2+(y-k)^2=r^2.
```

Equation đến trực tiếp từ geometric definition. Nếu nhớ definition, không cần học thuộc formula như một object riêng.

## 10. Conics là distance relationships

Coordinate equations của conics có meaning hình học.

**Parabola:** points equidistant từ focus và directrix.

**Ellipse:** sum distances tới hai foci là constant.

**Hyperbola:** absolute difference distances tới hai foci là constant.

Các standard equations xuất hiện sau khi chọn coordinates phù hợp với symmetry của object.

Đây là lesson quan trọng: chọn coordinate system tốt có thể làm equation đơn giản mạnh.

## 11. Rotation và change of coordinates

Giả sử point có coordinates `x` trong basis cũ. Khi basis thay đổi, coordinates mới có thể khác dù geometric point không đổi.

Trong 2D, rotation matrix

```math
R(\theta)=
\begin{bmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{bmatrix}
```

có thể dùng để rotate vector hoặc đổi representation tùy convention active/passive.

Hai operations dùng same matrix structure nhưng interpretation khác. Vì vậy trong graphics/robotics cần luôn rõ: ta đang move object hay đổi frame?

## 12. Worked example: intersection của line và circle

Circle:

```math
x^2+y^2=25.
```

Line:

```math
y=3.
```

Substitute:

```math
x^2+9=25
```

```math
x^2=16
```

nên

```math
x=\pm4.
```

Intersection points:

```math
(4,3),\qquad(-4,3).
```

Algebra giải system; geometry nói line cắt circle tại hai points. Discriminant của resulting quadratic encode số intersections.

## 13. Coordinate geometry trong Computer Graphics

Graphics thường có nhiều coordinate systems:

```text
model/local
→ world
→ view/camera
→ clip
→ normalized device
→ screen
```

Một vertex vật lý được transform qua pipeline matrices. Bug thường không đến từ matrix multiplication sai syntax, mà từ nhầm frame, multiplication order hoặc handedness convention.

Coordinate geometry vì vậy là prerequisite thực tế của 2D/3D graphics.

## 14. Robotics và localization

Robot có thể cần biết:

- point trong robot frame;
- point trong world frame;
- sensor measurement trong camera/LiDAR frame.

Transformation giữa frames thường dùng rotation + translation.

Cùng một obstacle có coordinates khác nhau trong mỗi frame. Điều quan trọng là relationship giữa frames, không phải một coordinate tuple duy nhất.

## 15. AI/Data: coordinates không tự động có metric meaning

Feature vector cũng là coordinate representation.

Nếu feature 1 là age `0–100`, feature 2 là income `0–100000000`, Euclidean distance trên raw coordinates sẽ bị income dominate.

Do đó metric meaningful phụ thuộc:

- scaling;
- units;
- feature semantics;
- covariance structure;
- representation learned bởi model.

Có coordinates không có nghĩa Euclidean geometry là model đúng.

## 16. Geographic coordinates: counterexample quan trọng

Latitude/longitude là coordinates trên curved Earth surface. Nếu lấy degree differences rồi dùng flat Euclidean distance cho points xa nhau, model geometry sai.

Ta cần spherical/ellipsoidal distance hoặc suitable projection.

Đây là example rõ:

> representation bằng numbers không quyết định geometry; metric assumptions mới quyết định distance.

## 17. Finance: state spaces và coordinate choice

Một portfolio có thể được represent bằng holdings vector, factor exposures hoặc principal components. Cùng economic position có nhiều coordinate systems.

Trong risk modeling, đổi từ asset coordinates sang factor coordinates có thể làm covariance structure dễ hiểu hơn — tương tự đổi basis trong linear algebra.

## Mental Model

> Coordinate geometry là nghệ thuật chọn một numerical representation cho space. Point, line, circle và distance không sinh ra từ coordinates; coordinates chỉ làm các relationships đó trở thành equations. Đổi coordinate system có thể đổi numbers mạnh nhưng không đổi geometric object.

## Common Misconceptions

**Coordinates là object.** Không; chúng phụ thuộc frame/basis.

**Slope undefined nghĩa vertical line không có direction.** Không; chỉ slope ratio representation bị singular.

**Euclidean distance dùng được cho mọi numerical data.** Không; metric phải match geometry/semantics.

**Rotation matrix luôn nghĩa rotate object.** Cùng matrix structure còn có thể represent change of coordinates; convention cần được nói rõ.
