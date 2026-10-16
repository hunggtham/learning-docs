# 네트워크 구조, OSI 7계층 및 TCP/IP 프로토콜 (Kiến trúc mạng máy tính, Topo, CSMA/CD & CD/CA, OSI 7 tầng & TCP/IP)

## 학습 목표 (Mục tiêu)
- Phân biệt cấu trúc phân loại mạng theo phạm vi địa lý: **LAN** (Mạng cục bộ), **MAN** (Mạng đô thị), và **WAN** (Mạng diện rộng).
- Làm chủ 5 cấu trúc topo mạng: **Star** (Hình sao), **Bus** (Hình tuyến), **Ring** (Hình vòng), **Tree** (Hình cây), và **Mesh** (Hình lưới toàn phần với công thức đường truyền $n(n-1)/2$).
- Nắm vững bản chất cơ chế truy cập đường truyền Ethernet **CSMA/CD** (Carrier Sense, Multiple Access, Collision Detection kèm thuật toán lùi lũy thừa nhị phân Binary Exponential Backoff) và mạng không dây Wi-Fi **CSMA/CA** (Collision Avoidance với RTS/CTS).
- Nắm vững kiến trúc phân tầng, chức năng kỹ thuật, đơn vị dữ liệu (PDU) và thiết bị của **Mô hình OSI 7 tầng** theo khẩu quyết **물데네전세표응**.
- So sánh sự khác nhau giữa **TCP** (hướng kết nối, tin cậy, 3-Way Handshake) và **UDP** (phi kết nối, tiêu đề 8 Byte, tối ưu streaming), cùng 3 giao thức định tuyến: **RIP**, **OSPF**, **BGP**.
- Giải thành thạo bài toán chia mạng con (**Subnetting**): Mặt nạ mạng con, Địa chỉ mạng, Địa chỉ quảng bá và Số lượng máy trạm khả dụng ($2^h - 2$).

## 핵심 키워드 (Từ khóa song ngữ)
- 네트워크 분류 (LAN 근거리 통신망, MAN 도시권 통신망, WAN 광역 통신망)
- 네트워크 토폴로지 (Topologies — 성형 Star, 버스형 Bus, 링형 Ring, 트리형 Tree, 망형 Mesh $\frac{n(n-1)}{2}$)
- CSMA/CD (Ethernet 유선망 — 반이중, 반송파 감지, 다중 접근, 충돌 검출, Jam 신호, 백오프 Backoff)
- CSMA/CA (Wi-Fi 무선망 — 충돌 회피, RTS/CTS 프레임 교환, 숨겨진 노드 문제 해결)
- OSI 7계층 (OSI 7 Layers — 물데네전세표응: 물리, 데이터링크, 네트워크, 전송, 세션, 표현, 응용)
- PDU (Protocol Data Unit — 비트 Bit, 프레임 Frame, 패킷 Packet, 세그먼트 Segment, 데이터 Data)
- TCP vs UDP (TCP 연결지향 신뢰성 20B 헤더 vs UDP 비연결 비신뢰 8B 헤더)
- 라우팅 프로토콜 (Routing — RIP 거리벡터 15홉 vs OSPF 링크상태 다익스트라 vs BGP 경로벡터)
- IPv4 서브네팅 (IPv4 Subnetting — 서브넷 마스크, 가용 호스트 $2^h - 2$)
- IPv6 (128비트, 유니캐스트, 애니캐스트, 멀티캐스트, 브로드캐스트 전면 폐지)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Từ các tín hiệu vật lý, kỹ thuật Baseband/Broadband và điều chế sóng tại [11-truyen-thong-du-lieu-va-dieu-che.md](11-truyen-thong-du-lieu-va-dieu-che.md), dữ liệu cần được đóng gói thành các cấu trúc tầng logic và điều phối quyền truy cập đường truyền chung.
- **Đang giải quyết gì (Current Problem):** Bài học này xây dựng bức tranh toàn cảnh về kiến trúc mạng viễn thông: từ phân loại quy mô LAN/MAN/WAN, các hình thái topo, cơ chế truy cập môi trường CSMA/CD và CSMA/CA, mô hình tham chiếu chuẩn OSI 7 tầng, phân tích chi tiết họ giao thức TCP/IP cho đến tính toán chia mạng con IPv4.
- **Dùng đi đâu (Forward Handoff):** Các gói tin sau khi được định tuyến tới máy chủ đích sẽ được hệ điều hành tiếp nhận, đưa vào hàng đợi tiến trình và lập lịch CPU tại [13-he-dieu-hanh-tien-trinh-va-dieu-phoi.md](13-he-dieu-hanh-tien-trinh-va-dieu-phoi.md).

