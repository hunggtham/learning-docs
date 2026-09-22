# PMP Knowledge Library — Coverage & Depth Audit

## Trạng thái audit

Audit cập nhật ngày 2026-09-22 sau các vòng canonicalization, systems-depth, exam-application, **full-depth mechanism pass** và follow-up cross-domain refinement. Coverage của thư viện được đánh giá theo mental model và decision capability, không theo số lượng chapter hoặc line count. Một topic chỉ được xem là đủ sâu khi người đọc có thể hiểu problem, mechanism, assumption/boundary, failure mode, evidence cần quan sát và cách decision đổi khi context đổi.

Audit dùng PMP Examination Content Outline có hiệu lực từ tháng 7/2026 làm exam map, PMBOK® Guide Eighth Edition làm standards context, đồng thời tham chiếu guidance PMI hiện hành về AI và sustainability. Learning dependency của repository vẫn được tổ chức theo causal understanding thay vì copy mục lục của standard hoặc ECO.

Kết luận hiện tại: **17 canonical learning chapters đủ bao phủ PMP core theo conceptual dependency và đã có systems-level depth ở mọi domain chính. Không có conceptual gap nào biện minh cho chapter mới ở vòng này.**

Full-depth pass đầu tiên tập trung `00`, `07–12` và `16`. Follow-up refinement sau đó tiếp tục đóng các gap có giá trị ở `01–04` và `15`: uncertainty profile/tailoring debt, people decision architecture/team resilience, stakeholder sensing/information validity, assumption/change-collision/integration debt và quantitative model robustness. Các chapter còn lại chỉ nên sửa khi xuất hiện missing mechanism thật; line count không phải proxy cho chất lượng.

## Canonical depth status

