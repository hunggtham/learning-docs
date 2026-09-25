# 정보처리기사 필기 2026 — Cross-Subject Connection Map

> File này dùng sau 5 deep-dive. Mục tiêu không phải học thêm một “môn thứ sáu”, mà nối các khái niệm đang nằm rời rạc giữa 5 môn thành một mô hình hệ thống thống nhất. Khi đề đổi cách diễn đạt, chính các liên kết này giúp suy ra đáp án thay vì phụ thuộc vào việc nhớ đúng một câu định nghĩa.
>
> Thuật ngữ quan trọng giữ tiếng Hàn, kèm English và nghĩa Việt khi cần. Các scenario và câu hỏi trong file đều được viết mới.

---

## 0. Một hệ thống thật không chia thành 5 môn

Trong đề thi, kiến thức được chia thành 소프트웨어 설계, 소프트웨어 개발, 데이터베이스 구축, 프로그래밍 언어 활용 và 정보시스템 구축 관리. Trong hệ thống thật, năm vùng này xảy ra đồng thời.

Một yêu cầu “người dùng có thể thanh toán đơn hàng trong dưới hai giây và không bị tính tiền hai lần” bắt đầu ở **요구사항 — requirement**, đi qua **애플리케이션 설계 — application design**, trở thành code và test trong **소프트웨어 개발**, lưu trạng thái bằng transaction trong **데이터베이스**, chạy trên process/thread, network và server trong **응용 SW 기초 기술**, rồi cần logging, deployment, security, availability và recovery trong **정보시스템 구축 관리**.

Nếu chỉ học theo từng môn, ta có thể biết tất cả các từ nhưng vẫn không biết chúng ghép với nhau thế nào. Vì vậy file này dùng một câu hỏi xuyên suốt:

> “Khái niệm này nằm ở đâu trong vòng đời request và nó bảo vệ điều gì?”

---

# 1. Từ 요구사항 đến 테스트 — Requirements ↔ Testing

## 1.1 Requirement không kết thúc ở tài liệu đặc tả

Functional Requirement — 기능 요구사항 — nói hệ thống phải làm gì. Non-functional Requirement — 비기능 요구사항 — nói hệ thống phải đạt chất lượng hoặc constraint nào.

Nhưng requirement chỉ có giá trị khi nó có thể được **검증 — verification/validation**. Vì vậy requirement và test có quan hệ traceability.

Ví dụ:

```text
R1: 사용자 로그인 가능
    User can log in

R2: 로그인 응답은 95% 요청에서 500ms 이하
    95% login requests finish within 500 ms

R3: 5회 연속 실패 시 계정 잠금
    Lock account after 5 consecutive failures
```

R1 dẫn tới functional test. R2 dẫn tới performance test với percentile/response-time criterion. R3 dẫn tới security/business-rule test, đồng thời liên quan state management và concurrency.

### Connection cần nhớ

```text
Requirement
    ↓
Acceptance criterion
    ↓
Design decision
    ↓
Implementation
    ↓
Test case
    ↓
Operational metric
```

Nếu đề hỏi “thay đổi requirement nhưng test case không được cập nhật”, vấn đề không chỉ là test. Đó là đứt **추적성 — traceability** giữa requirement và verification artifact.

## 1.2 Verification vs Validation nối Môn 1 và Môn 2

Verification hỏi: sản phẩm có được xây đúng theo specification không?

Validation hỏi: specification/sản phẩm có thực sự giải quyết nhu cầu stakeholder không?

Một unit test có thể verify code đúng spec nhưng không chứng minh spec đúng nhu cầu người dùng. Ngược lại, user acceptance test có thể phát hiện hệ thống “đúng tài liệu nhưng sai nhu cầu”.

---

# 2. UML, OOP và Design Pattern không phải ba thế giới khác nhau

## 2.1 Class Diagram là mô hình, OOP là cơ chế runtime

