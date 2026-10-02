# Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)

> **Mạch đọc:** [README](./README.md) là owner của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**; đặt lab sau coroutine/state và trước SDK/build forensics. Từ **1. Compose không “vẽ lại toàn màn hình” mỗi khi trạng thái (state / 상태) đổi** nối state read location, identity, effects/lifetime, stability, invalidation, semantics và evidence-based profiling, rồi tối ưu theo runtime model thay vì cảm giác.

Jetpack Compose dễ bắt đầu vì UI có thể được mô tả trực tiếp bằng hàm (function / 함수). Tuy nhiên khi app lớn lên, nhiều bug khó không còn nằm ở cú pháp (syntax / 문법) `@Composable`, mà nằm ở việc **trạng thái (state / 상태) được đọc ở phase nào, định danh (identity / 식별자) của nút (node / 노드) là gì, tác động (effect / 효과) sống bao lâu, đối tượng (object / 객체) có stable không, recomposition có thực sự là bottleneck hay không, và ngữ nghĩa (semantics / 의미론) cây (tree / 트리) có phản ánh đúng meaning của UI hay không**.

Độ sâu (depth / 깊이) Lab này tập trung vào cách lập luận (reasoning / 추론) từ thời gian chạy (runtime / 런타임) mô hình (model / 모델) thay vì tối ưu theo cảm giác.

---

## 1. Compose không “vẽ lại toàn màn hình” mỗi khi trạng thái (state / 상태) đổi

Mô hình tư duy (mental model / 사고 모델) quá đơn giản:

```text
state đổi -> toàn screen recompose -> toàn screen redraw
```

không chính xác.

Compose theo dõi trạng thái (state / 상태) read và có thể invalidate phần tương ứng của cây (tree / 트리). Frame có ba phase chính:

```text
Composition -> Layout -> Drawing
```

Bố cục (layout / 레이아웃) lại chia thành:

```text
Measure -> Placement
```

Trạng thái (state / 상태) được đọc ở phase nào ảnh hưởng phase nào phải chạy lại.

---

> **Chuyển mạch:** Compose invalidates readers of changed state, không redraw toàn màn hình; read location vì vậy ảnh hưởng recomposition scope và chi phí work.

## 2. trạng thái (state / 상태) read location là hiệu năng (performance / 성능) quyết định (decision / 결정)

Ví dụ animation translation:

```kotlin
val offset by animateDpAsState(...)

Box(
    Modifier.offset(x = offset)
)
```

`offset` dạng giá trị (value / 값) được đọc trong composition, nên trạng thái (state / 상태) thay đổi (change / 변경) có thể trigger recomposition trước khi bố cục (layout / 레이아웃).

Lambda overload:

```kotlin
Box(
    Modifier.offset {
        IntOffset(animatedX.roundToInt(), 0)
    }
)
```

có thể defer trạng thái (state / 상태) read tới placement phase.

Tương tự, visual transform có thể dùng `graphicsLayer` để trạng thái (state / 상태) read ở draw phase.

Tối ưu hóa (optimization / 최적화) không phải “tránh recomposition bằng mọi giá”. Nó là **đặt trạng thái (state / 상태) read ở phase muộn nhất vẫn đúng ngữ nghĩa (semantic / 의미적)** khi giá trị (value / 값) thay đổi nhanh.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **3. Recomposition không nhất thiết đắt, nhưng unnecessary công việc (work / 작업) có thể đắt** tiếp nhận điểm tựa từ **2. trạng thái (state / 상태) read location là hiệu năng (performance / 성능) quyết định (decision / 결정)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Composition phải gần với pure hàm (function / 함수)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Recomposition không nhất thiết đắt, nhưng unnecessary công việc (work / 작업) có thể đắt

Một recomposition nhỏ của vài thành phần nguyên thủy (primitive / 기본 요소) composable thường không phải vấn đề.

Vấn đề xảy ra khi recomposition kéo theo:

- expensive sorting,
- JSON parsing,
- cơ sở dữ liệu (database / 데이터베이스) lời gọi (call / 호출),
- đối tượng (object / 객체) allocation lớn,
- bố cục (layout / 레이아웃) cây (tree / 트리) quá sâu,
- subcomposition phức tạp,
- ảnh (image / 이미지) transform,
- synchronous I/O.

Đừng nhìn recomposition count một mình. Hãy đo frame chi phí (cost / 비용) và dấu vết (trace / 추적).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **4. Composition phải gần với pure hàm (function / 함수)** tiếp nhận điểm tựa từ **3. Recomposition không nhất thiết đắt, nhưng unnecessary công việc (work / 작업) có thể đắt** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. LaunchedEffect là lifecycle của coroutine theo composition key** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Composition phải gần với pure hàm (function / 함수)

Composable nên có mental form:

```text
UI = f(state)
```

Side tác động (effect / 효과) trực tiếp trong body là nguy hiểm:

```kotlin
@Composable
fun Screen(state: State) {
    analytics.logScreenShown() // sai nếu chạy mỗi recomposition
}
```

Body có thể chạy lại nhiều lần.

Tác động (effect / 효과) phải được đưa vào tác động (effect / 효과) API với thời gian tồn tại (lifetime / 수명)/key rõ ràng.

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **4. Composition phải gần với pure hàm (function / 함수)** xác định đầu vào; **5. LaunchedEffect là lifecycle của coroutine theo composition key** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **6. rememberUpdatedState giải quyết stale capture, không restart tác động (effect / 효과)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. `LaunchedEffect` là lifecycle của coroutine theo composition key
Phần này nối mạch Android vừa học với “5. `LaunchedEffect` là lifecycle của coroutine theo composition key”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

```kotlin
LaunchedEffect(userId) {
    load(userId)
}
```

Mô hình tư duy (mental model / 사고 모델):

```text
enter composition -> launch
same key -> keep current coroutine
key changes -> cancel old, launch new
leave composition -> cancel
```

