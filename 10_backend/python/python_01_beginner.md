# Python Part 1 — Beginner: Execution, object model, dữ liệu và hàm

> Baseline: Python 3.14.7. Kiểm chứng: 2026-09-22.

Python dễ bắt đầu vì cú pháp ngắn, nhưng chính sự ngắn gọn đó làm nhiều người hình thành mental model sai: tưởng biến là một chiếc hộp chứa dữ liệu, tưởng `=` sao chép object, tưởng `is` và `==` gần giống nhau, hoặc tưởng truyền list vào function là “pass by reference”. Part này xây mental model trước, rồi mới đặt syntax lên trên mental model đó.

## 1. Từ source code đến execution

`mã nguồn (source code / 소스 코드)`

`trình thông dịch (interpreter / 인터프리터)`

`đối tượng (object / 객체)`

Khi chạy `python app.py`, Python không xử lý file như một danh sách câu lệnh hoàn toàn rời rạc. Source được tokenize, parse thành cấu trúc cú pháp, compile thành code object/bytecode phù hợp với implementation, sau đó runtime thực thi. Với CPython, bytecode chạy trên evaluation loop của CPython. Đây là lý do một lỗi syntax có thể xảy ra trước khi một dòng cụ thể được “chạy”, còn một lỗi như `ZeroDivisionError` chỉ xuất hiện khi control flow thực sự đi tới operation đó.

```python
print("before")
if False:
    1 / 0
print("after")
```

Đoạn trên parse hợp lệ. `1 / 0` không thực thi vì branch không được chọn nên không có `ZeroDivisionError`. Ngược lại, thiếu dấu `:` sau `if False` là lỗi syntax và module không thể được compile bình thường.

Python module cũng là một unit thực thi. Khi một module được import lần đầu trong một process, top-level code của module thường được thực thi để tạo namespace của module. Điều này có hệ quả production rất lớn: không nên đặt network call, query database hoặc thao tác filesystem nặng ở top level nếu không thật sự muốn chúng chạy trong thời điểm import. Import không chỉ là “copy function vào file hiện tại”; nó là một cơ chế load, cache và bind module object.

### `if __name__ == "__main__"`

Khi một file được chạy như entry point, namespace của nó có `__name__ == "__main__"`. Khi cùng file được import, `__name__` là tên module. Vì vậy pattern sau tách definition khỏi hành động chạy chương trình:

```python
def main() -> None:
    print("run application")

if __name__ == "__main__":
    main()
```

Điểm quan trọng không phải thuộc lòng câu `if`; nó là boundary giữa “module có thể tái sử dụng” và “entry point có side effect”.

## 2. Biến không phải hộp: name binding và reference semantics

`ràng buộc tên (name binding / 이름 바인딩)`

`tham chiếu (reference / 참조)`

`định danh đối tượng (object identity / 객체 식별성)`

Trong Python, statement `x = value` bind tên `x` tới một object. Cách nghĩ hữu ích nhất là name → object, không phải name chứa object.

```python
a = [10, 20]
b = a
b.append(30)
print(a)  # [10, 20, 30]
```

Không có list thứ hai được tạo tại `b = a`. Cả `a` và `b` đều bind tới cùng list object. `append()` mutate object đó, nên quan sát qua tên nào cũng thấy state mới.

Cơ chế này giải thích cách Python truyền argument. Python không cần chọn giữa slogan “pass by value” và “pass by reference” theo nghĩa của C/C++. Function nhận một binding mới tới cùng object đã được evaluate ở caller; đôi khi cách mô tả này được gọi là call by sharing.

```python
def change(xs: list[int]) -> None:
    xs.append(3)      # mutate object caller đang cùng tham chiếu
    xs = [99]         # chỉ rebind local name xs sang object khác

values = [1, 2]
change(values)
print(values)         # [1, 2, 3]
```

`append()` thay state của list chung. Dòng `xs = [99]` không làm caller variable `values` trỏ sang list mới vì nó chỉ thay local binding.

Senior reasoning ở đây là phân biệt ba thao tác: tạo object, bind/rebind name và mutate object. Rất nhiều bug Python là do trộn ba thao tác này thành một ý niệm mơ hồ là “thay biến”.

### Ownership: ai được quyền mutate object?

