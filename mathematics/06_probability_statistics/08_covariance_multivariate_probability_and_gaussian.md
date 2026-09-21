# Covariance, xác suất nhiều biến và Gaussian geometry

Một random variable mô tả uncertainty theo một dimension. Dữ liệu thực tế thường nhiều chiều: height–weight, asset returns, sensor readings, pixels, embeddings, features. Khi đó câu hỏi không chỉ là từng biến phân tán bao nhiêu, mà là **chúng cùng biến động theo cấu trúc nào**.

Core chain:

```text
joint distribution
→ marginal / conditional
→ covariance
→ covariance matrix
→ quadratic geometry
→ Gaussian model
→ linear transforms / inference / optimization
```

## 1. Joint distribution: uncertainty trên nhiều dimensions

Với two variables `X,Y`, joint distribution mô tả probability của pairs `(X,Y)`.

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

Joint distribution chứa nhiều information hơn hai marginals riêng lẻ, vì nó encode dependence structure.

## 2. Marginalization là “sum out” uncertainty không quan tâm

Continuous case:

```math
f_X(x)=\int f(x,y)\,dy.
```

Discrete:

```math
p_X(x)=\sum_y p(x,y).
```

Marginalization là operation cực kỳ quan trọng trong probability, Bayesian inference và probabilistic graphical models.

## 3. Conditional distribution

Nếu `f_Y(y)>0`:

```math
f_{X|Y}(x|y)
=
\frac{f_{X,Y}(x,y)}{f_Y(y)}.
```

Conditional distribution trả lời: sau khi biết một coordinate/value, uncertainty ở coordinate khác thay đổi thế nào?

Đây là multivariate version của Bayes/conditional probability.

## 4. Independence factorizes joint distribution

Nếu `X,Y` independent:

```math
f(x,y)=f_X(x)f_Y(y).
```

Geometrically/statistically, knowing one variable không thay distribution của variable kia.

Dependence có thể tồn tại ngay cả khi covariance bằng 0.

## 5. Covariance: signed co-movement quanh means

```math
\operatorname{Cov}(X,Y)
=
E[(X-E[X])(Y-E[Y])].
```

Equivalent:

```math
\operatorname{Cov}(X,Y)=E[XY]-E[X]E[Y].
```

Positive covariance: deviations thường cùng sign. Negative: opposite signs. Zero: không có linear co-movement theo measure này.

## 6. Covariance phụ thuộc units

Nếu `X` đo meter và `Y` đo kilogram, covariance có unit `m·kg`.

Scale `X` by 100:

```math
\operatorname{Cov}(100X,Y)=100\operatorname{Cov}(X,Y).
```

Do đó covariance magnitude không comparable trực tiếp across differently scaled variables.

## 7. Correlation chuẩn hóa covariance

```math
\rho_{XY}
=
\frac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y}.
```

Correlation dimensionless và nằm `[-1,1]` khi variances finite/nonzero.

Nhưng correlation chỉ capture linear association. Nếu `Y=X^2` với symmetric `X`, correlation có thể zero dù dependence deterministic.

## 8. Covariance matrix

Random vector:

```math
X=
\begin{bmatrix}
X_1\\\vdots\\X_n
\end{bmatrix},
\qquad
\mu=E[X].
```

Covariance matrix:

```math
\Sigma
=E[(X-\mu)(X-\mu)^T].
```

Entries:

```math
\Sigma_{ij}=\operatorname{Cov}(X_i,X_j).
```

Diagonal = variances. Off-diagonal = pairwise covariances.

## 9. Vì sao covariance matrix positive semidefinite?

Với any vector `a`:

```math
a^T\Sigma a
=
\operatorname{Var}(a^TX)
\ge0.
```

Do đó `\Sigma` symmetric positive semidefinite.

Đây là bridge rất sâu: một probability object trở thành quadratic form trong Linear Algebra.

## 10. Variance của linear combination

Nếu scalar:

```math
Y=a^TX,
```

thì:

```math
\operatorname{Var}(Y)=a^T\Sigma a.
```

Đây là formula dùng khắp Finance, signal processing, uncertainty propagation và portfolio optimization.

## 11. Geometry của covariance ellipse

Level sets:

```math
(x-\mu)^T\Sigma^{-1}(x-\mu)=c
```

là ellipses/ellipsoids nếu `\Sigma` positive definite.

Eigenvectors của `\Sigma` cho principal directions. Eigenvalues cho variance dọc mỗi direction.

Do đó covariance matrix encode orientation + spread của probability cloud.

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

Đây không phải magic dimensionality reduction; nó là basis change theo covariance geometry.

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

## 14. Mahalanobis distance

