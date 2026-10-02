# Python Part 4 — Master: thời gian chạy (runtime / 런타임) internals, hiệu năng (performance / 성능), kiến trúc (architecture / 아키텍처) và hiện đại (modern / 현대적)/legacy evolution

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Python Part 4 — Master: thời gian chạy (runtime / 런타임) internals, hiệu năng (performance / 성능), kiến trúc (architecture / 아키텍처) và hiện đại (modern / 현대적)/legacy evolution**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. ngôn ngữ (language / 언어) Python khác hiện thực (implementation / 구현) CPython** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Compile đơn vị (unit / 단위), mã (code / 코드) đối tượng (object / 객체) và bytecode** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối Python Master với runtime, packaging, concurrency và production, để kiến thức nâng cao vẫn quay về quyết định vận hành cụ thể.

> Baseline: Python 3.14.7. Kiểm chứng: 2026-09-22.

Master ở đây không có nghĩa ghi nhớ mọi API. Mục tiêu là có mô hình tư duy (mental model / 사고 모델) đủ sâu để đọc hành vi (behavior / 동작) lạ, điều tra môi trường vận hành (production / 운영 환경) issue, rà soát (review / 검토) thiết kế (design / 설계) và phân biệt đâu là ngôn ngữ (language / 언어) guarantee, đâu là CPython hiện thực (implementation / 구현) detail, đâu là sản phẩm tạo ra (artifact / 산출물) của phiên bản (version / 버전) cũ. Ở mức (level / 수준) này, một câu hỏi tốt thường không còn là “API nào làm việc này?”, mà là “bất biến (invariant / 불변식) nào đang được giữ, thời gian chạy (runtime / 런타임) duy trì bất biến (invariant / 불변식) đó bằng cơ chế nào, và cơ chế ấy thất bại ở ranh giới (boundary / 경계) nào?”.

## 1. ngôn ngữ (language / 언어) Python khác hiện thực (implementation / 구현) CPython

`đặc tả ngôn ngữ (language specification / 언어 명세)`

`hiện thực (implementation / 구현)`

Python ngôn ngữ (language / 언어) tham chiếu (reference / 참조) mô tả ngữ nghĩa (semantics / 의미론) của ngôn ngữ. CPython là hiện thực (implementation / 구현) chuẩn phổ biến, nhưng không phải mọi chi tiết CPython đều là guarantee của Python nói chung. Ví dụ, tham chiếu (reference / 참조) counting và chuyện đối tượng (object / 객체) thường được thu hồi sớm khi refcount về zero là đặc trưng CPython quan trọng; ứng dụng (application / 애플리케이션) portable không nên dùng nó thay tài nguyên (resource / 자원) management tường minh (explicit / 명시적).

Khi đọc một hành vi (behavior / 동작), hãy tách bốn tầng:

1. ngôn ngữ (language / 언어) tham chiếu (reference / 참조) có guarantee không?
2. Standard-library API có đặc tả hợp đồng (contract / 계약) không?
3. Nếu không, đây có phải CPython hiện thực (implementation / 구현) detail?
4. phiên bản (version / 버전), nền tảng (platform / 플랫폼) và bản dựng (build / 빌드) nào đang chạy?

Cách phân lớp này ngăn việc biến observation trên laptop thành “quy tắc Python”. Nó cũng giúp đọc hiệu năng (performance / 성능) claim chính xác hơn. Ví dụ “dictionary lookup O(1) average” là lớp trừu tượng (abstraction / 추상화) thuật toán; chính xác (exact / 정확한) bộ nhớ (memory / 메모리) bố cục (layout / 레이아웃), băm (hash / 해시) hiện thực (implementation / 구현) và bộ nhớ đệm (cache / 캐시) hành vi (behavior / 동작) lại thuộc hiện thực (implementation / 구현)/phiên bản (version / 버전).

> **Chuyển mạch:** CPython implementation đặt ra câu hỏi về language behavior; compile và bytecode cho thấy source được chuyển thành execution units nào. Frame, call stack và traceback tiếp theo làm visible trạng thái đang chạy.

## 2. Compile đơn vị (unit / 단위), mã (code / 코드) đối tượng (object / 객체) và bytecode

Nguồn (source / 소스) mô-đun (module / 모듈)/hàm (function / 함수) được compile thành mã (code / 코드) đối tượng (object / 객체) chứa bytecode/instruction siêu dữ liệu (metadata / 메타데이터), constants, names và thông tin (information / 정보) phục vụ thời gian chạy (runtime / 런타임). Có thể inspect bằng `dis`:

```python
import dis

def add(a, b):
    return a + b

dis.dis(add)
```

Bytecode là hiện thực (implementation / 구현) surface có thể đổi giữa minor releases; đừng bản dựng (build / 빌드) lô-gic nghiệp vụ (business logic / 비즈니스 로직) phụ thuộc chính xác (exact / 정확한) opcode. Nó hữu ích để hiểu chi phí (cost / 비용) mô hình (model / 모델), trình biên dịch (compiler / 컴파일러) tối ưu hóa (optimization / 최적화) hoặc gỡ lỗi (debug / 디버그) tooling.

Hiện đại (modern / 현대적) CPython có specializing adaptive trình thông dịch (interpreter / 인터프리터): thời gian chạy (runtime / 런타임) có thể specialize thực thi (execution / 실행) dựa trên observed types/operations. Điều đó có hai hệ quả. Thứ nhất, “một biểu thức Python luôn tốn N bytecodes” không còn là chi phí (cost / 비용) mô hình (model / 모델) hữu ích. Thứ hai, microbenchmark quá ngắn có thể đo cả warmup/specialization thay vì steady-state hành vi (behavior / 동작).

Python 3.14 còn có optional tail-call trình thông dịch (interpreter / 인터프리터) bản dựng (build / 빌드) cấu hình (configuration / 구성) trong CPython. Tên này không đồng nghĩa Python hàm (function / 함수) tail-call tối ưu hóa (optimization / 최적화); nó là trình thông dịch (interpreter / 인터프리터) hiện thực (implementation / 구현) detail.

> **Chuyển mạch:** Bytecode tạo execution context; frame và traceback cho biết context đó giữ locals, globals và call state ra sao. Namespace, descriptor và attribute lookup tiếp theo giải thích cách tên được resolve trong context ấy.

## 3. Frame, ngăn xếp lời gọi (call stack / 호출 스택) và traceback

Mỗi active Python lời gọi (call / 호출) liên quan thực thi (execution / 실행) frame chứa cục bộ (local / 로컬)/toàn cục (global / 전역) references, instruction trạng thái (state / 상태) và thời gian chạy (runtime / 런타임) ngăn xếp (stack / 스택) trạng thái (state / 상태). Traceback nối frames tại thất bại (failure / 실패) đường dẫn (path / 경로).

Frame introspection (`inspect`, `sys._getframe`) rất mạnh cho debugger/khung phần mềm (framework / 프레임워크) nhưng tạo coupling với thời gian chạy (runtime / 런타임) và có thể giữ đối tượng (object / 객체) đồ thị (graph / 그래프) sống lâu hơn nếu references tới frame/traceback được giữ. Một exception đối tượng (object / 객체) giữ traceback có thể gián tiếp giữ locals, yêu cầu (request / 요청) đối tượng (object / 객체), large buffer hoặc secret lâu hơn dự kiến. Vì vậy diagnostic tooling phải có quyền sở hữu (ownership / 소유권) rõ và bản phát hành (release / 릴리스) references khi chúng hết giá trị.

Exception chaining giữ causality qua `__cause__`/`__context__`. Khi wrap exception, `raise NewError(...) from exc` giúp operator nhìn thấy cả lĩnh vực (domain / 도메인) ngữ cảnh (context / 맥락) lẫn nguyên nhân gốc (root cause / 근본 원인). Nếu cố tình che hiện thực (implementation / 구현) detail bằng `raise ... from None`, hãy chắc rằng khả năng quan sát (observability / 관측 가능성) tầng (layer / 계층) khác vẫn giữ bằng chứng (evidence / 증거) cần thiết; hiding chuỗi (chain / 사슬) để message “đẹp” có thể làm sự cố (incident / 인시던트) khó điều tra.

> **Chuyển mạch:** Frame cho biết nơi lookup diễn ra; namespace và descriptor xác định rule lookup nào thắng. Function object, closure cell và decorator tiếp theo cho thấy các rule đó được giữ trong object graph thế nào.

## 4. không gian tên (namespace / 네임스페이스), descriptor và attribute lookup

Attribute truy cập (access / 접근) `obj.x` không chỉ là lookup trong `obj.__dict__`. mô hình dữ liệu (data model / 데이터 모델) có descriptor giao thức (protocol / 프로토콜), lớp (class / 클래스) MRO và `__getattribute__`/`__getattr__` hooks.

`bộ mô tả (descriptor / 디스크립터)`

Descriptor là đối tượng (object / 객체) định nghĩa `__get__`, `__set__` hoặc `__delete__`. hàm (function / 함수) trên lớp (class / 클래스) là descriptor, nhờ đó `instance.method` trở thành bound phương thức (method / 메서드). `property`, `classmethod`, `staticmethod`, cached attributes, ORM trường dữ liệu (field / 필드) và khung phần mềm (framework / 프레임워크) attribute đều dựa trên cùng nền tảng này.

### Lookup precedence: tại sao cùng tên nhưng kết quả khác nhau?

Với instance lookup thông thường, mô hình tư duy (mental model / 사고 모델) hữu ích là:

```text
1. data descriptor trên class/MRO
2. instance __dict__
3. non-data descriptor trên class/MRO
4. class attribute thông thường
5. __getattr__ fallback nếu lookup trước đó thất bại
```

`data descriptor` là descriptor có `__set__` hoặc `__delete__`; nó ưu tiên hơn instance dictionary. Descriptor chỉ có `__get__` là `non-data descriptor`, nên instance attribute cùng tên có thể shadow nó.

`property` thường là dữ liệu (data / 데이터) descriptor, vì vậy assignment trực tiếp vào `obj.__dict__["name"]` không nhất thiết override thuộc tính (property / 속성) truy cập (access / 접근). Ngược lại, hàm (function / 함수) là non-data descriptor; truy cập hàm (function / 함수) qua instance kích hoạt `__get__` để tạo bound phương thức (method / 메서드).

```python
class Account:
    def deposit(self, amount):
        ...

account = Account()
method = account.deposit

assert method.__self__ is account
assert method.__func__ is Account.deposit
```

`account.deposit(10)` về mô hình tư duy (mental model / 사고 모델) gần với `Account.deposit(account, 10)`, nhưng binding được descriptor machinery thực hiện, không phải parser chèn `self` bằng mẹo đặc biệt.

### Descriptor có thể biến bộ nhớ đệm (cache / 캐시) thành vấn đề tính đúng đắn (correctness / 정확성)

Một mẫu (pattern / 패턴) phổ biến là non-data descriptor hoặc `cached_property` tính giá trị (value / 값) lần đầu rồi lưu vào instance dictionary để lần sau lookup đi thẳng tới cached giá trị (value / 값). Cơ chế này nhanh vì precedence cho phép instance giá trị (value / 값) shadow non-data descriptor, nhưng ngay lập tức tạo một bất biến (invariant / 불변식) mới: cached giá trị (value / 값) còn đúng đến khi nào?

Nếu cached giá trị (value / 값) phụ thuộc `self.config`, `self.locale` hoặc mutable child trạng thái (state / 상태), vô hiệu hóa (invalidation / 무효화) phải đi cùng mutation đường dẫn (path / 경로). Nếu không, bug không nằm ở descriptor giao thức (protocol / 프로토콜) mà ở đặc tả hợp đồng (contract / 계약) freshness. Một cached attribute không phải “tối ưu hóa (optimization / 최적화) thuần túy”; nó tạo retained trạng thái (state / 상태) và consistency obligation giống bộ nhớ đệm (cache / 캐시) ở Part 3.

Khi gỡ lỗi (debug / 디버그) một attribute “không cập nhật”, hãy hỏi ba câu: descriptor có dữ liệu (data / 데이터) hay non-data? giá trị (value / 값) hiện nằm ở lớp (class / 클래스) hay instance dictionary? phụ thuộc (dependency / 의존성) nào thay đổi nhưng bộ nhớ đệm (cache / 캐시) không bị invalidate?

### `__getattribute__` và `__getattr__` không giống nhau

`__getattribute__` tham gia mọi normal attribute truy cập (access / 접근). Nếu override nó và bên trong lại viết `self.name` một cách không kiểm soát, mã (code / 코드) rất dễ recursion vô hạn. Khi cần delegate hành vi (behavior / 동작) mặc định, thường gọi `object.__getattribute__(self, name)` hoặc `super().__getattribute__(name)` theo thiết kế lớp (class / 클래스).

