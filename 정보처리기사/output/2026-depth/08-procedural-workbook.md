# 정보처리기사 필기 2026 — Procedural Workbook

> Đây là workbook cho các dạng bài **không thể học chỉ bằng cách đọc**. Mỗi drill buộc phải viết tay các bước trung gian. Nếu nhìn đáp án rồi thấy “hiểu” nhưng không tự làm lại được, chưa tính là hoàn thành.
>
> Các bài đều được viết mới, dùng để luyện cơ chế chứ không sao chép 기출.

---

## 0. Cách dùng

Mỗi drill làm theo ba vòng.

**Vòng 1 — Closed book:** tự giải, ghi toàn bộ state trung gian.  
**Vòng 2 — Error classification:** nếu sai, đánh dấu `concept`, `procedure`, `arithmetic`, `term`, hoặc `careless`.  
**Vòng 3 — Reproduction:** sau ít nhất một lần chuyển sang bài khác, quay lại làm từ đầu mà không nhìn solution.

Mục tiêu không phải nhớ đáp số. Mục tiêu là tạo một procedure ổn định có thể dùng khi đề thay số liệu.

---

# Part A — 소프트웨어 설계 / 소프트웨어 개발

## Drill 1 — Cyclomatic Complexity

Cho control-flow graph có `N = 8` node và `E = 10` edge, một connected component.

### Tự giải

Tính Cyclomatic Complexity — 순환 복잡도 — bằng công thức:

```text
V(G) = E - N + 2P
```

với `P = 1`.

### Solution

```text
V(G) = 10 - 8 + 2 = 4
```

Nghĩa là graph có 4 independent paths trong basis-path interpretation. Đây không có nghĩa chỉ cần đúng 4 test case là “test hoàn toàn mọi behavior”; nó chỉ cho một structural testing measure liên quan independent path.

### Bẫy

Nếu graph có nhiều connected component, phải dùng đúng `P`, không mặc định luôn bằng 1.

---

## Drill 2 — Stack và postfix expression

Tính biểu thức postfix:

```text
5 2 3 * + 8 4 / -
```

### Procedure

Đọc từ trái sang phải.

1. gặp operand → push;
2. gặp operator → pop operand phải trước, rồi operand trái;
3. tính và push result.

### Trace

```text
5       → [5]
2       → [5, 2]
3       → [5, 2, 3]
*       → 2*3 = 6      → [5, 6]
+       → 5+6 = 11     → [11]
8       → [11, 8]
4       → [11, 8, 4]
/       → 8/4 = 2      → [11, 2]
-       → 11-2 = 9     → [9]
```

**Đáp án: 9.**

### Bẫy

Với `-` và `/`, thứ tự pop rất quan trọng. Operand pop đầu tiên là bên phải.

---

## Drill 3 — BFS và DFS

Graph vô hướng có adjacency theo đúng thứ tự sau:

```text
A: B, C
B: A, D, E
C: A, F
D: B
E: B, F
F: C, E
```

Bắt đầu tại A. Khi có nhiều neighbor, đi theo thứ tự liệt kê.

### BFS

Queue trace:

```text
visit A; queue [B, C]
visit B; enqueue D,E → [C, D, E]
visit C; enqueue F   → [D, E, F]
visit D              → [E, F]
visit E              → [F]
visit F              → []
```

**BFS order: A, B, C, D, E, F.**

### DFS

Nếu dùng recursive DFS theo thứ tự adjacency:

```text
A → B → D → back → E → F → C
```

**DFS order: A, B, D, E, F, C.**

### Bản chất

BFS dùng frontier theo FIFO nên khám phá theo “layer” số cạnh. Với graph không trọng số, đây là nền tảng shortest path theo số edge. DFS đi sâu trước và phù hợp nhiều bài connectivity, cycle, topological-style reasoning nhưng không tự bảo đảm shortest path unweighted.

---

## Drill 4 — Hash table với Linear Probing

Hash table size 7, hash function:

```text
h(k) = k mod 7
```

Insert theo thứ tự `10, 17, 24, 11` bằng Linear Probing.

### Trace

```text
10 mod 7 = 3 → slot 3 = 10
17 mod 7 = 3 → 3 occupied → slot 4 = 17
24 mod 7 = 3 → 3,4 occupied → slot 5 = 24
11 mod 7 = 4 → 4,5 occupied → slot 6 = 11
```

Final table:

```text
0: -
1: -
2: -
3: 10
4: 17
5: 24
6: 11
```

### Bản chất

Linear probing có thể tạo **Primary Clustering — 1차 군집화**: một cluster liên tục càng dài thì key mới hash vào gần đó càng dễ kéo cluster dài thêm.

---

## Drill 5 — Binary Search

Sorted array:

```text
[3, 8, 12, 19, 23, 31, 44, 57, 62]
```

Tìm 31 bằng binary search với index 0-based.

### Trace

```text
low=0 high=8 mid=4 → a[4]=23 < 31 → low=5
low=5 high=8 mid=6 → a[6]=44 > 31 → high=5
low=5 high=5 mid=5 → a[5]=31 → found
```

### Bản chất

Binary Search cần search space có ordering phù hợp. O(log n) ở đây đến từ việc mỗi comparison loại bỏ khoảng một nửa candidate range.

---

# Part B — 데이터베이스 구축

## Drill 6 — Candidate Key từ Functional Dependency

Relation:

```text
R(A, B, C, D)
```

Functional dependencies:

```text
A → B
B → C
AC → D
```

Tìm candidate key.

### Closure reasoning

Bắt đầu `A+`:

```text
A → B
B → C
=> A+ = {A, B, C}
```

Có A và C nên dùng `AC → D`:

```text
A+ = {A, B, C, D}
```

Vậy A xác định toàn bộ relation. Không thể bỏ gì khỏi A vì chỉ có một attribute.

**Candidate key: A.**

### Bẫy

FD `AC → D` không có nghĩa key bắt buộc là `AC`. Vì `A → B → C`, A đã suy ra C trước khi áp dụng dependency đó.

---

## Drill 7 — 2NF và Partial Dependency

Relation:

```text
Enrollment(StudentId, CourseId, StudentName, CourseName, Grade)
```

Candidate key là `(StudentId, CourseId)`.

Dependencies:

```text
StudentId → StudentName
CourseId  → CourseName
(StudentId, CourseId) → Grade
```

### Phân tích

`StudentName` phụ thuộc chỉ một phần của composite key: `StudentId`.  
`CourseName` phụ thuộc chỉ `CourseId`.

Đây là **부분 함수 종속 — partial functional dependency**, vi phạm 2NF.

### Decompose

```text
Student(StudentId, StudentName)
Course(CourseId, CourseName)
Enrollment(StudentId, CourseId, Grade)
```

### Bản chất

2NF nhắm tới partial dependency của non-prime attribute vào một phần candidate key. Nếu key chỉ có một attribute, partial dependency kiểu này không tồn tại.

---

## Drill 8 — 3NF và Transitive Dependency

Relation:

```text
Employee(EmpId, DeptId, DeptName)
```

Dependencies:

```text
EmpId  → DeptId
DeptId → DeptName
```

`EmpId` là key.

### Phân tích

```text
EmpId → DeptId → DeptName
```

`DeptName` phụ thuộc transitive vào key qua `DeptId`. Đây là **이행적 함수 종속 — transitive functional dependency**.

Decompose:

```text
Employee(EmpId, DeptId)
Department(DeptId, DeptName)
```

### Bẫy

Không phải cứ relation có foreign key là vi phạm 3NF. Vấn đề là dependency giữa non-key attributes theo điều kiện chuẩn hóa.

---

## Drill 9 — GROUP BY, WHERE và HAVING

Table `orders(customer_id, amount, status)`.

Yêu cầu: chỉ tính các order `PAID`, group theo customer, lấy customer có tổng amount > 1,000.

