# 전송 계층: TCP vs UDP 및 흐름·혼잡·오류 제어 (Tầng giao vận: TCP/UDP & Kiểm soát luồng)

## 학습 목표 (Mục tiêu)
- Phân biệt chi tiết sự khác nhau mang tính bản chất giữa hai giao thức giao vận chủ đạo trên Internet: TCP (hướng kết nối, tin cậy, luồng byte) và UDP (phi kết nối, tốc độ, datagram).
- Thấu hiểu và vẽ lại chính xác chu trình thiết lập kết nối Bắt tay 3 bước (3-Way Handshake: SYN $\rightarrow$ SYN-ACK $\rightarrow$ ACK) và chu trình giải phóng Bắt tay 4 bước (4-Way Handshake).
- Nắm vững 3 cơ chế kiểm soát chất lượng truyền thông của TCP: Kiểm soát luồng (Flow Control với Sliding Window), Kiểm soát tắc nghẽn (Congestion Control với Slow Start) và Kiểm soát lỗi (Error Control với ARQ).

## 핵심 키워드 (Từ khóa)
- TCP vs UDP — Hướng kết nối tin cậy (연결 지향형) vs Phi kết nối tốc độ cao (비연결형).
- 3-Way Handshake — SYN, SYN+ACK, ACK (Quy trình 3 bước thiết lập kết nối TCP an toàn).
- 4-Way Handshake — FIN, ACK, FIN, ACK (Quy trình 4 bước đóng kết nối TCP).
- 흐름 제어 (Flow Control) — Đồng bộ tốc độ bên gửi và bên nhận; Thuật toán Cửa sổ trượt (슬라이딩 윈도우 - Sliding Window).
- 혼잡 제어 (Congestion Control) — Ngăn ngừa nghẽn mạng; Thuật toán Khởi động chậm (Slow Start) và Tránh tắc nghẽn.
- 오류 제어 및 ARQ (Error Control & ARQ) — Stop-and-Wait ARQ, Go-Back-N ARQ, Selective Repeat ARQ.

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Kế thừa từ `16-mang-may-tinh-osi-7-tang-va-giao-thuc.md`, sau khi gói tin (Packet) được tầng Mạng định tuyến qua các Router, tầng Giao vận (Transport Layer) chịu trách nhiệm đảm bảo toàn vẹn dữ liệu giữa hai tiến trình ứng dụng.
- **Đang giải quyết gì (Current Problem):** Giải quyết câu hỏi: Làm sao các gói tin qua mạng Internet chập chờn vẫn ghép nối lại thành một tệp hoàn chỉnh không thiếu một byte nào (TCP), và tại sao xem video trực tiếp hoặc gọi thoại lại ưu tiên dùng UDP thay vì TCP.
- **Dùng đi đâu (Forward Handoff):** Các gói tin TCP và UDP đều mang địa chỉ định danh nguồn và đích thông qua hệ thống địa chỉ IP; bài toán định danh IP và kỹ thuật chia mạng con Subnetting sẽ được giải quyết ở bài `18-dia-chi-ip-ipv4-ipv6-va-chia-mang-con-subnetting.md`.

## 읽는 방법 (Cách đọc)
- **TCP vs UDP:**
  - Cần **chính xác 100%, không được mất dữ liệu** (Web, Email, File, Ngân hàng) $\rightarrow$ Chọn **TCP**.
  - Cần **tốc độ tức thời, chấp nhận rơi vài gói tin** (Video call, Livestream, DNS, Game) $\rightarrow$ Chọn **UDP**.
- **Handshake:**
  - Mở kết nối: **3 bước (SYN $\rightarrow$ SYN+ACK $\rightarrow$ ACK)**.
  - Đóng kết nối: **4 bước (FIN $\rightarrow$ ACK $\rightarrow$ FIN $\rightarrow$ ACK)**.
- **Cửa sổ trượt (Sliding Window):** Kích thước cửa sổ (Window Size) do bên nhận quyết định dựa trên bộ đệm còn trống, giúp bên gửi gửi một lúc nhiều gói tin mà không cần đợi từng ACK đơn lẻ.

---

