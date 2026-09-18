# Inner product, trực giao và phép chiếu

Dot product ở `R^n` không chỉ là cách nhân hai vectors để nhận một scalar. Nó tạo ra geometry: length, angle, perpendicularity và projection đều xuất hiện từ một structure chung gọi là **inner product (Tích trong / 내적)**.

## Từ dot product đến angle

Trong Euclidean coordinates,

```math
u\cdot v=\sum_{i=1}^n u_iv_i.
```

Geometric relation là

```math
u\cdot v=\|u\|\|v\|\cos\theta.
```

Vì vậy nếu `u,v` là nonzero:

```math
\cos\theta=\frac{u\cdot v}{\|u\|\|v\|}.
```

Khi `u·v=0`, angle là 90°, nên vectors trực giao.

Trong machine learning và information retrieval, cosine similarity dùng chính normalized dot product để so direction của embedding vectors. Hai vectors có magnitude rất khác vẫn có thể biểu diễn pattern tương tự nếu angle nhỏ.

## Norm từ inner product

Độ dài Euclidean là

```math
\|x\|=\sqrt{x\cdot x}.
```

Vì vậy distance giữa `x` và `y` là

```math
\|x-y\|.
```

Pythagoras mở rộng trực tiếp: nếu `u\cdot v=0`, thì

```math
\|u+v\|^2=\|u\|^2+\|v\|^2.
```

Derivation:

```math
\|u+v\|^2=(u+v)\cdot(u+v)
```

```math
=u\cdot u+2u\cdot v+v\cdot v.
```

Khi `u\cdot v=0`, cross term biến mất.

Đây chính là định lý Pythagoras trong ngôn ngữ vector.

## Trực giao không chỉ là “vuông góc hình học”

Hai vectors trực giao (Orthogonal / 직교) khi

```math
u\cdot v=0.
```

Khái niệm này mở rộng sang functions. Ví dụ trong một function space, ta có thể định nghĩa inner product

```math
\langle f,g\rangle=\int_a^b f(x)g(x)\,dx.
```

Khi integral bằng 0, hai functions được coi là orthogonal. Fourier series hoạt động vì sine/cosine ở các frequencies phù hợp tạo một orthogonal basis.

## Projection lên một vector

Muốn tìm component của vector `v` theo direction `u`, ta tìm scalar `c` sao cho `cu` gần `v` nhất.

Ta minimize

```math
\|v-cu\|^2.
```

Khai triển:

```math
(v-cu)\cdot(v-cu)=v\cdot v-2c(v\cdot u)+c^2(u\cdot u).
```

Derivative theo `c`:

```math
-2(v\cdot u)+2c(u\cdot u)=0.
```

Suy ra

```math
c=\frac{v\cdot u}{u\cdot u}.
```

Do đó projection vector là

```math
\operatorname{proj}_u(v)=\frac{v\cdot u}{u\cdot u}u.
```

Nếu `u` là unit vector, denominator bằng 1.

Điểm quan trọng: projection không phải arbitrary formula. Nó là **nearest point problem**.

## Projection lên subspace và least squares

Cho matrix `A` có columns sinh ra subspace `C(A)`. Ta muốn approximate vector `b` bằng một vector trong column space:

```math
Ax\approx b.
```

Best least-squares solution làm residual

```math
r=b-Ax
```

vuông góc với mọi column của `A`. Vì vậy

```math
A^Tr=0.
```

Thay `r`:

```math
A^T(b-Ax)=0.
```

Suy ra normal equations:

```math
A^TAx=A^Tb.
```

Đây là nền hình học của linear regression: predicted vector là orthogonal projection của observed data lên model subspace.

## Orthonormal basis

Một basis `{q_1,...,q_n}` là orthonormal nếu mỗi vector có norm 1 và các vectors khác nhau trực giao:

```math
q_i\cdot q_j=
\begin{cases}
1 & i=j,\\
0 & i\neq j.
\end{cases}
```

Khi basis orthonormal, coordinates cực kỳ đơn giản:

```math
x=\sum_i (x\cdot q_i)q_i.
```

Ta không cần giải system để tìm coefficients; mỗi coefficient chỉ là một projection.

## Gram–Schmidt

Nếu có independent vectors nhưng chưa orthogonal, Gram–Schmidt tạo orthogonal basis bằng cách lần lượt loại bỏ components theo directions đã xử lý.

Với `v_1,v_2`, đặt

```math
u_1=v_1,
```

```math
u_2=v_2-\operatorname{proj}_{u_1}(v_2).
```

`u_2` đã loại component theo `u_1`, nên `u_1\cdot u_2=0`. Normalize các `u_i` để có orthonormal vectors.

QR decomposition là matrix version của ý tưởng này và được dùng rộng rãi trong numerical linear algebra.

## Knowledge Connection

Projection nối Pythagoras với regression, PCA, computer graphics và signal filtering. Orthogonality nối geometry với Fourier basis. Dot product nối vector angle với cosine similarity trong embeddings. Least squares là bài toán “nearest point in a subspace”, không chỉ là một công thức thống kê.

## Mental Model

> Inner product là máy đo alignment. Orthogonality nghĩa hai directions không chia sẻ component theo metric đang dùng. Projection là giữ lại phần của một object nằm trong một subspace và bỏ phần vuông góc còn lại.

## Common Misconceptions

Dot product không phải vector; nó trả scalar. Orthogonal không đồng nghĩa independent trong mọi trường hợp nếu có zero vector; một tập orthogonal các vector khác 0 thì independent. Projection lên `u` phụ thuộc direction chứ không phụ thuộc magnitude của `u` vì hệ số tự bù. Normal equations là nền lý thuyết tốt nhưng trong numerical computation thường QR hoặc SVD ổn định hơn.
