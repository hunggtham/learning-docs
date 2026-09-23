# Switching Converters and Protection — Converter, switching và bảo vệ

Power electronics điều khiển năng lượng lớn bằng các phần tử đóng/ngắt nhanh. Khác với signal chain, một lỗi ngắn mạch có thể phá hỏng silicon, trace hoặc gây hazard trước khi software kịp phản ứng.

## 1. Buck converter lý tưởng

Ở continuous conduction mode, buck converter lý tưởng có:

    Vout ≈ D · Vin

D là duty cycle. Inductor làm dòng liên tục; capacitor giảm ripple voltage. Trong thực tế phải xét switch Ron, diode/MOSFET drop, ESR, dead time và switching loss.

## 2. Energy và ripple

Inductor không cho dòng đổi tức thời:

    ΔIL = VL · Δt / L

Capacitor không cho voltage đổi tức thời:

    ΔVC ≈ IC · Δt / C

Ripple quá lớn gây output noise, control instability, magnetic saturation hoặc violation của load.

## 3. Loss và thermal path

Conduction loss gần Pcond ≈ Irms² Ron. Switching loss phụ thuộc voltage, current, transition time và frequency. Tổng loss đi qua junction → package → PCB/heatsink → ambient. Nhiệt độ junction gần:

    Tj ≈ Ta + Ploss · θJA

Chọn component theo average current là chưa đủ; phải xét peak current, SOA, transient và derating.

## 4. Control loop và compensation

Converter là plant có poles từ LC filter và zero từ ESR. Feedback controller phải đạt transient response nhưng giữ phase margin qua input voltage, load và component tolerance. Current-mode control thêm inner loop nhưng cần slope compensation ở một số duty cycle.

## 5. Protection

Các lớp thường cần cycle-by-cycle over-current, short-circuit response, over-voltage/under-voltage lockout, over-temperature, reverse polarity, inrush limiting, shoot-through prevention/dead time và isolation khi fault domain khác nhau.

Protection không chỉ là “ngắt khi quá dòng”; phải xem năng lượng còn lại trong inductor/capacitor và đường discharge.

## 6. Worked reasoning: chọn inductor

Nếu buck 12 V → 5 V, fs = 500 kHz, Iout = 2 A, chọn ripple target 30% tức ΔIL = 0.6 A. Duty lý tưởng D ≈ 5/12. Trong on-time, VL ≈ 7 V, nên:

    L ≈ VL · D / (fs · ΔIL)

Sau khi tính, phải kiểm tra saturation current, copper loss, core loss, DCR và transient load. Một giá trị L đúng trên công thức nhưng saturate ở startup là thiết kế sai.

## 7. EMI/EMC và layout

Vòng dòng switching càng lớn thì di/dt và nhiễu bức xạ/conduction càng khó kiểm soát. Layout cần high di/dt loop nhỏ, gate loop ngắn, power/analog ground có chủ đích và sense Kelvin.

EMI filter thêm poles/impedance và có thể làm control loop thay đổi; không thêm filter sau cùng mà không re-verify stability.

## Failure modes

- switch node ringing vượt VDS rating;
- diode reverse recovery tạo shoot-through;
- inductor saturation làm current spike;
- thermal runaway do Ron tăng theo nhiệt;
- protection chậm hơn fault energy;
- probe ground lead tạo ringing giả.

## Bridge

Đi tiếp sang [control systems](../control_systems/00_feedback_stability_pid.md) để phân tích loop, [embedded systems](../embedded_systems/00_mcu_runtime_real_time.md) cho digital power control, và Physics về semiconductor/device behavior.