## 읽는 방법 (Cách đọc & Dấu hiệu nhận diện đề thi)
- **Quy mô mạng & Topo:**
  - Phạm vi nhỏ trong một tòa nhà, tốc độ cao, tỷ lệ lỗi cực thấp $\rightarrow$ **LAN (근거리 통신망)**.
  - Phạm vi liên quốc gia, châu lục, qua nhà mạng viễn thông $\rightarrow$ **WAN (광역 통신망)**.
  - Số đường truyền mạng lưới toàn phần Full Mesh $\rightarrow$ Công thức: $\frac{n(n-1)}{2}$.
- **CSMA/CD vs CSMA/CA:**
  - Nhắc đến mạng Ethernet có dây, phát hiện xung điện áp va chạm rồi gửi tín hiệu Jam và chạy thuật toán Backoff $\rightarrow$ **CSMA/CD**.
  - Nhắc đến mạng không dây Wi-Fi, phòng tránh va chạm do vấn đề nút ẩn, dùng khung điều khiển RTS/CTS $\rightarrow$ **CSMA/CA**.
- **Thứ tự 7 tầng OSI (Khẩu quyết vàng):**
  - **물 (Vật lý - 1) $\rightarrow$ 데 (Liên kết dữ liệu - 2) $\rightarrow$ 네 (Mạng - 3) $\rightarrow$ 전 (Giao vận - 4) $\rightarrow$ 세 (Phiên - 5) $\rightarrow$ 표 (Trình diễn - 6) $\rightarrow$ 응 (Ứng dụng - 7)**.
  - PDU tương ứng: **Bit (1) $\rightarrow$ Frame (2) $\rightarrow$ Packet (3) $\rightarrow$ Segment (4) $\rightarrow$ Data (5, 6, 7)**.
- **TCP vs UDP:**
  - Hướng kết nối, tin cậy, 3-Way Handshake, kiểm soát luồng $\rightarrow$ **TCP**.
  - Phi kết nối, không tin cậy, tiêu đề cố định 8 Byte, streaming $\rightarrow$ **UDP**.
- **Định tuyến:**
  - **RIP:** 거리 벡터 (Distance Vector), dùng Hop Count, tối đa 15 hop.
  - **OSPF:** 링크 상태 (Link State), dùng Dijkstra tìm đường ngắn nhất, phân chia Area.
  - **BGP:** 경로 벡터 (Path Vector), giao thức giữa các hệ tự trị AS toàn cầu.
- **Subnetting:**
  - Số máy trạm khả dụng luôn là **$2^h - 2$** (trừ Network ID và Broadcast ID).

---

## 네트워크 구조, OSI 7계층 및 TCP/IP 프로토콜

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Cấu trúc phân loại mạng và Topo mạng (Network Topologies)
- **Phân loại mạng theo phạm vi địa lý:**
  - **LAN (Local Area Network - 근거리 통신망):** Mạng nội bộ trong phạm vi hẹp (văn phòng, tòa nhà); tốc độ truyền cao (100Mbps - 10Gbps), tỷ lệ lỗi bit cực thấp; do một tổ chức duy nhất sở hữu và quản trị.
  - **MAN (Metropolitan Area Network - 도시권 통신망):** Mạng bao phủ phạm vi một thành phố, đô thị (vài km đến vài chục km); chuẩn tiêu biểu IEEE 802.6 DQDB.
  - **WAN (Wide Area Network - 광역 통신망):** Mạng diện rộng kết nối xuyên quốc gia, châu lục; tốc độ truyền phụ thuộc đường truyền viễn thông, tỷ lệ lỗi cao hơn; do các nhà cung cấp dịch vụ Internet (ISP) vận hành.
- **5 Cấu trúc hình học liên kết mạng cơ bản:**