Reference semantics chỉ mô tả cơ chế; API design phải nói rõ quyền sở hữu trạng thái (state ownership / 상태 소유권). Hai function sau có contract rất khác dù cùng nhận `list`:

```python
def normalize_in_place(names: list[str]) -> None:
    for i, name in enumerate(names):
        names[i] = name.strip().lower()


def normalized(names: list[str]) -> list[str]:
    return [name.strip().lower() for name in names]
```

Function đầu mutate object của caller và tên function nói rõ điều đó. Function thứ hai tạo list kết quả mới. Không có lựa chọn nào luôn tốt hơn; điều quan trọng là caller có dự đoán được side effect hay không. Ở production, bug thường không đến từ việc Python “share reference”, mà từ việc ownership không được định nghĩa nên hai component cùng nghĩ mình có quyền sửa cùng một object graph.

## 3. Identity, equality và hashability

`đồng nhất đối tượng (identity / 동일성)`

`bằng nhau về giá trị (equality / 동등성)`

`khả năng băm (hashability / 해시 가능성)`

Mỗi object có identity, type và value. `is` kiểm tra hai expression có trả về cùng object hay không. `==` gọi logic equality của type để hỏi hai value có được coi là bằng nhau hay không.

```python
x = [1, 2]
y = [1, 2]
z = x

print(x == y)  # True: cùng nội dung
print(x is y)  # False: hai list object
print(x is z)  # True: cùng object
```

Đừng dùng `is` để so sánh số hoặc chuỗi chỉ vì đôi lúc test thấy đúng. CPython có thể reuse/intern một số object, nhưng đó không phải contract để viết business logic. Trường hợp canonical của `is` là singleton như `None`:

```python
if result is None:
    ...
```

Hashability liên quan nhưng không đồng nhất với immutability. Key của `dict` và member của `set` cần hash ổn định trong thời gian object nằm trong collection. Các immutable built-in như `str`, `bytes`, `int` thường hashable. `list`, `dict`, `set` mutable nên không hashable. `tuple` chỉ hashable nếu mọi phần tử cần hash cũng hashable.

## 4. Mutable và immutable: điều gì thực sự thay đổi?

`khả biến (mutable / 가변)`

`bất biến (immutable / 불변)`

Mutable object cho phép state quan sát được thay đổi mà identity vẫn giữ nguyên. Immutable object không cho phép thay đổi value của chính object sau khi tạo; một operation “thay đổi” thường tạo object mới.

```python
name = "py"
old_id = id(name)
name += "thon"
print(name)            # python
print(id(name) == old_id)  # không nên dựa vào kết quả; binding có thể trỏ object mới
```

Với list:

```python
items = [1, 2]
before = id(items)
items += [3]
assert id(items) == before
```

`list.__iadd__` mutate list, trong khi behavior của `+=` phụ thuộc type. Vì vậy không thể hiểu augmented assignment chỉ bằng ký hiệu bề mặt.

Một pitfall sâu hơn xảy ra khi immutable container chứa mutable object:

```python
box = ([1, 2], "fixed")
box[0].append(3)
```

`tuple` vẫn không cho thay `box[0]` bằng object khác, nhưng list nằm bên trong vẫn mutable. “Tuple immutable” không có nghĩa toàn bộ object graph bên dưới bất biến.

## 5. Numeric types và model của số

Python có `int`, `float`, `complex` trong built-in numeric tower phổ biến. `bool` là subclass của `int`, nhưng trong domain model nên coi boolean là giá trị logic thay vì số 0/1 trừ khi API yêu cầu.

`int` của Python có arbitrary precision ở mức language behavior thực tế của CPython: nó không overflow ở 32/64 bit như primitive integer cố định trong nhiều ngôn ngữ, đổi lại số càng lớn càng tốn memory và CPU.

`float` thường theo binary floating-point của platform. Vì `0.1` không biểu diễn chính xác bằng finite binary fraction, phép tính tiền không nên dựa vào equality trực tiếp của float.

```python
0.1 + 0.2 == 0.3  # False
```

Cho tiền tệ, dùng `decimal.Decimal` khi cần decimal arithmetic có kiểm soát. Cho scientific tolerance, cân nhắc `math.isclose()` theo error model của bài toán.

