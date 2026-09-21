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

<!-- merge: preserve both canonical variants -->
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
<!-- merge: preserve both canonical variants -->
# 9. State machine, UDF và architecture invariant

UDF không phải tên khác của MVI framework. Nó là một constraint giúp reasoning:

```text
authoritative state
    ↓
UI render
    ↓
user/system event
    ↓
owner xử lý side effect / transition
    ↓
source of truth thay đổi
    ↓
state mới
```

Điểm Senior cần giữ không phải “mọi app phải có reducer”, mà là **mỗi fact quan trọng có owner và source of truth rõ**. Nếu cùng một bookmark tồn tại thành mutable state riêng ở database, repository cache, ViewModel và `remember`, hệ thống có bốn nơi có thể bất đồng.

## 9.1 Bắt đầu architecture bằng invariant

Trước khi chọn MVVM/MVI/Clean Architecture, hãy viết invariant:

```text
User A không bao giờ nhìn thấy cache của User B.
Sau khi payment được server confirm, retry không tạo transaction thứ hai.
UI chỉ render article snapshot từ local source of truth.
Process recreation có thể reconstruct screen từ stable ID.
```

Architecture có giá trị khi boundary làm invariant dễ giữ và dễ test.

## 9.2 State machine tránh impossible state

Nhiều flags độc lập dễ tạo tổ hợp vô nghĩa:

```text
loading=true
fatalError=true
contentEmpty=false
paymentSucceeded=true
```

Có hai kiểu model phổ biến:

```text
mutually exclusive phase
→ sealed state / explicit state machine

content có thể coexist với refresh/error metadata
→ immutable data class với invariant được document
```

Không ép mọi screen thành sealed state nếu UX cần cached content + refresh + warning cùng lúc. Model phải theo business invariant, không theo template.

## 9.3 Command, state và event phải phân biệt

```text
Command
= yêu cầu làm việc: Refresh, Submit, Retry

State
= fact hiện tại có thể đọc lại: PaymentCompleted, UserLoggedOut

Transient UI effect
= Snackbar "Copied", haptic, focus request
```

Nếu một fact quan trọng bị model thành event một lần và collector vắng mặt thì mất, design có thể sai. Durable fact nên có durable/source-of-truth representation.

## 9.4 Stale snapshot là architecture bug, không chỉ concurrency bug

Ví dụ ViewModel giữ object `Article` được truyền từ list screen sang detail. Trong lúc detail mở, DB sync article mới. Detail vẫn hiển thị object cũ vì navigation argument trở thành source of truth thứ hai.

Tốt hơn:

```text
navigation truyền articleId
→ destination observe repository/DB theo ID
→ UI luôn thấy authoritative snapshot
```

Architecture phải giải thích data freshness và reconstruction, không chỉ dependency direction.
<!-- end merged variant -->

```kotlin
sealed interface LoadState {
    data object Idle : LoadState
    data object Loading : LoadState
    data class Content(val items: List<Item>, val refreshing: Boolean) : LoadState
    data class Failed(val previous: List<Item>?) : LoadState
}
```

<!-- merge: preserve both canonical variants -->
UDF nghĩa state đi xuống, event/action đi lên owner; không bắt buộc dùng MVI framework hay giant reducer.

State owner phải là nơi duy nhất quyết định authoritative transition. UI local `remember` không nên cạnh tranh với database/ViewModel cho cùng business state.

# 10. Compose runtime, identity và recomposition

Compose compiler/runtime tạo composition tree, theo dõi state reads và invalidate scope liên quan. Recomposition không đồng nghĩa redraw toàn screen.

Composable body phải gần như pure render description. Side effect trực tiếp trong body sai vì body có thể chạy nhiều lần:
<!-- merge: preserve both canonical variants -->
Compose không phải “framework gọi lại toàn bộ screen mỗi khi state đổi”. Compiler Compose biến `@Composable` function thành code có thêm metadata/runtime protocol; runtime duy trì **Composition** để nhớ cấu trúc UI, identity của các call site và những state read nào xảy ra ở đâu. Khi observable state đổi, Compose invalidates đúng restart scope liên quan và cố làm lượng công việc tối thiểu cần thiết.

Mental model một frame:

```text
State/data
   ↓
Composition — UI nào tồn tại?
   ↓
Layout — đo và đặt ở đâu?
   ↓
Draw — vẽ như thế nào?
```

Recomposition chỉ nói về việc chạy lại phần **composition** cần thiết. Sau đó layout hoặc draw có thể chạy hoặc được bỏ qua tùy kết quả. Vì vậy “recomposition count cao” tự nó chưa chứng minh UI chậm.

