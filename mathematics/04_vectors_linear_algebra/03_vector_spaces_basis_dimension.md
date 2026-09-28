# Không gian véc-tơ (vector / 벡터), cơ sở và số chiều

> **Mạch đọc:** Đọc **Không gian véc-tơ (vector / 벡터), cơ sở và số chiều** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Tại sao cần lớp trừu tượng (abstraction / 추상화) này?** sang **véc-tơ (vector / 벡터) không gian (space / 공간) cần những properties nào?**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Khi mới học véc-tơ (vector / 벡터), ta thường nghĩ đến mũi tên trong mặt phẳng hoặc không gian 3D. Nhưng tuyến tính (linear / 선형) algebra đi xa hơn nhiều: điều quan trọng không phải đối tượng (object / 객체) “trông như mũi tên”, mà là đối tượng (object / 객체) có thể **cộng** và **nhân với scalar** theo những quy tắc nhất quán hay không. Từ observation đó xuất hiện khái niệm không gian véc-tơ (vector / 벡터).

Một véc-tơ (vector / 벡터) không gian (space / 공간) là một universe trong đó ta có thể tạo tuyến tính (linear / 선형) combinations mà vẫn ở trong cùng universe. Các vectors có thể là coordinate tuples, polynomials, functions, signals, matrices, images đã véc-tơ (vector / 벡터) hóa hoặc states của một hệ động (dynamic system / 동적 시스템).

> Không gian véc-tơ (vector / 벡터) không phải một nơi có hình học sẵn. Nó là một cấu trúc (structure / 구조) của những objects có thể được kết hợp tuyến tính.

## Tại sao cần lớp trừu tượng (abstraction / 추상화) này?

Giả sử ta hiểu tuyến tính (linear / 선형) algebra chỉ trên `R^2` và `R^3`. Khi chuyển sang polynomial

```math
p(x)=a+bx+cx^2,
```

hoặc tín hiệu (signal / 신호)

```math
f(t)=a\sin t+b\cos t,
```

ta có vẻ bước sang lĩnh vực khác. Nhưng algebra bên dưới giống hệt:

- cộng hai polynomials vẫn là polynomial;
- multiply polynomial với scalar vẫn là polynomial;
- cộng hai signals vẫn là tín hiệu (signal / 신호);
- multiply tín hiệu (signal / 신호) với scalar vẫn hợp lệ.

Nếu bỏ qua bề ngoài và giữ lại operations, ta thấy cùng một tuyến tính (linear / 선형) cấu trúc (structure / 구조). véc-tơ (vector / 벡터) không gian (space / 공간) lớp trừu tượng (abstraction / 추상화) cho phép một theorem về basis, projection hoặc tuyến tính (linear / 선형) transformation áp dụng đồng thời cho hình học (geometry / 기하학), signals, dữ liệu (data / 데이터) và differential equations.

## Véc-tơ (vector / 벡터) không gian (space / 공간) cần những properties nào?

Cho một set `V` và scalar trường dữ liệu (field / 필드) thường là `R` hoặc `C`. Ta có véc-tơ (vector / 벡터) addition và scalar multiplication.

Các operations phải behave giống tuyến tính (linear / 선형) arithmetic quen thuộc: addition associative và commutative, có zero véc-tơ (vector / 벡터), mỗi véc-tơ (vector / 벡터) có additive inverse, scalar multiplication compatible với scalar multiplication, và distributive laws phải đúng.

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

Điểm của axioms không phải để memorize một danh sách. Chúng xác định minimum cấu trúc (structure / 구조) cần để algebra của tuyến tính (linear / 선형) combinations hoạt động đáng tin cậy.

## Tuyến tính (linear / 선형) combination: building khối (block / 블록) trung tâm

Cho vectors `v_1,...,v_k`, một tuyến tính (linear / 선형) combination là

```math
c_1v_1+c_2v_2+\cdots+c_kv_k,
```

trong đó `c_i` là scalars.

Mọi concept quan trọng trong chapter này đều xoay quanh câu hỏi: **những tuyến tính (linear / 선형) combinations nào có thể được tạo ra, và có bao nhiêu directions thực sự độc lập?**

Nếu ta có hai vectors trong `R^2`,

```math
v_1=(1,0),\qquad v_2=(0,1),
```

thì mọi véc-tơ (vector / 벡터) `(x,y)` có thể viết

```math
(x,y)=xv_1+yv_2.
```

