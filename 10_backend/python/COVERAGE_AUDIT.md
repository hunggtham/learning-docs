# Thư viện kiến thức Python (Python knowledge library / 파이썬 지식 라이브러리) — Coverage & Final kiểm tra (audit / 감사)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Thư viện kiến thức Python (Python knowledge library / 파이썬 지식 라이브러리) — Coverage & Final kiểm tra (audit / 감사)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Vị trí conceptual trong repository** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. phụ thuộc (dependency / 의존성) và readability kiểm tra (audit / 감사)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối coverage audit với owner, chapter và bằng chứng của Python, để khoảng trống nội dung được nhìn thấy trước khi mở rộng.

Kiểm tra (audit / 감사) date: 2026-09-22. Baseline: Python 3.14.7. Deepening passes: 2026-09-22.

Kiểm tra (audit / 감사) này kiểm tra toàn bộ chuẩn gốc (canonical / 정본) Python thư viện (library / 라이브러리) sau các vòng xây dựng và đào sâu. Mục tiêu là phát hiện gap, phụ thuộc (dependency / 의존성) ẩn, duplicate, link sai, terminology drift và conceptual ranh giới (boundary / 경계) sai; không tăng số chapter chỉ để roadmap dài hơn.

## 1. Vị trí conceptual trong repository

`10_backend/python/` là ranh giới (boundary / 경계) phù hợp với cấu trúc hiện tại: Java/Spring nằm trong `10_backend`, JavaScript/TypeScript nằm trong `10_frontend`, còn Khoa học máy tính (computer science / 컴퓨터 과학) giữ foundation và cơ chế (mechanism / 메커니즘) xuyên ngôn ngữ. Python thư viện (library / 라이브러리) vì vậy tập trung vào Python ngôn ngữ (language / 언어)/thời gian chạy (runtime / 런타임)/thư viện chuẩn (standard library / 표준 라이브러리) và môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링), rồi cross-link sang chuẩn gốc (canonical / 정본) lĩnh vực (domain / 도메인) khác khi concept đã được giải thích tốt ở nơi khác.

Mã Python làm bằng chứng nằm trong các ví dụ và bài kiểm thử đi kèm từng Part. `automation/repo_audit.py` chỉ kiểm tra đường dẫn, catalog và liên kết Markdown; nó không sở hữu runtime hay sinh nội dung. Các ví dụ không được sao chép thành một worker dùng chung: chúng chỉ nối cơ chế Python với mã thật và phải được đọc cùng nguồn chính tương ứng.

> **Chuyển mạch:** Vị trí conceptual cho biết repository đang kiểm tra điều gì; **dependency và readability audit** chuyển câu hỏi đó thành bằng chứng về đường phụ thuộc và khả năng đọc. Kết quả được tổng hợp trong coverage matrix.

## 2. phụ thuộc (dependency / 의존성) và readability kiểm tra (audit / 감사)

Mạch học (learning flow / 학습 흐름) chuẩn gốc (canonical / 정본) là Part 1 → Part 2 → Part 3 → Part 4.

Part 1 thiết lập thực thi (execution / 실행)/name/đối tượng (object / 객체)/tham chiếu (reference / 참조)/evaluation ngữ nghĩa (semantics / 의미론). Part 2 dùng mô hình tư duy (mental model / 사고 모델) đó để giải mô hình dữ liệu (data model / 데이터 모델), giao thức (protocol / 프로토콜), tài nguyên (resource / 자원) vòng đời (lifecycle / 생명주기), nhị phân (binary / 이진) luồng dữ liệu (data flow / 데이터 흐름) và static contracts. Part 3 mở rộng lên dự án (project / 프로젝트)/testing/bộ nhớ đệm (cache / 캐시)/tính đồng thời (concurrency / 동시성)/ngữ cảnh (context / 맥락) propagation/môi trường vận hành (production / 운영 환경). Part 4 đi xuống thời gian chạy (runtime / 런타임) internals rồi quay lên kiến trúc (architecture / 아키텍처)/hiệu năng (performance / 성능)/triển khai (deployment / 배포).

`ENGINEERING_CASE_STUDIES.md` nằm sau bốn part nhưng không phải Part 5. Nó có ranh giới (boundary / 경계) riêng: bốn part dạy cơ chế (mechanism / 메커니즘) theo conceptual phụ thuộc (dependency / 의존성), còn trường hợp (case / 사례) studies luyện đường lập luận (reasoning / 추론) `symptom → invariant → mechanism → evidence → design`.

