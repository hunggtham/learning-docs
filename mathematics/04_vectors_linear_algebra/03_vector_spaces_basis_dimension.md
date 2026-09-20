# Không gian vector, cơ sở và số chiều

Khi mới học vector, ta thường nghĩ đến mũi tên trong mặt phẳng hoặc không gian 3D. Nhưng linear algebra đi xa hơn nhiều: điều quan trọng không phải object “trông như mũi tên”, mà là object có thể **cộng** và **nhân với scalar** theo những quy tắc nhất quán hay không. Từ observation đó xuất hiện khái niệm không gian vector (Vector Space / 벡터공간).

Một vector space là một universe trong đó ta có thể tạo linear combinations mà vẫn ở trong cùng universe. Các vectors có thể là coordinate tuples, polynomials, functions, signals, matrices, images đã vector hóa hoặc states của một dynamic system.

> Không gian vector không phải một nơi có hình học sẵn. Nó là một structure của những objects có thể được kết hợp tuyến tính.

## Tại sao cần abstraction này?

Giả sử ta hiểu linear algebra chỉ trên `R^2` và `R^3`. Khi chuyển sang polynomial

```math
p(x)=a+bx+cx^2,
```

hoặc signal

```math
f(t)=a\sin t+b\cos t,
```

ta có vẻ bước sang lĩnh vực khác. Nhưng algebra bên dưới giống hệt:

- cộng hai polynomials vẫn là polynomial;
- multiply polynomial với scalar vẫn là polynomial;
- cộng hai signals vẫn là signal;
- multiply signal với scalar vẫn hợp lệ.

Nếu bỏ qua bề ngoài và giữ lại operations, ta thấy cùng một linear structure. Vector space abstraction cho phép một theorem về basis, projection hoặc linear transformation áp dụng đồng thời cho geometry, signals, data và differential equations.

## Vector space cần những properties nào?

Cho một set `V` và scalar field thường là `R` hoặc `C`. Ta có vector addition và scalar multiplication.

Các operations phải behave giống linear arithmetic quen thuộc: addition associative và commutative, có zero vector, mỗi vector có additive inverse, scalar multiplication compatible với scalar multiplication, và distributive laws phải đúng.

Ví dụ:

```math
u+(v+w)=(u+v)+w,
```

```math
u+v=v+u,
```

```math
a(u+v)=au+av,
```

```math
(a+b)v=av+bv.
```

Điểm của axioms không phải để memorize một danh sách. Chúng xác định minimum structure cần để algebra của linear combinations hoạt động đáng tin cậy.

## Linear combination: building block trung tâm

Cho vectors `v_1,...,v_k`, một linear combination là

```math
c_1v_1+c_2v_2+\cdots+c_kv_k,
```

trong đó `c_i` là scalars.

Mọi concept quan trọng trong chapter này đều xoay quanh câu hỏi: **những linear combinations nào có thể được tạo ra, và có bao nhiêu directions thực sự độc lập?**

Nếu ta có hai vectors trong `R^2`,

```math
v_1=(1,0),\qquad v_2=(0,1),
```

thì mọi vector `(x,y)` có thể viết

```math
(x,y)=xv_1+yv_2.
```

Hai vectors đó đủ để generate toàn plane.

## Span: những gì ta có thể tạo ra

Span của một collection vectors là set của tất cả linear combinations:

```math
\operatorname{span}\{v_1,\ldots,v_k\}
=
\left\{\sum_{i=1}^k c_iv_i\;:\;c_i\in\mathbb F\right\}.
```

Span trả lời câu hỏi **reachability bằng linear combination**.

Trong `R^3`:

- một nonzero vector span một line qua origin;
- hai nonparallel vectors span một plane qua origin;
- ba vectors phù hợp có thể span toàn `R^3`.

Nếu một dataset có feature vectors nằm gần một low-dimensional span, dimensionality reduction có thể compress data bằng cách tìm basis thích hợp cho subspace đó.

## Linear dependence: khi có redundancy

Vectors `v_1,...,v_k` linearly independent nếu equation

```math
c_1v_1+\cdots+c_kv_k=0
```

chỉ có trivial solution

```math
c_1=\cdots=c_k=0.
```

