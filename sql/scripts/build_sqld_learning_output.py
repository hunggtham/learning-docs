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
    ("mon-2-sql-co-ban-va-ung-dung", "14-sql-style-guide.md", "SQL Style Guide và SQL dễ đọc cho pipeline AI", "Quy ước đặt tên, căn lề, tính portable, thiết kế schema và checklist review SQL trong pipeline.", "sql-style-guide.md", 1, None),
]

# These seven short lessons were authored directly from the same SQLD PDF
# notes rather than sliced from the long raw Markdown files above.  They still
# belong to the generated learning shelf, so the same lecture contract is
# applied to them on every build.
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


def heading_plain(heading: str) -> str:
    return re.sub(r"^#+\s*", "", heading).strip()


def sql_topic_question(topic: str) -> str:
    lowered = topic.lower()
    if re.fullmatch(r"[A-Z][A-Z0-9_ ]{2,}", topic.strip()):
        return "bảng này đang cung cấp những cột và hàng nào, khóa nào sẽ làm cầu nối, và dữ liệu thiếu sẽ ảnh hưởng kết quả ra sao"
    if lowered in {"핵심", "core", "điểm cốt lõi", "cốt lõi"}:
        return "quy tắc nào là bất biến của khái niệm vừa học, và dấu hiệu nào cho biết truy vấn đang áp dụng đúng quy tắc đó"
    if lowered in {"hình dung", "visualization", "cách nhớ", "ghi nhớ"}:
        return "hình ảnh hoặc câu nhớ này đang nén quan hệ nào để ta có thể tự dựng lại kết quả mà không học thuộc cú pháp"
    if "join" in lowered:
        return "ta đang kết hợp những tập hàng nào, cột nào làm cầu nối và điều kiện nối làm thay đổi kết quả ra sao"
    if "subquery" in lowered:
        return "truy vấn con đang tạo ra một giá trị, một tập hàng hay một bảng trung gian, và truy vấn ngoài dùng nó như thế nào"
    if "set operator" in lowered:
        return "ta đang hợp, giao hay trừ các tập kết quả, và điều kiện để hai tập có thể kết hợp là gì"
    if "group" in lowered or "window" in lowered:
        return "ta đang gom các hàng thành nhóm hay giữ từng hàng để tính trong một cửa sổ, và ranh giới tính toán nằm ở đâu"
    if "top" in lowered or "pagination" in lowered:
        return "ta chọn đúng đoạn kết quả nào, theo thứ tự nào, và làm sao không nhầm giữa giới hạn hàng với thứ tự xử lý"
    if "hierarchical" in lowered or "phân cấp" in lowered:
        return "quan hệ cha–con được bắt đầu, mở rộng và dừng lại theo điều kiện nào"
    if "dml" in lowered or "transaction" in lowered:
        return "thay đổi nào tác động lên hàng dữ liệu, phạm vi nào bị ảnh hưởng và khi nào thay đổi được xác nhận"
    if "ddl" in lowered or "constraint" in lowered or "view" in lowered:
        return "cấu trúc hoặc ràng buộc nào đang bảo vệ dữ liệu, và thay đổi đó ảnh hưởng đến các câu lệnh sau ra sao"
    if "pivot" in lowered or "regexp" in lowered:
        return "dữ liệu được biến đổi hình dạng hoặc nhận diện theo mẫu nào, và kết quả mới còn giữ quan hệ gì với dữ liệu đầu vào"
    return "khái niệm này giải quyết vấn đề nào, dựa trên điều kiện nào và tạo ra hệ quả gì trong truy vấn"


def sql_section_synthesis(topic: str, body: str) -> str:
    cues = []
    if "|" in body:
        cues.append("bảng đang đặt các lựa chọn cạnh nhau theo cùng tiêu chí")
    if re.search(r"```|\bSELECT\b|\bWHERE\b|\bON\b|\bGROUP BY\b", body, re.I):
        cues.append("cú pháp cho thấy quy tắc được thực hiện trong truy vấn")
    if re.search(r"ví dụ|example|예시", body, re.I):
        cues.append("ví dụ cho thấy quy tắc biến thành kết quả cụ thể")
    if not cues:
        cues.append("các định nghĩa và điều kiện làm rõ phạm vi áp dụng")
    return (
        f"Khi gom phần **{topic}** lại, ta không cần nhớ các dòng như những mảnh rời: "
        f"{' và '.join(cues)}. Hãy tự trả lời câu hỏi của section bằng một chuỗi **đối tượng → điều kiện → kết quả**; nếu thiếu một mắt xích, đó chính là điểm cần đọc lại trước khi chuyển phần."
    )


