# Transmission & Reduction Gearing — Vì sao động cơ không nối thẳng vào bánh xe?

Nếu engine hoặc motor đã tạo được torque, câu hỏi tiếp theo là: **vì sao không nối thẳng trục đó vào bánh xe?**

Lý do là power unit và bánh xe hoạt động trong các vùng speed/torque khác nhau. Engine đốt trong thường chỉ làm việc tốt trong một dải RPM hữu hạn; bánh xe lại cần torque rất lớn khi khởi hành và speed cao khi xe chạy nhanh. Transmission (hộp số / 변속기) và reduction gearing (bộ giảm tốc / 감속기) tồn tại để **biến đổi quan hệ giữa tốc độ quay và mô-men**, đồng thời cho phép power unit làm việc trong vùng phù hợp hơn.

Chapter này không coi `AT`, `CVT`, `DCT` hay “8 cấp” là badge. Ta sẽ bắt đầu từ cơ chế.

---

## 1. Gear ratio thực sự làm gì?

Một cặp bánh răng không tạo thêm energy. Nó đổi trade-off giữa torque và rotational speed.

Nếu input quay nhanh hơn output qua một reduction ratio, output nhận torque lớn hơn nhưng quay chậm hơn tương ứng, bỏ qua losses.

Mental model đơn giản:

```text
higher reduction ratio
→ lower output speed
→ higher output torque

lower reduction ratio
→ higher output speed
→ lower torque multiplication
```

Vì vậy một gear thấp giúp xe khởi hành, leo dốc hoặc tăng tốc; gear cao giúp chạy nhanh với engine RPM thấp hơn.

Đây cũng là lý do không thể nhìn engine torque rồi suy ra wheel torque trực tiếp. Wheel torque còn đi qua:

```text
engine / motor torque
× transmission ratio
× final-drive ratio
× driveline efficiency
→ wheel torque
```

Tire radius lại biến wheel torque thành force tại mặt đường.

---

## 2. Vì sao ICE cần nhiều ratio hơn motor điện?

Internal combustion engine có một operating envelope tương đối hẹp.

Ở RPM quá thấp, engine có thể tạo torque yếu hoặc rung/stall; ở RPM quá cao, friction, breathing limit và stress tăng. Fuel efficiency và power peak cũng nằm ở những vùng khác nhau.

Do đó transmission cho phép:

```text
vehicle speed thay đổi rất rộng
while
engine RPM vẫn nằm trong vùng usable
```

Electric motor có đặc tính khác: torque có thể mạnh từ tốc độ thấp và dải speed usable rộng hơn. Vì vậy nhiều BEV chỉ cần **single-speed reduction gear** thay vì gearbox nhiều cấp.

Điều này không có nghĩa transmission “không tồn tại” trên EV. EV vẫn cần reduction/final drive để biến motor speed cao thành wheel speed/torque phù hợp.

Một số EV hiệu năng cao dùng nhiều ratio, nhưng đây là lựa chọn architecture chứ không phải requirement cơ bản của mọi EV.

---

## 3. Manual transmission — baseline dễ hiểu nhất

Manual transmission (수동변속기) dùng các gear ratio cố định và clutch để tách/nối engine với gearbox.

Khi đổi gear:

```text
engine
↕ clutch
gear pair selected
→ output shaft
→ final drive
→ wheels
```

Clutch cho phép engine tiếp tục quay khi xe dừng và cho phép đổi ratio mà không khóa cứng các shaft đang quay ở tốc độ khác nhau.

Manual rất hữu ích làm baseline vì nó tách rõ ba câu hỏi:

1. ratio nào đang được chọn?
2. khi nào engine được disconnect khỏi wheels?
3. ai quyết định đổi ratio?

Các transmission tự động hóa một hoặc nhiều câu hỏi trên theo cách khác nhau.

---

## 4. Torque-converter automatic — “automatic” truyền thống hoạt động thế nào?

Conventional automatic transmission thường kết hợp:

```text
engine
→ torque converter
→ planetary gearsets
→ clutches/brakes
→ output
```

### Torque converter

Torque converter (토크 컨버터) truyền torque qua fluid thay vì một friction clutch đóng trực tiếp ngay từ đầu.

Nó cho phép:

- engine vẫn quay khi xe đứng yên;
- khởi hành êm hơn;
- một mức torque multiplication trong một số condition;
- giảm shock giữa engine và driveline.

