# Trường hợp (case / 사례) 07 — tham chiếu (reference / 참조) App Blueprint: Ghép Kotlin + Android thành một hệ thống môi trường vận hành (production / 운영 환경)

> **Mạch đọc:** Đặt **trường hợp (case / 사례) 07 — tham chiếu (reference / 참조) App Blueprint: Ghép Kotlin + Android thành một hệ thống môi trường vận hành (production / 운영 환경)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. yêu cầu (requirement / 요구사항) giả định** sang **2. mô-đun (module / 모듈) đồ thị (graph / 그래프)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Chương cuối không đưa ra một template bắt buộc, mà trình bày một **blueprint lập luận (reasoning / 추론)** cho app tương đối lớn: có authentication, home feed, detail, bookmark, offline bộ nhớ đệm (cache / 캐시), edit offline, background sync, notification/deep link, analytics và bản phát hành (release / 릴리스) môi trường vận hành (production / 운영 환경). Mục tiêu là cho thấy các concept trong toàn bộ bộ ghi chú (note / 노트) kết nối với nhau ở đâu.

## 1. yêu cầu (requirement / 요구사항) giả định

Ứng dụng có các năng lực (capability / 역량):

- người dùng (user / 사용자) sign in bằng passkey/password/federated credential;
- home hiển thị article/feed từ bộ nhớ đệm (cache / 캐시) và refresh mạng (network / 네트워크);
- article có bookmark offline;
- ghi chú (note / 노트) của người dùng (user / 사용자) có thể create/edit/delete offline;
- sync tự chạy khi có mạng (network / 네트워크);
- notification mở detail bằng deep link;
- tablet dùng list-detail bố cục (layout / 레이아웃);
- app có staged rollout, analytics, crash/ANR monitoring;
- backend có versioned REST API và token-based session.

Không phải app nào cũng cần tất cả. Blueprint cố tình đủ phức tạp để thể hiện ranh giới (boundary / 경계).

## 2. mô-đun (module / 모듈) đồ thị (graph / 그래프)

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

Trong app nhỏ, nhiều mô-đun (module / 모듈) trên có thể chỉ là gói (package / 패키지). Đừng mô-đun (module / 모듈) hóa để đạt “kiến trúc chuẩn”. Tách mô-đun (module / 모듈) khi cần quyền sở hữu (ownership / 소유권)/bản dựng (build / 빌드)/API ranh giới (boundary / 경계).

## 3. phụ thuộc (dependency / 의존성) direction

```text
feature UI
   ↓
repository/domain contracts
   ↓
data implementation
   ↓
network / database / datastore
```

Không để `core:database` import Composable. Không để `core:network` navigate. Không để tính năng (feature / 기능) A import nội bộ (internal / 내부) ViewModel của tính năng (feature / 기능) B.

`:app` là composition gốc (root / 루트): kết nối DI đồ thị (graph / 그래프), top-level điều hướng (navigation / 내비게이션) và ứng dụng (application / 애플리케이션) cấu hình (configuration / 구성).

## 4. lĩnh vực (domain / 도메인) mô hình (model / 모델)

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

Giá trị (value / 값) lớp (class / 클래스) có thể giảm nhầm ID giữa thực thể (entity / 엔터티) khác nhau mà thời gian chạy (runtime / 런타임) overhead thấp trong nhiều trường hợp (case / 사례). Tuy nhiên interop/serialization/boxing cần hiểu trước khi dùng API công khai (public API / 공개 API) rộng.

## 5. mạng (network / 네트워크) DTO

```kotlin
@Serializable
data class ArticleDto(
    val id: String,
    val title: String,
    val body: String,
    @SerialName("published_at") val publishedAt: String
)
```

DTO phản ánh máy chủ (server / 서버) đặc tả hợp đồng (contract / 계약), không expose thẳng lên UI.

## 6. cơ sở dữ liệu (database / 데이터베이스) thực thể (entity / 엔터티)

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

Thực thể (entity / 엔터티) phản ánh cục bộ (local / 로컬) lưu trữ (storage / 저장소). Local-only siêu dữ liệu (metadata / 메타데이터) không cần xuất hiện trong DTO/lĩnh vực (domain / 도메인) nếu không có ý nghĩa ở đó.

## 7. Repository đặc tả hợp đồng (contract / 계약)

```kotlin
interface ArticlesRepository {
    fun observeFeed(): Flow<List<Article>>
    fun observeArticle(id: ArticleId): Flow<Article?>
    suspend fun refreshFeed(): Result<Unit>
    suspend fun setBookmark(id: ArticleId, bookmarked: Boolean): Result<Unit>
}
```

