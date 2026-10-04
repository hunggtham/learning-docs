# Hybrid, PHEV & BEV Architecture — Năng lượng đi đâu trước khi tới bánh xe?

Sau khi hiểu động cơ đốt trong ở [`01_ice_engine_fundamentals.md`](01_ice_engine_fundamentals.md), bước tiếp theo không phải học thêm acronym mà là đổi câu hỏi: **xe lưu năng lượng ở đâu, thiết bị nào biến nó thành mô-men và hệ thống quyết định dùng nguồn nào ở từng thời điểm?**

ICE, HEV, PHEV và BEV khác nhau chủ yếu ở **energy storage + conversion path + control strategy**. Một sơ đồ đúng sẽ giải thích nhiều điều mà brochure thường trình bày như các feature rời: regenerative braking, EV mode, charging, engine start/stop, battery thermal management hay instant torque.

Mental map:

```text
energy source/storage
→ conversion device
→ power electronics / control
→ transmission or reduction
→ wheels

plus:
thermal management
charging/refueling
energy recovery
```

## 1. ICE làm baseline: một nguồn chính, nhiều loss path

Trong xe ICE truyền thống:

```text
fuel tank
→ combustion engine
→ transmission
→ differential/driveshaft
→ wheels
```

Fuel chứa chemical energy. Engine biến một phần thành mechanical rotation; phần lớn còn lại thoát qua heat/exhaust/friction và auxiliaries.

Điều quan trọng để so với điện hóa là ICE có efficiency thay đổi mạnh theo load/RPM. Engine không luôn chạy ở operating point tối ưu; idling và low-load city driving có thể kém hiệu quả.

Hybrid xuất hiện vì motor/battery có thể nhận một phần công việc ở những vùng ICE làm không tốt.

## 2. Electric drive path đơn giản hơn về mechanical conversion nhưng không “không có loss”

Trong BEV:

```text
battery
→ inverter / power electronics
→ electric motor
→ reduction gear / differential
→ wheels
```

Battery lưu electrical energy dưới dạng electrochemical state. Inverter điều khiển dòng điện phù hợp cho motor; motor tạo torque; reduction gear đưa torque/speed tới bánh.

Path có ít bước mechanical hơn một ICE drivetrain nhiều cấp, nhưng vẫn có loss:

```text
battery internal resistance
inverter switching/conduction
motor copper/iron losses
gear/bearing losses
thermal management
auxiliary loads
```

Vì vậy “EV efficiency = 100%” là sai. Điểm đúng hơn là electric drivetrain thường chuyển điện thành wheel motion hiệu quả hơn ICE chuyển fuel thành wheel motion trong nhiều operating conditions.

## 3. Motor điện có torque characteristic khác ICE

Electric motor có thể tạo torque cao từ tốc độ rất thấp và control rất nhanh. Vì vậy BEV thường không cần multi-speed transmission kiểu ICE passenger car phổ biến.

ICE lại có useful RPM band hẹp hơn và cần transmission để giữ engine gần vùng output/efficiency phù hợp.

Đây là lý do:

```text
motor torque figure
≠ directly comparable driving feel with engine torque figure
```

Wheel torque còn phụ thuộc gear ratio, speed, power limit, traction và control strategy.

## 4. Regenerative braking biến motor thành generator

Khi giảm tốc, kinetic energy của xe thường bị brake friction biến thành heat.

Electric drivetrain có thể dùng motor theo chiều ngược:

```text
vehicle kinetic energy
→ wheels
→ motor as generator
→ inverter
→ battery
```

Đây là regenerative braking (회생제동).

Nhưng regen không thu hồi toàn bộ năng lượng. Giới hạn đến từ:

- battery state of charge;
- battery temperature;
- motor/inverter capacity;
- tire traction;
- low-speed behavior;
- required braking force.

Vì vậy friction brake vẫn cần cho strong braking, low speed, emergency và các điều kiện regen bị giới hạn.

## 5. HEV: hai nguồn/đường năng lượng trong cùng vehicle

