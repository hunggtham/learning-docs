# 운영체제 기초, UNIX/Linux 구조 및 쉘 스크립트 (Tổng quan HĐH, UNIX/Linux & Shell Script)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và 4 mục tiêu đánh giá cốt lõi của Hệ điều hành (운영체제 4대 평가 목적): Tăng Năng suất (Throughput), Giảm Thời gian quay vòng (Turnaround Time), Tăng Độ tin cậy (Reliability), và Tăng Khả năng sẵn sàng (Availability).
- Phân biệt cấu trúc 3 tầng của hệ điều hành UNIX/Linux: Hạt nhân Kernel (thường trú RAM), Lớp vỏ Shell (trình thông dịch lệnh) và Tiện ích Utility; hiểu rõ cấu trúc khối dữ liệu i-node trong hệ thống tệp.
- Sử dụng thành thạo biến môi trường (`PATH`) và tính toán chính xác quyền truy cập tệp nhị phân/bát phân với lệnh `chmod` (ví dụ `755`, `644`) trong kịch bản Shell Script.

## 핵심 키워드 (Từ khóa)
- 운영체제 4대 목적 (OS 4 Evaluation Goals) — 처리능력 향상, 반환시간 단축, 신뢰도 향상, 사용가능도 향상.
- 제어 프로그램 vs 처리 프로그램 (Control vs Processing Programs) — 감시/작업/데이터 관리 vs 언어번역/서비스.
- 커널 vs 쉘 (Kernel vs Shell) — Luôn thường trú RAM, giao tiếp phần cứng vs Trình thông dịch lệnh tương tác người dùng.
- i-node 구조 (i-node Structure) — Khối lưu trữ thông tin thuộc tính tệp (quyền, kích thước, con trỏ đĩa, cấm lưu tên tệp).
- 파일 권한 설정 (File Permissions `chmod`) — Quyền Đọc ($r=4$), Ghi ($w=2$), Thực thi ($x=1$) theo 3 nhóm User/Group/Others.
- 환경변수 PATH (Environment Variable PATH) — Danh sách các thư mục chứa tệp thực thi mà hệ thống tìm kiếm tự động.

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Kế thừa từ `10-phan-loai-ngon-ngu-lap-trinh-bien-dich-vs-thong-dich.md`, khi mã nguồn được biên dịch ra tệp nhị phân, hệ điều hành là môi trường chịu trách nhiệm nạp, cấp phát tài nguyên và điều phối cho chương trình chạy.
- **Đang giải quyết gì (Current Problem):** Giải quyết câu hỏi về nền tảng hệ thống: Làm sao người dùng ra lệnh cho phần cứng hoạt động, quyền truy cập dữ liệu được bảo vệ thế nào trên máy chủ và tiêu chí nào để đo lường một hệ điều hành hoạt động hiệu quả.
- **Dùng đi đâu (Forward Handoff):** Khi Kernel khởi động và nạp một chương trình vào RAM, một Tiến trình (Process) sẽ được sinh ra; cơ chế quản lý vòng đời và điều phối CPU cho tiến trình sẽ được trình bày ở bài `12-tien-trinh-luong-va-dieu-phoi-cpu.md`.

## 읽는 방법 (Cách đọc)
- **4 mục tiêu đánh giá HĐH:** Nhớ chỉ duy nhất một mục tiêu là **GIẢM (단축 / Minimize)**: **Thời gian quay vòng (반환 시간 - Turnaround Time)**. Cả 3 tiêu chí còn lại (Năng suất 처리능력, Độ tin cậy 신뢰도, Khả năng sẵn sàng 사용가능도) đều phải **TĂNG (향상 / Maximize)**.
- **Kernel vs Shell:** Kernel là "Trái tim/Hạt nhân" nằm vĩnh viễn trong RAM điều khiển phần cứng; Shell là "Lớp vỏ" nhận lệnh gõ từ bàn phím dịch cho Kernel hiểu.
- **Quyền `chmod`:** $r = 4, w = 2, x = 1$. Lấy tổng ba số cho từng vị trí `User / Group / Others` (ví dụ `rwx = 4+2+1 = 7`, `r-x = 4+1 = 5`).

---

## 운영체제 기초, UNIX/Linux 구조 및 쉘 스크립트

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [한국어]: `운영체제의 4대 목적 중 반환시간은 단축되어야 하며, 처리능력, 신뢰도, 사용가능도는 향상되어야 한다. UNIX 시스템은 커널(하드웨어 제어, RAM 상주), 쉘(명령어 해석기), 유틸리티로 구성된다. chmod 명령에서 r=4, w=2, x=1의 8진수 합산 방식을 적용한다.`
  - [Tiếng Việt]: Trong 4 mục tiêu của hệ điều hành, thời gian quay vòng phải giảm, còn năng suất, độ tin cậy và khả năng sẵn sàng phải tăng. UNIX gồm Kernel (điều khiển phần cứng, thường trú RAM), Shell (trình thông dịch lệnh) và Utility. Lệnh chmod áp dụng cộng tổng bát phân: r=4, w=2, x=1.

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

- **3. Bảng tính toán quyền hạn tệp UNIX/Linux (`chmod` - File Permissions):**