Class Diagram — 클래스 다이어그램 — mô tả class, attribute, operation và relationship. Encapsulation, inheritance, polymorphism là các cơ chế mà implementation có thể dùng để hiện thực mô hình đó.

Một mũi tên generalization trong UML không tự động nói code sẽ “tốt”. Nếu hierarchy vi phạm Liskov Substitution Principle — LSP — 리스코프 치환 원칙, mô hình vẫn vẽ được nhưng thiết kế yếu.

## 2.2 Pattern là lời giải cho force lặp lại

Pattern không phải keyword để ghép tên. Hãy nối pattern với loại variation mà hệ thống cần hấp thụ.

Strategy — 전략 패턴 — variation của algorithm.  
State — 상태 패턴 — variation của behavior theo internal state.  
Observer — 옵저버 패턴 — one-to-many notification khi state thay đổi.  
Adapter — 어댑터 패턴 — interface không tương thích.  
Facade — 퍼사드 패턴 — subsystem phức tạp cần mặt tiền đơn giản.  
Decorator — 데코레이터 패턴 — thêm behavior động quanh object mà không đổi class gốc.

### Câu hỏi suy luận

Nếu hai class “nhìn giống nhau” trong UML nhưng một class được chọn dựa trên business policy còn một class được chọn vì object đang ở trạng thái `PAID/SHIPPED/CANCELLED`, hai trường hợp có thể dùng Strategy và State khác nhau dù sơ đồ class có cấu trúc gần giống.

---

# 3. Interface Design ↔ Integration ↔ Network

## 3.1 API contract không dừng ở JSON

인터페이스 설계 — interface design — xác định dữ liệu, protocol, error handling, sequence và contract giữa hai thành phần. Khi triển khai, contract đó đi qua network thật.

Ví dụ API:

```http
POST /payments
Idempotency-Key: abc-123
Content-Type: application/json
```

JSON schema thuộc contract. HTTP method/status thuộc application protocol. TCP chịu trách nhiệm reliable byte stream. IP chịu trách nhiệm packet forwarding. Ethernet/Wi-Fi xử lý local link.

Đây là lý do OSI/TCP-IP ở Môn 4 liên quan trực tiếp interface implementation ở Môn 1–2.

## 3.2 Timeout, retry và duplicate side effect

Nếu client timeout sau khi server đã charge card nhưng trước khi response quay lại, client có thể retry. Nếu endpoint không idempotent, cùng một business operation có thể chạy hai lần.

Vì vậy:

```text
Network uncertainty
    ↓
Retry
    ↓
Duplicate request risk
    ↓
Idempotency design
    ↓
DB uniqueness / transaction
```

Một câu hỏi về “중복 처리 방지 — duplicate processing prevention” có thể đòi suy nghĩ đồng thời về interface, server logic và database constraint.

## 3.3 EAI/ESB và coupling

Point-to-point integration tăng nhanh số connection khi số system tăng. EAI/ESB cố gắng tập trung hoặc chuẩn hóa mediation, routing và transformation.

Nhưng thêm middleware không tự động tạo low coupling. Nếu mọi consumer phụ thuộc chặt vào một schema duy nhất và thay schema gây vỡ toàn bộ, logical coupling vẫn cao.

---

# 4. Logical Data Model ↔ Physical DB ↔ SQL ↔ Transaction

## 4.1 Normalization giải quyết anomaly, không giải quyết mọi performance problem

정규화 — normalization — dùng functional dependency để giảm redundancy và update anomaly. 물리 설계 — physical design — chọn index, partition, storage, denormalization có kiểm soát để đáp ứng workload.

Do đó:

```text
Logical correctness ≠ Physical performance
```

Một schema có thể ở 3NF/BCNF nhưng query chậm vì thiếu index hoặc access pattern không phù hợp. Một schema denormalized có thể nhanh hơn cho read nhưng tăng consistency burden.

## 4.2 Index nối SQL với Data Structure

