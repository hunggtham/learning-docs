# 정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng

> Mục tiêu của file này không phải là một bản 요약 (tóm tắt) để học thuộc trong vài giờ. Đây là **xương sống ôn thi** dùng để kiểm tra rằng toàn bộ phạm vi 필기 đã được học đủ, hiểu đủ sâu và có thể phân biệt các khái niệm gần giống nhau trong câu hỏi trắc nghiệm.
>
> Thuật ngữ quan trọng giữ nguyên tiếng Hàn, kèm English và nghĩa Việt để khi gặp trực tiếp trong đề thi không phải dịch lại trong đầu.

## 0. Vì sao cần một master guide riêng

정보처리기사 필기 có 5 môn, mỗi môn 20 câu. Điểm trung bình phải từ 60 trở lên, đồng thời **không môn nào được dưới 40**. Điều này tạo ra hai loại rủi ro khác nhau. Rủi ro thứ nhất là không biết đủ rộng: một môn có vài vùng kiến thức bỏ trống sẽ dễ rơi vào 과락. Rủi ro thứ hai là biết nhiều thuật ngữ nhưng không phân biệt được chúng khi đáp án cố tình dùng những khái niệm gần nhau.

Vì vậy cách học ở đây dùng ba lớp.

**Coverage layer** trả lời: phạm vi chính thức có phần nào và mình đã học phần đó chưa?  
**Understanding layer** trả lời: cơ chế bên dưới là gì, tại sao khái niệm đó tồn tại, nó khác khái niệm gần nó ở đâu?  
**Exam layer** trả lời: nếu câu hỏi đổi cách diễn đạt, cho đoạn code, SQL, sơ đồ hoặc tình huống thì mình có suy ra được đáp án không?

Bộ 출제기준 áp dụng năm 2026 vẫn dùng 5 môn:

1. 소프트웨어 설계 — Software Design — Thiết kế phần mềm
2. 소프트웨어 개발 — Software Development — Phát triển phần mềm
3. 데이터베이스 구축 — Database Construction — Xây dựng cơ sở dữ liệu
4. 프로그래밍 언어 활용 — Programming Language Application — Ứng dụng ngôn ngữ lập trình
5. 정보시스템 구축관리 — Information System Construction Management — Quản lý xây dựng hệ thống thông tin

Khung ôn dưới đây bám theo 21 chương lớn đang được các giáo trình 2026 tổ chức theo 출제기준: 4 chương ở môn 1, 5 chương ở môn 2, 5 chương ở môn 3, 3 chương ở môn 4 và 4 chương ở môn 5.

---

# 1. 소프트웨어 설계 — Software Design

Môn 1 kiểm tra khả năng nhìn một hệ thống **trước khi code**. Nếu chỉ nhớ từ khóa UML, Agile, 디자인 패턴 mà không hiểu dòng chảy từ yêu cầu → mô hình → kiến trúc → module → interface, rất dễ nhầm đáp án.

## 1.1 요구사항 확인 — Requirements confirmation

### 현행 시스템 분석 — phân tích hệ thống hiện tại

Trước khi thiết kế hệ thống mới phải biết hệ thống hiện tại đang gồm những subsystem nào, giao tiếp ra sao, dùng OS/DBMS/network gì và có giới hạn kỹ thuật nào. Đây không phải thủ tục giấy tờ; nó quyết định liệu yêu cầu mới có khả thi hay không.

Khi đọc câu hỏi về 플랫폼 기능 분석, 플랫폼 성능 특성 분석, 운영체제 분석, 네트워크 분석, DBMS 분석, hãy luôn xác định **đối tượng đang được đánh giá là gì**. Ví dụ, throughput thấp có thể liên quan hiệu năng platform; một DBMS không hỗ trợ transaction isolation mong muốn lại là giới hạn của database platform.

### 요구사항 분류

Functional requirement — 기능 요구사항 — mô tả hệ thống **phải làm gì**.  
Non-functional requirement — 비기능 요구사항 — mô tả hệ thống **phải tốt đến mức nào hoặc bị ràng buộc như thế nào**: performance, security, availability, portability, usability, pháp lý.

Ví dụ: “người dùng có thể reset password” là functional. “reset password phải hoàn thành dưới 2 giây và token hết hạn sau 10 phút” là non-functional.

Đề thường làm khó bằng cách viết non-functional requirement dưới dạng một hành vi. Hãy nhìn vào bản chất: nếu câu nói về chất lượng, giới hạn hoặc constraint thì không phải chức năng nghiệp vụ chính.

### 요구사항 개발 프로세스

Elicitation — 도출 — khai thác yêu cầu.  
Analysis — 분석 — phân tích xung đột, feasibility, priority.  
Specification — 명세 — biểu diễn thành tài liệu/mô hình có thể kiểm tra.  
Validation — 확인/검증 — xác nhận yêu cầu phản ánh đúng điều stakeholder cần.

Phân biệt **Verification** và **Validation** theo câu hỏi nền tảng:

- Verification: “Are we building the product right?” — đang xây đúng theo đặc tả không?
- Validation: “Are we building the right product?” — đặc tả/sản phẩm có đúng nhu cầu không?

### 요구사항 분석 기법

Data Flow Diagram — DFD — 자료 흐름도 biểu diễn process, data flow, data store, external entity. DFD tập trung **dữ liệu đi đâu và được biến đổi thế nào**, không mô tả control flow chi tiết như flowchart.

Data Dictionary — DD — 자료 사전 mô tả cấu trúc dữ liệu và ký hiệu. Các ký hiệu truyền thống như `=`, `+`, `{}`, `[]`, `()` thường được hỏi theo kiểu ghép nghĩa; cần học theo bản chất cấu tạo dữ liệu thay vì chỉ học chuỗi ký hiệu.

Mini-specification — 소단위 명세서 dùng để mô tả logic bên trong process ở mức thấp của DFD khi tên process chưa đủ rõ.

### UML

UML không phải một diagram mà là một ngôn ngữ mô hình hóa có nhiều diagram.

Structural diagrams — 구조 다이어그램 — mô tả cấu trúc tĩnh: Class, Object, Component, Deployment, Package, Composite Structure.

Behavioral diagrams — 행위 다이어그램 — mô tả hành vi: Use Case, Activity, State Machine. Interaction diagrams như Sequence, Communication, Timing, Interaction Overview là nhóm hành vi tập trung tương tác.

Trong Sequence Diagram, lifeline đi theo chiều dọc, thời gian tiến từ trên xuống dưới, message biểu diễn tương tác. Trong Activity Diagram, trọng tâm là luồng hoạt động và decision/parallelism. Trong State Diagram, trọng tâm là trạng thái của một object và transition khi event xảy ra.

**Bẫy thường gặp:** cùng một nghiệp vụ có thể vẽ bằng nhiều diagram. Câu hỏi hỏi “muốn biết object nào gọi object nào theo thứ tự thời gian” → Sequence. “Muốn biết trạng thái object thay đổi thế nào” → State. “Muốn biết flow công việc” → Activity.

### Agile, Scrum, XP

Agile là nhóm tư tưởng/phương pháp ưu tiên feedback nhanh và thích nghi thay đổi; Scrum là framework quản lý công việc theo sprint; XP tập trung mạnh vào engineering practices.

