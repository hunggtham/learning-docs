# Python Part 1 — Beginner: thực thi (execution / 실행), mô hình đối tượng (object model / 객체 모델), dữ liệu và hàm

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Python Part 1 — Beginner: thực thi (execution / 실행), mô hình đối tượng (object model / 객체 모델), dữ liệu và hàm**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Từ mã nguồn (source code / 소스 코드) đến thực thi (execution / 실행)** gom dữ liệu hoặc nguồn để kiểm tra một nhận định cụ thể; sau đó sang **2. Biến không phải hộp: name binding và tham chiếu (reference / 참조) ngữ nghĩa (semantics / 의미론)** để xác định owner và đường quay lại nguồn chuẩn. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

> Baseline: Python 3.14.7. Kiểm chứng: 2026-09-22.

Python dễ bắt đầu vì cú pháp ngắn, nhưng chính sự ngắn gọn đó làm nhiều người hình thành mô hình tư duy (mental model / 사고 모델) sai: tưởng biến là một chiếc hộp chứa dữ liệu, tưởng `=` sao chép đối tượng (object / 객체), tưởng `is` và `==` gần giống nhau, hoặc tưởng truyền danh sách (list / 목록) vào hàm (function / 함수) là “pass by tham chiếu (reference / 참조)”. Part này xây mô hình tư duy (mental model / 사고 모델) trước, rồi mới đặt cú pháp (syntax / 문법) lên trên mô hình tư duy (mental model / 사고 모델) đó.

## 1. Từ mã nguồn (source code / 소스 코드) đến thực thi (execution / 실행)

`mã nguồn (source code / 소스 코드)`

`trình thông dịch (interpreter / 인터프리터)`

`đối tượng (object / 객체)`

Khi chạy `python app.py`, Python không xử lý tệp (file / 파일) như một danh sách câu lệnh hoàn toàn rời rạc. nguồn (source / 소스) được tokenize, parse thành cấu trúc cú pháp, compile thành mã (code / 코드) đối tượng (object / 객체)/bytecode phù hợp với hiện thực (implementation / 구현), sau đó thời gian chạy (runtime / 런타임) thực thi. Với CPython, bytecode chạy trên evaluation vòng lặp (loop / 루프) của CPython. Đây là lý do một lỗi cú pháp (syntax / 문법) có thể xảy ra trước khi một dòng cụ thể được “chạy”, còn một lỗi như `ZeroDivisionError` chỉ xuất hiện khi điều khiển (control / 제어) luồng (flow / 흐름) thực sự đi tới thao tác (operation / 연산) đó.

```python
print("before")
if False:
    1 / 0
print("after")
```

Đoạn trên parse hợp lệ. `1 / 0` không thực thi vì branch không được chọn nên không có `ZeroDivisionError`. Ngược lại, thiếu dấu `:` sau `if False` là lỗi cú pháp (syntax / 문법) và mô-đun (module / 모듈) không thể được compile bình thường.

Python mô-đun (module / 모듈) cũng là một đơn vị (unit / 단위) thực thi. Khi một mô-đun (module / 모듈) được import lần đầu trong một tiến trình (process / 프로세스), top-level mã (code / 코드) của mô-đun (module / 모듈) thường được thực thi để tạo không gian tên (namespace / 네임스페이스) của mô-đun (module / 모듈). Điều này có hệ quả môi trường vận hành (production / 운영 환경) rất lớn: không nên đặt mạng (network / 네트워크) lời gọi (call / 호출), truy vấn (query / 쿼리) cơ sở dữ liệu (database / 데이터베이스) hoặc thao tác filesystem nặng ở top mức (level / 수준) nếu không thật sự muốn chúng chạy trong thời điểm import. Import không chỉ là “bản sao (copy / 복사) hàm (function / 함수) vào tệp (file / 파일) hiện tại”; nó là một cơ chế tải (load / 로드), bộ nhớ đệm (cache / 캐시) và bind mô-đun (module / 모듈) đối tượng (object / 객체).

### `if __name__ == "__main__"`

Khi một tệp (file / 파일) được chạy như entry điểm (point / 지점), không gian tên (namespace / 네임스페이스) của nó có `__name__ == "__main__"`. Khi cùng tệp (file / 파일) được import, `__name__` là tên mô-đun (module / 모듈). Vì vậy mẫu (pattern / 패턴) sau tách definition khỏi hành động chạy chương trình:

```python
def main() -> None:
    print("run application")

if __name__ == "__main__":
    main()
```

Điểm quan trọng không phải thuộc lòng câu `if`; nó là ranh giới (boundary / 경계) giữa “mô-đun (module / 모듈) có thể tái sử dụng” và “entry điểm (point / 지점) có side tác động (effect / 효과)”.

> **Chuyển mạch:** Trong **Python Part 1 — Beginner: thực thi (execution / 실행), mô hình đối tượng (object model / 객체 모델), dữ liệu và hàm**, **1. Từ mã nguồn (source code / 소스 코드) đến thực thi (execution / 실행)** nêu điều cần giải thích; **2. Biến không phải hộp: name binding và tham chiếu (reference / 참조) ngữ nghĩa (semantics / 의미론)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **3. định danh (identity / 식별자), equality và hashability** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Biến không phải hộp: name binding và tham chiếu (reference / 참조) ngữ nghĩa (semantics / 의미론)

`ràng buộc tên (name binding / 이름 바인딩)`

`tham chiếu (reference / 참조)`

`định danh đối tượng (object identity / 객체 식별성)`

