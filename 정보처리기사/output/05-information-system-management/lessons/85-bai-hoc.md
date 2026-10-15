# 2. 접근 제어 정책 & 네트워크 보안 솔루션 (Chính sách Kiểm soát Truy cập & Giải pháp Bảo mật Mạng)

## 학습 목표 (Mục tiêu)
- Phân biệt toàn diện 3 mô hình chính sách kiểm soát truy cập chuẩn: Kiểm soát tùy ý (DAC), Kiểm soát bắt buộc (MAC), và Kiểm soát dựa trên vai trò (RBAC).
- Nắm vững quy tắc kiểm soát luồng thông tin trong mô hình bảo mật Bell-LaPadula (bảo vệ tính bí mật: NRU, NWD) và mô hình Biba (bảo vệ tính toàn vẹn: NRD, NWU).
- Làm chủ chức năng và phạm vi bảo vệ của các giải pháp an ninh mạng cốt lõi: Tường lửa mạng (Firewall), Tường lửa ứng dụng web (WAF), Hệ thống phát hiện/ngăn ngừa xâm nhập (IDS/IPS), và Mạng riêng ảo (VPN).

## 핵심 키워드 (Từ khóa)
- **DAC (임의적 접근 통제)**: Dựa trên danh tính (Identity), chủ sở hữu dữ liệu tự cấp quyền (Access Control List - ACL).
- **MAC (강제적 접근 통제)**: Dựa trên nhãn an ninh (Security Label), quản trị viên thiết lập bắt buộc, quy tắc quân sự.
- **RBAC (역할 기반 접근 통제)**: Dựa trên vị trí/vai trò công việc (Role), quản trị linh hoạt trong doanh nghiệp.
- **보안 모델 (Security Models)**: Bell-LaPadula (BLP - 기밀성: No Read Up, No Write Down), Biba (무결성: No Read Down, No Write Up).
- **네트워크 보안 도구**: 방화벽 (Firewall), WAF (Web Application Firewall - chặn SQLi, XSS), IDS (Detect), IPS (Prevent), VPN (Tunneling/Encryption).

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [83-bai-hoc.md](83-bai-hoc.md) (Khái niệm chủ thể, đối tượng và kiểm soát truy cập).
- Liên kết với [72-bai-hoc.md](72-bai-hoc.md) (Hệ thống IDS và IPS chi tiết).
- Liên kết với [22-bai-hoc.md](22-bai-hoc.md) (Giao thức VPN và tường lửa).

## 읽는 방법 (Cách đọc)
- Phân biệt các mô hình kiểm soát truy cập trong đề thi:
  - "Chủ sở hữu dữ liệu (Owner) tự quyết định trao quyền cho ai" $\rightarrow$ **DAC (임의적)**.
  - "Dựa trên cấp bậc an ninh (Top Secret, Secret), hệ thống bắt buộc thực thi" $\rightarrow$ **MAC (강제적)**.
  - "Gán quyền theo chức danh công việc của nhân viên trong công ty" $\rightarrow$ **RBAC (역할 기반)**.
  - Mô hình Bell-LaPadula (BLP): Chuyên về **Bí mật (기밀성)** $\rightarrow$ **Không đọc lên (NRU), Không ghi xuống (NWD)**.
  - Mô hình Biba: Chuyên về **Toàn vẹn (무결성)** $\rightarrow$ **Không đọc xuống (NRD), Không ghi lên (NWU)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng so sánh 3 Mô hình Kiểm soát Truy cập (Access Control Models)
| Mô hình (KR / EN) | Căn cứ cấp quyền | Ai là người quyết định quyền? | Đặc điểm kỹ thuật | Trường hợp sử dụng |
| :--- | :--- | :--- | :--- | :--- |
| **DAC / (Discretionary Access Control)** | **Danh tính người dùng / (Identity)** | **Chủ sở hữu dữ liệu / (Data Owner)** | Sử dụng danh sách kiểm soát truy cập (**ACL**); Người tạo file có toàn quyền trao quyền đọc/sửa cho người khác; Linh hoạt nhưng dễ rò rỉ nếu chủ sở hữu bất cẩn | Hệ thống tệp thông thường (Windows NTFS, Linux file permissions) |
| **MAC / (Mandatory Access Control)** | **Nhãn bảo mật / (Security Label)** | **Quản trị viên hệ điều hành / (System Admin)** | So sánh cấp độ an ninh của Chủ thể (Clearance) và Đối tượng (Classification); Người dùng không thể tự nhượng quyền; Cực kỳ khắt khe | Hệ thống quốc phòng, tình báo quân đội, Secure OS |
| **RBAC / (Role-Based Access Control)** | **Vai trò / Chức danh / (User Role)** | **Quản trị viên doanh nghiệp / (Central Admin)** | Quyền hạn được gán cho **Vai trò (Role)**, sau đó người dùng được gán vào Vai trò đó; Tuân thủ nguyên tắc đặc quyền tối thiểu (Least Privilege) | Hệ thống thông tin doanh nghiệp, Ngân hàng, Bệnh viện |