### SQL

```sql
SELECT customer_id, SUM(amount) AS total_amount
FROM orders
WHERE status = 'PAID'
GROUP BY customer_id
HAVING SUM(amount) > 1000;
```

### Cơ chế

`WHERE` lọc row trước grouping. `GROUP BY` tạo group. Aggregate chạy trên group. `HAVING` lọc group sau aggregate.

### Bẫy

Đừng dùng `WHERE SUM(amount) > 1000` vì aggregate value chưa tồn tại ở phase logic đó.

---

## Drill 10 — LEFT JOIN và NULL

Tables:

```text
Customer
id | name
1  | A
2  | B
3  | C

Order
id | customer_id
10 | 1
11 | 1
12 | 3
```

Query:

```sql
SELECT c.id, COUNT(o.id)
FROM Customer c
LEFT JOIN Order o ON o.customer_id = c.id
GROUP BY c.id;
```

### Result

```text
1 → 2
2 → 0
3 → 1
```

### Vì sao B vẫn xuất hiện?

LEFT JOIN giữ toàn bộ row bên trái. Với customer 2, columns bên Order trở thành NULL. `COUNT(o.id)` không đếm NULL nên result là 0.

### Bẫy

`COUNT(*)` ở group của customer 2 sẽ đếm preserved row và có thể cho 1, khác `COUNT(o.id)`.

---

## Drill 11 — Conflict Serializability

Schedule:

```text
T1: R(X)
T2: R(X)
T1: W(X)
T2: W(X)
```

### Precedence graph

Conflicts trên X:

- `R1(X)` trước `W2(X)` → edge `T1 → T2`
- `R2(X)` trước `W1(X)` → edge `T2 → T1`
- `W1(X)` trước `W2(X)` → edge `T1 → T2`

Graph có cycle:

```text
T1 → T2 → T1
```

**Schedule không conflict-serializable.**

### Procedure chung

1. chỉ xét operation khác transaction trên cùng data item;
2. ít nhất một operation phải là write;
3. thêm edge theo thứ tự xuất hiện;
4. graph acyclic → conflict-serializable; có cycle → không.

---

## Drill 12 — Isolation anomaly

T1 đọc balance = 100. T2 update balance = 50 và commit. T1 đọc lại cùng row và thấy 50.

### Nhận diện

Đây là **Non-repeatable Read — 반복 불가능 읽기**: cùng một row, cùng transaction, hai lần đọc cho value khác do transaction khác đã commit update.

Nếu T1 chạy cùng predicate `WHERE amount > 1000` và lần hai xuất hiện thêm row mới do T2 insert, đó gần với **Phantom Read — 팬텀 리드**.

---

# Part C — 프로그래밍 언어 활용 / OS / Network

## Drill 13 — FCFS Scheduling

Processes cùng arrive time 0:

| Process | Burst |
|---|---:|
| P1 | 5 |
| P2 | 3 |
| P3 | 2 |

FCFS order: P1 → P2 → P3.

### Waiting time

```text
P1 = 0
P2 = 5
P3 = 5 + 3 = 8
```

Average waiting time:

```text
(0 + 5 + 8) / 3 = 13/3 ≈ 4.33
```

### Turnaround time

```text
P1 = 5
P2 = 8
P3 = 10
```

Average turnaround:

```text
(5 + 8 + 10) / 3 = 23/3 ≈ 7.67
```

---

## Drill 14 — SJF Non-preemptive

Cùng processes trên, tất cả arrive time 0.

SJF order:

```text
P3(2) → P2(3) → P1(5)
```

Waiting:

```text
P3 = 0
P2 = 2
P1 = 2 + 3 = 5
```

Average waiting:

```text
(0 + 2 + 5) / 3 = 7/3 ≈ 2.33
```

### Bản chất

SJF giảm average waiting trong benchmark khi burst time biết trước, nhưng practical system thường không biết chính xác future CPU burst và có starvation risk với long jobs nếu short jobs liên tục đến.

