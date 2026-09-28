# 정보처리기사 필기 2026 — Mixed Exam Drills

> Đây là bộ câu hỏi **tự viết mới**, không sao chép 기출. Mục tiêu là luyện chuyển ngữ cảnh (context / 맥락) nhanh giữa 5 môn và phát hiện lỗ hổng thật sự. Làm toàn bộ câu trước, sau đó mới xem đáp án.

## Cách làm

Mỗi câu nên trả lời trong khoảng 60–90 giây. Với câu tính/mã (code / 코드), ghi bước suy luận ra giấy. Sau khi chấm, phân loại lỗi:

- `coverage hole`: chưa học chủ đề;
- `confusion pair`: biết cả hai nhưng nhầm ranh giới;
- `procedural error`: hiểu lý thuyết nhưng tính/dấu vết (trace / 추적) sai;
- `term recognition`: không nhận ra thuật ngữ Hàn;
- `careless reading`: đọc thiếu điều kiện.

---

# Phần A — 소프트웨어 설계

## Q1

Một yêu cầu (requirement / 요구사항) ghi: “Người dùng có thể khóa tài khoản và thao tác phải hoàn thành trong 1 giây.” Phân loại đúng nhất là gì?

A. Cả hai đều functional yêu cầu (requirement / 요구사항)
B. Khóa tài khoản là functional, 1 giây là non-functional
C. Khóa tài khoản là non-functional, 1 giây là functional
D. Cả hai đều non-functional

## Q2

Muốn thể hiện thứ tự message giữa `Controller`, `Service`, `Repository` theo thời gian, diagram phù hợp nhất là:

A. Use trường hợp (case / 사례) Diagram
B. trạng thái (state / 상태) Diagram
C. chuỗi (sequence / 시퀀스) Diagram
D. triển khai (deployment / 배포) Diagram

## Q3

`Order` sở hữu `OrderLine`; nếu thứ tự (order / 순서) bị xóa thì OrderLine không còn ý nghĩa tồn tại độc lập. Quan hệ phù hợp nhất là:

A. phụ thuộc (dependency / 의존성)
B. Aggregation
C. Composition
D. Generalization

## Q4

Mô-đun (module / 모듈) A truyền toàn bộ đối tượng (object / 객체) `Customer` sang B nhưng B chỉ cần `customerId`. Đây gần nhất với:

A. dữ liệu (data / 데이터) coupling
B. Stamp coupling
C. Content coupling
D. dùng chung (common / 공통) coupling

## Q5

Một hệ thống cần thay nhiều thuật toán tính discount tại thời gian chạy (runtime / 런타임) nhưng trạng thái (state / 상태) nội bộ của đối tượng (object / 객체) không tự quyết định thuật toán (algorithm / 알고리즘). mẫu (pattern / 패턴) phù hợp nhất:

A. trạng thái (state / 상태)
B. chiến lược (strategy / 전략)
C. Observer
D. Singleton

## Q6

Một subsystem phức tạp có nhiều lớp (class / 클래스) nhưng máy khách (client / 클라이언트) chỉ cần một API đơn giản ở phía trước. mẫu (pattern / 패턴) phù hợp nhất:

A. Adapter
B. Decorator
C. Facade
D. Prototype

## Q7

Trong Scrum, sản phẩm tạo ra (artifact / 산출물) chứa phần việc được chọn cho Sprint cùng plan để đạt Sprint Goal là:

A. sản phẩm (product / 제품) Backlog
B. Sprint Backlog
C. Increment
D. Burndown Chart

## Q8

Point-to-Point tích hợp (integration / 통합) bắt đầu gây khó quản lý chủ yếu khi:

A. Chỉ có một hệ thống duy nhất
B. Số lượng hệ thống (system / 시스템) và liên kết (connection / 연결) tăng mạnh
C. Không có cơ sở dữ liệu (database / 데이터베이스)
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

Trong đồ thị (graph / 그래프) không trọng số, thuật toán nền tảng để tìm shortest đường dẫn (path / 경로) theo số cạnh từ một nguồn (source / 소스) là:

A. DFS
B. BFS
C. Prim
D. Kruskal

## Q11

Quick Sort có độ phức tạp (complexity / 복잡도) worst-case điển hình là:

A. O(1)
B. O(log n)
C. O(n log n)
D. O(n²)

## Q12

Tuyến tính (linear / 선형) Probing trong bảng băm (hash table / 해시 테이블) dễ gặp hiện tượng:

A. Deadlock
B. Primary clustering
C. Phantom read
D. Starvation

## Q13

Trong Top-down kiểm thử tích hợp (integration test / 통합 테스트), mô-đun (module / 모듈) con chưa hoàn thành thường được thay bằng:

A. Driver
B. Stub
C. Oracle
D. Harness

## Q14

Technique nào thuộc Black-box Testing?

A. Statement Coverage
B. Branch Coverage
C. ranh giới (boundary / 경계) giá trị (value / 값) phân tích (analysis / 분석)
D. đường dẫn (path / 경로) Coverage

## Q15

`V(G) = E - N + 2` trong điều khiển (control / 제어) luồng (flow / 흐름) đồ thị (graph / 그래프) một thành phần (component / 컴포넌트) dùng để tính:

A. hàm (function / 함수) điểm (point / 지점)
B. Cyclomatic độ phức tạp (complexity / 복잡도)
C. Halstead Volume
D. phản hồi (response / 응답) thời gian (time / 시간)

## Q16

Chỉ số (metric / 지표) nào đo số yêu cầu (request / 요청)/giao dịch (transaction / 트랜잭션) xử lý trong một đơn vị thời gian?

A. phản hồi (response / 응답) thời gian (time / 시간)
B. độ trễ (latency / 지연 시간)
C. thông lượng (throughput / 처리량)
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

Relational algebra thao tác (operation / 연산) chọn một số row theo predicate là:

A. Projection
B. Selection
C. Division
D. Cartesian sản phẩm (product / 제품)

## Q19

Quan hệ (relation / 관계) có key `(StudentId, CourseId)`, nhưng `StudentName` chỉ phụ thuộc `StudentId`. Đây là:

A. Transitive phụ thuộc (dependency / 의존성)
B. Partial phụ thuộc (dependency / 의존성)
C. Multivalued phụ thuộc (dependency / 의존성)
D. phép nối (join / 조인) phụ thuộc (dependency / 의존성)

## Q20

BCNF yêu cầu điều gì với non-trivial functional phụ thuộc (dependency / 의존성) `X → Y`?

A. Y phải là foreign key
B. X phải là superkey
C. X phải là primary key duy nhất
D. Y phải là non-prime attribute

## Q21

Truy vấn (query / 쿼리) thường xuyên dùng phạm vi (range / 범위) điều kiện (condition / 조건) `created_at BETWEEN ...`. chỉ mục (index / 인덱스) nào tự nhiên hơn?

A. băm (hash / 해시) chỉ mục (index / 인덱스)
B. B+cây (tree / 트리) chỉ mục (index / 인덱스)
C. Bitmap luôn luôn tốt hơn
D. Không chỉ mục (index / 인덱스) nào hỗ trợ phạm vi (range / 범위)

## Q22

Điều kiện `AVG(salary) > 5000` khi dùng `GROUP BY department_id` nên đặt ở:

A. WHERE
B. HAVING
C. thứ tự (order / 순서) BY
D. VALUES

## Q23

T1 đọc một row hai lần. Giữa hai lần, T2 cập nhật (update / 업데이트) row đó và lần ghi nhận (commit / 커밋). T1 thấy hai giá trị (value / 값) khác nhau. Đây là:

A. Dirty Read
B. Non-repeatable Read
C. Phantom Read
D. Lost cập nhật (update / 업데이트)

## Q24

Trong khôi phục (recovery / 복구), thao tác áp lại thay đổi của giao dịch (transaction / 트랜잭션) đã lần ghi nhận (commit / 커밋) nhưng chưa phản ánh đầy đủ trên disk là:

A. UNDO
B. REDO
C. quay lui (rollback / 롤백) SAVEPOINT
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

Nếu `Child` override `run()`, phương thức (method / 메서드) nào chạy?

A. Parent.run() luôn luôn
B. Child.run() qua động (dynamic / 동적) dispatch
C. Compile lỗi (error / 오류)
D. Tùy trường dữ liệu (field / 필드) của Parent

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
D. lỗi (error / 오류)

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

Một tiến trình (process / 프로세스) đang chờ dữ liệu từ disk I/O thường ở trạng thái (state / 상태):

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
C. DNS máy chủ (server / 서버)
D. Modem luôn luôn

---

# Phần E — 정보시스템 구축 관리

## Q33

Trong PERT, O=2, M=5, P=14. Expected thời gian (time / 시간) là:

A. 5
B. 6
C. 7
D. 8

## Q34

Đường găng (critical path / 임계 경로) trong mạng (network / 네트워크) dự án (project / 프로젝트) cơ bản là:

A. đường dẫn (path / 경로) có ít activity nhất
B. đường dẫn (path / 경로) có nhiều activity nhất
C. đường dẫn (path / 경로) có tổng duration dài nhất
D. đường dẫn (path / 경로) có chi phí (cost / 비용) thấp nhất

