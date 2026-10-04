# Vehicles — Hiểu phương tiện từ năng lượng đến ownership

`vehicles/` tập trung vào những phương tiện mà người dùng trực tiếp vận hành, sử dụng, bảo dưỡng hoặc mua. Nó không sở hữu road network, traffic control, fuel distribution hay public-transport operations; các hệ thống hạ tầng đó thuộc How Things Work khi canonical.

Mental model chung của một vehicle:

```text
energy source
→ power conversion
→ transmission / drivetrain
→ contact with ground/air/water
→ steering / control
→ braking
→ structure / protection
→ thermal + electronics
→ maintenance / wear
→ ownership lifecycle
```

Nhánh đầu tiên là [Cars](cars/README.md), vì xe hơi tập hợp đủ nhiều mechanism để tạo một reference model tái sử dụng cho những vehicle khác sau này.

## Vì sao không bắt đầu bằng brand/model?

Model name thường trộn nhiều trục:

```text
body type
powertrain
drivetrain
market segment
trim level
options
```

Nếu chưa tách các trục này, người đọc dễ so sánh `SUV`, `AWD`, `Hybrid`, `Turbo` như thể chúng là các lựa chọn cùng cấp. Vì vậy vehicles học từ architecture trước, model sau.

## Shared handoff

- vật lý lực, năng lượng, nhiệt → Physics;
- motor, inverter, battery/power electronics → Electrical Engineering;
- fuel supply, road/traffic infrastructure → How Things Work khi canonical;
- purchase affordability, loan, insurance budget → Personal Finance;
- comparison/decision process → Thinking;
- specs, durability, maintenance và lifecycle → [`../consumer_literacy/`](../consumer_literacy/README.md).

Chỉ mở motorcycle, bicycle hoặc các vehicle khác sau khi Cars đủ sâu để các khái niệm dùng chung có owner rõ.