# Life Knowledge Library — Coverage Audit

## Mục tiêu

Audit này giữ `life/` đủ practical nhưng không biến thành encyclopedia mọi đồ vật hoặc duplicate How Things Work, Personal Finance và science domains.

Mỗi area dùng bốn trạng thái:

```text
deep enough for current layer
in progress
seed only
belongs elsewhere
```

## Scope contract

`life/` sở hữu:

- everyday objects/products/materials mà người dùng trực tiếp sử dụng;
- mechanism đủ để hiểu object;
- classification axes;
- specs/labels;
- use, maintenance, degradation và failure;
- reliability/repairability ở mức consumer;
- lifecycle/TCO drivers;
- consumer-side comparison criteria.

Không sở hữu:

- infrastructure/system end-to-end → How Things Work;
- budgeting/debt/affordability → Personal Finance;
- scientific theory sâu → canonical science domains;
- generic reasoning → Thinking;
- luật/quy trình hành chính → relevant legal/civic domain / official source.

---

# Current coverage

## Consumer Literacy — core backbone implemented

Status: **deep enough for current layer**.

Đã có bốn reusable chapters:

1. `00_reading_specs_labels_and_units.md` — measurement, units, protocol, peak/nominal/sustained, denominator, ratings và marketing labels.
2. `01_materials_quality_and_durability.md` — material × geometry × process × joining × environment × maintenance; wear/fatigue/aging/corrosion.
3. `02_reliability_repairability_and_maintenance.md` — failure modes, single-point failure, redundancy, maintenance strategies, diagnostics, modularity, parts/support và downtime.
4. `03_warranty_lifecycle_and_total_cost.md` — warranty boundary, lifecycle phases, TCO, depreciation, support horizon, repair/replace và sunk-cost boundary.

Generic consumer framework đã đủ để các vertical sau cross-link thay vì duplicate.

`marketing / reviews / product claims` vẫn là optional candidate, chỉ mở nếu vertical thật sự cần một Life-specific layer ngoài Thinking/Critical Thinking.

---

## Food & Drink — coherent vertical pair

Status: **deep enough for current foundation, còn sensory depth**.

### Whisky

Đã có:

1. `00_whisky_foundations.md` — grain → fermentation → distillation → maturation.
2. `01_classification_and_legal_definitions.md` — multi-axis taxonomy; Scotch/American/Irish/Japanese frameworks; official-source snapshot.
3. `02_distillation_stills_reflux_and_cuts.md` — vapour/liquid enrichment, pot vs column, reflux, copper, condensers, cuts, recycle và new-make character.
4. `03_casks_maturation_and_finishing.md` — extraction + transformation + subtraction, oak/char/toast, cask history, oxidation, evaporation, climate, finishing, blending và age boundary.

Whisky now has the full mechanism chain:

```text
grain / fermentation
→ distillation selection
→ new make
→ cask maturation
→ blending / bottling
```

Remaining high-value gap:

```text
tasting / sensory vocabulary
→ production comparison exercises
→ storage / serving
```

Không cần mở thêm country list trước sensory/application layer.

### Beer

Đã có:

1. `00_beer_foundations.md` — Ale/Lager/IPA/Stout map và ABV/IBU limits.
2. `01_ingredients_mashing_hops_and_fermentation.md` — malting, mashing, boil/hops, water, yeast, attenuation, conditioning, carbonation, packaging và off-flavour mechanisms.
3. `02_style_map_specs_freshness_and_serving.md` — style as multidimensional process space; ABV/IBU/OG/FG/SRM/pH/carbonation; freshness, oxidation/light, packaging, serving và sensory-control conditions.

Beer now has a complete first-pass route:

```text
ingredients/process
→ style map
→ specs
→ packaged state / freshness
→ serving / perception
```

Future beer depth should be case-driven, not a catalog of hundreds of styles.

### Breadth gate

Food & Drink đã đủ depth để chứng minh Life framework scale được, nhưng mở Wine/Coffee/Tea vẫn chưa phải priority cao hơn finishing Cars core systems hoặc Life canonicalization.

---

## Vehicles / Cars — strongest vertical

Status: **deep enough for core mechanics/chassis foundation; in progress for thermal/safety/ownership**.

Cars hiện có:

1. `README.md` — system map / classification axes.
2. `01_ice_engine_fundamentals.md` — fuel/air/combustion → piston/crankshaft → torque/RPM/power.
3. `02_hybrid_phev_bev_architecture.md` — battery/motor/inverter, HEV/PHEV/BEV topology, charging, regen, BMS/thermal and battery aging.
4. `03_transmissions_and_reduction_gearing.md` — gear ratio, AT/CVT/DCT/e-CVT, final drive, EV reduction.
5. `04_drivetrain_differentials_awd_4wd.md` — FWD/RWD/AWD/4WD, open diff/LSD/locker, transfer case, torque vectoring.
6. `05_tires_traction_and_contact_patch.md` — slip, friction budget, compound, pressure, load transfer, tread, alignment, rolling resistance.
7. `06_brakes_abs_and_regenerative_braking.md` — kinetic energy, friction brakes, ABS/EBD, fade, thermal capacity, regen, one-pedal and blending.
8. `07_steering_suspension_and_alignment.md` — steering geometry, springs/dampers, roll, unsprung mass, suspension architectures, camber/toe/caster, understeer/oversteer and ESC.

Cars now forms a continuous physical/control chain:

```text
energy
→ power unit
→ gearing
→ torque distribution
→ tire-road force
→ braking
→ steering / body response
```

