# Case 07 — Ảnh vệ tinh trở thành bản đồ lũ, nông nghiệp hoặc cảnh báo như thế nào?

Case này nối [satellites](../satellites/README.md), [GPS/GNSS](../gps/README.md), [cloud-computing](../cloud-computing/README.md), [Internet](../internet/README.md) và [mobile-networks](../mobile-networks/README.md).

Mental model quan trọng: **có vệ tinh không đồng nghĩa có ứng dụng**. Economic/social value xuất hiện sau một chuỗi data pipeline dài từ mission planning tới processed product và decision.

## 1. User không trực tiếp “bấm camera vệ tinh”

Một request quan sát có thể bắt đầu từ agency/researcher/application:

```text
question
“khu vực nào đang ngập?”
        ↓
area + time + sensor requirement
        ↓
observation request
        ↓
mission planning
        ↓
satellite tasking
```

Scheduler phải xét orbit, swath, cloud, sensor mode, energy, onboard storage và ground-station contact windows.

## 2. Sensor acquisition

Optical sensor đo reflected/emitted light. SAR phát microwave rồi đo phản xạ.

```text
Earth surface
   ↓ reflected/emitted signal
sensor
   ↓
raw digital measurements
   ↓
onboard storage
```

SAR hữu ích khi cần day/night và khả năng quan sát qua mây tốt hơn optical ở nhiều conditions; optical thường trực quan hơn cho human interpretation.

## 3. Downlink

Satellite chỉ có limited contact windows với ground stations.

```text
satellite pass
   ↓
antenna acquisition
   ↓
RF downlink
   ↓
ground station modem/baseband
   ↓
raw data storage
```

Bottleneck có thể là downlink capacity, không phải camera resolution.

## 4. Raw data chưa phải map-ready image

Processing steps có thể gồm:

```text
raw telemetry/image packets
      ↓
radiometric correction
      ↓
geometric correction
      ↓
orthorectification / georeferencing
      ↓
cloud mask / calibration
      ↓
standard image product
```

Để đặt pixel đúng chỗ trên map cần orbit/attitude information, Earth model và ground control/reference data.

## 5. Analysis layer tạo “information”

Ví dụ flood mapping:

```text
pre-event imagery
      +
post-event SAR/optical imagery
      ↓
classification/change detection
      ↓
flood extent polygon
      ↓
combine with roads/houses/population GIS
      ↓
impact estimate
```

Satellite chỉ đo signal. “Bao nhiêu nhà bị ảnh hưởng” cần GIS/database layers khác.

## 6. Cloud/AI layer

Large imagery datasets cần storage + parallel processing.

```text
object storage
   ↓
tile/catalog/index
   ↓
processing cluster
   ↓
ML / image analysis
   ↓
API / map tiles
   ↓
web/mobile application
```

AI có thể phát hiện building, water, forest loss hoặc crop patterns nhưng model accuracy phụ thuộc training data và sensor/domain shift.

## 7. Korea pipeline

KARI quản lý/khai thác national satellite data từ KOMPSAT/Chollian và các national assets; ground systems thực hiện planning, reception, processing và distribution.

KARI mô tả pipeline gồm antenna system, satellite operation, image processing và user request management. KOMPSAT/Chollian data được dùng cho land management, disaster monitoring, agriculture/forestry, water/marine/environment và nhiều lĩnh vực khác.

Một Earth-observation flow Hàn Quốc có thể nhìn:

```text
agency/user request
   ↓
KARI planning
   ↓
KOMPSAT / other satellite observation
   ↓
Daejeon/Jeju/other ground infrastructure
   ↓
processing
   ↓
national satellite data platform
   ↓
agency/research/private application
```

## 8. Việt Nam pipeline

VNSC có Trung tâm Khai thác và Ứng dụng Dữ liệu Vệ tinh, với chức năng xây dựng applications, image/GIS databases và khai thác LOTUSat/other satellite data.

Việt Nam hiện sử dụng cả dữ liệu từ international partners như ALOS-2/ALOS-4 của JAXA cho flood, agriculture, forest/climate applications, trong khi LOTUSat-1 là một phần chiến lược tăng domestic capability.

```text
international / future domestic EO data
        ↓
VNSC reception/access
        ↓
processing + GIS database
        ↓
research/application models
        ↓
agriculture / disaster / environment / planning
```

Điểm quan trọng: application ecosystem có thể phát triển trước khi national satellite tự phóng, nhờ data-sharing partnerships.

## 9. Korea ↔ Vietnam

| Layer | Korea | Vietnam |
|---|---|---|
| EO asset base | Multiple national satellite series and mature ground segment | Growing domestic program + international data partnerships |
| Processing | Mature national processing/distribution infrastructure | VNSC builds processing, GIS and application capabilities |
| Typical applications | land, disaster, environment, agriculture, marine/weather | disaster, agriculture, forest, climate, resource/environment management |
| Key growth issue | multi-satellite integration, AI, higher revisit/resolution | domestic capability, operationalization, user adoption, data pipeline scale |

## 10. Revisit time matters as much as resolution

A 30 cm image is useless for an emergency if it arrives after several days.

Operational value depends on:

```text
spatial resolution
+ temporal resolution / revisit
+ latency
+ weather/sensor availability
+ processing time
```

Disaster response often values fast delivery over maximum pixel detail.

## 11. Optical vs SAR in Korea/Vietnam weather

Monsoon/cloud-heavy conditions create a strong case for SAR in flood/disaster monitoring.

```text
optical
+ intuitive/color information
- cloud/night limitations

SAR
+ day/night
+ cloud penetration in many conditions
- harder interpretation/speckle/processing complexity
```

LOTUSat-1's SAR design is relevant precisely because Vietnam has frequent cloud/flood monitoring needs.

## 12. Failure cases

- Satellite healthy, ground station unavailable → data cannot downlink promptly.
- Downlink succeeds, processing pipeline fails → raw data exists but users see nothing.
- Processing succeeds, cloud/API fails → application unavailable.
- Model misclassifies → technically healthy pipeline but bad decision output.
- Bad georeferencing → image looks fine but overlays wrong location.

This is why EO reliability must be judged end-to-end.

## 13. Finality

For an operational user, finality is not “image captured”.

```text
acquired
→ downlinked
→ calibrated/georeferenced
→ analyzed
→ validated
→ delivered
→ decision/action taken
```

The value chain is complete only when data changes a decision or creates a usable product.

## 14. Example: flood response

```text
heavy rain / typhoon
   ↓
request recent SAR acquisition
   ↓
satellite pass
   ↓
downlink
   ↓
change detection
   ↓
flood extent map
   ↓
overlay roads / population / facilities
   ↓
prioritize field response
```

Mobile networks and Internet then distribute maps/alerts to responders and users.

## Nguồn chính thức tham chiếu

- KARI — Satellite application technology research: https://www.kari.re.kr/eng/contents/190
- KARI — Satellite operation technology research: https://www.kari.re.kr/eng/contents/189
- Vietnam National Space Center — Satellite Data Exploration and Utilization: https://vnsc.org.vn/en/about-vnsc/satellite-data-exploration-and-utilization/
- JAXA/VNSC ALOS-2/ALOS-4 cooperation: https://www.satnavi.jaxa.jp/en/news/2026/05/12/12399/index.html