def sql_section_opening(topic: str) -> str:
    question = sql_topic_question(topic)
    if re.fullmatch(r"[A-Z][A-Z0-9_ ]{2,}", topic.strip()):
        return (
            f"**{topic}** là dữ liệu đầu vào của phép suy luận, không phải một khái niệm cần học tách khỏi truy vấn. "
            f"Hãy đọc các cột và hàng để trả lời: **{question}?**"
        )
    if topic.lower() in {"핵심", "core", "điểm cốt lõi", "cốt lõi"}:
        return (
            f"Đây là đoạn rút quy tắc từ ví dụ vừa đọc. Với **{topic}**, câu hỏi là: **{question}?** "
            "Phần bên dưới phải được dùng để kiểm tra lại các dòng dữ liệu, không chỉ để nhắc lại khẩu hiệu."
        )
    if topic.lower() in {"hình dung", "visualization", "cách nhớ", "ghi nhớ"}:
        return (
            f"Đoạn **{topic}** đổi quy tắc thành hình ảnh hoặc câu nhớ. Hãy trả lời: **{question}?** "
            "Sau đó quay lại điều kiện SQL để chắc rằng cách nhớ không làm mất trường hợp biên."
        )
    return f"Ta bắt đầu **{topic}** bằng câu hỏi: **{question}?** Hãy đọc phần dưới để tìm cơ chế, điều kiện và hệ quả trả lời cho câu hỏi đó."


def lecture_content(content: str, title: str, description: str) -> str:
    """Build a connected lecture arc around source headings and their evidence."""
    cleaned = clean_markdown(content).strip()
    lines = cleaned.splitlines()
    headings = [line for line in lines if re.match(r"^#{2,6} ", line)]
    if not headings:
        return (
            f"Để học **{title}**, trước hết hãy giữ câu hỏi: **{sql_topic_question(title)}?** "
            f"Mục tiêu của bài là hiểu **{description.rstrip('.')}** như một quan hệ có thể áp dụng, không chỉ là danh sách thuật ngữ.\n\n"
            f"{cleaned}\n\n"
            f"Sau khi đọc, hãy tự chốt **{title}** bằng đối tượng, điều kiện và hệ quả rồi đối chiếu với bài kế tiếp."
        )

    enriched: list[str] = [
        f"Để học **{title}** như một mạch suy luận, trước hết hãy giữ câu hỏi: **{sql_topic_question(title)}?** Mục đích của bài là biến **{description.rstrip('.')}** thành cách đọc có thể áp dụng.",
        "",
    ]
    current: str | None = None
    current_body: list[str] = []
    section_index = 0

    def close_section(next_topic: str | None) -> None:
        nonlocal current, current_body, section_index
        if not current:
            return
        body = "\n".join(current_body).strip()
        enriched.extend(["", sql_section_synthesis(current, body)])
        if next_topic:
            relation = "mở rộng" if section_index % 3 == 1 else "đối chiếu" if section_index % 3 == 2 else "dùng lại"
            enriched.extend([
                "",
                f"Vậy ta đã có tiêu chí để đọc **{current}**. Bây giờ chuyển sang **{next_topic}**: phần mới sẽ **{relation}** điểm tựa vừa có, nên hãy giữ lại câu hỏi và kiểm tra xem đối tượng hoặc điều kiện nào đã thay đổi.",
                "",
            ])
        current_body = []

    for line in lines:
        match = re.match(r"^(#{2,6}) (.+)$", line)
        if match:
            next_topic = heading_plain(line)
            close_section(next_topic if current else None)
            current = next_topic
            section_index += 1
            enriched.extend([
                sql_section_opening(current),
                "",
                line,
                "",
            ])
            current_body = []
            continue
        enriched.append(line)
        if current:
            current_body.append(line)

    close_section(None)
    if current:
        enriched.extend([
            "",
            f"Như vậy, **{current}** đã được đặt trong quan hệ giữa đầu vào, quy tắc xử lý và kết quả. Khi ôn lại, hãy tự diễn đạt ranh giới của nó rồi dùng ranh giới đó làm điểm nối sang bài tiếp theo.",
        ])
    return re.sub(r"\n{3,}", "\n\n", "\n".join(enriched).strip())


