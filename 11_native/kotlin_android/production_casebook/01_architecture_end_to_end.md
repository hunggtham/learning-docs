# Case 01 — Android Architecture End-to-End

Một kiến trúc Android tốt không bắt đầu từ câu hỏi “dùng MVVM hay MVI?”, mà từ câu hỏi **dữ liệu nào tồn tại ở đâu, ai sở hữu nó, ai được thay đổi nó, và failure được xử lý ở boundary nào**. Khi trả lời đúng bốn câu này, tên pattern trở nên thứ yếu. Chương này xây một feature điển hình — danh sách bài viết có bookmark, refresh, offline cache và detail screen — để nối UI, ViewModel, repository, Room, network, coroutine/Flow, DI và module boundary thành một flow hoàn chỉnh.

## 1. Từ requirement sang state

Giả sử màn hình cần hiển thị danh sách article, cho phép refresh, bookmark, mở detail và vẫn đọc được dữ liệu cũ khi mất mạng. Trước khi viết class, ta phân loại state.

`Article` bản thân là application data. Trạng thái `isRefreshing`, filter đang chọn, search text và thông báo transient như snackbar là UI-related state. Article cache phải sống lâu hơn Activity và process, vì vậy không thể chỉ nằm trong ViewModel. Bookmark cũng là dữ liệu nghiệp vụ và cần được persist. Network response chỉ là một input để cập nhật source of truth, không nhất thiết là dữ liệu UI đọc trực tiếp.

Một `UiState` hợp lý có thể như sau:

```kotlin
data class ArticlesUiState(
    val items: List<ArticleUiModel> = emptyList(),
    val isLoading: Boolean = false,
    val isRefreshing: Boolean = false,
    val selectedCategory: Category = Category.All,
    val query: String = "",
    val error: UserMessage? = null
)
```

Điểm quan trọng không phải data class, mà là ý nghĩa: UI chỉ render snapshot hiện tại. UI không sở hữu repository, không gọi Retrofit trực tiếp và không tự quyết định cache policy.

## 2. Unidirectional Data Flow không đồng nghĩa một reducer khổng lồ

**Unidirectional Data Flow (UDF)** nghĩa là state đi xuống UI, event đi lên owner của state. Nó không bắt buộc mọi ứng dụng phải dùng Redux-style reducer.

```text
Data source -> Repository -> ViewModel -> UiState -> Compose UI
                                          ^          |
                                          |          v
                                      user events <- UI
```

Compose đọc `UiState`. User bấm bookmark, UI gửi event. ViewModel gọi operation tương ứng. Repository cập nhật local source of truth. Room phát Flow mới. ViewModel map nó thành UiState mới. Compose recomposition phần cần thiết.

Điều này tránh hai nguồn state cạnh tranh. Nếu UI tự toggle icon bookmark ngay trong local `remember`, còn database vẫn giữ giá trị cũ, sớm muộn hai trạng thái sẽ lệch nhau.

## 3. ViewModel là screen-level state holder, không phải service locator

Một ViewModel production thường làm ba việc: kết hợp các stream cần cho screen, nhận event, và chuyển domain/app data thành UI state. Nó không nên tự mở SQLite, tự tạo Retrofit client, giữ Activity context hoặc chứa toàn bộ business logic của ứng dụng.

```kotlin
class ArticlesViewModel(
    private val articlesRepository: ArticlesRepository,
    private val savedStateHandle: SavedStateHandle
) : ViewModel() {

    private val category = savedStateHandle.getStateFlow("category", Category.All)
    private val query = savedStateHandle.getStateFlow("query", "")

    val uiState: StateFlow<ArticlesUiState> = combine(
        articlesRepository.observeArticles(),
        category,
        query
    ) { articles, selectedCategory, searchQuery ->
        ArticlesUiState(
            items = articles
                .filter { selectedCategory == Category.All || it.category == selectedCategory }
                .filter { it.title.contains(searchQuery, ignoreCase = true) }
                .map(Article::toUiModel),
            selectedCategory = selectedCategory,
            query = searchQuery
        )
    }.stateIn(
        scope = viewModelScope,
        started = SharingStarted.WhileSubscribed(5_000),
        initialValue = ArticlesUiState(isLoading = true)
    )

    fun onCategoryChanged(value: Category) {
        savedStateHandle["category"] = value
    }

    fun onQueryChanged(value: String) {
        savedStateHandle["query"] = value
    }

    fun onBookmark(articleId: String) {
        viewModelScope.launch {
            articlesRepository.toggleBookmark(articleId)
        }
    }
}
```

Ở đây `SavedStateHandle` được dùng cho state nhỏ cần phục hồi sau process recreation như filter/query. Không nên nhét một danh sách hàng nghìn object vào SavedStateHandle; dữ liệu lớn phải khôi phục lại từ source of truth.

