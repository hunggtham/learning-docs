# Cars Knowledge Library — Hiểu xe hơi như một hệ thống

Xe hơi dễ bị học ngược: người ta biết tên hãng, model, mã động cơ hoặc horsepower trước khi hiểu chiếc xe phải giải quyết những bài toán vật lý nào. Nhánh này đi theo chiều ngược lại: bắt đầu từ **năng lượng**, đi qua force/control/thermal/sensing rồi kết thúc ở **evidence, maintenance và ownership decision**.

## 1. Một chiếc xe phải làm được những gì?

Có thể đọc car theo năm chain giao nhau:

```text
propulsion:
energy → power unit → gearing → drivetrain → tire → road

chassis/control:
steering + suspension + brakes + body + ESC

thermal:
heat source → transport → exchanger → ambient → derating/protection

ADAS:
environment → sensors → perception/estimation → controller
→ brake / steering / torque actuator → tire-road result

ownership:
use case → specs/evidence → wear/failure → maintenance/repair
→ downtime → lifecycle/TCO → keep/repair/replace
```

Các chain không độc lập. ADAS chỉ điều khiển actuator mà chassis/powertrain cung cấp; actuator chỉ tạo được force mà tire-road interface cho phép; sustained capability phụ thuộc thermal envelope; còn ownership result phụ thuộc cả degradation, serviceability và use case.

## 2. Các label trên xe nằm trên những trục khác nhau

```text
SUV       → body architecture
AWD       → drivetrain
Hybrid    → energy/powertrain architecture
400 hp    → output metric
8-speed   → transmission architecture/spec
Level 2   → driving-automation task allocation taxonomy
```

Không nên xếp chúng thành một taxonomy ngang hàng. Label chỉ có nghĩa khi biết **nó trả lời câu hỏi nào**.

## 3. Learning route hiện tại

Cars hiện có route từ component physics tới system behavior rồi sang application/ownership:

1. [`01_ice_engine_fundamentals.md`](01_ice_engine_fundamentals.md) — combustion → piston/crankshaft → torque/RPM/power.
2. [`02_hybrid_phev_bev_architecture.md`](02_hybrid_phev_bev_architecture.md) — battery/motor/inverter, regen, HEV/PHEV/BEV energy path.
3. [`03_transmissions_and_reduction_gearing.md`](03_transmissions_and_reduction_gearing.md) — AT/CVT/DCT/e-CVT, ratio, final drive, EV reduction.
4. [`04_drivetrain_differentials_awd_4wd.md`](04_drivetrain_differentials_awd_4wd.md) — FWD/RWD/AWD/4WD, open diff, LSD, locker, transfer case, torque vectoring.
5. [`05_tires_traction_and_contact_patch.md`](05_tires_traction_and_contact_patch.md) — contact patch, slip, compound, load transfer, traction limits.
6. [`06_brakes_abs_and_regenerative_braking.md`](06_brakes_abs_and_regenerative_braking.md) — friction braking, ABS/EBD, fade, regen, brake blending.
7. [`07_steering_suspension_and_alignment.md`](07_steering_suspension_and_alignment.md) — steering geometry, springs/dampers, alignment, understeer/oversteer, ESC.
8. [`08_engine_displacement_cylinders_na_turbo.md`](08_engine_displacement_cylinders_na_turbo.md) — displacement, cylinder architecture, VE, NA/turbo, boost/intercooling, knock, specific output.
9. [`09_thermal_management_ice_hybrid_bev.md`](09_thermal_management_ice_hybrid_bev.md) — heat generation/storage/rejection, coolant/oil/intercooler, battery/motor/inverter, heat pump/chiller, preconditioning, derating.
10. [`10_safety_adas_perception_control_and_limits.md`](10_safety_adas_perception_control_and_limits.md) — warning/intervention/control assistance, sensing/fusion, estimation/prediction, AEB/ACC/lane systems, driver monitoring, automation taxonomy, calibration/HMI và physical limits.
11. [`11_reading_a_complete_car_spec_sheet.md`](11_reading_a_complete_car_spec_sheet.md) — architecture → specs → protocol → evidence → lifecycle; weight/dimensions, tires/brakes, battery/charging/range, ADAS, towing, reliability và subsystem comparison.
12. [`12_maintenance_diagnostics_and_failure_reasoning.md`](12_maintenance_diagnostics_and_failure_reasoning.md) — precise symptom → competing hypotheses → discriminating evidence → intervention; OBD/DTC, NVH, thermal, brake, EV/ADAS diagnosis và maintenance strategy.
13. [`13_ownership_lifecycle_tco_and_replacement_decisions.md`](13_ownership_lifecycle_tco_and_replacement_decisions.md) — depreciation, energy, wear, repair/downtime, warranty, insurance, EV/Hybrid ownership, low/base/high TCO, repair-vs-replace và ownership horizon.

## 4. Một chiếc xe thật được trace như thế nào?

