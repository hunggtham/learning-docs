# Bất định (uncertainty / 불확실성) và Calibration trong AI

> **Mạch đọc:** Đặt **bất định (uncertainty / 불확실성) và Calibration trong AI** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **xác suất (probability / 확률) đầu ra (output / 출력) không tự động là Confidence thật** sang **Discrimination và Calibration**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Một mô hình không chỉ cần dự đoán đúng mà còn cần biểu diễn **mức độ chắc chắn** một cách đáng tin. **bất định (uncertainty / 불확실성)** và **hiệu chỉnh xác suất (calibration / 보정)** giúp biến score thành thông tin hữu ích cho decision-making.

## Xác suất (probability / 확률) đầu ra (output / 출력) không tự động là Confidence thật

Classifier có thể trả:

\[
P(y=1|x)=0.95
\]

Nhưng 0.95 chỉ có ý nghĩa xác suất thực dụng nếu mô hình (model / 모델) được calibration tốt trên population tương ứng.

Một thuộc tính (property / 속성) calibration lý tưởng là:

> Trong các trường hợp (case / 사례) mà mô hình (model / 모델) dự đoán xác suất 0.8, khoảng 80% thực sự đúng.

## Discrimination và Calibration

Một mô hình (model / 모델) có thể rank positive rất tốt nhưng vẫn quá tự tin.

AUC đo discrimination; calibration đo chất lượng của xác suất (probability / 확률). Đây là hai thuộc tính (property / 속성) khác nhau.

## Độ tin cậy (reliability / 신뢰성) Diagram

Có thể chia prediction thành các bin theo confidence rồi so sánh:

```text
predicted confidence ↔ observed accuracy
```

Nếu mô hình (model / 모델) dự đoán 0.9 nhưng observed accuracy chỉ 0.7 thì mô hình (model / 모델) đang overconfident.

## Expected Calibration lỗi (error / 오류)

ECE thường xấp xỉ weighted gap giữa confidence và accuracy qua các bin.

Nó hữu ích như summary chỉ số (metric / 지표) nhưng nhạy với cách chia bin và có thể che vấn đề ở subgroup.

## Brier Score

Với bài toán nhị phân:

\[
BS=\frac{1}{N}\sum_i(p_i-y_i)^2
\]

Brier score đo sai số của xác suất (probability / 확률) và có thể phân rã để phân tích calibration cùng khả năng phân biệt.

## Log mất mát (loss / 손실)

Negative log-likelihood phạt rất mạnh những prediction sai nhưng quá tự tin:

\[
L=-[y\log p+(1-y)\log(1-p)]
\]

Hai mô hình (model / 모델) có accuracy tương tự nhưng mô hình (model / 모델) overconfident có thể có log mất mát (loss / 손실) tệ hơn nhiều.

## Các phương pháp Calibration

### Platt Scaling

Fit một logistic ánh xạ (mapping / 매핑) trên kiểm tra hợp lệ (validation / 검증) logit hoặc score.

### Temperature Scaling

Với multiclass logit:

\[
p_i=softmax(z_i/T)
\]

`T>1` thường làm phân phối (distribution / 분포) mềm hơn và giảm overconfidence.

### Isotonic Regression

Đây là non-parametric monotonic ánh xạ (mapping / 매핑), linh hoạt hơn nhưng cần nhiều calibration dữ liệu (data / 데이터) và có nguy cơ overfit.

## Calibration Set

Calibration phải dùng held-out dữ liệu (data / 데이터) thay vì dữ liệu huấn luyện (training data / 학습 데이터). Nếu triển khai (deployment / 배포) phân phối (distribution / 분포) thay đổi thì calibration cũng có thể drift.

## Aleatoric và Epistemic bất định (uncertainty / 불확실성)

**Bất định nội tại của dữ liệu (aleatoric uncertainty)** đến từ noise hoặc ambiguity vốn có trong hiện tượng.

**Bất định do thiếu hiểu biết (epistemic uncertainty)** đến từ thiếu dữ liệu (data / 데이터), thiếu kiến thức (knowledge / 지식) hoặc bất định (uncertainty / 불확실성) của mô hình (model / 모델).

Không phải mô hình (model / 모델) nào cũng tách hai loại này rõ ràng, nhưng distinction giúp lập luận (reasoning / 추론) về cách hệ thống nên phản ứng.

## Bất định (uncertainty / 불확실성) với dữ liệu ngoài phân phối

Mô hình (model / 모델) có thể tự tin nhưng sai trên **out-of-distribution (OOD)** đầu vào (input / 입력). Softmax confidence thường không đủ để phát hiện OOD.

Các cách tiếp cận có thể dùng ensemble, năng lượng (energy / 에너지) score, density hoặc embedding distance và detector chuyên biệt, nhưng không có một giải pháp universal.

## Deep Ensemble

Train nhiều mô hình (model / 모델) hoặc nhiều seed rồi quan sát mức variation giữa prediction.

Lợi ích:

- bất định (uncertainty / 불확실성) estimate thường tốt hơn single mô hình (model / 모델);
- tăng robustness.