## 10.1 Identity đến từ vị trí call site và key

Compose cần biết instance logic nào ở lần composition hiện tại tương ứng với instance nào trước đó để giữ `remember`, effect và state đúng chỗ.

```kotlin
LazyColumn {
    items(
        items = users,
        key = { it.id },
        contentType = { "user" }
    ) { user ->
        UserRow(user)
    }
}
```

Key phải biểu diễn identity bền vững, không phải index nếu index thay đổi khi insert/delete/reorder.

## 10.2 `remember` thuộc Composition, không thuộc business object

```kotlin
val state = remember(key) { expensiveInitialization(key) }
```

Giá trị được giữ khi call site còn identity và key không đổi. `remember` không sống qua process death; không tự sống qua việc composable rời Composition; và không phải nơi giữ dữ liệu business lâu dài chỉ vì “muốn khỏi load lại”.

Phân lớp owner:

```text
UI ephemeral state trong call site
→ remember

UI state nhỏ cần save qua recreation
→ rememberSaveable

screen state/business interaction
→ ViewModel / state holder

durable data
→ repository + database/DataStore/server
```

## 10.3 State read quyết định phase nào bị invalidated

Compose theo dõi nơi đọc state, không chỉ nơi state được tạo. Read trong composition có thể trigger recomposition; read trong placement có thể chỉ restart layout; read trong draw có thể chỉ restart draw.

Senior optimization không phải chuyển mọi read xuống phase thấp nhất bằng mẹo khó đọc; nó là hiểu hot path để tránh work không cần thiết khi profiler chứng minh vấn đề.

## 10.4 Composable body phải gần pure

Composable có thể chạy lại, bị skip hoặc một composition attempt có thể không được apply. Vì vậy body không phải nơi gọi side effect tùy ý:
<!-- end merged variant -->

```kotlin
@Composable
fun Bad(userId: String) {
    repository.load(userId) // sai owner/lifetime
}
```

<!-- merge: preserve both canonical variants -->
## 10.1 Identity quan trọng như state

Composition state gắn với vị trí/identity. Với list động, stable key giúp state đi theo entity:

```kotlin
LazyColumn {
    items(items, key = { it.id }) { item ->
        ItemRow(item)
    }
}
```
<!-- merge: preserve both canonical variants -->
UI body nên chủ yếu mô tả output từ input/state. Business side effect thuộc event handler/ViewModel/data layer; effect gắn lifecycle UI dùng Effect API phù hợp.

# 11. Snapshot State, stability và performance

Compose Snapshot system cung cấp observable state model cho runtime. Ordinary Kotlin mutation không tự trở thành observable. Immutable snapshot hoặc Snapshot-aware collection làm mutation contract rõ hơn.

**Immutable** và **Stable** không phải cùng khái niệm. Không annotate `@Stable`/`@Immutable` chỉ để giảm metric; annotation sai có thể khiến runtime bỏ work cần thiết và tạo correctness bug.

`derivedStateOf` hữu ích khi input đổi thường xuyên nhưng output semantic đổi ít hơn. `remember` cache theo identity/key chứ không phải global cache. Lazy list cần stable key; key sai không chỉ ảnh hưởng performance mà còn có thể gắn state/effect nhầm entity.

Performance phải đo theo frame: composition, measure/layout, draw, allocation/GC, main-thread block và lazy reuse. Correctness đứng trước skip optimization.
<!-- end merged variant -->

Key sai có thể khiến text-field state/animation của item A nhảy sang B khi reorder.

<!-- merge: preserve both canonical variants -->
## 10.2 Route vs screen

