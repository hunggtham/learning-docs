# Modulation, Channel and Coding — Điều chế, kênh và mã hóa

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Modulation, Channel and Coding — Điều chế, kênh và mã hóa**. Route đi từ baseband/passband và I/Q → link budget → channel noise, fading và interference → coding, rate và reliability → trade-off latency/power, để tín hiệu được nối với điều kiện truyền thực tế.

Communication kỹ thuật (engineering / 엔지니어링) bắt đầu từ ngân sách (budget / 예산): cần truyền bao nhiêu bit, qua khoảng cách nào, với độ trễ (latency / 지연 시간), độ tin cậy (reliability / 신뢰성) và power bao nhiêu. Channel không chỉ làm tín hiệu (signal / 신호) nhỏ đi; nó thêm noise, distortion, fading, interference và bất định (uncertainty / 불확실성) về timing/carrier.

## 1. Baseband và passband

Baseband tín hiệu (signal / 신호) có thể biểu diễn bằng pulse hoặc symbol. Với passband, carrier được điều chế bởi amplitude/phase/frequency. I/Q biểu diễn (representation / 표현) viết tín hiệu (signal / 신호) hẹp băng dưới dạng:

    s(t) = I(t)cos(2πfct) - Q(t)sin(2πfct)

I/Q giúp tách amplitude/phase nhưng yêu cầu mixer, oscillator, ADC/DAC và calibration có sai số.

> **Chuyển mạch:** **1. Baseband và passband** xác định dạng tín hiệu; **2. Link budget** tính suy hao và dự trữ, rồi **3. Noise và SNR** kiểm tra chất lượng nhận.

## 2. Link ngân sách (budget / 예산)

Ở mức hệ thống:

    Prx(dBm) = Ptx(dBm) + Gtx(dBi) + Grx(dBi) - path_loss(dB) - cable_loss(dB)

Link margin là phần còn lại sau khi trừ receiver sensitivity, hiện thực (implementation / 구현) mất mát (loss / 손실) và fading margin. Một link pass ở lab nhưng thất bại (fail / 실패) ngoài trời thường thiếu margin cho obstruction, multipath hoặc antenna orientation.

> **Chuyển mạch:** Từ link budget và SNR, **4. Synchronization** xử lý lệch thời gian/tần số để receiver có thể giải điều chế đúng.

## 3. Noise và SNR

Thermal noise power gần N = kTB. Bandwidth B càng rộng thì noise power càng lớn. Receiver noise figure quy đổi noise thêm vào đầu vào (input / 입력). SNR phải được đo ở điểm tham chiếu rõ ràng; SNR trước detector và sau decoder không cùng nghĩa.

> **Chuyển mạch:** **Synchronization** khôi phục tham chiếu; **5. Coding và reliability** dùng phần dự trữ còn lại để sửa lỗi và đặt giới hạn xác suất sai.

## 4. Synchronization

Receiver cần biết symbol ranh giới (boundary / 경계) và carrier phase/frequency. Clock offset nhỏ tích lũy theo thời gian; carrier offset làm constellation quay. Vì vậy preamble, pilot, timing khôi phục (recovery / 복구) và carrier khôi phục (recovery / 복구) là một phần của giao thức (protocol / 프로토콜), không phải chi tiết hiện thực (implementation / 구현).

> **Chuyển mạch:** Sau coding và reliability, **6. Worked reasoning** cân bằng link margin giữa công suất, băng thông, lỗi và chi phí triển khai.

## 5. Coding và độ tin cậy (reliability / 신뢰성)

Channel coding thêm redundancy để decoder sửa lỗi. BER là lỗi bit vật lý; FER/PER là lỗi frame/packet sau framing. Retransmission có thể giảm lỗi (error / 오류) observable nhưng tăng độ trễ (latency / 지연 시간) và năng lượng (energy / 에너지). Không dùng BER mục tiêu để thay cho application-level delivery guarantee.

> **Chuyển mạch:** Ở chặng này của **Modulation, Channel and Coding — Điều chế, kênh và mã hóa**, **5. Coding và độ tin cậy (reliability / 신뢰성)** cho ta quy tắc; **6. Worked lập luận (reasoning / 추론): chọn link margin** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **7. Đo kiểm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Worked lập luận (reasoning / 추론): chọn link margin

Giả sử Ptx = 0 dBm, Gtx = 2 dBi, Grx = 2 dBi, đường dẫn (path / 경로) + cable mất mát (loss / 손실) = 92 dB, receiver sensitivity = -85 dBm. Prx = -88 dBm, thấp hơn sensitivity 3 dB: link không có margin.

Tăng công suất 3 dB có thể đủ trên giấy, nhưng nếu fading margin cần 10 dB thì vẫn chưa an toàn. Chọn antenna tốt hơn, bandwidth thấp hơn, coding mạnh hơn hoặc giảm khoảng cách đều là các sự đánh đổi (trade-off / 트레이드오프) khác nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Modulation, Channel and Coding — Điều chế, kênh và mã hóa**, **6. Worked lập luận (reasoning / 추론): chọn link margin** cho ta quy tắc; **7. Đo kiểm** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Thất bại (failure / 실패) modes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Đo kiểm

- Dùng calibrated nguồn (source / 소스)/attenuator trước khi đánh giá receiver sensitivity.
- Phân biệt conducted kiểm thử (test / 테스트) với over-the-air kiểm thử (test / 테스트).
- Ghi rõ bandwidth resolution của spectrum analyzer.
- kiểm thử (test / 테스트) frequency offset, clock drift, packet mất mát (loss / 손실) burst và khôi phục (recovery / 복구) thời gian (time / 시간).
- Kiểm tra coexistence/interference, không chỉ link trong channel sạch.

> **Chuyển mạch:** **7. Đo kiểm** tạo bằng chứng cho tín hiệu, SNR và lỗi; **Failure modes** phân loại nguyên nhân, rồi **Cầu nối** chuyển thành hành động sửa.

## Thất bại (failure / 실패) modes

- Nhầm dBm (log power) với dB (ratio).
- Link ngân sách (budget / 예산) không trừ connector/cable/hiện thực (implementation / 구현) mất mát (loss / 손실).
- Receiver “thấy carrier” nhưng không khóa (lock / 잠금) timing nên không decode được.
- Coding/thử lại (retry / 재시도) che giấu channel xấu cho tới khi độ trễ (latency / 지연 시간) vượt SLA.

> **Chuyển mạch:** **Cầu nối** khép bài bằng cách nối failure mode với checklist thiết kế và measurement record cho link kế tiếp.

## Cầu nối (bridge / 브리지)

Đi tiếp sang [hardware–software interfaces](../hardware_software_interfaces/00_register_bus_driver_contracts.md) khi radio/peripheral cần driver và DMA, hoặc sang Khoa học máy tính (computer science / 컴퓨터 과학) networking khi đã qua vật lý (physical / 물리적)/link tầng (layer / 계층) để xử lý packet, routing và congestion.

> **Bàn giao:** Sau **Cầu nối (bridge / 브리지)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
