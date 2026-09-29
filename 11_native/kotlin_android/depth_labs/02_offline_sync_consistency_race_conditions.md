# Độ sâu (depth / 깊이) Lab 02 — Offline-First, Consistency, Race điều kiện (condition / 조건) và Sync tính đúng đắn (correctness / 정확성)

> **Mạch đọc:** Đặt **độ sâu (depth / 깊이) Lab 02 — Offline-First, Consistency, Race điều kiện (condition / 조건) và Sync tính đúng đắn (correctness / 정확성)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Trước tiên phải phân biệt ba khái niệm: nguồn chuẩn (source of truth / 정본), authority và replica** sang **2. Consistency mô hình (model / 모델) phải được chọn có chủ ý**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Offline-first không có nghĩa đơn giản là “lưu dữ liệu vào Room để app vẫn mở được khi mất mạng”. Một hệ thống offline-first thật sự phải trả lời những câu khó hơn: cục bộ (local / 로컬) và remote có thể lệch nhau bao lâu, mutation nào được phép reorder, thử lại (retry / 재시도) có tạo duplicate tác động (effect / 효과) không, nhiều thiết bị (device / 장치) cùng sửa thì merge thế nào, logout giữa lúc sync ra sao, và nếu app bị kill sau cục bộ (local / 로컬) lần ghi nhận (commit / 커밋) nhưng trước remote lần ghi nhận (commit / 커밋) thì người dùng (user / 사용자) intent có còn tồn tại hay không.

Độ sâu (depth / 깊이) Lab này đi sâu vào **consistency mô hình (model / 모델)** và **thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론)** của sync engine.

---

## 1. Trước tiên phải phân biệt ba khái niệm: nguồn chuẩn (source of truth / 정본), authority và replica

Trong nhiều app offline-first:

```text
Room = local source of truth cho UI
Server = business authority cuối cùng
Device local DB = một replica có thể tạm lệch server
```

Ba vai trò này không mâu thuẫn.

UI đọc Room để có trải nghiệm reactive và offline. máy chủ (server / 서버) vẫn có thể là nơi quyết định nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙) cuối cùng. Room có thể chứa desired trạng thái (state / 상태) chưa được máy chủ (server / 서버) xác nhận.

Điều nguy hiểm là dùng từ “nguồn chuẩn (source of truth / 정본)” mà không nói rõ phạm vi. Hãy luôn hỏi:

```text
truth cho UI hiện tại?
truth cho billing?
truth cho authorization?
truth cho conflict resolution?
```

Ví dụ permission server-side không bao giờ nên lấy Room làm authority cuối cùng chỉ vì UI đang observe Room.

---

## 2. Consistency mô hình (model / 모델) phải được chọn có chủ ý

Không phải mọi tính năng (feature / 기능) cần strong consistency.

Một bookmark có thể chấp nhận eventual consistency:

```text
user tap -> local update ngay -> sync server sau
```

Nhưng chuyển tiền không thể chỉ “sync khi có mạng” theo cùng mô hình tư duy (mental model / 사고 모델).

Hãy phân loại thao tác (operation / 연산):

| Loại dữ liệu | Consistency thường phù hợp |
|---|---|
| UI preference | local-first |
| bookmark/favorite | eventual consistency |
| xã hội (social / 사회적) like | eventual + xung đột (conflict / 충돌) chính sách (policy / 정책) |
| draft document | cục bộ (local / 로컬) durable + merge/versioning |
| inventory reservation | server-authoritative |
| payment | server-authoritative + idempotency |
| authorization | server-authoritative |

Offline-first là chiến lược, không phải dogma áp cho mọi mutation.

---

## 3. Outbox mẫu (pattern / 패턴) bảo vệ người dùng (user / 사용자) intent khỏi tiến trình (process / 프로세스) death

Nếu mã (code / 코드) làm:

```kotlin
localDao.setBookmarked(id, true)
api.setBookmarked(id, true)
```

và tiến trình (process / 프로세스) chết sau dòng đầu, cục bộ (local / 로컬) trạng thái (state / 상태) đã đổi nhưng không còn thứ gì nhắc hệ thống phải sync máy chủ (server / 서버).

