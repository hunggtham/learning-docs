# Drivetrain, Differentials, AWD & 4WD — Torque đi đến bánh xe như thế nào?

Sau khi transmission đã tạo ratio phù hợp, power vẫn chưa “đến mặt đường”. Torque phải đi qua final drive, differential, driveshaft/axle rồi tới từng bánh. Đây là phần drivetrain (hệ truyền lực / 구동계).

Những nhãn như `FWD`, `RWD`, `AWD`, `4WD`, `LSD`, `locking differential` thường xuất hiện cạnh nhau nhưng trả lời các câu hỏi khác nhau. Chapter này tách chúng theo mechanism.

---

## 1. Drivetrain khác powertrain

Powertrain nói rộng về hệ tạo và truyền power:

```text
energy source
→ engine / motor
→ transmission / reduction
→ drivetrain
```

Drivetrain tập trung vào phần sau transmission: **power được phân phối tới bánh nào và bằng cơ chế gì**.

Vì vậy:

```text
Hybrid ≠ AWD
EV ≠ RWD
SUV ≠ 4WD
```

Một hybrid có thể FWD/AWD; BEV có thể RWD/AWD; SUV có thể chỉ FWD.

---

## 2. FWD — power tới bánh trước

Front-wheel drive (FWD / 전륜구동) dùng bánh trước vừa steer vừa truyền driving force.

Typical compact layout:

```text
engine / motor
→ transmission
→ front differential
→ left/right front axle
```

Ưu điểm thường gặp:

- packaging gọn;
- drivetrain ngắn/lighter;
- cabin space tốt;
- cost/efficiency phù hợp mass-market.

Trade-off:

- front tires phải chia traction budget cho steering + acceleration;
- high power có thể làm torque steer hoặc traction limit rõ hơn;
- weight transfer khi acceleration chuyển load về rear, không có lợi cho driven front wheels.

Không nên biến các trade-off này thành “FWD kém”. Với daily use và moderate power, simplicity/package efficiency có thể là objective quan trọng hơn.

---

## 3. RWD — steering và driving force được tách nhiều hơn

Rear-wheel drive (RWD / 후륜구동) đưa torque tới bánh sau.

Với front-engine layout truyền thống:

```text
engine
→ transmission
→ prop shaft
→ rear differential
→ rear wheels
```

Ưu điểm architecture:

- front wheels tập trung nhiều hơn vào steering;
- acceleration weight transfer tăng load lên driven rear tires;
- dễ phân bố power cao hơn trong nhiều performance applications.

Trade-off:

- packaging/weight có thể tăng;
- prop shaft/tunnel/differential chiếm space;
- low-grip behavior khác FWD và đòi hỏi stability control/driver input phù hợp.

BEV có thể RWD rất dễ vì motor có thể đặt trực tiếp gần rear axle; không cần long prop shaft như ICE layout truyền thống.

---

## 4. Vì sao cần differential?

Khi xe quay, bánh phía ngoài cua đi quãng đường dài hơn bánh phía trong.

Nếu hai bánh cùng axle bị khóa quay cùng speed mọi lúc:

```text
outer wheel needs faster speed
but locked axle forces same speed
→ tire scrub / stress / poor turning
```

Differential (vi sai / 디퍼렌셜) cho phép hai wheel quay ở tốc độ khác nhau trong khi vẫn truyền torque.

Đây là function cơ bản. Nhưng cách differential chia torque khi traction khác nhau tạo ra nhiều architecture tiếp theo.

---

## 5. Open differential — đơn giản nhưng có traction limitation

Open differential hoạt động tốt khi hai bánh có grip tương tự.

Vấn đề xuất hiện khi một wheel ở bề mặt rất trơn và wheel kia có grip cao. Trong simplified mental model, torque truyền qua open diff bị giới hạn bởi phía có khả năng chịu torque thấp hơn.

Kết quả quen thuộc:

```text
one wheel spins
other wheel has grip
but vehicle struggles to move
```

Đây không phải vì differential “gửi toàn bộ power sang wheel trơn” theo một ý chí nào đó. Nó là hệ quả của torque balance trong open-diff mechanism.

