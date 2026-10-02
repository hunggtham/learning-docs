# Inverter, Battery and EMI — Inverter, pin và tương thích điện từ

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Inverter, Battery and EMI — Inverter, pin và tương thích điện từ**. Route đi từ inverter/dead time → battery interface and state → control/protection → EMI, thermal and enclosure → system validation, để năng lượng, điều khiển và an toàn được đọc cùng nhau.

Converter chapter bắt đầu từ buck. Hệ công suất thực tế còn phải đổi DC/AC, quản lý battery trạng thái (state / 상태) và chứng minh EMI/thermal trong enclosure.

## 1. Inverter và dead thời gian (time / 시간)

Half-bridge tạo điện áp xoay chiều bằng hai switch bổ sung. Dead thời gian (time / 시간) tránh shoot-through nhưng tạo distortion và diode conduction. PWM chiến lược (strategy / 전략) cần xét modulation chỉ mục (index / 인덱스), switching mất mát (loss / 손실), common-mode voltage và motor/tải (load / 로드) hành vi (behavior / 동작).

> **Chuyển mạch:** Trong **Inverter, Battery and EMI — Inverter, pin và tương thích điện từ**, **2. Battery giao diện (interface / 인터페이스)** tiếp nhận điểm tựa từ **1. Inverter và dead thời gian (time / 시간)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. EMI/EMC** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Battery giao diện (interface / 인터페이스)

Battery voltage phụ thuộc trạng thái (state / 상태) of charge, temperature, hiện tại (current / 현재) và aging. Charger cần hiện tại (current / 현재)/voltage limits, cell balancing, precharge và protection. trạng thái (state / 상태) of charge là estimate với bất định (uncertainty / 불확실성), không phải đo lường (measurement / 측정) trực tiếp.

> **Chuyển mạch:** Ở chặng này của **Inverter, Battery and EMI — Inverter, pin và tương thích điện từ**, **3. EMI/EMC** tiếp nhận điểm tựa từ **2. Battery giao diện (interface / 인터페이스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Worked lập luận (reasoning / 추론): thermal derating** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. EMI/EMC

Common-mode và differential-mode noise có đường truyền khác nhau. Filter, shielding, grounding và bố cục (layout / 레이아웃) phải cùng được xem như mạng (network / 네트워크); thêm một capacitor có thể tạo resonance hoặc tăng leakage hiện tại (current / 현재).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Inverter, Battery and EMI — Inverter, pin và tương thích điện từ**, **3. EMI/EMC** cho ta quy tắc; **4. Worked lập luận (reasoning / 추론): thermal derating** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Cầu nối (bridge / 브리지)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Worked lập luận (reasoning / 추론): thermal derating

Converter đạt 95% efficiency ở 100 W nghĩa là 5 W mất mát (loss / 손실). Trong enclosure có θJA 12 °C/W, junction có thể cao hơn ambient khoảng 60 °C trước khi tính hotspot và airflow. Chạy 150 W không chỉ quy mô (scale / 규모) hiện tại (current / 현재); switching, magnetic và thermal margin đều đổi.

> **Chuyển mạch:** Trong **Inverter, Battery and EMI — Inverter, pin và tương thích điện từ**, **4. Worked lập luận (reasoning / 추론): thermal derating** cho ta quy tắc; **Cầu nối (bridge / 브리지)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Đi tiếp sang [control systems](../control_systems/01_state_space_discrete_control.md), [embedded systems](../embedded_systems/01_rtos_scheduling_verification.md) và Physics về electromagnetic tính tương thích (compatibility / 호환성).

> **Bàn giao:** Sau **Cầu nối (bridge / 브리지)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
