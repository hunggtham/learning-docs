# 정보처리기사 필기 2026 — High-Risk Confusion Atlas

> Mục tiêu của file này là xử lý nhóm câu hỏi khó nhất: **các đáp án đều nghe có vẻ đúng** nhưng chỉ một đáp án khớp chính xác với cơ chế, layer hoặc từ khóa của câu hỏi. Không học file này như flashcard. Với mỗi pair, phải trả lời được: *ranh giới nằm ở đâu, dấu hiệu đề bài là gì, và khi nào cả hai cùng xuất hiện nhưng một cái vẫn là đáp án tốt hơn?*

---

# 1. Môn 1 — 소프트웨어 설계

## 1.1 Verification vs Validation

**Verification — 검증** hỏi: sản phẩm/design/code có được xây đúng theo specification không?

**Validation — 확인/타당성 확인** hỏi: specification/sản phẩm có thực sự giải quyết nhu cầu stakeholder không?

### Dấu hiệu đề

- “conforms to specification”, “built correctly” → Verification.
- “meets user needs”, “right product” → Validation.

### Bẫy

Một system có thể verification tốt nhưng validation thất bại: code đúng spec, nhưng spec sai nhu cầu thật.

---

## 1.2 Functional vs Non-functional Requirement

**Functional Requirement — 기능 요구사항** mô tả capability/business behavior.

**Non-functional Requirement — 비기능 요구사항** mô tả quality, constraint hoặc operating condition.

### Dấu hiệu đề

`User can export report` → functional.

`Report must finish within 3 seconds for 5,000 concurrent users` → non-functional.

### Bẫy

Câu có động từ chưa chắc functional. Nếu capability vẫn tồn tại khi bỏ constraint thì constraint nhiều khả năng non-functional.

---

## 1.3 DFD vs Flowchart

**DFD** tập trung data movement và transformation giữa process, data store và external entity.

**Flowchart** tập trung control flow và sequence của step/decision.

### Bẫy

Cả hai đều có “mũi tên” và “process”. Hãy hỏi arrow biểu diễn **data** hay **control**.

---

## 1.4 Sequence Diagram vs Activity Diagram

**Sequence Diagram**: message giữa object/component theo trục thời gian.

**Activity Diagram**: workflow, branch, merge, parallel activity.

### Dấu hiệu đề

- “message order between objects” → Sequence.
- “business workflow / parallel branch” → Activity.

---

## 1.5 Aggregation vs Composition

**Aggregation**: whole–part yếu; part có thể tồn tại độc lập.

**Composition**: ownership/lifecycle mạnh; part phụ thuộc whole.

### Dấu hiệu đề

Nếu xóa whole và part cũng mất về semantic → composition.

---

## 1.6 Cohesion vs Coupling

**Cohesion — 응집도** nhìn **bên trong một module**: các phần tử có phục vụ cùng purpose không?

**Coupling — 결합도** nhìn **giữa các module**: mức phụ thuộc lẫn nhau.

### Bẫy

“High cohesion” và “low coupling” thường cùng là mục tiêu nhưng không đồng nghĩa.

---

## 1.7 Data Coupling vs Stamp Coupling

**Data Coupling**: chỉ truyền đúng dữ liệu cần thiết.

**Stamp Coupling**: truyền cả structure/object lớn hơn nhu cầu thật.

### Scenario

`send(customerId)` → Data Coupling.

`send(Customer customer)` nhưng callee chỉ dùng `customer.id` → Stamp Coupling.

---

## 1.8 Control Coupling vs Data Coupling

Nếu parameter chỉ là dữ liệu nghiệp vụ → Data Coupling.

Nếu parameter/flag quyết định branch nội bộ của module khác → Control Coupling.

```text
process(order)             → data-oriented
process(order, mode='X')   → có thể control coupling nếu mode điều khiển path nội bộ
```

---

## 1.9 SRP vs ISP

**SRP** hỏi một class/module có quá nhiều **reason to change** không.

