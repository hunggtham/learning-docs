# 네트워크 통신, OSI 7계층 및 네트워크 프로토콜 (Mạng máy tính, OSI 7 tầng & Giao thức)

## 학습 목표 (Mục tiêu)
- Thuộc lòng 7 tầng của mô hình tham chiếu OSI theo khẩu quyết **물데네 전세표응** (Vật lý, Liên kết dữ liệu, Mạng, Giao vận, Phiên, Trình diễn, Ứng dụng) và đối chiếu với mô hình TCP/IP 4 tầng.
- Nắm vững đơn vị dữ liệu giao thức (PDU: Bit, Frame, Packet, Segment, Data), quá trình Đóng gói (Encapsulation) và Mở gói (Decapsulation), cùng các thiết bị phần cứng tương ứng ở từng tầng (Repeater/Hub, Switch/Bridge, Router, Gateway).
- Phân biệt chi tiết 3 nhóm thuật toán định tuyến: Vectơ khoảng cách (Distance Vector / RIP - Bellman-Ford, giới hạn 15 hop, Count-to-Infinity), Trạng thái liên kết (Link State / OSPF - Dijkstra SPF, phân vùng Area), và Vectơ đường dẫn (Path Vector / BGP - liên kết các hệ tự trị AS).
- Làm chủ nguyên lý hoạt động của các giao thức tầng ứng dụng và mạng then chốt: DNS (Port 53), HTTP/HTTPS (Port 80/443, Status Codes), FTP (Port 20/21, Active vs Passive), Mail (SMTP 25, POP3 110, IMAP 143), DHCP (tiến trình 4 bước DORA), ARP (IP -> MAC), ICMP (báo cáo lỗi, lệnh `ping`).

## 핵심 키워드 (Từ khóa)
- OSI 7계층 vs TCP/IP 4계층 — 물데네 전세표응 vs 네트워크 액세스, 인터넷, 전송, 응용.
- 프로토콜 데이터 단위 (PDU) — Bit, Frame (L2 Switch), Packet (L3 Router), Segment (L4), Data (L5-7).
- 캡슐화 vs 역캡슐화 (Encapsulation vs Decapsulation) — Thêm Header/Trailer từ trên xuống vs Bóc tách Header từ dưới lên.
- 네트워크 장비 계층 (Network Devices) — Hub/Repeater (Tầng 1), Switch/Bridge (Tầng 2), Router (Tầng 3), Gateway (Tầng 4-7).
- 라우팅 프로토콜 (Routing Protocols) — RIP (거리 벡터, 15홉 제한, 벨만-포드), OSPF (링크 상태, 다익스트라, Area 분할), BGP (경로 벡터, AS 간 라우팅).
- 응용 계층 프로토콜 (Application Protocols) — DNS (53), HTTP (80) / HTTPS (443), FTP (20/21), SMTP (25), POP3 (110), IMAP (143), DHCP (DORA).
- ARP vs RARP — Phân giải IP sang MAC vs Phân giải MAC sang IP.

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Hoàn tất toàn bộ khối kiến thức về Hệ điều hành đơn máy (OS); chuyển sang giao tiếp liên máy tính thông qua mạng viễn thông.
- **Đang giải quyết gì (Current Problem):** Giải quyết câu hỏi: Làm thế nào dữ liệu từ ứng dụng trên máy tính này có thể đóng gói, chuyển đổi và định tuyến chính xác qua hàng trăm thiết bị mạng trung gian để đến đúng ứng dụng trên máy tính khác.
- **Dùng đi đâu (Forward Handoff):** Sau khi gói tin đến tầng Mạng, việc đảm bảo truyền thông tin cậy không mất gói giữa 2 đầu cuối sẽ do tầng Giao vận đảm nhận qua bài `17-tang-giao-van-tcp-udp-va-kiem-soat-luong.md`, và việc đánh địa chỉ IP/chia subnet được trình bày chi tiết ở `18-dia-chi-ip-ipv4-ipv6-va-chia-mang-con-subnetting.md`.