Scrum: Product Backlog → Sprint Planning → Sprint Backlog → Sprint → Increment, với Daily Scrum, Sprint Review, Sprint Retrospective.

XP thường gắn với Pair Programming, Test-Driven Development, Continuous Integration, Refactoring, Small Releases, Collective Ownership.

Đừng đồng nhất “Agile = không có tài liệu”. Agile giảm tài liệu không tạo giá trị, không phủ nhận documentation cần thiết.

## 1.2 화면 설계 — UI design

UI design không chỉ là bố cục. Đề có thể hỏi 원칙, 유형, 설계 도구, usability và accessibility.

### UI 유형

CLI — Command Line Interface: giao tiếp bằng lệnh.  
GUI — Graphical User Interface: cửa sổ, icon, menu.  
NUI — Natural User Interface: gesture, voice, touch tự nhiên.  
OUI — Organic User Interface: interface linh hoạt theo vật lý/hình dạng trong cách phân loại truyền thống của giáo trình.

### UI 설계 원칙

직관성 — intuitiveness: người dùng đoán được cách dùng.  
유효성 — effectiveness: đạt mục tiêu chính xác.  
학습성 — learnability: dễ học.  
유연성 — flexibility: thích ứng nhiều tình huống/người dùng.

Các giáo trình có thể diễn đạt thêm consistency, accessibility, feedback. Đề cần đọc đúng thuật ngữ đang hỏi thay vì suy từ “nghe có vẻ tốt”.

### UI 설계 산출물

Wireframe tập trung cấu trúc màn hình.  
Mockup cho hình thức gần giao diện thật nhưng thường chưa có tương tác đầy đủ.  
Prototype mô phỏng tương tác để kiểm chứng flow.  
Storyboard mô tả màn hình, transition và interaction theo kịch bản.

Bẫy: Prototype có thể low-fidelity hoặc high-fidelity; không phải cứ prototype là sản phẩm chạy hoàn chỉnh.

## 1.3 애플리케이션 설계 — Application design

### 모듈 독립성 — module independence

Thiết kế tốt thường hướng tới **high cohesion, low coupling**.

Cohesion — 응집도 — mức các phần bên trong cùng module phục vụ một mục tiêu thống nhất. Thứ tự thường học từ mạnh đến yếu:

Functional → Sequential → Communicational → Procedural → Temporal → Logical → Coincidental.

Coupling — 결합도 — mức module phụ thuộc module khác. Thứ tự thường học từ mạnh/xấu đến yếu/tốt:

Content → Common → External → Control → Stamp → Data.

Cần hiểu từng loại, không chỉ thuộc thứ tự. Data coupling truyền đúng dữ liệu cần thiết qua parameter. Stamp coupling truyền một cấu trúc tổng hợp dù chỉ dùng một phần. Control coupling truyền flag làm thay đổi logic nội bộ module kia. Common coupling cùng truy cập global data. Content coupling can thiệp trực tiếp nội bộ module khác.

### Fan-in / Fan-out

Fan-in là số module gọi vào một module. Fan-out là số module mà module hiện tại gọi ra. Fan-in cao có thể thể hiện reuse tốt; fan-out quá cao thường làm module phụ thuộc nhiều thành phần. Nhưng không dùng chỉ số này máy móc: luôn đọc ngữ cảnh câu hỏi.

### 객체지향 — OOP

Encapsulation — 캡슐화 — che giấu implementation và gom state + behavior.  
Inheritance — 상속 — lớp con kế thừa đặc tính/hành vi.  
Polymorphism — 다형성 — cùng interface/message nhưng behavior khác theo object.  
Abstraction — 추상화 — giữ bản chất cần thiết, bỏ chi tiết không liên quan.

Overloading = cùng tên method nhưng khác parameter list, thường quyết định compile time.  
Overriding = subclass định nghĩa lại method của superclass với cùng contract, thường liên quan dynamic dispatch/runtime polymorphism.

### SOLID

SRP: một module/class nên có một lý do chính để thay đổi.  
OCP: mở rộng behavior mà hạn chế sửa code ổn định.  
LSP: subtype phải thay thế supertype mà không phá contract.  
ISP: client không nên phụ thuộc interface chứa method nó không dùng.  
DIP: module cấp cao phụ thuộc abstraction thay vì concrete implementation.

Không nên học SOLID như khẩu hiệu. Ví dụ nếu `PaymentService` trực tiếp `new KakaoPayClient()` và mọi logic lệ thuộc class đó, DIP bị yếu. Nếu service nhận `PaymentGateway` interface qua constructor, dependency hướng về abstraction.

### Design Pattern

Ba nhóm GoF:

Creational — 생성: Abstract Factory, Builder, Factory Method, Prototype, Singleton.  
Structural — 구조: Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy.  
Behavioral — 행위: Chain of Responsibility, Command, Interpreter, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor.

Học pattern theo “problem → mechanism → consequence”.

Adapter đổi interface để hai thành phần không tương thích làm việc với nhau. Decorator bọc object để thêm behavior động. Proxy đứng thay object để kiểm soát truy cập/lazy loading/remote access. Strategy đóng gói algorithm có thể thay thế. State làm behavior thay đổi theo state nội bộ. Observer phát thông báo một-nhiều khi subject đổi.

## 1.4 인터페이스 설계 — Interface design

Interface giữa hệ thống phải định nghĩa dữ liệu, protocol, timing, error handling và security.

EAI — Enterprise Application Integration thường gặp các topology: Point-to-Point, Hub & Spoke, Message Bus, Hybrid. Point-to-Point đơn giản khi ít hệ thống nhưng số connection tăng nhanh khi hệ thống tăng. Hub & Spoke tập trung kết nối qua hub nhưng hub có thể trở thành bottleneck/single point of failure. Message Bus giảm coupling nhờ bus/message-oriented integration.

ESB — Enterprise Service Bus nhấn mạnh service integration, routing, transformation và mediation trên bus.

JSON nhẹ, dễ dùng trong web API. XML giàu khả năng mô tả schema/namespace nhưng verbose hơn. AJAX là kỹ thuật browser trao đổi dữ liệu bất đồng bộ mà không reload toàn trang; AJAX không phải một data format.

---

# 2. 소프트웨어 개발 — Software Development

Môn 2 thường gây cảm giác “rải rác” vì trộn 자료구조, testing, packaging, version control, interface. Hãy nhìn nó như giai đoạn **implementation → test → package → integrate**.

## 2.1 데이터 입출력 구현 — Data I/O implementation

### 자료구조

Array có truy cập index O(1) nhưng insert/delete giữa mảng thường O(n). Linked List truy cập vị trí bất kỳ O(n), nhưng insert/delete tại node đã biết có thể O(1).

Stack — LIFO — Last In First Out; dùng cho call stack, undo, expression evaluation.  
Queue — FIFO — First In First Out; dùng cho scheduling, buffering.  
Deque cho phép thêm/xóa hai đầu.

Tree cần nắm root, parent, child, sibling, leaf, degree, level, height/depth. Binary tree mỗi node tối đa hai child. Full/complete/perfect binary tree là các khái niệm khác nhau; đề có thể chỉ đưa hình rồi hỏi loại cây.

