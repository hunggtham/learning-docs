# Chuyên đề 18: Lập trình Python, Cấu trúc Dữ liệu và Tự động hóa (Python 프로그래밍, 자료구조 및 시스템 자동화)

## 학습 목표 (Mục tiêu học tập)
- Nắm vững đặc tính ngôn ngữ kịch bản bậc cao của Python: Định kiểu động (Dynamic Typing), cú pháp dựa trên thụt lề (Indentation) và gán đồng thời (Multiple Assignment).
- Sử dụng thành thạo các hàm nhập xuất chuẩn `input()`, `print()` với tham số định dạng `sep` và `end`, cùng kỹ thuật ép kiểu và tách chuỗi kết hợp `map(int, input().split())`.
- Phân biệt bản chất bộ nhớ và tính khả biến (Mutability) của 4 cấu trúc dữ liệu cốt lõi: List, Tuple, Set, Dictionary; làm chủ kỹ thuật cắt lát (Slicing) với bước nhảy âm và đảo ngược chuỗi.
- Kiểm soát hoàn hảo luồng điều khiển chương trình với `if-elif-else`, vòng lặp `for-in` duyệt qua `range()`, vòng lặp `while` và cơ chế khối lệnh `else` trong vòng lặp.
- Hiểu thấu tư duy lập trình hướng đối tượng trong Python: Khai báo lớp (`class`), hàm khởi tạo (`__init__`), tham số đại diện cá thể (`self`), kế thừa (`super()`) và ghi đè phương thức (Method Overriding).
- Xây dựng hệ thống an toàn thông qua khối xử lý ngoại lệ `try - except - finally`, kết nối trực tiếp với các thư viện chuẩn quản trị hệ thống và tự động hóa vận hành máy chủ trong Môn 5.

## 핵심 키워드 (Từ khóa cốt lõi)
- **동적 타이핑 & 들여쓰기 (Dynamic Typing & Indentation)**: Tự suy luận kiểu lúc chạy, dùng khoảng trắng (4 spaces) và dấu `:` để định nghĩa khối lệnh.
- **표준 입출력 (Standard I/O)**: `input()` (luôn trả về `str`), `print(sep=' ', end='\n')`, mẫu đọc nhanh `list(map(int, input().split()))`.
- **4대 컬렉션 (Collections)**: List (`[]` - mutable), Tuple (`()` - immutable), Set (`{}` - unique), Dictionary (`{k: v}` - hash map).
- **슬라이싱 (Slicing)**: Cú pháp trích xuất mảng con `sequence[start:stop:step]`, chỉ số âm, đảo chuỗi `[::-1]`.
- **객체지향 프로그래밍 (Python OOP)**: `class`, `__init__` (hàm khởi tạo), `self` (tương đương `this`), `super()` (gọi lớp cha).
- **예외 처리 & 자원 해제 (Exception & Cleanup)**: `try - except - else - finally`, đảm bảo giải phóng socket và file descriptor.
- **시스템 자동화 (System Automation)**: Dùng script Python xử lý tệp log, tự động hóa quản trị hệ thống và kiểm tra an ninh mạng.

## 선행·연결 개념 (Kiến thức liên kết)
- **Đi từ đâu (선행 개념)**: Tiếp thu từ [17-lap-trinh-c-va-cau-truc-bo-nho.md](17-lap-trinh-c-va-cau-truc-bo-nho.md) (Đối chiếu giữa ngôn ngữ thủ tục cấp thấp C và ngôn ngữ kịch bản bậc cao Python).
- **Đang giải quyết điều gì (핵심 해결)**: Cung cấp công cụ lập trình hiện đại, linh hoạt giúp người quản trị hệ thống viết kịch bản tự động hóa giám sát tài nguyên, phân tích nhật ký (log parser) và phản ứng sự cố an ninh.
- **Dùng để đi đâu (연결 개념)**: Hoàn thiện toàn bộ chương trình Môn 5, trực tiếp hỗ trợ kỹ năng đọc hiểu mã nguồn trong cả phần thi lý thuyết trắc nghiệm (필기) và phần thi thực hành lập trình viết tay (실기) của kỳ thi Kỹ sư xử lý thông tin.

