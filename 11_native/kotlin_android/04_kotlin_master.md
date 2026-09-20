# Kotlin + Android Master Note — Master / Production Engineering Supplement

> Mục tiêu: bao phủ các chủ đề còn thiếu để tiến tới mức thiết kế platform/app architecture, tối ưu compiler/build/runtime, API/library design, large-scale Android, Kotlin Multiplatform awareness và production governance.

## Mục lục

1. Version model: Kotlin 1.x → 2.x và Android toolchain
2. K2 compiler và language evolution
3. Kotlin/JVM bytecode awareness
4. Value classes và allocation model
5. Context parameters / language evolution awareness
6. Advanced generics và type erasure
7. Functional error modeling
8. Concurrency architecture
9. Locks, atomics và thread safety
10. Flow architecture ở hệ thống lớn
11. Compose architecture ở scale lớn
12. Design system
13. Adaptive UI, window size và foldables
14. Accessibility và internationalization
15. Startup architecture
16. Baseline Profiles và Macrobenchmark
17. Observability
18. Resilience engineering
19. Large-scale modularization
20. Convention plugins và build-logic
21. API/module compatibility
22. Library publishing
23. Kotlin Multiplatform awareness
24. Native/JNI interoperability awareness
25. Android platform boundaries
26. Privacy, security, compliance
27. Release engineering
28. Testing architecture cấp tổ chức
29. Technical debt và migration strategy
30. Master-level architectural heuristics
31. Kotlin/Android keyword & API index

---

# 1. Version model: Kotlin 1.x → Kotlin 2.x và Android toolchain

Kotlin 1.x là dòng lịch sử rất dài mà phần lớn syntax cốt lõi hiện nay vẫn tương thích. Kotlin 2.0 đánh dấu K2 compiler trở thành compiler frontend chính. Tới baseline tài liệu này, Kotlin 2.4.20 là release mới của line 2.4. Khi đọc project cũ, điều cần quan tâm không chỉ `kotlinVersion` mà còn Android Gradle Plugin, Gradle, JDK, Compose Compiler/plugin model, KSP/KAPT version và compile/target SDK.

Kotlin source thường tương thích khá tốt, nhưng toolchain matrix mới là nơi migration hay vỡ. Một plugin compiler cũ có thể không tương thích Kotlin mới dù source code không đổi. Vì vậy upgrade nên theo release notes và compatibility matrix, không nâng ngẫu nhiên từng version.

Android Studio baseline hiện tại là Quail 4 / 2026.1.4 Patch 1 stable; bản patch này đi cùng Android Gradle Plugin 9.4.1. IDE version và AGP version liên quan nhưng không hoàn toàn đồng nhất; IDE có thể hỗ trợ một range AGP. Production team nên pin Gradle wrapper và dependency để build reproducible thay vì dựa vào môi trường IDE cá nhân.

# 2. K2 compiler và language evolution

K2 không phải ngôn ngữ mới; đây là compiler frontend mới với kiến trúc, performance và analysis tốt hơn. Tuy nhiên compiler plugin, IDE analysis và edge-case inference có thể thay đổi. Khi migration Kotlin 1.x project lớn lên 2.x, cần chạy full test, lint, static analysis và kiểm tra plugin ecosystem.

Senior/master developer nên đọc changelog theo release line vì feature có thể đi qua trạng thái experimental -> beta -> stable, và behavior có thể bị gate bởi language/api version.

# 3. Kotlin/JVM bytecode awareness

Kotlin source tiện lợi có thể generate bytecode đáng kể: default arguments tạo synthetic methods/bitmask; lambdas có thể dùng invokedynamic hoặc generated class tùy target/toolchain; companion/object có runtime representation; delegated property có helper metadata; suspend function biến thành continuation state machine.

Không cần tối ưu bytecode bằng trực giác. Chỉ inspect bytecode khi profiler/build size/hot path cho thấy vấn đề. Android Studio có decompile bytecode/tools hỗ trợ xem Java equivalent ở mức nhất định.

# 4. Value classes

Value class (`@JvmInline value class`) cho phép type wrapper có thể tránh allocation trong nhiều trường hợp.

```kotlin
@JvmInline
value class UserId(val value: Long)
```

