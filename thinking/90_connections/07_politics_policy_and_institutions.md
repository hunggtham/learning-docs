# Politics, Public Policy & Institutions — Phân tích rule, incentives và evidence

Political/public-policy claim thường khó vì nhiều tầng bị trộn vào nhau:

```text
value judgment
institutional rule
actor incentive
behavioral response
causal effect
aggregate outcome
political communication
```

Case này không dạy ideology hay kết luận chính trị cụ thể. Mục tiêu là cung cấp workflow trung lập để đọc claim về chính sách, luật, nhà nước và institutions. Canonical facts/history phải handoff sang domain chính trị, pháp luật, Economics, Sociology hoặc History tương ứng.

## 1. Tách claim trước khi tranh luận

Một câu như:

> “Chính sách X tốt cho nền kinh tế.”

có thể chứa nhiều claim:

```text
X thật sự thay đổi rule nào?
actor nào chịu tác động trực tiếp?
behavior nào được dự đoán sẽ đổi?
metric kinh tế nào được gọi là “tốt”?
trong horizon bao lâu?
ai được lợi / ai chịu cost?
```

Nếu chưa tách, hai người có thể tranh luận về hai câu hỏi khác nhau.

Xem [Problem Framing](../problem-framing/README.md).

## 2. Descriptive, causal và normative là ba lớp khác nhau

### Descriptive

```text
Thuế suất tăng từ A lên B.
```

Đây là fact về rule nếu nguồn chính thức xác nhận.

### Causal

```text
Thay đổi thuế làm investment giảm Y%.
```

Đây là empirical causal claim; cần design/evidence.

### Normative

```text
Vì vậy chính sách là tốt/xấu.
```

Đây cần thêm value judgment: growth, equality, liberty, stability, health, environment, distribution hoặc mục tiêu khác được weighted thế nào.

Evidence không tự quyết định value weights.

## 3. Formal rule ≠ effective institution

Luật trên giấy không luôn bằng thực tế vận hành.

Hỏi:

```text
Ai thực thi?
Enforcement capacity thế nào?
Có discretion không?
Penalty có credible không?
Actor có cách né/lách không?
Informal norm có làm rule khác đi không?
```

Đây là điểm nối giữa legal text và institutional outcome.

## 4. Incentive map

Thay vì đoán “politician/business/voter muốn gì”, map observable incentives:

| Actor | Formal power | Objective / payoff | Constraint | Information | Accountability |
|---|---|---|---|---|---|
| voter | vote | mixed | limited information/time | partial | election cycle |
| politician | policy/agenda power | re-election, policy goals, coalition | institutions | asymmetric | voters/party/law |
| agency | implementation | mandate, budget, career | statute/resources | operational | legislature/executive/courts |
| business | production/lobby/compliance | profit/survival | market/law | firm-specific | regulators/market |

Bảng này là scaffold, không phải universal truth. Objective thực tế thay đổi theo institution/context.

Xem [Incentives](../incentives/README.md).

## 5. Policy changes behavior, behavior changes policy outcome

Không đánh giá policy chỉ từ first-order intention.

Ví dụ generic:

```text
subsidy introduced
→ target activity cheaper
→ demand rises
→ supplier response changes
→ input prices / capacity change
→ fiscal cost changes
→ political pressure for continuation changes
```

Second-order effects có thể củng cố hoặc làm yếu mục tiêu ban đầu.

Xem [Systems Thinking](../systems-thinking/README.md).

## 6. Incidence ≠ statutory payer

Người được ghi trên luật là payer không nhất thiết chịu toàn bộ economic burden.

Tax/regulation cost có thể truyền qua:

```text
prices
wages
profits
rents
entry / exit
quality
waiting time
```

Economic incidence là empirical/model question, không suy trực tiếp từ legal incidence.

Handoff sang [Economics](../../economics/README.md) khi cần formal analysis.

## 7. Counterfactual là bắt buộc cho causal claim

Nếu outcome cải thiện sau policy, chưa đủ kết luận policy gây ra improvement.

Hỏi:

```text
Nếu policy không được áp dụng,
outcome có thể đã diễn biến thế nào?
```

Potential alternatives:

- broader economic cycle;
- technology trend;
- demographic change;
- another concurrent policy;
- regression to the mean;
- selection differences.

Xem [Causal Reasoning](../causal-reasoning/README.md) và [Research Methods](../../research_methods/README.md).

## 8. Before/after chart không tự tạo causality

Một chart:

```text
policy date | outcome rises afterwards
```

chỉ cho temporal association. Cần xem identification strategy, comparison group, trend, anticipation effect và concurrent shocks.

Đặc biệt cẩn thận với chart bắt đầu đúng năm làm narrative đẹp nhất.

## 9. Distribution matters

Average outcome có thể che distribution:

```text
Who gains?
Who loses?
How large?
Temporary or persistent?
Can losers adjust?
```

Một policy có thể tăng aggregate output nhưng giảm welfare của một nhóm; hoặc giảm aggregate output nhỏ để đạt objective khác. Đây là lý do positive analysis và normative judgment phải tách.

## 10. Time horizon

Cùng policy có thể có:

```text
short-run effect
medium-run adaptation
long-run equilibrium effect
```

Ví dụ firms chưa thể thay capital stock ngay, nhưng có thể adjust technology/location trong nhiều năm.

Không extrapolate short-run estimate sang long run nếu mechanism thay đổi.

## 11. Strategic response và game theory

Khi nhiều governments, firms, parties hoặc interest groups phản ứng lẫn nhau, static analysis có thể sai.

```text
Actor A changes rule
→ B adapts
→ A anticipates adaptation
→ A redesigns rule
```

Trong trade, regulation, election strategy hoặc bargaining, outcome là equilibrium của responses chứ không chỉ direct effect của một move.

Xem [Game Theory](../game-theory/README.md).

## 12. Principal–agent problem

Người giao quyền và người thực thi có thể khác objective/information.

```text
citizen → elected representative
legislature → agency
shareholder/public → state-owned enterprise manager
central government → local implementation
```

Hỏi:

```text
Who delegates to whom?
What can principal observe?
What can agent hide?
How is performance measured?
What incentives does measurement create?
```

Metric design có thể tạo gaming.

## 13. Goodhart-style failure

Khi metric trở thành target, actor có thể optimize metric thay vì underlying objective.

Ví dụ generic:

```text
target = number of cases processed
→ faster processing
→ possibly lower quality / cherry-picking
```

Không phải mọi target đều thất bại; câu hỏi là metric có proxy quality tốt đến đâu và gaming cost thế nào.

## 14. Base rate cho policy promise

Khi nghe:

> “Program này sẽ hoàn thành đúng budget và đạt target.”

hãy hỏi reference class:

```text
projects/programs tương tự trước đây có cost overrun bao nhiêu?
implementation delay thường ra sao?
forecast error distribution thế nào?
```

Inside view vẫn quan trọng, nhưng base rate giúp chống planning fallacy.

Xem [Forecasting](../forecasting/README.md).

## 15. Source hierarchy

Tùy câu hỏi:

### Rule / institution fact

Ưu tiên constitution, statute, regulation, official agency material, court decision hoặc primary institutional source.

### Economic/social effect

Ưu tiên research có design phù hợp, systematic review, official statistics với methodology rõ; không coi press release là causal study.

### Historical claim

Ưu tiên primary/credible secondary historical scholarship và context.

### Political statement

Dùng speech/manifesto để biết actor **nói gì**, không tự dùng nó làm evidence rằng causal/economic claim trong statement là đúng.

## 16. Compare countries carefully

Cross-country comparison hữu ích nhưng dễ sai vì institutions khác nhau.

Trước khi nói “Country A làm được nên B cũng làm được”, kiểm tra:

```text
state capacity
legal system
fiscal capacity
market structure
demography
geography
political institutions
baseline income/productivity
international constraints
```

Country label không phải causal variable duy nhất.

## 17. Policy scenario analysis

Dùng ít nhất ba world:

```text
intended response
partial adaptation
strategic / unintended response
```

