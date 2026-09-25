# 정보처리기사 필기 2026 — Full Mock Exam 100 Questions

> **Đề tự viết mới, không sao chép 기출.** Cấu trúc mô phỏng đúng tỷ lệ chính thức: 5 môn × 20 câu = 100 câu. Mục tiêu là kiểm tra coverage, discrimination và procedural reasoning sau khi hoàn thành Master Guide + 5 deep-dive + workbook.
>
> Làm toàn bộ câu hỏi trước khi mở phần đáp án. Với 20 câu mỗi môn, mỗi câu tương đương 5 điểm trong môn đó. Để mô phỏng điều kiện đỗ: mỗi môn cần ít nhất 8/20 câu đúng và tổng thể cần ít nhất 60/100 câu đúng.

---

# 제1과목 — 소프트웨어 설계 — Software Design

## Q1

Requirement nào là **non-functional requirement — 비기능 요구사항** rõ nhất?

A. User có thể đổi mật khẩu  
B. Admin có thể khóa tài khoản  
C. 95% request phải trả lời trong 500 ms  
D. User có thể tải invoice

## Q2

Câu hỏi “Are we building the right product?” gắn gần nhất với:

A. Verification  
B. Validation  
C. Compilation  
D. Refactoring

## Q3

Trong DFD — Data Flow Diagram — thành phần nào biểu diễn nơi dữ liệu được lưu giữ?

A. Process  
B. Data Store  
C. External Entity  
D. Data Flow

## Q4

Muốn biểu diễn thứ tự message giữa `Controller`, `Service`, `Repository` theo thời gian, diagram phù hợp nhất là:

A. Sequence Diagram  
B. Class Diagram  
C. Deployment Diagram  
D. Package Diagram

## Q5

`Order` chứa `OrderLine`; `OrderLine` không có lifecycle độc lập và bị hủy khi `Order` bị hủy. Quan hệ UML phù hợp nhất:

A. Aggregation  
B. Composition  
C. Dependency  
D. Realization

## Q6

Mục tiêu thiết kế module tốt thường là:

A. Low cohesion, high coupling  
B. High cohesion, high coupling  
C. High cohesion, low coupling  
D. Low cohesion, low coupling

## Q7

Module A chỉ truyền đúng `customerId` mà module B cần thông qua parameter. Đây gần nhất với:

A. Content Coupling  
B. Common Coupling  
C. Control Coupling  
D. Data Coupling

## Q8

Module A truyền toàn bộ object `Customer` cho B dù B chỉ dùng `customerId`. Đây gần nhất với:

A. Stamp Coupling  
B. Data Coupling  
C. Content Coupling  
D. Common Coupling

## Q9

SOLID principle nào nhấn mạnh “một class/module nên có một lý do chính để thay đổi”?

A. SRP  
B. OCP  
C. LSP  
D. DIP

## Q10

`PaymentService` nhận một interface `PaymentGateway` qua constructor thay vì trực tiếp `new ConcreteKakaoClient()`. Thiết kế này hỗ trợ rõ nhất principle nào?

A. ISP  
B. DIP  
C. LSP  
D. SRP

## Q11

Hệ thống cần thay đổi thuật toán tính discount tại runtime mà client dùng cùng một interface. Pattern phù hợp nhất:

A. Strategy  
B. State  
C. Observer  
D. Prototype

## Q12

Một thư viện cũ có interface `legacyPay()`, hệ thống mới mong đợi interface `pay()`. Pattern phù hợp nhất để chuyển đổi interface:

A. Facade  
B. Adapter  
C. Singleton  
D. Builder

## Q13

Client cần một API đơn giản ở trước một subsystem phức tạp gồm nhiều class. Pattern phù hợp nhất:

A. Facade  
B. Proxy  
C. Flyweight  
D. Command

## Q14

Một object thay đổi trạng thái và cần thông báo cho nhiều subscriber mà không hard-code từng subscriber. Pattern phù hợp nhất:

A. Template Method  
B. Observer  
C. Factory Method  
D. Memento

## Q15

Artifact nào tập trung chủ yếu vào bố cục/cấu trúc màn hình, thường trước khi có tương tác hoàn chỉnh?

A. Wireframe  
B. Load Test  
C. Deployment Diagram  
D. Data Dictionary

## Q16

Trong Scrum, artifact chứa công việc được chọn cho Sprint cùng plan để đạt Sprint Goal là:

A. Product Backlog  
B. Sprint Backlog  
C. Increment  
D. Product Vision

