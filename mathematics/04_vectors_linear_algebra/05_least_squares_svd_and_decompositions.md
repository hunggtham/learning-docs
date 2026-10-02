# Least squares, SVD và ma trận (matrix / 행렬) decompositions: projection, approximation và cấu trúc (structure / 구조)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Least squares, SVD và ma trận (matrix / 행렬) decompositions: projection, approximation và cấu trúc (structure / 구조)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Từ chính xác (exact / 정확한) solving đến best approximation** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Vì sao residual phải orthogonal?** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối least squares với SVD và decompositions, để xấp xỉ, rank và ổn định số được nhìn trong cùng một khung.

Trong nhiều bài toán thực tế, equation

```math
Ax=b
```

không có chính xác (exact / 정확한) solution. Không phải vì algebra thất bại, mà vì mô hình (model / 모델) và dữ liệu (data / 데이터) thường chứa noise, sai số đo lường (measurement error / 측정 오차) hoặc nhiều các ràng buộc (constraints / 제약조건들) hơn unknowns. Khi `b` nằm ngoài column không gian (space / 공간) của `A`, câu hỏi đúng không còn là “giải chính xác”, mà là:

> Trong tất cả outputs mà `A` có thể tạo ra, đầu ra (output / 출력) nào gần `b` nhất?

Câu hỏi đó dẫn tới least squares (phương pháp bình phương tối thiểu / 최소제곱법), projection hình học (geometry / 기하학) và cuối cùng là QR, SVD, PCA, low-rank approximation và inverse problems.

## Từ chính xác (exact / 정확한) solving đến best approximation

Ta muốn chọn `x` minimize residual

```math
r=b-Ax.
```

Nếu dùng Euclidean norm, mục tiêu (objective / 목표) là

```math
\min_x \|Ax-b\|_2^2.
```

Square không chỉ để “tránh dấu âm”. Nó tạo mục tiêu (objective / 목표) smooth, liên hệ trực tiếp với Euclidean hình học (geometry / 기하학) và Gaussian-noise likelihood.

`Ax` luôn nằm trong column không gian (space / 공간) của `A`. Do đó least squares đang tìm điểm (point / 지점) trong column không gian (space / 공간) gần `b` nhất.

> **Chuyển mạch:** Trong **Least squares, SVD và ma trận (matrix / 행렬) decompositions: projection, approximation và cấu trúc (structure / 구조)**, **Vì sao residual phải orthogonal?** tiếp nhận điểm tựa từ **Từ chính xác (exact / 정확한) solving đến best approximation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Worked example — fit một đường thẳng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao residual phải orthogonal?

Gọi `\hat x` là optimum và

```math
\hat b=A\hat x.
```

Nếu residual

```math
r=b-\hat b
```

còn có thành phần (component / 컴포넌트) dọc theo column không gian (space / 공간), ta có thể move `\hat b` một chút theo direction đó và đến gần `b` hơn. Vì vậy tại nearest điểm (point / 지점), residual phải perpendicular với mọi column của `A`:

```math
A^Tr=0.
```

Thay `r=b-A\hat x`:

```math
A^T(b-A\hat x)=0,
```

suy ra normal equations:

```math
A^TA\hat x=A^Tb.
```

Đây là proof idea từ projection, không phải một formula xuất hiện ngẫu nhiên.

> **Chuyển mạch:** Ở chặng này của **Least squares, SVD và ma trận (matrix / 행렬) decompositions: projection, approximation và cấu trúc (structure / 구조)**, **Vì sao residual phải orthogonal?** cho ta quy tắc; **Worked example — fit một đường thẳng** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Least squares không đồng nghĩa “mô hình (model / 모델) đúng”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Worked example — fit một đường thẳng

Giả sử dữ liệu (data / 데이터):

```text
x: 0, 1, 2
y: 1, 2, 2
```

Ta muốn fit

```math
y\approx \beta_0+\beta_1x.
```

Thiết kế (design / 설계) ma trận (matrix / 행렬):

```math
X=
\begin{bmatrix}
1&0\\
1&1\\
1&2
\end{bmatrix},
\qquad
y=
\begin{bmatrix}
1\\2\\2
\end{bmatrix}.
```

Không có line nào đi qua cả ba points chính xác, nên solve `X\beta=y` impossible. Least squares tìm projection của `y` lên column không gian (space / 공간) của `X`.

Normal equations:

```math
X^TX\beta=X^Ty.
```

