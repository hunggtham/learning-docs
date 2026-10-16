# 파이썬 기본 문법 및 시퀀스 자료형 (Lập trình Python & Kiểu Sequence)

## 학습 목표 (Mục tiêu)
- Nắm vững đặc trưng cú pháp cốt lõi của ngôn ngữ Python: quy tắc thụt lề bắt buộc (Indentation), dấu hai chấm `:`, định kiểu động (Dynamic Typing) và cách khai báo hàm `def`, biểu thức `lambda`.
- Phân biệt sự khác nhau mang tính bản chất giữa hai kiểu dữ liệu tuần tự then chốt: Danh sách `list` (có thể thay đổi - Mutable `[]`) và Bộ `tuple` (bất biến - Immutable `()`).
- Sử dụng thành thạo kỹ thuật cắt lát (Slicing `[start:stop:step]`), chỉ số âm (Negative Indexing), cấu trúc từ điển `dict`, tập hợp `set` và cấu trúc Lớp hướng đối tượng với hàm khởi tạo `__init__` và tham số `self`.

## 핵심 키워드 (Từ khóa)
- 파이썬 시퀀스 자료형 (Python Sequence Data Types) — `list`, `tuple`, `range`, `str`.
- 가변 vs 불변 (Mutable vs Immutable) — `list` sửa đổi được vs `tuple` cấm sửa đổi.
- 슬라이싱 (Slicing `[start:stop:step]`) — Cắt chuỗi/mảng theo chỉ số bắt đầu, kết thúc và bước nhảy.
- 음수 인덱스 (Negative Indexing) — Chỉ số âm tính ngược từ cuối danh sách (`-1` là phần tử cuối).
- 딕셔너리와 세트 (Dictionary & Set) — Ánh xạ cặp `key:value` và Tập hợp khử trùng lặp.
- 파이썬 클래스 (Python Class & `__init__`) — Phương thức khởi tạo và tham số tự tham chiếu `self`.

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Kế thừa tư duy giải thuật điều khiển và vòng lặp từ `04-cau-truc-dieu-khien-re-nhanh-va-vong-lap.md`, chuyển đổi sang văn phong lập trình kịch bản hiện đại của Python.
- **Đang giải quyết gì (Current Problem):** Giải quyết nhóm câu hỏi viết mã Python ngày càng chiếm tỷ trọng lớn trong kỳ thi Kỹ sư xử lý thông tin: Lần vết cắt lát chuỗi/danh sách, phân biệt lỗi gán giá trị vào tuple và lần vết phương thức trong class.
- **Dùng đi đâu (Forward Handoff):** Kiến thức hướng đối tượng và hàm khởi tạo `__init__` của Python sẽ được đối chiếu với mô hình hướng đối tượng tĩnh, chặt chẽ trong Java ở bài `08-lap-trinh-huong-doi-tuong-java-oop.md`.

## 읽는 방법 (Cách đọc)
- **Cắt lát `[start:stop:step]`:** Luôn nhớ quy tắc "lấy từ $start$ đến trước $stop$" (tức là $stop - 1$). Nếu bước nhảy âm ($step < 0$), mảng sẽ được duyệt đảo ngược từ phải qua trái.
- **Cặp ngoặc phân loại:**
  - Ngoặc vuông `[]` là **`list`** (thêm, sửa, xóa thoải mái bằng `.append()`, `del`).
  - Ngoặc tròn `()` là **`tuple`** (bất biến, cố tình gán lại phần tử `t[0] = 10` sẽ bị báo lỗi `TypeError`).
  - Ngoặc nhọn `{}` là **`dict`** (nếu có dấu `:` như `{"k": "v"}`) hoặc **`set`** (nếu chỉ có giá trị `{1, 2, 3}`).

---

