# 네트워크 구조, OSI 7계층 및 TCP/IP 프로토콜 (Kiến trúc mạng máy tính, Mô hình OSI 7 tầng & Họ giao thức TCP/IP, IP Subnetting)

## 학습 목표 (Mục tiêu)
- Nắm vững kiến trúc phân tầng, chức năng kỹ thuật, đơn vị dữ liệu (PDU) và thiết bị tương ứng của **Mô hình tham chiếu OSI 7 tầng** theo khẩu quyết **물데네전세표응**.
- So sánh sự khác nhau giữa hai giao thức tầng giao vận: **TCP** (hướng kết nối, tin cậy, 3-Way Handshake, kiểm soát luồng) và **UDP** (phi kết nối, tốc độ cao, tiêu đề 8 Byte, tối ưu streaming thời gian thực).
- Làm chủ chức năng của các giao thức tầng mạng: **IP**, **ARP** (IP $\rightarrow$ MAC), **RARP** (MAC $\rightarrow$ IP), **ICMP**, cùng 3 giao thức định tuyến: **RIP** (Distance Vector, max 15 hops), **OSPF** (Link State, Dijkstra), **BGP** (Path Vector).
- Phân biệt cấu trúc địa chỉ IPv4 (32-bit, Classes A/B/C/D/E) và IPv6 (128-bit, 3 phương thức Unicast, Anycast, Multicast).
- Giải thành thạo bài toán chia mạng con (**서브네팅 - Subnetting**): Tính Mặt nạ mạng con (Subnet Mask), Địa chỉ mạng, Địa chỉ quảng bá Broadcast và Số lượng máy trạm khả dụng ($2^h - 2$).
- Nắm vững 5 cấu trúc hình học mạng (Star, Bus, Ring, Tree, Mesh) cùng công thức số đường truyền mạng lưới toàn phần $n(n-1)/2$.
- Phân biệt vai trò tầng hoạt động của các thiết bị mạng: Repeater, Hub, Bridge, L2/L3/L4 Switch, Router, Gateway và kiến trúc **SDN** (tách rời Control Plane và Data Plane).

## 핵심 키워드 (Từ khóa song ngữ)
- OSI 7계층 (OSI 7 Layers — 물데네전세표응: 물리, 데이터링크, 네트워크, 전송, 세션, 표현, 응용)
- PDU (Protocol Data Unit — 비트 Bit, 프레임 Frame, 패킷 Packet, 세그먼트 Segment, 메시지 Message)
- TCP (연결 지향, 신뢰성 보장, 3-Way Handshake, 흐름 제어 슬라이딩 윈도우)
- UDP (비연결 지향, 비신뢰성, 8바이트 헤더, 실시간 스트리밍 최적화)
- ARP / RARP (Address Resolution Protocol — IP $\leftrightarrow$ MAC 주소 변환)
- 라우팅 프로토콜 (Routing Protocols — RIP 거리벡터 15홉 vs OSPF 링크상태 다익스트라 vs BGP)
- IPv4 서브네팅 (IPv4 Subnetting — 서브넷 마스크, 네트워크 주소, 브로드캐스트 주소, 가용 호스트 $2^h - 2$)
- IPv6 (128비트, 16진수 8그룹, 유니캐스트, 애니캐스트, 멀티캐스트, 브로드캐스트 없음)
- 풀 메시 토폴로지 (Full Mesh — Đường truyền $\frac{n(n-1)}{2}$, số cổng mỗi nút $n-1$)
- SDN (Software-Defined Networking — 제어 평면 Control Plane과 데이터 평면 Data Plane의 분리)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Từ các tín hiệu vật lý và kỹ thuật điều chế sóng tại [11-truyen-thong-du-lieu-va-dieu-che.md](11-truyen-thong-du-lieu-va-dieu-che.md), dữ liệu cần được đóng gói thành các cấu trúc tầng logic để di chuyển xuyên qua các mạng máy tính toàn cầu.
- **Đang giải quyết gì (Current Problem):** Bài học này xây dựng bức tranh toàn cảnh về kiến trúc mạng viễn thông: từ mô hình tham chiếu chuẩn OSI 7 tầng, phân tích chi tiết họ giao thức TCP/IP, cách tính toán chia mạng con IPv4/IPv6, cho đến thiết bị phần cứng mạng và công nghệ mạng định nghĩa bằng phần mềm SDN.
- **Dùng đi đâu (Forward Handoff):** Các gói tin sau khi được định tuyến tới máy chủ đích sẽ được hệ điều hành tiếp nhận, đưa vào hàng đợi tiến trình và lập lịch CPU tại [13-he-dieu-hanh-tien-trinh-va-dieu-phoi.md](13-he-dieu-hanh-tien-trinh-va-dieu-phoi.md).