**ISP** hỏi client có bị buộc phụ thuộc vào **interface method không dùng** không.

Class vừa gửi mail, lưu DB, generate PDF → SRP.

Interface 25 methods nhưng một client chỉ cần 2 → ISP.

---

## 1.10 OCP vs DIP

**OCP**: mở rộng behavior mà giảm sửa code ổn định.

**DIP**: high-level policy không phụ thuộc trực tiếp low-level implementation; cả hai dựa abstraction.

Dependency Injection thường giúp DIP nhưng không tự động chứng minh OCP.

---

## 1.11 Strategy vs State

Cấu trúc class có thể rất giống nhau.

**Strategy**: algorithm/policy được chọn hoặc thay thế.

**State**: behavior thay đổi vì object đang ở internal state khác.

`DiscountPolicy` → Strategy.

`OrderState: PAID → SHIPPED → CANCELLED` → State.

---

## 1.12 Adapter vs Facade

**Adapter** giải quyết **interface mismatch**.

**Facade** giải quyết **subsystem complexity** bằng một mặt tiền đơn giản.

Nếu đề nói “legacy API không tương thích” → Adapter.

Nếu nói “client phải gọi 7 subsystem và cần API đơn giản” → Facade.

---

## 1.13 Decorator vs Proxy

Cả hai đều thường wrap object.

**Decorator** thêm behavior/responsibility động.

**Proxy** kiểm soát/đại diện truy cập tới object thật: lazy, remote, protection, caching tùy loại.

Hỏi: wrapper nhằm **thêm chức năng** hay **kiểm soát access**?

---

## 1.14 Factory Method vs Abstract Factory

**Factory Method** tập trung method tạo một loại product, thường cho subclass/implementation quyết định concrete type.

**Abstract Factory** tạo **một họ các object liên quan** mà client không cần biết concrete classes.

---

## 1.15 Wireframe vs Mockup vs Prototype

Wireframe → skeleton/layout.

Mockup → hình thức trực quan gần sản phẩm.

Prototype → interaction/flow thử nghiệm.

Câu hỏi “test interaction trước implementation” thường nghiêng Prototype hơn Mockup.

---

# 2. Môn 2 — 소프트웨어 개발

## 2.1 Stack vs Queue

Stack → LIFO.

Queue → FIFO.

Không chỉ nhớ acronym: hãy trace push/pop hoặc enqueue/dequeue.

---

## 2.2 BFS vs DFS

BFS dùng frontier FIFO và khám phá theo layer; graph unweighted cho shortest path theo số cạnh.

DFS đi sâu trước; mạnh trong traversal, connectivity, cycle/topological reasoning nhưng không tự bảo đảm shortest path unweighted.

---

## 2.3 BST vs Heap

**BST** duy trì ordering relation giữa left/root/right; inorder cho sorted order nếu key phù hợp.

**Heap** chỉ bảo đảm parent-child heap property; không tạo globally sorted traversal.

Min-heap lấy minimum hiệu quả nhưng search arbitrary key không giống BST.

---

## 2.4 Binary Search vs Hash Lookup

Binary Search cần ordered structure và O(log n) comparison search.

Hash lookup average-case có thể gần O(1), nhưng không tự hỗ trợ ordered/range semantics.

---

## 2.5 Quick Sort vs Merge Sort

Quick Sort thường in-place-ish với partition và average O(n log n), nhưng worst O(n²).

Merge Sort worst O(n log n), stable trong implementation điển hình nhưng cần extra memory cho array merge.

Đề hỏi worst-case → đừng chọn theo average reputation.

---

## 2.6 Stub vs Driver

Top-down integration → thiếu lower module → **Stub**.

Bottom-up integration → thiếu upper caller → **Driver**.

Mental model: stub giả người **bị gọi**; driver giả người **đi gọi**.

---

## 2.7 Black-box vs White-box

Black-box nhìn input/output theo specification, không cần internal structure.

White-box dùng internal control/data structure của code.

Boundary Value Analysis → black-box.

