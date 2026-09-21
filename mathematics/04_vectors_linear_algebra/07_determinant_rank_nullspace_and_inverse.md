# Determinant, rank, null space và inverse: structure, information loss và reversibility

Một matrix nên được nhìn như một linear transformation. Khi đó determinant, rank, null space và inverse không còn là bốn topics rời rạc mà là bốn cách đo cùng một structure:

```text
determinant → volume/orientation thay đổi ra sao?
rank        → bao nhiêu independent directions còn sống?
null space  → directions nào bị xóa?
inverse     → transformation có thể undo không?
```

Các khái niệm này nối geometry, systems of equations, numerical stability, data compression và identifiability.

## 1. Determinant là oriented volume scaling

Với matrix vuông

```math
A\in\mathbb R^{n\times n},
```

determinant

```math
\det(A)
```

đo signed factor mà `A` scale n-dimensional volume.

Trong 2D:

```math
A=
\begin{bmatrix}
a&b\\
c&d
\end{bmatrix}
```

thì

```math
\det(A)=ad-bc.
```

Magnitude `|det(A)|` là area scaling của unit square. Sign encode orientation.

Nếu

```math
\det(A)=2,
```

areas double.

Nếu

```math
\det(A)=-2,
```

area doubles và orientation flips.

Nếu

```math
\det(A)=0,
```

volume collapses xuống dimension thấp hơn.

## 2. Vì sao det(AB)=det(A)det(B)?

Composition `B` rồi `A` scale volume theo hai stages.

Nếu `B` scale volume factor `det(B)` và `A` tiếp tục scale factor `det(A)`, total scale phải là product:

```math
\det(AB)=\det(A)\det(B).
```

Property này có geometric meaning, không chỉ algebraic identity.

Nó cũng giải thích:

```math
\det(A^{-1})=
\frac1{\det(A)}
```

khi inverse tồn tại.

## 3. Row operations và determinant

Elementary row operations ảnh hưởng determinant có structure rõ:

- swap two rows → đổi sign;
- multiply row by `c` → determinant multiply `c`;
- add multiple of one row to another → determinant unchanged.

Điều này phản ánh cách parallelepiped volume thay đổi.

Nó cũng cho cách compute determinant qua elimination thay vì cofactor expansion tốn kém.

## 4. Cofactor expansion useful conceptually nhưng không phải default algorithm

Laplace/cofactor expansion giúp chứng minh properties và hiểu minors:

```math
\det(A)=
\sum_j(-1)^{i+j}a_{ij}M_{ij}.
```

Nhưng recursive implementation có complexity rất tệ cho large matrices.

Numerical libraries thường dùng LU-like factorization để compute determinant hoặc log-determinant.

Distinction:

```text
formula for theory
≠ algorithm for production
```

## 5. Rank là dimension của reachable output

Nếu

```math
A:\mathbb R^n\to\mathbb R^m,
```

rank là

```math
\operatorname{rank}(A)
=
\dim\mathcal C(A).
```

Column space là set all outputs:

```math
\mathcal C(A)
=
\{Ax:x\in\mathbb R^n\}.
```

Do đó rank trả lời:

> Transformation có thể tạo ra bao nhiêu independent output directions?

Một 3D map collapse mọi point xuống plane có rank 2.

Collapse xuống line có rank 1.

Map mọi thứ về zero có rank 0.

## 6. Row rank = column rank không phải coincidence

Một theorem trung tâm nói dimension của row space bằng dimension của column space.

Vì vậy ta nói đơn giản “rank”.

Proof đầy đủ cần linear algebra structure sâu hơn, nhưng intuition là row reduction bộc lộ cùng số independent constraints và independent output directions qua pivot structure.

Pivot count là rank.

## 7. Null space là information directions bị mất

Null space:

```math
\mathcal N(A)
=
\{x:Ax=0\}.
```

Nếu có nonzero `x` trong null space:

```math
Ax=0,
\qquad x\ne0,
```

thì inputs `z` và `z+x` map tới cùng output:

```math
A(z+x)=Az+Ax=Az.
```

Transformation không thể phân biệt hai inputs này.

Đây là meaning sâu của null space:

> null directions là directions mà representation làm mất hoàn toàn.

## 8. Rank–nullity là accounting identity của dimensions

Nếu `A` có `n` columns:

```math
\operatorname{rank}(A)
+
\operatorname{nullity}(A)
=n.
```