B+Tree index hoạt động tốt với equality và range vì key có thứ tự. Hash index tự nhiên cho equality lookup nhưng không hỗ trợ range theo ordering như B+Tree.

Đây là connection giữa:

- 자료구조 — data structure ở Môn 2;
- 물리 데이터베이스 설계 — physical DB ở Môn 3;
- query performance trong system management.

## 4.3 Transaction nối business invariant với concurrency

ACID không phải bốn từ riêng lẻ. Nó bảo vệ invariant khi nhiều operation cùng diễn ra hoặc hệ thống crash.

Ví dụ chuyển 100 từ A sang B:

```text
A = A - 100
B = B + 100
```

Atomicity bảo đảm không chỉ một nửa được commit. Consistency nói transaction hợp lệ phải đưa DB từ trạng thái thỏa invariant sang trạng thái thỏa invariant. Isolation kiểm soát interference giữa concurrent transaction. Durability bảo đảm committed result sống qua crash theo cơ chế persistence/recovery.

Locking, MVCC, log, checkpoint và recovery là implementation mechanisms hỗ trợ các property đó.

---

# 5. Algorithm/Data Structure ↔ Performance

## 5.1 Big-O không bằng thời gian chạy thực tế

복잡도 — complexity — mô tả tốc độ tăng resource theo input size. Nó không nói chính xác một request mất bao nhiêu millisecond.

Hai algorithm đều O(n log n) có thể khác constant factor, memory locality và behavior trên input cụ thể.

### Connection

```text
Algorithmic complexity
+ data structure
+ input distribution
+ I/O
+ cache/memory
+ concurrency
= observed performance
```

Nếu đề cho một vấn đề lookup nhiều lần, chọn data structure đúng thường quan trọng hơn micro-optimization syntax.

## 5.2 Queue xuất hiện ở nhiều môn

Queue — 큐 — FIFO structure ở Môn 2. Nhưng cùng abstraction xuất hiện trong:

- process scheduling;
- message queue;
- network buffer;
- job queue;
- producer/consumer.

Cần phân biệt abstraction “queue” với policy cụ thể. Round Robin dùng ready queue nhưng scheduling policy không đơn giản bằng “FIFO thuần”.

---

# 6. Server Program ↔ Process/Thread ↔ Synchronization

## 6.1 Request concurrency cuối cùng trở thành shared-state problem

Server nhận nhiều request cùng lúc. Tùy architecture, request có thể được xử lý bởi process, thread, event loop hoặc worker pool.

Nếu hai execution unit cùng cập nhật shared state mà không có synchronization phù hợp, race condition — 경쟁 상태 — có thể xuất hiện.

Ví dụ:

```text
stock = 1
T1 reads stock = 1
T2 reads stock = 1
T1 writes stock = 0
T2 writes stock = 0
```

Hai order đều nghĩ đã mua thành công dù chỉ có một item.

Ở application layer, có thể dùng lock. Ở database layer, có thể dùng transaction/row lock/optimistic concurrency. Chọn layer phụ thuộc invariant và system boundary.

## 6.2 Mutex, Semaphore và DB Lock có họ hàng nhưng không đồng nhất

Mutex — 상호배제 — thường biểu diễn ownership của critical section. Semaphore — 세마포어 — counter cho phép một số lượng permit. Database lock bảo vệ data item/range theo transaction semantics.

Không nên suy rằng “đều là lock nên giống nhau”. Chúng giải quyết concurrency ở các abstraction level khác nhau.

---

# 7. Virtual Memory ↔ Application Behavior

Page fault — 페이지 폴트 — xảy ra khi referenced page chưa ở physical memory. Page replacement policy quyết định page nào bị thay khi cần frame.

Application có poor locality có thể gây nhiều page fault. Vì vậy locality không chỉ là khái niệm OS; layout data và access pattern ở code ảnh hưởng behavior của memory hierarchy.

Working set quá lớn so với available memory có thể dẫn tới thrashing — 스래싱 — hệ thống tốn phần lớn thời gian paging thay vì làm công việc hữu ích.

