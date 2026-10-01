# Python Part 2 — Intermediate: mô hình dữ liệu (data model / 데이터 모델), lớp trừu tượng (abstraction / 추상화) và standard-library kỹ thuật (engineering / 엔지니어링)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Python Part 2 — Intermediate: mô hình dữ liệu (data model / 데이터 모델), lớp trừu tượng (abstraction / 추상화) và standard-library kỹ thuật (engineering / 엔지니어링)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. lớp (class / 클래스) không chỉ là nơi chứa trường dữ liệu (field / 필드)** gom dữ liệu hoặc nguồn để kiểm tra một nhận định cụ thể; sau đó sang **2. mô hình dữ liệu (data model / 데이터 모델) và dunder methods** để đối chiếu nhận định với dữ liệu và nguồn. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

> Baseline: Python 3.14.7. Kiểm chứng: 2026-09-22.

Part 1 xây mô hình tư duy (mental model / 사고 모델) name → đối tượng (object / 객체). Part 2 đi xuống mô hình dữ liệu (data model / 데이터 모델): tại sao `len(x)`, `for`, `with`, `+`, indexing, ngữ cảnh (context / 맥락) manager và nhiều cú pháp (syntax / 문법) khác có thể hoạt động với đối tượng (object / 객체) do chính ta định nghĩa. Đây là điểm Python chuyển từ “ngôn ngữ có cú pháp tiện” thành một đối tượng (object / 객체) giao thức (protocol / 프로토콜) hệ thống (system / 시스템).

## 1. lớp (class / 클래스) không chỉ là nơi chứa trường dữ liệu (field / 필드)

`lớp (class / 클래스)`

`thể hiện (instance / 인스턴스)`

Một `class` statement được thực thi để tạo lớp (class / 클래스) đối tượng (object / 객체). Instance được tạo bằng cách gọi lớp (class / 클래스). Attribute lookup, phương thức (method / 메서드) binding và inheritance đều có quy tắc (rule / 규칙) của mô hình dữ liệu (data model / 데이터 모델); vì vậy OOP Python không nên được học bằng cách bê nguyên mô hình tư duy (mental model / 사고 모델) Java/C++ sang.

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

`currency` nằm trên lớp (class / 클래스) không gian tên (namespace / 네임스페이스). `owner` và `balance` được bind trên instance. Khi evaluate `account.deposit`, Python attribute machinery tìm hàm (function / 함수) trên lớp (class / 클래스) và tạo bound phương thức (method / 메서드) có instance gắn làm first argument. `self` không phải từ khóa (keyword / 키워드) đặc biệt của parser; nó là convention cực mạnh của ecosystem.

### Lớp (class / 클래스) attribute và instance attribute

Pitfall thường gặp là đặt mutable trạng thái (state / 상태) trên lớp (class / 클래스) khi thực ra cần trạng thái (state / 상태) riêng cho mỗi instance:

```python
class BadCart:
    items = []  # dùng chung giữa mọi instance
```

Nếu trạng thái dùng chung (shared state / 공유 상태) là chủ đích, lớp (class / 클래스) attribute có thể đúng. Nếu không, initialize trong `__init__` hoặc dùng `dataclass` với `default_factory`.