Mỗi part đủ ngữ cảnh (context / 맥락) để bắt đầu tại đó. Khi prerequisite không hiển nhiên, chapter giải thích lại mô hình tư duy (mental model / 사고 모델) cần thiết hoặc tạo cầu nối (bridge / 브리지) rõ. Không có chapter thuần API danh sách (list / 목록); section được giữ khi nó tạo thêm cơ chế (mechanism / 메커니즘), dạng thất bại (failure mode / 실패 모드), hiệu năng (performance / 성능)/bảo mật (security / 보안) implication hoặc môi trường vận hành (production / 운영 환경) quyết định (decision / 결정).

> **Chuyển mạch:** Coverage matrix gom kết quả dependency/readability thành các năng lực có owner. **Misconception audit** kiểm tra tiếp xem người học có thể dùng đúng mental model hay đang mang theo một hiểu lầm có hệ thống.

## 3. Coverage ma trận (matrix / 행렬)

| yêu cầu (requirement / 요구사항) | chuẩn gốc (canonical / 정본) location | Status |
|---|---|---|
| thực thi (execution / 실행)/nguồn (source / 소스)→thời gian chạy (runtime / 런타임) mô hình (model / 모델) | Part 1 §1 | Covered |
| Variables/đối tượng (object / 객체)/tham chiếu (reference / 참조) ngữ nghĩa (semantics / 의미론) | Part 1 §2; trường hợp (case / 사례) 1 | Covered + integrated |
| quyền sở hữu trạng thái (state ownership / 상태 소유권) / mutating Đặc tả API (API contract / API 계약) | Part 1 §2; Part 4 §8; trường hợp (case / 사례) 1 | Covered explicitly |
| định danh (identity / 식별자)/equality/băm (hash / 해시) | Part 1 §3; Part 2 §2 | Covered |
| `NotImplemented` comparison giao thức (protocol / 프로토콜) | Part 2 §2 | Covered |
| Mutable/immutable/đối tượng (object / 객체) đồ thị (graph / 그래프) | Part 1 §4; Part 2 §5; Part 4 §8 | Covered |
| `frozen` dataclass vs deep immutability | Part 2 §5 | Covered explicitly |
| Numeric/string/bộ chứa (container / 컨테이너) types | Part 1 §5–7 | Covered |
| slicing/shallow bản sao (copy / 복사)/view | Part 1 §7; Part 2 §12 | Covered with bản sao (copy / 복사)/quyền sở hữu (ownership / 소유권) distinction |
| short-circuit/evaluation thứ tự (order / 순서) | Part 1 §8 | Covered |
| argument evaluation/binding/unpacking | Part 1 §10 | Covered |
| phạm vi (scope / 범위)/LEGB | Part 1 §11 | Covered |
| Closure/late binding | Part 1 §12 | Covered |
| Mutable default arguments | Part 1 §13 | Covered |
| Exception propagation/narrow `try` ranh giới (boundary / 경계) | Part 1 §14; Part 2 §11 | Covered |
| Import/circular import/reload/startup effects | Part 1 §15; Part 3 §3; Part 4 §6; trường hợp (case / 사례) 2 | Covered deeply |
| mô hình dữ liệu (data model / 데이터 모델)/dunder protocols | Part 2 §1–4; Part 4 §4 | Covered |
| descriptor precedence/dữ liệu (data / 데이터) vs non-data | Part 4 §4 | Covered with chính xác (exact / 정확한) lookup mô hình (model / 모델) |
| descriptor bộ nhớ đệm (cache / 캐시)/freshness/vô hiệu hóa (invalidation / 무효화) | Part 4 §4; Part 3 §7 | Covered with tính đúng đắn (correctness / 정확성) lập luận (reasoning / 추론) |
| thuộc tính (property / 속성)/phương thức (method / 메서드) binding/`__set_name__` | Part 2 §1/3; Part 4 §4 | Covered |
| `__getattribute__`/`__getattr__`/proxy pitfalls | Part 4 §4 | Covered |
| đối tượng (object / 객체) construction `__new__`/`__init__` | Part 4 §7 | Covered |
| lớp (class / 클래스) creation thứ tự (ordering / 순서)/`__prepare__`/`__classcell__` | Part 4 §7 | Covered at framework-author mental-model mức (level / 수준) |
| metaclass/lớp (class / 클래스) decorator/`__init_subclass__` | Part 4 §7 | Covered with hook-selection lập luận (reasoning / 추론) |
| `dataclass` | Part 2 §5 | Covered |
| iterable/iterator/exhaustion/mutation | Part 2 §6 | Covered |
| generator vòng đời (lifecycle / 생명주기)/close | Part 2 §7 | Covered |
| async iterable/iterator/generator | Part 2 §7; Part 3 §11 | Covered |
| ngữ cảnh (context / 맥락) manager cleanup/suppression | Part 2 §8 | Covered |
| decorator thứ tự (ordering / 순서)/trạng thái (state / 상태) | Part 2 §9; Part 4 §5 | Covered |
| typing/giao thức (protocol / 프로토콜)/generic/annotations | Part 2 §10; Part 4 §10 | Covered |
| `Any` vs `object` | Part 2 §10 | Covered |
| variance/read-write lập luận (reasoning / 추론) | Part 2 §10 | Covered |
| `Self` | Part 2 §10 | Covered |
| `TypeIs`/`TypeGuard` narrowing | Part 2 §10 | Covered as runtime-evidence/static-proof ranh giới (boundary / 경계) |
| `ExceptionGroup`/`except*` prerequisite | Part 2 §11; Part 3 §11 | Covered |
| tệp (file / 파일) I/O/pathlib/atomicity | Part 2 §12 | Covered |
| buffer giao thức (protocol / 프로토콜)/`memoryview` | Part 2 §12; Part 4 §11 | Covered with bản sao (copy / 복사)/thread-safety/biểu diễn (representation / 표현) lập luận (reasoning / 추론) |
| đường dẫn (path / 경로) canonicalization vs authorization | Part 2 §12; Part 3 §13 | Covered |
| serialization/lược đồ (schema / 스키마)/lĩnh vực (domain / 도메인) kiểm tra hợp lệ (validation / 검증) | Part 2 §13 | Covered |
| datetime/timezone/cục bộ (local / 로컬) civil thời gian (time / 시간) | Part 2 §14 | Covered |
| regex | Part 2 §15 | Covered |
| logging | Part 2 §16 | Covered |
| CLI/stdout-stderr đặc tả hợp đồng (contract / 계약) | Part 2 §17 | Covered |
| subprocess/bảo mật (security / 보안)/đầu ra (output / 출력)/process-tree vòng đời (lifecycle / 생명주기) | Part 2 §18; Part 3 §13; trường hợp (case / 사례) 9 | Covered |
| virtual môi trường (environment / 환경) | Part 3 §1 | Covered |
| packaging/phụ thuộc (dependency / 의존성)/`pyproject.toml` | Part 3 §2; trường hợp (case / 사례) 3 | Covered |
| phụ thuộc (dependency / 의존성) groups | Part 3 §2 | Covered |
| sdist/wheel/editable/bản dựng (build / 빌드) ranh giới (boundary / 경계) | Part 3 §2; trường hợp (case / 사례) 3 | Covered |
| wheel/bản địa (native / 네이티브) ABI/nền tảng (platform / 플랫폼) tính tương thích (compatibility / 호환성) | Part 3 §2; Part 4 §18 | Covered |
| testing/pytest/mocking | Part 3 §4; trường hợp (case / 사례) 8 | Covered |
| deterministic testing / clock-random-environment quyền sở hữu (ownership / 소유권) | Part 3 §4 | Covered |
| thuộc tính (property / 속성)/bất biến (invariant / 불변식)/fuzz thinking | Part 3 §4; trường hợp (case / 사례) 8 | Covered |
| debugging/profiling | Part 3 §5–6; trường hợp (case / 사례) 10 | Covered |
| bộ nhớ (memory / 메모리)/GC/leaks/đối tượng (object / 객체) đồ thị (graph / 그래프) | Part 3 §7; Part 4 §3/7/11; trường hợp (case / 사례) 5/10 | Covered |
| bộ nhớ đệm (cache / 캐시) key/freshness/vô hiệu hóa (invalidation / 무효화)/bộ nhớ (memory / 메모리) phạm vi (scope / 범위) | Part 3 §7; Part 4 §4/12 | Covered |
| `lru_cache` thread-safe vs single-flight distinction | Part 3 §7 | Covered |
| tính đồng thời (concurrency / 동시성) vs parallelism vs async | Part 3 §8; trường hợp (case / 사례) 6 | Covered |
| threading/GIL/free-threaded | Part 3 §9; Part 4 §13–14; trường hợp (case / 사례) 6–7 | Covered deeply |
| free-threaded built-in thread-safety phạm vi (scope / 범위) | Part 4 §13–14 | Covered with phạm vi (scope / 범위)/bất biến (invariant / 불변식) distinction |
| luồng thực thi (thread / 스레드) trạng thái (state / 상태) on free-threaded/bản địa (native / 네이티브) C API | Part 4 §13/18 | Covered |
| locks/invariants/deadlock | Part 3 §9; Part 4 §14 | Covered |
| multiprocessing/start methods | Part 3 §10; Part 4 §17 | Covered |
| multiple interpreters / `InterpreterPoolExecutor` | Part 3 §17; Part 4 §17 | Covered |
| extension `Py_mod_multiple_interpreters` năng lực (capability / 역량) | Part 4 §17 | Covered explicitly |
| extension `Py_mod_gil` / GIL re-enable hành vi (behavior / 동작) | Part 4 §13/17/18 | Covered explicitly |
| Python mô-đun (module / 모듈) trạng thái (state / 상태) vs process-global bản địa (native / 네이티브) trạng thái (state / 상태) | Part 4 §17–18 | Covered |
| `asyncio` vòng lặp sự kiện (event loop / 이벤트 루프)/cancellation/TaskGroup | Part 3 §11; Part 4 §15–16; trường hợp (case / 사례) 4–5 | Covered |
| scheduler fairness vs `asyncio.Lock` fairness | Part 4 §15 | Covered with phạm vi (scope / 범위) distinction |
| bounded tính đồng thời (concurrency / 동시성) vs bounded hàng đợi (queue / 큐) | Part 4 §15 | Covered explicitly |
| hàng đợi (queue / 큐) backpressure / `Queue.shutdown()` / drain bất biến (invariant / 불변식) | Part 4 §15/21 | Covered deeply |
| `gather()` vs `TaskGroup` thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론) | Part 3 §11 | Covered |
| `to_thread()` cancellation phạm vi (scope / 범위) | Part 3 §11/15; Part 4 §15 | Covered |
| `ContextVar` / task-thread ngữ cảnh (context / 맥락) propagation | Part 3 §11; Part 4 §20 | Covered |
| sync/async adapter ranh giới (boundary / 경계) | Part 3 §11; Part 4 §24 | Covered |
| cục bộ (local / 로컬) khóa (lock / 잠금) vs phân tán (distributed / 분산) coordination | Part 3 §15; trường hợp (case / 사례) 4 | Covered |
| networking/thử lại (retry / 재시도)/idempotency/deadline | Part 3 §12; trường hợp (case / 사례) 8 | Covered |
| bảo mật (security / 보안)/động (dynamic / 동적) thực thi (execution / 실행)/introspection | Part 2 §13/18; Part 3 §13; Part 4 §19; trường hợp (case / 사례) 9 | Covered |
| hiệu năng (performance / 성능)/specialization/biểu diễn (representation / 표현) | Part 3 §6/14; Part 4 §2/11/12/18 | Covered |
| khả năng quan sát (observability / 관측 가능성) log/chỉ số (metric / 지표)/dấu vết (trace / 추적) | Part 2 §16; Part 4 §20; trường hợp (case / 사례) 10 | Covered |
| chỉ số (metric / 지표) cardinality/sampling/telemetry thất bại (failure / 실패) chính sách (policy / 정책) | Part 4 §20 | Covered |
| triển khai (deployment / 배포)/reproducibility | Part 3 §15; Part 4 §21; trường hợp (case / 사례) 3 | Covered |
| readiness vs liveness | Part 4 §21 | Covered |
| tín hiệu (signal / 신호)→stop-accept→drain/cancel→close shutdown giao thức (protocol / 프로토콜) | Part 4 §14/21 | Covered deeply |
| `asyncio.Runner` Ctrl-C/cancellation shutdown mô hình (model / 모델) | Part 4 §21 | Covered |
| kiến trúc (architecture / 아키텍처) patterns | Part 4 §23–26; Capstone | Covered |
| môi trường vận hành (production / 운영 환경) thất bại (failure / 실패) lập luận (reasoning / 추론) | Part 4 §27–28; trường hợp (case / 사례) studies | Covered deeply |
| hiện đại (modern / 현대적) vs legacy/phiên bản (version / 버전) evolution | Part 4 §22 | Covered |
| terminology Việt–Anh–Hàn | `GLOSSARY.md` + chapter callouts | Covered |
| Pythonic idioms / cấp cao (senior / 시니어) notes | Integrated beside concepts | No duplicate chapter |

