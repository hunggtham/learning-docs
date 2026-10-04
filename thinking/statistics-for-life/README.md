# Statistics for Life — Đọc số liệu mà không bị con số dẫn dắt

Statistics for Life là lớp ứng dụng. Formal statistics nằm ở [Mathematics](../../mathematics/06_probability_statistics/05_descriptive_and_inferential_statistics.md); study design nằm ở [Research Methods](../../research_methods/README.md). Mục tiêu ở đây là đọc chart, survey, medical study, business metric và news statistic một cách có cấu trúc.

## 1. Bắt đầu từ denominator

“Risk tăng 50%” chưa đủ thông tin. Nếu baseline risk tăng từ 2/10,000 lên 3/10,000 thì relative increase là 50%, nhưng absolute increase là 1/10,000.

Luôn hỏi:

```text
50% of what?
Compared with what baseline?
Over what time period?
For which population?
```

## 2. Mean không phải lúc nào cũng là “typical”

Mean nhạy với outlier. Median thường mô tả center tốt hơn với income, house prices hoặc latency có long tail. Distribution shape quan trọng hơn một single summary statistic.

Khi ai đó nói “average”, hỏi họ dùng mean, median hay một weighted average.

## 3. Correlation ≠ causation

Correlation có thể xuất hiện do:

- X gây Y;
- Y gây X;
- Z gây cả X và Y;
- selection/collider bias;
- measurement artifact;
- chance.

Regression có thể mô tả association rất tốt mà vẫn không identify causal effect. Xem [Regression & Correlation](../../mathematics/06_probability_statistics/06_regression_and_correlation.md) và [Research Methods](../../research_methods/README.md).

## 4. Sample và population

Một số đo chỉ có ý nghĩa trong population mà sample đại diện. Với survey, cần hỏi sampling frame, response rate và weighting. Với online poll, self-selection có thể mạnh đến mức sample size lớn vẫn không cứu được bias.

**Big data không tự sửa bad sampling.**

## 5. Statistical significance không đồng nghĩa practical significance

Một effect rất nhỏ có thể có p-value thấp nếu sample cực lớn. Ngược lại, effect quan trọng có thể chưa đạt significance nếu sample nhỏ.

Hãy ưu tiên đọc cùng nhau:

```text
effect size
+ uncertainty interval
+ sample/design
+ practical consequence
```

Không đọc p-value như “xác suất hypothesis sai”.

## 6. Medical-study reading mini-protocol

Khi đọc một medical claim:

1. population nào được nghiên cứu;
2. observational hay randomized;
3. outcome là surrogate hay patient-important outcome;
4. absolute risk difference bao nhiêu;
5. follow-up đủ dài không;
6. confidence interval rộng đến đâu;
7. có multiple comparisons, attrition hoặc selective reporting không;
8. evidence là một study hay cumulative body of evidence.

Phần methodology đi sâu ở [Research Methods](../../research_methods/README.md); biological mechanism ở [Biology](../../biology/README.md).

## 7. Business và investment metrics

Revenue growth, conversion rate, retention, Sharpe ratio hoặc win rate đều cần denominator và cohort definition. Một metric có thể cải thiện chỉ vì mix của population thay đổi.

Trước khi kết luận “performance tốt hơn”, hỏi:

```text
same population?
same measurement window?
same definition?
same market regime?
selection/survivorship changed?
```

## Connections

- [Probability](../probability/README.md): uncertainty trước khi có hoặc khi diễn giải data.
- [Critical Thinking](../critical-thinking/README.md): claim–evidence–inference.
- [Cognitive Bias](../cognitive-bias/README.md): survivorship, availability và confirmation bias.
- [Investing](../../investing/README.md): return, volatility, backtests và performance metrics.
- [Economics](../../economics/README.md): econometrics và policy evidence.