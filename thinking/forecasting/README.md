# Forecasting — Dự báo có calibration thay vì đoán chắc chắn

Forecasting (dự báo / 예측) là biến belief về tương lai thành probability hoặc range có thể kiểm tra sau này. Mục tiêu không phải “đoán đúng mọi lần”, mà là **nhiều dự báo lặp lại phải calibrated**: sự kiện gán khoảng 70% nên xảy ra xấp xỉ 70% trong tập đủ lớn và tương đồng.

Probability formal nằm ở [Mathematics](../../mathematics/README.md). Decision consequence nằm ở [Expected Value](../expected-value/README.md) và [Risk](../risk/README.md).

## 1. Forecast phải có resolution condition

Một câu như “thị trường sẽ tốt hơn” quá mơ hồ.

Forecast tốt hơn:

```text
Variable: cái gì được đo?
Threshold / range: bao nhiêu?
Deadline: đến ngày nào?
Source of truth: dữ liệu nào resolve?
Probability: mức tin hiện tại?
```

Không có resolution rule thì hindsight rất dễ sửa lại nghĩa của prediction.

## 2. Base rate trước inside view

Bắt đầu bằng reference class:

> Những case giống thế này trước đây thường kết thúc ra sao?

Sau đó mới cập nhật bằng thông tin riêng của case hiện tại.

```text
outside view / base rate
→ case-specific evidence
→ updated forecast
```

Bỏ base rate làm prediction dễ bị narrative mạnh chi phối.

## 3. Decomposition

Thay câu hỏi lớn bằng các phần nhỏ hơn.

Ví dụ project launch đúng hạn phụ thuộc vào:

```text
requirements stable
× implementation complete
× test pass
× external approval
× deployment succeeds
```

Không nhất thiết nhân probability một cách máy móc nếu events phụ thuộc nhau; decomposition trước hết để expose assumptions.

## 4. Range thay vì point estimate

Một forecast “doanh thu 10 tỷ” thường tạo false precision.

Hãy nghĩ:

```text
central estimate
plausible range
major tail scenarios
```

Range phải đi cùng assumptions. Range rộng không phải dấu hiệu yếu nếu uncertainty thực sự lớn.

## 5. Update theo evidence

Forecast không phải lời hứa phải bảo vệ.

Khi information mới xuất hiện:

```text
prior belief
→ evidence
→ likelihood / diagnosticity
→ posterior belief
```

Không cần tính Bayes chính xác mọi lúc; điều quan trọng là biết evidence nào nên làm confidence thay đổi nhiều hay ít.

## 6. Calibration

Nếu thường xuyên dự báo, lưu lại probability và outcome.

Có thể dùng Brier score cho binary event:

```text
Brier score = (forecast probability - outcome)^2
```

Outcome được mã hóa 1 nếu xảy ra, 0 nếu không. Score thấp hơn là tốt hơn khi so trên cùng loại task và đủ sample.

Không dùng một vài forecast để kết luận khả năng dự báo dài hạn.

## 10. Aggregation, structural break và forecast postmortem

Một forecast riêng lẻ có thể phụ thuộc may/rủi; tập forecast tương đồng mới cho biết calibration. Khi gộp nhiều forecaster hoặc model, ghi rõ chúng có chung source, assumption hay failure mode không; trung bình các dự báo correlated không tạo ra evidence độc lập.

Luôn có một câu hỏi về structural break: cơ chế tạo base rate còn tồn tại không, hay policy, technology, competitor hoặc regime đã đổi? Sau resolution, postmortem phải tách `bad luck`, `bad estimate`, `bad model`, `bad data` và `bad resolution rule`, rồi ghi một update rule có thể áp dụng cho forecast sau. [Calibration & Bayesian Updating](../practice/01_calibration_and_bayesian_updating.md) và [Decision Journal & Postmortem](../practice/04_decision_journal_and_postmortem.md) cung cấp vòng feedback này.

## 7. Scenario ≠ forecast

Scenario hỏi:

> “Nếu trạng thái X xảy ra thì hệ quả là gì?”

Forecast hỏi:

> “X có khả năng xảy ra bao nhiêu?”

Một scenario cực đoan có thể đáng planning dù probability thấp nếu downside rất lớn. Đây là nơi Forecasting nối với [Risk](../risk/README.md).

## 8. Common failure modes

- dùng confidence language nhưng không có probability;
- forecast không có deadline;
- chỉ nhớ prediction đúng;
- đổi resolution rule sau outcome;
- extrapolate trend tuyến tính quá xa;
- bỏ structural break;
- nhầm “có thể xảy ra” với “có khả năng cao”.

## 9. Forecast journal

```text
Date
Question
Resolution rule
Base rate
Key drivers
Probability / range
Main uncertainty
What would move the estimate
Resolution date
Outcome
Postmortem
```

## Connections

- [Probability](../probability/README.md): uncertainty và conditional probability.
- [Statistics for Life](../statistics-for-life/README.md): noise, sampling và estimates.
- [Expected Value](../expected-value/README.md): biến forecast thành decision consequence.
- [Risk](../risk/README.md): tails và scenario planning.
- [Decision Making](../decision-making/README.md): action dưới uncertainty.
- [Investing](../../investing/README.md): assumptions về company, macro và valuation.
- [PMP](../../pmp/README.md): schedule, cost và project risk.
