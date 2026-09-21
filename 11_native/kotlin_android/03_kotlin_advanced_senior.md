# Kotlin + Android Master Note — Advanced / Senior

> Mục tiêu: hiểu sâu semantics của Kotlin, lifecycle/state/concurrency của Android, coroutine/Flow, Compose runtime, architecture, failure modes, performance, security, build/release và migration. Ở level này, không chỉ biết API nào tồn tại mà phải giải thích được **owner là ai, lifetime bao lâu, điều gì xảy ra khi interleave/process death/retry và API cũ nên giữ hay migrate vì lý do gì**.

## Mục lục

1. Kotlin type system nâng cao
2. Inline, noinline, crossinline và reified
3. Operator overloading và DSL
4. Contracts và compiler reasoning
5. Reflection, annotations và code generation
6. Coroutine internals và cancellation
7. Structured concurrency, exception và supervision
8. Flow internals, hot/cold, backpressure và sharing
9. State machine, UDF và event semantics
10. Compose runtime, identity và recomposition
11. Snapshot state, stability và phase performance
12. Side effects và lifetime
13. Android lifecycle, configuration change và process death
14. SavedStateHandle và state reconstruction
15. Multi-module architecture
16. Build system và Gradle performance
17. Dependency Injection ở quy mô lớn
18. Offline-first, cache và sync
19. Pagination và Paging 3
20. Background execution policy
21. Security production
22. Performance, memory và battery
23. Networking nâng cao
24. Database nâng cao
25. Testing strategy
26. Java interoperability
27. API design bằng Kotlin
28. Common design patterns và Kotlin idioms
29. Modern vs legacy API và migration strategy
30. Senior review checklist
31. Channel, Mutex, atomic và shared mutable state
32. Coroutine scheduler, dispatcher injection và starvation
33. Compose performance: đo recomposition đúng cách
34. Main thread, ANR, StrictMode và leak
35. R8, shrinking và keep rules
36. Signing, APK/AAB và release reproducibility
37. API-level compatibility, behavior change và feature gating
38. WebView như một security boundary
39. Database migration và schema evolution
40. Senior decision framework

---

# 1. Kotlin type system nâng cao

Kotlin type system có nullable types, bottom type `Nothing`, top types `Any`/`Any?`, variance, smart cast và platform types từ Java. Senior developer phải xem platform type như một **boundary chưa được normalize**, không phải convenience type bình thường.

Nếu Java trả `String!`, normalize nullability càng sớm càng tốt:

```kotlin
val safeName: String = javaApi.name ?: "Unknown"
```

Đừng để `String!` chảy sâu vào domain vì compiler không còn bảo vệ được invariant null-safety.

# 2. `inline`, `noinline`, `crossinline`, `reified`

`inline` có thể loại call/lambda allocation và cho phép non-local return; `noinline` giữ lambda như object; `crossinline` cấm non-local return khi callback chạy ở context khác; `reified` cho type parameter của inline function được dùng tại call site.

```kotlin
inline fun <reified T> Json.decode(text: String): T = ...
```

Đừng inline mọi higher-order function. Public inline API còn có compatibility implication vì body có thể được copy vào bytecode consumer.

# 3. Operator overloading và DSL

Operator nên phản ánh semantics tự nhiên. `moneyA + moneyB` hợp lý; `user + server` mà âm thầm gọi network là API gây bất ngờ. Kotlin DSL dựa vào lambda with receiver/extension/builder; Compose sử dụng syntax DSL-like nhưng runtime không phải builder thuần.

# 4. Contracts

Contracts giúp compiler hiểu một số quan hệ control-flow/state. Chỉ tạo custom contract khi hiểu effect và limitation; contract sai có thể làm compiler suy luận mạnh hơn behavior thực tế.

# 5. Reflection, annotations và code generation

Reflection hữu ích nhưng có cost startup/size/obfuscation. Android ecosystem hiện đại thường ưu tiên code generation khi phù hợp. KSP hiểu Kotlin symbol trực tiếp; kapt dựa Java annotation processing/stub. **Modern không đồng nghĩa bắt buộc KSP**: migrate theo processor support/maturity, không đổi chỉ vì tên API mới hơn.

