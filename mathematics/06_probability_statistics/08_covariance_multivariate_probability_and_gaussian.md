# Covariance, xác suất nhiều biến và Gaussian hình học (geometry / 기하학)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Covariance, xác suất nhiều biến và Gaussian hình học (geometry / 기하학)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Joint phân phối (distribution / 분포): bất định (uncertainty / 불확실성) trên nhiều dimensions** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Marginalization là “sum out” bất định (uncertainty / 불확실성) không quan tâm** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối covariance với multivariate probability và Gaussian, để dependence giữa biến trở thành ma trận có thể phân tích.

Một random variable mô tả bất định (uncertainty / 불확실성) theo một dimension. Dữ liệu thực tế thường nhiều chiều: height–weight, asset returns, sensor readings, pixels, embeddings, features. Khi đó câu hỏi không chỉ là từng biến phân tán bao nhiêu, mà là **chúng cùng biến động theo cấu trúc nào**.

Cốt lõi (core / 핵심) chuỗi (chain / 사슬):

```text
joint distribution
→ marginal / conditional
→ covariance
→ covariance matrix
→ quadratic geometry
→ Gaussian model
→ linear transforms / inference / optimization
```

## 1. Joint phân phối (distribution / 분포): bất định (uncertainty / 불확실성) trên nhiều dimensions

Với two variables `X,Y`, joint phân phối (distribution / 분포) mô tả xác suất (probability / 확률) của pairs `(X,Y)`.

Discrete:

```math
p(x,y)=P(X=x,Y=y).
```

Continuous:

```math
P((X,Y)\in A)
=
\iint_A f(x,y)\,dx\,dy.
```

Joint phân phối (distribution / 분포) chứa nhiều thông tin (information / 정보) hơn hai marginals riêng lẻ, vì nó encode dependence cấu trúc (structure / 구조).

> **Chuyển mạch:** Trong **Covariance, xác suất nhiều biến và Gaussian hình học (geometry / 기하학)**, **2. Marginalization là “sum out” bất định (uncertainty / 불확실성) không quan tâm** tiếp nhận điểm tựa từ **1. Joint phân phối (distribution / 분포): bất định (uncertainty / 불확실성) trên nhiều dimensions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Conditional phân phối (distribution / 분포)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Marginalization là “sum out” bất định (uncertainty / 불확실성) không quan tâm

Continuous trường hợp (case / 사례):

```math
f_X(x)=\int f(x,y)\,dy.
```

Discrete:

```math
p_X(x)=\sum_y p(x,y).
```

Marginalization là thao tác (operation / 연산) cực kỳ quan trọng trong xác suất (probability / 확률), Bayesian suy luận (inference / 추론) và probabilistic graphical các mô hình (models / 모델들).

> **Chuyển mạch:** Ở chặng này của **Covariance, xác suất nhiều biến và Gaussian hình học (geometry / 기하학)**, **3. Conditional phân phối (distribution / 분포)** tiếp nhận điểm tựa từ **2. Marginalization là “sum out” bất định (uncertainty / 불확실성) không quan tâm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Independence factorizes joint phân phối (distribution / 분포)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Conditional phân phối (distribution / 분포)

Nếu `f_Y(y)>0`:

```math
f_{X|Y}(x|y)
=
\frac{f_{X,Y}(x,y)}{f_Y(y)}.
```

Conditional phân phối (distribution / 분포) trả lời: sau khi biết một coordinate/giá trị (value / 값), bất định (uncertainty / 불확실성) ở coordinate khác thay đổi thế nào?

Đây là multivariate phiên bản (version / 버전) của Bayes/conditional xác suất (probability / 확률).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Covariance, xác suất nhiều biến và Gaussian hình học (geometry / 기하학)**, **4. Independence factorizes joint phân phối (distribution / 분포)** tiếp nhận điểm tựa từ **3. Conditional phân phối (distribution / 분포)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Covariance: signed co-movement quanh means** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Independence factorizes joint phân phối (distribution / 분포)

Nếu `X,Y` independent:

```math
f(x,y)=f_X(x)f_Y(y).
```

Geometrically/statistically, knowing one variable không thay phân phối (distribution / 분포) của variable kia.

Dependence có thể tồn tại ngay cả khi covariance bằng 0.

> **Chuyển mạch:** Trong **Covariance, xác suất nhiều biến và Gaussian hình học (geometry / 기하학)**, **5. Covariance: signed co-movement quanh means** tiếp nhận điểm tựa từ **4. Independence factorizes joint phân phối (distribution / 분포)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Covariance phụ thuộc units** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Covariance: signed co-movement quanh means

