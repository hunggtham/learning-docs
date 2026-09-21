# Depth Lab 02 — Offline-First, Consistency, Race Condition và Sync Correctness

Offline-first không có nghĩa đơn giản là “lưu dữ liệu vào Room để app vẫn mở được khi mất mạng”. Một hệ thống offline-first thật sự phải trả lời những câu khó hơn: local và remote có thể lệch nhau bao lâu, mutation nào được phép reorder, retry có tạo duplicate effect không, nhiều device cùng sửa thì merge thế nào, logout giữa lúc sync ra sao, và nếu app bị kill sau local commit nhưng trước remote commit thì user intent có còn tồn tại hay không.

Depth Lab này đi sâu vào **consistency model** và **failure semantics** của sync engine.

---

## 1. Trước tiên phải phân biệt ba khái niệm: source of truth, authority và replica

Trong nhiều app offline-first:

```text
Room = local source of truth cho UI
Server = business authority cuối cùng
Device local DB = một replica có thể tạm lệch server
```

Ba vai trò này không mâu thuẫn.

UI đọc Room để có trải nghiệm reactive và offline. Server vẫn có thể là nơi quyết định business rule cuối cùng. Room có thể chứa desired state chưa được server xác nhận.

Điều nguy hiểm là dùng từ “source of truth” mà không nói rõ phạm vi. Hãy luôn hỏi:

```text
truth cho UI hiện tại?
truth cho billing?
truth cho authorization?
truth cho conflict resolution?
```

Ví dụ permission server-side không bao giờ nên lấy Room làm authority cuối cùng chỉ vì UI đang observe Room.

---

## 2. Consistency model phải được chọn có chủ ý

Không phải mọi feature cần strong consistency.

Một bookmark có thể chấp nhận eventual consistency:

```text
user tap -> local update ngay -> sync server sau
```

Nhưng chuyển tiền không thể chỉ “sync khi có mạng” theo cùng mental model.

Hãy phân loại operation:

| Loại dữ liệu | Consistency thường phù hợp |
|---|---|
| UI preference | local-first |
| bookmark/favorite | eventual consistency |
| social like | eventual + conflict policy |
| draft document | local durable + merge/versioning |
| inventory reservation | server-authoritative |
| payment | server-authoritative + idempotency |
| authorization | server-authoritative |

Offline-first là chiến lược, không phải dogma áp cho mọi mutation.

---

## 3. Outbox pattern bảo vệ user intent khỏi process death

Nếu code làm:

```kotlin
localDao.setBookmarked(id, true)
api.setBookmarked(id, true)
```

và process chết sau dòng đầu, local state đã đổi nhưng không còn thứ gì nhắc hệ thống phải sync server.

Outbox giải quyết bằng cách transactionally lưu cả state và pending intent:

```text
transaction
├── update article desired state
└── insert mutation into outbox
```

Sau transaction, invariant là:

```text
nếu local state cần remote sync
=> luôn tồn tại durable mutation mô tả intent đó
```

Worker chỉ là executor đọc outbox. Worker có chết thì intent vẫn còn.

---

## 4. Outbox row phải mô tả intent, không chỉ request body

Một outbox tốt thường cần metadata như:

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

`accountId` đặc biệt quan trọng. Nếu user logout rồi login account khác, worker không được vô tình gửi mutation của account cũ với token mới.

Mutation ownership phải được namespace theo session/account.

---

## 5. Retry policy phải bắt đầu từ idempotency

Retry an toàn nếu operation có thể thực hiện nhiều lần mà business outcome không đổi.

Ví dụ tốt:

```http
PUT /articles/42/bookmark
{
  "bookmarked": true
}
```

Gửi `true` năm lần vẫn có cùng outcome.

Nguy hiểm hơn:

```http
POST /articles/42/toggle-bookmark
```

Nếu response lần đầu bị mất rồi client retry, bookmark có thể bị toggle hai lần và quay về trạng thái cũ.

Design API nên ưu tiên **set desired state** thay vì “toggle” khi operation cần retry.

---

## 6. Idempotency key bảo vệ operation có side effect

