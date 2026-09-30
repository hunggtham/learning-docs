# System Map — 22 hệ thống thực ra nối với nhau như thế nào?

Nếu đọc từng chapter riêng lẻ, rất dễ hình dung Internet, điện, ngân hàng, metro, road, buildings hay waste là những thế giới độc lập. Ngoài đời chúng tạo thành một **hệ thống của các hệ thống (system of systems / 시스템의 시스템)**: một hệ thống thường vừa cung cấp đầu vào cho hệ thống khác, vừa phụ thuộc ngược trở lại vào nó.

Tệp này không thay chapter chi tiết. Nó trả lời câu hỏi: **nếu một sự kiện xảy ra ở một lớp, nó có thể truyền sang các lớp khác bằng đường nào?**

## 1. Năm dòng chảy nền tảng

Phần lớn 22 chapter có thể nhìn bằng năm dòng chảy:

```text
ENERGY FLOW
fuel / renewable resource
        ↓
electricity grid
        ↓
buildings / data center / telecom / factory / metro / airport

INFORMATION FLOW
sensor / user / terminal
        ↓
mobile network / Internet
        ↓
cloud / control systems
        ↓
decision / command / information

MONEY FLOW
customer / company
        ↓
payment rail / banking / market
        ↓
clearing + settlement
        ↓
merchant / operator / investor

PHYSICAL FLOW
raw material / product / parcel / passenger
        ↓
factory / warehouse / road / rail / port / airport
        ↓
store / building / consumer

WASTE / RETURN FLOW
consumer / building / factory
        ↓
collection / reverse logistics / sewage
        ↓
sorting / treatment / recycling / disposal
```

Một system thật thường dùng nhiều flow cùng lúc. Ví dụ một apartment cần energy, water, Internet và parcel delivery; đồng thời tạo wastewater và solid waste.

## 2. Dependency graph tổng quát

```text
                              ┌──────────────┐
                              │ Satellites   │
                              └──────┬───────┘
                                     │ GNSS / EO / timing
                                     ▼
┌──────────────┐       ┌──────────────────┐       ┌───────────────┐
│Electricity   │──────▶│Mobile networks   │──────▶│ Internet      │
│grid          │       └────────┬─────────┘       └──────┬────────┘
└──────┬───────┘                │                         │
       │                        │                         ▼
       │                        │                  ┌───────────────┐
       │                        └─────────────────▶│Cloud computing│
       │                                           └──────┬────────┘
       │                                                  │
       ▼                                                  ▼
┌──────────────┐                                  ┌─────────────────┐
│Buildings     │◀──── water / sewer / telecom ───▶│City utilities   │
└──────┬───────┘                                  └─────────────────┘
       │
       ├──▶ waste/recycling
       ├──▶ parcel/postal deliveries
       └──▶ public transport / roads for occupants

Semiconductors ─▶ devices / radios / servers / vehicles / control systems

Banking ─▶ card/payment ─▶ retail / transit fares / tolls / fuel / e-commerce
   │
   └────────────▶ stock market settlement

Fuel/oil ─▶ road vehicles / aviation / industry

Road traffic ─▶ buses / parcel / supermarkets / ports / airport access
     │
     └────────▶ public transport network

Shipping logistics ─▶ factories / fuel / supermarkets / parcel imports

Airports + Airlines ─▶ passenger/cargo mobility
```

Mũi tên không phải quan hệ một chiều. Cloud giúp control electricity/transport, nhưng cloud lại cần điện và telecom. Public transport giảm road demand, nhưng bus lại phụ thuộc road network.

## 3. Những hạ tầng nền có blast radius lớn

### Electricity

Không có điện ổn định, cell tower, pump, traffic signal, fare gate, sorting hub, refinery terminal, elevator, data center và airport systems đều chịu ảnh hưởng. Battery/generator chỉ tạo **time buffer**.

### Telecom + Internet

Nhiều physical systems vẫn nguyên vẹn nhưng control/information layer biến mất khi connectivity lỗi: toll gate, fare backend, parcel tracking, BMS remote control, POS và ETA apps.

### Road network

Road là hidden dependency của bus, parcel last-mile, supermarket restock, waste collection, fuel distribution, airport access và construction supply.

### Banking/payment

Physical action có thể xong nhưng financial state chưa final: parcel delivered nhưng COD chưa remitted; card approved nhưng merchant chưa settled; toll passage recorded nhưng account reconciliation chưa xong.

### Buildings

Một large building tập trung nhiều dependencies. Municipal utilities có thể khỏe nhưng internal transformer, pumps, risers hoặc BMS fail làm users mất service.

## 4. Control plane vs physical/data plane lặp lại ở mọi domain

