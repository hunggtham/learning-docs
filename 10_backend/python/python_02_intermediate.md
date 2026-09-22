# Python Part 2 — Intermediate: Data model, abstraction và standard-library engineering

> Baseline: Python 3.14.7. Kiểm chứng: 2026-09-22.

Part 1 xây mental model name → object. Part 2 đi xuống data model: tại sao `len(x)`, `for`, `with`, `+`, indexing, context manager và nhiều syntax khác có thể hoạt động với object do chính ta định nghĩa. Đây là điểm Python chuyển từ “ngôn ngữ có cú pháp tiện” thành một object protocol system.

## 1. Class không chỉ là nơi chứa field

`lớp (class / 클래스)`

`thể hiện (instance / 인스턴스)`

Một `class` statement được thực thi để tạo class object. Instance được tạo bằng cách gọi class. Attribute lookup, method binding và inheritance đều có rule của data model; vì vậy OOP Python không nên được học bằng cách bê nguyên mental model Java/C++ sang.

```python
class Account:
    currency = "KRW"

    def __init__(self, owner: str, balance: int = 0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        self.balance += amount
```

`currency` nằm trên class namespace. `owner` và `balance` được bind trên instance. Khi evaluate `account.deposit`, Python attribute machinery tìm function trên class và tạo bound method có instance gắn làm first argument. `self` không phải keyword đặc biệt của parser; nó là convention cực mạnh của ecosystem.

### Class attribute và instance attribute

Pitfall thường gặp là đặt mutable state trên class khi thực ra cần state riêng cho mỗi instance:

```python
class BadCart:
    items = []  # dùng chung giữa mọi instance
```

Nếu shared state là chủ đích, class attribute có thể đúng. Nếu không, initialize trong `__init__` hoặc dùng `dataclass` với `default_factory`.

## 2. Data model và dunder methods

`mô hình dữ liệu (data model / 데이터 모델)`

`phương thức đặc biệt (special method, dunder method / 특수 메서드)`

Python syntax thường dispatch qua special methods. `len(x)` liên quan `x.__len__()`, `x[y]` liên quan `__getitem__`, `a + b` liên quan arithmetic protocol, `for` liên quan iteration protocol, `with` liên quan context manager protocol.

Bạn thường không gọi dunder method trực tiếp nếu có syntax/built-in tương ứng. Viết `len(x)` thay vì `x.__len__()` giúp runtime/type có cơ hội dùng protocol đúng và làm code thể hiện intent.

```python
class Batch:
    def __init__(self, records: list[str]) -> None:
        self._records = records

    def __len__(self) -> int:
        return len(self._records)

    def __iter__(self):
        return iter(self._records)
```

Bây giờ `len(batch)` và `for record in batch` hoạt động vì `Batch` tham gia protocol. Đây là một idiom Python quan trọng: thay vì tạo method riêng như `get_record_count()` cho mọi behavior phổ quát, hãy implement protocol chuẩn khi semantics thật sự khớp.

### `__repr__`, `__str__` và observability

`__repr__` nên ưu tiên representation hữu ích cho developer/debugging; `__str__` ưu tiên display cho người dùng. Một `repr` tốt giảm đáng kể thời gian debug log/test failure.

Đừng đưa secret/token/password vào `repr`. Observability và security giao nhau tại đây.

### Equality, `NotImplemented` và hashing custom object

Nếu override `__eq__`, cần suy nghĩ contract với `__hash__`. Mutable object có equality dựa trên mutable fields thường không nên hashable vì thay field sau khi object đã làm dict key có thể phá invariant của hash table.

Một chi tiết quan trọng là comparison method có thể trả `NotImplemented` khi không biết cách so sánh type bên kia. `NotImplemented` không phải `False`; nó báo runtime thử comparison phản chiếu hoặc fallback phù hợp trước khi kết luận.

```python
class Money:
    def __init__(self, amount: int, currency: str) -> None:
        self.amount = amount
        self.currency = currency

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return (
            self.amount == other.amount
            and self.currency == other.currency
        )
```

Trả `False` ngay cho mọi type lạ có thể khóa mất cơ hội để type bên kia định nghĩa comparison hợp lệ. Đây là ví dụ cho data model như một protocol hai phía, không phải chỉ một method local.

Value object immutable là ứng viên tốt cho equality/hash dựa trên fields; `@dataclass(frozen=True)` có thể phù hợp nếu semantics đúng.

## 3. Encapsulation trong Python: boundary bằng convention và property