Ta có

```math
X^TX=
\begin{bmatrix}
3&3\\
3&5
\end{bmatrix},
\qquad
X^Ty=
\begin{bmatrix}
5\\6
\end{bmatrix}.
```

Giải ra

```math
\beta_0=\frac76,\qquad \beta_1=\frac12.
```

Line fit là

```math
\hat y=\frac76+\frac12x.
```

Điểm quan trọng là hình học (geometry / 기하학): predicted véc-tơ (vector / 벡터) `X\hat\beta` là closest véc-tơ (vector / 벡터) trong mô hình (model / 모델) subspace.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Least squares, SVD và ma trận (matrix / 행렬) decompositions: projection, approximation và cấu trúc (structure / 구조)**, **Worked example — fit một đường thẳng** cho ta quy tắc; **Least squares không đồng nghĩa “mô hình (model / 모델) đúng”** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Vì sao normal equations không phải default numerical phương thức (method / 메서드)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Least squares không đồng nghĩa “mô hình (model / 모델) đúng”

Tối ưu hóa (optimization / 최적화) chỉ trả lời: trong mô hình (model / 모델) family đã chọn, parameter nào minimize squared lỗi (error / 오류)? Nó không chứng minh quan hệ (relation / 관계) thật sự tuyến tính (linear / 선형), không chứng minh causality và không bảo vệ khỏi outliers.

Nếu residual cấu trúc (structure / 구조) có mẫu (pattern / 패턴), mô hình (model / 모델) có thể misspecify. Nếu variance thay đổi theo đầu vào (input / 입력), ordinary least squares các giả định (assumptions / 가정들) về bất định (uncertainty / 불확실성) cần xem lại. Nếu features gần collinear, coefficients có thể unstable dù predictions vẫn tương đối ổn.

> **Chuyển mạch:** Trong **Least squares, SVD và ma trận (matrix / 행렬) decompositions: projection, approximation và cấu trúc (structure / 구조)**, **Vì sao normal equations không phải default numerical phương thức (method / 메서드)?** tiếp nhận điểm tựa từ **Least squares không đồng nghĩa “mô hình (model / 모델) đúng”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **QR decomposition: xây orthogonal coordinates cho column không gian (space / 공간)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao normal equations không phải default numerical phương thức (method / 메서드)?

Normal equations rất đẹp về lý thuyết (theory / 이론) nhưng có weakness numerical:

```math
\kappa(A^TA)\approx \kappa(A)^2,
```

trong dùng chung (common / 공통) 2-norm setting.

Nghĩa là conditioning có thể tệ lên đáng kể. Do đó môi trường vận hành (production / 운영 환경) numerical mã (code / 코드) thường solve least squares bằng QR hoặc SVD thay vì explicitly forming `A^TA`.

Đây là ví dụ quan trọng của distinction:

```text
mathematically equivalent ≠ numerically equally reliable.
```

> **Chuyển mạch:** Ở chặng này của **Least squares, SVD và ma trận (matrix / 행렬) decompositions: projection, approximation và cấu trúc (structure / 구조)**, **QR decomposition: xây orthogonal coordinates cho column không gian (space / 공간)** tiếp nhận điểm tựa từ **Vì sao normal equations không phải default numerical phương thức (method / 메서드)?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SVD: mọi tuyến tính (linear / 선형) map như rotate → quy mô (scale / 규모) → rotate** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## QR decomposition: xây orthogonal coordinates cho column không gian (space / 공간)

Nếu

```math
A=QR,
```

với columns của `Q` orthonormal và `R` upper triangular, thì

```math
\|Ax-b\|_2
=
\|QRx-b\|_2.
```

Orthogonality của `Q` giúp tách bài toán (problem / 문제) thành projection plus triangular solve. QR tránh việc squaring điều kiện (condition / 조건) number như normal equations và thường là workhorse cho dense least squares.

Householder reflections là hiện thực (implementation / 구현) phổ biến vì stable hơn classical Gram–Schmidt trong finite precision.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Least squares, SVD và ma trận (matrix / 행렬) decompositions: projection, approximation và cấu trúc (structure / 구조)**, **SVD: mọi tuyến tính (linear / 선형) map như rotate → quy mô (scale / 규모) → rotate** tiếp nhận điểm tựa từ **QR decomposition: xây orthogonal coordinates cho column không gian (space / 공간)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Rank, near-rank và numerical rank** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SVD: mọi tuyến tính (linear / 선형) map như rotate → quy mô (scale / 규모) → rotate

