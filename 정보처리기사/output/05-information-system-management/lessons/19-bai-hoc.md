# 네트워크 관련 장비 (Network Equipment)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, chức năng kỹ thuật và tầng hoạt động tương ứng trong mô hình OSI 7 tầng của các thiết bị phần cứng mạng: **NIC**, **Repeater (리피터)**, **Hub (허브)**, **Bridge (브리지)**, **Switch (스위치)**, **Router (라우터)**, và **Gateway (게이트웨이)**.
- Phân biệt sự khác biệt bản chất giữa thiết bị tầng 2 hoạt động bằng phần mềm (Bridge) và thiết bị chuyển mạch tầng 2 hoạt động bằng phần cứng chuyên dụng ASIC tốc độ cao (Switch).
- Hiểu chức năng định tuyến tìm đường tối ưu của Router ở tầng 3 (dựa trên địa chỉ IP) và chức năng chuyển đổi giao thức liên mạng của Gateway ở các tầng cao.

## 핵심 키워드 (Từ khóa)
- 네트워크 장비 (Network Hardware Devices)
- NIC (Network Interface Card - 랜카드, MAC 주소)
- 리피터 (Repeater - 1계층 신호 증폭 및 재생)
- 허브 (Hub - 더미 허브, 스위칭 허브)
- 브리지 (Bridge - 2계층 MAC 기반 LAN 연결)
- 스위치 (Switch - L2/L3/L4/L7 스위치, 하드웨어 ASIC)
- 라우터 (Router - 3계층 IP 기반 최적 경로 설정)
- 게이트웨이 (Gateway - 프로토콜 변환기)

## 선행·연결 개념 (Kiến thức liên kết)
- [18-bai-hoc.md](18-bai-hoc.md): Công nghệ mạng hạ tầng ảo hóa SDN và Cloud.
- [20-bai-hoc.md](20-bai-hoc.md): Cấu trúc liên kết mạng (Topologies) và chuẩn mạng cục bộ LAN.
- [44-bai-hoc.md](44-bai-hoc.md): Mô hình tham chiếu OSI 7 tầng và đơn vị dữ liệu PDU.

## 읽는 방법 (Cách đọc)
- Bản đồ tra cứu nhanh thiết bị theo tầng OSI trong đề thi:
  - **Tầng 1 (Physical):** **Repeater (리피터)** $\rightarrow$ Khuếch đại/tái sinh tín hiệu suy hao; **Hub (허브)** $\rightarrow$ Bộ chia cổng tập trung.
  - **Tầng 2 (Data Link):** **Bridge (브리지)** và **Switch (스위치)** $\rightarrow$ Chuyển tiếp khung dữ liệu (Frame) dựa trên địa chỉ vật lý **MAC**.
  - **Tầng 3 (Network):** **Router (라우터)** $\rightarrow$ Tìm đường đi tối ưu nhất (**최적 경로 설정**) dựa trên địa chỉ logic **IP**.
  - **Tầng 4 trở lên (Transport ~ Application):** **Gateway (게이트웨이)** $\rightarrow$ **Chuyển đổi giao thức (프로토콜 변환)** giữa hai mạng có cấu trúc hoàn toàn khác nhau.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng phân loại chi tiết các thiết bị mạng theo tầng OSI:**

