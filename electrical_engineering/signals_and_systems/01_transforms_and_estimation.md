# Transforms and Estimation — Biến đổi và ước lượng

LTI chapter giải thích filtering cơ bản. Chapter này thêm các công cụ để đọc transient, thiết kế discrete filter và ước lượng state khi measurement nhiễu.

## 1. Laplace và Z transform

Laplace biến differential equation thành algebraic relation và giữ thông tin về initial condition qua region of convergence. Z transform là counterpart discrete-time; pole gần unit circle tạo response dài và sensitivity cao.

Transfer function chỉ mô tả zero-state response. Khi startup, reset hoặc disturbance lớn, state/initial condition phải được mô hình hóa riêng.

## 2. Matched filtering

Nếu biết waveform mẫu trong white Gaussian noise, matched filter tối đa SNR tại thời điểm sampling. Đây là nguyên tắc phía sau pulse detection và nhiều receiver; nó không có nghĩa filter càng hẹp luôn tốt hơn vì timing uncertainty và channel distortion vẫn tồn tại.

## 3. State estimation

Một state-space model có thể viết:

    x[k+1] = A x[k] + B u[k] + w[k]
    y[k] = C x[k] + v[k]

Kalman filter kết hợp model prediction với measurement update theo covariance uncertainty. Nếu noise covariance đặt sai, estimator có thể quá tin model hoặc quá tin sensor.

## 4. Worked reasoning: sensor fusion

Accelerometer cho response nhanh nhưng drift khi tích phân; encoder chính xác vị trí nhưng có quantization/dropout. Estimator cần biểu diễn bias và timestamp, không chỉ average hai số. Innovation residual là signal để detect sensor fault hoặc model mismatch.

## Failure modes

- filter ổn định nhưng latency phá control loop;
- timestamp không đồng bộ làm correlation sai;
- covariance bằng zero giả tạo certainty;
- interpolation che giấu packet loss thay vì báo uncertainty.

## Bridge

Đi tiếp sang [communication systems](../communication_systems/00_modulation_channel_coding.md) cho detection qua channel và [control systems](../control_systems/00_feedback_stability_pid.md) cho observer/feedback.
