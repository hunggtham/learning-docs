# Engine Displacement, Cylinders, NA & Turbo — Vì sao `2.0L Turbo` chưa nói hết sức mạnh động cơ?

Sau khi hiểu chuỗi cơ bản `fuel + air → combustion → piston → crankshaft torque` trong [`01_ice_engine_fundamentals.md`](01_ice_engine_fundamentals.md), ta vẫn còn một khoảng trống rất thực tế: brochure xe thường ném ra các nhãn như `1.6T`, `2.0 NA`, `V6 3.5`, `I4 turbo`, `downsized turbo`, nhưng các nhãn này **không phải power rating**.

Chapter này giải quyết câu hỏi: **displacement, cylinder count, bore/stroke và forced induction thay đổi lượng air/fuel engine có thể xử lý như thế nào, và vì sao hai engine cùng dung tích vẫn cho torque/power/response khác nhau?**

Mental chain cần giữ:

```text
engine geometry
→ trapped air mass per cycle
→ fuel that can be burned cleanly
→ cylinder pressure
→ crankshaft torque
→ torque across RPM
→ power

plus:
intake pressure
thermal limits
knock / fuel quality
cooling
exhaust backpressure
control strategy
```

Điểm quan trọng là **engine size chỉ là một input vào hệ thống**, không phải output cuối.

---

## 1. Displacement đo thể tích piston quét qua — không trực tiếp đo horsepower

Dung tích động cơ (engine displacement / 배기량) là tổng thể tích mà các piston quét qua giữa điểm chết trên và điểm chết dưới trong các xi-lanh.

Với một cylinder, swept volume có thể hình dung bằng:

```text
V = π/4 × bore² × stroke
```

Trong đó:

- `bore` = đường kính cylinder;
- `stroke` = quãng piston di chuyển;
- tổng displacement = swept volume của một cylinder × số cylinder.

Ví dụ nhãn `2.0 L` nghĩa tổng swept volume xấp xỉ hai lít. Nó **không** có nghĩa engine hút đúng 2.0 L không khí mỗi giây, cũng không có nghĩa mọi 2.0 L đều tạo cùng torque.

Displacement hữu ích vì nó cho biết **geometric capacity per engine cycle**. Nhưng air mass thực sự đi vào cylinder còn phụ thuộc intake pressure, temperature, valve timing, RPM, volumetric efficiency và forced induction.

Vì vậy:

```text
same displacement
≠ same trapped air mass
≠ same cylinder pressure
≠ same torque
≠ same power
```

Displacement nên được đọc như geometry baseline, không phải performance verdict.

---

## 2. Vì sao nhiều displacement thường tạo tiềm năng torque lớn hơn?

Để tạo combustion torque, cylinder cần air + fuel. Ở cùng công nghệ và operating condition, engine có swept volume lớn hơn thường có khả năng xử lý nhiều air/fuel hơn mỗi cycle.

Một intuition hữu ích:

```text
more cylinder volume
→ potentially more air mass per cycle
→ potentially more fuel burned per cycle
→ potentially more expansion force
→ potentially more crankshaft torque
```

Từ `potentially` rất quan trọng. Nếu airflow kém, compression/combustion strategy khác hoặc engine bị giới hạn bởi emissions/thermal/control, displacement lớn hơn không đảm bảo output tăng tương ứng.

Torque thực tế có thể được nhìn qua khái niệm **brake mean effective pressure** (BMEP / 평균 유효 압력) ở mức intuition:

```text
torque
≈ displacement × effective cylinder pressure
```

BMEP giúp trả lời một câu hỏi mà chỉ displacement không trả lời được: **engine khai thác mỗi đơn vị displacement mạnh đến đâu?**

Một turbo engine nhỏ có thể tạo effective cylinder pressure cao hơn một naturally aspirated engine lớn, nên torque output có thể ngang hoặc vượt dù displacement thấp hơn.

Formal engine thermodynamics và combustion modeling sâu hơn thuộc Physics/Chemistry/engineering owner; Life chỉ giữ model đủ để đọc engine spec đúng.

---

## 3. Cylinder count và displacement là hai trục khác nhau

Một `2.0 L inline-4` và một hypothetical `2.0 L V6` có cùng total displacement nhưng chia volume đó thành số cylinder khác nhau.

