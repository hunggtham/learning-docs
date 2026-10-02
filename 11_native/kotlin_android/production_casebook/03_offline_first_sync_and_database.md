# Trường hợp (case / 사례) 03 — Offline-First, Sync, Room di chuyển (migration / 마이그레이션) và dữ liệu (data / 데이터) Integrity

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Trường hợp (case / 사례) 03 — Offline-First, Sync, Room di chuyển (migration / 마이그레이션) và dữ liệu (data / 데이터) Integrity**. Route đi từ local source of truth → offline read/write semantics → mutation queue, retries và conflicts → migrations, pagination và deletes → reconnect/recovery integrity.

“Offline-first” không có nghĩa chỉ thêm Room vào app. Một hệ thống offline-first phải trả lời được: dữ liệu nào là nguồn chuẩn (source of truth / 정본), cục bộ (local / 로컬) ghi (write / 쓰기) được coi là thành công ở thời điểm nào, khi reconnect thì sync theo thứ tự nào, xung đột (conflict / 충돌) giải quyết ra sao, delete được biểu diễn thế nào, thử lại (retry / 재시도) có tạo duplicate không, và app phiên bản (version / 버전) mới/quay lui (rollback / 롤백) có đọc được dữ liệu cũ không.

Chương này dùng một ứng dụng tác vụ (task / 작업)/ghi chú (note / 노트) có edit offline làm ví dụ vì nó chứa hầu hết vấn đề môi trường vận hành (production / 운영 환경): cục bộ (local / 로컬) cơ sở dữ liệu (database / 데이터베이스), remote API, hàng đợi (queue / 큐) mutation, sync, xung đột (conflict / 충돌), pagination, di chuyển (migration / 마이그레이션) và khôi phục (recovery / 복구).

## 1. cục bộ (local / 로컬) cơ sở dữ liệu (database / 데이터베이스) làm nguồn chuẩn (source of truth / 정본)

Nếu UI khi online đọc Retrofit nhưng khi offline đọc Room, bạn có hai đường dữ liệu với ngữ nghĩa (semantics / 의미론) khác nhau. Tốt hơn là UI luôn observe cục bộ (local / 로컬) nguồn chuẩn (source of truth / 정본); mạng (network / 네트워크) chỉ cập nhật cục bộ (local / 로컬) nguồn (source / 소스) đó.

```text
Remote API -----> sync/refresh -----> Room
                                      |
                                      v
UI <- ViewModel <- Repository <- Flow from Room
```

Repository expose `Flow<List<Task>>` từ cơ sở dữ liệu (database / 데이터베이스). Khi refresh thành công, repository transactionally upsert remote snapshot. UI nhận luồng (flow / 흐름) mới mà không cần biết yêu cầu (request / 요청) vừa xảy ra.

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

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — Offline-First, Sync, Room di chuyển (migration / 마이그레이션) và dữ liệu (data / 데이터) Integrity**, **1. cục bộ (local / 로컬) cơ sở dữ liệu (database / 데이터베이스) làm nguồn chuẩn (source of truth / 정본)** nêu điều cần giải thích; **2. Read offline và ghi (write / 쓰기) offline là hai mức khác nhau** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **3. Optimistic ghi (write / 쓰기)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Read offline và ghi (write / 쓰기) offline là hai mức khác nhau

Một app chỉ bộ nhớ đệm (cache / 캐시) phản hồi (response / 응답) để đọc offline đơn giản hơn nhiều so với app cho phép mutation offline.

Read-offline cần bộ nhớ đệm (cache / 캐시) chính sách (policy / 정책), stale chính sách (policy / 정책) và refresh.

Write-offline cần thêm durable pending thao tác (operation / 연산), idempotency, thứ tự (ordering / 순서), xung đột (conflict / 충돌) handling và reconciliation. Nếu sản phẩm (product / 제품) không cần ghi (write / 쓰기) offline, đừng tự thêm độ phức tạp (complexity / 복잡도) này.

> **Chuyển mạch:** Offline read chỉ cần local source; optimistic write thêm pending intent, nên mutation queue tiếp theo phải durable để survive process death và retry.

## 3. Optimistic ghi (write / 쓰기)

Khi người dùng (user / 사용자) sửa title offline, UX tốt thường cập nhật cục bộ (local / 로컬) cơ sở dữ liệu (database / 데이터베이스) ngay rồi đánh dấu thực thể (entity / 엔터티) đang pending sync.

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

