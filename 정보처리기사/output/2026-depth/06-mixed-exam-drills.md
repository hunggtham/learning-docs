# 정보처리기사 필기 2026 — Mixed Exam Drills

> Đây là bộ câu hỏi **tự viết mới**, không sao chép 기출. Mục tiêu là luyện chuyển context nhanh giữa 5 môn và phát hiện lỗ hổng thật sự. Làm toàn bộ câu trước, sau đó mới xem đáp án.

## Cách làm

Mỗi câu nên trả lời trong khoảng 60–90 giây. Với câu tính/code, ghi bước suy luận ra giấy. Sau khi chấm, phân loại lỗi:

- `coverage hole`: chưa học chủ đề;
- `confusion pair`: biết cả hai nhưng nhầm ranh giới;
- `procedural error`: hiểu lý thuyết nhưng tính/trace sai;
- `term recognition`: không nhận ra thuật ngữ Hàn;
- `careless reading`: đọc thiếu điều kiện.

---

# Phần A — 소프트웨어 설계

## Q1

Một requirement ghi: “Người dùng có thể khóa tài khoản và thao tác phải hoàn thành trong 1 giây.” Phân loại đúng nhất là gì?

A. Cả hai đều functional requirement  
B. Khóa tài khoản là functional, 1 giây là non-functional  
C. Khóa tài khoản là non-functional, 1 giây là functional  
D. Cả hai đều non-functional

## Q2

Muốn thể hiện thứ tự message giữa `Controller`, `Service`, `Repository` theo thời gian, diagram phù hợp nhất là:

A. Use Case Diagram  
B. State Diagram  
C. Sequence Diagram  
D. Deployment Diagram

## Q3

`Order` sở hữu `OrderLine`; nếu Order bị xóa thì OrderLine không còn ý nghĩa tồn tại độc lập. Quan hệ phù hợp nhất là:

A. Dependency  
B. Aggregation  
C. Composition  
D. Generalization

## Q4

Module A truyền toàn bộ object `Customer` sang B nhưng B chỉ cần `customerId`. Đây gần nhất với:

A. Data coupling  
B. Stamp coupling  
C. Content coupling  
D. Common coupling

## Q5

Một hệ thống cần thay nhiều thuật toán tính discount tại runtime nhưng state nội bộ của object không tự quyết định algorithm. Pattern phù hợp nhất:

A. State  
B. Strategy  
C. Observer  
D. Singleton

## Q6

Một subsystem phức tạp có nhiều class nhưng client chỉ cần một API đơn giản ở phía trước. Pattern phù hợp nhất:

A. Adapter  
B. Decorator  
C. Facade  
D. Prototype

## Q7

Trong Scrum, artifact chứa phần việc được chọn cho Sprint cùng plan để đạt Sprint Goal là:

A. Product Backlog  
B. Sprint Backlog  
C. Increment  
D. Burndown Chart

## Q8

Point-to-Point integration bắt đầu gây khó quản lý chủ yếu khi:

A. Chỉ có một hệ thống duy nhất  
B. Số lượng system và connection tăng mạnh  
C. Không có database  
D. Dùng JSON thay XML

---

# Phần B — 소프트웨어 개발

## Q9

Traversal nào của BST với key phân biệt cho kết quả tăng dần?

A. Preorder  
B. Inorder  
C. Postorder  
D. Level-order

## Q10

Trong graph không trọng số, thuật toán nền tảng để tìm shortest path theo số cạnh từ một source là:

A. DFS  
B. BFS  
C. Prim  
D. Kruskal

## Q11

Quick Sort có complexity worst-case điển hình là:

A. O(1)  
B. O(log n)  
C. O(n log n)  
D. O(n²)

## Q12

Linear Probing trong hash table dễ gặp hiện tượng:

A. Deadlock  
B. Primary clustering  
C. Phantom read  
D. Starvation

## Q13

Trong Top-down Integration Test, module con chưa hoàn thành thường được thay bằng:

A. Driver  
B. Stub  
C. Oracle  
D. Harness

## Q14

Technique nào thuộc Black-box Testing?

A. Statement Coverage  
B. Branch Coverage  
C. Boundary Value Analysis  
D. Path Coverage

## Q15

`V(G) = E - N + 2` trong control flow graph một component dùng để tính:

A. Function Point  
B. Cyclomatic Complexity  
C. Halstead Volume  
D. Response Time

## Q16

Metric nào đo số request/transaction xử lý trong một đơn vị thời gian?

A. Response Time  
B. Latency  
C. Throughput  
D. Availability

---

# Phần C — 데이터베이스 구축

## Q17

Một Super Key trở thành Candidate Key khi thêm điều kiện nào?

A. Có foreign key  
B. Minimality  
C. Có ít nhất hai attribute  
D. Không chứa NULL ở mọi column

## Q18

Relational algebra operation chọn một số row theo predicate là:

A. Projection  
B. Selection  
C. Division  
D. Cartesian Product

## Q19

