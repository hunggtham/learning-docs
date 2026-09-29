# Power Electronics — Điện tử công suất

> **Mạch đọc:** Đọc **Power Electronics — Điện tử công suất** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **cốt lõi (core / 핵심) tuyến (route / 경로)** sang **cốt lõi (core / 핵심) chapter**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Power electronics điều khiển dòng năng lượng bằng semiconductor switch, magnetics, capacitors và phản hồi (feedback / 피드백). Khác với tín hiệu (signal / 신호) electronics, thermal, isolation, EMI và fault năng lượng (energy / 에너지) có thể quyết định an toàn của toàn hệ thống.

## Cốt lõi (core / 핵심) tuyến (route / 경로)
Phần “Cốt lõi (core / 핵심) tuyến (route / 경로)” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```text
switching device → rectifier/inverter → buck/boost → PWM/control → magnetics → EMI/thermal/protection
```


> **Chuyển mạch:** Từ **cốt lõi (core / 핵심) tuyến (route / 경로)**, ta sang **cốt lõi (core / 핵심) chapter** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cốt lõi (core / 핵심) chapter
Phần “Cốt lõi (core / 핵심) chapter” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- [Switching converters and protection](00_switching_converters_protection.md) — buck mô hình (model / 모델), ripple, losses, thermal đường dẫn (path / 경로), protection và EMI/bố cục (layout / 레이아웃).
- [Inverter, battery and EMI](01_inverter_battery_emi.md) — half-bridge, dead thời gian (time / 시간), SOC bất định (uncertainty / 불확실성), derating và dùng chung (common / 공통)/differential-mode noise.


> **Chuyển mạch:** Từ **cốt lõi (core / 핵심) chapter**, ta sang **Cần nắm** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cần nắm
Phần “Cần nắm” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- conduction/switching mất mát (loss / 손실), dead thời gian (time / 시간), reverse khôi phục (recovery / 복구) và safe operating area;
- inductor/capacitor ripple, continuous/discontinuous conduction và converter efficiency;
- gate drive, isolation, snubber, hiện tại (current / 현재) limit và short-circuit protection;
- vòng lặp (loop / 루프) compensation, transient phản hồi (response / 응답), thermal đường dẫn (path / 경로) và derating;
- battery/charger interfaces, power integrity, EMI/EMC và compliance ranh giới (boundary / 경계).


> **Chuyển mạch:** Từ **Cần nắm**, ta sang **cầu nối (bridge / 브리지)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Mạch và điều khiển (control / 제어) là prerequisite; semiconductor thiết bị (device / 장치) physics quay về [Physics](../../physics/10_condensed_matter_devices/01_semiconductors_devices.md). Đi tiếp sang embedded khi converter cần digital điều khiển (control / 제어) hoặc telemetry.

> **Bàn giao:** Sau **cầu nối (bridge / 브리지)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 switching converters protection](./00_switching_converters_protection.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
