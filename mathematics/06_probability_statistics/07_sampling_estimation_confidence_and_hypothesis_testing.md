# Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Population, mẫu (sample / 표본), parameter và statistic** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Sampling thiết kế (design / 설계) quan trọng hơn cỡ mẫu (sample size / 표본 크기)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối sampling với estimation, confidence và hypothesis testing, để suy luận về quần thể luôn đi kèm bất định.

Thống kê suy luận (statistical inference / 통계적 추론) bắt đầu từ một giới hạn cơ bản: ta muốn biết điều gì đó về một population hoặc tiến trình (process / 프로세스) lớn, nhưng chỉ quan sát một mẫu (sample / 표본) hữu hạn.

Do đó mọi suy luận (inference / 추론) phải giữ rõ bốn lớp:

```text
population / process
→ sampling mechanism
→ observed sample
→ uncertainty about target quantity
```

Sai ở sampling cơ chế (mechanism / 메커니즘) thì formula phía sau có thể rất chính xác nhưng vẫn trả lời sai câu hỏi.

## 1. Population, mẫu (sample / 표본), parameter và statistic

Population là mục tiêu (target / 대상) tiến trình (process / 프로세스) hoặc tập đối tượng ta muốn hiểu.

Parameter là quantity của population, ví dụ:

```math
\mu,\quad \sigma^2,\quad p.
```

Mẫu (sample / 표본):

```math
X_1,\ldots,X_n.
```

Statistic là hàm (function / 함수) của mẫu (sample / 표본):

```math
T=T(X_1,\ldots,X_n).
```

Ví dụ mẫu (sample / 표본) mean:

```math
\bar X
=\frac1n\sum_{i=1}^{n}X_i.
```

Trong frequentist khung phần mềm (framework / 프레임워크), parameter là fixed unknown; statistic là random trước khi dữ liệu (data / 데이터) được quan sát.

> **Chuyển mạch:** Trong **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **2. Sampling thiết kế (design / 설계) quan trọng hơn cỡ mẫu (sample size / 표본 크기)** tiếp nhận điểm tựa từ **1. Population, mẫu (sample / 표본), parameter và statistic** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Random sampling tạo cầu nối (bridge / 브리지) từ mẫu (sample / 표본) sang population** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Sampling thiết kế (design / 설계) quan trọng hơn cỡ mẫu (sample size / 표본 크기)

Một mẫu (sample / 표본) rất lớn nhưng systematically biased có thể estimate sai quantity với precision rất cao.

Ví dụ survey chỉ gửi cho users active trong 7 ngày gần nhất nhưng claim đại diện toàn bộ users.

Increasing `n` giảm random sampling lỗi (error / 오류), nhưng không tự sửa:

- selection độ lệch (bias / 편향);
- nonresponse độ lệch (bias / 편향);
- đo lường (measurement / 측정) độ lệch (bias / 편향);
- survivorship độ lệch (bias / 편향);
- confounding.

Mental quy tắc (rule / 규칙):

```text
more data ≠ better identification
```

nếu data-generating/sampling tiến trình (process / 프로세스) sai.

> **Chuyển mạch:** Ở chặng này của **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **3. Random sampling tạo cầu nối (bridge / 브리지) từ mẫu (sample / 표본) sang population** tiếp nhận điểm tựa từ **2. Sampling thiết kế (design / 설계) quan trọng hơn cỡ mẫu (sample size / 표본 크기)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Sampling phân phối (distribution / 분포) là phân phối (distribution / 분포) của estimator qua repeated samples** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Random sampling tạo cầu nối (bridge / 브리지) từ mẫu (sample / 표본) sang population

Simple random sampling idealize rằng mỗi observation được lấy theo cơ chế (mechanism / 메커니즘) đã biết và representative theo xác suất.

IID giả định (assumption / 가정) thường viết:

```math
X_1,\ldots,X_n\overset{iid}{\sim}F.
```

Nó gói hai các giả định (assumptions / 가정들):

```text
identically distributed
independent
```

Real dữ liệu (data / 데이터) thường chỉ approximately iid hoặc không iid chút nào. thời gian (time / 시간) series, clusters, repeated measurements và mạng (network / 네트워크) dữ liệu (data / 데이터) cần dependency-aware methods.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **4. Sampling phân phối (distribution / 분포) là phân phối (distribution / 분포) của estimator qua repeated samples** tiếp nhận điểm tựa từ **3. Random sampling tạo cầu nối (bridge / 브리지) từ mẫu (sample / 표본) sang population** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Vì sao bất định (uncertainty / 불확실성) giảm theo 1/sqrt(n)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Sampling phân phối (distribution / 분포) là phân phối (distribution / 분포) của estimator qua repeated samples

Nếu ta lặp toàn bộ sampling procedure nhiều lần, statistic thay đổi.

Phân phối (distribution / 분포) đó gọi sampling phân phối (distribution / 분포).

