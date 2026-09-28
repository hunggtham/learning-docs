# Hệ thống (system / 시스템) decomposition, services và boundaries

> **Mạch đọc:** Đặt **hệ thống (system / 시스템) decomposition, services và boundaries** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Bài toán ban đầu: độ phức tạp (complexity / 복잡도) phải được partition, nhưng không thể biến mất** sang **2. bất biến (invariant / 불변식) trước ranh giới (boundary / 경계)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Một hệ thống (system / 시스템) lớn phải được chia để con người, thời gian chạy (runtime / 런타임) và organization có thể quản lý độ phức tạp (complexity / 복잡도). Nhưng mỗi ranh giới (boundary / 경계) cũng tạo serialization, độ trễ (latency / 지연 시간), versioning, authorization, khả năng quan sát (observability / 관측 가능성) và partial-failure chi phí (cost / 비용). kiến trúc (architecture / 아키텍처) tốt không tối đa số services; nó đặt boundaries nơi **invariants, quyền sở hữu trạng thái (state ownership / 상태 소유권) và tỷ lệ (rate / 비율) of thay đổi (change / 변경)** có thể được quản lý tương đối độc lập.

Mô hình tư duy (mental model / 사고 모델) trung tâm là: **mỗi ranh giới (boundary / 경계) là một đặc tả hợp đồng (contract / 계약) + quyền sở hữu (ownership / 소유권) ranh giới (boundary / 경계) + thất bại (failure / 실패) ranh giới (boundary / 경계) + sức chứa (capacity / 용량) ranh giới (boundary / 경계)**. Tách một hàm (function / 함수) thành remote dịch vụ (service / 서비스) chỉ hợp lý khi lợi ích quyền sở hữu (ownership / 소유권)/independent evolution lớn hơn coordination chi phí (cost / 비용) mà phân phối (distribution / 분포) tạo ra.

## 1. Bài toán ban đầu: độ phức tạp (complexity / 복잡도) phải được partition, nhưng không thể biến mất

Nếu mọi mã (code / 코드)/dữ liệu (data / 데이터) nằm trong một khối không có nội bộ (internal / 내부) cấu trúc (structure / 구조), thay đổi nhỏ có blast radius lớn và nhóm (team / 팀) khó lập luận (reasoning / 추론). Nếu tách quá nhỏ, độ phức tạp (complexity / 복잡도) chuyển thành mạng (network / 네트워크) calls, schemas, retries, deployments và coordination giữa teams.

Ta luôn trả độ phức tạp (complexity / 복잡도) ở đâu đó:

```text
inside module/process
hoặc
across API/network/team boundaries
```

Hệ thống (system / 시스템) thiết kế (design / 설계) là chọn **nơi độ phức tạp (complexity / 복잡도) rẻ nhất để sở hữu**, không phải xóa độ phức tạp (complexity / 복잡도).

## 2. bất biến (invariant / 불변식) trước ranh giới (boundary / 경계)

Trước khi vẽ services, hãy viết invariants:

```text
order chỉ được charge một lần
inventory không âm
user chỉ đọc data tenant của mình
after success, write survive failure model X
schema producer/consumer coexist trong deployment window
```

Trạng thái (state / 상태) cần coordination mạnh để giữ cùng bất biến (invariant / 불변식) thường là tín hiệu (signal / 신호) rằng quyền sở hữu (ownership / 소유권) nên gần nhau. Nếu tách hai services nhưng mọi thao tác (operation / 연산) vẫn cần phân tán (distributed / 분산) giao dịch (transaction / 트랜잭션) giữa chúng, ranh giới (boundary / 경계) có thể đang cắt xuyên bất biến (invariant / 불변식) sai chỗ.

## 3. mô-đun (module / 모듈) trước microservice

Modularity là principle; microservice là triển khai (deployment / 배포)/phân phối (distribution / 분포) choice.

Một modular monolith có thể có:

```text
clear package/module boundaries
private state
stable internal contracts
independent ownership at code level
```

mà không trả mạng (network / 네트워크)/TLS/thử lại (retry / 재시도)/serialization chi phí (cost / 비용) cho mọi lời gọi (call / 호출).

Phân phối (distribution / 분포) nên được chọn khi cần independent triển khai (deployment / 배포)/scaling/thất bại (failure / 실패) isolation/organizational autonomy đủ mạnh để bù overhead.

