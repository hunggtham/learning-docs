# Thống kê mô tả và suy luận

Thống kê (Statistics / 통계학) dùng data quan sát để mô tả population hoặc suy luận về process sinh data. Khác với probability đi từ model đến consequences, statistical inference thường đi từ sample ngược về unknown model parameters.

## Population và sample

Population là tập/process mục tiêu; sample là observations thực tế. Parameter như population mean `μ` cố định nhưng unknown trong frequentist framework; statistic như sample mean `\bar x` được tính từ sample và thay đổi giữa samples.

Một sample lớn nhưng biased vẫn có thể cho estimate rất chính xác của thứ sai. Sampling design quan trọng không kém sample size.

## Measures of center

Mean:

```math
\bar x=\frac1n\sum_i x_i
```

sensitive với outliers.

Median là middle quantile, robust hơn với skew/outliers. Mode là most frequent value/category.

Không có một “center tốt nhất” universal; lựa chọn phụ thuộc distribution và question.

## Spread

Range đơn giản nhưng phụ thuộc extremes. Variance/sample variance dùng squared deviations. Interquartile range `IQR=Q3-Q1` đo middle 50% và robust hơn.

Box plot dùng quartiles để visualize spread/outliers theo convention, nhưng points flagged không tự động là data errors.

## Sampling distribution

Nếu lặp sampling procedure, statistic có distribution riêng. Standard error đo variability của estimator qua hypothetical repeated samples.

Đây là key transition từ descriptive statistics sang inference.

## Confidence interval

Một 95% confidence procedure trong frequentist interpretation nghĩa: nếu lặp sampling và xây interval theo cùng procedure, khoảng 95% intervals sẽ chứa true parameter dưới assumptions.

Sau khi một interval cụ thể đã tính, parameter không được xem là random trong strict frequentist framework, nên không diễn giải đơn giản “95% probability parameter nằm trong interval” nếu không chuyển sang Bayesian framework.

## Hypothesis testing

Null hypothesis `H0` xác định reference model. Test statistic đo data lệch null đến đâu. p-value là probability, dưới assumption `H0` và model, quan sát test statistic ít nhất extreme như observed.

Nó không phải probability `H0` đúng.

Small p-value cho evidence chống null theo test design, nhưng effect size và practical significance vẫn cần xem xét.

## Type I và Type II errors

Type I: reject true null; rate control thường `α`.

Type II: fail to reject false null; probability `β`. Power `1-β` là chance detect effect under specified alternative.

Sample size, noise và effect size ảnh hưởng power.

## Multiple testing

Nếu test nhiều hypotheses ở 5% threshold, chance ít nhất một false positive tăng. Methods như Bonferroni hoặc false discovery rate procedures address multiple comparisons theo goals khác nhau.

## Causality

Association không tự động causal. Confounders, selection bias và reverse causation có thể tạo correlation. Randomized experiments giúp identify causal effects bằng balancing confounders in expectation, nhưng implementation, compliance và external validity vẫn matter.

## Mental Model

> Statistics là reasoning dưới uncertainty từ một sample hữu hạn về một process rộng hơn. Mỗi estimate/test phải được đọc cùng sampling mechanism, assumptions, uncertainty và effect size — không chỉ một con số cuối.

## Common Misconceptions

p-value không phải probability hypothesis sai. Confidence level không phải guarantee cho mỗi interval cụ thể theo frequentist interpretation. Larger sample giảm random error nhưng không tự sửa systematic bias. Statistical significance không đồng nghĩa practical importance.
