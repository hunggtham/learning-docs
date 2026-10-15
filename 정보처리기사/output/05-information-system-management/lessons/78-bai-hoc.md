# 3. 사이트 간 요청 위조 (CSRF; Cross-Site Request Forgery / Giả mạo Yêu cầu Liên trang)

## 학습 목표 (Mục tiêu)
- Nắm vững bản chất và kịch bản tấn công của lỗ hổng giả mạo yêu cầu liên trang (CSRF - Cross-Site Request Forgery).
- Phân biệt rõ sự khác nhau giữa tấn công XSS (khai thác sự tin tưởng của người dùng) và CSRF (khai thác sự tin tưởng của máy chủ).
- Làm chủ 4 cơ chế phòng vệ CSRF chuẩn công nghiệp: Mã xác thực ngẫu nhiên (CSRF Token), Thuộc tính SameSite của Cookie, Xác thực lại (Re-authentication), và Kiểm tra Header Origin/Referer.

## 핵심 키워드 (Từ khóa)
- **CSRF (사이트 간 요청 위조)**: Lợi dụng phiên đăng nhập (Cookie/Session) hợp lệ của người dùng để thực thi các yêu cầu ngoài ý muốn.
- **XSS vs CSRF**: XSS (đánh cắp dữ liệu/cookie qua JavaScript độc hại) vs CSRF (mượn quyền người dùng gửi yêu cầu thay đổi trạng thái).
- **CSRF Token**: Khóa bảo mật ngẫu nhiên duy nhất cho mỗi phiên/biểu mẫu mà bên thứ ba không thể đọc được.
- **SameSite Cookie**: Thuộc tính ngăn trình duyệt tự động đính kèm cookie trong các yêu cầu bắt nguồn từ trang web khác (`Strict`, `Lax`).
- **재인증 (Re-authentication)**: Yêu cầu nhập lại mật khẩu hoặc OTP trước các giao dịch tài chính nhạy cảm.

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [32-bai-hoc.md](32-bai-hoc.md) (Lỗ hổng bảo mật và CSRF).
- Liên kết với [27-bai-hoc.md](27-bai-hoc.md) (Lỗ hổng ứng dụng web và XSS).
- Liên kết với [30-bai-hoc.md](30-bai-hoc.md) (Các cơ chế xác thực người dùng).

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh trong đề thi trắc nghiệm:
  - "Lợi dụng người dùng đang đăng nhập ngân hàng, lừa nhấn vào liên kết để tự động chuyển tiền mà nạn nhân không biết" $\rightarrow$ **CSRF (사이트 간 요청 위조)**.
  - "Giải pháp phòng chống hiệu quả nhất cho CSRF là gì?" $\rightarrow$ Sử dụng **CSRF Token** ngẫu nhiên và cấu hình Cookie thuộc tính **SameSite**.
  - Nhớ mẹo: Chỉ đổi phương thức từ GET sang POST là **KHÔNG ĐỦ** để chặn CSRF (vì hacker có thể dùng form ẩn tự động submit).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bản chất và Kịch bản tấn công CSRF
- **Bản chất**: Kẻ tấn công không trực tiếp đánh cắp tài khoản hay đọc được dữ liệu của nạn nhân, mà lợi dụng việc **trình duyệt web tự động đính kèm Cookie xác thực (Session Cookie)** mỗi khi gửi yêu cầu tới máy chủ dịch vụ.
- **Kịch bản điển hình**:
  1. Nạn nhân đăng nhập thành công vào trang web ngân hàng trực tuyến (`bank.com`), máy chủ cấp cho trình duyệt một Session Cookie hợp lệ.
  2. Nạn nhân không đăng xuất, mở tiếp một tab mới và vô tình truy cập vào trang web độc hại của hacker (`evil.com`).
  3. Trang web `evil.com` chứa một thẻ ẩn (ví dụ: `<img src="https://bank.com/transfer?to=hacker&amount=1000">` hoặc một biểu mẫu tự động submit ngầm bằng JavaScript).
  4. Trình duyệt của nạn nhân tự động gửi request chuyển tiền tới `bank.com` kèm theo Session Cookie hợp lệ đang có.
  5. Máy chủ `bank.com` thấy Cookie xác thực hợp lệ nên thực hiện chuyển tiền thành công, coi đó là thao tác chính chủ của nạn nhân!

