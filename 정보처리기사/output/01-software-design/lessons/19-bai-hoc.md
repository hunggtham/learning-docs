# 12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **5. 요구공학 (Requirements Engineering)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

아키텍처, 설계, 심화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **1. 사용자 인터페이스 (User Interface - UI)**에서 만든 기준을 이어받아 **12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)

Ở bước 19/55, **12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)** xuất hiện như phần tiếp nối của **1. 사용자 인터페이스 (User Interface - UI)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)** như một bài học cho người mới, hãy giữ câu hỏi: **dữ liệu được tổ chức, ràng buộc và truy vấn theo quy tắc nào để kết quả vẫn đúng?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **사용자 인터페이스(UI) 추가 유형 (Các loại UI bổ sung)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **사용자 인터페이스(UI) 추가 유형 (Các loại UI bổ sung)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 사용자 인터페이스(UI) 추가 유형 (Các loại UI bổ sung)

Bây giờ ta đi vào nội dung của **사용자 인터페이스(UI) 추가 유형 (Các loại UI bổ sung)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **VUI (Voice User Interface):** 사람의 음성으로 기기를 조작하는 인터페이스. (Giao diện điều khiển bằng giọng nói - VD: Bixby, Alexa).
- **OUI (Organic User Interface):** 모든 사물과 사용자 간의 상호작용을 위한 인터페이스 (사물 인터넷, VR, AR, MR 등). (Giao diện hữu cơ, tương tác vật lý/thực tế ảo).

Các bullet của **사용자 인터페이스(UI) 추가 유형 (Các loại UI bổ sung)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **사용자 인터페이스(UI) 추가 유형 (Các loại UI bổ sung)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **사용자 인터페이스 설계 지침 (Hướng dẫn thiết kế UI)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **사용자 인터페이스 설계 지침 (Hướng dẫn thiết kế UI)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 사용자 인터페이스 설계 지침 (Hướng dẫn thiết kế UI)

Phần nguồn của **사용자 인터페이스 설계 지침 (Hướng dẫn thiết kế UI)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **사용자 중심 (User-centric):** 실사용자에 대한 이해가 바탕이 되어야 함. (Dựa trên sự hiểu biết về người dùng thực tế).
- **사용성 (Usability):** 설계 시 가장 우선적으로 고려해야 함. (Ưu tiên hàng đầu khi thiết kế - dễ hiểu, dễ dùng).
- **심미성 (Aesthetics):** 디자인적으로 완성도 높게 그래픽 요소 배치. (Bố trí đồ họa thẩm mỹ cao).
- **오류 발생 해결 (Error Recovery):** 오류 발생 시 쉽게 인지하고 해결할 수 있도록 설계. (Giúp user dễ nhận biết và khắc phục lỗi).

Các bullet của **사용자 인터페이스 설계 지침 (Hướng dẫn thiết kế UI)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **사용자 인터페이스 설계 지침 (Hướng dẫn thiết kế UI)**, đừng bắt đầu lại từ số không. **UI 설계 도구 심화 (Công cụ thiết kế UI chi tiết)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **UI 설계 도구 심화 (Công cụ thiết kế UI chi tiết)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### UI 설계 도구 심화 (Công cụ thiết kế UI chi tiết)

Các ý ngay dưới **UI 설계 도구 심화 (Công cụ thiết kế UI chi tiết)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **와이어프레임 (Wireframe):** 개략적인 레이아웃이나 뼈대 설계 (손그림, 스케치). (Khung xương, layout sơ lược).
- **목업 (Mockup):** 실제 화면과 유사하게 만든 정적인 형태의 모형. (Mô hình tĩnh giống thật nhưng không chạy được logic).
- **스토리보드 (Storyboard):** 와이어프레임 + 콘텐츠 설명 + 페이지 이동 흐름. 디자이너/개발자의 최종 참고 문서. (Tài liệu chi tiết nhất gồm wireframe + mô tả nội dung + luồng di chuyển).
- **프로토타입 (Prototype):** 인터랙션을 적용하여 실제 구현된 것처럼 테스트 가능한 동적인 모형. (Mô hình động có tương tác, test thử được).
- **유스케이스 (Use Case):** 사용자 측면의 요구사항 기술. (Mô tả yêu cầu chức năng từ góc nhìn người dùng).

Các bullet của **UI 설계 도구 심화 (Công cụ thiết kế UI chi tiết)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**UI 설계 도구 심화 (Công cụ thiết kế UI chi tiết)** vừa cho ta cách đặt câu hỏi. Bây giờ **UI 주요 요소 (Các thành phần UI)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Ở đoạn **UI 주요 요소 (Các thành phần UI)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### UI 주요 요소 (Các thành phần UI)

