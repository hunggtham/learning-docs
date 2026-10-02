# Môn 1 — 소프트웨어 설계: Deep Dive 2026

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Môn 1 — 소프트웨어 설계: Deep Dive 2026**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. 요구사항 확인 — Requirements confirmation** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. 화면 설계 — UI thiết kế (design / 설계)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này dùng software design depth làm owner, rồi nối requirements, UI, architecture, testing và quality.

> Mục tiêu của tệp (file / 파일) này là biến Môn 1 từ một danh sách thuật ngữ thành một chuỗi suy luận có thể dùng để giải câu hỏi. Khi gặp một lựa chọn lạ, hãy xác định nó đang nói về **yêu cầu (requirement / 요구사항), mô hình (model / 모델), kiến trúc (architecture / 아키텍처), mô-đun (module / 모듈), đối tượng (object / 객체) hay giao diện (interface / 인터페이스)** rồi mới so sánh đáp án.

## 1. 요구사항 확인 — Requirements confirmation

### 1.1 현행 시스템 분석 — phân tích hệ thống hiện tại

Phân tích hệ thống hiện tại không chỉ là liệt kê phần mềm đang chạy. Ta cần hiểu chức năng hiện có, ranh giới (boundary / 경계) của hệ thống, luồng dữ liệu, subsystem, giao diện (interface / 인터페이스), OS, DBMS, middleware, mạng (network / 네트워크) và các ràng buộc vận hành. Mục tiêu là biết hệ thống mới phải thay thế, tích hợp hay giữ tương thích với cái gì.

Trong câu hỏi thi, nếu đề nói về thông lượng (throughput / 처리량), phản hồi (response / 응답) thời gian (time / 시간), tài nguyên (resource / 자원) usage hoặc bottleneck thì thường đang hỏi **hiệu năng (performance / 성능) characteristic**. Nếu đề nói về phiên bản OS, DBMS, middleware, giao thức (protocol / 프로토콜) hoặc khả năng tương thích thì trọng tâm là **technical môi trường (environment / 환경)**. Nếu đề nói một hệ thống phụ thuộc một hệ thống khác thông qua giao diện (interface / 인터페이스) thì cần nghĩ tới **hệ thống (system / 시스템) phụ thuộc (dependency / 의존성)** chứ không phải yêu cầu (requirement / 요구사항) của người dùng (user / 사용자).

### 1.2 기능 요구사항 và 비기능 요구사항

기능 요구사항 (functional requirement) mô tả hệ thống phải thực hiện hành vi nào. 비기능 요구사항 (non-functional requirement) mô tả chất lượng, giới hạn hoặc ràng buộc (constraint / 제약조건) của hành vi đó. “Người dùng có thể tải báo cáo” là functional; “báo cáo phải tạo trong 3 giây với 5.000 người dùng (user / 사용자) đồng thời” là non-functional.

Một bẫy phổ biến là câu non-functional được viết bằng động từ nên trông giống chức năng. Hãy hỏi: **nếu bỏ phần này đi thì năng lực (capability / 역량) nghiệp vụ có biến mất hay chỉ chất lượng/ràng buộc thay đổi?** Nếu năng lực (capability / 역량) vẫn còn thì phần đó nhiều khả năng là non-functional.

### 1.3 요구사항 개발 프로세스

Một luồng (flow / 흐름) an toàn để nhớ là:

`도출 Elicitation → 분석 Analysis → 명세 Specification → 확인/검증 Validation`

Elicitation lấy thông tin từ stakeholder qua interview, workshop, observation, questionnaire, prototype và document phân tích (analysis / 분석). phân tích (analysis / 분석) xử lý xung đột (conflict / 충돌), phụ thuộc (dependency / 의존성), feasibility và priority. Specification biến yêu cầu thành dạng có cấu trúc, có thể kiểm tra. kiểm tra hợp lệ (validation / 검증) xác nhận yêu cầu (requirement / 요구사항) phản ánh đúng nhu cầu thực tế.

**xác minh (verification / 확인)** hỏi “đã làm đúng theo specification chưa?”. **kiểm tra hợp lệ (validation / 검증)** hỏi “specification/sản phẩm có đúng cái stakeholder cần không?”. Hai từ này có thể xuất hiện ở nhiều chapter khác nhau nhưng lô-gic (logic / 논리) phân biệt vẫn giữ nguyên.

