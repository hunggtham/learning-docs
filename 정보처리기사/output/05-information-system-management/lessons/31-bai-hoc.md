# 소프트웨어 개발 보안 관련 법규 (Hệ thống Pháp luật Bảo mật Phần mềm)

## 학습 목표 (Mục tiêu)
- Nắm vững các đạo luật cốt lõi điều chỉnh bảo mật dữ liệu và phát triển phần mềm tại Hàn Quốc trong phạm vi đề thi Kỹ sư xử lý thông tin.
- Phân biệt phạm vi áp dụng và đối tượng quản lý của 4 đạo luật chính: Đạo luật bảo vệ thông tin cá nhân (개인정보 보호법), Luật mạng thông tin truyền thông (정보통신망법), Luật thông tin tín dụng (신용정보법), Luật thông tin vị trí (위치정보법).
- Hiểu rõ các quy định kỹ thuật bắt buộc khi lập trình: mã hóa mật khẩu một chiều, bảo vệ số định danh cá nhân độc nhất, hủy bỏ dữ liệu khi hết thời hạn lưu trữ.

## 핵심 키워드 (Từ khóa)
- **개인정보 보호법 (Personal Information Protection Act)**: Luật cơ sở bảo vệ mọi thông tin cá nhân, định danh độc nhất (주민등록번호), mật khẩu băm một chiều, CPO.
- **정보통신망법 (Network Act)**: Áp dụng cho nhà cung cấp dịch vụ thông tin truyền thông (ISP, cổng thông tin, app online), chứng nhận ISMS.
- **신용정보법 (Credit Information Act)**: Bảo vệ thông tin tài chính, giao dịch thẻ, lịch sử tín dụng trong khối ngân hàng/tài chính.
- **위치정보법 (Location Information Act)**: Quản lý việc thu thập và sử dụng tọa độ GPS, trạm phát sóng di động của người dùng cá nhân.

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [30-bai-hoc.md](30-bai-hoc.md) (인증 및 보안 체계 - Bảo mật quản trị và chính sách an toàn).
- Liên kết với [33-bai-hoc.md](33-bai-hoc.md) (보안 기능 및 에러 처리 - Lỗi lưu mật khẩu dạng bản rõ).
- Liên kết với [34-bai-hoc.md](34-bai-hoc.md) (암호화 기술 - Kỹ thuật băm và mã hóa thông tin nhạy cảm).

## 읽는 방법 (Cách đọc)
- Phân biệt phạm vi áp dụng:
  - Nếu đối tượng là **toàn bộ các tổ chức, doanh nghiệp, cơ quan nhà nước xử lý thông tin cá nhân** -> chọn **개인정보 보호법**.
  - Nếu câu hỏi nhấn mạnh **nhà cung cấp dịch vụ mạng thông tin truyền thông (ISP, cổng thông tin web)** -> chọn **정보통신망법**.
  - Nếu nói về **giao dịch tài chính, điểm tín dụng, ngân hàng, công ty thẻ** -> chọn **신용정보법**.
  - Nếu nói về **vị trí địa lý, tọa độ GPS của thiết bị di động** -> chọn **위치정보법**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng so sánh 4 đạo luật bảo mật công nghệ thông tin
