# Python Part 4 — Master: Runtime internals, performance, architecture và modern/legacy evolution

> Baseline: Python 3.14.7. Kiểm chứng: 2026-09-22.

Master ở đây không có nghĩa ghi nhớ mọi API. Mục tiêu là có mental model đủ sâu để đọc behavior lạ, điều tra production issue, review design và phân biệt đâu là language guarantee, đâu là CPython implementation detail, đâu là artifact của version cũ. Ở level này, một câu hỏi tốt thường không còn là “API nào làm việc này?”, mà là “invariant nào đang được giữ, runtime duy trì invariant đó bằng cơ chế nào, và cơ chế ấy thất bại ở boundary nào?”.

## 1. Language Python khác implementation CPython

`đặc tả ngôn ngữ (language specification / 언어 명세)`

`hiện thực (implementation / 구현)`

Python Language Reference mô tả semantics của ngôn ngữ. CPython là implementation chuẩn phổ biến, nhưng không phải mọi chi tiết CPython đều là guarantee của Python nói chung. Ví dụ, reference counting và chuyện object thường được thu hồi sớm khi refcount về zero là đặc trưng CPython quan trọng; application portable không nên dùng nó thay resource management explicit.

Khi đọc một behavior, hãy tách bốn tầng:

1. Language reference có guarantee không?
2. Standard-library API có contract không?
3. Nếu không, đây có phải CPython implementation detail?
4. Version, platform và build nào đang chạy?

Cách phân lớp này ngăn việc biến observation trên laptop thành “quy tắc Python”. Nó cũng giúp đọc performance claim chính xác hơn. Ví dụ “dictionary lookup O(1) average” là abstraction thuật toán; exact memory layout, hash implementation và cache behavior lại thuộc implementation/version.

## 2. Compile unit, code object và bytecode

Source module/function được compile thành code object chứa bytecode/instruction metadata, constants, names và information phục vụ runtime. Có thể inspect bằng `dis`:

```python
import dis


def add(a, b):
    return a + b


dis.dis(add)
```

Bytecode là implementation surface có thể đổi giữa minor releases; đừng build business logic phụ thuộc exact opcode. Nó hữu ích để hiểu cost model, compiler optimization hoặc debug tooling.

Modern CPython có specializing adaptive interpreter: runtime có thể specialize execution dựa trên observed types/operations. Điều đó có hai hệ quả. Thứ nhất, “một biểu thức Python luôn tốn N bytecodes” không còn là cost model hữu ích. Thứ hai, microbenchmark quá ngắn có thể đo cả warmup/specialization thay vì steady-state behavior.

Python 3.14 còn có optional tail-call interpreter build configuration trong CPython. Tên này không đồng nghĩa Python function tail-call optimization; nó là interpreter implementation detail.

## 3. Frame, call stack và traceback

Mỗi active Python call liên quan execution frame chứa local/global references, instruction state và runtime stack state. Traceback nối frames tại failure path.

Frame introspection (`inspect`, `sys._getframe`) rất mạnh cho debugger/framework nhưng tạo coupling với runtime và có thể giữ object graph sống lâu hơn nếu references tới frame/traceback được giữ. Một exception object giữ traceback có thể gián tiếp giữ locals, request object, large buffer hoặc secret lâu hơn dự kiến. Vì vậy diagnostic tooling phải có ownership rõ và release references khi chúng hết giá trị.

Exception chaining giữ causality qua `__cause__`/`__context__`. Khi wrap exception, `raise NewError(...) from exc` giúp operator nhìn thấy cả domain context lẫn root cause. Nếu cố tình che implementation detail bằng `raise ... from None`, hãy chắc rằng observability layer khác vẫn giữ evidence cần thiết; hiding chain để message “đẹp” có thể làm incident khó điều tra.

## 4. Namespace, descriptor và attribute lookup

Attribute access `obj.x` không chỉ là lookup trong `obj.__dict__`. Data model có descriptor protocol, class MRO và `__getattribute__`/`__getattr__` hooks.

`bộ mô tả (descriptor / 디스크립터)`

Descriptor là object định nghĩa `__get__`, `__set__` hoặc `__delete__`. Function trên class là descriptor, nhờ đó `instance.method` trở thành bound method. `property`, `classmethod`, `staticmethod`, cached attributes, ORM field và framework attribute đều dựa trên cùng nền tảng này.

### Lookup precedence: tại sao cùng tên nhưng kết quả khác nhau?

Với instance lookup thông thường, mental model hữu ích là:

```text
1. data descriptor trên class/MRO
2. instance __dict__
3. non-data descriptor trên class/MRO
4. class attribute thông thường
5. __getattr__ fallback nếu lookup trước đó thất bại
```

`data descriptor` là descriptor có `__set__` hoặc `__delete__`; nó ưu tiên hơn instance dictionary. Descriptor chỉ có `__get__` là `non-data descriptor`, nên instance attribute cùng tên có thể shadow nó.

`property` thường là data descriptor, vì vậy assignment trực tiếp vào `obj.__dict__["name"]` không nhất thiết override property access. Ngược lại, function là non-data descriptor; truy cập function qua instance kích hoạt `__get__` để tạo bound method.

```python
class Account:
    def deposit(self, amount):
        ...


account = Account()
method = account.deposit

assert method.__self__ is account
assert method.__func__ is Account.deposit
```

`account.deposit(10)` về mental model gần với `Account.deposit(account, 10)`, nhưng binding được descriptor machinery thực hiện, không phải parser chèn `self` bằng mẹo đặc biệt.

### Descriptor có thể biến cache thành vấn đề correctness

Một pattern phổ biến là non-data descriptor hoặc `cached_property` tính value lần đầu rồi lưu vào instance dictionary để lần sau lookup đi thẳng tới cached value. Cơ chế này nhanh vì precedence cho phép instance value shadow non-data descriptor, nhưng ngay lập tức tạo một invariant mới: cached value còn đúng đến khi nào?

