# Kotlin + Android Master Note — Advanced / Senior

> Mục tiêu: hiểu sâu semantics của Kotlin, concurrency, Compose runtime, performance, architecture, testing, modularization, interoperability và các quyết định production mà một Senior Android Engineer phải kiểm soát.

## Mục lục

1. Kotlin type system nâng cao
2. Inline, noinline, crossinline và reified
3. Operator overloading và DSL
4. Contracts và compiler reasoning
5. Reflection, annotations và code generation
6. Coroutines internals và cancellation
7. Exception propagation trong coroutine
8. Flow internals, backpressure và sharing
9. State machine và unidirectional data flow
10. Compose runtime và recomposition
11. Stability, snapshot state và performance
12. Side effects đúng cách
13. Android lifecycle/process death
14. SavedStateHandle
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
29. Legacy migration
30. Senior review checklist

---

# 1. Kotlin type system nâng cao

Kotlin type system có nullable types, bottom type `Nothing`, top types `Any`/`Any?`, generic variance, intersection-like smart cast và platform types từ Java. Senior developer cần hiểu platform type vì đây là nơi null-safety có thể bị xuyên thủng.

Khi Java method trả `String` không có nullability annotation, Kotlin có thể coi nó như platform type `String!`. Compiler cho phép dùng linh hoạt hơn nhưng trách nhiệm runtime thuộc về bạn. Do đó Java boundary nên được normalize sớm:

```kotlin
val safeName: String = javaApi.name ?: "Unknown"
```

Không nên để platform type chảy sâu vào domain model.

`Nothing?` về lý thuyết có thể chứa `null`; `Nothing` không có instance bình thường. Hiểu bottom type giúp đọc type inference trong `throw`, `return`, `error()` và generic expression.

# 2. `inline`, `noinline`, `crossinline`, `reified`

Higher-order function tạo lambda object/call overhead trong một số trường hợp. `inline` cho phép compiler inline body tại call site, đồng thời mở khả năng non-local return từ lambda inline.

```kotlin
inline fun <T> measure(block: () -> T): T {
    val start = System.nanoTime()
    return block()
}
```

`noinline` giữ một lambda parameter không inline khi cần lưu/pass như object. `crossinline` cấm non-local return khi lambda sẽ được gọi trong context khác.

`reified` chỉ dùng cho type parameter của inline function và cho phép truy cập type ở runtime-like call site mà không phải truyền `Class<T>` thủ công.

```kotlin
inline fun <reified T> Json.decode(text: String): T = ...
```

Không dùng `inline` khắp nơi vì code size có thể tăng. Nó phù hợp API nhỏ, higher-order hot path hoặc cần `reified`/non-local return.

# 3. Operator overloading và DSL

Kotlin map syntax operator sang function có tên quy ước như `plus`, `get`, `set`, `contains`, `invoke`, `compareTo`.

```kotlin
operator fun Money.plus(other: Money): Money = ...
```

Operator overloading chỉ nên dùng khi semantics thực sự trực quan. `a + b` mà thực chất gọi network hoặc mutate database là API gây bất ngờ.

Type-safe DSL dựa nhiều vào lambda with receiver, extension và builder pattern.

```kotlin
html {
    body {
        text("Hello")
    }
}
```

Compose bản chất cũng tận dụng khả năng DSL-like của Kotlin, nhưng runtime/compiler semantics phức tạp hơn builder DSL thông thường.

# 4. Contracts

Kotlin contracts giúp compiler hiểu quan hệ giữa call và program state trong một số API. Đây là tính năng nâng cao; không nên tạo custom contract nếu chưa hiểu effect system và giới hạn compiler.

Một số standard functions như `requireNotNull` có semantics giúp smart cast/flow analysis.

# 5. Reflection, annotations và code generation

Reflection Kotlin/JVM cho phép inspect class/property/function runtime, nhưng có overhead và dependency `kotlin-reflect` nếu dùng full reflection. Android production thường ưu tiên code generation/KSP khi có thể vì startup, size và obfuscation predictability.

KSP là API xử lý symbol dành cho Kotlin tooling, được nhiều library dùng để generate code. KAPT dựa trên Java annotation processing và từng là lựa chọn phổ biến; codebase mới thường ưu tiên KSP nếu library hỗ trợ.

# 6. Coroutine internals và cancellation

