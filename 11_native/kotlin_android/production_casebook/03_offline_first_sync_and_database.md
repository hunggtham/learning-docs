# Case 03 — Offline-First, Sync, Room Migration và Data Integrity

“Offline-first” không có nghĩa chỉ thêm Room vào app. Một hệ thống offline-first phải trả lời được: dữ liệu nào là source of truth, local write được coi là thành công ở thời điểm nào, khi reconnect thì sync theo thứ tự nào, conflict giải quyết ra sao, delete được biểu diễn thế nào, retry có tạo duplicate không, và app version mới/rollback có đọc được dữ liệu cũ không.

Chương này dùng một ứng dụng task/note có edit offline làm ví dụ vì nó chứa hầu hết vấn đề production: local database, remote API, queue mutation, sync, conflict, pagination, migration và recovery.

## 1. Local database làm source of truth

Nếu UI khi online đọc Retrofit nhưng khi offline đọc Room, bạn có hai đường dữ liệu với semantics khác nhau. Tốt hơn là UI luôn observe local source of truth; network chỉ cập nhật local source đó.

```text
Remote API -----> sync/refresh -----> Room
                                      |
                                      v
UI <- ViewModel <- Repository <- Flow from Room
```

Repository expose `Flow<List<Task>>` từ database. Khi refresh thành công, repository transactionally upsert remote snapshot. UI nhận Flow mới mà không cần biết request vừa xảy ra.

```kotlin
class TasksRepository(
    private val dao: TaskDao,
    private val api: TasksApi,
    private val syncQueue: SyncQueue
) {
    fun observeTasks(): Flow<List<Task>> =
        dao.observeTasks().map { rows -> rows.map(TaskEntity::toDomain) }

    suspend fun refresh() {
        val remote = api.fetchTasks()
        dao.applyRemoteSnapshot(remote.map(TaskDto::toEntity))
    }
}
```

## 2. Read offline và write offline là hai mức khác nhau

Một app chỉ cache response để đọc offline đơn giản hơn nhiều so với app cho phép mutation offline.

Read-offline cần cache policy, stale policy và refresh.

Write-offline cần thêm durable pending operation, idempotency, ordering, conflict handling và reconciliation. Nếu product không cần write offline, đừng tự thêm complexity này.

## 3. Optimistic write

Khi user sửa title offline, UX tốt thường cập nhật local database ngay rồi đánh dấu entity đang pending sync.

```kotlin
@Entity
data class TaskEntity(
    @PrimaryKey val id: String,
    val title: String,
    val completed: Boolean,
    val serverVersion: Long?,
    val syncState: SyncState,
    val updatedAt: Long,
    val deleted: Boolean = false
)
```

`syncState` có thể là `Synced`, `PendingCreate`, `PendingUpdate`, `PendingDelete`, `FailedPermanent`. Không nên dùng một Boolean `dirty` nếu operation semantics cần phân biệt create/update/delete.

## 4. Queue mutation phải durable

Nếu pending operation chỉ nằm trong memory và process bị kill, local state có thể không bao giờ lên server. Vì vậy write-offline thường cần queue persist trong database.

```kotlin
@Entity
data class PendingMutationEntity(
    @PrimaryKey val operationId: String,
    val entityId: String,
    val type: MutationType,
    val payloadJson: String,
    val createdAt: Long,
    val attemptCount: Int
)
```

Một transaction nên cập nhật entity local và enqueue mutation cùng lúc. Nếu app crash giữa hai bước mà không có transaction, state có thể nói “đã sửa” nhưng không còn record để sync.

## 5. Operation ID và idempotency

Network có thể timeout sau khi server đã xử lý mutation. Client không biết request thành công hay chưa. Nếu retry create mù, server có thể tạo duplicate.

Giải pháp protocol là operation có stable idempotency key.

```text
local operation UUID
      ↓
POST /tasks
Idempotency-Key: <uuid>
      ↓
server remembers result for key
      ↓
retry same key returns same logical result
```

Exactly-once effect hiếm khi đến từ transport; nó đến từ idempotent protocol và reconciliation.

## 6. WorkManager phù hợp cho durable deferred sync

Nếu sync phải tiếp tục sau process death và có thể chạy khi constraint network được đáp ứng, WorkManager là lựa chọn tự nhiên.

```kotlin
val request = OneTimeWorkRequestBuilder<SyncWorker>()
    .setConstraints(
        Constraints.Builder()
            .setRequiredNetworkType(NetworkType.CONNECTED)
            .build()
    )
    .build()
```

Nhưng WorkManager không phải real-time socket và không đảm bảo chạy đúng một thời điểm tuyệt đối. Nếu chỉ cần refresh khi screen active, coroutine trong lifecycle/ViewModel đơn giản hơn.

## 7. Sync worker phải retry có kỷ luật

Không phải failure nào cũng retry.

- offline, timeout, 503: có thể retry với backoff;
- 401: session layer phải recover hoặc yêu cầu login;
- 400 validation: thường permanent cho mutation đó;
- 409 conflict: cần conflict strategy;
- 404 khi update entity đã bị xóa server-side: phải reconcile semantics.

