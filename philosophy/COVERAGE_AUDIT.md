# Philosophy — Coverage Kiểm tra (audit / 감사)

## Baseline 2026-09

Đợt kiểm tra (audit / 감사) này giữ 10 top-level không gian tên (namespace / 네임스페이스) đúng theo phụ thuộc (dependency / 의존성) của Philosophy và nâng thư viện (library / 라이브러리) lên **76 Markdown files**. Xã hội (social / 사회적)/political philosophy hiện không còn phụ thuộc vào một focused Marxism–Leninism tuyến (route / 경로) duy nhất: bên cạnh 4 cốt lõi (core / 핵심) chapters và mô-đun (module / 모듈) Marxism–Leninism 20 chapter, đã có thêm mô-đun (module / 모듈) Political Ideologies 10 chapter để tạo breadth đối xứng hơn giữa các traditions chính của hiện đại (modern / 현대적) political thought.

| Không gian tên (namespace / 네임스페이스) | Trạng thái | Trục câu hỏi |
|---|---|---|
| `00_philosophical_reasoning` | deep baseline | Câu hỏi, concept, lô-gic (logic / 논리), ngôn ngữ (language / 언어), argument, objection, thought experiment |
| `01_epistemology` | deep baseline | Kiến thức (knowledge / 지식), testimony, disagreement, virtue, formal belief, bằng chứng (evidence / 증거), bất định (uncertainty / 불확실성) |
| `02_metaphysics` | deep baseline | Reality, định danh (identity / 식별자), modality, thời gian (time / 시간), free will, tiến trình (process / 프로세스), emergence |
| `03_philosophy_of_science` | deep baseline | Mô hình (model / 모델), explanation, causality, realism, đo lường (measurement / 측정), replication, Biology/Physics |
| `04_philosophy_of_mind` | deep baseline | Mind, consciousness, mental causation, embodiment, perception, self-model |
| `05_ethics` | deep baseline | Metaethics, duty, consequence, virtue, care, bio/climate/professional ethics |
| `06_social_political_philosophy` | deep baseline + 2 focused modules | Justice, rights, democracy, power, labor, institutions, toàn cục (global / 전역) difference; Marx/Lenin/Marxism–Leninism độ sâu (depth / 깊이) tuyến (route / 경로); comparative ideologies tuyến (route / 경로) covering liberalism, conservatism, socialism/xã hội (social / 사회적) democracy, anarchism, libertarianism, republicanism, nationalism và fascism |
| `07_philosophy_of_technology` | deep baseline | Mediation, dữ liệu (data / 데이터), thiết kế (design / 설계), automation, thông tin (information / 정보), nền tảng (platform / 플랫폼) power |
| `08_history_of_philosophy` | deep baseline | Ancient–medieval–hiện đại (modern / 현대적), Indian, Chinese, toàn cục (global / 전역) and contemporary debates |
| `90_connections` | deep baseline | Mathematics, lô-gic (logic / 논리), computation, science, Psychology, CS, AI and cases |

## Gap tiếp theo

