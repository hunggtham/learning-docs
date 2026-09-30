# Case 08 — Một căn hộ cao tầng nhận điện, nước, Internet và thải nước/rác như thế nào?

Case này nối [construction-buildings](../construction-buildings/README.md), [electricity-grid](../electricity-grid/README.md), [water-supply](../water-supply/README.md), [sewage](../sewage/README.md), [waste-recycling](../waste-recycling/README.md), [Internet](../internet/README.md) và [mobile-networks](../mobile-networks/README.md).

Mục tiêu là làm rõ boundary rất hay bị nhầm: **utility ngoài phố hoạt động tốt không đồng nghĩa utility bên trong tòa nhà hoạt động tốt**.

## 1. Tòa nhà là điểm nối giữa municipal infrastructure và private/common infrastructure

```text
CITY / UTILITY SIDE
 ├─ electric distribution
 ├─ water main
 ├─ sewer
 ├─ telecom fiber
 └─ waste collection route
          ↓ property boundary
BUILDING SIDE
 ├─ transformer/switchgear
 ├─ tanks/pumps
 ├─ internal drainage
 ├─ telecom risers
 └─ waste rooms / collection point
          ↓
APARTMENT
```

Failure có thể nằm ở bất kỳ layer nào.

## 2. Điện tới ổ cắm

```text
generation
  ↓
transmission
  ↓
distribution grid
  ↓
building service connection
  ↓
transformer
  ↓
main switchboard
  ↓
riser
  ↓
floor panel
  ↓
apartment panel
  ↓
outlet
```

Nếu neighborhood grid có điện nhưng transformer/main breaker building lỗi, apartment vẫn mất điện.

## 3. Elevator, pump và emergency power

High-rise phụ thuộc electricity nhiều hơn low-rise vì vertical transport và water pressure.

```text
grid outage
   ↓
UPS / emergency generator / battery
   ↓
selected emergency loads
 ├─ fire alarm
 ├─ emergency lighting
 ├─ some pumps
 ├─ selected elevators depending design
 └─ control/security systems
```

Generator không nhất thiết cấp air-conditioner, mọi outlet hoặc toàn bộ elevators.

## 4. Nước lên tầng cao

Municipal network cung cấp water tới property boundary, nhưng pressure thường không được thiết kế để trực tiếp đẩy tới tầng rất cao.

```text
city water main
     ↓
meter / backflow protection
     ↓
break tank / reservoir
     ↓
booster pumps
     ↓
pressure zone A → lower floors
pressure zone B → mid floors
pressure zone C → upper floors
```

Pressure zoning tránh tầng thấp chịu áp suất quá lớn.

## 5. Vì sao tầng cao có thể mất nước trước tầng thấp?

Nếu booster pump lỗi:

```text
municipal supply still available
      ↓
basement tank still has water
      ↓
upper-zone pressure collapses
      ↓
upper floors lose water
```

Người ở có thể nghĩ “công ty nước cắt nước”, nhưng root cause nằm trong building.

## 6. Nước đã dùng đi đâu?

```text
sink / toilet / shower
      ↓
branch drain
      ↓
vertical stack
      ↓
building drain
      ↓
municipal sewer
      ↓
wastewater treatment plant
```

Drainage phần lớn dùng gravity. Basement fixtures dưới sewer level có thể cần sump/ejector pump.

## 7. Stormwater không nên luôn đi cùng sanitary wastewater

Modern systems có thể tách:

```text
roof / site rain
   ↓
storm drain

bathroom/kitchen/toilet
   ↓
sanitary sewer
```

Nếu infiltration/inflow quá lớn vào sanitary sewer, heavy rain có thể overload treatment/network.

## 8. Internet tới căn hộ

```text
ISP backbone
   ↓
metro/access network
   ↓
building telecom room
   ↓
vertical riser / fiber
   ↓
apartment ONT/router
   ↓
Wi‑Fi / Ethernet
```

