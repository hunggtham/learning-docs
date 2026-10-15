# 079. 프로그래밍 언어의 종류 (Types of Programming Languages)

## 학습 목표 (Mục tiêu)
- Nắm vững phân loại và đặc trưng bản chất của 3 mô hình ngôn ngữ lập trình chủ đạo: Hướng thủ tục (절차적 언어), Hướng đối tượng (객체지향 언어), và Kịch bản / Thông dịch (스크립트 언어).
- Phân biệt cơ chế thực thi, quản lý bộ nhớ và môi trường ứng dụng của từng nhóm ngôn ngữ đại diện: C, Java, Python, JavaScript, và PHP.
- Nhận diện các đặc trưng cú pháp riêng biệt thường gặp trong câu hỏi thi (ví dụ: ký hiệu `@` bỏ qua lỗi trong PHP, mô hình Prototype trong JavaScript, Garbage Collector trong Java).

## 핵심 키워드 (Từ khóa)
- 프로그래밍 언어 분류 (Language Classifications)
- 절차적 언어 (Procedural: C, FORTRAN, ALGOL, COBOL)
- 객체지향 언어 (OOP: C++, Java, Smalltalk)
- 스크립트 언어 (Scripting: Python, JS, PHP, Shell)
- 컴파일 언어 vs 인터프리터 언어 (Compiled vs Interpreted)
- PHP `@` 연산자 (Error Control Operator)
- 자바스크립트 프로토타입 (JavaScript Prototype-based OO)
- 가비지 컬렉터 (Garbage Collector)

## 선행·연결 개념 (Kiến thức liên kết)
- [71-bai-hoc.md](71-bai-hoc.md): Định nghĩa hàm và lớp đối tượng trong Java và Python.
- [73-bai-hoc.md](73-bai-hoc.md): Thuật toán thay thế trang nhớ trong hệ điều hành (Page Replacement).
- [53-bai-hoc.md](53-bai-hoc.md): Lịch sử và đặc điểm các ngôn ngữ lập trình hướng thủ tục.

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh theo mô hình thực thi:
  - Ngôn ngữ biên dịch (Compile): C, C++, Go $\rightarrow$ Chuyển toàn bộ mã nguồn thành mã máy nhị phân trước khi chạy, tốc độ cực nhanh.
  - Ngôn ngữ thông dịch (Interpreter / Script): Python, JavaScript, PHP $\rightarrow$ Dịch và thực thi từng dòng lệnh tại thời gian chạy (Runtime), mềm dẻo, dễ sửa nhưng tốc độ chậm hơn.
  - Ngôn ngữ lai (Hybrid): Java, C# $\rightarrow$ Biên dịch mã nguồn ra Bytecode trung gian, sau đó máy ảo (JVM / CLR) thông dịch hoặc biên dịch JIT khi chạy.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng phân loại 3 họ ngôn ngữ lập trình chính:**

| Họ ngôn ngữ | Đại diện tiêu biểu | Cơ chế hoạt động & Triết lý thiết kế | Đặc điểm kỹ thuật nổi bật |
| :--- | :--- | :--- | :--- |
| **Hướng thủ tục** (Procedural) | **C, FORTRAN, COBOL, ALGOL, Pascal** | Chia nhỏ chương trình thành các hàm/thủ tục (Procedure/Function) thực thi tuần tự từ trên xuống dưới. | Quản lý bộ nhớ thủ công, hiệu năng cao, gần gũi với phần cứng máy tính. |
| **Hướng đối tượng** (Object-Oriented) | **C++, Java, C#, Smalltalk** | Đóng gói trạng thái (dữ liệu) và hành vi (phương thức) vào các thực thể đối tượng. | Hỗ trợ 4 trụ cột: Đóng gói, Kế thừa, Đa hình, Trừu tượng hóa; tích hợp bộ dọn rác tự động (Java JVM GC). |
| **Kịch bản / Thông dịch** | **Python, JavaScript, PHP, Bash** | Không cần bước biên dịch độc lập ra tệp nhị phân `.exe`, mã nguồn được đọc và chạy trực tiếp bởi trình thông dịch. | Phát triển cực nhanh; định kiểu động (Dynamic Typing); dễ bảo trì và nhúng vào hệ thống khác. |

- **2. Điểm nhấn thi cử của các ngôn ngữ kịch bản phổ biến:**
  - **PHP:** Chuyên dụng cho phát triển ứng dụng web phía máy chủ (Server-side). Trong PHP, ký tự `@` đặt trước một biểu thức hoặc hàm (ví dụ: `@unlink(...)`) có tác dụng **bỏ qua / ngăn chặn hiển thị thông báo lỗi (Error Control Operator)** nếu lệnh đó thất bại.
  - **JavaScript:** Ngôn ngữ kịch bản ban đầu chạy trên trình duyệt máy khách (Client-side), xây dựng mô hình đối tượng dựa trên chuỗi nguyên mẫu (**Prototype-based Inheritance**) thay vì cấu trúc Class truyền thống.
  - **Python:** Ngôn ngữ mã nguồn mở có cú pháp trong sáng, dùng thụt lề (Indentation) thay cho cặp ngoặc nhọn `{ }`, hỗ trợ đa hình thái lập trình (cả thủ tục, hướng đối tượng và hàm số).

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Garbage Collection trong ngôn ngữ hiện đại:**
  - Trong các ngôn ngữ hướng thủ tục bậc thấp như C, lập trình viên phải tự cấp phát bộ nhớ bằng `malloc()` và bắt buộc phải gọi `free()`. Nếu quên, bộ nhớ sẽ bị rò rỉ (Memory Leak). Các ngôn ngữ OOP hiện đại như Java và ngôn ngữ script như Python đều tích hợp trình gom rác (Garbage Collector) ngầm định, tự động thu hồi RAM của các biến không còn tham chiếu.

### 복습 체크리스트
- [ ] Phân loại chính xác các ngôn ngữ: C/FORTRAN (Thủ tục), Java/C++ (OOP), Python/JS/PHP (Script).
- [ ] Nhớ trong PHP tiền tố `@` được dùng để tắt và bỏ qua cảnh báo lỗi.
- [ ] Nhớ JavaScript hỗ trợ mô hình hướng đối tượng dựa trên Prototype.
- [ ] Hiểu rõ sự khác nhau giữa cơ chế biên dịch trước (Compiler) và thông dịch trực tiếp từng dòng (Interpreter).
