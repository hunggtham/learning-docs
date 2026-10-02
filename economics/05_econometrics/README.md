# 05 — Econometrics

> **Mạch đọc:** [README](./README.md) là owner của **05 — Econometrics**. Route học đi từ probability/statistics → regression và inference → causal identification → panel/time series/measurement → robustness, để mỗi kết luận nêu rõ dữ liệu, giả định và uncertainty.

Econometrics nối economic questions với dữ liệu (data / 데이터) bằng đo lường (measurement / 측정), xác suất (probability / 확률), statistical suy luận (inference / 추론) và nhân quả (causal / 인과적) identification. Mô-đun (module / 모듈) này không coi regression là điểm bắt đầu. Thứ tự chuẩn gốc (canonical / 정본) là: xác định **dữ liệu (data / 데이터) + estimand + counterfactual** trước, sau đó mới chọn estimator phù hợp với nguồn (source / 소스) of variation và dependence cấu trúc (structure / 구조).

## Thứ tự học chuẩn gốc (canonical / 정본)

1. [Measurement, Data & Estimands](./00_measurement_data_and_estimands.md) — units/population, sampling/selection, missingness, sai số đo lường (measurement error / 측정 오차), descriptive vs nhân quả (causal / 인과적) targets, potential outcomes, ATE/ATT/LATE, DAG/collider/bad controls và nội bộ (internal / 내부)/bên ngoài (external / 외부) validity.
2. [Regression, Prediction & Inference](./01_regression_prediction_and_inference.md) — conditional expectation, OLS projection, multiple regression/FWL, omitted-variable độ lệch (bias / 편향), overlap, functional form, heteroskedastic/clustered suy luận (inference / 추론), testing và prediction-v-causality ranh giới (boundary / 경계).
3. [Causal Inference, Experiments & Selection](./02_causal_inference_experiments_and_selection.md) — randomization, ITT/noncompliance, attrition/spillovers, power, matching, propensity score/IPW, doubly robust estimation, natural experiments và scale-up.
4. [Endogeneity, IV & RDD](./03_endogeneity_instrumental_variables_and_rdd.md) — omitted variables/simultaneity/reverse causality, relevance/exclusion, weak instruments, LATE, sharp/fuzzy RDD, manipulation, bandwidth và cục bộ (local / 로컬) interpretation.
5. [Panel, Fixed Effects & Difference-in-Differences](./04_panel_fixed_effects_and_difference_in_differences.md) — within variation, đơn vị (unit / 단위)/thời gian (time / 시간) FE, parallel trends, sự kiện (event / 이벤트) studies, staggered adoption, heterogeneous effects, synthetic điều khiển (control / 제어) và clustered suy luận (inference / 추론).
6. [Time Series, Forecasting & Macro Identification](./05_time_series_forecasting_and_macro_identification.md) — stationarity, đơn vị (unit / 단위) roots, AR/MA, cointegration, forecasts, structural breaks, VAR/IRF, SVAR/cục bộ (local / 로컬) projections, chính sách (policy / 정책) endogeneity và real-time dữ liệu (data / 데이터).
7. [Robustness, External Validity & Research Workflow](./06_robustness_external_validity_and_research_workflow.md) — threat-specific robustness, falsification, sensitivity/bounds, multiple testing, reproducibility/replication, transportability, scale-up, economic significance và paper-reading workflow.

> **Chuyển mạch:** Econometrics spine tách measurement, prediction và causal inference; canonical order đi từ estimand/data đến identification, estimation, robustness và workflow.

## Trục học (learning spine / 학습 축)

```text
Economic question
→ measurement + sample
→ estimand / counterfactual
→ source of variation
→ estimator
→ design-consistent inference
→ falsification / robustness
→ external validity
→ economic interpretation
```

Công cụ (tool / 도구) choice comes after thiết kế (design / 설계). `OLS`, `IV`, `DiD`, `RDD` hay `VAR` không phải labels cho sophistication; chúng answer different questions under different các giả định (assumptions / 가정들).

> **Chuyển mạch:** Measurement, prediction and causal inference require different estimands and evidence; the econometrics spine makes that separation explicit before methods are chosen.

## Ba mục tiêu phải tách riêng

### Description

Mô tả phân phối (distribution / 분포), association, conditional means hoặc historical patterns. Không cần mọi descriptive question trở thành nhân quả (causal / 인과적) question.

### Prediction

Dự báo kết quả (outcome / 결과) mới với out-of-sample hiệu năng (performance / 성능). Prediction mô hình (model / 모델) có thể dùng variables không nhân quả (causal / 인과적) nếu available at prediction thời gian (time / 시간) và stable enough.

### Nhân quả (causal / 인과적) suy luận (inference / 추론)