Trong Python, statement `x = value` bind tên `x` tới một đối tượng (object / 객체). Cách nghĩ hữu ích nhất là name → đối tượng (object / 객체), không phải name chứa đối tượng (object / 객체).

```python
a = [10, 20]
b = a
b.append(30)
print(a)  # [10, 20, 30]
```

Không có danh sách (list / 목록) thứ hai được tạo tại `b = a`. Cả `a` và `b` đều bind tới cùng danh sách (list / 목록) đối tượng (object / 객체). `append()` mutate đối tượng (object / 객체) đó, nên quan sát qua tên nào cũng thấy trạng thái (state / 상태) mới.

Cơ chế này giải thích cách Python truyền argument. Python không cần chọn giữa slogan “pass by giá trị (value / 값)” và “pass by tham chiếu (reference / 참조)” theo nghĩa của C/C++. hàm (function / 함수) nhận một binding mới tới cùng đối tượng (object / 객체) đã được evaluate ở caller; đôi khi cách mô tả này được gọi là lời gọi (call / 호출) by sharing.

```python
def change(xs: list[int]) -> None:
    xs.append(3)      # mutate object caller đang cùng tham chiếu
    xs = [99]         # chỉ rebind local name xs sang object khác

values = [1, 2]
change(values)
print(values)         # [1, 2, 3]
```

`append()` thay trạng thái (state / 상태) của danh sách (list / 목록) chung. Dòng `xs = [99]` không làm caller variable `values` trỏ sang danh sách (list / 목록) mới vì nó chỉ thay cục bộ (local / 로컬) binding.

Cấp cao (senior / 시니어) lập luận (reasoning / 추론) ở đây là phân biệt ba thao tác: tạo đối tượng (object / 객체), bind/rebind name và mutate đối tượng (object / 객체). Rất nhiều bug Python là do trộn ba thao tác này thành một ý niệm mơ hồ là “thay biến”.

### Quyền sở hữu (ownership / 소유권): ai được quyền mutate đối tượng (object / 객체)?

Tham chiếu (reference / 참조) ngữ nghĩa (semantics / 의미론) chỉ mô tả cơ chế; API thiết kế (design / 설계) phải nói rõ quyền sở hữu trạng thái (state ownership / 상태 소유권). Hai hàm (function / 함수) sau có đặc tả hợp đồng (contract / 계약) rất khác dù cùng nhận `list`:

```python
def normalize_in_place(names: list[str]) -> None:
    for i, name in enumerate(names):
        names[i] = name.strip().lower()

def normalized(names: list[str]) -> list[str]:
    return [name.strip().lower() for name in names]
```

Hàm (function / 함수) đầu mutate đối tượng (object / 객체) của caller và tên hàm (function / 함수) nói rõ điều đó. hàm (function / 함수) thứ hai tạo danh sách (list / 목록) kết quả mới. Không có lựa chọn nào luôn tốt hơn; điều quan trọng là caller có dự đoán được side tác động (effect / 효과) hay không. Ở môi trường vận hành (production / 운영 환경), bug thường không đến từ việc Python “share tham chiếu (reference / 참조)”, mà từ việc quyền sở hữu (ownership / 소유권) không được định nghĩa nên hai thành phần (component / 컴포넌트) cùng nghĩ mình có quyền sửa cùng một đối tượng (object / 객체) đồ thị (graph / 그래프).

> **Chuyển mạch:** Name binding và reference semantics giải thích vì sao identity, equality và hashability không phải cùng một câu hỏi. Phần kế tiếp dùng distinction đó để phân tích mutable và immutable trong các phép gán thật.

## 3. định danh (identity / 식별자), equality và hashability

`đồng nhất đối tượng (identity / 동일성)`

`bằng nhau về giá trị (equality / 동등성)`

`khả năng băm (hashability / 해시 가능성)`

Mỗi đối tượng (object / 객체) có định danh (identity / 식별자), kiểu (type / 타입) và giá trị (value / 값). `is` kiểm tra hai expression có trả về cùng đối tượng (object / 객체) hay không. `==` gọi lô-gic (logic / 논리) equality của kiểu (type / 타입) để hỏi hai giá trị (value / 값) có được coi là bằng nhau hay không.

```python
x = [1, 2]
y = [1, 2]
z = x

print(x == y)  # True: cùng nội dung
print(x is y)  # False: hai list object
print(x is z)  # True: cùng object
```

Đừng dùng `is` để so sánh số hoặc chuỗi chỉ vì đôi lúc kiểm thử (test / 테스트) thấy đúng. CPython có thể reuse/intern một số đối tượng (object / 객체), nhưng đó không phải đặc tả hợp đồng (contract / 계약) để viết lô-gic nghiệp vụ (business logic / 비즈니스 로직). Trường hợp chuẩn gốc (canonical / 정본) của `is` là singleton như `None`:

```python
if result is None:
    ...
```

Hashability liên quan nhưng không đồng nhất với immutability. Key của `dict` và member của `set` cần băm (hash / 해시) ổn định trong thời gian đối tượng (object / 객체) nằm trong collection. Các immutable built-in như `str`, `bytes`, `int` thường hashable. `list`, `dict`, `set` mutable nên không hashable. `tuple` chỉ hashable nếu mọi phần tử cần băm (hash / 해시) cũng hashable.

> **Chuyển mạch:** Sau khi tách identity, equality và hashability, phần mutable/immutable cho thấy thao tác nào làm đổi object và thao tác nào chỉ đổi binding. Numeric types tiếp theo áp dụng cùng mental model cho value và phép tính.

