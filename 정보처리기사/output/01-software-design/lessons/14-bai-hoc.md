# 3. 모델링 및 UML (Mô hình hóa và UML)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, lịch sử và vai trò của Ngôn ngữ mô hình hóa thống nhất (`UML - Unified Modeling Language`) trong kỹ nghệ phần mềm hướng đối tượng.
- Thuộc nằm lòng 3 thành phần nền tảng của UML: Sự vật (`사물 - Things`), Mối quan hệ (`관계 - Relationships`), và Biểu đồ (`다이어그램 - Diagrams`).
- Phân biệt tuyệt đối giữa nhóm Biểu đồ cấu trúc tĩnh (`구조적/정적 다이어그램` - 6 loại) và nhóm Biểu đồ hành vi động (`행위적/동적 다이어그램` - 7 loại).
- Hiểu khái niệm Stereotype và cách biểu diễn bằng dấu ngoặc kép `<< >>` (Guillemet) cùng sự khác biệt giữa Tác nhân chính (`주액터`) và Tác nhân phụ (`부액터`).

## 핵심 키워드 (Từ khóa)
- UML (Unified Modeling Language / 표준 모델링 언어)
- 사물·관계·다이어그램 (Things, Relationships, Diagrams)
- 구조적 / 정적 다이어그램 (Structural / Static Diagrams: Class, Object, Component, Deployment, Composite, Package)
- 행위적 / 동적 다이어그램 (Behavioral / Dynamic Diagrams: Use Case, Sequence, Communication, State, Activity, Timing)
- 스테레오 타입 (Stereotype / 길러멧 `<< >>`)
- 주액터 / 부액터 (Primary Actor / Secondary Actor)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([3. 현행 시스템 파악](13-bai-hoc.md)):** Sau khi hoàn thành phân tích hiện trạng hệ thống, bài này chính thức bước vào công cụ thiết kế chuẩn hóa quốc tế mạnh mẽ nhất: UML.
- **Tiếp nối sang bài sau ([11. 모델링 및 다이어그램 심화](15-bai-hoc.md)):** Đi sâu vào các biểu đồ UML phức tạp, máy chủ ứng dụng web WAS và sự phân biệt ký hiệu DFD giữa các trường phái.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc 2 bài thơ mnemonic phân loại biểu đồ tĩnh (클-객-컴-배-복-패) và động (유-순-커-상-활-타) - câu hỏi nhận diện này chiếm tần suất cực cao trong đề thi.
- Đọc TẦNG B để hiểu rõ tại sao việc chia tách góc nhìn tĩnh (cấu trúc code, class) và góc nhìn động (thời gian, thông điệp truyền nhận) là bắt buộc trong thiết kế hướng đối tượng.

---

## 3. 모델링 및 UML (Mô hình hóa và UML)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **개념 (Định nghĩa UML):** Là ngôn ngữ mô hình hóa trực quan chuẩn hóa quốc tế (chuẩn hóa bởi tổ chức OMG) dùng để đặc tả, trực quan hóa, xây dựng và lập tài liệu cho các hệ thống phần mềm hướng đối tượng (`객체지향 모델링 언어`).
- **3 thành phần cơ bản của UML (UML 3대 구성 요소):**
  1. `사물 (Things)`: Các khối xây dựng cơ bản (mô hình hóa cấu trúc như Class, Component; hành vi như State, Interaction; nhóm như Package; chú thích như Note).
  2. `관계 (Relationships)`: Mối liên kết kết nối các sự vật lại với nhau (Liên kết, Phụ thuộc, Khái quát hóa, Hiện thực hóa).
  3. `다이어그램 (Diagrams)`: Tập hợp các biểu đồ trực quan biểu diễn sự vật và mối quan hệ theo các góc nhìn khác nhau.
