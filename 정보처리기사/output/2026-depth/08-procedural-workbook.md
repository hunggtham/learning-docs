# 정보처리기사 필기 2026 — Procedural Workbook

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **정보처리기사 필기 2026 — Procedural Workbook**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **0. Cách dùng** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Drill 1 — Cyclomatic độ phức tạp (complexity / 복잡도)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối procedural workbook với drill, complexity và remediation, để luyện tập bắt đầu từ lỗi quan sát được.

> Đây là workbook cho các dạng bài **không thể học chỉ bằng cách đọc**. Mỗi drill buộc phải viết tay các bước trung gian. Nếu nhìn đáp án rồi thấy “hiểu” nhưng không tự làm lại được, chưa tính là hoàn thành.
>
> Các bài đều được viết mới, dùng để luyện cơ chế chứ không sao chép 기출.

---

## 0. Cách dùng

Mỗi drill làm theo ba vòng.

**Vòng 1 — Closed book:** tự giải, ghi toàn bộ trạng thái (state / 상태) trung gian.
**Vòng 2 — lỗi (error / 오류) classification:** nếu sai, đánh dấu `concept`, `procedure`, `arithmetic`, `term`, hoặc `careless`.
**Vòng 3 — Reproduction:** sau ít nhất một lần chuyển sang bài khác, quay lại làm từ đầu mà không nhìn solution.

Mục tiêu không phải nhớ đáp số. Mục tiêu là tạo một procedure ổn định có thể dùng khi đề thay số liệu.

---

# Part A — 소프트웨어 설계 / 소프트웨어 개발

> **Nối mạch:** Trong **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 1 — Cyclomatic độ phức tạp (complexity / 복잡도)** nối từ **0. Cách dùng** sang **Drill 2 — ngăn xếp (stack / 스택) và postfix expression**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 1 — Cyclomatic độ phức tạp (complexity / 복잡도)

Cho control-flow đồ thị (graph / 그래프) có `N = 8` nút (node / 노드) và `E = 10` edge, một connected thành phần (component / 컴포넌트).

### Tự giải

Tính Cyclomatic độ phức tạp (complexity / 복잡도) — 순환 복잡도 — bằng công thức:

```text
V(G) = E - N + 2P
```

với `P = 1`.

### Solution

```text
V(G) = 10 - 8 + 2 = 4
```

Nghĩa là đồ thị (graph / 그래프) có 4 independent paths trong basis-path interpretation. Đây không có nghĩa chỉ cần đúng 4 trường hợp kiểm thử (test case / 테스트 케이스) là “kiểm thử (test / 테스트) hoàn toàn mọi hành vi (behavior / 동작)”; nó chỉ cho một structural testing measure liên quan independent đường dẫn (path / 경로).

### Bẫy

Nếu đồ thị (graph / 그래프) có nhiều connected thành phần (component / 컴포넌트), phải dùng đúng `P`, không mặc định luôn bằng 1.

---

> **Nối mạch:** Ở chặng này của **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 2 — ngăn xếp (stack / 스택) và postfix expression** nối từ **Drill 1 — Cyclomatic độ phức tạp (complexity / 복잡도)** sang **Drill 3 — BFS và DFS**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 2 — ngăn xếp (stack / 스택) và postfix expression

Tính biểu thức postfix:

```text
5 2 3 * + 8 4 / -
```

### Procedure

Đọc từ trái sang phải.

1. gặp operand → push;
2. gặp operator → pop operand phải trước, rồi operand trái;
3. tính và push kết quả (result / 결과).

### Dấu vết (trace / 추적)

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 3 — BFS và DFS** nối từ **Drill 2 — ngăn xếp (stack / 스택) và postfix expression** sang **Drill 4 — bảng băm (hash table / 해시 테이블) với tuyến tính (linear / 선형) Probing**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 3 — BFS và DFS

Đồ thị (graph / 그래프) vô hướng có adjacency theo đúng thứ tự sau:

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

Hàng đợi (queue / 큐) dấu vết (trace / 추적):

```text
visit A; queue [B, C]
visit B; enqueue D,E → [C, D, E]
visit C; enqueue F   → [D, E, F]
visit D              → [E, F]
visit E              → [F]
visit F              → []
```

**BFS thứ tự (order / 순서): A, B, C, D, E, F.**

### DFS

Nếu dùng recursive DFS theo thứ tự adjacency:

```text
A → B → D → back → E → F → C
```

**DFS thứ tự (order / 순서): A, B, D, E, F, C.**

### Bản chất

BFS dùng frontier theo FIFO nên khám phá theo “tầng (layer / 계층)” số cạnh. Với đồ thị (graph / 그래프) không trọng số, đây là nền tảng shortest đường dẫn (path / 경로) theo số edge. DFS đi sâu trước và phù hợp nhiều bài connectivity, cycle, topological-style lập luận (reasoning / 추론) nhưng không tự bảo đảm shortest đường dẫn (path / 경로) unweighted.

---

> **Nối mạch:** Trong **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 4 — bảng băm (hash table / 해시 테이블) với tuyến tính (linear / 선형) Probing** nối từ **Drill 3 — BFS và DFS** sang **Drill 5 — tìm kiếm nhị phân (binary search / 이진 탐색)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 4 — bảng băm (hash table / 해시 테이블) với tuyến tính (linear / 선형) Probing

