# 리눅스의 커널 로그 (Các Tệp Nhật ký Hệ thống Linux)

## 학습 목표 (Mục tiêu)
- Nắm vững vai trò của các tệp nhật ký (Log files) trong hệ thống Linux/UNIX phục vụ điều tra số (Digital Forensics) và kiểm toán bảo mật.
- Phân biệt chính xác chức năng và lệnh tra cứu của 4 tệp log đăng nhập kinh điển: `/var/log/wtmp`, `/var/run/utmp`, `/var/log/btmp`, và `/var/log/lastlog`.
- Hiểu rõ các tệp log an ninh và quản trị khác: `/var/log/secure` (auth.log), `/var/log/messages`, `/var/log/xferlog`, `/var/log/pacct`.

## 핵심 키워드 (Từ khóa)
- **`/var/log/wtmp`**: Lưu lịch sử đăng nhập/đăng xuất thành công và thời gian boot/shutdown (tra cứu bằng lệnh `last`).
- **`/var/run/utmp`**: Lưu thông tin người dùng đang trực tuyến hiện tại (tra cứu bằng `who`, `w`).
- **`/var/log/btmp`**: Lưu các lần đăng nhập thất bại do sai mật khẩu (tra cứu bằng lệnh `lastb`).
- **`/var/log/lastlog`**: Lưu lần đăng nhập thành công gần nhất của từng tài khoản (lệnh `lastlog`).
- **`/var/log/secure` (auth.log)**: Log xác thực truy cập SSH, `sudo`, `su`.
- **`pacct` / `acct`**: Ghi lại các lệnh người dùng đã thực thi (tra cứu bằng lệnh `lastcomm`).

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [64-bai-hoc.md](64-bai-hoc.md) (Lệnh UNIX và quản trị hệ thống).
- Liên kết với [72-bai-hoc.md](72-bai-hoc.md) (Hệ thống phát hiện xâm nhập IDS dựa trên tệp log).
- Liên kết với [27-bai-hoc.md](27-bai-hoc.md) (Các cuộc tấn công mạng và rà soát vết vết đột nhập).

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh 4 tệp log đăng nhập hay hỏi nhất:
  - Xem ai **đang đăng nhập ngay bây giờ** $\rightarrow$ **`utmp`** (lệnh `who`).
  - Xem lịch sử **tất cả các lần đăng nhập thành công** trong quá khứ $\rightarrow$ **`wtmp`** (lệnh `last`).
  - Xem các lần **đăng nhập thất bại** (dấu hiệu bị tấn công Brute-force mật khẩu) $\rightarrow$ **`btmp`** (lệnh `lastb`).
  - Xem **lần cuối cùng mỗi tài khoản đăng nhập** là khi nào $\rightarrow$ **`lastlog`** (lệnh `lastlog`).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng 4 Tệp Log Đăng nhập Cốt lõi của Linux
| Tên tệp Log | Định dạng tệp | Nội dung sự kiện ghi nhận | Lệnh chuyên dụng để đọc |
| :--- | :--- | :--- | :--- |
| **`/var/run/utmp`** | Tệp nhị phân (Binary) | Lưu thông tin về các tài khoản người dùng **hiện đang đăng nhập trực tuyến** tại thời điểm kiểm tra | `who`, `w`, `users`, `finger` |
| **`/var/log/wtmp`** | Tệp nhị phân (Binary) | Lưu toàn bộ lịch sử các lần **đăng nhập / đăng xuất thành công** từ trước tới nay, kèm thời gian hệ thống khởi động (Reboot) hoặc tắt máy (Shutdown) | `last` |
| **`/var/log/btmp`** | Tệp nhị phân (Binary) | Lưu vết toàn bộ các lần **đăng nhập thất bại** (sai mật khẩu, sai tên tài khoản), phục vụ điều tra tấn công vét cạn mật khẩu | `lastb` |
| **`/var/log/lastlog`** | Tệp nhị phân (Binary) | Lưu lại thời điểm và địa chỉ IP nguồn của **lần đăng nhập thành công gần nhất** đối với từng tài khoản người dùng trong file `/etc/passwd` | `lastlog` |

