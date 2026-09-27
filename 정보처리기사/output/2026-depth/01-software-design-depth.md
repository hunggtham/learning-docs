# Môn 1 — 소프트웨어 설계: Deep Dive 2026

> Mục tiêu của file này là biến Môn 1 từ một danh sách thuật ngữ thành một chuỗi suy luận có thể dùng để giải câu hỏi. Khi gặp một lựa chọn lạ, hãy xác định nó đang nói về **requirement, model, architecture, module, object hay interface** rồi mới so sánh đáp án.

## 1. 요구사항 확인 — Requirements confirmation

### 1.1 현행 시스템 분석 — phân tích hệ thống hiện tại

Phân tích hệ thống hiện tại không chỉ là liệt kê phần mềm đang chạy. Ta cần hiểu chức năng hiện có, boundary của hệ thống, luồng dữ liệu, subsystem, interface, OS, DBMS, middleware, network và các ràng buộc vận hành. Mục tiêu là biết hệ thống mới phải thay thế, tích hợp hay giữ tương thích với cái gì.

Trong câu hỏi thi, nếu đề nói về throughput, response time, resource usage hoặc bottleneck thì thường đang hỏi **performance characteristic**. Nếu đề nói về phiên bản OS, DBMS, middleware, protocol hoặc khả năng tương thích thì trọng tâm là **technical environment**. Nếu đề nói một hệ thống phụ thuộc một hệ thống khác thông qua interface thì cần nghĩ tới **system dependency** chứ không phải requirement của user.

### 1.2 기능 요구사항 và 비기능 요구사항

기능 요구사항 (functional requirement) mô tả hệ thống phải thực hiện hành vi nào. 비기능 요구사항 (non-functional requirement) mô tả chất lượng, giới hạn hoặc constraint của hành vi đó. “Người dùng có thể tải báo cáo” là functional; “báo cáo phải tạo trong 3 giây với 5.000 user đồng thời” là non-functional.

Một bẫy phổ biến là câu non-functional được viết bằng động từ nên trông giống chức năng. Hãy hỏi: **nếu bỏ phần này đi thì capability nghiệp vụ có biến mất hay chỉ chất lượng/ràng buộc thay đổi?** Nếu capability vẫn còn thì phần đó nhiều khả năng là non-functional.

### 1.3 요구사항 개발 프로세스

Một flow an toàn để nhớ là:

`도출 Elicitation → 분석 Analysis → 명세 Specification → 확인/검증 Validation`

Elicitation lấy thông tin từ stakeholder qua interview, workshop, observation, questionnaire, prototype và document analysis. Analysis xử lý conflict, dependency, feasibility và priority. Specification biến yêu cầu thành dạng có cấu trúc, có thể kiểm tra. Validation xác nhận requirement phản ánh đúng nhu cầu thực tế.

**Verification** hỏi “đã làm đúng theo specification chưa?”. **Validation** hỏi “specification/sản phẩm có đúng cái stakeholder cần không?”. Hai từ này có thể xuất hiện ở nhiều chapter khác nhau nhưng logic phân biệt vẫn giữ nguyên.

### 1.4 요구사항 우선순위와 추적성

Priority không đơn thuần là “quan trọng/không quan trọng”. Một requirement có business value cao nhưng cost/risk cũng cao. Trong thực tế có thể dùng MoSCoW: Must, Should, Could, Won't for now.

Traceability — 요구사항 추적성 — cho phép lần theo requirement từ nguồn gốc tới design, code, test và ngược lại. Khi đề hỏi vì sao traceability quan trọng, trọng tâm là **impact analysis và coverage**, không phải version control source code.

### 1.5 구조적 분석 — Structured analysis

DFD — 자료 흐름도 — mô tả dữ liệu đi từ external entity qua process tới data store và các luồng dữ liệu. DFD không phải flowchart: DFD tập trung vào **data transformation**, còn flowchart nhấn vào control flow.

Data Dictionary — 자료 사전 — định nghĩa dữ liệu xuất hiện trong DFD. Các ký hiệu cổ điển thường gặp trong tài liệu thi gồm cấu tạo, lựa chọn, lặp và optional. Không nên học chúng như ký tự rời; hãy hiểu chúng là một ngôn ngữ nhỏ để mô tả cấu trúc data.

Mini-specification — 소단위 명세서 — diễn giải logic chi tiết của một process thấp trong DFD khi tên process không đủ mô tả hành vi.

