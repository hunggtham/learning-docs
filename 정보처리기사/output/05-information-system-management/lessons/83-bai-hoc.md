# 108 서버 인증 & 109 접근 제어 (Server Authentication & Access Control Overview)

## 학습 목표 (Mục tiêu)
- Nắm vững kiến trúc khung bảo mật máy chủ theo mô hình AAA: Xác thực (Authentication), Cấp quyền (Authorization), và Kiểm toán kế toán (Accounting).
- Hiểu rõ cơ chế xác thực tập trung một lần (SSO - Single Sign-On) và giao thức xác thực dựa trên vé Kerberos (KDC, AS, TGS).
- Nắm vững 3 thành phần cốt lõi của hệ thống kiểm soát truy cập: Chủ thể (Subject), Đối tượng (Object), và Quyền hạn truy cập (Access Right).
- Phân biệt tổng quan 3 mô hình chính sách kiểm soát truy cập chuẩn: DAC (Tùy ý), MAC (Bắt buộc), và RBAC (Dựa trên vai trò).

## 핵심 키워드 (Từ khóa)
- **AAA 프레임워크**: Authentication (xác minh danh tính), Authorization (cấp phát quyền hạn), Accounting (ghi vết kiểm toán hoạt động).
- **SSO (Single Sign-On)**: Đăng nhập một lần duy nhất, sử dụng toàn bộ các hệ thống dịch vụ liên kết.
- **Kerberos**: Giao thức xác thực mạng bảo mật dựa trên vé (Ticket-based), gồm KDC, AS (Authentication Server), TGS (Ticket Granting Server).
- **접근 통제 3요소**: Subject (Chủ thể - Người dùng/Tiến trình), Object (Đối tượng - Tệp tin/DB), Access Right (Quyền - Đọc/Ghi/Chạy).

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [84-bai-hoc.md](84-bai-hoc.md) (Chi tiết 4 loại hình công nghệ xác thực người dùng).
- Liên kết với [85-bai-hoc.md](85-bai-hoc.md) (Chi tiết các chính sách kiểm soát truy cập DAC, MAC, RBAC).
- Liên kết với [30-bai-hoc.md](30-bai-hoc.md) (Hệ thống xác thực và an toàn thông tin).

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh quy trình AAA trong đề thi:
  - Hỏi "Kiểm tra ID và mật khẩu để chứng minh đúng là anh A" $\rightarrow$ **Authentication (인증)**.
  - Hỏi "Xác định anh A được phép đọc tệp nào và sửa tệp nào" $\rightarrow$ **Authorization (인가)**.
  - Hỏi "Ghi lại nhật ký anh A đã sửa tệp lúc mấy giờ" $\rightarrow$ **Accounting (감사/계정 관리)**.
  - "Giao thức xác thực sử dụng mô hình vé (Ticket) với máy chủ KDC" $\rightarrow$ **Kerberos**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Khung kiến trúc an ninh AAA (Authentication - Authorization - Accounting)
| Thành phần (KR / EN) | Câu hỏi cốt lõi giải quyết | Nhiệm vụ kỹ thuật chính | Ví dụ triển khai |
| :--- | :--- | :--- | :--- |
| **Authentication / (인증 - Xác thực)** | **"Bạn là ai?" / (Who are you?)** | Xác minh và chứng minh tính hợp pháp của danh tính mà người dùng khai báo | Kiểm tra ID / Mật khẩu, xác thực vân tay, OTP token |
| **Authorization / (인가 - Phân quyền)** | **"Bạn được làm gì?" / (What can you do?)** | Cấp phát các quyền hạn cụ thể (Read, Write, Execute) trên từng tài nguyên hệ thống | Phân quyền vai trò quản trị viên (Admin) vs nhân viên (User) |
| **Accounting / (계정 관리 / 감사)** | **"Bạn đã làm những gì?" / (What did you do?)** | Thu thập, ghi vết nhật ký thời gian đăng nhập, tài nguyên đã sử dụng phục vụ kiểm toán | Ghi tệp `/var/log/secure`, thống kê dung lượng mạng đã tải |

#### 2. Công nghệ Xác thực Máy chủ Tiêu biểu
- **SSO (Single Sign-On - Đăng nhập một lần)**:
  - Cho phép người dùng chỉ cần đăng nhập thành công một lần duy nhất tại cổng xác thực trung tâm là có thể truy cập hợp lệ vào tất cả các hệ thống ứng dụng độc lập khác trong mạng mà không cần phải nhập lại mật khẩu nhiều lần.
  - *Tiêu chuẩn triển khai*: SAML (Security Assertion Markup Language), OAuth 2.0, OpenID Connect.
- **Kerberos (Giao thức xác thực vé)**:
  - Giao thức xác thực mạng hoạt động dựa trên mật mã đối xứng, do viện MIT phát triển.
  - Sử dụng bên thứ ba tin cậy **KDC (Key Distribution Center)** gồm 2 dịch vụ:
    - **AS (Authentication Server)**: Xác thực danh tính ban đầu của người dùng và cấp vé **TGT (Ticket Granting Ticket)**.
    - **TGS (Ticket Granting Server)**: Kiểm tra vé TGT và cấp vé dịch vụ (**Service Ticket**) để người dùng gửi tới máy chủ ứng dụng cuối cùng.
  - *Đặc điểm*: Tuyệt đối không truyền mật khẩu trên mạng, ngăn chặn hoàn toàn tấn công nghe lén (Sniffing) và phát lại (Replay Attack).

#### 3. Ba Thành phần Cốt lõi của Kiểm soát Truy cập (Access Control)
1. **주체 (Subject - Chủ thể)**: Thực thể chủ động gửi yêu cầu truy cập vào tài nguyên (Người dùng, Chương trình ứng dụng, Tiến trình tiến trình).
2. **객체 (Object - Đối tượng)**: Tài nguyên thụ động được yêu cầu truy cập (Tệp tin, Thư mục, Bản ghi cơ sở dữ liệu, Cổng mạng, Thiết bị ngoại vi).
3. **접근 권한 (Access Right - Quyền hạn)**: Thao tác cụ thể mà chủ thể được phép thực hiện trên đối tượng (Đọc - Read, Ghi - Write, Thực thi - Execute, Xóa - Delete).

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ luồng xác thực của Giao thức Kerberos
```
[Máy khách (Client)] ──(1. Yêu cầu đăng nhập)──► [Authentication Server (AS)]
                     ◄──(2. Cấp vé TGT)─────────┘
        │
        ▼ (3. Gửi vé TGT xin vé dịch vụ)
[Ticket Granting Server (TGS)] ──(4. Cấp vé Service Ticket)──► [Client]
                                                                  │
                                                                  ▼ (5. Gửi vé Service Ticket)
                                                       [Server Ứng dụng]
```

---

### 복습 체크리스트
- [ ] Phân biệt sự khác nhau giữa hai khái niệm Authentication (인증) và Authorization (인가)?
- [ ] Thành phần Accounting trong mô hình an ninh AAA giải quyết bài toán quản trị nào?
- [ ] Công nghệ SSO (Single Sign-On) mang lại lợi ích gì cho trải nghiệm người dùng và quản trị hệ thống?
- [ ] Vai trò của hai thành phần AS và TGS trong trung tâm phân phối khóa KDC của Kerberos là gì?
