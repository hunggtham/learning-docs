# 정보처리기사 필기 2026 — Full Mock #2: Hard Mode 100

> **100 câu tự viết mới, 20 câu/môn.** Mock #2 cố ý dùng wording gần nhau, scenario nhiều layer và distractor “đúng nhưng không đúng nhất”. Không mở answer key trước khi hoàn thành toàn bộ 100 câu.
>
> Chấm như đề thật: mỗi môn 20 câu; mô phỏng 과락 nếu dưới 8/20 ở bất kỳ môn nào. Sau khi chấm, dùng `14-error-remediation-map.md` thay vì chỉ ghi đáp án.

---

# 제1과목 — 소프트웨어 설계

## Q1
Hai requirement sau cùng tồn tại:

```text
R1: User session hết hạn sau 30 phút không hoạt động.
R2: User session phải tồn tại tối thiểu 8 giờ bất kể hoạt động.
```

Vấn đề chính là:

A. Ambiguity  
B. Inconsistency  
C. Incompleteness  
D. Untraceability

## Q2
Requirement “search phải nhanh” có vấn đề chính nào trước tiên?

A. Không functional  
B. Không measurable/verifiable đủ rõ  
C. Không thể implement bằng database  
D. Không thể trace

## Q3
Context-level DFD có input `Order` và output `Receipt`. Khi phân rã process, level con tạo thêm external output `CreditScore` nhưng level trên không có. Khái niệm cần kiểm tra là:

A. Encapsulation  
B. DFD balancing  
C. Polymorphism  
D. Fan-in

## Q4
Muốn biểu diễn một object `Order` chuyển `CREATED → PAID → SHIPPED` theo event. Diagram phù hợp nhất:

A. Activity  
B. State Machine  
C. Deployment  
D. Component

## Q5
Use case `Checkout` luôn gọi `Validate Cart`; `Apply Coupon` chỉ xảy ra khi có coupon. Quan hệ phù hợp nhất:

A. Checkout extend Validate Cart; Apply Coupon include Checkout  
B. Checkout include Validate Cart; Apply Coupon extend Checkout  
C. Cả hai đều generalization  
D. Cả hai đều composition

## Q6
Một class `ReportService` vừa query DB, format PDF, gửi email, ghi audit và upload S3. Principle bị đe dọa trực tiếp nhất:

A. LSP  
B. SRP  
C. ISP  
D. OCP

## Q7
Một interface có 25 method; client A chỉ cần 2 method nhưng buộc implement/depend toàn bộ. Principle phù hợp nhất:

A. ISP  
B. LSP  
C. SRP  
D. Singleton

## Q8
Subclass `Square` kế thừa `Rectangle`, nhưng setter width/height của base class làm code client phá assumption khi dùng Square. Principle được nhắc tới rõ nhất:

A. DIP  
B. LSP  
C. ISP  
D. SRP

## Q9
Module A truyền cả `CustomerRecord` cho B, trong khi B chỉ dùng `customerId`. Đây là:

A. Data coupling  
B. Stamp coupling  
C. Control coupling  
D. Common coupling

## Q10
Hai module cùng phụ thuộc vào một định dạng file bên ngoài cố định. Đây gần nhất với:

A. External coupling  
B. Common coupling  
C. Content coupling  
D. Data coupling

## Q11
Pattern nào phù hợp nhất khi behavior thay đổi theo **internal lifecycle state** của object?

A. Strategy  
B. State  
C. Adapter  
D. Facade

## Q12
Pattern nào phù hợp khi cần thay đổi algorithm tính phí theo market/channel mà caller dùng cùng interface?

A. State  
B. Strategy  
C. Observer  
D. Composite

## Q13
Một subsystem có 8 service phức tạp; client chỉ cần một entry point đơn giản. Pattern:

A. Adapter  
B. Facade  
C. Decorator  
D. Prototype

