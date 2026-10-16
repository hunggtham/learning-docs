# 운영체제 기초, UNIX/Linux 구조 및 쉘 스크립트 (Tổng quan HĐH, UNIX/Linux & Shell Script)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và 4 mục tiêu đánh giá cốt lõi của Hệ điều hành (운영체제 4대 평가 목적): Tăng Năng suất (Throughput), Giảm Thời gian quay vòng (Turnaround Time), Tăng Độ tin cậy (Reliability), và Tăng Khả năng sẵn sàng (Availability).
- Phân biệt cấu trúc 3 tầng của hệ điều hành UNIX/Linux: Hạt nhân Kernel (thường trú RAM), Lớp vỏ Shell (trình thông dịch lệnh) và Tiện ích Utility; hiểu rõ cấu trúc khối dữ liệu i-node trong hệ thống tệp.
- Thấu hiểu cơ chế tạo và nạp tiến trình qua hai lời gọi hệ thống kinh điển: `fork()` (giá trị trả về cho cha > 0, con = 0) và `exec()` (thay thế không gian nhớ).
- Sử dụng thành thạo và tính toán chính xác quyền truy cập tệp nhị phân/bát phân với lệnh `chmod` (ví dụ `755`, `644`), đường ống Pipe (`|`) và các lệnh shell cơ bản (`ls, cd, pwd, cat, grep, ps, kill`).

## 핵심 키워드 (Từ khóa)
- 운영체제 4대 목적 (OS 4 Evaluation Goals) — 처리능력 향상, 반환시간 단축, 신뢰도 향상, 사용가능도 향상.
- 커널 vs 쉘 vs 유틸리티 (Kernel vs Shell vs Utility) — Hạt nhân thường trú RAM vs Trình thông dịch lệnh vs Tiện ích ứng dụng.
- fork() vs exec() — Nhân bản tiến trình (Cha > 0, Con = 0) vs Nạp chương trình mới ghi đè bộ nhớ.
- i-node 구조 (i-node Structure) — Khối lưu trữ thông tin thuộc tính tệp (quyền, kích thước, con trỏ đĩa, cấm lưu tên tệp).
- 파일 권한 설정 (File Permissions `chmod`) — Quyền Đọc ($r=4$), Ghi ($w=2$), Thực thi ($x=1$) theo 3 nhóm User/Group/Others.
- 파이프 및 리다이렉션 (Pipe `|` & Redirection `>`, `>>`) — Chuyển luồng đầu ra tiến trình này làm đầu vào tiến trình kia.
- 쉘 기본 명령어 (Basic Shell Commands) — `ls`, `cd`, `pwd`, `cat`, `grep`, `ps`, `kill`.

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Kế thừa từ `10-phan-loai-ngon-ngu-lap-trinh-bien-dich-vs-thong-dich.md`, khi mã nguồn được biên dịch ra tệp nhị phân, hệ điều hành là môi trường chịu trách nhiệm nạp, cấp phát tài nguyên và điều phối cho chương trình chạy.
- **Đang giải quyết gì (Current Problem):** Giải quyết câu hỏi về nền tảng hệ thống: Làm sao người dùng ra lệnh cho phần cứng hoạt động, quyền truy cập dữ liệu được bảo vệ thế nào trên máy chủ, cơ chế nào sinh ra và nạp tiến trình mới (`fork`, `exec`).
- **Dùng đi đâu (Forward Handoff):** Khi Kernel tạo tiến trình qua `fork()`, tiến trình sẽ bước vào chu trình điều phối CPU (Ready, Running, Blocked) được phân tích chi tiết ở bài `12-tien-trinh-luong-va-dieu-phoi-cpu.md`.

## 읽는 방법 (Cách đọc)
- **4 mục tiêu đánh giá HĐH:** Nhớ chỉ duy nhất một mục tiêu là **GIẢM (단축 / Minimize)**: **Thời gian quay vòng (반환 시간 - Turnaround Time)**. Cả 3 tiêu chí còn lại (Năng suất 처리능력, Độ tin cậy 신뢰도, Khả năng sẵn sàng 사용가능도) đều phải **TĂNG (향상 / Maximize)**.
- **`fork()` trả về:**
  - Trả về **`0`** cho tiến trình con.
  - Trả về **PID của con (> 0)** cho tiến trình cha.
  - Trả về **`-1`** nếu tạo tiến trình thất bại.