Outbox giải quyết bằng cách transactionally lưu cả trạng thái (state / 상태) và pending intent:

```text
transaction
├── update article desired state
└── insert mutation into outbox
```

Sau giao dịch (transaction / 트랜잭션), bất biến (invariant / 불변식) là:

```text
nếu local state cần remote sync
=> luôn tồn tại durable mutation mô tả intent đó
```

Worker chỉ là executor đọc outbox. Worker có chết thì intent vẫn còn.

---

## 4. Outbox row phải mô tả intent, không chỉ yêu cầu (request / 요청) body

Một outbox tốt thường cần siêu dữ liệu (metadata / 메타데이터) như:

```kotlin
data class PendingMutation(
    val mutationId: String,
    val accountId: String,
    val entityType: String,
    val entityId: String,
    val operation: String,
    val payload: ByteArray,
    val createdAt: Instant,
    val attemptCount: Int,
    val nextAttemptAt: Instant?,
    val state: MutationState
)
```

`accountId` đặc biệt quan trọng. Nếu người dùng (user / 사용자) logout rồi login account khác, worker không được vô tình gửi mutation của account cũ với đơn vị từ (token / 토큰) mới.

Mutation quyền sở hữu (ownership / 소유권) phải được không gian tên (namespace / 네임스페이스) theo session/account.

---

## 5. thử lại (retry / 재시도) chính sách (policy / 정책) phải bắt đầu từ idempotency

Thử lại (retry / 재시도) an toàn nếu thao tác (operation / 연산) có thể thực hiện nhiều lần mà nghiệp vụ (business / 비즈니스) kết quả (outcome / 결과) không đổi.

Ví dụ tốt:

```http
PUT /articles/42/bookmark
{
  "bookmarked": true
}
```

Gửi `true` năm lần vẫn có cùng kết quả (outcome / 결과).

Nguy hiểm hơn:

```http
POST /articles/42/toggle-bookmark
```

Nếu phản hồi (response / 응답) lần đầu bị mất rồi máy khách (client / 클라이언트) thử lại (retry / 재시도), bookmark có thể bị toggle hai lần và quay về trạng thái cũ.

Thiết kế (design / 설계) API nên ưu tiên **set desired trạng thái (state / 상태)** thay vì “toggle” khi thao tác (operation / 연산) cần thử lại (retry / 재시도).

---

## 6. Idempotency key bảo vệ thao tác (operation / 연산) có side tác động (effect / 효과)

Với thao tác (operation / 연산) không tự nhiên idempotent, dùng mutation id:

```http
POST /payments
Idempotency-Key: 55c0f6d2-...
```

Máy chủ (server / 서버) lưu ánh xạ (mapping / 매핑):

```text
idempotencyKey -> result
```

Nếu máy khách (client / 클라이언트) thử lại (retry / 재시도) cùng key, máy chủ (server / 서버) trả kết quả (result / 결과) cũ.

Điểm quan trọng là mutation id phải được tạo **trước lần gửi đầu tiên** và persist cùng durable intent. Tạo UUID mới cho mỗi thử lại (retry / 재시도) phá toàn bộ ý nghĩa idempotency.

---

## 7. hết thời gian chờ (timeout / 타임아웃) không đồng nghĩa thao tác (operation / 연산) thất bại

Timeline:

```text
T0 client gửi request
T1 server nhận
T2 server commit DB
T3 response trên đường về
T4 network đứt
T5 client timeout
```

Máy khách (client / 클라이언트) chỉ biết “không nhận phản hồi (response / 응답)”, không biết máy chủ (server / 서버) có lần ghi nhận (commit / 커밋) hay chưa.

Đây là ambiguous kết quả (outcome / 결과).

Vì vậy:

```text
timeout -> UNKNOWN
```

không phải luôn:

```text
timeout -> FAILED
```

Với thao tác (operation / 연산) quan trọng, máy khách (client / 클라이언트) cần idempotency hoặc endpoint truy vấn (query / 쿼리) trạng thái thao tác (operation / 연산).

