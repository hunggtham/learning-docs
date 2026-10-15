# 148-154. 파일 시스템과 디렉터리, 보안 (File System & Security)

## 학습 목표 (Mục tiêu)
- Nắm vững 3 cấu trúc tệp dữ liệu nền tảng trong hệ thống máy tính: **Tệp tuần tự (`순차 파일 / SAM`)**, **Tệp tuần tự có chỉ mục (`색인 순차 파일 / ISAM`)**, và **Tệp trực tiếp (`직접 파일 / DAM`)**.
- Phân tích chi tiết 3 vùng lưu trữ của tệp ISAM: Vùng cơ sở (`기본 구역`), Vùng chỉ mục (`색인 구역`), và Vùng tràn (`오버플로 구역`).
- So sánh các mô hình cấu trúc thư mục từ đơn giản đến hiện đại: Thư mục 1 cấp, 2 cấp, Thư mục dạng cây (`트리 구조`), và Thư mục đồ thị không chu trình (`비순환 그래프`).
- Phân biệt các kỹ thuật kiểm soát an toàn tệp: Ma trận kiểm soát truy cập (`접근 제어 행렬`), Danh sách kiểm soát truy cập (`ACL`), và Danh sách quyền hạn (`Capability List`).

## 핵심 키워드 (Từ khóa)
- 순차 파일 (Tệp tuần tự / Sequential File)
- 색인 순차 파일 (Tệp tuần tự có chỉ mục / ISAM)
- 직접 파일 (Tệp trực tiếp / Direct File: Hashing)
- 기본 구역 (Vùng cơ sở / Prime Area)
- 오버플로 구역 (Vùng tràn / Overflow Area)
- 트리 디렉터리 (Thư mục dạng cây / Tree Directory)
- 비순환 그래프 디렉터리 (Thư mục đồ thị không chu trình / Acyclic Graph)
- 접근 제어 리스트 (Danh sách kiểm soát truy cập / ACL)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([45-bai-hoc.md](45-bai-hoc.md), [46-bai-hoc.md](46-bai-hoc.md)):** Để lưu trữ các bảng và phân vùng CSDL, hệ quản trị DBMS phải dựa trên hệ thống tệp và cơ chế quản lý khối đĩa của hệ điều hành.
- **Tiếp nối sang các bài sau ([48-bai-hoc.md](48-bai-hoc.md), [49-bai-hoc.md](49-bai-hoc.md)):** Hệ thống tệp UNIX với cấu trúc khối I-node và các câu lệnh phân quyền chmod/chown là sự hiện thực hóa cụ thể nhất của các lý thuyết trong bài này.

## 읽는 방법 (Cách đọc)
- Học thuộc 3 vùng lưu trữ của tệp **색인 순차 파일 (ISAM)**:
  - **기본 구역 (Prime Area):** Nơi chứa dữ liệu thực tế.
  - **색인 구역 (Index Area):** Nơi chứa cây chỉ mục (Master, Cylinder, Track Index).
  - **오버플로 구역 (Overflow Area):** Nơi chứa bản ghi mới bị tràn ra khi Prime Area hết chỗ.
- Phân biệt cấu trúc thư mục cho phép chia sẻ: **비순환 그래프 디렉터리 (Acyclic Graph)** cho phép chia sẻ tệp/thư mục dùng chung giữa các người dùng mà không tạo thành vòng lặp vô tận.

---

## 148-154. 파일 시스템과 디렉터리, 보안 (File System & Security)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng phân loại 3 cấu trúc Tệp dữ liệu truyền thống:**
  | Cấu trúc Tệp | Thuật ngữ Hàn - Anh | Cơ chế tổ chức & Truy cập | Ưu điểm & Nhược điểm |
  |---|---|---|---|
  | **Tệp tuần tự** | `순차 파일` (Sequential File / SAM) | Các bản ghi được ghi liên tục theo thứ tự khóa trên thiết bị lưu trữ (như băng từ Magnetic Tape). | - Ưu điểm: Mật độ lưu trữ cao, tận dụng 100% không gian. ; - Nhược điểm: Truy xuất ngẫu nhiên cực chậm; thao tác thêm/xóa bản ghi phức tạp. |
  | **Tệp tuần tự có chỉ mục** | `색인 순차 파일` (Indexed Sequential / ISAM) | Kết hợp lưu trữ tuần tự với bảng chỉ mục (Index) hỗ trợ cả truy xuất tuần tự lẫn truy xuất ngẫu nhiên. | - Ưu điểm: Truy xuất ngẫu nhiên nhanh. ; - Nhược điểm: Tốn thêm dung lượng cho vùng chỉ mục và vùng tràn. |
  | **Tệp trực tiếp** | `직접 파일` (Direct File / DAM) | Sử dụng **hàm băm (Hashing function)** để tính toán trực tiếp địa chỉ vật lý của bản ghi từ giá trị khóa. | - Ưu điểm: Tốc độ truy xuất nhanh nhất. ; - Nhược điểm: Có thể xảy ra hiện tượng đụng độ (Collision); khó truy xuất theo khoảng. |

