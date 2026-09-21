# Hồi quy và tương quan: association, conditional modeling và prediction

Hồi quy (regression / 회귀) và tương quan (correlation / 상관관계) đều mô tả relationships giữa variables, nhưng chúng trả lời những câu hỏi khác nhau.

Correlation hỏi:

> Hai variables thay đổi cùng nhau mạnh đến mức nào theo một notion association cụ thể?

Regression hỏi:

> Ta muốn model/predict outcome như function của predictors ra sao, và coefficients nên được hiểu như thế nào dưới assumptions của model?

Cả hai đều **không tự động là causal analysis**.

## 1. Covariance: direction của joint variation

Với random variables `X,Y`, covariance:

```math
\operatorname{Cov}(X,Y)
=E[(X-E[X])(Y-E[Y])].
```

Nếu deviations thường cùng sign, covariance positive. Nếu opposite sign, negative.

Nhưng magnitude phụ thuộc units. Nếu đổi KRW thành million KRW, covariance đổi scale.

Do đó cần normalized measure để so association across scales.

## 2. Pearson correlation là normalized covariance

```math
\rho_{XY}
=
\frac{\operatorname{Cov}(X,Y)}{
\sigma_X\sigma_Y
}.
```

Sample version:

```math
r=
\frac{
\sum_i(x_i-\bar x)(y_i-\bar y)
}{
\sqrt{\sum_i(x_i-\bar x)^2}
\sqrt{\sum_i(y_i-\bar y)^2}
}.
```

Giá trị nằm trong `[-1,1]`.

Một geometric interpretation rất hữu ích: sau khi center observations, correlation là cosine giữa hai centered data vectors.

Vì vậy `r=1` khi standardized patterns align perfectly linearly.

## 3. Correlation chỉ đo linear association

`r≈0` không nghĩa “không có relationship”.

Ví dụ nếu

```math
Y=X^2
```

và `X` symmetric quanh zero, linear correlation có thể gần 0 dù `Y` được xác định hoàn toàn bởi `X`.

Do đó trước khi đọc correlation coefficient cần plot data và hiểu shape.

Spearman correlation dùng ranks và đo monotonic association, nhưng cũng không phải universal dependence measure.

## 4. Correlation không invariant trước selection

Nếu sample bị restricted range, correlation có thể shrink.

Nếu combine subgroups có centers khác nhau, correlation aggregate có thể khác hoặc đảo sign so với within-group correlations.

Đây là geometric/statistical version của Simpson's paradox và selection effects.

## 5. Simple linear regression bắt đầu từ conditional mean model

Model:

```math
Y_i=\beta_0+\beta_1X_i+\varepsilon_i.
```

Một interpretation cốt lõi là

```math
E[Y\mid X=x]
=\beta_0+\beta_1x
```

nếu error có conditional mean zero.

Ta không nói mọi point nằm trên line. Line mô tả conditional center; residuals mô tả unexplained variation.

## 6. Least squares đến từ projection

Given data, least squares chọn

```math
\hat\beta_0,\hat\beta_1
```

để minimize

```math
\sum_i(y_i-\hat y_i)^2.
```

Trong matrix form:

```math
\min_\beta\|X\beta-y\|_2^2.
```

Prediction vector `X\hat\beta` là orthogonal projection của `y` lên column space của design matrix `X`.

Đây là connection trực tiếp với linear algebra, không phải một statistics formula riêng.

## 7. Derive simple-regression slope

Với centered variables, model không cần intercept tạm thời:

```math
\tilde y_i\approx\beta_1\tilde x_i.
```

Least-squares objective:

```math
S(\beta_1)
=
\sum_i(\tilde y_i-\beta_1\tilde x_i)^2.
```

Differentiate:

```math
\frac{dS}{d\beta_1}
=-2\sum_i\tilde x_i(\tilde y_i-\beta_1\tilde x_i).
```

Set zero:

```math
\hat\beta_1
=
\frac{\sum_i\tilde x_i\tilde y_i}
{\sum_i\tilde x_i^2}.
```

Tức slope = covariance-like quantity / variance-like quantity.

Population analogue:

```math
\beta_1
=\frac{\operatorname{Cov}(X,Y)}{\operatorname{Var}(X)}
```

under linear projection interpretation.

## 8. Units của coefficient mang meaning

Nếu regress electricity bill `Y` (KRW) trên usage `X` (kWh):

```math
\hat Y=8000+120X,
```

slope 120 có unit

```text
KRW / kWh.
```

Nó nói conditional predicted bill thay khoảng 120 KRW cho mỗi additional kWh trong observed/model range.

Intercept 8000 là prediction tại `X=0`; nếu data chỉ từ 200–500 kWh, interpretation intercept có thể là extrapolation và không meaningful.

## 9. Multiple regression và “holding other variables fixed”

Model:

```math
Y=\beta_0+\beta_1X_1+\cdots+\beta_pX_p+\varepsilon.
```

Coefficient `\beta_j` mô tả difference in model prediction per one-unit `X_j` change while included other predictors held fixed.

Nhưng “hold fixed” trong regression là algebra/model comparison, không automatically equal a physical intervention.

Nếu predictors correlated strongly, such comparisons may correspond to rare/unrealistic states.

## 10. Omitted variable bias: vì sao causal interpretation dễ sai

Suppose true relation:

```math
Y=\beta_1X+\beta_2Z+\varepsilon,
```

nhưng ta regress only `Y` on `X`.

Nếu `Z` ảnh hưởng `Y` và correlated với `X`, estimated slope on `X` absorbs part of `Z` effect.

Đây là omitted-variable bias.

Ví dụ salary và defects có thể correlate vì seniority/project complexity. Regression coefficient không tự động là causal effect của salary.

## 11. Residuals là data về model failure

Residual:

```math
e_i=y_i-\hat y_i.
```

Residual diagnostics hỏi:

- còn nonlinear pattern không?
- variance có tăng theo fitted value không?
- residuals có serial dependence không?
- có influential points không?
- tails có heavier hơn assumed distribution không?

Một high `R^2` không trả lời những questions này.

## 12. Homoskedasticity và heteroskedasticity

Homoskedasticity assumption roughly:

```math
\operatorname{Var}(\varepsilon\mid X)=\sigma^2.
```

Nếu residual spread phụ thuộc `X`, ta có heteroskedasticity.

OLS coefficient estimates có thể vẫn unbiased/consistent dưới some conditions, nhưng conventional standard errors có thể sai. Robust standard errors hoặc model variance structure có thể cần thiết.

## 13. Independence và time series

Trong time series, residuals thường autocorrelated.

Nếu assume iid errors khi data có serial dependence, uncertainty estimates có thể quá optimistic.

Regression cho time-indexed data cần diagnostics/modeling như AR terms, Newey–West style robust errors hoặc full time-series models tùy goal.

## 14. `R^2` là gì và không phải gì?

Standard definition:

```math
R^2
=1-
\frac{\sum_i(y_i-\hat y_i)^2}
{\sum_i(y_i-\bar y)^2}.
```

Nó so residual squared error với baseline predict mean.

High `R^2` không guarantee:

- causal validity;
- good extrapolation;
- correct functional form;
- unbiased predictions for subgroups;
- production generalization.

Adding predictors thường không decrease training `R^2`, nên adjusted metrics/cross-validation cần cho model comparison.

## 15. Prediction intervals khác confidence intervals

Confidence interval cho mean response tại `x` quantify uncertainty về conditional mean.

Prediction interval cho một new observation rộng hơn vì gồm cả model-mean uncertainty và irreducible observation noise.

Hai intervals answer different questions.

## 16. Regularization: đổi objective để trade bias lấy variance

Ridge regression:

```math
\min_\beta
\|X\beta-y\|_2^2
+\lambda\|\beta\|_2^2.
```

Lasso:

```math
\min_\beta
\|X\beta-y\|_2^2
+\lambda\|\beta\|_1.
```

Ridge shrink coefficients và stabilize multicollinearity. Lasso có thể produce sparse coefficients.

Regularization deliberately introduces bias để reduce variance/generalization error.

Đây là statistics version của bias-variance trade-off.