Ví dụ đơn giản:

```text
2.0 L I4
→ ~0.5 L / cylinder

3.0 L V6
→ ~0.5 L / cylinder
```

Cylinder count ảnh hưởng:

- packaging;
- firing frequency;
- rotating/reciprocating mass;
- friction surface;
- intake/exhaust layout;
- balance/vibration characteristics;
- combustion chamber size;
- engine length/width;
- cost/complexity.

Nó không phải một ladder đơn giản kiểu:

```text
6 cylinders > 4 cylinders > 3 cylinders
```

Một modern turbo I4 có thể tạo nhiều power hơn một older NA V6. Ngược lại V6 có thể cho smoothness, response hoặc thermal/load behavior khác.

Do đó khi đọc `I3 / I4 / I6 / V6 / V8`, hãy hỏi:

```text
configuration giải quyết packaging/balance/firing như thế nào?
per-cylinder displacement là bao nhiêu?
aspiration system là gì?
output curve và operating goal là gì?
```

Cylinder count là architecture choice, không phải quality score.

---

## 4. Inline, V, boxer nói về geometry arrangement

### Inline engine

Inline engine (직렬 엔진) đặt cylinder theo một hàng.

Common examples:

```text
I3
I4
I6
```

I4 rất phổ biến vì packaging/cost hợp lý cho nhiều passenger cars. I6 nổi tiếng về inherent balance characteristics nhưng dài hơn, ảnh hưởng layout.

### V engine

V engine (V형 엔진) chia cylinders thành hai bank tạo thành góc V.

Ví dụ:

```text
V6
V8
```

Nó giúp pack nhiều cylinder trong chiều dài ngắn hơn inline equivalent, nhưng cylinder heads/exhaust/intake layout phức tạp hơn.

### Boxer / horizontally opposed

Boxer/horizontally opposed engine (수평대향 엔진) đặt cylinder đối diện hai bên crankcase.

Potential advantages/trade-offs liên quan center of gravity, width, exhaust routing và service access.

Điểm chốt:

```text
I4 / V6 / boxer
→ cylinder arrangement

2.0 L / 3.0 L
→ displacement

turbo / NA
→ aspiration

200 kW / 400 Nm
→ output
```

Bốn nhóm label này **không nằm trên cùng một taxonomy axis**.

---

## 5. Bore và stroke thay đổi geometry dù displacement giống nhau

Hai engine có thể cùng displacement nhưng bore/stroke ratio khác.

### Oversquare

```text
bore > stroke
```

Geometry này thường cho phép valve area lớn hơn và giảm mean piston speed ở cùng RPM so với long-stroke geometry, nên có thể phù hợp high-RPM breathing — nhưng đây không phải guarantee về toàn bộ engine behavior.

### Undersquare / long-stroke

```text
stroke > bore
```

Có thể hỗ trợ packaging/combustion/torque design goals khác, nhưng không nên biến thành slogan `long stroke = torque engine` không điều kiện.

### Square-ish

```text
bore ≈ stroke
```

Là một compromise geometry phổ biến.

Bore/stroke tác động tới:

- combustion chamber geometry;
- valve area potential;
- piston speed;
- surface-to-volume ratio;
- mechanical stress;
- RPM capability;
- knock/combustion characteristics.

Vì engine còn valve timing, intake/exhaust, compression ratio, boost và calibration, bore/stroke chỉ là một layer trong full design.

---

## 6. Mean piston speed giải thích vì sao RPM không thể tăng vô hạn

Khi crankshaft quay nhanh hơn, piston phải tăng tốc/giảm tốc qua stroke nhiều lần mỗi giây.

Một intuition hữu ích:

```text
mean piston speed
∝ stroke × RPM
```

Higher RPM làm tăng:

- inertial loads;
- friction losses;
- valvetrain demands;
- oiling demands;
- heat generation;
- mechanical stress.

Do đó power không thể tăng vô hạn bằng cách “cho engine quay nhanh hơn”. High-RPM engine cần geometry, materials, valvetrain, lubrication và breathing phù hợp.

Kết nối với power equation:

```text
Power = Torque × angular speed
```

Một engine có thể tạo power cao bằng:

```text
high torque
× moderate RPM
```

hoặc:

```text
moderate torque
× high RPM
```

Hai strategy có thể cho driving character rất khác dù peak power gần nhau.

---

## 7. Naturally aspirated engine phụ thuộc pressure difference tự nhiên

Naturally aspirated engine (NA / 자연흡기 엔진) không dùng compressor driven by exhaust turbine hoặc mechanical supercharger để nâng intake manifold pressure đáng kể trên ambient pressure.

Simplified intake path:

```text
atmosphere
→ air filter
→ throttle
→ intake manifold
→ intake valves
→ cylinder
```

Piston moving down + pressure dynamics giúp kéo air vào cylinder.

Nhưng cylinder không tự động fill đúng 100% geometric displacement mỗi intake event. Airflow bị ảnh hưởng bởi:

- filter/intake restriction;
- throttle;
- valve opening area/timing/lift;
- intake runner resonance;
- exhaust scavenging;
- RPM;
- ambient pressure;
- temperature.

Khái niệm **volumetric efficiency** (VE / 체적 효율) mô tả mức engine fill cylinder hiệu quả so với geometry reference.

Ở mức intuition:

```text
geometry says how much space exists
VE says how effectively that space is filled
```

Tuned NA engines ở một số RPM có thể đạt effective filling rất tốt nhờ pressure-wave dynamics; vì vậy `NA = always poor cylinder filling` cũng là simplification sai.

---

## 8. Turbocharger dùng exhaust energy để nén intake air

Turbocharger (터보차저) có hai phía chính nối bằng shaft:

```text
exhaust gas
→ turbine
→ shaft
→ compressor
→ compressed intake air
```

Turbine lấy một phần energy từ exhaust flow. Compressor dùng shaft work đó để tăng intake-air pressure.

Khi pressure tăng, cylinder có thể nhận **nhiều air mass hơn trong cùng geometric volume**.

Do đó:

```text
2.0 L turbo
```

không còn bị giới hạn ở lượng air tương đương một `2.0 L NA` ở atmospheric filling.

Đây là bản chất của forced induction:

```text
same geometric cylinder volume
+ higher intake density/pressure
→ more oxygen mass per cycle
→ more fuel can be burned
→ higher potential torque
```

Turbo không “tạo oxygen”; nó compress lượng air đi vào cylinder.

---

## 9. Boost pressure một mình chưa đủ để so turbo engines

Boost thường được nói dưới dạng pressure above ambient.

Nhưng cùng boost number không đảm bảo cùng air mass hoặc power vì còn:

- compressor efficiency;
- intake-air temperature;
- intercooler effectiveness;
- ambient pressure/temperature;
- engine displacement;
- RPM;
- VE;
- exhaust backpressure;
- valve timing;
- fuel/ignition strategy.

Air density phụ thuộc cả pressure và temperature.

Nếu compressor làm air nóng lên mạnh:

```text
higher pressure
but also higher temperature
→ density gain smaller than naive pressure ratio suggests
```

Vì vậy forced-induction system phải được đọc như **pressure + temperature + flow + control system**, không chỉ `boost psi/bar`.

---

## 10. Intercooler tồn tại vì compressed air nóng lên

Compress gas thường làm nhiệt độ tăng.

Hot intake air gây bất lợi:

- density giảm so với same-pressure cooler air;
- knock tendency có thể tăng;
- thermal load tăng;
- ECU có thể phải retard ignition hoặc giảm boost.

Intercooler (인터쿨러) lấy heat khỏi compressed intake air trước khi air vào engine.

Path:

```text
compressor
→ hot compressed air
→ intercooler
→ cooler denser air
→ engine
```

Intercooler performance vì vậy ảnh hưởng **repeatable power**, đặc biệt khi ambient temperature cao hoặc load kéo dài.

Một dyno pull ngắn ở điều kiện mát không nhất thiết đại diện sustained output trong mountain climb, track use hoặc hot weather.

Đây là bridge tự nhiên sang thermal-management chapter sau.

---

## 11. Turbo lag đến từ energy/flow dynamics, không chỉ “turbo chậm”

Turbo cần exhaust flow/enthalpy để quay turbine và compressor lên operating condition cần thiết.

