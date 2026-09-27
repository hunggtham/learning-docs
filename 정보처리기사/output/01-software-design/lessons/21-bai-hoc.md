# 12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

아키텍처, 설계, 심화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)

### 사용자 인터페이스(UI) 추가 유형 (Các loại UI bổ sung)
- **VUI (Voice User Interface):** 사람의 음성으로 기기를 조작하는 인터페이스. (Giao diện điều khiển bằng giọng nói - VD: Bixby, Alexa).
- **OUI (Organic User Interface):** 모든 사물과 사용자 간의 상호작용을 위한 인터페이스 (사물 인터넷, VR, AR, MR 등). (Giao diện hữu cơ, tương tác vật lý/thực tế ảo).

### 사용자 인터페이스 설계 지침 (Hướng dẫn thiết kế UI)
- **사용자 중심 (User-centric):** 실사용자에 대한 이해가 바탕이 되어야 함. (Dựa trên sự hiểu biết về người dùng thực tế).
- **사용성 (Usability):** 설계 시 가장 우선적으로 고려해야 함. (Ưu tiên hàng đầu khi thiết kế - dễ hiểu, dễ dùng).
- **심미성 (Aesthetics):** 디자인적으로 완성도 높게 그래픽 요소 배치. (Bố trí đồ họa thẩm mỹ cao).
- **오류 발생 해결 (Error Recovery):** 오류 발생 시 쉽게 인지하고 해결할 수 있도록 설계. (Giúp user dễ nhận biết và khắc phục lỗi).

### UI 설계 도구 심화 (Công cụ thiết kế UI chi tiết)
- **와이어프레임 (Wireframe):** 개략적인 레이아웃이나 뼈대 설계 (손그림, 스케치). (Khung xương, layout sơ lược).
- **목업 (Mockup):** 실제 화면과 유사하게 만든 정적인 형태의 모형. (Mô hình tĩnh giống thật nhưng không chạy được logic).
- **스토리보드 (Storyboard):** 와이어프레임 + 콘텐츠 설명 + 페이지 이동 흐름. 디자이너/개발자의 최종 참고 문서. (Tài liệu chi tiết nhất gồm wireframe + mô tả nội dung + luồng di chuyển).
- **프로토타입 (Prototype):** 인터랙션을 적용하여 실제 구현된 것처럼 테스트 가능한 동적인 모형. (Mô hình động có tương tác, test thử được).
- **유스케이스 (Use Case):** 사용자 측면의 요구사항 기술. (Mô tả yêu cầu chức năng từ góc nhìn người dùng).

### UI 주요 요소 (Các thành phần UI)
- **체크 박스 (Check Box):** 1개 이상의 값을 선택할 수 있는 버튼. (Chọn nhiều - Multiple choice).
- **라디오 버튼 (Radio Button):** 여러 항목 중 하나만 선택할 수 있는 버튼. (Chọn 1 - Single choice).
- **텍스트 박스 (Text Box):** 데이터를 입력/수정하는 상자. (Hộp nhập văn bản).
- **콤보 상자 (Combo Box):** 목록에서 선택하거나 새로 입력할 수 있는 상자. (Dropdown list có thể gõ thêm text).
- **목록 상자 (List Box):** 목록만 표시하고 새로 입력할 수는 없는 상자. (Chỉ chọn từ list có sẵn, không được gõ).

### 상위 설계와 하위 설계 (Thiết kế bậc cao và Bậc thấp)
- **상위 설계 (High-level Design):** 아키텍처 설계, 예비 설계. 대상: 시스템 전체 구조 (DB, Interface). (Thiết kế tổng thể, kiến trúc).
- **하위 설계 (Low-level Design):** 모듈 설계, 상세 설계. 대상: 시스템 내부 구조, 컴포넌트, 알고리즘. (Thiết kế chi tiết module, thuật toán).

### 소프트웨어 아키텍처 품질 속성 (Thuộc tính chất lượng Kiến trúc)
- **시스템 측면 (Hệ thống):** 성능, 보안, 가용성, 기능성. (Hiệu năng, bảo mật...).
- **비즈니스 측면 (Kinh doanh):** 시장 적시성 (Time-to-market), 비용과 혜택. (Thời điểm tung ra thị trường, chi phí).
- **아키텍처 측면 (Kiến trúc):** 개념적 무결성, 정확성, 완결성. (Tính toàn vẹn, chính xác).

### 협약(Contract)에 의한 설계 (Thiết kế theo hợp đồng)
- 컴포넌트의 정확한 인터페이스를 명세하는 방법. (Đặc tả chính xác interface của component).
- **선행 조건 (Precondition):** 오퍼레이션이 호출되기 전에 참이 되어야 할 조건. (Điều kiện bắt buộc trước khi chạy hàm).
- **결과 조건 (Postcondition):** 오퍼레이션이 수행된 후 만족되어야 할 조건. (Điều kiện phải đạt sau khi chạy hàm).
- **불변 조건 (Invariant):** 오퍼레이션이 실행되는 동안 항상 만족되어야 할 조건. (Điều kiện luôn đúng trong suốt quá trình chạy).