## 읽는 방법 (Cách đọc & Dấu hiệu nhận diện đề thi)
- **Thứ tự 7 tầng OSI (Khẩu quyết vàng):**
  - **물 (Vật lý - 1) $\rightarrow$ 데 (Liên kết dữ liệu - 2) $\rightarrow$ 네 (Mạng - 3) $\rightarrow$ 전 (Giao vận - 4) $\rightarrow$ 세 (Phiên - 5) $\rightarrow$ 표 (Trình diễn - 6) $\rightarrow$ 응 (Ứng dụng - 7)**.
  - PDU tương ứng: **Bit (1) $\rightarrow$ Frame (2) $\rightarrow$ Packet (3) $\rightarrow$ Segment (4) $\rightarrow$ Data/Message (5, 6, 7)**.
- **TCP vs UDP:**
  - Nhắc đến **"연결 지향" (Hướng kết nối)**, **"신뢰성 전송" (Truyền tin cậy)**, **"3-Way Handshake"**, **"흐름 제어"** $\rightarrow$ Chọn **TCP**.
  - Nhắc đến **"비연결 지향" (Phi kết nối)**, **"헤더가 8바이트로 작음"**, **"실시간 스트리밍/DNS"** $\rightarrow$ Chọn **UDP**.
- **Giao thức định tuyến:**
  - **RIP:** Thuật toán **거리 벡터 (Distance Vector)**, dùng **Hop Count**, tối đa **15 hop** (16 hop coi là không thể tới).
  - **OSPF:** Thuật toán **링크 상태 (Link State)**, dùng thuật toán **다익스트라 (Dijkstra)** tìm đường ngắn nhất, chia vùng **Area**.
  - **BGP:** Giao thức định tuyến giữa các mạng tự trị **AS (Autonomous System)**.
- **Bài toán Subnetting (Tính nhanh trong đề thi):**
  - Số máy trạm khả dụng luôn là **$2^h - 2$** (với $h$ là số bit 0 còn lại trong phần Host ID).
  - Bắt buộc trừ 2 vì: địa chỉ toàn bit 0 là **네트워크 주소 (Địa chỉ mạng)**, địa chỉ toàn bit 1 là **브로드캐스트 주소 (Địa chỉ quảng bá)**.
- **Công thức Mạng lưới toàn phần (Full Mesh Topology):**
  - Số đường truyền: $\frac{n(n-1)}{2}$. Ví dụ 6 nút cần $\frac{6 \times 5}{2} = 15$ đường truyền.

---

## 네트워크 구조, OSI 7계층 및 TCP/IP 프로토콜

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Mô hình tham chiếu OSI 7 tầng (ISO 7498)