> **Chuyển mạch:** Trong **Python Part 2 — Intermediate: mô hình dữ liệu (data model / 데이터 모델), lớp trừu tượng (abstraction / 추상화) và standard-library kỹ thuật (engineering / 엔지니어링)**, **1. lớp (class / 클래스) không chỉ là nơi chứa trường dữ liệu (field / 필드)** nêu điều cần giải thích; **2. mô hình dữ liệu (data model / 데이터 모델) và dunder methods** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **3. Encapsulation trong Python: ranh giới (boundary / 경계) bằng convention và thuộc tính (property / 속성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. mô hình dữ liệu (data model / 데이터 모델) và dunder methods

`mô hình dữ liệu (data model / 데이터 모델)`

`phương thức đặc biệt (special method, dunder method / 특수 메서드)`

Python cú pháp (syntax / 문법) thường dispatch qua special methods. `len(x)` liên quan `x.__len__()`, `x[y]` liên quan `__getitem__`, `a + b` liên quan arithmetic giao thức (protocol / 프로토콜), `for` liên quan iteration giao thức (protocol / 프로토콜), `with` liên quan ngữ cảnh (context / 맥락) manager giao thức (protocol / 프로토콜).

Bạn thường không gọi dunder phương thức (method / 메서드) trực tiếp nếu có cú pháp (syntax / 문법)/built-in tương ứng. Viết `len(x)` thay vì `x.__len__()` giúp thời gian chạy (runtime / 런타임)/kiểu (type / 타입) có cơ hội dùng giao thức (protocol / 프로토콜) đúng và làm mã (code / 코드) thể hiện intent.

```python
class Batch:
    def __init__(self, records: list[str]) -> None:
        self._records = records

    def __len__(self) -> int:
        return len(self._records)

    def __iter__(self):
        return iter(self._records)
```

Bây giờ `len(batch)` và `for record in batch` hoạt động vì `Batch` tham gia giao thức (protocol / 프로토콜). Đây là một idiom Python quan trọng: thay vì tạo phương thức (method / 메서드) riêng như `get_record_count()` cho mọi hành vi (behavior / 동작) phổ quát, hãy implement giao thức (protocol / 프로토콜) chuẩn khi ngữ nghĩa (semantics / 의미론) thật sự khớp.

### `__repr__`, `__str__` và khả năng quan sát (observability / 관측 가능성)

`__repr__` nên ưu tiên biểu diễn (representation / 표현) hữu ích cho nhà phát triển (developer / 개발자)/debugging; `__str__` ưu tiên display cho người dùng. Một `repr` tốt giảm đáng kể thời gian gỡ lỗi (debug / 디버그) log/kiểm thử (test / 테스트) thất bại (failure / 실패).

Đừng đưa secret/đơn vị từ (token / 토큰)/password vào `repr`. khả năng quan sát (observability / 관측 가능성) và bảo mật (security / 보안) giao nhau tại đây.

### Equality, `NotImplemented` và hashing custom đối tượng (object / 객체)

Nếu override `__eq__`, cần suy nghĩ đặc tả hợp đồng (contract / 계약) với `__hash__`. Mutable đối tượng (object / 객체) có equality dựa trên mutable fields thường không nên hashable vì thay trường dữ liệu (field / 필드) sau khi đối tượng (object / 객체) đã làm dict key có thể phá bất biến (invariant / 불변식) của bảng băm (hash table / 해시 테이블).

Một chi tiết quan trọng là comparison phương thức (method / 메서드) có thể trả `NotImplemented` khi không biết cách so sánh kiểu (type / 타입) bên kia. `NotImplemented` không phải `False`; nó báo thời gian chạy (runtime / 런타임) thử comparison phản chiếu hoặc fallback phù hợp trước khi kết luận.

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

Trả `False` ngay cho mọi kiểu (type / 타입) lạ có thể khóa mất cơ hội để kiểu (type / 타입) bên kia định nghĩa comparison hợp lệ. Đây là ví dụ cho mô hình dữ liệu (data model / 데이터 모델) như một giao thức (protocol / 프로토콜) hai phía, không phải chỉ một phương thức (method / 메서드) cục bộ (local / 로컬).

Giá trị (value / 값) đối tượng (object / 객체) immutable là ứng viên tốt cho equality/băm (hash / 해시) dựa trên fields; `@dataclass(frozen=True)` có thể phù hợp nếu ngữ nghĩa (semantics / 의미론) đúng.

> **Chuyển mạch:** Ở chặng này của **Python Part 2 — Intermediate: mô hình dữ liệu (data model / 데이터 모델), lớp trừu tượng (abstraction / 추상화) và standard-library kỹ thuật (engineering / 엔지니어링)**, **2. mô hình dữ liệu (data model / 데이터 모델) và dunder methods** đã nêu tiêu chí phân biệt, còn **3. Encapsulation trong Python: ranh giới (boundary / 경계) bằng convention và thuộc tính (property / 속성)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **4. Inheritance và composition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Encapsulation trong Python: ranh giới (boundary / 경계) bằng convention và thuộc tính (property / 속성)

Python không có private trường dữ liệu (field / 필드) tuyệt đối như một số ngôn ngữ. Một leading underscore như `_balance` nói “nội bộ (internal / 내부) API”; name mang double leading underscore kích hoạt name mangling chủ yếu để tránh collision trong inheritance, không phải bảo mật (security / 보안) cơ chế (mechanism / 메커니즘).

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

`property` hữu ích khi muốn giữ attribute-like giao diện (interface / 인터페이스) nhưng thêm bất biến (invariant / 불변식)/computation. Không nên biến mọi trường dữ liệu (field / 필드) thành Java-style getter/setter chỉ vì quen OOP khác; Python thường ưu tiên simple công khai (public / 공개) attribute cho simple trạng thái (state / 상태).

Điểm cơ chế quan trọng: `property` là một descriptor. Khi `self.celsius = value`, assignment không đơn giản ghi `celsius` vào `self.__dict__`; descriptor trên lớp (class / 클래스) có thể intercept thao tác (operation / 연산) và chuyển nó sang setter. Đây là cầu nối (bridge / 브리지) trực tiếp sang Part 4, nơi chính xác (exact / 정확한) precedence của dữ liệu (data / 데이터) descriptor, instance dictionary, non-data descriptor và lớp (class / 클래스) attribute được giải thích đầy đủ.

Mô hình tư duy (mental model / 사고 모델) hữu ích là: cú pháp (syntax / 문법) `obj.attr` là một giao thức (protocol / 프로토콜) lookup, không phải “đọc trường dữ liệu (field / 필드)”. Điều đó giải thích vì sao ORM trường dữ liệu (field / 필드), cached thuộc tính (property / 속성), phương thức (method / 메서드) binding và khung phần mềm (framework / 프레임워크) injection có thể nhìn giống attribute bình thường nhưng thực hiện lô-gic (logic / 논리) phía sau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Python Part 2 — Intermediate: mô hình dữ liệu (data model / 데이터 모델), lớp trừu tượng (abstraction / 추상화) và standard-library kỹ thuật (engineering / 엔지니어링)**, **3. Encapsulation trong Python: ranh giới (boundary / 경계) bằng convention và thuộc tính (property / 속성)** đã nêu tiêu chí phân biệt, còn **4. Inheritance và composition** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **5. dataclass: giảm boilerplate nhưng không thay lĩnh vực (domain / 도메인) modeling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Inheritance và composition

`kế thừa (inheritance / 상속)`

`kết hợp (composition / 합성)`

Inheritance mô hình quan hệ “is-a” và tham gia phương thức (method / 메서드) resolution thứ tự (order / 순서). Composition mô hình “has-a/uses-a”, thường giảm coupling.

```python
class Sender:
    def send(self, message: str) -> None:
        ...

class NotificationService:
    def __init__(self, sender: Sender) -> None:
        self.sender = sender
```

Ở môi trường vận hành (production / 운영 환경), composition thường dễ kiểm thử (test / 테스트) và thay phụ thuộc (dependency / 의존성) hơn inheritance hierarchy sâu. Inheritance vẫn phù hợp cho khung phần mềm (framework / 프레임워크) hooks, ABC/giao thức (protocol / 프로토콜) hiện thực (implementation / 구현) hoặc specialization có đặc tả hợp đồng (contract / 계약) rõ.

### MRO và `super()`

Python hỗ trợ multiple inheritance. phương thức (method / 메서드) Resolution thứ tự (order / 순서) (MRO) xác định đường dẫn (path / 경로) tìm phương thức (method / 메서드). `super()` không đơn giản nghĩa “gọi cha trực tiếp”; nó đi tiếp theo MRO từ ngữ cảnh (context / 맥락) hiện tại. Cooperative multiple inheritance đòi hỏi các lớp (class / 클래스) trong chuỗi (chain / 사슬) có signature/đặc tả hợp đồng (contract / 계약) tương thích và đều gọi `super()` đúng cách.

Một lỗi thiết kế điển hình là một lớp (class / 클래스) trong chuỗi (chain / 사슬) gọi trực tiếp `Base.method(self)` trong khi lớp (class / 클래스) khác dùng `super()`. Khi đó cooperative chuỗi (chain / 사슬) có thể bị bỏ qua hoặc phương thức (method / 메서드) chạy hai lần. Nếu multiple inheritance là chủ đích, constructor/phương thức (method / 메서드) tham gia chuỗi (chain / 사슬) phải thống nhất convention và đặc tả hợp đồng (contract / 계약).

Nếu bạn không thể giải thích MRO của hierarchy trong vài câu, composition có thể là thiết kế dễ bảo trì hơn.

> **Chuyển mạch:** Inheritance/composition quyết định object boundary; dataclass chỉ giảm phần ceremony, không thay domain model. Iterable/iterator tiếp theo chuyển boundary đó sang protocol của việc tạo và tiêu thụ dữ liệu.

## 5. `dataclass`: giảm boilerplate nhưng không thay lĩnh vực (domain / 도메인) modeling

`lớp dữ liệu (data class / 데이터 클래스)`

`@dataclass` sinh một số phương thức (method / 메서드) như `__init__`, `__repr__`, `__eq__` dựa trên fields. Nó phù hợp cho bản ghi (record / 레코드)/value-oriented đối tượng (object / 객체).

```python
from dataclasses import dataclass, field

@dataclass(slots=True)
class Job:
    name: str
    tags: list[str] = field(default_factory=list)
```

`default_factory=list` tạo danh sách (list / 목록) mới cho mỗi instance, tránh mutable-default trap. `slots=True` có thể giảm per-instance bộ nhớ (memory / 메모리) và ngăn arbitrary new attributes trong nhiều trường hợp, nhưng là thiết kế (design / 설계) choice chứ không phải option bật mặc định mù quáng. Nó ảnh hưởng inheritance, weakrefs và introspection expectations.

`frozen=True` cũng không tạo deep immutability. Nó chủ yếu ngăn assignment/delete trường dữ liệu (field / 필드) qua generated cơ chế (mechanism / 메커니즘); nếu trường dữ liệu (field / 필드) chứa danh sách (list / 목록)/dict mutable thì đối tượng (object / 객체) đồ thị (graph / 그래프) bên trong vẫn có thể đổi. Vì vậy “frozen dataclass” và “immutable lĩnh vực (domain / 도메인) giá trị (value / 값)” chỉ tương đương khi toàn trạng thái (state / 상태) transitively phù hợp với bất biến (invariant / 불변식) bất biến.

Nếu lớp (class / 클래스) có bất biến (invariant / 불변식) phức tạp, vòng đời (lifecycle / 생명주기), hành vi (behavior / 동작) và định danh (identity / 식별자) lĩnh vực (domain / 도메인) mạnh, đừng dùng dataclass chỉ vì muốn ít mã (code / 코드). Boilerplate reduction không phải kiến trúc (architecture / 아키텍처).

> **Chuyển mạch:** Dataclass mô tả dữ liệu; iterable/iterator mô tả protocol đọc dữ liệu và trạng thái exhaustion. Generator tiếp theo làm state machine lazy ấy hiện rõ qua từng lần `yield`.

## 6. Iterable, iterator và iterator exhaustion

`có thể lặp (iterable / 이터러블)`

`bộ lặp (iterator / 이터레이터)`

Iterable là đối tượng (object / 객체) có thể cung cấp iterator, thường qua `__iter__`. Iterator giữ iteration trạng thái (state / 상태), có `__next__` và thường `__iter__` trả chính nó. `for` lấy iterator rồi gọi `next()` cho tới `StopIteration`.

```python
numbers = [10, 20, 30]
it = iter(numbers)
print(next(it))  # 10
print(next(it))  # 20
```

Danh sách (list / 목록) là iterable có thể tạo iterator mới nhiều lần. Iterator thường single-pass: sau khi exhausted, lặp lại không tự reset.

```python
it = iter([1, 2])
print(list(it))  # [1, 2]
print(list(it))  # []
```

Iterator exhaustion gây bug tinh vi khi cùng generator/iterator được truyền qua hai kiểm tra hợp lệ (validation / 검증) step. Nếu cần replay, materialize có chủ đích hoặc thiết kế API nhận iterable factory. Materialize toàn bộ lại có bộ nhớ (memory / 메모리) chi phí (cost / 비용), nên quyết định dựa vào dữ liệu (data / 데이터) volume.

### Mutate collection trong khi đang iterate

Iteration không tạo snapshot chung cho mọi bộ chứa (container / 컨테이너). Nếu mutate danh sách (list / 목록) cấu trúc (structure / 구조) trong vòng lặp (loop / 루프), chỉ mục (index / 인덱스) progression có thể làm phần tử bị skip hoặc xử lý lặp lại:

```python
items = [1, 2, 3, 4]
for item in items:
    if item % 2 == 0:
        items.remove(item)
```

Mã (code / 코드) trên có thể cho kết quả khó lập luận (reasoning / 추론) vì iterator đang tiến trên chính danh sách (list / 목록) bị thay đổi. Với `dict`/`set`, thay đổi kích thước trong iteration thường bị phát hiện và raise `RuntimeError`. Đừng biến những khác biệt hiện thực (implementation / 구현) này thành mẹo.

Nếu mục tiêu là filter, tạo collection mới thường rõ hơn:

```python
items = [item for item in items if item % 2 != 0]
```

Nếu thật sự cần mutate original, iterate trên snapshot như `for key in list(mapping): ...` và chấp nhận chi phí (cost / 비용) bản sao (copy / 복사) rõ ràng. mô hình tư duy (mental model / 사고 모델) là iterator và bộ chứa (container / 컨테이너) đang chia sẻ vòng đời (lifecycle / 생명주기)/trạng thái (state / 상태); mutation chính sách (policy / 정책) phải tường minh (explicit / 명시적).

> **Chuyển mạch:** Generator cho thấy mỗi lần tiếp tục đều phụ thuộc state trước đó. Context manager tiếp theo áp dụng cùng tư duy lifecycle cho resource, đặc biệt ở nhánh exception và cleanup.

## 7. Generator: lazy máy trạng thái (state machine / 상태 머신)

`bộ sinh (generator / 제너레이터)`

Hàm (function / 함수) có `yield` tạo generator hàm (function / 함수); gọi nó trả generator đối tượng (object / 객체) mà body chưa chạy hết. Mỗi `next()` resume thực thi (execution / 실행) từ vị trí yield trước đó.

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

Generator giúp streaming và bounded bộ nhớ (memory / 메모리). Nhưng laziness thay đổi thời điểm exception/side tác động (effect / 효과) xảy ra: lỗi có thể xuất hiện khi bên tiêu thụ (consumer / 소비자) iterate, không phải lúc generator đối tượng (object / 객체) được tạo.

`yield from` delegate iteration và forwarding generator giao thức (protocol / 프로토콜) cho sub-iterator; nó không chỉ là sugar cho nested vòng lặp (loop / 루프) trong các trường hợp (case / 사례) có `send`/`throw`/return giá trị (value / 값), dù đa số nghiệp vụ (business / 비즈니스) mã (code / 코드) chỉ cần hiểu delegation cơ bản.

### Generator có vòng đời (lifecycle / 생명주기) và có thể bị đóng sớm

Generator giao thức (protocol / 프로토콜) không chỉ có `next()`. bên tiêu thụ (consumer / 소비자) hoặc thời gian chạy (runtime / 런타임) có thể `send()`, `throw()` hoặc `close()` generator. `close()` yêu cầu generator kết thúc; cleanup trong `finally` vì vậy vẫn quan trọng nếu generator sở hữu tài nguyên (resource / 자원).

```python
def lines(path):
    f = open(path, encoding="utf-8")
    try:
        for line in f:
            yield line
    finally:
        f.close()
```

Mẫu (pattern / 패턴) trên đúng về cleanup nhưng API vẫn đặt tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명) phụ thuộc bên tiêu thụ (consumer / 소비자) có iterate/close đúng cách. Khi tài nguyên (resource / 자원) quyền sở hữu (ownership / 소유권) quan trọng, ngữ cảnh (context / 맥락) manager hoặc API callback thường làm thời gian tồn tại (lifetime / 수명) rõ hơn. Lazy evaluation là lợi thế về bộ nhớ (memory / 메모리) nhưng đồng thời đẩy thực thi (execution / 실행) và thất bại (failure / 실패) sang bên tiêu thụ (consumer / 소비자) ranh giới (boundary / 경계).

