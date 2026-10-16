<!-- lecture-contract: v2 -->
# PIVOT, UNPIVOT và Regular Expression

> **Mục tiêu:** Nắm vững cơ chế xoay trục dữ liệu giữa dạng dọc (Long data) và dạng ngang (Wide data) bằng `PIVOT` / `UNPIVOT`, cùng bộ hàm biểu thức chính quy (`REGEXP_LIKE`, `REGEXP_SUBSTR`, `REGEXP_REPLACE`, `REGEXP_INSTR`, `REGEXP_COUNT`) trong Oracle SQL.
>
> **Phạm vi tham khảo:** PDF *2024 개정판 SQLD 개념정리*, trang 81–84.
>
> **Mạch kiến thức:** Bài trước đã phân tích quản trị an ninh dữ liệu. Bài này tập trung vào các kỹ thuật truy vấn nâng cao: *Làm thế nào để xoay chuyển hình dạng dữ liệu phục vụ báo cáo và xử lý khớp mẫu chuỗi phức tạp?*

---

### 1. Long Data vs Wide Data — Hai dạng cấu trúc hiển thị dữ liệu

> **KR:** Long 데이터는 하나의 속성값이 여러 행으로 누적되는 구조(Tidy Data)이고, Wide 데이터는 속성값이 여러 컬럼으로 전개되어 표현되는 교차표(Cross Table) 구조이다.

| Đặc tính cấu trúc | Long Data (Dữ liệu dạng dọc) | Wide Data (Dữ liệu dạng ngang / Ma trận) |
| --- | --- | --- |
| **Bản chất tổ chức** | Mỗi quan sát tương ứng một hàng độc lập. Cột ít, hàng nhiều. | Các giá trị của một thuộc tính được dàn thành nhiều cột riêng biệt. Cột nhiều, hàng ít. |
| **Tính tương thích RDBMS** | Cực kỳ tối ưu cho các thao tác `JOIN`, `GROUP BY`, lập chỉ mục và mở rộng dữ liệu. | Rất thuận tiện cho người dùng xem báo cáo trực quan hoặc trích xuất Excel. |
| **Lệnh chuyển đổi** | Chuyển sang Wide Data bằng mệnh đề **`PIVOT`**. | Chuyển sang Long Data bằng mệnh đề **`UNPIVOT`**. |

---

### 2. PIVOT — Xoay hàng thành cột

> **KR:** PIVOT은 집계 함수와 함께 사용되어 행 데이터를 열 데이터로 회전시키는 연산자이다.

```sql
SELECT *
FROM (
    SELECT deptno, job, sal
    FROM emp
)
PIVOT (
    SUM(sal)                           -- 1. Hàm tổng hợp bắt buộc
    FOR deptno IN (10 AS dept_10,
                   20 AS dept_20,
                   30 AS dept_30)
);
```

- **Quy tắc thi trắc nghiệm về `PIVOT`:**
  - Bắt buộc phải có **hàm tổng hợp (Aggregate Function)** như `SUM`, `COUNT`, `AVG`...
  - Mệnh đề `FOR column_name IN (...)` chỉ định cột nào sẽ được xoay giá trị thành tên cột mới.
  - Các cột còn lại trong subquery nguồn (không nằm trong hàm tổng hợp và không nằm trong `FOR`) sẽ tự động trở thành **khóa gom nhóm ngầm định (Implicit GROUP BY)**. Do đó, nên dùng Subquery hoặc Inline View chọn chính xác các cột cần thiết trước khi đưa vào `PIVOT`.

---

### 3. UNPIVOT — Xoay cột thành hàng

> **KR:** UNPIVOT은 가로로 전개된 여러 컬럼을 세로 형태의 행 데이터로 환원시키는 연산자이다.

```sql
SELECT job, deptno, total_sal
FROM sales_summary_wide
UNPIVOT (
    total_sal                          -- Tên cột mới chứa GIÁ TRỊ dữ liệu
    FOR deptno IN (dept_10 AS 10,
                   dept_20 AS 20,
                   dept_30 AS 30)
);
```

