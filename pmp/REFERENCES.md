# PMP Knowledge Library — References

## Phạm vi và thời điểm kiểm chứng

Các thông tin certification/exam có thể thay đổi. Những chi tiết hiện hành trong thư viện này được kiểm chứng lại ngày 2026-09-22 từ nguồn chính thức của Project Management Institute (PMI). Khi dùng thư viện ở thời điểm xa hơn, ưu tiên kiểm tra lại PMI trước khi dựa vào số câu, thời lượng, eligibility, training requirement, item format hoặc exam weighting.

Library cố ý tách `exam fact` khỏi `project-management mental model`. Những thứ như weighting, thời lượng hay eligibility có thể thay đổi theo policy; các mental model như value, uncertainty, governance, feedback hay decision rights bền hơn và không nên bị học như metadata của một exam version.

## Nguồn chuẩn chính

### PMP Certification Exam Content Outline — July 2026

https://www.pmi.org/-/media/pmi/documents/public/pdf/certifications/new-pmp-examination-content-outline-2026.pdf

Đây là exam map chính cho domain, task, enabler và approach mix. ECO 2026 nêu People 33%, Process 41%, Business Environment 26%; khoảng 40% item là predictive và phần còn lại được chia giữa adaptive/agile và hybrid.

ECO cũng nói rõ các delivery approach xuất hiện xuyên cả ba domain thay vì bị cô lập thành một phần “Agile riêng”. Đây là lý do library tổ chức predictive/adaptive/hybrid như delivery logic xuyên scope, people, governance, risk và business environment.

ECO July 2026 còn mô tả exam gồm 180 câu, trong đó 170 câu được chấm và 10 câu pretest không tính điểm. Item format có thể gồm single-response, multiple-response, drag-and-drop và practicum/hands-on testing với tools, data hoặc case-study questions. Đây là lý do chapter scenario không chỉ luyện paragraph text mà còn luyện dashboard, artifact, data interpretation và state model xuyên case.

ECO mô tả hai break 10 phút: break đầu sau case-study section, break thứ hai khoảng giữa phần independent questions. Sau khi review section và bắt đầu break, candidate không quay lại section trước. Cấu trúc section/break là exam logistics và phải re-check gần ngày thi.

### PMP Certification

https://www.pmi.org/certifications/project-management-pmp

Nguồn hiện hành cho exam logistics, eligibility và application path. Tại thời điểm audit ngày 2026-09-22, PMI công bố 180 questions, 4 hours và hai break 10 phút.

Exam logistics là fact cần re-check gần ngày thi. Không dùng một bản note cũ để suy ra số câu/thời lượng nếu PMI page đã thay đổi.

### PMP 2026 Exam Update

https://www.pmi.org/certifications/project-management-pmp/new-exam

Nguồn giải thích các thay đổi của kỳ thi ra mắt tháng 7/2026, gồm emphasis mới về outcomes/value, business impact, AI, sustainability và stakeholder engagement.

PMI cũng mô tả exam experience mới gần project work hơn, gồm case/scenario, graphic-based question và practical content dựa trên dashboard, project artifact, tools và data. Library phản ánh hướng này bằng cách coi artifact interpretation là một phần của decision reasoning, không phải một mẹo item-format riêng.

Trang này cũng thông báo một thay đổi tương lai đối với eligibility của live training có hiệu lực từ **2026-12-01**. Vì ngày audit hiện tại là 2026-09-22, đây là future policy change chứ chưa phải điều kiện đang áp dụng hôm nay. Khi chuẩn bị application sau ngày đó, cần kiểm tra lại trực tiếp PMI thay vì suy luận từ note này.

### PMBOK® Guide — Eighth Edition

https://www.pmi.org/standards/pmbok

PMBOK Eighth Edition được PMI phát hành tháng 11/2025. PMI mô tả edition này với sáu core principles, bảy performance domains, expanded AI/PMO/procurement và process guidance theo hướng non-prescriptive hơn.

PMI hiện mô tả bảy performance domains quanh governance, scope, schedule, finance, stakeholders, resources và risk. Library không sao chép cấu trúc đó; nó dùng chúng như coverage context rồi tổ chức lại theo conceptual dependency và system reasoning.

### The Standard for Artificial Intelligence in Portfolio, Program, and Project Management

https://www.pmi.org/standards/artificial-intelligence

PMI phát hành standard này tháng 6/2026. Tại thời điểm audit, PMI mô tả standard gồm tám guiding principles và năm performance domains, cùng guidance về human-in-the-loop, ethical/legal guardrails, lifecycle, tailoring và AI use cases trong portfolio/program/project work.

Library dùng nguồn này để củng cố mental model về risk-tiering, accountability, human oversight, configuration/change governance, vendor dependency và responsible adoption; không biến chapter PMP thành tài liệu kỹ thuật machine learning riêng.

Press release phát hành standard:

https://www.pmi.org/about/press-media/2026/pmi-publishes-worlds-first-global-standard-for-ai-in-project-work

### PMI® GPM® P5™ Standard for Sustainable Project Management — Version 4.0

https://www.pmi.org/standards/gpm-p5-standard-for-sustainability-in-project-management

Ấn bản công bố ngày 2026-04-22 mở rộng sustainability theo environmental, social và economic impact, đồng thời nhấn mạnh lifecycle governance, impact threshold, measurable outcome, value chain và alignment với PMBOK Eighth Edition.

Library diễn giải các idea này bằng lens Planet–People–Prosperity, lifecycle impact, externality và threshold/escalation. Đây là mental model để reasoning; nếu cần áp dụng chính thức P5 scoring/template, phải đọc standard/template gốc thay vì dựa vào bản tóm lược ở đây.

### PMP Exam Prep — reference list

https://www.pmi.org/certifications/project-management-pmp/pmp-exam-prep

PMI lưu ý PMP exam không được xây từ một cuốn sách duy nhất; reference list là các nguồn được question writers trích dẫn thường xuyên. Điều này là lý do Knowledge Library tổ chức theo conceptual dependency và ECO thay vì cố “chép PMBOK thành syllabus”.

## Source nội bộ repository

`./raw/` và `./workflow-output/` là provenance đã tồn tại trước Knowledge Library này. Chúng được giữ nguyên, không coi là nguồn chuẩn cho thông tin exam 2026 nếu nội dung cũ hơn.

Các canonical cross-domain docs được tái sử dụng:

- `../computer_science/09_software_engineering/00_requirements_specification_and_engineering_process.md`
- `../computer_science/09_software_engineering/02_testing_quality_and_verification_strategy.md`
- `../computer_science/09_software_engineering/03_delivery_configuration_and_operations.md`
- `../computer_science/09_software_engineering/04_maintenance_evolution_and_technical_debt.md`

Finance sâu hơn về valuation, markets và portfolio investing thuộc `../investing/`; PMP chỉ giữ mức financial reasoning cần cho project/investment decision.

## Nguyên tắc sử dụng nguồn

Library diễn giải bằng ngôn ngữ riêng và tập trung vào mental model. Không sao chép chapter text, task/enabler list hoặc bảng từ tài liệu PMI.

Khi cần exam-specific fact, xem ECO/certification page hiện hành. Khi cần standards context, xem PMBOK/AI/P5 official source. Khi cần technical software depth, theo internal link tới canonical Computer Science docs.

Mọi source có version/date nên được đọc như một snapshot. Một link vẫn tồn tại không chứng minh chi tiết trong note còn current; vì vậy future audit phải kiểm tra cả publication date, effective date và content hiện hành.