Đây là một major milestone: FWD/AWD, horsepower, “big brakes”, sport suspension và tire width đều có owner/mechanism thay vì badge-level explanations.

### Remaining Cars depth

Priority:

```text
engine displacement / cylinder / NA / turbo
→ thermal management across ICE/HEV/BEV
→ safety / ADAS as control systems over brake/steering
→ complete car-spec reading
→ maintenance / diagnostics
→ ownership lifecycle / TCO casebook
```

Có thể coi core mechanics/chassis foundation là **deep enough for current layer** sau khi các chapter trên được audit/link-clean.

---

# Reusable knowledge coverage

| Layer | Status | Owner |
|---|---|---|
| specs / labels / units | implemented | Consumer Literacy |
| materials / durability | implemented | Consumer Literacy |
| reliability / repairability | implemented | Consumer Literacy |
| maintenance vs aging | implemented | Consumer Literacy |
| warranty / lifecycle / TCO | implemented | Consumer Literacy |
| product claims / reviews | partial via handoff | Thinking + optional Life |
| classification-axis discipline | implemented | Life coordination |
| legal-label snapshot discipline | implemented | Whisky + official sources |
| propulsion / mechanical energy path | implemented | Cars |
| tire-road force / braking / chassis dynamics | implemented | Cars |
| fermented beverage process | implemented | Beer |
| beer state/spec/freshness model | implemented | Beer |
| distilled-spirit legal classification | implemented | Whisky |
| distillation + maturation mechanism | implemented | Whisky |

---

# Canonical ownership check

| Topic | Canonical owner | `life/` chỉ giữ |
|---|---|---|
| Physical/chemical/biological theory | Physics/Chemistry/Biology/EE | mechanism needed to understand object |
| Reasoning/decision framework | Thinking | product-specific application |
| Budget/debt/affordability | Personal Finance | object-side lifecycle cost drivers |
| Infrastructure/operating chain | How Things Work when canonical | user-facing object/subsystem |
| Regulation/law | official regulator + legal/civic owner | product-label context + dated snapshot |
| Formal reliability engineering | engineering/statistics domains | consumer failure/maintenance model |

---

# Quality gates

Một chapter Life đạt chuẩn khi có:

1. use case/problem rõ;
2. mechanism chứ không chỉ feature list;
3. classification axes không bị trộn;
4. spec/label giải thích `what / how / limit`;
5. trade-off;
6. use/maintenance hoặc nói rõ vì sao không relevant;
7. degradation/failure hoặc boundary;
8. reliability/repairability khi material;
9. lifecycle/TCO driver khi material;
10. practical comparison criteria;
11. canonical handoff;
12. internal links có ý nghĩa;
13. prose có mạch trước/sau list/table;
14. legal/time-sensitive rule có jurisdiction + source + snapshot date;
15. source-based chapter tuân thủ semantic coverage rule của `prompt/COMMON_PROMPT.md`.

Một chapter chưa đạt nếu chỉ có:

```text
definition
+ types
+ brands
+ tips
```

---

# Boundary tests

```text
system ngoài xã hội end-to-end?
→ How Things Work

object/product hoạt động, degrade, maintain thế nào?
→ Life

affordability / debt / budget?
→ Personal Finance

decision under uncertainty?
→ Thinking

formal physics/chemistry/biology/engineering theory?
→ canonical science owner

current legal definition / compliance?
→ official source / legal owner
```

Life only keeps enough of each adjacent domain to make the object understandable and navigable.

---

# Repository integration backlog

Life content is now coherent enough that **canonicalization becomes a legitimate next pass**, not premature taxonomy work.

Candidate repository-level integration after this PR is reviewed/merged:

- register `life` in `CATALOG.md`;
- add root README entrypoint;
- add `life` to `learning-library/library.config.json`;
- selective backlinks from Thinking, Personal Finance and relevant science domains;
- only link How Things Work after that domain is canonical on the target branch.

Do not mix this integration with more vertical expansion unless needed to resolve navigation.

---

# Next depth order

Content priority after current pass:

1. Cars: engine displacement / cylinder / naturally aspirated / turbocharging;
2. Cars: thermal management across ICE/Hybrid/BEV;
3. Cars: safety / ADAS connected to brake/steering/tire actuators;
4. Whisky: tasting/sensory vocabulary + comparison practice;
5. Life: decide whether product-claims/reviews deserves a dedicated chapter;
6. only then evaluate one new vertical such as Coffee/Tea/Home Appliances.

A separate **repository canonicalization pass** is now equally high priority because Life has enough structure to deserve discoverability once this content PR is accepted.

---

# Rule mở vertical mới

Chỉ mở vertical mới khi ít nhất một điều đúng:

1. nó dùng được Consumer Literacy backbone mà không duplicate;
2. nó expose một reusable mechanism chưa có owner trong Life;
3. current verticals are coherent enough that expansion improves the graph rather than diluting it.

Current state satisfies condition 3 better than before, nhưng depth/integration vẫn có ROI cao hơn opening multiple categories at once.

---

# Kết luận audit

Life hiện không còn là experimental seed. Nó đã có:

```text
coordination layer
+ Consumer Literacy backbone
+ Cars system vertical from energy to chassis dynamics
+ Whisky from grain to legal class to distillation to maturation
+ Beer from ingredients to process to style/spec/freshness/serving
```

Gap lớn nhất đã chuyển từ **“thiếu kiến thức nền”** sang **“hoàn thiện specialized depth + repository discoverability”**. Vì vậy pass tiếp theo nên chọn giữa Cars thermal/safety depth hoặc canonicalization—not another generic taxonomy expansion.