Python không có private field tuyệt đối như một số ngôn ngữ. Một leading underscore như `_balance` nói “internal API”; name mang double leading underscore kích hoạt name mangling chủ yếu để tránh collision trong inheritance, không phải security mechanism.

```python
class Temperature:
    def __init__(self, celsius: float) -> None:
        self.celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < -273.15:
            raise ValueError("below absolute zero")
        self._celsius = value
```

`property` hữu ích khi muốn giữ attribute-like interface nhưng thêm invariant/computation. Không nên biến mọi field thành Java-style getter/setter chỉ vì quen OOP khác; Python thường ưu tiên simple public attribute cho simple state.

Điểm cơ chế quan trọng: `property` là một descriptor. Khi `self.celsius = value`, assignment không đơn giản ghi `celsius` vào `self.__dict__`; descriptor trên class có thể intercept operation và chuyển nó sang setter. Đây là bridge trực tiếp sang Part 4, nơi exact precedence của data descriptor, instance dictionary, non-data descriptor và class attribute được giải thích đầy đủ.

Mental model hữu ích là: syntax `obj.attr` là một protocol lookup, không phải “đọc field”. Điều đó giải thích vì sao ORM field, cached property, method binding và framework injection có thể nhìn giống attribute bình thường nhưng thực hiện logic phía sau.

## 4. Inheritance và composition

`kế thừa (inheritance / 상속)`

`kết hợp (composition / 합성)`

Inheritance mô hình quan hệ “is-a” và tham gia method resolution order. Composition mô hình “has-a/uses-a”, thường giảm coupling.

```python
class Sender:
    def send(self, message: str) -> None:
        ...

class NotificationService:
    def __init__(self, sender: Sender) -> None:
        self.sender = sender
```

Ở production, composition thường dễ test và thay dependency hơn inheritance hierarchy sâu. Inheritance vẫn phù hợp cho framework hooks, ABC/protocol implementation hoặc specialization có contract rõ.

### MRO và `super()`

Python hỗ trợ multiple inheritance. Method Resolution Order (MRO) xác định path tìm method. `super()` không đơn giản nghĩa “gọi cha trực tiếp”; nó đi tiếp theo MRO từ context hiện tại. Cooperative multiple inheritance đòi hỏi các class trong chain có signature/contract tương thích và đều gọi `super()` đúng cách.

Một lỗi thiết kế điển hình là một class trong chain gọi trực tiếp `Base.method(self)` trong khi class khác dùng `super()`. Khi đó cooperative chain có thể bị bỏ qua hoặc method chạy hai lần. Nếu multiple inheritance là chủ đích, constructor/method tham gia chain phải thống nhất convention và contract.

Nếu bạn không thể giải thích MRO của hierarchy trong vài câu, composition có thể là thiết kế dễ bảo trì hơn.

## 5. `dataclass`: giảm boilerplate nhưng không thay domain modeling

`lớp dữ liệu (data class / 데이터 클래스)`

`@dataclass` sinh một số method như `__init__`, `__repr__`, `__eq__` dựa trên fields. Nó phù hợp cho record/value-oriented object.

```python
from dataclasses import dataclass, field

@dataclass(slots=True)
class Job:
    name: str
    tags: list[str] = field(default_factory=list)
```

`default_factory=list` tạo list mới cho mỗi instance, tránh mutable-default trap. `slots=True` có thể giảm per-instance memory và ngăn arbitrary new attributes trong nhiều trường hợp, nhưng là design choice chứ không phải option bật mặc định mù quáng. Nó ảnh hưởng inheritance, weakrefs và introspection expectations.

`frozen=True` cũng không tạo deep immutability. Nó chủ yếu ngăn assignment/delete field qua generated mechanism; nếu field chứa list/dict mutable thì object graph bên trong vẫn có thể đổi. Vì vậy “frozen dataclass” và “immutable domain value” chỉ tương đương khi toàn state transitively phù hợp với invariant bất biến.

Nếu class có invariant phức tạp, lifecycle, behavior và identity domain mạnh, đừng dùng dataclass chỉ vì muốn ít code. Boilerplate reduction không phải architecture.

## 6. Iterable, iterator và iterator exhaustion

`có thể lặp (iterable / 이터러블)`

`bộ lặp (iterator / 이터레이터)`

Iterable là object có thể cung cấp iterator, thường qua `__iter__`. Iterator giữ iteration state, có `__next__` và thường `__iter__` trả chính nó. `for` lấy iterator rồi gọi `next()` cho tới `StopIteration`.

