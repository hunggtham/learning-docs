# Feedback, Stability and PID — Feedback, ổn định và PID

Control system gồm plant, sensor, actuator, controller và disturbance. Mục tiêu không phải làm output “bám reference” bằng mọi giá, mà giữ sai số, overshoot, settling time, effort và risk trong giới hạn được chỉ định.

## 1. Closed-loop model

Với plant P(s) và controller C(s), unity feedback có:

    T(s) = C(s)P(s) / (1 + C(s)P(s))
    S(s) = 1 / (1 + C(s)P(s))

Sensitivity S mô tả phản ứng với disturbance. Tăng loop gain giảm sensitivity trong một dải tần, nhưng không thể giảm mọi disturbance vì bandwidth, noise và delay.

## 2. Stability là property của loop

Closed-loop pole quyết định mode tự nhiên. Delay sensor/computation/actuator thêm phase lag; gain quá cao có thể biến feedback thành oscillation. Gain margin và phase margin là evidence tốt hơn việc nhìn một step response đẹp ở một operating point.

Saturation làm hệ phi tuyến. Khi actuator chạm giới hạn, controller vẫn tích phân error và tạo windup; khi thoát saturation, output overshoot lớn.

## 3. PID

    u(t) = Kp e(t) + Ki ∫e(t)dt + Kd de(t)/dt

- P giảm error nhanh nhưng có thể để steady-state error.
- I xóa steady-state error nhưng tăng overshoot/windup.
- D dự đoán slope nhưng khuếch đại noise, thường cần derivative filter.

PID không phải tuning recipe phổ quát. Cần biết actuator limit, sample time, sensor noise, plant delay và operating region.

## 4. Worked reasoning: nhiệt độ lò

Plant nhiệt có time constant lớn và delay. Nếu tăng Kp tới khi step response nhanh, lò có thể overshoot vì nhiệt tiếp tục tích lũy sau khi heater đã tắt. Ki quá lớn làm windup trong giai đoạn warm-up. Thiết kế thực tế cần output limit, anti-windup, rate limit, sensor filtering và alarm/fail-safe state.

Với heater bị stuck-on, controller software không đủ; cần independent thermal cutoff.

## 5. State-space và observer

    x_dot = Ax + Bu
    y = Cx + Du

State-space hữu ích khi có nhiều input/output, coupling hoặc constraints. Observability hỏi liệu state bên trong có suy ra từ output đo được không. Observer không tạo information mới; nếu sensor không đo được mode nào, estimator chỉ đang dựa vào model.

## 6. Digital control

Sampling và computation delay biến controller thành discrete system. Sample time phải đủ nhanh so với dominant dynamics nhưng không quá nhanh khiến noise/computation load chi phối. Cần kiểm tra quantization, ADC delay, jitter, missed deadline, zero-order hold, numeric overflow và fixed-point scaling.

## 7. Verification

- model plant với uncertainty, không chỉ nominal;
- step/frequency response ở nhiều load và temperature;
- disturbance rejection và sensor dropout;
- hardware-in-the-loop với fault injection;
- chứng minh actuator không vượt safe operating area.

## Failure modes

- sign feedback nhầm;
- tune PID trên plant khác operating point;
- sensor filter tạo delay không được tính;
- retry/timeout của software tạo input discontinuity;
- controller ổn định nhưng actuator/power stage không đủ bandwidth.

## Bridge

Đi tiếp sang [embedded systems](../embedded_systems/00_mcu_runtime_real_time.md) cho scheduling/timing, hoặc [power electronics](../power_electronics/00_switching_converters_protection.md) cho converter loop và actuator energy.
