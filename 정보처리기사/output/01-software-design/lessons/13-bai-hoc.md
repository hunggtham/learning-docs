# 11. 모델링 및 다이어그램 심화 (Mô hình hóa & Biểu đồ chuyên sâu)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **11. 모델링 및 다이어그램 심화 (Mô hình hóa & Biểu đồ chuyên sâu)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **11. 모델링 및 다이어그램 심화 (Mô hình hóa & Biểu đồ chuyên sâu)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **4. UML (Unified Modeling Language)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

모델링, 다이어그램, 심화

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **3. 모델링 및 UML (Mô hình hóa và UML)**에서 만든 기준을 이어받아 **11. 모델링 및 다이어그램 심화 (Mô hình hóa & Biểu đồ chuyên sâu)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 11. 모델링 및 다이어그램 심화 (Mô hình hóa & Biểu đồ chuyên sâu)

Ở bước 13/55, **11. 모델링 및 다이어그램 심화 (Mô hình hóa & Biểu đồ chuyên sâu)** xuất hiện như phần tiếp nối của **3. 모델링 및 UML (Mô hình hóa và UML)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **11. 모델링 및 다이어그램 심화 (Mô hình hóa & Biểu đồ chuyên sâu)** như một bài học cho người mới, hãy giữ câu hỏi: **ta dùng mô hình nào để biểu diễn đối tượng, quan hệ hoặc hành vi, và giới hạn của mỗi cách là gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Trước hết, ta đặt **웹 애플리케이션 서버 (WAS - Web Application Server)** vào câu hỏi chung của mục này rồi mới đọc các ý chi tiết bên dưới. Mục đích của đoạn **웹 애플리케이션 서버 (WAS - Web Application Server)** là xác định phạm vi, vai trò và tiêu chí nhận diện trước khi so sánh nó với các phần kế tiếp.

### 웹 애플리케이션 서버 (WAS - Web Application Server)

Bây giờ ta đi vào nội dung của **웹 애플리케이션 서버 (WAS - Web Application Server)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 동적인 콘텐츠를 처리하기 위해 사용되는 미들웨어. (Middleware xử lý các nội dung web động thay vì web tĩnh).
- 종류: Tomcat, GlassFish, JBoss, Jetty, JEUS, Resin, WebLogic, WebSphere.

Các bullet của **웹 애플리케이션 서버 (WAS - Web Application Server)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **웹 애플리케이션 서버 (WAS - Web Application Server)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **자료 흐름도 (DFD) 표기법 차이 (Khác biệt ký hiệu DFD)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **자료 흐름도 (DFD) 표기법 차이 (Khác biệt ký hiệu DFD)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 자료 흐름도 (DFD) 표기법 차이 (Khác biệt ký hiệu DFD)

Phần nguồn của **자료 흐름도 (DFD) 표기법 차이 (Khác biệt ký hiệu DFD)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **Yourdon/DeMarco:** 프로세스를 원(원형)으로 표시. (Process là hình tròn).
- **Gane/Sarson:** 프로세스를 둥근 사각형으로 표시. (Process là hình chữ nhật bo góc).

Các bullet của **자료 흐름도 (DFD) 표기법 차이 (Khác biệt ký hiệu DFD)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **자료 흐름도 (DFD) 표기법 차이 (Khác biệt ký hiệu DFD)**, đừng bắt đầu lại từ số không. **HIPO Chart의 종류 (Các loại biểu đồ HIPO)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **HIPO Chart의 종류 (Các loại biểu đồ HIPO)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### HIPO Chart의 종류 (Các loại biểu đồ HIPO)

Các ý ngay dưới **HIPO Chart의 종류 (Các loại biểu đồ HIPO)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **가시적 도표 (Visual Table of Contents):** 시스템의 전체적인 기능과 흐름을 보여주는 계층(Tree) 구조도. (Cấu trúc cây tổng thể).
- **총체적 도표 (Overview Diagram):** 입력, 처리, 출력에 대한 전반적인 정보를 제공. (Cung cấp thông tin tổng quan I-P-O).
- **세부적 도표 (Detail Diagram):** 기본 요소들을 상세히 기술하는 도표. (Mô tả chi tiết các yếu tố cơ bản).
- 💡 **Mẹo ghi nhớ (Mnemonic):** **GTT** (Gia - Tổng - Tế): **Giữ Trật Tự**.

