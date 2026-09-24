# Robustness, External Validity & Research Workflow — Từ estimate đến kết luận đáng tin

Một econometric estimate không kết thúc analysis. Sau point estimate cần hỏi: result có phụ thuộc một specification duy nhất không, assumptions nào dễ vỡ, uncertainty nào chưa nằm trong standard error, và effect có áp dụng được ngoài sample/context hay không? Robustness không phải chạy hàng trăm regressions cho đến khi coefficient “ổn”; nó là kiểm tra có hệ thống những threats xuất phát từ design.

## 1. Identification trước robustness

Robustness không cứu được design sai từ đầu.

Nếu instrument vi phạm exclusion, sample selection severe hoặc treatment timing sai, thêm controls/specifications chỉ thay hình thức.

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

Một result có thể được estimate dưới nhiều reasonable choices: control set, sample window, functional form, clustering, outcome definition.

Specification curve/multiverse analysis hiển thị distribution of estimates across defensible specifications.

Mục tiêu là transparency, không phải đếm bao nhiêu regression significant.

## 3. Robustness phải có lý do

Mỗi robustness check nên map tới threat:

- alternative bandwidth → RDD local-fit sensitivity;
- alternative control group → DiD parallel-trend concern;
- clustered SE → correlated shocks;
- alternate outcome definition → measurement sensitivity;
- leave-one-region-out → influential unit;
- placebo timing → anticipation/common trends.

Randomly changing model without threat model tạo noise, không tạo credibility.

## 4. Falsification tests

A strong design makes predictions where effect **should not** appear.

Examples:

- pre-treatment effect should be absent;
- ineligible group should not react;
- placebo cutoff should show no discontinuity;
- negative-control outcome should not change.

Failure indicates alternative explanation; passing supports but does not prove identification.

## 5. Balance tests

In randomized/RDD settings, pre-treatment covariates should be balanced in expectation or smooth across cutoff.

Do not mechanically require every covariate p-value > 0.05. With many variables, some imbalance occurs by chance; focus on magnitude/joint patterns and design.

## 6. Sensitivity to unobserved confounding

Observational selection-on-observables designs rely on no hidden confounding after X.

Sensitivity analysis asks how strong an omitted variable would need to be to explain estimate.

This turns vague “maybe omitted variables” into quantitative threat assessment, while still not proving absence of confounding.

## 7. Bounds

When point identification requires implausibly strong assumptions, partial identification may provide credible bounds.

Examples: attrition bounds, worst-case missing outcomes, monotonicity-based bounds.

A wider honest interval can be more informative than a precise but fragile point estimate.

## 8. Influence and leverage

Some observations have disproportionate influence because X is extreme or residual large.

Check leverage, influence statistics, leave-one-out/group-out estimates and data errors.

But do not remove influential observations solely because they weaken desired result.

## 9. Outliers

Outlier may be measurement error or genuine tail event. Treatment depends on context.

Winsorizing changes estimand/distribution. Report why cutoff chosen and show raw sensitivity.

## 10. Alternative outcome definitions

If a concept has several valid measures, result should be interpreted relative to each.

Employment can be headcount, hours, payroll, formal jobs. Inflation can headline/core/sector indices.

Consistency across measures strengthens mechanism only if measures capture related but distinct aspects.

## 11. Multiple hypothesis correction

If many outcomes/subgroups are primary tests, control false positives using family-wise error or False Discovery Rate where appropriate.

Pre-specify outcome families; do not retroactively call one significant result “primary”.

## 12. Publication bias

Studies with significant/novel results may be more likely published. Literature can overstate effects even when each paper uses conventional inference.

Meta-analysis should inspect heterogeneity, small-study effects and design quality, not only pooled mean.

## 13. P-hacking and researcher degrees of freedom

Flexible choices after seeing data can generate low p-values without true effect.

Defenses include preregistration, pre-analysis plans, registered reports, code/data transparency and distinction confirmatory vs exploratory analysis.

## 14. Reproducibility

Computational reproducibility means same data/code regenerates result.

It requires versioned data, deterministic transformations where possible, environment documentation, seeds and clear pipeline.

Reproducible does not mean causally valid; it means analysis can be inspected and rerun.

## 15. Replication

Replication asks whether finding survives new sample/data/design.

Direct replication repeats closely; conceptual replication tests same mechanism in different setting.

Failure to replicate can reflect original false positive, contextual heterogeneity, implementation differences or underpowered replication.

## 16. External validity

Effect can vary by:

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

Generalization requires model of effect heterogeneity and comparison between study and target population.

## 17. Transportability

If treatment effect conditional on covariates is stable, reweighting study sample to target covariate distribution can transport effect under assumptions.

But unobserved effect modifiers or institutional differences remain threats.

## 18. Scale-up effects

Small pilot may use best staff, high monitoring and no equilibrium price response. National scale can dilute quality, change wages/rents and alter provider entry.

Scale is treatment version change, not merely larger N.

## 19. General equilibrium vs partial equilibrium

