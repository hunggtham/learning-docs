# Thinking Toolkit — Công cụ suy nghĩ dùng xuyên toàn bộ Learning Docs

`thinking/` không phải một thư viện triết học thứ hai và cũng không sở hữu lại Probability, Statistics, Psychology hay Economics. Đây là **lớp tích hợp (integration layer / 통합 계층)**: lấy các concept chuẩn gốc (canonical / 정본) đã nằm ở domain khác và biến chúng thành công cụ có thể mang sang quyết định đời sống, đầu tư, công việc, nghiên cứu, kinh doanh, engineering và đọc thông tin hằng ngày.

Mục tiêu là tạo một thói quen chung:

```text
Situation / claim / decision
→ frame the real problem
→ identify uncertainty
→ choose the right model
→ inspect evidence and causality
→ compare alternatives
→ inspect incentives and system effects
→ estimate payoff and downside
→ decide with explicit assumptions
→ define what new evidence would change the decision
```

## Vì sao cần `thinking/` nếu nội dung đã tồn tại?

Repository đã có các canonical owner:

- [Mathematics](../mathematics/README.md) sở hữu Probability, Statistics, expectation, optimization và formal models.
- [Psychology](../psychology/README.md) sở hữu cognitive bias, metacognition, decision under risk và human behavior.
- [Philosophy](../philosophy/README.md) sở hữu logic, argument, epistemology, evidence và calibration.
- [Economics](../economics/README.md) sở hữu scarcity, opportunity cost, incentives, equilibrium và game theory.
- [Research Methods](../research_methods/README.md) sở hữu study design, measurement, sampling, causal inference và evidence synthesis.

Nếu chép lại theory ở đây, repository sẽ duplicate và khó giữ consistency. Vì vậy mỗi topic trong `thinking/` tập trung vào **workflow**, **failure modes**, **câu hỏi kiểm tra**, **case application** và **handoff** sang canonical owner để học sâu.

## Cấu trúc

```text
thinking/
├── README.md
├── CONCEPTUAL_DEPENDENCIES.md
├── COVERAGE_AUDIT.md
├── problem-framing/
├── critical-thinking/
├── logical-fallacies/
├── cognitive-bias/
├── probability/
├── statistics-for-life/
├── causal-reasoning/
├── forecasting/
├── model-selection/
├── first-principles/
├── expected-value/
├── value-of-information/
├── risk/
├── opportunity-cost/
├── incentives/
├── systems-thinking/
├── game-theory/
├── decision-making/
├── practice/
└── 90_connections/
```

Xem [Conceptual Dependencies](./CONCEPTUAL_DEPENDENCIES.md) để biết tool nào phụ thuộc tool nào và route nào phù hợp theo loại câu hỏi. [`practice/`](./practice/README.md) dùng cho deliberate practice; [`90_connections/`](./90_connections/README.md) dùng cho applied cases cần phối hợp nhiều tool.

## Chọn route theo vấn đề

### 1. “Claim này có đáng tin không?”

[Problem Framing](./problem-framing/README.md) → [Critical Thinking](./critical-thinking/README.md) → [Statistics for Life](./statistics-for-life/README.md) → [Causal Reasoning](./causal-reasoning/README.md) → [Logical Fallacies](./logical-fallacies/README.md) / [Cognitive Bias](./cognitive-bias/README.md).

Dùng cho bài báo, research claim, chart, social media, business report và các con số có narrative đi kèm.

### 2. “Điều gì có thể xảy ra tiếp theo?”

[Probability](./probability/README.md) → [Forecasting](./forecasting/README.md) → [Model Selection](./model-selection/README.md) → [Risk](./risk/README.md).

Dùng khi uncertainty nằm ở tương lai: project schedule, investment assumption, demand, system capacity hoặc planning.

### 3. “Tôi nên chọn phương án nào?”

[Problem Framing](./problem-framing/README.md) → [Opportunity Cost](./opportunity-cost/README.md) → [Probability](./probability/README.md) → [Expected Value](./expected-value/README.md) → [Risk](./risk/README.md) → [Value of Information](./value-of-information/README.md) → [Decision Making](./decision-making/README.md).