Relation có key `(StudentId, CourseId)`, nhưng `StudentName` chỉ phụ thuộc `StudentId`. Đây là:

A. Transitive dependency  
B. Partial dependency  
C. Multivalued dependency  
D. Join dependency

## Q20

BCNF yêu cầu điều gì với non-trivial functional dependency `X → Y`?

A. Y phải là foreign key  
B. X phải là superkey  
C. X phải là primary key duy nhất  
D. Y phải là non-prime attribute

## Q21

Query thường xuyên dùng range condition `created_at BETWEEN ...`. Index nào tự nhiên hơn?

A. Hash index  
B. B+Tree index  
C. Bitmap luôn luôn tốt hơn  
D. Không index nào hỗ trợ range

## Q22

Điều kiện `AVG(salary) > 5000` khi dùng `GROUP BY department_id` nên đặt ở:

A. WHERE  
B. HAVING  
C. ORDER BY  
D. VALUES

## Q23

T1 đọc một row hai lần. Giữa hai lần, T2 update row đó và commit. T1 thấy hai value khác nhau. Đây là:

A. Dirty Read  
B. Non-repeatable Read  
C. Phantom Read  
D. Lost Update

## Q24

Trong recovery, thao tác áp lại thay đổi của transaction đã commit nhưng chưa phản ánh đầy đủ trên disk là:

A. UNDO  
B. REDO  
C. ROLLBACK SAVEPOINT  
D. GRANT

---

# Phần D — 프로그래밍 언어 활용

## Q25

Trong C:

```c
int x = 3;
int *p = &x;
*p = *p + 2;
```

Giá trị cuối của `x` là:

A. 2  
B. 3  
C. 5  
D. Không xác định

## Q26

Trong Java:

```java
Parent p = new Child();
p.run();
```

Nếu `Child` override `run()`, method nào chạy?

A. Parent.run() luôn luôn  
B. Child.run() qua dynamic dispatch  
C. Compile error  
D. Tùy field của Parent

## Q27

Trong Python:

```python
a = [1, 2]
b = a
b.append(3)
```

`a` trở thành:

A. `[1, 2]`  
B. `[1, 2, 3]`  
C. `None`  
D. Error

## Q28

Scheduling nào là phiên bản preemptive của SJF?

A. FCFS  
B. SRTF  
C. HRN  
D. Round Robin

## Q29

Belady's Anomaly gắn nổi tiếng với page replacement nào?

A. Optimal  
B. LRU  
C. FIFO  
D. Working Set

## Q30

Một process đang chờ dữ liệu từ disk I/O thường ở state:

A. Ready  
B. Running  
C. Blocked/Waiting  
D. New

## Q31

Prefix IPv4 `/26` có tổng số address trong subnet là:

A. 16  
B. 32  
C. 64  
D. 128

## Q32

Thiết bị forward frame dựa MAC address trong LAN điển hình là:

A. Router  
B. Switch  
C. DNS Server  
D. Modem luôn luôn

---

# Phần E — 정보시스템 구축 관리

## Q33

Trong PERT, O=2, M=5, P=14. Expected time là:

A. 5  
B. 6  
C. 7  
D. 8

## Q34

Critical Path trong network project cơ bản là:

A. Path có ít activity nhất  
B. Path có nhiều activity nhất  
C. Path có tổng duration dài nhất  
D. Path có cost thấp nhất

## Q35

RAID nào dùng dual parity và có thể chịu hai disk failure trong mô hình chuẩn?

A. RAID 0  
B. RAID 1  
C. RAID 5  
D. RAID 6

## Q36

RPO trả lời câu hỏi nào?

A. Service được phép down bao lâu?  
B. Chấp nhận mất tối đa bao nhiêu dữ liệu tính theo thời gian?  
C. Bao lâu phải đổi password?  
D. Bao nhiêu server cần chạy?

## Q37

Defense chính chống SQL Injection là:

A. Chỉ đổi tên table  
B. Parameterized query / prepared statement  
C. Chỉ dùng HTTPS  
D. Chỉ encode HTML output

## Q38

Một comment độc hại được lưu DB rồi render cho mọi user, chạy JavaScript trong browser. Đây gần nhất là:

A. Stored XSS  
B. CSRF  
C. SQL Injection  
D. Buffer Overflow

## Q39

Access control gán permission cho Role, sau đó gán user vào Role là:

A. DAC  
B. MAC  
C. RBAC  
D. ABAC bắt buộc

## Q40

System dùng firewall để lọc network traffic, còn thiết bị inline phân tích traffic và chủ động block attack là:

A. IDS  
B. IPS  
C. DNS  
D. NTP

---

# Đáp án và giải thích

## A — Software Design

**Q1: B.** Capability “khóa tài khoản” là functional; giới hạn 1 giây là performance constraint nên non-functional.

**Q2: C.** Sequence Diagram mô tả lifeline/message theo thứ tự thời gian.

**Q3: C.** Composition dùng khi part phụ thuộc vòng đời whole.