## 읽는 방법 (Cách đọc & Khung tư duy)
- **Quy tắc biên cắt lát (Half-open Interval)**: Trong biểu thức `arr[start:stop]`, phần tử tại chỉ số `start` được lấy nhưng phần tử tại `stop` luôn bị loại trừ ($[\text{start}, \text{stop})$). Khi `stop` bị bỏ trống, nó duyệt tới tận cùng của chuỗi.
- **Tính bất biến (Immutability)**: Tuple `()` và Khóa của Dictionary `{k: v}` là **bất biến**. Mọi thao tác gán sửa đổi (`t[0] = 5`) đều gây lỗi `TypeError`.
- **Khối `finally` thần thánh**: Dù trong khối `try` có xảy ra lỗi hay thực hiện lệnh `return` thì khối `finally` **bắt buộc luôn luôn được thực thi**.

---

### TẦNG A – ghi chú NÉN (ÔN / ĐI THI)

### 1. Cú pháp nền tảng, Nhập xuất và Ép kiểu

#### Khối lệnh và Gán đồng thời
- **Thụt lề (Indentation)**: Python không sử dụng dấu ngoặc nhọn `{}` hay từ khóa `begin/end`. Các khối lệnh được xác định duy nhất bằng mức thụt lề (chuẩn khuyến nghị là 4 khoảng trắng). Sau mỗi câu lệnh điều khiển bắt buộc có dấu hai chấm `:`.
- **Gán đồng thời (Multiple Assignment)**: Cho phép gán nhiều giá trị trong một câu lệnh và hoán đổi giá trị tức thì:
  ```python
  x, y = 10, 20
  x, y = y, x  # Hoán đổi giá trị tức thì mà không cần biến tạm temp!
  ```

#### Bảng hàm Nhập xuất và Tham số định dạng

| Hàm / Kỹ thuật | Cú pháp | Hành vi mặc định | Ví dụ tùy biến thi cử |
| :--- | :--- | :--- | :--- |
| **`input()`** | `val = input()` | Luôn trả về kiểu chuỗi văn bản (`str`), kể cả khi nhập số | `n = int(input())` (ép sang số nguyên) |
| **`print()`** | `print(a, b, ...)` | Xuất dữ liệu ra màn hình console | `print(a, b, sep='-')` (nối bằng gạch nối) |
| **Tham số `sep`** | `sep=' ký tự '` | Mặc định là một khoảng trắng (`' '`) | `print(1, 2, sep='')` $\rightarrow$ In ra `12` |
| **Tham số `end`** | `end=' ký tự '` | Mặc định là ký tự xuống dòng (`'\n'`) | `print(i, end=' ')` $\rightarrow$ In trên cùng dòng |
| **Đọc mảng 1 dòng** | `list(map(type, input().split()))` | Tách chuỗi theo dấu cách rồi ánh xạ ép kiểu | `a, b = map(int, input().split())` |

---

### 2. Bộ tứ Cấu trúc Dữ liệu Tập hợp (4대 컬렉션)

| Cấu trúc | Cú pháp | Thứ tự (Ordered) | Tính khả biến (Mutable) | Điểm đặc thù thi cử |
| :--- | :---: | :---: | :---: | :--- |
| **List (Danh sách)** | `[1, 2, 3]` | Có thứ tự ($0$-based) | **Có (Mutable)** | Cho phép trùng lặp, thêm phần tử bằng `append()`, `insert()`, xóa bằng `pop()`, `remove()` |
| **Tuple (Bộ giá trị)** | `(1, 2, 3)` | Có thứ tự ($0$-based) | **Không (Immutable)** | Kích thước cố định, an toàn dữ liệu, dùng làm Key trong Dict. Lưu ý Tuple 1 phần tử: `(5,)` |
| **Set (Tập hợp)** | `{1, 2, 3}` | Không thứ tự | **Có (Mutable)** | **Loại bỏ hoàn toàn phần tử trùng lặp**, hỗ trợ phép toán tập hợp: hợp `\|`, giao `&`, hiệu `-` |
| **Dictionary (Bảng băm)** | `{'a': 1}` | Có thứ tự (Python 3.7+) | **Có (Mutable)** | Lưu theo cặp `Key: Value`. **Khóa bắt buộc phải là kiểu bất biến** (`int`, `str`, `tuple`). Tra cứu $O(1)$ |