Bảng băm (hash table / 해시 테이블) kích thước (size / 크기) 7, băm (hash / 해시) hàm (function / 함수):

```text
h(k) = k mod 7
```

Insert theo thứ tự `10, 17, 24, 11` bằng tuyến tính (linear / 선형) Probing.

### Dấu vết (trace / 추적)

```text
10 mod 7 = 3 → slot 3 = 10
17 mod 7 = 3 → 3 occupied → slot 4 = 17
24 mod 7 = 3 → 3,4 occupied → slot 5 = 24
11 mod 7 = 4 → 4,5 occupied → slot 6 = 11
```

Final bảng (table / 테이블):

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

Tuyến tính (linear / 선형) probing có thể tạo **Primary Clustering — 1차 군집화**: một cluster liên tục càng dài thì key mới băm (hash / 해시) vào gần đó càng dễ kéo cluster dài thêm.

---

> **Nối mạch:** Ở chặng này của **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 5 — tìm kiếm nhị phân (binary search / 이진 탐색)** nối từ **Drill 4 — bảng băm (hash table / 해시 테이블) với tuyến tính (linear / 선형) Probing** sang **Drill 6 — Candidate Key từ Functional phụ thuộc (dependency / 의존성)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 5 — tìm kiếm nhị phân (binary search / 이진 탐색)

Sorted array:

```text
[3, 8, 12, 19, 23, 31, 44, 57, 62]
```

Tìm 31 bằng tìm kiếm nhị phân (binary search / 이진 탐색) với chỉ mục (index / 인덱스) 0-based.

### Dấu vết (trace / 추적)

```text
low=0 high=8 mid=4 → a[4]=23 < 31 → low=5
low=5 high=8 mid=6 → a[6]=44 > 31 → high=5
low=5 high=5 mid=5 → a[5]=31 → found
```

### Bản chất

Tìm kiếm nhị phân (binary search / 이진 탐색) cần tìm kiếm (search / 검색) không gian (space / 공간) có thứ tự (ordering / 순서) phù hợp. O(log n) ở đây đến từ việc mỗi comparison loại bỏ khoảng một nửa candidate phạm vi (range / 범위).

---

# Part B — 데이터베이스 구축

> **Nối mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 6 — Candidate Key từ Functional phụ thuộc (dependency / 의존성)** nối từ **Drill 5 — tìm kiếm nhị phân (binary search / 이진 탐색)** sang **Drill 7 — 2NF và Partial phụ thuộc (dependency / 의존성)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 6 — Candidate Key từ Functional phụ thuộc (dependency / 의존성)

Quan hệ (relation / 관계):

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

### Closure lập luận (reasoning / 추론)

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

Vậy A xác định toàn bộ quan hệ (relation / 관계). Không thể bỏ gì khỏi A vì chỉ có một attribute.

**Candidate key: A.**

### Bẫy

FD `AC → D` không có nghĩa key bắt buộc là `AC`. Vì `A → B → C`, A đã suy ra C trước khi áp dụng phụ thuộc (dependency / 의존성) đó.

---

> **Nối mạch:** Trong **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 7 — 2NF và Partial phụ thuộc (dependency / 의존성)** nối từ **Drill 6 — Candidate Key từ Functional phụ thuộc (dependency / 의존성)** sang **Drill 8 — 3NF và Transitive phụ thuộc (dependency / 의존성)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 7 — 2NF và Partial phụ thuộc (dependency / 의존성)

Quan hệ (relation / 관계):

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

Đây là **부분 함수 종속 — partial functional phụ thuộc (dependency / 의존성)**, vi phạm 2NF.

### Decompose

```text
Student(StudentId, StudentName)
Course(CourseId, CourseName)
Enrollment(StudentId, CourseId, Grade)
```

### Bản chất

2NF nhắm tới partial phụ thuộc (dependency / 의존성) của non-prime attribute vào một phần candidate key. Nếu key chỉ có một attribute, partial phụ thuộc (dependency / 의존성) kiểu này không tồn tại.

---

> **Nối mạch:** Ở chặng này của **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 8 — 3NF và Transitive phụ thuộc (dependency / 의존성)** nối từ **Drill 7 — 2NF và Partial phụ thuộc (dependency / 의존성)** sang **Drill 9 — GROUP BY, WHERE và HAVING**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 8 — 3NF và Transitive phụ thuộc (dependency / 의존성)

Quan hệ (relation / 관계):

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

`DeptName` phụ thuộc transitive vào key qua `DeptId`. Đây là **이행적 함수 종속 — transitive functional phụ thuộc (dependency / 의존성)**.

Decompose:

```text
Employee(EmpId, DeptId)
Department(DeptId, DeptName)
```

### Bẫy

Không phải cứ quan hệ (relation / 관계) có foreign key là vi phạm 3NF. Vấn đề là phụ thuộc (dependency / 의존성) giữa non-key attributes theo điều kiện chuẩn hóa.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 9 — GROUP BY, WHERE và HAVING** nối từ **Drill 8 — 3NF và Transitive phụ thuộc (dependency / 의존성)** sang **Drill 10 — LEFT phép nối (join / 조인) và NULL**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 9 — GROUP BY, WHERE và HAVING

