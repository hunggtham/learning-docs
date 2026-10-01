# Bất định (uncertainty / 불확실성) và Calibration trong AI

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Bất định (uncertainty / 불확실성) và Calibration trong AI**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Xác suất (probability / 확률) đầu ra (output / 출력) không tự động là Confidence thật** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Discrimination và Calibration** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Một mô hình không chỉ cần dự đoán đúng mà còn cần biểu diễn **mức độ chắc chắn** một cách đáng tin. **bất định (uncertainty / 불확실성)** và **hiệu chỉnh xác suất (calibration / 보정)** giúp biến score thành thông tin hữu ích cho decision-making.

## Xác suất (probability / 확률) đầu ra (output / 출력) không tự động là Confidence thật

Classifier có thể trả:

\[
P(y=1|x)=0.95
\]

Nhưng 0.95 chỉ có ý nghĩa xác suất thực dụng nếu mô hình (model / 모델) được calibration tốt trên population tương ứng.

Một thuộc tính (property / 속성) calibration lý tưởng là:

> Trong các trường hợp (case / 사례) mà mô hình (model / 모델) dự đoán xác suất 0.8, khoảng 80% thực sự đúng.

> **Chuyển mạch:** Output probability không tự động là confidence; discrimination đo khả năng xếp hạng, calibration đo độ khớp xác suất với tần suất thực, và reliability diagram giúp thấy lệch ở đâu.

## Discrimination và Calibration

Một mô hình (model / 모델) có thể rank positive rất tốt nhưng vẫn quá tự tin.

AUC đo discrimination; calibration đo chất lượng của xác suất (probability / 확률). Đây là hai thuộc tính (property / 속성) khác nhau.

> **Chuyển mạch:** Ở chặng này của **Bất định (uncertainty / 불확실성) và Calibration trong AI**, **Độ tin cậy (reliability / 신뢰성) Diagram** tiếp nhận điểm tựa từ **Discrimination và Calibration** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Expected Calibration lỗi (error / 오류)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ tin cậy (reliability / 신뢰성) Diagram

Có thể chia prediction thành các bin theo confidence rồi so sánh:

```text
predicted confidence ↔ observed accuracy
```

Nếu mô hình (model / 모델) dự đoán 0.9 nhưng observed accuracy chỉ 0.7 thì mô hình (model / 모델) đang overconfident.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bất định (uncertainty / 불확실성) và Calibration trong AI**, **Expected Calibration lỗi (error / 오류)** tiếp nhận điểm tựa từ **Độ tin cậy (reliability / 신뢰성) Diagram** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Brier Score** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Expected Calibration lỗi (error / 오류)

ECE thường xấp xỉ weighted gap giữa confidence và accuracy qua các bin.

Nó hữu ích như summary chỉ số (metric / 지표) nhưng nhạy với cách chia bin và có thể che vấn đề ở subgroup.

> **Chuyển mạch:** Trong **Bất định (uncertainty / 불확실성) và Calibration trong AI**, **Brier Score** tiếp nhận điểm tựa từ **Expected Calibration lỗi (error / 오류)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Log mất mát (loss / 손실)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Brier Score

Với bài toán nhị phân:

\[
BS=\frac{1}{N}\sum_i(p_i-y_i)^2
\]

Brier score đo sai số của xác suất (probability / 확률) và có thể phân rã để phân tích calibration cùng khả năng phân biệt.

> **Chuyển mạch:** Ở chặng này của **Bất định (uncertainty / 불확실성) và Calibration trong AI**, **Log mất mát (loss / 손실)** tiếp nhận điểm tựa từ **Brier Score** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Các phương pháp Calibration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Log mất mát (loss / 손실)

Negative log-likelihood phạt rất mạnh những prediction sai nhưng quá tự tin:

\[
L=-[y\log p+(1-y)\log(1-p)]
\]

