# 264 - 274. 파이썬 문법 (Python Syntax & Basics)

## 학습 목표 (Mục tiêu)
- Tổng hợp toàn diện ngữ pháp và cú pháp lập trình cốt lõi trong ngôn ngữ Python từ cơ bản đến nâng cao.
- Nắm vững cú pháp định nghĩa hàm khởi tạo đối tượng (`__init__`) và phương thức trong lập trình hướng đối tượng (OOP) của Python.
- Rèn luyện kỹ năng giải các câu hỏi lần vết thuật toán Python tổng hợp: Xử lý chuỗi, Cắt lát mảng, Thao tác trên từ điển (Dictionary) và Vòng lặp kết hợp điều kiện.

## 핵심 키워드 (Từ khóa)
- 파이썬 문법 종합 (Python Syntax Comprehensive)
- 생성자 메서드 (`__init__` Constructor)
- 인스턴스 메서드 (Instance Method / `self`)
- 딕셔너리 조작 (Dictionary Keys & Values / `d.keys()`, `d.values()`)
- 리스트 컴프리헨션 (List Comprehension)
- 내장 함수 (Built-in Functions / `len`, `sum`, `max`, `min`)

## 선행·연결 개념 (Kiến thức liên kết)
- [27-bai-hoc.md](27-bai-hoc.md): Các kiểu dữ liệu tuần tự trong Python.
- [29-bai-hoc.md](29-bai-hoc.md): So sánh toán tử quan hệ Java và luồng điều khiển Python.
- [25-bai-hoc.md](25-bai-hoc.md): Nền tảng nhập xuất và các cấu trúc dữ liệu Python.

## 읽는 방법 (Cách đọc)
- Ôn tập hệ thống qua 4 khối kiến trúc của Python:
  1. **Khối dữ liệu:** List (`[]`), Tuple (`()`), Dictionary (`{key: val}`), Set (`{val}`).
  2. **Khối điều khiển:** `if - elif - else`, vòng lặp `for item in sequence`, vòng lặp `while condition`.
  3. **Khối hàm & Module:** Định nghĩa bằng `def func_name(params):`.
  4. **Khối Hướng đối tượng:** Khai báo bằng `class ClassName:`, hàm tạo khởi tạo là `def __init__(self, ...):`.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng tổng hợp các thao tác cốt lõi trên Từ điển (Dictionary):**

| Thao tác | Cú pháp Python | Ý nghĩa kỹ thuật | Ví dụ với `d = {'a': 1, 'b': 2}` |
| :--- | :--- | :--- | :--- |
| **Thêm / Cập nhật** | `d[key] = value` | Nếu khóa đã có thì sửa giá trị; nếu chưa có thì thêm cặp mới | `d['c'] = 3` $\rightarrow$ Thêm cặp `'c': 3` |
| **Truy xuất an toàn** | `d.get(key, default)` | Lấy giá trị theo khóa; nếu không có trả về `default` (không báo lỗi) | `d.get('z', 0)` $\rightarrow$ Trả về `0` |
| **Lấy danh sách khóa** | `d.keys()` | Trả về danh sách chứa toàn bộ các Khóa (Keys) | `['a', 'b']` |
| **Lấy danh sách giá trị** | `d.values()` | Trả về danh sách chứa toàn bộ các Giá trị (Values) | `[1, 2]` |
| **Lấy cặp Khóa - Giá trị** | `d.items()` | Trả về danh sách các bộ Tuple `(key, value)` | `[('a', 1), ('b', 2)]` |

- **Cấu trúc Lớp (Class) và Hàm tạo (`__init__`) trong Python:**
  - *Đoạn mã OOP mẫu chuẩn đề thi:*
    ```python
    class Member:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def is_adult(self):
            return self.age >= 18

    m = Member("Kim", 20)
    print(m.name, m.is_adult())
    ```
  - *Quá trình thực thi:*
    1. Khi gọi `Member("Kim", 20)`, hàm tạo `__init__` tự động được kích hoạt.
    2. Thuộc tính `m.name` nhận giá trị `"Kim"`, `m.age` nhận giá trị `20`.
    3. Phương thức `is_adult()` kiểm tra `20 >= 18` $\rightarrow$ Trả về `True`.
    4. Màn hình in ra: `Kim True`.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Kỹ thuật List Comprehension trong Python:**
  - Cú pháp tạo danh sách siêu tốc: `[biểu_thức for biến in tập_hợp if điều_kiện]`
  - *Ví dụ:* Tạo danh sách các số chẵn bình phương từ 1 đến 5:
    ```python
    evens = [x * x for x in range(1, 6) if x % 2 == 0]
    print(evens) # In ra: [4, 16] (ứng với x=2 và x=4)
    ```
  - Đây là mẫu câu hỏi xuất hiện liên tục trong các đề thi lập trình nâng cao.

### 복습 체크리스트
- [ ] Nhớ tên hàm khởi tạo trong class Python là `__init__` (có 2 dấu gạch dưới ở mỗi bên).
- [ ] Nhớ từ điển dùng `{}` và tra cứu theo cặp `Key: Value`.
- [ ] Phân biệt được `d.keys()`, `d.values()`, và `d.items()`.
- [ ] Đọc hiểu và lần vết thành thạo cú pháp List Comprehension.
