# Phép biến đổi tuyến tính

Phép biến đổi tuyến tính (Linear transformation / 선형변환) là mapping `T` bảo toàn hai operations nền của vector spaces:

```math
T(u+v)=T(u)+T(v)
```

và

```math
T(cu)=cT(u)
```

Hai properties gộp thành

```math
T(au+bv)=aT(u)+bT(v)
```

## Vì sao linearity mạnh?

Nếu biết `T` làm gì với basis vectors, ta biết `T` làm gì với mọi vector. Nếu

```math
x=x_1e_1+\cdots+x_ne_n
```

thì

```math
T(x)=x_1T(e_1)+\cdots+x_nT(e_n)
```

Do đó một finite-dimensional linear transformation được xác định hoàn toàn bởi images của basis vectors. Đặt các images làm columns tạo matrix representation.

## Matrix columns có nghĩa gì?

Với matrix `A`, column thứ `j` chính là

```math
Ae_j
```

— nơi basis vector `e_j` bị gửi tới. Đây là mental model tốt hơn việc nhìn matrix như table coefficients vô nghĩa.

## Linear combination

`Ax` là linear combination của columns của `A`, weights là components của `x`:

```math
Ax=x_1a_1+\cdots+x_na_n
```

Vì vậy equation `Ax=b` hỏi: `b` có viết được như combination của columns không? Nếu có, coefficients chính là solution vector `x`.

## Kernel/null space

Kernel:

```math
\ker T=\{x:T(x)=0\}
```

là set directions bị transformation collapse về zero. Nếu kernel chỉ `{0}`, transformation injective.

Trong matrix form, null space giải

```math
Ax=0
```

Nonzero null vector nghĩa có information direction bị mất.

## Image/column space

Image của transformation là set outputs có thể đạt:

```math
\operatorname{Im}T=\{T(x)\}
```

Với matrix, đó là span của columns. `Ax=b` solvable iff `b` nằm trong column space.

## Rank-nullity

Nếu `T:V→W` với `V` finite-dimensional:

```math
\dim V=\operatorname{rank}T+\operatorname{nullity}T
```

Input dimensions được chia giữa directions sống sót trong output và directions bị collapse.

Đây là conservation-like counting principle của linear transformations.

## Affine layer trong neural networks

Layer

```math
z=Wx+b
```

không strictly linear nếu `b≠0`; nó là affine transformation. Sau activation nonlinear, composition trở thành nonlinear network. Terminology “linear layer” trong frameworks thường dùng informal cho affine map.

## Coordinate change

Cùng transformation có matrix khác dưới basis khác. Matrix không phải transformation intrinsically; nó là coordinates của transformation relative to chosen bases.

Điều này rất quan trọng trong eigenbasis/PCA/Fourier: đổi basis có thể làm operator đơn giản hơn.

## Mental Model

> Linear transformation là machine tôn trọng superposition. Matrix chỉ là bảng coordinates mô tả machine đó trong một basis. Basis tốt có thể làm cùng machine trở nên dễ hiểu hơn rất nhiều.

## Common Misconceptions

Mọi function có matrix-looking coefficients không nhất thiết linear nếu có translation/nonlinear term. Matrix và transformation không hoàn toàn cùng object. `rank` đo số output directions độc lập, không đơn giản là số rows/columns.
