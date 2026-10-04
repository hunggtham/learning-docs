# Red Team, Steelman & Disconfirmation — Tìm cách mình có thể sai trước khi commitment

Critical thinking dễ bị hiểu sai thành “tìm lỗi của người khác”. Nhưng failure mode nguy hiểm hơn thường là **ta kiểm tra rất kỹ conclusion mình không thích và kiểm tra rất nhẹ conclusion mình đã muốn tin**.

Drill này luyện một behavior khác:

```text
state the position fairly
→ steelman the strongest version
→ expose key assumptions
→ design a serious challenge
→ search for disconfirming evidence
→ predefine what would change confidence/action
→ update
```

Mục tiêu không phải thắng debate. Mục tiêu là giảm xác suất commit mạnh vào một claim, model hoặc decision vì confirmation bias, motivated reasoning hay group pressure.

Formal logic/argument theory thuộc [Philosophy](../../philosophy/README.md); evidence quality và study design thuộc [Research Methods](../../research_methods/README.md). Practice này chỉ tạo **reusable adversarial review workflow**.

## 1. Red team chỉ có giá trị sau khi steelman

Nếu ta attack một phiên bản yếu của position, ta chỉ luyện strawman.

Trước khi phản biện, viết:

```text
Position:
Strongest plausible version:
Best evidence supporting it:
Conditions under which it would be reasonable:
```

Một test đơn giản:

> Người tin position này có nói “đúng, đó là lý do mạnh nhất của tôi” không?

Nếu không, chưa nên red-team.

Steelman không có nghĩa đồng ý. Nó là control chất lượng cho object mà ta sắp test.

## 2. Tách claim, model và decision — vì mỗi thứ bị challenge khác nhau

### Claim

Ví dụ:

> “Conversion giảm vì pricing mới.”

Challenge cần evidence/causal alternatives.

### Model

Ví dụ:

> “System capacity chủ yếu bị giới hạn bởi CPU.”

Challenge cần load path, bottleneck shift, measurement và competing model.

### Decision

Ví dụ:

> “Nên rollout full ngay tuần này.”

Challenge cần downside, reversibility, option set, thresholds và cost of delay.

Nếu không xác định object, red team thường bắn vào mọi thứ cùng lúc và tạo nhiều objection nhưng ít information.

## 3. Assumption ledger là target map của red team

Một conclusion thường phụ thuộc vào nhiều assumption:

```text
Conclusion
├── factual assumptions
├── measurement assumptions
├── causal assumptions
├── behavioral assumptions
├── forecast assumptions
├── implementation assumptions
└── value / objective assumptions
```

Ví dụ rollout feature:

```text
users understand UI
backend handles load
support volume stays manageable
metric captures adoption
rollback works
no regulatory constraint
```

Red team tốt không hỏi chung chung “có risk gì?”. Nó hỏi:

> Assumption nào nếu sai sẽ làm conclusion đổi mạnh nhất?

Kết nối với [Sensitivity Analysis](02_sensitivity_analysis_and_uncertainty_decomposition.md).

## 4. Chọn attack surface theo impact × uncertainty

Không phải assumption nào cũng đáng challenge như nhau.

Ưu tiên:

```text
high impact on conclusion
× high uncertainty
× testable before commitment
```

Ví dụ một estimate phụ thay đổi 2% outcome không đáng dành hai ngày research nếu một assumption khác có thể đảo hoàn toàn ranking.

Red team không phải “tìm càng nhiều vấn đề càng tốt”; nó là **allocate skepticism tới nơi có value cao nhất**.

## 5. Tìm disconfirming evidence, không chỉ counterargument

Counterargument là một narrative khác. Disconfirming evidence là observation có khả năng làm confidence giảm nếu xuất hiện.

Ví dụ claim:

> “DB là bottleneck chính.”

Counterargument:

> “Có thể application code chậm.”

Disconfirming evidence tốt hơn:

```text
DB wait time <10% total latency
while application CPU/profile explains >60%
```

Hoặc business claim:

> “Pricing mới làm conversion giảm.”

Disconfirming evidence có thể là:

```text
conversion drop bắt đầu trước pricing change
hoặc control segment không nhận pricing change cũng giảm tương tự
```