```python
numbers = [10, 20, 30]
it = iter(numbers)
print(next(it))  # 10
print(next(it))  # 20
```

List là iterable có thể tạo iterator mới nhiều lần. Iterator thường single-pass: sau khi exhausted, lặp lại không tự reset.

```python
it = iter([1, 2])
print(list(it))  # [1, 2]
print(list(it))  # []
```

Iterator exhaustion gây bug tinh vi khi cùng generator/iterator được truyền qua hai validation step. Nếu cần replay, materialize có chủ đích hoặc thiết kế API nhận iterable factory. Materialize toàn bộ lại có memory cost, nên quyết định dựa vào data volume.

### Mutate collection trong khi đang iterate

Iteration không tạo snapshot chung cho mọi container. Nếu mutate list structure trong loop, index progression có thể làm phần tử bị skip hoặc xử lý lặp lại:

```python
items = [1, 2, 3, 4]
for item in items:
    if item % 2 == 0:
        items.remove(item)
```

Code trên có thể cho kết quả khó reasoning vì iterator đang tiến trên chính list bị thay đổi. Với `dict`/`set`, thay đổi kích thước trong iteration thường bị phát hiện và raise `RuntimeError`. Đừng biến những khác biệt implementation này thành mẹo.

Nếu mục tiêu là filter, tạo collection mới thường rõ hơn:

```python
items = [item for item in items if item % 2 != 0]
```

Nếu thật sự cần mutate original, iterate trên snapshot như `for key in list(mapping): ...` và chấp nhận cost copy rõ ràng. Mental model là iterator và container đang chia sẻ lifecycle/state; mutation policy phải explicit.

## 7. Generator: lazy state machine

`bộ sinh (generator / 제너레이터)`

Function có `yield` tạo generator function; gọi nó trả generator object mà body chưa chạy hết. Mỗi `next()` resume execution từ vị trí yield trước đó.

```python
def read_batches(rows, size: int):
    batch = []
    for row in rows:
        batch.append(row)
        if len(batch) == size:
            yield batch
            batch = []
    if batch:
        yield batch
```

Generator giúp streaming và bounded memory. Nhưng laziness thay đổi thời điểm exception/side effect xảy ra: lỗi có thể xuất hiện khi consumer iterate, không phải lúc generator object được tạo.

`yield from` delegate iteration và forwarding generator protocol cho sub-iterator; nó không chỉ là sugar cho nested loop trong các case có `send`/`throw`/return value, dù đa số business code chỉ cần hiểu delegation cơ bản.

### Generator có lifecycle và có thể bị đóng sớm

Generator protocol không chỉ có `next()`. Consumer hoặc runtime có thể `send()`, `throw()` hoặc `close()` generator. `close()` yêu cầu generator kết thúc; cleanup trong `finally` vì vậy vẫn quan trọng nếu generator sở hữu resource.

```python
def lines(path):
    f = open(path, encoding="utf-8")
    try:
        for line in f:
            yield line
    finally:
        f.close()
```

Pattern trên đúng về cleanup nhưng API vẫn đặt resource lifetime phụ thuộc consumer có iterate/close đúng cách. Khi resource ownership quan trọng, context manager hoặc API callback thường làm lifetime rõ hơn. Lazy evaluation là lợi thế về memory nhưng đồng thời đẩy execution và failure sang consumer boundary.

### Async iterable, async iterator và async generator

`có thể lặp bất đồng bộ (async iterable / 비동기 이터러블)` là object cung cấp `__aiter__()`. `bộ lặp bất đồng bộ (async iterator / 비동기 이터레이터)` cung cấp `__anext__()` trả awaitable và kết thúc bằng `StopAsyncIteration`. `async for` là syntax tiêu thụ protocol này.

Khác biệt bản chất với iterator thường là lấy phần tử kế tiếp có thể phải chờ I/O. Ví dụ một stream event từ socket hoặc database cursor async không thể luôn trả item ngay lập tức:

```python
async for event in event_stream:
    await handle(event)
```

Async generator dùng `async def` cùng `yield`. Nó kết hợp suspended generator state với khả năng `await` giữa các lần yield:

```python
async def poll(source):
    while True:
        item = await source.next_item()
        if item is None:
            return
        yield item
```

Điều này không làm CPU loop “nhanh hơn”; giá trị nằm ở việc producer có thể suspend khi chờ I/O và consumer giữ được streaming/backpressure-friendly structure. Async generator cũng có lifecycle: consumer có thể dừng sớm, cancellation có thể xảy ra giữa các `await`, và cleanup trong `finally` vẫn cần thiết. Khi phải đảm bảo đóng một async generator do code dừng iteration sớm, `aclose()` hoặc `contextlib.aclosing()` giúp ownership rõ hơn.

