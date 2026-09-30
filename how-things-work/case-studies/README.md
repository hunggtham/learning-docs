# Integrated Case Studies — khi nhiều hệ thống chạy cùng lúc

Các chapter riêng giải thích từng hệ thống. Thực tế, một hành động đơn giản thường đi xuyên nhiều hệ thống cùng lúc. Phần này dùng các case end-to-end để tập nhìn **dependency**, **state transition**, **settlement**, **failure propagation** và sự khác biệt Hàn Quốc ↔ Việt Nam.

Không cần đọc case theo thứ tự. Mỗi case đều link ngược về chapter sở hữu cơ chế chi tiết.

## Case 1 — Mua đồ ở convenience store bằng thẻ/điện thoại

[`01_CONVENIENCE_STORE_PAYMENT_AND_RESTOCK.md`](./01_CONVENIENCE_STORE_PAYMENT_AND_RESTOCK.md)

Nối điện → POS/network → payment rail → banking settlement → inventory → warehouse → restock. Case này đặc biệt hữu ích để hiểu tại sao `payment approved` và `merchant đã nhận tiền` là hai state khác nhau.

## Case 2 — Đặt một món hàng từ Hàn Quốc về Việt Nam

[`02_KOREA_TO_VIETNAM_ECOMMERCE_ORDER.md`](./02_KOREA_TO_VIETNAM_ECOMMERCE_ORDER.md)

Nối browser/app, cloud, payment, banking/FX, warehouse, customs, shipping/air cargo và last-mile. Đây là case rõ nhất để tách **information flow, money flow và physical flow**.

## Case 3 — Bay từ Seoul tới Hà Nội

[`03_SEOUL_TO_HANOI_FLIGHT.md`](./03_SEOUL_TO_HANOI_FLIGHT.md)

Nối booking/payment → airline network → airport → baggage → ATC → GNSS → aircraft operation → arrival. Case này cho thấy một passenger journey chỉ là giao diện cuối của nhiều hệ thống safety-critical.

## Case 4 — Mất điện và cascade sang hệ thống số

[`04_POWER_OUTAGE_CASCADE.md`](./04_POWER_OUTAGE_CASCADE.md)

Nối grid → cell tower → Internet → cloud/data center → POS/payment → supermarket/airport/water pumps. Mục tiêu là reasoning về **common-mode failure**, buffer và backup boundary.

## Case 5 — Một chip Hàn Quốc đi vào sản phẩm điện tử lắp ráp tại Việt Nam

[`05_SEMICONDUCTOR_KOREA_VIETNAM_CHAIN.md`](./05_SEMICONDUCTOR_KOREA_VIETNAM_CHAIN.md)

Nối semiconductor design/fab/memory → packaging/test → electronics manufacturing → shipping/air cargo → cloud/telecom demand. Supply chain được nhìn như network có feedback chứ không phải một đường thẳng.

## Case 6 — Mua một cổ phiếu tại Hàn Quốc và Việt Nam

[`06_BUY_ONE_STOCK_KOREA_VIETNAM.md`](./06_BUY_ONE_STOCK_KOREA_VIETNAM.md)

Đi từ broker app → risk/order management → exchange matching → clearing → depository → T+2 settlement. Case này đóng gap giữa `Filled` trên UI và final ownership/cash state.

## Case 7 — Ảnh vệ tinh trở thành flood/agriculture map

[`07_EARTH_OBSERVATION_DATA_PIPELINE.md`](./07_EARTH_OBSERVATION_DATA_PIPELINE.md)

Nối tasking → sensor acquisition → downlink → geometric/radiometric processing → GIS/AI → API/map → operational decision. Case này giải thích vì sao **satellite asset ≠ usable information**.

## Case 8 — Một apartment cao tầng nhận utility như thế nào?

[`08_HIGH_RISE_APARTMENT_UTILITIES.md`](./08_HIGH_RISE_APARTMENT_UTILITIES.md)

Nối city grid/water/sewer/fiber → building transformer/tank/pumps/risers → apartment → waste collection. Case này đặc biệt hữu ích để phân biệt failure ở municipal utility với failure trong building common system.

## Case 9 — Đi làm trong Seoul ↔ Hà Nội ↔ TP.HCM

[`09_URBAN_COMMUTE_SEOUL_HANOI_HCMC.md`](./09_URBAN_COMMUTE_SEOUL_HANOI_HCMC.md)

Nối route planning → GPS/mobile/cloud → road congestion → bus/metro operation → transfer → fare clearing → last mile. Case này cho thấy transport network effect và sự khác biệt giữa một network đã dày với một network đang mở rộng.

## Cách đọc case

Trong mỗi case, hãy tách năm câu hỏi:

1. **Flow:** data, tiền, năng lượng, người hay vật chất đang đi đâu?
2. **State:** hệ thống nào đang giữ source of truth?
3. **Control:** actor nào route/schedule/authorize hành động?
4. **Finality:** lúc nào process thực sự hoàn tất?
5. **Failure:** lỗi tại một layer lan sang layer nào tiếp theo?

Nếu không tách các lớp này, một UI đơn giản rất dễ che mất hệ thống thật phía sau.

Quay lại [`../SYSTEM_MAP.md`](../SYSTEM_MAP.md) nếu cần nhìn toàn bộ dependency graph trước khi đọc case.
