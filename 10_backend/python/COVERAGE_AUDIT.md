# Python Knowledge Library — Coverage & Final Audit

Audit date: 2026-09-22. Baseline: Python 3.14.7. Deepening passes: 2026-09-22.

Audit này kiểm tra toàn bộ canonical Python library sau các vòng xây dựng và đào sâu. Mục tiêu là phát hiện gap, dependency ẩn, duplicate, link sai, terminology drift và conceptual boundary sai; không tăng số chapter chỉ để roadmap dài hơn.

## 1. Vị trí conceptual trong repository

`10_backend/python/` là boundary phù hợp với cấu trúc hiện tại: Java/Spring nằm trong `10_backend`, JavaScript/TypeScript nằm trong `10_frontend`, còn Computer Science giữ foundation và mechanism xuyên ngôn ngữ. Python library vì vậy tập trung vào Python language/runtime/standard library và production engineering, rồi cross-link sang canonical domain khác khi concept đã được giải thích tốt ở nơi khác.

Code Python rõ nhất trên `main` nằm trong `automation/`:

- `automation/app.py`: FastAPI, `asyncio.Lock`, coroutine endpoint, `asyncio.to_thread`, environment variables và exception translation;
- `automation/pipeline.py`: `dataclass`, `Path`, regex, JSON, subprocess, environment/config, HTTP client, file I/O, hashing, exception handling và orchestration;
- `automation/test_pipeline.py`: standard-library `unittest` cho helper/pipeline behavior;
- `automation/requirements.txt`: dependency declaration của workflow hiện tại.

Các implementation file này không bị copy vào Python Knowledge Library. Chúng chỉ làm evidence/case study để nối mechanism chung với code thật.

## 2. Dependency và readability audit

Learning flow canonical là Part 1 → Part 2 → Part 3 → Part 4.

Part 1 thiết lập execution/name/object/reference/evaluation semantics. Part 2 dùng mental model đó để giải data model, protocol, resource lifecycle, binary data flow và static contracts. Part 3 mở rộng lên project/testing/cache/concurrency/context propagation/production. Part 4 đi xuống runtime internals rồi quay lên architecture/performance/deployment.

`ENGINEERING_CASE_STUDIES.md` nằm sau bốn part nhưng không phải Part 5. Nó có boundary riêng: bốn part dạy mechanism theo conceptual dependency, còn case studies luyện đường reasoning `symptom → invariant → mechanism → evidence → design`.

Mỗi part đủ context để bắt đầu tại đó. Khi prerequisite không hiển nhiên, chapter giải thích lại mental model cần thiết hoặc tạo bridge rõ. Không có chapter thuần API list; section được giữ khi nó tạo thêm mechanism, failure mode, performance/security implication hoặc production decision.

## 3. Coverage matrix

