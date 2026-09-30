# Shipping & Logistics — một container đi từ nhà máy tới khách hàng như thế nào?

Một sản phẩm “Made in Vietnam” bán ở Seoul hoặc linh kiện Hàn Quốc đưa vào nhà máy ở Bắc Ninh không chỉ đi trên một con tàu. Nó đi qua một chuỗi hợp đồng, kho, xe tải, cảng, hải quan, terminal, hãng tàu, chứng từ và thanh toán. Vì vậy **vận tải biển (ocean shipping / 해상운송)** chỉ là một đoạn của **chuỗi logistics (logistics chain / 물류 체계)**.

## 1. Luồng end-to-end của một container

```text
Factory
  ↓ packing / palletizing
Truck or barge
  ↓
Origin warehouse / ICD
  ↓ customs export clearance
Port gate
  ↓
Container terminal yard
  ↓ crane loading
Ocean vessel
  ↓ possibly transshipment hub
Destination port
  ↓ customs import clearance
Truck / rail / barge
  ↓
Distribution center
  ↓
Factory / retailer / final consignee
```

Song song với container vật lý là một **dòng thông tin (information flow / 정보 흐름)**:

```text
Purchase order
→ booking
→ shipping instruction
→ bill of lading
→ customs declaration
→ manifest
→ arrival notice
→ delivery order
→ proof of delivery
```

Nếu vật lý đi đúng nhưng chứng từ sai, container vẫn có thể đứng ở cảng. Logistics vì vậy là bài toán đồng bộ hàng hóa và dữ liệu.

## 2. Ai là ai trong một shipment?

**Chủ hàng (shipper / 화주)** là bên gửi hàng. **Người nhận hàng (consignee / 수하인)** nhận hàng theo chứng từ. **Hãng tàu (ocean carrier / 선사)** vận hành hoặc khai thác capacity trên tàu. **Công ty giao nhận (freight forwarder / 포워더)** tổ chức vận chuyển thay cho shipper, có thể gom nhiều shipment. **Nhà khai thác terminal (terminal operator / 터미널 운영사)** quản lý bãi, cẩu và gate. **Cảng vụ/cơ quan hàng hải** quản lý an toàn, luồng tàu và khuôn khổ cảng theo jurisdiction. **Hải quan (customs / 세관)** kiểm soát biên giới, thuế và compliance.

Một freight forwarder không nhất thiết sở hữu tàu. Giá trị của họ nằm ở network, booking, consolidation, documentation và xử lý exception.

## 3. FCL và LCL khác nhau ở đâu?

**Nguyên container (Full Container Load, FCL / 만재화물)** không nhất thiết có nghĩa container đầy 100%; nghĩa là một shipper/consignment thuê container như một đơn vị vận chuyển. **Hàng lẻ (Less than Container Load, LCL / 소량화물)** gom hàng của nhiều shipper vào cùng container tại consolidation warehouse.

LCL tiết kiệm khi volume nhỏ nhưng thêm handling và dependency vào consolidation schedule. FCL đơn giản hơn về custody nhưng có thể không kinh tế nếu hàng ít.

## 4. Tại sao container có thể đi vòng qua một nước khác?

Hãng tàu không chạy direct service giữa mọi cặp cảng. Họ xây mạng kiểu hub-and-spoke:

```text
Small origin port
     ↓ feeder
Major hub
     ↓ mainline vessel
Another hub
     ↓ feeder
Destination port
```

**Trung chuyển (transshipment / 환적)** cho phép gom cargo lên tàu lớn chạy tuyến chính. Đổi lại, shipment có thêm connection risk: tàu feeder trễ có thể làm container lỡ mainline vessel.

## 5. Hàn Quốc: Busan như một transshipment hub

Busan là cửa ngõ container lớn nhất Hàn Quốc và đồng thời là hub trung chuyển Đông Bắc Á. Số liệu Busan Port Authority cho thấy transshipment chiếm một phần rất lớn tổng container throughput; điều này phản ánh vai trò của Busan không chỉ với cargo Hàn Quốc mà còn với container đổi tàu để đi tiếp.

Hàn Quốc có nền công nghiệp xuất nhập khẩu tập trung vào manufacturing giá trị cao, đặc biệt bán dẫn, ô tô, hóa chất và machinery. Điều đó làm reliability của cảng, liner schedules và customs/data integration cực kỳ quan trọng. Busan New Port được thiết kế cho tàu container lớn, yard automation và kết nối logistics quy mô lớn.

## 6. Việt Nam: hai cụm cửa ngõ Bắc–Nam và mạng feeder

