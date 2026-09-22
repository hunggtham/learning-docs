# Python Glossary — Việt / English / 한국어

Glossary này chuẩn hóa các thuật ngữ quan trọng xuất hiện xuyên suốt Python Knowledge Library. Mục đích là giúp nhận diện cùng một concept khi đọc tài liệu Việt, documentation tiếng Anh hoặc tài liệu kỹ thuật Hàn Quốc. Đây không phải danh sách để học thuộc; phần giải thích đầy đủ vẫn nằm trong các chapter canonical.

## Execution, object và data

| Thuật ngữ chuẩn | Ý nghĩa ngắn |
|---|---|
| mã nguồn (source code / 소스 코드) | Văn bản chương trình trước khi runtime xử lý. |
| trình thông dịch (interpreter / 인터프리터) | Implementation thực thi semantics của Python; CPython là implementation phổ biến nhất. |
| đối tượng (object / 객체) | Đơn vị runtime có identity, type và value/state. |
| ràng buộc tên (name binding / 이름 바인딩) | Liên kết một name trong namespace với một object. |
| tham chiếu (reference / 참조) | Liên hệ cho phép một binding/container chỉ tới object. |
| quyền sở hữu trạng thái (state ownership / 상태 소유권) | Quy ước xác định component nào chịu trách nhiệm tạo, mutate, chia sẻ và kết thúc lifecycle của state. |
| định danh đối tượng (object identity / 객체 식별성) | Danh tính của object; `is` kiểm tra hai expression có chỉ cùng object hay không. |
| bằng nhau về giá trị (equality / 동등성) | Quan hệ giá trị do type định nghĩa, thường được kiểm tra bằng `==`. |
| khả năng băm (hashability / 해시 가능성) | Khả năng cung cấp hash ổn định phù hợp equality contract để dùng trong hash-based collection. |
| khả biến (mutable / 가변) | Object có thể đổi state quan sát được mà vẫn giữ identity. |
| bất biến (immutable / 불변) | Value của object không được mutate sau khi tạo. |
| bản sao nông (shallow copy / 얕은 복사) | Tạo container ngoài mới nhưng vẫn chia sẻ references tới object con. |
| bản sao sâu (deep copy / 깊은 복사) | Cố sao chép đệ quy object graph theo semantics của từng type. |
| đánh giá đoản mạch (short-circuit evaluation / 단락 평가) | Cơ chế dừng evaluate `and`/`or` khi operand hiện tại đã đủ quyết định operand được trả về. |
| văn bản Unicode (Unicode text / 유니코드 텍스트) | Text ở dạng `str`, tách khỏi representation byte cụ thể. |
| dãy byte (byte sequence / 바이트 시퀀스) | Binary data như `bytes`; cần encoding/decoding khi chuyển với text. |
| luồng điều khiển (control flow / 제어 흐름) | Quy tắc quyết định statement/expression nào được thực thi tiếp theo. |

## Function, scope và error

| Thuật ngữ chuẩn | Ý nghĩa ngắn |
|---|---|
| hàm (function / 함수) | Callable object đóng gói behavior và tạo local execution scope khi được gọi. |
| tham số (parameter / 매개변수) | Tên được khai báo trong function definition. |
| đối số (argument / 인자) | Value/object được truyền tại call site. |
| phạm vi (scope / 스코프) | Vùng áp dụng của name binding và name resolution. |
| bao đóng (closure / 클로저) | Function giữ liên hệ với binding ở enclosing scope. |
| phương thức đã gắn (bound method / 바운드 메서드) | Method object đã gắn instance/class làm receiver thông qua descriptor binding. |
| ngoại lệ (exception / 예외) | Object biểu diễn failure/control-flow path bất thường. |
| nhóm ngoại lệ (ExceptionGroup / 예외 그룹) | Object chứa nhiều exception độc lập để giữ đồng thời nhiều failure, thường hữu ích trong structured concurrency. |
| lan truyền ngoại lệ (exception propagation / 예외 전파) | Cơ chế exception đi ngược call stack cho tới handler phù hợp. |
| mô-đun (module / 모듈) | Unit import/execution tạo module namespace. |
| gói (package / 패키지) | Cấu trúc tổ chức module trong import namespace. |

## Object model, protocol và typing

