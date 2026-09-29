# Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection

Nhân quả (causal / 인과적) suy luận (inference / 추론) hỏi một câu rất cụ thể: **kết quả (outcome / 결과) sẽ khác thế nào nếu treatment thay đổi, trong khi counterfactual relevant được xây dựng đáng tin?** Randomized experiment là benchmark vì assignment cơ chế (mechanism / 메커니즘) có thể làm treatment independent of potential outcomes. Observational methods cố tái tạo một phần lô-gic (logic / 논리) đó bằng các giả định (assumptions / 가정들) và institutional variation.

## 1. Fundamental bài toán (problem / 문제) of nhân quả (causal / 인과적) suy luận (inference / 추론)

Mỗi đơn vị (unit / 단위) có potential outcomes:

```text
Y_i(1), Y_i(0)
```

Nhưng chỉ quan sát:

```text
Y_i = D_iY_i(1) + (1−D_i)Y_i(0)
```

Nhân quả (causal / 인과적) tác động (effect / 효과) của individual không directly observable. Ta cần comparison group đại diện cho missing potential kết quả (outcome / 결과).

## 2. Selection độ lệch (bias / 편향) decomposition

Naive difference:

```text
E[Y | D=1] − E[Y | D=0]
```

có thể decomposed thành treatment tác động (effect / 효과) plus selection difference.

Treated group thường khác untreated group trước treatment. Wage difference giữa college graduates và non-graduates không chỉ là schooling tác động (effect / 효과); ability, family background và preferences cùng influence selection.

## 3. Random assignment

Nếu treatment randomly assigned:

```text
D ⟂ {Y(1), Y(0)}
```

thì untreated outcomes of điều khiển (control / 제어) group provide unbiased counterfactual on average.

Randomization không làm groups identical trong từng mẫu (sample / 표본); nó làm imbalance stochastic và quantifiable.

## 4. Randomization suy luận (inference / 추론)

Under sharp null of no treatment tác động (effect / 효과) for every đơn vị (unit / 단위), treatment labels có thể được permuted according to assignment cơ chế (mechanism / 메커니즘) để derive chính xác (exact / 정확한)/randomization phân phối (distribution / 분포).

This emphasizes thiết kế (design / 설계) rather than asymptotic regression các giả định (assumptions / 가정들).

## 5. Intent-to-Treat

Intent-to-Treat (ITT) compares outcomes by assigned treatment, regardless of compliance:

```text
ITT = E[Y | Z=1] − E[Y | Z=0]
```

where `Z` is assignment.

ITT answers tác động (effect / 효과) of offering/assigning treatment under real compliance hành vi (behavior / 동작) and preserves randomization.

## 6. Treatment-on-the-Treated and noncompliance

If assigned participants do not all take treatment, comparing actual takers vs non-takers reintroduces selection.

Random assignment can be used as instrument for actual treatment under additional các giả định (assumptions / 가정들), leading to LATE for compliers.

## 7. Attrition

Randomization at baseline does not protect against differential attrition after assignment.

If treated low-outcome units drop out more often, observed treatment mean becomes biased.

Report attrition by arm, reasons, bounds/sensitivity and use administrative follow-up where possible.

## 8. Spillovers and contamination

Điều khiển (control / 제어) units may indirectly receive treatment through peers, markets or thông tin (information / 정보).

Then tiêu chuẩn (standard / 표준) treatment-control difference estimates tác động (effect / 효과) under contamination rather than isolated treatment.

Cluster randomization or exposure ánh xạ (mapping / 매핑) may be necessary.

## 9. Cluster randomization

Treatment may be assigned to schools, villages, hospitals or firms rather than individuals.

Effective independent cỡ mẫu (sample size / 표본 크기) is number of clusters, not raw individuals. Intra-cluster correlation reduces power.

Thiết kế (design / 설계) and SE must match assignment mức (level / 수준).

## 10. Stratification and blocking

Randomization within pre-defined blocks (region, baseline outcome, size) can improve balance and precision.

Phân tích (analysis / 분석) should account for thiết kế (design / 설계). Post-hoc subgroup creation is different from pre-randomization blocking.

