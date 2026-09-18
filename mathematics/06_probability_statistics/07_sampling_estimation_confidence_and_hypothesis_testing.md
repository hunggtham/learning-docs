# Lấy mẫu, ước lượng, confidence interval và hypothesis testing

Thống kê suy luận (Statistical Inference / 통계적 추론) bắt đầu từ một vấn đề bất khả tránh: ta muốn biết điều gì đó về một population lớn nhưng chỉ quan sát được một sample hữu hạn. Vì vậy mọi kết luận đều phải tách ba lớp: dữ liệu quan sát được, model xác suất dùng để mô tả quá trình sinh dữ liệu, và quantity của population mà ta muốn suy luận.

## Population, sample, parameter và statistic

Population là tập đối tượng hoặc process mà ta quan tâm. Parameter là quantity cố định nhưng chưa biết của population, chẳng hạn mean `\mu`, variance `\sigma^2`, proportion `p`.

Sample gồm observations:

```math
X_1,\ldots,X_n.
```

Statistic là function của sample, ví dụ sample mean:

```math
\bar X=\frac1n\sum_{i=1}^n X_i.
```

Parameter không random trong frequentist model; statistic random trước khi sample được quan sát vì nó phụ thuộc dữ liệu sẽ xuất hiện.

## Sampling distribution

Nếu lặp lại cùng sampling process nhiều lần, mỗi sample cho một `\bar X` khác nhau. Distribution của statistic qua các repeated samples gọi là sampling distribution.

Nếu observations independent, cùng mean `\mu` và variance `\sigma^2`, thì

```math
E[\bar X]=\mu
```

và

```math
\operatorname{Var}(\bar X)=\frac{\sigma^2}{n}.
```

Standard deviation của sampling distribution là

```math
SE(\bar X)=\frac{\sigma}{\sqrt n},
```

gọi là standard error.

Kết quả `1/\sqrt n` giải thích diminishing returns của sample size: muốn giảm standard error còn một nửa, cần khoảng bốn lần observations.

## Estimator và bias

Estimator (Estimator / 추정량) là rule dùng sample để estimate parameter. Estimator `\hat\theta` unbiased nếu

```math
E[\hat\theta]=\theta.
```

Nhưng unbiased không đồng nghĩa “tốt nhất”. Một estimator có bias nhỏ nhưng variance thấp có thể có mean squared error thấp hơn:

```math
\operatorname{MSE}(\hat\theta)
=\operatorname{Var}(\hat\theta)+\operatorname{Bias}(\hat\theta)^2.
```

Đây là bias–variance trade-off ở dạng thống kê cơ bản, cùng mental model xuất hiện trong machine learning.

## Confidence interval

Một 95% confidence interval không có nghĩa “xác suất parameter nằm trong interval này là 95%” trong frequentist interpretation sau khi interval đã được tính. Parameter được coi là fixed; interval là random procedure.

Ý nghĩa đúng: nếu lặp lại sampling và construction procedure rất nhiều lần dưới assumptions của model, khoảng 95% các intervals được tạo sẽ chứa true parameter.

Với mean và known `\sigma`, một interval điển hình là

```math
\bar x\pm z_{0.975}\frac{\sigma}{\sqrt n}.
```

Nếu `\sigma` unknown và sample normal hoặc sufficiently justified, Student's `t` distribution thường được dùng:

```math
\bar x\pm t_{n-1,0.975}\frac{s}{\sqrt n}.
```

Width phụ thuộc uncertainty và sample size, không chỉ mean.

## Hypothesis testing là model comparison dưới một null assumption

Null hypothesis `H_0` là một statement cụ thể, ví dụ

```math
H_0:\mu=100.
```

Ta chọn test statistic có known hoặc approximated distribution khi `H_0` đúng. Sau đó hỏi: observed statistic có quá extreme so với distribution đó không?

P-value là probability, **assuming `H_0` và model assumptions đúng**, thu được result ít nhất extreme như observed theo test definition.

Nó không phải

```text
P(H0 is true | data).
```

Frequentist p-value không trực tiếp cho posterior probability của hypothesis.

## Type I, Type II error và power

Type I error xảy ra khi reject `H_0` dù nó đúng. Significance level `\alpha` kiểm soát long-run Type I error dưới test assumptions.

Type II error xảy ra khi không reject `H_0` dù một alternative cụ thể đúng. Power là

```math
1-\beta,
```

xác suất detect effect dưới alternative đó.

Power tăng khi effect size lớn, noise nhỏ, sample size lớn hoặc threshold ít nghiêm ngặt hơn.

Điều này cho thấy “not significant” không đồng nghĩa “không có effect”; sample có thể simply thiếu power.

## Statistical significance khác practical significance

Với sample cực lớn, một effect rất nhỏ có thể cho tiny p-value. Nhưng business, medical hoặc engineering importance phụ thuộc effect size và context.

Ví dụ conversion rate tăng từ `10.00%` lên `10.05%` có thể statistically detectable với hàng chục triệu users nhưng impact kinh tế có thể nhỏ hoặc lớn tùy volume/cost. Vì vậy nên báo confidence interval và effect size, không chỉ p-value.

## Multiple testing

Nếu chạy nhiều tests với `\alpha=0.05`, probability có ít nhất một false positive tăng. Đây là lý do multiple comparisons cần correction hoặc hierarchical modeling tùy problem.

Bonferroni là approach bảo thủ: nếu có `m` tests, dùng threshold `\alpha/m` để control family-wise error rate. False discovery rate methods như Benjamini–Hochberg kiểm soát một criterion khác và thường có power tốt hơn trong large-scale testing.

## Experimental design và causality

Randomized experiment giúp tách treatment effect khỏi confounding vì random assignment cân bằng các factors chưa quan sát theo xác suất.

Observational correlation không tự động là causal effect. Nếu users tự chọn treatment, treatment group có thể khác control group ngay từ đầu.

Statistical inference mạnh hay yếu phụ thuộc design trước khi phụ thuộc test sau cùng.

## Knowledge Connection

Sampling distributions dựa trên probability và CLT. Confidence intervals nối estimation với uncertainty. Hypothesis tests nối tail probabilities với decision thresholds. A/B testing trong software products là application trực tiếp. Model validation trong ML cần phân biệt training variability, test uncertainty và multiple experimentation.

## Mental Model

> Thống kê suy luận không “biến sample thành sự thật”. Nó xây một cầu có định lượng uncertainty từ data hữu hạn tới claims về process rộng hơn. Mọi kết luận phải đọc cùng sampling design, assumptions và độ không chắc chắn.

## Common Misconceptions

P-value không phải probability null hypothesis đúng. `p>0.05` không chứng minh hai groups giống nhau. Confidence level không phải probability posterior của parameter trong frequentist interpretation. Sample size lớn không sửa selection bias. Statistical significance không tự động mang practical significance hay causality.
