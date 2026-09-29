# Trường hợp (case / 사례) 01 — Android kiến trúc (architecture / 아키텍처) End-to-End

> **Mạch đọc:** Đặt **trường hợp (case / 사례) 01 — Android kiến trúc (architecture / 아키텍처) End-to-End** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Từ yêu cầu (requirement / 요구사항) sang trạng thái (state / 상태)** sang **2. Unidirectional luồng dữ liệu (data flow / 데이터 흐름) không đồng nghĩa một reducer khổng lồ**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Một kiến trúc Android tốt không bắt đầu từ câu hỏi “dùng MVVM hay MVI?”, mà từ câu hỏi **dữ liệu nào tồn tại ở đâu, ai sở hữu nó, ai được thay đổi nó, và thất bại (failure / 실패) được xử lý ở ranh giới (boundary / 경계) nào**. Khi trả lời đúng bốn câu này, tên mẫu (pattern / 패턴) trở nên thứ yếu. Chương này xây một tính năng (feature / 기능) điển hình — danh sách bài viết có bookmark, refresh, offline bộ nhớ đệm (cache / 캐시) và detail screen — để nối UI, ViewModel, repository, Room, mạng (network / 네트워크), coroutine/luồng (flow / 흐름), DI và ranh giới mô-đun (module boundary / 모듈 경계) thành một luồng (flow / 흐름) hoàn chỉnh.

## 1. Từ yêu cầu (requirement / 요구사항) sang trạng thái (state / 상태)

Giả sử màn hình cần hiển thị danh sách article, cho phép refresh, bookmark, mở detail và vẫn đọc được dữ liệu cũ khi mất mạng. Trước khi viết lớp (class / 클래스), ta phân loại trạng thái (state / 상태).

`Article` bản thân là ứng dụng (application / 애플리케이션) dữ liệu (data / 데이터). Trạng thái `isRefreshing`, filter đang chọn, tìm kiếm (search / 검색) văn bản (text / 텍스트) và thông báo transient như snackbar là UI-related trạng thái (state / 상태). Article bộ nhớ đệm (cache / 캐시) phải sống lâu hơn Activity và tiến trình (process / 프로세스), vì vậy không thể chỉ nằm trong ViewModel. Bookmark cũng là dữ liệu nghiệp vụ và cần được persist. mạng (network / 네트워크) phản hồi (response / 응답) chỉ là một đầu vào (input / 입력) để cập nhật nguồn chuẩn (source of truth / 정본), không nhất thiết là dữ liệu UI đọc trực tiếp.

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

Điểm quan trọng không phải dữ liệu (data / 데이터) lớp (class / 클래스), mà là ý nghĩa: UI chỉ kết xuất (render / 렌더링) snapshot hiện tại. UI không sở hữu repository, không gọi Retrofit trực tiếp và không tự quyết định bộ nhớ đệm (cache / 캐시) chính sách (policy / 정책).

## 2. Unidirectional luồng dữ liệu (data flow / 데이터 흐름) không đồng nghĩa một reducer khổng lồ

**Unidirectional luồng dữ liệu (data flow / 데이터 흐름) (UDF)** nghĩa là trạng thái (state / 상태) đi xuống UI, sự kiện (event / 이벤트) đi lên đơn vị sở hữu (owner / 오너) của trạng thái (state / 상태). Nó không bắt buộc mọi ứng dụng phải dùng Redux-style reducer.

```text
Data source -> Repository -> ViewModel -> UiState -> Compose UI
                                          ^          |
                                          |          v
                                      user events <- UI
```

Compose đọc `UiState`. người dùng (user / 사용자) bấm bookmark, UI gửi sự kiện (event / 이벤트). ViewModel gọi thao tác (operation / 연산) tương ứng. Repository cập nhật cục bộ (local / 로컬) nguồn chuẩn (source of truth / 정본). Room phát luồng (flow / 흐름) mới. ViewModel map nó thành UiState mới. Compose recomposition phần cần thiết.