---

## Drill 15 — Round Robin

Processes đều arrive 0:

```text
P1 burst 5
P2 burst 3
P3 burst 1
Quantum = 2
```

### Trace

```text
0-2   P1, remaining 3
2-4   P2, remaining 1
4-5   P3, done
5-7   P1, remaining 1
7-8   P2, done
8-9   P1, done
```

Completion time:

```text
P3 = 5
P2 = 8
P1 = 9
```

Vì arrive time = 0, turnaround = completion.

Waiting = turnaround - burst:

```text
P1 = 9 - 5 = 4
P2 = 8 - 3 = 5
P3 = 5 - 1 = 4
```

Average waiting:

```text
(4 + 5 + 4) / 3 = 13/3 ≈ 4.33
```

---

## Drill 16 — FIFO Page Replacement

3 frame, reference string:

```text
1 2 3 1 4 5
```

### Trace

```text
1 → [1,-,-] fault
2 → [1,2,-] fault
3 → [1,2,3] fault
1 → [1,2,3] hit
4 → [4,2,3] fault   // replace oldest page 1
5 → [4,5,3] fault   // replace oldest page 2
```

**Page faults = 5.**

FIFO chỉ quan tâm arrival order vào frame, không quan tâm page vừa được dùng lại gần đây.

---

## Drill 17 — LRU Page Replacement

Cùng 3 frame và reference:

```text
1 2 3 1 4 5
```

### Trace reasoning

Sau `1 2 3`, cả ba ở memory. Reference `1` làm 1 trở thành recently used.

Khi `4` tới, least recently used là 2 → replace 2.

State: `{1,3,4}`.

Khi `5` tới, among 1,3,4 thì 3 là least recently used → replace 3.

**Page faults cũng = 5 trong chuỗi này**, dù victim khác FIFO. Đừng suy rằng LRU luôn cho ít fault hơn trên mọi short reference string; policy khác nhau có thể tình cờ cùng count.

---

## Drill 18 — IPv4 Subnetting /27

Network:

```text
192.168.10.0/27
```

### Step 1 — host bits

`/27` nghĩa 27 network bits, còn 5 host bits.

Total addresses:

```text
2^5 = 32
```

Traditional usable host addresses:

```text
32 - 2 = 30
```

### Step 2 — block size

Mask:

```text
255.255.255.224
```

Block size ở octet cuối:

```text
256 - 224 = 32
```

Subnet ranges bắt đầu 0, 32, 64, 96, ...

Với `192.168.10.0/27`:

```text
Network   = 192.168.10.0
First host= 192.168.10.1
Last host = 192.168.10.30
Broadcast = 192.168.10.31
```

---

## Drill 19 — Xác định subnet của host

Host:

```text
192.168.10.77/27
```

Block size = 32. Các boundary:

```text
0, 32, 64, 96, ...
```

77 nằm trong block 64–95.

```text
Network   = 192.168.10.64
Broadcast = 192.168.10.95
Usable    = 192.168.10.65 ~ 192.168.10.94
```

---

## Drill 20 — Longest Prefix Match

Routing table:

```text
10.0.0.0/8      → A
10.10.0.0/16    → B
10.10.20.0/24   → C
0.0.0.0/0       → D
```

Destination:

```text
10.10.20.55
```

Nó match /8, /16 và /24. Router chọn route có prefix dài nhất: **/24 → C**.

### Bản chất

Longest prefix match chọn route cụ thể nhất trong các route match, không phải route xuất hiện đầu tiên trong table.

---

## Drill 21 — C Array và Pointer

Code:

```c
#include <stdio.h>

int main(void) {
    int a[] = {10, 20, 30, 40};
    int *p = a + 1;
    printf("%d %d\n", *p, *(p + 2));
    return 0;
}
```

### Trace

`a` trong expression decay thành pointer tới `a[0]`.  
`a + 1` trỏ `a[1]` = 20.  
`*p` = 20.  
`p + 2` trỏ `a[3]` = 40.

