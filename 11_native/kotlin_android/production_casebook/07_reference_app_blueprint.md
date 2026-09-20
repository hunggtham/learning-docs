# Case 07 — Reference App Blueprint: Ghép Kotlin + Android thành một hệ thống Production

Chương cuối không đưa ra một template bắt buộc, mà trình bày một **blueprint reasoning** cho app tương đối lớn: có authentication, home feed, detail, bookmark, offline cache, edit offline, background sync, notification/deep link, analytics và release production. Mục tiêu là cho thấy các concept trong toàn bộ bộ note kết nối với nhau ở đâu.

## 1. Requirement giả định

Ứng dụng có các capability:

- user sign in bằng passkey/password/federated credential;
- home hiển thị article/feed từ cache và refresh network;
- article có bookmark offline;
- note của user có thể create/edit/delete offline;
- sync tự chạy khi có network;
- notification mở detail bằng deep link;
- tablet dùng list-detail layout;
- app có staged rollout, analytics, crash/ANR monitoring;
- backend có versioned REST API và token-based session.

Không phải app nào cũng cần tất cả. Blueprint cố tình đủ phức tạp để thể hiện boundary.

## 2. Module graph

Một cấu trúc có thể là:

```text
:app

:core:model
:core:common
:core:designsystem
:core:database
:core:network
:core:datastore
:core:analytics
:core:security
:core:testing

:feature:auth
:feature:feed
:feature:article
:feature:notes
:feature:settings

:sync
```

Trong app nhỏ, nhiều module trên có thể chỉ là package. Đừng module hóa để đạt “kiến trúc chuẩn”. Tách module khi cần ownership/build/API boundary.

## 3. Dependency direction

```text
feature UI
   ↓
repository/domain contracts
   ↓
data implementation
   ↓
network / database / datastore
```

Không để `core:database` import Composable. Không để `core:network` navigate. Không để feature A import internal ViewModel của feature B.

`:app` là composition root: kết nối DI graph, top-level navigation và application configuration.

## 4. Domain model

```kotlin
data class Article(
    val id: ArticleId,
    val title: String,
    val body: String,
    val bookmarked: Boolean,
    val publishedAt: Instant
)

@JvmInline
value class ArticleId(val value: String)
```

Value class có thể giảm nhầm ID giữa entity khác nhau mà runtime overhead thấp trong nhiều case. Tuy nhiên interop/serialization/boxing cần hiểu trước khi dùng public API rộng.

## 5. Network DTO

```kotlin
@Serializable
data class ArticleDto(
    val id: String,
    val title: String,
    val body: String,
    @SerialName("published_at") val publishedAt: String
)
```

DTO phản ánh server contract, không expose thẳng lên UI.

## 6. Database Entity

```kotlin
@Entity(tableName = "articles")
data class ArticleEntity(
    @PrimaryKey val id: String,
    val title: String,
    val body: String,
    val bookmarked: Boolean,
    val publishedAtEpochMillis: Long,
    val lastSyncedAtEpochMillis: Long?
)
```

Entity phản ánh local storage. Local-only metadata không cần xuất hiện trong DTO/domain nếu không có ý nghĩa ở đó.

## 7. Repository contract

```kotlin
interface ArticlesRepository {
    fun observeFeed(): Flow<List<Article>>
    fun observeArticle(id: ArticleId): Flow<Article?>
    suspend fun refreshFeed(): Result<Unit>
    suspend fun setBookmark(id: ArticleId, bookmarked: Boolean): Result<Unit>
}
```

Repository không expose `Retrofit.Response`, `Cursor`, `Room Entity` hoặc `MutableStateFlow` implementation nội bộ.

## 8. Source of truth

Feed dùng Room làm source of truth:

```text
network response
→ DTO validation/mapping
→ Room transaction
→ DAO Flow
→ repository domain model
→ ViewModel UiState
→ Compose
```

Network fail nhưng DB có cache: UI vẫn render cache + refresh error indicator.

## 9. UI state

```kotlin
sealed interface FeedUiState {
    data object Loading : FeedUiState

    data class Content(
        val articles: ImmutableList<ArticleUiModel>,
        val refreshing: Boolean,
        val message: UserMessage? = null
    ) : FeedUiState

    data class Empty(val canRetry: Boolean) : FeedUiState
    data class FatalError(val message: UserMessage) : FeedUiState
}
```