def lesson_document(title: str, description: str, content: str) -> str:
    taught = lecture_content(content, title, description)
    return f"""# {title}

> **Mục tiêu:** {description}

## Từ khóa cần nhớ (Keyword)

Phần giải thích dùng tiếng Việt trước. Ở mọi lần xuất hiện, thuật ngữ SQLD dùng dạng `nghĩa Việt (English / 한국어)` để vừa giữ mạch đọc vừa đối chiếu được từ khóa trong đề.

## Mạch tư duy (Logic học)

Hãy xác định **đối tượng dữ liệu** trước, sau đó đọc **điều kiện**, **phạm vi dòng**, **thứ tự xử lý** và cuối cùng kiểm tra **kết quả mong đợi**. Với SQL, luôn phân biệt điều kiện lọc trước nhóm (`WHERE`) với điều kiện lọc sau nhóm (`HAVING`); đây là cầu nối để hiểu vì sao cùng một truy vấn có thể cho kết quả khác nhau.

## Mạch nối của bài học

Bài này không đứng riêng: hãy nối **{title}** với bài trước bằng đối tượng dữ liệu/điều kiện mà nó tái sử dụng, rồi dùng kết quả ở phần cuối để chọn bài kế tiếp trong cùng môn. Khi gặp một truy vấn mới, nói rõ nó đang mở rộng mô hình dữ liệu, thứ tự xử lý hay cách kiểm tra kết quả nào trước khi nhớ cú pháp.

> **Cách học:** Đọc phần khái niệm → tự chạy lại các ví dụ SQL → chốt lại mục **từ khóa (Keyword)**, bảng so sánh và phần ghi nhớ cuối bài.

---

{taught}"""


def manual_lesson_document(path: Path, title: str, description: str) -> str:
    """Retrofit a directly-authored lesson without losing its source prose."""
    existing = path.read_text(encoding="utf-8")
    if "<!-- lecture-contract: v2 -->" in existing:
        return existing
    existing = re.sub(r"\A<!-- lecture-contract: v1 -->\n", "", existing)
    body = re.sub(r"\A# .*?\n\n?", "", existing, count=1)
    taught = lecture_content(body, title, description)
    return f"""<!-- lecture-contract: v2 -->
# {title}

> **Mục tiêu:** {description}

{taught.strip()}
"""


def main() -> None:
    # Preserve manually authored PDF-based lessons alongside generated lessons.
    OUT.mkdir(parents=True, exist_ok=True)

    for folder, name, title, description, source, first, last in LESSONS:
        target = OUT / folder
        target.mkdir(exist_ok=True)
        content = source_slice(source, first, last)
        (target / name).write_text(lesson_document(title, description, content), encoding="utf-8")

    manual_target = OUT / "mon-2-sql-co-ban-va-ung-dung"
    for name, title, description in MANUAL_LESSONS:
        path = manual_target / name
        path.write_text(manual_lesson_document(path, title, description), encoding="utf-8")

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
            f"# {subject_name}\n\n{guidance}\n\n## Mạch bài giảng\n\nMỗi bài mở bằng mục đích và câu hỏi cần giải quyết, đi qua các section nguồn bằng câu nối, rồi chốt quan hệ giữa đầu vào, điều kiện xử lý và kết quả trước khi bàn giao sang bài kế tiếp.\n\n## Danh sách bài học\n\n{links}\n",
            encoding="utf-8",
        )

    readme = """# SQLD – Tài liệu học đã chuẩn hóa

Tài liệu được chia theo hai môn của kỳ thi SQLD. Mỗi file là một bài học độc lập, giữ lại toàn bộ giải thích và ví dụ SQL từ nguồn, đồng thời có tiêu đề, mục tiêu học tập và mạch giảng mở đầu → giải thích → bàn giao → kết thúc.

> **Mạch nối:** Đi từ mô hình dữ liệu → JOIN/subquery/group/window → transaction/DDL/DCL → các truy vấn nâng cao. Mỗi bài dùng object, điều kiện hoặc thứ tự xử lý của bài trước; hãy quay lại ví dụ khi chuyển sang bài kế tiếp.

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
14. SQL Style Guide và SQL dễ đọc cho pipeline AI

## Phạm vi nguồn

Phần này giải thích phạm vi và giới hạn của bộ tài liệu, để người học biết các bài dưới đây được chọn từ đâu trước khi dùng chúng làm mạch ôn tập.

- Đã dùng: `1.md`, `2.md`, `3.md`, `join.md`, `sql-style-guide.md` và phần trang 85–103 của `2024개정판_SQLD_개념정리(1).pdf`.
- Không xuất: `temp.md` vì là bản sao của phần Transaction/NULL/Identifier trong `2.md`; `4.md` vì rỗng.
- Các tiêu đề tiếng Hàn được giữ lại để hỗ trợ đối chiếu thuật ngữ SQLD; phần giải thích chính vẫn bằng tiếng Việt.
"""
    (OUT / "README.md").write_text(readme, encoding="utf-8")


if __name__ == "__main__":
    main()
