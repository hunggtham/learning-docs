# Regression, Prediction & Suy luận (inference / 추론) — OLS là projection trước khi là nhân quả (causal / 인과적) tác động (effect / 효과)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Regression, Prediction & Suy luận (inference / 추론) — OLS là projection trước khi là nhân quả (causal / 인과적) tác động (effect / 효과)**. Route đi từ conditional expectation/projection → OLS và assumptions → prediction, uncertainty và specification → inference, để không nhầm fit dự báo với tác động nhân quả.

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

> **Chuyển mạch:** Conditional expectation là target tối ưu dưới squared loss; **linear projection** xấp xỉ target trong span của regressors, còn **OLS** tìm coefficient bằng cách tối thiểu hóa sai số bình phương trong mẫu.

## 2. Population tuyến tính (linear / 선형) projection

Ngay cả khi true conditional expectation không tuyến tính (linear / 선형), có thể định nghĩa coefficients làm minimize mean squared prediction lỗi (error / 오류):

```text
(β0, β1) = argmin E[(Y − β0 − β1X)^2]
```

OLS trong mẫu (sample / 표본) estimate population tuyến tính (linear / 선형) projection này.

Điểm này giúp tránh hiểu sai rằng tuyến tính (linear / 선형) regression luôn giả định reality “thật sự tuyến tính”.

> **Chuyển mạch:** Population projection định nghĩa coefficient tốt nhất theo tiêu chuẩn dự báo, dù conditional expectation thật có thể nonlinear. **OLS criterion** đưa tiêu chuẩn đó vào dữ liệu mẫu; sau đó cần tách residual quan sát được khỏi error term của quá trình sinh dữ liệu.

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

> **Chuyển mạch:** OLS chọn đường có tổng squared residual nhỏ nhất, còn error term là phần không quan sát trong population DGP. **Interpretation của slope** tiếp theo chỉ có ý nghĩa khi ghi rõ units, transformation và đây là association/prediction hay causal effect.

## 4. Residual và lỗi (error / 오류) term khác nhau

Lỗi (error / 오류) `u_i` trong mô hình quần thể (population model / 개체군 모델) là unobserved thành phần (component / 컴포넌트) relative to mô hình (model / 모델).

Residual:

```text
e_i = Y_i − Ŷ_i
```

là mẫu (sample / 표본) estimate sau khi fit.

Residual có algebraic properties của OLS mẫu (sample / 표본); lỗi (error / 오류) term là conceptual part của DGP.

> **Chuyển mạch:** Residual là estimate sau fit, không phải toàn bộ sai số của DGP; slope mô tả thay đổi dự báo khi X tăng một đơn vị dưới quy ước giữ các biến liên quan. **Multiple regression** mở rộng diễn giải đó bằng partial association, nhưng “hold fixed” vẫn không tự tạo intervention.

## 5. Interpretation của slope

Trong simple mô hình tuyến tính (linear model / 선형 모델), `β1` đo thay đổi (change / 변경) trong predicted/conditional Y khi X tăng một đơn vị (unit / 단위).

Nếu Y là log wage và X là years education:

```text
Δ log(Y) ≈ percentage change in Y
```

Coefficient interpretation phụ thuộc transformation và units.

> **Chuyển mạch:** Ở chặng này của **Regression, Prediction & Suy luận (inference / 추론) — OLS là projection trước khi là nhân quả (causal / 인과적) tác động (effect / 효과)**, **6. Multiple regression** tiếp nhận điểm tựa từ **5. Interpretation của slope** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Frisch–Waugh–Lovell intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Multiple regression

```text
Y = β0 + β1X1 + β2X2 + ... + u
```

`β1` là partial association giữa Y và X1 holding included X2... fixed theo tuyến tính (linear / 선형) projection.

“Hold fixed” không có nghĩa experimental intervention nếu controls không tạo conditional exogeneity.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Regression, Prediction & Suy luận (inference / 추론) — OLS là projection trước khi là nhân quả (causal / 인과적) tác động (effect / 효과)**, **7. Frisch–Waugh–Lovell intuition** tiếp nhận điểm tựa từ **6. Multiple regression** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Omitted-variable độ lệch (bias / 편향)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Frisch–Waugh–Lovell intuition

Coefficient của X1 trong multiple regression có thể hiểu bằng ba bước:

1. residualize X1 on other controls;
2. residualize Y on same controls;
3. regress residual Y on residual X1.

Nó dùng phần variation của X1 không explained linearly bởi controls.

Đây là mô hình tư duy (mental model / 사고 모델) tốt cho “what variation identifies coefficient?”.

> **Chuyển mạch:** Trong **Regression, Prediction & Suy luận (inference / 추론) — OLS là projection trước khi là nhân quả (causal / 인과적) tác động (effect / 효과)**, **8. Omitted-variable độ lệch (bias / 편향)** tiếp nhận điểm tựa từ **7. Frisch–Waugh–Lovell intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Conditional mean independence** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Omitted-variable độ lệch (bias / 편향)

Nếu true kết quả (outcome / 결과) depends on X và Z nhưng Z bị omit, X coefficient absorbs quan hệ (relation / 관계) qua Z khi X và Z correlate.

Sign intuition trong simple trường hợp (case / 사례):

```text
Bias sign ≈ sign(effect of Z on Y) × sign(Corr(X,Z))
```

Nhưng nhiều confounders/nonlinearities có thể làm sign không dễ đoán.

> **Chuyển mạch:** Ở chặng này của **Regression, Prediction & Suy luận (inference / 추론) — OLS là projection trước khi là nhân quả (causal / 인과적) tác động (effect / 효과)**, **9. Conditional mean independence** tiếp nhận điểm tựa từ **8. Omitted-variable độ lệch (bias / 편향)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Overlap / dùng chung (common / 공통) hỗ trợ (support / 지원)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Regression, Prediction & Suy luận (inference / 추론) — OLS là projection trước khi là nhân quả (causal / 인과적) tác động (effect / 효과)**, **10. Overlap / dùng chung (common / 공통) hỗ trợ (support / 지원)** tiếp nhận điểm tựa từ **9. Conditional mean independence** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Functional form** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Overlap / dùng chung (common / 공통) hỗ trợ (support / 지원)

Cần có comparable treated và untreated observations trong covariate regions.

Nếu mọi high-income đơn vị (unit / 단위) treated và mọi low-income đơn vị (unit / 단위) untreated, mô hình (model / 모델) extrapolates treatment tác động (effect / 효과) across regions without counterfactual hỗ trợ (support / 지원).

Regression không tạo overlap bằng algebra.

> **Chuyển mạch:** Trong **Regression, Prediction & Suy luận (inference / 추론) — OLS là projection trước khi là nhân quả (causal / 인과적) tác động (effect / 효과)**, **11. Functional form** tiếp nhận điểm tựa từ **10. Overlap / dùng chung (common / 공통) hỗ trợ (support / 지원)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Tương tác (interaction / 상호작용) terms** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Functional form

Suppose true quan hệ (relation / 관계) curved but mô hình (model / 모델) tuyến tính (linear / 선형). Prediction and coefficient interpretation depend on observed X phân phối (distribution / 분포).

Solutions có thể gồm polynomial, splines, transformations hoặc nonparametric methods, nhưng độ phức tạp (complexity / 복잡도) phải phục vụ question chứ không chỉ improve fit.

> **Chuyển mạch:** Ở chặng này của **Regression, Prediction & Suy luận (inference / 추론) — OLS là projection trước khi là nhân quả (causal / 인과적) tác động (effect / 효과)**, **12. Tương tác (interaction / 상호작용) terms** tiếp nhận điểm tựa từ **11. Functional form** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Dummy variables** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Regression, Prediction & Suy luận (inference / 추론) — OLS là projection trước khi là nhân quả (causal / 인과적) tác động (effect / 효과)**, **13. Dummy variables** tiếp nhận điểm tựa từ **12. Tương tác (interaction / 상호작용) terms** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Multicollinearity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Dummy variables

Nhị phân (binary / 이진) X coefficient so sánh predicted mean giữa group 1 và tham chiếu (reference / 참조) group 0, conditional on controls.

Với category nhiều levels, phải chọn omitted tham chiếu (reference / 참조) category để tránh perfect multicollinearity với intercept.

> **Chuyển mạch:** Trong **Regression, Prediction & Suy luận (inference / 추론) — OLS là projection trước khi là nhân quả (causal / 인과적) tác động (effect / 효과)**, **14. Multicollinearity** tiếp nhận điểm tựa từ **13. Dummy variables** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. R-squared** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Multicollinearity

