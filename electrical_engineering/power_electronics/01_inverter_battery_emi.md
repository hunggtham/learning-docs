# Inverter, Battery and EMI — Inverter, pin và tương thích điện từ

> **Mạch đọc:** Đặt **Inverter, Battery and EMI — Inverter, pin và tương thích điện từ** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Inverter và dead thời gian (time / 시간)** sang **2. Battery giao diện (interface / 인터페이스)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Converter chapter bắt đầu từ buck. Hệ công suất thực tế còn phải đổi DC/AC, quản lý battery trạng thái (state / 상태) và chứng minh EMI/thermal trong enclosure.

## 1. Inverter và dead thời gian (time / 시간)

Half-bridge tạo điện áp xoay chiều bằng hai switch bổ sung. Dead thời gian (time / 시간) tránh shoot-through nhưng tạo distortion và diode conduction. PWM chiến lược (strategy / 전략) cần xét modulation chỉ mục (index / 인덱스), switching mất mát (loss / 손실), common-mode voltage và motor/tải (load / 로드) hành vi (behavior / 동작).


> **Chuyển mạch:** Từ **1. Inverter và dead thời gian (time / 시간)**, ta sang **2. Battery giao diện (interface / 인터페이스)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 2. Battery giao diện (interface / 인터페이스)

Battery voltage phụ thuộc trạng thái (state / 상태) of charge, temperature, hiện tại (current / 현재) và aging. Charger cần hiện tại (current / 현재)/voltage limits, cell balancing, precharge và protection. trạng thái (state / 상태) of charge là estimate với bất định (uncertainty / 불확실성), không phải đo lường (measurement / 측정) trực tiếp.


> **Chuyển mạch:** Từ **2. Battery giao diện (interface / 인터페이스)**, ta sang **3. EMI/EMC** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 3. EMI/EMC

Common-mode và differential-mode noise có đường truyền khác nhau. Filter, shielding, grounding và bố cục (layout / 레이아웃) phải cùng được xem như mạng (network / 네트워크); thêm một capacitor có thể tạo resonance hoặc tăng leakage hiện tại (current / 현재).


> **Chuyển mạch:** Từ **3. EMI/EMC**, ta sang **4. Worked lập luận (reasoning / 추론): thermal derating** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 4. Worked lập luận (reasoning / 추론): thermal derating

Converter đạt 95% efficiency ở 100 W nghĩa là 5 W mất mát (loss / 손실). Trong enclosure có θJA 12 °C/W, junction có thể cao hơn ambient khoảng 60 °C trước khi tính hotspot và airflow. Chạy 150 W không chỉ quy mô (scale / 규모) hiện tại (current / 현재); switching, magnetic và thermal margin đều đổi.


> **Chuyển mạch:** Từ **4. Worked lập luận (reasoning / 추론): thermal derating**, ta sang **cầu nối (bridge / 브리지)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Đi tiếp sang [control systems](../control_systems/01_state_space_discrete_control.md), [embedded systems](../embedded_systems/01_rtos_scheduling_verification.md) và Physics về electromagnetic tính tương thích (compatibility / 호환성).

> **Bàn giao:** Sau **cầu nối (bridge / 브리지)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 switching converters protection](./00_switching_converters_protection.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
