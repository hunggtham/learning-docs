# 자바 객체지향 프로그래밍 (Lập trình hướng đối tượng trong Java)

## 학습 목표 (Mục tiêu)
- Nắm vững 5 đặc tính cốt lõi của Lập trình hướng đối tượng (OOP) theo khẩu quyết **캡정상추다** (Đóng gói, Che giấu thông tin, Kế thừa, Trừu tượng hóa, Đa hình).
- Phân biệt chính xác phạm vi của 4 cấp độ chỉ định truy cập (접근 제어자 - Access Modifiers): `public`, `protected`, `default`, `private` và vai trò của hàm tạo (Constructor), từ khóa `this` và `super()`.
- Phân biệt sự khác nhau mang tính quyết định giữa Nạp chồng phương thức (Overloading) và Ghi đè phương thức (Overriding); thuộc lòng 3 bước phân tích hướng đối tượng Rumbaugh theo khẩu quyết **객동기** (Đối tượng $\rightarrow$ Động $\rightarrow$ Chức năng).

## 핵심 키워드 (Từ khóa)
- 객체지향 5대 특성 (OOP Core Principles) — 캡슐화, 정보 은닉, 상속, 추상화, 다형성 (캡정상추다).
- 접근 제어자 (Access Modifiers) — `public`, `protected`, `default`, `private`.
- 생성자 및 super() (Constructor & super) — Hàm khởi tạo và gọi constructor của lớp cha.
- 오버로딩 vs 오버라이딩 (Overloading vs Overriding) — Cùng tên khác tham số vs Ghi đè phương thức lớp cha.
- 럼바우 분석 기법 (Rumbaugh OMT) — 객체 모델링 $\rightarrow$ 동적 모델링 $\rightarrow$ 기능 모델링 (객동기).
- 객체지향 언어 역사 (OOP History) — Simula 67 (đầu tiên), Smalltalk (thuần khiết đầu tiên).

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Kế thừa từ mô hình cấu trúc `struct` trong C của bài `06-con-tro-va-cau-truc-struct-trong-c.md`, phát triển mở rộng từ việc chỉ gom dữ liệu thuần túy thành thực thể tự chủ bao gồm cả dữ liệu (thuộc tính) và hành vi (phương thức).
- **Đang giải quyết gì (Current Problem):** Giải quyết câu hỏi trung tâm của bài thi Java: Khi một lớp con kế thừa lớp cha và ghi đè phương thức, nếu khai báo đối tượng kiểu đa hình (`Parent obj = new Child()`), phương thức của lớp nào sẽ thực sự được thực thi trong thời gian chạy.
- **Dùng đi đâu (Forward Handoff):** Các đối tượng tạo ra bởi từ khóa `new` trên bộ nhớ Heap sẽ được quản lý vòng đời và tự động giải phóng bởi Trình thu gom rác (Garbage Collector) trong bài `09-xu-ly-ngoai-le-thu-vien-va-garbage-collection.md`.

## 읽는 방법 (Cách đọc)
- **Phạm vi truy cập:** Xếp hạng từ rộng nhất đến hẹp nhất: `public` (tự do) > `protected` (cùng package + con cháu kế thừa) > `default` (chỉ trong cùng package) > `private` (chỉ trong nội bộ class).
- **Overloading vs Overriding:**
  - **Overloading (Nạp chồng - Tải thêm):** Cùng 1 lớp, **cùng tên hàm nhưng KHÁC tham số** (khác số lượng hoặc kiểu dữ liệu).
  - **Overriding (Ghi đè - Phủ lên):** Quan hệ Cha - Con, **GIỐNG HỆT tên, tham số và kiểu trả về**, lớp con viết lại nội dung để thay thế cha.
- **Khẩu quyết Rumbaugh:** **객·동·기** (Object Modeling $\rightarrow$ Dynamic Modeling $\rightarrow$ Functional Modeling).

---

## 자바 객체지향 프로그래밍

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [한국어]: `객체지향 기법의 핵심 원칙은 캡슐화, 정보 은닉, 상속, 추상화, 다형성이다. 오버로딩은 같은 이름의 메서드를 매개변수 차이로 중복 정의하는 것이고, 오버라이딩은 상속받은 상위 클래스의 메서드를 하위 클래스에서 재정의하는 것이다. 럼바우 기법의 순서는 객체 -> 동적 -> 기능 모델링이다.`
  - [Tiếng Việt]: Các nguyên tắc cốt lõi của OOP gồm Đóng gói, Che giấu thông tin, Kế thừa, Trừu tượng hóa, Đa hình (캡정상추다). Overloading là định nghĩa nhiều hàm cùng tên khác tham số; Overriding là lớp con định nghĩa lại hàm thừa kế từ lớp cha. Trình tự phương pháp Rumbaugh là Đối tượng -> Động -> Chức năng (객동기).

