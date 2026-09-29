# Trường hợp (case / 사례) 11 — Compose UI các hệ thống (systems / 시스템들): bố cục (layout / 레이아웃), Drawing, đầu vào (input / 입력), Animation, khả năng tiếp cận (accessibility / 접근성) và Adaptive UI

> **Mạch đọc:** Đặt **trường hợp (case / 사례) 11 — Compose UI các hệ thống (systems / 시스템들): bố cục (layout / 레이아웃), Drawing, đầu vào (input / 입력), Animation, khả năng tiếp cận (accessibility / 접근성) và Adaptive UI** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Composition** sang **bố cục (layout / 레이아웃)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Jetpack Compose thường được học qua `Column`, `Row`, `LazyColumn`, `Button` và `remember`. Cách đó đủ để làm UI cơ bản nhưng chưa đủ để gỡ lỗi (debug / 디버그) bố cục (layout / 레이아웃) khó, jank do recomposition, gesture xung đột (conflict / 충돌), keyboard/focus bug hoặc khả năng tiếp cận (accessibility / 접근성) issue. Để đi từ “biết viết Composable” lên cấp cao (senior / 시니어), cần hiểu Compose như một **UI thời gian chạy (runtime / 런타임)** có trạng thái (state / 상태) mô hình (model / 모델), composition cây (tree / 트리), bố cục (layout / 레이아웃)/draw chuỗi xử lý (pipeline / 파이프라인), đầu vào (input / 입력)/ngữ nghĩa (semantics / 의미론) cây (tree / 트리) và tích hợp (integration / 통합) với Android cửa sổ (window / 윈도우)/hệ thống (system / 시스템) UI.

Chapter này không lặp lại cú pháp (syntax / 문법) Compose cơ bản. Nó tập trung vào các ranh giới (boundary / 경계) nơi UI môi trường vận hành (production / 운영 환경) hay vỡ.

# 1. Một Composable không phải View đối tượng (object / 객체)

Composable hàm (function / 함수) mô tả UI dựa trên trạng thái (state / 상태). thời gian chạy (runtime / 런타임) ghi nhận cấu trúc composition và quản lý định danh (identity / 식별자) của các nút (node / 노드). Khi trạng thái (state / 상태) đọc bởi composition thay đổi, thời gian chạy (runtime / 런타임) xác định phạm vi (scope / 범위) cần recomposition.

Điều quan trọng: **recomposition không đồng nghĩa toàn màn hình redraw**, và **Composable hàm (function / 함수) lời gọi (call / 호출) không tương đương tạo một View đối tượng (object / 객체) mới mỗi lần**.

Mô hình tư duy (mental model / 사고 모델):

```text
state change
   ↓
recomposition của scope liên quan
   ↓
layout phase nếu geometry thay đổi
   ↓
draw phase nếu pixels cần thay đổi
```

Không phải trạng thái (state / 상태) thay đổi (change / 변경) nào cũng kích hoạt cả ba phase.

# 2. Ba phase: Composition → bố cục (layout / 레이아웃) → Draw

## Composition

Composition quyết định UI cây (tree / 트리) nào tồn tại và parameter/trạng thái (state / 상태) nào nút (node / 노드) dùng.

```kotlin
@Composable
fun Greeting(name: String) {
    Text("Hello $name")
}
```

Nếu `name` đổi, `Greeting` có thể recompose.

## Bố cục (layout / 레이아웃)

Bố cục (layout / 레이아웃) gồm đo lường (measurement / 측정) và placement. Parent đưa ràng buộc (constraint / 제약조건) xuống child; child trả kích thước (size / 크기) lên; parent đặt child ở vị trí.

```text
Parent constraints
      ↓
Child measurement
      ↓
Child size
      ↓
Parent placement
```

