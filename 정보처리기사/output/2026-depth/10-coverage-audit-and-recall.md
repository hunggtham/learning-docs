# 정보처리기사 필기 2026 — Coverage Audit & Closed-Book Recall

> File này là lớp **audit cuối**. Nó không dạy lại toàn bộ lý thuyết; nó kiểm tra xem 21 vùng kiến thức lớn đã thật sự được hiểu hay mới chỉ “đã đọc”. Mỗi mục có ba tiêu chuẩn: **Explain**, **Distinguish**, **Solve**.

---

## Cách chấm

Mỗi chapter tự đánh dấu:

```text
E = Explain: giải thích được bản chất không nhìn tài liệu
D = Distinguish: phân biệt được các khái niệm gần nhau
S = Solve: làm được scenario/code/SQL/tính liên quan
```

Chỉ khi `E+D+S` đều đạt mới coi chapter là closed-book ready.

---

# Môn 1 — 소프트웨어 설계

## 1. 요구사항 확인 — Requirements Confirmation

### Explain

Giải thích được vì sao requirement engineering không phải chỉ “ghi lại yêu cầu”, mà gồm elicitation, analysis, specification và validation. Giải thích được functional requirement, non-functional requirement, feasibility và traceability.

### Distinguish

Phải phân biệt được:

- functional vs non-functional;
- verification vs validation;
- DFD vs flowchart;
- Data Dictionary vs Mini-specification;
- stakeholder need vs implementation detail;
- structural UML vs behavioral UML.

### Solve

Không nhìn tài liệu, tự phân loại 10 requirement tự đặt; với mỗi requirement chỉ ra test/acceptance criterion phù hợp. Từ một scenario đơn giản, chọn đúng Use Case, Sequence, Activity hoặc State Diagram theo câu hỏi cần trả lời.

---

## 2. 화면 설계 — UI Design

### Explain

Giải thích wireframe, mockup, prototype, storyboard khác nhau về mục tiêu và fidelity. Giải thích usability không chỉ là “đẹp”, mà liên quan effectiveness, learnability, intuitiveness, consistency, feedback và accessibility tùy taxonomy.

### Distinguish

Phải phân biệt được:

- CLI / GUI / NUI;
- wireframe / mockup / prototype / storyboard;
- usability vs accessibility;
- visual design vs interaction flow.

### Solve

Cho một yêu cầu “cần test flow đăng ký trước khi code backend”, chọn artifact phù hợp và giải thích vì sao.

---

## 3. 애플리케이션 설계 — Application Design

### Explain

Giải thích module independence qua cohesion/coupling. Giải thích OOP, SOLID và design pattern như cơ chế quản lý variation/dependency, không phải danh sách từ khóa.

### Distinguish

Phải phân biệt được:

- Functional/Sequential/Communicational/Procedural/Temporal/Logical/Coincidental cohesion;
- Content/Common/External/Control/Stamp/Data coupling;
- overloading vs overriding;
- composition vs aggregation;
- Strategy vs State;
- Adapter vs Facade;
- Decorator vs Proxy;
- Factory Method vs Abstract Factory;
- inheritance vs delegation/composition.

### Solve

Nhìn một dependency graph module và chỉ ra fan-in/fan-out. Nhìn scenario và chọn pattern theo force. Nhìn code OOP và xác định polymorphism/encapsulation/vi phạm principle.

---

## 4. 인터페이스 설계 — Interface Design

### Explain

Giải thích interface contract gồm data, protocol, error semantics, sequence và compatibility. Giải thích point-to-point, EAI/ESB và lý do integration complexity tăng.

### Distinguish

Phải phân biệt được:

- synchronous vs asynchronous interaction;
- request validation vs business validation;
- transport failure vs application error;
- retry vs idempotency;
- data transformation vs routing.

### Solve

Thiết kế retry-safe cho một payment API; chỉ ra đâu cần idempotency key, transaction boundary và error mapping.

---

# Môn 2 — 소프트웨어 개발

## 5. 데이터 입출력 구현 — Data I/O Implementation

### Explain

Giải thích abstract data type, stack, queue, tree, graph, hash table và algorithm complexity. Giải thích tại sao data structure quyết định operation cost.

### Distinguish

Phải phân biệt được:

- stack vs queue;
- tree vs graph;
- BFS vs DFS;
- BST vs heap;
- linear search vs binary search;
- collision resolution strategies;
- time complexity vs actual elapsed time.

