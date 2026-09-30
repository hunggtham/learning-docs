# Regression, Prediction & Suy luận (inference / 추론) — OLS là projection trước khi là nhân quả (causal / 인과적) tác động (effect / 효과)

Tuyến tính (linear / 선형) regression là một trong những công cụ quan trọng nhất của econometrics, nhưng coefficient không tự động có nghĩa nhân quả (causal / 인과적). Trước hết, regression mô tả conditional relationship hoặc best tuyến tính (linear / 선형) prediction giữa variables. Nhân quả (causal / 인과적) interpretation chỉ xuất hiện khi thiết kế (design / 설계) và các giả định (assumptions / 가정들) bổ sung đủ mạnh.

## 1. Conditional expectation là điểm bắt đầu

Ta muốn hiểu:

```text
E[Y | X=x]
```

Đây là average kết quả (outcome / 결과) của units có `X=x`. Conditional expectation có thể nonlinear, asymmetric hoặc phụ thuộc nhiều covariates.

Tuyến tính (linear / 선형) regression approximates quan hệ (relation / 관계) bằng một tuyến tính (linear / 선형) hàm (function / 함수):

```text
Y_i = β0 + β1 X_i + u_i
```

## 2. Population tuyến tính (linear / 선형) projection

Ngay cả khi true conditional expectation không tuyến tính (linear / 선형), có thể định nghĩa coefficients làm minimize mean squared prediction lỗi (error / 오류):

```text
(β0, β1) = argmin E[(Y − β0 − β1X)^2]
```

OLS trong mẫu (sample / 표본) estimate population tuyến tính (linear / 선형) projection này.

Điểm này giúp tránh hiểu sai rằng tuyến tính (linear / 선형) regression luôn giả định reality “thật sự tuyến tính”.

## 3. OLS criterion

Trong mẫu (sample / 표본):

```text
min Σ (Y_i − β0 − β1X_i)^2
```

OLS chọn line có sum of squared residuals nhỏ nhất.

Với simple regression:

```text
β̂1 = Cov(X,Y) / Var(X)
```

Nên slope chỉ tồn tại khi X có variation.

## 4. Residual và lỗi (error / 오류) term khác nhau

Lỗi (error / 오류) `u_i` trong mô hình quần thể (population model / 개체군 모델) là unobserved thành phần (component / 컴포넌트) relative to mô hình (model / 모델).

Residual:

```text
e_i = Y_i − Ŷ_i
```

là mẫu (sample / 표본) estimate sau khi fit.

Residual có algebraic properties của OLS mẫu (sample / 표본); lỗi (error / 오류) term là conceptual part của DGP.

## 5. Interpretation của slope

Trong simple mô hình tuyến tính (linear model / 선형 모델), `β1` đo thay đổi (change / 변경) trong predicted/conditional Y khi X tăng một đơn vị (unit / 단위).

Nếu Y là log wage và X là years education:

```text
Δ log(Y) ≈ percentage change in Y
```

Coefficient interpretation phụ thuộc transformation và units.

## 6. Multiple regression
Phần “6. Multiple regression” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```text
Y = β0 + β1X1 + β2X2 + ... + u
```

`β1` là partial association giữa Y và X1 holding included X2... fixed theo tuyến tính (linear / 선형) projection.

“Hold fixed” không có nghĩa experimental intervention nếu controls không tạo conditional exogeneity.

## 7. Frisch–Waugh–Lovell intuition

Coefficient của X1 trong multiple regression có thể hiểu bằng ba bước:

1. residualize X1 on other controls;
2. residualize Y on same controls;
3. regress residual Y on residual X1.

Nó dùng phần variation của X1 không explained linearly bởi controls.

Đây là mô hình tư duy (mental model / 사고 모델) tốt cho “what variation identifies coefficient?”.

## 8. Omitted-variable độ lệch (bias / 편향)

Nếu true kết quả (outcome / 결과) depends on X và Z nhưng Z bị omit, X coefficient absorbs quan hệ (relation / 관계) qua Z khi X và Z correlate.

Sign intuition trong simple trường hợp (case / 사례):

```text
Bias sign ≈ sign(effect of Z on Y) × sign(Corr(X,Z))
```

Nhưng nhiều confounders/nonlinearities có thể làm sign không dễ đoán.

## 9. Conditional mean independence

Một strong giả định (assumption / 가정) cho nhân quả (causal / 인과적) interpretation:

```text
E[u | X, controls] = 0
```

hoặc potential-outcome ngôn ngữ (language / 언어):

```text
Y(d) ⟂ D | X
```

Nếu treatment assignment independent of potential outcomes conditional on controls, regression/matching can identify conditional nhân quả (causal / 인과적) effects under overlap.

Giả định (assumption / 가정) không kiểm thử (test / 테스트) trực tiếp từ observed dữ liệu (data / 데이터) alone.

## 10. Overlap / dùng chung (common / 공통) hỗ trợ (support / 지원)

