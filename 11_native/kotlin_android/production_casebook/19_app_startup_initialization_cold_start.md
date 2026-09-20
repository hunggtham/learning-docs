# Case 19 — App Startup, Initialization, Cold Start và Startup Performance

Một app có thể có architecture sạch nhưng vẫn tạo trải nghiệm tệ nếu cold start chậm, initialization chạy sai thread, SDK tự động khởi tạo quá sớm hoặc splash screen che một main-thread stall dài. Startup là nơi nhiều subsystem cùng tranh thời gian: process creation, class loading, `Application`, ContentProvider auto-init, DI graph, database/network config, Compose first frame và analytics/crash SDK.

Chapter này xây mental model startup từ OS process tới first useful frame, sau đó thiết kế initialization theo dependency/lifetime thay vì “nhét hết vào `Application.onCreate()`”.

## 1. Cold, warm và hot start là ba tình huống khác nhau

**Cold start**: process chưa tồn tại. System phải tạo process, runtime, Application và Activity trước khi render UI.

**Warm start**: process còn nhưng Activity cần recreate hoặc app quay lại từ state không còn UI fully resident.

**Hot start**: Activity/task còn gần như sẵn, resume nhanh.

Khi nói “startup 800 ms”, phải nói scenario nào. Tối ưu hot start không giải cold-start regression.

## 2. Startup critical path

Một mental model đơn giản:

```text
launcher tap/deep link/notification
→ process creation nếu cần
→ runtime/class loading
→ Application creation
→ auto-initializers/providers
→ Activity creation
→ theme/splash
→ Compose/View inflate
→ first frame
→ content/data ready
```

Không phải mọi bước đều chạy tuần tự tuyệt đối, nhưng model đủ để hỏi “work này có nằm trên path đến first frame không?”.

## 3. Time to Initial Display và Time to Full Display

**TTID** phản ánh thời gian tới frame đầu tiên meaningful enough để hiển thị. **TTFD** phản ánh thời gian tới khi UI thực sự ready với content quan trọng.

Một app có thể TTID đẹp bằng cách render skeleton sớm nhưng TTFD rất chậm. Product performance nên theo cả perceived readiness, không chỉ launcher-to-first-pixel.

## 4. `Application.onCreate()` là global startup hotspot

`Application.onCreate()` chạy sớm trên main thread của process. Code blocking ở đây trì hoãn mọi entry point.

Không nên:

- open/migrate database nặng synchronous;
- đọc file lớn;
- network call;
- parse config lớn;
- eagerly create mọi repository/service;
- initialize SDK không cần cho first screen.

Global initialization phải nhỏ, deterministic và main-safe.

## 5. ContentProvider auto-initialization

Nhiều libraries dùng `ContentProvider` để auto-init trước/around Application startup. Điều này tiện nhưng khiến work xuất hiện ngoài `Application.onCreate()`.

Khi startup chậm, inspect merged manifest và trace providers. Một SDK có thể add provider qua manifest dependency.

Không kết luận `Application` nhẹ nghĩa startup nhẹ.

## 6. AndroidX App Startup

AndroidX Startup cung cấp cách khai báo initializer dependency và centralize initialization graph. Nó hữu ích khi nhiều component cần ordered initialization.

Concept:

```kotlin
class AnalyticsInitializer : Initializer<Analytics> {
    override fun create(context: Context): Analytics {
        return Analytics.create(context)
    }

    override fun dependencies(): List<Class<out Initializer<*>>> = emptyList()
}
```

Tuy nhiên framework không biến heavy work thành free. Nếu initializer vẫn làm disk I/O trên main thread, startup vẫn chậm.

## 7. Eager vs lazy initialization

Một dependency nên eager chỉ nếu:

- mọi entry point cần nó ngay;
- initialization rất rẻ;
- delay sẽ gây race/correctness issue khó hơn.

Lazy tốt khi feature-specific hoặc expensive. Nhưng lazy không đồng nghĩa “first use muốn block bao lâu cũng được”. Nếu user mở feature, latency vẫn tồn tại—chỉ chuyển vị trí.

Có thể prewarm sau first frame hoặc khi device idle phù hợp.

## 8. Dependency graph và initialization graph khác nhau

DI graph nói object phụ thuộc object nào. Initialization graph nói side effect nào phải hoàn thành trước side effect khác.

Một singleton `Database` có thể được inject lazy nhưng schema migration vẫn là expensive initialization lúc first open.

Một analytics interface có thể available sớm nhưng backend upload worker init sau.

Không dùng DI framework như implicit startup scheduler.

## 9. Hilt/Dagger startup cost

Generated DI thường efficient nhưng object graph lớn/eager singleton constructors có thể tạo cost. Constructor nên gán dependency, không làm I/O hoặc heavy computation.

Anti-pattern:

```kotlin
@Singleton
class UserRepository @Inject constructor(
    db: AppDatabase
) {
    init {
        runBlocking { /* load everything */ }
    }
}
```

Constructor side effects làm creation path khó kiểm soát và test.

## 10. SplashScreen API

