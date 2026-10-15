# 인증 및 보안 체계 (Authentication & Security System)

## 학습 목표 (Mục tiêu)
- Phân biệt 4 nhóm nhân tố xác thực người dùng (지식, 소유, 생체, 위치/행위 기반 인증).
- Hiểu rõ khái niệm và lợi ích của xác thực đa nhân tố (Multi-Factor Authentication - MFA).
- Phân loại toàn diện 3 lĩnh vực bảo vệ hệ thống thông tin: Quản trị (관리적), Vật lý (물리적), Kỹ thuật (기술적 보안).

## 핵심 키워드 (Từ khóa)
- **인증 4요소 (4 Factors)**: 지식 기반 (Something You Know), 소유 기반 (Something You Have), 생체 기반 (Something You Are), 위치/행위 기반 (Somewhere You Are / Something You Do).
- **MFA (다중 인증)**: Xác thực đa yếu tố độc lập nhằm triệt tiêu rủi ro lộ mật khẩu đơn thuần.
- **보안 3영역**: 관리적 보안 (Administrative), 물리적 보안 (Physical), 기술적 보안 (Technical).

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [26-bai-hoc.md](26-bai-hoc.md) (정보 보안 일반 및 시스템 보안 - CIA Triad và bảo mật hệ thống).
- Liên kết với [31-bai-hoc.md](31-bai-hoc.md) (소프트웨어 개발 보안 관련 법규 - Quy định quản lý an toàn thông tin cá nhân).
- Liên kết với [36-bai-hoc.md](36-bai-hoc.md) (접근 통제 모델 - Kiểm soát truy cập sau khi đã xác thực).

## 읽는 방법 (Cách đọc)
- Phân biệt câu hỏi trắc nghiệm:
  - Hỏi "dựa vào trí nhớ của người dùng" -> 지식 기반 (Mật khẩu, PIN).
  - Hỏi "vật thể người dùng cầm theo" -> 소유 기반 (Thẻ thông minh, mã OTP tạo từ token).
  - Hỏi "đặc điểm sinh học không thay đổi" -> 생체 기반 (Vân tay, mống mắt).
  - Chú ý: MFA phải kết hợp các yếu tố **khác loại**, ví dụ Mật khẩu (Tri thức) + OTP (Sở hữu). Nếu dùng 2 mật khẩu khác nhau thì vẫn chỉ là xác thực 1 nhân tố.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bốn nhóm nhân tố xác thực (Authentication Factors)
| Nhóm nhân tố | Nguyên lý nhận diện | Ví dụ kỹ thuật tiêu biểu | Ưu điểm & Thách thức |
| :--- | :--- | :--- | :--- |
| **지식 기반 / (Something You Know)** | Dựa trên những gì người dùng ghi nhớ trong đầu | Mật khẩu (Password), mã PIN, câu hỏi bảo mật cá nhân | Dễ triển khai, chi phí thấp; Dễ bị quên, bị đoán mò hoặc tấn công vét cạn (Brute-force) |
| **소유 기반 / (Something You Have)** | Dựa trên vật thể vật lý hoặc thiết bị người dùng đang nắm giữ | Thẻ thông minh (Smart Card), Khóa bảo mật phần cứng (FIDO2/U2F), Thiết bị OTP Token, SMS OTP | Khó bị tấn công từ xa thuần túy; Có nguy cơ bị mất cắp vật lý, thất lạc |
| **생체 기반 / (Something You Are)** | Dựa trên đặc trưng sinh học sinh trắc duy nhất của cơ thể người dùng | Dấu vân tay, mống mắt (Iris), võng mạc (Retina), khuôn mặt (Face ID), tĩnh mạch ngón tay/lòng bàn tay | Không thể quên hoặc đánh rơi; Tỷ lệ nhận diện sai (FAR/FRR), chi phí thiết bị đọc cao |
| **위치/행위 기반 / (Somewhere You Are / Does)** | Dựa trên vị trí địa lý hoặc thói quen hành vi độc động học | Vị trí GPS, dải IP mạng nội bộ cơ quan, nhịp điệu gõ bàn phím (Keystroke Dynamics), chữ ký tay số | Ngăn chặn đăng nhập bất thường ngoài vùng cho phép; Độ chính xác phụ thuộc điều kiện môi trường |