Statement/Branch/Path Coverage → white-box.

---

## 2.8 Equivalence Partitioning vs Boundary Value Analysis

Equivalence Partitioning chia domain thành các class kỳ vọng behavior tương đương.

Boundary Value Analysis tập trung ngay biên và gần biên, nơi bug off-by-one dễ xuất hiện.

---

## 2.9 Retest vs Regression Test

**Retest**: kiểm lại chính defect đã sửa.

**Regression Test**: kiểm xem thay đổi có phá behavior cũ ở chỗ khác không.

Một release có thể cần cả hai.

---

## 2.10 Alpha vs Beta Test

Alpha thường nội bộ hoặc môi trường kiểm soát của tổ chức phát triển.

Beta thường do external/real users trong môi trường gần thực tế hơn trước release rộng.

---

## 2.11 Version Control vs Configuration Management

Version Control quản lý history/version/branch của source/artifact.

Configuration Management rộng hơn: identification, baseline, change control, status accounting, audit và release/configuration items.

Git là tool quan trọng nhưng không phải toàn bộ SCM/CM discipline.

---

## 2.12 Build vs Package vs Release

**Build** biến source thành executable/artifact.

**Package** gom artifact + dependency/metadata/config/manual cần cho distribution/install.

**Release** là một version được chuẩn bị/approve để phân phối/deploy theo process.

---

## 2.13 Checksum/Hash vs Digital Signature

Checksum/hash so sánh content giúp phát hiện thay đổi/corruption.

Digital Signature kết hợp cryptographic signing để hỗ trợ authenticity/integrity và non-repudiation assumptions.

Biết hash đúng không tự nói **ai** tạo package.

---

# 3. Môn 3 — 데이터베이스 구축

## 3.1 Super Key vs Candidate Key

Super Key xác định duy nhất row nhưng có thể dư attribute.

Candidate Key là **minimal superkey**.

Primary Key chỉ là candidate key được chọn làm key chính.

---

## 3.2 Candidate Key vs Primary Key

Một relation có thể có nhiều candidate keys nhưng chỉ chọn một primary key.

Các candidate key còn lại thường gọi alternate keys theo terminology truyền thống.

---

## 3.3 Selection vs Projection

Selection — σ — chọn **row** theo predicate.

Projection — π — chọn **column/attribute**.

Đừng bị đánh lừa bởi tiếng Anh “select” trong SQL vì `SELECT col` của SQL lại gần projection về relational algebra.

---

## 3.4 Partial vs Transitive Dependency

Partial dependency: non-key attribute phụ thuộc vào **một phần** composite key.

Transitive dependency: key → non-key A → non-key B.

2NF chủ yếu xử lý partial dependency; 3NF xử lý transitive dependency theo intuition thi cơ bản.

---

## 3.5 3NF vs BCNF

3NF cho phép một số FD mà determinant không là superkey nếu dependent là prime attribute theo formal definition.

BCNF chặt hơn: determinant của mọi non-trivial FD phải là superkey.

Nếu đề chỉ dùng ví dụ cơ bản, cả hai có thể cho cùng decomposition; cần nhìn formal condition khi câu hỏi cố tình tạo ngoại lệ.

---

## 3.6 Logical vs Physical Database Design

Logical design nói relation/entity, key, dependency, normalization.

Physical design nói storage, index, partition, clustering, access path, denormalization có kiểm soát.

Query chậm vì thiếu index là physical problem, không tự động là normalization problem.

---

## 3.7 B+Tree vs Hash Index

B+Tree giữ ordering → equality + range + ordered traversal.

Hash tự nhiên cho equality lookup nhưng không hỗ trợ ordered range theo cùng cách.

Nếu predicate `created_at BETWEEN ...` → B+Tree thường tự nhiên hơn.

---

## 3.8 Cardinality vs Selectivity

**Cardinality** thường nói số lượng distinct values hoặc số row tùy context thống kê.

**Selectivity** nói fraction/khả năng predicate thu hẹp data.