> **Chuyển mạch:** Khi matrix đã chỉ ra năng lực, misconception audit nêu rõ chỗ reasoning dễ sai. **Version audit** tiếp theo xác định claim nào phụ thuộc Python release và cần mốc nguồn.

## 4. Misconception kiểm tra (audit / 감사)

Các mental-model lỗi chính đều có chuẩn gốc (canonical / 정본) treatment:

`b = a` không bản sao (copy / 복사) đối tượng (object / 객체); `is` không thay `==`; immutable outer bộ chứa (container / 컨테이너) không làm toàn đối tượng (object / 객체) đồ thị (graph / 그래프) immutable; `frozen=True` không tạo deep immutability; `list[:]` là shallow bản sao (copy / 복사) còn `memoryview` có thể giữ dùng chung (shared / 공유) lưu trữ (storage / 저장소); default mutable argument được evaluate khi `def` chạy; closure thường giữ binding chứ không snapshot giá trị (value / 값); argument expression chạy trước parameter binding; `try` quá rộng có thể bắt nhầm lỗi từ success đường dẫn (path / 경로).

Ở mô hình dữ liệu (data model / 데이터 모델), `obj.x` không đồng nghĩa đọc `obj.__dict__`; thuộc tính (property / 속성) là descriptor; non-data descriptor có thể bị instance attribute shadow; descriptor bộ nhớ đệm (cache / 캐시) có freshness/vô hiệu hóa (invalidation / 무효화) đặc tả hợp đồng (contract / 계약); `__init__` không tạo đối tượng (object / 객체); lớp (class / 클래스) body là executable mã (code / 코드); `__prepare__`, `__set_name__`, `__init_subclass__` và decorator nằm ở các phase khác nhau; metaclass không phải hook duy nhất.

