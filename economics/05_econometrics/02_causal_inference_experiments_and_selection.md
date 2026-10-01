# Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Fundamental bài toán (problem / 문제) of nhân quả (causal / 인과적) suy luận (inference / 추론)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Selection độ lệch (bias / 편향) decomposition** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

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

> **Chuyển mạch:** Causal question cần counterfactual; selection bias decomposes observed difference, còn random assignment tạo exchangeability để isolate treatment effect.

## 2. Selection độ lệch (bias / 편향) decomposition

Naive difference:

```text
E[Y | D=1] − E[Y | D=0]
```

có thể decomposed thành treatment tác động (effect / 효과) plus selection difference.

Treated group thường khác untreated group trước treatment. Wage difference giữa college graduates và non-graduates không chỉ là schooling tác động (effect / 효과); ability, family background và preferences cùng influence selection.

> **Chuyển mạch:** Ở chặng này của **Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection**, **3. Random assignment** tiếp nhận điểm tựa từ **2. Selection độ lệch (bias / 편향) decomposition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Randomization suy luận (inference / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Random assignment

Nếu treatment randomly assigned:

```text
D ⟂ {Y(1), Y(0)}
```

thì untreated outcomes of điều khiển (control / 제어) group provide unbiased counterfactual on average.

Randomization không làm groups identical trong từng mẫu (sample / 표본); nó làm imbalance stochastic và quantifiable.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection**, **4. Randomization suy luận (inference / 추론)** tiếp nhận điểm tựa từ **3. Random assignment** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Intent-to-Treat** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Randomization suy luận (inference / 추론)

Under sharp null of no treatment tác động (effect / 효과) for every đơn vị (unit / 단위), treatment labels có thể được permuted according to assignment cơ chế (mechanism / 메커니즘) để derive chính xác (exact / 정확한)/randomization phân phối (distribution / 분포).

This emphasizes thiết kế (design / 설계) rather than asymptotic regression các giả định (assumptions / 가정들).

> **Chuyển mạch:** Trong **Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection**, **5. Intent-to-Treat** tiếp nhận điểm tựa từ **4. Randomization suy luận (inference / 추론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Treatment-on-the-Treated and noncompliance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Intent-to-Treat

Intent-to-Treat (ITT) compares outcomes by assigned treatment, regardless of compliance:

```text
ITT = E[Y | Z=1] − E[Y | Z=0]
```

where `Z` is assignment.

ITT answers tác động (effect / 효과) of offering/assigning treatment under real compliance hành vi (behavior / 동작) and preserves randomization.

> **Chuyển mạch:** Ở chặng này của **Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection**, **6. Treatment-on-the-Treated and noncompliance** tiếp nhận điểm tựa từ **5. Intent-to-Treat** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Attrition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Treatment-on-the-Treated and noncompliance

If assigned participants do not all take treatment, comparing actual takers vs non-takers reintroduces selection.

Random assignment can be used as instrument for actual treatment under additional các giả định (assumptions / 가정들), leading to LATE for compliers.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection**, **7. Attrition** tiếp nhận điểm tựa từ **6. Treatment-on-the-Treated and noncompliance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Spillovers and contamination** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Attrition

Randomization at baseline does not protect against differential attrition after assignment.

If treated low-outcome units drop out more often, observed treatment mean becomes biased.

Report attrition by arm, reasons, bounds/sensitivity and use administrative follow-up where possible.

> **Chuyển mạch:** Trong **Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection**, **8. Spillovers and contamination** tiếp nhận điểm tựa từ **7. Attrition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Cluster randomization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Spillovers and contamination

Điều khiển (control / 제어) units may indirectly receive treatment through peers, markets or thông tin (information / 정보).

Then tiêu chuẩn (standard / 표준) treatment-control difference estimates tác động (effect / 효과) under contamination rather than isolated treatment.

Cluster randomization or exposure ánh xạ (mapping / 매핑) may be necessary.

> **Chuyển mạch:** Ở chặng này của **Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection**, **9. Cluster randomization** tiếp nhận điểm tựa từ **8. Spillovers and contamination** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Stratification and blocking** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Cluster randomization

Treatment may be assigned to schools, villages, hospitals or firms rather than individuals.

Effective independent cỡ mẫu (sample size / 표본 크기) is number of clusters, not raw individuals. Intra-cluster correlation reduces power.

Thiết kế (design / 설계) and SE must match assignment mức (level / 수준).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection**, **10. Stratification and blocking** tiếp nhận điểm tựa từ **9. Cluster randomization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Power and minimum detectable tác động (effect / 효과)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Stratification and blocking

Randomization within pre-defined blocks (region, baseline outcome, size) can improve balance and precision.

Phân tích (analysis / 분석) should account for thiết kế (design / 설계). Post-hoc subgroup creation is different from pre-randomization blocking.

> **Chuyển mạch:** Trong **Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection**, **11. Power and minimum detectable tác động (effect / 효과)** tiếp nhận điểm tựa từ **10. Stratification and blocking** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Baseline adjustment** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection**, **12. Baseline adjustment** tiếp nhận điểm tựa từ **11. Power and minimum detectable tác động (effect / 효과)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Multiple outcomes and treatment arms** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Baseline adjustment

Including strongly predictive pre-treatment outcomes can improve precision without threatening randomization.

But post-treatment controls should not be added mechanically.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection**, **13. Multiple outcomes and treatment arms** tiếp nhận điểm tựa từ **12. Baseline adjustment** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Bên ngoài (external / 외부) validity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Multiple outcomes and treatment arms

Many outcomes/arms increase false positives. Pre-specify primary outcomes and adjust families when appropriate.

Exploratory outcomes are useful if labeled exploratory.

> **Chuyển mạch:** Trong **Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection**, **14. Bên ngoài (external / 외부) validity** tiếp nhận điểm tựa từ **13. Multiple outcomes and treatment arms** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Hawthorne and experiment effects** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Bên ngoài (external / 외부) validity

RCT identifies tác động (effect / 효과) for study mẫu (sample / 표본), treatment phiên bản (version / 버전) and hiện thực (implementation / 구현) ngữ cảnh (context / 맥락).

Scaling can thay đổi (change / 변경) prices, provider chất lượng (quality / 품질), equilibrium hành vi (behavior / 동작) and political responses. A village pilot may not predict national rollout.

Bên ngoài (external / 외부) validity is a separate nhân quả (causal / 인과적) question.

> **Chuyển mạch:** Ở chặng này của **Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection**, **15. Hawthorne and experiment effects** tiếp nhận điểm tựa từ **14. Bên ngoài (external / 외부) validity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Ethical and practical các ràng buộc (constraints / 제약조건들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Hawthorne and experiment effects

Subjects/providers may thay đổi (change / 변경) hành vi (behavior / 동작) because they know they are observed. Treatment delivery in trial may be more intensive than real program.

Hiện thực (implementation / 구현) fidelity and naturalistic settings matter.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection**, **16. Ethical and practical các ràng buộc (constraints / 제약조건들)** tiếp nhận điểm tựa từ **15. Hawthorne and experiment effects** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Selection on observables** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Ethical and practical các ràng buộc (constraints / 제약조건들)

Not every question can be randomized. It may be unethical to assign smoking, unemployment or harmful pollution.

Natural experiments and quasi-experimental methods exploit institutional variation instead.

> **Chuyển mạch:** Trong **Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection**, **17. Selection on observables** tiếp nhận điểm tựa từ **16. Ethical and practical các ràng buộc (constraints / 제약조건들)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Matching** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Selection on observables

Observational identification sometimes assumes:

```text
{Y(1),Y(0)} ⟂ D | X
```

Given observed X, assignment is as-good-as-random.

This is strong because unobserved confounders may remain.

> **Chuyển mạch:** Ở chặng này của **Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection**, **18. Matching** tiếp nhận điểm tựa từ **17. Selection on observables** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Propensity score** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Matching

Matching compares treated units to untreated with similar covariates.

Chính xác (exact / 정확한) matching is difficult with many dimensions. Distance or propensity-score methods reduce dimensionality but do not solve hidden confounding.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection**, **19. Propensity score** tiếp nhận điểm tựa từ **18. Matching** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Propensity-score pitfalls** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Propensity score

```text
e(X) = P(D=1 | X)
```

Under conditional independence and overlap, conditioning on propensity score can balance phân phối (distribution / 분포) of observed X.

Propensity score is not “xác suất (probability / 확률) treatment caused kết quả (outcome / 결과)”.

> **Chuyển mạch:** Trong **Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection**, **20. Propensity-score pitfalls** tiếp nhận điểm tựa từ **19. Propensity score** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Inverse xác suất (probability / 확률) weighting** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Propensity-score pitfalls

Good propensity mô hình (model / 모델) predicts treatment assignment for balance, not necessarily kết quả (outcome / 결과).

Including instruments or post-treatment variables may worsen hiệu năng (performance / 성능). Trimming extreme scores changes mục tiêu (target / 대상) population.

Balance diagnostics matter more than classification accuracy.

> **Chuyển mạch:** Ở chặng này của **Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection**, **21. Inverse xác suất (probability / 확률) weighting** tiếp nhận điểm tựa từ **20. Propensity-score pitfalls** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Regression adjustment** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Inverse xác suất (probability / 확률) weighting

ATE weighting uses roughly:

```text
D/e(X) + (1−D)/(1−e(X))
```

to create pseudo-population balanced on observed covariates.

Extreme propensity scores create huge weights and variance. Positivity/overlap is substantive, not merely numerical.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection**, **22. Regression adjustment** tiếp nhận điểm tựa từ **21. Inverse xác suất (probability / 확률) weighting** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Doubly robust estimators** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Regression adjustment

Kết quả (outcome / 결과) mô hình (model / 모델) estimates conditional outcomes then averages counterfactual predictions.

Correct specification can identify under selection-on-observables. Flexible các mô hình (models / 모델들) help but hidden confounding remains.

> **Chuyển mạch:** Trong **Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection**, **23. Doubly robust estimators** tiếp nhận điểm tựa từ **22. Regression adjustment** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Difference in means vs regression in RCT** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Doubly robust estimators

Augmented IPW combines treatment mô hình (model / 모델) and kết quả (outcome / 결과) mô hình (model / 모델). Under conditions, estimator remains consistent if one of the two nuisance các mô hình (models / 모델들) is correctly specified.

“Doubly robust” does not protect against unmeasured confounding or violations of positivity.

> **Chuyển mạch:** Ở chặng này của **Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection**, **24. Difference in means vs regression in RCT** tiếp nhận điểm tựa từ **23. Doubly robust estimators** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Natural experiments** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Difference in means vs regression in RCT

Simple difference in means is design-unbiased under randomization.

Regression can improve precision and handle stratification, but complicated controls should not obscure the assignment cơ chế (mechanism / 메커니즘).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection**, **25. Natural experiments** tiếp nhận điểm tựa từ **24. Difference in means vs regression in RCT** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Placebo tests** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Natural experiments

Natural experiment arises when institution/sự kiện (event / 이벤트) creates variation plausibly unrelated to potential outcomes, such as lottery, quy tắc (rule / 규칙) threshold, timing or geography.

Label “natural experiment” is not enough. Need explain chính xác (exact / 정확한) assignment cơ chế (mechanism / 메커니즘) and threats.

> **Chuyển mạch:** Trong **Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection**, **26. Placebo tests** tiếp nhận điểm tựa từ **25. Natural experiments** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Negative controls** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Placebo tests

If treatment supposedly starts at thời gian (time / 시간) T, finding “tác động (effect / 효과)” before T threatens thiết kế (design / 설계).

Placebo outcomes or populations unaffected by cơ chế (mechanism / 메커니즘) can kiểm thử (test / 테스트) alternative explanations, though passing placebo does not prove validity.

> **Chuyển mạch:** Ở chặng này của **Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection**, **27. Negative controls** tiếp nhận điểm tựa từ **26. Placebo tests** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Sensitivity phân tích (analysis / 분석)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Negative controls

A negative-control kết quả (outcome / 결과) should not causally respond to treatment; negative-control exposure should not affect kết quả (outcome / 결과).

Unexpected association can reveal residual confounding or đo lường (measurement / 측정) problems.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection**, **28. Sensitivity phân tích (analysis / 분석)** tiếp nhận điểm tựa từ **27. Negative controls** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Mediation vs total tác động (effect / 효과)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Sensitivity phân tích (analysis / 분석)

Because unobserved confounding cannot be fully tested, quantify how strong hidden độ lệch (bias / 편향) would need to be to overturn conclusion.

Sensitivity should complement, not replace, substantive thiết kế (design / 설계) lập luận (reasoning / 추론).

> **Chuyển mạch:** Trong **Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection**, **29. Mediation vs total tác động (effect / 효과)** tiếp nhận điểm tựa từ **28. Sensitivity phân tích (analysis / 분석)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. Heterogeneous treatment effects** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Mediation vs total tác động (effect / 효과)

If treatment works through mediator M:

```text
D → M → Y
```

Total tác động (effect / 효과) includes mediated đường dẫn (path / 경로). Conditioning on M changes estimand and may introduce post-treatment độ lệch (bias / 편향).

Mediation phân tích (analysis / 분석) requires stronger các giả định (assumptions / 가정들) than total-effect estimation.

> **Chuyển mạch:** Ở chặng này của **Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection**, **30. Heterogeneous treatment effects** tiếp nhận điểm tựa từ **29. Mediation vs total tác động (effect / 효과)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. Equilibrium effects** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Heterogeneous treatment effects

Average tác động (effect / 효과) may hide subgroup differences.

Pre-specified heterogeneity by baseline rủi ro (risk / 위험), age, firm kích thước (size / 크기) or region can matter for chính sách (policy / 정책). Data-driven subgroup discovery needs kiểm tra hợp lệ (validation / 검증) to avoid overfitting.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection**, **31. Equilibrium effects** tiếp nhận điểm tựa từ **30. Heterogeneous treatment effects** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. Thất bại (failure / 실패) modes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Equilibrium effects

Large-scale chính sách (policy / 정책) can thay đổi (change / 변경) wages, prices, rents or entry. Individual-level experiment may capture partial-equilibrium tác động (effect / 효과) only.

Scaling micro treatment into macro chính sách (policy / 정책) requires market-response mô hình (model / 모델) or larger-scale bằng chứng (evidence / 증거).

> **Chuyển mạch:** Trong **Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection**, **32. Thất bại (failure / 실패) modes** tiếp nhận điểm tựa từ **31. Equilibrium effects** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Thất bại (failure / 실패) modes

Sai lầm thứ nhất là compare treated vs untreated actual participation when compliance selective.

Sai lầm thứ hai là nghĩ randomization solves attrition/spillovers automatically.

Sai lầm thứ ba là dùng propensity score như magic cure for confounding.

Sai lầm thứ tư là ignore overlap and extreme weights.

Sai lầm thứ năm là generalize RCT beyond population/quy mô (scale / 규모) without cơ chế (mechanism / 메커니즘).

Sai lầm thứ sáu là điều khiển (control / 제어) mediator while claiming total tác động (effect / 효과).

> **Chuyển mạch:** Ở chặng này của **Nhân quả (causal / 인과적) Suy luận (inference / 추론) & Experiments — Counterfactual, randomization và selection**, **33. Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **32. Thất bại (failure / 실패) modes** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

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

> **Bàn giao:** Sau **33. Mô hình tư duy (mental model / 사고 모델)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