- **Phân loại biểu đồ UML theo 2 góc nhìn lớn (UML 2.0 chuẩn):**
  - **1. 구조적 다이어그램 (Structural Diagrams - Biểu đồ cấu trúc / Góc nhìn TĨNH - 6 loại):**
    - `클래스 다이어그램 (Class Diagram)`: Cấu trúc các lớp, thuộc tính, phương thức và quan hệ giữa chúng (quan trọng nhất).
    - `객체 다이어그램 (Object Diagram)`: Trạng thái của các đối tượng cụ thể tại một thời điểm nhất định.
    - `컴포넌트 다이어그램 (Component Diagram)`: Cấu trúc các mô-đun phần mềm có thể tái sử dụng và giao diện của chúng.
    - `배치 다이어그램 (Deployment Diagram)`: Phân bố vật lý của phần mềm trên các nút phần cứng máy chủ.
    - `복합체 구조 다이어그램 (Composite Structure Diagram)`: Cấu trúc bên trong của một lớp hoặc một thành phần phức hợp.
    - `패키지 다이어그램 (Package Diagram)`: Nhóm các phần tử mô hình thành các gói logic phân cấp.
    - 💡 **Mẹo nhớ biểu đồ tĩnh:** **클-객-컴-배-복-패** (Class, Object, Component, Deployment, Composite Structure, Package).
  - **2. 행위적 다이어그램 (Behavioral Diagrams - Biểu đồ hành vi / Góc nhìn ĐỘNG - 7 loại):**
    - `유스케이스 다이어그램 (Use Case Diagram)`: Yêu cầu chức năng nhìn từ góc độ người dùng (Actor và Use Case).
    - `순차 다이어그램 (Sequence Diagram)`: Tương tác giữa các đối tượng theo thứ tự dòng thời gian (`시간 순서`).
    - `커뮤니케이션 다이어그램 (Communication Diagram)`: Tương tác giữa các đối tượng nhấn mạnh mối quan hệ cấu trúc gửi nhận thông điệp.
    - `상태 다이어그램 (State Diagram)`: Sự thay đổi trạng thái của một đối tượng do các sự kiện kích hoạt.
    - `활동 다이어그램 (Activity Diagram)`: Luồng công việc xử lý logic bên trong của hệ thống (giống lưu đồ thuật toán).
    - `상호작용 개요 다이어그램 (Interaction Overview Diagram)`: Kết hợp giữa biểu đồ hoạt động và biểu đồ tuần tự.
    - `타이밍 다이어그램 (Timing Diagram)`: Biểu diễn sự biến đổi trạng thái của đối tượng theo thang đo thời gian thực chính xác.
    - 💡 **Mẹo nhớ biểu đồ động:** **유-순-커-상-활-상-타** (Use Case, Sequence, Communication, State, Activity, Interaction Overview, Timing).
- **스테레오 타입 (Stereotype):**
  - Cơ chế mở rộng của UML để bổ sung ngữ nghĩa cho các phần tử cơ bản.
  - Được viết trong cặp ngoặc kép gọi là Guillemet: `<<stereotype_name>>` (ví dụ: `<<include>>`, `<<extend>>`, `<<interface>>`).
- **Phân loại Tác nhân (Actor) trong Use Case:**
  - `주액터 (Primary Actor)`: Tác nhân trực tiếp sử dụng hệ thống để đạt được mục tiêu chính của mình, thường là con người đứng ở phía bên trái sơ đồ.
  - `부액터 (Secondary Actor)`: Hệ thống bên ngoài hoặc cơ quan hỗ trợ cung cấp dịch vụ giúp Primary Actor hoàn thành mục tiêu, thường vẽ ở phía bên phải (ví dụ: Cổng thanh toán trực tuyến, Hệ thống xác thực danh tính ngân hàng).
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Biểu đồ tuần tự (Sequence Diagram) là biểu đồ cấu trúc tĩnh?"* -> **Sai hoàn toàn**. Sequence Diagram là biểu đồ hành vi động (행위적/동적 다이어그램).
  - **Bẫy 2:** *"Package Diagram thuộc nhóm biểu đồ nào?"* -> **Nhóm cấu trúc tĩnh (구조적 다이어그램)**.
  - **Bẫy 3:** *"Dấu ngoặc kép biểu diễn Stereotype gọi là gì?"* -> **길러멧 (Guillemet - `<< >>`)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "UML gồm Sự vật - Quan hệ - Biểu đồ; tĩnh có 6 (클객컴배복패), động có 7 (유순커상활상타); mở rộng dùng Guillemet `<< >>`".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Sự khác biệt giữa Sequence Diagram và Communication Diagram:**
  - Cả hai đều thuộc nhóm Biểu đồ tương tác (`상호작용 다이어그램 - Interaction Diagram`), cùng biểu diễn việc các đối tượng gửi thông điệp (`메시지`) cho nhau.
  - **Sequence Diagram:** Trục thẳng đứng là đường sinh mệnh (Lifeline) đại diện cho thời gian trôi từ trên xuống dưới. Nhấn mạnh **Trật tự thời gian (시간 순서)**.
  - **Communication Diagram:** Không có trục thời gian, các đối tượng được nối với nhau bằng các đường liên kết và mũi tên thông điệp kèm số thứ tự (ví dụ: `1: login()`, `1.1: checkUser()`). Nhấn mạnh **Mối quan hệ cấu trúc không gian (구조적 관계)**.

### 복습 체크리스트
- [ ] Nhớ 3 thành phần cấu tạo nên UML: 사물 (Things), 관계 (Relationships), 다이어그램 (Diagrams).
- [ ] Đọc tên đủ 6 biểu đồ cấu trúc tĩnh (클-객-컴-배-복-패).
- [ ] Đọc tên đủ 7 biểu đồ hành vi động (유-순-커-상-활-상-타).
- [ ] Định nghĩa được Stereotype và ký hiệu 길러멧 `<< >>`.
- [ ] Phân biệt được Primary Actor (người nhận lợi ích) và Secondary Actor (hệ thống dịch vụ bên ngoài).
