# Road Traffic — đường, đèn tín hiệu, ETC và traffic control phối hợp như thế nào?

Một con đường không chỉ là asphalt. Hệ thống giao thông đường bộ gồm **hạ tầng vật lý (physical infrastructure / 물리 인프라)**, **quy tắc (rules / 규칙)**, **cảm biến (sensors / 센서)**, **điều khiển tín hiệu (signal control / 신호 제어)**, **thu phí (tolling / 통행료 징수)**, **thông tin giao thông (traffic information / 교통정보)** và **incident response**. Chỉ khi các lớp này hoạt động cùng nhau thì network mới chuyển được người và hàng với throughput chấp nhận được.

## 1. Flow cơ bản

```text
trip demand
   ↓
road network
   ↓
intersection / ramp / toll point
   ↓
traffic control
   ↓
vehicle movement
   ↓
parking / destination / logistics node
```

Traffic system không thể “schedule” từng xe như railway. Nó điều khiển bằng capacity, right-of-way, signals, lane rules, pricing và information.

## 2. Road hierarchy giải quyết conflict giữa access và speed

Đường local tối ưu access vào nhà/cửa hàng. Arterial gom lưu lượng. Expressway tối ưu tốc độ và throughput bằng cách hạn chế giao cắt.

```text
local street
   ↓
collector
   ↓
arterial
   ↓
expressway / motorway
```

Nếu một arterial có quá nhiều driveway/intersections, tốc độ và reliability giảm. Ngược lại expressway rất hiệu quả cho through traffic nhưng không thể thay local network.

## 3. Intersection là nơi capacity dễ sụp

Tại giao lộ, nhiều movement tranh cùng một không gian.

Traffic signal phải phân bổ **green time** theo phase:

```text
north-south through
        ↓
yellow / clearance
        ↓
east-west through
        ↓
protected turn / pedestrian phase
```

Cycle quá dài làm delay lớn; quá ngắn tăng lost time. Adaptive control dùng detector/camera/traffic data để thay timing theo demand.

## 4. Traffic jam là queueing problem

Khi inflow vượt service rate của một bottleneck:

```text
arrival rate > discharge capacity
           ↓
queue grows
           ↓
queue blocks upstream intersections
           ↓
network spillback
```

Một accident nhỏ ở lane quan trọng có thể giảm capacity đủ để tạo queue hàng kilomet. Sau khi accident được dọn, congestion vẫn có thể mất thời gian dài mới tiêu tan vì queue đã tích lũy.

## 5. ITS: road có một control/data layer phía trên asphalt

**Hệ thống giao thông thông minh (Intelligent Transport Systems, ITS / 지능형교통체계)** thường gồm:

```text
loop / radar / camera / probe GPS
              ↓
traffic data platform
              ↓
traffic management center
              ↓
incident detection / prediction
              ↓
variable message signs / navigation feed / signal control
```

Navigation apps không “nhìn” trực tiếp tất cả xe. Chúng dùng probe data, map topology, historical patterns và incident feeds để estimate travel time.

## 6. Electronic toll collection: xe qua trạm nhưng tiền được xử lý ở backend

Một **thu phí điện tử không dừng (Electronic Toll Collection, ETC / 전자요금징수)** có flow:

```text
vehicle approaches toll point
      ↓
tag / plate / OBU detected
      ↓
vehicle + account identified
      ↓
toll rule determines charge
      ↓
transaction recorded
      ↓
account/payment backend debited
      ↓
operator reconciliation
```

Barrierless/free-flow tolling còn đòi hỏi plate recognition và exception handling cho tag lỗi, account thiếu tiền hoặc disputed vehicle identity.

## 7. Hàn Quốc: expressway operations + Hi-Pass

Korea Expressway Corporation (한국도로공사) vận hành phần quan trọng của expressway network và các lớp dịch vụ như ROADPLUS traffic information và Hi-Pass.

**Hi-Pass (하이패스)** dùng onboard unit/tag/payment instrument để xe qua lane mà không phải dừng trả tiền mặt. Layer đáng học không chỉ là RFID/DSRC mà là toàn bộ exception and settlement system:

```text
vehicle / OBU
   ↓
roadside equipment
   ↓
toll transaction
   ↓
central account/payment processing
   ↓
reconciliation + enforcement
```

Hàn Quốc còn có network monitoring dày đặc, rest areas, incident response và traffic information tích hợp, phù hợp với expressway demand cao trên một quốc gia đô thị hóa mạnh.

## 8. Việt Nam: ETC trở thành lớp mặc định trên cao tốc

