# 정보처리기사 필기 2026 — Advanced Scenario Labs

> Đây là lớp luyện **reasoning nhiều bước**. Mỗi scenario được thiết kế để có nhiều khái niệm đúng cùng xuất hiện, nhưng bạn phải xác định **primary concept**, **mechanism**, **trade-off** và **bẫy wording**. Không xem phần phân tích trước khi tự trả lời.

---

# Môn 1 — 소프트웨어 설계

## Lab 1 — Requirement đúng nhưng sản phẩm vẫn thất bại

### Scenario

Stakeholder yêu cầu “hệ thống cho phép xuất báo cáo PDF”. Team viết spec đúng câu đó, code đúng spec, test pass. Sau release, người dùng nói họ thực ra cần CSV để import vào ERP; PDF gần như vô dụng.

### Tự trả lời

1. Verification có pass không?
2. Validation có pass không?
3. Sai ở phase nào của requirement engineering?
4. Traceability có tự giải quyết vấn đề này không?

### Phân tích

Verification có thể pass vì implementation đúng spec. Validation fail vì spec không phản ánh need thật.

Traceability chỉ giúp lần theo requirement → design → code → test; nếu requirement gốc sai thì traceability vẫn có thể hoàn hảo nhưng dẫn tới sai mục tiêu.

Root cause gần requirement elicitation/analysis/validation hơn là coding.

### Bẫy

Đừng chọn “unit test thiếu” chỉ vì sản phẩm không hữu ích. Đây là **right product vs product built right**.

---

## Lab 2 — Module dependency nhìn tưởng sạch nhưng vẫn coupling cao

### Scenario

`OrderService` chỉ gọi một method duy nhất:

```text
LegacyFacade.process(order, mode, retryFlag, regionCode, dbShard, debugFlag)
```

Team nói fan-out chỉ bằng 1 nên coupling thấp.

### Tự trả lời

1. Fan-out thấp có chứng minh coupling thấp không?
2. Những parameter nào có thể cho thấy control/external coupling?
3. Facade có tự động làm kiến trúc tốt không?

### Phân tích

Fan-out chỉ đo số dependency trực tiếp, không đo chất lượng dependency.

`mode`, `retryFlag`, `debugFlag` có thể là control coupling nếu caller điều khiển behavior nội bộ của callee.

`regionCode`, `dbShard` có thể leak infrastructure concern lên business layer.

Facade giảm số entry points nhưng có thể trở thành “god facade” nếu interface gom quá nhiều control detail.

### Insight

Metric structural không thay semantic analysis.

---

## Lab 3 — Strategy hay State?

### Scenario

Một shipping calculator có ba algorithm: `Normal`, `Express`, `International`. User hoặc policy engine chọn algorithm khi tạo shipment.

Một order khác có behavior thay đổi theo lifecycle `CREATED → PAID → SHIPPED → DELIVERED`.

### Tự trả lời

Pattern nào phù hợp từng case? Vì sao class diagram có thể trông giống nhau?

### Phân tích

Shipping algorithms → Strategy: policy/algorithm interchangeable.

Order lifecycle → State: behavior thay đổi theo internal state transition.

Cả hai có thể dùng interface + concrete implementations, nên không thể chọn pattern chỉ từ shape class diagram.

---

## Lab 4 — Adapter hay Facade hay Anti-corruption Layer?

### Scenario

Hệ thống mới dùng `Customer(id, name, email)`. Legacy CRM trả `CUST_NO`, `NM`, `MAIL_ADDR`, nhiều field khác và semantics khác đôi chút.

### Tự trả lời

1. Nếu chỉ đổi method/interface shape, pattern nào gần nhất?
2. Nếu cần translate cả model/semantics để domain mới không bị legacy model “nhiễm”, vấn đề sâu hơn là gì?
3. Facade có phải đáp án tốt nhất nếu câu hỏi nhấn “incompatible interface” không?

### Phân tích

Nếu chỉ interface mismatch → Adapter.

Nếu cần cô lập semantic model legacy khỏi domain mới, tư duy gần anti-corruption layer/domain boundary hơn, dù thuật ngữ này có thể ngoài trọng tâm đề.