Nhưng fluid coupling có slip, nên có energy loss. Vì vậy transmission hiện đại thường dùng **lock-up clutch** khi phù hợp để nối cơ học trực tiếp hơn và giảm loss.

### Planetary gearsets

Planetary gearset cho phép tạo nhiều ratio bằng cách giữ, nối hoặc drive các phần khác nhau của bộ sun–planet–ring.

Người lái không cần hiểu hết kinematic detail để giữ mental model:

> Automatic không “tạo gear bằng phần mềm”. Control system điều khiển clutch/brake để cấu hình gearset thành các ratio khác nhau.

Số cấp nhiều hơn có thể giúp engine ở gần operating zone mong muốn hơn, nhưng `10-speed > 8-speed` không tự động nghĩa tốt hơn. Calibration, ratio spread, shift logic, mass, friction và use case mới quyết định outcome.

---

## 5. CVT — không có các bước ratio cố định theo cách truyền thống

Continuously Variable Transmission (CVT / 무단변속기) thay đổi ratio liên tục trong một range thay vì chỉ chọn một tập gear cố định.

Một kiến trúc phổ biến dùng hai pulley có effective diameter thay đổi và belt/chain nối giữa chúng.

```text
small input radius + large output radius
→ high reduction

large input radius + small output radius
→ low reduction
```

Ưu điểm conceptually:

- engine có thể giữ gần RPM tối ưu cho efficiency hoặc power;
- ratio thay đổi smooth;
- không cần nhiều shift step.

Nhược điểm/trade-off:

- torque capacity và thermal management phụ thuộc design;
- cảm giác engine RPM giữ cao trong khi vehicle speed tăng có thể khác expectation của người lái;
- control calibration ảnh hưởng mạnh cảm nhận;
- durability không thể suy từ chữ `CVT` một mình.

Một số CVT giả lập “gear steps” để tạo familiar feel. Đây là control strategy, không biến hardware thành conventional stepped gearbox.

---

## 6. DCT — hai clutch để chuẩn bị gear kế tiếp

Dual-Clutch Transmission (DCT / 듀얼 클러치 변속기) thường chia gear thành hai đường truyền, mỗi đường có clutch riêng.

Ví dụ đơn giản:

```text
clutch A → gears 1,3,5,7
clutch B → gears 2,4,6
```

Khi xe đang chạy ở gear 3, transmission có thể preselect gear 4 trên shaft còn lại. Shift xảy ra bằng cách giảm engagement clutch A và tăng engagement clutch B.

Điểm mạnh:

- shift nhanh;
- mechanical efficiency cao;
- direct feel.

Trade-off:

- low-speed creeping có thể khó smooth hơn torque-converter system;
- clutch heat/wear quan trọng;
- dry vs wet clutch architecture có trade-off khác nhau;
- calibration rất quan trọng.

Không nên dùng câu “DCT luôn nhanh hơn và tốt hơn automatic”. Performance use case và low-speed daily use có objective khác nhau.

---

## 7. e-CVT trong hybrid có thể không phải CVT pulley-belt

Một nguồn nhầm phổ biến là từ `e-CVT`.

Trong nhiều hybrid power-split, “e-CVT” mô tả khả năng tạo **effective continuously variable ratio** bằng motor/generator + planetary power-split device, chứ không nhất thiết dùng belt-and-pulley CVT.

Mental model:

```text
engine power
├── mechanical path
└── electrical path via motor/generator
        ↓
control combines paths
        ↓
effective ratio changes continuously
```

Do đó cùng chữ “CVT” trên brochure chưa đủ để suy hardware architecture.

Đây là ví dụ điển hình của Consumer Literacy: label cần map về mechanism thực tế.

---

## 8. Final drive — ratio cuối trước bánh xe

Transmission ratio chưa phải ratio cuối cùng. Output thường đi qua final drive/differential trước wheel.

Ví dụ:

```text
engine 3000 rpm
transmission ratio 2.0:1
final drive 4.0:1

→ wheel-side reduction tổng ≈ 8:1
```

Nếu wheel radius không đổi, total reduction lớn hơn nghĩa wheel torque cao hơn nhưng vehicle speed tại cùng engine RPM thấp hơn.

Nhà thiết kế chọn final-drive ratio để cân bằng:

- acceleration;
- top speed;
- cruising RPM;
- efficiency;
- noise;
- towing/load.

---

## 9. Shift logic là một phần của system, không chỉ hardware

Hai xe dùng transmission hardware tương tự vẫn có driving behavior khác vì software/control map khác.

Control system có thể quyết định shift dựa trên:

```text
throttle position
vehicle speed
engine load
brake input
road gradient
temperature
drive mode
battery state (hybrid)
```

Eco mode có thể upshift sớm để hạ RPM; sport mode giữ gear thấp lâu hơn để response nhanh.

Vì vậy “gearbox tốt/xấu” phải tách:

```text
hardware capability
vs
control calibration
vs
condition
```

---

## 10. Gear count không phải quality score

Nhiều gear có thể giúp engine bám target operating zone hơn, nhưng đồng thời tăng:

- number of shift events;
- control complexity;
- packaging/mechanical complexity;
- potential hunting nếu calibration yếu.

Câu hỏi đúng không phải:

> “10 cấp có tốt hơn 8 cấp không?”

Mà là:

```text
ratio spread bao nhiêu?
spacing giữa ratios ra sao?
shift quality thế nào?
engine torque curve cần gì?
cruising RPM ra sao?
use case là city, highway, towing hay performance?
```

---

## 11. Failure / maintenance map

Transmission reliability phụ thuộc architecture và use.

Các layer cần phân biệt:

```text
fluid degradation
clutch wear
hydraulic control
mechatronics / solenoids
bearings/gears
seals
thermal overload
software/calibration
```

Maintenance schedule có thể gồm fluid inspection/replacement tùy manufacturer và transmission type.

Không dùng generic rule như “ATF lifetime nghĩa không bao giờ thay”. `Lifetime` phải đọc theo manufacturer definition, market condition và actual service schedule.

Khi đánh giá một transmission cụ thể, handoff sang [Reliability, Repairability & Maintenance](../../consumer_literacy/02_reliability_repairability_and_maintenance.md).

---

## 12. Comparison framework

Khi gặp hai transmission, không chỉ hỏi tên loại.

| Dimension | Câu hỏi |
|---|---|
| Ratio strategy | fixed steps hay continuously variable? |
| Launch device | dry clutch, wet clutch, torque converter, motor? |
| Efficiency | loss nằm ở đâu? |
| Torque capacity | phù hợp power unit/load không? |
| Low-speed behavior | creeping/parking có smooth không? |
| Thermal load | city traffic/towing ảnh hưởng thế nào? |
| Shift response | nhanh, smooth hay ưu tiên economy? |
| Maintenance | fluid/clutch/service needs? |
| Repairability | module nào thường replace? |
| Control | software calibration ảnh hưởng ra sao? |

---

## 13. Drill — đọc một spec mà không bị badge dẫn dắt

Chọn một xe và ghi:

```text
Power unit:
Transmission type:
Number/range of ratios:
Launch device:
Final drive:
Driven wheels:
Cruising behavior:
Low-speed behavior:
Known thermal/service needs:
What the brochure does NOT tell me:
```

Sau đó mới kết luận transmission đó hợp use case nào.

---

## Connections

- [`01_ice_engine_fundamentals.md`](01_ice_engine_fundamentals.md): engine torque/RPM là input của transmission.
- [`02_hybrid_phev_bev_architecture.md`](02_hybrid_phev_bev_architecture.md): hybrid/electric architecture thay đổi vai trò transmission.
- [`04_drivetrain_differentials_awd_4wd.md`](04_drivetrain_differentials_awd_4wd.md): sau khi ratio được tạo, torque còn phải được phân phối tới các bánh.
- [`../../consumer_literacy/00_reading_specs_labels_and_units.md`](../../consumer_literacy/00_reading_specs_labels_and_units.md): gear count và label không phải total quality.
- [`../../consumer_literacy/02_reliability_repairability_and_maintenance.md`](../../consumer_literacy/02_reliability_repairability_and_maintenance.md): wear, fluid, service và repairability.

Điểm chốt: **transmission không tạo thêm power; nó điều chỉnh nơi power unit làm việc và cách speed–torque được đưa tới bánh xe**. Hiểu nguyên lý này trước, các tên `AT`, `CVT`, `DCT`, `e-CVT` và “single-speed EV” mới trở thành những architecture có thể so sánh thay vì badge để ghi nhớ.