Ví dụ với mẫu (sample / 표본) mean:

```math
E[\bar X]=\mu
```

và nếu observations independent cùng variance `\sigma^2`:

```math
\operatorname{Var}(\bar X)=\frac{\sigma^2}{n}.
```

Tiêu chuẩn (standard / 표준) lỗi (error / 오류):

```math
SE(\bar X)=\frac{\sigma}{\sqrt n}.
```

Tiêu chuẩn (standard / 표준) lỗi (error / 오류) không phải tiêu chuẩn (standard / 표준) deviation của raw observations. Nó là bất định (uncertainty / 불확실성) của estimator.

> **Chuyển mạch:** Trong **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **5. Vì sao bất định (uncertainty / 불확실성) giảm theo 1/sqrt(n)?** tiếp nhận điểm tựa từ **4. Sampling phân phối (distribution / 분포) là phân phối (distribution / 분포) của estimator qua repeated samples** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Dependence làm effective cỡ mẫu (sample size / 표본 크기) nhỏ hơn raw count** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Vì sao bất định (uncertainty / 불확실성) giảm theo 1/sqrt(n)?

Average:

```math
\bar X=\frac1n\sum_iX_i.
```

Independent variances add:

```math
\operatorname{Var}\left(\sum_iX_i\right)=n\sigma^2.
```

Divide by `n^2`:

```math
\operatorname{Var}(\bar X)=\frac{\sigma^2}{n}.
```

Take square gốc (root / 루트):

```math
SE=\frac\sigma{\sqrt n}.
```

Diminishing returns:

```text
2× smaller SE → 4× sample
10× smaller SE → 100× sample
```

> **Chuyển mạch:** Ở chặng này của **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **6. Dependence làm effective cỡ mẫu (sample size / 표본 크기) nhỏ hơn raw count** tiếp nhận điểm tựa từ **5. Vì sao bất định (uncertainty / 불확실성) giảm theo 1/sqrt(n)?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Estimator: quy tắc (rule / 규칙) map mẫu (sample / 표본) → estimate** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Dependence làm effective cỡ mẫu (sample size / 표본 크기) nhỏ hơn raw count

Nếu observations positively correlated:

```math
\operatorname{Var}\left(\sum_iX_i\right)
=
\sum_i\operatorname{Var}(X_i)
+2\sum_{i<j}\operatorname{Cov}(X_i,X_j).
```

Positive covariance increases bất định (uncertainty / 불확실성).

Một million highly correlated observations có thể chứa ít independent thông tin (information / 정보) hơn nhiều so với one million iid observations.

Trong thời gian (time / 시간) series, MCMC và clustered experiments, effective cỡ mẫu (sample size / 표본 크기) quan trọng hơn raw `n`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **7. Estimator: quy tắc (rule / 규칙) map mẫu (sample / 표본) → estimate** tiếp nhận điểm tựa từ **6. Dependence làm effective cỡ mẫu (sample size / 표본 크기) nhỏ hơn raw count** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. độ lệch (bias / 편향) và variance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Estimator: quy tắc (rule / 규칙) map mẫu (sample / 표본) → estimate

Estimator:

```math
\hat\theta=T(X_1,\ldots,X_n).
```

Các qualities thường xét:

```text
bias
variance
consistency
efficiency
robustness
```

Không có estimator “tốt nhất” independent of mất mát (loss / 손실)/mô hình (model / 모델).

