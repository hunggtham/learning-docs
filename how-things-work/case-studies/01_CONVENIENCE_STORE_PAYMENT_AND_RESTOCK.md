# Case Study 01 — Mua một chai nước ở convenience store rồi hệ thống bổ sung hàng như thế nào?

Một giao dịch vài nghìn won ở Hàn Quốc hoặc vài chục nghìn đồng ở Việt Nam có thể kết thúc trong vài giây ở phía khách hàng. Nhưng phía sau nó là một chuỗi dài gồm điện, POS, mạng, thanh toán, ngân hàng, phần mềm bán lẻ, kho và logistics.

Case này không tập trung vào một chuỗi cửa hàng cụ thể. Mục tiêu là nhìn rõ **nhiều state machine chạy song song**.

## 1. Điểm bắt đầu: bạn lấy chai nước khỏi kệ

Trước cả lúc thanh toán, hệ thống đã có một trạng thái tồn kho (inventory state / 재고 상태) đại loại như:

```text
Store A
SKU: bottled-water-500ml
on_hand = 24
reserved = 0
available = 24
reorder_point = 8
```

Con số thật có thể không hoàn toàn khớp vật lý vì shrinkage, sai scan, hàng hỏng, theft hoặc receiving error. Điều quan trọng là retailer duy trì một **bản ghi logic** của hàng hóa để ra quyết định replenishment.

## 2. Barcode scan biến vật lý thành dữ liệu

Cashier hoặc self-checkout scan barcode:

```text
Barcode
   ↓
SKU lookup
   ↓
price / tax / promotion
   ↓
transaction basket
```

Barcode không “chứa toàn bộ thông tin sản phẩm”. Nó chủ yếu cung cấp identifier để POS/retail system lookup master data.

Nếu promotion kiểu `2+1`, loyalty discount hoặc coupon được áp dụng, pricing engine có thể phải kiểm tra rule từ local cache hoặc backend service.

## 3. POS phụ thuộc điện và network như thế nào?

POS cần ít nhất:

```text
Electricity
+ local store LAN/Wi-Fi
+ router/modem
+ connection to payment/retail backend
```

Một số POS có thể chạy offline cho một phần function, nhưng khả năng offline phụ thuộc policy và architecture. Payment authorization thường cần đường liên lạc tới processor/acquirer/network/issuer, trừ các fallback rất cụ thể.

Đây là chỗ [electricity-grid](../electricity-grid/README.md), [internet](../internet/README.md) và [mobile-networks](../mobile-networks/README.md) chạm trực tiếp vào retail.

## 4. Nếu bạn chạm thẻ hoặc điện thoại

Giả sử dùng card/mobile wallet:

```text
Card / phone
    ↓ NFC / chip
POS
    ↓
VAN / gateway / processor
    ↓
Acquirer
    ↓
Card network / domestic switch
    ↓
Issuer
```

Issuer kiểm tra trạng thái card/token, cryptographic data, hạn mức/số dư phù hợp, risk rules và các policy khác rồi trả `APPROVE` hoặc `DECLINE`.

Tại Hàn Quốc, VAN/PG là những lớp rất quen thuộc trong payment topology. Tại Việt Nam, card rail cùng tồn tại với NAPAS và các account-to-account/QR flows mạnh. Xem [credit-card-network](../credit-card-network/README.md).

## 5. Nếu bạn quét QR tại Việt Nam thì flow có thể khác hoàn toàn

UI tại quầy vẫn là “mở điện thoại → scan → trả tiền”, nhưng rail phía sau có thể là chuyển khoản account-to-account:

```text
Customer mobile banking app
      ↓
QR payload / merchant account data
      ↓
Customer bank
      ↓
interbank switching/payment infrastructure
      ↓
Merchant bank
      ↓
Merchant account
```

Vì vậy:

```text
same checkout UX
≠ same payment rail
```

Đây là một trong những khác biệt thực tế dễ thấy khi so sánh Hàn Quốc và Việt Nam.

## 6. `APPROVED` chưa phải kết thúc tài chính

POS nhận approval và in receipt. Nhưng phía financial infrastructure vẫn còn:

```text
Authorization
    ↓
Clearing
    ↓
Fee calculation / reconciliation
    ↓
Settlement
    ↓
Merchant receives net funds
```

Khách hàng cảm nhận giao dịch hoàn thành ở `APPROVED`. Merchant accounting quan tâm cả settlement và reconciliation sau đó.

Xem [banking-system](../banking-system/README.md) để hiểu vì sao payment message và final interbank settlement là hai lớp khác nhau.

## 7. Cùng lúc đó, inventory state thay đổi

Khi sale được confirmed, retail application có thể ghi:

```text
before sale: on_hand = 24
sale qty:    1
expected:    on_hand = 23
```

Trong hệ thống thực tế, update có thể đi qua local store server, message queue, central retail backend hoặc cloud service. Có thể có độ trễ giữa POS transaction và central inventory visibility.

Đây là chỗ [cloud-computing](../cloud-computing/README.md) xuất hiện: transaction, promotion, loyalty, inventory, reporting và forecasting thường dựa vào backend infrastructure.

