# Hình học tọa độ: từ không gian hình học đến biểu diễn (representation / 표현) bằng số

> **Mạch đọc:** Đọc **Hình học tọa độ: từ không gian hình học đến biểu diễn (representation / 표현) bằng số** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Vì sao coordinates hữu ích?** sang **2. Cartesian coordinates là một choice, không phải truth tuyệt đối**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Hình học tọa độ (analytic geometry / 해석기하학) không đơn giản là “hình học có công thức”. Ý tưởng cốt lõi là chọn một hệ tọa độ để **mã hóa vị trí bằng numbers**, rồi dùng algebra xử lý những câu hỏi vốn mang tính geometric.

Điểm quan trọng là phải phân biệt:

> geometric đối tượng (object / 객체) là đối tượng (object / 객체); coordinates chỉ là biểu diễn (representation / 표현) của đối tượng (object / 객체) trong một frame đã chọn.

Một điểm (point / 지점) ngoài đời không thay đổi khi ta đổi origin, xoay axes hay chuyển từ world coordinates sang camera coordinates. Chỉ description bằng số thay đổi.

## 1. Vì sao coordinates hữu ích?

Không dùng coordinates, ta có thể nói hai đoạn thẳng bằng nhau, hai góc vuông hay một điểm (point / 지점) nằm trên circle. Nhưng khi gán điểm (point / 지점) thành

```math
P=(x,y),
```

những quan hệ đó trở thành equations có thể tính, solve và generalize.

Ví dụ, “P cách origin đúng 5 units” trở thành

```math
x^2+y^2=25.
```

Hình học (geometry / 기하학) được chuyển thành algebra mà không mất meaning hình học.

## 2. Cartesian coordinates là một choice, không phải truth tuyệt đối

Trong 2D, Cartesian hệ thống (system / 시스템) dùng hai perpendicular axes. Một điểm (point / 지점) được represent bởi ordered pair

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

Điều này mở đường từ hình học (geometry / 기하학) sang vectors, tính năng (feature / 기능) spaces và trạng thái (state / 상태) spaces.

## 3. điểm (point / 지점) và véc-tơ (vector / 벡터): cùng numbers, khác concept

Điểm (point / 지점) `P=(3,4)` là một **location** trong chosen coordinate hệ thống (system / 시스템).

Véc-tơ (vector / 벡터)

```math
v=(3,4)
```

có thể là displacement từ một điểm (point / 지점) tới điểm (point / 지점) khác.

Nếu

```math
P=(1,2),\qquad Q=(4,6),
```

thì displacement

```math
Q-P=(3,4).
```

Ta có thể cộng véc-tơ (vector / 벡터) vào điểm (point / 지점):

```math
P+v=Q.
```

Nhưng “cộng hai points” không luôn có geometric meaning độc lập với chosen origin. Phân biệt điểm (point / 지점)/véc-tơ (vector / 벡터) trở nên quan trọng trong affine hình học (geometry / 기하학), graphics và robotics.

## 4. Distance formula đến từ orthogonal decomposition

Giữa

```math
P=(x_1,y_1)
```

và

```math
Q=(x_2,y_2),
```

difference véc-tơ (vector / 벡터) là

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

Đây chính là Euclidean norm của difference véc-tơ (vector / 벡터).

### Giả định (assumption / 가정) quan trọng

Formula trên assume coordinate axes là orthonormal trong Euclidean hình học (geometry / 기하학). Nếu coordinates không orthogonal, hoặc hình học (geometry / 기하학) không Euclidean, chỉ số (metric / 지표) formula thay đổi.

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

là affine combination. Đây là nền của interpolation trong graphics, animation và hình học (geometry / 기하학) processing.

## 6. Slope là ratio của directional thay đổi (change / 변경)

Với hai points,

```math
m=\frac{\Delta y}{\Delta x}
```

nếu `\Delta x\ne0`.

Slope không phải thuộc tính (property / 속성) “magic” của line; nó là ratio giữa hai components của direction véc-tơ (vector / 벡터).

Nếu direction véc-tơ (vector / 벡터) là

```math
v=(a,b),
```

thì

