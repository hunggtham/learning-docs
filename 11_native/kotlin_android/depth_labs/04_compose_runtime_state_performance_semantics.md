# Depth Lab 04 — Compose Runtime, State, Performance và Semantics

Jetpack Compose dễ bắt đầu vì UI có thể được mô tả trực tiếp bằng function. Tuy nhiên khi app lớn lên, nhiều bug khó không còn nằm ở syntax `@Composable`, mà nằm ở việc **state được đọc ở phase nào, identity của node là gì, effect sống bao lâu, object có stable không, recomposition có thực sự là bottleneck hay không, và semantics tree có phản ánh đúng meaning của UI hay không**.

Depth Lab này tập trung vào cách reasoning từ runtime model thay vì tối ưu theo cảm giác.

---

## 1. Compose không “vẽ lại toàn màn hình” mỗi khi state đổi

Mental model quá đơn giản:

```text
state đổi -> toàn screen recompose -> toàn screen redraw
```

không chính xác.

Compose theo dõi state read và có thể invalidate phần tương ứng của tree. Frame có ba phase chính:

```text
Composition -> Layout -> Drawing
```

Layout lại chia thành:

```text
Measure -> Placement
```

State được đọc ở phase nào ảnh hưởng phase nào phải chạy lại.

---

## 2. State read location là performance decision

Ví dụ animation translation:

```kotlin
val offset by animateDpAsState(...)

Box(
    Modifier.offset(x = offset)
)
```

`offset` dạng value được đọc trong composition, nên state change có thể trigger recomposition trước khi layout.

Lambda overload:

```kotlin
Box(
    Modifier.offset {
        IntOffset(animatedX.roundToInt(), 0)
    }
)
```

có thể defer state read tới placement phase.

Tương tự, visual transform có thể dùng `graphicsLayer` để state read ở draw phase.

Optimization không phải “tránh recomposition bằng mọi giá”. Nó là **đặt state read ở phase muộn nhất vẫn đúng semantic** khi value thay đổi nhanh.

---

## 3. Recomposition không nhất thiết đắt, nhưng unnecessary work có thể đắt

Một recomposition nhỏ của vài primitive composable thường không phải vấn đề.

Vấn đề xảy ra khi recomposition kéo theo:

- expensive sorting,
- JSON parsing,
- database call,
- object allocation lớn,
- layout tree quá sâu,
- subcomposition phức tạp,
- image transform,
- synchronous I/O.

Đừng nhìn recomposition count một mình. Hãy đo frame cost và trace.

---

## 4. Composition phải gần với pure function

Composable nên có mental form:

```text
UI = f(state)
```

Side effect trực tiếp trong body là nguy hiểm:

```kotlin
@Composable
fun Screen(state: State) {
    analytics.logScreenShown() // sai nếu chạy mỗi recomposition
}
```

Body có thể chạy lại nhiều lần.

Effect phải được đưa vào effect API với lifetime/key rõ ràng.

---

## 5. `LaunchedEffect` là lifecycle của coroutine theo composition key

```kotlin
LaunchedEffect(userId) {
    load(userId)
}
```

Mental model:

```text
enter composition -> launch
same key -> keep current coroutine
key changes -> cancel old, launch new
leave composition -> cancel
```

Nếu key sai, effect lifetime sai.

Ví dụ:

```kotlin
LaunchedEffect(Unit) {
    observeUser(userId)
}
```

nếu `userId` thay đổi nhưng key vẫn `Unit`, effect cũ vẫn observe user cũ.

---

## 6. `rememberUpdatedState` giải quyết stale capture, không restart effect

Một callback có thể thay đổi nhưng ta không muốn restart long-running effect:

```kotlin
val latestOnTimeout by rememberUpdatedState(onTimeout)

LaunchedEffect(Unit) {
    delay(5_000)
    latestOnTimeout()
}
```

Nếu dùng `onTimeout` trực tiếp, coroutine có thể capture callback cũ.

Nếu đưa callback làm key, effect restart mỗi callback identity change.

`rememberUpdatedState` tách hai vấn đề:

```text
effect lifetime ổn định
nhưng callback/value bên trong luôn mới nhất
```

---

## 7. `DisposableEffect` dành cho resource registration có cleanup

Ví dụ register listener:

```kotlin
DisposableEffect(lifecycleOwner) {
    val observer = ...
    lifecycleOwner.lifecycle.addObserver(observer)

    onDispose {
        lifecycleOwner.lifecycle.removeObserver(observer)
    }
}
```

Đây là resource ownership rõ ràng:

```text
composition owns registration
leave/key change -> dispose
```

Nếu cleanup không gắn với cùng owner, leak xuất hiện.

---

## 8. `SideEffect` dành cho publish state sau successful composition

Dùng khi cần đồng bộ state Compose ra object non-Compose sau mỗi successful composition.

Không dùng `SideEffect` cho network request hoặc long-running coroutine.

Mỗi effect API encode một lifetime khác nhau; chọn sai effect thường là architecture bug hơn syntax bug.

---

## 9. `remember` chỉ sống theo composition identity

```kotlin
val controller = remember { Controller() }
```

controller sống chừng nào call site giữ identity trong composition.

Nó không sống qua:

```text
process death
composable rời tree
key thay đổi
```

`remember` không phải persistence.

---

## 10. `rememberSaveable` không phải database

`rememberSaveable` phù hợp với state nhỏ có thể serialize qua saved instance state.

Ví dụ:

```text
selected tab
text input nhỏ
expanded/collapsed state
scroll position phù hợp saver
```

Không nên nhét:

```text
large object graph
bitmap
repository data
network response cache lớn
```

Persist large data ở Room/DataStore/file hoặc reconstruct từ source of truth.

---

## 11. Identity quyết định state đi theo item nào

Lazy list không có stable key:

```kotlin
items(items) { item ->
    RowItem(item)
}
```

nếu list insert/remove/reorder, Compose có thể associate remembered state theo position.

Stable key:

```kotlin
items(
    items = items,
    key = { it.id }
) { item ->
    RowItem(item)
}
```

giúp runtime theo identity business.

Nhưng key phải thật sự stable và unique trong list scope.

---

## 12. `key()` là identity boundary trong composition

Nếu cùng call site render resource phụ thuộc id:

```kotlin
key(article.id) {
    ArticleCard(article)
}
```

key change nói với Compose rằng đây là một identity khác.

Dùng key đúng giúp reset remembered state khi entity thay đổi; dùng key quá rộng có thể làm state reset không cần thiết.

---

## 13. Snapshot State là observable memory model của Compose

`mutableStateOf` không chỉ là field có listener. Nó tham gia snapshot system.

Khi composable đọc state, runtime ghi nhận dependency.

Khi state thay đổi, runtime biết scope nào cần invalidate.

Điều này giải thích vì sao:

```kotlin
var count by mutableStateOf(0)
```

khác với:

```kotlin
var count = 0
```

field thường không tạo observable dependency cho Compose.

---

## 14. Backwards write có thể tạo recomposition loop

Nguy hiểm:

```kotlin
@Composable
fun Bad() {
    var count by remember { mutableStateOf(0) }
    Text("$count")
    count++
}
```

Composable đọc state rồi ghi state trong cùng composition, schedule recomposition tiếp tục.

Rule:

> không mutate state như side effect của việc render state đó.

Mutation nên đi qua event/effect phù hợp.

---

## 15. Derived state giúp giảm invalidation khi output đổi ít hơn input

Ví dụ scroll index thay đổi liên tục nhưng UI chỉ quan tâm “đã scroll qua item đầu chưa”:

```kotlin
val showButton by remember {
    derivedStateOf {
        listState.firstVisibleItemIndex > 0
    }
}
```

`derivedStateOf` hữu ích khi input change frequency cao hơn meaningful output change frequency.

Không cần dùng cho mọi computed property đơn giản.

---

## 16. Stability là contract về khả năng thay đổi quan sát được

Runtime có thể skip composable khi input được xem là stable và value không đổi.