`suspend` không tự tạo thread. Compiler biến suspend function thành state machine với continuation. Tại suspension point, state được lưu; coroutine có thể resume sau mà không giữ thread blocked.

Cancellation trong coroutine là cooperative. Code CPU loop dài không gọi suspend function cần tự kiểm tra:

```kotlin
while (...) {
    ensureActive()
    computeChunk()
}
```

Không được swallow `CancellationException`:

```kotlin
try {
    work()
} catch (e: CancellationException) {
    throw e
} catch (e: IOException) {
    ...
}
```

Android guidance nhấn mạnh việc làm coroutine cancellable và tránh generic catch phá cancellation.

# 7. Exception propagation

Với `launch`, uncaught exception có thể được xử lý như uncaught exception của coroutine hierarchy và có thể crash tùy scope/handler. Với `async`, exception được giữ trong `Deferred` và rethrow khi `await`, nhưng parent hierarchy vẫn có propagation semantics.

`SupervisorJob`/`supervisorScope` cho phép sibling độc lập về failure, nhưng không phải “tắt exception”. Bạn vẫn cần quyết định ai log, ai retry, ai chuyển thành state.

`CoroutineExceptionHandler` chỉ là last-resort handler cho uncaught exception ở phù hợp coroutine context; không thay thế `try/catch` cho business error.

# 8. Flow internals, buffering và sharing

Flow mặc định sequential: emitter và downstream operator phối hợp theo suspension. Khi collector chậm, upstream cũng bị chậm trừ khi buffer/concurrency operator thay đổi pipeline.

`buffer()` tách producer/consumer bằng buffer. `conflate()` bỏ qua intermediate value và giữ value mới khi consumer chậm. `collectLatest` cancel block xử lý value trước khi value mới đến. `flatMapLatest` cancel upstream sub-flow cũ khi key mới đến; phù hợp search query.

```kotlin
queryFlow
    .debounce(300)
    .distinctUntilChanged()
    .flatMapLatest(repository::search)
```

`stateIn` và `shareIn` chuyển cold flow thành hot shared flow trong một scope. `SharingStarted.WhileSubscribed(...)` thường hợp UI nhưng timeout/replay phải được hiểu, không copy template máy móc.

# 9. State machine và UDF

UI phức tạp dễ rơi vào impossible states nếu dùng nhiều flags:

```kotlin
loading=true, success=true, error=true
```

Một state machine model rõ phase và transition. Unidirectional Data Flow có dạng:

```text
State -> UI -> Event -> Reducer/Handler -> New State
```

Không nhất thiết phải dùng MVI framework. Điều quan trọng là state ownership và transition deterministic.

# 10. Compose runtime và recomposition

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

Ví dụ:

```kotlin
@Composable
fun UserList(users: List<User>) {
    users.forEach { user ->
        UserRow(user)
    }
}
```

Nếu list thay đổi thứ tự, positional identity có thể làm runtime phải làm nhiều việc hơn và effect/state gắn item khó theo đúng entity. Với lazy list, stable key tạo identity rõ:

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

Key phải biểu diễn **identity bền vững**, không phải index nếu index thay đổi khi insert/delete/reorder.

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

Compose theo dõi **nơi đọc state**, không chỉ nơi state được tạo.

Composition read:

```kotlin
var padding by remember { mutableStateOf(8.dp) }
Text(
    "Hello",
    Modifier.padding(padding) // read khi dựng modifier trong composition
)
```

Khi `padding` đổi, composition scope liên quan phải chạy lại.

Layout-placement read có thể tránh composition:

```kotlin
Modifier.offset {
    IntOffset(offsetX.roundToPx(), 0)
}
```

Nếu `offsetX` được đọc trong placement lambda, thay đổi có thể chỉ invalidate layout/placement.

Draw read:

```kotlin
Modifier.drawBehind {
    drawRect(color = animatedColor)
}
```

Nếu state chỉ được đọc trong draw, runtime có thể chỉ chạy draw phase.

Senior optimization không phải chuyển mọi read xuống phase thấp nhất bằng mẹo khó đọc; nó là hiểu hot path để tránh recomposition/layout không cần thiết khi profiler chứng minh vấn đề.

## 10.4 Composable body phải gần pure

Composable có thể chạy lại, bị skip hoặc một composition attempt có thể không được apply. Vì vậy body không phải nơi gọi side effect tùy ý:

```kotlin
@Composable
fun Bad(userId: String) {
    repository.load(userId) // sai: side effect trong composition
}
```

