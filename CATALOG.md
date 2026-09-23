---
catalog_version: 1
last_reviewed: 2026-09-23
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
    related: [chemistry, computer_science, biology]
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

  - id: computer_science
    title: Computer Science
    group: Computing
    path: computer_science/
    entrypoint: computer_science/README.md
    status: canonical
    last_reviewed: 2026-09-23
    scope: Computing foundations, algorithms, systems, AI, databases, networks, security, software engineering, and professional connections.
    prerequisites: [mathematics]
    related: [data_engineering, devops_platform_engineering, backend, frontend]
  - id: backend
    title: Backend Development
    group: Computing
    path: 10_backend/
    entrypoint: 10_backend/python/README.md
    status: canonical
    last_reviewed: 2026-09-23
    scope: Backend language and framework tracks including Java, Spring, and Python runtime and production engineering.
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
    scope: Data foundations, pipelines, storage formats, reliability, quality, and production reasoning.
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
    related: [computer_science, korean_culture]
  - id: korean_history
    title: Korean History
    group: Human & Society
    path: korean_history/
    entrypoint: korean_history/README.md
    status: canonical
    last_reviewed: 2026-09-23
    scope: Korean peninsula history from prehistory through contemporary Korea with social, economic, and technology history.
    prerequisites: []
    related: [korean_culture, korea_business_economy, korea_law_civic_life]
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
    related: [investing, korean_culture, korea_law_civic_life]
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
  - id: world_geography
    title: World Geography
    group: Human & Society
    path: world_geography/
    entrypoint: world_geography/README.md
    status: canonical
    last_reviewed: 2026-09-23
    scope: Earth systems, regional geography, world atlas, human geography, and global connections.
    prerequisites: []
    related: [biology, physics, korea_business_economy]

  - id: investing
    title: Investing
    group: Professional
    path: investing/
    entrypoint: investing/README.md
    status: canonical
    last_reviewed: 2026-09-23
    scope: Investing foundations, asset classes, company analysis, economics, trading, derivatives, and Korea/Vietnam markets.
    prerequisites: [mathematics]
    related: [korea_business_economy, pmp, sql]
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
    title: KIIP / Korean Society
    group: Certifications
    path: kiip/
    entrypoint: kiip/level5/README.md
    status: canonical
    last_reviewed: 2026-09-23
    scope: Korean Immigration and Integration Program study material for Korean society and naturalization preparation.
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
├── Psychology
├── Korean History
├── Korean Culture
├── Korea Business & Economy
├── Korea Law, Civic & Everyday Life
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

## Domain entrypoints

Các link entrypoint đầy đủ nằm trong YAML ở đầu file để máy đọc được; README root chỉ là phần giới thiệu ngắn. Đây là catalog cấp repository, không thay thế README chuyên sâu của từng library.
