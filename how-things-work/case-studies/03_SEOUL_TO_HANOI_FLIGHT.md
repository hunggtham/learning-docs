# Case Study 03 — Từ lúc mua vé ở Seoul đến khi hạ cánh tại Hà Nội

Một chuyến bay thương mại là một hệ thống safety-critical ghép từ software, payment, airline operations, airport infrastructure, air traffic control, navigation và ground handling. Passenger nhìn thấy boarding pass; phía sau là hàng chục state phải đồng bộ đủ tốt để aircraft rời gate an toàn.

## 1. Booking bắt đầu trên Internet, không phải ở sân bay

```text
Passenger app / website
      ↓
Internet / CDN
      ↓
booking frontend
      ↓
reservation / inventory system
      ↓
fare rules + seat inventory
      ↓
payment
      ↓
ticket issuance
```

Giá vé không chỉ là “giá ghế”. Airline revenue management chia inventory theo booking class/fare rule và điều chỉnh availability dựa trên demand, schedule, connection và commercial strategy.

Đọc [Internet](../internet/README.md), [Cloud computing](../cloud-computing/README.md) và [Airlines](../airlines/README.md).

## 2. Reservation, payment và ticket là ba state khác nhau

Một mental model đơn giản:

```text
RESERVATION
passenger + itinerary exists

PAYMENT
financial authorization/collection exists

TICKET
carrier has issued transport document/e-ticket state
```

Trong normal flow ba state đi gần nhau, nhưng operationally chúng không phải cùng một object. Payment failure, schedule change, cancellation hoặc reissue có thể làm chúng lệch nhau tạm thời.

## 3. Trước ngày bay: airline phải tạo được một flight vận hành được

Một flight number trên timetable chỉ chạy được nếu airline ghép đủ:

```text
aircraft
+ pilots
+ cabin crew
+ airport slots
+ route permissions
+ fuel plan
+ maintenance status
+ ground handling
+ dispatch/flight plan
```

Nếu thiếu một yếu tố, ticket vẫn có thể tồn tại nhưng flight có thể delay, swap aircraft hoặc cancel.

Đây là lý do airline operation là scheduling problem lớn hơn nhiều so với website bán vé.

## 4. Airport slot khác gate

**Slot sân bay (airport slot / 공항 슬롯)** là quyền/thời điểm sử dụng capacity theo rule ở sân bay constrained. **Gate** là vị trí aircraft đỗ để boarding/deboarding. Runway, taxiway, gate và ATC capacity liên quan nhưng không phải một resource duy nhất.

```text
slot available
!= gate guaranteed in mọi tình huống
!= zero ATC delay
```

Weather hoặc disruption có thể làm planned schedule khác actual sequence.

## 5. Check-in tạo passenger/flight state mới

Khi check-in:

```text
reservation
   ↓
identity / travel-document checks as applicable
   ↓
seat assignment
   ↓
boarding pass
   ↓
checked-in passenger state
```

Boarding pass chứa dữ liệu để airport/airline systems identify passenger + flight + boarding entitlement. Nó không phải “vé máy bay” theo nghĩa accounting duy nhất; nó là artifact vận hành gần departure.

## 6. Checked baggage tạo một flow song song

```text
Bag tag
  ↓
conveyor
  ↓
automated/manual sort
  ↓
security screening
  ↓
make-up area
  ↓
cart/container
  ↓
aircraft hold
```

Passenger có thể ở gate trong khi bag ở hoàn toàn khác nơi trong airport. Bag tag và scan events giúp baggage reconciliation system biết bag được route theo flight nào.

Một failure ở baggage system có thể delay bags mà không nhất thiết làm aircraft technical system hỏng.

## 7. Seoul side: airline và airport là hai operator khác nhau

Nếu bay từ Incheon:

```text
Airline
→ reservation, aircraft, crew, flight operation

Incheon airport operator
→ terminal/runway/airport infrastructure and related operations

ATC authority/service
→ air traffic separation and traffic management

Ground handlers
→ ramp/baggage/cargo/service functions by contract
```

Không nên nói “Korean Air vận hành Incheon Airport” hoặc “airport quyết định toàn bộ flight operation”. Các actor phối hợp nhưng có ownership boundary khác nhau.

Đọc [Airports](../airports/README.md).

## 8. Pushback là điểm physical system thật sự bắt đầu di chuyển

Sau boarding và door close:

```text
load sheet / final passenger-bag state
+ fuel
+ dispatch clearance
+ maintenance release
+ ATC clearance
        ↓
pushback
        ↓
taxi
        ↓
runway
        ↓
takeoff
```

Aircraft weight/balance quan trọng vì passengers, baggage, cargo và fuel đều ảnh hưởng center of gravity và performance.

## 9. ATC không “lái” aircraft

Air traffic control cung cấp separation, clearances và traffic management. Pilots điều khiển aircraft và chịu trách nhiệm operation theo procedures/rules tương ứng.

Simplified flow:

```text
Ground control
   ↓
Tower
   ↓
Departure control
   ↓
En-route control
   ↓
Arrival control
   ↓
Tower
   ↓
Ground
```

Boundary thực tế phụ thuộc airspace organization, nhưng mental model quan trọng là flight được handoff giữa control sectors.

## 10. GPS/GNSS nằm ở đâu trong chuyến bay?

