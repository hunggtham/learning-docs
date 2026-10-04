# Decision Making — Từ uncertainty đến hành động

Ra quyết định (decision making / 의사결정) là nơi các thinking tools gặp nhau. Decision tốt không phải là “chọn đúng tương lai”; nó là chọn action hợp lý nhất **given information, objectives, constraints và uncertainty tại thời điểm quyết định**, đồng thời giữ cơ chế update khi evidence thay đổi.

Canonical psychology nằm ở [Thinking, Language & Decision](../../psychology/02_learning_and_cognition/02_thinking_language_and_decision.md) và [Decision under Risk](../../psychology/02_learning_and_cognition/08_decision_under_risk_uncertainty_and_ambiguity.md). Probability/optimization formal thuộc Mathematics, incentives/game theory thuộc Economics. Trang này chỉ giữ process tích hợp để biến những theory đó thành action có thể review.

Mental model cốt lõi:

```text
frame decision
→ define objective + constraints
→ generate realistic options
→ identify uncertainty
→ estimate payoff + downside
→ test robustness / reversibility
→ decide whether more information is worth delay
→ choose action + threshold
→ define update / review rule
→ learn from process, not only outcome
```

## 1. Decision quality không đồng nghĩa outcome quality

Một decision process tốt vẫn có thể cho outcome xấu vì uncertainty; decision process yếu vẫn có thể gặp may. Nếu chỉ học từ outcome, ta dễ reinforce behavior tệ sau một kết quả may mắn hoặc bỏ một process tốt chỉ vì tail event xảy ra.

Vì vậy khi review, luôn tách:

```text
Was the outcome good?
Was the process reasonable given what was knowable then?
```

Đây là reason quan trọng để dùng [Decision Journal & Postmortem](../practice/04_decision_journal_and_postmortem.md): lưu snapshot của reasoning trước khi biết kết quả.

## 2. Trước khi so options, phải định nghĩa decision thật sự

Một decision frame tối thiểu:

```text
Decision:
tôi phải chọn gì?

Objective:
outcome nào thật sự quan trọng?

Constraints:
tiền, thời gian, luật, skill, energy, capacity?

Options:
những lựa chọn realistic nào tồn tại?

Uncertainty:
điều gì chưa biết nhưng có thể đổi ranking?

Deadline:
khi nào phải chọn?

Reversibility:
có thể quay lại hoặc đổi course với cost nào?

Time horizon:
đang tối ưu tuần này, 1 năm hay 10 năm?
```

Nếu frame chưa rõ, scoring chi tiết phía sau chỉ tạo false precision. Khi cần chỉnh lại objective/scope, quay về [Problem Framing](../problem-framing/README.md).

## 3. Option set phải chứa status quo và các alternative thực sự

Một lỗi phổ biến là tạo một option mình thích và vài strawman option để nó thắng.

Nếu phù hợp, option set nên kiểm tra:

```text
do nothing / status quo
wait / gather information
small reversible trial
full commitment
hybrid / staged approach
best realistic alternative
```

“Không làm gì” không phải lúc nào cũng miễn phí: delay có cost, risk có thể tiếp tục tích lũy. Nhưng bỏ status quo khỏi option set cũng che đi opportunity cost của action.

Một decision chỉ có A/B đôi khi thực ra có thêm:

```text
A now
B now
A after pilot
B after information
partial A
reversible experiment
```

Mở option space không có nghĩa brainstorming vô hạn; chỉ cần đủ để tránh false dilemma và expose option value.

## 4. Objective nên tách outcome bắt buộc khỏi preference

Không phải mọi criterion có cùng vai trò.

```text
Hard constraint:
không được vượt budget / legal limit / safety threshold

Primary objective:
điều cần maximize/minimize

Secondary preference:
điều tốt nếu có nhưng có thể trade off
```

Nếu mọi criterion đều được cho weight rồi cộng vào một score, hard constraint có thể bị “bù” bởi điểm tốt ở tiêu chí khác dù thực tế không thể chấp nhận.