## Q14
Một wrapper thêm logging và caching quanh service mà giữ cùng interface. Pattern gần nhất:

A. Decorator  
B. Builder  
C. State  
D. Memento

## Q15
Diagram nào trả lời tốt nhất câu hỏi “artifact nào deploy trên node nào?”

A. Component  
B. Deployment  
C. Class  
D. Sequence

## Q16
Traceability giúp trực tiếp nhất cho:

A. Tăng CPU clock  
B. Impact analysis và kiểm coverage từ requirement tới test  
C. Chọn subnet mask  
D. Mã hóa file

## Q17
Một payment request timeout sau khi server đã commit. Client retry cùng logical request. Property cần thiết nhất ở interface/business operation là:

A. Inheritance  
B. Idempotency  
C. Compression  
D. Aggregation

## Q18
Thay field API từ optional thành required mà không versioning có rủi ro chính:

A. Physical fragmentation  
B. Backward compatibility break  
C. CPU starvation  
D. Deadlock

## Q19
Point-to-point integration giữa N systems tăng vấn đề gì khi N lớn?

A. Dependency/connection complexity  
B. Không thể dùng HTTP  
C. Không thể retry  
D. Không có data format

## Q20
Một architecture style chia xử lý thành nhiều stage độc lập, output stage trước thành input stage sau. Gần nhất:

A. Repository  
B. Pipe-and-Filter  
C. MVC  
D. Client-Server

---

# 제2과목 — 소프트웨어 개발

## Q21
Stack là:

A. Implementation duy nhất bằng array  
B. ADT có thể implement bằng nhiều structure  
C. Luôn FIFO  
D. Luôn tree

## Q22
Một max-heap bảo đảm điều gì?

A. Mọi node trái nhỏ hơn mọi node phải  
B. Parent không nhỏ hơn child theo heap property  
C. Inorder traversal luôn sorted  
D. Search arbitrary key luôn O(log n)

## Q23
Graph có 1 triệu vertices nhưng chỉ 2 triệu edges. Representation thường tiết kiệm memory hơn:

A. Adjacency Matrix  
B. Adjacency List  
C. Full table V×V bắt buộc  
D. Stack

## Q24
Muốn shortest path theo số cạnh trong graph unweighted:

A. DFS  
B. BFS  
C. Prim  
D. Kruskal

## Q25
Mục tiêu của Minimum Spanning Tree là:

A. Tối thiểu distance từ source tới mọi node  
B. Nối tất cả vertices với tổng edge weight nhỏ nhất mà không cycle  
C. Tìm strongly connected components  
D. Sort vertices

## Q26
Sort ổn định nghĩa là:

A. Không dùng memory phụ  
B. Luôn O(n log n)  
C. Giữ relative order của records có key bằng nhau  
D. Không bao giờ swap

## Q27
Hash collision là:

A. Cùng logical key xuất hiện hai lần  
B. Hai key khác nhau map tới cùng bucket/index  
C. Table đầy hoàn toàn  
D. Hash function trả negative

## Q28
Trong linear probing, xóa một item bằng cách đặt slot thành “never used” có thể phá:

A. Probe chain  
B. Tree balance  
C. Stack pointer  
D. TCP sequence

## Q29
Review source code mà không execute là:

A. Dynamic testing  
B. Static testing  
C. Load testing  
D. Beta testing

## Q30
Human hiểu sai requirement và viết sai condition. Sai condition trong code là:

A. Failure observable  
B. Defect/Fault  
C. Network latency  
D. Recovery point

## Q31
Một test suite đạt 100% statement coverage. Kết luận an toàn nhất:

A. Mọi branch đã chạy cả true và false  
B. Mọi path đã test  
C. Không thể suy ra branch/path coverage đầy đủ  
D. Không còn bug

## Q32
Black-box technique nào tập trung ngay cạnh giới hạn hợp lệ/không hợp lệ?

A. Branch Coverage  
B. Boundary Value Analysis  
C. Path Coverage  
D. Statement Coverage

