# Modulation, Channel and Coding — Điều chế, kênh và mã hóa

Communication engineering bắt đầu từ budget: cần truyền bao nhiêu bit, qua khoảng cách nào, với latency, reliability và power bao nhiêu. Channel không chỉ làm signal nhỏ đi; nó thêm noise, distortion, fading, interference và uncertainty về timing/carrier.

## 1. Baseband và passband

Baseband signal có thể biểu diễn bằng pulse hoặc symbol. Với passband, carrier được điều chế bởi amplitude/phase/frequency. I/Q representation viết signal hẹp băng dưới dạng:

    s(t) = I(t)cos(2πfct) - Q(t)sin(2πfct)

I/Q giúp tách amplitude/phase nhưng yêu cầu mixer, oscillator, ADC/DAC và calibration có sai số.

## 2. Link budget

Ở mức hệ thống:

    Prx(dBm) = Ptx(dBm) + Gtx(dBi) + Grx(dBi) - path_loss(dB) - cable_loss(dB)

Link margin là phần còn lại sau khi trừ receiver sensitivity, implementation loss và fading margin. Một link pass ở lab nhưng fail ngoài trời thường thiếu margin cho obstruction, multipath hoặc antenna orientation.

## 3. Noise và SNR

Thermal noise power gần N = kTB. Bandwidth B càng rộng thì noise power càng lớn. Receiver noise figure quy đổi noise thêm vào input. SNR phải được đo ở điểm tham chiếu rõ ràng; SNR trước detector và sau decoder không cùng nghĩa.

## 4. Synchronization

Receiver cần biết symbol boundary và carrier phase/frequency. Clock offset nhỏ tích lũy theo thời gian; carrier offset làm constellation quay. Vì vậy preamble, pilot, timing recovery và carrier recovery là một phần của protocol, không phải chi tiết implementation.

## 5. Coding và reliability

Channel coding thêm redundancy để decoder sửa lỗi. BER là lỗi bit vật lý; FER/PER là lỗi frame/packet sau framing. Retransmission có thể giảm error observable nhưng tăng latency và energy. Không dùng BER mục tiêu để thay cho application-level delivery guarantee.

## 6. Worked reasoning: chọn link margin

Giả sử Ptx = 0 dBm, Gtx = 2 dBi, Grx = 2 dBi, path + cable loss = 92 dB, receiver sensitivity = -85 dBm. Prx = -88 dBm, thấp hơn sensitivity 3 dB: link không có margin.

Tăng công suất 3 dB có thể đủ trên giấy, nhưng nếu fading margin cần 10 dB thì vẫn chưa an toàn. Chọn antenna tốt hơn, bandwidth thấp hơn, coding mạnh hơn hoặc giảm khoảng cách đều là các trade-off khác nhau.

## 7. Đo kiểm

- Dùng calibrated source/attenuator trước khi đánh giá receiver sensitivity.
- Phân biệt conducted test với over-the-air test.
- Ghi rõ bandwidth resolution của spectrum analyzer.
- Test frequency offset, clock drift, packet loss burst và recovery time.
- Kiểm tra coexistence/interference, không chỉ link trong channel sạch.

## Failure modes

- Nhầm dBm (log power) với dB (ratio).
- Link budget không trừ connector/cable/implementation loss.
- Receiver “thấy carrier” nhưng không lock timing nên không decode được.
- Coding/retry che giấu channel xấu cho tới khi latency vượt SLA.

## Bridge

Đi tiếp sang [hardware–software interfaces](../hardware_software_interfaces/00_register_bus_driver_contracts.md) khi radio/peripheral cần driver và DMA, hoặc sang Computer Science networking khi đã qua physical/link layer để xử lý packet, routing và congestion.
