# Model Evaluation: đo đúng thứ mà hệ thống thực sự cần

Model Evaluation (모델 평가 / đánh giá mô hình) không phải bước cuối để “in một con số accuracy”. Nó là quá trình thiết kế evidence để trả lời: model có hoạt động đủ tốt trên population, subgroup, operating condition và business objective mà system sẽ gặp hay không?

Một metric đơn lẻ hiếm khi trả lời đủ. Evaluation tốt cần nối **dataset design → metric → threshold → uncertainty → error analysis → deployment constraints**.

## Bắt đầu từ deployment question

Trước khi chọn metric, cần biết model sẽ được dùng thế nào.

Fraud model: có bao nhiêu cases review mỗi ngày? False negative mất bao nhiêu tiền? False positive gây friction gì?

Medical screening: ưu tiên sensitivity hay specificity? Ai chịu hậu quả của missed case?

Search/recommender: ranking quality ở top positions quan trọng hơn global classification accuracy.

LLM: correctness, factuality, instruction following, latency, safety và cost có thể cần evaluation riêng.

Metric phải follow use case, không ngược lại.

## Confusion Matrix

Binary classification:

| | Actual Positive | Actual Negative |
|---|---:|---:|
| Predicted Positive | TP | FP |
| Predicted Negative | FN | TN |

Từ đây:

\[
Precision=\frac{TP}{TP+FP}
\]

\[
Recall=\frac{TP}{TP+FN}
\]

\[
Specificity=\frac{TN}{TN+FP}
\]

\[
F1=2\frac{Precision\cdot Recall}{Precision+Recall}
\]

Không metric nào “tốt nhất” universal. Chúng encode priorities khác nhau.

## Accuracy và base rate

Accuracy:

\[
\frac{TP+TN}{N}
\]

có thể misleading với imbalance. Nếu disease prevalence 1%, classifier luôn negative đạt 99% accuracy nhưng recall = 0.

Luôn so model với meaningful baseline.

## Precision–Recall trade-off

Lower threshold thường tăng recall nhưng giảm precision. Higher threshold thường ngược lại.

Threshold selection là **decision policy**, không phải intrinsic model property.

Nếu business review capacity `K`, có thể evaluate Precision@K hoặc expected value top-K thay vì threshold cố định.

## ROC Curve

ROC plot:

\[
TPR=Recall
\]

against:

\[
FPR=\frac{FP}{FP+TN}
\]

qua mọi thresholds.

ROC-AUC có interpretation: probability một random positive được rank cao hơn random negative.

AUC đo ranking, không đảm bảo calibrated probabilities hay performance ở threshold operational cụ thể.

## Precision-Recall Curve

PR curve đặc biệt hữu ích khi positive rare. Precision trực tiếp chịu ảnh hưởng base rate, nên phản ánh alert burden tốt hơn ROC trong nhiều anomaly/fraud tasks.

PR-AUC giữa datasets có prevalence khác nhau cần interpret cẩn thận vì baseline precision thay theo positive rate.

## Log Loss và Brier Score

Nếu probability quality quan trọng, classification accuracy không đủ.

Log loss:

\[
-rac1n\sum_i[y_i\log p_i+(1-y_i)\log(1-p_i)]
\]

phạt confident wrong predictions mạnh.

Brier score:

\[
\frac1n\sum_i(p_i-y_i)^2
\]

đo squared probability error.

## Calibration

Model calibrated nếu among predictions near `p=0.7`, khoảng 70% positive về lâu dài trên relevant population.

Calibration curve/reliability diagram so predicted probability bins với empirical frequency.

Calibration có thể degrade under distribution shift dù discrimination/ranking vẫn tốt.

Techniques như Platt scaling, isotonic regression hoặc temperature scaling cần fit trên held-out calibration data.

## Regression Metrics

MAE:

\[
MAE=\frac1n\sum_i|y_i-\hat y_i|
\]

RMSE:

\[
RMSE=\sqrt{\frac1n\sum_i(y_i-\hat y_i)^2}
\]

RMSE nhạy large errors hơn MAE.

MAPE có issue khi target gần zero và asymmetric interpretation.

Metric nên gắn với error cost. Nếu error 100 KRW và 1,000,000 KRW không cùng consequence, generic MAE có thể không phù hợp.

## Ranking Metrics

Search/recommendation thường quan tâm top results.

**Precision@K**, **Recall@K** đo relevant items trong top K.

Discounted Cumulative Gain:

\[
DCG@K=\sum_{i=1}^{K}\frac{rel_i}{\log_2(i+1)}
\]

NDCG normalize theo ideal ranking.