Repository không expose `Retrofit.Response`, `Cursor`, `Room Entity` hoặc `MutableStateFlow` hiện thực (implementation / 구현) nội bộ.

## 8. nguồn chuẩn (source of truth / 정본)

Feed dùng Room làm nguồn chuẩn (source of truth / 정본):

```text
network response
→ DTO validation/mapping
→ Room transaction
→ DAO Flow
→ repository domain model
→ ViewModel UiState
→ Compose
```

Mạng (network / 네트워크) thất bại (fail / 실패) nhưng DB có bộ nhớ đệm (cache / 캐시): UI vẫn kết xuất (render / 렌더링) bộ nhớ đệm (cache / 캐시) + refresh lỗi (error / 오류) indicator.

## 9. UI trạng thái (state / 상태)

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

Không bắt buộc sealed lớp (class / 클래스); dữ liệu (data / 데이터) lớp (class / 클래스) tổng hợp cũng được. Chọn biểu diễn (representation / 표현) làm invalid trạng thái (state / 상태) khó biểu diễn.

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

Thực tế refresh trạng thái (state / 상태)/lỗi (error / 오류) cần kết hợp rõ hơn; snippet chỉ minh họa direction.

## 11. Compose tuyến (route / 경로)

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

`FeedScreen` pure hơn tuyến (route / 경로) và không giữ NavController/repository.

## 12. điều hướng (navigation / 내비게이션) đặc tả hợp đồng (contract / 계약)

```kotlin
@Serializable data object FeedRoute
@Serializable data class ArticleRoute(val articleId: String)
@Serializable data object SettingsRoute
```

Detail nhận ID, không nhận `Article` đối tượng (object / 객체).

## 13. Adaptive bố cục (layout / 레이아웃)

Compact width:

```text
Feed destination → navigate Article destination
```

Expanded width:

```text
Feed list | Article detail pane
```

Nghiệp vụ (business / 비즈니스) trạng thái (state / 상태) vẫn là selected article ID. Presentation khác theo cửa sổ (window / 윈도우) cấu hình (configuration / 구성).

## 14. Session đồ thị (graph / 그래프)

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

Gốc (root / 루트) UI observe SessionRepository. Protected repository vẫn dựa backend authorization; điều hướng (navigation / 내비게이션) chỉ điều khiển UX.

## 15. đơn vị từ (token / 토큰) tầng (layer / 계층)

```text
TokenStore
    ↑
TokenRefresher -- Mutex/single-flight
    ↑
Authenticated network client
    ↑
Repositories
```

Không tính năng (feature / 기능) nào tự implement refresh đơn vị từ (token / 토큰).

## 16. lỗi (error / 오류) hierarchy

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

Không nhất thiết một toàn cục (global / 전역) hierarchy cho mọi app; quan trọng là lỗi (error / 오류) ngữ nghĩa (semantics / 의미론) không leak khung phần mềm (framework / 프레임워크) exception vào UI.

## 17. Notes offline-write mô hình (model / 모델)

Cơ sở dữ liệu (database / 데이터베이스):

```text
notes
pending_mutations
sync_metadata
```

Edit cục bộ (local / 로컬) giao dịch (transaction / 트랜잭션):

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

Xung đột (conflict / 충돌) 409 đi vào reconciliation chính sách (policy / 정책), không thử lại (retry / 재시도) mù.

## 18. WorkManager unique công việc (work / 작업)

Sync có thể enqueue unique công việc (work / 작업) để tránh nhiều sync worker duplicate:

```kotlin
workManager.enqueueUniqueWork(
    "notes-sync",
    ExistingWorkPolicy.KEEP,
    syncRequest
)
```

Chính sách (policy / 정책) KEEP/REPLACE/APPEND phải dựa ngữ nghĩa (semantics / 의미론), không chọn ngẫu nhiên.

## 19. Background sync và session

Worker lấy session credential qua dữ liệu (data / 데이터)/bảo mật (security / 보안) tầng (layer / 계층). Nếu session signed out, worker dừng/mark thao tác (operation / 연산) chờ người dùng (user / 사용자) tùy sản phẩm (product / 제품). Logout cancel user-bound công việc (work / 작업).

Worker không giữ Activity/ViewModel tham chiếu (reference / 참조).

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

Không nhét full article JSON vào notification để làm nguồn chuẩn (source of truth / 정본).