Nếu tồn tại nontrivial coefficients, vectors linearly dependent.

### Vì sao dependence nghĩa là redundancy?

Giả sử

```math
c_1v_1+\cdots+c_kv_k=0
```

và `c_j≠0`. Ta solve cho `v_j`:

```math
v_j=-\sum_{i\ne j}\frac{c_i}{c_j}v_i.
```

Tức `v_j` có thể được tạo từ những vectors còn lại. Nó không thêm direction mới vào span.

Đây là mathematical meaning của redundancy.

Trong regression, nếu một feature là exact linear combination của others, design matrix mất full column rank. Parameters có thể không unique. Trong database/reporting, nếu một derived column hoàn toàn được determine bởi các columns khác, nó không thêm independent information theo linear sense.

## Basis: spanning mà không dư thừa

Một basis (Basis / 기저) của vector space `V` là collection vectors vừa:

1. linearly independent;
2. span toàn `V`.

Hai conditions này cùng nhau tạo ra một coordinate system tối thiểu: đủ để represent mọi vector, nhưng không có redundancy.

Standard basis của `R^3` là

```math
e_1=(1,0,0),\quad e_2=(0,1,0),\quad e_3=(0,0,1).
```

Mọi vector

```math
v=(x,y,z)
```

được viết uniquely:

```math
v=xe_1+ye_2+ze_3.
```

Tính **unique representation** này là consequence trực tiếp của independence + spanning.

Nếu representation không unique, basis vectors dependent. Nếu một số vector không represent được, collection chưa span toàn space.

## Basis không phải duy nhất

Trong `R^2`, standard basis

```math
(1,0),(0,1)
```

chỉ là một lựa chọn. Collection

```math
(1,1),(1,-1)
```

cũng là basis vì hai vectors independent và span plane.

Object không đổi khi basis đổi. Chỉ coordinates của object thay đổi.

Đây là một trong những mental shifts quan trọng nhất của linear algebra:

> coordinates không phải vector; chúng là description của vector relative to a chosen basis.

## Change of basis: cùng object, ngôn ngữ tọa độ khác

Giả sử basis `B={b_1,...,b_n}`. Một vector `v` có coordinates

```math
[v]_B=
\begin{bmatrix}
c_1\\
\vdots\\
c_n
\end{bmatrix}
```

nếu

```math
v=c_1b_1+\cdots+c_nb_n.
```

Nếu matrix

```math
P=
\begin{bmatrix}
|&&|\\
b_1&\cdots&b_n\\
|&&|
\end{bmatrix},
```

thì standard coordinates thỏa

```math
v=P[v]_B.
```

Nếu `P` invertible,

```math
[v]_B=P^{-1}v.
```

Change of basis vì thế là matrix transformation giữa hai coordinate descriptions của cùng abstract vector.

## Vì sao chọn basis tốt có thể thay đổi toàn bộ problem?

Một operator phức tạp trong standard basis có thể trở nên diagonal trong eigenbasis. Một signal khó nhìn theo time samples có thể trở nên sparse theo Fourier basis. PCA chọn orthogonal directions sao cho variance được concentrate vào few components.

Đây không phải cosmetic coordinate change. Representation phù hợp có thể biến computation từ coupled thành gần independent, làm pattern rõ hơn và giảm dimension cần thiết.

## Dimension: số degrees of freedom độc lập

Dimension (Dimension / 차원) của finite-dimensional vector space là số vectors trong bất kỳ basis nào của space đó.

Một theorem nền tảng bảo đảm mọi bases của cùng finite-dimensional space có cùng number of vectors. Vì vậy dimension là property của space, không phải của basis cụ thể.

`R^2` dimension 2, `R^3` dimension 3.

Space của polynomials degree at most 2,

```math
P_2=\{a+bx+cx^2\},
```

có basis

```math
\{1,x,x^2\}
```

nên dimension 3.

Space của `2×2` real matrices có dimension 4 vì một matrix

```math
\begin{bmatrix}
a&b\\
c&d
\end{bmatrix}
```

cần bốn independent coefficients.

Dimension không phải “số values đang lưu” một cách máy móc. Nó là số independent coordinates cần để specify arbitrary vector trong space.

