# Hình học Euclid: điểm, đường, góc và cấu trúc không gian

Hình học (Geometry / 기하학) nghiên cứu shape, distance, angle, position và những properties được bảo toàn qua các transformations. Hình học Euclid (Euclidean geometry / 유클리드 기하학) là model quen thuộc của mặt phẳng và không gian “phẳng” mà ta học ở trường.

## Điểm, đường thẳng và mặt phẳng

Điểm (Point / 점) lý tưởng hóa một vị trí không có kích thước. Đường thẳng (Line / 직선) là tập vô hạn points kéo dài hai phía. Mặt phẳng (Plane / 평면) là surface hai chiều lý tưởng.

Các object này không phải vật thể vật lý hoàn hảo; chúng là abstractions. Một nét bút có thickness, nhưng geometric line thì không. Bằng cách bỏ thickness, ta tập trung vào relationship position.

## Axioms và model Euclid

Hình học không thể derive mọi statement từ nothing; cần axioms/postulates. Một postulate nổi tiếng của Euclid liên quan parallel lines. Trong Euclidean plane, qua một point ngoài một line có đúng một parallel line.

Nếu thay parallel postulate, ta có non-Euclidean geometries. Trên sphere, “straightest paths” là great circles và hai great circles luôn gặp nhau. Điều này nhắc rằng geometric truth phụ thuộc model space.

## Angle

Góc (Angle / 각) đo amount of rotation giữa hai rays. Degree chia full rotation thành 360 phần; radian đo angle bằng ratio arc length/radius.

Radian quan trọng trong calculus vì nó làm formulas tự nhiên. Nếu angle `θ` radian trên circle radius `r`, arc length:

```math
s=r\theta
```

không cần conversion constant.

## Congruence và similarity

Hai figures đồng dạng theo nghĩa congruent (합동) nếu có cùng shape và size, có thể đưa trùng nhau bằng rigid transformations như translation, rotation, reflection.

Hai figures similar (닮음) nếu cùng shape nhưng size có thể khác theo uniform scale. Corresponding angles bằng nhau và corresponding lengths có cùng ratio.

Similarity là nền của map scale, perspective, indirect measurement và trigonometry.

## Triangle angle sum

Trong Euclidean plane, tổng ba interior angles của triangle là `180°` hay `π` radians. Một proof dùng line parallel qua một vertex và alternate interior angles.

Nhưng statement này không universal trong curved geometry. Trên sphere, triangle có thể có angle sum lớn hơn 180°. Vì vậy theorem cần context “Euclidean”.

## Area as measure

Diện tích (Area / 넓이) đo size hai chiều. Rectangle:

```math
A=wh
```

Triangle:

```math
A=\frac12bh
```

có thể derive bằng cách ghép hai congruent triangles thành parallelogram/rectangle tương ứng.

Circle area:

```math
A=\pi r^2
```

không phải arbitrary formula. Có thể hiểu bằng cách cắt circle thành nhiều sectors rồi xếp xen kẽ; khi số sectors tăng, shape gần rectangle có height `r` và width `πr`, cho area `πr^2`.

## Volume

Volume đo three-dimensional extent. Prism/cylinder có form

```math
V=A_{base}h
```

vì có thể nghĩ như stacking cross-sections có constant area.

Cone/pyramid có volume

```math
V=\frac13 A_{base}h
```

factor `1/3` có thể được chứng minh bằng geometric dissection hoặc calculus.

## Rigid transformations và invariants

Translation, rotation và reflection bảo toàn distance và angle. Những properties không đổi gọi là invariants.

Computer graphics dùng transformations liên tục, nhưng biểu diễn bằng matrices/homogeneous coordinates để composition hiệu quả. Hình học vì vậy nối tự nhiên sang linear algebra.

## Mental Model

> Hình học không phải collection công thức diện tích. Nó nghiên cứu những gì được bảo toàn khi object di chuyển, xoay, phản chiếu hoặc scale, và cách distance/angle tạo structure của space.

## Common Misconceptions

Một hình “trông giống” trên màn hình không đảm bảo mathematically similar nếu aspect ratio bị méo. Tổng góc triangle bằng 180° chỉ trong Euclidean geometry. Area scale theo bình phương length factor, không theo cùng factor với length.