Nhưng “data class” không tự động đồng nghĩa mọi field semantic đều immutable.

Ví dụ nguy hiểm:

```kotlin
data class UiState(
    val items: MutableList<Item>
)
```

object reference có thể không đổi trong khi nội dung list mutate.

Compose có thể không quan sát được mutation nếu collection không phải observable state container.

Prefer immutable data model hoặc observable collection phù hợp.

---

## 17. Không dùng stability annotation để che design mutable sai

Đánh dấu class stable/immutable khi thực tế field mutable ngoài sự quan sát của Compose có thể tạo UI stale.

Annotation là lời hứa với compiler/runtime.

Nếu lời hứa sai, bug khó debug hơn performance problem ban đầu.

---

## 18. Immutable snapshot giúp reasoning concurrency đơn giản hơn

ViewModel expose:

```kotlin
StateFlow<UiState>
```

với `UiState` immutable giúp UI luôn render một snapshot coherent.

Nếu expose mutable object rồi thay đổi field in-place, UI có thể đọc state giữa mutation sequence.

Immutable snapshot + atomic state replacement làm mental model rõ hơn:

```text
old state -> reducer/update -> new state
```

---

## 19. Layout là constraint negotiation

Parent đưa `Constraints` xuống child.

Child chọn size nằm trong constraint rồi parent place child.

Mental model:

```text
constraints down
size up
placement down
```

Nhiều layout bug đến từ việc nghĩ child tự chọn bất kỳ size nào.

---

## 20. Modifier order là semantic, không phải decoration order tùy ý

Ví dụ:

```kotlin
Modifier
    .clickable { }
    .padding(16.dp)
```

khác:

```kotlin
Modifier
    .padding(16.dp)
    .clickable { }
```

Hit target và vùng interaction có thể khác.

Modifier chain là pipeline; thứ tự ảnh hưởng measurement, drawing, input và semantics.

---

## 21. Custom layout cần giữ single-measure mental model

Compose layout thường đo child một lần mỗi layout pass.

Custom `Layout` phải tôn trọng constraint và không tùy tiện đo child nhiều lần.

Khi cần intrinsic measurement hoặc subcomposition, hiểu cost vì chúng phá simple single-pass path.

---

## 22. SubcomposeLayout là tool mạnh nhưng đắt hơn layout thường

`LazyColumn`, `BoxWithConstraints` và một số component cần subcomposition vì composition phụ thuộc layout constraints/viewport.

Không nên dùng subcomposition như mặc định cho custom component đơn giản.

Mỗi lớp dynamic composition thêm cost và complexity.

---

## 23. Draw phase nên tránh allocation nóng

Custom drawing chạy có thể mỗi frame.

Bad:

```kotlin
Canvas(...) {
    val path = Path()
    // build complex path mỗi frame
}
```

Nếu geometry chỉ đổi khi size/input đổi, dùng cache thích hợp như `drawWithCache`.

Mục tiêu là tránh object allocation và expensive computation trong hot draw loop.

---

## 24. `graphicsLayer` có thể tránh composition/layout nhưng không miễn phí

Transform ở graphics layer có thể chỉ invalidate draw/compositing path.

Nhưng tạo quá nhiều layer cũng có memory/GPU cost.

Tối ưu luôn phải benchmark, không đổi mọi animation sang graphics layer một cách máy móc.

---

## 25. Lazy list performance bắt đầu từ item identity và work per item

Checklist:

```text
stable key?
contentType hợp lý?
item composable có expensive work không?
image load resize đúng không?
object allocation mỗi recomposition?
nested lazy layout không cần thiết?
```

Recomposition count chỉ là một tín hiệu.

---

## 26. Expensive computation nên tách khỏi composition

Bad:

```kotlin
@Composable
fun Screen(items: List<Item>) {
    val sorted = items.sortedBy { expensiveScore(it) }
    ...
}
```

Nếu sort chỉ cần khi items đổi:

```kotlin
val sorted = remember(items) {
    items.sortedBy { expensiveScore(it) }
}
```