Ở typing, annotation không tự enforce thời gian chạy (runtime / 런타임); `Any` khác `object`; mutable generic không tự nhiên covariant; `Self` phải giữ động (dynamic / 동적) subclass đặc tả hợp đồng (contract / 계약); `TypeIs`/`TypeGuard` hiện thực (implementation / 구현) sai có thể đưa static checker tới giả định (assumption / 가정) sai.

Ở testing/thời gian chạy (runtime / 런타임), thử lại (retry / 재시도) flaky kiểm thử (test / 테스트) không tạo determinism; seed toàn cục (global / 전역) random không tự loại thứ tự (order / 순서) phụ thuộc (dependency / 의존성); `lru_cache` thread-safe không đồng nghĩa single-flight; bộ nhớ đệm (cache / 캐시) process-local không thành phân tán (distributed / 분산) bộ nhớ đệm (cache / 캐시); GC không giải phóng đối tượng (object / 객체) còn reachable.

Ở tính đồng thời (concurrency / 동시성), `async def` không đồng nghĩa parallelism; fairness của `asyncio.Lock` không đồng nghĩa event-loop scheduler fair; semaphore bounded không giới hạn số tác vụ (task / 작업) đang chờ; cancellation không kill luồng thực thi (thread / 스레드)/remote side tác động (effect / 효과); `TaskGroup` không tự quay lui (rollback / 롤백) nghiệp vụ (business / 비즈니스) tác động (effect / 효과); cục bộ (local / 로컬) khóa (lock / 잠금) không phải phân tán (distributed / 분산) khóa (lock / 잠금); GIL không bảo vệ nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식); free-threaded không nghĩa thời gian chạy (runtime / 런타임) không còn synchronization; luồng thực thi (thread / 스레드) trạng thái (state / 상태) vẫn cần cho C API.

