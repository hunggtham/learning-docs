# UNIX 주요 구성요소 (Các Thành phần Cốt lõi của UNIX)

## 학습 목표 (Mục tiêu)
- Nắm vững cấu trúc kiến trúc 3 tầng kinh điển của hệ điều hành UNIX: Hạt nhân (Kernel - 커널), Trình thông dịch lệnh (Shell - 쉘), và Chương trình tiện ích (Utility - 유틸리티).
- Phân biệt vai trò và tính chất thường trú RAM giữa Kernel (thường trú, tương tác phần cứng) và Shell (tệp thực thi, giao tiếp người dùng).
- Làm chủ các tính năng đặc sắc của Shell: Chuyển hướng nhập/xuất (I/O Redirection), Đường ống liên kết (Pipeline `|`), và Lập trình kịch bản Shell Script.

## 핵심 키워드 (Từ khóa)
- **커널 (Kernel)**: Trọng tâm cốt lõi của UNIX, thường trú RAM, quản lý CPU/Memory/Disk/I/O và ngắt.
- **쉘 (Shell)**: Bộ thông dịch lệnh (Command Interpreter), giao diện tương tác giữa User và Kernel, không thường trú RAM.
- **유틸리티 (Utility)**: Các công cụ ứng dụng hỗ trợ người dùng (`vi`, `gcc`, `grep`, `find`).
- **파이프라인 (Pipeline `|`)**: Chuyển luồng đầu ra tiêu chuẩn (stdout) của lệnh này thành đầu vào tiêu chuẩn (stdin) của lệnh kế tiếp.
- **입·출력 재지정 (I/O Redirection)**: Định tuyến lại luồng dữ liệu vào/ra bằng các ký tự `<`, `>`, `>>`.

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [57-bai-hoc.md](57-bai-hoc.md) (Đặc trưng hệ điều hành Windows và UNIX).
- Liên kết với [64-bai-hoc.md](64-bai-hoc.md) (Lệnh UNIX và biến môi trường).
- Liên kết với [04-programming-language/87-bai-hoc.md](../../04-programming-language/lessons/87-bai-hoc.md) (Kiến trúc UNIX chi tiết).

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh câu hỏi trắc nghiệm:
  - "Thành phần cốt lõi nhất luôn thường trú trong bộ nhớ chính RAM và quản lý phần cứng" $\rightarrow$ Chọn ngay **커널 (Kernel)**.
  - "Đóng vai trò là bộ thông dịch lệnh, nhận lệnh từ người dùng và gọi chương trình" $\rightarrow$ Chọn ngay **쉘 (Shell)**.
  - Chú ý: Shell **không thường trú** trong RAM; khi người dùng đăng nhập hệ thống mới khởi chạy tiến trình Shell tương ứng.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng đối chiếu 3 thành phần chính của UNIX
| Thành phần (KR / EN) | Vị trí trong kiến trúc | Tồn tại trong bộ nhớ | Chức năng kỹ thuật cốt lõi |
| :--- | :--- | :--- | :--- |
| **커널 (Kernel)** | Nằm ở tầng thấp nhất, tiếp xúc trực tiếp với phần cứng CPU, RAM, Disk | **Luôn thường trú trong RAM** từ khi khởi động máy | Quản lý tiến trình (CPU scheduling), quản lý bộ nhớ ảo (Paging), hệ thống tệp và trình điều khiển thiết bị ngoại vi |
| **쉘 (Shell)** | Bao bọc quanh Kernel, giao tiếp trực tiếp với người dùng qua thiết bị đầu cuối | **Không thường trú**, nạp vào khi người dùng mở phiên làm việc | Tiếp nhận câu lệnh của người dùng, phân tích cú pháp, thực hiện lời gọi hệ thống (System Call) tới Kernel |
| **유틸리티 (Utility)** | Tầng ngoài cùng, các chương trình ứng dụng người dùng | Nằm trên đĩa, chỉ nạp vào RAM khi được gọi | Cung cấp các công cụ tiện ích: Trình soạn thảo văn bản (`vi`), Trình biên dịch mã nguồn (`gcc`), Tiện ích tìm kiếm (`grep`, `find`) |