## 전송 계층: TCP vs UDP 및 흐름·혼잡·오류 제어

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [한국어]: `TCP는 3-Way Handshake를 사용하는 연결 지향형 신뢰성 프로토콜로 흐름 제어(슬라이딩 윈도우)와 혼잡 제어(Slow Start)를 제공한다. UDP는 오버헤드가 적고 빠른 비연결형 프로토콜로 실시간 스트리밍에 적합하다. 연결 해제는 4-Way Handshake를 거친다.`
  - [Tiếng Việt]: TCP là giao thức hướng kết nối tin cậy dùng bắt tay 3 bước (3-Way Handshake), cung cấp kiểm soát luồng (Sliding Window) và kiểm soát tắc nghẽn (Slow Start). UDP là giao thức phi kết nối tốc độ cao với overhead thấp phù hợp cho streaming thời gian thực. Đóng kết nối TCP trải qua bắt tay 4 bước.

- **1. Bảng đối chiếu toàn diện: TCP vs UDP:**

| Tiêu chuẩn so sánh | Giao thức TCP (Transmission Control Protocol) | Giao thức UDP (User Datagram Protocol) |
| :--- | :--- | :--- |
| **Loại hình kết nối** | **Hướng kết nối (연결 지향형 - Connection-oriented)**. | **Phi kết nối (비연결형 - Connectionless)**. |
| **Độ tin cậy truyền dữ liệu**| **Rất cao (신뢰성 보장)**; có ACK và tự động truyền lại gói mất. | **Không đảm bảo tin cậy**; gói tin có thể thất lạc hoặc sai thứ tự. |
| **Đơn vị truyền tải** | **Luồng byte liên tục (Byte Stream)**; có đánh số thứ tự. | **Khối tin độc lập (Datagram)**; không ghép chuỗi. |
| **Kích thước Header** | **20 ~ 60 Bytes** (phức tạp, chứa Sequence, ACK, Flags). | **Cố định 8 Bytes** (rất nhẹ, giảm tối đa độ trễ). |
| **Cơ chế kiểm soát** | **Có đầy đủ:** Kiểm soát luồng, tắc nghẽn, kiểm soát lỗi. | **Hoàn toàn không có** kiểm soát luồng và tắc nghẽn. |
| **Tốc độ truyền** | Chậm hơn do chi phí bắt tay và gửi nhận gói tin ACK. | **Rất nhanh**, truyền tức thời không cần đợi tín hiệu phản hồi. |
| **Ứng dụng tiêu biểu** | **HTTP/HTTPS (Web), FTP (Tệp), SMTP (Mail), SSH**. | **DNS, DHCP, SNMP, VoIP, Livestream, Game online**. |

- **2. Bảng quy trình bắt tay TCP (TCP Handshake Procedures):**

| Loại hình bắt tay | Các bước truyền tín hiệu cờ (Flags) | Ý nghĩa nghiệp vụ mạng |
| :--- | :--- | :--- |
| **Bắt tay 3 bước** (3-Way Handshake: Thiết lập kết nối) | 1. Client $\rightarrow$ Server: **SYN** ($seq = x$); 2. Server $\rightarrow$ Client: **SYN + ACK** ($seq = y, ack = x + 1$); 3. Client $\rightarrow$ Server: **ACK** ($seq = x + 1, ack = y + 1$) | Đồng bộ hóa số thứ tự (Sequence Number) ban đầu giữa hai máy tính; xác nhận cả 2 chiều gửi/nhận đều hoạt động bình thường. |
| **Bắt tay 4 bước** (4-Way Handshake: Giải phóng kết nối) | 1. Client $\rightarrow$ Server: **FIN**; 2. Server $\rightarrow$ Client: **ACK** (chờ xử lý nốt dữ liệu dở dang); 3. Server $\rightarrow$ Client: **FIN** (sẵn sàng đóng kết nối); 4. Client $\rightarrow$ Server: **ACK** $\rightarrow$ Kết thúc hoàn toàn. | Đảm bảo cả hai phía đã hoàn tất việc truyền gửi toàn bộ dữ liệu trong bộ đệm trước khi giải phóng cổng kết nối. |

- **3. Bảng 3 cơ chế kiểm soát cốt lõi của TCP:**

| Cơ chế kiểm soát | Thuật toán đại diện | Bản chất kỹ thuật chuẩn đề thi |
| :--- | :--- | :--- |
| **1. Kiểm soát luồng** (흐름 제어 - Flow Control) | **Sliding Window (슬라이딩 윈도우)** | Đồng bộ tốc độ giữa bên gửi (quá nhanh) và bên nhận (chậm). Bên nhận gửi kèm thông số **Window Size** để báo cho bên gửi biết dung lượng bộ đệm còn trống. |
| **2. Kiểm soát tắc nghẽn** (혼잡 제어 - Congestion) | **Slow Start (느린 시작)** | Điều chỉnh tốc độ truyền tùy theo tình trạng chịu tải của toàn mạng. Ban đầu gửi 1 gói, tăng theo hàm mũ ($1 \rightarrow 2 \rightarrow 4 \rightarrow 8$) đến ngưỡng **ssthresh**, sau đó tăng tuyến tính ($+1$). |
| **3. Kiểm soát lỗi** (오류 제어 - Error Control) | **ARQ (Automatic Repeat Request)** | Tự động phát hiện gói lỗi qua Checksum và gửi yêu cầu truyền lại: Stop-and-Wait ARQ, Go-Back-N ARQ, Selective Repeat ARQ. |

