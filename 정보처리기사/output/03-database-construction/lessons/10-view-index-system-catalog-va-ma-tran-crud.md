# 뷰, 인덱스, 시스템 카탈로그와 CRUD 매트릭스 (View, Index, System Catalog và Ma Trận CRUD)

## 학습 목표
- Nắm vững bản chất bảng ảo (`가상 테이블`), ưu điểm bảo mật và độc lập logic (`논리적 독립성`), cùng các giới hạn thi cử của Khung nhìn (View): không có chỉ mục độc lập, không có lệnh `ALTER VIEW`, hạn chế thao tác DML.
- Phân tích sâu 5 cấu trúc Chỉ mục (Index): B+Tree, Bitmap Index (cho cột có độ phân biệt thấp), Function-Based Index, Bitmap Join Index, Domain Index; phân biệt Clustered Index vs Non-Clustered Index.
- Nắm vững quy tắc quản trị Từ điển dữ liệu (`시스템 카탈로그 / 데이터 사전`): DBMS tự động cập nhật khi chạy DDL, người dùng chỉ được dùng lệnh `SELECT` để tra cứu, cấm tuyệt đối can thiệp DML trực tiếp.
- Ánh xạ 4 thao tác C-R-U-D với câu lệnh SQL tương ứng, ứng dụng đo lường tần suất giao dịch và ước tính dung lượng dữ liệu, cùng 3 quy tắc kiểm định chất lượng ma trận CRUD.

## 핵심 키워드
- 뷰 (Khung nhìn / View / 가상 테이블 / 논리적 독립성 / ALTER VIEW 불가)
- 인덱스 (Chỉ mục / Index / B+ Tree / Bitmap Index / Clustered vs Non-Clustered)
- 시스템 카탈로그 (Từ điển dữ liệu / System Catalog / 메타데이터 / SELECT만 허용)
- CRUD 매트릭스 (Ma trận CRUD / Create, Read, Update, Delete / 트랜잭션 부하 분석 / 용량 산정)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [09-ngon-ngu-sql-ddl-dml-dcl-va-procedural-sql.md](09-ngon-ngu-sql-ddl-dml-dcl-va-procedural-sql.md), chúng ta đã làm chủ cú pháp DDL, DML, DCL, TCL và cơ chế thực thi của các khối lệnh SQL thủ tục.
- **Đang giải quyết gì (Current Problem):** Bài học này giải quyết việc xây dựng các khung nhìn logic ảo (View), thiết kế cấu trúc chỉ mục vật lý (Index) để tối ưu tốc độ đọc, đồng thời khai thác siêu dữ liệu hệ thống (Catalog) và lập ma trận CRUD để đo tải giao dịch, rà soát khiếm khuyết thiết kế.
- **Dùng đi đâu (Forward Handoff):** Các phân tích về tải CRUD và cấu trúc chỉ mục này sẽ làm cơ sở trực tiếp để thiết kế kiến trúc phân tán, tính trong suốt (Transparency) và phân mảnh dữ liệu trên mạng ở bài học tiếp theo [11-co-so-du-lieu-phan-tan-va-tinh-trong-suot.md](11-co-so-du-lieu-phan-tan-va-tinh-trong-suot.md).

## 읽는 방법
- Đọc TẦNG A để ghi nhớ chuẩn xác các bẫy đề thi: View không có Index riêng, không có lệnh ALTER VIEW, người dùng chỉ được SELECT trên Catalog, và quy tắc bảng bắt buộc phải có ít nhất một chữ C và chữ R trong ma trận CRUD.
- Đọc TẦNG B để nắm chắc cơ chế vật lý của B+ Tree, so sánh chi tiết Clustered Index (sắp xếp vật lý) vs Non-Clustered Index (con trỏ ROWID), và công thức tính dung lượng trong CRUD.

---