Với operation không tự nhiên idempotent, dùng mutation id:

```http
POST /payments
Idempotency-Key: 55c0f6d2-...
```

Server lưu mapping:

```text
idempotencyKey -> result
```

Nếu client retry cùng key, server trả result cũ.

Điểm quan trọng là mutation id phải được tạo **trước lần gửi đầu tiên** và persist cùng durable intent. Tạo UUID mới cho mỗi retry phá toàn bộ ý nghĩa idempotency.

---

## 7. Timeout không đồng nghĩa operation thất bại

Timeline:

```text
T0 client gửi request
T1 server nhận
T2 server commit DB
T3 response trên đường về
T4 network đứt
T5 client timeout
```

Client chỉ biết “không nhận response”, không biết server có commit hay chưa.

Đây là ambiguous outcome.

Vì vậy:

```text
timeout -> UNKNOWN
```

không phải luôn:

```text
timeout -> FAILED
```

Với operation quan trọng, client cần idempotency hoặc endpoint query trạng thái operation.

---

## 8. Exponential backoff không đủ nếu không có jitter

Nếu hàng trăm nghìn device cùng retry sau outage với lịch:

```text
1s, 2s, 4s, 8s, 16s
```

chúng có thể cùng quay lại server đúng những thời điểm giống nhau, tạo **thundering herd**.

Thêm jitter:

```text
baseDelay = 8s
actualDelay = random(4s..12s)
```

Mục tiêu là phân tán retry load.

Retry policy nên dựa trên error class:

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

## 9. Ordering chỉ cần được bảo vệ khi business yêu cầu

Giả sử user thao tác:

```text
T1 bookmark = true
T2 bookmark = false
T3 bookmark = true
```

Nếu ba mutation được gửi song song, response có thể về thứ tự khác.

Nếu API dùng desired state và server last-write-wins theo version, ta có thể collapse queue.

Thay vì gửi 3 mutation:

```text
true
false
true
```

có thể chỉ cần giữ desired state cuối:

```text
true
```

Nhưng chỉ được compact nếu semantics cho phép.

Một sequence “create comment -> edit comment -> delete comment” không thể compact tùy tiện nếu remote identity chưa tồn tại.

---

## 10. Queue compaction giúp giảm sync debt

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

Điều này giảm request count và thời gian recovery sau offline dài.

Tuy nhiên mutation compaction phải bảo vệ audit/business semantics. Payment event, analytics cần ordering hoặc append-only history có thể không được compact.

---

## 11. Version number giúp chống stale response overwrite

Giả sử local entity có:

```text
version = 10
```

Client gửi update A dựa trên version 10. Trong khi request đang chạy, update B từ device khác đưa server lên version 11.

Nếu response cũ từ A về trễ và client ghi đè local state không kiểm tra version, dữ liệu mới có thể bị mất.

Một pattern:

```kotlin
if (incoming.version >= current.version) {
    dao.upsert(incoming)
}
```

Nhưng version policy phải do backend contract định nghĩa. Timestamp client không phải lúc nào đáng tin vì clock skew.

---

## 12. Optimistic concurrency control và If-Match

Server có thể yêu cầu client gửi version đã đọc:

```http
PUT /document/42
If-Match: "v10"
```

Nếu server hiện là v11:

```http
412 Precondition Failed
```

Client lúc đó biết rõ đã có conflict thay vì silently overwrite.

Điều này đặc biệt hữu ích với document edit, profile hoặc resource có concurrent writer.

---

## 13. Last-write-wins đơn giản nhưng cần hiểu điều gì đang bị mất

LWW thường dựa trên timestamp hoặc server revision.

Ưu điểm: dễ implement.

Nhược điểm: một writer có thể xóa thay đổi của writer khác mà không biết.

Ví dụ hai device edit profile:

```text
Device A: đổi avatar
Device B: đổi display name
```

Nếu toàn resource dùng LWW, update B có thể ghi lại avatar cũ.

Tách field-level patch hoặc merge semantics có thể tránh lost update.

---

## 14. Conflict resolution nên dựa theo domain semantics

