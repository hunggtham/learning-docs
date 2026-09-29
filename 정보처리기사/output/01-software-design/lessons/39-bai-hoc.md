# 11. 디자인 패턴 (Design Pattern)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **11. 디자인 패턴 (Design Pattern)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **11. 디자인 패턴 (Design Pattern)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

디자인, 패턴

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **4. 디자인 패턴 (Design Patterns - GoF)**에서 만든 기준을 이어받아 **11. 디자인 패턴 (Design Pattern)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 11. 디자인 패턴 (Design Pattern)

Từ **4. 디자인 패턴 (Design Patterns - GoF)**, ta đã có điểm tựa để bước vào **11. 디자인 패턴 (Design Pattern)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 39/55 trước khi đi vào chi tiết.

Để đọc **11. 디자인 패턴 (Design Pattern)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

**개념 (Khái niệm):** 설계 시 참조할 수 있는 전형적인 해결 방식 (Các mẫu giải pháp tiêu chuẩn dùng tham khảo khi thiết kế phần mềm). GoF (Gang of Four)가 23개로 체계화.
💡 **Mẹo ghi nhớ:** "바퀴를 다시 발명하지 마라 (Don't reinvent the wheel)" - Đừng phát minh lại bánh xe, hãy dùng các mẫu đã được kiểm chứng.

*   **장단점 (Ưu & Nhược điểm):**
    *   장점: 구조 파악 용이, 의사소통 원활, 생산성 향상 (Dễ nắm cấu trúc, giao tiếp tốt, tăng năng suất).
    *   단점: **초기 투자 비용 부담**, 객체지향 전용 (Tốn chi phí/thời gian học ban đầu, chỉ hợp với Hướng đối tượng).

Để không đọc **11.1 생성 패턴 (Creational - 5개)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 11.1 생성 패턴 (Creational - 5개)

Các ý ngay dưới **11.1 생성 패턴 (Creational - 5개)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

객체 생성 캡슐화 (Đóng gói quá trình tạo đối tượng).
1.  **추상 팩토리 (Abstract Factory):** 연관된 객체 그룹 생성 (Tạo nhóm đối tượng liên quan).
2.  **빌더 (Builder):** 생성 과정과 표현 방법 분리 (Tách quá trình xây dựng và biểu diễn).
3.  **팩토리 메소드 (Factory Method):** 객체 생성을 서브 클래스에 위임, 가상 생성자 (Giao việc tạo đối tượng cho lớp con).
4.  **프로토타입 (Prototype):** 원본 객체 복제 (Nhân bản đối tượng nguyên mẫu Clone).
5.  **싱글톤 (Singleton):** 인스턴스가 하나뿐임을 보장 (Đảm bảo chỉ có 1 instance duy nhất).

Phần **11.1 생성 패턴 (Creational - 5개)** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Ta vừa chốt **11.1 생성 패턴 (Creational - 5개)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **11.2 구조 패턴 (Structural - 7개)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **11.2 구조 패턴 (Structural - 7개)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 11.2 구조 패턴 (Structural - 7개)

Bây giờ ta đi vào nội dung của **11.2 구조 패턴 (Structural - 7개)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

객체 조합으로 더 큰 구조 생성 (Kết hợp đối tượng thành cấu trúc lớn hơn).
1.  **어댑터 (Adapter):** 호환 안 되는 인터페이스 변환 (Chuyển đổi interface không tương thích).
2.  **브리지 (Bridge):** 구현과 추상층 분리 (Tách biệt phần triển khai và phần trừu tượng).
3.  **컴포지트 (Composite):** 트리 구조, 단일/복합 객체 동일하게 다룸 (Cấu trúc cây, xử lý đối tượng đơn và phức như nhau).
4.  **데코레이터 (Decorator):** 동적으로 기능 덧붙임 (Thêm chức năng linh hoạt bằng cách bọc đối tượng).
5.  **퍼싸드 (Facade):** 복잡한 서브 시스템 위에 통합 인터페이스(Wrapper) 제공 (Tạo mặt tiền/giao diện chung đơn giản cho hệ thống phức tạp).
6.  **플라이웨이트 (Flyweight):** 인스턴스 공유로 메모리 절약 (Chia sẻ đối tượng để tiết kiệm bộ nhớ).
7.  **프록시 (Proxy):** 접근 어려운 객체를 대리 수행 (Đại diện/ủy quyền truy cập cho đối tượng khác).

Phần **11.2 구조 패턴 (Structural - 7개)** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Sau khi đọc **11.2 구조 패턴 (Structural - 7개)**, đừng bắt đầu lại từ số không. **11.3 행위 패턴 (Behavioral - 11개)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **11.3 행위 패턴 (Behavioral - 11개)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 11.3 행위 패턴 (Behavioral - 11개)

Phần nguồn của **11.3 행위 패턴 (Behavioral - 11개)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

객체 간 상호작용 및 책임 분배 (Tương tác và phân chia trách nhiệm giữa các đối tượng).
1.  **책임 연쇄 (Chain of Responsibility):** 고리를 따라 책임 넘김 (Truyền yêu cầu theo chuỗi xử lý).
2.  **커맨드 (Command):** 요청을 객체로 캡슐화 (로그, Undo) (Đóng gói yêu cầu thành đối tượng, tiện cho Undo/Log).
3.  **인터프리터 (Interpreter):** 언어 문법 정의 (Định nghĩa cú pháp ngôn ngữ).
4.  **반복자 (Iterator):** 내부 노출 없이 순차 접근 (Truy cập tuần tự không lộ cấu trúc).
5.  **중재자 (Mediator):** 복잡한 상호작용을 통제/지시 (Điều phối viên trung gian để giảm phụ thuộc chéo).
6.  **메멘토 (Memento):** 상태 스냅샷 저장/복원 (Lưu trạng thái để Undo/Khôi phục).
7.  **옵서버 (Observer):** 상태 변화를 구독자에게 전파 (Publish/Subscribe, thông báo khi có thay đổi).
8.  **상태 (State):** 상태에 따라 다른 동작 (Hành vi thay đổi theo trạng thái).
9.  **전략 (Strategy):** 알고리즘 캡슐화하여 교체 가능 (Đóng gói thuật toán, dễ dàng hoán đổi).
10. **템플릿 메소드 (Template Method):** 상위가 골격, 하위가 세부 구현 (Lớp cha tạo khung, lớp con điền chi tiết).
11. **방문자 (Visitor):** 처리 기능을 분리하여 방문 수행 (Tách logic xử lý ra khỏi cấu trúc dữ liệu, đi "thăm" từng phần tử).

---

Phần **11.3 행위 패턴 (Behavioral - 11개)** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Như vậy, **11.3 행위 패턴 (Behavioral - 11개)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Điểm chốt của **11. 디자인 패턴 (Design Pattern)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.