Nếu cached value phụ thuộc `self.config`, `self.locale` hoặc mutable child state, invalidation phải đi cùng mutation path. Nếu không, bug không nằm ở descriptor protocol mà ở contract freshness. Một cached attribute không phải “optimization thuần túy”; nó tạo retained state và consistency obligation giống cache ở Part 3.

Khi debug một attribute “không cập nhật”, hãy hỏi ba câu: descriptor có data hay non-data? value hiện nằm ở class hay instance dictionary? dependency nào thay đổi nhưng cache không bị invalidate?

### `__getattribute__` và `__getattr__` không giống nhau

`__getattribute__` tham gia mọi normal attribute access. Nếu override nó và bên trong lại viết `self.name` một cách không kiểm soát, code rất dễ recursion vô hạn. Khi cần delegate behavior mặc định, thường gọi `object.__getattribute__(self, name)` hoặc `super().__getattribute__(name)` theo thiết kế class.

`__getattr__` chỉ là fallback khi normal lookup kết thúc bằng `AttributeError`. Nó phù hợp cho lazy/dynamic attributes hơn là intercept toàn bộ access.

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

Một pitfall framework/proxy là catch `AttributeError` quá rộng bên trong property/descriptor rồi vô tình làm runtime tưởng attribute không tồn tại và chạy `__getattr__`. Vì vậy khi debug “fallback chạy dù property có thật”, hãy nhìn exception origin, không chỉ tên field.

Một pitfall khác là proxy `__getattribute__` forward mọi thứ sang target, kể cả internal attributes của proxy. Proxy tốt phải định nghĩa boundary rõ giữa state của proxy và state được forward; nếu không `__class__`, debug metadata, pickling hoặc introspection có thể cho behavior bất ngờ.

### `__set_name__` và descriptor biết tên của mình

Khi class được tạo, descriptor có `__set_name__()` có thể nhận owner class và attribute name. Đây là mechanism mà validator/ORM-style field có thể tự biết nó được gắn vào field nào mà không lặp string thủ công.

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

Nếu descriptor được gắn vào class sau khi class đã tạo, `__set_name__()` không tự được gọi. Đây là edge case quan trọng với dynamic framework/metaprogramming: assignment `A.x = descriptor` không hoàn toàn tương đương khai báo `x = descriptor` trong class body.

Descriptor mạnh vì nó đưa policy vào lookup protocol, nhưng cái giá là control flow bớt hiển nhiên. Nếu logic chỉ dùng ở một field đơn giản, `property` thường dễ đọc hơn. Descriptor đáng dùng khi cùng mechanism cần tái sử dụng cho nhiều attributes/classes.

### `__slots__`

`__slots__` có thể thay cách instance lưu attributes và giảm memory khi có rất nhiều objects. Nhưng optimization này đi kèm constraints về dynamic attributes, inheritance, weak references và tooling. Hãy đo memory/profile trước. Với 100 objects, complexity có thể không đáng; với hàng triệu nodes, nó có thể đáng kể.

`__slots__` cũng không tự làm object immutable hoặc thread-safe. Nó thay storage model, không thay ownership semantics.

## 5. Function object, closure cell và decorator stack

Function object chứa code object, globals reference, defaults, closure cells và metadata khác. Điều này giải thích nhiều hiện tượng đã thấy:

- default argument sống cùng function object;
- closure giữ cell/binding từ enclosing scope;
- decorator thay function binding bằng object/callable khác;
- monkey patch thay name/attribute lookup target chứ không “sửa bytecode đã gọi trước đó”.

`functools.wraps` chủ yếu copy/update metadata và `__wrapped__`, hỗ trợ introspection. Nó không làm wrapper biến mất khỏi call stack/cost.

Decorator stack cũng tạo ordering semantics. Với:

```python
@outer
@inner
def work():
    ...
```

mental model là `work = outer(inner(work))`. Nếu `inner` tạo transaction còn `outer` retry, semantics khác hẳn khi thứ tự đảo lại. Cross-cutting concern có side effect phải được review theo ordering, không chỉ theo từng decorator riêng lẻ.

## 6. Import system sâu hơn

Import được xây quanh finders, loaders, module specs và `sys.modules`. Một normal import đầu tiên tạo/đăng ký module object rồi execute code. Việc đưa module vào `sys.modules` sớm giúp xử lý recursive import nhưng cũng khiến circular import có thể thấy partially initialized module.

### Import side effects

Plugin registration và framework startup đôi khi cố ý dựa vào import side effect. Nhưng pattern này làm dependency ẩn, order-sensitive và khó test. Khi có thể, dùng explicit registration/bootstrap.

### `__init__.py`, namespace package và public API

Package có thể expose API từ `__init__.py`, nhưng re-export quá nhiều tạo dependency/circular-import khó thấy. Namespace packages cho phép package phân tán qua nhiều locations theo import rules; chỉ dùng khi distribution architecture cần, không vì muốn bỏ file.

### Import cost

Cold start của CLI/serverless có thể bị chi phối bởi import graph. Profile startup thay vì đoán; lazy import có thể giảm startup nhưng chuyển failure sang runtime và tăng complexity.

### Reload không phải state reset

`importlib.reload()` re-execute module code trong module object hiện có, nhưng references đã được copy/bind ở nơi khác không tự được “rewire” thành definitions mới. Instance cũ cũng vẫn thuộc class object cũ. Vì vậy reload phù hợp cho tooling/development scenario có contract rõ; nó không phải generic production strategy để “refresh config/code” trong process sống lâu.

## 7. Object lifecycle, construction, reference counting và cyclic GC

Trong CPython GIL-enabled build truyền thống, refcount là cơ chế lifecycle chính và cyclic GC thu cycles. Free-threaded CPython phải thay đổi nhiều synchronization/refcount implementation details để threads hoạt động an toàn hơn; application không nên dựa vào internal refcount representation.

### `__new__` tạo object, `__init__` khởi tạo object đã tạo