Hybrid electric vehicle (HEV / 하이브리드 자동차) kết hợp:

```text
fuel tank + ICE
battery + motor/generator
```

Mục tiêu không chỉ là “có thêm motor”. Control system phân chia công việc để:

- engine tránh một số low-efficiency region;
- motor hỗ trợ acceleration;
- regenerative braking thu hồi một phần energy;
- engine có thể tắt khi không cần;
- battery được charge/discharge trong operating strategy.

HEV thông thường không cần user cắm sạc ngoài cho daily operation; energy battery chủ yếu đến từ engine và regenerative braking.

## 6. Series hybrid: engine không nhất thiết trực tiếp kéo bánh

Một kiến trúc conceptual:

```text
fuel
→ engine
→ generator
→ electricity
→ motor
→ wheels
```

Engine có thể chạy như generator source trong khi motor là traction device chính.

Ưu điểm conceptual:

- engine operating point có thể được quản lý linh hoạt;
- mechanical path engine→wheel có thể đơn giản hơn.

Trade-off:

```text
chemical
→ mechanical
→ electrical
→ mechanical
```

mỗi conversion đều có loss. Ở highway steady-state, việc convert nhiều lần có thể kém lợi hơn direct mechanical path.

Không nên dùng label “series” để kết luận efficiency universally tốt/xấu; operating profile matter.

## 7. Parallel hybrid: engine và motor đều có thể đóng góp tới wheel

Conceptual:

```text
engine ─┐
        ├→ drivetrain → wheels
motor ──┘
```

Engine có thể trực tiếp truyền power tới wheel; motor hỗ trợ hoặc độc lập ở một số condition.

System cần clutch/gear/control strategy phù hợp để phối hợp two power sources.

Điểm cốt lõi:

> parallel hybrid giữ direct engine-to-wheel path, vì vậy có thể hiệu quả ở những condition engine hoạt động tốt.

## 8. Power-split / mixed architecture kết hợp behavior series và parallel

Một số hybrid dùng gearset/power-split device để chia engine power giữa mechanical path và electrical path.

Mental model:

```text
engine output
→ partly mechanical to wheels
→ partly generator/electrical path
→ motor contribution
```

Control strategy thay đổi liên tục theo speed, load, battery state và efficiency target.

Người học không cần nhớ tên từng manufacturer system để giữ principle:

> Hybrid architecture khác nhau ở **how power paths are connected and controlled**, không chỉ battery size.

## 9. PHEV thêm external charging và battery lớn hơn

Plug-in hybrid electric vehicle (PHEV / 플러그인 하이브리드 자동차) thêm khả năng:

```text
grid
→ onboard charger
→ larger battery
→ electric driving
```

PHEV thường có electric-only range đáng kể hơn HEV, sau đó vẫn có ICE/fuel path.

Nhưng real-world efficiency phụ thuộc use pattern mạnh.

Hai người cùng một PHEV có thể có fuel use rất khác:

```text
User A:
short commute + charge daily
→ high electric share

User B:
rare charging + long highway trips
→ engine share much higher
```

Do đó rating/spec phải được đọc cùng assumed test cycle và charging behavior.

## 10. BEV bỏ ICE nhưng thêm battery/charging/thermal dependency lớn

BEV architecture gồm nhiều subsystem critical:

```text
traction battery
BMS
inverter
motor
reduction gear
onboard charger / DC charging interface
12V/low-voltage system
thermal management
vehicle control software
```

Không có engine không có nghĩa “chỉ battery + motor”. Reliability, performance và charging đều phụ thuộc electronics/software/thermal system.

## 11. BMS không phải battery “brain” theo nghĩa magic — nó quản lý constraints

Battery management system (BMS / 배터리 관리 시스템) theo dõi/điều khiển các yếu tố như:

- cell/module voltage;
- current;
- temperature;
- estimated state of charge;
- balancing/protection;
- charge/discharge limits.

Battery cells có safe operating window. BMS giới hạn power/charging khi temperature, voltage hoặc state không phù hợp.

