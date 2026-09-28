# Robustness, bên ngoài (external / 외부) Validity & Research Workflow — Từ estimate đến kết luận đáng tin

> **Mạch đọc:** Đặt **Robustness, bên ngoài (external / 외부) Validity & Research Workflow — Từ estimate đến kết luận đáng tin** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Identification trước robustness** sang **2. Specification curve intuition**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Một econometric estimate không kết thúc phân tích (analysis / 분석). Sau điểm (point / 지점) estimate cần hỏi: kết quả (result / 결과) có phụ thuộc một specification duy nhất không, các giả định (assumptions / 가정들) nào dễ vỡ, bất định (uncertainty / 불확실성) nào chưa nằm trong tiêu chuẩn (standard / 표준) lỗi (error / 오류), và tác động (effect / 효과) có áp dụng được ngoài mẫu (sample / 표본)/ngữ cảnh (context / 맥락) hay không? Robustness không phải chạy hàng trăm regressions cho đến khi coefficient “ổn”; nó là kiểm tra có hệ thống những threats xuất phát từ thiết kế (design / 설계).

## 1. Identification trước robustness

Robustness không cứu được thiết kế (design / 설계) sai từ đầu.

Nếu instrument vi phạm exclusion, mẫu (sample / 표본) selection severe hoặc treatment timing sai, thêm controls/specifications chỉ thay hình thức.

Workflow đúng:

```text
Question
→ estimand
→ design / source of variation
→ main specification
→ design-specific threats
→ robustness / falsification
→ interpretation
```

## 2. Specification curve intuition

Một kết quả (result / 결과) có thể được estimate dưới nhiều reasonable choices: điều khiển (control / 제어) set, mẫu (sample / 표본) cửa sổ (window / 윈도우), functional form, clustering, kết quả (outcome / 결과) definition.

Specification curve/multiverse phân tích (analysis / 분석) hiển thị phân phối (distribution / 분포) of estimates across defensible specifications.

Mục tiêu là transparency, không phải đếm bao nhiêu regression significant.

## 3. Robustness phải có lý do

Mỗi robustness check nên map tới threat:

- alternative bandwidth → RDD local-fit sensitivity;
- alternative điều khiển (control / 제어) group → DiD parallel-trend concern;
- clustered SE → correlated shocks;
- alternate kết quả (outcome / 결과) definition → đo lường (measurement / 측정) sensitivity;
- leave-one-region-out → influential đơn vị (unit / 단위);
- placebo timing → anticipation/dùng chung (common / 공통) trends.

Randomly changing mô hình (model / 모델) without threat mô hình (model / 모델) tạo noise, không tạo credibility.

## 4. Falsification tests

A strong thiết kế (design / 설계) makes predictions where tác động (effect / 효과) **should not** appear.

Examples:

- pre-treatment tác động (effect / 효과) should be absent;
- ineligible group should not react;
- placebo cutoff should show no discontinuity;
- negative-control kết quả (outcome / 결과) should not thay đổi (change / 변경).

Thất bại (failure / 실패) indicates alternative explanation; passing supports but does not prove identification.

## 5. Balance tests

In randomized/RDD settings, pre-treatment covariates should be balanced in expectation or smooth across cutoff.

Do not mechanically require every covariate p-value > 0.05. With many variables, some imbalance occurs by chance; focus on magnitude/joint patterns and thiết kế (design / 설계).

## 6. Sensitivity to unobserved confounding

Observational selection-on-observables designs rely on no hidden confounding after X.

Sensitivity phân tích (analysis / 분석) asks how strong an omitted variable would need to be to explain estimate.

This turns vague “maybe omitted variables” into quantitative threat assessment, while still not proving absence of confounding.

## 7. Bounds

When điểm (point / 지점) identification requires implausibly strong các giả định (assumptions / 가정들), partial identification may provide credible bounds.

Examples: attrition bounds, worst-case missing outcomes, monotonicity-based bounds.

A wider honest interval can be more informative than a precise but fragile điểm (point / 지점) estimate.

## 8. Influence and leverage

Some observations have disproportionate influence because X is extreme or residual large.

Check leverage, influence statistics, leave-one-out/group-out estimates and dữ liệu (data / 데이터) errors.

But do not remove influential observations solely because they weaken desired kết quả (result / 결과).

