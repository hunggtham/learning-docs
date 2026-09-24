---
catalog_version: 1
last_reviewed: 2026-09-24
source_of_truth: main
review_policy: Update this catalog when a canonical library is added, removed, renamed, or changes domain.
domains:
  - id: mathematics
    title: Mathematics
    group: Science
    path: mathematics/
    entrypoint: mathematics/README.md
    status: canonical
    last_reviewed: 2026-09-23
    scope: First-principles mathematics from foundations through analysis, probability, optimization, and connections.
    prerequisites: []
    related: [physics, computer_science, investing]
  - id: physics
    title: Physics
    group: Science
    path: physics/
    entrypoint: physics/README.md
    status: canonical
    last_reviewed: 2026-09-23
    scope: Physics from measurement and mechanics through electromagnetism, quantum theory, matter, and astrophysics.
    prerequisites: [mathematics]
    related: [chemistry, electrical_engineering, computer_science, biology]
  - id: electrical_engineering
    title: Electrical Engineering
    group: Engineering
    path: electrical_engineering/
    entrypoint: electrical_engineering/README.md
    status: canonical
    last_reviewed: 2026-09-23
    scope: Circuits, analog and digital electronics, signals, communications, control, embedded systems, power electronics, and hardware–software interfaces.
    prerequisites: [mathematics, physics]
    related: [computer_science, native, devops_platform_engineering]
  - id: chemistry
    title: Chemistry
    group: Science
    path: chemistry/
    entrypoint: chemistry/README.md
    status: canonical
    last_reviewed: 2026-09-23
    scope: Matter, atomic structure, bonding, reactions, thermodynamics, kinetics, equilibrium, materials, and laboratory reasoning.
    prerequisites: [mathematics, physics]
    related: [biology, physics]
  - id: biology
    title: Biology
    group: Science
    path: biology/
    entrypoint: biology/README.md
    status: canonical
    last_reviewed: 2026-09-23
    scope: Life from chemistry and cells through genetics, evolution, physiology, ecology, biotechnology, and systems biology.
    prerequisites: [chemistry]
    related: [psychology, chemistry, computer_science]
  - id: philosophy
    title: Philosophy
    group: Human & Society
    path: philosophy/
    entrypoint: philosophy/README.md
    status: canonical
    last_reviewed: 2026-09-23
    scope: Philosophical reasoning, epistemology, metaphysics, philosophy of science, philosophy of mind, ethics, social-political philosophy, technology, history, and cross-domain connections.
    prerequisites: []
    related: [mathematics, physics, biology, psychology, computer_science, research_methods]
  - id: research_methods
    title: Research Methods
    group: Methods
    path: research_methods/
    entrypoint: research_methods/README.md
    status: canonical
    last_reviewed: 2026-09-24
    scope: Research questions and design, measurement and sampling, survey design, qualitative methods, systematic review and evidence synthesis, mixed methods, ethics, reproducibility, and open science.
    prerequisites: []
    related: [philosophy, mathematics, economics, psychology, world_history, computer_science]

  - id: computer_science
    title: Computer Science
    group: Computing
    path: computer_science/
    entrypoint: computer_science/README.md
    status: canonical
    last_reviewed: 2026-09-23
    scope: Computing foundations, algorithms, systems, AI, databases, networks, security, software engineering, and professional connections.
    prerequisites: [mathematics]
    related: [electrical_engineering, data_engineering, devops_platform_engineering, backend, frontend]
  - id: backend
    title: Backend Development
    group: Computing
    path: 10_backend/
    entrypoint: 10_backend/README.md
    status: canonical
    last_reviewed: 2026-09-23
    scope: Framework-independent backend core concepts plus Java, Spring, and Python language/framework tracks.
    prerequisites: [computer_science]
    related: [data_engineering, devops_platform_engineering, frontend]
  - id: frontend
    title: Frontend Development
    group: Computing
    path: 10_frontend/
    entrypoint: 10_frontend/javascript/javascript_beginner_rebuilt.md
    status: canonical
    last_reviewed: 2026-09-23
    scope: Web platform, JavaScript, TypeScript, React, CSS, XML, WebSquare, and frontend production practice.
    prerequisites: [computer_science]
    related: [backend, native, devops_platform_engineering]
  - id: native
    title: Native Mobile Development
    group: Computing
    path: 11_native/
    entrypoint: 11_native/00_INDEX.md
    status: canonical
    last_reviewed: 2026-09-23
    scope: Swift/iOS and Kotlin/Android from language foundations through platform and production engineering.
    prerequisites: [computer_science, frontend]
    related: [backend, frontend]
  - id: data_engineering
    title: Data Engineering
    group: Computing
    path: data_engineering/
    entrypoint: data_engineering/README.md
    status: canonical
    last_reviewed: 2026-09-23
    scope: Data lifecycle and pipeline semantics; analytical storage; modeling and transformation; distributed and streaming processing; orchestration/backfill; warehouse/lakehouse; serving and semantic metrics; governance, lineage, security, cost/capacity; and end-to-end case studies.
    prerequisites: [computer_science, mathematics]
    related: [backend, devops_platform_engineering, sql]
  - id: devops_platform_engineering
    title: DevOps / Platform Engineering
    group: Computing
    path: devops_platform_engineering/
    entrypoint: devops_platform_engineering/README.md
    status: canonical
    last_reviewed: 2026-09-23
    scope: Runtime, delivery, containers, infrastructure, Kubernetes, GitOps, SRE, security, platform, and production practice.
    prerequisites: [computer_science, linux]
    related: [backend, data_engineering, linux]
  - id: linux
    title: Linux
    group: Computing
    path: linux/
    entrypoint: linux/README.md
    status: canonical
    last_reviewed: 2026-09-23
    scope: Linux foundations, filesystem, shell, identity, processes, resources, networking, operations, and production systems.
    prerequisites: [computer_science]
    related: [devops_platform_engineering, backend]
  - id: automation
    title: Automation
    group: Computing
    path: automation/
    entrypoint: automation/README.md
    status: canonical
    last_reviewed: 2026-09-23
    scope: Automation workflows, prompts, and operational tooling for the learning repository.
    prerequisites: [computer_science]
    related: [devops_platform_engineering, backend]

  - id: psychology
    title: Psychology
    group: Human & Society
    path: psychology/
    entrypoint: psychology/README.md
    status: canonical
    last_reviewed: 2026-09-23
    scope: Psychology as a science with concepts, mechanisms, evidence status, limitations, and cross-domain connections.
    prerequisites: [biology]
    related: [computer_science, korean_culture, research_methods]
  - id: korean_history
    title: Korean History
    group: Human & Society
    path: korean_history/
    entrypoint: korean_history/README.md
    status: canonical
    last_reviewed: 2026-09-23
    scope: Korean peninsula history from prehistory through contemporary Korea with social, economic, and technology history.
    prerequisites: []
    related: [world_history, korean_culture, korea_business_economy, korea_law_civic_life]
  - id: world_history
    title: World History
    group: Human & Society
    path: world_history/
    entrypoint: world_history/README.md
    status: canonical
    last_reviewed: 2026-09-23
    scope: World history as a causal system from human origins through agrarian states, classical and medieval networks, industrialisation, imperialism, world wars, the Cold War, decolonisation, and the post-Cold-War world.
    prerequisites: []
    related: [world_geography, korean_history, korean_culture, investing, korea_law_civic_life, research_methods]
  - id: korean_culture
    title: Korean Culture
    group: Human & Society
    path: korean_culture/
    entrypoint: korean_culture/README.md
    status: canonical
    last_reviewed: 2026-09-23
    scope: Korean society, relationships, family, education, work, food, arts, regions, Hallyu, and modern life.
    prerequisites: [korean_history]
    related: [korea_law_civic_life, kiip, korean_history]
  - id: korea_business_economy
    title: Korea Business & Economy
    group: Human & Society
    path: korea_business_economy_knowledge_library/
    entrypoint: korea_business_economy_knowledge_library/README.md
    status: canonical
    last_reviewed: 2026-09-23
    scope: Korean business, economy, company cases, institutions, and market reasoning.
    prerequisites: [korean_history]
    related: [economics, investing, korean_culture, korea_law_civic_life]
  - id: korea_law_civic_life
    title: Korea Law, Civic & Everyday Life
    group: Human & Society
    path: korea_law_civic_life/
    entrypoint: korea_law_civic_life/README.md
    status: canonical
    last_reviewed: 2026-09-23
    scope: Korean law, public administration, labor, housing, tax, insurance, finance, immigration, and daily procedures.
    prerequisites: [korean_history, korean_culture]
    related: [kiip, korea_business_economy]
  - id: economics
    title: Economics
    group: Human & Society
    path: economics/
    entrypoint: economics/README.md
    status: canonical
    last_reviewed: 2026-09-24
    scope: Core-domain complete Economics library covering foundations, microeconomics, market structure/game theory, macroeconomics, applied economics, econometrics, and economic history/institutions with explicit evidence and integration boundaries.
    prerequisites: [mathematics]
    related: [investing, korea_business_economy, psychology, world_history, world_geography, computer_science, research_methods]
  - id: world_geography
    title: World Geography
    group: Human & Society
    path: world_geography/
    entrypoint: world_geography/README.md
    status: canonical
    last_reviewed: 2026-09-23
    scope: Earth systems, regional geography, world atlas, human geography, and global connections.
    prerequisites: []
    related: [world_history, biology, physics, korea_business_economy]

  - id: investing
    title: Investing
    group: Professional
    path: investing/
    entrypoint: investing/README.md
    status: canonical
    last_reviewed: 2026-09-23
    scope: Investing foundations, asset classes, company analysis, applied economics, trading, derivatives, and Korea/Vietnam markets.
    prerequisites: [mathematics]
    related: [economics, korea_business_economy, pmp, sql]
  - id: pmp
    title: Project Management / PMP
    group: Professional
    path: pmp/
    entrypoint: pmp/README.md
    status: canonical
    last_reviewed: 2026-09-23
    scope: Project value, delivery, people, planning, risk, governance, adaptive delivery, quantitative practice, and case studies.
    prerequisites: []
    related: [investing, devops_platform_engineering, psychology]

  - id: information_processing_engineer
    title: 정보처리기사
    group: Certifications
    path: 정보처리기사/
    entrypoint: 정보처리기사/output/README.md
    status: canonical
    last_reviewed: 2026-09-23
    scope: Korean Information Processing Engineer certification subjects and structured study outputs.
    prerequisites: [computer_science]
    related: [sql, backend, computer_science]
  - id: sql
    title: SQLD / SQL
    group: Certifications
    path: sql/
    entrypoint: sql/output/README.md
    status: canonical
    last_reviewed: 2026-09-23
    scope: Data modeling, SQL fundamentals, query patterns, normalization, and database reasoning.
    prerequisites: [computer_science]
    related: [data_engineering, investing]
  - id: kiip
    title: KIIP exam notes / Korean Society
    group: Certifications
    path: korean_culture/kiip/
    entrypoint: korean_culture/kiip/README.md
    status: canonical
    last_reviewed: 2026-09-23
    scope: Notes for the KIIP Korean Society comprehensive exam, organized by exam content rather than course-level folders.
    prerequisites: [korean_history, korean_culture, korea_law_civic_life]
    related: [korean_culture, korea_law_civic_life]