| Tên đạo luật (KR / EN) | Đối tượng và Phạm vi áp dụng | Nội dung kỹ thuật và Chế tài trọng tâm |
| :--- | :--- | :--- |
| **개인정보 보호법 / (Personal Information Protection Act)** | Mọi cơ quan công quyền, doanh nghiệp, cá nhân xử lý thông tin cá nhân (Luật chung - General Law) | - Bắt buộc mã hóa thông tin định danh độc nhất (Số CMND/Căn cước 주민등록번호, Số hộ chiếu, Số bằng lái) / - Bắt buộc mã hóa **một chiều (One-way Hash)** đối với mật khẩu / - Phải bổ nhiệm Cán bộ bảo vệ thông tin cá nhân (CPO - Chief Privacy Officer) / - Tiêu hủy dữ liệu ngay khi đạt mục đích hoặc hết thời hạn bảo quản |
| **정보통신망법 / (Network Act)** | Các doanh nghiệp cung cấp dịch vụ thông tin truyền thông (ISP, sàn thương mại điện tử, mạng xã hội) | - Bảo vệ an toàn mạng thông tin, kiểm soát thư rác (Spam) / - Bắt buộc thông báo cho người dùng và cơ quan quản lý khi xảy ra rò rỉ dữ liệu trong vòng 24 giờ / - Quy định chứng nhận Hệ thống quản lý an toàn thông tin (ISMS) |
| **신용정보법 / (Credit Information Act)** | Tổ chức tài chính, ngân hàng, công ty phát hành thẻ tín dụng, tổ chức đánh giá tín nhiệm | - Quản lý chặt chẽ thông tin giao dịch tài chính, số tài khoản, số thẻ tín dụng, lịch sử vay vốn / - Ngăn chặn sử dụng trái phép thông tin tín dụng khách hàng cho mục đích tiếp thị khi chưa được đồng ý riêng biệt |
| **위치정보법 / (Location Information Act)** | Doanh nghiệp thu thập hoặc sử dụng dữ liệu định vị cá nhân (dịch vụ gọi xe, bản đồ, giao hàng) | - Thu thập dữ liệu vị trí phải có sự đồng ý riêng (Consent) của chủ thể dữ liệu / - Cấm giám sát vị trí cá nhân trái pháp luật / - Lập quy trình lưu trữ và hủy bỏ lịch sử vị trí sau thời gian quy định |

#### 2. Các yêu cầu kỹ thuật lập trình bảo mật theo luật định
- **Xử lý mật khẩu (Password Handling)**: Mật khẩu của người dùng không bao giờ được lưu trữ dưới dạng bản rõ (Plaintext) hoặc mã hóa có thể giải mã hai chiều. Bắt buộc phải sử dụng hàm băm một chiều an toàn (như SHA-256, SHA-512) kết hợp với kỹ thuật thêm muối (Salting) và kéo dài khóa (Key Stretching như bcrypt, PBKDF2).
- **Mã hóa số nhận dạng độc nhất (Unique Identifiers)**: Số căn cước (주민등록번호), số hộ chiếu, số bằng lái xe lưu trữ trên cơ sở dữ liệu hoặc truyền trên mạng công cộng phải được mã hóa bằng thuật toán đối xứng an toàn (như AES-256, SEED, ARIA).
- **Nguyên tắc giảm thiểu dữ liệu (Data Minimization)**: Chỉ thu thập các trường thông tin tối thiểu cần thiết để cung cấp dịch vụ; các trường thông tin bổ sung không bắt buộc không được dùng làm điều kiện từ chối cung cấp dịch vụ cơ bản.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Hệ thống chứng nhận an toàn thông tin ISMS-P tại Hàn Quốc
```
    ┌────────────────────────────────────────────────────────┐
    │          ISMS-P (Hệ thống chứng nhận tích hợp)         │
    ├─────────────────────────────┬──────────────────────────┤
    │  ISMS (An toàn thông tin)   │ PIMS (Bảo vệ thông tin)  │
    │  - Quản lý chính sách       │ - Thu thập thông tin     │
    │  - Bảo mật kỹ thuật         │ - Lưu trữ & Sử dụng      │
    │  - Ứng phó sự cố mạng       │ - Tiêu hủy dữ liệu       │
    │  - Quản lý hạ tầng máy chủ  │ - Bảo vệ quyền chủ thể   │
    └─────────────────────────────┴──────────────────────────┘
```
- **ISMS-P**: Sự hợp nhất giữa ISMS (Information Security Management System - quản lý an ninh hệ thống kỹ thuật) và PIMS (Personal Information Management System - quản lý vòng đời dữ liệu riêng tư cá nhân).
- Các doanh nghiệp đạt doanh thu hoặc lượng người dùng web/ứng dụng quy mô lớn theo ngưỡng luật định bắt buộc phải trải qua đánh giá kiểm toán và duy trì chứng nhận ISMS-P hàng năm.

---

### 복습 체크리스트
- [ ] Sự khác biệt về phạm vi áp dụng giữa 개인정보 보호법 và 정보통신망법 là gì?
- [ ] Theo quy định pháp luật, mật khẩu của người dùng phải được lưu trữ bằng cơ chế mã hóa nào?
- [ ] Những loại thông tin nhận dạng độc nhất nào bắt buộc phải mã hóa an toàn khi lưu trữ trong cơ sở dữ liệu?
- [ ] Đạo luật nào điều chỉnh việc doanh nghiệp theo dõi tọa độ GPS của người dùng thông qua ứng dụng di động?
