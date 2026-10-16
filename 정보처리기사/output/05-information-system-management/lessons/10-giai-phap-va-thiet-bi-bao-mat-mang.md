# 네트워크 보안 솔루션 및 시스템 관제 (Giải pháp bảo mật mạng, Thiết bị an ninh & Giám sát nhật ký hệ thống: Firewall, IDS/IPS, VPN, Logs)

## 학습 목표 (Mục tiêu)
- Nắm vững kiến trúc đường hầm (터널링) và hai giao thức chuẩn hóa của Mạng riêng ảo (**VPN - Virtual Private Network**): **IPsec VPN** (Tầng 3: AH vs ESP, Transport Mode vs Tunnel Mode) và **SSL/TLS VPN** (Tầng giao vận/ứng dụng).
- Phân biệt bản chất hoạt động của các thiết bị bảo vệ mạng: Tường lửa (**Firewall**), Hệ thống phát hiện xâm nhập (**IDS**), Hệ thống ngăn chặn xâm nhập (**IPS**), và Tường lửa ứng dụng web (**WAF**).
- Phân biệt sâu sắc hai cơ chế phát hiện xâm nhập của IDS: **Phát hiện theo chữ ký mẫu (오용 탐지 - Misuse Detection)** và **Phát hiện bất thường theo hành vi (이상 탐지 - Anomaly Detection)**.
- Hiểu rõ khái niệm Hệ điều hành bảo mật (**Secure OS**) và 4 kỹ thuật phân ly tài nguyên an toàn (Vật lý, Thời gian, Logic, Mật mã).
- Thuộc lòng chức năng và câu lệnh tra cứu của 4 tệp nhật ký đăng nhập Linux nhị phân kinh điển: `/var/run/utmp`, `/var/log/wtmp`, `/var/log/btmp`, `/var/log/lastlog` cùng tệp nhật ký xác thực `/var/log/secure`.

## 핵심 키워드 (Từ khóa song ngữ)
- VPN (Virtual Private Network — Mạng riêng ảo kết nối qua đường hầm mã hóa an toàn)
- IPsec (IP Security — Tầng mạng L3, AH xác thực vs ESP mã hóa, Tunnel vs Transport)
- 방화벽 (Firewall — Lọc gói tin Packet Filter, Trạng thái Stateful Inspection, Proxy L7)
- 침입 탐지 시스템 (IDS — Intrusion Detection System, HIDS máy chủ vs NIDS mạng)
- 오용 탐지 (Misuse / Signature Detection — Tỷ lệ báo động sai thấp, bất lực trước Zero-Day)
- 이상 탐지 (Anomaly / Behavior Detection — Dựa trên Baseline, phát hiện được Zero-Day, báo sai cao)
- 침입 방지 시스템 (IPS — Intrusion Prevention System, Inline Mode, chủ động chặn gói tin)
- Secure OS (보안 운영체제 — Nhân bảo mật Security Kernel, thực thi bắt buộc MAC)
- 리눅스 로그 파일 (Linux Log Files — `utmp`, `wtmp`, `btmp`, `lastlog`, `secure`)
- last / lastb / who (Các câu lệnh tra cứu nhật ký nhị phân Linux)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Từ danh mục các đòn tấn công mạng (DoS, DDoS, Spoofing, Sniffing) đã học tại [09-tan-cong-mang-va-nguy-co-an-ninh.md](09-tan-cong-mang-va-nguy-co-an-ninh.md), hệ thống mạng doanh nghiệp bắt buộc phải triển khai các giải pháp phòng thủ chuyên sâu theo chiều sâu (Defense-in-Depth).
- **Đang giải quyết gì (Current Problem):** Bài học này trang bị toàn bộ vũ khí an ninh mạng: thiết lập kênh truyền mã hóa VPN, cấu hình tường lửa lọc gói tin, vận hành hệ thống phát hiện/ngăn chặn xâm nhập IDS/IPS, và giám sát kiểm toán tệp log hệ thống Linux để phục vụ điều tra số (Digital Forensics).
- **Dùng đi đâu (Forward Handoff):** Sau khi hoàn thành lớp phòng thủ an ninh mạng, người học sẽ nghiên cứu nền tảng hạ tầng truyền dẫn vật lý tại [11-truyen-thong-du-lieu-va-dieu-che.md](11-truyen-thong-du-lieu-va-dieu-che.md) và toàn bộ cấu trúc họ giao thức TCP/IP tại [12-mang-may-tinh-va-giao-thuc-tcp-ip.md](12-mang-may-tinh-va-giao-thuc-tcp-ip.md).

