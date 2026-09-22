# Python Knowledge Library

Python Knowledge Library là bộ tài liệu canonical cho kiến thức Python trong repository này. Mục tiêu không phải ghi nhớ cú pháp mà là hiểu mô hình thực thi, mô hình object, data model, hệ thống import, type system, concurrency và cách Python vận hành trong môi trường production.

Baseline hiện tại là Python 3.14.7, bản stable phát hành ngày 2026-08-05. Ngày kiểm chứng: 2026-09-22. Những phần nói riêng về CPython luôn được phân biệt với semantics của ngôn ngữ Python, vì CPython là implementation phổ biến nhất chứ không phải toàn bộ định nghĩa của Python.

## Learning flow và dependency

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

Bốn part là bốn canonical chapter lớn. Cấu trúc giữ convention Beginner → Intermediate → Senior → Master đã dùng ở Java/JavaScript, nhưng nội dung bên trong đi theo dependency tự nhiên của Python thay vì chia chapter chỉ để tăng số lượng. Pythonic idiom, anti-pattern, internals và senior note được đặt cạnh concept mà chúng tác động, không tách thành file rời gây duplicate.

`ENGINEERING_CASE_STUDIES.md` không phải Part 5. Nó là lớp tích hợp sau bốn part: cùng một tình huống production được nhìn qua object semantics, import, packaging, concurrency, security và observability để luyện causal reasoning. Các case không định nghĩa lại concept đã có; chúng chỉ nối các concept thành đường suy luận từ hiện tượng quan sát được tới invariant, mechanism và evidence.

Part 1 là prerequisite trực tiếp của Part 2. Part 3 có thể được đọc sớm nếu mục tiêu là project/deployment, nhưng các phần testing, import, concurrency và memory đều giả định mental model object/reference từ Part 1–2. Part 4 là lớp đào sâu; nó không thay thế ba phần trước mà giải thích vì sao các behavior đã học xuất hiện ở runtime và production.

## Boundary với các domain khác

Python core ở đây giải thích ngôn ngữ, CPython khi cần thiết, standard library và production practice gắn trực tiếp với Python. FastAPI, AI framework và Data Engineering framework không được kéo sâu vào library chỉ vì chúng dùng file `.py`.

Repository hiện có worker Python thực tế tại [automation/app.py](../../automation/app.py), [automation/pipeline.py](../../automation/pipeline.py) và [automation/test_pipeline.py](../../automation/test_pipeline.py). Các file này được dùng như case study để nối `asyncio`, `dataclass`, `pathlib`, `subprocess`, HTTP I/O, environment configuration, testing và orchestration với code thật. Phần triển khai/deploy của worker nằm tại [automation/README.md](../../automation/README.md).

Các concept nền rộng hơn như process/thread, scheduling, memory hierarchy, networking, data structures và software engineering thuộc [Computer Science Knowledge Library](../../computer_science/README.md). Python chapter giải thích đủ để đọc liền mạch rồi bridge sang canonical domain đó khi cần chiều sâu xuyên tầng.

Multiple interpreters, free-threaded CPython và process/thread execution được giải thích ở Python boundary vì chúng thay đổi behavior của Python runtime. Những nguyên lý rộng hơn về isolation, scheduling, shared state và IPC vẫn thuộc Computer Science; tài liệu Python chỉ giữ phần cần để hiểu quyết định engineering trong Python.

## Quy ước thuật ngữ

Giải thích chính dùng tiếng Việt tự nhiên. Thuật ngữ quan trọng được chuẩn hóa trong [Glossary](GLOSSARY.md) theo dạng `tiếng Việt (English term / 한국어 용어)`. Korean chỉ dùng khi mapping thật sự hữu ích. Tên API, module, class, method, command, identifier, standard, product và code như `asyncio`, `Path`, `__iter__`, `pyproject.toml` giữ nguyên bản gốc.

Khi đọc chapter, ưu tiên hiểu quan hệ giữa khái niệm và mechanism. Glossary dùng để nhận diện thuật ngữ, không thay thế phần giải thích trong chapter.

## Modern Python và legacy

