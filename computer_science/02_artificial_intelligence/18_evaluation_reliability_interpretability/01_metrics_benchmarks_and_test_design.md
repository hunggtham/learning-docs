# Metric, Benchmark và Test Design

Metric biến behavior thành số, nhưng con số chỉ có ý nghĩa khi **thiết kế phép đo (measurement design)** đúng. AI evaluation thường thất bại không phải vì thiếu metric mà vì metric đo sai population, benchmark bị contamination hoặc test case không phản ánh contract thật.

## Phân rã Metric

Một evaluation tốt thường có nhiều tầng:

```text
chất lượng task
calibration / uncertainty
latency
cost
robustness
safety
chất lượng theo subgroup / slice
```

Một model có accuracy cao nhưng cost quá lớn vẫn có thể không phù hợp để deploy.

## Metric cho Classification

Confusion matrix:

```text
TP FP
FN TN
```

Precision:

\[
\frac{TP}{TP+FP}
\]

Recall:

\[
\frac{TP}{TP+FN}
\]

F1:

\[
2\frac{Precision\cdot Recall}{Precision+Recall}
\]

Việc chọn metric phụ thuộc chi phí của từng loại error và prevalence của class.

## ROC-AUC và PR-AUC

ROC-AUC đo khả năng ranking qua nhiều threshold nhưng có thể trông quá tốt khi positive class rất hiếm.

PR-AUC tập trung vào precision và recall của positive class, thường cung cấp nhiều thông tin hơn cho highly imbalanced task.

## Regression

MAE ít nhạy với outlier hơn MSE; MSE phạt large error mạnh hơn.

Nếu target distribution bị lệch, nên báo cáo thêm quantile hoặc slice thay vì chỉ average metric.

## Ranking

Recall@k đo xem relevant item có xuất hiện trong top-k hay không.

MRR tập trung vào rank của relevant result đầu tiên.

nDCG hỗ trợ graded relevance và giảm trọng số cho position thấp.

RAG retrieval cần metric phù hợp với câu hỏi đang đo: candidate recall khác với final ranking quality.

## Metric cho Generation

BLEU hoặc ROUGE hữu ích trong một số task nhưng token overlap không đủ để đo factual correctness hay semantic quality.

LLM task thường cần kết hợp:

- exact hoặc deterministic validator;
- semantic judge;
- factual support;
- human evaluation;
- task-specific execution test.

## Metric cho Structured Output

JSON validity chỉ đo cú pháp. Cần tách:

```text
schema có hợp lệ không?
required field có đúng không?
value có đúng semantics không?
action có an toàn không?
```

## Metric cho Agent

Agent success không chỉ là final answer. Nên theo dõi:

- completion đã được verify;
- số step;
- tool call;
- retry;
- độ đúng của side effect;
- cost và time;
- policy violation.

## Benchmark Contamination

Nếu training data của model chứa benchmark, score không còn là phép đo sạch về generalization.

Với large web-trained model, contamination khó loại trừ hoàn toàn; benchmark nên có task mới hơn, private/held-out task hoặc dynamic evaluation để giảm rủi ro này.

## Benchmark Saturation

Khi score gần ceiling, difference nhỏ trở nên khó diễn giải và benchmark không còn phân biệt tốt các system mạnh. Khi đó cần task khó hơn hoặc coverage rộng hơn.

## Static và Dynamic Benchmark

Static benchmark dễ tái lập nhưng dễ bị overfit. Dynamic, rotating hoặc private benchmark giảm gaming nhưng khó so sánh lịch sử hơn.

Có thể kết hợp cả hai.

## Taxonomy của Test Case

Một suite tốt nên gồm:

```text
happy path
edge case
long-tail case
known regression
adversarial case
invalid input
out-of-distribution case
high-impact scenario
```

## Golden Set

Golden set nên được tuyển chọn có chủ đích, version hóa và có rationale cho từng case. Không nên để suite biến thành collection ngẫu nhiên không biết coverage.

## Hidden Holdout

Nếu developer xem test output mỗi ngày, test suite không còn unbiased. Một hidden set giúp phát hiện overfitting của chính release process.

## Data Split Leakage

Entity hoặc temporal duplicate giữa train và test làm metric bị phóng đại. Split strategy phải phản ánh deployment thật.

Temporal application thường cần future holdout.

## Sample Weighting

Nếu production population khác raw test sample, có thể cần weighting để ước lượng expected metric khi deploy.

Tuy nhiên weighting dựa trên giả định rằng target distribution đã được biết đủ tốt.

## Statistical Significance và Practical Significance

P-value nhỏ không bảo đảm improvement có giá trị thực tiễn. Với sample rất lớn, effect cực nhỏ vẫn có thể statistically significant nhưng business value không đáng kể.

Nên báo cáo effect size, confidence interval và operational cost cùng nhau.

## Paired Evaluation

Khi so sánh nhiều model trên cùng test case, paired bootstrap hoặc paired test thường có statistical power tốt hơn independent comparison vì kiểm soát độ khó của từng case.

## Benchmark Governance

Cần theo dõi:

```text
version
owner
source / license
contamination risk
refresh cadence
retirement policy
```

Evaluation dataset cũng là một data asset cần governance.

## Mô hình tư duy

```text
Metric là một cảm biến.
Benchmark là một thiết lập thí nghiệm.
Cả hai đều không phải bản thân reality.
```

## Những nhầm lẫn thường gặp

### “AUC cao nên threshold 0.5 chắc ổn”

Không. AUC không chọn decision threshold.

### “LLM judge score là khách quan tuyệt đối”

Không. Judge cũng có bias và error, cần được validation.

### “Cùng benchmark score nghĩa là hai system tương đương”

Không. Latency, calibration, safety, slice performance và cost có thể khác rất lớn.

## Liên kết kiến thức

Xem [Evaluation Foundations](./00_evaluation_foundations.md), [Uncertainty/Calibration](./02_uncertainty_and_calibration.md), [AI Testing](./05_ai_testing_and_behavioral_evaluation.md) và [Monitoring](../16_mlops_and_llmops/06_monitoring_and_observability.md).