Bảng (table / 테이블) `orders(customer_id, amount, status)`.

Yêu cầu: chỉ tính các thứ tự (order / 순서) `PAID`, group theo customer, lấy customer có tổng amount > 1,000.

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

Đừng dùng `WHERE SUM(amount) > 1000` vì aggregate giá trị (value / 값) chưa tồn tại ở phase lô-gic (logic / 논리) đó.

---

> **Nối mạch:** Trong **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 10 — LEFT phép nối (join / 조인) và NULL** nối từ **Drill 9 — GROUP BY, WHERE và HAVING** sang **Drill 11 — xung đột (conflict / 충돌) Serializability**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 10 — LEFT phép nối (join / 조인) và NULL

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

Truy vấn (query / 쿼리):

```sql
SELECT c.id, COUNT(o.id)
FROM Customer c
LEFT JOIN Order o ON o.customer_id = c.id
GROUP BY c.id;
```

### Kết quả (result / 결과)

```text
1 → 2
2 → 0
3 → 1
```

### Vì sao B vẫn xuất hiện?

LEFT phép nối (join / 조인) giữ toàn bộ row bên trái. Với customer 2, columns bên thứ tự (order / 순서) trở thành NULL. `COUNT(o.id)` không đếm NULL nên kết quả (result / 결과) là 0.

### Bẫy

`COUNT(*)` ở group của customer 2 sẽ đếm preserved row và có thể cho 1, khác `COUNT(o.id)`.

---

> **Nối mạch:** Ở chặng này của **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 11 — xung đột (conflict / 충돌) Serializability** nối từ **Drill 10 — LEFT phép nối (join / 조인) và NULL** sang **Drill 12 — Isolation anomaly**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 11 — xung đột (conflict / 충돌) Serializability

Schedule:

```text
T1: R(X)
T2: R(X)
T1: W(X)
T2: W(X)
```

### Precedence đồ thị (graph / 그래프)

Conflicts trên X:

- `R1(X)` trước `W2(X)` → edge `T1 → T2`
- `R2(X)` trước `W1(X)` → edge `T2 → T1`
- `W1(X)` trước `W2(X)` → edge `T1 → T2`

Đồ thị (graph / 그래프) có cycle:

```text
T1 → T2 → T1
```

**Schedule không conflict-serializable.**

### Procedure chung

1. chỉ xét thao tác (operation / 연산) khác giao dịch (transaction / 트랜잭션) trên cùng dữ liệu (data / 데이터) item;
2. ít nhất một thao tác (operation / 연산) phải là ghi (write / 쓰기);
3. thêm edge theo thứ tự xuất hiện;
4. đồ thị (graph / 그래프) acyclic → conflict-serializable; có cycle → không.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 12 — Isolation anomaly** nối từ **Drill 11 — xung đột (conflict / 충돌) Serializability** sang **Drill 13 — FCFS Scheduling**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 12 — Isolation anomaly

T1 đọc balance = 100. T2 cập nhật (update / 업데이트) balance = 50 và lần ghi nhận (commit / 커밋). T1 đọc lại cùng row và thấy 50.

### Nhận diện

Đây là **Non-repeatable Read — 반복 불가능 읽기**: cùng một row, cùng giao dịch (transaction / 트랜잭션), hai lần đọc cho giá trị (value / 값) khác do giao dịch (transaction / 트랜잭션) khác đã lần ghi nhận (commit / 커밋) cập nhật (update / 업데이트).

Nếu T1 chạy cùng predicate `WHERE amount > 1000` và lần hai xuất hiện thêm row mới do T2 insert, đó gần với **Phantom Read — 팬텀 리드**.

---

# Part C — 프로그래밍 언어 활용 / OS / mạng (network / 네트워크)

> **Nối mạch:** Trong **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 13 — FCFS Scheduling** nối từ **Drill 12 — Isolation anomaly** sang **Drill 14 — SJF Non-preemptive**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 13 — FCFS Scheduling

Processes cùng arrive thời gian (time / 시간) 0:

| tiến trình (process / 프로세스) | Burst |
|---|---:|
| P1 | 5 |
| P2 | 3 |
| P3 | 2 |

FCFS thứ tự (order / 순서): P1 → P2 → P3.

### Waiting thời gian (time / 시간)

```text
P1 = 0
P2 = 5
P3 = 5 + 3 = 8
```

Average waiting thời gian (time / 시간):

```text
(0 + 5 + 8) / 3 = 13/3 ≈ 4.33
```

### Turnaround thời gian (time / 시간)

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

> **Nối mạch:** Ở chặng này của **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 14 — SJF Non-preemptive** nối từ **Drill 13 — FCFS Scheduling** sang **Drill 15 — Round Robin**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 14 — SJF Non-preemptive

Cùng processes trên, tất cả arrive thời gian (time / 시간) 0.

SJF thứ tự (order / 순서):

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

