# Lấy mẫu, ước lượng, confidence interval và hypothesis testing: inference từ dữ liệu hữu hạn

Thống kê suy luận (statistical inference / 통계적 추론) bắt đầu từ một giới hạn cơ bản: ta muốn biết điều gì đó về một population hoặc process lớn, nhưng chỉ quan sát một sample hữu hạn.

Do đó mọi inference phải giữ rõ bốn lớp:

```text
population / process
→ sampling mechanism
→ observed sample
→ uncertainty about target quantity
```

Sai ở sampling mechanism thì formula phía sau có thể rất chính xác nhưng vẫn trả lời sai câu hỏi.

## 1. Population, sample, parameter và statistic

Population là target process hoặc tập đối tượng ta muốn hiểu.

Parameter là quantity của population, ví dụ:

```math
\mu,\quad \sigma^2,\quad p.
```

Sample:

```math
X_1,\ldots,X_n.
```

Statistic là function của sample:

```math
T=T(X_1,\ldots,X_n).
```

Ví dụ sample mean:

```math
\bar X
=\frac1n\sum_{i=1}^{n}X_i.
```

Trong frequentist framework, parameter là fixed unknown; statistic là random trước khi data được quan sát.

## 2. Sampling design quan trọng hơn sample size

Một sample rất lớn nhưng systematically biased có thể estimate sai quantity với precision rất cao.

Ví dụ survey chỉ gửi cho users active trong 7 ngày gần nhất nhưng claim đại diện toàn bộ users.

Increasing `n` giảm random sampling error, nhưng không tự sửa:

- selection bias;
- nonresponse bias;
- measurement bias;
- survivorship bias;
- confounding.

Mental rule:

```text
more data ≠ better identification
```

nếu data-generating/sampling process sai.

## 3. Random sampling tạo bridge từ sample sang population

Simple random sampling idealize rằng mỗi observation được lấy theo mechanism đã biết và representative theo xác suất.

IID assumption thường viết:

```math
X_1,\ldots,X_n\overset{iid}{\sim}F.
```

Nó gói hai assumptions:

```text
identically distributed
independent
```

Real data thường chỉ approximately iid hoặc không iid chút nào. Time series, clusters, repeated measurements và network data cần dependency-aware methods.

## 4. Sampling distribution là distribution của estimator qua repeated samples

Nếu ta lặp toàn bộ sampling procedure nhiều lần, statistic thay đổi.

Distribution đó gọi sampling distribution.

Ví dụ với sample mean:

```math
E[\bar X]=\mu
```

và nếu observations independent cùng variance `\sigma^2`:

```math
\operatorname{Var}(\bar X)=\frac{\sigma^2}{n}.
```

Standard error:

```math
SE(\bar X)=\frac{\sigma}{\sqrt n}.
```

Standard error không phải standard deviation của raw observations. Nó là uncertainty của estimator.

## 5. Vì sao uncertainty giảm theo 1/sqrt(n)?

Average:

```math
\bar X=\frac1n\sum_iX_i.
```

Independent variances add:

```math
\operatorname{Var}\left(\sum_iX_i\right)=n\sigma^2.
```

Divide by `n^2`:

```math
\operatorname{Var}(\bar X)=\frac{\sigma^2}{n}.
```

Take square root:

```math
SE=\frac\sigma{\sqrt n}.
```

Diminishing returns:

```text
2× smaller SE → 4× sample
10× smaller SE → 100× sample
```

## 6. Dependence làm effective sample size nhỏ hơn raw count

Nếu observations positively correlated:

```math
\operatorname{Var}\left(\sum_iX_i\right)
=
\sum_i\operatorname{Var}(X_i)
+2\sum_{i<j}\operatorname{Cov}(X_i,X_j).
```

Positive covariance increases uncertainty.

Một million highly correlated observations có thể chứa ít independent information hơn nhiều so với one million iid observations.

Trong time series, MCMC và clustered experiments, effective sample size quan trọng hơn raw `n`.

## 7. Estimator: rule map sample → estimate

Estimator:

```math
\hat\theta=T(X_1,\ldots,X_n).
```

Các qualities thường xét:

```text
bias
variance
consistency
efficiency
robustness
```

Không có estimator “tốt nhất” independent of loss/model.

## 8. Bias và variance

Bias:

```math
\operatorname{Bias}(\hat\theta)
=E[\hat\theta]-\theta.
```

Variance:

```math
\operatorname{Var}(\hat\theta).
```

Mean squared error:

```math
MSE
=E[(\hat\theta-\theta)^2]
=\operatorname{Var}(\hat\theta)
+\operatorname{Bias}(\hat\theta)^2.
```

Một slightly biased estimator có thể có lower MSE nếu variance giảm nhiều.

Đây là foundation của bias–variance trade-off trong machine learning.

## 9. Consistency là large-sample property

Estimator consistent nếu

```math
\hat\theta_n\to\theta
```

trong suitable probabilistic sense khi `n\to\infty`.

Unbiasedness và consistency khác nhau.

Một estimator có thể biased finite-sample nhưng bias vanish asymptotically.

Một estimator unbiased cũng có thể variance lớn và thực tế poor.

## 10. Standardization tạo pivot-like quantities

Nếu

```math
\bar X\approx N\left(\mu,\frac{\sigma^2}{n}\right),
```

thì

```math
Z=
\frac{\bar X-\mu}{\sigma/\sqrt n}
```

có distribution standard normal under ideal assumptions.

Inference hoạt động bằng cách tìm statistic có distribution known/approximately known không phụ thuộc unknown parameter quá nhiều.

## 11. Confidence interval là procedure, không phải posterior statement

Một 95% frequentist confidence procedure có coverage 95% nếu repeated sampling theo model làm khoảng 95% intervals chứa true parameter.

Sau khi interval cụ thể `[L,U]` được tính, strict frequentist interpretation không nói:

```text
P(θ ∈ [L,U] | observed data) = 0.95
```

Parameter không random trong framework đó.

Meaning là property của procedure qua repeated samples.

## 12. Derive normal mean interval

Nếu `\sigma` known và sample mean normal/CLT justified:

```math
\frac{\bar X-\mu}{\sigma/\sqrt n}
\sim N(0,1).
```

Với

```math
P(-z_{0.975}\le Z\le z_{0.975})=0.95,
```

rearrange:

```math
\bar X-z_{0.975}\frac\sigma{\sqrt n}
\le\mu\le
\bar X+z_{0.975}\frac\sigma{\sqrt n}.
```

CI formula đến từ probability statement về standardized estimator, không phải rule memorization.

## 13. Student t xuất hiện khi σ unknown

Khi population normal và `\sigma` unknown, thay bằng sample standard deviation `s` làm extra uncertainty.

Statistic:

```math
T=
\frac{\bar X-\mu}{s/\sqrt n}
```

follow Student t distribution with `n-1` degrees of freedom under assumptions.

T tails heavier than normal, reflecting uncertainty from estimating `\sigma`.

As `n` grows, t approaches normal.

## 14. Confidence interval width phản ánh three ingredients

Roughly:

```text
CI width
≈ critical value × standard error
```

Width increases with:

- higher noise;
- higher confidence level;
- dependence/design effect.

Width decreases with:

- larger effective sample size.

Narrow interval không guarantee unbiased sampling.

## 15. Bootstrap: approximate sampling distribution bằng resampling

Bootstrap resamples observed data with replacement để mimic repeated sampling under empirical distribution.

Workflow:

```text
sample data
→ resample many times
→ recompute statistic
→ approximate estimator distribution
```

Useful khi analytic SE khó.

Nhưng bootstrap không automatically fix nonrepresentative data hoặc severe dependency; resampling scheme phải match data structure.

## 16. Hypothesis testing là calibration của extremeness under H0

Null hypothesis:

```math
H_0:\theta=\theta_0.
```

Choose test statistic `T` whose distribution under `H_0` is known/approximated.

Observe `t_{obs}`.

P-value asks:

> Nếu `H_0` và assumptions đúng, probability thấy statistic at least as extreme as observed là bao nhiêu?

Form depends one-sided/two-sided test.

## 17. P-value không phải probability H0 đúng

Wrong interpretation:

```text
p = 0.03 → H0 chỉ có 3% chance đúng
```

Frequentist p-value là:

```math
P(\text{data/test statistic at least this extreme}\mid H_0).
```

Nó không đảo conditioning.

Để nói posterior probability of hypothesis cần prior/model, như Bayesian inference.

## 18. Significance level α là decision-rule error calibration

Test rule:

```text
reject H0 if p ≤ α
```

Under exact test assumptions và true `H_0`, long-run Type I error rate được control gần `\alpha`.

`\alpha=0.05` không phải law of nature. Nó là convention/decision threshold và phải liên hệ cost of false positives.

## 19. Type I, Type II và power

Type I:

```text
reject true H0
```

probability controlled by `\alpha`.

Type II:

```text
fail to reject H0 when alternative true
```

