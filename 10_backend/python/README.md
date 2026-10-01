# Thư viện kiến thức Python (Python knowledge library / 파이썬 지식 라이브러리)

> **Mạch đọc:** [README backend domain](../README.md) là owner cấp domain; thư mục này sở hữu các chapter Python và case study liên quan. **Mạch học và phụ thuộc** đi từ execution/object model tới packaging, concurrency và production; phần ranh giới chỉ rõ khi nào phải quay về Computer Science.

Thư viện kiến thức Python (Python knowledge library / 파이썬 지식 라이브러리) là bộ tài liệu chuẩn gốc (canonical / 정본) cho kiến thức Python trong repository này. Mục tiêu không phải ghi nhớ cú pháp mà là hiểu mô hình thực thi, mô hình đối tượng (object / 객체), mô hình dữ liệu (data model / 데이터 모델), hệ thống import, hệ kiểu (type system / 타입 시스템), tính đồng thời (concurrency / 동시성) và cách Python vận hành trong môi trường vận hành (production / 운영 환경).

Baseline hiện tại là Python 3.14.7, bản stable phát hành ngày 2026-08-05. Ngày kiểm chứng: 2026-09-22. Những phần nói riêng về CPython luôn được phân biệt với ngữ nghĩa (semantics / 의미론) của ngôn ngữ Python, vì CPython là hiện thực (implementation / 구현) phổ biến nhất chứ không phải toàn bộ định nghĩa của Python.

## Mạch học (learning flow / 학습 흐름) và phụ thuộc (dependency / 의존성)

```text
Part 1 — execution / name binding / object / data / function
    ↓
Part 2 — data model / protocol / abstraction / standard library
    ↓
Part 3 — project / packaging / testing / concurrency / production
    ↓
Part 4 — runtime internals / attribute lookup / object-class creation /
         performance / interpreters / architecture / evolution
    ↓
Engineering Case Studies — symptom → invariant → mechanism → evidence → design
```

1. [Part 1 — Beginner: Execution, object model, dữ liệu và hàm](python_01_beginner.md)
2. [Part 2 — Intermediate: Data model, abstraction và standard-library engineering](python_02_intermediate.md)
3. [Part 3 — Senior: Packaging, testing, concurrency và production engineering](python_03_senior.md)
4. [Part 4 — Master: Runtime internals, performance, architecture và modern/legacy evolution](python_04_master.md)
5. [Engineering Case Studies — reasoning xuyên nhiều layer](ENGINEERING_CASE_STUDIES.md)
6. [Glossary Việt–Anh–Hàn](GLOSSARY.md)
7. [Coverage & final audit](COVERAGE_AUDIT.md)

Bốn part là bốn chuẩn gốc (canonical / 정본) chapter lớn. Cấu trúc giữ convention Beginner → Intermediate → cấp cao (senior / 시니어) → Master đã dùng ở Java/JavaScript, nhưng nội dung bên trong đi theo phụ thuộc (dependency / 의존성) tự nhiên của Python thay vì chia chapter chỉ để tăng số lượng. Pythonic idiom, anti-pattern, internals và cấp cao (senior / 시니어) ghi chú (note / 노트) được đặt cạnh concept mà chúng tác động, không tách thành tệp (file / 파일) rời gây duplicate.

`ENGINEERING_CASE_STUDIES.md` không phải Part 5. Nó là lớp tích hợp sau bốn part: cùng một tình huống môi trường vận hành (production / 운영 환경) được nhìn qua đối tượng (object / 객체) ngữ nghĩa (semantics / 의미론), import, packaging, tính đồng thời (concurrency / 동시성), bảo mật (security / 보안) và khả năng quan sát (observability / 관측 가능성) để luyện lập luận nhân quả (causal reasoning / 인과적 추론). Các trường hợp (case / 사례) không định nghĩa lại concept đã có; chúng chỉ nối các concept thành đường suy luận từ hiện tượng quan sát được tới bất biến (invariant / 불변식), cơ chế (mechanism / 메커니즘) và bằng chứng (evidence / 증거).