Không bắt buộc sealed class; data class tổng hợp cũng được. Chọn representation làm invalid state khó biểu diễn.

## 10. ViewModel

```kotlin
class FeedViewModel(
    repository: ArticlesRepository,
    private val refreshFeed: RefreshFeedUseCase
) : ViewModel() {

    val uiState: StateFlow<FeedUiState> = repository.observeFeed()
        .map { articles ->
            if (articles.isEmpty()) FeedUiState.Empty(canRetry = true)
            else FeedUiState.Content(
                articles = articles.map(Article::toUiModel).toImmutableList(),
                refreshing = false
            )
        }
        .stateIn(
            viewModelScope,
            SharingStarted.WhileSubscribed(5_000),
            FeedUiState.Loading
        )

    fun refresh() {
        viewModelScope.launch {
            refreshFeed()
        }
    }
}
```

Thực tế refresh state/error cần kết hợp rõ hơn; snippet chỉ minh họa direction.

## 11. Compose Route

```kotlin
@Composable
fun FeedRoute(
    viewModel: FeedViewModel,
    onArticleClick: (ArticleId) -> Unit
) {
    val state by viewModel.uiState.collectAsStateWithLifecycle()

    FeedScreen(
        state = state,
        onRefresh = viewModel::refresh,
        onArticleClick = onArticleClick
    )
}
```

`FeedScreen` pure hơn route và không giữ NavController/repository.

## 12. Navigation contract

```kotlin
@Serializable data object FeedRoute
@Serializable data class ArticleRoute(val articleId: String)
@Serializable data object SettingsRoute
```

Detail nhận ID, không nhận `Article` object.

## 13. Adaptive layout

Compact width:

```text
Feed destination → navigate Article destination
```

Expanded width:

```text
Feed list | Article detail pane
```

Business state vẫn là selected article ID. Presentation khác theo window configuration.

## 14. Session graph

```text
AppStart
  ↓
SessionState.Unknown
  ↓ restore
 ┌──────────────┐
SignedOut     SignedIn
  ↓              ↓
AuthGraph      MainGraph
```

Root UI observe SessionRepository. Protected repository vẫn dựa backend authorization; navigation chỉ điều khiển UX.

## 15. Token layer

```text
TokenStore
    ↑
TokenRefresher -- Mutex/single-flight
    ↑
Authenticated network client
    ↑
Repositories
```

Không feature nào tự implement refresh token.

## 16. Error hierarchy

```kotlin
sealed interface AppError {
    sealed interface Network : AppError {
        data object Offline : Network
        data object Timeout : Network
        data class Http(val code: Int) : Network
    }

    sealed interface Auth : AppError {
        data object SessionExpired : Auth
        data object PermissionDenied : Auth
    }

    sealed interface Data : AppError {
        data object NotFound : Data
        data class Corrupt(val reason: String) : Data
    }
}
```

Không nhất thiết một global hierarchy cho mọi app; quan trọng là error semantics không leak framework exception vào UI.

## 17. Notes offline-write model

Database:

```text
notes
pending_mutations
sync_metadata
```

Edit local transaction:

```text
update note
+ enqueue PendingUpdate(operationId)
COMMIT
```

Worker:

```text
network available
→ read oldest pending operations
→ send with idempotency key
→ apply server response/version
→ remove pending operation
→ repeat
```

Conflict 409 đi vào reconciliation policy, không retry mù.

## 18. WorkManager unique work

Sync có thể enqueue unique work để tránh nhiều sync worker duplicate:

```kotlin
workManager.enqueueUniqueWork(
    "notes-sync",
    ExistingWorkPolicy.KEEP,
    syncRequest
)
```

Policy KEEP/REPLACE/APPEND phải dựa semantics, không chọn ngẫu nhiên.

## 19. Background sync và session

Worker lấy session credential qua data/security layer. Nếu session signed out, worker dừng/mark operation chờ user tùy product. Logout cancel user-bound work.

Worker không giữ Activity/ViewModel reference.

## 20. Notification/deep link

Payload nên chứa minimal ID:

```json
{
  "type": "ARTICLE_UPDATED",
  "articleId": "a123"
}
```

Tap:

```text
validate notification payload
→ map to type-safe ArticleRoute
→ session gate nếu cần
→ repository load by ID
→ render latest data
```

