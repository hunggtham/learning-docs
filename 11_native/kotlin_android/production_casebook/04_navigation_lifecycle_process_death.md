# Case 04 — Navigation, Deep Link, Lifecycle và Process Death

Navigation thường được học như `navController.navigate("detail/123")`, còn lifecycle được học riêng như một sơ đồ `onCreate` → `onStart` → `onResume`. Trong production, hai chủ đề này gắn chặt: một destination có lifetime riêng, back stack có thể được restore, app có thể mở từ deep link khi process chưa tồn tại, configuration change không giống process death, và state của screen cần được phân loại để biết cái gì nằm trong `remember`, `rememberSaveable`, `ViewModel`, `SavedStateHandle` hay persistent storage.

## 1. Bốn loại lifetime cần phân biệt

Một mental model hữu ích là chia state theo thời gian sống.

**Recomposition lifetime**: biến chỉ cần tồn tại qua recomposition trong cùng composition. Dùng `remember`.

**Configuration/recreation lifetime**: state UI nhỏ cần giữ khi Activity recreate, như tab/filter/text draft nhỏ. `rememberSaveable` hoặc `SavedStateHandle` phù hợp tùy owner.

**Navigation destination lifetime**: state thuộc một screen khi destination còn trên back stack. ViewModel scoped theo navigation entry thường phù hợp.

**Process/persistent lifetime**: data cần khôi phục sau process chết lâu hoặc app restart. Dữ liệu lớn/quan trọng phải từ Room/DataStore/server, không trông chờ Bundle.

Phân loại đúng lifetime quan trọng hơn thuộc tên API.

## 2. `remember` không phải persistence

```kotlin
var expanded by remember { mutableStateOf(false) }
```

Giá trị tồn tại qua recomposition nhưng mất nếu composable rời composition hoặc process/activity recreate tùy cấu trúc.

`rememberSaveable` dùng saved instance state cho type saveable:

```kotlin
var query by rememberSaveable { mutableStateOf("") }
```

Không nên save object lớn, bitmap, database result hoặc secret vào saved state chỉ để “khỏi load lại”. Bundle có size limit và process restore cần lightweight key/state.

## 3. ViewModel sống qua configuration change, không bảo đảm qua process death

Đây là nhầm lẫn rất phổ biến. ViewModel được giữ khi configuration change nhưng process bị hệ điều hành kill thì memory biến mất.

Vì vậy:

```kotlin
class DetailViewModel(
    savedStateHandle: SavedStateHandle,
    repository: ArticleRepository
) : ViewModel() {
    private val articleId: String = checkNotNull(savedStateHandle["articleId"])
    val article = repository.observeArticle(articleId)
}
```

ViewModel chỉ cần giữ **key** đủ để reconstruct state từ repository. Không cần persist toàn bộ Article object trong SavedStateHandle.

## 4. Navigation argument nên là identity, không phải object graph

Đừng pass một domain object lớn qua route. Pass ID hoặc minimal primitive/serializable argument rồi load từ source of truth.

Lợi ích:

- deep link có thể tạo destination chỉ từ URL;
- process restore không cần serialize object lớn;
- detail luôn đọc latest source of truth;
- route contract ổn định hơn model nội bộ.

## 5. Type-safe route với Navigation Compose

Navigation Compose hiện hỗ trợ type-safe route dựa trên Kotlin serialization. Mental model:

```kotlin
@Serializable
data object Home

@Serializable
data class ArticleDetail(val articleId: String)
```

Graph:

```kotlin
NavHost(
    navController = navController,
    startDestination = Home
) {
    composable<Home> {
        HomeRoute(
            onOpenArticle = { id ->
                navController.navigate(ArticleDetail(id))
            }
        )
    }

    composable<ArticleDetail> { backStackEntry ->
        val route = backStackEntry.toRoute<ArticleDetail>()
        ArticleDetailRoute(articleId = route.articleId)
    }
}
```

Type-safe route giảm string parsing và mismatch argument, nhưng vẫn cần design navigation contract tốt.

## 6. Route-level composable và screen-level composable

Route nên kết nối navigation/ViewModel; Screen nên tập trung render.

```kotlin
@Composable
fun ArticleDetailRoute(
    articleId: String,
    viewModel: ArticleDetailViewModel,
    onBack: () -> Unit
) {
    val state by viewModel.uiState.collectAsStateWithLifecycle()

    ArticleDetailScreen(
        state = state,
        onBack = onBack,
        onRetry = viewModel::retry
    )
}
```

Điều này tránh composable con giữ `NavController` khắp nơi và giúp test pure UI dễ hơn.

## 7. Navigation không phải global event bus

Một anti-pattern là đặt `NavController` vào singleton hoặc repository. Data layer không nên biết user đang ở screen nào.