Floor division `//` không đơn thuần là “bỏ phần thập phân”; nó floor về phía âm vô cùng:

```python
-3 // 2  # -2
```

Đây là edge case dễ sai khi port logic từ ngôn ngữ dùng truncation toward zero.

## 6. String, bytes và boundary encoding

`văn bản Unicode (Unicode text / 유니코드 텍스트)`

`dãy byte (byte sequence / 바이트 시퀀스)`

`str` biểu diễn text Unicode ở mức abstraction của Python. `bytes` biểu diễn octet/binary data. Encoding biến `str` thành `bytes`; decoding biến `bytes` thành `str` dựa trên một encoding như UTF-8.

```python
text = "안녕하세요"
payload = text.encode("utf-8")
restored = payload.decode("utf-8")
assert restored == text
```

Bug production thường xuất hiện ở boundary: file, socket, database driver, HTTP body, subprocess. Trong core logic hãy cố giữ text ở dạng `str`; encode/decode tại boundary rõ ràng.

Python string immutable. Các thao tác nối nhiều chuỗi trong loop có thể tạo nhiều object trung gian; khi ghép nhiều mảnh, `"".join(parts)` thể hiện intent và thường tốt hơn.

### f-string và t-string

F-string tạo `str` sau khi evaluate interpolation. Python 3.14 thêm template string literal `t"..."`, trả về `string.templatelib.Template` thay vì `str`, cho phép code xử lý phần literal và interpolation trước khi render. Đây là modern feature hữu ích cho API templating/security-aware processing, nhưng không cần dùng chỉ vì nó mới.

## 7. Container types: list, tuple, dict, set

`danh sách (list / 리스트)`

`bộ (set / 집합)`

`ánh xạ (mapping / 매핑)`

Chọn container theo operation chính, không theo thói quen.

`list` là ordered mutable sequence, phù hợp khi cần giữ thứ tự và index. `tuple` là fixed-shape immutable sequence, thường dùng khi một group value có ý nghĩa cấu trúc ổn định. `dict` ánh xạ key → value và giữ insertion order trong modern Python. `set` biểu diễn tập phần tử unique, phù hợp membership/deduplication.

```python
seen: set[str] = set()
for user_id in user_ids:
    if user_id in seen:
        continue
    seen.add(user_id)
    process(user_id)
```

Senior note: complexity Big-O là starting point, không phải kết luận. `x in set` thường average O(1), nhưng memory overhead, hash cost và data size thực tế cũng quan trọng. Với 5 phần tử, một list có thể đủ đơn giản; với hàng triệu key, cấu trúc dữ liệu và locality trở thành quyết định production.

### Slicing không đồng nghĩa “view miễn phí”

Với `list`, slicing thông thường tạo một list ngoài mới nhưng các phần tử bên trong vẫn là cùng object references:

```python
rows = [[1], [2], [3]]
window = rows[0:2]
window[0].append(99)

print(rows)    # [[1, 99], [2], [3]]
print(window)  # [[1, 99], [2]]
```

Vì vậy `rows[:]` là một dạng shallow copy của list, không phải deep copy. Nó cũng có chi phí theo số reference được copy; đừng coi slicing collection lớn là operation O(1). Một số API khác như `memoryview` thực sự cung cấp view lên binary buffer, nhưng đó là protocol khác. Khi performance hoặc ownership quan trọng, cần biết operation đang tạo copy hay view thay vì suy luận từ cú pháp `[:]`.

### Shallow copy và deep copy

`bản sao nông (shallow copy / 얕은 복사)`

`bản sao sâu (deep copy / 깊은 복사)`

Shallow copy tạo container ngoài mới nhưng giữ references tới object con:

```python
original = [[1], [2]]
clone = original.copy()
clone[0].append(99)
print(original)  # [[1, 99], [2]]
```

`copy.deepcopy()` cố sao chép recursively object graph, nhưng “deep” không đồng nghĩa “luôn đúng”. Object có shared identity, file handle, socket, lock hoặc custom `__deepcopy__` có semantics riêng. Trong domain model, thường tốt hơn thiết kế immutable value object hoặc explicit clone behavior thay vì dùng `deepcopy()` như phép chữa chung.

## 8. Control flow là điều khiển evaluation