## 읽는 방법 (Cách đọc)
- **Khẩu quyết 7 tầng:** Bắt buộc phải thuộc: **물·데·네 전·세·표·응** (물리 -> 데이터링크 -> 네트워크 -> 전송 -> 세션 -> 표현 -> 응용).
- **Khẩu quyết PDU (Đơn vị dữ liệu):** **비·프·패·세** (Bit -> Frame -> Packet -> Segment).
- **Thiết bị:** Tầng 1: Hub/Repeater; Tầng 2: Switch/Bridge; Tầng 3: Router; Tầng 4-7: Gateway.
- **Định tuyến:**
  - RIP: Bellman-Ford, đếm Hop tối đa **15 Hop** (16 Hop là vô cực), chu kỳ phát tán 30 giây.
  - OSPF: Dijkstra, Link State, không giới hạn bước nhảy, phân chia Area, hội tụ nhanh.
  - BGP: Path Vector giữa các hệ tự trị AS (Autonomous System).
- **Giao thức ứng dụng:**
  - DNS: Port 53 (UDP cho truy vấn thông thường, TCP khi truyền vùng Zone Transfer).
  - FTP: Port 21 (Lệnh điều khiển Control), Port 20 (Truyền dữ liệu Data).
  - DHCP: Quy trình 4 bước **DORA** (Discover -> Offer -> Request -> Acknowledge).

---

## 네트워크 통신, OSI 7계층 및 네트워크 프로토콜

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [한국어]: `OSI 7계층의 PDU는 물리(비트), 데이터링크(프레임-스위치), 네트워크(패킷-라우터), 전송(세그먼트-게이트웨이)이다. 데이터 송신 시 상위에서 하위로 헤더가 추가되는 캡슐화가, 수신 시 하위에서 상위로 헤더가 제거되는 역캡슐화가 일어난다. RIP는 거리 벡터 기반 최대 15홉, OSPF는 링크 상태 다익스트라 최단 경로, BGP는 AS 간 경로 벡터 프로토콜이다. DNS는 53번, HTTP/HTTPS는 80/443번, DHCP는 DORA 절차를 거친다.`
  - [Tiếng Việt]: PDU của mô hình OSI gồm Vật lý (Bit), Data Link (Frame - Switch), Mạng (Packet - Router), Giao vận (Segment - Gateway). Khi gửi dữ liệu diễn ra đóng gói thêm Header từ trên xuống, khi nhận diễn ra mở gói bóc tách Header từ dưới lên. RIP dựa trên vectơ khoảng cách tối đa 15 hop, OSPF dựa trên trạng thái liên kết dùng giải thuật Dijkstra, BGP là giao thức vectơ đường dẫn giữa các AS. DNS dùng port 53, HTTP/HTTPS dùng port 80/443, DHCP trải qua 4 bước DORA.

- **1. Bảng đối chiếu Mô hình OSI 7 tầng vs Mô hình TCP/IP:**

| Tầng OSI 7 Layer | Đơn vị PDU | Thiết bị mạng đại diện | Tầng TCP/IP tương ứng | Giao thức tiêu biểu |
| :---: | :---: | :--- | :---: | :--- |
| **7. Ứng dụng (응용 - Application)** | Data | Gateway / L7 Proxy | **4. Tầng Ứng dụng** (Application) | HTTP, HTTPS, FTP, DNS, SMTP, DHCP |
| **6. Trình diễn (표현 - Presentation)**| Data | Gateway | **4. Tầng Ứng dụng** (Application) | SSL/TLS, ASCII, JPEG, MPEG |
| **5. Phiên (세션 - Session)** | Data | Gateway | **4. Tầng Ứng dụng** (Application) | RPC, NetBIOS, Socket API |
| **4. Giao vận (전송 - Transport)** | **세그먼트 (Segment)** | **Gateway, L4 Switch** | **3. Tầng Giao vận** (Transport) | TCP, UDP |
| **3. Mạng (네트워크 - Network)** | **패킷 (Packet)** | **Router, L3 Switch** | **2. Tầng Internet** (Internet) | IP, ICMP, IGMP, ARP, RARP |
| **2. Liên kết dữ liệu (데이터링크)** | **프레임 (Frame)** | **Switch (L2), Bridge**| **1. Tầng Truy cập mạng** (Network Access)| Ethernet, PPP, HDLC, MAC |
| **1. Vật lý (물리 - Physical)** | **비트 (Bit)** | **Hub, Repeater** | **1. Tầng Truy cập mạng** (Network Access)| RS-232C, Cáp xoắn đôi, Cáp quang |

