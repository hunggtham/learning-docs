# Philosophy — Coverage Audit

## Baseline 2026-09

Đợt audit này giữ 10 top-level namespace đúng theo dependency của Philosophy và nâng library lên **76 Markdown files**. Social/political philosophy hiện không còn phụ thuộc vào một focused Marxism–Leninism route duy nhất: bên cạnh 4 core chapters và module Marxism–Leninism 20 chapter, đã có thêm module Political Ideologies 10 chapter để tạo breadth đối xứng hơn giữa các traditions chính của modern political thought.

| Namespace | Trạng thái | Trục câu hỏi |
|---|---|---|
| `00_philosophical_reasoning` | deep baseline | Câu hỏi, concept, logic, language, argument, objection, thought experiment |
| `01_epistemology` | deep baseline | Knowledge, testimony, disagreement, virtue, formal belief, evidence, uncertainty |
| `02_metaphysics` | deep baseline | Reality, identity, modality, time, free will, process, emergence |
| `03_philosophy_of_science` | deep baseline | Model, explanation, causality, realism, measurement, replication, Biology/Physics |
| `04_philosophy_of_mind` | deep baseline | Mind, consciousness, mental causation, embodiment, perception, self-model |
| `05_ethics` | deep baseline | Metaethics, duty, consequence, virtue, care, bio/climate/professional ethics |
| `06_social_political_philosophy` | deep baseline + 2 focused modules | Justice, rights, democracy, power, labor, institutions, global difference; Marx/Lenin/Marxism–Leninism depth route; comparative ideologies route covering liberalism, conservatism, socialism/social democracy, anarchism, libertarianism, republicanism, nationalism và fascism |
| `07_philosophy_of_technology` | deep baseline | Mediation, data, design, automation, information, platform power |
| `08_history_of_philosophy` | deep baseline | Ancient–medieval–modern, Indian, Chinese, global and contemporary debates |
| `90_connections` | deep baseline | Mathematics, logic, computation, science, Psychology, CS, AI and cases |

## Gap tiếp theo

- Bổ sung modal logic, philosophy of language, semantics/reference và formal epistemology.
- Mở rộng philosophy of science về laws of nature, experiment, values in science, social epistemology và philosophy of biology/physics.
- Đào sâu philosophy of mind về perception, self-model, predictive processing và consciousness measurement.
- Bổ sung professional ethics, disability justice, animal ethics và environmental ontology.
- Với Marxism–Leninism module, ưu tiên **deepening in-place**: causal mechanism, representation/accountability, value/price/reproduction, transition constraints, testability và empirical bridge. Namespace hiện đã đủ.
- Với Political Ideologies module, baseline breadth đã hình thành. Depth tiếp theo nên tăng **in-place** theo những comparative gaps thật: conception of freedom, constitutional design, property/decision rights, welfare/insurance, nation/citizenship, public/private domination, party/movement organization và historical implementation. Không cần thêm ideology chỉ để làm danh sách dài hơn.
- Historical/global balance vẫn có thể mở thêm African, Latin American, Islamic và non-Western political traditions khi có owner/dependency rõ, thay vì gắn chúng cơ học vào left–right Western taxonomy.
- Thêm case study ở các module Philosophy khác theo contract: claim → argument map → data/evidence → stakeholder impact → revision.

## Đánh giá hiện tại

| Tiêu chí | Kết quả | Nhận xét |
|---|---:|---|
| Namespace coverage | 10/10 | Giữ top-level structure ổn định, mở depth bằng focused submodules |
| Conceptual spine | đạt | Có dependency map và routes từ normative foundations → political economy → ideology comparison → empirical owners |
| Political breadth | đã cải thiện mạnh | Không còn chỉ có Marxism depth; đã có comparative baseline cho 8 ideology families và synthesis chung |
| Marxism–Leninism depth | focused deep pass | Genealogy, doctrine, implementation, Vietnam context, critiques, later traditions, *Capital* close reading, worked Soviet/China/Vietnam cases và evidence-depth chapters |
| Argument/evidence discipline | tốt | Tách conceptual/normative/descriptive/empirical claim; theory khỏi implementation; ideology label khỏi actual institution; historical outcome khỏi philosophical verdict |
| Comparison symmetry | đạt baseline | Dùng cùng axes freedom, authority, property, coordination, equality, community, voice/exit/contest và failure mode; không xếp hạng traditions |
| Historical/global balance | đang mở rộng | Western modern ideologies đã có baseline; non-Western political traditions chuyên sâu vẫn là future expansion |

Điểm nghẽn hiện không phải thiếu số lượng file. Hướng đúng là tăng **độ dày nội tại** và **comparative precision**: một term phải đi qua mechanism, institution, objection, failure mode và empirical handoff trước khi được dùng để so sánh.

