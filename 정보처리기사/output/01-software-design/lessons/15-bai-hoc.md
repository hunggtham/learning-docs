# 11. 모델링 및 다이어그램 심화 (Mô hình hóa & Biểu đồ chuyên sâu)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **11. 모델링 및 다이어그램 심화 (Mô hình hóa & Biểu đồ chuyên sâu)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

모델링, 다이어그램, 심화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 11. 모델링 및 다이어그램 심화 (Mô hình hóa & Biểu đồ chuyên sâu)

### 웹 애플리케이션 서버 (WAS - Web Application Server)
- 동적인 콘텐츠를 처리하기 위해 사용되는 미들웨어. (Middleware xử lý các nội dung web động thay vì web tĩnh).
- 종류: Tomcat, GlassFish, JBoss, Jetty, JEUS, Resin, WebLogic, WebSphere.

### 자료 흐름도 (DFD) 표기법 차이 (Khác biệt ký hiệu DFD)
- **Yourdon/DeMarco:** 프로세스를 원(원형)으로 표시. (Process là hình tròn).
- **Gane/Sarson:** 프로세스를 둥근 사각형으로 표시. (Process là hình chữ nhật bo góc).

### HIPO Chart의 종류 (Các loại biểu đồ HIPO)
- **가시적 도표 (Visual Table of Contents):** 시스템의 전체적인 기능과 흐름을 보여주는 계층(Tree) 구조도. (Cấu trúc cây tổng thể).
- **총체적 도표 (Overview Diagram):** 입력, 처리, 출력에 대한 전반적인 정보를 제공. (Cung cấp thông tin tổng quan I-P-O).
- **세부적 도표 (Detail Diagram):** 기본 요소들을 상세히 기술하는 도표. (Mô tả chi tiết các yếu tố cơ bản).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **GTT** (Gia - Tổng - Tế): **Giữ Trật Tự**.

### 클래스 다이어그램 심화 (Class Diagram chi tiết)
- **클래스 (Class):** 3개의 구획으로 나뉨 (Chia làm 3 phần). 이름 (Tên class), 속성 (Attribute/Biến), 오퍼레이션 (Operation/Hàm, Phương thức).
- **관계 (Relationships) 심화:**
  - **연관 (Association):** 2개 이상의 사물이 서로 관련되어 있음 (Mũi tên ngang).
  - **집합 (Aggregation):** 하나의 사물이 다른 사물에 포함되어 있는 관계 (Hình thoi rỗng). (Ví dụ: Máy tính và Chuột - Mất máy tính chuột vẫn tồn tại).
  - **포함 (Composition):** 집합 관계의 특수한 형태, 포함하는 사물의 변화가 포함되는 사물에게 영향을 미치는 관계 (Hình thoi đặc). (Ví dụ: Tòa nhà và Căn phòng - Phá tòa nhà thì phòng cũng mất).

### 스테레오 타입 (Stereotype) 추가
- `<<include>>`: 연결된 다른 UML 요소에 대해 포함 관계. (Quan hệ Bắt buộc phải có - Bắt buộc thực hiện Use case kia).
- `<<extend>>`: 확장 관계. (Quan hệ Tùy chọn/Mở rộng - Có thể thực hiện hoặc không).
- `<<interface>>`: 인터페이스 정의. (Định nghĩa Interface).
- `<<exception>>`: 예외 정의. (Định nghĩa Ngoại lệ).
- `<<constructor>>`: 생성자 역할. (Đóng vai trò Hàm khởi tạo).

### 순차 다이어그램 심화 (Sequence Diagram chi tiết)
- **생명선 (Lifeline):** 객체가 메모리에 존재하는 기간 (Đường nét đứt sổ dọc xuống).
- **실행 상자 (Active Box):** 객체가 메시지를 주고받으며 구동되고 있음을 표현 (Hình chữ nhật nằm trên đường sinh mệnh).

### 사용자 인터페이스(UI) 특성 (Đặc tính của UI)
- 소프트웨어 영역 중 변경이 가장 많이 발생한다. (Là phần thường xuyên bị thay đổi nhất trong phần mềm).
- 최소한의 노력으로 원하는 결과를 얻을 수 있게 한다. (Giúp user đạt kết quả mong muốn với nỗ lực ít nhất).
