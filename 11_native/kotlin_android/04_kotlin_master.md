# Kotlin + Android Master Note — Master / Production Engineering Supplement

> Mục tiêu: đưa người học từ mức Senior lên mức có thể reasoning về compiler, runtime, lifecycle, concurrency, API compatibility, production architecture, build/release và migration qua nhiều thế hệ Kotlin/Android. File này là canonical Master note; các `deep_dive/`, `production_casebook/` và `depth_labs/` chỉ mở rộng những boundary khó, không thay thế learning flow của file này.

## Mục lục

1. Version model: Kotlin 1.x → 2.x và Android toolchain
2. K2 compiler và language evolution
3. Kotlin/JVM bytecode awareness
4. Value classes và allocation model
5. Context parameters và feature maturity
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
32. Version matrix và cách đọc project Android hiện đại
33. Compiler plugin và generated code
34. Source/binary/behavioral compatibility
35. Architecture ở codebase lớn
36. Performance engineering
37. Reliability engineering
38. Security engineering
39. Release, rollout và rollback
40. Modern vs legacy Android
41. Production-ready checklist

---

# 1. Version model: Kotlin 1.x → Kotlin 2.x và Android toolchain

Kotlin/Android không có một “version của project”. Một project production là giao điểm của nhiều version axis. Nếu chỉ nhìn `kotlin = "2.4.20"` rồi kết luận project mới hay cũ, ta bỏ qua phần lớn compatibility contract thực tế.

Bốn tầng version cần tách riêng trong đầu:

```text
Tầng 1 — Language/compiler
Kotlin release
languageVersion
apiVersion
K1/K2 compiler
compiler plugins

Tầng 2 — JVM/toolchain
JDK chạy Gradle
Java source/target compatibility
Kotlin jvmTarget
bytecode level

Tầng 3 — Android build/platform
Gradle
Android Gradle Plugin (AGP)
compileSdk
minSdk
targetSdk
D8/R8
APK/AAB packaging

Tầng 4 — Ecosystem
Compose compiler plugin
Compose BOM / Jetpack libraries
KSP/kapt processors
Room/Hilt/serialization/plugin versions
NDK/native dependencies
Google Play policy
```

Các tầng này liên quan nhưng không đồng nhất. `Kotlin 2.4.20`, `AGP 9.4.1`, `compileSdk 37`, `targetSdk 36` và `Compose BOM 2026.09.00` hoàn toàn có thể cùng tồn tại vì chúng mô tả các contract khác nhau.

## 1.1 Kotlin version không đồng nghĩa language version

Compiler mới có thể hỗ trợ source language level cũ trong một khoảng thời gian. Vì vậy cần phân biệt:

```text
Kotlin compiler version
= compiler/toolchain đang chạy

languageVersion
= syntax + language semantics source được phép dùng

apiVersion
= mức Kotlin standard-library API source được phép gọi
```

Đối với application, thường ba mức này đi khá gần nhau. Đối với library, chúng có thể được pin bảo thủ hơn để không vô tình nâng minimum consumer requirement.

Ví dụ mental model:

```kotlin
kotlin {
    compilerOptions {
        languageVersion.set(KotlinVersion.KOTLIN_2_4)
        apiVersion.set(KotlinVersion.KOTLIN_2_4)
        jvmTarget.set(JvmTarget.JVM_17)
    }
}
```

`jvmTarget` lại là contract khác: nó mô tả bytecode JVM output, không phải Kotlin language feature set.

## 1.2 Kotlin 1.x → 2.x: thay đổi lớn nhất nằm ở compiler generation

Phần lớn syntax Kotlin nền tảng từ 1.x vẫn quen thuộc ở 2.x. Mốc lớn là Kotlin 2.0 khi K2 trở thành compiler frontend production mặc định. Do đó migration 1.x → 2.x thường không phải “rewrite Kotlin”, mà là kiểm tra những boundary phụ thuộc compiler:

```text
Kotlin source
→ type inference / diagnostics
→ compiler plugins
→ KSP/kapt processors
→ generated code
→ Kotlin metadata
→ JVM bytecode
→ D8/R8
→ APK/AAB
```

Source có thể không đổi nhưng build vẫn vỡ vì processor hoặc plugin chưa tương thích.