- **2. Bảng 3 giao thức định tuyến cốt lõi (Routing Protocols):**

| Giao thức định tuyến | Thuật toán cốt lõi | Thước đo (Metric) | Giới hạn quy mô & Phạm vi | Cơ chế cập nhật |
| :--- | :--- | :--- | :--- | :--- |
| **RIP (Routing Information Protocol)** | **거리 벡터 (Distance Vector)** dựa trên giải thuật Bellman-Ford | **Số bước nhảy (Hop Count)** | **Tối đa 15 Hop** (16 Hop là vô cực / Unreachable); chỉ dùng mạng nhỏ (IGP) | Cập nhật định kỳ toàn bộ bảng định tuyến mỗi 30 giây bằng Broadcast; dễ gặp lỗi Count-to-Infinity. |
| **OSPF (Open Shortest Path First)** | **링크 상태 (Link State)** dựa trên giải thuật Dijkstra (SPF) | Băng thông và chi phí liên kết (Cost) | **Không giới hạn bước nhảy**; phân chia vùng **Area** có cấu trúc phân cấp (IGP) | Chỉ gửi gói cập nhật (LSA/LSU) bằng Multicast khi mạng có biến động liên kết; hội tụ cực nhanh. |
| **BGP (Border Gateway Protocol)** | **경로 벡터 (Path Vector)** dựa trên chính sách định tuyến AS | Danh sách chuỗi hệ tự trị (AS-Path) | Định tuyến ngoài (**EGP**) kết nối giữa các mạng tự trị **AS (Autonomous System)** toàn cầu | Trao đổi thông tin định tuyến qua kết nối TCP (Port 179); ngăn chặn loop bằng thuộc tính AS-Path. |

- **3. Bảng các giao thức Tầng Ứng dụng (Application Layer Protocols):**

| Giao thức | Cổng cổng chuẩn (Port) | Giao thức tầng 4 | Chức năng kỹ thuật & Đặc điểm thi cử |
| :--- | :---: | :---: | :--- |
| **DNS** | **53** | **UDP / TCP** | Phân giải tên miền thành địa chỉ IP (dùng UDP cho truy vấn thông thường, TCP khi đồng bộ vùng Zone Transfer). |
| **HTTP** | **80** | **TCP** | Giao thức truyền siêu văn bản không mã hóa (Stateless, Request/Response). |
| **HTTPS** | **443** | **TCP** | HTTP kết hợp bảo mật SSL/TLS mã hóa dữ liệu đầu cuối. |
| **FTP** | **20 (Data), 21 (Control)**| **TCP** | Truyền tệp tin: Port 21 gửi lệnh điều khiển, Port 20 truyền tải dữ liệu (Active vs Passive Mode). |
| **SMTP** | **25** | **TCP** | Giao thức **gửi thư điện tử (Gửi mail)** giữa các máy chủ Mail Server. |
| **POP3** | **110** | **TCP** | Giao thức **nhận thư về máy khách và xóa thư trên server** (kéo về cục bộ). |
| **IMAP** | **143** | **TCP** | Giao thức **đồng bộ và đọc thư trực tiếp trên server** từ nhiều thiết bị. |
| **DHCP** | **67 (Server), 68 (Client)**| **UDP** | Tự động cấp phát địa chỉ IP động qua quy trình 4 bước **DORA**. |