Nó tăng type safety so với dùng raw `Long` cho mọi identifier. Tuy nhiên boxing có thể xảy ra khi dùng generic, nullable, interface hoặc boundary JVM. Không giả định “zero allocation” trong mọi context.

# 5. Context parameters và language evolution awareness

Kotlin tiếp tục tiến hóa với các tính năng context-oriented và compiler capability mới. Master-level note quan trọng không phải thuộc mọi experimental keyword mà là quản lý risk: không đưa experimental feature vào public API/library ổn định nếu migration cost chưa rõ; isolate experimental code; pin language version; bật opt-in có chủ đích.

# 6. Advanced generics và type erasure

JVM generic chủ yếu bị type erasure. `List<String>` và `List<Int>` không giữ đầy đủ generic type info runtime theo cách source thể hiện. `reified` giúp ở inline call site nhưng không xóa mọi giới hạn erasure.

Serialization framework cần type token/schema/code generation để giữ type information cần thiết. Reflection generic type có thể phức tạp khi nested parameterized type.

# 7. Functional error modeling

Exception tốt cho exceptional control flow và integration với Java/framework. Domain error đôi khi rõ hơn bằng sealed type:

```kotlin
sealed interface LoginError {
    data object InvalidCredential : LoginError
    data object NetworkUnavailable : LoginError
    data class Unknown(val cause: Throwable) : LoginError
}
```

Có thể model `Either`-like result, nhưng đừng biến mọi function thành monadic ceremony. Boundary cần nhất quán: đâu throw, đâu return result, đâu expose error state. Mixed semantics tùy hứng gây khó maintain hơn bản thân lựa chọn nào.

# 8. Concurrency architecture

Ở hệ thống lớn, không chỉ chọn `Dispatchers.IO`. Cần xác định concurrency ownership, parallelism budget, queue/backpressure, cancellation boundary và long-lived scope.

Một repository có external scope phải có owner application-level và lifecycle được quản lý. Không tạo ad-hoc `CoroutineScope(SupervisorJob() + Dispatchers.IO)` ở nhiều class mà không có shutdown/test strategy.

# 9. Locks, atomics và thread safety

Coroutine không làm shared mutable state tự động an toàn. Nếu nhiều coroutine/thread truy cập state, có thể cần confinement, `Mutex`, atomic hoặc actor-like model.

```kotlin
private val mutex = Mutex()

suspend fun update() = mutex.withLock {
    // critical section
}
```

`Mutex` suspend thay vì block thread, nhưng vẫn phải tránh critical section dài hoặc gọi external slow API trong lock nếu không cần.

# 10. Flow architecture ở hệ thống lớn

Flow graph lớn có thể gây duplicate upstream subscription, excessive combine, accidental replay và memory retention. Cần biết điểm nào nên `shareIn/stateIn`, scope nào giữ stream, và subscription policy nào đúng.

Avoid “Flow everywhere”. One-shot command vẫn nên là suspend function. Flow phù hợp value thay đổi theo thời gian. Nếu API trả Flow chỉ để emit một value rồi complete, hãy xem có thực sự cần stream abstraction không.

# 11. Compose architecture ở scale lớn

Ở app lớn, composable nên chia theo stateful route/screen và stateless content. Route nối ViewModel/navigation/lifecycle; content nhận state + callback để preview/test dễ.

```kotlin
@Composable
fun HomeRoute(viewModel: HomeViewModel = hiltViewModel()) {
    val state by viewModel.uiState.collectAsStateWithLifecycle()
    HomeScreen(
        state = state,
        onAction = viewModel::onAction
    )
}
```

`HomeScreen` không nên biết repository/DI graph. Preview có thể truyền fake state.

# 12. Design system

Design system production gồm token màu, typography, spacing, shape, icon, component, interaction state, accessibility và theming policy. Không chỉ là file `Color.kt`.

Component API nên semantic hơn là expose mọi Modifier/flag vô hạn. Ví dụ `AppPrimaryButton(text, enabled, loading, onClick)` có thể enforce accessibility/loading behavior thống nhất.

# 13. Adaptive UI

Android chạy trên phone, tablet, foldable, desktop-like window và multi-window. Không hardcode logic theo orientation. Dùng window size class/adaptive layout APIs phù hợp để quyết định navigation rail, list-detail, pane layout.

