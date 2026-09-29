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
    ("05-information-system-management", "Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)", "Subject_5.md", ((1, 659),)),
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
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    text = "\n".join(lines).strip()
    text = re.sub(r"(?m)^#(#{0,5})\s", lambda m: "#" + m.group(1) + " ", text)
    text = text.replace("<br/>", "\n").replace("<br>", "\n")
    text = re.sub(r"</?mark>", "", text)
    text = text.replace("**Vietnamese:**", "**VI (Vietnamese) (Tiếng Việt):**")
    text = text.replace("**Vietnamese**:", "**VI (Vietnamese) (Tiếng Việt):**")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def ensure_heading_lecture_leads(text: str) -> str:
    """Give list/table/code-heavy headings an explicit beginner-facing lead."""
    lines = text.splitlines()
    enriched: list[str] = []
    in_fence = False
    for index, line in enumerate(lines):
        enriched.append(line)
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or not re.match(r"^#{1,6} ", line):
            continue
        lookahead = index + 1
        while lookahead < len(lines) and not lines[lookahead].strip():
            lookahead += 1
        if lookahead >= len(lines) or lines[lookahead].lstrip().startswith("#"):
            continue
        first = lines[lookahead].lstrip()
        if first.startswith(("-", "*", "|", "```", "---")):
            title = heading_plain(line)
            enriched.extend([
                "",
                f"Phần **{title}** cần được đọc như một bước trong bài giảng: trước hết xác định mục đích, "
                "sau đó nối các ý bên dưới với điều kiện và hệ quả trước khi ghi nhớ từng dòng.",
            ])
    return re.sub(r"\n{3,}", "\n\n", "\n".join(enriched).strip())


def study_guide(title: str, content: str) -> str:
    return f"""# {title}

## 학습 목표 (Mục tiêu học tập)

Phần này đặt mục tiêu của bài, để người mới biết mình cần giải thích được điều gì trước khi đi vào thuật ngữ và ví dụ.

- 시험에서 사용하는 한국어 용어를 영어와 베트남어 뜻까지 함께 인식한다.
- 각 개념을 정의 → 구성요소/절차 → 비교 포인트 → 예시 순서로 설명할 수 있다.
- 앞에서 배운 개념과 뒤의 심화 개념을 연결하여 문제의 조건을 빠르게 해석한다.

> **Câu hỏi trung tâm:** Khi học môn này, người học không chỉ cần nhận ra thuật ngữ Hàn mà còn phải giải thích khái niệm đang giải quyết vấn đề nào, dựa trên điều kiện nào và được dùng để nối sang phần kiến thức nào tiếp theo.

## 권장 학습 순서 (Lộ trình đề xuất)

Phần này là đường đi của bài giảng: đọc theo thứ tự để mỗi mục sau dùng lại hoặc mở rộng tiêu chí của mục trước.

1. 먼저 이 문서의 각 `##` 단원을 순서대로 읽는다.
2. 단원마다 **핵심 키워드**를 소리 내어 읽고, 한국어 원문과 베트남어 설명을 함께 확인한다.
3. 마지막에 `복습 체크리스트`를 점검한 뒤, 세부 lesson 파일에서 헷갈리는 부분을 다시 본다.

> **Nguồn:** tổng hợp từ các Markdown đã generate trong `raw_md/final`, được đối chiếu với các nguồn `raw` và `raw_md` cùng môn. Nội dung gốc được giữ lại; chỉ chuẩn hoá cấu trúc bài học.

> **Quy ước đọc:** thuật ngữ được ưu tiên theo mẫu `한국어 (English) (Tiếng Việt)`. Mỗi ý tiếng Hàn có phần giải thích Việt ngữ liền kề hoặc ngay sau đó; khi gặp từ kỹ thuật trong ngoặc, hãy xem đó là nghĩa cần nhớ khi làm đề.

> **Cách học:** học theo thứ tự các mục; với mỗi mục, xác định khái niệm → cơ chế/quy tắc → ví dụ → mẹo nhớ. Các mục lặp lại ở phần “심화” (nâng cao) dùng để nối kiến thức trước đó với dạng câu hỏi sâu hơn.

> **Mạch giảng:** mỗi mục mở bằng vị trí và mục đích học, đi qua phần giải thích của nguồn, rồi chốt bằng một câu bàn giao sang mục kế tiếp. Hãy đọc các câu nối như một phần của bài giảng: chúng cho biết vì sao kiến thức hiện tại cần thiết trước khi chuyển sang kiến thức sau.

---

{ensure_heading_lecture_leads(clean_source(content))}"""


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


