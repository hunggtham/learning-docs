# Ma trận và hệ phương trình tuyến tính

Ma trận (matrix / 행렬) thường được nhìn thấy lần đầu như một bảng số, nhưng cách nhìn đó quá yếu để học linear algebra lâu dài. Một ma trận nên được hiểu đồng thời theo hai vai trò: nó mô tả **một hệ ràng buộc tuyến tính** và nó biểu diễn **một phép biến đổi tuyến tính** trong một hệ tọa độ cụ thể. Hai góc nhìn này gặp nhau trong phương trình

```math
Ax=b.
```

Nếu nhìn từ systems of equations, `A` chứa coefficients, `x` là unknown state và `b` là target. Nếu nhìn từ transformations, `A` là một operator nhận input `x` và tạo output `b`. Câu hỏi “giải hệ” vì vậy trở thành: **input nào khi đi qua transformation `A` tạo ra output mong muốn `b`?**

## Tại sao linear systems xuất hiện khắp nơi?

Nhiều bài toán thực tế có dạng nhiều quantities liên hệ gần tuyến tính trong một vùng làm việc. Kirchhoff laws trong circuits tạo systems của currents và voltages. Static equilibrium trong mechanics tạo systems từ force balance. Calibration, localization, regression, portfolio constraints, network flow approximations và numerical PDE đều dẫn đến những equations nơi nhiều unknowns bị ràng buộc đồng thời.

Ví dụ:

```math
\begin{cases}
2x+y=5\\
x-y=1
\end{cases}
```

có thể viết thành

```math
\begin{bmatrix}
2&1\\
1&-1
\end{bmatrix}
\begin{bmatrix}
x\\y
\end{bmatrix}
=
\begin{bmatrix}
5\\1
\end{bmatrix}.
```

Viết `Ax=b` không chỉ để ngắn hơn. Nó làm lộ structure chung của hàng nghìn problems tưởng như khác nhau.

## Matrix-vector product thực sự làm gì?

Cho

```math
A=[a_1\ a_2\ \cdots\ a_n],
```

trong đó `a_j` là column thứ `j`. Với

```math
x=\begin{bmatrix}x_1\\\vdots\\x_n\end{bmatrix},
```

thì

```math
Ax=x_1a_1+\cdots+x_na_n.
```

Đây là interpretation quan trọng nhất của matrix multiplication trong chapter này: **`Ax` là linear combination của các columns của `A`**. Vì vậy `Ax=b` có solution đúng khi `b` nằm trong span của các columns, tức column space.

Cùng phép nhân đó cũng có row viewpoint: component thứ `i` của `Ax` là dot product giữa row thứ `i` của `A` và vector `x`. Column view phù hợp với geometry của output space; row view phù hợp với constraints.

## Row operations tồn tại vì sao?

Gaussian elimination không phải một bộ mẹo máy móc. Ta muốn thay hệ equations ban đầu bằng một hệ **tương đương**, nghĩa là giữ nguyên solution set nhưng làm structure dễ nhìn hơn.

Ba elementary row operations đều reversible:

- đổi chỗ hai equations;
- nhân một equation với nonzero scalar;
- cộng một multiple của equation này vào equation khác.

Vì mỗi thao tác có thể đảo ngược, chúng không tạo hoặc xóa nghiệm. Đây là proof idea đứng sau Gaussian elimination.

Ví dụ hệ

```math
\begin{cases}
x+y=3\\
2x-y=0
\end{cases}
```

có augmented matrix

```math
\left[
\begin{array}{cc|c}
1&1&3\\
2&-1&0
\end{array}
\right].
```

Thực hiện `R_2 \leftarrow R_2-2R_1`:

```math
\left[
\begin{array}{cc|c}
1&1&3\\
0&-3&-6
\end{array}
\right],
```

nên `y=2`, rồi `x=1`. Elimination đã biến coupled constraints thành triangular dependency.

## Vì sao có unique, none hoặc infinitely many solutions?

Geometrically, mỗi linear equation là một hyperplane. Solution của system là intersection của các hyperplanes đó.

Nếu constraints độc lập và đủ để xác định state, intersection có thể là một point duy nhất. Nếu constraints mâu thuẫn, intersection rỗng. Nếu constraints không đủ độc lập, solution set còn free directions.

Algebraically, row

```math
[0\ 0\ \cdots\ 0\mid c],\qquad c\neq 0
```

nghĩa là `0=c`, nên system inconsistent.

Nếu sau elimination có non-pivot columns, các variables tương ứng trở thành free variables. Khi đó solution set thường là một affine subspace: một particular solution cộng với null-space directions.

## Rank là số constraints độc lập thực sự

Rank không nên được nhớ như “số pivot” rồi dừng ở đó. Nó đo số independent output directions mà matrix có thể tạo ra, đồng thời là số independent constraints sau khi redundancy bị loại bỏ.

Với `A` kích thước `m×n`:

```math
\operatorname{rank}(A)\le \min(m,n).
```

Nếu rank nhỏ hơn số rows, có redundant constraints trong row structure. Nếu rank nhỏ hơn số columns, tồn tại nonzero directions `x` sao cho `Ax=0`, tức null space không trivial.

Điều này nối trực tiếp sang theorem rank-nullity:

```math
n=\operatorname{rank}(A)+\operatorname{nullity}(A).
```

Input degrees of freedom được chia thành directions còn nhìn thấy ở output và directions bị transformation làm mất.

## Inverse: khi transformation giữ đủ thông tin

