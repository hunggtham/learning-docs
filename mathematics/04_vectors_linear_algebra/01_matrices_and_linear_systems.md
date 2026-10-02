# Ma trận và hệ phương trình tuyến tính

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Ma trận và hệ phương trình tuyến tính**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Tại sao tuyến tính (linear / 선형) các hệ thống (systems / 시스템들) xuất hiện khắp nơi?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Matrix-vector sản phẩm (product / 제품) thực sự làm gì?** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối matrices với linear systems, elimination và solution set, để phép tính bảng được gắn với bài toán cần giải.

Ma trận (matrix / 행렬) thường được nhìn thấy lần đầu như một bảng số, nhưng cách nhìn đó quá yếu để học tuyến tính (linear / 선형) algebra lâu dài. Một ma trận nên được hiểu đồng thời theo hai vai trò: nó mô tả **một hệ ràng buộc tuyến tính** và nó biểu diễn **một phép biến đổi tuyến tính** trong một hệ tọa độ cụ thể. Hai góc nhìn này gặp nhau trong phương trình

```math
Ax=b.
```

Nếu nhìn từ các hệ thống (systems / 시스템들) of equations, `A` chứa coefficients, `x` là unknown trạng thái (state / 상태) và `b` là mục tiêu (target / 대상). Nếu nhìn từ transformations, `A` là một operator nhận đầu vào (input / 입력) `x` và tạo đầu ra (output / 출력) `b`. Câu hỏi “giải hệ” vì vậy trở thành: **đầu vào (input / 입력) nào khi đi qua transformation `A` tạo ra đầu ra (output / 출력) mong muốn `b`?**

## Tại sao tuyến tính (linear / 선형) các hệ thống (systems / 시스템들) xuất hiện khắp nơi?

Nhiều bài toán thực tế có dạng nhiều quantities liên hệ gần tuyến tính trong một vùng làm việc. Kirchhoff laws trong circuits tạo các hệ thống (systems / 시스템들) của currents và voltages. Static equilibrium trong mechanics tạo các hệ thống (systems / 시스템들) từ force balance. Calibration, localization, regression, portfolio các ràng buộc (constraints / 제약조건들), mạng (network / 네트워크) luồng (flow / 흐름) approximations và numerical PDE đều dẫn đến những equations nơi nhiều unknowns bị ràng buộc đồng thời.

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

Viết `Ax=b` không chỉ để ngắn hơn. Nó làm lộ cấu trúc (structure / 구조) chung của hàng nghìn problems tưởng như khác nhau.

> **Chuyển mạch:** Trong **Ma trận và hệ phương trình tuyến tính**, **Matrix-vector sản phẩm (product / 제품) thực sự làm gì?** tiếp nhận điểm tựa từ **Tại sao tuyến tính (linear / 선형) các hệ thống (systems / 시스템들) xuất hiện khắp nơi?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Row operations tồn tại vì sao?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Matrix-vector sản phẩm (product / 제품) thực sự làm gì?

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

Đây là interpretation quan trọng nhất của phép nhân ma trận (matrix multiplication / 행렬 곱셈) trong chapter này: **`Ax` là tuyến tính (linear / 선형) combination của các columns của `A`**. Vì vậy `Ax=b` có solution đúng khi `b` nằm trong span của các columns, tức column không gian (space / 공간).

Cùng phép nhân đó cũng có row viewpoint: thành phần (component / 컴포넌트) thứ `i` của `Ax` là dot sản phẩm (product / 제품) giữa row thứ `i` của `A` và véc-tơ (vector / 벡터) `x`. Column view phù hợp với hình học (geometry / 기하학) của đầu ra (output / 출력) không gian (space / 공간); row view phù hợp với các ràng buộc (constraints / 제약조건들).

> **Chuyển mạch:** Ở chặng này của **Ma trận và hệ phương trình tuyến tính**, **Row operations tồn tại vì sao?** tiếp nhận điểm tựa từ **Matrix-vector sản phẩm (product / 제품) thực sự làm gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao có unique, none hoặc infinitely many solutions?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Row operations tồn tại vì sao?

Gaussian elimination không phải một bộ mẹo máy móc. Ta muốn thay hệ equations ban đầu bằng một hệ **tương đương**, nghĩa là giữ nguyên solution set nhưng làm cấu trúc (structure / 구조) dễ nhìn hơn.

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