def heading_plain(heading: str) -> str:
    """Return a compact bilingual heading suitable for prose links."""
    return re.sub(r"^#+\s*", "", heading).strip()


def core_headings(lesson: str) -> list[str]:
    return [heading_plain(line) for line in lesson.splitlines() if line.startswith("### ")]


def core_synthesis(core: str, has_table: bool, has_formula: bool,
                   has_example: bool, bullet_count: int) -> str:
    """Give the learner a topic-aware way to interpret the source block."""
    if has_formula and has_table:
        return (
            f"Khi đọc **{core}**, hãy tách hai lớp: bảng giúp đối chiếu các loại hoặc tiêu chí, "
            "còn công thức cần được đọc theo biến, đơn vị và quan hệ giữa các đại lượng. "
            "Cách tách này giúp ta hiểu cơ chế trước khi ghi nhớ ký hiệu."
        )
    if has_formula:
        return (
            f"Với **{core}**, hãy đọc các công thức như một chuỗi lập luận: đại lượng nào được "
            "đưa vào, phép biến đổi nói lên điều gì và kết quả dùng để quyết định ở đâu. "
            "Sau đó mới quay lại các dòng ghi nhớ hoặc ví dụ."
        )
    if has_table:
        return (
            f"Bảng trong **{core}** không phải danh sách rời. Hãy đọc theo từng cột để nhận ra "
            "tiêu chí so sánh, rồi tự diễn đạt bằng một câu: đối tượng nào khác nhau ở điểm nào "
            "và trong điều kiện nào sự khác biệt đó có ý nghĩa."
        )
    if has_example:
        return (
            f"Các ý về **{core}** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. "
            "Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem "
            "quy tắc nào đã dẫn đến kết luận đó."
        )
    if bullet_count:
        return (
            f"Các bullet của **{core}** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom "
            "chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến "
            "ghi chú nguồn thành hiểu biết có thể dùng lại."
        )
    return (
        f"Phần **{core}** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích "
        "và tự chốt bằng một câu giải thích trước khi đi tiếp."
    )


def lesson_topic_question(title: str) -> str:
    """Turn a heading into a concrete beginner-facing question."""
    lowered = title.lower()
    if any(token in lowered for token in ("생명 주기", "life cycle", "phương pháp luận", "방법론")):
        return "một dự án đi qua những giai đoạn nào, mỗi mô hình phân bổ công việc và rủi ro ra sao"
    if any(token in lowered for token in ("요구", "requirement", "yêu cầu")):
        return "một nhu cầu nghiệp vụ được chuyển thành yêu cầu có thể kiểm tra và bàn giao như thế nào"
    if any(token in lowered for token in ("모델", "model", "mô hình", "uml", "üml")):
        return "ta dùng mô hình nào để biểu diễn đối tượng, quan hệ hoặc hành vi, và giới hạn của mỗi cách là gì"
    if any(token in lowered for token in ("데이터", "database", "cơ sở dữ liệu", "sql", "키", "정규화")):
        return "dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng"
    if any(token in lowered for token in ("테스트", "test", "kiểm thử", "품질", "quality")):
        return "ta kiểm tra chất lượng bằng tiêu chí nào, ở thời điểm nào và kết quả kiểm tra dẫn đến quyết định gì"
    if any(token in lowered for token in ("네트워크", "network", "프로토콜", "giao thức")):
        return "các thành phần trao đổi dữ liệu theo lớp, quy tắc và điều kiện nào"
    return "khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì"


def lesson_body_synthesis(title: str, has_table: bool, has_formula: bool,
                          has_example: bool, bullet_count: int,
                          bullet_labels: list[str] | None = None) -> str:
    """Explain how to read a lesson's source block as evidence, not a list."""
    question = lesson_topic_question(title)
    if has_table and has_formula:
        detail = "Bảng cho ta tiêu chí đối chiếu, còn công thức cho ta quan hệ giữa các đại lượng; hãy dùng cả hai để kiểm tra cùng một kết luận."
    elif has_table:
        detail = "Bảng là bằng chứng để so sánh các lựa chọn theo cùng tiêu chí, không phải danh sách cần học thuộc từng ô."
    elif has_formula:
        detail = "Công thức cần được đọc từ ý nghĩa của biến và điều kiện áp dụng trước khi ghi nhớ ký hiệu."
    elif has_example:
        detail = "Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể."
    elif bullet_count:
        detail = "Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng."
    else:
        detail = "Các đoạn prose và thuật ngữ bên dưới cần được đọc như các bước trả lời cho câu hỏi đó."
    labels = [label.strip() for label in (bullet_labels or []) if label.strip()]
    if len(labels) >= 2:
        joined = ", ".join(f"**{label}**" for label in labels[:4])
        relation = (
            f"Trong khối này, {joined} không phải các đáp án rời: chúng lần lượt cho thấy "
            "các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng "
            "và hệ quả của chúng trước khi ghi nhớ tên."
        )
    else:
        relation = ""
    synthesis = "Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp."
    return (
        f"Để đọc **{title}** như một bài học cho người mới, hãy giữ câu hỏi: **{question}?** "
        f"Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. {detail} {relation} {synthesis}"
    ).strip()