Gọi `MyClass(...)` không đồng nghĩa trực tiếp với gọi `__init__`. Ở mức mental model, metaclass `type.__call__` điều phối object creation: gọi `__new__` để tạo/return object, sau đó nếu object trả về là instance phù hợp thì gọi `__init__` để initialize state.

```python
class User:
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        return obj

    def __init__(self, name):
        self.name = name
```

`__init__` phải return `None`; nó không chọn object nào được trả về. `__new__` đặc biệt hữu ích khi subclass immutable built-ins như `str`, `int`, `tuple`, vì value phải được tạo trước khi `__init__` có cơ hội chạy.

Nếu `__new__` trả object không phải instance của class đang construct, `__init__` tương ứng không chạy. Đây là edge case metaprogramming/factory mạnh nhưng dễ làm lifecycle khó đọc; application code thường không cần dùng.

### Finalization không phải resource ownership

`__del__` làm finalization khó reason hơn khi cycles/interpreter shutdown/resource order liên quan. Dùng context manager hoặc explicit `close()` ownership cho external resources. “Object sẽ được GC” không phải contract về thời điểm file/socket/transaction được release.

Weak references phù hợp cho cache/observer nơi reference phụ không nên giữ object sống. Nhưng weakref callback cũng là lifecycle complexity; không dùng chỉ để “giảm memory”.

### Class creation: class body cũng là code được thực thi

`class C: ...` thực thi class body để tạo namespace rồi tạo class object thông qua metaclass. Default metaclass phổ biến là `type`.

Quá trình class creation có thể reason theo thứ tự sau:

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

`__prepare__` quan trọng với framework/metaclass cần custom namespace behavior trước khi class body chạy. Nhưng namespace được đưa vào `type.__new__` cuối cùng được copy vào mapping riêng của class; giữ reference tới custom namespace rồi giả định mutate nó sẽ mutate class là mental model sai.

Class body chạy tại definition/import time. Vì vậy query database, đọc environment mutable hoặc register global state trong class body đều là import-time side effect như module top level.

### `__class__` cell và zero-argument `super()`

Compiler tạo implicit `__class__` closure cell khi method cần `__class__` hoặc zero-argument `super()`. Custom metaclass thao tác namespace quá mức mà không propagate `__classcell__` đúng tới `type.__new__` có thể phá behavior này. Đây chủ yếu là concern của framework/metaclass author, nhưng nó cho thấy class creation không chỉ là `dict` + `type()` đơn giản.

### `__init_subclass__`, class decorator hay metaclass?

Nếu mục tiêu chỉ là validate/register subclass, `__init_subclass__` thường đơn giản hơn custom metaclass. Nếu muốn transform một class sau khi nó được tạo, class decorator thường explicit hơn. Metaclass hợp khi cần kiểm soát chính quá trình class creation hoặc tạo family class có protocol ở cấp type.

Khi viết `__init_subclass__` trong hierarchy hợp tác, consume keyword mà class mình hiểu và forward phần còn lại bằng `super().__init_subclass__(**kwargs)`. Nuốt hết keyword hoặc không forward có thể phá mixin khác trong hierarchy.

Senior rule không phải “tránh metaclass”, mà là chọn hook nhỏ nhất đáp ứng invariant. Metaclass conflict trong multiple inheritance là failure mode thật: các base classes có incompatible metaclasses có thể khiến class mới không xác định được metaclass hợp lệ và fail ngay lúc definition.

## 8. Immutability, aliasing và API design

Reference semantics làm aliasing trở thành design concern. API nhận mutable object có ba chiến lược chính: mutate theo contract, copy defensively, hoặc treat as read-only convention/type. Mỗi chiến lược có cost.

Copy toàn bộ input ở mọi boundary có thể phá performance và identity semantics. Không copy có thể leak mutation. Thiết kế tốt nói rõ ownership.

```python
class Report:
    def __init__(self, tags: list[str]) -> None:
        self._tags = tuple(tags)
```

Ở đây copy+convert thể hiện invariant “tags của report không đổi qua alias caller”. Đây là reasoning, không phải rule rằng mọi list phải đổi thành tuple.

Một immutable outer object vẫn có thể tham chiếu mutable child. Vì vậy khi domain cần snapshot thật, hãy reason trên object graph chứ không chỉ `frozen=True` hoặc tuple ở root.

## 9. Equality, ordering và domain semantics

`@dataclass(order=True)` có thể sinh ordering lexicographic theo field order, nhưng domain có thật sự có total ordering không? User, connection hoặc transaction không tự nhiên có “nhỏ hơn” chỉ vì fields có thể so sánh.

Implement protocol chỉ khi semantics tồn tại. Convenience-generated dunder methods có thể tạo API sai mà test đơn giản không phát hiện.

Hash/equality contract cũng phải ổn định qua lifetime object nếu object dùng làm dict key/set member. Mutate field tham gia equality/hash sau khi insert là cách phá data structure invariant dù code không raise ngay.

## 10. Type system nâng cao: variance, ParamSpec, TypeVarTuple và protocols

Typing là một language/tooling layer phát triển nhanh. Modern Python type-parameter syntax giúp generic code đọc tự nhiên hơn, nhưng design vẫn cần hiểu abstraction.

`Protocol` diễn tả required behavior mà không ép inheritance. `ParamSpec` hữu ích khi decorator/higher-order function cần giữ callable parameter types. `TypeVarTuple` mô hình variadic generics cho shape-like APIs. `Self`, `TypeIs` và `TypeGuard` từ Part 2 giúp type checker nối method return/narrowing với runtime evidence.

Advanced typing chỉ có giá trị khi làm contract dễ hiểu hơn. Nếu signature generic dài hơn domain model mà nó mô tả, abstraction có thể đang sai tầng.

### Runtime annotations ở Python 3.14

Python 3.14 chuyển annotation semantics sang deferred evaluation model (PEP 649/749). Framework/tool code introspect annotation cần dùng API chính thức hiện hành và xử lý forward references/security đúng cách. Việc evaluate annotation có thể chạy code trong một số introspection pathways; untrusted annotation source không phải dữ liệu vô hại.