Aircraft navigation có thể dùng nhiều nguồn: GNSS, inertial systems và ground/radio navigation aids tùy aircraft, route và procedure.

GNSS receiver không nhận “bản đồ đường bay” từ satellite. Nó nhận timing/orbit signals rồi tính position. Flight management system dùng position cùng route database/sensors để hỗ trợ navigation.

Đọc [GPS/GNSS](../gps/README.md) và [Satellites](../satellites/README.md).

## 11. Mobile network biến mất nhưng aircraft vẫn bay

Passenger phone mất terrestrial mobile service ở cruising altitude không có nghĩa aircraft mất navigation.

```text
phone cellular network
≠ aircraft navigation system
≠ ATC communication
```

Đây là ví dụ tốt về nhiều radio/network systems cùng tồn tại nhưng phục vụ chức năng khác nhau.

## 12. Flight path không phải đường thẳng Seoul–Hanoi

Route thực tế bị ảnh hưởng bởi:

```text
airways / airspace structure
+ weather
+ winds
+ ATC constraints
+ restricted airspace
+ traffic
+ aircraft performance
```

Do đó great-circle line trên map chỉ là reference hình học, không phải flight clearance thực tế.

## 13. Arrival vào Việt Nam

Một simplified sequence:

```text
en-route
   ↓
arrival control
   ↓
approach
   ↓
landing clearance
   ↓
runway
   ↓
taxi
   ↓
gate / stand
```

Sau đó passenger và bag lại tách thành hai flows:

```text
Passenger → immigration → baggage claim → customs/exit
Bag       → unload → sort → conveyor → baggage claim
```

International-arrival procedures phụ thuộc nationality/document/status và regulation hiện hành; chapter này chỉ giữ cơ chế hệ thống tổng quát.

## 14. Một delay 30 phút có thể bắt nguồn từ đâu?

Không chỉ “airline chậm”. Có thể là:

- inbound aircraft tới muộn;
- crew rotation bị lệch;
- maintenance inspection;
- weather;
- ATC flow restriction;
- gate unavailable;
- baggage/loading delay;
- fueling;
- late connecting passengers/cargo;
- airport congestion.

Delay propagation thường có dạng:

```text
Flight A late
   ↓
aircraft rotation late
   ↓
Flight B late
   ↓
crew duty time pressure
   ↓
Flight C may need swap/cancel
```

Đây là network cascade, không phải từng flight độc lập.

## 15. Korea ↔ Vietnam: airport network topology khác nhau

Hàn Quốc có Incheon là international hub rất lớn, Gimpo và mạng sân bay do KAC vận hành ở các vai trò khác nhau. Việt Nam có Nội Bài và Tân Sơn Nhất là hai gateway lớn, cùng mạng sân bay trải dài và Long Thành đang trở thành một thay đổi topology quan trọng trong tương lai.

Khác biệt cần học không phải “sân bay nào tốt hơn” mà là:

```text
hub concentration
runway/gate capacity
international connection network
city-airport access
carrier network strategy
future capacity expansion
```

## 16. Payment và airline operation gặp nhau lần nữa sau chuyến bay

Nếu flight cancel hoặc passenger đổi vé:

```text
operational event
     ↓
reservation/ticket change
     ↓
fare rule calculation
     ↓
refund / additional collection
     ↓
payment rail
```

Một disruption physical ở aircraft/airport có thể tạo downstream financial transaction hàng giờ hoặc nhiều ngày sau.

## 17. Flight data đi đâu?

Airline/airport ecosystem tạo rất nhiều event:

```text
booking
check-in
bag scan
boarding
off-block
takeoff
landing
on-block
baggage delivery
```

Các hệ thống operational, customer-notification, airport display, analytics và regulatory/reporting có thể consume cùng event ở các boundary khác nhau.

Một airport display `DELAYED` là projection của operational state, không phải nguồn gốc của quyết định delay.

## 18. Failure domains

### Booking system outage

Aircraft đang bay vẫn tiếp tục; nhưng booking/check-in/customer service cho flights khác có thể bị ảnh hưởng.

### Airport baggage outage

Passenger processing và aircraft technical system có thể vẫn sống nhưng bag flow degraded.

### ATC disruption

Airline IT vẫn hoạt động nhưng departures/arrivals bị flow restriction.

### Power outage

Airport có layered backup power, nhưng backup có boundary. Một severe/common-mode event vẫn có thể tác động terminal, baggage, lighting, IT hoặc access systems tùy architecture.

### GNSS interference

Không nhất thiết làm aircraft “mù hoàn toàn” vì aviation navigation có redundancy/procedures; tác động phụ thuộc aircraft, airspace và procedure.

## 19. Mental model cuối

Passenger journey là interface đơn giản của một distributed operational system:

```text
reservation state
+ payment state
+ passenger state
+ baggage state
+ aircraft state
+ crew state
+ airport resource state
+ ATC/airspace state
```

Flight cất cánh khi đủ nhiều state thỏa constraint cùng lúc — không phải chỉ vì clock đến giờ ghi trên vé.

## Đọc tiếp

- [Airlines](../airlines/README.md)
- [Airports](../airports/README.md)
- [GPS/GNSS](../gps/README.md)
- [Satellites](../satellites/README.md)
- [Credit card network](../credit-card-network/README.md)
- [Cloud computing](../cloud-computing/README.md)