```text
Electricity
control: dispatch / market schedule
physical: generator + grid

Public transport
control: OCC / timetable / signaling / dispatch
physical: buses / trains / tracks

Road
control: signal plans / ITS / toll backend
physical: asphalt / lanes / vehicles

Building
control: BMS / controllers
physical: pumps / fans / switchgear / pipes

Cloud
control: API / scheduler
physical/data: CPU / storage / packets

Waste
control: collection schedule / route plan / facility acceptance
physical: waste / trucks / sorting / treatment

Fuel
control: contracts / inventory planning / dispatch
physical: crude/product / tanks / pipelines / trucks
```

Khi debug, hỏi **control plane hỏng hay physical flow hỏng?** là cách thu hẹp root cause rất mạnh.

## 5. Execution không đồng nghĩa finality

Pattern chung:

```text
Intent
  ↓
Validation
  ↓
Execution / acceptance
  ↓
Reconciliation / processing
  ↓
Settlement / final state
```

Examples:

- Card: `APPROVED` ≠ merchant settled.
- Stock: `FILLED` ≠ securities/cash settled.
- Parcel: `Out for delivery` ≠ delivered; `Delivered` ≠ merchant remitted for COD.
- Transit: gate opened ≠ final fare cleared among operators.
- Toll: vehicle passed ≠ transaction reconciliation final.
- Construction: installed ≠ commissioned ≠ accepted.
- Satellite: image captured ≠ usable validated data product.
- Waste: collected ≠ recycled.

## 6. Buffer làm failure bị trì hoãn

Nhiều systems có inventory/capacity buffer:

```text
power outage → battery / UPS / generator
water outage → building tank
fuel shock → commercial/strategic reserves
parcel peak → warehouse/hub backlog capacity
cloud spike → spare compute capacity
transit disruption → alternate route/mode
```

Buffer làm symptom xuất hiện muộn hơn root failure. Vì vậy timestamp của user complaint không nhất thiết là timestamp của failure ban đầu.

## 7. System coupling theo urban life

### Một ngày trong apartment

```text
Electricity + water + sewer + telecom
             ↓
building systems
             ↓
resident
   ├─ commute via road/transit
   ├─ payment via banking/card
   ├─ receives parcel
   └─ produces wastewater/waste
```

### Một store

```text
electricity
+ Internet/cloud
+ card/banking
+ road/parcel/logistics
+ building utilities
+ waste collection
= retail operation
```

### Một airport

```text
electricity
+ fuel
+ road/public transport access
+ telecom/cloud
+ banking/payment
+ GNSS
+ airlines
= passenger/cargo operation
```

## 8. Hàn Quốc ↔ Việt Nam: maturity topology khác nhau

Cả hai nước dùng nhiều technology/standards giống nhau, nhưng system topology khác do density, geography, infrastructure age và investment cycle.

Pattern đơn giản hóa:

```text
Korea
mature/dense network
      ↓
optimize capacity + resilience + aging assets + integration

Vietnam
rapid expansion / mixed legacy-new infrastructure
      ↓
build capacity + standardize + integrate + operate simultaneously
```

Không phải ranking. Một new Vietnamese system có thể dùng modern technology ngay từ đầu, trong khi Korea phải retrofit legacy assets.

## 9. Những feedback loop quan trọng

### Transit ↔ road

```text
better transit
→ fewer road trips
→ less congestion
→ bus reliability improves
→ transit becomes more attractive
```

hoặc ngược lại.

### E-commerce ↔ parcel ↔ road

```text
more e-commerce
→ more parcel volume
→ more last-mile vehicles
→ congestion / delivery cost
→ demand for hubs / automation / lockers
```

### EV ↔ fuel ↔ grid

```text
more EVs
→ less gasoline demand
→ more electricity demand
→ charging load + grid investment
```

### Cloud/AI ↔ semiconductor ↔ electricity

```text
AI demand
→ GPU/HBM demand
→ semiconductor investment
→ data-center expansion
→ electricity/cooling demand
```

## 10. Năm câu hỏi để “mổ” bất kỳ hệ thống nào

1. **Flow:** thứ gì đang di chuyển — electricity, packet, money, people, material, waste?
2. **State:** hệ thống phải nhớ trạng thái nào và source of truth ở đâu?
3. **Control:** ai route, schedule, authorize, price hoặc dispatch?
4. **Finality:** khi nào process được coi là hoàn tất?
5. **Failure:** một node chết thì failure bị cô lập hay lan sang system khác?

Thêm ba câu khi so Hàn ↔ Việt:

6. **Ownership:** ai sở hữu asset?
7. **Operator:** ai vận hành real-time?
8. **Bottleneck:** capacity bị giới hạn ở đâu hiện nay?

## Đọc tiếp

- [`KOREA_VIETNAM_COMPARISON.md`](./KOREA_VIETNAM_COMPARISON.md) cho topology song song.
- [`case-studies/`](./case-studies/README.md) cho các flow thực tế.
- [README chính](./README.md) cho 22 chapter chi tiết.
