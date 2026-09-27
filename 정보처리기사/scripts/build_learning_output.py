from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "raw_md" / "final"
OUTPUT = ROOT / "output"

SUBJECTS = [
    # (folder, title, source file, inclusive/exclusive line ranges).  The old
    # generated files had several subjects concatenated into one file; these
    # ranges retain only the sections that match the official subject boundary.
    ("01-software-design", "Môn 1 — 소프트웨어 설계 (Software Design) (Thiết kế phần mềm)", "Subject_1.md", ((1, 627), (929, None))),
    ("02-software-development", "Môn 2 — 소프트웨어 개발 (Software Development) (Phát triển phần mềm)", "Subject_2.md", ((1, 526), (1083, 1464), (1731, None))),
    ("03-database-construction", "Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)", "Subject_3.md", ((1, 315), (437, None))),
    ("04-programming-language", "Môn 4 — 프로그래밍 언어 활용 (Programming Language Application) (Ứng dụng ngôn ngữ lập trình)", "Subject_4.md", ((23, 331), (349, 681), (1312, None))),
    ("05-information-system-management", "Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)", "Subject_5.md", ((1, 659), (2617, None))),
]

# A stable thematic order makes the merged source easier to study.  Unknown or
# supplemental headings retain their original order at the end.
THEME_ORDER = {
    "01-software-design": ["생명 주기", "소프트웨어 공학", "요구사항", "현행 시스템", "모델링", "UML", "사용자 인터페이스", "UI", "아키텍처", "객체지향", "모듈", "품질", "디자인 패턴", "인터페이스", "미들웨어"],
    "02-software-development": ["자료 구조", "스택", "큐", "트리", "그래프", "수식", "정렬", "검색", "해싱", "모듈", "형상 관리", "패키징", "빌드", "DRM", "테스트", "성능", "인터페이스"],
    "03-database-construction": ["설계", "데이터 모델", "E-R", "키", "무결성", "관계대수", "정규화", "이상", "트랜잭션", "SQL", "데이터 조작", "뷰", "인덱스", "분산", "스토리지", "암호화"],
    "04-programming-language": ["언어 기초", "데이터 타입", "변수", "연산자", "입출력", "제어문", "배열", "포인터", "Python", "라이브러리", "예외", "운영체제", "메모리", "프로세스", "스레드", "네트워크", "OSI", "IP"],
    "05-information-system-management": ["방법론", "프레임워크", "프로젝트", "산정", "품질", "표준", "데이터 통신", "전송", "다중화", "오류", "네트워크", "프로토콜", "데이터베이스", "보안", "암호화", "해킹"],
}


def select_lines(text: str, ranges: tuple[tuple[int, int | None], ...]) -> str:
    """Keep subject-specific blocks from a formerly concatenated Markdown file."""
    lines = text.splitlines()
    blocks = []
    for start, end in ranges:
        blocks.append("\n".join(lines[start - 1:end]))
    return "\n\n---\n\n".join(block for block in blocks if block.strip())


def clean_source(text: str) -> str:
    # The source already contains Korean and Vietnamese explanations. Normalize its
    # presentation without removing study content, examples, tables or mnemonics.
    lines = text.splitlines()
    lines = [line.rstrip() for line in lines]
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    text = "\n".join(lines).strip()
    text = re.sub(r"(?m)^#(#{0,5})\s", lambda m: "#" + m.group(1) + " ", text)
    text = text.replace("**Vietnamese:**", "**VI (Vietnamese) (Tiếng Việt):**")
    text = text.replace("**Vietnamese**:", "**VI (Vietnamese) (Tiếng Việt):**")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def study_guide(title: str, content: str) -> str:
    return f"""# {title}

## 학습 목표 (Mục tiêu học tập)

- 시험에서 사용하는 한국어 용어를 영어와 베트남어 뜻까지 함께 인식한다.
- 각 개념을 정의 → 구성요소/절차 → 비교 포인트 → 예시 순서로 설명할 수 있다.
- 앞에서 배운 개념과 뒤의 심화 개념을 연결하여 문제의 조건을 빠르게 해석한다.

## 권장 학습 순서 (Lộ trình đề xuất)

1. 먼저 이 문서의 각 `##` 단원을 순서대로 읽는다.
2. 단원마다 **핵심 키워드**를 소리 내어 읽고, 한국어 원문과 베트남어 설명을 함께 확인한다.
3. 마지막에 `복습 체크리스트`를 점검한 뒤, 세부 lesson 파일에서 헷갈리는 부분을 다시 본다.

> **Nguồn:** tổng hợp từ các Markdown đã generate trong `raw_md/final`, được đối chiếu với các nguồn `raw` và `raw_md` cùng môn. Nội dung gốc được giữ lại; chỉ chuẩn hoá cấu trúc bài học.

> **Quy ước đọc:** thuật ngữ được ưu tiên theo mẫu `한국어 (English) (Tiếng Việt)`. Mỗi ý tiếng Hàn có phần giải thích Việt ngữ liền kề hoặc ngay sau đó; khi gặp từ kỹ thuật trong ngoặc, hãy xem đó là nghĩa cần nhớ khi làm đề.

> **Cách học:** học theo thứ tự các mục; với mỗi mục, xác định khái niệm → cơ chế/quy tắc → ví dụ → mẹo nhớ. Các mục lặp lại ở phần “심화” (nâng cao) dùng để nối kiến thức trước đó với dạng câu hỏi sâu hơn.

---

{clean_source(content)}"""