Hai vectors đó đủ để generate toàn plane.

## Span: những gì ta có thể tạo ra

Span của một collection vectors là set của tất cả tuyến tính (linear / 선형) combinations:

```math
\operatorname{span}\{v_1,\ldots,v_k\}
=
\left\{\sum_{i=1}^k c_iv_i\;:\;c_i\in\mathbb F\right\}.
```

Span trả lời câu hỏi **reachability bằng tuyến tính (linear / 선형) combination**.

Trong `R^3`:

- một nonzero véc-tơ (vector / 벡터) span một line qua origin;
- hai nonparallel vectors span một plane qua origin;
- ba vectors phù hợp có thể span toàn `R^3`.

Nếu một dataset có tính năng (feature / 기능) vectors nằm gần một low-dimensional span, dimensionality reduction có thể compress dữ liệu (data / 데이터) bằng cách tìm basis thích hợp cho subspace đó.

## Tuyến tính (linear / 선형) dependence: khi có redundancy

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

Trong regression, nếu một tính năng (feature / 기능) là chính xác (exact / 정확한) tuyến tính (linear / 선형) combination của others, thiết kế (design / 설계) ma trận (matrix / 행렬) mất full column rank. Parameters có thể không unique. Trong cơ sở dữ liệu (database / 데이터베이스)/reporting, nếu một derived column hoàn toàn được determine bởi các columns khác, nó không thêm independent thông tin (information / 정보) theo tuyến tính (linear / 선형) sense.

## Basis: spanning mà không dư thừa

Một basis (Basis / 기저) của véc-tơ (vector / 벡터) không gian (space / 공간) `V` là collection vectors vừa:

1. linearly independent;
2. span toàn `V`.

Hai conditions này cùng nhau tạo ra một coordinate hệ thống (system / 시스템) tối thiểu: đủ để represent mọi véc-tơ (vector / 벡터), nhưng không có redundancy.

Tiêu chuẩn (standard / 표준) basis của `R^3` là

```math
e_1=(1,0,0),\quad e_2=(0,1,0),\quad e_3=(0,0,1).
```

Mọi véc-tơ (vector / 벡터)

```math
v=(x,y,z)
```

được viết uniquely:

```math
v=xe_1+ye_2+ze_3.
```

Tính **unique biểu diễn (representation / 표현)** này là consequence trực tiếp của independence + spanning.

Nếu biểu diễn (representation / 표현) không unique, basis vectors dependent. Nếu một số véc-tơ (vector / 벡터) không represent được, collection chưa span toàn không gian (space / 공간).

## Basis không phải duy nhất

Trong `R^2`, tiêu chuẩn (standard / 표준) basis

```math
(1,0),(0,1)
```

chỉ là một lựa chọn. Collection

```math
(1,1),(1,-1)
```

cũng là basis vì hai vectors independent và span plane.

Đối tượng (object / 객체) không đổi khi basis đổi. Chỉ coordinates của đối tượng (object / 객체) thay đổi.

Đây là một trong những mental shifts quan trọng nhất của tuyến tính (linear / 선형) algebra:

> coordinates không phải véc-tơ (vector / 벡터); chúng là description của véc-tơ (vector / 벡터) relative to a chosen basis.

## Thay đổi (change / 변경) of basis: cùng đối tượng (object / 객체), ngôn ngữ tọa độ khác

Giả sử basis `B={b_1,...,b_n}`. Một véc-tơ (vector / 벡터) `v` có coordinates

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

Nếu ma trận (matrix / 행렬)

```math
P=
\begin{bmatrix}
|&&|\\
b_1&\cdots&b_n\\
|&&|
\end{bmatrix},
```

thì tiêu chuẩn (standard / 표준) coordinates thỏa

```math
v=P[v]_B.
```

Nếu `P` invertible,

```math
[v]_B=P^{-1}v.
```

Thay đổi (change / 변경) of basis vì thế là ma trận (matrix / 행렬) transformation giữa hai coordinate descriptions của cùng abstract véc-tơ (vector / 벡터).

## Vì sao chọn basis tốt có thể thay đổi toàn bộ bài toán (problem / 문제)?

Một operator phức tạp trong tiêu chuẩn (standard / 표준) basis có thể trở nên diagonal trong eigenbasis. Một tín hiệu (signal / 신호) khó nhìn theo thời gian (time / 시간) samples có thể trở nên sparse theo Fourier basis. PCA chọn orthogonal directions sao cho variance được concentrate vào few components.

