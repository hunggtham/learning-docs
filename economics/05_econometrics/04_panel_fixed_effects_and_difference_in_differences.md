# Panel Data, Fixed Effects & Difference-in-Differences — Dùng variation theo unit và thời gian

Panel data theo dõi cùng units qua nhiều periods, cho phép so sánh một unit với chính nó và tách một số unobserved differences cố định. Nhưng panel không tự động causal. Fixed effects chỉ loại confounding **không đổi theo thời gian**; Difference-in-Differences (DiD) cần thêm parallel-trends assumptions và careful treatment timing.

## 1. Panel structure

Basic panel notation:

```text
Y_it
X_it
```

với unit `i`, time `t`.

Balanced panel có mọi unit ở mọi periods; unbalanced panel thiếu một số observations. Attrition có thể endogenous.

## 2. Between vs within variation

Cross-sectional comparison dùng differences giữa units.

Fixed-effects estimation chủ yếu dùng changes within same unit over time.

Nếu education không đổi trong adult panel, person fixed effects không thể estimate effect của education level từ within-person variation.

## 3. Unit fixed effects

Model:

```text
Y_it = βX_it + α_i + u_it
```

`α_i` captures all time-invariant unit characteristics, observed or unobserved.

Demeaning removes `α_i`:

```text
Y_it − Ȳ_i = β(X_it − X̄_i) + (u_it − ū_i)
```

Thus identification comes from within-unit changes.

## 4. Time fixed effects

Add common shocks:

```text
Y_it = βX_it + α_i + λ_t + u_it
```

`λ_t` absorbs shocks affecting all units in a period: national recession, inflation, common technology trend.

Two-way fixed effects combine unit and time FE.

## 5. What fixed effects do not solve

If time-varying confounder affects both X and Y, unit FE does not remove it.

Example: local economic boom increases both public spending and employment. County FE removes permanent county differences but not boom shocks.

## 6. Bad controls remain bad

Panel does not make post-treatment controls safe. Conditioning on mediator or collider after treatment can still bias total effect.

## 7. Fixed effects and measurement error

Within transformation can amplify noise when true X changes slowly but measurement error varies period-to-period.

FE estimates may become more attenuated than cross-sectional estimates under classical measurement error.

## 8. Random effects

Random-effects model treats unit effect as uncorrelated with regressors under stronger assumption:

```text
Cov(α_i, X_it) = 0
```

It uses both within and between variation and can estimate time-invariant regressors.

Choice FE vs RE should be substantive, not only a mechanical Hausman test.

## 9. First differences

For two periods:

```text
ΔY_i = βΔX_i + Δu_i
```

First differencing also removes time-invariant unit effects.

With many periods, FE and FD differ in efficiency and response to serial correlation.

## 10. Difference-in-Differences idea

Suppose one group receives policy and another does not. Compare before-after change in treated to before-after change in control:

```text
DiD = (Y_T,after − Y_T,before)
    − (Y_C,after − Y_C,before)
```

Control group estimates counterfactual trend for treated group absent treatment.

## 11. Parallel trends

Core assumption:

```text
E[Y_T(0,after) − Y_T(0,before)]
=
E[Y_C(0,after) − Y_C(0,before)]
```

Treated and control need not have same levels. They need comparable untreated trends for relevant period.

Parallel trends is about counterfactual outcomes and cannot be fully tested after treatment.

## 12. Two-period regression form

A standard model:

```text
Y_it = α + βTreated_i + γPost_t
     + δ(Treated_i × Post_t) + u_it
```

`δ` is DiD estimate under assumptions.

With unit/time FE, time-invariant group dummy and common post dummy are absorbed.

## 13. Pre-trends

Plot and estimate event-time coefficients before treatment. Large pre-treatment divergence threatens parallel trends.

But failure to reject pre-trends does not prove parallel trends: pre-period may be noisy/short, and anticipation can start before formal treatment.

## 14. Event study

Event-study specification estimates dynamic effects relative to treatment time:

```text
Y_it = α_i + λ_t + Σ_k β_k 1[event time = k] + u_it
```

Pre-treatment coefficients diagnose trends/anticipation; post coefficients show dynamics.

Reference period must be omitted.

## 15. Staggered adoption problem

When units adopt treatment at different times, classic two-way fixed-effects DiD can use already-treated units as controls for later-treated units.

With heterogeneous treatment effects over cohorts/time, coefficient may be weighted average with undesirable or negative weights.