Không nhét full article JSON vào notification để làm source of truth.

## 21. Settings

Theme/locale/simple preference nằm trong DataStore qua SettingsRepository:

```kotlin
interface SettingsRepository {
    val settings: Flow<UserSettings>
    suspend fun setTheme(mode: ThemeMode)
}
```

Compose root collect settings và apply theme. UI con không tự đọc DataStore.

## 22. Analytics boundary

```kotlin
interface Analytics {
    fun track(event: AnalyticsEvent)
}
```

Feature phát semantic event:

```kotlin
analytics.track(AnalyticsEvent.ArticleOpened(articleId))
```

Vendor SDK nằm implementation module. Nếu đổi vendor, feature không sửa hàng trăm call vendor-specific.

## 23. Sensitive analytics

Không gửi article body, token, password hoặc unnecessary PII. Event schema cần version/owner và privacy review.

## 24. DI graph

Application scope:

```text
Database
HTTP client
Repositories
SessionRepository
Analytics
WorkManager integration
```

Screen scope:

```text
ViewModel/state holder
```

Đừng singleton object chỉ vì “Hilt tiện”. Scope theo lifetime và mutable state.

## 25. Dispatcher injection

```kotlin
@Qualifier
annotation class IoDispatcher
```

Blocking/CPU work nhận dispatcher dependency để main-safe và testable.

Không truyền dispatcher vào mọi pure function; chỉ boundary concurrency cần.

## 26. Package-by-feature bên trong module

Nếu app chưa multi-module:

```text
com.example.app
├── core
│   ├── data
│   ├── network
│   ├── database
│   └── designsystem
└── feature
    ├── feed
    ├── article
    ├── auth
    └── notes
```

Package-by-layer toàn app (`activities/`, `viewmodels/`, `repositories/`) dễ khiến một feature bị rải khắp repository.

## 27. Test matrix

Feed:

- repository Room/network integration;
- ViewModel state mapping;
- Compose screen render states;
- deep link detail integration.

Auth:

- session restore;
- single-flight refresh;
- logout cleanup;
- root graph transition.

Notes:

- local write transaction;
- worker retry/idempotency;
- conflict;
- migration với pending queue.

Release:

- minified build smoke;
- Macrobenchmark startup/scroll;
- migration test all supported schema path.

## 28. CI pipeline

```text
PR
├─ format/static analysis
├─ unit tests
├─ Room migration tests
├─ network contract tests
├─ assemble minified testable build
└─ selected Compose/instrumented tests

main/release
├─ full device/API matrix selected
├─ macrobenchmark regression check
├─ signing protected job
├─ mapping/symbol archive
└─ internal/staged distribution
```

## 29. Build variant

```text
debug
staging
release
```

Staging có backend/test analytics riêng. Production secret không nằm source. Build config public endpoint/flag không được nhầm với secret.

## 30. Version compatibility

App N và N-1 có thể cùng tồn tại hàng tuần/tháng. Backend API phải có compatibility window. Database migration mới phải tính rollback. Pending serialized work phải đọc được sau upgrade.

Versioning là distributed-system concern, không chỉ `versionCode++`.

## 31. Observability map

Critical journey có correlation:

```text
cold start
session restore
feed cache shown
feed refresh
article open
note mutation queued
sync started
sync succeeded/failed
```

Metric giúp trả lời “lỗi ở screen, local DB, auth hay backend?” mà không log dữ liệu nhạy cảm.

## 32. Performance budget

Ví dụ team-defined budget:

```text
cold startup p95 < target
feed first cached content < target
scroll jank < threshold
sync CPU/network within budget
APK/AAB size delta reviewed
```

Con số cụ thể phụ thuộc product/device population; quan trọng là có budget và regression tracking.

## 33. Security map

Threat boundary:

```text
Untrusted inputs:
deep links, notification payload, network payload, external URI, user file

Sensitive assets:
session credential, user private data, cryptographic keys

Trusted enforcement:
backend authorization + platform security primitives
```

Client validation giúp safety/UX nhưng server vẫn enforce permission.

## 34. Privacy map

Tạo data inventory:

```text
data field
→ why collected
→ stored where
→ encrypted?
→ sent to whom
→ retention
→ delete path
→ user control
```

Privacy engineering trở thành architecture concern thay vì form điền trước release.

## 35. Feature flag map