# 14. Accessibility và internationalization

Accessibility không phải việc “thêm contentDescription sau cùng”. UI semantics, touch target, focus order, dynamic font scale, contrast và screen reader behavior phải được design từ đầu.

Internationalization cần tránh nối string thủ công theo ngữ pháp tiếng Anh. Dùng plural resources, placeholder resource và locale-aware formatting cho ngày/số/tiền.

# 15. Startup architecture

Cold start chịu ảnh hưởng Application initialization, ContentProvider auto-init, DI graph, class loading, disk I/O và first frame work. Không initialize mọi SDK trong `Application.onCreate` nếu chưa cần.

App Startup library có thể quản lý initializer dependency nhưng vẫn cần đo. Lazy init giúp giảm cold start nhưng có thể dời jank sang màn hình đầu tiên nếu không quản lý.

# 16. Baseline Profiles và Macrobenchmark

Baseline Profile cung cấp profile-guided compilation information để cải thiện startup và interaction performance trên thiết bị hỗ trợ. Macrobenchmark đo behavior ở mức app/package thực tế hơn microbenchmark.

Performance optimization phải dựa trên measurement, percentile và representative device; không dựa trên “cảm giác emulator”.

# 17. Observability

Production app cần crash reporting, structured logging, performance trace và domain telemetry có privacy guard. Event naming/schema cần versioning và governance nếu analytics quan trọng.

Không log PII/token. Correlation ID giúp trace request qua client/server. Error log cần context đủ để debug nhưng không leak dữ liệu.

# 18. Resilience engineering

Mobile network không ổn định. Thiết kế cần timeout, retry with backoff, idempotency, offline queue khi phù hợp, circuit-breaking/throttling ở một số hệ thống, token refresh single-flight và graceful degradation.

Retry không phải mặc định. POST tạo giao dịch tài chính không thể retry mù nếu server không có idempotency contract.

# 19. Large-scale modularization

Module boundary tốt phản ánh ownership và dependency direction. Feature module có thể expose contract module nhỏ nếu nhiều feature cần giao tiếp mà không phụ thuộc implementation.

Tránh `core:common` chứa mọi thứ; nó trở thành dependency god-module. Tách theo capability ổn định như `core:model`, `core:network`, `core:database`, `core:designsystem`, `core:testing` nếu thực sự cần.

# 20. Convention plugins và build-logic

Project nhiều module nên tránh copy-paste Gradle config. Convention plugin trong `build-logic` có thể gom cấu hình Android library, Compose, test, lint.

Mục tiêu là type-safe, versioned internal build API và giảm drift. Nhưng convention plugin cũng là code cần test/maintain; đừng abstraction quá sớm cho project 2 module.

# 21. API/module compatibility

Internal module API thay đổi có thể trigger recompilation lớn. Public library cần semantic versioning và binary compatibility awareness. Kotlin metadata, JVM signature và default args có ảnh hưởng compatibility.

Nếu publish library, cân nhắc binary compatibility validator/API dump tooling để review API change.

# 22. Library publishing

Android/Kotlin library cần publication metadata, source/javadoc artifact nếu cần, consumer ProGuard/R8 rules, minimum SDK, transitive dependency strategy và API documentation. Không expose implementation dependency nếu caller không cần.

Gradle `api` vs `implementation` ảnh hưởng dependency exposure và compile classpath. `implementation` thường giảm coupling/recompilation.

# 23. Kotlin Multiplatform awareness

Kotlin Multiplatform cho phép share code giữa Android/iOS/desktop/server tùy target. KMP không đồng nghĩa “viết UI một lần” trừ khi dùng Compose Multiplatform hoặc stack khác. Shared domain/data code vẫn phải xử lý platform-specific API qua `expect/actual`, interface hoặc dependency injection.

Không đưa KMP vào chỉ vì trend. Nó có lợi khi shared logic đủ lớn và team sẵn sàng quản lý tooling/platform boundary.

# 24. JNI / native interoperability awareness

Android có thể gọi C/C++ qua JNI/NDK. Đây là boundary phức tạp về memory, thread, ABI và crash diagnostics. Chỉ dùng khi có native dependency, performance need đã đo hoặc platform requirement cụ thể.

# 25. Android platform boundaries

