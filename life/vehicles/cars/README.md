# Cars Knowledge Library — Hiểu xe hơi như một hệ thống

> **Mạch đọc:** [Life README](../../README.md) đặt Cars trong nhánh đời sống theo cơ chế. Route đi từ bài toán chuyển động và năng lượng → nguồn động lực (power unit) → truyền mô-men, lốp và mặt đường → hệ thống lái, treo, phanh và khung gầm → quản lý nhiệt, an toàn ADAS → thông số, chẩn đoán bảo dưỡng và tổng chi phí sở hữu (TCO), để tên gọi xe được đọc như kết quả của kiến trúc chứ không phải danh sách model tiếp thị.

Xe hơi rất dễ bị học ngược: người ta thường biết tên hãng, tên model, mã động cơ hay số mã lực (horsepower) trước khi hiểu chiếc xe phải giải quyết những bài toán vật lý nào. Nhánh này đi theo chiều ngược lại: bắt đầu từ **năng lượng**, đi qua chuỗi truyền lực, điều khiển, quản lý nhiệt, cảm biến an toàn, rồi kết thúc ở **bằng chứng thực nghiệm, chẩn đoán bảo dưỡng và quyết định kinh tế sở hữu**.

---

## 1. Một chiếc xe phải làm được những gì?

Ở góc độ kỹ thuật hệ thống, một chiếc xe là sự giao thoa của **năm chuỗi mắt xích liên hoàn**:

```text
1. Propulsion (Chuỗi động lực):
   energy source → power unit → gearing/transmission → drivetrain → tires → road

2. Chassis & Control (Chuỗi khung gầm và kiểm soát):
   steering + suspension + brakes + chassis/body + ESC (Electronic Stability Control)

3. Thermal (Chuỗi quản lý nhiệt):
   heat generation → transport/coolant → heat exchanger → ambient → derating/protection

4. Safety & ADAS (Chuỗi an toàn và hỗ trợ lái):
   environment → sensors (camera/radar/LiDAR) → perception/fusion → controller
   → actuator (phanh / lái / mô-men motor) → tire-road physical limits

5. Ownership Lifecycle (Chuỗi sở hữu và vận hành):
   use case → specs & evidence → wear & failure → maintenance & diagnostics
   → downtime → lifecycle TCO → repair vs replace decision
```

Các chuỗi này không hoạt động độc lập:
- ADAS chỉ có thể ra lệnh điều khiển cho các cơ cấu chấp hành (actuator) mà hệ thống lái, phanh và động cơ cung cấp.
- Cơ cấu chấp hành chỉ tạo ra được lực trong giới hạn ma sát mà bề mặt tiếp xúc lốp–mặt đường cho phép.
- Hiệu năng duy trì liên tục (sustained capability) bị khóa chặt bởi ngưỡng chịu nhiệt (thermal envelope) của động cơ, pin và phanh.
- Kết quả kinh tế sở hữu phụ thuộc vào tốc độ thoái hóa vật liệu, tính dễ sửa chữa (serviceability) và đúng đắn trong kịch bản sử dụng.

---

## 2. Các nhãn trên xe nằm trên những trục phân loại khác nhau

Một trong những sai lầm phổ biến là đặt các thuật ngữ xe hơi ngang hàng nhau:

```text
SUV          → Kiến trúc thân xe và không gian (body architecture)
AWD          → Phân phối lực tới các bánh (drivetrain)
Hybrid       → Nguồn năng lượng và kiến trúc động lực (energy/powertrain architecture)
400 hp       → Chỉ số công suất cực đại tức thời (output metric)
8-speed      → Đặc tả kiến trúc hộp số (transmission spec)
Level 2      → Phân loại nhiệm vụ hỗ trợ lái tự hành SAE (driving automation taxonomy)
```

Không bao giờ xếp các nhãn trên thành một danh sách lựa chọn duy nhất. Một mẫu xe có thể đồng thời là `SUV` (thân xe), `Hybrid` (nguồn động lực), `AWD` (dẫn động 4 bánh), sở hữu `hộp số 8 cấp` và tính năng `ADAS Level 2`. Mỗi nhãn trả lời cho một câu hỏi kiến trúc hoàn toàn riêng biệt.

---

## 3. Cấu trúc lộ trình học: Hai tầng từ nền tảng đến chuyên sâu

