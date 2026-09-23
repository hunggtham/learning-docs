# 3. 모델링 및 UML (Mô hình hóa và UML)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **3. 모델링 및 UML (Mô hình hóa và UML)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

모델링, UML

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 3. 모델링 및 UML (Mô hình hóa và UML)

### 013. UML (Unified Modeling Language)
- 시스템 개발자와 고객 또는 개발자 상호 간의 의사소통이 원활하게 이루어지도록 표준화한 대표적인 객체지향 모델링 언어이다. (Là ngôn ngữ mô hình hóa hướng đối tượng tiêu biểu được chuẩn hóa để việc giao tiếp giữa nhà phát triển hệ thống và khách hàng, hoặc giữa các nhà phát triển với nhau diễn ra suôn sẻ.)
- 구성 요소 (Components): 사물 (Things - Sự vật), 관계 (Relationships - Mối quan hệ), 다이어그램 (Diagram - Biểu đồ).
- **Ví dụ (Example):** Khi xây nhà cần bản vẽ thiết kế (Blueprint). Khi làm phần mềm, dùng UML làm bản vẽ thiết kế chung để ai cũng hiểu.
- 💡 **Mẹo ghi nhớ (Mnemonic):** **SQĐ** (Sự - Quan - Đa): **Sợ Quá Đi** (Sự vật - Quan hệ - Đa biểu đồ).

### 014. UML의 주요 관계 (Các mối quan hệ chính trong UML)
- 일반화 (Generalization) 관계: 하나의 사물이 다른 사물에 비해 더 일반적인지 구체적인지를 표현. (Thể hiện một sự vật là tổng quát hay cụ thể hơn sự vật khác - kế thừa).
- 의존 (Dependency) 관계: 필요에 의해 서로에게 영향을 주는 짧은 시간 동안만 연관을 유지하는 관계를 표현. (Thể hiện mối quan hệ phụ thuộc ngắn hạn, ảnh hưởng lẫn nhau khi cần thiết).
- 실체화 (Realization) 관계: 사물이 할 수 있거나 해야 하는 기능으로 서로를 그룹화 할 수 있는 관계를 표현. (Thể hiện mối quan hệ hiện thực hóa chức năng mà sự vật có thể/phải làm - interface).
- **Ví dụ (Example):** Động vật -> Chó, Mèo là mối quan hệ '일반화' (Generalization).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **NYT** (Nhất - Ý - Thực): **Như Ý Thật** (Nhất quát - Ý tồn - Thực thể).

### 015. 구조적(Structural) 다이어그램의 종류 (Các loại biểu đồ cấu trúc - Tĩnh)
- 클래스 다이어그램 (Class Diagram)
- 객체 다이어그램 (Object Diagram)
- 컴포넌트 다이어그램 (Component Diagram)
- 배치 다이어그램 (Deployment Diagram)
- 복합체 구조 다이어그램 (Composite Structure Diagram)
- 패키지 다이어그램 (Package Diagram)
- **Ví dụ (Example):** Class Diagram thể hiện cấu trúc tĩnh của hệ thống, giống như sơ đồ tổ chức của một công ty.
- 💡 **Mẹo ghi nhớ (Mnemonic):** **LĐCBPG** (Lớp - Đối - Com - Bố - Phức - Gói): **Làm Được Có Bữa Phải Giỏi**. Các biểu đồ này thể hiện cấu trúc "Tĩnh" (정적).

### 016. 행위(Behavioral) 다이어그램의 종류 (Các loại biểu đồ hành vi - Động)
- 유스케이스 다이어그램 (Use Case Diagram)
- 순차 다이어그램 (Sequence Diagram)
- 커뮤니케이션 다이어그램 (Communication Diagram)
- 상태 다이어그램 (State Diagram)
- 활동 다이어그램 (Activity Diagram)
- 상호작용 개요 다이어그램 (Interaction Overview Diagram)
- 타이밍 다이어그램 (Timing Diagram)
- **Ví dụ (Example):** Sequence Diagram thể hiện trình tự thời gian gửi tin nhắn (메시지) giữa các đối tượng (hành vi động).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **UTCTHTT** (Use - Trình - Com - Trạng - Hoạt - Tương - Time): **Uống Trà Chiều Thấy Hay Thật Tuyệt**. Các biểu đồ này thể hiện đặc tính "Động" (동적).

### 017. 스테레오 타입 (Stereotype)
- UML에서 표현하는 기본 기능 외에 추가적인 기능을 표현하기 위해 사용한다. (Dùng để biểu diễn các chức năng bổ sung ngoài chức năng cơ bản trong UML.)
- 길러멧(Guilemet)이라고 부르는 겹화살괄호(`<< >>`) 사이에 표현할 형태를 기술한다. (Viết hình thái muốn biểu diễn giữa cặp dấu ngoặc nhọn kép `<< >>` gọi là Guilemet.)
- **Ví dụ (Example):** `<<include>>` hoặc `<<extend>>` trong Use Case Diagram.

### 018. 유스케이스 다이어그램 - 액터(Actor) (Biểu đồ Use Case - Tác nhân)
- 시스템과 상호작용을 하는 모든 외부 요소로, 사람이나 외부 시스템을 의미한다. (Là tất cả các yếu tố bên ngoài tương tác với hệ thống, có nghĩa là con người hoặc hệ thống bên ngoài.)
- 주액터 (Primary Actor): 시스템을 사용함으로써 이득을 얻는 대상으로, 주로 사람이 해당함. (Đối tượng nhận được lợi ích khi dùng hệ thống, chủ yếu là con người - ví dụ: Khách hàng.)
- 부액터 (Secondary Actor): 주액터의 목적 달성을 위해 시스템에 서비스를 제공하는 외부 시스템으로, 조직이나 기관 등이 될 수 있음. (Hệ thống bên ngoài cung cấp dịch vụ cho hệ thống để đạt mục đích của Primary Actor - ví dụ: Cổng thanh toán ngân hàng.)

### 019. 순차(Sequence) 다이어그램의 구성 요소 (Thành phần của biểu đồ Sequence)
- 액터 (Actor - Tác nhân)
- 객체 (Object - Đối tượng)
- 생명선 (Lifeline - Đường đời)
- 실행 상자 (Active Box - Hộp thực thi)
- 메시지 (Message - Thông điệp)
- **Ví dụ (Example):** Khi user (Actor) ấn nút mua hàng, một mũi tên (Message) sẽ được gửi đến Giỏ hàng (Object). Đường nét đứt sổ dọc xuống từ Giỏ hàng là 생명선 (Lifeline).