def split_lessons(content: str) -> list[str]:
    """Make one focused lesson per level-2 source heading."""
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


def lesson_document(title: str, lesson: str) -> str:
    body_lines = lesson.splitlines()
    heading = body_lines[0] if body_lines else title
    plain = re.sub(r"^##\s*", "", heading).strip()
    # Keep meaningful Korean/English tokens from the bilingual heading; avoid
    # fragments produced by accented Vietnamese characters.
    keyword_source = plain.split("(", 1)[0]
    keywords = re.findall(r"[가-힣]{2,}|\b[A-Z][A-Za-z0-9_-]{2,}\b", keyword_source)
    keyword_text = ", ".join(dict.fromkeys(keywords[:10]))
    return f"""# {title}

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **{plain}**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

{keyword_text or plain}

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

{lesson}"""


def subject_readme(title: str, guide_name: str, lesson_rows: list[str]) -> str:
    return f"""# {title}

## Bài học

1. [Tài liệu học đầy đủ]({guide_name})

## Các bài học theo chủ đề

{chr(10).join(lesson_rows)}

## Ghi chú học

- Thuật ngữ giữ tiếng Hàn để đối chiếu đề thi, theo sau là English và nghĩa Việt khi nguồn có nêu.
- Đọc ví dụ ngay sau khái niệm vì các bài có nhiều cặp dễ nhầm như `결합도 (Coupling) (độ phụ thuộc)` và `응집도 (Cohesion) (độ gắn kết)`.
- Phần mở rộng/nâng cao không phải nội dung rời: nó nhắc lại kiến thức nền ở mức sâu hơn hoặc trong ngữ cảnh khác.

## 복습 체크리스트 (Checklist ôn tập)

- [ ] 한국어 용어를 보고 English와 Tiếng Việt 의미를 말할 수 있는가?
- [ ] 정의와 목적을 한 문장으로 설명할 수 있는가?
- [ ] 비슷한 개념과 구별 기준을 말할 수 있는가?
- [ ] 예시 또는 간단한 문제에 개념을 적용할 수 있는가?
"""


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    index_rows = []
    coverage_rows = []
    for folder, title, source_name, ranges in SUBJECTS:
        source_path = SOURCE / source_name
        content = select_lines(source_path.read_text(encoding="utf-8"), ranges)
        # Rebuild the full guide from the same ordered lesson blocks so the
        # contents page and the detailed guide never disagree.
        ordered_lessons = order_lessons(folder, split_lessons(content))
        ordered_content = "\n\n---\n\n".join(ordered_lessons)
        target = OUTPUT / folder
        target.mkdir(exist_ok=True)
        guide_name = "01-tai-lieu-hoc-day-du.md"
        (target / guide_name).write_text(study_guide(title, ordered_content), encoding="utf-8")
        lessons_dir = target / "lessons"
        lessons_dir.mkdir(exist_ok=True)
        for old_lesson in lessons_dir.glob("*.md"):
            old_lesson.unlink()
        lesson_rows = []
        lessons = ordered_lessons
        coverage_rows.append(
            f"| {title} | {len(lessons)} | `{source_name}` | 필기 범위 검토 완료 |")
        for number, lesson in enumerate(lessons, start=1):
            heading = lesson.splitlines()[0].removeprefix("## ")
            lesson_name = f"{number:02d}-bai-hoc.md"
            (lessons_dir / lesson_name).write_text(lesson_document(heading, lesson), encoding="utf-8")
            lesson_rows.append(f"{number}. [{heading}](lessons/{lesson_name})")
        readme = subject_readme(title, guide_name, lesson_rows)
        if folder == "01-software-design":
            readme += (
                "\n## Bài học bổ sung / Deep Dive\n\n"
                "- [Vòng đời và phương pháp phát triển phần mềm](01-vong-doi-va-phuong-phap-phat-trien.md)\n"
            )
        (target / "README.md").write_text(readme, encoding="utf-8")
        index_rows.append(f"- [{title}]({folder}/README.md)")

    (OUTPUT / "README.md").write_text(
        "# 정보처리기사 — Bộ tài liệu học\n\n"
        "Tài liệu được chia thành 5 môn. Mỗi folder có một bài học đầy đủ và mục lục học tập; nguồn gốc được bảo toàn trong `raw` và `raw_md`.\n\n"
        "## Phạm vi học\n\n"
        "- Output này tập trung vào **정보처리기사 필기** và giữ ranh giới 5 môn theo cấu trúc đề thi.\n"
        "- Nội dung **실기 (정보처리 실무)** chưa được xem là phạm vi hoàn tất của bộ output này; không dùng bộ 필기 này thay cho lộ trình 실기 riêng.\n"
        "- Bản source hiện đối chiếu theo 출제기준 Q-Net giai đoạn **2023.1.1–2025.12.31**; đây không phải cam kết cho kỳ thi 2026. Trước khi thi, hãy kiểm tra bản mới nhất trên [Q-Net](https://www.q-net.or.kr/cst006.do?artlSeq=5210765&brdId=Q006&code=1202&gId=&gSite=Q&id=cst00602).\n\n"
        "- [Coverage matrix / ma trận độ phủ](COVERAGE_MATRIX.md) ghi số lesson, source canonical và trạng thái rà soát của từng môn.\n\n"
        "- [Research register / sổ nguồn nghiên cứu](RESEARCH_REGISTER.md) ghi nguồn Q-Net và tài liệu kỹ thuật dùng để fact-check.\n\n"
        "## Các môn\n\n" + "\n".join(index_rows) + "\n\n"
        "## Phạm vi nguồn đã rà soát\n\n"
        "- `raw/`: PDF, DOCX và bản tóm tắt gốc.\n"
        "- `raw/notion/`: nội dung Notion theo môn.\n"
        "- `raw_md/generated_markdown*`, `final`, `final_extended`, `merged_subjects`: các lần OCR/dịch/tổng hợp trước.\n"
        "- Các file `final/Subject_*.md` cũ có đoạn ghép nhầm môn. Output đã lọc lại theo ranh giới môn trong `raw/notion/` (Môn 1: 0–72; Môn 2: 73–162; Môn 3: 163–231; Môn 4: 232–314; Môn 5: 315–376), đồng thời giữ các phần mở rộng cùng chủ đề.\n",
        encoding="utf-8",
    )
    (OUTPUT / "COVERAGE_MATRIX.md").write_text(
        "# 정보처리기사 필기 — Coverage Matrix\n\n"
        "> Baseline của branch: 출제기준 Q-Net 2023.1.1–2025.12.31. Kiểm tra lại Q-Net trước kỳ thi; ma trận này không xác nhận syllabus 2026.\n\n"
        "| Môn | Lessons | Source canonical | Status |\n"
        "|---|---:|---|---|\n"
        + "\n".join(coverage_rows)
        + "\n\n## Quality gates\n\n"
        "- Link nội bộ được kiểm tra bởi `scripts/audit_learning_output.py`.\n"
        "- Output được regenerate từ `raw_md/final/` bằng `scripts/build_learning_output.py`.\n"
        "- `실기` không nằm trong phạm vi hoàn tất của output này.\n",
        encoding="utf-8",
    )
    (OUTPUT / "RESEARCH_REGISTER.md").write_text(
        "# 정보처리기사 필기 — Research Register\n\n"
        "이 문서는 시험 범위의 canonical source와 기술 사실 확인에 사용한 1차/공식 자료를 구분한다.\n\n"
        "## 시험 범위\n\n"
        "- [Q-Net 정보처리기사 출제기준(2023.1.1~2025.12.31)](https://www.q-net.or.kr/cst006.do?artlSeq=5210765&brdId=Q006&code=1202&gId=&gSite=Q&id=cst00602) — 시험 범위 baseline.\n\n"
        "## 기술 사실 확인\n\n"
        "- [RFC 8200 IPv6 Specification](https://www.rfc-editor.org/rfc/rfc8200) — 128-bit addressing, anycast, header/MTU semantics.\n"
        "- [Oracle Java Language Specification](https://docs.oracle.com/javase/specs/jls/se26/html/jls-4.html) — primitive types, `char`, `boolean` and numeric widths.\n\n"
        "- [PostgreSQL SELECT documentation](https://www.postgresql.org/docs/17/queries-order.html) — `WHERE`/`GROUP BY`/`HAVING`/`ORDER BY` reasoning and result ordering.\n"
        "- [Python control-flow tutorial](https://docs.python.org/3/tutorial/controlflow.html) — `for`, `continue`, `break` and trace behavior.\n"
        "- [OWASP CSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/CSRF_Prevention_Cheat_Sheet.html) — token and SameSite defense limits.\n\n"
        "외부 자료는 기술 사실을 검증하기 위한 참고이며, 실제 응시 전에는 Q-Net 출제기준의 최신 게시물을 우선한다.\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
