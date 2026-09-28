# Python Glossary — Việt / English / 한국어

> **Mạch đọc:** Đặt **Python Glossary — Việt / English / 한국어** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **thực thi (execution / 실행), đối tượng (object / 객체) và dữ liệu (data / 데이터)** sang **hàm (function / 함수), phạm vi (scope / 범위) và lỗi (error / 오류)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Glossary này chuẩn hóa các thuật ngữ quan trọng xuất hiện xuyên suốt Thư viện kiến thức Python (Python knowledge library / 파이썬 지식 라이브러리). Mục đích là giúp nhận diện cùng một concept khi đọc tài liệu Việt, documentation tiếng Anh hoặc tài liệu kỹ thuật Hàn Quốc. Đây không phải danh sách để học thuộc; phần giải thích đầy đủ vẫn nằm trong các chapter chuẩn gốc (canonical / 정본).

## Thực thi (execution / 실행), đối tượng (object / 객체) và dữ liệu (data / 데이터)

| Thuật ngữ chuẩn | Ý nghĩa ngắn |
|---|---|
| mã nguồn (source code / 소스 코드) | Văn bản chương trình trước khi thời gian chạy (runtime / 런타임) xử lý. |
| trình thông dịch (interpreter / 인터프리터) | hiện thực (implementation / 구현) thực thi ngữ nghĩa (semantics / 의미론) của Python; CPython là hiện thực (implementation / 구현) phổ biến nhất. |
| đối tượng (object / 객체) | Đơn vị thời gian chạy (runtime / 런타임) có định danh (identity / 식별자), kiểu (type / 타입) và giá trị (value / 값)/trạng thái (state / 상태). |
| ràng buộc tên (name binding / 이름 바인딩) | Liên kết một name trong không gian tên (namespace / 네임스페이스) với một đối tượng (object / 객체). |
| tham chiếu (reference / 참조) | Liên hệ cho phép một binding/bộ chứa (container / 컨테이너) chỉ tới đối tượng (object / 객체). |
| quyền sở hữu trạng thái (state ownership / 상태 소유권) | Quy ước xác định thành phần (component / 컴포넌트) nào chịu trách nhiệm tạo, mutate, chia sẻ và kết thúc vòng đời (lifecycle / 생명주기) của trạng thái (state / 상태). |
| định danh đối tượng (object identity / 객체 식별성) | Danh tính của đối tượng (object / 객체); `is` kiểm tra hai expression có chỉ cùng đối tượng (object / 객체) hay không. |
| bằng nhau về giá trị (equality / 동등성) | Quan hệ giá trị do kiểu (type / 타입) định nghĩa, thường được kiểm tra bằng `==`. |
| khả năng băm (hashability / 해시 가능성) | Khả năng cung cấp băm (hash / 해시) ổn định phù hợp equality đặc tả hợp đồng (contract / 계약) để dùng trong hash-based collection. |
| khả biến (mutable / 가변) | đối tượng (object / 객체) có thể đổi trạng thái (state / 상태) quan sát được mà vẫn giữ định danh (identity / 식별자). |
| bất biến (immutable / 불변) | giá trị (value / 값) của đối tượng (object / 객체) không được mutate sau khi tạo. |
| bản sao nông (shallow copy / 얕은 복사) | Tạo bộ chứa (container / 컨테이너) ngoài mới nhưng vẫn chia sẻ references tới đối tượng (object / 객체) con. |
| bản sao sâu (deep copy / 깊은 복사) | Cố sao chép đệ quy đối tượng (object / 객체) đồ thị (graph / 그래프) theo ngữ nghĩa (semantics / 의미론) của từng kiểu (type / 타입). |
| đánh giá đoản mạch (short-circuit evaluation / 단락 평가) | Cơ chế dừng evaluate `and`/`or` khi operand hiện tại đã đủ quyết định operand được trả về. |
| văn bản Unicode (Unicode text / 유니코드 텍스트) | văn bản (text / 텍스트) ở dạng `str`, tách khỏi biểu diễn (representation / 표현) byte cụ thể. |
| dãy byte (byte sequence / 바이트 시퀀스) | nhị phân (binary / 이진) dữ liệu (data / 데이터) như `bytes`; cần encoding/decoding khi chuyển với văn bản (text / 텍스트). |
| luồng điều khiển (control flow / 제어 흐름) | Quy tắc quyết định statement/expression nào được thực thi tiếp theo. |