## 4. Mutable và immutable: điều gì thực sự thay đổi?

`khả biến (mutable / 가변)`

`bất biến (immutable / 불변)`

Mutable đối tượng (object / 객체) cho phép trạng thái (state / 상태) quan sát được thay đổi mà định danh (identity / 식별자) vẫn giữ nguyên. Immutable đối tượng (object / 객체) không cho phép thay đổi giá trị (value / 값) của chính đối tượng (object / 객체) sau khi tạo; một thao tác (operation / 연산) “thay đổi” thường tạo đối tượng (object / 객체) mới.

```python
name = "py"
old_id = id(name)
name += "thon"
print(name)            # python
print(id(name) == old_id)  # không nên dựa vào kết quả; binding có thể trỏ object mới
```

Với danh sách (list / 목록):

```python
items = [1, 2]
before = id(items)
items += [3]
assert id(items) == before
```

`list.__iadd__` mutate danh sách (list / 목록), trong khi hành vi (behavior / 동작) của `+=` phụ thuộc kiểu (type / 타입). Vì vậy không thể hiểu augmented assignment chỉ bằng ký hiệu bề mặt.

Một pitfall sâu hơn xảy ra khi immutable bộ chứa (container / 컨테이너) chứa mutable đối tượng (object / 객체):

```python
box = ([1, 2], "fixed")
box[0].append(3)
```

`tuple` vẫn không cho thay `box[0]` bằng đối tượng (object / 객체) khác, nhưng danh sách (list / 목록) nằm bên trong vẫn mutable. “Tuple immutable” không có nghĩa toàn bộ đối tượng (object / 객체) đồ thị (graph / 그래프) bên dưới bất biến.

> **Chuyển mạch:** Numeric types cho thấy value model và phép toán có thể tạo object mới thay vì mutate object cũ. String/bytes tiếp theo chuyển cùng câu hỏi đó sang encoding boundary giữa text và binary.

## 5. Numeric types và mô hình (model / 모델) của số

Python có `int`, `float`, `complex` trong built-in numeric tower phổ biến. `bool` là subclass của `int`, nhưng trong lĩnh vực (domain / 도메인) mô hình (model / 모델) nên coi boolean là giá trị lô-gic (logic / 논리) thay vì số 0/1 trừ khi API yêu cầu.

`int` của Python có arbitrary precision ở mức ngôn ngữ (language / 언어) hành vi (behavior / 동작) thực tế của CPython: nó không overflow ở 32/64 bit như thành phần nguyên thủy (primitive / 기본 요소) integer cố định trong nhiều ngôn ngữ, đổi lại số càng lớn càng tốn bộ nhớ (memory / 메모리) và CPU.

`float` thường theo nhị phân (binary / 이진) floating-point của nền tảng (platform / 플랫폼). Vì `0.1` không biểu diễn chính xác bằng finite nhị phân (binary / 이진) fraction, phép tính tiền không nên dựa vào equality trực tiếp của float.

```python
0.1 + 0.2 == 0.3  # False
```

Cho tiền tệ, dùng `decimal.Decimal` khi cần decimal arithmetic có kiểm soát. Cho scientific tolerance, cân nhắc `math.isclose()` theo lỗi (error / 오류) mô hình (model / 모델) của bài toán.

Floor division `//` không đơn thuần là “bỏ phần thập phân”; nó floor về phía âm vô cùng:

```python
-3 // 2  # -2
```

Đây là trường hợp biên (edge case / 경계 사례) dễ sai khi cổng (port / 포트) lô-gic (logic / 논리) từ ngôn ngữ dùng truncation toward zero.

> **Chuyển mạch:** Ở chặng này của **Python Part 1 — Beginner: thực thi (execution / 실행), mô hình đối tượng (object model / 객체 모델), dữ liệu và hàm**, **5. Numeric types và mô hình (model / 모델) của số** đã nêu tiêu chí phân biệt, còn **6. String, bytes và ranh giới (boundary / 경계) encoding** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **7. bộ chứa (container / 컨테이너) types: danh sách (list / 목록), tuple, dict, set** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. String, bytes và ranh giới (boundary / 경계) encoding

`văn bản Unicode (Unicode text / 유니코드 텍스트)`

`dãy byte (byte sequence / 바이트 시퀀스)`

`str` biểu diễn văn bản (text / 텍스트) Unicode ở mức lớp trừu tượng (abstraction / 추상화) của Python. `bytes` biểu diễn octet/nhị phân (binary / 이진) dữ liệu (data / 데이터). Encoding biến `str` thành `bytes`; decoding biến `bytes` thành `str` dựa trên một encoding như UTF-8.

```python
text = "안녕하세요"
payload = text.encode("utf-8")
restored = payload.decode("utf-8")
assert restored == text
```

Bug môi trường vận hành (production / 운영 환경) thường xuất hiện ở ranh giới (boundary / 경계): tệp (file / 파일), socket, cơ sở dữ liệu (database / 데이터베이스) driver, HTTP body, subprocess. Trong cốt lõi (core / 핵심) lô-gic (logic / 논리) hãy cố giữ văn bản (text / 텍스트) ở dạng `str`; encode/decode tại ranh giới (boundary / 경계) rõ ràng.

Python string immutable. Các thao tác nối nhiều chuỗi trong vòng lặp (loop / 루프) có thể tạo nhiều đối tượng (object / 객체) trung gian; khi ghép nhiều mảnh, `"".join(parts)` thể hiện intent và thường tốt hơn.

