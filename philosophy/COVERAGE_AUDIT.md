# Philosophy — Coverage Audit

## Baseline 2026-09

Đợt audit này giữ 10 namespace đúng theo dependency của Philosophy và nâng library từ scaffold lên một baseline có chiều sâu: **57 Markdown files**, gồm chapter trục, module lập luận nâng cao, applied ethics, history, dependency map, editorial standard, cross-domain casework và module Marx–Lenin–Marxism–Leninism. Vòng depth pass hiện đã làm dày các node trung tâm về epistemology, causality, free will, consciousness, ethics, justice, political economy và technology; chuỗi đọc chính vẫn là câu hỏi → epistemology → metaphysics → science → mind → ethics → political philosophy → technology.

| Namespace | Trạng thái | Trục câu hỏi |
|---|---|---|
| `00_philosophical_reasoning` | deep baseline | Câu hỏi, concept, logic, language, argument, objection, thought experiment |
| `01_epistemology` | deep baseline | Knowledge, testimony, disagreement, virtue, formal belief, evidence, uncertainty |
| `02_metaphysics` | deep baseline | Reality, identity, modality, time, free will, process, emergence |
| `03_philosophy_of_science` | deep baseline | Model, explanation, causality, realism, measurement, replication, Biology/Physics |
| `04_philosophy_of_mind` | deep baseline | Mind, consciousness, mental causation, embodiment, perception, self-model |
| `05_ethics` | deep baseline | Metaethics, duty, consequence, virtue, care, bio/climate/professional ethics |
| `06_social_political_philosophy` | deep baseline + focused module | Justice, rights, democracy, power, labor, institutions, global difference; Marx, Lenin, Marxism–Leninism, implementation, Vietnam context, critiques, later traditions, comparative political economy và primary-text route |
| `07_philosophy_of_technology` | deep baseline | Mediation, data, design, automation, information, platform power |
| `08_history_of_philosophy` | deep baseline | Ancient–medieval–modern, Indian, Chinese, global and contemporary debates |
| `90_connections` | deep baseline | Mathematics, logic, computation, science, Psychology, CS, AI and cases |

## Gap tiếp theo

- Bổ sung modal logic, philosophy of language, semantics/reference và formal epistemology.
- Mở rộng philosophy of science về laws of nature, experiment, values in science, social epistemology và philosophy of biology/physics.
- Đào sâu philosophy of mind về perception, self-model, free-energy/predictive processing và consciousness measurement.
- Bổ sung professional ethics, disability justice, global justice, animal ethics và environmental ontology.
- Trong social/political philosophy, mở comparative route rộng hơn giữa liberalism, conservatism, socialism/social democracy, anarchism và các traditions ngoài phương Tây; module Marxism hiện đã có comparative political economy nhưng chưa thay thế một survey đầy đủ các traditions.
- Với Marxism–Leninism module, baseline conceptual đã đủ. Depth tiếp theo nên ưu tiên **worked historical cases có data/source cụ thể** (industrialization, collectivization, planning/market reform, labor institutions, Vietnam transition) hoặc close reading một primary text cụ thể; không tiếp tục tăng file chỉ bằng vocabulary.
- Thêm case study đầy đủ: một claim → argument map → data/evidence → stakeholder impact → policy/revision.
- Tăng depth mỗi chapter lên dạng study note dài hơn với primary-text excerpts, formal notation và comparative bibliography khi cần.

## Đánh giá hiện tại

| Tiêu chí | Kết quả | Nhận xét |
|---|---:|---|
| Namespace coverage | 10/10 | Đủ các nhánh người dùng yêu cầu |
| Conceptual spine | đạt | Có dependency map và các learning routes, gồm political-economy → Marx/Lenin → implementation → critique → comparison → primary source |
| Cross-domain links | đạt | Có link Mathematics, Physics, Biology, Psychology, Economics, Sociology, CS và AI |
| Argument/evidence discipline | khá tốt | Có editorial standard; Marxism–Leninism module tách descriptive/normative/conceptual/empirical claim, theory khỏi implementation và primary text khỏi later doctrine |
| Historical/global balance | đang mở rộng | Đã có Indian/Chinese/global và Marxist-Leninist genealogy; còn thiếu African, Latin American và Islamic thinkers chuyên sâu |
| Chapter depth | đã có depth pass chọn lọc | Các node centrality cao theo format argument đầy đủ; focused political module hiện có cả genealogy, objections, rival frameworks và source-verification route |

Điểm nghẽn còn lại không phải thiếu thư mục, mà là tiếp tục tăng **độ dày của từng argument** và nối argument với primary text, empirical evidence hoặc worked case cụ thể ở các module chưa nằm trong vòng này. Không tạo folder mới chỉ để tăng file count.

## Tiêu chí hoàn thiện chapter

```text
question → definitions → strongest argument → objection
→ evidence boundary → practical implication → cross-domain link
```

Một chapter chưa hoàn chỉnh nếu chỉ liệt kê tên triết gia, trường phái hoặc khẩu hiệu mà không cho thấy lập luận, tiền đề và giới hạn của chúng.

## Depth pass đã áp dụng

Các node trung tâm hiện dùng sequence:

```text
question → definition → strongest argument → premises
→ objection → reply → rival position
→ empirical boundary → implication
```

Primary-source context được dùng để định vị tranh luận (Gettier, Hume/Kant/Frankfurt, Nagel/Dennett, Rawls/Sen, Marx/Engels/Lenin, Winner/STS...), không biến chapter thành quote collection. Các claim empirical vẫn phải ghi boundary và uncertainty theo `EDITORIAL_STANDARD.md`; riêng political-history modules phải tách declared doctrine, actual institution, policy và measured outcome trước khi suy luận causal.
