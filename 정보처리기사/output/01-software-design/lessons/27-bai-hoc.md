# 2. 객체지향 (OOP - Object Oriented Programming)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **2. 객체지향 (OOP - Object Oriented Programming)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối OOP với object, encapsulation, inheritance và polymorphism, để mô hình hóa gắn với trách nhiệm và thay đổi.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **2. 객체지향 (OOP - Object Oriented Programming)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **2. 객체지향 (OOP - Object Oriented Programming)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **1. 객체지향 설계 5대 원칙 (SOLID)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **2. 객체지향 (OOP - Object Oriented Programming)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

객체지향

> **Chuyển mạch:** Ở chặng này của **2. 객체지향 (OOP - Object Oriented Programming)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **6. 객체지향 (Hướng Đối Tượng - OOP)**에서 만든 기준을 이어받아 **2. 객체지향 (OOP - Object Oriented Programming)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **2. 객체지향 (OOP - Object Oriented Programming)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **2. 객체지향 (OOP - Object Oriented Programming)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **2. 객체지향 (OOP - Object Oriented Programming)**, **2. 객체지향 (OOP - Object Oriented Programming)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 2. 객체지향 (OOP - Object Oriented Programming)

Từ **6. 객체지향 (Hướng Đối Tượng - OOP)**, ta đã có điểm tựa để bước vào **2. 객체지향 (OOP - Object Oriented Programming)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 27/69 trước khi đi vào chi tiết.

Để đọc **2. 객체지향 (OOP - Object Oriented Programming)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **구성요소**, **객체지향 기법 (OOP Techniques)**, **캡슐화 (Encapsulation)**, **정보 은닉 (Information Hiding)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “2. 객체지향 (OOP - Object Oriented Programming)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

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

Điểm chốt của **2. 객체지향 (OOP - Object Oriented Programming)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **1. 객체지향 설계 5대 원칙 (SOLID)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.

> **Bàn giao:** Sau **2. 객체지향 (OOP - Object Oriented Programming)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