Điều này khác web CSS mô hình tư duy (mental model / 사고 모델) ở nhiều chỗ. Trong Compose, child không tự chọn arbitrary kích thước (size / 크기) vượt đặc tả hợp đồng (contract / 계약) ràng buộc (constraint / 제약조건) mà không có modifier/bố cục (layout / 레이아웃) custom xử lý rõ.

## Draw

Draw phase rasterize/kết xuất (render / 렌더링) visual content. Nếu chỉ visual thuộc tính (property / 속성) thay đổi mà không ảnh hưởng hình học (geometry / 기하학), có thể tránh composition/bố cục (layout / 레이아웃) thừa bằng API phù hợp.

# 3. ràng buộc (constraint / 제약조건) là ngôn ngữ thật của bố cục (layout / 레이아웃)

`Modifier.fillMaxWidth()` không có nghĩa “width bằng screen”. Nó có nghĩa child cố chiếm maximum width mà parent ràng buộc (constraint / 제약조건) cho phép.

Trong nested bố cục (layout / 레이아웃):

```text
Window
→ Scaffold
→ Row
→ Box
→ Child
```

mỗi mức (level / 수준) có thể transform ràng buộc (constraint / 제약조건). Khi UI kích thước (size / 크기) “kỳ lạ”, gỡ lỗi (debug / 디버그) ràng buộc (constraint / 제약조건) chuỗi (chain / 사슬) trước khi thêm random `width()`/`height()`.

# 4. Modifier thứ tự (ordering / 순서) là ngữ nghĩa (semantic / 의미적)

Modifier chuỗi (chain / 사슬) được áp dụng theo thứ tự và thứ tự có thể thay đổi bố cục (layout / 레이아웃), hit mục tiêu (target / 대상), clipping và drawing.

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

Ở chuỗi (chain / 사슬) đầu, padding xảy ra trước background theo modifier chuỗi xử lý (pipeline / 파이프라인) tương ứng nên vùng background khác chuỗi (chain / 사슬) sau.

Cấp cao (senior / 시니어) quy tắc (rule / 규칙): khi modifier có bug, đọc chuỗi (chain / 사슬) như transformation chuỗi xử lý (pipeline / 파이프라인), không như danh sách option không thứ tự.

# 5. Custom bố cục (layout / 레이아웃)

Khi `Row`/`Column`/`Box` không đủ, có thể viết custom `Layout` hoặc modifier bố cục (layout / 레이아웃).

Conceptual mẫu (pattern / 패턴):

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

Custom bố cục (layout / 레이아웃) nên được dùng khi có bất biến (invariant / 불변식) hình học (geometry / 기하학) rõ, không phải để né việc hiểu existing bố cục (layout / 레이아웃) thành phần nguyên thủy (primitive / 기본 요소).

# 6. Intrinsic đo lường (measurement / 측정)

Intrinsic đo lường (measurement / 측정) cho phép hỏi child về kích thước (size / 크기) “tự nhiên” trong một số scenario trước đo lường (measurement / 측정) thực. Nó hữu ích nhưng có chi phí (cost / 비용) và không phải mọi custom bố cục (layout / 레이아웃) đều hỗ trợ (support / 지원) dễ dàng.

Đừng dùng intrinsic như fix mặc định cho mọi alignment bài toán (problem / 문제). Nếu thiết kế (design / 설계) có thể dùng ràng buộc (constraint / 제약조건)/bố cục (layout / 레이아웃) thành phần nguyên thủy (primitive / 기본 요소) trực tiếp, thường đơn giản hơn.

# 7. Lazy bố cục (layout / 레이아웃) và định danh (identity / 식별자)

`LazyColumn` chỉ compose/measure item cần thiết gần viewport. Nhưng item định danh (identity / 식별자) phải ổn định khi danh sách (list / 목록) reorder/insert.

```kotlin
items(
    items = users,
    key = { it.id }
) { user ->
    UserRow(user)
}
```

