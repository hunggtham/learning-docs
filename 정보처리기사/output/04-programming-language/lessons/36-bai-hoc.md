# 283 - 288. 운영체제 구성 및 UNIX 시스템 (OS & UNIX)

## 학습 목표 (Mục tiêu)
- Nắm vững cấu trúc hai phân hệ chương trình của hệ điều hành: Chương trình điều khiển (제어 프로그램) và Chương trình xử lý (처리 프로그램).
- Phân biệt sâu sắc khái niệm Mô tả tệp (파일 디스크립터 - File Descriptor): số nguyên định danh (Integer Handle) do tiến trình sử dụng để tham chiếu tệp đang mở, hoàn toàn khác biệt với khối điều khiển tệp FCB hoặc khối i-node lưu trữ thuộc tính tệp.
- Nhớ các biến môi trường thông dụng trong hệ điều hành UNIX/Linux: `$HOME` (thư mục người dùng), `$PATH` (đường dẫn tìm kiếm lệnh thực thi), và `$PWD` (thư mục làm việc hiện thời).

## 핵심 키워드 (Từ khóa)
- 제어 프로그램 vs 처리 프로그램 (Control vs Processing Programs)
- UNIX 시스템 특징 (UNIX Operating System)
- 파일 디스크립터 (File Descriptor / 정수 핸들 / FD)
- i-node vs FCB (File Control Block / 속성 제어 블록)
- UNIX 환경 변수 (`$HOME`, `$PATH`, `$PWD`)
- 표준 파일 디스크립터 (0: stdin, 1: stdout, 2: stderr)

## 선행·연결 개념 (Kiến thức liên kết)
- [35-bai-hoc.md](35-bai-hoc.md): Định nghĩa và 4 mục tiêu hiệu năng của hệ điều hành.
- [37-bai-hoc.md](37-bai-hoc.md): Chiến lược nạp bộ nhớ First Fit, Best Fit, Worst Fit.
- [06-bai-hoc.md](06-bai-hoc.md): Lệnh Shell và cấu hình biến môi trường trong Linux.

## 읽는 방법 (Cách đọc)
- Phân biệt rạch ròi giữa File Descriptor và i-node/FCB (Bẫy đề thi cực kỳ quan trọng):
  - **i-node / FCB (File Control Block):** Là khối dữ liệu tĩnh lưu trên đĩa cứng chứa **toàn bộ thuộc tính vật lý của tệp tin** (kích thước, chủ sở hữu, ngày tạo, quyền hạn, con trỏ dữ liệu).
  - **File Descriptor (FD):** Là một **số nguyên không âm (Integer Handle: 0, 1, 2, 3...)** được hệ điều hành cấp phát tạm thời cho một tiến trình khi tiến trình đó mở một tệp (`open()`). Tiến trình dùng số nguyên này như một "vé vào cổng" để thực hiện đọc (`read()`) hoặc ghi (`write()`) tệp mà không cần duyệt lại cây thư mục.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng 3 bộ mô tả tệp chuẩn mặc định (Standard File Descriptors) trong UNIX:**

| Mã số FD | Luồng dữ liệu (Stream) | Thiết bị phần cứng mặc định | Cú pháp chuyển hướng (Redirection) |
| :---: | :--- | :--- | :--- |
| **`0`** | **Standard Input (`stdin`)** | Bàn phím (Keyboard) | `<` |
| **`1`** | **Standard Output (`stdout`)** | Màn hình hiển thị (Console Display) | `>` hoặc `1>` |
| **`2`** | **Standard Error (`stderr`)** | Màn hình hiển thị (Console Display) | `2>` |

- **Bảng các biến môi trường cốt lõi trong UNIX/Linux:**

| Tên biến môi trường | Giá trị lưu trữ | Mục đích sử dụng |
| :--- | :--- | :--- |
| **`$HOME`** | Đường dẫn tới thư mục gốc của tài khoản người dùng đăng nhập | Ví dụ: `/home/user` hoặc `/root` |
| **`$PATH`** | Danh sách các thư mục chứa tệp nhị phân thực thi, phân tách bằng dấu hai chấm `:` | Giúp Shell tìm thấy lệnh mà người dùng không cần gõ đường dẫn tuyệt đối |
| **`$PWD`** | Đường dẫn đầy đủ của **thư mục làm việc hiện tại (Print Working Directory)** | Tương đương kết quả của lệnh `pwd` |
| **`$USER`** | Tên tài khoản người dùng đang đăng nhập vào phiên làm việc | Kiểm tra danh tính người vận hành |
| **`$SHELL`** | Đường dẫn của trình thông dịch lệnh mặc định đang dùng | Ví dụ: `/bin/bash` hoặc `/bin/zsh` |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Mối liên hệ giữa File Descriptor Table, Open File Table và i-node Table:**
  - Mỗi tiến trình có một bảng mô tả tệp riêng (Process FD Table) chứa các số nguyên $0, 1, 2, 3...$
  - Các con số này trỏ tới một bảng chung của toàn hệ thống (System-wide Open File Table) lưu con trỏ vị trí đọc/ghi hiện tại (File Offset) và cờ quyền (Read/Write).
  - Bảng Open File Table này lại trỏ tiếp tới bảng i-node (i-node Table) lưu trên bộ nhớ để thao tác với các khối đĩa thực tế.

### 복습 체크리스트
- [ ] Nhớ File Descriptor là số nguyên (Integer Handle), không phải khối lưu trữ thuộc tính FCB/inode.
- [ ] Nhớ 3 số FD mặc định: 0 (stdin - bàn phím), 1 (stdout - màn hình), 2 (stderr - lỗi).
- [ ] Nhớ các biến môi trường: `$HOME` (thư mục nhà), `$PATH` (đường dẫn lệnh), `$PWD` (thư mục hiện tại).
- [ ] Phân biệt được nhiệm vụ của 제어 프로그램 (감시, 작업, 데이터) và 처리 프로그램 (언어, 서비스, 문제).