---

### 3. Kỹ thuật Cắt lát (Slicing) trên Chuỗi và Danh sách

Cú pháp chuẩn: `sequence[start : stop : step]`

| Biểu thức lát | Ý nghĩa chi tiết | Ví dụ với `s = "ABCDEF"` | Kết quả |
| :--- | :--- | :--- | :--- |
| `s[1:4]` | Lấy từ chỉ số 1 đến $4 - 1 = 3$ | `s[1]`, `s[2]`, `s[3]` | `"BCD"` |
| `s[:3]` | Lấy từ đầu đến chỉ số $3 - 1 = 2$ | `s[0]`, `s[1]`, `s[2]` | `"ABC"` |
| `s[2:]` | Lấy từ chỉ số 2 đến hết chuỗi | `s[2]` đến `s[5]` | `"CDEF"` |
| `s[::2]` | Duyệt từ đầu đến cuối với bước nhảy 2 | Bỏ qua phần tử xen kẽ | `"ACE"` |
| `s[::-1]` | **Đảo ngược toàn bộ chuỗi/mảng** | Duyệt từ cuối ngược về đầu | `"FEDCBA"` |
| `s[-3:]` | Chỉ số âm: 3 phần tử cuối cùng | Đếm từ cuối: $-3, -2, -1$ | `"DEF"` |

---

### 4. Cấu trúc Điều khiển và Lặp: `range()`, `for`, `while`

- **Cấu trúc rẽ nhánh `if-elif-else`**: Chú ý từ khóa là `elif` (viết tắt của else if trong C/Java).
- **Hàm sinh dãy số `range(start, stop, step)`**:
  - `range(5)` $\rightarrow 0, 1, 2, 3, 4$ (kết thúc tại $5 - 1 = 4$, gồm 5 phần tử).
  - `range(2, 6)` $\rightarrow 2, 3, 4, 5$.
  - `range(1, 10, 2)` $\rightarrow 1, 3, 5, 7, 9$ (bước nhảy 2).
  - `range(5, 0, -1)` $\rightarrow 5, 4, 3, 2, 1$ (đếm ngược, không bao gồm 0).
- **Khối `else` sau vòng lặp (`for - else`, `while - else`)**:
  - Khối `else` đi kèm vòng lặp sẽ **chỉ thực thi khi vòng lặp kết thúc bình thường** (điều kiện lặp thành `False`).
  - Nếu vòng lặp bị ngắt đột ngột bởi câu lệnh `break`, khối `else` sẽ **bị bỏ qua hoàn toàn**!

---

### 5. Hướng đối tượng (OOP) trong Python

```python
class Parent:
    def __init__(self, name):
        self.name = name  # Thuộc tính cá thể (Instance attribute)

    def greet(self):
        return f"Xin chào, tôi là {self.name}"

class Child(Parent):      # Kế thừa lớp Parent
    def __init__(self, name, age):
        super().__init__(name) # Gọi constructor của lớp cha
        self.age = age

    def greet(self):      # Ghi đè phương thức (Method Overriding)
        return f"Tôi là {self.name}, {self.age} tuổi"
```

- **`class TênLớp:`**: Định nghĩa một lớp mới.
- **`__init__(self, ...)`**: Phương thức khởi tạo (Constructor), tự động chạy khi một đối tượng được tạo (`obj = TênLớp()`).
- **Tham số `self`**: Luôn là tham số đầu tiên của mọi phương thức cá thể, đại diện cho chính thực thể đang gọi phương thức (tương đương con trỏ `this` trong C++/Java). Python tự động truyền đối số này ngầm định.
- **Kế thừa và `super()`**: Cú pháp `class Con(Cha):`. Hàm `super().__init__()` kích hoạt hàm dựng của lớp cha.