---

# 8. DB Concurrency ↔ OS Concurrency: giống câu hỏi, khác đơn vị bảo vệ

Cả OS synchronization và DB transaction đều hỏi:

> “Hai hoạt động cùng lúc có thể làm state trở nên sai không?”

Nhưng unit khác nhau.

OS có process/thread, memory, critical section.  
DB có transaction, row/page/range, isolation level.

Deadlock có thể tồn tại ở cả hai: mỗi bên giữ resource mà bên kia cần. Cách phát hiện/giải quyết có thể dùng wait-for graph, timeout, prevention hoặc victim selection, nhưng semantics cụ thể khác nhau.

---

# 9. Network ↔ Security

## 9.1 Security control nằm trên nhiều layer

Firewall — 방화벽 — kiểm soát traffic theo rule. IDS phát hiện suspicious activity. IPS có thể block inline. TLS cung cấp cryptographic protection cho transport/application communication. VPN tạo protected tunnel. WAF tập trung HTTP/web application traffic.

Không hỏi “công cụ nào mạnh nhất”; hỏi **threat ở layer nào và control quan sát được gì**.

Ví dụ SQL Injection không được giải quyết tận gốc bằng firewall L3/L4. Secure coding với parameterized query xử lý nguyên nhân tại application/DB boundary; WAF có thể là additional defense.

## 9.2 Authentication, Authorization, Encryption

인증 — authentication — xác minh ai.  
인가/권한부여 — authorization — người đó được làm gì.  
암호화 — encryption — bảo vệ confidentiality của data.

TLS có thể bảo vệ channel nhưng không tự quyết định user có quyền xóa record hay không.

---

# 10. Availability ↔ Redundancy ↔ Disaster Recovery

Availability — 가용성 — khả năng service sẵn sàng khi cần. Redundancy — 이중화/중복성 — thêm component/path dự phòng để giảm single point of failure. Backup — 백업 — bản sao data để phục hồi. Disaster Recovery — 재해복구 — capability khôi phục service/data sau sự cố lớn.

RTO — Recovery Time Objective — thời gian gián đoạn tối đa mục tiêu.  
RPO — Recovery Point Objective — mức mất dữ liệu tính theo thời gian mà tổ chức chấp nhận.

Một RAID array không thay thế backup. Một backup mỗi ngày không tự đảm bảo RPO 5 phút. Multi-AZ redundancy không tự động thay thế disaster recovery nếu cùng loại failure domain vẫn có thể phá hủy toàn hệ thống.

---

# 11. Secure SDLC nối Môn 1, 2 và 5

Security không chỉ nằm ở cuối project.

```text
Requirements: xác định security requirement
Design: threat modeling, trust boundary, least privilege
Implementation: secure coding
Testing: SAST/DAST, penetration testing, abuse cases
Deployment: secrets/config/network hardening
Operation: logging, monitoring, patching, incident response
```

Nếu chỉ “scan sau khi code xong”, nhiều flaw kiến trúc không thể sửa rẻ như khi phát hiện ở design stage.

### Example

Requirement: chỉ owner được xem invoice.  
Design: object-level authorization check.  
Implementation: server lấy owner từ authenticated identity, không tin `userId` do client tự gửi.  
Test: thử IDOR/BOLA bằng cách đổi invoice ID.  
Operation: audit access bất thường.

---

# 12. Project Management ↔ Configuration ↔ Change

Một change request không chỉ đổi code. Nó có thể đổi requirement, schema, API, test, deployment package, manual và operational procedure.

Configuration Management — 형상관리 — quản lý version/baseline/change của configuration items. Version Control là một phần quan trọng nhưng không đồng nghĩa toàn bộ configuration management.

### Chain

```text
Change request
→ impact analysis
→ approval/prioritization
→ requirement/design update
→ code + DB/API change
→ test update
→ version/baseline
→ release/deploy
→ monitoring/rollback plan
```