Ở trình thông dịch (interpreter / 인터프리터)/bản địa (native / 네이티브) ranh giới (boundary / 경계), subinterpreter không phải tiến trình (process / 프로세스) nhẹ; Python mô-đun (module / 모듈) globals isolate không chứng minh bản địa (native / 네이티브) process-global trạng thái (state / 상태) isolate; hỗ trợ (support / 지원) subinterpreter và hỗ trợ (support / 지원) no-GIL là hai năng lực (capability / 역량) riêng; import bản địa (native / 네이티브) extension có thể làm GIL được enable lại trên free-threaded thời gian chạy (runtime / 런타임) nếu extension không khai báo hỗ trợ (support / 지원) phù hợp.

Ở shutdown/operations, hàng đợi (queue / 큐) empty không đồng nghĩa mọi bên ngoài (external / 외부) side tác động (effect / 효과) đã lần ghi nhận (commit / 커밋); immediate hàng đợi (queue / 큐) shutdown có thể phá normal `join()` work-done bất biến (invariant / 불변식); liveness không đồng nghĩa readiness; tín hiệu (signal / 신호) không phải generic worker interrupt; Ctrl-C cancellation không thể tiến triển tốt nếu vòng lặp sự kiện (event loop / 이벤트 루프) bị CPU vòng lặp (loop / 루프) monopolize; chỉ số (metric / 지표) label high cardinality có thể biến khả năng quan sát (observability / 관측 가능성) thành hiệu năng (performance / 성능)/chi phí (cost / 비용) sự cố (incident / 인시던트).