Column gender có cardinality thấp; `user_id` thường cardinality cao.

---

## 3.9 WHERE vs HAVING

WHERE lọc row trước grouping.

HAVING lọc group sau aggregate.

`WHERE status='PAID'` và `HAVING SUM(amount)>1000` có thể xuất hiện cùng query nhưng ở hai phase khác nhau.

---

## 3.10 COUNT(*) vs COUNT(column)

`COUNT(*)` đếm rows.

`COUNT(column)` bỏ qua NULL ở column đó.

Trong LEFT JOIN unmatched row, khác biệt này dễ xuất hiện.

---

## 3.11 INNER JOIN vs LEFT JOIN

INNER JOIN giữ match hai bên.

LEFT JOIN giữ mọi row bên trái, unmatched bên phải thành NULL.

Nếu requirement là “show all customers kể cả chưa có order” → LEFT JOIN.

---

## 3.12 NULL vs Empty String vs 0

NULL biểu diễn missing/unknown/not-applicable theo model/context.

`''` là một string value; `0` là numeric value.

Comparison với NULL dùng `IS NULL`, không dùng `= NULL` trong SQL chuẩn.

---

## 3.13 Dirty Read vs Non-repeatable Read vs Phantom

Dirty Read: đọc data chưa commit của transaction khác.

Non-repeatable Read: cùng row đọc hai lần ra value khác do committed update/delete.

Phantom: cùng predicate query ra set row khác vì insert/delete phù hợp predicate.

Unit thay đổi là key để phân biệt: **uncommitted value**, **same row value**, hay **set membership**.

---

## 3.14 Deadlock vs Lost Update

Deadlock: transactions chờ resource vòng tròn, không tiến được.

Lost Update: một update bị ghi đè/mất vì concurrent writes không được kiểm soát.

Cả hai là concurrency problem nhưng symptom hoàn toàn khác.

---

## 3.15 Serial vs Serializable

Serial schedule: transaction chạy hoàn toàn từng cái một.

Serializable schedule: interleave nhưng effect tương đương một serial order theo criterion đang xét.

Conflict-serializable không đồng nghĩa schedule phải visually serial.

---

## 3.16 Undo vs Redo

Undo quay lại effect của transaction chưa commit/aborted theo recovery strategy.

Redo tái áp effect của committed transaction chưa reflected đầy đủ trên data pages sau crash.

WAL/log sequence quyết định recovery action cụ thể.

---

## 3.17 Backup vs Checkpoint

Backup là bản sao dữ liệu để restore sau loss/corruption/disaster.

Checkpoint giúp recovery engine giảm phạm vi log cần xem khi crash recovery.

Checkpoint không thay backup.

---

# 4. Môn 4 — 프로그래밍 언어 활용

## 4.1 Process vs Thread

Process có address space/resource context riêng hơn.

Threads trong cùng process thường share address space/resources.

Thread nhẹ hơn về communication/context nhưng shared state tạo synchronization risk.

---

## 4.2 Concurrency vs Parallelism

Concurrency: nhiều task có progress overlapping về thời gian.

Parallelism: nhiều task thực sự execute đồng thời trên nhiều execution unit/core.

Single-core event loop có concurrency nhưng không nhất thiết parallel CPU execution.

---

## 4.3 Mutex vs Semaphore

Mutex thường mutual exclusion với ownership semantics.

Semaphore là counter permits; có thể cho N concurrent holders.

Binary semaphore có thể giống mutex ở vài use case nhưng không đồng nhất abstraction.

---

## 4.4 Race Condition vs Deadlock

Race Condition: result phụ thuộc timing/interleaving.

Deadlock: các participant bị kẹt vì circular resource wait.

Race có thể cho result sai nhưng chương trình vẫn chạy tiếp; deadlock thường làm progress dừng.

---

## 4.5 Deadlock Prevention vs Avoidance vs Detection

Prevention: phá ít nhất một Coffman condition.

Avoidance: chỉ cấp resource nếu state vẫn safe, ví dụ Banker’s Algorithm.