## 읽는 방법 (Cách đọc & Dấu hiệu nhận diện đề thi)
- **IPsec VPN (Đặc điểm phân biệt):**
  - **AH (Authentication Header):** Chỉ bảo đảm tính toàn vẹn (Integrity) và xác thực (Authentication), **tuyệt đối không mã hóa dữ liệu** (không bảo đảm tính bí mật).
  - **ESP (Encapsulating Security Payload):** Vừa mã hóa bảo đảm tính bí mật (Confidentiality), vừa xác thực và bảo đảm tính toàn vẹn.
  - **Transport Mode:** Chỉ mã hóa Payload dữ liệu, giữ nguyên Header IP gốc.
  - **Tunnel Mode:** Mã hóa toàn bộ gói tin IP cũ (cả Header cũ), gắn thêm Header IP mới ở ngoài $\rightarrow$ Dùng cho kết nối Router-to-Router (Site-to-Site).
- **Cơ chế phát hiện của IDS (Cực kỳ hay bị bẫy):**
  - Nhắc đến **"알려진 공격 패턴(Signature) 비교"**, **"오탐률(False Positive) 낮음"**, **"새로운 공격(Zero-Day) 탐지 불가"** $\rightarrow$ Chọn ngay **오용 탐지 (Misuse / Signature Detection)**.
  - Nhắc đến **"정상 기준(Baseline) 설정"**, **"급격한 이상 행동 감지"**, **"새로운 공격(Zero-Day) 탐지 가능"**, **"오탐률 높음"** $\rightarrow$ Chọn ngay **이상 탐지 (Anomaly / Behavior Detection)**.
- **Bốn tệp log đăng nhập Linux (Bắt buộc phải thuộc):**
  - `/var/run/utmp` $\rightarrow$ Người dùng **hiện đang đăng nhập** (lệnh `who`, `w`).
  - `/var/log/wtmp` $\rightarrow$ Lịch sử **đăng nhập/đăng xuất thành công** và reboot (lệnh `last`).
  - `/var/log/btmp` $\rightarrow$ Lịch sử **đăng nhập THẤT BẠI** do sai mật khẩu (lệnh `lastb`).
  - `/var/log/lastlog` $\rightarrow$ Lần đăng nhập **thành công gần nhất của từng user** (lệnh `lastlog`).
  - `/var/log/secure` $\rightarrow$ Nhật ký xác thực qua SSH, `su`, `sudo` (tệp text, xem bằng `cat/tail`).

---

## 네트워크 보안 솔루션 및 시스템 관제

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Mạng riêng ảo (VPN - Virtual Private Network)
- **개념 (Khái niệm):** Công nghệ sử dụng hạ tầng mạng công cộng (Internet) để thiết lập một kênh kết nối riêng tư, an toàn giữa các chi nhánh hoặc người dùng từ xa tới mạng nội bộ doanh nghiệp thông qua kỹ thuật **Tạo đường hầm (터널링 - Tunneling)** và **Mã hóa dữ liệu (암호화)**.
- **Đối chiếu hai công nghệ VPN tiêu chuẩn:**

| Tiêu chuẩn VPN | Tầng mạng hoạt động | Đặc điểm kiến trúc & Giao thức thành phần |
| :--- | :---: | :--- |
| **IPsec VPN** | **Tầng 3 (Network Layer)** | Hoạt động độc lập ứng dụng ở L3. Giao thức AH xác thực toàn vẹn (không mã hóa), ESP vừa mã hóa vừa xác thực, IKE tự động thương lượng và trao đổi khóa bí mật. |
| **SSL/TLS VPN** | **Tầng 4 ~ 7 (Transport/App)** | Hoạt động qua giao thức HTTPS; người dùng truy cập trực tiếp qua trình duyệt web mà không cần cài đặt phần mềm Client chuyên dụng, dễ vượt tường lửa NAT. |