### Solve

Trace postfix expression, BFS/DFS, binary search, hash insertion và ít nhất một sorting process.

---

## 6. 통합 구현 — Integration Implementation

### Explain

Giải thích data/interface integration từ mapping, transformation, validation tới error handling. Hiểu rằng integration problem có schema, protocol và operational dimensions.

### Distinguish

Phân biệt:

- schema mismatch vs transport failure;
- batch integration vs real-time integration;
- adapter/connector vs business logic;
- data mapping vs data cleansing.

### Solve

Cho hai schema khác nhau, tự viết mapping rule và validation rule; chỉ ra cách xử lý missing/invalid field.

---

## 7. 제품 소프트웨어 패키징 — Product Software Packaging

### Explain

Giải thích packaging, release artifact, dependency, manual, version và configuration item. Hiểu DRM/license và distribution integrity ở mức khái niệm.

### Distinguish

Phân biệt:

- version control vs configuration management;
- build artifact vs source;
- checksum/integrity vs authentication/authorization;
- backup artifact vs release artifact.

### Solve

Từ source tới deployable package, liệt kê metadata/dependency/config/manual cần quản lý và cách verify package không bị corrupt.

---

## 8. 애플리케이션 테스트 관리 — Application Test Management

### Explain

Giải thích test level, black-box, white-box, regression, integration và acceptance. Hiểu test oracle, coverage và defect lifecycle ở mức cơ chế.

### Distinguish

Phân biệt:

- unit/integration/system/acceptance;
- black-box/white-box;
- equivalence partition/boundary value;
- statement/branch/path coverage;
- stub/driver;
- verification/validation;
- alpha/beta;
- regression/retest.

### Solve

Tính Cyclomatic Complexity, chọn black-box cases ở boundary, thiết kế top-down/bottom-up integration setup.

---

## 9. 인터페이스 구현 — Interface Implementation

### Explain

Giải thích contract implementation, serialization, validation, error handling, logging và interoperability.

### Distinguish

Phân biệt:

- syntax/schema validation vs semantic/business validation;
- timeout vs application rejection;
- retryable vs non-retryable error;
- serialization error vs data integrity error.

### Solve

Cho API payload và error matrix, xác định nơi validate và response category phù hợp.

---

# Môn 3 — 데이터베이스 구축

## 10. 논리 데이터베이스 설계 — Logical Database Design

### Explain

Giải thích relational model, key, functional dependency, normalization và integrity constraints.

### Distinguish

Phân biệt:

- super key / candidate key / primary key / alternate key / foreign key;
- selection / projection / join / division;
- partial / transitive dependency;
- 1NF / 2NF / 3NF / BCNF;
- entity integrity / referential integrity / domain integrity.

### Solve

Tính attribute closure, tìm candidate key, normalize một relation tới ít nhất 3NF/BCNF khi phù hợp và kiểm lossless reasoning cơ bản.

---

## 11. 물리 데이터베이스 설계 — Physical Database Design

### Explain

Giải thích index, storage, partition, clustering/organization và denormalization như physical decisions dựa trên workload.

### Distinguish

Phân biệt:

- logical schema vs physical design;
- B+Tree vs Hash cho equality/range;
- normalization vs denormalization;
- selectivity vs cardinality;
- clustered concept vs secondary index theo DBMS-specific implementation.

### Solve

Nhìn query pattern và đề xuất index key order có lý do; giải thích write cost và cases index không được dùng hiệu quả.

---

## 12. SQL 활용 — SQL Utilization

### Explain

Giải thích logical query processing: FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY như mental model.

### Distinguish

Phân biệt:

- WHERE vs HAVING;
- INNER vs LEFT/RIGHT/FULL OUTER JOIN;
- `COUNT(*)` vs `COUNT(column)`;
- subquery vs join theo semantics;
- NULL vs empty string/value 0;
- UNION vs UNION ALL.

### Solve

Tự viết query có join + aggregate + HAVING; dự đoán result khi có NULL và unmatched rows.

---

## 13. SQL 응용 — SQL Application

### Explain

Giải thích transaction, ACID, concurrency anomaly, locking/isolation và recovery.

### Distinguish

Phân biệt:

- dirty read / non-repeatable read / phantom;
- shared/exclusive lock concept;
- deadlock vs starvation;
- serial schedule vs serializable schedule;
- undo vs redo;
- checkpoint vs backup.