Hai mô hình (model / 모델) có accuracy tương tự nhưng mô hình (model / 모델) overconfident có thể có log mất mát (loss / 손실) tệ hơn nhiều.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bất định (uncertainty / 불확실성) và Calibration trong AI**, **Các phương pháp Calibration** tiếp nhận điểm tựa từ **Log mất mát (loss / 손실)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Calibration Set** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Bất định (uncertainty / 불확실성) và Calibration trong AI**, **Calibration Set** tiếp nhận điểm tựa từ **Các phương pháp Calibration** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Aleatoric và Epistemic bất định (uncertainty / 불확실성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Calibration Set

Calibration phải dùng held-out dữ liệu (data / 데이터) thay vì dữ liệu huấn luyện (training data / 학습 데이터). Nếu triển khai (deployment / 배포) phân phối (distribution / 분포) thay đổi thì calibration cũng có thể drift.

> **Chuyển mạch:** Ở chặng này của **Bất định (uncertainty / 불확실성) và Calibration trong AI**, **Aleatoric và Epistemic bất định (uncertainty / 불확실성)** tiếp nhận điểm tựa từ **Calibration Set** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bất định (uncertainty / 불확실성) với dữ liệu ngoài phân phối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Aleatoric và Epistemic bất định (uncertainty / 불확실성)

**Bất định nội tại của dữ liệu (aleatoric uncertainty)** đến từ noise hoặc ambiguity vốn có trong hiện tượng.

**Bất định do thiếu hiểu biết (epistemic uncertainty)** đến từ thiếu dữ liệu (data / 데이터), thiếu kiến thức (knowledge / 지식) hoặc bất định (uncertainty / 불확실성) của mô hình (model / 모델).

Không phải mô hình (model / 모델) nào cũng tách hai loại này rõ ràng, nhưng distinction giúp lập luận (reasoning / 추론) về cách hệ thống nên phản ứng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bất định (uncertainty / 불확실성) và Calibration trong AI**, **Aleatoric và Epistemic bất định (uncertainty / 불확실성)** nêu điều cần giải thích; **Bất định (uncertainty / 불확실성) với dữ liệu ngoài phân phối** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Deep Ensemble** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bất định (uncertainty / 불확실성) với dữ liệu ngoài phân phối

Mô hình (model / 모델) có thể tự tin nhưng sai trên **out-of-distribution (OOD)** đầu vào (input / 입력). Softmax confidence thường không đủ để phát hiện OOD.

Các cách tiếp cận có thể dùng ensemble, năng lượng (energy / 에너지) score, density hoặc embedding distance và detector chuyên biệt, nhưng không có một giải pháp universal.

> **Chuyển mạch:** Trong **Bất định (uncertainty / 불확실성) và Calibration trong AI**, **Bất định (uncertainty / 불확실성) với dữ liệu ngoài phân phối** nêu điều cần giải thích; **Deep Ensemble** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Monte Carlo Dropout** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Deep Ensemble

Train nhiều mô hình (model / 모델) hoặc nhiều seed rồi quan sát mức variation giữa prediction.

Lợi ích:

- bất định (uncertainty / 불확실성) estimate thường tốt hơn single mô hình (model / 모델);
- tăng robustness.

Chi phí là huấn luyện (training / 학습) và serving tăng theo số mô hình (model / 모델).

> **Chuyển mạch:** Ở chặng này của **Bất định (uncertainty / 불확실성) và Calibration trong AI**, **Monte Carlo Dropout** tiếp nhận điểm tựa từ **Deep Ensemble** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Góc nhìn Bayesian** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Monte Carlo Dropout

Có thể bật dropout ở suy luận (inference / 추론) và chạy nhiều mẫu (sample / 표본) để xấp xỉ predictive bất định (uncertainty / 불확실성). Cách này thực dụng trong một số setting nhưng không phải chính xác (exact / 정확한) Bayesian suy luận (inference / 추론).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bất định (uncertainty / 불확실성) và Calibration trong AI**, **Góc nhìn Bayesian** tiếp nhận điểm tựa từ **Monte Carlo Dropout** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Selective Prediction và Abstention** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Góc nhìn Bayesian

Bayesian predictive phân phối (distribution / 분포) lý tưởng tích phân trên posterior của parameter:

\[
p(y|x,D)=\int p(y|x,\theta)p(\theta|D)d\theta
\]

Với large neural mạng (network / 네트워크), chính xác (exact / 정확한) tích hợp (integration / 통합) hầu như không khả thi nên phải dùng approximation.

> **Chuyển mạch:** Trong **Bất định (uncertainty / 불확실성) và Calibration trong AI**, **Selective Prediction và Abstention** tiếp nhận điểm tựa từ **Góc nhìn Bayesian** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Conformal Prediction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Selective Prediction và Abstention

Hệ thống có thể từ chối quyết định khi bất định (uncertainty / 불확실성) cao:

```text
confidence cao → tự động quyết định
confidence trung bình → gọi thêm model / tool
confidence thấp → human review / fail safely
```

Evaluation nên xem **coverage–rủi ro (risk / 위험) curve**: abstain nhiều hơn thường tăng chất lượng trên phần được trả lời nhưng giảm automation coverage.

> **Chuyển mạch:** Ở chặng này của **Bất định (uncertainty / 불확실성) và Calibration trong AI**, **Conformal Prediction** tiếp nhận điểm tựa từ **Selective Prediction và Abstention** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Confidence của LLM** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Conformal Prediction

Conformal phương thức (method / 메서드) có thể tạo prediction set với coverage guarantee dưới các giả định (assumption / 가정) như exchangeability.

Ví dụ classification có thể trả `{A, C}` thay vì một lớp (class / 클래스) duy nhất khi bất định (uncertainty / 불확실성) cao.

Guarantee mang ý nghĩa thống kê trên population, không bảo đảm mỗi individual trường hợp (case / 사례).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bất định (uncertainty / 불확실성) và Calibration trong AI**, **Confidence của LLM** tiếp nhận điểm tựa từ **Conformal Prediction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Confidence trong RAG** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Confidence của LLM

Đơn vị từ (token / 토큰) xác suất (probability / 확률) không trực tiếp bằng factual confidence. Một hallucination trôi chảy vẫn có thể có đơn vị từ (token / 토큰) xác suất (probability / 확률) cao.

LLM bất định (uncertainty / 불확실성) có thể được ước lượng qua:

- self-consistency;
- multiple mẫu (sample / 표본);
- verifier mô hình (model / 모델);
- retrieval hỗ trợ (support / 지원);
- task-specific confidence đã calibration.

Việc mô hình (model / 모델) tự nói “tôi chắc 90%” không tự động có nghĩa con số đó đã được hiệu chỉnh.

> **Chuyển mạch:** Trong **Bất định (uncertainty / 불확실성) và Calibration trong AI**, **Confidence trong RAG** tiếp nhận điểm tựa từ **Confidence của LLM** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bất định (uncertainty / 불확실성) trong tác nhân (agent / 에이전트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Confidence trong RAG

RAG có nhiều nguồn bất định (uncertainty / 불확실성):

```text
retrieval relevance
source reliability
answer generation
citation support
```

Combined confidence score phải được kiểm tra hợp lệ (validation / 검증); không nên nhân các score tùy ý khi chưa calibration.

> **Chuyển mạch:** Ở chặng này của **Bất định (uncertainty / 불확실성) và Calibration trong AI**, **Bất định (uncertainty / 불확실성) trong tác nhân (agent / 에이전트)** tiếp nhận điểm tựa từ **Confidence trong RAG** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Calibration dưới phân phối (distribution / 분포) Shift** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bất định (uncertainty / 불확실성) trong tác nhân (agent / 에이전트)

Tác nhân (agent / 에이전트) có bất định (uncertainty / 불확실성) ở plan, công cụ (tool / 도구) argument và môi trường (environment / 환경) trạng thái (state / 상태). Với hành động (action / 동작) có impact cao, nên dùng verifier hoặc approval rõ ràng thay vì chỉ dựa vào mô hình (model / 모델) confidence.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bất định (uncertainty / 불확실성) và Calibration trong AI**, **Calibration dưới phân phối (distribution / 분포) Shift** tiếp nhận điểm tựa từ **Bất định (uncertainty / 불확실성) trong tác nhân (agent / 에이전트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quyết định (decision / 결정) lý thuyết (theory / 이론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Calibration dưới phân phối (distribution / 분포) Shift

Calibration thường giảm chất lượng khi triển khai (deployment / 배포) phân phối (distribution / 분포) khác kiểm tra hợp lệ (validation / 검증) phân phối (distribution / 분포). Vì vậy cần monitoring và recalibration định kỳ khi phù hợp.

> **Chuyển mạch:** Trong **Bất định (uncertainty / 불확실성) và Calibration trong AI**, **Quyết định (decision / 결정) lý thuyết (theory / 이론)** tiếp nhận điểm tựa từ **Calibration dưới phân phối (distribution / 분포) Shift** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quyết định (decision / 결정) lý thuyết (theory / 이론)

Confidence chỉ hữu ích khi được nối với chi phí của hành động.

Chọn hành động (action / 동작) tối thiểu expected mất mát (loss / 손실):

\[
a^*=\arg\min_a\mathbb{E}[L(a,Y)|x]
\]

Xác suất (probability / 확률) chất lượng (quality / 품질) quan trọng vì confidence sai sẽ dẫn tới quyết định (decision / 결정) sai.

> **Chuyển mạch:** Ở chặng này của **Bất định (uncertainty / 불확실성) và Calibration trong AI**, **Mô hình tư duy** gom các mảnh từ **Quyết định (decision / 결정) lý thuyết (theory / 이론)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những nhầm lẫn thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Prediction nói model nghĩ điều gì sẽ xảy ra.
Calibration nói mức confidence mà model đưa ra có đáng tin hay không.
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bất định (uncertainty / 불확실성) và Calibration trong AI**, **Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những nhầm lẫn thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những nhầm lẫn thường gặp

### “Softmax 0.99 nghĩa chắc chắn 99%”

Không nếu mô hình (model / 모델) chưa calibration hoặc đầu vào (input / 입력) là OOD.

### “Accuracy cao nghĩa bất định (uncertainty / 불확실성) estimate tốt”

Không. Đây là hai thuộc tính (property / 속성) khác nhau.

### “LLM nói ‘không chắc’ nghĩa là bất định (uncertainty / 불확실성) đã calibration”

Không. Natural-language self-assessment cần empirical kiểm tra hợp lệ (validation / 검증).

> **Chuyển mạch:** Trong **Bất định (uncertainty / 불확실성) và Calibration trong AI**, **Những nhầm lẫn thường gặp** đã nêu tiêu chí phân biệt, còn **Liên kết kiến thức** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Xem [Probability](../01_mathematical_foundations/02_probability_for_ai.md), [Statistics](../01_mathematical_foundations/03_statistics_for_ai.md), [Evaluation Foundations](./00_evaluation_foundations.md), [Robustness](./03_robustness_and_distribution_shift.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
