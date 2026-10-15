# UNIX/LINUX 환경 변수 및 기본 명령어 (Biến Môi trường & Lệnh Cơ bản UNIX/Linux)

## 학습 목표 (Mục tiêu)
- Nắm vững vai trò và cú pháp tham chiếu các biến môi trường hệ thống trong UNIX/Linux (`$HOME`, `$PWD`, `$PATH`, `$USER`, `$SHELL`).
- Làm chủ nhóm lệnh thao tác tệp và thư mục cơ bản (`ls`, `pwd`, `cd`, `cp`, `rm`, `mv`, `cat`, `find`).
- Hiểu rõ cơ chế phân quyền bảo mật tệp với lệnh `chmod` (hệ thống quyền rwx octal 4-2-1) và đổi chủ sở hữu `chown`.
- Nhận biết các lệnh và lời gọi hệ thống quản lý tiến trình và kiểm tra đĩa: `fork`, `ps`, `kill`, `fsck`.

## 핵심 키워드 (Từ khóa)
- **환경 변수 (Environment Variables)**: `$HOME` (thư mục cá nhân), `$PWD` (vị trí hiện tại), `$PATH` (đường dẫn tìm lệnh), `$USER`.
- **기본 명령어 (Basic Commands)**: `ls` (danh sách tệp), `cat` (xem nội dung), `cp` (sao chép), `rm` (xóa), `find` (tìm kiếm).
- **보안 및 권한 (Permissions)**: `chmod` (phân quyền Read=4, Write=2, Execute=1), `chown` (đổi chủ sở hữu).
- **시스템 관리 (System Administration)**: `fork` (nhân bản tiến trình), `fsck` (kiểm tra sửa chữa file system), `ps` / `kill`.

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [57-bai-hoc.md](57-bai-hoc.md) (Đặc trưng của UNIX và hệ thống tệp dạng cây).
- Liên kết với [58-bai-hoc.md](58-bai-hoc.md) (Cấu trúc Shell và thực thi lệnh Fork/Exec).
- Liên kết với [62-bai-hoc.md](62-bai-hoc.md) (Quản lý tiến trình và trạng thái PCB).

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh câu hỏi tính quyền trong `chmod`:
  - Quyền bao gồm 3 nhóm: Owner (Chủ) - Group (Nhóm) - Others (Khác).
  - Giá trị số: **Read ($r$) = 4**, **Write ($w$) = 2**, **Execute ($x$) = 1**.
  - Ví dụ `chmod 751 test.txt`:
    - Chủ sở hữu: $7 = 4 + 2 + 1$ (rwx - toàn quyền).
    - Nhóm: $5 = 4 + 0 + 1$ (r-x - đọc và thực thi).
    - Người khác: $1 = 0 + 0 + 1$ (--x - chỉ thực thi).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Các biến môi trường UNIX/Linux quan trọng
- **Cú pháp truy xuất**: Sử dụng tiền tố dấu đô la `$` trước tên biến (ví dụ: `echo $HOME`).
- **Bảng các biến môi trường phổ biến trong đề thi**:
  | Tên biến môi trường | Giá trị và Ý nghĩa kỹ thuật |
  | :--- | :--- |
  | **`$HOME`** | Đường dẫn tuyệt đối đến thư mục gốc của người dùng hiện tại (ví dụ: `/home/user`) |
  | **`$PWD`** | Thư mục làm việc hiện tại (Present Working Directory) |
  | **`$PATH`** | Danh sách các thư mục chứa các tệp thực thi phân tách nhau bằng dấu hai chấm `:`. Khi gõ lệnh, hệ điều hành sẽ tìm kiếm trong các thư mục này |
  | **`$USER`** | Tên tài khoản đăng nhập hiện tại của người dùng |
  | **`$SHELL`** | Đường dẫn tới tệp chương trình Shell mặc định đang sử dụng (ví dụ: `/bin/bash`) |