#### 2. Các tính năng kỹ thuật nâng cao của Shell
- **Đổi hướng vào/ra (I/O Redirection)**:
  - `command > file`: Ghi đè luồng xuất tiêu chuẩn (stdout) của lệnh vào tệp tin.
  - `command >> file`: Ghi nối thêm dữ liệu vào cuối tệp tin đã có.
  - `command < file`: Lấy nội dung từ tệp tin làm luồng nhập tiêu chuẩn (stdin) cho lệnh.
- **Đường ống (Pipeline - `|`)**:
  - Cho phép kết hợp nhiều lệnh đơn lẻ thành một chuỗi xử lý phức tạp:
  - Luồng đầu ra (stdout) của tiến trình đứng trước dấu `|` được kết nối trực tiếp làm luồng đầu vào (stdin) của tiến trình đứng sau dấu `|`.
  - *Ví dụ*: `ls -l | grep ".txt"` $\rightarrow$ Liệt kê tệp tin rồi lọc ra các tệp có đuôi `.txt`.
- **Các dòng Shell phổ biến trong UNIX**:
  - Bourne Shell (`sh` - Stephen Bourne, chuẩn cơ sở).
  - C Shell (`csh` - Bill Joy, cú pháp tương tự ngôn ngữ C).
  - Korn Shell (`ksh` - David Korn, mở rộng tính năng của Bourne Shell).
  - Bourne Again Shell (`bash` - Chuẩn mặc định của Linux).

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ kiến trúc phân tầng của Hệ điều hành UNIX
```
                  ┌──────────────────────────────────────────────┐
                  │          NGƯỜI DÙNG (Users / Clients)        │
                  └──────────────────────┬───────────────────────┘
                                         │ tương tác
                  ┌──────────────────────▼───────────────────────┐
                  │             CHƯƠNG TRÌNH TIỆN ÍCH            │
                  │   (Utilities: vi, gcc, find, web browser)    │
                  └──────────────────────┬───────────────────────┘
                                         │ gọi qua
                  ┌──────────────────────▼───────────────────────┐
                  │        TRÌNH THÔNG DỊCH LỆNH (SHELL)         │
                  │       (sh, bash, csh, ksh, zsh)              │
                  └──────────────────────┬───────────────────────┘
                                         │ system calls
                  ┌──────────────────────▼───────────────────────┐
                  │                 HẠT NHÂN (KERNEL)            │
                  │ (Quản lý tiến trình, bộ nhớ, tệp, ngắt I/O)  │
                  └──────────────────────┬───────────────────────┘
                                         │ điều khiển
                  ┌──────────────────────▼───────────────────────┐
                  │             PHẦN CỨNG MÁY TÍNH               │
                  │             (CPU, RAM, Hard Disk, NIC)       │
                  └──────────────────────────────────────────────┘
```

#### 2. Cơ chế thực thi lệnh của Shell (Fork & Exec)
- Khi người dùng gõ một lệnh (ví dụ: `ls`):
  1. Tiến trình Shell gọi hàm `fork()` để tạo ra một tiến trình con (Child Process) sao chép y hệt Shell cha.
  2. Tiến trình con gọi tiếp hàm `exec()` để nạp tệp nhị phân thực thi của lệnh `ls` từ đĩa vào vùng nhớ của nó và tiến hành chạy.
  3. Shell cha gọi `wait()` để tạm dừng chờ cho đến khi tiến trình con kết thúc rồi mới hiển thị lại dấu nhắc lệnh (Prompt).

---

### 복습 체크리스트
- [ ] Thành phần nào trong UNIX chịu trách nhiệm tương tác trực tiếp với các linh kiện phần cứng máy tính?
- [ ] Shell trong UNIX có thường trú trong bộ nhớ chính RAM như Kernel hay không?
- [ ] Dấu gạch đứng `|` (Pipeline) trong môi trường dòng lệnh UNIX mang ý nghĩa kỹ thuật gì?
- [ ] Kể tên 3 biến thể Shell phổ biến thường được sử dụng trong các hệ thống UNIX/Linux?