#### 2. Phân loại 3 lĩnh vực bảo mật (Security Domains)
- **관리적 보안 (Bảo mật quản trị - Con người & Quy trình)**:
  - Thiết lập chính sách an toàn thông tin (Security Policy), quy chế nội bộ, hướng dẫn vận hành.
  - Tổ chức phòng ban an ninh, phân công trách nhiệm rõ ràng (CISO, Security Officer).
  - Đào tạo nhận thức an toàn thông tin định kỳ cho toàn bộ nhân viên.
  - Xây dựng kế hoạch kinh doanh liên tục (BCP - Business Continuity Planning) và quy trình ứng phó sự cố an ninh.
  - Thực hiện kiểm toán nội bộ và kiểm toán độc lập định kỳ.
- **물리적 보안 (Bảo mật vật lý - Cơ sở hạ tầng)**:
  - Kiểm soát người ra vào khu vực máy chủ, trung tâm dữ liệu (Cổng an ninh, bảo vệ 24/7, đầu đọc thẻ từ, khóa sinh trắc học).
  - Hệ thống giám sát camera CCTV ghi hình, cảm biến chuyển động.
  - Biện pháp phòng chống thiên tai: Hệ thống chữa cháy khí sạch (FM-200, Novec), chống sét lan truyền, sàn nâng chống ngập nước.
  - Hệ thống cấp nguồn điện liên tục (UPS) và máy phát điện dự phòng khẩn cấp.
- **기술적 보안 (Bảo mật kỹ thuật - Công nghệ IT)**:
  - Cơ chế nhận dạng và xác thực người dùng (ID/Password, MFA).
  - Kiểm soát truy cập (Access Control) phân quyền theo vai trò hoặc theo nhãn an ninh.
  - Mã hóa dữ liệu lưu trữ (Data-at-Rest) và dữ liệu truyền trên đường truyền (Data-in-Transit).
  - Triển khai các giải pháp an ninh chuyên dụng: Tường lửa (Firewall), Hệ thống phát hiện/ngăn ngừa xâm nhập (IDS/IPS), Chống thất thoát dữ liệu (DLP), Mạng riêng ảo (VPN).

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Hai chỉ số sai số trong xác thực sinh trắc học (Biometrics)
- **FAR (False Acceptance Rate - Tỷ lệ chấp nhận sai)**: Tỷ lệ kẻ giả mạo (Impostor) không được phép nhưng hệ thống lại nhận diện nhầm là người dùng hợp lệ và cấp quyền truy cập. Chỉ số này phản ánh **độ an toàn** của hệ thống (FAR càng thấp càng an toàn).
- **FRR (False Rejection Rate - Tỷ lệ từ chối sai)**: Tỷ lệ người dùng thật, hợp lệ nhưng hệ thống lại từ chối cấp quyền. Chỉ số này phản ánh **độ tiện dụng** của hệ thống.
- **CER (Crossover Error Rate) / EER (Equal Error Rate)**: Điểm giao thoa mà tại đó giá trị FAR bằng FRR. EER càng thấp thì chất lượng của thuật toán sinh trắc học càng cao.

#### 2. Kiến trúc tổng thể 3 lĩnh vực bảo vệ an toàn thông tin
```
                  ┌──────────────────────────────────────────────┐
                  │          CHÍNH SÁCH BẢO MẬT QUẢN TRỊ         │
                  │ (Đào tạo nhân sự, BCP/DRP, Quy chế nội bộ)   │
                  └──────────────────────┬───────────────────────┘
                                         │ bao bọc
                  ┌──────────────────────▼───────────────────────┐
                  │            HÀNG RÀO BẢO VỆ VẬT LÝ            │
                  │ (Phòng Data Center, Khóa từ, Camera, UPS)    │
                  └──────────────────────┬───────────────────────┘
                                         │ bao bọc
                  ┌──────────────────────▼───────────────────────┐
                  │             BẢO VỆ BẰNG KỸ THUẬT             │
                  │ (Tường lửa, Mã hóa, Xác thực MFA, IDS/IPS)   │
                  └──────────────────────────────────────────────┘
```

---

### 복습 체크리스트
- [ ] Bốn nhân tố xác thực cơ bản gồm những gì và mỗi nhân tố lấy một ví dụ điển hình?
- [ ] Tại sao việc sử dụng đồng thời mật khẩu và mã PIN không được coi là xác thực đa nhân tố (MFA)?
- [ ] Việc lắp đặt hệ thống chữa cháy khí FM-200 trong phòng server thuộc lĩnh vực bảo mật nào?
- [ ] Khái niệm FAR và FRR trong xác thực sinh trắc học đo lường sai số gì của hệ thống?