## 1.3 Compose compiler: dấu mốc trước và sau Kotlin 2.0

Project Compose cũ thường có Compose compiler version mapping riêng với Kotlin. Từ Kotlin 2.0+, Compose compiler được tích hợp vào Kotlin repository và modern setup dùng plugin `org.jetbrains.kotlin.plugin.compose` cùng version Kotlin.

Điều này không có nghĩa Compose UI libraries dùng cùng version Kotlin. Phải tách:

```text
Kotlin / Compose compiler plugin
!=
Compose UI runtime/foundation/material versions
```

Compose BOM alignment chỉ quản lý nhóm Compose libraries; BOM không thay thế compatibility của Kotlin, AGP, JDK hay compileSdk.

## 1.4 Android version có bốn câu hỏi khác nhau

```text
minSdk
= Android thấp nhất app hỗ trợ runtime

compileSdk
= Android API surface dùng để compile

targetSdk
= behavior contract mới mà app tuyên bố đã thích nghi

Device OS
= platform thật đang chạy app
```

Một app có thể compile với API 37, target 36 và vẫn chạy trên API 26 nếu dependencies và code path cho phép. `targetSdk` mới đặc biệt nguy hiểm nếu bị xem như “chỉ đổi một số”: nó có thể bật behavior change về permission, background execution, foreground service, storage, window/edge-to-edge, notification hoặc networking.

## 1.5 Upgrade là dependency graph, không phải sửa version string

Một chuỗi upgrade có thể là:

```text
Compose/Jetpack mới
→ cần compileSdk mới
→ cần AGP mới
→ AGP cần Gradle/JDK mới
→ Kotlin plugin/processor cần version tương thích
→ release variant cần R8 rules mới
```

Vì vậy production upgrade nên theo thứ tự có kiểm soát:

```text
1. chụp baseline version fingerprint
2. đọc release notes + compatibility guide
3. đổi một axis hoặc một nhóm tightly-coupled axis
4. clean build tất cả variants
5. chạy unit/integration/instrumented tests
6. build release + minified artifact
7. benchmark nếu compiler/runtime path đổi đáng kể
8. rollout có telemetry và rollback plan
```

Không nên cùng một PR nâng Kotlin, AGP, targetSdk, Compose, đổi architecture và migrate database nếu không có lý do bắt buộc.

## 1.6 Cách đọc project theo generation

Một project có Kotlin 2.x nhưng vẫn XML/Fragment/RxJava có thể là codebase modern toolchain nhưng legacy UI/reactive stack. Một project Kotlin 1.9 có architecture sạch và test tốt vẫn có thể production-quality. Version chỉ giúp xác định **migration context**, không tự động đánh giá chất lượng kiến trúc.

Khi mở project lạ, hãy fingerprint:

```text
Gradle wrapper
AGP
Kotlin/KGP
JDK
languageVersion/apiVersion/jvmTarget
KSP hay kapt
Compose compiler setup
minSdk/compileSdk/targetSdk
UI stack: XML/View hay Compose
state stack: LiveData/RxJava hay Flow/StateFlow
background work: Service/Alarm/WorkManager
storage: SharedPreferences/DataStore/Room
```

Sau đó mới quyết định phần nào thật sự cần migrate.

# 2. K2 compiler và language evolution

K2 không phải “Kotlin 2 syntax”. Đây là compiler frontend thế hệ mới dựa trên FIR (Front-end Intermediate Representation), được thiết kế để unify analysis, cải thiện compiler/IDE architecture và làm language evolution bền vững hơn.

Một migration sang K2 cần quan tâm ba lớp:

```text
Source semantics
Compiler diagnostics/inference
Plugin/generated-code ecosystem
```

Một số source từng compile nhờ corner-case inference ở K1 có thể bị diagnostics khác ở K2. Đây không nhất thiết là regression; đôi khi compiler mới siết behavior vốn ambiguous. Vì vậy khi migration cần phân biệt:

```text
source bug bị compiler mới phát hiện
vs
compiler/plugin incompatibility
vs
behavioral regression của application
```

## 2.1 Feature maturity quan trọng hơn “feature xuất hiện ở version nào”

Language feature thường đi qua:

```text
Experimental / Preview
→ Beta
→ Stable
→ Deprecated
→ Error/Removal
```