`luồng điều khiển (control flow / 제어 흐름)`

`if`, `for`, `while`, `match`, `break`, `continue`, `return`, exception đều quyết định expression/statement nào được evaluate.

Python dùng truth-value testing. `None`, `False`, zero numeric, và empty container thường falsy. Nhưng đừng gộp “không có giá trị” và “giá trị rỗng hợp lệ” nếu domain phân biệt chúng:

```python
# Sai nếu 0 là giá hợp lệ
if not price:
    ...

# Rõ intent nếu None nghĩa là chưa có giá
if price is None:
    ...
```

`for` của Python hoạt động qua iterable protocol, không phải chỉ qua index. Phần iterator mechanism được đào sâu ở Part 2.

`match`/`case` từ Python 3.10 là structural pattern matching. Nó mạnh khi dữ liệu có shape rõ, nhưng không nên biến business logic đơn giản thành pattern tree khó đọc.

### Short-circuit: expression có thể không được evaluate

`đánh giá đoản mạch (short-circuit evaluation / 단락 평가)` là cơ chế mà `and` hoặc `or` có thể dừng sớm khi kết quả logic đã xác định. Điều quan trọng là Python trả về operand được chọn, không ép kết quả thành `bool`.

```python
name = user_input or "anonymous"

if user is not None and user.is_active:
    process(user)
```

Trong điều kiện thứ hai, `user.is_active` không được evaluate khi `user is None`. Đây là cách guard access rất tự nhiên. Nhưng side effect nằm bên phải `and`/`or` có thể không chạy, nên không nên giấu operation quan trọng trong expression chỉ để code ngắn.

Python nhìn chung evaluate expression từ trái sang phải theo semantics được định nghĩa. Với function call, các argument expression được evaluate trước khi function body bắt đầu. Vì vậy:

```python
def log_value(value):
    print("inside")


def build_value():
    print("build")
    return 10

log_value(build_value())
```

sẽ in `build` trước `inside`. Phân biệt “evaluate argument” và “bind parameter” giúp reasoning đúng khi argument có I/O, mutation hoặc exception.

## 9. Comprehension: transform có cấu trúc, không phải mọi loop

List/set/dict comprehensions kết hợp iteration, filtering và expression transform:

```python
active_names = [u.name for u in users if u.active]
```

Nó Pythonic khi toàn bộ transformation đọc được như một câu. Nếu có nhiều side effect, nhiều nested condition hoặc cần logging/debug từng bước, loop thường rõ hơn. “Pythonic” không có nghĩa càng ngắn càng tốt; nó nghĩa code phù hợp với semantic conventions của Python và dễ hiểu đối với người bảo trì.

Scope của comprehension trong Python 3 là scope riêng cho iteration variable, khác Python 2 legacy behavior. Code cũ hoặc tài liệu cũ có thể mô tả leakage của loop variable từ list comprehension; không áp dụng mental model đó cho modern Python.

## 10. Function là object và là boundary thiết kế

`hàm (function / 함수)`

`đối số (argument / 인자)`

`tham số (parameter / 매개변수)`

Function definition tạo function object và bind nó vào name. Vì function là object, nó có thể được truyền vào function khác, lưu trong collection, trả về từ function và đóng vai trò callback.

```python
def apply_twice(fn, value):
    return fn(fn(value))
```

### Argument binding

Python hỗ trợ positional-only (`/`), positional-or-keyword, keyword-only (`*`), variadic positional `*args` và variadic keyword `**kwargs`.

```python
def connect(host, /, port=5432, *, timeout=5.0):
    ...
```

Ở đây `host` buộc positional, còn `timeout` buộc keyword. Đây không chỉ là syntax; nó giúp API giữ compatibility. Positional-only cho phép đổi parameter name mà không phá caller dùng keyword, còn keyword-only làm call site tự-documenting cho các option khó nhớ.

Một call có thể được reasoning theo bốn bước khái niệm: evaluate argument expressions ở caller; expand `*iterable`/`**mapping`; bind các resulting arguments vào parameter theo signature; sau đó mới chạy function body. Nếu thiếu argument, truyền duplicate keyword hoặc vi phạm positional-only/keyword-only contract, lỗi xảy ra ở binding boundary trước khi body chạy.