Modern DiD methods compare appropriate not-yet-treated/never-treated groups and aggregate cohort-time effects explicitly.

## 16. Treatment-effect heterogeneity

Policy effect may grow over time or vary across cohorts. A single TWFE coefficient can obscure this.

Report dynamic/cohort-specific effects when substantive.

## 17. Never-treated vs not-yet-treated controls

Never-treated group can be useful if comparable. If all units eventually treated, not-yet-treated units provide temporary controls.

Need avoid using post-treated outcomes as untreated counterfactual.

## 18. Anticipation

If firms/households change behavior when policy announced before implementation, “pre-treatment” window after announcement is already affected.

Treatment timing should follow information exposure, not only legal effective date.

## 19. Spillovers

Policy in one region may affect neighboring control region through labor mobility, trade or prices.

Spillovers violate stable control condition and can attenuate or reverse DiD estimate.

## 20. Composition changes

If treatment changes who remains in sample, observed group outcome can shift even without individual outcome change.

Examples: migration after local tax, school enrollment after reform, firm exit after regulation.

Track population/composition alongside outcome.

## 21. Differential shocks

A local shock coinciding with treatment can mimic policy effect. Controls for measured shocks may help, but design needs institutional argument and alternative comparison groups.

## 22. Triple differences

Difference-in-Difference-in-Differences adds a third dimension to net out another differential trend.

Example compare treated vs control regions, before vs after, and eligible vs ineligible group.

DDD needs its own parallel-trends-style assumptions and can become hard to interpret.

## 23. Synthetic control

When one/few aggregate units are treated, synthetic control constructs weighted combination of untreated units matching pre-treatment outcomes/covariates.

It makes counterfactual transparent but requires good donor pool and long enough pre-period.

## 24. Synthetic-control risks

Poor pre-treatment fit weakens credibility. Donor contamination, interpolation outside convex hull or structural breaks also matter.

Placebo-in-space/time helps assess unusual post-treatment divergence.

## 25. Interactive fixed effects

Simple unit/time FE assume common time shocks plus unit constants. If latent factors affect units differently over time, interactive-factor models can capture richer trends:

```text
λ_i' f_t
```

But added flexibility raises identification/model-selection demands.

## 26. Clustered inference in DiD

Policy assigned at state/firm/school level creates within-cluster serial dependence.

SE usually clustered at treatment-assignment level. Few clusters require special methods such as wild-cluster bootstrap or randomization-based approaches depending design.

## 27. Serial correlation and false significance

Persistent outcomes and treatments make naive SE badly understated in policy panels.

Long time series per unit do not equal many independent treatment shocks.

## 28. Unit-specific trends

Adding linear unit trends can absorb differential pre-trends but may also absorb genuine treatment dynamics and rely heavily on functional form.

Use only with substantive justification and show sensitivity.

## 29. Fixed effects as design, not cleaning trick

Adding hundreds of FE does not automatically make regression causal. Every FE changes which variation identifies coefficient.

Ask: after absorbing these dimensions, what variation remains, and why is it exogenous?

## 30. Failure modes

Sai lầm thứ nhất là nói unit FE controls every unobserved confounder.

Sai lầm thứ hai là infer parallel trends just because pre-trend p-values > 0.05.

Sai lầm thứ ba là use classic TWFE with staggered adoption/heterogeneous effects without checking weights.

Sai lầm thứ tư là ignore anticipation/spillovers/composition.

Sai lầm thứ năm là cluster SE at individual level when treatment assigned at policy level.

Sai lầm thứ sáu là add unit trends mechanically until desired result appears.

## 31. Mental model

Khi đọc panel/DiD, hãy hỏi:

1. Identification dùng within hay between variation?
2. Unit/time FE absorb gì và không absorb gì?
3. Treatment timing và announcement timing khác nhau không?
4. Counterfactual trend đến từ group nào?
5. Pre-trends informative đến mức nào?
6. Adoption có staggered không, effect có heterogeneous không?
7. Controls đã từng treated có bị dùng sai không?
8. Spillover/migration/composition có phá comparison không?
9. Cluster level có khớp assignment không?
10. Event-study dynamics có economic mechanism hợp lý không?

Panel methods tận dụng space × time variation. Với macro/financial data, dependence qua thời gian tự thân trở thành object cần model. Chapter tiếp theo đi vào time series, forecasting và macro identification.