## 파이썬 기본 문법 및 시퀀스 자료형

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [한국어]: `파이썬은 들여쓰기로 블록을 구분하며, 리스트([])는 요소 수정이 가능한 가변(Mutable) 객체이고 튜플(())은 생성 후 수정이 불가능한 불변(Immutable) 객체이다. 슬라이싱 a[start:stop:step]은 stop 바로 앞 요소까지만 추출한다.`
  - [Tiếng Việt]: Python dùng thụt lề để phân tách khối lệnh; list ([]) là đối tượng khả biến (Mutable) cho phép sửa đổi, còn tuple (()) là đối tượng bất biến (Immutable) không thể sửa đổi sau khi tạo. Cắt lát a[start:stop:step] chỉ trích xuất đến phần tử ngay trước chỉ số stop.

- **1. Bảng đối chiếu các cấu trúc dữ liệu cốt lõi trong Python:**

| Cấu trúc dữ liệu | Cú pháp khởi tạo | Tính biến đổi (Mutability) | Đặc điểm thi cử trọng tâm |
| :--- | :--- | :---: | :--- |
| **`list` (Danh sách)** | `[1, 2, 3]` | **Mutable (Khả biến)** | Thêm bớt linh hoạt qua `append()`, `insert()`, `pop()`. |
| **`tuple` (Bộ hằng số)** | `(1, 2, 3)` | **Immutable (Bất biến)** | **Cấm sửa đổi**; tuple 1 phần tử bắt buộc có dấu phẩy: `(1,)`. |
| **`range` (Dãy số)** | `range(1, 5)` | **Immutable** | Sinh dãy số từ 1 đến 4 (dừng trước 5). |
| **`dict` (Từ điển)** | `{"id": 1, "name": "Kim"}` | **Mutable** | Truy xuất theo khóa `d["id"]`, khóa không được trùng lặp. |
| **`set` (Tập hợp)** | `{1, 2, 2, 3}` $\rightarrow$ `{1, 2, 3}`| **Mutable** | **Tự động khử trùng lặp**, không lưu thứ tự phần tử. |

- **2. Bảng quy tắc cắt lát (Slicing Syntax `[start:stop:step]`):**
Giả sử danh sách: `a = [10, 20, 30, 40, 50]` (chỉ số dương: $0 \rightarrow 4$, chỉ số âm: $-5 \rightarrow -1$).

| Cú pháp cắt lát | Kết quả trích xuất | Diễn giải quy tắc chuẩn thi |
| :--- | :--- | :--- |
| `a[1:4]` | `[20, 30, 40]` | Lấy từ chỉ số 1 đến trước chỉ số 4 (gồm index 1, 2, 3). |
| `a[:3]` | `[10, 20, 30]` | Khuyết $start$: Lấy từ đầu danh sách đến trước index 3. |
| `a[2:]` | `[30, 40, 50]` | Khuyết $stop$: Lấy từ index 2 cho đến hết danh sách. |
| `a[::2]` | `[10, 30, 50]` | $step = 2$: Lấy cách quãng 2 bước (index 0, 2, 4). |
| `a[::-1]` | `[50, 40, 30, 20, 10]` | $step = -1$: **Đảo ngược toàn bộ danh sách**. |
| `a[-1]` | `50` | Lấy phần tử cuối cùng bằng chỉ số âm. |
| `a[-3:-1]` | `[30, 40]` | Lấy từ index -3 (30) đến trước index -1 (trước 50). |

- **3. Hướng đối tượng trong Python (Class & Method):**

| Cú pháp Python | Tương đương trong Java/C++ | Vai trò kỹ thuật |
| :--- | :--- | :--- |
| `class Person:` | `class Person { ... }` | Khai báo Lớp đối tượng. |
| `def __init__(self, name):`| `public Person(String name) { ... }` | **Phương thức khởi tạo (Constructor)** tự động gọi khi tạo mới. |
| Tham số `self` | Con trỏ / Từ khóa `this` | Tham chiếu đại diện cho chính đối tượng hiện tại đang thực thi. |

- **주의/함정 (Bẫy đề thi):**
  - **Cố tình sửa Tuple:** `t = (1, 2, 3); t[0] = 10;` $\rightarrow$ Đề thi hỏi kết quả: Chương trình bị **báo lỗi thực thi `TypeError`**, không thể thay đổi giá trị của tuple.
  - **Tuple 1 phần tử:** Viết `x = (5)` thì Python hiểu `x` là số nguyên `int` thông thường. Muốn tạo tuple 1 phần tử bắt buộc phải có dấu phẩy: `x = (5,)`.
  - **Chỉ số kết thúc $stop$:** Lệnh `range(1, 10)` chỉ sinh các số từ $1$ đến $9$, hoàn toàn không có số $10$.

