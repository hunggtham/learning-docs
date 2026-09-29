# 2. 객체지향 (OOP - Object Oriented Programming)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **2. 객체지향 (OOP - Object Oriented Programming)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **2. 객체지향 (OOP - Object Oriented Programming)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **1. 객체지향 설계 5대 원칙 (SOLID)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

객체지향

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **15. 객체지향 및 모듈화 방법론 (Phương pháp luận OOP & Mô-đun hóa)**에서 만든 기준을 이어받아 **2. 객체지향 (OOP - Object Oriented Programming)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 2. 객체지향 (OOP - Object Oriented Programming)

Ở bước 28/55, **2. 객체지향 (OOP - Object Oriented Programming)** xuất hiện như phần tiếp nối của **15. 객체지향 및 모듈화 방법론 (Phương pháp luận OOP & Mô-đun hóa)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **2. 객체지향 (OOP - Object Oriented Programming)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **구성요소**, **객체지향 기법 (OOP Techniques)**, **캡슐화 (Encapsulation)**, **정보 은닉 (Information Hiding)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **구성요소**: 클래스 (Class), 객체 (Object), 메서드 (Method), 메시지 (Message), 인스턴스 (Instance), 속성 (Property).
- **객체지향 기법 (OOP Techniques)**:
  - **캡슐화 (Encapsulation)**: Đóng gói dữ liệu và phương thức, giảm kết dính (Coupling).
  - **정보 은닉 (Information Hiding)**: Giấu thông tin chi tiết.
  - **다형성 (Polymorphism)**: Đa hình (Overloading - Cùng tên khác tham số, Overriding - Ghi đè phương thức cha).
- **객체지향 설계 원칙 (SOLID)**:
  - **S (SRP)**: Đơn trách nhiệm (Một lớp một việc).
  - **O (OCP)**: Đóng-Mở (Mở rộng thì dễ, sửa đổi thì cấm).
  - **L (LSP)**: Thay thế Liskov (Lớp con thay thế được lớp cha).
  - **I (ISP)**: Phân tách Interface (Interface nhỏ gọn).
  - **D (DIP)**: Đảo ngược phụ thuộc (Phụ thuộc vào Interface, không phụ thuộc vào triển khai chi tiết).
- **분석 방법론 (OOA Methods)**:
  - **람바우 (Rumbaugh - OMT)**: 객체 모형 (Object) -> 동적 모형 (Dynamic) -> 기능 모형 (Functional - DFD). 
  - 💡 **Mẹo ghi nhớ**: K/Đ/C -> **Không Đợi Chờ**

Như vậy, **2. 객체지향 (OOP - Object Oriented Programming)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **1. 객체지향 설계 5대 원칙 (SOLID)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.