Key không chỉ là hiệu năng (performance / 성능) hint; nó giúp thời gian chạy (runtime / 런타임) gắn remembered trạng thái (state / 상태)/animation với logical item đúng.

Chỉ mục (index / 인덱스) thường là key tệ cho mutable/reorderable danh sách (list / 목록).

# 8. trạng thái (state / 상태) locality

Trạng thái (state / 상태) nên sống gần nơi nó được dùng nhất nhưng ở đơn vị sở hữu (owner / 오너) đủ cao để giữ bất biến (invariant / 불변식).

```text
pure visual toggle → local composable state
screen business state → ViewModel
shared navigation/session state → higher owner
persistent domain data → repository/database
```

Nếu mọi trạng thái (state / 상태) đều đẩy lên ViewModel, ViewModel thành UI hiện thực (implementation / 구현) bucket. Nếu mọi trạng thái (state / 상태) để cục bộ (local / 로컬), nghiệp vụ (business / 비즈니스) coordination khó kiểm thử (test / 테스트).

# 9. `derivedStateOf`

`derivedStateOf` hữu ích khi derived giá trị (value / 값) thay đổi ít hơn đầu vào (input / 입력) trạng thái (state / 상태) hoặc computation cần tránh vô hiệu hóa (invalidation / 무효화) không cần thiết.

```kotlin
val showButton by remember {
    derivedStateOf { listState.firstVisibleItemIndex > 0 }
}
```

Không dùng `derivedStateOf` cho mọi biến tính toán đơn giản; nó có overhead và làm mã (code / 코드) khó đọc nếu lạm dụng.

# 10. `rememberUpdatedState`

Tác động (effect / 효과) lâu sống đôi khi cần callback/giá trị (value / 값) mới nhất mà không restart tác động (effect / 효과).

```kotlin
val currentOnTimeout by rememberUpdatedState(onTimeout)

LaunchedEffect(Unit) {
    delay(3000)
    currentOnTimeout()
}
```

Không hiểu mẫu (pattern / 패턴) này dễ dẫn tới stale closure hoặc tác động (effect / 효과) restart quá nhiều.

# 11. Side-effect APIs theo quyền sở hữu (ownership / 소유권)

Các API tác động (effect / 효과) không interchangeable:

| API | mô hình tư duy (mental model / 사고 모델) |
|---|---|
| `LaunchedEffect(key)` | coroutine gắn composition, restart khi key đổi |
| `DisposableEffect(key)` | acquire/bản phát hành (release / 릴리스) tài nguyên (resource / 자원) theo composition |
| `SideEffect` | publish trạng thái (state / 상태) sau successful recomposition |
| `rememberCoroutineScope()` | launch từ người dùng (user / 사용자) sự kiện (event / 이벤트), phạm vi (scope / 범위) gắn composition |
| `produceState` | cầu nối (bridge / 브리지) async nguồn (source / 소스) thành Compose trạng thái (state / 상태) |

Chọn API dựa trên vòng đời (lifecycle / 생명주기) của side tác động (effect / 효과), không dựa vào ví dụ StackOverflow gần giống.

# Đầu vào (input / 입력) hệ thống (system / 시스템)

## 12. Clickable trước, pointerInput sau

Nếu use trường hợp (case / 사례) chỉ là click/toggle/scroll chuẩn, dùng high-level modifier như `clickable`, `combinedClickable`, scroll API. Chúng tích hợp ngữ nghĩa (semantics / 의미론), focus, ripple/tương tác (interaction / 상호작용) và khả năng tiếp cận (accessibility / 접근성) tốt hơn.

`pointerInput` nên dùng khi cần gesture custom thực sự.

## 13. Gesture detector có lifecycle
Phần này nối mạch Android vừa học với “13. Gesture detector có lifecycle”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.


```kotlin
Modifier.pointerInput(itemId) {
    detectTapGestures { offset ->
        // ...
    }
}
```