### Async iterable, async iterator và async generator

`có thể lặp bất đồng bộ (async iterable / 비동기 이터러블)` là đối tượng (object / 객체) cung cấp `__aiter__()`. `bộ lặp bất đồng bộ (async iterator / 비동기 이터레이터)` cung cấp `__anext__()` trả awaitable và kết thúc bằng `StopAsyncIteration`. `async for` là cú pháp (syntax / 문법) tiêu thụ giao thức (protocol / 프로토콜) này.

Khác biệt bản chất với iterator thường là lấy phần tử kế tiếp có thể phải chờ I/O. Ví dụ một stream sự kiện (event / 이벤트) từ socket hoặc cơ sở dữ liệu (database / 데이터베이스) cursor async không thể luôn trả item ngay lập tức:

```python
async for event in event_stream:
    await handle(event)
```

Async generator dùng `async def` cùng `yield`. Nó kết hợp suspended generator trạng thái (state / 상태) với khả năng `await` giữa các lần yield:

```python
async def poll(source):
    while True:
        item = await source.next_item()
        if item is None:
            return
        yield item
```

Điều này không làm CPU vòng lặp (loop / 루프) “nhanh hơn”; giá trị nằm ở việc producer có thể suspend khi chờ I/O và bên tiêu thụ (consumer / 소비자) giữ được streaming/backpressure-friendly cấu trúc (structure / 구조). Async generator cũng có vòng đời (lifecycle / 생명주기): bên tiêu thụ (consumer / 소비자) có thể dừng sớm, cancellation có thể xảy ra giữa các `await`, và cleanup trong `finally` vẫn cần thiết. Khi phải đảm bảo đóng một async generator do mã (code / 코드) dừng iteration sớm, `aclose()` hoặc `contextlib.aclosing()` giúp quyền sở hữu (ownership / 소유권) rõ hơn.

Part 3 sẽ giải vòng lặp sự kiện (event loop / 이벤트 루프), tác vụ (task / 작업) và cancellation sâu hơn. Ở đây chỉ cần giữ mô hình tư duy (mental model / 사고 모델): iterator giao thức (protocol / 프로토콜) quyết định **cách lấy item tiếp theo**, còn sync hay async quyết định việc lấy item có thể khối (block / 블록)/suspend thực thi (execution / 실행) ngữ cảnh (context / 맥락) như thế nào.

