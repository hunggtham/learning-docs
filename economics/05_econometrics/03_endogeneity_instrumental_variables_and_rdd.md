# Endogeneity, Instrumental Variables & RDD — Khi treatment không exogenous

> **Mạch đọc:** Đặt **Endogeneity, Instrumental Variables & RDD — Khi treatment không exogenous** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Endogeneity là vấn đề về nguồn (source / 소스) of variation** sang **2. Omitted-variable endogeneity**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Endogeneity xuất hiện khi regressor liên quan với lỗi (error / 오류) term theo cách làm coefficient không còn phản ánh nhân quả (causal / 인과적) tác động (effect / 효과) cần tìm. Sources chính gồm omitted variables, simultaneity/reverse causality, sai số đo lường (measurement error / 측정 오차) và endogenous selection. Instrumental Variables (IV) và Regression Discontinuity thiết kế (design / 설계) (RDD) là hai strategies quan trọng để tìm variation treatment có nhân quả (causal / 인과적) interpretation rõ hơn, nhưng cả hai chỉ mạnh khi institutional các giả định (assumptions / 가정들) thật sự credible.

## 1. Endogeneity là vấn đề về nguồn (source / 소스) of variation

Simple regression:

```text
Y = βD + u
```

Muốn đọc `β` nhân quả (causal / 인과적), cần variation của D không đi cùng unobserved determinants của Y.

Nếu:

```text
Cov(D,u) ≠ 0
```

OLS generally biased/inconsistent cho nhân quả (causal / 인과적) parameter.

## 2. Omitted-variable endogeneity

Nếu ability ảnh hưởng cả education và wage, regression wage on schooling omitting ability mixes schooling tác động (effect / 효과) với selection on ability.

Adding a proxy can reduce độ lệch (bias / 편향) only if proxy sufficiently captures confounder and does not introduce bad-control paths.

## 3. Simultaneity

Price và quantity determined together by supply and demand. Regressing quantity on observed price without a demand/supply shifter does not recover demand curve because price reacts to shocks in both curves.

This is classic identification bài toán (problem / 문제): equilibrium correlation is not structural slope.

## 4. Reverse causality

Crime may affect police triển khai (deployment / 배포) while police affects crime. Health affects income while income affects health.

Timing alone may not solve if anticipatory hành vi (behavior / 동작) or persistent shocks exist.

## 5. Measurement-error endogeneity

Classical lỗi (error / 오류) in explanatory variable creates correlation between observed regressor and composite lỗi (error / 오류), often attenuating OLS.

A valid instrument correlated with true X but independent of sai số đo lường (measurement error / 측정 오차) can sometimes solve this.

## 6. Instrumental-variable idea

An instrument `Z` changes treatment `D` but affects kết quả (outcome / 결과) `Y` only through D, under các giả định (assumptions / 가정들).

Two cốt lõi (core / 핵심) requirements:

```text
Relevance: Cov(Z,D) ≠ 0
Exogeneity / exclusion: Z affects Y only through D and is independent of relevant unobservables
```

Relevance is partly testable. Exclusion is fundamentally substantive/institutional.

## 7. First stage and reduced form

First stage:

```text
D = π0 + π1Z + controls + v
```

Reduced form:

```text
Y = γ0 + γ1Z + controls + e
```

With one instrument/treatment, Wald ratio:

```text
β_IV = γ1 / π1
```

Interpretation: tác động (effect / 효과) of instrument on kết quả (outcome / 결과) divided by tác động (effect / 효과) of instrument on treatment.

## 8. Two-Stage Least Squares

2SLS first predicts treatment using instruments:

```text
D̂ = projection of D on Z and controls
```

Then relates Y to instrument-induced thành phần (component / 컴포넌트) of D.

Mô hình tư duy (mental model / 사고 모델): IV discards endogenous variation in D and uses only variation moved by Z.

## 9. Weak instruments

If first stage is weak, IV estimates can be noisy, biased toward OLS in finite samples and suy luận (inference / 추론) unreliable.

First-stage F-statistic is a diagnostic, but simple rules like “F>10 always enough” are context-dependent, especially multiple instruments/heteroskedasticity.