Đây không phải cosmetic coordinate thay đổi (change / 변경). biểu diễn (representation / 표현) phù hợp có thể biến computation từ coupled thành gần independent, làm mẫu (pattern / 패턴) rõ hơn và giảm dimension cần thiết.

## Dimension: số degrees of freedom độc lập

Dimension (Dimension / 차원) của finite-dimensional véc-tơ (vector / 벡터) không gian (space / 공간) là số vectors trong bất kỳ basis nào của không gian (space / 공간) đó.

Một theorem nền tảng bảo đảm mọi bases của cùng finite-dimensional không gian (space / 공간) có cùng number of vectors. Vì vậy dimension là thuộc tính (property / 속성) của không gian (space / 공간), không phải của basis cụ thể.

`R^2` dimension 2, `R^3` dimension 3.

Không gian (space / 공간) của polynomials degree at most 2,

```math
P_2=\{a+bx+cx^2\},
```

có basis

```math
\{1,x,x^2\}
```

nên dimension 3.

Không gian (space / 공간) của `2×2` real matrices có dimension 4 vì một ma trận (matrix / 행렬)

```math
\begin{bmatrix}
a&b\\
c&d
\end{bmatrix}
```

cần bốn independent coefficients.

Dimension không phải “số values đang lưu” một cách máy móc. Nó là số independent coordinates cần để specify arbitrary véc-tơ (vector / 벡터) trong không gian (space / 공간).

## Subspace: một tuyến tính (linear / 선형) universe nhỏ hơn bên trong không gian (space / 공간) lớn

Một subset `W⊆V` là subspace nếu nó tự đóng dưới véc-tơ (vector / 벡터) addition và scalar multiplication.

Một practical kiểm thử (test / 테스트) là:

- `0∈W`;
- nếu `u,v∈W` thì `u+v∈W`;
- nếu `v∈W` và scalar `c`, thì `cv∈W`.

Column không gian (space / 공간), row không gian (space / 공간), null không gian (space / 공간) và eigenspaces là các subspaces tự nhiên.

Một affine plane không đi qua origin không phải tuyến tính (linear / 선형) subspace, vì zero véc-tơ (vector / 벡터) không thuộc nó. Nó là translated subspace.

Distinction này giải thích vì sao equation homogeneous

```math
Ax=0
```

có solution set là subspace, còn

```math
Ax=b
```

với `b≠0` thường tạo affine set.

## Column không gian (space / 공간) và null không gian (space / 공간)

Cho ma trận (matrix / 행렬)

```math
A\in\mathbb R^{m\times n}.
```

Column không gian (space / 공간) là span của columns của `A`. Nó chứa mọi possible đầu ra (output / 출력) của transformation

```math
x\mapsto Ax.
```

Null không gian (space / 공간) là

```math
\mathcal N(A)=\{x:Ax=0\}.
```

Nó chứa đầu vào (input / 입력) directions mà transformation collapse về zero.

Hai spaces này trả lời hai questions khác nhau:

- transformation có thể tạo ra outputs nào?
- transformation làm mất những đầu vào (input / 입력) directions nào?

## Rank-nullity: accounting của dimensions

Một theorem trung tâm là

```math
\operatorname{rank}(A)+\operatorname{nullity}(A)=n,
```

với `A` có `n` columns.

`rank(A)` là dimension của column không gian (space / 공간). `nullity(A)` là dimension của null không gian (space / 공간).

Interpretation:

> đầu vào (input / 입력) không gian (space / 공간) có `n` degrees of freedom; một phần survive thành independent đầu ra (output / 출력) directions, phần còn lại bị collapse vào null không gian (space / 공간).

Ví dụ nếu `A:R^5→R^3` có rank 3, thì nullity là 2. Transformation giữ được ba independent directions và mất hai degrees of freedom.

Đây là một dạng conservation/accounting law cho tuyến tính (linear / 선형) thông tin (information / 정보).

## Coordinates như compression khi cấu trúc (structure / 구조) tồn tại

Nếu một đối tượng (object / 객체) sống trong high-dimensional ambient không gian (space / 공간) nhưng thực sự nằm trong lower-dimensional subspace, basis của subspace cho biểu diễn (representation / 표현) compact hơn.

