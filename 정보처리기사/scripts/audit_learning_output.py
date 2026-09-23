from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output"
EXPECTED_SUBJECTS = {
    "01-software-design",
    "02-software-development",
    "03-database-construction",
    "04-programming-language",
    "05-information-system-management",
}
REQUIRED_LESSON_HEADINGS = (
    "## 학습 목표",
    "## 핵심 키워드",
    "## 선행·연결 개념",
    "## 읽는 방법",
)
FORBIDDEN_CONTENT = (
    "보헴이 제시한 고전적 생명 주기 모형",
    "EOF",
    ", , .",
)


def markdown_files():
    return sorted(OUTPUT.rglob("*.md"))


def check_links(path: Path, errors: list[str]) -> int:
    text = path.read_text(encoding="utf-8")
    count = 0
    for match in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", text):
        target = match.group(1).split("#", 1)[0].strip()
        if not target or re.match(r"^(https?:|mailto:|tel:)", target):
            continue
        count += 1
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            errors.append(f"{path.relative_to(ROOT)}: broken link {target}")
    return count


def main() -> int:
    errors: list[str] = []
    files = markdown_files()
    lessons = sorted(OUTPUT.glob("*/lessons/*.md"))

    actual_subjects = {path.parent.parent.name for path in lessons}
    missing_subjects = EXPECTED_SUBJECTS - actual_subjects
    if missing_subjects:
        errors.append(f"missing subject folders: {', '.join(sorted(missing_subjects))}")

    root_readme = OUTPUT / "README.md"
    root_text = root_readme.read_text(encoding="utf-8") if root_readme.exists() else ""
    for required in ("정보처리기사 필기", "Q-Net", "실기"):
        if required not in root_text:
            errors.append(f"output/README.md: missing scope marker {required}")

    total_links = 0
    for path in files:
        total_links += check_links(path, errors)
        text = path.read_text(encoding="utf-8")
        for forbidden in FORBIDDEN_CONTENT:
            if forbidden in text:
                errors.append(f"{path.relative_to(ROOT)}: stale factual error {forbidden}")

    for lesson in lessons:
        text = lesson.read_text(encoding="utf-8")
        for heading in REQUIRED_LESSON_HEADINGS:
            if heading not in text:
                errors.append(f"{lesson.relative_to(ROOT)}: missing heading {heading}")
        last_nonempty = next((line.strip() for line in reversed(text.splitlines()) if line.strip()), "")
        if last_nonempty.startswith("# "):
            errors.append(f"{lesson.relative_to(ROOT)}: orphan top-level heading at EOF: {last_nonempty}")

    print(f"subjects={len(actual_subjects)} lessons={len(lessons)} markdown={len(files)} links={total_links}")
    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1

    print("A/A+ baseline audit passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