có augmented ma trận (matrix / 행렬)

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

nên `y=2`, rồi `x=1`. Elimination đã biến coupled các ràng buộc (constraints / 제약조건들) thành triangular phụ thuộc (dependency / 의존성).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ma trận và hệ phương trình tuyến tính**, **Vì sao có unique, none hoặc infinitely many solutions?** tiếp nhận điểm tựa từ **Row operations tồn tại vì sao?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Rank là số các ràng buộc (constraints / 제약조건들) độc lập thực sự** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao có unique, none hoặc infinitely many solutions?

Geometrically, mỗi tuyến tính (linear / 선형) equation là một hyperplane. Solution của hệ thống (system / 시스템) là intersection của các hyperplanes đó.

Nếu các ràng buộc (constraints / 제약조건들) độc lập và đủ để xác định trạng thái (state / 상태), intersection có thể là một điểm (point / 지점) duy nhất. Nếu các ràng buộc (constraints / 제약조건들) mâu thuẫn, intersection rỗng. Nếu các ràng buộc (constraints / 제약조건들) không đủ độc lập, solution set còn free directions.

Algebraically, row

```math
[0\ 0\ \cdots\ 0\mid c],\qquad c\neq 0
```

nghĩa là `0=c`, nên hệ thống (system / 시스템) inconsistent.

Nếu sau elimination có non-pivot columns, các variables tương ứng trở thành free variables. Khi đó solution set thường là một affine subspace: một particular solution cộng với null-space directions.

> **Chuyển mạch:** Trong **Ma trận và hệ phương trình tuyến tính**, **Rank là số các ràng buộc (constraints / 제약조건들) độc lập thực sự** tiếp nhận điểm tựa từ **Vì sao có unique, none hoặc infinitely many solutions?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Inverse: khi transformation giữ đủ thông tin** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Rank là số các ràng buộc (constraints / 제약조건들) độc lập thực sự

Rank không nên được nhớ như “số pivot” rồi dừng ở đó. Nó đo số independent đầu ra (output / 출력) directions mà ma trận (matrix / 행렬) có thể tạo ra, đồng thời là số independent các ràng buộc (constraints / 제약조건들) sau khi redundancy bị loại bỏ.

Với `A` kích thước `m×n`:

```math
\operatorname{rank}(A)\le \min(m,n).
```

Nếu rank nhỏ hơn số rows, có redundant các ràng buộc (constraints / 제약조건들) trong row cấu trúc (structure / 구조). Nếu rank nhỏ hơn số columns, tồn tại nonzero directions `x` sao cho `Ax=0`, tức null không gian (space / 공간) không trivial.

Điều này nối trực tiếp sang theorem rank-nullity:

```math
n=\operatorname{rank}(A)+\operatorname{nullity}(A).
```

Đầu vào (input / 입력) degrees of freedom được chia thành directions còn nhìn thấy ở đầu ra (output / 출력) và directions bị transformation làm mất.

> **Chuyển mạch:** Ở chặng này của **Ma trận và hệ phương trình tuyến tính**, **Inverse: khi transformation giữ đủ thông tin** tiếp nhận điểm tựa từ **Rank là số các ràng buộc (constraints / 제약조건들) độc lập thực sự** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Determinant: vì sao zero determinant quan trọng?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Inverse: khi transformation giữ đủ thông tin

Square ma trận (matrix / 행렬) `A` invertible khi tồn tại `A^{-1}` sao cho

```math
A^{-1}A=AA^{-1}=I.
```

Khi đó mỗi `b` có đúng một preimage:

```math
x=A^{-1}b.
```

Nhưng đây là statement lý thuyết, không phải lời khuyên hiện thực (implementation / 구현). Trong numerical computing, tính tường minh (explicit / 명시적) inverse rồi nhân với `b` thường chậm hơn và kém ổn định hơn so với solving bằng LU, QR hoặc specialized factorizations.

Invertibility có nhiều cách mô tả tương đương cho square ma trận (matrix / 행렬) `A`:

```text
A invertible
⇔ rank(A)=n
⇔ null(A)={0}
⇔ columns independent
⇔ columns span R^n
⇔ det(A)≠0
⇔ Ax=b có unique solution với mọi b.
```