### 1.6 UML — nhìn theo mục đích

UML diagram nên học bằng câu hỏi “mình muốn nhìn thấy điều gì?”.

| Muốn nhìn thấy | Diagram phù hợp |
|---|---|
| class, attribute, method và quan hệ | Class Diagram |
| object cụ thể tại một thời điểm | Object Diagram |
| actor và chức năng hệ thống | Use Case Diagram |
| thứ tự message theo thời gian | Sequence Diagram |
| workflow và nhánh song song | Activity Diagram |
| state của object thay đổi theo event | State Machine Diagram |
| component và dependency | Component Diagram |
| node vật lý và deployment | Deployment Diagram |

Trong Class Diagram, association là quan hệ tổng quát. Aggregation là whole–part yếu hơn; part có thể tồn tại độc lập. Composition là whole–part mạnh; vòng đời part phụ thuộc whole. Generalization là quan hệ “is-a”. Dependency là phụ thuộc sử dụng tạm thời.

Một mẹo suy luận: nếu đề nói **lifecycle ownership** thì nghĩ tới composition; nếu chỉ là “có chứa” nhưng đối tượng con sống độc lập thì aggregation; nếu subclass kế thừa superclass thì generalization.

### 1.7 Agile, Scrum, XP

Agile là tư tưởng và tập phương pháp thích nghi theo feedback. Scrum là framework quản lý công việc theo Sprint. XP nhấn mạnh kỹ thuật coding và feedback ngắn.

Scrum cần phân biệt Product Backlog, Sprint Backlog và Increment. Product Backlog là danh sách toàn bộ nhu cầu được sắp xếp; Sprint Backlog là phần được chọn cùng plan cho Sprint; Increment là kết quả tích lũy đáp ứng Definition of Done.

XP thường gắn với pair programming, test-first/TDD, continuous integration, refactoring, small releases và collective ownership. Nếu câu hỏi nhấn vào engineering practice, XP thường hợp lý hơn Scrum.

## 2. 화면 설계 — UI Design

### 2.1 UI không chỉ là đẹp

UI design trong phạm vi thi liên quan usability, interaction, requirement của người dùng, layout và phương pháp biểu diễn prototype. Một UI đẹp nhưng người dùng không đoán được thao tác vẫn có usability kém.

Các nguyên tắc thường gặp: 직관성 (intuitiveness), 유효성 (effectiveness), 학습성 (learnability), 유연성 (flexibility). Khi đáp án diễn đạt khác từ khóa, hãy map về ý nghĩa: “người mới hiểu ngay” gần intuitiveness/learnability; “hoàn thành mục tiêu chính xác” gần effectiveness.

### 2.2 Wireframe, Mockup, Prototype, Storyboard

Wireframe mô tả skeleton/layout. Mockup nhấn hình thức trực quan gần sản phẩm. Prototype nhấn việc thử nghiệm flow hoặc interaction. Storyboard nối nhiều màn hình và hành động thành một kịch bản.

Đề có thể cố tình gọi prototype là “mẫu thử” rồi hỏi có nhất thiết phải full function không. Không: prototype có thể low-fidelity hoặc high-fidelity.

### 2.3 UI 유형

CLI dùng command text. GUI dùng visual elements. NUI dùng interaction tự nhiên như voice, gesture, touch. OUI trong phân loại giáo trình truyền thống nói tới interface gắn với bề mặt/vật thể có hình thức linh hoạt.

## 3. 애플리케이션 설계 — Application design

### 3.1 Architecture là quyết định ở mức lớn

Software architecture xác định decomposition, component, connector, responsibility và constraint quan trọng. Design chi tiết đi sâu hơn vào class, module, data structure và algorithm.

Các style/pattern kiến trúc nên hiểu theo trade-off:

Layered Architecture chia trách nhiệm thành tầng; dễ thay đổi từng tầng nhưng có thể tạo overhead. Client–Server tập trung service phía server và request phía client. MVC tách Model, View, Controller để giảm coupling giữa data/business logic và presentation. Repository/Data-centered dùng kho dữ liệu trung tâm làm điểm chia sẻ. Pipe-and-Filter biến dữ liệu qua chuỗi stage độc lập.

Không học pattern bằng tên. Hãy hỏi “data/control di chuyển thế nào?”.

### 3.2 Module independence — 독립성

Module tốt có **high cohesion** và **low coupling**.