Chi phí là huấn luyện (training / 학습) và serving tăng theo số mô hình (model / 모델).

## Monte Carlo Dropout

Có thể bật dropout ở suy luận (inference / 추론) và chạy nhiều mẫu (sample / 표본) để xấp xỉ predictive bất định (uncertainty / 불확실성). Cách này thực dụng trong một số setting nhưng không phải chính xác (exact / 정확한) Bayesian suy luận (inference / 추론).

## Góc nhìn Bayesian

Bayesian predictive phân phối (distribution / 분포) lý tưởng tích phân trên posterior của parameter:

\[
p(y|x,D)=\int p(y|x,\theta)p(\theta|D)d\theta
\]

Với large neural mạng (network / 네트워크), chính xác (exact / 정확한) tích hợp (integration / 통합) hầu như không khả thi nên phải dùng approximation.

## Selective Prediction và Abstention

Hệ thống có thể từ chối quyết định khi bất định (uncertainty / 불확실성) cao:

```text
confidence cao → tự động quyết định
confidence trung bình → gọi thêm model / tool
confidence thấp → human review / fail safely
```

Evaluation nên xem **coverage–rủi ro (risk / 위험) curve**: abstain nhiều hơn thường tăng chất lượng trên phần được trả lời nhưng giảm automation coverage.

## Conformal Prediction

Conformal phương thức (method / 메서드) có thể tạo prediction set với coverage guarantee dưới các giả định (assumption / 가정) như exchangeability.

Ví dụ classification có thể trả `{A, C}` thay vì một lớp (class / 클래스) duy nhất khi bất định (uncertainty / 불확실성) cao.

Guarantee mang ý nghĩa thống kê trên population, không bảo đảm mỗi individual trường hợp (case / 사례).

## Confidence của LLM

Đơn vị từ (token / 토큰) xác suất (probability / 확률) không trực tiếp bằng factual confidence. Một hallucination trôi chảy vẫn có thể có đơn vị từ (token / 토큰) xác suất (probability / 확률) cao.

LLM bất định (uncertainty / 불확실성) có thể được ước lượng qua:

- self-consistency;
- multiple mẫu (sample / 표본);
- verifier mô hình (model / 모델);
- retrieval hỗ trợ (support / 지원);
- task-specific confidence đã calibration.

Việc mô hình (model / 모델) tự nói “tôi chắc 90%” không tự động có nghĩa con số đó đã được hiệu chỉnh.

## Confidence trong RAG

RAG có nhiều nguồn bất định (uncertainty / 불확실성):

```text
retrieval relevance
source reliability
answer generation
citation support
```

Combined confidence score phải được kiểm tra hợp lệ (validation / 검증); không nên nhân các score tùy ý khi chưa calibration.

## Bất định (uncertainty / 불확실성) trong tác nhân (agent / 에이전트)

Tác nhân (agent / 에이전트) có bất định (uncertainty / 불확실성) ở plan, công cụ (tool / 도구) argument và môi trường (environment / 환경) trạng thái (state / 상태). Với hành động (action / 동작) có impact cao, nên dùng verifier hoặc approval rõ ràng thay vì chỉ dựa vào mô hình (model / 모델) confidence.

## Calibration dưới phân phối (distribution / 분포) Shift

Calibration thường giảm chất lượng khi triển khai (deployment / 배포) phân phối (distribution / 분포) khác kiểm tra hợp lệ (validation / 검증) phân phối (distribution / 분포). Vì vậy cần monitoring và recalibration định kỳ khi phù hợp.

## Quyết định (decision / 결정) lý thuyết (theory / 이론)

Confidence chỉ hữu ích khi được nối với chi phí của hành động.

Chọn hành động (action / 동작) tối thiểu expected mất mát (loss / 손실):

\[
a^*=\arg\min_a\mathbb{E}[L(a,Y)|x]
\]

Xác suất (probability / 확률) chất lượng (quality / 품질) quan trọng vì confidence sai sẽ dẫn tới quyết định (decision / 결정) sai.

## Mô hình tư duy

```text
Prediction nói model nghĩ điều gì sẽ xảy ra.
Calibration nói mức confidence mà model đưa ra có đáng tin hay không.
```

## Những nhầm lẫn thường gặp

### “Softmax 0.99 nghĩa chắc chắn 99%”

Không nếu mô hình (model / 모델) chưa calibration hoặc đầu vào (input / 입력) là OOD.

### “Accuracy cao nghĩa bất định (uncertainty / 불확실성) estimate tốt”

Không. Đây là hai thuộc tính (property / 속성) khác nhau.

### “LLM nói ‘không chắc’ nghĩa là bất định (uncertainty / 불확실성) đã calibration”

Không. Natural-language self-assessment cần empirical kiểm tra hợp lệ (validation / 검증).

## Liên kết kiến thức

Xem [Probability](../01_mathematical_foundations/02_probability_for_ai.md), [Statistics](../01_mathematical_foundations/03_statistics_for_ai.md), [Evaluation Foundations](./00_evaluation_foundations.md), [Robustness](./03_robustness_and_distribution_shift.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 evaluation foundations](./00_evaluation_foundations.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
