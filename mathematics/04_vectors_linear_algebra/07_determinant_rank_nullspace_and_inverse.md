# Determinant, rank, null không gian (space / 공간) và inverse: cấu trúc (structure / 구조), thông tin (information / 정보) mất mát (loss / 손실) và reversibility

> **Mạch đọc:** Đọc **Determinant, rank, null không gian (space / 공간) và inverse: cấu trúc (structure / 구조), thông tin (information / 정보) mất mát (loss / 손실) và reversibility** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Determinant là oriented volume scaling** sang **2. Vì sao det(AB)=det(A)det(B)?**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Một ma trận (matrix / 행렬) nên được nhìn như một tuyến tính (linear / 선형) transformation. Khi đó determinant, rank, null không gian (space / 공간) và inverse không còn là bốn topics rời rạc mà là bốn cách đo cùng một cấu trúc (structure / 구조):

```text
determinant → volume/orientation thay đổi ra sao?
rank        → bao nhiêu independent directions còn sống?
null space  → directions nào bị xóa?
inverse     → transformation có thể undo không?
```

Các khái niệm này nối hình học (geometry / 기하학), các hệ thống (systems / 시스템들) of equations, numerical stability, dữ liệu (data / 데이터) compression và identifiability.

## 1. Determinant là oriented volume scaling

Với ma trận (matrix / 행렬) vuông

```math
A\in\mathbb R^{n\times n},
```

determinant

```math
\det(A)
```

đo signed factor mà `A` quy mô (scale / 규모) n-dimensional volume.

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

Magnitude `|det(A)|` là area scaling của đơn vị (unit / 단위) square. Sign encode orientation.

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

Composition `B` rồi `A` quy mô (scale / 규모) volume theo hai stages.

Nếu `B` quy mô (scale / 규모) volume factor `det(B)` và `A` tiếp tục quy mô (scale / 규모) factor `det(A)`, total quy mô (scale / 규모) phải là sản phẩm (product / 제품):

```math
\det(AB)=\det(A)\det(B).
```

Thuộc tính (property / 속성) này có geometric meaning, không chỉ algebraic định danh (identity / 식별자).

Nó cũng giải thích:

```math
\det(A^{-1})=
\frac1{\det(A)}
```

khi inverse tồn tại.

## 3. Row operations và determinant

Elementary row operations ảnh hưởng determinant có cấu trúc (structure / 구조) rõ:

- swap two rows → đổi sign;
- multiply row by `c` → determinant multiply `c`;
- add multiple of one row to another → determinant unchanged.

Điều này phản ánh cách parallelepiped volume thay đổi.

Nó cũng cho cách compute determinant qua elimination thay vì cofactor expansion tốn kém.

## 4. Cofactor expansion useful conceptually nhưng không phải default thuật toán (algorithm / 알고리즘)

Laplace/cofactor expansion giúp chứng minh properties và hiểu minors:

```math
\det(A)=
\sum_j(-1)^{i+j}a_{ij}M_{ij}.
```

Nhưng recursive hiện thực (implementation / 구현) có độ phức tạp (complexity / 복잡도) rất tệ cho large matrices.

Numerical libraries thường dùng LU-like factorization để compute determinant hoặc log-determinant.

Distinction:

```text
formula for theory
≠ algorithm for production
```

## 5. Rank là dimension của reachable đầu ra (output / 출력)

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

Column không gian (space / 공간) là set all outputs:

```math
\mathcal C(A)
=
\{Ax:x\in\mathbb R^n\}.
```

Do đó rank trả lời:

> Transformation có thể tạo ra bao nhiêu independent đầu ra (output / 출력) directions?

Một 3D map collapse mọi điểm (point / 지점) xuống plane có rank 2.

Collapse xuống line có rank 1.

Map mọi thứ về zero có rank 0.

## 6. Row rank = column rank không phải coincidence

Một theorem trung tâm nói dimension của row không gian (space / 공간) bằng dimension của column không gian (space / 공간).

