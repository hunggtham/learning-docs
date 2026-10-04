# Thinking Practice — Luyện phối hợp công cụ suy nghĩ

`practice/` không thêm theory mới. Đây là nơi biến các chapter trong [`thinking/`](../README.md) thành bài luyện có thể lặp lại để cải thiện calibration, estimation, evidence mapping, adversarial review, sensitivity, scenario reasoning và chất lượng quyết định.

Khác với [`90_connections/`](../90_connections/README.md), nơi bắt đầu từ **một domain/case thực tế**, `practice/` bắt đầu từ **một kỹ năng reasoning** và đưa cùng kỹ năng qua nhiều bối cảnh. Mỗi drill phải tạo ra output có thể lưu, so sánh và review; nếu chỉ đọc rồi “cảm thấy hiểu hơn”, nó chưa tạo được feedback loop.

## Practice route

Bảy drill hiện tại có thể đọc theo ba lớp: làm judgment inspectable, challenge judgment đó, rồi kiểm tra decision dưới uncertainty qua thời gian.

1. [Calibration & Bayesian Updating](./01_calibration_and_bayesian_updating.md) — học nói bằng probability/range, update belief khi có evidence mới và review calibration.
2. [Estimation & Sanity Checks](./05_estimation_and_sanity_checks.md) — tạo rough independent estimate, kiểm tra unit, denominator, order of magnitude và capacity trước khi tin một con số chính xác.
3. [Argument & Evidence Mapping](./06_argument_and_evidence_mapping.md) — tách observation, inference, assumptions, competing explanations và evidence có thể đổi conclusion.
4. [Red Team, Steelman & Disconfirmation](./07_red_team_steelman_and_disconfirmation.md) — challenge strongest version của claim/model/decision, tìm disconfirming evidence và predefine update threshold.
5. [Sensitivity Analysis & Uncertainty Decomposition](./02_sensitivity_analysis_and_uncertainty_decomposition.md) — tìm assumption nào thật sự quyết định conclusion.
6. [Scenario Planning & Stress Testing](./03_scenario_planning_and_stress_testing.md) — kiểm tra decision khi tương lai khác base case.
7. [Decision Journal & Postmortem](./04_decision_journal_and_postmortem.md) — tách decision quality khỏi luck bằng record trước quyết định và review sau outcome.

Thứ tự trên không phải curriculum bắt buộc. Nếu vấn đề bắt đầu từ một con số khó tin, vào Estimation trước; nếu bắt đầu từ một claim gây tranh cãi, vào Argument Mapping; nếu team đồng thuận quá nhanh với một proposal material, dùng Red Team; nếu đã có decision model nhưng không biết assumption nào đáng research, vào Sensitivity.

## Chu kỳ luyện

Các drill khác nhau nhưng cùng đóng một feedback loop:

```text
make an explicit judgment
→ record evidence / assumptions / units / probabilities
→ create an independent baseline
→ steelman the strongest case
→ search for disconfirming evidence
→ expose sensitive variables and alternative explanations
→ test alternative scenarios
→ act or defer
→ observe outcome / new evidence
→ update
→ review process
```

Không đánh giá một reasoning process chỉ bằng outcome cuối. Một forecast hợp lý có thể sai; một quyết định yếu có thể gặp may; một estimate tốt có thể lệch vì input hiếm; một argument map tốt vẫn có thể chứa factual premise sai; một red-team session tốt có thể không đổi decision nếu proposal thật sự robust. Mục tiêu của practice là tăng **calibration**, **clarity**, **error detection**, **inspectability**, **disconfirmation skill** và khả năng update.

## Chọn drill theo failure mode

| Failure mode | Drill nên dùng trước |
|---|---|
| confidence quá chắc so với evidence | Calibration & Bayesian Updating |
| con số có vẻ chính xác nhưng không biết có hợp lý không | Estimation & Sanity Checks |
| tranh luận trộn observation, assumption và conclusion | Argument & Evidence Mapping |
| preferred conclusion chưa từng bị challenge nghiêm túc | Red Team, Steelman & Disconfirmation |
| không biết biến nào thật sự làm conclusion đổi | Sensitivity Analysis |
| plan chỉ sống được trong base case | Scenario Planning & Stress Testing |
| sau outcome không biết do process hay luck | Decision Journal & Postmortem |

Bảng này là routing aid, không phải taxonomy mới. Một decision material thường cần phối hợp nhiều drill thay vì chọn đúng một file.

## Practice depth theo stakes

Không phải mọi việc đều cần full workflow. Một rule thực dụng:

```text
stakes thấp + reversible + feedback nhanh
→ lightweight estimate / quick map / small experiment

stakes cao + uncertainty lớn + khó đảo ngược
→ evidence map
→ red team
→ sensitivity
→ stress test
→ decision journal
```

Practice không nên trở thành bureaucracy. Artifact chỉ đáng giữ khi nó cải thiện learning, decision quality hoặc khả năng audit reasoning sau này.

## Handoff

- Formal probability/Bayes/statistics → [Mathematics](../../mathematics/README.md).
- Logic, argument và epistemology → [Philosophy](../../philosophy/README.md).
- Study design/evidence synthesis → [Research Methods](../../research_methods/README.md).
- Cognitive mechanisms/bias → [Psychology](../../psychology/README.md).
- Economic payoff/incentive/game models → [Economics](../../economics/README.md).

Practice drills không thay thế canonical theory. Vai trò của chúng là biến theory thành **repeated behavior có artifact, challenge mechanism và feedback loop**.