- **`exec()`:** Không sinh tiến trình mới, chỉ nạp chương trình mới đè lên không gian bộ nhớ của tiến trình hiện tại.
- **Quyền `chmod`:** $r = 4, w = 2, x = 1$. Lấy tổng ba số cho từng vị trí `User / Group / Others` (ví dụ `rwx = 4+2+1 = 7`, `r-x = 4+1 = 5`).
- **Đường ống `|`:** Nối output lệnh trước làm input lệnh sau, ví dụ: `ps -ef | grep java`.

---

## 운영체제 기초, UNIX/Linux 구조 및 쉘 스크립트

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [한국어]: `운영체제 4대 목적 중 반환시간만 단축이고 처리능력, 신뢰도, 사용가능도는 향상이다. UNIX는 커널(RAM 상주, HW 제어), 쉘(명령어 해석기), 유틸리티로 구성된다. fork()는 자식 프로세스를 생성하며 반환값은 자식 0, 부모 양수(자식 PID), 실패 -1이다. exec()는 기존 프로세스 공간에 새 프로그램을 덮어쓴다. chmod는 r=4, w=2, x=1 8진수 합산이다.`
  - [Tiếng Việt]: Trong 4 mục tiêu của hệ điều hành, chỉ có thời gian quay vòng là giảm, còn năng suất, độ tin cậy và khả năng sẵn sàng là tăng. UNIX gồm Kernel (thường trú RAM, điều khiển phần cứng), Shell (trình thông dịch lệnh) và Utility. Lời gọi fork() sinh tiến trình con với giá trị trả về: con = 0, cha > 0 (PID con), thất bại = -1. Lời gọi exec() ghi đè chương trình mới lên không gian tiến trình hiện tại. Phân quyền chmod cộng tổng bát phân: r=4, w=2, x=1.

- **1. Bảng 4 mục tiêu đánh giá chất lượng Hệ điều hành (운영체제 4대 평가 목적):**

| Mục tiêu đánh giá | Thuật ngữ Hàn / Anh | Định nghĩa kỹ thuật chuẩn khảo thí | Yêu cầu tối ưu |
| :--- | :--- | :--- | :---: |
| **1. Năng suất xử lý** | **처리 능력** (Throughput) | Lượng công việc mà hệ thống hoàn thành trong một đơn vị thời gian. | **TĂNG (향상)** |
| **2. Thời gian quay vòng**| **반환 시간** (Turnaround Time)| Thời gian từ lúc nộp công việc vào hệ thống đến khi nhận được kết quả cuối cùng. | **GIẢM (단축)** |
| **3. Độ tin cậy** | **신뢰도** (Reliability) | Mức độ hoàn thành công việc một cách chính xác, không phát sinh sai sót. | **TĂNG (향상)** |
| **4. Khả năng sử dụng** | **사용 가능도** (Availability)| Tỷ lệ phần trăm thời gian hệ thống ở trạng thái sẵn sàng phục vụ khi có yêu cầu. | **TĂNG (향상)** |

- **2. Bảng phân loại 3 thành phần cốt lõi của UNIX/Linux:**

| Thành phần | Vị trí trong kiến trúc | Bản chất và chức năng chính | Khả năng thay đổi |
| :--- | :--- | :--- | :--- |
| **커널 (Kernel)** | **Lõi trong cùng (Hạt nhân)** | **Luôn thường trú trong RAM**; quản lý CPU, bộ nhớ, tiến trình, đĩa cứng; cung cấp các hàm gọi hệ thống (**System Call**). | Cố định theo bản build hệ điều hành. |
| **쉘 (Shell)** | **Tầng trung gian (Lớp vỏ)** | **Trình thông dịch lệnh (명령어 해석기)**; nhận lệnh từ người dùng, dịch sang ngôn ngữ máy chuyển cho Kernel thực thi. | **Người dùng có thể tự do thay đổi** (bash, zsh, csh). |
| **유틸리티 (Utility)**| **Tầng ngoài cùng (Tiện ích)**| Các chương trình ứng dụng và trình biên dịch: `cat`, `ls`, `grep`, `vi`, `gcc`.| Cài đặt và gỡ bỏ linh hoạt. |

- **3. Bảng đối chiếu hai hàm tạo và nạp tiến trình: `fork()` vs `exec()`:**