UI body nên chủ yếu mô tả output từ input/state. Business side effect thuộc event handler/ViewModel/data layer; effect gắn lifecycle UI dùng Effect API phù hợp.

# 11. Snapshot State, stability và performance

Compose Snapshot system cung cấp observable state model cho runtime. Khi code đọc một `State<T>` trong restart scope, runtime có thể theo dõi dependency đó; khi write hợp lệ thay đổi value, những scope đã đọc nó có thể bị invalidated.

Ordinary Kotlin mutation không tự trở thành observable:

```kotlin
val users = mutableListOf<User>()
users += newUser // Compose không tự biết list này đã đổi nếu list không nằm trong observable state model phù hợp
```

Một pattern an toàn hơn là immutable snapshot được publish qua observable holder:

```kotlin
var users by mutableStateOf<List<User>>(emptyList())
    private set

fun add(user: User) {
    users = users + user
}
```

hoặc dùng `SnapshotStateList` khi mutable collection semantics là chủ đích. Điều quan trọng là runtime phải nhìn thấy mutation contract.

## 11.1 Stability không đồng nghĩa immutability

**Immutable** nghĩa state quan sát được của object không đổi sau construction theo contract. **Stable** trong Compose là contract rộng hơn giúp compiler/runtime reasoning về việc input có thay đổi quan sát được không.

Không annotate `@Stable` hoặc `@Immutable` chỉ để benchmark đẹp. Nếu object thực tế mutate theo cách Compose không thể quan sát nhưng bạn tuyên bố stable, runtime có thể skip công việc cần thiết và tạo correctness bug.

Correctness > skip rate.

## 11.2 Parameter equality và granularity

Nếu một root `ScreenState` khổng lồ đổi object mỗi khi timer/scroll nhỏ thay đổi, nhiều subtree có thể bị invalidated dù chỉ một vùng quan tâm value đó. Ngược lại, chia state thành hàng trăm holder nhỏ có thể làm ownership khó hiểu.

Granularity tốt xuất phát từ semantic ownership:

```text
state nào thay đổi cùng nhau?
subtree nào thật sự đọc field nào?
field nào derived từ source khác?
update frequency khác nhau bao nhiêu?
```

Không tối ưu bằng cách “split mọi state” trước khi đo.

## 11.3 `derivedStateOf` dùng khi derived result đổi ít hơn input

Ví dụ scroll index thay đổi liên tục nhưng UI chỉ cần biết đã qua item đầu hay chưa:

```kotlin
val showScrollToTop by remember {
    derivedStateOf {
        listState.firstVisibleItemIndex > 0
    }
}
```

`derivedStateOf` có overhead. Không dùng cho phép nối string đơn giản chỉ vì value được tính từ state khác.

## 11.4 `remember` cache theo identity/key, không phải cache toàn cục

```kotlin
val sortedItems = remember(items) {
    items.sortedBy { it.title }
}
```

Cách này hợp lý nếu sorting đủ đáng kể và `items` có immutable/replacement semantics rõ. Nếu list bị mutate in-place nhưng reference không đổi, key `items` không thể tự biểu diễn mutation mà runtime không quan sát được.

## 11.5 Lazy list: key, content type và mutation

Stable key giúp item giữ identity qua reorder; `contentType` có thể giúp lazy container reuse item structure phù hợp. Nhưng key không chữa data model sai. Nếu hai item có cùng key hoặc key thay theo position, state/effect có thể gắn nhầm entity.

## 11.6 Performance phải đo theo frame, không theo trực giác

Các câu hỏi đúng:

```text
frame nào jank?
composition, measure/layout hay draw tốn thời gian?
allocation/GC có spike không?
expensive calculation có nằm trong composition không?
list có item identity ổn định không?
main thread có bị I/O/lock chặn không?
```

Dùng tracing/profiling/Macrobenchmark/Compose tooling theo vấn đề. Recomposition là một tín hiệu; không phải KPI duy nhất.

# 12. Side effects đúng cách

Compose effect API tồn tại vì composable body nên side-effect free. Chọn effect theo **lifetime và cleanup contract**, không theo việc “snippet nào chạy được”.

## 12.1 `LaunchedEffect`: coroutine sống cùng call site + key

```kotlin
LaunchedEffect(userId) {
    analytics.trackScreen(userId)
}
```

