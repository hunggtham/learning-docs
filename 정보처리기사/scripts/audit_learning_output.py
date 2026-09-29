from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output"
SUBJECTS = [
    "01-software-design",
    "02-software-development",
    "03-database-construction",
    "04-programming-language",
    "05-information-system-management",
]

CLOSING_MARKERS = ("Như vậy", "Ta có thể khép", "Điểm chốt", "Khép lại")


def lesson_issues(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    issues: list[str] = []
    required_headers = (
        "## 학습 목표",
        "## 핵심 키워드",
        "## 선행·연결 개념",
        "## 읽는 방법",
    )
    for header in required_headers:
        if header not in text:
            issues.append(f"missing {header}")
    if "mục đích" not in text.lower():
        issues.append("missing teaching purpose")
    if "Mục đích của bài này là hiểu" not in text:
        issues.append("missing topic-specific learning objective")
    if "Để đọc **" not in text:
        issues.append("missing beginner-facing topic question")
    if "Phần nguồn bên dưới cung cấp" not in text and "Các bullet đang nén" not in text:
        issues.append("missing prose bridge into source evidence")
    if not any(marker in text for marker in (
        "đối tượng → điều kiện → hệ quả",
        "đối tượng, điều kiện và giới hạn",
        "cơ chế, điều kiện và hệ quả",
    )):
        issues.append("missing object-condition-consequence synthesis")
    core_count = len(re.findall(r"^#{3,6} ", text, flags=re.MULTILINE))
    purpose_patterns = (
        r"Mục đích của đoạn",
        r"Hãy xác định \*\*[^\n]*\*\* đang",
        r"Để không đọc \*\*",
        r"Ở đoạn \*\*",
        r"Với \*\*[^\n]*, mục tiêu đọc",
        r"Đoạn \*\*[^\n]* trả lời",
    )
    core_purpose_count = sum(len(re.findall(pattern, text, flags=re.IGNORECASE)) for pattern in purpose_patterns)
    if core_count and core_purpose_count < core_count:
        issues.append(f"core purpose coverage {core_purpose_count}/{core_count}")
    bridge_count = text.count("Ta vừa chốt **") + text.count("Sau khi đọc **") + text.count(" vừa cho ta cách đặt câu hỏi.")
    final_core_closure = sum(text.count(marker) for marker in ("Với **", "Điểm chốt của **", "Như vậy, **"))
    if core_count and (bridge_count < core_count - 1 or final_core_closure < 1):
        issues.append("core closure coverage is incomplete")
    if not any(marker in text for marker in CLOSING_MARKERS):
        issues.append("missing teaching closure")
    if core_count > 1 and "Ta vừa chốt **" not in text and "Sau khi đọc **" not in text and "vừa cho ta cách đặt câu hỏi" not in text:
        issues.append("missing internal section handoff")
    if re.search(r"^#{1,6}\s*$", text, flags=re.MULTILINE):
        issues.append("empty heading")
    if "<br" in text or "<mark>" in text or "</mark>" in text:
        issues.append("unresolved markup")
    return issues


def guide_issues(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    sections = re.findall(r"^## (?!학습 목표|권장 학습 순서)(.+)$", text, flags=re.MULTILINE)
    issues: list[str] = []
    if not sections:
        issues.append("no lecture sections")
    purpose_count = text.lower().count("mục đích")
    if purpose_count < len(sections):
        issues.append(f"purpose coverage {purpose_count}/{len(sections)}")
    closing_count = sum(text.count(marker) for marker in CLOSING_MARKERS)
    if closing_count < len(sections):
        issues.append(f"closure coverage {closing_count}/{len(sections)}")
    if re.search(r"^#{1,6}\s*$", text, flags=re.MULTILINE):
        issues.append("empty heading")
    if "<br" in text or "<mark>" in text or "</mark>" in text:
        issues.append("unresolved markup")
    return issues


def main() -> int:
    failures: list[tuple[Path, list[str]]] = []
    lesson_count = 0
    for subject in SUBJECTS:
        target = OUTPUT / subject
        guide = target / "01-tai-lieu-hoc-day-du.md"
        issues = guide_issues(guide)
        if issues:
            failures.append((guide, issues))
        lessons = sorted((target / "lessons").glob("*.md"))
        lesson_count += len(lessons)
        for lesson in lessons:
            issues = lesson_issues(lesson)
            if issues:
                failures.append((lesson, issues))

        readme = (target / "README.md").read_text(encoding="utf-8")
        for link in re.findall(r"\]\((lessons/[^)]+\.md)\)", readme):
            if not (target / link).exists():
                failures.append((target / "README.md", [f"broken lesson link: {link}"]))

    print(f"subjects={len(SUBJECTS)} lessons={lesson_count} failures={len(failures)}")
    for path, issues in failures:
        print(f"FAIL {path.relative_to(ROOT)}: {'; '.join(issues)}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
