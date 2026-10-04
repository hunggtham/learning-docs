# Life Knowledge Library — Coverage Audit

## Mục tiêu

Audit này giữ `life/` practical nhưng không biến thành encyclopedia mọi đồ vật hoặc duplicate How Things Work, Personal Finance, Thinking và science domains.

Trạng thái dùng trong audit:

```text
deep enough for current layer
in progress
seed only
belongs elsewhere
```

## Scope contract

`life/` sở hữu object/product mechanism, classification axes, specs/labels, use/maintenance, degradation/failure, reliability/repairability ở mức consumer, lifecycle/TCO drivers và consumer-side comparison criteria.

Không sở hữu infrastructure end-to-end, household affordability/debt, formal science theory, generic reasoning hay legal procedure. Các phần đó handoff sang canonical owner tương ứng.

---

# Current coverage

## Consumer Literacy — core backbone implemented

Status: **deep enough for current layer**.

1. `00_reading_specs_labels_and_units.md` — measurement, units, protocol, peak/nominal/sustained, denominator, ratings và marketing labels.
2. `01_materials_quality_and_durability.md` — material × geometry × process × joining × environment × maintenance; wear/fatigue/aging/corrosion.
3. `02_reliability_repairability_and_maintenance.md` — failure modes, redundancy, maintenance strategies, diagnostics, modularity, parts/support và downtime.
4. `03_warranty_lifecycle_and_total_cost.md` — warranty boundary, lifecycle phases, TCO, depreciation, support horizon, repair/replace và sunk-cost boundary.

Generic backbone đã đủ để vertical mới cross-link thay vì duplicate. `marketing / reviews / product claims` vẫn là optional candidate; chưa có lý do mở riêng nếu Thinking/Critical Thinking đã xử lý failure mode đó.

---

## Food & Drink — Whisky application loop complete, Beer first-pass complete

Status: **deep enough for current layer**.

### Whisky

Đã có:

1. `00_whisky_foundations.md` — grain → fermentation → distillation → maturation.
2. `01_classification_and_legal_definitions.md` — multi-axis taxonomy; Scotch/American/Irish/Japanese frameworks; dated official-source snapshot.
3. `02_distillation_stills_reflux_and_cuts.md` — pot/column, reflux, copper, condensers, cuts, recycle và new-make character.
4. `03_casks_maturation_and_finishing.md` — extraction + transformation + subtraction, oak/char/toast, cask history, oxidation, evaporation, climate, finishing, blending và age boundary.
5. `04_tasting_sensory_vocabulary_and_comparison.md` — nose/palate/mouthfeel/finish; sensory families; intensity/balance; dilution; blind comparison; sensory-to-production hypotheses; storage/serving; practice drills.

Current route:

```text
grain / fermentation
→ distillation selection
→ new make
→ cask maturation
→ blending / bottling
→ sensory observation
→ calibrated production hypothesis
```

Whisky no longer has a foundational sensory gap. Future depth should be case-driven: production-region/tradition comparisons, bottle/value evaluation, or repeated blind-practice logs.

### Beer

Đã có:

1. `00_beer_foundations.md` — Ale/Lager/IPA/Stout map và ABV/IBU limits.
2. `01_ingredients_mashing_hops_and_fermentation.md` — malting, mashing, boil/hops, water, yeast, attenuation, conditioning, carbonation, packaging, off-flavour mechanisms.
3. `02_style_map_specs_freshness_and_serving.md` — multidimensional style map; ABV/IBU/OG/FG/SRM/pH/carbonation; freshness, oxidation/light, packaging, serving và sensory-control conditions.

Beer has a complete first-pass route. Future depth should be case-driven, not a catalog of hundreds of styles.

### Breadth gate

Wine/Coffee/Tea are now legitimate candidates only if they reuse the same process/spec/sensory/freshness framework and add a genuinely new reusable mechanism. They are no longer automatically higher priority than integration/application work.