## 11. Power and minimum detectable tác động (effect / 효과)

Study thiết kế (design / 설계) should ask what tác động (effect / 효과) kích thước (size / 크기) can be detected before collecting dữ liệu (data / 데이터).

Power depends on:

```text
sample size
variance
treatment share
cluster structure
baseline predictive covariates
true effect size
```

Underpowered experiment may produce noisy estimates rather than clear “no tác động (effect / 효과)”.

## 12. Baseline adjustment

Including strongly predictive pre-treatment outcomes can improve precision without threatening randomization.

But post-treatment controls should not be added mechanically.

## 13. Multiple outcomes and treatment arms

Many outcomes/arms increase false positives. Pre-specify primary outcomes and adjust families when appropriate.

Exploratory outcomes are useful if labeled exploratory.

## 14. Bên ngoài (external / 외부) validity

RCT identifies tác động (effect / 효과) for study mẫu (sample / 표본), treatment phiên bản (version / 버전) and hiện thực (implementation / 구현) ngữ cảnh (context / 맥락).

Scaling can thay đổi (change / 변경) prices, provider chất lượng (quality / 품질), equilibrium hành vi (behavior / 동작) and political responses. A village pilot may not predict national rollout.

Bên ngoài (external / 외부) validity is a separate nhân quả (causal / 인과적) question.

## 15. Hawthorne and experiment effects

Subjects/providers may thay đổi (change / 변경) hành vi (behavior / 동작) because they know they are observed. Treatment delivery in trial may be more intensive than real program.

Hiện thực (implementation / 구현) fidelity and naturalistic settings matter.

## 16. Ethical and practical các ràng buộc (constraints / 제약조건들)

Not every question can be randomized. It may be unethical to assign smoking, unemployment or harmful pollution.

Natural experiments and quasi-experimental methods exploit institutional variation instead.

## 17. Selection on observables

Observational identification sometimes assumes:

```text
{Y(1),Y(0)} ⟂ D | X
```

Given observed X, assignment is as-good-as-random.

This is strong because unobserved confounders may remain.

## 18. Matching

Matching compares treated units to untreated with similar covariates.

Chính xác (exact / 정확한) matching is difficult with many dimensions. Distance or propensity-score methods reduce dimensionality but do not solve hidden confounding.

## 19. Propensity score
Phần “19. Propensity score” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```text
e(X) = P(D=1 | X)
```

Under conditional independence and overlap, conditioning on propensity score can balance phân phối (distribution / 분포) of observed X.

Propensity score is not “xác suất (probability / 확률) treatment caused kết quả (outcome / 결과)”.

## 20. Propensity-score pitfalls

Good propensity mô hình (model / 모델) predicts treatment assignment for balance, not necessarily kết quả (outcome / 결과).

Including instruments or post-treatment variables may worsen hiệu năng (performance / 성능). Trimming extreme scores changes mục tiêu (target / 대상) population.

Balance diagnostics matter more than classification accuracy.

## 21. Inverse xác suất (probability / 확률) weighting

ATE weighting uses roughly:

```text
D/e(X) + (1−D)/(1−e(X))
```

to create pseudo-population balanced on observed covariates.

Extreme propensity scores create huge weights and variance. Positivity/overlap is substantive, not merely numerical.

## 22. Regression adjustment

Kết quả (outcome / 결과) mô hình (model / 모델) estimates conditional outcomes then averages counterfactual predictions.

Correct specification can identify under selection-on-observables. Flexible các mô hình (models / 모델들) help but hidden confounding remains.

## 23. Doubly robust estimators

Augmented IPW combines treatment mô hình (model / 모델) and kết quả (outcome / 결과) mô hình (model / 모델). Under conditions, estimator remains consistent if one of the two nuisance các mô hình (models / 모델들) is correctly specified.

“Doubly robust” does not protect against unmeasured confounding or violations of positivity.

## 24. Difference in means vs regression in RCT

Simple difference in means is design-unbiased under randomization.

Regression can improve precision and handle stratification, but complicated controls should not obscure the assignment cơ chế (mechanism / 메커니즘).

