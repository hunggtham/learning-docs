# Môn 2 — 소프트웨어 개발: Deep Dive 2026

> Môn 2 dễ tạo cảm giác “biết rồi” vì nhiều khái niệm quen thuộc với developer. Tuy nhiên đề thi thường hỏi theo thuật ngữ giáo trình, thứ tự process, complexity, test technique hoặc tool category. Vì vậy phải chuyển kiến thức nghề nghiệp thành **khả năng phân loại chính xác theo cách đề hỏi**.

## 1. 데이터 입출력 구현 — Data I/O implementation

### 1.1 자료구조 — Data Structures

Data structure nên học qua ba câu hỏi: dữ liệu được bố trí thế nào, operation chính là gì, và trade-off thời gian/bộ nhớ ra sao.

**Array** lưu phần tử liên tục nên truy cập index O(1), nhưng chèn/xóa giữa thường tốn O(n) vì phải dịch phần tử. **Linked List** không cần vùng nhớ liên tục, chèn/xóa khi đã có node reference có thể O(1), nhưng truy cập phần tử thứ k cần đi tuần tự O(n).

**Stack** dùng LIFO, operation cơ bản push/pop. Ứng dụng: call stack, undo, expression evaluation, DFS. **Queue** dùng FIFO, enqueue/dequeue. Ứng dụng: scheduling, buffering, BFS. **Deque** cho phép insert/delete hai đầu.

### 1.2 Tree

Tree có root, parent, child, sibling, leaf, level/depth, degree. Binary tree giới hạn mỗi node tối đa hai child.

Traversal phải làm được bằng tay:

- Preorder: Root → Left → Right.
- Inorder: Left → Root → Right.
- Postorder: Left → Right → Root.

Trong Binary Search Tree, với key phân biệt, subtree trái nhỏ hơn node và subtree phải lớn hơn node. Inorder traversal của BST cho sequence tăng dần.

Heap không phải BST. Max-Heap chỉ bảo đảm parent ≥ child, không bảo đảm toàn bộ subtree trái nhỏ hơn subtree phải.

### 1.3 Graph

Graph gồm vertex và edge. Directed graph phân biệt hướng; undirected graph không. Weighted graph có trọng số cạnh.

BFS dùng Queue và đi theo layer; DFS thường dùng recursion/Stack và đi sâu trước. Khi đề hỏi shortest path trong **unweighted graph**, BFS là lựa chọn nền tảng. Với weighted graph không âm, nghĩ tới Dijkstra. Với all-pairs shortest path, Floyd–Warshall thường là thuật ngữ quen thuộc.

Minimum Spanning Tree khác shortest path. Prim và Kruskal nhằm nối tất cả vertex với tổng trọng số cạnh nhỏ nhất mà không tạo cycle, không phải tìm đường ngắn nhất từ một source.

### 1.4 Expression notation

Infix: `A + B`. Prefix: `+ A B`. Postfix: `A B +`.

Khi chuyển infix sang postfix, operator precedence và parenthesis quyết định vị trí operator. Đừng chỉ học ví dụ cố định; hãy luyện stack algorithm.

Ví dụ:

`A + B * C` → `A B C * +`.

`(A + B) * C` → `A B + C *`.

### 1.5 Sorting

Các thuật toán thường cần biết idea và complexity điển hình:

| Algorithm | Ý tưởng | Average | Worst | Stable điển hình |
|---|---|---:|---:|---|
| Bubble | đổi cặp kề sai thứ tự | O(n²) | O(n²) | Có |
| Selection | chọn min/max mỗi lượt | O(n²) | O(n²) | Không điển hình |
| Insertion | chèn phần tử vào prefix đã sort | O(n²) | O(n²) | Có |
| Merge | chia rồi merge | O(n log n) | O(n log n) | Có |
| Quick | partition quanh pivot | O(n log n) | O(n²) | Không điển hình |
| Heap | dùng heap | O(n log n) | O(n log n) | Không |

Quick Sort thường nhanh trong thực tế nhưng pivot xấu có thể dẫn tới O(n²). Merge Sort ổn định và bảo đảm O(n log n) nhưng cần thêm memory cho merge trong implementation phổ biến.