Cohesion — 응집도 — đo mức các phần tử bên trong cùng phục vụ một mục đích. Từ yếu đến mạnh thường gặp:

`Coincidental < Logical < Temporal < Procedural < Communicational < Sequential < Functional`

Coupling — 결합도 — đo mức module phụ thuộc nhau. Từ mạnh/xấu tới yếu/tốt thường học:

`Content > Common > External > Control > Stamp > Data`

Một số tài liệu thêm message coupling ở mức rất thấp trong OOP. Khi thi, cần bám đúng bộ thuật ngữ trong câu hỏi.

Cách hiểu thay vì thuộc lòng: nếu module khác sửa trực tiếp nội dung bên trong module → Content coupling cực mạnh. Nếu share global data → Common. Nếu truyền flag điều khiển logic module khác → Control. Nếu truyền cả record/structure dù chỉ cần vài field → Stamp. Nếu chỉ truyền dữ liệu cần thiết qua parameter → Data coupling.

### 3.3 Fan-in / Fan-out

Fan-in là số module gọi vào module đang xét. Fan-out là số module mà module đang xét gọi ra. Module được tái sử dụng thường có fan-in cao. Fan-out quá cao thường cho thấy module đang biết/quản quá nhiều dependency.

### 3.4 OOP core

Encapsulation — 캡슐화 — giấu representation và kiểm soát truy cập state. Inheritance — 상속 — tái sử dụng/quan hệ is-a. Polymorphism — 다형성 — cùng interface nhưng behavior tùy object cụ thể. Abstraction — 추상화 — giữ đặc trưng cần thiết, bỏ chi tiết không liên quan.

Đừng đồng nhất inheritance với polymorphism. Inheritance là cơ chế tạo hierarchy; polymorphism là khả năng dispatch behavior qua cùng interface/type.

### 3.5 SOLID

SRP: một module/class nên có một lý do chính để thay đổi. OCP: mở rộng behavior mà hạn chế sửa code ổn định. LSP: subtype phải thay thế được base type mà không phá contract. ISP: tránh interface quá lớn buộc client phụ thuộc method không dùng. DIP: high-level policy không phụ thuộc trực tiếp low-level detail; cả hai phụ thuộc abstraction.

Trong câu hỏi scenario, hãy tìm dấu hiệu. Một class vừa validate, ghi DB, gửi mail, log → SRP. Subclass override làm vi phạm expectation của base class → LSP. Interface có 20 method nhưng client chỉ cần 2 → ISP.

### 3.6 Design Pattern — học theo intent

Creational giải quyết cách tạo object. Structural giải quyết cách ghép object/class. Behavioral giải quyết giao tiếp và phân phối responsibility.

Nhóm thường dễ nhầm:

**Factory Method** giao việc tạo object cho subclass/implementation. **Abstract Factory** tạo một họ object liên quan. **Builder** dựng object phức tạp theo từng bước. **Prototype** clone object hiện có. **Singleton** giới hạn một instance.

**Adapter** làm interface không tương thích nói chuyện được. **Bridge** tách abstraction khỏi implementation. **Decorator** thêm behavior động bằng wrapper. **Facade** cung cấp interface đơn giản cho subsystem. **Proxy** đại diện/kiểm soát truy cập object khác. **Composite** biểu diễn tree part–whole với interface thống nhất.

**Strategy** thay algorithm. **State** behavior đổi theo internal state. **Observer** one-to-many notification. **Command** đóng gói request thành object. **Template Method** cố định skeleton algorithm, để subclass override bước. **Iterator** duyệt collection mà không lộ representation.

### 3.7 Code design và reuse

Reuse có thể ở mức function/module, component, framework, service hoặc product line. Reuse cao không tự động tốt nếu abstraction sai; mục tiêu là giảm duplication mà vẫn giữ cohesion/coupling tốt.

## 4. 인터페이스 설계 — Interface Design

### 4.1 Interface requirement

Interface specification phải nói rõ source/target, data item, format, protocol, trigger, error handling, retry, timeout, authentication và security requirement. Đề có thể hỏi “interface list” và “interface specification” khác nhau: list cho inventory ở mức tổng quan; specification đi vào detail từng interface.

### 4.2 Interface method

Direct DB connection tạo coupling chặt với schema. API/Web Service cung cấp contract rõ hơn. File transfer phù hợp batch nhưng có latency. Message Queue phù hợp asynchronous processing và decoupling.