Traction control có thể can thiệp bằng brake wheel đang spin để tạo resistance, giúp hệ truyền nhiều usable torque hơn sang phía còn lại.

---

## 6. Limited-slip differential — hạn chế speed/torque difference

Limited-slip differential (LSD / 차동 제한 장치) giảm mức tự do của open diff khi hai wheel có traction khác nhau.

Có nhiều cơ chế:

- clutch-type;
- helical/Torsen-type;
- viscous;
- electronically controlled clutch.

Không nên học tất cả bằng một câu “LSD truyền lực sang bánh có độ bám”. Câu chính xác hơn:

> LSD tạo coupling/bias giữa hai output để hạn chế tình trạng một wheel nhận điều kiện spin quá dễ so với wheel còn lại.

Trade-off gồm:

- cost;
- heat;
- wear;
- behavior khi cornering;
- calibration.

---

## 7. Locking differential — khóa hai output lại

Differential lock khóa left/right output gần như cùng speed.

Điều này rất hữu ích khi off-road hoặc một wheel mất traction nghiêm trọng.

Nhưng trên high-grip surface khi quay cua, lock tạo driveline wind-up/tire scrub vì wheel cần speed khác nhau.

Vì vậy locker không phải “LSD mạnh hơn nên luôn tốt hơn”. Nó phù hợp một operating regime khác.

---

## 8. AWD — một family rộng, không phải một mechanism duy nhất

All-wheel drive (AWD / 상시사륜 또는 전자식 사륜 등) nói rằng system có thể drive cả front và rear axles, nhưng cách làm khác nhau rất nhiều.

Một số architecture:

### Mechanical full-time AWD

```text
engine
→ transmission
→ center differential
├── front axle
└── rear axle
```

Center differential cho front/rear axle quay khác speed khi cornering.

### On-demand AWD

Base vehicle có thể chủ yếu drive một axle. Clutch coupling engage axle còn lại khi system dự đoán/phát hiện slip hoặc cần performance.

```text
primary axle
+
controlled coupling
→ secondary axle when needed
```

### Electric AWD

Hybrid/BEV có thể dùng motor riêng cho axle sau mà không cần mechanical driveshaft nối front–rear.

```text
front motor / engine path
+
rear motor
→ software coordinates torque
```

Đây là ví dụ architecture điện hóa làm thay đổi drivetrain topology.

---

## 9. 4WD thường nhấn mạnh off-road/load architecture

`4WD` và `AWD` không có một boundary kỹ thuật toàn cầu duy nhất trong marketing, nhưng trong thực tế 4WD thường gắn với truck/off-road architecture có transfer case và khả năng khóa/low range mạnh hơn.

Typical part-time 4WD:

```text
engine
→ transmission
→ transfer case
├── front axle
└── rear axle
```

### High range vs low range

Low range thêm reduction lớn:

```text
vehicle speed lower
wheel torque higher
control at crawl speed better
```

Nó hữu ích cho steep terrain, rocks, heavy load hơn là highway cruising.

### Part-time 4WD trên dry pavement

Nếu system khóa front/rear output mà không có center differential, front/rear axles không thể tự bù speed difference khi cornering.

Dùng trên high-grip dry pavement có thể gây driveline bind/wind-up.

Vì vậy “4H dùng lúc nào” phụ thuộc architecture cụ thể; không áp một rule marketing chung cho mọi vehicle.

---

## 10. AWD không tạo thêm total tire grip từ hư không

AWD có thể cải thiện **acceleration traction** vì drive force được phân phối qua nhiều tires.

Nhưng khi braking:

```text
all cars already brake with all four wheels
```

AWD không tự rút ngắn braking distance chỉ vì có bốn bánh chủ động.

Braking/cornering grip phụ thuộc mạnh vào tires, road, load transfer và ABS/ESC.

Đây là một misunderstanding rất quan trọng trong snow/wet conditions:

> AWD giúp xe đi được dễ hơn; tires thường quyết định mạnh khả năng dừng và đổi hướng.