Nếu key sai, tác động (effect / 효과) thời gian tồn tại (lifetime / 수명) sai.

Ví dụ:

```kotlin
LaunchedEffect(Unit) {
    observeUser(userId)
}
```

nếu `userId` thay đổi nhưng key vẫn `Unit`, tác động (effect / 효과) cũ vẫn observe người dùng (user / 사용자) cũ.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **5. LaunchedEffect là lifecycle của coroutine theo composition key** xác định đầu vào; **6. rememberUpdatedState giải quyết stale capture, không restart tác động (effect / 효과)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **7. DisposableEffect dành cho tài nguyên (resource / 자원) registration có cleanup** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. `rememberUpdatedState` giải quyết stale capture, không restart tác động (effect / 효과)

Một callback có thể thay đổi nhưng ta không muốn restart long-running tác động (effect / 효과):

```kotlin
val latestOnTimeout by rememberUpdatedState(onTimeout)

LaunchedEffect(Unit) {
    delay(5_000)
    latestOnTimeout()
}
```

Nếu dùng `onTimeout` trực tiếp, coroutine có thể capture callback cũ.

Nếu đưa callback làm key, tác động (effect / 효과) restart mỗi callback định danh (identity / 식별자) thay đổi (change / 변경).

`rememberUpdatedState` tách hai vấn đề:

```text
effect lifetime ổn định
nhưng callback/value bên trong luôn mới nhất
```

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **6. rememberUpdatedState giải quyết stale capture, không restart tác động (effect / 효과)** nêu điều cần giải thích; **7. DisposableEffect dành cho tài nguyên (resource / 자원) registration có cleanup** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **8. SideEffect dành cho publish trạng thái (state / 상태) sau successful composition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. `DisposableEffect` dành cho tài nguyên (resource / 자원) registration có cleanup

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

Đây là tài nguyên (resource / 자원) quyền sở hữu (ownership / 소유권) rõ ràng:

```text
composition owns registration
leave/key change -> dispose
```

Nếu cleanup không gắn với cùng đơn vị sở hữu (owner / 오너), leak xuất hiện.

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **7. DisposableEffect dành cho tài nguyên (resource / 자원) registration có cleanup** nêu điều cần giải thích; **8. SideEffect dành cho publish trạng thái (state / 상태) sau successful composition** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **9. remember chỉ sống theo composition identity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. `SideEffect` dành cho publish trạng thái (state / 상태) sau successful composition

Dùng khi cần đồng bộ trạng thái (state / 상태) Compose ra đối tượng (object / 객체) non-Compose sau mỗi successful composition.

Không dùng `SideEffect` cho mạng (network / 네트워크) yêu cầu (request / 요청) hoặc long-running coroutine.