Không nên thấy feature trong release blog rồi đưa ngay vào public API. Với library/public SDK, maturity level là compatibility contract. Experimental feature có thể đổi syntax, metadata hoặc generated representation ở release sau.

## 2.2 Context parameters và explicit backing fields

Ở line 2.4, context parameters và explicit backing fields đã tiến tới Stable. Điều này làm source expressiveness mạnh hơn nhưng không tạo nghĩa vụ migrate toàn bộ code cũ.

Ví dụ context parameter:

```kotlin
context(logger: Logger)
fun save(user: User) {
    logger.info("save ${user.id}")
}
```

Đây không tự động thay constructor injection/Hilt. Android dependency thường mang lifecycle, scope và disposal semantics; lexical context không giải quyết ownership đó.

Explicit backing field có thể giảm boilerplate của mutable-inside/read-only-outside, nhưng `_state` + public `StateFlow` vẫn dễ hiểu và tương thích rộng. Chọn syntax mới khi nó cải thiện API/readability thật, không phải vì version mới tồn tại.

## 2.3 Compiler options là một phần của source contract

Modern Kotlin Gradle DSL ưu tiên `compilerOptions {}` thay `kotlinOptions {}` cũ. Compiler flags, progressive mode và opt-in API cần được xem như codebase policy. Một `-X...` flag experimental đặt ở root build có thể ảnh hưởng hàng chục module và làm migration khó hơn nhiều năm sau.

Nguyên tắc Master-level:

```text
stable feature mặc định
experimental feature phải có owner + lý do + exit strategy
compiler flag phải được document
public API không nên vô tình phụ thuộc unstable behavior
```

# 3. Kotlin/JVM bytecode awareness

Kotlin source có thể generate JVM representation khác điều source “trông như”. Default arguments tạo synthetic bridge/bitmask; suspend function thành continuation state machine; lambdas có thể dùng `invokedynamic` hoặc generated class tùy target/toolchain; companion/object có runtime representation; delegation và annotations tạo metadata/bridge code.

Không tối ưu bytecode bằng trực giác. Chỉ inspect khi profiler, binary size, Java interop hoặc compatibility issue đưa ra bằng chứng. Senior/Master workflow là source → generated bytecode/metadata → D8/R8 → runtime behavior, không dừng ở decompiled pseudo-Java.

Public `inline`, default parameter, `const val`, value class và JVM name cần đặc biệt thận trọng ở library vì implementation/signature có thể leak sang consumer binary.

# 4. Value classes và allocation model

`@JvmInline value class` tạo type safety mà có thể tránh wrapper allocation trong nhiều call path:

```kotlin
@JvmInline
value class UserId(val value: Long)
```

Nhưng “value class = zero allocation” là mental model sai. Boxing có thể xảy ra khi nullable, generic, interface, reflection hoặc Java boundary tham gia. Đối với public SDK, thay underlying representation hoặc signature còn là compatibility decision.

Dùng value class khi domain semantics mạnh hơn raw primitive và profiling không cho thấy downside đáng kể; không dùng chỉ như micro-optimization.

# 5. Context parameters và feature maturity

Master-level learning không yêu cầu thuộc mọi feature mới. Điều quan trọng là biết feature maturity, compiler requirement, Java interop và public-API implication.

Trước khi dùng feature ngôn ngữ mới trong code production, hỏi:

```text
feature Stable chưa?
minimum Kotlin version nào?
consumer/library có bị nâng floor không?
Java caller nhìn API ra sao?
KSP/compiler plugin/tooling đã hiểu chưa?
team có đọc/debug được không?
```

# 6. Advanced generics và type erasure

JVM generic chủ yếu bị type erasure. `List<String>` và `List<Int>` không giữ đầy đủ type parameter runtime như source thể hiện. `reified` giúp inline call site truy cập type trong một số trường hợp nhưng không “xóa” type erasure khỏi JVM.

Serialization, DI và reflection thường cần generated schema, type token hoặc metadata bổ sung. Public generic API cần để ý wildcard/JVM interop, variance và binary signature.

# 7. Functional error modeling

Exception phù hợp exceptional failure và framework/Java integration. Domain error đôi khi rõ hơn bằng sealed type:

```kotlin
sealed interface LoginError {
    data object InvalidCredential : LoginError
    data object NetworkUnavailable : LoginError
    data class Unknown(val cause: Throwable) : LoginError
}
```

Không biến mọi function thành `Result`/Either theo nghi thức. Boundary cần contract rõ: method nào throw, method nào trả domain error, cancellation có được propagate không, retry decision nằm ở đâu.

# 8. Concurrency architecture

Concurrency production không phải chọn `Dispatchers.IO` rồi kết thúc. Cần xác định:

```text
owner của scope
lifetime của work
structured parent/child relation
parallelism budget
shared-state policy
cancellation semantics
ordering requirement
backpressure
retry/replay semantics
```

Một repository tự tạo `CoroutineScope(SupervisorJob() + Dispatchers.IO)` có nghĩa repository đang sở hữu lifetime độc lập; phải có lý do và shutdown/test strategy. Nếu work chỉ thuộc request/screen, structured scope của caller thường đúng hơn.

## 8.1 Race condition tồn tại dù chỉ dùng coroutine

Coroutine có thể interleave ở suspension point. Đoạn read-modify-write vẫn race nếu nhiều coroutine cùng chạy:

```kotlin
val old = state.value
val next = old.copy(count = old.count + 1)
state.value = next
```

Nếu invariant yêu cầu atomicity, dùng API atomic phù hợp, `Mutex`, actor/state owner single-threaded hoặc database transaction. Chọn primitive theo invariant, không theo thói quen.

## 8.2 Cancellation là control flow

`CancellationException` không phải business failure. Generic `catch (Throwable)` rồi convert thành `Error` có thể phá structured cancellation. Cleanup bắt buộc có thể dùng `finally`; `NonCancellable` chỉ nên bọc đoạn cleanup nhỏ thật sự cần hoàn tất, không biến toàn operation thành uncancellable.

# 9. Locks, atomics và thread safety

`Mutex` suspend thay vì block thread:

```kotlin
private val mutex = Mutex()

suspend fun update() = mutex.withLock {
    // critical section nhỏ, không chứa network call nếu không cần
}
```

Atomic phù hợp state nhỏ/operation lock-free đơn giản. Actor/single-owner phù hợp khi nhiều event cần ordering. Thread confinement phù hợp khi subsystem có execution context rõ. Không dùng lock lớn quanh I/O chậm vì dễ tạo convoy/starvation.

# 10. Flow architecture ở hệ thống lớn

Flow phù hợp dữ liệu thay đổi theo thời gian; one-shot command vẫn thường là `suspend fun`. Khi graph Flow lớn, cần kiểm soát cold/hot semantics, sharing scope, replay và backpressure.

`stateIn`/`shareIn` không chỉ là optimization. Chúng thay đổi lifetime của upstream. Nếu scope sống application-level, network/database subscription có thể sống lâu hơn UI tưởng. `SharingStarted.WhileSubscribed(...)` phải được chọn dựa trên reconnect cost và stale-state semantics.

Backpressure operator có nghĩa nghiệp vụ khác nhau:

```text
buffer
= cho producer chạy trước consumer trong giới hạn buffer

conflate
= bỏ intermediate state, giữ mới nhất

collectLatest
= cancel xử lý cũ khi value mới tới

flatMapLatest
= cancel sub-flow cũ khi key mới tới
```

`conflate` hợp progress/state mới nhất, nhưng có thể sai với payment/event/audit stream nơi mỗi item đều có ý nghĩa.

## 10.1 StateFlow không phải event bus

`StateFlow` có current value và replay state cho collector mới. One-off event như “show copied toast” có semantics khác durable state như “payment succeeded”. Đừng ép mọi thứ vào `SharedFlow`/Channel; trước hết quyết định event có được phép mất khi collector inactive hay phải reconstruct từ state.

# 11. Compose architecture ở scale lớn

Compose tốt không chỉ là `@Composable`. Cần hiểu ba tầng:

```text
State model
→ Composition / identity / effects
→ Layout / draw / input / semantics
```

Route-level composable có thể nối ViewModel/navigation/lifecycle; content composable nhận immutable state + callbacks:

```kotlin
@Composable
fun HomeRoute(viewModel: HomeViewModel = hiltViewModel()) {
    val state by viewModel.uiState.collectAsStateWithLifecycle()
    HomeScreen(state = state, onAction = viewModel::onAction)
}
```

`HomeScreen` không nên biết repository hoặc DI graph. Điều này làm preview, screenshot test và semantics test đơn giản hơn.

## 11.1 Recomposition không đồng nghĩa redraw toàn màn hình

Compose ghi nhận state reads và invalidates scope/phases liên quan. Performance issue cần xác định state nào thay đổi và state được đọc ở composition, layout hay draw phase. Không sửa bằng cách thêm `remember` bừa.

Stable identity rất quan trọng với lazy content:

```kotlin
LazyColumn {
    items(items, key = { it.id }) { item ->
        Row(item)
    }
}
```

Key không phải chỉ để performance; nó gắn logical identity với composition state. Key sai có thể khiến local remembered state “đi theo vị trí” thay vì entity.

## 11.2 Effect API phải khớp lifetime

`LaunchedEffect(key)` restart theo key; `DisposableEffect` dành cho register/unregister resource; `rememberUpdatedState` giữ callback/value mới mà không restart effect; `SideEffect` sync ra object bên ngoài sau successful composition.

Một effect cần sống sau khi screen biến mất không thuộc UI composition lifecycle và nên được đẩy về owner khác như ViewModel/repository/WorkManager tùy semantics.

# 12. Design system

Design system production gồm color/typography/spacing/shape tokens, semantic component, interaction state, accessibility, theming và migration policy. Component API nên semantic hơn là expose vô hạn flag kỹ thuật.

# 13. Adaptive UI

Android chạy trên phone, tablet, foldable, desktop-like window và multi-window. Không hardcode theo orientation. Layout nên dựa available window/capability và giữ navigation/state continuity khi window đổi.

# 14. Accessibility và internationalization

Accessibility là correctness: semantics, focus order, touch target, dynamic font scale, contrast và TalkBack behavior cần được thiết kế từ đầu. Internationalization cần resource/plural/locale-aware formatting thay vì nối string theo English grammar.

# 15. Startup architecture

Cold start chịu ảnh hưởng `Application`, ContentProvider auto-init, DI graph, class loading, disk I/O, DB open/migration và first-frame Compose work. Mỗi eager initializer là một phần critical path.

Lazy initialization chỉ tốt nếu không dời latency thành jank ở first interaction. Dùng Perfetto/Macrobenchmark để xác định critical path thực, không đo bằng log thủ công rồi kết luận.

# 16. Baseline Profiles và Macrobenchmark

Baseline Profile giúp ART precompile hot paths quan trọng. Macrobenchmark đo startup/scroll/interaction ở package-level; microbenchmark đo primitive nhỏ. Baseline Profile không sửa algorithm xấu, blocking I/O hoặc layout/recomposition sai.

# 17. Observability

Production app cần crash/ANR reporting, structured logging, performance metrics và domain telemetry có privacy guard. Log phải trả lời “failure xảy ra ở đâu và với version/artifact/config nào” mà không leak PII/token.

Telemetry schema cũng là API. Nếu rename event/field tùy tiện, dashboard và alert mất continuity. Release version, build fingerprint, experiment/feature flag và correlation ID nên đủ để khoanh vùng regression.

# 18. Resilience engineering

Mobile luôn có partial failure: timeout sau server commit, process death giữa write và UI update, token expire đồng thời ở nhiều request, retry sau reconnect, duplicate tap, stale cache và backend rollout không đồng bộ.

Retry phải dựa idempotency. Một request timeout không nói server chưa xử lý. Với mutation quan trọng, client/server cần operation ID hoặc idempotency key để replay an toàn.

Graceful degradation nghĩa định nghĩa trước feature nào vẫn hoạt động khi dependency fail, không phải catch mọi exception rồi hiện “Something went wrong”.

# 19. Large-scale modularization

Module boundary tốt giới hạn vùng ảnh hưởng của thay đổi, enforce dependency direction và phản ánh ownership. Tránh `core:common` thành god-module. Interface chỉ đáng tồn tại khi tạo contract/decoupling/test seam thật, không phải vì mỗi class “phải có interface”.

# 20. Convention plugins và build-logic

