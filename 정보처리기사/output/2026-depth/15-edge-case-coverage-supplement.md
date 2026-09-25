# 정보처리기사 필기 2026 — Edge-Case Coverage Supplement

> File này dùng để bù các vùng kiến thức có **độ salience thấp**: dễ bị bỏ qua vì không nổi bật như UML, SQL hay subnetting, nhưng vẫn nằm trong các chapter đã xác nhận của 필기. Mục tiêu không phải học thêm ngoài phạm vi, mà làm cho coverage trong 21 chapter bớt phụ thuộc vào vài chủ đề quen thuộc.
>
> Cách dùng: chỉ đọc file này sau Master Guide và 5 Deep-Dive. Với mỗi mục, phải trả lời được ba câu: **Nó dùng để làm gì? Nó khác cái gần nhất ở đâu? Một câu hỏi có thể đổi wording thế nào?**

---

# Môn 1 — 소프트웨어 설계

## 1. Requirement feasibility không đồng nghĩa với requirement validity

Một requirement có thể phản ánh đúng mong muốn stakeholder nhưng vẫn không khả thi về kỹ thuật, ngân sách hoặc thời gian. Ngược lại, một chức năng hoàn toàn khả thi kỹ thuật vẫn có thể không giải quyết nhu cầu thực.

Hãy tách bốn câu hỏi:

- **Need:** stakeholder có thực sự cần không?
- **Feasibility:** có thể xây trong constraint không?
- **Priority:** có đáng làm trước không?
- **Verifiability:** có thể kiểm chứng rõ ràng không?

Nếu requirement nói “hệ thống phải rất nhanh”, vấn đề đầu tiên là **không verifiable** vì thiếu threshold. Nếu nói “mọi request phải trả trong 1 microsecond trên mobile network”, nó measurable nhưng có thể **không feasible**.

## 2. Requirement ambiguity vs incompleteness vs inconsistency

**Ambiguity — 모호성:** một câu có nhiều cách hiểu.  
**Incompleteness — 불완전성:** thiếu trường hợp hoặc thông tin cần thiết.  
**Inconsistency — 불일치성:** hai requirement mâu thuẫn nhau.

Ví dụ:

```text
R1: 비밀번호는 최소 8자이다.
R2: 비밀번호는 정확히 6자여야 한다.
```

Đây là inconsistency, không phải ambiguity.

## 3. DFD balancing

Khi phân rã một process từ level cao xuống level thấp, input/output data flow bên ngoài của process phải được bảo toàn về mặt logic. Đây là **balancing**.

Nếu context diagram có input `Order` và output `Receipt`, nhưng level con bỗng tạo thêm external output `CreditScore` chưa xuất hiện ở boundary level trên, cần kiểm tra consistency của decomposition.

## 4. Data Dictionary và Mini-specification

Data Dictionary định nghĩa **data element/data structure**. Mini-specification định nghĩa **logic xử lý** của process thấp.

Nếu đề mô tả “định nghĩa cấu trúc của CUSTOMER = ID + NAME + ...” → Data Dictionary.  
Nếu đề mô tả “nếu amount > 1,000 thì manager approval” → Mini-spec/decision logic.

## 5. Decision Table vs Decision Tree

Decision Table hữu ích khi có nhiều condition/action combinations cần kiểm tra coverage có hệ thống. Decision Tree trực quan hóa sequence/branch decision.

Đừng chọn theo hình thức “table dễ nhìn hơn”. Hỏi: có cần **liệt kê tổ hợp condition** và action tương ứng không?

## 6. UML relationship: realization

Realization — 실체화 — thường dùng khi class/component hiện thực interface/specification.

Generalization là subtype/inheritance relation. Realization gần “implements contract” hơn “is-a class hierarchy” thuần túy.

## 7. Include vs Extend trong Use Case

`<<include>>` thể hiện behavior chung được use case gốc **luôn gọi như phần bắt buộc** trong flow được mô hình hóa.  
`<<extend>>` thêm behavior **tùy điều kiện/extension point**.