Part 1 là prerequisite trực tiếp của Part 2. Part 3 có thể được đọc sớm nếu mục tiêu là dự án (project / 프로젝트)/triển khai (deployment / 배포), nhưng các phần testing, import, tính đồng thời (concurrency / 동시성) và bộ nhớ (memory / 메모리) đều giả định mô hình tư duy (mental model / 사고 모델) đối tượng (object / 객체)/tham chiếu (reference / 참조) từ Part 1–2. Part 4 là lớp đào sâu; nó không thay thế ba phần trước mà giải thích vì sao các hành vi (behavior / 동작) đã học xuất hiện ở thời gian chạy (runtime / 런타임) và môi trường vận hành (production / 운영 환경).

> **Chuyển mạch:** Mạch học xác định prerequisite giữa bốn part; ranh giới domain nói rõ phần nào thuộc Python và phần nào phải quay về Computer Science. Sau đó Quy ước thuật ngữ giữ cách dùng tiếng Việt nhất quán.

## Ranh giới (boundary / 경계) với các lĩnh vực (domain / 도메인) khác

Python cốt lõi (core / 핵심) ở đây giải thích ngôn ngữ, CPython khi cần thiết, thư viện chuẩn (standard library / 표준 라이브러리) và môi trường vận hành (production / 운영 환경) practice gắn trực tiếp với Python. FastAPI, AI khung phần mềm (framework / 프레임워크) và kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링) khung phần mềm (framework / 프레임워크) không được kéo sâu vào thư viện (library / 라이브러리) chỉ vì chúng dùng tệp (file / 파일) `.py`.

Các case study Python dùng những ví dụ được viết ngay trong từng Part để nối `asyncio`, `dataclass`, `pathlib`, `subprocess`, HTTP I/O, cấu hình môi trường và testing với mã thật. Thư mục `automation/` hiện chỉ giữ công cụ kiểm tra cấu trúc repository; nó không còn là owner của nội dung học hay một worker sinh tài liệu.

Các concept nền rộng hơn như tiến trình (process / 프로세스)/luồng thực thi (thread / 스레드), scheduling, bộ nhớ (memory / 메모리) hierarchy, networking, dữ liệu (data / 데이터) structures và kỹ nghệ phần mềm (software engineering / 소프트웨어 공학) thuộc [Computer Science Knowledge Library](../../computer_science/README.md). Python chapter giải thích đủ để đọc liền mạch rồi cầu nối (bridge / 브리지) sang chuẩn gốc (canonical / 정본) lĩnh vực (domain / 도메인) đó khi cần chiều sâu xuyên tầng.

Multiple interpreters, free-threaded CPython và tiến trình (process / 프로세스)/luồng thực thi (thread / 스레드) thực thi (execution / 실행) được giải thích ở Python ranh giới (boundary / 경계) vì chúng thay đổi hành vi (behavior / 동작) của Python thời gian chạy (runtime / 런타임). Những nguyên lý rộng hơn về isolation, scheduling, trạng thái dùng chung (shared state / 공유 상태) và IPC vẫn thuộc Khoa học máy tính (computer science / 컴퓨터 과학); tài liệu Python chỉ giữ phần cần để hiểu quyết định kỹ thuật (engineering / 엔지니어링) trong Python.

> **Chuyển mạch:** Quy ước thuật ngữ giữ tên API và thuật ngữ tra cứu ổn định; phần Hiện đại Python và legacy dùng quy ước đó để phân biệt hành vi theo phiên bản.

## Quy ước thuật ngữ

Giải thích chính dùng tiếng Việt tự nhiên. Mỗi lần thuật ngữ quan trọng xuất hiện, dùng dạng `tiếng Việt (English term / 한국어 용어)` theo ánh xạ trong [Glossary](GLOSSARY.md). Tên API, mô-đun (module / 모듈), lớp (class / 클래스), phương thức (method / 메서드), command, identifier, tiêu chuẩn (standard / 표준), sản phẩm (product / 제품) và mã (code / 코드) như `asyncio`, `Path`, `__iter__`, `pyproject.toml` giữ nguyên bản gốc.