Traversal:

- Preorder: Root → Left → Right
- Inorder: Left → Root → Right
- Postorder: Left → Right → Root

Binary Search Tree có left < node < right theo ordering rule. Balanced tree giữ chiều cao gần log n để search/insert/delete hiệu quả.

Graph cần phân biệt directed/undirected, weighted/unweighted, degree, path, cycle, connected component. BFS dùng queue; DFS dùng stack/recursion.

### 정렬

Không học sorting chỉ bằng Big-O. Cần biết cơ chế để nhận diện từ mô tả.

Bubble: đổi chỗ phần tử kề nhau, phần tử lớn “nổi” dần về cuối.  
Selection: mỗi vòng chọn min/max rồi đặt vào vị trí.  
Insertion: mở rộng vùng đã sắp và chèn phần tử mới đúng vị trí.  
Quick: chọn pivot, partition rồi đệ quy. Average O(n log n), worst O(n²).  
Merge: chia, sort từng nửa, merge; O(n log n), cần bộ nhớ phụ theo implementation.  
Heap: dùng heap để lặp lấy min/max; O(n log n).

### 검색 / 해싱

Binary Search yêu cầu dữ liệu có thứ tự; mỗi bước giảm search space một nửa, O(log n).

Hashing biến key thành bucket/index. Collision không phải lỗi logic bất thường mà là khả năng tự nhiên vì nhiều key có thể ánh xạ cùng vị trí. Cách xử lý: chaining hoặc open addressing như linear probing, quadratic probing, double hashing.

Load factor tăng cao thường làm collision tăng và performance giảm.

## 2.2 통합 구현 — Integration implementation

Unit module cần interface rõ, input/output rõ, error handling rõ và có khả năng test độc lập.

IPC — Inter-Process Communication gồm pipe, named pipe, message queue, shared memory, socket, semaphore/signal tùy phân loại. Shared memory nhanh vì không phải copy message nhiều lần nhưng cần synchronization cẩn thận. Message queue giảm coupling nhưng có overhead và ordering/delivery semantics cần xem xét.

Integration không chỉ “ghép module”; phải kiểm chứng contract và data flow giữa module.

## 2.3 제품 소프트웨어 패키징 — Product software packaging

Packaging gồm build artifact, dependency, installation/uninstallation, version, release notes, license, DRM khi có nội dung cần bảo vệ.

### 형상 관리 — Configuration Management

Configuration item là artifact được quản lý version/configuration. Các activity thường gặp: identification, version control, change control, configuration audit/status accounting.

Git là distributed version control. SVN là centralized. Không suy luận rằng distributed luôn tốt hơn; đề thường hỏi đúng thuộc tính kiến trúc.

### DRM

DRM — Digital Rights Management — quản lý quyền sử dụng nội dung số. Thành phần có thể gồm content provider, distributor, clearing house, consumer, license, packaging, encryption/key management.

Phân biệt DRM với encryption: encryption bảo mật dữ liệu bằng biến đổi cryptographic; DRM là hệ thống quản lý **quyền sử dụng và phân phối**, trong đó encryption có thể chỉ là một cơ chế.

### Build automation / CI

Build automation biến source + dependency thành artifact có thể deploy lặp lại. CI thường chạy build/test mỗi khi thay đổi code. Jenkins là automation server; Gradle là build automation tool. Không coi hai tool là cùng loại chỉ vì cả hai có thể xuất hiện trong pipeline.

## 2.4 애플리케이션 테스트 관리 — Application test management

### Test principle

Testing phát hiện defect, không chứng minh hệ thống “không có lỗi”. Exhaustive testing gần như không khả thi. Defect clustering gợi ý lỗi tập trung ở một số module. Pesticide paradox nói rằng lặp mãi cùng bộ test sẽ giảm khả năng tìm lỗi mới, nên test cần được xem xét/cập nhật.

### Static vs Dynamic

Static testing không chạy code: review, walkthrough, inspection, static analysis. Dynamic testing chạy software với input/state cụ thể.

### White-box vs Black-box

White-box nhìn cấu trúc bên trong. Coverage cần hiểu:

Statement coverage: mọi statement được chạy ít nhất một lần.  
Decision/Branch coverage: mỗi branch true/false được chạy.  
Condition coverage: từng atomic condition nhận true và false.  
Condition/Decision và MC/DC là mức mạnh hơn tùy phạm vi tài liệu.

Black-box tập trung input/output theo specification: equivalence partitioning, boundary value analysis, decision table, state transition, cause-effect graph, error guessing.

Ví dụ trường tuổi hợp lệ 18–65: boundary value nên kiểm tra quanh 18 và 65 như 17,18,19,64,65,66 thay vì chỉ nhiều giá trị ngẫu nhiên ở giữa.

### Test level

Unit → Integration → System → Acceptance.

Top-down integration dùng **stub** thay module cấp dưới chưa có. Bottom-up dùng **driver** thay module cấp trên chưa có. Đây là cặp rất dễ bị đảo.

Regression testing kiểm tra thay đổi mới không làm hỏng chức năng cũ. Smoke testing kiểm tra nhanh build có đủ ổn để test sâu hơn. Alpha thường tại môi trường developer/organization; beta tại môi trường user thực tế với nhóm người dùng bên ngoài.

### Test oracle

True oracle, sampling oracle, heuristic oracle, consistent oracle được phân loại theo mức biết trước expected result. Đề thường hỏi định nghĩa; hãy gắn “oracle = nguồn quyết định expected result đúng”.

### Performance

Response time là thời gian từ request đến response. Throughput là lượng công việc trong một đơn vị thời gian. Resource usage là CPU/memory/I/O/network consumption. Latency và throughput không phải hai cách gọi cùng một thứ.

Cyclomatic Complexity có thể tính từ control-flow graph theo `M = E - N + 2P`, hoặc với graph connected đơn giản thường là số decision + 1. Nó liên quan số independent path tối thiểu để basis path testing.

## 2.5 인터페이스 구현 — Interface implementation

Interface implementation cần kiểm tra message/data format, mapping, protocol, security, logging, exception handling và retry/idempotency.

Network security có thể dùng TLS/VPN; application/interface layer cần authentication, authorization, input validation, message integrity và secret management. Không coi “mã hóa đường truyền” là đủ bảo mật cho toàn bộ interface.

---

# 3. 데이터베이스 구축 — Database Construction

Môn 3 nên học theo chuỗi **model → key/dependency → normalization → physical design → SQL → transaction/concurrency/recovery**. Nếu tách SQL khỏi relational model sẽ dễ làm đúng câu syntax nhưng sai câu lý thuyết.

## 3.1 논리 데이터베이스 설계 — Logical DB design

### DBMS và three-schema architecture

External schema — 외부 스키마 — view của user/application.  
Conceptual schema — 개념 스키마 — cấu trúc logic tổng thể.  
Internal schema — 내부 스키마 — cách lưu trữ vật lý.

Data independence:

Logical data independence: thay conceptual schema mà hạn chế ảnh hưởng external schema.  
Physical data independence: thay internal storage mà hạn chế ảnh hưởng conceptual/external schema.

### Entity–Relationship model

