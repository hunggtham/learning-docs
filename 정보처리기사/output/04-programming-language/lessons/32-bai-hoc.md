# 스크립트 및 운영체제 (Script Languages & Operating Systems)

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm và đặc tính của ngôn ngữ kịch bản (스크립트 언어 - Script Languages) so với ngôn ngữ biên dịch truyền thống (Compiled Languages).
- Nắm vững 5 đặc trưng cốt lõi của hệ điều hành UNIX: Viết bằng ngôn ngữ C (C언어로 작성), Tính khả chuyển cao (이식성), Hỗ trợ đa người dùng (다중 사용자), Đa nhiệm (다중 작업), và Cấu trúc tệp tin dạng cây (트리 구조 파일 시스템).
- Ghi nhớ chức năng của các câu lệnh và lời gọi hệ thống (System Calls) tiêu biểu trong UNIX: `fork()`, `wait()`, `uname`, `chmod`, `chown`, `ls`, và `cat`.

## 핵심 키워드 (Từ khóa)
- 스크립트 언어 (Script Languages / 인터프리터 방식 / 빠른 개발)
- UNIX 운영체제 특징 (Features of UNIX)
- C언어 기반 이식성 (High Portability via C Language)
- 트리 구조 파일 시스템 (Tree-structured File System)
- fork() 시스템 호출 (프로세스 복제 생성)
- wait() 시스템 호출 (자식 프로세스 종료 대기)
- uname 명령어 (시스템 정보 출력)

## 선행·연결 개념 (Kiến thức liên kết)
- [31-bai-hoc.md](31-bai-hoc.md): Thư viện liên kết tĩnh và liên kết động.
- [33-bai-hoc.md](33-bai-hoc.md): Quản lý bộ nhớ và quản lý tiến trình trong hệ điều hành.
- [06-bai-hoc.md](06-bai-hoc.md): Biến môi trường và các lệnh kịch bản Shell trong Linux.

## 읽는 방법 (Cách đọc)
- Phân biệt hai mảng kiến thức:
  - **Script Languages:** Chạy thông qua trình thông dịch (Interpreter), không cần bước biên dịch ra mã máy trung gian (như JavaScript, Python, PHP, Shell Script). Phát triển nhanh nhưng tốc độ thực thi chậm hơn ngôn ngữ biên dịch như C/C++.
  - **UNIX:** Là cha đẻ của các hệ điều hành hiện đại (Linux, macOS). Được viết lại 90% bằng **ngôn ngữ C** bởi Ken Thompson và Dennis Ritchie tại Bell Labs $\rightarrow$ Giúp UNIX dễ dàng biên dịch và chạy trên các kiến trúc phần cứng khác nhau mà không cần viết lại từ đầu bằng Assembly (Tính khả chuyển - Portability).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng 5 đặc trưng kinh điển của hệ điều hành UNIX:**

| Đặc trưng cốt lõi | Chi tiết kỹ thuật chuẩn đề thi |
| :--- | :--- |
| **C언어로 대부분 작성** | Viết bằng ngôn ngữ bậc cao C; giúp hệ thống có **tính khả chuyển cực cao (높은 이식성)** và dễ dàng mở rộng |
| **다중 사용자 (Multi-User)** | Nhiều người dùng có thể cùng đăng nhập và làm việc trên hệ thống tại cùng một thời điểm |
| **다중 작업 (Multi-Tasking)** | Cho phép nhiều tiến trình (Process) cùng chạy đồng thời; áp dụng cơ chế phân chia thời gian (Time-sharing) |
| **트리 구조 파일 시스템** | Toàn bộ tệp và thư mục được tổ chức theo cấu trúc cây bắt đầu từ thư mục gốc Root (`/`) |
| **대화식 운영체제 (Interactive)** | Giao tiếp với người dùng qua trình thông dịch dòng lệnh (Shell) theo cơ chế hỏi - đáp trực tiếp |

- **Bảng các lệnh và System Call quản lý tiến trình trong UNIX:**

| Lệnh / Lời gọi hệ thống | Chức năng chi tiết chuẩn thi |
| :--- | :--- |
| **`fork()`** | **Tạo ra một tiến trình con mới (자식 프로세스 생성)** bằng cách sao chép y hệt toàn bộ không gian nhớ của tiến trình cha |
| **`wait()`** | Khiến tiến trình cha **tạm dừng thực thi để chờ cho đến khi tiến trình con kết thúc hoàn tất** |
| **`exec()`** | Nạp một chương trình nhị phân mới đè lên không gian nhớ của tiến trình hiện tại để thực thi |
| **`exit()`** | Chấm dứt tiến trình hiện tại và trả về mã trạng thái thoát cho tiến trình cha |
| **`uname`** | Hiển thị thông tin hệ điều hành (Tên kernel, phiên bản, kiến trúc máy tính) |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Giá trị trả về của lời gọi hệ thống `fork()`:**
  - `fork()` là hàm duy nhất được gọi 1 lần nhưng trả về kết quả 2 lần ở hai tiến trình khác nhau:
    - Ở tiến trình cha: Trả về **PID của tiến trình con** (một số nguyên dương).
    - Ở tiến trình con: Trả về số **`0`**.
    - Nếu tạo thất bại: Trả về số **`-1`**.
  - Lập trình viên dùng giá trị trả về này để phân nhánh logic cho cha và con chạy các công việc độc lập.

### 복습 체크리스트
- [ ] Nhớ UNIX được viết phần lớn bằng ngôn ngữ C nên có tính khả chuyển (이식성) rất cao.
- [ ] Nhớ hệ thống tệp tin của UNIX có cấu trúc hình Cây (Tree structure) bắt đầu từ gốc `/`.
- [ ] Nhớ lời gọi hệ thống `fork()` dùng để tạo tiến trình con mới (nhân bản tiến trình).
- [ ] Nhớ lời gọi hệ thống `wait()` dùng để chờ tiến trình con kết thúc.