## Q17

Practice nào gắn mạnh với XP — Extreme Programming?

A. Pair Programming  
B. Big Design Up Front bắt buộc  
C. Không bao giờ refactor  
D. Chỉ test sau release

## Q18

Client retry cùng một payment request sau timeout. Design concept nào trực tiếp giúp tránh thực hiện cùng side effect nhiều lần khi cùng request identity được gửi lại?

A. Idempotency  
B. Inheritance  
C. Compression  
D. Pagination

## Q19

Điểm yếu chính của point-to-point integration khi số lượng hệ thống tăng mạnh là:

A. Không dùng được JSON  
B. Số connection/dependency tăng khó quản lý  
C. Không thể dùng database  
D. Không thể có authentication

## Q20

UML diagram nào phù hợp nhất để biểu diễn software artifact/component được triển khai trên node/server nào?

A. Activity Diagram  
B. Deployment Diagram  
C. State Diagram  
D. Use Case Diagram

---

# 제2과목 — 소프트웨어 개발 — Software Development

## Q21

Data structure nào hoạt động theo LIFO?

A. Queue  
B. Stack  
C. Heap  
D. Graph

## Q22

Data structure nào hoạt động theo FIFO trong mô hình cơ bản?

A. Stack  
B. Queue  
C. Binary Search Tree  
D. Hash Function

## Q23

Traversal nào của BST với key phân biệt cho kết quả theo thứ tự tăng dần?

A. Preorder  
B. Inorder  
C. Postorder  
D. Level-order

## Q24

Trong graph không trọng số, thuật toán nền tảng tìm shortest path theo số cạnh từ một source là:

A. BFS  
B. DFS  
C. Prim  
D. Kruskal

## Q25

Worst-case time complexity điển hình của Quick Sort là:

A. O(1)  
B. O(log n)  
C. O(n log n)  
D. O(n²)

## Q26

Merge Sort có worst-case time complexity điển hình là:

A. O(n²)  
B. O(n log n)  
C. O(log n)  
D. O(1)

## Q27

Linear Probing trong hash table dễ gây:

A. Primary Clustering  
B. Dirty Read  
C. Dead Code  
D. Stack Overflow bắt buộc

## Q28

Trong Top-down Integration Testing, module cấp dưới chưa sẵn sàng thường được thay bằng:

A. Driver  
B. Stub  
C. Compiler  
D. Proxy Server

## Q29

Trong Bottom-up Integration Testing, component gọi phía trên chưa sẵn sàng thường được thay bằng:

A. Driver  
B. Stub  
C. Semaphore  
D. Index

## Q30

Technique nào thuộc Black-box Testing?

A. Statement Coverage  
B. Branch Coverage  
C. Boundary Value Analysis  
D. Path Coverage

## Q31

Metric nào kiểm tra các branch/decision outcomes trong white-box testing?

A. Boundary Coverage  
B. Branch Coverage  
C. Equivalence Partitioning  
D. Usability Coverage

## Q32

Control-flow graph có `E=12`, `N=10`, một connected component. Cyclomatic Complexity là:

A. 2  
B. 3  
C. 4  
D. 12

## Q33

Sau khi sửa bug trong module thanh toán, team chạy lại các test cũ để bảo đảm chức năng trước đó không bị phá. Đây là:

A. Regression Testing  
B. Smoke-free Testing  
C. Mutation bắt buộc  
D. Acceptance only

## Q34

Testing do một nhóm người dùng bên ngoài tổ chức thực hiện trước release rộng rãi thường gần nhất với:

A. Alpha Testing  
B. Beta Testing  
C. Unit Testing  
D. Static Analysis

## Q35

Baseline trong Configuration Management gần nhất với:

A. Một mốc cấu hình đã được xác lập/kiểm soát, thay đổi qua procedure  
B. Bất kỳ file tạm nào chưa commit  
C. Password mặc định  
D. CPU scheduling queue

## Q36

Version Control giúp giải quyết trực tiếp nhất vấn đề nào?

A. Theo dõi lịch sử thay đổi source/artifact và phối hợp phiên bản  
B. Tăng RAM vật lý  
C. Mã hóa toàn bộ network traffic  
D. Thay thế database transaction

## Q37

Mục đích của software packaging gần nhất với:

A. Chuẩn bị software, dependency, metadata/manual cần thiết để phân phối/cài đặt  
B. Chỉ nén source thành ZIP bất kể deployment  
C. Thay thế mọi test  
D. Xóa version information

## Q38

