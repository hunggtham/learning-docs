# PMP Knowledge Library

Thư viện này xây dựng một mô hình tư duy đầy đủ về quản lý dự án (project management / 프로젝트 관리) và đồng thời hỗ trợ chuẩn bị cho PMP®. Mục tiêu không phải ghi nhớ một danh sách process, input/output hay “mẹo chọn đáp án”, mà là hiểu vì sao một dự án cần được quản lý, tín hiệu nào cho thấy hệ thống đang lệch hướng, và người quản lý dự án phải reasoning như thế nào khi con người, giá trị, thời gian, tiền, rủi ro và bối cảnh kinh doanh cùng thay đổi.

`pmp/raw/` và `pmp/workflow-output/` là lớp nguồn/provenance đã có trong repository. Chúng không phải canonical learning path của thư viện này và không bị sửa. Các chapter ở ngay `pmp/` là lớp canonical để đọc trên website.

## Bản chất của PMP trong thư viện này

PMP không được trình bày như một “bộ quy trình cố định”. Một dự án là một hệ thống tạm thời dùng nguồn lực hữu hạn để tạo ra một kết quả mới trong điều kiện bất định. Vì vậy quản lý dự án là việc liên tục kết nối năm câu hỏi: ta đang cố tạo giá trị gì, ai cần cùng tham gia, cách giao hàng nào phù hợp với mức độ bất định, constraint nào phải được bảo vệ, và evidence nào cho biết ta nên tiếp tục hay điều chỉnh.

PMI hiện phân biệt rõ giữa Exam Content Outline (ECO) và PMBOK® Guide. ECO mô tả công việc thực tế được kiểm tra trong kỳ thi; PMBOK cung cấp knowledge/principles/practices rộng hơn. Thư viện vì vậy không dùng thứ tự chương của PMBOK hay thứ tự task của ECO làm dependency chính.

Từ kỳ thi cập nhật tháng 7/2026, PMP có ba exam domain: People 33%, Process 41% và Business Environment 26%. Predictive chiếm khoảng 40% câu hỏi, phần còn lại được chia giữa adaptive/agile và hybrid. Cấu trúc này chỉ là coverage map; nó không có nghĩa ba domain hoạt động độc lập trong dự án thực tế.

Exam 2026 cũng dùng item format gần project work hơn, gồm scenario/case, multiple-response, drag-and-drop và practicum dựa trên tools, data, dashboard hoặc project artifact. Vì vậy layer consolidation của library không chỉ luyện “đọc câu hỏi chữ”, mà còn luyện cách giữ state model, đọc evidence và ra decision xuyên nhiều artifact.

## Learning dependency

```text
project vs operations / outcome / value
        ↓
lifecycle / delivery approach / tailoring
        ↓
people / team / stakeholder / communication
        ↓
integrated planning / scope / schedule / finance
        ↓
quality / resources / procurement
        ↓
risk / issue / uncertainty / decision
        ↓
governance / compliance / business environment
        ↓
adaptive & hybrid delivery
        ↓
measurement / closure / organizational learning
        ↓
AI / sustainability / modern context
        ↓
scenario reasoning
        ↓
artifacts / quantitative practice / end-to-end cases
```

Có thể đọc liên tục theo thứ tự dưới đây. Mỗi chapter vẫn giải thích đủ context để có thể bắt đầu tại đó, nhưng dependency map giúp giảm số khái niệm phải giữ trong đầu cùng lúc.