def lecture_lesson(lesson: str, previous_title: str | None, next_title: str | None,
                   position: int, total: int) -> str:
    """Add a teaching arc around source material without changing source facts."""
    lines = lesson.splitlines()
    if not lines:
        return lesson
    heading = lines[0]
    title = heading_plain(heading)
    body = lines[1:]
    previous = previous_title or "kiến thức nền của môn"
    next_topic = next_title or "phần tổng kết của môn"

    if previous_title:
        openings = [
            f"Sau khi đã đặt nền bằng **{previous}**, ta chuyển sang **{title}**. Đây là mắt xích {position}/{total} của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.",
            f"Từ **{previous}**, ta đã có điểm tựa để bước vào **{title}**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục {position}/{total} trước khi đi vào chi tiết.",
            f"Ở bước {position}/{total}, **{title}** xuất hiện như phần tiếp nối của **{previous}**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.",
        ]
        opening = openings[(position - 2) % len(openings)]
    else:
        opening = (
            f"Chúng ta bắt đầu mạch học bằng **{title}**. Trước khi đi vào từng thuật ngữ, "
            f"hãy giữ câu hỏi trung tâm: phần kiến thức này giải quyết vấn đề gì và vì sao "
            f"các khái niệm sau phải được đọc trong cùng một bối cảnh? Mục đích của mục "
            f"{position}/{total} là tạo điểm tựa để những phần tiếp theo được hiểu theo quan hệ, "
            "không chỉ được ghi nhớ như danh sách."
        )

    body_text = "\n".join(body)
    body_has_table = "|" in body_text
    body_has_formula = bool(re.search(r"(?:공식|formula|công thức|\s=\s)", body_text, re.I))
    body_has_example = bool(re.search(r"(?:ví dụ|example|예시)", body_text, re.I))
    body_bullets = sum(int(line.lstrip().startswith(("- ", "* "))) for line in body)
    body_bullet_labels = re.findall(r"^\s*[-*]\s+\*\*([^*]+)\*\*\s*[:：]", body_text, re.M)
    enriched: list[str] = [heading, "", opening, "",
                           lesson_body_synthesis(title, body_has_table,
                                                 body_has_formula,
                                                 body_has_example,
                                                 body_bullets,
                                                 body_bullet_labels), ""]
    seen_core = 0
    last_core: str | None = None
    current_has_table = False
    current_has_formula = False
    current_has_example = False
    current_bullets = 0
    for line in body:
        if re.match(r"^#{3,6} ", line):
            core = heading_plain(line)
            if seen_core:
                enriched.extend(["", core_synthesis(last_core or "phần vừa học", current_has_table,
                                                      current_has_formula, current_has_example,
                                                      current_bullets)])
                bridge_templates = [
                    f"Ta vừa chốt **{last_core}** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **{core}** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.",
                    f"Sau khi đọc **{last_core}**, đừng bắt đầu lại từ số không. **{core}** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.",
                    f"**{last_core}** vừa cho ta cách đặt câu hỏi. Bây giờ **{core}** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.",
                ]
                enriched.extend([
                    "",
                    bridge_templates[(seen_core - 1) % len(bridge_templates)],
                    [
                        f"Ở đoạn **{core}**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.",
                        f"Với **{core}**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.",
                        f"Đoạn **{core}** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.",
                    ][(seen_core - 1 + position) % 3],
                    "",
                ])
            else:
                core_openings = [
                    f"Trước hết, ta đặt **{core}** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **{core}** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.",
                    f"Ta bắt đầu phần nội dung bằng **{core}**. Hãy xác định **{core}** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.",
                    f"Để không đọc **{core}** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.",
                ]
                enriched.extend([
                    core_openings[(position - 1) % len(core_openings)],
                    "",
                ])
            seen_core += 1
            last_core = core
            current_has_table = False
            current_has_formula = False
            current_has_example = False
            current_bullets = 0
        enriched.append(line)
        if re.match(r"^#{3,6} ", line):
            core_leads = [
                f"Các ý ngay dưới **{last_core}** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.",
                f"Bây giờ ta đi vào nội dung của **{last_core}**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.",
                f"Phần nguồn của **{last_core}** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.",
            ]
            enriched.extend(["", core_leads[(seen_core - 1 + position) % len(core_leads)], ""])
        else:
            stripped = line.strip().lower()
            current_has_table = current_has_table or stripped.startswith("|")
            current_has_formula = current_has_formula or any(
                token in stripped for token in ("공식", "formula", "công thức", " = ")
            )
            current_has_example = current_has_example or any(
                token in stripped for token in ("ví dụ", "example", "예시")
            )
            current_bullets += int(line.lstrip().startswith(("- ", "* ")))

    if last_core:
        enriched.extend(["", core_synthesis(last_core, current_has_table,
                                              current_has_formula, current_has_example,
                                              current_bullets)])
        core_closings = [
            f"Với **{last_core}**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.",
            f"Điểm chốt của **{last_core}** không nằm ở việc thuộc lòng từng bullet, mà ở việc biết khi nào tiêu chí của nó được áp dụng và khi nào cần đối chiếu với khái niệm khác. Đây là phần bàn giao để đọc tiếp.",
            f"Như vậy, **{last_core}** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.",
        ]
        enriched.extend(["", core_closings[(seen_core - 1) % len(core_closings)]])

    if next_title:
        closings = [
            f"Như vậy, **{title}** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **{next_topic}**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.",
            f"Ta có thể khép mục **{title}** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **{next_topic}**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.",
            f"Điểm chốt của **{title}** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **{next_topic}**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.",
        ]
        closing = closings[(position - 1) % len(closings)]
    else:
        closing = (
            f"Khép lại **{title}**, điều cần giữ lại là mối quan hệ giữa mục đích, cơ chế và "
            "điểm giới hạn của các khái niệm trong nguồn. Khi ôn lại, hãy tự giải thích chúng "
            "bằng một câu hoàn chỉnh rồi đối chiếu với các điểm dễ nhầm trước khi chuyển sang "
            "bài tổng hợp của môn."
        )
    enriched.extend(["", closing])
    return re.sub(r"\n{3,}", "\n\n", "\n".join(enriched).strip())