Input dimensions chia thành hai nhóm:

```text
directions visible in output
+
directions collapsed to zero
=
total input dimensions
```

Đây gần như conservation law của linear information.

## 9. System Ax=b dưới viewpoint rank

Equation

```math
Ax=b
```

solvable iff

```math
b\in\mathcal C(A).
```

Nếu solvable và null space nontrivial, solutions không unique.

Nếu `x_0` là một solution:

```math
Ax_0=b,
```

thì mọi

```math
x=x_0+z,
\qquad z\in\mathcal N(A)
```

cũng là solution.

Vì vậy general solution có structure:

```text
one particular solution
+
all homogeneous solutions
```

## 10. Full column rank và parameter identifiability

Nếu `A` có full column rank:

```math
\operatorname{rank}(A)=n,
```

null space chỉ có zero vector.

Khi `Ax=b` solvable, solution unique.

Trong regression, nếu design matrix columns linearly dependent, coefficients không uniquely identifiable.

Ví dụ nếu một feature luôn là exact sum của hai features khác, nhiều coefficient combinations cho cùng prediction.

## 11. Full row rank có meaning khác

Nếu `A\in\mathbb R^{m\times n}` có full row rank:

```math
\operatorname{rank}(A)=m,
```

column space là toàn bộ `\mathbb R^m`.

Do đó mọi `b\in\mathbb R^m` đều reachable.

Nhưng nếu `n>m`, null space vẫn có dimension ít nhất `n-m`, nên input solution thường không unique.

Đây là distinction giữa surjectivity và injectivity.

## 12. Invertible Matrix Theorem: nhiều statements là cùng một fact

Cho square matrix `A\in\mathbb R^{n\times n}`. Các statements sau equivalent:

```text
A invertible
⇔ det(A) ≠ 0
⇔ rank(A) = n
⇔ null(A) = {0}
⇔ columns independent
⇔ columns span R^n
⇔ Ax=b có unique solution cho mọi b
⇔ 0 không là eigenvalue
```

Đây không phải list cần memorize riêng. Tất cả đều nói:

> Không direction nào bị collapse và transformation giữ đủ information để undo.

## 13. Determinant zero là binary singularity test, nhưng không đo conditioning tốt

Nếu

```math
\det(A)=0,
```

matrix singular.

Nhưng determinant rất nhỏ không tự động nghĩa ill-conditioned theo scale-independent sense.

Ví dụ scale toàn matrix bởi tiny constant làm determinant shrink mạnh dù relative geometry có thể không tệ tương ứng.

Condition number dựa trên singular values là metric reliability tốt hơn.

## 14. Singular values cho quantitative picture của rank loss

SVD:

```math
A=U\Sigma V^T.
```

Singular values:

```math
\sigma_1\ge\sigma_2\ge\cdots\ge0.
```

Rank bằng số singular values nonzero trong exact math.

Nếu smallest singular value rất nhỏ nhưng nonzero, matrix technically invertible nhưng gần singular.

Condition number:

```math
\kappa_2(A)
=
\frac{\sigma_{max}}{\sigma_{min}}
```

cho square invertible matrix.

Large `\kappa` nghĩa some directions được stretch/compress rất khác nhau, khiến inverse amplify noise.

## 15. Near-null directions quan trọng trong data

Trong noisy real data, exact zero singular values hiếm. Thay vào đó có very small singular values.

Direction `v` với

```math
\|Av\|\ll\|v\|
```

là near-null direction.

Information ở direction đó gần như bị xóa; inversion phải divide by tiny scale và amplify noise.

Inverse problems, multicollinearity và ill-conditioned regression đều liên quan structure này.

## 16. Inverse là mathematical object, không phải default computational method

Nếu `A` invertible:

```math
x=A^{-1}b.
```

đúng về lý thuyết.

Nhưng code thường nên solve

```text
Ax = b
```

bằng LU/QR/Cholesky/iterative solver tùy structure.

Tính explicit inverse:

- thường tốn hơn;
- có thể kém stable;
- tạo unnecessary storage/work.

Rule engineering:

```text
need solution? solve system
need inverse as object? compute inverse only when justified
```

## 17. Pseudoinverse mở rộng inverse cho rectangular/rank-deficient matrices

Moore–Penrose pseudoinverse:

```math
A^+=V\Sigma^+U^T.
```

Với SVD, reciprocal chỉ áp cho nonzero singular values.

Pseudoinverse cho least-squares/minimum-norm solution trong broad cases.

