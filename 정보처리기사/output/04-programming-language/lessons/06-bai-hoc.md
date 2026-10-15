# 087. 환경변수와 쉘 스크립트 명령어 (Environment Variables & Shell Scripts)

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm biến môi trường (환경변수 - Environment Variables) và các lệnh quản lý biến môi trường trong hệ điều hành: `set`, `env`, và lệnh xuất biến toàn cục `export`.
- Nhận diện và đối chiếu bảng lệnh tương đương giữa hệ điều hành Windows (CMD) và hệ điều hành Unix/Linux (Shell).
- Ghi nhớ chức năng của các câu lệnh Unix/Linux kinh điển xuất hiện liên tục trong đề thi: `chmod`, `chown`, `cat`, `grep`, `ps`, `kill`, `tar`, và `crontab`.

## 핵심 키워드 (Từ khóa)
- 환경변수 (Environment Variables / set, env, export)
- 쉘 스크립트 (Shell Script)
- Windows vs Linux 명령어 (Command Comparison)
- chmod (권한 변경 / Change Mode)
- chown (소유자 변경 / Change Owner)
- grep (문자열 패턴 검색)
- ps & kill (프로세스 확인 및 강제 종료)
- tar (파일 묶기 및 압축)
- crontab (작업 스케줄링)

## 선행·연결 개념 (Kiến thức liên kết)
- [05-bai-hoc.md](05-bai-hoc.md): Kích thước các kiểu dữ liệu trong Java.
- [07-bai-hoc.md](07-bai-hoc.md): Chi tiết các quy tắc đặt tên biến trong lập trình.
- [정보처리기사/output/02-software-development/lessons/97-bai-hoc.md](../../02-software-development/lessons/97-bai-hoc.md): Môi trường phát triển tích hợp (IDE).

## 읽는 방법 (Cách đọc)
- Phân biệt các lệnh quản trị biến môi trường:
  - `set`: Hiển thị hoặc thiết lập các biến cục bộ (Local Shell Variables) trong phiên làm việc hiện thời.
  - `env`: Hiển thị danh sách các biến môi trường toàn cục (Environment Variables).
  - `export`: Chuyển một biến cục bộ thành biến môi trường toàn cục để các tiến trình con (Child Processes) sinh ra sau đó cũng kế thừa và đọc được giá trị (ví dụ: `export PATH=$PATH:/usr/local/bin`).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng đối chiếu các câu lệnh cơ bản: Windows vs Unix/Linux:**

| Thao tác trên tệp và thư mục | Lệnh trên Windows (CMD) | Lệnh tương đương trên Unix / Linux |
| :--- | :--- | :--- |
| **Xem danh sách tệp/thư mục** | `dir` | `ls` (List - ví dụ: `ls -al`) |
| **Sao chép tệp (Copy)** | `copy` | `cp` (Copy) |
| **Xóa tệp (Delete / Remove)** | `del` / `erase` | `rm` (Remove - ví dụ: `rm -rf`) |
| **Đổi tên hoặc di chuyển tệp** | `ren` / `move` | `mv` (Move / Rename) |
| **Tạo thư mục mới** | `md` / `mkdir` | `mkdir` (Make Directory) |
| **Xóa thư mục rỗng** | `rd` / `rmdir` | `rmdir` (Remove Directory) |
| **Xem nội dung tệp ra màn hình** | `type` | `cat` (Concatenate / View) |
| **Dọn sạch màn hình console** | `cls` | `clear` |

- **Bảng các lệnh Unix/Linux nâng cao chuẩn đề thi:**

| Câu lệnh | Chức năng chi tiết chuẩn thi | Ví dụ cú pháp tiêu biểu |
| :--- | :--- | :--- |
| **`chmod`** | Thay đổi quyền truy cập tệp/thư mục (Read, Write, Execute) | `chmod 755 run.sh` |
| **`chown`** | Thay đổi quyền sở hữu người dùng và nhóm của tệp | `chown user:group file.txt` |
| **`grep`** | Tìm kiếm chuỗi ký tự hoặc mẫu biểu thức chính quy (Regex) trong tệp | `grep "ERROR" server.log` |
| **`ps`** | Xem danh sách các tiến trình (Process) đang chạy trong hệ thống | `ps -ef \| grep java` |
| **`kill`** | Gửi tín hiệu buộc dừng hoặc tiêu diệt một tiến trình qua PID | `kill -9 1234` |
| **`tar`** | Gom nhiều tệp thành 1 tệp lưu trữ hoặc giải nén tệp | `tar -cvf backup.tar /data` |
| **`crontab`** | Lập lịch biểu tự động thực thi các tác vụ định kỳ theo thời gian | `crontab -e` |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Giải mã mã số quyền truy cập trong lệnh `chmod`:**
  - Ba nhóm đối tượng: Owner (Chủ sở hữu), Group (Nhóm), Others (Người khác).
  - Trọng số quyền cơ bản theo hệ nhị phân 3 bit: Read ($r=4$), Write ($w=2$), Execute ($x=1$).
  - Ví dụ `chmod 755`:
    - Owner: $4 + 2 + 1 = 7$ (Đầy đủ $rwx$).
    - Group: $4 + 0 + 1 = 5$ (Chỉ đọc và chạy $r-x$).
    - Others: $4 + 0 + 1 = 5$ (Chỉ đọc và chạy $r-x$).

### 복습 체크리스트
- [ ] Nhớ lệnh `export` dùng để chia sẻ biến môi trường cho các tiến trình con.
- [ ] Phân biệt được các cặp lệnh tương đương: dir/ls, copy/cp, del/rm, move/mv, type/cat.
- [ ] Nhớ lệnh `chmod` đổi quyền (755), `chown` đổi chủ sở hữu.
- [ ] Nhớ lệnh `grep` tìm kiếm chuỗi văn bản, `ps` xem tiến trình, `kill` dừng tiến trình.