| Cấu trúc Topo | Tên tiếng Hàn & Anh | Cơ chế vận hành & Điểm thi trọng tâm |
| :--- | :--- | :--- |
| **Hình sao** | **성형 (Star)** | Tất cả các nút máy trạm nối độc lập vào một thiết bị trung tâm (Hub/Switch). Dễ lắp đặt, dễ cô lập điểm lỗi; nếu thiết bị trung tâm hỏng thì toàn bộ mạng ngừng hoạt động. |
| **Hình tuyến** | **버스형 (Bus)** | Tất cả các nút cùng chia sẻ một đường cáp trục chính (Backbone) có trở đầu cuối (Terminator) hấp thụ sóng phản xạ. Tiết kiệm dây cáp; nếu đường trục chính bị đứt thì toàn mạng gián đoạn. |
| **Hình vòng** | **링형 (Ring)** | Các nút nối tiếp nhau thành một vòng tròn khép kín; dữ liệu truyền theo một chiều xác định thông qua thẻ bài điều khiển (Token Ring). |
| **Hình cây** | **트리형 / 계층형 (Tree)** | Mở rộng từ hình sao theo cấu trúc cây phân cấp nhiều tầng; dễ dàng quản trị và mở rộng hệ thống mạng theo phòng ban. |
| **Hình lưới toàn phần** | **망형 (Full Mesh)** | Mọi nút mạng đều có một đường nối cáp trực tiếp tới tất cả các nút còn lại; độ tin cậy và khả năng chịu lỗi cao nhất nhưng tốn chi phí dây cáp lớn nhất. |

- **Công thức tính toán mạng lưới toàn phần Full Mesh:**
  $$\text{Tổng số đường truyền} = \frac{n(n - 1)}{2}, \quad \text{Số cổng kết nối trên mỗi nút} = n - 1$$

#### 2. Cơ chế điều khiển truy cập đường truyền: CSMA/CD vs CSMA/CA
Khi nhiều máy tính cùng chia sẻ một môi trường truyền thông chung, cần có cơ chế tránh xung đột tín hiệu:

- **CSMA/CD (Carrier Sense Multiple Access with Collision Detection):**
  - Sử dụng trong mạng Ethernet có dây (chuẩn IEEE 802.3), hoạt động ở chế độ bán song công (Half-duplex).
  - **Carrier Sense (Nghe sóng mang):** Trước khi phát, nút mạng lắng nghe đường truyền xem có tín hiệu của máy khác hay không. Nếu rảnh thì phát dữ liệu.
  - **Multiple Access (Đa truy nhập):** Nhiều nút mạng có quyền truy cập đồng đẳng vào đường truyền chung.
  - **Collision Detection (Phát hiện va chạm):** Trong lúc đang phát dữ liệu, nút mạng vừa phát vừa liên tục đo điện áp đường truyền. Nếu hai máy cùng phát đồng thời gây va chạm (Collision):
    1. Lập tức ngừng truyền gói tin và phát một chuỗi tín hiệu kẹt tín hiệu (**Jam Signal**) để báo động cho tất cả các máy khác trên đường truyền biết va chạm đã xảy ra.
    2. Áp dụng **Thuật toán lùi lũy thừa nhị phân (Binary Exponential Backoff Algorithm)**: Tạm dừng và chờ một khoảng thời gian ngẫu nhiên trước khi thử lắng nghe và phát lại.
- **CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance):**
  - Sử dụng trong mạng không dây Wi-Fi (chuẩn IEEE 802.11).
  - Do đặc thù sóng vô tuyến không thể vừa phát vừa nghe để phát hiện va chạm (vấn đề nút ẩn - Hidden Node Problem), giao thức chuyển sang **Phòng tránh va chạm (Collision Avoidance)**:
    - Lắng nghe đường truyền rảnh trong khoảng thời gian xác định DIFS (Distributed Inter-Frame Space).
    - Sử dụng cơ chế bắt tay bằng các khung điều khiển nhỏ: Máy gửi gửi khung **RTS (Request to Send)**; Máy nhận phản hồi khung **CTS (Clear to Send)**. Tất cả các máy khác nhận được CTS sẽ tạm ngưng phát dữ liệu trong khoảng thời gian đã được thông báo.

#### 3. Mô hình tham chiếu OSI 7 tầng (ISO 7498)