> **Chuyển mạch:** Từ **thực thi (execution / 실행), đối tượng (object / 객체) và dữ liệu (data / 데이터)**, ta sang **hàm (function / 함수), phạm vi (scope / 범위) và lỗi (error / 오류)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Hàm (function / 함수), phạm vi (scope / 범위) và lỗi (error / 오류)

| Thuật ngữ chuẩn | Ý nghĩa ngắn |
|---|---|
| hàm (function / 함수) | Callable đối tượng (object / 객체) đóng gói hành vi (behavior / 동작) và tạo cục bộ (local / 로컬) thực thi (execution / 실행) phạm vi (scope / 범위) khi được gọi. |
| tham số (parameter / 매개변수) | Tên được khai báo trong hàm (function / 함수) definition. |
| đối số (argument / 인자) | giá trị (value / 값)/đối tượng (object / 객체) được truyền tại lời gọi (call / 호출) site. |
| phạm vi (scope / 스코프) | Vùng áp dụng của name binding và name resolution. |
| bao đóng (closure / 클로저) | hàm (function / 함수) giữ liên hệ với binding ở enclosing phạm vi (scope / 범위). |
| phương thức đã gắn (bound method / 바운드 메서드) | phương thức (method / 메서드) đối tượng (object / 객체) đã gắn instance/lớp (class / 클래스) làm receiver thông qua descriptor binding. |
| ngoại lệ (exception / 예외) | đối tượng (object / 객체) biểu diễn thất bại (failure / 실패)/control-flow đường dẫn (path / 경로) bất thường. |
| nhóm ngoại lệ (ExceptionGroup / 예외 그룹) | đối tượng (object / 객체) chứa nhiều exception độc lập để giữ đồng thời nhiều thất bại (failure / 실패), thường hữu ích trong structured tính đồng thời (concurrency / 동시성). |
| lan truyền ngoại lệ (exception propagation / 예외 전파) | Cơ chế exception đi ngược ngăn xếp lời gọi (call stack / 호출 스택) cho tới handler phù hợp. |
| mô-đun (module / 모듈) | đơn vị (unit / 단위) import/thực thi (execution / 실행) tạo mô-đun (module / 모듈) không gian tên (namespace / 네임스페이스). |
| gói (package / 패키지) | Cấu trúc tổ chức mô-đun (module / 모듈) trong import không gian tên (namespace / 네임스페이스). |


> **Chuyển mạch:** Từ **hàm (function / 함수), phạm vi (scope / 범위) và lỗi (error / 오류)**, ta sang **mô hình đối tượng (object model / 객체 모델), giao thức (protocol / 프로토콜) và typing** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình đối tượng (object model / 객체 모델), giao thức (protocol / 프로토콜) và typing

