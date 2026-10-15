# 6. 객체지향 (Hướng Đối Tượng - OOP)

## 학습 목표 (Mục tiêu)
- Nắm vững 6 khái niệm nền tảng của Lập trình hướng đối tượng (`객체지향 - OOP`): Đối tượng (`객체`), Lớp (`클래스`), Thông điệp (`메시지`), Đóng gói (`캡슐화`), Kế thừa (`상속`), và Đa hình (`다형성`).
- Hiểu rõ mối liên hệ giữa Đóng gói (`캡슐화`) và Che giấu thông tin (`정보 은닉`), vai trò nâng cao tính độc lập của mô-đun.
- Phân biệt tuyệt đối giữa hai cơ chế Đa hình kinh điển: Nạp chồng phương thức (`오버로딩 - Overloading`) và Ghi đè phương thức (`오버라이딩 - Overriding`).

## 핵심 키워드 (Từ khóa)
- 객체지향 (Lập trình hướng đối tượng / Object-Oriented Programming - OOP)
- 객체 / 클래스 (Object / Class)
- 메시지 (Thông điệp / Message)
- 캡슐화 / 정보 은닉 (Đóng gói / Che giấu thông tin / Encapsulation / Information Hiding)
- 상속성 (Tính kế thừa / Inheritance)
- 다형성 (Tính đa hình / Polymorphism)
- 오버로딩 vs 오버라이딩 (Overloading vs Overriding)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([1. 소프트웨어 아키텍처](25-bai-hoc.md)):** Sau khi xem xét kiến trúc mức cao và mô hình 4+1 View, bài này đi sâu vào phương pháp luận lập trình hướng đối tượng - nền tảng của mọi công nghệ phần mềm hiện đại.
- **Tiếp nối sang bài sau ([2. 객체지향](27-bai-hoc.md)):** Khảo sát các trường phái phân tích hướng đối tượng (OOA) kinh điển của Coad-Yourdon, Booch, Jacobson và Rumbaugh.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để ghi nhớ chuẩn xác bẫy phân biệt Overloading (cùng tên khác tham số trong 1 class) vs Overriding (lớp con viết lại hàm lớp cha).
- Đọc TẦNG B để thấy rõ mã nguồn minh họa sự khác nhau giữa Overloading và Overriding trong Java.

---

## 6. 객체지향 (Hướng Đối Tượng - OOP)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Các khái niệm cốt lõi của Lập trình hướng đối tượng (OOP):**
  - **객체 (Object - Đối tượng):**
    - Là thực thể tồn tại trong thế giới thực hoặc bài toán, bao gồm **Dữ liệu trạng thái (`속성 - Attribute/Data`)** và **Hành vi xử lý (`연산/메소드 - Operation/Method`)**.
    - Là một thể hiện cụ thể (Instance) được sinh ra từ một bản thiết kế mẫu (Class).
  - **클래스 (Class - Lớp):**
    - Là khuôn mẫu (Blueprint / Template) trừu tượng định nghĩa tập hợp các thuộc tính và phương thức chung cho các đối tượng cùng loại.
  - **메시지 (Message - Thông điệp):**
    - Là phương thức giao tiếp giữa các đối tượng; một đối tượng gửi yêu cầu ra lệnh cho đối tượng khác thực thi một hành vi mong muốn.
  - **캡슐화 (Encapsulation - Tính đóng gói):**
    - Gom nhóm dữ liệu và các hàm thao tác trên dữ liệu đó vào trong cùng một thực thể duy nhất.
    - **Ý nghĩa:** Tăng tính độc lập của mô-đun, giảm mức độ kết hợp (Coupling), tăng khả năng tái sử dụng.
  - **정보 은닉 (Information Hiding - Che giấu thông tin):**
    - Ẩn giấu chi tiết cấu trúc dữ liệu và cài đặt bên trong đối tượng (khai báo `private`), chỉ cung cấp giao diện công khai (`public`) để bên ngoài truy xuất, bảo vệ dữ liệu khỏi bị thay đổi tùy tiện.
  - **상속성 (Inheritance - Tính kế thừa):**
    - Cơ chế cho phép một lớp con (`자식 클래스 / Subclass`) tự động sở hữu và tái sử dụng toàn bộ thuộc tính và phương thức của lớp cha (`부모 클래스 / Superclass`), đồng thời có thể bổ sung các tính năng mới mà không cần viết lại mã nguồn cũ.
  - **다형성 (Polymorphism - Tính đa hình):**
    - Khả năng cùng một tên thông điệp gửi đi nhưng các đối tượng khác nhau sẽ phản ứng và thực thi theo các cách riêng biệt khác nhau.