Nhánh Cars được phân thành hai tầng học tập: **Tầng 1** xây dựng mô hình tư duy tổng quan và bài toán chuyển động; **Tầng 2** bóc tách chi tiết từng phân hệ cơ khí, điện tử, nhiệt, an toàn và bài toán tài chính sở hữu.

```text
Cars Knowledge Library
├── Tầng 1: Nền tảng hệ thống & Tổng quan vận hành
│   ├── 00_powertrain_motion_foundations.md (Lực, mô-men, lốp và giới hạn chuyển động)
│   ├── 01_ice_ev_hybrid_and_thermal.md (Nguồn năng lượng, ICE/EV/Hybrid và ranh giới nhiệt)
│   ├── 02_transmission_tires_safety_and_ownership.md (Hộp số, lốp, an toàn và chi phí)
│   └── 03_vehicle_specification_case_lab.md (Case lab đọc specification chọn xe)
│
└── Tầng 2: Chuyên sâu cơ chế & Chi tiết phân hệ
    ├── 01_ice_engine_fundamentals.md (Động cơ đốt trong ICE: chu trình, pít-tông, mô-men/vòng tua)
    ├── 02_hybrid_phev_bev_architecture.md (EV/HEV/PHEV: pin, motor, inverter, phanh tái sinh)
    ├── 03_transmissions_and_reduction_gearing.md (Hộp số: AT, CVT, DCT, e-CVT, final drive, EV reduction)
    ├── 04_drivetrain_differentials_awd_4wd.md (Dẫn động: vi sai mở, LSD, locker, transfer case, torque vectoring)
    ├── 05_tires_traction_and_contact_patch.md (Lốp xe: contact patch, góc trượt, hợp chất, dịch chuyển tải)
    ├── 06_brakes_abs_and_regenerative_braking.md (Phanh: ma sát, ABS, fade, tái sinh và brake blending)
    ├── 07_steering_suspension_and_alignment.md (Lái & treo: hình học lái, lò xo/giảm chấn, under/oversteer, ESC)
    ├── 08_engine_displacement_cylinders_na_turbo.md (Dung tích xilanh, NA vs Turbo, intercooler, kích nổ)
    ├── 09_thermal_management_ice_hybrid_bev.md (Quản lý nhiệt: làm mát, pin cao áp, heat pump, derating)
    ├── 10_safety_adas_perception_control_and_limits.md (An toàn chủ động, ADAS, cảm biến, thuật toán, giới hạn vật lý)
    ├── 11_reading_a_complete_car_spec_sheet.md (Đọc bảng thông số toàn diện: giao thức đo, bằng chứng, ma trận)
    ├── 12_maintenance_diagnostics_and_failure_reasoning.md (Chẩn đoán lỗi: triệu chứng, giả thuyết, OBD/DTC, sửa chữa)
    └── 13_ownership_lifecycle_tco_and_replacement_decisions.md (Vòng đời sở hữu: khấu hao, TCO, sửa vs thay thế)
```

### Tầng 1: Nền tảng hệ thống & Tổng quan vận hành

Tầng này giúp người học nhanh chóng định hình bức tranh toàn cảnh của chiếc xe qua 4 bài học:

1. [`00_powertrain_motion_foundations.md`](00_powertrain_motion_foundations.md) — năng lượng, mô-men xoắn, lực phát động tại mặt lốp và các định luật vật lý giới hạn chuyển động.
2. [`01_ice_ev_hybrid_and_thermal.md`](01_ice_ev_hybrid_and_thermal.md) — so sánh tổng quan giữa động cơ đốt trong (ICE), xe thuần điện (BEV), xe lai (HEV) và xe lai sạc ngoài (PHEV) cùng bài toán giới hạn nhiệt.
3. [`02_transmission_tires_safety_and_ownership.md`](02_transmission_tires_safety_and_ownership.md) — tổng quan về đường truyền lực từ hộp số tới lốp xe, các hệ thống an toàn cốt lõi và khung chi phí sở hữu (TCO).
4. [`03_vehicle_specification_case_lab.md`](03_vehicle_specification_case_lab.md) — phòng thực hành đọc bảng thông số kỹ thuật (spec sheet) để lựa chọn cấu hình xe phù hợp cho một hồ sơ nhu cầu thực tế.

> **Chuyển mạch:** Sau khi đã có nền tảng tổng quan về chuyển động và năng lượng, người học chuyển sang Tầng 2 để bóc tách cặn kẽ cơ chế vật lý và thiết kế kỹ thuật của từng bộ phận bên trong xe.