## Q35

RAID nào dùng dual parity và có thể chịu hai disk thất bại (failure / 실패) trong mô hình chuẩn?

A. RAID 0
B. RAID 1
C. RAID 5
D. RAID 6

## Q36

RPO trả lời câu hỏi nào?

A. dịch vụ (service / 서비스) được phép down bao lâu?
B. Chấp nhận mất tối đa bao nhiêu dữ liệu tính theo thời gian?
C. Bao lâu phải đổi password?
D. Bao nhiêu máy chủ (server / 서버) cần chạy?

## Q37

Defense chính chống SQL Injection là:

A. Chỉ đổi tên bảng (table / 테이블)
B. Parameterized truy vấn (query / 쿼리) / prepared statement
C. Chỉ dùng HTTPS
D. Chỉ encode HTML đầu ra (output / 출력)

## Q38

Một comment độc hại được lưu DB rồi kết xuất (render / 렌더링) cho mọi người dùng (user / 사용자), chạy JavaScript trong trình duyệt (browser / 브라우저). Đây gần nhất là:

A. Stored XSS
B. CSRF
C. SQL Injection
D. Buffer Overflow

## Q39

Kiểm soát truy cập (access control / 접근 제어) gán permission cho Role, sau đó gán người dùng (user / 사용자) vào Role là:

A. DAC
B. MAC
C. RBAC
D. ABAC bắt buộc

## Q40

Hệ thống (system / 시스템) dùng firewall để lọc mạng (network / 네트워크) traffic, còn thiết bị inline phân tích traffic và chủ động khối (block / 블록) attack là:

A. IDS
B. IPS
C. DNS
D. NTP

---

# Đáp án và giải thích

## A — Software thiết kế (design / 설계)

**Q1: B.** năng lực (capability / 역량) “khóa tài khoản” là functional; giới hạn 1 giây là hiệu năng (performance / 성능) ràng buộc (constraint / 제약조건) nên non-functional.

**Q2: C.** chuỗi (sequence / 시퀀스) Diagram mô tả lifeline/message theo thứ tự thời gian.

**Q3: C.** Composition dùng khi part phụ thuộc vòng đời whole.

**Q4: B.** Truyền cả cấu trúc (structure / 구조)/đối tượng (object / 객체) khi callee chỉ cần một phần là Stamp Coupling; dữ liệu (data / 데이터) Coupling sẽ truyền đúng dữ liệu (data / 데이터) cần thiết.

**Q5: B.** chiến lược (strategy / 전략) thay thuật toán (algorithm / 알고리즘) có thể chọn/thay thời gian chạy (runtime / 런타임). trạng thái (state / 상태) phù hợp khi hành vi (behavior / 동작) đổi do trạng thái nội bộ (internal state / 내부 상태).

**Q6: C.** Facade tạo giao diện (interface / 인터페이스) đơn giản phía trước subsystem phức tạp.

**Q7: B.** Sprint Backlog chứa selected sản phẩm (product / 제품) Backlog Items và plan cho Sprint.

**Q8: B.** Với N hệ thống (system / 시스템), số direct liên kết (connection / 연결) có thể tăng nhanh và coupling/maintenance trở nên phức tạp.

## B — Software Development

**Q9: B.** Inorder của BST cho key tăng dần nếu key distinct và thứ tự (ordering / 순서) chuẩn.

**Q10: B.** BFS đi theo tầng (layer / 계층) nên tìm shortest đường dẫn (path / 경로) theo số cạnh trong unweighted đồ thị (graph / 그래프).

**Q11: D.** Quick Sort average thường O(n log n), worst O(n²) nếu partition rất lệch.

**Q12: B.** tuyến tính (linear / 선형) Probing tạo cluster liên tiếp gọi là primary clustering.

**Q13: B.** Top-down cần Stub thay mô-đun (module / 모듈) con; Bottom-up dùng Driver thay caller cấp trên.

**Q14: C.** ranh giới (boundary / 경계) giá trị (value / 값) phân tích (analysis / 분석) là black-box technique dựa đầu vào (input / 입력) lĩnh vực (domain / 도메인)/specification.

**Q15: B.** Đây là công thức McCabe Cyclomatic độ phức tạp (complexity / 복잡도) với một connected thành phần (component / 컴포넌트).

**Q16: C.** thông lượng (throughput / 처리량) đo lượng công việc (work / 작업) xử lý trên đơn vị thời gian.

## C — cơ sở dữ liệu (database / 데이터베이스)

**Q17: B.** Candidate Key là Super Key minimal: bỏ bất kỳ attribute nào cũng mất uniqueness.