## 뷰, 인덱스, 시스템 카탈로그와 CRUD 매트릭스

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng tóm lược đặc tính và giới hạn của View (가상 테이블)
| Tiêu chí | Nội dung chi tiết | Điểm lưu ý thi cử |
| :--- | :--- | :--- |
| **Bản chất** | Bảng ảo (`가상 테이블`) sinh ra từ câu lệnh SELECT, không lưu dữ liệu thật trên đĩa | Chỉ lưu câu lệnh định nghĩa trong System Catalog |
| **Ưu điểm** | Độc lập dữ liệu logic (`논리적 독립성`), bảo mật dữ liệu, đơn giản hóa câu lệnh truy vấn phức tạp | Bảo vệ ứng dụng khi cấu trúc bảng cơ sở thay đổi |
| **Giới hạn 1** | **Không thể tạo chỉ mục độc lập** (`독립적인 인덱스를 가질 수 없음`) | Không có cấu trúc Index vật lý riêng |
| **Giới hạn 2** | **Không có câu lệnh ALTER VIEW** | Muốn sửa phải `DROP VIEW` rồi `CREATE VIEW` lại |
| **Giới hạn 3** | Cấm DML (INSERT/UPDATE/DELETE) nếu View chứa `GROUP BY`, `DISTINCT`, hàm tập hợp hoặc `JOIN` phức tạp | Không thể ánh xạ ngược về từng dòng bảng gốc |

#### 2. Bảng phân biệt 5 cấu trúc Chỉ mục (Index)
| Loại Index | Tên tiếng Hàn & Anh | Đặc trưng cấu trúc | Trường hợp ứng dụng tối ưu |
| :--- | :--- | :--- | :--- |
| **B+ Tree Index** | `B+ 트리 인덱스` | Gồm Root, Branch và Leaf; các nút lá liên kết danh sách đôi | **Chuẩn mực phổ biến nhất**, tối ưu tìm kiếm theo dải (`BETWEEN`, `<`, `>`) |
| **Bitmap Index** | `비트맵 인덱스` | Lưu bằng chuỗi bit 0 và 1, tính toán bằng phép toán bit AND/OR siêu tốc | Cột có **độ phân biệt thấp (ít giá trị khác biệt)** như Giới tính, Tình trạng |
| **Function-Based** | `함수 기반 인덱스` | Đánh chỉ mục trên kết quả của biểu thức hoặc hàm (ví dụ: `UPPER(email)`) | Truy vấn thường xuyên chứa biểu thức biến đổi trong mệnh đề WHERE |
| **Bitmap Join** | `비트맵 조인 인덱스` | Đánh chỉ mục bitmap trên kết quả join sẵn của nhiều bảng | Môi trường Data Warehouse với lược đồ hình sao (Star Schema) |
| **Domain Index** | `도메인 인덱스` | Chỉ mục do lập trình viên tự định nghĩa cho kiểu dữ liệu chuyên biệt | Dữ liệu không gian địa lý GIS, văn bản toàn văn, đa phương tiện |

#### 3. Đối chiếu Clustered Index vs Non-Clustered Index
| Tiêu chí | Clustered Index (`클러스터드 인덱스`) | Non-Clustered Index (`넌클러스터드 인덱스`) |
| :--- | :--- | :--- |
| **Sắp xếp vật lý** | Dữ liệu trên đĩa được sắp xếp trực tiếp theo khóa | Dữ liệu nằm độc lập trong Heap, không sắp xếp theo khóa |
| **Nút lá (Leaf Node)** | **Chính là trang dữ liệu thực** | Chỉ chứa **con trỏ (ROWID)** trỏ tới trang dữ liệu |
| **Số lượng trên 1 bảng** | **Duy nhất 1 chỉ mục** | **Nhiều chỉ mục** phụ trợ |
| **Tốc độ truy xuất** | Cực nhanh cho truy vấn theo khoảng | Nhanh cho tìm kiếm giá trị đơn lẻ |

#### 4. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Chỉ mục trên View:** View thông thường **hoàn toàn không thể tạo chỉ mục độc lập** (`독립 인덱스 생성 불가`).
- **Bẫy 2: Sửa đổi View:** Chuẩn SQL **không có lệnh `ALTER VIEW`**; muốn thay đổi bắt buộc phải xóa bằng `DROP VIEW` và tạo lại.
- **Bẫy 3: Quyền hạn trên System Catalog:** Người dùng và DBA **chỉ được phép dùng lệnh `SELECT` để tra cứu**; DBMS tự động duy trì cập nhật khi chạy DDL, nghiêm cấm dùng INSERT/UPDATE/DELETE can thiệp trực tiếp.
- **Bẫy 4: Bảng thiếu chữ C hoặc R trong Ma trận CRUD:** Bảng không có chữ `R` là bảng chết (dữ liệu lưu nhưng không ai dùng); bảng không có chữ `C` là bảng lỗi (dữ liệu không biết sinh ra từ đâu).

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Bản chất và cơ chế hoạt động của View
- Sơ đồ tương tác của View:
  ```
  [ Bảng cơ sở A ] ───┐
                      ├──> [ Lệnh SELECT định nghĩa View ] ──> [ View (Bảng ảo) ] ──> [ Ứng dụng tra cứu ]
  [ Bảng cơ sở B ] ───┘
  ```
