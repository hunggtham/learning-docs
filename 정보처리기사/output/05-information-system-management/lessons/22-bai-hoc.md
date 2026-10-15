# 네트워크 보안 기술 (Network Security Tech)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, cơ chế tạo đường hầm (터널링 - Tunneling) và giao thức mã hóa của Mạng riêng ảo (**VPN - Virtual Private Network**): Phân biệt IPSec VPN ở tầng 3 và SSL/TLS VPN ở tầng giao vận.
- Hiểu giao thức điều khiển từ xa an toàn **SSH (Secure Shell)**: Sử dụng **Cổng 22 (Port 22)** để thay thế cho giao thức Telnet không mã hóa cổ điển.
- Phân biệt kiến trúc hoạt động của các giải pháp phòng thủ an ninh mạng: Tường lửa (**Firewall**), Hệ thống phát hiện xâm nhập (**IDS**), Hệ thống ngăn ngừa xâm nhập (**IPS**), và Phân vùng mạng trung gian phi quân sự (**DMZ - Demilitarized Zone**).

## 핵심 키워드 (Từ khóa)
- 네트워크 보안 기술 (Network Security Technologies)
- VPN (Virtual Private Network - 가상 사설망, 터널링)
- IPSec (AH 인증, ESP 암호화, 전송 모드 vs 터널 모드)
- SSH (Secure Shell - 22번 포트, Telnet 대체)
- 방화벽 (Firewall - 패킷 필터링, 상태 기반 감사)
- IDS (침입 탐지 시스템) vs IPS (침입 방지 시스템 - 능동 차단)
- DMZ (Demilitarized Zone - 웹 서버, 메일 서버 배치)

## 선행·연결 개념 (Kiến thức liên kết)
- [21-bai-hoc.md](21-bai-hoc.md): Các hình thức tấn công mạng và 침해 공격 (DDoS, Smurfing, Session Hijacking).
- [23-bai-hoc.md](23-bai-hoc.md): Các giao thức chính theo từng tầng mạng (TCP, UDP, IP, ARP).
- [26-bai-hoc.md](26-bai-hoc.md): 3 yếu tố an ninh bảo mật CIA và quy chuẩn Secure SDLC.

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh trong đề thi:
  - **VPN:** Biến mạng Internet công cộng thành **đường truyền riêng ảo an toàn** thông qua công nghệ đóng gói đường hầm (**터널링 - Tunneling**) và mã hóa dữ liệu.
  - **SSH:** Dùng **Cổng 22 (Port 22)**, thay thế cho Telnet (Port 23) và rlogin để quản trị máy chủ từ xa an toàn bằng mật mã khóa công khai.
  - **IDS vs IPS:**
    - **IDS (Detection):** Thụ động (**수동적**) $\rightarrow$ Chỉ theo dõi, phát hiện và gửi cảnh báo (Alert) cho quản trị viên.
    - **IPS (Prevention):** Chủ động (**능동적**) $\rightarrow$ Tự động chặn đứng (Drop/Block) gói tin độc hại ngay tại thời gian thực.
  - **DMZ:** Nơi đặt các máy chủ công khai (**Web, Mail, DNS**) nằm giữa 2 lớp tường lửa.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng đối chiếu các công nghệ an ninh mạng cốt lõi:**

