# Car Maintenance & Diagnostic Reasoning — từ triệu chứng đến bằng chứng

Một chiếc xe có thể báo cùng một triệu chứng từ nhiều nguyên nhân khác nhau. `rung`, `ồn`, `nóng`, `hao xăng`, `check engine`, `phanh kêu`, `lệch lái` hay `sạc chậm` không phải diagnosis; chúng chỉ là **observations**.

Chapter này không phải repair manual. Mục tiêu là xây một workflow để:

```text
symptom
→ define operating conditions
→ identify affected system
→ generate competing hypotheses
→ rank by plausibility + severity
→ collect discriminating evidence
→ isolate subsystem
→ decide monitor / maintain / repair / escalate
```

Cách này nối trực tiếp Cars system map với [Reliability, Repairability & Maintenance](../../consumer_literacy/02_reliability_repairability_and_maintenance.md) và Thinking/causal reasoning.

---

## 1. Maintenance khác diagnostics ở câu hỏi

**Maintenance** hỏi:

> Ta nên làm gì trước khi hoặc khi wear/failure xảy ra để giữ hệ thống trong trạng thái làm việc?

**Diagnostics** hỏi:

> Với một symptom cụ thể, bằng chứng nào giúp phân biệt các nguyên nhân cạnh tranh?

Ví dụ:

```text
maintenance question
→ khi nào nên kiểm tra/đổi brake fluid?

diagnostic question
→ pedal mềm là do air, fluid degradation, leak, hose expansion hay master cylinder?
```

Không nên dùng maintenance schedule như diagnosis và cũng không nên thay part theo kiểu thử-và-sai nếu chưa có evidence.

---

## 2. Bắt đầu bằng symptom definition, không bằng tên part

Một symptom tốt phải trả lời:

```text
WHAT   — cái gì đang bất thường?
WHEN   — khi lạnh/nóng, idle/load, low/high speed?
WHERE  — front/rear, left/right, engine bay/cabin/wheel?
HOW    — steady/intermittent, vibration/noise/temperature/response?
TREND  — mới xuất hiện, tăng dần, sau service, sau va chạm?
TRIGGER— braking, acceleration, turning, bumps, charging?
```

Ví dụ kém:

> Xe rung.

Ví dụ tốt hơn:

> Rung xuất hiện 90–110 km/h, rõ ở steering wheel, gần như không phụ thuộc engine RPM và không xảy ra khi xe đứng yên rev engine.

Chỉ riêng framing này đã làm giảm rất nhiều hypothesis không phù hợp.

---

## 3. Phân biệt symptom, mechanism và root cause

```text
symptom
→ cái người dùng quan sát

mechanism
→ quá trình vật lý/điện/control trực tiếp tạo symptom

root cause
→ điều kiện/thành phần gây mechanism đó
```

Ví dụ:

```text
symptom: engine temperature warning
mechanism: heat rejection < heat generation
possible root causes:
- coolant low / leak
- thermostat stuck
- water pump issue
- radiator airflow restriction
- fan/control fault
- extreme load + ambient condition
```

`overheating` chưa phải root cause.

---

## 4. Chẩn đoán bằng competing hypotheses

Đừng hỏi:

> “Có phải wheel bearing không?”

Hãy viết:

```text
H1 tire/wheel imbalance
H2 wheel/tire deformation
H3 alignment/suspension issue
H4 wheel bearing
H5 driveline-related vibration
```

Sau đó hỏi:

> Observation nào có khả năng khác nhau nhất giữa H1, H2, H3...?

Đây là **discriminating evidence**.

Ví dụ:

```text
vibration tied to vehicle speed
but not engine RPM
→ weakens engine-side hypothesis

changes strongly with steering load
→ raises bearing/tire/suspension candidates

appears after tire replacement
→ raises wheel balance / installation candidates
```

Không có một clue riêng lẻ nào cần được coi là proof.

---

## 5. Bayes intuition trong diagnostics

Không cần tính xác suất chính xác để dùng Bayesian reasoning.

```text
posterior plausibility
≈ prior plausibility
× how expected this evidence is under hypothesis
```

Nói đời thường:

- lỗi phổ biến bắt đầu với prior cao hơn;
- một dấu hiệu rất đặc hiệu có thể đảo thứ tự;
- một dấu hiệu mơ hồ chỉ nên update nhẹ.

Ví dụ:

```text
car pulls after tire service
```

Có thể ưu tiên kiểm tra pressure, tire/wheel condition, alignment-related causes trước một failure hiếm của steering rack nếu không có evidence bổ sung.