---

### 6. Xử lý Ngoại lệ (Exception Handling) và Giải phóng Tài nguyên

```python
try:
    # Khối lệnh có nguy cơ phát sinh lỗi ngoại lệ
    file = open("system_audit.log", "r")
    val = int(file.readline())
except FileNotFoundError:
    print("Lỗi: Không tìm thấy tệp nhật ký hệ thống!")
except ValueError:
    print("Lỗi: Dữ liệu không đúng định dạng số nguyên!")
except Exception as e:
    print(f"Lỗi không xác định: {e}")
else:
    # Chỉ chạy khi khối try THÀNH CÔNG mà không có bất kỳ ngoại lệ nào
    print("Đọc dữ liệu thành công:", val)
finally:
    # BẮT BUỘC LUÔN LUÔN CHẠY dù có lỗi hay không (Dọn dẹp tài nguyên)
    print("Hoàn tất tiến trình dọn dẹp bộ nhớ.")
```

---

### TẦNG B – ghi chú BỔ SUNG (HIỂU SÂU)

### 1. Phân tích Trace Code câu hỏi thi OOP và Vòng lặp

Hãy phân tích bài thi thực tế trích từ đề thi Kỹ sư xử lý thông tin:

```python
class Calculator:
    def __init__(self, val=0):
        self.val = val

    def add(self, n):
        self.val += n
        return self

    def sub(self, n):
        self.val -= n
        return self

c = Calculator(10)
res = c.add(5).sub(3).val
print(res)
```

**Phân tích cơ chế Method Chaining:**
1. Khởi tạo đối tượng `c = Calculator(10)` $\rightarrow$ Thuộc tính `c.val = 10`.
2. Gọi phương thức `c.add(5)`:
   - `self.val = 10 + 5 = 15`.
   - `return self`: Trả về chính thực thể đối tượng `c`.
3. Tiếp tục chuỗi phương thức `.sub(3)` trên đối tượng `c` vừa trả về:
   - `self.val = 15 - 3 = 12`.
   - `return self`: Trả về thực thể `c`.
4. Truy xuất thuộc tính `.val` cuối cùng $\rightarrow$ Nhận được giá trị `12`.
5. Kết quả in ra console: `12`.

---

### 2. Ứng dụng Python trong Quản trị Hệ thống và Tự động hóa Môn 5

Trong thực tế vận hành trung tâm dữ liệu và hệ thống thông tin, Python là ngôn ngữ kịch bản số một để tự động hóa:

```
[Các kịch bản tự động hóa Môn 5]
├── 1. Phân tích tệp nhật ký (Log Parser): Dùng Regex quét brute-force / SQL Injection
├── 2. Quét cổng & Dịch vụ mạng: Dùng module `socket` phát hiện cổng mở bất thường
├── 3. Giám sát tài nguyên máy chủ: Dùng `psutil` đo đạc CPU/RAM, cảnh báo ngưỡng
└── 4. Sao lưu dữ liệu & Đồng bộ đám mây: Dùng `shutil`, `os` tự động nén và backup
```

#### Ví dụ Kịch bản Tự động hóa: Quét IP vi phạm từ nhật ký máy chủ (Log Audit Script)

```python
# Kịch bản phát hiện tấn công dò quét cổng tự động
log_entries = [
    "2026-10-16 10:01:23 192.168.1.50 GET /admin 404",
    "2026-10-16 10:01:25 192.168.1.50 GET /wp-login.php 404",
    "2026-10-16 10:01:28 192.168.1.50 POST /login 401",
    "2026-10-16 10:02:00 10.0.0.12 GET /index.html 200"
]

failed_attempts = {}

for log in log_entries:
    parts = log.split()
    ip = parts[2]
    status_code = parts[-1]

    # Ghi nhận các truy vấn thất bại (mã 4xx)
    if status_code.startswith("4"):
        failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

# Kích hoạt tường lửa chặn IP nếu vi phạm từ 3 lần trở lên
for ip, count in failed_attempts.items():
    if count >= 3:
        print(f"[CẢNH BÁO AN NINH] Đã phát hiện tấn công từ IP: {ip} ({count} lần vi phạm). Đang chặn...")
```