Binder IPC có transaction limit và serialization overhead. Parcelable/Bundle không phải channel để đẩy object graph lớn. Process/component boundary cần DTO nhỏ và stable identifier.

Exported Activity/Service/Receiver/Provider là security boundary. Intent extras từ external source phải được validate như untrusted input.

# 26. Privacy, security, compliance

Permission phải theo least privilege. Data collection cần minh bạch và phù hợp policy/store requirement. Sensitive local data cần encryption strategy phù hợp và key management bằng Keystore khi cần.

Screenshot blocking, clipboard handling, notification content, backup rules, WebView cache và log đều có thể là data-leak surface tùy domain.

# 27. Release engineering

Một pipeline production thường có formatting/static analysis, unit test, lint, build, instrumentation/smoke test theo mức, artifact signing, R8/proguard, mapping upload, staged rollout và rollback/feature flag strategy.

Signing key là tài sản critical. Không commit keystore/password. Play App Signing giảm một số rủi ro operational nhưng upload key vẫn phải quản lý.

Versioning Android dùng `versionCode` tăng đơn điệu cho distribution và `versionName` hiển thị cho người dùng. CI nên tạo version reproducible theo release process.

# 28. Testing architecture cấp tổ chức

Test fixture/fake/shared test module cần API rõ. Test không ổn định (flaky) phải được coi là defect engineering, không phải “chạy lại là được”. UI tests cần deterministic seed, network stub/fake backend hoặc environment kiểm soát.

Contract tests giữa mobile/backend có giá trị với API phức tạp, đặc biệt khi schema evolve độc lập.

# 29. Technical debt và migration strategy

Migration lớn nên có strangler pattern: tạo đường mới cạnh đường cũ, chuyển dần traffic/screen/module, đo regression, sau đó xóa legacy. Rewrite toàn bộ thường thất bại vì behavior ẩn trong code cũ không được document.

Mỗi migration cần exit criteria: bao giờ xóa API cũ, telemetry nào chứng minh ổn, fallback ra sao, owner là ai.

# 30. Master-level architectural heuristics

Một hệ thống tốt thường có các đặc tính: dependency đi một chiều; side effect nằm ở boundary có owner; state có source of truth; public API nhỏ; error semantics nhất quán; concurrency structured; persistence phù hợp process lifetime; build reproducible; security boundary rõ; performance được đo; migration có strategy; test tập trung vào behavior quan trọng.

Không có Clean Architecture/MVI/MVVM nào tự động tạo những đặc tính này. Pattern chỉ là công cụ để đạt chúng.

# 31. Kotlin/Android keyword & API index

## Kotlin keywords cần nhận diện

Các keyword cốt lõi cần biết gồm: `package`, `import`, `class`, `interface`, `fun`, `object`, `val`, `var`, `typealias`, `this`, `super`, `typeof`/type-related evolving syntax theo version, `as`, `is`, `in`, `when`, `if`, `else`, `for`, `while`, `do`, `try`, `catch`, `finally`, `throw`, `return`, `break`, `continue`, `sealed`, `data`, `enum`, `annotation`, `companion`, `inner`, `open`, `final`, `abstract`, `override`, `private`, `protected`, `internal`, `public`, `lateinit`, `const`, `tailrec`, `operator`, `infix`, `inline`, `noinline`, `crossinline`, `reified`, `suspend`, `external`, `expect`, `actual`, `out`, `vararg`, `where`, `by`, `field`, `property`, `receiver`, `setparam`, `delegate`, `file`, `get`, `set` và các soft/contextual keywords theo language version.

Không cần học thuộc danh sách trước khi code. Mục tiêu của index là để khi đọc code lạ, bạn biết từ nào thuộc language semantics và từ nào chỉ là API/library identifier.

## Kotlin standard library/API families cần nắm

String: `substring`, `split`, `trim`, `replace`, `contains`, `startsWith`, `endsWith`, `lowercase`, `uppercase`, `toIntOrNull`.

Collections: `map`, `mapNotNull`, `flatMap`, `filter`, `filterNotNull`, `associate`, `associateBy`, `groupBy`, `groupingBy`, `fold`, `reduce`, `sumOf`, `sortedBy`, `distinctBy`, `chunked`, `windowed`, `zip`, `partition`, `firstOrNull`, `singleOrNull`, `any`, `all`, `none`.