Entity là đối tượng cần quản lý. Attribute mô tả entity. Relationship biểu diễn liên hệ giữa entity. Cardinality 1:1, 1:N, M:N cho biết số instance có thể liên kết.

M:N thường phải giải quyết bằng associative/junction table khi chuyển sang relational schema.

### Key

Super key: tập attribute xác định duy nhất tuple.  
Candidate key: super key tối thiểu.  
Primary key: candidate key được chọn chính.  
Alternate key: candidate key không được chọn làm primary.  
Foreign key: attribute tham chiếu key của relation khác/cùng relation.  
Composite key: key gồm nhiều attribute.

Minimality áp dụng cho candidate key: bỏ bất kỳ attribute nào thì không còn uniqueness.

### Functional dependency

`X → Y` nghĩa là mỗi giá trị X xác định duy nhất Y trong relation hợp lệ. Functional dependency là nền của normalization.

Partial dependency: non-prime attribute phụ thuộc một phần composite candidate key.  
Transitive dependency: key → A và A → B, B không phụ thuộc trực tiếp key theo dạng cần loại bỏ ở 3NF.

### Normalization

1NF: attribute atomic, không repeating group theo mô hình quan hệ thông thường.  
2NF: 1NF + không partial dependency của non-prime attribute vào candidate key.  
3NF: 2NF + loại transitive dependency không phù hợp.  
BCNF: với mọi non-trivial FD `X → Y`, X phải là super key.  
4NF: xử lý multivalued dependency.  
5NF: xử lý join dependency.

Ví dụ `Enrollment(student_id, course_id, student_name, course_name, grade)` có key `(student_id, course_id)`. `student_name` chỉ phụ thuộc `student_id`, `course_name` chỉ phụ thuộc `course_id`, nên có partial dependencies → chưa đạt 2NF.

Normalization giảm redundancy và anomaly nhưng có thể tăng số join; denormalization đôi khi được dùng có chủ đích vì performance, không có nghĩa normalization “sai”.

### Relational algebra

Selection `σ`: chọn row.  
Projection `π`: chọn column.  
Join: kết hợp relation theo condition.  
Union, Difference, Cartesian Product, Intersection, Division cần nhận diện ý nghĩa.

Đừng nhầm SELECT của SQL với Selection của relational algebra: SQL `SELECT column` gần projection; SQL `WHERE` gần selection.

## 3.2 물리 데이터베이스 설계 — Physical DB design

Physical design chuyển logical model thành structure tối ưu lưu trữ/truy cập.

Index tăng tốc read nhưng tốn storage và làm write/update có thêm cost. B-tree/B+tree phù hợp range search và ordered access. Hash index phù hợp equality lookup nhưng không tự nhiên cho range query.

Clustered organization ảnh hưởng thứ tự lưu vật lý/logical locality tùy DBMS; non-clustered index giữ cấu trúc index riêng trỏ về row/page. Cần đọc theo khái niệm chung, không áp một DBMS cụ thể cho mọi câu hỏi.

Partitioning chia dữ liệu thành partition theo range/list/hash/composite. Horizontal partition chia row; vertical partition chia column.

Database integrity:

Entity integrity: primary key không null và xác định tuple.  
Referential integrity: foreign key phải tham chiếu giá trị tồn tại hoặc null nếu constraint cho phép.  
Domain integrity: giá trị thuộc domain/range/type hợp lệ.

## 3.3 SQL 활용 — SQL utilization

### DDL / DML / DCL / TCL

DDL: CREATE, ALTER, DROP, TRUNCATE theo phân loại phổ biến.  
DML: SELECT, INSERT, UPDATE, DELETE.  
DCL: GRANT, REVOKE.  
TCL: COMMIT, ROLLBACK, SAVEPOINT trong cách phân loại hiện đại.

### SELECT execution reasoning

Logical processing order hữu ích để giải câu khó:

FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY.

`WHERE` lọc row trước grouping. `HAVING` lọc group sau aggregation.

```sql
SELECT department_id, COUNT(*) AS cnt
FROM employee
WHERE active = 'Y'
GROUP BY department_id
HAVING COUNT(*) >= 5;
```

Câu trên không phải “department có ít nhất 5 employee tổng cộng”, mà là có ít nhất 5 employee **active**, vì WHERE đã lọc trước GROUP BY.

### NULL

NULL là unknown/missing, không bằng 0 và không bằng empty string theo SQL standard. So sánh `col = NULL` không đúng cách; dùng `IS NULL` / `IS NOT NULL`.

SQL dùng three-valued logic TRUE/FALSE/UNKNOWN. Điều này đặc biệt quan trọng với `NOT IN` khi subquery có NULL; trong thực tế nên hiểu semantics trước khi chọn đáp án.

### JOIN

INNER JOIN chỉ row match. LEFT OUTER JOIN giữ toàn bộ row bên trái. RIGHT OUTER JOIN giữ bên phải. FULL OUTER JOIN giữ cả hai phía. CROSS JOIN tạo Cartesian product.

Self join là cùng table xuất hiện nhiều alias để mô tả relationship nội bộ như employee-manager.

### Subquery

Scalar subquery trả một giá trị. Single-row/multi-row subquery cần operator phù hợp. `IN`, `EXISTS`, `ANY/SOME`, `ALL` có semantics khác nhau.

Correlated subquery phụ thuộc row của outer query và được đánh giá logic theo từng row outer; optimizer có thể rewrite nhưng khi giải đề hãy reasoning theo semantics.

### Aggregate / Window

COUNT(*), COUNT(column), SUM, AVG, MIN, MAX. `COUNT(column)` bỏ NULL; `COUNT(*)` đếm row.

Window function như `ROW_NUMBER`, `RANK`, `DENSE_RANK` không gom nhiều row thành một row như GROUP BY. `RANK` có gap khi tie; `DENSE_RANK` không có gap; `ROW_NUMBER` luôn tạo sequence duy nhất theo ordering được định nghĩa.

## 3.4 SQL 응용 — SQL application

### Procedural SQL

Procedure thực hiện một chuỗi logic và có thể có IN/OUT parameter. Function thường trả về value. Trigger tự động chạy khi event phù hợp xảy ra. Cursor cho phép xử lý result set theo row trong procedural context.

Tên syntax cụ thể khác nhau giữa Oracle, PostgreSQL, MySQL, SQL Server; đề thường hỏi concept hơn là vendor-specific syntax sâu.

### Transaction — 트랜잭션

ACID:

Atomicity — 원자성: toàn bộ hoặc không gì cả.  
Consistency — 일관성: transaction đưa DB từ valid state sang valid state.  
Isolation — 격리성: transaction concurrent không gây quan sát sai theo isolation guarantee.  
Durability — 영속성: commit tồn tại sau failure.

### Concurrency anomalies

Dirty read: đọc dữ liệu transaction khác chưa commit.  
Non-repeatable read: cùng row đọc hai lần cho kết quả khác vì transaction khác commit update.  
Phantom read: cùng predicate query thấy tập row khác vì insert/delete mới commit.

Lost update: hai transaction cùng đọc rồi update, một update ghi đè update kia nếu concurrency control không ngăn.

### Locking / 2PL