`syncState` có thể là `Synced`, `PendingCreate`, `PendingUpdate`, `PendingDelete`, `FailedPermanent`. Không nên dùng một Boolean `dirty` nếu thao tác (operation / 연산) ngữ nghĩa (semantics / 의미론) cần phân biệt create/cập nhật (update / 업데이트)/delete.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Offline-First, Sync, Room di chuyển (migration / 마이그레이션) và dữ liệu (data / 데이터) Integrity**, **4. hàng đợi (queue / 큐) mutation phải durable** tiếp nhận điểm tựa từ **3. Optimistic ghi (write / 쓰기)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. thao tác (operation / 연산) ID và idempotency** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. hàng đợi (queue / 큐) mutation phải durable

Nếu pending thao tác (operation / 연산) chỉ nằm trong bộ nhớ (memory / 메모리) và tiến trình (process / 프로세스) bị kill, cục bộ (local / 로컬) trạng thái (state / 상태) có thể không bao giờ lên máy chủ (server / 서버). Vì vậy write-offline thường cần hàng đợi (queue / 큐) persist trong cơ sở dữ liệu (database / 데이터베이스).

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

Một giao dịch (transaction / 트랜잭션) nên cập nhật thực thể (entity / 엔터티) cục bộ (local / 로컬) và enqueue mutation cùng lúc. Nếu app crash giữa hai bước mà không có giao dịch (transaction / 트랜잭션), trạng thái (state / 상태) có thể nói “đã sửa” nhưng không còn bản ghi (record / 레코드) để sync.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — Offline-First, Sync, Room di chuyển (migration / 마이그레이션) và dữ liệu (data / 데이터) Integrity**, **5. thao tác (operation / 연산) ID và idempotency** tiếp nhận điểm tựa từ **4. hàng đợi (queue / 큐) mutation phải durable** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. WorkManager phù hợp cho durable deferred sync** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. thao tác (operation / 연산) ID và idempotency

Mạng (network / 네트워크) có thể hết thời gian chờ (timeout / 타임아웃) sau khi máy chủ (server / 서버) đã xử lý mutation. máy khách (client / 클라이언트) không biết yêu cầu (request / 요청) thành công hay chưa. Nếu thử lại (retry / 재시도) create mù, máy chủ (server / 서버) có thể tạo duplicate.

Giải pháp giao thức (protocol / 프로토콜) là thao tác (operation / 연산) có stable idempotency key.

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

Exactly-once tác động (effect / 효과) hiếm khi đến từ vận chuyển (transport / 전송); nó đến từ idempotent giao thức (protocol / 프로토콜) và reconciliation.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Offline-First, Sync, Room di chuyển (migration / 마이그레이션) và dữ liệu (data / 데이터) Integrity**, **6. WorkManager phù hợp cho durable deferred sync** tiếp nhận điểm tựa từ **5. thao tác (operation / 연산) ID và idempotency** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Sync worker phải thử lại (retry / 재시도) có kỷ luật** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. WorkManager phù hợp cho durable deferred sync

Nếu sync phải tiếp tục sau tiến trình (process / 프로세스) death và có thể chạy khi ràng buộc (constraint / 제약조건) mạng (network / 네트워크) được đáp ứng, WorkManager là lựa chọn tự nhiên.

```kotlin
val request = OneTimeWorkRequestBuilder<SyncWorker>()
    .setConstraints(
        Constraints.Builder()
            .setRequiredNetworkType(NetworkType.CONNECTED)
            .build()
    )
    .build()
```

Nhưng WorkManager không phải real-time socket và không đảm bảo chạy đúng một thời điểm tuyệt đối. Nếu chỉ cần refresh khi screen active, coroutine trong vòng đời (lifecycle / 생명주기)/ViewModel đơn giản hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Offline-First, Sync, Room di chuyển (migration / 마이그레이션) và dữ liệu (data / 데이터) Integrity**, **7. Sync worker phải thử lại (retry / 재시도) có kỷ luật** tiếp nhận điểm tựa từ **6. WorkManager phù hợp cho durable deferred sync** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. xung đột (conflict / 충돌) là nghiệp vụ (business / 비즈니스) bài toán (problem / 문제) trước khi là technical bài toán (problem / 문제)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Sync worker phải thử lại (retry / 재시도) có kỷ luật

Không phải thất bại (failure / 실패) nào cũng thử lại (retry / 재시도).