Điều này tránh hai nguồn trạng thái (state / 상태) cạnh tranh. Nếu UI tự toggle icon bookmark ngay trong cục bộ (local / 로컬) `remember`, còn cơ sở dữ liệu (database / 데이터베이스) vẫn giữ giá trị cũ, sớm muộn hai trạng thái sẽ lệch nhau.

## 3. ViewModel là screen-level trạng thái (state / 상태) holder, không phải dịch vụ (service / 서비스) locator

Một ViewModel môi trường vận hành (production / 운영 환경) thường làm ba việc: kết hợp các stream cần cho screen, nhận sự kiện (event / 이벤트), và chuyển lĩnh vực (domain / 도메인)/app dữ liệu (data / 데이터) thành UI trạng thái (state / 상태). Nó không nên tự mở SQLite, tự tạo Retrofit máy khách (client / 클라이언트), giữ Activity ngữ cảnh (context / 맥락) hoặc chứa toàn bộ lô-gic nghiệp vụ (business logic / 비즈니스 로직) của ứng dụng.

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

Ở đây `SavedStateHandle` được dùng cho trạng thái (state / 상태) nhỏ cần phục hồi sau tiến trình (process / 프로세스) recreation như filter/truy vấn (query / 쿼리). Không nên nhét một danh sách hàng nghìn đối tượng (object / 객체) vào SavedStateHandle; dữ liệu lớn phải khôi phục lại từ nguồn chuẩn (source of truth / 정본).

## 4. Repository là dữ liệu (data / 데이터) đặc tả hợp đồng (contract / 계약), không chỉ là wrapper của Retrofit

Repository tồn tại để cung cấp một lớp trừu tượng (abstraction / 추상화) về **ứng dụng (application / 애플리케이션) dữ liệu (data / 데이터)**. Nếu repository chỉ có `return api.getX()`, nó chưa mua được nhiều giá trị. Khi app có cục bộ (local / 로컬) + remote, repository trở thành nơi giải quyết nguồn chuẩn (source of truth / 정본), refresh, xung đột (conflict / 충돌) và ánh xạ (mapping / 매핑).

```kotlin
interface ArticlesRepository {
    fun observeArticles(): Flow<List<Article>>
    suspend fun refresh()
    suspend fun toggleBookmark(articleId: String)
}
```

Hiện thực (implementation / 구현) có thể dùng Room làm nguồn chuẩn (source of truth / 정본):

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

UI không biết dữ liệu đang tới từ DB hay mạng (network / 네트워크). Repository đảm bảo sau refresh, cơ sở dữ liệu (database / 데이터베이스) được cập nhật và luồng (flow / 흐름) tự emit snapshot mới.

## 5. DTO, thực thể (entity / 엔터티), lĩnh vực (domain / 도메인) mô hình (model / 모델) và UI mô hình (model / 모델) không phải lúc nào cũng cần bốn lớp (class / 클래스)

Tách mô hình (model / 모델) theo ranh giới (boundary / 경계) giúp chống coupling nhưng over-modeling cũng có chi phí (cost / 비용). Nguyên tắc hợp lý là tách khi hai tầng (layer / 계층) có **lý do thay đổi khác nhau**.

`ArticleDto` phản ánh wire format của máy chủ (server / 서버). `ArticleEntity` phản ánh lược đồ (schema / 스키마) cục bộ (local / 로컬). `Article` phản ánh ngôn ngữ (language / 언어) của app. `ArticleUiModel` phản ánh presentation. Nếu backend trường dữ liệu (field / 필드) đổi từ `published_at` sang đối tượng (object / 객체) khác, lĩnh vực (domain / 도메인)/UI không nên bị kéo theo. Nếu cơ sở dữ liệu (database / 데이터베이스) thêm siêu dữ liệu (metadata / 메타데이터) sync nội bộ, lĩnh vực (domain / 도메인) cũng không nhất thiết thấy siêu dữ liệu (metadata / 메타데이터) đó.

