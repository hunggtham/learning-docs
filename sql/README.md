# Cẩm nang Chinh phục SQLD & Quản trị Cơ sở Dữ liệu (K-Data SQL Developer Master Hub)

Chào mừng bạn đến với **Cổng giáo trình và ôn luyện chứng chỉ SQLD chuẩn hóa** (`sql/`). Giáo trình được biên soạn bám sát 100% khung chương trình cải cách mới nhất của Cơ quan Xúc tiến Công nghiệp Dữ liệu Hàn Quốc (K-Data - 한국데이터산업진흥원), bao quát toàn bộ kiến thức mô hình hóa dữ liệu quan hệ, kỹ thuật viết câu lệnh truy vấn SQL từ cơ bản đến chuyên sâu, và hệ thống cạm bẫy thực chiến phòng thi.

---

## 1. Cấu trúc Khảo thí & Tiêu chuẩn Đỗ (K-Data SQLD Standard)

Kỳ thi SQLD được tổ chức dưới hình thức trắc nghiệm tập trung, gồm 50 câu hỏi tính điểm trực tiếp.

| Môn thi | Tên môn học | Số câu hỏi | Điểm số | Điều kiện tránh điểm liệt (과락) |
| :--- | :--- | :--- | :--- | :--- |
| **Môn 1** | 데이터 모델링의 이해 (Hiểu biết về Mô hình hóa Dữ liệu) | 10 câu | 20 điểm | Tối thiểu 4 câu đúng ($\ge 8$ điểm / 40%) |
| **Môn 2** | SQL 기본 및 활용 (SQL Cơ bản & Ứng dụng Thực chiến) | 40 câu | 80 điểm | Tối thiểu 16 câu đúng ($\ge 32$ điểm / 40%) |
| **Tổng cộng** | **Toàn bộ kỳ thi SQLD** | **50 câu** | **100 điểm** | **Tổng điểm $\ge 60$ điểm và không dính điểm liệt** |

- **Thời gian làm bài:** 90 phút.
- **Tiêu chuẩn hoàn thành:** Điểm tổng $\ge 60/100$, đồng thời cả 2 môn đều phải đạt từ 40% điểm trở lên.

> [!WARNING] Cạm bẫy điểm liệt Môn 1 (과락 기준):
> Môn 1 chỉ có 10 câu hỏi (20 điểm), rất nhiều thí sinh chủ quan chỉ tập trung luyện viết SQL (Môn 2) mà làm sai 7 câu ở Môn 1 (chỉ được 6 điểm), dẫn tới việc **trượt ngay lập tức vì điểm liệt** dù Môn 2 đạt điểm tuyệt đối 80/80!

---

## 2. Bản đồ 2 Môn học & Danh mục Bài giảng Chi tiết

Hệ thống bài học được chia thành 2 thư mục tương ứng với 2 môn thi chính thức:

```text
sql/output/
├── mon-1-mo-hinh-du-lieu/          (4 chuyên đề nền tảng mô hình hóa, ERD, chuẩn hóa 1NF-BCNF)
└── mon-2-sql-co-ban-va-ung-dung/   (15 chuyên đề truy vấn, JOIN, Window Functions, Phân cấp, Tối ưu)
```

### [Môn 1: Mô hình hóa Dữ liệu (데이터 모델링의 이해)](output/mon-1-mo-hinh-du-lieu/README.md)

1. [Nền tảng Mô hình hóa Dữ liệu](output/mon-1-mo-hinh-du-lieu/01-nen-tang-mo-hinh-du-lieu.md): Định nghĩa mô hình dữ liệu, 3 góc nhìn (Khái niệm, Logic, Vật lý), 3 mức kiến trúc ANSI-SPARC (External, Conceptual, Internal Schema), tính độc lập logic và vật lý của dữ liệu.
2. [ERD, Entity, Attribute, Relationship và Identifier](output/mon-1-mo-hinh-du-lieu/02-erd-entity-attribute-relationship-identifier.md): Phương pháp vẽ ERD (Ký hiệu Barker vs Information Engineering), phân loại Thực thể (Cơ bản, Trung tâm, Hoạt động), Thuộc tính (Đơn, Đa trị, Dẫn xuất) và Định danh (Chính, Thay thế, Nhân tạo).
3. [Mô hình Dữ liệu Hướng Hiệu năng & Chuẩn hóa](output/mon-1-mo-hinh-du-lieu/03-mo-hinh-du-lieu-huong-hieu-nang-va-chuan-hoa.md): Nguyên lý chuẩn hóa từ 1NF (nguyên tử hóa), 2NF (khử phụ thuộc hàm một phần), 3NF (khử phụ thuộc hàm bắc cầu) đến BCNF (mọi định thức đều là khóa ứng viên); kỹ thuật phản chuẩn hóa (Denormalization) khi cần tối ưu I/O.
4. [Quan hệ, Transaction, Ràng buộc NULL và Identifier](output/mon-1-mo-hinh-du-lieu/04-quan-he-transaction-null-va-identifier.md): Quan hệ xác định (Identifying Relationship - nét liền) vs Quan hệ không xác định (Non-identifying Relationship - nét đứt); ý nghĩa logic của thuộc tính cho phép NULL; tính toàn vẹn Transaction.