Legacy code dùng `from __future__ import annotations` theo PEP 563 era có behavior/intent khác historical default; khi migrate library, test introspection consumers chứ đừng chỉ chạy type checker.

## 11. Memory layout và allocation: tối ưu bằng evidence

Một Python integer/string/object có overhead lớn hơn raw C primitive vì mang metadata/headers/references. Container thường giữ references tới objects chứ không inline toàn bộ object value như typed packed array.

Do đó workload numeric/binary lớn thường dùng specialized packed representation, buffer protocol hoặc native libraries thay vì hàng triệu Python objects nếu domain cho phép. `memoryview` ở Part 2 là ví dụ application-facing của cùng principle: representation quyết định copy cost, memory bandwidth và cache locality.

`sys.getsizeof()` chỉ đo shallow size của object, không toàn object graph. Dùng nó như metric cục bộ, không cộng naïve rồi kết luận process RSS.

RSS còn chịu ảnh hưởng allocator, native libraries, mmap, fragmentation và object đã free ở Python level nhưng allocator chưa trả page về OS. Khi debug memory, tách “Python object retention” khỏi “process RSS behavior”.

## 12. Performance: specialization, cache và deoptimization

CPython optimizer có thể specialize common operations khi runtime assumptions ổn định. Dynamic behavior bất thường có thể làm specialization kém hiệu quả/deopt. Tuy vậy application engineer thường không nên “code cho opcode optimizer” trước algorithm và I/O.

Microbenchmark cần:

- cùng Python build/version;
- đủ repetitions và isolation;
- tránh đo setup nếu không phải target;
- hiểu warmup/specialization;
- nhìn distribution, không chỉ một số;
- xác nhận macro impact trên workload thật.

`timeit` tốt cho microbenchmark; production profiler tốt hơn cho end-to-end hotspot.

Performance optimization phải giữ correctness invariant. Cache, batching, vectorization và concurrency đều có thể đổi failure timing, stale-data window hoặc ownership; benchmark nhanh hơn nhưng semantics sai không phải optimization.

## 13. GIL, free-threading và migration mental model

Python 3.14 là mốc quan trọng: free-threaded CPython officially supported nhưng optional. Vì vậy documentation hiện đại cần chứa hai model.

### Default GIL-enabled CPython

Một thread giữ GIL khi execute Python objects/bytecode. I/O và native code có thể release GIL. Thread vẫn cần locks cho logical shared-state correctness.

### Free-threaded CPython

GIL có thể disabled; multiple threads có thể thực sự execute Python code song song. Built-ins/runtime có thread-safety guarantees cụ thể, nhưng atomicity của một số operation không nên được nâng thành application invariant nếu docs không guarantee.

Một điểm subtle: free-threaded không có nghĩa “không còn synchronization trong runtime”. Thread vẫn cần attached thread state để dùng Python C API, và runtime đôi lúc có thể phải dừng các thread ngắn hạn cho operation như garbage collection. Vì vậy performance model là “không có một global lock giữ mọi Python execution”, không phải “mọi thread luôn chạy tự do không bao giờ dừng nhau”.

### Extension có thể làm GIL quay lại

C extension muốn chạy an toàn khi GIL disabled phải khai báo support. Với multi-phase module initialization, CPython có `Py_mod_gil` slot; module có thể khai báo `Py_MOD_GIL_NOT_USED`. Nếu extension không khai báo support thích hợp, import trên free-threaded build có thể khiến GIL được enable lại cho runtime process theo documented behavior.

Điều này tạo production trap: bạn benchmark pure Python free-threaded thấy parallel tốt, rồi import một dependency native và throughput thay đổi. Vì vậy feature detection phải nằm ở runtime/dependency evidence, không chỉ ở executable name.

### Migration strategy

Không phải đổi flag rồi chạy benchmark. Audit shared mutable state, dependency/C-extension compatibility, thread-local assumptions, caches, signal/process-wide APIs và test race conditions. Race trước đây bị GIL làm khó xuất hiện có thể thành bug thật.

Senior/Master note: viết synchronization dựa trên invariant, không dựa trên “hiện tại operation này có vẻ atomic”.

## 14. Thread safety và process-wide state

Ngay cả free-threaded build, không phải mọi process-wide operation có thể chạy concurrent an toàn. Environment variables, signal handlers, current working directory và một số global native state cần xem contract cụ thể.

Một design tốt giảm shared process-wide mutation: config immutable sau startup, dependency explicit, request/job state scoped, side effects qua owned adapters.

### Thread-safe primitive không nâng cả workflow thành thread-safe

Một container method có internal synchronization hoặc atomicity guarantee chỉ bảo vệ invariant của container ở operation đó. Workflow “check rồi act” vẫn có race:

```python
if key not in cache:
    cache[key] = build_value()
```

Ngay cả khi từng dict operation an toàn ở runtime hiện tại, hai thread vẫn có thể cùng chạy `build_value()`. Application invariant cần lock/single-flight/idempotency tùy semantics.

### Signal là process/main-thread boundary

Python signal handler chạy theo model riêng và việc cài handler bị giới hạn vào main thread của main interpreter. Vì vậy signal không phải generic “interrupt bất kỳ worker thread nào”. Shutdown design nên coi signal là event ở process orchestration layer, sau đó chuyển nó thành state/cancellation mà worker model hiểu.

## 15. `asyncio` internals: readiness, scheduling và backpressure

Event loop không “chạy tất cả coroutine cùng lúc”. Nó schedule runnable callbacks/tasks và chờ I/O readiness/timers. Coroutine chỉ yield control ở await points mà awaitable thực sự suspend.

### Fairness: primitive guarantee khác scheduler fairness

Không giả định event loop chia CPU công bằng giữa mọi task. Một coroutine CPU loop không await sẽ monopolize loop. Thậm chí code có `await` nhưng awaitable hoàn tất tức thì liên tục có thể chạy rất lâu trước khi task khác có cơ hội hữu ích.