| Tầng OSI | Tên tiếng Hàn & Anh | Đơn vị dữ liệu (PDU) | Chức năng kỹ thuật cốt lõi | Thiết bị mạng tương ứng |
| :---: | :--- | :---: | :--- | :--- |
| **Tầng 7** | **응용 (Application)** | **Data / Message** | Giao diện trực tiếp cung cấp dịch vụ mạng cho người dùng cuối (HTTP, FTP, SMTP, DNS). | Gateway, L7 Switch, WAF |
| **Tầng 6** | **표현 (Presentation)** | **Data / Message** | Định dạng dữ liệu, chuyển đổi bảng mã (ASCII, EBCDIC), nén dữ liệu và **Mã hóa / Giải mã (Encryption)**. | Gateway |
| **Tầng 5** | **세션 (Session)** | **Data / Message** | Thiết lập, duy trì và giải phóng phiên giao tiếp; quản lý **Điểm đồng bộ (Synchronization Points: Major/Minor)** để phục hồi khi đứt kết nối. | Gateway |
| **Tầng 4** | **전송 (Transport)** | **세그먼트 (Segment)** | Đảm bảo truyền dữ liệu đầu cuối tới đầu cuối (**End-to-End**) tin cậy; đánh số cổng (**Port**); kiểm soát luồng, kiểm soát lỗi và phân mảnh. | **L4 Switch** |
| **Tầng 3** | **네트워크 (Network)** | **패킷 (Packet)** | Định tuyến đường đi tốt nhất qua mạng (**Routing**); đánh địa chỉ logic (**IP**); kiểm soát tắc nghẽn liên mạng. | **Router, L3 Switch** |
| **Tầng 2** | **데이터 링크 (Data Link)** | **프레임 (Frame)** | Truyền dữ liệu tin cậy giữa hai nút lân cận trên cùng đường truyền vật lý; đánh địa chỉ vật lý (**MAC**); kiểm soát lỗi khung (CRC). | **Bridge, L2 Switch, NIC** |
| **Tầng 1** | **물리 (Physical)** | **비트 (Bit)** | Chuyển đổi chuỗi bit nhị phân thành tín hiệu điện/quang và truyền qua dây cáp vật lý. | **Repeater, Hub** |

#### 4. Đối chiếu hai giao thức tầng giao vận: TCP vs UDP

| Đặc tính kỹ thuật | Giao thức TCP (Transmission Control Protocol) | Giao thức UDP (User Datagram Protocol) |
| :--- | :--- | :--- |
| **Phương thức kết nối** | **연결 지향 (Connection-Oriented)**; thiết lập kết nối trước bằng bắt tay 3 bước (**3-Way Handshake**). | **비연결 지향 (Connectionless)**; gửi trực tiếp không cần thiết lập kết nối trước. |
| **Độ tin cậy** | **Rất cao**; bảo đảm dữ liệu đến đích nguyên vẹn, đúng thứ tự tuần tự; tự động yêu cầu truyền lại khi mất gói. | **Không đảm bảo (Best-effort)**; gói tin có thể bị mất, trùng lặp hoặc đến đích sai thứ tự. |
| **Kích thước tiêu đề** | Tiêu đề lớn, tối thiểu **20 Byte** (có thể mở rộng đến 60 Byte). | Tiêu đề siêu nhẹ, cố định chỉ **8 Byte** (Source Port, Dest Port, Length, Checksum). |
| **Cơ chế kiểm soát** | Có cơ chế **Kiểm soát luồng (Sliding Window)** và **Kiểm soát tắc nghẽn (Congestion Control)**. | **Không có kiểm soát luồng và tắc nghẽn**; tốc độ xả gói tin tối đa theo khả năng ứng dụng. |
| **Ứng dụng tiêu biểu** | Truyền tệp tin (**FTP**), Tải trang web (**HTTP/HTTPS**), Gửi nhận thư điện tử (**SMTP, POP3**). | Truyền phát video trực tiếp (Streaming), Thoại Internet (**VoIP**), Tra cứu tên miền (**DNS**), Giám sát mạng (**SNMP**). |

#### 5. Các giao thức định tuyến cốt lõi (Routing Protocols)

| Giao thức định tuyến | Thuật toán định tuyến cốt lõi | Metric đo lường & Giới hạn quy mô | Đặc điểm vận hành trong đề thi |
| :--- | :--- | :--- | :--- |
| **RIP** | **거리 벡터 (Distance Vector)** dựa trên thuật toán Bellman-Ford | Số bước nhảy (**Hop Count**); **Giới hạn tối đa 15 Hop** (16 Hop coi là đích không thể tới). | Định kỳ mỗi 30 giây phát tán Broadcast toàn bộ bảng định tuyến cho các router lân cận; chỉ phù hợp cho mạng quy mô nhỏ. |
| **OSPF** | **링크 상태 (Link State)** dựa trên thuật toán Dijkstra SPF | Băng thông đường truyền (**Cost**); không giới hạn số bước nhảy. | Phân chia mạng thành các vùng (**Area**); chỉ gửi gói tin cập nhật khi mạng có sự thay đổi trạng thái đường truyền; phù hợp mạng doanh nghiệp lớn. |
| **BGP** | **경로 벡터 (Path Vector)** | Chính sách định tuyến mạng và danh sách các hệ tự trị AS. | Giao thức định tuyến ngoài (**EGP**) kết nối giữa các nhà mạng viễn thông và hệ thống tự trị **AS (Autonomous System)** trên toàn cầu. |

