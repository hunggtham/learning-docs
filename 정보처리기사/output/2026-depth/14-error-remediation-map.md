# 정보처리기사 필기 2026 — lỗi (error / 오류) Remediation Map

> Mục tiêu của tệp (file / 파일) này là biến mỗi câu sai thành một **đường sửa lỗi cụ thể**. Không ghi “sai câu 37” rồi đọc lại toàn bộ môn. Hãy xác định loại lỗi, concept gốc, tệp (file / 파일) cần quay lại và dạng bài phải làm lại.

---

# 1. lỗi (error / 오류) taxonomy

Mỗi câu sai chỉ gán **một primary lỗi (error / 오류) mã (code / 코드)** đầu tiên. Nếu có lỗi phụ, ghi sau.

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

## CON — Confusion lỗi (error / 오류)

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

## PRO — Procedural lỗi (error / 오류)

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

## LAY — tầng (layer / 계층)/phạm vi (scope / 범위) lỗi (error / 오류)

Chọn cơ chế (mechanism / 메커니즘) đúng nhưng ở sai lớp trừu tượng (abstraction / 추상화) tầng (layer / 계층) hoặc sai phạm vi bảo vệ.

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

## READ — Reading / Polarity lỗi (error / 오류)

Sai vì đọc nhầm:

```text
옳지 않은 것
해당하지 않는 것
가장 적절한 것
주된 목적
```

hoặc bỏ sót `NOT`, đơn vị (unit / 단위), arrival thời gian (time / 시간), prefix length.

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

## CAL — Arithmetic lỗi (error / 오류)

Procedure đúng nhưng tính nhầm số.

### Cách sửa

Tách calculation khỏi conceptual lập luận (reasoning / 추론).

Viết intermediate trạng thái (state / 상태); không tính mental quá nhiều trong scheduling/subnet/page replacement.

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
| Functional vs Non-functional | năng lực (capability / 역량) vs chất lượng (quality / 품질)/ràng buộc (constraint / 제약조건) | `01-software-design-depth.md`, Confusion Atlas §1.2 |
| xác minh (verification / 확인) vs kiểm tra hợp lệ (validation / 검증) | đúng spec vs đúng nhu cầu | Confusion Atlas §1.1, Scenario Lab 1 |
| DFD | luồng dữ liệu (data flow / 데이터 흐름) hay điều khiển (control / 제어) luồng (flow / 흐름) | Deep Dive §Structured phân tích (analysis / 분석), Confusion Atlas §1.3 |
| UML diagram | câu hỏi muốn quan sát gì | Deep Dive UML, Term cầu nối (bridge / 브리지) UML |
| Aggregation/Composition | vòng đời (lifecycle / 생명주기) quyền sở hữu (ownership / 소유권) | Confusion Atlas §1.5 |
| Cohesion | relationship bên trong mô-đun (module / 모듈) | Deep Dive mô-đun (module / 모듈) Independence |
| Coupling | phụ thuộc (dependency / 의존성) giữa modules | Deep Dive + Confusion Atlas §1.7–1.8 |
| Fan-in/Fan-out | count phụ thuộc (dependency / 의존성), không phải chất lượng (quality / 품질) | Scenario Lab 2 |
| SOLID | symptom của thiết kế (design / 설계) bài toán (problem / 문제) | Deep Dive SOLID + Atlas §1.9–1.10 |
| chiến lược (strategy / 전략)/trạng thái (state / 상태) | nguồn (source / 소스) của hành vi (behavior / 동작) variation | Atlas §1.11 + Lab 3 |
| Adapter/Facade | giao diện (interface / 인터페이스) mismatch vs độ phức tạp (complexity / 복잡도) | Atlas §1.12 + Lab 4 |
| Decorator/Proxy | add hành vi (behavior / 동작) vs kiểm soát truy cập (access control / 접근 제어) | Atlas §1.13 |
| Factory phương thức (method / 메서드)/Abstract Factory | one creation đường dẫn (path / 경로) vs sản phẩm (product / 제품) family | Atlas §1.14 |
| UI artifacts | skeleton/visual/tương tác (interaction / 상호작용) | Atlas §1.15 |
| giao diện (interface / 인터페이스) thử lại (retry / 재시도) | mạng (network / 네트워크) bất định (uncertainty / 불확실성) + idempotency | liên kết (connection / 연결) Map §3, Lab 5 |