Modern Android có SplashScreen API/system splash behavior. Splash là visual transition trong startup, không phải license để block main thread.

Nếu cần giữ splash tới condition, condition phải ngắn và bounded. Long authentication/network sync nên chuyển sang real loading UI.

Một splash đứng 5 giây vẫn là app chậm dù animation đẹp.

## 11. Startup route: auth state và deep link

App thường phải quyết định route đầu:

```text
cold start
→ restore session locally
→ resolve incoming intent/deep link
→ decide auth gate
→ render route
```

Không cần gọi backend trước khi render nếu local durable session metadata đủ quyết định provisional route. Network validation có thể update sau với correct state transition.

Case 02/04 đã cover auth/navigation; startup đặt chúng trên critical path.

## 12. Local state đọc bao nhiêu là đủ

DataStore/Room read nhỏ có thể cần để quyết route, nhưng loading toàn profile/feed database trước frame là không cần.

Tách:

- **startup-critical state**: theme, account existence, onboarding completed, pending route;
- **screen data**: load sau khi UI owner xuất hiện.

Minimize startup-critical dataset.

## 13. Main thread và disk I/O

Disk I/O latency có tail lớn tùy device/storage pressure. Nếu API cho synchronous disk read trong startup, hãy xem trace/StrictMode.

Một read “chỉ 5 ms trên Pixel dev” có thể 100+ ms trên low-end device dưới I/O contention.

Production performance phải quan tâm percentile, không chỉ median developer phone.

## 14. Class loading và static initialization

Large class graph, static initializer và reflection có thể tăng startup.

Kotlin `object`, top-level property hoặc companion static initialization có thể tạo work lúc class load.

Không đặt heavy expression vào global property:

```kotlin
val expensiveConfig = parseHugeConfig(loadFile()) // bad as implicit class init
```

Prefer explicit/lazy lifecycle-controlled creation.

## 15. Compose first composition

Compose startup gồm Activity setup, composition, layout, draw và potential resource/font/image work.

First screen nên tránh:

- huge list computation synchronous trong composable;
- decoding bitmap lớn trên main;
- creating unstable giant state graph;
- effect launch gây immediate recomposition storm;
- reading disk directly trong composable.

UI nên render from already modeled state; async load thuộc ViewModel/repository layer.

## 16. Baseline Profiles

Baseline Profile cho runtime biết code paths quan trọng để cải thiện compilation/startup/runtime performance. Đây không phải magic replacement cho slow algorithm/main-thread I/O.

Profile nên cover representative startup/critical journeys. Macrobenchmark đo benefit với profile enabled/disabled.

Nếu app startup 2 giây do network blocking main thread, Baseline Profile không sửa architecture error đó.

## 17. Macrobenchmark startup measurement

Macrobenchmark có thể đo cold/warm startup trên release-like build.

Key principle:

```text
benchmark production-like artifact
+ representative device
+ repeated iteration
+ controlled compilation mode
```

Debug build timing không đại diện release vì instrumentation/JIT/minification khác.

Theo dõi percentile/distribution, không chỉ một run.

## 18. Perfetto/System Trace

Khi startup chậm, trace cho evidence về main thread slices, binder calls, disk I/O, GC, class loading, rendering và scheduler.

Workflow:

```text
measure regression
→ capture trace
→ locate critical path
→ identify blocking work
→ move/remove/defer
→ remeasure
```

Không optimize bằng cảm giác hoặc số log timestamps rời rạc nếu Perfetto có thể cho timeline đầy đủ.

## 19. StrictMode trong development

StrictMode giúp detect disk/network operation trên main thread và một số resource misuse. Bật policy phù hợp trong debug/dev giúp bắt startup anti-pattern sớm.

Không dùng StrictMode penalty làm production crash mechanism tùy tiện. Mục tiêu là development signal.

## 20. SDK initialization governance

Mỗi third-party SDK thêm startup code cần owner và budget.

Inventory nên ghi:

| SDK | Need before first frame? | Auto provider? | Main-thread cost | Can lazy-init? | Owner |
|---|---|---|---|---|---|
| crash reporting | often early | maybe | measure | partially | platform |
| analytics | usually no hard block | maybe | measure | yes | data |
| ads | screen-specific | often | potentially high | yes | monetization |

Không để 10 SDK cùng tự auto-init vì vendor default.

## 21. Crash reporting nên init sớm nhưng nhỏ

Crash SDK cần available đủ sớm để capture startup crash, nhưng configuration không nên perform heavy network/remote fetch synchronously.

Upload có thể defer/background. Crash metadata critical có thể set sau khi local user/session known.

## 22. Remote Config không được là hard startup dependency

Nếu app cần network Remote Config trước khi render, outage config service có thể làm app không mở.

Use cached defaults/local persisted config và refresh async. Critical kill-switch cần previous known state và safe default.

Startup phải resilient khi network offline.

## 23. Database migration trên startup

Room DB first open có thể chạy migration. Large migration ngay khi user launch tạo long startup hoặc ANR nếu sai thread.

Schema migration strategy nên:

- benchmark realistic DB size;
- avoid unnecessary full-table rewrite;
- run via correct thread path;
- show durable migration/loading UX nếu truly long;
- backup/rollback compatibility đã được Case 03 cover.

“Migration chỉ chạy một lần” không làm user experience ít quan trọng.

## 24. Process-specific initialization

Nếu app có multi-process component, `Application.onCreate()` có thể chạy trong nhiều process.

Không giả định code startup chỉ chạy main app process. Heavy analytics/database initialization có thể bị duplicate ở service/provider process.

Nếu multi-process thật sự cần, detect process name và initialize only required subsystem per process. Tránh multi-process trừ khi requirement rõ vì complexity tăng mạnh.

## 25. Startup entry points không chỉ launcher icon

Cold start có thể đến từ:

- launcher;
- notification tap;
- deep link/App Link;
- share intent;
- widget;
- shortcut;
- service/receiver/provider.

Case 14 đã cover system surfaces. Startup design phải đảm bảo initialization order đúng cho tất cả entry point, không chỉ MainActivity path.

## 26. Lazy singleton race

Lazy initialize shared resource từ nhiều threads cần thread-safety. Kotlin `lazy` default synchronized semantics có thể đủ cho object initialization đơn giản, nhưng async initialization cần state machine.

Không dùng nullable global + `if (x == null) x = create()` unsynchronized.

Async resource có thể model:

```text
Uninitialized
→ Initializing(deferred)
→ Ready
→ Failed(retry policy)
```

Multiple callers await cùng initialization thay vì chạy duplicate.

## 27. Prewarming

Sau first frame, app có thể prewarm resource có xác suất sắp dùng cao: database connection, decoder, cache index, feature module.

Prewarm là speculation. Nếu làm quá nhiều sẽ tranh CPU/I/O với user interaction và tăng battery.

Chỉ prewarm thứ có measured benefit và bounded cost.

## 28. Startup memory budget

Eager initialization không chỉ tốn thời gian, còn tăng resident memory. Low-end device có thể bị memory pressure sớm.

Một SDK singleton có cache 20 MB “để nhanh” có thể làm process dễ kill background hơn.

Startup optimization nên xem time + memory + battery trade-off.

## 29. Startup network anti-pattern

Never require network round trip để app process trở thành usable nếu product có thể render offline/cached state.

Network có unbounded tail: DNS, TLS, captive portal, packet loss, server latency.

Nếu security requires fresh server validation trước sensitive action, gate **sensitive action**, không nhất thiết gate toàn app shell.

## 30. First frame vs first useful content

Đẩy mọi work sau first frame để metric đẹp có thể tạo skeleton nhấp nháy và content arrive quá muộn.

Optimize user-perceived journey:

```text
fast stable shell
→ critical local content
→ async remote refresh
```

Không metric-game bằng blank frame.

## 31. Startup budget

Team có thể đặt budget theo representative device tier, ví dụ TTID/TTFD percentile. Con số cụ thể tùy product; quan trọng là có budget và regression gate.

Build/CI benchmark nên detect trend chứ không fail vì noise một run. Performance test cần statistical tolerance.

## 32. Startup regression ownership

Nếu every feature có thể thêm initializer tự do, startup sẽ chậm dần theo thời gian.

Policy tốt:

- new eager initializer cần justification;
- owner + measured cost;
- trace before/after;
- prefer feature-local lazy init;
- review merged manifest providers;
- startup benchmark in release pipeline.

## 33. Case study mental model

Giả sử app cold start cần theme, auth state, analytics và feed.

Bad flow:

```text
Application
→ init every SDK
→ open/migrate DB
→ fetch remote config
→ validate token network
→ load feed network
→ Activity
```

Better flow:

```text
process
→ minimal crash/config bootstrap
→ Activity + splash/system theme
→ read tiny local startup state
→ render authenticated shell or login
→ async feed from local source of truth
→ remote refresh
→ lazy/noncritical SDK init after first frame
```

Không phải mọi app giống nhau, nhưng critical path thinking áp dụng rộng.

## 34. Senior startup checklist

Trước release, hỏi:

- cold/warm/hot startup measured chưa;
- main thread có disk/network/blocking lock không;
- merged manifest có provider auto-init mới không;
- `Application` constructor/onCreate làm gì;
- DI singleton nào eager/heavy;
- DB migration worst-case duration;
- release Baseline Profile valid không;
- notification/deep-link cold start test chưa;
- low-end device percentile thế nào;
- startup crash/ANR metrics segment theo version/device chưa.

## 35. Official references

- App startup time: https://developer.android.com/topic/performance/vitals/launch-time
- Baseline Profiles: https://developer.android.com/topic/performance/baselineprofiles/overview
- Macrobenchmark: https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview
- App Startup library: https://developer.android.com/topic/libraries/app-startup
- Perfetto/System tracing: https://developer.android.com/topic/performance/tracing

Performance guidance evolve cùng runtime/toolchain. Benchmark trên release-like artifact và representative devices luôn quan trọng hơn con số trong tutorial.