Nếu system underdetermined, `A^+b` thường chọn solution có minimum Euclidean norm.

Nếu overdetermined, nó cho least-squares projection solution.

## 18. Determinant và change of variables

Cho coordinate transform:

```math
x=T(u).
```

Jacobian matrix:

```math
J_T(u).
```

Local volume scales theo

```math
|\det J_T(u)|.
```

Do đó multiple integral đổi variables:

```math
\int f(x)\,dx
=
\int f(T(u))
|\det J_T(u)|\,du.
```

Jacobian determinant không phải correction factor bí ẩn; nó đo local volume distortion.

## 19. Determinant trong probability

Khi biến đổi continuous random vector, density phải compensate volume scaling.

Roughly:

```math
p_Y(y)
=
p_X(x)
\left|\det\frac{\partial x}{\partial y}\right|.
```

Nếu mapping expand space, density per unit volume giảm tương ứng để total probability vẫn bằng 1.

Đây là cùng geometric meaning với calculus.

## 20. Rank trong PCA và compression

Nếu data matrix có effective rank `k\ll n`, nhiều dimensions observed thực chất nằm gần low-dimensional subspace.

Truncated SVD giữ top singular directions:

```math
A_k=U_k\Sigma_kV_k^T.
```

Eckart–Young theorem nói đây là best rank-k approximation dưới common norms.

Low rank = compressible linear structure.

## 21. Rank trong neural networks

Weight matrix rank giới hạn dimension của transformed representation.

Low-rank factorization:

```math
W\approx UV^T
```

có thể giảm parameters/computation.

Nhưng rank reduction cũng giới hạn representational capacity. Compression là trade-off, không phải free improvement.

## 22. Null space trong constraints

Cho equality constraints:

```math
Cx=d.
```

Nếu `x_0` feasible, mọi feasible perturbation giữ constraints phải thỏa:

```math
C\Delta x=0.
```

Do đó feasible directions nằm trong null space của `C`.

Optimization under linear constraints có thể parameterize solutions bằng null-space basis.

## 23. Worked example: redundant equations

System:

```math
x+y=2
```

```math
2x+2y=4.
```

Second equation không thêm independent information.

Matrix:

```math
A=
\begin{bmatrix}
1&1\\
2&2
\end{bmatrix}.
```

Rank = 1, không phải 2.

Null space dimension:

```math
2-1=1.
```

Indeed:

```math
\begin{bmatrix}1\\-1\end{bmatrix}
```

nằm trong null space.

Solutions form a line, không phải unique point.

## 24. Worked example: rank loss as projection

Matrix

```math
A=
\begin{bmatrix}
1&0\\
0&0
\end{bmatrix}
```

map

```math
(x,y)\mapsto(x,0).
```

Nó project plane xuống x-axis.

```text
rank = 1
null space = y-axis
det = 0
inverse = không tồn tại
```

Bốn concepts đồng thời kể cùng một story.

## 25. Numerical rank không phải exact rank trong finite precision

Trong floating point, ta cần threshold để quyết định singular value có “effectively zero” hay không.

Threshold phụ thuộc:

- matrix scale;
- machine precision;
- noise level;
- application tolerance.

Vì vậy numerical rank là model/engineering judgment, không chỉ symbolic count.

## Knowledge Connection

```text
volume scaling → determinant
reachable outputs → rank
lost directions → null space
reversibility → inverse
near-lost directions → conditioning
best generalized inverse → pseudoinverse
low-dimensional structure → SVD/PCA/compression
coordinate volume change → Jacobian determinant
```

## Mental Model

> Matrix là một channel truyền information qua linear transformation. **Rank** đo dimension của information đi qua. **Null space** chứa information bị xóa. **Determinant** đo signed volume distortion khi input/output dimensions bằng nhau. **Inverse** tồn tại khi không information nào bị mất. **Conditioning** hỏi việc phục hồi information nhạy với noise đến đâu.

## Common Misconceptions

Determinant không phải chỉ để test inverse. Rank không phải số nonzero entries. `det(A)` nhỏ không tự động nghĩa matrix ill-conditioned nếu chưa xét scale. Square invertible matrix có null space `{0}`, nhưng rectangular matrices cần injective/surjective analysis riêng. Explicit inverse hiếm khi là cách tốt nhất để solve system. Numerical rank phụ thuộc tolerance; exact algebraic rank và practical rank có thể khác.