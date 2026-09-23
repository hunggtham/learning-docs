# Data Converters and Noise Budget — ADC, DAC và ngân sách sai số

ADC/DAC là boundary giữa continuous physical signal và discrete computation. Thiết kế tốt phải tách noise, distortion, offset, gain error, quantization, reference error và timing jitter.

## 1. ADC error model

ADC lý tưởng lượng tử hóa input theo LSB. ADC thật có offset error, gain error, INL, DNL, missing code, aperture jitter và reference noise. ENOB đo hiệu dụng cả noise và distortion, không chỉ số bit trên datasheet.

Với full-scale sine, quan hệ ideal SNR xấp xỉ 6.02N + 1.76 dB chỉ áp dụng khi signal dùng gần full scale, quantization là nguồn chi phối và front-end đủ sạch.

## 2. SNR, SINAD và dynamic range

SNR loại harmonic khỏi noise; SINAD gộp signal, noise và distortion. Một converter có SNR tốt nhưng distortion xấu vẫn không phù hợp measurement chính xác. Reference noise và supply coupling thường xuất hiện như spur hoặc low-frequency drift.

## 3. Anti-alias và settling

RC trước ADC tạo attenuation nhưng source impedance phải phù hợp acquisition capacitor. Op-amp buffer cần settle tới fraction của 1 LSB trong acquisition window. Nếu không, tăng số bit không tạo thêm information.

## 4. DAC và actuator

DAC cần monotonicity, glitch energy và settling time. Zero-order hold tạo spectral images; reconstruction filter loại bỏ ảnh ngoài band. Với actuator, code đúng vẫn có thể gây step quá lớn nếu slew/rate limit không được thiết kế.

## 5. Worked reasoning: error budget

Giả sử cần accuracy 1 mV trên range 0–3.3 V. Budget phải phân bổ cho sensor, amplifier offset/drift, resistor ratio, reference, ADC INL/noise và calibration residual. Nếu mỗi phần đều “dưới 1 mV”, tổng system chắc chắn vượt 1 mV. Cần RSS cho nguồn độc lập hoặc worst-case cho nguồn có tương quan.

## Bridge

Đi tiếp sang [signals and systems](../signals_and_systems/00_lti_sampling_filtering.md) cho sampling/filter và [embedded systems](../embedded_systems/00_mcu_runtime_real_time.md) cho DMA, timing và calibration lifecycle.
