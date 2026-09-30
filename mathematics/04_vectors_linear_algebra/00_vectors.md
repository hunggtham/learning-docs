# Véc-tơ (vector / 벡터): trạng thái (state / 상태), direction, projection và biểu diễn (representation / 표현)

> **Mạch đọc:** Đọc **véc-tơ (vector / 벡터): trạng thái (state / 상태), direction, projection và biểu diễn (representation / 표현)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Scalar và véc-tơ (vector / 벡터) khác nhau ở loại câu hỏi nào?** sang **2. điểm (point / 지점) và véc-tơ (vector / 벡터) không phải cùng đối tượng (object / 객체)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Véc-tơ (vector / 벡터) thường được dạy như “mũi tên có độ lớn và hướng”, nhưng đó chỉ là trực giác hình học đầu tiên. Về bản chất, véc-tơ (vector / 벡터) là một đối tượng (object / 객체) có thể cộng với véc-tơ (vector / 벡터) khác và quy mô (scale / 규모) bởi scalar theo rules nhất quán. Vì vậy véc-tơ (vector / 벡터) có thể biểu diễn displacement, velocity, force, tín hiệu (signal / 신호), tính năng (feature / 기능) embedding, portfolio exposure hoặc trạng thái (state / 상태) trong một không gian nhiều chiều.

Cách nhìn quan trọng là:

> véc-tơ (vector / 벡터) không chỉ là danh sách (list / 목록) numbers; danh sách (list / 목록) numbers là coordinates của véc-tơ (vector / 벡터) trong một basis đã chọn.

## 1. Scalar và véc-tơ (vector / 벡터) khác nhau ở loại câu hỏi nào?

Scalar (스칼라 / scalar) mô tả một quantity bằng một number, ví dụ temperature `25°C` hoặc mass `3 kg`.

Véc-tơ (vector / 벡터) cần nhiều components vì quantity có nhiều degrees of freedom:

```math
v=
\begin{bmatrix}
v_1\\v_2\\\vdots\\v_n
\end{bmatrix}.
```

Trong 2D, `v=(3,4)` có thể là displacement. Trong ML, véc-tơ (vector / 벡터) có thể có hàng nghìn dimensions mà không cần “mũi tên” literal.

## 2. điểm (point / 지점) và véc-tơ (vector / 벡터) không phải cùng đối tượng (object / 객체)

Điểm (point / 지점) là location. véc-tơ (vector / 벡터) là displacement/direction/trạng thái (state / 상태) increment.

Nếu

```math
P=(1,2),\qquad Q=(4,6),
```

thì

```math
Q-P=(3,4)
```

là véc-tơ (vector / 벡터) displacement từ `P` tới `Q`.

Ta có thể cộng véc-tơ (vector / 벡터) vào điểm (point / 지점):

```math
P+v=Q.
```

Nhưng coordinates có thể làm điểm (point / 지점) và véc-tơ (vector / 벡터) trông giống nhau. Phân biệt ngữ nghĩa (semantics / 의미론) này quan trọng trong affine hình học (geometry / 기하학), graphics và mechanics.

## 3. véc-tơ (vector / 벡터) addition là composition của displacements

Nếu đi véc-tơ (vector / 벡터) `u`, rồi véc-tơ (vector / 벡터) `v`, net displacement là

```math
u+v.
```

Theo components:

```math
(a,b)+(c,d)=(a+c,b+d).
```

Geometric parallelogram quy tắc (rule / 규칙) và componentwise addition là cùng một thao tác (operation / 연산) được nhìn dưới hai representations.

Addition commutative trong ordinary véc-tơ (vector / 벡터) spaces:

```math
u+v=v+u.
```

Nhưng composition của transformations sau này không nhất thiết commutative. Đây là distinction quan trọng.

## 4. Scalar multiplication là quy mô (scale / 규모) direction

Scalar multiplication thay đổi độ lớn vector và có thể đảo hướng khi scalar âm, nhưng không tạo hướng mới ngoài span ban đầu. Đây là bước nền để hiểu linear combination và vector space.

Scalar multiplication thay đổi độ lớn vector và có thể đảo hướng khi scalar âm, nhưng không tạo hướng mới ngoài span ban đầu. Đây là bước nền để hiểu linear combination và vector space.

```math
kv
```

Quy mô (scale / 규모) magnitude bởi `|k|`.

Nếu `k>0`, direction giữ nguyên. Nếu `k<0`, direction đảo. Nếu `k=0`, mọi véc-tơ (vector / 벡터) collapse về zero véc-tơ (vector / 벡터).

Tuyến tính (linear / 선형) combination

```math
a_1v_1+\cdots+a_kv_k
```