Khi effect vào Composition, coroutine được launch. Khi call site rời Composition, coroutine bị cancel. Khi key đổi, coroutine cũ bị cancel và block chạy lại với key mới.

Nếu operation phải tiếp tục sau khi screen rời Composition, đây thường là owner sai; ViewModel/application/WorkManager có thể phù hợp hơn tùy lifetime.

## 12.2 Constant key không có nghĩa “một lần toàn app”

```kotlin
LaunchedEffect(Unit) { ... }
```

nghĩa là effect không restart vì key đổi trong **lifetime hiện tại của call site**. Nếu call site rời Composition rồi quay lại, effect chạy lại. Vì vậy `LaunchedEffect(Unit)` không phải lifecycle toàn process.

## 12.3 `rememberUpdatedState`: latest value nhưng giữ effect lifetime

Nếu callback thay đổi qua recomposition nhưng ta không muốn restart delay/subscription dài:

```kotlin
val currentOnTimeout by rememberUpdatedState(onTimeout)

LaunchedEffect(Unit) {
    delay(3_000)
    currentOnTimeout()
}
```

Tách hai vấn đề:

```text
lifetime/restart của effect
!=
latest value effect cần đọc
```

## 12.4 `DisposableEffect`: acquire/release external resource

Phù hợp listener/observer cần cleanup:

```kotlin
DisposableEffect(lifecycleOwner) {
    val observer = LifecycleEventObserver { _, event ->
        // ...
    }
    lifecycleOwner.lifecycle.addObserver(observer)

    onDispose {
        lifecycleOwner.lifecycle.removeObserver(observer)
    }
}
```

Key đổi hoặc call site rời Composition thì cleanup cũ chạy trước khi resource mới được gắn. `onDispose {}` rỗng thường là dấu hiệu effect API khác phù hợp hơn.

## 12.5 `SideEffect`: publish sau successful composition

`SideEffect` phù hợp đồng bộ Compose state sang object ngoài Compose sau khi composition đã apply thành công. Không dùng nó cho network request hay work cần coroutine.

## 12.6 `produceState` và `snapshotFlow`

`produceState` hữu ích bridge producer async/callback thành Compose State khi ownership thực sự thuộc UI boundary.

`snapshotFlow` quan sát Snapshot state read trong block và biến change thành Flow, hữu ích cho analytics/stream transformation:

```kotlin
LaunchedEffect(listState) {
    snapshotFlow { listState.firstVisibleItemIndex }
        .distinctUntilChanged()
        .collect { index ->
            analytics.onVisibleIndex(index)
        }
}
```

Đừng dùng `snapshotFlow` để vòng ngược mọi Compose state sang ViewModel; nếu domain state vốn đã là Flow, giữ source ở layer gốc thường đơn giản hơn.

## 12.7 `rememberCoroutineScope`: coroutine từ event handler

Một event như bấm nút để show Snackbar cần coroutine nhưng không nhất thiết là effect của state:

```kotlin
val scope = rememberCoroutineScope()

Button(onClick = {
    scope.launch {
        snackbarHostState.showSnackbar("Saved")
    }
}) {
    Text("Save")
}
```

Scope này vẫn gắn với Composition. Không dùng để khởi chạy durable business work phải sống lâu hơn UI.

## 12.8 Effect review checklist

Với mỗi effect, hỏi:

```text
điều gì tạo identity của effect?
key nào phải restart nó?
value nào chỉ cần latest mà không restart?
cleanup ở đâu?
leaving composition có phải cancel work không?
operation này thật sự là UI side effect hay business command?
process death/re-entry có chạy lặp nguy hiểm không?
```

Nếu không trả lời được, effect đang dựa vào may mắn hơn là lifecycle contract.

# 13. Lifecycle, configuration change và process death

Configuration change thường recreate Activity nhưng ViewModel có thể sống qua recreation. Process death khác hoàn toàn: OS kill process, toàn bộ in-memory state mất. Nếu state phải restore, cần persistence/SavedStateHandle/rememberSaveable tùy loại dữ liệu.

Đừng lưu object lớn hoặc dữ liệu có thể reload vào Bundle. Bundle có giới hạn Binder transaction; stable IDs và persistence tốt hơn.

# 14. SavedStateHandle

`SavedStateHandle` cho ViewModel state cần phục hồi sau process recreation theo capability của saved state. Nó không phải database. Chỉ lưu dữ liệu nhỏ, serializable/savable hoặc identifier cần để reconstruct screen.

