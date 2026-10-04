# Cars Knowledge Library — Hiểu xe hơi như một hệ thống

Xe hơi dễ bị học ngược: người ta biết tên hãng, model, mã động cơ hoặc horsepower trước khi hiểu chiếc xe phải giải quyết những bài toán vật lý nào. Nhánh này đi theo chiều ngược lại: bắt đầu từ **năng lượng**, cách biến năng lượng thành mô-men, con đường truyền lực tới mặt đường và cách các subsystem cùng tạo ra performance, stability, reliability và ownership cost.

## 1. Một chiếc xe phải làm được những gì?

Ở mức cơ bản, xe phải lưu trữ hoặc nhận năng lượng, biến năng lượng thành chuyển động, truyền lực tới bánh xe, đổi hướng, giảm tốc, hấp thụ dao động từ mặt đường và bảo vệ người/hàng hóa. Vì vậy một car có thể được đọc theo hai chain giao nhau:

```text
propulsion chain:
energy source
→ power unit
→ transmission / reduction
→ drivetrain / differentials
→ wheels / tires
→ road

control / chassis chain:
steering
+ suspension
+ brakes
+ body/chassis
+ electronics
+ thermal management
```

Hai chain gặp nhau tại tire-road interface. Đây là điểm giúp tránh học từng subsystem như badge rời.

## 2. ICE, HEV, PHEV và BEV khác nhau ở energy topology

ICE lưu energy chủ yếu trong fuel; BEV trong battery; HEV/PHEV kết hợp engine, motor và battery theo architecture/control khác nhau. Vì vậy thay vì chỉ nhớ acronym, hãy hỏi:

```text
Năng lượng nằm ở đâu?
Thiết bị nào convert nó thành torque?
Ratio nào đổi speed ↔ torque?
Path nào đưa torque tới wheel?
Tire có truyền được force đó xuống road không?
Khi giảm tốc, energy đi thành heat hay được recover?
```

Chapter [`02_hybrid_phev_bev_architecture.md`](02_hybrid_phev_bev_architecture.md) dùng chính các câu hỏi này để so powertrain architecture.

## 3. Horsepower và torque chưa nói hết acceleration

Torque (토크) mô tả xu hướng làm quay; power (출력) mô tả tốc độ thực hiện công. Nhưng engine/motor output chưa phải wheel output:

```text
power-unit torque
× transmission ratio
× final drive
→ wheel torque
→ tire force
→ vehicle acceleration
```

Cùng horsepower, hai xe vẫn có thể khác response vì gearing, mass, tire grip, torque curve và control strategy khác nhau. Điều này mở đường từ engine sang transmission rồi drivetrain thay vì so một con số brochure.

## 4. FWD, RWD, AWD và 4WD là torque-path labels

FWD đưa drive torque chủ yếu tới front wheels; RWD tới rear wheels; AWD/4WD có thể drive cả hai axles nhưng implementation rất khác nhau.

Điều quan trọng:

```text
AWD
≠ more engine power
≠ automatically shorter braking distance
```

Drivetrain phân phối torque; tire-road interface mới quyết định force thực tế. Một BEV vẫn có thể FWD/RWD/AWD, vì powertrain architecture và driven-wheel layout là hai trục khác nhau.

## 5. Sedan, SUV, AWD, Hybrid và 8-speed nằm trên các trục khác nhau

```text
SUV       → body architecture
AWD       → drivetrain
Hybrid    → energy/powertrain architecture
400 hp    → output metric
8-speed   → transmission architecture/spec
```

Không nên xếp chúng thành một taxonomy ngang hàng. Đây là cùng discipline dùng ở Whisky: label chỉ có nghĩa khi biết **nó trả lời câu hỏi nào**.

## 6. Learning route hiện tại

Cars giờ có một dependency chain từ energy tới road rồi quay lại body control:

1. [`01_ice_engine_fundamentals.md`](01_ice_engine_fundamentals.md) — fuel + air → combustion → piston → crankshaft torque → RPM/power.
2. [`02_hybrid_phev_bev_architecture.md`](02_hybrid_phev_bev_architecture.md) — battery/motor/inverter, regen, HEV/PHEV/BEV energy path.
3. [`03_transmissions_and_reduction_gearing.md`](03_transmissions_and_reduction_gearing.md) — gear ratio, torque-converter AT, CVT, DCT, e-CVT, EV reduction gear và final drive.
4. [`04_drivetrain_differentials_awd_4wd.md`](04_drivetrain_differentials_awd_4wd.md) — FWD/RWD/AWD/4WD, open diff, LSD, locker, transfer case và torque vectoring.
5. [`05_tires_traction_and_contact_patch.md`](05_tires_traction_and_contact_patch.md) — contact patch, slip, compound, load transfer và traction limit.
6. [`06_brakes_abs_and_regenerative_braking.md`](06_brakes_abs_and_regenerative_braking.md) — friction braking, ABS/EBD, brake fade, thermal capacity, regen và brake blending.
7. [`07_steering_suspension_and_alignment.md`](07_steering_suspension_and_alignment.md) — steering geometry, springs/dampers, roll, camber/toe/caster, understeer/oversteer và ESC interaction.