SJF giảm average waiting trong benchmark khi burst thời gian (time / 시간) biết trước, nhưng practical hệ thống (system / 시스템) thường không biết chính xác future CPU burst và có starvation rủi ro (risk / 위험) với long jobs nếu short jobs liên tục đến.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 15 — Round Robin** nối từ **Drill 14 — SJF Non-preemptive** sang **Drill 16 — FIFO Page Replacement**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 15 — Round Robin

Processes đều arrive 0:

```text
P1 burst 5
P2 burst 3
P3 burst 1
Quantum = 2
```

### Dấu vết (trace / 추적)

```text
0-2   P1, remaining 3
2-4   P2, remaining 1
4-5   P3, done
5-7   P1, remaining 1
7-8   P2, done
8-9   P1, done
```

Completion thời gian (time / 시간):

```text
P3 = 5
P2 = 8
P1 = 9
```

Vì arrive thời gian (time / 시간) = 0, turnaround = completion.

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

> **Nối mạch:** Trong **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 16 — FIFO Page Replacement** nối từ **Drill 15 — Round Robin** sang **Drill 17 — LRU Page Replacement**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 16 — FIFO Page Replacement

3 frame, tham chiếu (reference / 참조) string:

```text
1 2 3 1 4 5
```

### Dấu vết (trace / 추적)

```text
1 → [1,-,-] fault
2 → [1,2,-] fault
3 → [1,2,3] fault
1 → [1,2,3] hit
4 → [4,2,3] fault   // replace oldest page 1
5 → [4,5,3] fault   // replace oldest page 2
```

**Page faults = 5.**

FIFO chỉ quan tâm arrival thứ tự (order / 순서) vào frame, không quan tâm page vừa được dùng lại gần đây.

---

> **Nối mạch:** Ở chặng này của **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 17 — LRU Page Replacement** nối từ **Drill 16 — FIFO Page Replacement** sang **Drill 18 — IPv4 Subnetting /27**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 17 — LRU Page Replacement

Cùng 3 frame và tham chiếu (reference / 참조):

```text
1 2 3 1 4 5
```

### Dấu vết (trace / 추적) lập luận (reasoning / 추론)

Sau `1 2 3`, cả ba ở bộ nhớ (memory / 메모리). tham chiếu (reference / 참조) `1` làm 1 trở thành recently used.

Khi `4` tới, least recently used là 2 → replace 2.

Trạng thái (state / 상태): `{1,3,4}`.

Khi `5` tới, among 1,3,4 thì 3 là least recently used → replace 3.

**Page faults cũng = 5 trong chuỗi này**, dù victim khác FIFO. Đừng suy rằng LRU luôn cho ít fault hơn trên mọi short tham chiếu (reference / 참조) string; chính sách (policy / 정책) khác nhau có thể tình cờ cùng count.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 18 — IPv4 Subnetting /27** nối từ **Drill 17 — LRU Page Replacement** sang **Drill 19 — Xác định subnet của host**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 18 — IPv4 Subnetting /27

Mạng (network / 네트워크):

```text
192.168.10.0/27
```

### Step 1 — host bits

`/27` nghĩa 27 mạng (network / 네트워크) bits, còn 5 host bits.

Total addresses:

```text
2^5 = 32
```

Traditional usable host addresses:

```text
32 - 2 = 30
```

### Step 2 — khối (block / 블록) kích thước (size / 크기)

Mask:

```text
255.255.255.224
```

Khối (block / 블록) kích thước (size / 크기) ở octet cuối:

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

> **Nối mạch:** Trong **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 19 — Xác định subnet của host** nối từ **Drill 18 — IPv4 Subnetting /27** sang **Drill 20 — Longest Prefix Match**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 19 — Xác định subnet của host

Host:

```text
192.168.10.77/27
```

Khối (block / 블록) kích thước (size / 크기) = 32. Các ranh giới (boundary / 경계):

```text
0, 32, 64, 96, ...
```

77 nằm trong khối (block / 블록) 64–95.

```text
Network   = 192.168.10.64
Broadcast = 192.168.10.95
Usable    = 192.168.10.65 ~ 192.168.10.94
```

---

> **Nối mạch:** Ở chặng này của **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 20 — Longest Prefix Match** nối từ **Drill 19 — Xác định subnet của host** sang **Drill 21 — C Array và Pointer**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 20 — Longest Prefix Match

Routing bảng (table / 테이블):

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

Nó match /8, /16 và /24. Router chọn tuyến (route / 경로) có prefix dài nhất: **/24 → C**.

### Bản chất

Longest prefix match chọn tuyến (route / 경로) cụ thể nhất trong các tuyến (route / 경로) match, không phải tuyến (route / 경로) xuất hiện đầu tiên trong bảng (table / 테이블).

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 21 — C Array và Pointer** nối từ **Drill 20 — Longest Prefix Match** sang **Drill 22 — C Pre/Post Increment**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 21 — C Array và Pointer

Mã (code / 코드):

```c
#include <stdio.h>

int main(void) {
    int a[] = {10, 20, 30, 40};
    int *p = a + 1;
    printf("%d %d\n", *p, *(p + 2));
    return 0;
}
```

### Dấu vết (trace / 추적)

`a` trong expression decay thành pointer tới `a[0]`.
`a + 1` trỏ `a[1]` = 20.
`*p` = 20.
`p + 2` trỏ `a[3]` = 40.