Mean Reciprocal Rank phù hợp khi vị trí relevant result đầu tiên quan trọng:

\[
MRR=\frac1N\sum_q\frac1{rank_q}
\]

Các metric này sẽ quay lại trong Retrieval/RAG.

## Confidence Intervals

Một point estimate như accuracy 0.91 không nói uncertainty.

Bootstrap có thể resample evaluation examples để estimate confidence interval cho metric phức tạp.

Với correlated/grouped data, bootstrap unit phải respect dependency, ví dụ resample users chứ không random rows nếu rows cùng user correlated.

## Statistical Significance vs Practical Significance

Model B AUC 0.901 vs A 0.899 có thể statistically significant trên millions samples nhưng business gain cực nhỏ.

Ngược lại improvement nhỏ global có thể rất quan trọng ở high-value subgroup.

Luôn hỏi effect size và operational impact.

## Error Analysis

Aggregate metric che giấu failure modes. Cần slice theo:

- geography;
- device;
- language;
- customer segment;
- time period;
- target difficulty;
- data quality state.

Sau đó inspect representative false positives/negatives.

Error taxonomy thường dẫn đến improvement rõ hơn blind hyperparameter tuning.

## Subgroup Evaluation và Fairness

Nếu system ảnh hưởng groups khác nhau, report metric theo subgroup. Aggregate score tốt có thể che severe disparity.

Nhưng subgroup analysis cần sample-size uncertainty; group quá nhỏ có metric noisy.

Fairness không thể thu gọn thành một metric duy nhất vì definitions như equalized odds, demographic parity và calibration có thể xung đột dưới differing base rates.

## Offline vs Online Evaluation

Offline test đo historical/replayed performance. Production behavior có feedback loop và user interaction.

A/B test hoặc online experiment đo causal impact của deployed change, nhưng cần guardrails và proper experimental design.

Recommendation model offline NDCG cao hơn chưa chắc increase long-term retention; user behavior adapts.

## Data Leakage trong Evaluation

Leakage có thể đến từ:

- preprocessing fit trên full dataset;
- same entity xuất hiện train/test;
- future info trong features;
- target-derived features;
- benchmark contamination.

Một metric tuyệt đẹp trên leaked test set không có value.

## Evaluation under Distribution Shift

Ngoài IID test set, nên có stress sets:

- later time period;
- new region/domain;
- rare edge cases;
- corrupted/noisy inputs;
- adversarial or worst-case slices.

Robustness là behavior qua conditions, không chỉ average metric.

## Cost-Sensitive Evaluation

Expected cost:

\[
EC=FP\cdot C_{FP}+FN\cdot C_{FN}+...
\]

có thể gần business objective hơn F1.

Nếu benefit/cost varies per case, decision có thể dùng expected value per sample thay fixed threshold.

## Reproducibility

Evaluation cần version:

```text
model version
code version
dataset snapshot
feature pipeline
metric implementation
random seed
threshold/config
```

Nếu không, score không audit được.

## LLM Evaluation Preview

LLM làm evaluation khó hơn vì output open-ended và multiple answers có thể acceptable. Exact match thường quá strict; LLM-as-a-judge có bias; human evaluation đắt; benchmark contamination possible.

Sau này `08_large_language_models/14_llm_evaluation.md` sẽ mở rộng, nhưng principles vẫn giống: task definition, representative data, independent evaluation, uncertainty và failure analysis.

## Mental Model

```text
Deployment goal
      ↓
Evaluation population
      ↓
Metric(s) + thresholds
      ↓
Uncertainty + slices
      ↓
Error analysis
      ↓
Decision to ship / revise / monitor
```

## Common Misconceptions

### “AUC cao nghĩa classifier production tốt”

AUC không nói calibration, operating threshold, latency, subgroup performance hay business cost.

### “Test set chỉ cần đủ lớn”

Representativeness và independence quan trọng không kém size.

### “F1 cân bằng precision/recall nên luôn fair”

F1 bỏ qua TN và implicitly weight precision/recall theo harmonic mean, không encode mọi business cost.

### “Một benchmark đủ để so models”

Benchmark chỉ đo một sampled task distribution và dễ bị contamination/optimization pressure.

## Knowledge Connection

Evaluation tổng hợp [Statistics](../01_mathematical_foundations/03_statistics_for_ai.md), [Training/Validation/Testing](./03_training_validation_and_testing.md), [Loss and Risk](./04_loss_objective_and_risk.md), [Bias–Variance](./14_bias_variance_and_generalization.md) và mở đường tới production monitoring, RAG/LLM evaluation, AI Safety.