Detection: cho phép deadlock xảy ra rồi phát hiện và recover.

---

## 4.6 FCFS vs SJF vs Round Robin

FCFS → đơn giản, convoy effect.

SJF → ưu tiên burst ngắn, tốt cho average waiting trong model lý tưởng, có starvation risk.

Round Robin → time quantum, preemptive/time-sharing, trade-off responsiveness vs context-switch overhead.

---

## 4.7 Waiting vs Turnaround vs Response Time

Turnaround = Completion − Arrival.

Waiting = Turnaround − CPU service time trong bài đơn giản.

Response = First Run − Arrival.

Một process có response tốt nhưng turnaround dài nếu được chạy sớm một chút rồi phải chờ lâu sau đó.

---

## 4.8 Paging vs Segmentation

Paging chia fixed-size page/frame.

Segmentation chia logical variable-size segment.

Paging thường gắn internal fragmentation; segmentation contiguous truyền thống dễ external fragmentation.

---

## 4.9 FIFO vs LRU Page Replacement

FIFO chọn page vào memory lâu nhất.

LRU chọn page lâu nhất chưa được sử dụng.

Reference gần đây có thể cứu page trong LRU nhưng không thay arrival order của FIFO.

---

## 4.10 Page Fault vs Thrashing

Page fault là một event: referenced page chưa resident.

Thrashing là system-level condition: quá nhiều paging/page faults làm useful work giảm mạnh.

Một page fault đơn lẻ không phải thrashing.

---

## 4.11 TCP vs UDP

TCP: connection-oriented, ordered reliable byte stream.

UDP: connectionless datagram, không tự bảo đảm delivery/order.

“UDP nhanh hơn” không phải universal truth; overhead/semantics khác nhau.

---

## 4.12 IP vs MAC Address

IP dùng logical network-layer addressing/routing.

MAC dùng link-layer addressing trên local segment.

Router forward theo IP; local frame delivery dùng link-layer address.

---

## 4.13 DNS vs DHCP

DNS giải tên/record.

DHCP cấp network configuration động như IP, mask, gateway, DNS server.

---

## 4.14 Network Address vs Broadcast Address

Trong subnet truyền thống:

Network address: host bits = all 0.

Broadcast address: host bits = all 1.

Usable host thường nằm giữa hai boundary này, trừ special cases.

---

## 4.15 Overloading vs Overriding

Overloading: cùng tên, parameter signature khác; resolution chủ yếu compile-time.

Overriding: subclass cung cấp implementation mới của instance method; runtime dynamic dispatch.

Chỉ khác return type không đủ overload trong Java.

---

## 4.16 Value vs Reference/Alias Reasoning

C pointer copy address value nhưng có thể mutate pointed object.

Java pass-by-value, kể cả khi value đó là object reference.

Python assignment bind name tới object; hai names có thể alias một mutable object.

Điểm chung: **copy reference/address value không đồng nghĩa copy object**.

---

# 5. Môn 5 — 정보시스템 구축 관리

## 5.1 Waterfall vs Agile

Waterfall tổ chức phase theo sequence rõ và feedback/change thường đắt hơn khi muộn.

Agile/iterative dùng vòng feedback ngắn và incremental delivery.

Không kết luận “Agile không cần design/documentation” hoặc “Waterfall luôn sai”.

---

## 5.2 Risk vs Issue

Risk là sự kiện **có thể xảy ra** trong tương lai với probability/impact.

Issue là vấn đề **đã xảy ra/đang tồn tại** cần xử lý.

---

## 5.3 PERT vs CPM

PERT truyền thống dùng optimistic/most-likely/pessimistic estimate để tính expected duration.

CPM tập trung dependency network, path duration, critical path/slack.

Một project có thể dùng cả hai ý tưởng.

---

## 5.4 Critical Path vs Longest Activity

Critical path là **chuỗi path** quyết định project duration, không phải activity đơn lẻ dài nhất.

Một activity rất dài nhưng có float vẫn có thể không nằm critical path.

