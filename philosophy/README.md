# Philosophy Knowledge Library — Thư viện Triết học

`philosophy/` là nơi sở hữu các câu hỏi nền tảng về tri thức, thực tại, khoa học, tâm trí, đạo đức và đời sống chung. Thư viện không trình bày triết học như danh sách học thuyết để ghi nhớ; mỗi chapter đi theo mạch:

```text
question → concept → argument → premise → objection → implication → connection
```

Mục tiêu là giúp người đọc nhận ra một claim đang nói về **mô tả**, **giải thích**, **chuẩn tắc** hay **khái niệm**, sau đó đánh giá claim bằng lập luận và bằng chứng thích hợp. Triết học không thay thế khoa học thực nghiệm, nhưng làm rõ câu hỏi, tiêu chuẩn biện minh, giới hạn mô hình và hệ quả giá trị mà khoa học không tự quyết định được.

## Những câu hỏi trung tâm

- Ta biết một điều bằng cách nào? Evidence là gì? Một claim được justified ra sao?
- Causality khác correlation ở đâu? Scientific model nói gì về reality?
- Mind, consciousness và identity là gì? Mô tả ngôi thứ nhất liên hệ thế nào với giải thích ngôi thứ ba?
- Moral reasoning hoạt động ra sao? Justice, freedom, power và legitimacy có quan hệ thế nào?
- Political ideologies khác nhau ở conception nào về freedom, authority, property, equality, community và institutional change?
- Technology chỉ là công cụ hay còn định hình agency, knowledge, work và social order?

## Cấu trúc

```text
philosophy/
├── README.md
├── COVERAGE_AUDIT.md
├── 00_philosophical_reasoning/       (4 chapters)
├── 01_epistemology/                  (5 chapters)
├── 02_metaphysics/                   (4 chapters)
├── 03_philosophy_of_science/         (4 chapters)
├── 04_philosophy_of_mind/            (3 chapters)
├── 05_ethics/                        (4 chapters)
├── 06_social_political_philosophy/
│   ├── 4 core chapters
│   ├── 04_marxism_leninism/          (20 chapters)
│   └── 05_political_ideologies/      (10 chapters)
├── 07_philosophy_of_technology/      (3 chapters)
├── 08_history_of_philosophy/         (4 chapters)
└── 90_connections/                   (5 chapters)

Hai file điều phối nằm ở root: [Conceptual Dependencies](CONCEPTUAL_DEPENDENCIES.md) và [Editorial Standard](EDITORIAL_STANDARD.md). Chúng là contract cho mọi chapter mới: không thêm topic nếu chưa biết prerequisite, objection, evidence boundary và downstream connection.
```

## Reading path

1. [Philosophical reasoning: câu hỏi, khái niệm và lập luận](00_philosophical_reasoning/00_questions_concepts_and_arguments.md)
2. [Knowledge, justification và evidence](01_epistemology/00_knowledge_justification_and_evidence.md)
3. [Belief, uncertainty và calibration](01_epistemology/01_belief_uncertainty_and_calibration.md)
4. [Reality, identity và change](02_metaphysics/00_reality_identity_and_change.md)
5. [Models, explanation và causality](03_philosophy_of_science/00_models_explanation_and_causality.md)
6. [Mind, consciousness và personal identity](04_philosophy_of_mind/00_mind_consciousness_and_identity.md)
7. [Moral reasoning, values và action](05_ethics/00_moral_reasoning_values_and_action.md)
8. [Justice, power và political legitimacy](06_social_political_philosophy/00_justice_power_and_legitimacy.md)
9. [Technology, design và human agency](07_philosophy_of_technology/00_technology_design_and_human_agency.md)
10. [Bản đồ lịch sử các truyền thống triết học](08_history_of_philosophy/00_map_of_philosophical_traditions.md)

### Reading path nâng cao

