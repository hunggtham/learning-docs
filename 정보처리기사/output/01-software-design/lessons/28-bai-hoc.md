# 1. 객체지향 설계 5대 원칙 (SOLID)

## 학습 목표 (Mục tiêu)
- Nắm vững bản chất, mục đích và định nghĩa chuẩn xác của 5 nguyên tắc thiết kế hướng đối tượng vàng (`SOLID 원칙`) do Robert C. Martin đúc kết.
- Phân biệt rõ ý nghĩa từng nguyên tắc: `SRP` (Đơn trách nhiệm), `OCP` (Đóng/Mở), `LSP` (Thay thế Liskov), `ISP` (Phân tách giao diện), và `DIP` (Đảo ngược phụ thuộc).
- Nhận diện các vi phạm thiết kế SOLID kinh điển thông qua các ví dụ thực tế và câu hỏi tình huống trong đề thi.

## 핵심 키워드 (Từ khóa)
- 객체지향 설계 원칙 (Nguyên tắc thiết kế hướng đối tượng / SOLID Principles)
- SRP (Single Responsibility Principle / 단일 책임 원칙)
- OCP (Open-Closed Principle / 개방-폐쇄 원칙)
- LSP (Liskov Substitution Principle / 리스코프 치환 원칙)
- ISP (Interface Segregation Principle / 인터페이스 분리 원칙)
- DIP (Dependency Inversion Principle / 의존 역전 원칙)
- 추상화 / 인터페이스 (Trừu tượng hóa / Interface)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([2. 객체지향](27-bai-hoc.md)):** Sau khi xem xét các phương pháp phân tích OOA (Rumbaugh, Booch), bài này chuyển sang giai đoạn thiết kế kiến trúc mã nguồn sạch, bền vững với bộ quy tắc SOLID.
- **Tiếp nối sang bài sau ([7. 설계 도구 및 모듈화 심화](29-bai-hoc.md)):** Mở rộng các nguyên lý thiết kế sang công cụ trực quan hóa lưu đồ N-S và các kỹ thuật mô-đun hóa độc lập.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc nằm lòng tên tiếng Hàn, tên tiếng Anh và định nghĩa 1 câu của từng nguyên tắc trong bộ 5 chữ cái SOLID.
- Đọc TẦNG B để phân tích ví dụ kinh điển vi phạm LSP (Bài toán Hình chữ nhật và Hình vuông) và giải pháp khắc phục bằng Interface.

---

