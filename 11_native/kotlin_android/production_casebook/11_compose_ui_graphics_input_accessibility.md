# Case 11 — Compose UI Systems: Layout, Drawing, Input, Animation, Accessibility và Adaptive UI

Jetpack Compose thường được học qua `Column`, `Row`, `LazyColumn`, `Button` và `remember`. Cách đó đủ để làm UI cơ bản nhưng chưa đủ để debug layout khó, jank do recomposition, gesture conflict, keyboard/focus bug hoặc accessibility issue. Để đi từ “biết viết Composable” lên Senior, cần hiểu Compose như một **UI runtime** có state model, composition tree, layout/draw pipeline, input/semantics tree và integration với Android window/system UI.

Chapter này không lặp lại syntax Compose cơ bản. Nó tập trung vào các boundary nơi UI production hay vỡ.

# 1. Một Composable không phải View object

Composable function mô tả UI dựa trên state. Runtime ghi nhận cấu trúc composition và quản lý identity của các node. Khi state đọc bởi composition thay đổi, runtime xác định scope cần recomposition.

Điều quan trọng: **recomposition không đồng nghĩa toàn màn hình redraw**, và **Composable function call không tương đương tạo một View object mới mỗi lần**.

Mental model:

```text
state change
   ↓
recomposition của scope liên quan
   ↓
layout phase nếu geometry thay đổi
   ↓
draw phase nếu pixels cần thay đổi
```

Không phải state change nào cũng kích hoạt cả ba phase.

# 2. Ba phase: Composition → Layout → Draw

## Composition

Composition quyết định UI tree nào tồn tại và parameter/state nào node dùng.

```kotlin
@Composable
fun Greeting(name: String) {
    Text("Hello $name")
}
```

Nếu `name` đổi, `Greeting` có thể recompose.

## Layout

Layout gồm measurement và placement. Parent đưa constraint xuống child; child trả size lên; parent đặt child ở vị trí.

```text
Parent constraints
      ↓
Child measurement
      ↓
Child size
      ↓
Parent placement
```

Điều này khác web CSS mental model ở nhiều chỗ. Trong Compose, child không tự chọn arbitrary size vượt contract constraint mà không có modifier/layout custom xử lý rõ.

## Draw

Draw phase rasterize/render visual content. Nếu chỉ visual property thay đổi mà không ảnh hưởng geometry, có thể tránh composition/layout thừa bằng API phù hợp.

# 3. Constraint là ngôn ngữ thật của layout

`Modifier.fillMaxWidth()` không có nghĩa “width bằng screen”. Nó có nghĩa child cố chiếm maximum width mà parent constraint cho phép.

Trong nested layout:

```text
Window
→ Scaffold
→ Row
→ Box
→ Child
```

mỗi level có thể transform constraint. Khi UI size “kỳ lạ”, debug constraint chain trước khi thêm random `width()`/`height()`.

# 4. Modifier ordering là semantic

Modifier chain được áp dụng theo thứ tự và thứ tự có thể thay đổi layout, hit target, clipping và drawing.

Ví dụ:

```kotlin
Modifier
    .padding(16.dp)
    .background(Color.Gray)
```

khác:

```kotlin
Modifier
    .background(Color.Gray)
    .padding(16.dp)
```

Ở chain đầu, padding xảy ra trước background theo modifier pipeline tương ứng nên vùng background khác chain sau.

Senior rule: khi modifier có bug, đọc chain như transformation pipeline, không như danh sách option không thứ tự.

# 5. Custom layout

Khi `Row`/`Column`/`Box` không đủ, có thể viết custom `Layout` hoặc modifier layout.

Conceptual pattern:

```kotlin
Layout(
    content = { /* children */ }
) { measurables, constraints ->
    val placeables = measurables.map { it.measure(constraints) }

    layout(width, height) {
        placeables.forEach { placeable ->
            placeable.placeRelative(x, y)
        }
    }
}
```

Custom layout nên được dùng khi có invariant geometry rõ, không phải để né việc hiểu existing layout primitive.

# 6. Intrinsic measurement

Intrinsic measurement cho phép hỏi child về size “tự nhiên” trong một số scenario trước measurement thực. Nó hữu ích nhưng có cost và không phải mọi custom layout đều support dễ dàng.

Đừng dùng intrinsic như fix mặc định cho mọi alignment problem. Nếu design có thể dùng constraint/layout primitive trực tiếp, thường đơn giản hơn.

# 7. Lazy layout và identity

`LazyColumn` chỉ compose/measure item cần thiết gần viewport. Nhưng item identity phải ổn định khi list reorder/insert.

