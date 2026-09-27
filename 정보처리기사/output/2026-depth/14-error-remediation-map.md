# 정보처리기사 필기 2026 — Error Remediation Map

> Mục tiêu của file này là biến mỗi câu sai thành một **đường sửa lỗi cụ thể**. Không ghi “sai câu 37” rồi đọc lại toàn bộ môn. Hãy xác định loại lỗi, concept gốc, file cần quay lại và dạng bài phải làm lại.

---

# 1. Error taxonomy

Mỗi câu sai chỉ gán **một primary error code** đầu tiên. Nếu có lỗi phụ, ghi sau.

## COV — Coverage Hole

Bạn chưa từng học hoặc không nhận ra concept.

Ví dụ:

```text
Không biết BCNF là gì.
Không biết RPO là gì.
Không biết Stub/Driver.
```

### Cách sửa

Quay lại deep-dive môn tương ứng, đọc từ explanation gốc tới example, sau đó tự giải thích closed-book.

Không sửa COV bằng cách học riêng đáp án của câu vừa sai.

---

## CON — Confusion Error

Bạn biết cả hai concept nhưng nhầm ranh giới.

Ví dụ:

```text
Validation ↔ Verification
Strategy ↔ State
3NF ↔ BCNF
RTO ↔ RPO
IDS ↔ IPS
```

### Cách sửa

Quay lại `11-high-risk-confusion-atlas.md`.

Viết một câu:

```text
A khác B ở ________.
```

Sau đó tự tạo một scenario mà A đúng và một scenario mà B đúng.

---

## PRO — Procedural Error

Biết lý thuyết nhưng không thực hiện được các bước tính/tracing.

Ví dụ:

```text
sai subnet
sai Round Robin timeline
sai attribute closure
sai conflict graph
sai page replacement
sai pointer trace
```

### Cách sửa

Quay lại `08-procedural-workbook.md`.

Làm lại procedure với **hai bộ số liệu tự đổi**, không học đáp số cũ.

---

## LAY — Layer/Scope Error

Chọn mechanism đúng nhưng ở sai abstraction layer hoặc sai phạm vi bảo vệ.

Ví dụ:

```text
TLS để giải authorization
mutex local để bảo vệ 10 server instances
RAID để giải backup
normalization để giải mọi query chậm
```

### Cách sửa

Quay lại `07-cross-subject-connection-map.md` và `12-advanced-scenario-labs.md`.

Tự trả lời:

```text
Mechanism này bảo vệ layer nào?
Invariant thật nằm ở layer nào?
```

---

## TERM — Korean Term Recognition

Bạn biết concept bằng English/Vietnamese nhưng không nhận ra wording tiếng Hàn.

### Cách sửa

Quay lại `13-korean-term-bridge.md`.

Luyện ba chiều:

```text
Korean → English
English → Korean
Korean → mechanism
```

Không chỉ dịch nghĩa.

---

## READ — Reading / Polarity Error

Sai vì đọc nhầm:

```text
옳지 않은 것
해당하지 않는 것
가장 적절한 것
주된 목적
```

hoặc bỏ sót `NOT`, unit, arrival time, prefix length.

### Cách sửa

Không cần đọc lại cả chapter.

Tạo checklist trước khi chọn đáp án:

```text
1. Câu đang hỏi đúng hay sai?
2. Hỏi definition, purpose, mechanism hay exception?
3. Có từ mạnh: 항상/반드시/완전히 không?
4. Có điều kiện số học/unit/prefix không?
```

---

## CAL — Arithmetic Error

Procedure đúng nhưng tính nhầm số.

### Cách sửa

Tách calculation khỏi conceptual reasoning.

Viết intermediate state; không tính mental quá nhiều trong scheduling/subnet/page replacement.

---

## MEM — Fragile Memorization

Bạn nhớ câu cũ nhưng khi wording đổi thì không nhận ra.

Dấu hiệu:

```text
"Tôi nhớ đáp án là B nhưng không giải thích được vì sao."
```

### Cách sửa

Quay về explanation và scenario, không làm thêm 20 câu giống hệt.