Khi đọc chapter, ưu tiên hiểu quan hệ giữa khái niệm và cơ chế (mechanism / 메커니즘). Glossary dùng để nhận diện thuật ngữ, không thay thế phần giải thích trong chapter.

> **Chuyển mạch:** Phân biệt modern và legacy giúp người học biết khi nào một claim phụ thuộc phiên bản; **Cách dùng thư viện** chuyển claim đó thành quyết định đọc và kiểm chứng trong dự án.

## Hiện đại (modern / 현대적) Python và legacy

Baseline của thư viện (library / 라이브러리) là Python 3.14. Codebase thực tế vẫn có thể mục tiêu (target / 대상) Python 3.8–3.13 hoặc mang mẫu (pattern / 패턴) cũ hơn; tài liệu chỉ nhắc legacy khi nó giúp giải thích mã (code / 코드) đang tồn tại hoặc di chuyển (migration / 마이그레이션) concern. Ví dụ, cú pháp (syntax / 문법) generic `class Box[T]` là hiện đại (modern / 현대적) cú pháp (syntax / 문법) từ Python 3.12, trong khi `TypeVar` + `Generic` vẫn cần biết để đọc thư viện (library / 라이브러리) hỗ trợ phiên bản (version / 버전) cũ.

Python 3.14 đưa free-threaded CPython thành cấu hình được hỗ trợ chính thức nhưng vẫn không phải bản dựng (build / 빌드) mặc định duy nhất. Vì vậy thư viện (library / 라이브러리) luôn tách hai mô hình tư duy (mental model / 사고 모델): CPython mặc định có GIL và free-threaded CPython không GIL. Không suy ra rằng mọi Python 3.14 chạy luồng thực thi (thread / 스레드) Python bytecode song song, cũng không dùng GIL như một lý do để bỏ qua synchronization của dùng chung (shared / 공유) mutable trạng thái (state / 상태).

Python 3.14 cũng đưa `concurrent.interpreters` và `InterpreterPoolExecutor` vào công khai (public / 공개) standard-library surface. Multiple interpreters tạo isolation của trình thông dịch (interpreter / 인터프리터) trạng thái (state / 상태) trong cùng tiến trình (process / 프로세스) và có thể kết hợp với threads để đạt multi-core, nhưng không phải tiến trình (process / 프로세스) isolation và không cho phép chia sẻ mutable Python objects tùy ý. Đây là một mô hình thực thi (execution model / 실행 모델) riêng cần phân biệt với luồng thực thi (thread / 스레드) pool, tiến trình (process / 프로세스) pool và free-threaded threads.

Trên POSIX hỗ trợ phù hợp, Python 3.14 dùng `forkserver` làm multiprocessing start phương thức (method / 메서드) mặc định thay cho `fork`. mã (code / 코드) phụ thuộc `fork` phải chọn tường minh (explicit / 명시적) ngữ cảnh (context / 맥락) thay vì coi historical default là ngôn ngữ (language / 언어) guarantee. Packaging cũng cần tách dự án (project / 프로젝트) siêu dữ liệu (metadata / 메타데이터), phụ thuộc (dependency / 의존성) groups, resolved triển khai (deployment / 배포) môi trường (environment / 환경) và nhị phân (binary / 이진) wheel/ABI tính tương thích (compatibility / 호환성) thành các lớp khác nhau.

> **Chuyển mạch:** Cách dùng thư viện nêu lúc nào cần đọc Part 1–4 và case study; Nguồn chuẩn gốc cung cấp tài liệu chính thức để kiểm tra claim theo phiên bản.

## Cách dùng thư viện (library / 라이브러리)