- **1. Bảng 5 đặc tính cốt lõi của OOP (객체지향 5대 주요 원칙 - 캡정상추다):**

| Đặc tính | Tên Hàn / Anh | Bản chất kỹ thuật chuẩn khảo thí |
| :--- | :--- | :--- |
| **1. Đóng gói** | **캡슐화** (Encapsulation) | Gom thuộc tính (dữ liệu) và phương thức (hành vi) vào một đơn vị Lớp; tăng tính độc lập module. |
| **2. Che giấu thông tin**| **정보 은닉** (Information Hiding) | Ẩn chi tiết nội bộ (`private`), chỉ cho phép tương tác qua giao diện công khai (`getter`/`setter`). |
| **3. Kế thừa** | **상속** (Inheritance) | Lớp con thừa hưởng và mở rộng tài nguyên từ lớp cha (`extends`), tối ưu hóa khả năng tái sử dụng mã nguồn. |
| **4. Trừu tượng hóa** | **추상화** (Abstraction) | Lược bỏ các chi tiết phức tạp thứ yếu, chỉ tập trung mô hình hóa các đặc trưng bản chất của thực thể. |
| **5. Tính đa hình** | **다형성** (Polymorphism) | Cùng một lời gọi phương thức nhưng các đối tượng khác nhau sẽ có hành vi thực thi khác nhau. |

- **2. Bảng phạm vi 4 cấp độ chỉ định truy cập trong Java (접근 제어자):**

| Cấp độ truy cập | Trong cùng Class | Trong cùng Package | Lớp con kế thừa (Subclass)| Toàn bộ bên ngoài |
| :--- | :---: | :---: | :---: | :---: |
| **`public`** | **O** | **O** | **O** | **O (Tự do)** |
| **`protected`** | **O** | **O** | **O** | X |
| **`default` (package-private)**| **O** | **O** | X | X |
| **`private`** | **O (Chỉ nội bộ)**| X | X | X |

- **3. Bảng đối chiếu quyết định: Overloading vs Overriding:**

| Tiêu chuẩn phân biệt | Nạp chồng (메서드 오버로딩 - Overloading) | Ghi đè (메서드 오버라이딩 - Overriding) |
| :--- | :--- | :--- |
| **Môi trường xuất hiện** | Diễn ra **ngay bên trong một Class**. | Diễn ra giữa **hai Class có quan hệ Cha - Con (Kế thừa)**. |
| **Tên phương thức** | **Bắt buộc phải giống hệt nhau**. | **Bắt buộc phải giống hệt nhau**. |
| **Danh sách tham số** | **BẮT BUỘC PHẢI KHÁC NHAU** (số lượng, kiểu dữ liệu). | **BẮT BUỘC PHẢI GIỐNG HỆT NHAU**. |
| **Kiểu dữ liệu trả về** | Có thể giống hoặc khác (không quyết định). | Bắt buộc phải giống hệt (hoặc là kiểu con). |
| **Thời điểm liên kết** | **Liên kết tĩnh (Static Binding / Compile-time)**. | **Liên kết động (Dynamic Binding / Runtime)**. |

- **4. 3 bước phân tích hướng đối tượng Rumbaugh (럼바우 분석 기법 - 객동기):**
  1. **객체 모델링 (Object Modeling):** Bước quan trọng nhất và tiến hành đầu tiên. Dùng **Biểu đồ đối tượng (Object Diagram)** biểu diễn cấu trúc tĩnh của hệ thống.
  2. **동적 모델링 (Dynamic Modeling):** Dùng **Biểu đồ trạng thái (State Diagram)** mô tả hành vi thay đổi trạng thái và phản ứng với sự kiện theo thời gian.
  3. **기능 모델링 (Functional Modeling):** Dùng **Biểu đồ luồng dữ liệu (DFD - Data Flow Diagram)** mô tả quá trình biến đổi dữ liệu của các hàm.