| Công nghệ bảo mật | Tên tiếng Hàn & Anh | Cơ chế hoạt động & Chức năng kỹ thuật chi tiết |
| :--- | :--- | :--- |
| **Mạng riêng ảo (VPN)** | **VPN** (Virtual Private Network) | Thiết lập kết nối mã hóa điểm-điểm an toàn xuyên qua mạng Internet công cộng. Giúp các chi nhánh và nhân viên làm việc từ xa kết nối vào mạng nội bộ công ty với chi phí rẻ hơn nhiều so với thuê đường truyền vật lý chuyên dụng (Leased Line). |
| **Giao thức SSH** | **SSH** (Secure Shell) | Giao thức mạng mã hóa vận hành tại **Cổng chuẩn 22 (Port 22)**; cung cấp kênh truyền bảo mật tuyệt đối cho các dịch vụ đăng nhập dòng lệnh từ xa (Remote Login), thực thi lệnh và truyền tệp tin (SFTP/SCP), loại bỏ nguy cơ lộ mật khẩu bản rõ của Telnet/FTP. |
| **Tường lửa (Firewall)** | **방화벽** (Firewall) | Thiết bị hoặc phần mềm kiểm soát luồng lưu lượng mạng vào/ra dựa trên các tập luật bảo mật (Security Rules: IP nguồn/đích, Port, giao thức); ngăn chặn các truy cập trái phép từ Internet vào mạng nội bộ. |
| **Phát hiện xâm nhập (IDS)** | **침입 탐지 시스템** (Intrusion Detection System) | Giám sát lưu lượng mạng hoặc nhật ký hệ điều hành; đối chiếu với cơ sở dữ liệu mẫu tấn công đã biết (Signature-based) hoặc phát hiện hành vi bất thường (Anomaly-based) để **phát cảnh báo** cho quản trị viên. |
| **Ngăn ngừa xâm nhập (IPS)** | **침입 방지 시스템** (Intrusion Prevention System) | Được lắp đặt nối tiếp (In-line) trực tiếp trên đường truyền mạng; khi phát hiện gói tin tấn công, hệ thống **chủ động can thiệp chặn đứng ngay lập tức (Drop packet / Reset connection)** trước khi gói tin chạm tới mục tiêu. |
| **Vùng DMZ** | **DMZ** (Demilitarized Zone) | Vùng mạng đệm cách ly nằm giữa mạng nội bộ an toàn (Internal LAN) và Internet; là nơi bắt buộc phải bố trí các máy chủ cung cấp dịch vụ ra bên ngoài (**Web Server, Mail Server, DNS Server, FTP Server**). Nếu máy chủ trong DMZ bị tin tặc chiếm quyền, tường lửa thứ hai sẽ chặn không cho tin tặc xâm nhập sâu vào mạng nội bộ. |

- **2. Chi tiết giao thức bảo mật IPSec (IP Security) trong VPN:**
  - Hoạt động ở **Tầng mạng (Network Layer - Tầng 3)** của mô hình OSI.
  - **2 giao thức thành phần chính:**
    1. **AH (Authentication Header):** Cung cấp tính toàn vẹn (Integrity) và xác thực nguồn gốc gói tin (Authentication); **hoàn toàn không hỗ trợ mã hóa bảo mật nội dung**.
    2. **ESP (Encapsulating Security Payload):** **Cung cấp tính bảo mật (Confidentiality via Encryption)** kết hợp cùng xác thực và tính toàn vẹn; là giao thức được sử dụng chủ đạo.
  - **2 chế độ vận hành:**
    - **전송 모드 (Transport Mode):** Chỉ mã hóa phần dữ liệu Payload của gói IP; giữ nguyên tiêu đề IP Header gốc $\rightarrow$ Dùng cho kết nối Host-to-Host.
    - **터널 모드 (Tunnel Mode):** **Mã hóa toàn bộ gói tin IP ban đầu (cả Header và Payload)**, sau đó bọc thêm một tiêu đề IP Header mới ở ngoài $\rightarrow$ Dùng cho kết nối VPN mạng nối mạng (Gateway-to-Gateway).

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **So sánh IPSec VPN vs SSL/TLS VPN:**
  - *IPSec VPN:* Yêu cầu cài đặt phần mềm Client chuyên dụng trên máy tính của người dùng; cấu hình phức tạp nhưng hỗ trợ bảo vệ tất cả mọi giao thức ở tầng mạng.
  - *SSL/TLS VPN:* Hoạt động tại tầng ứng dụng thông qua trình duyệt web thông thường (HTTPS Port 443); người dùng không cần cài đặt phần mềm phụ trợ, rất thuận tiện cho nhân viên làm việc từ xa.

### 복습 체크리스트
- [ ] Ghi nhớ SSH hoạt động tại cổng số **22** để thay thế cho Telnet (cổng 23).
- [ ] Phân biệt được: IDS là phát hiện cảnh báo thụ động, IPS là chủ động chặn đứng tấn công.
- [ ] Nhớ vùng DMZ là nơi bắt buộc đặt các máy chủ Web, Mail, DNS phục vụ Internet.
- [ ] Nắm vững hai giao thức của IPSec: AH (chỉ xác thực) và ESP (mã hóa bảo mật + xác thực).
- [ ] Phân biệt được: Transport Mode giữ nguyên IP Header, Tunnel Mode mã hóa toàn bộ gói tin IP.
