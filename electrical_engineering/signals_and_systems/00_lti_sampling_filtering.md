# LTI, Sampling and Filtering — Hệ tuyến tính, lấy mẫu và lọc

Signals and systems tạo một abstraction chung cho sensor, audio, control và communication. Ta quan tâm signal mang năng lượng/thông tin thế nào và system biến đổi nó ra sao dưới giới hạn bandwidth, noise và sampling.

## 1. LTI system

System linear và time-invariant được đặc trưng bởi impulse response h. Output là convolution:

    y(t) = x(t) * h(t)

Trong frequency domain:

    Y(f) = X(f)H(f)

H(f) có magnitude và phase. Hai system có cùng gain magnitude nhưng phase khác nhau có thể tạo waveform transient rất khác.

## 2. Poles, zeros và stability

Với transfer function H(s) = N(s) / D(s), pole quyết định mode tự nhiên. Continuous-time system BIBO stable khi poles ở left half-plane trong các điều kiện chuẩn. Discrete-time system stable khi poles nằm trong unit circle.

Pole gần boundary tạo response chậm, ringing hoặc nhạy với parameter variation. Đây là bridge trực tiếp sang control systems.

## 3. Sampling và aliasing

Sampling signal tại fs tạo bản sao phổ cách nhau fs. Nếu signal có thành phần trên Nyquist frequency fs/2, các bản sao chồng lên nhau và alias không thể khôi phục bằng digital filter sau đó.

Quy trình đúng:

    analog anti-alias filter → sample/hold → ADC → digital processing

Tăng sample rate không sửa được front-end đã để alias đi vào; nó chỉ nới vùng transition của filter.

## 4. Quantization và SNR

ADC N bit với full-scale range VFS có bước lượng tử xấp xỉ Δ = VFS / 2^N. Quantization error không luôn là white noise; nó phụ thuộc signal và dither. Với ideal ADC full-scale sine, SNR lý tưởng gần 6.02N + 1.76 dB.

ENOB thực tế giảm bởi thermal noise, reference noise, INL/DNL, clock jitter và distortion.

## 5. Filter design

Filter là trade-off giữa passband ripple, stopband attenuation, transition width, phase và computational cost.

- FIR thường dễ có linear phase và ổn định, nhưng cần nhiều taps.
- IIR đạt transition hẹp với order thấp, nhưng phase nonlinear và nhạy coefficient quantization.
- Analog filter xử lý alias trước ADC; digital filter không thay thế nó.

## 6. Worked reasoning: sensor 0–1 kHz

Nếu signal hữu ích tới 1 kHz, có interference 8 kHz, chọn fs = 10 kS/s là nguy hiểm vì Nyquist chỉ 5 kHz và anti-alias transition quá hẹp. Chọn fs = 20 kS/s hoặc cao hơn, thiết kế analog low-pass với stopband đủ attenuation trước 10 kHz, rồi digital filter sau ADC.

Nếu clock jitter σt lớn, signal tần số cao chịu noise xấp xỉ tăng theo 2πfσt; sample rate cao không tự động làm clock tốt hơn.

## 7. Đo và kiểm chứng

- Dùng known sine để đo gain/phase theo tần số.
- So sánh spectrum trước/sau filter, không chỉ nhìn time plot.
- Kiểm tra clipping trước FFT; clipping tạo harmonic giả.
- Ghi sample rate, window, record length và calibration khi báo PSD.
- Tách sensor noise, quantization noise và electrical interference bằng controlled input.

## Failure modes

- Dùng FFT bin như frequency resolution mà quên record length/window leakage.
- Lọc sau ADC khi alias đã xảy ra.
- Nhầm group delay với phase delay trong signal transient.
- Dùng filter ổn định trên float nhưng unstable sau fixed-point quantization.

## Bridge

Đi tiếp sang [communication systems](../communication_systems/00_modulation_channel_coding.md) để truyền signal qua channel, hoặc [control systems](../control_systems/00_feedback_stability_pid.md) để đóng vòng feedback. Nền Physics là [waves/Fourier](../../physics/02_oscillations_waves/01_waves_fourier_sound.md) và [signals/noise/sampling](../../physics/12_experimental_computational/01_signals_sampling_noise.md).