Shared lock cho read và có thể coexist với shared lock. Exclusive lock cho write và xung đột với shared/exclusive lock khác trên cùng resource theo matrix thông thường.

Two-Phase Locking — 2PL có growing phase chỉ acquire lock và shrinking phase chỉ release. Strict 2PL thường giữ exclusive locks đến commit/rollback, giúp tránh cascading rollback và tạo serializability phù hợp.

### Deadlock

Bốn điều kiện Coffman: mutual exclusion, hold and wait, no preemption, circular wait.

Prevention phá ít nhất một điều kiện. Avoidance dùng trạng thái safe/unsafe, ví dụ Banker’s Algorithm. Detection cho phép deadlock xảy ra rồi phát hiện cycle/wait-for graph. Recovery abort/rollback/preempt theo chiến lược.

### Recovery

Log-based recovery dùng before/after image tùy protocol. Undo đảo transaction chưa commit; redo áp lại transaction đã commit nhưng chưa flush đầy đủ. Checkpoint giảm lượng log phải quét khi recovery.

## 3.5 데이터 전환 — Data conversion / migration

Migration cần extraction, cleansing, transformation, loading, validation, reconciliation và rollback plan. Mapping source-to-target phải quản lý type, code conversion, null/default, key relationship.

Quan trọng: “load xong không lỗi” không đồng nghĩa data conversion đúng. Cần kiểm tra count, checksum/aggregate, referential integrity, business rule và sampling/detail reconciliation.

---

# 4. 프로그래밍 언어 활용 — Programming Language Application

Đây là môn cần chuyển từ học thuộc sang **trace execution**. Chỉ đọc syntax không đủ. Mỗi đoạn code phải tự mô phỏng variable/state/call stack.

## 4.1 서버 프로그램 구현 — Server program implementation

Development environment gồm IDE/editor, compiler/interpreter, build tool, dependency manager, version control, runtime, DB, middleware, test/debug tool.

Server program thường phân lớp presentation/controller → service/business → data access/repository. Layering giảm coupling nhưng không có nghĩa mọi hệ thống bắt buộc cùng một architecture.

Batch program xử lý lượng công việc định kỳ hoặc theo lịch, khác interactive request/response. Cần hiểu scheduling, logging, retry, idempotency, checkpoint khi job dài.

## 4.2 프로그래밍 언어 활용 — Language application

### Data type / operator

Phải nắm integer vs floating-point, signed/unsigned ở C khi có phạm vi, boolean, char/string, array/list, object/reference.

Operator precedence chỉ nên học các nhóm quan trọng và dùng ngoặc khi tự viết. Khi thi trace code, đừng dựa vào cảm giác. Ghi từng bước: unary → multiplicative → additive → comparison → equality → logical AND/OR → assignment theo ngôn ngữ cụ thể.

Short-circuit: `A && B` không evaluate B nếu A false; `A || B` không evaluate B nếu A true. Điều này có thể làm side effect không xảy ra.

### C

C dễ ra pointer, array, string, function, struct, operator.

`int *p` là pointer tới int. `*p` dereference lấy/ghi value tại address. `&x` lấy address của x.

Array name trong nhiều expression decay thành pointer tới first element, nhưng array và pointer không hoàn toàn là cùng một type/đối tượng. `p + 1` tăng theo size của pointed type, không phải luôn tăng 1 byte.

Ví dụ:

```c
int a[] = {10, 20, 30};
int *p = a;
printf("%d", *(p + 2));
```

Kết quả là `30` vì `p + 2` trỏ tới `a[2]`.

C string kết thúc bằng `\0`. Buffer size phải tính cả terminator. Câu hỏi về `strlen` và `sizeof` rất dễ nhầm: `strlen` đếm character trước `\0`; `sizeof(array)` cho kích thước array theo byte trong scope còn là array.

Pre-increment `++i` tăng rồi trả value mới; post-increment `i++` trả value cũ rồi tăng. Với expression phức tạp có nhiều side effect lên cùng variable, tránh suy luận nếu behavior không được định nghĩa rõ trong C; đề chuẩn thường tránh undefined behavior.

### Java

Java primitive khác reference. `==` với primitive so value; với object reference kiểm tra reference identity, trong khi `.equals()` thường dùng value equality nếu class override đúng.

Inheritance + overriding tạo dynamic dispatch.

```java
class A { void f(){ System.out.print("A"); } }
class B extends A { @Override void f(){ System.out.print("B"); } }
A x = new B();
x.f();
```

In `B` vì runtime object là `B` và method bị override.

Overloading được chọn theo signature/compile-time context; overriding theo runtime dispatch cho instance method.

`static` member thuộc class, không phải polymorphism kiểu instance overriding thông thường. `final` có nghĩa khác theo context: variable không reassign, method không override, class không extend.

Exception: checked và unchecked là phân loại quan trọng. `try-catch-finally`; `finally` thường chạy dù có exception/return, trừ các tình huống runtime termination đặc biệt.

### Python

Python dynamic typing nhưng object vẫn có type. List mutable; tuple immutable; set unique unordered theo semantic; dict map key→value.

Slicing `a[start:stop:step]` không gồm `stop`.

```python
x = [0, 1, 2, 3, 4]
print(x[1:4])
```

Kết quả `[1, 2, 3]`.

Mutable aliasing rất dễ ra dạng suy luận:

```python
a = [1, 2]
b = a
b.append(3)
print(a)
```

`a` cũng thành `[1, 2, 3]` vì `a` và `b` cùng reference list object.

`is` kiểm tra identity; `==` kiểm tra equality. Không dùng `is` như thay thế chung cho `==`.

### Recursion

Recursion phải có base case và tiến về base case. Khi trace, ghi call stack từ ngoài vào rồi unwind ngược ra.

Ví dụ factorial `f(4)` tạo `4 * f(3)`, `3 * f(2)`, `2 * f(1)`, sau đó trả ngược.

## 4.3 응용 SW 기초 기술 활용 — Basic application software technologies

### Operating System

Process là chương trình đang thực thi với address space/resources riêng; thread là unit execution trong process và thường share address space/resources với thread cùng process.

Process states thường gồm New, Ready, Running, Waiting/Blocked, Terminated. Context switch lưu/khôi phục context khi CPU đổi execution entity.

### CPU scheduling

FCFS: đơn giản nhưng có convoy effect.  
SJF: chọn burst ngắn nhất, tối ưu average waiting trong điều kiện biết burst nhưng dễ starvation.  
SRTF: preemptive SJF.  
Priority: chọn priority cao; low priority có thể starvation, aging giảm starvation.  
Round Robin: time quantum; quantum quá lớn gần FCFS, quá nhỏ làm context-switch overhead cao.

Khi gặp bài tính turnaround/waiting time, vẽ Gantt chart trước rồi tính:

Turnaround = completion − arrival.  
Waiting = turnaround − burst (nếu chỉ một CPU burst tổng quát).

### Memory

Paging chia logical memory thành fixed-size page, physical memory thành frame. Page table map page→frame. Internal fragmentation có thể xuất hiện ở page cuối; paging tránh external fragmentation theo mô hình cơ bản.

Segmentation chia theo logical unit variable-size và có thể external fragmentation.

Virtual memory dùng page replacement khi page fault và frame cần thay.