### 1.4 요구사항 우선순위와 추적성

Priority không đơn thuần là “quan trọng/không quan trọng”. Một yêu cầu (requirement / 요구사항) có nghiệp vụ (business / 비즈니스) giá trị (value / 값) cao nhưng chi phí (cost / 비용)/rủi ro (risk / 위험) cũng cao. Trong thực tế có thể dùng MoSCoW: Must, Should, Could, Won't for now.

Traceability — 요구사항 추적성 — cho phép lần theo yêu cầu (requirement / 요구사항) từ nguồn gốc tới thiết kế (design / 설계), mã (code / 코드), kiểm thử (test / 테스트) và ngược lại. Khi đề hỏi vì sao traceability quan trọng, trọng tâm là **impact phân tích (analysis / 분석) và coverage**, không phải phiên bản (version / 버전) điều khiển (control / 제어) mã nguồn (source code / 소스 코드).

### 1.5 구조적 분석 — Structured phân tích (analysis / 분석)

DFD — 자료 흐름도 — mô tả dữ liệu đi từ bên ngoài (external / 외부) thực thể (entity / 엔터티) qua tiến trình (process / 프로세스) tới dữ liệu (data / 데이터) store và các luồng dữ liệu. DFD không phải flowchart: DFD tập trung vào **dữ liệu (data / 데이터) transformation**, còn flowchart nhấn vào điều khiển (control / 제어) luồng (flow / 흐름).

Dữ liệu (data / 데이터) Dictionary — 자료 사전 — định nghĩa dữ liệu xuất hiện trong DFD. Các ký hiệu cổ điển thường gặp trong tài liệu thi gồm cấu tạo, lựa chọn, lặp và optional. Không nên học chúng như ký tự rời; hãy hiểu chúng là một ngôn ngữ nhỏ để mô tả cấu trúc dữ liệu (data / 데이터).

Mini-specification — 소단위 명세서 — diễn giải lô-gic (logic / 논리) chi tiết của một tiến trình (process / 프로세스) thấp trong DFD khi tên tiến trình (process / 프로세스) không đủ mô tả hành vi.

### 1.6 UML — nhìn theo mục đích

UML diagram nên học bằng câu hỏi “mình muốn nhìn thấy điều gì?”.

| Muốn nhìn thấy | Diagram phù hợp |
|---|---|
| lớp (class / 클래스), attribute, phương thức (method / 메서드) và quan hệ | lớp (class / 클래스) Diagram |
| đối tượng (object / 객체) cụ thể tại một thời điểm | đối tượng (object / 객체) Diagram |
| actor và chức năng hệ thống | Use trường hợp (case / 사례) Diagram |
| thứ tự message theo thời gian | chuỗi (sequence / 시퀀스) Diagram |
| workflow và nhánh song song | Activity Diagram |
| trạng thái (state / 상태) của đối tượng (object / 객체) thay đổi theo sự kiện (event / 이벤트) | máy trạng thái (state machine / 상태 머신) Diagram |
| thành phần (component / 컴포넌트) và phụ thuộc (dependency / 의존성) | thành phần (component / 컴포넌트) Diagram |
| nút (node / 노드) vật lý và triển khai (deployment / 배포) | triển khai (deployment / 배포) Diagram |

Trong lớp (class / 클래스) Diagram, association là quan hệ tổng quát. Aggregation là whole–part yếu hơn; part có thể tồn tại độc lập. Composition là whole–part mạnh; vòng đời part phụ thuộc whole. Generalization là quan hệ “is-a”. phụ thuộc (dependency / 의존성) là phụ thuộc sử dụng tạm thời.

Một mẹo suy luận: nếu đề nói **vòng đời (lifecycle / 생명주기) quyền sở hữu (ownership / 소유권)** thì nghĩ tới composition; nếu chỉ là “có chứa” nhưng đối tượng con sống độc lập thì aggregation; nếu subclass kế thừa superclass thì generalization.

### 1.7 Agile, Scrum, XP