Khối (block / 블록) `pointerInput` restart khi key đổi. Nếu capture trạng thái (state / 상태) sai key, callback có thể stale hoặc gesture detector restart không cần thiết.

## 14. Gesture competition

Nested scroll, swipe, pager, draggable và click có thể tranh đầu vào (input / 입력). Không giải quyết bằng việc thêm nhiều detector ngẫu nhiên.

Hãy xác định gesture quyền sở hữu (ownership / 소유권):

```text
parent scroll?
child horizontal drag?
click threshold?
long press?
```

và dùng API coordination như nested scroll khi cần.

# Focus, keyboard và IME

## 15. Focus là máy trạng thái (state machine / 상태 머신) riêng

Văn bản (text / 텍스트) trường dữ liệu (field / 필드) đầu vào (input / 입력) không chỉ là string trạng thái (state / 상태). Focus quyết định keyboard, kiểm tra hợp lệ (validation / 검증) UX, điều hướng (navigation / 내비게이션) bằng hardware keyboard và khả năng tiếp cận (accessibility / 접근성).

Có thể dùng `FocusRequester` cho luồng (flow / 흐름) có người dùng (user / 사용자) intent rõ, nhưng auto-focus quá mạnh có thể gây keyboard bật bất ngờ khi screen mở.

## 16. IME action
Phần này nối mạch Android vừa học với “16. IME action”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.


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

IME hành động (action / 동작) nên phản ánh hành động (action / 동작) nghiệp vụ (business / 비즈니스) thật. “Next” chuyển focus, “tìm kiếm (search / 검색)” submit tìm kiếm (search / 검색), “Done” kết thúc đầu vào (input / 입력).

## 17. Insets và keyboard

Edge-to-edge khiến content có thể nằm dưới hệ thống (system / 시스템) bars/IME. Không hardcode status bar height.

Compose cung cấp `WindowInsets`, padding modifier và scaffold patterns để content phản ứng hệ thống (system / 시스템) UI.

Mục tiêu (target / 대상) Android 15+ edge-to-edge đã được enforce mặc định ở nền tảng (platform / 플랫폼) ngữ cảnh (context / 맥락) tương ứng, nên app hiện đại phải xem insets là cốt lõi (core / 핵심) bố cục (layout / 레이아웃) bài toán (problem / 문제) chứ không phải polish cuối dự án.

# Drawing

## 18. Draw modifier

Cho visual decoration tùy chỉnh, `drawBehind`, `drawWithContent`, `drawWithCache` thường nhẹ hơn custom Composable cây (tree / 트리) phức tạp.

```kotlin
Modifier.drawBehind {
    drawCircle(
        radius = size.minDimension / 2
    )
}
```

`drawWithCache` phù hợp khi đối tượng (object / 객체)/đường dẫn (path / 경로)/brush đắt tiền có thể bộ nhớ đệm (cache / 캐시) theo kích thước (size / 크기)/trạng thái (state / 상태) phụ thuộc (dependency / 의존성).

## 19. Canvas

`Canvas` cho custom drawing 2D. Coordinate không gian (space / 공간) dùng điểm ảnh (pixel / 픽셀) trong draw phạm vi (scope / 범위), nên chuyển `Dp` bằng density khi cần.

Custom draw cần nghĩ tới scaling, RTL, khả năng tiếp cận (accessibility / 접근성) và hit testing—visual đẹp không tự động có ngữ nghĩa (semantics / 의미론).

# Animation

## 20. Chọn animation theo loại chuyển tiếp trạng thái (state transition / 상태 전이)

Compose có nhiều mức (level / 수준):

```text
animate*AsState → một value đơn giản
AnimatedVisibility / AnimatedContent → visibility/content transition
updateTransition → nhiều property cùng state machine
Animatable → imperative/physics/custom control
InfiniteTransition → animation lặp
```