| Chapter | Trạng thái | Depth hiện tại |
|---|---|---|
| [00 Foundations & Value](./00_foundations_value_and_project_system.md) | Deepened+ | project/operations boundary, causal problem framing, symptom-vs-mechanism-vs-constraint, output→outcome→value chain, benefit assumptions/counterfactual attribution, distribution of value/harm, option space/premature commitment, success time horizon, trade-off second-order effects, control-system sensor/actuator/latency, decision rights, strategy/portfolio/product boundary, continue/pivot/stop criteria, temporary-organization transaction cost, transition debt, complexity/feedback loops, ethics as value boundary |
| [01 Lifecycle & Tailoring](./01_lifecycle_delivery_approaches_and_tailoring.md) | Deepened+ | project/development lifecycle, commitment progression/irreversibility, five uncertainty dimensions, feedback type/latency, cost-of-change economics, predictive/adaptive failure boundaries, batch/risk exposure, hybrid interface contracts, tailoring as control system, control intensity by consequence, governance latency, planning-vs-decision horizon, stage-gate exit options, organizational capability, transition readiness, control accumulation/retirement, mixed uncertainty profile, uncertainty migration across lifecycle, multi-cadence synchronization, decision-flip test, methodology inertia/tailoring debt |
| [02 People](./02_people_leadership_team_and_conflict.md) | Deepened+ | leadership as decision-environment design, shared mental models, empowerment/accountability, delegation failure modes, reversibility-based decision rights, authority gradient/escalation friction/shadow authority, power asymmetry/dissent, psychological safety as sensor quality, topology/coordination surface, nonlinear coordination load, decision-load/attention budget, task-vs-relationship conflict, conflict debt, incentive/metric side effects, situational leadership, capability redundancy/team resilience, consensus limits, timezone latency, burnout/recovery debt, people evidence linked to project state, accountability feedback loop |
| [03 Stakeholders](./03_stakeholders_communication_and_knowledge.md) | Deepened+ | stakeholder network/coalition, dynamic salience, dependency-vs-power, representation risk/proxy validity, resistance diagnostics, feedback sampling bias, expectation debt, promise-vs-forecast semantics, closed-loop communication, latency/service levels, information half-life/freshness, channel richness, executive compression/distortion, incentive-driven noise, BATNA/ZOPA/leverage plus option creation, trust repair, stakeholder-risk propagation, knowledge decay/ownership, reasoning-capability transfer, translation semantic risk, attention economics, stakeholder decision debt |
| [04 Integration & Scope](./04_integration_scope_requirements_and_change.md) | Deepened+ | integration as project operating system, constraint coupling/nonlinearity, requirement conflict, assumption dependency graph/assumption debt, verification-vs-validation, traceability/blast radius, interfaces, acceptance debt, cost-of-change timing, change authority/materiality/latency, concurrent-change collision risk, configuration propagation, compatibility/migration window, scope-schedule-cost baseline topology, integration debt, interface contracts, decision provenance |
| [05 Schedule & Flow](./05_schedule_estimation_and_flow.md) | Deepened+ | causal network model, lead/lag semantics, dependency classes, CPM/float, negative float, hard/soft constraints, resource calendars, estimate distributions/reference class, near-critical switching, convergence/merge bias/correlation, resource contention, compression diminishing returns, external windows, Little's Law/queues/bottlenecks, schedule-health/open-end diagnostics |
| [06 Finance & Value](./06_finance_cost_and_value_measurement.md) | Deepened+ | estimate/budget/funding distinction, commitment/accrual/actual/cash states, committed-cost early warning, incremental economics/opportunity cost, reserve-vs-risk retirement, funding-limit reconciliation, payment terms, FX/inflation/tax boundary, EVM measurement limits, EAC/TCPI, variance attribution, burn/runway, sunk-vs-cancellation cost, marginal analysis, ROI/payback/NPV/BCR/break-even, cost of delay/quality, benefit attribution, living business case |
| [07 Quality, Resources & Procurement](./07_quality_resources_and_procurement.md) | Deepened+ | fitness/grade, operational criteria, process capability/quality-at-source, prevention/appraisal/failure economics, quality debt/escaped defects, root/contributing causes, statistical/process-drift intuition, effective capacity/utilization paradox, non-fungible skills, learning curve, shared-resource contention, procurement principal–agent/information asymmetry, make-or-buy option/capability cost, risk allocation, contract incentive architecture, supplier health, SOW/acceptance, claims `entitlement→causation→quantum`, negotiation/dispute, supply-chain common cause, tested exit strategy |
| [08 Risk & Decisions](./08_risk_uncertainty_issues_and_decisions.md) | Deepened+ | event risk plus ambiguity/variability/complexity, epistemic-vs-aleatory uncertainty, causal risk-model quality, weak signals/near misses, velocity/proximity/detectability/controllability, risk-adjusted value, scenario/stress/break-point analysis, Monte Carlo/P50/P80/correlation/sensitivity, preventive-detective-corrective controls and effectiveness evidence, risk capacity/appetite/threshold, reserve-vs-risk retirement, systemic/common-cause/concentration risk, robustness/resilience/recoverability, issue triage/crisis authority, Value of Information/real options, cost-of-waiting/decision regret, calibration/hindsight/cognitive bias |
| [09 Governance & Environment](./09_governance_compliance_and_business_environment.md) | Deepened+ | governance as decision architecture, governance debt, decision queue/latency, sponsor attention, PMO operating models, independent assurance, portfolio WIP/capacity, incremental funding/progressive commitment, program/portfolio dependencies and strategic drift, policy hierarchy, compliance-by-design, materiality/proportional control, exception concentration, environmental signal→trigger→response horizon, living business case, benefit dependency network, change readiness/reinforcement/saturation, adoption, truth-to-power/ethics, governance failure modes |
| [10 Adaptive & Hybrid](./10_agile_hybrid_and_adaptive_delivery.md) | Deepened+ | feedback economics, hypothesis→evidence→decision loop, empiricism/evidence quality, product goal as stable direction, backlog as option set plus aging/option decay, value/risk/learning/dependency/cost-of-delay priority, Done→deployed→released→value distinction, MVP/prototype/experiment boundaries, experiment decision rules, economic batch size, WIP/queues/class-of-service, Scrum/Kanban control loops, probabilistic forecast/calibration, decision horizon, continuous adaptive change control, technical option value, hybrid cadence mismatch/synchronization cost, adaptive funding/governance, autonomy-vs-blast-radius, scaling/dependency economics |
| [11 Measurement & Closure](./11_measurement_status_closure_and_continuous_improvement.md) | Deepened+ | metric as sensor/information system, measurement error-vs-model error, proxy distance, leading/lagging plus false-positive/negative trade-offs, baseline/actual/forecast, calibration plus responsiveness/stability, causal status narrative, percent-complete limits, metric portfolio/guardrails, thresholds/hysteresis, Goodhart/denominator/segmentation, aggregation loss, information+decision+action latency, benefit attribution/decay/unintended effects, knowledge capture/retrieval, post-mortem action effectiveness, closure as residual-risk transfer, operational readiness, legacy decommission, benefit ownership, improvement WIP/process stability, metric lifecycle |
| [12 AI & Sustainability](./12_ai_sustainability_and_modern_project_context.md) | Deepened+ | AI as socio-technical system, use-case/model/operating-system separation, intended-use/performance envelope, data-model-use-action boundaries, automation-level design, risk tiering, meaningful human oversight and oversight failure, abstention/fallback capacity, data provenance/rights/lineage, harm/segment/operating-condition evaluation, benchmark leakage/red-team/misuse, drift taxonomy/configuration/version traceability, semantic observability, incident remediation, vendor/concentration risk, automation bias, hidden human labor, shadow AI; sustainability Planet–People–Prosperity, materiality, lifecycle boundary, externality/burden shifting/rebound, value-chain evidence, obsolescence and pilot-to-production gap |
| [13 Scenario Reasoning](./13_pmp_scenario_reasoning_and_exam_strategy.md) | Deepened+ | state-based eight-step framework, surface-vs-reasoning-core distinction, five-gate answer filter, lifecycle/signal/authority/information/reversibility, assess-vs-act-vs-escalate, artifact/dashboard/practicum interpretation, domain patterns, distractor taxonomy, formula assumptions, mini-scenarios, counterfactual/error-log practice loop |
| [14 Artifacts & Traceability](./14_artifacts_information_and_traceability.md) | Deepened+ | artifacts as external memory/evidence architecture, source→state→decision→report layers, semantic contracts, data lineage, state transitions, bidirectional traceability/traceability debt, baseline-vs-working state, artifact lifecycle/effective state, immutable history/audit trail, change/decision provenance, gate evidence packages, dashboard compression/aggregation, information latency/freshness SLO, authoritative sources/versioning/access, automation boundaries, tacit transfer, artifact minimization/failure modes |
| [15 Quantitative Reasoning](./15_quantitative_reasoning_worked_examples.md) | Deepened+ | CPM forward/backward pass, total/free float, PERT expected value/variance, EVM state metrics and SPI limits, multiple EAC assumptions, ETC/VAC/TCPI, EMV/decision trees, Value of Information, NPV, Little's Law, communication-channel intuition, contract risk allocation, sensitivity/Monte Carlo/confidence reserve, claim arithmetic, integrated quantitative scenario, robustness check, decision-reversal threshold, model risk, forecast calibration, cross-metric consistency, unit/dimensional sanity; every formula tied to model validity and causal assumptions |
| [16 End-to-End Cases](./16_end_to_end_case_studies.md) | Deepened+ | predictive DR-site, adaptive product discovery, hybrid eKYC, troubled-project recovery, AI-assisted claims, portfolio/PMO shared-dependency case, contractual-claim micro-case; cross-case synthesis of invariants-vs-context variables, moving bottlenecks, risk state transitions, local-success/global-failure, decision-quality-vs-outcome-quality; seven-pass deliberate-practice loop |