- **Lợi ích an ninh:** Có thể che giấu các cột nhạy cảm (như Mức lương, Số CMND) bằng cách chỉ `SELECT` các cột công khai vào View và cấp quyền truy cập View đó cho nhân viên.

#### 2. Nguyên tắc thiết kế chỉ mục và quy luật đánh đổi
- **Chi phí tái lập chỉ mục:** Mỗi khi thực thi lệnh `INSERT`, `UPDATE` hoặc `DELETE`, toàn bộ các cây chỉ mục liên quan đều phải được sắp xếp lại hoặc chia tách nút (Page Split).
- **Quy tắc vàng:**
  - Bảng có tần suất **INSERT/DELETE liên tục** thì phải giảm tối đa số lượng chỉ mục để tránh làm tụt hiệu năng ghi.
  - Chỉ nên tạo chỉ mục trên các cột thường xuyên xuất hiện trong mệnh đề `WHERE`, `JOIN`, hoặc `ORDER BY`.

#### 3. Hệ thống ca-ta-lô và Siêu dữ liệu (System Catalog & Metadata)
- Sơ đồ quản trị ca-ta-lô:
  ```
  [ Thực thi DDL ] ───> [ DBMS Engine ] ──(Tự động cập nhật)──> [ System Catalog (Data Dictionary) ]
                             │
  [ Người dùng / DBA ] ──────┴──(Chỉ được phép SELECT)────────> [ Tra cứu Metadata ]
  ```
- **Nội dung lưu trữ:** Định nghĩa bảng, cột, kiểu dữ liệu, các ràng buộc toàn vẹn, chỉ mục, khung nhìn, người dùng, quyền hạn, số liệu thống kê tối ưu hóa.

#### 4. Phân tích ma trận CRUD (CRUD Matrix Analysis)
- **Ánh xạ 4 thao tác cơ bản:**
  - `C (Create)`: Ứng với lệnh `INSERT` trong SQL - Tạo mới bản ghi.
  - `R (Read)`: Ứng với lệnh `SELECT` trong SQL - Đọc và truy vấn bản ghi.
  - `U (Update)`: Ứng với lệnh `UPDATE` trong SQL - Sửa đổi giá trị bản ghi.
  - `D (Delete)`: Ứng với lệnh `DELETE` trong SQL - Xóa bản ghi.
- **Ứng dụng tính toán tải hệ thống:**
  - **Đo lường tần suất:** Tổng hợp số lần mỗi tiến trình nghiệp vụ gọi đến bảng trong một khoảng thời gian (giờ cao điểm) để xác định điểm nóng tài nguyên.
  - **Dự báo dung lượng:** Lấy số lượt Create nhân với kích thước trung bình của một bản ghi để dự đoán tốc độ tăng trưởng dung lượng đĩa cứng cần cấp phát.
- **Quy tắc kiểm tra chất lượng (CRUD Matrix Validation):**
  - Mỗi hàng (Process) phải chứa ít nhất một thao tác C, R, U hoặc D.
  - Mỗi cột (Table/Entity) bắt buộc phải có ít nhất một thao tác `C` và một thao tác `R`.
  - Khi một tiến trình thực hiện nhiều thao tác trên một bảng, ký hiệu theo thứ tự ưu tiên: `C > D > U > R`.

---

### 복습 체크리스트
- [ ] Phân tích được 3 ưu điểm cốt lõi của View (độc lập logic, bảo mật, đơn giản hóa truy vấn) và 3 giới hạn kinh điển.
- [ ] Nhớ rõ View không có cấu trúc Index độc lập và không có lệnh ALTER VIEW.
- [ ] So sánh 5 loại Index: B+ Tree (phổ biến nhất), Bitmap (độ phân biệt thấp), Function-Based, Bitmap Join, Domain.
- [ ] Phân biệt sự khác nhau căn bản giữa Clustered Index (dữ liệu thật ở lá, duy nhất 1) và Non-Clustered Index (dùng con trỏ ROWID).
- [ ] Trình bày đặc điểm của System Catalog: DBMS tự động duy trì khi chạy DDL, người dùng chỉ được dùng lệnh SELECT.
- [ ] Nắm vững 4 chữ cái CRUD, ánh xạ câu lệnh SQL và 2 quy tắc kiểm định ma trận bắt buộc.