Null/error helpers: `let`, `takeIf`, `takeUnless`, `require`, `requireNotNull`, `check`, `checkNotNull`, `error`, `runCatching`, `getOrElse`, `getOrNull`.

Coroutine: `launch`, `async`, `await`, `coroutineScope`, `supervisorScope`, `withContext`, `delay`, `yield`, `ensureActive`, `withTimeout`, `withTimeoutOrNull`, `Mutex`, `Channel`, `Flow`, `StateFlow`, `SharedFlow`.

## Android APIs/families cần nhận diện

Core component: `Application`, `Activity`, `ComponentActivity`, `Fragment`, `Service`, `BroadcastReceiver`, `ContentProvider`, `Context`, `Intent`, `Bundle`, `Uri`.

Lifecycle/state: `Lifecycle`, `ViewModel`, `SavedStateHandle`, `viewModelScope`, `lifecycleScope`, `repeatOnLifecycle`.

Compose: `@Composable`, `remember`, `rememberSaveable`, `mutableStateOf`, `derivedStateOf`, `LaunchedEffect`, `DisposableEffect`, `SideEffect`, `snapshotFlow`, `Modifier`, `LazyColumn`, `Scaffold`, `MaterialTheme`.

Persistence/background: Room (`@Entity`, `@Dao`, `@Query`, `@Transaction`, `RoomDatabase`), DataStore, WorkManager (`Worker`, `CoroutineWorker`, `WorkRequest`, constraints).

Navigation: `NavController`, `NavHost`, destinations, deep links, back stack.

Testing/performance: JUnit, coroutine test, Compose test, Espresso/UI Automator theo stack, Macrobenchmark, Baseline Profile, profiler/Perfetto.

---

## Final Master Note

Để “master Kotlin Android”, không đủ học hết keyword hay API. Bạn cần hiểu bốn lớp cùng lúc: semantics của Kotlin; lifecycle/concurrency của Android; state/recomposition của Compose; và engineering constraints của production như build, test, observability, performance, security, migration. Khi bốn lớp này kết nối được trong đầu, bạn có thể đọc cả code mới lẫn legacy, chọn abstraction phù hợp thay vì chạy theo trend, và thiết kế hệ thống có thể sống qua nhiều năm nâng version.

---

# 32. Version matrix và cách đọc một project Android năm 2026

Tại thời điểm cập nhật 2026-09-20, Kotlin stable baseline của bộ note là **2.4.20**. Android Studio stable là **Quail 4 / 2026.1.4 Patch 1**; patch này được phát hành cùng **Android Gradle Plugin 9.4.1**. Android 17 mang API level 37. Trong khi đó, policy Google Play từ 2026-08-31 yêu cầu app mới và update Android thông thường target Android 16 / API 36 trở lên. Vì vậy khi đọc một project, tuyệt đối không nhìn một version đơn lẻ rồi kết luận “cũ” hay “mới”.

Một Android build thực tế có ít nhất các version tương tác: JDK, Gradle Wrapper, AGP, Kotlin Gradle Plugin, Kotlin language/API version, KSP hoặc KAPT, Compose compiler/plugin model, compileSdk, targetSdk, minSdk và từng Jetpack library. Một dependency mới có thể yêu cầu compileSdk mới hơn; AGP có thể yêu cầu Gradle/JDK cụ thể; compiler plugin phải tương thích Kotlin version. Do đó nâng version là bài toán compatibility graph, không phải sửa một con số.

Senior workflow khi upgrade là thay đổi từng lớp có kiểm soát, đọc migration notes, chạy build/test/lint/benchmark và tách lỗi toolchain khỏi regression product. Không nên upgrade IDE, AGP, Gradle, Kotlin, Compose và targetSdk trong một commit khổng lồ nếu project lớn vì khi lỗi xuất hiện sẽ khó biết nguyên nhân.

# 33. K2, compiler plugin và generated code như một phần của kiến trúc

Kotlin 2.x dùng K2 frontend làm nền tảng compiler hiện đại. Trên Android, compiler không chỉ compile source Kotlin thuần. Compose compiler plugin transform composable function; serialization plugin generate serializer; Parcelize generate Parcelable implementation; KSP processor có thể generate DI/database/adapter code. Điều này nghĩa build architecture có generated source và compiler phases thực sự ảnh hưởng API, build time và debugging.

