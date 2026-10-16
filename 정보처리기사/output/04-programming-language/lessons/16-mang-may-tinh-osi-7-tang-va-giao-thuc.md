# 네트워크 통신, OSI 7계층 및 네트워크 프로토콜 (Mạng máy tính, OSI 7 tầng & Giao thức)

## 학습 목표 (Mục tiêu)
- Thuộc lòng 7 tầng của mô hình tham chiếu OSI theo khẩu quyết **물데네 전세표응** (Vật lý, Liên kết dữ liệu, Mạng, Giao vận, Phiên, Trình diễn, Ứng dụng) cùng đơn vị dữ liệu giao thức (PDU) và thiết bị phần cứng tương ứng ở từng tầng.
- Thấu hiểu và phân biệt chính xác chức năng của 4 giao thức mạng tầng Network cốt lõi trong đề thi: ARP (IP $\rightarrow$ MAC), RARP (MAC $\rightarrow$ IP), ICMP (báo cáo lỗi/ping), và IGMP (quản lý nhóm Multicast).
- Phân biệt hai giao thức định tuyến nội vùng (IGP) kinh điển: RIP (vectơ khoảng cách, đếm bước nhảy hop $\le 15$) và OSPF (trạng thái liên kết, giải thuật Dijkstra).

## 핵심 키워드 (Từ khóa)
- OSI 7계층 (OSI 7 Layers) — 물리, 데이터링크, 네트워크, 전송, 세션, 표현, 응용 (물데네 전세표응).
- 프로토콜 데이터 단위 (PDU) — Bit, Frame (L2 Switch), Packet (L3 Router), Segment (Gateway), Message.
- ARP vs RARP — Phân giải IP sang MAC vs Phân giải MAC sang IP.
- ICMP & IGMP — Báo cáo lỗi điều khiển mạng (Ping) vs Quản lý nhóm truyền thông đa hướng Multicast.
- 라우팅 프로토콜 (Routing Protocols) — RIP (거리 벡터, 15홉 제한) vs OSPF (링크 상태, 다익스트라).
- 표현 계층 (Presentation Layer) — Mã hóa bảo mật, nén dữ liệu và chuyển đổi định dạng mã ký tự.

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Hoàn tất toàn bộ khối kiến thức về Hệ điều hành đơn máy (OS); chuyển sang giao tiếp liên máy tính thông qua mạng viễn thông.
- **Đang giải quyết gì (Current Problem):** Giải quyết câu hỏi: Làm thế nào dữ liệu từ ứng dụng trên máy tính này có thể đóng gói, chuyển đổi và định tuyến chính xác qua hàng trăm thiết bị mạng trung gian để đến đúng ứng dụng trên máy tính khác.
- **Dùng đi đâu (Forward Handoff):** Sau khi gói tin đến tầng Mạng, việc đảm bảo truyền thông tin cậy không mất gói giữa 2 đầu cuối sẽ do tầng Giao vận đảm nhận qua bài `17-tang-giao-van-tcp-udp-va-kiem-soat-luong.md`.

## 읽는 방법 (Cách đọc)
- **Khẩu quyết 7 tầng:** Bắt buộc phải thuộc: **물·데·네 전·세·표·응** (물리 $\rightarrow$ 데이터링크 $\rightarrow$ 네트워크 $\rightarrow$ 전송 $\rightarrow$ 세션 $\rightarrow$ 표현 $\rightarrow$ 응용).
- **Khẩu quyết PDU (Đơn vị dữ liệu):** **비·프·패·세** (Bit $\rightarrow$ Frame $\rightarrow$ Packet $\rightarrow$ Segment).
- **Thiết bị:** Tầng 1: Hub/Repeater; Tầng 2: Switch/Bridge; Tầng 3: Router; Tầng 4: Gateway.
- **ARP vs RARP:** ARP là biến IP thành MAC; RARP là biến MAC thành IP.
- **RIP:** Giới hạn tối đa **15 Hop**, từ 16 Hop trở lên coi là không đến được.

---

## 네트워크 통신, OSI 7계층 및 네트워크 프로토콜

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [한국어]: `OSI 7계층의 PDU는 물리(비트), 데이터링크(프레임-스위치), 네트워크(패킷-라우터), 전송(세그먼트-게이트웨이)이다. ARP는 IP 주소를 MAC 주소로 변환하고, RARP는 MAC을 IP로 변환한다. RIP는 거리 벡터 기반으로 최대 15홉까지 지원하며, OSPF는 링크 상태 기반 다익스트라 알고리즘을 사용한다.`
  - [Tiếng Việt]: PDU của mô hình OSI gồm Vật lý (Bit), Data Link (Frame - Switch), Mạng (Packet - Router), Giao vận (Segment - Gateway). ARP chuyển đổi địa chỉ IP sang MAC, còn RARP chuyển MAC sang IP. RIP dựa trên vectơ khoảng cách hỗ trợ tối đa 15 hop, còn OSPF dựa trên trạng thái liên kết dùng giải thuật Dijkstra.