def lesson_document(title: str, lesson: str, previous_title: str | None,
                    next_title: str | None, position: int, total: int) -> str:
    body_lines = lesson.splitlines()
    heading = body_lines[0] if body_lines else title
    plain = heading_plain(heading)
    # Keep meaningful Korean/English tokens from the bilingual heading; avoid
    # fragments produced by accented Vietnamese characters.
    keyword_source = plain.split("(", 1)[0]
    keywords = re.findall(r"[가-힣]{2,}|\b[A-Z][A-Za-z0-9_-]{2,}\b", keyword_source)
    keyword_text = ", ".join(dict.fromkeys(keywords[:10]))
    next_hint = next_title or "phần tổng hợp của môn"
    objective_vi = (
        f"Mục đích của bài này là hiểu **{plain}** như một khái niệm có thể giải thích và áp dụng: "
        f"nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu "
        f"với **{next_hint}** khi chuyển sang phần tiếp theo."
    )
    return f"""# {title}

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **{plain}**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

{objective_vi}

## 핵심 키워드 (Từ khóa)

{keyword_text or plain}

## 선행·연결 개념 (Kiến thức liên kết)

{f"이 단원은 **{previous_title}**에서 만든 기준을 이어받아 **{plain}**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다." if previous_title else f"이 단원은 **{plain}**을(를) 독립된 암기 항목으로 두지 않고, 이 과목에서 다룰 문제의 출발점으로 삼는다. 먼저 무엇을 설명하는지와 어디까지 적용되는지를 확인한 뒤 세부 규칙으로 들어간다."}

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

{ensure_heading_lecture_leads(lesson)}"""