```kotlin
items(
    items = users,
    key = { it.id }
) { user ->
    UserRow(user)
}
```

Key không chỉ là performance hint; nó giúp runtime gắn remembered state/animation với logical item đúng.

Index thường là key tệ cho mutable/reorderable list.

# 8. State locality

State nên sống gần nơi nó được dùng nhất nhưng ở owner đủ cao để giữ invariant.

```text
pure visual toggle → local composable state
screen business state → ViewModel
shared navigation/session state → higher owner
persistent domain data → repository/database
```

Nếu mọi state đều đẩy lên ViewModel, ViewModel thành UI implementation bucket. Nếu mọi state để local, business coordination khó test.

# 9. `derivedStateOf`

`derivedStateOf` hữu ích khi derived value thay đổi ít hơn input state hoặc computation cần tránh invalidation không cần thiết.

```kotlin
val showButton by remember {
    derivedStateOf { listState.firstVisibleItemIndex > 0 }
}
```

Không dùng `derivedStateOf` cho mọi biến tính toán đơn giản; nó có overhead và làm code khó đọc nếu lạm dụng.

# 10. `rememberUpdatedState`

Effect lâu sống đôi khi cần callback/value mới nhất mà không restart effect.

```kotlin
val currentOnTimeout by rememberUpdatedState(onTimeout)

LaunchedEffect(Unit) {
    delay(3000)
    currentOnTimeout()
}
```

Không hiểu pattern này dễ dẫn tới stale closure hoặc effect restart quá nhiều.

# 11. Side-effect APIs theo ownership

Các API effect không interchangeable:

| API | Mental model |
|---|---|
| `LaunchedEffect(key)` | coroutine gắn composition, restart khi key đổi |
| `DisposableEffect(key)` | acquire/release resource theo composition |
| `SideEffect` | publish state sau successful recomposition |
| `rememberCoroutineScope()` | launch từ user event, scope gắn composition |
| `produceState` | bridge async source thành Compose state |

Chọn API dựa trên lifecycle của side effect, không dựa vào ví dụ StackOverflow gần giống.

# Input system

## 12. Clickable trước, pointerInput sau

Nếu use case chỉ là click/toggle/scroll chuẩn, dùng high-level modifier như `clickable`, `combinedClickable`, scroll API. Chúng tích hợp semantics, focus, ripple/interaction và accessibility tốt hơn.

`pointerInput` nên dùng khi cần gesture custom thực sự.

## 13. Gesture detector có lifecycle

```kotlin
Modifier.pointerInput(itemId) {
    detectTapGestures { offset ->
        // ...
    }
}
```

Block `pointerInput` restart khi key đổi. Nếu capture state sai key, callback có thể stale hoặc gesture detector restart không cần thiết.

## 14. Gesture competition

Nested scroll, swipe, pager, draggable và click có thể tranh input. Không giải quyết bằng việc thêm nhiều detector ngẫu nhiên.

Hãy xác định gesture ownership:

```text
parent scroll?
child horizontal drag?
click threshold?
long press?
```

và dùng API coordination như nested scroll khi cần.

# Focus, keyboard và IME

## 15. Focus là state machine riêng

Text field input không chỉ là string state. Focus quyết định keyboard, validation UX, navigation bằng hardware keyboard và accessibility.

Có thể dùng `FocusRequester` cho flow có user intent rõ, nhưng auto-focus quá mạnh có thể gây keyboard bật bất ngờ khi screen mở.

## 16. IME action

```kotlin
TextField(
    value = query,
    onValueChange = onQueryChanged,
    keyboardOptions = KeyboardOptions(
        imeAction = ImeAction.Search
    ),
    keyboardActions = KeyboardActions(
        onSearch = { onSearch() }
    )
)
```

IME action nên phản ánh action business thật. “Next” chuyển focus, “Search” submit search, “Done” kết thúc input.

## 17. Insets và keyboard

Edge-to-edge khiến content có thể nằm dưới system bars/IME. Không hardcode status bar height.

Compose cung cấp `WindowInsets`, padding modifier và scaffold patterns để content phản ứng system UI.

Target Android 15+ edge-to-edge đã được enforce mặc định ở platform context tương ứng, nên app hiện đại phải xem insets là core layout problem chứ không phải polish cuối dự án.

# Drawing

## 18. Draw modifier

Cho visual decoration tùy chỉnh, `drawBehind`, `drawWithContent`, `drawWithCache` thường nhẹ hơn custom Composable tree phức tạp.