- **주의/함정 (Bẫy đề thi):**
  - **Kích thước Header của UDP:** Header của UDP cực kỳ đơn giản và luôn cố định đúng **8 Byte** (gồm 4 trường: Cổng nguồn 2B, Cổng đích 2B, Độ dài 2B, Checksum 2B).
  - **Go-Back-N vs Selective Repeat:**
    - Go-Back-N: Bên nhận chỉ nhận gói đúng thứ tự; nếu mất gói 3 thì dù gói 4, 5 đến cũng bị vứt bỏ $\rightarrow$ Bên gửi phải truyền lại toàn bộ từ gói 3 trở đi.
    - Selective Repeat: Bên nhận có bộ đệm lưu gói 4, 5 $\rightarrow$ Bên gửi **chỉ cần truyền lại duy nhất gói số 3 bị mất**.

- **한 문장 설명 (Câu chốt tự nhớ):**
  - *"TCP tin cậy bắt tay 3 bước (SYN, SYN-ACK, ACK), UDP thần tốc header 8 byte; trôi luồng dùng Sliding Window, nghẽn mạng dùng Slow Start."*

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ ASCII Chu trình Thiết lập Kết nối: TCP 3-Way Handshake:

```text
       Client (Phía chủ động mở)                       Server (Phía lắng nghe)
      [ Trạng thái: CLOSED ]                           [ Trạng thái: LISTEN ]
                |                                                 |
                | --------- (Bước 1) SYN: seq = x --------------> | [ SYN_RCVD ]
         [ SYN_SENT ]                                             |
                |                                                 |
                | <--- (Bước 2) SYN + ACK: seq = y, ack = x + 1 - |
      [ ESTABLISHED ]                                             |
                |                                                 |
                | --------- (Bước 3) ACK: seq = x + 1, ack = y + 1 ->
                |                                                 | [ ESTABLISHED ]
                v                                                 v
  <==================== ĐƯỜNG TRUYỀN DỮ LIỆU SONG CÔNG TOÀN PHẦN (FULL-DUPLEX) ====================>
```

*Phân tích chi tiết từng bước trao đổi cờ và số thứ tự:*
1. **Bước 1 (Client $\rightarrow$ Server):** Client gửi gói tin có cờ `SYN = 1`, mang số thứ tự ngẫu nhiên ban đầu $seq = x$. Client chuyển sang trạng thái `SYN_SENT`.
2. **Bước 2 (Server $\rightarrow$ Client):** Server nhận `SYN`, gửi lại gói tin mang cả hai cờ: `SYN = 1` với số thứ tự riêng của Server $seq = y$, và `ACK = 1` với số xác nhận $ack = x + 1$ (báo cho Client biết Server đã nhận được $x$ và đang chờ nhận byte $x + 1$). Server chuyển sang trạng thái `SYN_RCVD`.
3. **Bước 3 (Client $\rightarrow$ Server):** Client nhận được `SYN+ACK`, chuyển ngay sang trạng thái `ESTABLISHED`. Client gửi tiếp gói `ACK = 1` mang $seq = x + 1$ và $ack = y + 1$. Server nhận được gói này cũng chuyển sang `ESTABLISHED`. Kết nối mở thành công!

#### 2. Sơ đồ ASCII Chu trình Đóng Kết nối: TCP 4-Way Handshake:

```text
       Client (Phía chủ động đóng)                     Server (Phía bị động đóng)
     [ Trạng thái: ESTABLISHED ]                       [ Trạng thái: ESTABLISHED ]
                |                                                 |
                | ---------- (Bước 1) FIN: seq = u -------------> | [ CLOSE_WAIT ]
        [ FIN_WAIT_1 ]                                            | (Server truyền nốt
                |                                                 |  dữ liệu dở dang)
                | <--------- (Bước 2) ACK: ack = u + 1 ---------- |
        [ FIN_WAIT_2 ]                                            |
                |                                                 |
                | <--- (Bước 3) FIN: seq = v, ack = u + 1 ------- | [ LAST_ACK ]
                |                                                 |
                | ---------- (Bước 4) ACK: ack = v + 1 ---------> |
        [ TIME_WAIT ]                                             |
       (Chờ 2 * MSL)                                              v
                |                                              [ CLOSED ]
                v
            [ CLOSED ]
```