| Thuật ngữ chuẩn | Ý nghĩa ngắn |
|---|---|
| lớp (class / 클래스) | đối tượng (object / 객체) mô tả construction, hành vi (behavior / 동작) và attribute lookup cho instances. |
| thể hiện (instance / 인스턴스) | đối tượng (object / 객체) được tạo theo lớp (class / 클래스)/kiểu (type / 타입). |
| mô hình dữ liệu (data model / 데이터 모델) | Hệ giao thức (protocol / 프로토콜) định nghĩa cách đối tượng (object / 객체) tương tác với cú pháp (syntax / 문법) và built-ins. |
| phương thức đặc biệt (special method, dunder method / 특수 메서드) | phương thức (method / 메서드) như `__iter__`, `__len__`, `__enter__` tham gia giao thức (protocol / 프로토콜) của Python. |
| bộ mô tả (descriptor / 디스크립터) | đối tượng (object / 객체) dùng `__get__`, `__set__`, `__delete__` để can thiệp attribute truy cập (access / 접근). |
| bộ mô tả dữ liệu (data descriptor / 데이터 디스크립터) | Descriptor có `__set__` hoặc `__delete__`, được ưu tiên hơn instance dictionary trong normal lookup. |
| bộ mô tả không dữ liệu (non-data descriptor / 비데이터 디스크립터) | Descriptor chỉ có `__get__`; instance attribute cùng tên có thể shadow nó. |
| siêu lớp (metaclass / 메타클래스) | lớp (class / 클래스) của lớp (class / 클래스); hook kiểm soát quá trình tạo lớp (class / 클래스) đối tượng (object / 객체) và hành vi (behavior / 동작) ở cấp kiểu (type / 타입). |
| chuẩn bị không gian tên (namespace / 네임스페이스) lớp (`__prepare__` / 클래스 네임스페이스 준비) | Hook metaclass tạo ánh xạ (mapping / 매핑) dùng để execute lớp (class / 클래스) body trước khi lớp (class / 클래스) đối tượng (object / 객체) được tạo. |
| hook tên descriptor (`__set_name__` / 디스크립터 이름 훅) | Callback giúp descriptor biết đơn vị sở hữu (owner / 오너) lớp (class / 클래스) và attribute name khi lớp (class / 클래스) được tạo. |
| hook khởi tạo subclass (`__init_subclass__` / 서브클래스 초기화 훅) | Hook của parent chạy khi subclass mới được tạo, phù hợp validate/register subclass. |
| kế thừa (inheritance / 상속) | Quan hệ lớp (class / 클래스) cho phép reuse/specialize hành vi (behavior / 동작) theo MRO. |
| kết hợp (composition / 합성) | Xây đối tượng (object / 객체) bằng cách sở hữu/sử dụng đối tượng (object / 객체) khác thay vì hierarchy kế thừa. |
| lớp dữ liệu (data class / 데이터 클래스) | lớp (class / 클래스) thiên về bản ghi (record / 레코드)/giá trị (value / 값), có thể dùng `@dataclass` để sinh boilerplate. |
| có thể lặp (iterable / 이터러블) | đối tượng (object / 객체) có thể cung cấp iterator. |
| bộ lặp (iterator / 이터레이터) | đối tượng (object / 객체) giữ iteration trạng thái (state / 상태) và cung cấp phần tử kế tiếp. |
| bộ sinh (generator / 제너레이터) | Iterator dựa trên suspended hàm (function / 함수) trạng thái (state / 상태), thường tạo bằng `yield`. |
| có thể lặp bất đồng bộ (async iterable / 비동기 이터러블) | đối tượng (object / 객체) cung cấp async iterator qua `__aiter__()`. |
| bộ lặp bất đồng bộ (async iterator / 비동기 이터레이터) | Iterator có `__anext__()` trả awaitable và kết thúc bằng `StopAsyncIteration`. |
| bộ sinh bất đồng bộ (async generator / 비동기 제너레이터) | Generator viết bằng `async def` + `yield`, cho phép vừa `await` vừa streaming item. |
| trình quản lý ngữ cảnh (context manager / 컨텍스트 매니저) | giao thức (protocol / 프로토콜) quản lý acquire/use/bản phát hành (release / 릴리스) quanh `with` hoặc `async with`. |
| bộ trang trí (decorator / 데코레이터) | Callable/lớp (class / 클래스) transformer áp dụng ở definition thời gian (time / 시간). |
| gợi ý kiểu (type hint / 타입 힌트) | siêu dữ liệu (metadata / 메타데이터) kiểu phục vụ static phân tích (analysis / 분석)/tooling; Python thời gian chạy (runtime / 런타임) không tự enforce toàn bộ. |
| kiểu cấu trúc (structural typing / 구조적 타이핑) | tính tương thích (compatibility / 호환성) dựa trên shape/hành vi (behavior / 동작) thay vì bắt buộc nominal inheritance. |
| phương sai (variance / 변성) | Quan hệ giữa subtype của kiểu (type / 타입) parameter và subtype của generic bộ chứa (container / 컨테이너); chịu ảnh hưởng trực tiếp bởi quyền read/ghi (write / 쓰기) của API. |
| kiểu bản thân (`Self` / 자기 타입) | kiểu (type / 타입) đại diện động (dynamic / 동적) lớp (class / 클래스) hiện tại, hữu ích cho fluent API và alternative constructor. |
| thu hẹp kiểu (type narrowing / 타입 좁히기) | Dùng bằng chứng (evidence / 증거) thời gian chạy (runtime / 런타임)/điều khiển (control / 제어) luồng (flow / 흐름) để giảm tập kiểu (type / 타입) khả dĩ mà static checker đang xét. |
| predicate kiểu (`TypeIs`/`TypeGuard` / 타입 판별 함수) | hàm (function / 함수) boolean cung cấp bằng chứng narrowing cho kiểu (type / 타입) checker; hiện thực (implementation / 구현) phải khớp đặc tả hợp đồng (contract / 계약) đã khai báo. |


