# GPS & Satellite Navigation — điện thoại biết mình đang ở đâu bằng cách nào?

Điện thoại không hỏi một vệ tinh “tôi đang ở đâu?” rồi nhận về latitude/longitude. Vệ tinh chủ yếu phát **thời gian và quỹ đạo** của chính nó. Receiver đo tín hiệu từ nhiều vệ tinh rồi tự giải bài toán vị trí. Vì vậy GPS là hệ thống đo thời gian cực chính xác trước khi là hệ thống bản đồ.

## 1. GPS chỉ là một GNSS

**Hệ thống vệ tinh định vị toàn cầu (Global Navigation Satellite System, GNSS / 위성항법시스템)** là tên chung. GPS là hệ thống của Hoa Kỳ; ngoài ra còn Galileo của EU, GLONASS của Nga, BeiDou của Trung Quốc và các hệ thống khu vực/bổ trợ khác. Smartphone hiện đại thường là multi-GNSS receiver, kết hợp nhiều constellation để tăng satellite availability và geometry.

Google Maps/Naver Map/KakaoMap không phải “GPS”. App bản đồ nhận position estimate từ operating system; position đó có thể kết hợp GNSS, Wi‑Fi, cell towers, inertial sensors và map matching.

## 2. Từ tín hiệu thời gian tới khoảng cách

Vệ tinh gửi thời điểm tín hiệu được phát. Receiver so với thời điểm nhận:

```text
travel time ≈ receive time - transmit time
range ≈ travel time × speed of light
```

Nhưng clock trong điện thoại không chính xác như atomic clock trên satellite. Vì vậy measured range chứa clock bias và được gọi là **giả khoảng cách (pseudorange / 의사거리)**.

Receiver cần giải bốn unknown cơ bản:

```text
x, y, z position
+ receiver clock error
```

Do đó về nguyên tắc cần ít nhất bốn satellite measurements để giải 3D position + clock bias.

## 3. “Trilateration” thực sự là giao của các mặt cầu

Nếu biết chính xác khoảng cách tới một satellite, receiver nằm trên một sphere quanh satellite. Hai sphere giao thành circle; thêm sphere nữa thu hẹp candidates; satellite thứ tư giúp giải clock bias và chọn nghiệm phù hợp.

```text
Satellite A  ○──── range A ────┐
Satellite B  ○──── range B ────┼→ receiver position
Satellite C  ○──── range C ────┤
Satellite D  ○──── range D ────┘ + clock correction
```

Đây là **trilateration**, không phải triangulation theo góc.

## 4. Vì sao GPS sai vài mét hoặc vài chục mét?

Tín hiệu GNSS rất yếu khi đến mặt đất. Sai số đến từ nhiều nguồn:

- Satellite clock/orbit error.
- Ionosphere và troposphere làm signal delay.
- Multipath: signal phản xạ từ tòa nhà trước khi tới receiver.
- Urban canyon che bầu trời, làm satellite geometry xấu.
- Receiver antenna/noise.
- Interference hoặc spoofing.

Trong Seoul giữa các high-rise hoặc các khu trung tâm Hà Nội/TP.HCM, multipath và blocked sky có thể làm vị trí nhảy dù cùng một phone hoạt động tốt ngoài trời.

## 5. A-GNSS giúp “bắt GPS nhanh” như thế nào?

**GNSS có hỗ trợ (Assisted GNSS, A-GNSS / 보조 위성항법)** dùng network để cung cấp dữ liệu hỗ trợ như approximate location, time và satellite orbital data. Phone không cần chờ tải toàn bộ navigation data từ tín hiệu satellite chậm. Cellular/Wi‑Fi cũng giúp tạo rough location trước khi GNSS fix ổn định.

Điều này giải thích vì sao bật airplane mode hoặc đứng trong building có thể làm time-to-first-fix khác dù satellites trên trời không thay đổi.

## 6. SBAS: satellite navigation có một lớp sửa sai

**Hệ thống tăng cường dựa trên vệ tinh (Satellite-Based Augmentation System, SBAS / 위성기반보강시스템)** dùng mạng reference stations biết chính xác tọa độ để quan sát lỗi GNSS, tính correction/integrity information rồi broadcast correction qua geostationary satellite.