**Q4: B.** Truyền cả structure/object khi callee chỉ cần một phần là Stamp Coupling; Data Coupling sẽ truyền đúng data cần thiết.

**Q5: B.** Strategy thay algorithm có thể chọn/thay runtime. State phù hợp khi behavior đổi do internal state.

**Q6: C.** Facade tạo interface đơn giản phía trước subsystem phức tạp.

**Q7: B.** Sprint Backlog chứa selected Product Backlog Items và plan cho Sprint.

**Q8: B.** Với N system, số direct connection có thể tăng nhanh và coupling/maintenance trở nên phức tạp.

## B — Software Development

**Q9: B.** Inorder của BST cho key tăng dần nếu key distinct và ordering chuẩn.

**Q10: B.** BFS đi theo layer nên tìm shortest path theo số cạnh trong unweighted graph.

**Q11: D.** Quick Sort average thường O(n log n), worst O(n²) nếu partition rất lệch.

**Q12: B.** Linear Probing tạo cluster liên tiếp gọi là primary clustering.

**Q13: B.** Top-down cần Stub thay module con; Bottom-up dùng Driver thay caller cấp trên.

**Q14: C.** Boundary Value Analysis là black-box technique dựa input domain/specification.

**Q15: B.** Đây là công thức McCabe Cyclomatic Complexity với một connected component.

**Q16: C.** Throughput đo lượng work xử lý trên đơn vị thời gian.

## C — Database

**Q17: B.** Candidate Key là Super Key minimal: bỏ bất kỳ attribute nào cũng mất uniqueness.

**Q18: B.** Selection chọn row; Projection chọn column.

**Q19: B.** `StudentName` phụ thuộc chỉ một phần composite key nên là partial dependency.

**Q20: B.** BCNF yêu cầu determinant X của mọi non-trivial FD phải là superkey.

**Q21: B.** B+Tree giữ ordering và hỗ trợ range scan tự nhiên; hash phù hợp equality hơn.

**Q22: B.** Aggregate condition sau grouping đặt ở HAVING.

**Q23: B.** Cùng row đọc lại thấy value khác sau committed update là Non-repeatable Read.

**Q24: B.** REDO áp lại committed change; UNDO đảo uncommitted change.

## D — Programming Language / OS / Network

**Q25: C.** `p` trỏ x; dereference rồi cộng 2 làm x từ 3 thành 5.

**Q26: B.** Overridden instance method được chọn theo actual object qua dynamic dispatch.

**Q27: B.** `a` và `b` bind cùng list; `append` mutate list chung.

**Q28: B.** Shortest Remaining Time First là preemptive SJF.

**Q29: C.** FIFO có thể xuất hiện Belady's Anomaly.

**Q30: C.** Chờ I/O/event là Blocked/Waiting, không phải Ready.

**Q31: C.** `/26` còn 6 bit host, tổng `2^6 = 64` address.

**Q32: B.** Switch L2 forward frame theo MAC table; router route packet theo IP.

## E — Information System Management

**Q33: B.** `(2 + 4×5 + 14)/6 = 36/6 = 6`.

**Q34: C.** Critical Path là path có tổng duration dài nhất và quyết định project duration tối thiểu trong model cơ bản.

**Q35: D.** RAID 6 dùng dual parity và chịu hai disk failure theo model chuẩn.

**Q36: B.** RPO là mức mất data tối đa chấp nhận được theo thời gian; RTO là downtime/recovery time objective.

**Q37: B.** Parameter binding tách query structure khỏi user data và là defense chính chống SQL Injection.

**Q38: A.** Payload được lưu rồi phát cho user khác là Stored XSS.

**Q39: C.** Permission → Role → User là Role-Based Access Control.

**Q40: B.** IDS chủ yếu detect/alert; IPS hoạt động inline để block/prevent theo policy/detection.

---

# Cách đọc kết quả

## 36–40 đúng

Coverage cơ bản khá ổn. Không dừng ở đây: chuyển sang đề timed và tập trung câu sai hiếm/chi tiết.

## 30–35 đúng

Có nền nhưng vẫn còn nhiều confusion/procedural hole. Lọc các câu sai theo môn và quay lại deep-dive tương ứng.

## 24–29 đúng

Chưa an toàn vì trung bình lý thuyết gần vùng pass nhưng chỉ cần một môn yếu là có nguy cơ 과락. Ưu tiên môn có tỷ lệ đúng thấp nhất.

## Dưới 24 đúng

Không nên học bằng đề ngẫu nhiên tiếp. Quay lại Master Guide + 5 deep-dive, lấp coverage trước rồi mới tăng số lượng mock test.

## Per-subject rule

Mỗi môn trong bộ này có 8 câu. Nếu một môn đúng dưới 5/8, xem môn đó là **risk area** dù tổng điểm cao. Đây là proxy luyện tập, không phải quy đổi trực tiếp sang điểm Q-Net, nhưng giúp tránh việc điểm mạnh che lấp một môn yếu.