Convention plugin giúp gom cấu hình repeated ở multi-module project. Nhưng build-logic là production code: cần versioning, test, configuration-cache awareness và tránh hidden I/O trong configuration phase.

# 21. API/module compatibility

Public API phải nghĩ theo ba lớp:

```text
source compatibility
binary compatibility
behavioral compatibility
```

Giữ signature chưa chắc giữ behavior. Thay caching/threading/cancellation semantics có thể phá caller dù compile vẫn xanh. Kotlin metadata, default args, public inline, JVM name và generic signature có thể ảnh hưởng binary consumer.

# 22. Library publishing

Android/Kotlin library cần AAR/POM metadata, dependency exposure policy, consumer R8 rules, minSdk/JVM target, public API docs, sample consumer và compatibility matrix. `api` vs `implementation` là public classpath contract chứ không chỉ build optimization.

# 23. Kotlin Multiplatform awareness

KMP giúp share code giữa platform nhưng không tự động làm platform boundary biến mất. Share concern ổn định như domain/data khi hợp lý; giữ platform-specific lifecycle/UI/hardware ở platform layer. `expect/actual` là công cụ, không phải mục tiêu tăng “% shared code”.

# 24. JNI / native interoperability awareness

JNI/NDK tạo boundary về memory ownership, thread affinity, ABI, page size, symbolication và crash diagnostics. Dùng khi có native dependency hoặc performance/platform requirement đã chứng minh; đừng chuyển code sang C++ theo trực giác “native nhanh hơn”.

# 25. Android platform boundaries

Binder IPC có transaction/serialization cost. Bundle/Parcelable không nên chứa object graph lớn. Exported component, deep link, ContentProvider URI, PendingIntent và Binder input là untrusted boundary; validate như network input.

# 26. Privacy, security, compliance

Permission theo least privilege. Authorization nghiệp vụ nằm server-side; client chỉ là UX/risk signal. Keystore bảo vệ key material tốt hơn file plaintext nhưng không biến compromised device thành trusted environment.

Log, clipboard, screenshot, backup, WebView, notification và analytics đều có thể leak sensitive data. Security review phải cover data lifecycle, không chỉ crypto API.

# 27. Release engineering

Release pipeline production tối thiểu cần formatting/static analysis, unit/integration tests, lint, release/minified build, signing, mapping/symbol upload, artifact provenance, staged rollout và rollback/kill-switch strategy.

`versionCode` là monotonically increasing distribution identity; `versionName` là user-facing label. Nhưng để debug production cần thêm artifact identity: Git commit, build config, dependency lock, mapping file và server/feature-flag context.

Release-only failure thường tới từ R8, resource shrinking, different manifest/resource merge, signing, build config hoặc production backend—not từ source path debug. Vì vậy CI phải build/test artifact gần production nhất.

# 28. Testing architecture cấp tổ chức

Test strategy dựa risk, không dựa tỷ lệ unit/UI cố định. Pure logic test nhanh; database/network contract test kiểm tra boundary; instrumentation/Compose UI test kiểm tra platform semantics; Macrobenchmark kiểm tra performance contract. Flaky test là defect engineering vì nó phá tín hiệu CI.

# 29. Technical debt và migration strategy

Migration lớn nên dùng strangler/branch-by-abstraction: tạo path mới cạnh path cũ, chuyển dần traffic, đo regression, rồi xóa legacy. Mỗi migration cần exit criteria, telemetry, fallback, owner và deadline xóa compatibility layer.

# 30. Master-level architectural heuristics

Một hệ thống tốt thường có dependency một chiều, state owner rõ, source of truth rõ, side effect ở boundary có owner, concurrency structured, public API nhỏ, error semantics nhất quán, persistence phù hợp lifetime, build reproducible, security boundary rõ và migration có kế hoạch.

Pattern như MVVM/MVI/Clean Architecture chỉ là công cụ. Nếu không giải thích được invariant, lifetime, failure và compatibility, tên pattern không chứng minh kiến trúc tốt.

# 31. Kotlin/Android keyword & API index