```kotlin
@Composable
fun HomeRoute(viewModel: HomeViewModel) {
    val state by viewModel.uiState.collectAsStateWithLifecycle()
    HomeScreen(state, viewModel::onAction)
<!-- merge: preserve both canonical variants -->
Compose effect API tồn tại vì composable body nên side-effect free. Chọn effect theo lifetime và cleanup contract.

`LaunchedEffect(key)` launch coroutine khi vào Composition, cancel khi rời Composition, và cancel/restart khi key đổi. Constant key như `Unit` chỉ có nghĩa “không restart vì key trong lifetime call site này”, không phải “một lần toàn app”.

`rememberUpdatedState` cho phép effect giữ lifetime hiện tại nhưng đọc callback/value mới nhất. `DisposableEffect` dùng khi có acquire/release listener/resource. `SideEffect` publish Compose state sang non-Compose object sau successful composition. `snapshotFlow` chuyển Snapshot reads thành Flow; `rememberCoroutineScope` hữu ích cho coroutine được kích hoạt từ UI event như snackbar.

Senior review phải hỏi:

```text
identity của effect là gì?
key nào restart?
value nào chỉ cần latest?
cleanup ở đâu?
leaving Composition có nên cancel operation không?
đây là UI effect hay business command?
```

# 13. Lifecycle, configuration change và process death

Configuration change thường recreate Activity nhưng ViewModel có thể sống qua recreation. Process death khác hoàn toàn: OS kill process, toàn bộ in-memory state mất. Nếu state phải restore, cần persistence/SavedStateHandle/rememberSaveable tùy loại dữ liệu.

Đừng lưu object lớn hoặc dữ liệu có thể reload vào Bundle. Bundle có giới hạn Binder transaction; stable IDs và persistence tốt hơn.

# 14. SavedStateHandle

`SavedStateHandle` cho ViewModel state cần phục hồi sau process recreation theo capability của saved state. Nó không phải database. Chỉ lưu dữ liệu nhỏ, serializable/savable hoặc identifier cần để reconstruct screen.

# 15. Multi-module architecture: boundary phải mua được giá trị

Module hóa không phải mục tiêu tự thân. Một module nên tồn tại vì ít nhất một force cụ thể: ownership/team boundary, dependency isolation, build parallelism/cache, reusable public contract, optional delivery hoặc giới hạn accidental coupling.

Một graph có thể như:

```text
:app
  ↓
:feature:home:impl ─────→ :feature:home:api
  ↓                           ↑
:core:data ─────→ :core:model │
  ↓                           │
:core:database / :core:network
```

Dependency phải có hướng. Nếu `feature:A` import internal implementation của `feature:B`, boundary trên sơ đồ không tồn tại thực tế.

## 15.1 Public surface nhỏ hơn implementation surface

Module public API nên chứa contract cần thiết, không export mọi DTO/entity/helper. `internal` là công cụ compile-time/module visibility hữu ích nhưng không phải security boundary.

Một thay đổi implementation phía sau API nhỏ có blast radius build/source nhỏ hơn một `core:common` expose hàng trăm symbol.

## 15.2 God core module là monolith đội lốt modularization

`core:common` chứa networking, analytics, navigation, model, auth và utility của mọi feature tạo dependency fan-in cực lớn. Mỗi sửa nhỏ có thể invalidated nhiều module và mọi team đều sở hữu “một chút”, cuối cùng không ai thực sự sở hữu.

Tách theo capability ổn định, không theo mong muốn tạo thật nhiều folder.

## 15.3 Module boundary phải đi cùng runtime ownership

Tách `feature:checkout` thành module không tự giải quyết việc checkout session sống bao lâu, repository source of truth ở đâu hay coroutine scope thuộc ai. Build boundary và runtime boundary là hai dimension khác nhau.

# 16. Gradle, build graph và release debugging

Gradle build cần được hiểu theo phase thay vì xem như “Android Studio bấm Run”.

```text
Settings / project discovery
→ configuration
→ variant/task graph
→ task execution
→ compiler/code generation
→ resource + manifest processing
→ D8/R8
→ packaging/signing
→ APK/AAB
```

Một lỗi phải được định vị ở phase nào trước khi sửa.

## 16.1 Configuration cost vs execution cost

Configuration cache giải quyết việc tái sử dụng configuration state khi build logic tương thích; build cache tái sử dụng task output dựa trên input. Hai cache khác nhau.

Không chạy network/file scanning tùy ý trong configuration. Custom task phải khai báo input/output đúng để incremental/cache có thể tin cậy.

## 16.2 Build reproducibility

Production artifact phải truy được:

```text
source commit
Gradle wrapper
AGP/Kotlin/JDK
resolved dependency graph
build variant/flavor
R8 rules
signing identity/process
feature/config inputs
```

Dynamic version như `1.+` phá reproducibility vì cùng commit có thể resolve dependency khác ở ngày khác.

## 16.3 Debug build pass không chứng minh release pass

Release có thể khác debug ở:

```text
R8 shrinking/optimization/obfuscation
resource shrinking
BuildConfig/manifest value
signing
proguard consumer rules
feature flag/environment
native symbols
```

Vì vậy CI cần compile/test release-like variant. Lỗi reflection/JNI/serialization chỉ xuất hiện sau minify là failure mode bình thường cần được thiết kế test.

## 16.4 Debugging theo exact variant

Khi bug chỉ xảy ra ở `prodRelease`, đừng reproduce bằng `devDebug` rồi kết luận. Ghi exact tuple:

```text
commit + variant + device/API + dependency lock + server/config version
```

Forensics bắt đầu từ artifact thật, không từ source “trông giống”.

# 17. DI ở quy mô lớn: graph và lifetime contract

DI không phải architecture; DI quản lý object graph và creation/lifetime. Scope phải phản ánh owner thật:

```text
application singleton
session scoped
activity/navigation graph scoped
ViewModel scoped
transient
```

Một object stateful vô tình `@Singleton` có thể leak data qua account switch. Một Activity Context bị giữ trong singleton tạo memory leak. Constructor injection làm dependency explicit nhưng không tự bảo đảm scope đúng.

Hilt/Dagger compile-time graph giúp verify dependency. Assisted injection hữu ích khi một số input là runtime identity như `itemId`. Multibinding phù hợp registry/plugin model. Không tạo interface cho mọi class chỉ để DI “đẹp”; seam phải phản ánh volatility/test requirement thật.

# 18. Offline-first, source of truth và sync correctness

Offline-first không chỉ là “cache API response”. Phải định nghĩa consistency contract giữa local và remote.

Một pattern production:

```text
UI observe local DB
network refresh/sync
    ↓