## 21. Settings

Theme/locale/simple preference nằm trong DataStore qua SettingsRepository:

```kotlin
interface SettingsRepository {
    val settings: Flow<UserSettings>
    suspend fun setTheme(mode: ThemeMode)
}
```

Compose gốc (root / 루트) collect settings và apply theme. UI con không tự đọc DataStore.

## 22. Analytics ranh giới (boundary / 경계)

```kotlin
interface Analytics {
    fun track(event: AnalyticsEvent)
}
```

Tính năng (feature / 기능) phát ngữ nghĩa (semantic / 의미적) sự kiện (event / 이벤트):

```kotlin
analytics.track(AnalyticsEvent.ArticleOpened(articleId))
```

Vendor SDK nằm hiện thực (implementation / 구현) mô-đun (module / 모듈). Nếu đổi vendor, tính năng (feature / 기능) không sửa hàng trăm lời gọi (call / 호출) vendor-specific.

## 23. Sensitive analytics

Không gửi article body, đơn vị từ (token / 토큰), password hoặc unnecessary PII. sự kiện (event / 이벤트) lược đồ (schema / 스키마) cần phiên bản (version / 버전)/đơn vị sở hữu (owner / 오너) và privacy rà soát (review / 검토).

## 24. DI đồ thị (graph / 그래프)

Ứng dụng (application / 애플리케이션) phạm vi (scope / 범위):

```text
Database
HTTP client
Repositories
SessionRepository
Analytics
WorkManager integration
```

Screen phạm vi (scope / 범위):

```text
ViewModel/state holder
```

Đừng singleton đối tượng (object / 객체) chỉ vì “Hilt tiện”. phạm vi (scope / 범위) theo thời gian tồn tại (lifetime / 수명) và mutable trạng thái (state / 상태).

## 25. Dispatcher injection

```kotlin
@Qualifier
annotation class IoDispatcher
```

Blocking/CPU công việc (work / 작업) nhận dispatcher phụ thuộc (dependency / 의존성) để main-safe và testable.

Không truyền dispatcher vào mọi pure hàm (function / 함수); chỉ ranh giới (boundary / 경계) tính đồng thời (concurrency / 동시성) cần.

## 26. Package-by-feature bên trong mô-đun (module / 모듈)

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

Package-by-layer toàn app (`activities/`, `viewmodels/`, `repositories/`) dễ khiến một tính năng (feature / 기능) bị rải khắp repository.

## 27. kiểm thử (test / 테스트) ma trận (matrix / 행렬)

Feed:

- repository Room/mạng (network / 네트워크) tích hợp (integration / 통합);
- ViewModel trạng thái (state / 상태) ánh xạ (mapping / 매핑);
- Compose screen kết xuất (render / 렌더링) states;
- deep link detail tích hợp (integration / 통합).

Auth:

- session restore;
- single-flight refresh;
- logout cleanup;
- gốc (root / 루트) đồ thị (graph / 그래프) chuyển tiếp (transition / 전이).

Notes:

- cục bộ (local / 로컬) ghi (write / 쓰기) giao dịch (transaction / 트랜잭션);
- worker thử lại (retry / 재시도)/idempotency;
- xung đột (conflict / 충돌);
- di chuyển (migration / 마이그레이션) với pending hàng đợi (queue / 큐).

Bản phát hành (release / 릴리스):

- minified bản dựng (build / 빌드) smoke;
- Macrobenchmark startup/scroll;
- di chuyển (migration / 마이그레이션) kiểm thử (test / 테스트) all supported lược đồ (schema / 스키마) đường dẫn (path / 경로).

## 28. CI chuỗi xử lý (pipeline / 파이프라인)

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

## 29. bản dựng (build / 빌드) variant

```text
debug
staging
release
```

Staging có backend/kiểm thử (test / 테스트) analytics riêng. môi trường vận hành (production / 운영 환경) secret không nằm nguồn (source / 소스). bản dựng (build / 빌드) cấu hình (config / 설정) công khai (public / 공개) endpoint/flag không được nhầm với secret.

## 30. phiên bản (version / 버전) tính tương thích (compatibility / 호환성)

App N và N-1 có thể cùng tồn tại hàng tuần/tháng. Backend API phải có tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우). cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션) mới phải tính quay lui (rollback / 롤백). Pending serialized công việc (work / 작업) phải đọc được sau upgrade.

Versioning là distributed-system concern, không chỉ `versionCode++`.

## 31. khả năng quan sát (observability / 관측 가능성) map

