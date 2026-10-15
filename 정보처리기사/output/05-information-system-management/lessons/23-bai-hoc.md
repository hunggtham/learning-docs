# 계층별 주요 프로토콜 (Major Protocols by Layer)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, chức năng kỹ thuật, tầng hoạt động và số hiệu cổng mặc định (**Port Numbers**) của các giao thức mạng trụ cột trong mô hình TCP/IP.
- Phân biệt chi tiết sự khác biệt mang tính bản chất giữa hai giao thức tầng giao vận: **TCP** (hướng kết nối, tin cậy, 3-Way Handshake, kiểm soát luồng) và **UDP** (phi kết nối, tốc độ cao, tiêu đề nhỏ 8 Byte, phù hợp truyền phát thời gian thực).
- Phân biệt các giao thức tầng mạng/Internet: Giao thức thông báo điều khiển **ICMP**, Giao thức quản lý nhóm đa hướng **IGMP**, Giao thức phân giải địa chỉ **ARP** (IP sang MAC), và **RARP** (MAC sang IP).

## 핵심 키워드 (Từ khóa)
- 프로토콜 계층화 (TCP/IP Protocol Suite)
- 응용 계층 포트 (HTTP 80, HTTPS 443, FTP 20/21, SSH 22, Telnet 23, SMTP 25, DNS 53)
- 전송 계층 (TCP vs UDP 특성 비교)
- 인터넷 계층 (IP, ICMP, IGMP)
- 주소 변환 프로토콜 (ARP: IP -> MAC vs RARP: MAC -> IP)
- 3-Way Handshake & 슬라이딩 윈도우 (Sliding Window Flow Control)

## 선행·연결 개념 (Kiến thức liên kết)
- [22-bai-hoc.md](22-bai-hoc.md): Các công nghệ bảo mật mạng (VPN, SSH, Firewall, DMZ).
- [24-bai-hoc.md](24-bai-hoc.md): Công nghệ lõi cơ sở dữ liệu (Recovery & Concurrency Control).
- [46-bai-hoc.md](46-bai-hoc.md): Chi tiết giao thức TCP/UDP và thuật toán bắt tay 3 bước.

## 읽는 방법 (Cách đọc)
- Bản đồ tra cứu nhanh giao thức và số hiệu Port bắt buộc phải thuộc:
  - **FTP:** Cổng 20 (Dữ liệu - Data) và Cổng 21 (Lệnh điều khiển - Control).
  - **SSH:** Cổng 22 / **Telnet:** Cổng 23 / **SMTP:** Cổng 25 (Gửi mail) / **DNS:** Cổng 53 / **HTTP:** Cổng 80 / **HTTPS:** Cổng 443.
  - Phân biệt ARP vs RARP:
    - **ARP (Address Resolution Protocol):** Biết IP logic $\rightarrow$ Tìm ra địa chỉ vật lý **MAC**.
    - **RARP (Reverse ARP):** Biết địa chỉ MAC $\rightarrow$ Hỏi xin địa chỉ **IP**.
  - Phân biệt ICMP vs IGMP:
    - **ICMP:** Quản lý thông báo lỗi và kiểm tra kết nối mạng (lệnh `ping`).
    - **IGMP:** Quản lý các nhóm truyền thông đa hướng (**Multicast Group**).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng đối chiếu hai giao thức tầng giao vận: TCP vs UDP:**

| Tiêu chuẩn so sánh | TCP (Transmission Control Protocol) | UDP (User Datagram Protocol) |
| :--- | :--- | :--- |
| **Mô hình kết nối** | **Hướng kết nối** (Connection-Oriented); thiết lập phiên qua thuật toán bắt tay 3 bước (**3-Way Handshake: SYN $\rightarrow$ SYN+ACK $\rightarrow$ ACK**). | **Phi kết nối** (Connectionless); gửi trực tiếp các gói tin Datagram mà không cần thỏa thuận kết nối trước. |
| **Độ tin cậy** | **Đảm bảo 100% tin cậy**; có cơ chế đánh số thứ tự (Sequence Number), gửi báo nhận (ACK), và tự động phát lại gói tin thất lạc (ARQ). | **Không đảm bảo độ tin cậy** (Best-Effort); không kiểm tra gói tin có đến nơi hay không, không gửi lại. |
| **Kiểm soát truyền** | Có cơ chế **Kiểm soát luồng** (Flow Control qua Sliding Window) và **Kiểm soát tắc nghẽn** (Congestion Control). | **Không có kiểm soát luồng** và không có kiểm soát tắc nghẽn; máy phát cứ phát hết tốc lực. |
| **Kích thước tiêu đề** | Tiêu đề lớn và phức tạp (**20 ~ 60 Byte**). | Tiêu đề siêu nhẹ cố định chỉ **8 Byte** (gồm Port nguồn, Port đích, Độ dài, Checksum). |
| **Tốc độ & Ứng dụng** | Tốc độ chậm hơn do chi phí overhead; dùng cho truyền tệp (**FTP**), duyệt web (**HTTP/HTTPS**), gửi nhận email (**SMTP**). | **Tốc độ cực nhanh, độ trễ thấp**; dùng cho truyền phát video trực tiếp (Streaming), thoại VoIP, game online, tra cứu tên miền (**DNS**), quản trị mạng (**SNMP**). |