FIFO thay page vào sớm nhất; có thể gặp Belady’s anomaly. LRU thay page lâu nhất chưa dùng. Optimal thay page sẽ được dùng xa nhất trong tương lai, dùng làm benchmark vì runtime không biết tương lai.

### Deadlock

Cùng 4 điều kiện Coffman đã nêu ở DB/system concurrency. Hãy liên kết thay vì học hai lần tách biệt.

### Network

OSI 7 layers:

7 Application  
6 Presentation  
5 Session  
4 Transport  
3 Network  
2 Data Link  
1 Physical

TCP/IP model thường gộp thành Application, Transport, Internet, Network Access/Link.

TCP connection-oriented, reliable byte stream, sequencing, ACK/retransmission, flow/congestion control. UDP connectionless, datagram, overhead thấp, không bảo đảm delivery/order ở protocol layer.

IP routing thuộc Network layer. Ethernet/MAC switching thuộc Data Link. TCP/UDP thuộc Transport. HTTP/DNS/SMTP application protocols.

### IPv4 subnetting

CIDR `/n` nghĩa n bit network prefix. Số IPv4 address trong subnet = `2^(32-n)`. Trong subnet truyền thống, usable host thường = total − 2 (network + broadcast), nhưng một số special subnet như /31 có semantics đặc biệt; câu thi cơ bản thường dùng công thức truyền thống.

Ví dụ `/26`: `2^(6)=64` address, thông thường 62 usable host.

### Common protocol/port associations

Không nên chỉ học port number, nhưng các cặp kinh điển cần nhận diện: HTTP 80, HTTPS 443, SSH 22, FTP control 21, DNS 53, SMTP 25, POP3 110, IMAP 143. Hãy nhớ đây là well-known defaults; thực tế service có thể cấu hình port khác.

---

# 5. 정보시스템 구축관리 — Information System Construction Management

Môn 5 rộng nhất về management + infrastructure + security. Đây là môn dễ bị “biết IT nhưng vẫn sai” vì nhiều thuật ngữ bảo mật và quản lý có định nghĩa rất sát nhau.

## 5.1 소프트웨어 개발 방법론 활용 — Software development methodology

Waterfall đi theo phase tương đối tuần tự, phù hợp khi requirement ổn định và governance cần checkpoint rõ. Prototype dùng bản mẫu để làm rõ requirement/UX. Spiral lặp theo vòng và nhấn mạnh risk analysis. Iterative/Incremental phát triển qua nhiều iteration/increment. Agile thích nghi feedback nhanh.

### Estimation

COCOMO truyền thống ước lượng effort theo KLOC và project mode (Organic, Semi-detached, Embedded) với coefficient khác nhau. Không cần chỉ thuộc hệ số nếu tài liệu/출제기준 không yêu cầu chi tiết công thức, nhưng phải hiểu input/output và ý nghĩa mode.

Function Point đo kích thước chức năng nhìn từ user, dùng các thành phần như external input/output/inquiry, internal logical file, external interface file trong mô hình truyền thống. Khác KLOC vì không phụ thuộc trực tiếp số dòng code.

### Tailoring

Methodology tailoring là điều chỉnh process/artifact/control phù hợp size, risk, team, domain, compliance. Tailoring không có nghĩa tùy tiện bỏ phase; phải giữ các control cần thiết theo risk và requirement.

## 5.2 IT 프로젝트 정보시스템 구축관리 — IT project / infrastructure construction management

Phần này cần phủ network, software, hardware, database và vận hành.

### Network construction

Switch chủ yếu forward frame dựa trên MAC ở L2; router forward packet dựa trên IP ở L3. L3 switch có routing capability. VLAN chia broadcast domain logic. NAT chuyển đổi address; PAT/NAPT dùng port để nhiều private host share public IP.

Firewall kiểm soát traffic theo rule. IDS phát hiện và cảnh báo; IPS có thể chặn/prevent inline. WAF tập trung HTTP/web application traffic. VPN tạo encrypted tunnel qua network không tin cậy.

Load balancer phân phối traffic qua nhiều backend; health check giúp tránh gửi request đến instance lỗi. L4 load balancing dựa transport information; L7 hiểu application protocol như HTTP và có thể route theo host/path/header.

### Hardware / storage

RAID cần hiểu mục tiêu capacity, performance, redundancy:

RAID 0: striping, không redundancy.  
RAID 1: mirroring.  
RAID 5: striping + distributed single parity, chịu một disk failure.  
RAID 6: dual parity, chịu hai disk failures.  
RAID 10: mirror + stripe, cần nhiều disk nhưng performance/redundancy tốt.

RAID không thay backup. RAID xử lý disk failure; backup xử lý deletion, corruption, ransomware, disaster theo retention/version.

### Virtualization / Cloud / Container

Virtual machine virtualize hardware và chạy guest OS riêng. Container share host kernel theo mô hình phổ biến và isolate process/filesystem/network namespace, nhẹ hơn VM nhưng boundary khác.

IaaS cung cấp compute/network/storage cơ bản. PaaS cung cấp platform/runtime để deploy app. SaaS cung cấp application hoàn chỉnh.

Public/private/hybrid cloud nói về deployment model, khác IaaS/PaaS/SaaS là service model.

### Availability / DR

Availability khác reliability. Availability quan tâm tỷ lệ hệ thống sẵn sàng; reliability khả năng hoạt động đúng liên tục trong khoảng thời gian.

RTO — Recovery Time Objective: thời gian downtime tối đa mục tiêu.  
RPO — Recovery Point Objective: mức data loss theo thời gian có thể chấp nhận.

Nếu RPO = 15 phút, backup/replication strategy phải đủ để mất tối đa khoảng 15 phút dữ liệu theo objective. Nếu RTO = 1 giờ, service cần được khôi phục trong target một giờ.

## 5.3 소프트웨어 개발 보안 구축 — Secure software development

### CIA triad

Confidentiality — 기밀성: chỉ chủ thể được phép đọc.  
Integrity — 무결성: dữ liệu không bị sửa trái phép.  
Availability — 가용성: dịch vụ/dữ liệu sẵn sàng khi cần.

Authentication — 인증 — “bạn là ai?”.  
Authorization — 인가 — “bạn được làm gì?”.  
Accounting/Auditing — 기록/감사 — “đã làm gì?”.

### Cryptography

Symmetric encryption dùng cùng/shared secret key, nhanh, phù hợp bulk encryption nhưng key distribution khó. AES là ví dụ phổ biến.

Asymmetric encryption dùng public/private key pair, hỗ trợ key exchange, encryption/signature theo algorithm/use case, nhưng chậm hơn. RSA/ECC là ví dụ family phổ biến.

Hash function là one-way mapping, không phải encryption vì không có decrypt key. SHA-2/SHA-3 là hash families. Password nên dùng password hashing KDF có salt và cost như PBKDF2/bcrypt/scrypt/Argon2 trong thực tế; không lưu plain SHA-256 password đơn thuần.

Digital signature thường hash message rồi ký digest bằng private key theo scheme; verifier dùng public key để kiểm tra authenticity/integrity/non-repudiation theo assumptions phù hợp.

### Common attack classes