Các keyword cần nhận diện: `package`, `import`, `class`, `interface`, `fun`, `object`, `val`, `var`, `typealias`, `this`, `super`, `as`, `is`, `in`, `when`, `if`, `else`, `for`, `while`, `try`, `catch`, `finally`, `throw`, `return`, `break`, `continue`, `sealed`, `data`, `enum`, `annotation`, `companion`, `inner`, `open`, `final`, `abstract`, `override`, `private`, `protected`, `internal`, `public`, `lateinit`, `const`, `tailrec`, `operator`, `infix`, `inline`, `noinline`, `crossinline`, `reified`, `suspend`, `external`, `expect`, `actual`, `out`, `vararg`, `where`, `by` và các contextual/use-site keywords theo language version.

Standard library families cần quen: string conversion/search, collection transformation/aggregation, null/error helpers, scope functions và sequence. Coroutine families cần nhận diện: `launch`, `async`, `coroutineScope`, `supervisorScope`, `withContext`, `delay`, `yield`, `ensureActive`, timeout, `Mutex`, Channel, Flow, StateFlow và SharedFlow.

Android families cần nhận diện: Application/Activity/Fragment/Service/Receiver/Provider; Lifecycle/ViewModel/SavedStateHandle; Compose state/effect/layout APIs; Room/DataStore/WorkManager; Navigation; testing/performance APIs.

# 32. Version matrix và cách đọc một project Android hiện đại

Baseline tài liệu này dùng Kotlin **2.4.20**, K2, Android Studio Quail 4 / 2026.1.4 Patch 1, AGP **9.4.1**, Android 17 / API 37 và Compose BOM snapshot 2026.09.00. Các số này là documentation snapshot, không phải constant kiến trúc.

Khi version thay đổi, không chỉ hỏi “latest là gì?” mà hỏi:

```text
node nào đổi?
contract nào đổi?
consumer nào bị ảnh hưởng?
artifact nào khác?
runtime behavior nào được bật?
rollback có còn tương thích dữ liệu không?
```

# 33. Compiler plugin và generated code như một phần của kiến trúc

Compose compiler plugin transform composable function; serialization/Parcelize/compiler plugin và KSP/kapt processors sinh code/metadata. Generated code ảnh hưởng compile time, API visibility, runtime startup và debugging.

Khi nâng Kotlin mà lỗi nằm trong Room/Hilt/serialization/Compose generated path, kiểm tra plugin/processor compatibility trước khi sửa business source. Clean build giúp loại stale generated artifacts; CI clean environment là tín hiệu quan trọng nếu local incremental build khác behavior.

# 34. Source compatibility, binary compatibility và behavioral compatibility

Một thay đổi có thể source-compatible nhưng binary-incompatible hoặc compile được nhưng behavior khác. Public default argument, inline function, const, value class, enum/sealed evolution và JVM signature đều cần review đặc biệt với library.

Behavioral compatibility thường bị bỏ qua: repository giữ nguyên signature nhưng đổi từ cache-first sang network-first có thể làm UX, latency và offline behavior thay đổi. Contract phải document threading, cancellation, ordering, nullability, retry và idempotency khi chúng quan trọng.

# 35. Architecture ở codebase lớn: dependency graph quan trọng hơn tên pattern

Architecture tốt giới hạn blast radius, làm dependency direction rõ và cho phép subsystem evolve độc lập ở mức hợp lý. Use case/interface/module không có giá trị nếu chỉ thêm ceremony. Mỗi abstraction cần trả lời nó đang cô lập volatility, ownership hay policy nào.

# 36. Performance engineering: hypothesis → measurement → change → verification

Bắt đầu từ user-facing metric như startup, frame time, time-to-content, memory, network latency, battery hoặc artifact size. Thu trace/profile trên device đại diện, tạo hypothesis, thay đổi một yếu tố và đo lại.

Nhìn percentile, không chỉ average. Một UI average 10 ms nhưng thường xuyên có frame 100 ms vẫn jank. Baseline Profile/Macrobenchmark/Perfetto là công cụ đo; chúng không thay design đúng.

# 37. Reliability engineering trên mobile

Mobile app sống cùng process death, network transition, duplicate delivery, server/client version skew và partial failure. Production design phải định nghĩa idempotency, retry policy, local persistence, conflict, reconstruction và observability trước khi bug xảy ra.