## 4. Repository là data contract, không chỉ là wrapper của Retrofit

Repository tồn tại để cung cấp một abstraction về **application data**. Nếu repository chỉ có `return api.getX()`, nó chưa mua được nhiều giá trị. Khi app có local + remote, repository trở thành nơi giải quyết source of truth, refresh, conflict và mapping.

```kotlin
interface ArticlesRepository {
    fun observeArticles(): Flow<List<Article>>
    suspend fun refresh()
    suspend fun toggleBookmark(articleId: String)
}
```

Implementation có thể dùng Room làm source of truth:

```kotlin
class OfflineFirstArticlesRepository(
    private val dao: ArticleDao,
    private val api: ArticlesApi,
    private val ioDispatcher: CoroutineDispatcher
) : ArticlesRepository {

    override fun observeArticles(): Flow<List<Article>> =
        dao.observeAll().map { entities -> entities.map(ArticleEntity::toDomain) }

    override suspend fun refresh() = withContext(ioDispatcher) {
        val remote = api.getArticles()
        dao.replaceRemoteSnapshot(remote.map(ArticleDto::toEntityPreservingLocalFlags))
    }

    override suspend fun toggleBookmark(articleId: String) {
        dao.toggleBookmark(articleId)
    }
}
```

UI không biết dữ liệu đang tới từ DB hay network. Repository đảm bảo sau refresh, database được cập nhật và Flow tự emit snapshot mới.

## 5. DTO, Entity, Domain model và UI model không phải lúc nào cũng cần bốn class

Tách model theo boundary giúp chống coupling nhưng over-modeling cũng có cost. Nguyên tắc hợp lý là tách khi hai layer có **lý do thay đổi khác nhau**.

`ArticleDto` phản ánh wire format của server. `ArticleEntity` phản ánh schema local. `Article` phản ánh language của app. `ArticleUiModel` phản ánh presentation. Nếu backend field đổi từ `published_at` sang object khác, domain/UI không nên bị kéo theo. Nếu database thêm metadata sync nội bộ, domain cũng không nhất thiết thấy metadata đó.

Trong app nhỏ, Entity và Domain có thể tạm dùng chung nếu contract thực sự đồng nhất. Senior engineering không phải tạo nhiều class nhất; nó là biết coupling nào đáng trả chi phí mapping.

## 6. Domain layer là optional, không phải nghi thức

Use case hữu ích khi business operation được dùng ở nhiều state holder hoặc có logic đủ phức tạp để ViewModel không nên chứa.

```kotlin
class ToggleBookmarkUseCase(
    private val repository: ArticlesRepository,
    private val analytics: Analytics
) {
    suspend operator fun invoke(articleId: String) {
        repository.toggleBookmark(articleId)
        analytics.logBookmarkChanged(articleId)
    }
}
```

Nếu `GetArticleUseCase` chỉ gọi `repository.getArticle(id)` và không tạo boundary, reuse hay policy nào, thêm class đó có thể chỉ tăng ceremony. Hãy dùng domain layer khi nó giảm complexity thật.

## 7. Main-safe contract

Public suspend function của repository/use case nên đủ an toàn để caller gọi từ main thread. Caller không nên phải nhớ “method này cần Dispatchers.IO”. Data layer chịu trách nhiệm chuyển dispatcher cho blocking work.

```kotlin
suspend fun parseLargePayload(bytes: ByteArray): Parsed =
    withContext(ioDispatcher) {
        parser.parse(bytes)
    }
```

Điều này biến threading thành implementation detail và làm test dễ hơn vì dispatcher có thể inject.

## 8. Error model phải có vocabulary

Một app production không nên ném mọi thứ thành string “Something went wrong”. Ta cần phân biệt ít nhất transport failure, protocol failure và domain failure.

```kotlin
sealed interface DataError {
    data object Offline : DataError
    data object Timeout : DataError
    data class Http(val code: Int) : DataError
    data object Unauthorized : DataError
    data class Validation(val field: String) : DataError
    data class Unknown(val cause: Throwable) : DataError
}
```

Tầng UI map error thành message/action phù hợp. `401` có thể trigger session recovery; validation error có thể focus field; offline có thể vẫn render cache cũ. Không nên để Retrofit exception type lan tới Composable.

## 9. Loading không phải boolean duy nhất

Một screen có thể vừa có cached content vừa refresh. Nếu `isLoading=true` khiến UI thay toàn bộ list bằng spinner, UX sẽ nhấp nháy vô ích. Vì vậy thường nên phân biệt **initial load**, **refresh**, **pagination load** và **mutation in progress**.

```kotlin
data class LoadState(
    val initial: Boolean = false,
    val refreshing: Boolean = false,
    val appending: Boolean = false
)
```

State model tốt làm UI behavior chính xác hơn mà không cần nhiều `if` rải rác.

## 10. One-off event và durable state