Ví dụ ảnh (image / 이미지) 100×100 pixels có 10,000 raw dimensions, nhưng nếu dataset variation chủ yếu nằm gần một lower-dimensional manifold/subspace, PCA có thể represent phần lớn variance bằng vài hundred components.

Đây là lý do dimension reduction không chỉ là “xóa columns”. Nó tìm coordinate hệ thống (system / 시스템) nơi thông tin (information / 정보) relevant concentrate hơn.

## Orthogonal và orthonormal basis

Nếu basis vectors mutually orthogonal,

```math
b_i\cdot b_j=0\quad(i\ne j),
```

và mỗi véc-tơ (vector / 벡터) normalized,

```math
\|b_i\|=1,
```

basis gọi là orthonormal.

Với orthonormal basis, coefficient rất dễ tính:

```math
c_i=v\cdot b_i.
```

Không cần solve full hệ tuyến tính (linear system / 선형 시스템). Projection, least squares, Fourier coefficients và QR decomposition đều hưởng lợi từ orthogonality.

Orthonormal bases cũng thường numerically stable hơn vì basis vectors không gần dependent.

## Hàm (function / 함수) spaces: véc-tơ (vector / 벡터) spaces có thể vô hạn chiều

Tuyến tính (linear / 선형) algebra không dừng ở finite tuples. Consider không gian (space / 공간) của functions trên interval. Nếu `f` và `g` là functions, ta có

```math
(f+g)(x)=f(x)+g(x)
```

và

```math
(cf)(x)=cf(x).
```

Nhiều hàm (function / 함수) spaces là véc-tơ (vector / 벡터) spaces, thường infinite-dimensional.

Fourier phân tích (analysis / 분석) nhìn hàm (function / 함수) như combination của basis-like sinusoids. Quantum mechanics dùng Hilbert spaces. Differential equations thường tìm unknown hàm (function / 함수) trong một hàm (function / 함수) không gian (space / 공간) phù hợp.

Vì vậy idea basis/dimension mở đường từ elementary tuyến tính (linear / 선형) algebra sang phân tích (analysis / 분석) và mathematical physics.

## Tính năng (feature / 기능) không gian (space / 공간) trong machine học tập (learning / 학습)

Một mẫu (sample / 표본) có thể được represent thành tính năng (feature / 기능) véc-tơ (vector / 벡터)

```math
x=(x_1,\ldots,x_d).
```

`d` là ambient tính năng (feature / 기능) dimension, nhưng không nhất thiết intrinsic dimension của dữ liệu (data / 데이터).

Nếu features strongly correlated, effective thông tin (information / 정보) dimension có thể thấp hơn. Nếu một tính năng (feature / 기능) chính xác (exact / 정확한) combination của others, thiết kế (design / 설계) ma trận (matrix / 행렬) rank giảm.

Điều này nối trực tiếp tuyến tính (linear / 선형) independence, rank và conditioning với practical ML issues như multicollinearity.

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

Không gian (space / 공간) volume tăng cực nhanh theo dimension, nên fixed number dữ liệu (data / 데이터) points trở nên sparse.

Distance hình học (geometry / 기하학) cũng thay đổi. Trong many high-dimensional distributions, nearest và farthest distances có thể trở nên tương đối gần nhau; intuition từ 2D/3D không còn tốt.

Đây là lý do algorithms dựa trên cục bộ (local / 로컬) density hoặc nearest neighbors cần careful scaling, regularization, dimensionality reduction hoặc structural các giả định (assumptions / 가정들).

## Basis và biểu diễn (representation / 표현) trong software/dữ liệu (data / 데이터) các hệ thống (systems / 시스템들)

Cùng idea “choose coordinates” xuất hiện ngoài pure mathematics.

One-hot encoding chọn tiêu chuẩn (standard / 표준) basis-like biểu diễn (representation / 표현) cho categories. Embedding học một coordinate biểu diễn (representation / 표현) dense hơn. PCA chọn orthogonal basis từ covariance cấu trúc (structure / 구조). Fourier transform đổi từ thời gian (time / 시간)/mẫu (sample / 표본) coordinates sang frequency coordinates. Wavelets chọn localized multi-scale basis.

Không phải mọi biểu diễn (representation / 표현) là literal tuyến tính (linear / 선형) basis, nhưng mô hình tư duy (mental model / 사고 모델) giống nhau: **cùng đối tượng (object / 객체) có thể dễ hiểu hơn trong coordinate hệ thống (system / 시스템) phù hợp**.

