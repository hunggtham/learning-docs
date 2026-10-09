# PMP thư viện kiến thức (knowledge library / 지식 라이브러리)

Edition, exam boundary và phân biệt PMI standard với nội dung tự biên soạn được ghi trong [source ledger](./SOURCES.md).

> **Mạch đọc:** README này là owner của **PMP thư viện kiến thức (knowledge library / 지식 라이브러리)**. Route đi từ mental model quản lý dự án → people, process và business environment → chapters theo lifecycle, uncertainty, value và governance → case/lab → references và cập nhật, để học PMP bằng lập luận thay vì mẹo đáp án.

Thư viện này xây dựng một mô hình tư duy đầy đủ về quản lý dự án (project management / 프로젝트 관리) và đồng thời hỗ trợ chuẩn bị cho PMP®. Mục tiêu không phải ghi nhớ một danh sách tiến trình (process / 프로세스), đầu vào (input / 입력)/đầu ra (output / 출력) hay “mẹo chọn đáp án”, mà là hiểu vì sao một dự án cần được quản lý, tín hiệu nào cho thấy hệ thống đang lệch hướng, và người quản lý dự án phải lập luận (reasoning / 추론) như thế nào khi con người, giá trị, thời gian, tiền, rủi ro và bối cảnh kinh doanh cùng thay đổi.

`pmp/raw/` và `pmp/workflow-output/` là lớp nguồn/provenance đã có trong repository. Chúng không phải chuẩn gốc (canonical / 정본) lộ trình học (learning path / 학습 경로) của thư viện này và không bị sửa. Các chapter ở ngay `pmp/` là lớp chuẩn gốc (canonical / 정본) để đọc trên website.

## Bản chất của PMP trong thư viện này

PMP không được trình bày như một “bộ quy trình cố định”. Một dự án là một hệ thống tạm thời dùng nguồn lực hữu hạn để tạo ra một kết quả mới trong điều kiện bất định. Vì vậy quản lý dự án là việc liên tục kết nối năm câu hỏi: ta đang cố tạo giá trị gì, ai cần cùng tham gia, cách giao hàng nào phù hợp với mức độ bất định, ràng buộc (constraint / 제약조건) nào phải được bảo vệ, và bằng chứng (evidence / 증거) nào cho biết ta nên tiếp tục hay điều chỉnh.

PMI hiện phân biệt rõ giữa Exam Content Outline (ECO) và PMBOK® Guide. ECO mô tả công việc thực tế được kiểm tra trong kỳ thi; PMBOK cung cấp kiến thức (knowledge / 지식)/principles/practices rộng hơn. Thư viện vì vậy không dùng thứ tự chương của PMBOK hay thứ tự tác vụ (task / 작업) của ECO làm phụ thuộc (dependency / 의존성) chính.

Từ kỳ thi cập nhật tháng 7/2026, PMP có ba exam lĩnh vực (domain / 도메인): People 33%, tiến trình (process / 프로세스) 41% và nghiệp vụ (business / 비즈니스) môi trường (environment / 환경) 26%. Predictive chiếm khoảng 40% câu hỏi, phần còn lại được chia giữa adaptive/agile và hybrid. Cấu trúc này chỉ là coverage map; nó không có nghĩa ba lĩnh vực (domain / 도메인) hoạt động độc lập trong dự án thực tế.

Exam 2026 cũng dùng item format gần dự án (project / 프로젝트) công việc (work / 작업) hơn, gồm scenario/trường hợp (case / 사례), multiple-response, drag-and-drop và practicum dựa trên tools, dữ liệu (data / 데이터), dashboard hoặc dự án (project / 프로젝트) sản phẩm tạo ra (artifact / 산출물). Vì vậy tầng (layer / 계층) consolidation của thư viện (library / 라이브러리) không chỉ luyện “đọc câu hỏi chữ”, mà còn luyện cách giữ trạng thái (state / 상태) mô hình (model / 모델), đọc bằng chứng (evidence / 증거) và ra quyết định (decision / 결정) xuyên nhiều sản phẩm tạo ra (artifact / 산출물).

> **Nối mạch:** Bản chất của PMP xác định mental model và owner; **Học tập phụ thuộc** biến chúng thành prerequisite. **Reading routes theo mục tiêu** chọn đường học phù hợp với nhu cầu.

## Học tập (learning / 학습) phụ thuộc (dependency / 의존성)

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

Có thể đọc liên tục theo thứ tự dưới đây. Mỗi chapter vẫn giải thích đủ ngữ cảnh (context / 맥락) để có thể bắt đầu tại đó, nhưng phụ thuộc (dependency / 의존성) map giúp giảm số khái niệm phải giữ trong đầu cùng lúc.

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

Các chapter 00–12 xây mô hình tư duy (mental model / 사고 모델) theo phụ thuộc (dependency / 의존성). Chapter 13–16 là lớp consolidation: lập luận (reasoning / 추론) với scenario/sản phẩm tạo ra (artifact / 산출물), nhìn dự án (project / 프로젝트) thông tin (information / 정보) như một hệ thống (system / 시스템), luyện quantitative lập luận (reasoning / 추론) cùng giả định (assumption / 가정) và nối nhiều lĩnh vực (domain / 도메인) trong các trường hợp (case / 사례) hoàn chỉnh.

