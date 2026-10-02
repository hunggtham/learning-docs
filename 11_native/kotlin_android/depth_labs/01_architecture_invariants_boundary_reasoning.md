# Độ sâu (depth / 깊이) Lab 01 — kiến trúc (architecture / 아키텍처) Invariants, ranh giới (boundary / 경계) lập luận (reasoning / 추론) và quyền sở hữu trạng thái (state ownership / 상태 소유권)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Độ sâu (depth / 깊이) Lab 01 — kiến trúc (architecture / 아키텍처) Invariants, ranh giới (boundary / 경계) lập luận (reasoning / 추론) và quyền sở hữu trạng thái (state ownership / 상태 소유권)**. Route đi từ invariants → state ownership → data flow và boundaries → concurrency/process death/retry → requirement change và failure evidence, để kiến trúc được đánh giá bằng điều luôn phải đúng.

Độ sâu (depth / 깊이) Lab này không giới thiệu thêm một mẫu (pattern / 패턴) kiến trúc mới. Mục tiêu là đi sâu vào câu hỏi khó hơn: **làm sao biết kiến trúc hiện tại có thực sự đúng khi hệ thống gặp tính đồng thời (concurrency / 동시성), tiến trình (process / 프로세스) death, partial thất bại (failure / 실패), thử lại (retry / 재시도) và thay đổi yêu cầu (requirement / 요구사항)?**

Ở mức (level / 수준) cấp cao (senior / 시니어)/Master, việc nhớ MVVM, MVI, Clean kiến trúc (architecture / 아키텍처) hay Repository mẫu (pattern / 패턴) không còn là phần khó nhất. Phần khó là xác định các **bất biến (invariant / 불변식)** — những điều bắt buộc phải luôn đúng — rồi thiết kế quyền sở hữu (ownership / 소유권), luồng dữ liệu (data flow / 데이터 흐름) và ranh giới (boundary / 경계) để hệ thống bảo vệ các bất biến (invariant / 불변식) đó ngay cả khi thực thi (execution / 실행) thứ tự (order / 순서) thay đổi.

---

## 1. Kiến trúc nên bắt đầu từ bất biến (invariant / 불변식), không từ lớp (class / 클래스) diagram

Giả sử ứng dụng có tính năng (feature / 기능) article với bookmark, offline bộ nhớ đệm (cache / 캐시) và đồng bộ máy chủ (server / 서버). Một lớp (class / 클래스) diagram có thể rất đẹp:

```text
Compose -> ViewModel -> UseCase -> Repository -> Room / Retrofit
```

Nhưng sơ đồ này chưa nói được điều gì quan trọng nhất. Ta cần biết những bất biến (invariant / 불변식) như:

```text
I1. Một article chỉ có một trạng thái bookmark chính thức ở local source of truth.
I2. UI không được hiển thị bookmark state trái ngược với local database quá một khoảng thời gian hợp lý.
I3. Nếu app bị kill sau khi user bookmark nhưng trước khi sync server xong, intent của user không được mất.
I4. Retry cùng một mutation không được tạo hiệu ứng lặp trên server.
I5. Một network response cũ không được ghi đè dữ liệu mới hơn.
```

Khi bất biến (invariant / 불변식) rõ, kiến trúc bắt đầu có thể kiểm chứng. Repository tồn tại không phải vì tài liệu bảo “nên có repository”, mà vì nó là ranh giới (boundary / 경계) nơi ta có thể enforce source-of-truth, xung đột (conflict / 충돌) chính sách (policy / 정책) và mutation ngữ nghĩa (semantics / 의미론).

---

> **Chuyển mạch:** Invariant nêu điều phải luôn đúng; state ownership trả lời ai quyết định giá trị cuối, rồi boundary tiếp theo xác định nơi semantics và trách nhiệm đổi.

## 2. quyền sở hữu trạng thái (state ownership / 상태 소유권) là câu hỏi “ai có quyền quyết định giá trị cuối cùng?”

Một giá trị có thể xuất hiện ở nhiều tầng (layer / 계층) nhưng chỉ nên có một đơn vị sở hữu (owner / 오너) chính.

Ví dụ `isBookmarked` có thể xuất hiện trong:

```text
ArticleEntity.isBookmarked
Article.isBookmarked
ArticleUiModel.isBookmarked
BookmarkButton.checked
```