- **Phân biệt sống còn: 오버로딩 (Overloading) vs 오버라이딩 (Overriding):**
  - **오버로딩 (Overloading - Nạp chồng):**
    - Diễn ra trong **cùng một lớp (동일 클래스 내)**.
    - Các phương thức có **CÙNG TÊN** nhưng **KHÁC NHAU VỀ DANH SÁCH THAM SỐ** (khác số lượng tham số hoặc khác kiểu dữ liệu của tham số). Kiểu trả về không ảnh hưởng đến nạp chồng.
  - **오버라이딩 (Overriding - Ghi đè):**
    - Diễn ra giữa **Lớp cha và Lớp con (상속 관계)**.
    - Lớp con định nghĩa lại hoàn toàn phần hiện thực (thân hàm) của phương thức đã kế thừa từ lớp cha; phương thức phải **GIỐNG HỆT VỀ TÊN, DANH SÁCH THAM SỐ VÀ KIỂU TRẢ VỀ**.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Trong cùng 1 class, tạo 2 hàm cùng tên nhưng khác kiểu dữ liệu tham số gọi là Overriding?"* -> **Sai hoàn toàn**. Đó là **Overloading (오버로딩)**.
  - **Bẫy 2:** *"Đóng gói (캡슐화) làm tăng độ phụ thuộc giữa các mô-đun?"* -> **Sai**. Đóng gói giúp tăng tính độc lập và **giảm độ kết hợp (결합도 감소)** giữa các mô-đun.
  - **Bẫy 3:** *"Thông điệp (메시지) là gì?"* -> **Là lệnh hoặc yêu cầu chỉ thị cho đối tượng thực hiện một hành vi (객체에게 행위를 하도록 지시하는 명령)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Class là khuôn đúc Object; Đóng gói che giấu thông tin; Overloading cùng lớp khác tham số, Overriding lớp con viết lại hàm cha".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa mã nguồn Java phân biệt Overloading và Overriding:**
  ```java
  // 1. Overloading (Nạp chồng trong cùng class MathUtil)
  class MathUtil {
      public int add(int a, int b) { return a + b; }
      public double add(double a, double b) { return a + b; } // Cùng tên add, khác kiểu tham số
  }

  // 2. Overriding (Ghi đè giữa lớp cha và con)
  class Animal {
      public void makeSound() { System.out.println("Animal sound"); }
  }
  class Dog extends Animal {
      @Override
      public void makeSound() { System.out.println("Gâu gâu"); } // Giống hệt chữ ký, thay đổi thân hàm
  }
  ```

### 복습 체크리스트
- [ ] Phân biệt rõ sự khác nhau giữa 클래스 (khuôn mẫu) và 객체 (thể hiện cụ thể).
- [ ] Giải thích được vai trò của 캡슐화 (Đóng gói) trong việc giảm độ kết hợp giữa các module.
- [ ] Định nghĩa được 정보 은닉 (Che giấu thông tin).
- [ ] Phân biệt được bản chất của 오버로딩 (cùng lớp, khác tham số) và 오버라이딩 (lớp con kế thừa ghi đè).
