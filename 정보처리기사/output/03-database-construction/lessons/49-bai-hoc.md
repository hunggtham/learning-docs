# 2. UNIX의 주요 명령어 (Các lệnh UNIX chính)

## 학습 목표 (Mục tiêu)
- Nắm vững các lệnh và lời gọi hệ thống (System Calls) điều khiển tiến trình trong UNIX: **`fork` (tạo/nhân bản tiến trình con)**, **`exec` (thay thế và thực thi chương trình mới)**, **`&` (chạy ngầm trong nền)**, **`wait` (chờ tiến trình con hoàn tất)**, và **`kill` (hủy tiến trình)**.
- Thành thạo các lệnh quản trị hệ thống tệp và phân quyền: **`chmod` (thay đổi quyền truy cập rwx)**, **`chown` (đổi chủ sở hữu)**, **`mount` (gắn hệ thống tệp)**, và **`fsck` (kiểm tra và sửa lỗi đĩa)**.
- Phân biệt rõ sự khác nhau cơ bản giữa hai lời gọi hệ thống cốt lõi: `fork` (nhân đôi tiến trình) và `exec` (thay thế mã thực thi).

## 핵심 키워드 (Từ khóa)
- UNIX 명령어 (Lệnh UNIX / UNIX Commands)
- fork (Lời gọi tạo tiến trình con / 복제 생성)
- exec (Lời gọi thực thi chương trình mới / 덮어쓰기 실행)
- 백그라운드 (& / Background Execution)
- wait (Đợi tiến trình con kết thúc)
- chmod (Thay đổi quyền / Change Mode: rwx)
- chown (Đổi chủ sở hữu / Change Owner)
- mount / umount (Gắn kết nối hệ thống tệp)
- fsck (Kiểm tra sửa lỗi hệ thống tệp / File System Check)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([48-bai-hoc.md](48-bai-hoc.md)):** Lệnh `chmod` và `chown` tác động trực tiếp vào các trường UID, GID và 9 bit quyền hạn (rwxrwxrwx) được lưu trữ trong khối I-node.
- **Tiếp nối sang các bài sau ([50-bai-hoc.md](50-bai-hoc.md), [51-bai-hoc.md](51-bai-hoc.md)):** Sau khi hoàn tất các kiến thức nền tảng về hệ điều hành máy chủ, chúng ta sẽ quay trở lại phần ứng dụng SQL chuyên sâu với cú pháp nâng cao của DDL, DML, DCL và các phép JOIN phức hợp.

## 읽는 방법 (Cách đọc)
- Học thuộc bảng phân biệt lệnh tiến trình và lệnh tệp ở TẦNG A:
  - `fork`: Tạo tiến trình con y hệt cha.
  - `exec`: Nạp chương trình mới đè lên không gian bộ nhớ hiện tại.
  - `&`: Đặt cuối dòng lệnh để chạy ngầm (Background).
  - `chmod`: Đổi quyền số bát phân (777, 755).
  - `chown`: Đổi chủ sở hữu người dùng/nhóm.
  - `fsck`: Quét và sửa lỗi đĩa (tương đương chkdsk).

---

## 2. UNIX의 주요 명령어 (Các lệnh UNIX chính)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng các Lệnh điều khiển Tiến trình (프로세스 제어 명령어):**
  | Lệnh / Lời gọi | Ý nghĩa kỹ thuật chính xác | Tình huống xuất hiện trong đề thi |
  |---|---|---|
  | **`fork`** | **Tạo tiến trình con mới** bằng cách nhân bản toàn bộ không gian địa chỉ của tiến trình cha. Tiến trình con nhận PID mới. | Đề thi nhắc đến: *"새로운 프로세스를 생성 / 복제"* |
  | **`exec`** | **Nạp và thực thi một tệp nhị phân mới**, ghi đè toàn bộ không gian bộ nhớ, mã lệnh và dữ liệu của tiến trình hiện tại. | Đề thi nhắc đến: *"새로운 프로세스를 수행 / 다른 프로그램으로 대체"* |
  | **`&`** | Ký tự đặt ở cuối dòng lệnh để ra lệnh cho hệ thống **thực thi tiến trình ở chế độ nền (Background)**. | Đề thi nhắc đến: *"백그라운드 처리"* |
  | **`wait`** | Tiến trình cha **tạm dừng thực thi** cho đến khi một trong các tiến trình con của nó kết thúc hoàn toàn. | Đề thi nhắc đến: *"하위 프로세스가 종료될 때까지 대기"* |
  | **`exit`** | Chấm dứt hoạt động của tiến trình hiện tại và trả mã trạng thái về cho tiến trình cha. | Kết thúc tiến trình (`프로세스 수행 종료`). |
  | **`kill`** | Gửi tín hiệu (Signal) đến một tiến trình để yêu cầu kết thúc hoặc dừng hoạt động theo mã PID. | Hủy tiến trình cưỡng chế (`프로세스 강제 종료`). |
  | **`getpid` / `getppid`** | Lấy mã định danh tiến trình của bản thân (PID) / của tiến trình cha (Parent PID). | Tra cứu mã định danh (`프로세스 ID 획득`). |