Metric nào đo số request/transaction được xử lý trong một đơn vị thời gian?

A. Throughput  
B. Response Time  
C. Latency percentile duy nhất  
D. Defect Density

## Q39

Nếu interface nhận JSON và cần kiểm tra field bắt buộc, type và format trước khi business logic chạy, đây gần nhất với:

A. Interface/Data Validation  
B. CPU Scheduling  
C. Deadlock Recovery  
D. RAID Rebuild

## Q40

Checksum/hash dùng trong quá trình phân phối package chủ yếu giúp phát hiện:

A. Package bị thay đổi/corrupt so với giá trị mong đợi  
B. User có quyền business nào  
C. CPU nào chạy process  
D. Transaction isolation level

---

# 제3과목 — 데이터베이스 구축 — Database Construction

## Q41

Một Super Key trở thành Candidate Key khi có thêm tính chất:

A. Minimality  
B. Luôn có hai column  
C. Luôn là foreign key  
D. Luôn là numeric

## Q42

Relational Algebra operation dùng để chọn các row thỏa predicate là:

A. Projection  
B. Selection  
C. Division  
D. Rename

## Q43

Operation dùng để lấy một số attribute/column trong relational algebra là:

A. Selection  
B. Projection  
C. Union  
D. Join

## Q44

Relation có key `(StudentId, CourseId)` và `StudentName` chỉ phụ thuộc `StudentId`. Đây là:

A. Partial Dependency  
B. Transitive Dependency  
C. Multivalued Dependency  
D. Join Dependency

## Q45

`EmpId → DeptId` và `DeptId → DeptName`; `EmpId` là key. `DeptName` phụ thuộc vào key qua `DeptId`. Đây là:

A. Partial Dependency  
B. Transitive Dependency  
C. Trivial Dependency  
D. No Dependency

## Q46

BCNF yêu cầu với mọi non-trivial FD `X → Y`:

A. X phải là superkey  
B. Y phải là foreign key  
C. X phải có đúng một attribute  
D. Y không được là prime attribute

## Q47

Index structure nào tự nhiên phù hợp với equality + range query vì giữ ordering theo key?

A. B+Tree  
B. Hash-only structure  
C. Stack  
D. FIFO Queue

## Q48

Thêm quá nhiều index vào table write-heavy có trade-off phổ biến nào?

A. Insert/Update/Delete tốn thêm chi phí duy trì index  
B. Mọi SELECT chắc chắn chậm hơn  
C. Transaction không còn ACID  
D. Foreign key tự biến mất

## Q49

Database View gần nhất với:

A. Một virtual relation/query abstraction dựa trên underlying data  
B. Một physical disk bắt buộc  
C. Một CPU register  
D. Một network route

## Q50

Statement nào là DDL điển hình?

A. CREATE TABLE  
B. SELECT  
C. COMMIT  
D. GRANT

## Q51

Muốn lọc group có `SUM(amount) > 1000` sau `GROUP BY customer_id`, clause phù hợp là:

A. WHERE  
B. HAVING  
C. FROM  
D. DISTINCT

## Q52

Trong `LEFT JOIN`, row bên trái không có match bên phải sẽ:

A. Bị loại luôn  
B. Vẫn được giữ, columns bên phải thường là NULL  
C. Tạo exception bắt buộc  
D. Biến thành INNER JOIN

## Q53

Constraint nào bảo đảm giá trị foreign key tham chiếu phù hợp tới key được phép ở relation cha, theo referential integrity?

A. FOREIGN KEY  
B. CHECKSUM  
C. INDEX-only  
D. VIEW-only

## Q54

ACID property nào bảo đảm một transaction hoặc hoàn thành toàn bộ hoặc không để lại một phần thay đổi đã commit?

A. Atomicity  
B. Consistency  
C. Isolation  
D. Durability

## Q55

T1 đọc một row hai lần. Giữa hai lần, T2 update row đó và commit, nên T1 thấy hai giá trị khác nhau. Đây là:

A. Dirty Read  
B. Non-repeatable Read  
C. Phantom Read  
D. Deadlock

## Q56

T1 chạy cùng một predicate query hai lần; lần hai xuất hiện thêm row mới do T2 insert và commit. Đây gần nhất với:

A. Phantom Read  
B. Lost Update  
C. Stack Overflow  
D. Paging

## Q57

Trong precedence graph của một schedule, nếu có cycle thì schedule đó:

A. Chắc chắn conflict-serializable  
B. Không conflict-serializable  
C. Luôn read-only  
D. Luôn deadlock