#### 2. So sánh đối chiếu XSS và CSRF
| Tiêu chí | XSS (Cross-Site Scripting) | CSRF (Cross-Site Request Forgery) |
| :--- | :--- | :--- |
| **Bản chất tấn công** | Khai thác **sự tin tưởng của người dùng đối với một trang web** | Khai thác **sự tin tưởng của máy chủ đối với trình duyệt của người dùng** |
| **Vị trí thực thi mã** | Mã độc JavaScript chạy trực tiếp trên trình duyệt của nạn nhân | Trình duyệt gửi yêu cầu HTTP giả mạo tới máy chủ mục tiêu |
| **Mục đích của hacker** | **Đọc trộm thông tin**, cướp Cookie, đánh cắp Token, chuyển hướng trang web | **Thực hiện hành động thay đổi trạng thái** (chuyển tiền, đổi mật khẩu, xóa bài) |
| **Biện pháp phòng thủ cốt lõi** | Lọc dữ liệu đầu vào, mã hóa thực thể HTML Output Encoding (`<` thành `&lt;`) | Sử dụng **CSRF Token**, kiểm tra SameSite Cookie, xác thực lại mật khẩu |

#### 3. Bốn Giải pháp Phòng ngừa CSRF Chuẩn mực
1. **CSRF Token (Mã thông báo ngẫu nhiên)**:
   - Mỗi khi người dùng yêu cầu một biểu mẫu (Form), máy chủ sinh ra một chuỗi ngẫu nhiên bí mật (CSRF Token) gắn vào Form và lưu trong phiên làm việc.
   - Khi submit, máy chủ kiểm tra Token gửi lên: nếu thiếu hoặc không khớp thì từ chối xử lý.
   - Kẻ tấn công ở domain khác bị chặn bởi chính sách cùng nguồn gốc (Same-Origin Policy - SOP) nên không thể đọc trộm được Token này.
2. **Cấu hình Cookie với thuộc tính `SameSite`**:
   - `SameSite=Strict`: Trình duyệt tuyệt đối không gửi Cookie trong các yêu cầu bắt nguồn từ trang web bên ngoài.
   - `SameSite=Lax`: Cho phép gửi Cookie trong các thao tác điều hướng an toàn (như bấm link GET thông thường), chặn toàn bộ POST liên trang.
3. **Tái xác thực cho giao dịch quan trọng (Re-authentication)**:
   - Trước khi thực hiện chuyển tiền hoặc đổi mật khẩu, bắt buộc người dùng phải nhập lại mật khẩu hiện tại, mã OTP SMS hoặc xác nhận sinh trắc học.
4. **Kiểm tra Header `Origin` và `Referer`**:
   - Máy chủ kiểm tra header HTTP `Origin` hoặc `Referer` của request để đảm bảo yêu cầu xuất phát từ đúng tên miền của ứng dụng, từ chối mọi yêu cầu gửi từ các trang web lạ.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ cơ chế hoạt động của CSRF Token
```
[Nạn nhân đã đăng nhập Website] ──► Mở form chuyển tiền
                                          │
                                          ▼
                                   [Máy chủ Web]
                                          │ (Cấp Form kèm: csrf_token = "a8f3b9...")
                                          ▼
[Trình duyệt nạn nhân nhận Form có Token]
       │
       ├───────────────────────────────────────────────────────┐
       ▼ (Người dùng bấm nút Gửi trên Form chính chủ)          ▼ (Hacker lừa gửi request từ evil.com)
Gửi: /transfer                                           Gửi: /transfer
Body: to=alice&amount=500&csrf_token="a8f3b9..."         Body: to=hacker&amount=1000 (KHÔNG CÓ TOKEN!)
       │                                                       │
       ▼                                                       ▼
[Máy chủ kiểm tra: Token khớp ──► HỢP LỆ]              [Máy chủ kiểm tra: Thiếu Token ──► TỪ CHỐI!]
```

---

### 복습 체크리스트
- [ ] Lỗ hổng CSRF lợi dụng đặc tính tự động nào của trình duyệt web đối với Cookie?
- [ ] Phân biệt sự khác nhau giữa mục đích tấn công của XSS và CSRF?
- [ ] Tại sao việc sử dụng CSRF Token lại ngăn chặn được kẻ tấn công từ trang web thứ ba?
- [ ] Hai giá trị `Strict` và `Lax` của thuộc tính SameSite trong Cookie kiểm soát việc gửi Cookie như thế nào?
