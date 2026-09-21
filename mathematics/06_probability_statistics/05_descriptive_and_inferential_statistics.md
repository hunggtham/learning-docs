# Thống kê mô tả và suy luận: từ sample tới uncertainty về population

Thống kê (statistics / 통계학) bắt đầu từ một bất cân xứng rất thực tế: ta muốn biết điều gì đó về một population hoặc process lớn, nhưng chỉ quan sát được một sample hữu hạn, noisy và có thể biased.

Probability thường đi theo hướng

```text
model → consequences
```

còn statistical inference thường đi ngược:

```text
data → plausible statements về model / parameter / future data
```

Vì vậy statistics không chỉ là “tính mean, variance và p-value”. Nó là reasoning dưới uncertainty, và mọi conclusion chỉ có ý nghĩa khi gắn với **sampling mechanism, assumptions và target question**.

## 1. Population, sample, parameter và statistic

Population không nhất thiết là “toàn bộ con người”. Nó có thể là:

- tất cả transactions tương lai của một system;
- process sản xuất tạo measurements;
- distribution của returns;
- user population mà product team quan tâm.

Parameter là quantity mô tả population/model, ví dụ population mean `\mu` hoặc variance `\sigma^2`.

Statistic là function của observed sample, ví dụ

```math
\bar x=\frac1n\sum_{i=1}^n x_i.
```

Trong frequentist framework, parameter được xem fixed but unknown; statistic là random trước khi sample được quan sát vì sample itself random.

## 2. Descriptive statistics chỉ mô tả data đã thấy

Descriptive statistics trả lời:

> Sample hiện có trông như thế nào?

Inferential statistics hỏi thêm:

> Sample này cho phép nói gì về process rộng hơn?

Hai tầng không được trộn lẫn.

Một histogram đẹp của sample không guarantee population có same shape. Một sample mean chính xác đến nhiều decimal places cũng không guarantee estimator unbiased hoặc representative.

## 3. Center: mean, median và mode trả lời câu hỏi khác nhau

### Mean

```math
\bar x=\frac1n\sum_i x_i.
```

Mean là balancing point và tối ưu squared-error loss:

```math
\bar x
=
\arg\min_a\sum_i(x_i-a)^2.
```

Đây là lý do mean gắn tự nhiên với least squares.

### Median

Median minimises absolute deviation:

```math
\operatorname{median}(x_i)
\in
\arg\min_a\sum_i|x_i-a|.
```

Nó robust hơn trước outliers.

### Mode

Mode là most frequent value/category, hữu ích với discrete/categorical data nhưng có thể unstable trong continuous settings nếu phụ thuộc binning/density estimation.

Không có một “center đúng” universal; choice phụ thuộc loss, distribution và question.

## 4. Spread: uncertainty nội tại của sample

Variance đo squared deviation quanh mean:

```math
s^2=
\frac{1}{n-1}
\sum_{i=1}^{n}(x_i-\bar x)^2.
```

Tại sao denominator thường là `n-1` trong sample variance? Vì sample mean đã được estimated từ data, làm mất một degree of freedom. Bessel correction làm estimator unbiased cho population variance dưới standard iid assumptions.

Standard deviation:

```math
s=\sqrt{s^2}
```

trở lại cùng unit với data.

IQR:

```math
IQR=Q_3-Q_1
```

robust hơn với heavy tails/outliers.

## 5. Outlier không đồng nghĩa error

Point xa phần lớn data có thể là:

- measurement error;
- rare but valid event;
- different subpopulation;
- tail event quan trọng;
- data pipeline bug.

Một rule như `1.5×IQR` chỉ là flagging convention, không phải proof point sai.

Trong finance và reliability, tail observations đôi khi chính là phần cần quan tâm nhất.

## 6. Sampling design quan trọng hơn sample size đơn thuần

Một sample lớn nhưng systematically biased có thể cho estimate rất precise của wrong quantity.

Ví dụ survey chỉ thu từ power users có thể estimate product satisfaction của power users cực chính xác nhưng không represent toàn customer base.