`Deepened+` chỉ có nghĩa chapter đã có đủ mechanism/system layer cho audit hiện tại; đây không phải ranking chất lượng giữa chapter.

## Mapping với PMP 2026

| PMP 2026 domain/task cluster | Canonical chapter |
|---|---|
| People: shared vision, conflict, lead team | [02 People](./02_people_leadership_team_and_conflict.md) |
| People: stakeholder engagement/expectations | [03 Stakeholders](./03_stakeholders_communication_and_knowledge.md) |
| People: knowledge transfer, communication/reporting | [03 Stakeholders](./03_stakeholders_communication_and_knowledge.md), [11 Measurement & Closure](./11_measurement_status_closure_and_continuous_improvement.md), [14 Artifacts](./14_artifacts_information_and_traceability.md) |
| Process: integrated plan, delivery approach | [01 Lifecycle & Tailoring](./01_lifecycle_delivery_approaches_and_tailoring.md), [04 Integration](./04_integration_scope_requirements_and_change.md) |
| Process: scope, requirements and integrated change | [04 Integration & Scope](./04_integration_scope_requirements_and_change.md), [14 Traceability](./14_artifacts_information_and_traceability.md) |
| Process: value-based delivery/business case | [00 Foundations & Value](./00_foundations_value_and_project_system.md), [06 Finance & Value](./06_finance_cost_and_value_measurement.md) |
| Process: resources, procurement | [07 Quality, Resources & Procurement](./07_quality_resources_and_procurement.md) |
| Process: finance/funding/forecast | [06 Finance](./06_finance_cost_and_value_measurement.md), [15 Quantitative Reasoning](./15_quantitative_reasoning_worked_examples.md) |
| Process: quality | [07 Quality](./07_quality_resources_and_procurement.md) |
| Process: schedule/dependency/flow | [05 Schedule & Flow](./05_schedule_estimation_and_flow.md), [15 Quantitative Reasoning](./15_quantitative_reasoning_worked_examples.md) |
| Process: risk/uncertainty/resilience | [08 Risk & Decisions](./08_risk_uncertainty_issues_and_decisions.md), [15 Quantitative Reasoning](./15_quantitative_reasoning_worked_examples.md) |
| Process: status, artifacts, closure | [11 Measurement & Closure](./11_measurement_status_closure_and_continuous_improvement.md), [14 Artifacts](./14_artifacts_information_and_traceability.md) |
| Business Environment: governance/portfolio/PMO | [09 Governance](./09_governance_compliance_and_business_environment.md), [16 Case Studies](./16_end_to_end_case_studies.md) |
| Business Environment: compliance/evidence | [09 Governance](./09_governance_compliance_and_business_environment.md), [14 Artifacts](./14_artifacts_information_and_traceability.md) |
| Business Environment: change control | [04 Integration](./04_integration_scope_requirements_and_change.md), [10 Adaptive & Hybrid](./10_agile_hybrid_and_adaptive_delivery.md) |
| Business Environment: impediments/issues | [08 Risk & Decisions](./08_risk_uncertainty_issues_and_decisions.md), [10 Adaptive & Hybrid](./10_agile_hybrid_and_adaptive_delivery.md) |
| Business Environment: continuous improvement/benefits | [11 Measurement & Closure](./11_measurement_status_closure_and_continuous_improvement.md), [09 Governance](./09_governance_compliance_and_business_environment.md) |
| Business Environment: organizational change/external environment | [09 Governance & Environment](./09_governance_compliance_and_business_environment.md), [12 Modern Context](./12_ai_sustainability_and_modern_project_context.md) |
| AI, sustainability, data-informed decisions | [12 Modern Context](./12_ai_sustainability_and_modern_project_context.md), [11 Measurement](./11_measurement_status_closure_and_continuous_improvement.md) |
| Predictive, adaptive/agile, hybrid across domains | [01 Lifecycle](./01_lifecycle_delivery_approaches_and_tailoring.md), [10 Adaptive & Hybrid](./10_agile_hybrid_and_adaptive_delivery.md), [16 Cases](./16_end_to_end_case_studies.md) |
| Scenario/practicum/application | [13 Scenario Reasoning](./13_pmp_scenario_reasoning_and_exam_strategy.md), [14 Artifacts](./14_artifacts_information_and_traceability.md), [16 Cases](./16_end_to_end_case_studies.md) |