Bốn chỗ có giá trị giống nhau không có nghĩa bốn chỗ cùng sở hữu trạng thái (state / 상태). Nếu cơ sở dữ liệu (database / 데이터베이스) là cục bộ (local / 로컬) nguồn chuẩn (source of truth / 정본), các tầng (layer / 계층) phía trên chỉ đang **dự án (project / 프로젝트)** hoặc **kết xuất (render / 렌더링)** trạng thái (state / 상태) đó.

Mô hình tư duy (mental model / 사고 모델):

```text
owner -> authoritative state
projection -> derived state
cache -> performance copy
snapshot -> state tại một thời điểm
command -> yêu cầu thay đổi state
```

Một lỗi phổ biến là biến projection thành đơn vị sở hữu (owner / 오너). Ví dụ UI tự `remember { mutableStateOf(article.isBookmarked) }` rồi toggle độc lập. Từ thời điểm đó, hệ thống có hai đơn vị sở hữu (owner / 오너) cạnh tranh: cục bộ (local / 로컬) UI và cơ sở dữ liệu (database / 데이터베이스).

### 2.1 Derived trạng thái (state / 상태) không cần persistence riêng

Nếu `canSubmit` được suy ra từ `name.isNotBlank() && email.isValid()`, nó là derived trạng thái (state / 상태). Persist cả `name`, `email`, `canSubmit` tạo thêm bất biến (invariant / 불변식) phải đồng bộ ba biến.

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

Càng ít nguồn chuẩn (source of truth / 정본), càng ít trạng thái bất hợp lệ có thể tồn tại.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 01 — kiến trúc (architecture / 아키텍처) Invariants, ranh giới (boundary / 경계) lập luận (reasoning / 추론) và quyền sở hữu trạng thái (state ownership / 상태 소유권)**, **2. quyền sở hữu trạng thái (state ownership / 상태 소유권) là câu hỏi “ai có quyền quyết định giá trị cuối cùng?”** đã nêu tiêu chí phân biệt, còn **3. ranh giới (boundary / 경계) là nơi ngữ nghĩa (semantic / 의미적) thay đổi** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **4. Command và trạng thái (state / 상태) phải được tách mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. ranh giới (boundary / 경계) là nơi ngữ nghĩa (semantic / 의미적) thay đổi

Ranh giới (boundary / 경계) không chỉ là gói (package / 패키지) hoặc giao diện (interface / 인터페이스). Một ranh giới (boundary / 경계) quan trọng xuất hiện khi **ý nghĩa của dữ liệu thay đổi**.

Ví dụ:

```text
HTTP JSON
  -> DTO
  -> validated application data
  -> persisted entity
  -> domain model
  -> UI projection
```

Máy chủ (server / 서버) có thể trả:

```json
{
  "bookmark": null,
  "published_at": "2026-09-20T10:30:00Z",
  "category": "NEW_CATEGORY"
}
```

DTO tầng (layer / 계층) có nhiệm vụ đọc wire format. ranh giới (boundary / 경계) DTO -> lĩnh vực (domain / 도메인) phải quyết định:

- `bookmark=null` nghĩa là false, unknown hay giao thức (protocol / 프로토콜) lỗi (error / 오류)?
- timezone của `published_at` được normalize thế nào?
- unknown enum có fallback hay reject toàn payload?

Nếu bỏ ranh giới (boundary / 경계) và deserialize thẳng vào lĩnh vực (domain / 도메인) mô hình (model / 모델), giao thức (protocol / 프로토콜) ngữ nghĩa (semantics / 의미론) âm thầm trở thành ứng dụng (application / 애플리케이션) ngữ nghĩa (semantics / 의미론).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 01 — kiến trúc (architecture / 아키텍처) Invariants, ranh giới (boundary / 경계) lập luận (reasoning / 추론) và quyền sở hữu trạng thái (state ownership / 상태 소유권)**, **3. ranh giới (boundary / 경계) là nơi ngữ nghĩa (semantic / 의미적) thay đổi** đã nêu tiêu chí phân biệt, còn **4. Command và trạng thái (state / 상태) phải được tách mô hình tư duy (mental model / 사고 모델)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **5. Read mô hình (model / 모델) và ghi (write / 쓰기) mô hình (model / 모델) không nhất thiết giống nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Command và trạng thái (state / 상태) phải được tách mô hình tư duy (mental model / 사고 모델)

UI sự kiện (event / 이벤트) không phải trạng thái (state / 상태).