> [!TIP] Bản chất kỹ thuật của Dictionary `.get(key, default)`
> Phương thức `.get(ip, 0)` trong Python giúp tránh hoàn toàn lỗi `KeyError` nếu khóa chưa từng tồn tại trong từ điển, là kỹ thuật lập trình phòng thủ (Defensive Programming) kinh điển trong xử lý dữ liệu lớn.

---

### 3. Phân biệt Bản chất Bộ nhớ: Shallow Copy vs Deep Copy

Khi quản trị cấu trúc dữ liệu mảng phức tạp, hiểu sai cơ chế sao chép trong Python có thể dẫn đến sai lệch dữ liệu hệ thống nghiêm trọng:

```python
import copy

a = [1, 2, [3, 4]]
b = a              # Phép gán: Cả 2 cùng trỏ vào 1 địa chỉ bộ nhớ (Reference)
c = a.copy()       # Shallow Copy: Sao chép lớp ngoài, lớp lồng nhau vẫn dùng chung địa chỉ
d = copy.deepcopy(a) # Deep Copy: Đệ quy cấp phát bộ nhớ mới hoàn toàn độc lập
```

```
[Minh họa bộ nhớ Shallow Copy vs Deep Copy]
─────────────────────────────────────────────────────────────────────────────
Vùng nhớ gốc:   a ───> [ 1 | 2 | con_trỏ ]
                                    │
                                    └───> [ 3 | 4 ] (Vùng nhớ con)
                                            ▲
Shallow copy:   c ───> [ 1 | 2 | con_trỏ ───┘  (Vẫn chia sẻ vùng nhớ con!)

Deep copy:      d ───> [ 1 | 2 | con_trỏ ]
                                    │
                                    └───> [ 3 | 4 ] (Vùng nhớ con hoàn toàn mới)
─────────────────────────────────────────────────────────────────────────────
```

- Nếu ta thực hiện `c[2][0] = 99`, giá trị của danh sách gốc `a` cũng bị biến đổi thành `[1, 2, [99, 4]]`!
- Với `d[2][0] = 77`, danh sách gốc `a` hoàn toàn không bị ảnh hưởng.

---

### 복습 체크리스트
- [ ] Tôi có thể giải thích tại sao hàm `input()` luôn trả về kiểu chuỗi văn bản (`str`) và cách dùng `map(int, input().split())`?
- [ ] Tôi có phân biệt được tham số `sep` (phân cách các đối số) và `end` (kết thúc dòng in) trong hàm `print()`?
- [ ] Tôi có nắm vững tính khả biến (Mutable) của List, Set, Dictionary so với tính bất biến (Immutable) của Tuple?
- [ ] Tôi có biết quy tắc khóa (Key) của Dictionary bắt buộc phải là đối tượng bất biến?
- [ ] Tôi có thể giải thích ngay kết quả của biểu thức cắt lát đảo chuỗi `s[::-1]` và cắt mảng `arr[1:4]`?
- [ ] Tôi có hiểu rõ cơ chế của khối `for - else`: Nhánh `else` bị hủy bỏ nếu vòng lặp bị ngắt bởi `break`?
- [ ] Tôi có nắm được ý nghĩa của tham số `self` trong phương thức lớp và hàm khởi tạo `__init__`?
- [ ] Tôi có phân biệt được cú pháp kế thừa `class Child(Parent):` và cách dùng `super()` để gọi phương thức lớp cha?
- [ ] Tôi có nhớ khối `finally` trong `try - except - finally` luôn luôn được thực thi kể cả khi có lệnh `return`?
- [ ] Tôi có hiểu được ứng dụng thực tế của Python trong việc bóc tách log và tự động hóa quản trị hệ thống Môn 5?