Đừng dùng `Animatable` cho mọi button color thay đổi (change / 변경); lớp trừu tượng (abstraction / 추상화) càng thấp càng nhiều trạng thái (state / 상태)/vòng đời (lifecycle / 생명주기) phải tự quản.

## 21. Animation và nghiệp vụ (business / 비즈니스) trạng thái (state / 상태)

Animation trạng thái (state / 상태) không nên trở thành nguồn chuẩn (source of truth / 정본) cho nghiệp vụ (business / 비즈니스). Ví dụ “thứ tự (order / 순서) success” là lĩnh vực (domain / 도메인) trạng thái (state / 상태); confetti animation chỉ là rendering side tác động (effect / 효과) của trạng thái (state / 상태) đó.

Nếu tiến trình (process / 프로세스) death xảy ra, không cần khôi phục confetti frame 63; cần khôi phục trạng thái thứ tự (order / 순서) thành công.

## 22. Motion khả năng tiếp cận (accessibility / 접근성)

Người dùng (user / 사용자) có thể nhạy cảm với motion. Animation nên tránh gây cản trở, đặc biệt parallax/flashing/aggressive motion. Với accessibility-sensitive app, cân nhắc hệ thống (system / 시스템) animation quy mô (scale / 규모)/reduced-motion-like signals khi nền tảng (platform / 플랫폼)/API phù hợp.

# Ngữ nghĩa (semantics / 의미론) và khả năng tiếp cận (accessibility / 접근성)

## 23. ngữ nghĩa (semantics / 의미론) cây (tree / 트리) không phải UI cây (tree / 트리) 1:1

Compose tạo ngữ nghĩa (semantics / 의미론) cây (tree / 트리) song song để khả năng tiếp cận (accessibility / 접근성) dịch vụ (service / 서비스) và UI kiểm thử (test / 테스트) hiểu ý nghĩa UI. Một bố cục (layout / 레이아웃) có nhiều nút (node / 노드) visual có thể merge thành một ngữ nghĩa (semantics / 의미론) nút (node / 노드) meaningful.

Khả năng tiếp cận (accessibility / 접근성) vì vậy không được “thêm sau” chỉ bằng content description. ngữ nghĩa (semantic / 의미적) role, trạng thái (state / 상태), hành động (action / 동작), traversal và grouping đều quan trọng.

## 24. Icon cần mô tả khi mang ý nghĩa
Phần này nối mạch Android vừa học với “24. Icon cần mô tả khi mang ý nghĩa”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.


```kotlin
Icon(
    imageVector = Icons.Default.Delete,
    contentDescription = "Delete item"
)
```

Nếu icon chỉ decorative cạnh văn bản (text / 텍스트) đã mô tả đầy đủ hành động (action / 동작), `contentDescription = null` có thể đúng để tránh screen reader đọc lặp.

## 25. Button nên là Button khi nó là button

Một `Box.clickable` có thể click được nhưng thiếu ngữ nghĩa (semantics / 의미론)/style/focus hành vi (behavior / 동작) chuẩn nếu không cấu hình kỹ. Dùng thành phần (component / 컴포넌트) ngữ nghĩa (semantic / 의미적) cao khi phù hợp.

Khả năng tiếp cận (accessibility / 접근성) thường tốt hơn khi chọn đúng thành phần nguyên thủy (primitive / 기본 요소).

## 26. Minimum touch mục tiêu (target / 대상)

UI nhìn đẹp nhưng mục tiêu (target / 대상) quá nhỏ là usability/khả năng tiếp cận (accessibility / 접근성) bug. Material thành phần (component / 컴포넌트) thường xử lý touch mục tiêu (target / 대상) chuẩn; custom điều khiển (control / 제어) phải tự đảm bảo.

## 27. động (dynamic / 동적) content announcement