Estimate tác động (effect / 효과) của intervention/treatment. Cần credible counterfactual/nguồn (source / 소스) of variation; predictive accuracy alone không đủ.

Một mô hình (model / 모델) có thể excellent ở một mục tiêu và weak ở mục tiêu khác.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **05 — Econometrics**, **Ba mục tiêu phải tách riêng** nêu điều cần giải thích; **Bằng chứng (evidence / 증거) discipline** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Ranh giới (boundary / 경계) với Mathematics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bằng chứng (evidence / 증거) discipline

Mọi empirical claim nên trả lời được:

```text
What is measured?
What is the estimand?
Where does identifying variation come from?
Why is the counterfactual credible?
What uncertainty is quantified?
What assumption is not testable directly?
How local is the result?
```

`p < 0.05`, high `R²`, large N hoặc many controls không thay thế identification.

> **Chuyển mạch:** Trong **05 — Econometrics**, **Bằng chứng (evidence / 증거) discipline** đã nêu tiêu chí phân biệt, còn **Ranh giới (boundary / 경계) với Mathematics** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Ranh giới (boundary / 경계) với Micro/Game Lý thuyết (theory / 이론)/Macro** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ranh giới (boundary / 경계) với Mathematics

[Mathematics](../../mathematics/README.md) cung cấp xác suất (probability / 확률), distributions, expectation, variance, covariance, tuyến tính (linear / 선형) algebra và statistics nền. Econometrics dùng chúng để answer economic questions có endogeneity, selection, treatment assignment, panel/thời gian (time / 시간) dependence và institutional variation.

Nếu người học chưa hiểu expectation/variance/covariance và sampling phân phối (distribution / 분포), nên quay lại Mathematics trước khi học suy luận (inference / 추론) sâu.

> **Chuyển mạch:** Ở chặng này của **05 — Econometrics**, **Ranh giới (boundary / 경계) với Mathematics** đã nêu tiêu chí phân biệt, còn **Ranh giới (boundary / 경계) với Micro/Game Lý thuyết (theory / 이론)/Macro** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Ranh giới (boundary / 경계) với Applied Economics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ranh giới (boundary / 경계) với Micro/Game Lý thuyết (theory / 이론)/Macro

Lý thuyết (theory / 이론) xác định cơ chế (mechanism / 메커니즘) và mục tiêu (target / 대상) parameters:

- Micro cần elasticity, welfare/treatment effects, incentive responses;
- Thị trường (market / 시장) Cấu trúc (structure / 구조) cần demand/markup/entry/merger effects;
- Macro cần chính sách (policy / 정책) shocks, multipliers, Phillips dynamics, growth/productivity và crisis transmission.

Econometrics không thay thế lý thuyết (theory / 이론). Nó kiểm tra lý thuyết (theory / 이론)/dữ liệu (data / 데이터) link và xác định phần nào có thể infer causally.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **05 — Econometrics**, **Ranh giới (boundary / 경계) với Micro/Game Lý thuyết (theory / 이론)/Macro** đã nêu tiêu chí phân biệt, còn **Ranh giới (boundary / 경계) với Applied Economics** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Checklist đọc empirical claim** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ranh giới (boundary / 경계) với Applied Economics

Applied Economics phải cite lý thuyết (theory / 이론) **và** identification chiến lược (strategy / 전략). Một labor/công khai (public / 공개)/trade/development/IO chapter không được gọi một correlation là empirical hỗ trợ (support / 지원) nếu chưa nói thiết kế (design / 설계).

Vì vậy Econometrics được triển khai trước Applied Economics trong repo dù folder numbering giữ `04 Applied`, `05 Econometrics`.

> **Chuyển mạch:** Trong **05 — Econometrics**, **Ranh giới (boundary / 경계) với Applied Economics** đã nêu tiêu chí phân biệt, còn **Checklist đọc empirical claim** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Checklist đọc empirical claim

Hỏi theo thứ tự: đơn vị (unit / 단위)/population; variable đo lường (measurement / 측정); treatment/kết quả (outcome / 결과) timing; estimand; assignment/nguồn (source / 소스) of variation; major confounders; overlap/hỗ trợ (support / 지원); estimator các giả định (assumptions / 가정들); clustering/dependence; tác động (effect / 효과) kích thước (size / 크기) + bất định (uncertainty / 불확실성); placebo/robustness; heterogeneity; bên ngoài (external / 외부) validity; equilibrium/scale-up effects; dữ liệu (data / 데이터)/mã (code / 코드) transparency.

Nếu một claim thất bại ở bước identification, không cần bị thuyết phục bởi coefficient bảng (table / 테이블) phía sau.

> **Bàn giao:** Sau **Checklist đọc empirical claim**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