Part 3 sẽ giải event loop, task và cancellation sâu hơn. Ở đây chỉ cần giữ mental model: iterator protocol quyết định **cách lấy item tiếp theo**, còn sync hay async quyết định việc lấy item có thể block/suspend execution context như thế nào.

## 8. Context manager và resource lifetime

`trình quản lý ngữ cảnh (context manager / 컨텍스트 매니저)`

`with` mô hình hóa acquire/use/release. Object tham gia qua `__enter__`/`__exit__`, hoặc async counterparts cho `async with`.

```python
with open("data.txt", encoding="utf-8") as f:
    text = f.read()
```

Lợi ích cốt lõi không phải bớt `close()`, mà là cleanup được gắn vào lexical control-flow boundary kể cả khi exception xảy ra.

Custom resource:

```python
from contextlib import contextmanager

@contextmanager
def transaction(db):
    tx = db.begin()
    try:
        yield tx
    except Exception:
        tx.rollback()
        raise
    else:
        tx.commit()
```

Context manager không nên nuốt exception trừ khi contract thực sự nói lỗi đã được xử lý. Suppression vô tình tạo failure im lặng.

Ở protocol level, `__exit__` nhận thông tin exception và nếu trả truthy thì exception được coi là đã xử lý. Với `@contextmanager`, exception phát sinh trong block được throw trở lại vào generator tại `yield`; nếu generator catch rồi kết thúc bình thường mà không re-raise, exception cũng bị suppress.

Đây là lý do context manager cho transaction cần `raise` lại sau rollback. “Cleanup thành công” không đồng nghĩa “business operation thành công”. Resource lifetime và failure semantics là hai contract riêng.

## 9. Decorator: transform binding có chủ đích

`bộ trang trí (decorator / 데코레이터)`

Decorator syntax áp dụng callable/class transformer tại definition time:

```python
def traced(fn):
    def wrapper(*args, **kwargs):
        print(f"calling {fn.__name__}")
        return fn(*args, **kwargs)
    return wrapper

@traced
def calculate(x: int) -> int:
    return x * 2
```

Thực chất gần với `calculate = traced(calculate)`. Vì wrapper là function mới, production decorator nên dùng `functools.wraps` để bảo toàn metadata hữu ích cho debugging, introspection và framework.

```python
from functools import wraps

def traced(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        ...
        return fn(*args, **kwargs)
    return wrapper
```

Decorator có thể làm control flow vô hình. Authentication, retry, transaction, caching rất mạnh nhưng nếu stack quá nhiều decorator thì debug call path khó. Senior decision là cân bằng cross-cutting concern với explicitness.

Decorator có state cũng cần concurrency/lifecycle reasoning. Nếu closure của decorator giữ mutable dict cache hoặc counter, state đó được share theo lifetime của decorated function object. Khi code chạy nhiều threads/processes, “decorator chỉ là syntax” không còn là mental model đủ sâu.

## 10. Typing: documentation + static contract, không phải runtime enforcement

`gợi ý kiểu (type hint / 타입 힌트)`

`kiểu cấu trúc (structural typing / 구조적 타이핑)`

Runtime Python không tự enforce annotation. Type checker, IDE, linter và framework có thể consume metadata, nhưng `def add(x: int)` vẫn có thể được gọi bằng object khác nếu runtime code không validate.

```python
def normalize(names: list[str]) -> list[str]:
    return [name.strip().lower() for name in names]
```

Type hint tốt làm data flow và contract rõ. Type hint tệ là khi dùng `Any` khắp nơi, cast để “im checker”, hoặc type quá phức tạp hơn business model.

### `Any` khác `object`

`Any` gần như nói với type checker “hãy ngừng chứng minh ở đây”; operation tùy ý thường được cho qua và uncertainty lan tiếp. `object` nói “đây là một Python object nhưng chưa biết type cụ thể”; checker chỉ cho các operation thực sự hợp lệ cho mọi object cho tới khi code narrow type.

```python
from typing import Any


def unsafe(value: Any) -> None:
    value.this_might_not_exist()  # checker thường cho qua


def inspect_value(value: object) -> None:
    if isinstance(value, str):
        print(value.upper())
```

