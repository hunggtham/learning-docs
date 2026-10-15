# 082. 운영체제 기능 및 종류 (Operating System OS)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và hai nhóm chương trình cấu thành hệ điều hành: Nhóm chương trình điều khiển (제어 프로그램 - Control Programs) và Nhóm chương trình xử lý (처리 프로그램 - Processing Programs).
- Phân biệt sâu sắc vai trò và vị trí của Nhân hệ điều hành (커널 - Kernel) và Trình thông dịch lệnh (쉘 - Shell) trong kiến trúc máy tính.
- Nắm vững cấu trúc 4 khối của hệ thống tệp tin UNIX: Khối khởi động (부트 블록 - Boot Block), Khối siêu dữ liệu (슈퍼 블록 - Super Block), Khối nút chỉ mục (아이노드 블록 - i-node Block), và Khối dữ liệu (데이터 블록 - Data Block).

## 핵심 키워드 (Từ khóa)
- 운영체제 구성 (OS Architecture)
- 제어 프로그램 (Control Programs / 감시, 작업 제어, 데이터 관리)
- 처리 프로그램 (Processing Programs / 언어 번역, 서비스, 문제)
- 커널 vs 쉘 (Kernel Core vs Shell Interface)
- UNIX 파일 시스템 구조 (UNIX File System Layout)
- 슈퍼 블록 (Super Block / 파일 시스템 전체 정보)
- i-node 블록 (Index Node / 파일 메타데이터)

## 선행·연결 개념 (Kiến thức liên kết)
- [33-bai-hoc.md](33-bai-hoc.md): Quản lý bộ nhớ và điều phối tiến trình.
- [35-bai-hoc.md](35-bai-hoc.md): Định nghĩa và 4 mục tiêu hiệu năng của hệ điều hành.
- [36-bai-hoc.md](36-bai-hoc.md): Cấu trúc tệp tin UNIX và biến môi trường.

## 읽는 방법 (Cách đọc)
- Ghi nhớ thần chú phân loại 2 nhóm chương trình của hệ điều hành:
  - **제어 프로그램 (Chương trình điều khiển):** Thần chú **감·작·데**
    - **감 (Giám - 감시 프로그램 / Supervisor):** Là trái tim của OS (Kernel), điều phối toàn bộ tài nguyên CPU, bộ nhớ và các chương trình khác.
    - **작 (Tác - 작업 제어 / Job Control):** Điều phối thứ tự chạy giữa các công việc (Jobs).
    - **데 (Dữ - 데이터 관리 / Data Management):** Quản lý truyền dẫn I/O và cấu trúc tệp dữ liệu.
  - **처리 프로그램 (Chương trình xử lý):** Thần chú **언·서·문**
    - **언 (Ngôn - 언어 번역 / Language Translator):** Trình biên dịch (Compiler, Assembler).
    - **서 (Dịch - 서비스 프로그램 / Service Utility):** Các tiện ích hệ thống (Sort/Merge).
    - **문 (Vấn - 문제 프로그램 / Problem Program):** Các ứng dụng do người dùng tự viết.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh: 커널 (Kernel) vs 쉘 (Shell):**

| Thành phần | Vị trí phân tầng | Bản chất chức năng | Quyền hạn và tương tác |
| :--- | :--- | :--- | :--- |
| **커널 (Kernel)** | Nằm ở **tầng lõi sâu nhất**, tiếp xúc trực tiếp với phần cứng | Là bộ não trung tâm của OS; quản lý trực tiếp CPU, bộ nhớ RAM, tiến trình và ngắt thiết bị | Chạy ở chế độ đặc quyền (**Kernel Mode / Ring 0**); không giao tiếp trực tiếp với người dùng |
| **쉘 (Shell)** | Nằm ở **lớp vỏ bên ngoài**, bao bọc lấy Kernel | Là **trình thông dịch lệnh (Command Interpreter)**; chuyển đổi lệnh của người dùng thành System Calls gửi cho Kernel | Chạy ở chế độ người dùng (**User Mode / Ring 3**); cung cấp giao diện CLI (bash) hoặc GUI |

- **Bảng cấu trúc 4 phân vùng của hệ thống tệp UNIX (UNIX File System):**

| Khối phân vùng | Tên tiếng Hàn & Anh | Nội dung lưu trữ chi tiết |
| :--- | :--- | :--- |
| **1. Boot Block** | **부트 블록** | Chứa đoạn mã bộ nạp khởi động (**Bootstrap Loader**) dùng để khởi động hệ điều hành khi bật máy tính |
| **2. Super Block** | **슈퍼 블록** | Lưu trữ thông tin tổng quan của toàn bộ hệ thống tệp: **Dung lượng đĩa, số lượng khối trống (Free Blocks), danh sách inode trống** |
| **3. i-node Block** | **아이노드 블록 (Index Node)** | Chứa thông tin **Siêu dữ liệu (Metadata)** của từng tệp tin: Quyền truy cập, chủ sở hữu, kích thước tệp, thời gian sửa đổi, và **địa chỉ con trỏ tới các khối dữ liệu** (Không lưu nội dung thực tế) |
| **4. Data Block** | **데이터 블록** | Lưu trữ **nội dung dữ liệu thực tế (Actual Data)** của tệp tin hoặc thư mục |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Cấu trúc con trỏ trong i-node:**
  - Mỗi i-node trong UNIX có kích thước cố định (thường là 128 hoặc 256 bytes) và quản lý 15 con trỏ địa chỉ khối:
    - 12 con trỏ trực tiếp (Direct Pointers): Trỏ thẳng tới 12 Data Block đầu tiên.
    - 1 con trỏ gián tiếp đơn (Single Indirect): Trỏ tới 1 khối chứa danh sách con trỏ.
    - 1 con trỏ gián tiếp kép (Double Indirect) và 1 con trỏ gián tiếp ba (Triple Indirect) để hỗ trợ các tệp tin có dung lượng khổng lồ hàng Terabytes.

### 복습 체크리스트
- [ ] Nhớ 제어 프로그램 gồm 3 loại: 감시 (Supervisor), 작업 제어 (Job Control), 데이터 관리 (Data Management).
- [ ] Nhớ 처리 프로그램 gồm: 언어 번역 (Compiler), 서비스 (Utility), 문제 (Problem).
- [ ] Phân biệt được Kernel (lõi não điều khiển phần cứng) và Shell (vỏ thông dịch lệnh người dùng).
- [ ] Kể tên 4 khối của UNIX File System: Boot Block, Super Block, i-node Block, Data Block.