## 4. Cohesion và coupling phải đo bằng thay đổi (change / 변경), dữ liệu (data / 데이터) và thời gian chạy (runtime / 런타임) tương tác (interaction / 상호작용)

High cohesion nghĩa responsibilities/invariants thay đổi cùng nhau. Low coupling nghĩa components không cần biết nội bộ (internal / 내부) details hay coordinate thường xuyên.

Coupling không chỉ imports:

```text
shared database schema
shared release train
chatty synchronous calls
shared cache key semantics
shared config/control plane
shared business transaction
one team blocks another for every change
```

Kiến trúc (architecture / 아키텍처) diagram có thể “microservices” nhưng operationally vẫn là phân tán (distributed / 분산) monolith.

## 5. Bounded ngữ cảnh (context / 맥락) là ngữ nghĩa (semantic / 의미적) ranh giới (boundary / 경계), không phải bảng (table / 테이블) ranh giới (boundary / 경계)

Trong Domain-Driven thiết kế (design / 설계), bounded ngữ cảnh (context / 맥락) xác định nơi mô hình (model / 모델)/terms có meaning nhất quán. `Customer` trong Billing có thể khác `Customer` trong hỗ trợ (support / 지원).

Ranh giới (boundary / 경계) hữu ích khi ngữ nghĩa (semantics / 의미론) + invariants + quyền sở hữu (ownership / 소유권) khác. Tách mỗi thực thể (entity / 엔터티)/bảng (table / 테이블) thành dịch vụ (service / 서비스) thường mechanical và tạo remote joins/chatty CRUD.

Một năng lực (capability / 역량) ranh giới (boundary / 경계) tốt trả lời:

```text
state nào thuộc authority này?
rule nào chỉ authority này được thay đổi?
contract nào bên ngoài được phép thấy?
```

## 6. quyền sở hữu trạng thái (state ownership / 상태 소유권) mạnh hơn mã (code / 코드) quyền sở hữu (ownership / 소유권)

Nếu dịch vụ (service / 서비스) A “owns” mã (code / 코드) nhưng dịch vụ (service / 서비스) B trực tiếp cập nhật (update / 업데이트) tables của A, quyền sở hữu (ownership / 소유권) không thật.

Dùng chung (shared / 공유) cơ sở dữ liệu (database / 데이터베이스) trap tạo hidden coupling:

```text
schema migration requires coordinated deployment
service B can violate invariant of A
query load of B impacts latency of A
rollback/versioning intertwined
```

Một dịch vụ (service / 서비스) owning dữ liệu (data / 데이터) qua đặc tả hợp đồng (contract / 계약) làm authority rõ hơn, nhưng không nghĩa mọi read phải synchronous RPC. Read các mô hình (models / 모델들), replicated views, bộ nhớ đệm (cache / 캐시) hoặc event-fed projections có thể giảm coupling nếu consistency đặc tả hợp đồng (contract / 계약) phù hợp.

## 7. Remote ranh giới (boundary / 경계) làm xuất hiện partial thất bại (failure / 실패)

Cục bộ (local / 로컬) hàm (function / 함수) lời gọi (call / 호출) thường có kết quả (outcome / 결과) trực tiếp hơn. Remote lời gọi (call / 호출) có states:

```text
request never sent
sent but server never received
server executed but response lost
server committed side effect then client timed out
response delayed while client retries
```

Do đó phân phối (distribution / 분포) thêm requirements:

```text
timeout/deadline
retry classification
idempotency
request identity
cancellation semantics
observability
```

Chia dịch vụ (service / 서비스) phải ngân sách (budget / 예산) cả tính đúng đắn (correctness / 정확성) chi phí (cost / 비용) này.

## 8. Synchronous ranh giới (boundary / 경계) đưa downstream vào đường găng (critical path / 임계 경로)

Synchronous lời gọi (call / 호출) dễ lập luận (reasoning / 추론) cho immediate kết quả (result / 결과) nhưng caller độ trễ (latency / 지연 시간)/availability phụ thuộc callee.

Một chuỗi (chain / 사슬):

```text
A → B → C → D
```

có deadline, hàng đợi (queue / 큐) và thử lại (retry / 재시도) ở nhiều hops. Fan-out còn khuếch đại tail độ trễ (latency / 지연 시간).