Khi lỗi chỉ xuất hiện sau nâng Kotlin, hãy kiểm tra compiler plugin/processor compatibility trước khi nghi business code. Generated code nên được coi là implementation detail có thể inspect khi debug. Hiểu code generator tạo gì giúp phân biệt “magic” khỏi dependency graph thật.

KAPT dựa trên Java annotation processing và thường cần stub/interoperability layer; KSP hiểu Kotlin symbol trực tiếp hơn và thường hiệu quả hơn khi ecosystem hỗ trợ. Tuy vậy “KSP luôn tốt hơn” không phải quy luật tuyệt đối: migration còn phụ thuộc processor maturity, generated API và build behavior.

# 34. Source compatibility, binary compatibility và behavioral compatibility

Một thay đổi có thể source-compatible nhưng binary-incompatible, hoặc compile được nhưng behavior thay đổi. Public library phải phân biệt ba lớp này. Đổi default parameter, inline public function, JVM name, generic signature, visibility hoặc class hierarchy có thể ảnh hưởng caller theo cách khác nhau.

Kotlin `internal` không phải security boundary; trên JVM nó vẫn có representation bytecode và name mangling. `inline` public function còn đặc biệt vì implementation có thể được copy vào bytecode caller, nên thay body có implications khác method call bình thường. Nếu publish library, API dump/binary compatibility tooling giúp review accidental public API growth.

Behavioral compatibility quan trọng nhất với app product. Một repository method giữ nguyên signature nhưng đổi caching semantics có thể phá UI. Vì vậy API review cần document cả contract về threading, cancellation, error, ordering, nullability và idempotency, không chỉ type signature.

# 35. Architecture ở codebase lớn: dependency graph quan trọng hơn tên pattern

Ở quy mô lớn, kiến trúc nên làm ba việc: giới hạn vùng ảnh hưởng của thay đổi, làm dependency direction rõ, và cho phép team build/test/release với mức độc lập hợp lý. “Clean Architecture” có ích khi boundary phản ánh domain thật, nhưng nếu mỗi use case chỉ forward một dòng sang repository thì abstraction đó có thể chỉ tăng navigation cost.

Feature module nên có public contract nhỏ. Core module chỉ nên chứa capability có tính dùng chung và ổn định; `core:common` chứa utility, model, networking, analytics, navigation và business rule của mọi feature sẽ trở thành god-module khiến incremental build và ownership xấu đi.

Dependency inversion có giá trị khi nó phá coupling vào volatile detail hoặc tạo test seam cần thiết. Không phải mọi class đều cần interface. Interface một implementation chỉ để “đúng pattern” thường làm code khó đọc hơn mà không tăng khả năng thay đổi thực tế.

# 36. Performance engineering: hypothesis → measurement → change → verification

Performance work không bắt đầu bằng “dùng Sequence”, “thêm remember” hay “đổi collection”. Bắt đầu bằng metric người dùng cảm nhận: cold/warm startup, frame time, time-to-content, memory peak, network latency, battery hoặc APK size. Sau đó thu trace/profile trên thiết bị đại diện, tạo hypothesis dựa trên evidence, thay đổi một yếu tố và đo lại.

Microbenchmark phù hợp primitive nhỏ; Macrobenchmark phù hợp startup/scroll/interaction ở app level; Perfetto cho timeline hệ thống/thread; Android Studio profiler hỗ trợ CPU/memory/network; Compose tooling giúp xem recomposition/layout. Baseline Profiles cải thiện compilation/runtime path phổ biến nhưng không sửa algorithm chậm hoặc I/O trên main thread.

Phải phân biệt average với tail latency. UI có thể “trung bình 10 ms” nhưng thỉnh thoảng frame 100 ms vẫn cho cảm giác giật. Production telemetry nên nhìn percentile thích hợp và device class thay vì một con số từ emulator mạnh.

# 37. Reliability engineering trên mobile

Mobile app hoạt động trong môi trường không ổn định: process có thể bị kill, mạng đổi Wi‑Fi/LTE, request timeout, app đi background, token hết hạn, clock lệch, user tap lặp, backend deploy version mới. Code chỉ hoạt động trên happy path chưa phải production-ready.