### 1.6 Searching

Linear Search O(n) và không cần sorted data. Binary Search O(log n) nhưng yêu cầu dữ liệu có thứ tự và truy cập vị trí giữa hiệu quả.

### 1.7 Hashing

Hashing map key thành bucket/index. Collision là hai key map vào cùng vị trí.

Collision resolution thường gồm:

- Separate Chaining: mỗi bucket chứa list/structure các entry.
- Open Addressing: tìm slot khác trong table, như Linear Probing, Quadratic Probing, Double Hashing.

Linear Probing dễ primary clustering. Double Hashing giảm pattern clustering bằng hash thứ hai.

Load factor `α = number of entries / table size` ảnh hưởng performance. Khi α quá cao trong open addressing, probe chain tăng mạnh.

## 2. 통합 구현 — Integration Implementation

### 2.1 Unit Module

Unit module là phần chức năng có boundary rõ, input/output và responsibility cụ thể. Module specification cần đủ rõ để implementation và test độc lập.

Common module nên chú ý correctness, clarity, completeness, consistency và traceability theo cách diễn đạt của giáo trình. Ý chính là module dùng chung phải có contract rõ và không gây interpretation khác nhau giữa team.

### 2.2 IPC — Inter-Process Communication

IPC cho phép process trao đổi data/synchronization. Các cơ chế thường gặp: pipe, named pipe, message queue, shared memory, socket, semaphore.

Shared Memory thường nhanh vì nhiều process truy cập cùng vùng memory nhưng cần synchronization. Message Queue tạo boundary rõ hơn nhưng có overhead copy/queue. Semaphore chủ yếu đồng bộ quyền truy cập resource, không phải kênh truyền payload lớn.

### 2.3 Integration

Khi tích hợp module/service, cần kiểm soát interface contract, data mapping, error code, transaction boundary, retry và idempotency. Một retry không an toàn có thể tạo duplicate operation; vì vậy “retry” không tự động là giải pháp cho mọi interface error.

## 3. 제품 소프트웨어 패키징 — Product Software Packaging

### 3.1 Packaging

Packaging không chỉ zip file. Nó bao gồm executable/artifact, dependency, environment/configuration, installation procedure, version information, release note và manual cần thiết để deploy/use sản phẩm.

### 3.2 Release Note

Release note thường chứa version, release date, changed features, fixed defects, known issues, dependency/environment và upgrade/migration notes. Đề có thể hỏi thành phần nào không thuộc release note; hãy nhớ release note giao tiếp **thay đổi của release**, không phải design specification chi tiết.

### 3.3 DRM

DRM — Digital Rights Management — bảo vệ quyền sử dụng nội dung số. Các khái niệm có thể xuất hiện: content provider, content distributor, clearing house, consumer, packaging, license và rights expression.

DRM khác encryption thuần túy. Encryption chỉ là một cơ chế kỹ thuật; DRM còn quản lý quyền sử dụng, phân phối, license và policy.

### 3.4 Configuration Management — 형상 관리

SCM kiểm soát artifact và thay đổi trong vòng đời software. Các hoạt động nền tảng thường xoay quanh identification, version control, change control, status accounting và audit.

Version Control là một phần của SCM, không phải toàn bộ SCM.

Centralized VCS như SVN dựa nhiều vào central repository. Distributed VCS như Git cho mỗi clone một repository với history đầy đủ.

### 3.5 Build Automation

Build automation tự động compile, test, package và đôi khi deploy. Jenkins là automation server/orchestrator; Gradle/Maven là build tools. Đề dễ trộn category: Jenkins không phải compiler và Git không phải build tool.

## 4. 애플리케이션 테스트 관리 — Application Test Management

### 4.1 Nguyên lý test

Một số nguyên lý kinh điển cần hiểu:

Testing cho thấy **sự hiện diện của defect**, không chứng minh tuyệt đối software không còn defect. Exhaustive testing thường bất khả thi. Defect có xu hướng tập trung ở một số module — defect clustering. Test case cần thay đổi theo thời gian để tránh pesticide paradox. Testing phụ thuộc context. Sản phẩm không có bug vẫn có thể thất bại nếu không đáp ứng nhu cầu — absence-of-errors fallacy.