- **Hai chế độ hoạt động của IPsec:**
  - **전송 모드 (Transport Mode):** Chỉ mã hóa phần dữ liệu (Payload) của gói tin IP, giữ nguyên Header IP gốc. Phù hợp cho giao tiếp trực tiếp giữa máy trạm và máy trạm (Host-to-Host).
  - **터널 모드 (Tunnel Mode):** Mã hóa toàn bộ gói tin IP ban đầu (cả Header và Payload), sau đó bọc thêm một Header IP mới ở phía trước. Phù hợp cho kết nối giữa mạng chi nhánh với mạng trụ sở chính (Gateway-to-Gateway / Site-to-Site).

#### 2. Các giải pháp phòng thủ an ninh mạng (Firewall, IDS, IPS, WAF)

| Giải pháp | Tên tiếng Hàn & Anh | Cơ chế hoạt động & Phạm vi bảo vệ |
| :--- | :--- | :--- |
| **Tường lửa** | **방화벽 (Firewall)** | Kiểm soát và lọc gói tin theo Security Rules (Packet Filter ở L3/L4, Stateful Inspection kiểm tra bảng trạng thái phiên, Proxy Gateway ở L7). |
| **Hệ thống phát hiện xâm nhập** | **IDS (Intrusion Detection System)** | Giám sát lưu lượng thụ động (Passive/Port Mirroring); khi phát hiện xâm nhập sẽ ghi log và phát cảnh báo (Alert) tới quản trị viên mà không làm nghẽn mạng. |
| **Hệ thống ngăn chặn xâm nhập** | **IPS (Intrusion Prevention System)** | Lắp đặt trực tiếp trên luồng truyền dữ liệu (Inline Mode); chủ động chặn đứng (Block/Drop) gói tin độc hại và ngắt phiên kết nối theo thời gian thực. |
| **Tường lửa ứng dụng Web** | **WAF (Web Application Firewall)** | Hoạt động chuyên sâu ở tầng L7; phân tích sâu bản tin HTTP/HTTPS để ngăn chặn SQL Injection, XSS, CSRF, File Upload độc hại. |

#### 3. Hai cơ chế phát hiện xâm nhập cốt lõi của IDS/IPS

| Cơ chế phát hiện | Tên tiếng Hàn & Anh | Bản chất nguyên lý & Ưu nhược điểm đề thi |
| :--- | :--- | :--- |
| **Phát hiện theo chữ ký mẫu** | **오용 탐지 (Misuse / Signature)** | So sánh lưu lượng với kho chữ ký mẫu đã biết; tỷ lệ báo động sai (False Positive) cực thấp, nhưng bất lực trước đòn tấn công mới (Zero-Day). |
| **Phát hiện bất thường theo hành vi** | **이상 탐지 (Anomaly / Behavior)** | So sánh với đường cơ sở hành vi bình thường (Baseline); phát hiện được đòn tấn công mới (Zero-Day), nhưng tỷ lệ báo động sai (False Positive) rất cao. |