- Bổ sung modal lô-gic (logic / 논리), philosophy of ngôn ngữ (language / 언어), ngữ nghĩa (semantics / 의미론)/tham chiếu (reference / 참조) và formal epistemology.
- Mở rộng philosophy of science về laws of nature, experiment, values in science, xã hội (social / 사회적) epistemology và philosophy of biology/physics.
- Đào sâu philosophy of mind về perception, self-model, predictive processing và consciousness đo lường (measurement / 측정).
- Bổ sung professional ethics, disability justice, animal ethics và environmental ontology.
- Với Marxism–Leninism mô-đun (module / 모듈), ưu tiên **deepening in-place**: nhân quả (causal / 인과적) cơ chế (mechanism / 메커니즘), biểu diễn (representation / 표현)/accountability, giá trị (value / 값)/price/reproduction, chuyển tiếp (transition / 전이) các ràng buộc (constraints / 제약조건들), testability và empirical cầu nối (bridge / 브리지). Không gian tên (namespace / 네임스페이스) hiện đã đủ.
- Với Political Ideologies mô-đun (module / 모듈), baseline breadth đã hình thành. Độ sâu (depth / 깊이) tiếp theo nên tăng **in-place** theo những comparative gaps thật: conception of freedom, constitutional thiết kế (design / 설계), thuộc tính (property / 속성)/quyết định (decision / 결정) rights, welfare/insurance, nation/citizenship, công khai (public / 공개)/private domination, party/movement organization và historical hiện thực (implementation / 구현). Không cần thêm ideology chỉ để làm danh sách dài hơn.
- Historical/toàn cục (global / 전역) balance vẫn có thể mở thêm African, Latin American, Islamic và non-Western political traditions khi có đơn vị sở hữu (owner / 오너)/phụ thuộc (dependency / 의존성) rõ, thay vì gắn chúng cơ học vào left–right Western taxonomy.
- Thêm trường hợp (case / 사례) study ở các mô-đun (module / 모듈) Philosophy khác theo đặc tả hợp đồng (contract / 계약): claim → argument map → dữ liệu (data / 데이터)/bằng chứng (evidence / 증거) → stakeholder impact → revision.

## Đánh giá hiện tại

| Tiêu chí | Kết quả | Nhận xét |
|---|---:|---|
| Không gian tên (namespace / 네임스페이스) coverage | 10/10 | Giữ top-level cấu trúc (structure / 구조) ổn định, mở độ sâu (depth / 깊이) bằng focused submodules |
| Conceptual spine | đạt | Có phụ thuộc (dependency / 의존성) map và routes từ normative foundations → political economy → ideology comparison → empirical owners |
| Political breadth | đã cải thiện mạnh | Không còn chỉ có Marxism độ sâu (depth / 깊이); đã có comparative baseline cho 8 ideology families và synthesis chung |
| Marxism–Leninism độ sâu (depth / 깊이) | focused deep pass | Genealogy, doctrine, hiện thực (implementation / 구현), Vietnam ngữ cảnh (context / 맥락), critiques, later traditions, *Capital* close reading, worked Soviet/China/Vietnam cases và evidence-depth chapters |
| Argument/bằng chứng (evidence / 증거) discipline | tốt | Tách conceptual/normative/descriptive/empirical claim; lý thuyết (theory / 이론) khỏi hiện thực (implementation / 구현); ideology label khỏi actual institution; historical kết quả (outcome / 결과) khỏi philosophical verdict |
| Comparison symmetry | đạt baseline | Dùng cùng axes freedom, authority, thuộc tính (property / 속성), coordination, equality, community, voice/exit/contest và dạng thất bại (failure mode / 실패 모드); không xếp hạng traditions |
| Historical/toàn cục (global / 전역) balance | đang mở rộng | Western hiện đại (modern / 현대적) ideologies đã có baseline; non-Western political traditions chuyên sâu vẫn là future expansion |

Điểm nghẽn hiện không phải thiếu số lượng tệp (file / 파일). Hướng đúng là tăng **độ dày nội tại** và **comparative precision**: một term phải đi qua cơ chế (mechanism / 메커니즘), institution, objection, dạng thất bại (failure mode / 실패 모드) và empirical handoff trước khi được dùng để so sánh.

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

Không suy definition của một tradition từ một party hoặc country đương đại. Không lấy historical thất bại (failure / 실패) của một trường hợp (case / 사례) làm proof cho toàn bộ family, và cũng không dùng ideal lý thuyết (theory / 이론) để miễn kiểm tra institutional kết quả (outcome / 결과).

## Tiêu chí cho historical-political trường hợp (case / 사례)

Worked trường hợp (case / 사례) phải tách:

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

Kết quả (outcome / 결과) phải giữ như véc-tơ (vector / 벡터) thay vì một score tổng. Growth, productivity, consumption, phân phối (distribution / 분포), health, coercion, political rights, môi trường (environment / 환경) và resilience là dimensions khác nhau; weighting giữa chúng là normative judgment.

## Tiêu chí cho evidence-depth chapter

Khi dùng quantitative hoặc historical bằng chứng (evidence / 증거):

