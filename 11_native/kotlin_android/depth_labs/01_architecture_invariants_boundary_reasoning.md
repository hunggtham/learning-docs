# Depth Lab 01 — Architecture Invariants, Boundary Reasoning và State Ownership

Depth Lab này không giới thiệu thêm một pattern kiến trúc mới. Mục tiêu là đi sâu vào câu hỏi khó hơn: **làm sao biết kiến trúc hiện tại có thực sự đúng khi hệ thống gặp concurrency, process death, partial failure, retry và thay đổi requirement?**

Ở level Senior/Master, việc nhớ MVVM, MVI, Clean Architecture hay Repository pattern không còn là phần khó nhất. Phần khó là xác định các **invariant** — những điều bắt buộc phải luôn đúng — rồi thiết kế ownership, data flow và boundary để hệ thống bảo vệ các invariant đó ngay cả khi execution order thay đổi.

---

## 1. Kiến trúc nên bắt đầu từ invariant, không từ class diagram

Giả sử ứng dụng có feature article với bookmark, offline cache và đồng bộ server. Một class diagram có thể rất đẹp:

```text
Compose -> ViewModel -> UseCase -> Repository -> Room / Retrofit
```

Nhưng sơ đồ này chưa nói được điều gì quan trọng nhất. Ta cần biết những invariant như:

```text
I1. Một article chỉ có một trạng thái bookmark chính thức ở local source of truth.
I2. UI không được hiển thị bookmark state trái ngược với local database quá một khoảng thời gian hợp lý.
I3. Nếu app bị kill sau khi user bookmark nhưng trước khi sync server xong, intent của user không được mất.
I4. Retry cùng một mutation không được tạo hiệu ứng lặp trên server.
I5. Một network response cũ không được ghi đè dữ liệu mới hơn.
```

Khi invariant rõ, kiến trúc bắt đầu có thể kiểm chứng. Repository tồn tại không phải vì tài liệu bảo “nên có repository”, mà vì nó là boundary nơi ta có thể enforce source-of-truth, conflict policy và mutation semantics.

---

## 2. State ownership là câu hỏi “ai có quyền quyết định giá trị cuối cùng?”

Một giá trị có thể xuất hiện ở nhiều layer nhưng chỉ nên có một owner chính.

Ví dụ `isBookmarked` có thể xuất hiện trong:

```text
ArticleEntity.isBookmarked
Article.isBookmarked
ArticleUiModel.isBookmarked
BookmarkButton.checked
```

Bốn chỗ có giá trị giống nhau không có nghĩa bốn chỗ cùng sở hữu state. Nếu database là local source of truth, các layer phía trên chỉ đang **project** hoặc **render** state đó.

Mental model:

```text
owner -> authoritative state
projection -> derived state
cache -> performance copy
snapshot -> state tại một thời điểm
command -> yêu cầu thay đổi state
```

Một lỗi phổ biến là biến projection thành owner. Ví dụ UI tự `remember { mutableStateOf(article.isBookmarked) }` rồi toggle độc lập. Từ thời điểm đó, hệ thống có hai owner cạnh tranh: local UI và database.

### 2.1 Derived state không cần persistence riêng

Nếu `canSubmit` được suy ra từ `name.isNotBlank() && email.isValid()`, nó là derived state. Persist cả `name`, `email`, `canSubmit` tạo thêm invariant phải đồng bộ ba biến.

Tốt hơn:

```kotlin
data class FormState(
    val name: String,
    val email: String
) {
    val canSubmit: Boolean
        get() = name.isNotBlank() && email.isValidEmail()
}
```

Càng ít source of truth, càng ít trạng thái bất hợp lệ có thể tồn tại.

---

## 3. Boundary là nơi semantic thay đổi

Boundary không chỉ là package hoặc interface. Một boundary quan trọng xuất hiện khi **ý nghĩa của dữ liệu thay đổi**.

Ví dụ:

```text
HTTP JSON
  -> DTO
  -> validated application data
  -> persisted entity
  -> domain model
  -> UI projection
```

Server có thể trả:

```json
{
  "bookmark": null,
  "published_at": "2026-09-20T10:30:00Z",
  "category": "NEW_CATEGORY"
}
```

DTO layer có nhiệm vụ đọc wire format. Boundary DTO -> domain phải quyết định:

- `bookmark=null` nghĩa là false, unknown hay protocol error?
- timezone của `published_at` được normalize thế nào?
- unknown enum có fallback hay reject toàn payload?

Nếu bỏ boundary và deserialize thẳng vào domain model, protocol semantics âm thầm trở thành application semantics.

---

## 4. Command và state phải được tách mental model

UI event không phải state.

```text
User taps bookmark
```

đây là command/intention.

```text
Article is bookmarked
```

đây là state.

Nếu hệ thống đang offline, command có thể đã được accept nhưng remote state chưa đạt desired state. Vì vậy ta cần model nhiều trạng thái hơn boolean đơn giản:

```kotlin
enum class SyncStatus {
    Synced,
    Pending,
    Failed
}

data class BookmarkState(
    val desired: Boolean,
    val syncStatus: SyncStatus
)
```

UI có thể hiển thị bookmark đã bật nhưng kèm pending indicator. Điều này mô tả hệ thống thật chính xác hơn việc rollback UI ngay khi request fail.

---

## 5. Read model và write model không nhất thiết giống nhau

Một screen có thể cần read model rất giàu dữ liệu:

```kotlin
data class ArticleDetailUiModel(
    val title: String,
    val authorDisplayName: String,
    val formattedDate: String,
    val isBookmarked: Boolean,
    val relatedArticles: List<RelatedArticleUi>
)
```

Nhưng write command có thể cực nhỏ:

```kotlin
data class SetBookmarkCommand(
    val articleId: String,
    val desired: Boolean
)
```

Đừng gửi nguyên UI model xuống data layer chỉ để thay đổi một field. UI model chứa presentation concern và có thể stale.

Một write command tốt nên mang đúng **intent tối thiểu** cần cho operation.

---

## 6. Stale snapshot là một trong những nguồn bug khó nhất

Giả sử ViewModel load article:

```kotlin
val article = repository.getArticle(id)
```

Sau đó user đợi 20 giây rồi bấm bookmark. Nếu handler dùng lại `article.isBookmarked` từ snapshot cũ:

```kotlin
repository.setBookmark(id, !article.isBookmarked)
```

trong 20 giây đó state có thể đã thay đổi do sync, notification, screen khác hoặc account switch.

Đây là bug **read-modify-write trên snapshot stale**.

An toàn hơn là operation thể hiện intent:

```kotlin
repository.toggleBookmark(id)
```

hoặc tốt hơn khi UI biết desired value:

```kotlin
repository.setBookmark(id, desired = true)
```

Data layer thực hiện mutation trên source of truth hiện tại trong transaction phù hợp.

---

## 7. Transaction boundary phải đi cùng business invariant

Nếu bookmark mutation cần đồng thời:

1. đổi `articles.isBookmarked`,
2. insert một pending sync mutation,
3. ghi `updatedAt`,

ba thao tác này có một invariant chung:

> hoặc cả ba cùng tồn tại, hoặc không cái nào tồn tại.

Vì vậy transaction nên bao quanh cả ba:

```kotlin
@Transaction
suspend fun setBookmarkWithOutbox(
    articleId: String,
    desired: Boolean,
    mutationId: String,
    now: Instant
) {
    updateBookmark(articleId, desired, now)
    insertOutbox(
        OutboxEntity(
            id = mutationId,
            type = "SET_BOOKMARK",
            entityId = articleId,
            payload = encodeBookmark(desired),
            createdAt = now
        )
    )
}
```

Nếu update article thành công nhưng insert outbox fail, user thấy bookmark mới nhưng operation sẽ không bao giờ sync. Đó là violation của business invariant, không chỉ database bug.

---

## 8. Repository interface nên mô tả semantic, không mô tả transport

Interface yếu:

```kotlin
interface ArticleRepository {
    suspend fun getArticlesFromApi(): List<ArticleDto>
    suspend fun saveArticlesToDb(items: List<ArticleEntity>)
}
```

Caller phải biết cả remote và local strategy. Repository chỉ đổi tên data source.

Interface giàu semantic hơn:

```kotlin
interface ArticleRepository {
    fun observeArticles(query: ArticleQuery): Flow<List<Article>>
    suspend fun refresh(query: ArticleQuery): RefreshResult
    suspend fun setBookmark(articleId: ArticleId, desired: Boolean)
}
```