Nhờ route này, người đọc có thể trace một event thật:

```text
accelerate
→ power / gearing / drivetrain / tire

brake
→ brake torque / ABS / tire / load transfer

corner
→ steering / suspension / tire / stability control
```

Đây là mức system continuity mà Cars cần trước khi mở rộng breadth.

## 7. Các chapter depth tiếp theo

Từ nền chassis dynamics hiện tại, priority hợp lý là:

```text
engine displacement / cylinder / NA / turbo
→ vehicle thermal management
→ safety / ADAS
→ reading complete car specs
→ maintenance / diagnostics
→ ownership lifecycle / TCO
```

Engine depth quay lại giải thích power-unit design; thermal management sau đó nối trực tiếp cả ICE, hybrid và BEV. Safety/ADAS chỉ nên học sau khi người đọc đã hiểu brake, steering và tire là actuator/physical limit mà electronic control phải dùng.

Không mở motorcycle hoặc broad vehicle taxonomy trước khi Cars đủ sâu để làm vertical mẫu.

## 8. Ba câu hỏi giúp đọc performance claim đúng

### Power unit tạo được gì?

```text
torque vs RPM
power vs RPM
```

### Driveline biến đổi/phân phối nó thế nào?

```text
ratio
final drive
differential
which wheels receive torque
```

### Tire/chassis dùng được bao nhiêu?

```text
traction
surface
load transfer
compound
temperature
slip
alignment
```

Nếu bỏ layer cuối, horsepower, AWD và brake size rất dễ bị overvalue.

## 9. Cars dùng Consumer Literacy như backbone chung

Khi câu hỏi chuyển từ “mechanism hoạt động thế nào?” sang:

```text
spec này đo gì?
part này bền thế nào?
what fails first?
maintenance nào thật sự matters?
warranty nói được gì?
TCO nằm ở đâu?
```

hãy dùng [`../../consumer_literacy/`](../../consumer_literacy/README.md) thay vì lặp generic framework trong từng Cars chapter.

Cụ thể:

- [Specs, Labels & Units](../../consumer_literacy/00_reading_specs_labels_and_units.md)
- [Materials, Quality & Durability](../../consumer_literacy/01_materials_quality_and_durability.md)
- [Reliability, Repairability & Maintenance](../../consumer_literacy/02_reliability_repairability_and_maintenance.md)
- [Warranty, Lifecycle & TCO](../../consumer_literacy/03_warranty_lifecycle_and_total_cost.md)

Cars giữ object-specific mechanism; Consumer Literacy giữ reusable comparison logic.

## 10. Boundary với các domain khác

Cars không sở hữu toàn bộ theory phía sau xe:

- combustion/thermodynamics sâu → Physics/Chemistry;
- motor, inverter, battery electronics → Electrical Engineering;
- road network/fuel/charging infrastructure end-to-end → How Things Work khi domain đó canonical;
- financing/loan/affordability → Personal Finance;
- decision under uncertainty → Thinking.

Life chỉ lấy theory đủ để reader nhìn một chiếc xe và hiểu **energy path, force path, control path, maintenance/failure và lifecycle trade-off**.

## Đọc tiếp theo mục tiêu

- Muốn hiểu engine tạo torque: [`01_ice_engine_fundamentals.md`](01_ice_engine_fundamentals.md).
- Muốn so HEV/PHEV/BEV: [`02_hybrid_phev_bev_architecture.md`](02_hybrid_phev_bev_architecture.md).
- Muốn hiểu AT/CVT/DCT: [`03_transmissions_and_reduction_gearing.md`](03_transmissions_and_reduction_gearing.md).
- Muốn hiểu AWD/4WD: [`04_drivetrain_differentials_awd_4wd.md`](04_drivetrain_differentials_awd_4wd.md), rồi nối sang tire.
- Muốn hiểu snow/wet/grip: [`05_tires_traction_and_contact_patch.md`](05_tires_traction_and_contact_patch.md).
- Muốn hiểu stopping/regen: [`06_brakes_abs_and_regenerative_braking.md`](06_brakes_abs_and_regenerative_braking.md).
- Muốn hiểu handling/ride/alignment: [`07_steering_suspension_and_alignment.md`](07_steering_suspension_and_alignment.md).

Điểm chốt của Cars Library là:

> **Đừng học badge trước system. Đi từ energy → conversion → gearing → torque path → tire-road force → braking/steering/body response, rồi mới đọc specs, marketing và ownership trade-offs.**