*Lưu ý kỹ thuật*: 4 tệp log trên đều được lưu dưới dạng cấu trúc nhị phân (Binary Data) để tối ưu tốc độ ghi và ngăn chặn chỉnh sửa thủ công bằng trình soạn thảo; do đó không thể xem bằng lệnh `cat` hay `vi` mà bắt buộc phải dùng các lệnh tiện ích tương ứng (`last`, `lastb`, `who`, `lastlog`).

#### 2. Các Tệp Log Quản trị và An ninh Tiêu biểu khác
- **`/var/log/secure`** (hoặc `/var/log/auth.log` trên Ubuntu/Debian):
  - Tệp văn bản thuần (Text file) ghi lại toàn bộ các sự kiện xác thực danh tính người dùng trong hệ thống.
  - Bao gồm: Các phiên đăng nhập từ xa qua dịch vụ SSH, việc sử dụng lệnh leo thang quyền hạn `su` và `sudo`, các yêu cầu dịch vụ PAM.
- **`/var/log/messages`** (hoặc `/var/log/syslog`):
  - Tệp nhật ký chung của toàn hệ thống, lưu trữ các thông báo vận hành của nhân hệ điều hành Kernel, các daemon dịch vụ hệ thống và thông báo lỗi phần cứng ngoại vi.
- **`/var/log/pacct` (hoặc `/var/account/acct`)**:
  - Ghi lại nhật ký lịch sử kiểm toán của **tất cả các câu lệnh mà người dùng đã gõ và thực thi** trên hệ thống, kèm theo PID và thời gian chạy. Tra cứu nội dung bằng lệnh `lastcomm`.
- **`/var/log/xferlog`**:
  - Lưu trữ chi tiết lịch sử truyền tải tệp tin (gồm thông tin tải lên Upload và tải xuống Download) của dịch vụ máy chủ FTP.
- **`/var/log/boot.log`**:
  - Ghi lại các thông báo trạng thái khởi động của các dịch vụ hệ thống trong quá trình bật máy chủ.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Kỹ thuật điều tra tấn công Brute-force qua tệp `/var/log/btmp`
```bash
# Xem 10 lần đăng nhập thất bại gần nhất:
lastb -n 10

# Kết quả hiển thị mẫu:
# root     ssh:notty    192.168.1.50   Thu Oct 15 14:30 - 14:30  (00:00)
# admin    ssh:notty    192.168.1.50   Thu Oct 15 14:30 - 14:30  (00:00)
# guest    ssh:notty    192.168.1.50   Thu Oct 15 14:31 - 14:31  (00:00)
# ---
# Nhận định an ninh: Địa chỉ IP 192.168.1.50 đang thực hiện tấn công dò quét từ điển (Dictionary Attack)!
```

#### 2. Dịch vụ quản lý nhật ký hệ thống rsyslog và logrotate
- **rsyslog**: Daemon thường trực tiếp nhận các thông điệp ghi log từ nhân kernel và ứng dụng, phân loại theo mức độ nghiêm trọng (Emergency, Alert, Critical, Error, Warning, Notice, Info, Debug) và ghi vào các tệp tương ứng trong `/var/log`.
- **logrotate**: Công cụ định kỳ nén, lưu trữ và luân chuyển các tệp log (xoay vòng log hàng tuần hoặc theo kích thước) để ngăn ngừa tình trạng tệp log phình to làm tràn đầy dung lượng ổ cứng.

---

### 복습 체크리스트
- [ ] Tệp `/var/log/wtmp` và `/var/run/utmp` ghi lại những sự kiện khác nhau như thế nào?
- [ ] Để phát hiện dấu hiệu kẻ tấn công đang cố gắng dò mật khẩu tài khoản root, quản trị viên cần kiểm tra tệp log nào bằng lệnh gì?
- [ ] Lệnh `lastcomm` dùng để đọc thông tin lịch sử từ tệp nhật ký nào?
- [ ] Tại sao không thể sử dụng trực tiếp các lệnh như `cat` hay `grep` thông thường để đọc nội dung của tệp `/var/log/wtmp`?
