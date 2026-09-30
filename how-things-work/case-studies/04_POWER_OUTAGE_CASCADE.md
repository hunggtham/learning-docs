# Case Study 04 — Một sự cố điện có thể lan sang Internet, payment, retail và water system như thế nào?

Mất điện thường được nhìn như một vấn đề của riêng ngành điện. Thực tế, electricity là **hạ tầng phụ thuộc nền (foundational dependency / 기반 의존성)** của gần như mọi hệ thống còn lại trong library. Case này không mô tả một blackout lịch sử cụ thể; nó xây mental model để phân tích failure propagation.

## 1. Grid failure không đồng nghĩa mọi nơi tắt cùng lúc

Một hệ thống điện có nhiều lớp protection, switching và restoration. Khi fault xảy ra, mục tiêu đầu tiên là cô lập phần lỗi để tránh damage/cascade lớn hơn.

```text
fault
  ↓
protection detects abnormal current/voltage/frequency
  ↓
breaker trips
  ↓
faulted section isolated
  ↓
remaining system attempts to rebalance
```

Nếu imbalance vượt khả năng chịu của system, frequency/voltage có thể lệch, generation/transmission units khác cũng trip và cascade rộng hơn.

Đọc [Electricity grid](../electricity-grid/README.md).

## 2. “Có backup” không có nghĩa độc lập với grid

Nhiều facility dùng nhiều tầng:

```text
Grid
 ↓
UPS / battery
 ↓
Generator
 ↓
critical loads
```

**Bộ lưu điện (Uninterruptible Power Supply, UPS / 무정전 전원 장치)** phản ứng rất nhanh nhưng energy capacity có giới hạn. Generator có thể chạy lâu hơn nhưng cần start, fuel, maintenance và switchgear hoạt động đúng.

Backup design luôn có boundary:

```text
backup power duration
+ fuel supply
+ cooling
+ network upstream
+ human operation
```

Một data center còn điện nhưng upstream telecom facility mất điện vẫn có thể mất connectivity.

## 3. Cell tower phản ứng thế nào?

Base station/site thường có battery backup và một số site quan trọng có generator hoặc resilience cao hơn tùy operator/site type.

```text
Grid lost
   ↓
site battery takes load
   ↓
site remains online temporarily
   ↓
if outage persists
battery drains
   ↓
site goes offline unless generator/refuel available
```

Nhưng mobile network không chỉ là tower. Backhaul, aggregation nodes, transport network và core facilities cũng cần power.

Đọc [Mobile networks](../mobile-networks/README.md).

## 4. Network congestion có thể xuất hiện trước khi site chết

Trong blackout, fixed broadband/Wi-Fi tại nhà có thể ngừng vì modem/router mất điện. Người dùng chuyển sang cellular:

```text
home broadband unavailable
       ↓
phones move traffic to mobile network
       ↓
traffic per surviving cell increases
       ↓
congestion
```

Vì vậy mobile signal bars vẫn hiện nhưng data chậm hoặc call setup khó. Đây là capacity problem, không nhất thiết coverage problem.

## 5. Internet là chain; một link sống chưa đủ

```text
Phone
 ↓
cell site
 ↓
backhaul
 ↓
operator core
 ↓
Internet exchange / transit
 ↓
DNS / CDN / cloud service
```

Nếu một upstream node mất điện, local radio site có thể vẫn phát sóng nhưng service phía sau unreachable.

Đọc [Internet](../internet/README.md).

## 6. Data center và cloud có layered redundancy nhưng vẫn có failure modes

Một data center thiết kế tốt có thể có:

```text
multiple utility feeds
UPS
battery
backup generators
redundant distribution paths
cooling redundancy
network redundancy
```

Nhưng common-mode failures vẫn có thể xảy ra: switchgear/configuration error, fuel logistics, cooling failure, fire/safety shutdown hoặc nhiều feeds phụ thuộc cùng upstream grid node.

Cloud region/multi-zone architecture giảm một số risk nhưng application cũng phải deploy đúng. Chỉ đặt một VM trong một zone rồi nói “đã dùng cloud nên HA” là sai mental model.

Đọc [Cloud computing](../cloud-computing/README.md).

## 7. Payment tại cửa hàng bị ảnh hưởng như thế nào?

```text
store power lost
    ↓
POS off
router off
lighting/refrigeration affected

or

store backup alive
    ↓
network/payment upstream unavailable
    ↓
card/QR authorization may fail
```

Một cửa hàng có thể còn điện nhưng không nhận electronic payment; hoặc payment rail còn sống nhưng cửa hàng hoàn toàn tắt.

Đọc [Credit card network](../credit-card-network/README.md) và [Banking system](../banking-system/README.md).

## 8. Banking system có thể sống trong khi branch/ATM địa phương chết

Core banking và interbank settlement infrastructure thường nằm trong protected data-center environments. Tuy nhiên access channel địa phương phụ thuộc:

```text
ATM power
branch power
telecom network
customer phone battery/network
```

Do đó phải tách:

```text
financial ledger is alive
≠ every customer can access it
```

## 9. Supermarket: power outage trở thành food-loss problem

Retail impact có nhiều tầng:

```text
POS unavailable
+ lighting/access systems
+ refrigeration/freezer temperature rises
+ inventory receiving disrupted
+ warehouse routing disrupted
```

Cold chain có time-temperature limits. Một outage dài có thể biến electrical incident thành inventory write-off và food-safety issue.

Đọc [Supermarkets](../supermarkets/README.md).

