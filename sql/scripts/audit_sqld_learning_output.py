from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "sql" / "output"
GENERATED = (
    "mon-1-mo-hinh-du-lieu/01-nen-tang-mo-hinh-du-lieu.md",
    "mon-1-mo-hinh-du-lieu/02-erd-entity-attribute-relationship-identifier.md",
    "mon-1-mo-hinh-du-lieu/03-mo-hinh-du-lieu-huong-hieu-nang-va-chuan-hoa.md",
    "mon-1-mo-hinh-du-lieu/04-quan-he-transaction-null-va-identifier.md",
    "mon-2-sql-co-ban-va-ung-dung/01-join.md",
    "mon-2-sql-co-ban-va-ung-dung/02-subquery.md",
    "mon-2-sql-co-ban-va-ung-dung/03-set-operators.md",
    "mon-2-sql-co-ban-va-ung-dung/04-group-functions.md",
    "mon-2-sql-co-ban-va-ung-dung/05-window-functions.md",
    "mon-2-sql-co-ban-va-ung-dung/06-top-n-va-pagination.md",
    "mon-2-sql-co-ban-va-ung-dung/07-hierarchical-query.md",
    "mon-2-sql-co-ban-va-ung-dung/00-sql-select-ham-va-loc.md",
    "mon-2-sql-co-ban-va-ung-dung/08-dml-va-toan-tu.md",
    "mon-2-sql-co-ban-va-ung-dung/09-tcl-va-transaction.md",
    "mon-2-sql-co-ban-va-ung-dung/10-ddl-va-dinh-nghia-bang.md",
    "mon-2-sql-co-ban-va-ung-dung/11-constraints-view-va-doi-tuong.md",
    "mon-2-sql-co-ban-va-ung-dung/12-dcl-quyen-va-role.md",
    "mon-2-sql-co-ban-va-ung-dung/13-pivot-unpivot-va-regexp.md",
    "mon-2-sql-co-ban-va-ung-dung/14-sql-style-guide.md",
)


def main() -> int:
    failures: list[str] = []
    section_count = 0
    for relative in GENERATED:
        path = OUT / relative
        text = path.read_text(encoding="utf-8")
        # The metadata headings ("Từ khóa cần nhớ" and "Mạch tư duy") are
        # intentionally outside the lecture body.  Scope structural checks to
        # the generated lesson body so those headings do not create false
        # coverage failures.
        body = text
        sections = re.findall(r"^#{2,6} ", body, flags=re.MULTILINE)
        section_count += len(sections)
        if "Mục đích của bài" not in text and "**Mục tiêu:**" not in text:
            failures.append(f"{relative}: missing lesson purpose")
        opening_count = body.count("Ta bắt đầu **")
        explanation_count = body.count("Khi gom phần **")
        if opening_count and explanation_count < opening_count:
            failures.append(f"{relative}: section explanation coverage")
        closure_count = (
            body.count("Vừa rồi ta đã khép **")
            + body.count("Như vậy, **")
            + body.count("Khi gom phần **")
        )
        if opening_count and closure_count < opening_count:
            failures.append(f"{relative}: section closure coverage")
        if "<br" in text or "<mark>" in text or re.search(r"^#{1,6}\s*$", text, re.MULTILINE):
            failures.append(f"{relative}: unresolved markup or empty heading")

    for readme in (OUT / "mon-1-mo-hinh-du-lieu/README.md", OUT / "mon-2-sql-co-ban-va-ung-dung/README.md"):
        text = readme.read_text(encoding="utf-8")
        for link in re.findall(r"\]\(([^)]+\.md)\)", text):
            if not (readme.parent / link).exists():
                failures.append(f"{readme.relative_to(ROOT)}: broken link {link}")

    print(f"generated_lessons={len(GENERATED)} sections={section_count} failures={len(failures)}")
    for failure in failures:
        print(f"FAIL {failure}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
