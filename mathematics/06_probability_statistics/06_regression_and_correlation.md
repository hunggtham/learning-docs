# Hồi quy và tương quan: association, conditional modeling và prediction

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Hồi quy và tương quan: association, conditional modeling và prediction**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Covariance: direction của joint variation** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Pearson correlation là normalized covariance** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối regression với correlation, prediction và causality, để không biến liên hệ thống kê thành kết luận nguyên nhân.

Hồi quy (regression / 회귀) và tương quan (correlation / 상관관계) đều mô tả relationships giữa variables, nhưng chúng trả lời những câu hỏi khác nhau.

Correlation hỏi:

> Hai variables thay đổi cùng nhau mạnh đến mức nào theo một notion association cụ thể?

Regression hỏi:

> Ta muốn mô hình (model / 모델)/predict kết quả (outcome / 결과) như hàm (function / 함수) của predictors ra sao, và coefficients nên được hiểu như thế nào dưới các giả định (assumptions / 가정들) của mô hình (model / 모델)?

Cả hai đều **không tự động là nhân quả (causal / 인과적) phân tích (analysis / 분석)**.

## 1. Covariance: direction của joint variation

Với random variables `X,Y`, covariance:

```math
\operatorname{Cov}(X,Y)
=E[(X-E[X])(Y-E[Y])].
```

Nếu deviations thường cùng sign, covariance positive. Nếu opposite sign, negative.

Nhưng magnitude phụ thuộc units. Nếu đổi KRW thành million KRW, covariance đổi quy mô (scale / 규모).

Do đó cần normalized measure để so association across scales.

> **Chuyển mạch:** Trong **Hồi quy và tương quan: association, conditional modeling và prediction**, **2. Pearson correlation là normalized covariance** tiếp nhận điểm tựa từ **1. Covariance: direction của joint variation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Correlation chỉ đo tuyến tính (linear / 선형) association** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Pearson correlation là normalized covariance

Pearson correlation chuẩn hóa covariance để so sánh mức liên hệ tuyến tính không phụ thuộc đơn vị. Nó hữu ích cho mô tả nhưng không tự chứng minh nguyên nhân hay độ phù hợp của một mô hình dự báo.

```math
\rho_{XY}
=
\frac{\operatorname{Cov}(X,Y)}{
\sigma_X\sigma_Y
}.
```

Mẫu (sample / 표본) phiên bản (version / 버전):

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

Một geometric interpretation rất hữu ích: sau khi center observations, correlation là cosine giữa hai centered dữ liệu (data / 데이터) vectors.

Vì vậy `r=1` khi standardized patterns align perfectly linearly.

> **Chuyển mạch:** Ở chặng này của **Hồi quy và tương quan: association, conditional modeling và prediction**, **3. Correlation chỉ đo tuyến tính (linear / 선형) association** tiếp nhận điểm tựa từ **2. Pearson correlation là normalized covariance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Correlation không bất biến (invariant / 불변식) trước selection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Correlation chỉ đo tuyến tính (linear / 선형) association

`r≈0` không nghĩa “không có relationship”.

Ví dụ nếu

```math
Y=X^2
```

và `X` symmetric quanh zero, tuyến tính (linear / 선형) correlation có thể gần 0 dù `Y` được xác định hoàn toàn bởi `X`.

Do đó trước khi đọc correlation coefficient cần plot dữ liệu (data / 데이터) và hiểu shape.