## 1. 객체지향 설계 5대 원칙 (SOLID)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng 5 nguyên tắc thiết kế hướng đối tượng SOLID:**
  1. **SRP (Single Responsibility Principle - 단일 책임 원칙):**
     - **Định nghĩa:** Mỗi một đối tượng hoặc lớp chỉ nên gánh vác **DUY NHẤT MỘT TRÁCH NHIỆM (`단 하나의 책임만 가져야 함`)**.
     - **Hệ quả:** Một lớp chỉ nên có một lý do duy nhất để thay đổi. Tăng độ gắn kết (Cohesion), giảm kích thước lớp, giúp mã nguồn dễ hiểu và dễ bảo trì.
  2. **OCP (Open-Closed Principle - 개방-폐쇄 원칙):**
     - **Định nghĩa:** Phần mềm cần phải **Mở đối với việc mở rộng (`확장에는 열려 있고`)** nhưng **Đóng đối với việc chỉnh sửa (`수정에는 닫혀 있어야 함`)**.
     - **Cách hiện thực:** Khi có yêu cầu nghiệp vụ mới, ta bổ sung thêm lớp mới (bằng cách kế thừa hoặc cài đặt Interface mới) chứ không được can thiệp sửa đổi các dòng code cũ đang vận hành ổn định.
  3. **LSP (Liskov Substitution Principle - 리스코프 치환 원칙):**
     - **Định nghĩa:** Lớp con (`자식 클래스`) phải có khả năng **thay thế hoàn toàn cho lớp cha (`부모 클래스`) mà không làm thay đổi tính đúng đắn hay phá vỡ hành vi kỳ vọng** của chương trình.
     - **Hệ quả:** Quan hệ kế thừa phải là quan hệ "is-a" thực chất về mặt hành vi, không chỉ là kế thừa cú pháp để tái sử dụng mã.
  4. **ISP (Interface Segregation Principle - 인터페이스 분리 원칙):**
     - **Định nghĩa:** Khách hàng không nên bị ép buộc phải phụ thuộc vào các phương thức giao diện (`인터페이스`) mà họ hoàn toàn không sử dụng đến.
     - **Cách hiện thực:** Thay vì tạo ra một Interface khổng lồ đa năng (Fat Interface), ta nên chia nhỏ thành nhiều Interface chuyên biệt, đơn mục đích (`클라이언트에 특화된 여러 개의 인터페이스로 분리`).
  5. **DIP (Dependency Inversion Principle - 의존 역전 원칙):**
     - **Định nghĩa:** Các mô-đun cấp cao (`상위 모듈`) không nên phụ thuộc trực tiếp vào các mô-đun cấp thấp (`하위 모듈`); **cả hai đều phải phụ thuộc vào sự trừu tượng (`추상화 / 인터페이스`)**.
     - **Hệ quả:** Chi tiết cài đặt cụ thể phải phụ thuộc vào giao diện trừu tượng, không được làm ngược lại.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Nguyên tắc nào quy định khi thêm chức năng mới thì tạo class mới mở rộng mà không sửa code cũ?"* -> **OCP (개방-폐쇄 원칙)**.
  - **Bẫy 2:** *"Lớp con phải thay thế được lớp cha mà chương trình vẫn chạy đúng là nguyên tắc nào?"* -> **LSP (리스코프 치환 원칙)**.
  - **Bẫy 3:** *"Chia nhỏ interface đồ sộ thành các interface chuyên biệt là nguyên tắc nào?"* -> **ISP (인터페이스 분리 원칙)**.
  - **Bẫy 4:** *"Phụ thuộc vào Interface thay vì phụ thuộc vào Class cài đặt cụ thể là nguyên tắc nào?"* -> **DIP (의존 역전 원칙)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "SOLID: S đơn trách nhiệm, O mở rộng đóng sửa, L con thế chỗ cha, I chia nhỏ interface, D phụ thuộc trừu tượng".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Phân tích bẫy vi phạm kinh điển trong đề thi:**
  - **Vi phạm SRP:** Lớp `User` vừa có hàm `saveToDB()` (lưu cơ sở dữ liệu), vừa có hàm `sendEmail()` (gửi mail), vừa có hàm `validateInput()` (kiểm tra form). Khi đổi cấu hình server email, ta phải mở file `User.java` ra sửa -> Sai! Phải tách thành `UserRepository`, `EmailService`, và `UserValidator`.
  - **Vi phạm LSP (Bài toán Cánh cụt - Chim):** Lớp cha `Bird` có hàm `fly()`. Lớp con `Penguin` (Chim cánh cụt) kế thừa `Bird` nhưng không biết bay, đành ném ra ngoại lệ `throw new CannotFlyException()`. Khi chương trình duyệt danh sách chim và gọi `b.fly()`, gặp chim cánh cụt chương trình lập tức bị crash -> Vi phạm LSP vì con không thay thế được cha.
  - **Tuân thủ DIP bằng Dependency Injection (DI):**
    ```java
    // Thay vì phụ thuộc trực tiếp vào MySQLDatabase (하위 모듈 cụ thể):
    // class OrderService { private MySQLDatabase db = new MySQLDatabase(); } // Sai DIP!

    // Phụ thuộc vào interface Database (추상화):
    class OrderService {
        private Database db; // Interface
        public OrderService(Database db) { this.db = db; } // Đúng DIP!
    }
    ```

### 복습 체크리스트
- [ ] Đọc tên tiếng Anh và tiếng Hàn đầy đủ của 5 chữ cái SOLID (SRP, OCP, LSP, ISP, DIP).
- [ ] Nêu định nghĩa cốt lõi của SRP (một trách nhiệm, một lý do thay đổi).
- [ ] Giải thích được nguyên tắc OCP (Mở mở rộng, Đóng chỉnh sửa).
- [ ] Phân tích được ví dụ vi phạm LSP khi lớp con phá vỡ hành vi lớp cha.
- [ ] Nhớ DIP là phụ thuộc vào trừu tượng (Interface) chứ không phụ thuộc vào chi tiết cụ thể.
