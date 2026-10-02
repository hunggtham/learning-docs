# Transforms and Estimation — Biến đổi và ước lượng

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Transforms and Estimation — Biến đổi và ước lượng**. Route đi từ Laplace/Z transform → transient và discrete filters → matched filtering → state estimation và noisy measurement → ứng dụng sensor/control, để biến đổi toán học nối với quyết định đo lường.

LTI chapter giải thích filtering cơ bản. Chapter này thêm các công cụ để đọc transient, thiết kế discrete filter và ước lượng trạng thái (state / 상태) khi đo lường (measurement / 측정) nhiễu.

## 1. Laplace và Z transform

Laplace biến differential equation thành algebraic quan hệ (relation / 관계) và giữ thông tin về initial điều kiện (condition / 조건) qua region of convergence. Z transform là counterpart discrete-time; pole gần đơn vị (unit / 단위) circle tạo phản hồi (response / 응답) dài và sensitivity cao.

Transfer hàm (function / 함수) chỉ mô tả zero-state phản hồi (response / 응답). Khi startup, reset hoặc disturbance lớn, trạng thái (state / 상태)/initial điều kiện (condition / 조건) phải được mô hình hóa riêng.

> **Chuyển mạch:** Trong **Transforms and Estimation — Biến đổi và ước lượng**, **2. Matched filtering** tiếp nhận điểm tựa từ **1. Laplace và Z transform** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. trạng thái (state / 상태) estimation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Matched filtering

Nếu biết waveform mẫu trong white Gaussian noise, matched filter tối đa SNR tại thời điểm sampling. Đây là nguyên tắc phía sau pulse detection và nhiều receiver; nó không có nghĩa filter càng hẹp luôn tốt hơn vì timing bất định (uncertainty / 불확실성) và channel distortion vẫn tồn tại.

> **Chuyển mạch:** Ở chặng này của **Transforms and Estimation — Biến đổi và ước lượng**, **3. trạng thái (state / 상태) estimation** tiếp nhận điểm tựa từ **2. Matched filtering** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Worked lập luận (reasoning / 추론): sensor fusion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. trạng thái (state / 상태) estimation

Một state-space mô hình (model / 모델) có thể viết:

    x[k+1] = A x[k] + B u[k] + w[k]
    y[k] = C x[k] + v[k]

Kalman filter kết hợp mô hình (model / 모델) prediction với đo lường (measurement / 측정) cập nhật (update / 업데이트) theo covariance bất định (uncertainty / 불확실성). Nếu noise covariance đặt sai, estimator có thể quá tin mô hình (model / 모델) hoặc quá tin sensor.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Transforms and Estimation — Biến đổi và ước lượng**, **3. trạng thái (state / 상태) estimation** cho ta quy tắc; **4. Worked lập luận (reasoning / 추론): sensor fusion** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Thất bại (failure / 실패) modes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Worked lập luận (reasoning / 추론): sensor fusion

Accelerometer cho phản hồi (response / 응답) nhanh nhưng drift khi tích phân; encoder chính xác vị trí nhưng có quantization/dropout. Estimator cần biểu diễn độ lệch (bias / 편향) và timestamp, không chỉ average hai số. Innovation residual là tín hiệu (signal / 신호) để detect sensor fault hoặc mô hình (model / 모델) mismatch.

> **Chuyển mạch:** Trong **Transforms and Estimation — Biến đổi và ước lượng**, **4. Worked lập luận (reasoning / 추론): sensor fusion** cho ta quy tắc; **Thất bại (failure / 실패) modes** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Cầu nối (bridge / 브리지)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thất bại (failure / 실패) modes

- filter ổn định nhưng độ trễ (latency / 지연 시간) phá vòng điều khiển (control loop / 제어 루프);
- timestamp không đồng bộ làm correlation sai;
- covariance bằng zero giả tạo certainty;
- interpolation che giấu packet mất mát (loss / 손실) thay vì báo bất định (uncertainty / 불확실성).

> **Chuyển mạch:** Ở chặng này của **Transforms and Estimation — Biến đổi và ước lượng**, **Cầu nối (bridge / 브리지)** tiếp nhận điểm tựa từ **Thất bại (failure / 실패) modes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Đi tiếp sang [communication systems](../communication_systems/00_modulation_channel_coding.md) cho detection qua channel và [control systems](../control_systems/00_feedback_stability_pid.md) cho observer/phản hồi (feedback / 피드백).

> **Bàn giao:** Sau **Cầu nối (bridge / 브리지)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