**đầu ra (output / 출력):**

```text
20 40
```

### Bẫy

Pointer arithmetic tăng theo element kích thước (size / 크기) tự động; `p + 1` không có nghĩa cộng 1 byte với `int*`.

---

> **Nối mạch:** Trong **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 22 — C Pre/Post Increment** nối từ **Drill 21 — C Array và Pointer** sang **Drill 23 — Java Overriding và động (dynamic / 동적) Dispatch**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 22 — C Pre/Post Increment

Mã (code / 코드):

```c
int x = 3;
int y = x++;
int z = ++x;
```

### Trạng thái (state / 상태)

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

Không mở rộng mẹo này sang expressions có undefined/unspecified hành vi (behavior / 동작) trong C. Khi cùng scalar bị modify/read phức tạp trong một expression, phải biết ngôn ngữ (language / 언어) quy tắc (rule / 규칙) chứ không “dấu vết (trace / 추적) theo cảm giác”.

---

> **Nối mạch:** Ở chặng này của **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 23 — Java Overriding và động (dynamic / 동적) Dispatch** nối từ **Drill 22 — C Pre/Post Increment** sang **Drill 24 — Python Alias và Mutability**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 23 — Java Overriding và động (dynamic / 동적) Dispatch

Mã (code / 코드):

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

Tham chiếu (reference / 참조) kiểu (type / 타입) là A nhưng thời gian chạy (runtime / 런타임) đối tượng (object / 객체) là B. Instance phương thức (method / 메서드) `f()` được override và động (dynamic / 동적) dispatch chọn hiện thực (implementation / 구현) của B.

**đầu ra (output / 출력): `B`.**

### Phân biệt

Overloading resolution chủ yếu dùng phương thức (method / 메서드) signature và compile-time typing; overriding liên quan thời gian chạy (runtime / 런타임) polymorphism cho instance phương thức (method / 메서드) có đặc tả hợp đồng (contract / 계약) phù hợp.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 24 — Python Alias và Mutability** nối từ **Drill 23 — Java Overriding và động (dynamic / 동적) Dispatch** sang **Drill 25 — PERT Expected thời gian (time / 시간)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 24 — Python Alias và Mutability

Mã (code / 코드):

```python
a = [1, 2]
b = a
b.append(3)
print(a)
```

`a` và `b` refer cùng danh sách (list / 목록) đối tượng (object / 객체). `append` mutate đối tượng (object / 객체) đó.

**đầu ra (output / 출력):**

```text
[1, 2, 3]
```

Nếu muốn independent shallow bản sao (copy / 복사) trong trường hợp (case / 사례) này:

```python
b = a.copy()
```

Nhưng shallow bản sao (copy / 복사) không recursively bản sao (copy / 복사) nested mutable objects.

---

# Part D — 정보시스템 구축 관리

> **Nối mạch:** Trong **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 25 — PERT Expected thời gian (time / 시간)** nối từ **Drill 24 — Python Alias và Mutability** sang **Drill 26 — đường găng (critical path / 임계 경로)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 25 — PERT Expected thời gian (time / 시간)

Một activity có:

```text
Optimistic  O = 4
Most likely M = 7
Pessimistic P = 16
```

PERT expected thời gian (time / 시간):

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

**Expected thời gian (time / 시간) = 8 thời gian (time / 시간) units.**

---

> **Nối mạch:** Ở chặng này của **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 25 — PERT Expected thời gian (time / 시간)** đặt đầu vào cho **Drill 26 — đường găng (critical path / 임계 경로)**, rồi **Drill 27 — RAID sức chứa (capacity / 용량)** mở rộng hệ quả liên quan.

## Drill 26 — đường găng (critical path / 임계 경로)

Dự án (project / 프로젝트) mạng (network / 네트워크) có hai đường dẫn (path / 경로) độc lập từ start tới finish:

```text
Path 1: A(3) → B(5) → C(2)
Path 2: D(4) → E(3)
```

Durations:

```text
Path 1 = 3+5+2 = 10
Path 2 = 4+3   = 7
```

Đường găng (critical path / 임계 경로) là đường dẫn (path / 경로) dài nhất theo total duration trong mạng (network / 네트워크) phụ thuộc (dependency / 의존성) này: **A-B-C = 10**.

Nếu activity trên đường găng (critical path / 임계 경로) delay 1 đơn vị và không có float/slack, dự án (project / 프로젝트) completion cũng delay 1.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 26 — đường găng (critical path / 임계 경로)** đặt đầu vào cho **Drill 27 — RAID sức chứa (capacity / 용량)**, rồi **Drill 28 — RTO và RPO** mở rộng hệ quả liên quan.

## Drill 27 — RAID sức chứa (capacity / 용량)

Có 4 disk, mỗi disk 2 TB.

### RAID 0

No redundancy.

```text
Capacity = 4 * 2 = 8 TB
```

### RAID 1

Nếu mirror theo pairs phổ biến, usable sức chứa (capacity / 용량) = một nửa raw sức chứa (capacity / 용량):

```text
4 * 2 / 2 = 4 TB
```

### RAID 5

Phân tán (distributed / 분산) parity tương đương sức chứa (capacity / 용량) của 1 disk dùng cho parity:

```text
(4 - 1) * 2 = 6 TB
```

Có thể chịu thất bại (failure / 실패) của một disk trong array trước khi rebuild/further thất bại (failure / 실패).

### RAID 6

Dual parity tương đương 2 disk sức chứa (capacity / 용량):

```text
(4 - 2) * 2 = 4 TB
```

Có thể chịu hai disk failures theo mô hình (model / 모델) RAID 6.

### Bẫy

RAID là availability/storage-failure cơ chế (mechanism / 메커니즘), **không phải backup**. Xóa nhầm/ransomware/corruption lô-gic (logic / 논리) có thể replicate lên toàn array.

---

> **Nối mạch:** Trong **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 28 — RTO và RPO** nối từ **Drill 27 — RAID sức chứa (capacity / 용량)** sang **Drill 29 — bảo mật (security / 보안) điều khiển (control / 제어) ánh xạ (mapping / 매핑)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 28 — RTO và RPO

Nghiệp vụ (business / 비즈니스) yêu cầu (requirement / 요구사항):

```text
Service must be restored within 30 minutes.
At most 5 minutes of committed business data may be lost.
```

Map:

```text
RTO = 30 minutes
RPO = 5 minutes
```

Nếu backup mỗi 24 giờ, backup chính sách (policy / 정책) đó một mình không đáp ứng RPO 5 phút.

Nếu replication gần real-time nhưng failover cần 4 giờ manual công việc (work / 작업), dữ liệu (data / 데이터) RPO có thể tốt nhưng RTO vẫn không đạt.

---

> **Nối mạch:** Ở chặng này của **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 29 — bảo mật (security / 보안) điều khiển (control / 제어) ánh xạ (mapping / 매핑)** nối từ **Drill 28 — RTO và RPO** sang **Drill 30 — Deadlock Conditions**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 29 — bảo mật (security / 보안) điều khiển (control / 제어) ánh xạ (mapping / 매핑)

Ghép threat với điều khiển (control / 제어) chính hợp lý nhất trong các lựa chọn sau:

1. SQL Injection
2. Password truyền plaintext trên mạng (network / 네트워크)
3. người dùng (user / 사용자) A đổi URL ID và đọc invoice của người dùng (user / 사용자) B
4. Internet scan vào cổng (port / 포트) không cần thiết
5. Malicious đầu vào (input / 입력) gây XSS stored

Controls:

A. TLS
B. Object-level authorization
C. Parameterized truy vấn (query / 쿼리) / prepared statement
D. mạng (network / 네트워크) firewall / bảo mật (security / 보안) group quy tắc (rule / 규칙)
E. Context-appropriate đầu ra (output / 출력) encoding + đầu vào (input / 입력) handling

### Answer

```text
1 → C
2 → A
3 → B
4 → D
5 → E
```

### Bản chất

Một hệ thống thật dùng defense in độ sâu (depth / 깊이), nhưng đề thường hỏi điều khiển (control / 제어) giải quyết nguyên nhân trực tiếp nhất.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 30 — Deadlock Conditions** nối từ **Drill 29 — bảo mật (security / 보안) điều khiển (control / 제어) ánh xạ (mapping / 매핑)** sang **Drill 31 — Composite chỉ mục (index / 인덱스)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 30 — Deadlock Conditions

Bốn Coffman conditions truyền thống:

```text
Mutual Exclusion
Hold and Wait
No Preemption
Circular Wait
```

Nếu hệ thống impose total thứ tự (ordering / 순서) lên tài nguyên (resource / 자원) và mọi tiến trình (process / 프로세스) phải acquire theo cùng thứ tự (order / 순서), nó nhắm phá **Circular Wait**.

Nếu tiến trình (process / 프로세스) phải yêu cầu (request / 요청) toàn bộ resources trước khi bắt đầu và không giữ một tài nguyên (resource / 자원) trong khi chờ tài nguyên (resource / 자원) mới, nó nhắm phá **Hold and Wait**.

### Bẫy

Deadlock prevention thay đổi điều kiện để deadlock không thể hình thành. Deadlock avoidance như Banker’s thuật toán (algorithm / 알고리즘) dùng trạng thái safe/unsafe và kiến thức (knowledge / 지식) về maximum demand. Detection cho phép xảy ra rồi phát hiện/recover. Ba chiến lược (strategy / 전략) không đồng nghĩa.

---

# Part E — Mixed procedural drills không xem solution ngay

> **Nối mạch:** Trong **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 31 — Composite chỉ mục (index / 인덱스)** nối từ **Drill 30 — Deadlock Conditions** sang **Drill 32 — giao dịch (transaction / 트랜잭션) + thử lại (retry / 재시도)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 31 — Composite chỉ mục (index / 인덱스)

Bảng (table / 테이블):

```text
Log(user_id, event_type, created_at, payload)
```

Truy vấn (query / 쿼리) chính:

```sql
SELECT created_at, event_type
FROM Log
WHERE user_id = ?
  AND created_at >= ?
ORDER BY created_at DESC;
```

Tự giải:

1. Đề xuất một composite B+cây (tree / 트리) chỉ mục (index / 인덱스) có lý do.
2. Giải thích vì sao `event_type` có thể đặt sau hoặc bỏ khỏi search-key tùy mục tiêu covering/chỉ mục (index / 인덱스) kích thước (size / 크기).
3. Giải thích vì sao chỉ mục (index / 인덱스) `(created_at, user_id)` có thể kém tự nhiên hơn cho truy cập (access / 접근) mẫu (pattern / 패턴) equality-user + time-range này.

### Expected lập luận (reasoning / 추론)

Một starting thiết kế (design / 설계) tự nhiên là `(user_id, created_at)`; DBMS-specific details và tải công việc (workload / 워크로드) vẫn quyết định final plan. Equality prefix theo người dùng (user / 사용자) thu hẹp phạm vi (range / 범위), sau đó ordered phạm vi (range / 범위) theo thời gian (time / 시간).

---

> **Nối mạch:** Ở chặng này của **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 32 — giao dịch (transaction / 트랜잭션) + thử lại (retry / 재시도)** nối từ **Drill 31 — Composite chỉ mục (index / 인덱스)** sang **Drill 33 — CPU vs I/O lập luận (reasoning / 추론)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 32 — giao dịch (transaction / 트랜잭션) + thử lại (retry / 재시도)

Máy khách (client / 클라이언트) gửi yêu cầu (request / 요청) transfer với `request_id = R123`. máy chủ (server / 서버) hết thời gian chờ (timeout / 타임아웃) sau lần ghi nhận (commit / 커밋). máy khách (client / 클라이언트) thử lại (retry / 재시도) cùng `request_id`.

Tự thiết kế:

- bảng hoặc ràng buộc (constraint / 제약조건) nào lưu idempotency định danh (identity / 식별자);
- giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) nào cần bao quanh transfer và idempotency bản ghi (record / 레코드);
- phản hồi (response / 응답) cho duplicate yêu cầu (request / 요청) hợp lệ nên dựa vào kết quả (result / 결과) cũ thế nào.

### Expected lập luận (reasoning / 추론)

Nếu nghiệp vụ (business / 비즈니스) side tác động (effect / 효과) lần ghi nhận (commit / 커밋) nhưng idempotency bản ghi (record / 레코드) không lần ghi nhận (commit / 커밋) atomically cùng ranh giới (boundary / 경계), thử lại (retry / 재시도) vẫn có thể lặp side tác động (effect / 효과). thiết kế (design / 설계) phải biến “same yêu cầu (request / 요청) định danh (identity / 식별자)” thành bất biến (invariant / 불변식) mà DB enforce hoặc kiểm tra an toàn dưới tính đồng thời (concurrency / 동시성).

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 33 — CPU vs I/O lập luận (reasoning / 추론)** nối từ **Drill 32 — giao dịch (transaction / 트랜잭션) + thử lại (retry / 재시도)** sang **Drill 34 — Subnet thiết kế (design / 설계)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 33 — CPU vs I/O lập luận (reasoning / 추론)

Một tiến trình (process / 프로세스) chạy mẫu (pattern / 패턴):

```text
CPU 2ms → I/O 20ms → CPU 2ms → I/O 20ms ...
```

Một tiến trình (process / 프로세스) khác chạy CPU burst dài 100ms.

Tự giải thích tại sao scheduling chính sách (policy / 정책) ảnh hưởng phản hồi (response / 응답)/interactivity khác nhau và vì sao chỉ nhìn tổng CPU thời gian (time / 시간) không đủ để hiểu hệ thống (system / 시스템) hành vi (behavior / 동작).

---

> **Nối mạch:** Trong **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 34 — Subnet thiết kế (design / 설계)** nối từ **Drill 33 — CPU vs I/O lập luận (reasoning / 추론)** sang **Drill 35 — Normalization vs hiệu năng (performance / 성능)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 34 — Subnet thiết kế (design / 설계)

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

> **Nối mạch:** Ở chặng này của **정보처리기사 필기 2026 — Procedural Workbook**, **Drill 35 — Normalization vs hiệu năng (performance / 성능)** nối từ **Drill 34 — Subnet thiết kế (design / 설계)** sang **Functional phụ thuộc (dependency / 의존성) / Key**, vì cơ chế trước tạo đầu vào cho bước sau.

## Drill 35 — Normalization vs hiệu năng (performance / 성능)

Một analytics truy vấn (query / 쿼리) phép nối (join / 조인) 8 bảng normalized và chạy quá chậm. nhóm (team / 팀) đề xuất denormalized summary bảng (table / 테이블).

Tự trả lời:

1. Denormalization có làm lược đồ (schema / 스키마) “sai” không?
2. Consistency burden mới là gì?
3. Khi nào materialized view/summary bảng (table / 테이블) có thể hợp lý?
4. Vì sao không nên phá normalization của OLTP tables chỉ vì một truy vấn (query / 쿼리) analytics chậm trước khi đo thực thi (execution / 실행) plan/chỉ mục (index / 인덱스)/dữ liệu (data / 데이터) volume?

### Expected lập luận (reasoning / 추론)

Normalization và vật lý (physical / 물리적)/hiệu năng (performance / 성능) tối ưu hóa (optimization / 최적화) giải quyết mục tiêu khác nhau. Denormalization có thể là deliberate sự đánh đổi (trade-off / 트레이드오프), nhưng phải quản lý refresh/consistency và chứng minh bằng tải công việc (workload / 워크로드).