Vì vậy ta nói đơn giản “rank”.

Proof đầy đủ cần tuyến tính (linear / 선형) algebra cấu trúc (structure / 구조) sâu hơn, nhưng intuition là row reduction bộc lộ cùng số independent các ràng buộc (constraints / 제약조건들) và independent đầu ra (output / 출력) directions qua pivot cấu trúc (structure / 구조).

Pivot count là rank.

## 7. Null không gian (space / 공간) là thông tin (information / 정보) directions bị mất

Null không gian (space / 공간):

```math
\mathcal N(A)
=
\{x:Ax=0\}.
```

Nếu có nonzero `x` trong null không gian (space / 공간):

```math
Ax=0,
\qquad x\ne0,
```

thì inputs `z` và `z+x` map tới cùng đầu ra (output / 출력):

```math
A(z+x)=Az+Ax=Az.
```

Transformation không thể phân biệt hai inputs này.

Đây là meaning sâu của null không gian (space / 공간):

> null directions là directions mà biểu diễn (representation / 표현) làm mất hoàn toàn.

## 8. Rank–nullity là accounting định danh (identity / 식별자) của dimensions

Nếu `A` có `n` columns:

```math
\operatorname{rank}(A)
+
\operatorname{nullity}(A)
=n.
```

Đầu vào (input / 입력) dimensions chia thành hai nhóm:

```text
directions visible in output
+
directions collapsed to zero
=
total input dimensions
```

Đây gần như conservation law của tuyến tính (linear / 선형) thông tin (information / 정보).

## 9. hệ thống (system / 시스템) Ax=b dưới viewpoint rank

Equation

```math
Ax=b
```

solvable iff

```math
b\in\mathcal C(A).
```

Nếu solvable và null không gian (space / 공간) nontrivial, solutions không unique.

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

Vì vậy general solution có cấu trúc (structure / 구조):

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

null không gian (space / 공간) chỉ có zero véc-tơ (vector / 벡터).

Khi `Ax=b` solvable, solution unique.

Trong regression, nếu thiết kế (design / 설계) ma trận (matrix / 행렬) columns linearly dependent, coefficients không uniquely identifiable.

Ví dụ nếu một tính năng (feature / 기능) luôn là chính xác (exact / 정확한) sum của hai features khác, nhiều coefficient combinations cho cùng prediction.

## 11. Full row rank có meaning khác

Nếu `A\in\mathbb R^{m\times n}` có full row rank:

```math
\operatorname{rank}(A)=m,
```

column không gian (space / 공간) là toàn bộ `\mathbb R^m`.

Do đó mọi `b\in\mathbb R^m` đều reachable.

Nhưng nếu `n>m`, null không gian (space / 공간) vẫn có dimension ít nhất `n-m`, nên đầu vào (input / 입력) solution thường không unique.

Đây là distinction giữa surjectivity và injectivity.

## 12. Invertible ma trận (matrix / 행렬) Theorem: nhiều statements là cùng một fact

Cho square ma trận (matrix / 행렬) `A\in\mathbb R^{n\times n}`. Các statements sau equivalent:

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

Đây không phải danh sách (list / 목록) cần memorize riêng. Tất cả đều nói:

> Không direction nào bị collapse và transformation giữ đủ thông tin (information / 정보) để undo.

## 13. Determinant zero là nhị phân (binary / 이진) singularity kiểm thử (test / 테스트), nhưng không đo conditioning tốt

Nếu

```math
\det(A)=0,
```

Ma trận (matrix / 행렬) singular.

Nhưng determinant rất nhỏ không tự động nghĩa ill-conditioned theo scale-independent sense.

Ví dụ quy mô (scale / 규모) toàn ma trận (matrix / 행렬) bởi tiny constant làm determinant shrink mạnh dù relative hình học (geometry / 기하학) có thể không tệ tương ứng.

