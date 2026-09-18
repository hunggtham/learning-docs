# Vector: đại lượng có nhiều thành phần và hướng

Vector (Vector / 벡터) là một đối tượng có nhiều components có thứ tự, thường dùng để biểu diễn displacement, velocity, force hoặc một point/feature trong high-dimensional space. Trong hình học 2D, vector có thể được nhìn như mũi tên có magnitude và direction; trong machine learning, vector có thể có hàng nghìn dimensions mà không cần hình dung bằng mũi tên.

## Vector và scalar

Scalar (Scalar / 스칼라) là một value đơn như temperature `25°C` hay mass `3 kg`. Vector có nhiều components:

```math
\mathbf v=
\begin{bmatrix}
v_1\\v_2\\\vdots\\v_n
\end{bmatrix}
```

Trong 2D, `v=(3,4)` có thể là displacement 3 units theo x, 4 theo y.

## Addition

Vector addition theo component:

```math
(a,b)+(c,d)=(a+c,b+d)
```

Geometrically, đặt tail vector thứ hai ở head vector thứ nhất; resultant nối start đến end. Đây là composition của displacements.

Nếu đi 3 m east rồi 4 m north, net displacement là vector `(3,4)`, dù path length là 7 m. Magnitude displacement chỉ 5 m. Path length và displacement là hai quantities khác nhau.

## Scalar multiplication

```math
k\mathbf v
```

scale magnitude bởi `|k|`; nếu `k<0`, direction đảo. Đây là phép “stretch/shrink/flip” vector.

## Norm

Euclidean norm:

```math
\|\mathbf v\|_2=\sqrt{v_1^2+\cdots+v_n^2}
```

trong 2D đến từ Pythagoras. Norm đo magnitude/distance to origin.

Unit vector:

```math
\hat v=\frac{\mathbf v}{\|\mathbf v\|}
```

có norm 1 và giữ direction. Tách vector thành magnitude × direction:

```math
\mathbf v=\|\mathbf v\|\hat v
```

## Dot product

Tích vô hướng (Dot product / 내적):

```math
\mathbf u\cdot\mathbf v=\sum_i u_iv_i
```

đồng thời có geometric form:

```math
\mathbf u\cdot\mathbf v=\|u\|\|v\|\cos\theta
```

Nếu dot product positive, vectors broadly align; zero nghĩa orthogonal; negative broadly opposite.

Tại sao dot product hữu ích? Nó đo component của một vector theo direction của vector kia. Projection scalar của `v` lên unit vector `u` là `u·v`.

## Projection

Projection của `v` lên nonzero `u`:

```math
\operatorname{proj}_{u}v
=\frac{v\cdot u}{u\cdot u}u
```

Coefficient đầu đo “bao nhiêu phần của u” cần để tạo component gần nhất của v along u.

Least squares regression sau này chính là projection data vector lên subspace sinh bởi model columns.

## Cosine similarity

Normalized dot product:

```math
\cos\theta=\frac{u\cdot v}{\|u\|\|v\|}
```

được dùng làm cosine similarity. Nó bỏ magnitude và so direction. Trong text embeddings, hai vectors có direction gần nhau có cosine similarity cao, nhưng interpretation phụ thuộc embedding model.

## Cross product

Trong 3D, cross product:

```math
u\times v
```

cho vector perpendicular với cả `u` và `v`, magnitude

```math
\|u\times v\|=\|u\|\|v\|\sin\theta
```

bằng area parallelogram span bởi hai vectors. Nó xuất hiện trong torque, surface normals và 3D graphics.

## Feature vectors

Một data point có thể encode thành

```math
x=[x_1,x_2,\ldots,x_n]^T
```

mỗi component là feature. Nhưng distance giữa feature vectors chỉ meaningful sau khi scale/semantics được cân nhắc. Một feature đo won có magnitude hàng triệu có thể dominate feature đo age hàng chục nếu dùng raw Euclidean distance.

## Mental Model

> Vector là “một trạng thái có nhiều coordinates” hoặc “một displacement trong space”. Operations như dot product và projection không chỉ tính numbers; chúng trả lời geometric questions về length, alignment và component.

## Common Misconceptions

Point và vector có cùng coordinate representation nhưng concept khác: point là location, vector là displacement/direction. Dot product trả scalar, không phải vector. Cosine similarity cao không tự động nghĩa hai objects “giống nhau” theo mọi khía cạnh; nó chỉ phản ánh geometry của chosen representation.