Điều này giải thích vì sao side effect của argument vẫn có thể xảy ra dù call sau đó fail khi binding:

```python
def build_port() -> int:
    print("evaluated")
    return 5432


def connect(host, /, *, timeout):
    ...

# build_port() đã chạy, rồi call mới fail vì thiếu timeout.
connect(build_port())
```

### Packing và unpacking

```python
coords = (10, 20)
x, y = coords

options = {"timeout": 2.0, "retries": 3}
request(**options)
```

Unpacking thao tác trên iterable/mapping protocol. Nó mạnh nhưng `**config` có thể che giấu nguồn parameter nếu config được xây qua nhiều layer; trong code production, validate configuration trước khi spread vào API.

Extended unpacking cũng là một allocation/design decision:

```python
first, *middle, last = records
```

`middle` là list mới chứa các phần tử ở giữa. Với iterable rất lớn, đừng dùng unpacking chỉ vì cú pháp đẹp nếu bạn thật sự cần streaming.

## 11. Scope và LEGB

`phạm vi (scope / 스코프)`

Tên được resolve theo các scope phù hợp. Mnemonic LEGB là Local → Enclosing → Global → Builtins, nhưng hãy hiểu đây là name resolution model chứ không phải bốn dictionary tùy ý giống hệt nhau.

```python
rate = 10

def outer():
    discount = 2
    def inner(price):
        return price * rate - discount
    return inner
```

`inner` tìm `price` ở local, `discount` ở enclosing function và `rate` ở module global.

`global` cho phép assignment nhắm module-level binding; `nonlocal` nhắm binding trong enclosing function scope. Dùng chúng tiết kiệm vì mutable global state làm testing/concurrency/reasoning khó hơn.

## 12. Closure và late binding

`bao đóng (closure / 클로저)`

Closure giữ liên hệ với variables từ enclosing scope. Điểm dễ sai: closure thường capture binding/cell, không snapshot value ở mỗi vòng loop.

```python
funcs = []
for i in range(3):
    funcs.append(lambda: i)

print([f() for f in funcs])  # [2, 2, 2]
```

Khi lambda chạy sau loop, cả ba lookup cùng thấy value cuối của `i`. Một cách explicit snapshot là default argument:

```python
funcs = [lambda i=i: i for i in range(3)]
```

Không nên học đây như mẹo “thêm `i=i`”. Cơ chế là default expression được evaluate lúc function được tạo, trong khi free variable lookup của closure xảy ra khi function chạy.

## 13. Default mutable argument: lỗi từ thời điểm evaluation

Default parameter được evaluate một lần khi `def` statement chạy, không phải mỗi lần function được gọi.

```python
def add_item(item, bucket=[]):
    bucket.append(item)
    return bucket
```

Nhiều call không truyền `bucket` sẽ cùng dùng list object mặc định. Pattern an toàn khi cần collection mới mỗi call:

```python
def add_item(item: str, bucket: list[str] | None = None) -> list[str]:
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket
```

Có trường hợp shared default state là cố ý, nhưng nếu vậy nên biểu diễn intent rõ bằng object/cache riêng thay vì dựa vào side effect khó thấy của default argument.

## 14. Exception cơ bản: lỗi là một control-flow path

`ngoại lệ (exception / 예외)`

`lan truyền ngoại lệ (exception propagation / 예외 전파)`

Khi raise exception, normal flow dừng và runtime tìm handler phù hợp trên call stack. Nếu current frame không handle, exception propagate lên caller. Vì vậy `try/except` không chỉ “bắt lỗi”; nó quyết định boundary nào đủ context để xử lý.

```python
def parse_port(raw: str) -> int:
    try:
        port = int(raw)
    except ValueError as exc:
        raise ValueError(f"invalid port: {raw!r}") from exc
    if not 1 <= port <= 65535:
        raise ValueError("port outside 1..65535")
    return port
```

`raise ... from exc` giữ causal chain. Anti-pattern là `except Exception: pass` vì nó xóa failure signal và làm hệ thống tiếp tục với state không chắc chắn.

`finally` chạy để cleanup dù normal path hay exception path. Tuy vậy resource management thường nên dùng context manager, được giải thích ở Part 2.

### Giữ `try` nhỏ để không bắt nhầm bug của chính mình