Generated code là một phần build architecture. Khi upgrade Kotlin/AGP mà lỗi nằm trong Room/Hilt/serialization/Compose generated path, kiểm tra plugin/processor compatibility trước khi sửa business code.

# 6. Coroutine internals và cancellation

`suspend` không tạo thread. Compiler biến suspend function thành state machine với continuation. Coroutine có thể suspend mà không giữ thread và resume trên thread khác theo dispatcher/context.

## 6.1 Suspension không đồng nghĩa background

```kotlin
suspend fun parseHugeJson(text: String): Model {
    return parser.parse(text) // vẫn CPU/blocking trên thread hiện tại nếu parser sync
}
```

`suspend` chỉ nói function có thể suspend; nó không nói work main-safe. Blocking/CPU-heavy work cần execution policy rõ ở layer sở hữu implementation.

## 6.2 Cancellation là cooperative control flow

CPU loop dài phải check cancellation:

```kotlin
while (hasMore()) {
    ensureActive()
    computeChunk()
}
```

Không swallow `CancellationException`:

```kotlin
try {
    work()
} catch (e: CancellationException) {
    throw e
} catch (e: IOException) {
    handle(e)
}
```

Generic `catch (Throwable)` rồi convert thành `UiError` có thể biến screen đã đóng thành operation tiếp tục chạy và emit state muộn.

## 6.3 Cleanup và `NonCancellable`

`finally` vẫn chạy khi cancel. Chỉ dùng `withContext(NonCancellable)` cho cleanup suspend nhỏ thật sự bắt buộc, ví dụ đóng transaction/protocol state. Bọc toàn operation trong `NonCancellable` phá structured cancellation.

# 7. Structured concurrency, exception và supervision

Structured concurrency tạo tree lifetime/failure:

```text
parent scope
├─ child A
└─ child B
```

Với `coroutineScope`, child failure thường cancel siblings/parent scope. `supervisorScope` tách failure của siblings nhưng không “nuốt lỗi”. Bạn vẫn cần xử lý từng child failure.

`launch` và `async` khác mục đích: `launch` cho fire-and-join side effect trong scope; `async` tạo value cần `await`. Dùng `async` mà không `await` thường là smell.

## 7.1 Concurrent start không phải always faster

```kotlin
coroutineScope {
    val a = async { loadA() }
    val b = async { loadB() }
    combine(a.await(), b.await())
}
```

Chỉ parallel nếu A/B độc lập và backend/device budget cho phép. Parallel hóa quá mức có thể tăng contention, rate-limit và battery cost.

## 7.2 Stale result race

User search `a`, rồi `ab`; request `a` có thể finish sau `ab` và overwrite UI. Giải pháp không chỉ “dùng coroutine”: cần latest-wins cancellation (`flatMapLatest`/cancel previous), request generation ID hoặc state owner reject stale result.

# 8. Flow internals, hot/cold, backpressure và sharing

Cold Flow chạy producer theo mỗi collector. Hot Flow tồn tại độc lập collector tùy scope/lifetime.

```text
cold Flow
collector mới → upstream mới

StateFlow/SharedFlow
upstream/state có lifetime riêng
```

## 8.1 Backpressure operator mang nghĩa nghiệp vụ

`buffer()` cho producer đi trước trong giới hạn buffer. `conflate()` bỏ intermediate values. `collectLatest` cancel xử lý value cũ. `flatMapLatest` cancel sub-flow cũ khi key mới đến.

```kotlin
queryFlow
    .debounce(300)
    .distinctUntilChanged()
    .flatMapLatest(repository::search)
```

Search phù hợp latest-wins. Audit/payment event thì không được conflate vì mỗi event có nghĩa.

## 8.2 `stateIn`/`shareIn` thay đổi lifetime

Chúng không chỉ tối ưu subscription; chúng biến cold upstream thành shared hot stream trong một scope. Nếu scope application-level, DB/network subscription có thể sống lâu hơn screen. `SharingStarted.WhileSubscribed(timeout)` phải chọn theo reconnect cost/staleness semantics.