Tuy vậy một số primitive có guarantee cụ thể hơn. `asyncio.Lock.acquire()` được documented là fair theo thứ tự coroutine bắt đầu chờ lock. Guarantee này chỉ nói queue waiter của **lock đó**, không nói toàn event loop là fair, không nói semaphore có cùng ordering contract, và không bảo đảm latency công bằng nếu task giữ lock quá lâu.

Đây là pattern reasoning quan trọng: đọc guarantee ở scope nhỏ nhất rồi không suy rộng nó thành guarantee hệ thống.

### Bounded concurrency khác backpressure

Semaphore giới hạn số work cùng chạy. Queue bounded giới hạn số work chờ. Hai concern khác nhau.

Nếu chỉ đặt `Semaphore(20)` nhưng producer vẫn tạo hàng triệu task đang chờ semaphore, memory vẫn có thể tăng lớn. Bounded architecture thường giới hạn cả **in-flight execution** lẫn **queued work**.

### Backpressure bằng bounded queue

Nếu producer nhanh hơn consumer và queue không bound, memory sẽ tăng. `asyncio.Queue(maxsize=N)` khiến `put()` suspend khi queue đầy:

```python
queue = asyncio.Queue(maxsize=100)
await queue.put(item)
```

Backpressure không chỉ là “đỡ memory”. Nó truyền capacity signal upstream. Nếu upstream không thể chậm lại, architecture phải chọn drop, spill-to-disk, reject hoặc external durable queue thay vì giả vờ buffer vô hạn.

### Queue lifecycle và `shutdown()`

Modern `asyncio.Queue` có `shutdown()`. Với graceful shutdown, queue có thể ngừng nhận item mới nhưng cho consumer drain work đã nhận; khi drain xong, `join()` vẫn giữ invariant “mọi work item đã được `task_done()`”.

Immediate shutdown lại cố ý phá invariant thông thường của `join()`: queue có thể được drain/unblock dù work chưa thực sự xử lý. Vì vậy `shutdown(immediate=True)` là emergency control-flow decision, không phải shortcut tương đương graceful drain.

Mental model shutdown queue:

```text
stop accepting
→ decide drain or abandon
→ finish/mark existing work
→ release waiters
→ close downstream resources
```

### Cancellation safety: safe interruption point

Nếu task bị cancel giữa hai side effects, state có thể partial. Transaction/context manager/idempotency giúp define safe interruption points. Shielding cancellation (`asyncio.shield`) chỉ dùng khi operation thực sự phải hoàn tất; lạm dụng làm shutdown không bounded.

Một critical section async có ba loại boundary khác nhau: “không muốn task khác vào” (lock), “không muốn operation bị cancel giữa invariant transition” (cancellation design), và “không muốn remote side effect bị duplicate” (idempotency/transaction). Một `asyncio.Lock` không giải quyết hai loại sau.

Cancellation cũng có scope. Cancel coroutine đang await `to_thread()` không cưỡng chế stop function sync đã chạy trong worker thread. Cancel request không mặc nhiên rollback side effect đã gửi tới remote service. Vì vậy cancellation policy phải nối với idempotency, transaction và ownership của execution resource.

## 16. Structured concurrency và task ownership

`TaskGroup` giúp lexical scope sở hữu tasks. Khi child fail, sibling cancellation và aggregated error handling có semantics rõ hơn loose tasks.

Fire-and-forget task cần registry, exception observation và shutdown handling. Nếu không, lỗi có thể chỉ hiện “Task exception was never retrieved”, hoặc task mất owner theo lifecycle.

Production rule: mọi concurrent unit phải có owner, deadline và failure policy.

### Cancellation propagation không thay business rollback

Structured concurrency tổ chức lifetime của tasks; nó không tự biết rollback database, hoàn tiền payment hay xóa file partial. Khi sibling fail, cancellation chỉ là signal control flow. Domain rollback cần transaction/compensation riêng.

Đây là lý do failure tree và side-effect tree không luôn giống nhau. Một task có thể đã commit external side effect trước khi sibling fail.

## 17. Multiprocessing, multiple interpreters và external resources

Fork copy process state theo OS copy-on-write semantics, nhưng threads, locks, DB/network connections và runtime state có thể không safe khi fork từ multithreaded process. Modern Python/platform defaults thay đổi để giảm unsafe assumptions.

Không mở DB connection pool rồi giả định forked workers có thể share connection object đúng. Tạo per-process resource sau worker startup theo library contract.

IPC serialization means object identity không đi qua process boundary như shared in-process reference. Đây là lý do process architecture thường tự nhiên hơn với messages/value data.

### Multiple interpreters trong Python 3.14

Python 3.14 thêm public high-level API `concurrent.interpreters` và `InterpreterPoolExecutor`. Interpreter là execution context Python với state riêng như import state và builtins. Nhiều interpreters có thể tồn tại trong cùng process, nhưng **interpreter tự nó không tạo concurrency**; concurrency xuất hiện khi execution được đặt trên nhiều threads/interpreters thích hợp.

`InterpreterPoolExecutor` dùng worker threads nhưng mỗi worker chạy trong interpreter riêng. Mỗi interpreter có GIL riêng trong model này, nên worker có thể đạt multi-core parallelism mà không dùng process riêng. Đổi lại isolation mạnh hơn thread thường: mutable Python objects nhìn chung không được chia sẻ tự do giữa interpreters; data cần copy/serialize hoặc đi qua communication primitive phù hợp.

```text
ThreadPoolExecutor
same process + same interpreter state + shared mutable objects

InterpreterPoolExecutor
same process + multiple isolated interpreter states + explicit data transfer

ProcessPoolExecutor
multiple processes + OS address-space isolation + IPC/serialization
```

Không nên gọi subinterpreter là “process nhẹ” vì failure/resource isolation vẫn khác process. Một segfault native extension vẫn có thể làm chết toàn process. Cũng không nên gọi nó là “thread bình thường” vì import/module/global state được isolate theo interpreter.

### Extension compatibility có hai trục khác nhau

