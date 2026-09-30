# Case — Đọc tin, số liệu và claim trên Internet

Online information tạo một môi trường dễ mắc lỗi: tốc độ cao, headline ngắn, selection mạnh và incentive cạnh tranh attention. Mục tiêu không phải nghi ngờ mọi thứ, mà là biết **claim nào cần kiểm tra sâu hơn và kiểm tra bằng cách nào**.

## Situation

Bạn thấy một headline:

> “X làm tăng Y 50%.”

Tempting shortcut là tin ngay vì con số cụ thể, hoặc bác bỏ ngay vì source không thích.

## Step 1 — Frame claim

Hỏi:

```text
X là gì?
Y là gì?
Population nào?
Time period nào?
50% là relative hay absolute change?
Claim là association, prediction hay causation?
```

Nếu baseline tăng từ 2 lên 3 trên 10.000, relative increase là 50% nhưng absolute increase chỉ 1 trên 10.000.

## Step 2 — Trace source chain

Phân biệt:

```text
social post
→ news article
→ press release
→ study / dataset / official source
```

Mỗi bước có thể làm mất context. Ưu tiên đọc source gần dữ liệu gốc nhất khi stakes đủ lớn.

## Step 3 — Check denominator và selection

Một chart có thể đúng số nhưng gây hiểu sai nếu:

- denominator đổi;
- sample thay đổi;
- chỉ hiển thị subgroup có effect mạnh;
- start/end date được chọn có lợi cho narrative;
- missing data không random.

Handoff sang [Statistics for Life](../statistics-for-life/README.md).

## Step 4 — Causal check

Nếu headline nói “X causes Y”, chạy [Causal Reasoning](../causal-reasoning/README.md):

```text
reverse causality?
confounder?
selection?
comparison group?
intervention?
```

## Step 5 — Incentive check

Không đoán motive của cá nhân. Chỉ hỏi structural incentives:

- media tối ưu attention/subscription?
- company press release tối ưu investor/customer perception?
- influencer tối ưu engagement?
- study publication có selection toward surprising results?

Incentive là hypothesis về pressure, không phải bằng chứng rằng claim sai.

## Step 6 — Confidence, không binary trust

Thay vì “tin / không tin”, dùng mức confidence:

```text
well-supported
plausible but incomplete
uncertain
weak evidence
contradicted by stronger evidence
```

Confidence phải thay đổi khi evidence mới xuất hiện.

## Step 7 — Stop rule

Không phải headline nào cũng đáng 30 phút research.

Research sâu hơn khi:

- claim ảnh hưởng decision material;
- claim gây bất ngờ lớn so với base rate;
- source chain mơ hồ;
- causal language mạnh;
- number có thể bị denominator/selection làm sai nghĩa.

## Toolkit used

[Problem Framing](../problem-framing/README.md) → [Critical Thinking](../critical-thinking/README.md) → [Statistics for Life](../statistics-for-life/README.md) → [Causal Reasoning](../causal-reasoning/README.md) → [Incentives](../incentives/README.md) → [Cognitive Bias](../cognitive-bias/README.md).

## Handoff

- Scientific claim → [Research Methods](../../research_methods/README.md)
- Economic claim → [Economics](../../economics/README.md)
- Historical claim → [World History](../../world_history/README.md)
- Psychology claim → [Psychology](../../psychology/README.md)
- Quantitative claim → [Mathematics](../../mathematics/README.md)