---

## Vehicles / Cars — complete vertical from mechanism to ownership application

Status: **deep enough for current layer**.

Cars hiện có:

1. `README.md` — system map / learning route.
2. `01_ice_engine_fundamentals.md` — combustion → crankshaft torque → RPM/power.
3. `02_hybrid_phev_bev_architecture.md` — HEV/PHEV/BEV energy topology, motor/inverter/battery, regen, charging.
4. `03_transmissions_and_reduction_gearing.md` — AT/CVT/DCT/e-CVT, ratio, final drive, EV reduction.
5. `04_drivetrain_differentials_awd_4wd.md` — FWD/RWD/AWD/4WD, open diff/LSD/locker, transfer case, torque vectoring.
6. `05_tires_traction_and_contact_patch.md` — slip, friction budget, compound, pressure, load transfer, alignment, rolling resistance.
7. `06_brakes_abs_and_regenerative_braking.md` — kinetic energy, friction brakes, ABS/EBD, fade, regen, blending.
8. `07_steering_suspension_and_alignment.md` — steering geometry, springs/dampers, suspension architectures, camber/toe/caster, understeer/oversteer, ESC.
9. `08_engine_displacement_cylinders_na_turbo.md` — displacement/BMEP intuition, cylinder architecture, bore/stroke, VE, NA/turbo, boost/intercooling, lag/wastegate, knock, downsizing, specific output, altitude/fuel/reliability trade-offs.
10. `09_thermal_management_ice_hybrid_bev.md` — heat generation/storage/rejection, coolant/oil/intercooler, hybrid multi-loop systems, battery/motor/inverter cooling, heat pump/chiller, preconditioning, fast charging, derating and thermal failure modes.
11. `10_safety_adas_perception_control_and_limits.md` — warning/intervention/control assistance, camera/radar/ultrasonic, fusion, state estimation/prediction, AEB/ACC/lane control, DMS, ODD, automation taxonomy, calibration, HMI, physical limits and source snapshot.
12. `11_reading_a_complete_car_spec_sheet.md` — application workflow for weight/dimensions, power-to-weight, tire/brake/suspension specs, ICE/hybrid/EV energy specs, gross/usable battery, kW/kWh, charging curve, range protocol, towing, ADAS, reliability evidence and subsystem comparison.
13. `12_maintenance_diagnostics_and_failure_reasoning.md` — symptom definition, severity triage, competing hypotheses, discriminating evidence, OBD/DTC, live data, NVH, thermal/brake/engine/EV/ADAS reasoning, maintenance strategies and repair-decision boundary.
14. `13_ownership_lifecycle_tco_and_replacement_decisions.md` — acquisition, depreciation, energy, wear, repairs/downtime, warranty, insurance, EV/Hybrid ownership, used-car condition, pre-purchase information value, repair-vs-replace, low/base/high TCO and sensitivity analysis.

Cars now covers five connected views:

```text
vehicle force/control
energy → power unit → gearing → drivetrain → tire → brake/steering/body response

engine architecture
geometry → filling/boost → cylinder pressure → torque/power

thermal envelope
heat generation → storage/transport → exchanger → ambient → sustained capability/derating

assistance/application
sensing → estimation/prediction → controller → actuator → physical result
→ spec/protocol/evidence

ownership/failure
wear/failure → symptom → hypotheses → discriminating evidence → maintenance/repair
→ downtime/depreciation/TCO → keep/repair/replace
```

This is sufficient continuity that Cars should no longer receive isolated component chapters without a concrete gap exposed by a real case.

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
| ICE geometry / aspiration / turbo | implemented | Cars |
| vehicle thermal-management model | implemented | Cars |
| safety / ADAS control layer | implemented | Cars + official taxonomy snapshot |
| complete spec-reading application | implemented | Cars + Consumer Literacy |
| maintenance / diagnostic reasoning | implemented | Cars |
| ownership/TCO casebook | implemented | Cars + Consumer Literacy + Personal Finance handoff |
| fermented beverage process | implemented | Beer |
| beer state/spec/freshness model | implemented | Beer |
| distilled-spirit legal classification | implemented | Whisky |
| distillation + maturation mechanism | implemented | Whisky |
| sensory vocabulary/comparison loop | implemented | Whisky |