> **Chuyển mạch:** Từ **mô hình đối tượng (object model / 객체 모델), giao thức (protocol / 프로토콜) và typing**, ta sang **I/O và standard-library kỹ thuật (engineering / 엔지니어링)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## I/O và standard-library kỹ thuật (engineering / 엔지니어링)

| Thuật ngữ chuẩn | Ý nghĩa ngắn |
|---|---|
| nhập/xuất (I/O / 입출력) | Giao tiếp với tệp (file / 파일), mạng (network / 네트워크), tiến trình (process / 프로세스) hoặc bên ngoài (external / 외부) thiết bị (device / 장치)/dịch vụ (service / 서비스). |
| giao thức bộ đệm (buffer protocol / 버퍼 프로토콜) | giao thức (protocol / 프로토콜) cho phép đối tượng (object / 객체) expose vùng dữ liệu nhị phân để bên tiêu thụ (consumer / 소비자) truy cập mà không bắt buộc bản sao (copy / 복사) trung gian. |
| khung nhìn bộ nhớ (`memoryview` / 메모리 뷰) | đối tượng (object / 객체) giữ view lên buffer; slicing có thể tiếp tục tham chiếu cùng underlying lưu trữ (storage / 저장소). |
| tuần tự hóa (serialization / 직렬화) | Chuyển dữ liệu/đối tượng (object / 객체) sang biểu diễn (representation / 표현) để lưu hoặc truyền. |
| thời gian có múi giờ (aware datetime / 시간대 인식 datetime) | `datetime` có timezone thông tin (information / 정보) phù hợp cho instant/civil-time lập luận (reasoning / 추론). |
| thời gian dân sự địa phương (local civil time / 현지 민간 시간) | Thời gian theo lịch/đồng hồ của một timezone; có thể ambiguous hoặc không tồn tại ở một số DST chuyển tiếp (transition / 전이). |
| biểu thức chính quy (regular expression / 정규 표현식) | Ngôn ngữ mẫu (pattern / 패턴) dùng để khớp chuỗi theo grammar giới hạn. |
| ghi nhật ký (logging / 로깅) | Ghi ngữ nghĩa (semantic / 의미적) events/ngữ cảnh (context / 맥락) để quan sát và điều tra hệ thống. |
| tiến trình con (subprocess / 하위 프로세스) | tiến trình (process / 프로세스) được ứng dụng (application / 애플리케이션) tạo và điều khiển qua OS ranh giới (boundary / 경계). |


> **Chuyển mạch:** Từ **I/O và standard-library kỹ thuật (engineering / 엔지니어링)**, ta sang **dự án (project / 프로젝트), packaging, testing và thời gian chạy (runtime / 런타임)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dự án (project / 프로젝트), packaging, testing và thời gian chạy (runtime / 런타임)

