# SQLD – Tài liệu học đã chuẩn hóa

> **Mạch đọc:** README này là owner của **SQLD – Tài liệu học đã chuẩn hóa**. Route đi từ mô hình dữ liệu → JOIN/subquery/group/window → transaction, DDL/DCL → truy vấn nâng cao và bàn giao ví dụ, để mỗi bài kế thừa object, điều kiện hoặc thứ tự xử lý của bài trước.

Tài liệu được chia theo hai môn của kỳ thi SQLD. Mỗi file là một bài học độc lập, giữ lại toàn bộ giải thích và ví dụ SQL từ nguồn, đồng thời có tiêu đề, mục tiêu học tập và mạch giảng mở đầu → giải thích → bàn giao → kết thúc.

> **Mạch nối:** Đi từ mô hình dữ liệu → JOIN/subquery/group/window → transaction/DDL/DCL → các truy vấn nâng cao. Mỗi bài dùng object, điều kiện hoặc thứ tự xử lý của bài trước; hãy quay lại ví dụ khi chuyển sang bài kế tiếp.

## Môn 1 – 데이터 모델링의 이해 / Mô hình dữ liệu

1. Nền tảng mô hình hóa dữ liệu
2. ERD, Entity, Attribute, Relationship và Identifier
3. Mô hình dữ liệu hướng hiệu năng và chuẩn hóa
4. Quan hệ, Transaction, NULL và Identifier

> **Chuyển mạch:** Trong **SQLD – Tài liệu học đã chuẩn hóa**, **Môn 1 – 데이터 모델링의 이해 / Mô hình dữ liệu** nêu điều cần giải thích; **Môn 2 – SQL 기본 및 활용 / SQL cơ bản và ứng dụng** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Phạm vi nguồn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Môn 2 – SQL 기본 및 활용 / SQL cơ bản và ứng dụng

0. SQL cơ bản: SELECT, hàm, lọc, nhóm và sắp xếp
1. JOIN
2. Subquery
3. Set Operators
4. Group Functions
5. Window Functions
6. TOP-N và Pagination
7. Hierarchical Query
8. DML và toán tử
9. TCL và Transaction
10. DDL và định nghĩa bảng
11. Constraints, View và các đối tượng hỗ trợ
12. DCL, quyền và Role
13. PIVOT, UNPIVOT và Regular Expression
14. SQL Style Guide và SQL dễ đọc cho pipeline AI

> **Chuyển mạch:** README này dùng **Phạm vi nguồn** để xác định bằng chứng và owner cho **Môn 2 – SQL cơ bản và ứng dụng**; hãy quay lại mục lục môn đó khi cần nối khái niệm với bài thực hành cụ thể.

## Phạm vi nguồn

Phần này giải thích phạm vi và giới hạn của bộ tài liệu, để người học biết các bài dưới đây được chọn từ đâu trước khi dùng chúng làm mạch ôn tập.

- Đã dùng: `1.md`, `2.md`, `3.md`, `join.md`, `sql-style-guide.md` và phần trang 85–103 của `2024개정판_SQLD_개념정리(1).pdf`.
- Không xuất: `temp.md` vì là bản sao của phần Transaction/NULL/Identifier trong `2.md`; `4.md` vì rỗng.
- Các tiêu đề tiếng Hàn được giữ lại để hỗ trợ đối chiếu thuật ngữ SQLD; phần giải thích chính vẫn bằng tiếng Việt.

> **Bàn giao:** Sau **Phạm vi nguồn**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