Nếu một câu hỏi hỏi “code đúng nhưng production dùng nhầm artifact”, đây có thể là release/configuration management problem, không phải coding algorithm problem.

---

# 13. Tám scenario liên môn

## Scenario 1 — Duplicate Payment

### Tình huống

Mobile app gọi payment API. Server charge thành công nhưng response bị mất do network interruption. App retry và user bị charge hai lần.

### Phân tích

Network không thể bảo đảm client luôn biết request trước đã hoàn thành. Vì vậy interface cần idempotency semantics. Server có thể lưu `Idempotency-Key` với result trong transaction hoặc enforce unique constraint theo business operation.

### Kiến thức nối

인터페이스 설계 → TCP/network uncertainty → server implementation → transaction/unique constraint → testing retry scenario.

### Tự trả lời

1. Tại sao “TCP reliable” vẫn không loại bỏ duplicate business operation?
2. Idempotency khác transaction atomicity ở đâu?
3. Nếu key được lưu ngoài transaction charge thì race nào vẫn có thể xảy ra?

---

## Scenario 2 — Overselling Stock

Hai request cùng mua item cuối cùng.

Application check `stock > 0`, sau đó update. Nếu check và update không nằm trong concurrency-control boundary phù hợp, lost update hoặc overselling có thể xảy ra.

Các phương án có thể gồm pessimistic lock, atomic conditional update, serializable transaction, optimistic version check. Không có một answer duy nhất cho mọi architecture; đề thường cho constraint để chọn.

### Tự trả lời

- `SELECT stock` rồi `UPDATE stock = stock - 1` tách rời có race gì?
- Atomic SQL `UPDATE ... WHERE stock > 0` thay đổi critical section như thế nào?
- Mutex trong một server instance có đủ khi chạy 10 instances không?

---

## Scenario 3 — Slow Search API

Table có 30 triệu row. Query:

```sql
SELECT id, created_at, total
FROM orders
WHERE customer_id = ?
  AND created_at >= ?
ORDER BY created_at DESC
LIMIT 20;
```

Đây không chỉ là SQL syntax. Cần xét index key order, selectivity, B+Tree range scan, sort avoidance, cardinality và access pattern.

Composite index `(customer_id, created_at)` có thể phù hợp vì equality trên customer rồi range/order trên created time. Nhưng quyết định cuối cùng phụ thuộc DBMS và workload.

### Tự trả lời

- Tại sao hash index không tự nhiên cho phần range/order?
- Normalization có giải quyết query chậm này không?
- Vì sao index quá nhiều lại làm write đắt hơn?

---

## Scenario 4 — Login Service bị tấn công brute force

Requirement cần rate limit/lockout. Design phải tránh cho attacker khóa account người khác quá dễ. Implementation cần secure password hashing, constant-time comparison ở chỗ phù hợp, session/token handling. Network cần TLS. Monitoring cần phát hiện pattern bất thường.

### Tự trả lời

- Authentication khác authorization ở đâu trong scenario này?
- TLS giải quyết phần nào và không giải quyết phần nào?
- Account lockout có thể tạo denial-of-service vector như thế nào?

---

## Scenario 5 — Batch Job ăn hết memory

Job đọc toàn bộ file 10 GB vào list trước khi process. Heap tăng, GC/paging tăng và host có thể thrash.

Giải pháp kiến trúc có thể là streaming/chunking. Đây là connection giữa algorithm/data structure, memory management và application performance.

### Tự trả lời

- Big-O space của cách load toàn bộ là gì theo input size?
- Streaming thay đổi peak memory ra sao?
- Page replacement policy có cứu được một working set vượt xa RAM không?

---

## Scenario 6 — API contract thay đổi làm nhiều hệ thống lỗi

Provider rename field `customerId` thành `userId`. Nhiều consumer fail.

Đây là interface compatibility, versioning và coupling problem. Integration architecture có thể giảm direct dependency, nhưng schema evolution vẫn cần compatibility strategy, consumer testing và change management.