```text
User taps bookmark
```

đây là command/intention.

```text
Article is bookmarked
```

đây là trạng thái (state / 상태).

Nếu hệ thống đang offline, command có thể đã được accept nhưng remote trạng thái (state / 상태) chưa đạt desired trạng thái (state / 상태). Vì vậy ta cần mô hình (model / 모델) nhiều trạng thái hơn boolean đơn giản:

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

UI có thể hiển thị bookmark đã bật nhưng kèm pending indicator. Điều này mô tả hệ thống thật chính xác hơn việc quay lui (rollback / 롤백) UI ngay khi yêu cầu (request / 요청) thất bại (fail / 실패).

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 01 — kiến trúc (architecture / 아키텍처) Invariants, ranh giới (boundary / 경계) lập luận (reasoning / 추론) và quyền sở hữu trạng thái (state ownership / 상태 소유권)**, **5. Read mô hình (model / 모델) và ghi (write / 쓰기) mô hình (model / 모델) không nhất thiết giống nhau** gom các mảnh từ **4. Command và trạng thái (state / 상태) phải được tách mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **6. Stale snapshot là một trong những nguồn bug khó nhất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Read mô hình (model / 모델) và ghi (write / 쓰기) mô hình (model / 모델) không nhất thiết giống nhau

Một screen có thể cần read mô hình (model / 모델) rất giàu dữ liệu:

```kotlin
data class ArticleDetailUiModel(
    val title: String,
    val authorDisplayName: String,
    val formattedDate: String,
    val isBookmarked: Boolean,
    val relatedArticles: List<RelatedArticleUi>
)
```

Nhưng ghi (write / 쓰기) command có thể cực nhỏ:

```kotlin
data class SetBookmarkCommand(
    val articleId: String,
    val desired: Boolean
)
```

Đừng gửi nguyên UI mô hình (model / 모델) xuống dữ liệu (data / 데이터) tầng (layer / 계층) chỉ để thay đổi một trường dữ liệu (field / 필드). UI mô hình (model / 모델) chứa presentation concern và có thể stale.

Một ghi (write / 쓰기) command tốt nên mang đúng **intent tối thiểu** cần cho thao tác (operation / 연산).

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 01 — kiến trúc (architecture / 아키텍처) Invariants, ranh giới (boundary / 경계) lập luận (reasoning / 추론) và quyền sở hữu trạng thái (state ownership / 상태 소유권)**, **5. Read mô hình (model / 모델) và ghi (write / 쓰기) mô hình (model / 모델) không nhất thiết giống nhau** nêu điều cần giải thích; **6. Stale snapshot là một trong những nguồn bug khó nhất** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **7. giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) phải đi cùng nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Stale snapshot là một trong những nguồn bug khó nhất

Giả sử ViewModel tải (load / 로드) article:

```kotlin
val article = repository.getArticle(id)
```

Sau đó người dùng (user / 사용자) đợi 20 giây rồi bấm bookmark. Nếu handler dùng lại `article.isBookmarked` từ snapshot cũ:

```kotlin
repository.setBookmark(id, !article.isBookmarked)
```

trong 20 giây đó trạng thái (state / 상태) có thể đã thay đổi do sync, notification, screen khác hoặc account switch.

Đây là bug **read-modify-write trên snapshot stale**.

An toàn hơn là thao tác (operation / 연산) thể hiện intent:

```kotlin
repository.toggleBookmark(id)
```

hoặc tốt hơn khi UI biết desired giá trị (value / 값):

```kotlin
repository.setBookmark(id, desired = true)
```

Dữ liệu (data / 데이터) tầng (layer / 계층) thực hiện mutation trên nguồn chuẩn (source of truth / 정본) hiện tại trong giao dịch (transaction / 트랜잭션) phù hợp.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 01 — kiến trúc (architecture / 아키텍처) Invariants, ranh giới (boundary / 경계) lập luận (reasoning / 추론) và quyền sở hữu trạng thái (state ownership / 상태 소유권)**, **6. Stale snapshot là một trong những nguồn bug khó nhất** đã nêu tiêu chí phân biệt, còn **7. giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) phải đi cùng nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **8. Repository giao diện (interface / 인터페이스) nên mô tả ngữ nghĩa (semantic / 의미적), không mô tả vận chuyển (transport / 전송)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) phải đi cùng nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식)

Nếu bookmark mutation cần đồng thời:

1. đổi `articles.isBookmarked`,
2. insert một pending sync mutation,
3. ghi `updatedAt`,

ba thao tác này có một bất biến (invariant / 불변식) chung:

> hoặc cả ba cùng tồn tại, hoặc không cái nào tồn tại.

Vì vậy giao dịch (transaction / 트랜잭션) nên bao quanh cả ba:

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

Nếu cập nhật (update / 업데이트) article thành công nhưng insert outbox thất bại (fail / 실패), người dùng (user / 사용자) thấy bookmark mới nhưng thao tác (operation / 연산) sẽ không bao giờ sync. Đó là violation của nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식), không chỉ cơ sở dữ liệu (database / 데이터베이스) bug.

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 01 — kiến trúc (architecture / 아키텍처) Invariants, ranh giới (boundary / 경계) lập luận (reasoning / 추론) và quyền sở hữu trạng thái (state ownership / 상태 소유권)**, **7. giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) phải đi cùng nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식)** đã nêu tiêu chí phân biệt, còn **8. Repository giao diện (interface / 인터페이스) nên mô tả ngữ nghĩa (semantic / 의미적), không mô tả vận chuyển (transport / 전송)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **9. lỗi (error / 오류) ranh giới (boundary / 경계) phải phân biệt “thao tác (operation / 연산) failed” và “hệ thống (system / 시스템) trạng thái (state / 상태) unknown”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Repository giao diện (interface / 인터페이스) nên mô tả ngữ nghĩa (semantic / 의미적), không mô tả vận chuyển (transport / 전송)

Giao diện (interface / 인터페이스) yếu:

```kotlin
interface ArticleRepository {
    suspend fun getArticlesFromApi(): List<ArticleDto>
    suspend fun saveArticlesToDb(items: List<ArticleEntity>)
}
```

Caller phải biết cả remote và cục bộ (local / 로컬) chiến lược (strategy / 전략). Repository chỉ đổi tên dữ liệu (data / 데이터) nguồn (source / 소스).

Giao diện (interface / 인터페이스) giàu ngữ nghĩa (semantic / 의미적) hơn:

```kotlin
interface ArticleRepository {
    fun observeArticles(query: ArticleQuery): Flow<List<Article>>
    suspend fun refresh(query: ArticleQuery): RefreshResult
    suspend fun setBookmark(articleId: ArticleId, desired: Boolean)
}
```

Hiện thực (implementation / 구현) được tự do thay đổi từ REST sang GraphQL, từ Room sang cục bộ (local / 로컬) engine khác hoặc thêm bộ nhớ đệm (cache / 캐시) mà không đổi ngữ nghĩa (semantic / 의미적) đặc tả hợp đồng (contract / 계약) với caller.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 01 — kiến trúc (architecture / 아키텍처) Invariants, ranh giới (boundary / 경계) lập luận (reasoning / 추론) và quyền sở hữu trạng thái (state ownership / 상태 소유권)**, **8. Repository giao diện (interface / 인터페이스) nên mô tả ngữ nghĩa (semantic / 의미적), không mô tả vận chuyển (transport / 전송)** đã nêu tiêu chí phân biệt, còn **9. lỗi (error / 오류) ranh giới (boundary / 경계) phải phân biệt “thao tác (operation / 연산) failed” và “hệ thống (system / 시스템) trạng thái (state / 상태) unknown”** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **10. ViewModel máy trạng thái (state machine / 상태 머신) giúp loại bỏ trạng thái bất khả thi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. lỗi (error / 오류) ranh giới (boundary / 경계) phải phân biệt “thao tác (operation / 연산) failed” và “hệ thống (system / 시스템) trạng thái (state / 상태) unknown”

Có hai loại thất bại (failure / 실패) rất khác nhau:

```text
A. Request chưa tới server -> operation có thể chưa xảy ra.
B. Server đã xử lý, nhưng response bị mất -> client không biết operation đã xảy ra chưa.
```

Trường hợp (case / 사례) B gọi là **ambiguous kết quả (outcome / 결과)**. Với payment, booking hoặc mutation quan trọng, thử lại (retry / 재시도) mù có thể tạo duplicate tác động (effect / 효과).

Vì vậy thao tác (operation / 연산) cần idempotency key hoặc query-able thao tác (operation / 연산) id:

```text
clientMutationId = UUID
POST /bookmark
Idempotency-Key: 89f...
```

