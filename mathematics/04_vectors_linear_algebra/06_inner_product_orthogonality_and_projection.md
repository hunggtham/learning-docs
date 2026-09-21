# Inner product, trực giao và phép chiếu: geometry từ một phép đo alignment

Dot product trong `\mathbb R^n` thường được học như một công thức:

```math
u\cdot v=\sum_i u_iv_i.
```

Nhưng ý nghĩa sâu hơn là: nó tạo ra geometry. Từ một inner product, ta có length, angle, perpendicularity, projection, orthogonal basis và least squares.

Vì vậy chapter này nên được đọc như một chuỗi dependency:

```text
inner product
→ norm
→ angle
→ orthogonality
→ projection
→ orthogonal decomposition
→ least squares
→ QR / Fourier / PCA
```

## 1. Inner product là generalized notion của alignment

Trong Euclidean space:

```math
\langle u,v\rangle=u^Tv.
```

Một inner product abstract cần thỏa các properties như linearity, symmetry/conjugate symmetry và positive definiteness.

Trên real vector space:

```math
\langle u,v\rangle=\langle v,u\rangle
```

và

```math
\langle v,v\rangle>0
```

cho mọi `v\ne0`.

Điều này cho phép định nghĩa geometry mà không phụ thuộc vào coordinate representation cụ thể.

## 2. Norm xuất hiện từ self-alignment

Length được định nghĩa bởi

```math
\|v\|=\sqrt{\langle v,v\rangle}.
```

Distance:

```math
d(u,v)=\|u-v\|.
```

Pythagoras chỉ là một consequence của inner product structure.

Nếu

```math
\langle u,v\rangle=0,
```

thì

```math
\|u+v\|^2
=\|u\|^2+\|v\|^2.
```

Derivation:

```math
\|u+v\|^2
=\langle u+v,u+v\rangle
```

```math
=\|u\|^2+2\langle u,v\rangle+\|v\|^2.
```

Cross term biến mất khi vectors orthogonal.

## 3. Cauchy–Schwarz là theorem làm angle hợp lệ

Ta muốn define

```math
\cos\theta=
\frac{\langle u,v\rangle}
{\|u\|\|v\|}.
```

Để expression nằm trong `[-1,1]`, cần theorem:

```math
|\langle u,v\rangle|
\le
\|u\|\|v\|.
```

Đây là bất đẳng thức Cauchy–Schwarz (Cauchy–Schwarz inequality / 코시-슈바르츠 부등식).

Proof idea: norm luôn nonnegative. Xét

```math
\|u-tv\|^2\ge0
```

như một quadratic theo `t`. Discriminant không thể dương theo cách tạo giá trị âm, dẫn tới Cauchy–Schwarz.

Theorem này không chỉ technical; nó bảo đảm notion cosine/angle consistent.

## 4. Orthogonality là independence theo geometry đang chọn

Hai vectors trực giao khi

```math
\langle u,v\rangle=0.
```

Nếu một set gồm các nonzero mutually orthogonal vectors, set đó linearly independent.

Proof idea: nếu

```math
c_1v_1+\cdots+c_kv_k=0,
```

inner product hai vế với `v_j`:

```math
c_j\|v_j\|^2=0,
```

nên `c_j=0`.

Orthogonality làm coefficients tách rời nhau rất mạnh.

## 5. Projection là nearest-point problem

Muốn approximate `v` bằng vector trên line span bởi `u`:

```math
cu.
```

Ta minimize

```math
\|v-cu\|^2.
```

Điều kiện optimum cho

```math
c=
\frac{\langle v,u\rangle}
{\langle u,u\rangle}.
```

Do đó

```math
\operatorname{proj}_u(v)
=
\frac{\langle v,u\rangle}
{\langle u,u\rangle}u.
```

Nếu `u` unit length:

```math
\operatorname{proj}_u(v)=\langle v,u\rangle u.
```

Projection formula không phải arbitrary formula; nó là solution của **closest point in a subspace**.