Covariance giữ dấu của việc hai biến cùng lệch khỏi mean hay lệch ngược nhau. Độ lớn còn phụ thuộc scale, nên cần chuẩn hóa hoặc đặt trong ma trận covariance khi so sánh.

```math
\operatorname{Cov}(X,Y)
=
E[(X-E[X])(Y-E[Y])].
```

Equivalent:

```math
\operatorname{Cov}(X,Y)=E[XY]-E[X]E[Y].
```

Positive covariance: deviations thường cùng sign. Negative: opposite signs. Zero: không có tuyến tính (linear / 선형) co-movement theo measure này.

> **Chuyển mạch:** Ở chặng này của **Covariance, xác suất nhiều biến và Gaussian hình học (geometry / 기하학)**, **6. Covariance phụ thuộc units** tiếp nhận điểm tựa từ **5. Covariance: signed co-movement quanh means** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Correlation chuẩn hóa covariance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Covariance phụ thuộc units

Nếu `X` đo meter và `Y` đo kilogram, covariance có đơn vị (unit / 단위) `m·kg`.

Quy mô (scale / 규모) `X` by 100:

```math
\operatorname{Cov}(100X,Y)=100\operatorname{Cov}(X,Y).
```

Do đó covariance magnitude không comparable trực tiếp across differently scaled variables.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Covariance, xác suất nhiều biến và Gaussian hình học (geometry / 기하학)**, **7. Correlation chuẩn hóa covariance** tiếp nhận điểm tựa từ **6. Covariance phụ thuộc units** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Covariance ma trận (matrix / 행렬)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Correlation chuẩn hóa covariance

Correlation đưa covariance về khoảng chuẩn hóa để đọc mức liên hệ tuyến tính dễ hơn. Nó vẫn chỉ là summary của một khía cạnh dependence và có thể bỏ qua cấu trúc tail hoặc phi tuyến.

```math
\rho_{XY}
=
\frac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y}.
```

Correlation dimensionless và nằm `[-1,1]` khi variances finite/nonzero.

Nhưng correlation chỉ capture tuyến tính (linear / 선형) association. Nếu `Y=X^2` với symmetric `X`, correlation có thể zero dù dependence deterministic.

> **Chuyển mạch:** Trong **Covariance, xác suất nhiều biến và Gaussian hình học (geometry / 기하학)**, **8. Covariance ma trận (matrix / 행렬)** tiếp nhận điểm tựa từ **7. Correlation chuẩn hóa covariance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Vì sao covariance ma trận (matrix / 행렬) positive semidefinite?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Covariance ma trận (matrix / 행렬)

Random véc-tơ (vector / 벡터):

```math
X=
\begin{bmatrix}
X_1\\\vdots\\X_n
\end{bmatrix},
\qquad
\mu=E[X].
```

Covariance ma trận (matrix / 행렬):

```math
\Sigma
=E[(X-\mu)(X-\mu)^T].
```

Entries:

```math
\Sigma_{ij}=\operatorname{Cov}(X_i,X_j).
```

Diagonal = variances. Off-diagonal = pairwise covariances.

> **Chuyển mạch:** Ở chặng này của **Covariance, xác suất nhiều biến và Gaussian hình học (geometry / 기하학)**, **9. Vì sao covariance ma trận (matrix / 행렬) positive semidefinite?** tiếp nhận điểm tựa từ **8. Covariance ma trận (matrix / 행렬)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Variance của tuyến tính (linear / 선형) combination** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Vì sao covariance ma trận (matrix / 행렬) positive semidefinite?

Với any véc-tơ (vector / 벡터) `a`:

```math
a^T\Sigma a
=
\operatorname{Var}(a^TX)
\ge0.
```

Do đó `\Sigma` symmetric positive semidefinite.

Đây là cầu nối (bridge / 브리지) rất sâu: một xác suất (probability / 확률) đối tượng (object / 객체) trở thành quadratic form trong tuyến tính (linear / 선형) Algebra.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Covariance, xác suất nhiều biến và Gaussian hình học (geometry / 기하학)**, **10. Variance của tuyến tính (linear / 선형) combination** tiếp nhận điểm tựa từ **9. Vì sao covariance ma trận (matrix / 행렬) positive semidefinite?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. hình học (geometry / 기하학) của covariance ellipse** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Variance của tuyến tính (linear / 선형) combination

Nếu scalar:

```math
Y=a^TX,
```

thì:

```math
\operatorname{Var}(Y)=a^T\Sigma a.
```

Đây là formula dùng khắp Finance, tín hiệu (signal / 신호) processing, bất định (uncertainty / 불확실성) propagation và portfolio tối ưu hóa (optimization / 최적화).