## 8.3 `StateFlow` vs event

`StateFlow` luôn có current state. Collector mới nhận trạng thái hiện tại. One-shot effect như “toast copied” có thể không cần survive process/recreation; payment success lại thường là domain state phải reconstruct. Trước khi chọn Channel/SharedFlow, hỏi event có được phép mất không và replay có nguy hiểm không.

# 9. State machine, UDF và event semantics

Nhiều boolean dễ tạo impossible state:

```text
loading=true
success=true
error=true
```

Model phase rõ hơn:

```kotlin
sealed interface LoadState {
    data object Idle : LoadState
    data object Loading : LoadState
    data class Content(val items: List<Item>, val refreshing: Boolean) : LoadState
    data class Failed(val previous: List<Item>?) : LoadState
}
```

UDF nghĩa state đi xuống, event/action đi lên owner; không bắt buộc dùng MVI framework hay giant reducer.

State owner phải là nơi duy nhất quyết định authoritative transition. UI local `remember` không nên cạnh tranh với database/ViewModel cho cùng business state.

# 10. Compose runtime, identity và recomposition

Compose compiler/runtime tạo composition tree, theo dõi state reads và invalidate scope liên quan. Recomposition không đồng nghĩa redraw toàn screen.

Composable body phải gần như pure render description. Side effect trực tiếp trong body sai vì body có thể chạy nhiều lần:

```kotlin
@Composable
fun Bad(userId: String) {
    repository.load(userId) // sai owner/lifetime
}
```

## 10.1 Identity quan trọng như state

Composition state gắn với vị trí/identity. Với list động, stable key giúp state đi theo entity:

```kotlin
LazyColumn {
    items(items, key = { it.id }) { item ->
        ItemRow(item)
    }
}
```

Key sai có thể khiến text-field state/animation của item A nhảy sang B khi reorder.

## 10.2 Route vs screen

```kotlin
@Composable
fun HomeRoute(viewModel: HomeViewModel) {
    val state by viewModel.uiState.collectAsStateWithLifecycle()
    HomeScreen(state, viewModel::onAction)
}
```

`HomeScreen` nên render state + forward action. Route xử lý lifecycle/navigation/DI. Cách này giúp preview/test và giảm coupling.

# 11. Snapshot state, stability và phase performance

Compose frame có các phase chính:

```text
Composition
→ Layout (measure/place)
→ Draw
```

State đọc ở phase nào quyết định phase nào bị invalidated. Đọc scroll offset chỉ để draw alpha không nhất thiết phải trigger recomposition toàn subtree nếu có API phase phù hợp.

`@Stable`/`@Immutable` là **contract**, không phải performance hint vô hại. Annotate sai có thể khiến runtime skip trong khi object mutate không observable.

`remember` cache theo composition lifetime/key, không phải global memoization. `derivedStateOf` hữu ích khi derived value thay đổi ít hơn source; dùng ở mọi chỗ tạo overhead không cần thiết.

# 12. Side effects và lifetime

`LaunchedEffect(key)` restart coroutine khi key thay đổi. `DisposableEffect` cho resource cần register/unregister. `rememberUpdatedState` cập nhật callback/value mà không restart effect. `SideEffect` sync outward sau successful composition.

Senior review hỏi hai câu:

```text
Effect này thuộc lifecycle nào?
Nếu screen biến mất, work có nên tiếp tục không?
```

Nếu phải tiếp tục sau navigation/process background, owner có thể là ViewModel/repository/WorkManager thay vì composition.

# 13. Android lifecycle, configuration change và process death

Phải phân biệt bốn lớp lifetime:

```text
recomposition
< composable destination
< Activity/Fragment instance
< process
< persistent storage/server
```

Configuration change recreate Activity/Fragment instance nhưng ViewModel có thể sống qua recreation. Process death giết toàn bộ in-memory state: ViewModel, singleton, coroutine scope, object cache đều biến mất.

## 13.1 State placement theo khả năng phục hồi