## 6. Orthogonal decomposition

Ta có thể viết

```math
v=v_{\parallel}+v_{\perp}
```

với

```math
v_{\parallel}=\operatorname{proj}_U(v)
```

và

```math
v_{\perp}=v-v_{\parallel}.
```

Điều kiện:

```math
v_{\perp}\perp U.
```

Mental model:

```text
vector = explainable component + residual component
```

Đây chính là geometry của regression.

## 7. Projection theorem trên subspace

Nếu `U` là finite-dimensional subspace trong Euclidean space, mỗi vector `v` có unique decomposition:

```math
v=u+r,
```

với

```math
u\in U,
\qquad
r\in U^\perp.
```

`u` là unique point trong `U` gần `v` nhất.

Điều này giải thích vì sao least squares solution có residual orthogonal với column space.

## 8. Least squares là projection, không phải regression trick

Cho system overdetermined:

```math
Ax\approx b.
```

Outputs reachable bởi model nằm trong column space:

```math
\mathcal C(A).
```

Ta chọn `\hat x` để

```math
A\hat x
```

là projection của `b` lên `\mathcal C(A)`.

Residual:

```math
r=b-A\hat x
```

phải orthogonal với every column của `A`:

```math
A^Tr=0.
```

Suy ra:

```math
A^TA\hat x=A^Tb.
```

Normal equations là consequence của orthogonality.

## 9. Vì sao orthonormal basis đặc biệt?

Basis `q_1,\ldots,q_n` orthonormal nếu

```math
\langle q_i,q_j\rangle
=
\begin{cases}
1&i=j\\
0&i\ne j.
\end{cases}
```

Khi đó coordinates của `x` chỉ là projections:

```math
x=
\sum_i
\langle x,q_i\rangle q_i.
```

Không cần solve general linear system.

Matrix `Q` với orthonormal columns thỏa:

```math
Q^TQ=I.
```

Do đó norm được bảo toàn:

```math
\|Qx\|=\|x\|.
```

Orthogonal matrices là geometry-preserving transforms.

## 10. Gram–Schmidt: remove explained components

Bắt đầu independent vectors `v_1,\ldots,v_k`.

Set:

```math
u_1=v_1.
```

Sau đó:

```math
u_2=v_2-
\operatorname{proj}_{u_1}(v_2).
```

General:

```math
u_j
=
v_j-
\sum_{i<j}
\operatorname{proj}_{u_i}(v_j).
```

Ta liên tục trừ đi components đã được explain bởi previous directions.

Normalize:

```math
q_i=\frac{u_i}{\|u_i\|}.
```

Đây là conceptual foundation của QR decomposition.

## 11. Classical Gram–Schmidt vs numerical stability

Trong exact arithmetic, Gram–Schmidt đẹp.

Trong floating point, classical Gram–Schmidt có thể mất orthogonality khi vectors gần linearly dependent.

Modified Gram–Schmidt hoặc Householder QR thường numerically stable hơn.

Đây là distinction quan trọng:

```text
mathematically equivalent
≠ numerically equivalent
```

## 12. Inner product không nhất thiết là ordinary dot product

Ta có thể define weighted inner product:

```math
\langle x,y\rangle_M=x^TMy
```

với `M` symmetric positive definite.

Khi đó geometry thay đổi: angle, norm và “nearest” đều phụ thuộc `M`.

Mahalanobis distance trong statistics:

```math
d(x,\mu)^2
=(x-\mu)^T\Sigma^{-1}(x-\mu)
```

là Euclidean-like geometry sau khi account covariance scaling.

## 13. Function spaces cũng có inner product

Ví dụ:

```math
\langle f,g\rangle
=
\int_a^b f(x)g(x)\,dx.
```

Functions orthogonal nếu integral product bằng zero.

Sine/cosine functions ở appropriate frequencies tạo orthogonal family.

Fourier coefficients là projections:

```text
signal
→ project onto frequency basis
→ coefficients
```

