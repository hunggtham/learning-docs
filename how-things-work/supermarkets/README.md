# Supermarkets — vì sao hàng luôn xuất hiện đúng trên kệ?

Một siêu thị nhìn giống tòa nhà đầy hàng hóa, nhưng về bản chất nó là một hệ thống dự báo nhu cầu, mua hàng, tồn kho, logistics, dữ liệu và vốn lưu động. Mỗi sản phẩm trên kệ là kết quả của nhiều quyết định trước đó: SKU nào được bán, đặt bao nhiêu, đi qua distribution center nào, khi nào markdown, và ai chịu rủi ro khi hàng không bán hết.

## 1. Luồng hàng hóa cơ bản

```text
Manufacturer / importer
        ↓ purchase order
Supplier warehouse
        ↓
Retail distribution center
        ↓ cross-dock / storage / picking
Store backroom
        ↓ shelf replenishment
Shelf
        ↓
Customer basket
        ↓
POS checkout
        ↓ sales data
Inventory / forecasting system
        ↓
New purchase & replenishment orders
```

Siêu thị vì vậy là một vòng feedback chứ không phải chuỗi một chiều. Mỗi lần barcode được scan, hệ thống giảm on-hand inventory và tạo thêm dữ liệu cho forecasting/replenishment.

## 2. SKU, barcode và planogram

**Đơn vị lưu kho (Stock Keeping Unit, SKU / 재고관리단위)** là định danh nội bộ cho một biến thể hàng hóa. Hai chai nước cùng brand nhưng khác dung tích thường là hai SKU. Barcode như EAN/UPC giúp POS nhận product identifier; hệ thống retail ánh xạ identifier này sang giá, thuế, promotion và inventory record.

**Sơ đồ trưng bày (planogram / 진열계획)** quyết định mỗi SKU nằm ở đâu và có bao nhiêu facings. Vị trí ngang mắt có giá trị thương mại vì ảnh hưởng probability được chọn. Vì vậy shelf space là tài nguyên hữu hạn cần tối ưu, không chỉ là việc “xếp hàng cho đẹp”.

## 3. Replenishment: tại sao không đặt thật nhiều để khỏi hết hàng?

Tồn kho tạo trade-off:

```text
Too little inventory
→ stockout → lost sales → unhappy customer

Too much inventory
→ capital tied up + storage + spoilage + markdown
```

Retailer theo dõi lead time, demand variability, safety stock và service level. Với mì gói hoặc giấy vệ sinh, shelf life dài nên buffer dễ hơn. Với sashimi, sữa tươi hoặc rau, overstock nhanh chóng trở thành waste.

Các cửa hàng lớn thường nhận hàng từ distribution center thay vì từng supplier tự giao mọi SKU. Distribution center gom volume, cross-dock, chia theo store và tối ưu truck routes.

## 4. POS không chỉ thu tiền

```text
Barcode scan
   ↓
Product master
   ↓ price / promotion / tax
Basket total
   ↓
Payment rail
   ↓
Receipt

Song song:
Sale → inventory decrement → demand data → replenishment forecast
```

Payment rail nối sang [credit-card-network](../credit-card-network/README.md) hoặc bank/QR rails. Nhưng với retailer, giá trị lớn của POS còn là dữ liệu demand gần thời gian thực.

## 5. Hàn Quốc: retail hiện đại, mật độ cao và omnichannel

Hàn Quốc có hệ sinh thái hypermarket, supermarket, convenience store và e-commerce dày đặc. Các chuỗi lớn như E-Mart, Lotte Mart và Homeplus hình thành mạng distribution center quy mô lớn; bên cạnh đó convenience stores và online grocery làm chu kỳ replenishment ngắn hơn. Mật độ đô thị và logistics phát triển giúp same-day/next-day và dawn delivery trở thành kỳ vọng thực tế ở nhiều khu vực.

Điểm đáng học không phải tên chuỗi nào đứng số một mà là **omnichannel inventory**: hàng online có thể được fulfill từ dedicated fulfillment center, micro-fulfillment hoặc store tùy retailer. Forecast phải kết hợp demand offline và online, trong khi cold chain phải duy trì nhiệt độ từ supplier tới door.