Random sampling giúp giảm selection bias theo design. Stratification, cluster sampling và weighting tồn tại vì real populations hiếm khi sample đơn giản.

## 7. Estimator có bias và variance

Estimator `\hat\theta` có bias:

```math
\operatorname{Bias}(\hat\theta)
=E[\hat\theta]-\theta.
```

Variance đo estimator fluctuate giữa repeated samples.

Một estimator có thể low bias nhưng high variance, hoặc ngược lại.

Mean squared error decomposition:

```math
E[(\hat\theta-\theta)^2]
=
\operatorname{Var}(\hat\theta)
+\operatorname{Bias}(\hat\theta)^2.
```

Đây là cùng bias-variance trade-off xuất hiện trong machine learning.

## 8. Sampling distribution là bridge tới inference

Nếu lặp cùng sampling procedure rất nhiều lần và mỗi lần tính statistic, statistic itself có distribution.

Ví dụ sample mean `\bar X` có

```math
E[\bar X]=\mu
```

và với iid observations variance `\sigma^2`:

```math
\operatorname{Var}(\bar X)=\frac{\sigma^2}{n}.
```

Standard error:

```math
SE(\bar X)=\frac{\sigma}{\sqrt n}
```

hoặc estimate bằng `s/\sqrt n`.

`1/\sqrt n` law giải thích vì sao muốn halve standard error cần roughly quadruple sample size.

## 9. Central Limit Theorem: vì sao normal xuất hiện nhiều trong inference?

Dưới conditions phù hợp, standardized sum/mean của many independent-ish observations tiến tới normal distribution khi `n` lớn.

Điều này không nói raw data phải normal. Nó nói **sampling distribution của aggregate** có thể approximately normal.

Đây là lý do normal-based confidence intervals xuất hiện rộng.

Heavy tails, dependence hoặc small samples có thể làm approximation kém.

## 10. Confidence interval: procedure trước, interval sau

Một 95% confidence procedure được thiết kế sao cho trong repeated sampling, khoảng 95% intervals chứa true parameter dưới assumptions.

Ví dụ roughly:

```math
\bar x\pm1.96\,SE
```

khi normal approximation phù hợp.

Strict frequentist interpretation không nói “parameter có 95% probability nằm trong interval này” sau khi data cố định. Parameter không random trong framework đó.

Bayesian credible interval có interpretation khác vì posterior treats parameter uncertainty probabilistically.

## 11. Hypothesis testing là model checking có controlled error rates

Null hypothesis `H_0` định nghĩa reference model.

Ta chọn test statistic `T` đo discrepancy giữa data và null.

p-value:

```math
P(
T\text{ at least as extreme as observed}
\mid H_0,
\text{model assumptions}
).
```

Nó **không phải**

```text
P(H0 true | data).
```

Đây là một trong những misconceptions phổ biến nhất.

## 12. Type I, Type II và power

Type I error: reject true null.

```math
P(\text{Type I})=\alpha
```

khi test calibrated đúng.

Type II error: fail to reject false null.

Power:

```math
1-\beta.
```

Power phụ thuộc:

- effect size;
- sample size;
- noise;
- significance threshold;
- test/model structure.

Không thể nói một test “80% power” nếu không specify alternative/effect assumptions.

## 13. Effect size quan trọng hơn chỉ p-value

Với huge sample, effect rất nhỏ có thể statistically significant.

Ví dụ conversion tăng từ 10.000% lên 10.010% có thể p-value rất nhỏ nếu `n` cực lớn, nhưng business impact có thể negligible.

Ngược lại, effect economically important có thể không significant nếu sample quá nhỏ.

Inference tốt cần report uncertainty + effect magnitude + domain relevance.

## 14. Multiple testing và false discoveries

Nếu chạy 100 independent tests ở `\alpha=0.05` khi tất cả null true, expected false rejections khoảng 5.

Bonferroni control family-wise error rất conservative.