## Q58

Write-ahead logging — WAL — về ý tưởng yêu cầu điều gì trước khi data page chứa thay đổi được ghi durable theo recovery protocol?

A. Relevant log record phải được ghi theo rule WAL trước  
B. Xóa toàn bộ log  
C. Tắt transaction  
D. Reboot server

## Q59

Sau data migration, bước nào quan trọng để phát hiện mất hoặc biến đổi sai dữ liệu?

A. Validation/Reconciliation  
B. Chỉ đổi tên file  
C. Chỉ tăng CPU  
D. Chỉ thêm CSS

## Q60

`COUNT(column)` khác `COUNT(*)` ở điểm quan trọng nào?

A. `COUNT(column)` không đếm NULL của column đó  
B. `COUNT(*)` luôn trả 0  
C. `COUNT(column)` chỉ dùng với primary key  
D. Hai cái luôn giống nhau trong mọi query

---

# 제4과목 — 프로그래밍 언어 활용 — Programming Language Application

## Q61

Điểm khác biệt cơ bản thường gặp giữa process và thread là:

A. Thread trong cùng process thường chia sẻ address space/resources nhiều hơn  
B. Process luôn chia sẻ toàn bộ memory với process khác  
C. Thread không bao giờ được schedule  
D. Process không có state

## Q62

Semaphore khác mutex ở điểm khái quát nào?

A. Semaphore có thể biểu diễn nhiều permit bằng counter  
B. Mutex luôn có counter 100  
C. Semaphore chỉ dùng cho database index  
D. Hai khái niệm hoàn toàn không liên quan synchronization

## Q63

Impose một thứ tự toàn cục khi acquire resource và buộc mọi process tuân theo thứ tự đó nhắm phá Coffman condition nào?

A. Mutual Exclusion  
B. Hold and Wait  
C. Circular Wait  
D. No Preemption

## Q64

Ba process cùng arrive time 0: P1=5, P2=3, P3=2. FCFS theo thứ tự P1→P2→P3. Average waiting time là:

A. 2.33  
B. 4.33  
C. 5.00  
D. 7.67

## Q65

Cùng ba process P1=5, P2=3, P3=2, tất cả arrive time 0. Non-preemptive SJF order là:

A. P1→P2→P3  
B. P3→P2→P1  
C. P2→P1→P3  
D. P3→P1→P2

## Q66

Trong Round Robin, giảm time quantum quá nhỏ thường dẫn tới trade-off nào?

A. Context-switch overhead tăng  
B. Không còn preemption  
C. Mọi process chạy đến hết burst  
D. Không cần ready queue

## Q67

Page Fault xảy ra khi:

A. Process tham chiếu page chưa hiện diện trong physical memory và OS phải xử lý  
B. CPU instruction luôn sai syntax  
C. DNS không resolve được  
D. SQL không có GROUP BY

## Q68

LRU page replacement chọn victim theo:

A. Page ít được dùng gần đây nhất  
B. Page có địa chỉ nhỏ nhất bắt buộc  
C. Page vào frame đầu tiên bất kể usage  
D. Page random theo chuẩn

## Q69

Thrashing gần nhất với tình trạng:

A. Hệ thống dành quá nhiều thời gian paging do working set không phù hợp memory  
B. CPU không có instruction set  
C. Database không có primary key  
D. Network chỉ dùng UDP

## Q70

Trong mô hình TCP/IP/OSI, TCP thuộc layer gần nhất với:

A. Transport  
B. Network  
C. Data Link  
D. Physical

## Q71

So với UDP, TCP cung cấp rõ nhất:

A. Connection-oriented reliable ordered byte stream  
B. Broadcast bắt buộc  
C. Không có port  
D. Không có congestion control concept

## Q72

Một subnet IPv4 `/27` có bao nhiêu địa chỉ usable theo cách tính truyền thống network/broadcast?

A. 14  
B. 30  
C. 32  
D. 62

## Q73

Routing table có các route `/8`, `/16`, `/24` cùng match destination. Router theo longest-prefix match sẽ chọn:

A. /8  
B. /16  
C. /24  
D. Chọn random

## Q74

DNS chủ yếu dùng để:

A. Phân giải tên miền và các record liên quan sang thông tin như IP theo record type  
B. Mã hóa disk  
C. Lập lịch CPU  
D. Normalize database

## Q75

ARP trong IPv4 LAN truyền thống dùng để:

A. Ánh xạ IPv4 address tới link-layer MAC address trong local network context  
B. Tìm SQL index  
C. Tính critical path  
D. Hash password