Hoặc tốt hơn compute trong ViewModel/domain nếu đó là application logic.

UI không nên trở thành data-processing engine.

---

## 27. `remember` cache theo key, không phải memoization global

Nếu `items` là mutable list cùng reference và mutate in-place, key có thể không đổi; remembered result stale.

Immutable input làm `remember(key)` semantics đáng tin hơn.

---

## 28. State hoisting tạo reusable boundary

Component low-level:

```kotlin
@Composable
fun SearchField(
    value: String,
    onValueChange: (String) -> Unit
)
```

không cần biết ViewModel.

Owner phía trên quyết định state nằm ở:

```text
remember
rememberSaveable
ViewModel
SavedStateHandle
repository
```

State hoisting không phải chỉ để preview; nó tách rendering khỏi ownership.

---

## 29. Không hoist state cao hơn mức cần thiết

Nếu hover state của một icon chỉ có ý nghĩa trong icon component, đẩy nó lên app-level ViewModel làm coupling tăng.

Rule:

> state nên được hoist tới lowest common owner cần đọc/ghi nó.

---

## 30. Navigation state và screen state là hai loại khác nhau

Route identity như `articleId` nên nằm ở navigation/saved-state boundary.

Article content nên lấy từ repository.

UI transient state như expanded section có thể ở local remember/saveable.

Không gom mọi thứ vào một ViewModel chỉ vì “single source of truth”. Source of truth có scope.

---

## 31. Semantics tree là public contract cho accessibility và test

UI nhìn bằng mắt có thể đúng nhưng semantics sai.

Ví dụ icon button chỉ có hình trái tim nhưng không có content description/state description phù hợp. TalkBack user không biết ý nghĩa.

Semantics cần mô tả **meaning và action**, không chỉ visual.

---

## 32. Merge semantics có thể thay đổi trải nghiệm accessibility

Một card gồm icon + title + subtitle có thể được expose thành nhiều node hoặc merge thành một meaningful node.

Quyết định phụ thuộc interaction.

Nếu toàn card clickable, một semantics node tổng hợp có thể phù hợp hơn nhiều fragment đọc rời rạc.

---

## 33. Test theo semantics tốt hơn test theo implementation detail

Thay vì tìm node bằng internal tag mọi nơi, ưu tiên user-visible semantic khi phù hợp:

```text
text
content description
role
state description
click action
```

Test như user nhìn hệ thống giúp refactor implementation mà test ít vỡ hơn.

TestTag vẫn hữu ích khi semantic selector không đủ hoặc cần node kỹ thuật cụ thể.

---

## 34. Accessibility state phải update cùng visual state

Toggle visual đổi màu nhưng semantics không đổi là bug correctness.

Ví dụ:

```text
visual: bookmarked
semantics: "Not bookmarked"
```

UI đã có hai source of truth.

Visual và semantics nên derive từ cùng state snapshot.

---

## 35. Font scaling là layout test, không chỉ accessibility setting

Text lớn có thể làm:

```text
button clip
row overflow
text overlap
fixed-height component vỡ
```

Tránh hard-code height khi content có thể expand.

Test font scale lớn là part của adaptive layout correctness.

---

## 36. RTL không chỉ mirror icon

Layout phải phân biệt `start/end` với `left/right`.

Một số icon directional cần mirror; một số icon semantic không cần.

Text alignment, gesture direction và animation cũng có thể cần review.

---

## 37. Edge-to-edge thay đổi trách nhiệm layout

Khi content vẽ dưới system bars, app phải xử lý window insets phù hợp.

Không hard-code padding status bar.

Dùng inset APIs để layout phản ứng với device cutout, navigation mode và IME.

---

## 38. IME là một dynamic inset + focus system

Form bug thường đến từ việc xử lý keyboard như fixed bottom panel.

Cần reasoning:

```text
focus owner
IME action
bring-into-view
window insets
scroll container
hardware keyboard
```

Form production phải hoạt động khi keyboard resize, floating keyboard hoặc physical keyboard.

---

## 39. Pointer input có lifetime theo key