Square matrix `A` invertible khi tồn tại `A^{-1}` sao cho

```math
A^{-1}A=AA^{-1}=I.
```

Khi đó mỗi `b` có đúng một preimage:

```math
x=A^{-1}b.
```

Nhưng đây là statement lý thuyết, không phải lời khuyên implementation. Trong numerical computing, tính explicit inverse rồi nhân với `b` thường chậm hơn và kém ổn định hơn so với solving bằng LU, QR hoặc specialized factorizations.

Invertibility có nhiều cách mô tả tương đương cho square matrix `A`:

```text
A invertible
⇔ rank(A)=n
⇔ null(A)={0}
⇔ columns independent
⇔ columns span R^n
⇔ det(A)≠0
⇔ Ax=b có unique solution với mọi b.
```

Đây không phải một list facts rời rạc; tất cả cùng nói một điều: transformation không collapse information direction nào.

## Determinant: vì sao zero determinant quan trọng?

Determinant (행렬식) có geometric meaning là signed volume scaling. Trong 2D, `|det A|` cho area scale; trong 3D, volume scale.

Nếu

```math
\det A=0,
```

một volume khác zero bị collapse thành zero volume. Nghĩa là toàn bộ space bị ép vào lower-dimensional set, nên ít nhất một direction bị mất và inverse không thể tồn tại.

Determinant hữu ích về theory, nhưng không nên dùng như default numerical test cho invertibility của large matrices. Conditioning và singular values thường informative hơn.

## Matrix multiplication tồn tại vì composition

Giả sử `B` map input từ `R^p` sang `R^n`, rồi `A` map từ `R^n` sang `R^m`. Composition là

```math
x\mapsto Bx\mapsto A(Bx).
```

Ta muốn một matrix duy nhất biểu diễn cả pipeline, nên định nghĩa product `AB` sao cho

```math
(AB)x=A(Bx).
```

Đây là lý do matrix multiplication có shape rule và vì sao generally

```math
AB\neq BA.
```

Composition của operations có order. Rotate rồi nonuniform scale có thể khác scale rồi rotate.

## Worked example — cân bằng một portfolio constraint đơn giản

Giả sử ba assets có weights `w_1,w_2,w_3`. Ta muốn tổng weights bằng 1 và exposure tới hai factors bằng target values:

```math
\begin{cases}
w_1+w_2+w_3=1\\
2w_1+w_2=0.8\\
w_2+2w_3=1.0
\end{cases}
```

Ta viết

```math
Aw=b.
```

Điểm quan trọng không nằm ở việc elimination bằng tay, mà ở modeling: mỗi row là một constraint, mỗi column mô tả cách một asset góp vào từng constraint. Nếu rows gần phụ thuộc tuyến tính, solution sẽ nhạy với data noise; lúc đó vấn đề không còn chỉ là “solve equation” mà chuyển sang conditioning và optimization.

## Từ exact equations đến data science

Trong real data, thường không tồn tại `x` sao cho `Ax=b` chính xác vì measurement noise hoặc model mismatch. Khi đó `b` nằm ngoài column space của `A`. Bài toán tự nhiên chuyển thành tìm `Ax` gần `b` nhất, dẫn tới least squares.

Vì vậy learning dependency tự nhiên là:

```text
Ax=b
→ column space / null space / rank
→ projection
→ least squares
→ QR/SVD
→ regression / PCA / inverse problems.
```

## Computer Science, AI và Physics connections

Trong graphics, matrix biểu diễn coordinate transforms. Trong ML, affine layer có dạng

```math
z=Wx+b,
```

trong đó `W` linear còn `b` là translation nên whole map là affine. Trong finite-state approximations, transition operators cũng được lưu bằng matrices. Trong physics, coupled linear systems xuất hiện sau linearization quanh equilibrium. Trong numerical simulation, sparse matrices cho phép xử lý systems hàng triệu unknowns nếu exploit structure đúng.

## Assumptions và failure modes

Linear system modeling giả định relation được mô tả đủ tốt bằng linear combinations. Nếu underlying physics nonlinear, `Ax=b` có thể chỉ là local approximation.

Even khi exact mathematical solution tồn tại, computation vẫn có thể unreliable nếu `A` ill-conditioned. Hai matrices đều invertible nhưng một matrix gần singular có thể amplify tiny input errors rất mạnh. Vì vậy “invertible” không đồng nghĩa “numerically safe”.

## Mental Model

> Matrix không chỉ là bảng coefficients. Nó là một machine tuyến tính được viết bằng tọa độ. `Ax=b` hỏi machine đó có thể tạo `b` hay không; rank cho biết bao nhiêu directions sống sót; null space cho biết directions nào bị mất; elimination chỉ là cách đổi representation để structure đó lộ ra.

## Common Misconceptions

**“Có inverse thì cứ dùng `A^{-1}b` để solve.”** Đúng về algebra nhưng thường không phải implementation tốt. Solver dựa factorization thường nhanh và ổn định hơn.

**“Nhiều equations hơn unknowns thì chắc chắn không có nghiệm.”** Không đúng. Equations có thể redundant, hoặc system overdetermined nhưng vẫn consistent.

**“`det(A)` nhỏ nghĩa matrix chắc chắn singular.”** Determinant phụ thuộc scaling và dimension; numerical sensitivity nên được đánh giá bằng singular values hoặc condition number.

**“Matrix multiplication là elementwise multiplication.”** Không. Matrix product được thiết kế để represent composition của linear maps.