# ⦁ 보안 취약점 및 보안 기능 (Lỗ hổng bảo mật & Chức năng bảo mật)

## 학습 목표 (Mục tiêu)
- Nắm vững cơ chế phát sinh và biện pháp kỹ thuật ngăn chặn lỗ hổng tràn bộ đệm bộ nhớ (Memory Buffer Overflow).
- Hiểu rõ phương thức tấn công tiêm lệnh hệ điều hành (OS Command Injection) và kỹ thuật lập trình an toàn thay thế.
- Phân biệt rõ sự khác nhau giữa tấn công XSS và CSRF (Cross-Site Request Forgery) cùng các cơ chế phòng vệ CSRF Token, SameSite Cookie.

## 핵심 키워드 (Từ khóa)
- **메모리 버퍼 오버플로 (Buffer Overflow)**: Stack Guard (Canary), ASLR, DEP/NX, hàm an toàn (`strncpy`).
- **운영체제 명령어 삽입 (OS Command Injection)**: Lợi dụng ký tự nối lệnh (`;`, `|`, `&&`) thực thi lệnh shell tùy ý trên máy chủ.
- **사이트 간 요청 위조 (CSRF - Cross-Site Request Forgery)**: Mượn phiên đăng nhập hợp lệ của nạn nhân để thực thi hành vi trái phép, CSRF Token, SameSite Cookie.

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [27-bai-hoc.md](27-bai-hoc.md) (해킹 및 보안 위협 - XSS, SQLi, DoS).
- Liên kết với [33-bai-hoc.md](33-bai-hoc.md) (보안 기능 및 에러 처리 - Lỗi xác thực và rò rỉ thông báo lỗi).
- Liên kết với [04-programming-language/70-bai-hoc.md](../../04-programming-language/lessons/70-bai-hoc.md) (Lỗ hổng bảo mật mã nguồn C/Java).

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh câu hỏi thi giữa XSS và CSRF:
  - Tấn công nhằm **đánh cắp Cookie/Session** của người dùng $\rightarrow$ **XSS**.
  - Lợi dụng người dùng **đã đăng nhập** để âm thầm thực hiện giao dịch/hành động mà nạn nhân không hay biết $\rightarrow$ **CSRF**.
  - Ghi nhớ mẹo CSRF: Kẻ tấn công không trực tiếp đọc được thông tin nạn nhân, mà mượn quyền hạn (credentials) của nạn nhân để gửi request giả mạo.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Chi tiết 3 lỗ hổng bảo mật trọng tâm