Các bullet của **HIPO Chart의 종류 (Các loại biểu đồ HIPO)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**HIPO Chart의 종류 (Các loại biểu đồ HIPO)** vừa cho ta cách đặt câu hỏi. Bây giờ **클래스 다이어그램 심화 (Class Diagram chi tiết)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Ở đoạn **클래스 다이어그램 심화 (Class Diagram chi tiết)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 클래스 다이어그램 심화 (Class Diagram chi tiết)

Bây giờ ta đi vào nội dung của **클래스 다이어그램 심화 (Class Diagram chi tiết)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **클래스 (Class):** 3개의 구획으로 나뉨 (Chia làm 3 phần). 이름 (Tên class), 속성 (Attribute/Biến), 오퍼레이션 (Operation/Hàm, Phương thức).
- **관계 (Relationships) 심화:**
  - **연관 (Association):** 2개 이상의 사물이 서로 관련되어 있음 (Mũi tên ngang).
  - **집합 (Aggregation):** 하나의 사물이 다른 사물에 포함되어 있는 관계 (Hình thoi rỗng). (Ví dụ: Máy tính và Chuột - Mất máy tính chuột vẫn tồn tại).
  - **포함 (Composition):** 집합 관계의 특수한 형태, 포함하는 사물의 변화가 포함되는 사물에게 영향을 미치는 관계 (Hình thoi đặc). (Ví dụ: Tòa nhà và Căn phòng - Phá tòa nhà thì phòng cũng mất).

Các ý về **클래스 다이어그램 심화 (Class Diagram chi tiết)** được nối với ví dụ để chuyển từ thuật ngữ sang tình huống. Hãy thử dự đoán kết quả hoặc lựa chọn trước khi đọc phần ví dụ, rồi đối chiếu xem quy tắc nào đã dẫn đến kết luận đó.

Ta vừa chốt **클래스 다이어그램 심화 (Class Diagram chi tiết)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **스테레오 타입 (Stereotype) 추가** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Với **스테레오 타입 (Stereotype) 추가**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 스테레오 타입 (Stereotype) 추가

Phần nguồn của **스테레오 타입 (Stereotype) 추가** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- `<<include>>`: 연결된 다른 UML 요소에 대해 포함 관계. (Quan hệ Bắt buộc phải có - Bắt buộc thực hiện Use case kia).
- `<<extend>>`: 확장 관계. (Quan hệ Tùy chọn/Mở rộng - Có thể thực hiện hoặc không).
- `<<interface>>`: 인터페이스 정의. (Định nghĩa Interface).
- `<<exception>>`: 예외 정의. (Định nghĩa Ngoại lệ).
- `<<constructor>>`: 생성자 역할. (Đóng vai trò Hàm khởi tạo).

Các bullet của **스테레오 타입 (Stereotype) 추가** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **스테레오 타입 (Stereotype) 추가**, đừng bắt đầu lại từ số không. **순차 다이어그램 심화 (Sequence Diagram chi tiết)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Đoạn **순차 다이어그램 심화 (Sequence Diagram chi tiết)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 순차 다이어그램 심화 (Sequence Diagram chi tiết)

Các ý ngay dưới **순차 다이어그램 심화 (Sequence Diagram chi tiết)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **생명선 (Lifeline):** 객체가 메모리에 존재하는 기간 (Đường nét đứt sổ dọc xuống).
- **실행 상자 (Active Box):** 객체가 메시지를 주고받으며 구동되고 있음을 표현 (Hình chữ nhật nằm trên đường sinh mệnh).

Các bullet của **순차 다이어그램 심화 (Sequence Diagram chi tiết)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**순차 다이어그램 심화 (Sequence Diagram chi tiết)** vừa cho ta cách đặt câu hỏi. Bây giờ **사용자 인터페이스(UI) 특성 (Đặc tính của UI)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Ở đoạn **사용자 인터페이스(UI) 특성 (Đặc tính của UI)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 사용자 인터페이스(UI) 특성 (Đặc tính của UI)

Bây giờ ta đi vào nội dung của **사용자 인터페이스(UI) 특성 (Đặc tính của UI)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- 소프트웨어 영역 중 변경이 가장 많이 발생한다. (Là phần thường xuyên bị thay đổi nhất trong phần mềm).
- 최소한의 노력으로 원하는 결과를 얻을 수 있게 한다. (Giúp user đạt kết quả mong muốn với nỗ lực ít nhất).

Các bullet của **사용자 인터페이스(UI) 특성 (Đặc tính của UI)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Với **사용자 인터페이스(UI) 특성 (Đặc tính của UI)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Như vậy, **11. 모델링 및 다이어그램 심화 (Mô hình hóa & Biểu đồ chuyên sâu)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **4. UML (Unified Modeling Language)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.