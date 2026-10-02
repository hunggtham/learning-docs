# Power Electronics — Điện tử công suất

> **Mạch đọc:** README này là owner của **Power Electronics — Điện tử công suất**. Route đi từ switching semiconductors, magnetics và feedback → converters → inverter/battery → EMI, thermal, isolation và protection → system safety/validation, để dòng năng lượng được nối với giới hạn vật lý.

Power electronics điều khiển dòng năng lượng bằng semiconductor switch, magnetics, capacitors và phản hồi (feedback / 피드백). Khác với tín hiệu (signal / 신호) electronics, thermal, isolation, EMI và fault năng lượng (energy / 에너지) có thể quyết định an toàn của toàn hệ thống.

## Cốt lõi (core / 핵심) tuyến (route / 경로)

```text
switching device → rectifier/inverter → buck/boost → PWM/control → magnetics → EMI/thermal/protection
```

> **Chuyển mạch:** Trong **Power Electronics — Điện tử công suất**, **Cốt lõi (core / 핵심) chapter** tiếp nhận điểm tựa từ **Cốt lõi (core / 핵심) tuyến (route / 경로)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cần nắm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cốt lõi (core / 핵심) chapter

- [Switching converters and protection](00_switching_converters_protection.md) — buck mô hình (model / 모델), ripple, losses, thermal đường dẫn (path / 경로), protection và EMI/bố cục (layout / 레이아웃).
- [Inverter, battery and EMI](01_inverter_battery_emi.md) — half-bridge, dead thời gian (time / 시간), SOC bất định (uncertainty / 불확실성), derating và dùng chung (common / 공통)/differential-mode noise.

> **Chuyển mạch:** Ở chặng này của **Power Electronics — Điện tử công suất**, **Cần nắm** tiếp nhận điểm tựa từ **Cốt lõi (core / 핵심) chapter** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cầu nối (bridge / 브리지)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cần nắm

- conduction/switching mất mát (loss / 손실), dead thời gian (time / 시간), reverse khôi phục (recovery / 복구) và safe operating area;
- inductor/capacitor ripple, continuous/discontinuous conduction và converter efficiency;
- gate drive, isolation, snubber, hiện tại (current / 현재) limit và short-circuit protection;
- vòng lặp (loop / 루프) compensation, transient phản hồi (response / 응답), thermal đường dẫn (path / 경로) và derating;
- battery/charger interfaces, power integrity, EMI/EMC và compliance ranh giới (boundary / 경계).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Power Electronics — Điện tử công suất**, **Cầu nối (bridge / 브리지)** tiếp nhận điểm tựa từ **Cần nắm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Mạch và điều khiển (control / 제어) là prerequisite; semiconductor thiết bị (device / 장치) physics quay về [Physics](../../physics/10_condensed_matter_devices/01_semiconductors_devices.md). Đi tiếp sang embedded khi converter cần digital điều khiển (control / 제어) hoặc telemetry.

> **Bàn giao:** Sau **Cầu nối (bridge / 브리지)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
