# Ma trận và hệ phương trình tuyến tính

Ma trận (Matrix / 행렬) thường được giới thiệu như bảng numbers, nhưng đó chỉ là representation. Trong linear algebra, matrix quan trọng vì nó có thể encode một linear transformation hoặc một hệ linear constraints.

## Matrix notation

Một `m×n` matrix có `m` rows và `n` columns:

```math
A=
\begin{bmatrix}
a_{11}&\cdots&a_{1n}\\
\vdots&\ddots&\vdots\\
a_{m1}&\cdots&a_{mn}
\end{bmatrix}
```

Matrix-vector product với `x∈R^n` tạo vector trong `R^m`:

```math
Ax
```

Mỗi output component là dot product của một row với input vector.

## Hệ phương trình dưới dạng Ax=b

System

```math
\begin{cases}
2x+y=5\\
x-y=1
\end{cases}
```

viết thành

```math
\begin{bmatrix}2&1\\1&-1\end{bmatrix}
\begin{bmatrix}x\\y\end{bmatrix}
=
\begin{bmatrix}5\\1\end{bmatrix}
```

Matrix gom coefficients; vector `x` gom unknowns; `b` gom targets.

## Row operations

Gaussian elimination dùng ba elementary row operations: swap rows, multiply a row bởi nonzero scalar, và add multiple của one row vào another. Những operations này bảo toàn solution set vì chúng tương ứng transformations reversible của equations.

Mục tiêu là đưa matrix về echelon form để relationships giữa variables lộ rõ.

## Unique, none, infinite solutions

Geometric interpretation: mỗi linear equation trong 2D là line, trong 3D là plane, trong higher dimensions là hyperplane. System solution là intersection.

Algebraically, inconsistency xuất hiện row dạng

```math
[0\ 0\ \cdots\ 0\mid c],\qquad c\ne0
```

nghĩa `0=c`, impossible.

Free variables xuất hiện khi không đủ independent constraints, tạo infinitely many solutions.

## Matrix multiplication

Nếu `A` map `R^n→R^m` và `B` map `R^p→R^n`, composition `A(Bx)` được encode bởi product `AB`.

Vì composition order quan trọng, matrix multiplication thường không commutative:

```math
AB\ne BA
```

Rotation rồi scale có thể khác scale rồi rotation nếu scale không uniform.

## Identity và inverse

Identity matrix `I` giữ vector nguyên:

```math
Ix=x
```

Nếu square matrix `A` có inverse `A^{-1}`:

```math
A^{-1}A=AA^{-1}=I
```

thì solution của `Ax=b` là

```math
x=A^{-1}b
```

về lý thuyết. Trong numerical computing, thường không tính inverse explicit để solve system vì factorization methods ổn định và hiệu quả hơn.

## Determinant intuition

Determinant (Determinant / 행렬식) của square matrix đo signed volume scaling của transformation. Trong 2D, `|det A|` là area scale factor; trong 3D là volume scale factor.

Nếu

```math
\det A=0
```

transformation collapse space vào lower dimension, nên information bị mất và inverse không tồn tại.

Điều này giải thích connection giữa zero determinant, linearly dependent columns và non-invertibility.

## Data matrix

Trong data science, matrix thường chứa samples×features. Nhưng orientation convention có thể đổi theo library. Matrix multiplication trở thành batch application của linear combinations, nền của neural network layers:

```math
z=Wx+b
```

## Mental Model

> Matrix là một operator được viết bằng coordinates. Hệ `Ax=b` hỏi input nào qua transformation A tạo ra b; Gaussian elimination thay representation của constraints để câu trả lời lộ ra.

## Common Misconceptions

Matrix multiplication không phải elementwise multiplication. `A^{-1}` không phải reciprocal từng element. Determinant không chỉ là công thức để nhớ; nó đo volume scaling và cho biết transformation có collapse dimension hay không.