Khi driver yêu cầu torque đột ngột ở low RPM:

```text
throttle/load request
→ more combustion/exhaust flow
→ turbine accelerates
→ compressor pressure rises
→ cylinder air mass increases
→ torque rises
```

Khoảng thời gian giữa request và boost/torque response thường được gọi là turbo lag.

Lag chịu ảnh hưởng bởi:

- turbine/compressor inertia;
- turbo size;
- exhaust manifold volume;
- engine displacement;
- RPM;
- gear;
- wastegate strategy;
- variable geometry nếu có;
- electric assist nếu có;
- hybrid torque fill;
- throttle/ECU calibration.

Do đó `bigger turbo = always better` sai vì turbo size tạo trade-off giữa flow capacity và transient response.

---

## 12. Wastegate và boost control giữ turbo khỏi “nén càng nhiều càng tốt”

Turbocharger không được phép tăng turbine/compressor speed không kiểm soát.

Wastegate cho một phần exhaust bypass turbine để control turbine power và boost.

Simplified loop:

```text
boost target
→ ECU / actuator
→ wastegate position
→ turbine power
→ compressor output
→ measured manifold pressure
→ feedback
```

Modern engines dùng closed-loop control phức tạp hơn, phối hợp:

- throttle;
- wastegate;
- ignition timing;
- fuel injection;
- cam timing;
- knock sensing;
- transmission torque request;
- traction/thermal limits.

Vì vậy engine output là **controlled system**, không chỉ hardware capability.

---

## 13. Knock là một boundary lớn của cylinder pressure

Spark-ignition gasoline engine muốn combustion diễn ra theo controlled flame propagation.

Knock (노킹) liên quan abnormal auto-ignition của unburned mixture/end gas, tạo pressure oscillations có thể gây stress/damage nếu nghiêm trọng.

Knock tendency chịu ảnh hưởng bởi:

- compression ratio;
- boost;
- intake temperature;
- combustion chamber design;
- ignition timing;
- fuel octane;
- mixture/cooling strategies;
- deposits/hot spots.

ECU dùng knock sensor và control logic để bảo vệ engine.

Khi knock margin giảm, ECU có thể:

```text
retard ignition
reduce boost
change mixture
limit torque
```

Do đó fuel quality và ambient heat có thể làm output thực tế khác brochure peak rating.

Không nên hiểu premium fuel như universal “power additive”; benefit phụ thuộc engine calibration và knock-limited operating region.

---

## 14. Compression ratio và boost không thể đọc độc lập

Static/geometric compression ratio mô tả volume ratio giữa piston positions.

Boost tăng intake charge pressure. Hai yếu tố cùng ảnh hưởng cylinder pressure/temperature nhưng không thể cộng bằng một công thức đơn giản kiểu:

```text
compression ratio + boost = effective compression ratio
```

because real engine còn:

- valve timing;
- dynamic compression;
- charge cooling;
- heat transfer;
- fuel evaporation;
- combustion timing;
- exhaust pressure;
- control strategy.

Mental model đúng hơn:

```text
hardware compression geometry
+ trapped charge state
+ valve timing
+ ignition/combustion
→ actual cylinder pressure history
```

Đây là lý do modern turbo engines có thể dùng compression ratios khác nhau đáng kể tùy combustion strategy.

---

## 15. Turbo downsizing đổi trade-off chứ không xóa physics

Một strategy phổ biến là dùng displacement nhỏ hơn + turbo để đạt peak torque/power tương đương engine NA lớn hơn.

Potential benefits ở một số duty cycle:

- reduced pumping/friction losses ở low load;
- smaller engine mass/packaging;
- high torque from low-mid RPM khi boost available;
- regulatory test-cycle efficiency.

Nhưng trade-offs:

- higher specific cylinder pressure;
- higher exhaust/turbo thermal load;
- cooling demand;
- transient enrichment/thermal protection depending design;
- more components/control complexity;
- real-world efficiency depends on how often boost/high load is used.

Vì vậy:

```text
small turbo engine
≠ automatically more efficient in every driving pattern
```

Nếu driver thường xuyên yêu cầu high power, engine vẫn phải burn fuel proportional to work produced plus losses.

Downsizing primarily changes **where/how efficiently engine operates across load map**, không tạo free energy.

