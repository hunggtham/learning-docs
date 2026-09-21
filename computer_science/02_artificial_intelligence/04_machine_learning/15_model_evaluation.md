# Đánh giá mô hình: đo đúng thứ hệ thống thật sự cần

**Đánh giá mô hình (Model Evaluation / 모델 평가)** không phải bước cuối chỉ để “in ra một con số accuracy”. Đây là quá trình thiết kế bằng chứng để trả lời: mô hình có hoạt động đủ tốt trên population, subgroup, điều kiện vận hành và mục tiêu nghiệp vụ mà hệ thống thật sự gặp hay không?

Một metric đơn lẻ hiếm khi đủ. Evaluation tốt cần nối liền:

```text
thiết kế dataset
→ metric
→ threshold
→ uncertainty
→ phân tích lỗi
→ ràng buộc deployment
```

## Bắt đầu từ câu hỏi deployment

Trước khi chọn metric, cần biết mô hình sẽ được dùng thế nào.

Với fraud model, cần biết mỗi ngày đội review xử lý được bao nhiêu case, false negative gây mất bao nhiêu tiền và false positive gây friction gì cho khách hàng.

Với medical screening, cần xác định ưu tiên sensitivity hay specificity và ai chịu hậu quả nếu bỏ sót ca bệnh.

Với search hoặc recommender, chất lượng ranking ở những vị trí đầu có thể quan trọng hơn global classification accuracy.

Với LLM, correctness, factuality, instruction following, latency, safety và cost thường phải được đánh giá riêng.

Metric phải xuất phát từ use case, không phải chọn metric trước rồi cố uốn bài toán theo nó.

## Confusion Matrix

Trong classification nhị phân:

| | Actual Positive | Actual Negative |
|---|---:|---:|
| Predicted Positive | TP | FP |
| Predicted Negative | FN | TN |

Từ đó:

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

Không có metric nào tốt nhất cho mọi bài toán. Mỗi metric phản ánh một ưu tiên khác nhau.

## Accuracy và tỷ lệ nền

Accuracy:

\[
\frac{TP+TN}{N}
\]

có thể gây hiểu nhầm khi dữ liệu mất cân bằng.

Nếu prevalence của bệnh chỉ 1%, bộ phân loại luôn dự đoán negative vẫn đạt 99% accuracy nhưng recall bằng 0.

Vì vậy luôn phải so với một baseline có ý nghĩa.

## Sự đánh đổi Precision–Recall

Threshold thấp thường tăng recall nhưng giảm precision. Threshold cao thường làm ngược lại.

Lựa chọn threshold là **chính sách quyết định (decision policy)**, không phải thuộc tính cố định của mô hình.

Nếu đội vận hành chỉ xử lý được `K` case mỗi ngày, có thể đánh giá Precision@K hoặc expected value ở top-K thay vì dùng threshold cố định.

## ROC Curve

ROC curve biểu diễn:

\[
TPR=Recall
\]

so với:

\[
FPR=\frac{FP}{FP+TN}
\]

qua nhiều threshold.

ROC-AUC có thể diễn giải là xác suất một positive ngẫu nhiên được xếp hạng cao hơn một negative ngẫu nhiên.

AUC đo khả năng ranking, không bảo đảm probability đã calibration hoặc mô hình hoạt động tốt ở threshold production cụ thể.

## Precision–Recall Curve

PR curve đặc biệt hữu ích khi positive hiếm.

Precision trực tiếp chịu ảnh hưởng của base rate nên thường phản ánh tải cảnh báo thực tế tốt hơn ROC trong các bài toán fraud hoặc anomaly.

Khi so PR-AUC giữa các dataset có prevalence khác nhau cần rất cẩn thận vì baseline precision thay đổi theo positive rate.

## Log Loss và Brier Score

Nếu chất lượng xác suất quan trọng, classification accuracy không đủ.

Log loss:

\[
-\frac1n\sum_i[y_i\log p_i+(1-y_i)\log(1-p_i)]
\]

phạt rất mạnh những dự đoán sai nhưng quá tự tin.

Brier score:

\[
\frac1n\sum_i(p_i-y_i)^2
\]

đo sai số bình phương của xác suất dự đoán.

## Calibration

Mô hình được **hiệu chuẩn (calibrated)** nếu trong nhóm các prediction gần `p=0.7`, khoảng 70% trường hợp thật sự positive về dài hạn trên population liên quan.

Calibration curve hoặc reliability diagram so sánh probability dự đoán với tần suất thực tế trong từng bin.

Calibration có thể xuống cấp khi distribution shift dù khả năng ranking vẫn còn tốt.

Các phương pháp như Platt scaling, isotonic regression hoặc temperature scaling cần fit trên held-out calibration data.

## Metric cho hồi quy

MAE:

\[
MAE=\frac1n\sum_i|y_i-\hat y_i|
\]

RMSE:

\[
RMSE=\sqrt{\frac1n\sum_i(y_i-\hat y_i)^2}
\]

RMSE nhạy với sai số lớn hơn MAE.

MAPE có vấn đề khi target gần 0 và cách diễn giải không đối xứng.

Metric nên gắn với chi phí lỗi trong domain. Nếu sai 100 KRW và sai 1.000.000 KRW có hậu quả rất khác, generic MAE có thể chưa phản ánh đúng mục tiêu.

## Metric xếp hạng

Search và recommendation thường quan tâm nhiều nhất tới các vị trí đầu.

**Precision@K** và **Recall@K** đo số item liên quan trong top K.

Discounted Cumulative Gain:

\[
DCG@K=\sum_{i=1}^{K}\frac{rel_i}{\log_2(i+1)}
\]

NDCG chuẩn hóa DCG theo ranking lý tưởng.

Mean Reciprocal Rank phù hợp khi vị trí của kết quả liên quan đầu tiên là quan trọng:

\[
MRR=\frac1N\sum_q\frac1{rank_q}
\]

Các metric này sẽ xuất hiện lại trong Retrieval và RAG.

## Khoảng tin cậy

Một point estimate như accuracy `0.91` không nói lên uncertainty của phép đo.

Bootstrap có thể lấy mẫu lại evaluation set để ước lượng confidence interval cho metric phức tạp.

Nếu dữ liệu có dependency theo user hoặc group, đơn vị bootstrap cũng phải giữ cấu trúc đó. Ví dụ nếu nhiều row cùng user tương quan, nên resample user thay vì từng row độc lập.

## Ý nghĩa thống kê và ý nghĩa thực tế

Mô hình B có AUC `0.901`, mô hình A có `0.899`. Với hàng triệu mẫu, chênh lệch có thể statistically significant nhưng lợi ích nghiệp vụ gần như không đáng kể.

Ngược lại, một cải thiện nhỏ ở toàn bộ population có thể rất quan trọng nếu tập trung vào subgroup có giá trị cao.

Luôn phải xem cả effect size và operational impact.

## Phân tích lỗi

Metric tổng thể che giấu nhiều failure mode.

Nên chia dữ liệu theo các lát cắt có ý nghĩa như geography, device, language, customer segment, time period, độ khó target hoặc trạng thái chất lượng dữ liệu.

Sau đó cần kiểm tra trực tiếp các false positive và false negative đại diện.

Một taxonomy lỗi tốt thường chỉ ra hướng cải thiện rõ ràng hơn việc tiếp tục tuning hyperparameter một cách mù quáng.

## Đánh giá theo subgroup và Fairness

Nếu hệ thống ảnh hưởng tới nhiều nhóm khác nhau, nên báo cáo metric theo subgroup.

Average score tốt có thể che giấu chênh lệch lớn ở một nhóm nhỏ.

Tuy nhiên metric của nhóm ít mẫu có statistical uncertainty cao, vì vậy cần báo cáo cả số lượng và confidence interval.

