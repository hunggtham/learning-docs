# Construction & Buildings — một tòa nhà đi từ đất trống tới lúc có người ở như thế nào?

Một tòa nhà không được “xây” bởi một actor duy nhất. Nó là chuỗi land → financing → design → permits → procurement → construction → inspection → commissioning → occupancy → maintenance. Sau khi hoàn thành, building tiếp tục là một system vận hành điện, nước, HVAC, fire protection, elevators, security và waste.

## 1. Project lifecycle

```text
site / land rights
      ↓
feasibility + financing
      ↓
architecture + engineering design
      ↓
permits / approvals
      ↓
procurement
      ↓
construction
      ↓
testing + commissioning
      ↓
inspection / occupancy approval
      ↓
operation + maintenance
```

Nếu chỉ nhìn construction site, ta bỏ mất hơn nửa system.

## 2. Owner, designer, contractor khác nhau

Actors thường gồm:

- **Chủ đầu tư (developer/owner / 발주자)**: quyết định project, funding và requirements.
- **Kiến trúc sư (architect / 건축사)**: spatial/function/design coordination.
- **Kỹ sư kết cấu (structural engineer / 구조기술자)**: load path và structural safety.
- **Kỹ sư MEP (mechanical-electrical-plumbing / 기계·전기·배관)**: HVAC, electrical, plumbing, fire systems.
- **Nhà thầu chính (general contractor / 종합건설사)**: sequencing và site execution.
- **Subcontractors**: concrete, steel, facade, electrical, HVAC, elevator…
- **Authority/inspector**: permits, code compliance, acceptance.
- **Facility manager**: building operation after handover.

Ownership of risk/contracts is as important as physical work.

## 3. Structural load path

Một building đứng được vì loads có đường truyền xuống đất:

```text
people / furniture / wind / self-weight
          ↓
floor slab
          ↓
beam / wall
          ↓
column / core
          ↓
foundation
          ↓
soil / rock
```

High-rise còn phải chịu lateral wind/seismic loads. Core walls, bracing, moment frames hoặc hệ tương đương chống sway.

## 4. Foundation phụ thuộc đất

Geotechnical investigation xác định soil layers, groundwater và bearing conditions.

```text
borehole / soil test
      ↓
geotechnical model
      ↓
foundation choice
      ↓
shallow footing / raft / piles
```

Chọn sai foundation có thể gây settlement, cracking hoặc instability dù superstructure được tính đúng.

## 5. Construction sequencing

Simplified high-rise flow:

```text
site preparation
→ excavation / retaining system
→ foundation
→ core + structural frame
→ facade
→ MEP rough-in
→ interior partitions/finishes
→ equipment installation
→ testing/commissioning
```

Nhưng các trade overlap. Nếu HVAC duct chạy qua chỗ structural beam, design coordination problem phải được giải trước hoặc site phải rework.

## 6. BIM là gì trong system này?

**Mô hình thông tin công trình (Building Information Modeling, BIM / 빌딩정보모델링)** không chỉ là 3D drawing. Nó có thể nối geometry với object properties, clash detection, quantities, sequencing và asset information.

```text
architectural model
+ structural model
+ MEP model
       ↓
coordination / clash detection
       ↓
construction information
```

BIM không tự đảm bảo project tốt; input/governance/version control vẫn quyết định quality.

## 7. MEP: building là một mini-infrastructure network

Sau khi structure đứng lên, building phải vận hành:

```text
Electricity grid → transformer/switchgear → floors → equipment
Water network → tank/pumps → fixtures
Used water → drainage → municipal sewage
Outdoor air → HVAC → rooms
Fire alarm/sprinkler → safety system
Internet/mobile → telecom risers → occupants
```

Một apartment tower là giao điểm trực tiếp của nhiều chapter trong library này.

## 8. Water in high-rise: municipal pressure thường chưa đủ cho mọi tầng

Typical topology:

```text
municipal water main
      ↓
building meter
      ↓
basement tank / break tank
      ↓
booster pumps
      ↓
pressure zones / roof tank depending design
      ↓
apartments
```

Pressure phải được chia zone; nếu bơm trực tiếp quá mạnh, tầng thấp chịu áp suất quá cao.

Wastewater:

```text
fixture
 ↓ gravity drainage
soil/waste stack
 ↓
building sewer
 ↓
municipal sewer
```

Nếu tầng hầm thấp hơn sewer level, ejector/sump pumps có thể cần thiết.

## 9. Electrical system

```text
utility medium/high voltage
        ↓
building transformer
        ↓
main switchboard
        ↓
riser / distribution board
        ↓
loads
```

Critical building có generator/UPS:

```text
grid outage
→ automatic transfer
→ generator / UPS
→ selected emergency loads only
```

Backup power không nhất thiết cấp toàn building.

## 10. HVAC và cooling

Large building có thể dùng chillers, boilers/heat pumps, AHU, FCU, cooling towers hoặc district energy tùy design.

Control layer là **hệ thống quản lý tòa nhà (Building Management System, BMS / 빌딩관리시스템)**:

```text
sensors
 ↓
controllers
 ↓
BMS
 ↓
setpoints / alarms / schedules
 ↓
HVAC / pumps / lighting
```

BMS là control plane; ducts/pipes/fans/pumps là physical plane.

## 11. Fire safety là nhiều layer, không phải một bình chữa cháy

```text
detection
→ alarm
→ compartmentation
→ smoke control
→ sprinkler / suppression
→ protected egress
→ fire department access
```

Building design phải giữ egress ngay cả khi normal elevators/power không dùng được.

## 12. Commissioning: “lắp xong” chưa phải “hoạt động đúng”

Commissioning kiểm tra systems dưới conditions thực tế:

- pump flow/pressure;
- HVAC balancing;
- fire alarm cause-and-effect;
- generator transfer;
- elevator operation;
- emergency lighting;
- BMS alarms;
- integrated system tests.

```text
installed
≠ tested
≠ commissioned
≠ accepted
```

Đây là pattern giống authorization/settlement ở finance.

## 13. Hàn Quốc

Korea có dense high-rise/apartment ecosystem, stringent building/fire/seismic rules và large domestic construction/engineering firms. MOLIT quản lý architecture/construction policy; building safety, seismic standards và green-building certification là các policy layers quan trọng.

Dense apartment complexes tạo standardized operation patterns: central management office, common MEP, parking, elevators, waste/recycling points và district/central heating tùy project.

Korean building market cũng có mạnh redevelopment/reconstruction của aging apartment stock, nên lifecycle không kết thúc ở maintenance mà có thể đi tới retrofit/redevelopment.

## 14. Việt Nam

Việt Nam đang đô thị hóa nhanh với lượng lớn apartment, commercial, industrial và infrastructure construction. Luật Xây dựng và các thông tư phân cấp/cấp công trình tạo framework cho quản lý design, permits, construction và acceptance.

Năm 2026, Bộ Xây dựng ban hành Thông tư 34/2026/TT-BXD về cấp công trình, có hiệu lực 1/7/2026. Đây là ví dụ cho thấy classification không phải detail hành chính nhỏ: cấp công trình có thể ảnh hưởng requirements/quyền quản lý và procedures.

Rapid construction tạo challenge song song:

```text
build fast
+ ensure code compliance
+ coordinate utilities
+ fire safety
+ long-term maintenance
```

## 15. Korea ↔ Vietnam

| Lớp | Hàn Quốc | Việt Nam |
|---|---|---|
| Urban building stock | Mature high-rise/apartment-heavy | Rapidly expanding high-rise/industrial stock |
| Core challenge | aging stock, retrofit/redevelopment, energy performance | growth, quality consistency, infrastructure coordination, maintenance maturity |
| Construction ecosystem | Large mature contractors/engineering supply chain | Large domestic + foreign contractors, fast-growing supply chain |
| Building operations | Professional apartment/FM ecosystems widespread | FM capacity expanding with newer urban stock |
| Regulatory pressure | seismic/fire/green retrofit and mature codes | evolving codes/classification, fire/safety and rapid-growth enforcement |

Không nên so bằng “building hiện đại hơn”. Một building mới ở Việt Nam có thể dùng technology rất mới; khác biệt lớn hơn nằm ở maturity của surrounding network, maintenance practices và stock age.

## 16. Building failures lan sang hệ thống khác thế nào?

- Pump failure → upper-floor water loss dù city water main vẫn có nước.
- Transformer failure → building outage dù neighborhood grid bình thường.
- Sewer blockage → local flooding/backflow.
- Elevator outage → accessibility failure trong high-rise.
- BMS/network issue → HVAC control degrade dù chillers còn tốt.
- Fire system failure → occupancy/safety impact.

Building boundary rất quan trọng: municipal utility có thể khỏe nhưng internal building infrastructure vẫn fail.

## 17. Finality

Project “hoàn thành xây dựng” chưa đồng nghĩa ready for occupancy.

```text
physical work complete
→ testing
→ commissioning
→ inspection/acceptance
→ occupancy/handover
→ defects liability
→ operation/maintenance
```

Sau handover, asset chuyển từ project system sang operations system.

## Đọc tiếp

- [Electricity grid](../electricity-grid/README.md)
- [Water supply](../water-supply/README.md)
- [Sewage](../sewage/README.md)
- [Waste/recycling](../waste-recycling/README.md)
- [Internet](../internet/README.md) và [mobile networks](../mobile-networks/README.md)
- [`../../personal-finance/`](../../personal-finance/) nếu domain này đã được canonical hóa cho housing finance; chapter hiện tại chỉ sở hữu building mechanism.

Mental model:

```text
Building
= project lifecycle
+ structure
+ MEP infrastructure
+ control systems
+ safety systems
+ commissioning
+ long-term operations
```

## Nguồn chính thức tham chiếu

- Korea Ministry of Land, Infrastructure and Transport — Architecture / Construction: https://www.molit.go.kr/english/
- Vietnam Ministry of Construction: https://moc.gov.vn/
