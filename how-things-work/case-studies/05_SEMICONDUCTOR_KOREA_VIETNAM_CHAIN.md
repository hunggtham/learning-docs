# Case Study 05 — Một chip Hàn Quốc đi vào sản phẩm điện tử lắp ráp tại Việt Nam

Semiconductor supply chain thường bị kể như một đường thẳng: thiết kế → fab → packaging → product. Thực tế nó là một mạng nhiều tầng, nhiều quốc gia và nhiều vòng feedback. Hàn Quốc và Việt Nam là hai node rất khác nhau nhưng có thể nằm trong cùng một product chain.

Case này dùng một ví dụ tổng quát: memory/semiconductor component được sản xuất trong hệ sinh thái Hàn Quốc rồi đi vào sản phẩm điện tử được lắp ráp tại Việt Nam. Không giả định một công ty hay model cụ thể.

## 1. Product bắt đầu từ architecture, không phải wafer

Trước khi silicon được chế tạo, product team đã xác định:

```text
system requirements
   ↓
chip / memory requirements
   ↓
architecture + interface
   ↓
component selection / design
   ↓
supply contract / forecast
```

Một smartphone, SSD, server hoặc appliance dùng nhiều loại semiconductor khác nhau: processor, memory, power-management IC, RF components, sensors, connectivity chips và discrete devices.

Đọc [Semiconductors](../semiconductors/README.md).

## 2. Korea mạnh ở một số layer rất capital-intensive

Hàn Quốc có vị trí đặc biệt mạnh trong memory semiconductor và manufacturing ecosystem. Fab cần:

```text
clean room
+ lithography/deposition/etch equipment
+ gases/chemicals
+ ultrapure water
+ extremely stable electricity
+ process control
+ metrology
+ highly skilled engineering
```

Một fab không phải “nhà máy điện tử lớn”. Nó là chemical/physics manufacturing system với tolerance rất nhỏ và capital intensity cực cao.

## 3. Wafer không trở thành chip usable ngay sau fab

Sau front-end fabrication:

```text
wafer
  ↓
wafer test / probe
  ↓
dicing
  ↓
packaging
  ↓
final test
  ↓
binning / qualification
  ↓
shippable component
```

Packaging không chỉ “bọc nhựa”. Advanced packaging có thể quyết định bandwidth, thermals, power delivery và system performance, đặc biệt với HBM/AI accelerators.

## 4. Yield biến engineering thành economics

Giả sử 1 wafer có nhiều die nhưng không phải die nào cũng đạt spec. **Tỷ lệ đạt (yield / 수율)** ảnh hưởng trực tiếp cost per good die.

```text
same wafer cost
÷ more good dies
= lower effective cost per usable die
```

Yield phụ thuộc process maturity, defect density, die size và nhiều process variables. Đây là lý do ramp một node/process mới có thể ảnh hưởng cả supply và margin.

## 5. Component supply không chạy theo retail order từng chiếc

Electronics manufacturer thường forecast demand trước nhiều tuần/tháng:

```text
sales forecast
   ↓
production plan
   ↓
BOM demand
   ↓
component orders / allocation
   ↓
semiconductor production plan
```

**Danh mục vật tư (Bill of Materials, BOM / 자재 명세서)** nói một sản phẩm cần bao nhiêu component. Nếu forecast tăng, demand signal truyền ngược lên suppliers.

Nhưng semiconductor lead time dài nên supply không thể tăng tức thì.

## 6. Bullwhip effect có thể xuất hiện

Nếu downstream company sợ thiếu chip, họ có thể order nhiều hơn nhu cầu thật:

```text
true demand + safety buffer
        ↓
customer order
        ↓
supplier interprets as stronger demand
        ↓
capacity/order expansion
```

Khi shortage qua đi, inventory correction có thể khiến orders giảm rất mạnh dù end-user demand chỉ giảm nhẹ. Đây là **hiệu ứng roi da (bullwhip effect / 채찍 효과)** trong supply chain.

## 7. Logistics đưa component tới Việt Nam

Semiconductor có value density cao: giá trị lớn trên mỗi kg. Nhiều component phù hợp air cargo hơn bulk sea freight vì lead-time sensitivity.

```text
Korea factory / packaging site
   ↓
secure packing / ESD/moisture controls
   ↓
truck
   ↓
airport cargo terminal
   ↓
air freight
   ↓
Vietnam airport / customs
   ↓
factory / bonded logistics / supplier hub
```

Tuy nhiên route thực tế phụ thuộc component type, origin, contract, inventory strategy và manufacturing location.

Đọc [Airports](../airports/README.md), [Airlines](../airlines/README.md) và [Shipping logistics](../shipping-logistics/README.md).

## 8. Customs data và physical cargo phải khớp

Cross-border electronics components cần commercial documents/classification/origin/value phù hợp với rule hiện hành.

```text
physical shipment
     ↕
invoice / packing data
     ↕
customs declaration
     ↕
clearance state
```

Cargo đã hạ khỏi aircraft chưa có nghĩa factory có thể dùng ngay; customs/legal release là một state riêng.

## 9. Vietnam electronics factory làm gì?

Một electronics manufacturing site có thể thực hiện các bước như:

```text
incoming inspection
   ↓
SMT placement
   ↓
solder / reflow
   ↓
board/system assembly
   ↓
firmware / calibration
   ↓
functional test
   ↓
final assembly
   ↓
quality control
   ↓
packaging
```

Role cụ thể khác nhau theo facility: component assembly/test, PCB assembly, device manufacturing hoặc final system integration không phải một thứ.

