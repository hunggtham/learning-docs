# 7. UML 심화 (Advanced UML)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **7. UML 심화 (Advanced UML)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **7. UML 심화 (Advanced UML)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **4. 사용자 인터페이스 (Giao diện người dùng - UI)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

UML, 심화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **5. UML 구성요소 상세 (UML Components Detail)**에서 만든 기준을 이어받아 **7. UML 심화 (Advanced UML)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 7. UML 심화 (Advanced UML)

Ở bước 16/55, **7. UML 심화 (Advanced UML)** xuất hiện như phần tiếp nối của **5. UML 구성요소 상세 (UML Components Detail)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **7. UML 심화 (Advanced UML)** như một bài học cho người mới, hãy giữ câu hỏi: **ta dùng mô hình nào để biểu diễn đối tượng, quan hệ hoặc hành vi, và giới hạn của mỗi cách là gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể. Trong khối này, **다이어그램 (Diagrams)**, **스테레오 타입 (Stereotype)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- Do OMG chuẩn hóa từ phương pháp của Rumbaugh, Booch, Jacobson.
- **다이어그램 (Diagrams)**:
  - 구조적 (Structural / Tĩnh): Class, Object, Component, Deployment, Composite, Package.
  - 행위적 (Behavioral / Động): Use Case, Sequence, Communication, State, Activity, Timing.
- **스테레오 타입 (Stereotype)**: Mở rộng UML bằng dấu `<< >>` (Guillemet). Ví dụ: `<<include>>`, `<<extend>>`.

Như vậy, **7. UML 심화 (Advanced UML)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **4. 사용자 인터페이스 (Giao diện người dùng - UI)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.