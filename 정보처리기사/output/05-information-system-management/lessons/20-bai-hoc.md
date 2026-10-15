# 네트워크 구조 및 기술 (Network Structures & Technologies)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, sơ đồ hình học, ưu nhược điểm và trường hợp ứng dụng của 5 cấu trúc liên kết mạng cơ bản (**네트워크 토폴로지 - Network Topologies**): Hình sao (**성형 - Star**), Hình vòng (**링형 - Ring**), Hình tuyến (**버스형 - Bus**), Hình cây (**계층형 - Tree**), và Hình lưới (**망형 - Mesh**).
- Thuộc lòng công thức tính toán số lượng đường truyền vật lý trong mạng lưới toàn phần (Full Mesh): $\frac{n(n-1)}{2}$ và số lượng cổng giao tiếp trên mỗi nút mạng ($n - 1$).
- Nhận diện các bộ tiêu chuẩn mạng cục bộ kinh điển của ủy ban IEEE 802: **IEEE 802.3** (Mạng Ethernet / CSMA/CD) và **IEEE 802.11** (Mạng cục bộ không dây Wi-Fi).

## 핵심 키워드 (Từ khóa)
- 네트워크 토폴로지 (Network Topologies)
- 성형 / 중앙 집중형 (Star Topology - Point-to-Point, 중앙 노드 고장 위험)
- 링형 / 루프형 (Ring Topology - 토큰 링, 단방향 루프)
- 버스형 (Bus Topology - 단일 회선 공유, 종단 저항기 Terminator)
- 망형 / 메시형 (Mesh Topology - 완전 연결망 공식 $n(n-1)/2$)
- IEEE 802 표준 (IEEE 802.3 이더넷, IEEE 802.11 무선랜 Wi-Fi)

## 선행·연결 개념 (Kiến thức liên kết)
- [19-bai-hoc.md](19-bai-hoc.md): Các thiết bị phần cứng mạng viễn thông (Hub, Switch, Router).
- [21-bai-hoc.md](21-bai-hoc.md): Kỹ thuật đa truy cập môi trường CSMA/CD và giao thức điều khiển mạng.
- [43-bai-hoc.md](43-bai-hoc.md): Phân loại mạng theo cự ly địa lý (LAN, MAN, WAN) và thiết bị định tuyến.

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh đặc điểm thi cử của từng cấu trúc Topology:
  - **성형 (Star - Hình sao):** Tất cả các máy tính nối về **một thiết bị trung tâm (Hub/Switch)** $\rightarrow$ Điểm chết duy nhất (Single Point of Failure): Thiết bị trung tâm hỏng thì toàn mạng tê liệt.
  - **링형 (Ring - Hình vòng):** Nối tiếp nhau thành vòng tròn $\rightarrow$ Dùng cơ chế **thẻ bài (Token Passing)**, nếu vòng đơn bị đứt 1 đoạn thì toàn bộ mạng bị gián đoạn.
  - **버스형 (Bus - Hình tuyến):** Dùng chung **1 đường cáp trục chính (Backbone)** $\rightarrow$ Bắt buộc phải có **bộ kết thúc điện trở (Terminator - 종단기)** ở 2 đầu để triệt tiêu sóng phản xạ.
  - **망형 (Mesh - Hình lưới):** Mọi nút nối trực tiếp với nhau $\rightarrow$ Độ tin cậy cao nhất nhưng tốn cáp nhất; thuộc lòng công thức số đường truyền: $\mathbf{\frac{n(n-1)}{2}}$.
  - **Chuẩn IEEE:** Thuộc làu **IEEE 802.3 là Ethernet**, còn **IEEE 802.11 là Wi-Fi**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng đối chiếu 5 cấu trúc liên kết mạng (Network Topologies):**

