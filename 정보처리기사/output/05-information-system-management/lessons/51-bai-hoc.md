# Python 클래스 (Class) - 기초 (Cơ bản)

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm Lớp (Class) và Đối tượng (Object/Instance) trong lập trình hướng đối tượng bằng Python.
- Hiểu rõ cú pháp định nghĩa lớp với từ khóa `class`, định nghĩa phương thức với `def`.
- Làm chủ vai trò và cơ chế truyền tự động của tham số `self` (tương đương con trỏ `this` trong Java/C++).
- Phân tích cơ chế hoạt động của phương thức khởi tạo `__init__` (Constructor) trong việc gán giá trị thuộc tính ban đầu.

## 핵심 키워드 (Từ khóa)
- **클래스 (Class)**: Bản thiết kế (Blueprint) trừu tượng đóng gói thuộc tính và phương thức.
- **객체 / 인스턴스 (Object / Instance)**: Thực thể cụ thể được sinh ra từ lớp trong bộ nhớ.
- **`self` 매개변수**: Đại diện cho chính thể hiện của đối tượng đang gọi phương thức (tương đương `this`).
- **생성자 `__init__`**: Phương thức khởi tạo tự động chạy khi đối tượng được sinh ra.

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [52-bai-hoc.md](52-bai-hoc.md) (Khởi tạo đối tượng và gọi phương thức trong Python).
- Liên kết với [04-programming-language/64-bai-hoc.md](../../04-programming-language/lessons/64-bai-hoc.md) (Khái niệm OOP trong Java và C++).
- Liên kết với [45-bai-hoc.md](45-bai-hoc.md) (Cú pháp cơ bản của Python).

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh vai trò của `self`:
  - Trong khai báo: `def set_name(self, name):` $\rightarrow$ Bắt buộc phải có `self` ở vị trí đối số đầu tiên.
  - Khi gọi phương thức: `user.set_name("Kim")` $\rightarrow$ Tuyệt đối **không** truyền `self` vào; Python tự động gán `self = user`.
  - Bên trong phương thức: Muốn truy xuất thuộc tính của đối tượng, bắt buộc phải viết `self.thuộc_tính` (ví dụ `self.name = name`).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Cấu trúc định nghĩa Lớp trong Python
```python
class Person:
    # Phương thức khởi tạo (Constructor)
    def __init__(self, name, age):
        self.name = name  # Thuộc tính thể hiện (Instance Attribute)
        self.age = age

    # Phương thức thể hiện thông thường
    def introduce(self):
        return f"Xin chào, tôi là {self.name}, {self.age} tuổi."
```

#### 2. Bản chất kỹ thuật của tham số `self`
| Tiêu chí | Tham số `self` trong Python | Từ khóa `this` trong Java / C++ |
| :--- | :--- | :--- |
| **Khai báo trong hàm** | **Bắt buộc phải viết tường minh** làm tham số đầu tiên của phương thức | Ẩn định ngầm (Implicit), không cần khai báo trong danh sách tham số |
| **Bản chất con trỏ** | Trỏ tới chính địa chỉ của thể hiện cụ thể đang thực thi | Con trỏ/Tham chiếu ngầm định trỏ tới đối tượng hiện tại |
| **Khi gọi hàm** | Trình thông dịch tự động truyền đối tượng vào vị trí `self` | Tự động gắn kết ngầm qua đối tượng gọi |

#### 3. Phương thức khởi tạo đặc biệt `__init__`
- Trong Python, các phương thức có hai dấu gạch dưới ở đầu và cuối (Dunder Methods / Magic Methods) giữ vai trò hệ thống đặc biệt.
- Phương thức `__init__` là hàm khởi tạo (Constructor). Khi thực thi lệnh `p = Person("Nam", 20)`, Python tự động thực hiện hai bước ngầm:
  1. Cấp phát vùng nhớ cho đối tượng `Person` mới (thông qua hàm `__new__`).
  2. Tự động gọi `Person.__init__(p, "Nam", 20)` để khởi tạo các trường dữ liệu ban đầu.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Ví dụ mã nguồn thi Kỹ sư xử lý thông tin
```python
class Counter:
    def __init__(self):
        self.count = 0      # Khởi tạo giá trị biến đếm ban đầu bằng 0

    def increment(self):
        self.count += 1     # Tăng biến đếm của đối tượng lên 1

    def get_count(self):
        return self.count

# Luồng thực thi:
c1 = Counter()
c2 = Counter()

c1.increment()
c1.increment()
c2.increment()

print(c1.get_count(), c2.get_count()) # In ra: 2 1
```

#### 2. Phân biệt Biến lớp (Class Variable) và Biến thể hiện (Instance Variable)
- **Biến thể hiện (Instance Variable)**: Khai báo với tiền tố `self.biến`, mỗi đối tượng sở hữu một bản sao riêng biệt trong bộ nhớ.
- **Biến lớp (Class Variable)**: Khai báo trực tiếp bên trong thân class ngoài các hàm, được chia sẻ chung cho tất cả các đối tượng được sinh ra từ lớp đó:
  ```python
  class Dog:
      species = "Mammal" # Biến lớp dùng chung cho mọi con chó
      def __init__(self, name):
          self.name = name # Biến thể hiện riêng của từng con chó
  ```

---

### 복습 체크리스트
- [ ] Tại sao mọi phương thức thể hiện trong Python đều bắt buộc phải có tham số `self` đứng đầu?
- [ ] Khi gọi `obj.display()`, tham số `self` được nạp giá trị từ đâu?
- [ ] Phương thức `__init__` trong Python tương đương với thành phần nào trong ngôn ngữ Java?
- [ ] Biến lớp (Class Variable) khác với Biến thể hiện (Instance Variable) ở điểm nào?