là thao tác (operation / 연산) nền phía sau span, basis, phép nhân ma trận (matrix multiplication / 행렬 곱셈) và tuyến tính (linear / 선형) các mô hình (models / 모델들).

## 5. Norm: véc-tơ (vector / 벡터) dài bao nhiêu?

Euclidean norm:

```math
\|v\|_2
=\sqrt{v_1^2+\cdots+v_n^2}.
```

Trong 2D/3D, formula đến từ Pythagoras. Nó đo distance từ origin trong Euclidean hình học (geometry / 기하학).

Đơn vị (unit / 단위) véc-tơ (vector / 벡터):

```math
\hat v=\frac{v}{\|v\|},\qquad v\ne0.
```

Tách véc-tơ (vector / 벡터) thành

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

Mỗi norm tạo hình học (geometry / 기하학) khác nhau. Trong tối ưu hóa (optimization / 최적화) và ML, choice of norm encode different các giả định (assumptions / 가정들) và penalties.

## 6. Dot sản phẩm (product / 제품) là measure của alignment

Dot sản phẩm (product / 제품):

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

Dot sản phẩm (product / 제품) không chỉ là arithmetic formula; nó nối coordinates với angle hình học (geometry / 기하학).

## 7. Vì sao dot sản phẩm (product / 제품) có form đó?

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

Dot sản phẩm (product / 제품) vì vậy encode angle hình học (geometry / 기하학) của Euclidean không gian (space / 공간).

## 8. Projection: tách véc-tơ (vector / 벡터) thành useful thành phần (component / 컴포넌트) và residual

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

cho biết cần bao nhiêu `u` để tạo thành phần (component / 컴포넌트) của `v` dọc direction `u`.

Residual

```math
r=v-\operatorname{proj}_u v
```

orthogonal với `u`.

Đây là seed concept của least squares: tách mục tiêu (target / 대상) thành phần giải thích được bởi subspace và phần residual vuông góc.

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

Một véc-tơ (vector / 벡터) đã được decomposition thành thành phần (component / 컴포넌트) along `u` và orthogonal thành phần (component / 컴포넌트).

## 10. Cosine similarity: hình học (geometry / 기하학) của direction, không phải universal similarity

Normalized dot sản phẩm (product / 제품):

```math
\cos\theta
=
\frac{u\cdot v}{\|u\|\|v\|}.
```

Cosine similarity bỏ magnitude và so alignment.

Trong embeddings, điều này hữu ích khi direction encode ngữ nghĩa (semantics / 의미론). Nhưng high cosine similarity chỉ meaningful relative to chosen biểu diễn (representation / 표현)/mô hình (model / 모델).

Nếu embedding không gian (space / 공간) distorted hoặc tính năng (feature / 기능) meanings khác nhau, cosine không tự động trở thành “ngữ nghĩa (semantic / 의미적) truth”.

## 11. Cross sản phẩm (product / 제품): oriented area trong 3D

Trong `\mathbb R^3`, cross sản phẩm (product / 제품)

```math
u\times v
```

cho véc-tơ (vector / 벡터) perpendicular với cả hai.

Magnitude:

```math
\|u\times v\|
=\|u\|\|v\|\sin\theta.
```

Đó là area của parallelogram span bởi `u,v`.

Direction theo right-hand quy tắc (rule / 규칙) encode orientation.

Cross sản phẩm (product / 제품) xuất hiện trong torque, angular momentum, surface normals và graphics.

## 12. véc-tơ (vector / 벡터) equation của line và plane

Line qua điểm (point / 지점) `P` direction `v`:

```math
L(t)=P+tv.
```

Plane trong 3D có thể viết bằng điểm (point / 지점) `P` và normal `n`:

```math
n\cdot(x-P)=0.
```

Véc-tơ (vector / 벡터) notation làm hình học (geometry / 기하학) coordinate-free hơn slope formulas và generalize dễ hơn sang higher dimensions.

## 13. Basis: coordinates phụ thuộc ngôn ngữ (language / 언어) đang dùng

Giả sử basis `e_1,e_2`. véc-tơ (vector / 벡터)

```math
v=3e_1+4e_2
```

có coordinates `(3,4)` trong basis đó.

Nếu đổi basis, same véc-tơ (vector / 벡터) có coordinates khác.

Do đó statement như “véc-tơ (vector / 벡터) này là `[3,4]`” thiếu ngữ cảnh (context / 맥락) nếu basis/frame không implicit rõ.

Tuyến tính (linear / 선형) algebra sau này formalize basis thay đổi (change / 변경), eigenbasis và PCA theo cùng idea.

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

Matrix-vector sản phẩm (product / 제품) không chỉ là row-by-column thuật toán (algorithm / 알고리즘); nó tạo một tuyến tính (linear / 선형) combination của đầu ra (output / 출력) directions encoded bởi columns.

