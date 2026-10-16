# 뷰, 인덱스, 시스템 카탈로그와 CRUD 매트릭스 (View, Index, System Catalog và Ma Trận CRUD)

## 학습 목표 (Mục tiêu)
- Nắm vững bản chất bảng ảo (`가상 테이블`), ưu điểm bảo mật và độc lập logic (`논리적 독립성`), cùng các giới hạn thi cử của Khung nhìn (View): không có chỉ mục độc lập, không có lệnh `ALTER VIEW`, các điều kiện nghiêm ngặt hạn chế thao tác DML (INSERT, UPDATE, DELETE).
- Phân tích sâu các cấu trúc Chỉ mục (Index): Cây B-Tree / B+Tree, Chỉ mục Bitmap (cho cột có độ phân biệt thấp); đối chiếu toàn diện Clustered Index vs Non-Clustered Index.
- Nắm vững quy tắc quản trị Từ điển dữ liệu (`시스템 카탈로그` / `데이터 사전` / Data Dictionary): DBMS tự động cập nhật khi chạy DDL, người dùng chỉ được dùng lệnh `SELECT` để tra cứu, cấm tuyệt đối can thiệp DML trực tiếp.
- Ánh xạ 4 thao tác C-R-U-D với câu lệnh SQL tương ứng, ứng dụng đo lường tần suất giao dịch và ước tính dung lượng dữ liệu, cùng các quy tắc kiểm định chất lượng ma trận CRUD.

## 핵심 키워드 (Từ khóa)
- 뷰 (Khung nhìn / View / 가상 테이블 / 논리적 독립성 / DML 제한)
- 인덱스 (Chỉ mục / Index / B-Tree / B+ Tree / 비트맵 인덱스 Bitmap)
- 클러스터드 인덱스 vs 넌클러스터드 인덱스 (Clustered Index vs Non-Clustered Index)
- 시스템 카탈로그 (Từ điển dữ liệu / System Catalog / Data Dictionary / 메타데이터 / SELECT 전용)
- CRUD 매트릭스 (Ma trận CRUD / Create, Read, Update, Delete / 유효성 검증 규칙)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [09-ngon-ngu-sql-ddl-dml-dcl-va-procedural-sql.md](09-ngon-ngu-sql-ddl-dml-dcl-va-procedural-sql.md), chúng ta đã làm chủ cú pháp DDL, DML, DCL, TCL và cơ chế thực thi của các khối lệnh SQL thủ tục.
- **Đang giải quyết gì (Current Problem):** Bài học này giải quyết việc xây dựng các khung nhìn logic ảo (View), thiết kế cấu trúc chỉ mục vật lý (Index) để tối ưu tốc độ đọc, đồng thời khai thác siêu dữ liệu hệ thống (System Catalog) và lập ma trận CRUD để đo tải giao dịch, rà soát khiếm khuyết thiết kế.
- **Dùng đi đâu (Forward Handoff):** Các phân tích về tải CRUD và cấu trúc chỉ mục này sẽ làm cơ sở trực tiếp để thiết kế kiến trúc phân tán, tính trong suốt (Transparency) và phân mảnh dữ liệu trên mạng ở bài học tiếp theo [11-co-so-du-lieu-phan-tan-va-tinh-trong-suot.md](11-co-so-du-lieu-phan-tan-va-tinh-trong-suot.md).

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để ghi nhớ chuẩn xác các bẫy đề thi: View không có Index riêng, không có lệnh ALTER VIEW, người dùng chỉ được SELECT trên Catalog, các trường hợp View cấm DML, và quy tắc bắt buộc phải có chữ C và chữ R trong ma trận CRUD.
- Đọc TẦNG B để nắm chắc cơ chế vật lý của B-Tree, so sánh chi tiết Clustered Index (sắp xếp vật lý) vs Non-Clustered Index (con trỏ ROWID), và nguyên tắc xây dựng ma trận CRUD.

---

## 뷰, 인덱스, 시스템 카탈로그와 CRUD 매트릭스

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng tóm lược đặc tính và giới hạn của View (가상 테이블)

| Tiêu chí | Nội dung chi tiết | Điểm lưu ý thi cử |
| :--- | :--- | :--- |
| **Bản chất** | Bảng ảo (`가상 테이블`) sinh ra từ câu lệnh SELECT, không lưu dữ liệu thật trên đĩa | Chỉ lưu câu lệnh định nghĩa trong System Catalog |
| **Ưu điểm** | Độc lập dữ liệu logic (`논리적 독립성`), bảo mật dữ liệu, đơn giản hóa câu lệnh truy vấn phức tạp | Che giấu các cột nhạy cảm, bảo vệ ứng dụng khi bảng cơ sở đổi cấu trúc |
| **Giới hạn 1** | **Không thể tạo chỉ mục độc lập** (`독립적인 인덱스를 가질 수 없음`) | Không có cấu trúc Index vật lý riêng biệt cho View |
| **Giới hạn 2** | **Không có câu lệnh ALTER VIEW** | Muốn sửa định nghĩa bắt buộc phải `DROP VIEW` rồi `CREATE VIEW` lại |
| **Giới hạn 3** | **Hạn chế nghiêm ngặt thao tác DML (INSERT, UPDATE, DELETE)** | Cấm DML nếu View chứa `DISTINCT`, `GROUP BY`, `HAVING`, hàm gộp hoặc biểu thức tính toán |