---

# 2. Remediation map — Môn 1

| Nếu sai ở vùng | Primary check | Quay lại |
|---|---|---|
| Functional vs Non-functional | capability vs quality/constraint | `01-software-design-depth.md`, Confusion Atlas §1.2 |
| Verification vs Validation | đúng spec vs đúng nhu cầu | Confusion Atlas §1.1, Scenario Lab 1 |
| DFD | data flow hay control flow | Deep Dive §Structured Analysis, Confusion Atlas §1.3 |
| UML diagram | câu hỏi muốn quan sát gì | Deep Dive UML, Term Bridge UML |
| Aggregation/Composition | lifecycle ownership | Confusion Atlas §1.5 |
| Cohesion | relationship bên trong module | Deep Dive Module Independence |
| Coupling | dependency giữa modules | Deep Dive + Confusion Atlas §1.7–1.8 |
| Fan-in/Fan-out | count dependency, không phải quality | Scenario Lab 2 |
| SOLID | symptom của design problem | Deep Dive SOLID + Atlas §1.9–1.10 |
| Strategy/State | source của behavior variation | Atlas §1.11 + Lab 3 |
| Adapter/Facade | interface mismatch vs complexity | Atlas §1.12 + Lab 4 |
| Decorator/Proxy | add behavior vs access control | Atlas §1.13 |
| Factory Method/Abstract Factory | one creation path vs product family | Atlas §1.14 |
| UI artifacts | skeleton/visual/interaction | Atlas §1.15 |
| Interface retry | network uncertainty + idempotency | Connection Map §3, Lab 5 |

### Gate để đóng lỗi Môn 1

Không đóng lỗi chỉ vì đọc lại. Phải tạo được một câu mới có distractor gần concept vừa nhầm.

---

# 3. Remediation map — Môn 2

| Nếu sai ở vùng | Primary check | Quay lại |
|---|---|---|
| Stack/Postfix | pop order | Workbook Drill 2 |
| BFS/DFS | frontier policy | Workbook Drill 3, Atlas §2.2 |
| Heap/BST | operation cần tối ưu | Atlas §2.3, Lab 6 |
| Binary Search | sorted precondition | Workbook Drill 5, Lab 7 |
| Hash collision | probing/clustering | Workbook Drill 4 |
| Complexity | worst/average/space | Deep Dive Algorithms |
| Stub/Driver | ai giả caller/callee | Atlas §2.6 |
| Black/White box | external behavior vs internal path | Atlas §2.7 |
| Boundary/Equivalence | edge vs partition | Atlas §2.8 |
| Coverage | statement/branch/path | Lab 8 |
| Retest/Regression | defect-specific vs collateral | Atlas §2.9 + Lab 9 |
| Alpha/Beta | internal controlled vs external users | Atlas §2.10 |
| Version/CM | VCS subset của CM | Atlas §2.11 |
| Build/Package/Release | lifecycle artifact | Atlas §2.12 |
| Checksum/Signature | content match vs authenticity | Lab 10 |

### Gate

Với algorithm/data structure error, phải trace state từng bước. Với testing error, phải tự viết một test case làm rõ ranh giới.

---

# 4. Remediation map — Môn 3

| Nếu sai ở vùng | Primary check | Quay lại |
|---|---|---|
| Candidate key | closure + minimality | Workbook Drill 6, Lab 11 |
| Super/Candidate/Primary | uniqueness vs minimality vs selected key | Atlas §3.1–3.2 |
| Selection/Projection | row vs column | Atlas §3.3 |
| 2NF | partial dependency | Workbook Drill 7 |
| 3NF | transitive/formal condition | Workbook Drill 8 |
| 3NF/BCNF | determinant + prime attribute | Atlas §3.5, Lab 12 |
| Index | access pattern + key order | Connection Map §4.2, Lab 13 |
| Selectivity/Cardinality | fraction vs distinct/row context | Atlas §3.8 |
| WHERE/HAVING | before/after grouping | Workbook Drill 9 |
| LEFT JOIN | preserved side + NULL | Workbook Drill 10, Lab 14 |
| COUNT NULL | COUNT(*) vs COUNT(col) | Atlas §3.10 |
| Dirty/NRR/Phantom | uncommitted/value/set | Atlas §3.13 |
| Lost Update | concurrent overwrite | Lab 15 |
| Serializability | precedence graph cycle | Workbook Drill 11 |
| Deadlock | resource wait cycle | Connection Map §8 |
| Recovery | undo/redo/log/checkpoint | Atlas §3.16–3.17 |
| Migration | validation/reconciliation | Coverage Audit Ch.14 |