Nếu mọi error đều `Result.retry()`, queue có thể lặp vô hạn và đốt pin.

## 8. Conflict là business problem trước khi là technical problem

Hai thiết bị có thể edit cùng record. Không có một thuật toán conflict đúng cho mọi domain.

Các strategy phổ biến:

**Last-write-wins** đơn giản nhưng có thể mất edit. Nó phù hợp khi field ít quan trọng hoặc server timestamp authoritative.

**Version check / optimistic concurrency** gửi `serverVersion`; server reject nếu version stale. Client sau đó fetch latest và yêu cầu merge.

**Field-level merge** có thể merge các field độc lập nhưng phức tạp với invariant.

**CRDT** hữu ích cho một số collaborative data nhưng complexity cao và không nên dùng chỉ vì “nghe advanced”.

Product phải định nghĩa conflict semantics. Kỹ thuật chỉ implement semantics đó.

## 9. Version-based optimistic concurrency

Ví dụ server trả version 7. Client edit dựa trên version 7:

```json
{
  "id": "task-1",
  "title": "New title",
  "baseVersion": 7
}
```

Nếu server đã lên version 8, response 409 conflict có thể kèm latest record. Client quyết định auto-merge hay hiển thị conflict UI.

## 10. Delete cần tombstone khi sync offline

Nếu xóa row local ngay, sync engine có thể quên rằng server cũng cần được xóa. Vì vậy thường dùng **tombstone**: row vẫn tồn tại với `deleted=true` cho tới khi delete sync thành công.

Sau khi server acknowledge, cleanup job mới hard-delete local row.

Tombstone cũng giúp remote snapshot không vô tình “hồi sinh” entity đã xóa local nhưng chưa sync.

## 11. Pull sync và cursor

Với data lớn, không nên mỗi lần sync tải toàn bộ dataset. Server có thể cung cấp cursor/since token:

```text
GET /tasks/changes?cursor=abc123
→ changes + nextCursor
```

Client transactionally apply change set rồi persist `nextCursor`. Cursor chỉ được advance sau khi apply thành công; nếu crash giữa chừng, retry cùng cursor phải an toàn.

## 12. Transaction boundary quan trọng hơn số lượng DAO method

Ví dụ apply remote page:

```kotlin
@Transaction
suspend fun applyPage(
    items: List<TaskEntity>,
    deletedIds: List<String>,
    nextCursor: String
) {
    upsert(items)
    markRemoteDeleted(deletedIds)
    updateSyncCursor(nextCursor)
}
```

Nếu cursor update trước data rồi app crash, lần sau server nghĩ client đã consume changes dù local chưa có chúng. Đây là data integrity bug.

## 13. Pagination và Paging 3

Khi dataset lớn, Paging giúp load theo page và tích hợp Compose. Với network + Room, `RemoteMediator` có thể điều phối remote page vào local database trong khi UI vẫn đọc PagingSource từ Room.

Mental model vẫn giống source-of-truth: network không đưa page thẳng cho UI; nó cập nhật DB, DB invalidate PagingSource và UI nhận data mới.

Remote key/cursor cũng là persistent state và cần transaction cùng page data nếu consistency yêu cầu.

## 14. Staleness và refresh policy

Offline-first không nghĩa luôn tin cache mãi mãi. Repository cần policy: data bao lâu thì stale, screen open có auto-refresh không, pull-to-refresh có force network không, failure khi refresh có giữ cache không.

Một model đơn giản:

```kotlin
data class Freshness(
    val lastSuccessfulSyncAt: Instant?,
    val isRefreshInProgress: Boolean,
    val lastError: SyncError?
)
```

UI có thể hiển thị cached content cùng “Last updated …” thay vì spinner full-screen.

## 15. Clock và ordering

Không nên dựa quá nhiều vào device wall clock để resolve conflict vì clock có thể sai. Nếu server có monotonic version/revision sequence, ưu tiên version do server quản lý.

`updatedAt` vẫn hữu ích cho UX, nhưng semantics conflict cần rõ nguồn thời gian nào authoritative.

## 16. Room migration là executable history

Schema production thay đổi theo version. `fallbackToDestructiveMigration()` có thể chấp nhận cho cache tái tạo được trong một số app, nhưng nguy hiểm nếu database chứa user-created/offline data.

Migration phải mô tả đường đi từ schema cũ sang mới:

```kotlin
val MIGRATION_3_4 = object : Migration(3, 4) {
    override fun migrate(db: SupportSQLiteDatabase) {
        db.execSQL("ALTER TABLE tasks ADD COLUMN deleted INTEGER NOT NULL DEFAULT 0")
    }
}
```

Không chỉ compile; migration phải preserve invariant và data meaning.

## 17. Migration phức tạp: create-copy-drop-rename

SQLite không hỗ trợ mọi ALTER dễ dàng. Khi đổi primary key/type hoặc normalize table, pattern thường là:

```text
create new table
→ copy/transform data
→ verify
→ drop old table
→ rename new table
→ recreate index/foreign key
```

Cần đặc biệt chú ý default value, nullability, index unique và foreign key.

## 18. Test migration bằng database thật của schema cũ

Room hỗ trợ migration test. Hãy tạo DB schema N, insert dữ liệu đại diện edge cases, chạy migration tới current version rồi assert cả schema lẫn data.

Các case nên có: null cũ, unicode, record lớn, foreign key, duplicate data trước khi thêm unique constraint, tombstone/pending mutation và user ở trạng thái offline lâu ngày.

## 19. AutoMigration không loại bỏ trách nhiệm hiểu schema

AutoMigration hữu ích cho thay đổi Room suy luận được. Nhưng nếu rename/delete column, transform semantic hoặc đổi invariant, cần spec/manual migration. Đừng coi “build pass” là bằng chứng data production an toàn.

## 20. Schema export và review

Export Room schema vào repository giúp review diff schema và test migration. Schema file là artifact quan trọng, không phải noise build.

Một PR đổi entity nên được review cùng schema diff: column nào thêm, default gì, index thay đổi không, migration path từ version trước ở đâu.

## 21. Rollback compatibility

Nếu release version 10 migrate database irreversible và sau đó phải rollback APK về version 9, version 9 có thể không đọc schema mới. Đây là vấn đề release engineering.

Các chiến lược gồm forward-compatible migration, staged rollout nhỏ trước, backup/export cần thiết, hoặc tránh destructive semantic change trong một release có risk cao. Database design và rollout strategy không thể tách rời.

## 22. Serialization compatibility

Pending mutation payload lưu JSON trong DB phải chịu versioning. Nếu class Kotlin đổi field name/type, worker version mới có thể không parse pending payload do version cũ tạo.

Có thể lưu explicit payload version:

```json
{
  "schemaVersion": 2,
  "operationId": "...",
  "taskId": "...",
  "changes": { ... }
}
```

Deserializer migrate payload cũ hoặc queue table lưu structured columns thay vì raw serialized object tùy use case.

## 23. Unknown enum và server evolution

Server có thể thêm enum mới trước khi app update. Nếu client deserialize enum strict và crash, compatibility kém. Cân nhắc `Unknown(rawValue)` pattern hoặc custom serializer cho protocol có khả năng mở rộng.

Tương tự, network DTO nên tolerant với additive fields nhưng strict với invariant thật sự cần thiết.

## 24. Sync state không nên leak implementation lên UI quá sâu

UI có thể cần biết “pending”, “sync failed” để hiển thị icon/retry. Nhưng UI không cần biết WorkManager ID hoặc HTTP status raw.

Map infrastructure state thành domain/UI concept:

```kotlin
enum class SyncStatus {
    Synced,
    Pending,
    NeedsAttention
}
```

Detailed diagnostics có thể nằm trong logging/debug tooling.

## 25. Multi-account và database

Nếu app hỗ trợ nhiều account, hãy quyết định sớm giữa database riêng mỗi account và shared DB với `accountId`. Cả hai đều có trade-off về isolation, migration và switching.

Điều không được phép là query quên filter account dẫn tới data leakage. Nếu shared table, repository/DAO API nên làm account scope khó bị quên.

## 26. Sync observability

Production sync cần metric/event như queue length, age của oldest pending mutation, success rate, permanent failure count, conflict count, migration failure và average sync duration.

Nếu user báo “note của tôi không lên máy khác”, log chỉ có stack trace HTTP là chưa đủ. Bạn cần biết local operation ID, sync lifecycle và server correlation ID — nhưng không log nội dung nhạy cảm nếu không cần.

## 27. Failure drill

Một sync architecture nên được test bằng các scenario:

1. edit offline, kill process, reopen, reconnect;
2. cùng entity edit trên hai device;
3. request timeout sau khi server đã commit;
4. refresh snapshot đến trước pending local update;
5. delete offline rồi server cũng update entity;
6. access token expire giữa worker;
7. app upgrade khi queue cũ còn pending;
8. database full/disk error;
9. user logout trong khi queue còn work;
10. server schema thêm unknown enum.

Nếu behavior mong muốn chưa được định nghĩa, đó là product/architecture gap chứ không chỉ là test gap.

## 28. Senior notes

Offline-first là một **distributed system nhỏ**. Có replica local, server authoritative hoặc co-authoritative, unreliable network, retry, duplicate delivery, clock/version, conflict và eventual consistency. Khi nhìn theo góc này, nhiều quyết định trở nên rõ hơn.

Dùng database transaction để bảo vệ invariant local; dùng operation ID/idempotency để bảo vệ retry network; dùng version/cursor để bảo vệ reconciliation; dùng durable queue khi work phải sống qua process death; dùng explicit conflict policy thay vì “server wins vì dễ”.

Quan trọng nhất: không claim offline-first chỉ vì app mở được khi airplane mode. Một feature write-offline thực sự phải chứng minh được dữ liệu không mất, không duplicate và có đường recovery khi conflict hoặc migration xảy ra.