High correlation giữa regressors làm estimates imprecise vì khó tách independent variation.

Multicollinearity không nhất thiết độ lệch (bias / 편향) OLS; nó tăng variance và làm coefficients sensitive.

Perfect multicollinearity khiến coefficient không identified.

> **Chuyển mạch:** Ở chặng này của **Regression, Prediction & Suy luận (inference / 추론) — OLS là projection trước khi là nhân quả (causal / 인과적) tác động (effect / 효과)**, **15. R-squared** tiếp nhận điểm tựa từ **14. Multicollinearity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Prediction lỗi (error / 오류) decomposition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. R-squared

```text
R² = 1 − SSR/TSS
```

R² đo fraction mẫu (sample / 표본) variation explained by fitted mô hình (model / 모델).

High R² không chứng minh nhân quả (causal / 인과적) validity. Low R² không làm treatment estimate vô dụng nếu assignment credible.

Prediction chất lượng (quality / 품질) và nhân quả (causal / 인과적) identification là objectives khác nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Regression, Prediction & Suy luận (inference / 추론) — OLS là projection trước khi là nhân quả (causal / 인과적) tác động (effect / 효과)**, **16. Prediction lỗi (error / 오류) decomposition** tiếp nhận điểm tựa từ **15. R-squared** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Sampling phân phối (distribution / 분포)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Prediction lỗi (error / 오류) decomposition

Out-of-sample prediction cần độ lệch (bias / 편향)–variance sự đánh đổi (trade-off / 트레이드오프). Mô hình (model / 모델) quá flexible fit noise; mô hình (model / 모델) quá rigid miss cấu trúc (structure / 구조).

Train/kiểm thử (test / 테스트) split hoặc cross-validation đánh giá predictive generalization, nhưng không giải confounding.

Machine học tập (learning / 학습) có thể improve nuisance prediction trong nhân quả (causal / 인과적) workflows, nhưng thiết kế (design / 설계) vẫn quyết định estimand.

> **Chuyển mạch:** Trong **Regression, Prediction & Suy luận (inference / 추론) — OLS là projection trước khi là nhân quả (causal / 인과적) tác động (effect / 효과)**, **17. Sampling phân phối (distribution / 분포)** tiếp nhận điểm tựa từ **16. Prediction lỗi (error / 오류) decomposition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Hypothesis testing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Sampling phân phối (distribution / 분포)

Estimate thay đổi qua hypothetical repeated samples. Tiêu chuẩn (standard / 표준) lỗi (error / 오류) approximates dispersion của estimator.

Confidence interval thường có form:

```text
estimate ± critical value × SE
```

Interpretation frequentist không phải “95% xác suất (probability / 확률) true β nằm trong interval này” sau khi interval đã fixed; procedure có 95% coverage under các giả định (assumptions / 가정들).

> **Chuyển mạch:** Ở chặng này của **Regression, Prediction & Suy luận (inference / 추론) — OLS là projection trước khi là nhân quả (causal / 인과적) tác động (effect / 효과)**, **18. Hypothesis testing** tiếp nhận điểm tựa từ **17. Sampling phân phối (distribution / 분포)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Kiểu (type / 타입) I, Kiểu (type / 타입) II và power** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Hypothesis testing

Typical null:

```text
H0: β = 0
```

p-value là xác suất (probability / 확률), dưới null và mô hình (model / 모델) các giả định (assumptions / 가정들), quan sát statistic ít nhất extreme như dữ liệu (data / 데이터) hiện tại.

Nó không phải xác suất (probability / 확률) null đúng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Regression, Prediction & Suy luận (inference / 추론) — OLS là projection trước khi là nhân quả (causal / 인과적) tác động (effect / 효과)**, **19. Kiểu (type / 타입) I, Kiểu (type / 타입) II và power** tiếp nhận điểm tựa từ **18. Hypothesis testing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Heteroskedasticity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Kiểu (type / 타입) I, Kiểu (type / 타입) II và power

Kiểu (type / 타입) I lỗi (error / 오류): reject true null.

Kiểu (type / 타입) II lỗi (error / 오류): thất bại (fail / 실패) to reject false null.

Power tăng với tác động (effect / 효과) kích thước (size / 크기), cỡ mẫu (sample size / 표본 크기) và lower noise.