Ví dụ `Checkout` include `Authenticate Payment`; `Apply Coupon` có thể extend flow khi user có coupon.

## 8. State vs Activity Diagram

State Diagram tập trung **một object thay đổi state theo event**. Activity Diagram tập trung **workflow/control flow** giữa action.

Một order đi `CREATED → PAID → SHIPPED → DELIVERED` → State.  
Một business process có fork/join giữa “verify stock” và “fraud check” → Activity.

## 9. Component vs Deployment Diagram

Component Diagram hỏi **software pieces và dependency**. Deployment Diagram hỏi **artifact/component chạy trên node nào**.

Nếu đề nói Web Server, App Server, DB Server như physical/runtime nodes → Deployment.

## 10. Architecture quality trade-off

Layering tăng separation nhưng có thể tăng latency/call overhead. Central repository đơn giản hóa sharing nhưng tạo central dependency. Client-server tập trung service nhưng server có thể thành bottleneck/failure concentration.

Không có architecture style “luôn tốt hơn”; đáp án đúng thường gắn với requirement cụ thể.

## 11. Cohesion nuance: sequential vs communicational

**Sequential cohesion:** output của một phần là input cho phần tiếp theo.  
**Communicational cohesion:** nhiều operation cùng dùng/chỉnh cùng data set.

Nếu module `read → parse → transform` theo pipeline → sequential. Nếu module có `create/read/update` cùng trên Customer record → communicational có thể gần hơn.

## 12. External coupling

External coupling xảy ra khi modules phụ thuộc vào external format/protocol/device interface chung.

Ví dụ hai module cùng phụ thuộc một file format hoặc communication protocol bên ngoài. Nó khác Common Coupling là **share global data**.

## 13. Fan-in không tự động đồng nghĩa tốt

Fan-in cao có thể cho thấy reuse tốt, nhưng một utility “god module” được mọi nơi gọi vì chứa quá nhiều responsibility vẫn có design smell.

Metric là signal, không phải verdict.

## 14. Interface error semantics

API/interface specification không chỉ có field. Cần xác định:

- validation error;
- authentication/authorization failure;
- business rejection;
- transient infrastructure error;
- timeout/retry behavior;
- duplicate request semantics.

Nếu tất cả lỗi đều trả một mã chung, consumer khó quyết định có retry được hay không.

## 15. Data format compatibility

Compatibility có thể phá vì:

- rename field;
- change type;
- change nullability;
- change enum value;
- change semantic nhưng giữ tên;
- change ordering/encoding assumptions.

Thay schema không chỉ là syntax issue; semantic compatibility quan trọng hơn.

---

# Môn 2 — 소프트웨어 개발

## 16. ADT vs implementation

Stack là **abstract data type** với push/pop/top semantics. Nó có thể được implement bằng array hoặc linked list.

Đừng đồng nhất ADT với structure implementation cụ thể.

## 17. Heap vs BST

Heap chỉ đảm bảo parent-child ordering phù hợp heap property; nó không duy trì full BST ordering giữa left/right subtree.

Max-heap root cho maximum nhanh. BST hỗ trợ ordered search/range tốt khi balanced phù hợp.

## 18. Complete binary tree

Complete Binary Tree điền node theo level từ trái sang phải, ngoại trừ level cuối có thể chưa đầy. Heap thường được lưu hiệu quả bằng array nhờ tính chất này.

## 19. AVL/Balanced tree reasoning

Balanced tree tồn tại để tránh height suy thoái thành O(n) như BST lệch. Không cần giả định mọi BST tự cân bằng.

Nếu insert key đã sorted vào naive BST, tree có thể thành chain.

## 20. Graph representations

Adjacency Matrix: memory O(V²), edge lookup nhanh.  
Adjacency List: memory O(V+E), phù hợp sparse graph.

Nếu graph cực sparse, matrix có thể lãng phí memory.