False Discovery Rate procedures như Benjamini–Hochberg target expected proportion false discoveries trong rejected set.

Choice method phụ thuộc cost của false positives và analysis goal.

## 15. Bootstrap: approximate sampling uncertainty bằng resampling

Khi analytic sampling distribution khó derive, bootstrap resamples observed data with replacement, tính statistic nhiều lần và dùng empirical distribution của bootstrap statistics.

Nó hữu ích nhưng không magic: nếu original sample biased hoặc dependence structure ignored, bootstrap không sửa design problem.

Time series cần block/bootstrap variants để preserve dependence.

## 16. Causality khác prediction và association

Correlation/regression mô tả association hoặc conditional expectation structure. Causal question hỏi:

> Outcome sẽ thay đổi thế nào nếu ta intervene và thay treatment/exposure?

Confounders, selection bias, collider bias và reverse causality có thể làm observational association khác causal effect.

Randomized experiments giúp vì treatment assignment independent of potential outcomes in expectation dưới proper implementation.

## 17. Worked example: A/B test không chỉ là p-value

Giả sử:

```text
Control:   1000 users, 100 conversions
Treatment: 1000 users, 120 conversions
```

Observed rates:

```math
\hat p_C=0.10,
\qquad
\hat p_T=0.12.
```

Absolute lift:

```math
0.12-0.10=0.02
```

= 2 percentage points.

Relative lift:

```math
\frac{0.12-0.10}{0.10}=20\%.
```

Hai numbers đều đúng nhưng answer different questions.

Một complete analysis còn cần uncertainty interval, test assumptions, pre-specified metric, exposure quality và practical value của 2-point lift.

## 18. Simpson's paradox: aggregation có thể đảo conclusion

Một trend có thể xuất hiện trong từng subgroup nhưng đảo khi aggregate vì group composition khác nhau.

Điều này nhắc rằng weighted aggregation và conditioning structure matter.

Statistics không chỉ xử lý numbers; nó xử lý **which comparisons are meaningful**.

## 19. Finance: return distribution và tail risk

Mean return và standard deviation chỉ summarize một phần distribution.

Skewness, kurtosis, drawdowns, serial dependence và tail dependence có thể quan trọng hơn.

Assume normal returns có thể underestimate extreme risk.

Confidence intervals cũng cần distinguish iid assumptions với autocorrelated/heteroskedastic financial time series.

## 20. AI/Data: train/test statistics và dataset shift

Train metrics estimate performance trên training distribution. Validation/test estimate generalization tới related sample distribution.

Nếu deployment distribution shifts, confidence từ iid test set không guarantee production behavior.

Dataset representativeness là statistical assumption, không chỉ MLOps detail.

## 21. Common failure modes của statistical reasoning

### Precision without validity

Very narrow confidence interval từ huge biased sample vẫn có thể center ở wrong target.

### p-value worship

Threshold `0.05` không phân chia truth/falsehood. Nó là decision convention trong defined testing framework.

### Ignoring denominator

“Errors tăng 50%” vô nghĩa nếu traffic cũng tăng 200%; rates và counts answer different questions.

### Post-selection inference

Nếu ta thử rất nhiều analyses rồi chỉ report one significant result, nominal p-value không còn reflect full search process.

## Mental Model

> Statistics là một pipeline: define target → understand data-generating/sampling process → choose estimator/model → quantify sampling uncertainty → check assumptions → interpret effect in domain context. Một number cuối như mean, p-value hay confidence interval chỉ có meaning bên trong pipeline đó.

## Common Misconceptions

**Larger sample luôn solve problem.** Nó giảm random error nhưng không tự chữa systematic bias.

**95% confidence interval nghĩa parameter có 95% probability nằm trong interval cụ thể.** Không trong strict frequentist interpretation.

**Small p-value nghĩa effect lớn hoặc important.** Không; p-value phụ thuộc cả effect và sample size/noise.

**Correlation hoặc regression đủ để nói causality.** Không; causal interpretation cần design/identification assumptions bổ sung.