Nếu mới học Python, đọc Part 1 → 2 và tự chạy các ví dụ nhỏ. Khi bắt đầu dự án (project / 프로젝트) thật, chuyển sang Part 3 để hiểu môi trường (environment / 환경), phụ thuộc (dependency / 의존성), testing, tính đồng thời (concurrency / 동시성) và môi trường vận hành (production / 운영 환경) ranh giới (boundary / 경계). Part 4 phù hợp khi cần điều tra hiệu năng (performance / 성능), bộ nhớ (memory / 메모리), import hành vi (behavior / 동작), descriptor/attribute lookup, `__new__`/lớp (class / 클래스) creation, free-threading, multiple interpreters, async internals hoặc rà soát (review / 검토) kiến trúc (architecture / 아키텍처).

Sau mỗi cụm lớn, đọc trường hợp (case / 사례) tương ứng trong `ENGINEERING_CASE_STUDIES.md`. Ví dụ sau đối tượng (object / 객체)/bản sao (copy / 복사) hãy đọc trường hợp (case / 사례) 1; sau import đọc trường hợp (case / 사례) 2; sau packaging đọc trường hợp (case / 사례) 3; sau tính đồng thời (concurrency / 동시성)/async đọc trường hợp (case / 사례) 4–7; sau testing/bảo mật (security / 보안)/khả năng quan sát (observability / 관측 가능성) đọc trường hợp (case / 사례) 8–10. Mục tiêu là kiểm tra xem bạn có thể suy luận từ symptom tới cơ chế (mechanism / 메커니즘) hay chỉ đang nhớ tên API.

Nếu đã viết Python nhưng mô hình tư duy (mental model / 사고 모델) chưa chắc, không cần đọc lại mọi cú pháp (syntax / 문법). Hãy bắt đầu từ Part 1 §2–4 về name/đối tượng (object / 객체)/định danh (identity / 식별자)/mutability, Part 2 về mô hình dữ liệu (data model / 데이터 모델)/iterator/ngữ cảnh (context / 맥락) manager, rồi Part 3 về tính đồng thời (concurrency / 동시성). Khi gặp phép màu của khung phần mềm (framework magic / 프레임워크 마법) như ORM trường dữ liệu (field / 필드)/thuộc tính (property / 속성)/proxy, đọc Part 4 §4; khi gặp vòng đời (lifecycle / 생명주기)/lớp (class / 클래스) factory/metaclass, đọc Part 4 §7; khi chọn CPU mô hình thực thi (execution model / 실행 모델), đọc Part 3 §17 và Part 4 §13/17.

> **Chuyển mạch:** Danh sách nguồn chuẩn gốc là điểm kiểm chứng cuối cho phiên bản và semantics; không thay thế phần giải thích bằng một danh sách URL.

## Nguồn chuẩn gốc (canonical / 정본)

- Python documentation by phiên bản (version / 버전): https://www.python.org/doc/versions/
- Python language reference: https://docs.python.org/3.14/reference/
- Python standard library: https://docs.python.org/3.14/library/
- Python data model: https://docs.python.org/3.14/reference/datamodel.html
- Python Descriptor Guide: https://docs.python.org/3.14/howto/descriptor.html
- Python import system: https://docs.python.org/3.14/reference/import.html
- Python `typing`: https://docs.python.org/3.14/library/typing.html
- `asyncio`: https://docs.python.org/3.14/library/asyncio.html
- `multiprocessing`: https://docs.python.org/3.14/library/multiprocessing.html
- `concurrent.interpreters`: https://docs.python.org/3.14/library/concurrent.interpreters.html
- `concurrent.futures`: https://docs.python.org/3.14/library/concurrent.futures.html
- Thread-safety guarantees: https://docs.python.org/3.14/builtins/threadsafety.html
- Python 3.14 What's New: https://docs.python.org/3.14/whatsnew/3.14.html
- Python Packaging người dùng (user / 사용자) Guide: https://packaging.python.org/
- `pyproject.toml` specification: https://packaging.python.org/en/latest/specifications/pyproject-toml/
- phụ thuộc (dependency / 의존성) Groups specification: https://packaging.python.org/en/latest/specifications/dependency-groups/

> **Bàn giao:** Sau **Nguồn chuẩn gốc**, quay về [README backend domain](../README.md) để chọn part hoặc case study phù hợp.