## Q76

C code:

```c
int a[] = {10,20,30,40};
int *p = a + 1;
printf("%d", *(p + 2));
```

Output là:

A. 10  
B. 20  
C. 30  
D. 40

## Q77

C code:

```c
int x = 3;
int y = x++;
```

Ngay sau đó:

A. x=3, y=4  
B. x=4, y=3  
C. x=4, y=4  
D. x=3, y=3

## Q78

Java:

```java
A x = new B();
x.f();
```

Nếu `B` override instance method `f()` của `A`, method body nào thường được gọi qua dynamic dispatch?

A. Luôn A  
B. B  
C. Không method nào  
D. Compile error chỉ vì reference type A

## Q79

Trong Java, overloading thường được phân biệt bằng:

A. Parameter list/signature khác phù hợp rule ngôn ngữ  
B. Chỉ khác return type  
C. Chỉ khác tên class  
D. Chỉ khác comment

## Q80

Python:

```python
a = [1, 2]
b = a
b.append(3)
print(a)
```

Output là:

A. `[1, 2]`  
B. `[1, 2, 3]`  
C. `[3]`  
D. Error bắt buộc

---

# 제5과목 — 정보시스템 구축 관리 — Information System Construction Management

## Q81

Đặc điểm nào gần nhất với Waterfall model truyền thống?

A. Các phase theo trình tự tương đối rõ, change muộn thường tốn kém  
B. Không có requirement  
C. Không có test  
D. Luôn deploy mỗi ngày

## Q82

PERT expected time với O=4, M=7, P=16 là:

A. 7  
B. 8  
C. 9  
D. 16

## Q83

Project có Path A tổng 12 ngày và Path B tổng 9 ngày, không có constraint khác. Critical path là:

A. Path B  
B. Path A  
C. Cả hai luôn critical  
D. Không path nào

## Q84

4 disk × 2 TB chạy RAID 5. Usable capacity theo mô hình parity một disk tương đương là:

A. 2 TB  
B. 4 TB  
C. 6 TB  
D. 8 TB

## Q85

RAID 1 chủ yếu dùng:

A. Mirroring  
B. Striping không redundancy  
C. Distributed dual parity  
D. DNS replication

## Q86

Business nói “service phải phục hồi trong 30 phút”. Đây mô tả:

A. RPO  
B. RTO  
C. MTU  
D. TTL DNS

## Q87

Business nói “chấp nhận mất tối đa 5 phút dữ liệu”. Đây mô tả:

A. RTO  
B. RPO  
C. CPU quantum  
D. Fan-out

## Q88

Phát biểu nào đúng nhất?

A. RAID hoàn toàn thay thế backup  
B. Backup, replication và RAID bảo vệ các failure modes khác nhau  
C. Có RAID thì ransomware không thể phá data  
D. Có backup thì không cần restore test

## Q89

Trong cloud service model, IaaS cung cấp gần nhất:

A. Compute/network/storage infrastructure mà customer quản lý nhiều phần software stack hơn SaaS  
B. Chỉ một ứng dụng hoàn chỉnh không quản lý OS nào  
C. Chỉ source code repository  
D. Chỉ password manager

## Q90

Container khác full VM điển hình ở điểm:

A. Container thường chia sẻ host kernel thay vì mỗi instance có guest OS/kernel riêng như VM truyền thống  
B. Container không cần isolation  
C. VM không thể chạy application  
D. Container luôn mạnh hơn VM về security

## Q91

Firewall gần nhất với nhiệm vụ:

A. Kiểm soát network traffic theo policy/rule  
B. Normalize relation  
C. Compile Java  
D. Tính PERT

## Q92

IDS và IPS khác nhau khái quát ở điểm:

A. IDS thiên về detection/alert; IPS có thể nằm inline để block/prevent  
B. IDS là database index; IPS là SQL clause  
C. IPS không liên quan network/security  
D. Hai cái luôn giống hệt deployment

## Q93

Authentication và Authorization khác nhau ở đâu?

A. Authentication xác minh identity; Authorization quyết định quyền hành động  
B. Authentication quyết định quyền; Authorization chỉ hash password  
C. Hai khái niệm đồng nghĩa hoàn toàn  
D. Authorization chỉ dùng cho network routing

## Q94

Cryptographic hash function chủ yếu tạo:

A. Fixed-size digest từ input, dùng cho integrity-related purposes tùy protocol  
B. Reversible ciphertext bằng cùng key bắt buộc  
C. IP route  
D. CPU schedule