- **4. Bảng mã trạng thái HTTP (HTTP Status Codes):**

| Nhóm mã | Tên gọi chuẩn | Mã tiêu biểu | Ý nghĩa kỹ thuật |
| :---: | :--- | :---: | :--- |
| **2xx** | **Thành công (Success)** | `200 OK` | Yêu cầu của Client đã được xử lý thành công trọn vẹn. |
| **3xx** | **Chuyển hướng (Redirection)** | `301 Moved Permanently` | Tài nguyên đã được chuyển vĩnh viễn sang URL mới. |
| **4xx** | **Lỗi phía máy khách (Client Error)** | `400 Bad Request`, `403 Forbidden`, `404 Not Found` | Lỗi cú pháp request, không có quyền truy cập, hoặc không tìm thấy trang. |
| **5xx** | **Lỗi phía máy chủ (Server Error)** | `500 Internal Error`, `502 Bad Gateway`, `503 Service Unavailable`| Máy chủ gặp sự cố nội bộ, nghẽn tải hoặc proxy lỗi. |

- **주의/함정 (Bẫy đề thi):**
  - **Giới hạn 15 Hop của RIP:** Đề thi khẳng định *"RIP hỗ trợ tối đa 30 Hop cho mạng doanh nghiệp lớn"* -> **SAI HOÀN TOÀN**; RIP giới hạn cứng 15 Hop (Hop thứ 16 coi là không đến được).
  - **Chức năng tầng Presentation:** Nén dữ liệu (압축) và Mã hóa (암호화) luôn luôn thuộc trách nhiệm của **Tầng 6 (표현 계층 - Presentation)**, không thuộc tầng ứng dụng.
  - **Cổng kép của FTP:** FTP dùng 2 cổng độc lập: Port 21 cho điều khiển (Control) và Port 20 cho dữ liệu (Data).
  - **Active vs Passive FTP:** Trong Active mode, Client mở cổng ngẫu nhiên và Server chủ động kết nối vào cổng đó (thường bị Firewall của Client chặn); trong Passive mode, Client chủ động tạo cả 2 kết nối đến Server.

- **한 문장 설명 (Câu chốt tự nhớ):**
  - *"물데네 전세표응 7 tầng, 비프패세 4 PDU; RIP 15 hop Bellman-Ford, OSPF Dijkstra chia Area; FTP 20 data 21 control, DHCP 4 bước DORA cấp IP."*

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ quá trình Đóng gói (Encapsulation) và Mở gói (Decapsulation):
```text
[ Máy Gửi: Đóng gói từ trên xuống ]
+-------------------------------------------------------------+
| Tầng 7 - 5 (Data)        |              DỮ LIỆU             |
+-------------------------------------------------------------+
               | Thêm Transport Header (TCP/UDP, Port nguồn, Port đích)
               v
+-------------------------------------------------------------+
| Tầng 4 (Segment)         | TH |           DỮ LIỆU           |
+-------------------------------------------------------------+
               | Thêm Network Header (IP nguồn, IP đích)
               v
+-------------------------------------------------------------+
| Tầng 3 (Packet)          | NH | TH |       DỮ LIỆU          |
+-------------------------------------------------------------+
               | Thêm Data Link Header (MAC nguồn, MAC đích) & Trailer (FCS/CRC)
               v
+-------------------------------------------------------------+
| Tầng 2 (Frame)           | DLH| NH | TH |   DỮ LIỆU   | DLT |
+-------------------------------------------------------------+
               | Chuyển đổi thành chuỗi tín hiệu vật lý 0/1
               v
  Tầng 1 (Bits)            011010010110101100010101...
               |
               ================ Cáp mạng / Sóng Wifi ===============
               v
[ Máy Nhận: Mở gói từ dưới lên ]
  Tầng 1: Đọc tín hiệu bit -> Chuyển thành Frame
  Tầng 2: Kiểm tra Frame Check Sequence (FCS), bóc tách DLH/DLT -> Lấy Packet
  Tầng 3: Kiểm tra IP đích, bóc tách Network Header (NH) -> Lấy Segment
  Tầng 4: Kiểm tra Port đích, sắp xếp lại thứ tự dữ liệu, bóc tách TH -> Lấy Data
  Tầng 7: Ứng dụng nhận dữ liệu gốc nguyên vẹn
```