Internet outage có thể ở ISP backbone, building telecom equipment, apartment router hoặc Wi‑Fi radio. “Mạng chậm” không nói layer nào.

## 9. Mobile signal trong high-rise

Outdoor macro cell không phải lúc nào phủ indoor tốt do reinforced concrete, coated glass và floor height.

Building có thể dùng:

- indoor distributed antenna system;
- repeaters;
- small cells;
- carrier shared indoor infrastructure.

Vì vậy điện tòa nhà mất có thể làm indoor coverage degrade dù outdoor cellular network vẫn bình thường.

## 10. Waste flow trong apartment complex

```text
apartment
 ↓
resident carries separated waste
 ↓
common collection point
 ├─ recyclables
 ├─ food waste
 └─ residual waste
 ↓
municipal/private collection
 ↓
treatment network
```

Ở Hàn Quốc, apartment complexes thường có standardized recycling/food-waste collection points. Ở Việt Nam, building practices khác nhau theo city/project/operator nhưng high-rise growth khiến dedicated waste-room/collection logistics ngày càng quan trọng.

## 11. Fire safety cắt ngang mọi utility

Fire incident có thể kích hoạt:

```text
detection
 ↓
alarm
 ↓
smoke control
 ↓
fire pump / sprinkler
 ↓
elevator recall / access control behavior
 ↓
emergency power
```

Các systems không độc lập; chúng phải được integrated tested.

## 12. Korea vs Vietnam apartment topology

### Korea
Dense apartment complexes thường có management office, centralized common systems, structured waste separation, parking, elevators, mechanical/electrical rooms và mature facility-management routines.

### Vietnam
New high-rise projects ngày càng có tương tự MEP/BMS/security systems; challenge thường nằm ở tốc độ đô thị hóa, coordination với external utilities, operation/maintenance quality và consistency giữa projects.

Điểm so sánh hữu ích không phải “nước nào có công nghệ hơn”, mà là **building stock age + operator maturity + municipal integration + maintenance regime**.

## 13. Một blackout 30 phút lan qua apartment như thế nào?

```text
grid trips
 ↓
main power lost
 ↓
emergency system starts
 ↓
selected elevators/pumps/control survive
 ↓
Wi‑Fi routers in apartments die unless local UPS
 ↓
indoor telecom equipment may rely on backup
 ↓
water service continues only while pressure/tank/pumps allow
 ↓
parking gates/access systems switch to fallback
```

Nếu outage kéo dài, fuel for generators và tank levels trở thành state variables mới.

## 14. Một water-main outage lan như thế nào?

```text
city main loses supply
 ↓
building tank buffers outage
 ↓
users may not notice immediately
 ↓
tank level falls
 ↓
pumps still operate but eventually run out
 ↓
water unavailable
```

Buffer làm failure delayed, nên time of symptom khác time of upstream failure.

## 15. Control plane của building

BMS có thể giám sát:

- temperatures;
- pumps;
- tank level;
- alarms;
- energy meters;
- ventilation;
- equipment status.

Nhưng BMS không phải physical system. Nếu pump motor hỏng, command trên screen không tạo pressure.

```text
BMS command
     ↓
controller / actuator
     ↓
physical equipment
     ↓
sensor feedback
```

Closed-loop control chỉ hoạt động khi cả sensor, controller và actuator khỏe.

## 16. Finality trong building operations

Một maintenance ticket `closed` chưa chắc system thực sự restored nếu không verify output.

```text
fault reported
→ technician action
→ equipment starts
→ output measured
→ user service restored
→ monitoring stable
```

Đây là phiên bản building của `execution ≠ settlement`.

## 17. Mental model cuối

```text
Apartment service
= external utility
+ property boundary
+ building plant
+ vertical distribution
+ apartment equipment
+ control/maintenance
```

Khi debug, luôn hỏi: **failure ở utility, building common system hay inside-unit system?**
