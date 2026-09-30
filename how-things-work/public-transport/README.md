# Public Transport — một chuyến đi bằng bus/metro thực ra được vận hành như thế nào?

Đi xe buýt hoặc metro nhìn từ hành khách chỉ là `tap card → lên xe/tàu → xuống`. Nhưng để một chuyến đi diễn ra đúng giờ, hàng loạt subsystem phải phối hợp: network planning, timetable, fleet/rolling stock, depot, driver/crew, signaling, fare collection, real-time passenger information, incident control và subsidy/revenue settlement.

Chapter này tập trung vào **vận tải công cộng đô thị (urban public transport / 도시 대중교통)**. Kỹ thuật railway sâu hơn thuộc domain giao thông/điện; pricing và subsidy policy sâu hơn thuộc economics. Mục tiêu ở đây là nhìn toàn bộ flow end-to-end, rồi so Hàn Quốc với Việt Nam.

## 1. Hành khách thực sự đang sử dụng một network, không phải một phương tiện đơn lẻ

Một thành phố hiệu quả không tối ưu từng tuyến độc lập. Nó thiết kế network gồm:

```text
origin
  ↓ walk / bike / feeder
bus stop / metro station
  ↓
trunk route
  ↓ transfer hub
another bus / metro / rail
  ↓
last mile
  ↓
destination
```

Metro có throughput cao trên corridor đông người nhưng station spacing lớn. Bus linh hoạt hơn và có thể làm **tuyến gom (feeder / 지선)**. Taxi/bike/walk xử lý first/last mile. Vì vậy chất lượng hệ thống phụ thuộc **khả năng chuyển tuyến (transferability / 환승성)** chứ không chỉ tốc độ của một mode.

## 2. Network planning: tuyến đi đâu và tại sao?

Planner bắt đầu bằng nhu cầu đi lại:

```text
population + jobs + schools + commercial areas
                 ↓
origin-destination demand
                 ↓
corridor demand by time of day
                 ↓
route / station design
                 ↓
frequency + vehicle capacity
```

Nếu corridor có demand rất cao và ổn định, rail/metro có thể phù hợp vì chi phí cố định lớn nhưng capacity cao. Nếu demand phân tán hoặc biến động, bus có thể hiệu quả hơn.

Một lỗi phổ biến là đánh giá metro chỉ bằng “bao nhiêu km đường ray”. Thực tế utility phụ thuộc station location, interchange, frequency, reliability và cách feeder network đưa người tới ga.

## 3. Timetable và headway

**Khoảng cách thời gian giữa hai phương tiện (headway / 배차간격)** quyết định thời gian chờ.

Ví dụ tuyến metro chạy 3 phút/chuyến về lý thuyết cho throughput cao hơn tuyến 10 phút/chuyến, nhưng để giữ headway cần đủ trainsets, crew, platform capacity và signaling.

```text
scheduled departure
      ↓
vehicle/train dispatched
      ↓
run time between stops
      ↓
dwell time at stops
      ↓
turnaround at terminal
      ↓
next trip
```

Một delay nhỏ có thể tạo **bus/train bunching**: phương tiện trễ đón nhiều khách hơn → dwell lâu hơn → càng trễ; phương tiện sau ít khách → bắt kịp. Operations control phải giữ spacing, không chỉ bám giờ giấy.

## 4. Metro: signaling quan trọng hơn việc người lái “nhìn đường”

Rail có guideway cố định và braking distance dài. Hệ thống signaling xác định train separation và movement authority.

Mental model:

```text
track circuits / axle counters / train position
                   ↓
signaling / ATP / CBTC logic
                   ↓
movement authority + speed limit
                   ↓
train traction / braking
```

Các hệ thống hiện đại dùng **điều khiển tàu dựa trên liên lạc (Communications-Based Train Control, CBTC / 무선통신기반 열차제어)** hoặc architecture tương đương để cho phép headway ngắn hơn và bảo vệ khoảng cách an toàn. Depot và operations control center (OCC / 종합관제센터) giám sát toàn network.