#### 2. Sơ đồ quy trình 4 bước cấp phát IP của giao thức DHCP (DORA Process):
```text
Client (Chưa có IP)                                DHCP Server
-------------------                                -----------
         |                                              |
         | -------- 1. DHCP Discover (Broadcast) ------> | "Tôi là máy mới, có ai cấp IP không?"
         |                                              |
         | <------- 2. DHCP Offer (Unicast/Bcast) ----- | "Tôi có IP 192.168.1.100 cho bạn thuê đây!"
         |                                              |
         | -------- 3. DHCP Request (Broadcast) ------> | "Tôi đồng ý thuê IP 192.168.1.100 này!"
         |                                              |
         | <------- 4. DHCP Acknowledge (ACK) --------- | "Xác nhận! Bạn được dùng IP này trong 24h."
         |                                              |
(Client cấu hình IP 192.168.1.100 và kết nối mạng thành công)
```

#### 3. Bảng so sánh chi tiết các giao thức định tuyến:

| Tiêu chí | RIP v1 / v2 | OSPF v2 / v3 | BGP v4 |
| :--- | :--- | :--- | :--- |
| **Phân loại** | IGP (Nội vùng) | IGP (Nội vùng) | EGP (Ngoại vùng, liên AS) |
| **Thuật toán** | Bellman-Ford | Dijkstra Shortest Path First | Path Vector Algorithm |
| **Thước đo** | Hop Count (Max 15) | Cost (Nghịch đảo băng thông) | AS-Path, Local Pref, Multi-Exit Discriminator |
| **Quy mô mạng** | Mạng nhỏ (< 15 routers) | Mạng doanh nghiệp lớn | Toàn bộ Internet toàn cầu |
| **Phân cấp** | Phẳng (Flat) | Phân tầng 2 cấp (Backbone Area 0) | Cụm hệ tự trị (Autonomous System) |
| **Giao thức vận chuyển**| UDP (Port 520) | IP trực tiếp (Protocol 89) | TCP (Port 179) |

---

### 복습 체크리스트
- [ ] Thuộc lòng 7 tầng OSI: **물데네 전세표응** (물리, 데이터링크, 네트워크, 전송, 세션, 표현, 응용).
- [ ] Thuộc lòng 4 đơn vị PDU: **비프패세** (Bit, Frame, Packet, Segment).
- [ ] Nắm chắc quy trình Encapsulation (gửi đóng gói thêm header) và Decapsulation (nhận bóc tách header).
- [ ] Nhớ thiết bị từng tầng: Tầng 1 (Hub/Repeater), Tầng 2 (Switch/Bridge), Tầng 3 (Router), Tầng 4-7 (Gateway).
- [ ] Thuộc lòng đặc trưng RIP: Vectơ khoảng cách, đếm bước nhảy Hop $\le 15$.
- [ ] Phân biệt OSPF: Trạng thái liên kết, Dijkstra SPF, phân vùng Area, hội tụ nhanh.
- [ ] Nhớ BGP: Định tuyến giữa các mạng tự trị AS trên Internet toàn cầu qua TCP Port 179.
- [ ] Nhớ các port giao thức: DNS (53), HTTP (80), HTTPS (443), FTP (20/21), SMTP (25), POP3 (110), IMAP (143).
- [ ] Thuộc lòng 4 bước của DHCP: **DORA** (Discover -> Offer -> Request -> Acknowledge).