`__getattr__` chỉ là fallback khi normal lookup kết thúc bằng `AttributeError`. Nó phù hợp cho lazy/động (dynamic / 동적) attributes hơn là intercept toàn bộ truy cập (access / 접근).

```python
class Config:
    def __init__(self, values):
        self._values = values

    def __getattr__(self, name):
        try:
            return self._values[name]
        except KeyError as exc:
            raise AttributeError(name) from exc
```

Một pitfall khung phần mềm (framework / 프레임워크)/proxy là catch `AttributeError` quá rộng bên trong thuộc tính (property / 속성)/descriptor rồi vô tình làm thời gian chạy (runtime / 런타임) tưởng attribute không tồn tại và chạy `__getattr__`. Vì vậy khi gỡ lỗi (debug / 디버그) “fallback chạy dù thuộc tính (property / 속성) có thật”, hãy nhìn exception origin, không chỉ tên trường dữ liệu (field / 필드).

Một pitfall khác là proxy `__getattribute__` forward mọi thứ sang mục tiêu (target / 대상), kể cả nội bộ (internal / 내부) attributes của proxy. Proxy tốt phải định nghĩa ranh giới (boundary / 경계) rõ giữa trạng thái (state / 상태) của proxy và trạng thái (state / 상태) được forward; nếu không `__class__`, gỡ lỗi (debug / 디버그) siêu dữ liệu (metadata / 메타데이터), pickling hoặc introspection có thể cho hành vi (behavior / 동작) bất ngờ.

### `__set_name__` và descriptor biết tên của mình

Khi lớp (class / 클래스) được tạo, descriptor có `__set_name__()` có thể nhận đơn vị sở hữu (owner / 오너) lớp (class / 클래스) và attribute name. Đây là cơ chế (mechanism / 메커니즘) mà validator/ORM-style trường dữ liệu (field / 필드) có thể tự biết nó được gắn vào trường dữ liệu (field / 필드) nào mà không lặp string thủ công.

```python
class Positive:
    def __set_name__(self, owner, name):
        self.storage_name = f"_{name}"

    def __get__(self, obj, owner=None):
        if obj is None:
            return self
        return getattr(obj, self.storage_name)

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError("must be positive")
        setattr(obj, self.storage_name, value)
```

Nếu descriptor được gắn vào lớp (class / 클래스) sau khi lớp (class / 클래스) đã tạo, `__set_name__()` không tự được gọi. Đây là trường hợp biên (edge case / 경계 사례) quan trọng với động (dynamic / 동적) khung phần mềm (framework / 프레임워크)/metaprogramming: assignment `A.x = descriptor` không hoàn toàn tương đương khai báo `x = descriptor` trong lớp (class / 클래스) body.

Descriptor mạnh vì nó đưa chính sách (policy / 정책) vào lookup giao thức (protocol / 프로토콜), nhưng cái giá là điều khiển (control / 제어) luồng (flow / 흐름) bớt hiển nhiên. Nếu lô-gic (logic / 논리) chỉ dùng ở một trường dữ liệu (field / 필드) đơn giản, `property` thường dễ đọc hơn. Descriptor đáng dùng khi cùng cơ chế (mechanism / 메커니즘) cần tái sử dụng cho nhiều attributes/classes.

### `__slots__`

`__slots__` có thể thay cách instance lưu attributes và giảm bộ nhớ (memory / 메모리) khi có rất nhiều objects. Nhưng tối ưu hóa (optimization / 최적화) này đi kèm các ràng buộc (constraints / 제약조건들) về động (dynamic / 동적) attributes, inheritance, weak references và tooling. Hãy đo bộ nhớ (memory / 메모리)/profile trước. Với 100 objects, độ phức tạp (complexity / 복잡도) có thể không đáng; với hàng triệu nodes, nó có thể đáng kể.

`__slots__` cũng không tự làm đối tượng (object / 객체) immutable hoặc thread-safe. Nó thay lưu trữ (storage / 저장소) mô hình (model / 모델), không thay quyền sở hữu (ownership / 소유권) ngữ nghĩa (semantics / 의미론).

> **Chuyển mạch:** Descriptor và lookup giải thích function object được tìm thấy và gọi ra sao; closure/decorator thêm state và binding vào call path. Import system tiếp theo mở rộng call path thành module initialization và dependency graph.

## 5. hàm (function / 함수) đối tượng (object / 객체), closure cell và decorator ngăn xếp (stack / 스택)

Hàm (function / 함수) đối tượng (object / 객체) chứa mã (code / 코드) đối tượng (object / 객체), globals tham chiếu (reference / 참조), defaults, closure cells và siêu dữ liệu (metadata / 메타데이터) khác. Điều này giải thích nhiều hiện tượng đã thấy:

- default argument sống cùng hàm (function / 함수) đối tượng (object / 객체);
- closure giữ cell/binding từ enclosing phạm vi (scope / 범위);
- decorator thay hàm (function / 함수) binding bằng đối tượng (object / 객체)/callable khác;
- monkey patch thay name/attribute lookup mục tiêu (target / 대상) chứ không “sửa bytecode đã gọi trước đó”.

`functools.wraps` chủ yếu bản sao (copy / 복사)/cập nhật (update / 업데이트) siêu dữ liệu (metadata / 메타데이터) và `__wrapped__`, hỗ trợ introspection. Nó không làm wrapper biến mất khỏi ngăn xếp lời gọi (call stack / 호출 스택)/chi phí (cost / 비용).

Decorator ngăn xếp (stack / 스택) cũng tạo thứ tự (ordering / 순서) ngữ nghĩa (semantics / 의미론). Với:

```python
@outer
@inner
def work():
    ...
```

Mô hình tư duy (mental model / 사고 모델) là `work = outer(inner(work))`. Nếu `inner` tạo giao dịch (transaction / 트랜잭션) còn `outer` thử lại (retry / 재시도), ngữ nghĩa (semantics / 의미론) khác hẳn khi thứ tự đảo lại. Cross-cutting concern có side tác động (effect / 효과) phải được rà soát (review / 검토) theo thứ tự (ordering / 순서), không chỉ theo từng decorator riêng lẻ.

> **Chuyển mạch:** Function/decorator state có thể giữ module references; import system quyết định khi nào graph đó được tạo và cache. Object lifecycle và GC tiếp theo kiểm tra khi nào graph được giải phóng hoặc giữ lại.

## 6. Import hệ thống (system / 시스템) sâu hơn

Import được xây quanh finders, loaders, mô-đun (module / 모듈) specs và `sys.modules`. Một normal import đầu tiên tạo/đăng ký mô-đun (module / 모듈) đối tượng (object / 객체) rồi execute mã (code / 코드). Việc đưa mô-đun (module / 모듈) vào `sys.modules` sớm giúp xử lý recursive import nhưng cũng khiến circular import có thể thấy partially initialized mô-đun (module / 모듈).

### Import side effects

Plugin registration và khung phần mềm (framework / 프레임워크) startup đôi khi cố ý dựa vào import side tác động (effect / 효과). Nhưng mẫu (pattern / 패턴) này làm phụ thuộc (dependency / 의존성) ẩn, order-sensitive và khó kiểm thử (test / 테스트). Khi có thể, dùng tường minh (explicit / 명시적) registration/bootstrap.

### `__init__.py`, không gian tên (namespace / 네임스페이스) gói (package / 패키지) và API công khai (public API / 공개 API)

Gói (package / 패키지) có thể expose API từ `__init__.py`, nhưng re-export quá nhiều tạo phụ thuộc (dependency / 의존성)/circular-import khó thấy. không gian tên (namespace / 네임스페이스) packages cho phép gói (package / 패키지) phân tán qua nhiều locations theo import rules; chỉ dùng khi phân phối (distribution / 분포) kiến trúc (architecture / 아키텍처) cần, không vì muốn bỏ tệp (file / 파일).

### Import chi phí (cost / 비용)

Cold start của CLI/serverless có thể bị chi phối bởi import đồ thị (graph / 그래프). Profile startup thay vì đoán; lazy import có thể giảm startup nhưng chuyển thất bại (failure / 실패) sang thời gian chạy (runtime / 런타임) và tăng độ phức tạp (complexity / 복잡도).

### Reload không phải trạng thái (state / 상태) reset

