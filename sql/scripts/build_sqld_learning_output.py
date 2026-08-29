from pathlib import Path
import re
import shutil


ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "sql" / "raw_md" / "sqld-learning"
OUT = ROOT / "sql" / "output"


LESSONS = [
    ("mon-1-mo-hinh-du-lieu", "01-nen-tang-mo-hinh-du-lieu.md", "Nền tảng mô hình hóa dữ liệu", "Khái niệm, mục tiêu, đặc điểm, góc nhìn, ba cấp độ và tính độc lập dữ liệu.", "1.md", 1, 881),
    ("mon-1-mo-hinh-du-lieu", "02-erd-entity-attribute-relationship-identifier.md", "ERD, Entity, Attribute, Relationship và Identifier", "Xây dựng ERD; phân loại entity/attribute/relationship; chọn và sử dụng identifier.", "1.md", 882, 5321),
    ("mon-1-mo-hinh-du-lieu", "03-mo-hinh-du-lieu-huong-hieu-nang-va-chuan-hoa.md", "Mô hình dữ liệu hướng hiệu năng và chuẩn hóa", "Quy trình tối ưu mô hình, phụ thuộc hàm, 1NF–5NF, BCNF và phi chuẩn hóa.", "2.md", 1, 595),
    ("mon-1-mo-hinh-du-lieu", "04-quan-he-transaction-null-va-identifier.md", "Quan hệ, Transaction, NULL và Identifier", "Quan hệ trong mô hình, ACID, NULL trong SQL và natural/surrogate key.", "2.md", 596, 2849),
    ("mon-2-sql-co-ban-va-ung-dung", "01-join.md", "JOIN", "INNER/OUTER/CROSS/SELF JOIN, NATURAL/USING, ANSI join và các bẫy điều kiện.", "join.md", 1, None),
    ("mon-2-sql-co-ban-va-ung-dung", "02-subquery.md", "Subquery", "Single/multi-row, correlated, scalar, inline view, EXISTS và các bẫy thường gặp.", "2.md", 2850, 4264),
    ("mon-2-sql-co-ban-va-ung-dung", "03-set-operators.md", "Set Operators", "UNION, UNION ALL, INTERSECT, MINUS/EXCEPT và các quy tắc kết hợp tập kết quả.", "2.md", 4265, 4874),
    ("mon-2-sql-co-ban-va-ung-dung", "04-group-functions.md", "Group Functions", "Aggregate, GROUP BY, ROLLUP, CUBE, GROUPING và GROUPING SETS.", "2.md", 4875, None),
    ("mon-2-sql-co-ban-va-ung-dung", "05-window-functions.md", "Window Functions", "OVER, PARTITION BY, window frame, ranking và các hàm phân tích.", "3.md", 1, 1713),
    ("mon-2-sql-co-ban-va-ung-dung", "06-top-n-va-pagination.md", "TOP-N và Pagination", "ROWNUM, ROW_NUMBER/RANK/DENSE_RANK, FETCH/OFFSET, TOP và WITH TIES.", "3.md", 1714, 3289),
    ("mon-2-sql-co-ban-va-ung-dung", "07-hierarchical-query.md", "Hierarchical Query", "START WITH, CONNECT BY PRIOR, LEVEL, NOCYCLE và các pseudocolumn phân cấp.", "3.md", 3290, None),
]


def source_slice(filename: str, first: int, last: int | None) -> str:
    lines = (RAW / filename).read_text(encoding="utf-8").splitlines()
    selected = lines[first - 1:last]
    return "\n".join(selected).strip() + "\n"


def clean_markdown(text: str) -> str:
    # Remove only accidental boilerplate; preserve explanations, examples and SQL.
    text = re.sub(r"\A(?:Tiếp tục \*\*.*?\n\n)+", "", text, flags=re.DOTALL)
    text = re.sub(r"\n{3,}", "\n\n", text)
    # A lesson already has one H1. Demote source headings to retain valid hierarchy.
    text = re.sub(r"(?m)^#(#{0,5})\s", lambda m: "#" + m.group(1) + "# ", text)
    return text.strip() + "\n"


def lesson_document(title: str, description: str, content: str) -> str:
    return f"""# {title}

> **Mục tiêu:** {description}

> **Cách học:** Đọc phần khái niệm → tự chạy lại các ví dụ SQL → chốt lại các mục `Keyword`, bảng so sánh và phần ghi nhớ cuối bài.

---

{clean_markdown(content)}"""