- offline, hết thời gian chờ (timeout / 타임아웃), 503: có thể thử lại (retry / 재시도) với backoff;
- 401: session tầng (layer / 계층) phải recover hoặc yêu cầu login;
- 400 kiểm tra hợp lệ (validation / 검증): thường permanent cho mutation đó;
- 409 xung đột (conflict / 충돌): cần xung đột (conflict / 충돌) chiến lược (strategy / 전략);
- 404 khi cập nhật (update / 업데이트) thực thể (entity / 엔터티) đã bị xóa server-side: phải reconcile ngữ nghĩa (semantics / 의미론).

Nếu mọi lỗi (error / 오류) đều `Result.retry()`, hàng đợi (queue / 큐) có thể lặp vô hạn và đốt pin.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — Offline-First, Sync, Room di chuyển (migration / 마이그레이션) và dữ liệu (data / 데이터) Integrity**, **8. xung đột (conflict / 충돌) là nghiệp vụ (business / 비즈니스) bài toán (problem / 문제) trước khi là technical bài toán (problem / 문제)** tiếp nhận điểm tựa từ **7. Sync worker phải thử lại (retry / 재시도) có kỷ luật** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Version-based optimistic tính đồng thời (concurrency / 동시성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. xung đột (conflict / 충돌) là nghiệp vụ (business / 비즈니스) bài toán (problem / 문제) trước khi là technical bài toán (problem / 문제)

Hai thiết bị có thể edit cùng bản ghi (record / 레코드). Không có một thuật toán xung đột (conflict / 충돌) đúng cho mọi lĩnh vực (domain / 도메인).

Các chiến lược (strategy / 전략) phổ biến:

**Last-write-wins** đơn giản nhưng có thể mất edit. Nó phù hợp khi trường dữ liệu (field / 필드) ít quan trọng hoặc máy chủ (server / 서버) timestamp authoritative.

**phiên bản (version / 버전) check / optimistic tính đồng thời (concurrency / 동시성)** gửi `serverVersion`; máy chủ (server / 서버) reject nếu phiên bản (version / 버전) stale. máy khách (client / 클라이언트) sau đó fetch latest và yêu cầu merge.

**Field-level merge** có thể merge các trường dữ liệu (field / 필드) độc lập nhưng phức tạp với bất biến (invariant / 불변식).

**CRDT** hữu ích cho một số collaborative dữ liệu (data / 데이터) nhưng độ phức tạp (complexity / 복잡도) cao và không nên dùng chỉ vì “nghe advanced”.

Sản phẩm (product / 제품) phải định nghĩa xung đột (conflict / 충돌) ngữ nghĩa (semantics / 의미론). Kỹ thuật chỉ implement ngữ nghĩa (semantics / 의미론) đó.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Offline-First, Sync, Room di chuyển (migration / 마이그레이션) và dữ liệu (data / 데이터) Integrity**, **9. Version-based optimistic tính đồng thời (concurrency / 동시성)** tiếp nhận điểm tựa từ **8. xung đột (conflict / 충돌) là nghiệp vụ (business / 비즈니스) bài toán (problem / 문제) trước khi là technical bài toán (problem / 문제)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Delete cần tombstone khi sync offline** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Version-based optimistic tính đồng thời (concurrency / 동시성)

Ví dụ máy chủ (server / 서버) trả phiên bản (version / 버전) 7. máy khách (client / 클라이언트) edit dựa trên phiên bản (version / 버전) 7:

```json
{
  "id": "task-1",
  "title": "New title",
  "baseVersion": 7
}
```

Nếu máy chủ (server / 서버) đã lên phiên bản (version / 버전) 8, phản hồi (response / 응답) 409 xung đột (conflict / 충돌) có thể kèm latest bản ghi (record / 레코드). máy khách (client / 클라이언트) quyết định auto-merge hay hiển thị xung đột (conflict / 충돌) UI.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Offline-First, Sync, Room di chuyển (migration / 마이그레이션) và dữ liệu (data / 데이터) Integrity**, **10. Delete cần tombstone khi sync offline** tiếp nhận điểm tựa từ **9. Version-based optimistic tính đồng thời (concurrency / 동시성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Pull sync và cursor** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Delete cần tombstone khi sync offline

Nếu xóa row cục bộ (local / 로컬) ngay, sync engine có thể quên rằng máy chủ (server / 서버) cũng cần được xóa. Vì vậy thường dùng **tombstone**: row vẫn tồn tại với `deleted=true` cho tới khi delete sync thành công.

Sau khi máy chủ (server / 서버) acknowledge, cleanup job mới hard-delete cục bộ (local / 로컬) row.

Tombstone cũng giúp remote snapshot không vô tình “hồi sinh” thực thể (entity / 엔터티) đã xóa cục bộ (local / 로컬) nhưng chưa sync.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — Offline-First, Sync, Room di chuyển (migration / 마이그레이션) và dữ liệu (data / 데이터) Integrity**, **11. Pull sync và cursor** tiếp nhận điểm tựa từ **10. Delete cần tombstone khi sync offline** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) quan trọng hơn số lượng DAO phương thức (method / 메서드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Pull sync và cursor

Với dữ liệu (data / 데이터) lớn, không nên mỗi lần sync tải toàn bộ dataset. máy chủ (server / 서버) có thể cung cấp cursor/since đơn vị từ (token / 토큰):

```text
GET /tasks/changes?cursor=abc123
→ changes + nextCursor
```

Máy khách (client / 클라이언트) transactionally apply thay đổi (change / 변경) set rồi persist `nextCursor`. Cursor chỉ được advance sau khi apply thành công; nếu crash giữa chừng, thử lại (retry / 재시도) cùng cursor phải an toàn.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Offline-First, Sync, Room di chuyển (migration / 마이그레이션) và dữ liệu (data / 데이터) Integrity**, **11. Pull sync và cursor** đã nêu tiêu chí phân biệt, còn **12. giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) quan trọng hơn số lượng DAO phương thức (method / 메서드)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **13. Pagination và Paging 3** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) quan trọng hơn số lượng DAO phương thức (method / 메서드)

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