```kotlin
Modifier.drawBehind {
    drawCircle(
        radius = size.minDimension / 2
    )
}
```

`drawWithCache` phù hợp khi object/path/brush đắt tiền có thể cache theo size/state dependency.

## 19. Canvas

`Canvas` cho custom drawing 2D. Coordinate space dùng pixel trong draw scope, nên chuyển `Dp` bằng density khi cần.

Custom draw cần nghĩ tới scaling, RTL, accessibility và hit testing—visual đẹp không tự động có semantics.

# Animation

## 20. Chọn animation theo loại state transition

Compose có nhiều level:

```text
animate*AsState → một value đơn giản
AnimatedVisibility / AnimatedContent → visibility/content transition
updateTransition → nhiều property cùng state machine
Animatable → imperative/physics/custom control
InfiniteTransition → animation lặp
```

Đừng dùng `Animatable` cho mọi button color change; abstraction càng thấp càng nhiều state/lifecycle phải tự quản.

## 21. Animation và business state

Animation state không nên trở thành source of truth cho business. Ví dụ “order success” là domain state; confetti animation chỉ là rendering side effect của state đó.

Nếu process death xảy ra, không cần khôi phục confetti frame 63; cần khôi phục trạng thái order thành công.

## 22. Motion accessibility

User có thể nhạy cảm với motion. Animation nên tránh gây cản trở, đặc biệt parallax/flashing/aggressive motion. Với accessibility-sensitive app, cân nhắc system animation scale/reduced-motion-like signals khi platform/API phù hợp.

# Semantics và accessibility

## 23. Semantics tree không phải UI tree 1:1

Compose tạo semantics tree song song để accessibility service và UI test hiểu ý nghĩa UI. Một layout có nhiều node visual có thể merge thành một semantics node meaningful.

Accessibility vì vậy không được “thêm sau” chỉ bằng content description. Semantic role, state, action, traversal và grouping đều quan trọng.

## 24. Icon cần mô tả khi mang ý nghĩa

```kotlin
Icon(
    imageVector = Icons.Default.Delete,
    contentDescription = "Delete item"
)
```

Nếu icon chỉ decorative cạnh text đã mô tả đầy đủ action, `contentDescription = null` có thể đúng để tránh screen reader đọc lặp.

## 25. Button nên là Button khi nó là button

Một `Box.clickable` có thể click được nhưng thiếu semantics/style/focus behavior chuẩn nếu không cấu hình kỹ. Dùng component semantic cao khi phù hợp.

Accessibility thường tốt hơn khi chọn đúng primitive.

## 26. Minimum touch target

UI nhìn đẹp nhưng target quá nhỏ là usability/accessibility bug. Material component thường xử lý touch target chuẩn; custom control phải tự đảm bảo.

## 27. Dynamic content announcement

Không phải mọi state update đều nên interrupt screen reader. Error quan trọng hoặc status cần feedback có thể dùng semantics/live region pattern phù hợp. Nhưng lạm dụng announcement khiến app rất khó dùng.

## 28. Heading và traversal

Large screen có section, pane và complex hierarchy. Semantic heading/traversal giúp screen reader user hiểu cấu trúc, tương tự heading trong document/web.

## 29. Accessibility testing

UI test dựa trên semantics, vì vậy semantics tốt đồng thời tăng testability. Nhưng test query pass không đảm bảo accessibility hoàn chỉnh. Cần manual testing với TalkBack/switch/hardware keyboard trong flow critical.

# Adaptive UI

## 30. Responsive khác adaptive

Responsive UI co giãn. Adaptive UI có thể **thay đổi structure/navigation pattern** theo available space hoặc posture.

Ví dụ:

```text
compact → list screen → detail screen
expanded → list + detail two-pane
```

Không chỉ tăng `padding` trên tablet.

## 31. Window size thay vì device label

Đừng viết:

```text
if tablet
```

như core architecture. Cùng một tablet có split-screen nhỏ; foldable thay posture; desktop window có thể resize.

UI nên phản ứng actual window characteristics/size class.

## 32. Material 3 Adaptive

Material 3 Adaptive cung cấp building block cho adaptive scaffold, pane và navigation theo window/posture. Version library thay đổi nhanh, nên note architecture dựa trên concept: window info → layout strategy → navigation strategy, không hardcode một alpha API vào core domain.

## 33. Navigation rail/drawer/bar

Navigation surface có thể thay đổi:

```text
compact → bottom navigation
medium → navigation rail
expanded → rail/drawer + multi-pane
```

Destination/business state không nên phụ thuộc trực tiếp vào loại navigation widget.