Nếu đề nhấn subsystem complexity → Facade. Nếu nhấn mismatch → Adapter.

---

## Lab 5 — Retry-safe interface

### Scenario

Client gửi `POST /payments`, server charge thành công nhưng response bị mất. Client retry.

### Tự trả lời

1. Timeout có chứng minh server chưa xử lý không?
2. Idempotency key nên thuộc request identity hay session identity?
3. Unique constraint có thể đóng vai trò gì?
4. Transaction cần bao quanh những gì?

### Phân tích

Timeout chỉ nói client không nhận response trong thời gian chờ; server có thể đã commit.

Idempotency key nên đại diện logical operation. Server cần bảo đảm cùng key không tạo duplicate side effect.

Một design mạnh là lưu request identity + result trong cùng transaction boundary với side effect hoặc dùng invariant tương đương. Unique constraint giúp concurrent duplicate requests không cùng “thắng”.

---

# Môn 2 — 소프트웨어 개발

## Lab 6 — Chọn data structure từ operation pattern

### Scenario

Một service cần:

- insert event liên tục;
- luôn lấy event có priority nhỏ nhất;
- không cần iterate toàn bộ theo sorted order;
- không cần arbitrary lookup theo key.

### Tự trả lời

Chọn BST, hash table, queue hay min-heap?

### Phân tích

Min-heap phù hợp vì operation trọng tâm là insert + extract-min.

BST cũng có thể hỗ trợ min, nhưng heap trực tiếp tối ưu cho priority queue abstraction. Hash table không giữ ordering; FIFO queue không xét priority.

### Bẫy

Đừng chọn structure chỉ vì nó “nhanh” tổng quát. Chọn theo operation mix.

---

## Lab 7 — Binary search sai dù code nhìn đúng

### Scenario

Team dùng binary search trên array `[8, 3, 12, 1, 20]` và đôi khi không tìm thấy value tồn tại.

### Phân tích

Binary search dựa invariant rằng search space được ordered theo comparator tương thích. Không có ordering, bước loại bỏ nửa search space không hợp lệ.

Root cause không phải off-by-one trước tiên mà là violated precondition.

---

## Lab 8 — Coverage cao nhưng bug vẫn lọt

### Scenario

Một function có 100% statement coverage nhưng condition `a && b` chỉ được test với `(true,true)` và `(false,false)`.

### Tự trả lời

1. 100% statement coverage chứng minh điều gì?
2. Nó có chứng minh mọi branch/condition combination đã test không?
3. Test nào nên thêm?

### Phân tích

Statement coverage chỉ chứng minh mỗi statement đã execute ít nhất một lần.

Cần xét branch/condition coverage tùy mục tiêu. Cases `(true,false)` và `(false,true)` có thể phơi lộ logic bug bị statement coverage bỏ qua.

---

## Lab 9 — Regression hay Retest?

### Scenario

Bug: discount code `SAVE10` không áp dụng cho order trên 100,000 won. Dev sửa bug.

Team chạy:

- test đúng case `SAVE10 + 150,000`;
- test các code khác;
- test checkout không discount;
- test refund sau checkout.

### Phân tích

Case đầu là retest trực tiếp defect.

Các test còn lại là regression để xem fix có phá behavior liên quan không.

Một test session có thể chứa cả hai loại.

---

## Lab 10 — Package integrity nhưng source không đáng tin

### Scenario

Một installer tải về có SHA-256 đúng với hash đăng trên cùng website vừa bị compromise.

### Tự trả lời

Hash check đã bảo vệ điều gì? Điều gì vẫn thiếu?

### Phân tích

Hash giúp phát hiện mismatch giữa file và expected digest, nhưng nếu attacker kiểm soát cả file và digest thì authenticity không được đảm bảo.

Digital signature/trusted distribution chain giải bài identity/authenticity tốt hơn.

### Insight

Integrity check chỉ mạnh bằng trust source của expected value.

---

# Môn 3 — 데이터베이스 구축

## Lab 11 — Candidate key không nhìn từ FD bằng mắt

### Scenario

Relation:

```text
R(A,B,C,D,E)
```

