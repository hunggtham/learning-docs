# Psychology thư viện kiến thức (knowledge library / 지식 라이브러리)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Psychology thư viện kiến thức (knowledge library / 지식 라이브러리)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Quy ước bắt buộc** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Cấu trúc** để mở rộng đối tượng sang phạm vi kế cận. Mạch này dùng README làm bản đồ owner của psychology, rồi nối các domain theo dependency thay vì danh sách môn rời.

Thư viện này tổ chức Psychology theo **concept → phụ thuộc (dependency / 의존성) → cơ chế (mechanism / 메커니즘) → bằng chứng (evidence / 증거) → limitation → liên kết (connection / 연결)**, không chia Beginner/Intermediate/Advanced và không coi số lượng tệp (file / 파일) là mục tiêu.

Chuẩn gốc (canonical / 정본) nguồn chuẩn (source of truth / 정본) hiện tại: `main`.

## Quy ước bắt buộc

### Ngôn ngữ

Phần giải thích chính dùng **tiếng Việt**. English chỉ giữ như từ khóa (keyword / 키워드) khi cần nhận diện thuật ngữ chuyên ngành:

- câu hỏi (question);
- thiên kiến nhận thức (cognitive bias);
- trí nhớ làm việc (working memory);
- suy luận nhân quả (causal inference);
- an toàn tâm lý (psychological safety).

Không giữ nguyên một câu tiếng Anh nếu có thể diễn đạt tự nhiên bằng tiếng Việt. Tên riêng, acronym, mã (code / 코드), công thức, tên bài báo và thuật ngữ chuẩn có thể giữ nguyên khi cần.

### Năm mức trạng thái bằng chứng

Mọi chapter phải phân biệt khi cần:

1. **Bằng chứng khoa học tương đối vững (established evidence)**;
2. **Lý thuyết hiện đại (current theory)**;
3. **Giả thuyết (hypothesis)**;
4. **Vấn đề còn tranh luận (debated issue/interpretation)**;
5. **Lý thuyết lịch sử (historical theory)**.

Quy tắc chi tiết: [[EVIDENCE_STATUS_GUIDE]].

### Historical Psychology

Freud, Adler và Jung được trình bày như **historical theories có ảnh hưởng**, không phải scientific consensus hiện đại.

Mỗi phần historical cần tách:

```text
bối cảnh
→ khái niệm gốc
→ ảnh hưởng
→ khả năng kiểm tra
→ evidence hiện đại liên quan
→ điểm tương đồng nhưng không tương đương
→ giới hạn / tranh luận
```

Xem [[90_connections/06_historical_theories_and_modern_evidence_matrix]].