Native extension cần phân biệt “có chạy trong subinterpreter không?” và “có chạy khi GIL disabled không?”. CPython C API có module slots khác nhau cho hai capability này.

`Py_mod_multiple_interpreters` cho phép extension khai báo mức support với multiple interpreters. Một module có thể không support subinterpreter, support khi interpreters share GIL, hoặc support per-interpreter GIL. `Py_mod_gil` lại khai báo extension có cần GIL không.

Hai trục này độc lập về mặt reasoning. Một extension có thể thread-safe dưới GIL nhưng vẫn dùng process-global state khiến subinterpreter isolation sai. Hoặc support subinterpreter nhưng chưa an toàn free-threaded. Vì vậy “import được” trong một execution model không chứng minh model khác an toàn.

### Process-global native state là hidden shared state

Python module globals có thể isolate theo interpreter nhưng native static/global variable của extension có thể vẫn sống ở process scope. Extension hiện đại thường cần per-module/per-interpreter state thay vì giả định singleton process-global state nếu muốn support interpreter isolation tốt.

Use case hợp lý cho interpreter pool là CPU-heavy Python tasks có dữ liệu message/value tương đối độc lập và muốn multi-core trong cùng process, nhưng trade-off phải được đo so với process pool và free-threaded threads.

## 18. Native extensions và Python performance ceiling

C/C++/Rust extension hoặc native libraries có thể thực hiện heavy work ngoài Python interpreter. Một số release GIL; một số không. Vì vậy statement “thread không giúp CPU-bound Python” phải thêm điều kiện “pure Python on GIL-enabled CPython”. Native workloads có performance profile khác.

ABI/API compatibility cũng là deployment concern. Wheel tags, platform architecture và Python version quyết định binary distribution nào install được. Pure Python package đơn giản hơn native package về portability.

### Thread state vẫn quan trọng khi GIL disabled

Free-threaded build không xóa khái niệm Python thread state. Native thread dùng Python C API vẫn cần attached thread state. Code C cũ đồng nhất “có thread state” với “đang giữ GIL” có thể cần audit lại mental model.

Long-running native computation không cần Python objects có thể detach thread state để cho runtime/threads khác hoạt động. Trên free-threaded build, detach vẫn có ý nghĩa vì runtime đôi lúc cần coordination như GC stop-the-world ngắn hạn.

### Stable ABI không đồng nghĩa behavior compatibility tuyệt đối

ABI compatibility giúp binary load across supported versions theo contract, nhưng behavior còn phụ thuộc platform library, runtime build mode, extension assumptions và feature support. Deployment test vẫn phải chạy artifact thật trên target environment.

## 19. Security sâu hơn: deserialization, introspection và dynamic execution

Dynamic features làm Python mạnh nhưng tăng attack surface.

`eval`, `exec`, dynamic import, pickle, template rendering, regex, archive extraction, YAML loader của third-party tools, plugin discovery và subprocess đều là boundary cần threat model.

Không có “sanitize string” chung cho mọi context. SQL, shell, HTML, regex, path và URL đều có grammar khác; solution là parameterization/structured API đúng context.

### Introspection cũng có side effect surface

`getattr`, descriptor access, annotation evaluation hoặc plugin import có thể execute code. Security-sensitive tooling không nên giả định “chỉ đang đọc metadata”. Nếu object đến từ untrusted/plugin boundary, inspect operation nào kích hoạt user code cần được hiểu rõ.

### Supply chain

Build system trong `pyproject.toml` có code/dependency thực thi trong build environment. Install package không nên được xem là đọc data thụ động. CI cần isolate build, pin trusted sources và review dependency updates phù hợp risk.

## 20. Observability: log, metric và trace trả lời câu hỏi khác nhau

Log ghi event/context chi tiết. Metric tổng hợp numeric time series. Trace theo request/job qua components. Python code nên expose semantic context chứ không chỉ stack trace.

Instrument tại boundary: request start/end, external call latency, queue depth, retry count, failure class. Đừng log mỗi loop iteration trong hot path rồi tạo bottleneck/log bill.

Correlation ID/context propagation trong async/thread code cần strategy rõ; `contextvars` giữ context-local state qua async task boundaries tốt hơn thread-local trong nhiều async use cases. `asyncio.to_thread()` mang current context sang worker thread, nhưng qua process/interpreter/service boundary thì context phải thành explicit metadata.

### Cardinality là performance/cost invariant của metrics

Label metric bằng `user_id`, request URL raw hoặc exception message arbitrary có thể tạo cardinality khổng lồ. Metric system khi đó tốn memory/cost và query chậm. Metric label nên có bounded domain; high-cardinality detail thuộc log/trace phù hợp hơn.

### Sampling làm evidence không đầy đủ

Trace có thể sampled. Log có thể rate-limit. Metric aggregate mất per-request detail. Vì vậy incident reasoning phải biết loại evidence nào có thể thiếu dữ liệu do policy, không kết luận “không thấy trace = request không xảy ra”.

### Observability không được đổi business behavior

Logging formatter, exporter hoặc tracing hook không nên raise làm fail request thông thường nếu contract không yêu cầu. Instrumentation nằm trên critical path phải có failure policy rõ: drop/buffer/retry/bounded queue, tránh biến outage telemetry thành outage application.

## 21. Deployment: artifact, process, signals và graceful shutdown

Một deployable artifact cần biết Python version/build, dependency resolution/lock, OS/native dependencies, entry point, configuration contract, migration/startup/shutdown behavior, health/readiness semantics và resource limits.

Container image là một cách đóng gói artifact, nhưng reproducibility vẫn phụ thuộc base image tag/digest và build inputs.

### Startup: readiness khác liveness

Process “đang sống” không nghĩa đã sẵn sàng nhận request. Startup có thể cần load config, initialize pool, warm cache bắt buộc hoặc validate migration compatibility. Readiness chỉ nên bật khi invariant phục vụ request đã đạt.

Ngược lại, liveness trả lời process còn khả năng tiến triển hay không. Dùng cùng một check cho cả hai dễ tạo restart loop hoặc route traffic quá sớm.

