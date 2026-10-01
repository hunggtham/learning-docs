# Mô hình (model / 모델) Evaluation: đo đúng thứ mà hệ thống thực sự cần

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Mô hình (model / 모델) Evaluation: đo đúng thứ mà hệ thống thực sự cần**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Bắt đầu từ triển khai (deployment / 배포) question** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **Confusion ma trận (matrix / 행렬)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Mô hình (model / 모델) Evaluation (모델 평가 / đánh giá mô hình) không phải bước cuối để “in một con số accuracy”. Nó là quá trình thiết kế bằng chứng (evidence / 증거) để trả lời: mô hình (model / 모델) có hoạt động đủ tốt trên population, subgroup, operating điều kiện (condition / 조건) và nghiệp vụ (business / 비즈니스) mục tiêu (objective / 목표) mà hệ thống (system / 시스템) sẽ gặp hay không?

Một chỉ số (metric / 지표) đơn lẻ hiếm khi trả lời đủ. Evaluation tốt cần nối **dataset thiết kế (design / 설계) → chỉ số (metric / 지표) → threshold → bất định (uncertainty / 불확실성) → lỗi (error / 오류) phân tích (analysis / 분석) → triển khai (deployment / 배포) các ràng buộc (constraints / 제약조건들)**.

## Bắt đầu từ triển khai (deployment / 배포) question

Trước khi chọn chỉ số (metric / 지표), cần biết mô hình (model / 모델) sẽ được dùng thế nào.

Fraud mô hình (model / 모델): có bao nhiêu cases rà soát (review / 검토) mỗi ngày? False negative mất bao nhiêu tiền? False positive gây friction gì?

Medical screening: ưu tiên sensitivity hay specificity? Ai chịu hậu quả của missed trường hợp (case / 사례)?

Tìm kiếm (search / 검색)/recommender: ranking chất lượng (quality / 품질) ở top positions quan trọng hơn toàn cục (global / 전역) classification accuracy.

LLM: tính đúng đắn (correctness / 정확성), factuality, instruction following, độ trễ (latency / 지연 시간), an toàn (safety / 안전) và chi phí (cost / 비용) có thể cần evaluation riêng.

Chỉ số (metric / 지표) phải follow use trường hợp (case / 사례), không ngược lại.

> **Chuyển mạch:** Trong **Mô hình (model / 모델) Evaluation: đo đúng thứ mà hệ thống thực sự cần**, **Confusion ma trận (matrix / 행렬)** tiếp nhận điểm tựa từ **Bắt đầu từ triển khai (deployment / 배포) question** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Accuracy và cơ sở (base / 기반) tỷ lệ (rate / 비율)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Confusion ma trận (matrix / 행렬)

Nhị phân (binary / 이진) classification:

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

Không chỉ số (metric / 지표) nào “tốt nhất” universal. Chúng encode priorities khác nhau.