Nếu `try` bao quá nhiều code, handler có thể vô tình bắt exception phát sinh từ operation khác với operation bạn định recover. `else` giúp tách success path khỏi vùng đang được catch:

```python
try:
    port = int(raw)
except ValueError:
    return default_port
else:
    return validate_port(port)
```

Ở đây `ValueError` từ `validate_port()` không bị handler dành cho parsing nuốt mất. Đây là một ví dụ cho nguyên tắc rộng hơn: exception boundary nên hẹp đủ để recovery semantics rõ ràng.

## 15. Modules, packages và import mental model

`mô-đun (module / 모듈)`

`gói (package / 패키지)`

Module thường là một Python source file hoặc module object load được. Package tổ chức module thành namespace/package hierarchy. `import x` về mặt khái niệm gồm tìm module theo import system, load/execute nếu cần, cache trong `sys.modules`, rồi bind name ở namespace hiện tại.

Vì module cache theo process, top-level code thường chỉ chạy lần đầu của normal import. `importlib.reload()` có semantics phức tạp và không phải cách chữa thông thường cho state management.

### Circular import

Nếu `a.py` import `b.py`, trong khi `b.py` import ngược `a.py` và truy cập name chưa được tạo, bạn đang quan sát module ở trạng thái partially initialized. Fix bền vững thường là sửa dependency direction: tách shared abstraction sang module thứ ba, chuyển orchestration lên layer cao hơn, hoặc trì hoãn import có chủ đích. Di chuyển import vào function chỉ để “hết lỗi” mà không sửa architecture dễ che cycle.

## 16. Một mini case study: config loader

```python
from pathlib import Path


def load_lines(path: Path, *, encoding: str = "utf-8") -> list[str]:
    if not path.is_file():
        raise FileNotFoundError(path)

    text = path.read_text(encoding=encoding)
    return [line.strip() for line in text.splitlines() if line.strip()]
```

Đoạn ngắn này dùng nhiều concept của Part 1. `path` là binding tới một `Path` object; `encoding` là keyword-only để call site rõ; `read_text()` là I/O boundary trả `str`; list comprehension phù hợp vì transformation đơn giản và không có side effect; failure `FileNotFoundError` được giữ nguyên vì caller có thể có context tốt hơn để quyết định retry, báo user hay fail process.

Nếu function này nằm trong service, câu hỏi senior không phải “có thể viết một dòng không?” mà là: file lớn đến mức nào, có cần streaming không, input có tin cậy không, lỗi encoding xử lý ra sao, ai chịu trách nhiệm logging, và call path có block event loop hay không. Các câu hỏi đó dẫn sang Part 2/3.

## 17. Checklist mental model trước khi sang Part 2

Hãy chắc rằng bạn có thể tự giải thích vì sao `b = a` không copy list; vì sao `is` không thay `==`; vì sao tuple có thể chứa list mutable; vì sao slice của list là shallow outer copy chứ không phải view; vì sao short-circuit có thể làm expression bên phải không chạy; vì sao argument expression chạy trước parameter binding; vì sao default list có thể sống qua nhiều function call; vì sao closure trong loop thấy value cuối; vì sao `try` quá rộng có thể bắt nhầm bug; vì sao import có thể chạy code; và vì sao `async` chưa thể kết luận gì về parallelism.

Phần cuối cùng mới chỉ là preview: `async` là syntax tạo coroutine/asynchronous control flow; parallel execution là vấn đề khác, sẽ được tách rõ ở Part 3.

## Nguồn chính

- Python Language Reference — Data Model: https://docs.python.org/3.14/reference/datamodel.html
- Python Language Reference — Execution model: https://docs.python.org/3.14/reference/executionmodel.html
- Python Language Reference — Expressions: https://docs.python.org/3.14/reference/expressions.html
- Python Language Reference — Simple statements: https://docs.python.org/3.14/reference/simple_stmts.html
- Python Language Reference — Import system: https://docs.python.org/3.14/reference/import.html
- Built-in Types: https://docs.python.org/3.14/library/stdtypes.html
- Exceptions: https://docs.python.org/3.14/tutorial/errors.html
- Python 3.14 What's New: https://docs.python.org/3.14/whatsnew/3.14.html