Fourier analysis vì vậy là linear algebra trong infinite-dimensional function space.

## 14. Cosine similarity và embeddings

Cosine similarity:

```math
\cos\theta
=
\frac{x^Ty}{\|x\|\|y\|}.
```

Nó bỏ magnitude và đo directional alignment.

Trong embedding space, interpretation phụ thuộc model training geometry. High cosine similarity không universal đồng nghĩa “semantically same”; nó chỉ nói representation vectors align theo metric được chọn.

## 15. Projection matrix

Nếu columns của `Q` orthonormal span subspace `U`, projection matrix là

```math
P=QQ^T.
```

Properties:

```math
P^2=P
```

(idempotent) và

```math
P^T=P
```

(symmetric).

`P^2=P` có meaning: project lần hai không thay gì thêm.

Nếu `A` full column rank nhưng columns chưa orthonormal:

```math
P=A(A^TA)^{-1}A^T.
```

Trong implementation, thường không form expression này explicit nếu numerical stability quan trọng.

## 16. Pythagorean energy decomposition

Nếu

```math
v=u+r,
\qquad u\perp r,
```

thì

```math
\|v\|^2=\|u\|^2+\|r\|^2.
```

Trong regression:

```text
signal explained by model + residual
```

có geometric decomposition liên quan sum of squares dưới assumptions/setup phù hợp.

Trong signal processing, orthogonal basis cũng cho energy decomposition.

## 17. PCA connection

PCA tìm directions orthonormal sao cho projected variance lớn nhất sequentially.

First principal component solve conceptually:

```math
\max_{\|u\|=1}
\operatorname{Var}(Xu).
```

Projection lên low-dimensional principal subspace giữ lại nhiều squared energy/variance nhất theo criterion PCA.

Orthogonality làm selected directions không redundant theo Euclidean geometry.

## 18. Physics connection

Work:

```math
W=F\cdot d
```

chỉ component của force theo displacement đóng góp.

Projection giải thích trực tiếp:

```text
force perpendicular to motion → zero work contribution
```

Inner product là “alignment multiplier”.

## 19. Proof idea: best projection vì residual orthogonal

Giả sử `p` là projection của `v` lên subspace `U`, residual `r=v-p` orthogonal `U`.

Cho bất kỳ `u\in U`:

```math
v-u=(v-p)+(p-u)=r+(p-u).
```

Hai terms orthogonal, nên Pythagoras:

```math
\|v-u\|^2
=\|r\|^2+\|p-u\|^2
\ge\|r\|^2.
```

Equality chỉ khi `u=p`.

Đây là proof hình học rằng projection là nearest point.

## 20. Assumptions và metric choice

Projection phụ thuộc inner product.

Nếu feature scales khác nhau mạnh, ordinary Euclidean inner product có thể tạo geometry không phù hợp.

Standardization, whitening hoặc weighted metrics không chỉ preprocessing cosmetic; chúng thay notion length, angle và nearest point.

## Knowledge Connection

Inner product nối:

```text
Pythagoras
→ norm / angle
→ orthogonality
→ projection
→ least squares
→ QR
→ Fourier
→ PCA
→ cosine similarity
→ weighted statistical geometry
```

## Mental Model

> Inner product là **máy đo alignment**. Orthogonality nghĩa “không share component” theo geometry đã chọn. Projection là **best approximation trong một subspace**. Least squares, Fourier coefficients, PCA và nhiều regression methods đều là các phiên bản của cùng một câu hỏi: phần nào của object nằm trong space ta có thể represent?

## Common Misconceptions

Orthogonality phụ thuộc inner product, không phải một notion tuyệt đối trong mọi geometry. Zero vector orthogonal với mọi vector nhưng không thể normalize. Normal equations đúng về lý thuyết nhưng có thể kém ổn định hơn QR/SVD. Cosine similarity bỏ magnitude nhưng không xóa mọi bias của representation. Gram–Schmidt trong exact math và floating-point implementation không có cùng numerical behavior.