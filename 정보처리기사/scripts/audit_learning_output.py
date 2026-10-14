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

def lesson_issues(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    issues: list[str] = []
    if re.search(r"^#{1,6}\s*$", text, flags=re.MULTILINE):
        issues.append("empty heading")
    if "<br" in text or "<mark>" in text or "</mark>" in text:
        issues.append("unresolved markup")
    return issues


def guide_issues(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    sections = re.findall(r"^## (.+)$", text, flags=re.MULTILINE)
    issues: list[str] = []
    if not sections:
        issues.append("no sections")
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