Report first-stage strength and weak-IV-robust suy luận (inference / 추론) when relevant.

## 10. Exclusion restriction

Suppose distance to college instruments education. Exclusion requires distance affects earnings only through schooling, not cục bộ (local / 로컬) labor markets, family location selection or urban opportunities.

A statistically strong first stage does nothing to validate exclusion.

## 11. Independence

Instrument must be as-good-as-random relative to potential outcomes, often conditional on controls.

Chính sách (policy / 정책) eligibility, lottery or historical assignment may provide stronger trường hợp (case / 사례) than arbitrary proxy.

## 12. Monotonicity and LATE

With heterogeneous treatment effects and noncompliance, IV often identifies cục bộ (local / 로컬) Average Treatment tác động (effect / 효과) for **compliers** if monotonicity holds: instrument does not push some units toward treatment while pushing others away in opposite way.

Thus IV tác động (effect / 효과) may not equal ATE.

## 13. Compliers, always-takers, never-takers, defiers

Under nhị phân (binary / 이진) assignment/treatment:

- compliers follow assignment;
- always-takers take regardless;
- never-takers never take;
- defiers do opposite.

Monotonicity rules out defiers. LATE applies to compliers whose treatment is changed by instrument.

## 14. bên ngoài (external / 외부) validity of IV

Different instruments move different populations/margins. Draft lottery may identify tác động (effect / 효과) for people induced by draft rủi ro (risk / 위험); college-distance instrument for marginal students near truy cập (access / 접근) ranh giới (boundary / 경계).

Two valid IVs can estimate different cục bộ (local / 로컬) effects without contradiction.

## 15. Overidentification tests

With more instruments than endogenous regressors, overidentification tests check whether instrument-implied moments jointly fit mô hình (model / 모델).

Passing kiểm thử (test / 테스트) does not prove all instruments valid; tests have power/mô hình (model / 모델) dependence and invalid instruments can thất bại (fail / 실패) in offsetting ways.

## 16. Many instruments

Adding many weak instruments can overfit first stage and worsen độ lệch (bias / 편향). Instrument count should follow credible sources of variation, not “more is better”.

## 17. Control-function intuition

Some endogeneity các mô hình (models / 모델들) explicitly estimate selection/endogenous residual then include correction term in kết quả (outcome / 결과) equation.

Điều khiển (control / 제어) functions can be useful in nonlinear settings but need structural các giả định (assumptions / 가정들) comparable in seriousness to IV.

## 18. Regression Discontinuity thiết kế (design / 설계)

RDD exploits treatment assignment changing discontinuously at a threshold of running variable:

```text
D = 1 if X ≥ c
```

If potential outcomes evolve smoothly through cutoff absent treatment, kết quả (outcome / 결과) jump at cutoff identifies a cục bộ (local / 로컬) nhân quả (causal / 인과적) tác động (effect / 효과).

## 19. Sharp vs fuzzy RDD

Sharp RDD: treatment status changes deterministically at threshold.

Fuzzy RDD: xác suất (probability / 확률) of treatment jumps but compliance imperfect. Cutoff indicator becomes instrument for actual treatment.

Fuzzy RDD therefore has IV/LATE interpretation near threshold.

## 20. cục bộ (local / 로컬) nature of RDD

RDD identifies tác động (effect / 효과) for units near cutoff, not necessarily far away.

Scholarship cutoff tác động (effect / 효과) for students scoring around 80 does not automatically generalize to students scoring 50 or 100.

## 21. Continuity giả định (assumption / 가정)

Key giả định (assumption / 가정): other determinants of kết quả (outcome / 결과) thay đổi (change / 변경) smoothly at cutoff.

If another chính sách (policy / 정책) begins at same threshold, kết quả (outcome / 결과) discontinuity cannot be attributed cleanly to treatment of interest.

## 22. Manipulation of running variable

If units can precisely sort around cutoff, groups just above/below may differ systematically.

Examples: income reported just below eligibility threshold, kiểm thử (test / 테스트) score manipulation, firms changing kích thước (size / 크기) to avoid regulation.

Density tests and institutional kiến thức (knowledge / 지식) help assess sorting.