Trọng yếu (critical / 중요) journey có correlation:

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

Chỉ số (metric / 지표) giúp trả lời “lỗi ở screen, cục bộ (local / 로컬) DB, auth hay backend?” mà không log dữ liệu nhạy cảm.

## 32. hiệu năng (performance / 성능) ngân sách (budget / 예산)

Ví dụ team-defined ngân sách (budget / 예산):

```text
cold startup p95 < target
feed first cached content < target
scroll jank < threshold
sync CPU/network within budget
APK/AAB size delta reviewed
```

Con số cụ thể phụ thuộc sản phẩm (product / 제품)/thiết bị (device / 장치) population; quan trọng là có ngân sách (budget / 예산) và regression tracking.

## 33. bảo mật (security / 보안) map

Threat ranh giới (boundary / 경계):

```text
Untrusted inputs:
deep links, notification payload, network payload, external URI, user file

Sensitive assets:
session credential, user private data, cryptographic keys

Trusted enforcement:
backend authorization + platform security primitives
```

Máy khách (client / 클라이언트) kiểm tra hợp lệ (validation / 검증) giúp an toàn (safety / 안전)/UX nhưng máy chủ (server / 서버) vẫn enforce permission.

## 34. Privacy map

Tạo dữ liệu (data / 데이터) inventory:

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

Privacy kỹ thuật (engineering / 엔지니어링) trở thành kiến trúc (architecture / 아키텍처) concern thay vì form điền trước bản phát hành (release / 릴리스).

## 35. cờ tính năng (feature flag / 기능 플래그) map

Flag chỉ dùng khi có rollout/di chuyển (migration / 마이그레이션) need rõ. Mỗi flag có đơn vị sở hữu (owner / 오너), default, created date và removal điều kiện (condition / 조건).

```text
new_notes_sync_v2
owner: notes team
purpose: staged sync engine migration
remove after: 100% rollout + 2 stable releases
```

## 36. sự cố (incident / 인시던트) phản hồi (response / 응답)

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

Kiến trúc (architecture / 아키텍처) có cờ tính năng (feature flag / 기능 플래그)/thao tác (operation / 연산) ID/khả năng quan sát (observability / 관측 가능성) khiến sự cố (incident / 인시던트) khôi phục (recovery / 복구) khả thi hơn.

## 37. ADR

Quyết định (decision / 결정) quan trọng nên có kiến trúc (architecture / 아키텍처) quyết định (decision / 결정) bản ghi (record / 레코드) ngắn:

```text
Context
Decision
Alternatives
Consequences
Rollback/migration notes
```

Ví dụ “Room là nguồn chuẩn (source of truth / 정본) cho Notes”, “Credential Manager cho sign-in”, “sync dùng durable mutation hàng đợi (queue / 큐)”. ADR giúp người mới hiểu tại sao mã (code / 코드) có hình dạng hiện tại.

## 38. Khi nào cần use trường hợp (case / 사례)?

Dùng khi lô-gic (logic / 논리) phức tạp/reuse/cross repository:

```kotlin
class PublishNoteUseCase(
    private val notesRepository: NotesRepository,
    private val quotaRepository: QuotaRepository,
    private val analytics: Analytics
)
```

Không tạo `GetThemeUseCase` chỉ để gọi một getter nếu không có chính sách (policy / 정책)/reuse.

## 39. Khi nào không cần repository mới?

Repository đại diện một lĩnh vực (domain / 도메인)/dữ liệu (data / 데이터) concept, không phải mỗi endpoint. `UserRepository` có thể có profile/preferences remote operations; không cần `GetUserApiRepository`, `UpdateUserRepository` tách vô nghĩa.

## 40. Khi nào cần KMP?

Nếu sau này có iOS/dùng chung (shared / 공유) nền tảng (platform / 플랫폼), phần tốt để share là nghiệp vụ (business / 비즈니스)/lĩnh vực (domain / 도메인)/dữ liệu (data / 데이터) lô-gic (logic / 논리) ổn định và platform-neutral. Không ép share Compose/UI, permission/thiết bị (device / 장치) API chỉ để tăng “dùng chung (shared / 공유) percentage”.

Công khai (public / 공개) dùng chung (shared / 공유) API phải nhỏ, cancellation/threading/serialization ngữ nghĩa (semantics / 의미론) rõ.

## 41. Kotlin/JVM awareness trong blueprint

