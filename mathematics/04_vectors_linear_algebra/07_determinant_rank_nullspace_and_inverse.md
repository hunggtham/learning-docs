# Determinant, rank, null space và nghịch đảo ma trận

Một matrix không chỉ là bảng số. Nó biểu diễn linear transformation. Khi nhìn như vậy, determinant, rank, null space và inverse trở thành các câu trả lời cho bốn câu hỏi khác nhau: transformation scale volume thế nào, giữ lại bao nhiêu dimensions, làm mất directions nào, và có thể undo hay không.

## Determinant là hệ số scale có hướng của volume

Với matrix vuông `A`, determinant (Determinant / 행렬식) là scalar `det(A)`.

Trong 2D, nếu columns của

```math
A=\begin{bmatrix}a&b\\c&d\end{bmatrix}
```

là hai vectors, area của parallelogram chúng sinh ra có magnitude

```math
|ad-bc|.
```

Do đó

```math
\det(A)=ad-bc.
```

Dấu của determinant encode orientation. Determinant dương giữ orientation, âm đảo orientation, và bằng 0 nghĩa area/volume collapse xuống dimension thấp hơn.

## Vì sao determinant bằng 0 quan trọng?

Nếu

```math
\det(A)=0,
```

transformation làm mất ít nhất một direction. Hai input khác nhau có thể map tới cùng output. Khi information bị mất, không thể có unique inverse.

Do đó với square matrix:

```math
A^{-1}\text{ tồn tại}\iff \det(A)\neq0.
```

Điều này không nên học như theorem tách rời. Nó là cùng một statement nhìn từ geometry và algebra: no volume collapse ↔ no lost direction ↔ one-to-one ↔ invertible.

## Rank đo số dimensions thực sự còn lại

Rank (Rank / 계수, 랭크) của matrix là dimension của column space, đồng thời bằng dimension của row space.

Nếu matrix `A` map từ `\mathbb R^n` sang `\mathbb R^m`, rank cho biết output có thể trải rộng trên bao nhiêu independent directions.

Ví dụ một 3D transformation ép mọi points xuống một plane có rank 2. Ép mọi points xuống một line có rank 1.

Rank không nhất thiết bằng số rows hoặc columns; nó đo independent structure, không đo kích thước storage.

## Null space là tập directions bị xóa

Null space (Kernel / 영공간, 핵) là

```math
\mathcal N(A)=\{x:Ax=0\}.
```

Nếu tồn tại `x\neq0` với `Ax=0`, transformation biến một nonzero direction thành zero. Khi đó `A` không injective.

Nullity là dimension của null space. Rank–nullity theorem nói

```math
\operatorname{rank}(A)+\operatorname{nullity}(A)=n,
```

với `n` là số columns, tức dimension của input space.

Đây là conservation law của dimensions: input dimensions hoặc sống sót trong image, hoặc biến mất vào kernel.

## Row reduction và pivots

Gaussian elimination biến matrix thành row-echelon form bằng elementary row operations. Các operations này không thay solution set của system theo cách mất kiểm soát.

Pivot columns xác định independent directions. Số pivots bằng rank. Free variables tương ứng với degrees of freedom trong null space.

Do đó row reduction không chỉ để “giải hệ”. Nó là công cụ nhìn structure của linear map.

## Inverse matrix

Nếu `A` invertible, tồn tại `A^{-1}` sao cho

```math
A^{-1}A=AA^{-1}=I.
```

Với system

```math
Ax=b,
```

formally ta có

```math
x=A^{-1}b.
```

Nhưng trong numerical computing, ta thường **không tính inverse explicit** chỉ để solve system. Factorizations như LU, QR hoặc iterative solvers thường hiệu quả và ổn định hơn.

Inverse là concept quan trọng; explicit inverse không luôn là implementation tốt.

## Determinant và change of variables

Trong calculus nhiều biến, nếu transformation thay coordinates bằng `x=T(u)`, local volume element scale theo absolute determinant của Jacobian:

```math
dx=|\det J_T(u)|\,du.
```

Lý do hình học chính là determinant đo local volume scaling. Đây là bridge trực tiếp giữa linear algebra và multiple integrals.

## Rank trong data và machine learning

Một data matrix có low rank khi nhiều features thực chất phụ thuộc vào ít latent directions. PCA tìm principal directions để approximate data bằng lower-dimensional subspace. Matrix factorization trong recommender systems dựa trên giả thuyết rằng user–item interactions có underlying low-dimensional structure.

Rank cũng liên hệ đến identifiability: nếu design matrix thiếu full column rank, parameters của linear model không thể được xác định duy nhất.

## Conditioning khác singularity

Matrix có determinant khác 0 có thể vẫn gần singular. Khi smallest singular value rất nhỏ, một perturbation nhỏ ở input có thể gây change lớn ở solution.

Condition number đo sensitivity này. Vì vậy “invertible” là statement yes/no; “well-conditioned” là statement định lượng về reliability.

## Knowledge Connection

Determinant nối geometry volume với Jacobian. Rank nối dimensions với degrees of freedom. Null space nối lost information với non-uniqueness. Inverse nối solving systems với reversible transformations. SVD cung cấp view thống nhất: singular values cho biết transformation stretch từng orthogonal direction bao nhiêu, và zero singular values trực tiếp biểu lộ rank loss.

## Mental Model

> Hãy nhìn matrix như một cỗ máy biến đổi không gian. Determinant hỏi máy scale volume bao nhiêu; rank hỏi còn bao nhiêu dimensions độc lập; null space hỏi directions nào bị xóa; inverse hỏi liệu có thể chạy máy ngược để khôi phục input hay không.

## Common Misconceptions

Determinant không phải “một số để kiểm tra inverse” בלבד; ý nghĩa geometry là volume scaling và orientation. Rank không phải số nonzero entries. `A^{-1}b` là notation đúng nhưng không có nghĩa nên tính explicit inverse trong code. Determinant rất nhỏ không tự động nói matrix ill-conditioned nếu scale chưa được xét; singular values/condition number cho picture tốt hơn.
