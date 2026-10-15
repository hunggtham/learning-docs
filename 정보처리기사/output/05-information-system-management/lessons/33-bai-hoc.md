# 4. 보안 기능 및 에러 처리 (Chức năng bảo mật & Xử lý lỗi)

## 학습 목표 (Mục tiêu)
- Nắm vững 4 lỗ hổng bảo mật phổ biến thuộc nhóm chức năng bảo mật và xử lý ngoại lệ trong phần mềm.
- Nhận diện rủi ro từ việc cấp quyền thiếu xác thực, lưu trữ truyền tải dữ liệu nhạy cảm dưới dạng bản rõ (Plaintext).
- Hiểu rõ sự nguy hại của mật khẩu mã hóa cứng (Hardcoded Credentials) và lộ lọt thông tin cấu trúc nội bộ qua thông báo lỗi hệ thống.

## 핵심 키워드 (Từ khóa)
- **인증 누락 (Missing Authentication)**: Không yêu cầu tái xác thực khi thực hiện chức năng quan trọng.
- **평문 저장/전송 (Plaintext Storage/Transmission)**: Lưu trữ hoặc truyền mật khẩu, số thẻ ngân hàng không mã hóa.
- **하드코드된 패스워드 (Hardcoded Credentials)**: Ghi cứng mật khẩu hoặc API Key bí mật trong mã nguồn.
- **오류 메시지 노출 (Information Exposure Through Error Messages)**: Lộ dấu vết ngăn xếp (Stack Trace), tên bảng DB, đường dẫn tệp máy chủ qua thông báo lỗi.

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [31-bai-hoc.md](31-bai-hoc.md) (소프트웨어 개발 보안 관련 법규 - Yêu cầu mã hóa thông tin cá nhân).
- Liên kết với [32-bai-hoc.md](32-bai-hoc.md) (보안 취약점 및 보안 기능 - Lỗ hổng Buffer Overflow, CSRF).
- Liên kết với [04-programming-language/16-bai-hoc.md](../../04-programming-language/lessons/16-bai-hoc.md) (Lỗi rò rỉ tài nguyên và ngoại lệ).

## 읽는 방법 (Cách đọc)
- Phân biệt các tình huống câu hỏi đề thi:
  - Mã nguồn chứa chuỗi `String password = "admin123";` $\rightarrow$ Lỗ hổng **하드코드된 비밀번호 (Hardcoded Password)**.
  - Khi kết nối DB thất bại, màn hình hiện `Failed connecting to root@localhost:3306 on table tbl_users` $\rightarrow$ Lỗi **오류 메시지 통한 정보 노출**.
  - Người dùng truy cập trực tiếp URL `/admin/deleteUser` mà không bị kiểm tra quyền đăng nhập $\rightarrow$ Lỗi **적절한 인증 없는 중요기능 허용**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bốn lỗ hổng bảo mật chức năng và lỗi thường gặp
| Tên lỗ hổng (KR / EN) | Bản chất nguy cơ an ninh | Hậu quả thực tế | Giải pháp khắc phục chuẩn |
| :--- | :--- | :--- | :--- |
| **적절한 인증 없이 중요기능 허용 / (Missing Authentication)** | Các chức năng nhạy cảm (đổi mật khẩu, chuyển khoản, xóa dữ liệu) không kiểm tra quyền hoặc không bắt đăng nhập lại | Kẻ tấn công có thể truy cập trái phép bằng cách sửa đổi URL hoặc gửi request trực tiếp | Bắt buộc kiểm tra phiên làm việc (Session check) và quyền hạn (RBAC) trên máy chủ cho từng API; yêu cầu nhập lại mật khẩu cho thao tác rủi ro cao |
| **중요정보 평문 저장 및 전송 / (Plaintext Storage/Transmission)** | Mật khẩu, số căn cước, số thẻ tín dụng được lưu trong DB hoặc truyền qua mạng mà không được mã hóa | Bị nghe lén dữ liệu trên đường truyền (Sniffing) hoặc lộ thông tin khi bị sao chép DB | Dùng giao thức truyền thông bảo mật (HTTPS, TLS 1.3, SSH); mã hóa DB bằng AES-256; băm mật khẩu một chiều có Salt (bcrypt, Argon2) |
| **하드코드된 비밀번호 / (Hardcoded Password)** | Mật khẩu quản trị, API Key, chuỗi kết nối DB được viết cố định trực tiếp vào mã nguồn | Khi chia sẻ mã nguồn lên Git hoặc dịch ngược file nhị phân (`.class`, `.exe`), bí mật lập tức bị lộ | Tách thông tin nhạy cảm ra file cấu hình riêng ngoài mã nguồn, nạp qua biến môi trường (Environment Variables) hoặc dùng Secrets Manager |
| **오류 메시지 통한 정보 노출 / (Information Exposure via Errors)** | Hệ thống in nguyên văn lỗi ngoại lệ của cơ sở dữ liệu hoặc framework ra màn hình cho người dùng xem | Tiết lộ tên bảng, tên cột, đường dẫn tệp trên server, phiên bản phần mềm cho hacker khai thác | Sử dụng khối `try-catch` tùy chỉnh; hiển thị thông báo lỗi chung thân thiện; ghi nhật ký (logging) chi tiết vào tệp nội bộ bảo mật |