Nếu hết thời gian chờ (timeout / 타임아웃) sau lần ghi nhận (commit / 커밋), máy khách (client / 클라이언트) thử lại (retry / 재시도) cùng key. máy chủ (server / 서버) trả kết quả của thao tác (operation / 연산) trước thay vì thực thi lần hai.

Kiến trúc (architecture / 아키텍처) tốt phải mô hình (model / 모델) được ambiguous kết quả (outcome / 결과); `catch IOException -> retry` là chưa đủ.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 01 — kiến trúc (architecture / 아키텍처) Invariants, ranh giới (boundary / 경계) lập luận (reasoning / 추론) và quyền sở hữu trạng thái (state ownership / 상태 소유권)**, **9. lỗi (error / 오류) ranh giới (boundary / 경계) phải phân biệt “thao tác (operation / 연산) failed” và “hệ thống (system / 시스템) trạng thái (state / 상태) unknown”** đã nêu tiêu chí phân biệt, còn **10. ViewModel máy trạng thái (state machine / 상태 머신) giúp loại bỏ trạng thái bất khả thi** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **11. tiến trình (process / 프로세스) death kiểm thử (test / 테스트) là kiến trúc (architecture / 아키텍처) kiểm thử (test / 테스트) mạnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. ViewModel máy trạng thái (state machine / 상태 머신) giúp loại bỏ trạng thái bất khả thi

Boolean rời rạc dễ tạo trạng thái (state / 상태) vô nghĩa:

```kotlin
isLoading = true
hasError = true
hasContent = false
isRefreshing = true
```

Có thể đây là trạng thái (state / 상태) hợp lệ, cũng có thể không. Khi nhiều boolean tăng, số combination tăng theo `2^n`.

Một máy trạng thái (state machine / 상태 머신) rõ hơn:

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

Trong `Content`, refresh có thể thất bại (fail / 실패) nhưng content vẫn tồn tại. Fatal lỗi (error / 오류) chỉ dành cho trường hợp không có usable content.