Individual subsidy effect may differ when everyone receives subsidy because market prices adjust.

Micro causal estimate can be internally valid but insufficient for economy-wide policy without equilibrium model/evidence.

## 20. Treatment heterogeneity

Report subgroup effects when motivated by mechanism and sufficiently powered.

Avoid searching dozens of splits then highlighting one large coefficient. Machine-learning heterogeneity methods require honest sample splitting/validation.

## 21. Distributional effects

Average treatment effect can hide winners and losers.

Quantile treatment effects, outcome distribution or subgroup effects may be necessary when equity/risk matters.

But quantile effects need careful interpretation because individuals at same quantile are not necessarily same units across counterfactual distributions.

## 22. Mechanism evidence

A reduced-form effect can be policy-relevant without fully proving mechanism.

Mediator outcomes, timing patterns and heterogeneous response can support mechanism, but post-treatment variables require care.

Distinguish:

```text
Treatment affects Y
vs.
Treatment affects Y specifically through M
```

The second claim needs additional assumptions/evidence.

## 23. Economic significance

Translate estimates to natural units and compare with baseline, costs and feasible alternatives.

Example:

```text
+0.1 SD test score
```

needs context: baseline distribution, persistence, intervention cost and comparison to other programs.

## 24. Cost-effectiveness

A causal effect is not a policy recommendation by itself.

Cost-effectiveness:

```text
Effect / Cost
```

helps compare interventions with same outcome. Cost-benefit requires monetizing broader benefits/costs and distribution assumptions.

## 25. Statistical vs decision uncertainty

Policy decision depends not only confidence interval but asymmetric costs of errors, option value, irreversibility and learning.

A small uncertain benefit may justify experiment if reversible/cheap; same uncertainty may not justify irreversible costly policy.

## 26. Bayesian interpretation

Bayesian analysis combines prior and likelihood to form posterior.

It can express probability over parameters conditional on model/prior, but conclusions depend on prior and model assumptions.

Bayesian credible intervals and frequentist confidence intervals answer different probability statements.

## 27. Model averaging and model uncertainty

If several plausible models exist, conditioning on one ignores model uncertainty.

Model averaging or scenario ranges can help, but no automatic procedure replaces substantive judgment about causal structure.

## 28. Prediction calibration

For predictive models, check calibration, discrimination and out-of-sample stability.

A model can rank risk well but systematically overpredict levels; calibration matters for decisions.

## 29. Distribution shift

Model trained under one regime may fail after technology, policy or behavior changes.

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
2. draw causal structure / institutional timeline;
3. inspect measurement and sample construction;
4. identify source of variation;
5. write main specification before outcome hunting;
6. inspect raw/descriptive data;
7. estimate main effect with design-consistent inference;
8. run threat-specific robustness/falsification;
9. examine heterogeneity/mechanism carefully;
10. translate effect into economic magnitude;
11. state external-validity and policy limits;
12. package reproducible code/data documentation.

## 32. Reading a paper efficiently

Khi đọc empirical paper, không bắt đầu từ coefficient table. Đọc theo thứ tự:

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

Nếu design không credible, precision của table phía sau không cứu được conclusion.

## 33. Red flags

Các red flags mạnh gồm:

- causal language nhưng không có assignment/counterfactual argument;
- many controls được mô tả như proof of causality;
- treatment timing mơ hồ;
- no raw trends around DiD/RDD design;
- IV without exclusion story;
- clustered treatment nhưng iid SE;
- only significant outcomes reported;
- result depends one narrow specification without justification;
- extrapolation far beyond support/sample;
- policy recommendation không discuss costs/equilibrium/distribution.

## 34. Failure modes

Sai lầm thứ nhất là equate robustness with many regressions.

Sai lầm thứ hai là let robustness replace identification.

Sai lầm thứ ba là report only standard error and ignore model/design uncertainty.

Sai lầm thứ tư là generalize local/RCT effect mechanically to national scale.

Sai lầm thứ năm là infer mechanism from mediator correlation.

Sai lầm thứ sáu là turn causal estimate directly into policy recommendation without costs/trade-offs.

## 35. Mental model

Trước khi tin một empirical conclusion, hãy hỏi:

1. Estimand và counterfactual có rõ không?
2. Source of variation thật sự là gì?
3. Assumption yếu nhất nằm ở đâu?
4. Robustness checks có target đúng threats không?
5. Result có driven bởi vài observations/groups không?
6. Multiple testing/specification search được xử lý thế nào?
7. Effect size economic meaningful không?
8. Mechanism được identified hay chỉ suggested?
9. Sample effect có transport/scale được không?
10. Data/code/result có reproducible và transparent không?

Econometrics không phải toolkit để làm coefficient “đẹp”. Nó là discipline buộc economic claim phải nói rõ measurement, counterfactual, source of variation, uncertainty và phạm vi kết luận. Với foundation này, Applied Economics có thể được xây trên cả theory lẫn empirical identification thay vì case narrative.