**Q18: B.** Selection chọn row; Projection chọn column.

**Q19: B.** `StudentName` phụ thuộc chỉ một phần composite key nên là partial phụ thuộc (dependency / 의존성).

**Q20: B.** BCNF yêu cầu determinant X của mọi non-trivial FD phải là superkey.

**Q21: B.** B+cây (tree / 트리) giữ thứ tự (ordering / 순서) và hỗ trợ phạm vi (range / 범위) scan tự nhiên; băm (hash / 해시) phù hợp equality hơn.

**Q22: B.** Aggregate điều kiện (condition / 조건) sau grouping đặt ở HAVING.

**Q23: B.** Cùng row đọc lại thấy giá trị (value / 값) khác sau committed cập nhật (update / 업데이트) là Non-repeatable Read.

**Q24: B.** REDO áp lại committed thay đổi (change / 변경); UNDO đảo uncommitted thay đổi (change / 변경).

## D — Programming ngôn ngữ (language / 언어) / OS / mạng (network / 네트워크)

**Q25: C.** `p` trỏ x; dereference rồi cộng 2 làm x từ 3 thành 5.

**Q26: B.** Overridden instance phương thức (method / 메서드) được chọn theo actual đối tượng (object / 객체) qua động (dynamic / 동적) dispatch.

**Q27: B.** `a` và `b` bind cùng danh sách (list / 목록); `append` mutate danh sách (list / 목록) chung.

**Q28: B.** Shortest Remaining thời gian (time / 시간) First là preemptive SJF.

**Q29: C.** FIFO có thể xuất hiện Belady's Anomaly.

**Q30: C.** Chờ I/O/sự kiện (event / 이벤트) là Blocked/Waiting, không phải Ready.

**Q31: C.** `/26` còn 6 bit host, tổng `2^6 = 64` address.

**Q32: B.** Switch L2 forward frame theo MAC bảng (table / 테이블); router tuyến (route / 경로) packet theo IP.

## E — thông tin (information / 정보) hệ thống (system / 시스템) Management

**Q33: B.** `(2 + 4×5 + 14)/6 = 36/6 = 6`.

**Q34: C.** đường găng (critical path / 임계 경로) là đường dẫn (path / 경로) có tổng duration dài nhất và quyết định dự án (project / 프로젝트) duration tối thiểu trong mô hình (model / 모델) cơ bản.

**Q35: D.** RAID 6 dùng dual parity và chịu hai disk thất bại (failure / 실패) theo mô hình (model / 모델) chuẩn.

**Q36: B.** RPO là mức mất dữ liệu (data / 데이터) tối đa chấp nhận được theo thời gian; RTO là downtime/khôi phục (recovery / 복구) thời gian (time / 시간) mục tiêu (objective / 목표).

**Q37: B.** Parameter binding tách truy vấn (query / 쿼리) cấu trúc (structure / 구조) khỏi người dùng (user / 사용자) dữ liệu (data / 데이터) và là defense chính chống SQL Injection.

**Q38: A.** Payload được lưu rồi phát cho người dùng (user / 사용자) khác là Stored XSS.

**Q39: C.** Permission → Role → người dùng (user / 사용자) là Role-Based kiểm soát truy cập (access control / 접근 제어).

**Q40: B.** IDS chủ yếu detect/alert; IPS hoạt động inline để khối (block / 블록)/prevent theo chính sách (policy / 정책)/detection.

---

# Cách đọc kết quả

## 36–40 đúng

Coverage cơ bản khá ổn. Không dừng ở đây: chuyển sang đề timed và tập trung câu sai hiếm/chi tiết.

## 30–35 đúng

Có nền nhưng vẫn còn nhiều confusion/procedural hole. Lọc các câu sai theo môn và quay lại deep-dive tương ứng.

## 24–29 đúng

Chưa an toàn vì trung bình lý thuyết gần vùng pass nhưng chỉ cần một môn yếu là có nguy cơ 과락. Ưu tiên môn có tỷ lệ đúng thấp nhất.

## Dưới 24 đúng

Không nên học bằng đề ngẫu nhiên tiếp. Quay lại Master Guide + 5 deep-dive, lấp coverage trước rồi mới tăng số lượng mock kiểm thử (test / 테스트).

## Per-subject quy tắc (rule / 규칙)

Mỗi môn trong bộ này có 8 câu. Nếu một môn đúng dưới 5/8, xem môn đó là **rủi ro (risk / 위험) area** dù tổng điểm cao. Đây là proxy luyện tập, không phải quy đổi trực tiếp sang điểm Q-Net, nhưng giúp tránh việc điểm mạnh che lấp một môn yếu.