#### 2. Các lệnh hệ thống UNIX/Linux cốt lõi
| Lệnh (Command) | Chức năng kỹ thuật | Ví dụ cú pháp sử dụng |
| :--- | :--- | :--- |
| **`ls`** | Liệt kê danh sách các tệp tin và thư mục con | `ls -la` (xem chi tiết và hiện tệp ẩn bắt đầu bằng `.`) |
| **`cat`** | Nối và hiển thị toàn bộ nội dung của tệp tin ra màn hình | `cat filename.txt` |
| **`pwd`** | In đường dẫn thư mục làm việc hiện tại | `pwd` |
| **`cp`** | Sao chép tệp tin hoặc thư mục | `cp source.txt dest.txt` |
| **`rm`** | Xóa tệp tin hoặc thư mục | `rm -rf dir_name` (xóa đệ quy cưỡng chế) |
| **`mv`** | Di chuyển vị trí hoặc đổi tên tệp tin | `mv old_name.txt new_name.txt` |
| **`find`** | Tìm kiếm tệp tin trong cây thư mục theo tên, kích thước | `find / -name "*.c"` |
| **`chmod`** | Thay đổi chế độ bảo vệ và quyền truy cập của tệp tin | `chmod 755 run.sh` |
| **`chown`** | Thay đổi người sở hữu (Owner) và nhóm sở hữu của tệp | `chown user:group file.txt` |
| **`fork`** | Lời gọi hệ thống nhân bản tạo ra một tiến trình con mới | `pid = fork();` |
| **`fsck`** | Kiểm tra và sửa chữa tính nhất quán của hệ thống tệp | `fsck /dev/sda1` |
| **`ps`** | Xem danh sách các tiến trình hiện đang hoạt động | `ps -ef` hoặc `ps aux` |
| **`kill`** | Gửi tín hiệu để kết thúc hoặc cưỡng chế hủy một tiến trình | `kill -9 1234` (buộc dừng PID 1234) |

#### 3. Bảng tính quyền hạn số bát phân trong `chmod`
- Mỗi tệp có 3 cấp độ đối tượng: **User (u)**, **Group (g)**, **Others (o)**.
- Mỗi cấp độ có 3 quyền cơ bản:
  - **Read (r)**: Quyền đọc $= 4$ ($2^2$)
  - **Write (w)**: Quyền ghi/sửa $= 2$ ($2^1$)
  - **Execute (x)**: Quyền thực thi $= 1$ ($2^0$)
- *Bảng ánh xạ nhanh*:
  - $7 = 4 + 2 + 1 \rightarrow \text{rwx}$ (Toàn quyền đọc, ghi, chạy).
  - $6 = 4 + 2 + 0 \rightarrow \text{rw-}$ (Đọc và ghi, không chạy).
  - $5 = 4 + 0 + 1 \rightarrow \text{r-x}$ (Đọc và chạy, không sửa).
  - $4 = 4 + 0 + 0 \rightarrow \text{r--}$ (Chỉ đọc).
  - $0 = 0 + 0 + 0 \rightarrow \text{---}$ (Không có quyền gì).

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Bài toán phân quyền thực tế trong đề thi
- *Đề bài*: Để thiết lập cho tệp tin `script.sh` sao cho:
  - Chủ sở hữu có toàn quyền (Đọc, Ghi, Thực thi).
  - Các thành viên cùng nhóm có quyền Đọc và Thực thi.
  - Những người dùng khác chỉ có quyền Thực thi.
  Hãy viết lệnh `chmod` bằng số tương ứng?
- *Lời giải*:
  - Chủ sở hữu: $\text{rwx} = 4 + 2 + 1 = 7$.
  - Nhóm: $\text{r-x} = 4 + 0 + 1 = 5$.
  - Người khác: $\text{--x} = 0 + 0 + 1 = 1$.
  - Câu lệnh hoàn chỉnh là: `chmod 751 script.sh`.

#### 2. Lệnh `fsck` và an toàn hệ thống tệp
- Khi hệ thống máy chủ bị mất điện đột ngột hoặc tắt không đúng cách, bảng siêu dữ liệu Superblock hoặc bảng Inode của hệ thống tệp có thể bị sai lệch.
- Quản trị viên sử dụng công cụ `fsck` (File System Consistency Check) ở chế độ bảo trì để quét các khối đĩa mồ côi (Orphan blocks), khôi phục và đưa vào thư mục `/lost+found`.

---

### 복습 체크리스트
- [ ] Biến môi trường `$PATH` trong UNIX/Linux đảm nhận nhiệm vụ kỹ thuật gì?
- [ ] Lệnh `chmod 644 document.txt` sẽ cấp những quyền cụ thể nào cho Chủ sở hữu, Nhóm và Người khác?
- [ ] Sự khác biệt giữa lệnh `chmod` và `chown` là gì?
- [ ] Lời gọi hệ thống nào được sử dụng để nhân bản một tiến trình con từ tiến trình cha trong UNIX?