Nếu cursor cập nhật (update / 업데이트) trước dữ liệu (data / 데이터) rồi app crash, lần sau máy chủ (server / 서버) nghĩ máy khách (client / 클라이언트) đã consume changes dù cục bộ (local / 로컬) chưa có chúng. Đây là dữ liệu (data / 데이터) integrity bug.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Offline-First, Sync, Room di chuyển (migration / 마이그레이션) và dữ liệu (data / 데이터) Integrity**, **12. giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) quan trọng hơn số lượng DAO phương thức (method / 메서드)** đã nêu tiêu chí phân biệt, còn **13. Pagination và Paging 3** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **14. Staleness và refresh chính sách (policy / 정책)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Pagination và Paging 3

Khi dataset lớn, Paging giúp tải (load / 로드) theo page và tích hợp Compose. Với mạng (network / 네트워크) + Room, `RemoteMediator` có thể điều phối remote page vào cục bộ (local / 로컬) cơ sở dữ liệu (database / 데이터베이스) trong khi UI vẫn đọc PagingSource từ Room.

Mô hình tư duy (mental model / 사고 모델) vẫn giống source-of-truth: mạng (network / 네트워크) không đưa page thẳng cho UI; nó cập nhật DB, DB invalidate PagingSource và UI nhận dữ liệu (data / 데이터) mới.

Remote key/cursor cũng là persistent trạng thái (state / 상태) và cần giao dịch (transaction / 트랜잭션) cùng page dữ liệu (data / 데이터) nếu consistency yêu cầu.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — Offline-First, Sync, Room di chuyển (migration / 마이그레이션) và dữ liệu (data / 데이터) Integrity**, **14. Staleness và refresh chính sách (policy / 정책)** tiếp nhận điểm tựa từ **13. Pagination và Paging 3** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Clock và thứ tự (ordering / 순서)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Staleness và refresh chính sách (policy / 정책)

Offline-first không nghĩa luôn tin bộ nhớ đệm (cache / 캐시) mãi mãi. Repository cần chính sách (policy / 정책): dữ liệu (data / 데이터) bao lâu thì stale, screen open có auto-refresh không, pull-to-refresh có force mạng (network / 네트워크) không, thất bại (failure / 실패) khi refresh có giữ bộ nhớ đệm (cache / 캐시) không.

Một mô hình (model / 모델) đơn giản:

```kotlin
data class Freshness(
    val lastSuccessfulSyncAt: Instant?,
    val isRefreshInProgress: Boolean,
    val lastError: SyncError?
)
```

UI có thể hiển thị cached content cùng “Last updated …” thay vì spinner full-screen.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Offline-First, Sync, Room di chuyển (migration / 마이그레이션) và dữ liệu (data / 데이터) Integrity**, **15. Clock và thứ tự (ordering / 순서)** tiếp nhận điểm tựa từ **14. Staleness và refresh chính sách (policy / 정책)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Room di chuyển (migration / 마이그레이션) là executable lịch sử (history / 이력)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Clock và thứ tự (ordering / 순서)