- **2. Ba vùng lưu trữ của Tệp ISAM (색인 순차 파일의 3대 구역):**
  1. **기본 구역 (Prime Area):** Vùng lưu trữ các bản ghi dữ liệu thực tế được sắp xếp tuần tự theo thứ tự khóa.
  2. **색인 구역 (Index Area):** Vùng lưu các bảng chỉ mục phân cấp hỗ trợ tìm kiếm nhanh, gồm 3 cấp:
     - `Track Index` (Chỉ mục rãnh) $\rightarrow$ `Cylinder Index` (Chỉ mục hình trụ) $\rightarrow$ `Master Index` (Chỉ mục chính).
  3. **오버플로 구역 (Overflow Area):** Vùng lưu tạm các bản ghi mới được chèn vào khi Prime Area đã bị lấp đầy, gồm:
     - `Cylinder Overflow Area` (Vùng tràn hình trụ) và `Independent Overflow Area` (Vùng tràn độc lập).
- **3. Các mô hình Cấu trúc Thư mục (디렉터리 구조):**
  - **1단계 디렉터리 (Thư mục 1 cấp):** Tất cả tệp nằm chung trong 1 thư mục duy nhất; tên tệp không được trùng; không có thư mục con.
  - **2단계 디렉터리 (Thư mục 2 cấp):** Thư mục chính MFD (Master File Directory) quản lý các thư mục người dùng UFD (User File Directory).
  - **트리 디렉터리 (Thư mục dạng cây):** Phổ biến nhất trong các hệ điều hành hiện đại (Windows, Linux, macOS). Gồm thư mục gốc (Root), các thư mục con và tệp; định danh tệp thông qua đường dẫn tuyệt đối hoặc tương đối.
  - **비순환 그래프 디렉터리 (Thư mục đồ thị không chu trình / Acyclic Graph):** Mở rộng cấu trúc cây cho phép các nhánh thư mục khác nhau có thể **chia sẻ chung tệp tin hoặc thư mục con** (thông qua liên kết cứng/mềm), loại bỏ nguy cơ lặp vô hạn nhờ cấu trúc không chu trình.
- **4. Các kỹ thuật Kiểm soát an toàn tệp:**
  - **접근 제어 행렬 (Access Control Matrix):** Ma trận 2 chiều với Hàng là Người dùng (Subject) và Cột là Tài nguyên/Tệp (Object).
  - **접근 제어 리스트 (ACL - Access Control List):** Bảng phân quyền được gắn trực tiếp vào **đối tượng tệp tin** (Ví dụ: Tệp A cho phép User1 đọc, User2 sửa).
  - **권한 리스트 (Capability List):** Danh sách quyền hạn được gắn trực tiếp vào **người dùng** (Ví dụ: User1 có quyền truy cập tệp A, tệp B).
- **주의/함정 (Bẫy đề thi trắc nghiệm):**
  - Đề hỏi: *"Vùng lưu trữ các bản ghi bị tràn khi Prime Area bị đầy trong ISAM là gì?"* $\rightarrow$ Đáp án: **오버플로 구역 (Overflow Area)**.
  - Đề hỏi: *"Cấu trúc thư mục nào cho phép chia sẻ tệp mà không tạo thành chu trình lặp?"* $\rightarrow$ Đáp án: **비순환 그래프 디렉터리 (Acyclic Graph Directory)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **So sánh giữa ACL và Capability List:**
  - `ACL (접근 제어 리스트)`: Giống như danh sách khách mời dán trước cửa phòng tiệc (tệp tin). Muốn vào phòng, nhân viên an ninh nhìn vào danh sách dán trên cửa xem có tên bạn không.
  - `Capability List (권한 리스트)`: Giống như vé mời cầm trên tay người dùng. Bạn cầm vé mời đi đến cửa nào có ghi trên vé thì được phép vào cửa đó.

### 복습 체크리스트
- [ ] Phân biệt được 3 cấu trúc tệp: 순차 파일 (SAM), 색인 순차 파일 (ISAM), 직접 파일 (DAM).
- [ ] Kể tên 3 vùng của ISAM: 기본 구역 (Prime), 색인 구역 (Index), 오버플로 구역 (Overflow).
- [ ] Nhớ đặc điểm của 비순환 그래프 디렉터리 (cho phép chia sẻ tệp/thư mục).
- [ ] Phân biệt được ACL (gắn vào tệp) và Capability List (gắn vào người dùng).