---

### Tầng 2: Chuyên sâu cơ chế & Chi tiết phân hệ

13 bài học chuyên sâu được thiết kế liền mạch theo dòng chảy từ năng lượng sinh công tới vận hành và kinh tế:

1. [`01_ice_engine_fundamentals.md`](01_ice_engine_fundamentals.md) — combustion → piston/crankshaft → torque/RPM/power: bản chất nhiệt động học của động cơ đốt trong.
2. [`02_hybrid_phev_bev_architecture.md`](02_hybrid_phev_bev_architecture.md) — kiến trúc pin cao áp, motor điện, inverter, thu hồi năng lượng khi phanh (regen) và sự khác biệt giữa các cấu hình Hybrid nối tiếp/song song/hỗn hợp và BEV.
3. [`03_transmissions_and_reduction_gearing.md`](03_transmissions_and_reduction_gearing.md) — các loại hộp số AT (biến mô), CVT (dây đai), DCT (ly hợp kép), e-CVT (hành tinh phân chia công suất) và hộp số giảm tốc đơn cấp trên xe điện.
4. [`04_drivetrain_differentials_awd_4wd.md`](04_drivetrain_differentials_awd_4wd.md) — phân phối mô-men: vi sai mở, vi sai chống trượt (LSD), khóa vi sai cơ khí, hộp số phụ cài cầu 4WD và hệ thống điều hướng mô-men chủ động (torque vectoring).
5. [`05_tires_traction_and_contact_patch.md`](05_tires_traction_and_contact_patch.md) — giao diện duy nhất giữa xe và mặt đường: vệt tiếp xúc, độ đàn hồi hợp chất, góc trượt, vòng tròn ma sát Kamm và sự dịch chuyển tải trọng khi tăng tốc/phanh/vào cua.
6. [`06_brakes_abs_and_regenerative_braking.md`](06_brakes_abs_and_regenerative_braking.md) — phanh ma sát thủy lực, hiện tượng mỏi nhiệt mất phanh (brake fade), thuật toán chống bó cứng ABS/EBD, và cơ chế hòa trộn lực phanh (brake blending) giữa phanh tái sinh và phanh cơ khí.
7. [`07_steering_suspension_and_alignment.md`](07_steering_suspension_and_alignment.md) — hình học bánh xe (toe, camber, caster), góc lái Ackermann, lò xo và giảm xóc thủy lực, hiện tượng thiếu lái (understeer) / thừa lái (oversteer) và vai trò can thiệp của hệ thống cân bằng điện tử ESC.
8. [`08_engine_displacement_cylinders_na_turbo.md`](08_engine_displacement_cylinders_na_turbo.md) — dung tích xi lanh, số xi lanh (I3, I4, V6, V8, Boxer), hiệu suất nạp khí (volumetric efficiency), động cơ hút khí tự nhiên vs Turbo tăng áp, intercooler, hiện tượng kích nổ (knock) và công suất riêng (specific output).
9. [`09_thermal_management_ice_hybrid_bev.md`](09_thermal_management_ice_hybrid_bev.md) — quản lý nhiệt toàn diện: sinh nhiệt, tản nhiệt, két nước/két dầu, làm mát pin cao áp/inverter/motor, bơm nhiệt (heat pump/chiller), điều hòa nhiệt độ pin (preconditioning) và hiện tượng tự hạ công suất bảo vệ (thermal derating).
10. [`10_safety_adas_perception_control_and_limits.md`](10_safety_adas_perception_control_and_limits.md) — an toàn chủ động và hệ thống ADAS: cảnh báo, can thiệp và hỗ trợ lái; cảm biến camera/radar/LiDAR và hợp nhất dữ liệu (sensor fusion); ước lượng/dự đoán quỹ đạo; AEB, ACC, giữ làn; giám sát người lái; thang phân cấp tự hành SAE Level 0-5; hiệu chuẩn, giao diện HMI và giới hạn vật lý.
11. [`11_reading_a_complete_car_spec_sheet.md`](11_reading_a_complete_car_spec_sheet.md) — phương pháp đọc bảng thông số toàn diện: kiến trúc → thông số kỹ thuật → quy chuẩn đo kiểm → bằng chứng thực tế → vòng đời; kích thước/khối lượng, lốp/phanh, pin/sạc/quãng đường, ADAS, khả năng kéo và ma trận so sánh.
12. [`12_maintenance_diagnostics_and_failure_reasoning.md`](12_maintenance_diagnostics_and_failure_reasoning.md) — tư duy chẩn đoán lỗi có phương pháp: triệu chứng chính xác → giả thuyết cạnh tranh → bằng chứng phân biệt → can thiệp kỹ thuật; đọc mã lỗi OBD/DTC, rung động ồn (NVH), quá nhiệt, lỗi phanh, chẩn đoán EV/ADAS và chiến lược bảo dưỡng phòng ngừa.
13. [`13_ownership_lifecycle_tco_and_replacement_decisions.md`](13_ownership_lifecycle_tco_and_replacement_decisions.md) — kinh tế sở hữu xe: khấu hao theo thời gian, chi phí năng lượng/nhiên liệu, hao mòn vật tư, bảo hành, bảo hiểm, bài toán sở hữu EV vs Hybrid, xây dựng kịch bản TCO và mô hình ra quyết định: tiếp tục sửa hay bán xe mua mới.