---

## 16. Specific output giúp normalize displacement nhưng vẫn không phải quality score

Ta có thể normalize peak power theo displacement:

```text
specific power = power / displacement
```

Ví dụ:

```text
150 kW from 2.0 L
→ 75 kW/L
```

Specific torque cũng có thể dùng tương tự.

Metric này giúp thấy engine tạo output cao đến mức nào trên mỗi liter geometry, nhưng high specific output có thể kéo theo trade-off về:

- boost/cylinder pressure;
- heat;
- durability margin;
- fuel requirement;
- calibration;
- cost.

Không thể kết luận:

```text
higher kW/L = better engine
```

Nếu use case là long-life commercial duty, low thermal stress có thể quan trọng hơn peak specific power.

Consumer Literacy rule áp dụng trực tiếp: **normalized metric giúp so một dimension; nó không thay total system judgment**.

---

## 17. Peak torque plateau của turbo engine đến từ control, không phải “torque tự nhiên phẳng”

Modern turbo engines thường advertise plateau kiểu:

```text
350 Nm @ 1,800–4,500 rpm
```

Điều này thường phản ánh control strategy:

- turbo có potential tạo hơn ở một số region;
- ECU giới hạn boost/cylinder pressure/torque theo RPM;
- drivetrain/transmission protection có thể đặt torque cap;
- thermal/knock constraints thay đổi theo speed/load.

Vì vậy torque curve là product của:

```text
hardware airflow capability
× combustion limits
× turbo system
× ECU targets
× protection constraints
```

Không chỉ displacement.

---

## 18. Vì sao same engine có nhiều power rating khác nhau?

Cùng engine family có thể xuất hiện nhiều tune/output variant.

Differences có thể đến từ:

- ECU calibration;
- boost target;
- turbo hardware;
- intercooler;
- exhaust;
- fuel system;
- cooling capacity;
- compression ratio;
- transmission torque limit;
- emissions hardware;
- market/fuel requirement.

Do đó “same 2.0T block” chưa đủ để kết luận hai vehicle có identical engine system.

Khi so variant, cần tách:

```text
shared architecture
vs
shared exact hardware
vs
shared calibration
```

Ba mức này rất khác nhau.

---

## 19. Altitude làm NA và turbo behave khác nhau vì ambient pressure thay đổi

Ở altitude cao, atmospheric pressure/density thấp hơn.

NA engine không có compressor để bù đáng kể pressure loss nên trapped air mass và available torque thường giảm.

Turbo engine có thể tăng compressor work để duy trì manifold target tốt hơn trong một range nhất định.

Nhưng turbo không miễn nhiễm altitude:

- compressor phải dùng pressure ratio cao hơn;
- shaft speed/temperature tăng;
- compressor map/overspeed limit xuất hiện;
- cooling/knock margin thay đổi.

Mental model:

```text
NA
ambient pressure drop
→ cylinder air mass drops more directly

Turbo
ambient pressure drop
→ control may compensate partially
→ until turbo/thermal limits are reached
```

Đây là ví dụ tốt cho việc hardware feature chỉ có ý nghĩa trong operating condition cụ thể.

---

## 20. Turbocharger, supercharger và electric boost cùng mục tiêu nhưng energy source khác

### Turbocharger

```text
exhaust energy
→ turbine
→ compressor
```

### Mechanical supercharger

```text
crankshaft mechanical power
→ compressor
```

Response có thể khác nhưng compressor work cuối cùng vẫn cần energy; supercharger lấy mechanical work từ engine trực tiếp.

### Electric compressor / e-turbo assist

```text
electrical energy
→ electric motor
→ compressor/turbo shaft assistance
```

Nó có thể cải thiện transient response nhưng lại tạo electrical/thermal/control demands.

Điểm chốt:

```text
forced induction
= increase intake charge density/flow

but
compressing air always has energy + thermal cost
```

Không có boost miễn phí.

---

## 21. “Turbo engine bền kém hơn NA” là claim quá rộng

Turbo engine thường chịu higher pressure/temperature và có thêm hardware:

- turbo bearings;
- oil/coolant lines;
- intercooler/hoses;
- wastegate/actuators;
- boost-control plumbing.