Khi nói “Việt Nam sản xuất electronics/semiconductor”, phải phân biệt rõ layer nào của value chain.

## 10. Semiconductor manufacturing và electronics assembly khác nhau

```text
SEMICONDUCTOR FAB
creates transistor structures on wafer

SEMICONDUCTOR PACKAGING/TEST
turns die into qualified package/module

ELECTRONICS ASSEMBLY
mounts chips/components into boards/products
```

Ba layer cần capital, knowledge, equipment và supplier ecosystem khác nhau.

Đây là điểm rất quan trọng khi so sánh Korea ↔ Vietnam.

## 11. Korea ↔ Vietnam: complementary nodes hơn là cùng một vị trí

Một simplified mental model:

### Korea

```text
strong semiconductor manufacturing depth
+ memory leadership
+ materials/equipment/customer ecosystem
+ advanced electronics companies
```

### Vietnam

```text
electronics manufacturing / assembly scale
+ semiconductor design/packaging/test capability growing
+ FDI-linked supply chains
+ national push to deepen domestic semiconductor capability
```

Không nên suy ra rằng toàn bộ Korean semiconductor chain nằm ở Korea hoặc toàn bộ Vietnam electronics chain chỉ là assembly. Supply chains vượt biên giới và capability thay đổi theo thời gian.

## 12. Electricity là hidden dependency của cả hai đầu

Fab ở Korea cần power quality cực cao. Electronics plant ở Vietnam cũng cần stable power cho SMT lines, test systems, HVAC và production IT.

```text
Electricity disruption
     ↓
production stop
     ↓
WIP / lot impact
     ↓
restart + quality verification
     ↓
shipment delay
```

Xem [Power outage cascade](./04_POWER_OUTAGE_CASCADE.md) và [Electricity grid](../electricity-grid/README.md).

## 13. Water cũng quan trọng ở semiconductor fab

Front-end manufacturing dùng lượng lớn ultrapure water cho cleaning/process steps. Vì vậy semiconductor capacity phụ thuộc không chỉ electricity mà cả water infrastructure, treatment và environmental management.

```text
raw water
  ↓
advanced purification
  ↓
ultrapure water
  ↓
process use
  ↓
wastewater treatment / reuse/discharge controls
```

Đọc [Water supply](../water-supply/README.md) và [Sewage](../sewage/README.md).

## 14. Cloud và AI đẩy demand ngược về chip

Một AI user gửi request lên cloud:

```text
AI application
   ↓
cloud data center
   ↓
GPU / accelerator cluster
   ↓
HBM + networking + storage
   ↓
semiconductor demand
```

Vì vậy digital demand có thể truyền ngược xuống physical manufacturing.

Đây là một feedback loop lớn:

```text
AI/cloud demand
   ↓
chip demand
   ↓
fab/packaging capex
   ↓
power + water + equipment demand
   ↓
new capacity
   ↓
cloud supply
```

Đọc [Cloud computing](../cloud-computing/README.md).

## 15. Inventory có thể nằm ở nhiều node

```text
semiconductor supplier inventory
in-transit inventory
Vietnam hub inventory
factory line-side inventory
finished-goods inventory
retailer/distributor inventory
```

Một shortage headline không nói node nào thiếu. Có thể fab output đủ nhưng logistics chậm; hoặc component có nhưng đúng package/spec thiếu; hoặc finished product tồn kho cao dù upstream chip order giảm.

## 16. Lead time khiến system phản ứng chậm

Nếu consumer demand tăng hôm nay, một fab mới không thể xuất hiện tuần sau. Capacity expansion có thể cần:

```text
site + permits
facility construction
clean room
tool delivery
installation
qualification
yield ramp
customer qualification
```

Do đó semiconductor supply chain có **độ trễ vốn (capital lag / 자본 시차)** rất lớn. Đây là lý do ngành có cycle mạnh.

## 17. Failure examples

### Fab disruption ở Korea

Supply loss có thể chỉ lộ rõ downstream sau khi buffer inventory cạn.

### Air cargo disruption

Chip đã sản xuất nhưng Vietnam line thiếu component đúng lúc.

### Vietnam factory disruption

Chip supplier vẫn giao nhưng finished-product output giảm, sau đó upstream orders có thể điều chỉnh.

### Demand collapse

Finished goods build up → factory cuts production → component inventory rises → semiconductor orders fall → fab utilization/price pressure.

## 18. Stock market nhìn cùng system ở một lớp khác

Investor có thể nhìn:

```text
end demand
→ inventory
→ ASP
→ utilization
→ capex
→ revenue/margin
→ valuation
```

Nhưng `how-things-work/` chỉ sở hữu physical/operating mechanism. Phân tích investment của Korea/Vietnam markets thuộc [`../../investing/`](../../investing/README.md).

## 19. Mental model cuối

Đừng vẽ semiconductor chain như một đường duy nhất. Hãy nghĩ như network:

```text
EDA/IP/tools/materials
        ↓
design ↔ fabrication ↔ packaging/test
        ↓
component distribution
        ↓
electronics manufacturing
        ↓
logistics
        ↓
consumer / cloud / telecom / auto demand
        ↘____________________________↗
             demand feedback
```

Hàn Quốc và Việt Nam đứng ở các node khác nhau của cùng global network, và value chain có thể sâu thêm theo thời gian.

## Đọc tiếp

- [Semiconductors](../semiconductors/README.md)
- [Electricity grid](../electricity-grid/README.md)
- [Water supply](../water-supply/README.md)
- [Shipping logistics](../shipping-logistics/README.md)
- [Airports](../airports/README.md)
- [Cloud computing](../cloud-computing/README.md)