## Q95

Digital signature chủ yếu hỗ trợ combination nào?

A. Authenticity/integrity và non-repudiation theo scheme/context phù hợp  
B. Compression  
C. Database normalization  
D. Load balancing

## Q96

Mitigation trực tiếp nhất cho SQL Injection trong application code là:

A. Parameterized Query / Prepared Statement  
B. Chỉ đổi port database  
C. Chỉ nén response  
D. Chỉ thêm CSS validation phía client

## Q97

Mitigation quan trọng cho Stored/Reflected XSS khi render untrusted data là:

A. Context-appropriate output encoding/escaping  
B. RAID 1  
C. CPU affinity  
D. B+Tree index

## Q98

Principle of Least Privilege — 최소 권한 원칙 — nghĩa là:

A. Cấp tối thiểu quyền cần thiết cho task, trong phạm vi/thời gian phù hợp  
B. Mọi user đều admin  
C. Tắt logging  
D. Không cần authorization

## Q99

Configuration Management — 형상관리 — rộng hơn Version Control vì nó còn bao gồm:

A. Identification/baseline/change/status/audit của configuration items và release-related control  
B. Chỉ syntax highlighting  
C. Chỉ CPU scheduling  
D. Chỉ DNS cache

## Q100

Risk có probability thấp nhưng impact cực lớn. Cách đánh giá đúng nhất là:

A. Bỏ qua vì probability thấp  
B. Xem xét cả likelihood và impact, cùng exposure/context và mitigation  
C. Chỉ nhìn impact, không cần probability  
D. Chỉ nhìn số lượng developer

---

# Answer Key + Rationales

## Môn 1

**Q1 — C.** Performance threshold là quality constraint, không phải business function chính.  
**Q2 — B.** Validation hỏi sản phẩm/spec có đúng nhu cầu thực không; verification hỏi có xây đúng spec không.  
**Q3 — B.** Data Store biểu diễn nơi dữ liệu được giữ trong DFD.  
**Q4 — A.** Sequence Diagram tập trung order của messages theo thời gian.  
**Q5 — B.** Composition biểu diễn whole-part ownership/lifecycle mạnh.  
**Q6 — C.** Module independence thường hướng tới high cohesion, low coupling.  
**Q7 — D.** Chỉ truyền đúng dữ liệu cần dùng qua parameter là Data Coupling.  
**Q8 — A.** Truyền whole record/object nhưng chỉ dùng một phần là Stamp Coupling.  
**Q9 — A.** SRP = Single Responsibility Principle.  
**Q10 — B.** High-level service phụ thuộc abstraction `PaymentGateway`, phù hợp DIP.  
**Q11 — A.** Strategy encapsulates interchangeable algorithms/policies.  
**Q12 — B.** Adapter chuyển interface hiện có sang interface client mong đợi.  
**Q13 — A.** Facade cung cấp mặt tiền đơn giản cho subsystem phức tạp.  
**Q14 — B.** Observer phù hợp one-to-many notification.  
**Q15 — A.** Wireframe tập trung layout/structure hơn visual polish hoặc interaction hoàn chỉnh.  
**Q16 — B.** Sprint Backlog chứa selected work và plan để đạt Sprint Goal.  
**Q17 — A.** Pair Programming là practice tiêu biểu của XP.  
**Q18 — A.** Idempotency giúp same logical request không lặp side effect ngoài ý muốn.  
**Q19 — B.** Số connection/dependency tăng nhanh khiến point-to-point khó maintain.  
**Q20 — B.** Deployment Diagram biểu diễn mapping artifact/component lên deployment nodes.

**Môn 1 score:** `___ / 20` → `___ / 100`.

---

## Môn 2