### Solve

Vẽ precedence graph cho schedule; xác định conflict-serializability; nhận diện anomaly từ timeline; reasoning lock ordering/deadlock.

---

## 14. 데이터 전환 — Data Migration/Conversion

### Explain

Giải thích extract, transform, load/migrate, validation, reconciliation và cutover. Hiểu migration là correctness + operational transition problem.

### Distinguish

Phân biệt:

- schema mapping vs data cleansing;
- migration vs replication;
- validation vs reconciliation;
- full cutover vs staged/parallel strategy.

### Solve

Thiết kế checklist migration có row counts, constraints, sampled/business reconciliation, rollback/cutover criteria.

---

# Môn 4 — 프로그래밍 언어 활용

## 15. 서버 프로그램 구현 — Server Program Implementation

### Explain

Giải thích request lifecycle, process/thread, shared state, synchronization và server concurrency.

### Distinguish

Phân biệt:

- process vs thread;
- concurrency vs parallelism;
- race condition vs deadlock;
- mutex vs semaphore;
- blocking vs non-blocking ở mức khái niệm.

### Solve

Nhìn code increment shared counter và chỉ ra race; chọn synchronization boundary hợp lý trong single-process và multi-instance system.

---

## 16. 프로그래밍 언어 활용 — Programming Language Application

### Explain

Hiểu evaluation/state change trong C, Java, Python thay vì học output pattern máy móc.

### Distinguish

Phân biệt:

- C pointer vs pointed value;
- pre-increment vs post-increment;
- Java overloading vs overriding;
- reference type vs runtime object;
- Python mutable vs immutable object;
- alias vs copy.

### Solve

Trace code C pointer/array, Java dynamic dispatch và Python alias/mutation từng line bằng bảng variable state.

---

## 17. 응용 SW 기초 기술 활용 — OS / Network / Basic Infrastructure

### Explain

Giải thích CPU scheduling, deadlock, virtual memory, page replacement, TCP/IP, subnetting và routing.

### Distinguish

Phân biệt:

- FCFS / SJF / Round Robin;
- waiting / turnaround / response time;
- FIFO / LRU page replacement;
- page fault vs thrashing;
- TCP vs UDP;
- IP address / subnet / gateway / DNS;
- network prefix vs host bits;
- shortest path concept vs longest-prefix routing match.

### Solve

Tính scheduling timeline, page faults, subnet network/broadcast/usable range và longest-prefix route.

---

# Môn 5 — 정보시스템 구축 관리

## 18. 소프트웨어 개발 방법론 활용 — Software Development Methodology

### Explain

Giải thích lifecycle/methodology, estimation, schedule/risk/change. Hiểu rằng Agile/Waterfall là cách tổ chức feedback/change khác nhau chứ không phải “mới vs cũ” đơn giản.

### Distinguish

Phân biệt:

- Waterfall vs iterative/agile;
- project activity duration vs path duration;
- critical path vs non-critical path;
- estimate vs commitment;
- risk vs issue.

### Solve

Tính PERT expected time, critical path đơn giản và impact khi activity critical delay.

---

## 19. IT 프로젝트 정보시스템 구축관리 — IT Project / Infrastructure Construction Management

### Explain

Giải thích compute/storage/network/database/cloud infrastructure, redundancy, capacity và failure domain.

### Distinguish

Phân biệt:

- RAID 0/1/5/6;
- redundancy vs backup;
- replication vs backup;
- vertical vs horizontal scaling;
- IaaS/PaaS/SaaS;
- VM vs container;
- high availability vs disaster recovery;
- RTO vs RPO.

### Solve

Tính RAID usable capacity, chọn architecture theo RTO/RPO scenario và chỉ ra single point of failure.

---

## 20. 소프트웨어 개발 보안 구축 — Software Development Security

### Explain

Giải thích secure SDLC, input handling, authentication, authorization, secrets và common application vulnerabilities.

### Distinguish

Phân biệt:

- authentication vs authorization;
- SQL Injection vs XSS;
- parameterized query vs escaping;
- hashing vs encryption;
- symmetric vs asymmetric encryption;
- confidentiality/integrity/authenticity;
- threat/vulnerability/risk/control.

### Solve

Cho attack scenario, chọn root-cause mitigation và defense-in-depth controls; giải thích vì sao control ở sai layer không xử lý nguyên nhân.