> **Chuyển mạch:** Trong **Psychology thư viện kiến thức (knowledge library / 지식 라이브러리)**, **Cấu trúc** tiếp nhận điểm tựa từ **Quy ước bắt buộc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ba tệp (file / 파일) điều phối thư viện (library / 라이브러리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cấu trúc

Cấu trúc này đi từ scientific foundations và brain/mind tới cognition, development, social context, mental health và ứng dụng. Mỗi tuyến chỉ là một cách đi qua cùng hệ thống; phần giải thích của chapter phải chỉ rõ concept trước đó được dùng ở đâu.

```text
psychology/
├── 00_foundations/
├── 01_brain_and_mind/
├── 02_learning_and_cognition/
├── 03_human_development_and_person/
├── 04_mental_health/
├── 05_intervention/
├── 06_applied/
├── 90_connections/
├── EVIDENCE_STATUS_GUIDE.md
├── CONCEPTUAL_DEPENDENCIES.md
├── COVERAGE_AUDIT.md
└── README.md
```

> **Chuyển mạch:** Ở chặng này của **Psychology thư viện kiến thức (knowledge library / 지식 라이브러리)**, **Ba tệp (file / 파일) điều phối thư viện (library / 라이브러리)** tiếp nhận điểm tựa từ **Cấu trúc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Reading đường dẫn (path / 경로) 1 — Scientific foundations** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ba tệp (file / 파일) điều phối thư viện (library / 라이브러리)

Ba file này giữ cho việc học không bị tách thành các chapter rời: dependency cho biết học gì trước, coverage audit cho biết còn gap nào, còn evidence guide cho biết nên tin claim ở mức nào. Hãy dùng chúng để điều hướng và kiểm tra sau mỗi reading path.

- [[CONCEPTUAL_DEPENDENCIES]]: prerequisite và connection giữa các domain.
- [[COVERAGE_AUDIT]]: coverage, depth, language, evidence-status và conceptual gap.
- [[EVIDENCE_STATUS_GUIDE]]: rule phân loại claim theo mức bằng chứng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Psychology thư viện kiến thức (knowledge library / 지식 라이브러리)**, **Ba tệp (file / 파일) điều phối thư viện (library / 라이브러리)** xác định đầu vào; **Reading đường dẫn (path / 경로) 1 — Scientific foundations** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Reading đường dẫn (path / 경로) 2 — Brain, perception, attention và consciousness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reading đường dẫn (path / 경로) 1 — Scientific foundations

1. [[00_foundations/00_psychology_as_science]]
2. [[00_foundations/02_research_methods]]
3. [[00_foundations/03_measurement_statistics]]
4. [[00_foundations/05_psychometrics_and_test_interpretation]]
5. [[00_foundations/06_open_science_and_evidence_evaluation]]
6. [[00_foundations/08_causal_inference_and_psychological_evidence]]
7. [[00_foundations/09_replication_meta_analysis_and_bayesian_reasoning]]

Mục tiêu: phân biệt construct với score, association với causation, statistical significance với tác động (effect / 효과) magnitude, và một paper với cumulative bằng chứng (evidence / 증거).

> **Chuyển mạch:** Trong **Psychology thư viện kiến thức (knowledge library / 지식 라이브러리)**, **Reading đường dẫn (path / 경로) 1 — Scientific foundations** xác định đầu vào; **Reading đường dẫn (path / 경로) 2 — Brain, perception, attention và consciousness** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Reading đường dẫn (path / 경로) 3 — học tập (learning / 학습), bộ nhớ (memory / 메모리) và cognition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reading đường dẫn (path / 경로) 2 — Brain, perception, attention và consciousness

1. [[01_brain_and_mind/00_nervous_system_and_brain]]
2. [[01_brain_and_mind/01_sensation_and_perception]]
3. [[01_brain_and_mind/07_attention_consciousness_and_awareness]]
4. [[01_brain_and_mind/09_consciousness_theories_and_evidence]]
5. [[01_brain_and_mind/04_interoception_pain_and_embodied_mind]]
6. [[01_brain_and_mind/06_stress_allostasis_and_psychoneuroimmunology]]
7. [[01_brain_and_mind/08_sleep_circadian_and_recovery]]
8. [[01_brain_and_mind/05_neuroplasticity_brain_change_and_learning]]

Không dùng neural correlate như nhân quả (causal / 인과적) proof. Các lý thuyết (theory / 이론) consciousness được giữ ở mức hiện tại (current / 현재)/debated lý thuyết (theory / 이론) nếu bằng chứng (evidence / 증거) chưa phân biệt rõ.

> **Chuyển mạch:** Ở chặng này của **Psychology thư viện kiến thức (knowledge library / 지식 라이브러리)**, **Reading đường dẫn (path / 경로) 2 — Brain, perception, attention và consciousness** xác định đầu vào; **Reading đường dẫn (path / 경로) 3 — học tập (learning / 학습), bộ nhớ (memory / 메모리) và cognition** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Reading đường dẫn (path / 경로) 4 — Development, personality và định danh (identity / 식별자)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reading đường dẫn (path / 경로) 3 — học tập (learning / 학습), bộ nhớ (memory / 메모리) và cognition

1. [[02_learning_and_cognition/00_learning_and_conditioning]]
2. [[02_learning_and_cognition/01_memory]]
3. [[02_learning_and_cognition/02_thinking_language_and_decision]]
4. [[02_learning_and_cognition/03_intelligence_and_cognitive_differences]]
5. [[02_learning_and_cognition/04_cognitive_biases_and_metacognition]]
6. [[02_learning_and_cognition/05_language_social_cognition_and_theory_of_mind]]
7. [[02_learning_and_cognition/06_expertise_creativity_and_problem_solving]]
8. [[02_learning_and_cognition/07_memory_distortion_eyewitness_and_false_memory]]
9. [[02_learning_and_cognition/08_decision_under_risk_uncertainty_and_ambiguity]]
10. [[02_learning_and_cognition/09_learning_transfer_forgetting_and_durable_knowledge]]
11. [[02_learning_and_cognition/10_cognitive_offloading_external_memory_and_extended_cognition]]
12. [[02_learning_and_cognition/11_emotion_memory_and_affective_cognition]]
13. [[02_learning_and_cognition/12_temporal_cognition_prospective_memory_and_time]]

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Psychology thư viện kiến thức (knowledge library / 지식 라이브러리)**, **Reading đường dẫn (path / 경로) 3 — học tập (learning / 학습), bộ nhớ (memory / 메모리) và cognition** xác định đầu vào; **Reading đường dẫn (path / 경로) 4 — Development, personality và định danh (identity / 식별자)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Reading đường dẫn (path / 경로) 5 — xã hội (social / 사회적), culture và di chuyển (migration / 마이그레이션)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reading đường dẫn (path / 경로) 4 — Development, personality và định danh (identity / 식별자)

1. [[03_human_development_and_person/00_lifespan_development]]
2. [[03_human_development_and_person/01_attachment_and_relationships]]
3. [[03_human_development_and_person/02_motivation_and_emotion]]
4. [[03_human_development_and_person/03_personality]]
5. [[03_human_development_and_person/09_self_concept_identity_and_self_regulation]]
6. [[03_human_development_and_person/14_parenting_caregiving_and_family_development]]
7. [[03_human_development_and_person/11_aging_cognitive_health_and_late_life]]

> **Chuyển mạch:** Trong **Psychology thư viện kiến thức (knowledge library / 지식 라이브러리)**, **Reading đường dẫn (path / 경로) 4 — Development, personality và định danh (identity / 식별자)** xác định đầu vào; **Reading đường dẫn (path / 경로) 5 — xã hội (social / 사회적), culture và di chuyển (migration / 마이그레이션)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Reading đường dẫn (path / 경로) 6 — Relationships và family** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reading đường dẫn (path / 경로) 5 — xã hội (social / 사회적), culture và di chuyển (migration / 마이그레이션)

1. [[03_human_development_and_person/04_social_and_cultural_psychology]]
2. [[03_human_development_and_person/10_group_dynamics_collective_behavior_and_cooperation]]
3. [[03_human_development_and_person/15_power_status_hierarchy_and_inequality]]
4. [[03_human_development_and_person/16_acculturation_migration_and_bicultural_identity]]
5. [[03_human_development_and_person/12_loneliness_social_connection_and_belonging]]
6. [[03_human_development_and_person/08_moral_psychology_and_prosocial_behavior]]

> **Chuyển mạch:** Ở chặng này của **Psychology thư viện kiến thức (knowledge library / 지식 라이브러리)**, **Reading đường dẫn (path / 경로) 5 — xã hội (social / 사회적), culture và di chuyển (migration / 마이그레이션)** xác định đầu vào; **Reading đường dẫn (path / 경로) 6 — Relationships và family** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Reading đường dẫn (path / 경로) 7 — Stress, coping và everyday self-regulation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reading đường dẫn (path / 경로) 6 — Relationships và family

1. [[03_human_development_and_person/01_attachment_and_relationships]]
2. [[03_human_development_and_person/07_close_relationships_intimacy_and_family]]
3. [[03_human_development_and_person/13_sexuality_desire_and_relationship_functioning]]
4. [[03_human_development_and_person/14_parenting_caregiving_and_family_development]]
5. [[06_applied/03_interpersonal_communication_and_conflict]]
6. [[06_applied/20_negotiation_conflict_and_joint_decision_making]]

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Psychology thư viện kiến thức (knowledge library / 지식 라이브러리)**, **Reading đường dẫn (path / 경로) 6 — Relationships và family** xác định đầu vào; **Reading đường dẫn (path / 경로) 7 — Stress, coping và everyday self-regulation** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Reading đường dẫn (path / 경로) 8 — Mental health, psychopathology và intervention** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reading đường dẫn (path / 경로) 7 — Stress, coping và everyday self-regulation

1. [[01_brain_and_mind/06_stress_allostasis_and_psychoneuroimmunology]]
2. [[03_human_development_and_person/06_stress_coping_and_emotion_regulation]]
3. [[03_human_development_and_person/09_self_concept_identity_and_self_regulation]]
4. [[02_learning_and_cognition/12_temporal_cognition_prospective_memory_and_time]]
5. [[06_applied/12_psychology_in_daily_life_and_self_regulation]]
6. [[06_applied/14_work_stress_burnout_and_recovery]]

Applied content ở đường dẫn (path / 경로) này phải giải thích cơ chế (mechanism / 메커니즘) và bằng chứng (evidence / 증거) strength; không dùng motivational slogan như psychological law.

> **Chuyển mạch:** Trong **Psychology thư viện kiến thức (knowledge library / 지식 라이브러리)**, **Reading đường dẫn (path / 경로) 7 — Stress, coping và everyday self-regulation** xác định đầu vào; **Reading đường dẫn (path / 경로) 8 — Mental health, psychopathology và intervention** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Reading đường dẫn (path / 경로) 9 — Freud, Adler, Jung và historical schools** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reading đường dẫn (path / 경로) 8 — Mental health, psychopathology và intervention

1. [[04_mental_health/00_mental_health_and_psychopathology]]
2. [[04_mental_health/01_assessment_and_diagnosis]]
3. [[04_mental_health/13_anxiety_and_fear_related_disorders]]
4. [[04_mental_health/14_obsessive_compulsive_and_related_disorders]]
5. [[04_mental_health/15_trauma_and_stressor_related_disorders]]
6. [[04_mental_health/12_depressive_disorders_and_anhedonia]]
7. [[04_mental_health/13_bipolar_spectrum_and_mood_regulation]]
8. [[04_mental_health/14_suicide_self_harm_risk_and_prevention]]
9. [[04_mental_health/04_psychosis_and_schizophrenia_spectrum]]
10. [[04_mental_health/15_adhd_attention_executive_function_and_development]]
11. [[04_mental_health/16_autism_social_communication_sensory_and_support]]
12. [[04_mental_health/06_personality_pathology]]
13. [[04_mental_health/07_eating_disorders_and_body_image]]
14. [[04_mental_health/08_substance_use_and_addictive_behavior]]
15. [[04_mental_health/09_grief_loss_and_bereavement]]
16. [[04_mental_health/10_dissociation_somatic_and_functional_symptoms]]
17. [[04_mental_health/11_sleep_insomnia_and_circadian_disorders]]
18. [[05_intervention/00_psychotherapy_and_change]]
19. [[05_intervention/01_cbt_behavioral_and_third_wave]]
20. [[05_intervention/03_psychodynamic_humanistic_and_systemic_therapy]]
21. [[05_intervention/02_biological_and_community_treatment]]

Các tệp (file / 파일) `02_anxiety_ocd_and_trauma.md`, `03_depression_bipolar_and_suicidality.md` và `05_neurodevelopmental_adhd_autism.md` được giữ làm tính tương thích (compatibility / 호환성) cầu nối (bridge / 브리지); lộ trình học (learning path / 학습 경로) mới đi thẳng vào chuẩn gốc (canonical / 정본) chapter. Đây là lộ trình học (learning path / 학습 경로), không phải công cụ tự chẩn đoán.

> **Chuyển mạch:** Ở chặng này của **Psychology thư viện kiến thức (knowledge library / 지식 라이브러리)**, **Reading đường dẫn (path / 경로) 8 — Mental health, psychopathology và intervention** xác định đầu vào; **Reading đường dẫn (path / 경로) 9 — Freud, Adler, Jung và historical schools** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Reading đường dẫn (path / 경로) 10 — công việc (work / 작업), leadership và nhóm (team / 팀)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reading đường dẫn (path / 경로) 9 — Freud, Adler, Jung và historical schools

1. [[00_foundations/01_history_and_major_perspectives]]
2. [[90_connections/00_freud_jung_and_depth_psychology_in_context]]
3. [[90_connections/05_adler_individual_psychology_in_context]]
4. [[90_connections/06_historical_theories_and_modern_evidence_matrix]]
5. [[05_intervention/03_psychodynamic_humanistic_and_systemic_therapy]]
6. [[02_learning_and_cognition/07_memory_distortion_eyewitness_and_false_memory]]
7. [[03_human_development_and_person/03_personality]]
8. [[03_human_development_and_person/09_self_concept_identity_and_self_regulation]]

Mục tiêu là hiểu **historical influence**, không “chứng minh” historical các hệ thống (systems / 시스템들) bằng construct hiện đại có tên tương tự.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Psychology thư viện kiến thức (knowledge library / 지식 라이브러리)**, **Reading đường dẫn (path / 경로) 9 — Freud, Adler, Jung và historical schools** xác định đầu vào; **Reading đường dẫn (path / 경로) 10 — công việc (work / 작업), leadership và nhóm (team / 팀)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Reading đường dẫn (path / 경로) 11 — quyết định (decision / 결정), finance và negotiation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reading đường dẫn (path / 경로) 10 — công việc (work / 작업), leadership và nhóm (team / 팀)

1. [[06_applied/00_work_organization_and_leadership]]
2. [[03_human_development_and_person/10_group_dynamics_collective_behavior_and_cooperation]]
3. [[03_human_development_and_person/15_power_status_hierarchy_and_inequality]]
4. [[06_applied/16_psychological_safety_team_learning_and_speaking_up]]
5. [[06_applied/03_interpersonal_communication_and_conflict]]
6. [[06_applied/14_work_stress_burnout_and_recovery]]
7. [[06_applied/22_career_vocational_psychology_and_person_environment_fit]]

> **Chuyển mạch:** Trong **Psychology thư viện kiến thức (knowledge library / 지식 라이브러리)**, **Reading đường dẫn (path / 경로) 10 — công việc (work / 작업), leadership và nhóm (team / 팀)** xác định đầu vào; **Reading đường dẫn (path / 경로) 11 — quyết định (decision / 결정), finance và negotiation** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Reading đường dẫn (path / 경로) 12 — HCI, digital psychology và AI** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reading đường dẫn (path / 경로) 11 — quyết định (decision / 결정), finance và negotiation

1. [[02_learning_and_cognition/02_thinking_language_and_decision]]
2. [[02_learning_and_cognition/08_decision_under_risk_uncertainty_and_ambiguity]]
3. [[02_learning_and_cognition/12_temporal_cognition_prospective_memory_and_time]]
4. [[06_applied/18_financial_psychology_and_personal_decision_making]]
5. [[06_applied/20_negotiation_conflict_and_joint_decision_making]]

> **Chuyển mạch:** Ở chặng này của **Psychology thư viện kiến thức (knowledge library / 지식 라이브러리)**, **Reading đường dẫn (path / 경로) 11 — quyết định (decision / 결정), finance và negotiation** xác định đầu vào; **Reading đường dẫn (path / 경로) 12 — HCI, digital psychology và AI** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Reading đường dẫn (path / 경로) 13 — Health, body và ngữ cảnh (context / 맥락)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reading đường dẫn (path / 경로) 12 — HCI, digital psychology và AI

1. [[02_learning_and_cognition/01_memory]]
2. [[02_learning_and_cognition/10_cognitive_offloading_external_memory_and_extended_cognition]]
3. [[06_applied/02_hci_ai_and_human_decision_support]]
4. [[06_applied/05_digital_psychology_social_media_and_online_behavior]]
5. [[06_applied/17_misinformation_belief_revision_and_inoculation]]
6. [[90_connections/02_human_ai_collaboration_trust_and_cognitive_offloading]]
7. [[90_connections/03_risk_uncertainty_and_science_communication]]

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Psychology thư viện kiến thức (knowledge library / 지식 라이브러리)**, **Reading đường dẫn (path / 경로) 12 — HCI, digital psychology và AI** xác định đầu vào; **Reading đường dẫn (path / 경로) 13 — Health, body và ngữ cảnh (context / 맥락)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Nguyên tắc viết chapter** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reading đường dẫn (path / 경로) 13 — Health, body và ngữ cảnh (context / 맥락)

1. [[01_brain_and_mind/04_interoception_pain_and_embodied_mind]]
2. [[01_brain_and_mind/06_stress_allostasis_and_psychoneuroimmunology]]
3. [[06_applied/04_health_behavior_stress_and_psychosomatic_connections]]
4. [[04_mental_health/10_dissociation_somatic_and_functional_symptoms]]
5. [[06_applied/13_placebo_nocebo_expectation_and_context]]

Đường dẫn (path / 경로) này tránh false dichotomy “biological hoặc psychological”.

> **Chuyển mạch:** Trong **Psychology thư viện kiến thức (knowledge library / 지식 라이브러리)**, **Reading đường dẫn (path / 경로) 13 — Health, body và ngữ cảnh (context / 맥락)** xác định đầu vào; **Nguyên tắc viết chapter** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Chuẩn gốc (canonical / 정본) nguồn (source / 소스) và merge chính sách (policy / 정책)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nguyên tắc viết chapter

Một chapter tốt cần trả lời tự nhiên:

- phenomenon/bài toán (problem / 문제) là gì;
- construct được định nghĩa và đo thế nào;
- cơ chế (mechanism / 메커니즘) hoặc mô hình (model / 모델) hoạt động ra sao;
- bằng chứng (evidence / 증거) status là gì;
- alternative explanation nào còn tồn tại;
- ranh giới (boundary / 경계) điều kiện (condition / 조건) là gì;
- ứng dụng thực tế có bằng chứng (evidence / 증거) tới đâu;
- chapter nối với lĩnh vực (domain / 도메인) nào khác.

Không dùng bullet thay lập luận (reasoning / 추론) nếu phần đó cần explanatory prose.

> **Chuyển mạch:** Ở chặng này của **Psychology thư viện kiến thức (knowledge library / 지식 라이브러리)**, **Nguyên tắc viết chapter** nêu điều cần giải thích; **Chuẩn gốc (canonical / 정본) nguồn (source / 소스) và merge chính sách (policy / 정책)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Chuẩn gốc (canonical / 정본) nguồn (source / 소스) và merge chính sách (policy / 정책)

Psychology đã được hợp nhất vào `main`. Các branch `feat/psychology-*` chỉ là snapshot lịch sử và không còn là nguồn chuẩn (source of truth / 정본).

Mọi thay đổi mới phải cập nhật trực tiếp chuẩn gốc (canonical / 정본) content trên `main` và ghi nhận chất lượng (quality / 품질) gap, bằng chứng (evidence / 증거) refresh hoặc điều hướng (navigation / 내비게이션) thay đổi (change / 변경) trong [[COVERAGE_AUDIT]].

> **Bàn giao:** Sau **Chuẩn gốc (canonical / 정본) nguồn (source / 소스) và merge chính sách (policy / 정책)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