Singular giá trị (value / 값) Decomposition viết

```math
A=U\Sigma V^T.
```

Interpretation:

1. `V^T` đổi đầu vào (input / 입력) sang orthonormal directions đặc biệt;
2. `\Sigma` quy mô (scale / 규모) mỗi direction bằng singular giá trị (value / 값);
3. `U` đổi sang orthonormal đầu ra (output / 출력) directions.

SVD tồn tại cho mọi real ma trận (matrix / 행렬), kể cả rectangular và matrices không diagonalizable.

Nếu singular values là

```math
\sigma_1\ge\sigma_2\ge\cdots\ge0,
```

thì chúng cho biết transformation mạnh yếu thế nào theo các orthogonal directions.

> **Chuyển mạch:** Trong **Least squares, SVD và ma trận (matrix / 행렬) decompositions: projection, approximation và cấu trúc (structure / 구조)**, **Rank, near-rank và numerical rank** tiếp nhận điểm tựa từ **SVD: mọi tuyến tính (linear / 선형) map như rotate → quy mô (scale / 규모) → rotate** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Pseudoinverse: inverse khi inverse thật không tồn tại** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Rank, near-rank và numerical rank

Chính xác (exact / 정확한) algebra nói rank là số nonzero singular values. Nhưng measured dữ liệu (data / 데이터) hiếm khi có chính xác (exact / 정확한) zeros; noise biến zero thành tiny nonzero values.

Vì vậy numerical rank phụ thuộc tolerance và bài toán (problem / 문제) quy mô (scale / 규모). Một singular giá trị (value / 값) rất nhỏ nghĩa direction đó gần bị collapse. Inversion theo direction ấy sẽ divide by số rất nhỏ và amplify noise.

Đây là cốt lõi (core / 핵심) intuition của ill-conditioned inverse problems.

> **Chuyển mạch:** Ở chặng này của **Least squares, SVD và ma trận (matrix / 행렬) decompositions: projection, approximation và cấu trúc (structure / 구조)**, **Pseudoinverse: inverse khi inverse thật không tồn tại** tiếp nhận điểm tựa từ **Rank, near-rank và numerical rank** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Regularization: chấp nhận độ lệch (bias / 편향) để giảm variance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pseudoinverse: inverse khi inverse thật không tồn tại

Moore–Penrose pseudoinverse dùng SVD:

```math
A^+=V\Sigma^+U^T,
```

trong đó nonzero singular values được reciprocal.

Least-squares solution minimum-norm có thể viết

```math
\hat x=A^+b.
```

Nếu hệ thống (system / 시스템) underdetermined, có infinitely many chính xác (exact / 정확한) solutions; pseudoinverse chọn solution có smallest Euclidean norm. Nếu hệ thống (system / 시스템) inconsistent, nó cho least-squares fit.

Nhưng tiny singular values gây amplification, nên practical inverse problems thường cần regularization thay vì blindly using every reciprocal.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Least squares, SVD và ma trận (matrix / 행렬) decompositions: projection, approximation và cấu trúc (structure / 구조)**, **Regularization: chấp nhận độ lệch (bias / 편향) để giảm variance** tiếp nhận điểm tựa từ **Pseudoinverse: inverse khi inverse thật không tồn tại** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Low-rank approximation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Regularization: chấp nhận độ lệch (bias / 편향) để giảm variance

Ridge regression solve

```math
\min_x \|Ax-b\|_2^2+\lambda\|x\|_2^2.
```

Normal equations trở thành

```math
(A^TA+\lambda I)x=A^Tb.
```

Term `\lambda I` làm weak directions bớt nguy hiểm. Ta cố ý độ lệch (bias / 편향) solution toward smaller norm để giảm sensitivity to noise.

Trong SVD coordinates, ridge không invert tiny singular values một cách hung hăng; nó damp chúng. Đây là cách nhìn geometric/numerical rõ hơn việc chỉ gọi regularization là “chống overfitting”.

