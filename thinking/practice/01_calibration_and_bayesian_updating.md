# Calibration & Bayesian Updating — Luyện belief có thể kiểm tra và update

Mục tiêu của bài luyện này không phải học lại định lý Bayes. Formal foundation nằm ở [Mathematics — Conditional Probability & Bayes](../../mathematics/06_probability_statistics/02_conditional_probability_and_bayes.md). Ở đây ta luyện ba năng lực thực tế:

```text
express uncertainty
→ update when evidence arrives
→ check whether confidence matched reality
```

## 1. Từ “chắc / có lẽ / khó” sang probability range

Khi một claim có uncertainty, thử thay câu mơ hồ bằng range:

```text
"gần như chắc" → khoảng 90–99%?
"khả năng cao" → khoảng 65–85%?
"50/50" → thật sự không biết, hay chỉ đang né estimate?
```

Không cần giả precision. `65–80%` thường trung thực hơn `73%` nếu evidence yếu.

### Drill A — 10 forecast nhỏ

Chọn 10 sự kiện có thể resolve trong 1–4 tuần:

- task có hoàn thành đúng deadline không;
- một package có đến trước ngày X không;
- bug có nằm ở service A không;
- giá/metric có vượt threshold đã định không;
- một lịch hẹn có bị đổi không.

Ghi:

```text
Forecast
Resolve date
Probability / range
Base rate used?
Main evidence
What would change the estimate?
```

Sau khi resolve, không chỉ đếm đúng/sai. Hỏi: những event bạn gọi 70% có xảy ra khoảng 7/10 về dài hạn không?

## 2. Base rate trước case detail

Một lỗi phổ biến là nhìn ngay vào câu chuyện đặc biệt của case hiện tại. Trước khi đọc detail, hỏi:

```text
reference class là gì?
những case tương tự thường có outcome nào?
```

Ví dụ một project “có vẻ gần xong” không đủ để estimate delivery. Hãy tìm tỷ lệ delay của các project cùng loại, cùng team hoặc cùng stage nếu có.

[Forecasting](../forecasting/README.md) giải thích reference class và base rate ở mức workflow.

## 3. Bayesian update bằng likelihood intuition

Không nhất thiết phải tính exact posterior mỗi lần. Hỏi hai câu:

```text
Nếu hypothesis H đúng, evidence E này có dễ xuất hiện không?
Nếu H sai, E này có vẫn dễ xuất hiện không?
```

Evidence mạnh khi nó **phân biệt** hai thế giới.

Ví dụ log error xuất hiện ở mọi service không giúp phân biệt service nào là root cause. Một trace chỉ xuất hiện khi request đi qua service A có diagnostic value cao hơn.

## 4. Drill B — Update theo từng evidence

Chọn một hypothesis có thể kiểm tra, ví dụ:

```text
H: regression được gây bởi deployment mới.
Prior: 40%.
```

Mỗi khi evidence mới đến, ghi:

| Evidence | Direction | New range | Vì sao? |
|---|---|---|---|
| error bắt đầu ngay sau deploy | tăng H | 60–75% | timing phù hợp |
| rollback không giảm error | giảm H | 25–40% | H dự đoán rollback nên giúp |
| upstream dependency cũng lỗi cùng lúc | giảm thêm | 10–25% | alternative explanation mạnh |

Điểm quan trọng là **update**, không phải bảo vệ estimate ban đầu.

## 5. Evidence không độc lập

Ba bài báo cùng dựa trên một dataset không phải ba evidence độc lập. Ba news site copy cùng một nguồn cũng không làm claim mạnh gấp ba.

Khi update nhiều evidence, hỏi:

```text
chúng có chung source không?
chúng có cùng measurement error không?
chúng có cùng selection process không?
```

Đây là lý do naive multiplication của likelihood có thể tạo overconfidence.

## 6. Calibration review

Mỗi tháng, gom forecast theo bucket:

```text
50–60%
60–70%
70–80%
80–90%
90–100%
```

Nếu các event bạn gọi 90% chỉ xảy ra 65%, bạn đang overconfident hoặc reference class sai. Nếu event 60% xảy ra 90%, bạn có thể đang underconfident hoặc estimate quá bảo thủ.

Sample nhỏ tạo noise, vì vậy đừng rút conclusion mạnh sau vài forecast.

## 7. Brier score — optional, không bắt buộc

Cho binary event, Brier score:

```text
(p - outcome)^2
```

với outcome = `1` nếu xảy ra, `0` nếu không.

Score thấp hơn tốt hơn, nhưng không dùng score một cách máy móc: forecast difficulty và event selection cũng ảnh hưởng comparison. Formal scoring rules thuộc Probability/Statistics.

## 8. Failure modes

### Update quá mạnh theo một datapoint

Một evidence mới không tự động xóa base rate.

### Không update vì sunk belief

Nếu evidence đáng lẽ khiến người khác đổi estimate nhưng không khiến bạn đổi, hãy kiểm tra confirmation bias.

### Probability như confidence performance

Nói `99%` không làm argument mạnh hơn. Probability phải phản ánh evidence, không phải mức quyết đoán trong cách nói.

### Hindsight overwrite

Sau outcome, đừng sửa lại memory rằng “mình đã biết từ đầu”. Decision/forecast journal tồn tại để chống lỗi này.

## 9. Mini-template

```text
Question:
Resolve condition:
Reference class:
Prior / initial range:
Key evidence:
Alternative hypotheses:
Current range:
Evidence that would move me up:
Evidence that would move me down:
Resolve date:
Review:
```

## Connections

- [Probability](../probability/README.md)
- [Forecasting](../forecasting/README.md)
- [Cognitive Bias](../cognitive-bias/README.md)
- [Decision Making](../decision-making/README.md)
- [Research Methods](../../research_methods/README.md)

Calibration không có nghĩa lúc nào cũng đúng. Nó có nghĩa confidence của bạn, xét qua nhiều decision/forecast, dần tương thích hơn với tần suất outcome thực tế.