---

## 8. Exponential backoff không đủ nếu không có jitter

Nếu hàng trăm nghìn thiết bị (device / 장치) cùng thử lại (retry / 재시도) sau outage với lịch:

```text
1s, 2s, 4s, 8s, 16s
```

chúng có thể cùng quay lại máy chủ (server / 서버) đúng những thời điểm giống nhau, tạo **thundering herd**.

Thêm jitter:

```text
baseDelay = 8s
actualDelay = random(4s..12s)
```

Mục tiêu là phân tán thử lại (retry / 재시도) tải (load / 로드).

Thử lại (retry / 재시도) chính sách (policy / 정책) nên dựa trên lỗi (error / 오류) lớp (class / 클래스):

```text
network unavailable -> retry
timeout -> retry nếu operation idempotent
HTTP 429 -> honor Retry-After nếu có
HTTP 5xx -> bounded retry
HTTP 401 -> session recovery, không blind retry
HTTP 400 validation -> không retry
HTTP 403 -> không retry như network error
```

---

## 9. thứ tự (ordering / 순서) chỉ cần được bảo vệ khi nghiệp vụ (business / 비즈니스) yêu cầu

Giả sử người dùng (user / 사용자) thao tác:

```text
T1 bookmark = true
T2 bookmark = false
T3 bookmark = true
```

Nếu ba mutation được gửi song song, phản hồi (response / 응답) có thể về thứ tự khác.

Nếu API dùng desired trạng thái (state / 상태) và máy chủ (server / 서버) last-write-wins theo phiên bản (version / 버전), ta có thể collapse hàng đợi (queue / 큐).

Thay vì gửi 3 mutation:

```text
true
false
true
```

có thể chỉ cần giữ desired trạng thái (state / 상태) cuối:

```text
true
```

Nhưng chỉ được compact nếu ngữ nghĩa (semantics / 의미론) cho phép.

Một chuỗi (sequence / 시퀀스) “create comment -> edit comment -> delete comment” không thể compact tùy tiện nếu remote định danh (identity / 식별자) chưa tồn tại.

---

## 10. hàng đợi (queue / 큐) compaction giúp giảm sync debt

Với preference-like mutation, outbox có thể compact:

```text
SET_BOOKMARK true
SET_BOOKMARK false
SET_BOOKMARK true
```

thành:

```text
SET_BOOKMARK true
```

Điều này giảm yêu cầu (request / 요청) count và thời gian khôi phục (recovery / 복구) sau offline dài.

Tuy nhiên mutation compaction phải bảo vệ kiểm tra (audit / 감사)/nghiệp vụ (business / 비즈니스) ngữ nghĩa (semantics / 의미론). Payment sự kiện (event / 이벤트), analytics cần thứ tự (ordering / 순서) hoặc append-only lịch sử (history / 이력) có thể không được compact.

---

## 11. phiên bản (version / 버전) number giúp chống stale phản hồi (response / 응답) overwrite

Giả sử cục bộ (local / 로컬) thực thể (entity / 엔터티) có:

```text
version = 10
```

Máy khách (client / 클라이언트) gửi cập nhật (update / 업데이트) A dựa trên phiên bản (version / 버전) 10. Trong khi yêu cầu (request / 요청) đang chạy, cập nhật (update / 업데이트) B từ thiết bị (device / 장치) khác đưa máy chủ (server / 서버) lên phiên bản (version / 버전) 11.

Nếu phản hồi (response / 응답) cũ từ A về trễ và máy khách (client / 클라이언트) ghi đè cục bộ (local / 로컬) trạng thái (state / 상태) không kiểm tra phiên bản (version / 버전), dữ liệu mới có thể bị mất.

Một mẫu (pattern / 패턴):

```kotlin
if (incoming.version >= current.version) {
    dao.upsert(incoming)
}
```

Nhưng phiên bản (version / 버전) chính sách (policy / 정책) phải do backend đặc tả hợp đồng (contract / 계약) định nghĩa. Timestamp máy khách (client / 클라이언트) không phải lúc nào đáng tin vì clock skew.

