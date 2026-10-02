# Thông tin (information / 정보) ngân sách (budget / 예산) and Synchronization — Dung lượng và đồng bộ

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Thông tin (information / 정보) ngân sách (budget / 예산) and Synchronization — Dung lượng và đồng bộ**. Route đi từ Nyquist/Shannon → constellation, EVM và link budget → synchronization, coding và overhead → throughput, latency và reliability → giới hạn đo, để thông lượng được nối với điều kiện vật lý của đường truyền.

Link ngân sách (budget / 예산) vật lý chưa đủ để dự đoán thông lượng (throughput / 처리량). Communication hệ thống (system / 시스템) phải đồng thời thỏa bandwidth, SNR, symbol tỷ lệ (rate / 비율), coding overhead, synchronization chi phí (cost / 비용) và độ trễ (latency / 지연 시간).

## 1. Nyquist và Shannon

Kênh bandwidth B không nhiễu có giới hạn symbol tỷ lệ (rate / 비율) theo Nyquist pulse shaping. Với AWGN channel, sức chứa (capacity / 용량) lý thuyết có dạng:

    C = B log2(1 + SNR)

Sức chứa (capacity / 용량) là upper bound dưới các giả định (assumptions / 가정들), không phải tốc độ ứng dụng luôn đạt. Roll-off, pilot, guard interval, giao thức (protocol / 프로토콜) header và retransmission làm net thông lượng (throughput / 처리량) thấp hơn.

> **Chuyển mạch:** Trong **Thông tin (information / 정보) ngân sách (budget / 예산) and Synchronization — Dung lượng và đồng bộ**, **2. Constellation và EVM** tiếp nhận điểm tựa từ **1. Nyquist và Shannon** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Synchronization vòng lặp (loop / 루프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Constellation và EVM

QPSK, QAM và các constellation khác đổi symbol năng lượng (energy / 에너지) thành bits/symbol. Khoảng cách điểm quyết định noise tolerance. lỗi (error / 오류) véc-tơ (vector / 벡터) magnitude (EVM) đo khoảng cách véc-tơ (vector / 벡터) giữa điểm nhận và điểm lý tưởng; EVM giúp thấy phase noise, IQ imbalance, compression và multipath.

> **Chuyển mạch:** Ở chặng này của **Thông tin (information / 정보) ngân sách (budget / 예산) and Synchronization — Dung lượng và đồng bộ**, **3. Synchronization vòng lặp (loop / 루프)** tiếp nhận điểm tựa từ **2. Constellation và EVM** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Worked lập luận (reasoning / 추론): thông lượng (throughput / 처리량) thực** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Synchronization vòng lặp (loop / 루프)

Timing khôi phục (recovery / 복구) và carrier khôi phục (recovery / 복구) thường là điều khiển (control / 제어) loops. vòng lặp (loop / 루프) bandwidth rộng bắt nhanh nhưng thu thêm noise; hẹp thì lọc tốt nhưng nhánh học (track / 트랙) oscillator drift chậm. Preamble/pilot tiêu tốn thông lượng (throughput / 처리량) để đổi lấy khóa (lock / 잠금) độ tin cậy (reliability / 신뢰성).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thông tin (information / 정보) ngân sách (budget / 예산) and Synchronization — Dung lượng và đồng bộ**, **3. Synchronization vòng lặp (loop / 루프)** cho ta quy tắc; **4. Worked lập luận (reasoning / 추론): thông lượng (throughput / 처리량) thực** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Thất bại (failure / 실패) modes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Worked lập luận (reasoning / 추론): thông lượng (throughput / 처리량) thực

Một link 10 Msymbol/s, 16-QAM có 4 bit/symbol, nên raw tỷ lệ (rate / 비율) 40 Mbit/s. Nếu coding tỷ lệ (rate / 비율) 3/4, giao thức (protocol / 프로토콜) overhead 10% và retransmission trung bình 5%, goodput xấp xỉ 40 × 0.75 × 0.9 × 0.95 = 25.65 Mbit/s, chưa trừ inter-frame gap và power-save wake-up.

> **Chuyển mạch:** Trong **Thông tin (information / 정보) ngân sách (budget / 예산) and Synchronization — Dung lượng và đồng bộ**, **4. Worked lập luận (reasoning / 추론): thông lượng (throughput / 처리량) thực** cho ta quy tắc; **Thất bại (failure / 실패) modes** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Cầu nối (bridge / 브리지)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thất bại (failure / 실패) modes

- báo raw dữ liệu (data / 데이터) tỷ lệ (rate / 비율) như ứng dụng (application / 애플리케이션) thông lượng (throughput / 처리량);
- tăng modulation thứ tự (order / 순서) khi EVM không đủ;
- pilot quá ít làm carrier drift thành burst lỗi (error / 오류);
- FEC sửa được bit nhưng độ trễ (latency / 지연 시간)/thử lại (retry / 재시도) vẫn vượt deadline.

> **Chuyển mạch:** Ở chặng này của **Thông tin (information / 정보) ngân sách (budget / 예산) and Synchronization — Dung lượng và đồng bộ**, **Cầu nối (bridge / 브리지)** tiếp nhận điểm tựa từ **Thất bại (failure / 실패) modes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Đi tiếp sang [hardware–software interfaces](../hardware_software_interfaces/00_register_bus_driver_contracts.md) cho DMA/driver và Khoa học máy tính (computer science / 컴퓨터 과학) networking cho queueing, congestion và giao thức (protocol / 프로토콜) độ tin cậy (reliability / 신뢰성).

> **Bàn giao:** Sau **Cầu nối (bridge / 브리지)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