**Q21 — B.** Stack là LIFO.  
**Q22 — B.** Queue cơ bản là FIFO.  
**Q23 — B.** Inorder traversal của BST distinct keys cho sorted order.  
**Q24 — A.** BFS khám phá theo layer nên cho shortest path theo số edge trong unweighted graph.  
**Q25 — D.** Quick Sort worst case điển hình O(n²).  
**Q26 — B.** Merge Sort worst-case O(n log n).  
**Q27 — A.** Linear probing dễ tạo primary clustering.  
**Q28 — B.** Top-down dùng stub thay module con chưa có.  
**Q29 — A.** Bottom-up dùng driver mô phỏng caller phía trên.  
**Q30 — C.** Boundary Value Analysis là black-box technique.  
**Q31 — B.** Branch Coverage đo các decision outcome/branches.  
**Q32 — C.** `12 - 10 + 2 = 4`.  
**Q33 — A.** Regression test kiểm tra thay đổi không phá behavior trước đó.  
**Q34 — B.** Beta thường do external users trong môi trường gần thực tế hơn alpha.  
**Q35 — A.** Baseline là cấu hình/mốc đã được formally established và controlled.  
**Q36 — A.** Version Control quản lý lịch sử, branch/version và collaboration trên artifacts.  
**Q37 — A.** Packaging chuẩn bị artifact/dependency/metadata/manual cần cho distribution/install.  
**Q38 — A.** Throughput = work completed per time unit.  
**Q39 — A.** Kiểm tra schema/type/required fields là interface/data validation.  
**Q40 — A.** Checksum/hash giúp phát hiện package khác expected content; authentication/authorization là vấn đề khác.

**Môn 2 score:** `___ / 20` → `___ / 100`.

---

## Môn 3

**Q41 — A.** Candidate key = minimal superkey.  
**Q42 — B.** Selection chọn rows theo predicate.  
**Q43 — B.** Projection chọn attributes/columns.  
**Q44 — A.** Non-key attribute phụ thuộc một phần composite key là partial dependency.  
**Q45 — B.** Key → non-key → non-key tạo transitive dependency.  
**Q46 — A.** BCNF yêu cầu determinant của mọi non-trivial FD là superkey.  
**Q47 — A.** B+Tree giữ ordering và hỗ trợ range scan tự nhiên.  
**Q48 — A.** Index phải được cập nhật khi writes thay đổi indexed keys/rows.  
**Q49 — A.** View là query abstraction/virtual relation, trừ materialized-view variant có storage riêng.  
**Q50 — A.** `CREATE TABLE` là DDL. `SELECT` là query/DML-style, `COMMIT` TCL, `GRANT` DCL theo phân loại truyền thống.  
**Q51 — B.** HAVING lọc group sau aggregate.  
**Q52 — B.** LEFT JOIN giữ rows phía trái và fill NULL cho unmatched right side.  
**Q53 — A.** FOREIGN KEY enforce referential constraint theo DBMS rule.  
**Q54 — A.** Atomicity = all-or-nothing transaction effect.  
**Q55 — B.** Cùng row đọc hai lần ra giá trị khác do committed update là non-repeatable read.  
**Q56 — A.** Predicate result có thêm/mất row do insert/delete concurrent là phantom.  
**Q57 — B.** Cycle trong precedence graph nghĩa không conflict-serializable.  
**Q58 — A.** WAL yêu cầu log record tương ứng được forced theo rule trước data page cần thiết cho recovery.  
**Q59 — A.** Migration phải có validation/reconciliation về count, constraint, sampled/full checks tùy criticality.  
**Q60 — A.** `COUNT(column)` bỏ qua NULL; `COUNT(*)` đếm rows.

**Môn 3 score:** `___ / 20` → `___ / 100`.

---

## Môn 4

**Q61 — A.** Threads cùng process thường share address space/resources nhiều hơn independent processes.  
**Q62 — A.** Semaphore có counter/permits; mutex thường mô hình ownership/exclusion một critical section.  
**Q63 — C.** Resource ordering phá circular wait.  
**Q64 — B.** Waiting: 0,5,8 → average `13/3 ≈ 4.33`.  
**Q65 — B.** SJF chọn burst ngắn: P3(2) → P2(3) → P1(5).  
**Q66 — A.** Quantum quá nhỏ tăng scheduling/context-switch overhead.  
**Q67 — A.** Page fault khi referenced page không resident và OS phải bring/resolve mapping.  
**Q68 — A.** LRU thay page least recently used.  
**Q69 — A.** Thrashing = paging activity quá mức, useful work giảm mạnh.  
**Q70 — A.** TCP là transport-layer protocol.  
**Q71 — A.** TCP cung cấp connection-oriented reliable ordered byte stream.  
**Q72 — B.** `/27` còn 5 host bits → 32 addresses, usable truyền thống 30.  
**Q73 — C.** Longest-prefix match chọn route cụ thể nhất `/24`.  
**Q74 — A.** DNS phân giải names/records, không phải routing/scheduling.  
**Q75 — A.** ARP dùng trong IPv4 local-link address resolution.  
**Q76 — D.** `p=a+1` trỏ 20; `p+2` trỏ index 3 = 40.  
**Q77 — B.** Post-increment trả old value cho assignment rồi tăng x: y=3, x=4.  
**Q78 — B.** Overridden instance method dispatch theo runtime object B.  
**Q79 — A.** Overloading dựa trên khác parameter signature; chỉ khác return type không đủ.  
**Q80 — B.** `a` và `b` alias cùng mutable list, append qua b làm a thấy `[1,2,3]`.