- **2. Bảng phân loại các giao thức tầng mạng (Internet Layer):**

| Giao thức | Tên đầy đủ | Vai trò chức năng trong ngăn xếp mạng |
| :--- | :--- | :--- |
| **IP** | Internet Protocol | Giao thức truyền gói tin không tin cậy ở tầng mạng; thực hiện đánh địa chỉ logic (IPv4/IPv6) và phân mảnh gói tin khi cần. |
| **ICMP** | Internet Control Message Protocol | Giao thức truyền thông điệp điều khiển; báo cáo trạng thái lỗi mạng (Host Unreachable, Time Exceeded) và hỗ trợ công cụ chẩn đoán mạng (`ping`, `traceroute`). |
| **IGMP** | Internet Group Management Protocol | Cho phép các máy trạm thông báo với các bộ định tuyến lân cận về việc tham gia hay rời khỏi một **nhóm truyền đa hướng (Multicast Group)**. |
| **ARP** | Address Resolution Protocol | Ánh xạ và chuyển đổi từ **địa chỉ logic IP sang địa chỉ vật lý MAC** trong mạng cục bộ LAN. |
| **RARP** | Reverse Address Resolution Protocol | Chuyển đổi ngược lại từ **địa chỉ vật lý MAC sang địa chỉ logic IP** (dùng cho các máy trạm không có ổ cứng khi khởi động mạng). |

- **3. Bảng số hiệu cổng (Port Numbers) tầng ứng dụng kinh điển:**

| Giao thức ứng dụng | Số hiệu Port mặc định | Giao thức tầng giao vận | Chức năng nghiệp vụ |
| :--- | :---: | :---: | :--- |
| **FTP** | **20** (Data) / **21** (Control) | TCP | Truyền và nhận tệp tin giữa máy khách và máy chủ. |
| **SSH** | **22** | TCP | Đăng nhập dòng lệnh từ xa có mã hóa bảo mật. |
| **Telnet** | **23** | TCP | Đăng nhập dòng lệnh từ xa dạng văn bản thô (Plain text). |
| **SMTP** | **25** | TCP | Chuyển phát thư điện tử giữa các máy chủ mail (Gửi đi). |
| **DNS** | **53** | **UDP** (chính) / TCP | Phân giải tên miền (Domain Name) thành địa chỉ IP. |
| **HTTP** | **80** | TCP | Truyền nhận siêu văn bản Web thông thường. |
| **POP3** | **110** | TCP | Nhận thư điện tử từ máy chủ về máy khách (xóa trên server). |
| **IMAP** | **143** | TCP | Đồng bộ và quản lý thư điện tử trực tiếp trên máy chủ. |
| **SNMP** | **161** / **162** | **UDP** | Giám sát và quản trị các thiết bị mạng từ xa. |
| **HTTPS** | **443** | TCP | Truyền nhận Web an toàn có mã hóa qua SSL/TLS. |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Quy trình phân giải địa chỉ của giao thức ARP:**
  - Khi máy A muốn gửi gói tin cho máy B trong cùng mạng LAN nhưng chỉ biết địa chỉ IP của B mà chưa biết địa chỉ MAC:
    1. Máy A phát một gói tin **ARP Request** dưới dạng quảng bá (**Broadcast - gửi tới địa chỉ MAC `FF:FF:FF:FF:FF:FF`**) hỏi: *"Ai có địa chỉ IP này thì trả lời địa chỉ MAC cho tôi"*.
    2. Tất cả các máy trong mạng đều nhận được gói tin, nhưng chỉ có máy B khớp địa chỉ IP mới phản hồi lại.
    3. Máy B gửi gói tin **ARP Reply** dưới dạng đơn vị truyền (**Unicast**) chứa địa chỉ MAC của mình về cho máy A.
    4. Máy A lưu ánh xạ IP - MAC này vào bảng bộ đệm **ARP Cache** để sử dụng cho các lần sau.

### 복습 체크리스트
- [ ] Phân biệt rõ TCP (hướng kết nối, tin cậy, chậm) vs UDP (phi kết nối, tiêu đề 8B, nhanh).
- [ ] Nhớ ARP chuyển từ IP sang MAC, còn RARP chuyển từ MAC sang IP.
- [ ] Nhớ ICMP dùng báo lỗi mạng và lệnh ping, IGMP dùng quản lý nhóm Multicast.
- [ ] Thuộc lòng các cổng kinh điển: SSH (22), Telnet (23), SMTP (25), DNS (53), HTTP (80), HTTPS (443).