Không có một thuật toán conflict chung cho mọi feature.

Ví dụ:

```text
bookmark -> desired boolean, LWW thường đủ
shopping cart quantity -> server business rule + merge
notes text -> manual conflict hoặc CRDT/OT nếu collaborative
profile fields -> field-level merge
bank balance -> không client-merge
```

Senior design là chọn conflict model theo domain, không theo thư viện đang dùng.

---

## 15. Tombstone cần thiết khi delete cũng phải sync

Nếu delete local row ngay lập tức:

```sql
DELETE FROM article WHERE id = 42
```

worker sau đó không còn biết entity nào cần delete remote.

Tombstone giữ dấu vết:

```text
id = 42
deleted = true
syncState = PENDING_DELETE
```

Sau remote confirmation mới purge vật lý khi policy cho phép.

Tombstone cũng giúp server/client phân biệt:

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

Sync API tốt thường có server-defined token:

```text
GET /sync?cursor=abc123
-> changes + nextCursor
```

Client chỉ advance cursor sau khi apply local transaction thành công.

Nếu advance trước rồi crash trước local commit, client có thể bỏ mất change vĩnh viễn.

---

## 17. Checkpoint phải commit cùng data

Invariant:

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

Nếu app chết trước transaction commit, cả data và cursor rollback. Lần sau fetch lại batch cũ — an toàn nếu apply idempotent.

---

## 18. Pull-before-push hay push-before-pull?

Không có câu trả lời chung.

### Push-before-pull

Ưu điểm: user intent local được gửi nhanh.

Rủi ro: server đã có version mới; mutation có thể conflict.

### Pull-before-push

Ưu điểm: client update local base trước.

Rủi ro: user mutation phải đợi; merge policy vẫn cần.

Nhiều sync engine dùng cycle:

```text
1. pull remote changes
2. merge/apply
3. push local mutations
4. pull acknowledgement/final state nếu cần
```

Nhưng domain và API contract quyết định ordering thật.

---

## 19. WorkManager là scheduler, không phải sync architecture

WorkManager giúp đảm bảo durable background execution theo constraint. Nó không tự quyết định:

- source of truth,
- idempotency,
- ordering,
- conflict policy,
- account ownership,
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

Logic correctness nằm trong SyncEngine/data layer, không chôn trong Android scheduling callback.

---

## 20. Unique work giúp tránh duplicate scheduler, không thay idempotency

Có thể enqueue:

```kotlin
WorkManager.getInstance(context).enqueueUniqueWork(
    "account:$accountId:sync",
    ExistingWorkPolicy.KEEP,
    request
)
```

Điều này giảm duplicate workers.

Nhưng vẫn phải assume worker có thể chạy lại sau process restart, retry hoặc framework behavior. Operation bên trong vẫn cần idempotent.

---

## 21. Logout là một consistency event lớn

Khi logout, phải quyết định:

```text
pending mutation account cũ xử lý thế nào?
local cached data có xóa không?
sync cursor có namespace theo account không?
worker đang chạy có cancel không?
request in-flight dùng token cũ hay mới?
```

Một lỗi nguy hiểm là worker account A retry sau khi user login account B và lấy token B từ singleton session provider.

Mọi durable data liên quan session nên namespace theo account identity hoặc bị clear rõ ràng.

---

## 22. Account switch cần generation/session epoch

Một kỹ thuật là dùng `sessionEpoch`:

```text
login A -> epoch 41
logout
login B -> epoch 42
```

Worker/request capture epoch lúc bắt đầu. Trước khi commit result:

```kotlin
if (capturedEpoch != sessionManager.currentEpoch) {
    return
}
```

Điều này giúp chặn response từ session cũ ghi vào state session mới.

---

## 23. Stale network response cần guard

Ví dụ user search:

```text
T0 query = "ko"
T1 request A start
T2 query = "kotlin"
T3 request B start
T4 B complete
T5 A complete
```

Nếu A ghi result cuối cùng, UI quay về data của query cũ.

Có nhiều cách bảo vệ:

- `flatMapLatest`,
- cancel request cũ,
- generation/request token,
- compare query trước commit.