- `UNPIVOT` chuyển đổi các cột báo cáo ngang trở lại thành 2 cột chuẩn: cột định danh thuộc tính (ví dụ: `deptno`) và cột chứa giá trị đo lường (ví dụ: `total_sal`), đưa dữ liệu về dạng chuẩn để tiếp tục phân tích hoặc liên kết bảng.

---

### 4. 정규 표현식 (Regular Expression) — Các ký tự siêu mẫu (Metacharacters)

> **KR:** 정규 표현식은 문자열의 공통된 규칙을 패턴화하여 복잡한 문자열 검색, 유효성 검증, 치환을 수행하는 강력한 도구이다.

- **Ký tự định vị & ranh giới (Anchors):**
  - `^`: Bắt đầu chuỗi (ví dụ: `^A` bắt đầu bằng ký tự 'A').
  - `$`: Kết thúc chuỗi (ví dụ: `Z$` kết thúc bằng ký tự 'Z').
  - `.`: Đại diện cho đúng 1 ký tự bất kỳ (ngoại trừ ký tự ngắt dòng).
- **Bộ định lượng (Quantifiers):**
  - `?`: Xuất hiện 0 hoặc 1 lần.
  - `*`: Xuất hiện 0 hoặc nhiều lần.
  - `+`: Xuất hiện 1 hoặc nhiều lần.
  - `{m, n}`: Xuất hiện tối thiểu $m$ lần, tối đa $n$ lần.
- **Lớp ký tự chuẩn (POSIX Character Classes):**
  - `[[:digit:]]` hoặc `\d`: Chữ số (`0-9`).
  - `[[:alpha:]]`: Chữ cái (`a-z`, `A-Z`).
  - `[[:alnum:]]`: Chữ cái hoặc chữ số.
  - `[[:space:]]` hoặc `\s`: Ký tự khoảng trắng.

---

### 5. Bộ 5 hàm Regular Expression trong Oracle SQL

| Tên hàm | Chức năng nghiệp vụ | Ví dụ & Cú pháp |
| --- | --- | --- |
| **`REGEXP_LIKE`** | Kiểm tra chuỗi có khớp với mẫu quy định hay không (dùng trực tiếp trong `WHERE`). | `WHERE REGEXP_LIKE(phone, '^010-[0-9]{4}-[0-9]{4}$')` |
| **`REGEXP_SUBSTR`** | Trích xuất chuỗi con thỏa mãn mẫu quy định. | `SELECT REGEXP_SUBSTR('user@test.com', '[^@]+', 1, 2) FROM dual; -- Trả về 'test.com'` |
| **`REGEXP_REPLACE`** | Tìm kiếm đoạn chuỗi khớp mẫu và thay thế bằng chuỗi mới. | `SELECT REGEXP_REPLACE('Hello   World', '\s+', ' ') FROM dual; -- Chuẩn hóa khoảng trắng` |
| **`REGEXP_INSTR`** | Trả về vị trí xuất hiện (vị trí ký tự 1-indexed) của mẫu trong chuỗi. | `SELECT REGEXP_INSTR('abc123xyz', '\d+') FROM dual; -- Trả về 4` |
| **`REGEXP_COUNT`** | Đếm tổng số lần mẫu xuất hiện trong chuỗi nguồn. | `SELECT REGEXP_COUNT('abc_def_xyz', '_') FROM dual; -- Trả về 2` |

---

## 6. Nối mạch sang Bài tiếp theo: SQL Style Guide và viết truy vấn sạch

> **Mạch nối (Bridge):**
> - **Từ đâu (Kiến thức nền):** Bài 13 đã hoàn tất toàn bộ các kỹ thuật thao tác dữ liệu chuyên sâu từ cơ bản đến nâng cao của SQLD Môn 2.
> - **Đang giải quyết gì:** Trong môi trường dự án thực tế và tích hợp pipeline AI, làm thế nào để viết các truy vấn SQL chuẩn mực, rõ ràng, dễ bảo trì và có hiệu năng tối ưu?
> - **Dùng đi đâu:** Bàn giao trực tiếp sang [Bài 14 — SQL Style Guide và SQL dễ đọc cho pipeline AI](./14-sql-style-guide.md) để tổng kết các quy ước đặt tên, quy tắc thụt dòng, cấu trúc CTE và bộ tiêu chí kiểm duyệt SQL sạch.
