# Fuel & Oil Supply — xăng dầu đi từ crude oil tới cây xăng như thế nào?

Khi đổ xăng, người dùng thấy một pump và một giá bán lẻ. Phía sau là chuỗi toàn cầu: crude production → tanker → refinery → storage terminal → wholesale distribution → truck/pipeline → retail station. Đây là một hệ thống vừa vật lý, vừa tài chính, vừa địa chính trị.

## 1. Crude oil khác petroleum product

Crude oil là hỗn hợp hydrocarbon. Refinery tách/chuyển đổi thành nhiều product:

```text
crude oil
   ↓ refinery
├─ LPG
├─ gasoline
├─ naphtha
├─ jet fuel / kerosene
├─ diesel
├─ fuel oil
└─ petrochemical feedstocks
```

Một quốc gia có refinery không có nghĩa tự chủ crude. Nó có thể nhập phần lớn crude nhưng refine trong nước.

## 2. End-to-end flow

```text
oil field / crude exporter
      ↓ tanker
import terminal
      ↓
refinery / crude storage
      ↓ refining
product tank farm
      ↓ pipeline / coastal ship / tank truck
regional depot
      ↓
retail fuel station / airport / factory
      ↓
vehicle / aircraft / industrial user
```

Mỗi layer có inventory buffer. Supply resilience phụ thuộc tổng thể chứ không chỉ “còn dầu trong refinery”.

## 3. Refinery là một network của process units

Simplified:

```text
crude distillation
      ↓
fraction streams
      ↓
conversion units
(cracking / reforming / hydroprocessing)
      ↓
blending
      ↓
finished product specs
```

Product phải đạt sulfur, octane/cetane, vapor pressure và nhiều quality specs. Blending là bài toán optimization giữa feedstock, demand và regulation.

## 4. Inventory có nhiều tầng

```text
strategic reserve
commercial reserve
refinery feedstock inventory
terminal inventory
station inventory
```

**Dự trữ chiến lược (strategic petroleum reserve / 전략비축유)** tồn tại để chịu shock lớn; commercial inventory phục vụ hoạt động thường ngày.

Không nên cộng tất cả rồi nói “có X ngày dự trữ” nếu definition khác nhau.

## 5. Price transmission

Retail price không chỉ là crude price.

```text
crude/product international price
+ freight
+ refining margin
+ storage/distribution
+ wholesale/retail margin
+ taxes / levies / policy components
+ FX
= retail price
```

Với Hàn Quốc, KRW/USD matters. Với Việt Nam, VND và cơ chế quản lý/điều hành giá trong nước cũng ảnh hưởng timing truyền dẫn.

## 6. Hàn Quốc: import-dependent nhưng refinery/storage infrastructure rất lớn

Hàn Quốc có mức phụ thuộc nhập khẩu dầu cao nhưng đồng thời sở hữu refinery/petrochemical capacity và commercial/strategic storage lớn. Korea National Oil Corporation (KNOC / 한국석유공사) vận hành strategic stockpiling và oil-information infrastructure.

Tính đến tháng 8/2026, KNOC công bố chín stockpiling bases với capacity khoảng 146 triệu barrels và khoảng 100 triệu barrels reserve do KNOC nắm giữ, không tính international joint stockpiling. Đây là strategic buffer, không phải toàn bộ commercial inventory của quốc gia.

Korea còn phát triển Yeosu/Ulsan energy hubs cho commercial storage/trading. Vì vậy topology là:

```text
large crude imports
      ↓
large coastal refinery clusters
      ↓
strategic + commercial tank farms
      ↓
domestic product distribution
      ↓
retail / aviation / petrochemical users
```

## 7. Việt Nam: domestic refining + imports + nationwide distribution

Việt Nam có domestic refineries nhưng vẫn cần cân đối giữa crude/feedstock, refinery output và imported petroleum products. Bộ Công Thương theo dõi supply-demand, yêu cầu wholesalers/producers/distributors maintain sourcing and inventory plans và có contingency cho disruptions.

Trong 2026, policy focus bao gồm diversification of crude/product supply, vận hành refinery ổn định, commercial reserves và tiếp tục hoàn thiện framework petroleum trading.