### [Môn 2: SQL Cơ bản & Ứng dụng (SQL 기본 및 활용)](output/mon-2-sql-co-ban-va-ung-dung/README.md)

1. [SELECT, Hàm Đơn dòng & Bộ lọc Điều kiện](output/mon-2-sql-co-ban-va-ung-dung/00-sql-select-ham-va-loc.md): Cú pháp chuẩn SELECT, WHERE, ORDER BY, xử lý giá trị NULL với NVL/NVL2/COALESCE/ISNULL, hàm số học, ngày tháng và chuỗi.
2. [Kỹ thuật Nối bảng (JOIN)](output/mon-2-sql-co-ban-va-ung-dung/01-join.md): Nguyên lý hoạt động của NL Join (Nested Loop), Sort Merge Join và Hash Join; chuẩn cú pháp ANSI JOIN (INNER, LEFT/RIGHT/FULL OUTER, CROSS, NATURAL JOIN).
3. [Truy vấn Con (Subquery)](output/mon-2-sql-co-ban-va-ung-dung/02-subquery.md): Subquery đơn dòng (Scalar Subquery), Subquery tương quan (Correlated Subquery), Inline View trong mệnh đề FROM, toán tử kiểm tra EXISTS và NOT EXISTS.
4. [Toán tử Tập hợp (Set Operators)](output/mon-2-sql-co-ban-va-ung-dung/03-set-operators.md): Phép hội và khử trùng UNION vs UNION ALL, giao INTERSECT, hiệu MINUS (Oracle) vs EXCEPT (SQL Server).
5. [Hàm Nhóm & Gom cụm Đa chiều (Group Functions)](output/mon-2-sql-co-ban-va-ung-dung/04-group-functions.md): ROLLUP (tính tổng thứ cấp phân cấp), CUBE (tính tổng mọi tổ hợp), GROUPING SETS (chỉ định tổ hợp cụ thể), hàm nhận diện chỉ số `GROUPING()`.
6. [Hàm Cửa sổ (Window Functions)](output/mon-2-sql-co-ban-va-ung-dung/05-window-functions.md): Xếp hạng (RANK, DENSE_RANK, ROW_NUMBER), tham chiếu dòng lân cận (LEAD, LAG), tích lũy SUM/AVG OVER, định nghĩa phạm vi cửa sổ ROWS vs RANGE.
7. [TOP-N & Phân trang (Pagination)](output/mon-2-sql-co-ban-va-ung-dung/06-top-n-va-pagination.md): ROWNUM trong Oracle, chuẩn mới `OFFSET ... FETCH FIRST ... ROWS ONLY`, mệnh đề TOP trong SQL Server.
8. [Truy vấn Phân cấp (Hierarchical Query)](output/mon-2-sql-co-ban-va-ung-dung/07-hierarchical-query.md): Cú pháp `START WITH ... CONNECT BY PRIOR`, giả cột `LEVEL`, hàm `SYS_CONNECT_BY_PATH`, điều kiện `ORDER SIBLINGS BY`.
9. [DML & Xử lý Dữ liệu](output/mon-2-sql-co-ban-va-ung-dung/08-dml-va-toan-tu.md): Thao tác INSERT, UPDATE, DELETE, MERGE (Upsert dữ liệu), toán tử so sánh logic, LIKE với ký tự đại diện `%` và `_`.
10. [TCL & Quản lý Giao dịch (Transaction)](output/mon-2-sql-co-ban-va-ung-dung/09-tcl-va-transaction.md): Cơ chế COMMIT, ROLLBACK, SAVEPOINT, tính chất ACID và mức độ cô lập (Isolation Levels).
11. [DDL & Định nghĩa Bảng](output/mon-2-sql-co-ban-va-ung-dung/10-ddl-va-dinh-nghia-bang.md): Lệnh CREATE TABLE, ALTER TABLE (ADD, MODIFY, DROP COLUMN), TRUNCATE TABLE vs DELETE TABLE.
12. [Ràng buộc Toàn vẹn & Khung nhìn (View)](output/mon-2-sql-co-ban-va-ung-dung/11-constraints-view-va-doi-tuong.md): Ràng buộc PRIMARY KEY, FOREIGN KEY (CASCADE, RESTRICT, SET NULL), UNIQUE, CHECK, NOT NULL; cơ chế View độc lập.
13. [DCL, Quản lý Quyền & Vai trò (Role)](output/mon-2-sql-co-ban-va-ung-dung/12-dcl-quyen-va-role.md): Lệnh GRANT, REVOKE, phân quyền hệ thống (System Privilege) vs phân quyền đối tượng (Object Privilege).
14. [Chuyển đổi Ma trận (PIVOT/UNPIVOT) & Biểu thức Chính quy](output/mon-2-sql-co-ban-va-ung-dung/13-pivot-unpivot-va-regexp.md): Chuyển dòng thành cột (PIVOT) và ngược lại; hàm tìm kiếm chuỗi REGEXP_LIKE, REGEXP_SUBSTR.
15. [Quy chuẩn Viết SQL & Tối ưu Pipeline AI](output/mon-2-sql-co-ban-va-ung-dung/14-sql-style-guide.md): Cẩm nang định dạng mã SQL sạch, nhất quán, hỗ trợ phân tích hiệu năng và AI Assistant.