```math
d_M(x,\mu)^2
=(x-\mu)^T\Sigma^{-1}(x-\mu).
```

Euclidean distance coi mọi directions cùng scale. Mahalanobis distance chuẩn hóa theo covariance.

Deviation dọc high-variance direction ít surprising hơn same Euclidean displacement dọc low-variance direction.

## 15. Whitening

Nếu `\Sigma=Q\Lambda Q^T`, whitening transform conceptually:

```math
Z=\Lambda^{-1/2}Q^T(X-\mu)
```

cho covariance gần identity.

Whitening rotate + rescale để remove second-order correlation structure.

Trong ML preprocessing, whitening có thể useful nhưng cũng có numerical/noise issues nếu eigenvalues nhỏ.

## 16. Linear transformation of uncertainty

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

Đây là uncertainty propagation chính xác cho linear maps.

## 17. First-order nonlinear uncertainty propagation

Với nonlinear `Y=g(X)`, linearize quanh mean:

```math
Y\approx g(\mu)+J(X-\mu).
```

Do đó:

```math
\operatorname{Cov}(Y)
\approx J\Sigma J^T.
```

Đây là connection giữa Jacobian, Taylor approximation và covariance propagation.

## 18. Conditional Gaussian

Một đặc tính quan trọng của multivariate Gaussian: conditional distributions vẫn Gaussian.

Partition:

```math
X=
\begin{bmatrix}X_1\\X_2\end{bmatrix}
```

với block covariance. Conditional mean của one block given another là affine function của observed value; conditional covariance giảm theo information gained.

Structure này đứng sau Gaussian regression, Kalman filtering và nhiều probabilistic models.

## 19. Zero covariance và independence

General case:

```text
independence ⇒ covariance zero
```

nhưng converse sai.

Special jointly Gaussian case:

```text
zero covariance ⇔ independence
```

Đây là lý do Gaussian models đặc biệt tractable: second-order structure đủ mô tả dependence hoàn toàn.

## 20. Singular covariance

Nếu features có exact linear dependency, `\Sigma` singular.

Ví dụ:

```math
X_3=X_1+X_2.
```

Random vector thực chất sống trên lower-dimensional subspace.

Then:

```math
|\Sigma|=0,
```

và inverse không tồn tại.

Conceptually đây không chỉ là numerical bug; nó nói support của distribution collapse xuống dimension thấp hơn.

## 21. Portfolio variance

Asset return vector `R`, weights `w`:

```math
R_p=w^TR.
```

Portfolio variance:

```math
\operatorname{Var}(R_p)=w^T\Sigma w.
```

Diversification phụ thuộc covariance, không chỉ individual volatility.

Hai assets risk riêng cao vẫn có thể giảm portfolio variance nếu co-movement thấp/negative.

## 22. Correlation matrix và feature scaling

Correlation matrix là covariance của standardized variables.

Nó hữu ích khi features có units/scales khác nhau. Nhưng standardization thay geometry; không phải luôn correct choice nếu absolute scale mang domain meaning.

## 23. Gaussian không tự động đúng vì data “trông bell-shaped”

Multivariate Gaussian assumptions gồm shape của joint distribution, not just each marginal.

Có distributions mà each marginal Gaussian nhưng joint structure không jointly Gaussian.

Outliers/heavy tails cũng có thể phá covariance estimates mạnh.

## 24. Robustness và heavy tails

Sample covariance nhạy với extreme points vì dùng squared deviations/products.

Trong Finance hoặc sensor data có heavy tails/outliers, covariance estimate có thể unstable. Robust covariance, shrinkage hoặc heavy-tailed models có thể phù hợp hơn.

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

Covariance term quyết định diversification benefit; không thể tính portfolio risk bằng average volatilities.

## Knowledge Connection

```text
probability
→ covariance
→ quadratic forms
→ eigenvectors/PCA
→ Gaussian geometry
→ regression/Kalman/portfolio optimization
```

Trong AI, covariance links tới feature normalization, PCA và Gaussian latent models. Trong Physics, covariance describes fluctuations. Trong Finance, covariance drives quadratic portfolio risk.

## Mental Model

> Covariance matrix là metric-like map của uncertainty: nó cho biết cloud trải rộng theo directions nào và variables co-move ra sao. Gaussian model biến structure đó thành ellipsoidal probability geometry.

## Common Misconceptions

Zero correlation không nói chung imply independence. Correlation không imply causation. Covariance magnitude phụ thuộc units. Singular covariance có thể phản ánh genuine lower-dimensional structure. Gaussian marginals không đảm bảo joint Gaussian. Inverting a poorly conditioned covariance matrix có thể numerically unstable.