> **Chuyển mạch:** Trong **Covariance, xác suất nhiều biến và Gaussian hình học (geometry / 기하학)**, **11. hình học (geometry / 기하학) của covariance ellipse** tiếp nhận điểm tựa từ **10. Variance của tuyến tính (linear / 선형) combination** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. PCA là rotate sang covariance eigenbasis** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. hình học (geometry / 기하학) của covariance ellipse

Mức (level / 수준) sets:

```math
(x-\mu)^T\Sigma^{-1}(x-\mu)=c
```

là ellipses/ellipsoids nếu `\Sigma` positive definite.

Eigenvectors của `\Sigma` cho principal directions. Eigenvalues cho variance dọc mỗi direction.

Do đó covariance ma trận (matrix / 행렬) encode orientation + spread của xác suất (probability / 확률) cloud.

> **Chuyển mạch:** Ở chặng này của **Covariance, xác suất nhiều biến và Gaussian hình học (geometry / 기하학)**, **12. PCA là rotate sang covariance eigenbasis** tiếp nhận điểm tựa từ **11. hình học (geometry / 기하학) của covariance ellipse** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Multivariate Gaussian** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. PCA là rotate sang covariance eigenbasis

Nếu:

```math
\Sigma=Q\Lambda Q^T,
```

thì coordinates:

```math
Z=Q^T(X-\mu)
```

có diagonal covariance `\Lambda`.

PCA chọn directions có eigenvalues lớn nhất để giữ nhiều variance nhất.

Đây không phải magic dimensionality reduction; nó là basis thay đổi (change / 변경) theo covariance hình học (geometry / 기하학).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Covariance, xác suất nhiều biến và Gaussian hình học (geometry / 기하학)**, **13. Multivariate Gaussian** tiếp nhận điểm tựa từ **12. PCA là rotate sang covariance eigenbasis** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Mahalanobis distance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Multivariate Gaussian

Density:

```math
f(x)=
\frac1{(2\pi)^{n/2}|\Sigma|^{1/2}}
\exp\left[
-\frac12(x-\mu)^T\Sigma^{-1}(x-\mu)
\right].
```

Có ba structures chính:

```text
\mu → center
\Sigma → geometry/spread
|\Sigma| → volume scaling normalization
```

Quadratic exponent tạo ellipsoidal contours.

> **Chuyển mạch:** Trong **Covariance, xác suất nhiều biến và Gaussian hình học (geometry / 기하학)**, **14. Mahalanobis distance** tiếp nhận điểm tựa từ **13. Multivariate Gaussian** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Whitening** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Mahalanobis distance

Mahalanobis distance đo độ xa trong không gian đã tính tới covariance giữa các chiều. Vì vậy một lệch nhỏ theo hướng biến động thấp có thể đáng kể hơn một lệch lớn theo hướng biến động cao.

```math
d_M(x,\mu)^2
=(x-\mu)^T\Sigma^{-1}(x-\mu).
```

Euclidean distance coi mọi directions cùng quy mô (scale / 규모). Mahalanobis distance chuẩn hóa theo covariance.

Deviation dọc high-variance direction ít surprising hơn same Euclidean displacement dọc low-variance direction.