Đây không phải một danh sách (list / 목록) facts rời rạc; tất cả cùng nói một điều: transformation không collapse thông tin (information / 정보) direction nào.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ma trận và hệ phương trình tuyến tính**, **Determinant: vì sao zero determinant quan trọng?** tiếp nhận điểm tựa từ **Inverse: khi transformation giữ đủ thông tin** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phép nhân ma trận (matrix multiplication / 행렬 곱셈) tồn tại vì composition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Determinant: vì sao zero determinant quan trọng?

Determinant (행렬식) có geometric meaning là signed volume scaling. Trong 2D, `|det A|` cho area quy mô (scale / 규모); trong 3D, volume quy mô (scale / 규모).

Nếu

```math
\det A=0,
```

một volume khác zero bị collapse thành zero volume. Nghĩa là toàn bộ không gian (space / 공간) bị ép vào lower-dimensional set, nên ít nhất một direction bị mất và inverse không thể tồn tại.

Determinant hữu ích về lý thuyết (theory / 이론), nhưng không nên dùng như default numerical kiểm thử (test / 테스트) cho invertibility của large matrices. Conditioning và singular values thường informative hơn.

> **Chuyển mạch:** Trong **Ma trận và hệ phương trình tuyến tính**, **Phép nhân ma trận (matrix multiplication / 행렬 곱셈) tồn tại vì composition** tiếp nhận điểm tựa từ **Determinant: vì sao zero determinant quan trọng?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Worked example — cân bằng một portfolio ràng buộc (constraint / 제약조건) đơn giản** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phép nhân ma trận (matrix multiplication / 행렬 곱셈) tồn tại vì composition

Giả sử `B` map đầu vào (input / 입력) từ `R^p` sang `R^n`, rồi `A` map từ `R^n` sang `R^m`. Composition là

```math
x\mapsto Bx\mapsto A(Bx).
```

Ta muốn một ma trận (matrix / 행렬) duy nhất biểu diễn cả chuỗi xử lý (pipeline / 파이프라인), nên định nghĩa sản phẩm (product / 제품) `AB` sao cho

```math
(AB)x=A(Bx).
```

Đây là lý do phép nhân ma trận (matrix multiplication / 행렬 곱셈) có shape quy tắc (rule / 규칙) và vì sao generally

```math
AB\neq BA.
```

Composition của operations có thứ tự (order / 순서). Rotate rồi nonuniform quy mô (scale / 규모) có thể khác quy mô (scale / 규모) rồi rotate.

> **Chuyển mạch:** Ở chặng này của **Ma trận và hệ phương trình tuyến tính**, **Phép nhân ma trận (matrix multiplication / 행렬 곱셈) tồn tại vì composition** cho ta quy tắc; **Worked example — cân bằng một portfolio ràng buộc (constraint / 제약조건) đơn giản** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Từ chính xác (exact / 정확한) equations đến dữ liệu (data / 데이터) science** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Worked example — cân bằng một portfolio ràng buộc (constraint / 제약조건) đơn giản

Giả sử ba assets có weights `w_1,w_2,w_3`. Ta muốn tổng weights bằng 1 và exposure tới hai factors bằng mục tiêu (target / 대상) values:

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

Điểm quan trọng không nằm ở việc elimination bằng tay, mà ở modeling: mỗi row là một ràng buộc (constraint / 제약조건), mỗi column mô tả cách một asset góp vào từng ràng buộc (constraint / 제약조건). Nếu rows gần phụ thuộc tuyến tính, solution sẽ nhạy với dữ liệu (data / 데이터) noise; lúc đó vấn đề không còn chỉ là “solve equation” mà chuyển sang conditioning và tối ưu hóa (optimization / 최적화).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ma trận và hệ phương trình tuyến tính**, **Worked example — cân bằng một portfolio ràng buộc (constraint / 제약조건) đơn giản** cho ta quy tắc; **Từ chính xác (exact / 정확한) equations đến dữ liệu (data / 데이터) science** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Khoa học máy tính (computer science / 컴퓨터 과학), AI và Physics connections** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Từ chính xác (exact / 정확한) equations đến dữ liệu (data / 데이터) science

Trong real dữ liệu (data / 데이터), thường không tồn tại `x` sao cho `Ax=b` chính xác vì đo lường (measurement / 측정) noise hoặc mô hình (model / 모델) mismatch. Khi đó `b` nằm ngoài column không gian (space / 공간) của `A`. Bài toán tự nhiên chuyển thành tìm `Ax` gần `b` nhất, dẫn tới least squares.