Nhưng severity phải được xem riêng với probability:

```text
low probability + catastrophic consequence
→ still worth urgent exclusion
```

---

## 6. Severity triage trước detailed diagnosis

Trước khi tối ưu chẩn đoán, hỏi:

```text
Có unsafe condition không?
Có nguy cơ tạo secondary damage không?
Có fluid leak / smoke / overheating / brake loss / severe steering issue không?
Có high-voltage warning trên HEV/BEV không?
```

Một practical triage:

### Stop / escalate immediately

Ví dụ:

- mất braking authority;
- severe steering loss;
- engine oil-pressure warning;
- major coolant overheat;
- fuel leak/smell mạnh;
- smoke/fire indication;
- tire sidewall/bulge/severe damage;
- high-voltage isolation/thermal warning nghiêm trọng.

### Drive minimally / inspect soon

Ví dụ:

- wheel bearing noise tăng nhanh;
- recurring misfire;
- brake vibration mạnh;
- cooling system loss nhỏ nhưng có trend;
- charging thermal limitation bất thường.

### Monitor / scheduled maintenance

Ví dụ:

- wear trend đã biết;
- cosmetic noise không tăng;
- non-safety convenience feature.

Triage không thay diagnosis; nó quyết định **urgency**.

---

# 7. Maintenance theo failure mechanism

Calendar/mileage chỉ là proxy. Hiểu tốt hơn bằng:

```text
component
→ stress/load
→ degradation mechanism
→ inspection signal
→ intervention
```

## Engine oil

Oil phải:

- lubricate;
- carry heat;
- suspend contaminants;
- support hydraulic functions ở một số systems;
- protect surfaces.

Degradation chịu ảnh hưởng bởi:

```text
temperature
+ oxidation
+ contamination
+ fuel dilution
+ soot/by-products
+ additive depletion
+ operating cycle
```

Short trips có thể khác long highway operation dù mileage giống nhau.

## Coolant

Coolant không chỉ “nước làm mát”. Nó liên quan:

- freezing/boiling protection;
- corrosion inhibition;
- material compatibility;
- pump/seal environment.

Vì vậy topping-up sai fluid hoặc chỉ nhìn màu có thể gây false confidence.

## Brake fluid

Brake fluid có thể hấp thụ moisture tùy chemistry/system, làm thay đổi boiling performance. Vì vậy brake pad thickness không đại diện toàn bộ braking maintenance.

## Tires

Wear phụ thuộc:

```text
pressure
+ load
+ alignment
+ compound
+ temperature
+ driving style
+ road surface
```

Uneven wear là **diagnostic evidence**, không chỉ cosmetic problem.

## 12V battery

Ngay cả HEV/BEV vẫn thường có low-voltage architecture cho control/boot/wake functions. Một weak 12V battery có thể tạo symptoms tưởng như unrelated electronics fault.

---

# 8. OBD/DTC: code là clue, không phải part order

DTC — **Diagnostic Trouble Code** (진단 고장 코드) thường cho biết controller phát hiện một condition ngoài expectation.

Nó không nhất thiết nói:

```text
“hãy thay component X”
```

Ví dụ generic:

```text
mixture too lean
```

có thể liên quan tới:

- unmetered air;
- fuel delivery;
- sensor bias;
- exhaust leak ảnh hưởng measurement;
- control/adaptation limits.

Workflow tốt:

```text
read code
→ record freeze-frame / context
→ map code to monitored variable/system
→ build hypotheses
→ inspect live data / physical evidence
→ test before replacing
```

### Freeze frame và live data

Context hữu ích:

- RPM;
- load;
- coolant temperature;
- vehicle speed;
- fuel trims;
- sensor values;
- battery voltage;
- event timing.

Một code khi cold start khác một code chỉ xuất hiện high-load.

---

# 9. Sensor data phải hiểu theo chain measurement

Mỗi sensor reading có thể sai vì:

```text
true physical state
→ sensor
→ wiring/power/ground
→ signal conditioning
→ ECU interpretation
→ displayed/logged value
```

Do đó:

```text
implausible reading
≠ automatically bad sensor
```

Có thể là:

- connector;
- reference voltage;
- ground;
- wiring resistance/open/short;
- contamination;
- calibration;
- actual physical abnormality.

Diagnostic reasoning phải tách **measurement failure** khỏi **measured-system failure**.

---

# 10. Noise, vibration, harshness — NVH như evidence

NVH có thể được phân loại theo frequency/source coupling.

Hãy hỏi symptom scale với gì:

```text
engine RPM?
vehicle speed?
wheel speed?
braking force?
steering angle?
road roughness?
gear/load state?
```

Ví dụ:

### Scale với engine RPM khi xe đứng yên

Tăng suspicion ở:

- engine/accessory;
- mount;
- exhaust/contact;
- rotating engine-side part.

### Scale với vehicle speed nhưng không RPM

Tăng suspicion ở:

- tire/wheel;
- wheel bearing;
- driveline;
- aero/body interaction.

### Chỉ khi braking

Tăng suspicion ở:

- rotor/friction variation;
- pad/caliper;
- suspension compliance under brake load;
- ABS intervention in certain cases.

Đây là cách dùng **coupling variable** để phân biệt hypotheses.

---

# 11. Steering pull, wandering và uneven tire wear

Một xe kéo lệch không tự động là “alignment”.

Hypotheses có thể gồm:

```text
left/right tire pressure difference
→ tire construction/wear difference
→ road crown
→ brake drag
→ alignment geometry
→ suspension damage/bushing compliance
→ steering sensor/control issue
```

Evidence tốt:

- pressure measured cold;
- tire wear pattern;
- swap test nếu phù hợp và an toàn;
- brake temperature difference;
- alignment measurement;
- post-impact history.

Điểm chính:

> alignment number là measurement của geometry, không phải diagnosis toàn bộ steering problem.

---

# 12. Brake diagnostics: friction, hydraulics, control và thermal

Một brake complaint có thể nằm ở bốn layer:

```text
friction hardware
hydraulics
control electronics
thermal state
```

### Pedal pulsation / steering shake khi phanh

Có thể cần phân biệt:

- friction/rotor thickness variation;
- wheel/tire/suspension interaction;
- ABS activation;
- installation/runout related issues.

### Pedal mềm

Cần nghĩ về hydraulic compliance/air/leak/fluid/system state, không chỉ pads.

### Brake fade

```text
repeated energy conversion
→ heat accumulation
→ friction/fluid operating limit
→ reduced braking response
```

Nó nối trực tiếp chapter [Brakes](06_brakes_abs_and_regenerative_braking.md) với [Thermal Management](09_thermal_management_ice_hybrid_bev.md).

---

# 13. Engine performance diagnostics

Một complaint “xe yếu” cần operationalize:

```text
weak at low RPM?
weak only high load?
slow throttle response?
boost missing?
fuel economy worse?
misfire?
heat-soak related?
transmission not selecting expected ratio?
```

Power result là chain:

```text
air
+ fuel
+ compression
+ ignition/combustion
+ exhaust flow
+ thermal state
+ ECU protection
→ crank torque
→ transmission
→ wheel force
```

Chẩn đoán chỉ engine mà bỏ transmission/tire/thermal state có thể sai layer.

### Turbo-related reasoning

Low boost không tự động = failed turbo.

Có thể cần phân biệt:

- intake leak;
- charge-air leak;
- wastegate/control issue;
- sensor/measurement issue;
- exhaust energy issue;
- protection/limp mode;
- actual compressor/turbine mechanical problem.

---

# 14. Overheating diagnostics bằng heat-flow model

Chapter Thermal đã cho invariant:

```text
heat generation
→ transport
→ rejection
```

Nếu temperature tăng bất thường, chia hypotheses theo layer:

### Generation quá cao

- abnormal combustion/load;
- excessive friction;
- sustained severe duty.

### Transport kém

- low coolant;
- pump/circulation issue;
- trapped air;
- thermostat/valve problem.

### Rejection kém

- radiator/exchanger restriction;
- airflow/fan problem;
- external blockage;
- high ambient + insufficient margin.

Đây là ví dụ tốt về **system decomposition before part replacement**.

---

# 15. HEV/BEV diagnostics: đừng dùng ICE mental model nguyên xi

Electrified vehicle complaints có thêm layers:

```text
high-voltage battery
→ contactors / HV distribution
→ inverter
→ motor
→ reduction/drivetrain

plus
BMS + thermal management + low-voltage control
```

### Range drop

Không tự động = battery degradation.

Có thể do:

- temperature;
- HVAC load;
- speed/aero;
- tire pressure;
- route/elevation;
- state-of-charge window;
- recent driving adaptation;
- actual battery aging.

### Fast charging slow

Phân biệt:

```text
charger capability
vehicle voltage/current limit
battery SOC
battery temperature
pack thermal state
station sharing/derating
charging curve
```

Peak brochure kW gần như không đủ để diagnosis.

### Reduced power

Có thể là deliberate protection:

- low SOC;
- high/low battery temperature;
- inverter/motor thermal limit;
- fault mode.