Đây là route chính cho investment, insurance, career, purchasing, project và resource allocation.

### 4. “Vì sao kết quả này xảy ra?”

[Problem Framing](./problem-framing/README.md) → [Causal Reasoning](./causal-reasoning/README.md) → [Systems Thinking](./systems-thinking/README.md) → [Model Selection](./model-selection/README.md).

Dùng cho debugging, scientific explanation, business performance, social systems và failure analysis.

### 5. “Người khác sẽ phản ứng thế nào nếu rule thay đổi?”

[Incentives](./incentives/README.md) → [Game Theory](./game-theory/README.md) → [Systems Thinking](./systems-thinking/README.md) → [Decision Making](./decision-making/README.md).

Dùng khi outcome phụ thuộc vào adaptation của nhiều actor, không phải một cơ chế cơ học cố định.

### 6. “Có nên tìm hiểu thêm hay quyết định ngay?”

[Value of Information](./value-of-information/README.md) → [Risk](./risk/README.md) → [Decision Making](./decision-making/README.md).

Dùng để tránh hai cực: quyết định quá sớm khi thiếu evidence, hoặc research vô hạn dù information mới không còn khả năng thay đổi action.

## Practice — luyện reasoning thay vì chỉ đọc concept

[Thinking Practice](./practice/README.md) hiện có bốn drill:

1. [Calibration & Bayesian Updating](./practice/01_calibration_and_bayesian_updating.md) — đưa uncertainty thành probability/range có thể review và update.
2. [Sensitivity Analysis & Uncertainty Decomposition](./practice/02_sensitivity_analysis_and_uncertainty_decomposition.md) — tìm assumption nào thật sự làm conclusion đổi.
3. [Scenario Planning & Stress Testing](./practice/03_scenario_planning_and_stress_testing.md) — kiểm tra decision khi tương lai lệch base case hoặc system gặp stress.
4. [Decision Journal & Postmortem](./practice/04_decision_journal_and_postmortem.md) — tách process quality khỏi luck và tạo feedback loop qua thời gian.

Practice layer không thêm canonical theory. Nó biến knowledge thành kỹ năng bằng chu kỳ `estimate → expose assumptions → test → observe → update → review`.

## Casebook — từ concept sang tình huống thật

[Thinking Connections](./90_connections/README.md) ghép nhiều tool trên cùng một case:

1. [Đọc tin, số liệu và claim trên Internet](./90_connections/00_news_claims_and_online_information.md)
2. [Tiền, đầu tư, bảo hiểm và quyết định tài chính](./90_connections/01_money_investing_and_insurance.md)
3. [Engineering incident, debugging và system reliability](./90_connections/02_engineering_incidents_and_debugging.md)
4. [Đọc nghiên cứu, health claim và statistical evidence](./90_connections/03_research_health_and_statistics.md)
5. [Career, learning và project decisions](./90_connections/04_career_learning_and_projects.md)
6. [Business, metrics, incentives và organizations](./90_connections/05_business_metrics_incentives_and_organizations.md)
7. [Negotiation, bargaining và conflict](./90_connections/06_negotiation_bargaining_and_conflict.md)
8. [Politics, public policy và institutions](./90_connections/07_politics_policy_and_institutions.md)

Casebook có ba mức depth: quick pass cho vấn đề nhỏ, normal pass cho quyết định thường ngày và deep pass cho quyết định material/khó đảo ngược.

## Cross-domain map