Điều này nối vectors trực tiếp với tuyến tính (linear / 선형) transformations.

## 15. Physics: vectors là ngôn ngữ (language / 언어) của directional quantities

Displacement, velocity, acceleration, force và electric trường dữ liệu (field / 필드) đều cần direction.

Newton's second law:

```math
F=ma
```

là véc-tơ (vector / 벡터) equation: direction của acceleration follow net force.

Công việc (work / 작업):

```math
W=F\cdot d
```

chỉ lấy thành phần (component / 컴포넌트) force theo displacement direction.

Torque:

```math
\tau=r\times F
```

encode rotational tác động (effect / 효과).

Dot/cross products vì vậy có vật lý (physical / 물리적) meaning rõ, không chỉ formal operations.

## 16. Computer Graphics

Positions, normals, light directions và camera directions đều là vectors hoặc affine points.

Surface normal `n` dùng dot sản phẩm (product / 제품) với light direction `l`:

```math
\max(0,n\cdot l)
```

để approximate diffuse lighting.

Normals còn transform khác positions dưới non-uniform scaling; đây là reminder rằng ngữ nghĩa (semantics / 의미론) của véc-tơ (vector / 벡터) kiểu (type / 타입) matters.

## 17. AI/dữ liệu (data / 데이터): tính năng (feature / 기능) vectors và biểu diễn (representation / 표현) các giả định (assumptions / 가정들)

Dữ liệu (data / 데이터) điểm (point / 지점):

```math
x=[x_1,\ldots,x_n]^T.
```

Mỗi coordinate có ngữ nghĩa (semantics / 의미론). Distance/dot sản phẩm (product / 제품) meaningful chỉ khi biểu diễn (representation / 표현) makes hình học (geometry / 기하학) meaningful.

Tính năng (feature / 기능) scaling, whitening, embeddings và learned representations đều cố tạo hình học (geometry / 기하학) nơi vectors có useful relationships.

Neural mạng (network / 네트워크) tuyến tính (linear / 선형) tầng (layer / 계층):

```math
z=Wx+b
```

biến đầu vào (input / 입력) véc-tơ (vector / 벡터) thành đầu ra (output / 출력) véc-tơ (vector / 벡터) qua affine map.

## 18. Finance: portfolio vectors

Portfolio weights:

```math
w=(w_1,\ldots,w_n)
```

và asset return véc-tơ (vector / 벡터) `r` cho portfolio return

```math
R_p=w^Tr.
```

Đây là dot sản phẩm (product / 제품).

Rủi ro (risk / 위험) với covariance ma trận (matrix / 행렬) `\Sigma`:

```math
\operatorname{Var}(R_p)=w^T\Sigma w.
```

Véc-tơ (vector / 벡터)/ma trận (matrix / 행렬) ngôn ngữ (language / 언어) làm portfolio lý thuyết (theory / 이론) trở thành hình học (geometry / 기하학) trong exposure không gian (space / 공간).

## 19. High-dimensional hình học (geometry / 기하학) có thể counterintuitive

Trong high dimension:

- distances có thể concentrate;
- random vectors thường gần orthogonal;
- volume hành vi (behavior / 동작) khác intuition 2D/3D;
- raw nearest-neighbor distance có thể kém informative.

Vì vậy véc-tơ (vector / 벡터) biểu diễn (representation / 표현) powerful nhưng không nên kéo trực giác 2D sang high dimension một cách máy móc.

## Mô hình tư duy (mental model / 사고 모델)

> véc-tơ (vector / 벡터) là một trạng thái (state / 상태)/displacement được mô tả trong một basis. Norm hỏi “lớn bao nhiêu?”, dot sản phẩm (product / 제품) hỏi “align bao nhiêu?”, projection hỏi “bao nhiêu phần nằm theo direction/subspace này?”, còn matrices transform vectors sang representations/states mới.

## Dùng chung (common / 공통) Misconceptions

**véc-tơ (vector / 벡터) là danh sách (list / 목록) numbers.** danh sách (list / 목록) numbers chỉ là coordinates của véc-tơ (vector / 벡터) trong basis cụ thể.

**điểm (point / 지점) và véc-tơ (vector / 벡터) interchangeable.** Chúng có thể có cùng tuple biểu diễn (representation / 표현) nhưng ngữ nghĩa (semantics / 의미론) khác.

**Euclidean norm luôn là distance đúng.** Không; chỉ số (metric / 지표)/norm phải match bài toán (problem / 문제).

**Cosine similarity cao nghĩa objects giống nhau một cách tuyệt đối.** Không; nó chỉ nói vectors align trong chosen biểu diễn (representation / 표현).

> **Bàn giao:** Sau **dùng chung (common / 공통) Misconceptions**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 matrices and linear systems](./01_matrices_and_linear_systems.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