## 21. MST vs shortest path

Minimum Spanning Tree nối **tất cả vertices** với total edge weight nhỏ nhất, không cycle. Shortest Path tối ưu đường từ source tới target/all targets.

Prim/Kruskal ≠ Dijkstra.

## 22. Stable sorting

Stable sort bảo toàn relative order của records có key bằng nhau.

Nếu sort employee theo department sau khi đã stable-sort theo hire date, stability có thể có ý nghĩa cho multi-key ordering strategy.

## 23. In-place vs out-of-place

In-place algorithm dùng auxiliary memory nhỏ theo input size, còn out-of-place cần buffer đáng kể. Merge Sort array implementation điển hình cần auxiliary array; Heap Sort có thể in-place.

## 24. Collision ≠ duplicate key

Hash collision là **khác key nhưng cùng hash/index**. Duplicate key là cùng logical key xuất hiện lại.

Collision resolution không tự giải business duplicate semantics.

## 25. Open addressing deletion

Trong open addressing, xóa một slot bằng cách biến nó thành “never occupied” có thể phá probe chain. Thường cần tombstone/deleted marker hoặc rehash strategy.

Đây là ví dụ cho việc implementation detail ảnh hưởng correctness.

## 26. Static testing vs dynamic testing

Static testing không chạy program: review, inspection, static analysis. Dynamic testing chạy program với inputs.

Code review có thể tìm bug mà không cần execute.

## 27. Error, Defect/Fault, Failure

Human error có thể tạo defect/fault trong artifact. Khi defect được kích hoạt runtime, system có thể failure observable.

Ba tầng này không đồng nghĩa.

## 28. Test case vs test condition

Test Condition là aspect/scenario cần test. Test Case cụ thể hóa precondition, input, steps, expected result.

“Nên test password boundary” là condition; “7-char → reject, 8-char → accept” là concrete cases.

## 29. Equivalence Partition không thay Boundary Value

Equivalence Partition chia input thành classes được kỳ vọng behave giống nhau. Boundary Value tập trung cạnh của ranges vì lỗi thường nằm quanh boundaries.

Hai technique bổ sung nhau.

## 30. Statement 100% không bảo đảm Branch 100%

Một `if` có thể execute statement trong true branch mà chưa từng exercise false outcome. Do đó statement coverage 100% vẫn có thể thiếu decision outcome.

## 31. Condition coverage vs branch coverage

Với compound condition `A && B`, branch coverage chỉ cần overall decision true/false. Condition coverage quan tâm từng atomic condition nhận true/false.

Không suy rằng một metric luôn subsume metric kia trong mọi form nếu không xét criterion formal.

## 32. Smoke vs regression

Smoke test là shallow check để biết build đủ ổn cho testing tiếp. Regression test kiểm behavior cũ sau change.

Một smoke suite có thể cũng chạy lại nhiều lần, nhưng intent khác regression.

## 33. Alpha vs beta nuance

Alpha thường diễn ra trong môi trường controlled của tổ chức phát triển. Beta đưa sản phẩm cho external/representative users trong context gần thực tế hơn.

## 34. Configuration item

Configuration Item không chỉ source code. Có thể gồm requirement document, build script, schema, config, test artifact, binary, manual.

## 35. Build vs release

Build biến source/dependency thành artifact. Release là decision/process đưa một phiên bản xác định tới environment/user.

Nhiều build không trở thành release.

## 36. DRM roles ở mức khái niệm

DRM liên quan quyền sử dụng nội dung số: license, key, usage policy, packaging/protection và enforcement. Đừng nhầm với source version control hoặc transport encryption đơn thuần.

## 37. Interface monitoring

Integration production cần quan sát latency, error rate, throughput, retry, timeout, queue backlog và schema/contract failure. Interface “đã implement” nhưng không observable rất khó vận hành.

## 38. Idempotency vs deduplication

