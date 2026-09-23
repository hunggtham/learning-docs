# State-Space and Discrete Control — State-space và điều khiển số

Transfer function trực quan cho SISO tuyến tính; state-space mạnh hơn khi có nhiều state, input/output, coupling và constraint.

## 1. Controllability và observability

Controllability hỏi input có thể đưa state tới vùng mong muốn không. Observability hỏi output đo được có đủ để suy ra state không. Không controller nào sửa được một mode không controllable; không observer nào tạo được information bị sensor bỏ qua.

## 2. Discretization

Plant continuous được sample với period Ts. Zero-order hold, computational delay và jitter tạo discrete dynamics khác mô hình continuous đơn giản. Ts phải được chọn từ dominant pole, bandwidth và worst-case execution time.

## 3. Discrete PID

Integral và derivative cần discretize có chủ đích. Derivative trên measurement có thể tránh derivative kick khi reference step; integral cần anti-windup và giới hạn numeric. Fixed-point implementation phải có scaling và overflow proof.

## 4. Worked reasoning: actuator deadline

Nếu control loop chạy mỗi 1 ms nhưng task đôi khi hoàn thành sau 1.4 ms, controller không chỉ “chậm hơn”: nó tạo variable delay và có thể làm phase margin giảm. Giải pháp có thể là giảm model cost, ưu tiên task, tăng Ts có kiểm chứng, hoặc thiết kế controller robust với delay; không che bằng retry.

## 5. Verification

- pole placement ở nominal và parameter corners;
- disturbance/noise injection;
- saturation, sensor dropout và reset giữa loop;
- HIL với timestamp thật;
- kiểm tra invariant an toàn trước khi tối ưu response.

## Bridge

Đi tiếp sang [embedded systems](../embedded_systems/00_mcu_runtime_real_time.md) để biến controller thành task có deadline, và [power electronics](../power_electronics/00_switching_converters_protection.md) cho plant công suất.
