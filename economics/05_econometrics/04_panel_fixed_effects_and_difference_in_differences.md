# Panel dữ liệu (data / 데이터), Fixed Effects & Difference-in-Differences — Dùng variation theo đơn vị (unit / 단위) và thời gian

> **Mạch đọc:** Đặt **Panel dữ liệu (data / 데이터), Fixed Effects & Difference-in-Differences — Dùng variation theo đơn vị (unit / 단위) và thời gian** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Panel cấu trúc (structure / 구조)** sang **2. Between vs within variation**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Panel dữ liệu (data / 데이터) theo dõi cùng units qua nhiều periods, cho phép so sánh một đơn vị (unit / 단위) với chính nó và tách một số unobserved differences cố định. Nhưng panel không tự động nhân quả (causal / 인과적). Fixed effects chỉ loại confounding **không đổi theo thời gian**; Difference-in-Differences (DiD) cần thêm parallel-trends các giả định (assumptions / 가정들) và careful treatment timing.

## 1. Panel cấu trúc (structure / 구조)

Basic panel notation:

```text
Y_it
X_it
```

với đơn vị (unit / 단위) `i`, thời gian (time / 시간) `t`.

Balanced panel có mọi đơn vị (unit / 단위) ở mọi periods; unbalanced panel thiếu một số observations. Attrition có thể endogenous.

## 2. Between vs within variation

Cross-sectional comparison dùng differences giữa units.

Fixed-effects estimation chủ yếu dùng changes within same đơn vị (unit / 단위) over thời gian (time / 시간).

Nếu education không đổi trong adult panel, person fixed effects không thể estimate tác động (effect / 효과) của education mức (level / 수준) từ within-person variation.

## 3. đơn vị (unit / 단위) fixed effects

Mô hình (model / 모델):

```text
Y_it = βX_it + α_i + u_it
```

`α_i` captures all time-invariant đơn vị (unit / 단위) characteristics, observed or unobserved.

Demeaning removes `α_i`:

```text
Y_it − Ȳ_i = β(X_it − X̄_i) + (u_it − ū_i)
```

Thus identification comes from within-unit changes.

## 4. thời gian (time / 시간) fixed effects

Add dùng chung (common / 공통) shocks:

```text
Y_it = βX_it + α_i + λ_t + u_it
```

`λ_t` absorbs shocks affecting all units in a period: national recession, inflation, dùng chung (common / 공통) technology trend.

Two-way fixed effects combine đơn vị (unit / 단위) and thời gian (time / 시간) FE.

## 5. What fixed effects do not solve

If time-varying confounder affects both X and Y, đơn vị (unit / 단위) FE does not remove it.

Example: cục bộ (local / 로컬) economic boom increases both công khai (public / 공개) spending and employment. County FE removes permanent county differences but not boom shocks.

## 6. Bad controls remain bad

Panel does not make post-treatment controls safe. Conditioning on mediator or collider after treatment can still độ lệch (bias / 편향) total tác động (effect / 효과).

## 7. Fixed effects and sai số đo lường (measurement error / 측정 오차)

Within transformation can amplify noise when true X changes slowly but sai số đo lường (measurement error / 측정 오차) varies period-to-period.

FE estimates may become more attenuated than cross-sectional estimates under classical sai số đo lường (measurement error / 측정 오차).

## 8. Random effects

Random-effects mô hình (model / 모델) treats đơn vị (unit / 단위) tác động (effect / 효과) as uncorrelated with regressors under stronger giả định (assumption / 가정):

```text
Cov(α_i, X_it) = 0
```

It uses both within and between variation and can estimate time-invariant regressors.

Choice FE vs RE should be substantive, not only a mechanical Hausman kiểm thử (test / 테스트).

## 9. First differences

For two periods:

```text
ΔY_i = βΔX_i + Δu_i
```

First differencing also removes time-invariant đơn vị (unit / 단위) effects.

With many periods, FE and FD differ in efficiency and phản hồi (response / 응답) to serial correlation.

## 10. Difference-in-Differences idea

Suppose one group receives chính sách (policy / 정책) and another does not. Compare before-after thay đổi (change / 변경) in treated to before-after thay đổi (change / 변경) in điều khiển (control / 제어):