Agile là tư tưởng và tập phương pháp thích nghi theo phản hồi (feedback / 피드백). Scrum là khung phần mềm (framework / 프레임워크) quản lý công việc theo Sprint. XP nhấn mạnh kỹ thuật coding và phản hồi (feedback / 피드백) ngắn.

Scrum cần phân biệt sản phẩm (product / 제품) Backlog, Sprint Backlog và Increment. sản phẩm (product / 제품) Backlog là danh sách toàn bộ nhu cầu được sắp xếp; Sprint Backlog là phần được chọn cùng plan cho Sprint; Increment là kết quả tích lũy đáp ứng Definition of Done.

XP thường gắn với pair programming, test-first/TDD, continuous tích hợp (integration / 통합), refactoring, small releases và collective quyền sở hữu (ownership / 소유권). Nếu câu hỏi nhấn vào kỹ thuật (engineering / 엔지니어링) practice, XP thường hợp lý hơn Scrum.

> **Chuyển mạch:** Trong **Môn 1 — 소프트웨어 설계: Deep Dive 2026**, **2. 화면 설계 — UI thiết kế (design / 설계)** tiếp nhận điểm tựa từ **1. 요구사항 확인 — Requirements confirmation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. 애플리케이션 설계 — ứng dụng (application / 애플리케이션) thiết kế (design / 설계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. 화면 설계 — UI thiết kế (design / 설계)

### 2.1 UI không chỉ là đẹp

UI thiết kế (design / 설계) trong phạm vi thi liên quan usability, tương tác (interaction / 상호작용), yêu cầu (requirement / 요구사항) của người dùng, bố cục (layout / 레이아웃) và phương pháp biểu diễn prototype. Một UI đẹp nhưng người dùng không đoán được thao tác vẫn có usability kém.

Các nguyên tắc thường gặp: 직관성 (intuitiveness), 유효성 (effectiveness), 학습성 (learnability), 유연성 (flexibility). Khi đáp án diễn đạt khác từ khóa, hãy map về ý nghĩa: “người mới hiểu ngay” gần intuitiveness/learnability; “hoàn thành mục tiêu chính xác” gần effectiveness.

### 2.2 Wireframe, Mockup, Prototype, Storyboard

Wireframe mô tả skeleton/bố cục (layout / 레이아웃). Mockup nhấn hình thức trực quan gần sản phẩm. Prototype nhấn việc thử nghiệm luồng (flow / 흐름) hoặc tương tác (interaction / 상호작용). Storyboard nối nhiều màn hình và hành động thành một kịch bản.

Đề có thể cố tình gọi prototype là “mẫu thử” rồi hỏi có nhất thiết phải full hàm (function / 함수) không. Không: prototype có thể low-fidelity hoặc high-fidelity.

### 2.3 UI 유형

CLI dùng command văn bản (text / 텍스트). GUI dùng visual elements. NUI dùng tương tác (interaction / 상호작용) tự nhiên như voice, gesture, touch. OUI trong phân loại giáo trình truyền thống nói tới giao diện (interface / 인터페이스) gắn với bề mặt/vật thể có hình thức linh hoạt.

> **Chuyển mạch:** Ở chặng này của **Môn 1 — 소프트웨어 설계: Deep Dive 2026**, **3. 애플리케이션 설계 — ứng dụng (application / 애플리케이션) thiết kế (design / 설계)** tiếp nhận điểm tựa từ **2. 화면 설계 — UI thiết kế (design / 설계)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. 인터페이스 설계 — giao diện (interface / 인터페이스) thiết kế (design / 설계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. 애플리케이션 설계 — ứng dụng (application / 애플리케이션) thiết kế (design / 설계)

### 3.1 kiến trúc (architecture / 아키텍처) là quyết định ở mức lớn

Software kiến trúc (architecture / 아키텍처) xác định decomposition, thành phần (component / 컴포넌트), connector, responsibility và ràng buộc (constraint / 제약조건) quan trọng. thiết kế (design / 설계) chi tiết đi sâu hơn vào lớp (class / 클래스), mô-đun (module / 모듈), cấu trúc dữ liệu (data structure / 자료구조) và thuật toán (algorithm / 알고리즘).

Các style/mẫu (pattern / 패턴) kiến trúc nên hiểu theo sự đánh đổi (trade-off / 트레이드오프):

Layered kiến trúc (architecture / 아키텍처) chia trách nhiệm thành tầng; dễ thay đổi từng tầng nhưng có thể tạo overhead. máy khách (client / 클라이언트)–máy chủ (server / 서버) tập trung dịch vụ (service / 서비스) phía máy chủ (server / 서버) và yêu cầu (request / 요청) phía máy khách (client / 클라이언트). MVC tách mô hình (model / 모델), View, Controller để giảm coupling giữa dữ liệu (data / 데이터)/lô-gic nghiệp vụ (business logic / 비즈니스 로직) và presentation. Repository/Data-centered dùng kho dữ liệu trung tâm làm điểm chia sẻ. Pipe-and-Filter biến dữ liệu qua chuỗi stage độc lập.

Không học mẫu (pattern / 패턴) bằng tên. Hãy hỏi “dữ liệu (data / 데이터)/điều khiển (control / 제어) di chuyển thế nào?”.

### 3.2 mô-đun (module / 모듈) independence — 독립성

Mô-đun (module / 모듈) tốt có **high cohesion** và **low coupling**.

Cohesion — 응집도 — đo mức các phần tử bên trong cùng phục vụ một mục đích. Từ yếu đến mạnh thường gặp:

`Coincidental < Logical < Temporal < Procedural < Communicational < Sequential < Functional`

Coupling — 결합도 — đo mức mô-đun (module / 모듈) phụ thuộc nhau. Từ mạnh/xấu tới yếu/tốt thường học:

`Content > Common > External > Control > Stamp > Data`

Một số tài liệu thêm message coupling ở mức rất thấp trong OOP. Khi thi, cần bám đúng bộ thuật ngữ trong câu hỏi.

Cách hiểu thay vì thuộc lòng: nếu mô-đun (module / 모듈) khác sửa trực tiếp nội dung bên trong mô-đun (module / 모듈) → Content coupling cực mạnh. Nếu share toàn cục (global / 전역) dữ liệu (data / 데이터) → dùng chung (common / 공통). Nếu truyền flag điều khiển lô-gic (logic / 논리) mô-đun (module / 모듈) khác → điều khiển (control / 제어). Nếu truyền cả bản ghi (record / 레코드)/cấu trúc (structure / 구조) dù chỉ cần vài trường dữ liệu (field / 필드) → Stamp. Nếu chỉ truyền dữ liệu cần thiết qua parameter → dữ liệu (data / 데이터) coupling.

### 3.3 Fan-in / Fan-out

Fan-in là số mô-đun (module / 모듈) gọi vào mô-đun (module / 모듈) đang xét. Fan-out là số mô-đun (module / 모듈) mà mô-đun (module / 모듈) đang xét gọi ra. mô-đun (module / 모듈) được tái sử dụng thường có fan-in cao. Fan-out quá cao thường cho thấy mô-đun (module / 모듈) đang biết/quản quá nhiều phụ thuộc (dependency / 의존성).

### 3.4 OOP cốt lõi (core / 핵심)

Encapsulation — 캡슐화 — giấu biểu diễn (representation / 표현) và kiểm soát truy cập trạng thái (state / 상태). Inheritance — 상속 — tái sử dụng/quan hệ is-a. Polymorphism — 다형성 — cùng giao diện (interface / 인터페이스) nhưng hành vi (behavior / 동작) tùy đối tượng (object / 객체) cụ thể. lớp trừu tượng (abstraction / 추상화) — 추상화 — giữ đặc trưng cần thiết, bỏ chi tiết không liên quan.

Đừng đồng nhất inheritance với polymorphism. Inheritance là cơ chế tạo hierarchy; polymorphism là khả năng dispatch hành vi (behavior / 동작) qua cùng giao diện (interface / 인터페이스)/kiểu (type / 타입).

### 3.5 SOLID

SRP: một mô-đun (module / 모듈)/lớp (class / 클래스) nên có một lý do chính để thay đổi. OCP: mở rộng hành vi (behavior / 동작) mà hạn chế sửa mã (code / 코드) ổn định. LSP: subtype phải thay thế được cơ sở (base / 기반) kiểu (type / 타입) mà không phá đặc tả hợp đồng (contract / 계약). ISP: tránh giao diện (interface / 인터페이스) quá lớn buộc máy khách (client / 클라이언트) phụ thuộc phương thức (method / 메서드) không dùng. DIP: high-level chính sách (policy / 정책) không phụ thuộc trực tiếp low-level detail; cả hai phụ thuộc lớp trừu tượng (abstraction / 추상화).

Trong câu hỏi scenario, hãy tìm dấu hiệu. Một lớp (class / 클래스) vừa validate, ghi DB, gửi mail, log → SRP. Subclass override làm vi phạm expectation của cơ sở (base / 기반) lớp (class / 클래스) → LSP. giao diện (interface / 인터페이스) có 20 phương thức (method / 메서드) nhưng máy khách (client / 클라이언트) chỉ cần 2 → ISP.

### 3.6 mẫu thiết kế (design pattern / 디자인 패턴) — học theo intent

Creational giải quyết cách tạo đối tượng (object / 객체). Structural giải quyết cách ghép đối tượng (object / 객체)/lớp (class / 클래스). Behavioral giải quyết giao tiếp và phân phối responsibility.

Nhóm thường dễ nhầm:

**Factory phương thức (method / 메서드)** giao việc tạo đối tượng (object / 객체) cho subclass/hiện thực (implementation / 구현). **Abstract Factory** tạo một họ đối tượng (object / 객체) liên quan. **Builder** dựng đối tượng (object / 객체) phức tạp theo từng bước. **Prototype** clone đối tượng (object / 객체) hiện có. **Singleton** giới hạn một instance.

**Adapter** làm giao diện (interface / 인터페이스) không tương thích nói chuyện được. **cầu nối (bridge / 브리지)** tách lớp trừu tượng (abstraction / 추상화) khỏi hiện thực (implementation / 구현). **Decorator** thêm hành vi (behavior / 동작) động bằng wrapper. **Facade** cung cấp giao diện (interface / 인터페이스) đơn giản cho subsystem. **Proxy** đại diện/kiểm soát truy cập đối tượng (object / 객체) khác. **Composite** biểu diễn cây (tree / 트리) part–whole với giao diện (interface / 인터페이스) thống nhất.

**chiến lược (strategy / 전략)** thay thuật toán (algorithm / 알고리즘). **trạng thái (state / 상태)** hành vi (behavior / 동작) đổi theo trạng thái nội bộ (internal state / 내부 상태). **Observer** one-to-many notification. **Command** đóng gói yêu cầu (request / 요청) thành đối tượng (object / 객체). **Template phương thức (method / 메서드)** cố định skeleton thuật toán (algorithm / 알고리즘), để subclass override bước. **Iterator** duyệt collection mà không lộ biểu diễn (representation / 표현).

### 3.7 mã (code / 코드) thiết kế (design / 설계) và reuse

Reuse có thể ở mức hàm (function / 함수)/mô-đun (module / 모듈), thành phần (component / 컴포넌트), khung phần mềm (framework / 프레임워크), dịch vụ (service / 서비스) hoặc sản phẩm (product / 제품) line. Reuse cao không tự động tốt nếu lớp trừu tượng (abstraction / 추상화) sai; mục tiêu là giảm duplication mà vẫn giữ cohesion/coupling tốt.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Môn 1 — 소프트웨어 설계: Deep Dive 2026**, **4. 인터페이스 설계 — giao diện (interface / 인터페이스) thiết kế (design / 설계)** tiếp nhận điểm tựa từ **3. 애플리케이션 설계 — ứng dụng (application / 애플리케이션) thiết kế (design / 설계)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Bảng phân biệt phải thuộc bằng cơ chế** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. 인터페이스 설계 — giao diện (interface / 인터페이스) thiết kế (design / 설계)

### 4.1 giao diện (interface / 인터페이스) yêu cầu (requirement / 요구사항)

Giao diện (interface / 인터페이스) specification phải nói rõ nguồn (source / 소스)/mục tiêu (target / 대상), dữ liệu (data / 데이터) item, format, giao thức (protocol / 프로토콜), trigger, lỗi (error / 오류) handling, thử lại (retry / 재시도), hết thời gian chờ (timeout / 타임아웃), authentication và bảo mật (security / 보안) yêu cầu (requirement / 요구사항). Đề có thể hỏi “giao diện (interface / 인터페이스) danh sách (list / 목록)” và “giao diện (interface / 인터페이스) specification” khác nhau: danh sách (list / 목록) cho inventory ở mức tổng quan; specification đi vào detail từng giao diện (interface / 인터페이스).

### 4.2 giao diện (interface / 인터페이스) phương thức (method / 메서드)

Direct DB liên kết (connection / 연결) tạo coupling chặt với lược đồ (schema / 스키마). API/Web dịch vụ (service / 서비스) cung cấp đặc tả hợp đồng (contract / 계약) rõ hơn. tệp (file / 파일) transfer phù hợp batch nhưng có độ trễ (latency / 지연 시간). Message hàng đợi (queue / 큐) phù hợp asynchronous processing và decoupling.

Không có cách nào luôn tốt nhất; câu hỏi thường ẩn sự đánh đổi (trade-off / 트레이드오프) trong yêu cầu (requirement / 요구사항).

### 4.3 EAI patterns

Point-to-Point nối trực tiếp hệ thống với nhau; đơn giản khi ít hệ thống (system / 시스템) nhưng số liên kết (connection / 연결) tăng nhanh. Hub & Spoke dùng hub trung tâm để giảm liên kết (connection / 연결) trực tiếp. Message Bus dùng bus chung để trao đổi. Hybrid kết hợp nhiều cách.

ESB — Enterprise dịch vụ (service / 서비스) Bus — thường mở rộng tư tưởng bus bằng routing, transformation, orchestration và dịch vụ (service / 서비스) tích hợp (integration / 통합). Không nên đồng nhất mọi Message Bus với ESB.

### 4.4 XML, JSON, AJAX

XML biểu diễn dữ liệu (data / 데이터) có tag và lược đồ (schema / 스키마)/không gian tên (namespace / 네임스페이스) phong phú nhưng verbose. JSON nhẹ và tự nhiên với đối tượng (object / 객체)/array. AJAX là kỹ thuật trình duyệt (browser / 브라우저) trao đổi dữ liệu asynchronous với máy chủ (server / 서버) mà không reload toàn bộ page; AJAX không phải một format dữ liệu.

### 4.5 giao diện (interface / 인터페이스) bảo mật (security / 보안) và integrity

Giao diện (interface / 인터페이스) cần kiểm soát confidentiality, integrity, authentication và authorization. băm (hash / 해시)/checksum có thể kiểm tra integrity nhưng không tự cung cấp confidentiality. Encryption bảo vệ confidentiality nhưng nếu không có authentication/integrity cơ chế (mechanism / 메커니즘) thì vẫn có thể bị tamper theo nhiều cách.

> **Chuyển mạch:** Trong **Môn 1 — 소프트웨어 설계: Deep Dive 2026**, **4. 인터페이스 설계 — giao diện (interface / 인터페이스) thiết kế (design / 설계)** xác định đầu vào; **5. Bảng phân biệt phải thuộc bằng cơ chế** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **6. Procedural drills — phải tự trả lời trước khi xem ghi chú** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Bảng phân biệt phải thuộc bằng cơ chế

| Cặp dễ nhầm | Điểm tách |
|---|---|
| Functional vs Non-functional | năng lực (capability / 역량) vs chất lượng (quality / 품질)/ràng buộc (constraint / 제약조건) |
| xác minh (verification / 확인) vs kiểm tra hợp lệ (validation / 검증) | đúng spec vs đúng nhu cầu |
| DFD vs Flowchart | dữ liệu (data / 데이터) transformation vs điều khiển (control / 제어) luồng (flow / 흐름) |
| Aggregation vs Composition | vòng đời (lifecycle / 생명주기) độc lập vs phụ thuộc whole |
| chuỗi (sequence / 시퀀스) vs Activity | message theo thời gian vs workflow |
| Cohesion vs Coupling | bên trong mô-đun (module / 모듈) vs giữa modules |
| Factory phương thức (method / 메서드) vs Abstract Factory | một sản phẩm (product / 제품) hierarchy vs family products |
| Adapter vs Facade | đổi giao diện (interface / 인터페이스) để tương thích vs đơn giản hóa subsystem |
| chiến lược (strategy / 전략) vs trạng thái (state / 상태) | máy khách (client / 클라이언트) chọn thuật toán (algorithm / 알고리즘) vs hành vi (behavior / 동작) đổi theo trạng thái (state / 상태) |
| Wireframe vs Prototype | cấu trúc (structure / 구조) tĩnh vs thử nghiệm tương tác (interaction / 상호작용) |

> **Chuyển mạch:** Ở chặng này của **Môn 1 — 소프트웨어 설계: Deep Dive 2026**, **5. Bảng phân biệt phải thuộc bằng cơ chế** xác định đầu vào; **6. Procedural drills — phải tự trả lời trước khi xem ghi chú** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **7. 과락 방지 checklist — Môn 1** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Procedural drills — phải tự trả lời trước khi xem ghi chú

### Drill 1

Một yêu cầu (requirement / 요구사항) nói: “Hệ thống phải cho phép nhân viên export Excel và tệp (file / 파일) phải được tạo trong 2 giây”. Hãy tách phần functional và non-functional.

### Drill 2

Một mô-đun (module / 모듈) nhận toàn bộ `Customer` đối tượng (object / 객체) nhưng chỉ dùng `customerId`. Đây gần loại coupling nào hơn: dữ liệu (data / 데이터) hay Stamp? Giải thích tại sao.

### Drill 3

Một hệ thống cần thay thuật toán tính phí theo loại khách hàng tại thời gian chạy (runtime / 런타임). chiến lược (strategy / 전략) hay trạng thái (state / 상태) phù hợp hơn? Nếu thuật toán (algorithm / 알고리즘) tự đổi khi đối tượng (object / 객체) chuyển trạng thái (state / 상태) thì đáp án có thay đổi không?

### Drill 4

Một mô-đun (module / 모듈) A truy cập trực tiếp biến nội bộ của mô-đun (module / 모듈) B. Đây là dấu hiệu của coupling nào và vì sao nó nguy hiểm?

### Drill 5

Một đối tượng (object / 객체) thứ tự (order / 순서) chứa OrderLine; OrderLine không có nghĩa tồn tại độc lập ngoài thứ tự (order / 순서). Aggregation hay Composition?

### Drill 6

Đề yêu cầu “xem actor nào kích hoạt chức năng nào” nhưng không quan tâm thứ tự message. Use trường hợp (case / 사례) hay chuỗi (sequence / 시퀀스)?

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Môn 1 — 소프트웨어 설계: Deep Dive 2026**, **7. 과락 방지 checklist — Môn 1** tiếp nhận điểm tựa từ **6. Procedural drills — phải tự trả lời trước khi xem ghi chú** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 7. 과락 방지 checklist — Môn 1

Trước khi xem Môn 1 đã an toàn, phải tự làm được các việc sau mà không nhìn tài liệu:

- phân loại functional/non-functional và xác minh (verification / 확인)/kiểm tra hợp lệ (validation / 검증);
- đọc mục đích của DFD, DD, mini-spec;
- chọn đúng UML diagram cho scenario;
- phân biệt association, aggregation, composition, generalization, phụ thuộc (dependency / 의존성);
- giải thích Scrum sản phẩm tạo ra (artifact / 산출물) và XP practice;
- phân biệt wireframe/mockup/prototype/storyboard;
- sắp xếp cohesion và coupling theo hướng tốt/xấu;
- giải thích fan-in/fan-out;
- nhận diện OOP/SOLID từ scenario;
- phân nhóm và phân biệt các GoF mẫu (pattern / 패턴) chính;
- chọn phương án giao diện (interface / 인터페이스) theo sync/async, coupling, độ trễ (latency / 지연 시간);
- phân biệt Point-to-Point, Hub & Spoke, Message Bus, ESB;
- giải thích XML, JSON, AJAX mà không trộn category.

Nếu một dòng trên chưa làm được, đó là **coverage hole**, không phải “chi tiết phụ”.

> **Bàn giao:** Sau **7. 과락 방지 checklist — Môn 1**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
