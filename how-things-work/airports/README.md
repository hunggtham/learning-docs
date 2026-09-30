# Airports — runway, terminal và air traffic được phối hợp như thế nào?

Airport không phải chỉ là tòa terminal. Nó là nơi bốn network gặp nhau: aircraft trên bầu trời, runway/taxiway trên mặt đất, passenger/baggage trong terminal và road/rail đưa người tới sân bay. Chỉ cần một network nghẽn là toàn hệ thống giảm capacity.

## 1. Hành trình passenger và baggage

```text
Passenger
  ↓ airport access
Check-in / bag drop
  ↓
Security / immigration when applicable
  ↓
Departure gate
  ↓
Aircraft
  ↓
Arrival gate
  ↓
Immigration / baggage reclaim / customs
  ↓
Ground transport
```

Baggage đi một route song song:

```text
Bag tag
  ↓
Conveyor
  ↓ screening
Baggage sortation
  ↓
Make-up area
  ↓
Aircraft hold
  ↓
Arrival unload
  ↓
Baggage reclaim
```

Bag tag liên kết passenger itinerary với sorting system. Với connection, bag có thể phải tự động chuyển từ flight này sang flight khác mà passenger không nhận lại.

## 2. Runway capacity không bằng số runway

Hai sân bay cùng có hai runway có thể có capacity rất khác vì geometry, separation, taxiway, weather, ATC procedure và traffic mix. Parallel runways đủ xa có thể cho phép independent operations trong điều kiện nhất định; crossing runways tạo nhiều dependency hơn.

Một flight chiếm nhiều resource theo chuỗi:

```text
Airspace arrival stream
→ runway landing slot
→ taxiway
→ gate
→ turnaround
→ pushback
→ taxiway
→ runway departure slot
→ airspace
```

Nếu gate chưa trống, aircraft có thể chờ dù runway available. Nếu weather làm spacing giữa aircraft tăng, runway throughput giảm dù infrastructure không hỏng.

## 3. Slot là gì?

Ở sân bay congested, **khung giờ cất/hạ cánh (airport slot / 공항 슬롯)** là quyền sử dụng airport infrastructure vào thời điểm cụ thể theo rule điều phối. Slot không phải air traffic control clearance. Airline có slot theo schedule nhưng flight vẫn cần ATC clearance thực tế ngày khai thác.

IATA phân loại sân bay theo mức congestion; cơ quan quốc gia và coordinator áp cơ chế phù hợp. Việt Nam trong năm 2026 tiếp tục công bố Nội Bài và Tân Sơn Nhất là các sân bay điều phối Level 3 trong giai đoạn áp dụng tương ứng, phản ánh constraint cao về capacity.

## 4. Ai vận hành airport và ai điều khiển máy bay?

Đây là ranh giới dễ nhầm:

- **Airport operator** quản lý terminal, airfield assets, commercial facilities và coordination tại sân bay theo mandate.
- **Air navigation service provider / air traffic control** quản lý separation và luồng aircraft trong airspace.
- **Airline/ground handler** quản lý aircraft turnaround, passenger và baggage services thuộc phạm vi hợp đồng.
- **Security, immigration, customs, quarantine** là các cơ quan/chức năng nhà nước riêng.

Một operator airport không tự “điều khiển mọi máy bay trên trời”.

## 5. Hàn Quốc: Incheon tách khỏi mạng 14 sân bay KAC

Incheon International Airport Corporation (IIAC / 인천국제공항공사) vận hành Incheon. Korea Airports Corporation (KAC / 한국공항공사) vận hành 14 sân bay khác, gồm Gimpo, Gimhae, Jeju và các regional airports. Cấu trúc này tạo một boundary tổ chức rõ: international mega-hub Incheon có operator riêng, trong khi phần lớn mạng airport dân dụng còn lại nằm dưới KAC.

Incheon được thiết kế như transfer hub: terminal capacity, automated baggage, rail/road access, cargo complex và hub-carrier banks phối hợp để tạo connection. Gimpo lại có vai trò khác, gần Seoul và tập trung domestic/short-haul hơn.

## 6. Việt Nam: mạng airport quốc gia và các gateway đang mở rộng