## 8. Một sale không nhất thiết tạo ngay một delivery

Retail replenishment thường dựa trên aggregation:

```text
sales history
+ current inventory
+ expected demand
+ promotion calendar
+ lead time
+ safety stock
+ case-pack constraints
        ↓
replenishment decision
```

Ví dụ cửa hàng bán 1 chai nước không có nghĩa truck sẽ lập tức mang 1 chai đến. Hệ thống có thể chờ đến khi inventory xuống reorder point hoặc dùng forecast để tạo order trước.

## 9. Từ store order tới distribution center

Một flow đơn giản:

```text
Store demand
   ↓
Retail ERP / replenishment system
   ↓
Distribution center order
   ↓
Warehouse Management System
   ↓
Pick / sort / pack
   ↓
Route planning
   ↓
Truck delivery
   ↓
Store receiving
```

Warehouse có thể gom hàng từ nhiều supplier rồi cross-dock hoặc lưu inventory. Convenience-store network mật độ cao ở Hàn Quốc làm route density và delivery frequency trở thành optimization problem lớn. Ở Việt Nam, modern convenience/retail chains cũng cần giải bài toán tương tự nhưng topology store, traffic, warehouse footprint và traditional-trade coexistence khác.

Xem [supermarkets](../supermarkets/README.md) và [shipping-logistics](../shipping-logistics/README.md).

## 10. Ba source of truth khác nhau

Một giao dịch nhỏ có ít nhất ba dạng state quan trọng:

```text
PAYMENT STATE
approved → cleared → settled

INVENTORY STATE
on shelf → sold logically → replenishment pending → received

ACCOUNTING STATE
sale recognized → fees/reconciliation → merchant funds posted
```

Nếu ba state không đồng bộ, retailer phải reconcile.

Ví dụ:

- POS báo sale nhưng inventory event bị mất.
- Payment approved nhưng transaction bị reversed.
- Goods returned sau khi settlement đã xảy ra.
- Physical count cho thấy còn 7 nhưng system ghi 11.

## 11. Failure propagation

### Mất điện tại cửa hàng

```text
Grid outage
   ↓
UPS may keep router/POS alive temporarily
   ↓
if backup exhausted
   ↓
POS + refrigeration + lighting + network fail
```

Đây không chỉ là payment problem. Với food retail, refrigeration failure còn thành inventory-loss problem.

### Internet/payment processor lỗi

Store vẫn có điện và hàng nhưng electronic payment có thể unavailable. Cash hoặc một rail khác có thể tiếp tục nếu policy cho phép.

### Central cloud/backend lỗi

Payment có thể vẫn chạy nếu payment path tách khỏi retail backend, nhưng loyalty, promotion, central inventory hoặc reporting có thể degraded.

### Warehouse/logistics bị gián đoạn

Checkout vẫn chạy bình thường trong vài giờ/ngày, nhưng shelf availability giảm sau đó. Đây là ví dụ failure có **độ trễ truyền dẫn**.

## 12. Korea ↔ Vietnam — cùng sale, khác payment mix và logistics context

### Hàn Quốc

Một mental model thường gặp:

```text
Dense convenience-store network
+ high card/mobile-payment usage
+ mature VAN/PG/card infrastructure
+ dense urban logistics
+ highly digitized retail backends
```

Điểm đáng học là mật độ store cao làm replenishment frequency, route optimization và small-basket payment throughput quan trọng.

### Việt Nam

Một mental model phù hợp hơn:

```text
Modern convenience/supermarket growth
+ card
+ mobile banking
+ VietQR/account transfer
+ e-wallets
+ coexistence with traditional retail
```

Payment mix đa dạng làm cùng một checkout counter có thể route transaction qua nhiều rail rất khác nhau.

Không nên suy ra rằng một mô hình “tốt hơn” mô hình kia. Chúng phản ánh installed base, consumer behavior, merchant cost, banking infrastructure và market evolution khác nhau.

## 13. Một chai nước liên kết bao nhiêu chapter?

```text
Electricity grid
    ↓
Internet / mobile network
    ↓
POS + cloud
    ↓
Card/payment network
    ↓
Banking system
    ↓
Supermarket inventory
    ↓
Warehouse + logistics
```

Nếu chai nước là hàng nhập khẩu, graph còn nối tiếp tới port, container shipping, customs và FX/payment cross-border.

## 14. Mental model cuối

Đừng nhìn checkout như một action duy nhất. Hãy nhìn nó là **điểm đồng bộ tạm thời của nhiều hệ thống**:

```text
customer intent
+ product identity
+ price rules
+ payment authorization
+ inventory mutation
+ accounting event
+ future replenishment demand
```

Transaction hoàn tất đối với khách trước khi toàn bộ downstream work hoàn tất đối với retailer.

## Đọc tiếp

- [Credit card network](../credit-card-network/README.md)
- [Banking system](../banking-system/README.md)
- [Supermarkets](../supermarkets/README.md)
- [Shipping logistics](../shipping-logistics/README.md)
- [Cloud computing](../cloud-computing/README.md)
- [Electricity grid](../electricity-grid/README.md)