probability `\beta` for specified alternative.

Power:

```math
1-\beta.
```

Power depends on:

```text
effect size
noise
sample size
test threshold
design
```

## 20. Non-significant result ≠ evidence of no effect

If p-value > 0.05, data may be:

- consistent with no effect;
- too noisy;
- underpowered;
- poorly measured;
- affected by design issues.

To claim equivalence/no practically meaningful effect, use equivalence/noninferiority framework or interval relative to practical threshold.

Absence of significance is not automatically significance of absence.

## 21. Statistical significance vs practical significance

With huge sample, tiny effect can have tiny p-value.

Example:

```text
conversion 10.00% → 10.05%
```

Could be statistically certain but business value depends traffic, margin and implementation cost.

Always pair inference with effect size and uncertainty interval.

## 22. Effect size creates domain scale

Examples:

- mean difference in original units;
- standardized mean difference;
- risk ratio;
- odds ratio;
- absolute risk difference.

Different effect measures answer different questions.

A p-value alone lacks practical scale.

## 23. One-sided vs two-sided tests must be chosen before seeing data

Two-sided alternative:

```math
H_1:\theta\ne\theta_0.
```

One-sided:

```math
H_1:\theta>\theta_0.
```

Choosing direction after seeing result inflates false-positive risk.

Test design must be specified independently of favorable observed outcome.

## 24. Multiple testing creates false discovery pressure

Run 100 independent null tests at `\alpha=0.05`; expected false rejections about 5.

Probability of at least one false positive can be high.

Bonferroni controls family-wise error:

```math
\alpha_{each}=\frac\alpha m.
```

Benjamini–Hochberg controls false discovery rate under assumptions and is less conservative for discovery settings.

Different corrections optimize different error goals.

## 25. Optional stopping and repeated peeking can inflate Type I error

If team repeatedly checks p-value after every new user and stops when `p<0.05`, ordinary fixed-sample test calibration no longer holds.

Sequential testing requires sequentially valid methods or alpha-spending designs.

A/B testing platforms need explicit treatment of repeated looks.

## 26. Power analysis before experiment

Before collecting data, choose:

```text
minimum effect of interest
noise/baseline rate
α
required power
```

Then calculate sample size.

This forces experimental design to encode practical significance before results are known.

## 27. A/B test for proportions

Suppose control conversion `p_A`, treatment `p_B`.

Estimate difference:

```math
\hat\Delta=\hat p_B-\hat p_A.
```

Standard error approximately:

```math
SE(\hat\Delta)
\approx
\sqrt{
\frac{\hat p_A(1-\hat p_A)}{n_A}
+
\frac{\hat p_B(1-\hat p_B)}{n_B}
}.
```

CI for difference gives both direction and plausible magnitude.

Business decision should consider expected value/cost, not only significance.

## 28. Randomization supports causal identification

Random assignment makes treatment independent of pre-treatment confounders **in expectation**.

This supports causal comparison between groups if:

- assignment implemented correctly;
- interference limited per design assumptions;
- attrition/noncompliance handled;
- outcome measurement comparable.

Randomization is design tool, not magic aftercare.

## 29. Observational adjustment requires stronger assumptions

Regression/control can adjust measured confounders.

But unmeasured confounding remains possible.

No statistical test can reconstruct randomization from nothing without causal assumptions.

Inference precision and causal identification are separate dimensions.

## 30. Clustered data need clustered uncertainty

If users are grouped by company/school/device household and outcomes correlated within groups, treating every row independent underestimates uncertainty.

Methods include cluster-robust SE, multilevel models or cluster randomization.

Unit of randomization and unit of analysis must align.

## 31. Time series invalidate naive iid intervals

Daily metrics often autocorrelated.

If

```math
X_t
```

correlated over time, ordinary `\sigma/\sqrt n` can understate standard error.

Need time-series/blocked bootstrap/HAC-style methods depending setup.

Raw row count is not effective independent information count.

## 32. Missing data mechanism matters

Missing completely at random, missing at random and missing not at random imply different identification assumptions.

Dropping missing rows can bias estimates if missingness depends on outcome-related variables.

“Clean data” via deletion can silently change target population.

## 33. Measurement error can attenuate relationships

If predictor measured with noise, naive regression slope often biased toward zero under classical measurement-error setup.

More sample does not remove systematic measurement error.

Statistics depends on measurement quality upstream.

## 34. Robustness: mean-based inference can be sensitive to tails

Heavy-tailed/outlier-prone data can make sample mean unstable.

Alternatives include:

- median;
- trimmed mean;
- robust M-estimators;
- transformed scale;
- bootstrap with caution.

Estimator should match distribution and loss, not tradition.

## 35. Bayesian credible interval answers a different probability question

Bayesian posterior interval may satisfy:

```math
P(\theta\in[L,U]\mid D)=0.95
```

under prior + likelihood model.

Frequentist confidence interval has repeated-sampling coverage interpretation.

Both can produce numerically similar intervals in some regimes but philosophical/technical conditioning differs.

## 36. Confidence sequence for anytime-valid inference

A confidence sequence is a sequence of intervals designed so that coverage holds simultaneously over time under conditions:

```text
valid even when stopping time is data-dependent
```

This is useful for continuously monitored online experiments.

It solves a different problem from fixed-horizon CI.

## 37. Reproducibility and pre-registration

Research/product analysis becomes biased if teams try many metrics, filters and windows then report only favorable result.

Pre-specifying primary metric/hypothesis and analysis plan reduces researcher degrees of freedom.

Multiple testing correction alone does not solve every selective reporting issue.

## 38. Confidence interval as inversion of hypothesis tests

For many standard procedures, a `1-\alpha` CI contains exactly parameter values not rejected by corresponding two-sided level-`\alpha` tests.

This shows intervals and tests are two views of the same inferential geometry:

```text
CI → plausible parameter region under procedure
Test → evaluate one parameter value against data
```

## 39. Likelihood viewpoint connects estimation and testing

Likelihood:

```math
L(\theta)=p(D\mid\theta).
```

MLE chooses parameter maximizing likelihood.

Likelihood-ratio tests compare how well constrained vs unconstrained parameter spaces explain data.

This creates a bridge to the library chapter on MLE/MAP/model selection.

## 40. Worked example: why sample size cannot repair bias

Suppose true population approval is 50%, but sampling mechanism over-represents a subgroup whose approval is 70%.

As `n` grows, sample estimate may converge tightly around, say, 60% under biased mixture.

Standard error shrinks:

```math
SE\to0
```

while bias remains about 10 percentage points.

Large data makes wrong estimate more confidently wrong.

## 41. Worked example: practical threshold

Suppose new feature increases revenue/user estimate by:

```text
+10 KRW/user/day
```

95% CI:

```text
[-2, +22] KRW
```

If rollout cost equivalent to +15 KRW/user/day required to break even, merely rejecting zero is not right decision criterion.

Decision needs probability/uncertainty relative to business threshold `15`, not just null `0`.

## 42. AI model evaluation connection

Accuracy on test set is an estimate.

It has sampling uncertainty.

If benchmark has 100 samples, 1% difference may be one item.

Repeated model selection on same test set causes adaptive overfitting.

Need held-out validation/test discipline, confidence intervals or resampling, and multiple-comparison awareness.

## 43. Finance connection

Backtest Sharpe, mean return or alpha estimates have uncertainty and strong time dependence.

Multiple strategy searches create data-snooping bias.

Regime changes violate iid assumptions.

A tiny p-value from naive model can be meaningless if serial correlation, selection and nonstationarity are ignored.

## 44. Practical inference checklist

Before trusting result, ask:

```text
Target population/process là gì?
Sampling/randomization mechanism là gì?
Estimator đang estimate quantity nào?
Independence assumptions có hợp lý?
Standard error tính theo design nào?
Effect size có practical meaning gì?
CI interpretation đúng framework chưa?
P-value có bị multiple testing/optional stopping ảnh hưởng?
Missingness/attrition/measurement error thế nào?
Claim là associational hay causal?
```

## Knowledge Connection

```text
probability
→ LLN / CLT
→ sampling distributions
→ standard errors
→ estimators
→ confidence intervals
→ hypothesis tests
→ power / experimental design
→ A/B testing
→ regression / likelihood
→ Bayesian intervals
→ causal inference
```

## Mental Model

> Statistical inference is **uncertainty accounting for a sampling process**. A sample does not magically reveal a population. We need a design that connects observations to the target, an estimator with known behavior, and a procedure that quantifies uncertainty under explicit assumptions. Precision without identification is false confidence.

## Common Misconceptions

P-value is not `P(H0 true | data)`. `p>0.05` does not prove no effect. 95% confidence does not mean 95% posterior probability in frequentist interpretation. Huge `n` cannot fix systematic bias. More rows do not equal more independent information. Statistical significance is not practical significance or causality. Repeated peeking/multiple metrics can destroy nominal error rates. Narrow intervals can be precisely wrong if design or measurement is biased.