> **Chuyển mạch:** Ở chặng này của **Mô hình (model / 모델) Evaluation: đo đúng thứ mà hệ thống thực sự cần**, **Accuracy và cơ sở (base / 기반) tỷ lệ (rate / 비율)** tiếp nhận điểm tựa từ **Confusion ma trận (matrix / 행렬)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Precision–Recall sự đánh đổi (trade-off / 트레이드오프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Accuracy và cơ sở (base / 기반) tỷ lệ (rate / 비율)

Accuracy:

\[
\frac{TP+TN}{N}
\]

có thể misleading với imbalance. Nếu disease prevalence 1%, classifier luôn negative đạt 99% accuracy nhưng recall = 0.

Luôn so mô hình (model / 모델) với meaningful baseline.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Mô hình (model / 모델) Evaluation: đo đúng thứ mà hệ thống thực sự cần**, **Precision–Recall sự đánh đổi (trade-off / 트레이드오프)** tiếp nhận điểm tựa từ **Accuracy và cơ sở (base / 기반) tỷ lệ (rate / 비율)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **ROC Curve** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Precision–Recall sự đánh đổi (trade-off / 트레이드오프)

Lower threshold thường tăng recall nhưng giảm precision. Higher threshold thường ngược lại.

Threshold selection là **quyết định (decision / 결정) chính sách (policy / 정책)**, không phải intrinsic mô hình (model / 모델) thuộc tính (property / 속성).

Nếu nghiệp vụ (business / 비즈니스) rà soát (review / 검토) sức chứa (capacity / 용량) `K`, có thể evaluate Precision@K hoặc expected giá trị (value / 값) top-K thay vì threshold cố định.

> **Chuyển mạch:** Trong **Mô hình (model / 모델) Evaluation: đo đúng thứ mà hệ thống thực sự cần**, **ROC Curve** tiếp nhận điểm tựa từ **Precision–Recall sự đánh đổi (trade-off / 트레이드오프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Precision-Recall Curve** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

ROC-AUC có interpretation: xác suất (probability / 확률) một random positive được rank cao hơn random negative.

AUC đo ranking, không đảm bảo calibrated probabilities hay hiệu năng (performance / 성능) ở threshold operational cụ thể.

> **Chuyển mạch:** Ở chặng này của **Mô hình (model / 모델) Evaluation: đo đúng thứ mà hệ thống thực sự cần**, **Precision-Recall Curve** tiếp nhận điểm tựa từ **ROC Curve** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Log mất mát (loss / 손실) và Brier Score** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Precision-Recall Curve

PR curve đặc biệt hữu ích khi positive rare. Precision trực tiếp chịu ảnh hưởng cơ sở (base / 기반) tỷ lệ (rate / 비율), nên phản ánh alert burden tốt hơn ROC trong nhiều anomaly/fraud tasks.

PR-AUC giữa datasets có prevalence khác nhau cần interpret cẩn thận vì baseline precision thay theo positive tỷ lệ (rate / 비율).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Mô hình (model / 모델) Evaluation: đo đúng thứ mà hệ thống thực sự cần**, **Log mất mát (loss / 손실) và Brier Score** tiếp nhận điểm tựa từ **Precision-Recall Curve** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Calibration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Log mất mát (loss / 손실) và Brier Score

Nếu xác suất (probability / 확률) chất lượng (quality / 품질) quan trọng, classification accuracy không đủ.

Log mất mát (loss / 손실):

\[
-rac1n\sum_i[y_i\log p_i+(1-y_i)\log(1-p_i)]
\]

phạt confident wrong predictions mạnh.

Brier score:

\[
\frac1n\sum_i(p_i-y_i)^2
\]

đo squared xác suất (probability / 확률) lỗi (error / 오류).

> **Chuyển mạch:** Trong **Mô hình (model / 모델) Evaluation: đo đúng thứ mà hệ thống thực sự cần**, **Calibration** tiếp nhận điểm tựa từ **Log mất mát (loss / 손실) và Brier Score** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Regression Metrics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Calibration

Mô hình (model / 모델) calibrated nếu among predictions near `p=0.7`, khoảng 70% positive về lâu dài trên relevant population.

Calibration curve/độ tin cậy (reliability / 신뢰성) diagram so predicted xác suất (probability / 확률) bins với empirical frequency.

Calibration có thể degrade under phân phối (distribution / 분포) shift dù discrimination/ranking vẫn tốt.

Techniques như Platt scaling, isotonic regression hoặc temperature scaling cần fit trên held-out calibration dữ liệu (data / 데이터).

> **Chuyển mạch:** Ở chặng này của **Mô hình (model / 모델) Evaluation: đo đúng thứ mà hệ thống thực sự cần**, **Regression Metrics** tiếp nhận điểm tựa từ **Calibration** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ranking Metrics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

MAPE có issue khi mục tiêu (target / 대상) gần zero và asymmetric interpretation.

Chỉ số (metric / 지표) nên gắn với lỗi (error / 오류) chi phí (cost / 비용). Nếu lỗi (error / 오류) 100 KRW và 1,000,000 KRW không cùng consequence, generic MAE có thể không phù hợp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Mô hình (model / 모델) Evaluation: đo đúng thứ mà hệ thống thực sự cần**, **Ranking Metrics** tiếp nhận điểm tựa từ **Regression Metrics** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Confidence Intervals** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ranking Metrics

Tìm kiếm (search / 검색)/recommendation thường quan tâm top results.

**Precision@K**, **Recall@K** đo relevant items trong top K.

Discounted Cumulative Gain:

\[
DCG@K=\sum_{i=1}^{K}\frac{rel_i}{\log_2(i+1)}
\]

NDCG normalize theo ideal ranking.

Mean Reciprocal Rank phù hợp khi vị trí relevant kết quả (result / 결과) đầu tiên quan trọng:

\[
MRR=\frac1N\sum_q\frac1{rank_q}
\]

Các chỉ số (metric / 지표) này sẽ quay lại trong Retrieval/RAG.

> **Chuyển mạch:** Trong **Mô hình (model / 모델) Evaluation: đo đúng thứ mà hệ thống thực sự cần**, **Confidence Intervals** tiếp nhận điểm tựa từ **Ranking Metrics** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Statistical Significance vs Practical Significance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Confidence Intervals

Một điểm (point / 지점) estimate như accuracy 0.91 không nói bất định (uncertainty / 불확실성).

Bootstrap có thể resample evaluation examples để estimate confidence interval cho chỉ số (metric / 지표) phức tạp.

Với correlated/grouped dữ liệu (data / 데이터), bootstrap đơn vị (unit / 단위) phải respect phụ thuộc (dependency / 의존성), ví dụ resample users chứ không random rows nếu rows cùng người dùng (user / 사용자) correlated.

> **Chuyển mạch:** Ở chặng này của **Mô hình (model / 모델) Evaluation: đo đúng thứ mà hệ thống thực sự cần**, **Statistical Significance vs Practical Significance** tiếp nhận điểm tựa từ **Confidence Intervals** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lỗi (error / 오류) phân tích (analysis / 분석)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Statistical Significance vs Practical Significance

Mô hình (model / 모델) B AUC 0.901 vs A 0.899 có thể statistically significant trên millions samples nhưng nghiệp vụ (business / 비즈니스) gain cực nhỏ.

Ngược lại improvement nhỏ toàn cục (global / 전역) có thể rất quan trọng ở high-value subgroup.

Luôn hỏi tác động (effect / 효과) kích thước (size / 크기) và operational impact.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Mô hình (model / 모델) Evaluation: đo đúng thứ mà hệ thống thực sự cần**, **Lỗi (error / 오류) phân tích (analysis / 분석)** tiếp nhận điểm tựa từ **Statistical Significance vs Practical Significance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Subgroup Evaluation và Fairness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lỗi (error / 오류) phân tích (analysis / 분석)

Aggregate chỉ số (metric / 지표) che giấu thất bại (failure / 실패) modes. Cần slice theo:

- geography;
- thiết bị (device / 장치);
- ngôn ngữ (language / 언어);
- customer segment;
- thời gian (time / 시간) period;
- mục tiêu (target / 대상) difficulty;
- dữ liệu (data / 데이터) chất lượng (quality / 품질) trạng thái (state / 상태).

Sau đó inspect representative false positives/negatives.

Lỗi (error / 오류) taxonomy thường dẫn đến improvement rõ hơn blind hyperparameter tuning.

> **Chuyển mạch:** Trong **Mô hình (model / 모델) Evaluation: đo đúng thứ mà hệ thống thực sự cần**, **Subgroup Evaluation và Fairness** tiếp nhận điểm tựa từ **Lỗi (error / 오류) phân tích (analysis / 분석)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Offline vs Online Evaluation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Subgroup Evaluation và Fairness

Nếu hệ thống (system / 시스템) ảnh hưởng groups khác nhau, report chỉ số (metric / 지표) theo subgroup. Aggregate score tốt có thể che severe disparity.

Nhưng subgroup phân tích (analysis / 분석) cần sample-size bất định (uncertainty / 불확실성); group quá nhỏ có chỉ số (metric / 지표) noisy.

Fairness không thể thu gọn thành một chỉ số (metric / 지표) duy nhất vì definitions như equalized odds, demographic parity và calibration có thể xung đột dưới differing cơ sở (base / 기반) rates.

> **Chuyển mạch:** Ở chặng này của **Mô hình (model / 모델) Evaluation: đo đúng thứ mà hệ thống thực sự cần**, **Offline vs Online Evaluation** tiếp nhận điểm tựa từ **Subgroup Evaluation và Fairness** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dữ liệu (data / 데이터) Leakage trong Evaluation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Offline vs Online Evaluation

Offline kiểm thử (test / 테스트) đo historical/replayed hiệu năng (performance / 성능). môi trường vận hành (production / 운영 환경) hành vi (behavior / 동작) có vòng phản hồi (feedback loop / 피드백 루프) và người dùng (user / 사용자) tương tác (interaction / 상호작용).

A/B kiểm thử (test / 테스트) hoặc online experiment đo nhân quả (causal / 인과적) impact của deployed thay đổi (change / 변경), nhưng cần guardrails và proper experimental thiết kế (design / 설계).

Recommendation mô hình (model / 모델) offline NDCG cao hơn chưa chắc increase long-term retention; người dùng (user / 사용자) hành vi (behavior / 동작) adapts.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Mô hình (model / 모델) Evaluation: đo đúng thứ mà hệ thống thực sự cần**, **Offline vs Online Evaluation** nêu điều cần giải thích; **Dữ liệu (data / 데이터) Leakage trong Evaluation** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Evaluation under phân phối (distribution / 분포) Shift** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dữ liệu (data / 데이터) Leakage trong Evaluation

Leakage có thể đến từ:

- preprocessing fit trên full dataset;
- same thực thể (entity / 엔터티) xuất hiện train/kiểm thử (test / 테스트);
- future info trong features;
- target-derived features;
- benchmark contamination.

Một chỉ số (metric / 지표) tuyệt đẹp trên leaked kiểm thử (test / 테스트) set không có giá trị (value / 값).

> **Chuyển mạch:** Trong **Mô hình (model / 모델) Evaluation: đo đúng thứ mà hệ thống thực sự cần**, **Dữ liệu (data / 데이터) Leakage trong Evaluation** nêu điều cần giải thích; **Evaluation under phân phối (distribution / 분포) Shift** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Cost-Sensitive Evaluation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Evaluation under phân phối (distribution / 분포) Shift

Ngoài IID kiểm thử (test / 테스트) set, nên có stress sets:

- later thời gian (time / 시간) period;
- new region/lĩnh vực (domain / 도메인);
- rare edge cases;
- corrupted/noisy inputs;
- adversarial or worst-case slices.

Robustness là hành vi (behavior / 동작) qua conditions, không chỉ average chỉ số (metric / 지표).

> **Chuyển mạch:** Ở chặng này của **Mô hình (model / 모델) Evaluation: đo đúng thứ mà hệ thống thực sự cần**, **Cost-Sensitive Evaluation** tiếp nhận điểm tựa từ **Evaluation under phân phối (distribution / 분포) Shift** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Reproducibility** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cost-Sensitive Evaluation

Expected chi phí (cost / 비용):

\[
EC=FP\cdot C_{FP}+FN\cdot C_{FN}+...
\]

có thể gần nghiệp vụ (business / 비즈니스) mục tiêu (objective / 목표) hơn F1.

Nếu benefit/chi phí (cost / 비용) varies per trường hợp (case / 사례), quyết định (decision / 결정) có thể dùng expected giá trị (value / 값) per mẫu (sample / 표본) thay fixed threshold.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Mô hình (model / 모델) Evaluation: đo đúng thứ mà hệ thống thực sự cần**, **Reproducibility** tiếp nhận điểm tựa từ **Cost-Sensitive Evaluation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **LLM Evaluation Preview** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reproducibility

Evaluation cần phiên bản (version / 버전):

```text
model version
code version
dataset snapshot
feature pipeline
metric implementation
random seed
threshold/config
```

Nếu không, score không kiểm tra (audit / 감사) được.

> **Chuyển mạch:** Trong **Mô hình (model / 모델) Evaluation: đo đúng thứ mà hệ thống thực sự cần**, **LLM Evaluation Preview** tiếp nhận điểm tựa từ **Reproducibility** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## LLM Evaluation Preview

LLM làm evaluation khó hơn vì đầu ra (output / 출력) open-ended và multiple answers có thể acceptable. chính xác (exact / 정확한) match thường quá strict; LLM-as-a-judge có độ lệch (bias / 편향); human evaluation đắt; benchmark contamination possible.

Sau này `08_large_language_models/14_llm_evaluation.md` sẽ mở rộng, nhưng principles vẫn giống: tác vụ (task / 작업) definition, representative dữ liệu (data / 데이터), independent evaluation, bất định (uncertainty / 불확실성) và thất bại (failure / 실패) phân tích (analysis / 분석).

> **Chuyển mạch:** Ở chặng này của **Mô hình (model / 모델) Evaluation: đo đúng thứ mà hệ thống thực sự cần**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **LLM Evaluation Preview** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Mô hình (model / 모델) Evaluation: đo đúng thứ mà hệ thống thực sự cần**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “AUC cao nghĩa classifier môi trường vận hành (production / 운영 환경) tốt”

AUC không nói calibration, operating threshold, độ trễ (latency / 지연 시간), subgroup hiệu năng (performance / 성능) hay nghiệp vụ (business / 비즈니스) chi phí (cost / 비용).

### “kiểm thử (test / 테스트) set chỉ cần đủ lớn”

Representativeness và independence quan trọng không kém kích thước (size / 크기).

### “F1 cân bằng precision/recall nên luôn fair”

F1 bỏ qua TN và implicitly weight precision/recall theo harmonic mean, không encode mọi nghiệp vụ (business / 비즈니스) chi phí (cost / 비용).

### “Một benchmark đủ để so các mô hình (models / 모델들)”

Benchmark chỉ đo một sampled tác vụ (task / 작업) phân phối (distribution / 분포) và dễ bị contamination/tối ưu hóa (optimization / 최적화) pressure.

> **Chuyển mạch:** Trong **Mô hình (model / 모델) Evaluation: đo đúng thứ mà hệ thống thực sự cần**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Evaluation tổng hợp [Statistics](../01_mathematical_foundations/03_statistics_for_ai.md), [Training/Validation/Testing](./03_training_validation_and_testing.md), [Loss and Risk](./04_loss_objective_and_risk.md), [Bias–Variance](./14_bias_variance_and_generalization.md) và mở đường tới production monitoring, RAG/LLM evaluation, AI Safety.

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