---

# Part F — Procedure templates phải nhớ

> **Nối mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Procedural Workbook**, **Functional phụ thuộc (dependency / 의존성) / Key** nối từ **Drill 35 — Normalization vs hiệu năng (performance / 성능)** sang **Normalization**, vì cơ chế trước tạo đầu vào cho bước sau.

## Functional phụ thuộc (dependency / 의존성) / Key

```text
1. Chọn attribute set X
2. Tính X+ bằng closure
3. Nếu X+ chứa mọi attribute → superkey
4. Thử bỏ từng attribute khỏi X
5. Không bỏ được nữa → candidate key
```

> **Nối mạch:** Trong **정보처리기사 필기 2026 — Procedural Workbook**, **Normalization** nối từ **Functional phụ thuộc (dependency / 의존성) / Key** sang **SQL Aggregate**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Ở chặng này của **정보처리기사 필기 2026 — Procedural Workbook**, **SQL Aggregate** nối từ **Normalization** sang **Xung đột (conflict / 충돌) Serializability**, vì cơ chế trước tạo đầu vào cho bước sau.

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

Đây là logical lập luận (reasoning / 추론) mô hình (model / 모델), không khẳng định DBMS physically execute đúng thứ tự đó.

> **Nối mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Procedural Workbook**, **Xung đột (conflict / 충돌) Serializability** nối từ **SQL Aggregate** sang **CPU Scheduling**, vì cơ chế trước tạo đầu vào cho bước sau.

## Xung đột (conflict / 충돌) Serializability

```text
1. Tìm conflict pair trên cùng item
2. Ít nhất một write
3. Thêm precedence edge
4. Cycle? yes → not conflict-serializable
5. Acyclic → topological order cho equivalent serial order
```

> **Nối mạch:** Trong **정보처리기사 필기 2026 — Procedural Workbook**, **CPU Scheduling** nối từ **Xung đột (conflict / 충돌) Serializability** sang **Page Replacement**, vì cơ chế trước tạo đầu vào cho bước sau.

## CPU Scheduling

```text
1. Vẽ timeline/Gantt
2. Tính completion time
3. turnaround = completion - arrival
4. waiting = turnaround - burst
5. response = first_run - arrival
```

> **Nối mạch:** Ở chặng này của **정보처리기사 필기 2026 — Procedural Workbook**, **Page Replacement** nối từ **CPU Scheduling** sang **Subnetting**, vì cơ chế trước tạo đầu vào cho bước sau.

## Page Replacement

```text
1. Ghi state frame sau từng reference
2. Hit hay fault?
3. Nếu fault và full → chọn victim đúng policy
4. Update policy metadata
5. Đếm fault sau cùng
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **정보처리기사 필기 2026 — Procedural Workbook**, **Subnetting** nối từ **Page Replacement** sang **PERT/CPM**, vì cơ chế trước tạo đầu vào cho bước sau.

## Subnetting

```text
1. prefix → host bits
2. total addresses = 2^host_bits
3. mask
4. block size ở interesting octet
5. tìm boundary chứa IP
6. network / broadcast / usable range
```

> **Nối mạch:** Trong **정보처리기사 필기 2026 — Procedural Workbook**, **PERT/CPM** nối từ **Subnetting** sang phần giải thích tiếp theo, vì phần trước cung cấp điểm tựa cho chủ đề này.

## PERT/CPM

```text
PERT expected = (O + 4M + P)/6
CPM: tính path duration / earliest-latest time
Critical path: zero-slack path quyết định project duration trong model
```

---

# Final Check — không nhìn đáp án

Bạn chỉ được đánh dấu workbook hoàn thành khi có thể tự làm lại tối thiểu các dạng sau mà không cần nhớ con số cụ thể của ví dụ:

- Cyclomatic độ phức tạp (complexity / 복잡도);
- ngăn xếp (stack / 스택)/postfix;
- BFS/DFS;
- băm (hash / 해시) probing;
- tìm kiếm nhị phân (binary search / 이진 탐색) dấu vết (trace / 추적);
- attribute closure và candidate key;
- 2NF/3NF/BCNF lập luận (reasoning / 추론);
- phép nối (join / 조인)/NULL/GROUP BY/HAVING;
- xung đột (conflict / 충돌) serializability và isolation anomaly;
- FCFS/SJF/Round Robin;
- FIFO/LRU page replacement;
- IPv4 subnetting và longest-prefix match;
- C pointer/basic expression dấu vết (trace / 추적);
- Java overriding/động (dynamic / 동적) dispatch;
- Python tham chiếu (reference / 참조)/mutability;
- PERT và đường găng (critical path / 임계 경로);
- RAID sức chứa (capacity / 용량);
- RTO/RPO;
- threat → điều khiển (control / 제어) ánh xạ (mapping / 매핑);
- deadlock điều kiện (condition / 조건)/prevention.

Nếu một procedure chỉ làm được khi nhìn lại ví dụ, quay về drill tương ứng và thay số liệu tự tạo thêm ít nhất hai lần.

> **Bàn giao:** Sau **PERT/CPM**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