Vì vậy advertised peak charge/power không phải khả năng sustained ở mọi condition.

## 12. Thermal management ảnh hưởng performance, charging và aging

Battery, motor và power electronics đều sinh heat.

Temperature quá thấp/cao có thể ảnh hưởng:

- available power;
- charge rate;
- efficiency;
- battery degradation;
- component protection.

BEV/PHEV vì vậy dùng cooling/heating loops, heat pump/resistance heater hoặc nhiều thermal strategy khác nhau.

Một feature như “preconditioning” thực chất là đưa battery/cabin gần operating temperature phù hợp trước use/fast charging.

## 13. Charging power khác battery capacity

Hai spec rất dễ bị trộn:

```text
kWh
= energy capacity

kW
= power / rate of energy transfer
```

Ví dụ battery 80 kWh không có nghĩa luôn charge ở 80 kW.

Charging time phụ thuộc:

```text
charger capability
vehicle acceptance limit
battery SOC
battery temperature
charging curve
shared infrastructure / voltage/current constraints
```

Peak DC charging figure chỉ là một point; average power across useful SOC window thường phản ánh trip charging experience tốt hơn.

Handoff cách đọc spec sang [`../../consumer_literacy/00_reading_specs_labels_and_units.md`](../../consumer_literacy/00_reading_specs_labels_and_units.md).

## 14. Charging curve giải thích vì sao 10→80% thường nhanh hơn 80→100%

Battery không nhận peak power từ 0 tới 100% liên tục.

Simplified:

```text
low/moderate SOC
→ potentially higher charging power

high SOC
→ power tapers to protect cells/voltage limits
```

Exact curve phụ thuộc chemistry, temperature, pack design và software.

Do đó “X kW fast charging” không đủ để estimate full-session time.

## 15. Range là system outcome, không chỉ battery size

Range phụ thuộc:

```text
usable battery energy
÷
energy consumption per distance
```

Consumption lại phụ thuộc:

- speed/aerodynamics;
- temperature/HVAC;
- mass/load;
- tires;
- elevation;
- traffic;
- driving style;
- drivetrain efficiency.

Vì vậy battery lớn hơn thường tăng range nhưng không cho phép compare hai xe bằng kWh alone.

## 16. Highway và city có advantage pattern khác ICE

ICE thường kém ở stop-and-go vì idle/low-load losses; hybrid/EV có thể recover braking và avoid idle fuel consumption.

Ở highway speed cao:

- aerodynamic drag tăng mạnh;
- regen opportunity ít hơn;
- efficient ICE direct drive có thể cải thiện relative position;
- EV consumption tăng theo drag/HVAC/temperature.

Do đó “hybrid tốt bao nhiêu” phụ thuộc route profile.

## 17. Battery degradation khác fuel tank aging

Fuel tank capacity gần như không giảm đáng kể do normal cycle như battery usable capacity có thể giảm theo time/cycles/temperature.

Battery aging có nhiều mechanism; consumer mental model chỉ cần:

```text
calendar aging
+ cycle aging
+ temperature
+ charge/discharge stress
→ capacity / resistance change over time
```

Không suy battery life chỉ từ một owner anecdote hoặc cycle count đơn giản. Chemistry, thermal management và use pattern matter.

Handoff durability sang [`../../consumer_literacy/01_materials_quality_and_durability.md`](../../consumer_literacy/01_materials_quality_and_durability.md).

## 18. Hybrid complexity không thể đánh giá bằng component count alone

HEV/PHEV có cả engine path và electric path, nên intuition “nhiều component hơn = chắc chắn unreliable” có vẻ plausible nhưng chưa đủ.

Reliability phụ thuộc:

- architecture;
- maturity;
- operating stress;
- component quality;
- thermal design;
- software/control;
- maintenance;
- failure isolation.

Một hybrid có thể giảm stress một số engine/brake components nhưng thêm battery/motor/electronics. Cần evidence thực tế, không chỉ count parts.

