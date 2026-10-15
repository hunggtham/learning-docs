# 2. 데이터 전송 방식 및 변조 (Phương thức truyền & Điều chế)

## 학습 목표 (Mục tiêu)
- Nắm vững phân loại phương thức truyền dữ liệu theo hướng truyền thông: Đơn công (**단방향 - Simplex**), Bán song công (**반이중 - Half-Duplex**), và Song công toàn phần (**전이중 - Full-Duplex**).
- Phân biệt sự khác nhau mang tính bản chất giữa truyền thông không đồng bộ (**비동기식 전송 - Asynchronous**) sử dụng Start/Stop bit và truyền thông đồng bộ (**동기식 전송 - Synchronous**) sử dụng khung khối (Frame/Block) và xung nhịp Clock.
- Hiểu các kỹ thuật điều chế số cơ bản (ASK, FSK, PSK, QAM) và mối quan hệ giữa tốc độ Baud và tốc độ Bit (bps).

## 핵심 키워드 (Từ khóa)
- 단방향 통신 (Simplex - TV, 라디오)
- 반이중 통신 (Half-Duplex - 무전기, CSMA/CD)
- 전이중 통신 (Full-Duplex - 전화기, 전송 회선 2개)
- 비동기식 전송 (Asynchronous - Start/Stop Bit, 저속)
- 동기식 전송 (Synchronous - 블록 전송, 클록 동기, 고속)
- 디지털 변조 기법 (ASK, FSK, PSK, QAM)
- 전송 효율 및 오버헤드 (Transmission Efficiency)

## 선행·연결 개념 (Kiến thức liên kết)
- [12-bai-hoc.md](12-bai-hoc.md): Tổng quan truyền thông dữ liệu và 3 yếu tố cơ bản.
- [14-bai-hoc.md](14-bai-hoc.md): Kỹ thuật đa hợp ghép kênh FDM và TDM.
- [15-bai-hoc.md](15-bai-hoc.md): Kiểm soát lỗi FEC, ARQ và các phương thức chuyển mạch.

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh hướng truyền qua ví dụ thực tế trong đề thi:
  - **단방향 (Simplex):** Dòng chảy 1 chiều $\rightarrow$ TV, Đài phát thanh Radio (người xem chỉ nghe, không gửi ngược lại được).
  - **반이중 (Half-Duplex):** Cả 2 bên đều nói được, nhưng **không thể nói cùng lúc** (bên này nói xong phải hô "Over" để nhường kênh cho bên kia) $\rightarrow$ Bộ đàm (무전기 - Walkie-talkie).
  - **전이중 (Full-Duplex):** Cả 2 bên có thể **đồng thời vừa nói vừa nghe cùng một lúc** $\rightarrow$ Điện thoại thoại (전화기).
- Phân biệt đồng bộ:
  - Cứ thấy **"Start Bit và Stop Bit"** $\rightarrow$ Chọn ngay **비동기식 (Asynchronous)**.
  - Cứ thấy **"Truyền theo khối Block / Frame, dùng xung nhịp Clock chung"** $\rightarrow$ Chọn ngay **동기식 (Synchronous)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng đối chiếu 3 phương thức truyền thông theo hướng dòng chảy dữ liệu:**

| Phương thức truyền | Khả năng truyền dẫn | Ví dụ thiết bị thực tế | Đặc điểm kỹ thuật thi cử |
| :--- | :--- | :--- | :--- |
| **단방향 (Simplex)** | Chỉ truyền cố định theo **duy nhất một hướng** từ trạm phát sang trạm thu. | Đài Radio, Truyền hình TV, Cảm biến truyền về trung tâm. | Cấu trúc mạch truyền đơn giản nhất; không có khả năng gửi tín hiệu phản hồi xác nhận (ACK). |
| **반이중 (Half-Duplex)** | Có thể truyền theo cả hai hướng, nhưng **tại một thời điểm chỉ có 1 bên được phát**. | Máy bộ đàm (Walkie-Talkie), Mạng Ethernet bán song công (CSMA/CD). | Phải mất thời gian đảo chiều đường truyền (Turnaround Time) để chuyển đổi giữa phát và thu. |
| **전이중 (Full-Duplex)** | Có thể truyền và nhận dữ liệu **đồng thời cả 2 hướng tại cùng một thời điểm**. | Cuộc gọi điện thoại di động, Mạng máy tính chuyển mạch Switch (Full-Duplex Ethernet). | Cần 2 đường truyền vật lý riêng biệt hoặc dùng kỹ thuật phân tách tần số trên cùng một cáp; hiệu suất tối đa. |

