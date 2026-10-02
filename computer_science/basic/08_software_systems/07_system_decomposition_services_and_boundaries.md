# Hệ thống (system / 시스템) decomposition, services và boundaries

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **System decomposition, services và boundaries**. Route đi từ complexity partition/invariants → modules trước microservices → state ownership/API contracts → sync/async failure → saga, capacity, security và multi-region boundaries, để mỗi service boundary có lý do vận hành rõ ràng.

Một hệ thống (system / 시스템) lớn phải được chia nhỏ vì một nhóm (team / 팀) hay một tiến trình (process / 프로세스) không thể giữ toàn bộ độ phức tạp (complexity / 복잡도) trong đầu. Nhưng mỗi ranh giới (boundary / 경계) mới cũng tạo communication, versioning, bảo mật (security / 보안), độ trễ (latency / 지연 시간) và thất bại (failure / 실패) chi phí (cost / 비용). **hệ thống (system / 시스템) thiết kế (design / 설계)** vì vậy không phải chọn mẫu (pattern / 패턴) hoặc công nghệ theo catalogue; nó là bài toán đặt quyền sở hữu (ownership / 소유권) và thất bại (failure / 실패) boundaries sao cho bất biến (invariant / 불변식) quan trọng vẫn được giữ khi tải (load / 로드), thất bại (failure / 실패) và organizational thay đổi (change / 변경) xuất hiện.

Câu hỏi đúng không phải “monolith hay microservices?”. Câu hỏi là: **trạng thái (state / 상태)/bất biến (invariant / 불변식) nào thuộc về ai, consistency nào cần giữ, thất bại (failure / 실패) nào được phép lan qua ranh giới (boundary / 경계), và bằng chứng (evidence / 증거) nào cho biết ranh giới (boundary / 경계) đang hoạt động đúng?**

## 1. ranh giới (boundary / 경계) chỉ có giá trị khi nó gom quyền sở hữu (ownership / 소유권) rõ

Một mô-đun (module / 모듈)/dịch vụ (service / 서비스) hữu ích khi nó sở hữu một nhóm trạng thái (state / 상태) và rules thay đổi cùng nhau. Nếu hai services phải cùng deploy mỗi lần, cùng sửa một lược đồ (schema / 스키마) và cùng gỡ lỗi (debug / 디버그) một giao dịch (transaction / 트랜잭션), ranh giới (boundary / 경계) vật lý không tạo autonomy thật.

Mô hình tư duy (mental model / 사고 모델):

```text
boundary tốt
= ownership rõ
+ contract rõ
+ failure semantics rõ
+ change có thể tương đối độc lập
```

Chia nhỏ vì “mỗi dịch vụ (service / 서비스) khoảng 1.000 dòng” hoặc “mỗi bảng (table / 테이블) một dịch vụ (service / 서비스)” không tạo mô hình tư duy (mental model / 사고 모델) tốt.