```text
render-local ephemeral state
→ remember

small UI state cần survive recreation
→ rememberSaveable / SavedStateHandle

screen/business state
→ ViewModel + source of truth

large/durable data
→ database/file/server
```

Không nhét object lớn/list vào Bundle. Binder/saved-state có limit và object lớn thường reconstruct được từ stable ID.

## 13.2 Lifecycle-aware collection

Flow UI collection phải gắn lifecycle phù hợp. Compose dùng `collectAsStateWithLifecycle()` cho Android UI thường an toàn hơn collect không lifecycle-aware. Trong View system, `repeatOnLifecycle` giúp start/cancel collector theo state lifecycle.

# 14. SavedStateHandle và state reconstruction

`SavedStateHandle` không phải database. Nó phù hợp query/filter/entity ID/navigation argument hoặc small form state cần reconstruct sau process recreation.

Pattern tốt:

```text
SavedStateHandle giữ articleId
→ ViewModel khởi tạo lại
→ repository/Room load Article(articleId)
→ UI state được reconstruct
```

Pattern xấu: serialize toàn `Article` graph/list/cache vào saved state rồi coi đó là source of truth.

# 15. Multi-module architecture

Module hóa để enforce direction/ownership/build isolation, không để tăng số folder. Feature public API nên nhỏ. Tránh circular dependency và `core:common` god-module.

# 16. Build system và Gradle performance

Nắm configuration phase, task graph, incremental build, build/configuration cache, source set, variants, KSP/kapt cost và dependency resolution. Tránh dynamic version `1.+` và hidden I/O trong configuration.

# 17. Dependency Injection ở quy mô lớn

DI quản lý dependency graph/lifetime, không phải architecture. Scope phải khớp owner: singleton giữ Activity là leak; stateful session object singleton có thể leak user state giữa logout/login nếu reset contract không rõ.

# 18. Offline-first, cache và sync

Local DB thường là source of truth cho read path. Mutation offline cần durable pending operation, idempotency, ordering/conflict strategy và retry classification. Timeout sau request gửi đi có thể là **ambiguous outcome**: server đã commit nhưng client không nhận response.

Không xây sync engine nếu product chỉ cần read cache. Complexity phải theo requirement.

# 19. Pagination và Paging 3

`Pager`, `PagingSource`, `RemoteMediator` giúp page từ DB/network. Refresh/append/prepend error có semantics riêng; append fail không nên xóa content đang hiển thị.

# 20. Background execution policy

Chọn primitive theo lifetime/durability:

```text
screen-bound work → viewModelScope/coroutine
short lifecycle UI work → lifecycle/composition scope
persisted deferrable guaranteed work → WorkManager
user-visible ongoing work → foreground service nếu use case/policy cho phép
exact wall-clock need → exact alarm khi đủ điều kiện
```

Service không phải thread. WorkManager không phải general async replacement cho mọi request.

# 21. Security production

Threat model xem APK/device là untrusted. Backend phải authorize. Validate exported component/deep link/PendingIntent/URI/WebView input. R8 không phải secret storage.

WebView + JavaScript bridge là high-risk boundary. Chỉ expose capability tối thiểu, validate URL/origin và tránh token trong URL/log.

# 22. Performance, memory và battery

Đo startup, frame/jank, memory, network, DB, battery trên thiết bị đại diện. Leak thường do long-lived owner giữ short-lived Activity/View/listener/callback hoặc coroutine scope sai lifetime.

Performance optimization phải theo:

```text
metric → trace → hypothesis → change → verify
```

# 23. Networking nâng cao

Timeout cần phân biệt call/connect/read/write. Retry chỉ khi operation idempotent hoặc backend có idempotency key. Token refresh cần single-flight để tránh hàng chục 401 cùng refresh.

# 24. Database nâng cao

Room transaction bảo vệ invariant trong DB boundary. Index theo query pattern; quá nhiều index tăng write/storage. Migration test cần schema cũ + data thật đại diện → migrate → assert schema/data.

# 25. Testing strategy