---

## 4. Một chiếc xe thật được truy vết (system tracing) như thế nào?

Khi quan sát một hiện tượng hoặc đưa ra quyết định về xe, hãy truy vết theo đúng chuỗi cơ chế:

```text
Khi đạp ga tăng tốc
→ Nguồn năng lượng sinh mô-men / tỷ số truyền hộp số / vi sai phân phối lực / độ bám lốp trên mặt đường

Khi phanh gấp hoặc vào cua
→ Phanh ma sát & tái sinh / góc đánh lái / phản ứng hệ thống treo / giới hạn ma sát lốp / ESC can thiệp

Khi nhìn tem động cơ ("2.0T", "V6 3.5", "EV Dual Motor")
→ Dung tích xi lanh / bố trí xilanh / nạp khí tự nhiên hay tăng áp / luồng khí và áp suất nén

Khi hỏi xe có duy trì được sức mạnh liên tục không
→ Nhiệt lượng sinh ra → năng lực tản nhiệt của hệ thống → ngưỡng kích hoạt giảm tải bảo vệ (derating)

Khi nhìn nhãn tính năng ADAS ("Autopilot", "Driving Assistant")
→ Tính năng thuộc cấp độ nào theo SAE → trách nhiệm lái thuộc về ai → cảm biến và cơ cấu chấp hành hỗ trợ

Khi so sánh hai mẫu xe
→ Nhu cầu sử dụng thực tế → ma trận phân hệ kỹ thuật → giao thức thử nghiệm độc lập → trade-off trọn vòng đời

Khi xe xuất hiện hiện tượng lạ (tiếng kêu, rung lắc, đèn báo)
→ Điều kiện vận hành xuất hiện lỗi → các giả thuyết cạnh tranh → bằng chứng phân biệt loại trừ → sửa chữa

Khi quyết định giữ xe cũ hay mua xe mới
→ Chi phí bảo dưỡng và sửa chữa sắp tới + tổn thất thời gian dừng xe + khấu hao + giá trị sử dụng
→ So sánh định lượng với chi phí lăn bánh của phương án mua xe thay thế
```

---

## 5. Kết nối sang Consumer Literacy và các lĩnh vực liên quan

Xe hơi là sản phẩm tiêu dùng phức tạp bậc nhất của đời sống cá nhân. Khi bài toán chuyển từ nguyên lý vận hành sang kỹ năng đọc thông số, đánh giá bảo hành hoặc so sánh chi phí:

- Sử dụng [`../../consumer_literacy/`](../../consumer_literacy/README.md) làm khung tư duy chung:
  - [Specs, Labels & Units](../../consumer_literacy/00_reading_specs_labels_and_units.md) — đọc hiểu công suất, mô-men xoắn, dung tích pin, chu trình đo WLTP/EPA.
  - [Materials, Quality & Durability](../../consumer_literacy/01_materials_quality_and_durability.md) — vật liệu khung thép cường lực/nhôm, ăn mòn gầm, thoái hóa gioăng cao su và linh kiện điện tử.
  - [Reliability, Repairability & Maintenance](../../consumer_literacy/02_reliability_repairability_and_maintenance.md) — các chế độ hỏng hóc, tính sẵn có của phụ tùng, độ phức tạp khi chẩn đoán.
  - [Warranty, Lifecycle & TCO](../../consumer_literacy/03_warranty_lifecycle_and_total_cost.md) — điều khoản loại trừ bảo hành, đường cong khấu hao xe và tính toán TCO.

