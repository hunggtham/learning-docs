# Thông tin (information / 정보) ngân sách (budget / 예산) and Synchronization — Dung lượng và đồng bộ

> **Mạch đọc:** Đặt **thông tin (information / 정보) ngân sách (budget / 예산) and Synchronization — Dung lượng và đồng bộ** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Nyquist và Shannon** sang **2. Constellation và EVM**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Link ngân sách (budget / 예산) vật lý chưa đủ để dự đoán thông lượng (throughput / 처리량). Communication hệ thống (system / 시스템) phải đồng thời thỏa bandwidth, SNR, symbol tỷ lệ (rate / 비율), coding overhead, synchronization chi phí (cost / 비용) và độ trễ (latency / 지연 시간).

## 1. Nyquist và Shannon

Kênh bandwidth B không nhiễu có giới hạn symbol tỷ lệ (rate / 비율) theo Nyquist pulse shaping. Với AWGN channel, sức chứa (capacity / 용량) lý thuyết có dạng:

    C = B log2(1 + SNR)

Sức chứa (capacity / 용량) là upper bound dưới các giả định (assumptions / 가정들), không phải tốc độ ứng dụng luôn đạt. Roll-off, pilot, guard interval, giao thức (protocol / 프로토콜) header và retransmission làm net thông lượng (throughput / 처리량) thấp hơn.


> **Chuyển mạch:** Từ **1. Nyquist và Shannon**, ta sang **2. Constellation và EVM** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 2. Constellation và EVM

QPSK, QAM và các constellation khác đổi symbol năng lượng (energy / 에너지) thành bits/symbol. Khoảng cách điểm quyết định noise tolerance. lỗi (error / 오류) véc-tơ (vector / 벡터) magnitude (EVM) đo khoảng cách véc-tơ (vector / 벡터) giữa điểm nhận và điểm lý tưởng; EVM giúp thấy phase noise, IQ imbalance, compression và multipath.


> **Chuyển mạch:** Từ **2. Constellation và EVM**, ta sang **3. Synchronization vòng lặp (loop / 루프)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 3. Synchronization vòng lặp (loop / 루프)

Timing khôi phục (recovery / 복구) và carrier khôi phục (recovery / 복구) thường là điều khiển (control / 제어) loops. vòng lặp (loop / 루프) bandwidth rộng bắt nhanh nhưng thu thêm noise; hẹp thì lọc tốt nhưng nhánh học (track / 트랙) oscillator drift chậm. Preamble/pilot tiêu tốn thông lượng (throughput / 처리량) để đổi lấy khóa (lock / 잠금) độ tin cậy (reliability / 신뢰성).


> **Chuyển mạch:** Từ **3. Synchronization vòng lặp (loop / 루프)**, ta sang **4. Worked lập luận (reasoning / 추론): thông lượng (throughput / 처리량) thực** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 4. Worked lập luận (reasoning / 추론): thông lượng (throughput / 처리량) thực

Một link 10 Msymbol/s, 16-QAM có 4 bit/symbol, nên raw tỷ lệ (rate / 비율) 40 Mbit/s. Nếu coding tỷ lệ (rate / 비율) 3/4, giao thức (protocol / 프로토콜) overhead 10% và retransmission trung bình 5%, goodput xấp xỉ 40 × 0.75 × 0.9 × 0.95 = 25.65 Mbit/s, chưa trừ inter-frame gap và power-save wake-up.


> **Chuyển mạch:** Từ **4. Worked lập luận (reasoning / 추론): thông lượng (throughput / 처리량) thực**, ta sang **thất bại (failure / 실패) modes** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Thất bại (failure / 실패) modes
Phần “Thất bại (failure / 실패) modes” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- báo raw dữ liệu (data / 데이터) tỷ lệ (rate / 비율) như ứng dụng (application / 애플리케이션) thông lượng (throughput / 처리량);
- tăng modulation thứ tự (order / 순서) khi EVM không đủ;
- pilot quá ít làm carrier drift thành burst lỗi (error / 오류);
- FEC sửa được bit nhưng độ trễ (latency / 지연 시간)/thử lại (retry / 재시도) vẫn vượt deadline.


> **Chuyển mạch:** Từ **thất bại (failure / 실패) modes**, ta sang **cầu nối (bridge / 브리지)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Đi tiếp sang [hardware–software interfaces](../hardware_software_interfaces/00_register_bus_driver_contracts.md) cho DMA/driver và Khoa học máy tính (computer science / 컴퓨터 과학) networking cho queueing, congestion và giao thức (protocol / 프로토콜) độ tin cậy (reliability / 신뢰성).

> **Bàn giao:** Sau **cầu nối (bridge / 브리지)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 modulation channel coding](./00_modulation_channel_coding.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
