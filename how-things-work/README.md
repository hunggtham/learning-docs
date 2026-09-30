# How Things Work — Hệ thống ngoài đời vận hành như thế nào?

> Snapshot kiểm tra nguồn: 2026-09-30. Đây là tài liệu học cơ chế, không phải bảng số liệu thị phần cố định. Những quy tắc, cơ quan và cấu trúc có thể thay đổi theo thời gian phải được kiểm tra lại từ nguồn chính thức trước khi dùng cho quyết định thực tế.

`how-things-work/` giải thích những hệ thống ta sử dụng mỗi ngày nhưng thường chỉ nhìn thấy phần giao diện cuối: bật đèn, mở website, quẹt thẻ, mua cổ phiếu, nhận một kiện hàng, đi metro, lái xe trên cao tốc, bỏ rác, đổ xăng, sống trong apartment cao tầng hay mở một ứng dụng trên đám mây. Mục tiêu không phải ghi nhớ tên công ty mà là nhìn được **chuỗi vận hành (operating chain / 운영 체계)** phía sau: vật chất, điện, tiền hoặc dữ liệu đi qua những lớp nào; ai sở hữu từng lớp; ai điều phối; state được lưu ở đâu; lỗi ở đâu sẽ lan sang đâu; và vì sao cùng một công nghệ lại có hình thái thị trường khác nhau ở Hàn Quốc và Việt Nam.

Phần này dùng Hàn Quốc và Việt Nam như hai trường hợp so sánh xuyên suốt. Hàn Quốc thường cho thấy một hệ thống đã công nghiệp hóa sâu, mật độ hạ tầng cao và mức số hóa lớn; Việt Nam thường cho thấy một hệ thống tăng trưởng nhanh, đang mở rộng hạ tầng và cải tổ thể chế. Đây không phải đánh giá hơn–kém. Cùng một cơ chế kỹ thuật có thể tối ưu theo địa lý, lịch sử đầu tư, cấu trúc doanh nghiệp và chính sách khác nhau.

## Bắt đầu từ bản đồ hệ thống

Nếu chưa biết nên đọc chapter nào trước, bắt đầu bằng:

1. [`SYSTEM_MAP.md`](./SYSTEM_MAP.md) — thấy điện, Internet, road, transit, cloud, banking, logistics, buildings, waste, fuel, semiconductor… phụ thuộc nhau ra sao.
2. [`KOREA_VIETNAM_COMPARISON.md`](./KOREA_VIETNAM_COMPARISON.md) — đặt topology Hàn Quốc và Việt Nam cạnh nhau theo cùng bộ câu hỏi.
3. [`case-studies/`](./case-studies/README.md) — theo một hành động thực tế xuyên qua nhiều hệ thống cùng lúc.
4. Quay lại chapter chuyên biệt khi muốn đào sâu một subsystem.

Mental model chung:

```text
FLOW
thứ gì đang di chuyển?
điện / packet / tiền / người / hàng hóa / waste / fuel

STATE
hệ thống đang nhớ trạng thái gì?

CONTROL
ai quyết định route / schedule / price / permission?

FINALITY
khi nào state thực sự được coi là hoàn tất?

FAILURE
một node lỗi thì ảnh hưởng dừng ở đâu?
```

## Cách đọc mỗi chapter

Mỗi chapter bắt đầu từ một hành động đời thường rồi đi ngược vào hệ thống. Nhịp chung là:

```text
Hành động của người dùng
        ↓
Điểm truy cập đầu tiên
        ↓
Mạng / hạ tầng trung gian
        ↓
Đơn vị điều phối hoặc thị trường
        ↓
Hệ thống lõi
        ↓
Thanh toán / quyết toán / giao hàng / phản hồi
        ↓
Người dùng nhận kết quả
```

Sau phần cơ chế chung, chapter mới đặt Hàn Quốc và Việt Nam lên cùng sơ đồ để thấy **cùng một chức năng nhưng khác cách tổ chức**. Khi một chủ đề đã có đơn vị sở hữu chuẩn gốc ở nơi khác trong repository, chapter này chỉ giải thích cơ chế end-to-end và cross-link sang phần chuyên sâu thay vì lặp lý thuyết.

