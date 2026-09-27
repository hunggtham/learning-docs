# Philosophy — Coverage Audit

## Baseline 2026-09

Đợt audit này giữ 10 namespace đúng theo dependency của Philosophy và nâng library từ scaffold lên một baseline có chiều sâu: **65 Markdown files**, gồm chapter trục, module lập luận nâng cao, applied ethics, history, dependency map, editorial standard, cross-domain casework và module Marx–Lenin–Marxism–Leninism. Vòng depth pass hiện đã làm dày các node trung tâm về epistemology, causality, free will, consciousness, ethics, justice, political economy và technology; chuỗi đọc chính vẫn là câu hỏi → epistemology → metaphysics → science → mind → ethics → political philosophy → technology.

| Namespace | Trạng thái | Trục câu hỏi |
|---|---|---|
| `00_philosophical_reasoning` | deep baseline | Câu hỏi, concept, logic, language, argument, objection, thought experiment |
| `01_epistemology` | deep baseline | Knowledge, testimony, disagreement, virtue, formal belief, evidence, uncertainty |
| `02_metaphysics` | deep baseline | Reality, identity, modality, time, free will, process, emergence |
| `03_philosophy_of_science` | deep baseline | Model, explanation, causality, realism, measurement, replication, Biology/Physics |
| `04_philosophy_of_mind` | deep baseline | Mind, consciousness, mental causation, embodiment, perception, self-model |
| `05_ethics` | deep baseline | Metaethics, duty, consequence, virtue, care, bio/climate/professional ethics |
| `06_social_political_philosophy` | deep baseline + focused module | Justice, rights, democracy, power, labor, institutions, global difference; Marx, Lenin, Marxism–Leninism, implementation, Vietnam context, critiques, later traditions, comparative political economy, primary-text route, worked Soviet/China/Vietnam cases và evidence-depth pass |
| `07_philosophy_of_technology` | deep baseline | Mediation, data, design, automation, information, platform power |
| `08_history_of_philosophy` | deep baseline | Ancient–medieval–modern, Indian, Chinese, global and contemporary debates |
| `90_connections` | deep baseline | Mathematics, logic, computation, science, Psychology, CS, AI and cases |

## Gap tiếp theo

- Bổ sung modal logic, philosophy of language, semantics/reference và formal epistemology.
- Mở rộng philosophy of science về laws of nature, experiment, values in science, social epistemology và philosophy of biology/physics.
- Đào sâu philosophy of mind về perception, self-model, free-energy/predictive processing và consciousness measurement.
- Bổ sung professional ethics, disability justice, global justice, animal ethics và environmental ontology.
- Trong social/political philosophy, comparative route vẫn có thể được deepen in-place bằng stronger institutional mechanisms và empirical bridges; không cần mở thêm ideology folder chỉ để tăng breadth.
- Với Marxism–Leninism module, conceptual baseline, worked-case pass và evidence-depth pass đã đủ namespace. Từ đây ưu tiên **deepening in-place**: làm dày causal mechanism, representation/accountability, value/price/reproduction, transition constraints, testability và institutional comparison trong các chapter hiện có thay vì tiếp tục tăng số file.
- Thêm case study ở các module Philosophy khác theo contract: một claim → argument map → data/evidence → stakeholder impact → policy/revision.
- Tăng depth mỗi chapter lên dạng study note dài hơn với primary-text excerpts, formal notation và comparative bibliography khi cần.

## Đánh giá hiện tại

| Tiêu chí | Kết quả | Nhận xét |
|---|---:|---|
| Namespace coverage | 10/10 | Đủ các nhánh người dùng yêu cầu |
| Conceptual spine | đạt | Có dependency map và các learning routes, gồm political-economy → Marx/Lenin → implementation → critique → primary source → worked cases → evidence depth → synthesis |
| Cross-domain links | đạt | Có link Mathematics, Physics, Biology, Psychology, Economics, Research Methods, Sociology, CS và AI |
| Argument/evidence discipline | tốt | Editorial standard được áp dụng; political module tách descriptive/normative/conceptual/empirical claim, theory khỏi implementation, declared doctrine khỏi actual institution, output khỏi productivity/welfare và quantitative series khỏi methodological assumptions |
| Historical/global balance | đang mở rộng | Đã có Indian/Chinese/global, Marxist-Leninist genealogy và Soviet/China/Vietnam casework; còn thiếu African, Latin American và Islamic thinkers chuyên sâu |
| Chapter depth | focused deep pass + in-place mechanism pass | Module hiện có genealogy, objections, rival frameworks, source verification, worked comparative cases, *Capital* close reading, evidence-specific chapters và một pass mới làm dày trực tiếp Marx social theory, Marxian political economy, Lenin, doctrinal institutionalization, critique và comparative political economy |

