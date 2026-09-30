# Case — Business, metrics, incentives và organizations

Business decisions thường tạo feedback: khi metric, bonus hoặc process đổi, con người thích nghi. Vì vậy không thể chỉ nhìn direct effect của policy rồi giả định behavior đứng yên.

## Situation

Một organization muốn tăng performance bằng cách thưởng theo một KPI duy nhất.

Ví dụ:

```text
sales volume
tickets closed
lines of code
calls handled
orders shipped
```

## Step 1 — Frame true outcome

KPI là proxy. Outcome có thể là:

```text
profitable revenue
customer problem solved
software value delivered
service quality
reliable fulfillment
```

Nếu proxy chỉ capture một phần outcome, optimization mạnh có thể làm phần còn lại xấu đi.

Handoff: [Problem Framing](../problem-framing/README.md).

## Step 2 — Map incentive

Viết payoff thay đổi thế nào:

```text
rule / KPI
→ reward or penalty
→ behavior at margin
→ metric movement
→ real outcome
→ side effects
```

Không giả định “mọi người sẽ gian lận”. Chỉ xác định behavior nào trở nên rẻ hơn hoặc có lợi hơn dưới rule mới.

## Step 3 — Gaming và Goodhart-style failure

Khi measure trở thành target, relationship giữa measure và underlying outcome có thể suy yếu.

Ví dụ ticket close rate tăng có thể đi cùng reopen rate tăng nếu closure được thưởng nhưng resolution quality không được đo.

Đây là systems/incentive failure, không chỉ moral failure của cá nhân.

## Step 4 — Second-order effects

Một bonus có thể:

```text
increase output
→ increase workload downstream
→ increase defects
→ increase rework
→ reduce net throughput
```

Local optimization có thể làm system outcome xấu đi.

Handoff: [Systems Thinking](../systems-thinking/README.md).

## Step 5 — Strategic response

Nếu nhiều teams hoặc firms tương tác, rule change có thể làm mỗi actor đổi strategy.

Ví dụ pricing, queue priority, performance ranking hoặc procurement rule có thể tạo strategic adaptation.

Handoff: [Game Theory](../game-theory/README.md).

## Step 6 — Measurement design

Một metric system tốt thường cần balance:

```text
quantity
quality
speed
cost
risk
long-term outcome
```

Không phải lúc nào cũng cần dashboard lớn. Mục tiêu là tránh một proxy đơn lẻ bị optimize đến mức phá outcome.

## Step 7 — Pilot và value of information

Nếu policy có uncertainty lớn:

```text
small pilot
→ observe adaptation
→ detect side effects
→ revise metric / guardrail
→ scale
```

Pilot tốt cần comparison phù hợp; nếu không, seasonal change hoặc selection có thể bị nhầm thành policy effect.

## Step 8 — Distribution

Average improvement có thể che nhóm chịu downside.

Hỏi:

- ai nhận benefit?
- ai chịu cost?
- có bottleneck chuyển sang team khác không?
- risk có bị đẩy sang vendor/customer/frontline worker không?

## Toolkit used

[Problem Framing](../problem-framing/README.md) → [Incentives](../incentives/README.md) → [Systems Thinking](../systems-thinking/README.md) → [Game Theory](../game-theory/README.md) → [Causal Reasoning](../causal-reasoning/README.md) → [Value of Information](../value-of-information/README.md).

## Handoff

- Incentives, firms, contracts, market structure → [Economics](../../economics/README.md)
- Human behavior, motivation, group dynamics → [Psychology](../../psychology/README.md)
- Organizations, institutions, hierarchy → [Sociology](../../sociology/README.md)
- Korean company/economy cases → [Korea Business & Economy](../../korea_business_economy_knowledge_library/README.md)
- Project governance → [PMP](../../pmp/README.md)