1. [Nền tảng: project, outcome, value và hệ thống tạo giá trị](./00_foundations_value_and_project_system.md)
2. [Vòng đời, delivery approach và tailoring](./01_lifecycle_delivery_approaches_and_tailoring.md)
3. [People: leadership, team, conflict và empowerment](./02_people_leadership_team_and_conflict.md)
4. [Stakeholder, communication và knowledge transfer](./03_stakeholders_communication_and_knowledge.md)
5. [Integration, scope, requirements và change](./04_integration_scope_requirements_and_change.md)
6. [Schedule, estimation, dependency và flow](./05_schedule_estimation_and_flow.md)
7. [Finance, cost, reserves và value measurement](./06_finance_cost_and_value_measurement.md)
8. [Quality, resources và procurement](./07_quality_resources_and_procurement.md)
9. [Risk, uncertainty, issue và decision making](./08_risk_uncertainty_issues_and_decisions.md)
10. [Governance, compliance và business environment](./09_governance_compliance_and_business_environment.md)
11. [Agile, adaptive và hybrid delivery](./10_agile_hybrid_and_adaptive_delivery.md)
12. [Measurement, status, closure và continuous improvement](./11_measurement_status_closure_and_continuous_improvement.md)
13. [AI, sustainability và bối cảnh dự án hiện đại](./12_ai_sustainability_and_modern_project_context.md)
14. [Scenario reasoning và chiến lược làm PMP](./13_pmp_scenario_reasoning_and_exam_strategy.md)
15. [Artifacts, information flow và traceability](./14_artifacts_information_and_traceability.md)
16. [Quantitative reasoning: bài toán và lời giải đủ bước](./15_quantitative_reasoning_worked_examples.md)
17. [End-to-end case studies: predictive, adaptive và hybrid](./16_end_to_end_case_studies.md)

Các chapter 00–12 xây mental model theo dependency. Chapter 13–16 là lớp consolidation: reasoning với scenario/artifact, nhìn project information như một system, luyện quantitative reasoning cùng assumption và nối nhiều domain trong các case hoàn chỉnh.

## Reading routes theo mục tiêu

### Route A — Học PMP như một hệ thống kiến thức

Đây là route mặc định: đọc `00 → 16` theo thứ tự. Route này phù hợp nếu muốn xây nền project management lâu dài thay vì chỉ chuẩn bị exam. Các concept về value, people, governance và uncertainty được học trước khi đi vào scenario và formula, nên ít phải nhớ máy móc.

### Route B — Luyện scenario sau khi đã có core foundation

Nếu đã học qua các chapter core và muốn tập trung decision quality, bắt đầu ở [Scenario Reasoning](./13_pmp_scenario_reasoning_and_exam_strategy.md), sau đó đọc [Artifacts & Traceability](./14_artifacts_information_and_traceability.md), [Quantitative Reasoning](./15_quantitative_reasoning_worked_examples.md) và [End-to-End Cases](./16_end_to_end_case_studies.md).

Route này đặc biệt phù hợp với exam 2026 vì chapter 13 không chỉ xử lý text scenario mà còn dashboard/data/artifact/case-study reasoning. Khi một scenario lộ gap về domain nào, quay lại chapter canonical tương ứng thay vì học answer pattern.

### Route C — Project phần mềm và hệ thống số

Đọc [Foundations](./00_foundations_value_and_project_system.md) → [Lifecycle & Tailoring](./01_lifecycle_delivery_approaches_and_tailoring.md) → [Stakeholders](./03_stakeholders_communication_and_knowledge.md) → [Integration & Scope](./04_integration_scope_requirements_and_change.md) → [Quality/Resources/Procurement](./07_quality_resources_and_procurement.md) → [Risk](./08_risk_uncertainty_issues_and_decisions.md) → [Adaptive & Hybrid](./10_agile_hybrid_and_adaptive_delivery.md) → [Measurement & Closure](./11_measurement_status_closure_and_continuous_improvement.md) → [AI & Sustainability](./12_ai_sustainability_and_modern_project_context.md) → [Cases](./16_end_to_end_case_studies.md).

Route này intentionally không duplicate software-engineering mechanics. Khi cần kỹ thuật sâu, đi qua internal links sang canonical Computer Science docs.

### Route D — Leadership, governance và business decision

Đọc [Foundations](./00_foundations_value_and_project_system.md) → [People](./02_people_leadership_team_and_conflict.md) → [Stakeholders](./03_stakeholders_communication_and_knowledge.md) → [Finance & Value](./06_finance_cost_and_value_measurement.md) → [Risk & Decisions](./08_risk_uncertainty_issues_and_decisions.md) → [Governance](./09_governance_compliance_and_business_environment.md) → [Measurement & Benefits](./11_measurement_status_closure_and_continuous_improvement.md) → [Cases](./16_end_to_end_case_studies.md).