`importlib.reload()` re-execute mô-đun (module / 모듈) mã (code / 코드) trong mô-đun (module / 모듈) đối tượng (object / 객체) hiện có, nhưng references đã được bản sao (copy / 복사)/bind ở nơi khác không tự được “rewire” thành definitions mới. Instance cũ cũng vẫn thuộc lớp (class / 클래스) đối tượng (object / 객체) cũ. Vì vậy reload phù hợp cho tooling/development scenario có đặc tả hợp đồng (contract / 계약) rõ; nó không phải generic môi trường vận hành (production / 운영 환경) chiến lược (strategy / 전략) để “refresh cấu hình (config / 설정)/mã (code / 코드)” trong tiến trình (process / 프로세스) sống lâu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Python Part 4 — Master: thời gian chạy (runtime / 런타임) internals, hiệu năng (performance / 성능), kiến trúc (architecture / 아키텍처) và hiện đại (modern / 현대적)/legacy evolution**, **6. Import hệ thống (system / 시스템) sâu hơn** xác định đầu vào; **7. đối tượng (object / 객체) vòng đời (lifecycle / 생명주기), construction, tham chiếu (reference / 참조) counting và cyclic GC** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **8. Immutability, aliasing và API thiết kế (design / 설계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. đối tượng (object / 객체) vòng đời (lifecycle / 생명주기), construction, tham chiếu (reference / 참조) counting và cyclic GC

Trong CPython GIL-enabled bản dựng (build / 빌드) truyền thống, refcount là cơ chế vòng đời (lifecycle / 생명주기) chính và cyclic GC thu cycles. Free-threaded CPython phải thay đổi nhiều synchronization/refcount hiện thực (implementation / 구현) details để threads hoạt động an toàn hơn; ứng dụng (application / 애플리케이션) không nên dựa vào nội bộ (internal / 내부) refcount biểu diễn (representation / 표현).

### `__new__` tạo đối tượng (object / 객체), `__init__` khởi tạo đối tượng (object / 객체) đã tạo

Gọi `MyClass(...)` không đồng nghĩa trực tiếp với gọi `__init__`. Ở mức mô hình tư duy (mental model / 사고 모델), metaclass `type.__call__` điều phối đối tượng (object / 객체) creation: gọi `__new__` để tạo/return đối tượng (object / 객체), sau đó nếu đối tượng (object / 객체) trả về là instance phù hợp thì gọi `__init__` để initialize trạng thái (state / 상태).

```python
class User:
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        return obj

    def __init__(self, name):
        self.name = name
```

`__init__` phải return `None`; nó không chọn đối tượng (object / 객체) nào được trả về. `__new__` đặc biệt hữu ích khi subclass immutable built-ins như `str`, `int`, `tuple`, vì giá trị (value / 값) phải được tạo trước khi `__init__` có cơ hội chạy.

Nếu `__new__` trả đối tượng (object / 객체) không phải instance của lớp (class / 클래스) đang construct, `__init__` tương ứng không chạy. Đây là trường hợp biên (edge case / 경계 사례) metaprogramming/factory mạnh nhưng dễ làm vòng đời (lifecycle / 생명주기) khó đọc; ứng dụng (application / 애플리케이션) mã (code / 코드) thường không cần dùng.

### Finalization không phải tài nguyên (resource / 자원) quyền sở hữu (ownership / 소유권)

`__del__` làm finalization khó reason hơn khi cycles/trình thông dịch (interpreter / 인터프리터) shutdown/tài nguyên (resource / 자원) thứ tự (order / 순서) liên quan. Dùng ngữ cảnh (context / 맥락) manager hoặc tường minh (explicit / 명시적) `close()` quyền sở hữu (ownership / 소유권) cho bên ngoài (external / 외부) resources. “đối tượng (object / 객체) sẽ được GC” không phải đặc tả hợp đồng (contract / 계약) về thời điểm tệp (file / 파일)/socket/giao dịch (transaction / 트랜잭션) được bản phát hành (release / 릴리스).

Weak references phù hợp cho bộ nhớ đệm (cache / 캐시)/observer nơi tham chiếu (reference / 참조) phụ không nên giữ đối tượng (object / 객체) sống. Nhưng weakref callback cũng là vòng đời (lifecycle / 생명주기) độ phức tạp (complexity / 복잡도); không dùng chỉ để “giảm bộ nhớ (memory / 메모리)”.

### Lớp (class / 클래스) creation: lớp (class / 클래스) body cũng là mã (code / 코드) được thực thi

`class C: ...` thực thi lớp (class / 클래스) body để tạo không gian tên (namespace / 네임스페이스) rồi tạo lớp (class / 클래스) đối tượng (object / 객체) thông qua metaclass. Default metaclass phổ biến là `type`.

Quá trình lớp (class / 클래스) creation có thể reason theo thứ tự sau:

```text
resolve MRO entries
→ chọn metaclass
→ metaclass.__prepare__ tạo namespace
→ execute class body vào namespace đó
→ gọi metaclass(name, bases, namespace, ...)
→ type.__new__ tạo class object
→ gọi __set_name__ cho descriptor trong namespace
→ gọi __init_subclass__ trên parent phù hợp
→ áp dụng class decorators
→ bind kết quả cuối vào class name
```

`__prepare__` quan trọng với khung phần mềm (framework / 프레임워크)/metaclass cần custom không gian tên (namespace / 네임스페이스) hành vi (behavior / 동작) trước khi lớp (class / 클래스) body chạy. Nhưng không gian tên (namespace / 네임스페이스) được đưa vào `type.__new__` cuối cùng được bản sao (copy / 복사) vào ánh xạ (mapping / 매핑) riêng của lớp (class / 클래스); giữ tham chiếu (reference / 참조) tới custom không gian tên (namespace / 네임스페이스) rồi giả định mutate nó sẽ mutate lớp (class / 클래스) là mô hình tư duy (mental model / 사고 모델) sai.

Lớp (class / 클래스) body chạy tại definition/import thời gian (time / 시간). Vì vậy truy vấn (query / 쿼리) cơ sở dữ liệu (database / 데이터베이스), đọc môi trường (environment / 환경) mutable hoặc register toàn cục (global / 전역) trạng thái (state / 상태) trong lớp (class / 클래스) body đều là import-time side tác động (effect / 효과) như mô-đun (module / 모듈) top mức (level / 수준).

### `__class__` cell và zero-argument `super()`

Trình biên dịch (compiler / 컴파일러) tạo implicit `__class__` closure cell khi phương thức (method / 메서드) cần `__class__` hoặc zero-argument `super()`. Custom metaclass thao tác không gian tên (namespace / 네임스페이스) quá mức mà không propagate `__classcell__` đúng tới `type.__new__` có thể phá hành vi (behavior / 동작) này. Đây chủ yếu là concern của khung phần mềm (framework / 프레임워크)/metaclass author, nhưng nó cho thấy lớp (class / 클래스) creation không chỉ là `dict` + `type()` đơn giản.

### `__init_subclass__`, lớp (class / 클래스) decorator hay metaclass?

Nếu mục tiêu chỉ là validate/register subclass, `__init_subclass__` thường đơn giản hơn custom metaclass. Nếu muốn transform một lớp (class / 클래스) sau khi nó được tạo, lớp (class / 클래스) decorator thường tường minh (explicit / 명시적) hơn. Metaclass hợp khi cần kiểm soát chính quá trình lớp (class / 클래스) creation hoặc tạo family lớp (class / 클래스) có giao thức (protocol / 프로토콜) ở cấp kiểu (type / 타입).

Khi viết `__init_subclass__` trong hierarchy hợp tác, consume từ khóa (keyword / 키워드) mà lớp (class / 클래스) mình hiểu và forward phần còn lại bằng `super().__init_subclass__(**kwargs)`. Nuốt hết từ khóa (keyword / 키워드) hoặc không forward có thể phá mixin khác trong hierarchy.

Cấp cao (senior / 시니어) quy tắc (rule / 규칙) không phải “tránh metaclass”, mà là chọn hook nhỏ nhất đáp ứng bất biến (invariant / 불변식). Metaclass xung đột (conflict / 충돌) trong multiple inheritance là dạng thất bại (failure mode / 실패 모드) thật: các cơ sở (base / 기반) classes có incompatible metaclasses có thể khiến lớp (class / 클래스) mới không xác định được metaclass hợp lệ và thất bại (fail / 실패) ngay lúc definition.

> **Chuyển mạch:** Trong **Python Part 4 — Master: thời gian chạy (runtime / 런타임) internals, hiệu năng (performance / 성능), kiến trúc (architecture / 아키텍처) và hiện đại (modern / 현대적)/legacy evolution**, **7. đối tượng (object / 객체) vòng đời (lifecycle / 생명주기), construction, tham chiếu (reference / 참조) counting và cyclic GC** xác định đầu vào; **8. Immutability, aliasing và API thiết kế (design / 설계)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **9. Equality, thứ tự (ordering / 순서) và lĩnh vực (domain / 도메인) ngữ nghĩa (semantics / 의미론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Immutability, aliasing và API thiết kế (design / 설계)

Tham chiếu (reference / 참조) ngữ nghĩa (semantics / 의미론) làm aliasing trở thành thiết kế (design / 설계) concern. API nhận mutable đối tượng (object / 객체) có ba chiến lược chính: mutate theo đặc tả hợp đồng (contract / 계약), bản sao (copy / 복사) defensively, hoặc treat as read-only convention/kiểu (type / 타입). Mỗi chiến lược có chi phí (cost / 비용).

Bản sao (copy / 복사) toàn bộ đầu vào (input / 입력) ở mọi ranh giới (boundary / 경계) có thể phá hiệu năng (performance / 성능) và định danh (identity / 식별자) ngữ nghĩa (semantics / 의미론). Không bản sao (copy / 복사) có thể leak mutation. Thiết kế tốt nói rõ quyền sở hữu (ownership / 소유권).

```python
class Report:
    def __init__(self, tags: list[str]) -> None:
        self._tags = tuple(tags)
```

Ở đây bản sao (copy / 복사)+convert thể hiện bất biến (invariant / 불변식) “tags của report không đổi qua alias caller”. Đây là lập luận (reasoning / 추론), không phải quy tắc (rule / 규칙) rằng mọi danh sách (list / 목록) phải đổi thành tuple.

Một immutable outer đối tượng (object / 객체) vẫn có thể tham chiếu mutable child. Vì vậy khi lĩnh vực (domain / 도메인) cần snapshot thật, hãy reason trên đối tượng (object / 객체) đồ thị (graph / 그래프) chứ không chỉ `frozen=True` hoặc tuple ở gốc (root / 루트).

> **Chuyển mạch:** Immutability và aliasing quyết định object nào có thể thay đổi qua API. Equality/ordering/domain semantics biến constraint đó thành behavior quan sát được; type-system nâng cao tiếp theo mô tả contract của behavior ấy.

## 9. Equality, thứ tự (ordering / 순서) và lĩnh vực (domain / 도메인) ngữ nghĩa (semantics / 의미론)

`@dataclass(order=True)` có thể sinh thứ tự (ordering / 순서) lexicographic theo trường dữ liệu (field / 필드) thứ tự (order / 순서), nhưng lĩnh vực (domain / 도메인) có thật sự có total thứ tự (ordering / 순서) không? người dùng (user / 사용자), liên kết (connection / 연결) hoặc giao dịch (transaction / 트랜잭션) không tự nhiên có “nhỏ hơn” chỉ vì fields có thể so sánh.

Implement giao thức (protocol / 프로토콜) chỉ khi ngữ nghĩa (semantics / 의미론) tồn tại. Convenience-generated dunder methods có thể tạo API sai mà kiểm thử (test / 테스트) đơn giản không phát hiện.

Băm (hash / 해시)/equality đặc tả hợp đồng (contract / 계약) cũng phải ổn định qua thời gian tồn tại (lifetime / 수명) đối tượng (object / 객체) nếu đối tượng (object / 객체) dùng làm dict key/set member. Mutate trường dữ liệu (field / 필드) tham gia equality/băm (hash / 해시) sau khi insert là cách phá cấu trúc dữ liệu (data structure / 자료구조) bất biến (invariant / 불변식) dù mã (code / 코드) không raise ngay.

> **Chuyển mạch:** Domain equality và ordering xác định invariant mà type contract phải giữ. Variance, ParamSpec và protocols làm contract đó tĩnh hơn; memory layout/allocation tiếp theo kiểm tra chi phí runtime của object graph.

## 10. hệ kiểu (type system / 타입 시스템) nâng cao: variance, ParamSpec, TypeVarTuple và protocols

Typing là một ngôn ngữ (language / 언어)/tooling tầng (layer / 계층) phát triển nhanh. hiện đại (modern / 현대적) Python type-parameter cú pháp (syntax / 문법) giúp generic mã (code / 코드) đọc tự nhiên hơn, nhưng thiết kế (design / 설계) vẫn cần hiểu lớp trừu tượng (abstraction / 추상화).

`Protocol` diễn tả required hành vi (behavior / 동작) mà không ép inheritance. `ParamSpec` hữu ích khi decorator/higher-order hàm (function / 함수) cần giữ callable parameter types. `TypeVarTuple` mô hình variadic generics cho shape-like APIs. `Self`, `TypeIs` và `TypeGuard` từ Part 2 giúp kiểu (type / 타입) checker nối phương thức (method / 메서드) return/narrowing với thời gian chạy (runtime / 런타임) bằng chứng (evidence / 증거).

Advanced typing chỉ có giá trị khi làm đặc tả hợp đồng (contract / 계약) dễ hiểu hơn. Nếu signature generic dài hơn lĩnh vực (domain / 도메인) mô hình (model / 모델) mà nó mô tả, lớp trừu tượng (abstraction / 추상화) có thể đang sai tầng.

### Thời gian chạy (runtime / 런타임) annotations ở Python 3.14

Python 3.14 chuyển annotation ngữ nghĩa (semantics / 의미론) sang deferred evaluation mô hình (model / 모델). khung phần mềm (framework / 프레임워크)/công cụ (tool / 도구) mã (code / 코드) introspect annotation cần dùng API chính thức hiện hành và xử lý forward references/bảo mật (security / 보안) đúng cách. Việc evaluate annotation có thể chạy mã (code / 코드) trong một số introspection pathways; untrusted annotation nguồn (source / 소스) không phải dữ liệu vô hại.

Legacy mã (code / 코드) dùng `from __future__ import annotations` theo PEP 563 era có hành vi (behavior / 동작)/intent khác historical default; khi migrate thư viện (library / 라이브러리), kiểm thử (test / 테스트) introspection consumers chứ đừng chỉ chạy kiểu (type / 타입) checker.

> **Chuyển mạch:** Trong **Python Part 4 — Master: thời gian chạy (runtime / 런타임) internals, hiệu năng (performance / 성능), kiến trúc (architecture / 아키텍처) và hiện đại (modern / 현대적)/legacy evolution**, **10. hệ kiểu (type system / 타입 시스템) nâng cao: variance, ParamSpec, TypeVarTuple và protocols** nêu điều cần giải thích; **11. bộ nhớ (memory / 메모리) bố cục (layout / 레이아웃) và allocation: tối ưu bằng bằng chứng (evidence / 증거)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **12. hiệu năng (performance / 성능): specialization, bộ nhớ đệm (cache / 캐시) và deoptimization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. bộ nhớ (memory / 메모리) bố cục (layout / 레이아웃) và allocation: tối ưu bằng bằng chứng (evidence / 증거)

Một Python integer/string/đối tượng (object / 객체) có overhead lớn hơn raw C thành phần nguyên thủy (primitive / 기본 요소) vì mang siêu dữ liệu (metadata / 메타데이터)/headers/references. bộ chứa (container / 컨테이너) thường giữ references tới objects chứ không inline toàn bộ đối tượng (object / 객체) giá trị (value / 값) như typed packed array.

Do đó tải công việc (workload / 워크로드) numeric/nhị phân (binary / 이진) lớn thường dùng specialized packed biểu diễn (representation / 표현), buffer giao thức (protocol / 프로토콜) hoặc bản địa (native / 네이티브) libraries thay vì hàng triệu Python objects nếu lĩnh vực (domain / 도메인) cho phép. `memoryview` ở Part 2 là ví dụ application-facing của cùng principle: biểu diễn (representation / 표현) quyết định bản sao (copy / 복사) chi phí (cost / 비용), bộ nhớ (memory / 메모리) bandwidth và bộ nhớ đệm (cache / 캐시) locality.

`sys.getsizeof()` chỉ đo shallow kích thước (size / 크기) của đối tượng (object / 객체), không toàn đối tượng (object / 객체) đồ thị (graph / 그래프). Dùng nó như chỉ số (metric / 지표) cục bộ, không cộng naïve rồi kết luận tiến trình (process / 프로세스) RSS.

RSS còn chịu ảnh hưởng allocator, bản địa (native / 네이티브) libraries, mmap, fragmentation và đối tượng (object / 객체) đã free ở Python mức (level / 수준) nhưng allocator chưa trả page về OS. Khi gỡ lỗi (debug / 디버그) bộ nhớ (memory / 메모리), tách “Python đối tượng (object / 객체) retention” khỏi “tiến trình (process / 프로세스) RSS hành vi (behavior / 동작)”.

> **Chuyển mạch:** Ở chặng này của **Python Part 4 — Master: thời gian chạy (runtime / 런타임) internals, hiệu năng (performance / 성능), kiến trúc (architecture / 아키텍처) và hiện đại (modern / 현대적)/legacy evolution**, **11. bộ nhớ (memory / 메모리) bố cục (layout / 레이아웃) và allocation: tối ưu bằng bằng chứng (evidence / 증거)** nêu điều cần giải thích; **12. hiệu năng (performance / 성능): specialization, bộ nhớ đệm (cache / 캐시) và deoptimization** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **13. GIL, free-threading và di chuyển (migration / 마이그레이션) mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. hiệu năng (performance / 성능): specialization, bộ nhớ đệm (cache / 캐시) và deoptimization

CPython optimizer có thể specialize dùng chung (common / 공통) operations khi thời gian chạy (runtime / 런타임) các giả định (assumptions / 가정들) ổn định. động (dynamic / 동적) hành vi (behavior / 동작) bất thường có thể làm specialization kém hiệu quả/deopt. Tuy vậy ứng dụng (application / 애플리케이션) engineer thường không nên “mã (code / 코드) cho opcode optimizer” trước thuật toán (algorithm / 알고리즘) và I/O.

Microbenchmark cần:

- cùng Python bản dựng (build / 빌드)/phiên bản (version / 버전);
- đủ repetitions và isolation;
- tránh đo setup nếu không phải mục tiêu (target / 대상);
- hiểu warmup/specialization;
- nhìn phân phối (distribution / 분포), không chỉ một số;
- xác nhận macro impact trên tải công việc (workload / 워크로드) thật.

`timeit` tốt cho microbenchmark; môi trường vận hành (production / 운영 환경) profiler tốt hơn cho end-to-end hotspot.

Hiệu năng (performance / 성능) tối ưu hóa (optimization / 최적화) phải giữ tính đúng đắn (correctness / 정확성) bất biến (invariant / 불변식). bộ nhớ đệm (cache / 캐시), batching, vectorization và tính đồng thời (concurrency / 동시성) đều có thể đổi thất bại (failure / 실패) timing, stale-data cửa sổ (window / 윈도우) hoặc quyền sở hữu (ownership / 소유권); benchmark nhanh hơn nhưng ngữ nghĩa (semantics / 의미론) sai không phải tối ưu hóa (optimization / 최적화).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Python Part 4 — Master: thời gian chạy (runtime / 런타임) internals, hiệu năng (performance / 성능), kiến trúc (architecture / 아키텍처) và hiện đại (modern / 현대적)/legacy evolution**, **13. GIL, free-threading và di chuyển (migration / 마이그레이션) mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **12. hiệu năng (performance / 성능): specialization, bộ nhớ đệm (cache / 캐시) và deoptimization** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **14. luồng thực thi (thread / 스레드) an toàn (safety / 안전) và process-wide trạng thái (state / 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. GIL, free-threading và di chuyển (migration / 마이그레이션) mô hình tư duy (mental model / 사고 모델)

Python 3.14 là mốc quan trọng: free-threaded CPython officially supported nhưng optional. Vì vậy documentation hiện đại cần chứa hai mô hình (model / 모델).

### Default GIL-enabled CPython

Một luồng thực thi (thread / 스레드) giữ GIL khi execute Python objects/bytecode. I/O và bản địa (native / 네이티브) mã (code / 코드) có thể bản phát hành (release / 릴리스) GIL. luồng thực thi (thread / 스레드) vẫn cần locks cho logical shared-state tính đúng đắn (correctness / 정확성).

### Free-threaded CPython

GIL có thể disabled; multiple threads có thể thực sự execute Python mã (code / 코드) song song. Built-ins/thời gian chạy (runtime / 런타임) có thread-safety guarantees cụ thể, nhưng atomicity của một số thao tác (operation / 연산) không nên được nâng thành ứng dụng (application / 애플리케이션) bất biến (invariant / 불변식) nếu docs không guarantee.

Một điểm subtle: free-threaded không có nghĩa “không còn synchronization trong thời gian chạy (runtime / 런타임)”. luồng thực thi (thread / 스레드) vẫn cần attached luồng thực thi (thread / 스레드) trạng thái (state / 상태) để dùng Python C API, và thời gian chạy (runtime / 런타임) đôi lúc có thể phải dừng các luồng thực thi (thread / 스레드) ngắn hạn cho thao tác (operation / 연산) như garbage collection. Vì vậy hiệu năng (performance / 성능) mô hình (model / 모델) là “không có một toàn cục (global / 전역) khóa (lock / 잠금) giữ mọi Python thực thi (execution / 실행)”, không phải “mọi luồng thực thi (thread / 스레드) luôn chạy tự do không bao giờ dừng nhau”.

### Extension có thể làm GIL quay lại

C extension muốn chạy an toàn khi GIL disabled phải khai báo hỗ trợ (support / 지원). Với multi-phase mô-đun (module / 모듈) initialization, CPython có `Py_mod_gil` slot; mô-đun (module / 모듈) có thể khai báo `Py_MOD_GIL_NOT_USED`. Nếu extension không khai báo hỗ trợ (support / 지원) thích hợp, import trên free-threaded bản dựng (build / 빌드) có thể khiến GIL được enable lại cho thời gian chạy (runtime / 런타임) tiến trình (process / 프로세스) theo documented hành vi (behavior / 동작).

Điều này tạo môi trường vận hành (production / 운영 환경) trap: bạn benchmark pure Python free-threaded thấy parallel tốt, rồi import một phụ thuộc (dependency / 의존성) bản địa (native / 네이티브) và thông lượng (throughput / 처리량) thay đổi. Vì vậy tính năng (feature / 기능) detection phải nằm ở thời gian chạy (runtime / 런타임)/phụ thuộc (dependency / 의존성) bằng chứng (evidence / 증거), không chỉ ở executable name.

### Di chuyển (migration / 마이그레이션) chiến lược (strategy / 전략)

Không phải đổi flag rồi chạy benchmark. kiểm tra (audit / 감사) dùng chung (shared / 공유) mutable trạng thái (state / 상태), phụ thuộc (dependency / 의존성)/C-extension tính tương thích (compatibility / 호환성), thread-local các giả định (assumptions / 가정들), caches, tín hiệu (signal / 신호)/process-wide APIs và kiểm thử (test / 테스트) race conditions. Race trước đây bị GIL làm khó xuất hiện có thể thành bug thật.

Cấp cao (senior / 시니어)/Master ghi chú (note / 노트): viết synchronization dựa trên bất biến (invariant / 불변식), không dựa trên “hiện tại thao tác (operation / 연산) này có vẻ atomic”.

> **Chuyển mạch:** Trong **Python Part 4 — Master: thời gian chạy (runtime / 런타임) internals, hiệu năng (performance / 성능), kiến trúc (architecture / 아키텍처) và hiện đại (modern / 현대적)/legacy evolution**, **14. luồng thực thi (thread / 스레드) an toàn (safety / 안전) và process-wide trạng thái (state / 상태)** gom các mảnh từ **13. GIL, free-threading và di chuyển (migration / 마이그레이션) mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **15. asyncio internals: readiness, scheduling và backpressure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. luồng thực thi (thread / 스레드) an toàn (safety / 안전) và process-wide trạng thái (state / 상태)

Ngay cả free-threaded bản dựng (build / 빌드), không phải mọi process-wide thao tác (operation / 연산) có thể chạy concurrent an toàn. môi trường (environment / 환경) variables, tín hiệu (signal / 신호) handlers, hiện tại (current / 현재) working directory và một số toàn cục (global / 전역) bản địa (native / 네이티브) trạng thái (state / 상태) cần xem đặc tả hợp đồng (contract / 계약) cụ thể.

Một thiết kế (design / 설계) tốt giảm dùng chung (shared / 공유) process-wide mutation: cấu hình (config / 설정) immutable sau startup, phụ thuộc (dependency / 의존성) tường minh (explicit / 명시적), yêu cầu (request / 요청)/job trạng thái (state / 상태) scoped, side effects qua owned adapters.

### Thread-safe thành phần nguyên thủy (primitive / 기본 요소) không nâng cả workflow thành thread-safe

Một bộ chứa (container / 컨테이너) phương thức (method / 메서드) có nội bộ (internal / 내부) synchronization hoặc atomicity guarantee chỉ bảo vệ bất biến (invariant / 불변식) của bộ chứa (container / 컨테이너) ở thao tác (operation / 연산) đó. Workflow “check rồi act” vẫn có race:

```python
if key not in cache:
    cache[key] = build_value()
```

Ngay cả khi từng dict thao tác (operation / 연산) an toàn ở thời gian chạy (runtime / 런타임) hiện tại, hai luồng thực thi (thread / 스레드) vẫn có thể cùng chạy `build_value()`. ứng dụng (application / 애플리케이션) bất biến (invariant / 불변식) cần khóa (lock / 잠금)/single-flight/idempotency tùy ngữ nghĩa (semantics / 의미론).

### Tín hiệu (signal / 신호) là tiến trình (process / 프로세스)/main-thread ranh giới (boundary / 경계)

Python tín hiệu (signal / 신호) handler chạy theo mô hình (model / 모델) riêng và việc cài handler bị giới hạn vào main luồng thực thi (thread / 스레드) của main trình thông dịch (interpreter / 인터프리터). Vì vậy tín hiệu (signal / 신호) không phải generic “interrupt bất kỳ worker luồng thực thi (thread / 스레드) nào”. Shutdown thiết kế (design / 설계) nên coi tín hiệu (signal / 신호) là sự kiện (event / 이벤트) ở tiến trình (process / 프로세스) orchestration tầng (layer / 계층), sau đó chuyển nó thành trạng thái (state / 상태)/cancellation mà worker mô hình (model / 모델) hiểu.

> **Chuyển mạch:** Ở chặng này của **Python Part 4 — Master: thời gian chạy (runtime / 런타임) internals, hiệu năng (performance / 성능), kiến trúc (architecture / 아키텍처) và hiện đại (modern / 현대적)/legacy evolution**, **14. luồng thực thi (thread / 스레드) an toàn (safety / 안전) và process-wide trạng thái (state / 상태)** xác định đầu vào; **15. asyncio internals: readiness, scheduling và backpressure** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **16. Structured tính đồng thời (concurrency / 동시성) và tác vụ (task / 작업) quyền sở hữu (ownership / 소유권)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. `asyncio` internals: readiness, scheduling và backpressure

Vòng lặp sự kiện (event loop / 이벤트 루프) không “chạy tất cả coroutine cùng lúc”. Nó schedule runnable callbacks/tasks và chờ I/O readiness/timers. Coroutine chỉ yield điều khiển (control / 제어) ở await points mà awaitable thực sự suspend.

### Fairness: thành phần nguyên thủy (primitive / 기본 요소) guarantee khác scheduler fairness

Không giả định vòng lặp sự kiện (event loop / 이벤트 루프) chia CPU công bằng giữa mọi tác vụ (task / 작업). Một coroutine CPU vòng lặp (loop / 루프) không await sẽ monopolize vòng lặp (loop / 루프). Thậm chí mã (code / 코드) có `await` nhưng awaitable hoàn tất tức thì liên tục có thể chạy rất lâu trước khi tác vụ (task / 작업) khác có cơ hội hữu ích.

Tuy vậy một số thành phần nguyên thủy (primitive / 기본 요소) có guarantee cụ thể hơn. `asyncio.Lock.acquire()` được documented là fair theo thứ tự coroutine bắt đầu chờ khóa (lock / 잠금). Guarantee này chỉ nói hàng đợi (queue / 큐) waiter của **khóa (lock / 잠금) đó**, không nói toàn vòng lặp sự kiện (event loop / 이벤트 루프) là fair, không nói semaphore có cùng thứ tự (ordering / 순서) đặc tả hợp đồng (contract / 계약), và không bảo đảm độ trễ (latency / 지연 시간) công bằng nếu tác vụ (task / 작업) giữ khóa (lock / 잠금) quá lâu.

Đây là mẫu (pattern / 패턴) lập luận (reasoning / 추론) quan trọng: đọc guarantee ở phạm vi (scope / 범위) nhỏ nhất rồi không suy rộng nó thành guarantee hệ thống.

### Bounded tính đồng thời (concurrency / 동시성) khác backpressure

Semaphore giới hạn số công việc (work / 작업) cùng chạy. hàng đợi (queue / 큐) bounded giới hạn số công việc (work / 작업) chờ. Hai concern khác nhau.

Nếu chỉ đặt `Semaphore(20)` nhưng producer vẫn tạo hàng triệu tác vụ (task / 작업) đang chờ semaphore, bộ nhớ (memory / 메모리) vẫn có thể tăng lớn. Bounded kiến trúc (architecture / 아키텍처) thường giới hạn cả **in-flight thực thi (execution / 실행)** lẫn **queued công việc (work / 작업)**.

### Backpressure bằng bounded hàng đợi (queue / 큐)

Nếu producer nhanh hơn bên tiêu thụ (consumer / 소비자) và hàng đợi (queue / 큐) không bound, bộ nhớ (memory / 메모리) sẽ tăng. `asyncio.Queue(maxsize=N)` khiến `put()` suspend khi hàng đợi (queue / 큐) đầy:

```python
queue = asyncio.Queue(maxsize=100)
await queue.put(item)
```

Backpressure không chỉ là “đỡ bộ nhớ (memory / 메모리)”. Nó truyền sức chứa (capacity / 용량) tín hiệu (signal / 신호) upstream. Nếu upstream không thể chậm lại, kiến trúc (architecture / 아키텍처) phải chọn drop, spill-to-disk, reject hoặc bên ngoài (external / 외부) durable hàng đợi (queue / 큐) thay vì giả vờ buffer vô hạn.

### Hàng đợi (queue / 큐) vòng đời (lifecycle / 생명주기) và `shutdown()`

Hiện đại (modern / 현대적) `asyncio.Queue` có `shutdown()`. Với graceful shutdown, hàng đợi (queue / 큐) có thể ngừng nhận item mới nhưng cho bên tiêu thụ (consumer / 소비자) drain công việc (work / 작업) đã nhận; khi drain xong, `join()` vẫn giữ bất biến (invariant / 불변식) “mọi công việc (work / 작업) item đã được `task_done()`”.

Immediate shutdown lại cố ý phá bất biến (invariant / 불변식) thông thường của `join()`: hàng đợi (queue / 큐) có thể được drain/unblock dù công việc (work / 작업) chưa thực sự xử lý. Vì vậy `shutdown(immediate=True)` là emergency control-flow quyết định (decision / 결정), không phải shortcut tương đương graceful drain.

Mô hình tư duy (mental model / 사고 모델) shutdown hàng đợi (queue / 큐):

```text
stop accepting
→ decide drain or abandon
→ finish/mark existing work
→ release waiters
→ close downstream resources
```

### Cancellation an toàn (safety / 안전): safe interruption điểm (point / 지점)

Nếu tác vụ (task / 작업) bị cancel giữa hai side effects, trạng thái (state / 상태) có thể partial. giao dịch (transaction / 트랜잭션)/ngữ cảnh (context / 맥락) manager/idempotency giúp define safe interruption points. Shielding cancellation (`asyncio.shield`) chỉ dùng khi thao tác (operation / 연산) thực sự phải hoàn tất; lạm dụng làm shutdown không bounded.

Một trọng yếu (critical / 중요) section async có ba loại ranh giới (boundary / 경계) khác nhau: “không muốn tác vụ (task / 작업) khác vào” (lock), “không muốn thao tác (operation / 연산) bị cancel giữa bất biến (invariant / 불변식) chuyển tiếp (transition / 전이)” (cancellation design), và “không muốn remote side tác động (effect / 효과) bị duplicate” (idempotency/transaction). Một `asyncio.Lock` không giải quyết hai loại sau.

Cancellation cũng có phạm vi (scope / 범위). Cancel coroutine đang await `to_thread()` không cưỡng chế stop hàm (function / 함수) sync đã chạy trong worker luồng thực thi (thread / 스레드). Cancel yêu cầu (request / 요청) không mặc nhiên quay lui (rollback / 롤백) side tác động (effect / 효과) đã gửi tới remote dịch vụ (service / 서비스). Vì vậy cancellation chính sách (policy / 정책) phải nối với idempotency, giao dịch (transaction / 트랜잭션) và quyền sở hữu (ownership / 소유권) của thực thi (execution / 실행) tài nguyên (resource / 자원).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Python Part 4 — Master: thời gian chạy (runtime / 런타임) internals, hiệu năng (performance / 성능), kiến trúc (architecture / 아키텍처) và hiện đại (modern / 현대적)/legacy evolution**, sau nội dung của **15. asyncio internals: readiness, scheduling và backpressure**, **16. Structured tính đồng thời (concurrency / 동시성) và tác vụ (task / 작업) quyền sở hữu (ownership / 소유권)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **17. Multiprocessing, multiple interpreters và bên ngoài (external / 외부) resources** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Structured tính đồng thời (concurrency / 동시성) và tác vụ (task / 작업) quyền sở hữu (ownership / 소유권)

`TaskGroup` giúp lexical phạm vi (scope / 범위) sở hữu tasks. Khi child thất bại (fail / 실패), sibling cancellation và aggregated lỗi (error / 오류) handling có ngữ nghĩa (semantics / 의미론) rõ hơn loose tasks.

Fire-and-forget tác vụ (task / 작업) cần registry, exception observation và shutdown handling. Nếu không, lỗi có thể chỉ hiện “tác vụ (task / 작업) exception was never retrieved”, hoặc tác vụ (task / 작업) mất đơn vị sở hữu (owner / 오너) theo vòng đời (lifecycle / 생명주기).

Môi trường vận hành (production / 운영 환경) quy tắc (rule / 규칙): mọi concurrent đơn vị (unit / 단위) phải có đơn vị sở hữu (owner / 오너), deadline và thất bại (failure / 실패) chính sách (policy / 정책).

### Cancellation propagation không thay nghiệp vụ (business / 비즈니스) quay lui (rollback / 롤백)

Structured tính đồng thời (concurrency / 동시성) tổ chức thời gian tồn tại (lifetime / 수명) của tasks; nó không tự biết quay lui (rollback / 롤백) cơ sở dữ liệu (database / 데이터베이스), hoàn tiền payment hay xóa tệp (file / 파일) partial. Khi sibling thất bại (fail / 실패), cancellation chỉ là tín hiệu (signal / 신호) điều khiển (control / 제어) luồng (flow / 흐름). lĩnh vực (domain / 도메인) quay lui (rollback / 롤백) cần giao dịch (transaction / 트랜잭션)/compensation riêng.

Đây là lý do thất bại (failure / 실패) cây (tree / 트리) và side-effect cây (tree / 트리) không luôn giống nhau. Một tác vụ (task / 작업) có thể đã lần ghi nhận (commit / 커밋) bên ngoài (external / 외부) side tác động (effect / 효과) trước khi sibling thất bại (fail / 실패).

> **Chuyển mạch:** Trong **Python Part 4 — Master: thời gian chạy (runtime / 런타임) internals, hiệu năng (performance / 성능), kiến trúc (architecture / 아키텍처) và hiện đại (modern / 현대적)/legacy evolution**, **16. Structured tính đồng thời (concurrency / 동시성) và tác vụ (task / 작업) quyền sở hữu (ownership / 소유권)** nêu điều cần giải thích; **17. Multiprocessing, multiple interpreters và bên ngoài (external / 외부) resources** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **18. bản địa (native / 네이티브) extensions và Python hiệu năng (performance / 성능) ceiling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Multiprocessing, multiple interpreters và bên ngoài (external / 외부) resources

Fork bản sao (copy / 복사) tiến trình (process / 프로세스) trạng thái (state / 상태) theo OS sao chép khi ghi (copy-on-write / 쓰기 시 복사) ngữ nghĩa (semantics / 의미론), nhưng threads, locks, DB/mạng (network / 네트워크) connections và thời gian chạy (runtime / 런타임) trạng thái (state / 상태) có thể không safe khi fork từ multithreaded tiến trình (process / 프로세스). hiện đại (modern / 현대적) Python/nền tảng (platform / 플랫폼) defaults thay đổi để giảm unsafe các giả định (assumptions / 가정들).

Không mở DB liên kết (connection / 연결) pool rồi giả định forked workers có thể share liên kết (connection / 연결) đối tượng (object / 객체) đúng. Tạo per-process tài nguyên (resource / 자원) sau worker startup theo thư viện (library / 라이브러리) đặc tả hợp đồng (contract / 계약).

IPC serialization means đối tượng (object / 객체) định danh (identity / 식별자) không đi qua tiến trình (process / 프로세스) ranh giới (boundary / 경계) như dùng chung (shared / 공유) in-process tham chiếu (reference / 참조). Đây là lý do tiến trình (process / 프로세스) kiến trúc (architecture / 아키텍처) thường tự nhiên hơn với messages/giá trị (value / 값) dữ liệu (data / 데이터).

### Multiple interpreters trong Python 3.14

Python 3.14 thêm công khai (public / 공개) high-level API `concurrent.interpreters` và `InterpreterPoolExecutor`. trình thông dịch (interpreter / 인터프리터) là thực thi (execution / 실행) ngữ cảnh (context / 맥락) Python với trạng thái (state / 상태) riêng như import trạng thái (state / 상태) và builtins. Nhiều interpreters có thể tồn tại trong cùng tiến trình (process / 프로세스), nhưng **trình thông dịch (interpreter / 인터프리터) tự nó không tạo tính đồng thời (concurrency / 동시성)**; tính đồng thời (concurrency / 동시성) xuất hiện khi thực thi (execution / 실행) được đặt trên nhiều threads/interpreters thích hợp.

`InterpreterPoolExecutor` dùng worker threads nhưng mỗi worker chạy trong trình thông dịch (interpreter / 인터프리터) riêng. Mỗi trình thông dịch (interpreter / 인터프리터) có GIL riêng trong mô hình (model / 모델) này, nên worker có thể đạt multi-core parallelism mà không dùng tiến trình (process / 프로세스) riêng. Đổi lại isolation mạnh hơn luồng thực thi (thread / 스레드) thường: mutable Python objects nhìn chung không được chia sẻ tự do giữa interpreters; dữ liệu (data / 데이터) cần bản sao (copy / 복사)/serialize hoặc đi qua communication thành phần nguyên thủy (primitive / 기본 요소) phù hợp.

```text
ThreadPoolExecutor
same process + same interpreter state + shared mutable objects

InterpreterPoolExecutor
same process + multiple isolated interpreter states + explicit data transfer

ProcessPoolExecutor
multiple processes + OS address-space isolation + IPC/serialization
```

Không nên gọi subinterpreter là “tiến trình (process / 프로세스) nhẹ” vì thất bại (failure / 실패)/tài nguyên (resource / 자원) isolation vẫn khác tiến trình (process / 프로세스). Một segfault bản địa (native / 네이티브) extension vẫn có thể làm chết toàn tiến trình (process / 프로세스). Cũng không nên gọi nó là “luồng thực thi (thread / 스레드) bình thường” vì import/mô-đun (module / 모듈)/toàn cục (global / 전역) trạng thái (state / 상태) được isolate theo trình thông dịch (interpreter / 인터프리터).

### Extension tính tương thích (compatibility / 호환성) có hai trục khác nhau

Bản địa (native / 네이티브) extension cần phân biệt “có chạy trong subinterpreter không?” và “có chạy khi GIL disabled không?”. CPython C API có mô-đun (module / 모듈) slots khác nhau cho hai năng lực (capability / 역량) này.

`Py_mod_multiple_interpreters` cho phép extension khai báo mức hỗ trợ (support / 지원) với multiple interpreters. Một mô-đun (module / 모듈) có thể không hỗ trợ (support / 지원) subinterpreter, hỗ trợ (support / 지원) khi interpreters share GIL, hoặc hỗ trợ (support / 지원) per-interpreter GIL. `Py_mod_gil` lại khai báo extension có cần GIL không.

Hai trục này độc lập về mặt lập luận (reasoning / 추론). Một extension có thể thread-safe dưới GIL nhưng vẫn dùng process-global trạng thái (state / 상태) khiến subinterpreter isolation sai. Hoặc hỗ trợ (support / 지원) subinterpreter nhưng chưa an toàn free-threaded. Vì vậy “import được” trong một mô hình thực thi (execution model / 실행 모델) không chứng minh mô hình (model / 모델) khác an toàn.

### Process-global bản địa (native / 네이티브) trạng thái (state / 상태) là hidden trạng thái dùng chung (shared state / 공유 상태)

Python mô-đun (module / 모듈) globals có thể isolate theo trình thông dịch (interpreter / 인터프리터) nhưng bản địa (native / 네이티브) static/toàn cục (global / 전역) variable của extension có thể vẫn sống ở tiến trình (process / 프로세스) phạm vi (scope / 범위). Extension hiện đại thường cần per-module/per-interpreter trạng thái (state / 상태) thay vì giả định singleton process-global trạng thái (state / 상태) nếu muốn hỗ trợ (support / 지원) trình thông dịch (interpreter / 인터프리터) isolation tốt.

Use trường hợp (case / 사례) hợp lý cho trình thông dịch (interpreter / 인터프리터) pool là CPU-heavy Python tasks có dữ liệu message/giá trị (value / 값) tương đối độc lập và muốn multi-core trong cùng tiến trình (process / 프로세스), nhưng sự đánh đổi (trade-off / 트레이드오프) phải được đo so với tiến trình (process / 프로세스) pool và free-threaded threads.

> **Chuyển mạch:** Ở chặng này của **Python Part 4 — Master: thời gian chạy (runtime / 런타임) internals, hiệu năng (performance / 성능), kiến trúc (architecture / 아키텍처) và hiện đại (modern / 현대적)/legacy evolution**, **17. Multiprocessing, multiple interpreters và bên ngoài (external / 외부) resources** nêu điều cần giải thích; **18. bản địa (native / 네이티브) extensions và Python hiệu năng (performance / 성능) ceiling** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **19. bảo mật (security / 보안) sâu hơn: deserialization, introspection và động (dynamic / 동적) thực thi (execution / 실행)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. bản địa (native / 네이티브) extensions và Python hiệu năng (performance / 성능) ceiling

C/C++/Rust extension hoặc bản địa (native / 네이티브) libraries có thể thực hiện heavy công việc (work / 작업) ngoài Python trình thông dịch (interpreter / 인터프리터). Một số bản phát hành (release / 릴리스) GIL; một số không. Vì vậy statement “luồng thực thi (thread / 스레드) không giúp CPU-bound Python” phải thêm điều kiện “pure Python on GIL-enabled CPython”. bản địa (native / 네이티브) workloads có hiệu năng (performance / 성능) profile khác.

ABI/API tính tương thích (compatibility / 호환성) cũng là triển khai (deployment / 배포) concern. Wheel tags, nền tảng (platform / 플랫폼) kiến trúc (architecture / 아키텍처) và Python phiên bản (version / 버전) quyết định nhị phân (binary / 이진) phân phối (distribution / 분포) nào install được. Pure Python gói (package / 패키지) đơn giản hơn bản địa (native / 네이티브) gói (package / 패키지) về portability.

### Luồng thực thi (thread / 스레드) trạng thái (state / 상태) vẫn quan trọng khi GIL disabled

Free-threaded bản dựng (build / 빌드) không xóa khái niệm Python luồng thực thi (thread / 스레드) trạng thái (state / 상태). bản địa (native / 네이티브) luồng thực thi (thread / 스레드) dùng Python C API vẫn cần attached luồng thực thi (thread / 스레드) trạng thái (state / 상태). mã (code / 코드) C cũ đồng nhất “có luồng thực thi (thread / 스레드) trạng thái (state / 상태)” với “đang giữ GIL” có thể cần kiểm tra (audit / 감사) lại mô hình tư duy (mental model / 사고 모델).

Long-running bản địa (native / 네이티브) computation không cần Python objects có thể detach luồng thực thi (thread / 스레드) trạng thái (state / 상태) để cho thời gian chạy (runtime / 런타임)/threads khác hoạt động. Trên free-threaded bản dựng (build / 빌드), detach vẫn có ý nghĩa vì thời gian chạy (runtime / 런타임) đôi lúc cần coordination như GC stop-the-world ngắn hạn.

### Stable ABI không đồng nghĩa hành vi (behavior / 동작) tính tương thích (compatibility / 호환성) tuyệt đối

ABI tính tương thích (compatibility / 호환성) giúp nhị phân (binary / 이진) tải (load / 로드) across supported versions theo đặc tả hợp đồng (contract / 계약), nhưng hành vi (behavior / 동작) còn phụ thuộc nền tảng (platform / 플랫폼) thư viện (library / 라이브러리), thời gian chạy (runtime / 런타임) bản dựng (build / 빌드) chế độ (mode / 모드), extension các giả định (assumptions / 가정들) và tính năng (feature / 기능) hỗ trợ (support / 지원). triển khai (deployment / 배포) kiểm thử (test / 테스트) vẫn phải chạy sản phẩm tạo ra (artifact / 산출물) thật trên mục tiêu (target / 대상) môi trường (environment / 환경).

> **Chuyển mạch:** Native extensions đặt ceiling và trust boundary cho Python performance; security tiếp theo kiểm tra deserialization, introspection và dynamic execution trong boundary đó. Observability sau đó cần chứng minh cả behavior lẫn failure.

## 19. bảo mật (security / 보안) sâu hơn: deserialization, introspection và động (dynamic / 동적) thực thi (execution / 실행)

Động (dynamic / 동적) features làm Python mạnh nhưng tăng attack surface.

`eval`, `exec`, động (dynamic / 동적) import, pickle, template rendering, regex, archive extraction, YAML loader của third-party tools, plugin discovery và subprocess đều là ranh giới (boundary / 경계) cần threat mô hình (model / 모델).

Không có “sanitize string” chung cho mọi ngữ cảnh (context / 맥락). SQL, shell, HTML, regex, đường dẫn (path / 경로) và URL đều có grammar khác; solution là parameterization/structured API đúng ngữ cảnh (context / 맥락).

### Introspection cũng có side tác động (effect / 효과) surface

`getattr`, descriptor truy cập (access / 접근), annotation evaluation hoặc plugin import có thể execute mã (code / 코드). Security-sensitive tooling không nên giả định “chỉ đang đọc siêu dữ liệu (metadata / 메타데이터)”. Nếu đối tượng (object / 객체) đến từ untrusted/plugin ranh giới (boundary / 경계), inspect thao tác (operation / 연산) nào kích hoạt người dùng (user / 사용자) mã (code / 코드) cần được hiểu rõ.

### Supply chuỗi (chain / 사슬)

Hệ thống dựng (build system / 빌드 시스템) trong `pyproject.toml` có mã (code / 코드)/phụ thuộc (dependency / 의존성) thực thi trong bản dựng (build / 빌드) môi trường (environment / 환경). Install gói (package / 패키지) không nên được xem là đọc dữ liệu (data / 데이터) thụ động. CI cần isolate bản dựng (build / 빌드), pin trusted sources và rà soát (review / 검토) phụ thuộc (dependency / 의존성) updates phù hợp rủi ro (risk / 위험).

> **Chuyển mạch:** Security boundary quyết định dữ liệu nào được phép đi qua runtime; observability phân biệt log, metric và trace để theo dõi boundary đó. Deployment tiếp theo đưa artifact qua process lifecycle và graceful shutdown.

## 20. khả năng quan sát (observability / 관측 가능성): log, chỉ số (metric / 지표) và dấu vết (trace / 추적) trả lời câu hỏi khác nhau

Log ghi sự kiện (event / 이벤트)/ngữ cảnh (context / 맥락) chi tiết. chỉ số (metric / 지표) tổng hợp numeric thời gian (time / 시간) series. dấu vết (trace / 추적) theo yêu cầu (request / 요청)/job qua components. Python mã (code / 코드) nên expose ngữ nghĩa (semantic / 의미적) ngữ cảnh (context / 맥락) chứ không chỉ dấu vết ngăn xếp (stack trace / 스택 트레이스).

Instrument tại ranh giới (boundary / 경계): yêu cầu (request / 요청) start/end, bên ngoài (external / 외부) lời gọi (call / 호출) độ trễ (latency / 지연 시간), hàng đợi (queue / 큐) độ sâu (depth / 깊이), thử lại (retry / 재시도) count, thất bại (failure / 실패) lớp (class / 클래스). Đừng log mỗi vòng lặp (loop / 루프) iteration trong đường xử lý nóng (hot path / 핫 패스) rồi tạo bottleneck/log bill.

Correlation ID/ngữ cảnh (context / 맥락) propagation trong async/luồng thực thi (thread / 스레드) mã (code / 코드) cần chiến lược (strategy / 전략) rõ; `contextvars` giữ context-local trạng thái (state / 상태) qua async tác vụ (task / 작업) boundaries tốt hơn thread-local trong nhiều async use cases. `asyncio.to_thread()` mang hiện tại (current / 현재) ngữ cảnh (context / 맥락) sang worker luồng thực thi (thread / 스레드), nhưng qua tiến trình (process / 프로세스)/trình thông dịch (interpreter / 인터프리터)/dịch vụ (service / 서비스) ranh giới (boundary / 경계) thì ngữ cảnh (context / 맥락) phải thành tường minh (explicit / 명시적) siêu dữ liệu (metadata / 메타데이터).

### Cardinality là hiệu năng (performance / 성능)/chi phí (cost / 비용) bất biến (invariant / 불변식) của metrics

Label chỉ số (metric / 지표) bằng `user_id`, yêu cầu (request / 요청) URL raw hoặc exception message arbitrary có thể tạo cardinality khổng lồ. chỉ số (metric / 지표) hệ thống (system / 시스템) khi đó tốn bộ nhớ (memory / 메모리)/chi phí (cost / 비용) và truy vấn (query / 쿼리) chậm. chỉ số (metric / 지표) label nên có bounded lĩnh vực (domain / 도메인); high-cardinality detail thuộc log/dấu vết (trace / 추적) phù hợp hơn.

### Sampling làm bằng chứng (evidence / 증거) không đầy đủ

Dấu vết (trace / 추적) có thể sampled. Log có thể rate-limit. chỉ số (metric / 지표) aggregate mất per-request detail. Vì vậy sự cố (incident / 인시던트) lập luận (reasoning / 추론) phải biết loại bằng chứng (evidence / 증거) nào có thể thiếu dữ liệu do chính sách (policy / 정책), không kết luận “không thấy dấu vết (trace / 추적) = yêu cầu (request / 요청) không xảy ra”.

### Khả năng quan sát (observability / 관측 가능성) không được đổi nghiệp vụ (business / 비즈니스) hành vi (behavior / 동작)

Logging formatter, exporter hoặc tracing hook không nên raise làm thất bại (fail / 실패) yêu cầu (request / 요청) thông thường nếu đặc tả hợp đồng (contract / 계약) không yêu cầu. Instrumentation nằm trên đường găng (critical path / 임계 경로) phải có thất bại (failure / 실패) chính sách (policy / 정책) rõ: drop/buffer/thử lại (retry / 재시도)/bounded hàng đợi (queue / 큐), tránh biến outage telemetry thành outage ứng dụng (application / 애플리케이션).

> **Chuyển mạch:** Ở chặng này của **Python Part 4 — Master: thời gian chạy (runtime / 런타임) internals, hiệu năng (performance / 성능), kiến trúc (architecture / 아키텍처) và hiện đại (modern / 현대적)/legacy evolution**, **20. khả năng quan sát (observability / 관측 가능성): log, chỉ số (metric / 지표) và dấu vết (trace / 추적) trả lời câu hỏi khác nhau** xác định đầu vào; **21. triển khai (deployment / 배포): sản phẩm tạo ra (artifact / 산출물), tiến trình (process / 프로세스), signals và graceful shutdown** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **22. phiên bản (version / 버전) evolution: đọc mã (code / 코드) cũ bằng ngữ cảnh (context / 맥락)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. triển khai (deployment / 배포): sản phẩm tạo ra (artifact / 산출물), tiến trình (process / 프로세스), signals và graceful shutdown

Một deployable sản phẩm tạo ra (artifact / 산출물) cần biết Python phiên bản (version / 버전)/bản dựng (build / 빌드), phụ thuộc (dependency / 의존성) resolution/khóa (lock / 잠금), OS/bản địa (native / 네이티브) dependencies, entry điểm (point / 지점), cấu hình (configuration / 구성) đặc tả hợp đồng (contract / 계약), di chuyển (migration / 마이그레이션)/startup/shutdown hành vi (behavior / 동작), health/readiness ngữ nghĩa (semantics / 의미론) và tài nguyên (resource / 자원) limits.

Ảnh bộ chứa (container image / 컨테이너 이미지) là một cách đóng gói sản phẩm tạo ra (artifact / 산출물), nhưng reproducibility vẫn phụ thuộc cơ sở (base / 기반) ảnh (image / 이미지) tag/digest và bản dựng (build / 빌드) inputs.

### Startup: readiness khác liveness

Tiến trình (process / 프로세스) “đang sống” không nghĩa đã sẵn sàng nhận yêu cầu (request / 요청). Startup có thể cần tải (load / 로드) cấu hình (config / 설정), initialize pool, warm bộ nhớ đệm (cache / 캐시) bắt buộc hoặc validate di chuyển (migration / 마이그레이션) tính tương thích (compatibility / 호환성). Readiness chỉ nên bật khi bất biến (invariant / 불변식) phục vụ yêu cầu (request / 요청) đã đạt.

Ngược lại, liveness trả lời tiến trình (process / 프로세스) còn khả năng tiến triển hay không. Dùng cùng một check cho cả hai dễ tạo restart vòng lặp (loop / 루프) hoặc tuyến (route / 경로) traffic quá sớm.

### Graceful shutdown là giao thức (protocol / 프로토콜) nhiều bước

Một shutdown môi trường vận hành (production / 운영 환경) điển hình:

```text
nhận signal/stop event
→ chuyển readiness sang false / ngừng nhận work mới
→ signal producer dừng enqueue
→ drain hoặc cancel work đang có theo policy
→ chờ deadline
→ close pool/socket/file/exporter
→ flush state cần durability
→ exit
```

Tín hiệu (signal / 신호) handler không nên làm toàn bộ cleanup phức tạp trực tiếp. Nó nên chuyển tiến trình (process / 프로세스) sang shutdown trạng thái (state / 상태) mà main orchestration/tác vụ (task / 작업) hiểu.

Python tín hiệu (signal / 신호) handler có main-thread/main-interpreter ngữ nghĩa (semantics / 의미론); điều này càng củng cố việc tín hiệu (signal / 신호) là orchestration ranh giới (boundary / 경계), không phải worker-control thành phần nguyên thủy (primitive / 기본 요소).

### `asyncio.Runner` và Ctrl-C

`asyncio.Runner` xử lý `SIGINT` theo cách phù hợp async hơn việc để `KeyboardInterrupt` cắt arbitrary internals: nó cancel main tác vụ (task / 작업) để ngăn xếp (stack / 스택) có cơ hội unwind qua `try/finally`, rồi mới surface `KeyboardInterrupt`. Nhưng tight CPU vòng lặp (loop / 루프) không reach suspension điểm (point / 지점) thì cancellation không thể tiến triển bình thường.

Điều này nối trực tiếp scheduler fairness với shutdown tính đúng đắn (correctness / 정확성): vòng lặp sự kiện (event loop / 이벤트 루프) bị monopolize không chỉ tăng độ trễ (latency / 지연 시간) mà còn làm tiến trình (process / 프로세스) khó dừng graceful.

### Hàng đợi (queue / 큐) drain trong shutdown

Nếu dùng `asyncio.Queue`, graceful đường dẫn (path / 경로) nên ngừng producer trước, rồi drain hàng đợi (queue / 큐) và đảm bảo `task_done()`/`join()` bất biến (invariant / 불변식). Immediate hàng đợi (queue / 큐) shutdown chỉ dùng khi chính sách (policy / 정책) chấp nhận abandon công việc (work / 작업).

Nếu công việc (work / 작업) đã được giao sang luồng thực thi (thread / 스레드)/tiến trình (process / 프로세스)/bên ngoài (external / 외부) dịch vụ (service / 서비스), hàng đợi (queue / 큐) empty không đồng nghĩa side tác động (effect / 효과) ngoài tiến trình (process / 프로세스) đã xong. Shutdown phải theo quyền sở hữu (ownership / 소유권) thật của thực thi (execution / 실행) tài nguyên (resource / 자원).

### Executor và background tài nguyên (resource / 자원)

Default executor/luồng thực thi (thread / 스레드) pool có vòng đời (lifecycle / 생명주기) riêng. Background tác vụ (task / 작업) không có đơn vị sở hữu (owner / 오너) rõ sẽ làm shutdown treo hoặc bị bỏ dở. Mọi background đơn vị (unit / 단위) nên biết ai chờ nó, ai cancel nó, và deadline nào áp dụng.

### Bytecode bộ nhớ đệm (cache / 캐시) `.pyc`

CPython có thể bộ nhớ đệm (cache / 캐시) compiled bytecode trong `__pycache__`; đây là hiệu năng (performance / 성능) sản phẩm tạo ra (artifact / 산출물), không phải nguồn chuẩn (source of truth / 정본). Không lần ghi nhận (commit / 커밋)/treat `.pyc` như deploy lô-gic (logic / 논리) trừ workflow đặc biệt. Invalid bộ nhớ đệm (cache / 캐시) không nên thay nguồn (source / 소스) ngữ nghĩa (semantics / 의미론).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Python Part 4 — Master: thời gian chạy (runtime / 런타임) internals, hiệu năng (performance / 성능), kiến trúc (architecture / 아키텍처) và hiện đại (modern / 현대적)/legacy evolution**, **21. triển khai (deployment / 배포): sản phẩm tạo ra (artifact / 산출물), tiến trình (process / 프로세스), signals và graceful shutdown** xác định đầu vào; **22. phiên bản (version / 버전) evolution: đọc mã (code / 코드) cũ bằng ngữ cảnh (context / 맥락)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **23. kiến trúc (architecture / 아키텍처): functional cốt lõi (core / 핵심), imperative shell** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. phiên bản (version / 버전) evolution: đọc mã (code / 코드) cũ bằng ngữ cảnh (context / 맥락)

### Python 2 → Python 3

Legacy rất cũ có `print` statement, bytes/văn bản (text / 텍스트) mô hình (model / 모델) khác, integer division differences và old-style idioms. Đừng thêm tính tương thích (compatibility / 호환성) hack Python 2 vào mã (code / 코드) mới.

### Python 3.8–3.11

Rất nhiều môi trường vận hành (production / 운영 환경) mã (code / 코드) vẫn mục tiêu (target / 대상) line này. Bạn sẽ gặp `typing.List[str]`, `Optional[T]`, `TypeVar`/`Generic`, manual event-loop patterns và packaging cấu hình (config / 설정) cũ. Đọc được không có nghĩa tiếp tục viết mới y hệt nếu hỗ trợ (support / 지원) ma trận (matrix / 행렬) đã nâng.

### Python 3.10+

`X | None` union cú pháp (syntax / 문법) và structural mẫu (pattern / 패턴) matching xuất hiện. Không dùng `match` chỉ để thay `if/elif` đơn giản.

### Python 3.11

Exception groups/`except*`, `TaskGroup` và nhiều hiệu năng (performance / 성능) improvements làm concurrent lỗi (error / 오류) handling hiện đại hơn.

### Python 3.12

Kiểu (type / 타입) parameter cú pháp (syntax / 문법) (`class Box[T]`, `def f[T]`) và typing evolution giúp generic mã (code / 코드) gọn hơn. Multiple-interpreter C API contracts cũng tiếp tục rõ hơn.

### Python 3.13

Free-threaded bản dựng (build / 빌드) bắt đầu experimental. hàng đợi (queue / 큐) APIs ở cả sync/async ecosystems có tường minh (explicit / 명시적) shutdown ngữ nghĩa (semantics / 의미론) mới, giúp termination trở thành giao thức (protocol / 프로토콜) rõ thay vì chỉ dùng sentinel ad hoc.

### Python 3.14

Free-threaded bản dựng (build / 빌드) officially supported nhưng vẫn optional; t-string (`t"..."`) được thêm; annotation ngữ nghĩa (semantics / 의미론) thay đổi theo deferred evaluation; asyncio chính sách (policy / 정책) hệ thống (system / 시스템) deprecated hướng tới removal 3.16; `concurrent.interpreters` và `InterpreterPoolExecutor` đưa multiple interpreters thành công khai (public / 공개) application-facing tính đồng thời (concurrency / 동시성) option. Đây là những phiên bản (version / 버전) distinctions có thể ảnh hưởng trực tiếp hiện đại (modern / 현대적) mã (code / 코드).

Không biến chapter thành changelog: timeline tồn tại để giải thích vì sao codebase cũ và mã (code / 코드) mới có mẫu (pattern / 패턴) khác nhau.

> **Chuyển mạch:** Legacy context giúp phân biệt domain logic và side effect. Functional core/imperative shell đặt boundary đó rõ ràng; sync hay async API tiếp theo chọn execution model phù hợp boundary.

## 23. kiến trúc (architecture / 아키텍처): functional cốt lõi (core / 핵심), imperative shell

Một mẫu (pattern / 패턴) hữu ích cho automation/dịch vụ (service / 서비스) là giữ lĩnh vực (domain / 도메인) transformation càng pure/deterministic càng tốt và đẩy filesystem/mạng (network / 네트워크)/subprocess/thời gian (time / 시간)/random ra adapter/orchestration ranh giới (boundary / 경계).

Ví dụ, một hàm `split_sections(text) -> dict` tự viết có thể dễ kiểm thử vì đầu vào (input / 입력) và đầu ra (output / 출력) rõ. Git/HTTP operations có side tác động (effect / 효과) nên isolate sau phương thức (method / 메서드) ranh giới (boundary / 경계). Đây là lập luận (reasoning / 추론) mẫu (pattern / 패턴) chứ không yêu cầu codebase phải “functional programming”.

Lợi ích: kiểm thử (test / 테스트) nhanh, thử lại (retry / 재시도)/giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) rõ, thất bại (failure / 실패) injection dễ, và tính đồng thời (concurrency / 동시성) ít dùng chung (shared / 공유) mutable trạng thái (state / 상태).

Pure cốt lõi (core / 핵심) không có nghĩa không được bộ nhớ đệm (cache / 캐시). Nó có nghĩa bộ nhớ đệm (cache / 캐시)/clock/random/I/O được đặt ở ranh giới (boundary / 경계) có quyền sở hữu (ownership / 소유권) tường minh (explicit / 명시적), để cốt lõi (core / 핵심) ngữ nghĩa (semantics / 의미론) không phụ thuộc hidden tiến trình (process / 프로세스) trạng thái (state / 상태).

> **Chuyển mạch:** Functional core giữ computation thuần, imperative shell giữ I/O; sync/async API là lựa chọn theo blocking và cancellation boundary. Exception taxonomy tiếp theo làm rõ failure contract của API đó.

## 24. kiến trúc (architecture / 아키텍처): sync hay async API?

Đừng chọn async chỉ vì khung phần mềm (framework / 프레임워크) hỗ trợ. Nếu entire phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) là sync và traffic thấp, sync dịch vụ (service / 서비스) có thể đơn giản hơn. Nếu cần hàng nghìn concurrent sockets và ecosystem async-native, async có lợi.

Một API thư viện (library / 라이브러리) nên cân nhắc không ép bên tiêu thụ (consumer / 소비자) vào vòng lặp sự kiện (event loop / 이벤트 루프) nếu thao tác (operation / 연산) bản chất CPU/cục bộ (local / 로컬) và sync. Ngược lại, wrap mạng (network / 네트워크) async API bằng sync luồng thực thi (thread / 스레드) hack có thể gây nested vòng lặp (loop / 루프)/deadlock/độ trễ (latency / 지연 시간) độ phức tạp (complexity / 복잡도).

Ranh giới (boundary / 경계) tốt là một mô hình (model / 모델) nhất quán hoặc cung cấp sync/async adapters có quyền sở hữu (ownership / 소유권) rõ.

Nếu cung cấp cả sync và async API, tránh copy-paste hai hiện thực (implementation / 구현) lô-gic nghiệp vụ (business logic / 비즈니스 로직) độc lập. Tách dùng chung (shared / 공유) pure lô-gic (logic / 논리) và hai orchestration adapters để bug fix không divergence.

> **Chuyển mạch:** Sync/async boundary quyết định lỗi được propagate và retry ở đâu. Exception taxonomy biến các lỗi đó thành contract; configuration/feature evolution tiếp theo kiểm soát thay đổi contract theo thời gian.

## 25. kiến trúc (architecture / 아키텍처): exception taxonomy

Define exception theo khôi phục (recovery / 복구) ngữ nghĩa (semantics / 의미론). Ví dụ invalid người dùng (user / 사용자) đầu vào (input / 입력) thì caller sửa yêu cầu (request / 요청); transient bên ngoài (external / 외부) thất bại (failure / 실패) có thể thử lại (retry / 재시도); cấu hình (configuration / 구성) lỗi (error / 오류) nên thất bại (fail / 실패) startup; bất biến (invariant / 불변식) violation/programming lỗi (error / 오류) không nên silently recover.

Đừng tạo 50 exception subclasses chỉ vì có 50 functions. Taxonomy phải giúp caller quyết định.

Exception kiểu (type / 타입) cũng là API tính tương thích (compatibility / 호환성). thư viện (library / 라이브러리) đổi từ `ValueError` sang custom lỗi (error / 오류) có thể phá bên tiêu thụ (consumer / 소비자) đang catch chính xác (exact / 정확한) kiểu (type / 타입). Khi refactor taxonomy, xem nó như công khai (public / 공개) đặc tả hợp đồng (contract / 계약) nếu exception vượt ranh giới mô-đun (module boundary / 모듈 경계).

> **Chuyển mạch:** Exception taxonomy mô tả failure contract; configuration và feature evolution quyết định contract nào được bật theo môi trường/version. Failure matrix tiếp theo kiểm tra các tổ hợp đó dưới production conditions.

## 26. kiến trúc (architecture / 아키텍처): cấu hình (configuration / 구성) và tính năng (feature / 기능) evolution

Cấu hình (config / 설정) nên parse một lần thành typed/validated đối tượng (object / 객체) ở startup. Passing `os.getenv()` rải khắp mã (code / 코드) làm phụ thuộc (dependency / 의존성) ẩn và kiểm thử (test / 테스트) khó.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    timeout_seconds: float
    dry_run: bool
```

Adapter env → Settings nằm ở composition gốc (root / 루트). nghiệp vụ (business / 비즈니스) mã (code / 코드) nhận `Settings` hoặc specific values. Đây là ứng dụng (application / 애플리케이션) kiến trúc (architecture / 아키텍처) áp dụng mô hình đối tượng (object model / 객체 모델)/immutability từ Part 1–2.

Cờ tính năng (feature flag / 기능 플래그) cũng là cấu hình (configuration / 구성) có vòng đời (lifecycle / 생명주기). Nếu flag thay đổi thời gian chạy (runtime / 런타임), mã (code / 코드) phải biết consistency phạm vi (scope / 범위): mỗi yêu cầu (request / 요청) snapshot một giá trị (value / 값) hay mỗi branch đọc live store? Hai hành vi (behavior / 동작) khác nhau và có thể tạo yêu cầu (request / 요청) chạy nửa theo old flag, nửa theo new flag nếu không định nghĩa snapshot ranh giới (boundary / 경계).

> **Chuyển mạch:** Feature/config evolution tạo ra các versioned states; failure matrix biến chúng thành test cases có owner và evidence. Master checklist tiếp theo gom các case thành điều kiện review cho một service.

## 27. môi trường vận hành (production / 운영 환경) thất bại (failure / 실패) ma trận (matrix / 행렬)

| Hiện tượng | cơ chế (mechanism / 메커니즘) cần kiểm tra | Sai lầm thường gặp |
|---|---|---|
| bộ nhớ (memory / 메모리) tăng mãi | retained references, unbounded bộ nhớ đệm (cache / 캐시)/hàng đợi (queue / 큐)/tasks | gọi `gc.collect()` rồi coi là fix |
| Async dịch vụ (service / 서비스) “đơ” | blocking sync lời gọi (call / 호출) / CPU vòng lặp (loop / 루프) / await không suspend | tăng số coroutine |
| hàng đợi (queue / 큐) bộ nhớ (memory / 메모리) tăng | producer nhanh hơn bên tiêu thụ (consumer / 소비자), hàng đợi (queue / 큐)/tác vụ (task / 작업) creation không bounded | chỉ thêm semaphore quanh worker |
| Shutdown treo | tác vụ (task / 작업)/luồng thực thi (thread / 스레드)/executor không đơn vị sở hữu (owner / 오너), CPU vòng lặp (loop / 루프) không yield, tài nguyên (resource / 자원) close không deadline | gửi thêm tín hiệu (signal / 신호) rồi hy vọng |
| `queue.join()` trả nhưng công việc (work / 작업) chưa xong | immediate hàng đợi (queue / 큐) shutdown hoặc `task_done()` sai bất biến (invariant / 불변식) | coi phép nối (join / 조인) như “mọi side tác động (effect / 효과) đã lần ghi nhận (commit / 커밋)” |
| yêu cầu (request / 요청) cancel nhưng side tác động (effect / 효과) vẫn chạy | sync công việc (work / 작업) đã offload sang luồng thực thi (thread / 스레드)/tiến trình (process / 프로세스)/bên ngoài (external / 외부) dịch vụ (service / 서비스) | tưởng cancel coroutine là kill thực thi (execution / 실행) tài nguyên (resource / 자원) |
| Duplicate job | thử lại (retry / 재시도) + non-idempotent side tác động (effect / 효과) / multi-worker | chỉ thêm cục bộ (local / 로컬) khóa (lock / 잠금) |
| Import thất bại (fail / 실패) ngẫu nhiên | circular import / side tác động (effect / 효과)/thứ tự (order / 순서) | move import vào hàm (function / 함수) ở mọi nơi |
| Attribute “biến mất” hoặc fallback lạ | descriptor precedence / `AttributeError` phát sinh bên trong lookup | chỉ nhìn `__dict__` |
| Cached attribute stale | descriptor/bộ nhớ đệm (cache / 캐시) vô hiệu hóa (invalidation / 무효화) không nối mutation đường dẫn (path / 경로) | clear bộ nhớ đệm (cache / 캐시) thủ công ở caller rải rác |
| luồng thực thi (thread / 스레드) race | dùng chung (shared / 공유) mutable bất biến (invariant / 불변식) | tin rằng GIL bảo vệ nghiệp vụ (business / 비즈니스) thao tác (operation / 연산) |
| Free-threaded không parallel như dự kiến | bản địa (native / 네이티브) extension re-enable GIL / contention / tải công việc (workload / 워크로드) không phù hợp | kết luận bản dựng (build / 빌드) “bị lỗi” từ benchmark đơn |
| Deadlock | khóa (lock / 잠금) thứ tự (ordering / 순서)/cyclic wait | thêm nhiều khóa (lock / 잠금) hơn |
| tiến trình (process / 프로세스) pool chậm | serialization/startup/dữ liệu (data / 데이터) transfer | tăng worker vô hạn |
| trình thông dịch (interpreter / 인터프리터) pool import thất bại (fail / 실패) | extension không hỗ trợ (support / 지원) trình thông dịch (interpreter / 인터프리터) isolation | coi subinterpreter như luồng thực thi (thread / 스레드) thường |
| trình thông dịch (interpreter / 인터프리터) pool chạy nhưng trạng thái (state / 상태) sai | bản địa (native / 네이티브) process-global trạng thái (state / 상태) leak giữa interpreters | chỉ kiểm Python mô-đun (module / 모듈) globals |
| Tests flaky | clock/random/mạng (network / 네트워크)/dùng chung (shared / 공유) fixture/thứ tự (order / 순서) | thử lại (retry / 재시도) kiểm thử (test / 테스트) thay vì loại nondeterminism |
| CPU 100% | hot vòng lặp (loop / 루프), regex/pathological đầu vào (input / 입력), thử lại (retry / 재시도) storm | đổi `list` thành tuple không profile |
| Startup chậm | import đồ thị (graph / 그래프), mạng (network / 네트워크) lời gọi (call / 호출) at import, phụ thuộc (dependency / 의존성) tải (load / 로드) | lazy import tùy tiện |
| Secret leak | repr/log/cấu hình (config / 설정) dump/dấu vết (trace / 추적) | chỉ xóa secret khỏi mã nguồn (source code / 소스 코드) |
| Metrics backend quá tải | high-cardinality labels | thêm nhiều label để “dễ gỡ lỗi (debug / 디버그)” |

> **Chuyển mạch:** Failure matrix biến các versioned states thành evidence có thể review. Master checklist kiểm tra service-level invariants; cầu nối cuối cùng mở ra các owner ngoài Python core khi cần.

## 28. cấp cao (senior / 시니어)/Master rà soát (review / 검토) checklist cho một Python dịch vụ (service / 서비스)

Khi rà soát (review / 검토), đi theo chuỗi nhân quả (causal chain / 인과 사슬) thay vì style checklist thuần túy.

Mã (code / 코드) đang giữ trạng thái (state / 상태) ở đâu và ai sở hữu nó? Có alias mutable không? bộ nhớ đệm (cache / 캐시) nào có freshness/vô hiệu hóa (invalidation / 무효화) đặc tả hợp đồng (contract / 계약)? Attribute truy cập (access / 접근) có descriptor/proxy hành vi (behavior / 동작) ẩn không? đối tượng (object / 객체)/lớp (class / 클래스) được construct bằng hook nào? lớp (class / 클래스) creation có import-time side tác động (effect / 효과) không? thất bại (failure / 실패) propagate tới ranh giới (boundary / 경계) nào? tài nguyên (resource / 자원) cleanup có lexical quyền sở hữu (ownership / 소유권) không? bên ngoài (external / 외부) calls có hết thời gian chờ (timeout / 타임아웃)/deadline/idempotency không? tính đồng thời (concurrency / 동시성) mô hình (model / 모델) có đúng tải công việc (workload / 워크로드) không? thành phần nguyên thủy (primitive / 기본 요소) nào có guarantee thật, guarantee đó ở phạm vi (scope / 범위) nào? trạng thái dùng chung (shared state / 공유 상태) được synchronize theo bất biến (invariant / 불변식) nào? tiến trình (process / 프로세스)/trình thông dịch (interpreter / 인터프리터)/replica scaling có làm cục bộ (local / 로컬) trạng thái (state / 상태) hoặc khóa (lock / 잠금) vô nghĩa không? bản địa (native / 네이티브) phụ thuộc (dependency / 의존성) có hỗ trợ (support / 지원) free-threaded/subinterpreter không? kiểm thử (test / 테스트) đang kiểm đặc tả hợp đồng (contract / 계약) hay hiện thực (implementation / 구현) detail? Packaging/deploy có reproducible không? Shutdown có stop-accept → drain/cancel → close theo deadline không? khả năng quan sát (observability / 관측 가능성) có đủ bằng chứng (evidence / 증거) nhưng vẫn bounded cardinality/chi phí (cost / 비용) không?

Nếu trả lời được các câu đó, cú pháp (syntax / 문법)/API lookup còn lại thường là vấn đề nhỏ.

> **Chuyển mạch:** Master checklist xác định phần nào còn thuộc Python runtime và phần nào cần owner khác như OS, network, database hoặc framework. Cầu nối này đưa người học tới nguồn chính tương ứng mà không tạo duplicate chapter.

## 29. cầu nối (bridge / 브리지) ra ngoài Python cốt lõi (core / 핵심)

- FastAPI/ASGI là ví dụ để nối coroutine, vòng lặp sự kiện (event loop / 이벤트 루프), khóa (lock / 잠금) và `to_thread`; routing/phụ thuộc (dependency / 의존성) injection thuộc FastAPI/backend domain, không phải Python core.
- Các ví dụ triển khai phải được viết từ case study còn được owner duy trì; không dùng worker sinh tài liệu làm nguồn chuẩn.
- tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), scheduling, networking và algorithms sâu hơn: [Computer Science Knowledge Library](../../computer_science/README.md).
- AI/kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링) framework-specific hành vi (behavior / 동작) không được duplicate vào Python cốt lõi (core / 핵심). Khi các chuẩn gốc (canonical / 정본) lĩnh vực (domain / 도메인) đó tồn tại, Python README nên link trực tiếp tới chapter tương ứng.

> **Chuyển mạch:** Cầu nối chốt ranh giới của Part 4: Python runtime đã được giải thích, còn claim bên ngoài phải quay về canonical owner và nguồn chính. Đây là điểm kết thúc của file.

## Nguồn chính

- Python ngôn ngữ (language / 언어) tham chiếu (reference / 참조): https://docs.python.org/3.14/reference/
- mô hình dữ liệu (data model / 데이터 모델): https://docs.python.org/3.14/reference/datamodel.html
- Descriptor Guide: https://docs.python.org/3.14/howto/descriptor.html
- mô hình thực thi (execution model / 실행 모델): https://docs.python.org/3.14/reference/executionmodel.html
- Import hệ thống (system / 시스템): https://docs.python.org/3.14/reference/import.html
- `dis`: https://docs.python.org/3.14/library/dis.html
- `inspect`: https://docs.python.org/3.14/library/inspect.html
- `gc`: https://docs.python.org/3.14/library/gc.html
- `weakref`: https://docs.python.org/3.14/library/weakref.html
- `contextvars`: https://docs.python.org/3.14/library/contextvars.html
- `asyncio` synchronization primitives: https://docs.python.org/3.14/library/asyncio-sync.html
- `asyncio` queues: https://docs.python.org/3.14/library/asyncio-queue.html
- `asyncio` runners: https://docs.python.org/3.14/library/asyncio-runner.html
- `concurrent.interpreters`: https://docs.python.org/3.14/library/concurrent.interpreters.html
- `concurrent.futures`: https://docs.python.org/3.14/library/concurrent.futures.html
- C API mô-đun (module / 모듈) slots: https://docs.python.org/3.14/c-api/module.html
- Free-threaded C extensions: https://docs.python.org/3.14/howto/free-threading-extensions.html
- luồng thực thi (thread / 스레드) trạng thái (state / 상태)/GIL: https://docs.python.org/3.14/c-api/threads.html
- `signal`: https://docs.python.org/3.14/library/signal.html
- `asyncio`: https://docs.python.org/3.14/library/asyncio.html
- Python 3.14 What's New: https://docs.python.org/3.14/whatsnew/3.14.html
- Packaging người dùng (user / 사용자) Guide: https://packaging.python.org/

> **Bàn giao:** Sau **Nguồn chính**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