- **1. Bảng tổng hợp toàn diện Mô hình tham chiếu OSI 7 tầng (OSI 7계층 종합):**

| Tầng (Layer) | Tên tiếng Hàn & Anh | Đơn vị dữ liệu (PDU) | Thiết bị mạng đại diện | Chức năng kỹ thuật cốt lõi chuẩn khảo thí |
| :---: | :--- | :---: | :--- | :--- |
| **Tầng 7** | **응용 계층** (Application) | Data / Message | — | Giao diện cho người dùng và ứng dụng: HTTP, FTP, SMTP, DNS. |
| **Tầng 6** | **표현 계층** (Presentation)| Data | — | **Mã hóa/Giải mã bảo mật, Nén dữ liệu**, chuyển đổi mã (ASCII, SSL). |
| **Tầng 5** | **세션 계층** (Session) | Data | — | Thiết lập, duy trì, **đồng bộ hóa điểm kiểm tra (Checkpoint)** phiên đàm thoại. |
| **Tầng 4** | **전송 계층** (Transport) | **세그먼트 (Segment)** | **Gateway** | Truyền thông tin cậy đầu cuối (End-to-End), kiểm soát luồng/lỗi: TCP, UDP. |
| **Tầng 3** | **네트워크 계층** (Network) | **패킷 (Packet)** | **Router (L3)** | **Định tuyến đường đi (Routing)**, gán địa chỉ logic: IP, ICMP, ARP. |
| **Tầng 2** | **데이터링크 계층** (Data Link)| **프레임 (Frame)** | **Switch (L2), Bridge** | Truyền không lỗi giữa 2 nút kề nhau qua địa chỉ vật lý MAC; Ethernet. |
| **Tầng 1** | **물리 계층** (Physical) | **비트 (Bit)** | **Hub, Repeater** | Truyền tải chuỗi bit thô 0/1 qua tín hiệu điện, quang học; cáp mạng. |

- **2. Bảng 4 giao thức then chốt ở Tầng Network (네트워크 계층 핵심 프로토콜):**

| Tên giao thức | Tên tiếng Anh đầy đủ | Bản chất kỹ thuật & Câu hỏi thi thường gặp |
| :--- | :--- | :--- |
| **ARP** | **Address Resolution Protocol** | **Chuyển đổi từ địa chỉ logic IP sang địa chỉ vật lý MAC (NIC).** Máy tính phát sóng quảng bá (Broadcast) để hỏi MAC của IP đích. |
| **RARP** | **Reverse ARP** | **Chuyển đổi ngược từ địa chỉ vật lý MAC sang địa chỉ IP.** Dùng cho các máy trạm không có ổ cứng (Diskless Workstation) khi khởi động. |
| **ICMP** | **Internet Control Message Protocol** | **Báo cáo lỗi và gửi thông điệp điều khiển trạng thái mạng.** Lệnh `ping` và `traceroute` sử dụng các gói tin ICMP Echo Request / Reply. |
| **IGMP** | **Internet Group Management Protocol**| **Quản lý tư cách thành viên nhóm truyền thông đa hướng (Multicast).** Dùng giữa máy chủ và Router cục bộ để quản lý nhóm nhận gói. |

- **3. Bảng đối chiếu hai giao thức định tuyến nội vùng: RIP vs OSPF:**

| Tiêu chuẩn so sánh | RIP (Routing Information Protocol) | OSPF (Open Shortest Path First) |
| :--- | :--- | :--- |
| **Thuật toán cốt lõi** | **Vectơ khoảng cách (거리 벡터 - Distance Vector)** dựa trên giải thuật Bellman-Ford. | **Trạng thái liên kết (링크 상태 - Link State)** dựa trên giải thuật Dijkstra (SPF). |
| **Thước đo định tuyến** | **Số bước nhảy (홉 수 - Hop Count)**. | Băng thông, độ trễ và chi phí liên kết (Cost). |
| **Giới hạn quy mô mạng**| **Tối đa 15 Hop** (Hop thứ 16 coi là không đến được); chỉ phù hợp mạng nhỏ. | **Không giới hạn bước nhảy**; chia vùng Autonomous System (AS) phân cấp. |
| **Chu kỳ cập nhật** | Cập nhật định kỳ toàn bộ bảng định tuyến mỗi **30 giây** bằng Broadcast. | Chỉ cập nhật tức thì khi có biến động liên kết bằng Multicast. |

