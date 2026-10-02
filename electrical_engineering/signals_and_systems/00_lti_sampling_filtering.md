# LTI, Sampling and Filtering — Hệ tuyến tính, lấy mẫu và lọc

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **LTI, Sampling and Filtering — Hệ tuyến tính, lấy mẫu và lọc**. Route đi từ LTI systems → impulse/frequency response → poles, zeros và stability → sampling, aliasing và reconstruction → filter design, để tín hiệu nối với giới hạn bandwidth/noise.

Signals and các hệ thống (systems / 시스템들) tạo một lớp trừu tượng (abstraction / 추상화) chung cho sensor, audio, điều khiển (control / 제어) và communication. Ta quan tâm tín hiệu (signal / 신호) mang năng lượng/thông tin thế nào và hệ thống (system / 시스템) biến đổi nó ra sao dưới giới hạn bandwidth, noise và sampling.

## 1. LTI hệ thống (system / 시스템)

Hệ thống (system / 시스템) tuyến tính (linear / 선형) và time-invariant được đặc trưng bởi impulse phản hồi (response / 응답) h. đầu ra (output / 출력) là convolution:

    y(t) = x(t) * h(t)

Trong frequency lĩnh vực (domain / 도메인):

    Y(f) = X(f)H(f)

H(f) có magnitude và phase. Hai hệ thống (system / 시스템) có cùng gain magnitude nhưng phase khác nhau có thể tạo waveform transient rất khác.

> **Chuyển mạch:** Trong **LTI, Sampling and Filtering — Hệ tuyến tính, lấy mẫu và lọc**, **2. Poles, zeros và stability** tiếp nhận điểm tựa từ **1. LTI hệ thống (system / 시스템)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Sampling và aliasing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Poles, zeros và stability

Với transfer hàm (function / 함수) H(s) = N(s) / D(s), pole quyết định chế độ (mode / 모드) tự nhiên. Continuous-time hệ thống (system / 시스템) BIBO stable khi poles ở left half-plane trong các điều kiện chuẩn. Discrete-time hệ thống (system / 시스템) stable khi poles nằm trong đơn vị (unit / 단위) circle.

Pole gần ranh giới (boundary / 경계) tạo phản hồi (response / 응답) chậm, ringing hoặc nhạy với parameter variation. Đây là cầu nối (bridge / 브리지) trực tiếp sang điều khiển (control / 제어) các hệ thống (systems / 시스템들).

> **Chuyển mạch:** Ở chặng này của **LTI, Sampling and Filtering — Hệ tuyến tính, lấy mẫu và lọc**, **3. Sampling và aliasing** tiếp nhận điểm tựa từ **2. Poles, zeros và stability** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Quantization và SNR** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Sampling và aliasing

Sampling tín hiệu (signal / 신호) tại fs tạo bản sao phổ cách nhau fs. Nếu tín hiệu (signal / 신호) có thành phần trên Nyquist frequency fs/2, các bản sao chồng lên nhau và alias không thể khôi phục bằng digital filter sau đó.

Quy trình đúng:

    analog anti-alias filter → mẫu (sample / 표본)/hold → ADC → digital processing