#### 2. Đối chiếu Clustered Index vs Non-Clustered Index

| Tiêu chí so sánh | Clustered Index (`클러스터드 인덱스`) | Non-Clustered Index (`넌클러스터드 인덱스`) |
| :--- | :--- | :--- |
| **Sắp xếp vật lý** | **Dữ liệu thực tế trên đĩa được sắp xếp trực tiếp** theo thứ tự của khóa chỉ mục | Dữ liệu trên đĩa nằm độc lập (Heap structure), **không sắp xếp theo khóa** |
| **Nút lá (Leaf Node)** | **Chính là trang dữ liệu thực tế (Data Page)** | Chỉ chứa **con trỏ (ROWID)** trỏ tới trang dữ liệu thực |
| **Số lượng trên 1 bảng** | **DUY NHẤT 1 chỉ mục** trên mỗi bảng | **Có thể tạo NHIỀU chỉ mục** phụ trợ trên cùng một bảng |
| **Tốc độ truy vấn** | **Cực nhanh cho truy vấn theo dải/khoảng** (`BETWEEN`, `<`, `>`) | Rất nhanh cho tìm kiếm giá trị đơn lẻ chính xác (`=`) |
| **Chi phí thao tác ghi** | Chậm hơn, dễ phát sinh hiện tượng phân mảnh/tách trang (`Page Split`) | Nhanh hơn, chỉ cần cập nhật cây chỉ mục phụ và con trỏ |

#### 3. Bảng phân biệt các cấu trúc Chỉ mục (Index)

| Loại Index | Tên tiếng Hàn & Anh | Đặc trưng cấu trúc | Trường hợp ứng dụng tối ưu |
| :--- | :--- | :--- | :--- |
| **B-Tree / B+ Tree** | `B-트리 / B+ 트리 인덱스` | Cây cân bằng gồm Root, Branch và Leaf; B+ Tree liên kết hai chiều các nút lá | **Chuẩn mực phổ biến nhất**, tối ưu cả tìm kiếm chính xác và tìm kiếm theo khoảng |
| **Bitmap Index** | `비트맵 인덱스` | Lưu trữ bằng chuỗi bit 0 và 1, thực hiện phép toán bit AND/OR siêu tốc | Cột có **độ phân biệt thấp (ít giá trị khác biệt)** như Giới tính, Trạng thái |
| **Function-Based** | `함수 기반 인덱스` | Đánh chỉ mục trên kết quả của biểu thức hoặc hàm (ví dụ: `UPPER(email)`) | Mệnh đề WHERE thường xuyên chứa hàm xử lý dữ liệu |
| **Domain Index** | `도메인 인덱스` | Chỉ mục do người dùng/lập trình viên tự định nghĩa cho kiểu dữ liệu phức tạp | Dữ liệu không gian địa lý GIS, văn bản toàn văn, đa phương tiện |

#### 4. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)

- **Bẫy 1: Chỉ mục trên View:** View thông thường **hoàn toàn không thể tạo chỉ mục độc lập** (`독립 인덱스 생성 불가`).
- **Bẫy 2: Sửa đổi View:** Chuẩn SQL **không có lệnh `ALTER VIEW`**; muốn thay đổi bắt buộc phải xóa bằng `DROP VIEW` và tạo lại.
- **Bẫy 3: Quyền hạn trên System Catalog (Data Dictionary):**
  - Hệ quản trị CSDL (DBMS) **tự động duy trì và cập nhật** ca-ta-lô khi chạy các câu lệnh DDL.
  - Người dùng và DBA **CHỈ ĐƯỢC PHÉP DÙNG LỆNH `SELECT` ĐỂ TRA CỨU**, tuyệt đối cấm dùng INSERT, UPDATE, DELETE can thiệp trực tiếp vào ca-ta-lô.
- **Bẫy 4: Các điều kiện cấm DML trên View:**
  - View chứa `DISTINCT`, hàm tổng hợp (`SUM`, `COUNT`), mệnh đề `GROUP BY`, hoặc cột phái sinh thì **không thể thực hiện lệnh INSERT hay UPDATE**.
- **Bẫy 5: Quy tắc kiểm định Ma trận CRUD:**
  - Mỗi cột (Bảng/Thực thể) bắt buộc phải có ít nhất một thao tác `C` (Create) và một thao tác `R` (Read). Nếu thiếu `C` là dữ liệu không rõ nguồn gốc; nếu thiếu `R` là dữ liệu thừa không ai sử dụng.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Chi tiết cơ chế hoạt động và giới hạn DML của View