---

## 12. Optimistic tính đồng thời (concurrency / 동시성) điều khiển (control / 제어) và If-Match

Máy chủ (server / 서버) có thể yêu cầu máy khách (client / 클라이언트) gửi phiên bản (version / 버전) đã đọc:

```http
PUT /document/42
If-Match: "v10"
```

Nếu máy chủ (server / 서버) hiện là v11:

```http
412 Precondition Failed
```

Máy khách (client / 클라이언트) lúc đó biết rõ đã có xung đột (conflict / 충돌) thay vì silently overwrite.

Điều này đặc biệt hữu ích với document edit, profile hoặc tài nguyên (resource / 자원) có concurrent writer.

---

## 13. Last-write-wins đơn giản nhưng cần hiểu điều gì đang bị mất

LWW thường dựa trên timestamp hoặc máy chủ (server / 서버) revision.

Ưu điểm: dễ implement.

Nhược điểm: một writer có thể xóa thay đổi của writer khác mà không biết.

Ví dụ hai thiết bị (device / 장치) edit profile:

```text
Device A: đổi avatar
Device B: đổi display name
```

Nếu toàn tài nguyên (resource / 자원) dùng LWW, cập nhật (update / 업데이트) B có thể ghi lại avatar cũ.

Tách field-level patch hoặc merge ngữ nghĩa (semantics / 의미론) có thể tránh lost cập nhật (update / 업데이트).

---

## 14. giải quyết xung đột (conflict resolution / 충돌 해결) nên dựa theo lĩnh vực (domain / 도메인) ngữ nghĩa (semantics / 의미론)

Không có một thuật toán xung đột (conflict / 충돌) chung cho mọi tính năng (feature / 기능).

Ví dụ:

```text
bookmark -> desired boolean, LWW thường đủ
shopping cart quantity -> server business rule + merge
notes text -> manual conflict hoặc CRDT/OT nếu collaborative
profile fields -> field-level merge
bank balance -> không client-merge
```

Cấp cao (senior / 시니어) thiết kế (design / 설계) là chọn xung đột (conflict / 충돌) mô hình (model / 모델) theo lĩnh vực (domain / 도메인), không theo thư viện đang dùng.

---

## 15. Tombstone cần thiết khi delete cũng phải sync

Nếu delete cục bộ (local / 로컬) row ngay lập tức:

```sql
DELETE FROM article WHERE id = 42
```

worker sau đó không còn biết thực thể (entity / 엔터티) nào cần delete remote.

Tombstone giữ dấu vết:

```text
id = 42
deleted = true
syncState = PENDING_DELETE
```

Sau remote confirmation mới purge vật lý khi chính sách (policy / 정책) cho phép.

Tombstone cũng giúp máy chủ (server / 서버)/máy khách (client / 클라이언트) phân biệt:

```text
entity chưa từng tồn tại
vs
entity đã bị xóa
```

---

## 16. Sync cursor khác page cursor

Page cursor trả lời:

```text
cho tôi trang tiếp theo của query hiện tại
```

Sync cursor trả lời:

```text
cho tôi tất cả thay đổi kể từ checkpoint X
```

Đừng mặc định một pagination API có thể dùng làm sync API.

Sync API tốt thường có server-defined đơn vị từ (token / 토큰):

```text
GET /sync?cursor=abc123
-> changes + nextCursor
```

Máy khách (client / 클라이언트) chỉ advance cursor sau khi apply cục bộ (local / 로컬) giao dịch (transaction / 트랜잭션) thành công.

Nếu advance trước rồi crash trước cục bộ (local / 로컬) lần ghi nhận (commit / 커밋), máy khách (client / 클라이언트) có thể bỏ mất thay đổi (change / 변경) vĩnh viễn.

---

## 17. Checkpoint phải lần ghi nhận (commit / 커밋) cùng dữ liệu (data / 데이터)

Bất biến (invariant / 불변식):

```text
local applied changes và sync cursor phải tiến cùng transaction
```

Pseudo-flow:

```kotlin
db.withTransaction {
    applyRemoteChanges(batch.items)
    syncStateDao.updateCursor(batch.nextCursor)
}
```

Nếu app chết trước giao dịch (transaction / 트랜잭션) lần ghi nhận (commit / 커밋), cả dữ liệu (data / 데이터) và cursor quay lui (rollback / 롤백). Lần sau fetch lại batch cũ — an toàn nếu apply idempotent.

---

## 18. Pull-before-push hay push-before-pull?

Không có câu trả lời chung.

### Push-before-pull

Ưu điểm: người dùng (user / 사용자) intent cục bộ (local / 로컬) được gửi nhanh.

Rủi ro: máy chủ (server / 서버) đã có phiên bản (version / 버전) mới; mutation có thể xung đột (conflict / 충돌).

### Pull-before-push

Ưu điểm: máy khách (client / 클라이언트) cập nhật (update / 업데이트) cục bộ (local / 로컬) cơ sở (base / 기반) trước.

Rủi ro: người dùng (user / 사용자) mutation phải đợi; merge chính sách (policy / 정책) vẫn cần.

Nhiều sync engine dùng cycle:

```text
1. pull remote changes
2. merge/apply
3. push local mutations
4. pull acknowledgement/final state nếu cần
```

Nhưng lĩnh vực (domain / 도메인) và Đặc tả API (API contract / API 계약) quyết định thứ tự (ordering / 순서) thật.

---

## 19. WorkManager là scheduler, không phải sync kiến trúc (architecture / 아키텍처)

WorkManager giúp đảm bảo durable background thực thi (execution / 실행) theo ràng buộc (constraint / 제약조건). Nó không tự quyết định:

- nguồn chuẩn (source of truth / 정본),
- idempotency,
- thứ tự (ordering / 순서),
- xung đột (conflict / 충돌) chính sách (policy / 정책),
- account quyền sở hữu (ownership / 소유권),
- cursor atomicity.

Worker nên mỏng:

```kotlin
class SyncWorker(
    private val syncEngine: SyncEngine
) : CoroutineWorker(...) {

    override suspend fun doWork(): Result =
        when (syncEngine.runOneCycle()) {
            SyncOutcome.Success -> Result.success()
            SyncOutcome.RetryableFailure -> Result.retry()
            SyncOutcome.PermanentFailure -> Result.failure()
        }
}
```

Lô-gic (logic / 논리) tính đúng đắn (correctness / 정확성) nằm trong SyncEngine/dữ liệu (data / 데이터) tầng (layer / 계층), không chôn trong Android scheduling callback.

---

## 20. Unique công việc (work / 작업) giúp tránh duplicate scheduler, không thay idempotency

Có thể enqueue:

```kotlin
WorkManager.getInstance(context).enqueueUniqueWork(
    "account:$accountId:sync",
    ExistingWorkPolicy.KEEP,
    request
)
```

Điều này giảm duplicate workers.

Nhưng vẫn phải assume worker có thể chạy lại sau tiến trình (process / 프로세스) restart, thử lại (retry / 재시도) hoặc khung phần mềm (framework / 프레임워크) hành vi (behavior / 동작). thao tác (operation / 연산) bên trong vẫn cần idempotent.

---

## 21. Logout là một consistency sự kiện (event / 이벤트) lớn

Khi logout, phải quyết định:

```text
pending mutation account cũ xử lý thế nào?
local cached data có xóa không?
sync cursor có namespace theo account không?
worker đang chạy có cancel không?
request in-flight dùng token cũ hay mới?
```

Một lỗi nguy hiểm là worker account A thử lại (retry / 재시도) sau khi người dùng (user / 사용자) login account B và lấy đơn vị từ (token / 토큰) B từ singleton session provider.

Mọi durable dữ liệu (data / 데이터) liên quan session nên không gian tên (namespace / 네임스페이스) theo account định danh (identity / 식별자) hoặc bị clear rõ ràng.

---

## 22. Account switch cần generation/session epoch

Một kỹ thuật là dùng `sessionEpoch`:

```text
login A -> epoch 41
logout
login B -> epoch 42
```

