# 05 — Econometrics

Econometrics nối economic questions với data bằng measurement, probability, statistical inference và causal identification. Module này không coi regression là điểm bắt đầu. Thứ tự canonical là: xác định **data + estimand + counterfactual** trước, sau đó mới chọn estimator phù hợp với source of variation và dependence structure.

## Thứ tự học canonical

1. [Measurement, Data & Estimands](./00_measurement_data_and_estimands.md) — units/population, sampling/selection, missingness, measurement error, descriptive vs causal targets, potential outcomes, ATE/ATT/LATE, DAG/collider/bad controls và internal/external validity.
2. [Regression, Prediction & Inference](./01_regression_prediction_and_inference.md) — conditional expectation, OLS projection, multiple regression/FWL, omitted-variable bias, overlap, functional form, heteroskedastic/clustered inference, testing và prediction-v-causality boundary.
3. [Causal Inference, Experiments & Selection](./02_causal_inference_experiments_and_selection.md) — randomization, ITT/noncompliance, attrition/spillovers, power, matching, propensity score/IPW, doubly robust estimation, natural experiments và scale-up.
4. [Endogeneity, IV & RDD](./03_endogeneity_instrumental_variables_and_rdd.md) — omitted variables/simultaneity/reverse causality, relevance/exclusion, weak instruments, LATE, sharp/fuzzy RDD, manipulation, bandwidth và local interpretation.
5. [Panel, Fixed Effects & Difference-in-Differences](./04_panel_fixed_effects_and_difference_in_differences.md) — within variation, unit/time FE, parallel trends, event studies, staggered adoption, heterogeneous effects, synthetic control và clustered inference.
6. [Time Series, Forecasting & Macro Identification](./05_time_series_forecasting_and_macro_identification.md) — stationarity, unit roots, AR/MA, cointegration, forecasts, structural breaks, VAR/IRF, SVAR/local projections, policy endogeneity và real-time data.
7. [Robustness, External Validity & Research Workflow](./06_robustness_external_validity_and_research_workflow.md) — threat-specific robustness, falsification, sensitivity/bounds, multiple testing, reproducibility/replication, transportability, scale-up, economic significance và paper-reading workflow.

## Learning spine

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

Tool choice comes after design. `OLS`, `IV`, `DiD`, `RDD` hay `VAR` không phải labels cho sophistication; chúng answer different questions under different assumptions.

## Ba mục tiêu phải tách riêng

### Description

Mô tả distribution, association, conditional means hoặc historical patterns. Không cần mọi descriptive question trở thành causal question.

### Prediction

Dự báo outcome mới với out-of-sample performance. Prediction model có thể dùng variables không causal nếu available at prediction time và stable enough.

### Causal inference

Estimate effect của intervention/treatment. Cần credible counterfactual/source of variation; predictive accuracy alone không đủ.

Một model có thể excellent ở một mục tiêu và weak ở mục tiêu khác.

## Evidence discipline

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

## Boundary với Mathematics

[Mathematics](../../mathematics/README.md) cung cấp probability, distributions, expectation, variance, covariance, linear algebra và statistics nền. Econometrics dùng chúng để answer economic questions có endogeneity, selection, treatment assignment, panel/time dependence và institutional variation.

Nếu người học chưa hiểu expectation/variance/covariance và sampling distribution, nên quay lại Mathematics trước khi học inference sâu.

## Boundary với Micro/Game Theory/Macro

Theory xác định mechanism và target parameters:

- Micro cần elasticity, welfare/treatment effects, incentive responses;
- Market Structure cần demand/markup/entry/merger effects;
- Macro cần policy shocks, multipliers, Phillips dynamics, growth/productivity và crisis transmission.

Econometrics không thay thế theory. Nó kiểm tra theory/data link và xác định phần nào có thể infer causally.

## Boundary với Applied Economics

Applied Economics phải cite theory **và** identification strategy. Một labor/public/trade/development/IO chapter không được gọi một correlation là empirical support nếu chưa nói design.

Vì vậy Econometrics được triển khai trước Applied Economics trong repo dù folder numbering giữ `04 Applied`, `05 Econometrics`.

## Checklist đọc empirical claim

Hỏi theo thứ tự: unit/population; variable measurement; treatment/outcome timing; estimand; assignment/source of variation; major confounders; overlap/support; estimator assumptions; clustering/dependence; effect size + uncertainty; placebo/robustness; heterogeneity; external validity; equilibrium/scale-up effects; data/code transparency.

Nếu một claim thất bại ở bước identification, không cần bị thuyết phục bởi coefficient table phía sau.