| Thuật ngữ chuẩn | Ý nghĩa ngắn |
|---|---|
| môi trường ảo (virtual environment / 가상 환경) | môi trường (environment / 환경) tách trình thông dịch (interpreter / 인터프리터) ngữ cảnh (context / 맥락)/site-packages của dự án (project / 프로젝트) khỏi toàn cục (global / 전역) Python. |
| gói phân phối (distribution package / 배포 패키지) | sản phẩm tạo ra (artifact / 산출물)/siêu dữ liệu (metadata / 메타데이터) được installer phân phối, không nhất thiết trùng tên import gói (package / 패키지). |
| gói import (import package / 임포트 패키지) | gói (package / 패키지) không gian tên (namespace / 네임스페이스) được Python import. |
| bản phân phối nguồn (source distribution, sdist / 소스 배포판) | sản phẩm tạo ra (artifact / 산출물) chứa nguồn (source / 소스) và siêu dữ liệu (metadata / 메타데이터) cần để bản dựng (build / 빌드) gói (package / 패키지) trên môi trường (environment / 환경) đích. |
| wheel nhị phân (binary wheel / 바이너리 휠) | phân phối (distribution / 분포) sản phẩm tạo ra (artifact / 산출물) có thể chứa bản địa (native / 네이티브) mã (code / 코드) và vì vậy phụ thuộc tính tương thích (compatibility / 호환성) tags của Python/ABI/nền tảng (platform / 플랫폼). |
| khả năng tái lập (reproducibility / 재현 가능성) | Khả năng tái tạo cùng bản dựng (build / 빌드)/môi trường (environment / 환경)/hành vi (behavior / 동작) từ inputs đã kiểm soát thay vì phụ thuộc trạng thái (state / 상태) ngầm của máy. |
| nhóm phụ thuộc (dependency group / 의존성 그룹) | Nhóm yêu cầu (requirement / 요구사항) trong `pyproject.toml` phục vụ development/nội bộ (internal / 내부) workflow và không trở thành thời gian chạy (runtime / 런타임) phụ thuộc (dependency / 의존성) siêu dữ liệu (metadata / 메타데이터) của built phân phối (distribution / 분포). |
| kiểm thử đơn vị (unit test / 단위 테스트) | kiểm thử (test / 테스트) một hành vi (behavior / 동작) nhỏ với phụ thuộc (dependency / 의존성) được kiểm soát. |
| kiểm thử tích hợp (integration test / 통합 테스트) | kiểm thử (test / 테스트) tương tác (interaction / 상호작용) giữa nhiều thành phần (component / 컴포넌트)/ranh giới (boundary / 경계) thật hơn. |
| kiểm thử xác định (deterministic testing / 결정적 테스트) | kiểm thử (test / 테스트) kiểm soát clock/random/môi trường (environment / 환경) và các nguồn nondeterminism để cùng inputs + dependencies cho hành vi (behavior / 동작) dự đoán được. |
| bất biến (invariant / 불변 조건) | Điều kiện tính đúng đắn (correctness / 정확성) phải luôn được duy trì qua các chuyển tiếp trạng thái (state transition / 상태 전이) hợp lệ. |
| kiểm thử dựa trên thuộc tính (property-based testing / 속성 기반 테스트) | Kiểm tra bất biến (invariant / 불변식) trên nhiều đầu vào (input / 입력) được sinh thay vì chỉ vài example cố định. |
| kiểm thử fuzz (fuzz testing / 퍼즈 테스트) | Sinh hoặc biến đổi đầu vào (input / 입력) để tìm crash, violation hoặc trường hợp biên (edge case / 경계 사례) ngoài tập ví dụ dự kiến. |
| bộ nhớ đệm (cache / 캐시) | Retained trạng thái (state / 상태) đổi bộ nhớ (memory / 메모리)/freshness độ phức tạp (complexity / 복잡도) lấy việc tránh computation hoặc I/O lặp lại. |
| vô hiệu hóa bộ nhớ đệm (cache / 캐시) | Cơ chế loại bỏ hoặc làm stale entry hết hiệu lực khi source-of-truth thay đổi. |
| trình gỡ lỗi (debugger / 디버거) | công cụ (tool / 도구) cho phép quan sát thực thi (execution / 실행) trạng thái (state / 상태) và điều khiển (control / 제어) luồng (flow / 흐름). |
| lập hồ sơ hiệu năng (profiling / 프로파일링) | Đo nơi CPU/thời gian (time / 시간)/allocation thực sự được tiêu thụ. |
| thu gom rác (garbage collection / 가비지 컬렉션) | Cơ chế reclaim đối tượng (object / 객체) không còn reachable theo thời gian chạy (runtime / 런타임) mô hình (model / 모델). |
| đặc tả ngôn ngữ (language specification / 언어 명세) | đặc tả hợp đồng (contract / 계약) ngữ nghĩa (semantics / 의미론) của Python độc lập với một hiện thực (implementation / 구현) cụ thể. |
| hiện thực (implementation / 구현) | Chương trình thực thi Python, ví dụ CPython, PyPy. |
| trạng thái luồng Python (thread state / 파이썬 스레드 상태) | thời gian chạy (runtime / 런타임) trạng thái (state / 상태) gắn luồng thực thi (thread / 스레드) đang sử dụng Python C API; vẫn cần thiết cả khi chạy free-threaded bản dựng (build / 빌드). |
| trạng thái theo trình thông dịch (interpreter / 인터프리터) | trạng thái (state / 상태) tách theo trình thông dịch (interpreter / 인터프리터) thay vì dùng singleton process-global trạng thái (state / 상태), quan trọng với subinterpreter/bản địa (native / 네이티브) extension. |