Điều kiện (condition / 조건) number dựa trên singular values là chỉ số (metric / 지표) độ tin cậy (reliability / 신뢰성) tốt hơn.

## 14. Singular values cho quantitative picture của rank mất mát (loss / 손실)

SVD:

```math
A=U\Sigma V^T.
```

Singular values:

```math
\sigma_1\ge\sigma_2\ge\cdots\ge0.
```

Rank bằng số singular values nonzero trong chính xác (exact / 정확한) math.

Nếu smallest singular giá trị (value / 값) rất nhỏ nhưng nonzero, ma trận (matrix / 행렬) technically invertible nhưng gần singular.

Điều kiện (condition / 조건) number:

```math
\kappa_2(A)
=
\frac{\sigma_{max}}{\sigma_{min}}
```

cho square invertible ma trận (matrix / 행렬).

Large `\kappa` nghĩa some directions được stretch/compress rất khác nhau, khiến inverse amplify noise.

## 15. Near-null directions quan trọng trong dữ liệu (data / 데이터)

Trong noisy real dữ liệu (data / 데이터), chính xác (exact / 정확한) zero singular values hiếm. Thay vào đó có very small singular values.

Direction `v` với

```math
\|Av\|\ll\|v\|
```

là near-null direction.

Thông tin (information / 정보) ở direction đó gần như bị xóa; inversion phải divide by tiny quy mô (scale / 규모) và amplify noise.

Inverse problems, multicollinearity và ill-conditioned regression đều liên quan cấu trúc (structure / 구조) này.

## 16. Inverse là mathematical đối tượng (object / 객체), không phải default computational phương thức (method / 메서드)

Nếu `A` invertible:

```math
x=A^{-1}b.
```

đúng về lý thuyết.

Nhưng mã (code / 코드) thường nên solve

```text
Ax = b
```

bằng LU/QR/Cholesky/iterative solver tùy cấu trúc (structure / 구조).

Tính tường minh (explicit / 명시적) inverse:

- thường tốn hơn;
- có thể kém stable;
- tạo unnecessary lưu trữ (storage / 저장소)/công việc (work / 작업).

Quy tắc (rule / 규칙) kỹ thuật (engineering / 엔지니어링):

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

Nếu hệ thống (system / 시스템) underdetermined, `A^+b` thường chọn solution có minimum Euclidean norm.

Nếu overdetermined, nó cho least-squares projection solution.

## 18. Determinant và thay đổi (change / 변경) of variables

Cho coordinate transform:

```math
x=T(u).
```

Jacobian ma trận (matrix / 행렬):

```math
J_T(u).
```

Cục bộ (local / 로컬) volume scales theo

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

Jacobian determinant không phải correction factor bí ẩn; nó đo cục bộ (local / 로컬) volume distortion.

## 19. Determinant trong xác suất (probability / 확률)

Khi biến đổi continuous random véc-tơ (vector / 벡터), density phải compensate volume scaling.

Roughly:

```math
p_Y(y)
=
p_X(x)
\left|\det\frac{\partial x}{\partial y}\right|.
```

Nếu ánh xạ (mapping / 매핑) expand không gian (space / 공간), density per đơn vị (unit / 단위) volume giảm tương ứng để total xác suất (probability / 확률) vẫn bằng 1.

Đây là cùng geometric meaning với calculus.

## 20. Rank trong PCA và compression

Nếu dữ liệu (data / 데이터) ma trận (matrix / 행렬) có effective rank `k\ll n`, nhiều dimensions observed thực chất nằm gần low-dimensional subspace.

Truncated SVD giữ top singular directions:

```math
A_k=U_k\Sigma_kV_k^T.
```

Eckart–Young theorem nói đây là best rank-k approximation dưới dùng chung (common / 공통) norms.

Low rank = compressible tuyến tính (linear / 선형) cấu trúc (structure / 구조).

## 21. Rank trong neural networks

