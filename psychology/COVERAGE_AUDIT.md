# Psychology Knowledge Library — Coverage Audit

Cập nhật: 2026-09-21. Canonical branch: `feat/psychology-knowledge-library`.

Audit này theo dõi **coverage, độ sâu, trạng thái bằng chứng, ngôn ngữ, mechanism, limitation và conceptual gap**. Mục tiêu là làm đều chất lượng core domain, không tối đa số file.

## Trạng thái

- **Strong**: đủ depth, mechanism, evidence boundary, limitation và connection.
- **Strong / fast-moving**: đủ chất lượng hiện tại nhưng cần periodic evidence refresh vì literature thay đổi nhanh.
- **Bridge**: compatibility/navigation file sau khi canonical content đã tách.
- **Historical-context**: historical theory được đặt đúng bối cảnh, không trình bày như consensus.

Evidence taxonomy: [[EVIDENCE_STATUS_GUIDE]].

## 1. Foundations

Psychology as science, history, research methods, measurement/statistics, ethics, psychometrics, open science, EMA, causal inference và replication/meta-analysis/Bayes hiện đều **Strong**.

## 2. Brain & Mind

Nervous system, sensation/perception, attention, sleep/circadian, interoception/pain, neuroplasticity, stress/allostasis/PNI và evolution/genetics hiện **Strong**. Consciousness có canonical chapter riêng `09_consciousness_theories_and_evidence.md` và được đánh dấu **Strong / current-debated** vì chưa có theory consensus winner.

`02_consciousness_sleep_and_attention.md` là **Bridge** có chủ đích.

## 3. Learning & Cognition

Core group hiện **Strong**: learning, memory, reasoning, language/social cognition, intelligence, decision making, cognitive bias/metacognition, expertise/creativity, memory distortion, durable learning, cognitive offloading, emotion–memory và temporal cognition.

## 4. Human Development & Social Psychology

Lifespan, attachment, motivation/emotion, personality, social-cultural psychology, relationships/family, parenting, identity, acculturation, stress/coping, moral psychology, group dynamics, power/status, loneliness và aging hiện **Strong**.

`10_group_dynamics_collective_behavior_and_cooperation.md` và `15_power_status_hierarchy_and_inequality.md` đã được level 2026-09-21 về tiếng Việt, mechanism, evidence boundary và connection với work/decision systems.

## 5. Mental Health & Psychopathology

Core psychopathology hiện **Strong** sau các đợt split/leveling.

Compatibility bridge được giữ có chủ đích:

- `02_anxiety_ocd_and_trauma.md`;
- `03_depression_bipolar_and_suicidality.md`;
- `05_neurodevelopmental_adhd_autism.md`.

Canonical chapters tương ứng đã tách thành anxiety/fear, OCD, trauma, depression/anhedonia, bipolar, suicide prevention, ADHD và autism.

Psychosis, eating/body image và addiction đã được level 2026-09-21 về tiếng Việt, mechanism và evidence boundary.

## 6. Psychotherapy & Intervention

Psychotherapy/change, CBT/behavioral/third-wave, biological/community treatment và psychodynamic/humanistic/systemic hiện **Strong**. Treatment outcome evidence luôn được tách khỏi truth-status của historical theory hoặc mechanism hypothesis.

## 7. Historical Schools

Freud, Adler và Jung = **Historical-context**.

Canonical guardrail:

- `00_freud_jung_and_depth_psychology_in_context.md`;
- `05_adler_individual_psychology_in_context.md`;
- `06_historical_theories_and_modern_evidence_matrix.md`.

Không trình bày nonconscious processing, attachment, identity integration hoặc modern motivation science như “proof” cho Freud/Adler/Jung.

## 8. Applied Psychology

Everyday self-regulation theo `mechanism → option → limitation`. Work/leadership, communication, burnout, psychological safety, finance, negotiation và career hiện **Strong**.

Nhóm fast-moving sau đã refresh 2026-09-21:

| Domain | Status | Boundary sau refresh |
|---|---|---|
| Digital psychology / social media | **Strong / fast-moving** | General use ≠ problematic use; average associations heterogeneous; không suy causal effect chỉ từ screen time. |
| Misinformation / belief revision | **Strong / fast-moving** | Debunking và prebunking có positive average effects nhưng không phải permanent immunity; source, identity và platform incentive vẫn quan trọng. |
| Human–AI trust / reliance | **Strong / fast-moving** | Trust ≠ trustworthiness ≠ reliance; appropriate reliance quan trọng hơn maximized trust; explainability không tự động tạo calibration. |
| Risk / uncertainty communication | **Strong / fast-moving** | Uncertainty communication không có một effect trust duy nhất; audience, prior belief, topic và presentation matter. |

## 9. Short-file audit — hoàn tất 2026-09-21

Đã kiểm tra foundations, brain/mind, mental health, intervention, applied và historical connections theo kích thước file và vai trò conceptual.

Kết quả:

- không phát hiện core chapter rỗng;
- không phát hiện accidental core stub vài chục dòng;
- các file rất ngắn được phát hiện đều là compatibility bridge có chủ đích;
- bridge không được kéo dài giả tạo chỉ để tăng số dòng.

Các bridge chính: legacy consciousness/sleep/attention, anxiety/OCD/trauma map, depression/bipolar/suicidality map và neurodevelopmental ADHD/autism map.

## 10. README / navigation audit — hoàn tất vòng chính 2026-09-21

`README.md` đã được sửa để reading path Mental Health đi thẳng tới canonical split chapters thay vì bắt người đọc đi qua bridge.

Bridge tiếp tục tồn tại để giữ backward compatibility cho wiki links cũ.

Targeted critical-link pass đã sửa stale path đã phát hiện như financial psychology và xác minh canonical target quan trọng sau refactor. Không tuyên bố full graph `0 broken links` vì connector hiện không có full wiki-link resolver.

## 11. Current state

Không còn domain cốt lõi nào trong audit hiện tại bị đánh dấu thiếu depth hoặc accidental stub.

Remaining work được xếp vào hai loại:

1. **minor polish**: wording, local cross-link hoặc example nhỏ;
2. **periodic evidence refresh**: digital psychology, misinformation, AI reliance và risk communication.

Không tạo chapter mới nếu không phát hiện conceptual gap thực sự.

## 12. Merge gate

Về **content coverage/depth**, merge gate hiện đã đạt: không còn core chapter rỗng/quá sơ sài trong audit hiện tại.

Tuy nhiên branch **chưa được merge tự động trong pass này**. Trước merge nên thực hiện một final targeted branch/navigation check theo workflow repo, đặc biệt xác minh canonical paths và build/site behavior nếu có.