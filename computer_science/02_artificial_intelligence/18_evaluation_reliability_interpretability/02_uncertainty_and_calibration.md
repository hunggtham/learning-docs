# Uncertainty và Calibration trong AI

Một mô hình không chỉ cần dự đoán đúng mà còn cần biểu diễn **mức độ chắc chắn** một cách đáng tin. **Bất định (uncertainty / 불확실성)** và **hiệu chỉnh xác suất (calibration / 보정)** giúp biến score thành thông tin hữu ích cho decision-making.

## Probability Output không tự động là Confidence thật

Classifier có thể trả:

\[
P(y=1|x)=0.95
\]

Nhưng 0.95 chỉ có ý nghĩa xác suất thực dụng nếu model được calibration tốt trên population tương ứng.

Một property calibration lý tưởng là:

> Trong các case mà model dự đoán xác suất 0.8, khoảng 80% thực sự đúng.

## Discrimination và Calibration

Một model có thể rank positive rất tốt nhưng vẫn quá tự tin.

AUC đo discrimination; calibration đo chất lượng của probability. Đây là hai property khác nhau.

## Reliability Diagram

Có thể chia prediction thành các bin theo confidence rồi so sánh:

```text
predicted confidence ↔ observed accuracy
```

Nếu model dự đoán 0.9 nhưng observed accuracy chỉ 0.7 thì model đang overconfident.

## Expected Calibration Error

ECE thường xấp xỉ weighted gap giữa confidence và accuracy qua các bin.

Nó hữu ích như summary metric nhưng nhạy với cách chia bin và có thể che vấn đề ở subgroup.

## Brier Score

Với bài toán nhị phân:

\[
BS=\frac{1}{N}\sum_i(p_i-y_i)^2
\]

Brier score đo sai số của probability và có thể phân rã để phân tích calibration cùng khả năng phân biệt.

## Log Loss

Negative log-likelihood phạt rất mạnh những prediction sai nhưng quá tự tin:

\[
L=-[y\log p+(1-y)\log(1-p)]
\]

Hai model có accuracy tương tự nhưng model overconfident có thể có log loss tệ hơn nhiều.

## Các phương pháp Calibration

### Platt Scaling

Fit một logistic mapping trên validation logit hoặc score.

### Temperature Scaling

Với multiclass logit:

\[
p_i=softmax(z_i/T)
\]

`T>1` thường làm distribution mềm hơn và giảm overconfidence.

### Isotonic Regression

Đây là non-parametric monotonic mapping, linh hoạt hơn nhưng cần nhiều calibration data và có nguy cơ overfit.

## Calibration Set

Calibration phải dùng held-out data thay vì training data. Nếu deployment distribution thay đổi thì calibration cũng có thể drift.

## Aleatoric và Epistemic Uncertainty

**Bất định nội tại của dữ liệu (aleatoric uncertainty)** đến từ noise hoặc ambiguity vốn có trong hiện tượng.

**Bất định do thiếu hiểu biết (epistemic uncertainty)** đến từ thiếu data, thiếu knowledge hoặc uncertainty của model.

Không phải model nào cũng tách hai loại này rõ ràng, nhưng distinction giúp reasoning về cách hệ thống nên phản ứng.

## Uncertainty với dữ liệu ngoài phân phối

Model có thể tự tin nhưng sai trên **out-of-distribution (OOD)** input. Softmax confidence thường không đủ để phát hiện OOD.

Các cách tiếp cận có thể dùng ensemble, energy score, density hoặc embedding distance và detector chuyên biệt, nhưng không có một giải pháp universal.

## Deep Ensemble

Train nhiều model hoặc nhiều seed rồi quan sát mức variation giữa prediction.

Lợi ích:

- uncertainty estimate thường tốt hơn single model;
- tăng robustness.

Chi phí là training và serving tăng theo số model.

## Monte Carlo Dropout

Có thể bật dropout ở inference và chạy nhiều sample để xấp xỉ predictive uncertainty. Cách này thực dụng trong một số setting nhưng không phải exact Bayesian inference.

## Góc nhìn Bayesian

Bayesian predictive distribution lý tưởng tích phân trên posterior của parameter:

\[
p(y|x,D)=\int p(y|x,\theta)p(\theta|D)d\theta
\]

Với large neural network, exact integration hầu như không khả thi nên phải dùng approximation.

## Selective Prediction và Abstention

Hệ thống có thể từ chối quyết định khi uncertainty cao:

```text
confidence cao → tự động quyết định
confidence trung bình → gọi thêm model / tool
confidence thấp → human review / fail safely
```

Evaluation nên xem **coverage–risk curve**: abstain nhiều hơn thường tăng chất lượng trên phần được trả lời nhưng giảm automation coverage.

## Conformal Prediction

Conformal method có thể tạo prediction set với coverage guarantee dưới các assumption như exchangeability.

Ví dụ classification có thể trả `{A, C}` thay vì một class duy nhất khi uncertainty cao.

Guarantee mang ý nghĩa thống kê trên population, không bảo đảm mỗi individual case.

## Confidence của LLM

Token probability không trực tiếp bằng factual confidence. Một hallucination trôi chảy vẫn có thể có token probability cao.

LLM uncertainty có thể được ước lượng qua:

- self-consistency;
- multiple sample;
- verifier model;
- retrieval support;
- task-specific confidence đã calibration.

Việc model tự nói “tôi chắc 90%” không tự động có nghĩa con số đó đã được hiệu chỉnh.

## Confidence trong RAG

RAG có nhiều nguồn uncertainty:

```text
retrieval relevance
source reliability
answer generation
citation support
```

Combined confidence score phải được validation; không nên nhân các score tùy ý khi chưa calibration.

## Uncertainty trong Agent

Agent có uncertainty ở plan, tool argument và environment state. Với action có impact cao, nên dùng verifier hoặc approval rõ ràng thay vì chỉ dựa vào model confidence.

## Calibration dưới Distribution Shift

Calibration thường giảm chất lượng khi deployment distribution khác validation distribution. Vì vậy cần monitoring và recalibration định kỳ khi phù hợp.

## Decision Theory

Confidence chỉ hữu ích khi được nối với chi phí của hành động.

Chọn action tối thiểu expected loss:

\[
a^*=\arg\min_a\mathbb{E}[L(a,Y)|x]
\]

Probability quality quan trọng vì confidence sai sẽ dẫn tới decision sai.

## Mô hình tư duy

```text
Prediction nói model nghĩ điều gì sẽ xảy ra.
Calibration nói mức confidence mà model đưa ra có đáng tin hay không.
```

## Những nhầm lẫn thường gặp

### “Softmax 0.99 nghĩa chắc chắn 99%”

Không nếu model chưa calibration hoặc input là OOD.

### “Accuracy cao nghĩa uncertainty estimate tốt”

Không. Đây là hai property khác nhau.

### “LLM nói ‘không chắc’ nghĩa là uncertainty đã calibration”

Không. Natural-language self-assessment cần empirical validation.

## Liên kết kiến thức

Xem [Probability](../01_mathematical_foundations/02_probability_for_ai.md), [Statistics](../01_mathematical_foundations/03_statistics_for_ai.md), [Evaluation Foundations](./00_evaluation_foundations.md), [Robustness](./03_robustness_and_distribution_shift.md).