## 17. Multicollinearity và identifiability

Nếu columns predictors gần linearly dependent, many coefficient combinations produce similar predictions.

Then individual coefficients become unstable even if overall predictions okay.

Condition number/SVD từ numerical linear algebra giúp diagnose this geometry.

Statistics và numerical linear algebra gặp nhau trực tiếp ở đây.

## 18. Logistic regression: linear model trên log-odds scale

Với binary outcome, probability must stay in `[0,1]`.

Model:

```math
\log\frac{p}{1-p}
=\beta_0+\beta^Tx.
```

Invert:

```math
p=
\frac{1}{1+e^{-(\beta_0+\beta^Tx)}}.
```

Coefficient `\beta_j` là additive change in log-odds per unit predictor; exponentiating gives odds ratio:

```math
e^{\beta_j}.
```

Điều này nối logarithms/exponentials với statistical modeling.

## 19. Maximum likelihood viewpoint

Under Gaussian error assumptions with constant variance, minimizing squared error tương đương maximizing Gaussian likelihood.

Do đó least squares không chỉ geometric projection; nó cũng là probabilistic estimation under a specific noise model.

Nếu noise model khác, optimal loss có thể khác.

Ví dụ Laplace noise liên hệ L1 loss.

## 20. Nonlinear regression và model flexibility

Regression không đồng nghĩa linear regression.

Ta có thể dùng:

- polynomial basis;
- splines;
- generalized linear models;
- trees;
- neural networks.

Càng flexible, approximation bias có thể giảm nhưng overfitting risk tăng. Cross-validation và regularization trở nên quan trọng.

## 21. Extrapolation là assumption mạnh

Model fit tốt trong observed range không guarantee behavior ngoài range.

Một quadratic fit cho historical growth có thể explode absurdly khi extrapolate xa.

Physics/domain constraints đôi khi quan trọng hơn fit error trong-sample.

## 22. Worked example: confounding

Suppose data cho thấy projects có higher developer salary cũng có more defects.

Simple regression có positive salary coefficient.

Nhưng nếu high-salary senior engineers được assign tới projects phức tạp hơn, project complexity là confounder ảnh hưởng cả salary composition và defects.

Thêm complexity variables có thể change coefficient, nhưng causal validity còn phụ thuộc whether confounders measured correctly và no major unmeasured confounding.

Regression adjustment là tool, không phải automatic causal machine.

## 23. Finance: beta là regression coefficient có assumptions

CAPM-style beta thường estimated từ regression asset excess returns trên market excess returns:

```math
R_i-R_f
=\alpha+\beta(R_m-R_f)+\varepsilon.
```

`\beta` đo linear sensitivity in sample/model.

Nó không phải immutable physical constant; estimate phụ thuộc window, frequency, regime và data quality.

## 24. AI: regression as supervised learning

Supervised learning generalizes regression idea:

```text
features X → target Y
```

Loss function defines what “best fit” means.

Train error measures fit observed data; validation/test estimate generalization. Distribution shift can break both regression assumptions và ML performance.

## 25. Correlation, regression và causality — relationship map

```text
Correlation
    ↓ describes association
Regression
    ↓ models conditional relationship / prediction
Causal inference
    ↓ asks intervention/counterfactual effect
```

Chúng có thể dùng chung algebra/probability, nhưng estimand khác nhau.

## Mental Model

> Correlation measures alignment. Regression constructs a predictive/conditional surface. Causal inference asks what would change under intervention. Least squares is projection geometry; statistical interpretation arrives only after specifying how data/noise were generated.

## Common Misconceptions

**`r=0` means no relationship.** Không; it means no linear association under Pearson measure.

**High `R^2` means model is correct.** Không; wrong causal/functional model có thể vẫn fit sample tốt.

**Regression coefficient is automatically a causal effect.** Không; causal interpretation needs identification assumptions/design.

**More predictors always improve model.** Training fit often improves, but variance, multicollinearity and overfitting can worsen generalization.

**OLS formula `(X^TX)^{-1}X^Ty` is how software should always solve regression.** Numerical implementations often prefer QR/SVD for stability.