| Thuật ngữ chuẩn | Ý nghĩa ngắn |
|---|---|
| lớp (class / 클래스) | Object mô tả construction, behavior và attribute lookup cho instances. |
| thể hiện (instance / 인스턴스) | Object được tạo theo class/type. |
| mô hình dữ liệu (data model / 데이터 모델) | Hệ protocol định nghĩa cách object tương tác với syntax và built-ins. |
| phương thức đặc biệt (special method, dunder method / 특수 메서드) | Method như `__iter__`, `__len__`, `__enter__` tham gia protocol của Python. |
| bộ mô tả (descriptor / 디스크립터) | Object dùng `__get__`, `__set__`, `__delete__` để can thiệp attribute access. |
| bộ mô tả dữ liệu (data descriptor / 데이터 디스크립터) | Descriptor có `__set__` hoặc `__delete__`, được ưu tiên hơn instance dictionary trong normal lookup. |
| bộ mô tả không dữ liệu (non-data descriptor / 비데이터 디스크립터) | Descriptor chỉ có `__get__`; instance attribute cùng tên có thể shadow nó. |
| siêu lớp (metaclass / 메타클래스) | Class của class; hook kiểm soát quá trình tạo class object và behavior ở cấp type. |
| chuẩn bị namespace lớp (`__prepare__` / 클래스 네임스페이스 준비) | Hook metaclass tạo mapping dùng để execute class body trước khi class object được tạo. |
| hook tên descriptor (`__set_name__` / 디스크립터 이름 훅) | Callback giúp descriptor biết owner class và attribute name khi class được tạo. |
| hook khởi tạo subclass (`__init_subclass__` / 서브클래스 초기화 훅) | Hook của parent chạy khi subclass mới được tạo, phù hợp validate/register subclass. |
| kế thừa (inheritance / 상속) | Quan hệ class cho phép reuse/specialize behavior theo MRO. |
| kết hợp (composition / 합성) | Xây object bằng cách sở hữu/sử dụng object khác thay vì hierarchy kế thừa. |
| lớp dữ liệu (data class / 데이터 클래스) | Class thiên về record/value, có thể dùng `@dataclass` để sinh boilerplate. |
| có thể lặp (iterable / 이터러블) | Object có thể cung cấp iterator. |
| bộ lặp (iterator / 이터레이터) | Object giữ iteration state và cung cấp phần tử kế tiếp. |
| bộ sinh (generator / 제너레이터) | Iterator dựa trên suspended function state, thường tạo bằng `yield`. |
| có thể lặp bất đồng bộ (async iterable / 비동기 이터러블) | Object cung cấp async iterator qua `__aiter__()`. |
| bộ lặp bất đồng bộ (async iterator / 비동기 이터레이터) | Iterator có `__anext__()` trả awaitable và kết thúc bằng `StopAsyncIteration`. |
| bộ sinh bất đồng bộ (async generator / 비동기 제너레이터) | Generator viết bằng `async def` + `yield`, cho phép vừa `await` vừa streaming item. |
| trình quản lý ngữ cảnh (context manager / 컨텍스트 매니저) | Protocol quản lý acquire/use/release quanh `with` hoặc `async with`. |
| bộ trang trí (decorator / 데코레이터) | Callable/class transformer áp dụng ở definition time. |
| gợi ý kiểu (type hint / 타입 힌트) | Metadata kiểu phục vụ static analysis/tooling; Python runtime không tự enforce toàn bộ. |
| kiểu cấu trúc (structural typing / 구조적 타이핑) | Compatibility dựa trên shape/behavior thay vì bắt buộc nominal inheritance. |
| phương sai (variance / 변성) | Quan hệ giữa subtype của type parameter và subtype của generic container; chịu ảnh hưởng trực tiếp bởi quyền read/write của API. |
| kiểu bản thân (`Self` / 자기 타입) | Type đại diện dynamic class hiện tại, hữu ích cho fluent API và alternative constructor. |
| thu hẹp kiểu (type narrowing / 타입 좁히기) | Dùng evidence runtime/control flow để giảm tập type khả dĩ mà static checker đang xét. |
| predicate kiểu (`TypeIs`/`TypeGuard` / 타입 판별 함수) | Function boolean cung cấp bằng chứng narrowing cho type checker; implementation phải khớp contract đã khai báo. |

## I/O và standard-library engineering