Offline-first không có nghĩa mọi app phải có distributed sync engine. Nó nghĩa requirement offline được model rõ. Nếu chỉ cần cached read, đừng xây durable mutation queue không cần thiết.

# 38. Security engineering: xem APK là môi trường không đáng tin

Attacker có thể inspect/decompile/hook client. Không lưu server secret dài hạn trong APK rồi kỳ vọng R8 bảo vệ. Backend phải authorize. Client chỉ giữ credential/session với lifetime và secure-storage strategy phù hợp.

External Intent/URI/WebView/native input đều là untrusted input. Native parser còn có memory-safety risk riêng.

# 39. Release, rollout và rollback như một phần của feature design

Staged rollout giảm blast radius chỉ khi telemetry đủ phát hiện regression. Feature flag giúp kill behavior nhưng tạo thêm state space; mỗi flag phải có owner và cleanup date.

Rollback binary không đủ nếu DB schema, serialized data hoặc backend protocol đã migrate theo hướng không tương thích. Release design cần backward/forward compatibility window cho dữ liệu quan trọng.

# 40. Modern vs legacy Android — phân loại thay vì phán xét

Không nên gắn `legacy = sai`, `modern = đúng`. Hãy phân loại:

```text
Deprecated / unsafe
→ cần migration có kế hoạch

Supported nhưng có replacement hiện đại
→ migrate khi benefit > cost

Still-valid API cho use case cụ thể
→ giữ nếu contract phù hợp

Historical API
→ học để đọc code cũ, không dùng cho code mới
```

Ví dụ phổ biến:

| Thế hệ cũ | Hướng modern | Ghi chú |
|---|---|---|
| Java-heavy Android | Kotlin-first | Java interop vẫn quan trọng |
| Kotlin synthetic views | View Binding / Compose | synthetic không còn là modern workflow |
| `findViewById` | View Binding / Compose | vẫn hợp lệ trong View code |
| XML/Fragment | Compose hoặc hybrid | XML/Fragment vẫn supported |
| `AsyncTask` | coroutine / WorkManager theo lifetime | không thay bằng coroutine một cách máy móc |
| callback pyramid | suspend / Flow | callback vẫn tồn tại ở platform boundary |
| LiveData everywhere | Flow/StateFlow ở modern stack | LiveData vẫn usable/interop tốt |
| SharedPreferences | DataStore cho structured settings | không phải mọi key-value đều buộc migrate tức thì |
| `startActivityForResult` | Activity Result API | lifecycle-aware contract tốt hơn |
| manual Service cho deferred work | WorkManager | Service vẫn đúng cho ongoing user-visible work |
| RxJava-heavy | coroutine/Flow phổ biến hơn | RxJava codebase không tự động sai |
| kapt | KSP khi processor hỗ trợ | migrate per-processor |
| `kotlinOptions {}` | `compilerOptions {}` | modern Kotlin Gradle DSL |
| Compose compiler mapping riêng | Compose compiler plugin cùng Kotlin | Kotlin 2.0+ |
| K1 | K2 | K2 là compiler generation mặc định mới |

Migration tốt giữ behavior trước rồi thay implementation. Characterization test, adapter boundary và incremental rollout quan trọng hơn “rewrite sạch”.

# 41. Master checklist trước khi gọi hệ thống production-ready

Một hệ thống Kotlin/Android mature phải trả lời được:

```text
Version/toolchain contract là gì?
Source of truth ở đâu?
Owner của state/coroutine/resource là ai?
Điều gì sống qua recomposition/configuration/process death?
Race/order/idempotency được kiểm soát thế nào?
Flow/event semantics có bị mất hoặc replay sai không?
Compose effect có đúng lifetime không?
Network/database migration có rollback-compatible không?
Security boundary nào nhận untrusted input?
Metric/log nào chứng minh behavior production?
Release artifact nào đang chạy trên device?
R8/signing/variant có được test không?
Feature lỗi thì rollback/disable bằng cách nào?
Legacy path bao giờ được xóa?
```

Mastery không phải nhớ toàn bộ Android SDK. Nó là khả năng hạ một vấn đề từ UI xuống state/lifecycle, từ coroutine xuống ordering/cancellation, từ Kotlin source xuống compiler/bytecode, từ Gradle xuống artifact, và từ bug production xuống invariant + evidence thay vì đoán.