Bây giờ ta đi vào nội dung của **UI 주요 요소 (Các thành phần UI)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **체크 박스 (Check Box):** 1개 이상의 값을 선택할 수 있는 버튼. (Chọn nhiều - Multiple choice).
- **라디오 버튼 (Radio Button):** 여러 항목 중 하나만 선택할 수 있는 버튼. (Chọn 1 - Single choice).
- **텍스트 박스 (Text Box):** 데이터를 입력/수정하는 상자. (Hộp nhập văn bản).
- **콤보 상자 (Combo Box):** 목록에서 선택하거나 새로 입력할 수 있는 상자. (Dropdown list có thể gõ thêm text).
- **목록 상자 (List Box):** 목록만 표시하고 새로 입력할 수는 없는 상자. (Chỉ chọn từ list có sẵn, không được gõ).

Các bullet của **UI 주요 요소 (Các thành phần UI)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **UI 주요 요소 (Các thành phần UI)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **상위 설계와 하위 설계 (Thiết kế bậc cao và Bậc thấp)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **상위 설계와 하위 설계 (Thiết kế bậc cao và Bậc thấp)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 상위 설계와 하위 설계 (Thiết kế bậc cao và Bậc thấp)

Phần nguồn của **상위 설계와 하위 설계 (Thiết kế bậc cao và Bậc thấp)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **상위 설계 (High-level Design):** 아키텍처 설계, 예비 설계. 대상: 시스템 전체 구조 (DB, Interface). (Thiết kế tổng thể, kiến trúc).
- **하위 설계 (Low-level Design):** 모듈 설계, 상세 설계. 대상: 시스템 내부 구조, 컴포넌트, 알고리즘. (Thiết kế chi tiết module, thuật toán).

Các bullet của **상위 설계와 하위 설계 (Thiết kế bậc cao và Bậc thấp)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **상위 설계와 하위 설계 (Thiết kế bậc cao và Bậc thấp)**, đừng bắt đầu lại từ số không. **소프트웨어 아키텍처 품질 속성 (Thuộc tính chất lượng Kiến trúc)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **소프트웨어 아키텍처 품질 속성 (Thuộc tính chất lượng Kiến trúc)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 소프트웨어 아키텍처 품질 속성 (Thuộc tính chất lượng Kiến trúc)

Các ý ngay dưới **소프트웨어 아키텍처 품질 속성 (Thuộc tính chất lượng Kiến trúc)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **시스템 측면 (Hệ thống):** 성능, 보안, 가용성, 기능성. (Hiệu năng, bảo mật...).
- **비즈니스 측면 (Kinh doanh):** 시장 적시성 (Time-to-market), 비용과 혜택. (Thời điểm tung ra thị trường, chi phí).
- **아키텍처 측면 (Kiến trúc):** 개념적 무결성, 정확성, 완결성. (Tính toàn vẹn, chính xác).

Các bullet của **소프트웨어 아키텍처 품질 속성 (Thuộc tính chất lượng Kiến trúc)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**소프트웨어 아키텍처 품질 속성 (Thuộc tính chất lượng Kiến trúc)** vừa cho ta cách đặt câu hỏi. Bây giờ **협약(Contract)에 의한 설계 (Thiết kế theo hợp đồng)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Ở đoạn **협약(Contract)에 의한 설계 (Thiết kế theo hợp đồng)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 협약(Contract)에 의한 설계 (Thiết kế theo hợp đồng)

Bây giờ ta đi vào nội dung của **협약(Contract)에 의한 설계 (Thiết kế theo hợp đồng)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 컴포넌트의 정확한 인터페이스를 명세하는 방법. (Đặc tả chính xác interface của component).
- **선행 조건 (Precondition):** 오퍼레이션이 호출되기 전에 참이 되어야 할 조건. (Điều kiện bắt buộc trước khi chạy hàm).
- **결과 조건 (Postcondition):** 오퍼레이션이 수행된 후 만족되어야 할 조건. (Điều kiện phải đạt sau khi chạy hàm).
- **불변 조건 (Invariant):** 오퍼레이션이 실행되는 동안 항상 만족되어야 할 조건. (Điều kiện luôn đúng trong suốt quá trình chạy).

Các bullet của **협약(Contract)에 의한 설계 (Thiết kế theo hợp đồng)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Với **협약(Contract)에 의한 설계 (Thiết kế theo hợp đồng)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Như vậy, **12. UI 및 아키텍처 설계 심화 (Thiết kế UI & Kiến trúc chuyên sâu)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **5. 요구공학 (Requirements Engineering)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.