| Thinking tool | Những nơi nên dùng ngay |
|---|---|
| Problem Framing | [PMP](../pmp/README.md), [Computer Science](../computer_science/README.md), [Research Methods](../research_methods/README.md), [Economics](../economics/README.md) |
| Critical Thinking | [Philosophy](../philosophy/README.md), [Research Methods](../research_methods/README.md), [World History](../world_history/README.md), [Psychology](../psychology/README.md), [Sociology](../sociology/README.md) |
| Probability | [Mathematics](../mathematics/README.md), [Investing](../investing/README.md), [Research Methods](../research_methods/README.md), [Psychology](../psychology/README.md), [Economics](../economics/README.md) |
| Statistics for Life | [Research Methods](../research_methods/README.md), [Biology](../biology/README.md), [Psychology](../psychology/README.md), [Economics](../economics/README.md), [Investing](../investing/README.md) |
| Causal Reasoning | [Research Methods](../research_methods/README.md), [Economics](../economics/README.md), [Computer Science](../computer_science/README.md), [Psychology](../psychology/README.md) |
| Forecasting | [Investing](../investing/README.md), [PMP](../pmp/README.md), [Economics](../economics/README.md), [Data Engineering](../data_engineering/README.md) |
| Model Selection | [Mathematics](../mathematics/README.md), [Economics](../economics/README.md), [Computer Science](../computer_science/README.md), [Research Methods](../research_methods/README.md) |
| Opportunity Cost | [Economics](../economics/README.md), [Investing](../investing/README.md), [PMP](../pmp/README.md), [Psychology](../psychology/README.md) |
| Expected Value | [Mathematics](../mathematics/README.md), [Investing](../investing/README.md), [PMP](../pmp/README.md), [Economics](../economics/README.md) |
| Value of Information | [Research Methods](../research_methods/README.md), [PMP](../pmp/README.md), [Computer Science](../computer_science/README.md), [Investing](../investing/README.md) |
| Incentives | [Economics](../economics/README.md), [Korea Business & Economy](../korea_business_economy_knowledge_library/README.md), [Psychology](../psychology/README.md), [Sociology](../sociology/README.md), [Philosophy](../philosophy/README.md) |
| Risk | [Investing](../investing/README.md), [PMP](../pmp/README.md), [Research Methods](../research_methods/README.md), [Computer Science](../computer_science/README.md) |
| Systems Thinking | [Biology](../biology/README.md), [Economics](../economics/README.md), [Computer Science](../computer_science/README.md), [Data Engineering](../data_engineering/README.md), [Sociology](../sociology/README.md) |
| Game Theory | [Economics](../economics/README.md), [Psychology](../psychology/README.md), [Korea Business & Economy](../korea_business_economy_knowledge_library/README.md), [Computer Science](../computer_science/README.md) |

## Unified protocol

Với một claim hoặc decision quan trọng, chạy protocol sau ở mức depth phù hợp:

1. **Frame** — Ta thật sự đang hỏi hoặc quyết định điều gì? Outcome và constraint là gì?
2. **Alternatives** — Có những explanation hoặc option nào khác?
3. **Base rate** — Trước khi nhìn case này, case tương tự thường ra sao?
4. **Evidence** — Dữ liệu là observation, experiment, survey, anecdote hay model output?
5. **Causality** — Evidence nói association hay intervention effect?
6. **Model** — Lens nào phù hợp và assumptions nào đang bị bỏ qua?
7. **Forecast** — Những future states nào plausible và confidence bao nhiêu?
8. **Payoff** — Upside/downside của mỗi state là gì?
9. **Risk** — Tail risk, ruin, irreversibility, correlation hoặc blast radius có đáng lo không?
10. **Opportunity cost** — Option tốt nhất bị bỏ qua là gì?
11. **Incentives** — Actor nào có payoff gì và rule change làm behavior đổi thế nào?
12. **System** — Feedback loop, delay, bottleneck và second-order effect nào tồn tại?
13. **Bias check** — Ta có đang bảo vệ conclusion đã thích từ trước không?
14. **Information value** — Evidence bổ sung nào có thể đổi action, và nó có đáng cost/delay không?
15. **Decision / update rule** — Chọn action nào và evidence nào trong tương lai sẽ khiến ta đổi ý?

Không phải vấn đề nào cũng cần đủ 15 bước. Complexity của reasoning nên tỷ lệ với **stakes × uncertainty × irreversibility**.

## Boundary

`thinking/` không thay thế domain chuyên môn. Decision framework không thay thế medical evidence; expected value không thay thế portfolio construction; logical fallacy không chứng minh một conclusion sai; systems thinking không tự tạo causal evidence; incentive analysis không tự chứng minh motive của một cá nhân; forecast không trở thành fact chỉ vì có probability.

Khi vấn đề chuyển từ công cụ suy nghĩ sang kiến thức chuyên ngành, hãy handoff về canonical domain tương ứng.