- [Logic và argument forms](00_philosophical_reasoning/01_logic_validity_and_argument_forms.md) → [Thought experiments](00_philosophical_reasoning/02_thought_experiments_and_conceptual_analysis.md) → [Social epistemology](01_epistemology/02_social_epistemology_testimony_and_disagreement.md).
- [Modality, time và free will](02_metaphysics/01_modality_time_and_free_will.md) → [Reduction và emergence](02_metaphysics/02_reduction_emergence_and_naturalism.md) → [Scientific realism](03_philosophy_of_science/01_scientific_realism_laws_and_underdetermination.md).
- [Measurement, statistics và replication](03_philosophy_of_science/02_measurement_statistics_and_replication.md) → [Mental causation và embodiment](04_philosophy_of_mind/01_mental_causation_embodiment_and_extended_mind.md) → [Metaethics](05_ethics/01_metaethics_and_normative_frameworks.md).
- [Bioethics, climate và AI ethics](05_ethics/02_bioethics_climate_and_ai_ethics.md) → [Democracy và public reason](06_social_political_philosophy/01_democracy_rights_and_public_reason.md) → [Technology ethics](07_philosophy_of_technology/01_technology_ethics_data_and_automation.md) → [AI alignment](90_connections/03_ai_alignment_and_moral_agency.md).
- [Capitalism, Labor và Institutions](06_social_political_philosophy/02_capitalism_labor_and_institutions.md) → [Marx, Marxism, Lenin và Marxism–Leninism](06_social_political_philosophy/04_marxism_leninism/README.md) → [Major critiques](06_social_political_philosophy/04_marxism_leninism/08_major_critiques_and_open_questions.md) → [Comparative political economy](06_social_political_philosophy/04_marxism_leninism/10_comparative_political_economy.md) → [Primary-text reading guide](06_social_political_philosophy/04_marxism_leninism/11_primary_text_reading_guide.md) → worked Soviet/China/Vietnam cases và evidence-depth chapters. Route này tách intellectual history, doctrine, institutional implementation, critique và empirical economics.
- [Political Ideologies — comparative learning route](06_social_political_philosophy/05_political_ideologies/README.md) → [Comparison framework](06_social_political_philosophy/05_political_ideologies/00_comparison_framework.md) → Liberalism → Conservatism → Socialism/Social Democracy → Anarchism → Libertarianism → Republicanism → Nationalism → Fascism → [Comparative synthesis](06_social_political_philosophy/05_political_ideologies/09_comparative_synthesis.md). Route này dùng cùng institutional grammar cho các traditions thay vì xếp chúng trên một score trái–phải duy nhất.

Các route nâng cao không phải thứ tự bắt buộc. Chúng làm lộ dependency: logic giúp kiểm tra argument; epistemology kiểm tra warrant; philosophy of science kiểm tra model/evidence; ethics và political philosophy kiểm tra action/institution; technology và AI đưa toàn bộ chuỗi vào case thực tế.

Depth pass hiện tại không mở thêm top-level namespace. Social/political philosophy giờ có hai focused routes bổ sung nhau: Marxism–Leninism đi sâu genealogy → doctrine → implementation → evidence; Political Ideologies mở breadth có kiểm soát giữa liberalism, conservatism, socialism, anarchism, libertarianism, republicanism, nationalism và fascism. Cả hai route đều dùng contract `problem → definition → mechanism → institution → objection → evidence boundary → handoff`, không biến history of ideas thành glossary hoặc bảng xếp hạng ideology.

## Knowledge connections

- [Philosophy, science, mathematics và AI](90_connections/00_philosophy_science_mathematics_and_ai.md) nối epistemology, model, probability, computation và AI.
- [Philosophy, psychology, mind và society](90_connections/01_philosophy_psychology_mind_and_society.md) nối consciousness, identity, moral psychology, institutions và technology.
- [Mathematics](../mathematics/README.md) cung cấp logic, probability, uncertainty và formal models.
- [Physics](../physics/README.md) và [Biology](../biology/README.md) cung cấp các trường hợp về model, explanation, emergence và reduction.
- [Psychology](../psychology/README.md) kiểm tra các claim về cognition, consciousness, identity và moral judgment bằng evidence thực nghiệm.
- [Economics](../economics/README.md) là owner canonical khi political philosophy tạo claim về price, profit, market structure, growth, planning, welfare, institutions hoặc historical economic outcomes.
- [Sociology](../sociology/README.md) là owner canonical cho class, status, institutions, socialization, collective action, nation/identity và structure/agency khi political theory mở sang empirical social explanation.
- [World History](../world_history/README.md) là owner canonical khi ideology chapter chuyển từ conceptual genealogy sang historical movements, wars, state formation hoặc regime change.
- [Computer Science / AI](../computer_science/README.md) mở rộng các câu hỏi về computation, representation, agency, alignment và responsibility.

## Chuẩn biên soạn

Mỗi chapter nên phân biệt rõ:

1. **descriptive claim** — thế giới hoặc con người đang vận hành thế nào;
2. **normative claim** — nên hành động hoặc tổ chức thế nào;
3. **conceptual claim** — một từ/khái niệm được định nghĩa và phân biệt ra sao;
4. **empirical premise** — tiền đề cần evidence từ Economics, Sociology, History, Psychology hoặc các khoa học khác.

Lập luận phải ghi rõ premise, inference, conclusion, counterargument và điều kiện khiến nó thất bại. Không trình bày một quan điểm lịch sử như consensus hiện đại; các traditions và tác giả được đặt trong bối cảnh, ảnh hưởng, internal variation, objections và giới hạn. Với political ideologies, không suy definition của một tradition từ một party/country đương đại duy nhất và không so ideal của một side với worst historical case của side khác.

Xem [Coverage Audit](COVERAGE_AUDIT.md) để theo dõi phạm vi, các gap còn lại và thứ tự mở rộng chapter.