- **Bản chất kỹ thuật:** View là một câu lệnh `SELECT` được lưu trữ sẵn trong System Catalog. Khi người dùng truy vấn `SELECT * FROM v_emp`, DBMS sẽ trộn (merge) câu truy vấn của người dùng với câu truy vấn định nghĩa View thành một câu SQL hoàn chỉnh trên các bảng cơ sở.
- **Các trường hợp KHÔNG ĐƯỢC PHÉP thực hiện INSERT / UPDATE / DELETE trên View:**
  1. View được định nghĩa có chứa từ khóa `DISTINCT`.
  2. View có sử dụng các hàm gộp tổng hợp: `COUNT()`, `SUM()`, `AVG()`, `MAX()`, `MIN()`.
  3. View có mệnh đề `GROUP BY` hoặc `HAVING`.
  4. View sử dụng các toán tử tập hợp: `UNION`, `UNION ALL`, `INTERSECT`, `MINUS`.
  5. Cột cần cập nhật là cột biểu thức tính toán (ví dụ: `Luong * 1.1`).
  6. View kết hợp từ nhiều bảng (JOIN) mà không bảo toàn khóa chính (Non-key-preserved table).

#### 2. Cấu trúc cây chỉ mục B-Tree và B+Tree

- **B-Tree (Balanced Tree):** Cây cân bằng trong đó mọi nút lá đều nằm ở cùng một độ sâu. Dữ liệu và con trỏ khóa nằm ở cả nút gốc, nút trung gian và nút lá.
- **B+ Tree (Biến thể tối ưu cho CSDL):**
  - Các nút trung gian (Root, Branch) chỉ chứa khóa dẫn đường (Index Keys) và con trỏ phân nhánh.
  - **Toàn bộ dữ liệu thực tế hoặc con trỏ bản ghi đều dồn xuống các nút lá (Leaf Nodes)**.
  - Các nút lá được liên kết với nhau bằng danh sách liên kết đôi (Doubly Linked List), cho phép duyệt tuần tự toàn bộ dải dữ liệu một cách cực kỳ hiệu quả mà không cần quay lui lên cây.

#### 3. Hệ thống ca-ta-lô và Siêu dữ liệu (System Catalog & Metadata)

```text
[ Thực thi DDL (CREATE, ALTER, DROP) ]
                │
                ▼
      [ DBMS Engine ] ────(Tự động cập nhật ngầm)────> [ System Catalog (Data Dictionary) ]
                                                                   │
[ Người dùng / DBA ] ─────────(Chỉ được phép SELECT)───────────────┘
```

- **Metadata (메타데이터):** Là "dữ liệu mô tả về dữ liệu", bao gồm:
  + Tên bảng, tên cột, kiểu dữ liệu, độ dài thuộc tính.
  + Các ràng buộc toàn vẹn: Primary Key, Foreign Key, NOT NULL, CHECK, UNIQUE.
  + Danh sách khung nhìn (View), chỉ mục (Index), thủ tục (Stored Procedure), Trigger.
  + Tài khoản người dùng, phân quyền truy cập, nhật ký bảo mật.
  + Số liệu thống kê phục vụ bộ tối ưu hóa CBO (số block, số dòng, độ cao cây index).

#### 4. Phân tích ma trận CRUD (CRUD Matrix Analysis)

- **Cấu trúc ma trận:**
  - Hàng (Rows): Danh sách các quy trình nghiệp vụ (Business Processes).
  - Cột (Columns): Danh sách các thực thể hoặc bảng dữ liệu (Entities / Tables).
- **Thứ tự ưu tiên ký hiệu:** Khi một quy trình thực hiện nhiều thao tác trên cùng một bảng, ghi nhận theo thứ tự ưu tiên:
  $$\mathbf{C > D > U > R}$$
  *(Ví dụ: nếu tiến trình vừa đọc vừa sửa vừa xóa thì ký hiệu là `D`)*.
- **Quy tắc thẩm định chất lượng ma trận CRUD (CRUD Verification):**
  1. Mọi tiến trình (hàng) phải tương tác với ít nhất một bảng (chứa ít nhất một ký tự C, R, U, D).
  2. Mọi bảng (cột) bắt buộc phải có ít nhất một ký tự `C` (phải có tiến trình sinh ra dữ liệu) và ít nhất một ký tự `R` (phải có tiến trình sử dụng dữ liệu).

---

### 복습 체크리스트
- [ ] Phân tích được 3 ưu điểm cốt lõi của View (độc lập logic, bảo mật, đơn giản hóa truy vấn) và các trường hợp cấm DML.
- [ ] Nhớ rõ View không có cấu trúc Index độc lập và không có lệnh ALTER VIEW.
- [ ] Phân biệt sự khác nhau căn bản giữa Clustered Index (dữ liệu thật ở lá, duy nhất 1) và Non-Clustered Index (con trỏ ROWID, nhiều chỉ mục).
- [ ] Hiểu rõ ứng dụng của Bitmap Index cho các cột có độ phân biệt thấp (ít giá trị riêng biệt).
- [ ] Trình bày đặc điểm của System Catalog: DBMS tự động duy trì khi chạy DDL, người dùng chỉ được dùng lệnh SELECT.
- [ ] Nắm vững 4 chữ cái CRUD, ánh xạ câu lệnh SQL và 2 quy tắc kiểm định ma trận bắt buộc: mỗi cột phải có ít nhất chữ C và chữ R.
