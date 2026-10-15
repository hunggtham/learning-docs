# Python 기초 (Python Basics)

## 학습 목표 (Mục tiêu)
- Nắm vững cú pháp cơ bản và các cấu trúc dữ liệu nền tảng trong ngôn ngữ lập trình Python: Danh sách (List), Bộ dữ liệu bất biến (Tuple), Từ điển (Dictionary), Dãy số (`range`), và Kỹ thuật cắt lát (Slicing).
- Hiểu rõ cơ chế nhập xuất dữ liệu trong Python: hàm `input()` luôn trả về chuỗi, kỹ thuật ép kiểu hàng loạt bằng `map(int, input().split())`, và các tham số `sep`, `end` của hàm `print()`.
- Nắm vững cú pháp vòng lặp `for` duyệt qua phần tử và cách định nghĩa lớp (Class), phương thức cùng tham số bắt buộc `self`.

## 핵심 키워드 (Từ khóa)
- 파이썬 기초 (Python Basics)
- 리스트 vs 튜플 (List Mutable vs Tuple Immutable)
- 딕셔너리 (Dictionary / Key-Value Pair)
- 슬라이스 (Slicing / `[start:stop:step]`)
- input() & 형변환 (`map(int, input().split())`)
- print() 제어 (sep, end 매개변수)
- 클래스와 self (Classes & self Parameter)

## 선행·연결 개념 (Kiến thức liên kết)
- [24-bai-hoc.md](24-bai-hoc.md): Con trỏ và quản lý bộ nhớ động trong C.
- [26-bai-hoc.md](26-bai-hoc.md): Cú pháp thụt lề và đặc trưng ngôn ngữ Python.
- [27-bai-hoc.md](27-bai-hoc.md): Chi tiết các kiểu dữ liệu chuỗi tuần tự trong Python.

## 읽는 방법 (Cách đọc)
- Phân biệt các cấu trúc ngoặc trong Python:
  - `[ ]` (Ngoặc vuông): **List** - Danh sách động, có thể sửa, thêm, xóa thoải mái.
  - `( )` (Ngoặc tròn): **Tuple** - Bộ dữ liệu hằng, một khi đã tạo thì **không thể sửa đổi hay xóa** bất kỳ phần tử nào.
  - `{ }` (Ngoặc nhọn có cặp `k:v`): **Dictionary** - Bảng băm tra cứu theo Khóa (Key) ra Giá trị (Value).
  - `{ }` (Ngoặc nhọn chỉ có giá trị rời): **Set** - Tập hợp các phần tử duy nhất, không trùng lặp và không có thứ tự.
- Kỹ thuật cắt lát (Slicing) `a[start : stop : step]`:
  - Lấy từ chỉ số `start` đến `stop - 1` (không bao gồm `stop`).
  - Bước nhảy `step = -1` (ví dụ `a[::-1]`) dùng để đảo ngược toàn bộ chuỗi/mảng.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh 4 cấu trúc tập hợp dữ liệu trong Python:**

| Cấu trúc dữ liệu | Cú pháp khởi tạo | Tính có thể biến đổi (Mutability) | Trùng lặp phần tử | Thao tác truy xuất |
| :--- | :--- | :--- | :--- | :--- |
| **List (리스트)** | `a = [10, 20, 30]` | **Có thể thay đổi (Mutable)** | Cho phép trùng lặp | Theo chỉ số số học: `a[0]` |
| **Tuple (튜플)** | `t = (10, 20, 30)` | **Bất biến (Immutable)** | Cho phép trùng lặp | Theo chỉ số số học: `t[0]` (Chỉ đọc) |
| **Dictionary (딕셔너리)** | `d = {'name': 'Lee', 'age': 20}` | **Có thể thay đổi (Mutable)** | Key không được trùng, Value tùy ý | Theo Khóa: `d['name']` |
| **Set (세트)** | `s = {1, 2, 3}` | **Có thể thay đổi (Mutable)** | **Tuyệt đối không trùng lặp** | Không có chỉ số; dùng toán tử `in` |

- **Bảng quy tắc Slicing trong Python (`a = [10, 20, 30, 40, 50]`):**

| Cú pháp lát cắt | Ý nghĩa thao tác | Kết quả trả về |
| :--- | :--- | :--- |
| **`a[1:3]`** | Lấy từ chỉ số 1 đến chỉ số $3 - 1 = 2$ | `[20, 30]` |
| **`a[:3]`** | Bỏ trống `start` $\rightarrow$ Lấy từ đầu đến chỉ số 2 | `[10, 20, 30]` |
| **`a[2:]`** | Bỏ trống `stop` $\rightarrow$ Lấy từ chỉ số 2 đến hết mảng | `[30, 40, 50]` |
| **`a[0:5:2]`** | Lấy từ 0 đến 4 với bước nhảy 2 (lấy chỉ số 0, 2, 4) | `[10, 30, 50]` |
| **`a[::-1]`** | Bước nhảy -1 $\rightarrow$ Đảo ngược toàn bộ mảng | `[50, 40, 30, 20, 10]` |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Quy tắc tham số `self` trong phương thức lớp (Class Method):**
  - Trong Python, khi định nghĩa hàm bên trong một lớp (Class), tham số đầu tiên của hàm **bắt buộc phải là `self`** (đại diện cho chính đối tượng thể hiện hiện tại, tương đương con trỏ `this` trong Java/C++).
  - *Ví dụ:*
    ```python
    class Calculator:
        def add(self, a, b):
            return a + b
    calc = Calculator()
    print(calc.add(3, 5)) # In ra: 8 (calc tự động truyền vào self)
    ```

### 복습 체크리스트
- [ ] Phân biệt được List (ngoặc `[]`, sửa được) và Tuple (ngoặc `()`, không sửa được).
- [ ] Nhớ kỹ thuật cắt lát `a[start:stop]` không bao gồm phần tử tại chỉ số `stop`.
- [ ] Nhớ cú pháp đảo ngược mảng trong Python: `a[::-1]`.
- [ ] Nhớ tham số đầu tiên của phương thức trong class Python bắt buộc là `self`.
