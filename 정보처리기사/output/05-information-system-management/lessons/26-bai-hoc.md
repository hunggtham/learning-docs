# 8. 정보 보안 일반 및 시스템 보안 (Bảo mật thông tin & Hệ thống)

## 학습 목표 (Mục tiêu)
- Nắm vững 3 thuộc tính nền tảng của an toàn thông tin (보안 3대 요소 - CIA Triad: 기밀성, 무결성, 가용성).
- Phân biệt các mô hình bảo mật phần mềm (Seven Touchpoints, OWASP) và phân loại bảo mật (관리적, 물리적, 기술적).
- Hiểu rõ các giải pháp bảo vệ hệ thống: TCP Wrapper, Secure OS, Hệ thống phát hiện xâm nhập (IDS - 오용 탐지 vs 이상 탐지), High Availability (HACMP), và các yếu tố xác thực.

## 핵심 키워드 (Từ khóa)
- **보안 3대 요소 (CIA Triad)**: 기밀성 (Confidentiality), 무결성 (Integrity), 가용성 (Availability).
- **보안 프레임워크**: Seven Touchpoints (tích hợp thực tiễn bảo mật vào SDLC), OWASP (Tổ chức an ninh ứng dụng web mở).
- **보안 체계 3영역**: 관리적 (Administrative), 물리적 (Physical), 기술적 (Technical).
- **시스템 보안 도구**: TCP Wrapper (kiểm soát truy cập dựa trên file hosts.allow/deny), Secure OS (bảo vệ hạt nhân kernel), IDS (침입 탐지 시스템), HACMP (고가용성 이중화).
- **인증 3대 요소 (Authentication Factors)**: 지식 기반 (Something you know), 소유 기반 (Something you have), 생체/행위 기반 (Something you are/do).

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [27-bai-hoc.md](27-bai-hoc.md) (해킹 및 보안 위협 - Các mối đe dọa và tấn công mạng).
- Liên kết với [30-bai-hoc.md](30-bai-hoc.md) (인증 및 보안 체계 - Phân loại chi tiết cơ chế xác thực và phạm vi an ninh).
- Liên kết với [04-programming-language/70-bai-hoc.md](../../04-programming-language/lessons/70-bai-hoc.md) (Security vulnerabilities trong mã nguồn).

## 읽는 방법 (Cách đọc)
- Đi thi chú trọng nhận diện định nghĩa CIA Triad: hỏi "người được cấp quyền mới được đọc" -> 기밀성, "chỉ người được phép mới sửa" -> 무결성, "cần là dùng được ngay" -> 가용성.
- Phân biệt cơ chế IDS: Signature-based (오용 탐지 - biết mẫu sẵn) vs Anomaly-based (이상 탐지 - phát hiện hành vi sai lệch mức chuẩn).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. 보안 3대 요소 (CIA Triad)
| Yếu tố (KR / EN) | Định nghĩa cốt lõi | Biện pháp kỹ thuật tiêu biểu |
| :--- | :--- | :--- |
| **기밀성 (Confidentiality)** | Chỉ người dùng/tiến trình được ủy quyền mới có thể truy cập đọc thông tin | Mã hóa dữ liệu (Encryption), kiểm soát truy cập (Access Control) |
| **무결성 (Integrity)** | Thông tin chỉ có thể được chỉnh sửa/xóa bởi đối tượng được ủy quyền, không bị sửa đổi trái phép | Chữ ký số (Digital Signature), hàm băm kiểm tra (Hash, MAC) |
| **가용성 (Availability)** | Tài nguyên và dịch vụ luôn sẵn sàng phục vụ khi người dùng hợp lệ yêu cầu | Dự phòng phần cứng (Redundancy, RAID), cân bằng tải, chống DDoS, sao lưu dữ liệu |