`derating` đôi khi là hệ thống hoạt động đúng để tránh damage.

---

# 16. ADAS diagnostics: sensor visibility, calibration, state và actuator

ADAS complaint có thể nằm ở:

```text
sensor visibility
→ sensor hardware
→ calibration/alignment
→ perception
→ state estimation
→ controller
→ actuator
→ physical environment
```

Ví dụ “lane centering hoạt động kém” có thể liên quan:

- lane markings;
- weather/light;
- windshield/camera contamination;
- calibration sau windshield/alignment work;
- tire/alignment state;
- system operating-domain boundary.

Không nên đánh giá chỉ từ một drive event mà không kiểm soát conditions.

---

# 17. Maintenance schedule phải đọc theo service severity

Owner manual thường phân biệt hoặc ngầm giả định operating conditions.

Severity drivers có thể gồm:

- nhiều short trip;
- stop-and-go;
- dusty environment;
- high/low temperature;
- towing/heavy load;
- repeated mountain driving;
- frequent fast charging hoặc high thermal load tùy system;
- long storage.

Vì vậy:

```text
same odometer
≠ same degradation history
```

Mileage là exposure proxy, không phải wear measurement tuyệt đối.

---

# 18. Preventive, condition-based và corrective maintenance

## Preventive

Intervene theo schedule/exposure trước failure.

Ưu điểm:

- predictable;
- suitable cho components có known degradation interval.

Nhược điểm:

- có thể replace sớm;
- schedule có thể không phản ánh actual condition.

## Condition-based

Intervene dựa measurement/inspection.

Ví dụ:

- pad thickness;
- tire tread/wear;
- battery health metrics;
- fluid condition khi có valid test;
- vibration/noise trends.

## Corrective

Repair sau khi failure/functional degradation đã xuất hiện.

Phù hợp hơn với non-critical low-consequence items; rủi ro với safety-critical systems.

---

# 19. Parts cannon là một diagnostic anti-pattern

**Parts cannon** = thay hàng loạt component theo guess đến khi symptom biến mất.

Nó có ba vấn đề:

```text
cost
+ confounding
+ lost information
```

Nếu thay 4 parts cùng lúc và symptom hết, ta mất khả năng biết cái nào là cause.

Tốt hơn:

```text
hypothesis
→ prediction
→ least-invasive discriminating test
→ update
→ next test / repair
```

Đây chính là experimental reasoning ở quy mô nhỏ.

---

# 20. Diagnostic test nên có prediction trước khi đo

Trước một test, viết:

```text
Nếu H1 đúng, tôi kỳ vọng observation X.
Nếu H2 đúng, tôi kỳ vọng observation Y.
```

Nếu không biết result nào sẽ phân biệt hypotheses, test có information value thấp.

Ví dụ:

```text
H1 vibration is wheel-speed coupled
H2 vibration is engine-speed coupled

test:
compare same engine RPM at different vehicle speeds / stationary condition
```

Một test tốt giảm uncertainty, không chỉ tạo thêm data.

---

# 21. False certainty từ scanner, app và AI

Tool có thể cung cấp:

- DTC;
- live data;
- maintenance history;
- thermal data;
- battery data;
- sound pattern;
- AI-generated possible causes.

Nhưng tool không xóa các vấn đề:

```text
measurement error
missing context
base-rate error
correlated symptoms
model limitations
```

Một ranked list từ app nên được coi là **hypothesis generator**, không phải authoritative diagnosis.

---

# 22. Diagnostic evidence hierarchy

Không có một hierarchy tuyệt đối, nhưng thường có thể ưu tiên:

```text
reproducible symptom under defined conditions
+ direct measurement
+ visual/physical inspection
+ controller data with known context
+ before/after controlled intervention
> vague anecdote
```

Evidence mạnh nhất thường là evidence vừa:

- gần mechanism;
- repeatable;
- discriminating giữa hypotheses.

---

# 23. Repair decision khác diagnosis

Ngay cả khi diagnosis tương đối rõ, decision còn cần:

```text
safety consequence
repair cost
secondary-damage risk
remaining vehicle value
parts availability
warranty
future reliability
planned ownership horizon
```

Do đó:

```text
correct diagnosis
≠ automatically correct economic decision
```

Economic layer được xử lý ở chapter ownership/TCO tiếp theo và Consumer Literacy.

---

# 24. Reusable diagnostic worksheet