Cần có comparable treated và untreated observations trong covariate regions.

Nếu mọi high-income đơn vị (unit / 단위) treated và mọi low-income đơn vị (unit / 단위) untreated, mô hình (model / 모델) extrapolates treatment tác động (effect / 효과) across regions without counterfactual hỗ trợ (support / 지원).

Regression không tạo overlap bằng algebra.

## 11. Functional form

Suppose true quan hệ (relation / 관계) curved but mô hình (model / 모델) tuyến tính (linear / 선형). Prediction and coefficient interpretation depend on observed X phân phối (distribution / 분포).

Solutions có thể gồm polynomial, splines, transformations hoặc nonparametric methods, nhưng độ phức tạp (complexity / 복잡도) phải phục vụ question chứ không chỉ improve fit.

## 12. Tương tác (interaction / 상호작용) terms

Nếu treatment tác động (effect / 효과) varies by Z:

```text
Y = β0 + β1D + β2Z + β3(D×Z) + u
```

Tác động (effect / 효과) of D:

```text
β1 + β3Z
```

Không interpret β1 là “overall treatment tác động (effect / 효과)” nếu tương tác (interaction / 상호작용) có mặt; nó là tác động (effect / 효과) tại `Z=0`, trừ khi recentered.

## 13. Dummy variables

Nhị phân (binary / 이진) X coefficient so sánh predicted mean giữa group 1 và tham chiếu (reference / 참조) group 0, conditional on controls.

Với category nhiều levels, phải chọn omitted tham chiếu (reference / 참조) category để tránh perfect multicollinearity với intercept.

## 14. Multicollinearity

High correlation giữa regressors làm estimates imprecise vì khó tách independent variation.

Multicollinearity không nhất thiết độ lệch (bias / 편향) OLS; nó tăng variance và làm coefficients sensitive.

Perfect multicollinearity khiến coefficient không identified.

## 15. R-squared
Phần “15. R-squared” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```text
R² = 1 − SSR/TSS
```

R² đo fraction mẫu (sample / 표본) variation explained by fitted mô hình (model / 모델).

High R² không chứng minh nhân quả (causal / 인과적) validity. Low R² không làm treatment estimate vô dụng nếu assignment credible.

Prediction chất lượng (quality / 품질) và nhân quả (causal / 인과적) identification là objectives khác nhau.

## 16. Prediction lỗi (error / 오류) decomposition

Out-of-sample prediction cần độ lệch (bias / 편향)–variance sự đánh đổi (trade-off / 트레이드오프). Mô hình (model / 모델) quá flexible fit noise; mô hình (model / 모델) quá rigid miss cấu trúc (structure / 구조).

Train/kiểm thử (test / 테스트) split hoặc cross-validation đánh giá predictive generalization, nhưng không giải confounding.

Machine học tập (learning / 학습) có thể improve nuisance prediction trong nhân quả (causal / 인과적) workflows, nhưng thiết kế (design / 설계) vẫn quyết định estimand.

## 17. Sampling phân phối (distribution / 분포)

Estimate thay đổi qua hypothetical repeated samples. Tiêu chuẩn (standard / 표준) lỗi (error / 오류) approximates dispersion của estimator.

Confidence interval thường có form:

```text
estimate ± critical value × SE
```

Interpretation frequentist không phải “95% xác suất (probability / 확률) true β nằm trong interval này” sau khi interval đã fixed; procedure có 95% coverage under các giả định (assumptions / 가정들).

## 18. Hypothesis testing

Typical null:

```text
H0: β = 0
```

p-value là xác suất (probability / 확률), dưới null và mô hình (model / 모델) các giả định (assumptions / 가정들), quan sát statistic ít nhất extreme như dữ liệu (data / 데이터) hiện tại.

Nó không phải xác suất (probability / 확률) null đúng.

## 19. Kiểu (type / 타입) I, Kiểu (type / 타입) II và power

Kiểu (type / 타입) I lỗi (error / 오류): reject true null.

Kiểu (type / 타입) II lỗi (error / 오류): thất bại (fail / 실패) to reject false null.

Power tăng với tác động (effect / 효과) kích thước (size / 크기), cỡ mẫu (sample size / 표본 크기) và lower noise.

“No significant tác động (effect / 효과)” không đồng nghĩa “tác động (effect / 효과) bằng zero”, đặc biệt khi study underpowered.

## 20. Heteroskedasticity

Homoskedasticity assumes constant conditional lỗi (error / 오류) variance. Economic dữ liệu (data / 데이터) thường heteroskedastic: income dispersion tăng theo education/age, firm-size variance khác nhau.

OLS coefficients vẫn có thể unbiased/consistent under exogeneity, nhưng classical SE sai. Heteroskedasticity-robust SE thường là baseline cho cross-sectional công việc (work / 작업).

## 21. Clustered tiêu chuẩn (standard / 표준) errors

Nếu observations trong cluster share shocks, errors correlated within group.