> **Chuyển mạch:** Từ **dự án (project / 프로젝트), packaging, testing và thời gian chạy (runtime / 런타임)**, ta sang **tính đồng thời (concurrency / 동시성) và môi trường vận hành (production / 운영 환경)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Tính đồng thời (concurrency / 동시성) và môi trường vận hành (production / 운영 환경)

| Thuật ngữ chuẩn | Ý nghĩa ngắn |
|---|---|
| đồng thời (concurrency / 동시성) | Nhiều tác vụ (task / 작업) có tiến trình chồng lấn theo thời gian. |
| song song (parallelism / 병렬성) | Nhiều computation thực sự chạy đồng thời trên nhiều thực thi (execution / 실행) tài nguyên (resource / 자원). |
| bất đồng bộ (asynchrony / 비동기) | Programming mô hình (model / 모델) cho phép suspend/resume thay vì khối (block / 블록) thực thi (execution / 실행) ngữ cảnh (context / 맥락). |
| trạng thái cục bộ theo ngữ cảnh (context-local state / 컨텍스트 로컬 상태) | trạng thái (state / 상태) gắn với thực thi (execution / 실행) ngữ cảnh (context / 맥락) hiện tại thay vì một toàn cục (global / 전역) binding dùng chung cho mọi công việc (work / 작업). |
| biến ngữ cảnh (`ContextVar` / 컨텍스트 변수) | thành phần nguyên thủy (primitive / 기본 요소) lưu context-local giá trị (value / 값) và được `asyncio` hỗ trợ bản địa (native / 네이티브) cho tác vụ (task / 작업) ngữ cảnh (context / 맥락). |
| khóa thông dịch toàn cục (Global Interpreter Lock, GIL / 전역 인터프리터 잠금) | khóa (lock / 잠금) của CPython GIL-enabled liên quan thực thi (execution / 실행) trên Python objects/bytecode; không phải application-level khóa (lock / 잠금). |
| trình thông dịch con (subinterpreter / 서브인터프리터) | trình thông dịch (interpreter / 인터프리터) trạng thái (state / 상태) độc lập tồn tại trong cùng tiến trình (process / 프로세스); isolation khác luồng thực thi (thread / 스레드) thường và tiến trình (process / 프로세스) riêng. |
| executor (executor / 실행기) | lớp trừu tượng (abstraction / 추상화) nhận callable/tác vụ (task / 작업) rồi giao cho pool thực thi (execution / 실행) tài nguyên (resource / 자원) như luồng thực thi (thread / 스레드), tiến trình (process / 프로세스) hoặc trình thông dịch (interpreter / 인터프리터). |
| kết quả tương lai (Future / 퓨처) | đối tượng (object / 객체) đại diện cho computation sẽ hoàn thành sau; `concurrent.futures.Future` và `asyncio.Future` thuộc hai mô hình thực thi (execution model / 실행 모델) khác nhau. |
| vòng lặp sự kiện (event loop / 이벤트 루프) | Scheduler phối hợp tasks, callbacks, timers và I/O readiness trong async thời gian chạy (runtime / 런타임). |
| coroutine (coroutine / 코루틴) | Computation có thể suspend và resume tại các điểm await/yield phù hợp. |
| công bằng lập lịch (scheduler fairness / 스케줄러 공정성) | Mức độ scheduler cho các runnable đơn vị (unit / 단위) cơ hội tiến triển; không được suy ra chỉ từ fairness của một khóa (lock / 잠금)/thành phần nguyên thủy (primitive / 기본 요소). |
| áp lực ngược (backpressure / 역압) | Cơ chế buộc producer chậm lại khi bên tiêu thụ (consumer / 소비자)/downstream không theo kịp. |
| đồng thời bị chặn giới hạn (bounded concurrency / 제한된 동시성) | Giới hạn số thao tác (operation / 연산) đang chạy; khác với giới hạn số item đang chờ trong hàng đợi (queue / 큐). |
| tắt hàng đợi (queue shutdown / 큐 종료) | giao thức (protocol / 프로토콜) ngừng nhận item mới rồi drain hoặc abandon công việc (work / 작업) theo chính sách (policy / 정책), thay vì để producer/bên tiêu thụ (consumer / 소비자) treo vô hạn. |
| đồng thời có cấu trúc (structured concurrency / 구조적 동시성) | Mô hình trong đó tác vụ (task / 작업) có đơn vị sở hữu (owner / 오너)/vòng đời (lifecycle / 생명주기)/thất bại (failure / 실패) phạm vi (scope / 범위) rõ ràng. |
| tính lặp an toàn (idempotency / 멱등성) | Thuộc tính cho phép lặp lại thao tác (operation / 연산) mà không tạo thêm tác động (effect / 효과) ngoài ngữ nghĩa (semantics / 의미론) mong muốn, rất quan trọng cho thử lại (retry / 재시도). |
| thời hạn (deadline / 마감 시간) | Mốc thời gian tối đa cho toàn thao tác (operation / 연산); khác với hết thời gian chờ (timeout / 타임아웃) cục bộ của từng bước. |
| thử lại (retry / 재시도) ngân sách (budget / 예산) | Giới hạn tổng tài nguyên/thời gian/số lần dành cho thử lại (retry / 재시도) để tránh thử lại (retry / 재시도) storm và độ trễ (latency / 지연 시간) không giới hạn. |
| khả năng quan sát (observability / 관측 가능성) | Khả năng suy ra trạng thái hệ thống từ log, chỉ số (metric / 지표), dấu vết (trace / 추적) và bằng chứng (evidence / 증거) thời gian chạy (runtime / 런타임). |
| cardinality chỉ số (metric / 지표) | Số combination label/giá trị (value / 값) khác nhau của thời gian (time / 시간) series; cardinality quá cao làm tăng bộ nhớ (memory / 메모리), chi phí (cost / 비용) và truy vấn (query / 쿼리) pressure. |
| sẵn sàng phục vụ (readiness / 준비 상태) | Trạng thái tiến trình (process / 프로세스) đã đủ phụ thuộc (dependency / 의존성)/bất biến (invariant / 불변식) để nhận traffic hoặc công việc (work / 작업) mới. |
| còn sống (liveness / 생존 상태) | Tín hiệu tiến trình (process / 프로세스) còn khả năng tiến triển; không đồng nghĩa đã sẵn sàng phục vụ. |
| tắt graceful (graceful shutdown / 정상 종료) | giao thức (protocol / 프로토콜) ngừng nhận công việc (work / 작업) mới, drain/cancel theo chính sách (policy / 정책), đóng tài nguyên (resource / 자원) và exit trong deadline. |
| giao diện nhị phân ứng dụng (ABI, Application Binary Interface / 애플리케이션 바이너리 인터페이스) | đặc tả hợp đồng (contract / 계약) nhị phân quyết định tính tương thích (compatibility / 호환성) của bản địa (native / 네이티브) extension/wheel với thời gian chạy (runtime / 런타임)/nền tảng (platform / 플랫폼). |


> **Chuyển mạch:** Từ **tính đồng thời (concurrency / 동시성) và môi trường vận hành (production / 운영 환경)**, ta sang **Cách dùng** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cách dùng

Khi một thuật ngữ đã được ánh xạ (mapping / 매핑) một lần, chapter có thể dùng English API term hoặc tiếng Việt tự nhiên để giữ mạch đọc. Nếu nghĩa ở Python khác với cách hiểu thông thường của cùng từ, ưu tiên definition trong chapter và Python documentation thay vì dịch từng chữ.

> **Bàn giao:** Sau **Cách dùng**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [COVERAGE AUDIT](./COVERAGE_AUDIT.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