> **Chuyển mạch:** Trong **Hệ thống (system / 시스템) decomposition, services và boundaries**, **1. ranh giới (boundary / 경계) chỉ có giá trị khi nó gom quyền sở hữu (ownership / 소유권) rõ** đã nêu tiêu chí phân biệt, còn **2. mô-đun (module / 모듈) trước phân tán (distributed / 분산) ranh giới (boundary / 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **3. Cohesion và coupling phải đo bằng thay đổi (change / 변경)/thất bại (failure / 실패), không chỉ import đồ thị (graph / 그래프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. mô-đun (module / 모듈) trước phân tán (distributed / 분산) ranh giới (boundary / 경계)

Modularity là principle; microservice chỉ là một triển khai (deployment / 배포) form. Một modular monolith có thể có strong boundaries mà không chịu mạng (network / 네트워크), serialization, hết thời gian chờ (timeout / 타임아웃), thử lại (retry / 재시도) và partial thất bại (failure / 실패) chi phí (cost / 비용).

Khi đổi một hàm (function / 함수) lời gọi (call / 호출) thành remote lời gọi (call / 호출), ta thêm ít nhất:

```text
network latency
connection management
serialization/protocol compatibility
timeout/retry
authentication/authorization
partial failure
observability context propagation
```

Do đó phân tán (distributed / 분산) ranh giới (boundary / 경계) phải “kiếm được quyền tồn tại” bằng independent scaling, quyền sở hữu (ownership / 소유권), thất bại (failure / 실패) isolation hoặc triển khai (deployment / 배포)/evolution benefit đủ lớn.

> **Chuyển mạch:** Ở chặng này của **Hệ thống (system / 시스템) decomposition, services và boundaries**, **2. mô-đun (module / 모듈) trước phân tán (distributed / 분산) ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **3. Cohesion và coupling phải đo bằng thay đổi (change / 변경)/thất bại (failure / 실패), không chỉ import đồ thị (graph / 그래프)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **4. Bounded ngữ cảnh (context / 맥락) là ngữ nghĩa (semantic / 의미적) ranh giới (boundary / 경계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Cohesion và coupling phải đo bằng thay đổi (change / 변경)/thất bại (failure / 실패), không chỉ import đồ thị (graph / 그래프)

High cohesion nghĩa responsibilities thực sự thay đổi cùng nhau. Low coupling nghĩa thành phần (component / 컴포넌트) ít các giả định (assumptions / 가정들) về internals của nhau.

Coupling có nhiều dạng:

```text
code coupling        -> imports/internal API
schema coupling      -> cùng database/table format
temporal coupling    -> caller phải đợi callee sống ngay lúc đó
release coupling     -> phải deploy cùng nhau
semantic coupling    -> cùng hiểu một event/field theo assumptions ngầm
operational coupling -> cùng quota/control plane/failure domain
```

Một kiến trúc (architecture / 아키텍처) có repository tách biệt vẫn có thể coupled mạnh ở thời gian chạy (runtime / 런타임).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hệ thống (system / 시스템) decomposition, services và boundaries**, **3. Cohesion và coupling phải đo bằng thay đổi (change / 변경)/thất bại (failure / 실패), không chỉ import đồ thị (graph / 그래프)** đã nêu tiêu chí phân biệt, còn **4. Bounded ngữ cảnh (context / 맥락) là ngữ nghĩa (semantic / 의미적) ranh giới (boundary / 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **5. trạng thái (state / 상태) placement quyết định kiến trúc (architecture / 아키텍처) nhiều hơn compute placement** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Bounded ngữ cảnh (context / 맥락) là ngữ nghĩa (semantic / 의미적) ranh giới (boundary / 경계)

Trong Domain-Driven thiết kế (design / 설계), bounded ngữ cảnh (context / 맥락) xác định nơi một mô hình (model / 모델) và vocabulary có meaning nhất quán. `Customer` trong billing có thể cần credit/payment định danh (identity / 식별자); `Customer` trong hỗ trợ (support / 지원) có thể cần contact/lịch sử (history / 이력).

Ranh giới (boundary / 경계) tốt thường đi theo **nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식)** hơn là thực thể (entity / 엔터티) CRUD. Nếu bất biến (invariant / 불변식) “một thứ tự (order / 순서) chỉ được settle một lần” thuộc payment/thứ tự (order / 순서) workflow, cần biết authority nào quyết định chuyển tiếp (transition / 전이) đó.

Hệ thống (system / 시스템) thiết kế (design / 설계) bắt đầu từ bất biến (invariant / 불변식) quyền sở hữu (ownership / 소유권) chứ không từ boxes trên diagram.

> **Chuyển mạch:** Trong **Hệ thống (system / 시스템) decomposition, services và boundaries**, **4. Bounded ngữ cảnh (context / 맥락) là ngữ nghĩa (semantic / 의미적) ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **5. trạng thái (state / 상태) placement quyết định kiến trúc (architecture / 아키텍처) nhiều hơn compute placement** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **6. dùng chung (shared / 공유) cơ sở dữ liệu (database / 데이터베이스) làm quyền sở hữu (ownership / 소유권) mơ hồ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. trạng thái (state / 상태) placement quyết định kiến trúc (architecture / 아키텍처) nhiều hơn compute placement

Stateless ứng dụng (application / 애플리케이션) replicas dễ quy mô (scale / 규모) vì yêu cầu (request / 요청) có thể chạy ở nhiều nodes. Nhưng durable trạng thái (state / 상태), bộ nhớ đệm (cache / 캐시), session, locks và coordination vẫn phải sống ở đâu đó.

Khi thiết kế, hỏi:

```text
source of truth ở đâu?
ai được ghi?
reader cần freshness mức nào?
state có partition được không?
failover có giữ authority không?
cache có thể stale trong bao lâu?
```

Nhiều kiến trúc (architecture / 아키텍처) thất bại (failure / 실패) là state-ownership bài toán (problem / 문제) bị che dưới “dịch vụ (service / 서비스) topology”.

> **Chuyển mạch:** Ở chặng này của **Hệ thống (system / 시스템) decomposition, services và boundaries**, **5. trạng thái (state / 상태) placement quyết định kiến trúc (architecture / 아키텍처) nhiều hơn compute placement** nêu điều cần giải thích; **6. dùng chung (shared / 공유) cơ sở dữ liệu (database / 데이터베이스) làm quyền sở hữu (ownership / 소유권) mơ hồ** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **7. Synchronous ranh giới (boundary / 경계) thêm availability và độ trễ (latency / 지연 시간) phụ thuộc (dependency / 의존성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. dùng chung (shared / 공유) cơ sở dữ liệu (database / 데이터베이스) làm quyền sở hữu (ownership / 소유권) mơ hồ

Nếu nhiều services trực tiếp mutate cùng tables, giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) có thể tiện nhưng lĩnh vực (domain / 도메인) quyền sở hữu (ownership / 소유권) trở nên mơ hồ. lược đồ (schema / 스키마) thay đổi (change / 변경) cần coordination; dịch vụ (service / 서비스) B có thể phá bất biến (invariant / 불변식) dịch vụ (service / 서비스) A.

Không phải dùng chung (shared / 공유) cơ sở dữ liệu (database / 데이터베이스) luôn sai. Nhưng cần biết đặc tả hợp đồng (contract / 계약): tables nào thật sự dùng chung (shared / 공유), ai sở hữu di chuyển (migration / 마이그레이션), ghi (write / 쓰기) paths nào hợp lệ và isolation/thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론) ra sao.

Tách cơ sở dữ liệu (database / 데이터베이스) per dịch vụ (service / 서비스) cũng không tự động tốt nếu kết quả là hàng chục synchronous remote reads cho một yêu cầu (request / 요청) đơn giản.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hệ thống (system / 시스템) decomposition, services và boundaries**, **6. dùng chung (shared / 공유) cơ sở dữ liệu (database / 데이터베이스) làm quyền sở hữu (ownership / 소유권) mơ hồ** cho ta quy tắc; **7. Synchronous ranh giới (boundary / 경계) thêm availability và độ trễ (latency / 지연 시간) phụ thuộc (dependency / 의존성)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **8. Asynchronous ranh giới (boundary / 경계) đổi coupling chứ không xóa coupling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Synchronous ranh giới (boundary / 경계) thêm availability và độ trễ (latency / 지연 시간) phụ thuộc (dependency / 의존성)

Synchronous yêu cầu (request / 요청)/phản hồi (response / 응답) dễ hiểu khi caller cần kết quả ngay. Nhưng caller độ trễ (latency / 지연 시간) ít nhất phụ thuộc đường găng (critical path / 임계 경로) của callee; availability của caller cũng có thể bị kéo xuống nếu callee thất bại (fail / 실패) và fallback không có.

Một chuỗi (chain / 사슬) dài:

```text
A → B → C → D
```

có thể tạo cumulative độ trễ (latency / 지연 시간), thử lại (retry / 재시도) amplification và cascading thất bại (failure / 실패). ngân sách thời gian chờ (timeout budget / 타임아웃 예산) phải propagate thay vì mỗi hop tự đặt một hết thời gian chờ (timeout / 타임아웃) đầy đủ mới.

Synchronous lời gọi (call / 호출) không xấu; nó chỉ tạo **temporal coupling** cần được ngân sách (budget / 예산) rõ.

> **Chuyển mạch:** Trong **Hệ thống (system / 시스템) decomposition, services và boundaries**, trường hợp ở **7. Synchronous ranh giới (boundary / 경계) thêm availability và độ trễ (latency / 지연 시간) phụ thuộc (dependency / 의존성)** cho thấy quy tắc hoạt động; **8. Asynchronous ranh giới (boundary / 경계) đổi coupling chứ không xóa coupling** kiểm tra nơi quy tắc ấy không còn áp dụng hoặc dễ bị hiểu nhầm. Từ đây, **9. Consistency yêu cầu (requirement / 요구사항) phải xuất phát từ bất biến (invariant / 불변식) nghiệp vụ (business / 비즈니스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Asynchronous ranh giới (boundary / 경계) đổi coupling chứ không xóa coupling

Sự kiện (event / 이벤트)/message giúp producer không cần bên tiêu thụ (consumer / 소비자) available tức thời. Nhưng ta thêm hàng đợi (queue / 큐) trạng thái (state / 상태), delivery ngữ nghĩa (semantics / 의미론), replay, thứ tự (ordering / 순서) và eventual consistency.

Questions cần trả lời:

```text
event là fact hay command?
at-least-once có tạo duplicate không?
consumer xử lý idempotent không?
partition/order key là gì?
backlog lớn thì freshness/SLO ra sao?
schema evolve thế nào khi nhiều consumer versions cùng tồn tại?
```

Event-driven kiến trúc (architecture / 아키텍처) không tự decoupled. Nó chuyển coupling từ call-time sang lược đồ (schema / 스키마)/ngữ nghĩa (semantic / 의미적)/time-history coupling.

> **Chuyển mạch:** Ở chặng này của **Hệ thống (system / 시스템) decomposition, services và boundaries**, **8. Asynchronous ranh giới (boundary / 경계) đổi coupling chứ không xóa coupling** đã nêu tiêu chí phân biệt, còn **9. Consistency yêu cầu (requirement / 요구사항) phải xuất phát từ bất biến (invariant / 불변식) nghiệp vụ (business / 비즈니스)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **10. Saga và compensation không phải quay lui (rollback / 롤백) phân tán** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Consistency yêu cầu (requirement / 요구사항) phải xuất phát từ bất biến (invariant / 불변식) nghiệp vụ (business / 비즈니스)

Không phải mọi dữ liệu (data / 데이터) cần strong consistency. Nhưng “eventual consistency” cũng không phải default excuse.

Ví dụ sản phẩm (product / 제품) danh mục (catalog / 카탈로그) có thể chấp nhận giá hiển thị stale vài giây trong một ngữ cảnh (context / 맥락), nhưng payment ledger có thể cần stronger serialization/idempotency guarantees.

Trước khi chọn replication/bộ nhớ đệm (cache / 캐시)/sự kiện (event / 이벤트) kiến trúc (architecture / 아키텍처), viết:

```text
state nào không được mâu thuẫn?
violation window tối đa bao lâu?
ai có authority quyết định state?
conflict có thể merge hay phải reject/serialize?
```

Consistency là sản phẩm (product / 제품)/lĩnh vực (domain / 도메인) thuộc tính (property / 속성) trước khi là cơ sở dữ liệu (database / 데이터베이스) tính năng (feature / 기능).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hệ thống (system / 시스템) decomposition, services và boundaries**, **10. Saga và compensation không phải quay lui (rollback / 롤백) phân tán** tiếp nhận điểm tựa từ **9. Consistency yêu cầu (requirement / 요구사항) phải xuất phát từ bất biến (invariant / 불변식) nghiệp vụ (business / 비즈니스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Idempotency là ranh giới (boundary / 경계) bất biến (invariant / 불변식) khi thử lại (retry / 재시도)/duplicate có thể xảy ra** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Saga và compensation không phải quay lui (rollback / 롤백) phân tán

Workflow qua nhiều services thường dùng cục bộ (local / 로컬) transactions + messaging. **Saga** có thể orchestrate hoặc choreograph steps và compensation.

Compensation là nghiệp vụ (business / 비즈니스) hành động (action / 동작) mới, không phải thời gian (time / 시간) machine. Nếu hàng đã giao, compensation có thể là return/refund; email đã gửi không thể “unsend” một cách transactionally.

Bất biến (invariant / 불변식) phải được thiết kế cho intermediate states. người dùng (user / 사용자) có thể thấy `PAYMENT_CAPTURED, SHIPMENT_PENDING`; hệ thống (system / 시스템) cần khôi phục (recovery / 복구)/reconciliation thay vì giả định atomicity toàn cầu.

> **Chuyển mạch:** Trong **Hệ thống (system / 시스템) decomposition, services và boundaries**, **10. Saga và compensation không phải quay lui (rollback / 롤백) phân tán** đã nêu tiêu chí phân biệt, còn **11. Idempotency là ranh giới (boundary / 경계) bất biến (invariant / 불변식) khi thử lại (retry / 재시도)/duplicate có thể xảy ra** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **12. hàng đợi (queue / 큐) là trạng thái (state / 상태) và debt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Idempotency là ranh giới (boundary / 경계) bất biến (invariant / 불변식) khi thử lại (retry / 재시도)/duplicate có thể xảy ra

Mạng (network / 네트워크) hết thời gian chờ (timeout / 타임아웃) tạo ambiguity: yêu cầu (request / 요청) có thể đã được máy chủ (server / 서버) thực hiện nhưng phản hồi (response / 응답) bị mất. thử lại (retry / 재시도) có thể lặp side tác động (effect / 효과).

Idempotency key/deduplication giúp cùng logical thao tác (operation / 연산) không bị áp dụng nhiều lần theo chính sách (policy / 정책). Nhưng lưu trữ (storage / 저장소)/thời gian tồn tại (lifetime / 수명) của dedupe bản ghi (record / 레코드), key phạm vi (scope / 범위) và phản hồi (response / 응답) replay ngữ nghĩa (semantics / 의미론) phải được định nghĩa.

“HTTP PUT idempotent” ở giao thức (protocol / 프로토콜) mức (level / 수준) không tự chứng minh nghiệp vụ (business / 비즈니스) side effects bên dưới idempotent.

> **Chuyển mạch:** Ở chặng này của **Hệ thống (system / 시스템) decomposition, services và boundaries**, **11. Idempotency là ranh giới (boundary / 경계) bất biến (invariant / 불변식) khi thử lại (retry / 재시도)/duplicate có thể xảy ra** đã nêu tiêu chí phân biệt, còn **12. hàng đợi (queue / 큐) là trạng thái (state / 상태) và debt** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **13. bộ nhớ đệm (cache / 캐시) là một replicated trạng thái (state / 상태) hệ thống (system / 시스템) nhỏ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. hàng đợi (queue / 큐) là trạng thái (state / 상태) và debt

Message broker, luồng thực thi (thread / 스레드) hàng đợi (queue / 큐) hoặc async job hàng đợi (queue / 큐) không chỉ là vận chuyển (transport / 전송). hàng đợi (queue / 큐) chứa công việc (work / 작업) chưa hoàn thành — một dạng debt.

Khi producer tỷ lệ (rate / 비율) vượt bên tiêu thụ (consumer / 소비자) dịch vụ (service / 서비스) tỷ lệ (rate / 비율):

```text
backlog tăng
→ processing lag tăng
→ data freshness giảm
→ deadline có thể hết trước khi xử lý
→ recovery time sau incident kéo dài
```

Backpressure/admission điều khiển (control / 제어) cần đặt ở nơi producer nhận được sức chứa (capacity / 용량) tín hiệu (signal / 신호). hàng đợi (queue / 큐) vô hạn chỉ trì hoãn thất bại (failure / 실패).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hệ thống (system / 시스템) decomposition, services và boundaries**, **13. bộ nhớ đệm (cache / 캐시) là một replicated trạng thái (state / 상태) hệ thống (system / 시스템) nhỏ** tiếp nhận điểm tựa từ **12. hàng đợi (queue / 큐) là trạng thái (state / 상태) và debt** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Partitioning tăng sức chứa (capacity / 용량) nhưng tạo hotspot và cross-partition chi phí (cost / 비용)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. bộ nhớ đệm (cache / 캐시) là một replicated trạng thái (state / 상태) hệ thống (system / 시스템) nhỏ

Bộ nhớ đệm (cache / 캐시) làm read đường dẫn (path / 경로) nhanh nhưng tạo bản sao (copy / 복사) trạng thái (state / 상태) ngoài nguồn chuẩn (source of truth / 정본). Cần định nghĩa freshness, vô hiệu hóa (invalidation / 무효화), stampede hành vi (behavior / 동작) và thất bại (failure / 실패) fallback.

Nếu bộ nhớ đệm (cache / 캐시) outage khiến toàn traffic đập vào cơ sở dữ liệu (database / 데이터베이스), bộ nhớ đệm (cache / 캐시) đã trở thành **load-bearing phụ thuộc (dependency / 의존성)**. sức chứa (capacity / 용량) plan phải xét trượt bộ nhớ đệm (cache miss / 캐시 미스) storm, không chỉ normal hit ratio.

Bộ nhớ đệm (cache / 캐시) thiết kế (design / 설계) vì vậy là hệ thống (system / 시스템) thiết kế (design / 설계), consistency và độ tin cậy (reliability / 신뢰성) cùng lúc.

> **Chuyển mạch:** Trong **Hệ thống (system / 시스템) decomposition, services và boundaries**, **14. Partitioning tăng sức chứa (capacity / 용량) nhưng tạo hotspot và cross-partition chi phí (cost / 비용)** tiếp nhận điểm tựa từ **13. bộ nhớ đệm (cache / 캐시) là một replicated trạng thái (state / 상태) hệ thống (system / 시스템) nhỏ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Replication tăng availability/read quy mô (scale / 규모) nhưng thêm authority bài toán (problem / 문제)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Partitioning tăng sức chứa (capacity / 용량) nhưng tạo hotspot và cross-partition chi phí (cost / 비용)

Sharding chia trạng thái (state / 상태)/công việc (work / 작업) theo key để tăng horizontal sức chứa (capacity / 용량). Nhưng shard key quyết định locality và balance.

Một celebrity tenant/hot key có thể phá giả định (assumption / 가정) uniform phân phối (distribution / 분포). Cross-shard truy vấn (query / 쿼리)/giao dịch (transaction / 트랜잭션) thêm coordination. Rebalancing cần move trạng thái (state / 상태) trong khi traffic vẫn chạy.

Không nên nói “hệ thống (system / 시스템) horizontally scalable” nếu chưa biết đơn vị (unit / 단위) partition và hotspot chiến lược (strategy / 전략).

> **Chuyển mạch:** Ở chặng này của **Hệ thống (system / 시스템) decomposition, services và boundaries**, **14. Partitioning tăng sức chứa (capacity / 용량) nhưng tạo hotspot và cross-partition chi phí (cost / 비용)** cho ta quy tắc; **15. Replication tăng availability/read quy mô (scale / 규모) nhưng thêm authority bài toán (problem / 문제)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **16. bộ cân bằng tải (load balancer / 로드 밸런서) và khám phá dịch vụ (service discovery / 서비스 디스커버리) là điều khiển (control / 제어) loops** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Replication tăng availability/read quy mô (scale / 규모) nhưng thêm authority bài toán (problem / 문제)

Replica chỉ hữu ích nếu giao thức (protocol / 프로토콜) xác định ai được ghi (write / 쓰기), khi nào ghi (write / 쓰기) committed và failover tránh split-brain.

Async replica có lag; read-after-write có thể thất bại (fail / 실패) nếu reader đi tới follower cũ. Sync quorum tăng consistency/durability nhưng thêm độ trễ (latency / 지연 시간) và giảm availability dưới partition nhất định.

Replication không phải bản sao (copy / 복사) count; nó là consistency giao thức (protocol / 프로토콜) dưới thất bại (failure / 실패) mô hình (model / 모델).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hệ thống (system / 시스템) decomposition, services và boundaries**, **15. Replication tăng availability/read quy mô (scale / 규모) nhưng thêm authority bài toán (problem / 문제)** cho ta quy tắc; **16. bộ cân bằng tải (load balancer / 로드 밸런서) và khám phá dịch vụ (service discovery / 서비스 디스커버리) là điều khiển (control / 제어) loops** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **17. API gateway/dịch vụ (service / 서비스) mesh di chuyển cross-cutting lô-gic (logic / 논리) xuống hạ tầng (infrastructure / 인프라)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. bộ cân bằng tải (load balancer / 로드 밸런서) và khám phá dịch vụ (service discovery / 서비스 디스커버리) là điều khiển (control / 제어) loops

Routing tầng (layer / 계층) phải biết backend nào tồn tại, healthy và còn sức chứa (capacity / 용량). Health check quá nông có thể gửi traffic tới nút (node / 노드) sống tiến trình (process / 프로세스) nhưng đang overload. Health dữ liệu (data / 데이터) stale có thể tạo oscillation/hotspot.

Liên kết (connection / 연결) reuse cũng làm tải (load / 로드) balancing stateful: nhiều long-lived HTTP/2 connections có thể giữ traffic trên old subset nodes dù fleet đã quy mô (scale / 규모).

Topology điều khiển (control / 제어) là hệ động (dynamic system / 동적 시스템), không chỉ round-robin thuật toán (algorithm / 알고리즘).

> **Chuyển mạch:** Trong **Hệ thống (system / 시스템) decomposition, services và boundaries**, **17. API gateway/dịch vụ (service / 서비스) mesh di chuyển cross-cutting lô-gic (logic / 논리) xuống hạ tầng (infrastructure / 인프라)** tiếp nhận điểm tựa từ **16. bộ cân bằng tải (load balancer / 로드 밸런서) và khám phá dịch vụ (service discovery / 서비스 디스커버리) là điều khiển (control / 제어) loops** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. ranh giới bảo mật (security boundary / 보안 경계) phải đi cùng dịch vụ (service / 서비스) ranh giới (boundary / 경계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. API gateway/dịch vụ (service / 서비스) mesh di chuyển cross-cutting lô-gic (logic / 논리) xuống hạ tầng (infrastructure / 인프라)

Gateway có thể centralize auth, tỷ lệ (rate / 비율) limit, routing và khả năng quan sát (observability / 관측 가능성) cho north-south traffic. dịch vụ (service / 서비스) mesh có thể xử lý mTLS, retries, telemetry và routing east-west.

Lợi ích là chính sách (policy / 정책) consistency; chi phí (cost / 비용) là thêm proxies/điều khiển (control / 제어) plane/thất bại (failure / 실패) modes. Nếu proxy tự thử lại (retry / 재시도) và ứng dụng (application / 애플리케이션) cũng thử lại (retry / 재시도), tải (load / 로드) amplification tăng mà nhóm (team / 팀) khó nhìn thấy.

Hạ tầng (infrastructure / 인프라) lớp trừu tượng (abstraction / 추상화) phải expose bằng chứng (evidence / 증거) đủ để gỡ lỗi (debug / 디버그), nếu không nó biến thất bại (failure / 실패) thành “mạng (network / 네트워크) mystery”.

> **Chuyển mạch:** Ở chặng này của **Hệ thống (system / 시스템) decomposition, services và boundaries**, **17. API gateway/dịch vụ (service / 서비스) mesh di chuyển cross-cutting lô-gic (logic / 논리) xuống hạ tầng (infrastructure / 인프라)** đã nêu tiêu chí phân biệt, còn **18. ranh giới bảo mật (security boundary / 보안 경계) phải đi cùng dịch vụ (service / 서비스) ranh giới (boundary / 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **19. miền lỗi (failure domain / 장애 도메인) phải tường minh (explicit / 명시적)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. ranh giới bảo mật (security boundary / 보안 경계) phải đi cùng dịch vụ (service / 서비스) ranh giới (boundary / 경계)

Tách dịch vụ (service / 서비스) mà mọi dịch vụ (service / 서비스) tin cùng credential/gốc (root / 루트) permission thì containment kém. Mỗi ranh giới (boundary / 경계) nên xác định principal nào được gọi, hành động (action / 동작) nào được phép và secret/key phạm vi (scope / 범위) nào cần thiết.

mTLS chứng minh dịch vụ (service / 서비스) định danh (identity / 식별자) không thay authorization. mạng (network / 네트워크) segmentation không thay ứng dụng (application / 애플리케이션) chính sách (policy / 정책). Least privilege làm dịch vụ (service / 서비스) decomposition trở thành incident-containment kiến trúc (architecture / 아키텍처).

Đọc [PKI/service identity](../../07_security_reliability/advanced/02_pki_certificate_validation_mtls_and_service_identity.md).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hệ thống (system / 시스템) decomposition, services và boundaries**, **18. ranh giới bảo mật (security boundary / 보안 경계) phải đi cùng dịch vụ (service / 서비스) ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **19. miền lỗi (failure domain / 장애 도메인) phải tường minh (explicit / 명시적)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **20. Graceful degradation cần giữ bất biến (invariant / 불변식) quan trọng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. miền lỗi (failure domain / 장애 도메인) phải tường minh (explicit / 명시적)

Hai replicas cùng zone, cùng cơ sở dữ liệu (database / 데이터베이스), cùng KMS hoặc cùng triển khai (deployment / 배포) sản phẩm tạo ra (artifact / 산출물) có thể cùng thất bại (fail / 실패). kiến trúc (architecture / 아키텍처) diagram chỉ vẽ nhiều boxes nhưng phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) vẫn có dùng chung (shared / 공유) single điểm (point / 지점).

Khi thiết kế redundancy, hỏi:

```text
failure nào ta muốn survive?
replicas có độc lập trước failure đó không?
control plane có shared dependency nào?
failover path đã được test chưa?
```

“Multi-instance” không đồng nghĩa multi-failure-domain.

> **Chuyển mạch:** Trong **Hệ thống (system / 시스템) decomposition, services và boundaries**, **20. Graceful degradation cần giữ bất biến (invariant / 불변식) quan trọng** tiếp nhận điểm tựa từ **19. miền lỗi (failure domain / 장애 도메인) phải tường minh (explicit / 명시적)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. khả năng quan sát (observability / 관측 가능성) phải được thiết kế tại ranh giới (boundary / 경계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Graceful degradation cần giữ bất biến (invariant / 불변식) quan trọng

Khi phụ thuộc (dependency / 의존성) thất bại (fail / 실패), hệ thống (system / 시스템) có thể serve stale bộ nhớ đệm (cache / 캐시), bỏ recommendation, chuyển read-only hoặc reject optional công việc (work / 작업).

Nhưng không được degrade bằng cách bỏ authorization, double-charge hoặc trả committed success khi durability chưa đạt. Degradation phải phân biệt optional chất lượng (quality / 품질) với tính đúng đắn (correctness / 정확성)/bảo mật (security / 보안) bất biến (invariant / 불변식).

Thiết kế fallback là sản phẩm (product / 제품)/hệ thống (system / 시스템) quyết định (decision / 결정) trước sự cố (incident / 인시던트), không phải improvisation lúc outage.

> **Chuyển mạch:** Ở chặng này của **Hệ thống (system / 시스템) decomposition, services và boundaries**, **20. Graceful degradation cần giữ bất biến (invariant / 불변식) quan trọng** đã nêu tiêu chí phân biệt, còn **21. khả năng quan sát (observability / 관측 가능성) phải được thiết kế tại ranh giới (boundary / 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **22. Conway's Law và quyền sở hữu (ownership / 소유권) là một phần của thời gian chạy (runtime / 런타임) kiến trúc (architecture / 아키텍처)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. khả năng quan sát (observability / 관측 가능성) phải được thiết kế tại ranh giới (boundary / 경계)

Mỗi remote ranh giới (boundary / 경계) nên giữ nhân quả (causal / 인과적) ngữ cảnh (context / 맥락) đủ để trả lời:

```text
caller nào?
principal nào?
attempt thứ mấy?
deadline còn bao nhiêu?
queue wait bao lâu?
downstream service time bao lâu?
version/schema nào?
```

Dấu vết (trace / 추적), metrics và structured logs cần gắn với đặc tả hợp đồng (contract / 계약). Nếu chỉ có CPU đồ thị (graph / 그래프) của từng dịch vụ (service / 서비스) mà không có end-to-end ngữ cảnh (context / 맥락), phân tán (distributed / 분산) kiến trúc (architecture / 아키텍처) làm debugging khó hơn rất nhiều.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hệ thống (system / 시스템) decomposition, services và boundaries**, **21. khả năng quan sát (observability / 관측 가능성) phải được thiết kế tại ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **22. Conway's Law và quyền sở hữu (ownership / 소유권) là một phần của thời gian chạy (runtime / 런타임) kiến trúc (architecture / 아키텍처)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **23. phân tán (distributed / 분산) monolith là dạng thất bại (failure mode / 실패 모드) của decomposition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Conway's Law và quyền sở hữu (ownership / 소유권) là một phần của thời gian chạy (runtime / 런타임) kiến trúc (architecture / 아키텍처)

Hệ thống (system / 시스템) cấu trúc (structure / 구조) thường phản chiếu communication cấu trúc (structure / 구조) của organization. Nếu một dịch vụ (service / 서비스) “owned” bởi ba teams và mọi thay đổi (change / 변경) cần committee, dịch vụ (service / 서비스) ranh giới (boundary / 경계) không tạo autonomy.

Ngược lại, nhóm (team / 팀) ranh giới (boundary / 경계) không nên ép tạo mạng (network / 네트워크) dịch vụ (service / 서비스) nếu ranh giới mô-đun (module boundary / 모듈 경계) trong monolith đã đủ.

Kiến trúc (architecture / 아키텍처) là socio-technical: mã (code / 코드), dữ liệu (data / 데이터), deploy, on-call và quyết định (decision / 결정) authority nên tương đối aligned.

> **Chuyển mạch:** Trong **Hệ thống (system / 시스템) decomposition, services và boundaries**, **23. phân tán (distributed / 분산) monolith là dạng thất bại (failure mode / 실패 모드) của decomposition** tiếp nhận điểm tựa từ **22. Conway's Law và quyền sở hữu (ownership / 소유권) là một phần của thời gian chạy (runtime / 런타임) kiến trúc (architecture / 아키텍처)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. hiệu năng (performance / 성능) pressure làm ranh giới (boundary / 경계) hành vi (behavior / 동작) thay đổi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. phân tán (distributed / 분산) monolith là dạng thất bại (failure mode / 실패 모드) của decomposition

Dấu hiệu:

```text
services deploy cùng lúc
shared DB writes everywhere
chatty synchronous calls
cross-service transaction assumptions
one failure cascades toàn graph
schema change cần coordinated rollout lớn
```

Ta nhận mạng (network / 네트워크)/ops chi phí (cost / 비용) của hệ thống phân tán (distributed system / 분산 시스템) nhưng vẫn giữ coupling của monolith.

Fix thường là làm ranh giới (boundary / 경계) sâu hơn—quyền sở hữu (ownership / 소유권)/contracts—không phải chia thêm services.

> **Chuyển mạch:** Ở chặng này của **Hệ thống (system / 시스템) decomposition, services và boundaries**, **23. phân tán (distributed / 분산) monolith là dạng thất bại (failure mode / 실패 모드) của decomposition** đã nêu tiêu chí phân biệt, còn **24. hiệu năng (performance / 성능) pressure làm ranh giới (boundary / 경계) hành vi (behavior / 동작) thay đổi** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **25. bằng chứng (evidence / 증거) để đánh giá một ranh giới (boundary / 경계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. hiệu năng (performance / 성능) pressure làm ranh giới (boundary / 경계) hành vi (behavior / 동작) thay đổi

Ở low tải (load / 로드), remote lời gọi (call / 호출) chi phí (cost / 비용) có thể nhỏ. Gần saturation, mỗi ranh giới (boundary / 경계) thêm hàng đợi (queue / 큐), thử lại (retry / 재시도) và connection-pool pressure. Fan-out khuếch đại tail độ trễ (latency / 지연 시간); trượt bộ nhớ đệm (cache miss / 캐시 미스) storm tạo tải (load / 로드) lên nguồn (source / 소스); DB pool chuyển hàng đợi (queue / 큐) xuống lưu trữ (storage / 저장소)/locks.

Hệ thống (system / 시스템) thiết kế (design / 설계) phải được load-test ở operating region thật. kiến trúc (architecture / 아키텍처) đúng về chức năng nhưng collapse dưới overload là kiến trúc (architecture / 아키텍처) thiếu sức chứa (capacity / 용량)/thất bại (failure / 실패) lập luận (reasoning / 추론).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hệ thống (system / 시스템) decomposition, services và boundaries**, **24. hiệu năng (performance / 성능) pressure làm ranh giới (boundary / 경계) hành vi (behavior / 동작) thay đổi** đã nêu tiêu chí phân biệt, còn **25. bằng chứng (evidence / 증거) để đánh giá một ranh giới (boundary / 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **26. quyết định (decision / 결정) khung phần mềm (framework / 프레임워크) thay vì mẫu (pattern / 패턴) catalogue** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. bằng chứng (evidence / 증거) để đánh giá một ranh giới (boundary / 경계)

Một ranh giới (boundary / 경계) khỏe thường có bằng chứng (evidence / 증거) về:

```text
change/deploy independence
request/event volume và latency
error/timeout/retry rate
queue/backlog
schema compatibility failures
authorization decisions
resource saturation
dependencies/failure propagation
ownership/on-call clarity
```

Không phải mọi chỉ số (metric / 지표) cần dashboard riêng. Nhưng nếu không thể biết ranh giới (boundary / 경계) đang chờ gì, thất bại (fail / 실패) ở đâu và ai sở hữu trạng thái (state / 상태), kiến trúc (architecture / 아키텍처) đang thiếu khả năng quan sát (observability / 관측 가능성)/quyền sở hữu (ownership / 소유권).

> **Chuyển mạch:** Trong **Hệ thống (system / 시스템) decomposition, services và boundaries**, **25. bằng chứng (evidence / 증거) để đánh giá một ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **26. quyết định (decision / 결정) khung phần mềm (framework / 프레임워크) thay vì mẫu (pattern / 패턴) catalogue** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **27. Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. quyết định (decision / 결정) khung phần mềm (framework / 프레임워크) thay vì mẫu (pattern / 패턴) catalogue

Khi cần tách dịch vụ (service / 서비스) hoặc chọn tương tác (interaction / 상호작용) mô hình (model / 모델), lập luận (reasoning / 추론) chuỗi (sequence / 시퀀스) hữu ích là:

```text
1. invariant/state nào cần ownership?
2. change nào cần độc lập?
3. consistency/freshness requirement là gì?
4. expected load và partition key là gì?
5. failure nào phải contain/survive?
6. sync hay async phù hợp deadline và semantics?
7. security principal/trust boundary nằm đâu?
8. observability/evidence nào chứng minh contract?
9. operational complexity có đáng với benefit không?
```

Chỉ sau đó mới chọn hàng đợi (queue / 큐), bộ nhớ đệm (cache / 캐시), cơ sở dữ liệu (database / 데이터베이스), gateway hay dịch vụ (service / 서비스) mesh cụ thể.

> **Chuyển mạch:** Ở chặng này của **Hệ thống (system / 시스템) decomposition, services và boundaries**, **27. Mô hình tư duy** gom các mảnh từ **26. quyết định (decision / 결정) khung phần mềm (framework / 프레임워크) thay vì mẫu (pattern / 패턴) catalogue** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những hiểu nhầm thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Mô hình tư duy

> hệ thống (system / 시스템) thiết kế (design / 설계) là **đặt quyền sở hữu (ownership / 소유권), trạng thái (state / 상태), communication và thất bại (failure / 실패) boundaries**. ranh giới (boundary / 경계) tốt gom bất biến (invariant / 불변식) và authority rõ, có đặc tả hợp đồng (contract / 계약) có thể evolve, giới hạn blast radius và có bằng chứng (evidence / 증거) khi hành vi (behavior / 동작) xấu. ranh giới (boundary / 경계) xấu chỉ chuyển hàm (function / 함수) lời gọi (call / 호출) thành mạng (network / 네트워크) lời gọi (call / 호출) rồi thêm hết thời gian chờ (timeout / 타임아웃)/thử lại (retry / 재시도) mà không giảm coupling. Technology là hiện thực (implementation / 구현); bất biến (invariant / 불변식) và thất bại (failure / 실패) mô hình (model / 모델) mới là kiến trúc.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hệ thống (system / 시스템) decomposition, services và boundaries**, **27. Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những hiểu nhầm thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu nhầm thường gặp

**“Microservices quy mô (scale / 규모) tốt hơn monolith.”** Chỉ khi bottleneck/tải công việc (workload / 워크로드) thật sự partition được và ranh giới (boundary / 경계) có independent sức chứa (capacity / 용량).

**“Event-driven nghĩa decoupled.”** Coupling chuyển sang sự kiện (event / 이벤트) ngữ nghĩa (semantics / 의미론), thứ tự (ordering / 순서), lược đồ (schema / 스키마) và backlog.

**“Nhiều replicas nghĩa high availability.”** Chỉ khi thất bại (failure / 실패) domains và authority/failover giao thức (protocol / 프로토콜) phù hợp.

**“hệ thống (system / 시스템) thiết kế (design / 설계) interview mẫu (pattern / 패턴) là kiến trúc vận hành (production architecture / 운영 아키텍처).”** mẫu (pattern / 패턴) chỉ hữu ích khi các giả định (assumptions / 가정들)/bất biến (invariant / 불변식)/thất bại (failure / 실패) mô hình (model / 모델) khớp hệ thống (system / 시스템) thật.

> **Chuyển mạch:** Trong **Hệ thống (system / 시스템) decomposition, services và boundaries**, **Những hiểu nhầm thường gặp** đã nêu tiêu chí phân biệt, còn **Kết nối** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc [modularity/API](./00_abstraction_modularity_interfaces_and_apis.md), [state/queues/backpressure](./03_state_queues_backpressure_and_boundaries.md), [event-driven](./06_event_driven_and_stream_processing.md), [distributed consistency](../06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md), [capacity engineering](../../08_software_systems/advanced/01_capacity_planning_utilization_knee_and_admission_control.md), [architecture decisions](../../09_software_engineering/advanced/00_architecture_decisions_evolution_and_socio_technical_constraints.md), [end-to-end request path](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md) và [debugging xuyên abstraction layers](../../90_connections/advanced/00_debugging_across_abstraction_layers.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