# 15. Multi-module architecture

Module hóa giúp enforce dependency, tăng parallel build/caching và ownership, nhưng quá nhiều module tạo build overhead và complexity. Module boundary có thể theo feature (`feature:home`, `feature:checkout`) và core (`core:model`, `core:network`, `core:database`, `core:designsystem`).

Feature module không nên phụ thuộc vòng. Public API của module nên nhỏ. Internal implementation nên dùng `internal` khi phù hợp.

# 16. Gradle và build performance

Các khái niệm cần nắm: Gradle configuration phase, task graph, build cache, configuration cache, incremental compilation, KSP/KAPT cost, dependency resolution, build variants, product flavors, build types.

Không chạy logic I/O tùy tiện trong Gradle configuration. Dependency version nên centralize. Tránh dynamic version như `1.+` vì build khó reproducible.

# 17. DI ở quy mô lớn

Hilt/Dagger compile-time graph giúp verify dependency. Scope phải map đúng lifecycle. `@Singleton` không nên dùng chỉ vì “đỡ tạo object”. Một object stateful vô tình singleton có thể leak state giữa user/session.

Assisted injection hữu ích khi một số parameter runtime không nằm trong graph. Multibinding hữu ích plugin architecture/handler registry.

# 18. Offline-first, cache và sync

Offline-first thường chọn local DB làm source of truth. Repository observe local data, refresh từ network, merge theo conflict policy, rồi write local. Sync cần xử lý idempotency, retry, ordering, conflict và auth expiration.

Không đủ khi chỉ “cache response 5 phút”. Cần xác định freshness policy, stale-while-revalidate, ownership của timestamp, và hành vi khi partial failure.

# 19. Paging 3

Paging 3 giúp load dữ liệu theo trang từ database/network. `Pager`, `PagingSource`, `RemoteMediator` là các abstraction chính. `RemoteMediator` phù hợp khi network + DB kết hợp và DB là source of truth.

UI cần handle refresh/append/prepend load states độc lập. Sai lầm thường gặp là biến mọi error thành full-screen error dù chỉ append page fail.

# 20. Background execution policy

Android giới hạn background ngày càng chặt. Chọn công cụ theo semantic: coroutine trong ViewModel cho work gắn màn hình; foreground service cho user-visible ongoing task có yêu cầu rõ; WorkManager cho deferrable guaranteed work; exact alarm chỉ cho use case đủ điều kiện; push notification/FCM cho server-triggered signal.

Không dùng Service chỉ vì “cần thread nền”. Service không phải thread.

# 21. Security production

Threat model phải xem attacker có thể decompile APK, hook runtime, MITM thiết bị compromised, steal token hoặc exploit exported component. Không dựa vào obfuscation như biện pháp bảo mật duy nhất.

Kiểm tra `android:exported`, deep link validation, PendingIntent mutability, WebView settings, JavaScript bridge, file URI/content URI, certificate pinning trade-off, Keystore và token lifetime.

WebView đặc biệt nguy hiểm nếu load content không tin cậy cùng JS bridge. `addJavascriptInterface` cần threat model nghiêm ngặt.

# 22. Performance, memory và battery

Các nhóm performance chính: startup, frame rendering/jank, memory, network, database và battery. Dùng Android Profiler, Perfetto, Macrobenchmark, Baseline Profiles, Layout Inspector/Compose tooling tùy vấn đề.

Memory leak thường đến từ listener không unregister, coroutine scope sống quá lâu, singleton giữ Activity/View, Fragment binding giữ sau `onDestroyView`, callback capture reference và cache không bounded.

# 23. Networking nâng cao

OkHttp interceptor chain có application interceptor và network interceptor với semantics khác. Authentication refresh cần tránh thundering herd khi nhiều request cùng nhận 401. Có thể serialize token refresh bằng mutex/single-flight pattern.

Timeout cần phân biệt connect/read/write/call. Retry chỉ an toàn khi operation idempotent hoặc backend hỗ trợ idempotency key.

# 24. Database nâng cao

Room transaction:

```kotlin
@Transaction
suspend fun replaceData(...) { ... }
```

Index cần dựa trên query pattern. Too many indexes làm write chậm và tăng storage. Migration phải test bằng exported schema/migration test khi production data quan trọng.

Database operation cần hiểu thread/concurrency; Room suspend/Flow hỗ trợ tốt nhưng transaction dài vẫn block database resources.