> **Chuyển mạch:** Trong **Python Part 2 — Intermediate: mô hình dữ liệu (data model / 데이터 모델), lớp trừu tượng (abstraction / 추상화) và standard-library kỹ thuật (engineering / 엔지니어링)**, **7. Generator: lazy máy trạng thái (state machine / 상태 머신)** nêu điều cần giải thích; **8. ngữ cảnh (context / 맥락) manager và tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **9. Decorator: transform binding có chủ đích** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. ngữ cảnh (context / 맥락) manager và tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)

`trình quản lý ngữ cảnh (context manager / 컨텍스트 매니저)`

`with` mô hình hóa acquire/use/bản phát hành (release / 릴리스). đối tượng (object / 객체) tham gia qua `__enter__`/`__exit__`, hoặc async counterparts cho `async with`.

```python
with open("data.txt", encoding="utf-8") as f:
    text = f.read()
```

Lợi ích cốt lõi không phải bớt `close()`, mà là cleanup được gắn vào lexical control-flow ranh giới (boundary / 경계) kể cả khi exception xảy ra.

Custom tài nguyên (resource / 자원):

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

Ngữ cảnh (context / 맥락) manager không nên nuốt exception trừ khi đặc tả hợp đồng (contract / 계약) thực sự nói lỗi đã được xử lý. Suppression vô tình tạo thất bại (failure / 실패) im lặng.

Ở giao thức (protocol / 프로토콜) mức (level / 수준), `__exit__` nhận thông tin exception và nếu trả truthy thì exception được coi là đã xử lý. Với `@contextmanager`, exception phát sinh trong khối (block / 블록) được throw trở lại vào generator tại `yield`; nếu generator catch rồi kết thúc bình thường mà không re-raise, exception cũng bị suppress.

Đây là lý do ngữ cảnh (context / 맥락) manager cho giao dịch (transaction / 트랜잭션) cần `raise` lại sau quay lui (rollback / 롤백). “Cleanup thành công” không đồng nghĩa “nghiệp vụ (business / 비즈니스) thao tác (operation / 연산) thành công”. tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론) là hai đặc tả hợp đồng (contract / 계약) riêng.

> **Chuyển mạch:** Ở chặng này của **Python Part 2 — Intermediate: mô hình dữ liệu (data model / 데이터 모델), lớp trừu tượng (abstraction / 추상화) và standard-library kỹ thuật (engineering / 엔지니어링)**, **8. ngữ cảnh (context / 맥락) manager và tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명)** nêu điều cần giải thích; **9. Decorator: transform binding có chủ đích** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **10. Typing: documentation + static đặc tả hợp đồng (contract / 계약), không phải thời gian chạy (runtime / 런타임) enforcement** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Decorator: transform binding có chủ đích

`bộ trang trí (decorator / 데코레이터)`

Decorator cú pháp (syntax / 문법) áp dụng callable/lớp (class / 클래스) transformer tại definition thời gian (time / 시간):

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

Thực chất gần với `calculate = traced(calculate)`. Vì wrapper là hàm (function / 함수) mới, môi trường vận hành (production / 운영 환경) decorator nên dùng `functools.wraps` để bảo toàn siêu dữ liệu (metadata / 메타데이터) hữu ích cho debugging, introspection và khung phần mềm (framework / 프레임워크).

```python
from functools import wraps

def traced(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        ...
        return fn(*args, **kwargs)
    return wrapper
```

Decorator có thể làm điều khiển (control / 제어) luồng (flow / 흐름) vô hình. Authentication, thử lại (retry / 재시도), giao dịch (transaction / 트랜잭션), caching rất mạnh nhưng nếu ngăn xếp (stack / 스택) quá nhiều decorator thì gỡ lỗi (debug / 디버그) lời gọi (call / 호출) đường dẫn (path / 경로) khó. cấp cao (senior / 시니어) quyết định (decision / 결정) là cân bằng cross-cutting concern với explicitness.

Decorator có trạng thái (state / 상태) cũng cần tính đồng thời (concurrency / 동시성)/vòng đời (lifecycle / 생명주기) lập luận (reasoning / 추론). Nếu closure của decorator giữ mutable dict bộ nhớ đệm (cache / 캐시) hoặc counter, trạng thái (state / 상태) đó được share theo thời gian tồn tại (lifetime / 수명) của decorated hàm (function / 함수) đối tượng (object / 객체). Khi mã (code / 코드) chạy nhiều threads/processes, “decorator chỉ là cú pháp (syntax / 문법)” không còn là mô hình tư duy (mental model / 사고 모델) đủ sâu.

> **Chuyển mạch:** Decorator thay đổi binding có chủ đích; typing mô tả contract tĩnh của binding đó nhưng không enforce runtime. Exception design tiếp theo kiểm tra contract khi control-flow đi qua boundary lỗi.

## 10. Typing: documentation + static đặc tả hợp đồng (contract / 계약), không phải thời gian chạy (runtime / 런타임) enforcement

`gợi ý kiểu (type hint / 타입 힌트)`

`kiểu cấu trúc (structural typing / 구조적 타이핑)`

Thời gian chạy (runtime / 런타임) Python không tự enforce annotation. kiểu (type / 타입) checker, IDE, linter và khung phần mềm (framework / 프레임워크) có thể consume siêu dữ liệu (metadata / 메타데이터), nhưng `def add(x: int)` vẫn có thể được gọi bằng đối tượng (object / 객체) khác nếu thời gian chạy (runtime / 런타임) mã (code / 코드) không validate.

```python
def normalize(names: list[str]) -> list[str]:
    return [name.strip().lower() for name in names]
```

Kiểu (type / 타입) hint tốt làm luồng dữ liệu (data flow / 데이터 흐름) và đặc tả hợp đồng (contract / 계약) rõ. kiểu (type / 타입) hint tệ là khi dùng `Any` khắp nơi, cast để “im checker”, hoặc kiểu (type / 타입) quá phức tạp hơn nghiệp vụ (business / 비즈니스) mô hình (model / 모델).

### `Any` khác `object`

`Any` gần như nói với kiểu (type / 타입) checker “hãy ngừng chứng minh ở đây”; thao tác (operation / 연산) tùy ý thường được cho qua và bất định (uncertainty / 불확실성) lan tiếp. `object` nói “đây là một Python đối tượng (object / 객체) nhưng chưa biết kiểu (type / 타입) cụ thể”; checker chỉ cho các thao tác (operation / 연산) thực sự hợp lệ cho mọi đối tượng (object / 객체) cho tới khi mã (code / 코드) narrow kiểu (type / 타입).

```python
from typing import Any

def unsafe(value: Any) -> None:
    value.this_might_not_exist()  # checker thường cho qua

def inspect_value(value: object) -> None:
    if isinstance(value, str):
        print(value.upper())
```

Vì vậy dùng `object` khi muốn biểu diễn unknown giá trị (value / 값) nhưng vẫn giữ kiểu (type / 타입) an toàn (safety / 안전); dùng `Any` khi ranh giới (boundary / 경계) thực sự cần escape hatch và kiểm soát nơi bất định (uncertainty / 불확실성) đi vào.

### `Protocol` và duck typing có kiểu (type / 타입) an toàn (safety / 안전)

```python
from typing import Protocol

class Writer(Protocol):
    def write(self, text: str) -> int: ...

def save_report(writer: Writer, report: str) -> None:
    writer.write(report)
```

Một đối tượng (object / 객체) không cần inherit `Writer`; chỉ cần static shape phù hợp. Đây là structural subtyping và rất hợp với composition/testing. `@runtime_checkable` chỉ kiểm tra presence theo giới hạn thời gian chạy (runtime / 런타임) giao thức (protocol / 프로토콜); đừng hiểu nó như full thời gian chạy (runtime / 런타임) kiểu (type / 타입) verifier.