Worker/yêu cầu (request / 요청) capture epoch lúc bắt đầu. Trước khi lần ghi nhận (commit / 커밋) kết quả (result / 결과):

```kotlin
if (capturedEpoch != sessionManager.currentEpoch) {
    return
}
```

Điều này giúp chặn phản hồi (response / 응답) từ session cũ ghi vào trạng thái (state / 상태) session mới.

---

## 23. Stale mạng (network / 네트워크) phản hồi (response / 응답) cần guard

Ví dụ người dùng (user / 사용자) tìm kiếm (search / 검색):

```text
T0 query = "ko"
T1 request A start
T2 query = "kotlin"
T3 request B start
T4 B complete
T5 A complete
```

Nếu A ghi kết quả (result / 결과) cuối cùng, UI quay về dữ liệu (data / 데이터) của truy vấn (query / 쿼리) cũ.

Có nhiều cách bảo vệ:

- `flatMapLatest`,
- cancel yêu cầu (request / 요청) cũ,
- generation/yêu cầu (request / 요청) đơn vị từ (token / 토큰),
- compare truy vấn (query / 쿼리) trước lần ghi nhận (commit / 커밋).

Luồng (flow / 흐름) operator chỉ là công cụ. bất biến (invariant / 불변식) thật là:

```text
result của request cũ không được thay thế state của request mới hơn
```

---

## 24. cục bộ (local / 로컬) optimistic trạng thái (state / 상태) cần phân biệt confirmed và desired

Một mô hình (model / 모델) hữu ích:

```kotlin
data class SyncableField<T>(
    val confirmed: T,
    val desired: T,
    val pending: Boolean
)
```

Nếu máy chủ (server / 서버) reject desired trạng thái (state / 상태), UI có đủ thông tin để:

- quay lui (rollback / 롤백),
- giữ desired và báo lỗi,
- yêu cầu người dùng (user / 사용자) resolve.

Chỉ lưu một boolean không chứa đủ ngữ nghĩa (semantics / 의미론).

---

## 25. Partial thất bại (failure / 실패) khi batch sync

Batch 100 mutation có thể có:

```text
90 success
5 retryable
3 validation failure
2 unauthorized
```

Không nên chỉ trả `Boolean success`.

Sync engine cần per-item kết quả (outcome / 결과) hoặc máy chủ (server / 서버) đặc tả hợp đồng (contract / 계약) atomic batch.

Nếu batch là atomic, hoặc tất cả lần ghi nhận (commit / 커밋) hoặc không. Nếu non-atomic, máy khách (client / 클라이언트) phải persist kết quả từng mutation.

---

## 26. Backpressure trong sync hàng đợi (queue / 큐)

Nếu app tạo mutation nhanh hơn khả năng upload, outbox tăng vô hạn.

Cần monitor:

```text
queue depth
oldest pending age
attempt count distribution
success latency
permanent failure count
```

Sync tính đúng đắn (correctness / 정확성) không chỉ là đường đi mã (code path / 코드 경로); khả năng quan sát (observability / 관측 가능성) cho biết hệ thống đang có sync debt hay không.

---

## 27. Poison mutation

Một mutation malformed có thể thất bại (fail / 실패) mãi và chặn hàng đợi (queue / 큐) nếu worker xử lý strictly ordered.

Cần chính sách (policy / 정책):

```text
retry N lần
-> classify permanent failure
-> dead-letter/quarantine
-> tiếp tục queue nếu ordering cho phép
```

Đừng để một row hỏng chặn sync toàn account mãi mãi.

---

## 28. Sync máy trạng thái (state machine / 상태 머신) nên tường minh (explicit / 명시적)

Ví dụ:

```kotlin
sealed interface MutationState {
    data object Pending : MutationState
    data class InFlight(val attempt: Int) : MutationState
    data class RetryAt(val instant: Instant, val attempt: Int) : MutationState
    data class FailedPermanent(val reason: String) : MutationState
}
```