```text
DiD = (Y_T,after − Y_T,before)
    − (Y_C,after − Y_C,before)
```

Điều khiển (control / 제어) group estimates counterfactual trend for treated group absent treatment.

## 11. Parallel trends

Cốt lõi (core / 핵심) giả định (assumption / 가정):

```text
E[Y_T(0,after) − Y_T(0,before)]
=
E[Y_C(0,after) − Y_C(0,before)]
```

Treated and điều khiển (control / 제어) need not have same levels. They need comparable untreated trends for relevant period.

Parallel trends is about counterfactual outcomes and cannot be fully tested after treatment.

## 12. Two-period regression form

A tiêu chuẩn (standard / 표준) mô hình (model / 모델):

```text
Y_it = α + βTreated_i + γPost_t
     + δ(Treated_i × Post_t) + u_it
```

`δ` is DiD estimate under các giả định (assumptions / 가정들).

With đơn vị (unit / 단위)/thời gian (time / 시간) FE, time-invariant group dummy and dùng chung (common / 공통) post dummy are absorbed.

## 13. Pre-trends

Plot and estimate event-time coefficients before treatment. Large pre-treatment divergence threatens parallel trends.

But thất bại (failure / 실패) to reject pre-trends does not prove parallel trends: pre-period may be noisy/short, and anticipation can start before formal treatment.

## 14. sự kiện (event / 이벤트) study

Event-study specification estimates động (dynamic / 동적) effects relative to treatment thời gian (time / 시간):

```text
Y_it = α_i + λ_t + Σ_k β_k 1[event time = k] + u_it
```

Pre-treatment coefficients diagnose trends/anticipation; post coefficients show dynamics.

Tham chiếu (reference / 참조) period must be omitted.

## 15. Staggered adoption bài toán (problem / 문제)

When units adopt treatment at different times, classic two-way fixed-effects DiD can use already-treated units as controls for later-treated units.

With heterogeneous treatment effects over cohorts/thời gian (time / 시간), coefficient may be weighted average with undesirable or negative weights.

Hiện đại (modern / 현대적) DiD methods compare appropriate not-yet-treated/never-treated groups and aggregate cohort-time effects explicitly.

## 16. Treatment-effect heterogeneity

Chính sách (policy / 정책) tác động (effect / 효과) may grow over thời gian (time / 시간) or vary across cohorts. A single TWFE coefficient can obscure this.

Report động (dynamic / 동적)/cohort-specific effects when substantive.

## 17. Never-treated vs not-yet-treated controls

Never-treated group can be useful if comparable. If all units eventually treated, not-yet-treated units provide temporary controls.

Need avoid using post-treated outcomes as untreated counterfactual.

## 18. Anticipation

If firms/households thay đổi (change / 변경) hành vi (behavior / 동작) when chính sách (policy / 정책) announced before hiện thực (implementation / 구현), “pre-treatment” cửa sổ (window / 윈도우) after announcement is already affected.

Treatment timing should follow thông tin (information / 정보) exposure, not only legal effective date.

## 19. Spillovers

Chính sách (policy / 정책) in one region may affect neighboring điều khiển (control / 제어) region through labor mobility, trade or prices.

Spillovers violate stable điều khiển (control / 제어) điều kiện (condition / 조건) and can attenuate or reverse DiD estimate.

## 20. Composition changes

If treatment changes who remains in mẫu (sample / 표본), observed group kết quả (outcome / 결과) can shift even without individual kết quả (outcome / 결과) thay đổi (change / 변경).

Examples: di chuyển (migration / 마이그레이션) after cục bộ (local / 로컬) tax, school enrollment after reform, firm exit after regulation.

Nhánh học (track / 트랙) population/composition alongside kết quả (outcome / 결과).

## 21. Differential shocks

A cục bộ (local / 로컬) shock coinciding with treatment can mimic chính sách (policy / 정책) tác động (effect / 효과). Controls for measured shocks may help, but thiết kế (design / 설계) needs institutional argument and alternative comparison groups.

## 22. Triple differences

Difference-in-Difference-in-Differences adds a third dimension to net out another differential trend.

Example compare treated vs điều khiển (control / 제어) regions, before vs after, and eligible vs ineligible group.

