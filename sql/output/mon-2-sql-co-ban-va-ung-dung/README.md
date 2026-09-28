# Môn 2 – SQL 기본 및 활용

Nên học phép nối (join / 조인) trước, sau đó đến Subquery/Group hàm (function / 함수) rồi các kỹ thuật truy vấn nâng cao.

> **Mạch nối:** Hãy đọc các bài theo thứ tự được liệt kê; mỗi bài mở rộng một ranh giới (boundary / 경계) của bài trước và chuẩn bị điều kiện để đọc bài sau.

## Danh sách bài học

1. [SQL cơ bản: SELECT, hàm, lọc, nhóm và sắp xếp](00-sql-select-ham-va-loc.md) — SELECT, WHERE, hàm, GROUP BY/HAVING và thứ tự (order / 순서) BY.
2. [JOIN](01-join.md) — INNER/OUTER/CROSS/SELF phép nối (join / 조인), NATURAL/USING, ANSI phép nối (join / 조인) và các bẫy điều kiện.
3. [Subquery](02-subquery.md) — Single/multi-row, correlated, scalar, inline view, EXISTS và các bẫy thường gặp.
4. [Set Operators](03-set-operators.md) — UNION, UNION ALL, INTERSECT, MINUS/EXCEPT và các quy tắc kết hợp tập kết quả.
5. [Group Functions](04-group-functions.md) — Aggregate, GROUP BY, ROLLUP, CUBE, GROUPING và GROUPING SETS.
6. [Window Functions](05-window-functions.md) — OVER, PARTITION BY, cửa sổ (window / 윈도우) frame, ranking và các hàm phân tích.
7. [TOP-N và Pagination](06-top-n-va-pagination.md) — ROWNUM, ROW_NUMBER/RANK/DENSE_RANK, FETCH/OFFSET, TOP và WITH TIES.
8. [Hierarchical Query](07-hierarchical-query.md) — START WITH, CONNECT BY PRIOR, mức (level / 수준), NOCYCLE và các pseudocolumn phân cấp.
9. [DML và toán tử](08-dml-va-toan-tu.md) — INSERT, cập nhật (update / 업데이트), DELETE, MERGE, SELECT, toán tử số học và nối chuỗi.
10. [TCL và Transaction](09-tcl-va-transaction.md) — ACID, lần ghi nhận (commit / 커밋), quay lui (rollback / 롤백), SAVEPOINT và khác biệt Oracle/SQL máy chủ (server / 서버).
11. [DDL và định nghĩa bảng](10-ddl-va-dinh-nghia-bang.md) — Kiểu dữ liệu, CREATE/CTAS/ALTER/DROP/TRUNCATE.
12. [Constraints, View và các đối tượng hỗ trợ](11-constraints-view-va-doi-tuong.md) — PK/FK/UNIQUE/CHECK, VIEW, chuỗi (sequence / 시퀀스) và SYNONYM.
13. [DCL, quyền và Role](12-dcl-quyen-va-role.md) — GRANT, REVOKE, ROLE, WITH GRANT OPTION và WITH ADMIN OPTION.
14. [PIVOT, UNPIVOT và Regular Expression](13-pivot-unpivot-va-regexp.md) — Chuyển đổi cấu trúc dữ liệu và regex Oracle.