### Generic hiện đại và variance

Python 3.12+ có type-parameter cú pháp (syntax / 문법):

```python
def first[T](items: list[T]) -> T:
    return items[0]
```

Legacy-compatible mã (code / 코드) thường dùng `TypeVar`:

```python
from typing import TypeVar
T = TypeVar("T")

def first(items: list[T]) -> T:
    return items[0]
```

Cả hai mô hình tư duy (mental model / 사고 모델) đều cần biết vì ecosystem còn nhiều thư viện (library / 라이브러리) hỗ trợ phiên bản cũ.

Một điểm dễ nhầm là bộ chứa (container / 컨테이너) mutable không thể tự do thay subtype. Giả sử `Cat` là subtype của `Animal`. Nếu `list[Cat]` được dùng như `list[Animal]`, hàm (function / 함수) nhận `list[Animal]` có thể append `Dog`, phá bất biến (invariant / 불변식) của danh sách (list / 목록) ban đầu. Vì vậy mutable generic như `list[T]` được kiểu (type / 타입) checker xử lý chặt hơn read-only lớp trừu tượng (abstraction / 추상화).

Nếu hàm (function / 함수) chỉ cần đọc, kiểu (type / 타입) rộng hơn như `Sequence[Animal]` thường diễn tả intent tốt hơn:

```python
from collections.abc import Sequence

def feed_all(animals: Sequence[Animal]) -> None:
    for animal in animals:
        animal.feed()
```

Variance không phải “lý thuyết kiểu (type / 타입) để học thuộc”; nó xuất hiện trực tiếp từ câu hỏi API có quyền ghi (write / 쓰기) giá trị (value / 값) mới vào bộ chứa (container / 컨테이너) hay chỉ read giá trị (value / 값) hiện có.

### `Self`: đặc tả hợp đồng (contract / 계약) trả về đúng động (dynamic / 동적) lớp (class / 클래스)

`Self` biểu diễn lớp (class / 클래스) hiện tại trong hệ kiểu (type system / 타입 시스템). Nó hữu ích cho fluent API, ngữ cảnh (context / 맥락) manager trả `self` và alternative constructor vì subclass nên giữ được kiểu (type / 타입) chính xác của chính nó.

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

Nếu annotate `-> Query`, caller của subclass có thể mất thông tin subtype. Nhưng `Self` chỉ đúng khi hiện thực (implementation / 구현) thật sự trả instance tương thích động (dynamic / 동적) lớp (class / 클래스); nếu phương thức (method / 메서드) luôn `return Query()` ngay cả trên subclass thì annotate `Self` sẽ hứa quá mức.

### `TypeIs` và `TypeGuard`: hàm (function / 함수) boolean có thể trở thành bằng chứng cho checker

Một helper thời gian chạy (runtime / 런타임) có thể kiểm tra dữ liệu rồi cung cấp bằng chứng (evidence / 증거) cho static kiểu (type / 타입) checker. `TypeIs[T]` mô tả predicate hai chiều: khi trả `True`, argument được narrow về phần giao với `T`; khi trả `False`, checker có thể loại `T` khỏi kiểu (type / 타입) khả dĩ. kiểu (type / 타입) bên trong `TypeIs` phải tương thích như subtype của đầu vào (input / 입력) kiểu (type / 타입).

```python
from typing import TypeIs

def is_str(value: object) -> TypeIs[str]:
    return isinstance(value, str)
```

`TypeGuard[T]` cũ hơn và linh hoạt theo hướng khác: nhánh `True` có thể narrow tới `T` ngay cả khi `T` không phải subtype theo quy tắc (rule / 규칙) thông thường, điều hữu ích với bất biến (invariant / 불변식) mutable generic như `list[object]` → `list[str]`. Đổi lại nhánh `False` không có narrowing đối xứng như `TypeIs`.

Điểm cấp cao (senior / 시니어) quan trọng là annotation predicate không tự chứng minh hiện thực (implementation / 구현) đúng. Nếu hàm (function / 함수) khai `TypeIs[str]` nhưng trả `True` cho integer, checker sẽ lập luận (reasoning / 추론) từ một bằng chứng giả và kiểu (type / 타입) an toàn (safety / 안전) trở nên unsound. kiểu (type / 타입) narrowing helper vì vậy là một **proof ranh giới (boundary / 경계)**: thời gian chạy (runtime / 런타임) check và static đặc tả hợp đồng (contract / 계약) phải khớp nhau.

### Annotation hành vi (behavior / 동작) ở hiện đại (modern / 현대적) Python

Python 3.14 thay đổi annotation evaluation theo PEP 649/749: annotation được deferred/lazy hơn so với nhiều mã (code / 코드) cũ kỳ vọng. mã (code / 코드) khung phần mềm (framework / 프레임워크) tự đọc `__annotations__` cần theo API/best practices hiện hành như `annotationlib`/`inspect` guidance thay vì giả định mọi annotation đã là thời gian chạy (runtime / 런타임) đối tượng (object / 객체) ngay tại definition. ứng dụng (application / 애플리케이션) nhà phát triển (developer / 개발자) thông thường nên để kiểu (type / 타입) checker/khung phần mềm (framework / 프레임워크) xử lý hơn là tự introspect thô.

> **Chuyển mạch:** Typing mô tả contract tĩnh nhưng không xử lý failure lúc chạy. Exception design tiếp theo quyết định tầng nào thêm context, đổi loại lỗi hoặc để lỗi đi qua; I/O sau đó áp dụng cùng boundary cho resource.

## 11. Exception thiết kế (design / 설계) và exception propagation

Bắt exception ở tầng (layer / 계층) có khả năng thêm ngữ cảnh (context / 맥락) hoặc quyết định khôi phục (recovery / 복구). Một repository hàm (function / 함수) có thể convert low-level cơ sở dữ liệu (database / 데이터베이스) exception thành domain-specific exception nếu caller không nên biết driver; một CLI tầng (layer / 계층) có thể catch lĩnh vực (domain / 도메인) exception để in message và chọn exit mã (code / 코드).

```python
class ConfigError(Exception):
    pass

def load_config(path):
    try:
        ...
    except OSError as exc:
        raise ConfigError(f"cannot read config {path}") from exc
```

Không dùng exception cho điều khiển (control / 제어) luồng (flow / 흐름) bình thường nếu branch predictable và cheap. Ngược lại, Python idiom EAFP (“easier to ask forgiveness than permission”) có thể hợp khi thao tác (operation / 연산) chính là nguồn chuẩn (source of truth / 정본):

```python
try:
    value = mapping[key]
except KeyError:
    value = default
```

LBYL (“look before you leap”) như `if key in mapping` không luôn xấu. Với concurrent/bên ngoài (external / 외부) resources, check rồi hành động (action / 동작) có thể tạo TOCTOU race. Chọn dựa vào ngữ nghĩa (semantics / 의미론) chứ không biến EAFP thành giáo điều.

### Nhiều thất bại (failure / 실패) cùng tồn tại: `ExceptionGroup`

Concurrent/structured operations có thể có nhiều child failures thay vì một exception đơn. Python 3.11+ có `ExceptionGroup` và `except*` để biểu diễn và xử lý nhóm exception mà không làm mất các thất bại (failure / 실패) còn lại.

Intermediate reader chưa cần dùng chúng ở mọi nơi, nhưng cần biết mô hình tư duy (mental model / 사고 모델) này trước khi sang `asyncio.TaskGroup` ở Part 3: structured tính đồng thời (concurrency / 동시성) có thể cần báo cáo nhiều lỗi sibling, nên exception mô hình (model / 모델) cũng phải biểu diễn nhiều thất bại (failure / 실패) cùng lúc thay vì ép chọn một “gốc (root / 루트) exception” duy nhất.