Điểm nghẽn còn lại không phải thiếu thư mục. Công việc đúng hướng là tăng **độ dày nội tại** của reasoning chain: mỗi concept phải đi qua mechanism, boundary, objection và empirical handoff trước khi chuyển sang concept kế tiếp.

## Tiêu chí hoàn thiện chapter

```text
prerequisite / position
→ definition
→ mechanism
→ consequence
→ objection or rival interpretation
→ evidence boundary
→ downstream handoff
```

Một chapter chưa hoàn chỉnh nếu chỉ liệt kê tên triết gia, trường phái hoặc khẩu hiệu mà không cho thấy lập luận, tiền đề và giới hạn của chúng. Với chapter đã có breadth đủ, không thêm heading mới chỉ để tăng độ dài; ưu tiên làm rõ các arrow giữa các concept đang có.

## Tiêu chí cho historical-political case

Worked case phải tách:

```text
country × period × starting condition
→ declared goal / doctrine
→ actual institution
→ policy
→ incentive + information mechanism
→ implementation method
→ measured outcome
→ unintended consequence
→ adaptation / correction
→ counterfactual + uncertainty
```

Outcome phải được giữ như vector thay vì một score tổng. Growth, productivity, consumption, distribution, health, coercion, political rights, environment và resilience là các dimensions khác nhau; việc gán trọng số giữa chúng là normative judgment, không phải empirical result.

## Tiêu chí cho evidence-depth chapter

Khi một chapter dùng quantitative hoặc historical evidence để deepen một case, cần giữ visible:

```text
claim
→ source / primary record
→ measurement unit / definition
→ identification or causal mechanism
→ competing explanation
→ counterfactual
→ uncertainty
```

`output`, `productivity`, `welfare`, `distribution` và `human cost` không được collapse thành một scalar. Với poverty/GDP/price series phải giữ methodology, real/current/PPP distinction và break in definition nếu có. Với primary text phải phân biệt author's argument với later interpretation hoặc doctrine.

## In-place mechanism depth pass — 2026-09-27

Pass này không tạo thêm chapter. Nó deepen trực tiếp các node đã có centrality cao:

- `01_marx_alienation_history_class_and_ideology.md`: thêm productive activity → social relations, species-being, alienation/fetishism distinction, contradiction as mechanism, class-position → organization → action, social reproduction, agency–structure feedback và ideology mechanisms.
- `02_marxian_political_economy.md`: thêm concrete/abstract labor, value-form, money, `C–M–C` / `M–C–M′`, `c + v + s`, reproduction, reserve army, concentration/centralization, exploitation reconstruction và transformation boundary.
- `04_lenin_party_state_revolution_and_imperialism.md`: thêm spontaneity/consciousness context, information flow, representation/substitution, democratic centralism as institutional rules, transition/coercion mechanism, worker–peasant alliance, monopoly/competition và evidence decomposition cho imperialism.
- `05_marxism_leninism_doctrine_and_variation.md`: thêm canon formation, doctrine functions, party–state separation, democratic centralism, ownership/coordination distinction, national adaptation, legitimacy function và epistemic error-correction problem.
- `08_major_critiques_and_open_questions.md`: thêm functional explanation, transformation problem, exploitation without LTV, profit/crisis decomposition, falling-profit testability, transition constraints và symmetric planning/market information analysis.
- `10_comparative_political_economy.md`: thêm property as bundle of rights, firm governance, workplace authority, cooperatives, investment, innovation, soft budget constraints, competition policy, social insurance, macro stabilization và path-dependent transition.

Pass này phản ánh common prompt: **Understanding > Memorization; Mechanism > Label; Connection > Isolated Fact**.

## Depth pass đã áp dụng

Các node trung tâm hiện dùng sequence:

```text
question / problem
→ definition
→ strongest mechanism or argument
→ premises
→ objection / rival account
→ evidence boundary
→ implication
→ handoff
```

Primary-source context được dùng để định vị tranh luận (Gettier, Hume/Kant/Frankfurt, Nagel/Dennett, Rawls/Sen, Marx/Engels/Lenin, Winner/STS...), không biến chapter thành quote collection. Các claim empirical vẫn phải ghi boundary và uncertainty theo `EDITORIAL_STANDARD.md`; riêng political-history modules phải tách declared doctrine, actual institution, policy và measured outcome trước khi suy luận causal.