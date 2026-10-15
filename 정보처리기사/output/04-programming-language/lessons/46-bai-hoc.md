# 309 - 314. OSI 7계층과 네트워크 프로토콜 (OSI 7 Layers & Protocols)

## 학습 목표 (Mục tiêu)
- Nắm vững danh sách các giao thức mạng chuẩn hóa theo từng tầng trong mô hình OSI 7 tầng và bộ giao thức TCP/IP.
- Phân biệt chính xác chức năng của các giao thức tầng mạng (Network Layer): IP (định tuyến), ICMP (báo cáo lỗi và lệnh `ping`), IGMP (quản lý nhóm multicast), ARP (biến đổi IP sang MAC), và RARP (biến đổi MAC sang IP).
- Nắm vững các giao thức ứng dụng phổ biến và số hiệu cổng mặc định: HTTP (80), HTTPS (443), FTP (20/21), SSH (22), Telnet (23), SMTP (25), và DNS (53).

## 핵심 키워드 (Từ khóa)
- 네트워크 프로토콜 (Network Protocols)
- ARP vs RARP (Address Resolution Protocol / IP $\leftrightarrow$ MAC 변환)
- ICMP (Internet Control Message Protocol / 오류 보고 및 ping)
- IGMP (Internet Group Management Protocol / 멀티캐스트 그룹 관리)
- 응용 계층 프로토콜 (HTTP, FTP, SMTP, DNS, SNMP)
- 표준 포트 번호 (Standard Port Numbers: 80, 443, 21, 22, 25, 53)

## 선행·연결 개념 (Kiến thức liên kết)
- [45-bai-hoc.md](45-bai-hoc.md): Giao thức TCP vs UDP và điều khiển luồng.
- [47-bai-hoc.md](47-bai-hoc.md): Nguyên lý thiết kế phần mềm có cấu trúc.
- [44-bai-hoc.md](44-bai-hoc.md): Mô hình tham chiếu OSI 7 tầng và đơn vị dữ liệu PDU.

## 읽는 방법 (Cách đọc)
- Phân biệt hai cặp giao thức chuyển đổi địa chỉ và kiểm tra mạng:
  - **`ARP` vs `RARP`:**
    - **`ARP` (Address Resolution Protocol):** Khi biết địa chỉ logic **IP**, phát thanh (Broadcast) để hỏi và tìm địa chỉ vật lý **MAC** tương ứng của card mạng.
    - **`RARP` (Reverse ARP):** Ngược lại hoàn toàn; khi một máy không có ổ cứng chỉ biết địa chỉ **MAC**, hỏi máy chủ để lấy về địa chỉ **IP**.
  - **`ICMP` (Internet Control Message Protocol):**
    - Giao thức báo cáo lỗi và kiểm tra trạng thái hoạt động của mạng. Câu lệnh **`ping`** và **`traceroute`** trên máy tính chạy trực tiếp trên nền của giao thức ICMP.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng các giao thức cốt lõi tại Tầng Mạng (Network Layer - L3):**

| Tên giao thức | Tên tiếng Anh đầy đủ | Chức năng kỹ thuật chuẩn đề thi |
| :--- | :--- | :--- |
| **`IP`** | **Internet Protocol** | Đóng gói dữ liệu thành gói tin (Packet) và **định tuyến (Routing)** chuyển tiếp qua các mạng |
| **`ARP`** | **Address Resolution Protocol** | Chuyển đổi từ địa chỉ logic **IP $\rightarrow$ Địa chỉ vật lý MAC** |
| **`RARP`** | **Reverse Address Resolution Protocol** | Chuyển đổi ngược từ địa chỉ vật lý **MAC $\rightarrow$ Địa chỉ logic IP** |
| **`ICMP`** | **Internet Control Message Protocol** | Báo cáo lỗi truyền thông mạng (Destination Unreachable, Time Exceeded); **công cụ `ping`** |
| **`IGMP`** | **Internet Group Management Protocol** | Quản lý việc tham gia hoặc rời khỏi của các máy trạm trong các **nhóm truyền đa hướng (Multicast Group)** |

- **Bảng các giao thức Tầng Ứng dụng (Application Layer - L7) và Cổng (Port):**

| Giao thức | Tên đầy đủ | Số hiệu cổng (Port) | Giao thức tầng 4 | Chức năng ứng dụng |
| :--- | :--- | :---: | :---: | :--- |
| **`FTP`** | **File Transfer Protocol** | **20 (Data), 21 (Control)** | TCP | Truyền và tải tệp tin giữa máy khách và máy chủ |
| **`SSH`** | **Secure Shell** | **22** | TCP | Đăng nhập và điều khiển máy chủ từ xa có mã hóa an toàn |
| **`Telnet`** | **Telecommunication Network** | **23** | TCP | Điều khiển từ xa cổ điển dạng văn bản thuần (Không mã hóa) |
| **`SMTP`** | **Simple Mail Transfer Protocol** | **25** | TCP | Gửi thư điện tử (Email) từ Client lên Mail Server |
| **`DNS`** | **Domain Name System** | **53** | UDP / TCP | Chuyển đổi giữa Tên miền chữ cái (ví dụ: `google.com`) và Địa chỉ số IP |
| **`HTTP`** | **Hypertext Transfer Protocol** | **80** | TCP | Truyền tải tài liệu siêu văn bản Web không mã hóa |
| **`HTTPS`** | **HTTP Secure** | **443** | TCP (qua SSL/TLS) | Truyền web an toàn có mã hóa chứng chỉ số |
| **`SNMP`** | **Simple Network Management Protocol**| **161 / 162** | UDP | Thu thập thông tin và giám sát tình trạng các thiết bị mạng |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Cơ chế lưu trữ bảng ARP Cache:**
  - Để tránh việc liên tục phát thanh (Broadcast) gây nghẽn mạng mỗi khi gửi dữ liệu, hệ điều hành duy trì một bảng nhớ tạm gọi là **ARP Cache Table**.
  - Khi đã phân giải thành công địa chỉ MAC của một IP, máy trạm lưu cặp `(IP, MAC)` vào bộ nhớ trong một khoảng thời gian nhất định (thường là 2 đến 20 phút).

### 복습 체크리스트
- [ ] Nhớ ARP đổi IP sang MAC, RARP đổi MAC sang IP.
- [ ] Nhớ ICMP dùng để báo cáo lỗi và chạy lệnh `ping`.
- [ ] Nhớ IGMP dùng để quản lý nhóm Multicast.
- [ ] Ghi nhớ số hiệu cổng thông dụng: HTTP (80), HTTPS (443), SSH (22), FTP (20/21), DNS (53).