```math
m=\frac ba
```

khi `a\ne0`.

Vertical line có `a=0`; slope biểu diễn (representation / 표현) `b/a` undefined, nhưng direction véc-tơ (vector / 벡터) vẫn hoàn toàn hợp lệ.

Điều này cho thấy véc-tơ (vector / 벡터) biểu diễn (representation / 표현) tổng quát hơn slope.

## 7. Equation của line từ hai viewpoints

### Direction viewpoint

Line qua `P` với direction `v`:

```math
L(t)=P+tv.
```

Đây là parametric form.

### Normal-vector viewpoint

Nếu `n=(A,B)` vuông góc line, thì mọi điểm (point / 지점) `x=(x,y)` trên line thỏa

```math
n\cdot(x-P)=0.
```

Khai triển cho

```math
Ax+By+C=0.
```

General form mạnh vì vertical lines không cần special trường hợp (case / 사례).

Direction form và normal form là hai representations của cùng line.

## 8. Distance từ điểm (point / 지점) tới line là projection

Line

```math
Ax+By+C=0
```

có normal véc-tơ (vector / 벡터)

```math
n=(A,B).
```

Với điểm (point / 지점) `P=(x_0,y_0)`, signed distance theo normal direction tỷ lệ với

```math
Ax_0+By_0+C.
```

Normalize bởi length của normal:

```math
d=
\frac{|Ax_0+By_0+C|}{\sqrt{A^2+B^2}}.
```

Đây không phải formula tách rời. Nó là projection của displacement lên đơn vị (unit / 단위) normal.

Nó nối coordinate hình học (geometry / 기하학) trực tiếp với dot sản phẩm (product / 제품) và projection trong tuyến tính (linear / 선형) algebra.

## 9. Circle là locus từ distance ràng buộc (constraint / 제약조건)

Circle center `C=(h,k)` radius `r` được định nghĩa là set points `P=(x,y)` sao cho

```math
d(P,C)=r.
```

Square hai phía:

```math
(x-h)^2+(y-k)^2=r^2.
```

Equation đến trực tiếp từ geometric definition. Nếu nhớ definition, không cần học thuộc formula như một đối tượng (object / 객체) riêng.

## 10. Conics là distance relationships

Coordinate equations của conics có meaning hình học.

**Parabola:** points equidistant từ focus và directrix.

**Ellipse:** sum distances tới hai foci là constant.

**Hyperbola:** absolute difference distances tới hai foci là constant.

Các tiêu chuẩn (standard / 표준) equations xuất hiện sau khi chọn coordinates phù hợp với symmetry của đối tượng (object / 객체).

Đây là lesson quan trọng: chọn coordinate hệ thống (system / 시스템) tốt có thể làm equation đơn giản mạnh.

## 11. Rotation và thay đổi (change / 변경) of coordinates

Giả sử điểm (point / 지점) có coordinates `x` trong basis cũ. Khi basis thay đổi, coordinates mới có thể khác dù geometric điểm (point / 지점) không đổi.

Trong 2D, rotation ma trận (matrix / 행렬)

```math
R(\theta)=
\begin{bmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{bmatrix}
```

có thể dùng để rotate véc-tơ (vector / 벡터) hoặc đổi biểu diễn (representation / 표현) tùy convention active/passive.

Hai operations dùng same ma trận (matrix / 행렬) cấu trúc (structure / 구조) nhưng interpretation khác. Vì vậy trong graphics/robotics cần luôn rõ: ta đang move đối tượng (object / 객체) hay đổi frame?

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

Algebra giải hệ thống (system / 시스템); hình học (geometry / 기하학) nói line cắt circle tại hai points. Discriminant của resulting quadratic encode số intersections.

## 13. Coordinate hình học (geometry / 기하학) trong Computer Graphics

Graphics thường có nhiều coordinate các hệ thống (systems / 시스템들):

```text
model/local
→ world
→ view/camera
→ clip
→ normalized device
→ screen
```

Một vertex vật lý được transform qua chuỗi xử lý (pipeline / 파이프라인) matrices. Bug thường không đến từ phép nhân ma trận (matrix multiplication / 행렬 곱셈) sai cú pháp (syntax / 문법), mà từ nhầm frame, multiplication thứ tự (order / 순서) hoặc handedness convention.