| Tiêu chuẩn so sánh | Lời gọi hệ thống `fork()` | Lời gọi hệ thống `exec()` |
| :--- | :--- | :--- |
| **Bản chất hành động** | **Tạo ra một tiến trình con mới** là bản sao độc lập của tiến trình cha. | **Tải chương trình mới đè lên** không gian nhớ của tiến trình hiện tại. |
| **Số lượng tiến trình**| Tăng thêm 1 tiến trình mới trong bảng tiến trình hệ thống. | Giữ nguyên 1 tiến trình, không sinh thêm tiến trình mới. |
| **Mã định danh (PID)** | Tiến trình con được cấp một **PID hoàn toàn mới**. | Tiến trình **giữ nguyên PID cũ**, chỉ thay đổi nội dung code và dữ liệu. |
| **Giá trị trả về** | Tiến trình con nhận **`0`**; Tiến trình cha nhận **`PID con` (> 0)**; Thất bại nhận **`-1`**. | **Không trả về** nếu thành công (vì code cũ bị xóa sổ); trả về `-1` nếu thất bại. |

- **4. Bảng tính toán quyền hạn tệp UNIX/Linux (`chmod` - File Permissions):**

| Quyền hạn | Ký hiệu chữ | Giá trị bát phân | Ý nghĩa thao tác đối với tệp |
| :---: | :---: | :---: | :--- |
| **Đọc (Read)** | `r` | **`4`** | Đọc nội dung tệp; xem danh sách tệp trong thư mục. |
| **Ghi (Write)** | `w` | **`2`** | Sửa đổi, ghi đè, xóa nội dung tệp. |
| **Thực thi (Execute)** | `x` | **`1`** | Chạy tệp kịch bản (Script), chương trình thực thi nhị phân. |
| **Không có quyền** | `-` | **`0`** | Không có bất kỳ thao tác nào được cấp phép. |

- **Bảng mẫu các tổ hợp `chmod` thường gặp trong đề thi:**
  - `chmod 755 script.sh` -> User: $4+2+1 = \mathbf{7}$ (`rwx`), Group: $4+1 = \mathbf{5}$ (`r-x`), Others: $4+1 = \mathbf{5}$ (`r-x`).
  - `chmod 644 document.txt` -> User: $4+2 = \mathbf{6}$ (`rw-`), Group: $4$ (`r--`), Others: $4$ (`r--`).
  - `chmod 777 data.log` -> Cấp toàn quyền cho mọi người dùng (`rwxrwxrwx`).

- **주의/함정 (Bẫy đề thi):**
  - **Khối i-node không chứa tên tệp:** Đề thi khẳng định *"Khối i-node trong UNIX lưu trữ tên tệp (File Name)"* -> Đây là khẳng định **SAI**. i-node chỉ lưu metadata (quyền, kích thước, thời gian tạo, con trỏ khối đĩa); **tên tệp được lưu trong tệp thư mục cha (Directory File)**.
  - **Nhầm lẫn giá trị trả về của `fork()`:** Đề thi hỏi *"Giá trị trả về của `fork()` trong tiến trình con là gì?"* -> Đáp án đúng là **`0`**, chứ không phải PID của nó!
  - **Sau khi gọi `exec()`:** Mọi dòng lệnh phía sau lệnh gọi `exec()` trong file nguồn sẽ **không bao giờ được thực thi** nếu nạp thành công, vì mã nguồn đã bị thay thế hoàn toàn bởi chương trình mới.

- **한 문장 설명 (Câu chốt tự nhớ):**
  - *"4 mục tiêu chỉ giảm 반환시간; Kernel thường trú RAM, Shell nhận lệnh thông dịch; fork con nhận 0 cha nhận PID, exec ghi đè không đổi số danh; chmod cộng 4-2-1."*

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Lần vết chương trình C sử dụng `fork()` và phân luồng cha/con:
```c
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main() {
    pid_t pid = fork();

    if (pid < 0) {
        // Truong hop 1: fork that bai
        printf("Tao tien trinh that bai!\n");
        return 1;
    } else if (pid == 0) {
        // Truong hop 2: Tien trinh con thuc thi
        printf("[Con] Day la tien trinh con, PID tra ve = %d, PID thuc te = %d\n", pid, getpid());
    } else {
        // Truong hop 3: Tien trinh cha thuc thi (pid > 0 la PID cua con)
        printf("[Cha] Day la tien trinh cha, PID tra ve = %d, PID thuc te = %d\n", pid, getpid());
    }

    return 0;
}
```