Examples:

- students within school;
- workers within firm;
- counties within trạng thái (state / 상태);
- repeated observations within person.

SE nên account assignment/shock dependence. Large number of observations không bù được ít independent clusters.

## 22. Serial correlation

Time-series/panel errors có thể correlated across thời gian (time / 시간). Naive SE underestimate bất định (uncertainty / 불확실성).

Need HAC/Newey-West, cluster-by-unit/thời gian (time / 시간) hoặc model-specific correction depending thiết kế (design / 설계).

## 23. Weighted regression

Weights có nhiều meaning: sampling weights, frequency weights, precision weights.

Dùng weights phải giải thích estimand thay đổi thế nào. Survey weights giúp population representativeness; inverse-variance weights mục tiêu (target / 대상) precision under các giả định (assumptions / 가정들).

## 24. Standardization

Standardized coefficient đo thay đổi (change / 변경) in SD units, useful comparison but hides real economic units.

Chính sách (policy / 정책) interpretation nên quay lại natural units: dollars, percentage points, hours, test-score SD với ngữ cảnh (context / 맥락).

## 25. Log-level, level-log và log-log

Dùng chung (common / 공통) interpretations:

```text
log(Y) on X: 1-unit X ≈ 100β% change Y
Y on log(X): 1% X ≈ β/100 unit Y
log(Y) on log(X): β ≈ elasticity
```

Approximations cần adjustment cho large coefficients.

## 26. Extrapolation

Regression line ngoài hỗ trợ (support / 지원) của X có thể vô nghĩa. A wage–experience quan hệ (relation / 관계) estimated age 20–60 không nên extrapolate đến age 120.

Plot dữ liệu (data / 데이터)/hỗ trợ (support / 지원) trước khi dùng fitted equation.

## 27. Regression to the mean

Units selected vì extreme kết quả (outcome / 결과) thường move closer to average next period even without treatment.

Before-after phân tích (analysis / 분석) trên low-performing schools/patients dễ nhầm regression to mean với chính sách (policy / 정책) tác động (effect / 효과).

Need comparison group/thiết kế (design / 설계).

## 28. Multiple testing

Nếu kiểm thử (test / 테스트) hàng trăm outcomes/specifications, some p-values nhỏ xuất hiện by chance.

Pre-specification, family-wise/FDR adjustments và transparent reporting giảm false discovery.

## 29. Specification searching

Researcher degrees of freedom gồm điều khiển (control / 제어) set, mẫu (sample / 표본), kết quả (outcome / 결과) transform, thời gian (time / 시간) cửa sổ (window / 윈도우), subgroup.

Nếu specification được chọn sau khi nhìn desired sign/significance, nominal p-values mất meaning.

Robustness should show kết quả (result / 결과) across substantively defensible specifications, not cherry-pick.

## 30. Prediction vs explanation vs causality

Regression có ba uses khác nhau:

```text
Description: summarize association
Prediction: forecast Y
Causality: estimate intervention effect
```

Một mô hình (model / 모델) có thể excellent prediction nhưng poor nhân quả (causal / 인과적) interpretation; một randomized treatment regression có low R² nhưng highly credible nhân quả (causal / 인과적) tác động (effect / 효과).

## 31. Thất bại (failure / 실패) modes

Sai lầm thứ nhất là đọc every coefficient như nhân quả (causal / 인과적) tác động (effect / 효과).

Sai lầm thứ hai là dùng high R² làm bằng chứng (evidence / 증거) mô hình (model / 모델) đúng.

Sai lầm thứ ba là thêm controls không có lập luận nhân quả (causal reasoning / 인과적 추론).

Sai lầm thứ tư là dùng conventional SE khi heteroskedastic/clustered dependence rõ.

Sai lầm thứ năm là equate non-significance với no tác động (effect / 효과).

Sai lầm thứ sáu là extrapolate beyond hỗ trợ (support / 지원).

## 32. Mô hình tư duy (mental model / 사고 모델)

Khi đọc regression, hãy hỏi:

1. Regression đang dùng để description, prediction hay causality?
2. Coefficient dùng variation nào sau khi partialling controls?
3. Units/transformation cho interpretation gì?
4. Có overlap không?
5. Functional form hợp lý trong hỗ trợ (support / 지원) không?
6. Omitted confounder nào có thể drive coefficient?
7. Lỗi (error / 오류) dependence yêu cầu robust/cluster/HAC SE gì?
8. Cỡ mẫu (sample size / 표본 크기) thực sự độc lập là observations hay clusters?
9. Economic magnitude có meaningful không?
10. Specification có pre-specified và robust không?

Regression cung cấp ngôn ngữ (language / 언어) và estimator. Để biến association thành nhân quả (causal / 인과적) estimate, cần nguồn (source / 소스) of assignment/variation đáng tin. Randomized experiments là benchmark rõ nhất cho lô-gic (logic / 논리) đó.