## Tiêu chí hoàn thiện chapter

```text
prerequisite / position
→ problem definition
→ concept
→ mechanism
→ institutional form
→ consequence
→ objection / internal variation
→ failure mode
→ evidence boundary
→ downstream handoff
```

Một chapter chưa hoàn chỉnh nếu chỉ liệt kê philosopher, ideology label hoặc slogan. Với chapter đã có breadth đủ, không thêm heading chỉ để tăng độ dài; ưu tiên làm rõ arrow giữa concept và institution.

## Tiêu chí cho political-ideology chapter

Mỗi ideology chapter phải giữ cùng comparative grammar:

```text
human/social problem
→ conception of freedom
→ source and limit of authority
→ property / decision rights
→ market / hierarchy / association / planning
→ equality / hierarchy
→ community / membership
→ voice / exit / contestation
→ transition/change model
→ failure mode
→ empirical boundary
```

Không suy definition của một tradition từ một party hoặc country đương đại. Không lấy historical failure của một case làm proof cho toàn bộ family, và cũng không dùng ideal theory để miễn kiểm tra institutional outcome.

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

Outcome phải giữ như vector thay vì một score tổng. Growth, productivity, consumption, distribution, health, coercion, political rights, environment và resilience là dimensions khác nhau; weighting giữa chúng là normative judgment.

## Tiêu chí cho evidence-depth chapter

Khi dùng quantitative hoặc historical evidence:

```text
claim
→ source / primary record
→ measurement unit / definition
→ identification / causal mechanism
→ competing explanation
→ counterfactual
→ uncertainty
```

`output`, `productivity`, `welfare`, `distribution` và `human cost` không được collapse thành một scalar. Với poverty/GDP/price series phải giữ methodology và definition break; với primary text phải phân biệt author's argument với later interpretation/doctrine.

## In-place mechanism depth pass — Marxism–Leninism

Pass trước đã deepen trực tiếp các node centrality cao:

- `01_marx_alienation_history_class_and_ideology.md`: productive activity → social relations, species-being, alienation/fetishism, contradiction, class-position → organization → action, reproduction, agency–structure và ideology mechanisms.
- `02_marxian_political_economy.md`: concrete/abstract labor, value-form, money, `C–M–C` / `M–C–M′`, `c + v + s`, reproduction, reserve army, concentration/centralization, exploitation reconstruction và transformation boundary.
- `04_lenin_party_state_revolution_and_imperialism.md`: information flow, representation/substitution, democratic centralism, transition/coercion, worker–peasant alliance và imperialism evidence decomposition.
- `05_marxism_leninism_doctrine_and_variation.md`: canon formation, doctrine functions, party–state separation, ownership/coordination distinction, national adaptation, legitimacy và epistemic correction.
- `08_major_critiques_and_open_questions.md`: functional explanation, transformation problem, exploitation without LTV, profit/crisis decomposition, transition constraints và planning/market information symmetry.
- `10_comparative_political_economy.md`: property bundle, firm governance, workplace authority, cooperatives, investment, innovation, soft budget constraints, competition policy, insurance, macro stabilization và path-dependent transition.

## Political Ideologies breadth pass — 2026-09-28

Module `05_political_ideologies/` hiện có:

```text
00 comparison framework
01 liberalism
02 conservatism
03 socialism + social democracy
04 anarchism
05 libertarianism
06 republicanism
07 nationalism
08 fascism
09 comparative synthesis
```

Các distinction bắt buộc đã được explicit hóa:

- liberalism ≠ libertarianism;
- socialism ≠ Marxism–Leninism;
- anarchism ≠ chaos;
- republicanism ≠ contemporary party name;
- nationalism ≠ fascism;
- conservatism ≠ fascism;
- market coordination ≠ capitalism by definition;
- state ownership ≠ socialism by definition;
- state intervention level không đủ để classify ideology.

Module dùng Stanford Encyclopedia of Philosophy làm scholarly anchor cho liberalism, conservatism, socialism, anarchism, libertarianism, republicanism và nationalism; fascism dùng historical reference từ United States Holocaust Memorial Museum/Britannica để tránh biến một contested historical category thành casual political label.

## Depth pass chung

Các node trung tâm dùng sequence:

```text
question / problem
→ definition
→ strongest mechanism or argument
→ premises
→ objection / rival account
→ institutional consequences
→ evidence boundary
→ implication
→ handoff
```

Primary-source context dùng để định vị tranh luận, không biến chapter thành quote collection. Empirical claim phải quay sang canonical owners như Economics, Sociology, Psychology, Research Methods hoặc World History thay vì được “chứng minh” bằng ideology text.