Idempotency là property khi repeated same operation không làm thay đổi outcome sau lần đầu theo semantics. Deduplication là technique phát hiện/loại duplicate events/requests.

Deduplication có thể là một cách implement idempotency, nhưng hai từ không đồng nghĩa hoàn toàn.

---

# Môn 3 — 데이터베이스 구축

## 39. Domain và attribute

Domain là tập giá trị hợp lệ về type/constraint semantics. Attribute là named property trong relation.

`Age` là attribute; integers 0–150 có thể là conceptual domain.

## 40. Degree vs cardinality

Degree — 차수 — số attributes/columns.  
Cardinality — 카디널리티 — số tuples/rows trong relation theo relational terminology cơ bản.

Trong query optimization, cardinality còn được dùng cho row count/estimated row count; đừng nhầm với selectivity.

## 41. Natural key vs surrogate key

Natural key có business meaning; surrogate key được tạo để identify row. Surrogate key không loại bỏ nhu cầu unique constraint trên business candidate key nếu business vẫn yêu cầu uniqueness.

## 42. Composite key nuance

Composite key gồm nhiều attributes. Partial dependency mới trở thành vấn đề 2NF khi non-prime attribute phụ thuộc một **proper subset** của candidate key composite.

## 43. Prime attribute

Prime attribute là attribute thuộc ít nhất một candidate key. Non-prime không thuộc candidate key nào.

Formal 3NF condition dùng khái niệm prime attribute; không chỉ học “loại transitive dependency” như shortcut.

## 44. Trivial FD

FD `X → Y` là trivial nếu `Y ⊆ X`.

Ví dụ `{A,B} → A` luôn đúng theo relational dependency definition, không cung cấp information mới.

## 45. Lossless decomposition

Decomposition tốt cần tránh tạo spurious tuples khi join lại. Lossless join bảo đảm join các relation con khôi phục đúng relation gốc theo dependency assumptions.

Normalization không chỉ là “chia bảng nhỏ”.

## 46. Dependency preservation

Dependency-preserving decomposition cho phép enforce dependencies bằng cách kiểm từng relation con mà không cần join phức tạp.

BCNF decomposition có thể lossless nhưng không luôn preserve mọi dependency; đây là trade-off lý thuyết quan trọng.

## 47. View updatability

Không phải mọi view đều dễ update. Aggregation, GROUP BY, DISTINCT hoặc join phức tạp có thể làm update ambiguous/không được DBMS cho phép.

## 48. Clustered concept

Một storage organization/index có thể ảnh hưởng physical ordering/locality, nhưng exact semantics phụ thuộc DBMS. Trong thi lý thuyết, hiểu ý tưởng **data được tổ chức gần order của key** và một table không thể có nhiều physical order độc lập cùng lúc.

## 49. Covering index

Nếu index chứa đủ columns để trả query mà không cần lookup row/table thêm, query có thể được “covered”. Nhưng index rộng hơn tăng storage và write maintenance.

## 50. Selectivity

Selectivity cao thường nghĩa predicate giữ ít rows hơn tương đối, làm index có thể hữu ích hơn. Column boolean với 50/50 distribution thường selectivity thấp hơn unique ID.

## 51. Sargability

Predicate có form cho phép DB dùng index search hiệu quả được gọi sargable trong thực hành DB. Ví dụ function áp lên indexed column có thể làm optimizer khó dùng range seek tùy DBMS.

Concept này nối SQL syntax với physical access path.

## 52. NULL logic

SQL dùng three-valued logic: TRUE/FALSE/UNKNOWN. `col = NULL` không dùng để test nullness; dùng `IS NULL`.

`NOT IN` với NULL trong subquery có thể cho result bất ngờ do UNKNOWN; phải reasoning cẩn thận.

## 53. UNION vs UNION ALL

UNION loại duplicate, thường cần additional work. UNION ALL giữ tất cả rows.

Nếu business không cần deduplicate, UNION ALL thường tránh cost loại trùng.