#### 4. Hệ điều hành bảo mật (Secure OS)
- **개념 (Khái niệm):** Hệ điều hành được tích hợp thêm **Nhân bảo mật (보안 커널 - Security Kernel)** bên trong nhân hệ thống, cung cấp cơ chế Kiểm soát truy cập bắt buộc (MAC), bảo vệ tính toàn vẹn của tệp tin nhị phân và ngăn chặn người dùng có quyền quản trị tối cao (Root) lạm dụng quyền lực.
- **4 phương pháp phân ly bảo mật trong Secure OS:**
  1. **물리적 분리 (Phân ly vật lý):** Sử dụng các hệ thống phần cứng và dây cáp mạng tách rời hoàn toàn cho các mức bảo mật khác nhau.
  2. **시간적 분리 (Phân ly thời gian):** Các tiến trình thuộc các cấp độ bảo mật khác nhau chỉ được phép thực thi ở các khoảng thời gian tách biệt.
  3. **논리적 분리 (Phân ly logic):** Phân chia không gian địa chỉ bộ nhớ hoặc sử dụng máy ảo (Virtualization/Containers) để cách ly tiến trình.
  4. **암호적 분리 (Phân ly mật mã):** Mã hóa dữ liệu bên trong bộ nhớ để các tiến trình khác dù nhìn thấy cũng không thể đọc hiểu được.

#### 5. Bảng tra cứu các tệp nhật ký hệ thống Linux (Linux System Logs)

| Đường dẫn tệp nhật ký | Định dạng tệp | Nội dung lưu trữ chi tiết | Lệnh tra cứu chuẩn |
| :--- | :---: | :--- | :---: |
| **`/var/run/utmp`** | **Nhị phân** (Binary) | Lưu thông tin về **những người dùng hiện đang đăng nhập trực tiếp** vào hệ thống tại thời điểm hiện tại. | **`who`**, **`w`**, `users` |
| **`/var/log/wtmp`** | **Nhị phân** (Binary) | Lưu lịch sử **tất cả các phiên đăng nhập và đăng xuất thành công** từ trước đến nay, kèm thời gian hệ thống khởi động lại (Reboot). | **`last`** |
| **`/var/log/btmp`** | **Nhị phân** (Binary) | Lưu lịch sử **tất cả các lần đăng nhập THẤT BẠI** (sai mật khẩu, sai tài khoản). Là bằng chứng then chốt để phát hiện đòn tấn công Brute Force. | **`lastb`** |
| **`/var/log/lastlog`** | **Nhị phân** (Binary) | Lưu lại thông tin về **lần đăng nhập thành công gần đây nhất của từng tài khoản người dùng** trong hệ thống. | **`lastlog`** |
| **`/var/log/secure`** (Ubuntu: `auth.log`) | **Văn bản thuần** (Text) | Lưu toàn bộ các sự kiện xác thực hệ thống: đăng nhập từ xa qua dịch vụ SSH, chuyển quyền quản trị qua lệnh `su`, thực thi lệnh đặc quyền `sudo`. | `cat`, `tail`, `grep` |
| **`/var/log/messages`** | **Văn bản thuần** (Text) | Tệp nhật ký hệ thống chung ghi lại các thông báo cảnh báo và hoạt động của Kernel và các dịch vụ nền tảng hệ thống. | `cat`, `tail`, `grep` |

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ phân cấp bố trí thiết bị an ninh mạng (Defense-in-Depth Architecture)
Mô hình phòng thủ mạng theo chiều sâu tiêu chuẩn quốc tế phân chia mạng doanh nghiệp thành các vùng độc lập với các thiết bị an ninh được bố trí tại các vị trí chiến lược:

```text
  [ INTERNET - MẠNG CÔNG CỘNG KHÔNG TIN CẬY ]
                     |
                     v
             +---------------+
             |  Edge Router  |  (Lọc gói tin thô ban đầu bằng Access Control List - ACL)
             +---------------+
                     |
                     v
             +---------------+
             |  External FW  |  (Tường lửa ngoại vi: Chỉ mở các Port dịch vụ công khai 80, 443, 25, 53)
             +---------------+
                     |
         +-----------+-----------+
         |                       |
         v                       v
  [ VÙNG ĐỆM DMZ ]        [ LUỒNG ĐI VÀO MẠNG NỘI BỘ ]
  (Demilitarized Zone)           |
         |                       v
         |               +---------------+
         |               |  Internal FW  |  (Tường lửa nội bộ: Chặn đứng mọi lưu lượng khởi tạo từ DMZ)
         |               +---------------+
         |                       |
         |                       v
         |               +---------------+
         |               |      IPS      |  (Inline Mode: Nối tiếp trên dây, chặn DROP gói tin độc hại)
         |               +---------------+
         |                       |
         |                       v
         |               +---------------+
         |               |  Core Switch  | ===== (Port Mirroring / SPAN) =====> [ NIDS (Passive) ]
         |               +---------------+                                      (Ghi log & Cảnh báo SOC)
         |                       |
         |       +---------------+---------------+
         |       |                               |
         |       v                               v
         | [ MẠNG NỘI BỘ (LAN) ]       [ MÁY CHỦ BẢO MẬT CAO ]
         | (Máy trạm Workstations)     (Database Server, Active Directory, Secure OS)
         |
         v
  [ CÁC MÁY CHỦ CÔNG KHAI TRONG DMZ ]
  +-------------------------------------------------------+
  |  +--------------------+       +--------------------+  |
  |  |    WAF (Web FW)    |       |     DNS Server     |  |
  |  +--------------------+       +--------------------+  |
  |            |                                          |
  |            v                  +--------------------+  |
  |  +--------------------+       |    Mail Server     |  |
  |  |  Web App Server    |       +--------------------+  |
  |  +--------------------+                               |
  +-------------------------------------------------------+
```

- **Phân tích kỹ thuật các thành phần phòng thủ cốt lõi:**
  - **1. Firewall (방화벽 — Tường lửa mạng):**
    - Kiểm soát luồng lưu lượng L3/L4 giữa các vùng mạng dựa trên địa chỉ IP nguồn/đích, Cổng dịch vụ (Port), và bảng trạng thái kết nối (State Table).
    - Áp dụng nguyên tắc **Default Deny**: Mọi lưu lượng không được cho phép rõ ràng trong chính sách sẽ mặc định bị từ chối.
  - **2. DMZ (Demilitarized Zone — Vùng đệm phi quân sự):**
    - Là vùng mạng trung gian cách ly giữa Internet và mạng nội bộ tin cậy (LAN).
    - Đặt các máy chủ cung cấp dịch vụ ra bên ngoài: Web Server, Mail Server, DNS Server, Proxy.
    - **Nguyên tắc an toàn sống còn:** Máy chủ trong DMZ **tuyệt đối không được phép chủ động khởi tạo kết nối vào mạng nội bộ (Internal LAN)**. Nếu máy chủ web trong DMZ bị tin tặc chiếm quyền điều khiển, kẻ tấn công vẫn bị Tường lửa nội bộ chặn lại, không thể tiến vào thâm nhập CSDL doanh nghiệp.
  - **3. WAF (Web Application Firewall — Tường lửa ứng dụng Web):**
    - Được triển khai ngay phía trước Web Server trong vùng DMZ.
    - Phân tích chuyên sâu ở tầng ứng dụng (L7), kiểm tra toàn bộ Payload HTTP/HTTPS để phát hiện các lỗ hổng OWASP Top 10 (SQL Injection, Cross-Site Scripting XSS, File Inclusion, Command Injection) mà Firewall thông thường ở L3/L4 không thể đọc hiểu được.
  - **4. IPS (Intrusion Prevention System — Ngăn chặn xâm nhập):**
    - Lắp đặt theo chế độ **Inline (nối tiếp trực tiếp trên đường truyền)** tại vị trí trước khi luồng dữ liệu tiến vào mạng nội bộ.
    - Khi phát hiện gói tin chứa chữ ký tấn công hoặc hành vi dị thường, IPS chủ động DROP (hủy) gói tin ngay lập tức và reset phiên kết nối TCP, bảo vệ máy chủ đích trước khi đòn tấn công kịp tiếp cận.
  - **5. IDS (Intrusion Detection System — Phát hiện xâm nhập):**
    - Lắp đặt theo chế độ **Passive (thụ động / ngoài luồng)** thông qua cổng SPAN / Port Mirroring của Switch trung tâm.
    - Thu thập bản sao lưu lượng để phân tích thống kê chuyên sâu và phát tín hiệu cảnh báo (Alert) tới trung tâm vận hành giám sát an ninh (SOC) mà hoàn toàn không gây trễ hoặc nghẽn đường truyền mạng chính.