### Gate

DB procedural lỗi chỉ đóng khi làm được **một ví dụ mới tự tạo**: closure, normalization, SQL result hoặc schedule.

---

# 5. Remediation map — Môn 4

| Nếu sai ở vùng | Primary check | Quay lại |
|---|---|---|
| Process/Thread | address space/resource sharing | Atlas §4.1 |
| Concurrency/Parallelism | overlapping vs simultaneous | Atlas §4.2 |
| Mutex/Semaphore | ownership vs permits | Atlas §4.3 |
| Race/Deadlock | wrong result vs no progress | Atlas §4.4 |
| Deadlock strategy | prevention/avoidance/detection | Workbook Drill 30 |
| FCFS | timeline first | Workbook Drill 13 |
| SJF | shortest burst + starvation | Workbook Drill 14 |
| RR | quantum + rotation | Workbook Drill 15, Lab 17 |
| Metrics | waiting/turnaround/response | Atlas §4.7 |
| FIFO/LRU | insertion age vs recency | Workbook Drill 16–17 |
| Page Fault/Thrashing | event vs systemic condition | Atlas §4.10 |
| Subnet | host bits + block boundary | Workbook Drill 18–19,34 |
| Routing | longest prefix | Workbook Drill 20 |
| TCP/UDP | stream reliability vs datagram | Atlas §4.11 |
| TCP/idempotency | transport vs business semantics | Lab 19 |
| C pointer | address/reference state | Workbook Drill 21–22 |
| Java dispatch | compile-time type vs runtime method | Workbook Drill 23, Lab 20 |
| Python alias | same mutable object | Workbook Drill 24 |
| Multi-instance sync | scope của mutex | Lab 16 |

### Gate

Với code/OS/network, phải viết state table hoặc timeline. Không chấp nhận “đọc và thấy hiểu”.

---

# 6. Remediation map — Môn 5

| Nếu sai ở vùng | Primary check | Quay lại |
|---|---|---|
| Risk/Issue | future uncertainty vs existing problem | Atlas §5.2 |
| PERT | formula | Workbook Drill 25 |
| Critical Path | path duration/slack | Workbook Drill 26 |
| RAID | level/capacity/failure model | Workbook Drill 27 |
| RAID/Backup | physical redundancy vs recoverable copy | Atlas §5.5, Lab 23 |
| Replication/Backup | current copy vs recovery history | Atlas §5.6 |
| HA/DR | routine failover vs major recovery | Atlas §5.7 |
| RTO/RPO | restore time vs data-loss window | Workbook Drill 28, Lab 21 |
| Backup reliability | restore test | Lab 22 |
| Scaling | node bigger vs more nodes | Atlas §5.9 |
| VM/Container | guest kernel vs shared host kernel | Atlas §5.10 |
| IaaS/PaaS/SaaS | responsibility boundary | Atlas §5.11 |
| AuthN/AuthZ | identity vs permission | Atlas §5.12, Lab 24 |
| Hash/Encryption | one-way digest vs reversible confidentiality | Atlas §5.13 |
| SQLi/XSS | sink/root cause | Workbook Drill 29, Atlas §5.15 |
| Firewall/WAF | network rule vs HTTP app semantics | Atlas §5.16 |
| IDS/IPS | detect vs inline prevent | Atlas §5.17 |
| TLS/VPN | application channel vs network tunnel | Atlas §5.18 |
| Threat/Vulnerability/Risk | actor/event vs weakness vs contextual loss | Atlas §5.19 |
| Defense in depth | root control vs additional layer | Lab 25 |