SQL Injection: input bị ghép thành SQL làm thay đổi query. Defense chính: parameterized query/prepared statement, validation và least privilege.

XSS: attacker đưa script/content hoạt động trong browser context. Stored, Reflected, DOM-based là các loại phổ biến. Defense: context-aware output encoding, safe templating, CSP hỗ trợ, validation/sanitization phù hợp.

CSRF: browser của user đã authenticated bị dụ gửi request ngoài ý muốn. Defense: CSRF token, SameSite cookie, kiểm tra origin/re-authentication tùy operation.

Command Injection: untrusted input điều khiển OS command. Dùng API thay shell, allowlist và escaping đúng context nếu buộc phải invoke shell.

Path Traversal: `../` hoặc biến thể vượt thư mục cho phép. Canonicalize/resolve path, allowlist base path và kiểm tra containment.

Buffer Overflow: ghi vượt memory boundary, đặc biệt C/C++. Defense gồm memory-safe language, bounds checking, ASLR, stack canary, DEP/NX nhưng prevention ở source vẫn quan trọng.

Race condition/TOCTOU: state thay đổi giữa check và use. Dùng atomic operation, locking/transaction và secure API.

### Access control models

DAC — Discretionary Access Control: owner có quyền phân phối permission.  
MAC — Mandatory Access Control: policy/label bắt buộc, user không tùy ý cấp lại.  
RBAC — Role-Based Access Control: quyền gắn role.  
ABAC — Attribute-Based Access Control: decision dựa attribute của subject/resource/action/context.

Least privilege và separation of duties là nguyên tắc xuyên suốt.

## 5.4 시스템 보안 구축 — System security construction

### Malware / attack vocabulary

Virus cần host và lan khi host thực thi. Worm tự lan qua network. Trojan giả dạng hợp pháp để thực hiện hành vi độc hại. Ransomware mã hóa/khóa tài nguyên để đòi tiền. Rootkit che giấu/duy trì quyền kiểm soát. Bot/botnet tập hợp host bị điều khiển.

Phishing lừa user qua message/site; spear phishing nhắm mục tiêu cụ thể. Pharming chuyển hướng nạn nhân bằng DNS/host manipulation. Smishing dùng SMS. Vishing dùng voice.

DoS làm cạn resource từ một/few source; DDoS từ nhiều distributed source. SYN flood lợi dụng TCP handshake bằng nhiều half-open connection. Amplification dùng protocol phản hồi lớn hơn request và spoof source.

### Network attack concepts

Sniffing nghe lén traffic. Spoofing giả identity/address. MITM đứng giữa hai bên. Session hijacking chiếm session. ARP spoofing đầu độc mapping IP-MAC trong LAN. DNS poisoning thao túng name resolution/cache.

### Security control categories

Preventive ngăn xảy ra. Detective phát hiện. Corrective khắc phục. Deterrent răn đe. Recovery khôi phục. Một control có thể có nhiều vai trò nhưng đề thường mô tả mục tiêu chính.

Physical, administrative/managerial, technical/logical là cách phân loại theo nature.

### Security operations

Logging chỉ có giá trị nếu time sync, retention, integrity và monitoring phù hợp. SIEM thu thập/correlate event từ nhiều nguồn. SOC là tổ chức/quy trình vận hành security monitoring/response, không phải một tool duy nhất.

Vulnerability assessment tìm weakness; penetration testing chủ động khai thác có kiểm soát để đánh giá exploitability/impact. Patch management giảm known vulnerability nhưng cần inventory, prioritization, testing và rollout/rollback.

Backup strategy cần xét full/incremental/differential, retention, offsite/immutable copy và restore test. Backup chưa từng restore-test không bảo đảm recovery thực tế.

---

# 6. Các cặp khái niệm phải phân biệt ngay lập tức

Đây là nhóm dễ mất điểm dù “đã từng học”. Mỗi cặp phải nói được **một câu phân biệt bản chất**, không chỉ đọc định nghĩa riêng rẽ.

| Cặp | Điểm phân biệt cốt lõi |
|---|---|
| Verification / Validation | làm sản phẩm đúng đặc tả / làm đúng sản phẩm người dùng cần |
| Functional / Non-functional requirement | hệ thống làm gì / hệ thống phải đạt chất lượng hoặc constraint nào |
| Cohesion / Coupling | liên kết bên trong module / phụ thuộc giữa module |
| Overloading / Overriding | cùng tên khác parameter / subclass định nghĩa lại behavior |
| Adapter / Decorator / Proxy | đổi interface / thêm behavior / kiểm soát truy cập hoặc đại diện |
| Stack / Queue | LIFO / FIFO |
| BFS / DFS | queue / stack hoặc recursion |
| Stub / Driver | thay module cấp dưới / thay module cấp trên |
| Static / Dynamic testing | không chạy code / chạy code |
| White-box / Black-box | cấu trúc nội bộ / behavior theo specification |
| WHERE / HAVING | lọc row trước group / lọc group sau aggregation |
| Candidate / Primary / Foreign key | key tối thiểu khả dĩ / key được chọn / key tham chiếu |
| 2NF / 3NF / BCNF | bỏ partial / bỏ transitive / mọi determinant phải là super key |
| Dirty / Non-repeatable / Phantom | đọc uncommitted / cùng row đổi / tập row đổi |
| Undo / Redo | đảo transaction chưa commit / áp lại transaction đã commit |
| Process / Thread | execution context riêng / unit execution chia sẻ process resources |
| Paging / Segmentation | fixed-size / logical variable-size |
| TCP / UDP | reliable connection-oriented stream / connectionless datagram |
| Authentication / Authorization | bạn là ai / bạn được làm gì |
| Encryption / Hashing | reversible bằng key phù hợp / one-way digest |
| Symmetric / Asymmetric | shared secret / public-private key pair |
| IDS / IPS | detect-alert / detect-and-block inline |
| Firewall / WAF | network/transport rule rộng / web application HTTP-focused |
| RAID / Backup | availability khi disk lỗi / khôi phục dữ liệu theo version/disaster |
| RTO / RPO | thời gian phục hồi / mức mất dữ liệu theo thời gian |
| VM / Container | guest OS isolation / share host kernel theo mô hình phổ biến |
| IaaS / PaaS / SaaS | infrastructure / platform / application |

---

# 7. Những dạng phải làm được bằng tay

Nếu chỉ đọc lý thuyết mà không làm được các thao tác sau thì coverage chưa đủ.

## 7.1 Code tracing

Với C/Java/Python, phải trace được:

- vòng lặp lồng nhau;
- recursion;
- array/list/string indexing;
- pointer cơ bản của C;
- pre/post increment;
- inheritance/overriding Java;
- mutable aliasing Python;
- short-circuit logic;
- function call và scope cơ bản.

Cách làm: tạo bảng từng dòng gồm `step | statement | variable state | output`. Không tính nhẩm toàn đoạn code.

## 7.2 SQL reasoning

Phải tự viết/đọc được:

- SELECT + WHERE + GROUP BY + HAVING + ORDER BY;
- INNER/LEFT JOIN;
- subquery IN/EXISTS;
- aggregate + NULL;
- INSERT/UPDATE/DELETE;
- GRANT/REVOKE;
- transaction COMMIT/ROLLBACK;
- normalization từ functional dependency đơn giản.