| Quyền hạn | Ký hiệu chữ | Giá trị bát phân | Ý nghĩa thao tác đối với tệp |
| :---: | :---: | :---: | :--- |
| **Đọc (Read)** | `r` | **`4`** | Đọc nội dung tệp; xem danh sách tệp trong thư mục. |
| **Ghi (Write)** | `w` | **`2`** | Sửa đổi, ghi đè, xóa nội dung tệp. |
| **Thực thi (Execute)** | `x` | **`1`** | Chạy tệp kịch bản (Script), chương trình thực thi nhị phân. |
| **Không có quyền** | `-` | **`0`** | Không có bất kỳ thao tác nào được cấp phép. |

- **Bảng mẫu các tổ hợp `chmod` thường gặp trong đề thi:**
  - `chmod 755 script.sh` $\rightarrow$ User: $4+2+1 = \mathbf{7}$ (`rwx`), Group: $4+1 = \mathbf{5}$ (`r-x`), Others: $4+1 = \mathbf{5}$ (`r-x`).
  - `chmod 644 document.txt` $\rightarrow$ User: $4+2 = \mathbf{6}$ (`rw-`), Group: $4$ (`r--`), Others: $4$ (`r--`).
  - `chmod 777 data.log` $\rightarrow$ Cấp toàn quyền cho mọi người dùng (`rwxrwxrwx`).

- **주의/함정 (Bẫy đề thi):**
  - **Khối i-node không chứa tên tệp:** Đề thi khẳng định *"Khối i-node trong UNIX lưu trữ tên tệp (File Name)"* $\rightarrow$ Đây là khẳng định **SAI**. i-node chỉ lưu metadata (quyền, kích thước, thời gian tạo, con trỏ khối đĩa); **tên tệp được lưu trong tệp thư mục cha (Directory File)**.
  - **Nhầm mục tiêu HĐH:** Chọn phương án *"Tăng thời gian quay vòng (반환시간 향상)"* là sai bẫy; thời gian quay vòng càng ngắn càng tốt (단축).
  - **Kịch bản Shell Script:** Dòng đầu tiên `#!/bin/bash` (Shebang) dùng để chỉ định trình thông dịch shell sẽ thực thi kịch bản đó.

- **한 문장 설명 (Câu chốt tự nhớ):**
  - *"4 mục tiêu chỉ giảm 반환시간; Kernel thường trú RAM, Shell nhận lệnh thông dịch; chmod cộng 4-2-1 cho User, Group, Others."*

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Bài toán trắc nghiệm tính toán phân quyền `chmod` chuẩn đề thi:
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

#### 2. Cấu trúc kịch bản Shell Script và biến môi trường:
```bash
#!/bin/bash
# Khai bao bien cuc bo
APP_NAME="InfoEngine"
COUNT=5

# In bien moi truong he thong
echo "Nguoi dung hien tai: $USER"
echo "Thu muc Home: $HOME"
echo "Duong dan tim kiem PATH: $PATH"

# Vong lap for trong Shell
for ((i=1; i<=COUNT; i++))
do
    echo "Tien trinh $APP_NAME lan $i dang chay..."
done
```

#### 3. Bảng đối chiếu các lệnh CLI UNIX/Linux thường xuất hiện trong đề thi:

| Lệnh Linux / UNIX | Bản chất chức năng | Lệnh tương đương trên Windows |
| :--- | :--- | :--- |
| **`ls -l`** | Liệt kê chi tiết tệp, thư mục và quyền truy cập | `dir` |
| **`pwd`** | Hiển thị đường dẫn thư mục làm việc hiện tại (Print Working Directory)| `cd` (không tham số) |
| **`cp` / `mv`** | Sao chép (`cp`) hoặc Di chuyển/Đổi tên (`mv`) tệp tin | `copy` / `move` |
| **`rm -rf`** | Xóa tệp hoặc thư mục đệ quy cưỡng chế | `del` / `rmdir /s /q` |
| **`cat` / `more`** | Hiển thị nội dung tệp văn bản ra màn hình | `type` |
| **`grep`** | Tìm kiếm dòng chứa mẫu ký tự (biểu thức chính quy) trong tệp| `findstr` |
| **`ps -ef`** | Hiển thị danh sách toàn bộ các tiến trình đang hoạt động | `tasklist` |
| **`kill -9 PID`** | Cưỡng chế chấm dứt ngay lập tức một tiến trình theo PID | `taskkill /f /pid` |

---

### 복습 체크리스트
- [ ] Ghi nhớ 4 mục tiêu đánh giá HĐH: Chỉ có Turnaround Time là giảm (단축), 3 mục tiêu còn lại đều tăng.
- [ ] Phân biệt được: Kernel thường trú RAM quản lý phần cứng, Shell là trình thông dịch lệnh cho người dùng.
- [ ] Nhớ khối i-node trong UNIX không lưu tên tệp (tên tệp lưu trong thư mục cha).
- [ ] Thuộc lòng giá trị bát phân quyền tệp: `r = 4`, `w = 2`, `x = 1`.
- [ ] Tính nhẩm thành thạo các số quyền: 755 (`rwxr-xr-x`), 644 (`rw-r--r--`), 700 (`rwx------`).
- [ ] Nắm được vai trò của biến `PATH`: Định nghĩa các thư mục tìm kiếm tệp thực thi.