Ranh giới với các domain học thuật khác:
- Lý thuyết nhiệt động học, chu trình nhiệt, ma sát cơ bản → [`Physics`](../../../physics/README.md).
- Động cơ điện, biến tần inverter, vi mạch điều khiển, pin lithium-ion → [`Electrical Engineering`](../../../electrical_engineering/README.md).
- Thuật toán thị giác máy tính, nhận diện vật thể, mạng nơ-ron ADAS → [`Computer Science`](../../../computer_science/README.md).
- Hạ tầng trạm sạc điện, phân phối xăng dầu, mạng lưới đường cao tốc → [`How Things Work`](../../how_things_work/README.md).
- Vay mua xe, bảo hiểm thân vỏ, quản lý dòng tiền hộ gia đình → `Personal Finance`.
- Tư duy phản biện claims quảng cáo, suy luận nguyên nhân lỗi → `Thinking Toolkit`.

---

## 6. Hướng dẫn đọc theo mục tiêu học tập

- Bắt đầu từ nền tảng chuyển động và lực → [`00_powertrain_motion_foundations.md`](00_powertrain_motion_foundations.md).
- Tìm hiểu sự khác nhau cơ bản giữa xe xăng, hybrid và điện → [`01_ice_ev_hybrid_and_thermal.md`](01_ice_ev_hybrid_and_thermal.md) rồi đào sâu tại [`02_hybrid_phev_bev_architecture.md`](02_hybrid_phev_bev_architecture.md).
- Động cơ đốt trong và mô-men xoắn → [`01_ice_engine_fundamentals.md`](01_ice_engine_fundamentals.md).
- Phân biệt các loại hộp số tự động AT, CVT, DCT → [`03_transmissions_and_reduction_gearing.md`](03_transmissions_and_reduction_gearing.md).
- Hiểu đúng về hệ dẫn động FWD, RWD, AWD, 4WD và vi sai → [`04_drivetrain_differentials_awd_4wd.md`](04_drivetrain_differentials_awd_4wd.md).
- Vai trò quyết định của lốp xe và độ bám đường → [`05_tires_traction_and_contact_patch.md`](05_tires_traction_and_contact_patch.md).
- Cơ chế phanh ma sát, ABS và phanh tái sinh EV → [`06_brakes_abs_and_regenerative_braking.md`](06_brakes_abs_and_regenerative_braking.md).
- Hệ thống lái, treo, góc đặt bánh xe và cân bằng điện tử ESC → [`07_steering_suspension_and_alignment.md`](07_steering_suspension_and_alignment.md).
- Đọc nhãn động cơ, turbo tăng áp, intercooler và kích nổ → [`08_engine_displacement_cylinders_na_turbo.md`](08_engine_displacement_cylinders_na_turbo.md).
- Quản lý nhiệt pin xe điện, bơm nhiệt và hiện tượng sụt công suất → [`09_thermal_management_ice_hybrid_bev.md`](09_thermal_management_ice_hybrid_bev.md).
- Bản chất cảm biến an toàn, tính năng ADAS và giới hạn tự hành → [`10_safety_adas_perception_control_and_limits.md`](10_safety_adas_perception_control_and_limits.md).
- Cách đọc một bảng thông số kỹ thuật xe hơi toàn diện → [`11_reading_a_complete_car_spec_sheet.md`](11_reading_a_complete_car_spec_sheet.md) và thực hành tại [`03_vehicle_specification_case_lab.md`](03_vehicle_specification_case_lab.md).
- Phương pháp chẩn đoán lỗi, đọc mã OBD và chiến lược bảo dưỡng → [`12_maintenance_diagnostics_and_failure_reasoning.md`](12_maintenance_diagnostics_and_failure_reasoning.md).
- Tính toán tổng chi phí sở hữu (TCO) và bài toán sửa tiếp hay mua xe mới → [`13_ownership_lifecycle_tco_and_replacement_decisions.md`](13_ownership_lifecycle_tco_and_replacement_decisions.md).

> **Bàn giao:** Đừng học badge trước system. Đọc một chiếc xe như một chỉnh thể thống nhất của năng lượng + lực truyền + kiểm soát nhiệt + cảm biến điều khiển + bảo dưỡng thực nghiệm + kinh tế vòng đời; chỉ sau khi nắm vững chuỗi mắt xích này, các thông số brochure, lời khuyên sửa chữa và quyết định sở hữu xe mới thực sự có ý nghĩa.
