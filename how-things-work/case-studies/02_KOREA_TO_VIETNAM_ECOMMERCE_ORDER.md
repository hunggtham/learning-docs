# Case Study 02 — Đặt một món hàng từ Hàn Quốc về Việt Nam

Một nút `Buy now` có thể tạo ra ba dòng chảy hoàn toàn khác nhau:

```text
INFORMATION FLOW
browser → cloud → seller → warehouse → carrier → customs → tracking

MONEY FLOW
buyer → payment rail → issuer/bank → merchant/acquirer → seller

PHYSICAL FLOW
warehouse → truck → airport/port → aircraft/ship → customs → last-mile → buyer
```

Ba flow có liên hệ nhưng không di chuyển cùng tốc độ. Payment có thể được authorized trong vài giây, warehouse chỉ pick hàng vài giờ sau, còn physical delivery mất nhiều ngày.

## 1. Bạn mở trang sản phẩm

```text
Phone / laptop
     ↓
DNS
     ↓
Internet / CDN
     ↓
e-commerce frontend
     ↓
API
     ↓
product catalog / inventory / pricing / recommendation services
```

Ảnh sản phẩm có thể đến từ CDN/object storage, giá và inventory từ database/cache, recommendation từ service khác. Vì vậy một trang “đơn giản” thường là composition của nhiều service.

Đọc [Internet](../internet/README.md) và [Cloud computing](../cloud-computing/README.md).

## 2. `In stock` không có nghĩa món hàng đang nằm ngay cạnh người bán

E-commerce inventory có thể nằm tại:

```text
seller warehouse
3PL fulfillment center
marketplace fulfillment center
store inventory
supplier inventory
cross-border bonded warehouse
```

UI `in stock` là projection của inventory data chứ không phải camera nhìn trực tiếp vào một chiếc hộp. Overselling xảy ra nếu nhiều order cạnh tranh cho cùng quantity hoặc inventory sync chậm.

Một architecture thường cần bước **reservation**:

```text
available = 10
order requests 1 unit
      ↓
reserve 1
available-to-promise = 9
```

Reservation có timeout để tránh một checkout bỏ dở giữ inventory mãi.

## 3. Checkout tạo order state machine

Một order không chỉ có `paid/unpaid`. Mental model tốt hơn:

```text
CREATED
  ↓
PAYMENT_PENDING
  ↓
PAID / AUTHORIZED
  ↓
ALLOCATED
  ↓
PICKING
  ↓
PACKED
  ↓
HANDED_TO_CARRIER
  ↓
EXPORT_CUSTOMS
  ↓
INTERNATIONAL_TRANSIT
  ↓
IMPORT_CUSTOMS
  ↓
LAST_MILE
  ↓
DELIVERED
```

Có thể có nhánh `CANCELLED`, `PAYMENT_FAILED`, `RETURNED`, `LOST`, `CUSTOMS_HOLD`.

Một hệ thống tốt không giả định mọi order luôn đi thẳng xuống dưới.

## 4. Payment xảy ra trước physical fulfillment

Nếu thanh toán bằng card:

```text
Browser/app
   ↓
Payment gateway
   ↓
Acquirer
   ↓
Card network
   ↓
Issuer
   ↓
Authorization result
```

Nếu dùng bank transfer hoặc rail khác, route thay đổi. Cross-border e-commerce còn có thể thêm FX conversion, foreign merchant acquiring, payment service provider hoặc marketplace settlement.

Điểm phải nhớ:

```text
payment authorization time
≠ merchant settlement time
≠ seller payout time
```

Marketplace có thể giữ tiền rồi payout cho seller theo schedule sau khi trừ fee/refund reserve. Xem [Credit card network](../credit-card-network/README.md) và [Banking system](../banking-system/README.md).

## 5. Currency conversion diễn ra ở đâu?

Giả sử hàng niêm yết bằng KRW nhưng buyer trả bằng VND/card account khác currency. Conversion có thể xảy ra ở issuer/card network/payment provider/merchant-side arrangement tùy cấu trúc giao dịch.

Không nên suy nghĩ đơn giản:

```text
KRW price × Google exchange rate = số tiền cuối
```

Final cost có thể gồm exchange rate applied by relevant institution, card/network/FX fee, cross-border fee, tax/duties và merchant pricing.

## 6. Warehouse biến digital order thành physical parcel

Sau khi order được release cho fulfillment:

```text
Order Management System
       ↓
Warehouse Management System
       ↓
pick task
       ↓
worker / robot retrieves SKU
       ↓
scan
       ↓
pack
       ↓
label
       ↓
sort by carrier / route
```

Barcode scan ở mỗi checkpoint giúp hệ thống chuyển state từ “nên tồn tại ở vị trí X” sang “đã được scan tại vị trí Y”.

Tracking vì vậy không phải GPS liên tục của parcel. Phần lớn tracking là chuỗi event do scanner/system ghi tại checkpoint.

## 7. Chọn air cargo hay sea freight

Với parcel e-commerce nhỏ, air transport thường phù hợp hơn vì lead time. Với hàng bulk/container, sea freight có economics khác.

```text
Air
higher cost per kg
faster transit
capacity constrained by flights/aircraft

Sea
lower unit cost for large volumes
slower transit
container + port dependent
```

Marketplace/forwarder còn có thể consolidate nhiều parcel nhỏ thành shipment lớn rồi deconsolidate ở destination.

Đọc [Shipping logistics](../shipping-logistics/README.md), [Airlines](../airlines/README.md) và [Airports](../airports/README.md).