supporting:
  - id: dev_everyday
    path: dev_everyday/
    status: support
    scope: Personal developer notes and local workflow configuration; not a canonical knowledge library.
  - id: study_planner
    path: planner/
    status: support
    scope: Planning application and study scheduling data.
  - id: study_library
    path: learning-library/
    status: support
    scope: Static Markdown/PDF reader and publication pipeline for GitHub Pages.
  - id: templates
    path: 99.template_folder/
    status: support
    scope: Reusable templates for future libraries.

---

# Repository catalog

`main` là source of truth hiện tại. Các branch feature chỉ là lịch sử phát triển; không dùng tên branch để mô tả trạng thái canonical của library.

## Cây domain

```text
Science
├── Mathematics
├── Physics
├── Chemistry
└── Biology

Engineering
└── Electrical Engineering

Methods
└── Research Methods

Computing
├── Computer Science
├── Backend Development
├── Frontend Development
├── Native Mobile Development
├── Data Engineering
├── DevOps / Platform Engineering
├── Linux
└── Automation

Human & Society
├── Philosophy
├── Psychology
├── Korean History
├── World History
├── Korean Culture
├── Korea Business & Economy
├── Korea Law, Civic & Everyday Life
├── Economics
└── World Geography

Professional
├── Investing
└── Project Management / PMP

Certifications
├── 정보처리기사
├── SQLD / SQL
└── KIIP / Korean Society

Supporting
├── Study Planner
├── Study Library
└── Templates
```