Flow operator chỉ là công cụ. Invariant thật là:

```text
result của request cũ không được thay thế state của request mới hơn
```

---

## 24. Local optimistic state cần phân biệt confirmed và desired

Một model hữu ích:

```kotlin
data class SyncableField<T>(
    val confirmed: T,
    val desired: T,
    val pending: Boolean
)
```

Nếu server reject desired state, UI có đủ thông tin để:

- rollback,
- giữ desired và báo lỗi,
- yêu cầu user resolve.

Chỉ lưu một boolean không chứa đủ semantics.

---

## 25. Partial failure khi batch sync

Batch 100 mutation có thể có:

```text
90 success
5 retryable
3 validation failure
2 unauthorized
```

Không nên chỉ trả `Boolean success`.

Sync engine cần per-item outcome hoặc server contract atomic batch.

Nếu batch là atomic, hoặc tất cả commit hoặc không. Nếu non-atomic, client phải persist kết quả từng mutation.

---

## 26. Backpressure trong sync queue

Nếu app tạo mutation nhanh hơn khả năng upload, outbox tăng vô hạn.

Cần monitor:

```text
queue depth
oldest pending age
attempt count distribution
success latency
permanent failure count
```

Sync correctness không chỉ là code path; observability cho biết hệ thống đang có sync debt hay không.

---

## 27. Poison mutation

Một mutation malformed có thể fail mãi và chặn queue nếu worker xử lý strictly ordered.

Cần policy:

```text
retry N lần
-> classify permanent failure
-> dead-letter/quarantine
-> tiếp tục queue nếu ordering cho phép
```

Đừng để một row hỏng chặn sync toàn account mãi mãi.

---

## 28. Sync state machine nên explicit

Ví dụ:

```kotlin
sealed interface MutationState {
    data object Pending : MutationState
    data class InFlight(val attempt: Int) : MutationState
    data class RetryAt(val instant: Instant, val attempt: Int) : MutationState
    data class FailedPermanent(val reason: String) : MutationState
}
```

Nếu app crash khi `InFlight`, startup recovery có thể đưa row về Pending vì network outcome chưa chắc biết. Idempotency key bảo vệ retry.

---

## 29. Test sync bằng timeline và failure injection

Một suite tốt không chỉ test happy path.

Test các điểm:

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

Mỗi test phải assert invariant, không chỉ assert method được gọi.

---

## 30. Property-based test có giá trị với sync engine

Có thể sinh ngẫu nhiên chuỗi event:

```text
local mutation
remote mutation
network on/off
process restart
retry
account switch
```

Invariant cuối:

```text
không mất durable user intent
không cross-account write
không duplicate business effect
cursor không vượt quá data đã apply
```

Property-based testing hữu ích vì race/order combination quá lớn để viết tay hết.

---

## 31. Observability schema cho sync

Log/trace nên có correlation fields:

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

Không log token, raw PII hoặc payload nhạy cảm.

Khi incident xảy ra, câu hỏi cần trả lời là:

```text
mutation nào bị stuck?
bao lâu?
retry bao nhiêu lần?
server response gì?
client version nào?
```

---

## 32. Decision framework

Trước khi build sync, trả lời:

| Câu hỏi | Ý nghĩa |
|---|---|
| Local có được mutate khi offline không? | optimistic/local-first |
| Server có authority cuối không? | validation/conflict |
| Operation idempotent không? | retry safety |
| Có concurrent writer không? | version/conflict |
| Ordering có quan trọng không? | queue semantics |
| Delete có cần sync không? | tombstone |
| Mutation có account scope không? | session isolation |
| Outcome có thể ambiguous không? | idempotency/query status |
| Queue có thể compact không? | debt control |
| Cursor commit cùng data chưa? | lost-update protection |

---

## 33. Kết luận

Offline-first đúng nghĩa là một distributed-system problem thu nhỏ trên mobile.

Mental model nên giữ:

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

Room và WorkManager chỉ giải quyết một phần cơ chế. Correctness đến từ consistency model, invariant, idempotency, versioning, failure classification và account isolation.