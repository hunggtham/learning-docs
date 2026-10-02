# State-Space and Discrete điều khiển (control / 제어) — State-space và điều khiển số

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **State-Space and Discrete điều khiển (control / 제어) — State-space và điều khiển số**. Route đi từ state-space model → controllability/observability → discretization và sampling → state feedback, observers và digital control → constraints, để mô hình nhiều trạng thái dẫn tới thiết kế điều khiển.

Transfer hàm (function / 함수) trực quan cho SISO tuyến tính; state-space mạnh hơn khi có nhiều trạng thái (state / 상태), đầu vào (input / 입력)/đầu ra (output / 출력), coupling và ràng buộc (constraint / 제약조건).

## 1. Controllability và khả năng quan sát (observability / 관측 가능성)

Controllability hỏi đầu vào (input / 입력) có thể đưa trạng thái (state / 상태) tới vùng mong muốn không. khả năng quan sát (observability / 관측 가능성) hỏi đầu ra (output / 출력) đo được có đủ để suy ra trạng thái (state / 상태) không. Không controller nào sửa được một chế độ (mode / 모드) không controllable; không observer nào tạo được thông tin (information / 정보) bị sensor bỏ qua.

> **Chuyển mạch:** Trong **State-Space and Discrete điều khiển (control / 제어) — State-space và điều khiển số**, **1. Controllability và khả năng quan sát (observability / 관측 가능성)** cho ta quy tắc; **2. Discretization** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **3. Discrete PID** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Discretization

Plant continuous được mẫu (sample / 표본) với period Ts. Zero-order hold, computational delay và jitter tạo discrete dynamics khác mô hình continuous đơn giản. Ts phải được chọn từ dominant pole, bandwidth và worst-case thực thi (execution / 실행) thời gian (time / 시간).

> **Chuyển mạch:** Ở chặng này của **State-Space and Discrete điều khiển (control / 제어) — State-space và điều khiển số**, **3. Discrete PID** tiếp nhận điểm tựa từ **2. Discretization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Worked lập luận (reasoning / 추론): actuator deadline** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Discrete PID

Integral và derivative cần discretize có chủ đích. Derivative trên đo lường (measurement / 측정) có thể tránh derivative kick khi tham chiếu (reference / 참조) step; integral cần anti-windup và giới hạn numeric. Fixed-point hiện thực (implementation / 구현) phải có scaling và overflow proof.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **State-Space and Discrete điều khiển (control / 제어) — State-space và điều khiển số**, **3. Discrete PID** cho ta quy tắc; **4. Worked lập luận (reasoning / 추론): actuator deadline** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **5. xác minh (verification / 확인)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Worked lập luận (reasoning / 추론): actuator deadline

Nếu vòng điều khiển (control loop / 제어 루프) chạy mỗi 1 ms nhưng tác vụ (task / 작업) đôi khi hoàn thành sau 1.4 ms, controller không chỉ “chậm hơn”: nó tạo variable delay và có thể làm phase margin giảm. Giải pháp có thể là giảm mô hình (model / 모델) chi phí (cost / 비용), ưu tiên tác vụ (task / 작업), tăng Ts có kiểm chứng, hoặc thiết kế controller robust với delay; không che bằng thử lại (retry / 재시도).

> **Chuyển mạch:** Trong **State-Space and Discrete điều khiển (control / 제어) — State-space và điều khiển số**, **4. Worked lập luận (reasoning / 추론): actuator deadline** cho ta quy tắc; **5. xác minh (verification / 확인)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Cầu nối (bridge / 브리지)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. xác minh (verification / 확인)

- pole placement ở nominal và parameter corners;
- disturbance/noise injection;
- saturation, sensor dropout và reset giữa vòng lặp (loop / 루프);
- HIL với timestamp thật;
- kiểm tra bất biến (invariant / 불변식) an toàn trước khi tối ưu phản hồi (response / 응답).

> **Chuyển mạch:** Ở chặng này của **State-Space and Discrete điều khiển (control / 제어) — State-space và điều khiển số**, **Cầu nối (bridge / 브리지)** tiếp nhận điểm tựa từ **5. xác minh (verification / 확인)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Đi tiếp sang [embedded systems](../embedded_systems/00_mcu_runtime_real_time.md) để biến controller thành tác vụ (task / 작업) có deadline, và [power electronics](../power_electronics/00_switching_converters_protection.md) cho plant công suất.

> **Bàn giao:** Sau **Cầu nối (bridge / 브리지)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
