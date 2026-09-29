# 4. UML (Unified Modeling Language)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **4. UML (Unified Modeling Language)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **4. UML (Unified Modeling Language)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **5. UML 구성요소 상세 (UML Components Detail)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

UML

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **11. 모델링 및 다이어그램 심화 (Mô hình hóa & Biểu đồ chuyên sâu)**에서 만든 기준을 이어받아 **4. UML (Unified Modeling Language)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 4. UML (Unified Modeling Language)

Sau khi đã đặt nền bằng **11. 모델링 및 다이어그램 심화 (Mô hình hóa & Biểu đồ chuyên sâu)**, ta chuyển sang **4. UML (Unified Modeling Language)**. Đây là mắt xích 14/55 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **4. UML (Unified Modeling Language)** như một bài học cho người mới, hãy giữ câu hỏi: **ta dùng mô hình nào để biểu diễn đối tượng, quan hệ hoặc hành vi, và giới hạn của mỗi cách là gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **개념**, **구성요소**, **관계 (Relationships)**, **다이어그램 (Diagrams)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **개념**: Ngôn ngữ mô hình hóa hướng đối tượng chuẩn.
- **구성요소**: 사물 (Things), 관계 (Relationships), 다이어그램 (Diagrams).
- **관계 (Relationships)**: 
  - 연관 (Association), 의존 (Dependency), 집합 (Aggregation), 포함 (Composition), 일반화 (Generalization - Kế thừa), 실체화 (Realization - Interface).
- **다이어그램 (Diagrams)**:
  - **구조적/정적 (Structural/Static)**: Class, Object, Component, Deployment, Composite Structure, Package.
  - **행위적/동적 (Behavioral/Dynamic)**: Use Case, Sequence, Communication, State, Activity, Timing.
- 💡 **Mẹo ghi nhớ**: 
  - 정적 다이어그램: 클/객/컴/배/복/패 (Class, Object, Component, Deployment, Composite, Package)
  - 동적 다이어그램: 유/순/커/상/활/타 (Use case, Sequence, Comm, State, Activity, Timing)

Ta có thể khép mục **4. UML (Unified Modeling Language)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **5. UML 구성요소 상세 (UML Components Detail)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.