Flag chỉ dùng khi có rollout/migration need rõ. Mỗi flag có owner, default, created date và removal condition.

```text
new_notes_sync_v2
owner: notes team
purpose: staged sync engine migration
remove after: 100% rollout + 2 stable releases
```

## 36. Incident response

Nếu sync V2 gây duplicate:

```text
metric alert
→ halt rollout
→ disable sync_v2 flag
→ inspect operationId/idempotency logs
→ patch backend/client
→ reconcile affected data
→ postmortem + invariant test
```

Architecture có feature flag/operation ID/observability khiến incident recovery khả thi hơn.

## 37. ADR

Decision quan trọng nên có Architecture Decision Record ngắn:

```text
Context
Decision
Alternatives
Consequences
Rollback/migration notes
```

Ví dụ “Room là source of truth cho Notes”, “Credential Manager cho sign-in”, “sync dùng durable mutation queue”. ADR giúp người mới hiểu tại sao code có hình dạng hiện tại.

## 38. Khi nào cần use case?

Dùng khi logic phức tạp/reuse/cross repository:

```kotlin
class PublishNoteUseCase(
    private val notesRepository: NotesRepository,
    private val quotaRepository: QuotaRepository,
    private val analytics: Analytics
)
```

Không tạo `GetThemeUseCase` chỉ để gọi một getter nếu không có policy/reuse.

## 39. Khi nào không cần repository mới?

Repository đại diện một domain/data concept, không phải mỗi endpoint. `UserRepository` có thể có profile/preferences remote operations; không cần `GetUserApiRepository`, `UpdateUserRepository` tách vô nghĩa.

## 40. Khi nào cần KMP?

Nếu sau này có iOS/shared platform, phần tốt để share là business/domain/data logic ổn định và platform-neutral. Không ép share Compose/UI, permission/device API chỉ để tăng “shared percentage”.

Public shared API phải nhỏ, cancellation/threading/serialization semantics rõ.

## 41. Kotlin/JVM awareness trong blueprint

Hot path cần nhớ allocation/boxing. Value class/generic có thể box. Reflection/generated code ảnh hưởng R8. `suspend` compile thành state machine. Lambda/capture có allocation tùy trường hợp.

Không micro-optimize sớm, nhưng khi profiler chỉ ra hotspot thì hiểu runtime giúp sửa đúng.

## 42. K2/compiler/plugin awareness

Kotlin compiler/plugin version phải compatible với AGP/Compose/serialization/KSP ecosystem. Upgrade compiler là dependency graph change, không chỉ sửa một số version.

Generated code directory/API là build contract; clean CI phải generate được từ source.

## 43. Review checklist cho feature mới

Một feature mới trước khi merge cần trả lời:

- state owner là ai?
- source of truth là gì?
- process death restore ra sao?
- error taxonomy?
- offline behavior?
- auth/permission boundary?
- test ở tầng nào?
- metric nào detect failure?
- release/rollback risk?
- public module API có cần không?

Không phải feature nào cũng có câu trả lời phức tạp, nhưng không nên “không biết”.

## 44. Mental model cuối cùng

Một production Android app có thể nhìn như các vòng lồng nhau:

```text
Platform lifecycle
└── Application/session lifetime
    └── Data sources + persistent state
        └── Repository/domain policies
            └── Navigation destination/state holder
                └── Compose/View UI state
```

Network, background work, security, testing và observability cắt ngang các vòng này nhưng mỗi thứ vẫn cần owner rõ.

## 45. Master notes cuối

Đến mức Master, mục tiêu không còn là nhớ nhiều API nhất. Mục tiêu là nhìn requirement và lập tức nghĩ tới **lifetime, ownership, source of truth, concurrency, failure, compatibility, security và operability**.

Một developer có thể viết Compose rất nhanh nhưng vẫn tạo app mong manh nếu state không restore, token refresh race, migration mất data hoặc release không rollback được. Ngược lại, khi các invariant trên rõ ràng, framework/API có thể thay đổi qua version mà architecture vẫn thích nghi được.

Đó là lý do blueprint này kết thúc bộ casebook: Kotlin syntax, coroutine, Room, Navigation, Compose, WorkManager, Gradle và security chỉ thật sự trở thành kỹ năng production khi chúng được nối thành một hệ thống có behavior dự đoán được dưới cả happy path lẫn failure path.