Nếu bất biến (invariant / 불변식) thật sự cần immediate quyết định (decision / 결정), sync có thể đúng. Nếu không, asynchronous ranh giới (boundary / 경계) có thể giảm temporal coupling.

## 9. Asynchronous ranh giới (boundary / 경계) đổi coupling chứ không xóa coupling

Sự kiện (event / 이벤트)/message giúp producer không chờ bên tiêu thụ (consumer / 소비자) availability ngay lúc publish, nhưng bên tiêu thụ (consumer / 소비자) phụ thuộc lược đồ (schema / 스키마)/ngữ nghĩa (semantics / 의미론)/thứ tự (order / 순서)/delivery đặc tả hợp đồng (contract / 계약).

New thất bại (failure / 실패) modes:

```text
duplicate delivery
out-of-order
consumer lag
poison message
schema mismatch
replay side effect
unbounded backlog
```

Event-driven không tự “decoupled”; coupling chuyển từ call-time availability sang **giao thức (protocol / 프로토콜) + trạng thái (state / 상태) evolution + operations**.

## 10. Saga là phân tán (distributed / 분산) máy trạng thái (state machine / 상태 머신), không phải quay lui (rollback / 롤백) nhiều cơ sở dữ liệu (database / 데이터베이스)

Workflow xuyên services có thể dùng cục bộ (local / 로컬) transactions + messages/compensation.

Compensation không quay thời gian (time / 시간). Gửi hàng rồi “undo” có thể là return/refund workflow với real-world trạng thái (state / 상태) mới.

Một saga cần tường minh (explicit / 명시적):

```text
state transitions
idempotency key
retry policy
compensation rule
irreversible step
manual intervention state
observability/correlation
```

Hệ thống (system / 시스템) thiết kế (design / 설계) phải xem saga như durable máy trạng thái (state machine / 상태 머신), không chỉ mẫu (pattern / 패턴) name.

## 11. Đặc tả API (API contract / API 계약) phải bao gồm hành vi (behavior / 동작), không chỉ lược đồ (schema / 스키마)

Đặc tả hợp đồng (contract / 계약) gồm hơn JSON fields:

```text
meaning/units
idempotency
ordering
error taxonomy
pagination consistency
timeout expectations
rate/cost limits
backward/forward compatibility
security principal semantics
```

Hai services compile với cùng protobuf/OpenAPI nhưng hiểu ngữ nghĩa (semantics / 의미론) khác vẫn có đặc tả hợp đồng (contract / 계약) bug.

Đọc [schema/protocol evolution](./advanced/06_schema_protocol_evolution_and_compatibility_contracts.md).

## 12. sức chứa (capacity / 용량) ranh giới (boundary / 경계) phải nằm gần tài nguyên (resource / 자원) hữu hạn

Mỗi dịch vụ (service / 서비스) có pools/queues/CPU/bộ nhớ (memory / 메모리)/lưu trữ (storage / 저장소)/downstream limits. Nếu caller có thể tạo unlimited tính đồng thời (concurrency / 동시성) vào tài nguyên (resource / 자원) giới hạn, dịch vụ (service / 서비스) ranh giới (boundary / 경계) không bảo vệ phụ thuộc (dependency / 의존성).

Useful bất biến (invariant / 불변식):

> Accepted công việc (work / 작업) không được vượt sức chứa (capacity / 용량) khiến useful completion trước deadline collapse.

Cơ chế (mechanism / 메커니즘): bounded queues, semaphore, admission điều khiển (control / 제어), per-tenant quota, backpressure, tải (load / 로드) shedding.

Hệ thống (system / 시스템) thiết kế (design / 설계) không chỉ vẽ boxes; nó phải chỉ ra **hàng đợi (queue / 큐) nằm đâu và ai chịu trách nhiệm reject khi full**.

## 13. Multi-tenant ranh giới (boundary / 경계) cần fairness ngữ nghĩa (semantics / 의미론)

Nếu tenants share pool/bộ nhớ đệm (cache / 캐시)/cơ sở dữ liệu (database / 데이터베이스), kiến trúc (architecture / 아키텍처) phải quyết định isolation mức (level / 수준):

```text
best effort shared
weighted fair
reserved capacity
hard quota
physical separation
```