Nếu app crash khi `InFlight`, startup khôi phục (recovery / 복구) có thể đưa row về Pending vì mạng (network / 네트워크) kết quả (outcome / 결과) chưa chắc biết. Idempotency key bảo vệ thử lại (retry / 재시도).

---

## 29. kiểm thử (test / 테스트) sync bằng timeline và thất bại (failure / 실패) injection

Một suite tốt không chỉ kiểm thử (test / 테스트) happy đường dẫn (path / 경로).

Kiểm thử (test / 테스트) các điểm:

```text
crash sau local transaction
crash sau HTTP send nhưng trước response
response duplicate
response out-of-order
server 429
server 500
server 401
account switch giữa request
cursor batch apply fail
DB full
clock lệch
network flapping
```

Mỗi kiểm thử (test / 테스트) phải assert bất biến (invariant / 불변식), không chỉ assert phương thức (method / 메서드) được gọi.

---

## 30. Property-based kiểm thử (test / 테스트) có giá trị với sync engine

Có thể sinh ngẫu nhiên chuỗi sự kiện (event / 이벤트):

```text
local mutation
remote mutation
network on/off
process restart
retry
account switch
```

Bất biến (invariant / 불변식) cuối:

```text
không mất durable user intent
không cross-account write
không duplicate business effect
cursor không vượt quá data đã apply
```

Property-based testing hữu ích vì race/thứ tự (order / 순서) combination quá lớn để viết tay hết.

---

## 31. khả năng quan sát (observability / 관측 가능성) lược đồ (schema / 스키마) cho sync

Log/dấu vết (trace / 추적) nên có correlation fields:

```text
accountHash
mutationId
entityType
entityIdHash
attempt
queueAgeMs
httpStatus
outcome
syncCycleId
```

Không log đơn vị từ (token / 토큰), raw PII hoặc payload nhạy cảm.

Khi sự cố (incident / 인시던트) xảy ra, câu hỏi cần trả lời là:

```text
mutation nào bị stuck?
bao lâu?
retry bao nhiêu lần?
server response gì?
client version nào?
```

---

## 32. quyết định (decision / 결정) khung phần mềm (framework / 프레임워크)

Trước khi bản dựng (build / 빌드) sync, trả lời:

| Câu hỏi | Ý nghĩa |
|---|---|
| cục bộ (local / 로컬) có được mutate khi offline không? | optimistic/local-first |
| máy chủ (server / 서버) có authority cuối không? | kiểm tra hợp lệ (validation / 검증)/xung đột (conflict / 충돌) |
| thao tác (operation / 연산) idempotent không? | thử lại (retry / 재시도) an toàn (safety / 안전) |
| Có concurrent writer không? | phiên bản (version / 버전)/xung đột (conflict / 충돌) |
| thứ tự (ordering / 순서) có quan trọng không? | hàng đợi (queue / 큐) ngữ nghĩa (semantics / 의미론) |
| Delete có cần sync không? | tombstone |
| Mutation có account phạm vi (scope / 범위) không? | session isolation |
| kết quả (outcome / 결과) có thể ambiguous không? | idempotency/truy vấn (query / 쿼리) status |
| hàng đợi (queue / 큐) có thể compact không? | debt điều khiển (control / 제어) |
| Cursor lần ghi nhận (commit / 커밋) cùng dữ liệu (data / 데이터) chưa? | lost-update protection |

---

## 33. Kết luận

Offline-first đúng nghĩa là một distributed-system bài toán (problem / 문제) thu nhỏ trên mobile.

Mô hình tư duy (mental model / 사고 모델) nên giữ:

```text
local intent
-> durable mutation
-> idempotent transport
-> conflict-aware remote authority
-> atomic local apply
-> checkpoint
-> retry/recovery
-> observability
```

Room và WorkManager chỉ giải quyết một phần cơ chế. tính đúng đắn (correctness / 정확성) đến từ consistency mô hình (model / 모델), bất biến (invariant / 불변식), idempotency, versioning, thất bại (failure / 실패) classification và account isolation.

> **Bàn giao:** Sau **33. Kết luận**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 architecture invariants boundary reasoning](./01_architecture_invariants_boundary_reasoning.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