Spearman correlation dùng ranks và đo monotonic association, nhưng cũng không phải universal dependence measure.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hồi quy và tương quan: association, conditional modeling và prediction**, **4. Correlation không bất biến (invariant / 불변식) trước selection** tiếp nhận điểm tựa từ **3. Correlation chỉ đo tuyến tính (linear / 선형) association** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Simple tuyến tính (linear / 선형) regression bắt đầu từ conditional mean mô hình (model / 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Correlation không bất biến (invariant / 불변식) trước selection

Nếu mẫu (sample / 표본) bị restricted phạm vi (range / 범위), correlation có thể shrink.

Nếu combine subgroups có centers khác nhau, correlation aggregate có thể khác hoặc đảo sign so với within-group correlations.

Đây là geometric/statistical phiên bản (version / 버전) của Simpson's paradox và selection effects.

> **Chuyển mạch:** Trong **Hồi quy và tương quan: association, conditional modeling và prediction**, **5. Simple tuyến tính (linear / 선형) regression bắt đầu từ conditional mean mô hình (model / 모델)** tiếp nhận điểm tựa từ **4. Correlation không bất biến (invariant / 불변식) trước selection** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Least squares đến từ projection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Simple tuyến tính (linear / 선형) regression bắt đầu từ conditional mean mô hình (model / 모델)

Mô hình (model / 모델):

```math
Y_i=\beta_0+\beta_1X_i+\varepsilon_i.
```

Một interpretation cốt lõi là

```math
E[Y\mid X=x]
=\beta_0+\beta_1x
```

nếu lỗi (error / 오류) có conditional mean zero.

Ta không nói mọi điểm (point / 지점) nằm trên line. Line mô tả conditional center; residuals mô tả unexplained variation.

> **Chuyển mạch:** Ở chặng này của **Hồi quy và tương quan: association, conditional modeling và prediction**, **6. Least squares đến từ projection** tiếp nhận điểm tựa từ **5. Simple tuyến tính (linear / 선형) regression bắt đầu từ conditional mean mô hình (model / 모델)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Derive simple-regression slope** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Least squares đến từ projection

Given dữ liệu (data / 데이터), least squares chọn

```math
\hat\beta_0,\hat\beta_1
```

để minimize

```math
\sum_i(y_i-\hat y_i)^2.
```

Trong ma trận (matrix / 행렬) form:

```math
\min_\beta\|X\beta-y\|_2^2.
```

Prediction véc-tơ (vector / 벡터) `X\hat\beta` là orthogonal projection của `y` lên column không gian (space / 공간) của thiết kế (design / 설계) ma trận (matrix / 행렬) `X`.

Đây là liên kết (connection / 연결) trực tiếp với tuyến tính (linear / 선형) algebra, không phải một statistics formula riêng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hồi quy và tương quan: association, conditional modeling và prediction**, **7. Derive simple-regression slope** tiếp nhận điểm tựa từ **6. Least squares đến từ projection** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Units của coefficient mang meaning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Derive simple-regression slope

Với centered variables, mô hình (model / 모델) không cần intercept tạm thời:

```math
\tilde y_i\approx\beta_1\tilde x_i.
```

Least-squares mục tiêu (objective / 목표):

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

under tuyến tính (linear / 선형) projection interpretation.

> **Chuyển mạch:** Trong **Hồi quy và tương quan: association, conditional modeling và prediction**, **8. Units của coefficient mang meaning** tiếp nhận điểm tựa từ **7. Derive simple-regression slope** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Multiple regression và “holding other variables fixed”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Units của coefficient mang meaning

Nếu regress electricity bill `Y` (KRW) trên usage `X` (kWh):

```math
\hat Y=8000+120X,
```

slope 120 có đơn vị (unit / 단위)

```text
KRW / kWh.
```

Nó nói conditional predicted bill thay khoảng 120 KRW cho mỗi additional kWh trong observed/mô hình (model / 모델) phạm vi (range / 범위).

Intercept 8000 là prediction tại `X=0`; nếu dữ liệu (data / 데이터) chỉ từ 200–500 kWh, interpretation intercept có thể là extrapolation và không meaningful.

> **Chuyển mạch:** Ở chặng này của **Hồi quy và tương quan: association, conditional modeling và prediction**, **9. Multiple regression và “holding other variables fixed”** tiếp nhận điểm tựa từ **8. Units của coefficient mang meaning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Omitted variable độ lệch (bias / 편향): vì sao nhân quả (causal / 인과적) interpretation dễ sai** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Multiple regression và “holding other variables fixed”

Mô hình (model / 모델):

```math
Y=\beta_0+\beta_1X_1+\cdots+\beta_pX_p+\varepsilon.
```

Coefficient `\beta_j` mô tả difference in mô hình (model / 모델) prediction per one-unit `X_j` thay đổi (change / 변경) while included other predictors held fixed.

Nhưng “hold fixed” trong regression là algebra/mô hình (model / 모델) comparison, không automatically equal a vật lý (physical / 물리적) intervention.

Nếu predictors correlated strongly, such comparisons may correspond to rare/unrealistic states.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hồi quy và tương quan: association, conditional modeling và prediction**, **10. Omitted variable độ lệch (bias / 편향): vì sao nhân quả (causal / 인과적) interpretation dễ sai** tiếp nhận điểm tựa từ **9. Multiple regression và “holding other variables fixed”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Residuals là dữ liệu (data / 데이터) về mô hình (model / 모델) thất bại (failure / 실패)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Omitted variable độ lệch (bias / 편향): vì sao nhân quả (causal / 인과적) interpretation dễ sai

Suppose true quan hệ (relation / 관계):

```math
Y=\beta_1X+\beta_2Z+\varepsilon,
```

nhưng ta regress only `Y` on `X`.

Nếu `Z` ảnh hưởng `Y` và correlated với `X`, estimated slope on `X` absorbs part of `Z` tác động (effect / 효과).

Đây là omitted-variable độ lệch (bias / 편향).

Ví dụ salary và defects có thể correlate vì seniority/dự án (project / 프로젝트) độ phức tạp (complexity / 복잡도). Regression coefficient không tự động là nhân quả (causal / 인과적) tác động (effect / 효과) của salary.

> **Chuyển mạch:** Trong **Hồi quy và tương quan: association, conditional modeling và prediction**, **10. Omitted variable độ lệch (bias / 편향): vì sao nhân quả (causal / 인과적) interpretation dễ sai** nêu điều cần giải thích; **11. Residuals là dữ liệu (data / 데이터) về mô hình (model / 모델) thất bại (failure / 실패)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **12. Homoskedasticity và heteroskedasticity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Residuals là dữ liệu (data / 데이터) về mô hình (model / 모델) thất bại (failure / 실패)

Residual:

```math
e_i=y_i-\hat y_i.
```

Residual diagnostics hỏi:

- còn nonlinear mẫu (pattern / 패턴) không?
- variance có tăng theo fitted giá trị (value / 값) không?
- residuals có serial dependence không?
- có influential points không?
- tails có heavier hơn assumed phân phối (distribution / 분포) không?

Một high `R^2` không trả lời những questions này.

> **Chuyển mạch:** Ở chặng này của **Hồi quy và tương quan: association, conditional modeling và prediction**, **11. Residuals là dữ liệu (data / 데이터) về mô hình (model / 모델) thất bại (failure / 실패)** nêu điều cần giải thích; **12. Homoskedasticity và heteroskedasticity** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **13. Independence và thời gian (time / 시간) series** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Homoskedasticity và heteroskedasticity

Homoskedasticity giả định (assumption / 가정) roughly:

```math
\operatorname{Var}(\varepsilon\mid X)=\sigma^2.
```

Nếu residual spread phụ thuộc `X`, ta có heteroskedasticity.

OLS coefficient estimates có thể vẫn unbiased/consistent dưới some conditions, nhưng conventional tiêu chuẩn (standard / 표준) errors có thể sai. Robust tiêu chuẩn (standard / 표준) errors hoặc mô hình (model / 모델) variance cấu trúc (structure / 구조) có thể cần thiết.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hồi quy và tương quan: association, conditional modeling và prediction**, **13. Independence và thời gian (time / 시간) series** tiếp nhận điểm tựa từ **12. Homoskedasticity và heteroskedasticity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. R^2 là gì và không phải gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Independence và thời gian (time / 시간) series

Trong thời gian (time / 시간) series, residuals thường autocorrelated.

Nếu assume iid errors khi dữ liệu (data / 데이터) có serial dependence, bất định (uncertainty / 불확실성) estimates có thể quá optimistic.

Regression cho time-indexed dữ liệu (data / 데이터) cần diagnostics/modeling như AR terms, Newey–West style robust errors hoặc full time-series các mô hình (models / 모델들) tùy goal.

> **Chuyển mạch:** Trong **Hồi quy và tương quan: association, conditional modeling và prediction**, **14. R^2 là gì và không phải gì?** tiếp nhận điểm tựa từ **13. Independence và thời gian (time / 시간) series** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Prediction intervals khác confidence intervals** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. `R^2` là gì và không phải gì?

Tiêu chuẩn (standard / 표준) definition:

```math
R^2
=1-
\frac{\sum_i(y_i-\hat y_i)^2}
{\sum_i(y_i-\bar y)^2}.
```

Nó so residual squared lỗi (error / 오류) với baseline predict mean.

High `R^2` không guarantee:

- nhân quả (causal / 인과적) validity;
- good extrapolation;
- correct functional form;
- unbiased predictions for subgroups;
- môi trường vận hành (production / 운영 환경) generalization.

Adding predictors thường không decrease huấn luyện (training / 학습) `R^2`, nên adjusted metrics/cross-validation cần cho mô hình (model / 모델) comparison.

> **Chuyển mạch:** Ở chặng này của **Hồi quy và tương quan: association, conditional modeling và prediction**, **15. Prediction intervals khác confidence intervals** tiếp nhận điểm tựa từ **14. R^2 là gì và không phải gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Regularization: đổi mục tiêu (objective / 목표) để trade độ lệch (bias / 편향) lấy variance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Prediction intervals khác confidence intervals

Confidence interval cho mean phản hồi (response / 응답) tại `x` quantify bất định (uncertainty / 불확실성) về conditional mean.

Prediction interval cho một new observation rộng hơn vì gồm cả model-mean bất định (uncertainty / 불확실성) và irreducible observation noise.

Hai intervals answer different questions.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hồi quy và tương quan: association, conditional modeling và prediction**, **16. Regularization: đổi mục tiêu (objective / 목표) để trade độ lệch (bias / 편향) lấy variance** tiếp nhận điểm tựa từ **15. Prediction intervals khác confidence intervals** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Multicollinearity và identifiability** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Regularization: đổi mục tiêu (objective / 목표) để trade độ lệch (bias / 편향) lấy variance

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

Regularization deliberately introduces độ lệch (bias / 편향) để reduce variance/generalization lỗi (error / 오류).

Đây là statistics phiên bản (version / 버전) của bias-variance sự đánh đổi (trade-off / 트레이드오프).

> **Chuyển mạch:** Trong **Hồi quy và tương quan: association, conditional modeling và prediction**, **17. Multicollinearity và identifiability** tiếp nhận điểm tựa từ **16. Regularization: đổi mục tiêu (objective / 목표) để trade độ lệch (bias / 편향) lấy variance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Logistic regression: mô hình tuyến tính (linear model / 선형 모델) trên log-odds quy mô (scale / 규모)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Multicollinearity và identifiability

Nếu columns predictors gần linearly dependent, many coefficient combinations produce similar predictions.

Then individual coefficients become unstable even if overall predictions okay.

Điều kiện (condition / 조건) number/SVD từ numerical tuyến tính (linear / 선형) algebra giúp diagnose this hình học (geometry / 기하학).

Statistics và numerical tuyến tính (linear / 선형) algebra gặp nhau trực tiếp ở đây.

> **Chuyển mạch:** Ở chặng này của **Hồi quy và tương quan: association, conditional modeling và prediction**, **18. Logistic regression: mô hình tuyến tính (linear model / 선형 모델) trên log-odds quy mô (scale / 규모)** tiếp nhận điểm tựa từ **17. Multicollinearity và identifiability** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Maximum likelihood viewpoint** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Logistic regression: mô hình tuyến tính (linear model / 선형 모델) trên log-odds quy mô (scale / 규모)

Với nhị phân (binary / 이진) kết quả (outcome / 결과), xác suất (probability / 확률) must stay in `[0,1]`.

Mô hình (model / 모델):

```math
\log\frac{p}{1-p}
=\beta_0+\beta^Tx.
```

Invert:

```math
p=
\frac{1}{1+e^{-(\beta_0+\beta^Tx)}}.
```

Coefficient `\beta_j` là additive thay đổi (change / 변경) in log-odds per đơn vị (unit / 단위) predictor; exponentiating gives odds ratio:

```math
e^{\beta_j}.
```

Điều này nối logarithms/exponentials với statistical modeling.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hồi quy và tương quan: association, conditional modeling và prediction**, **19. Maximum likelihood viewpoint** tiếp nhận điểm tựa từ **18. Logistic regression: mô hình tuyến tính (linear model / 선형 모델) trên log-odds quy mô (scale / 규모)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Nonlinear regression và mô hình (model / 모델) flexibility** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Maximum likelihood viewpoint

Under Gaussian lỗi (error / 오류) các giả định (assumptions / 가정들) with constant variance, minimizing squared lỗi (error / 오류) tương đương maximizing Gaussian likelihood.

Do đó least squares không chỉ geometric projection; nó cũng là probabilistic estimation under a specific noise mô hình (model / 모델).

Nếu noise mô hình (model / 모델) khác, optimal mất mát (loss / 손실) có thể khác.

Ví dụ Laplace noise liên hệ L1 mất mát (loss / 손실).

> **Chuyển mạch:** Trong **Hồi quy và tương quan: association, conditional modeling và prediction**, **20. Nonlinear regression và mô hình (model / 모델) flexibility** tiếp nhận điểm tựa từ **19. Maximum likelihood viewpoint** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Extrapolation là giả định (assumption / 가정) mạnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Nonlinear regression và mô hình (model / 모델) flexibility

Regression không đồng nghĩa tuyến tính (linear / 선형) regression.

Ta có thể dùng:

- polynomial basis;
- splines;
- generalized tuyến tính (linear / 선형) các mô hình (models / 모델들);
- trees;
- neural networks.

Càng flexible, approximation độ lệch (bias / 편향) có thể giảm nhưng overfitting rủi ro (risk / 위험) tăng. Cross-validation và regularization trở nên quan trọng.

> **Chuyển mạch:** Ở chặng này của **Hồi quy và tương quan: association, conditional modeling và prediction**, **21. Extrapolation là giả định (assumption / 가정) mạnh** tiếp nhận điểm tựa từ **20. Nonlinear regression và mô hình (model / 모델) flexibility** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Worked example: confounding** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Extrapolation là giả định (assumption / 가정) mạnh

Mô hình (model / 모델) fit tốt trong observed phạm vi (range / 범위) không guarantee hành vi (behavior / 동작) ngoài phạm vi (range / 범위).

Một quadratic fit cho historical growth có thể explode absurdly khi extrapolate xa.

Physics/lĩnh vực (domain / 도메인) các ràng buộc (constraints / 제약조건들) đôi khi quan trọng hơn fit lỗi (error / 오류) trong-sample.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hồi quy và tương quan: association, conditional modeling và prediction**, **21. Extrapolation là giả định (assumption / 가정) mạnh** cho ta quy tắc; **22. Worked example: confounding** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **23. Finance: beta là regression coefficient có các giả định (assumptions / 가정들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Worked example: confounding

Suppose dữ liệu (data / 데이터) cho thấy projects có higher nhà phát triển (developer / 개발자) salary cũng có more defects.

Simple regression có positive salary coefficient.

Nhưng nếu high-salary cấp cao (senior / 시니어) engineers được assign tới projects phức tạp hơn, dự án (project / 프로젝트) độ phức tạp (complexity / 복잡도) là confounder ảnh hưởng cả salary composition và defects.

Thêm độ phức tạp (complexity / 복잡도) variables có thể thay đổi (change / 변경) coefficient, nhưng nhân quả (causal / 인과적) validity còn phụ thuộc whether confounders measured correctly và no major unmeasured confounding.

Regression adjustment là công cụ (tool / 도구), không phải automatic nhân quả (causal / 인과적) machine.

> **Chuyển mạch:** Trong **Hồi quy và tương quan: association, conditional modeling và prediction**, **22. Worked example: confounding** cho ta quy tắc; **23. Finance: beta là regression coefficient có các giả định (assumptions / 가정들)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **24. AI: regression as supervised học tập (learning / 학습)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Finance: beta là regression coefficient có các giả định (assumptions / 가정들)

CAPM-style beta thường estimated từ regression asset excess returns trên thị trường (market / 시장) excess returns:

```math
R_i-R_f
=\alpha+\beta(R_m-R_f)+\varepsilon.
```

`\beta` đo tuyến tính (linear / 선형) sensitivity in mẫu (sample / 표본)/mô hình (model / 모델).

Nó không phải immutable vật lý (physical / 물리적) constant; estimate phụ thuộc cửa sổ (window / 윈도우), frequency, regime và dữ liệu (data / 데이터) chất lượng (quality / 품질).

> **Chuyển mạch:** Ở chặng này của **Hồi quy và tương quan: association, conditional modeling và prediction**, **24. AI: regression as supervised học tập (learning / 학습)** tiếp nhận điểm tựa từ **23. Finance: beta là regression coefficient có các giả định (assumptions / 가정들)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Correlation, regression và causality — relationship map** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. AI: regression as supervised học tập (learning / 학습)

Supervised học tập (learning / 학습) generalizes regression idea:

```text
features X → target Y
```

Hàm mất mát (loss function / 손실 함수) defines what “best fit” means.

Train lỗi (error / 오류) measures fit observed dữ liệu (data / 데이터); kiểm tra hợp lệ (validation / 검증)/kiểm thử (test / 테스트) estimate generalization. phân phối (distribution / 분포) shift can break both regression các giả định (assumptions / 가정들) và ML hiệu năng (performance / 성능).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hồi quy và tương quan: association, conditional modeling và prediction**, **25. Correlation, regression và causality — relationship map** tiếp nhận điểm tựa từ **24. AI: regression as supervised học tập (learning / 학습)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Correlation, regression và causality — relationship map

Bản đồ này phân biệt ba câu hỏi: hai biến có cùng thay đổi không, một biến dự đoán biến kia tốt đến đâu, và can thiệp có làm kết quả đổi không. Giữ ranh giới này giúp tránh diễn giải hồi quy như bằng chứng nhân quả.

```text
Correlation
    ↓ describes association
Regression
    ↓ models conditional relationship / prediction
Causal inference
    ↓ asks intervention/counterfactual effect
```

Chúng có thể dùng chung algebra/xác suất (probability / 확률), nhưng estimand khác nhau.

> **Chuyển mạch:** Trong **Hồi quy và tương quan: association, conditional modeling và prediction**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **25. Correlation, regression và causality — relationship map** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Correlation measures alignment. Regression constructs a predictive/conditional surface. nhân quả (causal / 인과적) suy luận (inference / 추론) asks what would thay đổi (change / 변경) under intervention. Least squares is projection hình học (geometry / 기하학); statistical interpretation arrives only after specifying how dữ liệu (data / 데이터)/noise were generated.

> **Chuyển mạch:** Ở chặng này của **Hồi quy và tương quan: association, conditional modeling và prediction**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**`r=0` means no relationship.** Không; it means no tuyến tính (linear / 선형) association under Pearson measure.

**High `R^2` means mô hình (model / 모델) is correct.** Không; wrong nhân quả (causal / 인과적)/functional mô hình (model / 모델) có thể vẫn fit mẫu (sample / 표본) tốt.

**Regression coefficient is automatically a nhân quả (causal / 인과적) tác động (effect / 효과).** Không; nhân quả (causal / 인과적) interpretation needs identification các giả định (assumptions / 가정들)/thiết kế (design / 설계).

**More predictors always improve mô hình (model / 모델).** huấn luyện (training / 학습) fit often improves, but variance, multicollinearity and overfitting can worsen generalization.

**OLS formula `(X^TX)^{-1}X^Ty` is how software should always solve regression.** Numerical implementations often prefer QR/SVD for stability.

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