**Output:**

```text
20 40
```

### Bẫy

Pointer arithmetic tăng theo element size tự động; `p + 1` không có nghĩa cộng 1 byte với `int*`.

---

## Drill 22 — C Pre/Post Increment

Code:

```c
int x = 3;
int y = x++;
int z = ++x;
```

### State

```text
start: x=3
 y=x++ → y=3, x becomes 4
 z=++x → x becomes 5, z=5
```

Final:

```text
x=5, y=3, z=5
```

### Warning

Không mở rộng mẹo này sang expressions có undefined/unspecified behavior trong C. Khi cùng scalar bị modify/read phức tạp trong một expression, phải biết language rule chứ không “trace theo cảm giác”.

---

## Drill 23 — Java Overriding và Dynamic Dispatch

Code:

```java
class A {
    void f() { System.out.print("A"); }
}

class B extends A {
    @Override
    void f() { System.out.print("B"); }
}

public class Main {
    public static void main(String[] args) {
        A x = new B();
        x.f();
    }
}
```

Reference type là A nhưng runtime object là B. Instance method `f()` được override và dynamic dispatch chọn implementation của B.

**Output: `B`.**

### Phân biệt

Overloading resolution chủ yếu dùng method signature và compile-time typing; overriding liên quan runtime polymorphism cho instance method có contract phù hợp.

---

## Drill 24 — Python Alias và Mutability

Code:

```python
a = [1, 2]
b = a
b.append(3)
print(a)
```

`a` và `b` refer cùng list object. `append` mutate object đó.

**Output:**

```text
[1, 2, 3]
```

Nếu muốn independent shallow copy trong case này:

```python
b = a.copy()
```

Nhưng shallow copy không recursively copy nested mutable objects.

---

# Part D — 정보시스템 구축 관리

## Drill 25 — PERT Expected Time

Một activity có:

```text
Optimistic  O = 4
Most likely M = 7
Pessimistic P = 16
```

PERT expected time:

```text
TE = (O + 4M + P) / 6
```

Substitute:

```text
TE = (4 + 4*7 + 16) / 6
   = (4 + 28 + 16) / 6
   = 48 / 6
   = 8
```

**Expected time = 8 time units.**

---

## Drill 26 — Critical Path

Project network có hai path độc lập từ start tới finish:

```text
Path 1: A(3) → B(5) → C(2)
Path 2: D(4) → E(3)
```

Durations:

```text
Path 1 = 3+5+2 = 10
Path 2 = 4+3   = 7
```

Critical path là path dài nhất theo total duration trong network dependency này: **A-B-C = 10**.

Nếu activity trên critical path delay 1 đơn vị và không có float/slack, project completion cũng delay 1.

---

## Drill 27 — RAID Capacity

Có 4 disk, mỗi disk 2 TB.

### RAID 0

No redundancy.

```text
Capacity = 4 * 2 = 8 TB
```

### RAID 1

Nếu mirror theo pairs phổ biến, usable capacity = một nửa raw capacity:

```text
4 * 2 / 2 = 4 TB
```

### RAID 5

Distributed parity tương đương capacity của 1 disk dùng cho parity:

```text
(4 - 1) * 2 = 6 TB
```

Có thể chịu failure của một disk trong array trước khi rebuild/further failure.

### RAID 6

Dual parity tương đương 2 disk capacity:

```text
(4 - 2) * 2 = 4 TB
```

Có thể chịu hai disk failures theo model RAID 6.

### Bẫy

RAID là availability/storage-failure mechanism, **không phải backup**. Xóa nhầm/ransomware/corruption logic có thể replicate lên toàn array.

---

## Drill 28 — RTO và RPO

Business requirement:

```text
Service must be restored within 30 minutes.
At most 5 minutes of committed business data may be lost.
```

Map:

```text
RTO = 30 minutes
RPO = 5 minutes
```

