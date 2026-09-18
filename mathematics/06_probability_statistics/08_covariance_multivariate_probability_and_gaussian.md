# Covariance, xác suất nhiều biến và multivariate Gaussian

Một biến ngẫu nhiên đơn lẻ mô tả uncertainty theo một dimension. Nhưng dữ liệu thực tế thường có nhiều quantities cùng thay đổi: height và weight, return của nhiều assets, pixels trong image, features trong ML. Khi đó câu hỏi không chỉ là từng variable biến thiên bao nhiêu, mà còn **chúng biến thiên cùng nhau thế nào**.

## Joint distribution

Với hai random variables `X,Y`, joint distribution mô tả probability của pairs `(X,Y)`.

Discrete case dùng joint probability mass function:

```math
p(x,y)=P(X=x,Y=y).
```

Continuous case dùng density `f(x,y)` sao cho probability trên region `A` là

```math
P((X,Y)\in A)=\iint_A f(x,y)\,dx\,dy.
```

Marginal distribution của `X` được lấy bằng cách sum/integrate out `Y`:

```math
f_X(x)=\int f(x,y)\,dy.
```

“Marginalize” nghĩa bỏ một dimension uncertainty bằng accumulation qua tất cả values có thể của dimension đó.

## Covariance

Covariance (Covariance / 공분산) được định nghĩa

```math
\operatorname{Cov}(X,Y)
=E[(X-E[X])(Y-E[Y])].
```

Tương đương

```math
\operatorname{Cov}(X,Y)=E[XY]-E[X]E[Y].
```

Nếu `X` thường cao hơn mean khi `Y` cũng cao hơn mean, product deviations thường dương nên covariance dương. Nếu một biến cao khi biến kia thấp, covariance âm.

Units của covariance là product units của hai variables, nên magnitude khó so giữa datasets.

## Correlation là covariance đã chuẩn hóa

Pearson correlation:

```math
\rho_{XY}=
\frac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y}.
```

Nó dimensionless và nằm trong `[-1,1]` khi variances hữu hạn.

`\rho=1` hoặc `-1` nghĩa perfect linear relationship. `\rho=0` nghĩa zero linear covariance, không nhất thiết independence.

Ví dụ nếu `X` symmetric quanh 0 và `Y=X^2`, relationship deterministic nhưng covariance có thể bằng 0 vì positive/negative `X` cancel.

## Independence mạnh hơn uncorrelated

Nếu `X,Y` independent, thì khi expectations tồn tại:

```math
E[XY]=E[X]E[Y],
```

nên covariance bằng 0.

Chiều ngược thường sai. Một exception quan trọng: với jointly Gaussian variables, zero covariance implies independence.

## Covariance matrix

Cho random vector

```math
X=\begin{bmatrix}X_1\\\vdots\\X_n\end{bmatrix},
```

mean vector là

```math
\mu=E[X].
```

Covariance matrix:

```math
\Sigma=E[(X-\mu)(X-\mu)^T].
```

Entry diagonal là variances; off-diagonal là pairwise covariances.

`\Sigma` luôn symmetric và positive semidefinite vì với mọi vector `a`:

```math
a^T\Sigma a
=\operatorname{Var}(a^TX)\ge0.
```

Đây là bridge sâu giữa probability và linear algebra.

## Geometry của covariance

Trong 2D, data cloud có thể dài theo một diagonal direction. Covariance matrix encode orientation và spread của ellipse xác suất.

Eigenvectors của `\Sigma` cho principal directions; eigenvalues cho variance dọc theo các directions đó. PCA khai thác chính structure này để rotate coordinate system sang axes mà covariance matrix trở thành diagonal.

## Multivariate Gaussian

Multivariate normal distribution có density

```math
f(x)=\frac{1}{(2\pi)^{n/2}|\Sigma|^{1/2}}
\exp\left(
-\frac12(x-\mu)^T\Sigma^{-1}(x-\mu)
\right).
```

Quadratic form

```math
(x-\mu)^T\Sigma^{-1}(x-\mu)
```

là squared Mahalanobis distance: distance đã điều chỉnh theo variance và correlations.

Nếu một direction có variance lớn, deviation dọc direction đó ít “surprising” hơn cùng Euclidean distance ở direction variance nhỏ.

## Linear transformations của random vectors

Nếu

```math
Y=AX+b,
```

thì

```math
E[Y]=A\mu+b
```

và

```math
\operatorname{Cov}(Y)=A\Sigma A^T.
```

Công thức covariance transformation là một lý do matrices xuất hiện tự nhiên trong uncertainty propagation.

Trong sensor fusion, finance và Kalman filtering, ta repeatedly transform means và covariance matrices để track uncertainty.

## Portfolio variance

Nếu asset return vector là `R`, portfolio weights `w`, portfolio return là

```math
R_p=w^TR.
```

Variance:

```math
\operatorname{Var}(R_p)=w^T\Sigma w.
```

Diversification không chỉ phụ thuộc individual variances mà phụ thuộc covariances. Hai assets biến động mạnh nhưng negatively correlated có thể giảm total portfolio variance khi kết hợp.

## Knowledge Connection

Covariance nối probability với dot products và quadratic forms. PCA diagonalizes covariance. Gaussian models nối determinant, inverse matrix và exponential. Regression, Kalman filters, Gaussian processes và portfolio optimization đều dựa trên multivariate uncertainty structure.

## Mental Model

> Variance hỏi một variable phân tán bao nhiêu. Covariance hỏi hai variables nghiêng cùng nhau thế nào. Covariance matrix gom toàn bộ hình học của spread bậc hai thành một linear-algebra object.

## Common Misconceptions

Zero correlation không nói chung imply independence. Covariance magnitude phụ thuộc units. Correlation gần 1 không chứng minh causality. Covariance matrix singular có thể xảy ra khi một feature là linear combination của các features khác; khi đó inverse không tồn tại và model Gaussian full-rank cần xử lý riêng.