> **Chuyển mạch:** Trong **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **8. độ lệch (bias / 편향) và variance** tiếp nhận điểm tựa từ **7. Estimator: quy tắc (rule / 규칙) map mẫu (sample / 표본) → estimate** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Consistency là large-sample thuộc tính (property / 속성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. độ lệch (bias / 편향) và variance

Độ lệch (bias / 편향):

```math
\operatorname{Bias}(\hat\theta)
=E[\hat\theta]-\theta.
```

Variance:

```math
\operatorname{Var}(\hat\theta).
```

Mean squared lỗi (error / 오류):

```math
MSE
=E[(\hat\theta-\theta)^2]
=\operatorname{Var}(\hat\theta)
+\operatorname{Bias}(\hat\theta)^2.
```

Một slightly biased estimator có thể có lower MSE nếu variance giảm nhiều.

Đây là foundation của độ lệch (bias / 편향)–variance sự đánh đổi (trade-off / 트레이드오프) trong machine học tập (learning / 학습).

> **Chuyển mạch:** Ở chặng này của **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **9. Consistency là large-sample thuộc tính (property / 속성)** tiếp nhận điểm tựa từ **8. độ lệch (bias / 편향) và variance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Standardization tạo pivot-like quantities** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Consistency là large-sample thuộc tính (property / 속성)

Estimator consistent nếu

```math
\hat\theta_n\to\theta
```

trong suitable probabilistic sense khi `n\to\infty`.

Unbiasedness và consistency khác nhau.

Một estimator có thể biased finite-sample nhưng độ lệch (bias / 편향) vanish asymptotically.

Một estimator unbiased cũng có thể variance lớn và thực tế poor.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **10. Standardization tạo pivot-like quantities** tiếp nhận điểm tựa từ **9. Consistency là large-sample thuộc tính (property / 속성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Confidence interval là procedure, không phải posterior statement** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Standardization tạo pivot-like quantities

Nếu

```math
\bar X\approx N\left(\mu,\frac{\sigma^2}{n}\right),
```

thì

```math
Z=
\frac{\bar X-\mu}{\sigma/\sqrt n}
```

có phân phối (distribution / 분포) tiêu chuẩn (standard / 표준) normal under ideal các giả định (assumptions / 가정들).

Suy luận (inference / 추론) hoạt động bằng cách tìm statistic có phân phối (distribution / 분포) known/approximately known không phụ thuộc unknown parameter quá nhiều.

> **Chuyển mạch:** Trong **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **11. Confidence interval là procedure, không phải posterior statement** tiếp nhận điểm tựa từ **10. Standardization tạo pivot-like quantities** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Derive normal mean interval** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Confidence interval là procedure, không phải posterior statement

Một 95% frequentist confidence procedure có coverage 95% nếu repeated sampling theo mô hình (model / 모델) làm khoảng 95% intervals chứa true parameter.

Sau khi interval cụ thể `[L,U]` được tính, strict frequentist interpretation không nói:

```text
P(θ ∈ [L,U] | observed data) = 0.95
```

Parameter không random trong khung phần mềm (framework / 프레임워크) đó.

Meaning là thuộc tính (property / 속성) của procedure qua repeated samples.

> **Chuyển mạch:** Ở chặng này của **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **12. Derive normal mean interval** tiếp nhận điểm tựa từ **11. Confidence interval là procedure, không phải posterior statement** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Student t xuất hiện khi σ unknown** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Derive normal mean interval

Nếu `\sigma` known và mẫu (sample / 표본) mean normal/CLT justified:

```math
\frac{\bar X-\mu}{\sigma/\sqrt n}
\sim N(0,1).
```

Với

```math
P(-z_{0.975}\le Z\le z_{0.975})=0.95,
```

rearrange:

```math
\bar X-z_{0.975}\frac\sigma{\sqrt n}
\le\mu\le
\bar X+z_{0.975}\frac\sigma{\sqrt n}.
```

CI formula đến từ xác suất (probability / 확률) statement về standardized estimator, không phải quy tắc (rule / 규칙) memorization.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **13. Student t xuất hiện khi σ unknown** tiếp nhận điểm tựa từ **12. Derive normal mean interval** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Confidence interval width phản ánh three ingredients** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Student t xuất hiện khi σ unknown

Khi population normal và `\sigma` unknown, thay bằng mẫu (sample / 표본) tiêu chuẩn (standard / 표준) deviation `s` làm extra bất định (uncertainty / 불확실성).

Statistic:

```math
T=
\frac{\bar X-\mu}{s/\sqrt n}
```

follow Student t phân phối (distribution / 분포) with `n-1` degrees of freedom under các giả định (assumptions / 가정들).

T tails heavier than normal, reflecting bất định (uncertainty / 불확실성) from estimating `\sigma`.

As `n` grows, t approaches normal.

> **Chuyển mạch:** Trong **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **14. Confidence interval width phản ánh three ingredients** tiếp nhận điểm tựa từ **13. Student t xuất hiện khi σ unknown** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Bootstrap: approximate sampling phân phối (distribution / 분포) bằng resampling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Confidence interval width phản ánh three ingredients

Roughly:

```text
CI width
≈ critical value × standard error
```

Width increases with:

- higher noise;
- higher confidence mức (level / 수준);
- dependence/thiết kế (design / 설계) tác động (effect / 효과).

Width decreases with:

- larger effective cỡ mẫu (sample size / 표본 크기).

Narrow interval không guarantee unbiased sampling.

> **Chuyển mạch:** Ở chặng này của **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **15. Bootstrap: approximate sampling phân phối (distribution / 분포) bằng resampling** tiếp nhận điểm tựa từ **14. Confidence interval width phản ánh three ingredients** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Hypothesis testing là calibration của extremeness under H0** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Bootstrap: approximate sampling phân phối (distribution / 분포) bằng resampling

Bootstrap resamples observed dữ liệu (data / 데이터) with replacement để mimic repeated sampling under empirical phân phối (distribution / 분포).

Workflow:

```text
sample data
→ resample many times
→ recompute statistic
→ approximate estimator distribution
```

Useful khi analytic SE khó.

Nhưng bootstrap không automatically fix nonrepresentative dữ liệu (data / 데이터) hoặc severe phụ thuộc (dependency / 의존성); resampling scheme phải match cấu trúc dữ liệu (data structure / 자료구조).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **16. Hypothesis testing là calibration của extremeness under H0** tiếp nhận điểm tựa từ **15. Bootstrap: approximate sampling phân phối (distribution / 분포) bằng resampling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. P-value không phải xác suất (probability / 확률) H0 đúng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Hypothesis testing là calibration của extremeness under H0

Null hypothesis:

```math
H_0:\theta=\theta_0.
```

Choose kiểm thử (test / 테스트) statistic `T` whose phân phối (distribution / 분포) under `H_0` is known/approximated.

Observe `t_{obs}`.

P-value asks:

> Nếu `H_0` và các giả định (assumptions / 가정들) đúng, xác suất (probability / 확률) thấy statistic at least as extreme as observed là bao nhiêu?

Form depends one-sided/two-sided kiểm thử (test / 테스트).

> **Chuyển mạch:** Trong **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **17. P-value không phải xác suất (probability / 확률) H0 đúng** tiếp nhận điểm tựa từ **16. Hypothesis testing là calibration của extremeness under H0** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Significance mức (level / 수준) α là decision-rule lỗi (error / 오류) calibration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. P-value không phải xác suất (probability / 확률) H0 đúng

Wrong interpretation:

```text
p = 0.03 → H0 chỉ có 3% chance đúng
```

Frequentist p-value là:

```math
P(\text{data/test statistic at least this extreme}\mid H_0).
```

Nó không đảo conditioning.

Để nói posterior xác suất (probability / 확률) of hypothesis cần prior/mô hình (model / 모델), như Bayesian suy luận (inference / 추론).

> **Chuyển mạch:** Ở chặng này của **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **18. Significance mức (level / 수준) α là decision-rule lỗi (error / 오류) calibration** tiếp nhận điểm tựa từ **17. P-value không phải xác suất (probability / 확률) H0 đúng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. kiểu (type / 타입) I, kiểu (type / 타입) II và power** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Significance mức (level / 수준) α là decision-rule lỗi (error / 오류) calibration

Kiểm thử (test / 테스트) quy tắc (rule / 규칙):

```text
reject H0 if p ≤ α
```

Under chính xác (exact / 정확한) kiểm thử (test / 테스트) các giả định (assumptions / 가정들) và true `H_0`, long-run kiểu (type / 타입) I lỗi (error / 오류) tỷ lệ (rate / 비율) được điều khiển (control / 제어) gần `\alpha`.

`\alpha=0.05` không phải law of nature. Nó là convention/quyết định (decision / 결정) threshold và phải liên hệ chi phí (cost / 비용) of false positives.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **19. kiểu (type / 타입) I, kiểu (type / 타입) II và power** tiếp nhận điểm tựa từ **18. Significance mức (level / 수준) α là decision-rule lỗi (error / 오류) calibration** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Non-significant kết quả (result / 결과) ≠ bằng chứng (evidence / 증거) of no tác động (effect / 효과)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. kiểu (type / 타입) I, kiểu (type / 타입) II và power

Kiểu (type / 타입) I:

```text
reject true H0
```

Xác suất (probability / 확률) controlled by `\alpha`.

Kiểu (type / 타입) II:

```text
fail to reject H0 when alternative true
```

Xác suất (probability / 확률) `\beta` for specified alternative.

Power:

```math
1-\beta.
```

Power depends on:

```text
effect size
noise
sample size
test threshold
design
```

> **Chuyển mạch:** Trong **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **19. kiểu (type / 타입) I, kiểu (type / 타입) II và power** nêu điều cần giải thích; **20. Non-significant kết quả (result / 결과) ≠ bằng chứng (evidence / 증거) of no tác động (effect / 효과)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **21. Statistical significance vs practical significance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Non-significant kết quả (result / 결과) ≠ bằng chứng (evidence / 증거) of no tác động (effect / 효과)

If p-value > 0.05, dữ liệu (data / 데이터) may be:

- consistent with no tác động (effect / 효과);
- too noisy;
- underpowered;
- poorly measured;
- affected by thiết kế (design / 설계) issues.

To claim equivalence/no practically meaningful tác động (effect / 효과), use equivalence/noninferiority khung phần mềm (framework / 프레임워크) or interval relative to practical threshold.

Absence of significance is not automatically significance of absence.

> **Chuyển mạch:** Ở chặng này của **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **20. Non-significant kết quả (result / 결과) ≠ bằng chứng (evidence / 증거) of no tác động (effect / 효과)** nêu điều cần giải thích; **21. Statistical significance vs practical significance** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **22. tác động (effect / 효과) kích thước (size / 크기) creates lĩnh vực (domain / 도메인) quy mô (scale / 규모)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Statistical significance vs practical significance

With huge mẫu (sample / 표본), tiny tác động (effect / 효과) can have tiny p-value.

Example:

```text
conversion 10.00% → 10.05%
```

Could be statistically certain but nghiệp vụ (business / 비즈니스) giá trị (value / 값) depends traffic, margin and hiện thực (implementation / 구현) chi phí (cost / 비용).

Always pair suy luận (inference / 추론) with tác động (effect / 효과) kích thước (size / 크기) and bất định (uncertainty / 불확실성) interval.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **22. tác động (effect / 효과) kích thước (size / 크기) creates lĩnh vực (domain / 도메인) quy mô (scale / 규모)** tiếp nhận điểm tựa từ **21. Statistical significance vs practical significance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. One-sided vs two-sided tests must be chosen before seeing dữ liệu (data / 데이터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. tác động (effect / 효과) kích thước (size / 크기) creates lĩnh vực (domain / 도메인) quy mô (scale / 규모)

Examples:

- mean difference in original units;
- standardized mean difference;
- rủi ro (risk / 위험) ratio;
- odds ratio;
- absolute rủi ro (risk / 위험) difference.

Different tác động (effect / 효과) measures answer different questions.

A p-value alone lacks practical quy mô (scale / 규모).

> **Chuyển mạch:** Trong **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **22. tác động (effect / 효과) kích thước (size / 크기) creates lĩnh vực (domain / 도메인) quy mô (scale / 규모)** nêu điều cần giải thích; **23. One-sided vs two-sided tests must be chosen before seeing dữ liệu (data / 데이터)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **24. Multiple testing creates false discovery pressure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. One-sided vs two-sided tests must be chosen before seeing dữ liệu (data / 데이터)

Two-sided alternative:

```math
H_1:\theta\ne\theta_0.
```

One-sided:

```math
H_1:\theta>\theta_0.
```

Choosing direction after seeing kết quả (result / 결과) inflates false-positive rủi ro (risk / 위험).

Kiểm thử (test / 테스트) thiết kế (design / 설계) must be specified independently of favorable observed kết quả (outcome / 결과).

> **Chuyển mạch:** Ở chặng này của **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **23. One-sided vs two-sided tests must be chosen before seeing dữ liệu (data / 데이터)** nêu điều cần giải thích; **24. Multiple testing creates false discovery pressure** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **25. Optional stopping and repeated peeking can inflate kiểu (type / 타입) I lỗi (error / 오류)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Multiple testing creates false discovery pressure

Run 100 independent null tests at `\alpha=0.05`; expected false rejections about 5.

Xác suất (probability / 확률) of at least one false positive can be high.

Bonferroni controls family-wise lỗi (error / 오류):

```math
\alpha_{each}=\frac\alpha m.
```

Benjamini–Hochberg controls false discovery tỷ lệ (rate / 비율) under các giả định (assumptions / 가정들) and is less conservative for discovery settings.

Different corrections optimize different lỗi (error / 오류) goals.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **25. Optional stopping and repeated peeking can inflate kiểu (type / 타입) I lỗi (error / 오류)** tiếp nhận điểm tựa từ **24. Multiple testing creates false discovery pressure** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Power phân tích (analysis / 분석) before experiment** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Optional stopping and repeated peeking can inflate kiểu (type / 타입) I lỗi (error / 오류)

If nhóm (team / 팀) repeatedly checks p-value after every new người dùng (user / 사용자) and stops when `p<0.05`, ordinary fixed-sample kiểm thử (test / 테스트) calibration no longer holds.

Sequential testing requires sequentially valid methods or alpha-spending designs.

A/B testing platforms need tường minh (explicit / 명시적) treatment of repeated looks.

> **Chuyển mạch:** Trong **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **26. Power phân tích (analysis / 분석) before experiment** tiếp nhận điểm tựa từ **25. Optional stopping and repeated peeking can inflate kiểu (type / 타입) I lỗi (error / 오류)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. A/B kiểm thử (test / 테스트) for proportions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Power phân tích (analysis / 분석) before experiment

Before collecting dữ liệu (data / 데이터), choose:

```text
minimum effect of interest
noise/baseline rate
α
required power
```

Then calculate cỡ mẫu (sample size / 표본 크기).

This forces experimental thiết kế (design / 설계) to encode practical significance before results are known.

> **Chuyển mạch:** Ở chặng này của **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **27. A/B kiểm thử (test / 테스트) for proportions** tiếp nhận điểm tựa từ **26. Power phân tích (analysis / 분석) before experiment** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Randomization supports nhân quả (causal / 인과적) identification** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. A/B kiểm thử (test / 테스트) for proportions

Suppose điều khiển (control / 제어) conversion `p_A`, treatment `p_B`.

Estimate difference:

```math
\hat\Delta=\hat p_B-\hat p_A.
```

Tiêu chuẩn (standard / 표준) lỗi (error / 오류) approximately:

```math
SE(\hat\Delta)
\approx
\sqrt{
\frac{\hat p_A(1-\hat p_A)}{n_A}
+
\frac{\hat p_B(1-\hat p_B)}{n_B}
}.
```

CI for difference gives both direction and plausible magnitude.

Nghiệp vụ (business / 비즈니스) quyết định (decision / 결정) should consider expected giá trị (value / 값)/chi phí (cost / 비용), not only significance.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **28. Randomization supports nhân quả (causal / 인과적) identification** tiếp nhận điểm tựa từ **27. A/B kiểm thử (test / 테스트) for proportions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Observational adjustment requires stronger các giả định (assumptions / 가정들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Randomization supports nhân quả (causal / 인과적) identification

Random assignment makes treatment independent of pre-treatment confounders **in expectation**.

This supports nhân quả (causal / 인과적) comparison between groups if:

- assignment implemented correctly;
- interference limited per thiết kế (design / 설계) các giả định (assumptions / 가정들);
- attrition/noncompliance handled;
- kết quả (outcome / 결과) đo lường (measurement / 측정) comparable.

Randomization is thiết kế (design / 설계) công cụ (tool / 도구), not magic aftercare.

> **Chuyển mạch:** Trong **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **29. Observational adjustment requires stronger các giả định (assumptions / 가정들)** tiếp nhận điểm tựa từ **28. Randomization supports nhân quả (causal / 인과적) identification** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. Clustered dữ liệu (data / 데이터) need clustered bất định (uncertainty / 불확실성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Observational adjustment requires stronger các giả định (assumptions / 가정들)

Regression/điều khiển (control / 제어) can adjust measured confounders.

But unmeasured confounding remains possible.

No statistical kiểm thử (test / 테스트) can reconstruct randomization from nothing without nhân quả (causal / 인과적) các giả định (assumptions / 가정들).

Suy luận (inference / 추론) precision and nhân quả (causal / 인과적) identification are separate dimensions.

> **Chuyển mạch:** Ở chặng này của **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **29. Observational adjustment requires stronger các giả định (assumptions / 가정들)** nêu điều cần giải thích; **30. Clustered dữ liệu (data / 데이터) need clustered bất định (uncertainty / 불확실성)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **31. thời gian (time / 시간) series invalidate naive iid intervals** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Clustered dữ liệu (data / 데이터) need clustered bất định (uncertainty / 불확실성)

If users are grouped by company/school/thiết bị (device / 장치) household and outcomes correlated within groups, treating every row independent underestimates bất định (uncertainty / 불확실성).

Methods include cluster-robust SE, multilevel các mô hình (models / 모델들) or cluster randomization.

Đơn vị (unit / 단위) of randomization and đơn vị (unit / 단위) of phân tích (analysis / 분석) must align.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **30. Clustered dữ liệu (data / 데이터) need clustered bất định (uncertainty / 불확실성)** nêu điều cần giải thích; **31. thời gian (time / 시간) series invalidate naive iid intervals** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **32. Missing dữ liệu (data / 데이터) cơ chế (mechanism / 메커니즘) matters** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. thời gian (time / 시간) series invalidate naive iid intervals

Daily metrics often autocorrelated.

If

```math
X_t
```

correlated over thời gian (time / 시간), ordinary `\sigma/\sqrt n` can understate tiêu chuẩn (standard / 표준) lỗi (error / 오류).

Need time-series/blocked bootstrap/HAC-style methods depending setup.

Raw row count is not effective independent thông tin (information / 정보) count.

> **Chuyển mạch:** Trong **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **31. thời gian (time / 시간) series invalidate naive iid intervals** nêu điều cần giải thích; **32. Missing dữ liệu (data / 데이터) cơ chế (mechanism / 메커니즘) matters** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **33. sai số đo lường (measurement error / 측정 오차) can attenuate relationships** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Missing dữ liệu (data / 데이터) cơ chế (mechanism / 메커니즘) matters

Missing completely at random, missing at random and missing not at random imply different identification các giả định (assumptions / 가정들).

Dropping missing rows can độ lệch (bias / 편향) estimates if missingness depends on outcome-related variables.

“Clean dữ liệu (data / 데이터)” via deletion can silently thay đổi (change / 변경) mục tiêu (target / 대상) population.

> **Chuyển mạch:** Ở chặng này của **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, cơ chế trong **32. Missing dữ liệu (data / 데이터) cơ chế (mechanism / 메커니즘) matters** cần được kiểm chứng bằng dấu vết cụ thể; **33. sai số đo lường (measurement error / 측정 오차) can attenuate relationships** đưa dữ liệu và nguồn vào đúng điểm đó. Từ đây, **34. Robustness: mean-based suy luận (inference / 추론) can be sensitive to tails** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. sai số đo lường (measurement error / 측정 오차) can attenuate relationships

If predictor measured with noise, naive regression slope often biased toward zero under classical measurement-error setup.

More mẫu (sample / 표본) does not remove systematic sai số đo lường (measurement error / 측정 오차).

Statistics depends on đo lường (measurement / 측정) chất lượng (quality / 품질) upstream.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **33. sai số đo lường (measurement error / 측정 오차) can attenuate relationships** nêu điều cần giải thích; **34. Robustness: mean-based suy luận (inference / 추론) can be sensitive to tails** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **35. Bayesian credible interval answers a different xác suất (probability / 확률) question** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. Robustness: mean-based suy luận (inference / 추론) can be sensitive to tails

Heavy-tailed/outlier-prone dữ liệu (data / 데이터) can make mẫu (sample / 표본) mean unstable.

Alternatives include:

- median;
- trimmed mean;
- robust M-estimators;
- transformed quy mô (scale / 규모);
- bootstrap with caution.

Estimator should match phân phối (distribution / 분포) and mất mát (loss / 손실), not tradition.

> **Chuyển mạch:** Trong **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **35. Bayesian credible interval answers a different xác suất (probability / 확률) question** tiếp nhận điểm tựa từ **34. Robustness: mean-based suy luận (inference / 추론) can be sensitive to tails** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **36. Confidence chuỗi (sequence / 시퀀스) for anytime-valid suy luận (inference / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. Bayesian credible interval answers a different xác suất (probability / 확률) question

Bayesian posterior interval may satisfy:

```math
P(\theta\in[L,U]\mid D)=0.95
```

under prior + likelihood mô hình (model / 모델).

Frequentist confidence interval has repeated-sampling coverage interpretation.

Both can produce numerically similar intervals in some regimes but philosophical/technical conditioning differs.

> **Chuyển mạch:** Ở chặng này của **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **35. Bayesian credible interval answers a different xác suất (probability / 확률) question** xác định đầu vào; **36. Confidence chuỗi (sequence / 시퀀스) for anytime-valid suy luận (inference / 추론)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **37. Reproducibility and pre-registration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. Confidence chuỗi (sequence / 시퀀스) for anytime-valid suy luận (inference / 추론)

A confidence chuỗi (sequence / 시퀀스) is a chuỗi (sequence / 시퀀스) of intervals designed so that coverage holds simultaneously over thời gian (time / 시간) under conditions:

```text
valid even when stopping time is data-dependent
```

This is useful for continuously monitored online experiments.

It solves a different bài toán (problem / 문제) from fixed-horizon CI.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **36. Confidence chuỗi (sequence / 시퀀스) for anytime-valid suy luận (inference / 추론)** xác định đầu vào; **37. Reproducibility and pre-registration** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **38. Confidence interval as inversion of hypothesis tests** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. Reproducibility and pre-registration

Research/sản phẩm (product / 제품) phân tích (analysis / 분석) becomes biased if teams try many metrics, filters and windows then report only favorable kết quả (result / 결과).

Pre-specifying primary chỉ số (metric / 지표)/hypothesis and phân tích (analysis / 분석) plan reduces researcher degrees of freedom.

Multiple testing correction alone does not solve every selective reporting issue.

> **Chuyển mạch:** Trong **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **38. Confidence interval as inversion of hypothesis tests** tiếp nhận điểm tựa từ **37. Reproducibility and pre-registration** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **39. Likelihood viewpoint connects estimation and testing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. Confidence interval as inversion of hypothesis tests

For many tiêu chuẩn (standard / 표준) procedures, a `1-\alpha` CI contains exactly parameter values not rejected by corresponding two-sided level-`\alpha` tests.

This shows intervals and tests are two views of the same inferential hình học (geometry / 기하학):

```text
CI → plausible parameter region under procedure
Test → evaluate one parameter value against data
```

> **Chuyển mạch:** Ở chặng này của **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **39. Likelihood viewpoint connects estimation and testing** tiếp nhận điểm tựa từ **38. Confidence interval as inversion of hypothesis tests** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **40. Worked example: why cỡ mẫu (sample size / 표본 크기) cannot repair độ lệch (bias / 편향)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 39. Likelihood viewpoint connects estimation and testing

Likelihood:

```math
L(\theta)=p(D\mid\theta).
```

MLE chooses parameter maximizing likelihood.

Likelihood-ratio tests compare how well constrained vs unconstrained parameter spaces explain dữ liệu (data / 데이터).

This creates a cầu nối (bridge / 브리지) to the thư viện (library / 라이브러리) chapter on MLE/MAP/mô hình (model / 모델) selection.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **39. Likelihood viewpoint connects estimation and testing** cho ta quy tắc; **40. Worked example: why cỡ mẫu (sample size / 표본 크기) cannot repair độ lệch (bias / 편향)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **41. Worked example: practical threshold** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 40. Worked example: why cỡ mẫu (sample size / 표본 크기) cannot repair độ lệch (bias / 편향)

Suppose true population approval is 50%, but sampling cơ chế (mechanism / 메커니즘) over-represents a subgroup whose approval is 70%.

As `n` grows, mẫu (sample / 표본) estimate may converge tightly around, say, 60% under biased mixture.

Tiêu chuẩn (standard / 표준) lỗi (error / 오류) shrinks:

```math
SE\to0
```

while độ lệch (bias / 편향) remains about 10 percentage points.

Large dữ liệu (data / 데이터) makes wrong estimate more confidently wrong.

> **Chuyển mạch:** Trong **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **40. Worked example: why cỡ mẫu (sample size / 표본 크기) cannot repair độ lệch (bias / 편향)** cho ta quy tắc; **41. Worked example: practical threshold** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **42. AI mô hình (model / 모델) evaluation liên kết (connection / 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 41. Worked example: practical threshold

Suppose new tính năng (feature / 기능) increases revenue/người dùng (user / 사용자) estimate by:

```text
+10 KRW/user/day
```

95% CI:

```text
[-2, +22] KRW
```

If rollout chi phí (cost / 비용) equivalent to +15 KRW/người dùng (user / 사용자)/day required to break even, merely rejecting zero is not right quyết định (decision / 결정) criterion.

Quyết định (decision / 결정) needs xác suất (probability / 확률)/bất định (uncertainty / 불확실성) relative to nghiệp vụ (business / 비즈니스) threshold `15`, not just null `0`.

> **Chuyển mạch:** Ở chặng này của **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **41. Worked example: practical threshold** cho ta quy tắc; **42. AI mô hình (model / 모델) evaluation liên kết (connection / 연결)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **43. Finance liên kết (connection / 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 42. AI mô hình (model / 모델) evaluation liên kết (connection / 연결)

Accuracy on kiểm thử (test / 테스트) set is an estimate.

It has sampling bất định (uncertainty / 불확실성).

If benchmark has 100 samples, 1% difference may be one item.

Repeated mô hình (model / 모델) selection on same kiểm thử (test / 테스트) set causes adaptive overfitting.

Need held-out kiểm tra hợp lệ (validation / 검증)/kiểm thử (test / 테스트) discipline, confidence intervals or resampling, and multiple-comparison awareness.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **43. Finance liên kết (connection / 연결)** tiếp nhận điểm tựa từ **42. AI mô hình (model / 모델) evaluation liên kết (connection / 연결)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **44. Practical suy luận (inference / 추론) checklist** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 43. Finance liên kết (connection / 연결)

Backtest Sharpe, mean return or alpha estimates have bất định (uncertainty / 불확실성) and strong thời gian (time / 시간) dependence.

Multiple chiến lược (strategy / 전략) searches create data-snooping độ lệch (bias / 편향).

Regime changes violate iid các giả định (assumptions / 가정들).

A tiny p-value from naive mô hình (model / 모델) can be meaningless if serial correlation, selection and nonstationarity are ignored.

> **Chuyển mạch:** Trong **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **44. Practical suy luận (inference / 추론) checklist** tiếp nhận điểm tựa từ **43. Finance liên kết (connection / 연결)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 44. Practical suy luận (inference / 추론) checklist

Before trusting kết quả (result / 결과), ask:

```text
Target population/process là gì?
Sampling/randomization mechanism là gì?
Estimator đang estimate quantity nào?
Independence assumptions có hợp lý?
Standard error tính theo design nào?
Effect size có practical meaning gì?
CI interpretation đúng framework chưa?
P-value có bị multiple testing/optional stopping ảnh hưởng?
Missingness/attrition/measurement error thế nào?
Claim là associational hay causal?
```

> **Chuyển mạch:** Ở chặng này của **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, sau nội dung của **44. Practical suy luận (inference / 추론) checklist**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Phần kết nối đặt sampling và uncertainty cạnh experiment, regression và decision. Hãy phân biệt uncertainty do mẫu với bias do thiết kế trước khi diễn giải khoảng tin cậy.

```text
probability
→ LLN / CLT
→ sampling distributions
→ standard errors
→ estimators
→ confidence intervals
→ hypothesis tests
→ power / experimental design
→ A/B testing
→ regression / likelihood
→ Bayesian intervals
→ causal inference
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Liên kết kiến thức (knowledge connection / 지식 연결)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Statistical suy luận (inference / 추론) is **bất định (uncertainty / 불확실성) accounting for a sampling tiến trình (process / 프로세스)**. A mẫu (sample / 표본) does not magically reveal a population. We need a thiết kế (design / 설계) that connects observations to the mục tiêu (target / 대상), an estimator with known hành vi (behavior / 동작), and a procedure that quantifies bất định (uncertainty / 불확실성) under tường minh (explicit / 명시적) các giả định (assumptions / 가정들). Precision without identification is false confidence.

> **Chuyển mạch:** Trong **Lấy mẫu, ước lượng, confidence interval và hypothesis testing: suy luận (inference / 추론) từ dữ liệu hữu hạn**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

P-value is not `P(H0 true | data)`. `p>0.05` does not prove no effect. 95% confidence does not mean 95% posterior probability in frequentist interpretation. Huge `n` cannot fix systematic bias. More rows do not equal more independent information. Statistical significance is not practical significance or causality. Repeated peeking/multiple metrics can destroy nominal error rates. Narrow intervals can be precisely wrong if design or measurement is biased.

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