> **Chuyển mạch:** Ở chặng này của **Covariance, xác suất nhiều biến và Gaussian hình học (geometry / 기하학)**, **15. Whitening** tiếp nhận điểm tựa từ **14. Mahalanobis distance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. tuyến tính (linear / 선형) transformation of bất định (uncertainty / 불확실성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Whitening

Nếu `\Sigma=Q\Lambda Q^T`, whitening transform conceptually:

```math
Z=\Lambda^{-1/2}Q^T(X-\mu)
```

cho covariance gần định danh (identity / 식별자).

Whitening rotate + rescale để remove second-order correlation cấu trúc (structure / 구조).

Trong ML preprocessing, whitening có thể useful nhưng cũng có numerical/noise issues nếu eigenvalues nhỏ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Covariance, xác suất nhiều biến và Gaussian hình học (geometry / 기하학)**, **16. tuyến tính (linear / 선형) transformation of bất định (uncertainty / 불확실성)** tiếp nhận điểm tựa từ **15. Whitening** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. First-order nonlinear bất định (uncertainty / 불확실성) propagation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. tuyến tính (linear / 선형) transformation of bất định (uncertainty / 불확실성)

Nếu:

```math
Y=AX+b,
```

thì:

```math
E[Y]=A\mu+b,
```

```math
\operatorname{Cov}(Y)=A\Sigma A^T.
```

Derivation covariance:

```math
Y-E[Y]=A(X-\mu),
```

nên:

```math
E[A(X-\mu)(X-\mu)^TA^T]
=A\Sigma A^T.
```

Đây là bất định (uncertainty / 불확실성) propagation chính xác cho tuyến tính (linear / 선형) maps.

> **Chuyển mạch:** Trong **Covariance, xác suất nhiều biến và Gaussian hình học (geometry / 기하학)**, **17. First-order nonlinear bất định (uncertainty / 불확실성) propagation** tiếp nhận điểm tựa từ **16. tuyến tính (linear / 선형) transformation of bất định (uncertainty / 불확실성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Conditional Gaussian** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. First-order nonlinear bất định (uncertainty / 불확실성) propagation

Với nonlinear `Y=g(X)`, linearize quanh mean:

```math
Y\approx g(\mu)+J(X-\mu).
```

Do đó:

```math
\operatorname{Cov}(Y)
\approx J\Sigma J^T.
```

Đây là liên kết (connection / 연결) giữa Jacobian, Taylor approximation và covariance propagation.

> **Chuyển mạch:** Ở chặng này của **Covariance, xác suất nhiều biến và Gaussian hình học (geometry / 기하학)**, **18. Conditional Gaussian** tiếp nhận điểm tựa từ **17. First-order nonlinear bất định (uncertainty / 불확실성) propagation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Zero covariance và independence** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Conditional Gaussian

Một đặc tính quan trọng của multivariate Gaussian: conditional distributions vẫn Gaussian.

Partition:

```math
X=
\begin{bmatrix}X_1\\X_2\end{bmatrix}
```

với khối (block / 블록) covariance. Conditional mean của one khối (block / 블록) given another là affine hàm (function / 함수) của observed giá trị (value / 값); conditional covariance giảm theo thông tin (information / 정보) gained.

Cấu trúc (structure / 구조) này đứng sau Gaussian regression, Kalman filtering và nhiều probabilistic các mô hình (models / 모델들).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Covariance, xác suất nhiều biến và Gaussian hình học (geometry / 기하학)**, **19. Zero covariance và independence** tiếp nhận điểm tựa từ **18. Conditional Gaussian** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Singular covariance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Zero covariance và independence

General trường hợp (case / 사례):

```text
independence ⇒ covariance zero
```

nhưng converse sai.

Special jointly Gaussian trường hợp (case / 사례):

```text
zero covariance ⇔ independence
```

Đây là lý do Gaussian các mô hình (models / 모델들) đặc biệt tractable: second-order cấu trúc (structure / 구조) đủ mô tả dependence hoàn toàn.

> **Chuyển mạch:** Trong **Covariance, xác suất nhiều biến và Gaussian hình học (geometry / 기하학)**, **20. Singular covariance** tiếp nhận điểm tựa từ **19. Zero covariance và independence** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Portfolio variance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Singular covariance

Nếu features có chính xác (exact / 정확한) tuyến tính (linear / 선형) phụ thuộc (dependency / 의존성), `\Sigma` singular.

Ví dụ:

```math
X_3=X_1+X_2.
```

Random véc-tơ (vector / 벡터) thực chất sống trên lower-dimensional subspace.

Then:

```math
|\Sigma|=0,
```

và inverse không tồn tại.

Conceptually đây không chỉ là numerical bug; nó nói hỗ trợ (support / 지원) của phân phối (distribution / 분포) collapse xuống dimension thấp hơn.

> **Chuyển mạch:** Ở chặng này của **Covariance, xác suất nhiều biến và Gaussian hình học (geometry / 기하학)**, **21. Portfolio variance** tiếp nhận điểm tựa từ **20. Singular covariance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Correlation ma trận (matrix / 행렬) và tính năng (feature / 기능) scaling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Portfolio variance

Asset return véc-tơ (vector / 벡터) `R`, weights `w`:

```math
R_p=w^TR.
```

Portfolio variance:

```math
\operatorname{Var}(R_p)=w^T\Sigma w.
```

Diversification phụ thuộc covariance, không chỉ individual volatility.

Hai assets rủi ro (risk / 위험) riêng cao vẫn có thể giảm portfolio variance nếu co-movement thấp/negative.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Covariance, xác suất nhiều biến và Gaussian hình học (geometry / 기하학)**, **22. Correlation ma trận (matrix / 행렬) và tính năng (feature / 기능) scaling** tiếp nhận điểm tựa từ **21. Portfolio variance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Gaussian không tự động đúng vì dữ liệu (data / 데이터) “trông bell-shaped”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Correlation ma trận (matrix / 행렬) và tính năng (feature / 기능) scaling

Correlation ma trận (matrix / 행렬) là covariance của standardized variables.

Nó hữu ích khi features có units/scales khác nhau. Nhưng standardization thay hình học (geometry / 기하학); không phải luôn correct choice nếu absolute quy mô (scale / 규모) mang lĩnh vực (domain / 도메인) meaning.

> **Chuyển mạch:** Trong **Covariance, xác suất nhiều biến và Gaussian hình học (geometry / 기하학)**, **22. Correlation ma trận (matrix / 행렬) và tính năng (feature / 기능) scaling** nêu điều cần giải thích; **23. Gaussian không tự động đúng vì dữ liệu (data / 데이터) “trông bell-shaped”** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **24. Robustness và heavy tails** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Gaussian không tự động đúng vì dữ liệu (data / 데이터) “trông bell-shaped”

Multivariate Gaussian các giả định (assumptions / 가정들) gồm shape của joint phân phối (distribution / 분포), not just each marginal.

Có distributions mà each marginal Gaussian nhưng joint cấu trúc (structure / 구조) không jointly Gaussian.

Outliers/heavy tails cũng có thể phá covariance estimates mạnh.

> **Chuyển mạch:** Ở chặng này của **Covariance, xác suất nhiều biến và Gaussian hình học (geometry / 기하학)**, **23. Gaussian không tự động đúng vì dữ liệu (data / 데이터) “trông bell-shaped”** nêu điều cần giải thích; **24. Robustness và heavy tails** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **25. Worked example: two-asset portfolio** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Robustness và heavy tails

Mẫu (sample / 표본) covariance nhạy với extreme points vì dùng squared deviations/products.

Trong Finance hoặc sensor dữ liệu (data / 데이터) có heavy tails/outliers, covariance estimate có thể unstable. Robust covariance, shrinkage hoặc heavy-tailed các mô hình (models / 모델들) có thể phù hợp hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Covariance, xác suất nhiều biến và Gaussian hình học (geometry / 기하학)**, **24. Robustness và heavy tails** cho ta quy tắc; **25. Worked example: two-asset portfolio** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Worked example: two-asset portfolio

Giả sử:

```math
\sigma_1=0.20,
\qquad
\sigma_2=0.10,
\qquad
\rho=0.2.
```

Covariance:

```math
\sigma_{12}=\rho\sigma_1\sigma_2=0.004.
```

Equal weights `w=(0.5,0.5)`:

```math
\operatorname{Var}(R_p)
=0.25(0.20^2)+0.25(0.10^2)+2(0.25)(0.004).
```

Covariance term quyết định diversification benefit; không thể tính portfolio rủi ro (risk / 위험) bằng average volatilities.

> **Chuyển mạch:** Trong **Covariance, xác suất nhiều biến và Gaussian hình học (geometry / 기하학)**, **25. Worked example: two-asset portfolio** cho ta quy tắc; **Liên kết kiến thức (knowledge connection / 지식 연결)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Phần kết nối đưa covariance, Gaussian và Mahalanobis vào PCA, anomaly detection, portfolio risk và multivariate inference. Hãy giữ covariance structure khi chuyển từ một biến sang nhiều biến.

```text
probability
→ covariance
→ quadratic forms
→ eigenvectors/PCA
→ Gaussian geometry
→ regression/Kalman/portfolio optimization
```

Trong AI, covariance links tới tính năng (feature / 기능) normalization, PCA và Gaussian latent các mô hình (models / 모델들). Trong Physics, covariance describes fluctuations. Trong Finance, covariance drives quadratic portfolio rủi ro (risk / 위험).

> **Chuyển mạch:** Ở chặng này của **Covariance, xác suất nhiều biến và Gaussian hình học (geometry / 기하학)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Liên kết kiến thức (knowledge connection / 지식 연결)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Covariance ma trận (matrix / 행렬) là metric-like map của bất định (uncertainty / 불확실성): nó cho biết cloud trải rộng theo directions nào và variables co-move ra sao. Gaussian mô hình (model / 모델) biến cấu trúc (structure / 구조) đó thành ellipsoidal xác suất (probability / 확률) hình học (geometry / 기하학).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Covariance, xác suất nhiều biến và Gaussian hình học (geometry / 기하학)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

Zero correlation không nói chung imply independence. Correlation không imply causation. Covariance magnitude phụ thuộc units. Singular covariance có thể phản ánh genuine lower-dimensional cấu trúc (structure / 구조). Gaussian marginals không đảm bảo joint Gaussian. Inverting a poorly conditioned covariance ma trận (matrix / 행렬) có thể numerically unstable.

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