Đây là lý do red team phải nối với [Argument & Evidence Mapping](06_argument_and_evidence_mapping.md) và [Causal Reasoning](../causal-reasoning/README.md), không dừng ở debate.

## 6. Falsification test — điều gì nếu xảy ra sẽ chứng minh model hiện tại không đủ?

Không phải mọi theory đều dễ falsify trực tiếp, nhưng practical decision nên có failure condition.

Template:

```text
Current belief/model:

If X is observed,
then current model becomes materially weaker because Y.

If Z is observed,
current model becomes stronger because W.
```

Nếu không nghĩ ra bất kỳ observation nào có thể làm belief yếu đi, có thể ta đang giữ một narrative quá elastic.

## 7. Precommit update rule trước khi xem data

Confirmation bias mạnh nhất khi threshold đổi sau khi outcome xuất hiện.

Ghi trước:

```text
Current confidence: 75%

Evidence A → reduce to ~50%
Evidence B → reduce below 30%
Evidence C → increase above 90%
```

Không cần probability giả chính xác. Ý chính là **định hướng và magnitude update phải được nghĩ trước**, để tránh “evidence nào cũng support tôi theo một cách nào đó”.

Formal calibration handoff sang [Calibration & Bayesian Updating](01_calibration_and_bayesian_updating.md).

## 8. Attack model, không attack identity

Một red team session nên hỏi:

```text
Which assumption can fail?
Which evidence is missing?
Which mechanism is alternative?
Which threshold is too optimistic?
Which dependency is single-point failure?
```

Không hỏi:

```text
Ai ngu?
Ai có lỗi?
Ai không hiểu gì?
```

Identity attack làm defender bảo vệ status thay vì update model. Trong team setting, psychological safety không phải nicety; nó ảnh hưởng information flow.

## 9. Role rotation chống “permanent skeptic”

Nếu cùng một người luôn là red team, group dễ biến skepticism thành role identity.

Một format tốt:

```text
Round 1: Team A steelman proposal
Round 2: Team B red-team
Round 3: swap roles
Round 4: joint update
```

Khi người đề xuất cũng phải steelman alternative và skeptic cũng phải defend proposal, quality của argument thường tăng.

## 10. Drill A — Red-team một claim trên Internet

Chọn một claim có consequence vừa phải, không cần topic quá cảm xúc.

Ghi:

```text
Claim:
Strongest version:
Best supporting evidence:
Key assumptions:
Alternative explanations:
Evidence against:
Evidence currently missing:
Disconfirming observation:
Current confidence:
Update trigger:
```

Sau đó tìm ít nhất một source/evidence mà **nếu đúng sẽ làm bạn giảm confidence**, không chỉ source ủng hộ.

Scoring:

- có steelman trước phản biện: 0/1;
- evidence và inference được tách: 0/1;
- có alternative explanation serious: 0/1;
- có disconfirming evidence cụ thể: 0/1;
- có update trigger: 0/1.

## 11. Drill B — Red-team một engineering plan

Ví dụ:

> “Migrate service X sang architecture Y trong tháng này.”

Không bắt đầu bằng “architecture Y tốt/xấu”. Map:

```text
Objective:
Current constraint:
Proposal:
Assumptions:
- migration time
- compatibility
- performance
- rollback
- observability
- team skill
- operational burden
```

Red-team từng assumption theo:

```text
How could this fail?
How would we detect it early?
Can we test cheaply?
What is blast radius?
What is rollback threshold?
```

Output tốt nhất không phải danh sách fear. Nó là **test plan + stop/rollback criteria**.

## 12. Drill C — Red-team preferred decision

Chọn option bạn hiện thích nhất.

### Step 1 — Viết case for

```text
Why I prefer it:
Evidence:
Expected upside:
```

### Step 2 — Steelman best alternative

```text
Best alternative:
Why a reasonable person chooses it:
Best evidence:
```

### Step 3 — Attack preferred option

```text
Most fragile assumption:
Tail downside:
Hidden opportunity cost:
Cost of being wrong:
```

### Step 4 — Define switch condition

```text
If X, I switch to alternative.
If Y, I delay.
If Z, I proceed.
```

Kết nối với [Decision Making](../decision-making/README.md).

## 13. Drill D — Premortem có cấu trúc

Giả sử plan thất bại sau 6 tháng.

Không brainstorm 30 lý do. Phân loại:

```text
framing
information
model
estimate
incentive / strategic response
execution
external shock
```

Chọn top 3 failure mode theo:

```text
plausibility
× impact
× detectability before damage
```

Sau đó thêm:

```text
early warning signal
mitigation
owner
trigger
```

Premortem trở thành operational artifact thay vì anxiety exercise.

## 14. Red team và security-style adversarial thinking

Một số system có adaptive adversary. Khi đó hỏi:

```text
If someone wanted this control to fail,
what path would they exploit?
```

Nhưng không apply adversarial assumption cho mọi human interaction. Customer, colleague hay partner không mặc định là attacker. Context quyết định threat model.

Generic security theory thuộc Computer Science/Security; practice này chỉ giữ pattern “assume pressure against control and test weakest path”.

## 15. Khi nào không nên red-team sâu

Không phải decision nào cũng cần adversarial review.

Giảm depth khi:

- stakes thấp;
- reversible;
- feedback nhanh;
- failure cheap;
- experiment nhỏ tự cung cấp information.

Tăng depth khi:

- irreversible;
- blast radius lớn;
- group consensus quá nhanh;
- strong financial/reputational incentive;
- evidence ambiguous;
- one-shot decision;
- downside asymmetric.

Reasoning cost cũng là cost.

## 16. Common failure modes

### Strawman

Attack phiên bản yếu thay vì strongest plausible version.

### Contrarianism

Phản đối để thể hiện independent thinking, không nhằm tăng information.

### Infinite skepticism

Đòi certainty không thể đạt và làm mọi action dừng lại.

### Evidence asymmetry

Yêu cầu evidence cực mạnh cho side không thích nhưng chấp nhận anecdote cho side mình thích.

### Motive substitution

Không trả lời argument mà suy đoán motive người nói.

### Moving goalposts

Evidence đến thì đổi threshold để conclusion cũ luôn sống sót.

### Fear list

Liệt kê risk mà không có probability, trigger, test hoặc mitigation.

### Red team theatre

Có meeting “challenge session” nhưng không có quyền làm decision update.

## 17. Reusable red-team artifact

```text
# Red Team Review

Claim / model / decision:
Owner:
Date:

## Steelman
Strongest version:
Best supporting evidence:
Why it is reasonable:

## Assumptions
1.
2.
3.

## Fragility
Most sensitive assumption:
Largest downside:
Hidden dependency:
Alternative explanation / option:

## Disconfirmation
Evidence against:
Missing evidence:
Observation that would materially weaken conclusion:
Cheap test / probe:

## Update rule
Current confidence:
Proceed threshold:
Delay threshold:
Switch / rollback threshold:

## Result
What changed after red team:
Decision/model update:
Remaining uncertainty:
Review date:
```

## 18. Feedback loop

Sau nhiều red-team sessions, review:

```text
Which failure modes were repeatedly found?
Which objections sounded strong but rarely mattered?
Did red team change decisions or only generate text?
Were update thresholds respected?
Were we better at finding false positives or false negatives?
```

Mục tiêu dài hạn không phải trở nên pessimistic. Mục tiêu là **calibrated skepticism**: challenge đủ mạnh ở nơi downside lớn, nhưng vẫn có stopping rule để hành động.

## Connections

- [Argument & Evidence Mapping](06_argument_and_evidence_mapping.md): object hóa claim, evidence và assumptions trước khi challenge.
- [Calibration & Bayesian Updating](01_calibration_and_bayesian_updating.md): update confidence theo evidence.
- [Sensitivity Analysis](02_sensitivity_analysis_and_uncertainty_decomposition.md): chọn assumption đáng attack nhất.
- [Scenario Planning & Stress Testing](03_scenario_planning_and_stress_testing.md): test plan ngoài base case.
- [Decision Journal & Postmortem](04_decision_journal_and_postmortem.md): kiểm tra sau outcome xem red team có bắt đúng failure mode không.
- [Critical Thinking](../critical-thinking/README.md): claim/source reasoning.
- [Causal Reasoning](../causal-reasoning/README.md): competing causal explanations.
- [Decision Making](../decision-making/README.md): biến challenge thành threshold/action.

Điểm chốt: **red team tốt không làm conclusion yếu đi bằng mọi giá; nó làm connection giữa evidence, assumptions và action khó tự lừa mình hơn**.