### Gate để đóng lỗi Môn 1

Không đóng lỗi chỉ vì đọc lại. Phải tạo được một câu mới có distractor gần concept vừa nhầm.

---

# 3. Remediation map — Môn 2

| Nếu sai ở vùng | Primary check | Quay lại |
|---|---|---|
| ngăn xếp (stack / 스택)/Postfix | pop thứ tự (order / 순서) | Workbook Drill 2 |
| BFS/DFS | frontier chính sách (policy / 정책) | Workbook Drill 3, Atlas §2.2 |
| vùng nhớ động (heap / 힙)/BST | thao tác (operation / 연산) cần tối ưu | Atlas §2.3, Lab 6 |
| tìm kiếm nhị phân (binary search / 이진 탐색) | sorted precondition | Workbook Drill 5, Lab 7 |
| băm (hash / 해시) collision | probing/clustering | Workbook Drill 4 |
| độ phức tạp (complexity / 복잡도) | worst/average/không gian (space / 공간) | Deep Dive Algorithms |
| Stub/Driver | ai giả caller/callee | Atlas §2.6 |
| Black/White box | bên ngoài (external / 외부) hành vi (behavior / 동작) vs nội bộ (internal / 내부) đường dẫn (path / 경로) | Atlas §2.7 |
| ranh giới (boundary / 경계)/Equivalence | edge vs partition | Atlas §2.8 |
| Coverage | statement/branch/đường dẫn (path / 경로) | Lab 8 |
| Retest/Regression | defect-specific vs collateral | Atlas §2.9 + Lab 9 |
| Alpha/Beta | nội bộ (internal / 내부) controlled vs bên ngoài (external / 외부) users | Atlas §2.10 |
| phiên bản (version / 버전)/CM | VCS subset của CM | Atlas §2.11 |
| bản dựng (build / 빌드)/gói (package / 패키지)/bản phát hành (release / 릴리스) | vòng đời (lifecycle / 생명주기) sản phẩm tạo ra (artifact / 산출물) | Atlas §2.12 |
| Checksum/Signature | content match vs authenticity | Lab 10 |

### Gate

Với thuật toán (algorithm / 알고리즘)/cấu trúc dữ liệu (data structure / 자료구조) lỗi (error / 오류), phải dấu vết (trace / 추적) trạng thái (state / 상태) từng bước. Với testing lỗi (error / 오류), phải tự viết một trường hợp kiểm thử (test case / 테스트 케이스) làm rõ ranh giới.

---

# 4. Remediation map — Môn 3

| Nếu sai ở vùng | Primary check | Quay lại |
|---|---|---|
| Candidate key | closure + minimality | Workbook Drill 6, Lab 11 |
| Super/Candidate/Primary | uniqueness vs minimality vs selected key | Atlas §3.1–3.2 |
| Selection/Projection | row vs column | Atlas §3.3 |
| 2NF | partial phụ thuộc (dependency / 의존성) | Workbook Drill 7 |
| 3NF | transitive/formal điều kiện (condition / 조건) | Workbook Drill 8 |
| 3NF/BCNF | determinant + prime attribute | Atlas §3.5, Lab 12 |
| chỉ mục (index / 인덱스) | truy cập (access / 접근) mẫu (pattern / 패턴) + key thứ tự (order / 순서) | liên kết (connection / 연결) Map §4.2, Lab 13 |
| Selectivity/Cardinality | fraction vs distinct/row ngữ cảnh (context / 맥락) | Atlas §3.8 |
| WHERE/HAVING | before/after grouping | Workbook Drill 9 |
| LEFT phép nối (join / 조인) | preserved side + NULL | Workbook Drill 10, Lab 14 |
| COUNT NULL | COUNT(*) vs COUNT(col) | Atlas §3.10 |
| Dirty/NRR/Phantom | uncommitted/giá trị (value / 값)/set | Atlas §3.13 |
| Lost cập nhật (update / 업데이트) | concurrent overwrite | Lab 15 |
| Serializability | precedence đồ thị (graph / 그래프) cycle | Workbook Drill 11 |
| Deadlock | tài nguyên (resource / 자원) wait cycle | liên kết (connection / 연결) Map §8 |
| khôi phục (recovery / 복구) | undo/redo/log/checkpoint | Atlas §3.16–3.17 |
| di chuyển (migration / 마이그레이션) | kiểm tra hợp lệ (validation / 검증)/reconciliation | Coverage kiểm tra (audit / 감사) Ch.14 |