“No significant tác động (effect / 효과)” không đồng nghĩa “tác động (effect / 효과) bằng zero”, đặc biệt khi study underpowered.

> **Chuyển mạch:** Trong **Regression, Prediction & Suy luận (inference / 추론) — OLS là projection trước khi là nhân quả (causal / 인과적) tác động (effect / 효과)**, **20. Heteroskedasticity** tiếp nhận điểm tựa từ **19. Kiểu (type / 타입) I, Kiểu (type / 타입) II và power** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Clustered tiêu chuẩn (standard / 표준) errors** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Heteroskedasticity

Homoskedasticity assumes constant conditional lỗi (error / 오류) variance. Economic dữ liệu (data / 데이터) thường heteroskedastic: income dispersion tăng theo education/age, firm-size variance khác nhau.

OLS coefficients vẫn có thể unbiased/consistent under exogeneity, nhưng classical SE sai. Heteroskedasticity-robust SE thường là baseline cho cross-sectional công việc (work / 작업).

> **Chuyển mạch:** Ở chặng này của **Regression, Prediction & Suy luận (inference / 추론) — OLS là projection trước khi là nhân quả (causal / 인과적) tác động (effect / 효과)**, **21. Clustered tiêu chuẩn (standard / 표준) errors** tiếp nhận điểm tựa từ **20. Heteroskedasticity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Serial correlation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Clustered tiêu chuẩn (standard / 표준) errors

Nếu observations trong cluster share shocks, errors correlated within group.

Examples:

- students within school;
- workers within firm;
- counties within trạng thái (state / 상태);
- repeated observations within person.

SE nên account assignment/shock dependence. Large number of observations không bù được ít independent clusters.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Regression, Prediction & Suy luận (inference / 추론) — OLS là projection trước khi là nhân quả (causal / 인과적) tác động (effect / 효과)**, **22. Serial correlation** tiếp nhận điểm tựa từ **21. Clustered tiêu chuẩn (standard / 표준) errors** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Weighted regression** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Serial correlation

Time-series/panel errors có thể correlated across thời gian (time / 시간). Naive SE underestimate bất định (uncertainty / 불확실성).

Need HAC/Newey-West, cluster-by-unit/thời gian (time / 시간) hoặc model-specific correction depending thiết kế (design / 설계).

> **Chuyển mạch:** Trong **Regression, Prediction & Suy luận (inference / 추론) — OLS là projection trước khi là nhân quả (causal / 인과적) tác động (effect / 효과)**, **23. Weighted regression** tiếp nhận điểm tựa từ **22. Serial correlation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Standardization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Weighted regression

Weights có nhiều meaning: sampling weights, frequency weights, precision weights.

Dùng weights phải giải thích estimand thay đổi thế nào. Survey weights giúp population representativeness; inverse-variance weights mục tiêu (target / 대상) precision under các giả định (assumptions / 가정들).

> **Chuyển mạch:** Ở chặng này của **Regression, Prediction & Suy luận (inference / 추론) — OLS là projection trước khi là nhân quả (causal / 인과적) tác động (effect / 효과)**, **24. Standardization** tiếp nhận điểm tựa từ **23. Weighted regression** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Log-level, level-log và log-log** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Standardization

Standardized coefficient đo thay đổi (change / 변경) in SD units, useful comparison but hides real economic units.

Chính sách (policy / 정책) interpretation nên quay lại natural units: dollars, percentage points, hours, test-score SD với ngữ cảnh (context / 맥락).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Regression, Prediction & Suy luận (inference / 추론) — OLS là projection trước khi là nhân quả (causal / 인과적) tác động (effect / 효과)**, **25. Log-level, level-log và log-log** tiếp nhận điểm tựa từ **24. Standardization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Extrapolation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Log-level, level-log và log-log

Dùng chung (common / 공통) interpretations:

```text
log(Y) on X: 1-unit X ≈ 100β% change Y
Y on log(X): 1% X ≈ β/100 unit Y
log(Y) on log(X): β ≈ elasticity
```

Approximations cần adjustment cho large coefficients.

> **Chuyển mạch:** Trong **Regression, Prediction & Suy luận (inference / 추론) — OLS là projection trước khi là nhân quả (causal / 인과적) tác động (effect / 효과)**, **26. Extrapolation** tiếp nhận điểm tựa từ **25. Log-level, level-log và log-log** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Regression to the mean** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Extrapolation