> **Chuyển mạch:** Trong **Least squares, SVD và ma trận (matrix / 행렬) decompositions: projection, approximation và cấu trúc (structure / 구조)**, **Low-rank approximation** tiếp nhận điểm tựa từ **Regularization: chấp nhận độ lệch (bias / 편향) để giảm variance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **PCA quan hệ (relation / 관계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Low-rank approximation

Giữ top `k` singular values:

```math
A_k=U_k\Sigma_kV_k^T.
```

Eckart–Young theorem nói đây là best rank-`k` approximation theo Frobenius norm và spectral norm.

Meaning: nếu ma trận (matrix / 행렬) thật sự có dominant low-dimensional cấu trúc (structure / 구조), ta có thể bỏ weak directions với minimum possible reconstruction lỗi (error / 오류) trong lớp (class / 클래스) rank-`k`.

> **Chuyển mạch:** Ở chặng này của **Least squares, SVD và ma trận (matrix / 행렬) decompositions: projection, approximation và cấu trúc (structure / 구조)**, **PCA quan hệ (relation / 관계)** tiếp nhận điểm tựa từ **Low-rank approximation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Compression và recommender các hệ thống (systems / 시스템들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## PCA quan hệ (relation / 관계)

Với centered dữ liệu (data / 데이터) ma trận (matrix / 행렬) `X`, PCA directions là eigenvectors của covariance ma trận (matrix / 행렬), nhưng compute trực tiếp qua SVD thường tốt hơn:

```math
X=U\Sigma V^T.
```

Columns của `V` là principal directions trong tính năng (feature / 기능) không gian (space / 공간); squared singular values liên hệ với explained variance.

PCA vì vậy là một change-of-basis bài toán (problem / 문제): tìm orthogonal axes theo thứ tự variance decreasing.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Least squares, SVD và ma trận (matrix / 행렬) decompositions: projection, approximation và cấu trúc (structure / 구조)**, **Compression và recommender các hệ thống (systems / 시스템들)** tiếp nhận điểm tựa từ **PCA quan hệ (relation / 관계)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Finance liên kết (connection / 연결) — factor các mô hình (models / 모델들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Compression và recommender các hệ thống (systems / 시스템들)

Ảnh (image / 이미지) ma trận (matrix / 행렬) thường có correlated cấu trúc (structure / 구조), nên rank thấp có thể approximate tốt. Recommender các hệ thống (systems / 시스템들) cũng assume user-item interactions có latent factors nhỏ hơn observed dimension rất nhiều.

Nhưng low-rank giả định (assumption / 가정) là mô hình (model / 모델) giả định (assumption / 가정). Nếu dữ liệu (data / 데이터) không có low-rank cấu trúc (structure / 구조), compression hoặc latent-factor interpretation sẽ kém.

> **Chuyển mạch:** Trong **Least squares, SVD và ma trận (matrix / 행렬) decompositions: projection, approximation và cấu trúc (structure / 구조)**, sau nội dung của **Compression và recommender các hệ thống (systems / 시스템들)**, **Finance liên kết (connection / 연결) — factor các mô hình (models / 모델들)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **AI liên kết (connection / 연결) — embeddings và low-rank parameterization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Finance liên kết (connection / 연결) — factor các mô hình (models / 모델들)

Return ma trận (matrix / 행렬) có thể được approximate bằng vài dùng chung (common / 공통) factors:

```math
R\approx FB^T.
```

Đây là low-rank idea. PCA có thể tìm statistical factors, nhưng statistical principal directions không tự động có economic meaning. Một direction maximize variance chưa chắc là factor có interpretation nhân quả (causal / 인과적).

> **Chuyển mạch:** Ở chặng này của **Least squares, SVD và ma trận (matrix / 행렬) decompositions: projection, approximation và cấu trúc (structure / 구조)**, **AI liên kết (connection / 연결) — embeddings và low-rank parameterization** tiếp nhận điểm tựa từ **Finance liên kết (connection / 연결) — factor các mô hình (models / 모델들)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ma trận (matrix / 행렬) decompositions là chiến lược (strategy / 전략) chung** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## AI liên kết (connection / 연결) — embeddings và low-rank parameterization

Large matrices trong neural networks có thể được approximated hoặc adapted bằng low-rank factors. LoRA-style ideas khai thác giả định rằng useful cập nhật (update / 업데이트) nằm trong subspace dimension nhỏ hơn full parameter không gian (space / 공간).

SVD cũng giúp hiểu why low-rank representations compress thông tin (information / 정보), nhưng trained low-rank adapters không đơn giản là “SVD của mô hình (model / 모델)”. cấu trúc (structure / 구조) và tối ưu hóa (optimization / 최적화) đường dẫn (path / 경로) khác nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Least squares, SVD và ma trận (matrix / 행렬) decompositions: projection, approximation và cấu trúc (structure / 구조)**, **Ma trận (matrix / 행렬) decompositions là chiến lược (strategy / 전략) chung** tiếp nhận điểm tựa từ **AI liên kết (connection / 연결) — embeddings và low-rank parameterization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thất bại (failure / 실패) modes và các giả định (assumptions / 가정들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ma trận (matrix / 행렬) decompositions là chiến lược (strategy / 전략) chung

LU, QR, Cholesky, eigendecomposition và SVD không phải các tricks rời rạc. Ý tưởng chung là factor một operator khó thành sản phẩm (product / 제품) của operators có cấu trúc (structure / 구조) dễ xử lý.

- LU: triangular các hệ thống (systems / 시스템들), useful cho repeated solves;
- Cholesky: symmetric positive-definite matrices, nhanh và efficient;
- QR: orthogonalization và least squares;
- eigendecomposition: natural bất biến (invariant / 불변식) directions khi possible;
- SVD: universal orthogonal đầu vào (input / 입력)/đầu ra (output / 출력) directions.

Chọn decomposition phụ thuộc ma trận (matrix / 행렬) cấu trúc (structure / 구조) và tác vụ (task / 작업), không có một decomposition “tốt nhất” cho mọi bài toán (problem / 문제).

> **Chuyển mạch:** Trong **Least squares, SVD và ma trận (matrix / 행렬) decompositions: projection, approximation và cấu trúc (structure / 구조)**, **Thất bại (failure / 실패) modes và các giả định (assumptions / 가정들)** tiếp nhận điểm tựa từ **Ma trận (matrix / 행렬) decompositions là chiến lược (strategy / 전략) chung** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thất bại (failure / 실패) modes và các giả định (assumptions / 가정들)

Squared mất mát (loss / 손실) nhạy với outliers vì residual lớn bị square. Robust regression có thể dùng L1/Huber losses.

SVD trên raw features bị ảnh hưởng mạnh bởi quy mô (scale / 규모). Nếu một tính năng (feature / 기능) đo bằng thousands và tính năng (feature / 기능) khác bằng units, variance hình học (geometry / 기하학) có thể chủ yếu phản ánh units. Standardization cần dựa trên lĩnh vực (domain / 도메인) meaning, không áp dụng máy móc.

Low-rank truncation có thể xóa weak nhưng meaningful tín hiệu (signal / 신호). “Small singular giá trị (value / 값)” chỉ nói weak tuyến tính (linear / 선형) direction relative to chosen scaling, không nói nghiệp vụ (business / 비즈니스) importance bằng zero.

> **Chuyển mạch:** Ở chặng này của **Least squares, SVD và ma trận (matrix / 행렬) decompositions: projection, approximation và cấu trúc (structure / 구조)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Thất bại (failure / 실패) modes và các giả định (assumptions / 가정들)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Least squares là projection: khi mục tiêu (target / 대상) nằm ngoài reachable subspace, chọn reachable điểm (point / 지점) gần nhất. QR xây coordinates ổn định cho subspace đó. SVD bóc một tuyến tính (linear / 선형) map thành orthogonal đầu vào (input / 입력) directions, independent scaling strengths và orthogonal đầu ra (output / 출력) directions. Tiny singular values là directions gần mất thông tin; regularization quyết định không cố phục hồi chúng quá mức.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Least squares, SVD và ma trận (matrix / 행렬) decompositions: projection, approximation và cấu trúc (structure / 구조)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“Least squares fit tốt nghĩa mô hình (model / 모델) đúng.”** Không. Nó chỉ tối ưu trong mô hình (model / 모델) family và mất mát (loss / 손실) đã chọn.

**“Normal equations là cách chuẩn nhất để mã (code / 코드) regression.”** Chúng tốt để derive lý thuyết (theory / 이론) nhưng QR/SVD thường preferable numerically.

**“SVD chỉ dùng cho square matrices.”** Sai. SVD tồn tại cho rectangular matrices và chính đó là một ưu điểm lớn.

**“PCA tìm các features quan trọng nhất.”** PCA tìm directions có variance lớn nhất, không trực tiếp tìm nhân quả (causal / 인과적) hoặc predictive importance.

**“Tiny singular values nên luôn xóa.”** Không. Threshold là modeling/numerical quyết định (decision / 결정) dựa trên noise, quy mô (scale / 규모) và purpose.

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