Fairness cũng không thể thu gọn về một metric duy nhất. Equalized odds, demographic parity và calibration có thể xung đột khi base rate giữa các nhóm khác nhau.

## Offline và Online Evaluation

Offline test đo performance trên dữ liệu lịch sử hoặc replay.

Production lại có feedback loop và tương tác người dùng.

A/B test hoặc online experiment đo causal impact của thay đổi khi được deploy thật, nhưng cần guardrail và thiết kế thí nghiệm đúng.

Ví dụ recommender có NDCG offline cao hơn chưa chắc tăng long-term retention vì hành vi người dùng sẽ thích nghi với feed mới.

## Leakage trong Evaluation

Leakage có thể đến từ preprocessing fit trên toàn bộ dataset, cùng entity xuất hiện ở train/test, feature chứa thông tin tương lai, feature dẫn xuất từ target hoặc benchmark contamination.

Một metric tuyệt đẹp trên test set bị leakage gần như không có giá trị chứng minh.

## Đánh giá dưới Distribution Shift

Ngoài IID test set, nên có stress set cho các tình huống như thời điểm tương lai hơn, region hoặc domain mới, edge case hiếm, input bị nhiễu hoặc hỏng, và các lát cắt adversarial hoặc worst-case.

Robustness là hành vi qua nhiều điều kiện khác nhau, không phải chỉ average metric trên một distribution duy nhất.

## Đánh giá theo chi phí

Expected cost:

\[
EC=FP\cdot C_{FP}+FN\cdot C_{FN}+...
\]

có thể gần business objective hơn F1.

Nếu benefit và cost thay đổi theo từng case, hệ thống thậm chí có thể tính expected value cho từng sample thay vì dùng một threshold cố định cho tất cả.

## Reproducibility

Evaluation cần version ít nhất:

```text
model version
code version
dataset snapshot
feature pipeline
metric implementation
random seed
threshold / config
```

Nếu không, score sau này rất khó audit hoặc tái lập.

## Preview về đánh giá LLM

LLM làm evaluation khó hơn vì đầu ra mở và nhiều câu trả lời khác nhau có thể đều hợp lệ.

Exact match thường quá cứng; LLM-as-a-judge có bias; human evaluation đắt; benchmark có thể bị contamination.

Phần LLM phía sau sẽ đi sâu hơn, nhưng các nguyên tắc cốt lõi vẫn giống nhau: định nghĩa task, dữ liệu đại diện, evaluation độc lập, uncertainty và phân tích failure mode.

## Mô hình tư duy

```text
Mục tiêu deployment
      ↓
Population đánh giá
      ↓
Metric + threshold
      ↓
Uncertainty + slice
      ↓
Phân tích lỗi
      ↓
Quyết định deploy / sửa / monitor
```

## Các hiểu lầm thường gặp

### “AUC cao nghĩa classifier production tốt”

Không. AUC không nói calibration, threshold vận hành, latency, subgroup performance hay business cost.

### “Test set chỉ cần đủ lớn”

Không. Tính đại diện và tính độc lập quan trọng không kém sample size.

### “F1 cân bằng precision và recall nên luôn phù hợp”

Không. F1 bỏ qua TN và áp đặt một kiểu cân bằng cụ thể giữa precision và recall; nó không mã hóa mọi business cost.

### “Một benchmark là đủ để so mô hình”

Không. Benchmark chỉ đại diện một task distribution cụ thể và có thể bị contamination hoặc bị tối ưu quá mức theo thời gian.

## Liên kết kiến thức

Evaluation tổng hợp [Thống kê](../01_mathematical_foundations/03_statistics_for_ai.md), [Training/Validation/Testing](./03_training_validation_and_testing.md), [Loss và Risk](./04_loss_objective_and_risk.md), [Bias–Variance](./14_bias_variance_and_generalization.md) và mở đường tới production monitoring, đánh giá RAG/LLM và AI Safety.