Regression line ngoài hỗ trợ (support / 지원) của X có thể vô nghĩa. A wage–experience quan hệ (relation / 관계) estimated age 20–60 không nên extrapolate đến age 120.

Plot dữ liệu (data / 데이터)/hỗ trợ (support / 지원) trước khi dùng fitted equation.

> **Chuyển mạch:** Ở chặng này của **Regression, Prediction & Suy luận (inference / 추론) — OLS là projection trước khi là nhân quả (causal / 인과적) tác động (effect / 효과)**, **27. Regression to the mean** tiếp nhận điểm tựa từ **26. Extrapolation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Multiple testing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Regression to the mean

Units selected vì extreme kết quả (outcome / 결과) thường move closer to average next period even without treatment.

Before-after phân tích (analysis / 분석) trên low-performing schools/patients dễ nhầm regression to mean với chính sách (policy / 정책) tác động (effect / 효과).

Need comparison group/thiết kế (design / 설계).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Regression, Prediction & Suy luận (inference / 추론) — OLS là projection trước khi là nhân quả (causal / 인과적) tác động (effect / 효과)**, **28. Multiple testing** tiếp nhận điểm tựa từ **27. Regression to the mean** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Specification searching** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Multiple testing

Nếu kiểm thử (test / 테스트) hàng trăm outcomes/specifications, some p-values nhỏ xuất hiện by chance.

Pre-specification, family-wise/FDR adjustments và transparent reporting giảm false discovery.

> **Chuyển mạch:** Trong **Regression, Prediction & Suy luận (inference / 추론) — OLS là projection trước khi là nhân quả (causal / 인과적) tác động (effect / 효과)**, **29. Specification searching** tiếp nhận điểm tựa từ **28. Multiple testing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. Prediction vs explanation vs causality** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Specification searching

Researcher degrees of freedom gồm điều khiển (control / 제어) set, mẫu (sample / 표본), kết quả (outcome / 결과) transform, thời gian (time / 시간) cửa sổ (window / 윈도우), subgroup.

Nếu specification được chọn sau khi nhìn desired sign/significance, nominal p-values mất meaning.

Robustness should show kết quả (result / 결과) across substantively defensible specifications, not cherry-pick.

> **Chuyển mạch:** Ở chặng này của **Regression, Prediction & Suy luận (inference / 추론) — OLS là projection trước khi là nhân quả (causal / 인과적) tác động (effect / 효과)**, **30. Prediction vs explanation vs causality** tiếp nhận điểm tựa từ **29. Specification searching** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. Thất bại (failure / 실패) modes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Prediction vs explanation vs causality

Regression có ba uses khác nhau:

```text
Description: summarize association
Prediction: forecast Y
Causality: estimate intervention effect
```

Một mô hình (model / 모델) có thể excellent prediction nhưng poor nhân quả (causal / 인과적) interpretation; một randomized treatment regression có low R² nhưng highly credible nhân quả (causal / 인과적) tác động (effect / 효과).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Regression, Prediction & Suy luận (inference / 추론) — OLS là projection trước khi là nhân quả (causal / 인과적) tác động (effect / 효과)**, **31. Thất bại (failure / 실패) modes** tiếp nhận điểm tựa từ **30. Prediction vs explanation vs causality** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Thất bại (failure / 실패) modes

Sai lầm thứ nhất là đọc every coefficient như nhân quả (causal / 인과적) tác động (effect / 효과).

Sai lầm thứ hai là dùng high R² làm bằng chứng (evidence / 증거) mô hình (model / 모델) đúng.

Sai lầm thứ ba là thêm controls không có lập luận nhân quả (causal reasoning / 인과적 추론).

Sai lầm thứ tư là dùng conventional SE khi heteroskedastic/clustered dependence rõ.

Sai lầm thứ năm là equate non-significance với no tác động (effect / 효과).

Sai lầm thứ sáu là extrapolate beyond hỗ trợ (support / 지원).

> **Chuyển mạch:** Trong **Regression, Prediction & Suy luận (inference / 추론) — OLS là projection trước khi là nhân quả (causal / 인과적) tác động (effect / 효과)**, **32. Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **31. Thất bại (failure / 실패) modes** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

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

> **Bàn giao:** Sau **32. Mô hình tư duy (mental model / 사고 모델)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