## 25. Natural experiments

Natural experiment arises when institution/sự kiện (event / 이벤트) creates variation plausibly unrelated to potential outcomes, such as lottery, quy tắc (rule / 규칙) threshold, timing or geography.

Label “natural experiment” is not enough. Need explain chính xác (exact / 정확한) assignment cơ chế (mechanism / 메커니즘) and threats.

## 26. Placebo tests

If treatment supposedly starts at thời gian (time / 시간) T, finding “tác động (effect / 효과)” before T threatens thiết kế (design / 설계).

Placebo outcomes or populations unaffected by cơ chế (mechanism / 메커니즘) can kiểm thử (test / 테스트) alternative explanations, though passing placebo does not prove validity.

## 27. Negative controls

A negative-control kết quả (outcome / 결과) should not causally respond to treatment; negative-control exposure should not affect kết quả (outcome / 결과).

Unexpected association can reveal residual confounding or đo lường (measurement / 측정) problems.

## 28. Sensitivity phân tích (analysis / 분석)

Because unobserved confounding cannot be fully tested, quantify how strong hidden độ lệch (bias / 편향) would need to be to overturn conclusion.

Sensitivity should complement, not replace, substantive thiết kế (design / 설계) lập luận (reasoning / 추론).

## 29. Mediation vs total tác động (effect / 효과)

If treatment works through mediator M:

```text
D → M → Y
```

Total tác động (effect / 효과) includes mediated đường dẫn (path / 경로). Conditioning on M changes estimand and may introduce post-treatment độ lệch (bias / 편향).

Mediation phân tích (analysis / 분석) requires stronger các giả định (assumptions / 가정들) than total-effect estimation.

## 30. Heterogeneous treatment effects

Average tác động (effect / 효과) may hide subgroup differences.

Pre-specified heterogeneity by baseline rủi ro (risk / 위험), age, firm kích thước (size / 크기) or region can matter for chính sách (policy / 정책). Data-driven subgroup discovery needs kiểm tra hợp lệ (validation / 검증) to avoid overfitting.

## 31. Equilibrium effects

Large-scale chính sách (policy / 정책) can thay đổi (change / 변경) wages, prices, rents or entry. Individual-level experiment may capture partial-equilibrium tác động (effect / 효과) only.

Scaling micro treatment into macro chính sách (policy / 정책) requires market-response mô hình (model / 모델) or larger-scale bằng chứng (evidence / 증거).

## 32. Thất bại (failure / 실패) modes

Sai lầm thứ nhất là compare treated vs untreated actual participation when compliance selective.

Sai lầm thứ hai là nghĩ randomization solves attrition/spillovers automatically.

Sai lầm thứ ba là dùng propensity score như magic cure for confounding.

Sai lầm thứ tư là ignore overlap and extreme weights.

Sai lầm thứ năm là generalize RCT beyond population/quy mô (scale / 규모) without cơ chế (mechanism / 메커니즘).

Sai lầm thứ sáu là điều khiển (control / 제어) mediator while claiming total tác động (effect / 효과).

## 33. Mô hình tư duy (mental model / 사고 모델)

Khi đọc nhân quả (causal / 인과적) study, hãy hỏi:

1. Treatment assignment cơ chế (mechanism / 메커니즘) là gì?
2. Missing counterfactual được approximated bởi group nào?
3. Randomization/conditional independence có credible không?
4. Compliance, attrition và spillovers ra sao?
5. Đơn vị (unit / 단위)/cluster assignment và SE có khớp không?
6. Overlap có đủ không?
7. Estimand là ITT, ATE, ATT hay cục bộ (local / 로컬) tác động (effect / 효과)?
8. Placebo/negative controls nói gì?
9. Scale-up có equilibrium tác động (effect / 효과) không?
10. Bên ngoài (external / 외부) validity dựa cơ chế (mechanism / 메커니즘) nào?

Experiments là benchmark, nhưng many economic questions rely on endogenous choices. Chapter tiếp theo xử lý các designs dùng instruments và thresholds để isolate exogenous variation.