### f-string và t-string

F-string tạo `str` sau khi evaluate interpolation. Python 3.14 thêm template string literal `t"..."`, trả về `string.templatelib.Template` thay vì `str`, cho phép mã (code / 코드) xử lý phần literal và interpolation trước khi kết xuất (render / 렌더링). Đây là hiện đại (modern / 현대적) tính năng (feature / 기능) hữu ích cho API templating/security-aware processing, nhưng không cần dùng chỉ vì nó mới.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Python Part 1 — Beginner: thực thi (execution / 실행), mô hình đối tượng (object model / 객체 모델), dữ liệu và hàm**, **6. String, bytes và ranh giới (boundary / 경계) encoding** đã nêu tiêu chí phân biệt, còn **7. bộ chứa (container / 컨테이너) types: danh sách (list / 목록), tuple, dict, set** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **8. điều khiển (control / 제어) luồng (flow / 흐름) là điều khiển evaluation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. bộ chứa (container / 컨테이너) types: danh sách (list / 목록), tuple, dict, set

`danh sách (list / 리스트)`

`bộ (set / 집합)`

`ánh xạ (mapping / 매핑)`

Chọn bộ chứa (container / 컨테이너) theo thao tác (operation / 연산) chính, không theo thói quen.

`list` là ordered mutable chuỗi (sequence / 시퀀스), phù hợp khi cần giữ thứ tự và chỉ mục (index / 인덱스). `tuple` là fixed-shape immutable chuỗi (sequence / 시퀀스), thường dùng khi một group giá trị (value / 값) có ý nghĩa cấu trúc ổn định. `dict` ánh xạ key → giá trị (value / 값) và giữ insertion thứ tự (order / 순서) trong hiện đại (modern / 현대적) Python. `set` biểu diễn tập phần tử unique, phù hợp membership/deduplication.

```python
seen: set[str] = set()
for user_id in user_ids:
    if user_id in seen:
        continue
    seen.add(user_id)
    process(user_id)
```

Cấp cao (senior / 시니어) ghi chú (note / 노트): độ phức tạp (complexity / 복잡도) Big-O là starting điểm (point / 지점), không phải kết luận. `x in set` thường average O(1), nhưng bộ nhớ (memory / 메모리) overhead, băm (hash / 해시) chi phí (cost / 비용) và dữ liệu (data / 데이터) kích thước (size / 크기) thực tế cũng quan trọng. Với 5 phần tử, một danh sách (list / 목록) có thể đủ đơn giản; với hàng triệu key, cấu trúc dữ liệu và locality trở thành quyết định môi trường vận hành (production / 운영 환경).

### Slicing không đồng nghĩa “view miễn phí”

Với `list`, slicing thông thường tạo một danh sách (list / 목록) ngoài mới nhưng các phần tử bên trong vẫn là cùng đối tượng (object / 객체) references:

```python
rows = [[1], [2], [3]]
window = rows[0:2]
window[0].append(99)

print(rows)    # [[1, 99], [2], [3]]
print(window)  # [[1, 99], [2]]
```

Vì vậy `rows[:]` là một dạng shallow bản sao (copy / 복사) của danh sách (list / 목록), không phải deep bản sao (copy / 복사). Nó cũng có chi phí theo số tham chiếu (reference / 참조) được bản sao (copy / 복사); đừng coi slicing collection lớn là thao tác (operation / 연산) O(1). Một số API khác như `memoryview` thực sự cung cấp view lên nhị phân (binary / 이진) buffer, nhưng đó là giao thức (protocol / 프로토콜) khác. Khi hiệu năng (performance / 성능) hoặc quyền sở hữu (ownership / 소유권) quan trọng, cần biết thao tác (operation / 연산) đang tạo bản sao (copy / 복사) hay view thay vì suy luận từ cú pháp `[:]`.

### Shallow bản sao (copy / 복사) và deep bản sao (copy / 복사)

`bản sao nông (shallow copy / 얕은 복사)`

`bản sao sâu (deep copy / 깊은 복사)`

Shallow bản sao (copy / 복사) tạo bộ chứa (container / 컨테이너) ngoài mới nhưng giữ references tới đối tượng (object / 객체) con:

```python
original = [[1], [2]]
clone = original.copy()
clone[0].append(99)
print(original)  # [[1, 99], [2]]
```

`copy.deepcopy()` cố sao chép recursively đối tượng (object / 객체) đồ thị (graph / 그래프), nhưng “deep” không đồng nghĩa “luôn đúng”. đối tượng (object / 객체) có dùng chung (shared / 공유) định danh (identity / 식별자), tệp (file / 파일) handle, socket, khóa (lock / 잠금) hoặc custom `__deepcopy__` có ngữ nghĩa (semantics / 의미론) riêng. Trong lĩnh vực (domain / 도메인) mô hình (model / 모델), thường tốt hơn thiết kế immutable giá trị (value / 값) đối tượng (object / 객체) hoặc tường minh (explicit / 명시적) clone hành vi (behavior / 동작) thay vì dùng `deepcopy()` như phép chữa chung.