Với mỗi world:

```text
mechanism
winners / losers
fiscal/resource cost
leading indicators
reversibility
```

Xem [Scenario Planning & Stress Testing](../practice/03_scenario_planning_and_stress_testing.md).

## 18. Value of information

Không phải policy debate nào cũng cần “thêm data” vô hạn.

Hỏi:

```text
Uncertainty nào đang làm decision đổi?
Study/data nào có thể giảm uncertainty đó?
Có thể pilot không?
Decision có reversible không?
Cost của delay là gì?
```

Pilot có thể tạo information nhưng cũng có externality, political lock-in hoặc scale-up issue.

Xem [Value of Information](../value-of-information/README.md).

## 19. Political communication và motivated reasoning

Issue identity-laden làm confirmation bias mạnh hơn. Một defense đơn giản:

```text
Trước khi biết party/person nào đề xuất,
criteria nào tôi sẽ dùng để đánh giá policy này?
```

Sau đó áp cùng criteria cho alternatives.

Không có nghĩa mọi proposal tương đương; mục tiêu là giữ evaluation rule ổn định.

## 20. Steelman trước critique

Trước khi phản bác, viết version mạnh nhất có thể của mechanism:

```text
Policy aims at X
through mechanism Y
under assumptions A/B/C
with expected trade-off D
```

Sau đó critique assumption/evidence, không critique caricature.

## 21. Drill — đọc một policy claim

Lấy một claim đang thấy trên news/social media và điền:

```text
Exact claim:
Claim type: descriptive / causal / normative
Formal rule:
Actors:
Incentives:
Intended mechanism:
Alternative mechanisms:
Counterfactual:
Evidence type:
Main confounders:
Short-run effect:
Long-run adaptation:
Distribution:
Second-order effects:
Strategic response:
Uncertainty:
What evidence would change my view:
Canonical domain to consult:
```

## 22. Failure modes

### Motive fallacy

Một actor có incentive không chứng minh họ đã thực hiện một action cụ thể vì incentive đó.

### Policy by anecdote

Một beneficiary/victim story có thể minh họa mechanism nhưng không estimate prevalence/effect size.

### Country cherry-picking

Chọn một country thành công sau policy không tạo causal proof.

### One-metric politics

GDP, unemployment, inequality, crime, health hoặc approval đều có measurement/coverage limits. Một metric không đại diện toàn welfare.

### Institution-free comparison

Copy policy text mà không xét enforcement/capacity có thể cho outcome khác hoàn toàn.

### False neutrality

Tách fact/value không có nghĩa tránh kết luận. Khi evidence đủ, có thể kết luận descriptive/causal claim mạnh; chỉ cần nói rõ phần nào là evidence và phần nào là value trade-off.

## 23. Workflow

```text
Frame claim
→ separate descriptive / causal / normative layers
→ verify institutional facts
→ map actors / incentives / constraints
→ specify mechanism and counterfactual
→ inspect evidence / identification
→ model distribution and time horizon
→ anticipate strategic / system response
→ assess uncertainty and reversibility
→ decide / update with explicit value criteria
```

## Connections

- [Critical Thinking](../critical-thinking/README.md)
- [Causal Reasoning](../causal-reasoning/README.md)
- [Incentives](../incentives/README.md)
- [Game Theory](../game-theory/README.md)
- [Systems Thinking](../systems-thinking/README.md)
- [Forecasting](../forecasting/README.md)
- [Economics](../../economics/README.md)
- [Research Methods](../../research_methods/README.md)
- [Philosophy](../../philosophy/README.md)
- [Sociology](../../sociology/README.md)
- [World History](../../world_history/README.md)
- [Korea Law, Civic & Everyday Life](../../korea_law_civic_life/README.md)

Political reasoning tốt không bắt đầu bằng “phe nào đúng?”. Nó bắt đầu bằng **claim nào đang được đưa ra, rule nào thật sự tồn tại, mechanism nào được dự đoán, evidence nào phân biệt các explanation, và trade-off/value nào đang được lựa chọn**.