Chapter tiếp theo về tires sẽ giải thích điều này.

---

## 11. Torque vectoring — không chỉ “chia 50:50”

Modern systems có thể điều khiển torque từng axle hoặc từng wheel.

Torque vectoring có thể dùng:

- clutch packs;
- brake intervention;
- multiple electric motors.

Mục tiêu có thể là:

- traction;
- yaw response;
- stability;
- efficiency.

Do đó ratio `50:50`, `40:60` trên brochure không phải toàn bộ behavior. Dynamic system có thể thay đổi distribution theo condition.

---

## 12. Weight transfer và traction

Khi acceleration, load chuyển về rear; khi braking, load chuyển về front.

Điều này không thay total vehicle weight nhưng thay normal force từng axle, từ đó ảnh hưởng maximum tire force.

Simplified:

```text
acceleration
→ rear axle load ↑
→ front axle load ↓
```

Vì vậy layout driven wheels tương tác với:

- center of gravity;
- wheelbase;
- acceleration level;
- suspension geometry;
- tire grip.

Không thể đánh giá drivetrain chỉ bằng số wheel driven.

---

## 13. Efficiency / complexity trade-off

Driving more axles thường cần thêm:

- shafts/gears/clutches hoặc motors;
- bearings;
- oil;
- mass;
- control system.

Điều đó có thể tăng parasitic loss và maintenance surface.

Modern systems giảm loss bằng disconnect clutches hoặc electric architecture, nhưng principle vẫn là:

```text
more capability
usually
→ more hardware/control complexity
```

Capability chỉ có value nếu use case cần nó.

---

## 14. Failure / maintenance map

Drivetrain có nhiều failure modes:

```text
CV joints / boots
wheel bearings
prop shaft joints
transfer-case fluid
clutch coupling
axle seals
differential oil
mounts
sensors / actuators
```

Symptom có thể là noise/vibration/leak/binding nhưng diagnosis cần phân biệt load, speed, steering angle và temperature.

Handoff generic maintenance reasoning sang [Reliability, Repairability & Maintenance](../../consumer_literacy/02_reliability_repairability_and_maintenance.md).

---

## 15. Comparison framework

Khi đọc drivetrain spec:

```text
Which wheels can receive torque?
Always or on-demand?
Mechanical or electric connection?
Center differential or clutch coupling?
Open / LSD / locker at each axle?
Low range available?
Can axles disconnect for efficiency?
How is torque vectoring implemented?
What happens on high-grip turns?
What service items exist?
```

Đây hữu ích hơn câu “AWD tốt hơn FWD bao nhiêu?”.

---

## 16. Drill — vẽ torque path

Chọn một xe FWD, một AWD và một BEV dual-motor.

Vẽ:

```text
energy source
→ power unit
→ transmission/reduction
→ coupling/differential
→ axle
→ wheel
```

Sau đó đánh dấu:

- component nào thay ratio;
- component nào cho speed difference;
- component nào có thể lock/bias torque;
- component nào software-controlled;
- failure point chính.

Nếu không vẽ được torque path, label `AWD` vẫn còn quá abstract.

---

## Connections

- [`03_transmissions_and_reduction_gearing.md`](03_transmissions_and_reduction_gearing.md): tạo speed/torque ratio trước drivetrain.
- [`05_tires_traction_and_contact_patch.md`](05_tires_traction_and_contact_patch.md): drivetrain chỉ hữu ích khi tire có thể truyền force xuống road.
- [`02_hybrid_phev_bev_architecture.md`](02_hybrid_phev_bev_architecture.md): electric axle và dual-motor AWD.
- [`../../consumer_literacy/02_reliability_repairability_and_maintenance.md`](../../consumer_literacy/02_reliability_repairability_and_maintenance.md): complexity, failure và service.

Điểm chốt: **FWD/RWD/AWD/4WD mô tả torque path, không mô tả toàn bộ traction hay safety**. Differential, coupling, control system và đặc biệt tires mới quyết định xe biến torque thành motion như thế nào trong từng condition.