# 25. Testing strategy

Test pyramid Android thực tế nên tối đa hóa fast deterministic tests ở domain/data boundary, thêm integration test nơi serialization/DB/DI cần xác minh, và giữ UI/end-to-end test cho critical flows.

Fake thường tốt hơn mock cho stateful collaborator vì behavior gần thực tế hơn. Mock phù hợp verify interaction hẹp. Tránh test implementation detail như “method A phải gọi method B đúng 1 lần” nếu contract chỉ yêu cầu output state.

Compose UI test nên query bằng semantics/testTag khi cần, nhưng ưu tiên semantics phản ánh accessibility/meaning.

# 26. Java interoperability

Annotations quan trọng gồm `@JvmStatic`, `@JvmField`, `@JvmOverloads`, `@JvmName`, `@Throws`. Không dùng tự động; chỉ thêm khi Java caller cần API shape tương ứng.

SAM conversion hoạt động tốt với Java functional interface và Kotlin `fun interface`.

```kotlin
fun interface Listener {
    fun onEvent(value: String)
}
```

# 27. API design bằng Kotlin

Public API nên ưu tiên type safety, immutability, explicit ownership và predictable failure semantics. Tránh boolean parameter khó đọc:

```kotlin
send(true, false)
```

Tốt hơn dùng enum/options object hoặc named arguments nếu internal Kotlin-only API.

Builder chỉ cần khi constructor/named defaults không đủ. Kotlin data class + default parameter thường loại bỏ boilerplate builder Java.

# 28. Design patterns và Kotlin idioms

Nhiều GoF pattern được Kotlin làm nhẹ hơn. Strategy có thể là function type thay vì hierarchy class. Singleton có `object`. Builder có DSL/named/default args. Decorator có delegation. Observer thường biểu diễn bằng Flow. State pattern có sealed hierarchy/reducer.

Không áp pattern vì tên nghe “senior”. Pattern là giải pháp cho force cụ thể. Nếu language feature làm vấn đề biến mất, đừng dựng class graph chỉ để giống sách.

# 29. Legacy migration

Migration Java -> Kotlin nên incremental, không “Convert Java File to Kotlin” rồi coi là xong. Code convert tự động thường giữ Java idiom: nullable rộng, mutable collection, companion boilerplate, platform type chưa normalize.

Migration XML -> Compose cũng nên incremental. Có thể giữ Fragment navigation, chuyển từng leaf screen sang ComposeView, sau đó cân nhắc nâng architecture. Rewrite big-bang tăng regression risk.

# 30. Senior review checklist

Một review senior không chỉ nhìn syntax. Cần kiểm tra state ownership; cancellation; lifecycle; error semantics; idempotency; retry; persistence; null boundary; thread safety; source of truth; testability; security; accessibility; performance; observability; backward compatibility; migration cost; API contract; module dependency; build impact.

---

## Senior Notes tổng kết

Code Android production bền không đến từ việc dùng nhiều library nhất mà từ việc đặt đúng ownership. State thuộc ai, coroutine thuộc scope nào, database là source of truth hay cache, retry thuộc layer nào, error được map ở boundary nào, event có thực sự là event hay chỉ là state chưa model đúng, dependency sống bao lâu, và behavior nào phải survive process death. Seniority thể hiện ở khả năng trả lời rõ những câu hỏi đó trước khi bug xảy ra.

---

# 31. Channel, Mutex, atomic và shared mutable state

Coroutine giúp viết concurrency dễ đọc hơn nhưng không tự loại bỏ data race. Nếu nhiều coroutine truy cập shared mutable state trên nhiều thread, bạn vẫn cần synchronization. `Mutex` là primitive coroutine-friendly cho critical section có thể suspend; `Channel` mô hình hóa việc truyền message giữa producer/consumer; atomic primitive phù hợp cho operation nhỏ không cần suspension.

```kotlin
private val mutex = Mutex()
private var cached: Token? = null

suspend fun token(): Token = mutex.withLock {
    cached ?: refreshToken().also { cached = it }
}
```

Ví dụ trên còn gợi ý pattern **single-flight**: nhiều caller cùng cần token mới nhưng chỉ một refresh chạy. Tuy nhiên nếu `refreshToken()` có thể lâu hoặc re-enter dependency khác, phải xem xét lock scope để tránh contention/deadlock logic. Senior engineer không chọn Mutex vì “có concurrency”; trước tiên cần giảm shared mutable state, xác định owner, rồi mới dùng primitive phù hợp.