| Tầng OSI | Tên tiếng Hàn & Anh | Đơn vị dữ liệu (PDU) | Chức năng kỹ thuật cốt lõi | Thiết bị mạng tương ứng |
| :---: | :--- | :---: | :--- | :--- |
| **Tầng 7** | **응용 (Application)** | **Data / Message** | Giao diện trực tiếp cung cấp dịch vụ mạng cho người dùng cuối (HTTP, FTP, SMTP, DNS). | Gateway, L7 Switch, WAF |
| **Tầng 6** | **표현 (Presentation)** | **Data / Message** | Định dạng dữ liệu, chuyển đổi bảng mã (ASCII, EBCDIC), nén dữ liệu và **Mã hóa / Giải mã (Encryption)**. | Gateway |
| **Tầng 5** | **세션 (Session)** | **Data / Message** | Thiết lập, duy trì và giải phóng phiên giao tiếp; quản lý **Điểm đồng bộ (Synchronization Points: Major/Minor)** để phục hồi khi đứt kết nối. | Gateway |
| **Tầng 4** | **전송 (Transport)** | **세그먼트 (Segment)** | Đảm bảo truyền dữ liệu đầu cuối tới đầu cuối (**End-to-End**) tin cậy; đánh số cổng (**Port**); kiểm soát luồng, kiểm soát lỗi và phân mảnh. | **L4 Switch** |
| **Tầng 3** | **네트워크 (Network)** | **패킷 (Packet)** | Định tuyến đường đi tốt nhất qua mạng (**Routing**); đánh địa chỉ logic (**IP**); kiểm soát tắc nghẽn liên mạng. | **Router, L3 Switch** |
| **Tầng 2** | **데이터 링크 (Data Link)** | **프레임 (Frame)** | Truyền dữ liệu tin cậy giữa hai nút lân cận trên cùng đường truyền vật lý; đánh địa chỉ vật lý (**MAC**); kiểm soát lỗi khung (CRC). | **Bridge, L2 Switch, NIC** |
| **Tầng 1** | **물리 (Physical)** | **비트 (Bit)** | Chuyển đổi chuỗi bit nhị phân thành tín hiệu điện/quang và truyền qua dây cáp vật lý. | **Repeater, Hub** |

#### 2. Đối chiếu hai giao thức tầng giao vận: TCP vs UDP

| Đặc tính kỹ thuật | Giao thức TCP (Transmission Control Protocol) | Giao thức UDP (User Datagram Protocol) |
| :--- | :--- | :--- |
| **Phương thức kết nối** | **연결 지향 (Connection-Oriented)**; thiết lập kết nối trước bằng bắt tay 3 bước (**3-Way Handshake**). | **비연결 지향 (Connectionless)**; gửi trực tiếp không cần thiết lập kết nối trước. |
| **Độ tin cậy** | **Rất cao**; bảo đảm dữ liệu đến đích nguyên vẹn, đúng thứ tự tuần tự; tự động yêu cầu truyền lại khi mất gói. | **Không đảm bảo (Best-effort)**; gói tin có thể bị mất, trùng lặp hoặc đến đích sai thứ tự. |
| **Kích thước tiêu đề** | Tiêu đề lớn, tối thiểu **20 Byte** (có thể mở rộng đến 60 Byte). | Tiêu đề siêu nhẹ, cố định chỉ **8 Byte** (Source Port, Dest Port, Length, Checksum). |
| **Cơ chế kiểm soát** | Có cơ chế **Kiểm soát luồng (Sliding Window)** và **Kiểm soát tắc nghẽn (Congestion Control)**. | **Không có kiểm soát luồng và tắc nghẽn**; tốc độ xả gói tin tối đa theo khả năng ứng dụng. |
| **Ứng dụng tiêu biểu** | Truyền tệp tin (**FTP**), Tải trang web (**HTTP/HTTPS**), Gửi nhận thư điện tử (**SMTP, POP3**). | Truyền phát video trực tiếp (Streaming), Thoại Internet (**VoIP**), Tra cứu tên miền (**DNS**), Giám sát mạng (**SNMP**). |

#### 3. Các giao thức tầng mạng và định tuyến (Routing Protocols)
- **Giao thức ánh xạ địa chỉ:**
  - **ARP (Address Resolution Protocol):** Phân giải địa chỉ logic IP (32-bit) thành địa chỉ vật lý MAC (48-bit) của card mạng.
  - **RARP (Reverse ARP):** Phân giải ngược từ địa chỉ vật lý MAC thành địa chỉ IP (dùng cho máy trạm không có ổ đĩa Diskless Workstation).
- **Giao thức điều khiển và quản trị:**
  - **ICMP (Internet Control Message Protocol):** Giao thức thông báo lỗi và chẩn đoán đường truyền (lệnh `ping`, `traceroute`).
  - **IGMP (Internet Group Management Protocol):** Quản lý thành viên trong các nhóm truyền đa hướng (Multicast Group).
- **So sánh 3 giao thức định tuyến cốt lõi:**

