# Causal Inference & Experiments — Counterfactual, randomization và selection

Causal inference hỏi một câu rất cụ thể: **outcome sẽ khác thế nào nếu treatment thay đổi, trong khi counterfactual relevant được xây dựng đáng tin?** Randomized experiment là benchmark vì assignment mechanism có thể làm treatment independent of potential outcomes. Observational methods cố tái tạo một phần logic đó bằng assumptions và institutional variation.

## 1. Fundamental problem of causal inference

Mỗi unit có potential outcomes:

```text
Y_i(1), Y_i(0)
```

Nhưng chỉ quan sát:

```text
Y_i = D_iY_i(1) + (1−D_i)Y_i(0)
```

Causal effect của individual không directly observable. Ta cần comparison group đại diện cho missing potential outcome.

## 2. Selection bias decomposition

Naive difference:

```text
E[Y | D=1] − E[Y | D=0]
```

có thể decomposed thành treatment effect plus selection difference.

Treated group thường khác untreated group trước treatment. Wage difference giữa college graduates và non-graduates không chỉ là schooling effect; ability, family background và preferences cùng influence selection.

## 3. Random assignment

Nếu treatment randomly assigned:

```text
D ⟂ {Y(1), Y(0)}
```

thì untreated outcomes of control group provide unbiased counterfactual on average.

Randomization không làm groups identical trong từng sample; nó làm imbalance stochastic và quantifiable.

## 4. Randomization inference

Under sharp null of no treatment effect for every unit, treatment labels có thể được permuted according to assignment mechanism để derive exact/randomization distribution.

This emphasizes design rather than asymptotic regression assumptions.

## 5. Intent-to-Treat

Intent-to-Treat (ITT) compares outcomes by assigned treatment, regardless of compliance:

```text
ITT = E[Y | Z=1] − E[Y | Z=0]
```

where `Z` is assignment.

ITT answers effect of offering/assigning treatment under real compliance behavior and preserves randomization.

## 6. Treatment-on-the-Treated and noncompliance

If assigned participants do not all take treatment, comparing actual takers vs non-takers reintroduces selection.

Random assignment can be used as instrument for actual treatment under additional assumptions, leading to LATE for compliers.

## 7. Attrition

Randomization at baseline does not protect against differential attrition after assignment.

If treated low-outcome units drop out more often, observed treatment mean becomes biased.

Report attrition by arm, reasons, bounds/sensitivity and use administrative follow-up where possible.

## 8. Spillovers and contamination

Control units may indirectly receive treatment through peers, markets or information.

Then standard treatment-control difference estimates effect under contamination rather than isolated treatment.

Cluster randomization or exposure mapping may be necessary.

## 9. Cluster randomization

Treatment may be assigned to schools, villages, hospitals or firms rather than individuals.

Effective independent sample size is number of clusters, not raw individuals. Intra-cluster correlation reduces power.

Design and SE must match assignment level.

## 10. Stratification and blocking

Randomization within pre-defined blocks (region, baseline outcome, size) can improve balance and precision.

Analysis should account for design. Post-hoc subgroup creation is different from pre-randomization blocking.

## 11. Power and minimum detectable effect

Study design should ask what effect size can be detected before collecting data.

Power depends on:

```text
sample size
variance
treatment share
cluster structure
baseline predictive covariates
true effect size
```

Underpowered experiment may produce noisy estimates rather than clear “no effect”.

## 12. Baseline adjustment

Including strongly predictive pre-treatment outcomes can improve precision without threatening randomization.

But post-treatment controls should not be added mechanically.

## 13. Multiple outcomes and treatment arms

Many outcomes/arms increase false positives. Pre-specify primary outcomes and adjust families when appropriate.

Exploratory outcomes are useful if labeled exploratory.

## 14. External validity

RCT identifies effect for study sample, treatment version and implementation context.

Scaling can change prices, provider quality, equilibrium behavior and political responses. A village pilot may not predict national rollout.

External validity is a separate causal question.

## 15. Hawthorne and experiment effects

Subjects/providers may change behavior because they know they are observed. Treatment delivery in trial may be more intensive than real program.

Implementation fidelity and naturalistic settings matter.

## 16. Ethical and practical constraints

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