`Channel` không thay thế Flow. Flow phù hợp mô hình stream/declarative transformation; Channel phù hợp queue/message hand-off. Đặc biệt tránh dùng Channel như event bus toàn app vì ownership và backpressure nhanh chóng trở nên khó kiểm soát.

# 32. Coroutine scheduler, dispatcher injection và starvation

`Dispatchers.IO` và `Dispatchers.Default` đều dùng thread pools được quản lý, nhưng có mục đích khác nhau. Blocking I/O nên tách khỏi CPU-bound work để không làm nghẽn compute pool. Ngược lại, đưa vòng lặp CPU nặng vào IO không biến nó thành “I/O”.

Dispatcher injection làm code testable và giúp library/data layer kiểm soát main-safety. Tuy nhiên abstraction quá mức như inject năm dispatcher vào mọi class cũng tạo ceremony. Một pattern thực tế là định nghĩa một `DispatcherProvider` ở boundary lớn, hoặc inject dispatcher trực tiếp cho component thật sự cần chuyển context.

Thread starvation có thể xảy ra khi code dùng blocking call trong pool nhỏ, giữ lock quá lâu hoặc tạo quá nhiều công việc CPU đồng thời. Khi điều tra performance, phải phân biệt coroutine đang **suspend** với thread đang **blocked**; stack trace và profiler thể hiện hai hiện tượng khác nhau.

# 33. Compose performance: từ invalidation tới frame evidence

Recomposition count tự nó không phải bug. Compose có ba phase chính cho frame: **composition → layout → draw**, và Snapshot state read ở phase nào sẽ quyết định scope công việc có thể bị restart khi state đổi. Vì vậy Senior review phải hỏi “state này được đọc ở phase nào?” trước khi cố giảm mọi recomposition.

Ví dụ animation chỉ thay đổi offset có thể đọc state trong placement lambda; color animation có thể đọc trong draw block. Nếu đọc cùng value khi dựng modifier trong composition, phạm vi invalidation có thể rộng hơn. Nhưng chỉ chuyển read xuống layout/draw khi code vẫn rõ và profiling chứng minh hot path.

Expensive calculation trong composition cần được xem xét:

```kotlin
val sortedItems = remember(items) {
    items.sortedBy { it.title }
}
```

`remember` chỉ đúng nếu key phản ánh mutation semantics. Nếu `items` bị mutate in-place mà reference không đổi, cache có thể stale. Immutable replacement làm state/equality reasoning đơn giản hơn.

`derivedStateOf` hữu ích khi input đổi thường xuyên nhưng output semantic đổi ít hơn, ví dụ scroll index → `showScrollToTop`. Nó không phải helper bắt buộc cho mọi computed value.

Khi profile Compose, phân biệt:

```text
composition cost
measure/layout cost
draw cost
allocation + GC
main-thread blocking
image/text cost
lazy list identity/reuse
```

Một composable recompose nhiều nhưng mỗi lần cực rẻ có thể không đáng tối ưu. Một composable hiếm recompose nhưng mỗi lần sort/parse hàng nghìn item trên Main mới là vấn đề lớn.

Production correctness luôn đứng trước skip optimization. Không dùng annotation stability sai contract, không mutate model âm thầm, không tạo key giả chỉ để giảm metric.

# 34. Main thread, ANR, StrictMode và leak

Android UI thread xử lý input, lifecycle callback, drawing orchestration và nhiều callback framework. Blocking disk/network hoặc CPU work dài trên main có thể gây jank và **ANR**. Không phải mọi freeze đều do network; JSON parse lớn, database transaction, bitmap decode hoặc lock contention cũng có thể chặn main.

`StrictMode` trong debug build giúp phát hiện một số disk/network operation hoặc leaked closable object. Memory leak thường đến từ object sống lâu giữ reference đến Activity/View/Context sống ngắn: singleton giữ Activity, callback không unregister, coroutine scope sai owner hoặc ViewBinding của Fragment không clear đúng lifecycle là ví dụ kinh điển.

Khi nghi leak, cần nhìn retention path bằng memory profiler/tooling thay vì thêm `System.gc()`. GC không thể thu hồi object còn reachable.

# 35. R8, shrinking và keep rules