## 23. Bandwidth choice

Use observations near cutoff to improve comparability, but too narrow means high variance; too wide means functional-form độ lệch (bias / 편향).

Hiện đại (modern / 현대적) RDD uses data-driven bandwidth procedures and cục bộ (local / 로컬) polynomial estimation rather than high-order toàn cục (global / 전역) polynomials.

## 24. Polynomial warning

High-order polynomial fits can behave wildly near boundaries and give misleading confidence intervals.

Prefer cục bộ (local / 로컬) tuyến tính (linear / 선형)/quadratic specifications with transparent bandwidth sensitivity.

## 25. RDD plots

A good plot shows binned outcomes and cục bộ (local / 로컬) fitted trends around cutoff, but visual bin choices can manipulate appearance.

Plot supports thiết kế (design / 설계); formal estimate/suy luận (inference / 추론) should not depend solely on eye inspection.

## 26. Covariate balance near cutoff

Pre-treatment covariates should not show suspicious jumps at cutoff under credible RDD.

Balance is diagnostic, not proof.

## 27. Placebo cutoffs

Estimate discontinuities at fake thresholds where no treatment changes. Effects there may suggest functional-form or other institutional problems.

## 28. Regression kink thiết kế (design / 설계)

Instead of mức (level / 수준) jump, chính sách (policy / 정책) may thay đổi (change / 변경) slope of treatment at threshold. Regression Kink thiết kế (design / 설계) uses discontinuity in derivative under stronger smoothness các giả định (assumptions / 가정들).

It is more sensitive to functional form and power.

## 29. Instrument vs điều khiển (control / 제어) confusion

A điều khiển (control / 제어) blocks confounding by conditioning. An instrument supplies exogenous treatment variation and generally should not directly affect kết quả (outcome / 결과).

A strong predictor of Y is not automatically a good instrument; often the opposite, because direct prediction threatens exclusion.

## 30. Structural interpretation

IV/RDD estimate specific cục bộ (local / 로컬) nhân quả (causal / 인과적) parameters. To predict effects of chính sách (policy / 정책) changes beyond observed margin, structural mô hình (model / 모델) or stronger các giả định (assumptions / 가정들) may be needed.

Do not lời gọi (call / 호출) a cục bộ (local / 로컬) estimate “universal elasticity” without justification.

## 31. thất bại (failure / 실패) modes

Sai lầm thứ nhất là chọn instrument chỉ vì correlated strongly with treatment.

Sai lầm thứ hai là kiểm thử (test / 테스트) exclusion restriction bằng p-value rồi coi validated.

Sai lầm thứ ba là bỏ weak-instrument bài toán (problem / 문제).

Sai lầm thứ tư là report IV as ATE when it is LATE.

Sai lầm thứ năm là extrapolate RDD tác động (effect / 효과) far from cutoff.

Sai lầm thứ sáu là use high-order polynomial mechanically.

Sai lầm thứ bảy là ignore manipulation/coincident policies at threshold.

## 32. mô hình tư duy (mental model / 사고 모델)

Khi dùng IV/RDD, hãy hỏi:

1. Endogeneity nguồn (source / 소스) cụ thể là gì?
2. Instrument thay đổi treatment bằng cơ chế (mechanism / 메커니즘) nào?
3. First stage đủ mạnh không?
4. Exclusion restriction có plausible theo institution không?
5. Population of compliers là ai?
6. tác động (effect / 효과) cục bộ (local / 로컬) ở margin nào?
7. RDD cutoff có manipulable không?
8. Có chính sách (policy / 정책)/shock khác cùng cutoff không?
9. kết quả (result / 결과) stable across reasonable bandwidth/specifications không?
10. chính sách (policy / 정책) question có cần extrapolate beyond identified cục bộ (local / 로컬) tác động (effect / 효과) không?

IV và RDD dùng special variation. Một family khác tận dụng variation across units and thời gian (time / 시간): panel fixed effects và Difference-in-Differences.

> **Bàn giao:** Sau **32. mô hình tư duy (mental model / 사고 모델)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 measurement data and estimands](./00_measurement_data_and_estimands.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