## 8. Export side tại Hàn Quốc

Một simplified path:

```text
Seller / fulfillment center
    ↓ truck
Consolidation / forwarder
    ↓
Export declaration / security procedures
    ↓
Airport cargo terminal OR seaport terminal
    ↓
Aircraft / vessel
```

Seoul metro e-commerce fulfillment có thể kết nối mạnh với Incheon air cargo. Containerized commercial cargo có thể route qua Busan hoặc các cảng khác tùy origin, service và carrier network.

Không nên đồng nhất “Hàn Quốc xuất hàng” với “mọi hàng đều đi Busan” hoặc “mọi parcel đều đi Incheon”; route là optimization theo cargo type, geography, cost và schedule.

## 9. International leg: một shipment không nhất thiết đi thẳng

```text
Korea origin
    ↓
direct flight/vessel?
    ↓ or
regional hub / transshipment
    ↓
Vietnam gateway
```

Air parcel có thể transit qua hub. Container có thể đi direct hoặc feeder/mainline/transshipment tùy service network.

Đây là lý do tracking đôi khi cho thấy hàng đi qua một nước/thành phố không nằm trên “đường thẳng địa lý”. Logistics tối ưu theo network schedule chứ không chỉ khoảng cách bản đồ.

## 10. Import side tại Việt Nam

Physical arrival không đồng nghĩa được giao ngay:

```text
arrival
   ↓
manifest / customs data
   ↓
import customs assessment
   ↓
duties/taxes if applicable
   ↓
inspection/clearance if required
   ↓
release
   ↓
local sorting hub
   ↓
last-mile delivery
```

Một parcel có thể nằm tại gateway trong khi tracking vẫn “đã đến Việt Nam” vì customs state chưa final.

## 11. Customs là information system gắn với physical control

Customs không chỉ “mở hộp kiểm tra”. Hệ thống dựa nhiều vào declaration data, classification, value, origin, risk assessment và document matching.

```text
physical cargo
      ↕
customs declaration
      ↕
risk engine / rules
      ↕
release / inspection decision
```

Nếu dữ liệu sai, physical cargo có thể bị hold dù network transport hoạt động bình thường.

## 12. Last-mile: phần cuối nhưng thường đắt và khó

International transport có thể đưa hàng hàng nghìn km rất hiệu quả nhờ scale. Last-mile phải đưa một parcel tới một address cụ thể:

```text
regional hub
  ↓
local depot
  ↓
route assignment
  ↓
van / motorcycle
  ↓
customer
```

Urban density cao có thể giảm distance per stop nhưng traffic, parking, apartment access và failed delivery tạo cost khác.

Korea có dense urban logistics và apartment delivery infrastructure trưởng thành. Việt Nam có motorcycle-based last-mile rất mạnh, address/urban form đa dạng và e-commerce delivery network mở rộng nhanh.

## 13. Tracking page là một distributed projection

Khi bạn thấy:

```text
Order confirmed
Picked up
Departed origin
Arrived destination
Customs clearance
Out for delivery
Delivered
```

đó là event từ nhiều actor được gom thành một timeline. Các event có thể đến trễ hoặc out of order.

Do đó:

```text
tracking UI
≠ perfect real-time physical truth
```

Nó là best-known logical state của shipment.

## 14. Nếu payment thành công nhưng hàng thất lạc?

Financial và physical system tách nhau nên cần refund/dispute flow:

```text
physical failure
      ↓
merchant/carrier investigation
      ↓
refund / replacement decision
      ↓
payment reversal/refund
      ↓
issuer/customer statement update
```

Nếu merchant không giải quyết, card dispute/chargeback có thể trở thành lớp risk allocation sau cùng tùy rail và rule.

## 15. Failure propagation examples

### Cloud outage

Website/order API lỗi → không tạo order mới, dù warehouse và aircraft vẫn chạy.

### Payment outage

Catalog vẫn mở, inventory vẫn tồn tại nhưng checkout fail.

### Port/airport congestion

Order và payment hoàn tất nhưng physical flow chậm.

### Customs hold

International transport hoàn thành nhưng legal state chưa cho phép last-mile.

### Typhoon/weather

Flight/vessel delay → hub backlog → warehouse/depot capacity pressure → tracking và customer-support volume tăng.

Một physical disruption vì vậy có thể lan ngược thành software/support/payment-refund load.

## 16. Korea ↔ Vietnam — điều gì thực sự khác?

Không phải TCP/IP hay container standard. Khác biệt nằm nhiều ở:

```text
warehouse network topology
international gateway location
carrier/service frequency
customs process
last-mile vehicle mix
payment behavior
FX/cross-border payment structure
urban density and address topology
```

Vì vậy cùng một marketplace software có thể cần operational design khác ở hai nước.

## 17. Mental model cuối

Một cross-border order là **distributed transaction không có một atomic commit chung**.

Không có khoảnh khắc duy nhất mà cloud, bank, warehouse, customs, carrier và customer cùng commit một database transaction.

Thay vào đó:

```text
many independent systems
+ messages/events
+ retries
+ reconciliation
+ compensating actions such as refund/return
```

Đây chính là lý do logistics và commerce phải được thiết kế để chịu trạng thái “đang ở giữa”.

## Đọc tiếp

- [Internet](../internet/README.md)
- [Cloud computing](../cloud-computing/README.md)
- [Banking system](../banking-system/README.md)
- [Credit card network](../credit-card-network/README.md)
- [Shipping logistics](../shipping-logistics/README.md)
- [Airlines](../airlines/README.md)
- [Airports](../airports/README.md)