- **Bảng đối chiếu tổng hợp 5 thành phần kiến trúc an ninh:**

| Thành phần | Vị trí bố trí tiêu chuẩn | Chế độ kết nối | Tầng OSI | Hành động xử lý chính |
| :--- | :--- | :---: | :---: | :--- |
| **Firewall** | Ranh giới Internet - DMZ và DMZ - LAN | Inline | L3 / L4 / L7 | Chấp nhận (Allow) hoặc Từ chối (Deny/Drop) theo IP/Port/State. |
| **DMZ** | Vùng cách ly giữa External FW và Internal FW | Subnet riêng | L2 ~ L7 | Cách ly máy chủ công khai, ngăn chặn tấn công lan truyền vào LAN. |
| **WAF** | Phía trước các máy chủ Web trong DMZ | Inline / Reverse Proxy | L7 (Application) | Phân tích sâu HTTP/HTTPS, chặn SQL Injection, XSS, CSRF. |
| **IPS** | Trước các phân vùng mạng nội bộ quan trọng | Inline | L3 ~ L7 | Phát hiện và chủ động chặn đứng (Drop/Block) gói tin thời gian thực. |
| **IDS** | Cổng Mirroring của Switch trung tâm | Passive (Sniffing) | L3 ~ L7 | Giám sát thụ động, ghi nhận nhật ký và gửi cảnh báo (Alert). |

#### 2. Sự khác biệt giữa chế độ Promiscuous Mode và Port Mirroring
- **Promiscuous Mode:** Chế độ của card mạng (NIC) cho phép nó tiếp nhận và chuyển lên hệ điều hành tất cả các khung dữ liệu đi qua dây cáp, bất kể địa chỉ MAC đích có thuộc về card mạng đó hay không. Được các công cụ Sniffing (Wireshark, tcpdump) sử dụng.
- **Port Mirroring (SPAN - Switched Port Analyzer):** Tính năng trên thiết bị chuyển mạch Switch chuyên dụng, sao chép toàn bộ lưu lượng mạng đi qua một hoặc nhiều cổng mục tiêu rồi chuyển hướng sang cổng giám sát kết nối với thiết bị **NIDS (Network IDS)** để phân tích an ninh mà không làm gián đoạn lưu lượng mạng gốc.

---

### 복습 체크리스트
- [ ] Phân biệt IPsec VPN: AH chỉ xác thực (không mã hóa); ESP vừa mã hóa vừa xác thực.
- [ ] Phân biệt chế độ IPsec: Transport Mode chỉ mã hóa Payload (Host-to-Host); Tunnel Mode mã hóa toàn bộ gói tin cũ và bọc thêm Header IP mới (Site-to-Site).
- [ ] So sánh IDS vs IPS: IDS là thụ động (cảnh báo qua Port Mirroring); IPS là chủ động chặn đứng (Inline Mode).
- [ ] Nắm vững 2 cơ chế phát hiện IDS:
  - 오용 탐지 (Misuse): Dựa trên chữ ký mẫu đã biết, tỷ lệ báo sai thấp, không bắt được Zero-Day.
  - 이상 탐지 (Anomaly): Dựa trên đường cơ sở bình thường, phát hiện được Zero-Day, tỷ lệ báo sai cao.
- [ ] Thuộc lòng 4 tệp log nhị phân Linux: `utmp` (đang đăng nhập - `who`), `wtmp` (đăng nhập thành công - `last`), `btmp` (đăng nhập thất bại - `lastb`), `lastlog` (lần đăng nhập cuối - `lastlog`).
- [ ] Nhớ tệp log xác thực SSH: `/var/log/secure` (RedHat/CentOS) hoặc `/var/log/auth.log` (Ubuntu/Debian).
- [ ] Nắm vững kiến trúc mạng phân vùng chuyên sâu: Firewall lọc L3/L4, DMZ cách ly máy chủ công cộng, WAF bảo vệ web L7, IPS chặn Inline, IDS giám sát Passive.