## Lộ trình 22 hệ thống

### A. Digital & compute infrastructure

1. [Internet](./internet/README.md) — một request từ điện thoại đi tới server và quay lại bằng cách nào.
2. [Mạng di động](./mobile-networks/README.md) — từ SIM và sóng radio tới core network và Internet.
3. [GPS và định vị vệ tinh](./gps/README.md) — điện thoại tính vị trí từ tín hiệu thời gian như thế nào.
4. [Vệ tinh](./satellites/README.md) — spacecraft, ground segment, dữ liệu và dịch vụ tạo thành một hệ thống thế nào.
5. [Bán dẫn](./semiconductors/README.md) — chip đi từ thiết kế tới wafer, đóng gói, kiểm thử rồi vào thiết bị ra sao.
6. [Điện toán đám mây](./cloud-computing/README.md) — một ứng dụng Internet thực sự chạy trên compute, network, storage và database như thế nào.

### B. Utility & built environment

7. [Lưới điện](./electricity-grid/README.md) — điện được phát, điều độ, truyền tải và bán đến hộ gia đình như thế nào.
8. [Cấp nước](./water-supply/README.md) — nước thô trở thành nước máy rồi đến căn hộ bằng cách nào.
9. [Thoát nước và nước thải](./sewage/README.md) — nước sau khi dùng đi đâu và được xử lý ra sao.
10. [Rác và tái chế](./waste-recycling/README.md) — rác được thu gom, phân loại, tái chế, đốt hoặc chôn lấp như thế nào.
11. [Xây dựng và tòa nhà](./construction-buildings/README.md) — một building đi từ đất/design tới construction, commissioning và vận hành MEP ra sao.
12. [Hệ thống xăng dầu](./fuel-oil-supply/README.md) — crude, refinery, terminal, reserve và cây xăng nối với nhau thế nào.

### C. Money & markets

13. [Hệ thống ngân hàng](./banking-system/README.md) — tiền gửi, tín dụng, thanh khoản và quyết toán ngân hàng liên kết thế nào.
14. [Mạng thẻ](./credit-card-network/README.md) — từ cú quẹt thẻ tới authorization, clearing và settlement.
15. [Thị trường chứng khoán](./stock-market/README.md) — từ lệnh mua tới khớp lệnh, bù trừ, lưu ký và sở hữu chứng khoán.

### D. Goods & commerce

16. [Vận tải biển và logistics](./shipping-logistics/README.md) — một container đi qua nhà máy, cảng, tàu và hải quan như thế nào.
17. [Postal & parcel](./postal-parcel/README.md) — một kiện hàng nhỏ được gắn tracking ID, chia chọn, linehaul và giao last-mile ra sao.
18. [Siêu thị](./supermarkets/README.md) — hàng hóa được mua, dự báo, phân phối, trưng bày và bổ sung tồn kho ra sao.

### E. Mobility

19. [Giao thông công cộng](./public-transport/README.md) — bus/metro network, timetable, signaling, fare và transfer vận hành thế nào.
20. [Giao thông đường bộ](./road-traffic/README.md) — road hierarchy, signals, ITS, congestion và ETC phối hợp ra sao.
21. [Hãng hàng không](./airlines/README.md) — lịch bay, giá vé, slot, khai thác và mạng đường bay được tạo như thế nào.
22. [Sân bay](./airports/README.md) — passenger flow, baggage, runway, ATC và airport operator phối hợp ra sao.

## Integrated case studies

Phần [`case-studies/`](./case-studies/README.md) dùng các tình huống không thể hiểu bằng một chapter duy nhất:

1. [Convenience store: payment → inventory → restock](./case-studies/01_CONVENIENCE_STORE_PAYMENT_AND_RESTOCK.md).
2. [Cross-border e-commerce: Korea → Vietnam](./case-studies/02_KOREA_TO_VIETNAM_ECOMMERCE_ORDER.md).
3. [Chuyến bay Seoul → Hà Nội](./case-studies/03_SEOUL_TO_HANOI_FLIGHT.md).
4. [Power outage cascade](./case-studies/04_POWER_OUTAGE_CASCADE.md).
5. [Semiconductor Korea → Vietnam electronics chain](./case-studies/05_SEMICONDUCTOR_KOREA_VIETNAM_CHAIN.md).
6. [Mua một cổ phiếu Korea ↔ Vietnam](./case-studies/06_BUY_ONE_STOCK_KOREA_VIETNAM.md).
7. [Earth-observation satellite data pipeline](./case-studies/07_EARTH_OBSERVATION_DATA_PIPELINE.md).
8. [High-rise apartment utilities](./case-studies/08_HIGH_RISE_APARTMENT_UTILITIES.md).
9. [Urban commute Seoul ↔ Hà Nội ↔ TP.HCM](./case-studies/09_URBAN_COMMUTE_SEOUL_HANOI_HCMC.md).

Các case ưu tiên tách **dòng thông tin (information flow / 정보 흐름)**, **dòng tiền (money flow / 자금 흐름)**, **dòng vật chất/người (physical flow / 물리적 흐름)** và **dòng năng lượng (energy flow / 에너지 흐름)**. Đây là cách đọc hữu ích nhất khi một UI đơn giản che đi nhiều hệ thống phía sau.

## Lộ trình đọc theo mục tiêu

### Muốn hiểu hạ tầng đô thị và đời sống apartment

```text
Electricity grid
→ Water supply
→ Sewage
→ Waste & recycling
→ Construction & buildings
→ High-rise apartment case
→ Power outage case
```

### Muốn hiểu mobility thành phố

```text
Road traffic
→ Public transport
→ GPS
→ Mobile networks
→ Urban commute case
```

### Muốn hiểu tiền và giao dịch

```text
Banking system
→ Credit card network
→ Stock market
→ Convenience-store case
→ Buy-one-stock case
```

### Muốn hiểu logistics và commerce

```text
Shipping logistics
→ Postal/parcel
→ Supermarkets
→ Korea–Vietnam e-commerce case
```

### Muốn hiểu hàng không

```text
Fuel/oil supply
→ Airlines
→ Airports
→ GPS/GNSS
→ Seoul–Hanoi flight case
```

### Muốn hiểu technology infrastructure

```text
GPS
→ Satellites
→ Mobile networks
→ Internet
→ Semiconductors
→ Cloud computing
→ Earth-observation case
→ Semiconductor Korea–Vietnam case
```

## Ranh giới với các domain khác

`how-things-work/` sở hữu **cơ chế end-to-end ngoài đời**. Lý thuyết kinh tế và cấu trúc thị trường thuộc [`../economics/`](../economics/README.md); đầu tư và phân tích KRX/HOSE/HNX thuộc [`../investing/`](../investing/README.md); mạng máy tính, hệ điều hành và hệ phân tán thuộc [`../computer_science/`](../computer_science/README.md); điện và điện tử nền tảng thuộc [`../electrical_engineering/`](../electrical_engineering/README.md). Chapter ở đây nối những domain đó thành một hệ thống người dùng thật sự chạm vào.

Ví dụ, `stock-market/` ở đây giải thích lệnh → matching → clearing → settlement → custody; chiến lược định giá hay lựa chọn cổ phiếu vẫn thuộc `investing/`. `cloud-computing/` ở đây đi từ request đến physical data center; Kubernetes/IaC/SRE chuyên sâu vẫn thuộc `devops_platform_engineering/`. `construction-buildings/` giải thích lifecycle và building systems, không thay housing finance/law.

## Quy tắc so sánh Hàn Quốc ↔ Việt Nam

Không so sánh chỉ bằng quy mô doanh nghiệp hay GDP. Mỗi chapter ưu tiên các câu hỏi: ai sở hữu hạ tầng, ai điều phối, ai đặt rule, thị trường cạnh tranh ở lớp nào, source of truth nằm đâu, điểm nghẽn kỹ thuật nằm ở đâu, failure có thể lan sang đâu và người dùng cuối nhìn thấy khác biệt gì.

Những số liệu dễ đổi chỉ được dùng khi giúp hiểu cơ chế và phải ghi thời điểm. Với actor/regulation/market structure thay đổi theo thời gian, ưu tiên nguồn chính thức và giữ snapshot date.
