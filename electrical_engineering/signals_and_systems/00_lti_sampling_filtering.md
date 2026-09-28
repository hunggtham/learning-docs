# LTI, Sampling and Filtering — Hệ tuyến tính, lấy mẫu và lọc

> **Mạch đọc:** Đặt **LTI, Sampling and Filtering — Hệ tuyến tính, lấy mẫu và lọc** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. LTI hệ thống (system / 시스템)** sang **2. Poles, zeros và stability**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Signals and các hệ thống (systems / 시스템들) tạo một lớp trừu tượng (abstraction / 추상화) chung cho sensor, audio, điều khiển (control / 제어) và communication. Ta quan tâm tín hiệu (signal / 신호) mang năng lượng/thông tin thế nào và hệ thống (system / 시스템) biến đổi nó ra sao dưới giới hạn bandwidth, noise và sampling.

## 1. LTI hệ thống (system / 시스템)

Hệ thống (system / 시스템) tuyến tính (linear / 선형) và time-invariant được đặc trưng bởi impulse phản hồi (response / 응답) h. đầu ra (output / 출력) là convolution:

    y(t) = x(t) * h(t)

Trong frequency lĩnh vực (domain / 도메인):

    Y(f) = X(f)H(f)

H(f) có magnitude và phase. Hai hệ thống (system / 시스템) có cùng gain magnitude nhưng phase khác nhau có thể tạo waveform transient rất khác.


> **Chuyển mạch:** Từ **1. LTI hệ thống (system / 시스템)**, ta sang **2. Poles, zeros và stability** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 2. Poles, zeros và stability

Với transfer hàm (function / 함수) H(s) = N(s) / D(s), pole quyết định chế độ (mode / 모드) tự nhiên. Continuous-time hệ thống (system / 시스템) BIBO stable khi poles ở left half-plane trong các điều kiện chuẩn. Discrete-time hệ thống (system / 시스템) stable khi poles nằm trong đơn vị (unit / 단위) circle.

Pole gần ranh giới (boundary / 경계) tạo phản hồi (response / 응답) chậm, ringing hoặc nhạy với parameter variation. Đây là cầu nối (bridge / 브리지) trực tiếp sang điều khiển (control / 제어) các hệ thống (systems / 시스템들).


> **Chuyển mạch:** Từ **2. Poles, zeros và stability**, ta sang **3. Sampling và aliasing** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 3. Sampling và aliasing

Sampling tín hiệu (signal / 신호) tại fs tạo bản sao phổ cách nhau fs. Nếu tín hiệu (signal / 신호) có thành phần trên Nyquist frequency fs/2, các bản sao chồng lên nhau và alias không thể khôi phục bằng digital filter sau đó.

Quy trình đúng:

    analog anti-alias filter → mẫu (sample / 표본)/hold → ADC → digital processing

Tăng mẫu (sample / 표본) tỷ lệ (rate / 비율) không sửa được front-end đã để alias đi vào; nó chỉ nới vùng chuyển tiếp (transition / 전이) của filter.


> **Chuyển mạch:** Từ **3. Sampling và aliasing**, ta sang **4. Quantization và SNR** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 4. Quantization và SNR

ADC N bit với full-scale phạm vi (range / 범위) VFS có bước lượng tử xấp xỉ Δ = VFS / 2^N. Quantization lỗi (error / 오류) không luôn là white noise; nó phụ thuộc tín hiệu (signal / 신호) và dither. Với ideal ADC full-scale sine, SNR lý tưởng gần 6.02N + 1.76 dB.

ENOB thực tế giảm bởi thermal noise, tham chiếu (reference / 참조) noise, INL/DNL, clock jitter và distortion.


> **Chuyển mạch:** Từ **4. Quantization và SNR**, ta sang **5. Filter thiết kế (design / 설계)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 5. Filter thiết kế (design / 설계)

Filter là sự đánh đổi (trade-off / 트레이드오프) giữa passband ripple, stopband attenuation, chuyển tiếp (transition / 전이) width, phase và computational chi phí (cost / 비용).

- FIR thường dễ có tuyến tính (linear / 선형) phase và ổn định, nhưng cần nhiều taps.
- IIR đạt chuyển tiếp (transition / 전이) hẹp với thứ tự (order / 순서) thấp, nhưng phase nonlinear và nhạy coefficient quantization.
- Analog filter xử lý alias trước ADC; digital filter không thay thế nó.


> **Chuyển mạch:** Từ **5. Filter thiết kế (design / 설계)**, ta sang **6. Worked lập luận (reasoning / 추론): sensor 0–1 kHz** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 6. Worked lập luận (reasoning / 추론): sensor 0–1 kHz

Nếu tín hiệu (signal / 신호) hữu ích tới 1 kHz, có interference 8 kHz, chọn fs = 10 kS/s là nguy hiểm vì Nyquist chỉ 5 kHz và anti-alias chuyển tiếp (transition / 전이) quá hẹp. Chọn fs = 20 kS/s hoặc cao hơn, thiết kế analog low-pass với stopband đủ attenuation trước 10 kHz, rồi digital filter sau ADC.

Nếu clock jitter σt lớn, tín hiệu (signal / 신호) tần số cao chịu noise xấp xỉ tăng theo 2πfσt; mẫu (sample / 표본) tỷ lệ (rate / 비율) cao không tự động làm clock tốt hơn.


> **Chuyển mạch:** Từ **6. Worked lập luận (reasoning / 추론): sensor 0–1 kHz**, ta sang **7. Đo và kiểm chứng** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 7. Đo và kiểm chứng

- Dùng known sine để đo gain/phase theo tần số.
- So sánh spectrum trước/sau filter, không chỉ nhìn thời gian (time / 시간) plot.
- Kiểm tra clipping trước FFT; clipping tạo harmonic giả.
- Ghi mẫu (sample / 표본) tỷ lệ (rate / 비율), cửa sổ (window / 윈도우), bản ghi (record / 레코드) length và calibration khi báo PSD.
- Tách sensor noise, quantization noise và electrical interference bằng controlled đầu vào (input / 입력).


> **Chuyển mạch:** Từ **7. Đo và kiểm chứng**, ta sang **thất bại (failure / 실패) modes** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Thất bại (failure / 실패) modes

- Dùng FFT bin như frequency resolution mà quên bản ghi (record / 레코드) length/cửa sổ (window / 윈도우) leakage.
- Lọc sau ADC khi alias đã xảy ra.
- Nhầm group delay với phase delay trong tín hiệu (signal / 신호) transient.
- Dùng filter ổn định trên float nhưng unstable sau fixed-point quantization.


> **Chuyển mạch:** Từ **thất bại (failure / 실패) modes**, ta sang **cầu nối (bridge / 브리지)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Đi tiếp sang [communication systems](../communication_systems/00_modulation_channel_coding.md) để truyền tín hiệu (signal / 신호) qua channel, hoặc [control systems](../control_systems/00_feedback_stability_pid.md) để đóng vòng phản hồi (feedback / 피드백). Nền Physics là [waves/Fourier](../../physics/02_oscillations_waves/01_waves_fourier_sound.md) và [signals/noise/sampling](../../physics/12_experimental_computational/01_signals_sampling_noise.md).

> **Bàn giao:** Sau **cầu nối (bridge / 브리지)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 transforms and estimation](./01_transforms_and_estimation.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