---

## 5.5 RAID vs Backup

RAID tăng availability/tolerance với một số disk failure.

Backup cung cấp restore point độc lập hơn cho deletion, corruption, ransomware, disaster tùy architecture.

RAID không phải backup.

---

## 5.6 Replication vs Backup

Replication giữ copy gần current để availability/read scale/failover.

Backup giữ recovery copy/version theo policy.

Sai dữ liệu/xóa nhầm có thể replicate nhanh sang replica; backup lịch sử có thể giúp quay lại state cũ.

---

## 5.7 HA vs DR

High Availability — 고가용성 — giảm downtime trong failure thường gặp, thường failover nhanh.

Disaster Recovery — 재해복구 — phục hồi sau sự cố lớn/failure domain rộng.

Multi-node trong cùng failure domain có thể HA nhưng vẫn DR yếu.

---

## 5.8 RTO vs RPO

RTO hỏi: **bao lâu phải khôi phục service?**

RPO hỏi: **chấp nhận mất bao nhiêu dữ liệu tính theo thời gian?**

30 phút downtime → RTO.

Mất tối đa 5 phút transaction → RPO.

---

## 5.9 Vertical vs Horizontal Scaling

Vertical: tăng resource cho một node.

Horizontal: thêm nhiều node/instance.

Horizontal scaling thường cần giải bài state distribution, load balancing và consistency.

---

## 5.10 VM vs Container

VM truyền thống có guest OS/kernel riêng trên hypervisor.

Container thường share host kernel nhưng isolate process/resources qua OS primitives.

Container không tự động “an toàn hơn” hoặc “nhanh hơn” trong mọi context.

---

## 5.11 IaaS vs PaaS vs SaaS

IaaS: provider cung cấp compute/storage/network primitives; customer quản nhiều layer OS/runtime/app hơn.

PaaS: provider quản platform/runtime nhiều hơn, customer tập trung application/data.

SaaS: customer sử dụng ứng dụng hoàn chỉnh.

Hãy hỏi **ai quản layer nào**, không học bằng tên vendor.

---

## 5.12 Authentication vs Authorization

Authentication — 인증 — xác minh identity.

Authorization — 인가/권한부여 — quyết định identity đó được phép làm gì.

Login đúng không có nghĩa được quyền đọc mọi invoice.

---

## 5.13 Hashing vs Encryption

Hashing là one-way digest theo design cryptographic; dùng integrity/password storage với scheme phù hợp.

Encryption là reversible với key, dùng confidentiality.

Password không nên lưu bằng reversible encryption như substitute cho password hashing KDF.

---

## 5.14 Symmetric vs Asymmetric Cryptography

Symmetric dùng cùng secret key family cho encrypt/decrypt, hiệu quả với bulk data.

Asymmetric dùng public/private key pair, phù hợp key exchange/signature và một số encryption use case.

TLS thường kết hợp nhiều primitive, không phải chỉ “asymmetric encryption”.

---

## 5.15 SQL Injection vs XSS

SQL Injection làm untrusted input thay đổi cấu trúc/ý nghĩa SQL command.

Core defense: parameterized query/prepared statement.

XSS đưa script/content độc hại vào browser context.

Core defense: context-aware output encoding/escaping, template safety và related controls.

Cả hai đều liên quan input, nhưng root cause/sink khác nhau.

---

## 5.16 Firewall vs WAF

Network firewall kiểm traffic theo network/transport rule và context thiết bị.

WAF hiểu HTTP/web application semantics sâu hơn để filter web attack patterns.

WAF không thay secure coding; firewall L3/L4 không tự giải SQL injection root cause.

---

## 5.17 IDS vs IPS

IDS thiên detection/alert.

IPS thường inline và có khả năng block/prevent traffic.

Deployment thực tế đa dạng, nhưng đây là ranh giới conceptual thường dùng trong đề.

---

## 5.18 TLS vs VPN

TLS bảo vệ một application/session/channel cụ thể theo protocol setup.