- **주의/함정 (Bẫy đề thi):**
  - **Hàm tạo Constructor:** Tên hàm tạo **bắt buộc phải trùng 100% với tên Class** và **tuyệt đối không có kiểu trả về** (kể cả `void`). Nếu viết `public void Person()`, Java coi đó là phương thức thường chứ không phải hàm tạo.
  - **Lệnh `super()`:** Lệnh gọi constructor của lớp cha `super()` bắt buộc phải là **câu lệnh đầu tiên** nằm trong thân hàm tạo của lớp con.
  - **Simula vs Smalltalk:** Ngôn ngữ OOP đầu tiên là **Simula 67**, nhưng ngôn ngữ OOP thuần khiết (Pure OOP) đầu tiên là **Smalltalk**.

- **한 문장 설명 (Câu chốt tự nhớ):**
  - *"캡정상추다 5 nguyên tắc, public mở toang private giấu kín; Overloading khác tham số, Overriding đè lớp cha; Rumbaugh nhớ ngay 객-동-기."*

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Lần vết chương trình Kế thừa, Overriding và Đa hình trong Java:
```java
// Lớp cha
class Parent {
    int x = 10;

    void display() {
        System.out.println("Parent display, x = " + x);
    }
}

// Lớp con kế thừa từ Parent
class Child extends Parent {
    int x = 20; // Che mờ biến x của cha

    // Ghi đè (Overriding) phương thức display
    @Override
    void display() {
        System.out.println("Child display, x = " + x + ", super.x = " + super.x);
    }

    void childOnly() {
        System.out.println("Phuong thuc rieng cua Child");
    }
}

public class PolymorphismDemo {
    public static void main(String[] args) {
        // Đa hình: Khai báo kiểu cha nhưng trỏ tới đối tượng con
        Parent p = new Child();

        // BẪY THI: Phương thức được gọi dựa trên ĐỐI TƯỢNG THỰC TẾ TRÊN HEAP (Child)
        p.display(); // In ra: Child display, x = 20, super.x = 10

        // BẪY THI VỀ BIẾN: Thuộc tính không có đa hình, truy xuất biến phụ thuộc KIỂU KHAI BÁO (Parent)
        System.out.println("p.x = " + p.x); // In ra: p.x = 10 (chứ không phải 20!)
    }
}
```

#### 2. Minh họa Nạp chồng phương thức (Method Overloading):
```java
class MathUtils {
    // 1. Hàm cộng 2 số nguyên
    int add(int a, int b) {
        return a + b;
    }

    // 2. Overloading: Khác số lượng tham số (3 số nguyên)
    int add(int a, int b, int c) {
        return a + b + c;
    }

    // 3. Overloading: Khác kiểu dữ liệu tham số (2 số thực)
    double add(double a, double b) {
        return a + b;
    }
}
```

#### 3. Bảng lần vết khởi tạo thứ tự Constructor (`super()` ngầm định):
Đoạn mã:
```java
class A {
    public A() {
        System.out.print("A ");
    }
}
class B extends A {
    public B() {
        // Trình biên dịch tự động chèn super(); gọi constructor của A trước
        System.out.print("B ");
    }
}
class C extends B {
    public C() {
        // Tự động gọi constructor của B trước
        System.out.print("C ");
    }
}

public class Test {
    public static void main(String[] args) {
        C obj = new C();
    }
}
```

*Trình tự thực thi:*
1. Lệnh `new C()` kích hoạt constructor của `C`.
2. Do có kế thừa, `C` gọi `super()` của `B` trước $\rightarrow$ `B` lại gọi `super()` của `A` trước.
3. Constructor của `A` in ra: **`A`**.
4. Quay trở về `B`, in tiếp: **`B`**.
5. Cuối cùng constructor của `C` mới in: **`C`**.
- **Kết quả in ra màn hình:** **`A B C `**.

---

### 복습 체크리스트
- [ ] Thuộc lòng 5 nguyên tắc OOP: **캡정상추다** (캡슐화, 정보 은닉, 상속, 추상화, 다형성).
- [ ] Nhớ thứ tự phạm vi truy cập: `public` > `protected` > `default` > `private`.
- [ ] Phân biệt được: Overloading (cùng class, khác tham số) vs Overriding (cha con, giống hệt tham số).
- [ ] Nhớ hàm tạo bắt buộc trùng tên class và không có kiểu trả về; `super()` luôn nằm ở dòng đầu tiên.
- [ ] Thuộc lòng 3 bước Rumbaugh: **객동기** (객체 모델링 $\rightarrow$ 동적 모델링 $\rightarrow$ 기능 모델링).
- [ ] Ghi nhớ Simula 67 là ngôn ngữ OOP đầu tiên, Smalltalk là OOP thuần khiết đầu tiên.