## Mapping với PMBOK Eighth Edition

PMBOK 8 giữ principles/performance domains và mở rộng context về AI, PMO, procurement. Library bao phủ các mental model tương ứng qua value/system thinking, people/stakeholder, integration, schedule/finance, quality/resources/procurement, risk, governance, adaptive delivery, measurement/closure và modern context nhưng không sao chép structure/writing của PMBOK.

Điểm khác biệt có chủ ý là library dùng các **connection layer** làm spine: investment/value (`00`), commitment/learning (`01`), decision/incentive (`02`), influence/information (`03`), state/change propagation (`04`), causal flow (`05`), economic state (`06`), capability/organizational boundary (`07`), uncertainty/resilience (`08`), governance/capital allocation (`09`), adaptive option economics (`10`), sensor/learning (`11`), socio-technical/lifecycle externality (`12`), scenario state machine (`13`), evidence lineage (`14`), quantitative model validity (`15`) và cross-case transfer (`16`).

## Formula và worked-example audit

Các phép tính được giữ vì chúng tạo decision model, không phải vì “PMP thường hỏi công thức”. [Schedule](./05_schedule_estimation_and_flow.md) giải thích CPM/float/PERT/probabilistic forecast và model limits; [Finance](./06_finance_cost_and_value_measurement.md) giải thích EVM/EAC/TCPI/time-value và economic-state assumptions; [Risk](./08_risk_uncertainty_issues_and_decisions.md) giải thích EMV/scenario/Monte Carlo/sensitivity/Value of Information và risk-adjusted decision.