Baseline của library là Python 3.14. Codebase thực tế vẫn có thể target Python 3.8–3.13 hoặc mang pattern cũ hơn; tài liệu chỉ nhắc legacy khi nó giúp giải thích code đang tồn tại hoặc migration concern. Ví dụ, syntax generic `class Box[T]` là modern syntax từ Python 3.12, trong khi `TypeVar` + `Generic` vẫn cần biết để đọc library hỗ trợ version cũ.

Python 3.14 đưa free-threaded CPython thành cấu hình được hỗ trợ chính thức nhưng vẫn không phải build mặc định duy nhất. Vì vậy library luôn tách hai mental model: CPython mặc định có GIL và free-threaded CPython không GIL. Không suy ra rằng mọi Python 3.14 chạy thread Python bytecode song song, cũng không dùng GIL như một lý do để bỏ qua synchronization của shared mutable state.

Python 3.14 cũng đưa `concurrent.interpreters` và `InterpreterPoolExecutor` vào public standard-library surface. Multiple interpreters tạo isolation của interpreter state trong cùng process và có thể kết hợp với threads để đạt multi-core, nhưng không phải process isolation và không cho phép chia sẻ mutable Python objects tùy ý. Đây là một execution model riêng cần phân biệt với thread pool, process pool và free-threaded threads.

Trên POSIX hỗ trợ phù hợp, Python 3.14 dùng `forkserver` làm multiprocessing start method mặc định thay cho `fork`. Code phụ thuộc `fork` phải chọn explicit context thay vì coi historical default là language guarantee. Packaging cũng cần tách project metadata, dependency groups, resolved deployment environment và binary wheel/ABI compatibility thành các lớp khác nhau.

## Cách dùng library

Nếu mới học Python, đọc Part 1 → 2 và tự chạy các ví dụ nhỏ. Khi bắt đầu project thật, chuyển sang Part 3 để hiểu environment, dependency, testing, concurrency và production boundary. Part 4 phù hợp khi cần điều tra performance, memory, import behavior, descriptor/attribute lookup, `__new__`/class creation, free-threading, multiple interpreters, async internals hoặc review architecture.

Sau mỗi cụm lớn, đọc case tương ứng trong `ENGINEERING_CASE_STUDIES.md`. Ví dụ sau object/copy hãy đọc Case 1; sau import đọc Case 2; sau packaging đọc Case 3; sau concurrency/async đọc Case 4–7; sau testing/security/observability đọc Case 8–10. Mục tiêu là kiểm tra xem bạn có thể suy luận từ symptom tới mechanism hay chỉ đang nhớ tên API.

Nếu đã viết Python nhưng mental model chưa chắc, không cần đọc lại mọi syntax. Hãy bắt đầu từ Part 1 §2–4 về name/object/identity/mutability, Part 2 về data model/iterator/context manager, rồi Part 3 về concurrency. Khi gặp framework magic như ORM field/property/proxy, đọc Part 4 §4; khi gặp lifecycle/class factory/metaclass, đọc Part 4 §7; khi chọn CPU execution model, đọc Part 3 §17 và Part 4 §13/17.

## Nguồn canonical

- Python documentation by version: https://www.python.org/doc/versions/
- Python Language Reference: https://docs.python.org/3.14/reference/
- Python Standard Library: https://docs.python.org/3.14/library/
- Python Data Model: https://docs.python.org/3.14/reference/datamodel.html
- Python Descriptor Guide: https://docs.python.org/3.14/howto/descriptor.html
- Python Import System: https://docs.python.org/3.14/reference/import.html
- Python `typing`: https://docs.python.org/3.14/library/typing.html
- `asyncio`: https://docs.python.org/3.14/library/asyncio.html
- `multiprocessing`: https://docs.python.org/3.14/library/multiprocessing.html
- `concurrent.interpreters`: https://docs.python.org/3.14/library/concurrent.interpreters.html
- `concurrent.futures`: https://docs.python.org/3.14/library/concurrent.futures.html
- Thread-safety guarantees: https://docs.python.org/3.14/builtins/threadsafety.html
- Python 3.14 What's New: https://docs.python.org/3.14/whatsnew/3.14.html
- Python Packaging User Guide: https://packaging.python.org/
- `pyproject.toml` specification: https://packaging.python.org/en/latest/specifications/pyproject-toml/
- Dependency Groups specification: https://packaging.python.org/en/latest/specifications/dependency-groups/