Tách dịch vụ (service / 서비스) không tự tạo tenant isolation nếu backend tài nguyên (resource / 자원) vẫn dùng chung (shared / 공유). Noisy-neighbor hành vi (behavior / 동작) thường leak từ lower tầng (layer / 계층) như DB liên kết (connection / 연결) pool hoặc lưu trữ (storage / 저장소) IOPS.

## 14. bảo mật (security / 보안) principal đổi ở ranh giới (boundary / 경계) nào?

North-south yêu cầu (request / 요청) có end-user định danh (identity / 식별자); east-west dịch vụ (service / 서비스) lời gọi (call / 호출) có tải công việc (workload / 워크로드) định danh (identity / 식별자); dịch vụ (service / 서비스) có thể act on behalf of người dùng (user / 사용자) hoặc bằng own authority.

Ranh giới (boundary / 경계) cần tường minh (explicit / 명시적):

```text
caller principal là ai?
user context nào được delegated?
service authority nào được dùng?
authorization ở đâu?
credential/secret nào mở downstream capability?
```

Nếu backend chỉ tin header `role=admin` từ gateway mà direct đường dẫn (path / 경로) tồn tại, kiến trúc (architecture / 아키텍처) ranh giới bảo mật (security boundary / 보안 경계) sai dù nghiệp vụ (business / 비즈니스) mã (code / 코드) đúng.

Đọc [Security boundaries](../07_security_reliability/advanced/00_security_boundaries_attack_chains_and_exploitability.md).

## 15. API gateway và dịch vụ (service / 서비스) mesh là chính sách (policy / 정책)/thời gian chạy (runtime / 런타임) layers, không phải dây dẫn trong suốt

Gateway có thể tuyến (route / 경로), auth, rate-limit, thử lại (retry / 재시도), bộ nhớ đệm (cache / 캐시), transform headers. Mesh/mặt phẳng dữ liệu (data plane / 데이터 플레인) có thể mTLS, retries, tải (load / 로드) balancing, telemetry.

Mỗi tính năng (feature / 기능) thêm hàng đợi (queue / 큐), trạng thái (state / 상태) và dạng thất bại (failure mode / 실패 모드). Nếu proxy thử lại (retry / 재시도) và ứng dụng (application / 애플리케이션) cũng thử lại (retry / 재시도), tải (load / 로드) amplification có thể nhân.

Centralized chính sách (policy / 정책) giúp consistency nhưng tạo dùng chung (shared / 공유) phụ thuộc (dependency / 의존성); khả năng quan sát (observability / 관측 가능성) phải cho thấy công việc (work / 작업) đã chờ hoặc bị thử lại (retry / 재시도) ở proxy chứ không chỉ ứng dụng (application / 애플리케이션).

## 16. dữ liệu (data / 데이터) locality và mạng (network / 네트워크) locality thuộc cùng thiết kế (design / 설계)

Tách compute khỏi dữ liệu (data / 데이터) làm remote truy cập (access / 접근). Chatty dịch vụ (service / 서비스) gọi DB/dịch vụ (service / 서비스) khác cho từng trường dữ liệu (field / 필드) có thể biến cục bộ (local / 로컬) bộ nhớ (memory / 메모리) lời gọi (call / 호출) thành nhiều RTT.

Ranh giới (boundary / 경계) nên cân:

```text
data ownership
read locality
write invariant
cacheability
replication freshness
cross-region traffic
```

Independent triển khai (deployment / 배포) không đáng nếu mọi yêu cầu (request / 요청) vẫn phải synchronous round-trip qua nhiều owners để assemble trivial trạng thái (state / 상태).

## 17. Multi-region decomposition phải phân loại thao tác (operation / 연산) theo coordination need

Không phải mọi ghi (write / 쓰기) cần toàn cục (global / 전역) consensus. Hãy phân loại:

```text
must preserve global invariant
region-local authority enough
read-your-writes required
stale read acceptable
asynchronous merge acceptable
```

Sau đó chọn placement/replication. toàn cục (global / 전역) strong đường dẫn (path / 경로) cho mọi thao tác (operation / 연산) trả độ trễ (latency / 지연 시간)/sức chứa (capacity / 용량) chi phí (cost / 비용); eventual-everything lại có thể phá nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식).

Đọc [multi-region replication](../06_networks_distributed_systems/advanced/05_multi_region_replication_and_geo_distributed_tradeoffs.md).