## Q33
Top-down integration khi module con chưa có dùng:

A. Driver  
B. Stub  
C. Proxy bắt buộc  
D. Hash table

## Q34
Bottom-up integration khi caller phía trên chưa có dùng:

A. Stub  
B. Driver  
C. Semaphore  
D. Mock DB bắt buộc

## Q35
Sau bug fix, chạy test cụ thể chứng minh bug đã hết gọi gần nhất là:

A. Retest/confirmation test  
B. Regression-only  
C. Alpha test  
D. Static test

## Q36
Chạy broader existing suite để xem bug fix có phá chức năng khác là:

A. Regression test  
B. Unit compile  
C. Acceptance-only  
D. Mutation-only

## Q37
Artifact nào có thể là configuration item?

A. Chỉ source code  
B. Source, config, schema, build script, test artifact, manual  
C. Chỉ binary  
D. Chỉ README

## Q38
Build khác release ở đâu?

A. Build tạo artifact; release là process/decision đưa version xác định ra environment/user  
B. Hai từ đồng nghĩa  
C. Release chỉ compile source  
D. Build luôn production

## Q39
Checksum trên package chủ yếu kiểm:

A. Authorization  
B. Integrity/change/corruption  
C. CPU speed  
D. Business role

## Q40
Một interface production có timeout tăng nhưng error rate thấp. Metric quan trọng để phát hiện issue này là:

A. Latency/response-time distribution  
B. Chỉ success count  
C. Chỉ version number  
D. Chỉ line count source

---

# 제3과목 — 데이터베이스 구축

## Q41
Trong relational terminology cơ bản, degree là:

A. Số rows  
B. Số attributes  
C. Số indexes  
D. Số foreign keys

## Q42
Candidate key là:

A. Bất kỳ superkey nào  
B. Minimal superkey  
C. Luôn surrogate key  
D. Luôn single-column

## Q43
Một table dùng surrogate `id`, nhưng email phải unique theo business. Cần:

A. Không cần constraint email vì đã có id  
B. Unique constraint/business candidate-key enforcement cho email nếu requirement yêu cầu  
C. Bỏ primary key  
D. Chuyển email thành index không unique là đủ

## Q44
FD `{A,B} → A` là:

A. Partial  
B. Trivial  
C. Transitive  
D. Multivalued

## Q45
Relation có candidate key `(A,B)`, và `A → C`, C non-prime. Vi phạm rõ nhất:

A. 1NF  
B. 2NF  
C. BCNF nhưng không 2NF  
D. Không normalization issue

## Q46
3NF formal cho FD `X → A` chấp nhận nếu:

A. X là superkey hoặc A là prime attribute, ngoài trivial condition  
B. X luôn single attribute  
C. A phải foreign key  
D. Relation có index

## Q47
BCNF mạnh hơn 3NF chủ yếu vì:

A. Mọi determinant của non-trivial FD phải là superkey  
B. Cấm foreign key  
C. Cấm composite key  
D. Cấm NULL

## Q48
Lossless decomposition bảo đảm:

A. Query luôn nhanh hơn  
B. Join lại không tạo/mất information sai theo dependency assumptions  
C. Không cần indexes  
D. Không có deadlock

## Q49
Dependency preservation quan tâm:

A. Có enforce các FD từ relation con mà không cần join phức tạp không  
B. Disk capacity  
C. TCP retransmission  
D. Backup retention

## Q50
Index `(customer_id, created_at)` hữu ích tự nhiên cho query equality theo customer + range/order theo time vì:

A. B+Tree key ordering có thể thu hẹp prefix rồi scan ordered range  
B. Hash luôn hỗ trợ range tốt hơn  
C. Index bỏ qua equality  
D. Normalization tự tạo index

## Q51
Một boolean column phân bố gần 50/50 thường có:

A. Selectivity rất cao như unique key  
B. Selectivity tương đối thấp  
C. Cardinality bằng số rows luôn  
D. Không thể index

## Q52
`WHERE YEAR(created_at)=2026` trên indexed `created_at` có thể kém sargable hơn range predicate vì:

A. Function trên column có thể cản index range seek tùy DBMS  
B. YEAR luôn syntax error  
C. Index không dùng với date  
D. Range query không tồn tại

## Q53
SQL kiểm NULL đúng cách:

A. `col = NULL`  
B. `col IS NULL`  
C. `col == NULL`  
D. `NULL(col)`

## Q54
`COUNT(col)` khác `COUNT(*)` vì:

A. `COUNT(col)` bỏ qua NULL  
B. `COUNT(*)` bỏ qua mọi NULL row  
C. Hai cái luôn giống  
D. COUNT chỉ dùng numeric

## Q55
UNION ALL khác UNION:

A. UNION ALL giữ duplicate; UNION loại duplicate  
B. UNION ALL chỉ numeric  
C. UNION luôn nhanh hơn  
D. UNION ALL sort bắt buộc

## Q56
T2 đọc uncommitted value từ T1; T1 abort khiến T2 phải rollback. Đây liên quan:

A. Cascading rollback  
B. Phantom only  
C. Heap overflow  
D. NAT

## Q57
Basic Two-Phase Locking có phases:

A. Read/Write  
B. Growing acquire locks rồi Shrinking release locks  
C. Commit/Rollback only  
D. Encode/Decode

## Q58
Precedence graph có cycle. Kết luận:

A. Conflict-serializable  
B. Không conflict-serializable  
C. Chắc chắn deadlock runtime  
D. Chắc chắn recoverable

## Q59
Checkpoint khác backup vì:

A. Checkpoint hỗ trợ recovery coordination/log scan; backup là copy data để restore  
B. Checkpoint luôn offsite  
C. Backup nằm trong RAM  
D. Hai cái đồng nghĩa

## Q60
Migration chỉ so row count là chưa đủ vì có thể vẫn sai:

A. Value precision, encoding, referential integrity, aggregates, business invariants  
B. Chỉ CSS  
C. Chỉ CPU model  
D. Chỉ DNS TTL

---

# 제4과목 — 프로그래밍 언어 활용

## Q61
Static typing đồng nghĩa tuyệt đối với compiled language?

A. Có  
B. Không; typing discipline và execution model là dimensions khác nhau  
C. Chỉ với Java  
D. Chỉ với C

## Q62
Scope khác lifetime vì:

A. Scope là visibility trong source; lifetime là thời gian object/storage tồn tại runtime  
B. Hai cái giống nhau  
C. Lifetime chỉ compile-time  
D. Scope chỉ heap

## Q63
Trong C, `int **pp` là:

A. Int value  
B. Pointer tới pointer tới int  
C. Array 2 chiều bắt buộc  
D. Function pointer

## Q64
Trong C function parameter `int a[]`, `sizeof(a)` thường cho:

A. Total original array size  
B. Pointer size do parameter adjustment  
C. 0  
D. Compile error luôn

## Q65
Union khác struct chủ yếu ở:

A. Members share storage  
B. Không có type  
C. Không thể chứa int  
D. Luôn lớn hơn tổng members

## Q66
Java instance method overridden được chọn chủ yếu theo:

A. Runtime object type  
B. Chỉ reference variable name  
C. Return type  
D. File name

## Q67
Java static method khi subclass định nghĩa cùng signature:

A. Dynamic overriding giống instance method hoàn toàn  
B. Method hiding/resolution khác dynamic instance dispatch  
C. Compile error luôn  
D. Không thể có static

## Q68
Với object references Java, `==` thường kiểm:

A. Logical equality do `.equals()`  
B. Reference identity  
C. Hash code equality bắt buộc  
D. String content luôn

## Q69
Python shallow copy của nested list:

A. Copy recursively mọi nested object  
B. Outer container mới nhưng nested objects có thể vẫn shared  
C. Không tạo object mới  
D. Chuyển thành tuple

## Q70
Python mutable default argument có thể giữ state giữa calls vì:

A. Default được evaluate khi function definition executed  
B. Python reset process mỗi call  
C. List immutable  
D. `def` không tạo object

## Q71
SJF tại thời điểm t chỉ được chọn trong:

A. Mọi process kể cả chưa arrive  
B. Ready processes đã arrive  
C. Terminated processes  
D. I/O devices

## Q72
Response time là:

A. Completion - arrival  
B. First CPU run - arrival  
C. Total ready waiting  
D. Burst - arrival

## Q73
Aging dùng để giảm:

A. Starvation  
B. Deadlock cycle bắt buộc  
C. Page size  
D. IP fragmentation

## Q74
TLB miss có nghĩa:

A. Chắc chắn page fault  
B. Translation không ở TLB; page vẫn có thể resident  
C. Disk hỏng  
D. Process deadlock

## Q75
Thrashing xảy ra khi:

A. Useful work bị áp đảo bởi paging activity  
B. CPU không có cache  
C. DNS fail  
D. DB normalize

## Q76
Private IPv4 nào đúng?

A. 172.0.0.0/8 toàn bộ  
B. 172.16.0.0/12  
C. 169.0.0.0/8 toàn bộ  
D. 11.0.0.0/8

## Q77
Host `192.168.1.70/26` thuộc network:

A. 192.168.1.0  
B. 192.168.1.64  
C. 192.168.1.128  
D. 192.168.1.192

## Q78
Default gateway dùng khi:

A. Destination nằm ngoài local subnet và cần router forward  
B. Resolve domain  
C. Encrypt packet  
D. Detect SQL injection

## Q79
TCP flow control chủ yếu bảo vệ:

A. Receiver khỏi sender gửi quá nhanh  
B. Toàn Internet khỏi routing loop  
C. Password storage  
D. DNS authority

## Q80
Three-way handshake của TCP không cung cấp trực tiếp:

A. Connection state establishment  
B. Sequence synchronization  
C. Encryption/confidentiality  
D. Connection-oriented setup

---

# 제5과목 — 정보시스템 구축 관리

## Q81
Risk khác issue ở điểm:

A. Risk chưa chắc xảy ra; issue đã xảy ra/cần xử lý  
B. Issue luôn positive  
C. Risk không có impact  
D. Hai cái giống nhau

## Q82
Trong CPM, forward pass chủ yếu tính:

A. Earliest start/finish  
B. Latest start/finish  
C. Password hash  
D. Subnet range

## Q83
Một non-critical activity có float 3 ngày. Delay 2 ngày, mọi assumption khác giữ nguyên. Kết luận hợp lý nhất:

A. Project chắc chắn delay 2 ngày  
B. Có thể chưa ảnh hưởng final finish nếu vẫn trong float  
C. Critical path biến mất  
D. Không cần theo dõi nữa

## Q84
Vertical scaling là:

A. Thêm nodes  
B. Tăng resource của một node  
C. Chia subnet  
D. Add backup site

## Q85
Load balancing khác failover vì:

A. Load balancing phân phối work; failover chuyển sang healthy/standby khi failure  
B. Hai cái đồng nghĩa  
C. Failover chỉ DB  
D. Load balancing chỉ storage

## Q86
Synchronous replication trade-off điển hình:

A. Giảm data-loss window nhưng tăng latency/coupling với replica health  
B. Không cần network  
C. RPO luôn vô hạn  
D. Không có consistency

## Q87
Differential backup thường chứa:

A. Changes từ last full backup  
B. Changes từ immediate previous backup bất kể type  
C. Toàn disk bắt buộc  
D. Chỉ metadata

## Q88
Hot site so với cold site thường:

A. Recovery nhanh hơn nhưng cost cao hơn  
B. Recovery chậm hơn và rẻ hơn luôn  
C. Không có equipment  
D. Không có data strategy

## Q89
RPO 5 phút nghĩa:

A. Service phải phục hồi trong 5 phút  
B. Mục tiêu mức mất dữ liệu theo thời gian tối đa khoảng 5 phút  
C. Backup chạy 5 phút  
D. MTTR 5 phút

## Q90
MTTR giảm thường giúp:

A. Availability tăng, các yếu tố khác giữ nguyên  
B. Availability giảm  
C. RPO tăng bắt buộc  
D. CPU clock giảm

## Q91
Trong IaaS, customer thường còn trách nhiệm nhiều hơn SaaS về:

A. OS/middleware/application configuration  
B. Physical datacenter hoàn toàn  
C. Provider staff  
D. Internet backbone toàn cầu

## Q92
Container image là:

A. Runtime process instance duy nhất  
B. Packaged template/layers dùng để tạo containers  
C. Hypervisor  
D. DNS zone

## Q93
Base64 là:

A. Encryption  
B. Encoding  
C. Hash  
D. Signature

## Q94
Password salt chủ yếu giúp:

A. Chống precomputed hash/rainbow attacks và làm cùng password không ra cùng stored hash pattern  
B. Mã hóa reversible password  
C. Thay password policy  
D. Tạo digital signature

## Q95
MAC khác digital signature vì MAC:

A. Dùng shared secret giữa parties  
B. Luôn dùng public/private key  
C. Không kiểm integrity  
D. Chỉ dùng cho database

## Q96
RBAC cấp quyền bằng cách:

A. Gắn permissions với roles rồi assign users vào roles  
B. Mỗi packet có ACL  
C. Mọi user admin  
D. Chỉ dùng encryption

## Q97
Least privilege khác Separation of Duties vì:

A. Một cái giảm mức quyền; một cái chia critical responsibility qua nhiều principals/roles  
B. Hai cái giống nhau  
C. SoD chỉ firewall  
D. Least privilege chỉ password

## Q98
Stateful firewall khác stateless filter vì:

A. Theo dõi connection/session state  
B. Luôn decrypt TLS  
C. Luôn là WAF  
D. Không có rules

## Q99
Vulnerability scan khác penetration test ở chỗ:

A. Scan thường tìm known weaknesses tự động hơn; pentest cố exploit/chaining để chứng minh impact trong scope  
B. Pentest không cần authorization  
C. Scan luôn sửa bug  
D. Hai cái giống nhau

## Q100
Incident response sau containment thường cần tiếp tục với:

A. Eradication và recovery, rồi lessons learned  
B. Xóa logs  
C. Tắt backup  
D. Bỏ root-cause analysis

---

# Answer Key

```text
1 B   2 B   3 B   4 B   5 B
6 B   7 A   8 B   9 B  10 A
11 B 12 B 13 B 14 A 15 B
16 B 17 B 18 B 19 A 20 B

21 B 22 B 23 B 24 B 25 B
26 C 27 B 28 A 29 B 30 B
31 C 32 B 33 B 34 B 35 A
36 A 37 B 38 A 39 B 40 A

41 B 42 B 43 B 44 B 45 B
46 A 47 A 48 B 49 A 50 A
51 B 52 A 53 B 54 A 55 A
56 A 57 B 58 B 59 A 60 A

61 B 62 A 63 B 64 B 65 A
66 A 67 B 68 B 69 B 70 A
71 B 72 B 73 A 74 B 75 A
76 B 77 B 78 A 79 A 80 C

81 A 82 A 83 B 84 B 85 A
86 A 87 A 88 A 89 B 90 A
91 A 92 B 93 B 94 A 95 A
96 A 97 A 98 A 99 A 100 A
```

---

# High-value rationales

## Q1
Hai requirement cho cùng session lifetime nhưng đưa constraint mâu thuẫn. Đây là **inconsistency**, không phải ambiguity.

