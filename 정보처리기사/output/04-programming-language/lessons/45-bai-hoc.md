# 088. 인터넷 구성과 네트워크 - TCP vs UDP & 흐름/오류 제어

## 학습 목표 (Mục tiêu)
- Phân tích sâu sắc sự khác biệt về cơ chế và mục đích sử dụng giữa hai giao thức tầng giao vận cốt lõi: Giao thức điều khiển truyền vận TCP (hướng kết nối, tin cậy tuyệt đối) và Giao thức dữ liệu người dùng UDP (không kết nối, tốc độ cao).
- Nắm vững các kỹ thuật điều khiển luồng dữ liệu (흐름 제어 - Flow Control): Phương pháp Dừng và Chờ (Stop-and-Wait) và Phương pháp Cửa sổ trượt (슬라이딩 윈도우 - Sliding Window).
- Nắm vững các cơ chế điều khiển lỗi tự động gửi lại (오류 제어 - ARQ): Go-Back-N ARQ (gửi lại từ gói lỗi trở đi) và Selective Repeat ARQ (chỉ gửi lại duy nhất gói bị lỗi).
- Hiểu quy trình thiết lập kết nối 3 bước (3-Way Handshake) và ngắt kết nối 4 bước (4-Way Handshake) của TCP.

## 핵심 키워드 (Từ khóa)
- TCP vs UDP (Transmission Control Protocol vs User Datagram Protocol)
- 연결 지향형 vs 비연결형 (Connection-oriented vs Connectionless)
- 3-Way Handshake (SYN, SYN+ACK, ACK)
- 흐름 제어 (Flow Control / 슬라이딩 윈도우 Sliding Window)
- 오류 제어 (Error Control / ARQ - Automatic Repeat reQuest)
- Go-Back-N ARQ vs Selective Repeat ARQ
- 혼잡 제어 (Congestion Control / Slow Start)

## 선행·연결 개념 (Kiến thức liên kết)
- [44-bai-hoc.md](44-bai-hoc.md): Mô hình tham chiếu OSI 7 tầng và đơn vị PDU.
- [46-bai-hoc.md](46-bai-hoc.md): Các giao thức chi tiết ở từng tầng mạng.
- [49-bai-hoc.md](49-bai-hoc.md): Cấu trúc địa chỉ IP và kỹ thuật chia mạng con (Subnetting).

## 읽는 방법 (Cách đọc)
- Phân biệt hai trường phái truyền thông tầng Transport:
  - **TCP (Cẩn thận, tin cậy cao):** Trước khi gửi dữ liệu phải bắt tay 3 bước (3-Way Handshake). Mỗi gói tin gửi đi phải có xác nhận nhận tin (ACK). Nếu bên nhận xử lý không kịp, bên nhận yêu cầu thu hẹp cửa sổ (Sliding Window); nếu mất gói thì gửi lại (ARQ) $\rightarrow$ Dùng cho Web (HTTP), Email (SMTP), Truyền tệp (FTP).
  - **UDP (Nhanh, không bảo đảm):** Cứ có dữ liệu là bắn đi liên tục không cần bắt tay, không cần phản hồi ACK, mất gói tin cũng không thèm gửi lại $\rightarrow$ Tốc độ tối đa, độ trễ cực thấp $\rightarrow$ Dùng cho Truyền hình trực tiếp (Streaming), Cuộc gọi Video (VoIP), Game trực tuyến nhiều người chơi, Truy vấn DNS.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh chi tiết: TCP vs UDP:**

| Tiêu chuẩn so sánh | TCP (Transmission Control Protocol) | UDP (User Datagram Protocol) |
| :--- | :--- | :--- |
| **Loại hình kết nối** | **연결 지향형 (Connection-oriented)**; thiết lập phiên trước | **비연결형 (Connectionless)**; gửi trực tiếp không cần kết nối |
| **Độ tin cậy truyền dẫn** | **Rất cao (신뢰성 보장)**; kiểm soát mất gói, đúng thứ tự | **Thấp (신뢰성 미보장)**; có thể mất gói hoặc lệch thứ tự |
| **Tốc độ truyền dữ liệu** | Chậm hơn, do có tiêu đề Header lớn (20-60 Bytes) và kiểm tra | **Rất nhanh**, tiêu đề Header siêu nhẹ (cố định **8 Bytes**) |
| **Cơ chế kiểm soát** | Hỗ trợ đầy đủ: **Điều khiển luồng, Điều khiển lỗi, Điều khiển tắc nghẽn** | **Không hỗ trợ** điều khiển luồng hay tắc nghẽn |
| **Hình thức truyền** | Điểm - Điểm (Unicast 1:1) | Hỗ trợ cả 1:1 (Unicast), 1:N (Multicast), 1:All (Broadcast) |
| **Giao thức ứng dụng** | **HTTP, HTTPS, FTP, SMTP, SSH, Telnet** | **DNS, SNMP, DHCP, TFTP, VoIP, IPTV Streaming** |

- **Bảng so sánh các kỹ thuật kiểm soát lỗi ARQ:**

| Thuật toán ARQ | Cơ chế hoạt động khi phát hiện gói tin bị lỗi | Ưu điểm & Nhược điểm kỹ thuật |
| :--- | :--- | :--- |
| **Stop-and-Wait ARQ** | Gửi từng gói tin một, đứng chờ nhận được `ACK` mới gửi gói tiếp theo | Rất đơn giản; lãng phí băng thông kênh truyền cực lớn |
| **Go-Back-N ARQ** | Cho phép gửi liên tục một cửa sổ $N$ gói tin; nếu gói số $k$ bị lỗi, **gửi lại TOÀN BỘ từ gói $k$ đến hết cửa sổ** | Bộ đệm bên nhận rất đơn giản (không cần xếp thứ tự); tốn băng thông gửi lại các gói đã thành công |
| **Selective Repeat ARQ** | Bên nhận lưu trữ các gói sau vào bộ đệm; **CHỈ YÊU CẦU GỬI LẠI ĐÚNG GÓI SỐ $k$ BỊ LỖI** | Tiết kiệm tối đa băng thông đường truyền; đòi hỏi bộ đệm bên nhận phức tạp để lắp ghép lại đúng thứ tự |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Quy trình bắt tay 3 bước của TCP (3-Way Handshake):**
  1. **Bước 1 (Client $\rightarrow$ Server):** Client gửi gói tin có cờ `SYN` (kèm số thứ tự khởi tạo Sequence Number $= x$).
  2. **Bước 2 (Server $\rightarrow$ Client):** Server phản hồi gói tin có cả cờ `SYN` và `ACK` (với `ACK = x + 1` và số thứ tự của Server $= y$).
  3. **Bước 3 (Client $\rightarrow$ Server):** Client gửi gói tin xác nhận `ACK` (với `ACK = y + 1`). Kết nối chính thức được thiết lập!

### 복습 체크리스트
- [ ] Phân biệt được TCP (hướng kết nối, tin cậy, chậm) và UDP (không kết nối, không bảo đảm, nhanh).
- [ ] Nhớ kích thước Header của UDP cố định là 8 Bytes (nhẹ hơn nhiều so với TCP 20-60 Bytes).
- [ ] Phân biệt được Go-Back-N (gửi lại từ gói lỗi trở đi) và Selective Repeat (chỉ gửi lại đúng gói lỗi).
- [ ] Nhớ 3 bước Handshake của TCP: SYN $\rightarrow$ SYN+ACK $\rightarrow$ ACK.
