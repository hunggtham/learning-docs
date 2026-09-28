# Regression, Prediction & Inference — OLS là projection trước khi là causal effect

Linear regression là một trong những công cụ quan trọng nhất của econometrics, nhưng coefficient không tự động có nghĩa causal. Trước hết, regression mô tả conditional relationship hoặc best linear prediction giữa variables. Causal interpretation chỉ xuất hiện khi design và assumptions bổ sung đủ mạnh.

## 1. Conditional expectation là điểm bắt đầu

Ta muốn hiểu:

```text
E[Y | X=x]
```

Đây là average outcome của units có `X=x`. Conditional expectation có thể nonlinear, asymmetric hoặc phụ thuộc nhiều covariates.

Linear regression approximates relation bằng một linear function:

```text
Y_i = β0 + β1 X_i + u_i
```

## 2. Population linear projection

Ngay cả khi true conditional expectation không linear, có thể định nghĩa coefficients làm minimize mean squared prediction error:

```text
(β0, β1) = argmin E[(Y − β0 − β1X)^2]
```

OLS trong sample estimate population linear projection này.

Điểm này giúp tránh hiểu sai rằng linear regression luôn giả định reality “thật sự tuyến tính”.

## 3. OLS criterion

Trong sample:

```text
min Σ (Y_i − β0 − β1X_i)^2
```

OLS chọn line có sum of squared residuals nhỏ nhất.

Với simple regression:

```text
β̂1 = Cov(X,Y) / Var(X)
```

Nên slope chỉ tồn tại khi X có variation.

## 4. Residual và error term khác nhau

Error `u_i` trong population model là unobserved component relative to model.

Residual:

```text
e_i = Y_i − Ŷ_i
```

là sample estimate sau khi fit.

Residual có algebraic properties của OLS sample; error term là conceptual part của DGP.

## 5. Interpretation của slope

Trong simple linear model, `β1` đo change trong predicted/conditional Y khi X tăng một unit.

Nếu Y là log wage và X là years education:

```text
Δ log(Y) ≈ percentage change in Y
```

Coefficient interpretation phụ thuộc transformation và units.

## 6. Multiple regression

```text
Y = β0 + β1X1 + β2X2 + ... + u
```

`β1` là partial association giữa Y và X1 holding included X2... fixed theo linear projection.

“Hold fixed” không có nghĩa experimental intervention nếu controls không tạo conditional exogeneity.

## 7. Frisch–Waugh–Lovell intuition

Coefficient của X1 trong multiple regression có thể hiểu bằng ba bước:

1. residualize X1 on other controls;
2. residualize Y on same controls;
3. regress residual Y on residual X1.

Nó dùng phần variation của X1 không explained linearly bởi controls.

Đây là mental model tốt cho “what variation identifies coefficient?”.

## 8. Omitted-variable bias

Nếu true outcome depends on X và Z nhưng Z bị omit, X coefficient absorbs relation qua Z khi X và Z correlate.

Sign intuition trong simple case:

```text
Bias sign ≈ sign(effect of Z on Y) × sign(Corr(X,Z))
```

Nhưng nhiều confounders/nonlinearities có thể làm sign không dễ đoán.

## 9. Conditional mean independence

Một strong assumption cho causal interpretation:

```text
E[u | X, controls] = 0
```

hoặc potential-outcome language:

```text
Y(d) ⟂ D | X
```

Nếu treatment assignment independent of potential outcomes conditional on controls, regression/matching can identify conditional causal effects under overlap.

Assumption không test trực tiếp từ observed data alone.

## 10. Overlap / common support

Cần có comparable treated và untreated observations trong covariate regions.

Nếu mọi high-income unit treated và mọi low-income unit untreated, model extrapolates treatment effect across regions without counterfactual support.

Regression không tạo overlap bằng algebra.

## 11. Functional form

Suppose true relation curved but model linear. Prediction and coefficient interpretation depend on observed X distribution.

Solutions có thể gồm polynomial, splines, transformations hoặc nonparametric methods, nhưng complexity phải phục vụ question chứ không chỉ improve fit.

## 12. Interaction terms

Nếu treatment effect varies by Z:

```text
Y = β0 + β1D + β2Z + β3(D×Z) + u
```

Effect of D:

```text
β1 + β3Z
```

Không interpret β1 là “overall treatment effect” nếu interaction có mặt; nó là effect tại `Z=0`, trừ khi recentered.

## 13. Dummy variables

Binary X coefficient so sánh predicted mean giữa group 1 và reference group 0, conditional on controls.

Với category nhiều levels, phải chọn omitted reference category để tránh perfect multicollinearity với intercept.

## 14. Multicollinearity

High correlation giữa regressors làm estimates imprecise vì khó tách independent variation.

Multicollinearity không nhất thiết bias OLS; nó tăng variance và làm coefficients sensitive.

Perfect multicollinearity khiến coefficient không identified.

## 15. R-squared

```text
R² = 1 − SSR/TSS
```

R² đo fraction sample variation explained by fitted model.

High R² không chứng minh causal validity. Low R² không làm treatment estimate vô dụng nếu assignment credible.

Prediction quality và causal identification là objectives khác nhau.