Decision matrix hữu ích khi nó expose trade-off, không phải khi nó biến judgment thành decimal giả chính xác.

## 5. Reversible và irreversible decisions cần tốc độ khác nhau

Decision dễ đảo ngược thường nên ưu tiên **speed + learning**. Decision khó đảo ngược cần thêm evidence, margin of safety và stress test.

Ví dụ:

```text
reversible:
đổi editor
chạy experiment nhỏ
pilot feature

less reversible:
ký khoản vay dài hạn
migrate irreversible data path
bán strategic asset
chọn surgery
```

Reversibility không phải binary. Hỏi:

```text
Cost to reverse?
Time to reverse?
Damage accumulated before reversal?
Can we detect failure early enough?
```

Một action technically reversible nhưng feedback chậm có thể thực tế rất khó đảo ngược.

## 6. Option value — flexibility có thể đáng tiền khi uncertainty cao

Một option có giá trị không chỉ vì immediate payoff mà còn vì nó giữ mở future choices.

Ví dụ:

```text
pilot before full rollout
short contract before long lock-in
modular architecture before irreversible coupling
small position before concentrated exposure
```

Pilot có thể “kém tối ưu” theo short-term efficiency nhưng mua information và giữ quyền dừng. Đây là nơi [Value of Information](../value-of-information/README.md), [Risk](../risk/README.md) và Expected Value gặp nhau.

Option value đặc biệt lớn khi:

- uncertainty cao;
- decision khó đảo ngược;
- information sẽ đến sớm;
- cost giữ flexibility thấp hơn downside của commitment sai.

## 7. Sequential decision — nhiều decision không cần giải toàn bộ ngay hôm nay

Thực tế nhiều quyết định là chuỗi:

```text
choose first action
→ observe signal
→ update belief
→ choose next action
```

Nếu tương lai cho phép update, không nên model decision như một one-shot static choice.

Ví dụ project rollout:

```text
internal pilot
→ 5% traffic
→ measure error/adoption
→ 25%
→ full rollout
```

Mỗi stage cần:

```text
entry condition
success metric
failure threshold
rollback option
next decision point
```

Sequential design biến uncertainty thành learning path và giảm blast radius.

## 8. Threshold thinking — khi nào action A trở thành hợp lý?

Nhiều decision dễ hơn nếu hỏi threshold thay vì cố tìm “con số đúng tuyệt đối”.

Ví dụ:

```text
Nếu probability failure > X, rollback.
Nếu expected demand < Y, không mở capacity.
Nếu cost estimate > Z, chọn alternative.
```

Threshold phải dựa trên payoff/downside, không phải number đẹp.

Một conceptual rule:

```text
act when expected benefit of action
exceeds cost + downside + opportunity cost
by enough margin for uncertainty
```

Không phải lúc nào cũng tính được chính xác; threshold vẫn hữu ích vì nó nói **evidence nào có thể đổi action**.

## 9. Stopping rule — khi nào ngừng research và quyết định?

Research vô hạn cũng có cost. Một stopping rule tốt hỏi:

```text
Information tiếp theo có khả năng đổi decision không?
Cost/time để lấy information là bao nhiêu?
Delay itself có downside gì?
Decision có reversible không?
```

Nếu evidence mới khó đổi action hoặc cost delay lớn, research thêm có value thấp. Nếu decision irreversible và uncertainty trọng yếu có thể giảm rẻ, research thêm có value cao.

Đây là ứng dụng trực tiếp của [Value of Information](../value-of-information/README.md).

## 10. Cost of delay phải được đưa vào option set

“Chờ thêm” nghe an toàn nhưng không miễn phí.

Delay có thể tạo:

- missed opportunity;
- continued losses;
- schedule slip;
- customer churn;
- compounding risk;
- loss of option window.

Ngược lại action sớm có thể tạo irreversible mistake. Vì vậy comparison đúng là:

```text
cost of acting too early
vs
cost of acting too late
```

Không phải “action có risk còn waiting thì không”.

## 11. Expected Value hữu ích nhưng chưa đủ

Expected Value giúp combine probability và payoff, nhưng EV positive không tự động nghĩa “nên làm”.

Cần hỏi thêm:

```text
Can we survive the downside?
Is utility linear with money/time/outcome?
Is risk correlated with existing exposure?
Is the decision repeated or one-shot?
Is downside irreversible?
```

Một decision có EV tốt nhưng small probability of ruin có thể không acceptable. Handoff sang [Expected Value](../expected-value/README.md) và [Risk](../risk/README.md).

## 12. Robust decision khác optimal decision

“Optimal” thường phụ thuộc mạnh vào model/assumptions. Khi model uncertainty lớn, robust option có thể tốt hơn: không đứng nhất trong base case nhưng vẫn acceptable ở nhiều plausible worlds.

Ví dụ:

```text
Option A:
+20 best case
-30 adverse case

Option B:
+14 best case
+6 adverse case
```

Nếu uncertainty về model cao và downside của A lớn, B có thể là lựa chọn robust hơn dù expected central estimate thấp hơn.

Stress test bằng [Scenario Planning & Stress Testing](../practice/03_scenario_planning_and_stress_testing.md), rồi dùng [Sensitivity Analysis](../practice/02_sensitivity_analysis_and_uncertainty_decomposition.md) để xem ranking phụ thuộc assumption nào.

## 13. Margin of safety — đừng commit sát boundary khi estimate rất noisy

Nếu threshold là 100 và estimate là 101 ± 30, nói “đã vượt threshold” là false precision.

Margin of safety có thể đến từ:

- extra budget/capacity;
- conservative assumption;
- lower leverage;
- rollback buffer;
- schedule contingency;
- redundant path.

Margin không miễn phí. Nó là cost mua resilience trước estimation error và tail event.

## 14. Incentives và strategic response có thể làm payoff đổi sau decision

Nếu decision ảnh hưởng người khác, actor có thể adapt.

Ví dụ:

```text
new KPI
→ employee behavior adapts

new pricing rule
→ customer/supplier response

new security control
→ attacker changes tactic
```

Không thể giữ payoff table cố định nếu rule change thay incentives. Handoff sang [Incentives](../incentives/README.md), [Game Theory](../game-theory/README.md) và [Systems Thinking](../systems-thinking/README.md).

## 15. Premortem dùng để tìm failure mode trước commitment

Giả sử decision đã thất bại sau 6–12 tháng. Hỏi:

> Những nguyên nhân hợp lý nhất là gì?

Sau đó phân loại:

```text
framing failure
information failure
model failure
execution failure
incentive response
external shock
```

Premortem không phải bi quan vô hạn. Chỉ giữ failure modes có plausibility và actionable mitigation.

Nếu muốn đi sâu hơn vào phản biện có cấu trúc, dùng [Red Team, Steelman & Disconfirmation](../practice/07_red_team_steelman_and_disconfirmation.md).

## 16. Decision matrix — dùng để expose trade-off, không outsource judgment

Một matrix có thể hữu ích:

| Criterion | Weight | A | B | C |
|---|---:|---:|---:|---:|
| Cost |  |  |  |  |
| Reliability |  |  |  |  |
| Flexibility |  |  |  |  |
| Time |  |  |  |  |

Nhưng weight và score là judgment. Hãy test:

```text
Nếu weight thay 20%, ranking có đổi không?
Có hard constraint nào đang bị average hóa?
Criteria có double-count cùng một thing không?
```

Nếu ranking rất nhạy, conclusion phải thể hiện uncertainty thay vì “A = 8.37 nên thắng”.

## 17. Decision journal phải ghi prediction và update trigger

Trước decision material, ghi:

```text
Date
Decision
Objective
Options
Key evidence
Key assumptions
Probability/ranges
Expected upside/downside
Main risks
Reversibility
Opportunity cost
What would change my mind
Review date
```

Sau outcome, không rewrite phần “Before”. Review process bằng [Decision Journal & Postmortem](../practice/04_decision_journal_and_postmortem.md).

## 18. Reusable decision worksheet

```text
# Decision

Decision:
Deadline:
Time horizon:

Objective:
Hard constraints:
Secondary preferences:

Options:
A.
B.
C.
Status quo / wait:

Base rates / evidence:
Key uncertainties:
Sensitive assumptions:

Expected upside/downside:
Ruin / irreversible downside:
Reversibility:
Option value:

Strategic / incentive response:
Second-order effects:

Information worth gathering:
Cost of delay:
Stopping rule:

Threshold / trigger:
Chosen action:
Why this option is robust enough:

Update trigger:
Review date:
```

Không cần điền full template cho low-stakes choice. Depth nên tỷ lệ với **stakes × uncertainty × irreversibility**.

## 19. Common failure modes

### Outcome bias

Kết quả xấu không chứng minh process tệ; kết quả tốt không chứng minh process tốt.

### False dilemma

Bỏ status quo, staged option hoặc pilot khỏi option set.

### Analysis paralysis

Research thêm dù information mới khó đổi action.

### Premature optimization

Chọn “best” theo model chưa được stress-test.

### Ignoring cost of delay

Tưởng waiting là neutral option.

### Risk blindness

Nhìn EV mà bỏ ruin, correlation và irreversibility.

### Precision theater

Matrix/forecast cho decimal rất đẹp trong khi inputs chỉ là rough judgment.

### Commitment escalation

Tiếp tục vì sunk cost thay vì update theo forward-looking payoff.

## 20. Unified workflow

Với decision material, route thực dụng là:

```text
Problem Frame
→ realistic options + status quo
→ opportunity cost
→ base rate / evidence
→ estimate + sanity check
→ probability / forecast
→ expected value
→ downside / ruin / irreversibility
→ sensitivity + stress test
→ incentives / system response
→ value of additional information
→ stopping rule
→ choose action + threshold
→ define update/review rule
→ journal / postmortem
```

Không phải decision nào cũng cần toàn bộ route. Nhưng nếu một step bị bỏ, nên biết vì sao nó không material chứ không phải quên nó tồn tại.

## Connections

- [Problem Framing](../problem-framing/README.md): xác định decision trước khi optimize.
- [Probability](../probability/README.md): uncertainty.
- [Forecasting](../forecasting/README.md): future states và calibration.
- [Expected Value](../expected-value/README.md): probability-weighted payoff.
- [Risk](../risk/README.md): downside, tails, correlation và survivability.
- [Opportunity Cost](../opportunity-cost/README.md): best forgone alternative.
- [Value of Information](../value-of-information/README.md): research vs act.
- [Sensitivity Analysis](../practice/02_sensitivity_analysis_and_uncertainty_decomposition.md): assumption nào làm ranking đổi.
- [Scenario Planning & Stress Testing](../practice/03_scenario_planning_and_stress_testing.md): robustness ngoài base case.
- [Decision Journal & Postmortem](../practice/04_decision_journal_and_postmortem.md): feedback loop.
- [Red Team, Steelman & Disconfirmation](../practice/07_red_team_steelman_and_disconfirmation.md): challenge preferred option trước commitment.
- [Incentives](../incentives/README.md) + [Game Theory](../game-theory/README.md): decisions involving adaptive actors.
- [PMP](../../pmp/README.md): project decision, risk và governance.
- [Investing](../../investing/README.md): capital allocation under uncertainty.

Điểm chốt của Decision Making không phải “tính đủ mọi thứ”. Nó là **chọn mức reasoning phù hợp, giữ option set và uncertainty explicit, rồi biến decision thành một process có threshold, update trigger và review loop**.