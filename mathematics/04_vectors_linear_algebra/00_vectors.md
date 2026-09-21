# Vector: state, direction, projection và representation

Vector (벡터 / vector) thường được dạy như “mũi tên có độ lớn và hướng”, nhưng đó chỉ là trực giác hình học đầu tiên. Về bản chất, vector là một object có thể cộng với vector khác và scale bởi scalar theo rules nhất quán. Vì vậy vector có thể biểu diễn displacement, velocity, force, signal, feature embedding, portfolio exposure hoặc state trong một không gian nhiều chiều.

Cách nhìn quan trọng là:

> vector không chỉ là list numbers; list numbers là coordinates của vector trong một basis đã chọn.

## 1. Scalar và vector khác nhau ở loại câu hỏi nào?

Scalar (스칼라 / scalar) mô tả một quantity bằng một number, ví dụ temperature `25°C` hoặc mass `3 kg`.

Vector cần nhiều components vì quantity có nhiều degrees of freedom:

```math
v=
\begin{bmatrix}
v_1\\v_2\\\vdots\\v_n
\end{bmatrix}.
```

Trong 2D, `v=(3,4)` có thể là displacement. Trong ML, vector có thể có hàng nghìn dimensions mà không cần “mũi tên” literal.

## 2. Point và vector không phải cùng object

Point là location. Vector là displacement/direction/state increment.

Nếu

```math
P=(1,2),\qquad Q=(4,6),
```

thì

```math
Q-P=(3,4)
```

là vector displacement từ `P` tới `Q`.

Ta có thể cộng vector vào point:

```math
P+v=Q.
```

Nhưng coordinates có thể làm point và vector trông giống nhau. Phân biệt semantics này quan trọng trong affine geometry, graphics và mechanics.

## 3. Vector addition là composition của displacements

Nếu đi vector `u`, rồi vector `v`, net displacement là

```math
u+v.
```

Theo components:

```math
(a,b)+(c,d)=(a+c,b+d).
```

Geometric parallelogram rule và componentwise addition là cùng một operation được nhìn dưới hai representations.

Addition commutative trong ordinary vector spaces:

```math
u+v=v+u.
```

Nhưng composition của transformations sau này không nhất thiết commutative. Đây là distinction quan trọng.

## 4. Scalar multiplication là scale direction

```math
kv
```

scale magnitude bởi `|k|`.

Nếu `k>0`, direction giữ nguyên. Nếu `k<0`, direction đảo. Nếu `k=0`, mọi vector collapse về zero vector.

Linear combination

```math
a_1v_1+\cdots+a_kv_k
```

là operation nền phía sau span, basis, matrix multiplication và linear models.

## 5. Norm: vector dài bao nhiêu?

Euclidean norm:

```math
\|v\|_2
=\sqrt{v_1^2+\cdots+v_n^2}.
```

Trong 2D/3D, formula đến từ Pythagoras. Nó đo distance từ origin trong Euclidean geometry.

Unit vector:

```math
\hat v=\frac{v}{\|v\|},\qquad v\ne0.
```

Tách vector thành

```math
v=\|v\|\hat v.
```

Ta có magnitude × direction.

### Nhưng norm không chỉ có L2

L1 norm:

```math
\|v\|_1=\sum_i|v_i|.
```

L-infinity norm:

```math
\|v\|_\infty=\max_i|v_i|.
```

Mỗi norm tạo geometry khác nhau. Trong optimization và ML, choice of norm encode different assumptions và penalties.

## 6. Dot product là measure của alignment

Dot product (내적 / inner product trong Euclidean coordinates):

```math
u\cdot v=\sum_i u_iv_i.
```

Geometrically:

```math
u\cdot v
=\|u\|\|v\|\cos\theta.
```

Do đó:

- positive → broadly same direction;
- zero → orthogonal;
- negative → broadly opposite.

Dot product không chỉ là arithmetic formula; nó nối coordinates với angle geometry.

## 7. Vì sao dot product có form đó?

Từ

```math
\|u-v\|^2
=(u-v)\cdot(u-v)
```

suy ra

```math
\|u-v\|^2
=\|u\|^2+\|v\|^2-2u\cdot v.
```

So với law of cosines:

```math
\|u-v\|^2
=\|u\|^2+\|v\|^2-2\|u\|\|v\|\cos\theta,
```

nên

```math
u\cdot v=\|u\|\|v\|\cos\theta.
```

Dot product vì vậy encode angle geometry của Euclidean space.

## 8. Projection: tách vector thành useful component và residual

Projection của `v` lên nonzero `u`:

```math
\operatorname{proj}_u v
=
\frac{v\cdot u}{u\cdot u}u.
```

Coefficient

```math
\frac{v\cdot u}{u\cdot u}
```

cho biết cần bao nhiêu `u` để tạo component của `v` dọc direction `u`.

Residual

```math
r=v-\operatorname{proj}_u v
```

orthogonal với `u`.

Đây là seed concept của least squares: tách target thành phần giải thích được bởi subspace và phần residual vuông góc.

## 9. Worked example: projection

Cho

```math
u=(1,0),\qquad v=(3,4).
```

Ta có

```math
v\cdot u=3,
```

```math
u\cdot u=1,
```

nên