| Giao thức định tuyến | Thuật toán định tuyến cốt lõi | Metric đo lường & Giới hạn quy mô | Đặc điểm vận hành trong đề thi |
| :--- | :--- | :--- | :--- |
| **RIP** | **거리 벡터 (Distance Vector)**<br>(Thuật toán Bellman-Ford) | Số bước nhảy (**Hop Count**); **Giới hạn tối đa 15 Hop** (16 Hop coi là đích không thể tới). | Định kỳ **mỗi 30 giây phát tán Broadcast toàn bộ bảng định tuyến** cho các router lân cận; chỉ phù hợp cho mạng quy mô nhỏ. |
| **OSPF** | **링크 상태 (Link State)**<br>(Thuật toán Dijkstra SPF) | Băng thông đường truyền (**Cost**); không giới hạn số bước nhảy. | Phân chia mạng thành các vùng (**Area**); chỉ gửi gói tin cập nhật khi mạng có sự thay đổi trạng thái đường truyền; phù hợp mạng doanh nghiệp lớn. |
| **BGP** | **경로 벡터 (Path Vector)** | Chính sách định tuyến mạng và danh sách các hệ tự trị AS. | Giao thức định tuyến ngoài (**EGP**) kết nối giữa các nhà mạng viễn thông và hệ thống tự trị **AS (Autonomous System)** trên toàn cầu. |

#### 4. Địa chỉ IPv4 và Kỹ thuật chia mạng con (Subnetting)
- **Cấu trúc IPv4 (32-bit):** 4 nhóm số thập phân (Octet), mỗi nhóm 8 bit ($0 \sim 255$):
  - **Lớp A:** $0.0.0.0 \sim 127.255.255.255$ (Subnet Mask mặc định: `255.0.0.0` hay `/8`).
  - **Lớp B:** $128.0.0.0 \sim 191.255.255.255$ (Subnet Mask mặc định: `255.255.0.0` hay `/16`).
  - **Lớp C:** $192.0.0.0 \sim 223.255.255.255$ (Subnet Mask mặc định: `255.255.255.0` hay `/24`).
  - **Lớp D:** $224.0.0.0 \sim 239.255.255.255$ (Dành riêng cho truyền đa hướng **Multicast**).
  - **Lớp E:** $240.0.0.0 \sim 255.255.255.255$ (Dành riêng cho nghiên cứu thử nghiệm).
- **Công thức tính toán Subnetting chuẩn:**
  - Nếu mượn $s$ bit từ phần Host ID làm Subnet ID $\rightarrow$ Số lượng mạng con tạo thành $= 2^s$.
  - Số bit còn lại trong phần Host ID là $h$ bit $\rightarrow$ Số lượng địa chỉ IP khả dụng gán cho máy trạm:
    $$\text{Số Host khả dụng} = 2^h - 2$$
  - *(Lý do trừ 2: Địa chỉ có toàn bit host bằng 0 đại diện cho **Network Address**, địa chỉ có toàn bit host bằng 1 đại diện cho **Broadcast Address**).*
- **Đặc trưng của thế hệ IPv6 (128-bit):**
  - Độ dài 128 bit, biểu diễn bằng 8 nhóm số thập lục phân (Hexadecimal), phân cách bằng dấu hai chấm `:`.
  - Hỗ trợ 3 phương thức truyền: **유니캐스트 (Unicast - 1:1)**, **애니캐스트 (Anycast - 1:Gần nhất)**, **멀티캐스트 (Multicast - 1:Nhiều)**.
  - **핵심 포인트:** IPv6 **HOÀN TOÀN BÃI BỎ phương thức phát tán Quảng bá (Broadcast)**; thay thế bằng Multicast để chống bão mạng.