## 34. Foldable posture

Hinge/posture có thể chia usable region. UI hai pane nên tránh đặt primary interaction dưới hinge và cân nhắc continuity khi fold/unfold.

Process thường không chết khi posture đổi, nhưng configuration/window state thay đổi có thể trigger recomposition/recreation tùy setup. State ownership đúng giúp UI adapt mà không mất business state.

# Keyboard, mouse và non-touch input

## 35. Android không còn chỉ là phone touch

Tablet, Chromebook, desktop mode và external keyboard khiến hover, focus, keyboard shortcut, scroll wheel quan trọng hơn.

Một UI chỉ test bằng tap có thể unusable khi keyboard navigation.

## 36. Focus traversal

Interactive element cần focusable order hợp lý. Custom layout có thể cần focus properties nếu visual order khác semantic order.

## 37. Shortcut

Power-user app có thể hỗ trợ Ctrl/Cmd-like shortcut theo platform pattern. Nhưng shortcut phải bổ sung, không thay action discoverable trên UI.

# Text và localization

## 38. Không thiết kế width theo English string

German/Vietnamese/Korean/Arabic text length khác. Font scaling accessibility có thể tăng mạnh text size.

UI production cần chịu được:

```text
long translation
large font scale
RTL
multiline
IME
small window
```

## 39. RTL

Dùng `start/end` semantics thay `left/right` khi layout directional. Icon directional có thể cần auto-mirroring hoặc asset riêng.

## 40. Text measurement và truncation

Ellipsis không phải universal fix. Nếu information critical bị truncate, cần expandable/layout khác. Test font scale cao để phát hiện button/row bị cắt.

# Performance

## 41. Recomposition count không tự động là bug

Recomposition rẻ có thể hoàn toàn bình thường. Tối ưu dựa trên observed jank/allocation/trace, không chase zero recomposition.

## 42. Stability

Compose compiler/runtime dùng stability information để quyết định skip/recompose. Data model immutable và parameter stable giúp runtime reasoning tốt hơn, nhưng không nên gắn annotation chỉ để “làm compiler vui” mà phá semantic truth.

## 43. Avoid allocation trong hot draw path

Custom drawing mỗi frame không nên tạo object/path/brush nặng nếu có thể cache. `drawWithCache` tồn tại cho use case này.

## 44. Lazy list image

Image decode/load nên size-aware và async. Key ổn định, content type hợp lý và tránh nested unbounded layout giúp list smooth hơn.

# Interop với View system

## 45. `AndroidView`

Khi library/View chưa có Compose equivalent, dùng `AndroidView`. Nhưng phải quản lifecycle/state của View rõ, đặc biệt WebView/Map/Player.

Không wrap whole legacy screen vào Compose chỉ để nói rằng “đã migrate”. Migration boundary nên có mục tiêu.

## 46. Compose trong Fragment/View app

`ComposeView` cho incremental migration. Disposal strategy phải phù hợp View lifecycle để composition không sống lâu hơn Fragment view.

Đây là nơi hiểu Fragment lifecycle + Composition lifetime cực quan trọng.

# Senior Notes

## 47. UI correctness trước visual polish

State ownership, accessibility, focus, input, restore và adaptive behavior là correctness. Shadow/animation chỉ là polish sau đó.

## 48. Semantics là public API của UI với accessibility và test

Nếu visual node thay đổi nhưng semantics contract giữ ổn định, automated test bền hơn. Test bằng pixel/node structure quá chi tiết dễ brittle.

## 49. Adaptive layout là architecture concern

Nếu screen model giả định “chỉ có một pane”, thêm two-pane về sau có thể khó. Navigation state nên đủ neutral để list/detail cùng tồn tại khi window rộng.

## 50. Edge-to-edge phải design từ đầu

Insets, IME và system bars ảnh hưởng scaffold/navigation/content. Patch bằng padding random cuối sprint thường sinh bug trên device/form factor khác.

# Checklist kết thúc chapter

Bạn nên giải thích được Composition/Layout/Draw khác nhau thế nào; constraint đi qua tree ra sao; modifier order vì sao quan trọng; khi nào custom layout/draw hợp lý; lazy key liên quan identity thế nào; effect API khác nhau theo lifetime nào; gesture/focus/IME cần ownership gì; semantics tree dùng cho accessibility và test ra sao; edge-to-edge/insets ảnh hưởng UI thế nào; responsive khác adaptive thế nào; và tại sao tablet/foldable/keyboard support phải dựa trên window/capability thay vì hardcode device type.