FDs:

```text
A → B
B → C
CD → E
E → D
```

### Tự làm

Tìm một candidate key.

### Gợi ý

`A+ = {A,B,C}` chưa có D/E.

Thử `AD+`:

```text
A → B → C
C,D → E
```

Vậy `AD+ = {A,B,C,D,E}`.

Có bỏ A được không? `D+` không ra A/B/C.

Có bỏ D được không? `A+` không ra D/E.

`AD` là candidate key.

Nhưng vì `E → D`, thử `AE`:

A → B → C và E → D → từ C,D suy E vốn đã có.

`AE` cũng là candidate key.

### Insight

Một relation có thể có nhiều candidate keys. Đừng dừng ở superkey đầu tiên.

---

## Lab 12 — 3NF nhưng chưa BCNF

### Scenario

Relation `R(Student, Course, Instructor)` với FDs:

```text
(Student, Course) → Instructor
Instructor → Course
```

Candidate keys gồm `(Student, Course)` và `(Student, Instructor)`.

### Tự trả lời

`Instructor → Course` vi phạm BCNF không? 3NF thì sao?

### Phân tích

`Instructor` không phải superkey → vi phạm BCNF.

Nhưng `Course` là prime attribute vì nằm trong candidate key `(Student, Course)`, nên FD này có thể vẫn thỏa 3NF theo formal condition.

### Insight

Đây là kiểu case cho thấy 3NF và BCNF không đồng nghĩa.

---

## Lab 13 — Index đúng cột nhưng sai thứ tự

### Scenario

Query chính:

```sql
SELECT id, created_at
FROM orders
WHERE customer_id = ?
  AND created_at >= ?
ORDER BY created_at DESC
LIMIT 20;
```

Hai index:

```text
I1(created_at, customer_id)
I2(customer_id, created_at)
```

### Tự trả lời

Index nào thường tự nhiên hơn và vì sao?

### Phân tích

`I2(customer_id, created_at)` thường phù hợp hơn vì equality trên `customer_id` tạo một ordered range nhỏ theo `created_at`.

`I1` bắt đầu bằng time, có thể phải scan nhiều customer trong time range rồi filter.

DBMS optimizer/cardinality có thể làm quyết định cụ thể khác, nhưng đây là reasoning access-pattern cơ bản.

---

## Lab 14 — LEFT JOIN bị biến thành INNER JOIN ngoài ý muốn

### Scenario

```sql
SELECT c.id, o.id
FROM customer c
LEFT JOIN orders o
  ON o.customer_id = c.id
WHERE o.status = 'PAID';
```

Team kỳ vọng customer chưa có order vẫn xuất hiện.

### Phân tích

Unmatched row có `o.status = NULL`. `WHERE o.status='PAID'` loại row đó, nên semantics gần INNER JOIN cho condition này.

Nếu mục tiêu là giữ mọi customer và chỉ match paid orders:

```sql
LEFT JOIN orders o
  ON o.customer_id = c.id
 AND o.status = 'PAID'
```

### Insight

Vị trí predicate ảnh hưởng outer join semantics.

---

## Lab 15 — Lost update và optimistic concurrency

### Scenario

Row:

```text
account(id=1, balance=100, version=7)
```

T1 và T2 cùng đọc balance 100, version 7.

T1 muốn -20; T2 muốn -30.

### Tự thiết kế

Dùng optimistic versioning để tránh lost update.

### Phân tích

```sql
UPDATE account
SET balance = 80,
    version = 8
WHERE id = 1
  AND version = 7;
```

T1 update 1 row.

T2 sau đó:

```sql
UPDATE account
SET balance = 70,
    version = 8
WHERE id = 1
  AND version = 7;
```

update 0 row → phát hiện concurrent modification, phải retry/recompute trên state mới.

### Insight

Optimistic locking không “khóa” row trước; nó detect conflict khi write bằng version/invariant.

---

# Môn 4 — 프로그래밍 언어 활용

## Lab 16 — Mutex đúng nhưng production vẫn race

### Scenario

Một app có global in-memory counter và dùng mutex. Single instance test luôn đúng. Production chạy 8 instances sau load balancer và counter sai.