transaction update local DB
    ↓
DB emit authoritative snapshot
    ↓
UI update
```

## 18.1 Read-offline và write-offline khác độ khó

Read cache chỉ cần freshness/revalidation policy. Write-offline cần durable pending mutation, idempotency, ordering, conflict, retry và account isolation.

Nếu product không cần offline mutation, đừng xây distributed sync engine chỉ vì “offline-first nghe hiện đại”.

## 18.2 Ambiguous outcome

Request timeout không có nghĩa server chưa commit:

```text
client gửi POST
server commit
response mất
client thấy timeout
```

Nếu retry mù, duplicate side effect có thể xuất hiện. Idempotency key/server contract mới giải quyết được nhóm failure này.

## 18.3 Durable outbox invariant

Nếu local optimistic update và pending operation phải luôn cùng tồn tại, ghi chúng trong cùng local transaction:

```text
entity state changed
AND
outbox mutation exists
```

Crash giữa hai write riêng biệt sẽ phá invariant.

## 18.4 Conflict và ordering

LWW chỉ đúng nếu business chấp nhận last-write-wins và clock/version đáng tin. Nhiều domain cần server revision/optimistic concurrency/field merge hoặc explicit conflict UI.

Mutation queue cũng cần biết operation có commute không. `setFavorite(true)` có semantics retry khác `toggleFavorite()` vì toggle phụ thuộc state trước đó.

## 18.5 Account/session isolation

Pending work và cache phải namespace theo account/session nếu dữ liệu user-specific. Logout không chỉ xóa token; cần xác định worker đang chạy, DB/cache cũ, in-flight response và notification/deep link state.

# 19. Paging 3

Paging 3 giúp load dữ liệu theo trang từ database/network. `Pager`, `PagingSource`, `RemoteMediator` là các abstraction chính. `RemoteMediator` phù hợp khi network + DB kết hợp và DB là source of truth.

UI cần handle refresh/append/prepend load states độc lập. Sai lầm thường gặp là biến mọi error thành full-screen error dù chỉ append page fail.

# 20. Background execution policy: chọn primitive theo lifetime + guarantee

Không chọn background API theo câu hỏi “cái nào chạy nền?”, mà theo contract:

```text
work chỉ có ý nghĩa khi screen còn sống
→ ViewModel/lifecycle coroutine

work user-visible đang chạy liên tục
→ foreground service nếu platform policy/use case cho phép

work có thể trì hoãn nhưng cần eventually execute
→ WorkManager

đúng thời điểm gần tuyệt đối
→ alarm API chỉ khi use case đủ điều kiện

server-triggered signal
→ push/FCM, sau đó app quyết định work phù hợp
```

Service không phải thread. WorkManager không phải sync correctness engine; nó schedule execution, còn idempotency/source-of-truth/retry semantic thuộc business/data design.

Production failure cần test Doze, battery saver, process kill, reboot, network mất/đổi, permission revoke và duplicate scheduling nếu relevant.

# 21. Security production: threat model trước API

Mobile client là môi trường người dùng kiểm soát. Attacker có thể decompile APK, hook method, inspect memory, chạy rooted/emulated environment hoặc gửi Intent/deep link trực tiếp.

## 21.1 Trust boundary

```text
client-side role check
= UX optimization