---

## 21. 시스템 보안 구축 — System Security Construction

### Explain

Giải thích network/system security controls, firewall, IDS/IPS, VPN/TLS, access control, logging/monitoring, patching và incident/recovery.

### Distinguish

Phân biệt:

- firewall vs WAF;
- IDS vs IPS;
- TLS vs VPN;
- detection vs prevention;
- preventive/detective/corrective control;
- availability mechanism vs security monitoring.

### Solve

Với một architecture có Internet → LB → Web → App → DB, đặt trust boundary và đề xuất controls theo layer mà không biến thành “gắn firewall ở mọi nơi”.

---

# Cross-Chapter Recall — 30 câu không nhìn tài liệu

1. Requirement “response < 1s” sẽ nối sang test type và operational metric nào?  
2. Vì sao Sequence Diagram và Activity Diagram có thể cùng mô tả một nghiệp vụ nhưng trả lời câu hỏi khác nhau?  
3. Stamp Coupling khác Data Coupling ở boundary nào?  
4. Strategy khác State ở nguồn quyết định behavior nào?  
5. Retry vì timeout có thể tạo duplicate business side effect thế nào?  
6. Tại sao BFS tìm shortest path unweighted nhưng DFS không bảo đảm?  
7. Vì sao Binary Search cần ordering?  
8. Linear Probing tạo primary clustering bằng cơ chế nào?  
9. Branch Coverage khác Boundary Value Analysis ở góc nhìn internal/external thế nào?  
10. Vì sao checksum không thay thế digital signature/authentication?  
11. Tại sao candidate key phải minimal?  
12. Tại sao 2NF chủ yếu trở nên đáng chú ý khi candidate key composite?  
13. B+Tree hỗ trợ range tốt hơn hash bằng cơ chế nào?  
14. `WHERE` và `HAVING` xảy ra ở logical phase nào?  
15. `COUNT(*)` và `COUNT(col)` khác nhau khi NULL thế nào?  
16. Non-repeatable read khác phantom read ở unit thay đổi nào?  
17. Cycle trong precedence graph chứng minh điều gì?  
18. Race condition ở application khác lost update ở DB thế nào và giống nhau ở bản chất nào?  
19. Quantum quá nhỏ trong Round Robin có cost gì?  
20. FIFO và LRU chọn victim theo information nào?  
21. `/27` để lại bao nhiêu host bit?  
22. Longest-prefix match vì sao chọn route cụ thể nhất?  
23. Java overriding khác overloading về dispatch thế nào?  
24. Python alias của mutable list gây effect gì?  
25. Critical path quyết định project duration trong model thế nào?  
26. RAID5 và backup bảo vệ các failure mode khác nhau ra sao?  
27. RTO và RPO trả lời hai câu hỏi khác nhau nào?  
28. TLS bảo vệ channel nhưng không thay authorization ra sao?  
29. SQL Injection và XSS có root cause/mitigation khác nhau thế nào?  
30. Configuration Management rộng hơn Git Version Control ở đâu?

---

# 과락 방지 — Fail-Safe Audit

Vì mỗi môn có ngưỡng riêng, không được coi tổng điểm cao ở một môn có thể “bù” hoàn toàn cho môn yếu. Trước khi làm mock cuối, mỗi môn cần có tối thiểu:

```text
Môn 1: E+D+S cho 4/4 chapter
Môn 2: E+D+S cho 5/5 chapter
Môn 3: E+D+S cho 5/5 chapter
Môn 4: E+D+S cho 3/3 chapter
Môn 5: E+D+S cho 4/4 chapter
```

Nếu một chapter thiếu `S`, ưu tiên Procedural Workbook. Nếu thiếu `D`, quay lại confusion pairs trong deep-dive. Nếu thiếu `E`, quay lại explanation gốc trong Master Guide/deep-dive và tự nói lại bằng lời của mình.

---

# Definition of Done

Bạn có thể coi toàn bộ track 2026 đạt coverage khi:

- 21 chapter đều có E+D+S;
- 30 cross-chapter recall questions trả lời được mà không mở tài liệu;
- Procedural Workbook không còn dạng bài “biết lý thuyết nhưng không làm được”;
- Full Mock không có môn dưới 8/20;
- mọi câu sai được truy ngược về một concept/procedure cụ thể và sửa ở file nguồn, không chỉ học đáp án.