### 4.2 Verification vs Validation

Verification kiểm tra artifact có tuân specification/process không. Validation kiểm tra software có đáp ứng nhu cầu người dùng/thực tế không. Hai khái niệm này lặp lại từ Môn 1; nếu vẫn nhầm thì xem là lỗi nền tảng.

### 4.3 White-box testing

White-box dựa vào internal logic/code structure.

Coverage thường gặp:

- Statement Coverage: mỗi statement được execute ít nhất một lần.
- Decision/Branch Coverage: mỗi outcome của decision được thực hiện.
- Condition Coverage: mỗi atomic condition có True và False.
- Condition/Decision Coverage: kết hợp condition và decision.
- Modified Condition/Decision Coverage — MC/DC: mỗi condition chứng minh ảnh hưởng độc lập tới decision outcome.

Nếu một `if (A && B)` chỉ test `(T,T)` và `(F,T)`, ta có thể cover cả outcome decision T/F nhưng chưa chắc cover độc lập mọi condition theo tiêu chí mạnh hơn.

### 4.4 Cyclomatic Complexity

McCabe Cyclomatic Complexity đo số path độc lập tuyến tính. Công thức phổ biến:

`V(G) = E - N + 2P`

với E edge, N node, P số connected component; control flow graph của một routine thường P=1. Một cách khác thường dùng là số decision point + 1 trong cấu trúc đơn giản.

Complexity cao thường gợi ý nhiều path cần test và code khó maintain hơn.

### 4.5 Black-box testing

Black-box dựa specification và input/output, không cần biết code bên trong.

**Equivalence Partitioning** chia input thành class được kỳ vọng xử lý giống nhau. **Boundary Value Analysis** tập trung ranh giới vì defect hay xuất hiện tại min/max và sát biên. **Decision Table** phù hợp khi nhiều condition kết hợp rule. **State Transition Testing** phù hợp behavior phụ thuộc state. **Cause-Effect Graph** biểu diễn quan hệ logic giữa condition và effect.

### 4.6 Test levels

Unit Test kiểm tra module/class nhỏ. Integration Test kiểm tra interaction giữa module. System Test kiểm tra hệ thống hoàn chỉnh với requirement. Acceptance Test xác nhận system chấp nhận được cho user/business.

Trong V-Model, development artifact ở bên trái tương ứng test level ở bên phải. Mục tiêu là trace verification/validation từ requirement/design tới test.

### 4.7 Top-down vs Bottom-up integration

Top-down bắt đầu từ module cấp cao; module thấp chưa có có thể thay bằng **Stub**. Bottom-up bắt đầu từ module cấp thấp; module gọi phía trên chưa có có thể thay bằng **Driver**.

Mẹo không học vẹt: Stub **được gọi** như một module con giả. Driver **gọi** module đang test như module cha giả.

### 4.8 Test Oracle

Oracle là nguồn/cơ chế quyết định output có đúng không. Các loại hay gặp trong giáo trình: True Oracle, Sampling Oracle, Heuristic Oracle, Consistent Oracle.

True Oracle có expected result chính xác. Sampling Oracle chỉ kiểm tra sample. Heuristic Oracle dùng heuristic/approximation khi không thể biết expected hoàn hảo. Consistent Oracle so sánh tính nhất quán qua implementation/result liên quan.

### 4.9 Test Harness

Test Harness là môi trường hỗ trợ thực thi test, có thể gồm driver, stub, test script, test data, monitor và tool. Đừng đồng nhất Harness với một test automation tool riêng lẻ.

### 4.10 Performance

Các metric cần phân biệt:

- Response Time: thời gian từ request tới response.
- Throughput: lượng work/request xử lý mỗi đơn vị thời gian.
- Resource Usage: CPU, memory, disk, network.
- TPS: transactions per second.

Latency thấp không đồng nghĩa throughput cao và ngược lại.

## 5. 인터페이스 구현 — Interface Implementation

### 5.1 Implementation