> **Nối mạch:** Reading routes theo mục tiêu sắp xếp nội dung theo nhu cầu; **Kết nối với thư viện khác** mở rộng bối cảnh nhưng giữ owner và ranh giới của PMP.

## Reading routes theo mục tiêu

### Tuyến (route / 경로) A — Học PMP như một hệ thống kiến thức

Đây là tuyến (route / 경로) mặc định: đọc `00 → 16` theo thứ tự. tuyến (route / 경로) này phù hợp nếu muốn xây nền dự án (project / 프로젝트) management lâu dài thay vì chỉ chuẩn bị exam. Các concept về giá trị (value / 값), people, quản trị (governance / 거버넌스) và bất định (uncertainty / 불확실성) được học trước khi đi vào scenario và formula, nên ít phải nhớ máy móc.

### Tuyến (route / 경로) B — Luyện scenario sau khi đã có cốt lõi (core / 핵심) foundation

Nếu đã học qua các chapter cốt lõi (core / 핵심) và muốn tập trung quyết định (decision / 결정) chất lượng (quality / 품질), bắt đầu ở [Scenario Reasoning](./13_pmp_scenario_reasoning_and_exam_strategy.md), sau đó đọc [Artifacts & Traceability](./14_artifacts_information_and_traceability.md), [Quantitative Reasoning](./15_quantitative_reasoning_worked_examples.md) và [End-to-End Cases](./16_end_to_end_case_studies.md).

Tuyến (route / 경로) này đặc biệt phù hợp với exam 2026 vì chapter 13 không chỉ xử lý văn bản (text / 텍스트) scenario mà còn dashboard/dữ liệu (data / 데이터)/sản phẩm tạo ra (artifact / 산출물)/case-study lập luận (reasoning / 추론). Khi một scenario lộ gap về lĩnh vực (domain / 도메인) nào, quay lại chapter chuẩn gốc (canonical / 정본) tương ứng thay vì học answer mẫu (pattern / 패턴).

### Tuyến (route / 경로) C — dự án (project / 프로젝트) phần mềm và hệ thống số

Đọc [Foundations](./00_foundations_value_and_project_system.md) → [Lifecycle & Tailoring](./01_lifecycle_delivery_approaches_and_tailoring.md) → [Stakeholders](./03_stakeholders_communication_and_knowledge.md) → [Integration & Scope](./04_integration_scope_requirements_and_change.md) → [Quality/Resources/Procurement](./07_quality_resources_and_procurement.md) → [Risk](./08_risk_uncertainty_issues_and_decisions.md) → [Adaptive & Hybrid](./10_agile_hybrid_and_adaptive_delivery.md) → [Measurement & Closure](./11_measurement_status_closure_and_continuous_improvement.md) → [AI & Sustainability](./12_ai_sustainability_and_modern_project_context.md) → [Cases](./16_end_to_end_case_studies.md).

Tuyến (route / 경로) này intentionally không duplicate software-engineering mechanics. Khi cần kỹ thuật sâu, đi qua nội bộ (internal / 내부) links sang chuẩn gốc (canonical / 정본) Khoa học máy tính (computer science / 컴퓨터 과학) docs.

### Tuyến (route / 경로) D — Leadership, quản trị (governance / 거버넌스) và nghiệp vụ (business / 비즈니스) quyết định (decision / 결정)

Đọc [Foundations](./00_foundations_value_and_project_system.md) → [People](./02_people_leadership_team_and_conflict.md) → [Stakeholders](./03_stakeholders_communication_and_knowledge.md) → [Finance & Value](./06_finance_cost_and_value_measurement.md) → [Risk & Decisions](./08_risk_uncertainty_issues_and_decisions.md) → [Governance](./09_governance_compliance_and_business_environment.md) → [Measurement & Benefits](./11_measurement_status_closure_and_continuous_improvement.md) → [Cases](./16_end_to_end_case_studies.md).

Tuyến (route / 경로) này phù hợp khi mục tiêu là nâng khả năng quản trị dự án (project / 프로젝트) thực tế hơn là học công cụ (tool / 도구)/tiến trình (process / 프로세스) riêng lẻ.

### Tuyến (route / 경로) E — Last-mile exam consolidation

Tuyến (route / 경로) này dùng khi foundation đã tương đối vững và muốn chuyển từ “biết concept” sang “ra quyết định (decision / 결정) dưới thời gian (time / 시간) pressure”. Đọc [Scenario Reasoning](./13_pmp_scenario_reasoning_and_exam_strategy.md) để dùng eight-step khung phần mềm (framework / 프레임워크) + five-gate option filter; đọc [Artifacts](./14_artifacts_information_and_traceability.md) để biết sản phẩm tạo ra (artifact / 산출물) nào là authoritative bằng chứng (evidence / 증거); luyện [Quantitative Reasoning](./15_quantitative_reasoning_worked_examples.md); sau đó làm [End-to-End Cases](./16_end_to_end_case_studies.md) theo 5 pass: tự lập luận (reasoning / 추론), dấu vết (trace / 추적) về chapter, counterfactual, sản phẩm tạo ra (artifact / 산출물) injection và explain rejected alternative.

