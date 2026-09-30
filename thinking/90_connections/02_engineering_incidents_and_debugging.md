# Case — Engineering incident, debugging và system reliability

Engineering incident là môi trường tốt để luyện thinking tools vì observation, causality, feedback loop, risk và action đều xuất hiện cùng lúc.

## Situation

Sau một deployment, latency tăng và error rate tăng.

Tempting shortcut:

> “Deploy vừa xong nên deploy chắc chắn là nguyên nhân.”

Đó là hypothesis hợp lý, chưa phải conclusion.

## Step 1 — Define symptom và scope

```text
Which service?
Which endpoint?
Which region?
Which users?
When did it start?
Which metric moved first?
```

Một aggregate metric có thể che local failure.

Handoff: [Problem Framing](../problem-framing/README.md).

## Step 2 — Build timeline

Đặt các event theo thời gian:

```text
deploy
config change
traffic change
dependency incident
queue growth
CPU / memory change
error spike
```

Temporal order giúp loại causal story không thể xảy ra, nhưng “A xảy ra trước B” vẫn chưa đủ chứng minh A gây B.

## Step 3 — Generate competing hypotheses

Ví dụ:

```text
H1: application regression
H2: database contention
H3: downstream dependency
H4: traffic mix changed
H5: configuration mismatch
```

Không chỉ kiểm tra hypothesis đầu tiên phù hợp với intuition.

## Step 4 — Choose discriminating evidence

Tìm test có thể phân biệt hypotheses:

- rollback có làm metric recover?
- canary cũ/mới khác nhau không?
- dependency error có precede app error không?
- query latency có tăng cùng window không?

Đây là [Value of Information](../value-of-information/README.md) trong debugging.

## Step 5 — Causal intervention

Rollback, traffic shift hoặc feature flag có thể hoạt động như intervention nếu operational risk cho phép.

Không phải incident nào cũng nên experiment trực tiếp; safety và blast radius ưu tiên trước learning.

Handoff: [Causal Reasoning](../causal-reasoning/README.md).

## Step 6 — System dynamics

Một lỗi nhỏ có thể amplify:

```text
latency
→ retries
→ more load
→ more latency
```

Đây là reinforcing feedback loop. Fix local symptom nhưng không phá loop có thể khiến incident quay lại.

Handoff: [Systems Thinking](../systems-thinking/README.md).

## Step 7 — Risk decision

Trong incident, decision thường là:

```text
rollback now
vs
continue diagnosis
vs
partial mitigation
```

Cân nhắc:

- current user harm;
- rollback risk;
- reversibility;
- uncertainty;
- blast radius;
- time to learn.

## Step 8 — Postmortem without hindsight

Postmortem nên tách:

```text
trigger
contributing factors
amplifiers
missing detection
response constraints
recovery mechanism
preventive controls
```

Không quy toàn bộ lỗi cho một cá nhân nếu system design, incentive hoặc control structure góp phần tạo failure.

## Toolkit used

[Problem Framing](../problem-framing/README.md) → [Causal Reasoning](../causal-reasoning/README.md) → [Value of Information](../value-of-information/README.md) → [Systems Thinking](../systems-thinking/README.md) → [Risk](../risk/README.md) → [Decision Making](../decision-making/README.md).

## Handoff

- Runtime, architecture, algorithms → [Computer Science](../../computer_science/README.md)
- Backend behavior → [Backend](../../10_backend/README.md)
- Delivery, observability, SRE → [DevOps / Platform Engineering](../../devops_platform_engineering/README.md)
- Data pipeline incidents → [Data Engineering](../../data_engineering/README.md)