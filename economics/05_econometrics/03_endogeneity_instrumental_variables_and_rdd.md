# Endogeneity, Instrumental Variables & RDD — Khi treatment không exogenous

Endogeneity xuất hiện khi regressor liên quan với error term theo cách làm coefficient không còn phản ánh causal effect cần tìm. Sources chính gồm omitted variables, simultaneity/reverse causality, measurement error và endogenous selection. Instrumental Variables (IV) và Regression Discontinuity Design (RDD) là hai strategies quan trọng để tìm variation treatment có causal interpretation rõ hơn, nhưng cả hai chỉ mạnh khi institutional assumptions thật sự credible.

## 1. Endogeneity là vấn đề về source of variation

Simple regression:

```text
Y = βD + u
```

Muốn đọc `β` causal, cần variation của D không đi cùng unobserved determinants của Y.

Nếu:

```text
Cov(D,u) ≠ 0
```

OLS generally biased/inconsistent cho causal parameter.

## 2. Omitted-variable endogeneity

Nếu ability ảnh hưởng cả education và wage, regression wage on schooling omitting ability mixes schooling effect với selection on ability.

Adding a proxy can reduce bias only if proxy sufficiently captures confounder and does not introduce bad-control paths.

## 3. Simultaneity

Price và quantity determined together by supply and demand. Regressing quantity on observed price without a demand/supply shifter does not recover demand curve because price reacts to shocks in both curves.

This is classic identification problem: equilibrium correlation is not structural slope.

## 4. Reverse causality

Crime may affect police deployment while police affects crime. Health affects income while income affects health.

Timing alone may not solve if anticipatory behavior or persistent shocks exist.

## 5. Measurement-error endogeneity

Classical error in explanatory variable creates correlation between observed regressor and composite error, often attenuating OLS.

A valid instrument correlated with true X but independent of measurement error can sometimes solve this.

## 6. Instrumental-variable idea

An instrument `Z` changes treatment `D` but affects outcome `Y` only through D, under assumptions.

Two core requirements:

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

Interpretation: effect of instrument on outcome divided by effect of instrument on treatment.

## 8. Two-Stage Least Squares

2SLS first predicts treatment using instruments:

```text
D̂ = projection of D on Z and controls
```

Then relates Y to instrument-induced component of D.

Mental model: IV discards endogenous variation in D and uses only variation moved by Z.

## 9. Weak instruments

If first stage is weak, IV estimates can be noisy, biased toward OLS in finite samples and inference unreliable.

First-stage F-statistic is a diagnostic, but simple rules like “F>10 always enough” are context-dependent, especially multiple instruments/heteroskedasticity.

Report first-stage strength and weak-IV-robust inference when relevant.

## 10. Exclusion restriction

Suppose distance to college instruments education. Exclusion requires distance affects earnings only through schooling, not local labor markets, family location selection or urban opportunities.

A statistically strong first stage does nothing to validate exclusion.

## 11. Independence

Instrument must be as-good-as-random relative to potential outcomes, often conditional on controls.

Policy eligibility, lottery or historical assignment may provide stronger case than arbitrary proxy.

## 12. Monotonicity and LATE

With heterogeneous treatment effects and noncompliance, IV often identifies Local Average Treatment Effect for **compliers** if monotonicity holds: instrument does not push some units toward treatment while pushing others away in opposite way.

Thus IV effect may not equal ATE.

## 13. Compliers, always-takers, never-takers, defiers

Under binary assignment/treatment:

- compliers follow assignment;
- always-takers take regardless;
- never-takers never take;
- defiers do opposite.

Monotonicity rules out defiers. LATE applies to compliers whose treatment is changed by instrument.

## 14. External validity of IV

Different instruments move different populations/margins. Draft lottery may identify effect for people induced by draft risk; college-distance instrument for marginal students near access boundary.

Two valid IVs can estimate different local effects without contradiction.

## 15. Overidentification tests

With more instruments than endogenous regressors, overidentification tests check whether instrument-implied moments jointly fit model.

Passing test does not prove all instruments valid; tests have power/model dependence and invalid instruments can fail in offsetting ways.

## 16. Many instruments

Adding many weak instruments can overfit first stage and worsen bias. Instrument count should follow credible sources of variation, not “more is better”.

## 17. Control-function intuition