Không phải mọi trạng thái (state / 상태) cập nhật (update / 업데이트) đều nên interrupt screen reader. lỗi (error / 오류) quan trọng hoặc status cần phản hồi (feedback / 피드백) có thể dùng ngữ nghĩa (semantics / 의미론)/live region mẫu (pattern / 패턴) phù hợp. Nhưng lạm dụng announcement khiến app rất khó dùng.

## 28. Heading và traversal

Large screen có section, pane và complex hierarchy. ngữ nghĩa (semantic / 의미적) heading/traversal giúp screen reader người dùng (user / 사용자) hiểu cấu trúc, tương tự heading trong document/web.

## 29. khả năng tiếp cận (accessibility / 접근성) testing

UI kiểm thử (test / 테스트) dựa trên ngữ nghĩa (semantics / 의미론), vì vậy ngữ nghĩa (semantics / 의미론) tốt đồng thời tăng testability. Nhưng kiểm thử (test / 테스트) truy vấn (query / 쿼리) pass không đảm bảo khả năng tiếp cận (accessibility / 접근성) hoàn chỉnh. Cần manual testing với TalkBack/switch/hardware keyboard trong luồng (flow / 흐름) trọng yếu (critical / 중요).

# Adaptive UI

## 30. Responsive khác adaptive

Responsive UI co giãn. Adaptive UI có thể **thay đổi cấu trúc (structure / 구조)/điều hướng (navigation / 내비게이션) mẫu (pattern / 패턴)** theo available không gian (space / 공간) hoặc posture.

Ví dụ:

```text
compact → list screen → detail screen
expanded → list + detail two-pane
```

Không chỉ tăng `padding` trên tablet.

## 31. cửa sổ (window / 윈도우) kích thước (size / 크기) thay vì thiết bị (device / 장치) label

Đừng viết:

```text
if tablet
```

như cốt lõi (core / 핵심) kiến trúc (architecture / 아키텍처). Cùng một tablet có split-screen nhỏ; foldable thay posture; desktop cửa sổ (window / 윈도우) có thể resize.

UI nên phản ứng actual cửa sổ (window / 윈도우) characteristics/kích thước (size / 크기) lớp (class / 클래스).

## 32. Material 3 Adaptive

Material 3 Adaptive cung cấp building khối (block / 블록) cho adaptive scaffold, pane và điều hướng (navigation / 내비게이션) theo cửa sổ (window / 윈도우)/posture. phiên bản (version / 버전) thư viện (library / 라이브러리) thay đổi nhanh, nên ghi chú (note / 노트) kiến trúc (architecture / 아키텍처) dựa trên concept: cửa sổ (window / 윈도우) info → bố cục (layout / 레이아웃) chiến lược (strategy / 전략) → điều hướng (navigation / 내비게이션) chiến lược (strategy / 전략), không hardcode một alpha API vào cốt lõi (core / 핵심) lĩnh vực (domain / 도메인).

## 33. điều hướng (navigation / 내비게이션) rail/drawer/bar

Điều hướng (navigation / 내비게이션) surface có thể thay đổi:

```text
compact → bottom navigation
medium → navigation rail
expanded → rail/drawer + multi-pane
```

Destination/nghiệp vụ (business / 비즈니스) trạng thái (state / 상태) không nên phụ thuộc trực tiếp vào loại điều hướng (navigation / 내비게이션) widget.

## 34. Foldable posture

Hinge/posture có thể chia usable region. UI hai pane nên tránh đặt primary tương tác (interaction / 상호작용) dưới hinge và cân nhắc continuity khi fold/unfold.

Tiến trình (process / 프로세스) thường không chết khi posture đổi, nhưng cấu hình (configuration / 구성)/cửa sổ (window / 윈도우) trạng thái (state / 상태) thay đổi có thể trigger recomposition/recreation tùy setup. quyền sở hữu trạng thái (state ownership / 상태 소유권) đúng giúp UI adapt mà không mất nghiệp vụ (business / 비즈니스) trạng thái (state / 상태).