## 6. Việt Nam: modern trade và traditional trade cùng tồn tại

Việt Nam có supermarket/hypermarket, minimart/convenience chains và e-commerce tăng nhanh, nhưng chợ truyền thống và cửa hàng nhỏ vẫn là một phần quan trọng của distribution. Vì thế supplier thường phải phục vụ hai logic song song:

```text
Modern trade
Supplier → DC → chain stores → POS data

Traditional trade
Manufacturer/importer → distributor → wholesaler → small store / market stall
```

Modern trade tạo dữ liệu SKU và demand tập trung hơn; traditional trade có network phân phối sâu, linh hoạt và gần khu dân cư nhưng dữ liệu end-to-end phân mảnh hơn. Đây là lý do cùng một FMCG company có thể có sales organization và route-to-market rất khác ở Việt Nam so với Hàn Quốc.

## 7. Hàn Quốc ↔ Việt Nam

| Câu hỏi | Hàn Quốc | Việt Nam |
|---|---|---|
| Retail structure | Modern retail + convenience + e-commerce có độ phủ rất cao | Modern trade tăng nhanh nhưng coexist với chợ/cửa hàng truyền thống |
| Fulfillment | DC automation, dense last-mile, dawn/same-day delivery phát triển sâu | DC và modern logistics mở rộng nhanh; last-mile chịu ảnh hưởng hạ tầng đô thị và fragmented demand |
| Payment | Card/mobile payment rất phổ biến | Cash giảm vai trò nhưng vẫn tồn tại; QR, bank transfer, cards và wallets cùng phát triển |
| Data | POS/loyalty/online data thường tập trung ở chain lớn | Chain có data tốt; traditional channel thường cần distributor data và field sales để nhìn demand |
| Fresh food | Cold-chain và prepared-food ecosystem trưởng thành | Cold-chain đang mở rộng, nhưng độ đồng đều theo khu vực/supplier khác nhau |

## 8. Ai có bargaining power?

Một retailer lớn gom demand của hàng triệu customer nên có bargaining power với supplier: giá mua, promotion funding, shelf placement, payment terms. Ngược lại, một brand cực mạnh cũng có power vì retailer không muốn thiếu sản phẩm khách bắt buộc tìm.

Điểm này nối thẳng sang economics: market power không chỉ nằm ở người sản xuất. Nó có thể nằm ở platform, distributor hoặc retailer kiểm soát access tới consumer.

## 9. Vì sao một món hàng “lỗ” vẫn xuất hiện trên kệ?

Retailer không tối ưu từng SKU độc lập. Một sản phẩm có margin thấp có thể là **traffic builder** kéo khách vào store; khách sau đó mua basket có margin cao hơn. Promotion kiểu loss leader, private label, slotting arrangements và category management đều khiến economics ở cấp basket/category khác cấp SKU.

## 10. Failure modes

- Forecast sai → stockout hoặc excess inventory.
- Supplier delay → shelf empty dù store vẫn hoạt động.
- DC outage → ảnh hưởng hàng loạt store.
- Cold-chain break → hàng trông bình thường nhưng mất an toàn/chất lượng.
- POS/master-data lỗi → sai giá hoặc inventory record.
- Promotion không đồng bộ → demand spike vượt safety stock.

Mental model nên giữ:

```text
Retail shelf
= procurement
+ inventory
+ logistics
+ data
+ merchandising
+ payment
+ working capital
```

Chapter [shipping-logistics](../shipping-logistics/README.md) mở rộng từ distribution center ra chuỗi cung ứng quốc tế; [banking-system](../banking-system/README.md) giải thích working capital và payment rails phía tài chính.

## Nguồn tham chiếu

- Statistics Korea / KOSIS — retail and distribution statistics: https://kosis.kr/
- National Statistics Office of Vietnam — retail statistics: https://www.nso.gov.vn/
- GS1 — barcode / product identification standards: https://www.gs1.org/
