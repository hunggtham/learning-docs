from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "raw_md" / "final"
OUTPUT = ROOT / "output"

SUBJECTS = [
    ("01-software-design", "Môn 1 — 소프트웨어 설계 (Software Design) (Thiết kế phần mềm)", "Subject_1.md", ((1, 627), (929, None))),
    ("02-software-development", "Môn 2 — 소프트웨어 개발 (Software Development) (Phát triển phần mềm)", "Subject_2.md", ((1, 526), (1083, 1464), (1731, None))),
    ("03-database-construction", "Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)", "Subject_3.md", ((1, 315), (437, None))),
    ("04-programming-language", "Môn 4 — 프로그래밍 언어 활용 (Programming Language Application) (Ứng dụng ngôn ngữ lập trình)", "Subject_4.md", ((23, 331), (349, 681), (1312, None))),
    ("05-information-system-management", "Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)", "Subject_5.md", ((1, 659), (2617, None))),
]

THEME_ORDER = {
    "01-software-design": ["생명 주기", "소프트웨어 공학", "요구사항", "현행 시스템", "모델링", "UML", "사용자 인터페이스", "UI", "아키텍처", "객체지향", "모듈", "품질", "디자인 패턴", "인터페이스", "미들웨어"],
    "02-software-development": ["자료 구조", "스택", "큐", "트리", "그래프", "수식", "정렬", "검색", "해싱", "모듈", "형상 관리", "패키징", "빌드", "DRM", "테스트", "성능", "인터페이스"],
    "03-database-construction": ["설계", "데이터 모델", "E-R", "키", "무결성", "관계대수", "정규화", "이상", "트랜잭션", "SQL", "데이터 조작", "뷰", "인덱스", "분산", "스토리지", "암호화"],
    "04-programming-language": ["언어 기초", "데이터 타입", "변수", "연산자", "입출력", "제어문", "배열", "포인터", "Python", "라이브러리", "예외", "운영체제", "메모리", "프로세스", "스레드", "네트워크", "OSI", "IP"],
    "05-information-system-management": ["방법론", "프레임워크", "프로젝트", "산정", "품질", "표준", "데이터 통신", "전송", "다중화", "오류", "네트워크", "프로토콜", "데이터베이스", "보안", "암호화", "해킹"],
}


def select_lines(text: str, ranges: tuple[tuple[int, int | None], ...]) -> str:
    lines = text.splitlines()
    blocks = ["\n".join(lines[start - 1:end]) for start, end in ranges]
    return "\n\n---\n\n".join(block for block in blocks if block.strip())


def clean_source(text: str) -> str:
    """Normalize source markup without adding teaching prose."""
    lines = [line.rstrip() for line in text.splitlines()]
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    text = "\n".join(lines).strip()
    text = re.sub(r"(?m)^#(#{0,5})\s", lambda match: "#" + match.group(1) + " ", text)
    text = text.replace("<br/>", "\n").replace("<br>", "\n")
    text = re.sub(r"</?mark>", "", text)
    text = text.replace("**Vietnamese:**", "**VI (Vietnamese) (Tiếng Việt):**")
    text = text.replace("**Vietnamese**:", "**VI (Vietnamese) (Tiếng Việt):**")
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


def split_lessons(content: str) -> list[str]:
    chunks = re.split(r"(?=^## )", content, flags=re.MULTILINE)
    return [clean_source(chunk) for chunk in chunks if chunk.lstrip().startswith("## ")]


def order_lessons(folder: str, lessons: list[str]) -> list[str]:
    themes = THEME_ORDER.get(folder, [])

    def key(lesson: str) -> tuple[int, int]:
        heading = lesson.splitlines()[0] if lesson.splitlines() else ""
        for index, theme in enumerate(themes):
            if theme.lower() in heading.lower():
                return (index, 0)
        return (len(themes), lessons.index(lesson))

    return sorted(lessons, key=key)


def heading_plain(heading: str) -> str:
    return re.sub(r"^#+\s*", "", heading).strip()


def study_guide(title: str, content: str) -> str:
    return f"# {title}\n\n{content.strip()}\n"


def lesson_document(title: str, lesson: str) -> str:
    return f"# {title}\n\n{lesson.strip()}\n"


def subject_readme(title: str, guide_name: str, lesson_rows: list[str]) -> str:
    return (
        f"# {title}\n\n"
        "## Bài học\n\n"
        f"1. [Tài liệu học đầy đủ]({guide_name})\n\n"
        "## Các bài học theo chủ đề\n\n"
        + "\n".join(lesson_rows)
        + "\n"
    )


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    index_rows: list[str] = []
    coverage_rows: list[str] = []

    for folder, title, source_name, ranges in SUBJECTS:
        source_path = SOURCE / source_name
        content = select_lines(source_path.read_text(encoding="utf-8"), ranges)
        ordered_lessons = order_lessons(folder, split_lessons(content))
        ordered_content = "\n\n---\n\n".join(ordered_lessons)

        target = OUTPUT / folder
        target.mkdir(exist_ok=True)
        guide_name = "01-tai-lieu-hoc-day-du.md"
        (target / guide_name).write_text(study_guide(title, ordered_content), encoding="utf-8")

        lessons_dir = target / "lessons"
        lessons_dir.mkdir(exist_ok=True)
        lesson_rows: list[str] = []
        for number, lesson in enumerate(ordered_lessons, start=1):
            heading = heading_plain(lesson.splitlines()[0])
            lesson_name = f"{number:02d}-bai-hoc.md"
            (lessons_dir / lesson_name).write_text(
                lesson_document(heading, lesson), encoding="utf-8"
            )
            lesson_rows.append(f"{number}. [{heading}](lessons/{lesson_name})")

        (target / "README.md").write_text(
            subject_readme(title, guide_name, lesson_rows), encoding="utf-8"
        )
        index_rows.append(f"- [{title}]({folder}/README.md)")
        coverage_rows.append(
            f"| {title} | {len(ordered_lessons)} | `{source_name}` | source-preserving |"
        )

    (OUTPUT / "README.md").write_text(
        "# 정보처리기사 — Bộ tài liệu học\n\n"
        "## Các môn\n\n"
        + "\n".join(index_rows)
        + "\n",
        encoding="utf-8",
    )
    (OUTPUT / "COVERAGE_MATRIX.md").write_text(
        "# 정보처리기사 필기 — Coverage Matrix\n\n"
        "| Môn | Lessons | Source canonical | Status |\n"
        "|---|---:|---|---|\n"
        + "\n".join(coverage_rows)
        + "\n",
        encoding="utf-8",
    )
    (OUTPUT / "RESEARCH_REGISTER.md").write_text(
        "# 정보처리기사 필기 — Research Register\n\n"
        "- [Q-Net 정보처리기사 출제기준](https://www.q-net.or.kr/)\n"
        "- [RFC Editor](https://www.rfc-editor.org/)\n"
        "- [Oracle Java Language Specification](https://docs.oracle.com/javase/specs/)\n"
        "- [PostgreSQL Documentation](https://www.postgresql.org/docs/)\n"
        "- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