```math
\operatorname{proj}_u v=(3,0).
```

Residual:

```math
(3,4)-(3,0)=(0,4).
```

Một vector đã được decomposition thành component along `u` và orthogonal component.

## 10. Cosine similarity: geometry của direction, không phải universal similarity

Normalized dot product:

```math
\cos\theta
=
\frac{u\cdot v}{\|u\|\|v\|}.
```

Cosine similarity bỏ magnitude và so alignment.

Trong embeddings, điều này hữu ích khi direction encode semantics. Nhưng high cosine similarity chỉ meaningful relative to chosen representation/model.

Nếu embedding space distorted hoặc feature meanings khác nhau, cosine không tự động trở thành “semantic truth”.

## 11. Cross product: oriented area trong 3D

Trong `\mathbb R^3`, cross product

```math
u\times v
```

cho vector perpendicular với cả hai.

Magnitude:

```math
\|u\times v\|
=\|u\|\|v\|\sin\theta.
```

Đó là area của parallelogram span bởi `u,v`.

Direction theo right-hand rule encode orientation.

Cross product xuất hiện trong torque, angular momentum, surface normals và graphics.

## 12. Vector equation của line và plane

Line qua point `P` direction `v`:

```math
L(t)=P+tv.
```

Plane trong 3D có thể viết bằng point `P` và normal `n`:

```math
n\cdot(x-P)=0.
```

Vector notation làm geometry coordinate-free hơn slope formulas và generalize dễ hơn sang higher dimensions.

## 13. Basis: coordinates phụ thuộc language đang dùng

Giả sử basis `e_1,e_2`. Vector

```math
v=3e_1+4e_2
```

có coordinates `(3,4)` trong basis đó.

Nếu đổi basis, same vector có coordinates khác.

Do đó statement như “vector này là `[3,4]`” thiếu context nếu basis/frame không implicit rõ.

Linear algebra sau này formalize basis change, eigenbasis và PCA theo cùng idea.

## 14. Matrix-vector multiplication là combination của columns

Nếu

```math
A=[a_1\ a_2\ \cdots\ a_n]
```

và

```math
x=
\begin{bmatrix}
x_1\\\vdots\\x_n
\end{bmatrix},
```

thì

```math
Ax=x_1a_1+\cdots+x_na_n.
```

Matrix-vector product không chỉ là row-by-column algorithm; nó tạo một linear combination của output directions encoded bởi columns.

Điều này nối vectors trực tiếp với linear transformations.

## 15. Physics: vectors là language của directional quantities

Displacement, velocity, acceleration, force và electric field đều cần direction.

Newton's second law:

```math
F=ma
```

là vector equation: direction của acceleration follow net force.

Work:

```math
W=F\cdot d
```

chỉ lấy component force theo displacement direction.

Torque:

```math
\tau=r\times F
```

encode rotational effect.

Dot/cross products vì vậy có physical meaning rõ, không chỉ formal operations.

## 16. Computer Graphics

Positions, normals, light directions và camera directions đều là vectors hoặc affine points.

Surface normal `n` dùng dot product với light direction `l`:

```math
\max(0,n\cdot l)
```

để approximate diffuse lighting.

Normals còn transform khác positions dưới non-uniform scaling; đây là reminder rằng semantics của vector type matters.

## 17. AI/Data: feature vectors và representation assumptions

Data point:

```math
x=[x_1,\ldots,x_n]^T.
```

Mỗi coordinate có semantics. Distance/dot product meaningful chỉ khi representation makes geometry meaningful.

Feature scaling, whitening, embeddings và learned representations đều cố tạo geometry nơi vectors có useful relationships.

Neural network linear layer:

```math
z=Wx+b
```

biến input vector thành output vector qua affine map.

## 18. Finance: portfolio vectors

Portfolio weights:

```math
w=(w_1,\ldots,w_n)
```

và asset return vector `r` cho portfolio return

```math
R_p=w^Tr.
```

Đây là dot product.

Risk với covariance matrix `\Sigma`:

```math
\operatorname{Var}(R_p)=w^T\Sigma w.
```

Vector/matrix language làm portfolio theory trở thành geometry trong exposure space.

## 19. High-dimensional geometry có thể counterintuitive

Trong high dimension:

- distances có thể concentrate;
- random vectors thường gần orthogonal;
- volume behavior khác intuition 2D/3D;
- raw nearest-neighbor distance có thể kém informative.

Vì vậy vector representation powerful nhưng không nên kéo trực giác 2D sang high dimension một cách máy móc.

## Mental Model

> Vector là một state/displacement được mô tả trong một basis. Norm hỏi “lớn bao nhiêu?”, dot product hỏi “align bao nhiêu?”, projection hỏi “bao nhiêu phần nằm theo direction/subspace này?”, còn matrices transform vectors sang representations/states mới.

## Common Misconceptions

**Vector là list numbers.** List numbers chỉ là coordinates của vector trong basis cụ thể.

**Point và vector interchangeable.** Chúng có thể có cùng tuple representation nhưng semantics khác.

**Euclidean norm luôn là distance đúng.** Không; metric/norm phải match problem.

**Cosine similarity cao nghĩa objects giống nhau một cách tuyệt đối.** Không; nó chỉ nói vectors align trong chosen representation.