- **한 문장 설명 (Câu chốt tự nhớ):**
  - *"List vuông sửa được tuple tròn cấm thay; cắt lát dừng trước stop, âm một (-1) đứng cuối hàng."*

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Lần vết chi tiết cắt lát và các thao tác trên List trong Python:
```python
# Khởi tạo danh sách
numbers = [10, 20, 30, 40, 50, 60]

# 1. Cắt lát cơ bản
print(numbers[1:5:2]) # Index 1 (20), index 3 (40) -> Kết quả: [20, 40]

# 2. Thao tác thêm, bớt
numbers.append(70)    # Thêm 70 vào cuối: [10, 20, 30, 40, 50, 60, 70]
numbers.pop(0)        # Xóa phần tử tại index 0 (10): [20, 30, 40, 50, 60, 70]

# 3. Phân biệt Tuple và lỗi bất biến
my_tuple = (100, 200, 300)
print(my_tuple[1])    # Đọc dữ liệu bình thường -> 200
# my_tuple[1] = 999   # LỖI BẪY: TypeError: 'tuple' object does not support item assignment

# 4. Tập hợp loại bỏ phần tử trùng lặp
raw_data = [1, 2, 2, 3, 3, 3, 4]
unique_data = list(set(raw_data))
print(unique_data)    # Kết quả: [1, 2, 3, 4]
```

#### 2. Lần vết chương trình Hướng đối tượng Python trong đề thi thực tế:
```python
class Calculator:
    def __init__(self, initial_val=0):
        self.val = initial_val # Thuộc tính lưu trữ giá trị

    def add(self, n):
        self.val += n
        return self.val

    def subtract(self, n):
        self.val -= n
        return self.val

# Khởi tạo đối tượng
calc = Calculator(10)
calc.add(5)       # val = 10 + 5 = 15
calc.subtract(3)  # val = 15 - 3 = 12

print("Ket qua cuoi cung:", calc.val) # Kết quả in ra: 12
```

#### 3. Bảng lần vết thuật toán duyệt Dictionary kết hợp điều kiện:
Đoạn mã Python:
```python
scores = {"Kim": 85, "Lee": 92, "Park": 78}
total = 0
for name, score in scores.items():
    if score >= 80:
        total += score
print("Total =", total)
```

*Bảng lần vết biến:*

| Lượt duyệt | Cặp `(name, score)` | Điều kiện `score >= 80` | Hành động thực hiện | Giá trị `total` |
| :---: | :---: | :---: | :--- | :---: |
| 1 | `("Kim", 85)` | $85 \ge 80$ (Đúng) | Thực hiện `total += 85` | **85** |
| 2 | `("Lee", 92)` | $92 \ge 80$ (Đúng) | Thực hiện `total += 92` | **177** |
| 3 | `("Park", 78)`| $78 \ge 80$ (Sai) | Bỏ qua, không cộng | **177** |
| **Kết quả in ra** | — | — | **`Total = 177`** | — |

---

### 복습 체크리스트
- [ ] Nhớ trong Python: Thụt lề là bắt buộc để xác định khối lệnh (thay thế `{ }`).
- [ ] Phân biệt được: List `[]` là Mutable (sửa được), Tuple `()` là Immutable (bất biến).
- [ ] Nhớ cách tạo tuple 1 phần tử: Bắt buộc có dấu phẩy sau số `(5,)`.
- [ ] Nắm chắc cú pháp cắt lát: `a[start:stop:step]` chỉ lấy đến $stop - 1$.
- [ ] Nhớ `a[::-1]` đảo ngược danh sách và `a[-1]` lấy phần tử cuối cùng.
- [ ] Nắm vững cách khai báo hàm `def`, constructor `__init__` và tham số `self` trong Class.