## 18. chi phí (cost / 비용) mô hình (model / 모델) phải gồm coordination chi phí (cost / 비용)

Hệ thống (system / 시스템) thiết kế (design / 설계) interview/môi trường vận hành (production / 운영 환경) thường hỏi QPS/lưu trữ (storage / 저장소) nhưng bỏ coordination overhead.

Sức chứa (capacity / 용량) estimate nên ít nhất cover:

```text
request rate × fan-out
retry/hedge amplification
payload × replication factor
cache hit/miss path
peak/burst not only average
cross-region egress/RTT
per-tenant skew
background jobs/backfill/replay
```

Một thiết kế (design / 설계) “10k QPS” có thể tạo 100k downstream attempts nếu mỗi yêu cầu (request / 요청) fan-out 5 và thử lại (retry / 재시도) 2 tầng.

## 19. thất bại (failure / 실패) domains phải được vẽ, không giả định từ box count

Hai services ở two pods nhưng cùng nút (node / 노드)/cơ sở dữ liệu (database / 데이터베이스)/KMS/điều khiển (control / 제어) plane có dùng chung (shared / 공유) thất bại (failure / 실패). Three regions nhưng same toàn cục (global / 전역) định danh (identity / 식별자) issuer có correlated phụ thuộc (dependency / 의존성).

Availability lập luận (reasoning / 추론) cần phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프):

```text
compute
network
storage
control plane
identity/KMS
schema/config rollout
human/operator workflow
```

Redundancy chỉ có giá trị với dạng thất bại (failure mode / 실패 모드) độc lập tương ứng.

## 20. triển khai (deployment / 배포) ranh giới (boundary / 경계) và dữ liệu (data / 데이터) ranh giới (boundary / 경계) có thể khác

Một mã (code / 코드) rollout có thể quay lui (rollback / 롤백) nhị phân (binary / 이진), nhưng lược đồ (schema / 스키마)/dữ liệu (data / 데이터) mutation có thể irreversible. cờ tính năng (feature flag / 기능 플래그) chỉ reversible nếu old đường dẫn (path / 경로) còn hiểu trạng thái (state / 상태) mới.

Hệ thống (system / 시스템) thiết kế (design / 설계) cần cùng Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학) xác định tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우) và di chuyển (migration / 마이그레이션) trạng thái (state / 상태), không xem triển khai (deployment / 배포) là bên ngoài (external / 외부) concern.

Đọc [large-scale migration](../09_software_engineering/advanced/03_large_scale_refactoring_strangler_and_branch_by_abstraction.md).

## 21. Conway's Law và quyền sở hữu (ownership / 소유권) hàng đợi (queue / 큐)

Hệ thống (system / 시스템) communication thường phản chiếu organization communication. Nếu một dịch vụ (service / 서비스) cần approval từ nhóm (team / 팀) khác cho mọi thay đổi, “independent dịch vụ (service / 서비스)” không independent về lead thời gian (time / 시간).

Kiến trúc (architecture / 아키텍처) quyết định (decision / 결정) cần xem:

```text
who owns on-call?
who owns schema/API?
who can deploy independently?
who resolves incident across boundary?
```

Poor socio-technical ranh giới (boundary / 경계) tạo coordination hàng đợi (queue / 큐) giống thời gian chạy (runtime / 런타임) hàng đợi (queue / 큐): công việc (work / 작업) chờ người khác trước khi luồng (flow / 흐름) tiếp.

## 22. phân tán (distributed / 분산) monolith là dạng thất bại (failure mode / 실패 모드) có dấu hiệu đo được

Dấu hiệu:

```text
services deploy together
shared DB writes
chatty synchronous chains
cross-team changes bắt buộc
one service outage cascades fleet-wide
contract/version changes lock-step
```

Tách thêm services không chữa; thường cần gom bất biến (invariant / 불변식) lại hoặc thiết kế quyền sở hữu (ownership / 소유권)/giao thức (protocol / 프로토콜) đúng hơn.

## 23. bằng chứng vận hành (production evidence / 운영 증거) phải theo ranh giới (boundary / 경계)

Bằng chứng (evidence / 증거) cho kiến trúc (architecture / 아키텍처) không chỉ infra dashboard. Cần:

```text
call graph/fan-out
per-boundary latency + queue wait
retry/attempt amplification
error taxonomy
data/replica freshness
schema/version distribution
per-tenant resource use
change/deploy coupling
incident blast radius
```

Một dịch vụ (service / 서비스) map đẹp nhưng traces cho thấy 40 synchronous calls/yêu cầu (request / 요청) là bằng chứng (evidence / 증거) ranh giới (boundary / 경계) chi phí (cost / 비용) đang cao.

## 24. ranh giới (boundary / 경계) rà soát (review / 검토) checklist theo bất biến (invariant / 불변식)

Trước khi tách/giữ dịch vụ (service / 서비스), hỏi:

```text
Invariant nào nằm trong boundary?
State authority ở đâu?
Remote failure tạo outcome ambiguity nào?
Queue/admission ở đâu?
Security principal đổi thế nào?
Schema/version coexist ra sao?
Data locality/replication ra sao?
Failure domain có thật sự khác?
Team có sở hữu độc lập được không?
Evidence nào chứng minh boundary tốt hơn hiện tại?
```

Nếu không trả lời được, technology choice còn quá sớm.

## Dùng chung (common / 공통) Misconceptions

**“Microservices quy mô (scale / 규모) tốt hơn monolith.”** Một monolith stateless vẫn horizontal quy mô (scale / 규모); microservices chủ yếu cho independent scaling/quyền sở hữu (ownership / 소유권)/thất bại (failure / 실패) isolation khi ranh giới (boundary / 경계) đúng.

**“Mỗi bảng (table / 테이블) nên là một dịch vụ (service / 서비스).”** bảng (table / 테이블) là lưu trữ (storage / 저장소) biểu diễn (representation / 표현); dịch vụ (service / 서비스) ranh giới (boundary / 경계) nên theo bất biến (invariant / 불변식)/năng lực (capability / 역량)/quyền sở hữu (ownership / 소유권).

**“Event-driven nghĩa decoupled.”** Coupling chuyển sang sự kiện (event / 이벤트) ngữ nghĩa (semantics / 의미론), lag, replay và lược đồ (schema / 스키마) evolution.

**“dịch vụ (service / 서비스) mesh giải độ tin cậy (reliability / 신뢰성).”** Nó có thể cung cấp cơ chế (mechanism / 메커니즘), nhưng thử lại (retry / 재시도)/hết thời gian chờ (timeout / 타임아웃)/admission chính sách (policy / 정책) sai vẫn tạo cascading thất bại (failure / 실패).

**“Nhiều regions nghĩa highly available.”** Chỉ đúng với thất bại (failure / 실패) domains/dependencies thật sự independent và failover sức chứa (capacity / 용량) đủ.

## 25. Mô hình tư duy

> hệ thống (system / 시스템) thiết kế (design / 설계) là bài toán **đặt authority, invariants, queues và thất bại (failure / 실패) boundaries**. mô-đun (module / 모듈)/dịch vụ (service / 서비스) ranh giới (boundary / 경계) tốt gom trạng thái (state / 상태) cần coordination và cho phần còn lại evolve độc lập. phân phối (distribution / 분포) chỉ đáng khi autonomy/scaling/isolation lợi hơn mạng (network / 네트워크)/giao thức (protocol / 프로토콜) chi phí (cost / 비용). **Bắt đầu bằng bất biến (invariant / 불변식) + tải công việc (workload / 워크로드) + thất bại (failure / 실패) mô hình (model / 모델) + bằng chứng (evidence / 증거); technology là hiện thực (implementation / 구현) của những đặc tả hợp đồng (contract / 계약) đó.**

## Kết nối

Đọc [modularity/API](./00_abstraction_modularity_interfaces_and_apis.md), [performance/capacity](./02_performance_capacity_and_scalability.md), [state/queues/backpressure](./03_state_queues_backpressure_and_boundaries.md), [event-driven](./06_event_driven_and_stream_processing.md), [queueing advanced](./advanced/00_queueing_tail_latency_and_backpressure.md), [distributed consistency](../06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md), [Security boundaries](../07_security_reliability/advanced/00_security_boundaries_attack_chains_and_exploitability.md), [software architecture](../09_software_engineering/01_software_architecture_and_design_reasoning.md) và [end-to-end request path](../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 abstraction modularity interfaces and apis](./00_abstraction_modularity_interfaces_and_apis.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