### Gate

DB procedural lỗi chỉ đóng khi làm được **một ví dụ mới tự tạo**: closure, normalization, SQL kết quả (result / 결과) hoặc schedule.

---

# 5. Remediation map — Môn 4

| Nếu sai ở vùng | Primary check | Quay lại |
|---|---|---|
| tiến trình (process / 프로세스)/luồng thực thi (thread / 스레드) | address không gian (space / 공간)/tài nguyên (resource / 자원) sharing | Atlas §4.1 |
| tính đồng thời (concurrency / 동시성)/Parallelism | overlapping vs simultaneous | Atlas §4.2 |
| Mutex/Semaphore | quyền sở hữu (ownership / 소유권) vs permits | Atlas §4.3 |
| Race/Deadlock | wrong kết quả (result / 결과) vs no progress | Atlas §4.4 |
| Deadlock chiến lược (strategy / 전략) | prevention/avoidance/detection | Workbook Drill 30 |
| FCFS | timeline first | Workbook Drill 13 |
| SJF | shortest burst + starvation | Workbook Drill 14 |
| RR | quantum + rotation | Workbook Drill 15, Lab 17 |
| Metrics | waiting/turnaround/phản hồi (response / 응답) | Atlas §4.7 |
| FIFO/LRU | insertion age vs recency | Workbook Drill 16–17 |
| Page Fault/Thrashing | sự kiện (event / 이벤트) vs systemic điều kiện (condition / 조건) | Atlas §4.10 |
| Subnet | host bits + khối (block / 블록) ranh giới (boundary / 경계) | Workbook Drill 18–19,34 |
| Routing | longest prefix | Workbook Drill 20 |
| TCP/UDP | stream độ tin cậy (reliability / 신뢰성) vs datagram | Atlas §4.11 |
| TCP/idempotency | vận chuyển (transport / 전송) vs nghiệp vụ (business / 비즈니스) ngữ nghĩa (semantics / 의미론) | Lab 19 |
| C pointer | address/tham chiếu (reference / 참조) trạng thái (state / 상태) | Workbook Drill 21–22 |
| Java dispatch | compile-time kiểu (type / 타입) vs thời gian chạy (runtime / 런타임) phương thức (method / 메서드) | Workbook Drill 23, Lab 20 |
| Python alias | same mutable đối tượng (object / 객체) | Workbook Drill 24 |
| Multi-instance sync | phạm vi (scope / 범위) của mutex | Lab 16 |

### Gate

Với mã (code / 코드)/OS/mạng (network / 네트워크), phải viết trạng thái (state / 상태) bảng (table / 테이블) hoặc timeline. Không chấp nhận “đọc và thấy hiểu”.

---

# 6. Remediation map — Môn 5