Navigation, snackbar và permission request thường được gọi là event, nhưng cần phân loại cẩn thận. Nếu event quan trọng mà bị mất khi collector tạm inactive thì design sai.

State có ý nghĩa lâu dài nên nằm trong UiState. Ví dụ “payment completed” có thể là state của transaction, không phải chỉ là một Channel event. Snackbar “Đã copy” có thể transient. Navigation sau submit nên được thiết kế sao cho không navigate hai lần sau recreation; thường state machine hoặc consumed state rõ ràng an toàn hơn một event bus vô danh.

## 11. Module boundary theo capability, không theo tên layer một cách máy móc

Một codebase lớn có thể có:

```text
:app
:core:model
:core:database
:core:network
:core:designsystem
:core:common
:feature:articles:api
:feature:articles:impl
:feature:profile:api
:feature:profile:impl
```

Không có cấu trúc duy nhất đúng. Điều quan trọng là graph dependency có hướng. `core:database` không phụ thuộc UI. Feature không import implementation nội bộ của feature khác. Public API nhỏ giúp build cache và ownership tốt hơn.

Quá nhiều module trong app nhỏ làm Gradle/configuration và navigation phức tạp. Modularization chỉ đáng làm khi có mục tiêu như build isolation, ownership, optional delivery, reusable boundary hoặc giảm accidental coupling.

## 12. DI graph phải phản ánh lifetime

Dependency injection không chỉ để tránh `new`. Scope phải khớp lifetime. Singleton repository có thể giữ connection/cache toàn app. Screen state holder không nên thành singleton. Object giữ Activity không thể sống application scope.

Các câu hỏi cần hỏi với mỗi dependency là: ai tạo nó, sống bao lâu, có mutable state không, có thread-safety requirement không, và dispose ở đâu.

## 13. Compose screen boundary

Một pattern dễ test là tách route-level composable và pure content composable:

```kotlin
@Composable
fun ArticlesRoute(
    viewModel: ArticlesViewModel,
    onOpenArticle: (String) -> Unit
) {
    val state by viewModel.uiState.collectAsStateWithLifecycle()

    ArticlesScreen(
        state = state,
        onBookmark = viewModel::onBookmark,
        onOpenArticle = onOpenArticle
    )
}

@Composable
fun ArticlesScreen(
    state: ArticlesUiState,
    onBookmark: (String) -> Unit,
    onOpenArticle: (String) -> Unit
) {
    // Pure rendering + event forwarding
}
```

`ArticlesScreen` không cần biết Hilt, Navigation Controller hoặc repository. Vì vậy preview, screenshot test và Compose UI test đơn giản hơn.

## 14. Architecture test bằng failure scenario

Đừng chỉ review class diagram. Hãy mô phỏng failure:

- xoay màn hình giữa lúc refresh;
- process bị kill khi đang ở detail;
- API trả 500 nhưng cache có dữ liệu;
- user bấm bookmark liên tục;
- network request finish sau khi screen đã rời back stack;
- database migration chạy trên dữ liệu thật của version cũ;
- server thêm field hoặc trả unknown enum value;
- duplicate deep link mở cùng entity hai lần.

Nếu architecture không trả lời được behavior mong muốn trong các tình huống này, sơ đồ đẹp không có nhiều giá trị.

## 15. Một end-to-end read path

Khi app khởi động, Room emit cached articles. Repository map Entity thành domain model. ViewModel combine data với filter/query. UI render ngay. Một refresh coroutine gọi network, validate DTO, transactionally update database. Database emit snapshot mới. UI update mà không cần imperative callback.

Khi user bookmark, operation cập nhật local database trước nếu product muốn optimistic UX. Nếu bookmark phải sync server, operation tạo pending mutation hoặc gửi request. Nếu server fail, policy quyết định rollback, retry hoặc giữ pending state. Policy này thuộc data/domain logic, không nên nằm trong icon click handler.

## 16. Senior notes

Architecture càng lớn càng cần **explicit contracts** hơn framework. Hãy document source of truth, state ownership, public module API, error vocabulary và sync semantics. Đừng để người mới phải đọc 30 class mới hiểu “bookmark có offline không”.

Giữ ViewModel nhỏ bằng cách tách reusable business operation, nhưng không biến mọi method thành use case. Giữ repository giàu ý nghĩa data, không để nó thành một folder chứa Retrofit wrapper. Dùng Flow cho observable state, nhưng không biến tất cả function thành Flow nếu chỉ cần một one-shot result. Dùng Compose state đúng lifetime, không đưa persistent application data vào `remember`.

Một architecture tốt khiến path dữ liệu dễ kể bằng lời: **server/local source → repository → domain policy → state holder → immutable UI state → UI event quay lại owner**. Nếu phải dùng nhiều ngoại lệ để mô tả path đó, boundary đang có vấn đề.
