# State-Space and Discrete điều khiển (control / 제어) — State-space và điều khiển số

> **Mạch đọc:** Đặt **State-Space and Discrete điều khiển (control / 제어) — State-space và điều khiển số** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Controllability và khả năng quan sát (observability / 관측 가능성)** sang **2. Discretization**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Transfer hàm (function / 함수) trực quan cho SISO tuyến tính; state-space mạnh hơn khi có nhiều trạng thái (state / 상태), đầu vào (input / 입력)/đầu ra (output / 출력), coupling và ràng buộc (constraint / 제약조건).

## 1. Controllability và khả năng quan sát (observability / 관측 가능성)

Controllability hỏi đầu vào (input / 입력) có thể đưa trạng thái (state / 상태) tới vùng mong muốn không. khả năng quan sát (observability / 관측 가능성) hỏi đầu ra (output / 출력) đo được có đủ để suy ra trạng thái (state / 상태) không. Không controller nào sửa được một chế độ (mode / 모드) không controllable; không observer nào tạo được thông tin (information / 정보) bị sensor bỏ qua.


> **Chuyển mạch:** Từ **1. Controllability và khả năng quan sát (observability / 관측 가능성)**, ta sang **2. Discretization** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 2. Discretization

Plant continuous được mẫu (sample / 표본) với period Ts. Zero-order hold, computational delay và jitter tạo discrete dynamics khác mô hình continuous đơn giản. Ts phải được chọn từ dominant pole, bandwidth và worst-case thực thi (execution / 실행) thời gian (time / 시간).


> **Chuyển mạch:** Từ **2. Discretization**, ta sang **3. Discrete PID** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 3. Discrete PID

Integral và derivative cần discretize có chủ đích. Derivative trên đo lường (measurement / 측정) có thể tránh derivative kick khi tham chiếu (reference / 참조) step; integral cần anti-windup và giới hạn numeric. Fixed-point hiện thực (implementation / 구현) phải có scaling và overflow proof.


> **Chuyển mạch:** Từ **3. Discrete PID**, ta sang **4. Worked lập luận (reasoning / 추론): actuator deadline** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 4. Worked lập luận (reasoning / 추론): actuator deadline

Nếu vòng điều khiển (control loop / 제어 루프) chạy mỗi 1 ms nhưng tác vụ (task / 작업) đôi khi hoàn thành sau 1.4 ms, controller không chỉ “chậm hơn”: nó tạo variable delay và có thể làm phase margin giảm. Giải pháp có thể là giảm mô hình (model / 모델) chi phí (cost / 비용), ưu tiên tác vụ (task / 작업), tăng Ts có kiểm chứng, hoặc thiết kế controller robust với delay; không che bằng thử lại (retry / 재시도).


> **Chuyển mạch:** Từ **4. Worked lập luận (reasoning / 추론): actuator deadline**, ta sang **5. xác minh (verification / 확인)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 5. xác minh (verification / 확인)
Phần “5. xác minh (verification / 확인)” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- pole placement ở nominal và parameter corners;
- disturbance/noise injection;
- saturation, sensor dropout và reset giữa vòng lặp (loop / 루프);
- HIL với timestamp thật;
- kiểm tra bất biến (invariant / 불변식) an toàn trước khi tối ưu phản hồi (response / 응답).


> **Chuyển mạch:** Từ **5. xác minh (verification / 확인)**, ta sang **cầu nối (bridge / 브리지)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Đi tiếp sang [embedded systems](../embedded_systems/00_mcu_runtime_real_time.md) để biến controller thành tác vụ (task / 작업) có deadline, và [power electronics](../power_electronics/00_switching_converters_protection.md) cho plant công suất.

> **Bàn giao:** Sau **cầu nối (bridge / 브리지)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 feedback stability pid](./00_feedback_stability_pid.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