```text
claim
→ source / primary record
→ measurement unit / definition
→ identification / causal mechanism
→ competing explanation
→ counterfactual
→ uncertainty
```

`output`, `productivity`, `welfare`, `distribution` và `human cost` không được collapse thành một scalar. Với poverty/GDP/price series phải giữ methodology và definition break; với primary văn bản (text / 텍스트) phải phân biệt author's argument với later interpretation/doctrine.

## In-place cơ chế (mechanism / 메커니즘) độ sâu (depth / 깊이) pass — Marxism–Leninism

Pass trước đã deepen trực tiếp các nút (node / 노드) centrality cao:

- `01_marx_alienation_history_class_and_ideology.md`: productive activity → xã hội (social / 사회적) relations, species-being, alienation/fetishism, contradiction, class-position → organization → hành động (action / 동작), reproduction, agency–cấu trúc (structure / 구조) và ideology mechanisms.
- `02_marxian_political_economy.md`: concrete/abstract labor, value-form, money, `C–M–C` / `M–C–M′`, `c + v + s`, reproduction, reserve army, concentration/centralization, exploitation reconstruction và transformation ranh giới (boundary / 경계).
- `04_lenin_party_state_revolution_and_imperialism.md`: thông tin (information / 정보) luồng (flow / 흐름), biểu diễn (representation / 표현)/substitution, democratic centralism, chuyển tiếp (transition / 전이)/coercion, worker–peasant alliance và imperialism bằng chứng (evidence / 증거) decomposition.
- `05_marxism_leninism_doctrine_and_variation.md`: canon formation, doctrine functions, party–trạng thái (state / 상태) separation, quyền sở hữu (ownership / 소유권)/coordination distinction, national adaptation, legitimacy và epistemic correction.
- `08_major_critiques_and_open_questions.md`: functional explanation, transformation bài toán (problem / 문제), exploitation without LTV, profit/crisis decomposition, chuyển tiếp (transition / 전이) các ràng buộc (constraints / 제약조건들) và planning/thị trường (market / 시장) thông tin (information / 정보) symmetry.
- `10_comparative_political_economy.md`: thuộc tính (property / 속성) bundle, firm quản trị (governance / 거버넌스), workplace authority, cooperatives, investment, innovation, soft ngân sách (budget / 예산) các ràng buộc (constraints / 제약조건들), competition chính sách (policy / 정책), insurance, macro stabilization và path-dependent chuyển tiếp (transition / 전이).

## Political Ideologies breadth pass — 2026-09-28

Mô-đun (module / 모듈) `05_political_ideologies/` hiện có:

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

Các distinction bắt buộc đã được tường minh (explicit / 명시적) hóa:

- liberalism ≠ libertarianism;
- socialism ≠ Marxism–Leninism;
- anarchism ≠ chaos;
- republicanism ≠ contemporary party name;
- nationalism ≠ fascism;
- conservatism ≠ fascism;
- thị trường (market / 시장) coordination ≠ capitalism by definition;
- quyền sở hữu trạng thái (state ownership / 상태 소유권) ≠ socialism by definition;
- trạng thái (state / 상태) intervention mức (level / 수준) không đủ để classify ideology.

Mô-đun (module / 모듈) dùng Stanford Encyclopedia of Philosophy làm scholarly anchor cho liberalism, conservatism, socialism, anarchism, libertarianism, republicanism và nationalism; fascism dùng historical tham chiếu (reference / 참조) từ United States Holocaust Memorial Museum/Britannica để tránh biến một contested historical category thành casual political label.

## Độ sâu (depth / 깊이) pass chung

Các nút (node / 노드) trung tâm dùng chuỗi (sequence / 시퀀스):

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

Primary-source ngữ cảnh (context / 맥락) dùng để định vị tranh luận, không biến chapter thành quote collection. Empirical claim phải quay sang chuẩn gốc (canonical / 정본) owners như Economics, Sociology, Psychology, Research Methods hoặc World Lịch sử (history / 이력) thay vì được “chứng minh” bằng ideology văn bản (text / 텍스트).