| Cấu trúc mạng | Sơ đồ liên kết vật lý | Ưu điểm kỹ thuật nổi bật | Nhược điểm & Rủi ro then chốt |
| :--- | :--- | :--- | :--- |
| **성형 (Star / Hình sao)** | Tất cả các máy trạm kết nối độc lập về một **nút trung tâm (Central Node / Hub, Switch)** theo dạng điểm-điểm. | Dễ lắp đặt cáp; dễ dàng bổ sung hoặc tháo gỡ máy tính mà không làm gián đoạn mạng; khi 1 máy trạm hỏng thì các máy khác vẫn hoạt động bình thường. | **Nếu nút trung tâm (Hub/Switch) bị hỏng thì toàn bộ hệ thống mạng bị tê liệt hoàn toàn** (Single Point of Failure). |
| **링형 (Ring / Hình vòng)** | Các nút mạng được kết nối nối tiếp với nhau thành một **vòng tròn khép kín (Loop)**; tín hiệu truyền theo 1 chiều qua thẻ bài (Token). | Không xảy ra hiện tượng đụng độ xung đột gói tin (Collision-free); hiệu năng ổn định ngay cả khi tải mạng lớn. | Thêm bớt một máy tính rất phức tạp; **nếu một điểm nút trên vòng bị đứt thì toàn mạng bị tê liệt** (khắc phục bằng vòng kép Dual-Ring). |
| **버스형 (Bus / Tuyến tính)** | Tất cả các nút mạng cùng chia sẻ chung một **đường cáp trục chính duy nhất (Backbone)**; hai đầu cáp gắn **Terminator (종단기)**. | Cấu trúc rất đơn giản, tốn ít chiều dài cáp nhất, chi phí lắp đặt thấp; dễ dàng mở rộng mạng. | Rất khó xác định vị trí đứt cáp chính xác; khi lưu lượng truyền lớn dễ xảy ra nghẽn đường truyền và xung đột tín hiệu. |
| **계층형 (Tree / Hình cây)** | Cấu trúc phân nhánh theo thứ tự hình cây phân cấp; nút gốc kết nối tới các nút phân phối cấp dưới. | Rất phù hợp với việc phân chia mạng theo cơ cấu tổ chức phòng ban của doanh nghiệp; dễ quản lý mở rộng. | Nếu nút nhánh cấp trên bị hỏng thì toàn bộ nhánh cây con cấp dưới sẽ bị cô lập hoàn toàn khỏi hệ thống. |
| **망형 (Mesh / Hình lưới)** | Mỗi nút mạng đều được thiết lập đường truyền cáp vật lý trực tiếp tới các nút mạng khác trong hệ thống. | **Độ tin cậy và an toàn cao nhất**; luôn có nhiều đường truyền dự phòng thay thế; không bao giờ bị nghẽn mạch cục bộ. | **Chi phí đầu tư phần cứng và kéo cáp đắt đỏ nhất**; việc cấu hình và quản trị bảng định tuyến cực kỳ phức tạp. |

- **2. Công thức tính toán trong Mạng lưới toàn phần (Full Mesh):**
  - Cho mạng gồm $n$ nút máy tính được kết nối toàn phần (Full Mesh Topology):
    $$\mathbf{\text{Tổng số đường truyền cáp cần thiết} = \frac{n(n - 1)}{2}}$$
    $$\mathbf{\text{Số cổng giao tiếp (Ports) trên mỗi nút máy tính} = n - 1}$$
  - *Ví dụ bài toán thi:* Một phòng máy chủ có $n = 6$ máy chủ muốn kết nối mạng lưới toàn phần Mesh. Hỏi cần bao nhiêu đường dây cáp mạng và mỗi máy cần bao nhiêu card mạng?
    - Số đường cáp: $\frac{6(6 - 1)}{2} = \frac{30}{2} = 15$ đường cáp.
    - Số cổng trên mỗi máy: $6 - 1 = 5$ cổng.

- **3. Bảng các tiêu chuẩn mạng cục bộ IEEE 802 quan trọng:**

| Chuẩn IEEE | Tên công nghệ | Môi trường truyền dẫn & Cơ chế điều khiển |
| :--- | :--- | :--- |
| **IEEE 802.1** | Architecture & Bridging | Cấu trúc mạng tổng thể và công nghệ bắc cầu liên mạng LAN. |
| **IEEE 802.2** | LLC (Logical Link Control) | Tầng con điều khiển liên kết logic trong tầng Data Link. |
| **IEEE 802.3** | **Ethernet (CSMA/CD)** | Chuẩn mạng LAN cáp có dây phổ biến nhất; sử dụng cơ chế tranh chấp đường truyền CSMA/CD. |
| **IEEE 802.4** | Token Bus | Mạng cấu trúc tuyến tính Bus nhưng điều khiển truyền bằng thẻ bài Token. |
| **IEEE 802.5** | Token Ring | Mạng vòng khép kín điều khiển truyền bằng thẻ bài Token Passing của IBM. |
| **IEEE 802.11** | **Wireless LAN (Wi-Fi)** | Chuẩn mạng cục bộ không dây; sử dụng cơ chế tránh xung đột **CSMA/CA**. |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Vai trò của bộ kết thúc Terminator (종단기) trong mạng Bus:**
  - Tín hiệu điện truyền trên cáp đồng khi gặp đoạn cuối cụt của dây cáp nếu không được hấp thụ sẽ bị dội ngược trở lại (Signal Reflection). Sóng dội ngược này sẽ va chạm trực tiếp với các tín hiệu đang phát trên dây, gây nhiễu sóng và phá hủy hoàn toàn dữ liệu. Điện trở Terminator (thường là $50 \, \Omega$) gắn ở hai đầu cáp có nhiệm vụ hấp thụ triệt để năng lượng tín hiệu điện khi đến cuối đường cáp.

### 복습 체크리스트
- [ ] Phân biệt được: Star (Hub trung tâm), Ring (vòng Token), Bus (đường cáp trục + Terminator).
- [ ] Thuộc lòng công thức tính số dây cáp của mạng Full Mesh: $\frac{n(n-1)}{2}$.
- [ ] Nhớ mỗi máy trong mạng Full Mesh cần $n - 1$ cổng kết nối.
- [ ] Nhớ IEEE 802.3 là Ethernet (CSMA/CD), còn IEEE 802.11 là Wi-Fi (CSMA/CA).