*Phân tích vai trò then chốt của trạng thái `TIME_WAIT` trên Client:*
- Sau khi gửi `ACK` ở Bước 4, Client **không đóng ngay** mà chuyển sang trạng thái `TIME_WAIT` và duy trì bộ đếm thời gian bằng **$2 \times \text{MSL}$** (Maximum Segment Lifetime, thường là 2 đến 4 phút).
- **Ý nghĩa 1 (Phòng ngừa rơi gói ACK cuối):** Nếu gói `ACK` ở Bước 4 bị thất lạc trên mạng, Server sẽ hết thời gian chờ (Timeout) và gửi lại gói `FIN` (Bước 3). Client ở trạng thái `TIME_WAIT` sẽ nhận lại được `FIN` này và gửi lại `ACK`, đảm bảo Server đóng kết nối thành công.
- **Ý nghĩa 2 (Tránh nhiễu kết nối mới):** Đảm bảo tất cả các gói tin cũ bị trễ trên đường truyền của phiên này hoàn toàn biến mất trước khi một kết nối mới có thể tái sử dụng cùng cặp địa chỉ IP và Port đó.

#### 3. Lần vết thuật toán Khởi động chậm (Slow Start) trong kiểm soát tắc nghẽn:
- Giả sử ngưỡng chuyển đổi tắc nghẽn (Slow Start Threshold - `ssthresh`) được cấu hình là **`16 MSS`** (Maximum Segment Size).
  - Chu kỳ 1: Gửi 1 MSS.
  - Chu kỳ 2: Gửi 2 MSS (tăng gấp đôi $2^1$).
  - Chu kỳ 3: Gửi 4 MSS (tăng gấp đôi $2^2$).
  - Chu kỳ 4: Gửi 8 MSS (tăng gấp đôi $2^3$).
  - Chu kỳ 5: Gửi 16 MSS (chạm ngưỡng `ssthresh`).
  - Chu kỳ 6 trở đi: Chuyển sang giai đoạn **Tránh tắc nghẽn (Congestion Avoidance)**, chỉ tăng tuyến tính mỗi chu kỳ thêm 1 MSS: $17 \rightarrow 18 \rightarrow 19$...

#### 4. Bảng đối chiếu số hiệu cổng dịch vụ chuẩn (Well-known Ports) thường gặp:

| Cổng mạng (Port) | Giao thức tầng 4 | Dịch vụ ứng dụng tương ứng |
| :---: | :---: | :--- |
| **`20 / 21`** | TCP | **FTP** (20: Dữ liệu, 21: Điều khiển lệnh) |
| **`22`** | TCP | **SSH** (Giao thức truyền thông vỏ bảo mật) |
| **`23`** | TCP | **Telnet** (Truy cập từ xa không mã hóa văn bản thô) |
| **`25`** | TCP | **SMTP** (Gửi thư điện tử) |
| **`53`** | **UDP / TCP** | **DNS** (Phân giải tên miền thành địa chỉ IP, mặc định dùng UDP) |
| **`67 / 68`** | **UDP** | **DHCP** (Cấp phát địa chỉ IP động tự động) |
| **`80`** | TCP | **HTTP** (Truy cập Web thông thường) |
| **`443`** | TCP | **HTTPS** (Truy cập Web mã hóa bảo mật qua SSL/TLS) |

---

### 복습 체크리스트
- [ ] Phân biệt được: TCP hướng kết nối tin cậy, UDP phi kết nối tốc độ cao.
- [ ] Thuộc lòng 3 bước Handshake mở: SYN $\rightarrow$ SYN+ACK $\rightarrow$ ACK.
- [ ] Thuộc lòng 4 bước Handshake đóng: FIN $\rightarrow$ ACK $\rightarrow$ FIN $\rightarrow$ ACK.
- [ ] Ghi nhớ kích thước Header UDP luôn cố định 8 Byte.
- [ ] Nắm chắc thuật toán kiểm soát luồng: Sliding Window do bên nhận báo Window Size.
- [ ] Nắm chắc thuật toán kiểm soát tắc nghẽn: Slow Start tăng hàm mũ $2^n$ đến ngưỡng `ssthresh`.
- [ ] Nhớ các cổng dịch vụ then chốt: FTP (21), SSH (22), DNS (53), HTTP (80), HTTPS (443).