Nếu backup mỗi 24 giờ, backup policy đó một mình không đáp ứng RPO 5 phút.

Nếu replication gần real-time nhưng failover cần 4 giờ manual work, data RPO có thể tốt nhưng RTO vẫn không đạt.

---

## Drill 29 — Security Control Mapping

Ghép threat với control chính hợp lý nhất trong các lựa chọn sau:

1. SQL Injection  
2. Password truyền plaintext trên network  
3. User A đổi URL ID và đọc invoice của User B  
4. Internet scan vào port không cần thiết  
5. Malicious input gây XSS stored

Controls:

A. TLS  
B. Object-level authorization  
C. Parameterized query / prepared statement  
D. Network firewall / security group rule  
E. Context-appropriate output encoding + input handling

### Answer

```text
1 → C
2 → A
3 → B
4 → D
5 → E
```

### Bản chất

Một hệ thống thật dùng defense in depth, nhưng đề thường hỏi control giải quyết nguyên nhân trực tiếp nhất.

---

## Drill 30 — Deadlock Conditions

Bốn Coffman conditions truyền thống:

```text
Mutual Exclusion
Hold and Wait
No Preemption
Circular Wait
```

Nếu hệ thống impose total ordering lên resource và mọi process phải acquire theo cùng order, nó nhắm phá **Circular Wait**.

Nếu process phải request toàn bộ resources trước khi bắt đầu và không giữ một resource trong khi chờ resource mới, nó nhắm phá **Hold and Wait**.

### Bẫy

Deadlock prevention thay đổi điều kiện để deadlock không thể hình thành. Deadlock avoidance như Banker’s Algorithm dùng trạng thái safe/unsafe và knowledge về maximum demand. Detection cho phép xảy ra rồi phát hiện/recover. Ba strategy không đồng nghĩa.

---

# Part E — Mixed procedural drills không xem solution ngay

## Drill 31 — Composite Index

Table:

```text
Log(user_id, event_type, created_at, payload)
```

Query chính:

```sql
SELECT created_at, event_type
FROM Log
WHERE user_id = ?
  AND created_at >= ?
ORDER BY created_at DESC;
```

Tự giải:

1. Đề xuất một composite B+Tree index có lý do.
2. Giải thích vì sao `event_type` có thể đặt sau hoặc bỏ khỏi search-key tùy mục tiêu covering/index size.
3. Giải thích vì sao index `(created_at, user_id)` có thể kém tự nhiên hơn cho access pattern equality-user + time-range này.

### Expected reasoning

Một starting design tự nhiên là `(user_id, created_at)`; DBMS-specific details và workload vẫn quyết định final plan. Equality prefix theo user thu hẹp range, sau đó ordered range theo time.

---

## Drill 32 — Transaction + Retry

Client gửi request transfer với `request_id = R123`. Server timeout sau commit. Client retry cùng `request_id`.

Tự thiết kế:

- bảng hoặc constraint nào lưu idempotency identity;
- transaction boundary nào cần bao quanh transfer và idempotency record;
- response cho duplicate request hợp lệ nên dựa vào result cũ thế nào.

### Expected reasoning

Nếu business side effect commit nhưng idempotency record không commit atomically cùng boundary, retry vẫn có thể lặp side effect. Design phải biến “same request identity” thành invariant mà DB enforce hoặc kiểm tra an toàn dưới concurrency.

---

## Drill 33 — CPU vs I/O reasoning

Một process chạy pattern:

```text
CPU 2ms → I/O 20ms → CPU 2ms → I/O 20ms ...
```

Một process khác chạy CPU burst dài 100ms.

Tự giải thích tại sao scheduling policy ảnh hưởng response/interactivity khác nhau và vì sao chỉ nhìn tổng CPU time không đủ để hiểu system behavior.

---

## Drill 34 — Subnet design

Cần ít nhất 50 usable IPv4 host addresses trong một subnet truyền thống.

Tìm prefix nhỏ nhất thỏa:

```text
2^h - 2 >= 50
```