#### 2. Khung bảo mật và Phân loại an ninh
- **Seven Touchpoints (Gary McGraw)**: Phương pháp luận tích hợp 7 hoạt động thực tiễn bảo mật tốt nhất vào từng pha của vòng đời phát triển phần mềm (SDLC).
- **OWASP (Open Web Application Security Project)**: Tổ chức phi lợi nhuận toàn cầu nghiên cứu các lỗ hổng bảo mật web, định kỳ công bố tài liệu OWASP Top 10.
- **Phân loại 3 lớp bảo mật**:
  - **관리적 보안 (Bảo mật quản trị)**: Chính sách an toàn thông tin, quy trình nghiệp vụ, đào tạo nhân sự, kiểm toán bảo mật.
  - **물리적 보안 (Bảo mật vật lý)**: Kiểm soát ra vào trung tâm dữ liệu, khóa cửa, camera CCTV, cảm biến cháy nổ, phòng chống thiên tai.
  - **기술적 보안 (Bảo mật kỹ thuật)**: Xác thực người dùng, ủy quyền, tường lửa (Firewall), hệ thống IDS/IPS, mã hóa mạng và cơ sở dữ liệu.

#### 3. Hệ thống bảo mật & Giám sát xâm nhập
- **TCP Wrapper**: Công cụ kiểm soát truy cập tầng mạng dựa trên phần mềm máy chủ, kiểm tra quyền của client qua file `/etc/hosts.allow` và `/etc/hosts.deny` trước khi chuyển tiếp cho daemon dịch vụ.
- **Secure OS**: Hệ điều hành được tích hợp nhân bảo mật (Security Kernel) nhằm thực thi cơ chế kiểm soát truy cập bắt buộc (MAC) và phân vùng tài nguyên an toàn.
- **침입 탐지 시스템 (IDS - Intrusion Detection System)**:
  - **오용 탐지 (Misuse/Signature Detection)**: So khớp lưu lượng với cơ sở dữ liệu mẫu chữ ký tấn công đã biết. Ưu điểm: Tỷ lệ báo động giả (False Positive) thấp. Nhược điểm: Không phát hiện được tấn công mới (Zero-day).
  - **이상 탐지 (Anomaly Detection)**: Thiết lập hồ sơ hành vi bình thường, cảnh báo khi phát hiện độ lệch bất thường. Ưu điểm: Có thể phát hiện tấn công mới. Nhược điểm: Tỷ lệ báo động giả cao.
- **HACMP (High Availability Cluster Multi-Processing)**: Giải pháp máy chủ cụm của IBM đảm bảo tính sẵn sàng cao (High Availability), tự động chuyển đổi dự phòng (failover) sang node phụ khi node chính gặp sự cố.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. So sánh chi tiết hai mô hình IDS
```
                 [Lưu lượng mạng / Nhật ký hệ thống]
                                 │
         ┌───────────────────────┴───────────────────────┐
         ▼                                               ▼
[오용 탐지 (Signature)]                         [이상 탐지 (Anomaly)]
- So khớp với mẫu tấn công đã biết              - So sánh với ngưỡng hành vi chuẩn
- Tỷ lệ cảnh báo giả rất thấp                   - Có khả năng chặn Zero-day Attack
- Không phát hiện được biến thể mới             - Dễ báo động nhầm người dùng hợp lệ
```

#### 2. Kỹ thuật ghi nhớ các nhân tố xác thực (Authentication Factors)
- **Something you know (지식)**: Mật khẩu (Password), mã PIN, câu hỏi bảo mật.
- **Something you have (소유)**: Thẻ thông minh (Smart card), khóa bảo mật phần cứng OTP, token USB.
- **Something you are (생체)**: Vân tay, quét mống mắt (Iris), nhận diện khuôn mặt, cấu trúc tĩnh mạch.
- **Multi-Factor Authentication (MFA)**: Kết hợp từ 2 nhóm yếu tố độc lập trở lên để nâng cao an toàn.

---

### 복습 체크리스트
- [ ] Bạn có thể giải thích sự khác biệt giữa 3 thành phần của CIA Triad không?
- [ ] Điểm khác biệt cốt lõi giữa IDS 오용 탐지 (Signature) và 이상 탐지 (Anomaly) là gì?
- [ ] TCP Wrapper quyết định cấp quyền truy cập dựa trên những tệp tin cấu hình nào?
- [ ] Ba lĩnh vực bảo mật (Quản trị, Vật lý, Kỹ thuật) bao gồm những biện pháp triển khai cụ thể nào?