| Thuật ngữ chuẩn | Ý nghĩa ngắn |
|---|---|
| nhập/xuất (I/O / 입출력) | Giao tiếp với file, network, process hoặc external device/service. |
| giao thức bộ đệm (buffer protocol / 버퍼 프로토콜) | Protocol cho phép object expose vùng dữ liệu nhị phân để consumer truy cập mà không bắt buộc copy trung gian. |
| khung nhìn bộ nhớ (`memoryview` / 메모리 뷰) | Object giữ view lên buffer; slicing có thể tiếp tục tham chiếu cùng underlying storage. |
| tuần tự hóa (serialization / 직렬화) | Chuyển dữ liệu/object sang representation để lưu hoặc truyền. |
| thời gian có múi giờ (aware datetime / 시간대 인식 datetime) | `datetime` có timezone information phù hợp cho instant/civil-time reasoning. |
| thời gian dân sự địa phương (local civil time / 현지 민간 시간) | Thời gian theo lịch/đồng hồ của một timezone; có thể ambiguous hoặc không tồn tại ở một số DST transition. |
| biểu thức chính quy (regular expression / 정규 표현식) | Ngôn ngữ pattern dùng để khớp chuỗi theo grammar giới hạn. |
| ghi nhật ký (logging / 로깅) | Ghi semantic events/context để quan sát và điều tra hệ thống. |
| tiến trình con (subprocess / 하위 프로세스) | Process được application tạo và điều khiển qua OS boundary. |

## Project, packaging, testing và runtime

| Thuật ngữ chuẩn | Ý nghĩa ngắn |
|---|---|
| môi trường ảo (virtual environment / 가상 환경) | Environment tách interpreter context/site-packages của project khỏi global Python. |
| gói phân phối (distribution package / 배포 패키지) | Artifact/metadata được installer phân phối, không nhất thiết trùng tên import package. |
| gói import (import package / 임포트 패키지) | Package namespace được Python import. |
| bản phân phối nguồn (source distribution, sdist / 소스 배포판) | Artifact chứa source và metadata cần để build package trên environment đích. |
| wheel nhị phân (binary wheel / 바이너리 휠) | Distribution artifact có thể chứa native code và vì vậy phụ thuộc compatibility tags của Python/ABI/platform. |
| khả năng tái lập (reproducibility / 재현 가능성) | Khả năng tái tạo cùng build/environment/behavior từ inputs đã kiểm soát thay vì phụ thuộc state ngầm của máy. |
| nhóm phụ thuộc (dependency group / 의존성 그룹) | Nhóm requirement trong `pyproject.toml` phục vụ development/internal workflow và không trở thành runtime dependency metadata của built distribution. |
| kiểm thử đơn vị (unit test / 단위 테스트) | Test một behavior nhỏ với dependency được kiểm soát. |
| kiểm thử tích hợp (integration test / 통합 테스트) | Test interaction giữa nhiều component/boundary thật hơn. |
| kiểm thử xác định (deterministic testing / 결정적 테스트) | Test kiểm soát clock/random/environment và các nguồn nondeterminism để cùng inputs + dependencies cho behavior dự đoán được. |
| bất biến (invariant / 불변 조건) | Điều kiện correctness phải luôn được duy trì qua các state transition hợp lệ. |
| kiểm thử dựa trên thuộc tính (property-based testing / 속성 기반 테스트) | Kiểm tra invariant trên nhiều input được sinh thay vì chỉ vài example cố định. |
| kiểm thử fuzz (fuzz testing / 퍼즈 테스트) | Sinh hoặc biến đổi input để tìm crash, violation hoặc edge case ngoài tập ví dụ dự kiến. |
| bộ nhớ đệm (cache / 캐시) | Retained state đổi memory/freshness complexity lấy việc tránh computation hoặc I/O lặp lại. |
| vô hiệu hóa cache (cache invalidation / 캐시 무효화) | Cơ chế loại bỏ hoặc làm stale entry hết hiệu lực khi source-of-truth thay đổi. |
| trình gỡ lỗi (debugger / 디버거) | Tool cho phép quan sát execution state và control flow. |
| lập hồ sơ hiệu năng (profiling / 프로파일링) | Đo nơi CPU/time/allocation thực sự được tiêu thụ. |
| thu gom rác (garbage collection / 가비지 컬렉션) | Cơ chế reclaim object không còn reachable theo runtime model. |
| đặc tả ngôn ngữ (language specification / 언어 명세) | Contract semantics của Python độc lập với một implementation cụ thể. |
| hiện thực (implementation / 구현) | Chương trình thực thi Python, ví dụ CPython, PyPy. |
| trạng thái luồng Python (thread state / 파이썬 스레드 상태) | Runtime state gắn thread đang sử dụng Python C API; vẫn cần thiết cả khi chạy free-threaded build. |
| trạng thái theo interpreter (per-interpreter state / 인터프리터별 상태) | State tách theo interpreter thay vì dùng singleton process-global state, quan trọng với subinterpreter/native extension. |

## Concurrency và production

