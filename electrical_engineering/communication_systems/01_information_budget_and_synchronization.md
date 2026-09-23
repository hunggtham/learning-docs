# Information Budget and Synchronization — Dung lượng và đồng bộ

Link budget vật lý chưa đủ để dự đoán throughput. Communication system phải đồng thời thỏa bandwidth, SNR, symbol rate, coding overhead, synchronization cost và latency.

## 1. Nyquist và Shannon

Kênh bandwidth B không nhiễu có giới hạn symbol rate theo Nyquist pulse shaping. Với AWGN channel, capacity lý thuyết có dạng:

    C = B log2(1 + SNR)

Capacity là upper bound dưới assumptions, không phải tốc độ ứng dụng luôn đạt. Roll-off, pilot, guard interval, protocol header và retransmission làm net throughput thấp hơn.

## 2. Constellation và EVM

QPSK, QAM và các constellation khác đổi symbol energy thành bits/symbol. Khoảng cách điểm quyết định noise tolerance. Error vector magnitude (EVM) đo khoảng cách vector giữa điểm nhận và điểm lý tưởng; EVM giúp thấy phase noise, IQ imbalance, compression và multipath.

## 3. Synchronization loop

Timing recovery và carrier recovery thường là control loops. Loop bandwidth rộng bắt nhanh nhưng thu thêm noise; hẹp thì lọc tốt nhưng track oscillator drift chậm. Preamble/pilot tiêu tốn throughput để đổi lấy lock reliability.

## 4. Worked reasoning: throughput thực

Một link 10 Msymbol/s, 16-QAM có 4 bit/symbol, nên raw rate 40 Mbit/s. Nếu coding rate 3/4, protocol overhead 10% và retransmission trung bình 5%, goodput xấp xỉ 40 × 0.75 × 0.9 × 0.95 = 25.65 Mbit/s, chưa trừ inter-frame gap và power-save wake-up.

## Failure modes

- báo raw data rate như application throughput;
- tăng modulation order khi EVM không đủ;
- pilot quá ít làm carrier drift thành burst error;
- FEC sửa được bit nhưng latency/retry vẫn vượt deadline.

## Bridge

Đi tiếp sang [hardware–software interfaces](../hardware_software_interfaces/00_register_bus_driver_contracts.md) cho DMA/driver và Computer Science networking cho queueing, congestion và protocol reliability.