> **Chuyển mạch:** Version audit khóa các claim theo runtime và tài liệu tương ứng; **Terminology audit** bảo đảm cùng một khái niệm không bị gọi bằng nhiều thuật ngữ làm đứt mạch học.

## 5. phiên bản (version / 버전) kiểm tra (audit / 감사)

Các volatile facts được đối chiếu với official documentation vào 2026-09-22:

- Python 3.14.7 là stable 3.x bản phát hành (release / 릴리스) hiện tại, phát hành 2026-08-05.
- Free-threaded CPython officially supported từ 3.14 nhưng vẫn optional.
- Type-parameter cú pháp (syntax / 문법) hiện đại có từ 3.12; `Self` từ 3.11; `TypeGuard` từ 3.10; `TypeIs` từ 3.13.
- Python 3.14 có t-strings và deferred annotation evaluation theo PEP 649/749.
- Buffer giao thức (protocol / 프로토콜) có Python-level customization từ 3.12; `memoryview` là tiêu chuẩn (standard / 표준) bên tiêu thụ (consumer / 소비자) lớp trừu tượng (abstraction / 추상화) cho buffer.
- `asyncio` chính sách (policy / 정책) hệ thống (system / 시스템) deprecated ở 3.14 và hướng tới removal ở 3.16.
- `asyncio.get_event_loop()` trong 3.14 không còn ngầm tạo vòng lặp (loop / 루프) nếu không có hiện tại (current / 현재) vòng lặp (loop / 루프).
- `asyncio.Lock.acquire()` documented fair theo waiter thứ tự (order / 순서); guarantee này không mở rộng thành scheduler-wide fairness.
- `asyncio.Queue.shutdown()`/`QueueShutDown` tồn tại trong hiện đại (modern / 현대적) Python line và phân biệt graceful drain với immediate shutdown; immediate chế độ (mode / 모드) có thể phá normal `join()` bất biến (invariant / 불변식) về công việc (work / 작업) đã hoàn thành.
- Từ 3.14, `fork` không còn là default start phương thức (method / 메서드) trên nền tảng (platform / 플랫폼) nào; POSIX phù hợp dùng `forkserver` mặc định, còn macOS/Windows có hành vi (behavior / 동작) platform-specific.
- Python 3.14 có công khai (public / 공개) `concurrent.interpreters` và `InterpreterPoolExecutor`.
- C extension có `Py_mod_multiple_interpreters` để khai báo hỗ trợ (support / 지원) subinterpreter và `Py_mod_gil` để khai báo phụ thuộc (dependency / 의존성) vào GIL; hai năng lực (capability / 역량) không đồng nghĩa nhau.
- Trên free-threaded bản dựng (build / 빌드), extension không khai báo no-GIL hỗ trợ (support / 지원) phù hợp có thể làm GIL được enable lại khi import.
- Python luồng thực thi (thread / 스레드) trạng thái (state / 상태) vẫn là yêu cầu (requirement / 요구사항) cho C API ngay cả khi GIL disabled.
- tín hiệu (signal / 신호) handler installation/processing có main-thread/main-interpreter các ràng buộc (constraints / 제약조건들); tín hiệu (signal / 신호) không phải thread-cancellation cơ chế (mechanism / 메커니즘).
- `pyproject.toml` là cấu hình (configuration / 구성) điểm (point / 지점) chuẩn cho bản dựng (build / 빌드)/dự án (project / 프로젝트)/công cụ (tool / 도구) siêu dữ liệu (metadata / 메타데이터); standardized phụ thuộc (dependency / 의존성) groups phục vụ development/nội bộ (internal / 내부) yêu cầu (requirement / 요구사항) và không trở thành built thời gian chạy (runtime / 런타임) phụ thuộc (dependency / 의존성) siêu dữ liệu (metadata / 메타데이터).