| Requirement | Canonical location | Status |
|---|---|---|
| Execution/source→runtime model | Part 1 §1 | Covered |
| Variables/object/reference semantics | Part 1 §2; Case 1 | Covered + integrated |
| State ownership / mutating API contract | Part 1 §2; Part 4 §8; Case 1 | Covered explicitly |
| Identity/equality/hash | Part 1 §3; Part 2 §2 | Covered |
| `NotImplemented` comparison protocol | Part 2 §2 | Covered |
| Mutable/immutable/object graph | Part 1 §4; Part 2 §5; Part 4 §8 | Covered |
| `frozen` dataclass vs deep immutability | Part 2 §5 | Covered explicitly |
| Numeric/string/container types | Part 1 §5–7 | Covered |
| slicing/shallow copy/view | Part 1 §7; Part 2 §12 | Covered with copy/ownership distinction |
| short-circuit/evaluation order | Part 1 §8 | Covered |
| argument evaluation/binding/unpacking | Part 1 §10 | Covered |
| Scope/LEGB | Part 1 §11 | Covered |
| Closure/late binding | Part 1 §12 | Covered |
| Mutable default arguments | Part 1 §13 | Covered |
| Exception propagation/narrow `try` boundary | Part 1 §14; Part 2 §11 | Covered |
| Import/circular import/reload/startup effects | Part 1 §15; Part 3 §3; Part 4 §6; Case 2 | Covered deeply |
| Data model/dunder protocols | Part 2 §1–4; Part 4 §4 | Covered |
| descriptor precedence/data vs non-data | Part 4 §4 | Covered with exact lookup model |
| descriptor cache/freshness/invalidation | Part 4 §4; Part 3 §7 | Covered with correctness reasoning |
| property/method binding/`__set_name__` | Part 2 §1/3; Part 4 §4 | Covered |
| `__getattribute__`/`__getattr__`/proxy pitfalls | Part 4 §4 | Covered |
| object construction `__new__`/`__init__` | Part 4 §7 | Covered |
| class creation ordering/`__prepare__`/`__classcell__` | Part 4 §7 | Covered at framework-author mental-model level |
| metaclass/class decorator/`__init_subclass__` | Part 4 §7 | Covered with hook-selection reasoning |
| `dataclass` | Part 2 §5 | Covered |
| iterable/iterator/exhaustion/mutation | Part 2 §6 | Covered |
| generator lifecycle/close | Part 2 §7 | Covered |
| async iterable/iterator/generator | Part 2 §7; Part 3 §11 | Covered |
| context manager cleanup/suppression | Part 2 §8 | Covered |
| decorator ordering/state | Part 2 §9; Part 4 §5 | Covered |
| typing/Protocol/generic/annotations | Part 2 §10; Part 4 §10 | Covered |
| `Any` vs `object` | Part 2 §10 | Covered |
| variance/read-write reasoning | Part 2 §10 | Covered |
| `Self` | Part 2 §10 | Covered |
| `TypeIs`/`TypeGuard` narrowing | Part 2 §10 | Covered as runtime-evidence/static-proof boundary |
| `ExceptionGroup`/`except*` prerequisite | Part 2 §11; Part 3 §11 | Covered |
| File I/O/pathlib/atomicity | Part 2 §12 | Covered |
| buffer protocol/`memoryview` | Part 2 §12; Part 4 §11 | Covered with copy/thread-safety/representation reasoning |
| path canonicalization vs authorization | Part 2 §12; Part 3 §13 | Covered |
| serialization/schema/domain validation | Part 2 §13 | Covered |
| datetime/timezone/local civil time | Part 2 §14 | Covered |
| regex | Part 2 §15 | Covered |
| logging | Part 2 §16 | Covered |
| CLI/stdout-stderr contract | Part 2 §17 | Covered |
| subprocess/security/output/process-tree lifecycle | Part 2 §18; Part 3 §13; Case 9 | Covered |
| virtual environment | Part 3 §1 | Covered |
| packaging/dependency/`pyproject.toml` | Part 3 §2; Case 3 | Covered |
| dependency groups | Part 3 §2 | Covered |
| sdist/wheel/editable/build boundary | Part 3 §2; Case 3 | Covered |
| wheel/native ABI/platform compatibility | Part 3 §2; Part 4 §18 | Covered |
| testing/pytest/mocking | Part 3 §4; Case 8 | Covered |
| deterministic testing / clock-random-environment ownership | Part 3 §4 | Covered |
| property/invariant/fuzz thinking | Part 3 §4; Case 8 | Covered |
| debugging/profiling | Part 3 §5–6; Case 10 | Covered |
| memory/GC/leaks/object graph | Part 3 §7; Part 4 §3/7/11; Case 5/10 | Covered |
| cache key/freshness/invalidation/memory scope | Part 3 §7; Part 4 §4/12 | Covered |
| `lru_cache` thread-safe vs single-flight distinction | Part 3 §7 | Covered |
| concurrency vs parallelism vs async | Part 3 §8; Case 6 | Covered |
| threading/GIL/free-threaded | Part 3 §9; Part 4 §13–14; Case 6–7 | Covered deeply |
| free-threaded built-in thread-safety scope | Part 4 §13–14 | Covered with scope/invariant distinction |
| thread state on free-threaded/native C API | Part 4 §13/18 | Covered |
| locks/invariants/deadlock | Part 3 §9; Part 4 §14 | Covered |
| multiprocessing/start methods | Part 3 §10; Part 4 §17 | Covered |
| multiple interpreters / `InterpreterPoolExecutor` | Part 3 §17; Part 4 §17 | Covered |
| extension `Py_mod_multiple_interpreters` capability | Part 4 §17 | Covered explicitly |
| extension `Py_mod_gil` / GIL re-enable behavior | Part 4 §13/17/18 | Covered explicitly |
| Python module state vs process-global native state | Part 4 §17–18 | Covered |
| `asyncio` event loop/cancellation/TaskGroup | Part 3 §11; Part 4 §15–16; Case 4–5 | Covered |
| scheduler fairness vs `asyncio.Lock` fairness | Part 4 §15 | Covered with scope distinction |
| bounded concurrency vs bounded queue | Part 4 §15 | Covered explicitly |
| queue backpressure / `Queue.shutdown()` / drain invariant | Part 4 §15/21 | Covered deeply |
| `gather()` vs `TaskGroup` failure semantics | Part 3 §11 | Covered |
| `to_thread()` cancellation scope | Part 3 §11/15; Part 4 §15 | Covered |
| `ContextVar` / task-thread context propagation | Part 3 §11; Part 4 §20 | Covered |
| sync/async adapter boundary | Part 3 §11; Part 4 §24 | Covered |
| local lock vs distributed coordination | Part 3 §15; Case 4 | Covered |
| networking/retry/idempotency/deadline | Part 3 §12; Case 8 | Covered |
| security/dynamic execution/introspection | Part 2 §13/18; Part 3 §13; Part 4 §19; Case 9 | Covered |
| performance/specialization/representation | Part 3 §6/14; Part 4 §2/11/12/18 | Covered |
| observability log/metric/trace | Part 2 §16; Part 4 §20; Case 10 | Covered |
| metric cardinality/sampling/telemetry failure policy | Part 4 §20 | Covered |
| deployment/reproducibility | Part 3 §15; Part 4 §21; Case 3 | Covered |
| readiness vs liveness | Part 4 §21 | Covered |
| signal→stop-accept→drain/cancel→close shutdown protocol | Part 4 §14/21 | Covered deeply |
| `asyncio.Runner` Ctrl-C/cancellation shutdown model | Part 4 §21 | Covered |
| architecture patterns | Part 4 §23–26; Capstone | Covered |
| production failure reasoning | Part 4 §27–28; case studies | Covered deeply |
| modern vs legacy/version evolution | Part 4 §22 | Covered |
| terminology Việt–Anh–Hàn | `GLOSSARY.md` + chapter callouts | Covered |
| Pythonic idioms / senior notes | Integrated beside concepts | No duplicate chapter |