## 10. Water supply cũng phụ thuộc điện

Water flows nhờ gravity ở một số segment nhưng hệ thống đô thị thường cần pumps cho intake, treatment, transmission, booster stations và high-rise buildings.

```text
source
 ↓ pump/treatment
reservoir
 ↓
distribution
 ↓ booster/building pumps
consumer
```

Nếu grid outage đủ dài, backup/pumped storage boundary bị vượt, pressure có thể giảm hoặc service gián đoạn ở một số zone.

Đọc [Water supply](../water-supply/README.md).

## 11. Sewage failure có thể xuất hiện trễ hơn

Wastewater collection/treatment cũng dùng pumps, aeration và process equipment. Một outage ngắn có thể được buffer bởi storage/backup; outage dài có thể gây overflow hoặc treatment degradation.

```text
power outage
   ↓
pump/aeration disruption
   ↓
process/storage buffer absorbs temporarily
   ↓
if prolonged
overflow / reduced treatment performance risk
```

Đọc [Sewage](../sewage/README.md).

## 12. Airport và airline chịu tác động theo nhiều lớp

Airport cần power cho:

```text
runway/taxiway systems
terminal
baggage
security
IT
communications
boarding bridges
fueling support
```

Safety-critical facilities có backup/resilience requirements, nhưng severe disruption vẫn có thể làm operation giảm capacity hoặc stop tùy affected subsystem.

Airline booking cloud có thể hoàn toàn bình thường trong khi airport ground infrastructure bị giới hạn — một ví dụ control/information plane sống nhưng physical plane degraded.

## 13. Semiconductor fab đặc biệt nhạy với power quality

Fab không chỉ cần “có điện”. Nhiều process đòi hỏi stable power, clean-room environment, vacuum, gases, ultrapure water và precise equipment control.

```text
voltage disturbance / outage
        ↓
process interrupted
        ↓
wafer lot may be lost or require requalification
        ↓
tool restart / clean / calibration
        ↓
production recovery slower than electricity restoration
```

Vì vậy **thời gian có điện trở lại (power restoration time)** có thể ngắn hơn **thời gian production trở lại (production recovery time)**.

Đọc [Semiconductors](../semiconductors/README.md).

## 14. Cascade có nhiều time scale

```text
milliseconds–seconds
protection trips, UPS switches

minutes
cell/network congestion, generator starts, traffic lights fail

hours
battery depletion, retail refrigeration concern, transport disruption

many hours–days
fuel logistics, water pressure/treatment issues, warehouse backlog

days–weeks
industrial restart, semiconductor yield/production effects, supply-chain backlog
```

Failure propagation vì vậy không kết thúc khi grid indicator chuyển từ red sang green.

## 15. Korea ↔ Vietnam — resilience phải đọc theo topology

Không nên kết luận đơn giản rằng nước nào “dễ mất điện hơn” chỉ từ anecdote. Hai hệ thống có:

```text
different generation mix
transmission topology
demand growth
weather exposure
urban density
industrial load concentration
backup penetration
```

Hàn Quốc có power-intensive industrial clusters, data centers và dense urban services; một disruption ở critical node có downstream economic concentration cao.

Việt Nam có demand growth nhanh và geography kéo dài Bắc–Nam; planning, generation additions và transmission capacity phải theo kịp load growth và regional balance.

Khi so sánh, hãy hỏi **failure domain** và **restoration topology**, không chỉ annual outage statistic.

## 16. Common-mode failure là gì?

Redundancy chỉ hữu ích nếu redundant paths không cùng chết vì một nguyên nhân.

```text
Server A on UPS A
Server B on UPS B
```

trông redundant. Nhưng nếu:

```text
UPS A + UPS B
both depend on same switchboard
```

thì switchboard là common-mode dependency.

Tương tự:

- hai Internet links đi chung một conduit;
- hai generators dùng cùng flooded fuel room;
- multi-cloud apps phụ thuộc cùng DNS/identity provider;
- hai warehouse routes cùng phải qua một bridge.

## 17. Restoration cũng là scheduling problem

Sau outage diện rộng, operator không chỉ “bật tất cả lại”. Power system restoration phải cân bằng generation/load và tránh inrush/instability. Telecom teams phải prioritize critical sites; enterprises phải kiểm tra systems trước khi resume.

Một service có thể return theo thứ tự:

```text
power restored
   ↓
network equipment boots
   ↓
routing converges
   ↓
servers/databases recover
   ↓
applications reconnect
   ↓
queues/backlogs drain
   ↓
normal service
```

Do đó “đã có điện” không có nghĩa “mọi app hoạt động ngay”.

## 18. Mental model cuối

Blackout là bài học tốt nhất về **dependency graph**:

```text
Electricity
├── Telecom
│   ├── Internet
│   └── Mobile access
├── Cloud / data centers
├── Banking/payment access
├── Retail / cold chain
├── Airports / transport
├── Water / sewage
└── Semiconductor / industry
```

Resilience không phải có một UPS. Nó là khả năng giữ critical function qua nhiều failure layer và phục hồi theo thứ tự có kiểm soát.

## Đọc tiếp

- [Electricity grid](../electricity-grid/README.md)
- [Mobile networks](../mobile-networks/README.md)
- [Internet](../internet/README.md)
- [Cloud computing](../cloud-computing/README.md)
- [Water supply](../water-supply/README.md)
- [Sewage](../sewage/README.md)
- [Semiconductors](../semiconductors/README.md)
