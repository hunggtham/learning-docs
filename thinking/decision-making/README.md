# Decision Making — Từ uncertainty đến hành động

Ra quyết định (decision making / 의사결정) là nơi các thinking tools gặp nhau. Canonical psychology nằm ở [Thinking, Language & Decision](../../psychology/02_learning_and_cognition/02_thinking_language_and_decision.md) và [Decision under Risk](../../psychology/02_learning_and_cognition/08_decision_under_risk_uncertainty_and_ambiguity.md). Trang này cung cấp process có thể tái sử dụng.

## 1. Decision quality ≠ outcome quality

Một quyết định có process tốt vẫn có thể cho outcome xấu vì uncertainty; quyết định tệ vẫn có thể gặp may. Nếu chỉ học từ outcome, ta dễ rơi vào hindsight/outcome bias.

Đánh giá decision bằng information có sẵn **tại thời điểm quyết định**.

## 2. Decision frame

Viết rõ:

```text
Decision: tôi phải chọn gì?
Objective: outcome nào thực sự quan trọng?
Constraints: tiền, thời gian, law, skill, energy?
Options: ít nhất 3 nếu có thể?
Uncertainty: điều gì chưa biết?
Deadline: khi nào cần quyết định?
Reversibility: có thể quay lại không?
```

Nếu frame sai, phân tích chi tiết phía sau cũng sai hướng.

## 3. Reversible vs irreversible

Decision dễ đảo ngược nên ưu tiên tốc độ và learning. Decision khó đảo ngược cần nhiều evidence, margin of safety và premortem hơn.

Ví dụ đổi editor tool có thể reversible; ký khoản vay dài hạn, surgery hoặc bán một strategic asset có mức irreversibility cao hơn.

## 4. Option value

Một option có giá trị không chỉ vì payoff trực tiếp mà còn vì nó giữ mở future choices. Khi uncertainty cao, flexibility có thể đáng giá.

Ví dụ pilot nhỏ trước full rollout mua information và giữ quyền dừng; đây là cách kết hợp decision making với [Risk](../risk/README.md) và [Expected Value](../expected-value/README.md).

## 5. Premortem

Giả sử quyết định đã thất bại sau 12 tháng. Hỏi “những nguyên nhân hợp lý nhất là gì?”. Premortem giúp tìm failure modes mà optimism hoặc commitment hiện tại dễ bỏ qua.

Không dùng premortem để bi quan vô hạn; mục tiêu là tìm risk có thể mitigate.

## 6. Decision matrix — dùng khi tiêu chí thật sự khác nhau

Có thể chấm options theo criteria, nhưng score không nên tạo precision giả. Weight là judgment. Hãy dùng matrix để expose trade-offs, không để che chúng.

## 7. Decision journal

Trước quyết định quan trọng, ghi:

```text
Date
Decision
Options considered
Key assumptions
Probability ranges
Expected upside/downside
Main risks
What would change my mind
Review date
```

Sau outcome, review process thay vì tự kể một narrative mới.

## 8. Unified workflow

```text
Frame
→ generate options
→ opportunity cost
→ probability/base rate
→ expected value
→ risk/ruin/irreversibility
→ incentives/strategic response
→ second-order effects
→ bias check
→ choose
→ define update/review rule
```

## 9. Sequential decisions và stopping rule

Nhiều decision không phải một lần chọn A/B mà là chuỗi hành động có thể quan sát và điều chỉnh. Viết `next action → signal → update → continue/stop/switch`, rồi đặt điều kiện dừng trước khi sunk cost hoặc identity kéo decision đi tiếp. Pilot và staged commitment thường mua option value, nhưng chỉ hữu ích khi trigger và quyền dừng thật sự tồn tại.

## 10. Robust decision trước tối ưu hóa

Khi probability/model không đáng tin, chọn action giữ outcome đủ tốt qua nhiều plausible worlds thay vì action tối ưu trong một base case mỏng. So sánh rõ `expected value`, `worst acceptable state`, `ruin condition`, `reversibility` và `cost of delay`; robust không đồng nghĩa luôn conservative, mà là phù hợp với stakes và model uncertainty.

## Connections

- [Probability](../probability/README.md): uncertainty.
- [Expected Value](../expected-value/README.md): probability-weighted payoff.
- [Risk](../risk/README.md): downside, tails và survivability.
- [Opportunity Cost](../opportunity-cost/README.md): best forgone alternative.
- [Incentives](../incentives/README.md) + [Game Theory](../game-theory/README.md): decisions involving other actors.
- [PMP](../../pmp/README.md): project decisions, risk and governance.
- [Investing](../../investing/README.md): capital allocation under uncertainty.