### Tự trả lời

Mutex đã bảo vệ gì? Vì sao chưa đủ?

### Phân tích

Mutex chỉ synchronize threads/process scope mà primitive đó chia sẻ được. 8 instances có memory riêng nên mỗi instance có mutex riêng.

Nếu invariant global giữa instances, cần shared coordination/state mechanism ở layer phù hợp: DB atomic update/transaction, distributed lock khi thật cần, hoặc redesign.

### Insight

Đúng mechanism ở sai scope vẫn sai invariant.

---

## Lab 17 — Round Robin quantum trade-off

### Scenario

Quantum giảm từ 50 ms xuống 1 ms.

### Tự trả lời

Response time và overhead có xu hướng gì?

### Phân tích

Quantum nhỏ thường cải thiện responsiveness/fairness ngắn hạn nhưng tăng context-switch overhead.

Nếu quantum quá lớn, Round Robin tiến gần FCFS cho CPU-bound jobs.

Không có quantum tối ưu universal; phụ thuộc workload và switch cost.

---

## Lab 18 — FIFO vs LRU khác victim nhưng fault count bằng nhau

### Scenario

Reference string ngắn cho cùng số page faults ở FIFO và LRU.

### Tự trả lời

Có kết luận hai algorithm tương đương không?

### Phân tích

Không. Same result trên một trace không chứng minh same policy. FIFO dùng insertion age; LRU dùng recency of access.

Cần nhìn mechanism, không chỉ count ở một sample.

---

## Lab 19 — TCP reliable nhưng API vẫn duplicate

### Scenario

TCP bảo đảm bytes ordered/retransmitted trong một connection. Tại sao payment API vẫn cần idempotency?

### Phân tích

Reliability transport không giải ambiguity application-level khi connection mất sau server commit nhưng trước khi client biết result. Client mở request mới/retry → logical operation có thể lặp.

TCP giải byte delivery semantics; idempotency giải business operation semantics.

---

## Lab 20 — Java reference type vs runtime type

### Scenario

```java
class A {
    void f() { System.out.print("A"); }
    void onlyA() {}
}
class B extends A {
    @Override void f() { System.out.print("B"); }
    void onlyB() {}
}
A x = new B();
```

### Tự trả lời

1. `x.f()` gọi gì?
2. `x.onlyB()` compile được không?
3. Vì sao?

### Phân tích

`x.f()` → `B.f()` qua dynamic dispatch.

`x.onlyB()` không accessible qua static/reference type `A` nếu không cast/typing khác.

Compile-time member availability và runtime overriding là hai stage reasoning khác nhau.

---

# Môn 5 — 정보시스템 구축 관리

## Lab 21 — RPO tốt nhưng RTO tệ

### Scenario

DB sync replication gần như zero data loss. Primary fail, nhưng failover manual cần 3 giờ.

Business requirement:

```text
RPO <= 1 minute
RTO <= 15 minutes
```

### Phân tích

RPO có thể đạt, RTO fail.

Replication freshness không tự giải recovery orchestration.

Need automated failover, tested runbook, dependency recovery và operational readiness tùy architecture.

---

## Lab 22 — Backup đầy đủ nhưng restore không được

### Scenario

Team backup mỗi giờ nhưng chưa bao giờ restore test. Khi incident xảy ra, file backup corrupt từ 3 tuần trước.

### Tự trả lời

Backup policy đã thiếu dimension nào?

### Phân tích

Backup không hoàn thành khi “job success”. Cần restore verification, integrity monitoring, retention, isolation và recovery drill.

Availability/recovery là end-to-end capability.

---

## Lab 23 — RAID 5 không cứu ransomware

### Scenario

Server dùng RAID 5. Ransomware encrypt filesystem hợp lệ qua OS.

### Phân tích

RAID parity bảo vệ một số physical disk failures, không bảo vệ logical overwrite/encryption. Mọi disk trong array sẽ chứa encrypted blocks hợp lệ.

Need backup/versioning/isolation/security controls khác.

---

## Lab 24 — Authentication đúng, authorization sai

### Scenario

User đăng nhập hợp lệ. API:

```http
GET /invoice/12345
```

Server kiểm token valid nhưng không kiểm invoice 12345 thuộc user nào. User đổi ID và đọc invoice người khác.

### Phân tích

Authentication pass; object-level authorization fail.

TLS cũng không giải root cause vì attacker là user hợp lệ trong protected channel.

Đây là lý do phải phân identity verification khỏi permission decision.

---

## Lab 25 — Defense in depth nhưng root cause vẫn tồn tại

### Scenario

App dùng WAF và firewall nhưng query xây bằng string concat:

```text
"SELECT * FROM users WHERE name='" + input + "'"
```

### Tự trả lời

WAF có làm code an toàn không? Root control là gì?

### Phân tích

WAF có thể block một số pattern nhưng bypass/false positive/encoding variation vẫn tồn tại.

Root control là parameterized query/prepared statement để data không thay đổi SQL structure.

Defense in depth tốt, nhưng perimeter control không thay code correctness.

---

# Cross-subject mega labs

## Mega Lab A — Checkout endpoint

### Scenario

Requirement:

```text
User đặt order.
Không oversell.
Không charge hai lần.
95% request < 2s.
System chịu mất một app instance mà không gián đoạn đáng kể.
```

### Hãy nối 5 môn

**Môn 1:** functional/non-functional requirement, sequence/interface design, idempotency contract.

**Môn 2:** test boundary, regression, integration test cho retry/concurrent order.

**Môn 3:** transaction, atomic stock update, unique key, index.

**Môn 4:** concurrent requests, process/thread, TCP timeout ambiguity.

**Môn 5:** load balancing, HA, authentication/authorization, monitoring/recovery.

### Câu hỏi sâu

1. Mutex local có đủ cho stock không?
2. Unique idempotency key và transaction phải phối hợp thế nào?
3. Index nào hỗ trợ lookup request identity?
4. Performance requirement phải biến thành test/metric gì?
5. Nếu app instance chết sau DB commit nhưng trước response, client behavior phải thế nào?

---

## Mega Lab B — Reporting system chậm

### Scenario

Report query join 8 bảng normalized, chạy 45 giây. Team đề xuất:

- denormalize mọi table;
- thêm index vào mọi column;
- tăng RAM;
- cache report 24 giờ.

### Tư duy đúng

Không chọn solution trước khi phân tích access pattern và bottleneck.

Cần:

1. xác định requirement về freshness/latency;
2. xem execution plan/cardinality/index;
3. phân biệt OLTP vs analytics workload;
4. cân nhắc summary/materialized structure;
5. hiểu consistency cost của cache/denormalization;
6. đo thay vì đoán.

### Bẫy

Mọi proposed solution đều có thể hợp lý trong một context, nhưng không cái nào universal.

---

## Mega Lab C — Incident sau deployment

### Scenario

Version mới deploy 10:00. 10:05 error rate tăng mạnh. DB CPU bình thường, app CPU tăng 95%, GC liên tục. Rollback artifact lại bị nhầm version.

### Nối kiến thức

- configuration management/release artifact;
- application memory behavior;
- observability;
- rollback plan;
- version identification/baseline;
- validation sau deploy.

### Root learning

Một incident production có thể bắt đầu là code/performance issue nhưng recovery thất bại vì configuration management.

---

# Cách tự chấm scenario

Mỗi lab chấm 0–4:

```text
0 = không biết bắt đầu
1 = nhớ keyword nhưng không giải thích mechanism
2 = chọn đúng concept nhưng reasoning thiếu layer/scope
3 = giải đúng mechanism + phân biệt distractor
4 = giải đúng + nêu trade-off + liên kết sang môn khác
```

Mục tiêu trước full mock:

```text
25 labs cơ bản: trung bình >= 3
3 mega labs: mỗi lab >= 3
không có lab nào = 0
```

Nếu score 1 vì nhầm hai concept, quay lại `11-high-risk-confusion-atlas.md`.

Nếu score 1–2 vì không làm được calculation/trace, quay lại `08-procedural-workbook.md`.

Nếu score thấp vì không hiểu concept gốc, quay lại deep-dive môn tương ứng.