Some endogeneity models explicitly estimate selection/endogenous residual then include correction term in outcome equation.

Control functions can be useful in nonlinear settings but need structural assumptions comparable in seriousness to IV.

## 18. Regression Discontinuity Design

RDD exploits treatment assignment changing discontinuously at a threshold of running variable:

```text
D = 1 if X ≥ c
```

If potential outcomes evolve smoothly through cutoff absent treatment, outcome jump at cutoff identifies a local causal effect.

## 19. Sharp vs fuzzy RDD

Sharp RDD: treatment status changes deterministically at threshold.

Fuzzy RDD: probability of treatment jumps but compliance imperfect. Cutoff indicator becomes instrument for actual treatment.

Fuzzy RDD therefore has IV/LATE interpretation near threshold.

## 20. Local nature of RDD

RDD identifies effect for units near cutoff, not necessarily far away.

Scholarship cutoff effect for students scoring around 80 does not automatically generalize to students scoring 50 or 100.

## 21. Continuity assumption

Key assumption: other determinants of outcome change smoothly at cutoff.

If another policy begins at same threshold, outcome discontinuity cannot be attributed cleanly to treatment of interest.

## 22. Manipulation of running variable

If units can precisely sort around cutoff, groups just above/below may differ systematically.

Examples: income reported just below eligibility threshold, test score manipulation, firms changing size to avoid regulation.

Density tests and institutional knowledge help assess sorting.

## 23. Bandwidth choice

Use observations near cutoff to improve comparability, but too narrow means high variance; too wide means functional-form bias.

Modern RDD uses data-driven bandwidth procedures and local polynomial estimation rather than high-order global polynomials.

## 24. Polynomial warning

High-order polynomial fits can behave wildly near boundaries and give misleading confidence intervals.

Prefer local linear/quadratic specifications with transparent bandwidth sensitivity.

## 25. RDD plots

A good plot shows binned outcomes and local fitted trends around cutoff, but visual bin choices can manipulate appearance.

Plot supports design; formal estimate/inference should not depend solely on eye inspection.

## 26. Covariate balance near cutoff

Pre-treatment covariates should not show suspicious jumps at cutoff under credible RDD.

Balance is diagnostic, not proof.

## 27. Placebo cutoffs

Estimate discontinuities at fake thresholds where no treatment changes. Effects there may suggest functional-form or other institutional problems.

## 28. Regression kink design

Instead of level jump, policy may change slope of treatment at threshold. Regression Kink Design uses discontinuity in derivative under stronger smoothness assumptions.

It is more sensitive to functional form and power.

## 29. Instrument vs control confusion

A control blocks confounding by conditioning. An instrument supplies exogenous treatment variation and generally should not directly affect outcome.

A strong predictor of Y is not automatically a good instrument; often the opposite, because direct prediction threatens exclusion.

## 30. Structural interpretation

IV/RDD estimate specific local causal parameters. To predict effects of policy changes beyond observed margin, structural model or stronger assumptions may be needed.

Do not call a local estimate “universal elasticity” without justification.

## 31. Failure modes

Sai lầm thứ nhất là chọn instrument chỉ vì correlated strongly with treatment.

Sai lầm thứ hai là test exclusion restriction bằng p-value rồi coi validated.

Sai lầm thứ ba là bỏ weak-instrument problem.

Sai lầm thứ tư là report IV as ATE when it is LATE.

Sai lầm thứ năm là extrapolate RDD effect far from cutoff.

Sai lầm thứ sáu là use high-order polynomial mechanically.

Sai lầm thứ bảy là ignore manipulation/coincident policies at threshold.

## 32. Mental model

Khi dùng IV/RDD, hãy hỏi:

1. Endogeneity source cụ thể là gì?
2. Instrument thay đổi treatment bằng mechanism nào?
3. First stage đủ mạnh không?
4. Exclusion restriction có plausible theo institution không?
5. Population of compliers là ai?
6. Effect local ở margin nào?
7. RDD cutoff có manipulable không?
8. Có policy/shock khác cùng cutoff không?
9. Result stable across reasonable bandwidth/specifications không?
10. Policy question có cần extrapolate beyond identified local effect không?

IV và RDD dùng special variation. Một family khác tận dụng variation across units and time: panel fixed effects và Difference-in-Differences.
