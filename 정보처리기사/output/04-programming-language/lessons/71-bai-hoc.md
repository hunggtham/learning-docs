# 078. 사용자 정의 함수와 클래스 (User Defined Functions & Classes)

## 학습 목표 (Mục tiêu)
- Nắm vững cú pháp định nghĩa hàm do người dùng tự tạo (사용자 정의 함수) và cấu trúc lớp đối tượng (클래스 - Class) trong Java và Python.
- Thuộc lòng phạm vi quyền hạn của 4 chỉ định truy cập (접근 제어자 - Access Modifiers) trong Java: `public`, `protected`, `default` (package-private), và `private`.
- Phân biệt cơ chế khởi tạo đối tượng (생성자 - Constructor) giữa Java (tên trùng tên Class, không có kiểu trả về, từ khóa `this`) và Python (phương thức ma thuật `__init__`, tham số bắt buộc `self`).

## 핵심 키워드 (Từ khóa)
- 사용자 정의 함수 (User-Defined Functions)
- 클래스와 객체 (Class & Object)
- 접근 제어자 (Access Modifiers: public, protected, default, private)
- 생성자 (Constructor / 인스턴스 초기화)
- `this` 키워드 (Java Instance Reference)
- `__init__` 메소드 & `self` (Python Dunder Method)
- 정보 은닉 (Information Hiding / Encapsulation)

## 선행·연결 개념 (Kiến thức liên kết)
- [70-bai-hoc.md](70-bai-hoc.md): Nhận diện các lỗ hổng bảo mật và quản lý an toàn bộ nhớ.
- [72-bai-hoc.md](72-bai-hoc.md): Phân loại các ngôn ngữ lập trình hướng thủ tục, OOP và thông dịch.
- [48-bai-hoc.md](48-bai-hoc.md): 5 nguyên lý hướng đối tượng kinh điển (캡정상추다).

## 읽는 방법 (Cách đọc)
- Trong bài thi kỹ sư CNTT:
  - Bảng quyền hạn truy cập của Java là câu hỏi xuất hiện liên tục:
    - Rộng nhất: `public` (Mọi nơi).
    - Cùng package + Lớp con kế thừa ở package khác: `protected`.
    - Chỉ trong cùng package (mặc định khi không khai báo): `default`.
    - Hẹp nhất: `private` (Chỉ nội bộ bên trong chính Class đó).
  - Về Constructor: Nhớ rằng Constructor **không bao giờ có kiểu dữ liệu trả về** (kể cả `void`), tự động kích hoạt khi toán tử `new` được gọi.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng phân cấp 4 chỉ định truy cập trong Java (Access Modifiers):**

| Chỉ định (Modifier) | Cùng lớp (Class) | Cùng gói (Package) | Lớp con khác gói (Subclass) | Toàn thế giới (World) |
| :--- | :---: | :---: | :---: | :---: |
| **`public`** | O | O | O | **O** |
| **`protected`** | O | O | **O** | X |
| **`default`** (không ghi) | O | **O** | X | X |
| **`private`** | **O** | X | X | X |

- **2. So sánh Constructor và tham chiếu đối tượng giữa Java và Python:**

| Tiêu chí | Ngôn ngữ Java | Ngôn ngữ Python |
| :--- | :--- | :--- |
| **Tên phương thức khởi tạo** | Bắt buộc **trùng tên với Class** (ví dụ: `public Student()`) | Sử dụng phương thức đặc biệt **`__init__()`** |
| **Kiểu dữ liệu trả về** | **Tuyệt đối không có** (kể cả `void`) | Không có (trả về ngầm định `None`) |
| **Tham chiếu bản thân đối tượng** | Sử dụng từ khóa ngầm định **`this`** (ví dụ: `this.name = name;`) | Khai báo tường minh tham số đầu tiên là **`self`** (ví dụ: `self.name = name`) |
| **Thời điểm kích hoạt** | Tự động chạy ngay khi gọi toán tử `new Student(...)` | Tự động chạy ngay khi khởi tạo instance `Student(...)` |

- **3. Cú pháp minh họa đối chiếu:**
  - *Mã nguồn Java:*
    ```java
    public class Person {
        private String name; // Bảo mật dữ liệu
        public Person(String name) { // Constructor
            this.name = name;
        }
        public String getName() { return this.name; }
    }
    ```
  - *Mã nguồn Python:*
    ```python
    class Person:
        def __init__(self, name): # Hàm khởi tạo
            self.__name = name    # Tiền tố __ đại diện private
        def get_name(self):
            return self.__name
    ```

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Phương thức nạp chồng khởi tạo (Constructor Overloading):**
  - Trong một lớp Java có thể định nghĩa nhiều Constructor có cùng tên nhưng khác nhau về số lượng hoặc kiểu dữ liệu của các tham số. Khi khởi tạo đối tượng, trình biên dịch sẽ tự động đối sánh tham số truyền vào để gọi đúng hàm tương ứng.

### 복습 체크리스트
- [ ] Thuộc làu thứ tự phạm vi Access Modifier từ rộng đến hẹp: `public` $\rightarrow$ `protected` $\rightarrow$ `default` $\rightarrow$ `private`.
- [ ] Nhớ `protected` cho phép truy cập từ cùng package và lớp con kế thừa khác package.
- [ ] Khẳng định Constructor trong Java không có kiểu trả về và mang tên trùng tên lớp.
- [ ] Phân biệt được `this` trong Java (tự động) và `self` trong Python (khai báo tường minh).
