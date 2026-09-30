# Airlines — một chuyến bay được “sản xuất” như thế nào?

Vé máy bay không chỉ là quyền ngồi trên ghế 2 giờ. Hãng hàng không phải biến một fleet máy bay, crew, airport slots, maintenance capacity và network demand thành hàng nghìn chuyến bay đúng thời gian. Điểm đặc biệt là **ghế trống trên chuyến bay đã cất cánh không thể tồn kho để bán ngày mai**. Vì vậy airline economics bị chi phối mạnh bởi scheduling và revenue management.

## 1. Từ kế hoạch mùa bay tới một flight

```text
Network planning
   ↓ choose routes / frequencies
Schedule planning
   ↓ airport slots + timings
Fleet assignment
   ↓ aircraft type
Crew planning
   ↓ pilots + cabin crew
Maintenance planning
   ↓ aircraft availability
Day-of-operation dispatch
   ↓
Boarding → pushback → flight → arrival
```

Các lớp này phải khớp nhau. Một airline có máy bay nhưng không có slot phù hợp tại sân bay congested vẫn không thể tùy ý thêm chuyến. Có slot nhưng thiếu crew qualified cho aircraft type cũng không khai thác được.

## 2. Network carrier và low-cost carrier khác mental model thế nào?

**Hãng mạng truyền thống (network carrier / 대형항공사)** thường tối ưu hub-and-spoke, connecting passengers, premium cabins, cargo và alliance connectivity. **Hãng hàng không chi phí thấp (Low-Cost Carrier, LCC / 저비용항공사)** thường đơn giản hóa fleet, service và turnaround để giảm unit cost, dù thực tế hiện nay hai model đã pha trộn nhiều.

```text
Hub-and-spoke
A ─┐
B ─┼→ HUB → X / Y / Z
C ─┘

Point-to-point emphasis
A ───── X
B ───── Y
C ───── Z
```

Hub tăng connectivity nhưng tạo wave peaks ở airport và làm disruption ở hub lan rộng trong network.

## 3. Tại sao cùng một ghế có 10 mức giá?

Airline bán một resource có expiry. **Quản trị doanh thu (revenue management / 수익관리)** dự báo xác suất customer có willingness-to-pay khác nhau xuất hiện trước departure. Thay vì bán toàn bộ ghế ở một giá, airline mở/đóng các fare buckets với rule khác nhau.

```text
180 seats
↓
Protect some seats for later high-fare demand
↓
Sell lower fares earlier where useful
↓
Continuously update forecast as bookings arrive
```

Giá vé vì vậy không đơn giản bằng `cost + fixed margin`. Một ghế cuối cùng có marginal operating cost nhỏ, nhưng bán quá rẻ sớm có thể crowd out passenger trả giá cao sau đó; giữ quá nhiều ghế lại có thể khiến flight cất cánh empty.

## 4. Load factor cao chưa chắc lợi nhuận cao

**Hệ số sử dụng ghế (load factor / 탑승률)** cho biết tỷ lệ seat capacity được bán/được sử dụng, nhưng không nói yield. Airline có thể fill 95% bằng vé quá rẻ mà vẫn lỗ. Revenue per available seat kilomet và cost per available seat kilomet giúp nhìn cả revenue/capacity và cost/capacity.

Cargo cũng quan trọng. Widebody passenger aircraft có belly cargo; trên một số route, cargo revenue làm economics khác đáng kể.

## 5. Hàn Quốc: hub quốc tế mạnh, LCC lớn và giai đoạn hợp nhất

Incheon là hub quốc tế chính; Gimpo giữ vai trò lớn cho domestic và short-haul; Jeju, Gimhae và nhiều regional airports tạo network nội địa. Korean Air và Asiana đã trải qua quá trình sáp nhập kéo dài. Theo Ministry of Land, Infrastructure and Transport, việc hợp nhất pháp nhân/khai thác vào Korean Air được lên kế hoạch từ **17/12/2026**; tại snapshot 29/09/2026 đây vẫn là mốc tương lai, không nên viết như sự kiện đã hoàn tất.

Bên dưới full-service carriers, Hàn Quốc có LCC ecosystem lớn. Điều này làm market cạnh tranh mạnh ở short-haul Northeast Asia và leisure routes. Việc consolidation của full-service groups và các LCC affiliates làm network/fleet structure tiếp tục thay đổi, nên tên group và route share cần được kiểm tra lại khi dùng số liệu thực tế.