Test theo risk. Pure logic test nhanh, integration test cho serialization/DB/network/DI, instrumented/Compose test cho platform semantics. Test race bằng scheduler/barrier/fake controllable, không `delay()` ngẫu nhiên rồi hy vọng timing.

# 26. Java interoperability

`@JvmStatic`, `@JvmField`, `@JvmOverloads`, `@JvmName`, `@Throws` chỉ dùng khi Java caller cần API shape đó. Public Kotlin API nên review Java ergonomics nếu module có Java consumer.

# 27. API design bằng Kotlin

API tốt làm ownership/failure semantics explicit. Tránh boolean khó đọc và generic `Any`. Prefer type-safe domain model, immutable state và sealed result khi phù hợp.

# 28. Common design patterns và Kotlin idioms

Kotlin làm nhiều GoF pattern nhẹ hơn: Strategy bằng function type, Singleton bằng `object`, Decorator bằng delegation, Observer bằng Flow, State bằng sealed hierarchy. Pattern là giải pháp cho force cụ thể, không phải huy hiệu senior.

# 29. Modern vs legacy API và migration strategy

Đây là điểm thường bị tài liệu Android giải thích quá đơn giản. Không phải API cũ nào cũng phải xóa.

Phân loại trước khi migrate:

```text
A. Deprecated/unsafe
→ lập kế hoạch migrate

B. Supported nhưng replacement mới có benefit rõ
→ migrate incremental khi đáng chi phí

C. Still-valid cho use case cụ thể
→ giữ

D. Historical
→ biết để maintain, không chọn cho code mới
```

## 29.1 Bản đồ legacy → modern

| Legacy / older stack | Modern direction | Reasoning |
|---|---|---|
| Java-heavy | Kotlin-first | Java vẫn fully relevant cho interop/legacy |
| Kotlin synthetic view | View Binding / Compose | synthetic không còn modern workflow |
| `findViewById` | View Binding / Compose | vẫn valid trong custom/View code |
| XML + Fragment | Compose hoặc hybrid | XML/Fragment vẫn supported |
| `AsyncTask` | coroutine / WorkManager theo lifetime | replacement phụ thuộc durability |
| callback pyramid | suspend / Flow | callback vẫn đúng ở SDK boundary |
| LiveData-centric | Flow/StateFlow ở modern Kotlin stack | LiveData vẫn dùng được |
| RxJava-heavy | coroutine/Flow thường phổ biến hơn | không rewrite nếu cost/risk không có lợi |
| SharedPreferences | DataStore cho structured settings | migration theo data/behavior contract |
| `startActivityForResult` | Activity Result API | lifecycle-aware registration/result |
| manual Service cho deferred work | WorkManager | Service còn đúng cho ongoing work |
| kapt | KSP khi processor hỗ trợ | migrate từng processor |
| `kotlinOptions {}` | `compilerOptions {}` | modern Kotlin Gradle DSL |
| K1 | K2 | compiler generation mới |

## 29.2 Migration giữ behavior trước, đổi implementation sau

Ví dụ RxJava repository cũ có thể adapter sang Flow ở boundary thay vì rewrite data layer cùng lúc. XML Fragment có thể host `ComposeView`, hoặc Compose có thể host `AndroidView`. Java module có thể được gọi từ Kotlin mà chưa cần convert tất cả.

Characterization test bảo vệ behavior hiện tại trước khi refactor. Strangler migration cho phép feature/screen mới dùng stack modern trong khi path cũ vẫn chạy; khi telemetry/test đủ confidence mới xóa legacy.

## 29.3 Đừng nhầm modern với architecture tốt

Compose + Flow + Hilt + Kotlin 2.x vẫn có thể có duplicated state, leaked scope, race và god ViewModel. Ngược lại XML + Fragment + RxJava có thể có contract/test rất tốt. Migration phải mua được giá trị: safety, maintainability, policy compatibility, performance hoặc developer productivity.

# 30. Senior review checklist

Review theo invariant/lifetime thay vì syntax:

```text
state owner/source of truth?
process death reconstruct thế nào?
coroutine scope owner?
cancellation propagate không?
race/stale result có thể xảy ra không?
Flow hot/cold/replay đúng semantics không?
Compose effect đúng lifetime không?
operation retry/idempotent không?
legacy API thuộc nhóm A/B/C/D nào?
security boundary nào nhận input không tin cậy?
performance metric nào quan trọng?
release/minified path có test không?
```

# 31. Channel, Mutex, atomic và shared mutable state

Coroutine không loại data race. `Mutex` phù hợp critical section suspend-aware; atomic cho operation nhỏ; Channel cho message hand-off/queue; actor/single-owner cho ordered mutation.

```kotlin
private val mutex = Mutex()
private var cached: Token? = null

suspend fun token(): Token = mutex.withLock {
    cached ?: refreshToken().also { cached = it }
}
```

Ví dụ trên single-flight nhưng giữ lock trong network call. Tùy design có thể cần deferred-in-flight state để không giữ lock rộng. Primitive phải theo invariant, không theo template.

# 32. Coroutine scheduler, dispatcher injection và starvation

Blocking I/O, CPU-heavy và main-thread UI có execution need khác nhau. Dispatcher injection giúp test/main-safety nhưng không cần inject năm dispatcher vào mọi class.

Starvation xảy ra khi blocking work giữ pool thread, lock dài hoặc CPU parallelism vượt budget. Phân biệt coroutine `suspended` với thread `blocked` khi đọc profiler/stack trace.

# 33. Compose performance: đo recomposition đúng cách

Recomposition count không tự là bug. Quan tâm frame time, expensive composition/layout/draw, allocation và invalidation scope. `remember`/`derivedStateOf` chỉ dùng khi semantics đúng và measurement chỉ ra benefit.

# 34. Main thread, ANR, StrictMode và leak

UI thread xử lý input/lifecycle/draw orchestration. Disk/network, JSON parse, DB, bitmap decode hoặc lock contention đều có thể gây jank/ANR.

`StrictMode` hữu ích ở debug để phát hiện một số policy violation. Leak investigation cần retention path; `System.gc()` không sửa reachable reference.

# 35. R8, shrinking và keep rules

Reflection/JNI/name-based lookup có thể bị R8 ảnh hưởng. Keep rule phải hẹp. Library tự cần rule thì nên ship consumer rules. Release crash cần mapping đúng artifact để deobfuscate.

# 36. Signing, APK/AAB và release reproducibility

Release artifact phải ký. Quản lý signing/upload key như credential dài hạn. Reproducibility nghĩa trace được source commit, dependency versions, Gradle/JDK/toolchain/config đã tạo artifact.

# 37. API-level compatibility, behavior change và feature gating

`compileSdk` cho symbol compile-time; `minSdk` cho runtime floor; `targetSdk` opt-in platform behavior contract. Khi nâng target, phải audit behavior changes, không chỉ sửa số Gradle.

API mới cần runtime guard/compat abstraction nếu minSdk thấp hơn. Platform latest và Play target requirement là hai khái niệm khác nhau.

# 38. WebView như một security boundary

Validate scheme/host/navigation. Cấu hình JavaScript/file access/debugging theo threat model. `addJavascriptInterface` chỉ cho trusted content và API tối thiểu. Token không nên nằm tùy tiện trong URL.

# 39. Database migration và schema evolution

Production migration phải bảo vệ data thật. Test từ nhiều schema version còn tồn tại, không chỉ previous → latest. Với sync app, local schema migration còn phải tương thích rollout backend/client lệch version.

# 40. Senior decision framework

Khi gặp feature mới, đi theo chuỗi:

```text
Requirement
→ invariant
→ owner/lifetime
→ state/source of truth
→ concurrency/order
→ cancellation/failure/retry
→ persistence/reconstruction
→ platform/version compatibility
→ security
→ performance evidence
→ tests
→ release/rollback
```

Nếu chuỗi này rõ, việc chọn MVVM/MVI, Hilt/Koin, Room/SQLDelight hay Retrofit/Ktor trở thành quyết định có lý do thay vì preference.