Weight ma trận (matrix / 행렬) rank giới hạn dimension của transformed biểu diễn (representation / 표현).

Low-rank factorization:

```math
W\approx UV^T
```

có thể giảm parameters/computation.

Nhưng rank reduction cũng giới hạn representational sức chứa (capacity / 용량). Compression là sự đánh đổi (trade-off / 트레이드오프), không phải free improvement.

## 22. Null không gian (space / 공간) trong các ràng buộc (constraints / 제약조건들)

Cho equality các ràng buộc (constraints / 제약조건들):

```math
Cx=d.
```

Nếu `x_0` feasible, mọi feasible perturbation giữ các ràng buộc (constraints / 제약조건들) phải thỏa:

```math
C\Delta x=0.
```

Do đó feasible directions nằm trong null không gian (space / 공간) của `C`.

Tối ưu hóa (optimization / 최적화) under tuyến tính (linear / 선형) các ràng buộc (constraints / 제약조건들) có thể parameterize solutions bằng null-space basis.

## 23. Worked example: redundant equations

Hệ thống (system / 시스템):

```math
x+y=2
```

```math
2x+2y=4.
```

Second equation không thêm independent thông tin (information / 정보).

Ma trận (matrix / 행렬):

```math
A=
\begin{bmatrix}
1&1\\
2&2
\end{bmatrix}.
```

Rank = 1, không phải 2.

Null không gian (space / 공간) dimension:

```math
2-1=1.
```

Indeed:

```math
\begin{bmatrix}1\\-1\end{bmatrix}
```

nằm trong null không gian (space / 공간).

Solutions form a line, không phải unique điểm (point / 지점).

## 24. Worked example: rank mất mát (loss / 손실) as projection

Ma trận (matrix / 행렬)

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

Nó dự án (project / 프로젝트) plane xuống x-axis.

```text
rank = 1
null space = y-axis
det = 0
inverse = không tồn tại
```

Bốn concepts đồng thời kể cùng một story.

## 25. Numerical rank không phải chính xác (exact / 정확한) rank trong finite precision

Trong floating điểm (point / 지점), ta cần threshold để quyết định singular giá trị (value / 값) có “effectively zero” hay không.

Threshold phụ thuộc:

- ma trận (matrix / 행렬) quy mô (scale / 규모);
- machine precision;
- noise mức (level / 수준);
- ứng dụng (application / 애플리케이션) tolerance.

Vì vậy numerical rank là mô hình (model / 모델)/kỹ thuật (engineering / 엔지니어링) judgment, không chỉ symbolic count.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Phần này nối determinant, rank và null space với khả năng đảo, số chiều thông tin và nghiệm của hệ tuyến tính. Hãy dùng các connection để kiểm tra một ma trận đang giữ, nén hay làm mất thông tin.

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

## Mô hình tư duy (mental model / 사고 모델)

> ma trận (matrix / 행렬) là một channel truyền thông tin (information / 정보) qua tuyến tính (linear / 선형) transformation. **Rank** đo dimension của thông tin (information / 정보) đi qua. **Null không gian (space / 공간)** chứa thông tin (information / 정보) bị xóa. **Determinant** đo signed volume distortion khi đầu vào (input / 입력)/đầu ra (output / 출력) dimensions bằng nhau. **Inverse** tồn tại khi không thông tin (information / 정보) nào bị mất. **Conditioning** hỏi việc phục hồi thông tin (information / 정보) nhạy với noise đến đâu.

## Dùng chung (common / 공통) Misconceptions

Determinant không phải chỉ để test inverse. Rank không phải số nonzero entries. `det(A)` nhỏ không tự động nghĩa matrix ill-conditioned nếu chưa xét scale. Square invertible matrix có null space `{0}`, nhưng rectangular matrices cần injective/surjective analysis riêng. Explicit inverse hiếm khi là cách tốt nhất để solve system. Numerical rank phụ thuộc tolerance; exact algebraic rank và practical rank có thể khác.