Vietnam có mạng sân bay trải dài; Airports Corporation of Vietnam (ACV) quản lý/khai thác phần lớn commercial airports, trong khi aviation authority và air-navigation organizations giữ các chức năng regulatory/ATC khác. Nội Bài phục vụ phía Bắc, Tân Sơn Nhất là gateway lớn phía Nam và Đà Nẵng là node miền Trung quan trọng.

Long Thành là dự án làm thay đổi topology của miền Nam: khi capacity mới được đưa vào vận hành theo phase, một phần traffic quốc tế/nội địa, airline bases, ground access và cargo flows phải được phân bổ lại giữa các sân bay. Điều đó cho thấy airport không thể phân tích tách khỏi road/rail access và airline network.

## 7. Hàn Quốc ↔ Việt Nam

| Câu hỏi | Hàn Quốc | Việt Nam |
|---|---|---|
| Mega international hub | Incheon, operator riêng IIAC | Tân Sơn Nhất/Nội Bài hiện là gateways lớn; Long Thành bổ sung hệ thống phía Nam theo phase |
| National airport operator | KAC quản lý 14 sân bay ngoài Incheon | ACV quản lý phần lớn commercial airport network |
| Surface competition | KTX làm giảm nhu cầu bay trên một số domestic trunk route | Khoảng cách Bắc–Nam lớn làm air transport giữ vai trò mạnh |
| Main capacity issue | Hub peak waves, slots, weather, transfer coordination | Rapid traffic growth, terminal/runway/access capacity và airport expansion |
| Transfer role | Incheon có international transfer ecosystem rất phát triển | International transfer nhỏ hơn; O&D traffic hiện nổi bật hơn, nhưng network có thể phát triển theo capacity mới |

## 8. Tại sao check-in online không loại bỏ airport process?

Online check-in chỉ tạo boarding credential và xác nhận một phần passenger record. Passenger có checked bag vẫn cần bag drop; security/immigration vẫn cần identity/process riêng; gate có thể cần document check. Vì vậy digital UX giảm queue ở một layer chứ không xóa physical constraints.

## 9. Baggage thất lạc thường là vấn đề handoff

Bag càng qua nhiều connection, số handoff càng tăng:

```text
Origin handler
→ sorter
→ aircraft 1
→ transfer handler
→ sorter
→ aircraft 2
→ destination handler
```

Tag lỗi, minimum connection time quá ngắn hoặc flight đổi gate phút cuối có thể làm bag miss connection dù passenger kịp chạy sang gate.

## 10. Vì sao sân bay kiếm tiền ngoài landing fee?

Airport có hai nhóm revenue lớn: **aeronautical** như landing/passenger/parking charges và **non-aeronautical** như retail, duty-free, parking, real estate, advertising. Một hub có passenger dwell time cao tạo retail economics khác airport chủ yếu domestic point-to-point.

## 11. Failure propagation

```text
Thunderstorm
→ arrival rate reduced
→ aircraft hold/divert
→ gates occupied longer
→ departing aircraft cannot push on time
→ crews exceed duty limits
→ cancellations
→ next-day aircraft out of position
```

Đây là lý do airport disruption có memory dài hơn cơn mưa.

Mental model:

```text
Airport capacity
= airspace
∩ runway
∩ taxiway
∩ gate
∩ terminal
∩ baggage
∩ ground access
```

Dấu `∩` nhấn mạnh capacity bị giới hạn bởi bottleneck nhỏ nhất tại thời điểm đó.

Đọc tiếp [airlines](../airlines/README.md) nếu cần hiểu airline scheduling, hoặc [shipping-logistics](../shipping-logistics/README.md) để so sánh một network vận tải nơi cargo không “hết hạn” ngay khi slot departure trôi qua.

## Nguồn chính thức tham chiếu

- Incheon International Airport Corporation: https://www.airport.kr/
- Korea Airports Corporation — airport network: https://www.airport.co.kr/
- Korea MOLIT — civil aviation information: https://www.molit.go.kr/
- Civil Aviation Authority of Vietnam — slot/airport information: https://caa.gov.vn/
- Airports Corporation of Vietnam: https://www.vietnamairport.vn/