## Khi tuyến tính (linear / 선형) không gian (space / 공간) mô hình (model / 모델) không đủ

Véc-tơ (vector / 벡터) không gian (space / 공간) giả định closure dưới arbitrary scalar multiplication và addition. Nhiều real-world sets không thỏa.

Xác suất (probability / 확률) distributions không thể cộng arbitrary coefficients rồi vẫn là valid xác suất (probability / 확률) phân phối (distribution / 분포). Rotations form a group, không phải véc-tơ (vector / 벡터) không gian (space / 공간) dưới ma trận (matrix / 행렬) addition. Points trên sphere không đóng dưới addition.

Trong các trường hợp đó, forcing vector-space intuition có thể gây sai. Ta có thể cần affine spaces, manifolds, groups, cones hoặc xác suất (probability / 확률) simplices.

Biết khi nào tuyến tính (linear / 선형) cấu trúc (structure / 구조) không phù hợp cũng quan trọng như biết dùng nó.

## Liên kết kiến thức (knowledge connection / 지식 연결) — basis và eigenvectors

Nếu tuyến tính (linear / 선형) operator `A` có đủ independent eigenvectors, chúng tạo basis `P` và

```math
A=PDP^{-1}.
```

Trong eigenbasis, operator trở thành diagonal scaling. Đây là ultimate example của “choose basis to expose cấu trúc (structure / 구조)”.

Nếu ma trận (matrix / 행렬) defective và không có đủ eigenvectors, diagonal basis không tồn tại; ta cần richer structures như Jordan form. Vì vậy basis availability ảnh hưởng trực tiếp cách ta simplify transformation.

## Liên kết kiến thức (knowledge connection / 지식 연결) — basis và Fourier

Sine/cosine hoặc complex exponentials đóng vai trò basis functions cho nhiều tín hiệu (signal / 신호) spaces. Time-domain waveform có thể được represent bằng coefficients theo frequency components.

Cùng tín hiệu (signal / 신호) không thay đổi; chỉ coordinate ngôn ngữ (language / 언어) đổi. Một convolution khó nhìn trong thời gian (time / 시간) lĩnh vực (domain / 도메인) có thể trở thành multiplication đơn giản trong frequency lĩnh vực (domain / 도메인).

Đây là lý do basis không phải một khái niệm abstract tách khỏi kỹ thuật (engineering / 엔지니어링) — nó quyết định biểu diễn (representation / 표현) nơi thao tác (operation / 연산) trở nên đơn giản.

## Mô hình tư duy (mental model / 사고 모델)

> véc-tơ (vector / 벡터) không gian (space / 공간) là một universe của những objects có thể được kết hợp tuyến tính. Span hỏi “ta tạo được những gì?”, independence hỏi “có redundancy không?”, basis là vocabulary tối thiểu đủ để diễn đạt mọi véc-tơ (vector / 벡터), còn dimension là số degrees of freedom độc lập. Đổi basis không đổi đối tượng (object / 객체); nó đổi ngôn ngữ mô tả đối tượng (object / 객체), và một ngôn ngữ tốt có thể làm cấu trúc (structure / 구조) ẩn trở nên hiển nhiên.

## Dùng chung (common / 공통) Misconceptions

**“véc-tơ (vector / 벡터) không gian (space / 공간) nghĩa là không gian hình học có mũi tên.”** Không. Polynomials, functions và matrices cũng có thể là vectors nếu operations thỏa vector-space axioms.

**“Basis là duy nhất.”** Basis có thể có vô số lựa chọn. Dimension mới là bất biến (invariant / 불변식).

**“Có nhiều coordinates nghĩa là có nhiều independent thông tin (information / 정보).”** Không. Coordinates/features có thể linearly dependent. Rank đo independent tuyến tính (linear / 선형) directions, không phải raw column count.

**“Mọi plane trong `R^3` là subspace.”** Chỉ plane đi qua origin mới là tuyến tính (linear / 선형) subspace. Plane translated khỏi origin là affine set.

**“High dimension luôn tốt vì chứa nhiều thông tin (information / 정보).”** Higher ambient dimension có thể chỉ thêm redundancy/noise và làm estimation khó hơn. giá trị (value / 값) nằm ở independent, relevant cấu trúc (structure / 구조) chứ không phải dimension count tự thân.

> **Bàn giao:** Sau **dùng chung (common / 공통) Misconceptions**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 vectors](./00_vectors.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
