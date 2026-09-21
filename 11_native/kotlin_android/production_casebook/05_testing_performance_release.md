# Case 05 — Testing, Performance, CI/CD và Release Engineering

Một Android app “chạy được trên máy dev” còn rất xa production. Production quality đòi hỏi ba vòng phản hồi liên tục: **correctness** được bảo vệ bằng test và static analysis; **performance** được đo bằng profiler/benchmark thay vì cảm giác; **release** được kiểm soát bằng reproducible build, signing, staged rollout, telemetry và rollback plan.

Chương này không liệt kê tool đơn lẻ mà xây một quality pipeline từ code tới Play release.

## 1. Test theo risk, không theo tỷ lệ thần thánh

“70% unit, 20% integration, 10% UI” không phải luật. Test strategy phải phản ánh failure cost.

Pure business rule nên có unit test nhanh. Mapping/network serialization cần contract test. Room migration cần migration test thật. Navigation/deep link cần integration/UI test. Payment/auth cần nhiều tầng hơn một màn hình brochure.

Mục tiêu là mỗi critical behavior có test ở tầng rẻ nhất đủ chứng minh behavior đó.

## 2. Unit test domain logic

Một use case thuần Kotlin không cần emulator:

```kotlin
class CalculateCartTotalUseCase {
    operator fun invoke(items: List<CartItem>): Money =
        items.fold(Money.zero()) { total, item ->
            total + item.price * item.quantity
        }
}
```

Test boundary quan trọng hơn happy path:

```kotlin
@Test
fun zero_quantity_does_not_change_total() {
    val result = CalculateCartTotalUseCase()(
        listOf(CartItem(price = Money.of(10), quantity = 0))
    )
    assertEquals(Money.zero(), result)
}
```

## 3. Fake thường hữu ích hơn mock cho stateful repository

Mock rất tốt để verify interaction nhỏ, nhưng với Flow/repository stateful, fake có thể mô phỏng behavior tự nhiên hơn.

```kotlin
class FakeArticlesRepository : ArticlesRepository {
    private val data = MutableStateFlow<List<Article>>(emptyList())

    override fun observeArticles(): Flow<List<Article>> = data

    override suspend fun refresh() = Unit

    override suspend fun toggleBookmark(articleId: String) {
        data.update { items ->
            items.map { if (it.id == articleId) it.copy(bookmarked = !it.bookmarked) else it }
        }
    }
}
```

ViewModel test có thể assert state transition thay vì verify “method X được gọi đúng một lần” trong mọi trường hợp.

## 4. Coroutine test và virtual time

Code dùng `delay`, retry/backoff hoặc debounce không nên làm test ngủ thật.

```kotlin
@Test
fun search_is_debounced() = runTest {
    viewModel.onQueryChanged("kot")
    advanceTimeBy(299)
    assertEquals(0, repository.searchCount)

    advanceTimeBy(1)
    runCurrent()
    assertEquals(1, repository.searchCount)
}
```

Inject dispatcher/scheduler-friendly dependency thay vì hard-code thread behavior khắp nơi.

## 5. Main dispatcher trong test

ViewModel dùng `viewModelScope` cần test Main dispatcher. Có thể dùng test rule thiết lập `Dispatchers.Main` thành `StandardTestDispatcher` và reset sau test.

Điểm quan trọng là tất cả coroutine trong test chia sẻ cùng `TestCoroutineScheduler` nếu muốn deterministic virtual time.

## 6. Flow test

Với StateFlow, nhiều case có thể assert `value`. Với Flow sequence, có thể collect bằng test helper/library phù hợp hoặc tự collect có kiểm soát.

Test nên chú ý conflation: StateFlow đại diện state mới nhất, không đảm bảo test observer thấy mọi intermediate value nếu producer chạy nhanh. Nếu cần assert sequence event, chọn primitive phù hợp.

## 7. Room test

DAO query nên test với database thực in-memory hoặc test DB, không mock SQL behavior.

Test transaction/invariant như:

- upsert preserve local bookmark;
- delete cascade đúng;
- unique constraint đúng;
- relation query không duplicate;
- transaction rollback khi một bước fail.

Migration test phải dùng schema cũ và dữ liệu edge case như đã trình bày ở Case 03.

## 8. Network contract test

Không cần gọi production backend trong unit test. Dùng fake HTTP server để test:

- URL/path/query/header;
- serialization/deserialization;
- 2xx/4xx/5xx mapping;
- timeout/cancellation;
- malformed response;
- unknown field/enum compatibility.

Contract test hữu ích hơn mock Retrofit interface vì nó test boundary wire thực tế.

## 9. Compose UI test

Pure content composable giúp test dễ:

```kotlin
composeTestRule.setContent {
    ArticlesScreen(
        state = ArticlesUiState(items = sampleItems),
        onBookmark = { bookmarkedId = it },
        onOpenArticle = {}
    )
}

composeTestRule
    .onNodeWithText("Kotlin Coroutines")
    .assertIsDisplayed()
```