## Metadata contract

Mỗi entry trong YAML front matter có các field tối thiểu:

- `status`: `canonical` là nội dung thuộc source of truth hiện tại; `support` là tooling hoặc dữ liệu hỗ trợ.
- `last_reviewed`: ngày audit cấu trúc/nội dung gần nhất.
- `scope`: ranh giới nội dung, không phải slogan marketing.
- `prerequisites`: các domain nên học trước.
- `related`: các domain có quan hệ knowledge graph trực tiếp.

Khi thêm library mới, cập nhật cả YAML metadata và cây domain trong file này. Không rename/move hàng loạt folder nếu chưa có kế hoạch cập nhật internal links.

## 7. Economics: core-domain complete

[`economics/`](economics/README.md) hiện có full canonical route từ Foundations → Microeconomics → Market Structure & Game Theory → Macroeconomics → Econometrics → Applied Economics → Economic History & Institutions. Applied layer bao phủ labor, public economics, trade, development và industrial organization; historical/institutional layer bao phủ state capacity, finance/fiscal states, industrialization/globalization và crises/path dependence.

Economics giữ explicit boundaries: theory không thay evidence, accounting identity không thay causal theory, estimator không thay identification strategy, causal estimate không tự trở thành policy recommendation. [`investing/04_economics/`](investing/04_economics/) tiếp tục giữ market/application layer về macro data, liquidity, transmission, crisis cases và nowcasting; World/Korean History giữ chronology; Korea Business giữ Korean company/institution cases.