```text
GNSS satellites
      ↓
Ground reference stations
      ↓ measure common errors
Processing centers
      ↓ correction + integrity
Geostationary satellite
      ↓
Aircraft / receiver
```

Aviation quan tâm không chỉ accuracy mà còn **integrity**: hệ thống phải cảnh báo nhanh khi navigation information không còn đáng tin.

## 7. Hàn Quốc: KASS là lớp augmentation quốc gia

Hàn Quốc đã xây Korea Augmentation Satellite System (KASS / 한국형 정밀 GPS 위치보정시스템). KARI mô tả KASS dùng SBAS để giảm lỗi GPS xuống dưới khoảng 3 m và cung cấp integrity information; hệ thống được phát triển cho aviation và có thể mở rộng ứng dụng sang vehicle, drone, maritime và location-based services.

Điểm quan trọng: KASS **không thay thế GPS bằng một constellation GPS của Hàn Quốc**. Nó quan sát GPS/GNSS và phát correction. Đây là layer augmentation.

## 8. Việt Nam: user của multi-GNSS và xây năng lực space/positioning theo ứng dụng

Receiver tại Việt Nam cũng dùng các constellation toàn cầu như GPS, Galileo, BeiDou và GLONASS tùy chipset. Việt Nam hiện không vận hành một global navigation constellation riêng tương đương GPS. Do đó thực tế định vị phụ thuộc vào GNSS quốc tế, cellular positioning, local reference networks và các dịch vụ correction chuyên dụng theo ngành.

Nhu cầu precision positioning lại rất lớn: surveying, agriculture, construction, autonomous equipment, maritime và disaster response. Khi cần centimet-level, hệ thống thường dùng RTK/Network RTK hoặc precise-point-positioning services thay vì chỉ standalone smartphone GNSS.

## 9. Hàn Quốc ↔ Việt Nam

| Câu hỏi | Hàn Quốc | Việt Nam |
|---|---|---|
| Global GNSS constellation riêng | Không phải GPS-owner; receiver dùng global GNSS | Không; receiver dùng global GNSS |
| National augmentation | KASS SBAS đã được triển khai cho high-integrity/aviation use | Precision services chủ yếu dựa trên ground/reference networks và GNSS services theo ngành; không nên đồng nhất với một SBAS quốc gia như KASS |
| Dense urban challenge | Seoul high-rise tạo multipath/urban canyon | Hà Nội/TP.HCM high-rise ngày càng tạo bài toán tương tự; rural/open-sky thường geometry tốt hơn |
| Industrial use | Automotive, drones, logistics, aviation, maritime | Surveying, construction, agriculture, logistics, maritime, mapping và emerging autonomous applications |

## 10. Tại sao phone đôi khi biết vị trí khi không nhìn thấy satellite?

Indoor positioning có thể dùng Wi‑Fi access-point database, Bluetooth beacons, cellular cell IDs và inertial dead reckoning. Phone đo bước chân/rotation từ IMU để tiếp tục estimate giữa hai reliable fixes. Hệ thống mapping còn dùng **map matching** để ép trajectory vào road/rail/path hợp lý.

Vì vậy location stack thực tế:

```text
GNSS
+ cellular
+ Wi‑Fi
+ IMU
+ barometer
+ map constraints
→ fused position
```

## 11. GPS spoofing khác jamming thế nào?

**Gây nhiễu (jamming / 전파방해)** làm receiver không nghe được signal. **Giả mạo tín hiệu (spoofing / 기만신호)** phát signal giả đủ thuyết phục để receiver tính vị trí/thời gian sai. Critical infrastructure không nên dựa vào một sensor navigation duy nhất; aviation/maritime systems dùng integrity monitoring và alternate sources.

Mental model cuối:

```text
Satellite does not know your position.
Satellite broadcasts time + orbit.
Your receiver solves its own position.
```

Đọc [satellites](../satellites/README.md) để hiểu vì sao vệ tinh giữ được orbit, nguồn điện và communication link; [mobile-networks](../mobile-networks/README.md) giải thích network assistance phía mặt đất.

## Nguồn chính thức tham chiếu

- Korea Aerospace Research Institute — KASS: https://www.kari.re.kr/eng/contents/200
- GPS.gov — GPS fundamentals: https://www.gps.gov/
- European Union Agency for the Space Programme — Galileo: https://www.euspa.europa.eu/eu-space-programme/galileo