| Tên lỗ hổng (KR / EN) | Cơ chế phát sinh lỗ hổng | Ví dụ thực tế | Biện pháp phòng chống cốt lõi |
| :--- | :--- | :--- | :--- |
| **메모리 버퍼 오버플로 / (Memory Buffer Overflow)** | Chương trình ghi dữ liệu vượt quá kích thước bộ đệm được cấp phát trên Stack/Heap, làm đè lên địa chỉ quay về (Return Address) của hàm | Cấp mảng 10 bytes nhưng hàm `strcpy` chép vào 50 bytes từ người dùng | - Dùng hàm an toàn kiểm tra độ dài: `strncpy`, `snprintf` / - Bật cơ chế phần cứng: **Stack Guard (Canary)**, **ASLR**, **DEP/NX** |
| **운영체제 명령어 삽입 / (OS Command Injection)** | Dữ liệu đầu vào chưa được lọc được đưa trực tiếp vào hàm thực thi lệnh hệ thống (`system()`, `exec()`), cho phép kẻ tấn công chèn lệnh shell tùy ý | Người dùng nhập IP: `127.0.0.1; rm -rf /` khiến máy chủ thực thi cả lệnh ping lẫn lệnh xóa file | - Không truyền trực tiếp chuỗi vào shell hệ thống / - Dùng API chuyên dụng có sẵn của ngôn ngữ / - Lọc ký tự đặc biệt: `;`, `\|`, `&`, `` ` ``, `$`, `\n` |
| **사이트 간 요청 위조 / (CSRF - Cross-Site Request Forgery)** | Lợi dụng việc trình duyệt tự động đính kèm Cookie/Session khi gửi yêu cầu tới trang web mà người dùng đã đăng nhập trước đó | Nạn nhân đang đăng nhập tài khoản ngân hàng, nhấn vào link ảnh chứa URL: `/transfer?to=hacker&amount=1000` | - Sử dụng **CSRF Token** ngẫu nhiên duy nhất cho mỗi phiên/biểu mẫu / - Thiết lập Cookie thuộc tính `SameSite=Strict` hoặc `Lax` / - Yêu cầu xác thực lại (Re-authentication) cho các hành động trọng yếu |

#### 2. So sánh đối chiếu XSS và CSRF
- **XSS (Cross-Site Scripting)**:
  - Mục tiêu: Đưa mã kịch bản JavaScript độc hại vào trang web hợp lệ.
  - Hậu quả: Thực thi mã trên trình duyệt của nạn nhân, đánh cắp Cookie, chiếm phiên làm việc.
  - Kẻ tấn công **đọc được** thông tin nhạy cảm.
- **CSRF (Cross-Site Request Forgery)**:
  - Mục tiêu: Lừa trình duyệt của người dùng gửi một yêu cầu HTTP độc hại tới máy chủ dịch vụ mà nạn nhân đã được xác thực.
  - Hậu quả: Thực hiện hành vi ngoài ý muốn (đổi mật khẩu, chuyển khoản, mua hàng).
  - Kẻ tấn công **không nhất thiết phải đọc được** phản hồi hay Cookie, mà chỉ cần yêu cầu được máy chủ thực thi thành công.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Luồng tấn công và cơ chế ngăn chặn CSRF Token
```
[Nạn nhân đã đăng nhập Ngân hàng]
         │ (Cookie hợp lệ đã lưu trên trình duyệt)
         ▼
[Trang web độc hại của Hacker] ──► Ép trình duyệt tự động gửi ngầm POST tới Ngân hàng:
                                   URL: /api/change-password
                                   Body: new_pass=hacker123
                                   (Trình duyệt tự gắn kèm Cookie xác thực!)
                                             │
                                             ▼
                                    [Máy chủ Ngân hàng]
                                             │
      ┌──────────────────────────────────────┴──────────────────────────────────────┐
      ▼ (Nếu KHÔNG có CSRF Token)                   ▼ (Nếu CÓ kiểm tra CSRF Token)
Đổi mật khẩu thành công! ──► Thất thoát tài khoản  Từ chối do thiếu/sai Token ──► AN TOÀN
```

#### 2. Cơ chế Stack Guard (Canary) phòng chống Buffer Overflow
- Trước khi địa chỉ quay về (Return Address) được lưu trên Stack, trình biên dịch chèn một giá trị ngẫu nhiên nhỏ gọi là **Canary (Chim hoàng yến)** nằm giữa bộ đệm cục bộ và Return Address.
- Khi hàm thực thi xong và chuẩn bị nhảy về địa chỉ Return Address:
  - Hệ thống kiểm tra xem giá trị Canary có bị thay đổi không.
  - Nếu bị đè tràn dữ liệu, giá trị Canary sẽ bị thay đổi $\rightarrow$ Hệ điều hành lập tức hủy tiến trình ngay, ngăn không cho chuyển quyền điều khiển vào mã độc của hacker.

---

### 복습 체크리스트
- [ ] Lỗ hổng tràn bộ đệm (Buffer Overflow) có thể được phòng chống bằng những cơ chế phần cứng và phần mềm nào?
- [ ] Bản chất khác biệt cơ bản giữa tấn công XSS và CSRF là gì?
- [ ] Tại sao việc sử dụng CSRF Token lại ngăn chặn được kẻ tấn công thực hiện hành vi giả mạo yêu cầu?
- [ ] Trong tấn công OS Command Injection, những ký tự phân tách lệnh nào thường bị hacker lợi dụng?