| Thuật ngữ chuẩn | Ý nghĩa ngắn |
|---|---|
| đồng thời (concurrency / 동시성) | Nhiều task có tiến trình chồng lấn theo thời gian. |
| song song (parallelism / 병렬성) | Nhiều computation thực sự chạy đồng thời trên nhiều execution resource. |
| bất đồng bộ (asynchrony / 비동기) | Programming model cho phép suspend/resume thay vì block execution context. |
| trạng thái cục bộ theo ngữ cảnh (context-local state / 컨텍스트 로컬 상태) | State gắn với execution context hiện tại thay vì một global binding dùng chung cho mọi work. |
| biến ngữ cảnh (`ContextVar` / 컨텍스트 변수) | Primitive lưu context-local value và được `asyncio` hỗ trợ native cho task context. |
| khóa thông dịch toàn cục (Global Interpreter Lock, GIL / 전역 인터프리터 잠금) | Lock của CPython GIL-enabled liên quan execution trên Python objects/bytecode; không phải application-level lock. |
| trình thông dịch con (subinterpreter / 서브인터프리터) | Interpreter state độc lập tồn tại trong cùng process; isolation khác thread thường và process riêng. |
| executor (executor / 실행기) | Abstraction nhận callable/task rồi giao cho pool execution resource như thread, process hoặc interpreter. |
| kết quả tương lai (Future / 퓨처) | Object đại diện cho computation sẽ hoàn thành sau; `concurrent.futures.Future` và `asyncio.Future` thuộc hai execution model khác nhau. |
| vòng lặp sự kiện (event loop / 이벤트 루프) | Scheduler phối hợp tasks, callbacks, timers và I/O readiness trong async runtime. |
| coroutine (coroutine / 코루틴) | Computation có thể suspend và resume tại các điểm await/yield phù hợp. |
| công bằng lập lịch (scheduler fairness / 스케줄러 공정성) | Mức độ scheduler cho các runnable unit cơ hội tiến triển; không được suy ra chỉ từ fairness của một lock/primitive. |
| áp lực ngược (backpressure / 역압) | Cơ chế buộc producer chậm lại khi consumer/downstream không theo kịp. |
| đồng thời bị chặn giới hạn (bounded concurrency / 제한된 동시성) | Giới hạn số operation đang chạy; khác với giới hạn số item đang chờ trong queue. |
| tắt hàng đợi (queue shutdown / 큐 종료) | Protocol ngừng nhận item mới rồi drain hoặc abandon work theo policy, thay vì để producer/consumer treo vô hạn. |
| đồng thời có cấu trúc (structured concurrency / 구조적 동시성) | Mô hình trong đó task có owner/lifecycle/failure scope rõ ràng. |
| tính lặp an toàn (idempotency / 멱등성) | Thuộc tính cho phép lặp lại operation mà không tạo thêm effect ngoài semantics mong muốn, rất quan trọng cho retry. |
| thời hạn (deadline / 마감 시간) | Mốc thời gian tối đa cho toàn operation; khác với timeout cục bộ của từng bước. |
| retry budget (retry budget / 재시도 예산) | Giới hạn tổng tài nguyên/thời gian/số lần dành cho retry để tránh retry storm và latency không giới hạn. |
| khả năng quan sát (observability / 관측 가능성) | Khả năng suy ra trạng thái hệ thống từ log, metric, trace và evidence runtime. |
| cardinality metric (metric cardinality / 메트릭 카디널리티) | Số combination label/value khác nhau của time series; cardinality quá cao làm tăng memory, cost và query pressure. |
| sẵn sàng phục vụ (readiness / 준비 상태) | Trạng thái process đã đủ dependency/invariant để nhận traffic hoặc work mới. |
| còn sống (liveness / 생존 상태) | Tín hiệu process còn khả năng tiến triển; không đồng nghĩa đã sẵn sàng phục vụ. |
| tắt graceful (graceful shutdown / 정상 종료) | Protocol ngừng nhận work mới, drain/cancel theo policy, đóng resource và exit trong deadline. |
| giao diện nhị phân ứng dụng (ABI, Application Binary Interface / 애플리케이션 바이너리 인터페이스) | Contract nhị phân quyết định compatibility của native extension/wheel với runtime/platform. |

## Cách dùng

Khi một thuật ngữ đã được mapping một lần, chapter có thể dùng English API term hoặc tiếng Việt tự nhiên để giữ mạch đọc. Nếu nghĩa ở Python khác với cách hiểu thông thường của cùng từ, ưu tiên definition trong chapter và Python documentation thay vì dịch từng chữ.