## Subspace: một linear universe nhỏ hơn bên trong space lớn

Một subset `W⊆V` là subspace nếu nó tự đóng dưới vector addition và scalar multiplication.

Một practical test là:

- `0∈W`;
- nếu `u,v∈W` thì `u+v∈W`;
- nếu `v∈W` và scalar `c`, thì `cv∈W`.

Column space, row space, null space và eigenspaces là các subspaces tự nhiên.

Một affine plane không đi qua origin không phải linear subspace, vì zero vector không thuộc nó. Nó là translated subspace.

Distinction này giải thích vì sao equation homogeneous

```math
Ax=0
```

có solution set là subspace, còn

```math
Ax=b
```

với `b≠0` thường tạo affine set.

## Column space và null space

Cho matrix

```math
A\in\mathbb R^{m\times n}.
```

Column space là span của columns của `A`. Nó chứa mọi possible output của transformation

```math
x\mapsto Ax.
```

Null space là

```math
\mathcal N(A)=\{x:Ax=0\}.
```

Nó chứa input directions mà transformation collapse về zero.

Hai spaces này trả lời hai questions khác nhau:

- transformation có thể tạo ra outputs nào?
- transformation làm mất những input directions nào?

## Rank-nullity: accounting của dimensions

Một theorem trung tâm là

```math
\operatorname{rank}(A)+\operatorname{nullity}(A)=n,
```

với `A` có `n` columns.

`rank(A)` là dimension của column space. `nullity(A)` là dimension của null space.

Interpretation:

> input space có `n` degrees of freedom; một phần survive thành independent output directions, phần còn lại bị collapse vào null space.

Ví dụ nếu `A:R^5→R^3` có rank 3, thì nullity là 2. Transformation giữ được ba independent directions và mất hai degrees of freedom.

Đây là một dạng conservation/accounting law cho linear information.

## Coordinates như compression khi structure tồn tại

Nếu một object sống trong high-dimensional ambient space nhưng thực sự nằm trong lower-dimensional subspace, basis của subspace cho representation compact hơn.

Ví dụ image 100×100 pixels có 10,000 raw dimensions, nhưng nếu dataset variation chủ yếu nằm gần một lower-dimensional manifold/subspace, PCA có thể represent phần lớn variance bằng vài hundred components.

Đây là lý do dimension reduction không chỉ là “xóa columns”. Nó tìm coordinate system nơi information relevant concentrate hơn.

## Orthogonal và orthonormal basis

Nếu basis vectors mutually orthogonal,

```math
b_i\cdot b_j=0\quad(i\ne j),
```

và mỗi vector normalized,

```math
\|b_i\|=1,
```

basis gọi là orthonormal.

Với orthonormal basis, coefficient rất dễ tính:

```math
c_i=v\cdot b_i.
```

Không cần solve full linear system. Projection, least squares, Fourier coefficients và QR decomposition đều hưởng lợi từ orthogonality.

Orthonormal bases cũng thường numerically stable hơn vì basis vectors không gần dependent.

## Function spaces: vector spaces có thể vô hạn chiều

Linear algebra không dừng ở finite tuples. Consider space của functions trên interval. Nếu `f` và `g` là functions, ta có

```math
(f+g)(x)=f(x)+g(x)
```

và

```math
(cf)(x)=cf(x).
```

Nhiều function spaces là vector spaces, thường infinite-dimensional.

Fourier analysis nhìn function như combination của basis-like sinusoids. Quantum mechanics dùng Hilbert spaces. Differential equations thường tìm unknown function trong một function space phù hợp.

Vì vậy idea basis/dimension mở đường từ elementary linear algebra sang analysis và mathematical physics.

## Feature space trong machine learning

Một sample có thể được represent thành feature vector

```math
x=(x_1,\ldots,x_d).
```

`d` là ambient feature dimension, nhưng không nhất thiết intrinsic dimension của data.

Nếu features strongly correlated, effective information dimension có thể thấp hơn. Nếu một feature exact combination của others, design matrix rank giảm.

Điều này nối trực tiếp linear independence, rank và conditioning với practical ML issues như multicollinearity.

## Curse of dimensionality: tại sao nhiều dimensions khó?