## 4. Misconception audit

Các mental-model lỗi chính đều có canonical treatment:

`b = a` không copy object; `is` không thay `==`; immutable outer container không làm toàn object graph immutable; `frozen=True` không tạo deep immutability; `list[:]` là shallow copy còn `memoryview` có thể giữ shared storage; default mutable argument được evaluate khi `def` chạy; closure thường giữ binding chứ không snapshot value; argument expression chạy trước parameter binding; `try` quá rộng có thể bắt nhầm lỗi từ success path.

Ở data model, `obj.x` không đồng nghĩa đọc `obj.__dict__`; property là descriptor; non-data descriptor có thể bị instance attribute shadow; descriptor cache có freshness/invalidation contract; `__init__` không tạo object; class body là executable code; `__prepare__`, `__set_name__`, `__init_subclass__` và decorator nằm ở các phase khác nhau; metaclass không phải hook duy nhất.

Ở typing, annotation không tự enforce runtime; `Any` khác `object`; mutable generic không tự nhiên covariant; `Self` phải giữ dynamic subclass contract; `TypeIs`/`TypeGuard` implementation sai có thể đưa static checker tới assumption sai.

Ở testing/runtime, retry flaky test không tạo determinism; seed global random không tự loại order dependency; `lru_cache` thread-safe không đồng nghĩa single-flight; cache process-local không thành distributed cache; GC không giải phóng object còn reachable.

Ở concurrency, `async def` không đồng nghĩa parallelism; fairness của `asyncio.Lock` không đồng nghĩa event-loop scheduler fair; semaphore bounded không giới hạn số task đang chờ; cancellation không kill thread/remote side effect; `TaskGroup` không tự rollback business effect; local lock không phải distributed lock; GIL không bảo vệ business invariant; free-threaded không nghĩa runtime không còn synchronization; thread state vẫn cần cho C API.