Release build có thể bật R8 để shrink, optimize và obfuscate. Code dùng reflection, JNI, serializer cũ hoặc framework tìm class theo tên có thể bị ảnh hưởng nếu R8 không biết entry point. Keep rule phải càng hẹp càng tốt; rule kiểu `-keep class ** { *; }` vô hiệu hóa phần lớn lợi ích và che giấu dependency reflection không được model rõ.

Library Android nên cung cấp **consumer rules** nếu chính library yêu cầu keep rule. App không nên phải đoán internals của dependency. Sau obfuscation, crash stack trace cần mapping file để deobfuscate; release pipeline phải lưu/upload mapping tương ứng artifact.

# 36. Signing, APK/AAB và release reproducibility

Android artifact release phải được ký. Debug keystore chỉ dành cho development. Release signing key cần quản lý như credential quan trọng; mất key hoặc để lộ key có hậu quả dài hạn. Với Play App Signing, Google quản lý app signing key trong service, còn team thường quản lý upload key, nhưng quy trình rotate/recovery vẫn phải được document.

Build reproducibility nghĩa một release có thể truy ra source commit, dependency versions, Gradle wrapper, JDK/toolchain, signing process và configuration đã tạo artifact. Không dùng dynamic version kiểu `1.+` cho production dependency vì build cùng commit ở hai ngày khác nhau có thể khác nhau.

# 37. API level compatibility, behavior change và feature gating

Ba khái niệm `minSdk`, `compileSdk`, `targetSdk` phải được hiểu ở cấp Senior. `compileSdk` quyết định symbol API nào compiler nhìn thấy; `minSdk` quyết định thiết bị thấp nhất có thể cài; `targetSdk` opt-in nhiều behavior change của platform và chịu policy distribution.

Code gọi API mới trên thiết bị cũ phải guard bằng API check hoặc abstraction đã xử lý compatibility. Khi nâng targetSdk, không chỉ sửa số Gradle rồi build. Cần đọc behavior changes của từng Android version, test notification/permission/background execution/storage/window/insets và các API nhạy cảm với platform policy.

Tại thời điểm tài liệu được cập nhật (2026-09-20), Android 17 là API 37. Google Play yêu cầu app mới và update thông thường từ 2026-08-31 phải target Android 16 / API 36 trở lên. Hai con số này minh họa rằng “latest platform API” và “minimum Play target requirement” là hai khái niệm khác nhau.

# 38. WebView như một security boundary

WebView kết hợp web security model với native app privilege. URL từ external input phải validate scheme/host; navigation cần quyết định domain nào được phép ở lại trong WebView; file access, mixed content, JavaScript và debugging phải được cấu hình theo threat model. `addJavascriptInterface` có thể mở native capability cho JavaScript, vì vậy chỉ expose API tối thiểu cho content đáng tin cậy.

Authentication token không nên nhét tùy tiện vào URL vì URL có thể đi vào log/history/referrer. Cookie/session, custom header và OAuth redirect cần thiết kế cùng backend. Certificate pinning chỉ dùng khi có operational plan cho certificate rotation; pin sai có thể làm toàn bộ app mất kết nối khi backend đổi certificate.

# 39. Database migration và schema evolution trong production

Room migration phải coi dữ liệu người dùng hiện có là tài sản, không phải sample database có thể xóa. Mỗi schema change cần migration path được test từ các version thực tế còn tồn tại. Destructive migration chỉ phù hợp nếu dữ liệu thật sự disposable/cache và product chấp nhận mất dữ liệu.

Migration test nên tạo database ở schema cũ, insert dữ liệu đại diện, chạy migration rồi xác minh schema lẫn dữ liệu. Với sync app, cần suy nghĩ thêm compatibility giữa local schema mới và payload server cũ/mới trong giai đoạn rollout.

# 40. Senior decision framework

Khi review một feature, hãy đi theo chuỗi câu hỏi thay vì bắt đầu từ framework: state thuộc owner nào; lifetime bao lâu; source of truth ở đâu; operation có blocking hay suspend; failure nào có thể retry; dữ liệu có cần tồn tại qua process death không; input có đến từ boundary không tin cậy không; API có thay đổi theo version Android không; performance nào cần đo; test nào bảo vệ behavior quan trọng; và migration/rollback ra sao. Nếu những câu hỏi này có đáp án rõ, lựa chọn MVVM/MVI, Hilt/Koin, Room/SQLDelight hoặc Retrofit/Ktor thường trở thành quyết định kỹ thuật dễ lý giải hơn.