Mỗi tác động (effect / 효과) API encode một thời gian tồn tại (lifetime / 수명) khác nhau; chọn sai tác động (effect / 효과) thường là kiến trúc (architecture / 아키텍처) bug hơn cú pháp (syntax / 문법) bug.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **9. remember chỉ sống theo composition identity** tiếp nhận điểm tựa từ **8. SideEffect dành cho publish trạng thái (state / 상태) sau successful composition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. rememberSaveable không phải cơ sở dữ liệu (database / 데이터베이스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. `remember` chỉ sống theo composition identity
Phần này nối mạch Android vừa học với “9. `remember` chỉ sống theo composition identity”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

```kotlin
val controller = remember { Controller() }
```

controller sống chừng nào lời gọi (call / 호출) site giữ định danh (identity / 식별자) trong composition.

Nó không sống qua:

```text
process death
composable rời tree
key thay đổi
```

`remember` không phải persistence.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **9. remember chỉ sống theo composition identity** nêu điều cần giải thích; **10. rememberSaveable không phải cơ sở dữ liệu (database / 데이터베이스)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **11. định danh (identity / 식별자) quyết định trạng thái (state / 상태) đi theo item nào** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. `rememberSaveable` không phải cơ sở dữ liệu (database / 데이터베이스)

`rememberSaveable` phù hợp với trạng thái (state / 상태) nhỏ có thể serialize qua saved instance trạng thái (state / 상태).

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

Persist large dữ liệu (data / 데이터) ở Room/DataStore/tệp (file / 파일) hoặc reconstruct từ nguồn chuẩn (source of truth / 정본).

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **10. rememberSaveable không phải cơ sở dữ liệu (database / 데이터베이스)** nêu điều cần giải thích; **11. định danh (identity / 식별자) quyết định trạng thái (state / 상태) đi theo item nào** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **12. key() là định danh (identity / 식별자) ranh giới (boundary / 경계) trong composition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. định danh (identity / 식별자) quyết định trạng thái (state / 상태) đi theo item nào

Lazy danh sách (list / 목록) không có stable key:

```kotlin
items(items) { item ->
    RowItem(item)
}
```

nếu danh sách (list / 목록) insert/remove/reorder, Compose có thể associate remembered trạng thái (state / 상태) theo position.

Stable key:

```kotlin
items(
    items = items,
    key = { it.id }
) { item ->
    RowItem(item)
}
```

giúp thời gian chạy (runtime / 런타임) theo định danh (identity / 식별자) nghiệp vụ (business / 비즈니스).

Nhưng key phải thật sự stable và unique trong danh sách (list / 목록) phạm vi (scope / 범위).

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **11. định danh (identity / 식별자) quyết định trạng thái (state / 상태) đi theo item nào** đã nêu tiêu chí phân biệt, còn **12. key() là định danh (identity / 식별자) ranh giới (boundary / 경계) trong composition** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **13. Snapshot trạng thái (state / 상태) là observable bộ nhớ (memory / 메모리) mô hình (model / 모델) của Compose** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. `key()` là định danh (identity / 식별자) ranh giới (boundary / 경계) trong composition

Nếu cùng lời gọi (call / 호출) site kết xuất (render / 렌더링) tài nguyên (resource / 자원) phụ thuộc id:

```kotlin
key(article.id) {
    ArticleCard(article)
}
```

key thay đổi (change / 변경) nói với Compose rằng đây là một định danh (identity / 식별자) khác.

Dùng key đúng giúp reset remembered trạng thái (state / 상태) khi thực thể (entity / 엔터티) thay đổi; dùng key quá rộng có thể làm trạng thái (state / 상태) reset không cần thiết.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **12. key() là định danh (identity / 식별자) ranh giới (boundary / 경계) trong composition** đã nêu tiêu chí phân biệt, còn **13. Snapshot trạng thái (state / 상태) là observable bộ nhớ (memory / 메모리) mô hình (model / 모델) của Compose** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **14. Backwards ghi (write / 쓰기) có thể tạo recomposition vòng lặp (loop / 루프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Snapshot trạng thái (state / 상태) là observable bộ nhớ (memory / 메모리) mô hình (model / 모델) của Compose

`mutableStateOf` không chỉ là trường dữ liệu (field / 필드) có listener. Nó tham gia snapshot hệ thống (system / 시스템).

Khi composable đọc trạng thái (state / 상태), thời gian chạy (runtime / 런타임) ghi nhận phụ thuộc (dependency / 의존성).

Khi trạng thái (state / 상태) thay đổi, thời gian chạy (runtime / 런타임) biết phạm vi (scope / 범위) nào cần invalidate.

Điều này giải thích vì sao:

```kotlin
var count by mutableStateOf(0)
```

khác với:

```kotlin
var count = 0
```

Trường dữ liệu (field / 필드) thường không tạo observable phụ thuộc (dependency / 의존성) cho Compose.

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **14. Backwards ghi (write / 쓰기) có thể tạo recomposition vòng lặp (loop / 루프)** tiếp nhận điểm tựa từ **13. Snapshot trạng thái (state / 상태) là observable bộ nhớ (memory / 메모리) mô hình (model / 모델) của Compose** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Derived trạng thái (state / 상태) giúp giảm vô hiệu hóa (invalidation / 무효화) khi đầu ra (output / 출력) đổi ít hơn đầu vào (input / 입력)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Backwards ghi (write / 쓰기) có thể tạo recomposition vòng lặp (loop / 루프)

Nguy hiểm:

```kotlin
@Composable
fun Bad() {
    var count by remember { mutableStateOf(0) }
    Text("$count")
    count++
}
```

Composable đọc trạng thái (state / 상태) rồi ghi trạng thái (state / 상태) trong cùng composition, schedule recomposition tiếp tục.

Quy tắc (rule / 규칙):

> không mutate trạng thái (state / 상태) như side tác động (effect / 효과) của việc kết xuất (render / 렌더링) trạng thái (state / 상태) đó.

Mutation nên đi qua sự kiện (event / 이벤트)/tác động (effect / 효과) phù hợp.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **15. Derived trạng thái (state / 상태) giúp giảm vô hiệu hóa (invalidation / 무효화) khi đầu ra (output / 출력) đổi ít hơn đầu vào (input / 입력)** tiếp nhận điểm tựa từ **14. Backwards ghi (write / 쓰기) có thể tạo recomposition vòng lặp (loop / 루프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Stability là đặc tả hợp đồng (contract / 계약) về khả năng thay đổi quan sát được** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Derived trạng thái (state / 상태) giúp giảm vô hiệu hóa (invalidation / 무효화) khi đầu ra (output / 출력) đổi ít hơn đầu vào (input / 입력)

Ví dụ scroll chỉ mục (index / 인덱스) thay đổi liên tục nhưng UI chỉ quan tâm “đã scroll qua item đầu chưa”:

```kotlin
val showButton by remember {
    derivedStateOf {
        listState.firstVisibleItemIndex > 0
    }
}
```

`derivedStateOf` hữu ích khi đầu vào (input / 입력) thay đổi (change / 변경) frequency cao hơn meaningful đầu ra (output / 출력) thay đổi (change / 변경) frequency.

Không cần dùng cho mọi computed thuộc tính (property / 속성) đơn giản.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **16. Stability là đặc tả hợp đồng (contract / 계약) về khả năng thay đổi quan sát được** tiếp nhận điểm tựa từ **15. Derived trạng thái (state / 상태) giúp giảm vô hiệu hóa (invalidation / 무효화) khi đầu ra (output / 출력) đổi ít hơn đầu vào (input / 입력)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Không dùng stability annotation để che thiết kế (design / 설계) mutable sai** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Stability là đặc tả hợp đồng (contract / 계약) về khả năng thay đổi quan sát được

Thời gian chạy (runtime / 런타임) có thể skip composable khi đầu vào (input / 입력) được xem là stable và giá trị (value / 값) không đổi.

Nhưng “dữ liệu (data / 데이터) lớp (class / 클래스)” không tự động đồng nghĩa mọi trường dữ liệu (field / 필드) ngữ nghĩa (semantic / 의미적) đều immutable.

Ví dụ nguy hiểm:

```kotlin
data class UiState(
    val items: MutableList<Item>
)
```

Đối tượng (object / 객체) tham chiếu (reference / 참조) có thể không đổi trong khi nội dung danh sách (list / 목록) mutate.

Compose có thể không quan sát được mutation nếu collection không phải observable trạng thái (state / 상태) bộ chứa (container / 컨테이너).

Prefer immutable mô hình dữ liệu (data model / 데이터 모델) hoặc observable collection phù hợp.

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **17. Không dùng stability annotation để che thiết kế (design / 설계) mutable sai** tiếp nhận điểm tựa từ **16. Stability là đặc tả hợp đồng (contract / 계약) về khả năng thay đổi quan sát được** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Immutable snapshot giúp lập luận (reasoning / 추론) tính đồng thời (concurrency / 동시성) đơn giản hơn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Không dùng stability annotation để che thiết kế (design / 설계) mutable sai

Đánh dấu lớp (class / 클래스) stable/immutable khi thực tế trường dữ liệu (field / 필드) mutable ngoài sự quan sát của Compose có thể tạo UI stale.

Annotation là lời hứa với trình biên dịch (compiler / 컴파일러)/thời gian chạy (runtime / 런타임).

Nếu lời hứa sai, bug khó gỡ lỗi (debug / 디버그) hơn hiệu năng (performance / 성능) bài toán (problem / 문제) ban đầu.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **18. Immutable snapshot giúp lập luận (reasoning / 추론) tính đồng thời (concurrency / 동시성) đơn giản hơn** tiếp nhận điểm tựa từ **17. Không dùng stability annotation để che thiết kế (design / 설계) mutable sai** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. bố cục (layout / 레이아웃) là ràng buộc (constraint / 제약조건) negotiation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Immutable snapshot giúp lập luận (reasoning / 추론) tính đồng thời (concurrency / 동시성) đơn giản hơn

ViewModel expose:

```kotlin
StateFlow<UiState>
```

với `UiState` immutable giúp UI luôn kết xuất (render / 렌더링) một snapshot coherent.

Nếu expose mutable đối tượng (object / 객체) rồi thay đổi trường dữ liệu (field / 필드) in-place, UI có thể đọc trạng thái (state / 상태) giữa mutation chuỗi (sequence / 시퀀스).

Immutable snapshot + atomic trạng thái (state / 상태) replacement làm mô hình tư duy (mental model / 사고 모델) rõ hơn:

```text
old state -> reducer/update -> new state
```

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **19. bố cục (layout / 레이아웃) là ràng buộc (constraint / 제약조건) negotiation** tiếp nhận điểm tựa từ **18. Immutable snapshot giúp lập luận (reasoning / 추론) tính đồng thời (concurrency / 동시성) đơn giản hơn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Modifier thứ tự (order / 순서) là ngữ nghĩa (semantic / 의미적), không phải decoration thứ tự (order / 순서) tùy ý** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. bố cục (layout / 레이아웃) là ràng buộc (constraint / 제약조건) negotiation

Parent đưa `Constraints` xuống child.

Child chọn kích thước (size / 크기) nằm trong ràng buộc (constraint / 제약조건) rồi parent place child.

Mô hình tư duy (mental model / 사고 모델):

```text
constraints down
size up
placement down
```

Nhiều bố cục (layout / 레이아웃) bug đến từ việc nghĩ child tự chọn bất kỳ kích thước (size / 크기) nào.

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **20. Modifier thứ tự (order / 순서) là ngữ nghĩa (semantic / 의미적), không phải decoration thứ tự (order / 순서) tùy ý** tiếp nhận điểm tựa từ **19. bố cục (layout / 레이아웃) là ràng buộc (constraint / 제약조건) negotiation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Custom bố cục (layout / 레이아웃) cần giữ single-measure mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Modifier thứ tự (order / 순서) là ngữ nghĩa (semantic / 의미적), không phải decoration thứ tự (order / 순서) tùy ý

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

Hit mục tiêu (target / 대상) và vùng tương tác (interaction / 상호작용) có thể khác.

Modifier chuỗi (chain / 사슬) là chuỗi xử lý (pipeline / 파이프라인); thứ tự ảnh hưởng đo lường (measurement / 측정), drawing, đầu vào (input / 입력) và ngữ nghĩa (semantics / 의미론).

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **21. Custom bố cục (layout / 레이아웃) cần giữ single-measure mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **20. Modifier thứ tự (order / 순서) là ngữ nghĩa (semantic / 의미적), không phải decoration thứ tự (order / 순서) tùy ý** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **22. SubcomposeLayout là công cụ (tool / 도구) mạnh nhưng đắt hơn bố cục (layout / 레이아웃) thường** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Custom bố cục (layout / 레이아웃) cần giữ single-measure mô hình tư duy (mental model / 사고 모델)

Compose bố cục (layout / 레이아웃) thường đo child một lần mỗi bố cục (layout / 레이아웃) pass.

Custom `Layout` phải tôn trọng ràng buộc (constraint / 제약조건) và không tùy tiện đo child nhiều lần.

Khi cần intrinsic đo lường (measurement / 측정) hoặc subcomposition, hiểu chi phí (cost / 비용) vì chúng phá simple single-pass đường dẫn (path / 경로).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **22. SubcomposeLayout là công cụ (tool / 도구) mạnh nhưng đắt hơn bố cục (layout / 레이아웃) thường** gom các mảnh từ **21. Custom bố cục (layout / 레이아웃) cần giữ single-measure mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **23. Draw phase nên tránh allocation nóng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. SubcomposeLayout là công cụ (tool / 도구) mạnh nhưng đắt hơn bố cục (layout / 레이아웃) thường

`LazyColumn`, `BoxWithConstraints` và một số thành phần (component / 컴포넌트) cần subcomposition vì composition phụ thuộc bố cục (layout / 레이아웃) các ràng buộc (constraints / 제약조건들)/viewport.

Không nên dùng subcomposition như mặc định cho custom thành phần (component / 컴포넌트) đơn giản.

Mỗi lớp động (dynamic / 동적) composition thêm chi phí (cost / 비용) và độ phức tạp (complexity / 복잡도).

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **23. Draw phase nên tránh allocation nóng** tiếp nhận điểm tựa từ **22. SubcomposeLayout là công cụ (tool / 도구) mạnh nhưng đắt hơn bố cục (layout / 레이아웃) thường** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. graphicsLayer có thể tránh composition/bố cục (layout / 레이아웃) nhưng không miễn phí** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Draw phase nên tránh allocation nóng

Custom drawing chạy có thể mỗi frame.

Bad:

```kotlin
Canvas(...) {
    val path = Path()
    // build complex path mỗi frame
}
```

Nếu hình học (geometry / 기하학) chỉ đổi khi kích thước (size / 크기)/đầu vào (input / 입력) đổi, dùng bộ nhớ đệm (cache / 캐시) thích hợp như `drawWithCache`.

Mục tiêu là tránh đối tượng (object / 객체) allocation và expensive computation trong hot draw vòng lặp (loop / 루프).

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **24. graphicsLayer có thể tránh composition/bố cục (layout / 레이아웃) nhưng không miễn phí** tiếp nhận điểm tựa từ **23. Draw phase nên tránh allocation nóng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Lazy danh sách (list / 목록) hiệu năng (performance / 성능) bắt đầu từ item định danh (identity / 식별자) và công việc (work / 작업) per item** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. `graphicsLayer` có thể tránh composition/bố cục (layout / 레이아웃) nhưng không miễn phí

Transform ở graphics tầng (layer / 계층) có thể chỉ invalidate draw/compositing đường dẫn (path / 경로).

Nhưng tạo quá nhiều tầng (layer / 계층) cũng có bộ nhớ (memory / 메모리)/GPU chi phí (cost / 비용).

Tối ưu luôn phải benchmark, không đổi mọi animation sang graphics tầng (layer / 계층) một cách máy móc.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **25. Lazy danh sách (list / 목록) hiệu năng (performance / 성능) bắt đầu từ item định danh (identity / 식별자) và công việc (work / 작업) per item** tiếp nhận điểm tựa từ **24. graphicsLayer có thể tránh composition/bố cục (layout / 레이아웃) nhưng không miễn phí** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Expensive computation nên tách khỏi composition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Lazy danh sách (list / 목록) hiệu năng (performance / 성능) bắt đầu từ item định danh (identity / 식별자) và công việc (work / 작업) per item

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

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **26. Expensive computation nên tách khỏi composition** tiếp nhận điểm tựa từ **25. Lazy danh sách (list / 목록) hiệu năng (performance / 성능) bắt đầu từ item định danh (identity / 식별자) và công việc (work / 작업) per item** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. remember bộ nhớ đệm (cache / 캐시) theo key, không phải memoization toàn cục (global / 전역)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Hoặc tốt hơn compute trong ViewModel/lĩnh vực (domain / 도메인) nếu đó là ứng dụng (application / 애플리케이션) lô-gic (logic / 논리).

UI không nên trở thành data-processing engine.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **27. remember bộ nhớ đệm (cache / 캐시) theo key, không phải memoization toàn cục (global / 전역)** tiếp nhận điểm tựa từ **26. Expensive computation nên tách khỏi composition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. trạng thái (state / 상태) hoisting tạo reusable ranh giới (boundary / 경계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. `remember` bộ nhớ đệm (cache / 캐시) theo key, không phải memoization toàn cục (global / 전역)

Nếu `items` là mutable danh sách (list / 목록) cùng tham chiếu (reference / 참조) và mutate in-place, key có thể không đổi; remembered kết quả (result / 결과) stale.

Immutable đầu vào (input / 입력) làm `remember(key)` ngữ nghĩa (semantics / 의미론) đáng tin hơn.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **27. remember bộ nhớ đệm (cache / 캐시) theo key, không phải memoization toàn cục (global / 전역)** đã nêu tiêu chí phân biệt, còn **28. trạng thái (state / 상태) hoisting tạo reusable ranh giới (boundary / 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **29. Không hoist trạng thái (state / 상태) cao hơn mức cần thiết** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. trạng thái (state / 상태) hoisting tạo reusable ranh giới (boundary / 경계)

Thành phần (component / 컴포넌트) low-level:

```kotlin
@Composable
fun SearchField(
    value: String,
    onValueChange: (String) -> Unit
)
```

không cần biết ViewModel.

Đơn vị sở hữu (owner / 오너) phía trên quyết định trạng thái (state / 상태) nằm ở:

```text
remember
rememberSaveable
ViewModel
SavedStateHandle
repository
```

Trạng thái (state / 상태) hoisting không phải chỉ để preview; nó tách rendering khỏi quyền sở hữu (ownership / 소유권).

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **28. trạng thái (state / 상태) hoisting tạo reusable ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **29. Không hoist trạng thái (state / 상태) cao hơn mức cần thiết** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **30. điều hướng (navigation / 내비게이션) trạng thái (state / 상태) và screen trạng thái (state / 상태) là hai loại khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Không hoist trạng thái (state / 상태) cao hơn mức cần thiết

Nếu hover trạng thái (state / 상태) của một icon chỉ có ý nghĩa trong icon thành phần (component / 컴포넌트), đẩy nó lên app-level ViewModel làm coupling tăng.

Quy tắc (rule / 규칙):

> trạng thái (state / 상태) nên được hoist tới lowest dùng chung (common / 공통) đơn vị sở hữu (owner / 오너) cần đọc/ghi nó.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **30. điều hướng (navigation / 내비게이션) trạng thái (state / 상태) và screen trạng thái (state / 상태) là hai loại khác nhau** tiếp nhận điểm tựa từ **29. Không hoist trạng thái (state / 상태) cao hơn mức cần thiết** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. ngữ nghĩa (semantics / 의미론) cây (tree / 트리) là công khai (public / 공개) đặc tả hợp đồng (contract / 계약) cho khả năng tiếp cận (accessibility / 접근성) và kiểm thử (test / 테스트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. điều hướng (navigation / 내비게이션) trạng thái (state / 상태) và screen trạng thái (state / 상태) là hai loại khác nhau

Tuyến (route / 경로) định danh (identity / 식별자) như `articleId` nên nằm ở điều hướng (navigation / 내비게이션)/saved-state ranh giới (boundary / 경계).

Article content nên lấy từ repository.

UI transient trạng thái (state / 상태) như expanded section có thể ở cục bộ (local / 로컬) remember/saveable.

Không gom mọi thứ vào một ViewModel chỉ vì “single nguồn chuẩn (source of truth / 정본)”. nguồn chuẩn (source of truth / 정본) có phạm vi (scope / 범위).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **31. ngữ nghĩa (semantics / 의미론) cây (tree / 트리) là công khai (public / 공개) đặc tả hợp đồng (contract / 계약) cho khả năng tiếp cận (accessibility / 접근성) và kiểm thử (test / 테스트)** tiếp nhận điểm tựa từ **30. điều hướng (navigation / 내비게이션) trạng thái (state / 상태) và screen trạng thái (state / 상태) là hai loại khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. Merge ngữ nghĩa (semantics / 의미론) có thể thay đổi trải nghiệm khả năng tiếp cận (accessibility / 접근성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. ngữ nghĩa (semantics / 의미론) cây (tree / 트리) là công khai (public / 공개) đặc tả hợp đồng (contract / 계약) cho khả năng tiếp cận (accessibility / 접근성) và kiểm thử (test / 테스트)

UI nhìn bằng mắt có thể đúng nhưng ngữ nghĩa (semantics / 의미론) sai.

Ví dụ icon button chỉ có hình trái tim nhưng không có content description/trạng thái (state / 상태) description phù hợp. TalkBack người dùng (user / 사용자) không biết ý nghĩa.

Ngữ nghĩa (semantics / 의미론) cần mô tả **meaning và hành động (action / 동작)**, không chỉ visual.

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **32. Merge ngữ nghĩa (semantics / 의미론) có thể thay đổi trải nghiệm khả năng tiếp cận (accessibility / 접근성)** tiếp nhận điểm tựa từ **31. ngữ nghĩa (semantics / 의미론) cây (tree / 트리) là công khai (public / 공개) đặc tả hợp đồng (contract / 계약) cho khả năng tiếp cận (accessibility / 접근성) và kiểm thử (test / 테스트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. kiểm thử (test / 테스트) theo ngữ nghĩa (semantics / 의미론) tốt hơn kiểm thử (test / 테스트) theo hiện thực (implementation / 구현) detail** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Merge ngữ nghĩa (semantics / 의미론) có thể thay đổi trải nghiệm khả năng tiếp cận (accessibility / 접근성)

Một card gồm icon + title + subtitle có thể được expose thành nhiều nút (node / 노드) hoặc merge thành một meaningful nút (node / 노드).

Quyết định phụ thuộc tương tác (interaction / 상호작용).

Nếu toàn card clickable, một ngữ nghĩa (semantics / 의미론) nút (node / 노드) tổng hợp có thể phù hợp hơn nhiều fragment đọc rời rạc.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **33. kiểm thử (test / 테스트) theo ngữ nghĩa (semantics / 의미론) tốt hơn kiểm thử (test / 테스트) theo hiện thực (implementation / 구현) detail** tiếp nhận điểm tựa từ **32. Merge ngữ nghĩa (semantics / 의미론) có thể thay đổi trải nghiệm khả năng tiếp cận (accessibility / 접근성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. khả năng tiếp cận (accessibility / 접근성) trạng thái (state / 상태) phải cập nhật (update / 업데이트) cùng visual trạng thái (state / 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. kiểm thử (test / 테스트) theo ngữ nghĩa (semantics / 의미론) tốt hơn kiểm thử (test / 테스트) theo hiện thực (implementation / 구현) detail

Thay vì tìm nút (node / 노드) bằng nội bộ (internal / 내부) tag mọi nơi, ưu tiên user-visible ngữ nghĩa (semantic / 의미적) khi phù hợp:

```text
text
content description
role
state description
click action
```

Kiểm thử (test / 테스트) như người dùng (user / 사용자) nhìn hệ thống giúp refactor hiện thực (implementation / 구현) mà kiểm thử (test / 테스트) ít vỡ hơn.

TestTag vẫn hữu ích khi ngữ nghĩa (semantic / 의미적) selector không đủ hoặc cần nút (node / 노드) kỹ thuật cụ thể.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **34. khả năng tiếp cận (accessibility / 접근성) trạng thái (state / 상태) phải cập nhật (update / 업데이트) cùng visual trạng thái (state / 상태)** tiếp nhận điểm tựa từ **33. kiểm thử (test / 테스트) theo ngữ nghĩa (semantics / 의미론) tốt hơn kiểm thử (test / 테스트) theo hiện thực (implementation / 구현) detail** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35. Font scaling là bố cục (layout / 레이아웃) kiểm thử (test / 테스트), không chỉ khả năng tiếp cận (accessibility / 접근성) setting** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. khả năng tiếp cận (accessibility / 접근성) trạng thái (state / 상태) phải cập nhật (update / 업데이트) cùng visual trạng thái (state / 상태)

Toggle visual đổi màu nhưng ngữ nghĩa (semantics / 의미론) không đổi là bug tính đúng đắn (correctness / 정확성).

Ví dụ:

```text
visual: bookmarked
semantics: "Not bookmarked"
```

UI đã có hai nguồn chuẩn (source of truth / 정본).

Visual và ngữ nghĩa (semantics / 의미론) nên derive từ cùng trạng thái (state / 상태) snapshot.

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **35. Font scaling là bố cục (layout / 레이아웃) kiểm thử (test / 테스트), không chỉ khả năng tiếp cận (accessibility / 접근성) setting** tiếp nhận điểm tựa từ **34. khả năng tiếp cận (accessibility / 접근성) trạng thái (state / 상태) phải cập nhật (update / 업데이트) cùng visual trạng thái (state / 상태)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **36. RTL không chỉ mirror icon** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. Font scaling là bố cục (layout / 레이아웃) kiểm thử (test / 테스트), không chỉ khả năng tiếp cận (accessibility / 접근성) setting

Văn bản (text / 텍스트) lớn có thể làm:

```text
button clip
row overflow
text overlap
fixed-height component vỡ
```

Tránh hard-code height khi content có thể expand.

Kiểm thử (test / 테스트) font quy mô (scale / 규모) lớn là part của adaptive bố cục (layout / 레이아웃) tính đúng đắn (correctness / 정확성).

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **36. RTL không chỉ mirror icon** tiếp nhận điểm tựa từ **35. Font scaling là bố cục (layout / 레이아웃) kiểm thử (test / 테스트), không chỉ khả năng tiếp cận (accessibility / 접근성) setting** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **37. Edge-to-edge thay đổi trách nhiệm bố cục (layout / 레이아웃)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. RTL không chỉ mirror icon

Bố cục (layout / 레이아웃) phải phân biệt `start/end` với `left/right`.

Một số icon directional cần mirror; một số icon ngữ nghĩa (semantic / 의미적) không cần.

Văn bản (text / 텍스트) alignment, gesture direction và animation cũng có thể cần rà soát (review / 검토).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **37. Edge-to-edge thay đổi trách nhiệm bố cục (layout / 레이아웃)** tiếp nhận điểm tựa từ **36. RTL không chỉ mirror icon** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **38. IME là một động (dynamic / 동적) inset + focus hệ thống (system / 시스템)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. Edge-to-edge thay đổi trách nhiệm bố cục (layout / 레이아웃)

Khi content vẽ dưới hệ thống (system / 시스템) bars, app phải xử lý cửa sổ (window / 윈도우) insets phù hợp.

Không hard-code padding status bar.

Dùng inset APIs để bố cục (layout / 레이아웃) phản ứng với thiết bị (device / 장치) cutout, điều hướng (navigation / 내비게이션) chế độ (mode / 모드) và IME.

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **38. IME là một động (dynamic / 동적) inset + focus hệ thống (system / 시스템)** tiếp nhận điểm tựa từ **37. Edge-to-edge thay đổi trách nhiệm bố cục (layout / 레이아웃)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **39. Pointer input có lifetime theo key** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. IME là một động (dynamic / 동적) inset + focus hệ thống (system / 시스템)

Form bug thường đến từ việc xử lý keyboard như fixed bottom panel.

Cần lập luận (reasoning / 추론):

```text
focus owner
IME action
bring-into-view
window insets
scroll container
hardware keyboard
```

Form môi trường vận hành (production / 운영 환경) phải hoạt động khi keyboard resize, floating keyboard hoặc vật lý (physical / 물리적) keyboard.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **39. Pointer input có lifetime theo key** tiếp nhận điểm tựa từ **38. IME là một động (dynamic / 동적) inset + focus hệ thống (system / 시스템)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **40. Nested scroll là giao thức (protocol / 프로토콜) giữa parent và child** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 39. Pointer input có lifetime theo key
Phần này nối mạch Android vừa học với “39. Pointer input có lifetime theo key”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

```kotlin
Modifier.pointerInput(key) {
    detectGestures(...)
}
```

key đổi có thể restart gesture detector coroutine.

Nếu detector capture stale trạng thái (state / 상태), dùng key hoặc updated-state chiến lược (strategy / 전략) đúng.

Đầu vào (input / 입력) handling cũng là tác động (effect / 효과)/thời gian tồn tại (lifetime / 수명) bài toán (problem / 문제).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **40. Nested scroll là giao thức (protocol / 프로토콜) giữa parent và child** tiếp nhận điểm tựa từ **39. Pointer input có lifetime theo key** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **41. Animation cần mô hình (model / 모델) mục tiêu (target / 대상) trạng thái (state / 상태), không imperative timeline khắp nơi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 40. Nested scroll là giao thức (protocol / 프로토콜) giữa parent và child

Trong nested scroll, delta có thể được consume ở nhiều phase.

Đừng nghĩ “child scroll xong rồi parent scroll”. Pre-scroll/post-scroll và fling cooperation có thể phức tạp.

Khi implement collapsing toolbar hoặc coordinated motion, cần hiểu consumption đặc tả hợp đồng (contract / 계약) thay vì patch offset thủ công.

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **41. Animation cần mô hình (model / 모델) mục tiêu (target / 대상) trạng thái (state / 상태), không imperative timeline khắp nơi** tiếp nhận điểm tựa từ **40. Nested scroll là giao thức (protocol / 프로토콜) giữa parent và child** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **42. hiệu năng (performance / 성능) tối ưu hóa (optimization / 최적화) workflow** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 41. Animation cần mô hình (model / 모델) mục tiêu (target / 대상) trạng thái (state / 상태), không imperative timeline khắp nơi

Prefer:

```text
state A -> state B
Compose animation system interpolate
```

thay vì nhiều mutable progress variable được set thủ công.

Declarative animation giảm khả năng visual trạng thái (state / 상태) lệch ứng dụng (application / 애플리케이션) trạng thái (state / 상태).

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **41. Animation cần mô hình (model / 모델) mục tiêu (target / 대상) trạng thái (state / 상태), không imperative timeline khắp nơi** xác định đầu vào; **42. hiệu năng (performance / 성능) tối ưu hóa (optimization / 최적화) workflow** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **43. gỡ lỗi (debug / 디버그) bản dựng (build / 빌드) không đại diện bản phát hành (release / 릴리스) hiệu năng (performance / 성능)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 42. hiệu năng (performance / 성능) tối ưu hóa (optimization / 최적화) workflow

Đừng bắt đầu bằng refactor mã (code / 코드).

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

Ví dụ jank danh sách (list / 목록):

```text
recomposition?
layout?
draw?
image decode?
Binder call?
GC?
```

Nếu chưa biết bottleneck nằm ở đâu, tối ưu hóa (optimization / 최적화) chỉ là guess.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **42. hiệu năng (performance / 성능) tối ưu hóa (optimization / 최적화) workflow** xác định đầu vào; **43. gỡ lỗi (debug / 디버그) bản dựng (build / 빌드) không đại diện bản phát hành (release / 릴리스) hiệu năng (performance / 성능)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **44. Baseline Profile không sửa kiến trúc (architecture / 아키텍처) chậm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 43. gỡ lỗi (debug / 디버그) bản dựng (build / 빌드) không đại diện bản phát hành (release / 릴리스) hiệu năng (performance / 성능)

Gỡ lỗi (debug / 디버그) có instrumentation và thiếu tối ưu R8/AOT/profile hành vi (behavior / 동작) giống bản phát hành (release / 릴리스).

Đánh giá hiệu năng (performance / 성능) môi trường vận hành (production / 운영 환경) nên dùng release-like bản dựng (build / 빌드) và benchmark tooling phù hợp.

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **44. Baseline Profile không sửa kiến trúc (architecture / 아키텍처) chậm** tiếp nhận điểm tựa từ **43. gỡ lỗi (debug / 디버그) bản dựng (build / 빌드) không đại diện bản phát hành (release / 릴리스) hiệu năng (performance / 성능)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **45. Frame ngân sách (budget / 예산) là end-to-end ngân sách (budget / 예산)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 44. Baseline Profile không sửa kiến trúc (architecture / 아키텍처) chậm

Baseline Profiles giúp precompile trọng yếu (critical / 중요) đường đi mã (code path / 코드 경로).

Nếu startup khối (block / 블록) 500ms do synchronous cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션) trên main luồng thực thi (thread / 스레드), profile không biến nghiệp vụ (business / 비즈니스) công việc (work / 작업) đó thành miễn phí.

Profile là tối ưu hóa (optimization / 최적화) tầng (layer / 계층) sau khi đường găng (critical path / 임계 경로) đã hợp lý.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **45. Frame ngân sách (budget / 예산) là end-to-end ngân sách (budget / 예산)** tiếp nhận điểm tựa từ **44. Baseline Profile không sửa kiến trúc (architecture / 아키텍처) chậm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **46. Recomposition counter có thể gây hiểu nhầm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 45. Frame ngân sách (budget / 예산) là end-to-end ngân sách (budget / 예산)

Một frame miss deadline có thể do:

```text
composition 3ms
layout 5ms
draw 2ms
GC 8ms
```

tổng vượt ngân sách (budget / 예산) dù từng phase riêng không quá lớn.

Hiệu năng (performance / 성능) rà soát (review / 검토) phải xem toàn dấu vết (trace / 추적).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **45. Frame ngân sách (budget / 예산) là end-to-end ngân sách (budget / 예산)** đã nêu tiêu chí phân biệt, còn **46. Recomposition counter có thể gây hiểu nhầm** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **47. Stable key không cứu item nếu mô hình (model / 모델) thay đổi toàn bộ mỗi frame** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 46. Recomposition counter có thể gây hiểu nhầm

Một composable recompose 1.000 lần nhưng mỗi lần 5 microsecond có thể không đáng lo.

Một composable recompose 10 lần nhưng mỗi lần làm expensive sort 20ms mới là vấn đề.

Chi phí (cost / 비용) > count.

---

> **Chuyển mạch:** Trong **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **46. Recomposition counter có thể gây hiểu nhầm** đã nêu tiêu chí phân biệt, còn **47. Stable key không cứu item nếu mô hình (model / 모델) thay đổi toàn bộ mỗi frame** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **48. Compose correctness checklist** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 47. Stable key không cứu item nếu mô hình (model / 모델) thay đổi toàn bộ mỗi frame

Nếu ViewModel tạo danh sách (list / 목록) mô hình (model / 모델) mới với random id hoặc unstable equality mỗi emission, Lazy danh sách (list / 목록) mất khả năng reuse tốt.

Định danh (identity / 식별자) phải bắt đầu từ lĩnh vực (domain / 도메인)/mô hình (model / 모델) thiết kế (design / 설계), không chỉ thêm `key = { it.id }` ở UI.

---

> **Chuyển mạch:** Ở chặng này của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **48. Compose correctness checklist** tiếp nhận điểm tựa từ **47. Stable key không cứu item nếu mô hình (model / 모델) thay đổi toàn bộ mỗi frame** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **49. Kết luận** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 48. Compose correctness checklist
Phần này nối mạch Android vừa học với “48. Compose correctness checklist”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

| Câu hỏi | Ý nghĩa |
|---|---|
| trạng thái (state / 상태) đơn vị sở hữu (owner / 오너) ở đâu? | thời gian tồn tại (lifetime / 수명) đúng |
| trạng thái (state / 상태) read ở phase nào? | vô hiệu hóa (invalidation / 무효화) chi phí (cost / 비용) |
| tác động (effect / 효과) key đúng chưa? | stale/restart hành vi (behavior / 동작) |
| Cleanup ở đâu? | leak prevention |
| Item định danh (identity / 식별자) stable không? | remembered trạng thái (state / 상태)/reuse |
| mô hình (model / 모델) immutable/stable thật không? | skip tính đúng đắn (correctness / 정확성) |
| ngữ nghĩa (semantics / 의미론) phản ánh visual trạng thái (state / 상태) không? | khả năng tiếp cận (accessibility / 접근성) tính đúng đắn (correctness / 정확성) |
| Font/RTL/insets đã kiểm thử (test / 테스트) chưa? | adaptive tính đúng đắn (correctness / 정확성) |
| hiệu năng (performance / 성능) đo trên release-like bản dựng (build / 빌드) chưa? | evidence-based tối ưu hóa (optimization / 최적화) |
| Bottleneck là composition/bố cục (layout / 레이아웃)/draw hay bên ngoài (external / 외부) công việc (work / 작업)? | fix đúng tầng |

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ sâu (depth / 깊이) Lab 04 — Compose thời gian chạy (runtime / 런타임), trạng thái (state / 상태), hiệu năng (performance / 성능) và ngữ nghĩa (semantics / 의미론)**, **49. Kết luận** gom các mảnh từ **48. Compose correctness checklist** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 49. Kết luận

Compose trở nên dễ lập luận (reasoning / 추론) khi xem nó như một thời gian chạy (runtime / 런타임) có định danh (identity / 식별자), snapshot phụ thuộc (dependency / 의존성) và phase-specific vô hiệu hóa (invalidation / 무효화).

Mô hình tư duy (mental model / 사고 모델):

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

> **Bàn giao:** Sau **49. Kết luận**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