Coordinate hình học (geometry / 기하학) vì vậy là prerequisite thực tế của 2D/3D graphics.

## 14. Robotics và localization

Robot có thể cần biết:

- điểm (point / 지점) trong robot frame;
- điểm (point / 지점) trong world frame;
- sensor đo lường (measurement / 측정) trong camera/LiDAR frame.

Transformation giữa frames thường dùng rotation + translation.

Cùng một obstacle có coordinates khác nhau trong mỗi frame. Điều quan trọng là relationship giữa frames, không phải một coordinate tuple duy nhất.

## 15. AI/dữ liệu (data / 데이터): coordinates không tự động có chỉ số (metric / 지표) meaning

Tính năng (feature / 기능) véc-tơ (vector / 벡터) cũng là coordinate biểu diễn (representation / 표현).

Nếu tính năng (feature / 기능) 1 là age `0–100`, tính năng (feature / 기능) 2 là income `0–100000000`, Euclidean distance trên raw coordinates sẽ bị income dominate.

Do đó chỉ số (metric / 지표) meaningful phụ thuộc:

- scaling;
- units;
- tính năng (feature / 기능) ngữ nghĩa (semantics / 의미론);
- covariance cấu trúc (structure / 구조);
- biểu diễn (representation / 표현) learned bởi mô hình (model / 모델).

Có coordinates không có nghĩa Euclidean hình học (geometry / 기하학) là mô hình (model / 모델) đúng.

## 16. Geographic coordinates: counterexample quan trọng

Latitude/longitude là coordinates trên curved Earth surface. Nếu lấy degree differences rồi dùng flat Euclidean distance cho points xa nhau, mô hình (model / 모델) hình học (geometry / 기하학) sai.

Ta cần spherical/ellipsoidal distance hoặc suitable projection.

Đây là example rõ:

> biểu diễn (representation / 표현) bằng numbers không quyết định hình học (geometry / 기하학); chỉ số (metric / 지표) các giả định (assumptions / 가정들) mới quyết định distance.

## 17. Finance: trạng thái (state / 상태) spaces và coordinate choice

Một portfolio có thể được represent bằng holdings véc-tơ (vector / 벡터), factor exposures hoặc principal components. Cùng economic position có nhiều coordinate các hệ thống (systems / 시스템들).

Trong rủi ro (risk / 위험) modeling, đổi từ asset coordinates sang factor coordinates có thể làm covariance cấu trúc (structure / 구조) dễ hiểu hơn — tương tự đổi basis trong tuyến tính (linear / 선형) algebra.

## Mô hình tư duy (mental model / 사고 모델)

> Coordinate hình học (geometry / 기하학) là nghệ thuật chọn một numerical biểu diễn (representation / 표현) cho không gian (space / 공간). điểm (point / 지점), line, circle và distance không sinh ra từ coordinates; coordinates chỉ làm các relationships đó trở thành equations. Đổi coordinate hệ thống (system / 시스템) có thể đổi numbers mạnh nhưng không đổi geometric đối tượng (object / 객체).

## Dùng chung (common / 공통) Misconceptions

**Coordinates là đối tượng (object / 객체).** Không; chúng phụ thuộc frame/basis.

**Slope undefined nghĩa vertical line không có direction.** Không; chỉ slope ratio biểu diễn (representation / 표현) bị singular.

**Euclidean distance dùng được cho mọi numerical dữ liệu (data / 데이터).** Không; chỉ số (metric / 지표) phải match hình học (geometry / 기하학)/ngữ nghĩa (semantics / 의미론).

**Rotation ma trận (matrix / 행렬) luôn nghĩa rotate đối tượng (object / 객체).** Cùng ma trận (matrix / 행렬) cấu trúc (structure / 구조) còn có thể represent thay đổi (change / 변경) of coordinates; convention cần được nói rõ.

> **Bàn giao:** Sau **dùng chung (common / 공통) Misconceptions**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 euclidean geometry](./00_euclidean_geometry.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