- **2. Bảng so sánh toàn diện: Truyền thông không đồng bộ vs Đồng bộ:**

| Tiêu chuẩn so sánh | 비동기식 전송 (Asynchronous) | 동기식 전송 (Synchronous) |
| :--- | :--- | :--- |
| **Đơn vị truyền** | Từng ký tự đơn lẻ (Character, 5 ~ 8 bit). | Từng khối dữ liệu lớn (Block hoặc Frame hàng nghìn byte). |
| **Cơ chế đồng bộ** | Gắn **1 Start Bit (bit 0)** ở đầu và **1 ~ 2 Stop Bit (bit 1)** ở cuối mỗi ký tự; giữa các ký tự có khoảng nghỉ biến thiên. | Máy phát và máy thu dùng chung **xung nhịp Clock đồng bộ**; mở đầu bằng cờ chuẩn (**SYN / Flag `01111110`**). |
| **Tốc độ truyền** | Tốc độ thấp (thường dưới 2.000 bps); khoảng cách ngắn. | **Tốc độ rất cao** (hàng Mbps đến Gbps); đường truyền cự ly xa. |
| **Hiệu suất & Chi phí** | Hiệu suất thấp do chi phí phụ trội (Overhead) lên tới 20% ~ 30%; thiết bị đơn giản, giá rẻ. | **Hiệu suất đường truyền rất cao** (Overhead nhỏ); thiết bị phần cứng đồng bộ phức tạp, đắt tiền. |

- **3. Các kỹ thuật điều chế số (Digital Modulation):**
  - **ASK (Amplitude Shift Keying):** Thay đổi biên độ sóng mang theo bit 0/1; dễ bị ảnh hưởng bởi nhiễu biên độ.
  - **FSK (Frequency Shift Keying):** Thay đổi tần số sóng mang; chống nhiễu tốt hơn ASK, dùng trong modem tốc độ thấp.
  - **PSK (Phase Shift Keying):** Thay đổi pha của sóng mang ($0^\circ, 180^\circ$ đối với BPSK; $0^\circ, 90^\circ, 180^\circ, 270^\circ$ đối với QPSK).
  - **QAM (Quadrature Amplitude Modulation):** **Kết hợp đồng thời cả biến đổi biên độ và góc pha**, cho phép 1 tín hiệu Baud mang được nhiều bit (ví dụ 16-QAM mang 4 bit/baud, 64-QAM mang 6 bit/baud), đạt hiệu năng truyền thông cao nhất.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Công thức Nyquist và Shannon về dung lượng kênh truyền:**
  - *Định lý Nyquist (Kênh không có nhiễu):* Tốc độ truyền cực đại $C = 2B \log_2 M$ (bps), trong đó $B$ là băng thông (Hz), $M$ là số mức tín hiệu.
  - *Định lý Shannon (Kênh có nhiễu trắng Gaussian):* Dung lượng tối đa $C = B \log_2 (1 + \frac{S}{N})$ (bps), trong đó $\frac{S}{N}$ là tỷ số tín hiệu trên nhiễu (Signal-to-Noise Ratio).

### 복습 체크리스트
- [ ] Phân biệt được: Simplex (1 hướng), Half-Duplex (2 hướng luân phiên), Full-Duplex (2 hướng đồng thời).
- [ ] Nhớ thiết bị đại diện: Bộ đàm là Half-Duplex, điện thoại là Full-Duplex, TV là Simplex.
- [ ] Phân biệt được: Truyền không đồng bộ dùng Start/Stop bit (chậm), truyền đồng bộ dùng xung clock (nhanh).
- [ ] Nhớ kỹ thuật QAM kết hợp đồng thời cả biến đổi biên độ (Amplitude) và pha (Phase).