Vì vậy dùng `object` khi muốn biểu diễn unknown value nhưng vẫn giữ type safety; dùng `Any` khi boundary thực sự cần escape hatch và kiểm soát nơi uncertainty đi vào.

### `Protocol` và duck typing có type safety

```python
from typing import Protocol

class Writer(Protocol):
    def write(self, text: str) -> int: ...


def save_report(writer: Writer, report: str) -> None:
    writer.write(report)
```

Một object không cần inherit `Writer`; chỉ cần static shape phù hợp. Đây là structural subtyping và rất hợp với composition/testing. `@runtime_checkable` chỉ kiểm tra presence theo giới hạn runtime protocol; đừng hiểu nó như full runtime type verifier.

### Generic hiện đại và variance

Python 3.12+ có type-parameter syntax:

```python
def first[T](items: list[T]) -> T:
    return items[0]
```

Legacy-compatible code thường dùng `TypeVar`:

```python
from typing import TypeVar
T = TypeVar("T")


def first(items: list[T]) -> T:
    return items[0]
```

Cả hai mental model đều cần biết vì ecosystem còn nhiều library hỗ trợ phiên bản cũ.

Một điểm dễ nhầm là container mutable không thể tự do thay subtype. Giả sử `Cat` là subtype của `Animal`. Nếu `list[Cat]` được dùng như `list[Animal]`, function nhận `list[Animal]` có thể append `Dog`, phá invariant của list ban đầu. Vì vậy mutable generic như `list[T]` được type checker xử lý chặt hơn read-only abstraction.

Nếu function chỉ cần đọc, type rộng hơn như `Sequence[Animal]` thường diễn tả intent tốt hơn:

```python
from collections.abc import Sequence


def feed_all(animals: Sequence[Animal]) -> None:
    for animal in animals:
        animal.feed()
```

Variance không phải “lý thuyết type để học thuộc”; nó xuất hiện trực tiếp từ câu hỏi API có quyền write value mới vào container hay chỉ read value hiện có.

### `Self`: contract trả về đúng dynamic class

`Self` biểu diễn class hiện tại trong type system. Nó hữu ích cho fluent API, context manager trả `self` và alternative constructor vì subclass nên giữ được type chính xác của chính nó.

```python
from typing import Self

class Query:
    @classmethod
    def empty(cls) -> Self:
        return cls()

    def limit(self, n: int) -> Self:
        self._limit = n
        return self
```

Nếu annotate `-> Query`, caller của subclass có thể mất thông tin subtype. Nhưng `Self` chỉ đúng khi implementation thật sự trả instance tương thích dynamic class; nếu method luôn `return Query()` ngay cả trên subclass thì annotate `Self` sẽ hứa quá mức.

### `TypeIs` và `TypeGuard`: function boolean có thể trở thành bằng chứng cho checker

Một helper runtime có thể kiểm tra dữ liệu rồi cung cấp evidence cho static type checker. `TypeIs[T]` mô tả predicate hai chiều: khi trả `True`, argument được narrow về phần giao với `T`; khi trả `False`, checker có thể loại `T` khỏi type khả dĩ. Type bên trong `TypeIs` phải tương thích như subtype của input type.

```python
from typing import TypeIs


def is_str(value: object) -> TypeIs[str]:
    return isinstance(value, str)
```

`TypeGuard[T]` cũ hơn và linh hoạt theo hướng khác: nhánh `True` có thể narrow tới `T` ngay cả khi `T` không phải subtype theo rule thông thường, điều hữu ích với invariant mutable generic như `list[object]` → `list[str]`. Đổi lại nhánh `False` không có narrowing đối xứng như `TypeIs`.

Điểm senior quan trọng là annotation predicate không tự chứng minh implementation đúng. Nếu function khai `TypeIs[str]` nhưng trả `True` cho integer, checker sẽ reasoning từ một bằng chứng giả và type safety trở nên unsound. Type narrowing helper vì vậy là một **proof boundary**: runtime check và static contract phải khớp nhau.

### Annotation behavior ở modern Python

Python 3.14 thay đổi annotation evaluation theo PEP 649/749: annotation được deferred/lazy hơn so với nhiều code cũ kỳ vọng. Code framework tự đọc `__annotations__` cần theo API/best practices hiện hành như `annotationlib`/`inspect` guidance thay vì giả định mọi annotation đã là runtime object ngay tại definition. Application developer thông thường nên để type checker/framework xử lý hơn là tự introspect thô.

## 11. Exception design và exception propagation

