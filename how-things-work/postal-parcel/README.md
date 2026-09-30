# Postal & Parcel Network — một kiện hàng nhỏ đi qua mạng lưới như thế nào?

Parcel logistics khác container shipping ở scale và granularity. Container network tối ưu lô hàng lớn qua port/ship; parcel network phải xử lý hàng triệu object nhỏ, mỗi object có address, barcode, service level và tracking events riêng.

## 1. Một parcel bắt đầu bằng data trước khi bắt đầu di chuyển

```text
order created
   ↓
shipping label generated
   ↓
barcode / tracking ID
   ↓
parcel accepted
   ↓
origin sort
   ↓
linehaul
   ↓
destination sort
   ↓
last-mile route
   ↓
delivery confirmation
```

Tracking ID là key nối physical parcel với digital state machine.

## 2. Address normalization tại sao quan trọng?

Con người có thể hiểu một địa chỉ viết hơi sai; sorting machine thì cần structure rõ hơn.

System thường chuyển:

```text
raw address text
      ↓
normalization / postcode lookup
      ↓
geocoding / delivery-zone mapping
      ↓
sort plan
```

Apartment number, building name, street address và postcode đều giúp giảm ambiguity.

## 3. Hub-and-spoke

Parcel network hiếm khi gửi trực tiếp origin → destination.

```text
local pickup depot
      ↓
regional sorting hub
      ↓
linehaul truck / air
      ↓
destination hub
      ↓
local delivery depot
      ↓
recipient
```

Hub tăng consolidation: thay vì mọi depot nối trực tiếp với mọi depot, network gom flow về một số node throughput cao.

## 4. Sorting automation

Một automated sort center có thể dùng:

```text
induction
  ↓
barcode/OCR scan
  ↓
weight + dimension
  ↓
sort decision
  ↓
conveyor / diverter
  ↓
destination chute / bag / cage
```

Korea Post còn dùng route-sequencing equipment cho mail: address được đọc và item được xếp theo **delivery route sequence (순로)** để giảm walking/driving time của courier.

## 5. Tracking event không phải GPS continuous tracking

Khi app hiện:

```text
Accepted
→ Departed origin hub
→ Arrived destination hub
→ Out for delivery
→ Delivered
```

đa số event là scan/state transition tại nodes. Parcel có thể đang ở truck giữa hai hub nhưng system không biết vị trí centimeter-by-centimeter.

Tracking quality phụ thuộc scan discipline và event integration.

## 6. Last mile là đoạn đắt và khó nhất

Linehaul truck có thể chở hàng nghìn parcel. Last-mile courier phải dừng nhiều lần cho từng address.

```text
1000 parcels in one truck between hubs
             ↓
10–200 parcels per local route
             ↓
many stops + elevators + access codes + failed delivery
```

Density cao giúp economics: apartment complexes ở Seoul hoặc dense districts tại Hà Nội/TP.HCM cho phép nhiều delivery trong bán kính nhỏ.

## 7. Route planning

Dispatcher/courier cần giải:

- parcel volume;
- vehicle capacity;
- stop sequence;
- promised delivery windows;
- apartment access;
- traffic;
- pickup returns;
- failed delivery risk.

Đây gần với Vehicle Routing Problem trong optimization nhưng thực tế có rất nhiều constraints không hoàn hảo.

## 8. Korea: Korea Post + commercial parcel ecosystem

Korea Post cung cấp universal postal service cùng parcel/EMS. Korea có parcel density rất cao nhờ e-commerce, urban density và address infrastructure. Bên cạnh Korea Post còn có large commercial parcel networks.

Một flow domestic điển hình:

```text
merchant / post office pickup
       ↓
local handling center
       ↓
automated sorting hub
       ↓
regional linehaul
       ↓
delivery post office/depot
       ↓
route-sequenced courier delivery
```

Korea Post công bố các automated sorters có OCR/postcode recognition và route sequencing, cho thấy “post office” thực chất là một data + automation network lớn.

## 9. Việt Nam: postal network + e-commerce logistics

Vietnam Post và các commercial couriers vận hành mạng pickup, sortation, inter-provincial linehaul và last-mile. Growth của e-commerce làm parcel network ngày càng giống digital fulfillment network hơn postal network truyền thống.

Challenge đặc trưng:

- address quality không đồng nhất;
- alley/narrow-road access;
- COD vẫn là payment mode đáng kể ở nhiều segment;
- inter-provincial geography dài theo trục Bắc–Nam;
- peak events tạo volume spike lớn.

COD làm parcel state nối thêm banking/payment:

```text
parcel delivered
      ↓
cash/payment collected
      ↓
reconciliation
      ↓
merchant remittance
```

Vì vậy “Delivered” chưa chắc merchant đã nhận tiền.

## 10. Korea ↔ Vietnam

| Lớp | Hàn Quốc | Việt Nam |
|---|---|---|
| Address/density | Dense urban addresses, apartment-heavy | Dense cities + more heterogeneous address/access patterns |
| Sorting automation | Mature high-throughput automated hubs | Automation expanding rapidly with e-commerce volume |
| Last mile | High drop density, parcel boxes/managed buildings common | Motorbike-based last mile very important in dense urban areas |
| Payment coupling | Mostly prepaid e-commerce flows | COD/reconciliation remains more visible in many flows |
| Geography | Compact national territory | Long north–south geography increases linehaul design importance |

## 11. International parcel adds customs

```text
origin acceptance
   ↓
export processing
   ↓
international air/sea linehaul
   ↓
import customs
   ↓
duties/taxes if applicable
   ↓
domestic delivery network
```

Tracking gap often occurs at handoff between postal/courier/customs systems.

## 12. Returns reverse the network

E-commerce return:

```text
customer return request
   ↓
label / pickup
   ↓
reverse sort
   ↓
merchant return center
   ↓
inspection
   ↓
restock / refurbish / dispose
   ↓
refund settlement
```

Reverse logistics can cost disproportionately because flow is less predictable than outbound fulfillment.

## 13. Failure cases

- Barcode damaged → manual exception handling.
- Address invalid → delivery delay / return-to-sender.
- Hub outage → backlog propagates across many routes.
- Snow/typhoon/flood → linehaul and last mile both affected.
- Cloud/IT outage → parcels still exist physically but routing/tracking state may freeze.
- Payment/COD reconciliation error → physical delivery final but financial state unresolved.

## 14. Finality

Parcel system has multiple “final” states depending stakeholder:

```text
carrier: proof of delivery captured
customer: parcel received intact
merchant: order completed + payment settled
inventory system: shipment state closed
```

Một scan `Delivered` là evidence mạnh nhưng không đồng nghĩa mọi dispute/financial state đã kết thúc.

## Đọc tiếp

- [Shipping logistics](../shipping-logistics/README.md) cho container/port/global freight.
- [Road traffic](../road-traffic/README.md) cho linehaul/last-mile reliability.
- [Cloud computing](../cloud-computing/README.md) cho tracking backend.
- [Supermarkets](../supermarkets/README.md) cho inventory/replenishment logic.
- [Banking](../banking-system/README.md) cho COD/remittance/payment settlement.

Mental model:

```text
Parcel network
= identity + address
+ sorting
+ consolidation
+ linehaul
+ route planning
+ last mile
+ event tracking
+ exception handling
```

## Nguồn chính thức tham chiếu

- Korea Post — postal services and automation: https://www.koreapost.go.kr/ ; https://postman.koreapost.go.kr/jodal/
- Vietnam Post: https://vnpost.vn/