## 9. Outliers

Outlier may be sai số đo lường (measurement error / 측정 오차) or genuine tail sự kiện (event / 이벤트). Treatment depends on ngữ cảnh (context / 맥락).

Winsorizing changes estimand/phân phối (distribution / 분포). Report why cutoff chosen and show raw sensitivity.

## 10. Alternative kết quả (outcome / 결과) definitions

If a concept has several valid measures, kết quả (result / 결과) should be interpreted relative to each.

Employment can be headcount, hours, payroll, formal jobs. Inflation can headline/cốt lõi (core / 핵심)/sector indices.

Consistency across measures strengthens cơ chế (mechanism / 메커니즘) only if measures capture related but distinct aspects.

## 11. Multiple hypothesis correction

If many outcomes/subgroups are primary tests, điều khiển (control / 제어) false positives using family-wise lỗi (error / 오류) or False Discovery tỷ lệ (rate / 비율) where appropriate.

Pre-specify kết quả (outcome / 결과) families; do not retroactively lời gọi (call / 호출) one significant kết quả (result / 결과) “primary”.

## 12. Publication độ lệch (bias / 편향)

Studies with significant/novel results may be more likely published. Literature can overstate effects even when each paper uses conventional suy luận (inference / 추론).

Meta-analysis should inspect heterogeneity, small-study effects and thiết kế (design / 설계) chất lượng (quality / 품질), not only pooled mean.

## 13. P-hacking and researcher degrees of freedom

Flexible choices after seeing dữ liệu (data / 데이터) can generate low p-values without true tác động (effect / 효과).

Defenses include preregistration, pre-analysis plans, registered reports, mã (code / 코드)/dữ liệu (data / 데이터) transparency and distinction confirmatory vs exploratory phân tích (analysis / 분석).

## 14. Reproducibility

Computational reproducibility means same dữ liệu (data / 데이터)/mã (code / 코드) regenerates kết quả (result / 결과).

It requires versioned dữ liệu (data / 데이터), deterministic transformations where possible, môi trường (environment / 환경) documentation, seeds and clear chuỗi xử lý (pipeline / 파이프라인).

Reproducible does not mean causally valid; it means phân tích (analysis / 분석) can be inspected and rerun.

## 15. Replication

Replication asks whether finding survives new mẫu (sample / 표본)/dữ liệu (data / 데이터)/thiết kế (design / 설계).

Direct replication repeats closely; conceptual replication tests same cơ chế (mechanism / 메커니즘) in different setting.

Thất bại (failure / 실패) to replicate can reflect original false positive, contextual heterogeneity, hiện thực (implementation / 구현) differences or underpowered replication.

## 16. bên ngoài (external / 외부) validity

Tác động (effect / 효과) can vary by:

```text
population
institution
geography
time
baseline risk
treatment intensity
implementation quality
scale
```

Generalization requires mô hình (model / 모델) of tác động (effect / 효과) heterogeneity and comparison between study and mục tiêu (target / 대상) population.

## 17. Transportability

If treatment tác động (effect / 효과) conditional on covariates is stable, reweighting study mẫu (sample / 표본) to mục tiêu (target / 대상) covariate phân phối (distribution / 분포) can vận chuyển (transport / 전송) tác động (effect / 효과) under các giả định (assumptions / 가정들).

But unobserved tác động (effect / 효과) modifiers or institutional differences remain threats.

## 18. Scale-up effects

Small pilot may use best staff, high monitoring and no equilibrium price phản hồi (response / 응답). National quy mô (scale / 규모) can dilute chất lượng (quality / 품질), thay đổi (change / 변경) wages/rents and alter provider entry.

Quy mô (scale / 규모) is treatment phiên bản (version / 버전) thay đổi (change / 변경), not merely larger N.

## 19. General equilibrium vs partial equilibrium

Individual subsidy tác động (effect / 효과) may differ when everyone receives subsidy because thị trường (market / 시장) prices adjust.

Micro nhân quả (causal / 인과적) estimate can be internally valid but insufficient for economy-wide chính sách (policy / 정책) without equilibrium mô hình (model / 모델)/bằng chứng (evidence / 증거).

## 20. Treatment heterogeneity

Report subgroup effects when motivated by cơ chế (mechanism / 메커니즘) and sufficiently powered.

