# Satellites — một hệ thống ngoài không gian thực sự gồm những gì?

Vệ tinh không phải “camera bay trên trời” hay “antenna Internet” độc lập. Một mission hoàn chỉnh luôn có ít nhất ba segment: **space segment**, **ground segment** và **user/application segment**. Nếu spacecraft hoàn hảo nhưng không có ground station để command/download data, mission vẫn thất bại về chức năng.

## 1. Kiến trúc một mission

```text
MISSION
├── Space segment
│   ├── satellite bus
│   └── payload
├── Ground segment
│   ├── mission control
│   ├── ground stations
│   └── data processing
└── User segment
    └── terminals / analysts / applications
```

**Nền tảng vệ tinh (satellite bus / 위성 본체)** cung cấp power, thermal control, attitude control, onboard computer, propulsion và communication. **Tải trọng nhiệm vụ (payload / 탑재체)** là thiết bị tạo giá trị: camera quang học, SAR radar, communication transponder, navigation payload hoặc science instrument.

## 2. LEO, MEO và GEO là ba trade-off khác nhau

**Quỹ đạo thấp (Low Earth Orbit, LEO / 저궤도)** có latency thấp và resolution tốt cho Earth observation nhưng satellite chạy nhanh qua bầu trời; muốn continuous service cần constellation hoặc nhiều ground stations.

**Quỹ đạo trung bình (Medium Earth Orbit, MEO / 중궤도)** thường phù hợp navigation constellations vì coverage rộng hơn LEO nhưng vẫn có signal geometry tốt.

**Quỹ đạo địa tĩnh (Geostationary Orbit, GEO / 정지궤도)** ở độ cao lớn và quay cùng tốc độ Trái Đất, nên nhìn từ mặt đất gần như đứng yên trên một longitude. GEO phù hợp broadcasting, weather và communication coverage rộng, đổi lại latency cao hơn và launch/spacecraft requirements khác.

```text
Earth
│ LEO: close, fast pass, low latency
│
│      MEO: navigation-scale orbits
│
└──────────── GEO: appears fixed over equator
```

## 3. Tại sao satellite không rơi xuống?

Satellite thực ra luôn rơi. Nó có horizontal velocity đủ lớn để khi rơi về phía Earth, bề mặt Earth cong ra khỏi đường đi với tốc độ tương ứng. Orbit là free fall liên tục.

Atmospheric drag vẫn tồn tại ở LEO, nên orbit có thể decay. Propulsion hoặc drag-management duy trì mission; khi fuel hết, satellite có thể mất khả năng station keeping dù electronics vẫn hoạt động.

## 4. Power và thermal mới là constraints nền tảng

Solar arrays tạo điện khi có sunlight; battery nuôi spacecraft trong eclipse. Power budget quyết định payload có thể hoạt động bao lâu và transmitter phát mạnh tới mức nào.

Trong vacuum không có convection như không khí. Satellite chủ yếu nhận/radiate heat qua radiation và dẫn nhiệt bên trong structure. Một mặt hướng Sun có thể nóng, mặt khác rất lạnh; thermal design giữ electronics/battery trong operating range.

## 5. Satellite “gửi ảnh xuống” như thế nào?

Earth-observation payload tạo raw data. Onboard computer lưu/encode; khi satellite bay qua vùng ground station nhìn thấy, radio downlink truyền data xuống. Với optical Earth observation, cloud có thể che ảnh; Synthetic Aperture Radar (SAR / 합성개구레이더) chủ động phát microwave và nhận phản xạ, nên có khả năng quan sát ngày/đêm và xuyên mây theo đặc tính hệ thống.

```text
Target on Earth
   ↓ sensed by payload
Onboard storage
   ↓ when ground station visible
Downlink
   ↓
Ground station
   ↓
Processing pipeline
   ↓
Georeferenced product
   ↓
Disaster / agriculture / mapping user
```

## 6. Link budget: vì sao antenna size và frequency quan trọng?

Radio signal yếu đi rất mạnh theo distance. **Ngân sách đường truyền (link budget / 링크 버짓)** cộng gain/loss từ transmitter tới receiver: transmit power, antenna gain, free-space path loss, atmosphere, pointing loss và receiver sensitivity. Dish lớn hoặc phased array tăng gain nhưng thêm cost/complexity.

Higher frequency cho bandwidth lớn hơn nhưng có thể nhạy hơn với rain fade. Vì vậy satellite communication là bài toán physics + regulation + economics.

## 7. Hàn Quốc: từ application tới launch capability