## 8. Research Methods: cross-domain methodology foundation

[`research_methods/`](research_methods/README.md) giữ methodology dùng chung cho toàn repository: research question/design, measurement/sampling/surveys, qualitative methods, systematic reviews/evidence synthesis, mixed methods, ethics, reproducibility và open science. Estimator-level causal/statistical methods tiếp tục nằm ở [`economics/05_econometrics/`](economics/05_econometrics/README.md); Philosophy giữ epistemology/philosophy-of-science foundation.

Mục tiêu là tránh mỗi domain tự lặp lại generic research methods và tạo một evidence contract thống nhất cho các library sau này, đặc biệt Sociology.

## 9. P3 — Electrical / Electronics / Control

Physics hiện đã rất mạnh, bao gồm Maxwell, circuits, transmission line, semiconductor, MOSFET, signal/noise và các nền tảng liên quan. Nhưng **Physics không đồng nghĩa với Electrical Engineering**: engineering cần thêm topology, design trade-off, measurement, timing, power, control, verification và failure handling.

Vì vậy đã thêm [`electrical_engineering/`](electrical_engineering/README.md) như một domain P3, với cấu trúc:

```text
electrical_engineering/
├── circuits
├── analog_electronics
├── digital_electronics
├── signals_and_systems
├── communication_systems
├── control_systems
├── embedded_systems
├── power_electronics
└── hardware_software_interfaces
```

Bridge kiến thức chủ đích:

```text
Physics
→ Electronics
→ Digital logic
→ Computer Architecture
→ Embedded
→ Software
```

Đây là một library canonical đã có core chapter cho cả 9 nhánh, dependency map và coverage audit; các chapter chuyên sâu sẽ được mở rộng theo từng nhánh, không duplicate Physics hoặc Computer Science.

## Domain entrypoints

Các link entrypoint đầy đủ nằm trong YAML ở đầu file để máy đọc được; README root chỉ là phần giới thiệu ngắn. Đây là catalog cấp repository, không thay thế README chuyên sâu của từng library.