def subject_readme(title: str, guide_name: str, lesson_rows: list[str]) -> str:
    return f"""# {title}

## Bài học

1. [Tài liệu học đầy đủ]({guide_name})

## Các bài học theo chủ đề

{chr(10).join(lesson_rows)}

## Ghi chú học

Phần này hướng dẫn cách dùng tài liệu như một bài giảng, để ghi chú và thuật ngữ luôn quay về mục tiêu học tập thay vì đứng riêng lẻ.

- Thuật ngữ giữ tiếng Hàn để đối chiếu đề thi, theo sau là English và nghĩa Việt khi nguồn có nêu.
- Đọc ví dụ ngay sau khái niệm vì các bài có nhiều cặp dễ nhầm như `결합도 (Coupling) (độ phụ thuộc)` và `응집도 (Cohesion) (độ gắn kết)`.
- Phần mở rộng/nâng cao không phải nội dung rời: nó nhắc lại kiến thức nền ở mức sâu hơn hoặc trong ngữ cảnh khác.

## Mạch bài giảng

Mỗi lesson mở bằng prerequisite và mục đích, đi qua nội dung nguồn bằng các câu nối tự nhiên, rồi kết thúc bằng điểm chốt và hướng bàn giao sang lesson kế tiếp. Khi học, đừng bỏ qua các đoạn prose này: chúng giải thích vì sao các bullet, bảng và ví dụ được đặt cạnh nhau.

## 복습 체크리스트 (Checklist ôn tập)

Checklist này khép lại bài bằng các câu hỏi kiểm tra; hãy dùng nó để xác nhận mình đã nối khái niệm, điều kiện và ví dụ thành một lời giải thích hoàn chỉnh.

- [ ] 한국어 용어를 보고 English와 Tiếng Việt 의미를 말할 수 있는가?
- [ ] 정의와 목적을 한 문장으로 설명할 수 있는가?
- [ ] 비슷한 개념과 구별 기준을 말할 수 있는가?
- [ ] 예시 또는 간단한 문제에 개념을 적용할 수 있는가?
"""


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    index_rows = []
    for folder, title, source_name, ranges in SUBJECTS:
        source_path = SOURCE / source_name
        content = select_lines(source_path.read_text(encoding="utf-8"), ranges)
        # Rebuild the full guide from the same ordered lesson blocks so the
        # contents page and the detailed guide never disagree.
        ordered_lessons = order_lessons(folder, split_lessons(content))
        lesson_titles = [heading_plain(lesson.splitlines()[0]) for lesson in ordered_lessons]
        lecture_lessons = [
            lecture_lesson(
                lesson,
                lesson_titles[index - 1] if index else None,
                lesson_titles[index + 1] if index + 1 < len(lesson_titles) else None,
                index + 1,
                len(lesson_titles),
            )
            for index, lesson in enumerate(ordered_lessons)
        ]
        ordered_content = "\n\n---\n\n".join(lecture_lessons)
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
        for number, lesson in enumerate(lecture_lessons, start=1):
            heading = lesson.splitlines()[0].removeprefix("## ")
            lesson_name = f"{number:02d}-bai-hoc.md"
            (lessons_dir / lesson_name).write_text(
                lesson_document(
                    heading,
                    lesson,
                    lesson_titles[number - 2] if number > 1 else None,
                    lesson_titles[number] if number < len(lesson_titles) else None,
                    number,
                    len(lesson_titles),
                ),
                encoding="utf-8",
            )
            lesson_rows.append(f"{number}. [{heading}](lessons/{lesson_name})")
        (target / "README.md").write_text(subject_readme(title, guide_name, lesson_rows), encoding="utf-8")
        index_rows.append(f"- [{title}]({folder}/README.md)")

    (OUTPUT / "README.md").write_text(
        "# 정보처리기사 — Bộ tài liệu học\n\n"
        "Tài liệu được chia thành 5 môn. Mỗi folder có một bài học đầy đủ và mục lục học tập; nguồn gốc được bảo toàn trong `raw` và `raw_md`. Mọi lesson và full guide đều được dựng với mạch mở đầu → giải thích → bàn giao → kết thúc; kiểm tra lại bằng `scripts/audit_learning_output.py`.\n\n"
        "## Các môn\n\n"
        "Phần này là mục lục định hướng: chọn môn theo thứ tự học, rồi đi vào lesson để theo dõi mạch giải thích và phần bàn giao.\n\n"
        + "\n".join(index_rows) + "\n\n"
        "## Phạm vi nguồn đã rà soát\n\n"
        "Phần này nêu nguồn và giới hạn biên soạn, giúp người học biết nội dung nào là tài liệu học đã chuẩn hóa trước khi tra cứu nguồn thô.\n\n"
        "- `raw/`: PDF, DOCX và bản tóm tắt gốc.\n"
        "- `raw/notion/`: nội dung Notion theo môn.\n"
        "- `raw_md/generated_markdown*`, `final`, `final_extended`, `merged_subjects`: các lần OCR/dịch/tổng hợp trước.\n"
        "- Các file `final/Subject_*.md` cũ có đoạn ghép nhầm môn. Output đã lọc lại theo ranh giới môn trong `raw/notion/` (Môn 1: 0–72; Môn 2: 73–162; Môn 3: 163–231; Môn 4: 232–314; Môn 5: 315–376), đồng thời giữ các phần mở rộng cùng chủ đề.\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
