# 2. UNIX의 주요 명령어 (Các lệnh UNIX chính)

## 2. UNIX의 주요 명령어 (Các lệnh UNIX chính)
Phần “2. UNIX의 주요 명령어 (Các lệnh UNIX chính)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

| 명령어 (Command) | 의미 (Ý nghĩa) | Giải thích & Ví dụ (VN) |
|---|---|---|
| `fork` | 새로운 프로세스 생성 (Tạo tiến trình con/nhân bản tiến trình). | Giống như phân thân. Ví dụ: Tiến trình cha gọi `fork` tạo ra một tiến trình con y hệt để làm việc song song. |
| `exec` | 새로운 프로세스 수행 (Thực thi tiến trình mới). | Thay thế tiến trình hiện tại bằng tiến trình mới. Ví dụ: Dùng `exec` để mở chương trình máy tính (calculator). |
| `&` | 백그라운드 처리 (Chạy nền). | Đặt ở cuối lệnh. Ví dụ: `find / -name test.txt &` (Tìm kiếm ngầm, cho phép gõ tiếp lệnh khác). |
| `wait` | 하위 프로세스 종료 대기 (Đợi tiến trình con kết thúc). | Ví dụ: Tiến trình cha đứng đợi (wait) tiến trình con hoàn thành công việc mới tiếp tục. |
| `exit` | 프로세스 수행 종료 (Kết thúc tiến trình). | Ví dụ: Gõ `exit` để đóng terminal. |
| `cat` | 파일 내용 표시 (Hiển thị nội dung tệp, giống `TYPE` trong DOS). | Ví dụ: `cat file.txt` (In nội dung file.txt ra màn hình). |
| `chmod` | 파일 권한 지정 (Thay đổi quyền truy cập tệp). | Ví dụ: `chmod 777 file.sh` (Cấp toàn quyền đọc, ghi, chạy). |
| `chown` | 소유자 변경 (Thay đổi chủ sở hữu). | Ví dụ: `chown root file.txt` (Đổi chủ tệp thành root). |
| `mount` | 파일 시스템 마운팅 (Gắn hệ thống tệp). | Ví dụ: Cắm USB vào và dùng `mount` để hệ thống nhận diện nội dung USB. |
| `mkfs` | 파일 시스템 생성 (Tạo hệ thống tệp). | Format ổ đĩa. Ví dụ: `mkfs.ext4 /dev/sda1`. |
| `chdir` / `cd` | 디렉터리 위치 변경 (Thay đổi thư mục). | Ví dụ: `cd /home`. |
| `fsck` | 파일 시스템 검사 및 보수 (Kiểm tra và sửa lỗi hệ thống tệp). | Giống chkdsk trong Windows. Ví dụ: `fsck /dev/sda1`. |
| `rmdir` | 디렉터리 삭제 (Xóa thư mục rỗng). | Ví dụ: `rmdir empty_folder`. |
| `ls` | 파일 목록 확인 (Xem danh sách tệp). | Ví dụ: `ls -l` (Xem danh sách chi tiết). |
| `getpid` / `getppid` | 자신의 / 부모 프로세스 ID 획득 (Lấy PID / Parent PID). | ID tiến trình để quản lý (vd: dùng kill để tắt). |
| `cp` / `mv` / `rm`| 복사 (Copy) / 이동 및 이름 변경 (Move/Rename) / 삭제 (Remove). | `cp a.txt b.txt`, `mv old.txt new.txt`, `rm a.txt`. |
| `finger` | 사용자 정보 표시 (Hiển thị thông tin người dùng). | Xem ai đang đăng nhập vào hệ thống. |

---

# CHAPTER 01 SQL 응용 (Ứng dụng SQL)