## 5. Bus: control problem khác rail

Bus dùng đường chung với xe cá nhân nên bị ảnh hưởng bởi congestion, traffic signals, accidents và curb activity.

```text
bus GPS
  ↓
AVL / fleet management
  ↓
control center
  ↓
ETA prediction
  ↓
passenger information app / display
```

**Định vị xe tự động (Automatic Vehicle Location, AVL / 차량위치자동추적)** giúp operator biết vị trí bus, điều chỉnh dispatch và tính ETA. Bus-only lanes và signal priority có thể giảm variance của travel time.

## 6. Fare collection: tap thẻ chỉ là front-end

Fare system phải xác định:

- ai là hành khách;
- họ đã tap-in/tap-out ở đâu;
- mode nào đã dùng;
- transfer có hợp lệ không;
- tổng quãng đường/fare bao nhiêu;
- revenue thuộc operator nào;
- subsidy/discount được ai bù.

```text
Card / phone / QR / bank card
          ↓
Gate or onboard validator
          ↓
fare transaction log
          ↓
fare engine
          ↓
transfer / distance rules
          ↓
clearing between operators
```

Nếu hệ thống có nhiều operator nhưng một fare card dùng xuyên suốt, backend phải chia revenue sau khi hành khách hoàn thành journey. Đây là một dạng clearing tương tự payment network nhưng asset là **quyền đi lại (transport entitlement / 운송 권리)**.

## 7. Hàn Quốc: Seoul là integrated network chứ không chỉ Seoul Metro

Seoul Metropolitan Area kết nối city bus, metropolitan bus, subway, Korail-operated rail sections và nhiều rail operators khác bằng integrated fare rules. T-money và các transit cards tương thích ghi nhận boarding/alighting để tính distance và transfer discount.

Official Seoul guidance yêu cầu hành khách tap khi lên và khi xuống để integrated transfer fare được áp dụng đúng. Transfer discount dựa vào time window và tổng journey, thay vì coi mỗi lần đổi bus/metro là một vé hoàn toàn mới.

Điều đáng học ở Seoul là **institutional integration**:

```text
multiple physical operators
          +
common fare media/rules
          +
real-time information
          +
high-frequency trunk network
          =
one passenger-facing system
```

Seoul Metro không sở hữu toàn bộ rail network mà hành khách gọi chung là “subway”. Nhiều operator khác cùng tham gia; fare/interchange layer làm chúng có vẻ như một network thống nhất.

## 8. Việt Nam: metro đang chuyển từ từng tuyến sang network

Hà Nội hiện có tuyến 2A Cát Linh–Hà Đông và đoạn trên cao Nhổn–Cầu Giấy của tuyến số 3 đang vận hành. Chính quyền Hà Nội đang mở rộng mô hình từ các line riêng lẻ sang mạng đường sắt đô thị có integration với bus và last-mile.

Một thay đổi đáng chú ý là fare technology: hệ thống soát vé mới trên Cát Linh–Hà Đông và Nhổn–Cầu Giấy đã hỗ trợ định danh điện tử, QR, NFC và cashless methods thay vì chỉ phụ thuộc vé/tokens riêng của từng tuyến.

TP.HCM có Metro Line 1 Bến Thành–Suối Tiên đang vận hành và đang chuẩn bị/thi công thêm các tuyến mới. Trong Phase 2 của metro development, bài toán lớn không còn chỉ là “xây tuyến” mà là:

```text
metro
 + bus feeder
 + park-and-ride / bike
 + common fare
 + interchange design
 + dense land use around stations
```

Nếu thiếu integration, mỗi line có thể chạy tốt nhưng network effect vẫn yếu.

## 9. Seoul ↔ Hà Nội/TP.HCM