```text
accelerate
→ power / gearing / drivetrain / tire

brake / corner
→ brake / steering / suspension / tire / ESC

read engine badge
→ displacement / cylinders / aspiration / airflow / pressure

ask if performance repeats
→ heat generation → rejection → derating

ask what ADAS badge means
→ function → responsibility → sensing/estimation → actuator

compare two cars
→ use case → subsystem matrix → protocol/evidence → lifecycle trade-off

investigate a symptom
→ operating condition → hypotheses → discriminating evidence → repair/monitor

keep or replace
→ future maintenance/repair + downtime + depreciation + utility
→ compare with replacement path
```

## 5. Trạng thái depth hiện tại

Cars đã có đủ core subsystem + application continuity để **không cần mở thêm component chapter chỉ vì còn tên part chưa có file**.

Priority tiếp theo chỉ nên mở khi expose gap thật, ví dụ:

```text
real diagnostic casebook
used-car inspection / evidence
ownership scenario drills
```

hoặc một vehicle subsystem còn thiếu làm reader không thể giải thích một use case quan trọng.

Không mở motorcycle hoặc broad vehicle taxonomy chỉ để tăng breadth.

## 6. Cars dùng Consumer Literacy như backbone chung

Khi câu hỏi chuyển từ mechanism sang comparison:

```text
spec này đo gì?
claim có protocol nào?
part này fail/degrade thế nào?
maintenance nào matters?
warranty/TCO ra sao?
```

hãy dùng [`../../consumer_literacy/`](../../consumer_literacy/README.md):

- [Specs, Labels & Units](../../consumer_literacy/00_reading_specs_labels_and_units.md)
- [Materials, Quality & Durability](../../consumer_literacy/01_materials_quality_and_durability.md)
- [Reliability, Repairability & Maintenance](../../consumer_literacy/02_reliability_repairability_and_maintenance.md)
- [Warranty, Lifecycle & TCO](../../consumer_literacy/03_warranty_lifecycle_and_total_cost.md)

Cars giữ object-specific mechanism/application; Consumer Literacy giữ reusable comparison logic.

## 7. Boundary với các domain khác

- combustion/thermodynamics/heat-transfer formal theory → Physics/Chemistry;
- motor, inverter, battery electronics/control theory → Electrical Engineering;
- computer vision/ML/autonomy algorithms → Computer Science;
- road/fuel/charging infrastructure end-to-end → How Things Work khi canonical;
- financing/loan/household affordability → Personal Finance;
- generic decision/uncertainty/causal reasoning → Thinking;
- legal ADAS responsibility/regulation → official/legal owner.

Life chỉ lấy theory đủ để reader hiểu **energy path, force path, control path, thermal constraints, safety-assistance behavior, specs/evidence, maintenance/failure và lifecycle trade-off**.

## Đọc tiếp theo mục tiêu

- Engine torque → [`01_ice_engine_fundamentals.md`](01_ice_engine_fundamentals.md)
- HEV/PHEV/BEV → [`02_hybrid_phev_bev_architecture.md`](02_hybrid_phev_bev_architecture.md)
- AT/CVT/DCT → [`03_transmissions_and_reduction_gearing.md`](03_transmissions_and_reduction_gearing.md)
- AWD/4WD → [`04_drivetrain_differentials_awd_4wd.md`](04_drivetrain_differentials_awd_4wd.md)
- Tire/grip → [`05_tires_traction_and_contact_patch.md`](05_tires_traction_and_contact_patch.md)
- Braking/regen → [`06_brakes_abs_and_regenerative_braking.md`](06_brakes_abs_and_regenerative_braking.md)
- Handling/alignment → [`07_steering_suspension_and_alignment.md`](07_steering_suspension_and_alignment.md)
- Engine badges/turbo → [`08_engine_displacement_cylinders_na_turbo.md`](08_engine_displacement_cylinders_na_turbo.md)
- Heat soak/preconditioning/derating → [`09_thermal_management_ice_hybrid_bev.md`](09_thermal_management_ice_hybrid_bev.md)
- AEB/ACC/lane assist/automation → [`10_safety_adas_perception_control_and_limits.md`](10_safety_adas_perception_control_and_limits.md)
- Full spec comparison → [`11_reading_a_complete_car_spec_sheet.md`](11_reading_a_complete_car_spec_sheet.md)
- Symptom/OBD/diagnostic reasoning → [`12_maintenance_diagnostics_and_failure_reasoning.md`](12_maintenance_diagnostics_and_failure_reasoning.md)
- Ownership/TCO/repair-vs-replace → [`13_ownership_lifecycle_tco_and_replacement_decisions.md`](13_ownership_lifecycle_tco_and_replacement_decisions.md)

> **Đừng học badge trước system. Đọc một chiếc xe như energy + force + thermal + sensing/control + evidence + degradation + lifecycle system; chỉ sau đó spec, repair claim và ownership decision mới có nghĩa.**
