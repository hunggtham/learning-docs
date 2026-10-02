# Dữ liệu (data / 데이터) Converters and Noise ngân sách (budget / 예산) — ADC, DAC và ngân sách sai số

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Dữ liệu (data / 데이터) Converters and Noise ngân sách (budget / 예산) — ADC, DAC và ngân sách sai số**. Route đi từ ADC/DAC error model → SNR, SINAD và dynamic range → quantization, reference, jitter và distortion → noise budget, calibration và measurement → chọn converter theo hệ thống.

ADC/DAC là ranh giới (boundary / 경계) giữa continuous vật lý (physical / 물리적) tín hiệu (signal / 신호) và discrete computation. Thiết kế tốt phải tách noise, distortion, offset, gain lỗi (error / 오류), quantization, tham chiếu (reference / 참조) lỗi (error / 오류) và timing jitter.

## 1. ADC lỗi (error / 오류) mô hình (model / 모델)

ADC lý tưởng lượng tử hóa đầu vào (input / 입력) theo LSB. ADC thật có offset lỗi (error / 오류), gain lỗi (error / 오류), INL, DNL, missing mã (code / 코드), aperture jitter và tham chiếu (reference / 참조) noise. ENOB đo hiệu dụng cả noise và distortion, không chỉ số bit trên datasheet.

Với full-scale sine, quan hệ ideal SNR xấp xỉ 6.02N + 1.76 dB chỉ áp dụng khi tín hiệu (signal / 신호) dùng gần full quy mô (scale / 규모), quantization là nguồn chi phối và front-end đủ sạch.

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) Converters and Noise ngân sách (budget / 예산) — ADC, DAC và ngân sách sai số**, **2. SNR, SINAD và động (dynamic / 동적) phạm vi (range / 범위)** tiếp nhận điểm tựa từ **1. ADC lỗi (error / 오류) mô hình (model / 모델)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Anti-alias và settling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. SNR, SINAD và động (dynamic / 동적) phạm vi (range / 범위)

SNR loại harmonic khỏi noise; SINAD gộp tín hiệu (signal / 신호), noise và distortion. Một converter có SNR tốt nhưng distortion xấu vẫn không phù hợp đo lường (measurement / 측정) chính xác. tham chiếu (reference / 참조) noise và supply coupling thường xuất hiện như spur hoặc low-frequency drift.

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) Converters and Noise ngân sách (budget / 예산) — ADC, DAC và ngân sách sai số**, **3. Anti-alias và settling** tiếp nhận điểm tựa từ **2. SNR, SINAD và động (dynamic / 동적) phạm vi (range / 범위)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. DAC và actuator** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Anti-alias và settling

RC trước ADC tạo attenuation nhưng nguồn (source / 소스) impedance phải phù hợp acquisition capacitor. Op-amp buffer cần settle tới fraction của 1 LSB trong acquisition cửa sổ (window / 윈도우). Nếu không, tăng số bit không tạo thêm thông tin (information / 정보).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Dữ liệu (data / 데이터) Converters and Noise ngân sách (budget / 예산) — ADC, DAC và ngân sách sai số**, **4. DAC và actuator** tiếp nhận điểm tựa từ **3. Anti-alias và settling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Worked lập luận (reasoning / 추론): lỗi (error / 오류) ngân sách (budget / 예산)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. DAC và actuator

DAC cần monotonicity, glitch năng lượng (energy / 에너지) và settling thời gian (time / 시간). Zero-order hold tạo spectral images; reconstruction filter loại bỏ ảnh ngoài band. Với actuator, mã (code / 코드) đúng vẫn có thể gây step quá lớn nếu slew/tỷ lệ (rate / 비율) limit không được thiết kế.

> **Chuyển mạch:** Trong **Dữ liệu (data / 데이터) Converters and Noise ngân sách (budget / 예산) — ADC, DAC và ngân sách sai số**, **4. DAC và actuator** cho ta quy tắc; **5. Worked lập luận (reasoning / 추론): lỗi (error / 오류) ngân sách (budget / 예산)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Cầu nối (bridge / 브리지)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Worked lập luận (reasoning / 추론): lỗi (error / 오류) ngân sách (budget / 예산)

Giả sử cần accuracy 1 mV trên phạm vi (range / 범위) 0–3.3 V. ngân sách (budget / 예산) phải phân bổ cho sensor, amplifier offset/drift, resistor ratio, tham chiếu (reference / 참조), ADC INL/noise và calibration residual. Nếu mỗi phần đều “dưới 1 mV”, tổng hệ thống (system / 시스템) chắc chắn vượt 1 mV. Cần RSS cho nguồn độc lập hoặc worst-case cho nguồn có tương quan.

> **Chuyển mạch:** Ở chặng này của **Dữ liệu (data / 데이터) Converters and Noise ngân sách (budget / 예산) — ADC, DAC và ngân sách sai số**, **5. Worked lập luận (reasoning / 추론): lỗi (error / 오류) ngân sách (budget / 예산)** cho ta quy tắc; **Cầu nối (bridge / 브리지)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Đi tiếp sang [signals and systems](../signals_and_systems/00_lti_sampling_filtering.md) cho sampling/filter và [embedded systems](../embedded_systems/00_mcu_runtime_real_time.md) cho DMA, timing và calibration vòng đời (lifecycle / 생명주기).

> **Bàn giao:** Sau **Cầu nối (bridge / 브리지)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