### Graceful shutdown là protocol nhiều bước

Một shutdown production điển hình:

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

Signal handler không nên làm toàn bộ cleanup phức tạp trực tiếp. Nó nên chuyển process sang shutdown state mà main orchestration/task hiểu.

Python signal handler có main-thread/main-interpreter semantics; điều này càng củng cố việc signal là orchestration boundary, không phải worker-control primitive.

### `asyncio.Runner` và Ctrl-C

`asyncio.Runner` xử lý `SIGINT` theo cách phù hợp async hơn việc để `KeyboardInterrupt` cắt arbitrary internals: nó cancel main task để stack có cơ hội unwind qua `try/finally`, rồi mới surface `KeyboardInterrupt`. Nhưng tight CPU loop không reach suspension point thì cancellation không thể tiến triển bình thường.

Điều này nối trực tiếp scheduler fairness với shutdown correctness: event loop bị monopolize không chỉ tăng latency mà còn làm process khó dừng graceful.

### Queue drain trong shutdown

Nếu dùng `asyncio.Queue`, graceful path nên ngừng producer trước, rồi drain queue và đảm bảo `task_done()`/`join()` invariant. Immediate queue shutdown chỉ dùng khi policy chấp nhận abandon work.

Nếu work đã được giao sang thread/process/external service, queue empty không đồng nghĩa side effect ngoài process đã xong. Shutdown phải theo ownership thật của execution resource.

### Executor và background resource

Default executor/thread pool có lifecycle riêng. Background task không có owner rõ sẽ làm shutdown treo hoặc bị bỏ dở. Mọi background unit nên biết ai chờ nó, ai cancel nó, và deadline nào áp dụng.

### Bytecode cache `.pyc`

CPython có thể cache compiled bytecode trong `__pycache__`; đây là performance artifact, không phải source of truth. Không commit/treat `.pyc` như deploy logic trừ workflow đặc biệt. Invalid cache không nên thay source semantics.

## 22. Version evolution: đọc code cũ bằng context

### Python 2 → Python 3

Legacy rất cũ có `print` statement, bytes/text model khác, integer division differences và old-style idioms. Đừng thêm compatibility hack Python 2 vào code mới.

### Python 3.8–3.11

Rất nhiều production code vẫn target line này. Bạn sẽ gặp `typing.List[str]`, `Optional[T]`, `TypeVar`/`Generic`, manual event-loop patterns và packaging config cũ. Đọc được không có nghĩa tiếp tục viết mới y hệt nếu support matrix đã nâng.

### Python 3.10+

`X | None` union syntax và structural pattern matching xuất hiện. Không dùng `match` chỉ để thay `if/elif` đơn giản.

### Python 3.11

Exception groups/`except*`, `TaskGroup` và nhiều performance improvements làm concurrent error handling hiện đại hơn.

### Python 3.12

Type parameter syntax (`class Box[T]`, `def f[T]`) và typing evolution giúp generic code gọn hơn. Multiple-interpreter C API contracts cũng tiếp tục rõ hơn.

### Python 3.13

Free-threaded build bắt đầu experimental. Queue APIs ở cả sync/async ecosystems có explicit shutdown semantics mới, giúp termination trở thành protocol rõ thay vì chỉ dùng sentinel ad hoc.

### Python 3.14

Free-threaded build officially supported nhưng vẫn optional; t-string (`t"..."`) được thêm; annotation semantics thay đổi theo deferred evaluation; asyncio policy system deprecated hướng tới removal 3.16; `concurrent.interpreters` và `InterpreterPoolExecutor` đưa multiple interpreters thành public application-facing concurrency option. Đây là những version distinctions có thể ảnh hưởng trực tiếp modern code.

Không biến chapter thành changelog: timeline tồn tại để giải thích vì sao codebase cũ và code mới có pattern khác nhau.

## 23. Architecture: functional core, imperative shell

Một pattern hữu ích cho automation/service là giữ domain transformation càng pure/deterministic càng tốt và đẩy filesystem/network/subprocess/time/random ra adapter/orchestration boundary.

Ví dụ, function `split_parts(text) -> dict` trong [automation/pipeline.py](../../automation/pipeline.py) dễ test vì input/output rõ. Git/HTTP operations có side effect nên isolate sau method boundary. Đây là reasoning pattern chứ không yêu cầu codebase phải “functional programming”.

Lợi ích: test nhanh, retry/transaction boundary rõ, failure injection dễ, và concurrency ít shared mutable state.

Pure core không có nghĩa không được cache. Nó có nghĩa cache/clock/random/I/O được đặt ở boundary có ownership explicit, để core semantics không phụ thuộc hidden process state.

## 24. Architecture: sync hay async API?

Đừng chọn async chỉ vì framework hỗ trợ. Nếu entire dependency graph là sync và traffic thấp, sync service có thể đơn giản hơn. Nếu cần hàng nghìn concurrent sockets và ecosystem async-native, async có lợi.

Một API library nên cân nhắc không ép consumer vào event loop nếu operation bản chất CPU/local và sync. Ngược lại, wrap network async API bằng sync thread hack có thể gây nested loop/deadlock/latency complexity.

Boundary tốt là một model nhất quán hoặc cung cấp sync/async adapters có ownership rõ.

Nếu cung cấp cả sync và async API, tránh copy-paste hai implementation business logic độc lập. Tách shared pure logic và hai orchestration adapters để bug fix không divergence.

## 25. Architecture: exception taxonomy

Define exception theo recovery semantics. Ví dụ invalid user input thì caller sửa request; transient external failure có thể retry; configuration error nên fail startup; invariant violation/programming error không nên silently recover.

Đừng tạo 50 exception subclasses chỉ vì có 50 functions. Taxonomy phải giúp caller quyết định.

Exception type cũng là API compatibility. Library đổi từ `ValueError` sang custom error có thể phá consumer đang catch exact type. Khi refactor taxonomy, xem nó như public contract nếu exception vượt module boundary.