#### 2. Ví dụ trực quan về xử lý thông báo lỗi an toàn
- **Cách làm nguy hiểm (Khai báo lộ thông tin)**:
  ```
  [Lỗi hệ thống]: Không thể kết nối cơ sở dữ liệu MySQL tại 192.168.1.100:3306.
  Tài khoản 'root' sai mật khẩu tại tệp /var/www/vhosts/config/db_connect.php dòng 42.
  ```
  *(Hacker biết được IP nội bộ, cổng dịch vụ, tên tài khoản root và cấu trúc thư mục máy chủ).*
- **Cách làm an toàn (Chuẩn hóa thông báo)**:
  ```
  [Thông báo]: Đã xảy ra sự cố kỹ thuật tạm thời. Vui lòng thử lại sau. (Mã lỗi tham chiếu: ERR-2026-X9)
  ```
  *(Toàn bộ Stack trace kỹ thuật được lưu vào log nội bộ của quản trị viên kèm mã tham chiếu để tra cứu).*

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Quy trình quản trị khóa bí mật thay thế Hardcoded Credentials
```
       [Mã nguồn chương trình] ──(Gọi biến môi trường)──► System.getenv("DB_PASSWORD")
                                                                  ▲
                                                                  │ (Nạp giá trị lúc runtime)
 ┌────────────────────────────────────────────────────────────────┴────────────────────────┐
 │                     Dịch vụ Quản lý Khóa Bí mật (Secrets Management)                   │
 │  - AWS Secrets Manager / Azure Key Vault / HashiCorp Vault                             │
 │  - Tệp .env nằm ngoài kho lưu trữ Git (.gitignore) và được phân quyền phân quyền 600   │
 └────────────────────────────────────────────────────────────────────────────────────────┘
```

#### 2. Kỹ thuật lưu trữ mật khẩu an toàn theo tiêu chuẩn KISA / OWASP
- Không bao giờ dùng mã hóa hai chiều (Reversible Encryption) cho mật khẩu vì khóa mã hóa có thể bị lộ.
- Không dùng các hàm băm cũ có tốc độ tính toán quá nhanh hoặc đã bị phá vỡ va chạm: MD5, SHA-1.
- Bắt buộc dùng hàm băm chậm (Slow Hashing Function) kết hợp:
  - **Salt (Muối ngẫu nhiên)**: Chuỗi ngẫu nhiên được thêm vào mật khẩu trước khi băm, giúp vô hiệu hóa kỹ thuật tấn công bằng Bảng Cầu vồng (Rainbow Table).
  - **Key Stretching (Kéo dài khóa)**: Lặp lại quá trình băm hàng nghìn lần (ví dụ: bcrypt, PBKDF2) để làm tăng chi phí tính toán của kẻ tấn công vét cạn bằng GPU/ASIC.

---

### 복습 체크리스트
- [ ] Tại sao việc lưu mật khẩu dạng bản rõ (Plaintext) hoặc mã hóa bằng MD5/SHA-1 không còn được chấp nhận?
- [ ] Hardcoded Password trong mã nguồn dẫn đến nguy cơ bảo mật như thế nào và cách giải quyết triệt để là gì?
- [ ] Thông báo lỗi hệ thống cần được xử lý như thế nào để không làm rò rỉ cấu trúc nội bộ của máy chủ?
- [ ] Khái niệm "Salt" trong lưu trữ mật khẩu có tác dụng phòng chống kiểu tấn công nào?