#### 6. Địa chỉ IPv4, Kỹ thuật chia mạng con và Thế hệ IPv6
- **Công thức tính toán Subnetting:**
  - Nếu mượn $s$ bit từ phần Host ID làm Subnet ID $\rightarrow$ Số mạng con tạo thành $= 2^s$.
  - Số bit còn lại trong phần Host ID là $h$ bit $\rightarrow$ Số lượng địa chỉ IP khả dụng gán cho máy trạm:
    $$\text{Số Host khả dụng} = 2^h - 2$$
  - *(Trừ 2 vì địa chỉ toàn bit 0 là Network Address, địa chỉ toàn bit 1 là Broadcast Address).*
- **Đặc trưng của thế hệ IPv6 (128-bit):**
  - Độ dài 128 bit, biểu diễn bằng 8 nhóm số thập lục phân (Hexadecimal), phân cách bằng dấu hai chấm `:`.
  - Hỗ trợ 3 phương thức truyền: **유니캐스트 (Unicast - 1:1)**, **애니캐스트 (Anycast - 1:Gần nhất)**, **멀티캐스트 (Multicast - 1:Nhiều)**.
  - **핵심 포인트:** IPv6 **HOÀN TOÀN BÃI BỎ phương thức phát tán Quảng bá (Broadcast)**; thay thế bằng Multicast để chống bão mạng.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### Bài toán ví dụ chia mạng con Subnetting thực tế trong đề thi
- **Đề bài mẫu:** Cho dải địa chỉ mạng lớp C `192.168.1.0/24`. Công ty cần chia thành các mạng con với Mặt nạ mạng con mới là `255.255.255.224` (tương đương `/27`).
- **Lời giải:**
  - Octet cuối của Subnet Mask là $224 = 128 + 64 + 32 = 11100000_2$.
  - Số bit mượn làm Subnet ID là $s = 3 \implies \text{Số mạng con} = 2^3 = 8\text{ mạng con}$.
  - Số bit Host còn lại là $h = 8 - 3 = 5\text{ bit}$.
  - Số máy trạm khả dụng mỗi mạng con: $2^h - 2 = 2^5 - 2 = 32 - 2 = 30\text{ máy trạm}$.
  - Mạng con đầu tiên có bước nhảy $2^5 = 32$:
    - Địa chỉ mạng (Network ID): `192.168.1.0`
    - Dải IP khả dụng cho máy trạm: `192.168.1.1` $\sim$ `192.168.1.30`
    - Địa chỉ quảng bá (Broadcast ID): `192.168.1.31`

---

### 복습 체크리스트
- [ ] Phân biệt quy mô mạng: LAN (nội bộ, tốc độ cao), MAN (đô thị), WAN (diện rộng viễn thông).
- [ ] Thuộc công thức Full Mesh: Số đường truyền $=\frac{n(n-1)}{2}$, số cổng mỗi nút $=n-1$.
- [ ] Phân biệt CSMA/CD (Ethernet có dây, phát hiện xung đột, phát tín hiệu Jam, lùi lũy thừa nhị phân) vs CSMA/CA (Wi-Fi không dây, phòng tránh va chạm qua RTS/CTS).
- [ ] Đọc vanh vách 7 tầng OSI và PDU: Vật lý (Bit) $\rightarrow$ Data Link (Frame) $\rightarrow$ Mạng (Packet) $\rightarrow$ Giao vận (Segment) $\rightarrow$ Phiên/Biểu diễn/Ứng dụng (Data).
- [ ] Phân biệt TCP vs UDP: TCP hướng kết nối, tin cậy, 3-Way Handshake, tiêu đề $\ge 20\text{B}$; UDP phi kết nối, tiêu đề $8\text{B}$, tối ưu streaming.
- [ ] Phân biệt 3 giao thức định tuyến: RIP (Distance Vector, max 15 hops), OSPF (Link State, Dijkstra), BGP (Path Vector giữa các AS).
- [ ] Tính thành thạo Subnetting: Số host khả dụng $= 2^h - 2$ (loại trừ Network Address và Broadcast Address).
- [ ] Nắm vững đặc trưng IPv6: 128 bit, 8 nhóm Hexadecimal, hỗ trợ Unicast/Anycast/Multicast, không có Broadcast.