> **Chuyển mạch:** Ở chặng này của **Python Part 2 — Intermediate: mô hình dữ liệu (data model / 데이터 모델), lớp trừu tượng (abstraction / 추상화) và standard-library kỹ thuật (engineering / 엔지니어링)**, **11. Exception thiết kế (design / 설계) và exception propagation** xác định đầu vào; **12. tệp (file / 파일) I/O, pathlib, buffer và streaming** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **13. Serialization: dữ liệu, tính tương thích (compatibility / 호환성) và trust ranh giới (boundary / 경계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. tệp (file / 파일) I/O, `pathlib`, buffer và streaming

`nhập/xuất (I/O / 입출력)`

`Path` biểu diễn filesystem đường dẫn (path / 경로) bằng object-oriented API và thường rõ hơn string concatenation.

```python
from pathlib import Path

root = Path("data")
for path in root.glob("*.json"):
    print(path.name)
```

Dùng tường minh (explicit / 명시적) encoding với văn bản (text / 텍스트) files để tránh phụ thuộc nền tảng (platform / 플랫폼) locale khi portability quan trọng. Với tệp (file / 파일) lớn, `read_text()` tải (load / 로드) toàn bộ bộ nhớ (memory / 메모리); iterate tệp (file / 파일) line-by-line hoặc chunk khi cần bounded bộ nhớ (memory / 메모리).

Atomicity là concern khác. “Ghi tệp (file / 파일) thành công” không có nghĩa tiến trình (process / 프로세스) crash giữa chừng không thể để tệp (file / 파일) partial. mẫu (pattern / 패턴) môi trường vận hành (production / 운영 환경) có thể ghi temp tệp (file / 파일) cùng filesystem, `flush`/`fsync` theo durability yêu cầu (requirement / 요구사항), rồi atomic rename/replace nơi nền tảng (platform / 플랫폼) hỗ trợ ngữ nghĩa (semantics / 의미론) cần thiết.

Đường dẫn (path / 경로) đối tượng (object / 객체) cũng không phải authorization. `Path.resolve()` có thể giúp canonicalize đường dẫn (path / 경로) nhưng symlink, TOCTOU và permission ngữ nghĩa (semantics / 의미론) vẫn thuộc ranh giới bảo mật (security boundary / 보안 경계). Part 3 sẽ nối filesystem API với đường dẫn (path / 경로) traversal và privilege lập luận (reasoning / 추론).

### Buffer giao thức (protocol / 프로토콜) và `memoryview`: khi bản sao (copy / 복사) dữ liệu trở thành chi phí (cost / 비용) thật

`giao thức bộ đệm (buffer protocol / 버퍼 프로토콜)` cho phép một đối tượng (object / 객체) expose vùng dữ liệu nhị phân bên dưới để bên tiêu thụ (consumer / 소비자) truy cập mà không bắt buộc tạo intermediate bản sao (copy / 복사). `bytes`, `bytearray`, `array.array` và nhiều extension kiểu (type / 타입) có thể tham gia giao thức (protocol / 프로토콜) này. Ở Python mức (level / 수준), `memoryview` là lớp trừu tượng (abstraction / 추상화) phổ biến để giữ một view lên buffer.

```python
payload = bytearray(b"abcdefgh")
view = memoryview(payload)
window = view[2:6]
window[0] = ord("X")

print(payload)  # bytearray(b'abXdefgh')
```

Khác `list[2:6]`, slice của `memoryview` có thể vẫn tham chiếu cùng underlying lưu trữ (storage / 저장소) thay vì bản sao (copy / 복사) bytes. Điều này quan trọng với tệp (file / 파일)/mạng (network / 네트워크)/ảnh (image / 이미지)/numeric tải công việc (workload / 워크로드) lớn vì bản sao (copy / 복사) hàng trăm MB chỉ để truyền qua một tầng (layer / 계층) có thể chiếm cả bộ nhớ (memory / 메모리) bandwidth và tăng allocation pressure.

Nhưng zero-copy không phải miễn phí về thiết kế (design / 설계). bên tiêu thụ (consumer / 소비자) phải hiểu buffer read-only hay writable, format/item kích thước (size / 크기) là gì, đối tượng (object / 객체) gốc phải sống bao lâu và mutation qua alias có được phép không. Một `memoryview` writable tạo dùng chung (shared / 공유) mutable trạng thái (state / 상태) ở mức byte; bug quyền sở hữu (ownership / 소유권) vì vậy có thể khó thấy hơn danh sách (list / 목록) thông thường.

Nghiệp vụ (business / 비즈니스) mã (code / 코드) nhỏ không cần đổi mọi `bytes` thành `memoryview`. Chỉ dùng khi profiling hoặc data-flow cho thấy bản sao (copy / 복사) là dominant chi phí (cost / 비용), hoặc khi API nhị phân (binary / 이진) cụ thể đã thiết kế quanh buffer giao thức (protocol / 프로토콜). mô hình tư duy (mental model / 사고 모델) quan trọng là phân biệt **giá trị (value / 값) bản sao (copy / 복사)** với **view lên cùng lưu trữ (storage / 저장소)**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Python Part 2 — Intermediate: mô hình dữ liệu (data model / 데이터 모델), lớp trừu tượng (abstraction / 추상화) và standard-library kỹ thuật (engineering / 엔지니어링)**, **12. tệp (file / 파일) I/O, pathlib, buffer và streaming** đã nêu tiêu chí phân biệt, còn **13. Serialization: dữ liệu, tính tương thích (compatibility / 호환성) và trust ranh giới (boundary / 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **14. datetime, timezone và thời gian thật** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Serialization: dữ liệu, tính tương thích (compatibility / 호환성) và trust ranh giới (boundary / 경계)

`tuần tự hóa (serialization / 직렬화)`

JSON phù hợp cho interoperable văn bản (text / 텍스트) dữ liệu (data / 데이터) nhưng không biểu diễn mọi Python kiểu (type / 타입). `pickle` có thể serialize nhiều đối tượng (object / 객체) Python hơn nhưng không an toàn cho dữ liệu không tin cậy vì unpickling có thể thực thi hành vi (behavior / 동작) nguy hiểm.

```python
import json
payload = json.dumps({"id": 1, "active": True}, ensure_ascii=False)
restored = json.loads(payload)
```

Môi trường vận hành (production / 운영 환경) thiết kế (design / 설계) cần lược đồ (schema / 스키마)/phiên bản (version / 버전) chiến lược (strategy / 전략). Serialization format là đặc tả hợp đồng (contract / 계약) giữa producer và bên tiêu thụ (consumer / 소비자); thay trường dữ liệu (field / 필드)/meaning có thể là breaking thay đổi (change / 변경) dù Python mã (code / 코드) compile bình thường.

Một subtle thất bại (failure / 실패) là “parse thành công” nhưng ngữ nghĩa (semantic / 의미적) dữ liệu (data / 데이터) vẫn sai. JSON parser chỉ chứng minh đầu vào (input / 입력) là JSON hợp lệ, không chứng minh `age` nằm trong phạm vi (range / 범위), `currency` được hỗ trợ hoặc đối tượng (object / 객체) đúng phiên bản (version / 버전) lược đồ (schema / 스키마). cú pháp (syntax / 문법) kiểm tra hợp lệ (validation / 검증) và lĩnh vực (domain / 도메인) kiểm tra hợp lệ (validation / 검증) là hai tầng khác nhau.

> **Chuyển mạch:** Trong **Python Part 2 — Intermediate: mô hình dữ liệu (data model / 데이터 모델), lớp trừu tượng (abstraction / 추상화) và standard-library kỹ thuật (engineering / 엔지니어링)**, **13. Serialization: dữ liệu, tính tương thích (compatibility / 호환성) và trust ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **14. datetime, timezone và thời gian thật** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **15. Regex: parser nhỏ nhưng dễ trở thành debt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. `datetime`, timezone và thời gian thật

`thời gian có múi giờ (aware datetime / 시간대 인식 datetime)`

`datetime` naive không mang timezone info; aware datetime có `tzinfo` phù hợp. môi trường vận hành (production / 운영 환경) sự kiện (event / 이벤트) timestamp thường nên lưu/trao đổi ở UTC và convert cho display/nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙) ở timezone cần thiết.

```python
from datetime import datetime, timezone
now_utc = datetime.now(timezone.utc)
```

Đừng tự cộng `timedelta(hours=9)` để “tạo Korea thời gian (time / 시간)” cho lô-gic (logic / 논리) tổng quát. Timezone có historical quy tắc (rule / 규칙)/DST ở nhiều khu vực; dùng `zoneinfo.ZoneInfo` với IANA timezone khi cần cục bộ (local / 로컬) civil thời gian (time / 시간).

```python
from zoneinfo import ZoneInfo
seoul = now_utc.astimezone(ZoneInfo("Asia/Seoul"))
```

Một cục bộ (local / 로컬) civil thời gian (time / 시간) có thể ambiguous hoặc thậm chí không tồn tại tại DST chuyển tiếp (transition / 전이) ở một số zone. Vì vậy “2026-11-01 01:30 cục bộ (local / 로컬)” và “một instant tuyệt đối” là hai loại dữ liệu khác nhau. Nếu lĩnh vực (domain / 도메인) cần lịch hẹn theo cục bộ (local / 로컬) rules, giữ timezone ngữ nghĩa (semantics / 의미론); nếu lĩnh vực (domain / 도메인) cần sự kiện (event / 이벤트) thứ tự (ordering / 순서), UTC instant thường phù hợp hơn.

Duration đo lường (measurement / 측정) cho hết thời gian chờ (timeout / 타임아웃)/hiệu năng (performance / 성능) nên dùng monotonic clock như `time.monotonic()`/`perf_counter()` thay vì wall clock có thể được chỉnh.

> **Chuyển mạch:** Datetime/timezone làm rõ dữ liệu thời gian và ambiguity; regex tiếp theo xử lý text boundary nhưng có thể thành parser debt. Logging sau đó ghi lại failure và context thay vì chỉ in chuỗi.

## 15. Regex: parser nhỏ nhưng dễ trở thành debt

`biểu thức chính quy (regular expression / 정규 표현식)`

Regex phù hợp cho lexical mẫu (pattern / 패턴) tương đối cục bộ. Raw string `r"..."` giảm escaping giữa Python string cú pháp (syntax / 문법) và regex cú pháp (syntax / 문법).

```python
import re
USER_ID = re.compile(r'"user_id"\s*:\s*"([^"]+)"')
```

Nếu đầu vào (input / 입력) thật sự là JSON, hãy parse JSON thay vì regex. Regex trên structured format thường thất bại khi whitespace, escaping, nesting hoặc thứ tự (ordering / 순서) thay đổi. cấp cao (senior / 시니어) ghi chú (note / 노트): dùng công cụ (tool / 도구) khớp với grammar của dữ liệu.

Catastrophic backtracking có thể thành hiệu năng (performance / 성능)/bảo mật (security / 보안) rủi ro (risk / 위험) khi regex nhận untrusted đầu vào (input / 입력). Hạn chế mẫu (pattern / 패턴) mơ hồ, kiểm thử (test / 테스트) worst trường hợp (case / 사례) và cân nhắc parser khác nếu độ phức tạp (complexity / 복잡도) tăng.

> **Chuyển mạch:** Regex tạo ra các failure cần context khi parse input; logging làm context đó có thể truy nguyên. CLI/argparse tiếp theo đưa validation và exit behavior ra boundary của chương trình.

## 16. Logging: sự kiện (event / 이벤트) có ngữ cảnh (context / 맥락), không phải `print` nâng cấp

`ghi nhật ký (logging / 로깅)`

Logging môi trường vận hành (production / 운영 환경) cần mức (level / 수준), timestamp, logger name và ngữ cảnh (context / 맥락) đủ để reconstruct sự kiện (event / 이벤트). thư viện (library / 라이브러리) mã (code / 코드) thường không cấu hình toàn cục (global / 전역) handler; ứng dụng (application / 애플리케이션) entry điểm (point / 지점) sở hữu logging cấu hình (configuration / 구성).

```python
import logging
logger = logging.getLogger(__name__)

logger.info("job_completed", extra={"job_id": job_id})
```

Không log secrets, truy cập (access / 접근) đơn vị từ (token / 토큰), password, full personal dữ liệu (data / 데이터) hoặc yêu cầu (request / 요청) body bừa bãi. Structured logging giúp tìm kiếm (search / 검색)/aggregation nhưng lược đồ (schema / 스키마) của log cũng cần ổn định.

Dùng lazy formatting của logging khi có thể:

```python
logger.debug("loaded %d records", count)
```

thay vì luôn bản dựng (build / 빌드) expensive f-string trước khi logger biết mức (level / 수준) có enabled hay không.

Một log bản ghi (record / 레코드) hữu ích nên mang ngữ nghĩa (semantic / 의미적) ngữ cảnh (context / 맥락) chứ không chỉ dump đối tượng (object / 객체). `repr` và log có thể vô tình kéo secret từ nested đối tượng (object / 객체) vào đầu ra (output / 출력); redaction phải dựa trên dữ liệu (data / 데이터) classification chứ không chỉ string replace ở cuối chuỗi xử lý (pipeline / 파이프라인).

> **Chuyển mạch:** CLI biến validation và logging thành interface người dùng; subprocess mở rộng boundary đó sang process, environment và security. Vì vậy input contract phải được giữ qua cả hai lớp.

## 17. CLI và `argparse`

CLI là công khai (public / 공개) giao diện (interface / 인터페이스) cho người dùng/script khác. `argparse` đủ cho nhiều standard-library công cụ (tool / 도구).

```python
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()
```

Exit mã (code / 코드), stdout/stderr, stable option names và help văn bản (text / 텍스트) là Đặc tả API (API contract / API 계약). Không trộn lô-gic nghiệp vụ (business logic / 비즈니스 로직) vào parser; parse đầu vào (input / 입력) → validate/configure → gọi ứng dụng (application / 애플리케이션) hàm (function / 함수) → map kết quả (result / 결과)/exception thành đầu ra (output / 출력)/exit mã (code / 코드).

CLI dùng trong automation còn có machine-consumer. Nếu stdout được parse bởi script khác, format đầu ra (output / 출력) là tính tương thích (compatibility / 호환성) đặc tả hợp đồng (contract / 계약); diagnostic nên đi stderr để không phá dữ liệu (data / 데이터) stream.

> **Chuyển mạch:** **17. CLI và argparse** tách đầu vào khỏi lô-gic ứng dụng; sang **18. subprocess**, ta hỏi thêm dữ liệu ấy đi qua ranh giới tiến trình và quyền hạn như thế nào. Mục 19 sẽ đặt hai nguyên tắc đó vào một case study nhỏ về boundary an toàn.

## 18. `subprocess`: tiến trình (process / 프로세스) ranh giới (boundary / 경계) và bảo mật (security / 보안)

`tiến trình con (subprocess / 하위 프로세스)`

`subprocess.run()` tạo/đợi tiến trình (process / 프로세스) với điều khiển (control / 제어) rõ hơn `os.system`.

```python
import subprocess

result = subprocess.run(
    ["git", "status", "--short"],
    text=True,
    capture_output=True,
    check=True,
)
```

Truyền argument danh sách (list / 목록) và mặc định `shell=False` tránh một lớp shell injection. Nếu bắt buộc dùng shell cú pháp (syntax / 문법), treat untrusted đầu vào (input / 입력) đặc biệt cẩn trọng. `check=True` biến non-zero exit thành exception, giúp thất bại (failure / 실패) không bị bỏ qua.

Hết thời gian chờ (timeout / 타임아웃), đầu ra (output / 출력) kích thước (size / 크기) và child-process cleanup là môi trường vận hành (production / 운영 환경) concerns. Một command treo hoặc in gigabyte đầu ra (output / 출력) có thể làm dịch vụ (service / 서비스) chết dù cú pháp (syntax / 문법) đúng. `capture_output=True` giữ đầu ra (output / 출력) trong bộ nhớ (memory / 메모리), vì vậy command có đầu ra (output / 출력) không bounded cần streaming/tệp (file / 파일) redirect hoặc tường minh (explicit / 명시적) kích thước (size / 크기) chiến lược (strategy / 전략).

Hết thời gian chờ (timeout / 타임아웃) của một child tiến trình (process / 프로세스) cũng không tự định nghĩa vòng đời (lifecycle / 생명주기) cho toàn tiến trình (process / 프로세스) cây (tree / 트리). Child có thể tạo descendants, daemon hoặc bên ngoài (external / 외부) side tác động (effect / 효과) không biến mất chỉ vì parent wrapper raise `TimeoutExpired`. Khi cần hard isolation/cancellation, tiến trình (process / 프로세스) group/bộ chứa (container / 컨테이너)/job runner ngữ nghĩa (semantics / 의미론) phải được thiết kế ở OS/triển khai (deployment / 배포) tầng (layer / 계층).

> **Chuyển mạch:** Biết cách gọi subprocess chưa đủ; cần nhìn cả timeout, kích thước output, cleanup và cách kiểm thử. Mục **19. Case study: subprocess và boundary an toàn** làm rõ các điểm đó, rồi mục 20 nối kết luận sang các câu hỏi dự án của Part 3.

## 19. Case study: subprocess và boundary an toàn

Một case study được viết riêng cho mục này có thể kết hợp `dataclass`, `Path`, `subprocess`, regex, JSON, biến môi trường và HTTP I/O. Hãy đọc nó bằng mô hình tư duy của Part này:

`Usage` là data-oriented trạng thái (state / 상태) phù hợp với `dataclass`; `Path` tạo filesystem ranh giới (boundary / 경계) rõ; `subprocess.run([...])` dùng argument danh sách (list / 목록); `clean()`/`split_parts()` dùng regex cho văn bản (text / 텍스트) transformation; `json.loads` parse structured phản hồi (response / 응답); exception được raise khi bên ngoài (external / 외부) thao tác (operation / 연산) vi phạm bất biến (invariant / 불변식).

Điểm cần phân biệt: HTTP máy khách (client / 클라이언트) `httpx` là third-party phụ thuộc (dependency / 의존성) nên kiến thức sâu về máy khách (client / 클라이언트)/khung phần mềm (framework / 프레임워크) không thuộc Python cốt lõi (core / 핵심). cốt lõi (core / 핵심) thư viện (library / 라이브러리) chỉ cần giải thích ngữ cảnh (context / 맥락) manager, exception, I/O và typing đủ để hiểu cách Python orchestrate nó.

Khi rà soát (review / 검토) tệp (file / 파일) này, hãy để ý thêm hidden contracts vừa học: collection nào bị mutate hay snapshot; iterator nào single-pass; subprocess đầu ra (output / 출력) có bounded không; JSON parse xong đã domain-validate chưa; exception nào được translate và exception nào nên propagate; annotation đang là static đặc tả hợp đồng (contract / 계약) hay thời gian chạy (runtime / 런타임) bằng chứng (evidence / 증거).

> **Chuyển mạch:** Case study đã cho thấy dữ liệu, tiến trình và lỗi gặp nhau ở cùng một boundary. Sang **20. Cầu nối tới Part 3**, ta mở rộng câu hỏi: khi có nhiều dependency, test suite và I/O đồng thời, làm sao giữ được khả năng tái lập? Phần Nguồn chính sẽ đối chiếu câu trả lời với tài liệu gốc.

## 20. cầu nối (bridge / 브리지) sang Part 3

Khi mã (code / 코드) bắt đầu có phụ thuộc (dependency / 의존성) ngoài, nhiều worker, bộ kiểm thử (test suite / 테스트 스위트), gói (package / 패키지) install, concurrent I/O, CPU công việc (work / 작업) hoặc triển khai (deployment / 배포), câu hỏi đổi từ “đối tượng (object / 객체) này hoạt động thế nào?” sang “dự án (project / 프로젝트) này tái lập, kiểm thử (test / 테스트), profile, chạy đồng thời và vận hành ra sao?”. Đó là ranh giới (boundary / 경계) của Part 3.

Trước khi sang Part 3, bạn nên tự giải thích được vì sao `property` là descriptor-based lookup chứ không phải magic cú pháp (syntax / 문법); vì sao `NotImplemented` khác `False`; vì sao mutate bộ chứa (container / 컨테이너) trong iteration nguy hiểm; vì sao generator và async generator có vòng đời (lifecycle / 생명주기) riêng; ngữ cảnh (context / 맥락) manager có thể suppress exception bằng đặc tả hợp đồng (contract / 계약) nào; vì sao `Any` khác `object`; vì sao mutable generic dẫn tới variance ràng buộc (constraint / 제약조건); `Self`/`TypeIs` đang hứa điều gì với checker; khi nào `memoryview` là view thay vì bản sao (copy / 복사); và vì sao một timestamp cục bộ (local / 로컬) không luôn ánh xạ đơn giản tới một instant.

> **Chuyển mạch:** Cầu nối sang Part 3 gom data model và standard library thành các concern về packaging, testing, concurrency và operations. **Nguồn chính** xác nhận behavior trước khi người học chuyển sang các failure mode cấp hệ thống.

## Nguồn chính

- mô hình dữ liệu (data model / 데이터 모델): https://docs.python.org/3.14/reference/datamodel.html
- `dataclasses`: https://docs.python.org/3.14/library/dataclasses.html
- `typing`: https://docs.python.org/3.14/library/typing.html
- `collections.abc`: https://docs.python.org/3.14/library/collections.abc.html
- Iterators: https://docs.python.org/3.14/library/stdtypes.html#iterator-types
- Async iteration: https://docs.python.org/3.14/reference/expressions.html#asynchronous-generator-iterator-methods
- `contextlib`: https://docs.python.org/3.14/library/contextlib.html
- Exceptions and `ExceptionGroup`: https://docs.python.org/3.14/library/exceptions.html
- `pathlib`: https://docs.python.org/3.14/library/pathlib.html
- `memoryview`: https://docs.python.org/3.14/library/stdtypes.html#memoryview
- Buffer giao thức (protocol / 프로토콜): https://docs.python.org/3.14/c-api/buffer.html
- `datetime`: https://docs.python.org/3.14/library/datetime.html
- `zoneinfo`: https://docs.python.org/3.14/library/zoneinfo.html
- `re`: https://docs.python.org/3.14/library/re.html
- `logging`: https://docs.python.org/3.14/library/logging.html
- `subprocess`: https://docs.python.org/3.14/library/subprocess.html
- Annotation best practices: https://docs.python.org/3.14/howto/annotations.html

> **Bàn giao:** Sau **Nguồn chính**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
