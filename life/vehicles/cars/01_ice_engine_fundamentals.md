# ICE Fundamentals — Động cơ đốt trong biến nhiên liệu thành chuyển động như thế nào?

Cars README đã cho ta system map `energy source → power unit → drivetrain → wheels`. Chapter này zoom vào power unit của xe dùng động cơ đốt trong (internal combustion engine, ICE / 내연기관): **nhiên liệu chứa năng lượng hóa học; động cơ phải chuyển một phần năng lượng đó thành công cơ học quay ở trục khuỷu**.

Mục tiêu không phải thuộc mọi loại động cơ. Ta cần một mental model đủ mạnh để sau này hiểu displacement, cylinder count, naturally aspirated, turbocharger, diesel, RPM, torque, power và efficiency mà không coi chúng là các badge marketing rời nhau.

## 1. Động cơ không “tạo” năng lượng

Nhiên liệu chứa năng lượng hóa học. Quá trình cháy giải phóng năng lượng, làm khí trong cylinder đạt nhiệt độ và áp suất cao. Áp suất tác dụng lên piston, piston truyền lực qua connecting rod để làm crankshaft quay.

Chuỗi tối giản:

```text
chemical energy in fuel
→ combustion
→ hot high-pressure gas
→ piston force
→ connecting rod
→ crankshaft rotation
```

Động cơ vì vậy là một energy-conversion machine. Nó không thể biến 100% năng lượng nhiên liệu thành wheel power: một phần đi vào exhaust heat, cooling system, friction, pumping loss và accessories.

Formal thermodynamics thuộc Physics/Engineering; ở đây ta chỉ giữ consequence thực dụng: **fuel consumed không tỷ lệ hoàn hảo với useful work vì conversion efficiency thay đổi theo operating point**.

## 2. Bốn kỳ của động cơ xăng phổ biến

Một four-stroke engine thường đi qua:

```text
intake
→ compression
→ power/combustion
→ exhaust
```

### Intake

Piston đi xuống, cylinder nhận air hoặc air–fuel mixture tùy architecture.

### Compression

Piston đi lên, hỗn hợp/không khí bị nén. Compression làm điều kiện trước combustion thay đổi.

### Power

Combustion làm pressure tăng, đẩy piston xuống và tạo work hữu ích lên crankshaft.

### Exhaust

Khí cháy được đẩy ra để cycle có thể bắt đầu lại.

Điểm cần giữ không phải tên bốn kỳ mà là một cylinder **không tạo power liên tục ở mọi thời điểm**. Multi-cylinder engines sắp xếp cycles lệch nhau để torque delivery mượt hơn.

## 3. Cylinder count nói gì?

Cylinder count ảnh hưởng packaging, smoothness, potential airflow/displacement, friction, weight, cost và character, nhưng không phải direct ranking của power.

Một 4-cylinder turbo hiện đại có thể tạo nhiều power hơn một engine nhiều cylinder cũ hoặc tuned cho objective khác.

Do đó:

```text
more cylinders
≠ automatically more powerful
≠ automatically better
```

Cần đọc cùng displacement, boost, RPM range, tuning, efficiency và vehicle mass.

## 4. Displacement là volume geometry, không phải “sức mạnh”

Engine displacement (dung tích động cơ / 배기량) liên quan tổng swept volume của piston qua các cylinder.

Intuition:

```text
larger cylinder volume
× number of cylinders
→ larger total displacement
```

Displacement cho biết quy mô geometric của engine, nhưng power còn phụ thuộc lượng air/fuel thực sự được xử lý theo thời gian và efficiency.

Hai engine 2.0 L có thể khác rất xa vì:

- naturally aspirated vs turbo;
- RPM capability;
- valve timing;
- compression ratio;
- combustion/control strategy;
- intake/exhaust restriction.

Vì vậy displacement là một **input architecture**, không phải output performance score.

## 5. Vì sao động cơ cần air?

Combustion cần oxygen. Với engine, airflow là một constraint quan trọng: muốn đốt nhiều fuel hiệu quả hơn, thường phải đưa đủ air vào cylinder.

Điều này giải thích vì sao intake, valves, cam timing, turbocharger/supercharger và exhaust flow đều liên quan power.

Một cách nghĩ hữu ích:

```text
power potential
~ how much useful combustion can happen per unit time
```

Không dùng expression này như formula chính xác; nó chỉ cho thấy vì sao engine breathing quan trọng.

## 6. Naturally aspirated và forced induction