| Câu hỏi | Seoul | Hà Nội / TP.HCM |
|---|---|---|
| Network maturity | Dense multi-line metro + extensive bus network | Metro network còn đang mở rộng từ số line ít hơn |
| Fare integration | Mature integrated transfer/distance fare across modes/operators | Đang tiến tới interoperability/cashless/common-platform sâu hơn |
| First/last mile | Walk, buses, neighborhood routes, bikes/taxis | Bus, motorbike/taxi/bike và feeder integration là bài toán đặc biệt quan trọng |
| Operational challenge | Capacity, crowding, aging assets, reliability | Expansion speed, interoperability, construction, ridership ramp-up |
| User mental model | “One network” dù nhiều operators | Người dùng vẫn dễ cảm nhận từng tuyến/hệ thống riêng biệt hơn |

Không nên kết luận “Seoul tốt vì nhiều line hơn”. Nguyên nhân sâu hơn là network đã đạt mật độ cho phép nhiều route alternatives và transfer patterns; Việt Nam đang ở giai đoạn xây network effect đó.

## 10. Subsidy và farebox recovery

Public transport hiếm khi chỉ là retail business thu vé để tối đa profit. Thành phố còn quan tâm congestion, emissions, accessibility và land use.

```text
fare revenue
+ government/local subsidy
+ advertising/commercial income
+ sometimes development/other revenue
        ↓
operation + maintenance + labor + energy + capital costs
```

Một fare thấp có thể tăng ridership nhưng cần subsidy. Một fare cao có thể giảm fiscal burden nhưng làm mode share thấp. Đây là policy trade-off, không phải bài toán kỹ thuật thuần túy.

## 11. Khi một hệ thống lỗi thì sao?

### Fare system outage
Train/bus có thể vẫn chạy nhưng gates/validators hoặc account-based ticketing gặp lỗi. Operator cần fallback policy để tránh dừng toàn service.

### Signaling failure
Rail capacity có thể giảm mạnh vì phải chuyển sang degraded/manual operating mode với headway lớn hơn.

### Power failure
Metro traction power, station equipment, elevators và signaling đều chịu ảnh hưởng; backup systems ưu tiên safety, không nhất thiết giữ full service.

### Telecom/cloud outage
ETA app hoặc fare backend có thể lỗi dù phương tiện vật lý vẫn chạy.

### Road congestion
Bus service reliability giảm mà metro trên right-of-way riêng có thể ít bị ảnh hưởng hơn.

## 12. Finality trong public transport là gì?

Một hành trình không “final” tại thời điểm tap-in.

```text
fare entitlement accepted
        ↓
passenger boards
        ↓
journey segments completed
        ↓
tap-out / journey inferred
        ↓
final fare calculated
        ↓
operator clearing / settlement
```

Với account-based ticketing, final charge thậm chí có thể được tính sau khi backend gom các trip trong ngày để áp daily cap hoặc rule khác.

## 13. Kết nối sang các hệ thống khác

- [Road traffic](../road-traffic/README.md): bus chịu tác động trực tiếp của traffic control.
- [Mobile networks](../mobile-networks/README.md): AVL, apps và account-based ticketing cần connectivity.
- [Banking system](../banking-system/README.md) và [card network](../credit-card-network/README.md): cashless fare payment.
- [Electricity grid](../electricity-grid/README.md): metro traction và depot charging.
- [GPS/GNSS](../gps/README.md): bus positioning và navigation.
- [Cloud computing](../cloud-computing/README.md): passenger information/fare/control applications.

Mental model cần giữ:

```text
Public transport
≠ vehicle

Public transport
= network design
+ operations control
+ vehicles/infrastructure
+ fare/clearing
+ passenger information
+ transfers
+ maintenance
```

## Nguồn chính thức tham chiếu

- Seoul Metropolitan Government — Public Transportation / Subway: https://english.seoul.go.kr/service/movement/public-transportation/ ; https://english.seoul.go.kr/policy/transportation/modes-of-transport/subway/
- Hanoi Government — operation and modernization of Hanoi Metro: https://hanoi.gov.vn/
- Ho Chi Minh City Metro / Government Portal updates: https://tphcm.baochinhphu.vn/