```text
SYMPTOM
- exact observation:
- when / where / trigger:
- frequency / trend:
- recent service / impact / software change:

TRIAGE
- safety critical?
- secondary-damage risk?
- stop / limited use / monitor?

SYSTEM MAP
- likely subsystem(s):
- adjacent subsystem(s):

HYPOTHESES
H1:
H2:
H3:

PREDICTIONS
- if H1, expect:
- if H2, expect:
- if H3, expect:

DISCRIMINATING EVIDENCE
- measurement/test:
- result:
- hypothesis update:

DECISION
- monitor
- maintenance
- further test
- repair
- professional escalation
```

---

# 25. Case study 1 — vibration ở highway speed

Symptom:

```text
steering vibration 95–115 km/h
minimal below 70
no meaningful change with engine RPM at standstill
```

Possible hypotheses:

```text
H1 wheel imbalance
H2 tire deformation
H3 wheel damage
H4 suspension/alignment interaction
H5 engine/mount
```

Evidence:

- vehicle-speed coupling weakens H5;
- steering-wheel localization raises front axle candidates;
- recent tire work raises H1/H2 prior;
- visible tire/wheel inspection và balance/runout measurements có high information value.

Điểm học:

> Không cần biết part trước; cần biết **biến nào symptom đang couple theo**.

---

# 26. Case study 2 — fuel economy giảm

Symptom:

> fuel economy giảm 15% trong một tháng.

Trước diagnosis, normalize:

- route?
- traffic?
- ambient temperature?
- tire pressure?
- fuel type?
- HVAC?
- short trips?
- seasonal blend?

Sau đó mới build hypotheses:

```text
tire/rolling resistance
engine thermal operation
sensor/control adaptation
brake drag
fuel/air issue
changed driving pattern
```

Nếu không kiểm soát context, ta có thể “repair” một hệ thống không hỏng.

---

# 27. Case study 3 — EV range giảm mùa đông

Observation:

> displayed/actual range thấp hơn summer.

Hypotheses:

```text
H1 ambient/battery cold effect
H2 cabin heating load
H3 tire/rolling resistance
H4 route/speed change
H5 battery degradation
```

Nếu range phục hồi rõ trong warm conditions, H5 không biến mất nhưng update yếu hơn so với thermal/auxiliary-load hypotheses.

Đây là ví dụ điển hình:

```text
condition effect
≠ permanent degradation
```

---

# 28. Case study 4 — AEB unavailable sau windshield replacement

Relevant chain:

```text
windshield / camera geometry
→ sensor alignment
→ calibration state
→ perception confidence
→ feature availability
```

Thay windshield là event có causal relevance. Nếu system yêu cầu calibration mà chưa hoàn thành, đây có thể là higher-value hypothesis hơn “ADAS ECU hỏng”.

---

# 29. Khi nào cần professional diagnosis

Life Library không thay thế qualified technician khi:

- safety-critical system;
- high-voltage EV/HEV system;
- fuel leak/fire risk;
- brake/steering severe failure;
- specialized pressure/electrical tests;
- warranty/recall issue;
- diagnosis cần manufacturer scan data/procedure.

Mục tiêu của chapter là giúp người dùng:

```text
mô tả symptom tốt hơn
→ hiểu câu hỏi technician đang kiểm tra
→ tránh parts-cannon reasoning
→ đánh giá evidence tốt hơn
```

không phải biến reader thành mechanic chỉ bằng một chapter.

---

# 30. Connections

- System mechanics: [Cars README](README.md)
- Engine mechanism: [ICE fundamentals](01_ice_engine_fundamentals.md)
- Tire/grip: [Tires](05_tires_traction_and_contact_patch.md)
- Braking: [Brakes/ABS/Regen](06_brakes_abs_and_regenerative_braking.md)
- Chassis: [Steering/Suspension/Alignment](07_steering_suspension_and_alignment.md)
- Thermal diagnosis: [Thermal Management](09_thermal_management_ice_hybrid_bev.md)
- ADAS diagnosis: [Safety/ADAS](10_safety_adas_perception_control_and_limits.md)
- Generic maintenance framework: [Reliability, Repairability & Maintenance](../../consumer_literacy/02_reliability_repairability_and_maintenance.md)

---

## Kết luận

Car diagnostics không phải trò đoán part. Nó là một quá trình uncertainty reduction:

```text
precise symptom
→ system boundary
→ competing hypotheses
→ predicted observations
→ discriminating evidence
→ update
→ intervention
→ verify outcome
```

Khi giữ được chain này, maintenance trở thành quản lý degradation có lý do, diagnostics trở thành causal reasoning có kiểm chứng, và repair decision được tách khỏi việc chỉ “thay thứ scanner gợi ý”.