# Phản hồi (feedback / 피드백), Stability and PID — phản hồi (feedback / 피드백), ổn định và PID

> **Mạch đọc:** Đặt **phản hồi (feedback / 피드백), Stability and PID — phản hồi (feedback / 피드백), ổn định và PID** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Closed-loop mô hình (model / 모델)** sang **2. Stability là thuộc tính (property / 속성) của vòng lặp (loop / 루프)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Điều khiển (control / 제어) hệ thống (system / 시스템) gồm plant, sensor, actuator, controller và disturbance. Mục tiêu không phải làm đầu ra (output / 출력) “bám tham chiếu (reference / 참조)” bằng mọi giá, mà giữ sai số, overshoot, settling thời gian (time / 시간), effort và rủi ro (risk / 위험) trong giới hạn được chỉ định.

## 1. Closed-loop mô hình (model / 모델)

Với plant P(s) và controller C(s), unity phản hồi (feedback / 피드백) có:

    T(s) = C(s)P(s) / (1 + C(s)P(s))
    S(s) = 1 / (1 + C(s)P(s))

Sensitivity S mô tả phản ứng với disturbance. Tăng vòng lặp (loop / 루프) gain giảm sensitivity trong một dải tần, nhưng không thể giảm mọi disturbance vì bandwidth, noise và delay.


> **Chuyển mạch:** Từ **1. Closed-loop mô hình (model / 모델)**, ta sang **2. Stability là thuộc tính (property / 속성) của vòng lặp (loop / 루프)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 2. Stability là thuộc tính (property / 속성) của vòng lặp (loop / 루프)

Closed-loop pole quyết định chế độ (mode / 모드) tự nhiên. Delay sensor/computation/actuator thêm phase lag; gain quá cao có thể biến phản hồi (feedback / 피드백) thành oscillation. Gain margin và phase margin là bằng chứng (evidence / 증거) tốt hơn việc nhìn một step phản hồi (response / 응답) đẹp ở một operating điểm (point / 지점).

Saturation làm hệ phi tuyến. Khi actuator chạm giới hạn, controller vẫn tích phân lỗi (error / 오류) và tạo windup; khi thoát saturation, đầu ra (output / 출력) overshoot lớn.


> **Chuyển mạch:** Từ **2. Stability là thuộc tính (property / 속성) của vòng lặp (loop / 루프)**, ta sang **3. PID** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 3. PID

    u(t) = Kp e(t) + Ki ∫e(t)dt + Kd de(t)/dt

- P giảm lỗi (error / 오류) nhanh nhưng có thể để steady-state lỗi (error / 오류).
- I xóa steady-state lỗi (error / 오류) nhưng tăng overshoot/windup.
- D dự đoán slope nhưng khuếch đại noise, thường cần derivative filter.

PID không phải tuning recipe phổ quát. Cần biết actuator limit, mẫu (sample / 표본) thời gian (time / 시간), sensor noise, plant delay và operating region.


> **Chuyển mạch:** Từ **3. PID**, ta sang **4. Worked lập luận (reasoning / 추론): nhiệt độ lò** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 4. Worked lập luận (reasoning / 추론): nhiệt độ lò

Plant nhiệt có thời gian (time / 시간) constant lớn và delay. Nếu tăng Kp tới khi step phản hồi (response / 응답) nhanh, lò có thể overshoot vì nhiệt tiếp tục tích lũy sau khi heater đã tắt. Ki quá lớn làm windup trong giai đoạn warm-up. Thiết kế thực tế cần đầu ra (output / 출력) limit, anti-windup, tỷ lệ (rate / 비율) limit, sensor filtering và alarm/fail-safe trạng thái (state / 상태).

Với heater bị stuck-on, controller software không đủ; cần independent thermal cutoff.


> **Chuyển mạch:** Từ **4. Worked lập luận (reasoning / 추론): nhiệt độ lò**, ta sang **5. State-space và observer** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 5. State-space và observer

    x_dot = Ax + Bu
    y = Cx + Du

State-space hữu ích khi có nhiều đầu vào (input / 입력)/đầu ra (output / 출력), coupling hoặc các ràng buộc (constraints / 제약조건들). khả năng quan sát (observability / 관측 가능성) hỏi liệu trạng thái (state / 상태) bên trong có suy ra từ đầu ra (output / 출력) đo được không. Observer không tạo thông tin (information / 정보) mới; nếu sensor không đo được chế độ (mode / 모드) nào, estimator chỉ đang dựa vào mô hình (model / 모델).


> **Chuyển mạch:** Từ **5. State-space và observer**, ta sang **6. Digital điều khiển (control / 제어)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 6. Digital điều khiển (control / 제어)

Sampling và computation delay biến controller thành discrete hệ thống (system / 시스템). mẫu (sample / 표본) thời gian (time / 시간) phải đủ nhanh so với dominant dynamics nhưng không quá nhanh khiến noise/computation tải (load / 로드) chi phối. Cần kiểm tra quantization, ADC delay, jitter, missed deadline, zero-order hold, numeric overflow và fixed-point scaling.


> **Chuyển mạch:** Từ **6. Digital điều khiển (control / 제어)**, ta sang **7. xác minh (verification / 확인)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 7. xác minh (verification / 확인)

- mô hình (model / 모델) plant với bất định (uncertainty / 불확실성), không chỉ nominal;
- step/frequency phản hồi (response / 응답) ở nhiều tải (load / 로드) và temperature;
- disturbance rejection và sensor dropout;
- hardware-in-the-loop với fault injection;
- chứng minh actuator không vượt safe operating area.


> **Chuyển mạch:** Từ **7. xác minh (verification / 확인)**, ta sang **thất bại (failure / 실패) modes** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Thất bại (failure / 실패) modes

- sign phản hồi (feedback / 피드백) nhầm;
- tune PID trên plant khác operating điểm (point / 지점);
- sensor filter tạo delay không được tính;
- thử lại (retry / 재시도)/hết thời gian chờ (timeout / 타임아웃) của software tạo đầu vào (input / 입력) discontinuity;
- controller ổn định nhưng actuator/power stage không đủ bandwidth.


> **Chuyển mạch:** Từ **thất bại (failure / 실패) modes**, ta sang **cầu nối (bridge / 브리지)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Đi tiếp sang [embedded systems](../embedded_systems/00_mcu_runtime_real_time.md) cho scheduling/timing, hoặc [power electronics](../power_electronics/00_switching_converters_protection.md) cho converter vòng lặp (loop / 루프) và actuator năng lượng (energy / 에너지).

> **Bàn giao:** Sau **cầu nối (bridge / 브리지)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 state space discrete control](./01_state_space_discrete_control.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