Route này phù hợp khi mục tiêu là nâng khả năng quản trị project thực tế hơn là học tool/process riêng lẻ.

### Route E — Last-mile exam consolidation

Route này dùng khi foundation đã tương đối vững và muốn chuyển từ “biết concept” sang “ra decision dưới time pressure”. Đọc [Scenario Reasoning](./13_pmp_scenario_reasoning_and_exam_strategy.md) để dùng eight-step framework + five-gate option filter; đọc [Artifacts](./14_artifacts_information_and_traceability.md) để biết artifact nào là authoritative evidence; luyện [Quantitative Reasoning](./15_quantitative_reasoning_worked_examples.md); sau đó làm [End-to-End Cases](./16_end_to_end_case_studies.md) theo 5 pass: tự reasoning, trace về chapter, counterfactual, artifact injection và explain rejected alternative.

Nếu error log cho thấy cùng một class of reasoning failure lặp lại, dừng làm thêm câu và quay lại đúng chapter mechanism. Chỉ khi mechanism đã rõ mới tăng volume/time pressure.

Khi gặp thuật ngữ chưa quen, xem [Glossary](./GLOSSARY.md). Coverage đối với PMP 2026, PMBOK 8 và các boundary với domain khác được theo dõi ở [Coverage & Depth Audit](./COVERAGE_AUDIT.md). Nguồn chuẩn và thời điểm kiểm chứng nằm ở [References](./REFERENCES.md).

## Kết nối với Knowledge Library khác

PMP nhìn requirements, quality, delivery và change ở cấp dự án; Computer Science nhìn chúng ở cấp hệ thống phần mềm. Vì vậy thư viện này chỉ giải thích đủ mental model để quản lý dự án, sau đó cross-link tới canonical Software Engineering khi cần cơ chế kỹ thuật sâu hơn. Requirement có thể đọc tiếp ở [Requirements Engineering](../computer_science/09_software_engineering/00_requirements_specification_and_engineering_process.md), quality ở [Testing & Verification](../computer_science/09_software_engineering/02_testing_quality_and_verification_strategy.md), delivery ở [Delivery & Operations](../computer_science/09_software_engineering/03_delivery_configuration_and_operations.md), và technical debt/evolution ở [Maintenance & Evolution](../computer_science/09_software_engineering/04_maintenance_evolution_and_technical_debt.md).

PMP chỉ dùng finance ở mức project/business-case decision. Nếu cần đi sâu hơn vào financial system, asset pricing, company analysis, portfolio hoặc macroeconomics, chuyển sang [Investing Knowledge Library](../investing/README.md) thay vì kéo các chapter PMP vượt conceptual boundary.

## Cách sử dụng khi học PMP

Sau khi hiểu một chapter, không nên chỉ hỏi “định nghĩa là gì?” mà nên tự đặt tình huống: dấu hiệu nào đang có, root cause có thể là gì, constraint nào không được phá, ai có quyền quyết định, hành động tiếp theo nào tạo thêm evidence với chi phí thấp nhất. Đây cũng là cách các câu hỏi scenario-based kiểm tra khả năng áp dụng thay vì khả năng nhớ tên artifact.

Khi luyện formula, hãy viết meaning của quantity trước arithmetic. Khi luyện scenario, hãy đổi một biến như delivery approach, authority, compliance boundary hoặc reversibility rồi kiểm tra xem next action có thay đổi không. Với dashboard/artifact, đọc decision ask trước rồi mới tìm metric/evidence liên quan. Nếu answer không thay đổi khi context thay đổi đáng kể, có khả năng bạn đang pattern-match thay vì reasoning.

Một study loop tốt là:

```text
chapter mechanism
→ scenario/artifact/case
→ decision
→ feedback/error log
→ identify reasoning failure
→ revisit đúng concept
→ new variant
```

Library được xem là hoàn thành khi vòng lặp này giúp người đọc tự sửa reasoning, không phải khi mọi file dài bằng nhau.