---

# 7. Score-driven remediation

## Nếu một môn < 8/20

Đây là **과락 risk**, không chỉ “điểm hơi thấp”.

Không tiếp tục spam mock ngay.

Flow:

```text
1. phân loại toàn bộ câu sai
2. tìm 2 error code lớn nhất
3. sửa concept/procedure gốc
4. làm 5 câu mới trong vùng đó
5. chỉ quay lại full mock khi closed-book explanation đã ổn
```

---

## Nếu môn 8–11/20

Đã qua ngưỡng mô phỏng nhưng margin quá thấp.

Ưu tiên:

```text
CON + PRO + TERM
```

Vì đây thường là lỗi có thể cải thiện nhanh hơn việc học thêm edge-case mới.

---

## Nếu môn 12–15/20

Coverage khá ổn. Tập trung:

```text
scenario discrimination
careless reading
cross-subject connections
```

Dùng Advanced Scenario Labs và Confusion Atlas.

---

## Nếu môn 16+/20

Không cần tiếp tục đọc toàn bộ môn từ đầu.

Audit câu sai và chuyển thời gian sang môn yếu nhất để tránh 과락.

---

# 8. Error ledger template

Sau mỗi mock, ghi dạng sau:

```text
Date:
Mock:

Q__ | Subject __ | Code: CON
Concept: RTO vs RPO
Why I chose wrong option:
Correct boundary:
Source to revisit: 11-high-risk-confusion-atlas §5.8
Re-drill: Workbook 28
Closed-book retry result: PASS/FAIL

Q__ | Subject __ | Code: PRO
Concept: /27 subnet
Failure step: wrong block size
Source: Workbook 18–19
New numbers tried: /26, /28
Closed-book retry result: PASS/FAIL
```

Không ghi “careless” nếu thực ra bạn không hiểu concept. `READ` chỉ dùng khi có thể giải đúng ngay sau khi nhìn lại wording mà không cần học thêm.

---

# 9. Error clusters cần cảnh giác

## Cluster A — “đều là security”

```text
Authentication
Authorization
Encryption
Hashing
Firewall
WAF
IDS/IPS
TLS
VPN
```

Nếu cứ chọn bằng cảm giác “security-related”, lỗi gốc là LAY/CON.

---

## Cluster B — “đều là database consistency”

```text
ACID
Lock
Isolation
Serializability
Deadlock
Lost Update
Dirty Read
Non-repeatable Read
Phantom Read
WAL
Checkpoint
Backup
```

Cần phân: property, concurrency control, anomaly, recovery, disaster copy.

---

## Cluster C — “đều là design”

```text
Architecture
Module
OOP
SOLID
Pattern
Interface
UML
```

Hãy xác định abstraction level trước khi chọn.

---

## Cluster D — “đều là performance”

```text
Complexity
Index
Cache
Paging
Scheduling
Throughput
Latency
Scaling
```

Mỗi cái tác động một resource/layer khác nhau.

---

# 10. Weekly remediation cycle

Một cycle học hiệu quả hơn việc làm đề liên tục:

```text
Day 1: mock / mixed drills
Day 2: classify errors + repair COV/CON
Day 3: procedural drills cho PRO/CAL
Day 4: scenario labs cho LAY/CON
Day 5: Korean term recall cho TERM
Day 6: closed-book audit
Day 7: second mixed set hoặc full mock
```

Không bắt buộc theo ngày thật; đây là logical cycle.

---

# 11. Definition of repaired error

Một lỗi chỉ được đánh dấu `REPAIRED` khi đủ bốn điều kiện:

1. **Explain:** giải thích concept bằng lời của mình.
2. **Distinguish:** phân biệt được concept gần nhất.
3. **Reproduce:** làm lại procedure/scenario mà không nhìn lời giải.
4. **Transfer:** làm đúng một câu mới có wording/số liệu khác.

Nếu chỉ nhớ lại option đúng của câu cũ, lỗi vẫn chưa được sửa.