Handoff sang [`../../consumer_literacy/02_reliability_repairability_and_maintenance.md`](../../consumer_literacy/02_reliability_repairability_and_maintenance.md).

## 19. “EV không cần bảo dưỡng” là simplification sai

BEV không có engine oil, spark plug hay exhaust system, nhưng vẫn có:

- tires;
- suspension;
- brakes;
- coolant/thermal system depending design;
- cabin filter;
- bearings;
- reduction gear fluid depending design;
- 12V/low-voltage components;
- HVAC;
- software/diagnostics.

Regenerative braking có thể giảm friction-brake wear, nhưng brakes vẫn cần inspection vì safety/corrosion/use pattern.

Đúng hơn:

> Maintenance mix thay đổi, không biến mất.

## 20. Classification axes cần tách rõ

Các label sau không cùng một trục:

```text
BEV / HEV / PHEV
= energy/powertrain architecture

FWD / RWD / AWD
= driven wheels / drivetrain layout

SUV / sedan / hatchback
= body architecture

400 hp
= power output metric

800V
= electrical architecture nominal class
```

Một BEV có thể AWD SUV; một HEV có thể FWD sedan. Trộn các label thành một list choice làm mental model rối.

## 21. Comparison framework cho powertrain architecture

Khi compare ICE/HEV/PHEV/BEV, không bắt đầu bằng “công nghệ nào tốt nhất”. Bắt đầu bằng use case:

```text
daily distance
trip profile
charging access
highway/city mix
climate
parking
payload/towing if relevant
ownership horizon
maintenance/support access
energy/fuel prices
```

Sau đó map:

```text
energy path
conversion losses
charging/refueling friction
range/route constraint
maintenance mix
battery/engine aging
failure/recovery path
```

TCO comparison dùng [`../../consumer_literacy/03_warranty_lifecycle_and_total_cost.md`](../../consumer_literacy/03_warranty_lifecycle_and_total_cost.md), còn affordability/financing thuộc Personal Finance.

## 22. Common misunderstandings

### “Hybrid = EV có engine backup”

Có nhiều architecture; engine/motor roles khác nhau.

### “PHEV luôn tiết kiệm fuel hơn HEV”

Use/charging pattern quyết định electric share.

### “BEV battery càng lớn càng tốt”

Battery lớn tăng energy/range nhưng cũng mass/cost/material/charging implications.

### “Peak charging = charging speed thực tế”

Charging curve và temperature/SOC matter.

### “Regenerative braking thu hồi gần hết energy”

Có conversion/traction/battery limits.

### “EV không có transmission”

Thường vẫn có reduction gear/differential; chỉ không cần multi-speed gearbox kiểu ICE phổ biến.

### “Hybrid nhiều parts nên chắc chắn kém bền”

Part count alone không đủ infer reliability.

## 23. Reusable architecture map

```text
Vehicle:
Architecture: ICE / HEV / PHEV / BEV
Energy stores:
Conversion devices:
Wheel drive path:
Charging/refueling path:
Regeneration path:
Transmission/reduction:
Thermal system:
Peak vs sustained limits:
Dominant efficiency conditions:
Dominant degradation mechanisms:
Maintenance mix:
Critical failure dependencies:
Use profile fit:
```

## Đọc tiếp

Từ đây có hai hướng cần học song song.

Một hướng đi sâu engine-side: displacement, cylinder layout, naturally aspirated, turbocharger và engine efficiency. Hướng còn lại đi vào **transmission** để hiểu vì sao engine/motor torque chưa trực tiếp là wheel torque và tại sao torque converter automatic, CVT, DCT hay fixed reduction tạo behavior khác nhau.

Khi compare architecture theo cost/lifecycle, dùng Consumer Literacy thay vì biến chapter kỹ thuật thành shopping recommendation.

Điểm chốt: **ICE/HEV/PHEV/BEV là các topology của energy flow và control. Hiểu topology trước thì các spec như battery size, charging power, horsepower, regen hay EV range mới có đúng vị trí trong hệ thống**.