`h=5` cho 30, không đủ. `h=6` cho 62, đủ.

Prefix:

```text
32 - 6 = /26
```

**Đáp án: /26.**

---

## Drill 35 — Normalization vs Performance

Một analytics query join 8 bảng normalized và chạy quá chậm. Team đề xuất denormalized summary table.

Tự trả lời:

1. Denormalization có làm schema “sai” không?
2. Consistency burden mới là gì?
3. Khi nào materialized view/summary table có thể hợp lý?
4. Vì sao không nên phá normalization của OLTP tables chỉ vì một query analytics chậm trước khi đo execution plan/index/data volume?

### Expected reasoning

Normalization và physical/performance optimization giải quyết mục tiêu khác nhau. Denormalization có thể là deliberate trade-off, nhưng phải quản lý refresh/consistency và chứng minh bằng workload.

---

# Part F — Procedure templates phải nhớ

## Functional Dependency / Key

```text
1. Chọn attribute set X
2. Tính X+ bằng closure
3. Nếu X+ chứa mọi attribute → superkey
4. Thử bỏ từng attribute khỏi X
5. Không bỏ được nữa → candidate key
```

## Normalization

```text
1. Xác định candidate key
2. Liệt kê functional dependencies
3. 1NF: atomic domain theo model quan hệ
4. 2NF: loại partial dependency vào composite key
5. 3NF: xử lý transitive dependency / kiểm điều kiện formal
6. BCNF: mọi determinant của non-trivial FD phải là superkey
7. Kiểm lossless join và dependency preservation khi decomposition
```

## SQL Aggregate

```text
FROM/JOIN
→ WHERE
→ GROUP BY
→ aggregate
→ HAVING
→ SELECT
→ ORDER BY
```

Đây là logical reasoning model, không khẳng định DBMS physically execute đúng thứ tự đó.

## Conflict Serializability

```text
1. Tìm conflict pair trên cùng item
2. Ít nhất một write
3. Thêm precedence edge
4. Cycle? yes → not conflict-serializable
5. Acyclic → topological order cho equivalent serial order
```

## CPU Scheduling

```text
1. Vẽ timeline/Gantt
2. Tính completion time
3. turnaround = completion - arrival
4. waiting = turnaround - burst
5. response = first_run - arrival
```

## Page Replacement

```text
1. Ghi state frame sau từng reference
2. Hit hay fault?
3. Nếu fault và full → chọn victim đúng policy
4. Update policy metadata
5. Đếm fault sau cùng
```

## Subnetting

```text
1. prefix → host bits
2. total addresses = 2^host_bits
3. mask
4. block size ở interesting octet
5. tìm boundary chứa IP
6. network / broadcast / usable range
```

## PERT/CPM

```text
PERT expected = (O + 4M + P)/6
CPM: tính path duration / earliest-latest time
Critical path: zero-slack path quyết định project duration trong model
```

---

# Final Check — không nhìn đáp án

Bạn chỉ được đánh dấu workbook hoàn thành khi có thể tự làm lại tối thiểu các dạng sau mà không cần nhớ con số cụ thể của ví dụ:

- Cyclomatic complexity;
- stack/postfix;
- BFS/DFS;
- hash probing;
- binary search trace;
- attribute closure và candidate key;
- 2NF/3NF/BCNF reasoning;
- JOIN/NULL/GROUP BY/HAVING;
- conflict serializability và isolation anomaly;
- FCFS/SJF/Round Robin;
- FIFO/LRU page replacement;
- IPv4 subnetting và longest-prefix match;
- C pointer/basic expression trace;
- Java overriding/dynamic dispatch;
- Python reference/mutability;
- PERT và critical path;
- RAID capacity;
- RTO/RPO;
- threat → control mapping;
- deadlock condition/prevention.

Nếu một procedure chỉ làm được khi nhìn lại ví dụ, quay về drill tương ứng và thay số liệu tự tạo thêm ít nhất hai lần.