## 54. Correlated subquery

Correlated subquery tham chiếu row từ outer query. Mental model là inner logic phụ thuộc current outer row, dù optimizer có thể transform execution.

## 55. Transaction savepoint

SAVEPOINT cho phép rollback một phần transaction tới marker, không nhất thiết rollback toàn transaction. Exact syntax/behavior DBMS-specific nhưng concept là partial rollback point.

## 56. Recoverability vs serializability

Serializability liên quan correctness của concurrent interleaving như serial order. Recoverability liên quan commit dependency và khả năng recovery khi transaction abort.

Một schedule có thể xét hai properties khác nhau.

## 57. Cascading rollback

Nếu T2 đọc uncommitted value từ T1 rồi T1 abort, T2 có thể phải rollback theo → cascading rollback.

Strict scheduling/appropriate isolation giúp tránh chain này.

## 58. Two-Phase Locking concept

2PL có growing phase acquire locks và shrinking phase release locks; sau khi bắt đầu release thì không acquire lock mới theo basic 2PL.

2PL hỗ trợ conflict serializability nhưng variants khác nhau ảnh hưởng recoverability/deadlock.

## 59. Deadlock graph

Wait-for graph node là transactions/processes, edge `Ti → Tj` nghĩa Ti đang chờ resource do Tj giữ. Cycle có thể chỉ ra deadlock trong single-instance lock model.

## 60. Checkpoint không phải backup

Checkpoint giảm lượng log/recovery work cần scan bằng cách ghi recovery state/coordination. Backup là copy data phục vụ restore.

## 61. Logical vs physical backup

Logical backup có thể xuất schema/data dưới dạng SQL/records; physical backup copy storage pages/files. Trade-off về portability, speed, restore granularity khác nhau.

## 62. Migration validation dimensions

Không chỉ row count. Cần xem:

- count;
- checksum/hash khi phù hợp;
- key uniqueness;
- referential integrity;
- aggregate reconciliation;
- business invariants;
- encoding/timezone/precision.

---

# Môn 4 — 프로그래밍 언어 활용

## 63. Compile-time vs runtime error

Syntax/type error có thể bị phát hiện compile-time tùy language. Null dereference, divide-by-zero, bounds error có thể runtime.

Không suy mọi bug đều compile error chỉ vì code “sai”.

## 64. Static vs dynamic typing

Static typing kiểm type relation chủ yếu trước runtime; dynamic typing gắn/check type ở runtime. Cả hai vẫn có strong/weak typing nuances; đừng equate static = compiled, dynamic = interpreted tuyệt đối.

## 65. Scope vs lifetime

Variable có thể out of scope nhưng object vẫn sống nếu còn reference. Static local có lexical local scope nhưng lifetime lâu.

## 66. Stack vs heap memory

Call stack thường giữ frame/local control state; heap dùng dynamic objects/allocation. Exact language runtime có abstraction riêng, nhưng exam concept nên tách automatic call lifetime và dynamic allocation.

## 67. C pointer to pointer

`int **pp` chứa address của `int*`. Dereference một lần → pointer; hai lần → int value.

Câu pointer nhiều lớp phải vẽ address/value table, không trace trong đầu.

## 68. C array parameter

Khi truyền array vào function parameter theo cú pháp thông thường, parameter thường được điều chỉnh thành pointer type. Vì vậy `sizeof(param)` trong function không cho total array size như ở original array object.

## 69. C struct vs union

Struct members có storage riêng (với padding). Union members share storage. Union size thường đủ chứa largest member + alignment.

## 70. Java static method vs overriding

Static method không dynamic-dispatch như instance overriding; method hiding/resolution khác. Nếu đề trộn `static`, đừng áp dụng máy móc rule `A x = new B(); x.f()` của instance method.

## 71. Java equals vs reference identity

`==` với object references kiểm reference identity; `.equals()` có thể được override để kiểm logical equality.