Tăng mẫu (sample / 표본) tỷ lệ (rate / 비율) không sửa được front-end đã để alias đi vào; nó chỉ nới vùng chuyển tiếp (transition / 전이) của filter.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **LTI, Sampling and Filtering — Hệ tuyến tính, lấy mẫu và lọc**, **4. Quantization và SNR** tiếp nhận điểm tựa từ **3. Sampling và aliasing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Filter thiết kế (design / 설계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Quantization và SNR

ADC N bit với full-scale phạm vi (range / 범위) VFS có bước lượng tử xấp xỉ Δ = VFS / 2^N. Quantization lỗi (error / 오류) không luôn là white noise; nó phụ thuộc tín hiệu (signal / 신호) và dither. Với ideal ADC full-scale sine, SNR lý tưởng gần 6.02N + 1.76 dB.

ENOB thực tế giảm bởi thermal noise, tham chiếu (reference / 참조) noise, INL/DNL, clock jitter và distortion.

> **Chuyển mạch:** Trong **LTI, Sampling and Filtering — Hệ tuyến tính, lấy mẫu và lọc**, **5. Filter thiết kế (design / 설계)** tiếp nhận điểm tựa từ **4. Quantization và SNR** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Worked lập luận (reasoning / 추론): sensor 0–1 kHz** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Filter thiết kế (design / 설계)

Filter là sự đánh đổi (trade-off / 트레이드오프) giữa passband ripple, stopband attenuation, chuyển tiếp (transition / 전이) width, phase và computational chi phí (cost / 비용).

- FIR thường dễ có tuyến tính (linear / 선형) phase và ổn định, nhưng cần nhiều taps.
- IIR đạt chuyển tiếp (transition / 전이) hẹp với thứ tự (order / 순서) thấp, nhưng phase nonlinear và nhạy coefficient quantization.
- Analog filter xử lý alias trước ADC; digital filter không thay thế nó.

> **Chuyển mạch:** Ở chặng này của **LTI, Sampling and Filtering — Hệ tuyến tính, lấy mẫu và lọc**, **5. Filter thiết kế (design / 설계)** cho ta quy tắc; **6. Worked lập luận (reasoning / 추론): sensor 0–1 kHz** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **7. Đo và kiểm chứng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Worked lập luận (reasoning / 추론): sensor 0–1 kHz

Nếu tín hiệu (signal / 신호) hữu ích tới 1 kHz, có interference 8 kHz, chọn fs = 10 kS/s là nguy hiểm vì Nyquist chỉ 5 kHz và anti-alias chuyển tiếp (transition / 전이) quá hẹp. Chọn fs = 20 kS/s hoặc cao hơn, thiết kế analog low-pass với stopband đủ attenuation trước 10 kHz, rồi digital filter sau ADC.

Nếu clock jitter σt lớn, tín hiệu (signal / 신호) tần số cao chịu noise xấp xỉ tăng theo 2πfσt; mẫu (sample / 표본) tỷ lệ (rate / 비율) cao không tự động làm clock tốt hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **LTI, Sampling and Filtering — Hệ tuyến tính, lấy mẫu và lọc**, **6. Worked lập luận (reasoning / 추론): sensor 0–1 kHz** cho ta quy tắc; **7. Đo và kiểm chứng** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Thất bại (failure / 실패) modes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Đo và kiểm chứng

- Dùng known sine để đo gain/phase theo tần số.
- So sánh spectrum trước/sau filter, không chỉ nhìn thời gian (time / 시간) plot.
- Kiểm tra clipping trước FFT; clipping tạo harmonic giả.
- Ghi mẫu (sample / 표본) tỷ lệ (rate / 비율), cửa sổ (window / 윈도우), bản ghi (record / 레코드) length và calibration khi báo PSD.
- Tách sensor noise, quantization noise và electrical interference bằng controlled đầu vào (input / 입력).

> **Chuyển mạch:** Trong **LTI, Sampling and Filtering — Hệ tuyến tính, lấy mẫu và lọc**, **Thất bại (failure / 실패) modes** tiếp nhận điểm tựa từ **7. Đo và kiểm chứng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cầu nối (bridge / 브리지)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thất bại (failure / 실패) modes

- Dùng FFT bin như frequency resolution mà quên bản ghi (record / 레코드) length/cửa sổ (window / 윈도우) leakage.
- Lọc sau ADC khi alias đã xảy ra.
- Nhầm group delay với phase delay trong tín hiệu (signal / 신호) transient.
- Dùng filter ổn định trên float nhưng unstable sau fixed-point quantization.

> **Chuyển mạch:** Ở chặng này của **LTI, Sampling and Filtering — Hệ tuyến tính, lấy mẫu và lọc**, **Cầu nối (bridge / 브리지)** tiếp nhận điểm tựa từ **Thất bại (failure / 실패) modes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Đi tiếp sang [communication systems](../communication_systems/00_modulation_channel_coding.md) để truyền tín hiệu (signal / 신호) qua channel, hoặc [control systems](../control_systems/00_feedback_stability_pid.md) để đóng vòng phản hồi (feedback / 피드백). Nền Physics là [waves/Fourier](../../physics/02_oscillations_waves/01_waves_fourier_sound.md) và [signals/noise/sampling](../../physics/12_experimental_computational/01_signals_sampling_noise.md).

> **Bàn giao:** Sau **Cầu nối (bridge / 브리지)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