Exact matching is difficult with many dimensions. Distance or propensity-score methods reduce dimensionality but do not solve hidden confounding.

## 19. Propensity score

```text
e(X) = P(D=1 | X)
```

Under conditional independence and overlap, conditioning on propensity score can balance distribution of observed X.

Propensity score is not “probability treatment caused outcome”.

## 20. Propensity-score pitfalls

Good propensity model predicts treatment assignment for balance, not necessarily outcome.

Including instruments or post-treatment variables may worsen performance. Trimming extreme scores changes target population.

Balance diagnostics matter more than classification accuracy.

## 21. Inverse probability weighting

ATE weighting uses roughly:

```text
D/e(X) + (1−D)/(1−e(X))
```

to create pseudo-population balanced on observed covariates.

Extreme propensity scores create huge weights and variance. Positivity/overlap is substantive, not merely numerical.

## 22. Regression adjustment

Outcome model estimates conditional outcomes then averages counterfactual predictions.

Correct specification can identify under selection-on-observables. Flexible models help but hidden confounding remains.

## 23. Doubly robust estimators

Augmented IPW combines treatment model and outcome model. Under conditions, estimator remains consistent if one of the two nuisance models is correctly specified.

“Doubly robust” does not protect against unmeasured confounding or violations of positivity.

## 24. Difference in means vs regression in RCT

Simple difference in means is design-unbiased under randomization.

Regression can improve precision and handle stratification, but complicated controls should not obscure the assignment mechanism.

## 25. Natural experiments

Natural experiment arises when institution/event creates variation plausibly unrelated to potential outcomes, such as lottery, rule threshold, timing or geography.

Label “natural experiment” is not enough. Need explain exact assignment mechanism and threats.

## 26. Placebo tests

If treatment supposedly starts at time T, finding “effect” before T threatens design.

Placebo outcomes or populations unaffected by mechanism can test alternative explanations, though passing placebo does not prove validity.

## 27. Negative controls

A negative-control outcome should not causally respond to treatment; negative-control exposure should not affect outcome.

Unexpected association can reveal residual confounding or measurement problems.

## 28. Sensitivity analysis

Because unobserved confounding cannot be fully tested, quantify how strong hidden bias would need to be to overturn conclusion.

Sensitivity should complement, not replace, substantive design reasoning.

## 29. Mediation vs total effect

If treatment works through mediator M:

```text
D → M → Y
```

Total effect includes mediated path. Conditioning on M changes estimand and may introduce post-treatment bias.

Mediation analysis requires stronger assumptions than total-effect estimation.

## 30. Heterogeneous treatment effects

Average effect may hide subgroup differences.

Pre-specified heterogeneity by baseline risk, age, firm size or region can matter for policy. Data-driven subgroup discovery needs validation to avoid overfitting.

## 31. Equilibrium effects

Large-scale policy can change wages, prices, rents or entry. Individual-level experiment may capture partial-equilibrium effect only.

Scaling micro treatment into macro policy requires market-response model or larger-scale evidence.

## 32. Failure modes

Sai lầm thứ nhất là compare treated vs untreated actual participation when compliance selective.

Sai lầm thứ hai là nghĩ randomization solves attrition/spillovers automatically.

Sai lầm thứ ba là dùng propensity score như magic cure for confounding.

Sai lầm thứ tư là ignore overlap and extreme weights.

Sai lầm thứ năm là generalize RCT beyond population/scale without mechanism.

Sai lầm thứ sáu là control mediator while claiming total effect.

## 33. Mental model

Khi đọc causal study, hãy hỏi:

1. Treatment assignment mechanism là gì?
2. Missing counterfactual được approximated bởi group nào?
3. Randomization/conditional independence có credible không?
4. Compliance, attrition và spillovers ra sao?
5. Unit/cluster assignment và SE có khớp không?
6. Overlap có đủ không?
7. Estimand là ITT, ATE, ATT hay local effect?
8. Placebo/negative controls nói gì?
9. Scale-up có equilibrium effect không?
10. External validity dựa mechanism nào?

Experiments là benchmark, nhưng many economic questions rely on endogenous choices. Chapter tiếp theo xử lý các designs dùng instruments và thresholds để isolate exogenous variation.