| Tầng OSI | Thiết bị mạng | Cơ chế hoạt động & Chức năng kỹ thuật chi tiết |
| :---: | :--- | :--- |
| **Tầng 1** (Physical) | **NIC** (Card mạng LAN) | Kết nối vật lý giữa máy tính với cáp mạng; chứa địa chỉ MAC cố định do nhà sản xuất phần cứng nạp sẵn (48 bit). |
| **Tầng 1** (Physical) | **리피터** (Repeater) | Tiếp nhận các xung tín hiệu điện/sóng vô tuyến bị suy hao trên đường truyền dài, **khuếch đại và tái sinh lại dạng sóng gốc nguyên vẹn** để mở rộng cự ly truyền dẫn vật lý của mạng. |
| **Tầng 1** (Physical) | **허브** (Hub) | Thiết bị tập trung kết nối nhiều máy tính trong mạng LAN hình sao (Star); loại Dummy Hub phát tín hiệu đến tất cả các cổng (Broadcast), dễ gây xung đột tín hiệu (Collision). |
| **Tầng 2** (Data Link) | **브리지** (Bridge) | Kết nối hai phân đoạn mạng LAN cùng chuẩn giao thức; phân tích địa chỉ MAC nguồn và đích để quyết định lọc hay chuyển tiếp khung; hoạt động chủ yếu bằng **phần mềm**. |
| **Tầng 2** (Data Link) | **스위치** (Switch - L2) | Thiết bị chuyển mạch tốc độ cực cao sử dụng chip phần cứng chuyên dụng (**ASIC**); mỗi cổng của Switch tạo thành một miền xung đột riêng biệt (Collision Domain), loại bỏ hiện tượng đụng độ gói tin. |
| **Tầng 3** (Network) | **라우터** (Router) | Kết nối giữa các mạng khác nhau (LAN với WAN); dựa vào bảng định tuyến (Routing Table) và các thuật toán định tuyến để **lựa chọn đường đi ngắn nhất, tối ưu nhất** cho gói tin dựa trên địa chỉ **IP**. |
| **Tầng 4 ~ 7** (Upper Layers) | **게이트웨이** (Gateway) | Đóng vai trò là cửa ngõ giao tiếp, thực hiện **chuyển đổi cấu trúc giao thức truyền thông (Protocol Conversion)** giữa các hệ thống mạng hoàn toàn khác biệt nhau về mặt kiến trúc. |

- **2. Bảng phân cấp các loại thiết bị Switch hiện đại (L2 ~ L7):**

| Loại Switch | Tầng OSI | Căn cứ định tuyến / Chuyển mạch | Trường hợp ứng dụng |
| :---: | :---: | :--- | :--- |
| **L2 Switch** | Tầng 2 | Địa chỉ vật lý **MAC** | Phân phối khung trong mạng LAN nội bộ phòng ban. |
| **L3 Switch** | Tầng 3 | Địa chỉ logic **IP** | Kết hợp tốc độ phần cứng của Switch và khả năng định tuyến liên VLAN của Router. |
| **L4 Switch** | Tầng 4 | Địa chỉ IP + **Số hiệu cổng Port** (TCP/UDP) | Cân bằng tải máy chủ (Server Load Balancing) dựa trên dịch vụ (HTTP port 80, HTTPS port 443). |
| **L7 Switch** | Tầng 7 | Nội dung thông điệp ứng dụng (**URL, HTTP Header, Cookie**) | Phân tích sâu gói tin (DPI), tường lửa ứng dụng web (WAF), phòng chống tấn công DoS/DDoS. |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Phân biệt Miền xung đột (Collision Domain) vs Miền quảng bá (Broadcast Domain):**
  - *Hub:* Tất cả các cổng dùng chung 1 Collision Domain và 1 Broadcast Domain (khi máy A gửi thì tất cả các máy khác phải chờ, dễ nghẽn).
  - *Switch:* Mỗi cổng là 1 Collision Domain riêng biệt (các máy truyền nhận song song không đụng độ), nhưng tất cả các cổng vẫn chung 1 Broadcast Domain.
  - *Router:* Mỗi cổng của Router chia tách hoàn toàn cả Collision Domain lẫn Broadcast Domain riêng biệt (ngăn chặn bão quảng bá Broadcast Storm lan truyền ra toàn mạng).

### 복습 체크리스트
- [ ] Ghép đúng thiết bị với tầng OSI: Repeater (Tầng 1), Bridge/Switch (Tầng 2), Router (Tầng 3), Gateway (Tầng 4-7).
- [ ] Nhớ Repeater làm nhiệm vụ khuếch đại và tái sinh tín hiệu bị suy hao trên đường dài.
- [ ] Nhớ Router dùng địa chỉ IP để tìm đường đi tối ưu nhất (Routing).
- [ ] Nhớ Gateway làm nhiệm vụ chuyển đổi giao thức giữa các mạng khác cấu trúc.
- [ ] Phân biệt được: L4 Switch cân bằng tải theo Port, L7 Switch cân bằng tải theo nội dung URL/Cookie.