Interface implementation cần mapping data, serialization, protocol handling, authentication, transaction/error policy và logging/monitoring. Câu hỏi có thể đưa JSON/XML/API nhưng mục tiêu là nhận ra component nào đang làm **data exchange** chứ không phải business logic.

### 5.2 EAI và ESB

EAI giải bài toán tích hợp enterprise application. Kiểu triển khai có thể Point-to-Point, Hub & Spoke, Message Bus, Hybrid. ESB thường cung cấp bus hạ tầng cho routing, transformation và service mediation.

### 5.3 Interface security

Network zone có thể dùng encryption/protocol security. Application zone cần validation, authentication/authorization, secure coding. Database zone cần access control, encryption, audit và integrity.

Integrity check có thể dùng hash/checksum. Hash không dùng để khôi phục plaintext và không phải encryption.

### 5.4 Interface verification tools

Tool category thường gặp gồm xUnit-style unit test framework, API testing tools, static/dynamic analysis, monitoring/APM. Hãy phân loại tool theo **mục đích**, không học tên tool đơn độc vì tool ecosystem thay đổi.

## 6. Các cặp dễ mất điểm

| Cặp | Phân biệt |
|---|---|
| Stack vs Queue | LIFO vs FIFO |
| BFS vs DFS | Queue/layer vs Stack/depth |
| BST vs Heap | total ordering theo subtree vs parent-child heap property |
| Shortest Path vs MST | đường giữa điểm vs cây nối toàn graph |
| Binary Search vs Hash | O(log n) trên sorted order vs mapping key vào bucket |
| SCM vs Version Control | quản lý configuration/change toàn diện vs lịch sử version |
| Jenkins vs Gradle | automation server vs build tool |
| White-box vs Black-box | internal structure vs specification behavior |
| Stub vs Driver | module con giả vs module cha giả |
| Response Time vs Throughput | latency từng request vs lượng work/time |
| Hash vs Encryption | one-way digest/integrity vs reversible confidentiality với key phù hợp |

## 7. Procedural drills

### Drill 1 — Traversal

Cho tree có root A, left B, right C; B có D và E; C có F. Viết Preorder, Inorder và Postorder.

### Drill 2 — Postfix

Chuyển `(A + B) * (C - D) / E` sang postfix bằng stack.

### Drill 3 — Complexity

Vì sao Binary Search không phù hợp trực tiếp với linked list dù về lý thuyết vẫn có thể tìm “middle” bằng traversal?

### Drill 4 — Hash collision

Table size 10, hash `h(k)=k mod 10`, insert 12, 22, 32 bằng Linear Probing. Các key nằm ở index nào? Sau đó giải thích primary clustering.

### Drill 5 — Coverage

Với `if (A || B)`, tự tạo test tối thiểu để đạt Decision Coverage rồi so sánh với test cần để chứng minh từng condition ảnh hưởng độc lập.

### Drill 6 — Stub/Driver

Trong top-down integration, module `OrderService` gọi `PaymentClient` nhưng PaymentClient chưa hoàn thành. Ta cần Stub hay Driver? Vì sao?

### Drill 7 — Performance

Một API response time giảm từ 500ms xuống 200ms nhưng số request/second không tăng vì DB connection pool vẫn giới hạn. Metric nào cải thiện, metric nào gần như không đổi?

## 8. 과락 방지 checklist — Môn 2

Phải tự làm được:

- traversal tree, BFS/DFS và phân biệt shortest path/MST;
- chuyển infix/prefix/postfix cơ bản;
- nhận diện complexity và đặc tính chính của sorting/searching;
- giải collision hashing cơ bản;
- phân loại IPC và vai trò synchronization;
- giải thích SCM, version control, packaging, DRM, build automation;
- phân biệt test principle, level, technique và coverage;
- tính cyclomatic complexity ở control flow đơn giản;
- phân biệt Stub/Driver và Top-down/Bottom-up;
- phân biệt test oracle/harness;
- nhận biết performance metric;
- giải thích EAI/ESB và interface security.

Nếu chỉ đọc được định nghĩa nhưng không làm được drill, vẫn chưa đủ an toàn cho 필기.