- **2. Bảng các Lệnh quản trị Hệ thống tệp và Thư mục:**
  | Lệnh | Ý nghĩa kỹ thuật | Ví dụ minh họa trong thực tế |
  |---|---|---|
  | **`chmod`** | Thay đổi quyền truy cập của tệp/thư mục (Change Mode: r, w, x). | `chmod 755 run.sh` (Chủ sở hữu toàn quyền 7=rwx; Nhóm và Khách quyền 5=r-x). |
  | **`chown`** | Thay đổi chủ sở hữu của tệp/thư mục (Change Owner). | `chown oracle:dba dbfile.dbf` (Đổi chủ sở hữu thành user oracle, nhóm dba). |
  | **`mount`** | Gắn một hệ thống tệp vật lý (ổ đĩa, USB) vào một điểm gắn kết (Mount point) trên cây thư mục. | `mount /dev/sdb1 /mnt/usb`. |
  | **`fsck`** | Kiểm tra tính nhất quán và sửa chữa lỗi của hệ thống tệp (File System Check). | `fsck /dev/sda1` (Tương tự công cụ chkdsk trong Windows). |
  | **`mkfs`** | Định dạng (Format) và tạo mới một hệ thống tệp trên phân vùng ổ đĩa (Make File System). | `mkfs.ext4 /dev/sdb1`. |
  | **`cat`** | Ghép và in toàn bộ nội dung của tệp tin ra màn hình (Concatenate). | `cat access.log`. |
  | **`ls`** | Liệt kê danh sách các tệp và thư mục trong đường dẫn chỉ định. | `ls -la` (Hiển thị chi tiết cả tệp ẩn). |
  | **`finger`** | Tra cứu và hiển thị thông tin chi tiết về những người dùng đang đăng nhập vào hệ thống. | `finger admin`. |

- **주의/함정 (Bẫy đề thi trắc nghiệm):**
  - Đề hỏi: *"Lời gọi hệ thống nào tạo tiến trình con bằng cách nhân bản tiến trình cha?"* $\rightarrow$ Đáp án: **`fork`**.
  - Đề hỏi: *"Ký tự nào dùng để thực thi lệnh ở chế độ chạy ngầm (Background)?"* $\rightarrow$ Đáp án: **`&`**.
  - Đề hỏi: *"Lệnh nào dùng để thay đổi quyền truy cập của tệp tin trong UNIX?"* $\rightarrow$ Đáp án: **`chmod`**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tính toán quyền truy cập theo hệ bát phân trong `chmod`:**
  - Mỗi nhóm quyền (User, Group, Others) được tạo bởi 3 quyền:
    - **`r` (Read - Đọc):** Có giá trị là $4$ ($2^2$).
    - **`w` (Write - Ghi):** Có giá trị là $2$ ($2^1$).
    - **`x` (Execute - Thực thi):** Có giá trị là $1$ ($2^0$).
  - Ví dụ lệnh `chmod 754 file.txt`:
    - User = $4 + 2 + 1 = 7$ (Đọc + Ghi + Chạy $\rightarrow$ `rwx`).
    - Group = $4 + 0 + 1 = 5$ (Đọc + Chạy $\rightarrow$ `r-x`).
    - Others = $4 + 0 + 0 = 4$ (Chỉ Đọc $\rightarrow$ `r--`).

### 복습 체크리스트
- [ ] Phân biệt được sự khác nhau giữa fork (nhân đôi) và exec (thay thế).
- [ ] Nhớ tác dụng của ký tự & (chạy nền background).
- [ ] Tính thành thạo giá trị số bát phân của chmod (r=4, w=2, x=1).
- [ ] Nêu chức năng của các lệnh mount, fsck, chown, cat.