## 7.3 Scheduling

Cho arrival/burst/priority/quantum, phải vẽ Gantt chart cho FCFS, SJF/SRTF, Priority, Round Robin rồi tính waiting/turnaround.

## 7.4 Page replacement

Cho reference string và số frame, phải mô phỏng FIFO/LRU/Optimal và đếm page fault. Dùng bảng frame theo từng reference, không làm bằng trực giác.

## 7.5 Subnetting

Từ CIDR phải suy được số host, network range/broadcast trong bài cơ bản. Cần nhớ prefix dài hơn → subnet nhỏ hơn.

## 7.6 Tree / graph / complexity

Phải viết được preorder/inorder/postorder; nhận biết BFS/DFS; so sánh O(1), O(log n), O(n), O(n log n), O(n²), O(2^n), O(n!).

## 7.7 Transaction / locking

Từ lịch interleaving đơn giản phải nhận diện dirty read, lost update, non-repeatable read, phantom và deadlock.

---

# 8. 과락 방지 — Checklist chống rớt từng môn

Mục tiêu của checklist không phải tự tin mơ hồ. Chỉ đánh dấu khi có thể **giải thích bằng lời của mình và làm một câu biến thể**.

## Môn 1

- [ ] phân loại functional / non-functional requirement;
- [ ] đọc DFD/UML và chọn đúng diagram theo mục đích;
- [ ] phân biệt Scrum / XP / Agile;
- [ ] phân biệt wireframe / mockup / prototype / storyboard;
- [ ] nhớ và hiểu cohesion/coupling theo thứ tự;
- [ ] hiểu OOP, SOLID, GoF pattern cốt lõi;
- [ ] hiểu EAI/ESB, JSON/XML/AJAX và interface security.

## Môn 2

- [ ] stack/queue/tree/graph/traversal;
- [ ] sorting/search/hash và complexity;
- [ ] IPC/module integration;
- [ ] SCM/Git/SVN/release/package/DRM;
- [ ] static/dynamic, white/black box;
- [ ] test level, stub/driver, oracle;
- [ ] performance metric và cyclomatic complexity;
- [ ] interface implementation/verification.

## Môn 3

- [ ] schema/data independence/ER model;
- [ ] all key types và functional dependency;
- [ ] 1NF→BCNF, anomaly;
- [ ] relational algebra;
- [ ] index/partition/integrity;
- [ ] SQL join/group/subquery/NULL;
- [ ] procedure/function/trigger;
- [ ] ACID/isolation anomaly;
- [ ] lock/2PL/deadlock/recovery;
- [ ] migration validation.

## Môn 4

- [ ] C pointer/array/string/operator;
- [ ] Java inheritance/overload/override/static/final/exception;
- [ ] Python list/tuple/set/dict/slicing/reference;
- [ ] recursion và execution trace;
- [ ] process/thread/scheduling;
- [ ] paging/segmentation/page replacement;
- [ ] deadlock;
- [ ] OSI/TCP-IP/TCP/UDP/protocol;
- [ ] IPv4/CIDR cơ bản.

## Môn 5

- [ ] lifecycle/methodology/estimation/tailoring;
- [ ] network device/VLAN/NAT/load balancing;
- [ ] RAID/storage/virtualization/cloud;
- [ ] availability/RTO/RPO/backup/DR;
- [ ] CIA/authentication/authorization;
- [ ] symmetric/asymmetric/hash/signature;
- [ ] SQLi/XSS/CSRF/command/path/buffer/race;
- [ ] DAC/MAC/RBAC/ABAC;
- [ ] malware/phishing/DoS/spoofing/MITM;
- [ ] firewall/IDS/IPS/WAF/VPN/SIEM;
- [ ] vulnerability/patch/backup/incident fundamentals.

---

# 9. Cách sử dụng bộ lesson hiện có với master guide này

Các folder môn hiện tại chứa nhiều lesson nhỏ được sinh/tổng hợp từ nhiều nguồn và có phần trùng chủ đề. Không cần đọc tuần tự hàng chục file như một cuốn sách từ trang 1 đến cuối.

Quy trình hợp lý hơn là:

**Bước 1 — Coverage pass.** Đọc master guide và đánh dấu phần hoàn toàn chưa biết.  
**Bước 2 — Deep pass.** Mở `01-tai-lieu-hoc-day-du.md` của đúng môn và lesson liên quan để đọc giải thích dài, ví dụ và terminology.  
**Bước 3 — Retrieval pass.** Đóng tài liệu và tự giải thích lại khái niệm, tự trace code/SQL/calculation.  
**Bước 4 — Mixed practice.** Trộn câu từ nhiều chương để tránh chỉ nhớ context ngay trước đó.  
**Bước 5 — Error log.** Mỗi câu sai ghi `khái niệm bị nhầm → tại sao nhầm → quy tắc phân biệt → một ví dụ mới`. Không chỉ ghi đáp án A/B/C/D.

Sau hai lần thi chưa đạt, điều quan trọng nhất không phải đọc lại toàn bộ tài liệu theo cùng một cách, mà là xác định **coverage hole** và **confusion pair**. Một câu sai vì chưa từng thấy thuật ngữ là coverage hole. Một câu sai vì nhầm hai thuật ngữ đã học là discrimination/retrieval problem. Một câu sai vì tính nhầm code/SQL là procedural practice problem. Ba loại lỗi cần cách sửa khác nhau.

---

# 10. Nguồn kiểm chứng phạm vi

Phạm vi thi và điều kiện đỗ phải ưu tiên Q-Net (한국산업인력공단) làm nguồn chính thức. Năm 2026 có 출제기준 riêng áp dụng `2026.1.1 ~ 2026.12.31`.

Để kiểm tra cách các mục chính thức được triển khai thành chapter học, đối chiếu nhiều giáo trình 2026 như 시나공, 수제비, 흥달쌤 và curriculum đào tạo nghề; không dùng một giáo trình duy nhất làm “chuẩn đề”.

Tài liệu này cố ý **không sao chép câu hỏi 기출 nguyên văn**. Ví dụ/code được viết lại để luyện cơ chế và tránh phụ thuộc vào việc nhớ đáp án của một câu cụ thể.

---

# 11. Definition of Done trước khi thi lại

Không coi “đã đọc hết file” là hoàn thành. Chỉ coi một chương đã sẵn sàng khi đáp ứng cả bốn điều kiện:

1. Có thể giải thích khái niệm chính bằng tiếng Việt nhưng vẫn nhận ra thuật ngữ Korean/English trong đề.
2. Có thể phân biệt nó với ít nhất một khái niệm gần nhất mà không nhìn tài liệu.
3. Với phần procedural, có thể tự làm một ví dụ mới: code trace, SQL, normalization, scheduling, page replacement, subnetting hoặc transaction.
4. Làm mixed practice sau vài ngày vẫn suy ra được, không chỉ nhớ vì vừa đọc.

Nếu một môn có bất kỳ vùng lớn nào trong checklist chưa đạt, ưu tiên lấp vùng đó trước khi tối ưu điểm môn mạnh. Đây là cách trực tiếp nhất để giảm rủi ro 과락 và đồng thời nâng điểm trung bình.