Avoid searching dozens of splits then highlighting one large coefficient. Machine-learning heterogeneity methods require honest mẫu (sample / 표본) splitting/kiểm tra hợp lệ (validation / 검증).

## 21. Distributional effects

Average treatment tác động (effect / 효과) can hide winners and losers.

Quantile treatment effects, kết quả (outcome / 결과) phân phối (distribution / 분포) or subgroup effects may be necessary when equity/rủi ro (risk / 위험) matters.

But quantile effects need careful interpretation because individuals at same quantile are not necessarily same units across counterfactual distributions.

## 22. cơ chế (mechanism / 메커니즘) bằng chứng (evidence / 증거)

A reduced-form tác động (effect / 효과) can be policy-relevant without fully proving cơ chế (mechanism / 메커니즘).

Mediator outcomes, timing patterns and heterogeneous phản hồi (response / 응답) can hỗ trợ (support / 지원) cơ chế (mechanism / 메커니즘), but post-treatment variables require care.

Distinguish:

```text
Treatment affects Y
vs.
Treatment affects Y specifically through M
```

The second claim needs additional các giả định (assumptions / 가정들)/bằng chứng (evidence / 증거).

## 23. Economic significance

Translate estimates to natural units and compare with baseline, costs and feasible alternatives.

Example:

```text
+0.1 SD test score
```

needs ngữ cảnh (context / 맥락): baseline phân phối (distribution / 분포), persistence, intervention chi phí (cost / 비용) and comparison to other programs.

## 24. Cost-effectiveness

A nhân quả (causal / 인과적) tác động (effect / 효과) is not a chính sách (policy / 정책) recommendation by itself.

Cost-effectiveness:

```text
Effect / Cost
```

helps compare interventions with same kết quả (outcome / 결과). Cost-benefit requires monetizing broader benefits/costs and phân phối (distribution / 분포) các giả định (assumptions / 가정들).

## 25. Statistical vs quyết định (decision / 결정) bất định (uncertainty / 불확실성)

Chính sách (policy / 정책) quyết định (decision / 결정) depends not only confidence interval but asymmetric costs of errors, option giá trị (value / 값), irreversibility and học tập (learning / 학습).

A small uncertain benefit may justify experiment if reversible/cheap; same bất định (uncertainty / 불확실성) may not justify irreversible costly chính sách (policy / 정책).

## 26. Bayesian interpretation

Bayesian phân tích (analysis / 분석) combines prior and likelihood to form posterior.

It can express xác suất (probability / 확률) over parameters conditional on mô hình (model / 모델)/prior, but conclusions depend on prior and mô hình (model / 모델) các giả định (assumptions / 가정들).

Bayesian credible intervals and frequentist confidence intervals answer different xác suất (probability / 확률) statements.

## 27. mô hình (model / 모델) averaging and mô hình (model / 모델) bất định (uncertainty / 불확실성)

If several plausible các mô hình (models / 모델들) exist, conditioning on one ignores mô hình (model / 모델) bất định (uncertainty / 불확실성).

Mô hình (model / 모델) averaging or scenario ranges can help, but no automatic procedure replaces substantive judgment about nhân quả (causal / 인과적) cấu trúc (structure / 구조).

## 28. Prediction calibration

For predictive các mô hình (models / 모델들), check calibration, discrimination and out-of-sample stability.

A mô hình (model / 모델) can rank rủi ro (risk / 위험) well but systematically overpredict levels; calibration matters for decisions.

## 29. phân phối (distribution / 분포) shift

Mô hình (model / 모델) trained under one regime may thất bại (fail / 실패) after technology, chính sách (policy / 정책) or hành vi (behavior / 동작) changes.

Monitor covariate shift, concept drift and structural breaks. Historical backtest is not guarantee under new regime.

## 30. Transparent reporting

A credible report states:

```text
estimand
sample/population
assignment/design
main assumptions
estimate + uncertainty
specification choices
robustness/falsification
heterogeneity
external-validity limits
data/code provenance
```

Do not hide null results or inconvenient specifications.

## 31. Research workflow

A disciplined workflow can be:

1. define economic question and estimand;
2. draw nhân quả (causal / 인과적) cấu trúc (structure / 구조) / institutional timeline;
3. inspect đo lường (measurement / 측정) and mẫu (sample / 표본) construction;
4. identify nguồn (source / 소스) of variation;
5. ghi (write / 쓰기) main specification before kết quả (outcome / 결과) hunting;
6. inspect raw/descriptive dữ liệu (data / 데이터);
7. estimate main tác động (effect / 효과) with design-consistent suy luận (inference / 추론);
8. run threat-specific robustness/falsification;
9. examine heterogeneity/cơ chế (mechanism / 메커니즘) carefully;
10. translate tác động (effect / 효과) into economic magnitude;
11. trạng thái (state / 상태) external-validity and chính sách (policy / 정책) limits;
12. gói (package / 패키지) reproducible mã (code / 코드)/dữ liệu (data / 데이터) documentation.

## 32. Reading a paper efficiently

Khi đọc empirical paper, không bắt đầu từ coefficient bảng (table / 테이블). Đọc theo thứ tự:

```text
Question
Institution / assignment mechanism
Data construction
Estimand
Identification assumptions
Main graph/descriptive evidence
Estimate
Threats / robustness
External validity
```

Nếu thiết kế (design / 설계) không credible, precision của bảng (table / 테이블) phía sau không cứu được conclusion.

## 33. Red flags

Các red flags mạnh gồm:

- nhân quả (causal / 인과적) ngôn ngữ (language / 언어) nhưng không có assignment/counterfactual argument;
- many controls được mô tả như proof of causality;
- treatment timing mơ hồ;
- no raw trends around DiD/RDD thiết kế (design / 설계);
- IV without exclusion story;
- clustered treatment nhưng iid SE;
- only significant outcomes reported;
- kết quả (result / 결과) depends one narrow specification without justification;
- extrapolation far beyond hỗ trợ (support / 지원)/mẫu (sample / 표본);
- chính sách (policy / 정책) recommendation không discuss costs/equilibrium/phân phối (distribution / 분포).

## 34. thất bại (failure / 실패) modes

Sai lầm thứ nhất là equate robustness with many regressions.

Sai lầm thứ hai là let robustness replace identification.

Sai lầm thứ ba là report only tiêu chuẩn (standard / 표준) lỗi (error / 오류) and ignore mô hình (model / 모델)/thiết kế (design / 설계) bất định (uncertainty / 불확실성).

Sai lầm thứ tư là generalize cục bộ (local / 로컬)/RCT tác động (effect / 효과) mechanically to national quy mô (scale / 규모).

Sai lầm thứ năm là infer cơ chế (mechanism / 메커니즘) from mediator correlation.

Sai lầm thứ sáu là turn nhân quả (causal / 인과적) estimate directly into chính sách (policy / 정책) recommendation without costs/trade-offs.

## 35. mô hình tư duy (mental model / 사고 모델)

Trước khi tin một empirical conclusion, hãy hỏi:

1. Estimand và counterfactual có rõ không?
2. nguồn (source / 소스) of variation thật sự là gì?
3. giả định (assumption / 가정) yếu nhất nằm ở đâu?
4. Robustness checks có mục tiêu (target / 대상) đúng threats không?
5. kết quả (result / 결과) có driven bởi vài observations/groups không?
6. Multiple testing/specification tìm kiếm (search / 검색) được xử lý thế nào?
7. tác động (effect / 효과) kích thước (size / 크기) economic meaningful không?
8. cơ chế (mechanism / 메커니즘) được identified hay chỉ suggested?
9. mẫu (sample / 표본) tác động (effect / 효과) có vận chuyển (transport / 전송)/quy mô (scale / 규모) được không?
10. dữ liệu (data / 데이터)/mã (code / 코드)/kết quả (result / 결과) có reproducible và transparent không?

Econometrics không phải toolkit để làm coefficient “đẹp”. Nó là discipline buộc economic claim phải nói rõ đo lường (measurement / 측정), counterfactual, nguồn (source / 소스) of variation, bất định (uncertainty / 불확실성) và phạm vi kết luận. Với foundation này, Applied Economics có thể được xây trên cả lý thuyết (theory / 이론) lẫn empirical identification thay vì trường hợp (case / 사례) narrative.

> **Bàn giao:** Sau **35. mô hình tư duy (mental model / 사고 모델)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 measurement data and estimands](./00_measurement_data_and_estimands.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