Navigation decision thường thuộc UI coordination. Domain có thể trả result/state như `PaymentCompleted(orderId)`, còn route/UI quyết định navigate tới receipt.

## 8. Back stack semantics

Hiểu `popBackStack`, `popUpTo`, inclusive, `launchSingleTop`, `restoreState` quan trọng hơn memorize snippet.

Ví dụ sau login, bạn thường không muốn Back quay lại login:

```kotlin
navController.navigate(Home) {
    popUpTo<Login> { inclusive = true }
}
```

Sau logout, protected back stack cần được reset tương tự. Nhưng data security không được dựa vào việc xóa back stack; protected repository/backend vẫn phải kiểm tra session.

## 9. Multiple tabs và state restoration

Bottom navigation thường muốn mỗi tab giữ back stack riêng. Nếu mỗi lần đổi tab bạn tạo graph mới hoặc navigate vô hạn, back stack có thể phình.

Pattern thường dùng `launchSingleTop`, `restoreState` và `popUpTo` start destination với `saveState` để preserve tab state. Quan trọng là test behavior: đổi tab, drill detail, đổi tab khác, quay lại phải ở đúng vị trí product mong muốn.

## 10. Deep link là external input

Deep link có thể đến từ browser, notification, email hoặc app khác. Vì vậy route argument là **untrusted input**.

Không được giả định `articleId` hợp lệ chỉ vì route type-safe. Validate ID, check authorization, handle entity không tồn tại và session chưa login.

```text
external URI
→ parse + validate
→ resolve app route
→ auth/authorization gate
→ load data
→ render or safe error
```

## 11. App Link và custom scheme

Custom scheme như `myapp://article/123` dễ đăng ký nhưng app khác cũng có thể claim scheme.

Android App Links dùng HTTPS domain association để hệ thống có thể verify ownership. Với link public từ web, App Link thường tạo trust model tốt hơn.

Dù verified link, input path/query vẫn cần validation.

## 12. Authentication-gated deep link

Một case điển hình: user mở link `/orders/123`, nhưng chưa login.

Sai pattern: bỏ link và chuyển login; sau login user mất context.

Tốt hơn:

```text
Deep link arrives
→ parse target destination
→ session SignedOut
→ store small pending navigation intent
→ login
→ validate target against current account
→ navigate to target
```

Pending target phải minimal và safe. Không persist secret hoặc raw unvalidated payload tùy tiện.

## 13. Notification navigation

Notification tap cũng là deep entry. PendingIntent flags, unique request code và task/back-stack behavior cần được thiết kế.

Nếu notification dẫn đến message detail, app có thể đang:

- chưa chạy;
- background với existing task;
- foreground ở chính message đó;
- signed out;
- user đã switch account.

Route handler phải idempotent và account-aware.

## 14. Configuration change khác process death

Configuration change tạo Activity instance mới trong cùng process. ViewModel thường được giữ.

Process death xóa memory. Khi user quay lại từ recent apps, Android có thể recreate task/back stack từ saved state. ViewModel mới được tạo. Nếu ViewModel giả định một in-memory singleton còn data thì bug xuất hiện.

Test process death riêng, không coi rotation là đủ.

## 15. Cách test process recreation

Trong manual test, có thể dùng Developer Options / “Don’t keep activities” cho một số lifecycle issue, nhưng nó không hoàn toàn mô phỏng process death.

Một kỹ thuật thực tế là background app rồi dùng ADB kill process hoặc Android Studio tooling phù hợp, sau đó restore task. Mục tiêu test:

- destination restore đúng;
- route argument đủ để reload;
- unsaved transient state behavior đúng;
- repository reconnect data source;
- session restore trước protected screen.

## 16. SavedStateHandle không phải database

`SavedStateHandle` hợp với ID, filter, draft nhỏ, step number. Dữ liệu user-created quan trọng chưa gửi server không nên chỉ dựa vào saved state.

Ví dụ form dài có thể autosave draft vào local DB nếu mất dữ liệu là unacceptable.

## 17. Lifecycle-aware Flow collection

Compose UI nên collect observable state theo lifecycle để không giữ unnecessary collection khi screen không active.

```kotlin
val uiState by viewModel.uiState.collectAsStateWithLifecycle()
```

Ở View system có `repeatOnLifecycle`:

```kotlin
lifecycleScope.launch {
    repeatOnLifecycle(Lifecycle.State.STARTED) {
        viewModel.uiState.collect { render(it) }
    }
}
```

Không dùng `launchWhenStarted` như một cargo-cult nếu semantics suspension/resource upstream không phù hợp. Hiểu lifecycle của producer/collector mới quan trọng.

## 18. `LaunchedEffect` và lifecycle của effect

```kotlin
LaunchedEffect(articleId) {
    viewModel.load(articleId)
}
```