Việt Nam có geography dài nên không có một cảng duy nhất đóng vai trò giống Busan cho toàn quốc. Miền Bắc xoay quanh cụm Hải Phòng – Lạch Huyện phục vụ hành lang công nghiệp Hà Nội, Hải Phòng, Bắc Ninh, Thái Nguyên; miền Nam có cụm Cái Mép – Thị Vải cho tàu mẹ quốc tế và cụm TP.HCM phục vụ mạng nội vùng.

Cấu trúc này phản ánh distribution của manufacturing: electronics và supplier networks lớn ở phía Bắc; manufacturing, consumer market và industrial zones lớn ở phía Nam. Một phần cargo vẫn dùng feeder tới các hub khu vực tùy tuyến, trong khi Cái Mép – Thị Vải có khả năng nhận nhiều direct mainline services đường dài.

## 7. Hàn Quốc ↔ Việt Nam

| Câu hỏi | Hàn Quốc | Việt Nam |
|---|---|---|
| Hub nổi bật | Busan là national gateway và transshipment hub lớn | Nhiều gateway theo vùng; Hải Phòng/Lạch Huyện và Cái Mép–Thị Vải rất quan trọng |
| Cargo profile | Export manufacturing giá trị cao, import energy/raw materials, transshipment lớn | Export manufacturing tăng nhanh; electronics, garments, furniture, machinery; import components/raw materials lớn |
| Hinterland | Dense road/rail/logistics network, khoảng cách nội địa tương đối ngắn | Đất nước kéo dài; road, inland waterway, ICD và regional logistics quyết định cost |
| Transshipment | Busan tự là hub trung chuyển | Một phần cargo đi direct, một phần feeder/transshipment qua regional hubs tùy service |
| Operational challenge | Hub congestion, mega-vessel scheduling, automation, labor/terminal productivity | Port–road connectivity, uneven infrastructure, customs/document coordination, logistics cost và regional bottlenecks |

Bảng trên không nên đọc thành “Hàn Quốc luôn direct, Việt Nam luôn transship”. Route thật phụ thuộc carrier service, origin/destination, season và contract.

## 8. Incoterms không phải hợp đồng vận tải

Incoterms như FOB, CIF, FCA, DAP xác định cách phân bổ delivery obligation, cost và risk giữa buyer/seller tại các điểm quy ước. Chúng **không tự xác định quyền sở hữu hàng**, payment term hay toàn bộ contract. Một shipment FOB vẫn cần booking, bill of lading và customs documents.

Ví dụ khái niệm:

```text
FOB named port
Seller responsibility ──────┐
Factory → export → vessel onboard
                            │ risk transfer point
                            └────────→ ocean freight → import → buyer
```

Phải dùng đúng phiên bản Incoterms và wording trong hợp đồng thay vì học một câu “FOB = người bán trả tới cảng” rồi áp cho mọi tình huống.

## 9. Container delay đến từ đâu?

Một ETA có thể trễ dù tàu không hỏng:

- Factory cargo ready date trễ.
- Truck/ICD congestion.
- Customs hold hoặc document mismatch.
- Port congestion làm vessel bỏ lượt hoặc đổi berth.
- Weather đóng cảng.
- Blank sailing do carrier điều chỉnh capacity.
- Transshipment connection missed.
- Destination demurrage/detention vì container không được lấy/trả đúng hạn.

**Demurrage** thường gắn với container/cargo lưu trong terminal quá free time; **detention** thường gắn với container bị giữ ngoài terminal quá free time. Cách định nghĩa tính phí cụ thể phụ thuộc carrier/terminal contract.

## 10. Vì sao freight rate biến động dữ dội?

Capacity tàu thay đổi chậm hơn demand. Khi demand tăng nhanh hoặc một chokepoint bị gián đoạn, effective capacity giảm và spot rate có thể tăng mạnh. Carrier còn điều chỉnh network bằng blank sailing, slow steaming và reposition empty containers. Vì container phải ở đúng nơi trước khi được đóng hàng, “thiếu container” có thể là vấn đề positioning chứ không phải thế giới thiếu vỏ container tuyệt đối.

Mental model:

```text
Delivered product
= physical transport
+ document flow
+ customs
+ terminal capacity
+ schedule reliability
+ inventory buffer
```

Chapter [supermarkets](../supermarkets/README.md) tiếp tục từ cảng tới retail shelf; [airlines](../airlines/README.md) cho thấy một network vận tải khác nơi capacity biến mất ngay khi flight cất cánh.

## Nguồn chính thức tham chiếu

- Busan Port Authority — port/container statistics: https://www.busanpa.com/
- Korea Customs Service UNI-PASS: https://unipass.customs.go.kr/
- Vietnam Maritime and Waterway Administration: https://vimawa.gov.vn/
- Vietnam Customs portal: https://www.customs.gov.vn/
- International Chamber of Commerce — Incoterms: https://iccwbo.org/business-solutions/incoterms-rules/