Không nên dựa quá nhiều vào thiết bị (device / 장치) wall clock để resolve xung đột (conflict / 충돌) vì clock có thể sai. Nếu máy chủ (server / 서버) có monotonic phiên bản (version / 버전)/revision chuỗi (sequence / 시퀀스), ưu tiên phiên bản (version / 버전) do máy chủ (server / 서버) quản lý.

`updatedAt` vẫn hữu ích cho UX, nhưng ngữ nghĩa (semantics / 의미론) xung đột (conflict / 충돌) cần rõ nguồn thời gian nào authoritative.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Offline-First, Sync, Room di chuyển (migration / 마이그레이션) và dữ liệu (data / 데이터) Integrity**, **16. Room di chuyển (migration / 마이그레이션) là executable lịch sử (history / 이력)** tiếp nhận điểm tựa từ **15. Clock và thứ tự (ordering / 순서)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. di chuyển (migration / 마이그레이션) phức tạp: create-copy-drop-rename** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Room di chuyển (migration / 마이그레이션) là executable lịch sử (history / 이력)

Lược đồ (schema / 스키마) môi trường vận hành (production / 운영 환경) thay đổi theo phiên bản (version / 버전). `fallbackToDestructiveMigration()` có thể chấp nhận cho bộ nhớ đệm (cache / 캐시) tái tạo được trong một số app, nhưng nguy hiểm nếu cơ sở dữ liệu (database / 데이터베이스) chứa user-created/offline dữ liệu (data / 데이터).

Di chuyển (migration / 마이그레이션) phải mô tả đường đi từ lược đồ (schema / 스키마) cũ sang mới:

```kotlin
val MIGRATION_3_4 = object : Migration(3, 4) {
    override fun migrate(db: SupportSQLiteDatabase) {
        db.execSQL("ALTER TABLE tasks ADD COLUMN deleted INTEGER NOT NULL DEFAULT 0")
    }
}
```

Không chỉ compile; di chuyển (migration / 마이그레이션) phải preserve bất biến (invariant / 불변식) và dữ liệu (data / 데이터) meaning.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — Offline-First, Sync, Room di chuyển (migration / 마이그레이션) và dữ liệu (data / 데이터) Integrity**, **17. di chuyển (migration / 마이그레이션) phức tạp: create-copy-drop-rename** tiếp nhận điểm tựa từ **16. Room di chuyển (migration / 마이그레이션) là executable lịch sử (history / 이력)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. kiểm thử (test / 테스트) di chuyển (migration / 마이그레이션) bằng cơ sở dữ liệu (database / 데이터베이스) thật của lược đồ (schema / 스키마) cũ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. di chuyển (migration / 마이그레이션) phức tạp: create-copy-drop-rename

SQLite không hỗ trợ mọi ALTER dễ dàng. Khi đổi primary key/kiểu (type / 타입) hoặc normalize bảng (table / 테이블), mẫu (pattern / 패턴) thường là:

```text
create new table
→ copy/transform data
→ verify
→ drop old table
→ rename new table
→ recreate index/foreign key
```

Cần đặc biệt chú ý default giá trị (value / 값), nullability, chỉ mục (index / 인덱스) unique và foreign key.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Offline-First, Sync, Room di chuyển (migration / 마이그레이션) và dữ liệu (data / 데이터) Integrity**, **17. di chuyển (migration / 마이그레이션) phức tạp: create-copy-drop-rename** nêu điều cần giải thích; **18. kiểm thử (test / 테스트) di chuyển (migration / 마이그레이션) bằng cơ sở dữ liệu (database / 데이터베이스) thật của lược đồ (schema / 스키마) cũ** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **19. AutoMigration không loại bỏ trách nhiệm hiểu lược đồ (schema / 스키마)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. kiểm thử (test / 테스트) di chuyển (migration / 마이그레이션) bằng cơ sở dữ liệu (database / 데이터베이스) thật của lược đồ (schema / 스키마) cũ

Room hỗ trợ di chuyển (migration / 마이그레이션) kiểm thử (test / 테스트). Hãy tạo DB lược đồ (schema / 스키마) N, insert dữ liệu đại diện edge cases, chạy di chuyển (migration / 마이그레이션) tới hiện tại (current / 현재) phiên bản (version / 버전) rồi assert cả lược đồ (schema / 스키마) lẫn dữ liệu (data / 데이터).

