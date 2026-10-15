# 24. 인터페이스 보안 - 네트워크 영역 (Interface Security - Network Area)

## 학습 목표 (Mục tiêu)
- Nắm vững các giải pháp và giao thức bảo mật dữ liệu truyền thông trên phân vùng mạng (네트워크 영역 보안) khi các ứng dụng kết nối giao tiếp với nhau.
- Phân biệt rõ các giao thức mã hóa đường truyền phổ biến trong đề thi: IPSec (tầng mạng L3), SSL/TLS (tầng giao vận L4/phiên L5), và S-HTTP (tầng ứng dụng L7).
- Hiểu cấu trúc và hai chế độ hoạt động của IPSec: Chế độ truyền tải (Transport Mode) và Chế độ đường hầm (Tunnel Mode).

## 핵심 키워드 (Từ khóa)
- 인터페이스 보안 (Interface Security)
- 네트워크 영역 암호화 (Network Traffic Encryption)
- IPSec (IP Security / AH, ESP, IKE)
- 전송 모드 vs 터널 모드 (Transport Mode vs Tunnel Mode)
- SSL/TLS (Secure Sockets Layer / Transport Layer Security)
- S-HTTP (Secure Hypertext Transfer Protocol)

## 선행·연결 개념 (Kiến thức liên kết)
- [68-bai-hoc.md](68-bai-hoc.md): Tối ưu hóa truy vấn dữ liệu và kế hoạch thực thi.
- [70-bai-hoc.md](70-bai-hoc.md): Công cụ kiểm thử và xác minh triển khai giao diện.
- [정보처리기사/output/05-information-system-management/lessons/01-bai-hoc.md](../../05-information-system-management/lessons/01-bai-hoc.md): Kiến trúc an toàn thông tin và bảo mật mạng.

## 읽는 방법 (Cách đọc)
- Phân tầng giao thức bảo mật theo mô hình OSI:
  - **Tầng mạng (Network Layer - L3):** **IPSec** (Mã hóa toàn bộ gói tin IP ở mức hệ điều hành, bảo vệ mọi ứng dụng chạy phía trên).
  - **Tầng giao vận/phiên (Transport/Session Layer - L4/L5):** **SSL/TLS** (Bảo vệ luồng TCP, dùng phổ biến trong HTTPS).
  - **Tầng ứng dụng (Application Layer - L7):** **S-HTTP** (Chỉ mã hóa từng thông điệp HTTP riêng lẻ thay vì toàn bộ kênh truyền).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh 3 giao thức bảo mật giao diện mạng:**

| Giao thức bảo mật | Tầng OSI đối ứng | Đặc điểm cơ chế hoạt động | Phạm vi ứng dụng thực tế |
| :--- | :--- | :--- | :--- |
| **IPSec (IP Security)** | **Tầng mạng (L3 - Network)** | Cung cấp dịch vụ bảo mật ở mức gói tin IP. Bao gồm giao thức xác thực **AH** (Authentication Header) và giao thức mã hóa dữ liệu **ESP** (Encapsulating Security Payload) | Thiết lập mạng riêng ảo **VPN**, kết nối an toàn giữa các máy chủ chi nhánh |
| **SSL / TLS** | **Tầng giao vận (L4/L5 - Transport)** | Sử dụng mã hóa bất đối xứng để trao đổi khóa và chứng chỉ số (X.509), sau đó dùng mã hóa đối xứng để truyền dữ liệu tốc độ cao | Truyền web an toàn (**HTTPS / Port 443**), email bảo mật (FTPS, SMTPS) |
| **S-HTTP** | **Tầng ứng dụng (L7 - Application)** | Chỉ mã hóa nội dung của thông điệp HTTP cụ thể giữa Client và Server; không tạo kênh truyền mã hóa toàn diện | Kiểm soát bảo mật chi tiết từng thông điệp riêng lẻ (ít dùng hơn SSL/TLS) |

- **Hai chế độ hoạt động của IPSec (IPSec Modes):**

| Chế độ | Phạm vi mã hóa (Encrypted Area) | IP Header mới | Ngữ cảnh ứng dụng |
| :--- | :--- | :--- | :--- |
| **전송 모드 (Transport Mode)** | Chỉ mã hóa **Payload (Dữ liệu)**; giữ nguyên IP Header gốc | **Không tạo** IP Header mới | Giao tiếp trực tiếp giữa 2 máy trạm (Host-to-Host) |
| **터널 모드 (Tunnel Mode)** | Mã hóa **toàn bộ gói tin IP gốc** (Cả Header cũ lẫn Payload) | **Tạo thêm** New IP Header ở bên ngoài | Kết nối giữa hai cổng mạng an toàn qua VPN (Gateway-to-Gateway) |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Các thành phần cốt lõi của bộ giao thức IPSec:**
  - **AH (Authentication Header):** Đảm bảo tính toàn vẹn (Integrity) và xác thực nguồn gốc dữ liệu; chống phát lại (Anti-replay). Không có chức năng mã hóa bảo mật bí mật (Confidentiality).
  - **ESP (Encapsulating Security Payload):** Cung cấp cả tính bảo mật (Mã hóa nội dung) lẫn xác thực nguồn gốc và toàn vẹn.
  - **IKE (Internet Key Exchange):** Cơ chế quản lý và thương lượng khóa mật mã tự động giữa hai đầu thiết bị truyền thông.

### 복습 체크리스트
- [ ] Phân loại tầng hoạt động của IPSec (L3), SSL/TLS (L4/L5), và S-HTTP (L7).
- [ ] Nắm chắc sự khác biệt giữa IPSec Transport Mode (chỉ mã hóa dữ liệu) và Tunnel Mode (mã hóa cả gói tin cũ + bọc IP Header mới).
- [ ] Nhớ vai trò của AH (xác thực/toàn vẹn) và ESP (mã hóa + xác thực).
