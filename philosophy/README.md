# Philosophy thư viện kiến thức (knowledge library / 지식 라이브러리) — Thư viện Triết học

> **Mạch đọc:** Đọc **Philosophy thư viện kiến thức (knowledge library / 지식 라이브러리) — Thư viện Triết học** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Những câu hỏi trung tâm** sang **Cấu trúc**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


`philosophy/` là nơi sở hữu các câu hỏi nền tảng về tri thức, thực tại, khoa học, tâm trí, đạo đức và đời sống chung. Thư viện không trình bày triết học như danh sách học thuyết để ghi nhớ; mỗi chapter đi theo mạch:

```text
question → concept → argument → premise → objection → implication → connection
```

Mục tiêu là giúp người đọc nhận ra một claim đang nói về **mô tả**, **giải thích**, **chuẩn tắc** hay **khái niệm**, sau đó đánh giá claim bằng lập luận và bằng chứng thích hợp. Triết học không thay thế khoa học thực nghiệm, nhưng làm rõ câu hỏi, tiêu chuẩn biện minh, giới hạn mô hình và hệ quả giá trị mà khoa học không tự quyết định được.

## Những câu hỏi trung tâm

- Ta biết một điều bằng cách nào? bằng chứng (evidence / 증거) là gì? Một claim được justified ra sao?
- Causality khác correlation ở đâu? Scientific mô hình (model / 모델) nói gì về reality?
- Mind, consciousness và định danh (identity / 식별자) là gì? Mô tả ngôi thứ nhất liên hệ thế nào với giải thích ngôi thứ ba?
- Moral lập luận (reasoning / 추론) hoạt động ra sao? Justice, freedom, power và legitimacy có quan hệ thế nào?
- Technology chỉ là công cụ hay còn định hình agency, kiến thức (knowledge / 지식), công việc (work / 작업) và xã hội (social / 사회적) thứ tự (order / 순서)?


> **Chuyển mạch:** Từ **Những câu hỏi trung tâm**, ta sang **Cấu trúc** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

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
├── 06_social_political_philosophy/   (4 chapters)
├── 07_philosophy_of_technology/      (3 chapters)
├── 08_history_of_philosophy/         (4 chapters)
└── 90_connections/                   (5 chapters)

Hai file điều phối nằm ở root: [Conceptual Dependencies](CONCEPTUAL_DEPENDENCIES.md) và [Editorial Standard](EDITORIAL_STANDARD.md). Chúng là contract cho mọi chapter mới: không thêm topic nếu chưa biết prerequisite, objection, evidence boundary và downstream connection.
```


> **Chuyển mạch:** Từ **Cấu trúc**, ta sang **Reading đường dẫn (path / 경로)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Reading đường dẫn (path / 경로)

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

### Reading đường dẫn (path / 경로) nâng cao

- [Logic và argument forms](00_philosophical_reasoning/01_logic_validity_and_argument_forms.md) → [Thought experiments](00_philosophical_reasoning/02_thought_experiments_and_conceptual_analysis.md) → [Social epistemology](01_epistemology/02_social_epistemology_testimony_and_disagreement.md).
- [Modality, time và free will](02_metaphysics/01_modality_time_and_free_will.md) → [Reduction và emergence](02_metaphysics/02_reduction_emergence_and_naturalism.md) → [Scientific realism](03_philosophy_of_science/01_scientific_realism_laws_and_underdetermination.md).
- [Measurement, statistics và replication](03_philosophy_of_science/02_measurement_statistics_and_replication.md) → [Mental causation và embodiment](04_philosophy_of_mind/01_mental_causation_embodiment_and_extended_mind.md) → [Metaethics](05_ethics/01_metaethics_and_normative_frameworks.md).
- [Bioethics, climate và AI ethics](05_ethics/02_bioethics_climate_and_ai_ethics.md) → [Democracy và public reason](06_social_political_philosophy/01_democracy_rights_and_public_reason.md) → [Technology ethics](07_philosophy_of_technology/01_technology_ethics_data_and_automation.md) → [AI alignment](90_connections/03_ai_alignment_and_moral_agency.md).

Các tuyến (route / 경로) nâng cao không phải thứ tự bắt buộc. Chúng làm lộ phụ thuộc (dependency / 의존성): lô-gic (logic / 논리) giúp kiểm tra argument; epistemology kiểm tra warrant; philosophy of science kiểm tra mô hình (model / 모델)/bằng chứng (evidence / 증거); ethics và political philosophy kiểm tra hành động (action / 동작)/institution; technology và AI đưa toàn bộ chuỗi vào trường hợp (case / 사례) thực tế.

Độ sâu (depth / 깊이) pass hiện tại không mở thêm không gian tên (namespace / 네임스페이스). Các nút (node / 노드) trung tâm về epistemology, causality, free will, consciousness, ethics, justice và technology đã được viết lại theo chuỗi `question → definition → strongest argument → premises → objection → reply → rival position → empirical boundary → implication`; primary-source ngữ cảnh (context / 맥락) chỉ dùng để định vị tranh luận, không biến chapter thành tuyển tập trích dẫn.


> **Chuyển mạch:** Từ **Reading đường dẫn (path / 경로)**, ta sang **kiến thức (knowledge / 지식) connections** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kiến thức (knowledge / 지식) connections

- [Philosophy, science, mathematics và AI](90_connections/00_philosophy_science_mathematics_and_ai.md) nối epistemology, mô hình (model / 모델), xác suất (probability / 확률), computation và AI.
- [Philosophy, psychology, mind và society](90_connections/01_philosophy_psychology_mind_and_society.md) nối consciousness, định danh (identity / 식별자), moral psychology, institutions và technology.
- [Mathematics](../mathematics/README.md) cung cấp lô-gic (logic / 논리), xác suất (probability / 확률), bất định (uncertainty / 불확실성) và formal các mô hình (models / 모델들).
- [Physics](../physics/README.md) và [Biology](../biology/README.md) cung cấp các trường hợp về mô hình (model / 모델), explanation, emergence và reduction.
- [Psychology](../psychology/README.md) kiểm tra các claim về cognition, consciousness, định danh (identity / 식별자) và moral judgment bằng bằng chứng (evidence / 증거) thực nghiệm.
- [Computer Science / AI](../computer_science/README.md) mở rộng các câu hỏi về computation, biểu diễn (representation / 표현), agency, alignment và responsibility.


> **Chuyển mạch:** Từ **kiến thức (knowledge / 지식) connections**, ta sang **Chuẩn biên soạn** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Chuẩn biên soạn

Mỗi chapter nên phân biệt rõ:

1. **descriptive claim** — thế giới hoặc con người đang vận hành thế nào;
2. **normative claim** — nên hành động hoặc tổ chức thế nào;
3. **conceptual claim** — một từ/khái niệm được định nghĩa và phân biệt ra sao;
4. **empirical premise** — tiền đề cần bằng chứng (evidence / 증거) từ Psychology, Biology, Physics hoặc các khoa học khác.

Lập luận phải ghi rõ premise, suy luận (inference / 추론), conclusion, counterargument và điều kiện khiến nó thất bại. Không trình bày một quan điểm lịch sử như consensus hiện đại; các truyền thống và tác giả được đặt trong bối cảnh, ảnh hưởng, điểm mạnh, phản biện và giới hạn của chúng.

Xem [Coverage Audit](COVERAGE_AUDIT.md) để theo dõi phạm vi, các gap còn lại và thứ tự mở rộng chapter.

> **Bàn giao:** Sau **Chuẩn biên soạn**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [CONCEPTUAL DEPENDENCIES](./CONCEPTUAL_DEPENDENCIES.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
