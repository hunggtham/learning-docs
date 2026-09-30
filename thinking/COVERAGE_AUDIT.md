# Thinking Toolkit — Coverage Audit

## Mục tiêu

`thinking/` là integration layer, không phải canonical owner của logic, probability, statistics, psychology hay economics. Audit này kiểm tra bốn điều:

```text
coverage đủ rộng để dùng thực tế
without theory duplication
with explicit handoff
with cross-domain application
```

## Coverage hiện tại

### Problem definition

- Problem Framing
- First Principles
- Model Selection

### Evidence and belief

- Critical Thinking
- Logical Fallacies
- Cognitive Bias
- Probability
- Statistics for Life
- Causal Reasoning

### Future uncertainty

- Forecasting
- Expected Value
- Risk
- Value of Information

### Choice and trade-off

- Opportunity Cost
- Decision Making

### Multi-actor / dynamic systems

- Incentives
- Game Theory
- Systems Thinking

### Applied integration

Casebook hiện bao phủ:

- online claims/news;
- money/investing/insurance;
- engineering/debugging;
- research/health evidence;
- career/learning/projects;
- business/metrics/organizations;
- negotiation/bargaining/conflict;
- politics/public policy/institutions.

### Deliberate practice

`practice/` hiện bao phủ các năng lực khó hình thành chỉ bằng đọc concept:

- calibration và Bayesian updating;
- sensitivity analysis và uncertainty decomposition;
- scenario planning và stress testing;
- decision journal và postmortem.

Practice và casebook có vai trò khác nhau:

```text
practice/       skill-first, lặp lại cùng reasoning skill qua nhiều context
90_connections/ case-first, chọn và phối hợp nhiều tools cho một context thực tế
```

## Canonical ownership check

| Concept | Canonical owner | `thinking/` chỉ giữ |
|---|---|---|
| Logic / argument | Philosophy | practical claim checks |
| Probability / statistics | Mathematics | everyday uncertainty workflow + calibration drills |
| Cognitive bias / decision science | Psychology | bias checks inside decisions và review process |
| Opportunity cost / incentives / game theory | Economics | cross-domain application / negotiation workflow |
| Causal inference / evidence synthesis | Research Methods + Econometrics | causal checklist / tool selection |
| Project risk / governance | PMP | generic decision/risk/scenario layer |
| Investing mechanics | Investing | reasoning workflow only |
| Public institutions / law / civic systems | relevant civic, legal, economics and history domains | neutral reasoning workflow for policy/institution claims |

## Quality gates

Một topic trong `thinking/` đạt chuẩn khi có:

1. problem/failure mode rõ;
2. intuition trước formula;
3. workflow có thể dùng;
4. boundary — tool không chứng minh được điều gì;
5. ít nhất hai internal links;
6. handoff về canonical theory;
7. ví dụ không biến anecdote thành evidence;
8. không tạo pseudo-precision.

Một practice drill thêm ba gate:

9. có output có thể ghi lại hoặc review;
10. phân biệt process quality với outcome/luck;
11. tạo được update loop thay vì bài tập một lần.

## Những điều cố ý không thêm

### “100 mental models” list

Không thêm danh sách dài mental model nếu không có dependency và application. Repository ưu tiên một graph nhỏ nhưng dùng được hơn taxonomy lớn để ghi nhớ.

### Duplicate Bayesian/statistics chapters

Formal derivation tiếp tục ở Mathematics. `thinking/` chỉ dùng Bayesian intuition, base rate, updating và calibration khi cần cho reasoning.

### Duplicate behavioral economics

Behavioral theory tiếp tục ở Psychology/Economics. `thinking/` chỉ nối bias/incentive vào decision workflow.

### Domain-specific advice

Không biến `thinking/` thành medical, legal, financial, political hoặc engineering handbook. Casebook phải handoff khi reasoning chạm subject-matter detail.

## Integration status

### Repository-level discoverability — implemented

- root `README.md` có Thinking Toolkit entrypoint;
- `CATALOG.md` đăng ký `thinking` là canonical domain trong group `Methods`;
- Philosophy, Economics và Research Methods README đã backlink về `thinking/` và ghi rõ ownership boundary;
- Psychology conceptual-dependency map đã nối cognitive bias/decision/negotiation sang `thinking/`;
- Investing Foundations đã nối probability → expected value → risk → decision making và practice drills;
- Computer Science Security/Reliability hub đã nối incident/debugging sang problem framing, causal reasoning, systems thinking và risk;
- CATALOG knowledge graph đã thêm `thinking` vào các `related` phù hợp.

### Outbound links — implemented

`thinking/` đã nối sang Mathematics, Philosophy, Psychology, Economics, Research Methods, Investing, Biology, Sociology, World History, PMP, Computer Science, Backend, Frontend, DevOps/Platform Engineering, Data Engineering, Korea Business & Economy và các civic/institutional domains phù hợp.

### Inbound links — selective, ongoing

Không thêm backlink cơ học vào mọi file chỉ để tăng link count. Backlink chỉ nên xuất hiện ở entrypoint/chapter nơi tool giúp reader chuyển context thực sự.

Các điểm inbound có giá trị cao đã triển khai gồm Philosophy, Economics, Research Methods, Psychology, Investing và Computer Science Security/Reliability. Những nơi còn có thể bổ sung khi có chỉnh sửa tự nhiên ở domain đó:

```text
PMP → Risk / Value of Information / Decision Making / Stress Testing
DevOps / Data Engineering → Causal Reasoning / Systems Thinking / Incident case
Sociology / civic domains → Incentives / Game Theory / Policy-institution case
```

Đây là backlog integration, không phải lý do tự tạo commit sửa hàng loạt canonical files.

## Gap review sau integration pass

Các candidate trước đây đã được xử lý:

- negotiation / bargaining integration → `90_connections/06_negotiation_bargaining_and_conflict.md`;
- politics / public policy / institutions → `90_connections/07_politics_policy_and_institutions.md`;
- Bayesian updating applied drills → `practice/01_calibration_and_bayesian_updating.md`;
- uncertainty decomposition / sensitivity analysis → `practice/02_sensitivity_analysis_and_uncertainty_decomposition.md`;
- scenario planning / stress testing → `practice/03_scenario_planning_and_stress_testing.md`;
- decision journal / review exercises → `practice/04_decision_journal_and_postmortem.md`.

## Next depth rule

Không mở thêm taxonomy chỉ vì có một mental model nổi tiếng. Chỉ mở topic/practice/case mới khi ít nhất một trong ba điều đúng:

1. casebook hiện tại có recurring failure mode chưa được tool nào xử lý;
2. một cross-domain route phải duplicate explanation vì thiếu integration node;
3. practice review cho thấy skill quan trọng nhưng không có drill hoặc feedback loop.

Ở trạng thái hiện tại, ưu tiên **sử dụng, backlink có chọn lọc và consistency** hơn là tăng số folder.