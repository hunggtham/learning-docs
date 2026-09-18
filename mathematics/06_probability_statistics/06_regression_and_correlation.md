# Hồi quy và tương quan

Hồi quy (Regression / 회귀) model relationship giữa outcome và predictors; tương quan (Correlation / 상관관계) đo association, thường tuyến tính trong Pearson correlation. Hai khái niệm liên quan nhưng không đồng nhất.

## Pearson correlation

Sample correlation:

```math
r=\frac{\sum_i(x_i-\bar x)(y_i-\bar y)}
{\sqrt{\sum_i(x_i-\bar x)^2}\sqrt{\sum_i(y_i-\bar y)^2}}
```

Đây là normalized covariance và cũng là cosine giữa centered data vectors.

`r≈1` strong positive linear association, `r≈-1` negative, `r≈0` weak linear association. Nonlinear relationship mạnh vẫn có thể `r≈0`.

## Simple linear regression

Model:

```math
y_i=\beta_0+\beta_1x_i+\varepsilon_i
```

Least squares chọn coefficients minimize

```math
\sum_i(y_i-\hat y_i)^2
```

Slope estimate trong simple regression liên hệ covariance/variance:

```math
\hat\beta_1=\frac{\operatorname{Cov}(x,y)}{\operatorname{Var}(x)}
```

under sample formula conventions.

## Matrix form

Multiple regression:

```math
y=X\beta+\varepsilon
```

Least squares estimate solves projection problem. Nếu full rank:

```math
\hat\beta=(X^TX)^{-1}X^Ty
```

conceptually; numerical software thường dùng QR/SVD.

## Interpretation of coefficient

Trong multiple regression, coefficient `β_j` mô tả expected change in outcome per unit predictor j holding other included predictors fixed, under model. “Holding fixed” là model comparison, không tự động causal intervention.

## Residual diagnostics

Residuals nên được inspect cho nonlinearity, heteroskedasticity, dependence và outliers. A single `R^2` cannot validate model assumptions.

`R^2` đo fraction variance explained relative to mean baseline in standard setup, nhưng high `R^2` không chứng minh causality hoặc good out-of-sample prediction.

## Overfitting

Thêm predictors thường không làm training SSE tăng, nhưng có thể worsen generalization. Train/test split, cross-validation và regularization quản lý tradeoff fit vs complexity.

## Regularization

Ridge regression adds

```math
\lambda\|\beta\|_2^2
```

Lasso adds

```math
\lambda\|\beta\|_1
```

Penalty thay optimization objective để control coefficient magnitude/sparsity.

## Correlation is not causation

Ice cream sales và drowning incidents có thể correlate vì common cause temperature/season. Regression adjustment có thể help nếu confounders measured/modelled appropriately, nhưng observational regression alone không magically establish causality.

## Mental Model

> Correlation đo geometric/statistical alignment; regression chọn một function để predict/describe conditional relationship. Causal interpretation cần design/assumptions bổ sung ngoài fit quality.

## Common Misconceptions

`r=0` không nghĩa “không có relationship”. High `R^2` không guarantee good prediction outside sample. Regression coefficient không mặc định là causal effect. Extrapolation ngoài data range có thể rất nguy hiểm.

## Worked Example: slope và units

Giả sử regress monthly electricity cost `y` (KRW) trên usage `x` (kWh):

```math
\hat y=120x+8000
```

Slope 120 có unit KRW/kWh; intercept 8,000 KRW có thể đại diện fixed charge nếu pricing/model phù hợp. Nếu data chỉ quan sát x từ 200–500 kWh, diễn giải intercept tại x=0 là extrapolation và có thể không meaningful.

## Confounding example

Nếu senior developers vừa có salary cao hơn vừa thường tham gia projects phức tạp hơn, simple regression project defects trên salary có thể thấy association không phải vì salary gây defects. Experience/project complexity/role cùng ảnh hưởng variables. Statistical control chỉ giải quyết confounders measured và correctly modeled; unmeasured confounding vẫn tồn tại.

## Logistic regression connection

Với binary outcome, linear regression có thể predict ngoài [0,1]. Logistic regression model log-odds:

```math
\log\frac{p}{1-p}=\beta_0+\beta^Tx
```

nên

```math
p=\frac{1}{1+e^{-(\beta_0+\beta^Tx)}}
```

Logarithm/exponential biến unconstrained real score thành valid probability. Đây là connection trực tiếp giữa algebra của log-odds và statistical modeling.
