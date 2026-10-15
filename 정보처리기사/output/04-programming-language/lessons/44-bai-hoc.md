# 088. 인터넷 구성과 네트워크 - OSI 7계층 (OSI 7 Layer)

## 학습 목표 (Mục tiêu)
- Nắm vững cấu trúc phân tầng và chức năng chuyên biệt của mô hình tham chiếu kết nối các hệ thống mở OSI 7 tầng (OSI 7 계층 - Open Systems Interconnection) do tổ chức ISO ban hành.
- Ghi nhớ thần chú thứ tự 7 tầng từ dưới lên trên: **물·데·네·전·세·표·응** (Vật $\rightarrow$ Dữ $\rightarrow$ Mạng $\rightarrow$ Truyền $\rightarrow$ Phiên $\rightarrow$ Biểu $\rightarrow$ Ứng).
- Ghi nhớ chính xác đơn vị dữ liệu giao thức (PDU - Protocol Data Unit) của từng tầng: **Bit $\rightarrow$ Frame $\rightarrow$ Packet $\rightarrow$ Segment $\rightarrow$ Data** theo thần chú **비·프·패·세**.
- Nhận diện các chuẩn mạng cục bộ IEEE 802 tiêu biểu: IEEE 802.3 (Mạng có dây Ethernet / CSMA/CD) và IEEE 802.11 (Mạng không dây Wi-Fi / CSMA/CA).

## 핵심 키워드 (Từ khóa)
- OSI 7계층 (OSI 7 Layers Reference Model)
- 물데네 전세표응 (Mnemonic: 물리, 데이터링크, 네트워크, 전송, 세션, 표현, 응용)
- 프로토콜 데이터 단위 (PDU: Bit, Frame, Packet, Segment, Data)
- 비프패세 (Mnemonic: Bit, Frame, Packet, Segment)
- IEEE 802.3 (이더넷 Ethernet / CSMA/CD)
- IEEE 802.11 (무선랜 Wi-Fi / CSMA/CA)
- 캡슐화 및 역캡슐화 (Encapsulation & Decapsulation)

## 선행·연결 개념 (Kiến thức liên kết)
- [43-bai-hoc.md](43-bai-hoc.md): Mạng truyền thông và thiết bị mạng.
- [45-bai-hoc.md](45-bai-hoc.md): Giao thức TCP vs UDP và điều khiển luồng.
- [46-bai-hoc.md](46-bai-hoc.md): Các giao thức chi tiết theo từng tầng OSI.

## 읽는 방법 (Cách đọc)
- Học theo thần chú 7 tầng từ tầng 1 lên tầng 7:
  $$\mathbf{물} \rightarrow \mathbf{데} \rightarrow \mathbf{네} \rightarrow \mathbf{전} \rightarrow \mathbf{세} \rightarrow \mathbf{표} \rightarrow \mathbf{응}$$
  1. **물 (Vật - 물리 계층 / Physical):** Truyền tín hiệu điện/quang nhị phân thô qua dây cáp mạng $\rightarrow$ Đơn vị là **Bit**. Thiết bị: Cáp mạng, Hub, Repeater.
  2. **데 (Dữ - 데이터 링크 계층 / Data Link):** Truyền dữ liệu tin cậy giữa hai nút lân cận trên cùng mạng LAN, phát hiện lỗi $\rightarrow$ Đơn vị là **Frame**. Địa chỉ vật lý: **MAC Address**. Thiết bị: Switch, Bridge.
  3. **네 (Mạng - 네트워크 계층 / Network):** Định tuyến đường đi tối ưu qua nhiều mạng khác nhau $\rightarrow$ Đơn vị là **Packet**. Địa chỉ logic: **IP Address**. Thiết bị: Router, L3 Switch.
  4. **전 (Truyền - 전송 계층 / Transport):** Truyền dữ liệu đầu cuối (End-to-End) thông suốt giữa hai máy trạm $\rightarrow$ Đơn vị là **Segment**. Định danh: **Port Number**. Giao thức: TCP, UDP.
  5. **세 (Phiên - 세션 계층 / Session):** Thiết lập, duy trì và đồng bộ hóa các cuộc hội thoại giữa các ứng dụng.
  6. **표 (Biểu - 표현 계층 / Presentation):** Mã hóa, giải mã, nén dữ liệu và chuyển đổi định dạng (ASCII, JPEG).
  7. **응 (Ứng - 응용 계층 / Application):** Giao diện cung cấp dịch vụ mạng trực tiếp cho người dùng (HTTP, FTP, DNS).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng tổng hợp chi tiết mô hình OSI 7 tầng:**