Trong app nhỏ, thực thể (entity / 엔터티) và lĩnh vực (domain / 도메인) có thể tạm dùng chung nếu đặc tả hợp đồng (contract / 계약) thực sự đồng nhất. cấp cao (senior / 시니어) kỹ thuật (engineering / 엔지니어링) không phải tạo nhiều lớp (class / 클래스) nhất; nó là biết coupling nào đáng trả chi phí ánh xạ (mapping / 매핑).

## 6. lĩnh vực (domain / 도메인) tầng (layer / 계층) là optional, không phải nghi thức

Use trường hợp (case / 사례) hữu ích khi nghiệp vụ (business / 비즈니스) thao tác (operation / 연산) được dùng ở nhiều trạng thái (state / 상태) holder hoặc có lô-gic (logic / 논리) đủ phức tạp để ViewModel không nên chứa.

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

Nếu `GetArticleUseCase` chỉ gọi `repository.getArticle(id)` và không tạo ranh giới (boundary / 경계), reuse hay chính sách (policy / 정책) nào, thêm lớp (class / 클래스) đó có thể chỉ tăng ceremony. Hãy dùng lĩnh vực (domain / 도메인) tầng (layer / 계층) khi nó giảm độ phức tạp (complexity / 복잡도) thật.

## 7. Main-safe đặc tả hợp đồng (contract / 계약)

Công khai (public / 공개) suspend hàm (function / 함수) của repository/use trường hợp (case / 사례) nên đủ an toàn để caller gọi từ main luồng thực thi (thread / 스레드). Caller không nên phải nhớ “phương thức (method / 메서드) này cần Dispatchers.IO”. dữ liệu (data / 데이터) tầng (layer / 계층) chịu trách nhiệm chuyển dispatcher cho blocking công việc (work / 작업).

```kotlin
suspend fun parseLargePayload(bytes: ByteArray): Parsed =
    withContext(ioDispatcher) {
        parser.parse(bytes)
    }
```

Điều này biến threading thành hiện thực (implementation / 구현) detail và làm kiểm thử (test / 테스트) dễ hơn vì dispatcher có thể inject.

## 8. lỗi (error / 오류) mô hình (model / 모델) phải có vocabulary

Một app môi trường vận hành (production / 운영 환경) không nên ném mọi thứ thành string “Something went wrong”. Ta cần phân biệt ít nhất vận chuyển (transport / 전송) thất bại (failure / 실패), giao thức (protocol / 프로토콜) thất bại (failure / 실패) và lĩnh vực (domain / 도메인) thất bại (failure / 실패).

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

Tầng UI map lỗi (error / 오류) thành message/hành động (action / 동작) phù hợp. `401` có thể trigger session khôi phục (recovery / 복구); kiểm tra hợp lệ (validation / 검증) lỗi (error / 오류) có thể focus trường dữ liệu (field / 필드); offline có thể vẫn kết xuất (render / 렌더링) bộ nhớ đệm (cache / 캐시) cũ. Không nên để Retrofit exception kiểu (type / 타입) lan tới Composable.

## 9. Loading không phải boolean duy nhất

Một screen có thể vừa có cached content vừa refresh. Nếu `isLoading=true` khiến UI thay toàn bộ danh sách (list / 목록) bằng spinner, UX sẽ nhấp nháy vô ích. Vì vậy thường nên phân biệt **initial tải (load / 로드)**, **refresh**, **pagination tải (load / 로드)** và **mutation in progress**.

```kotlin
data class LoadState(
    val initial: Boolean = false,
    val refreshing: Boolean = false,
    val appending: Boolean = false
)
```

Trạng thái (state / 상태) mô hình (model / 모델) tốt làm UI hành vi (behavior / 동작) chính xác hơn mà không cần nhiều `if` rải rác.

## 10. One-off sự kiện (event / 이벤트) và durable trạng thái (state / 상태)

Điều hướng (navigation / 내비게이션), snackbar và permission yêu cầu (request / 요청) thường được gọi là sự kiện (event / 이벤트), nhưng cần phân loại cẩn thận. Nếu sự kiện (event / 이벤트) quan trọng mà bị mất khi collector tạm inactive thì thiết kế (design / 설계) sai.