| Nếu sai ở vùng | Primary check | Quay lại |
|---|---|---|
| rủi ro (risk / 위험)/Issue | future bất định (uncertainty / 불확실성) vs existing bài toán (problem / 문제) | Atlas §5.2 |
| PERT | formula | Workbook Drill 25 |
| đường găng (critical path / 임계 경로) | đường dẫn (path / 경로) duration/slack | Workbook Drill 26 |
| RAID | mức (level / 수준)/sức chứa (capacity / 용량)/thất bại (failure / 실패) mô hình (model / 모델) | Workbook Drill 27 |
| RAID/Backup | vật lý (physical / 물리적) redundancy vs recoverable bản sao (copy / 복사) | Atlas §5.5, Lab 23 |
| Replication/Backup | hiện tại (current / 현재) bản sao (copy / 복사) vs khôi phục (recovery / 복구) lịch sử (history / 이력) | Atlas §5.6 |
| HA/DR | routine failover vs major khôi phục (recovery / 복구) | Atlas §5.7 |
| RTO/RPO | restore thời gian (time / 시간) vs data-loss cửa sổ (window / 윈도우) | Workbook Drill 28, Lab 21 |
| Backup độ tin cậy (reliability / 신뢰성) | restore kiểm thử (test / 테스트) | Lab 22 |
| Scaling | nút (node / 노드) bigger vs more nodes | Atlas §5.9 |
| VM/bộ chứa (container / 컨테이너) | guest kernel vs dùng chung (shared / 공유) host kernel | Atlas §5.10 |
| IaaS/PaaS/SaaS | responsibility ranh giới (boundary / 경계) | Atlas §5.11 |
| AuthN/AuthZ | định danh (identity / 식별자) vs permission | Atlas §5.12, Lab 24 |
| băm (hash / 해시)/Encryption | one-way digest vs reversible confidentiality | Atlas §5.13 |
| SQLi/XSS | sink/nguyên nhân gốc (root cause / 근본 원인) | Workbook Drill 29, Atlas §5.15 |
| Firewall/WAF | mạng (network / 네트워크) quy tắc (rule / 규칙) vs HTTP app ngữ nghĩa (semantics / 의미론) | Atlas §5.16 |
| IDS/IPS | detect vs inline prevent | Atlas §5.17 |
| TLS/VPN | ứng dụng (application / 애플리케이션) channel vs mạng (network / 네트워크) tunnel | Atlas §5.18 |
| Threat/Vulnerability/rủi ro (risk / 위험) | actor/sự kiện (event / 이벤트) vs weakness vs contextual mất mát (loss / 손실) | Atlas §5.19 |
| Defense in độ sâu (depth / 깊이) | gốc (root / 루트) điều khiển (control / 제어) vs additional tầng (layer / 계층) | Lab 25 |

---

# 7. Score-driven remediation

## Nếu một môn < 8/20

Đây là **과락 rủi ro (risk / 위험)**, không chỉ “điểm hơi thấp”.

Không tiếp tục spam mock ngay.

Luồng (flow / 흐름):

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

Kiểm tra (audit / 감사) câu sai và chuyển thời gian sang môn yếu nhất để tránh 과락.

---

# 8. lỗi (error / 오류) ledger template

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

# 9. lỗi (error / 오류) clusters cần cảnh giác

## Cluster A — “đều là bảo mật (security / 보안)”

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

## Cluster B — “đều là cơ sở dữ liệu (database / 데이터베이스) consistency”

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

Cần phân: thuộc tính (property / 속성), tính đồng thời (concurrency / 동시성) điều khiển (control / 제어), anomaly, khôi phục (recovery / 복구), disaster bản sao (copy / 복사).

---

## Cluster C — “đều là thiết kế (design / 설계)”

```text
Architecture
Module
OOP
SOLID
Pattern
Interface
UML
```

Hãy xác định lớp trừu tượng (abstraction / 추상화) mức (level / 수준) trước khi chọn.

---

## Cluster D — “đều là hiệu năng (performance / 성능)”

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

Mỗi cái tác động một tài nguyên (resource / 자원)/tầng (layer / 계층) khác nhau.

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

# 11. Definition of repaired lỗi (error / 오류)

Một lỗi chỉ được đánh dấu `REPAIRED` khi đủ bốn điều kiện:

1. **Explain:** giải thích concept bằng lời của mình.
2. **Distinguish:** phân biệt được concept gần nhất.
3. **Reproduce:** làm lại procedure/scenario mà không nhìn lời giải.
4. **Transfer:** làm đúng một câu mới có wording/số liệu khác.

Nếu chỉ nhớ lại option đúng của câu cũ, lỗi vẫn chưa được sửa.