Việt Nam đã mở rộng thu phí điện tử không dừng trên các tuyến cao tốc và đang tiếp tục đưa các đoạn Bắc–Nam mới vào thu phí trong 2026. Với các dự án đầu tư công, dữ liệu giao dịch được truyền về hệ thống/trung tâm phục vụ xử lý, lưu trữ và kiểm soát tập trung.

Điểm cần hiểu là **đường đã mở cho xe chạy** và **toll system đã sẵn sàng** là hai trạng thái khác nhau. Một số tuyến có thể phải hoàn thiện ITS, toll equipment, communications hoặc interchange works trước khi thu phí.

```text
physical expressway complete
        ≠
ITS/toll/payment operations complete
```

Đây là ví dụ rất rõ của control plane và physical plane tách nhau.

## 9. Korea ↔ Vietnam

| Lớp | Hàn Quốc | Việt Nam |
|---|---|---|
| Expressway maturity | Network lâu năm, traffic/toll operations trưởng thành | Network mở rộng rất nhanh, nhiều đoạn mới đưa vào khai thác |
| ETC | Hi-Pass ecosystem mature | ETC đang là tiêu chuẩn chính trên cao tốc |
| Control data | Dense ITS + traffic info | ITS/control centers đang mở rộng song hành network |
| Urban challenge | congestion ở dense metro areas, high car volume | mixed traffic, motorbike share lớn, rapid urbanization |
| Expansion problem | optimize/maintain mature assets | build capacity + standardize operations simultaneously |

Mixed traffic làm bài toán Việt Nam khác đáng kể: motorbike, car, bus, truck cùng chia road space với khác biệt lớn về acceleration, lane behavior và safety exposure.

## 10. Parking cũng là một traffic-control mechanism

Parking không đứng ngoài road system. Nếu curb parking chiếm lane, effective capacity giảm. Nếu parking quá rẻ ở CBD, demand lái xe vào trung tâm tăng.

```text
parking price / availability
          ↓
mode choice + destination choice
          ↓
traffic demand
```

Smart parking có thể dùng sensors/cameras/payment apps, nhưng công nghệ chỉ giải information/payment; supply và pricing vẫn là policy decision.

## 11. Incident management

Một crash cần nhiều actor:

```text
incident detected
   ↓
police / road operator / rescue dispatched
   ↓
lane control + warning
   ↓
medical / towing / cleanup
   ↓
reopen lane
   ↓
queue recovery
```

Response time ảnh hưởng trực tiếp secondary crashes và total delay.

## 12. Traffic signal failure vs network failure

- Một signal chết: intersection có thể chuyển flashing/manual control.
- Fiber/traffic-control center mất kết nối: local controllers có thể chạy fixed timing nhưng optimization mất.
- GPS/navigation outage: road vẫn tồn tại nhưng route guidance kém.
- Electricity outage: signals/cameras/toll equipment chịu ảnh hưởng; backup power quyết định resilience.
- Mobile network outage: probe data và app updates giảm, nhưng vehicle movement vẫn tiếp tục.

## 13. Road traffic nối với public transport và logistics

Bus reliability phụ thuộc traffic. Truck delivery time ảnh hưởng inventory. Airport access roads ảnh hưởng passenger check-in risk. Toll pricing ảnh hưởng route selection.

```text
road congestion
 ├── bus delay
 ├── parcel delay
 ├── supermarket restock delay
 ├── port drayage delay
 └── airport access delay
```

Đây là lý do road network là dependency chung của nhiều chapter.

## 14. Finality trong road traffic

Một vehicle passage có nhiều state:

```text
vehicle enters road
   ↓
toll event detected
   ↓
charge calculated
   ↓
payment/account posted
   ↓
operator reconciliation
```

Xe đã qua trạm không đồng nghĩa transaction không thể bị điều chỉnh/disputed. Physical movement và financial finality tách nhau.

## Đọc tiếp

- [Public transport](../public-transport/README.md) cho bus/metro operations.
- [GPS](../gps/README.md) cho positioning.
- [Mobile networks](../mobile-networks/README.md) và [Internet](../internet/README.md) cho ITS connectivity.
- [Credit-card network](../credit-card-network/README.md) và [banking](../banking-system/README.md) cho toll payment.
- [Shipping logistics](../shipping-logistics/README.md) cho freight movement.

Mental model:

```text
Road system
= physical network
+ traffic rules
+ signals
+ sensing
+ control center
+ toll/payment
+ incident response
+ maintenance
```

## Nguồn chính thức tham chiếu

- Korea Expressway Corporation: https://www.ex.co.kr/
- Korea Expressway Corporation Hi-Pass information: https://www.hipass.co.kr/
- Vietnam Government Portal / Road Administration ETC updates: https://baochinhphu.vn/