---

# Canonical ownership check

| Topic | Canonical owner | `life/` chỉ giữ |
|---|---|---|
| Physical/chemical/biological theory | Physics/Chemistry/Biology/EE | mechanism needed to understand object |
| Computer vision/ML/autonomy algorithms | Computer Science | consumer-facing ADAS system behavior |
| Generic reasoning/decision framework | Thinking | product-specific application |
| Budget/debt/affordability | Personal Finance | object-side lifecycle cost drivers |
| Infrastructure/operating chain | How Things Work when canonical | user-facing object/subsystem |
| Regulation/law | official regulator + legal/civic owner | product label/context + dated snapshot |
| Formal reliability/safety engineering | engineering/statistics/safety owners | consumer failure/maintenance model |

---

# Quality gates

Một chapter Life đạt chuẩn khi có: use case rõ; mechanism; classification axes đúng; spec/label có `what/how/limit`; trade-off; degradation/use/maintenance khi relevant; practical comparison criteria; canonical handoff; meaningful internal links; prose nối quanh list/table; và source/time-sensitive discipline theo `prompt/COMMON_PROMPT.md`.

Một chapter chưa đạt nếu chỉ có:

```text
definition + types + brands + tips
```

---

# Repository integration status

Status: **implemented in this branch**.

- `CATALOG.md` — `life` canonical under `Everyday & Consumer`.
- root `README.md` — Life entrypoint.
- `learning-library/library.config.json` — `life/` published as `Life / Consumer Literacy`.
- CATALOG graph — relation with Thinking and Personal Finance.
- ownership boundaries explicit against science theory, Personal Finance, Thinking and How Things Work.

Deliberately không sửa hàng loạt unrelated READMEs chỉ để tăng backlink count.

---

# Next depth order

Life has crossed the threshold where **audit-driven expansion** should replace fixed backlog expansion.

Priority now:

1. Review real usage/search gaps from Cars/Whisky/Beer before opening another deep chapter.
2. Decide whether `product claims / reviews / evidence` exposes a Life-specific failure mode not already covered by Thinking.
3. If adding a new vertical, prefer one that exercises a new reusable mechanism. Strong candidates:
   - Coffee — extraction, roast, grind, brew ratio, freshness and sensory calibration;
   - Tea — oxidation/processing, infusion variables, storage and sensory;
   - Home appliances — energy labels, duty cycle, maintenance, repairability and TCO.
4. Keep Wine deferred unless it adds more than another fermentation/classification/sensory taxonomy.

---

# Rule mở vertical mới

Chỉ mở vertical mới khi nó reuse Consumer Literacy without duplication, expose một reusable mechanism chưa có owner, hoặc current verticals đã coherent đến mức breadth improves the graph rather than dilutes it.

Current state now satisfies the coherence requirement; the remaining question is **which new vertical adds the most new mechanism per file**, not which category is popular.

---

# Kết luận audit

Life hiện có:

```text
canonical repository integration
+ coordination layer
+ Consumer Literacy backbone
+ Cars from propulsion/chassis/thermal/ADAS through diagnostics and ownership/TCO
+ Whisky from grain/legal class/distillation/maturation through sensory comparison
+ Beer from ingredients/process through style/spec/freshness/serving
```

Gap lớn nhất không còn là một chapter cụ thể đã biết trước. Từ đây, chất lượng repository sẽ tăng tốt hơn bằng **real-case feedback + selective breadth** thay vì tiếp tục kéo dài Cars hoặc Whisky theo một taxonomy vô hạn.
