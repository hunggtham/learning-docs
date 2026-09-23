# Inverter, Battery and EMI — Inverter, pin và tương thích điện từ

Converter chapter bắt đầu từ buck. Hệ công suất thực tế còn phải đổi DC/AC, quản lý battery state và chứng minh EMI/thermal trong enclosure.

## 1. Inverter và dead time

Half-bridge tạo điện áp xoay chiều bằng hai switch bổ sung. Dead time tránh shoot-through nhưng tạo distortion và diode conduction. PWM strategy cần xét modulation index, switching loss, common-mode voltage và motor/load behavior.

## 2. Battery interface

Battery voltage phụ thuộc state of charge, temperature, current và aging. Charger cần current/voltage limits, cell balancing, precharge và protection. State of charge là estimate với uncertainty, không phải measurement trực tiếp.

## 3. EMI/EMC

Common-mode và differential-mode noise có đường truyền khác nhau. Filter, shielding, grounding và layout phải cùng được xem như network; thêm một capacitor có thể tạo resonance hoặc tăng leakage current.

## 4. Worked reasoning: thermal derating

Converter đạt 95% efficiency ở 100 W nghĩa là 5 W loss. Trong enclosure có θJA 12 °C/W, junction có thể cao hơn ambient khoảng 60 °C trước khi tính hotspot và airflow. Chạy 150 W không chỉ scale current; switching, magnetic và thermal margin đều đổi.

## Bridge

Đi tiếp sang [control systems](../control_systems/01_state_space_discrete_control.md), [embedded systems](../embedded_systems/01_rtos_scheduling_verification.md) và Physics về electromagnetic compatibility.