Bắt exception ở layer có khả năng thêm context hoặc quyết định recovery. Một repository function có thể convert low-level database exception thành domain-specific exception nếu caller không nên biết driver; một CLI layer có thể catch domain exception để in message và chọn exit code.

```python
class ConfigError(Exception):
    pass


def load_config(path):
    try:
        ...
    except OSError as exc:
        raise ConfigError(f"cannot read config {path}") from exc
```

Không dùng exception cho control flow bình thường nếu branch predictable và cheap. Ngược lại, Python idiom EAFP (“easier to ask forgiveness than permission”) có thể hợp khi operation chính là source of truth:

```python
try:
    value = mapping[key]
except KeyError:
    value = default
```

LBYL (“look before you leap”) như `if key in mapping` không luôn xấu. Với concurrent/external resources, check rồi action có thể tạo TOCTOU race. Chọn dựa vào semantics chứ không biến EAFP thành giáo điều.

### Nhiều failure cùng tồn tại: `ExceptionGroup`

Concurrent/structured operations có thể có nhiều child failures thay vì một exception đơn. Python 3.11+ có `ExceptionGroup` và `except*` để biểu diễn và xử lý nhóm exception mà không làm mất các failure còn lại.

Intermediate reader chưa cần dùng chúng ở mọi nơi, nhưng cần biết mental model này trước khi sang `asyncio.TaskGroup` ở Part 3: structured concurrency có thể cần báo cáo nhiều lỗi sibling, nên exception model cũng phải biểu diễn nhiều failure cùng lúc thay vì ép chọn một “root exception” duy nhất.

## 12. File I/O, `pathlib`, buffer và streaming

`nhập/xuất (I/O / 입출력)`

`Path` biểu diễn filesystem path bằng object-oriented API và thường rõ hơn string concatenation.

```python
from pathlib import Path

root = Path("data")
for path in root.glob("*.json"):
    print(path.name)
```

Dùng explicit encoding với text files để tránh phụ thuộc platform locale khi portability quan trọng. Với file lớn, `read_text()` load toàn bộ memory; iterate file line-by-line hoặc chunk khi cần bounded memory.

Atomicity là concern khác. “Ghi file thành công” không có nghĩa process crash giữa chừng không thể để file partial. Pattern production có thể ghi temp file cùng filesystem, `flush`/`fsync` theo durability requirement, rồi atomic rename/replace nơi platform hỗ trợ semantics cần thiết.

Path object cũng không phải authorization. `Path.resolve()` có thể giúp canonicalize path nhưng symlink, TOCTOU và permission semantics vẫn thuộc security boundary. Part 3 sẽ nối filesystem API với path traversal và privilege reasoning.

### Buffer protocol và `memoryview`: khi copy dữ liệu trở thành cost thật

`giao thức bộ đệm (buffer protocol / 버퍼 프로토콜)` cho phép một object expose vùng dữ liệu nhị phân bên dưới để consumer truy cập mà không bắt buộc tạo intermediate copy. `bytes`, `bytearray`, `array.array` và nhiều extension type có thể tham gia protocol này. Ở Python level, `memoryview` là abstraction phổ biến để giữ một view lên buffer.

```python
payload = bytearray(b"abcdefgh")
view = memoryview(payload)
window = view[2:6]
window[0] = ord("X")

print(payload)  # bytearray(b'abXdefgh')
```

Khác `list[2:6]`, slice của `memoryview` có thể vẫn tham chiếu cùng underlying storage thay vì copy bytes. Điều này quan trọng với file/network/image/numeric workload lớn vì copy hàng trăm MB chỉ để truyền qua một layer có thể chiếm cả memory bandwidth và tăng allocation pressure.

Nhưng zero-copy không phải miễn phí về design. Consumer phải hiểu buffer read-only hay writable, format/item size là gì, object gốc phải sống bao lâu và mutation qua alias có được phép không. Một `memoryview` writable tạo shared mutable state ở mức byte; bug ownership vì vậy có thể khó thấy hơn list thông thường.

Business code nhỏ không cần đổi mọi `bytes` thành `memoryview`. Chỉ dùng khi profiling hoặc data-flow cho thấy copy là dominant cost, hoặc khi API binary cụ thể đã thiết kế quanh buffer protocol. Mental model quan trọng là phân biệt **value copy** với **view lên cùng storage**.

## 13. Serialization: dữ liệu, compatibility và trust boundary

`tuần tự hóa (serialization / 직렬화)`

JSON phù hợp cho interoperable text data nhưng không biểu diễn mọi Python type. `pickle` có thể serialize nhiều object Python hơn nhưng không an toàn cho dữ liệu không tin cậy vì unpickling có thể thực thi behavior nguy hiểm.