Đường xử lý nóng (hot path / 핫 패스) cần nhớ allocation/boxing. giá trị (value / 값) lớp (class / 클래스)/generic có thể box. Reflection/generated mã (code / 코드) ảnh hưởng R8. `suspend` compile thành máy trạng thái (state machine / 상태 머신). Lambda/capture có allocation tùy trường hợp.

Không micro-optimize sớm, nhưng khi profiler chỉ ra hotspot thì hiểu thời gian chạy (runtime / 런타임) giúp sửa đúng.

## 42. K2/trình biên dịch (compiler / 컴파일러)/plugin awareness

Kotlin trình biên dịch (compiler / 컴파일러)/plugin phiên bản (version / 버전) phải compatible với AGP/Compose/serialization/KSP ecosystem. Upgrade trình biên dịch (compiler / 컴파일러) là phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) thay đổi (change / 변경), không chỉ sửa một số phiên bản (version / 버전).

Generated mã (code / 코드) directory/API là bản dựng (build / 빌드) đặc tả hợp đồng (contract / 계약); clean CI phải generate được từ nguồn (source / 소스).

## 43. rà soát (review / 검토) checklist cho tính năng (feature / 기능) mới

Một tính năng (feature / 기능) mới trước khi merge cần trả lời:

- trạng thái (state / 상태) đơn vị sở hữu (owner / 오너) là ai?
- nguồn chuẩn (source of truth / 정본) là gì?
- tiến trình (process / 프로세스) death restore ra sao?
- lỗi (error / 오류) taxonomy?
- offline hành vi (behavior / 동작)?
- auth/permission ranh giới (boundary / 경계)?
- kiểm thử (test / 테스트) ở tầng nào?
- chỉ số (metric / 지표) nào detect thất bại (failure / 실패)?
- bản phát hành (release / 릴리스)/quay lui (rollback / 롤백) rủi ro (risk / 위험)?
- công khai (public / 공개) mô-đun (module / 모듈) API có cần không?

Không phải tính năng (feature / 기능) nào cũng có câu trả lời phức tạp, nhưng không nên “không biết”.

## 44. mô hình tư duy (mental model / 사고 모델) cuối cùng

Một môi trường vận hành (production / 운영 환경) Android app có thể nhìn như các vòng lồng nhau:

```text
Platform lifecycle
└── Application/session lifetime
    └── Data sources + persistent state
        └── Repository/domain policies
            └── Navigation destination/state holder
                └── Compose/View UI state
```

Mạng (network / 네트워크), background công việc (work / 작업), bảo mật (security / 보안), testing và khả năng quan sát (observability / 관측 가능성) cắt ngang các vòng này nhưng mỗi thứ vẫn cần đơn vị sở hữu (owner / 오너) rõ.

## 45. Master notes cuối

Đến mức Master, mục tiêu không còn là nhớ nhiều API nhất. Mục tiêu là nhìn yêu cầu (requirement / 요구사항) và lập tức nghĩ tới **thời gian tồn tại (lifetime / 수명), quyền sở hữu (ownership / 소유권), nguồn chuẩn (source of truth / 정본), tính đồng thời (concurrency / 동시성), thất bại (failure / 실패), tính tương thích (compatibility / 호환성), bảo mật (security / 보안) và operability**.

Một nhà phát triển (developer / 개발자) có thể viết Compose rất nhanh nhưng vẫn tạo app mong manh nếu trạng thái (state / 상태) không restore, đơn vị từ (token / 토큰) refresh race, di chuyển (migration / 마이그레이션) mất dữ liệu (data / 데이터) hoặc bản phát hành (release / 릴리스) không quay lui (rollback / 롤백) được. Ngược lại, khi các bất biến (invariant / 불변식) trên rõ ràng, khung phần mềm (framework / 프레임워크)/API có thể thay đổi qua phiên bản (version / 버전) mà kiến trúc (architecture / 아키텍처) vẫn thích nghi được.

Đó là lý do blueprint này kết thúc bộ casebook: Kotlin cú pháp (syntax / 문법), coroutine, Room, điều hướng (navigation / 내비게이션), Compose, WorkManager, Gradle và bảo mật (security / 보안) chỉ thật sự trở thành kỹ năng môi trường vận hành (production / 운영 환경) khi chúng được nối thành một hệ thống có hành vi (behavior / 동작) dự đoán được dưới cả happy đường dẫn (path / 경로) lẫn thất bại (failure / 실패) đường dẫn (path / 경로).

> **Bàn giao:** Sau **45. Master notes cuối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 architecture end to end](./01_architecture_end_to_end.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