### Tự trả lời

- Adapter có thể dùng ở đâu?
- Version control có đủ để ngăn breaking change production không?
- Contract test nối requirement/interface với test như thế nào?

---

## Scenario 7 — Database primary chết

Nếu hệ thống có replica nhưng failover mất 20 phút, availability có thể vẫn không đạt SLO. Nếu replica async lag 30 giây, failover có thể mất recent data.

RTO liên quan thời gian phục hồi. RPO liên quan mức data loss. Redundancy, replication, backup và DR phải được thiết kế theo objective, không phải chỉ “có nhiều server”.

### Tự trả lời

- Async replication ảnh hưởng RPO thế nào?
- Backup hàng đêm có thể đáp ứng RPO 5 phút không?
- RAID bảo vệ loại failure nào và không bảo vệ loại nào?

---

## Scenario 8 — Deadlock trong order processing

Transaction T1 lock `order` rồi `inventory`; T2 lock `inventory` rồi `order`. Hai bên chờ nhau.

Đây là circular wait. Có thể giảm bằng consistent lock ordering, timeout/deadlock detection hoặc transaction redesign.

### Tự trả lời

- Vì sao “lock nhiều hơn” không đồng nghĩa an toàn hơn?
- Deadlock khác starvation ở đâu?
- Consistent resource ordering phá điều kiện nào của deadlock?

---

# 14. Connection matrix để tự kiểm tra

| Nếu gặp khái niệm này | Hãy nối ngay sang |
|---|---|
| 요구사항 / Requirement | acceptance criteria, test, traceability, change management |
| UML / Architecture | OOP, patterns, module coupling, interface contract |
| Interface/API | protocol, timeout/retry, idempotency, security, integration |
| Data structure | algorithm complexity, index, scheduler/buffer usage |
| Normalization | dependency, anomaly, physical design, query workload |
| SQL | index, transaction, locking, authorization |
| Process/Thread | scheduling, synchronization, server concurrency |
| Virtual memory | locality, page fault, application memory behavior |
| Network | interface transport, routing, firewall, TLS, availability |
| Security | requirement, design, code, test, operation |
| RAID/Replication | availability, failure domain, RTO/RPO, backup |
| SCM/Configuration | change, build artifact, release, rollback |

---

# 15. Closed-book integration drill

Không nhìn tài liệu, hãy giải thích liên tục một request `POST /orders` từ lúc requirement được viết đến lúc production phục hồi sau failure. Câu trả lời đạt yêu cầu khi tự nối được ít nhất các điểm sau mà không biến thành danh sách từ khóa rời rạc:

1. functional/non-functional requirement;
2. UML/component/interface design;
3. module responsibility và coupling;
4. validation/input handling;
5. server process/thread execution;
6. algorithm/data structure chính;
7. SQL và index;
8. transaction/isolation/concurrency;
9. TCP/IP và network path;
10. authentication/authorization/TLS;
11. logging/monitoring;
12. deployment/configuration/version;
13. redundancy/backup;
14. RTO/RPO và recovery.

Nếu bị đứng ở bất kỳ transition nào, quay lại deep-dive của hai môn nằm hai bên transition đó. Đây là dấu hiệu của **connection gap**, khác với việc hoàn toàn chưa biết một concept.

---

# 16. Definition of Done

File này chỉ hoàn thành khi bạn có thể làm ba việc.

**End-to-end reasoning:** nhìn một scenario và theo request/data xuyên qua design → code → DB → OS/network → operation/security.

**Boundary reasoning:** biết cùng một vấn đề như concurrency, availability hoặc validation được xử lý khác nhau ở các abstraction layer nào.

**Trade-off reasoning:** không trả lời bằng khẩu hiệu “càng nhiều index càng tốt”, “normalize luôn tốt”, “RAID là backup”, “TLS là đủ bảo mật”, mà chỉ ra benefit, cost và phạm vi bảo vệ.