#### 5. Cấu trúc hình học mạng (Network Topologies) và Thiết bị phần cứng
- **5 Cấu trúc liên kết mạng cơ bản:**
  - **성형 (Star - Hình sao):** Tất cả các nút nối vào điểm trung tâm (Switch/Hub). Dễ cấu hình, dễ cô lập lỗi; nếu thiết bị trung tâm hỏng thì toàn mạng tê liệt.
  - **버스형 (Bus - Hình tuyến):** Dùng chung 1 đường trục cáp chính (Backbone) có trở đầu cuối (Terminator). Tiết kiệm dây cáp; nếu đứt đường trục thì toàn mạng gián đoạn.
  - **링형 (Ring - Hình vòng):** Các nút nối thành vòng tròn khép kín; dữ liệu truyền 1 chiều bằng thẻ bài Token.
  - **망형 (Mesh - Hình lưới toàn phần Full Mesh):** Mọi nút đều có đường nối dây cáp trực tiếp tới tất cả các nút còn lại:
    $$\text{Tổng số đường truyền} = \frac{n(n - 1)}{2}, \quad \text{Số cổng kết nối trên mỗi nút} = n - 1$$
- **Mạng định nghĩa bằng phần mềm (SDN - Software-Defined Networking):**
  - **Kiến trúc cốt lõi:** Tách rời hoàn toàn giữa Tầng điều khiển thông minh tập trung (**제어 평면 - Control Plane**) và Tầng chuyển tiếp dữ liệu phần cứng (**데이터 평면 - Data Plane / Forwarding**).
  - Giúp quản trị viên lập trình và điều hướng luồng giao thông toàn mạng một cách linh hoạt thông qua phần mềm tập trung mà không cần cấu hình thủ công từng Switch vật lý.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### Bài toán ví dụ chia mạng con Subnetting thực tế trong đề thi
- **Đề bài mẫu:** Cho dải địa chỉ mạng lớp C `192.168.1.0/24`. Công ty cần chia thành các mạng con với điều kiện: Mặt nạ mạng con mới là `255.255.255.224` (tương đương `/27`). Hãy tính:
  1. Số lượng mạng con tạo thành.
  2. Số lượng máy trạm (Host) tối đa có thể sử dụng trên mỗi mạng con.
  3. Dải địa chỉ IP khả dụng của mạng con đầu tiên.
- **Lời giải:**
  - Ta có Octet cuối của Subnet Mask là $224 = 128 + 64 + 32 = 11100000_2$.
  - Số bit mượn làm Subnet ID là $s = 3 \implies \text{Số mạng con} = 2^3 = 8\text{ mạng con}$.
  - Số bit Host còn lại là $h = 8 - 3 = 5\text{ bit}$.
  - Số máy trạm khả dụng mỗi mạng con: $2^h - 2 = 2^5 - 2 = 32 - 2 = 30\text{ máy trạm}$.
  - Mạng con đầu tiên có bước nhảy $2^5 = 32$:
    - Địa chỉ mạng (Network ID): `192.168.1.0`
    - Dải IP khả dụng cho máy trạm: `192.168.1.1` $\sim$ `192.168.1.30`
    - Địa chỉ quảng bá (Broadcast ID): `192.168.1.31`

---

### 복습 체크리스트
- [ ] Đọc vanh vách 7 tầng OSI và PDU: Vật lý (Bit) $\rightarrow$ Data Link (Frame) $\rightarrow$ Mạng (Packet) $\rightarrow$ Giao vận (Segment) $\rightarrow$ Phiên/Biểu diễn/Ứng dụng (Data).
- [ ] Phân biệt TCP vs UDP: TCP hướng kết nối, tin cậy, 3-Way Handshake, tiêu đề $\ge 20\text{B}$; UDP phi kết nối, không tin cậy, tiêu đề $8\text{B}$, tối ưu streaming.
- [ ] Phân biệt 3 giao thức định tuyến: RIP (Distance Vector, max 15 hops), OSPF (Link State, Dijkstra), BGP (Path Vector giữa các AS).
- [ ] Tính thành thạo Subnetting: Số host khả dụng $= 2^h - 2$ (loại trừ Network Address và Broadcast Address).
- [ ] Nắm vững đặc trưng IPv6: 128 bit, 8 nhóm Hexadecimal, hỗ trợ Unicast/Anycast/Multicast, không có Broadcast.
- [ ] Thuộc công thức Full Mesh: Số đường truyền $=\frac{n(n-1)}{2}$, số cổng mỗi nút $=n-1$.
- [ ] Hiểu nguyên lý cốt lõi của SDN: Tách rời Control Plane (điều khiển) và Data Plane (chuyển tiếp dữ liệu).