[Quantitative Reasoning](./15_quantitative_reasoning_worked_examples.md) là consolidation layer. Follow-up refinement bổ sung robustness, decision-reversal threshold, model risk, calibration, cross-metric consistency và dimensional sanity để tránh lỗi “arithmetic đúng nhưng decision model sai”. Arithmetic không được xem là đủ nếu model validity, dependency/correlation, sensitivity boundary và interpretation chưa rõ.

## Boundary và duplicate audit

`pmp/raw/` và `pmp/workflow-output/` là provenance, không phải canonical learning docs và không bị sửa.

Software requirements/testing/release/technical debt tiếp tục thuộc canonical `computer_science/09_software_engineering/`; PMP chỉ giữ project-level consequence và cross-link. AI chapter không duplicate machine-learning algorithms/MLOps. Finance không trở thành corporate accounting/treasury/investing textbook. Risk/schedule không trở thành stochastic-operations-research textbook. Procurement claim không thay legal counsel. People/stakeholder không trở thành organizational psychology/HR/labor-law textbook. Sustainability không biến thành ESG reporting framework riêng.

Các depth pass chủ động **không tạo chapter mới**, vì mọi mechanism mới đều có conceptual home rõ trong chapter hiện hữu.

## Readability audit

Canonical docs tiếp tục dùng prose làm hình thức giải thích chính. Table chỉ dùng khi mapping/audit thực sự phù hợp; bullet/list không được dùng thay cho causal explanation.

Mỗi phần ưu tiên problem → mechanism → assumption/boundary → failure mode → evidence → scenario/connection. Các term mới chỉ được dùng khi chúng nén một failure mechanism cụ thể; glossary không bắt buộc chứa mọi chapter-local term nếu term đã được giải thích đầy đủ tại chỗ.

Depth pass audit mọi chapter nhưng không rewrite chapter đã đủ sâu chỉ để đổi wording. Đây là tiêu chí bảo vệ signal-to-noise của library.

## Dependency audit

Learning route vẫn giữ:

```text
value/project system
→ lifecycle/tailoring
→ people/stakeholders
→ integration/scope
→ schedule/finance
→ quality/resources/procurement
→ risk/decision
→ governance/environment
→ adaptive/hybrid
→ measurement/closure
→ AI/sustainability
→ scenario reasoning
→ artifacts/quantitative/cases
```

Deepening không làm thay conceptual route. Nó chỉ làm mỗi node có causal model mạnh hơn và làm connection giữa các node rõ hơn.

README hiện có full conceptual route, scenario route, software-project route, leadership/governance route và last-mile exam consolidation. Không cần thêm competing route.

## Internal-link audit

Toàn bộ 17 chapter trong [README](./README.md) vẫn dùng canonical filename. Links tới [Glossary](./GLOSSARY.md), [Coverage Audit](./COVERAGE_AUDIT.md), [References](./REFERENCES.md), quantitative practice và case studies vẫn nằm trong cùng canonical tree.

Cross-domain links chỉ dùng ở boundary có giá trị thực: Software Engineering cho implementation mechanics và [Investing Knowledge Library](../investing/README.md) cho finance/investment depth ngoài PMP.

`raw/` và `workflow-output/` không được đưa vào learning route.

## Source/provenance audit

`pmp/raw/` và `pmp/workflow-output/` giữ nguyên source role. Depth pass không rewrite source, không biến cleaned source thành canonical chapter và không xóa provenance.

Canonical learning layer vẫn nằm trực tiếp ở `pmp/*.md`: 17 chapter + README + Glossary + References + Coverage Audit.

## Modern-source audit

[References](./REFERENCES.md) tiếp tục tách exam facts khỏi conceptual material và ghi nguồn chính thức PMI cho PMP 2026, PMBOK Eighth Edition, AI Standard và P5 Sustainability Standard.

Tại audit 2026-09-22, exam metadata hiện hành trong library vẫn dùng snapshot đã kiểm chứng: 180 questions, 4 hours, two 10-minute breaks; ECO domains People 33%, Process 41%, Business Environment 26%, cùng predictive/adaptive/hybrid coverage. Các refinement mới không thay đổi current PMI facts nên không cần rewrite References.

AI và sustainability deepening chỉ mở rộng conceptual governance/lifecycle reasoning, không thêm claim mới về current PMI metadata.