## Q3
DFD decomposition phải bảo toàn logical external input/output của parent process. Đây là **balancing**.

## Q5
`include` cho behavior được reuse như phần bắt buộc; `extend` cho behavior tùy điều kiện/extension point.

## Q8
LSP hỏi subtype có thay thế base type mà không phá expectation/contract không.

## Q10
External coupling liên quan external format/protocol/device interface chung; common coupling là shared global data.

## Q17
Timeout làm client không biết outcome cuối cùng; idempotency bảo repeated same logical operation không nhân side effect.

## Q22
Heap chỉ bảo đảm parent-child heap property, không full ordering như BST.

## Q25
MST tối ưu tổng weight để connect all vertices, khác shortest path từ source.

## Q31
Statement coverage không chứng minh mọi branch outcome/path được exercise.

## Q35–36
Retest xác nhận defect cụ thể đã sửa; regression kiểm side effects trên behavior khác.

## Q43
Surrogate primary key không tự enforce business uniqueness của candidate key tự nhiên.

## Q46
3NF formal cho phép determinant là superkey **hoặc** dependent attribute là prime, ngoài trivial dependency.

## Q48–49
Lossless bảo toàn information khi join lại; dependency preservation bảo toàn khả năng enforce dependencies ở relations con.

## Q52
Sargability nối cách viết predicate với khả năng optimizer dùng access path/index hiệu quả.

## Q56
Dirty dependency có thể gây cascading rollback nếu reader phụ thuộc transaction chưa commit.

## Q61
Static/dynamic typing và compiled/interpreted/JIT là dimensions khác nhau.

## Q67
Static method không dùng runtime polymorphic dispatch giống overridden instance method.

## Q74
TLB miss chỉ là translation cache miss; page table có thể map tới resident frame nên không page fault.

## Q77
`/26` block size 64: ranges 0–63, 64–127, ...; 70 thuộc network `.64`.

## Q79
TCP flow control bảo vệ receiver; congestion control phản ứng trạng thái network path.

## Q83
Float/slack cho phép một mức delay không đổi project finish, nếu assumptions/network không đổi.

## Q86
Sync replication trade RPO/data durability against write latency và dependence vào replica/network availability.

## Q89
RPO là data-loss objective; RTO là service recovery-time objective.

## Q93
Encoding không cung cấp confidentiality. Base64 chỉ thay representation.

## Q95
MAC dựa shared secret; digital signature dùng asymmetric key và có trust/non-repudiation semantics khác.

## Q97
Least privilege hỏi “bao nhiêu quyền”; SoD hỏi “một người có được làm toàn bộ critical flow không”.

---

# Score interpretation

| Môn | Correct / 20 | Action |
|---|---:|---|
| 1 | ___ | nếu < 12: quay `01`, `11`, `12`, `15` |
| 2 | ___ | nếu < 12: quay `02`, `08`, `11`, `15` |
| 3 | ___ | nếu < 12: quay `03`, `08`, `11`, `15` |
| 4 | ___ | nếu < 12: quay `04`, `08`, `13`, `15` |
| 5 | ___ | nếu < 12: quay `05`, `11`, `12`, `15` |

Ngưỡng 8/20 ở đây chỉ mô phỏng 과락 40 điểm. Mục tiêu học nên cao hơn: **ít nhất 14/20 mỗi môn ở mock tự viết**, vì đề thật có thể dùng wording và distribution khác.

## Error audit bắt buộc

Mỗi câu sai phải ghi:

```text
Q__
Subject:
Error code: COV / CON / PRO / LAY / TERM / READ / CAL / MEM
Why my choice looked plausible:
Why correct answer fits wording better:
Source file to revisit:
Transfer question I can now answer:
```

Không làm lại ngay cùng câu để “nhớ đáp án”. Sau remediation, hãy tự tạo một scenario mới cùng mechanism nhưng đổi nouns/numbers.