String literals/interning làm output puzzle dễ gây nhầm; tập trung semantic contract, không mẹo tình cờ.

## 72. Java checked vs unchecked exception

Checked exception thường phải catch/declare. RuntimeException hierarchy là unchecked. Nhưng “checked = recoverable” và “unchecked = unrecoverable” không phải định nghĩa formal.

## 73. Python shallow vs deep copy

Shallow copy tạo outer container mới nhưng nested objects vẫn shared. Deep copy recursively copy object graph theo khả năng/library semantics.

## 74. Python default mutable argument

Default argument được evaluate khi function definition executed, không mỗi call. Mutable default có thể giữ state qua calls.

Concept này kiểm tra lifetime/evaluation, không chỉ syntax.

## 75. Process scheduling arrival time

Không được sort chỉ theo burst nếu process chưa arrive. SJF/SRTF selection xét ready processes tại thời điểm scheduling.

## 76. Response time vs waiting time

Response time = lần đầu được CPU − arrival. Waiting time = tổng thời gian ở ready queue.

Một process có thể response sớm nhưng sau đó chờ nhiều lần → waiting lớn.

## 77. Starvation vs deadlock

Starvation: một process có thể chờ vô hạn vì scheduling/resource unfairness dù system vẫn tiến. Deadlock: set processes chờ vòng nhau và không tiến.

## 78. Aging

Aging tăng priority của process chờ lâu để giảm starvation trong priority scheduling.

## 79. Internal vs external fragmentation

Fixed-size allocation có thể lãng phí bên trong allocated block → internal. Variable-size contiguous allocation có holes bên ngoài → external.

## 80. TLB

Translation Lookaside Buffer cache recent virtual-to-physical address translations để giảm page-table lookup cost.

TLB miss không đồng nghĩa page fault: page có thể resident nhưng translation không có trong TLB.

## 81. Demand paging

Page được load khi được referenced, thay vì load toàn bộ trước. Nó dựa locality để giảm memory footprint/I/O ban đầu, nhưng page fault cost cao khi miss.

## 82. FIFO Belady anomaly

FIFO có thể tăng page faults khi tăng số frames đối với một số reference strings. LRU/Optimal thuộc stack algorithms nên không có anomaly này theo property classic.

## 83. IPv4 private ranges

Private IPv4 ranges thường cần nhận diện:

```text
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

Đừng nhầm toàn bộ `172.x.x.x` là private.

## 84. Network address vs host address

Với prefix, network address có host bits = 0; broadcast truyền thống host bits = 1. Host address nằm giữa, trừ special prefix/use cases.

## 85. Default gateway

Host gửi packet tới destination ngoài local subnet thông qua default gateway/router. DNS không làm nhiệm vụ forwarding packet.

## 86. MAC vs IP

MAC phục vụ local-link delivery; IP phục vụ logical addressing/routing across networks. Router thay đổi link-layer frame hop-by-hop trong khi IP destination có thể giữ end-to-end (trừ NAT và các mechanism khác).

## 87. TCP handshake purpose

Three-way handshake thiết lập connection state và đồng bộ initial sequence information. Nó không “mã hóa” connection; TLS làm cryptographic protection ở layer khác.

## 88. Flow control vs congestion control

Flow control bảo vệ receiver khỏi sender quá nhanh. Congestion control phản ứng capacity/congestion của network path.

## 89. DNS recursive vs iterative idea

Recursive resolver có thể thay client thực hiện chuỗi lookup. Authoritative server cung cấp records cho zone nó quản lý.

## 90. NAT

NAT translate address/port giữa domains, thường cho phép nhiều private hosts share public address bằng PAT/NAPT. NAT không phải firewall semantic hoàn chỉnh dù có thể ảnh hưởng reachability.

---

# Môn 5 — 정보시스템 구축 관리

## 91. Project risk vs issue

Risk là uncertain event/condition có thể ảnh hưởng mục tiêu. Issue là vấn đề đã xảy ra/cần xử lý hiện tại.

Risk register có probability/impact/response; issue log tracking khác.

## 92. Contingency reserve

Reserve dành cho known/identified risks khác với management reserve cho unknown/overall uncertainty theo project-management taxonomy. Nếu đề dùng terminology cụ thể, đọc wording kỹ.

## 93. Forward pass / backward pass

CPM forward pass tính earliest start/finish. Backward pass tính latest start/finish. Slack/float = khoảng delay có thể có mà không ảnh hưởng project finish theo network assumptions.

## 94. Critical path có thể thay đổi

Sau delay, acceleration hoặc dependency change, critical path có thể đổi. Không coi critical path là thuộc tính vĩnh viễn của project.

## 95. Vertical vs horizontal scaling

Vertical scale-up: tăng resource của một node. Horizontal scale-out: thêm nodes.

Scale-out cần distribution, load balancing, state/data coordination; không miễn phí.

## 96. Load balancing vs failover

Load balancing phân phối traffic/work. Failover chuyển service sang standby/healthy component khi failure.

Một load balancer có health checks có thể hỗ trợ failover, nhưng intents khác nhau.

## 97. Active-active vs active-standby

Active-active nhiều instance cùng serve traffic; active-standby có primary active và standby chờ takeover.

Active-active tăng capacity/availability nhưng consistency/state coordination phức tạp hơn.

## 98. Replication mode

Synchronous replication giảm RPO vì acknowledge sau khi replica xác nhận theo design, nhưng tăng latency/availability trade-off. Asynchronous replication giảm write latency coupling nhưng có lag/data-loss window.

## 99. Backup full/incremental/differential

Full: toàn bộ selected data.  
Incremental: changes từ backup gần nhất theo scheme.  
Differential: changes từ last full.

Restore chain và backup time/storage trade-off khác nhau.

## 100. Cold/Warm/Hot site concept

Cold site có facility cơ bản, cần thời gian setup dài. Warm có partial equipment/data readiness. Hot gần production-ready hơn, RTO thấp hơn nhưng cost cao.

## 101. RTO/RPO không phải measurement thực tế

RTO/RPO là **objectives**. Actual recovery time/data loss có thể tệ hơn nếu design/test không đáp ứng.

## 102. MTBF vs MTTR

MTBF — mean time between failures — reliability interval metric.  
MTTR — mean time to repair/recover — duration restore metric.

Availability thường tăng khi MTBF tăng hoặc MTTR giảm.

## 103. IaaS/PaaS/SaaS responsibility

Càng lên SaaS, provider quản nhiều stack hơn; customer tập trung config/data/use. IaaS customer vẫn quản OS/middleware/app nhiều hơn.

Không chỉ học tên; hỏi “ai chịu responsibility cho layer nào?”.

## 104. Container image vs running container

Image là immutable-ish packaged template/layers. Container là runtime instance của image với writable state/process namespace.

## 105. Orchestration

Container orchestration xử deployment, scheduling, scaling, health, service discovery/config/secrets tùy platform. Nó không tự sửa application logic bug.

## 106. Confidentiality vs privacy

Confidentiality là security property ngăn disclosure trái phép. Privacy rộng hơn, liên quan collection/use/retention/rights của personal data.

## 107. Threat, vulnerability, exploit, risk

Threat có khả năng gây harm. Vulnerability là weakness. Exploit là cách/code tận dụng weakness. Risk kết hợp likelihood/impact/context của harm.

## 108. Symmetric vs asymmetric crypto

Symmetric dùng shared secret và hiệu quả cho bulk encryption. Asymmetric dùng public/private key và hỗ trợ key exchange/signature scenarios nhưng computationally costlier.

Hybrid protocols thường kết hợp cả hai.

## 109. Encryption vs hashing vs encoding

Encryption reversible với key. Hash one-way digest. Encoding chỉ representation transformation, không nhằm confidentiality.

Base64 không phải encryption.

## 110. Salt vs encryption key

Password salt là non-secret random value thêm trước hashing để chống precomputed/rainbow attacks và duplicate hash patterns. Nó không cần giữ bí mật như encryption key.

## 111. MAC vs digital signature

Message Authentication Code dùng shared secret để integrity/authenticity giữa parties biết secret; digital signature dùng private/public key và hỗ trợ non-repudiation property theo trust model.

## 112. RBAC vs ACL

ACL gắn permissions theo resource và identities/groups. RBAC gán permissions cho roles rồi users nhận roles.

Hai model có thể coexist.

## 113. Least privilege vs separation of duties

Least privilege giảm quyền mỗi principal xuống mức cần thiết. Separation of Duties chia critical process qua nhiều roles để một cá nhân không tự hoàn tất toàn bộ sensitive flow.

## 114. Firewall stateful vs stateless

Stateless filter xét packet rule riêng lẻ. Stateful firewall theo dõi connection/session state để quyết định traffic liên quan.

## 115. WAF scope

WAF tập trung HTTP/application-layer patterns. Nó không thay network firewall, secure coding hay DB permissions.

## 116. SIEM concept

SIEM tập trung/chuẩn hóa/correlate security logs/events để detection/investigation. Nó không phải IDS sensor duy nhất và không tự block mọi attack.

## 117. Vulnerability scan vs penetration test

Vulnerability scan tìm known weaknesses/config signatures tự động hơn. Penetration test cố exploit/chaining trong scope để chứng minh impact.

## 118. Patch management

Không chỉ “cài patch”. Bao gồm inventory, assess severity/exposure, test compatibility, deploy, verify và rollback plan.

## 119. Incident response lifecycle

Một flow khái quát:

```text
Preparation → Detection/Analysis → Containment → Eradication → Recovery → Lessons Learned
```

Wording có thể thay đổi tùy framework nhưng intent giữ: phát hiện, hạn chế harm, loại nguyên nhân, phục hồi, cải tiến.

## 120. Backup restore test

Có backup file không chứng minh restore được. Restore drill kiểm tính toàn vẹn, procedure, dependency, credential/key và RTO thực tế.

---

# Closed-book edge-case check

Không nhìn tài liệu, trả lời ngắn 30 câu sau:

1. Ambiguity khác inconsistency thế nào?  
2. DFD balancing bảo toàn điều gì?  
3. Realization khác generalization ở đâu?  
4. Include khác extend ở Use Case thế nào?  
5. Sequential cohesion khác communicational cohesion thế nào?  
6. External coupling khác common coupling thế nào?  
7. Heap khác BST ở ordering invariant nào?  
8. MST khác shortest path ở objective nào?  
9. Stable sort bảo toàn property nào?  
10. Collision khác duplicate key thế nào?  
11. Static testing khác dynamic testing thế nào?  
12. Statement coverage 100% vì sao chưa đủ branch coverage?  
13. Candidate key và surrogate key khác vai trò nào?  
14. Prime attribute là gì?  
15. Lossless decomposition bảo vệ điều gì?  
16. Dependency preservation có thể trade-off với BCNF thế nào?  
17. `IS NULL` khác `= NULL` thế nào?  
18. Serializability khác recoverability ở đâu?  
19. TLB miss khác page fault thế nào?  
20. Response time khác waiting time thế nào?  
21. Starvation khác deadlock thế nào?  
22. Flow control khác congestion control thế nào?  
23. NAT khác firewall ở intent nào?  
24. Risk khác issue thế nào?  
25. Load balancing khác failover thế nào?  
26. RTO/RPO là objective hay measurement?  
27. Encryption/hash/encoding khác nhau ra sao?  
28. Least privilege khác separation of duties thế nào?  
29. Vulnerability scan khác penetration test thế nào?  
30. Vì sao backup phải được restore-test?

Nếu dưới 24/30 câu trả lời rõ ràng, chưa coi phần edge-case coverage là ổn.