## 16. Prediction error decomposition

Out-of-sample prediction cần bias–variance trade-off. Model quá flexible fit noise; model quá rigid miss structure.

Train/test split hoặc cross-validation đánh giá predictive generalization, nhưng không giải confounding.

Machine learning có thể improve nuisance prediction trong causal workflows, nhưng design vẫn quyết định estimand.

## 17. Sampling distribution

Estimate thay đổi qua hypothetical repeated samples. Standard error approximates dispersion của estimator.

Confidence interval thường có form:

```text
estimate ± critical value × SE
```

Interpretation frequentist không phải “95% probability true β nằm trong interval này” sau khi interval đã fixed; procedure có 95% coverage under assumptions.

## 18. Hypothesis testing

Typical null:

```text
H0: β = 0
```

p-value là probability, dưới null và model assumptions, quan sát statistic ít nhất extreme như data hiện tại.

Nó không phải probability null đúng.

## 19. Type I, Type II và power

Type I error: reject true null.

Type II error: fail to reject false null.

Power tăng với effect size, sample size và lower noise.

“No significant effect” không đồng nghĩa “effect bằng zero”, đặc biệt khi study underpowered.

## 20. Heteroskedasticity

Homoskedasticity assumes constant conditional error variance. Economic data thường heteroskedastic: income dispersion tăng theo education/age, firm-size variance khác nhau.

OLS coefficients vẫn có thể unbiased/consistent under exogeneity, nhưng classical SE sai. Heteroskedasticity-robust SE thường là baseline cho cross-sectional work.

## 21. Clustered standard errors

Nếu observations trong cluster share shocks, errors correlated within group.

Examples:

- students within school;
- workers within firm;
- counties within state;
- repeated observations within person.

SE nên account assignment/shock dependence. Large number of observations không bù được ít independent clusters.

## 22. Serial correlation

Time-series/panel errors có thể correlated across time. Naive SE underestimate uncertainty.

Need HAC/Newey-West, cluster-by-unit/time hoặc model-specific correction depending design.

## 23. Weighted regression

Weights có nhiều meaning: sampling weights, frequency weights, precision weights.

Dùng weights phải giải thích estimand thay đổi thế nào. Survey weights giúp population representativeness; inverse-variance weights target precision under assumptions.

## 24. Standardization

Standardized coefficient đo change in SD units, useful comparison but hides real economic units.

Policy interpretation nên quay lại natural units: dollars, percentage points, hours, test-score SD với context.

## 25. Log-level, level-log và log-log

Common interpretations:

```text
log(Y) on X: 1-unit X ≈ 100β% change Y
Y on log(X): 1% X ≈ β/100 unit Y
log(Y) on log(X): β ≈ elasticity
```

Approximations cần adjustment cho large coefficients.

## 26. Extrapolation

Regression line ngoài support của X có thể vô nghĩa. A wage–experience relation estimated age 20–60 không nên extrapolate đến age 120.

Plot data/support trước khi dùng fitted equation.

## 27. Regression to the mean

Units selected vì extreme outcome thường move closer to average next period even without treatment.

Before-after analysis trên low-performing schools/patients dễ nhầm regression to mean với policy effect.

Need comparison group/design.

## 28. Multiple testing

Nếu test hàng trăm outcomes/specifications, some p-values nhỏ xuất hiện by chance.

Pre-specification, family-wise/FDR adjustments và transparent reporting giảm false discovery.

## 29. Specification searching

Researcher degrees of freedom gồm control set, sample, outcome transform, time window, subgroup.

Nếu specification được chọn sau khi nhìn desired sign/significance, nominal p-values mất meaning.

Robustness should show result across substantively defensible specifications, not cherry-pick.

## 30. Prediction vs explanation vs causality

Regression có ba uses khác nhau:

```text
Description: summarize association
Prediction: forecast Y
Causality: estimate intervention effect
```

Một model có thể excellent prediction nhưng poor causal interpretation; một randomized treatment regression có low R² nhưng highly credible causal effect.

## 31. Failure modes

Sai lầm thứ nhất là đọc every coefficient như causal effect.

Sai lầm thứ hai là dùng high R² làm evidence model đúng.

Sai lầm thứ ba là thêm controls không có causal reasoning.

Sai lầm thứ tư là dùng conventional SE khi heteroskedastic/clustered dependence rõ.

Sai lầm thứ năm là equate non-significance với no effect.

Sai lầm thứ sáu là extrapolate beyond support.

## 32. Mental model

Khi đọc regression, hãy hỏi:

1. Regression đang dùng để description, prediction hay causality?
2. Coefficient dùng variation nào sau khi partialling controls?
3. Units/transformation cho interpretation gì?
4. Có overlap không?
5. Functional form hợp lý trong support không?
6. Omitted confounder nào có thể drive coefficient?
7. Error dependence yêu cầu robust/cluster/HAC SE gì?
8. Sample size thực sự độc lập là observations hay clusters?
9. Economic magnitude có meaningful không?
10. Specification có pre-specified và robust không?

Regression cung cấp language và estimator. Để biến association thành causal estimate, cần source of assignment/variation đáng tin. Randomized experiments là benchmark rõ nhất cho logic đó.