# Keyboard, mouse và non-touch đầu vào (input / 입력)

## 35. Android không còn chỉ là phone touch

Tablet, Chromebook, desktop chế độ (mode / 모드) và bên ngoài (external / 외부) keyboard khiến hover, focus, keyboard shortcut, scroll wheel quan trọng hơn.

Một UI chỉ kiểm thử (test / 테스트) bằng tap có thể unusable khi keyboard điều hướng (navigation / 내비게이션).

## 36. Focus traversal

Interactive element cần focusable thứ tự (order / 순서) hợp lý. Custom bố cục (layout / 레이아웃) có thể cần focus properties nếu visual thứ tự (order / 순서) khác ngữ nghĩa (semantic / 의미적) thứ tự (order / 순서).

## 37. Shortcut

Power-user app có thể hỗ trợ Ctrl/Cmd-like shortcut theo nền tảng (platform / 플랫폼) mẫu (pattern / 패턴). Nhưng shortcut phải bổ sung, không thay hành động (action / 동작) discoverable trên UI.

# Văn bản (text / 텍스트) và localization

## 38. Không thiết kế width theo English string

German/Vietnamese/Korean/Arabic văn bản (text / 텍스트) length khác. Font scaling khả năng tiếp cận (accessibility / 접근성) có thể tăng mạnh văn bản (text / 텍스트) kích thước (size / 크기).

UI môi trường vận hành (production / 운영 환경) cần chịu được:

```text
long translation
large font scale
RTL
multiline
IME
small window
```

## 39. RTL

Dùng `start/end` ngữ nghĩa (semantics / 의미론) thay `left/right` khi bố cục (layout / 레이아웃) directional. Icon directional có thể cần auto-mirroring hoặc asset riêng.

## 40. văn bản (text / 텍스트) đo lường (measurement / 측정) và truncation

Ellipsis không phải universal fix. Nếu thông tin (information / 정보) trọng yếu (critical / 중요) bị truncate, cần expandable/bố cục (layout / 레이아웃) khác. kiểm thử (test / 테스트) font quy mô (scale / 규모) cao để phát hiện button/row bị cắt.

# Hiệu năng (performance / 성능)

## 41. Recomposition count không tự động là bug

Recomposition rẻ có thể hoàn toàn bình thường. Tối ưu dựa trên observed jank/allocation/dấu vết (trace / 추적), không chase zero recomposition.

## 42. Stability

Compose trình biên dịch (compiler / 컴파일러)/thời gian chạy (runtime / 런타임) dùng stability thông tin (information / 정보) để quyết định skip/recompose. mô hình dữ liệu (data model / 데이터 모델) immutable và parameter stable giúp thời gian chạy (runtime / 런타임) lập luận (reasoning / 추론) tốt hơn, nhưng không nên gắn annotation chỉ để “làm trình biên dịch (compiler / 컴파일러) vui” mà phá ngữ nghĩa (semantic / 의미적) truth.

## 43. Avoid allocation trong hot draw đường dẫn (path / 경로)

Custom drawing mỗi frame không nên tạo đối tượng (object / 객체)/đường dẫn (path / 경로)/brush nặng nếu có thể bộ nhớ đệm (cache / 캐시). `drawWithCache` tồn tại cho use trường hợp (case / 사례) này.

## 44. Lazy danh sách (list / 목록) ảnh (image / 이미지)

Ảnh (image / 이미지) decode/tải (load / 로드) nên size-aware và async. Key ổn định, content kiểu (type / 타입) hợp lý và tránh nested unbounded bố cục (layout / 레이아웃) giúp danh sách (list / 목록) smooth hơn.

# Interop với View hệ thống (system / 시스템)

## 45. `AndroidView`

Khi thư viện (library / 라이브러리)/View chưa có Compose equivalent, dùng `AndroidView`. Nhưng phải quản vòng đời (lifecycle / 생명주기)/trạng thái (state / 상태) của View rõ, đặc biệt WebView/Map/Player.