```python
import json
payload = json.dumps({"id": 1, "active": True}, ensure_ascii=False)
restored = json.loads(payload)
```

Production design cần schema/version strategy. Serialization format là contract giữa producer và consumer; thay field/meaning có thể là breaking change dù Python code compile bình thường.

Một subtle failure là “parse thành công” nhưng semantic data vẫn sai. JSON parser chỉ chứng minh input là JSON hợp lệ, không chứng minh `age` nằm trong range, `currency` được hỗ trợ hoặc object đúng version schema. Syntax validation và domain validation là hai tầng khác nhau.

## 14. `datetime`, timezone và thời gian thật

`thời gian có múi giờ (aware datetime / 시간대 인식 datetime)`

`datetime` naive không mang timezone info; aware datetime có `tzinfo` phù hợp. Production event timestamp thường nên lưu/trao đổi ở UTC và convert cho display/business rule ở timezone cần thiết.

```python
from datetime import datetime, timezone
now_utc = datetime.now(timezone.utc)
```

Đừng tự cộng `timedelta(hours=9)` để “tạo Korea time” cho logic tổng quát. Timezone có historical rule/DST ở nhiều khu vực; dùng `zoneinfo.ZoneInfo` với IANA timezone khi cần local civil time.

```python
from zoneinfo import ZoneInfo
seoul = now_utc.astimezone(ZoneInfo("Asia/Seoul"))
```

Một local civil time có thể ambiguous hoặc thậm chí không tồn tại tại DST transition ở một số zone. Vì vậy “2026-11-01 01:30 local” và “một instant tuyệt đối” là hai loại dữ liệu khác nhau. Nếu domain cần lịch hẹn theo local rules, giữ timezone semantics; nếu domain cần event ordering, UTC instant thường phù hợp hơn.

Duration measurement cho timeout/performance nên dùng monotonic clock như `time.monotonic()`/`perf_counter()` thay vì wall clock có thể được chỉnh.

## 15. Regex: parser nhỏ nhưng dễ trở thành debt

`biểu thức chính quy (regular expression / 정규 표현식)`

Regex phù hợp cho lexical pattern tương đối cục bộ. Raw string `r"..."` giảm escaping giữa Python string syntax và regex syntax.

```python
import re
USER_ID = re.compile(r'"user_id"\s*:\s*"([^"]+)"')
```

Nếu input thật sự là JSON, hãy parse JSON thay vì regex. Regex trên structured format thường thất bại khi whitespace, escaping, nesting hoặc ordering thay đổi. Senior note: dùng tool khớp với grammar của dữ liệu.

Catastrophic backtracking có thể thành performance/security risk khi regex nhận untrusted input. Hạn chế pattern mơ hồ, test worst case và cân nhắc parser khác nếu complexity tăng.

## 16. Logging: event có context, không phải `print` nâng cấp

`ghi nhật ký (logging / 로깅)`

Logging production cần level, timestamp, logger name và context đủ để reconstruct event. Library code thường không cấu hình global handler; application entry point sở hữu logging configuration.

```python
import logging
logger = logging.getLogger(__name__)

logger.info("job_completed", extra={"job_id": job_id})
```

Không log secrets, access token, password, full personal data hoặc request body bừa bãi. Structured logging giúp search/aggregation nhưng schema của log cũng cần ổn định.

Dùng lazy formatting của logging khi có thể:

```python
logger.debug("loaded %d records", count)
```

thay vì luôn build expensive f-string trước khi logger biết level có enabled hay không.

Một log record hữu ích nên mang semantic context chứ không chỉ dump object. `repr` và log có thể vô tình kéo secret từ nested object vào output; redaction phải dựa trên data classification chứ không chỉ string replace ở cuối pipeline.

## 17. CLI và `argparse`

CLI là public interface cho người dùng/script khác. `argparse` đủ cho nhiều standard-library tool.

```python
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()
```

Exit code, stdout/stderr, stable option names và help text là API contract. Không trộn business logic vào parser; parse input → validate/configure → gọi application function → map result/exception thành output/exit code.

CLI dùng trong automation còn có machine-consumer. Nếu stdout được parse bởi script khác, format output là compatibility contract; diagnostic nên đi stderr để không phá data stream.

## 18. `subprocess`: process boundary và security

`tiến trình con (subprocess / 하위 프로세스)`

`subprocess.run()` tạo/đợi process với control rõ hơn `os.system`.