**Môn 4 score:** `___ / 20` → `___ / 100`.

---

## Môn 5

**Q81 — A.** Waterfall truyền thống có phase ordering rõ; change late thường có rework cost cao.  
**Q82 — B.** `(4 + 4×7 + 16)/6 = 48/6 = 8`.  
**Q83 — B.** Path dài 12 quyết định duration trong network đơn giản này.  
**Q84 — C.** RAID5 usable `(4-1)×2 = 6 TB`.  
**Q85 — A.** RAID1 là mirroring.  
**Q86 — B.** RTO = objective cho thời gian phục hồi service.  
**Q87 — B.** RPO = objective cho mức data loss theo thời gian.  
**Q88 — B.** RAID, replication và backup giải quyết failure modes khác nhau và không thay thế hoàn toàn nhau.  
**Q89 — A.** IaaS cung cấp infrastructure primitives; customer kiểm soát nhiều layer phía trên hơn SaaS.  
**Q90 — A.** Containers thường share host kernel; VMs truyền thống có guest OS/kernel riêng.  
**Q91 — A.** Firewall enforce network traffic policy.  
**Q92 — A.** IDS thiên detection/alert; IPS thường inline/prevent/block tùy deployment.  
**Q93 — A.** Authentication = who are you; Authorization = what may you do.  
**Q94 — A.** Hash tạo digest fixed-size; không phải reversible encryption.  
**Q95 — A.** Digital signatures hỗ trợ integrity/authenticity và non-repudiation assumptions theo scheme/context.  
**Q96 — A.** Parameterized query tách code/SQL structure khỏi untrusted values, mitigation cốt lõi cho SQL injection.  
**Q97 — A.** Output encoding theo context là defense cốt lõi khi render untrusted content; CSP có thể là layer bổ sung.  
**Q98 — A.** Least privilege cấp đúng mức quyền cần thiết, không mặc định admin.  
**Q99 — A.** Configuration Management bao gồm identification, baseline, change/status accounting, audit/release control; VCS chỉ là một phần tooling/process.  
**Q100 — B.** Risk assessment phải xét likelihood + impact + context/exposure/controls; low probability không tự động nghĩa bỏ qua.

**Môn 5 score:** `___ / 20` → `___ / 100`.

---

# Score Sheet

| Môn | Correct / 20 | Score / 100 | ≥ 40? |
|---|---:|---:|---|
| 소프트웨어 설계 | ___ | ___ | ___ |
| 소프트웨어 개발 | ___ | ___ | ___ |
| 데이터베이스 구축 | ___ | ___ | ___ |
| 프로그래밍 언어 활용 | ___ | ___ | ___ |
| 정보시스템 구축 관리 | ___ | ___ | ___ |

```text
Total correct = _____ / 100
Average score = _____ / 100
```

Trong mô hình này, vì năm môn có cùng 20 câu và cùng weight, `60/100` total correct tương ứng average 60, **nhưng vẫn phải đồng thời đạt tối thiểu 8/20 ở từng môn**.

---

# Error Audit

Với mỗi câu sai, ghi một mã duy nhất đầu tiên:

```text
COV = coverage hole
CON = confusion pair
PRO = procedural error
TERM = Korean/English term recognition
READ = careless reading
```

Sau đó ghi concept gốc phải sửa. Ví dụ:

```text
Q55 — CON — non-repeatable read vs phantom read
Q64 — PRO — FCFS waiting-time timeline
Q72 — PRO — /27 host-bit calculation
Q96 — COV — parameterized query
```

Không học lại nguyên 100 câu. Học lại **cơ chế tạo ra lỗi**.

---

# Definition of Done

Mock này chưa “xong” khi chỉ đạt 60 câu đúng một lần. Xong khi:

1. không môn nào dưới 8/20;
2. mọi câu procedural sai đều có thể làm lại bằng bước trung gian;
3. mọi confusion pair sai đều giải thích được ranh giới bằng lời của mình;
4. mọi term-recognition error đều nhận ra cả Korean + English concept;
5. khi làm lại sau một khoảng cách, không còn phụ thuộc vào việc nhớ vị trí đáp án A/B/C/D.
