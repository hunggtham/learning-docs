# Decision Journal & Postmortem — Học từ process thay vì chỉ nhìn outcome

Nếu không ghi reasoning trước decision, sau outcome bộ nhớ rất dễ rewrite câu chuyện: ta nhớ mình “đã biết”, quên uncertainty ban đầu, hoặc đánh giá process dựa trên may/rủi.

Decision journal tạo một snapshot **trước khi biết kết quả**. Postmortem dùng snapshot đó để review.

## 1. Decision journal dùng cho việc gì?

Không cần ghi mọi quyết định nhỏ. Dùng khi decision có ít nhất một trong các đặc điểm:

```text
high consequence
high uncertainty
hard to reverse
repeated decision worth learning from
many assumptions / stakeholders
```

Ví dụ: chọn project, mua asset lớn, rollout production change, thay architecture, đổi công việc, ký contract dài hạn hoặc chọn strategy học dài hạn.

## 2. Minimum viable journal

```text
Date:
Decision:
Deadline:
Objective:
Options considered:
Constraints:
Information available now:
Key assumptions:
Probability / ranges:
Expected upside:
Expected downside:
Main risks:
Reversibility:
Opportunity cost:
What would change my mind:
Review date:
```

Nếu mất quá lâu, journal sẽ không được dùng. Với decision vừa phải, 5–10 phút là đủ.

## 3. Ghi alternatives thật sự

Không ghi:

```text
Option A: plan tôi thích
Option B: plan vô lý
```

Hãy ghi best realistic alternatives. Nếu không, opportunity cost bị bóp méo ngay từ đầu.

Xem [Opportunity Cost](../opportunity-cost/README.md).

## 4. Record assumptions, không chỉ conclusion

Một conclusion có thể sai vì:

- input sai;
- causal model sai;
- probability sai;
- actor phản ứng khác dự kiến;
- execution fail;
- shock ngoài model.

Nếu chỉ ghi “tôi chọn A”, postmortem không biết lỗi ở layer nào.

## 5. Prediction ledger

Tách các prediction có thể resolve:

| Prediction | Probability/range | Resolve date |
|---|---:|---|
| migration hoàn thành trong 3 tuần | 70% | 20 Oct |
| error rate giảm ≥30% | 60–75% | 30 Oct |
| adoption ≥50% sau 1 tháng | 55% | 15 Nov |

Ledger giúp review calibration thay vì narrative.

## 6. Decision review ≠ result review

Khi outcome đến, tách hai câu hỏi:

```text
Outcome tốt hay xấu?
Decision process tốt hay xấu given information available then?
```

Bốn trường hợp đều có thể xảy ra:

| Process | Outcome | Interpretation |
|---|---|---|
| tốt | tốt | expected success hoặc good luck |
| tốt | xấu | uncertainty/tail risk có thể xảy ra |
| yếu | tốt | may mắn; không nên reinforcement mù quáng |
| yếu | xấu | cần tìm process failure |

## 7. Postmortem taxonomy

Khi decision không đạt mục tiêu, phân loại trước khi sửa:

### Framing error

Đã giải sai question/objective.

### Information error

Critical data thiếu hoặc chất lượng thấp.

### Model error

Mechanism/model không phù hợp.

### Estimation error

Range/probability quá optimistic hoặc pessimistic.

### Incentive / strategic error

Actor phản ứng khác prediction.

### Execution error

Plan hợp lý nhưng implementation fail.

### External shock

Một event khó dự kiến thay đổi system.

Một failure có thể thuộc nhiều loại.

## 8. Counterfactual review

Hỏi:

```text
Nếu quay lại thời điểm decision với đúng information khi đó,
tôi có chọn khác không?
```

Sau đó hỏi tiếp:

```text
Information nào tôi có thể hợp lý thu thập thêm lúc đó?
```

Câu thứ hai kết nối với [Value of Information](../value-of-information/README.md).

## 9. Avoid hindsight leakage

Khi review, đọc journal gốc **trước** khi viết explanation mới. Không sửa journal cũ; thêm review bên dưới hoặc file mới.

Nếu journal được chỉnh sau outcome, provenance mất giá trị.

## 10. Drill A — Một decision đang mở

Chọn một decision chưa resolve và viết journal hôm nay.

Sau đó đặt review date. Khi review:

1. score prediction;
2. xác định assumption đúng/sai;
3. phân loại process error nếu có;
4. viết 1–3 rule update cụ thể.

Không viết 20 “bài học”. Một rule có thể hành động tốt hơn một narrative dài.

## 11. Drill B — Reconstruct một decision cũ

Nếu không có journal cũ, thử reconstruct từ email, issue, commit, calendar hoặc note có timestamp.

Tách:

```text
what was knowable then
vs
what is known now
```

Bài luyện này cho thấy hindsight bias mạnh đến mức nào.

## 12. Team postmortem

Với engineering/project team, giữ postmortem blameless ở level cá nhân nhưng precise ở level system:

```text
What happened?
What signals existed?
Why did the system/process allow it?
Which assumptions failed?
Which controls/feedback loops were missing?
What changes reduce recurrence?
```

“Human error” thường là điểm bắt đầu điều tra, không phải root cause cuối cùng.

Xem [Engineering Incidents & Debugging](../90_connections/02_engineering_incidents_and_debugging.md).

## 13. Failure modes

### Journal như bureaucracy

Nếu template quá dài, giảm xuống minimum viable fields.

### Outcome bias

Outcome xấu không chứng minh decision tệ.

### Self-justification

Postmortem không phải nơi chứng minh “tôi vẫn đúng”. Mục tiêu là update model/process.

### Lesson quá chung

“Cẩn thận hơn” không phải action. Tốt hơn:

```text
Trước production migration >2h, luôn chạy rollback drill trên staging.
```

## 14. Reusable template

```text
# Decision — YYYY-MM-DD

## Before
Decision:
Objective:
Options:
Constraints:
Assumptions:
Evidence:
Probabilities / ranges:
Expected value / trade-offs:
Risks / ruin conditions:
Reversibility / option value:
Information worth gathering:
Decision:
Update trigger:
Review date:

## After — do not rewrite Before
Outcome:
Predictions resolved:
What was luck?
What was process quality?
Framing / information / model / estimation / incentive / execution errors:
What changed my model?
1–3 process rules to carry forward:
```

## Connections

- [Decision Making](../decision-making/README.md)
- [Cognitive Bias](../cognitive-bias/README.md)
- [Forecasting](../forecasting/README.md)
- [Value of Information](../value-of-information/README.md)
- [Risk](../risk/README.md)

Decision journal không đảm bảo decision đúng. Nó tạo **feedback loop** để reasoning có thể cải thiện qua thời gian.