> **Chuyển mạch:** Trong **Python Part 1 — Beginner: thực thi (execution / 실행), mô hình đối tượng (object model / 객체 모델), dữ liệu và hàm**, **7. bộ chứa (container / 컨테이너) types: danh sách (list / 목록), tuple, dict, set** xác định đầu vào; **8. điều khiển (control / 제어) luồng (flow / 흐름) là điều khiển evaluation** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **9. Comprehension: transform có cấu trúc, không phải mọi vòng lặp (loop / 루프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. điều khiển (control / 제어) luồng (flow / 흐름) là điều khiển evaluation

`luồng điều khiển (control flow / 제어 흐름)`

`if`, `for`, `while`, `match`, `break`, `continue`, `return`, exception đều quyết định expression/statement nào được evaluate.

Python dùng truth-value testing. `None`, `False`, zero numeric, và empty bộ chứa (container / 컨테이너) thường falsy. Nhưng đừng gộp “không có giá trị” và “giá trị rỗng hợp lệ” nếu lĩnh vực (domain / 도메인) phân biệt chúng:

```python
# Sai nếu 0 là giá hợp lệ
if not price:
    ...

# Rõ intent nếu None nghĩa là chưa có giá
if price is None:
    ...
```

`for` của Python hoạt động qua iterable giao thức (protocol / 프로토콜), không phải chỉ qua chỉ mục (index / 인덱스). Phần iterator cơ chế (mechanism / 메커니즘) được đào sâu ở Part 2.

`match`/`case` từ Python 3.10 là structural mẫu (pattern / 패턴) matching. Nó mạnh khi dữ liệu có shape rõ, nhưng không nên biến lô-gic nghiệp vụ (business logic / 비즈니스 로직) đơn giản thành mẫu (pattern / 패턴) cây (tree / 트리) khó đọc.

### Short-circuit: expression có thể không được evaluate

`đánh giá đoản mạch (short-circuit evaluation / 단락 평가)` là cơ chế mà `and` hoặc `or` có thể dừng sớm khi kết quả lô-gic (logic / 논리) đã xác định. Điều quan trọng là Python trả về operand được chọn, không ép kết quả thành `bool`.

```python
name = user_input or "anonymous"

if user is not None and user.is_active:
    process(user)
```

Trong điều kiện thứ hai, `user.is_active` không được evaluate khi `user is None`. Đây là cách guard truy cập (access / 접근) rất tự nhiên. Nhưng side tác động (effect / 효과) nằm bên phải `and`/`or` có thể không chạy, nên không nên giấu thao tác (operation / 연산) quan trọng trong expression chỉ để mã (code / 코드) ngắn.

Python nhìn chung evaluate expression từ trái sang phải theo ngữ nghĩa (semantics / 의미론) được định nghĩa. Với hàm (function / 함수) lời gọi (call / 호출), các argument expression được evaluate trước khi hàm (function / 함수) body bắt đầu. Vì vậy:

```python
def log_value(value):
    print("inside")

def build_value():
    print("build")
    return 10

log_value(build_value())
```

sẽ in `build` trước `inside`. Phân biệt “evaluate argument” và “bind parameter” giúp lập luận (reasoning / 추론) đúng khi argument có I/O, mutation hoặc exception.

> **Chuyển mạch:** Ở chặng này của **Python Part 1 — Beginner: thực thi (execution / 실행), mô hình đối tượng (object model / 객체 모델), dữ liệu và hàm**, **8. điều khiển (control / 제어) luồng (flow / 흐름) là điều khiển evaluation** xác định đầu vào; **9. Comprehension: transform có cấu trúc, không phải mọi vòng lặp (loop / 루프)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **10. hàm (function / 함수) là đối tượng (object / 객체) và là ranh giới (boundary / 경계) thiết kế** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Comprehension: transform có cấu trúc, không phải mọi vòng lặp (loop / 루프)

Danh sách (list / 목록)/set/dict comprehensions kết hợp iteration, filtering và expression transform:

```python
active_names = [u.name for u in users if u.active]
```

Nó Pythonic khi toàn bộ transformation đọc được như một câu. Nếu có nhiều side tác động (effect / 효과), nhiều nested điều kiện (condition / 조건) hoặc cần logging/gỡ lỗi (debug / 디버그) từng bước, vòng lặp (loop / 루프) thường rõ hơn. “Pythonic” không có nghĩa càng ngắn càng tốt; nó nghĩa mã (code / 코드) phù hợp với ngữ nghĩa (semantic / 의미적) conventions của Python và dễ hiểu đối với người bảo trì.

Phạm vi (scope / 범위) của comprehension trong Python 3 là phạm vi (scope / 범위) riêng cho iteration variable, khác Python 2 legacy hành vi (behavior / 동작). mã (code / 코드) cũ hoặc tài liệu cũ có thể mô tả leakage của vòng lặp (loop / 루프) variable từ danh sách (list / 목록) comprehension; không áp dụng mô hình tư duy (mental model / 사고 모델) đó cho hiện đại (modern / 현대적) Python.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Python Part 1 — Beginner: thực thi (execution / 실행), mô hình đối tượng (object model / 객체 모델), dữ liệu và hàm**, **9. Comprehension: transform có cấu trúc, không phải mọi vòng lặp (loop / 루프)** đã nêu tiêu chí phân biệt, còn **10. hàm (function / 함수) là đối tượng (object / 객체) và là ranh giới (boundary / 경계) thiết kế** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **11. phạm vi (scope / 범위) và LEGB** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. hàm (function / 함수) là đối tượng (object / 객체) và là ranh giới (boundary / 경계) thiết kế

`hàm (function / 함수)`

`đối số (argument / 인자)`

`tham số (parameter / 매개변수)`

Hàm (function / 함수) definition tạo hàm (function / 함수) đối tượng (object / 객체) và bind nó vào name. Vì hàm (function / 함수) là đối tượng (object / 객체), nó có thể được truyền vào hàm (function / 함수) khác, lưu trong collection, trả về từ hàm (function / 함수) và đóng vai trò callback.

```python
def apply_twice(fn, value):
    return fn(fn(value))
```

### Argument binding

Python hỗ trợ positional-only (`/`), positional-or-keyword, keyword-only (`*`), variadic positional `*args` và variadic từ khóa (keyword / 키워드) `**kwargs`.

```python
def connect(host, /, port=5432, *, timeout=5.0):
    ...
```

Ở đây `host` buộc positional, còn `timeout` buộc từ khóa (keyword / 키워드). Đây không chỉ là cú pháp (syntax / 문법); nó giúp API giữ tính tương thích (compatibility / 호환성). Positional-only cho phép đổi parameter name mà không phá caller dùng từ khóa (keyword / 키워드), còn keyword-only làm lời gọi (call / 호출) site tự-documenting cho các option khó nhớ.

Một lời gọi (call / 호출) có thể được lập luận (reasoning / 추론) theo bốn bước khái niệm: evaluate argument expressions ở caller; expand `*iterable`/`**mapping`; bind các resulting arguments vào parameter theo signature; sau đó mới chạy hàm (function / 함수) body. Nếu thiếu argument, truyền duplicate từ khóa (keyword / 키워드) hoặc vi phạm positional-only/keyword-only đặc tả hợp đồng (contract / 계약), lỗi xảy ra ở binding ranh giới (boundary / 경계) trước khi body chạy.

Điều này giải thích vì sao side tác động (effect / 효과) của argument vẫn có thể xảy ra dù lời gọi (call / 호출) sau đó thất bại (fail / 실패) khi binding:

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

Unpacking thao tác trên iterable/ánh xạ (mapping / 매핑) giao thức (protocol / 프로토콜). Nó mạnh nhưng `**config` có thể che giấu nguồn parameter nếu cấu hình (config / 설정) được xây qua nhiều tầng (layer / 계층); trong mã (code / 코드) môi trường vận hành (production / 운영 환경), validate cấu hình (configuration / 구성) trước khi spread vào API.

Extended unpacking cũng là một allocation/thiết kế (design / 설계) quyết định (decision / 결정):

```python
first, *middle, last = records
```

`middle` là danh sách (list / 목록) mới chứa các phần tử ở giữa. Với iterable rất lớn, đừng dùng unpacking chỉ vì cú pháp đẹp nếu bạn thật sự cần streaming.

> **Chuyển mạch:** Trong **Python Part 1 — Beginner: thực thi (execution / 실행), mô hình đối tượng (object model / 객체 모델), dữ liệu và hàm**, **10. hàm (function / 함수) là đối tượng (object / 객체) và là ranh giới (boundary / 경계) thiết kế** đã nêu tiêu chí phân biệt, còn **11. phạm vi (scope / 범위) và LEGB** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **12. Closure và late binding** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. phạm vi (scope / 범위) và LEGB

`phạm vi (scope / 스코프)`

Tên được resolve theo các phạm vi (scope / 범위) phù hợp. Mnemonic LEGB là cục bộ (local / 로컬) → Enclosing → toàn cục (global / 전역) → Builtins, nhưng hãy hiểu đây là name resolution mô hình (model / 모델) chứ không phải bốn dictionary tùy ý giống hệt nhau.

```python
rate = 10

def outer():
    discount = 2
    def inner(price):
        return price * rate - discount
    return inner
```

`inner` tìm `price` ở cục bộ (local / 로컬), `discount` ở enclosing hàm (function / 함수) và `rate` ở mô-đun (module / 모듈) toàn cục (global / 전역).

`global` cho phép assignment nhắm module-level binding; `nonlocal` nhắm binding trong enclosing hàm (function / 함수) phạm vi (scope / 범위). Dùng chúng tiết kiệm vì mutable toàn cục (global / 전역) trạng thái (state / 상태) làm testing/tính đồng thời (concurrency / 동시성)/lập luận (reasoning / 추론) khó hơn.

> **Chuyển mạch:** LEGB xác định tên được resolve ở scope nào; closure giữ lại binding đó sau khi outer function kết thúc. Phần default mutable argument tiếp tục bằng một lỗi khác của evaluation timing.

## 12. Closure và late binding

`bao đóng (closure / 클로저)`

Closure giữ liên hệ với variables từ enclosing phạm vi (scope / 범위). Điểm dễ sai: closure thường capture binding/cell, không snapshot giá trị (value / 값) ở mỗi vòng vòng lặp (loop / 루프).

```python
funcs = []
for i in range(3):
    funcs.append(lambda: i)

print([f() for f in funcs])  # [2, 2, 2]
```

Khi lambda chạy sau vòng lặp (loop / 루프), cả ba lookup cùng thấy giá trị (value / 값) cuối của `i`. Một cách tường minh (explicit / 명시적) snapshot là default argument:

```python
funcs = [lambda i=i: i for i in range(3)]
```

Không nên học đây như mẹo “thêm `i=i`”. Cơ chế là default expression được evaluate lúc hàm (function / 함수) được tạo, trong khi free variable lookup của closure xảy ra khi hàm (function / 함수) chạy.

> **Chuyển mạch:** Closure và default argument đều buộc người học theo dõi thời điểm binding/evaluation, nhưng chúng giữ state theo cơ chế khác nhau. Exception cơ bản tiếp theo mở rộng mental model sang control-flow và failure boundary.

## 13. Default mutable argument: lỗi từ thời điểm evaluation

Default parameter được evaluate một lần khi `def` statement chạy, không phải mỗi lần hàm (function / 함수) được gọi.

```python
def add_item(item, bucket=[]):
    bucket.append(item)
    return bucket
```

Nhiều lời gọi (call / 호출) không truyền `bucket` sẽ cùng dùng danh sách (list / 목록) đối tượng (object / 객체) mặc định. mẫu (pattern / 패턴) an toàn khi cần collection mới mỗi lời gọi (call / 호출):

```python
def add_item(item: str, bucket: list[str] | None = None) -> list[str]:
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket
```

Có trường hợp dùng chung (shared / 공유) default trạng thái (state / 상태) là cố ý, nhưng nếu vậy nên biểu diễn intent rõ bằng đối tượng (object / 객체)/bộ nhớ đệm (cache / 캐시) riêng thay vì dựa vào side tác động (effect / 효과) khó thấy của default argument.

> **Chuyển mạch:** Trong **Python Part 1 — Beginner: thực thi (execution / 실행), mô hình đối tượng (object model / 객체 모델), dữ liệu và hàm**, **13. Default mutable argument: lỗi từ thời điểm evaluation** xác định đầu vào; **14. Exception cơ bản: lỗi là một control-flow đường dẫn (path / 경로)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **15. Modules, packages và import mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Exception cơ bản: lỗi là một control-flow đường dẫn (path / 경로)

`ngoại lệ (exception / 예외)`

`lan truyền ngoại lệ (exception propagation / 예외 전파)`

Khi raise exception, luồng bố cục thông thường (normal flow / 일반 흐름) dừng và thời gian chạy (runtime / 런타임) tìm handler phù hợp trên ngăn xếp lời gọi (call stack / 호출 스택). Nếu hiện tại (current / 현재) frame không handle, exception propagate lên caller. Vì vậy `try/except` không chỉ “bắt lỗi”; nó quyết định ranh giới (boundary / 경계) nào đủ ngữ cảnh (context / 맥락) để xử lý.

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

`raise ... from exc` giữ chuỗi nhân quả (causal chain / 인과 사슬). Anti-pattern là `except Exception: pass` vì nó xóa thất bại (failure / 실패) tín hiệu (signal / 신호) và làm hệ thống tiếp tục với trạng thái (state / 상태) không chắc chắn.

`finally` chạy để cleanup dù normal đường dẫn (path / 경로) hay exception đường dẫn (path / 경로). Tuy vậy tài nguyên (resource / 자원) management thường nên dùng ngữ cảnh (context / 맥락) manager, được giải thích ở Part 2.

### Giữ `try` nhỏ để không bắt nhầm bug của chính mình

Nếu `try` bao quá nhiều mã (code / 코드), handler có thể vô tình bắt exception phát sinh từ thao tác (operation / 연산) khác với thao tác (operation / 연산) bạn định recover. `else` giúp tách success đường dẫn (path / 경로) khỏi vùng đang được catch:

```python
try:
    port = int(raw)
except ValueError:
    return default_port
else:
    return validate_port(port)
```

Ở đây `ValueError` từ `validate_port()` không bị handler dành cho parsing nuốt mất. Đây là một ví dụ cho nguyên tắc rộng hơn: exception ranh giới (boundary / 경계) nên hẹp đủ để khôi phục (recovery / 복구) ngữ nghĩa (semantics / 의미론) rõ ràng.

> **Chuyển mạch:** Ở chặng này của **Python Part 1 — Beginner: thực thi (execution / 실행), mô hình đối tượng (object model / 객체 모델), dữ liệu và hàm**, **15. Modules, packages và import mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **14. Exception cơ bản: lỗi là một control-flow đường dẫn (path / 경로)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **16. Một mini trường hợp (case / 사례) study: cấu hình (config / 설정) loader** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Modules, packages và import mô hình tư duy (mental model / 사고 모델)

`mô-đun (module / 모듈)`

`gói (package / 패키지)`

Mô-đun (module / 모듈) thường là một Python nguồn (source / 소스) tệp (file / 파일) hoặc mô-đun (module / 모듈) đối tượng (object / 객체) tải (load / 로드) được. gói (package / 패키지) tổ chức mô-đun (module / 모듈) thành không gian tên (namespace / 네임스페이스)/gói (package / 패키지) hierarchy. `import x` về mặt khái niệm gồm tìm mô-đun (module / 모듈) theo import hệ thống (system / 시스템), tải (load / 로드)/execute nếu cần, bộ nhớ đệm (cache / 캐시) trong `sys.modules`, rồi bind name ở không gian tên (namespace / 네임스페이스) hiện tại.

Vì mô-đun (module / 모듈) bộ nhớ đệm (cache / 캐시) theo tiến trình (process / 프로세스), top-level mã (code / 코드) thường chỉ chạy lần đầu của normal import. `importlib.reload()` có ngữ nghĩa (semantics / 의미론) phức tạp và không phải cách chữa thông thường cho trạng thái (state / 상태) management.

### Circular import

Nếu `a.py` import `b.py`, trong khi `b.py` import ngược `a.py` và truy cập name chưa được tạo, bạn đang quan sát mô-đun (module / 모듈) ở trạng thái partially initialized. Fix bền vững thường là sửa phụ thuộc (dependency / 의존성) direction: tách dùng chung (shared / 공유) lớp trừu tượng (abstraction / 추상화) sang mô-đun (module / 모듈) thứ ba, chuyển orchestration lên tầng (layer / 계층) cao hơn, hoặc trì hoãn import có chủ đích. Di chuyển import vào hàm (function / 함수) chỉ để “hết lỗi” mà không sửa kiến trúc (architecture / 아키텍처) dễ che cycle.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Python Part 1 — Beginner: thực thi (execution / 실행), mô hình đối tượng (object model / 객체 모델), dữ liệu và hàm**, **15. Modules, packages và import mô hình tư duy (mental model / 사고 모델)** cho ta quy tắc; **16. Một mini trường hợp (case / 사례) study: cấu hình (config / 설정) loader** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **17. Checklist mô hình tư duy (mental model / 사고 모델) trước khi sang Part 2** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Một mini trường hợp (case / 사례) study: cấu hình (config / 설정) loader

```python
from pathlib import Path

def load_lines(path: Path, *, encoding: str = "utf-8") -> list[str]:
    if not path.is_file():
        raise FileNotFoundError(path)

    text = path.read_text(encoding=encoding)
    return [line.strip() for line in text.splitlines() if line.strip()]
```

Đoạn ngắn này dùng nhiều concept của Part 1. `path` là binding tới một `Path` đối tượng (object / 객체); `encoding` là keyword-only để lời gọi (call / 호출) site rõ; `read_text()` là I/O ranh giới (boundary / 경계) trả `str`; danh sách (list / 목록) comprehension phù hợp vì transformation đơn giản và không có side tác động (effect / 효과); thất bại (failure / 실패) `FileNotFoundError` được giữ nguyên vì caller có thể có ngữ cảnh (context / 맥락) tốt hơn để quyết định thử lại (retry / 재시도), báo người dùng (user / 사용자) hay thất bại (fail / 실패) tiến trình (process / 프로세스).

Nếu hàm (function / 함수) này nằm trong dịch vụ (service / 서비스), câu hỏi cấp cao (senior / 시니어) không phải “có thể viết một dòng không?” mà là: tệp (file / 파일) lớn đến mức nào, có cần streaming không, đầu vào (input / 입력) có tin cậy không, lỗi encoding xử lý ra sao, ai chịu trách nhiệm logging, và lời gọi (call / 호출) đường dẫn (path / 경로) có khối (block / 블록) vòng lặp sự kiện (event loop / 이벤트 루프) hay không. Các câu hỏi đó dẫn sang Part 2/3.

> **Chuyển mạch:** Trong **Python Part 1 — Beginner: thực thi (execution / 실행), mô hình đối tượng (object model / 객체 모델), dữ liệu và hàm**, **16. Một mini trường hợp (case / 사례) study: cấu hình (config / 설정) loader** cho ta quy tắc; **17. Checklist mô hình tư duy (mental model / 사고 모델) trước khi sang Part 2** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Nguồn chính** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Checklist mô hình tư duy (mental model / 사고 모델) trước khi sang Part 2

Hãy chắc rằng bạn có thể tự giải thích vì sao `b = a` không bản sao (copy / 복사) danh sách (list / 목록); vì sao `is` không thay `==`; vì sao tuple có thể chứa danh sách (list / 목록) mutable; vì sao slice của danh sách (list / 목록) là shallow outer bản sao (copy / 복사) chứ không phải view; vì sao short-circuit có thể làm expression bên phải không chạy; vì sao argument expression chạy trước parameter binding; vì sao default danh sách (list / 목록) có thể sống qua nhiều hàm (function / 함수) lời gọi (call / 호출); vì sao closure trong vòng lặp (loop / 루프) thấy giá trị (value / 값) cuối; vì sao `try` quá rộng có thể bắt nhầm bug; vì sao import có thể chạy mã (code / 코드); và vì sao `async` chưa thể kết luận gì về parallelism.

Phần cuối cùng mới chỉ là preview: `async` là cú pháp (syntax / 문법) tạo coroutine/asynchronous điều khiển (control / 제어) luồng (flow / 흐름); parallel thực thi (execution / 실행) là vấn đề khác, sẽ được tách rõ ở Part 3.

> **Chuyển mạch:** Checklist Part 1 gom execution, binding, object, function và exception thành các câu hỏi có thể kiểm tra. **Nguồn chính** ở cuối file giúp xác nhận từng behavior trước khi chuyển sang data model của Part 2.

## Nguồn chính

- Python ngôn ngữ (language / 언어) tham chiếu (reference / 참조) — mô hình dữ liệu (data model / 데이터 모델): https://docs.python.org/3.14/reference/datamodel.html
- Python ngôn ngữ (language / 언어) tham chiếu (reference / 참조) — mô hình thực thi (execution model / 실행 모델): https://docs.python.org/3.14/reference/executionmodel.html
- Python ngôn ngữ (language / 언어) tham chiếu (reference / 참조) — Expressions: https://docs.python.org/3.14/reference/expressions.html
- Python ngôn ngữ (language / 언어) tham chiếu (reference / 참조) — Simple statements: https://docs.python.org/3.14/reference/simple_stmts.html
- Python ngôn ngữ (language / 언어) tham chiếu (reference / 참조) — Import hệ thống (system / 시스템): https://docs.python.org/3.14/reference/import.html
- Built-in Types: https://docs.python.org/3.14/library/stdtypes.html
- Exceptions: https://docs.python.org/3.14/tutorial/errors.html
- Python 3.14 What's New: https://docs.python.org/3.14/whatsnew/3.14.html

> **Bàn giao:** Sau **Nguồn chính**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