---

## 3. Ma trận Khác biệt Cốt lõi: Oracle vs SQL Server

Đề thi SQLD thường xuyên cài cắm các câu hỏi so sánh hành vi giữa hai hệ quản trị cơ sở dữ liệu phổ biến nhất:

| Tính năng / Hành vi | Oracle Database | Microsoft SQL Server | Ý nghĩa thực chiến phòng thi |
| :--- | :--- | :--- | :--- |
| **Chuỗi rỗng (`''`)** | Được coi tương đương giá trị `NULL` | Coi là chuỗi có độ dài bằng 0 (`LENGTH('') = 0`) | `WHERE col = ''` trong Oracle luôn trả về rỗng vì `col = NULL` là UNKNOWN |
| **Phép ghép chuỗi** | Sử dụng toán tử `\|\|` hoặc hàm `CONCAT()` | Sử dụng toán tử `+` hoặc hàm `CONCAT()` | `SELECT 'A' \|\| 'B'` hợp lệ trên Oracle, báo lỗi trên SQL Server |
| **Xử lý NULL khi ghép chuỗi** | `'A' \|\| NULL` trả về kết quả `'A'` | `'A' + NULL` trả về kết quả `NULL` | Cực kỳ phổ biến trong các câu trắc nghiệm kết quả biểu thức |
| **Toán tử Tập hợp Trừ** | Sử dụng từ khóa `MINUS` | Sử dụng từ khóa `EXCEPT` | Dùng sai từ khóa giữa hai hệ CSDL sẽ bị trừ điểm |
| **Thứ tự NULL khi ORDER BY** | Mặc định xếp ở **cuối cùng** (lớn nhất) khi ASC | Mặc định xếp ở **đầu tiên** (nhỏ nhất) khi ASC | Kết quả hiển thị của TOP-N bị đảo lộn nếu không chú ý |
| **Tự động Commit DDL** | DDL (CREATE, DROP, TRUNCATE) tự động ngầm commit | DDL có thể nằm trong Transaction và ROLLBACK được | `ROLLBACK` trong Oracle không thể hoàn tác câu lệnh `CREATE TABLE` vừa chạy |

---

## 4. Chiến lược Ôn luyện & Tránh bẫy Phòng thi

1. **Quy tắc số học với NULL:**
   - Bất kỳ phép toán số học nào với `NULL` đều cho kết quả là `NULL` (`10 + NULL = NULL`).
   - Phép so sánh với `NULL` (`= NULL`, `<> NULL`) luôn trả về giá trị logic `UNKNOWN`, không bao giờ là `TRUE`. Muốn kiểm tra bắt buộc phải dùng `IS NULL` hoặc `IS NOT NULL`.
   - Các hàm nhóm (`COUNT(col)`, `SUM(col)`, `AVG(col)`) tự động loại trừ các dòng có giá trị `NULL`. Ngoại lệ duy nhất: `COUNT(*)` đếm toàn bộ số dòng dữ liệu kể cả dòng toàn `NULL`.
2. **Thứ tự thực thi logic của câu lệnh SQL:**
   - Thứ tự viết: `SELECT -> FROM -> WHERE -> GROUP BY -> HAVING -> ORDER BY`.
   - **Thứ tự thực thi thực tế của Database:**
     $$\text{FROM} \longrightarrow \text{ON / WHERE} \longrightarrow \text{GROUP BY} \longrightarrow \text{HAVING} \longrightarrow \text{SELECT} \longrightarrow \text{ORDER BY}$$
   - *Hệ quả:* Không thể dùng bí danh (Alias) được đặt trong mệnh đề `SELECT` ở mệnh đề `WHERE` hoặc `GROUP BY`, nhưng hoàn toàn có thể dùng ở mệnh đề `ORDER BY`.

---

## 5. Điều hướng Liên kết Hệ thống

- [Quay về Cổng Chứng chỉ Chuyên môn Quốc gia](../cert/README.md)
- [Thư mục Bài giảng Môn 1: Mô hình hóa Dữ liệu](output/mon-1-mo-hinh-du-lieu/README.md)
- [Thư mục Bài giảng Môn 2: SQL Cơ bản & Ứng dụng](output/mon-2-sql-co-ban-va-ung-dung/README.md)