DDD needs its own parallel-trends-style các giả định (assumptions / 가정들) and can become hard to interpret.

## 23. Synthetic điều khiển (control / 제어)

When one/few aggregate units are treated, synthetic điều khiển (control / 제어) constructs weighted combination of untreated units matching pre-treatment outcomes/covariates.

It makes counterfactual transparent but requires good donor pool and long enough pre-period.

## 24. Synthetic-control risks

Poor pre-treatment fit weakens credibility. Donor contamination, interpolation outside convex hull or structural breaks also matter.

Placebo-in-space/thời gian (time / 시간) helps assess unusual post-treatment divergence.

## 25. Interactive fixed effects

Simple đơn vị (unit / 단위)/thời gian (time / 시간) FE assume dùng chung (common / 공통) thời gian (time / 시간) shocks plus đơn vị (unit / 단위) constants. If latent factors affect units differently over thời gian (time / 시간), interactive-factor các mô hình (models / 모델들) can capture richer trends:

```text
λ_i' f_t
```

But added flexibility raises identification/model-selection demands.

## 26. Clustered suy luận (inference / 추론) in DiD

Chính sách (policy / 정책) assigned at trạng thái (state / 상태)/firm/school mức (level / 수준) creates within-cluster serial dependence.

SE usually clustered at treatment-assignment mức (level / 수준). Few clusters require special methods such as wild-cluster bootstrap or randomization-based approaches depending thiết kế (design / 설계).

## 27. Serial correlation and false significance

Persistent outcomes and treatments make naive SE badly understated in chính sách (policy / 정책) panels.

Long thời gian (time / 시간) series per đơn vị (unit / 단위) do not equal many independent treatment shocks.

## 28. Unit-specific trends

Adding tuyến tính (linear / 선형) đơn vị (unit / 단위) trends can absorb differential pre-trends but may also absorb genuine treatment dynamics and rely heavily on functional form.

Use only with substantive justification and show sensitivity.

## 29. Fixed effects as thiết kế (design / 설계), not cleaning trick

Adding hundreds of FE does not automatically make regression nhân quả (causal / 인과적). Every FE changes which variation identifies coefficient.

Ask: after absorbing these dimensions, what variation remains, and why is it exogenous?

## 30. thất bại (failure / 실패) modes

Sai lầm thứ nhất là nói đơn vị (unit / 단위) FE controls every unobserved confounder.

Sai lầm thứ hai là infer parallel trends just because pre-trend p-values > 0.05.

Sai lầm thứ ba là use classic TWFE with staggered adoption/heterogeneous effects without checking weights.

Sai lầm thứ tư là ignore anticipation/spillovers/composition.

Sai lầm thứ năm là cluster SE at individual mức (level / 수준) when treatment assigned at chính sách (policy / 정책) mức (level / 수준).

Sai lầm thứ sáu là add đơn vị (unit / 단위) trends mechanically until desired kết quả (result / 결과) appears.

## 31. mô hình tư duy (mental model / 사고 모델)

Khi đọc panel/DiD, hãy hỏi:

1. Identification dùng within hay between variation?
2. đơn vị (unit / 단위)/thời gian (time / 시간) FE absorb gì và không absorb gì?
3. Treatment timing và announcement timing khác nhau không?
4. Counterfactual trend đến từ group nào?
5. Pre-trends informative đến mức nào?
6. Adoption có staggered không, tác động (effect / 효과) có heterogeneous không?
7. Controls đã từng treated có bị dùng sai không?
8. Spillover/di chuyển (migration / 마이그레이션)/composition có phá comparison không?
9. Cluster mức (level / 수준) có khớp assignment không?
10. Event-study dynamics có economic cơ chế (mechanism / 메커니즘) hợp lý không?

Panel methods tận dụng không gian (space / 공간) × thời gian (time / 시간) variation. Với macro/financial dữ liệu (data / 데이터), dependence qua thời gian tự thân trở thành đối tượng (object / 객체) cần mô hình (model / 모델). Chapter tiếp theo đi vào thời gian (time / 시간) series, forecasting và macro identification.

> **Bàn giao:** Sau **31. mô hình tư duy (mental model / 사고 모델)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 measurement data and estimands](./00_measurement_data_and_estimands.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