Implementation được tự do thay đổi từ REST sang GraphQL, từ Room sang local engine khác hoặc thêm cache mà không đổi semantic contract với caller.

---

## 9. Error boundary phải phân biệt “operation failed” và “system state unknown”

Có hai loại failure rất khác nhau:

```text
A. Request chưa tới server -> operation có thể chưa xảy ra.
B. Server đã xử lý, nhưng response bị mất -> client không biết operation đã xảy ra chưa.
```

Case B gọi là **ambiguous outcome**. Với payment, booking hoặc mutation quan trọng, retry mù có thể tạo duplicate effect.

Vì vậy operation cần idempotency key hoặc query-able operation id:

```text
clientMutationId = UUID
POST /bookmark
Idempotency-Key: 89f...
```

Nếu timeout sau commit, client retry cùng key. Server trả kết quả của operation trước thay vì thực thi lần hai.

Architecture tốt phải model được ambiguous outcome; `catch IOException -> retry` là chưa đủ.

---

## 10. ViewModel state machine giúp loại bỏ trạng thái bất khả thi

Boolean rời rạc dễ tạo state vô nghĩa:

```kotlin
isLoading = true
hasError = true
hasContent = false
isRefreshing = true
```

Có thể đây là state hợp lệ, cũng có thể không. Khi nhiều boolean tăng, số combination tăng theo `2^n`.

Một state machine rõ hơn:

```kotlin
sealed interface ArticlesState {
    data object InitialLoading : ArticlesState

    data class Content(
        val items: List<ArticleUiModel>,
        val refresh: RefreshState = RefreshState.Idle
    ) : ArticlesState

    data class Empty(
        val refresh: RefreshState = RefreshState.Idle
    ) : ArticlesState

    data class FatalError(
        val message: UserMessage
    ) : ArticlesState
}
```

Trong `Content`, refresh có thể fail nhưng content vẫn tồn tại. Fatal error chỉ dành cho trường hợp không có usable content.

State model tốt encode invariant vào type system thay vì dựa vào comment.

---

## 11. Process death test là architecture test mạnh

Configuration change thường giữ được ViewModel, nên nhiều kiến trúc tưởng đúng vì xoay màn hình vẫn hoạt động. Process death mới lộ source-of-truth sai.

Test mental sequence:

```text
1. User mở ArticleDetail(id=42)
2. UI load data
3. User đổi filter hoặc nhập query
4. App đi background
5. OS kill process
6. User quay lại từ recent tasks hoặc notification
```

Sau bước 6, hệ thống chỉ còn những thứ thực sự persist hoặc reconstruct được:

- navigation arguments,
- SavedStateHandle data nhỏ,
- Room/DataStore/file,
- remote backend.

Mọi singleton cache, in-memory repository state và static variable đều biến mất.

Nếu screen không thể reconstruct từ stable identifier, architecture đang phụ thuộc lifecycle may mắn.

---

## 12. Navigation argument nên là identity, không phải object graph

Không nên truyền một object lớn như:

```kotlin
navController.navigate(ArticleDetailRoute(article = article))
```

vì object có thể stale, khó persist, versioning kém và không phản ánh source of truth.

Tốt hơn:

```kotlin
navController.navigate(ArticleDetailRoute(articleId = article.id))
```

Detail screen reconstruct state bằng `articleId`.

Identity nhỏ và stable là một trong những boundary quan trọng nhất giữa navigation và data architecture.

---

## 13. Side effect phải có owner và retry semantics

Một action như analytics, push registration hay upload attachment không nên được “tiện tay” gọi ở nhiều layer.

Hãy hỏi:

```text
Side effect này:
- cần at-most-once, at-least-once hay exactly-once về business meaning?
- mất khi process chết có được không?
- retry được không?
- cần transaction với local mutation không?
- có yêu cầu ordering không?
```

Ví dụ analytics thường chấp nhận best-effort. Payment capture không chấp nhận best-effort.

Cùng là `suspend fun`, nhưng reliability contract hoàn toàn khác.

---

## 14. Dependency graph không phải architecture graph

Hilt có thể resolve:

```text
ViewModel -> Repository -> Api
```

nhưng điều đó không chứng minh dependency direction đúng về mặt business.

Một module có thể compile nhưng vẫn sai kiến trúc nếu:

- feature A import internal model của feature B,
- database entity leak lên UI,
- analytics SDK type xuất hiện trong domain API,
- networking exception leak tới screen,
- library module expose implementation dependency không cần thiết.

Compile graph chỉ chứng minh “code nối được”. Architecture graph cần chứng minh “boundary hợp lý”.

---

## 15. Kiến trúc nên được review bằng timeline, không chỉ bằng sơ đồ

Với một mutation, hãy viết timeline thật:

```text
T0 user tap
T1 ViewModel nhận command
T2 transaction local commit
T3 Room emit
T4 UI render desired state
T5 worker gửi request
T6 server commit
T7 response về
T8 local outbox mark completed
```

Sau đó chèn failure vào từng điểm:

```text
kill process giữa T2 và T5
network timeout giữa T5 và T6
response mất giữa T6 và T7
database full ở T8
account logout giữa T4 và T5
```

Nếu design không xác định được state sau mỗi failure, implementation chưa đủ chặt.

---

## 16. Architecture decision record nên ghi trade-off, không chỉ kết luận

ADR yếu:

```text
Chọn Room làm database.
```

ADR hữu ích hơn:

```text
Decision:
Room là local source of truth cho article.

Why:
- cần observe reactive data,
- cần transaction,
- cần migration schema,
- cần offline persistence.

Rejected:
DataStore vì dataset lớn và cần relational query.
In-memory cache vì không sống qua process death.

Consequences:
- cần migration test,
- cần DAO transaction boundary,
- schema trở thành compatibility contract giữa app versions.
```

ADR tốt giúp người mới hiểu reasoning thay vì chỉ kế thừa một tool choice.

---

## 17. Khi nào không cần Repository, UseCase hoặc multi-module?

Architecture trưởng thành không đồng nghĩa nhiều layer nhất.

Nếu một feature local-only cực nhỏ:

```text
UI -> ViewModel -> DataStore-backed settings store
```

có thể đủ.

Thêm `UseCase -> Repository -> DataSource` cho một boolean preference có thể chỉ tăng indirection.

Nguyên tắc:

> thêm abstraction khi nó bảo vệ một boundary, invariant, reuse point hoặc change axis cụ thể.

Nếu không chỉ ra được điều đó, abstraction có thể chỉ là ceremony.

---

## 18. Review checklist theo invariant

Khi review một feature production, đừng bắt đầu bằng tên package. Hãy lần lượt trả lời:

| Câu hỏi | Điều cần xác định |
|---|---|
| Source of truth ở đâu? | Room, DataStore, backend hay state holder |
| Ai được mutate? | một owner hay nhiều writer cạnh tranh |
| State nào derived? | tránh persist duplicate truth |
| Mutation có durable không? | process death có làm mất intent không |
| Operation có idempotent không? | retry có tạo duplicate effect không |
| Snapshot có stale được không? | read-modify-write có race không |
| Boundary nào validate data? | DTO/domain/entity/UI mapping |
| Failure có ambiguous outcome không? | timeout sau remote commit |
| Navigation reconstruct bằng gì? | stable id thay vì object graph |
| Release rollback có đọc data mới không? | schema/data backward compatibility |

---

## 19. Bài tập reasoning

Hãy thiết kế feature “favorite article” với yêu cầu:

```text
- hoạt động offline,
- sync khi có mạng,
- user có thể login account khác,
- server hỗ trợ nhiều device,
- mutation có thể đến out-of-order,
- process có thể chết bất kỳ lúc nào.
```

Trước khi viết code, tự định nghĩa:

1. source of truth local,
2. remote authority,
3. mutation identity,
4. conflict policy,
5. logout cleanup policy,
6. retry semantics,
7. stale response protection,
8. observability fields.

Nếu chưa trả lời được tám điểm này, viết thêm class chưa giải quyết được phần khó nhất.

---

## 20. Kết luận

Architecture ở level Senior không còn là “dùng pattern nào”. Nó là khả năng biến requirement thành invariant, biến invariant thành ownership và boundary, rồi chứng minh hệ thống vẫn đúng khi execution order không còn lý tưởng.

Mental model nên giữ:

```text
requirement
-> invariant
-> state owner
-> source of truth
-> command semantics
-> transaction boundary
-> failure model
-> reconstruction
-> observability
-> compatibility
```

Khi chuỗi này rõ, framework chỉ còn là công cụ hiện thực hóa quyết định kiến trúc.