```text
domestic crude + imported crude/products
              ↓
refineries / import terminals
              ↓
major wholesalers
              ↓
distributors / depots
              ↓
retail stations
```

Một local shortage có thể xảy ra dù national balance nhìn tổng thể đủ nếu distribution/incentive/inventory tại một region bị nghẽn.

## 8. Korea ↔ Vietnam

| Lớp | Hàn Quốc | Việt Nam |
|---|---|---|
| Crude dependency | Very high import dependency | Mix domestic production + imports; still exposed to imports/global prices |
| Refining | Large export-capable refining/petrochemical clusters | Domestic refineries important but imports remain part of balance |
| Strategic stockpile | KNOC institutional strategic stockpiling mature | Strategic/commercial reserve policy đang tiếp tục được tăng cường |
| Distribution | Dense mature terminal/pipeline/truck network | Nationwide wholesale/distributor/retail network with regional balancing challenge |
| Core risk | global crude shock, shipping chokepoints, FX | global price/shipping shock + domestic balancing/distribution + FX |

## 9. Fuel station operation

At station:

```text
tank truck delivery
   ↓
underground storage tank
   ↓
pump dispenser
   ↓
metering
   ↓
vehicle tank
```

Station must manage product segregation, tank inventory, vapor/safety controls và measurement accuracy.

Pump display là meter reading; financial payment đi qua separate POS/payment rail.

## 10. Airport jet fuel supply

Airline fuel chain khác retail car fuel:

```text
refinery/import
   ↓
airport fuel terminal
   ↓
quality control
   ↓
hydrant system / refueler truck
   ↓
aircraft
```

Fuel quality contamination là safety-critical. Airport disruption có thể đến từ fuel logistics dù runway/aircraft đều bình thường.

## 11. Biofuel và energy transition

Fuel system đang đổi bởi biofuel, EV và hydrogen nhưng legacy liquid-fuel infrastructure vẫn quan trọng.

EV adoption giảm gasoline demand nhưng tăng electricity demand:

```text
less gasoline
    ↓
more EV charging
    ↓
load shifts toward electricity grid
```

Nghĩa là transport energy dependency chuyển từ oil system sang [electricity grid](../electricity-grid/README.md), không biến mất.

## 12. Strategic reserve release hoạt động ra sao?

Reserve không phải stock “để đó vĩnh viễn”. Khi shock, authority có thể release/swap/loan inventory theo rules.

```text
supply disruption
   ↓
policy decision
   ↓
reserve barrels released
   ↓
refinery/market receives supply
   ↓
commercial distribution
```

Release có thể giảm physical scarcity nhưng không đảm bảo price quay về mức cũ nếu global market vẫn tight.

## 13. Bottlenecks

- Strait/shipping disruption → crude/product arrival delay.
- Refinery outage → product output drops.
- Port/terminal outage → inventory inaccessible.
- Tank-truck shortage → local stations run dry while terminal still has stock.
- Price/incentive mismatch → distributors may reduce movement.
- Electricity outage → terminal pumps, station pumps và refinery systems impacted.

## 14. Finality

Fuel supply có cả physical và commercial states:

```text
cargo contracted
→ loaded
→ shipped
→ discharged
→ quality/quantity accepted
→ title/payment settled
→ product distributed
```

Tanker “đã cập cảng” chưa có nghĩa product đã sẵn ở station.

## Đọc tiếp

- [Shipping logistics](../shipping-logistics/README.md): tanker/port flow.
- [Airlines](../airlines/README.md) và [airports](../airports/README.md): jet fuel demand.
- [Road traffic](../road-traffic/README.md): gasoline/diesel demand.
- [Electricity grid](../electricity-grid/README.md): EV transition và refinery/grid dependence.
- [`../../economics/`](../../economics/README.md): commodity prices, taxes, market structure.

Mental model:

```text
Fuel system
= global feedstock
+ refining
+ storage
+ transport
+ wholesale
+ retail
+ reserves
+ pricing/FX
```

## Nguồn chính thức tham chiếu

- Korea National Oil Corporation — stockpiling, oil hubs and statistics: https://www.knoc.co.kr/ENG/
- Vietnam Ministry of Industry and Trade — petroleum supply and market management: https://moit.gov.vn/
