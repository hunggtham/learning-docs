# Dữ liệu (data / 데이터) Converters and Noise ngân sách (budget / 예산) — ADC, DAC và ngân sách sai số

> **Mạch đọc:** Đặt **dữ liệu (data / 데이터) Converters and Noise ngân sách (budget / 예산) — ADC, DAC và ngân sách sai số** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. ADC lỗi (error / 오류) mô hình (model / 모델)** sang **2. SNR, SINAD và động (dynamic / 동적) phạm vi (range / 범위)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

ADC/DAC là ranh giới (boundary / 경계) giữa continuous vật lý (physical / 물리적) tín hiệu (signal / 신호) và discrete computation. Thiết kế tốt phải tách noise, distortion, offset, gain lỗi (error / 오류), quantization, tham chiếu (reference / 참조) lỗi (error / 오류) và timing jitter.

## 1. ADC lỗi (error / 오류) mô hình (model / 모델)

ADC lý tưởng lượng tử hóa đầu vào (input / 입력) theo LSB. ADC thật có offset lỗi (error / 오류), gain lỗi (error / 오류), INL, DNL, missing mã (code / 코드), aperture jitter và tham chiếu (reference / 참조) noise. ENOB đo hiệu dụng cả noise và distortion, không chỉ số bit trên datasheet.

Với full-scale sine, quan hệ ideal SNR xấp xỉ 6.02N + 1.76 dB chỉ áp dụng khi tín hiệu (signal / 신호) dùng gần full quy mô (scale / 규모), quantization là nguồn chi phối và front-end đủ sạch.


> **Chuyển mạch:** Từ **1. ADC lỗi (error / 오류) mô hình (model / 모델)**, ta sang **2. SNR, SINAD và động (dynamic / 동적) phạm vi (range / 범위)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 2. SNR, SINAD và động (dynamic / 동적) phạm vi (range / 범위)

SNR loại harmonic khỏi noise; SINAD gộp tín hiệu (signal / 신호), noise và distortion. Một converter có SNR tốt nhưng distortion xấu vẫn không phù hợp đo lường (measurement / 측정) chính xác. tham chiếu (reference / 참조) noise và supply coupling thường xuất hiện như spur hoặc low-frequency drift.


> **Chuyển mạch:** Từ **2. SNR, SINAD và động (dynamic / 동적) phạm vi (range / 범위)**, ta sang **3. Anti-alias và settling** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 3. Anti-alias và settling

RC trước ADC tạo attenuation nhưng nguồn (source / 소스) impedance phải phù hợp acquisition capacitor. Op-amp buffer cần settle tới fraction của 1 LSB trong acquisition cửa sổ (window / 윈도우). Nếu không, tăng số bit không tạo thêm thông tin (information / 정보).


> **Chuyển mạch:** Từ **3. Anti-alias và settling**, ta sang **4. DAC và actuator** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 4. DAC và actuator

DAC cần monotonicity, glitch năng lượng (energy / 에너지) và settling thời gian (time / 시간). Zero-order hold tạo spectral images; reconstruction filter loại bỏ ảnh ngoài band. Với actuator, mã (code / 코드) đúng vẫn có thể gây step quá lớn nếu slew/tỷ lệ (rate / 비율) limit không được thiết kế.


> **Chuyển mạch:** Từ **4. DAC và actuator**, ta sang **5. Worked lập luận (reasoning / 추론): lỗi (error / 오류) ngân sách (budget / 예산)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 5. Worked lập luận (reasoning / 추론): lỗi (error / 오류) ngân sách (budget / 예산)

Giả sử cần accuracy 1 mV trên phạm vi (range / 범위) 0–3.3 V. ngân sách (budget / 예산) phải phân bổ cho sensor, amplifier offset/drift, resistor ratio, tham chiếu (reference / 참조), ADC INL/noise và calibration residual. Nếu mỗi phần đều “dưới 1 mV”, tổng hệ thống (system / 시스템) chắc chắn vượt 1 mV. Cần RSS cho nguồn độc lập hoặc worst-case cho nguồn có tương quan.


> **Chuyển mạch:** Từ **5. Worked lập luận (reasoning / 추론): lỗi (error / 오류) ngân sách (budget / 예산)**, ta sang **cầu nối (bridge / 브리지)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Đi tiếp sang [signals and systems](../signals_and_systems/00_lti_sampling_filtering.md) cho sampling/filter và [embedded systems](../embedded_systems/00_mcu_runtime_real_time.md) cho DMA, timing và calibration vòng đời (lifecycle / 생명주기).

> **Bàn giao:** Sau **cầu nối (bridge / 브리지)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 device biasing feedback](./00_device_biasing_feedback.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
