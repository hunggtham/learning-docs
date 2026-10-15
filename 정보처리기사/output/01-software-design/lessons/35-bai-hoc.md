# 8. 디자인 패턴 (Design Patterns)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, nguồn gốc và lợi ích của Mẫu thiết kế phần mềm (`디자인 패턴 - Design Patterns`) do nhóm GoF (Gang of Four) hệ thống hóa thành 23 mẫu kinh điển.
- Phân loại tuyệt đối 23 mẫu thiết kế thành 3 nhóm lớn: Nhóm khởi tạo (`생성 패턴` - 5 mẫu), Nhóm cấu trúc (`구조 패턴` - 7 mẫu), và Nhóm hành vi (`행위 패턴` - 11 mẫu).
- Thuộc nằm lòng các câu thần chú nhận diện nhanh nhóm của từng mẫu thiết kế trong đề thi trắc nghiệm.

## 핵심 키워드 (Từ khóa)
- GoF 디자인 패턴 (Gang of Four 23 Design Patterns)
- 생성 패턴 (Creational Patterns - 5: Abstract Factory, Builder, Factory Method, Prototype, Singleton)
- 구조 패턴 (Structural Patterns - 7: Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy)
- 행위 패턴 (Behavioral Patterns - 11: Chain of Responsibility, Command, Interpreter, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor)
- 재사용성 / 유지보수성 (Reusability / Maintainability)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([9. 소프트웨어 품질 특성 (ISO/IEC 9126)](34-bai-hoc.md)):** Sau khi xem xét các tiêu chuẩn chất lượng (Dễ bảo trì, Dễ mở rộng), bài này trang bị bộ công cụ giải pháp mẫu chuẩn hóa để đạt được các tiêu chuẩn đó.
- **Tiếp nối sang bài sau ([4. 디자인 패턴 (Design Patterns - GoF)](36-bai-hoc.md)):** Khảo sát chi tiết phân loại và ngữ cảnh áp dụng thực tế của từng nhóm mẫu.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc 2 bài thơ thần chú phân loại: Tạo dựng gồm 5 (추-빌-팩-프-싱), Cấu trúc gồm 7 (어-브-컴-데-퍼-플-프) - dạng câu hỏi "Mẫu nào sau đây KHÔNG THUỘC nhóm cấu trúc?" xuất hiện liên tục trong đề thi.
- Đọc TẦNG B để hiểu triết lý "Đừng phát minh lại bánh xe" (Don't reinvent the wheel) khi áp dụng Design Patterns vào dự án thực tế.

---

## 8. 디자인 패턴 (Design Patterns)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **개념 (Định nghĩa Mẫu thiết kế GoF):**
  - Là tập hợp các giải pháp thiết kế tiêu chuẩn đã được chứng minh hiệu quả trong thực tế, dùng để giải quyết các vấn đề thường xuyên lặp lại trong quá trình thiết kế phần mềm hướng đối tượng do nhóm 4 tác giả GoF (Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides) tổng hợp thành **23 mẫu kinh điển**.
- **Phân loại 23 mẫu thiết kế GoF thành 3 nhóm mục đích:**
  - **1. 생성 패턴 (Creational Patterns - Nhóm khởi tạo - 5 mẫu):**
    - Trọng tâm: Cơ chế tạo lập đối tượng một cách linh hoạt, che giấu quá trình khởi tạo cụ thể bên trong.
    - 5 mẫu cốt lõi:
      1. `Abstract Factory (추상 팩토리)`: Tạo ra các họ đối tượng liên quan mà không chỉ định lớp cụ thể.
      2. `Builder (빌더)`: Tách rời quá trình xây dựng đối tượng phức tạp khỏi biểu diễn của nó.
      3. `Factory Method (팩토리 메소드)`: Giao việc khởi tạo đối tượng cụ thể cho các lớp con.
      4. `Prototype (프로토타입)`: Tạo ra đối tượng mới bằng cách sao chép nhân bản (Clone) từ một đối tượng mẫu có sẵn.
      5. `Singleton (싱글톤)`: Đảm bảo một lớp chỉ có duy nhất một thể hiện (Instance) trong toàn bộ ứng dụng và cung cấp điểm truy cập toàn cục.
    - 💡 **Thần chú nhớ 5 mẫu khởi tạo:** **추 - 빌 - 팩 - 프 - 싱** (Chuẩn Bị Phê Pha Sớm).
  - **2. 구조 패턴 (Structural Patterns - Nhóm cấu trúc - 7 mẫu):**
    - Trọng tâm: Kết hợp các lớp (Classes) và đối tượng (Objects) thành các cấu trúc lớn hơn, linh hoạt hơn.
    - 7 mẫu cốt lõi:
      1. `Adapter (어댑터)`: Chuyển đổi giao diện không tương thích thành giao diện mà client mong đợi.
      2. `Bridge (브리지)`: Tách rời phần trừu tượng khỏi phần hiện thực để cả hai có thể thay đổi độc lập.
      3. `Composite (컴포지트)`: Xây dựng cấu trúc cây biểu diễn phân cấp toàn thể - bộ phận, coi đối tượng đơn và nhóm đối tượng như nhau.
      4. `Decorator (데코레이터)`: Bổ sung trách nhiệm mới cho đối tượng một cách linh hoạt trong thời gian chạy (Runtime) thay vì kế thừa.
      5. `Facade (퍼사드)`: Cung cấp một giao diện đơn giản duy nhất để giao tiếp với cả một hệ thống con (Subsystem) phức tạp bên trong.
      6. `Flyweight (플라이웨이트)`: Chia sẻ trạng thái chung giữa nhiều đối tượng nhỏ để tiết kiệm bộ nhớ RAM.
      7. `Proxy (프록시)`: Tạo đối tượng đại diện thay thế để kiểm soát quyền truy cập hoặc trì hoãn nạp đối tượng thật.
    - 💡 **Thần chú nhớ 7 mẫu cấu trúc:** **어 - 브 - 컴 - 데 - 퍼 - 플 - 프** (Anh Bảo Chú Đừng Phá Phách Phòng).
  - **3. 행위 패턴 (Behavioral Patterns - Nhóm hành vi - 11 mẫu):**
    - Trọng tâm: Phân chia trách nhiệm, thuật toán và luồng giao tiếp tương tác giữa các đối tượng.
    - 11 mẫu cốt lõi:
      - `Chain of Responsibility (책임 연쇄)`, `Command (커맨드)`, `Interpreter (인터프리터)`, `Iterator (반복자)`, `Mediator (중재자)`, `Memento (메멘토)`, `Observer (옵서버)`, `State (상태)`, `Strategy (전략)`, `Template Method (템플릿 메소드)`, `Visitor (방문자)`.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Mẫu thiết kế nào thuộc nhóm Tạo dựng (생성 패턴)?"* -> Ghi nhớ 5 mẫu: **Abstract Factory, Builder, Factory Method, Prototype, Singleton**. Các mẫu còn lại không thuộc nhóm này.
  - **Bẫy 2:** *"Decorator và Facade thuộc nhóm mẫu thiết kế nào?"* -> **구조 패턴 (Nhóm cấu trúc - Structural Patterns)**.
  - **Bẫy 3:** *"Observer và Strategy thuộc nhóm mẫu thiết kế nào?"* -> **행위 패턴 (Nhóm hành vi - Behavioral Patterns)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "GoF có 23 mẫu: Tạo dựng có 5 (추빌팩프싱), Cấu trúc có 7 (어브컴데퍼플프), Hành vi có 11 mẫu điều phối tương tác".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ý nghĩa thực tiễn của việc sử dụng Design Patterns:**
  - Tiết kiệm thời gian thiết kế vì không phải giải lại các bài toán kiến trúc kinh điển.
  - Giúp việc giao tiếp giữa các kỹ sư phần mềm trở nên cô đọng và chính xác (chỉ cần nói "chỗ này áp dụng Singleton và Observer", cả nhóm đều hiểu ngay cấu trúc mã nguồn mà không cần giải thích dài dòng).
  - Tăng độ bền vững của mã nguồn theo đúng các nguyên tắc SOLID.

### 복습 체크리스트
- [ ] Nhớ tên nhóm tác giả GoF và tổng số 23 mẫu thiết kế.
- [ ] Đọc tên đủ 5 mẫu tạo dựng (생성 패턴): Abstract Factory, Builder, Factory Method, Prototype, Singleton.
- [ ] Đọc tên đủ 7 mẫu cấu trúc (구조 패턴): Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy.
- [ ] Nhận diện được các mẫu phổ biến thuộc nhóm hành vi (Observer, Strategy, Template Method, Command).