Operation tạo side effect server cần idempotency contract nếu có retry. Sync engine cần model local pending operation, remote truth và conflict resolution. Token refresh nên single-flight để hàng chục request 401 không đồng loạt refresh. Retry phải có giới hạn và backoff; lỗi 4xx nghiệp vụ thường không nên retry như network timeout.

Offline-first không có nghĩa mọi app phải sync phức tạp. Nó nghĩa UX/data model xác định rõ behavior khi offline: đọc cache nào, thao tác nào được queue, trạng thái “pending” hiển thị ra sao, khi reconnect giải quyết conflict thế nào. Nếu product không cần offline mutation, cache read-only đơn giản có thể đúng hơn.

# 38. Security engineering: xem APK là môi trường không đáng tin

Client mobile nằm trên thiết bị người dùng, nên attacker có thể decompile APK, hook method, inspect memory hoặc chạy trên rooted/emulated environment. Vì vậy app không thể giữ một server secret dài hạn theo nghĩa cryptographic chỉ bằng obfuscation. R8 làm reverse engineering khó hơn đôi chút nhưng không biến client thành trusted server.

Authorization phải thực thi phía backend. Client-side role check chỉ là UX. Token cần lifetime, refresh/revocation strategy và secure storage phù hợp. Android Keystore giúp bảo vệ key material tốt hơn file plaintext nhưng không loại bỏ mọi threat trên compromised device.

Component exported, deep link, WebView, PendingIntent, notification intent, file provider và IPC đều là input boundary. Nguyên tắc chung là validate input, least privilege, explicit intent khi phù hợp, không log credential/PII và giữ dependency/security patch process hoạt động.

# 39. Release, rollout và rollback như một phần của thiết kế feature

Feature production không kết thúc khi merge vào `main`. Release pipeline phải biết artifact nào được build từ commit nào, test nào đã chạy, mapping file nào tương ứng, config/feature flag nào bật và rollout đang ở phần trăm nào. Staged rollout giảm blast radius nhưng chỉ hữu ích khi telemetry có thể phát hiện regression.

Feature flag có thể tắt behavior mà không cần phát hành APK mới, nhưng flag cũng tạo state space: code path cũ/mới cùng tồn tại, config có thể stale và cleanup bị quên. Mỗi flag nên có owner và ngày xóa dự kiến. Database/schema migration phải tương thích với rollback; nếu server hoặc local schema thay đổi irreversible, “rollback app binary” có thể không đủ.

# 40. Đọc legacy Android mà không áp framework hiện đại một cách máy móc

Một codebase cũ có thể dùng Java, XML, Fragment, LiveData, RxJava, Dagger 2, custom Service và callback. Nhiệm vụ đầu tiên không phải rewrite sang Compose/Flow/Hilt mà là hiểu lifecycle, dependency và behavior hiện có. Những abstraction cũ không tự động sai; rủi ro nằm ở API deprecated không còn an toàn, behavior platform thay đổi, test coverage yếu hoặc maintenance cost quá cao.

Migration tốt thường tạo seam: ví dụ repository cũ expose RxJava có thể được adapter sang Flow tại boundary; màn hình mới dùng Compose nhưng host trong Fragment cũ; ViewModel mới dùng StateFlow trong khi phần legacy vẫn LiveData. Khi telemetry/test chứng minh path mới ổn, mới xóa path cũ. Strangler migration kiểm soát risk tốt hơn big-bang rewrite.

# 41. Master checklist trước khi gọi một hệ thống là production-ready

Một hệ thống Kotlin/Android mature phải giải thích được: source of truth của từng loại dữ liệu; ownership của coroutine và state; behavior khi configuration change/process death; API/version compatibility; network timeout/retry/idempotency; database migration; security boundary; observability; test strategy; performance budget; build reproducibility; signing/release; rollout/rollback và legacy migration. Nếu câu trả lời chỉ là tên framework, kiến trúc vẫn chưa đủ sâu.

Mastery không phải nhớ toàn bộ Android SDK. Nó là khả năng xác định đúng abstraction level, đọc contract/version, lần theo runtime/build behavior, đo thay vì đoán, và thiết kế sao cho hệ thống vẫn hiểu được khi team, backend và platform cùng thay đổi.
