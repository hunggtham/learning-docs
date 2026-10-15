# 2. 운영체제 명령어 삽입 (OS Command Injection / Tiêm lệnh Hệ điều hành)

## 학습 목표 (Mục tiêu)
- Nắm vững bản chất cơ chế phát sinh lỗ hổng tiêm lệnh hệ điều hành (OS Command Injection).
- Nhận diện các ký tự phân tách lệnh shell đặc biệt thường bị kẻ tấn công lợi dụng (`;`, `|`, `&&`, `||`, `$()`).
- Phân tích các ví dụ tấn công thực tế và hậu quả nghiêm trọng đối với an toàn máy chủ.
- Làm chủ các biện pháp phòng vệ chuẩn trong lập trình an toàn: Sử dụng API tích hợp sẵn, truyền mảng đối số tách biệt (`shell=False`), và xác thực dữ liệu đầu vào bằng Whitelist.

## 핵심 키워드 (Từ khóa)
- **운영체제 명령어 삽입 (OS Command Injection)**: Lợi dụng đầu vào chưa kiểm tra để ép máy chủ thực thi lệnh shell trái phép.
- **명령어 구분자 (Command Separators)**: Các ký tự nối lệnh hệ thống (`;`, `|`, `&`, `&&`, `||`, `` ` ``).
- **시큐어 코딩 (Secure Coding)**: Không dùng hàm gọi shell trực tiếp (`system()`, `exec()`), ưu tiên API chuyên dụng.
- **파라미터 분리 (Argument Separation)**: Truyền danh sách đối số độc lập (`shell=False`), vô hiệu hóa việc thông dịch lệnh của shell.

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [32-bai-hoc.md](32-bai-hoc.md) (Lỗ hổng bảo mật và chức năng an toàn).
- Liên kết với [76-bai-hoc.md](76-bai-hoc.md) (Lỗ hổng tràn bộ đệm bộ nhớ).
- Liên kết với [80-bai-hoc.md](80-bai-hoc.md) (Sử dụng API an toàn trong lập trình).

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh câu hỏi trong đề thi:
  - "Người dùng nhập địa chỉ IP kèm theo `; rm -rf /` khiến tệp tin trên máy chủ bị xóa" $\rightarrow$ Đây là lỗ hổng **운영체제 명령어 삽입 (OS Command Injection)**.
  - "Biện pháp phòng ngừa triệt để nhất là gì?" $\rightarrow$ Không dùng các hàm gọi shell hệ điều hành trực tiếp; dùng danh sách tham số tách biệt và xác thực Whitelist.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Cơ chế phát sinh Lỗ hổng Tiêm lệnh Hệ điều hành
- **Bản chất**: Lỗ hổng xảy ra khi ứng dụng nhận chuỗi dữ liệu từ bên ngoài (form nhập liệu web, tham số URL) và ghép chuỗi trực tiếp vào một câu lệnh hệ thống để chuyển cho trình thông dịch shell (`/bin/sh`, `cmd.exe`) thực thi thông qua các hàm như `system()`, `popen()`, `exec()` trong C, hoặc `Runtime.getRuntime().exec()` trong Java.
- **Các ký tự phân tách lệnh shell bị lợi dụng**:
  | Ký tự phân tách | Hệ điều hành | Hành vi thực thi của Shell | Ví dụ chuỗi tiêm độc hại |
  | :--- | :--- | :--- | :--- |
  | **`;` (Semicolon)** | Linux / UNIX | Chạy lệnh thứ nhất, sau đó tiếp tục chạy lệnh thứ hai bất kể kết quả | `127.0.0.1; cat /etc/passwd` |
  | **`|` (Pipe)** | Linux / Windows | Chuyển đầu ra của lệnh thứ nhất làm đầu vào cho lệnh thứ hai | `127.0.0.1 | net user` |
  | **`&&` (AND logic)** | Linux / Windows | Lệnh thứ hai chỉ chạy nếu lệnh thứ nhất thực thi thành công | `127.0.0.1 && dir C:\` |
  | **`||` (OR logic)** | Linux / Windows | Lệnh thứ hai chỉ chạy nếu lệnh thứ nhất bị lỗi | `invalid_ip || whoami` |
  | **`&` (Background)** | Linux / UNIX | Đẩy lệnh thứ nhất chạy ngầm, chạy ngay lệnh thứ hai | `127.0.0.1 & id` |

#### 2. Kỹ thuật Phòng chống Chuẩn hóa (Remediation)
- **Nguyên tắc 1: Tránh gọi shell hệ thống bằng mọi giá**:
  - Nếu muốn xóa tệp: Dùng hàm `File.delete()` của Java thay vì gọi lệnh hệ thống `rm` hoặc `del`.
  - Nếu muốn kiểm tra trạng thái mạng: Dùng thư viện socket tích hợp thay vì gọi lệnh `ping`.
- **Nguyên tắc 2: Truyền đối số dạng mảng tách rời (Argument Vector)**:
  - Không truyền chuỗi đơn lẻ vào shell; sử dụng mảng tham số để hệ thống hiểu các ký tự phân tách chỉ là dữ liệu thuần túy:
  ```python
  # Nguy hiểm (Chạy qua shell, dễ bị tiêm lệnh):
  subprocess.run(f"ping -c 4 {user_input}", shell=True)

  # An toàn (Không qua shell, các ký tự đặc biệt được coi là dữ liệu thô):
  subprocess.run(["ping", "-c", "4", user_input], shell=False)
  ```
- **Nguyên tắc 3: Xác thực dữ liệu đầu vào bằng Danh sách trắng (Whitelist)**:
  - Chỉ cho phép các ký tự hợp lệ (ví dụ: chỉ cho phép chữ số và dấu chấm trong địa chỉ IP `^[0-9.]{7,15}$`), lập tức từ chối và ghi log cảnh báo nếu xuất hiện bất kỳ ký tự đặc biệt nào.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Luồng tấn công OS Command Injection thực tế
```
[Giao diện Web: Ô kiểm tra kết nối mạng (Ping)]
  Người dùng bình thường nhập:  "8.8.8.8"
  ──► Máy chủ thực thi lệnh:   `ping -c 1 8.8.8.8` (An toàn)

  Kẻ tấn công nhập chuỗi:      "8.8.8.8; cat /etc/shadow"
  ──► Máy chủ thực thi lệnh:   `ping -c 1 8.8.8.8 ; cat /etc/shadow`
                               └───── Lệnh 1 ─────┘  └────── Lệnh 2 ──────┘
                               (Ping xong chuyển sang in toàn bộ mật khẩu mã hóa!)
```

---

### 복습 체크리스트
- [ ] Lỗ hổng OS Command Injection phát sinh từ lỗi lập trình căn bản nào?
- [ ] Kể tên 4 ký tự phân tách lệnh thường bị hacker lợi dụng để nối lệnh shell?
- [ ] Tại sao việc thiết lập tham số `shell=False` trong Python lại ngăn chặn được việc tiêm lệnh hệ thống?
- [ ] Chiến lược xác thực dữ liệu Whitelist khác với Blacklist như thế nào trong phòng chống Command Injection?