Nếu lỗi (error / 오류) log cho thấy cùng một lớp (class / 클래스) of lập luận (reasoning / 추론) thất bại (failure / 실패) lặp lại, dừng làm thêm câu và quay lại đúng chapter cơ chế (mechanism / 메커니즘). Chỉ khi cơ chế (mechanism / 메커니즘) đã rõ mới tăng volume/thời gian (time / 시간) pressure.

Khi gặp thuật ngữ chưa quen, xem [Glossary](./GLOSSARY.md). Coverage đối với PMP 2026, PMBOK 8 và các ranh giới (boundary / 경계) với lĩnh vực (domain / 도메인) khác được theo dõi ở [Coverage & Depth Audit](./COVERAGE_AUDIT.md). Nguồn chuẩn và thời điểm kiểm chứng nằm ở [References](./REFERENCES.md).

> **Nối mạch:** Sau khi biết route và thư viện liên quan, Cách sử dụng khi học PMP chỉ cách chọn file, ghi bằng chứng và quay về route khi phát hiện gap.

## Kết nối với thư viện kiến thức (knowledge library / 지식 라이브러리) khác

PMP nhìn requirements, chất lượng (quality / 품질), delivery và thay đổi (change / 변경) ở cấp dự án; Khoa học máy tính (computer science / 컴퓨터 과학) nhìn chúng ở cấp hệ thống phần mềm. Vì vậy thư viện này chỉ giải thích đủ mô hình tư duy (mental model / 사고 모델) để quản lý dự án, sau đó cross-link tới chuẩn gốc (canonical / 정본) Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학) khi cần cơ chế kỹ thuật sâu hơn. yêu cầu (requirement / 요구사항) có thể đọc tiếp ở [Requirements Engineering](../computer_science/09_software_engineering/00_requirements_specification_and_engineering_process.md), chất lượng (quality / 품질) ở [Testing & Verification](../computer_science/09_software_engineering/02_testing_quality_and_verification_strategy.md), delivery ở [Delivery & Operations](../computer_science/09_software_engineering/03_delivery_configuration_and_operations.md), và technical debt/evolution ở [Maintenance & Evolution](../computer_science/09_software_engineering/04_maintenance_evolution_and_technical_debt.md).

PMP chỉ dùng finance ở mức dự án (project / 프로젝트)/business-case quyết định (decision / 결정). Nếu cần đi sâu hơn vào financial hệ thống (system / 시스템), asset pricing, company phân tích (analysis / 분석), portfolio hoặc macroeconomics, chuyển sang [Investing Knowledge Library](../investing/README.md) thay vì kéo các chapter PMP vượt conceptual ranh giới (boundary / 경계).

> **Nối mạch:** Cách sử dụng khi học PMP khép README bằng vòng lặp chọn owner → học prerequisite → kiểm tra case → cập nhật gap; tài liệu vì vậy không bị biến thành danh sách thuật ngữ.

## Cách sử dụng khi học PMP

Sau khi hiểu một chapter, không nên chỉ hỏi “định nghĩa là gì?” mà nên tự đặt tình huống: dấu hiệu nào đang có, nguyên nhân gốc (root cause / 근본 원인) có thể là gì, ràng buộc (constraint / 제약조건) nào không được phá, ai có quyền quyết định, hành động tiếp theo nào tạo thêm bằng chứng (evidence / 증거) với chi phí thấp nhất. Đây cũng là cách các câu hỏi scenario-based kiểm tra khả năng áp dụng thay vì khả năng nhớ tên sản phẩm tạo ra (artifact / 산출물).

Khi luyện formula, hãy viết meaning của quantity trước arithmetic. Khi luyện scenario, hãy đổi một biến như delivery approach, authority, compliance ranh giới (boundary / 경계) hoặc reversibility rồi kiểm tra xem next hành động (action / 동작) có thay đổi không. Với dashboard/sản phẩm tạo ra (artifact / 산출물), đọc quyết định (decision / 결정) ask trước rồi mới tìm chỉ số (metric / 지표)/bằng chứng (evidence / 증거) liên quan. Nếu answer không thay đổi khi ngữ cảnh (context / 맥락) thay đổi đáng kể, có khả năng bạn đang pattern-match thay vì lập luận (reasoning / 추론).

Một study vòng lặp (loop / 루프) tốt là:

```text
chapter mechanism
→ scenario/artifact/case
→ decision
→ feedback/error log
→ identify reasoning failure
→ revisit đúng concept
→ new variant
```

Thư viện (library / 라이브러리) được xem là hoàn thành khi vòng lặp này giúp người đọc tự sửa lập luận (reasoning / 추론), không phải khi mọi tệp (file / 파일) dài bằng nhau.

> **Bàn giao:** Sau **Cách sử dụng khi học PMP**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