#### 2. Hai Mô hình Bảo mật Hình thức: Bell-LaPadula vs Biba
- **Mô hình Bell-LaPadula (BLP Model - Trọng tâm Tính Bí mật / 기밀성)**:
  - Được thiết kế cho Bộ Quốc phòng Mỹ nhằm chống lộ lọt thông tin tối mật xuống cấp dưới:
  - **No Read Up (NRU / Simple Security Property)**: Chủ thể cấp thấp **không được đọc** dữ liệu của đối tượng có cấp bảo mật cao hơn.
  - **No Write Down (NWD / Star-Property $\star$)**: Chủ thể cấp cao **không được ghi** dữ liệu xuống đối tượng có cấp bảo mật thấp hơn (để ngăn vô tình làm rò rỉ tài liệu mật ra vùng công cộng).
- **Mô hình Biba (Biba Integrity Model - Trọng tâm Tính Toàn vẹn / 무결성)**:
  - Được thiết kế nhằm ngăn chặn việc dữ liệu không đáng tin cậy làm sai lệch hoặc phá hỏng dữ liệu quan trọng:
  - **No Read Down (NRD / Simple Integrity Property)**: Chủ thể cấp cao **không được đọc** dữ liệu từ đối tượng cấp thấp hơn (tránh đọc phải dữ liệu rác, chưa kiểm chứng).
  - **No Write Up (NWU / Star-Integrity Property $\star$)**: Chủ thể cấp thấp **không được ghi** vào đối tượng cấp cao hơn (ngăn kẻ không đủ thẩm quyền phá hoại tài liệu chính thức).

#### 3. Bảng các Giải pháp An ninh Mạng Doanh nghiệp
| Giải pháp an ninh | Tầng mạng bảo vệ | Cơ chế hoạt động cốt lõi | Mối đe dọa ngăn chặn |
| :--- | :--- | :--- | :--- |
| **방화벽 (Firewall)** | Tầng 3 (Network) và Tầng 4 (Transport) | Kiểm tra IP nguồn, IP đích, Cổng dịch vụ (Port); Lọc gói tin (Packet Filtering) và theo dõi trạng thái kết nối (Stateful Inspection) | Chặn truy cập trái phép từ bên ngoài, đóng các cổng dịch vụ nguy hiểm |
| **WAF (Web Application Firewall)** | Tầng 7 (Application Layer) | Phân tích sâu nội dung Payload của các yêu cầu HTTP/HTTPS | Ngăn chặn các đòn tấn công ứng dụng web: **SQL Injection, XSS, CSRF** |
| **IDS (Intrusion Detection)** | Tầng 2 đến Tầng 7 (Nối song song) | Bắt gói tin, so khớp mẫu chữ ký hoặc phát hiện bất thường, gửi cảnh báo ghi log | Giám sát và phát hiện xâm nhập thời gian thực |
| **IPS (Intrusion Prevention)** | Tầng 2 đến Tầng 7 (Nối tiếp Inline) | Nằm trực tiếp trên luồng truyền, tự động ngắt kết nối và thả bỏ gói tin độc hại | Ngăn chặn tức thì các hành vi tấn công mạng |
| **VPN (Virtual Private Network)** | Tầng 3 (IPSec) hoặc Tầng 4-7 (SSL/TLS) | Thiết lập đường hầm mã hóa an toàn (Tunneling & Encryption) truyền qua mạng Internet công cộng | Chống nghe lén (Sniffing), cho phép nhân viên truy cập mạng nội bộ an toàn từ xa |

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Ma trận đối chiếu quy tắc của Bell-LaPadula và Biba
```
                  ┌──────────────────────────────┬──────────────────────────────┐
                  │   Mô hình Bell-LaPadula      │         Mô hình Biba         │
                  │   (Trọng tâm: KHOÁ BÍ MẬT)   │   (Trọng tâm: TÍNH TOÀN VẸN) │
├─────────────────┼──────────────────────────────┼──────────────────────────────┤
│ Quy tắc Đọc     │ No Read Up (NRU)             │ No Read Down (NRD)           │
│ (Reading)       │ (Cấm đọc lên mức mật hơn)    │ (Cấm đọc xuống mức bẩn hơn)  │
├─────────────────┼──────────────────────────────┼──────────────────────────────┤
│ Quy tắc Ghi     │ No Write Down (NWD)          │ No Write Up (NWU)            │
│ (Writing)       │ (Cấm ghi xuống mức thấp hơn) │ (Cấm ghi lên mức cao hơn)    │
└─────────────────┴──────────────────────────────┴──────────────────────────────┘
```

---

### 복습 체크리스트
- [ ] Sự khác biệt cốt lõi giữa hai chính sách kiểm soát truy cập DAC và MAC là gì?
- [ ] Tại sao trong mô hình Bell-LaPadula, một tướng quân đội cấp cao lại không được phép ghi (Write) vào tệp tin ở mức Unclassified (No Write Down)?
- [ ] Mô hình Biba được thiết kế nhằm bảo vệ thuộc tính an toàn nào trong CIA Triad?
- [ ] Tường lửa ứng dụng web (WAF) khác với Tường lửa truyền thống (Firewall) ở những điểm kỹ thuật nào?
