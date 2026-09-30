# Case 09 — Đi làm trong thành phố: Seoul ↔ Hà Nội ↔ TP.HCM

Case này nối [public transport](../public-transport/README.md), [road traffic](../road-traffic/README.md), [mobile networks](../mobile-networks/README.md), [GPS](../gps/README.md), [banking/payment](../credit-card-network/README.md) và [cloud](../cloud-computing/README.md).

Mục tiêu là thấy một chuyến commute không phải “chọn bus hay metro”, mà là một chuỗi decision + network + payment + real-time control.

## 1. Trước khi rời nhà: routing đã bắt đầu

```text
origin + destination
      ↓
map/transit app
      ↓
road/transit topology
+ timetable/headway
+ live vehicle/traffic data
      ↓
route alternatives
      ↓
user chooses trip
```

App có thể dùng GPS của phone để biết origin, cloud backend để tính route và live feeds để estimate ETA.

## 2. Seoul example

Một commuter có thể:

```text
walk
 ↓
local bus
 ↓ tap T-money
subway interchange
 ↓
second subway operator/line
 ↓
walk to office
```

Passenger-facing journey có vẻ unified dù phía sau có thể có nhiều bus/rail operators.

Fare backend cần nhận tap-in/tap-out, distance và transfer timing để tính integrated fare và sau đó phân bổ revenue.

## 3. Hà Nội example

Một journey có thể:

```text
motorbike/bus/walk
 ↓
Cát Linh–Hà Đông or Nhổn–Cầu Giấy metro
 ↓
walk / bus / bike / ride-hailing
 ↓
destination
```

Hà Nội đang tăng integration giữa metro, cashless ticketing và first/last-mile services. Vì network rail chưa dày như Seoul, feeder quality và transfer friction ảnh hưởng mode choice mạnh hơn.

## 4. TP.HCM example

```text
bus / walk / bike / ride-hailing
 ↓
Metro Line 1
 ↓
feeder bus / last mile
 ↓
destination
```

Line 1 tạo high-capacity corridor nhưng citywide utility phụ thuộc bus network và interchange. Khi thêm line mới, value có thể tăng nonlinear vì nhiều origin-destination pairs bắt đầu có rail path.

## 5. Network effect

Một line đơn lẻ tạo N station pairs. Khi thêm line giao nhau, số possible journeys tăng mạnh.

```text
Line A only: stations connected along A
Line B only: stations connected along B
A intersects B:
A stations can reach B stations via transfer
```

Đây là lý do network integration quan trọng hơn chỉ tổng km.

## 6. Road traffic tương tác với public transport

Bus và last-mile modes chia đường với car/motorbike.

```text
road congestion
  ↓
bus delay
  ↓
missed rail connection / longer waiting
  ↓
lower perceived reliability
```

Bus lanes hoặc signal priority có thể bảo vệ transit travel time khỏi general traffic.

## 7. Fare/payment state

```text
tap accepted
 ↓
ride authorized
 ↓
journey continues
 ↓
tap-out / transfer events
 ↓
final fare computed
 ↓
operator clearing
```

Một gate mở là authorization to enter, không nhất thiết final fare settlement.

## 8. Real-time data loop

```text
vehicle/train position
 ↓
operations system
 ↓
ETA/feed
 ↓
passenger app
 ↓
passenger arrival pattern
 ↓
station/bus crowding
```

Information changes behavior, behavior changes load. Đây là feedback loop.

## 9. Seoul vs Vietnam cities

| Dimension | Seoul | Hà Nội / TP.HCM |
|---|---|---|
| Rail network | Dense multi-line | Early expansion stage |
| Bus role | Complement + feeder + independent network | Critical citywide backbone and feeder |
| Fare integration | Mature and normalized | Rapidly improving; still more fragmented across modes/services |
| First/last mile | Walk/bus/bike/taxi | Motorbike/ride-hailing/bus/walk particularly important |
| Main challenge | crowding, aging assets, reliability optimization | expansion, interchange, feeder design, behavior shift from private modes |

## 10. Why people may still drive even if metro is fast

Door-to-door generalized cost includes:

```text
walk time
+ wait time
+ in-vehicle time
+ transfer penalty
+ crowding discomfort
+ fare
+ reliability risk
```

A 20-minute train segment can lose against a 35-minute motorbike trip if access/transfer adds too much friction.

## 11. Failure scenario: rail disruption

```text
signaling/power incident
 ↓
train service reduced
 ↓
passengers reroute
 ↓
more demand on buses/roads
 ↓
road congestion rises
 ↓
ride-hailing prices/wait may rise
```

Transport modes are coupled through passenger substitution.

## 12. Failure scenario: mobile/cloud outage

Train/bus may continue physically, but:

- live ETA disappears;
- mobile ticketing/payment may degrade;
- ride-hailing coordination fails;
- passenger information worsens.

Physical transport and digital transport layer are separate.

## 13. What “good transit” actually means

```text
coverage
+ frequency
+ speed
+ reliability
+ easy transfer
+ fare integration
+ first/last mile
+ accessible stations
+ useful information
```

A single metric cannot capture the whole system.

## 14. Final mental model

```text
Commute
= route choice
+ access mode
+ network operation
+ transfer
+ payment
+ real-time information
+ last mile
```

Seoul cho thấy network sau khi integration đã trưởng thành trông như thế nào; Hà Nội và TP.HCM cho thấy challenge khi network đang được hình thành và phải tích hợp với city mobility vốn dựa nhiều vào road/motorbike.