## 26. Architecture: configuration và feature evolution

Config nên parse một lần thành typed/validated object ở startup. Passing `os.getenv()` rải khắp code làm dependency ẩn và test khó.

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    timeout_seconds: float
    dry_run: bool
```

Adapter env → Settings nằm ở composition root. Business code nhận `Settings` hoặc specific values. Đây là application architecture áp dụng object model/immutability từ Part 1–2.

Feature flag cũng là configuration có lifecycle. Nếu flag thay đổi runtime, code phải biết consistency scope: mỗi request snapshot một value hay mỗi branch đọc live store? Hai behavior khác nhau và có thể tạo request chạy nửa theo old flag, nửa theo new flag nếu không định nghĩa snapshot boundary.

## 27. Production failure matrix

| Hiện tượng | Mechanism cần kiểm tra | Sai lầm thường gặp |
|---|---|---|
| Memory tăng mãi | retained references, unbounded cache/queue/tasks | gọi `gc.collect()` rồi coi là fix |
| Async service “đơ” | blocking sync call / CPU loop / await không suspend | tăng số coroutine |
| Queue memory tăng | producer nhanh hơn consumer, queue/task creation không bounded | chỉ thêm semaphore quanh worker |
| Shutdown treo | task/thread/executor không owner, CPU loop không yield, resource close không deadline | gửi thêm signal rồi hy vọng |
| `queue.join()` trả nhưng work chưa xong | immediate queue shutdown hoặc `task_done()` sai invariant | coi join như “mọi side effect đã commit” |
| Request cancel nhưng side effect vẫn chạy | sync work đã offload sang thread/process/external service | tưởng cancel coroutine là kill execution resource |
| Duplicate job | retry + non-idempotent side effect / multi-worker | chỉ thêm local lock |
| Import fail ngẫu nhiên | circular import / side effect/order | move import vào function ở mọi nơi |
| Attribute “biến mất” hoặc fallback lạ | descriptor precedence / `AttributeError` phát sinh bên trong lookup | chỉ nhìn `__dict__` |
| Cached attribute stale | descriptor/cache invalidation không nối mutation path | clear cache thủ công ở caller rải rác |
| Thread race | shared mutable invariant | tin rằng GIL bảo vệ business operation |
| Free-threaded không parallel như dự kiến | native extension re-enable GIL / contention / workload không phù hợp | kết luận build “bị lỗi” từ benchmark đơn |
| Deadlock | lock ordering/cyclic wait | thêm nhiều lock hơn |
| Process pool chậm | serialization/startup/data transfer | tăng worker vô hạn |
| Interpreter pool import fail | extension không support interpreter isolation | coi subinterpreter như thread thường |
| Interpreter pool chạy nhưng state sai | native process-global state leak giữa interpreters | chỉ kiểm Python module globals |
| Tests flaky | clock/random/network/shared fixture/order | retry test thay vì loại nondeterminism |
| CPU 100% | hot loop, regex/pathological input, retry storm | đổi `list` thành tuple không profile |
| Startup chậm | import graph, network call at import, dependency load | lazy import tùy tiện |
| Secret leak | repr/log/config dump/trace | chỉ xóa secret khỏi source code |
| Metrics backend quá tải | high-cardinality labels | thêm nhiều label để “dễ debug” |

## 28. Senior/Master review checklist cho một Python service

Khi review, đi theo causal chain thay vì style checklist thuần túy.

Code đang giữ state ở đâu và ai sở hữu nó? Có alias mutable không? Cache nào có freshness/invalidation contract? Attribute access có descriptor/proxy behavior ẩn không? Object/class được construct bằng hook nào? Class creation có import-time side effect không? Failure propagate tới boundary nào? Resource cleanup có lexical ownership không? External calls có timeout/deadline/idempotency không? Concurrency model có đúng workload không? Primitive nào có guarantee thật, guarantee đó ở scope nào? Shared state được synchronize theo invariant nào? Process/interpreter/replica scaling có làm local state hoặc lock vô nghĩa không? Native dependency có support free-threaded/subinterpreter không? Test đang kiểm contract hay implementation detail? Packaging/deploy có reproducible không? Shutdown có stop-accept → drain/cancel → close theo deadline không? Observability có đủ evidence nhưng vẫn bounded cardinality/cost không?

Nếu trả lời được các câu đó, syntax/API lookup còn lại thường là vấn đề nhỏ.

## 29. Bridge ra ngoài Python core

- FastAPI example hiện có: [automation/app.py](../../automation/app.py). Core Python giải thích coroutine, event loop, lock và `to_thread`; routing/dependency injection/ASGI thuộc FastAPI/backend domain khi canonical library tương ứng được xây.
- Automation worker: [automation/pipeline.py](../../automation/pipeline.py) và [automation/README.md](../../automation/README.md).
- Process, thread, scheduling, networking và algorithms sâu hơn: [Computer Science Knowledge Library](../../computer_science/README.md).
- AI/Data Engineering framework-specific behavior không được duplicate vào Python core. Khi các canonical domain đó tồn tại, Python README nên link trực tiếp tới chapter tương ứng.

## Nguồn chính

- Python Language Reference: https://docs.python.org/3.14/reference/
- Data Model: https://docs.python.org/3.14/reference/datamodel.html
- Descriptor Guide: https://docs.python.org/3.14/howto/descriptor.html
- Execution Model: https://docs.python.org/3.14/reference/executionmodel.html
- Import System: https://docs.python.org/3.14/reference/import.html
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
- C API module slots: https://docs.python.org/3.14/c-api/module.html
- Free-threaded C extensions: https://docs.python.org/3.14/howto/free-threading-extensions.html
- Thread state/GIL: https://docs.python.org/3.14/c-api/threads.html
- `signal`: https://docs.python.org/3.14/library/signal.html
- `asyncio`: https://docs.python.org/3.14/library/asyncio.html
- Python 3.14 What's New: https://docs.python.org/3.14/whatsnew/3.14.html
- Packaging User Guide: https://packaging.python.org/