| Thứ tự tầng | Tên tầng (Tiếng Hàn & Anh) | Đơn vị dữ liệu (PDU) | Địa chỉ định danh | Giao thức / Thiết bị tiêu biểu |
| :---: | :--- | :--- | :--- | :--- |
| **7** | **응용 계층 (Application)** | **Data (메시지)** | Tên dịch vụ / URL | HTTP, FTP, SMTP, DNS, Telnet |
| **6** | **표현 계층 (Presentation)** | **Data** | Định dạng mã hóa | JPEG, MPEG, SSL/TLS mã hóa, ASCII |
| **5** | **세션 계층 (Session)** | **Data** | Điểm đồng bộ (Sync) | RPC, NetBIOS, Quản lý hội thoại song công |
| **4** | **전송 계층 (Transport)** | **세그먼트 (Segment)** | **Port 번호 (16 bits)** | **TCP, UDP**; L4 Switch |
| **3** | **네트워크 계층 (Network)** | **패킷 (Packet)** | **IP 주소 (32/128 bits)** | **IP, ICMP, IGMP, ARP, RARP**; 라우터 (Router) |
| **2** | **데이터 링크 (Data Link)** | **프레임 (Frame)** | **MAC 주소 (48 bits)** | **HDLC, PPP, Ethernet**; 브리지, L2 스위치 |
| **1** | **물리 계층 (Physical)** | **비트 (Bit)** | Tín hiệu điện, Volt | Cáp xoắn đôi UTP, Cáp quang, 리피터, 허브 |

- **Bảng các chuẩn mạng cục bộ IEEE 802 cốt lõi:**

| Mã chuẩn IEEE | Tên công nghệ mạng | Cơ chế điều khiển truy cập môi trường truyền dẫn |
| :--- | :--- | :--- |
| **IEEE 802.3** | **이더넷 (Ethernet / Mạng LAN có dây)** | **CSMA/CD (Carrier Sense Multiple Access with Collision Detection)** - Lắng nghe đường truyền, phát hiện xung đột và phát lại |
| **IEEE 802.11** | **무선랜 (Wireless LAN / Wi-Fi)** | **CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance)** - Lắng nghe đường truyền, chủ động tránh va chạm xung đột |
| **IEEE 802.15** | **WPAN (Mạng cá nhân không dây)** | Công nghệ truyền thông tầm gần **블루투스 (Bluetooth)** |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Quá trình Đóng gói (Encapsulation) và Mở gói (Decapsulation):**
  - Khi gửi dữ liệu: Dữ liệu đi từ tầng 7 xuống tầng 1. Qua mỗi tầng, một tiêu đề điều khiển (**Header**) tương ứng được gắn thêm vào đầu khối dữ liệu (Data $\rightarrow$ Segment $\rightarrow$ Packet $\rightarrow$ Frame $\rightarrow$ Bit stream).
  - Khi nhận dữ liệu: Quá trình diễn ra ngược lại từ tầng 1 lên tầng 7. Mỗi tầng đọc và bóc tách tiêu đề của mình rồi chuyển phần dữ liệu nguyên bản lên tầng trên.

### 복습 체크리스트
- [ ] Học thuộc lòng thứ tự 7 tầng: 물데네 전세표응 (물리 $\rightarrow$ 데이터링크 $\rightarrow$ 네트워크 $\rightarrow$ 전송 $\rightarrow$ 세션 $\rightarrow$ 표현 $\rightarrow$ 응용).
- [ ] Nhớ đơn vị PDU tương ứng: 비프패세 (Bit, Frame, Packet, Segment).
- [ ] Nhớ IEEE 802.3 là Ethernet có dây (CSMA/CD), IEEE 802.11 là Wi-Fi không dây (CSMA/CA).
- [ ] Nhớ địa chỉ MAC hoạt động ở tầng 2, địa chỉ IP ở tầng 3, và số cổng Port ở tầng 4.