Effect restart khi key thay đổi và cancel khi rời composition. Nhưng nếu `load` là screen initialization, thường ViewModel init/repository stream có semantics ổn định hơn. Tránh dùng `LaunchedEffect(Unit)` để biến Composable thành imperative controller cho mọi thứ.

Effect phù hợp khi cần side effect gắn với composition/key, ví dụ scroll, analytics screen exposure, focus hoặc collect one-off UI effect.

## 19. `DisposableEffect` cho registration có cleanup

Khi bridge listener API:

```kotlin
DisposableEffect(owner) {
    val observer = LifecycleEventObserver { _, event ->
        // react
    }
    owner.lifecycle.addObserver(observer)

    onDispose {
        owner.lifecycle.removeObserver(observer)
    }
}
```

Registration và cleanup phải cùng boundary để tránh leak.

## 20. `rememberUpdatedState` khi callback thay đổi nhưng effect không nên restart

Một long-lived effect có thể cần callback mới nhất mà không restart timer/listener:

```kotlin
val latestOnTimeout by rememberUpdatedState(onTimeout)

LaunchedEffect(Unit) {
    delay(5_000)
    latestOnTimeout()
}
```

Đây là ví dụ Compose effect semantics không thể hiểu chỉ bằng “API này dùng khi nào” mà phải hiểu lifetime/key.

## 21. Navigation result

Screen B edit item rồi quay về A. Có nhiều lựa chọn:

- database là source of truth: B update repository; A đang observe nên tự nhận update;
- small one-off result: SavedStateHandle của previous entry;
- shared scoped ViewModel nếu hai destination thực sự share workflow state.

Nếu data đã nằm trong repository, truyền object quay lại thường tạo duplicate state không cần thiết.

## 22. Shared ViewModel scope phải có lý do

Checkout nhiều bước có thể dùng ViewModel scoped theo navigation graph để giữ workflow state. Nhưng global Activity-scoped ViewModel cho mọi screen dễ biến thành god state holder và leak coupling.

Scope state theo nhỏ nhất lifetime đáp ứng requirement.

## 23. Nested graph là boundary workflow

Auth graph, onboarding graph, checkout graph có thể là nested graph. Nó giúp scope ViewModel và back-stack policy theo workflow.

Nested graph không nên chỉ dùng để làm file navigation “đẹp”; nó có ý nghĩa khi destination share lifecycle/flow.

## 24. Adaptive navigation

Phone có thể dùng bottom navigation, tablet có navigation rail hoặc list-detail pane. Architecture tốt không encode business navigation trực tiếp vào widget cụ thể.

Một selection như `selectedArticleId` có thể ở state holder; compact layout navigate detail destination, expanded layout hiển thị detail pane cùng screen. Cùng một state, presentation/navigation khác theo window size.

## 25. Foldable và window size

Không hard-code “tablet nếu width > X dp” rải rác. Dùng adaptive/window APIs và centralize layout policy. Khi posture/window thay đổi runtime, state phải giữ đúng entity selection.

## 26. Accessibility và navigation focus

Sau navigation, screen reader focus nên có hành vi hợp lý. Dialog/bottom sheet phải có semantic role và focus management đúng. Back gesture/system back không chỉ là technical callback; nó là UX contract.

Predictive back và transition hiện đại yêu cầu navigation stack có semantics đúng, không override Back tùy tiện để chống user rời screen. Nếu có unsaved changes, model explicit confirmation state.

## 27. Unsaved form và back

Không nên block back bằng một global flag khó hiểu. Form state biết nó dirty hay không:

```kotlin
data class EditUiState(
    val draft: Draft,
    val original: Draft,
    val showDiscardDialog: Boolean = false
) {
    val isDirty: Boolean get() = draft != original
}
```

Back event nếu dirty thì show confirm. Nếu process death, nếu draft quan trọng thì persist draft; dialog state có thể không cần persist tùy UX.

## 28. Navigation test

Test ở nhiều tầng.

Pure ViewModel test: session/payment state dẫn đến navigation signal/state đúng.

Navigation integration test: route parse, graph action, back stack.

Compose UI test: click element và assert destination semantics.

Deep link test: invalid ID, signed-out user, missing entity, multiple entry state.

Process recreation test: restored entry load được từ ID.

## 29. Senior notes

Navigation bug thường là state ownership bug disguised. Nếu route phải mang object lớn để screen hoạt động, source-of-truth boundary có thể sai. Nếu process death làm app crash, restoration contract chưa đủ. Nếu logout rồi Back xem được protected data, session/data boundary có vấn đề. Nếu deep link bypass validation, external input boundary sai.

Hãy thiết kế destination như một function nhận **minimal stable identity + current application state** và có khả năng reconstruct UI. Khi làm được điều đó, navigation, deep link, adaptive layout và process restoration đều đơn giản hơn.