Naturally aspirated engine (NA / 자연흡기 엔진) chủ yếu dựa vào pressure difference tạo bởi piston/intake dynamics để cylinder nhận air.

Forced induction dùng compressor để đưa air vào với pressure cao hơn. Turbocharger (터보차저) dùng energy trong exhaust flow để drive turbine nối với compressor; supercharger thường lấy mechanical power trực tiếp từ engine hoặc architecture khác.

Mental model turbo:

```text
exhaust energy
→ turbine
→ shaft
→ compressor
→ denser intake charge
→ more oxygen available
→ more fuel can be burned under control
→ higher torque/power potential
```

Turbo không tạo energy miễn phí. Nó tận dụng exhaust energy nhưng hệ thống có thermal load, backpressure, control, lubrication và response trade-offs.

## 7. Turbo lag và transient response

Một turbo cần exhaust flow/shaft speed để tạo boost. Vì thế response có thể không tức thời ở mọi operating condition.

“Turbo lag” không chỉ là một con số cố định; response phụ thuộc:

- turbo size/inertia;
- engine speed/load;
- exhaust energy;
- gearing;
- control strategy;
- hybrid/electric assist ở một số architecture.

Design trade-off thường là:

```text
large airflow capacity at high output
vs
fast response at low flow
```

Modern systems dùng nhiều kỹ thuật để giảm trade-off nhưng không xóa physics.

## 8. Torque và power gặp nhau ở crankshaft

Torque là twisting effect ở shaft. Power cho biết rate of doing work.

Trong rotating system:

```text
Power = Torque × Angular speed
```

Không cần nhớ conversion constant cụ thể để hiểu consequence:

- cùng torque ở RPM cao hơn → power cao hơn;
- engine có peak torque lớn không tự động có peak power lớn nhất;
- gearbox có thể đổi torque/speed ở wheels nhưng không tạo thêm energy lý tưởng.

Vì vậy cảm giác acceleration phụ thuộc toàn system, không chỉ engine torque headline.

## 9. RPM là operating state, không phải quality metric

RPM (revolutions per minute / 분당 회전수) cho biết crankshaft quay nhanh thế nào.

Engine có torque curve theo RPM. Một engine có thể mạnh ở low RPM, engine khác cần rev cao hơn để đạt power.

Redline cao không tự động tốt; low-RPM torque cao cũng không tự động tốt. Vehicle use case, gearing, noise, efficiency và durability đều matter.

## 10. Gasoline và diesel khác nhau ở combustion strategy

Gasoline spark-ignition engine thường dùng spark plug để initiate combustion của prepared mixture/charge.

Diesel compression-ignition engine dựa vào high compression làm air nóng lên rồi fuel injection tạo combustion theo strategy tương ứng.

Sự khác biệt kéo theo design khác về:

- compression;
- injection pressure;
- torque characteristics;
- emissions control;
- component loading;
- efficiency behavior.

Không rút gọn thành “diesel mạnh hơn” hay “gasoline nhanh hơn”; đó là stereotype không đủ context.

## 11. Compression ratio nói gì?

Compression ratio mô tả ratio giữa cylinder volume lớn nhất và nhỏ nhất trong cycle geometry.

Nó liên quan thermodynamic behavior và combustion constraints, nhưng không phải một knob “càng cao càng tốt”. Fuel characteristics, knock tendency, boost, combustion design và emissions requirements cùng giới hạn lựa chọn.

Một spec compression ratio chỉ có meaning khi đặt trong engine architecture.

## 12. Knock và vì sao combustion timing quan trọng

Combustion cần diễn ra có kiểm soát. Nếu phần charge tự bốc cháy không đúng cách hoặc pressure rise không như design, knock/detonation có thể tạo stress và giảm performance/control margin.

Modern engine dùng sensors và control để điều chỉnh ignition, boost, fueling và nhiều variables.

Điểm cần giữ: **engine performance hiện đại là mechanical + thermal + electronic control system**, không chỉ hardware piston/cylinder.

## 13. Cooling và lubrication không phải subsystem phụ

Combustion tạo heat lớn; moving parts tạo friction. Vì vậy engine cần:

- cooling system để giữ temperature trong operating range;
- lubrication để giảm friction/wear và hỗ trợ heat management ở nhiều component.

Nếu cooling/lubrication fail, engine có thể damage dù combustion architecture ban đầu tốt.

Đây là bridge sang Consumer Literacy: durability phụ thuộc material + thermal cycles + lubrication + maintenance, không chỉ engine badge.