Ở interpreter/native boundary, subinterpreter không phải process nhẹ; Python module globals isolate không chứng minh native process-global state isolate; support subinterpreter và support no-GIL là hai capability riêng; import native extension có thể làm GIL được enable lại trên free-threaded runtime nếu extension không khai báo support phù hợp.

Ở shutdown/operations, queue empty không đồng nghĩa mọi external side effect đã commit; immediate queue shutdown có thể phá normal `join()` work-done invariant; liveness không đồng nghĩa readiness; signal không phải generic worker interrupt; Ctrl-C cancellation không thể tiến triển tốt nếu event loop bị CPU loop monopolize; metric label high cardinality có thể biến observability thành performance/cost incident.

## 5. Version audit

Các volatile facts được đối chiếu với official documentation vào 2026-09-22:

- Python 3.14.7 là stable 3.x release hiện tại, phát hành 2026-08-05.
- Free-threaded CPython officially supported từ 3.14 nhưng vẫn optional.
- Type-parameter syntax hiện đại có từ 3.12; `Self` từ 3.11; `TypeGuard` từ 3.10; `TypeIs` từ 3.13.
- Python 3.14 có t-strings và deferred annotation evaluation theo PEP 649/749.
- Buffer protocol có Python-level customization từ 3.12; `memoryview` là standard consumer abstraction cho buffer.
- `asyncio` policy system deprecated ở 3.14 và hướng tới removal ở 3.16.
- `asyncio.get_event_loop()` trong 3.14 không còn ngầm tạo loop nếu không có current loop.
- `asyncio.Lock.acquire()` documented fair theo waiter order; guarantee này không mở rộng thành scheduler-wide fairness.
- `asyncio.Queue.shutdown()`/`QueueShutDown` tồn tại trong modern Python line và phân biệt graceful drain với immediate shutdown; immediate mode có thể phá normal `join()` invariant về work đã hoàn thành.
- Từ 3.14, `fork` không còn là default start method trên platform nào; POSIX phù hợp dùng `forkserver` mặc định, còn macOS/Windows có behavior platform-specific.
- Python 3.14 có public `concurrent.interpreters` và `InterpreterPoolExecutor`.
- C extension có `Py_mod_multiple_interpreters` để khai báo support subinterpreter và `Py_mod_gil` để khai báo dependency vào GIL; hai capability không đồng nghĩa nhau.
- Trên free-threaded build, extension không khai báo no-GIL support phù hợp có thể làm GIL được enable lại khi import.
- Python thread state vẫn là requirement cho C API ngay cả khi GIL disabled.
- Signal handler installation/processing có main-thread/main-interpreter constraints; signal không phải thread-cancellation mechanism.
- `pyproject.toml` là configuration point chuẩn cho build/project/tool metadata; standardized dependency groups phục vụ development/internal requirement và không trở thành built runtime dependency metadata.

Các facts trên phải được re-check khi baseline đổi sang Python 3.15+.

## 6. Terminology audit

Giải thích chính dùng tiếng Việt. API, module, class, method, standard, command, identifier và code giữ nguyên bản gốc. `GLOSSARY.md` là canonical mapping theo format `tiếng Việt (English term / 한국어 용어)` khi Korean mapping thực sự hữu ích.

Glossary không thay thế explanation. Chapter vẫn phải nói concept tồn tại để giải quyết vấn đề gì, mechanism nào tạo behavior và failure/performance/security implication khi có.

Các deepening pass mới đã bổ sung mapping cho class-creation hooks, thread state/per-interpreter state, scheduler fairness, bounded concurrency, queue shutdown, metric cardinality, readiness/liveness và graceful shutdown; không tạo glossary phụ.

## 7. Boundary và duplicate audit

Python core không đào sâu FastAPI routing/DI/ASGI internals, `httpx` API cụ thể, AI framework, Data Engineering framework, distributed cache product, observability backend cụ thể hoặc C/Rust extension implementation tutorial đầy đủ.

Part 4 chỉ đi đủ sâu vào C/native boundary để application engineer hiểu capability/ABI/runtime-assumption của dependency. Chi tiết tự viết extension C/Rust, allocator internals, low-level transport/TLS implementation vẫn là specialization boundary.