## 6. Việt Nam: domestic trunk routes + outbound/inbound international growth

Việt Nam có domestic market dài theo trục Bắc–Nam, trong đó Hà Nội, TP.HCM và Đà Nẵng là các node lớn; international traffic kết nối mạnh tới Đông Bắc Á và Đông Nam Á. Vietnam Airlines vận hành network-carrier model; Vietjet phát triển LCC model quy mô lớn; các hãng khác tạo thêm capacity ở từng giai đoạn.

Geography làm air travel có giá trị đặc biệt: Hà Nội–TP.HCM đủ xa để aviation cạnh tranh mạnh với surface transport về thời gian. Khi Long Thành đi vào khai thác theo từng giai đoạn, cấu trúc capacity khu vực TP.HCM sẽ tiếp tục thay đổi, vì vậy airport allocation và network planning phải được đọc theo thời điểm.

## 7. Hàn Quốc ↔ Việt Nam

| Câu hỏi | Hàn Quốc | Việt Nam |
|---|---|---|
| International hub | Incheon rất mạnh về transfer và long-haul | Nội Bài và Tân Sơn Nhất là gateways lớn; Long Thành sẽ bổ sung/reconfigure capacity trong tương lai |
| Domestic geography | Peninsula nhỏ hơn; rail tốc độ cao cạnh tranh mạnh Seoul–Busan | Trục Bắc–Nam dài làm aviation có lợi thế thời gian lớn |
| Carrier structure | Full-service consolidation + nhiều LCC | Network carrier + LCC lớn + các hãng nhỏ hơn |
| Short-haul international | Japan/China/SEA dense network | Korea/Japan/China/SEA dense network, tourism and labor/business flows quan trọng |
| Capacity constraint | Slots ở Incheon/Gimpo/Jeju và airport peaks | Tân Sơn Nhất/Noi Bai congestion, airport expansion và Long Thành là yếu tố lớn |

## 8. Một delay lan qua cả ngày như thế nào?

Một aircraft thường bay nhiều sector trong ngày:

```text
ICN → FUK → ICN → BKK → ICN
```

Nếu sector đầu trễ 90 phút, cùng aircraft và crew mang delay sang sector sau. Airline có thể recover bằng schedule buffer, aircraft swap, spare aircraft hoặc crew reserve, nhưng các biện pháp này tốn tiền.

Weather ở destination cũng có thể gây holding, diversion hoặc cancellation; vấn đề ATC ở một quốc gia có thể ảnh hưởng aircraft rotation tại quốc gia khác.

## 9. Turnaround là “factory floor” của airline

Trong thời gian aircraft ở gate, nhiều task chạy song song:

```text
Passengers deplane
Cleaning
Catering
Fueling
Baggage unload/load
Cargo
Crew change
Maintenance inspection
Boarding
```

Nếu critical path kéo dài, departure trễ. LCC thường coi turnaround ngắn là lợi thế vì mỗi phút aircraft nằm đất là asset không tạo flight revenue.

## 10. Tại sao airline hay hedge fuel nhưng vẫn bị oil price ảnh hưởng?

Jet fuel là cost lớn và biến động. Hedging có thể khóa một phần exposure nhưng không xóa toàn bộ: hedge ratio, tenor, basis difference giữa crude và jet fuel, FX và contract timing đều quan trọng. Với Hàn Quốc và Việt Nam, USD exposure cũng đáng chú ý vì aircraft lease, maintenance, fuel và nhiều khoản industry cost được định giá trực tiếp hoặc gián tiếp bằng USD.

Mental model:

```text
Airline product
= seat inventory with expiry
+ network connectivity
+ aircraft utilization
+ crew & maintenance constraints
+ airport slots
+ fuel / FX exposure
```

Chapter [airports](../airports/README.md) đổi góc nhìn từ airline sang infrastructure provider: runway, terminal, baggage và air traffic flow.

## Nguồn chính thức tham chiếu

- Korea Ministry of Land, Infrastructure and Transport — Korean Air/Asiana integration schedule, 25 Jun 2026: https://www.molit.go.kr/USR/NEWS/m_71/dtl.jsp?id=95092156
- Korea Airports Corporation: https://www.airport.co.kr/
- Incheon International Airport Corporation: https://www.airport.kr/
- Civil Aviation Authority of Vietnam: https://caa.gov.vn/