```kotlin
Modifier.pointerInput(key) {
    detectGestures(...)
}
```

key đổi có thể restart gesture detector coroutine.

Nếu detector capture stale state, dùng key hoặc updated-state strategy đúng.

Input handling cũng là effect/lifetime problem.

---

## 40. Nested scroll là protocol giữa parent và child

Trong nested scroll, delta có thể được consume ở nhiều phase.

Đừng nghĩ “child scroll xong rồi parent scroll”. Pre-scroll/post-scroll và fling cooperation có thể phức tạp.

Khi implement collapsing toolbar hoặc coordinated motion, cần hiểu consumption contract thay vì patch offset thủ công.

---

## 41. Animation cần model target state, không imperative timeline khắp nơi

Prefer:

```text
state A -> state B
Compose animation system interpolate
```

thay vì nhiều mutable progress variable được set thủ công.

Declarative animation giảm khả năng visual state lệch application state.

---

## 42. Performance optimization workflow

Đừng bắt đầu bằng refactor code.

Workflow:

```text
1. reproduction ổn định
2. release/profileable build
3. metric xác định
4. trace/benchmark
5. locate expensive phase
6. change nhỏ
7. benchmark lại
```

Ví dụ jank list:

```text
recomposition?
layout?
draw?
image decode?
Binder call?
GC?
```

Nếu chưa biết bottleneck nằm ở đâu, optimization chỉ là guess.

---

## 43. Debug build không đại diện release performance

Debug có instrumentation và thiếu tối ưu R8/AOT/profile behavior giống release.

Đánh giá performance production nên dùng release-like build và benchmark tooling phù hợp.

---

## 44. Baseline Profile không sửa architecture chậm

Baseline Profiles giúp precompile critical code path.

Nếu startup block 500ms do synchronous database migration trên main thread, profile không biến business work đó thành miễn phí.

Profile là optimization layer sau khi critical path đã hợp lý.

---

## 45. Frame budget là end-to-end budget

Một frame miss deadline có thể do:

```text
composition 3ms
layout 5ms
draw 2ms
GC 8ms
```

tổng vượt budget dù từng phase riêng không quá lớn.

Performance review phải xem toàn trace.

---

## 46. Recomposition counter có thể gây hiểu nhầm

Một composable recompose 1.000 lần nhưng mỗi lần 5 microsecond có thể không đáng lo.

Một composable recompose 10 lần nhưng mỗi lần làm expensive sort 20ms mới là vấn đề.

Cost > count.

---

## 47. Stable key không cứu item nếu model thay đổi toàn bộ mỗi frame

Nếu ViewModel tạo list model mới với random id hoặc unstable equality mỗi emission, Lazy list mất khả năng reuse tốt.

Identity phải bắt đầu từ domain/model design, không chỉ thêm `key = { it.id }` ở UI.

---

## 48. Compose correctness checklist

| Câu hỏi | Ý nghĩa |
|---|---|
| State owner ở đâu? | lifetime đúng |
| State read ở phase nào? | invalidation cost |
| Effect key đúng chưa? | stale/restart behavior |
| Cleanup ở đâu? | leak prevention |
| Item identity stable không? | remembered state/reuse |
| Model immutable/stable thật không? | skip correctness |
| Semantics phản ánh visual state không? | accessibility correctness |
| Font/RTL/insets đã test chưa? | adaptive correctness |
| Performance đo trên release-like build chưa? | evidence-based optimization |
| Bottleneck là composition/layout/draw hay external work? | fix đúng tầng |

---

## 49. Kết luận

Compose trở nên dễ reasoning khi xem nó như một runtime có identity, snapshot dependency và phase-specific invalidation.

Mental model:

```text
state ownership
-> composition identity
-> snapshot read tracking
-> phase invalidation
-> effect lifetime
-> layout constraints
-> semantics
-> measured performance
```

Mục tiêu không phải “zero recomposition”. Mục tiêu là UI đúng, lifecycle đúng, accessibility đúng và chỉ làm lượng work cần thiết ở phase cần thiết.