*Cơ chế rẽ nhánh sau `fork()`:*
- Tại thời điểm `fork()` chạy xong, cả tiến trình cha và tiến trình con cùng tiếp tục chạy từ dòng lệnh tiếp theo.
- Nhờ giá trị `pid` khác nhau (`0` cho con, `> 0` cho cha), khối lệnh `if-else` tự động phân tách đường đi của cha và con.

#### 2. Bài toán trắc nghiệm tính toán phân quyền `chmod` chuẩn đề thi:
- **Đề bài:** Một tệp kịch bản `run.sh` hiện tại có chuỗi quyền là `-rwxr-xr--`. Người quản trị muốn thay đổi quyền sao cho:
  - Chủ sở hữu (User): Đọc và Ghi (không cho thực thi).
  - Nhóm (Group): Chỉ Đọc.
  - Người khác (Others): Không có bất kỳ quyền gì.
  Hỏi lệnh `chmod` với đối số bát phân nào dưới đây là đúng?
- **Phân tích từng nhóm:**
  - Chủ sở hữu: Đọc ($r = 4$) + Ghi ($w = 2$) = **`6`** (`rw-`).
  - Nhóm: Đọc ($r = 4$) = **`4`** (`r--`).
  - Người khác: Không quyền = **`0`** (`---`).
- **Đáp án:** Lệnh cần chạy là: `chmod 640 run.sh`.

#### 3. Bảng đối chiếu các lệnh CLI UNIX/Linux và cơ chế Pipe `|`:

| Lệnh Linux / UNIX | Bản chất chức năng | Ví dụ thao tác thực tế |
| :--- | :--- | :--- |
| **`ls -l`** | Liệt kê chi tiết danh sách tệp, thư mục và quyền hạn | `ls -la /var/log` |
| **`cd`** | Chuyển đổi thư mục làm việc (Change Directory) | `cd /usr/local/bin` |
| **`pwd`** | Hiển thị đường dẫn thư mục làm việc hiện tại | `pwd` -> `/home/user` |
| **`cat`** | Đọc và nối nội dung tệp ra màn hình console | `cat app.log` |
| **`grep`** | Lọc và tìm kiếm các dòng chứa từ khóa/mẫu regex | `grep "ERROR" server.log` |
| **`ps -ef`** | Liệt kê danh sách toàn bộ các tiến trình đang hoạt động | `ps -ef` |
| **`kill -9 PID`** | Gửi tín hiệu SIGKILL cưỡng chế chấm dứt ngay tiến trình | `kill -9 1234` |
| **Pipe (`\|`)** | Lấy đầu ra (stdout) của lệnh trước làm đầu vào (stdin) lệnh sau | `ps -ef \| grep nginx` |
| **Ghi đè (`>`)** | Chuyển hướng đầu ra ghi đè vào tệp | `ls -l > file_list.txt` |
| **Nối thêm (`>>`)** | Chuyển hướng đầu ra ghi nối tiếp vào cuối tệp | `echo "New Entry" >> audit.log` |

---

### 복습 체크리스트
- [ ] Ghi nhớ 4 mục tiêu đánh giá HĐH: Chỉ có Turnaround Time là giảm (단축), 3 mục tiêu còn lại đều tăng.
- [ ] Phân biệt được: Kernel thường trú RAM quản lý phần cứng, Shell là trình thông dịch lệnh cho người dùng.
- [ ] Nhớ khối i-node trong UNIX không lưu tên tệp (tên tệp lưu trong thư mục cha).
- [ ] Nắm chắc giá trị trả về của `fork()`: Con nhận `0`, Cha nhận `PID con` (> 0), lỗi nhận `-1`.
- [ ] Hiểu rõ `exec()` không sinh tiến trình mới mà ghi đè chương trình lên không gian tiến trình cũ.
- [ ] Thuộc lòng giá trị bát phân quyền tệp: `r = 4`, `w = 2`, `x = 1`.
- [ ] Tính nhẩm thành thạo các số quyền: 755 (`rwxr-xr-x`), 644 (`rw-r--r--`), 640 (`rw-r-----`).
- [ ] Nắm chắc chức năng đường ống Pipe (`|`) và các lệnh shell `ls`, `cd`, `pwd`, `cat`, `grep`, `ps`, `kill`.