Trạng thái (state / 상태) có ý nghĩa lâu dài nên nằm trong UiState. Ví dụ “payment completed” có thể là trạng thái (state / 상태) của giao dịch (transaction / 트랜잭션), không phải chỉ là một Channel sự kiện (event / 이벤트). Snackbar “Đã bản sao (copy / 복사)” có thể transient. điều hướng (navigation / 내비게이션) sau submit nên được thiết kế sao cho không navigate hai lần sau recreation; thường máy trạng thái (state machine / 상태 머신) hoặc consumed trạng thái (state / 상태) rõ ràng an toàn hơn một sự kiện (event / 이벤트) bus vô danh.

## 11. ranh giới mô-đun (module boundary / 모듈 경계) theo năng lực (capability / 역량), không theo tên tầng (layer / 계층) một cách máy móc

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

Không có cấu trúc duy nhất đúng. Điều quan trọng là đồ thị (graph / 그래프) phụ thuộc (dependency / 의존성) có hướng. `core:database` không phụ thuộc UI. tính năng (feature / 기능) không import hiện thực (implementation / 구현) nội bộ của tính năng (feature / 기능) khác. API công khai (public API / 공개 API) nhỏ giúp bản dựng (build / 빌드) bộ nhớ đệm (cache / 캐시) và quyền sở hữu (ownership / 소유권) tốt hơn.

Quá nhiều mô-đun (module / 모듈) trong app nhỏ làm Gradle/cấu hình (configuration / 구성) và điều hướng (navigation / 내비게이션) phức tạp. Modularization chỉ đáng làm khi có mục tiêu như bản dựng (build / 빌드) isolation, quyền sở hữu (ownership / 소유권), optional delivery, reusable ranh giới (boundary / 경계) hoặc giảm accidental coupling.

## 12. DI đồ thị (graph / 그래프) phải phản ánh thời gian tồn tại (lifetime / 수명)

Phụ thuộc (dependency / 의존성) injection không chỉ để tránh `new`. phạm vi (scope / 범위) phải khớp thời gian tồn tại (lifetime / 수명). Singleton repository có thể giữ liên kết (connection / 연결)/bộ nhớ đệm (cache / 캐시) toàn app. Screen trạng thái (state / 상태) holder không nên thành singleton. đối tượng (object / 객체) giữ Activity không thể sống ứng dụng (application / 애플리케이션) phạm vi (scope / 범위).

Các câu hỏi cần hỏi với mỗi phụ thuộc (dependency / 의존성) là: ai tạo nó, sống bao lâu, có mutable trạng thái (state / 상태) không, có thread-safety yêu cầu (requirement / 요구사항) không, và dispose ở đâu.

## 13. Compose screen ranh giới (boundary / 경계)

Một mẫu (pattern / 패턴) dễ kiểm thử (test / 테스트) là tách route-level composable và pure content composable:

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

`ArticlesScreen` không cần biết Hilt, điều hướng (navigation / 내비게이션) Controller hoặc repository. Vì vậy preview, screenshot kiểm thử (test / 테스트) và Compose UI kiểm thử (test / 테스트) đơn giản hơn.

## 14. kiến trúc (architecture / 아키텍처) kiểm thử (test / 테스트) bằng thất bại (failure / 실패) scenario

Đừng chỉ rà soát (review / 검토) lớp (class / 클래스) diagram. Hãy mô phỏng thất bại (failure / 실패):

- xoay màn hình giữa lúc refresh;
- tiến trình (process / 프로세스) bị kill khi đang ở detail;
- API trả 500 nhưng bộ nhớ đệm (cache / 캐시) có dữ liệu;
- người dùng (user / 사용자) bấm bookmark liên tục;
- mạng (network / 네트워크) yêu cầu (request / 요청) finish sau khi screen đã rời back ngăn xếp (stack / 스택);
- cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션) chạy trên dữ liệu thật của phiên bản (version / 버전) cũ;
- máy chủ (server / 서버) thêm trường dữ liệu (field / 필드) hoặc trả unknown enum giá trị (value / 값);
- duplicate deep link mở cùng thực thể (entity / 엔터티) hai lần.