Dùng semantics/testTag khi text/content description không đủ ổn định, nhưng đừng làm UI chỉ để phục vụ test nếu semantics user-facing có thể dùng.

## 10. Screenshot test và visual regression

Logic test không phát hiện padding sai, dark theme broken hoặc text overflow. Screenshot test hữu ích cho design system/component ổn định.

Cần kiểm soát font, density, locale, device config để giảm flaky pixel diff. Với dynamic content, test component/state cụ thể hơn full app screenshot.

## 11. Accessibility test

Quality gate nên kiểm tra content description, touch target, contrast, font scaling và semantics tree. Một screen “đẹp” ở font 1.0 có thể unusable ở font scale lớn.

Test manual với TalkBack vẫn quan trọng vì automated rule không đánh giá được toàn bộ reading order và interaction semantics.

## 12. Instrumented test chọn lọc

Instrumented test chậm hơn local JVM, nên dành cho behavior phụ thuộc Android framework/device: permission, Activity lifecycle, database integration đặc thù, deep link/task behavior, biometric/credential flow có test harness phù hợp.

Không biến mọi unit test thành emulator test.

## 13. End-to-end test ít nhưng giá trị cao

Một số user journey critical nên có E2E smoke test:

```text
cold start
→ restore session
→ open home
→ create item
→ item appears
→ restart app
→ item persists
```

E2E dễ flaky nếu phụ thuộc backend/network thật. Có thể dùng controlled test environment, fake backend hoặc hermetic dependency tùy mục tiêu.

## 14. Static analysis là test chạy trước runtime

Android Lint, Kotlin compiler warning, detekt/ktlint hoặc tool tương đương giúp bắt issue sớm. Nhưng rule phải có owner và policy, không bật hàng trăm rule rồi suppress toàn bộ.

CI nên fail trên warning quan trọng như exported component không an toàn, resource issue, API misuse, Compose stability issue có rule tương ứng, hoặc architecture dependency violation nếu project có custom rule.

## 15. Performance: đo trước khi tối ưu

Bốn nhóm metric thường quan trọng:

- startup: cold/warm/hot startup;
- frame rendering: jank/frame time;
- memory: allocation, heap growth, leak;
- resource: CPU, battery, network, disk.

Không optimize một `map` nhỏ trong khi main thread đang parse 5 MB JSON.

## 16. Startup budget

Application startup dễ bị chậm vì DI graph eager, SDK initialization, database open, disk I/O hoặc network setup trên main thread.

Phân loại init:

```text
must before first frame
should before first interaction
can lazy after screen visible
can defer until feature first used
```

Không phải SDK nào cũng cần init trong `Application.onCreate()`.

## 17. Macrobenchmark

Macrobenchmark đo behavior như startup/scroll ở app build gần production hơn unit benchmark.

Một benchmark tốt có scenario ổn định, warmup/iteration hợp lý và metric cụ thể. So sánh regression theo baseline thay vì nhìn một con số một lần.

## 18. Baseline Profiles

Baseline Profile giúp runtime precompile hot code path, cải thiện startup và interaction. Profile cần đại diện journey thực tế: launch, navigate screen chính, scroll/list interaction.

Profile cũ không nên được coi là “set and forget”; khi app flow thay đổi, regenerate/review.

## 19. Perfetto/System Trace

Khi UI jank, trace giúp thấy main thread làm gì, binder, scheduling, I/O, GC và frame timeline. Đây là bước chuyển từ đoán “Compose chậm” sang biết exact work gây frame miss.

Một trace investigation nên ghi:

```text
symptom → reproduction → trace marker → root cause → fix → benchmark before/after
```

## 20. Compose performance

Recomposition không mặc định xấu. Vấn đề là expensive work trong composition, unstable parameter gây invalidation rộng, allocation nhiều trong hot path hoặc layout/draw quá nặng.

Đưa calculation nặng ra khỏi composition hoặc dùng memoization phù hợp:

```kotlin
val filtered by remember(items, query) {
    derivedStateOf { items.filter { it.matches(query) } }
}
```

Nhưng không bọc mọi expression bằng `remember`. Memoization cũng có complexity/memory cost.

## 21. Leak investigation

Leak thường đến từ object lifetime sai: singleton giữ Activity, listener không unregister, coroutine scope dài hơn owner, callback giữ Fragment/View, static cache giữ large object.

Heap dump/leak detector chỉ ra reference chain. Fix root ownership, không chỉ set random variable `null`.

## 22. ANR

ANR không chỉ do infinite loop. Sync disk I/O, binder call lâu, lock contention, heavy serialization hoặc main thread chờ worker đều có thể gây freeze.

Một mutex dùng sai trên main thread hoặc `runBlocking` trong callback framework cũng có thể tạo ANR/deadlock.

## 23. Release build phải khác debug

Debug build thường bật logging, inspection, mock menu và không minify. Release cần:

- release signing;
- R8/minification/resource shrink nếu phù hợp;
- debug endpoint/menu bị loại;
- secret/config production đúng;
- network security policy production;
- crash/analytics mapping file upload;
- `android:debuggable=false` theo build system;
- versionCode/versionName traceable.

Không test performance trên debug build rồi kết luận release performance.

## 24. R8 và keep rule

Reflection/serialization/JNI có thể cần keep metadata/class. Không thêm `-keep class ** { *; }` để “fix crash” vì nó vô hiệu hóa shrink lớn.

Tìm boundary nào cần reflection và giữ tối thiểu. Library nên cung cấp consumer ProGuard rule nếu cần.

Release test phải chạy minified build vì bug R8 chỉ xuất hiện ở đó.

## 25. Signing

Signing key là identity update của app. Mất key hoặc leak key là incident nghiêm trọng. Với Play App Signing, quản lý upload key và Play signing flow đúng.

Không commit keystore/password vào repository. CI lấy secret từ secure secret store và giới hạn quyền.

## 26. Reproducible dependency graph

Version catalog/BOM giúp centralize version. Dependency locking hoặc verification giúp giảm build “hôm nay khác hôm qua”.

CI nên có command rõ ràng build từ clean checkout. Nếu chỉ máy một developer build được vì local Maven cache/manual SDK file, pipeline chưa reproducible.

## 27. CI stages

Một pipeline điển hình:

```text
checkout
→ verify formatting/static analysis
→ unit tests
→ build debug/release-like artifacts
→ integration/instrumented tests selected
→ lint
→ generate signed artifact in protected job
→ upload mapping/baseline metadata
→ publish internal track
```

Không nhất thiết mọi PR chạy full device matrix; có thể tách fast PR gate và nightly/release suite.

## 28. Build cache và CI cache

Cache giúp nhanh nhưng cache key sai có thể gây artifact stale. Cache Gradle theo file/version phù hợp, không cache output tùy tiện mà không hiểu invalidation.

Đừng dùng cache để che build dependency không khai báo. Clean build định kỳ hữu ích phát hiện hidden dependency.

## 29. Staged rollout

Không release 100% user ngay khi có thể rollout dần. Staged rollout cho phép quan sát crash/ANR/business metric ở cohort nhỏ.

Quy trình:

```text
internal/QA
→ small production percentage
→ observe technical + business metrics
→ expand gradually
→ halt/rollback if regression
```

Rollout percentage không cứu được nếu backend/schema change không backward-compatible.

## 30. Kill switch và feature flag

Feature flag cho phép disable một feature server-side khi issue. Nhưng flag phải có lifecycle: owner, default, expiry/removal date.

Một app đầy flag vĩnh viễn tạo state-space khó test. Sau rollout ổn định, remove obsolete flag/code path.

## 31. Rollback

Trước release hỏi: nếu app version mới gây lỗi, rollback bằng cách nào?

Nếu database migration irreversible hoặc backend API đã drop compatibility, rollback binary có thể không đủ. Vì vậy release engineering cần backward compatibility window.

## 32. Crash, ANR và symbolication

Minified release stack trace cần mapping file để deobfuscate. Native crash cần symbol tương ứng. Artifact/mapping phải gắn với versionCode/build ID và lưu đủ lâu để điều tra crash cũ.

## 33. Observability quality gate

Trước rollout, dashboard cần biết ít nhất:

- crash-free users/sessions;
- ANR rate;
- startup/jank key metric;
- login/payment/sync success rate nếu critical;
- backend error increase;
- adoption theo version.

Một release “không có ticket” không có nghĩa healthy nếu telemetry không nhìn thấy failure.

## 34. Privacy trong telemetry

Không log/token/user content thừa. Event schema phải biết field nào PII. Sampling/redaction/retention cần policy.

Debug log có thể verbose hơn production nhưng vẫn không nên in password/token.

## 35. Release checklist theo invariant

Thay vì checklist “bấm 50 ô” không hiểu lý do, nhóm theo invariant:

**Correctness**: test/lint pass, migration tested, minified build smoke-tested.

**Security**: prod endpoint, signing, no debug backdoor, dependency risk reviewed.

**Performance**: critical macrobenchmark không regression vượt budget.

**Operability**: telemetry, mapping/symbol, feature flag/rollback plan sẵn.

**Compatibility**: backend/schema/target SDK behavior được kiểm tra.

## 36. Senior notes

Testing không phải mục tiêu coverage percentage; nó là confidence system. Performance không phải tối ưu microbenchmark; nó là budget + trace + regression detection. CI/CD không phải YAML dài; nó là khả năng tạo artifact lặp lại, kiểm chứng và phát hành có kiểm soát.

Một team trưởng thành có thể trả lời: “PR này thay invariant nào?”, “test nào bảo vệ nó?”, “metric nào phát hiện regression?”, “release bao nhiêu phần trăm trước?”, “nếu fail thì rollback/disable thế nào?”. Khi câu trả lời rõ, Android engineering đã vượt xa mức chỉ biết API.
