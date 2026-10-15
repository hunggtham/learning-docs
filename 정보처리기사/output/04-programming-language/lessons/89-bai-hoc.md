# 287. UNIX 시스템의 구성 (Cấu trúc hệ thống UNIX)

## 학습 목표 (Mục tiêu)
- Nắm vững kiến trúc phân tầng 3 lớp của hệ điều hành UNIX: **Hạt nhân (커널 - Kernel)**, **Vỏ giao tiếp (쉘 - Shell)**, và **Tiện ích ứng dụng (유틸리티 - Utility)**.
- Phân biệt sự khác nhau mang tính bản chất giữa Kernel (quản lý phần cứng, tài nguyên, thường trú trong RAM) và Shell (trình thông dịch lệnh, đóng vai trò giao diện tương tác người dùng).
- Nhận diện các biến thể Shell phổ biến trong hệ sinh thái UNIX/Linux (sh, bash, csh, ksh, zsh) và cơ chế chuyển đổi Shell linh hoạt.

## 핵심 키워드 (Từ khóa)
- UNIX 시스템 구성 (UNIX System Architecture)
- 커널 (Kernel - 주기억장치 상주, 하드웨어 제어)
- 쉘 (Shell - 명령어 해석기, 사용자 인터페이스)
- 유틸리티 (Utility - 응용 프로그램 및 컴파일러)
- 시스템 호출 (System Call - API 인터페이스)
- 표준 쉘 종류 (Bourne sh, C-Shell csh, Korn ksh, Bash)

## 선행·연결 개념 (Kiến thức liên kết)
- [88-bai-hoc.md](88-bai-hoc.md): Mô hình Tập làm việc Working Set trong quản lý bộ nhớ ảo.
- [90-bai-hoc.md](90-bai-hoc.md): Thuật toán thay thế trang nhớ (OPT, FIFO, LRU, LFU, NUR).
- [06-bai-hoc.md](06-bai-hoc.md): Các lệnh quản trị hệ thống và shell script trong UNIX/Linux.

## 읽는 방법 (Cách đọc)
- Điểm mấu chốt bất di bất dịch trong mọi đề thi:
  - Khi hỏi về **"Thành phần quản lý trực tiếp phần cứng, quản lý tiến trình, bộ nhớ, tệp tin và LUÔN THƯỜNG TRÚ TRONG RAM (주기억장치에 항상 상주)"** $\rightarrow$ Chọn ngay **커널 (Kernel)**.
  - Khi hỏi về **"Thành phần nhận lệnh từ người dùng, dịch lệnh và chuyển giao cho Kernel thực thi (명령어 해석기 - Command Interpreter)"** $\rightarrow$ Chọn ngay **쉘 (Shell)**.
  - Khẩu quyết hình tượng: *Kernel là Đầu bếp trong bếp kín (phần cứng), Shell là Phục vụ bàn nhận order của khách (người dùng).*

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng đối chiếu 3 thành phần cốt lõi của UNIX:**

| Thành phần hệ thống | Vị trí & Trạng thái hoạt động | Chức năng kỹ thuật chi tiết | Khả năng thay thế |
| :--- | :--- | :--- | :---: |
| **커널 (Kernel - Hạt nhân)** | Nằm ở tầng lõi thấp nhất, **luôn luôn thường trú trong RAM** từ khi khởi động máy. | Trực tiếp điều khiển và tương tác với phần cứng (CPU, RAM, Ổ đĩa, Card mạng); Quản lý tiến trình (Lập lịch CPU, tạo/hủy process qua `fork`, `exec`); Quản lý bộ nhớ thực và bộ nhớ ảo; Quản lý hệ thống tệp tin (File System qua i-node) và thiết bị I/O. | Cố định cho từng phiên bản bản phân phối |
| **쉘 (Shell - Lớp vỏ)** | Nằm ở tầng trung gian giữa Kernel và người dùng; là một tiến trình bình thường. | Đóng vai trò là **Trình thông dịch lệnh (명령어 해석기)**; Đọc lệnh do người dùng gõ vào, phân tích cú pháp, tìm kiếm tệp thực thi và thực hiện các lệnh gọi hệ thống (**System Call**) tới Kernel; Hỗ trợ lập trình Shell Script, đường ống (Pipe `\|`), và chuyển hướng (Redirection `<`, `>`). | **Người dùng có thể tự do thay đổi tùy ý** |
| **유틸리티 (Utility - Tiện ích)** | Nằm ở tầng ngoài cùng của không gian người dùng (User Space). | Các chương trình ứng dụng phục vụ công việc: Trình biên dịch (`gcc`), Trình soạn thảo văn bản (`vi`, `nano`), Công cụ lọc tìm kiếm (`grep`, `find`, `awk`, `sed`), Nén tệp (`tar`, `gzip`). | Cài đặt thêm bớt tự do |

- **2. Bảng nhận diện các loại Shell kinh điển trong UNIX/Linux:**

| Tên Shell | Ký hiệu tệp | Tác giả & Đặc trưng thi cử |
| :--- | :--- | :--- |
| **Bourne Shell** | `/bin/sh` | Do Stephen Bourne phát triển tại Bell Labs; shell tiêu chuẩn ban đầu của UNIX. |
| **C Shell** | `/bin/csh` | Do Bill Joy phát triển tại UC Berkeley; cú pháp script rất giống ngôn ngữ lập trình C. |
| **Korn Shell** | `/bin/ksh` | Do David Korn phát triển; kết hợp ưu điểm của Bourne shell và tính tương tác của C shell. |
| **Bash Shell** | `/bin/bash` | *Bourne Again Shell* thuộc dự án GNU; shell mặc định tiêu chuẩn trên hầu hết bản phân phối Linux hiện đại. |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Giao diện Lời gọi hệ thống (System Call - 시스템 호출):**
  - Trong UNIX, Kernel vận hành ở chế độ đặc quyền cao nhất (**Kernel Mode / Ring 0**), còn các chương trình tiện ích và Shell chạy ở chế độ người dùng (**User Mode / Ring 3**).
  - Khi Shell hoặc ứng dụng muốn đọc tệp tin hay cấp phát bộ nhớ, chúng không được phép chạm trực tiếp vào phần cứng mà bắt buộc phải phát ra một **System Call** (như `open()`, `read()`, `write()`, `fork()`). Khi đó CPU chuyển chế độ sang Kernel Mode để hạt nhân xử lý an toàn và trả lại kết quả.

### 복습 체크리스트
- [ ] Ghi nhớ Kernel là hạt nhân quản lý phần cứng và luôn thường trú trong RAM.
- [ ] Ghi nhớ Shell là trình thông dịch lệnh (명령어 해석기) đóng vai trò giao diện với người dùng.
- [ ] Khẳng định Shell có thể thay đổi linh hoạt bởi người dùng, còn Kernel thì không.
- [ ] Kể tên được 4 loại Shell kinh điển: Bourne sh, C-Shell csh, Korn ksh, và Bash.