Các trường hợp (case / 사례) nên có: null cũ, unicode, bản ghi (record / 레코드) lớn, foreign key, duplicate dữ liệu (data / 데이터) trước khi thêm unique ràng buộc (constraint / 제약조건), tombstone/pending mutation và người dùng (user / 사용자) ở trạng thái offline lâu ngày.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Offline-First, Sync, Room di chuyển (migration / 마이그레이션) và dữ liệu (data / 데이터) Integrity**, **18. kiểm thử (test / 테스트) di chuyển (migration / 마이그레이션) bằng cơ sở dữ liệu (database / 데이터베이스) thật của lược đồ (schema / 스키마) cũ** nêu điều cần giải thích; **19. AutoMigration không loại bỏ trách nhiệm hiểu lược đồ (schema / 스키마)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **20. lược đồ (schema / 스키마) export và rà soát (review / 검토)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. AutoMigration không loại bỏ trách nhiệm hiểu lược đồ (schema / 스키마)

AutoMigration hữu ích cho thay đổi Room suy luận được. Nhưng nếu rename/delete column, transform ngữ nghĩa (semantic / 의미적) hoặc đổi bất biến (invariant / 불변식), cần spec/manual di chuyển (migration / 마이그레이션). Đừng coi “bản dựng (build / 빌드) pass” là bằng chứng dữ liệu (data / 데이터) môi trường vận hành (production / 운영 환경) an toàn.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — Offline-First, Sync, Room di chuyển (migration / 마이그레이션) và dữ liệu (data / 데이터) Integrity**, **20. lược đồ (schema / 스키마) export và rà soát (review / 검토)** tiếp nhận điểm tựa từ **19. AutoMigration không loại bỏ trách nhiệm hiểu lược đồ (schema / 스키마)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. quay lui (rollback / 롤백) tính tương thích (compatibility / 호환성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. lược đồ (schema / 스키마) export và rà soát (review / 검토)

Export Room lược đồ (schema / 스키마) vào repository giúp rà soát (review / 검토) diff lược đồ (schema / 스키마) và kiểm thử (test / 테스트) di chuyển (migration / 마이그레이션). lược đồ (schema / 스키마) tệp (file / 파일) là sản phẩm tạo ra (artifact / 산출물) quan trọng, không phải noise bản dựng (build / 빌드).

Một PR đổi thực thể (entity / 엔터티) nên được rà soát (review / 검토) cùng lược đồ (schema / 스키마) diff: column nào thêm, default gì, chỉ mục (index / 인덱스) thay đổi không, di chuyển (migration / 마이그레이션) đường dẫn (path / 경로) từ phiên bản (version / 버전) trước ở đâu.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Offline-First, Sync, Room di chuyển (migration / 마이그레이션) và dữ liệu (data / 데이터) Integrity**, **21. quay lui (rollback / 롤백) tính tương thích (compatibility / 호환성)** tiếp nhận điểm tựa từ **20. lược đồ (schema / 스키마) export và rà soát (review / 검토)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Serialization tính tương thích (compatibility / 호환성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. quay lui (rollback / 롤백) tính tương thích (compatibility / 호환성)

Nếu bản phát hành (release / 릴리스) phiên bản (version / 버전) 10 migrate cơ sở dữ liệu (database / 데이터베이스) irreversible và sau đó phải quay lui (rollback / 롤백) APK về phiên bản (version / 버전) 9, phiên bản (version / 버전) 9 có thể không đọc lược đồ (schema / 스키마) mới. Đây là vấn đề bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링).

Các chiến lược gồm forward-compatible di chuyển (migration / 마이그레이션), staged rollout nhỏ trước, backup/export cần thiết, hoặc tránh destructive ngữ nghĩa (semantic / 의미적) thay đổi (change / 변경) trong một bản phát hành (release / 릴리스) có rủi ro (risk / 위험) cao. cơ sở dữ liệu (database / 데이터베이스) thiết kế (design / 설계) và rollout chiến lược (strategy / 전략) không thể tách rời.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Offline-First, Sync, Room di chuyển (migration / 마이그레이션) và dữ liệu (data / 데이터) Integrity**, **22. Serialization tính tương thích (compatibility / 호환성)** tiếp nhận điểm tựa từ **21. quay lui (rollback / 롤백) tính tương thích (compatibility / 호환성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Unknown enum và máy chủ (server / 서버) evolution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Serialization tính tương thích (compatibility / 호환성)

Pending mutation payload lưu JSON trong DB phải chịu versioning. Nếu lớp (class / 클래스) Kotlin đổi trường dữ liệu (field / 필드) name/kiểu (type / 타입), worker phiên bản (version / 버전) mới có thể không parse pending payload do phiên bản (version / 버전) cũ tạo.

Có thể lưu tường minh (explicit / 명시적) payload phiên bản (version / 버전):

```json
{
  "schemaVersion": 2,
  "operationId": "...",
  "taskId": "...",
  "changes": { ... }
}
```

Deserializer migrate payload cũ hoặc hàng đợi (queue / 큐) bảng (table / 테이블) lưu structured columns thay vì raw serialized đối tượng (object / 객체) tùy use trường hợp (case / 사례).

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — Offline-First, Sync, Room di chuyển (migration / 마이그레이션) và dữ liệu (data / 데이터) Integrity**, **23. Unknown enum và máy chủ (server / 서버) evolution** tiếp nhận điểm tựa từ **22. Serialization tính tương thích (compatibility / 호환성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Sync trạng thái (state / 상태) không nên leak hiện thực (implementation / 구현) lên UI quá sâu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Unknown enum và máy chủ (server / 서버) evolution

Máy chủ (server / 서버) có thể thêm enum mới trước khi app cập nhật (update / 업데이트). Nếu máy khách (client / 클라이언트) deserialize enum strict và crash, tính tương thích (compatibility / 호환성) kém. Cân nhắc `Unknown(rawValue)` mẫu (pattern / 패턴) hoặc custom serializer cho giao thức (protocol / 프로토콜) có khả năng mở rộng.

Tương tự, mạng (network / 네트워크) DTO nên tolerant với additive fields nhưng strict với bất biến (invariant / 불변식) thật sự cần thiết.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Offline-First, Sync, Room di chuyển (migration / 마이그레이션) và dữ liệu (data / 데이터) Integrity**, **24. Sync trạng thái (state / 상태) không nên leak hiện thực (implementation / 구현) lên UI quá sâu** tiếp nhận điểm tựa từ **23. Unknown enum và máy chủ (server / 서버) evolution** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Multi-account và cơ sở dữ liệu (database / 데이터베이스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Sync trạng thái (state / 상태) không nên leak hiện thực (implementation / 구현) lên UI quá sâu

UI có thể cần biết “pending”, “sync failed” để hiển thị icon/thử lại (retry / 재시도). Nhưng UI không cần biết WorkManager ID hoặc HTTP status raw.

Map hạ tầng (infrastructure / 인프라) trạng thái (state / 상태) thành lĩnh vực (domain / 도메인)/UI concept:

```kotlin
enum class SyncStatus {
    Synced,
    Pending,
    NeedsAttention
}
```

Detailed diagnostics có thể nằm trong logging/gỡ lỗi (debug / 디버그) tooling.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Offline-First, Sync, Room di chuyển (migration / 마이그레이션) và dữ liệu (data / 데이터) Integrity**, **24. Sync trạng thái (state / 상태) không nên leak hiện thực (implementation / 구현) lên UI quá sâu** nêu điều cần giải thích; **25. Multi-account và cơ sở dữ liệu (database / 데이터베이스)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **26. Sync khả năng quan sát (observability / 관측 가능성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Multi-account và cơ sở dữ liệu (database / 데이터베이스)

Nếu app hỗ trợ nhiều account, hãy quyết định sớm giữa cơ sở dữ liệu (database / 데이터베이스) riêng mỗi account và dùng chung (shared / 공유) DB với `accountId`. Cả hai đều có sự đánh đổi (trade-off / 트레이드오프) về isolation, di chuyển (migration / 마이그레이션) và switching.

Điều không được phép là truy vấn (query / 쿼리) quên filter account dẫn tới dữ liệu (data / 데이터) leakage. Nếu dùng chung (shared / 공유) bảng (table / 테이블), repository/DAO API nên làm account phạm vi (scope / 범위) khó bị quên.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) 03 — Offline-First, Sync, Room di chuyển (migration / 마이그레이션) và dữ liệu (data / 데이터) Integrity**, **25. Multi-account và cơ sở dữ liệu (database / 데이터베이스)** nêu điều cần giải thích; **26. Sync khả năng quan sát (observability / 관측 가능성)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **27. thất bại (failure / 실패) drill** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Sync khả năng quan sát (observability / 관측 가능성)

Môi trường vận hành (production / 운영 환경) sync cần chỉ số (metric / 지표)/sự kiện (event / 이벤트) như hàng đợi (queue / 큐) length, age của oldest pending mutation, success tỷ lệ (rate / 비율), permanent thất bại (failure / 실패) count, xung đột (conflict / 충돌) count, di chuyển (migration / 마이그레이션) thất bại (failure / 실패) và average sync duration.

Nếu người dùng (user / 사용자) báo “ghi chú (note / 노트) của tôi không lên máy khác”, log chỉ có dấu vết ngăn xếp (stack trace / 스택 트레이스) HTTP là chưa đủ. Bạn cần biết cục bộ (local / 로컬) thao tác (operation / 연산) ID, sync vòng đời (lifecycle / 생명주기) và máy chủ (server / 서버) correlation ID — nhưng không log nội dung nhạy cảm nếu không cần.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) 03 — Offline-First, Sync, Room di chuyển (migration / 마이그레이션) và dữ liệu (data / 데이터) Integrity**, **27. thất bại (failure / 실패) drill** tiếp nhận điểm tựa từ **26. Sync khả năng quan sát (observability / 관측 가능성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. cấp cao (senior / 시니어) notes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. thất bại (failure / 실패) drill

Một sync kiến trúc (architecture / 아키텍처) nên được kiểm thử (test / 테스트) bằng các scenario:

1. edit offline, kill tiến trình (process / 프로세스), reopen, reconnect;
2. cùng thực thể (entity / 엔터티) edit trên hai thiết bị (device / 장치);
3. yêu cầu (request / 요청) hết thời gian chờ (timeout / 타임아웃) sau khi máy chủ (server / 서버) đã lần ghi nhận (commit / 커밋);
4. refresh snapshot đến trước pending cục bộ (local / 로컬) cập nhật (update / 업데이트);
5. delete offline rồi máy chủ (server / 서버) cũng cập nhật (update / 업데이트) thực thể (entity / 엔터티);
6. truy cập (access / 접근) đơn vị từ (token / 토큰) expire giữa worker;
7. app upgrade khi hàng đợi (queue / 큐) cũ còn pending;
8. cơ sở dữ liệu (database / 데이터베이스) full/disk lỗi (error / 오류);
9. người dùng (user / 사용자) logout trong khi hàng đợi (queue / 큐) còn công việc (work / 작업);
10. máy chủ (server / 서버) lược đồ (schema / 스키마) thêm unknown enum.

Nếu hành vi (behavior / 동작) mong muốn chưa được định nghĩa, đó là sản phẩm (product / 제품)/kiến trúc (architecture / 아키텍처) gap chứ không chỉ là kiểm thử (test / 테스트) gap.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) 03 — Offline-First, Sync, Room di chuyển (migration / 마이그레이션) và dữ liệu (data / 데이터) Integrity**, **28. cấp cao (senior / 시니어) notes** tiếp nhận điểm tựa từ **27. thất bại (failure / 실패) drill** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 28. cấp cao (senior / 시니어) notes

Offline-first là một **hệ thống phân tán (distributed system / 분산 시스템) nhỏ**. Có replica cục bộ (local / 로컬), máy chủ (server / 서버) authoritative hoặc co-authoritative, unreliable mạng (network / 네트워크), thử lại (retry / 재시도), duplicate delivery, clock/phiên bản (version / 버전), xung đột (conflict / 충돌) và eventual consistency. Khi nhìn theo góc này, nhiều quyết định trở nên rõ hơn.

Dùng cơ sở dữ liệu (database / 데이터베이스) giao dịch (transaction / 트랜잭션) để bảo vệ bất biến (invariant / 불변식) cục bộ (local / 로컬); dùng thao tác (operation / 연산) ID/idempotency để bảo vệ thử lại (retry / 재시도) mạng (network / 네트워크); dùng phiên bản (version / 버전)/cursor để bảo vệ reconciliation; dùng durable hàng đợi (queue / 큐) khi công việc (work / 작업) phải sống qua tiến trình (process / 프로세스) death; dùng tường minh (explicit / 명시적) xung đột (conflict / 충돌) chính sách (policy / 정책) thay vì “máy chủ (server / 서버) wins vì dễ”.

Quan trọng nhất: không claim offline-first chỉ vì app mở được khi airplane chế độ (mode / 모드). Một tính năng (feature / 기능) write-offline thực sự phải chứng minh được dữ liệu không mất, không duplicate và có đường khôi phục (recovery / 복구) khi xung đột (conflict / 충돌) hoặc di chuyển (migration / 마이그레이션) xảy ra.

> **Bàn giao:** Sau **28. cấp cao (senior / 시니어) notes**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