VPN tạo protected tunnel/network overlay giữa endpoint/network.

Cả hai có thể dùng cryptography nhưng scope khác.

---

## 5.19 Threat vs Vulnerability vs Risk

Threat: tác nhân/sự kiện có thể gây hại.

Vulnerability: weakness có thể bị khai thác.

Risk: khả năng + impact của harm trong context cụ thể.

Control giảm likelihood/impact/exposure nhưng không nhất thiết xóa threat.

---

# 6. Meta-confusions — khi hai đáp án đều đúng

## 6.1 Root cause vs Defense in Depth

Nếu SQL injection xảy ra, cả WAF và prepared statement đều có thể giúp. Nhưng nếu đề hỏi **biện pháp trực tiếp xử lý nguyên nhân trong code**, prepared statement là đáp án mạnh hơn.

Nếu hỏi “additional perimeter control”, WAF có thể đúng.

Câu hỏi thi thường không chỉ kiểm fact; nó kiểm **scope của fact**.

---

## 6.2 Mechanism vs Goal

Ví dụ:

```text
Goal: Availability
Mechanisms: redundancy, replication, failover
```

Nếu hỏi “thuộc tính chất lượng” → Availability.

Nếu hỏi “cách đạt thuộc tính đó” → mechanism cụ thể.

---

## 6.3 Symptom vs Cause

Slow query là symptom.

Nguyên nhân có thể là full scan, poor cardinality estimate, missing index, lock wait, I/O saturation hoặc design khác.

Đừng chọn giải pháp chỉ vì nó “liên quan performance”. Chọn đáp án khớp evidence trong đề.

---

## 6.4 Logical layer vs Physical layer

Normalization đúng logic không đảm bảo query nhanh.

TLS đúng network security không đảm bảo object-level authorization.

Mutex đúng trong một process không bảo vệ shared state giữa nhiều server instances.

Đây là pattern chung: một mechanism có thể đúng **ở layer của nó** nhưng không đủ cho invariant ở layer khác.

---

# 7. Closed-book discrimination test

Không nhìn phần trên, tự trả lời trong một câu cho mỗi cặp:

1. Verification / Validation  
2. DFD / Flowchart  
3. Sequence / Activity Diagram  
4. Aggregation / Composition  
5. Cohesion / Coupling  
6. Data / Stamp Coupling  
7. SRP / ISP  
8. OCP / DIP  
9. Strategy / State  
10. Adapter / Facade  
11. Decorator / Proxy  
12. Stub / Driver  
13. Black-box / White-box  
14. Retest / Regression  
15. Version Control / Configuration Management  
16. Super Key / Candidate Key  
17. Partial / Transitive Dependency  
18. 3NF / BCNF  
19. B+Tree / Hash Index  
20. WHERE / HAVING  
21. COUNT(*) / COUNT(column)  
22. Dirty / Non-repeatable / Phantom Read  
23. Deadlock / Lost Update  
24. Serial / Serializable  
25. Backup / Checkpoint  
26. Process / Thread  
27. Concurrency / Parallelism  
28. Mutex / Semaphore  
29. Race / Deadlock  
30. Prevention / Avoidance / Detection  
31. Waiting / Turnaround / Response Time  
32. FIFO / LRU  
33. Page Fault / Thrashing  
34. TCP / UDP  
35. DNS / DHCP  
36. Overloading / Overriding  
37. Risk / Issue  
38. PERT / CPM  
39. RAID / Backup  
40. Replication / Backup  
41. HA / DR  
42. RTO / RPO  
43. Vertical / Horizontal Scaling  
44. VM / Container  
45. Authentication / Authorization  
46. Hashing / Encryption  
47. SQL Injection / XSS  
48. Firewall / WAF  
49. IDS / IPS  
50. Threat / Vulnerability / Risk

Nếu một cặp cần nhìn đáp án mới giải thích được, hãy đánh dấu `CONFUSION GAP` và quay lại deep-dive tương ứng trước khi làm full mock.