## 14. Efficiency thay đổi theo operating point

Engine không có một efficiency duy nhất trong mọi tình huống.

Low load, high load, cold start, cruising, acceleration, RPM khác nhau tạo losses và combustion conditions khác nhau.

Vì vậy official fuel-economy cycle là measurement theo protocol, không phải guarantee consumption của mọi driver.

Handoff sang [`../../consumer_literacy/00_reading_specs_labels_and_units.md`](../../consumer_literacy/00_reading_specs_labels_and_units.md) để đọc test-cycle metric đúng boundary.

## 15. Vì sao engine nhỏ turbo có thể thay engine lớn NA?

Một engine displacement nhỏ hơn có thể dùng boost để đưa nhiều air vào khi cần, trong khi ở một số operating point giảm pumping/friction/size-related losses so với architecture lớn hơn. Nhưng outcome thực phụ thuộc design và driving cycle.

Do đó downsizing + turbo là trade-off system:

```text
size/weight/efficiency opportunities
vs
thermal load/complexity/boost dependence/response
```

Không nên kết luận từ displacement một mình rằng engine “yếu” hoặc “tiết kiệm”.

## 16. Engine spec sheet nên đọc theo route nào?

Khi gặp:

```text
2.0 L turbo
4 cylinder
250 hp
350 Nm
6500 rpm redline
compression ratio X
```

đọc theo dependency:

```text
architecture
→ airflow/boost
→ torque curve
→ RPM
→ power
→ gearbox
→ vehicle mass/traction
```

Không xếp từng spec thành điểm cộng độc lập.

## 17. Maintenance và wear

ICE có nhiều component chịu:

- heat cycles;
- friction;
- pressure;
- contamination;
- vibration;
- chemical degradation.

Oil, coolant, filters, ignition/fuel-system components và belts/chains tùy architecture đều có maintenance logic riêng.

Nhưng interval cụ thể là manufacturer/model-specific và có thể time-sensitive; Life Knowledge không hard-code một lịch bảo dưỡng chung cho mọi xe.

Mental model:

```text
maintenance item
→ failure mode prevented/monitored
→ interval/condition defined by actual system
```

## 18. Common misconceptions

### “2.0L luôn mạnh hơn 1.6L”

Sai vì displacement không chứa boost/RPM/efficiency/tuning.

### “Torque = acceleration”

Thiếu gearing, wheel torque, speed, mass và traction.

### “Turbo tạo power miễn phí”

Turbo tận dụng exhaust energy nhưng mang thermal/control/backpressure/complexity trade-offs.

### “Horsepower cao = xe nhanh hơn trong mọi tình huống”

Vehicle performance còn phụ thuộc mass, gearing, traction, aero và response.

### “Engine tốt thì xe bền”

Vehicle reliability là system property; transmission, cooling, electronics, seals, suspension và maintenance cũng matter.

## 19. Mental model cần giữ lại

```text
fuel
+ air
→ controlled combustion
→ cylinder pressure
→ piston force
→ crankshaft torque
× rotational speed
→ power
→ transmission/drivetrain
→ wheel force
```

Mỗi spec mới nên được đặt vào chuỗi trên thay vì học riêng.

## Đọc tiếp

Sau khi hiểu ICE như energy converter, bước hợp lý tiếp theo là đối chiếu [Hybrid / PHEV / BEV architecture] — nơi battery, motor, inverter, regenerative braking và control strategy thay đổi route năng lượng. Song song, transmission chapter sẽ giải thích tại sao crankshaft output chưa phải wheel output.

## Connections

- [`README.md`](README.md): system map toàn Cars.
- [`../../consumer_literacy/00_reading_specs_labels_and_units.md`](../../consumer_literacy/00_reading_specs_labels_and_units.md): đọc displacement, power, torque và economy metrics đúng scope.
- [`../../consumer_literacy/01_materials_quality_and_durability.md`](../../consumer_literacy/01_materials_quality_and_durability.md): heat, wear, interfaces và maintenance.
- Physics/Chemistry: thermodynamics, combustion và mechanics sâu hơn.
- Electrical Engineering: control, sensors, motor/inverter ở hybrid/EV.

Chapter này không nhằm biến người đọc thành engine designer. Nó cung cấp dependency map đủ để khi gặp một spec hoặc marketing claim mới, người đọc có thể hỏi: **nó tác động vào mắt xích nào của energy → torque → power → wheel force, và trade-off nằm ở đâu?**