def main() -> None:
    # Preserve manually authored PDF-based lessons alongside generated lessons.
    OUT.mkdir(parents=True, exist_ok=True)

    for folder, name, title, description, source, first, last in LESSONS:
        target = OUT / folder
        target.mkdir(exist_ok=True)
        content = source_slice(source, first, last)
        (target / name).write_text(lesson_document(title, description, content), encoding="utf-8")

    subject_indexes = {
        "mon-1-mo-hinh-du-lieu": ("Môn 1 – 데이터 모델링의 이해", "Nên học theo thứ tự từ mô hình hóa cơ bản đến chuẩn hóa và các khái niệm SQL biểu diễn trong mô hình."),
        "mon-2-sql-co-ban-va-ung-dung": ("Môn 2 – SQL 기본 및 활용", "Nên học JOIN trước, sau đó đến Subquery/Group Function rồi các kỹ thuật truy vấn nâng cao."),
    }
    for folder, (subject_name, guidance) in subject_indexes.items():
        entries = [lesson for lesson in LESSONS if lesson[0] == folder]
        if folder == "mon-2-sql-co-ban-va-ung-dung":
            entries.extend([
                (folder, "00-sql-select-ham-va-loc.md", "SQL cơ bản: SELECT, hàm, lọc, nhóm và sắp xếp", "SELECT, WHERE, hàm, GROUP BY/HAVING và ORDER BY."),
                (folder, "08-dml-va-toan-tu.md", "DML và toán tử", "INSERT, UPDATE, DELETE, MERGE, SELECT, toán tử số học và nối chuỗi."),
                (folder, "09-tcl-va-transaction.md", "TCL và Transaction", "ACID, COMMIT, ROLLBACK, SAVEPOINT và khác biệt Oracle/SQL Server."),
                (folder, "10-ddl-va-dinh-nghia-bang.md", "DDL và định nghĩa bảng", "Kiểu dữ liệu, CREATE/CTAS/ALTER/DROP/TRUNCATE."),
                (folder, "11-constraints-view-va-doi-tuong.md", "Constraints, View và các đối tượng hỗ trợ", "PK/FK/UNIQUE/CHECK, VIEW, SEQUENCE và SYNONYM."),
                (folder, "12-dcl-quyen-va-role.md", "DCL, quyền và Role", "GRANT, REVOKE, ROLE, WITH GRANT OPTION và WITH ADMIN OPTION."),
                (folder, "13-pivot-unpivot-va-regexp.md", "PIVOT, UNPIVOT và Regular Expression", "Chuyển đổi cấu trúc dữ liệu và regex Oracle."),
            ])
        entries.sort(key=lambda lesson: lesson[1])
        links = "\n".join(f"{index}. [{title}]({name}) — {description}" for index, (_, name, title, description, *_rest) in enumerate(entries, 1))
        (OUT / folder / "README.md").write_text(
            f"# {subject_name}\n\n{guidance}\n\n## Danh sách bài học\n\n{links}\n",
            encoding="utf-8",
        )

    readme = """# SQLD – Tài liệu học đã chuẩn hóa

Tài liệu được chia theo hai môn của kỳ thi SQLD. Mỗi file là một bài học độc lập, giữ lại toàn bộ giải thích và ví dụ SQL từ nguồn, đồng thời có tiêu đề và mục tiêu học tập thống nhất.

## Môn 1 – 데이터 모델링의 이해 / Mô hình dữ liệu

1. Nền tảng mô hình hóa dữ liệu
2. ERD, Entity, Attribute, Relationship và Identifier
3. Mô hình dữ liệu hướng hiệu năng và chuẩn hóa
4. Quan hệ, Transaction, NULL và Identifier

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

## Phạm vi nguồn

- Đã dùng: `1.md`, `2.md`, `3.md`, `join.md` và phần trang 85–103 của `2024개정판_SQLD_개념정리(1).pdf`.
- Không xuất: `temp.md` vì là bản sao của phần Transaction/NULL/Identifier trong `2.md`; `4.md` vì rỗng.
- Các tiêu đề tiếng Hàn được giữ lại để hỗ trợ đối chiếu thuật ngữ SQLD; phần giải thích chính vẫn bằng tiếng Việt.
"""
    (OUT / "README.md").write_text(readme, encoding="utf-8")


if __name__ == "__main__":
    main()