backend authorization
= security authority
```

Không nhúng server secret dài hạn rồi trông chờ R8/obfuscation bảo vệ. Keystore bảo vệ key material tốt hơn file plaintext nhưng không biến compromised device thành trusted server.

## 21.2 External input phải coi là untrusted

Các boundary cần validate:

```text
Intent/deep link
exported Activity/Service/Receiver/Provider
PendingIntent
content URI/FileProvider
WebView navigation/JS bridge
notification action
Binder/native input
```

Kiểm tra scheme/host/path/ID, authorization sau navigation, URI grant tối thiểu và `android:exported` có chủ đích.

## 21.3 Token/session security là lifecycle problem

Token có expiry/refresh/revoke. Concurrent `401` cần single-flight refresh; logout cần vô hiệu session state, cancel/namespace pending work và không để response của account cũ update state account mới.

Không log token/PII. Telemetry schema phải có privacy review vì observability cũng là data export surface.

## 21.4 Certificate pinning có operational cost

Pinning chỉ dùng khi threat model biện minh và có rotation/recovery plan. Certificate/key thay đổi không được chuẩn bị có thể biến security control thành outage toàn app.

# 22. Performance, memory và battery: evidence before optimization

Performance engineering theo vòng:

```text
user-visible metric
→ reproduce trên representative device
→ trace/profile
→ hypothesis
→ one controlled change
→ measure lại
→ regression guard
```

Các metric khác nhau cần tool khác nhau:

```text
startup TTID/TTFD
frame time/jank
CPU hot path
allocation/GC/memory peak
DB latency/query plan
network latency/bytes
battery/background wakeup
APK/download size
```

Macrobenchmark phù hợp startup/interaction ở package level; Perfetto/System Trace nhìn thread/system timeline; memory profiler tìm retention/allocation; baseline profile cải thiện compiled hot path nhưng không sửa algorithm chậm.

## 22.1 Tail latency quan trọng hơn average đẹp

Average 8 ms không có nghĩa smooth nếu p95/p99 có frame 80–150 ms. Production telemetry nên segment theo device class/OS/network nếu metric nhạy với environment.

## 22.2 Memory leak = lifetime mismatch

Các pattern thường gặp:

```text
singleton giữ Activity/View
listener không unregister
Fragment binding sống sau onDestroyView
coroutine scope sống dài hơn owner
unbounded cache
callback/lambda capture object graph lớn
```

GC không thể thu object còn reachable. Debug bằng retention path thay vì gọi `System.gc()`.

## 22.3 Battery là scheduling + radio + sensor problem

Polling thường xuyên, location high accuracy liên tục, wakeup quá nhiều và retry storm đều tốn pin. Batch work, chọn constraint hợp lý, debounce/throttle khi đúng semantic và dừng sensor/camera/BLE theo lifecycle/resource ownership.

# 23. Networking nâng cao: failure taxonomy trước retry

Phân biệt:

```text
DNS/connectivity/timeout
TLS failure
HTTP protocol status
serialization/schema failure
auth/session failure
domain validation/conflict
ambiguous outcome sau side effect
```

Không map tất cả thành `NetworkError` rồi retry.

OkHttp interceptor chain có application/network interceptor với semantics khác. Token refresh cần tránh thundering herd khi nhiều request cùng `401`; mutex/single-flight có thể phù hợp nếu lock scope đúng.

Timeout cần phân biệt connect/read/write/call. Retry chỉ an toàn khi operation idempotent hoặc backend có idempotency key. Backoff nên có jitter ở fleet lớn để tránh nhiều client retry cùng lúc.

HTTP cache và application DB cache là hai layer khác nhau. Cache policy phải xác định freshness, validation và source of truth.

# 24. Database nâng cao: transaction là invariant boundary

Room transaction không chỉ để “chạy nhanh hơn”; nó bảo đảm nhóm write quan trọng commit/rollback cùng nhau.

```kotlin
@Transaction
suspend fun replaceData(...) { ... }
```

Nếu business invariant là entity update và outbox mutation phải cùng tồn tại, transaction phải bao quanh cả hai.

Index cần dựa trên query plan. Quá nhiều index tăng write/storage. Migration phải test bằng schema cũ + dữ liệu đại diện; destructive migration chỉ hợp với disposable cache nếu product chấp nhận mất dữ liệu.

Database lock/transaction dài có thể block resource dù API là suspend. Không đặt network call trong DB transaction. Sync cursor + downloaded page có thể cần cùng transaction để crash không tạo “cursor mới nhưng data chưa ghi”.

Rollback release cũng phải đọc được schema/data đã do version mới tạo nếu product muốn binary rollback thực sự khả thi.

# 25. Testing strategy: test invariant và failure order

Test pyramid Android nên tối đa hóa fast deterministic tests ở domain/data boundary, thêm integration test tại serialization/DB/DI/boundary, và UI/end-to-end test cho critical flows.

Fake thường tốt hơn mock cho stateful collaborator vì giữ behavior gần hệ thống thật. Mock phù hợp interaction hẹp.

Senior test không chỉ happy path. Cần chủ động điều khiển order:

```text
request A bắt đầu
request B bắt đầu
B success
A success muộn
→ assert A không overwrite B
```

Các failure test có giá trị cao:

```text
process death giữa flow
DB migration từ schema thực
network timeout sau remote commit
401 đồng thời
permission revoke
disk full / serialization corrupt nếu domain quan trọng
R8/minified release
rollback đọc data version mới
```

Compose UI test nên query semantics phản ánh meaning/accessibility thay vì chỉ testTag nếu có thể.

# 26. Java interoperability

Annotations quan trọng gồm `@JvmStatic`, `@JvmField`, `@JvmOverloads`, `@JvmName`, `@Throws`. Không dùng tự động; chỉ thêm khi Java caller cần API shape tương ứng.

SAM conversion hoạt động tốt với Java functional interface và Kotlin `fun interface`.

```kotlin
fun interface Listener {
    fun onEvent(value: String)
<!-- end merged variant -->
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

<!-- merge: preserve both canonical variants -->
`remember` cache theo composition lifetime/key, không phải global memoization. `derivedStateOf` hữu ích khi derived value thay đổi ít hơn source; dùng ở mọi chỗ tạo overhead không cần thiết.
<!-- merge: preserve both canonical variants -->
Public API cần document cả **behavioral contract**: threading, cancellation, ordering, replay, nullability, ownership và failure; type signature một mình chưa đủ.

# 28. Design patterns và Kotlin idioms
<!-- end merged variant -->

# 12. Side effects và lifetime

`LaunchedEffect(key)` restart coroutine khi key thay đổi. `DisposableEffect` cho resource cần register/unregister. `rememberUpdatedState` cập nhật callback/value mà không restart effect. `SideEffect` sync outward sau successful composition.

<!-- merge: preserve both canonical variants -->
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
<!-- merge: preserve both canonical variants -->
# 29. Legacy migration: strangler thay big-bang

Migration Java → Kotlin hoặc XML → Compose nên tạo seam và di chuyển incrementally.

Ví dụ:

```text
Rx repository cũ
→ adapter boundary expose Flow cho feature mới
→ migrate caller dần
→ đo/test
→ xóa Rx path khi không còn consumer
```

Hoặc:

```text
Fragment host cũ
→ ComposeView cho leaf screen mới
→ navigation/lifecycle vẫn giữ contract cũ
→ migrate screen theo risk/ownership
```

Mỗi migration phải có:

```text
behavior baseline
entry/exit criteria
coexistence contract
telemetry/test
rollback/fallback
owner
ngày/điều kiện xóa legacy
```

Convert source tự động không đồng nghĩa migration semantic hoàn tất.

# 30. Senior review checklist

Review theo chain thay vì theo framework:

```text
Requirement
→ invariant
→ owner/lifetime
→ source of truth
→ state transition
→ execution context
→ concurrency/ordering
→ external boundary
→ failure/retry/idempotency
→ persistence/reconstruction
→ security/privacy
→ performance budget
→ test evidence
→ build/artifact
→ rollout/rollback
```

Một feature chưa production-ready nếu chỉ trả lời “dùng MVVM + Hilt + Room + Compose” nhưng không giải thích được race, process death, stale data, retry, security boundary hoặc rollback.

---

## Senior Notes tổng kết

Code Android production bền không đến từ việc dùng nhiều library nhất mà từ việc đặt đúng ownership và giữ invariant. State thuộc ai, coroutine thuộc scope nào, database là source of truth hay cache, retry thuộc layer nào, error được map ở boundary nào, event có thực sự là event hay chỉ là state chưa model đúng, dependency sống bao lâu, và behavior nào phải survive process death. Seniority thể hiện ở khả năng trả lời rõ những câu hỏi đó trước khi bug xảy ra.

---
<!-- end merged variant -->

# 31. Channel, Mutex, atomic và shared mutable state

Coroutine không loại data race. `Mutex` phù hợp critical section suspend-aware; atomic cho operation nhỏ; Channel cho message hand-off/queue; actor/single-owner cho ordered mutation.

```kotlin
private val mutex = Mutex()
private var cached: Token? = null

suspend fun token(): Token = mutex.withLock {
    cached ?: refreshToken().also { cached = it }
}
```

<!-- merge: preserve both canonical variants -->
Ví dụ trên single-flight nhưng giữ lock trong network call. Tùy design có thể cần deferred-in-flight state để không giữ lock rộng. Primitive phải theo invariant, không theo template.

# 32. Coroutine scheduler, dispatcher injection và starvation

Blocking I/O, CPU-heavy và main-thread UI có execution need khác nhau. Dispatcher injection giúp test/main-safety nhưng không cần inject năm dispatcher vào mọi class.

Starvation xảy ra khi blocking work giữ pool thread, lock dài hoặc CPU parallelism vượt budget. Phân biệt coroutine `suspended` với thread `blocked` khi đọc profiler/stack trace.
<!-- merge: preserve both canonical variants -->
Ví dụ trên còn gợi ý pattern single-flight. Tuy nhiên nếu `refreshToken()` lâu hoặc re-enter dependency khác, phải xem lock scope để tránh contention/deadlock logic. Trước tiên giảm shared mutable state và xác định owner rồi mới chọn primitive.

`Channel` không thay thế Flow. Flow phù hợp stream/declarative transformation; Channel phù hợp queue/message hand-off. Tránh Channel như event bus toàn app vì ownership/backpressure khó kiểm soát.

# 32. Coroutine scheduler, dispatcher injection và starvation

`Dispatchers.IO` và `Dispatchers.Default` có mục đích khác nhau. Blocking I/O nên tách khỏi CPU-bound work. Đưa vòng lặp CPU nặng vào IO không biến nó thành I/O.

Dispatcher injection làm code testable và giúp data layer kiểm soát main-safety. Thread starvation có thể xảy ra khi blocking call trong pool nhỏ, lock quá lâu hoặc quá nhiều CPU work đồng thời. Khi profile, phân biệt coroutine suspend với thread blocked.

# 33. Compose performance: từ invalidation tới frame evidence
<!-- end merged variant -->

Recomposition count tự nó không phải bug. Compose có ba phase chính cho frame: composition → layout → draw, và Snapshot state read ở phase nào quyết định work có thể restart khi state đổi.

<!-- merge: preserve both canonical variants -->
Recomposition count không tự là bug. Quan tâm frame time, expensive composition/layout/draw, allocation và invalidation scope. `remember`/`derivedStateOf` chỉ dùng khi semantics đúng và measurement chỉ ra benefit.

# 34. Main thread, ANR, StrictMode và leak

UI thread xử lý input/lifecycle/draw orchestration. Disk/network, JSON parse, DB, bitmap decode hoặc lock contention đều có thể gây jank/ANR.

`StrictMode` hữu ích ở debug để phát hiện một số policy violation. Leak investigation cần retention path; `System.gc()` không sửa reachable reference.

# 35. R8, shrinking và keep rules

Reflection/JNI/name-based lookup có thể bị R8 ảnh hưởng. Keep rule phải hẹp. Library tự cần rule thì nên ship consumer rules. Release crash cần mapping đúng artifact để deobfuscate.

# 36. Signing, APK/AAB và release reproducibility

Release artifact phải ký. Quản lý signing/upload key như credential dài hạn. Reproducibility nghĩa trace được source commit, dependency versions, Gradle/JDK/toolchain/config đã tạo artifact.

# 37. API-level compatibility, behavior change và feature gating
<!-- merge: preserve both canonical variants -->
Expensive calculation trong composition cần được xem xét:

```kotlin
val sortedItems = remember(items) {
    items.sortedBy { it.title }
}
```

`remember` chỉ đúng nếu key phản ánh mutation semantics. `derivedStateOf` hữu ích khi input đổi thường xuyên nhưng output semantic đổi ít hơn.

Khi profile Compose, phân biệt composition cost, measure/layout, draw, allocation/GC, main-thread block, image/text cost và lazy list identity/reuse. Production correctness luôn đứng trước skip optimization.

# 34. Main thread, ANR, StrictMode và leak

Android UI thread xử lý input, lifecycle callback, drawing orchestration và nhiều callback framework. Blocking disk/network hoặc CPU work dài trên main có thể gây jank và ANR. JSON parse lớn, bitmap decode, DB transaction hoặc lock contention cũng có thể chặn main.

`StrictMode` trong debug build giúp phát hiện một số disk/network operation hoặc leaked closable object. Khi nghi leak, nhìn retention path bằng memory profiler/tooling; GC không thể thu object còn reachable.

ANR investigation nên kết hợp main-thread stack/thread dump, trace/Perfetto và context về binder/lock/I/O. Không “sửa ANR” bằng cách chuyển toàn bộ code sang IO nếu bottleneck thật là lock contention hoặc algorithm CPU.

# 35. R8, shrinking và keep rules

Release build có thể bật R8 để shrink, optimize và obfuscate. Reflection, JNI, serializer hoặc framework tìm class theo tên có thể bị ảnh hưởng nếu entry point không được model.

Keep rule phải càng hẹp càng tốt. Library Android nên cung cấp consumer rules nếu chính library cần. Sau obfuscation, release pipeline phải lưu/upload mapping đúng artifact để deobfuscate crash.

Failure forensic:

```text
debug pass + release fail
→ compare minify/resource shrink/BuildConfig/manifest/signing
→ inspect R8 diagnostics/mapping/usage
→ reproduce exact release variant
```

# 36. Signing, APK/AAB và release reproducibility

Android artifact release phải được ký. Release signing key/upload key là credential operational quan trọng.

Build reproducibility nghĩa release truy ra được source commit, dependency graph, wrapper/JDK/toolchain, variant, config, R8 mapping, native symbols và signing process.

AAB là publishing artifact; thiết bị thường nhận split APK phù hợp configuration. Vì vậy verify install/delivery path khi bug liên quan ABI/resource/language split, không chỉ inspect `.aab` upload.
<!-- end merged variant -->

`compileSdk` cho symbol compile-time; `minSdk` cho runtime floor; `targetSdk` opt-in platform behavior contract. Khi nâng target, phải audit behavior changes, không chỉ sửa số Gradle.

<!-- merge: preserve both canonical variants -->
API mới cần runtime guard/compat abstraction nếu minSdk thấp hơn. Platform latest và Play target requirement là hai khái niệm khác nhau.

# 38. WebView như một security boundary

Validate scheme/host/navigation. Cấu hình JavaScript/file access/debugging theo threat model. `addJavascriptInterface` chỉ cho trusted content và API tối thiểu. Token không nên nằm tùy tiện trong URL.

# 39. Database migration và schema evolution

Production migration phải bảo vệ data thật. Test từ nhiều schema version còn tồn tại, không chỉ previous → latest. Với sync app, local schema migration còn phải tương thích rollout backend/client lệch version.
<!-- merge: preserve both canonical variants -->
`minSdk`, `compileSdk`, `targetSdk` là ba contract khác nhau. Code gọi API mới trên OS cũ cần guard hoặc compat abstraction.

Nâng `targetSdk` là behavior migration: test notification, permission, background execution, storage, window/insets, exported component và policy thay đổi. Nên tách target migration khỏi Kotlin/AGP migration khi có thể để forensic rõ.

Tại baseline này Android 17 là API 37, trong khi Play target requirement có thể thấp hơn latest platform. Latest SDK và distribution requirement không phải cùng một khái niệm.

# 38. WebView như một security boundary

WebView kết hợp web security model với native app privilege. Validate external URL scheme/host, quyết định domain nào được ở trong WebView, hạn chế file access/JS/debugging theo threat model và cực kỳ thận trọng với `addJavascriptInterface`.

Authentication token không nên nhét tùy tiện vào URL. Certificate pinning chỉ dùng khi có operational plan cho rotation/recovery.

# 39. Database migration và schema evolution trong production

Room migration phải coi dữ liệu người dùng là tài sản. Test từ schema cũ thực tế, insert dữ liệu đại diện, chạy migration rồi verify schema + data.

Với staged rollout, app version cũ và mới có thể cùng tồn tại. Local data, remote payload và server behavior phải có compatibility window. Nếu migration irreversible, binary rollback có thể không cứu được user đã mở app version mới.
<!-- end merged variant -->

# 40. Production failure model và Senior decision framework

<!-- merge: preserve both canonical variants -->
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
<!-- merge: preserve both canonical variants -->
Mobile production không chạy theo happy path. Một feature nên được review với failure matrix:

```text
Process
- configuration recreate
- process kill
- app update
- device reboot

Concurrency
- duplicate tap
- request A/B out of order
- 401 storm
- worker + foreground UI cùng mutate

Network
- offline
- timeout trước commit
- timeout sau remote commit
- partial payload/schema drift

Persistence
- migration
- disk full/corrupt data
- transaction partiality
- rollback binary đọc schema mới

Platform
- permission revoke
- targetSdk behavior change
- OEM/WebView difference
- background restriction

Release
- R8-only failure
- ABI/split issue
- bad remote config
- staged rollout regression
```

Sau đó hỏi theo chuỗi:

```text
state thuộc owner nào?
lifetime bao lâu?
source of truth ở đâu?
operation blocking hay suspend?
ordering được định nghĩa chưa?
retry có an toàn/idempotent không?
process death reconstruct thế nào?
input nào untrusted?
performance budget nào cần đo?
test nào chứng minh invariant?
telemetry nào phát hiện regression?
rollback/fallback có thật sự khả thi không?
```

Nếu những câu hỏi này có đáp án rõ, lựa chọn MVVM/MVI, Hilt/Koin, Room/SQLDelight hoặc Retrofit/Ktor thường trở thành quyết định kỹ thuật dễ lý giải hơn.
<!-- end merged variant -->