Suppose mỗi dimension được discretize thành `k` levels. Một grid trong `d` dimensions có

```math
k^d
```

cells.

Nếu `k=10` và `d=2`, có 100 cells. Với `d=10`, đã có

```math
10^{10}
```

cells.

Space volume tăng cực nhanh theo dimension, nên fixed number data points trở nên sparse.

Distance geometry cũng thay đổi. Trong many high-dimensional distributions, nearest và farthest distances có thể trở nên tương đối gần nhau; intuition từ 2D/3D không còn tốt.

Đây là lý do algorithms dựa trên local density hoặc nearest neighbors cần careful scaling, regularization, dimensionality reduction hoặc structural assumptions.

## Basis và representation trong software/data systems

Cùng idea “choose coordinates” xuất hiện ngoài pure mathematics.

One-hot encoding chọn standard basis-like representation cho categories. Embedding học một coordinate representation dense hơn. PCA chọn orthogonal basis từ covariance structure. Fourier transform đổi từ time/sample coordinates sang frequency coordinates. Wavelets chọn localized multi-scale basis.

Không phải mọi representation là literal linear basis, nhưng mental model giống nhau: **cùng object có thể dễ hiểu hơn trong coordinate system phù hợp**.

## Khi linear space model không đủ

Vector space giả định closure dưới arbitrary scalar multiplication và addition. Nhiều real-world sets không thỏa.

Probability distributions không thể cộng arbitrary coefficients rồi vẫn là valid probability distribution. Rotations form a group, không phải vector space dưới matrix addition. Points trên sphere không đóng dưới addition.

Trong các trường hợp đó, forcing vector-space intuition có thể gây sai. Ta có thể cần affine spaces, manifolds, groups, cones hoặc probability simplices.

Biết khi nào linear structure không phù hợp cũng quan trọng như biết dùng nó.

## Knowledge Connection — basis và eigenvectors

Nếu linear operator `A` có đủ independent eigenvectors, chúng tạo basis `P` và

```math
A=PDP^{-1}.
```

Trong eigenbasis, operator trở thành diagonal scaling. Đây là ultimate example của “choose basis to expose structure”.

Nếu matrix defective và không có đủ eigenvectors, diagonal basis không tồn tại; ta cần richer structures như Jordan form. Vì vậy basis availability ảnh hưởng trực tiếp cách ta simplify transformation.

## Knowledge Connection — basis và Fourier

Sine/cosine hoặc complex exponentials đóng vai trò basis functions cho nhiều signal spaces. Time-domain waveform có thể được represent bằng coefficients theo frequency components.

Cùng signal không thay đổi; chỉ coordinate language đổi. Một convolution khó nhìn trong time domain có thể trở thành multiplication đơn giản trong frequency domain.

Đây là lý do basis không phải một khái niệm abstract tách khỏi engineering — nó quyết định representation nơi operation trở nên đơn giản.

## Mental Model

> Vector space là một universe của những objects có thể được kết hợp tuyến tính. Span hỏi “ta tạo được những gì?”, independence hỏi “có redundancy không?”, basis là vocabulary tối thiểu đủ để diễn đạt mọi vector, còn dimension là số degrees of freedom độc lập. Đổi basis không đổi object; nó đổi ngôn ngữ mô tả object, và một ngôn ngữ tốt có thể làm structure ẩn trở nên hiển nhiên.

## Common Misconceptions

**“Vector space nghĩa là không gian hình học có mũi tên.”** Không. Polynomials, functions và matrices cũng có thể là vectors nếu operations thỏa vector-space axioms.

**“Basis là duy nhất.”** Basis có thể có vô số lựa chọn. Dimension mới là invariant.

**“Có nhiều coordinates nghĩa là có nhiều independent information.”** Không. Coordinates/features có thể linearly dependent. Rank đo independent linear directions, không phải raw column count.

**“Mọi plane trong `R^3` là subspace.”** Chỉ plane đi qua origin mới là linear subspace. Plane translated khỏi origin là affine set.

**“High dimension luôn tốt vì chứa nhiều information.”** Higher ambient dimension có thể chỉ thêm redundancy/noise và làm estimation khó hơn. Value nằm ở independent, relevant structure chứ không phải dimension count tự thân.