## Gap review sau các depth pass

`00` đóng gap về solution-first framing, option preservation, counterfactual benefit attribution, distributed value/harm, temporary-organization transaction cost, transition debt và stop/pivot criteria.

`01` được nâng thêm bằng mixed uncertainty profile, uncertainty migration theo lifecycle, nhiều feedback cadence/synchronization point, decision-flip test và tailoring debt. Delivery approach vì vậy được reasoning từ causal variable thay vì methodology identity.

`02` được nâng từ leadership/team concepts sang decision architecture sâu hơn: authority gradient, escalation friction/shadow authority, nonlinear coordination surface, decision-load capacity, team resilience, recovery debt và cách nối people signal với operational evidence.

`03` được nâng thêm về stakeholder sensing và validity: representation/proxy risk, feedback sampling bias, information half-life, option creation trong negotiation, transfer of reasoning capability và stakeholder decision debt.

`04` được nâng thêm về hidden/concurrent state: assumption dependency graph/assumption debt, concurrent-change collision, compatibility/migration window và integration debt. Integration giờ bao phủ cả current/target/intermediate state thay vì chỉ approved change propagation.

`07` nâng quality từ inspection sang process capability/quality-at-source; resource từ headcount sang effective capacity/queue/learning curve/shared contention; procurement từ contract type sang principal–agent, information asymmetry, risk allocation, supplier health và real exit capability.

`08` nâng risk từ register/response sang epistemic-vs-aleatory uncertainty, velocity/detectability, risk-adjusted value, stress/break point, control effectiveness, risk capacity, resilience/recoverability, crisis triage và cost-of-waiting.

`09` nâng governance từ authority/committee sang decision architecture/debt/queue, sponsor attention, portfolio WIP/incremental funding, strategic drift, compliance-by-design, materiality, exception concentration, benefit dependency và post-rollout reinforcement.

`10` nâng adaptive delivery từ feedback ceremony sang hypothesis→evidence→decision economics, backlog option decay, economic batch size, deploy/release/value state, forecast calibration, decision horizon, technical option value và cadence synchronization.

`11` nâng measurement thành sensor system với measurement-vs-model error, proxy distance, false-alarm trade-offs, metric portfolio, total control latency, aggregation loss, residual-risk transfer at closure, knowledge retrieval và action-effectiveness verification.

`12` nâng AI thành socio-technical operating system với intended-use envelope, automation-level design, oversight failure, data rights/lineage, abuse/misuse, drift taxonomy, semantic observability, incident remediation, concentration/shadow-AI/hidden-human-work; sustainability được nâng bằng materiality, lifecycle boundary, burden shifting và evidence quality.

`15` được nâng thêm từ quantitative interpretation sang quantitative decision robustness: decision-reversal threshold, model risk, calibration, cross-metric consistency và dimensional sanity. Mục tiêu là phát hiện khi con số chính xác nhưng decision mong manh hoặc model boundary sai.

`16` nâng case layer từ collection of examples thành transfer-learning layer qua invariants-vs-context variables, moving bottleneck, changing risk state, local-success/global-failure và decision-quality-vs-outcome-quality.

Các chapter `05–06`, `13–14` vẫn được giữ ở trạng thái hiện tại vì audit chưa tìm thấy missing mechanism đủ lớn để biện minh cho thêm prose. Đây là quyết định giữ signal-to-noise, không phải bỏ qua chúng.

## Tiêu chí cho vòng tiếp theo

Library hiện ở **maintenance + evidence-driven refinement mode**. Chỉ tiếp tục deepening khi có một trong các signal: practice exam lặp lại cùng reasoning failure; real project case lộ missing mechanism; internal link/path thay đổi; PMI exam/standard fact stale; hoặc một concept hiện chỉ có statement mà chưa có causal explanation.

Không dùng line count làm target. Không tạo chapter mới cho framework/tool mới nếu nó không tạo conceptual boundary mới. Khi có gap, ưu tiên mở rộng canonical chapter hiện tại và kiểm tra connection với các chapter khác trước khi tạo artifact mới.

Mental model cuối cho audit:

> Coverage tạo node; depth tạo causal model; dependency nối node; scenario/case kiểm tra transfer. Mục tiêu cuối không phải nhớ nhiều PMP hơn mà là nhìn được project như một system của value, people, evidence, uncertainty, authority và feedback—rồi đổi decision đúng khi context thay đổi.