Hàn Quốc có hệ sinh thái space phát triển qua KARI, Korea AeroSpace Administration (KASA / 우주항공청), các viện/trường và doanh nghiệp. Các series như KOMPSAT/Arirang và CAS500 phục vụ Earth observation; hệ thống KASS bổ trợ satellite navigation; chương trình Nuri/KSLV-II tạo sovereign launch capability cho payload phù hợp.

Điểm quan trọng về “thị trường” là Hàn Quốc không chỉ mua ảnh vệ tinh. Value chain đã mở rộng sang satellite manufacturing, payload, ground systems, launch, downstream data và commercial space suppliers. Mức trưởng thành này tạo connection trực tiếp với semiconductor, telecom, defense và cloud/data processing.

## 8. Việt Nam: trọng tâm Earth observation và xây năng lực từng lớp

Vietnam National Space Center (VNSC) đang vận hành/khai thác năng lực Earth observation và phát triển human/infrastructure capability. VNSC cho biết đang vận hành VNREDSat-1, phát triển dòng small satellite và chuẩn bị LOTUSat-1 — radar Earth-observation satellite dùng SAR.

Một chi tiết time-sensitive: update giữa năm 2026 của VNSC nêu LOTUSat-1 **dự kiến phóng trong năm tài khóa 2027 của Nhật Bản**. Vì vậy không nên ghi “LOTUSat-1 đã hoạt động năm 2026” chỉ dựa trên các kế hoạch cũ.

Trung tâm Vũ trụ Việt Nam tại Hòa Lạc gồm satellite assembly/integration/test capability, mission operation và data exploitation infrastructure. Đây là bước chuyển từ chỉ mua satellite data sang xây một phần value chain trong nước.

## 9. Hàn Quốc ↔ Việt Nam

| Lớp value chain | Hàn Quốc | Việt Nam |
|---|---|---|
| Satellite design/manufacturing | Mature national programs + growing private sector | Small-satellite capability đang xây; dự án lớn vẫn dựa đáng kể vào international cooperation |
| Launch | Nuri tạo domestic orbital-launch capability | Chưa có sovereign orbital launch system; launch dựa vào partner/provider quốc tế |
| Earth observation | Multiple missions và downstream ecosystem | VNREDSat-1 + small satellites; LOTUSat-1 SAR là bước capability quan trọng khi được phóng |
| Navigation augmentation | KASS operational | Sử dụng global GNSS và local precision services; chưa tương đương KASS national SBAS |
| Ground/data | Dense research/industrial infrastructure | VNSC Hòa Lạc tăng năng lực ground control, AIT và data use |
| Market stage | Broader upstream + downstream commercial ecosystem | Application/downstream + capability-building, hướng tới mở rộng upstream |

## 10. Satellite lifetime kết thúc vì điều gì?

- Fuel for station keeping cạn.
- Battery/solar degradation.
- Radiation damage electronics.
- Reaction wheel/attitude-control failure.
- Payload degradation.
- Collision/debris damage.
- Ground segment or economics khiến mission không còn hữu ích.

Space debris làm LEO traffic management ngày càng quan trọng. Một satellite chết nhưng còn trên orbit vẫn là physical object có thể va chạm.

## 11. Constellation thay đổi economics ra sao?

Một satellite lớn tối đa hóa capability trên một platform; constellation nhiều satellite nhỏ phân tán capacity và tăng revisit rate nhưng đòi manufacturing repetition, launch cadence, inter-satellite/network coordination và fleet operations.

```text
One satellite
→ high unit capability, sparse revisit

Constellation
→ repeated manufacturing + many passes + network operations
```

Đây là lý do space industry ngày càng giống cloud/telecom: value không chỉ nằm ở hardware mà ở network và recurring service.

Mental model:

```text
Useful satellite service
= spacecraft
+ orbit
+ ground station
+ spectrum
+ data pipeline
+ application
```

Đọc [gps](../gps/README.md) cho navigation use-case và [cloud-computing](../cloud-computing/README.md) cho data processing sau khi downlink.

## Nguồn chính thức tham chiếu

- Korea Aerospace Research Institute: https://www.kari.re.kr/eng/
- Korea AeroSpace Administration: https://www.kasa.go.kr/
- Vietnam National Space Center — activities and LOTUSat-1: https://vnsc.org.vn/vi/hoat-dong/
- VNSC 2026 mid-year update on LOTUSat-1 schedule: https://vnsc.org.vn/vi/tin-tuc-su-kien/trung-tam-vu-tru-viet-nam-to-chuc-hoi-nghi-so-ket-cong-tac-6-thang-dau-nam-va-trien-khai-nhiem-vu-6-thang-cuoi-nam-2026/