Vì vậy học tập (learning / 학습) phụ thuộc (dependency / 의존성) tự nhiên là:

```text
Ax=b
→ column space / null space / rank
→ projection
→ least squares
→ QR/SVD
→ regression / PCA / inverse problems.
```

> **Chuyển mạch:** Trong **Ma trận và hệ phương trình tuyến tính**, **Từ chính xác (exact / 정확한) equations đến dữ liệu (data / 데이터) science** nêu điều cần giải thích; **Khoa học máy tính (computer science / 컴퓨터 과학), AI và Physics connections** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Các giả định (assumptions / 가정들) và thất bại (failure / 실패) modes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khoa học máy tính (computer science / 컴퓨터 과학), AI và Physics connections

Trong graphics, ma trận (matrix / 행렬) biểu diễn coordinate transforms. Trong ML, affine tầng (layer / 계층) có dạng

```math
z=Wx+b,
```

trong đó `W` tuyến tính (linear / 선형) còn `b` là translation nên whole map là affine. Trong finite-state approximations, chuyển tiếp (transition / 전이) operators cũng được lưu bằng matrices. Trong physics, coupled tuyến tính (linear / 선형) các hệ thống (systems / 시스템들) xuất hiện sau linearization quanh equilibrium. Trong numerical simulation, sparse matrices cho phép xử lý các hệ thống (systems / 시스템들) hàng triệu unknowns nếu exploit cấu trúc (structure / 구조) đúng.

> **Chuyển mạch:** Ở chặng này của **Ma trận và hệ phương trình tuyến tính**, **Các giả định (assumptions / 가정들) và thất bại (failure / 실패) modes** tiếp nhận điểm tựa từ **Khoa học máy tính (computer science / 컴퓨터 과학), AI và Physics connections** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Các giả định (assumptions / 가정들) và thất bại (failure / 실패) modes

Hệ tuyến tính (linear system / 선형 시스템) modeling giả định quan hệ (relation / 관계) được mô tả đủ tốt bằng tuyến tính (linear / 선형) combinations. Nếu underlying physics nonlinear, `Ax=b` có thể chỉ là cục bộ (local / 로컬) approximation.

Even khi chính xác (exact / 정확한) mathematical solution tồn tại, computation vẫn có thể unreliable nếu `A` ill-conditioned. Hai matrices đều invertible nhưng một ma trận (matrix / 행렬) gần singular có thể amplify tiny đầu vào (input / 입력) errors rất mạnh. Vì vậy “invertible” không đồng nghĩa “numerically safe”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ma trận và hệ phương trình tuyến tính**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Các giả định (assumptions / 가정들) và thất bại (failure / 실패) modes** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> ma trận (matrix / 행렬) không chỉ là bảng coefficients. Nó là một machine tuyến tính được viết bằng tọa độ. `Ax=b` hỏi machine đó có thể tạo `b` hay không; rank cho biết bao nhiêu directions sống sót; null không gian (space / 공간) cho biết directions nào bị mất; elimination chỉ là cách đổi biểu diễn (representation / 표현) để cấu trúc (structure / 구조) đó lộ ra.

> **Chuyển mạch:** Trong **Ma trận và hệ phương trình tuyến tính**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“Có inverse thì cứ dùng `A^{-1}b` để solve.”** Đúng về algebra nhưng thường không phải hiện thực (implementation / 구현) tốt. Solver dựa factorization thường nhanh và ổn định hơn.

**“Nhiều equations hơn unknowns thì chắc chắn không có nghiệm.”** Không đúng. Equations có thể redundant, hoặc hệ thống (system / 시스템) overdetermined nhưng vẫn consistent.

**“`det(A)` nhỏ nghĩa ma trận (matrix / 행렬) chắc chắn singular.”** Determinant phụ thuộc scaling và dimension; numerical sensitivity nên được đánh giá bằng singular values hoặc điều kiện (condition / 조건) number.

**“phép nhân ma trận (matrix multiplication / 행렬 곱셈) là elementwise multiplication.”** Không. ma trận (matrix / 행렬) sản phẩm (product / 제품) được thiết kế để represent composition của tuyến tính (linear / 선형) maps.

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