Không có cách nào luôn tốt nhất; câu hỏi thường ẩn trade-off trong requirement.

### 4.3 EAI patterns

Point-to-Point nối trực tiếp hệ thống với nhau; đơn giản khi ít system nhưng số connection tăng nhanh. Hub & Spoke dùng hub trung tâm để giảm connection trực tiếp. Message Bus dùng bus chung để trao đổi. Hybrid kết hợp nhiều cách.

ESB — Enterprise Service Bus — thường mở rộng tư tưởng bus bằng routing, transformation, orchestration và service integration. Không nên đồng nhất mọi Message Bus với ESB.

### 4.4 XML, JSON, AJAX

XML biểu diễn data có tag và schema/namespace phong phú nhưng verbose. JSON nhẹ và tự nhiên với object/array. AJAX là kỹ thuật browser trao đổi dữ liệu asynchronous với server mà không reload toàn bộ page; AJAX không phải một format dữ liệu.

### 4.5 Interface security và integrity

Interface cần kiểm soát confidentiality, integrity, authentication và authorization. Hash/checksum có thể kiểm tra integrity nhưng không tự cung cấp confidentiality. Encryption bảo vệ confidentiality nhưng nếu không có authentication/integrity mechanism thì vẫn có thể bị tamper theo nhiều cách.

## 5. Bảng phân biệt phải thuộc bằng cơ chế

| Cặp dễ nhầm | Điểm tách |
|---|---|
| Functional vs Non-functional | capability vs quality/constraint |
| Verification vs Validation | đúng spec vs đúng nhu cầu |
| DFD vs Flowchart | data transformation vs control flow |
| Aggregation vs Composition | lifecycle độc lập vs phụ thuộc whole |
| Sequence vs Activity | message theo thời gian vs workflow |
| Cohesion vs Coupling | bên trong module vs giữa modules |
| Factory Method vs Abstract Factory | một product hierarchy vs family products |
| Adapter vs Facade | đổi interface để tương thích vs đơn giản hóa subsystem |
| Strategy vs State | client chọn algorithm vs behavior đổi theo state |
| Wireframe vs Prototype | structure tĩnh vs thử nghiệm interaction |

## 6. Procedural drills — phải tự trả lời trước khi xem ghi chú

### Drill 1

Một requirement nói: “Hệ thống phải cho phép nhân viên export Excel và file phải được tạo trong 2 giây”. Hãy tách phần functional và non-functional.

### Drill 2

Một module nhận toàn bộ `Customer` object nhưng chỉ dùng `customerId`. Đây gần loại coupling nào hơn: Data hay Stamp? Giải thích tại sao.

### Drill 3

Một hệ thống cần thay thuật toán tính phí theo loại khách hàng tại runtime. Strategy hay State phù hợp hơn? Nếu algorithm tự đổi khi object chuyển state thì đáp án có thay đổi không?

### Drill 4

Một module A truy cập trực tiếp biến nội bộ của module B. Đây là dấu hiệu của coupling nào và vì sao nó nguy hiểm?

### Drill 5

Một object Order chứa OrderLine; OrderLine không có nghĩa tồn tại độc lập ngoài Order. Aggregation hay Composition?

### Drill 6

Đề yêu cầu “xem actor nào kích hoạt chức năng nào” nhưng không quan tâm thứ tự message. Use Case hay Sequence?

## 7. 과락 방지 checklist — Môn 1

Trước khi xem Môn 1 đã an toàn, phải tự làm được các việc sau mà không nhìn tài liệu:

- phân loại functional/non-functional và verification/validation;
- đọc mục đích của DFD, DD, mini-spec;
- chọn đúng UML diagram cho scenario;
- phân biệt association, aggregation, composition, generalization, dependency;
- giải thích Scrum artifact và XP practice;
- phân biệt wireframe/mockup/prototype/storyboard;
- sắp xếp cohesion và coupling theo hướng tốt/xấu;
- giải thích fan-in/fan-out;
- nhận diện OOP/SOLID từ scenario;
- phân nhóm và phân biệt các GoF pattern chính;
- chọn phương án interface theo sync/async, coupling, latency;
- phân biệt Point-to-Point, Hub & Spoke, Message Bus, ESB;
- giải thích XML, JSON, AJAX mà không trộn category.

Nếu một dòng trên chưa làm được, đó là **coverage hole**, không phải “chi tiết phụ”.