Trạng thái (state / 상태) mô hình (model / 모델) tốt encode bất biến (invariant / 불변식) vào hệ kiểu (type system / 타입 시스템) thay vì dựa vào comment.

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 01 — kiến trúc (architecture / 아키텍처) Invariants, ranh giới (boundary / 경계) lập luận (reasoning / 추론) và quyền sở hữu trạng thái (state ownership / 상태 소유권)**, **10. ViewModel máy trạng thái (state machine / 상태 머신) giúp loại bỏ trạng thái bất khả thi** xác định đầu vào; **11. tiến trình (process / 프로세스) death kiểm thử (test / 테스트) là kiến trúc (architecture / 아키텍처) kiểm thử (test / 테스트) mạnh** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **12. điều hướng (navigation / 내비게이션) argument nên là định danh (identity / 식별자), không phải đối tượng (object / 객체) đồ thị (graph / 그래프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. tiến trình (process / 프로세스) death kiểm thử (test / 테스트) là kiến trúc (architecture / 아키텍처) kiểm thử (test / 테스트) mạnh

Cấu hình (configuration / 구성) thay đổi (change / 변경) thường giữ được ViewModel, nên nhiều kiến trúc tưởng đúng vì xoay màn hình vẫn hoạt động. tiến trình (process / 프로세스) death mới lộ source-of-truth sai.

Kiểm thử (test / 테스트) mental chuỗi (sequence / 시퀀스):

```text
1. User mở ArticleDetail(id=42)
2. UI load data
3. User đổi filter hoặc nhập query
4. App đi background
5. OS kill process
6. User quay lại từ recent tasks hoặc notification
```

Sau bước 6, hệ thống chỉ còn những thứ thực sự persist hoặc reconstruct được:

- điều hướng (navigation / 내비게이션) arguments,
- SavedStateHandle dữ liệu (data / 데이터) nhỏ,
- Room/DataStore/tệp (file / 파일),
- remote backend.

Mọi singleton bộ nhớ đệm (cache / 캐시), in-memory repository trạng thái (state / 상태) và static variable đều biến mất.

Nếu screen không thể reconstruct từ stable identifier, kiến trúc (architecture / 아키텍처) đang phụ thuộc vòng đời (lifecycle / 생명주기) may mắn.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 01 — kiến trúc (architecture / 아키텍처) Invariants, ranh giới (boundary / 경계) lập luận (reasoning / 추론) và quyền sở hữu trạng thái (state ownership / 상태 소유권)**, **11. tiến trình (process / 프로세스) death kiểm thử (test / 테스트) là kiến trúc (architecture / 아키텍처) kiểm thử (test / 테스트) mạnh** xác định đầu vào; **12. điều hướng (navigation / 내비게이션) argument nên là định danh (identity / 식별자), không phải đối tượng (object / 객체) đồ thị (graph / 그래프)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **13. Side tác động (effect / 효과) phải có đơn vị sở hữu (owner / 오너) và thử lại (retry / 재시도) ngữ nghĩa (semantics / 의미론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. điều hướng (navigation / 내비게이션) argument nên là định danh (identity / 식별자), không phải đối tượng (object / 객체) đồ thị (graph / 그래프)

Không nên truyền một đối tượng (object / 객체) lớn như:

```kotlin
navController.navigate(ArticleDetailRoute(article = article))
```

vì đối tượng (object / 객체) có thể stale, khó persist, versioning kém và không phản ánh nguồn chuẩn (source of truth / 정본).

Tốt hơn:

```kotlin
navController.navigate(ArticleDetailRoute(articleId = article.id))
```

Detail screen reconstruct trạng thái (state / 상태) bằng `articleId`.

Định danh (identity / 식별자) nhỏ và stable là một trong những ranh giới (boundary / 경계) quan trọng nhất giữa điều hướng (navigation / 내비게이션) và dữ liệu (data / 데이터) kiến trúc (architecture / 아키텍처).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 01 — kiến trúc (architecture / 아키텍처) Invariants, ranh giới (boundary / 경계) lập luận (reasoning / 추론) và quyền sở hữu trạng thái (state ownership / 상태 소유권)**, sau nội dung của **12. điều hướng (navigation / 내비게이션) argument nên là định danh (identity / 식별자), không phải đối tượng (object / 객체) đồ thị (graph / 그래프)**, **13. Side tác động (effect / 효과) phải có đơn vị sở hữu (owner / 오너) và thử lại (retry / 재시도) ngữ nghĩa (semantics / 의미론)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **14. phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) không phải kiến trúc (architecture / 아키텍처) đồ thị (graph / 그래프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Side tác động (effect / 효과) phải có đơn vị sở hữu (owner / 오너) và thử lại (retry / 재시도) ngữ nghĩa (semantics / 의미론)

Một hành động (action / 동작) như analytics, push registration hay upload attachment không nên được “tiện tay” gọi ở nhiều tầng (layer / 계층).

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

Cùng là `suspend fun`, nhưng độ tin cậy (reliability / 신뢰성) đặc tả hợp đồng (contract / 계약) hoàn toàn khác.

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 01 — kiến trúc (architecture / 아키텍처) Invariants, ranh giới (boundary / 경계) lập luận (reasoning / 추론) và quyền sở hữu trạng thái (state ownership / 상태 소유권)**, **14. phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) không phải kiến trúc (architecture / 아키텍처) đồ thị (graph / 그래프)** tiếp nhận điểm tựa từ **13. Side tác động (effect / 효과) phải có đơn vị sở hữu (owner / 오너) và thử lại (retry / 재시도) ngữ nghĩa (semantics / 의미론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Kiến trúc nên được rà soát (review / 검토) bằng timeline, không chỉ bằng sơ đồ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) không phải kiến trúc (architecture / 아키텍처) đồ thị (graph / 그래프)

Hilt có thể resolve:

```text
ViewModel -> Repository -> Api
```

nhưng điều đó không chứng minh phụ thuộc (dependency / 의존성) direction đúng về mặt nghiệp vụ (business / 비즈니스).

Một mô-đun (module / 모듈) có thể compile nhưng vẫn sai kiến trúc nếu:

- tính năng (feature / 기능) A import nội bộ (internal / 내부) mô hình (model / 모델) của tính năng (feature / 기능) B,
- cơ sở dữ liệu (database / 데이터베이스) thực thể (entity / 엔터티) leak lên UI,
- analytics SDK kiểu (type / 타입) xuất hiện trong lĩnh vực (domain / 도메인) API,
- networking exception leak tới screen,
- thư viện (library / 라이브러리) mô-đun (module / 모듈) expose hiện thực (implementation / 구현) phụ thuộc (dependency / 의존성) không cần thiết.

Compile đồ thị (graph / 그래프) chỉ chứng minh “mã (code / 코드) nối được”. kiến trúc (architecture / 아키텍처) đồ thị (graph / 그래프) cần chứng minh “ranh giới (boundary / 경계) hợp lý”.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 01 — kiến trúc (architecture / 아키텍처) Invariants, ranh giới (boundary / 경계) lập luận (reasoning / 추론) và quyền sở hữu trạng thái (state ownership / 상태 소유권)**, **15. Kiến trúc nên được rà soát (review / 검토) bằng timeline, không chỉ bằng sơ đồ** tiếp nhận điểm tựa từ **14. phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) không phải kiến trúc (architecture / 아키텍처) đồ thị (graph / 그래프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. kiến trúc (architecture / 아키텍처) quyết định (decision / 결정) bản ghi (record / 레코드) nên ghi sự đánh đổi (trade-off / 트레이드오프), không chỉ kết luận** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Kiến trúc nên được rà soát (review / 검토) bằng timeline, không chỉ bằng sơ đồ

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

Sau đó chèn thất bại (failure / 실패) vào từng điểm:

```text
kill process giữa T2 và T5
network timeout giữa T5 và T6
response mất giữa T6 và T7
database full ở T8
account logout giữa T4 và T5
```

Nếu thiết kế (design / 설계) không xác định được trạng thái (state / 상태) sau mỗi thất bại (failure / 실패), hiện thực (implementation / 구현) chưa đủ chặt.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 01 — kiến trúc (architecture / 아키텍처) Invariants, ranh giới (boundary / 경계) lập luận (reasoning / 추론) và quyền sở hữu trạng thái (state ownership / 상태 소유권)**, **16. kiến trúc (architecture / 아키텍처) quyết định (decision / 결정) bản ghi (record / 레코드) nên ghi sự đánh đổi (trade-off / 트레이드오프), không chỉ kết luận** gom các mảnh từ **15. Kiến trúc nên được rà soát (review / 검토) bằng timeline, không chỉ bằng sơ đồ** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **17. Khi nào không cần Repository, UseCase hoặc multi-module?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. kiến trúc (architecture / 아키텍처) quyết định (decision / 결정) bản ghi (record / 레코드) nên ghi sự đánh đổi (trade-off / 트레이드오프), không chỉ kết luận

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

ADR tốt giúp người mới hiểu lập luận (reasoning / 추론) thay vì chỉ kế thừa một công cụ (tool / 도구) choice.

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 01 — kiến trúc (architecture / 아키텍처) Invariants, ranh giới (boundary / 경계) lập luận (reasoning / 추론) và quyền sở hữu trạng thái (state ownership / 상태 소유권)**, **16. kiến trúc (architecture / 아키텍처) quyết định (decision / 결정) bản ghi (record / 레코드) nên ghi sự đánh đổi (trade-off / 트레이드오프), không chỉ kết luận** cho ta quy tắc; **17. Khi nào không cần Repository, UseCase hoặc multi-module?** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **18. rà soát (review / 검토) checklist theo bất biến (invariant / 불변식)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Khi nào không cần Repository, UseCase hoặc multi-module?

Kiến trúc (architecture / 아키텍처) trưởng thành không đồng nghĩa nhiều tầng (layer / 계층) nhất.

Nếu một tính năng (feature / 기능) local-only cực nhỏ:

```text
UI -> ViewModel -> DataStore-backed settings store
```

có thể đủ.

Thêm `UseCase -> Repository -> DataSource` cho một boolean preference có thể chỉ tăng indirection.

Nguyên tắc:

> thêm lớp trừu tượng (abstraction / 추상화) khi nó bảo vệ một ranh giới (boundary / 경계), bất biến (invariant / 불변식), reuse điểm (point / 지점) hoặc thay đổi (change / 변경) axis cụ thể.

Nếu không chỉ ra được điều đó, lớp trừu tượng (abstraction / 추상화) có thể chỉ là ceremony.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 01 — kiến trúc (architecture / 아키텍처) Invariants, ranh giới (boundary / 경계) lập luận (reasoning / 추론) và quyền sở hữu trạng thái (state ownership / 상태 소유권)**, **17. Khi nào không cần Repository, UseCase hoặc multi-module?** cho ta quy tắc; **18. rà soát (review / 검토) checklist theo bất biến (invariant / 불변식)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **19. Bài tập lập luận (reasoning / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. rà soát (review / 검토) checklist theo bất biến (invariant / 불변식)

Khi rà soát (review / 검토) một tính năng (feature / 기능) môi trường vận hành (production / 운영 환경), đừng bắt đầu bằng tên gói (package / 패키지). Hãy lần lượt trả lời:

| Câu hỏi | Điều cần xác định |
|---|---|
| nguồn chuẩn (source of truth / 정본) ở đâu? | Room, DataStore, backend hay trạng thái (state / 상태) holder |
| Ai được mutate? | một đơn vị sở hữu (owner / 오너) hay nhiều writer cạnh tranh |
| trạng thái (state / 상태) nào derived? | tránh persist duplicate truth |
| Mutation có durable không? | tiến trình (process / 프로세스) death có làm mất intent không |
| thao tác (operation / 연산) có idempotent không? | thử lại (retry / 재시도) có tạo duplicate tác động (effect / 효과) không |
| Snapshot có stale được không? | read-modify-write có race không |
| ranh giới (boundary / 경계) nào validate dữ liệu (data / 데이터)? | DTO/lĩnh vực (domain / 도메인)/thực thể (entity / 엔터티)/UI ánh xạ (mapping / 매핑) |
| thất bại (failure / 실패) có ambiguous kết quả (outcome / 결과) không? | hết thời gian chờ (timeout / 타임아웃) sau remote lần ghi nhận (commit / 커밋) |
| điều hướng (navigation / 내비게이션) reconstruct bằng gì? | stable id thay vì đối tượng (object / 객체) đồ thị (graph / 그래프) |
| bản phát hành (release / 릴리스) quay lui (rollback / 롤백) có đọc dữ liệu (data / 데이터) mới không? | lược đồ (schema / 스키마)/dữ liệu (data / 데이터) backward tính tương thích (compatibility / 호환성) |

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 01 — kiến trúc (architecture / 아키텍처) Invariants, ranh giới (boundary / 경계) lập luận (reasoning / 추론) và quyền sở hữu trạng thái (state ownership / 상태 소유권)**, **19. Bài tập lập luận (reasoning / 추론)** tiếp nhận điểm tựa từ **18. rà soát (review / 검토) checklist theo bất biến (invariant / 불변식)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Kết luận** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Bài tập lập luận (reasoning / 추론)

Hãy thiết kế tính năng (feature / 기능) “favorite article” với yêu cầu:

```text
- hoạt động offline,
- sync khi có mạng,
- user có thể login account khác,
- server hỗ trợ nhiều device,
- mutation có thể đến out-of-order,
- process có thể chết bất kỳ lúc nào.
```

Trước khi viết mã (code / 코드), tự định nghĩa:

1. nguồn chuẩn (source of truth / 정본) cục bộ (local / 로컬),
2. remote authority,
3. mutation định danh (identity / 식별자),
4. xung đột (conflict / 충돌) chính sách (policy / 정책),
5. logout cleanup chính sách (policy / 정책),
6. thử lại (retry / 재시도) ngữ nghĩa (semantics / 의미론),
7. stale phản hồi (response / 응답) protection,
8. khả năng quan sát (observability / 관측 가능성) fields.

Nếu chưa trả lời được tám điểm này, viết thêm lớp (class / 클래스) chưa giải quyết được phần khó nhất.

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 01 — kiến trúc (architecture / 아키텍처) Invariants, ranh giới (boundary / 경계) lập luận (reasoning / 추론) và quyền sở hữu trạng thái (state ownership / 상태 소유권)**, **20. Kết luận** gom các mảnh từ **19. Bài tập lập luận (reasoning / 추론)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 20. Kết luận

Kiến trúc (architecture / 아키텍처) ở mức (level / 수준) cấp cao (senior / 시니어) không còn là “dùng mẫu (pattern / 패턴) nào”. Nó là khả năng biến yêu cầu (requirement / 요구사항) thành bất biến (invariant / 불변식), biến bất biến (invariant / 불변식) thành quyền sở hữu (ownership / 소유권) và ranh giới (boundary / 경계), rồi chứng minh hệ thống vẫn đúng khi thực thi (execution / 실행) thứ tự (order / 순서) không còn lý tưởng.

Mô hình tư duy (mental model / 사고 모델) nên giữ:

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

Khi chuỗi này rõ, khung phần mềm (framework / 프레임워크) chỉ còn là công cụ hiện thực hóa quyết định kiến trúc.

> **Bàn giao:** Sau **20. Kết luận**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