Không wrap whole legacy screen vào Compose chỉ để nói rằng “đã migrate”. di chuyển (migration / 마이그레이션) ranh giới (boundary / 경계) nên có mục tiêu.

## 46. Compose trong Fragment/View app

`ComposeView` cho incremental di chuyển (migration / 마이그레이션). Disposal chiến lược (strategy / 전략) phải phù hợp View vòng đời (lifecycle / 생명주기) để composition không sống lâu hơn Fragment view.

Đây là nơi hiểu Fragment vòng đời (lifecycle / 생명주기) + Composition thời gian tồn tại (lifetime / 수명) cực quan trọng.

# Cấp cao (senior / 시니어) Notes

## 47. UI tính đúng đắn (correctness / 정확성) trước visual polish

Quyền sở hữu trạng thái (state ownership / 상태 소유권), khả năng tiếp cận (accessibility / 접근성), focus, đầu vào (input / 입력), restore và adaptive hành vi (behavior / 동작) là tính đúng đắn (correctness / 정확성). Shadow/animation chỉ là polish sau đó.

## 48. ngữ nghĩa (semantics / 의미론) là API công khai (public API / 공개 API) của UI với khả năng tiếp cận (accessibility / 접근성) và kiểm thử (test / 테스트)

Nếu visual nút (node / 노드) thay đổi nhưng ngữ nghĩa (semantics / 의미론) đặc tả hợp đồng (contract / 계약) giữ ổn định, automated kiểm thử (test / 테스트) bền hơn. kiểm thử (test / 테스트) bằng điểm ảnh (pixel / 픽셀)/nút (node / 노드) cấu trúc (structure / 구조) quá chi tiết dễ brittle.

## 49. Adaptive bố cục (layout / 레이아웃) là kiến trúc (architecture / 아키텍처) concern

Nếu screen mô hình (model / 모델) giả định “chỉ có một pane”, thêm two-pane về sau có thể khó. điều hướng (navigation / 내비게이션) trạng thái (state / 상태) nên đủ neutral để danh sách (list / 목록)/detail cùng tồn tại khi cửa sổ (window / 윈도우) rộng.

## 50. Edge-to-edge phải thiết kế (design / 설계) từ đầu

Insets, IME và hệ thống (system / 시스템) bars ảnh hưởng scaffold/điều hướng (navigation / 내비게이션)/content. Patch bằng padding random cuối sprint thường sinh bug trên thiết bị (device / 장치)/form factor khác.

# Checklist kết thúc chapter

Bạn nên giải thích được Composition/bố cục (layout / 레이아웃)/Draw khác nhau thế nào; ràng buộc (constraint / 제약조건) đi qua cây (tree / 트리) ra sao; modifier thứ tự (order / 순서) vì sao quan trọng; khi nào custom bố cục (layout / 레이아웃)/draw hợp lý; lazy key liên quan định danh (identity / 식별자) thế nào; tác động (effect / 효과) API khác nhau theo thời gian tồn tại (lifetime / 수명) nào; gesture/focus/IME cần quyền sở hữu (ownership / 소유권) gì; ngữ nghĩa (semantics / 의미론) cây (tree / 트리) dùng cho khả năng tiếp cận (accessibility / 접근성) và kiểm thử (test / 테스트) ra sao; edge-to-edge/insets ảnh hưởng UI thế nào; responsive khác adaptive thế nào; và tại sao tablet/foldable/keyboard hỗ trợ (support / 지원) phải dựa trên cửa sổ (window / 윈도우)/năng lực (capability / 역량) thay vì hardcode thiết bị (device / 장치) kiểu (type / 타입).

> **Bàn giao:** Sau **50. Edge-to-edge phải thiết kế (design / 설계) từ đầu**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 architecture end to end](./01_architecture_end_to_end.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