Điều này tạo **additional failure modes**.

Nhưng durability thực tế còn phụ thuộc:

- design margin;
- cooling/lubrication;
- material;
- calibration;
- duty cycle;
- maintenance;
- manufacturing quality.

Một conservatively tuned turbo engine có thể rất durable; một high-specific-output engine abused/poorly maintained có risk profile khác.

Dùng framework từ [`../../consumer_literacy/02_reliability_repairability_and_maintenance.md`](../../consumer_literacy/02_reliability_repairability_and_maintenance.md):

```text
more components / higher stress
→ more potential failure modes
≠ proof of poor reliability
```

Reliability cần field data hoặc evidence phù hợp, không suy từ architecture alone.

---

## 22. Oil và coolant quan trọng hơn khi heat density tăng

Turbocharger có thể quay ở very high speed và turbine side làm việc trong hot exhaust environment.

Oil có vai trò lubricate/cool bearings tùy design; coolant có thể được dùng cho center housing hoặc broader engine thermal control.

Các failure risks tăng khi:

- oil degraded/contaminated;
- wrong viscosity/spec;
- oil starvation;
- cooling system weak;
- repeated high load + inadequate heat rejection;
- shutdown/use pattern không phù hợp với design/thermal state.

Modern engines có nhiều control/cooling strategy giúp quản lý vấn đề này, nên old rule kiểu “mọi turbo phải idle vài phút trước khi tắt” không nên áp dụng universal.

Hãy theo manufacturer-specific maintenance/operating guidance khi có.

Generic lesson:

```text
higher thermal/mechanical loading
→ maintenance quality matters more
```

---

## 23. Fuel economy phải đọc trên engine load map, không đọc từ displacement alone

Một misconception:

```text
smaller displacement = always lower fuel consumption
```

Fuel use phụ thuộc requested vehicle work và engine efficiency ở operating points.

Driving scenario:

### Light cruise

Smaller turbo engine có thể hoạt động ở favorable load region, với lower friction/pumping loss so với larger engine.

### High load / boost

Nó phải move/burn enough air/fuel để tạo requested power; fuel consumption có thể tăng mạnh.

### Vehicle-level factors

- mass;
- aero drag;
- tire rolling resistance;
- gearing;
- hybridization;
- speed;
- traffic;
- HVAC;
- ambient condition.

Do đó fuel economy là **vehicle-system metric**, không phải engine-displacement label.

---

## 24. Cách đọc một badge `1.6T`, `2.0T`, `3.5 V6` đúng hơn

Khi gặp badge engine, đừng dừng ở displacement.

### Bước 1 — Geometry

```text
displacement?
cylinder count?
arrangement?
bore/stroke if relevant?
```

### Bước 2 — Aspiration

```text
NA?
turbo?
supercharged?
hybrid torque assistance?
```

### Bước 3 — Output curve

```text
peak torque + RPM range
peak power + RPM
redline / operating range
```

### Bước 4 — System constraints

```text
fuel requirement
cooling
transmission torque rating
vehicle mass
gearing
traction
```

### Bước 5 — Lifecycle

```text
maintenance requirements
thermal load
known failure modes with evidence
repairability / parts / TCO
```

Badge chỉ là entrypoint vào system map.

---

## 25. Worked comparison — vì sao `2.5 NA` và `1.6 Turbo` không thể so bằng liter

Giả sử hai xe có:

```text
Engine A
2.5 L naturally aspirated
190 hp
245 Nm

Engine B
1.6 L turbo
200 hp
300 Nm
```

Không thể kết luận B “mạnh hơn hoàn toàn” chỉ vì peak torque cao.

Cần xét:

```text
torque curve
transmission ratios
vehicle mass
throttle/transient response
fuel economy under actual duty cycle
thermal behavior
fuel requirement
maintenance/lifecycle
```

Engine B có thể tạo higher effective cylinder pressure nhờ boost; Engine A có larger displacement và simpler air path. Nhưng driver experience và lifecycle outcome vẫn là **vehicle-level result**.

Đây là pattern xuyên Life:

```text
spec label
→ mechanism
→ operating condition
→ system interaction
→ trade-off
```

---

## 26. Worked comparison — same `2.0T`, khác output

Hai 2.0T engines có thể khác:

```text
Engine X: 150 kW / 320 Nm
Engine Y: 220 kW / 400 Nm
```

Same displacement + turbo label không nói:

- turbo flow capacity;
- boost target;
- compression ratio;
- head/valve airflow;
- intercooling;
- fuel system;
- exhaust restriction;
- knock strategy;
- thermal limit;
- ECU calibration.

Vì vậy:

```text
2.0T
= geometry + broad aspiration class
≠ exact performance architecture
```

Đây là lý do car comparison phải đọc actual output curve và system context.

---

## 27. Failure modes khi học engine specs

### `Displacement lớn = engine mạnh hơn`

Sai vì output còn effective cylinder pressure/RPM/airflow/control.

### `Nhiều cylinder = tốt hơn`

Sai vì cylinder count là architecture/trade-off.

### `Turbo = free power từ exhaust`

Sai vì exhaust energy recovery đi kèm backpressure, compressor work, heat và control limits.

### `Boost cao hơn = engine mạnh hơn`

Sai nếu không xét airflow, temperature, displacement, RPM và calibration.

### `Turbo luôn tiết kiệm hơn`

Sai nếu không xét duty cycle/load.

### `Turbo luôn kém bền`

Architecture tạo thêm stress/failure modes nhưng reliability cần evidence và design context.

### `Peak torque thấp = xe chậm`

Transmission, RPM, power, mass và traction quyết định vehicle acceleration.

---

## 28. Consumer worksheet — đọc engine spec theo mechanism

Khi so hai engine, ghi:

```text
A. Geometry
- displacement:
- cylinders/configuration:
- bore/stroke if material:

B. Air system
- NA / turbo / supercharger:
- intercooling:
- boost info if meaningful:

C. Output
- peak torque:
- torque RPM range:
- peak power:
- power RPM:

D. Constraints
- fuel grade:
- cooling/thermal clues:
- transmission pairing:
- vehicle mass:

E. Use case
- city response:
- highway cruise:
- sustained load/towing/track:
- altitude/hot climate:

F. Lifecycle
- maintenance:
- additional components:
- reliability evidence:
- repairability/parts:
```

Nếu worksheet chỉ có `displacement + hp`, comparison vẫn quá nông.

---

## 29. Boundary với các chapter khác

Chapter này sở hữu **engine-side geometry + airflow/forced-induction mental model**.

Nó không sở hữu:

- thermodynamics/combustion theory formal → Physics/Chemistry;
- detailed turbo compressor-map design → mechanical/automotive engineering owner nếu được mở;
- full cooling architecture → thermal-management chapter tiếp theo;
- transmission torque multiplication → [`03_transmissions_and_reduction_gearing.md`](03_transmissions_and_reduction_gearing.md);
- wheel-force/traction → [`05_tires_traction_and_contact_patch.md`](05_tires_traction_and_contact_patch.md);
- maintenance/reliability generic framework → [`../../consumer_literacy/02_reliability_repairability_and_maintenance.md`](../../consumer_literacy/02_reliability_repairability_and_maintenance.md).

Boundary này giữ Cars ở đúng layer: đủ mechanism để đọc vehicle, không duplicate engine-design textbook.

---

## 30. Bàn giao sang thermal management

Ta đã có chain:

```text
displacement + geometry
→ cylinder filling
→ NA / forced induction
→ cylinder pressure
→ torque across RPM
→ power
```

Nhưng tăng air/fuel flow và specific output làm một constraint trở nên rõ hơn:

```text
more power density
→ more heat to reject
```

Engine coolant, oil, intercooler, radiator, battery/motor/inverter cooling ở HEV/BEV đều trả lời cùng một câu hỏi cấp hệ thống: **heat sinh ra ở đâu, đi qua path nào và chuyện gì xảy ra khi heat rejection không theo kịp load?**

Vì vậy chapter thermal-management tiếp theo sẽ nối trực tiếp engine/turbo hardware với sustained performance, battery protection và component life.

Điểm chốt cần giữ:

> **Displacement nói geometric volume; cylinder count nói architecture; turbo nói cách tăng intake charge density. Performance chỉ xuất hiện khi geometry × airflow × pressure × RPM × thermal/control limits cùng được xét.**
