from pathlib import Path
import re


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
    ("mon-2-sql-co-ban-va-ung-dung", "14-sql-style-guide.md", "SQL Style Guide và SQL dễ đọc cho pipeline AI", "Quy ước đặt tên, căn lề, tính portable, thiết kế schema và checklist review SQL trong pipeline.", "sql-style-guide.md", 1, None),
]

# These seven short lessons were authored directly from the same SQLD PDF
# notes rather than sliced from the long raw Markdown files above.
MANUAL_LESSONS = [
    ("00-sql-select-ham-va-loc.md", "SQL cơ bản: SELECT, hàm, lọc, nhóm và sắp xếp", "SELECT, WHERE, hàm, GROUP BY/HAVING và ORDER BY."),
    ("08-dml-va-toan-tu.md", "DML và toán tử", "INSERT, UPDATE, DELETE, MERGE, SELECT, toán tử số học và nối chuỗi."),
    ("09-tcl-va-transaction.md", "TCL và Transaction", "ACID, COMMIT, ROLLBACK, SAVEPOINT và khác biệt Oracle/SQL Server."),
    ("10-ddl-va-dinh-nghia-bang.md", "DDL và định nghĩa bảng", "Kiểu dữ liệu, CREATE/CTAS/ALTER/DROP/TRUNCATE."),
    ("11-constraints-view-va-doi-tuong.md", "Constraints, View và các đối tượng hỗ trợ", "PK/FK/UNIQUE/CHECK, VIEW, SEQUENCE và SYNONYM."),
    ("12-dcl-quyen-va-role.md", "DCL, quyền và Role", "GRANT, REVOKE, ROLE, WITH GRANT OPTION và WITH ADMIN OPTION."),
    ("13-pivot-unpivot-va-regexp.md", "PIVOT, UNPIVOT và Regular Expression", "Chuyển đổi cấu trúc dữ liệu và regex Oracle."),
]


def source_slice(filename: str, first: int, last: int | None) -> str:
    lines = (RAW / filename).read_text(encoding="utf-8").splitlines()
    selected = lines[first - 1:last]
    return "\n".join(selected).strip() + "\n"


def clean_markdown(text: str) -> str:
    # Remove only accidental boilerplate; preserve explanations, examples and SQL.
    text = re.sub(r"\A(?:Tiếp tục \*\*.*?\n\n)+", "", text, flags=re.DOTALL)
    text = re.sub(r"[ \t]+$", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text)
    # A lesson already has one H1. Demote source headings to retain valid hierarchy.
    text = re.sub(r"(?m)^#(#{0,5})\s", lambda m: "#" + m.group(1) + "# ", text)
    return text.strip() + "\n"


def lesson_document(title: str, content: str) -> str:
    """Wrap source content without inventing teaching prose."""
    return f"# {title}\n\n{clean_markdown(content).strip()}\n"


def manual_lesson_document(path: Path) -> str:
    """Keep directly-authored lessons unchanged during regeneration."""
    return path.read_text(encoding="utf-8")


def main() -> None:
    # Preserve manually authored PDF-based lessons alongside generated lessons.
    OUT.mkdir(parents=True, exist_ok=True)

    for folder, name, title, description, source, first, last in LESSONS:
        target = OUT / folder
        target.mkdir(exist_ok=True)
        content = source_slice(source, first, last)
        (target / name).write_text(lesson_document(title, content), encoding="utf-8")

    manual_target = OUT / "mon-2-sql-co-ban-va-ung-dung"
    for name, title, description in MANUAL_LESSONS:
        path = manual_target / name
        path.write_text(manual_lesson_document(path), encoding="utf-8")

    subject_indexes = {
        "mon-1-mo-hinh-du-lieu": ("Môn 1 – 데이터 모델링의 이해", "Nên học theo thứ tự từ mô hình hóa cơ bản đến chuẩn hóa và các khái niệm SQL biểu diễn trong mô hình."),
        "mon-2-sql-co-ban-va-ung-dung": ("Môn 2 – SQL 기본 및 활용", "Nên học JOIN trước, sau đó đến Subquery/Group Function và các kỹ thuật truy vấn nâng cao; kết thúc bằng SQL Style Guide để áp dụng các quy ước vào model trong pipeline."),
    }
    for folder, (subject_name, guidance) in subject_indexes.items():
        entries = [lesson for lesson in LESSONS if lesson[0] == folder]
        if folder == "mon-2-sql-co-ban-va-ung-dung":
            entries.extend([
                *[(folder, name, title, description) for name, title, description in MANUAL_LESSONS],
            ])
        entries.sort(key=lambda lesson: lesson[1])
        links = "\n".join(f"{index}. [{title}]({name}) — {description}" for index, (_, name, title, description, *_rest) in enumerate(entries, 1))
        (OUT / folder / "README.md").write_text(
            f"# {subject_name}\n\n## Danh sách bài học\n\n{links}\n",
            encoding="utf-8",
        )

    links = [
        f"- [{title}]({folder}/README.md)"
        for folder, _name, title, _description, *_rest in LESSONS
    ]
    (OUT / "README.md").write_text(
        "# SQLD – Tài liệu học đã chuẩn hóa\n\n"
        "## Các môn\n\n"
        + "\n".join(dict.fromkeys(links))
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