- **주의/함정 (Bẫy đề thi):**
  - **Giới hạn 15 Hop của RIP:** Đề thi khẳng định *"RIP hỗ trợ tối đa 30 Hop cho mạng doanh nghiệp lớn"* $\rightarrow$ **SAI HOÀN TOÀN**; RIP giới hạn cứng 15 Hop.
  - **Chức năng tầng Presentation:** Nén dữ liệu (압축) và Mã hóa (암호화) luôn luôn thuộc trách nhiệm của **Tầng 6 (표현 계층 - Presentation)**, không thuộc tầng ứng dụng.
  - **Thiết bị hoạt động ở tầng nào:** L2 Switch ở Tầng 2 (xử lý MAC); Router ở Tầng 3 (xử lý IP); Repeater ở Tầng 1 (khuếch đại tín hiệu bit).

- **한 문장 설명 (Câu chốt tự nhớ):**
  - *"물데네 전세표응 7 tầng, 비프패세 4 PDU; ARP đổi IP ra MAC, RIP đếm hop tối đa mười lăm (15)."*

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Quy trình phân giải địa chỉ mạng của giao thức ARP:
1. Máy nguồn muốn gửi gói tin cho IP đích `192.168.1.50` nhưng chưa biết địa chỉ MAC của máy đích.
2. Máy nguồn gửi một gói tin **ARP Request** quảng bá (Broadcast: `FF:FF:FF:FF:FF:FF`) đến toàn bộ mạng LAN: *"Ai đang sở hữu IP 192.168.1.50, hãy trả lời địa chỉ MAC cho tôi!"*.
3. Mọi máy tính nhận được gói tin đều kiểm tra; chỉ duy nhất máy tính có IP `192.168.1.50` phản hồi bằng gói tin **ARP Reply** đơn hướng (Unicast) chứa địa chỉ MAC thực tế của nó.
4. Máy nguồn lưu kết quả vào bảng tạm **ARP Cache** để sử dụng cho các lần gửi tiếp theo.

#### 2. Minh họa lệnh kiểm tra kết nối mạng với ICMP (`ping`):
```bash
# Gui 4 goi tin ICMP Echo Request den may chu DNS cua Google
ping -c 4 8.8.8.8

# Ket qua phan hoi:
# 64 bytes from 8.8.8.8: icmp_seq=1 ttl=116 time=14.2 ms
# 64 bytes from 8.8.8.8: icmp_seq=2 ttl=116 time=13.8 ms
# Nhan duoc ICMP Echo Reply -> Mang hoat dong binh thuong
```

#### 3. Bảng so sánh các tầng thiết bị mạng và giao thức truyền thông:

| Thiết bị mạng | Tầng OSI tương ứng | Thông tin bóc tách xử lý |
| :--- | :---: | :--- |
| **Repeater / Hub** | **Tầng 1 (Vật lý)** | Khuếch đại và tái tạo dạng sóng tín hiệu điện thô (Bit). |
| **Bridge / L2 Switch** | **Tầng 2 (Data Link)** | Đọc bảng địa chỉ vật lý MAC để chuyển tiếp khung (Frame). |
| **Router / L3 Switch** | **Tầng 3 (Network)** | Đọc bảng định tuyến IP để chọn đường đi tối ưu cho gói tin (Packet). |
| **Gateway / L7 Firewall**| **Tầng 4 – 7 (Cao cấp)** | Chuyển đổi giao thức khác biệt hoàn toàn giữa 2 mạng độc lập. |

---

### 복습 체크리스트
- [ ] Thuộc lòng 7 tầng OSI: **물데네 전세표응** (물리, 데이터링크, 네트워크, 전송, 세션, 표현, 응용).
- [ ] Thuộc lòng 4 đơn vị PDU: **비프패세** (Bit, Frame, Packet, Segment).
- [ ] Nhớ thiết bị từng tầng: Tầng 1 (Hub/Repeater), Tầng 2 (Switch/Bridge), Tầng 3 (Router), Tầng 4 (Gateway).
- [ ] Phân biệt được: ARP (IP $\rightarrow$ MAC) vs RARP (MAC $\rightarrow$ IP).
- [ ] Nhớ ICMP dùng báo lỗi (lệnh `ping`), IGMP dùng quản lý nhóm Multicast.
- [ ] Thuộc lòng đặc trưng RIP: Vectơ khoảng cách, đếm bước nhảy Hop $\le 15$.
