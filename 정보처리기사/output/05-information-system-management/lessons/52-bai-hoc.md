# Python 클래스와 함수 (Class and Functions)

## 학습 목표 (Mục tiêu)
- Nắm vững cú pháp tạo lập đối tượng (Instantiation) từ lớp và cách truy xuất thành viên bằng toán tử dấu chấm `.`.
- Phân biệt rõ sự khác nhau giữa Hàm độc lập (Function) và Phương thức của lớp (Method) trong Python.
- Hiểu rõ cơ chế kế thừa (Inheritance: `class Child(Parent):`) và kỹ thuật gọi hàm khởi tạo lớp cha thông qua hàm `super()`.
- Làm chủ kỹ thuật ghi đè phương thức (Method Overriding) thường xuất hiện trong các câu hỏi thi thực hành.

## 핵심 키워드 (Từ khóa)
- **객체 생성 (Instantiation)**: Cú pháp `obj = ClassName()`.
- **점 연산자 (Dot Operator `.`)**: Truy cập thuộc tính (`obj.attr`) hoặc gọi hàm thành viên (`obj.method()`).
- **함수 vs 메소드 (Function vs Method)**: Hàm độc lập tự do (`def fn():`) vs Phương thức gắn liền với đối tượng qua `self`.
- **상속 (Inheritance)**: Tái sử dụng và mở rộng lớp `class LớpCon(LớpCha):`.
- **메소드 오버라이딩 (Method Overriding)**: Lớp con viết lại phương thức cùng tên của lớp cha để thay đổi hành vi.

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [51-bai-hoc.md](51-bai-hoc.md) (Khái niệm cơ bản về Class và tham số self).
- Liên kết với [04-programming-language/64-bai-hoc.md](../../04-programming-language/lessons/64-bai-hoc.md) (Tính kế thừa và đa hình trong OOP).
- Liên kết với [50-bai-hoc.md](50-bai-hoc.md) (Cấu trúc điều khiển trong Python).

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh trong đề thi:
  - Nếu gọi `calc(3, 4)` trực tiếp mà không có dấu chấm trước tên hàm $\rightarrow$ Đây là **Hàm độc lập (Function)**.
  - Nếu gọi `a.calc(3, 4)` qua một biến đối tượng $\rightarrow$ Đây là **Phương thức (Method)**.
  - Khi lớp con ghi đè phương thức `talk()` của lớp cha, đối tượng của lớp con sẽ ưu tiên chạy hàm `talk()` của **chính lớp con**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Khởi tạo đối tượng và Truy xuất thành viên
- **Cú pháp tạo đối tượng**: `biến = TênLớp(tham_số)`
  - Ví dụ: `a = Cls(10)` $\rightarrow$ Cấp phát đối tượng trong bộ nhớ Heap và gán tham chiếu cho biến `a`.
- **Toán tử truy xuất dấu chấm (`.`)**:
  - Truy xuất thuộc tính: `print(a.x)`
  - Gọi phương thức: `a.chg(20)`
- **So sánh Hàm độc lập vs Phương thức**:
  | Tiêu chí | Hàm độc lập (Function) | Phương thức của lớp (Method) |
  | :--- | :--- | :--- |
  | **Vị trí định nghĩa** | Nằm ở phạm vi toàn cục (Global) ngoài class | Nằm bên trong phạm vi khối mã của một Class |
  | **Tham số đối tượng** | Không yêu cầu tham số `self` bắt buộc | Luôn yêu cầu `self` là tham số đầu tiên |
  | **Cách thức gọi** | Gọi trực tiếp qua tên hàm: `calc(10, 20)` | Phải gọi thông qua một thể hiện: `obj.calc(10, 20)` |

#### 2. Kế thừa (Inheritance) và Ghi đè (Method Overriding)
- **Cú pháp kế thừa**: `class LớpCon(LớpCha):`
- **Hàm `super()`**: Cho phép lớp con gọi trực tiếp các phương thức (đặc biệt là `__init__`) của lớp cha:
  ```python
  class Parent:
      def __init__(self, name):
          self.name = name

      def greet(self):
          return f"Xin chào, tôi là {self.name}"

  class Child(Parent):
      def __init__(self, name, school):
          super().__init__(name) # Tái sử dụng logic khởi tạo của lớp cha
          self.school = school

      # Ghi đè phương thức greet()
      def greet(self):
          return f"Chào bạn! Em là học sinh {self.name} trường {self.school}"
  ```

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Bài toán lần vết đề thi Kỹ sư xử lý thông tin
```python
class Calc:
    def __init__(self, x):
        self.x = x

    def add(self, y):
        self.x += y
        return self.x

    def mul(self, y):
        self.x *= y
        return self.x

a = Calc(5)      # Khởi tạo đối tượng a với x = 5
print(a.add(3))  # self.x = 5 + 3 = 8 -> in ra: 8
print(a.mul(2))  # self.x = 8 * 2 = 16 -> in ra: 16
```

#### 2. Tính đa kế thừa (Multiple Inheritance) trong Python
- Khác với Java (chỉ hỗ trợ đơn kế thừa lớp), Python cho phép một lớp con kế thừa đồng thời từ nhiều lớp cha:
  ```python
  class A:
      def feature_a(self): print("Tính năng A")

  class B:
      def feature_b(self): print("Tính năng B")

  class C(A, B): # Lớp C kế thừa cả A và B
      pass

  obj = C()
  obj.feature_a() # Hợp lệ!
  obj.feature_b() # Hợp lệ!
  ```

---

### 복습 체크리스트
- [ ] Sự khác biệt then chốt giữa một Function độc lập và một Method của Class trong Python là gì?
- [ ] Cú pháp khai báo một lớp con kế thừa từ một lớp cha trong Python được viết như thế nào?
- [ ] Hàm `super()` trong phương thức `__init__` của lớp con có tác dụng kỹ thuật gì?
- [ ] Điều gì xảy ra khi lớp con định nghĩa một phương thức có cùng tên và danh sách tham số với lớp cha (Method Overriding)?
