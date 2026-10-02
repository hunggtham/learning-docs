# Môn 2 – SQL 기본 및 활용

> **Mạch đọc:** Đây là README owner của **Môn 2 – SQL 기본 및 활용**. Route đọc đi từ SELECT/filter → JOIN/subquery/aggregation → analytic/hierarchical queries → DML/TCL/DDL/DCL → style and portability, để kỹ thuật truy vấn nối với semantics và vận hành.

Nên học JOIN trước, sau đó đến Subquery/Group Function và các kỹ thuật truy vấn nâng cao; kết thúc bằng SQL Style Guide để áp dụng các quy ước vào model trong pipeline.

## Mạch bài giảng

Mỗi bài mở bằng mục đích và câu hỏi cần giải quyết, đi qua các section nguồn bằng câu nối, rồi chốt quan hệ giữa đầu vào, điều kiện xử lý và kết quả trước khi bàn giao sang bài kế tiếp.

> **Chuyển mạch:** Trong **Môn 2 – SQL 기본 및 활용**, **Danh sách bài học** tiếp nhận điểm tựa từ **Mạch bài giảng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Danh sách bài học

1. [SQL cơ bản: SELECT, hàm, lọc, nhóm và sắp xếp](00-sql-select-ham-va-loc.md) — SELECT, WHERE, hàm, GROUP BY/HAVING và ORDER BY.
2. [JOIN](01-join.md) — INNER/OUTER/CROSS/SELF JOIN, NATURAL/USING, ANSI join và các bẫy điều kiện.
3. [Subquery](02-subquery.md) — Single/multi-row, correlated, scalar, inline view, EXISTS và các bẫy thường gặp.
4. [Set Operators](03-set-operators.md) — UNION, UNION ALL, INTERSECT, MINUS/EXCEPT và các quy tắc kết hợp tập kết quả.
5. [Group Functions](04-group-functions.md) — Aggregate, GROUP BY, ROLLUP, CUBE, GROUPING và GROUPING SETS.
6. [Window Functions](05-window-functions.md) — OVER, PARTITION BY, window frame, ranking và các hàm phân tích.
7. [TOP-N và Pagination](06-top-n-va-pagination.md) — ROWNUM, ROW_NUMBER/RANK/DENSE_RANK, FETCH/OFFSET, TOP và WITH TIES.
8. [Hierarchical Query](07-hierarchical-query.md) — START WITH, CONNECT BY PRIOR, LEVEL, NOCYCLE và các pseudocolumn phân cấp.
9. [DML và toán tử](08-dml-va-toan-tu.md) — INSERT, UPDATE, DELETE, MERGE, SELECT, toán tử số học và nối chuỗi.
10. [TCL và Transaction](09-tcl-va-transaction.md) — ACID, COMMIT, ROLLBACK, SAVEPOINT và khác biệt Oracle/SQL Server.
11. [DDL và định nghĩa bảng](10-ddl-va-dinh-nghia-bang.md) — Kiểu dữ liệu, CREATE/CTAS/ALTER/DROP/TRUNCATE.
12. [Constraints, View và các đối tượng hỗ trợ](11-constraints-view-va-doi-tuong.md) — PK/FK/UNIQUE/CHECK, VIEW, SEQUENCE và SYNONYM.
13. [DCL, quyền và Role](12-dcl-quyen-va-role.md) — GRANT, REVOKE, ROLE, WITH GRANT OPTION và WITH ADMIN OPTION.
14. [PIVOT, UNPIVOT và Regular Expression](13-pivot-unpivot-va-regexp.md) — Chuyển đổi cấu trúc dữ liệu và regex Oracle.
15. [SQL Style Guide và SQL dễ đọc cho pipeline AI](14-sql-style-guide.md) — Quy ước đặt tên, căn lề, tính portable, thiết kế schema và checklist review SQL trong pipeline.

> **Bàn giao:** Sau **Danh sách bài học**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