`ENGINEERING_CASE_STUDIES.md` chỉ dùng `automation/` như evidence/capstone, không biến framework-specific API thành Python core.

Không có `_v2`, `_final`, `_updated`, `_rewrite`, chapter Pythonic riêng, anti-pattern riêng hoặc Senior Notes riêng. Nội dung đúng được consolidate vào bốn canonical part.

## 8. Internal-link audit

Các cross-link quan trọng được giữ:

- `../../automation/app.py`
- `../../automation/pipeline.py`
- `../../automation/test_pipeline.py`
- `../../automation/README.md`
- `../../computer_science/README.md`

Python README link tới bốn part, case studies, glossary và audit bằng relative paths. Root README phải link trực tiếp `10_backend/python/README.md` sau mỗi rebase/squash lên latest `main`.

## 9. Depth audit sau deepening passes

Part 1 hiện đi từ execution/evaluation tới binding/ownership/exception boundary.

Part 2 nối usage-level protocol với underlying semantics: descriptor-backed property, iterator mutation/lifecycle, sync→async generator, context-manager suppression, typing variance/narrowing, buffer protocol/view semantics, schema validation, civil-time ambiguity và subprocess lifecycle.

Part 3 nối project engineering với determinism/cache/context/concurrency: artifact build, test ownership of nondeterminism, retained-state/cache invalidation, GIL/free-threaded migration, structured async failure, context propagation, retry/deadline/idempotency và deployment process model.

Part 4 hiện đi sâu thêm ở những vùng trước đây còn mỏng: descriptor cache correctness, class-creation ordering và `__classcell__`, runtime thread-state/free-threaded nuance, native extension capability declarations, subinterpreter vs process-global native state, scheduler fairness vs primitive fairness, bounded queue/concurrency, queue shutdown invariants, telemetry cardinality/sampling/failure policy và signal-driven graceful shutdown.

Những vùng vẫn chưa cần tách tài liệu riêng: CPython allocator/GC source-level implementation, tự viết C/Rust extension, low-level asyncio transport/protocol, TLS internals, parser/compiler construction, OS scheduler internals và framework-specific metaprogramming. Nếu nhu cầu thực tế xuất hiện, ưu tiên cross-link Computer Science hoặc mở rộng Part 4 trước; chỉ tách file khi dependency riêng đủ lớn.

## 10. Canonical source set

- https://www.python.org/doc/versions/
- https://docs.python.org/3.14/reference/
- https://docs.python.org/3.14/reference/expressions.html
- https://docs.python.org/3.14/reference/datamodel.html
- https://docs.python.org/3.14/reference/import.html
- https://docs.python.org/3.14/howto/descriptor.html
- https://docs.python.org/3.14/howto/free-threading-python.html
- https://docs.python.org/3.14/howto/free-threading-extensions.html
- https://docs.python.org/3.14/library/typing.html
- https://docs.python.org/3.14/library/contextlib.html
- https://docs.python.org/3.14/library/contextvars.html
- https://docs.python.org/3.14/library/functools.html
- https://docs.python.org/3.14/library/exceptions.html
- https://docs.python.org/3.14/library/stdtypes.html#memoryview
- https://docs.python.org/3.14/c-api/buffer.html
- https://docs.python.org/3.14/c-api/module.html
- https://docs.python.org/3.14/c-api/threads.html
- https://docs.python.org/3.14/builtins/threadsafety.html
- https://docs.python.org/3.14/library/asyncio.html
- https://docs.python.org/3.14/library/asyncio-sync.html
- https://docs.python.org/3.14/library/asyncio-queue.html
- https://docs.python.org/3.14/library/asyncio-task.html
- https://docs.python.org/3.14/library/asyncio-runner.html
- https://docs.python.org/3.14/library/signal.html
- https://docs.python.org/3.14/library/multiprocessing.html
- https://docs.python.org/3.14/library/concurrent.interpreters.html
- https://docs.python.org/3.14/library/concurrent.futures.html
- https://docs.python.org/3.14/whatsnew/3.14.html
- https://packaging.python.org/
- https://packaging.python.org/en/latest/specifications/pyproject-toml/
- https://packaging.python.org/en/latest/specifications/dependency-groups/
- https://packaging.python.org/en/latest/specifications/binary-distribution-format/