Các facts trên phải được re-check khi baseline đổi sang Python 3.15+.

> **Chuyển mạch:** Terminology audit làm rõ tên gọi trước khi kiểm tra owner. **Boundary và duplicate audit** dùng tên gọi đó để phát hiện nội dung lấn sang chapter hoặc lặp lại nguồn khác.

## 6. Terminology kiểm tra (audit / 감사)

Giải thích chính dùng tiếng Việt. API, mô-đun (module / 모듈), lớp (class / 클래스), phương thức (method / 메서드), tiêu chuẩn (standard / 표준), command, identifier và mã (code / 코드) giữ nguyên bản gốc. `GLOSSARY.md` là chuẩn gốc (canonical / 정본) ánh xạ (mapping / 매핑) theo format `tiếng Việt (English term / 한국어 용어)` khi Korean ánh xạ (mapping / 매핑) thực sự hữu ích.

Glossary không thay thế explanation. Chapter vẫn phải nói concept tồn tại để giải quyết vấn đề gì, cơ chế (mechanism / 메커니즘) nào tạo hành vi (behavior / 동작) và thất bại (failure / 실패)/hiệu năng (performance / 성능)/bảo mật (security / 보안) implication khi có.

Các deepening pass mới đã bổ sung ánh xạ (mapping / 매핑) cho class-creation hooks, luồng thực thi (thread / 스레드) trạng thái (state / 상태)/per-interpreter trạng thái (state / 상태), scheduler fairness, bounded tính đồng thời (concurrency / 동시성), hàng đợi (queue / 큐) shutdown, chỉ số (metric / 지표) cardinality, readiness/liveness và graceful shutdown; không tạo glossary phụ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thư viện kiến thức Python (Python knowledge library / 파이썬 지식 라이브러리) — Coverage & Final kiểm tra (audit / 감사)**, **6. Terminology kiểm tra (audit / 감사)** đã nêu tiêu chí phân biệt, còn **7. ranh giới (boundary / 경계) và duplicate kiểm tra (audit / 감사)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **8. Internal-link kiểm tra (audit / 감사)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. ranh giới (boundary / 경계) và duplicate kiểm tra (audit / 감사)

Python cốt lõi (core / 핵심) không đào sâu FastAPI routing/DI/ASGI internals, `httpx` API cụ thể, AI khung phần mềm (framework / 프레임워크), kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링) khung phần mềm (framework / 프레임워크), phân tán (distributed / 분산) bộ nhớ đệm (cache / 캐시) sản phẩm (product / 제품), khả năng quan sát (observability / 관측 가능성) backend cụ thể hoặc C/Rust extension hiện thực (implementation / 구현) tutorial đầy đủ.

Part 4 chỉ đi đủ sâu vào C/bản địa (native / 네이티브) ranh giới (boundary / 경계) để ứng dụng (application / 애플리케이션) engineer hiểu năng lực (capability / 역량)/ABI/runtime-assumption của phụ thuộc (dependency / 의존성). Chi tiết tự viết extension C/Rust, allocator internals, low-level vận chuyển (transport / 전송)/TLS hiện thực (implementation / 구현) vẫn là specialization ranh giới (boundary / 경계).

`ENGINEERING_CASE_STUDIES.md` chỉ dùng `automation/` như bằng chứng (evidence / 증거)/capstone, không biến framework-specific API thành Python cốt lõi (core / 핵심).

Không có `_v2`, `_final`, `_updated`, `_rewrite`, chapter Pythonic riêng, anti-pattern riêng hoặc cấp cao (senior / 시니어) Notes riêng. Nội dung đúng được consolidate vào bốn chuẩn gốc (canonical / 정본) part.

> **Chuyển mạch:** Trong **Thư viện kiến thức Python (Python knowledge library / 파이썬 지식 라이브러리) — Coverage & Final kiểm tra (audit / 감사)**, **7. ranh giới (boundary / 경계) và duplicate kiểm tra (audit / 감사)** đã nêu tiêu chí phân biệt, còn **8. Internal-link kiểm tra (audit / 감사)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **9. độ sâu (depth / 깊이) kiểm tra (audit / 감사) sau deepening passes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Internal-link kiểm tra (audit / 감사)

Các cross-link quan trọng được giữ:

- `../../automation/repo_audit.py`
- `../../prompt/DOCS_AUDIT_PROMPT.md`
- `../../prompt/DOCS_REVIEW_PROMPT.md`
- `../../automation/README.md`
- `../../computer_science/README.md`

Python README link tới bốn part, trường hợp (case / 사례) studies, glossary và kiểm tra (audit / 감사) bằng relative paths. gốc (root / 루트) README phải link trực tiếp `10_backend/python/README.md` sau mỗi rebase/squash lên latest `main`.

> **Chuyển mạch:** Internal-link audit chỉ chứng minh đi được tới tài liệu; **depth audit** kiểm tra nội dung đã đủ reasoning sau các lần mở rộng chưa. Sau đó canonical source set xác nhận claim bằng nguồn owner.

## 9. độ sâu (depth / 깊이) kiểm tra (audit / 감사) sau deepening passes

Part 1 hiện đi từ thực thi (execution / 실행)/evaluation tới binding/quyền sở hữu (ownership / 소유권)/exception ranh giới (boundary / 경계).

Part 2 nối usage-level giao thức (protocol / 프로토콜) với underlying ngữ nghĩa (semantics / 의미론): descriptor-backed thuộc tính (property / 속성), iterator mutation/vòng đời (lifecycle / 생명주기), sync→async generator, context-manager suppression, typing variance/narrowing, buffer giao thức (protocol / 프로토콜)/view ngữ nghĩa (semantics / 의미론), lược đồ (schema / 스키마) kiểm tra hợp lệ (validation / 검증), civil-time ambiguity và subprocess vòng đời (lifecycle / 생명주기).

Part 3 nối dự án (project / 프로젝트) kỹ thuật (engineering / 엔지니어링) với determinism/bộ nhớ đệm (cache / 캐시)/ngữ cảnh (context / 맥락)/tính đồng thời (concurrency / 동시성): sản phẩm tạo ra (artifact / 산출물) bản dựng (build / 빌드), kiểm thử (test / 테스트) quyền sở hữu (ownership / 소유권) of nondeterminism, retained-state/bộ nhớ đệm (cache / 캐시) vô hiệu hóa (invalidation / 무효화), GIL/free-threaded di chuyển (migration / 마이그레이션), structured async thất bại (failure / 실패), ngữ cảnh (context / 맥락) propagation, thử lại (retry / 재시도)/deadline/idempotency và triển khai (deployment / 배포) tiến trình (process / 프로세스) mô hình (model / 모델).

Part 4 hiện đi sâu thêm ở những vùng trước đây còn mỏng: descriptor bộ nhớ đệm (cache / 캐시) tính đúng đắn (correctness / 정확성), class-creation thứ tự (ordering / 순서) và `__classcell__`, thời gian chạy (runtime / 런타임) thread-state/free-threaded nuance, bản địa (native / 네이티브) extension năng lực (capability / 역량) declarations, subinterpreter vs process-global bản địa (native / 네이티브) trạng thái (state / 상태), scheduler fairness vs thành phần nguyên thủy (primitive / 기본 요소) fairness, bounded hàng đợi (queue / 큐)/tính đồng thời (concurrency / 동시성), hàng đợi (queue / 큐) shutdown invariants, telemetry cardinality/sampling/thất bại (failure / 실패) chính sách (policy / 정책) và signal-driven graceful shutdown.

Những vùng vẫn chưa cần tách tài liệu riêng: CPython allocator/GC tầng mã nguồn (source-level / 소스 수준) hiện thực (implementation / 구현), tự viết C/Rust extension, low-level asyncio vận chuyển (transport / 전송)/giao thức (protocol / 프로토콜), TLS internals, parser/trình biên dịch (compiler / 컴파일러) construction, OS scheduler internals và framework-specific metaprogramming. Nếu nhu cầu thực tế xuất hiện, ưu tiên cross-link Khoa học máy tính (computer science / 컴퓨터 과학) hoặc mở rộng Part 4 trước; chỉ tách tệp (file / 파일) khi phụ thuộc (dependency / 의존성) riêng đủ lớn.

> **Chuyển mạch:** Khi depth audit đã chỉ ra đoạn cần giữ hoặc viết lại, canonical source set đối chiếu từng claim với tài liệu Python chính thức. Đây là điều kiện cuối trước khi ghi coverage là đã có bằng chứng.

## 10. chuẩn gốc (canonical / 정본) nguồn (source / 소스) set

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

> **Bàn giao:** Sau **10. chuẩn gốc (canonical / 정본) nguồn (source / 소스) set**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