Nếu kiến trúc (architecture / 아키텍처) không trả lời được hành vi (behavior / 동작) mong muốn trong các tình huống này, sơ đồ đẹp không có nhiều giá trị.

## 15. Một end-to-end read đường dẫn (path / 경로)

Khi app khởi động, Room emit cached articles. Repository map thực thể (entity / 엔터티) thành lĩnh vực (domain / 도메인) mô hình (model / 모델). ViewModel combine dữ liệu (data / 데이터) với filter/truy vấn (query / 쿼리). UI kết xuất (render / 렌더링) ngay. Một refresh coroutine gọi mạng (network / 네트워크), validate DTO, transactionally cập nhật (update / 업데이트) cơ sở dữ liệu (database / 데이터베이스). cơ sở dữ liệu (database / 데이터베이스) emit snapshot mới. UI cập nhật (update / 업데이트) mà không cần imperative callback.

Khi người dùng (user / 사용자) bookmark, thao tác (operation / 연산) cập nhật cục bộ (local / 로컬) cơ sở dữ liệu (database / 데이터베이스) trước nếu sản phẩm (product / 제품) muốn optimistic UX. Nếu bookmark phải sync máy chủ (server / 서버), thao tác (operation / 연산) tạo pending mutation hoặc gửi yêu cầu (request / 요청). Nếu máy chủ (server / 서버) thất bại (fail / 실패), chính sách (policy / 정책) quyết định quay lui (rollback / 롤백), thử lại (retry / 재시도) hoặc giữ pending trạng thái (state / 상태). chính sách (policy / 정책) này thuộc dữ liệu (data / 데이터)/lĩnh vực (domain / 도메인) lô-gic (logic / 논리), không nên nằm trong icon click handler.

## 16. cấp cao (senior / 시니어) notes

Kiến trúc (architecture / 아키텍처) càng lớn càng cần **tường minh (explicit / 명시적) contracts** hơn khung phần mềm (framework / 프레임워크). Hãy document nguồn chuẩn (source of truth / 정본), quyền sở hữu trạng thái (state ownership / 상태 소유권), công khai (public / 공개) mô-đun (module / 모듈) API, lỗi (error / 오류) vocabulary và sync ngữ nghĩa (semantics / 의미론). Đừng để người mới phải đọc 30 lớp (class / 클래스) mới hiểu “bookmark có offline không”.

Giữ ViewModel nhỏ bằng cách tách reusable nghiệp vụ (business / 비즈니스) thao tác (operation / 연산), nhưng không biến mọi phương thức (method / 메서드) thành use trường hợp (case / 사례). Giữ repository giàu ý nghĩa dữ liệu (data / 데이터), không để nó thành một folder chứa Retrofit wrapper. Dùng luồng (flow / 흐름) cho observable trạng thái (state / 상태), nhưng không biến tất cả hàm (function / 함수) thành luồng (flow / 흐름) nếu chỉ cần một one-shot kết quả (result / 결과). Dùng Compose trạng thái (state / 상태) đúng thời gian tồn tại (lifetime / 수명), không đưa persistent ứng dụng (application / 애플리케이션) dữ liệu (data / 데이터) vào `remember`.

Một kiến trúc (architecture / 아키텍처) tốt khiến đường dẫn (path / 경로) dữ liệu dễ kể bằng lời: **máy chủ (server / 서버)/cục bộ (local / 로컬) nguồn (source / 소스) → repository → lĩnh vực (domain / 도메인) chính sách (policy / 정책) → trạng thái (state / 상태) holder → immutable UI trạng thái (state / 상태) → UI sự kiện (event / 이벤트) quay lại đơn vị sở hữu (owner / 오너)**. Nếu phải dùng nhiều ngoại lệ để mô tả đường dẫn (path / 경로) đó, ranh giới (boundary / 경계) đang có vấn đề.

> **Bàn giao:** Sau **16. cấp cao (senior / 시니어) notes**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [02 auth session network security](./02_auth_session_network_security.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