```python
import subprocess

result = subprocess.run(
    ["git", "status", "--short"],
    text=True,
    capture_output=True,
    check=True,
)
```

Truyền argument list và mặc định `shell=False` tránh một lớp shell injection. Nếu bắt buộc dùng shell syntax, treat untrusted input đặc biệt cẩn trọng. `check=True` biến non-zero exit thành exception, giúp failure không bị bỏ qua.

Timeout, output size và child-process cleanup là production concerns. Một command treo hoặc in gigabyte output có thể làm service chết dù syntax đúng. `capture_output=True` giữ output trong memory, vì vậy command có output không bounded cần streaming/file redirect hoặc explicit size strategy.

Timeout của một child process cũng không tự định nghĩa lifecycle cho toàn process tree. Child có thể tạo descendants, daemon hoặc external side effect không biến mất chỉ vì parent wrapper raise `TimeoutExpired`. Khi cần hard isolation/cancellation, process group/container/job runner semantics phải được thiết kế ở OS/deployment layer.

## 19. Automation case study trong repository

[automation/pipeline.py](../../automation/pipeline.py) là ví dụ hiện hữu dùng `dataclass`, `Path`, `subprocess`, regex, JSON, environment variables và HTTP I/O. Hãy đọc nó bằng mental model của Part này:

`Usage` là data-oriented state phù hợp với `dataclass`; `Path` tạo filesystem boundary rõ; `subprocess.run([...])` dùng argument list; `clean()`/`split_parts()` dùng regex cho text transformation; `json.loads` parse structured response; exception được raise khi external operation vi phạm invariant.

Điểm cần phân biệt: HTTP client `httpx` là third-party dependency nên kiến thức sâu về client/framework không thuộc Python core. Core library chỉ cần giải thích context manager, exception, I/O và typing đủ để hiểu cách Python orchestrate nó.

Khi review file này, hãy để ý thêm hidden contracts vừa học: collection nào bị mutate hay snapshot; iterator nào single-pass; subprocess output có bounded không; JSON parse xong đã domain-validate chưa; exception nào được translate và exception nào nên propagate; annotation đang là static contract hay runtime evidence.

## 20. Bridge sang Part 3

Khi code bắt đầu có dependency ngoài, nhiều worker, test suite, package install, concurrent I/O, CPU work hoặc deployment, câu hỏi đổi từ “object này hoạt động thế nào?” sang “project này tái lập, test, profile, chạy đồng thời và vận hành ra sao?”. Đó là boundary của Part 3.

Trước khi sang Part 3, bạn nên tự giải thích được vì sao `property` là descriptor-based lookup chứ không phải magic syntax; vì sao `NotImplemented` khác `False`; vì sao mutate container trong iteration nguy hiểm; vì sao generator và async generator có lifecycle riêng; context manager có thể suppress exception bằng contract nào; vì sao `Any` khác `object`; vì sao mutable generic dẫn tới variance constraint; `Self`/`TypeIs` đang hứa điều gì với checker; khi nào `memoryview` là view thay vì copy; và vì sao một timestamp local không luôn ánh xạ đơn giản tới một instant.

## Nguồn chính

- Data Model: https://docs.python.org/3.14/reference/datamodel.html
- `dataclasses`: https://docs.python.org/3.14/library/dataclasses.html
- `typing`: https://docs.python.org/3.14/library/typing.html
- `collections.abc`: https://docs.python.org/3.14/library/collections.abc.html
- Iterators: https://docs.python.org/3.14/library/stdtypes.html#iterator-types
- Async iteration: https://docs.python.org/3.14/reference/expressions.html#asynchronous-generator-iterator-methods
- `contextlib`: https://docs.python.org/3.14/library/contextlib.html
- Exceptions and `ExceptionGroup`: https://docs.python.org/3.14/library/exceptions.html
- `pathlib`: https://docs.python.org/3.14/library/pathlib.html
- `memoryview`: https://docs.python.org/3.14/library/stdtypes.html#memoryview
- Buffer protocol: https://docs.python.org/3.14/c-api/buffer.html
- `datetime`: https://docs.python.org/3.14/library/datetime.html
- `zoneinfo`: https://docs.python.org/3.14/library/zoneinfo.html
- `re`: https://docs.python.org/3.14/library/re.html
- `logging`: https://docs.python.org/3.14/library/logging.html
- `subprocess`: https://docs.python.org/3.14/library/subprocess.html
- Annotation best practices: https://docs.python.org/3.14/howto/annotations.html