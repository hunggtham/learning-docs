# Kotlin + Android — Coverage Audit

Tài liệu này kiểm tra bộ note đã cover những lớp kiến thức nào và phần nào thuộc learning spine, deep-dive hay production casebook. Đây không phải cheat sheet. Vai trò của nó là tránh hai lỗi khi library lớn dần: **bổ sung trùng lặp** và **bỏ sót một boundary/failure mode quan trọng**.

## 1. Kotlin language foundations

| Nhóm | Coverage | Nơi đọc chính |
|---|---|---|
| syntax, `val`/`var`, type inference | Nền tảng đầy đủ | Beginner |
| null-safety, smart cast, cast | Nền tảng đầy đủ | Beginner |
| function/default/named/vararg | Đầy đủ | Beginner |
| class/property/inheritance/interface | Đầy đủ | Beginner |
| data/enum/sealed | Đầy đủ theo level | Beginner + Intermediate |
| package/import/top-level declaration | Deep dive | Deep Dive 01 |
| equality/range/array/collection transformations | Đầy đủ | Beginner + Deep Dive 01 |
| lambda/HOF/scope functions | Đầy đủ | Beginner + Intermediate |
| generics/variance/projection/erasure | Đầy đủ | Intermediate + Advanced + Case 08 |
| delegation/delegated property | Đầy đủ | Intermediate |
| inline/reified/contracts/reflection | Advanced | Advanced + Case 08 |
| value class/boxing/JVM representation | Master | Master + Case 08 |
| suspend state machine/lambda capture | Under the hood | Case 08 |
| Java interop/ABI/compiler plugin | Master | Advanced + Case 08 + Case 20 |

## 2. Coroutine và Flow

| Nhóm | Coverage | Nơi đọc chính |
|---|---|---|
| `suspend`, `launch`, `async`, `withContext` | Đầy đủ | Intermediate |
| structured concurrency/supervision | Đầy đủ | Intermediate + Deep Dive 02 |
| cancellation/exception propagation | Đầy đủ | Intermediate + Advanced |
| `CoroutineContext`/Job hierarchy | Deep dive | Deep Dive 02 |
| Flow cold/hot | Đầy đủ | Intermediate + Deep Dive 02 |
| StateFlow/SharedFlow | Đầy đủ | Intermediate |
| `stateIn`/`shareIn`/SharingStarted | Đầy đủ | Deep Dive 02 |
| `flowOn`/context preservation | Đầy đủ | Deep Dive 02 |
| `callbackFlow` | Đầy đủ | Deep Dive 02 + Case 06 |
| buffer/conflate/collectLatest/backpressure | Senior | Deep Dive 03 |
| Channel/Mutex/atomic/shared state | Senior | Advanced |
| dispatcher injection/test scheduler | Senior | Advanced + Deep Dive 02 |
| main-safety/thread confinement | Production | Case 09 |
| native callback/thread crossing | Production/native | Case 17 |

## 3. Android runtime và component model

| Nhóm | Coverage | Nơi đọc chính |
|---|---|---|
| Activity/Service/Receiver/Provider | Nền tảng → production | Beginner + Case 14 |
| Context/Application/Activity lifetime | Đầy đủ | Deep Dive 01 + Case 09 |
| Intent/Bundle/Uri | Đầy đủ | Beginner + Deep Dive 01 + Case 14 |
| lifecycle/configuration change | Đầy đủ | Beginner → Advanced + Case 04 |
| process death/SavedStateHandle | Đầy đủ | Intermediate + Advanced + Case 04/09 |
| Linux process/app sandbox | Platform | Case 09 |
| Looper/MessageQueue/Handler | Platform | Case 09 |
| Binder/IPC/Parcelable transaction | Platform | Case 09 |
| ART/DEX/class loading/runtime memory | Platform | Case 08/09 |
| Service/Receiver/Provider cold entry | Production | Case 14 |
| notification/widget/shortcut/tile | Production | Case 14 |
| startup initialization critical path | Production | Case 19 |

## 4. Jetpack Compose UI

| Nhóm | Coverage | Nơi đọc chính |
|---|---|---|
| composable/layout/modifier | Đầy đủ | Beginner + Deep Dive 01 |
| state/recomposition/hoisting | Đầy đủ | Beginner → Advanced + Deep Dive 02 |
| remember/rememberSaveable | Đầy đủ | Beginner + Intermediate |
| effect APIs | Đầy đủ | Intermediate + Deep Dive 02 + Case 11 |
| lazy identity/key | Đầy đủ | Deep Dive 02/03 + Case 11 |
| Snapshot State/CompositionLocal | Senior | Advanced + Deep Dive 03 |
| composition/layout/draw phases | Đầy đủ sâu | Deep Dive 03 + Case 11 |
| constraint/custom layout/draw | Production UI | Case 11 |
| gestures/nested scroll/input | Production UI | Case 11 |
| focus/IME/hardware keyboard | Production UI | Case 11 |
| animation state model | Production UI | Case 11 |
| semantics/accessibility | Đầy đủ sâu | Master + Deep Dive 04 + Case 11 |
| edge-to-edge/insets | Đầy đủ | Case 11 |
| adaptive/foldable/window sizes | Đầy đủ | Master + Case 11 |
| first composition/startup cost | Production performance | Case 19 |

## 5. XML/View và legacy interoperability

XML layout, View Binding, Fragment/View lifecycle, RecyclerView, Data Binding awareness và Compose/View interoperability được giữ từ Beginner/Intermediate. Case 06 mở rộng incremental migration Java/XML/Fragment/LiveData/Rx → Kotlin/coroutine/Flow/Compose. Case 11 cover `AndroidView`/`ComposeView` như interoperability boundary. Legacy API được phân loại thành deprecated/historical/still-valid thay vì gắn nhãn “sai” một cách máy móc.

## 6. Architecture và state management

| Nhóm | Coverage | Nơi đọc chính |
|---|---|---|
| ViewModel/UiState/UDF | Đầy đủ | Intermediate + Case 01 |
| repository/data source | Đầy đủ | Intermediate + Case 01 |
| source of truth | Đầy đủ | Intermediate + Deep Dive 02 + Case 01/03 |
| domain/use-case layer decision | Đầy đủ | Intermediate + Case 01 |
| offline-first/sync/conflict | Production | Advanced/Master + Case 03 |
| multi-module architecture | Senior/Master | Advanced/Master + Case 06/07 |
| dependency direction/API surface | Master | Master + Deep Dive 04 + Case 07/20 |
| ADR/ownership/governance | Master | Deep Dive 04 + Case 07 |
| legacy strangler migration | Đầy đủ | Case 06 |
| state reconstruction after cold/system entry | Production | Case 04/14/19 |

## 7. Persistence và storage

Room, DAO, relation, type converter, transaction, migration/schema evolution, DataStore, file/MediaStore/scoped storage, source of truth và backup concern đã được cover từ Intermediate → Senior. Case 03 đi sâu durable mutation queue, tombstone, conflict, pagination, migration và rollback compatibility. Case 12 bổ sung SAF/Photo Picker/MediaStore/content URI. Case 13 bổ sung backup/restore/upgrade-path test.

## 8. Networking

Retrofit/serialization nằm ở Intermediate; timeout/error/cancellation ở Deep Dive 02; retry/idempotency/cache/TLS/WebSocket/SSE ở Deep Dive 03; auth/session/token refresh ở Case 02; offline sync ở Case 03; slow/unreliable connectivity ở Case 12/13. Error được tách transport → protocol → domain; UI không phụ thuộc transport detail.

## 9. Authentication, authorization và session

Case 02 cover Credential Manager, account/session state, access/refresh token, concurrent `401`, single-flight refresh, logout và secure storage. Case 10 nhấn mạnh OS permission không phải business entitlement. Security model không xem client/device là trusted authority.

## 10. Dependency Injection

Constructor injection, Hilt/DI concept, scope/lifetime và large-scale DI đã được cover. DI không được coi là architecture; nó quản lý dependency graph/lifetime. Case 14/19 nhấn mạnh system entry point và startup initialization không được phụ thuộc MainActivity chạy trước. Case 20 cover dependency exposure từ góc SDK author.

## 11. Background execution

WorkManager, foreground service/work, notification, exact-alarm awareness, coroutine lifetime và background restriction đã được cover. Deep Dive 03 có decision framework; Case 10 nối foreground execution với permission/system policy; Case 14 phân biệt Service/Receiver/WorkManager theo lifetime/durability; Case 18 đặt chúng vào target-SDK migration.

## 12. Testing

| Tầng | Coverage |
|---|---|
| pure Kotlin JVM unit test | Beginner + Intermediate |
| fake/mock/test double | Deep Dive 02 |
| coroutine virtual-time/Flow test | Intermediate + Deep Dive 02 |
| Robolectric | Deep Dive 03 |
| instrumented Android test | Beginner + Deep Dive 03 |
| Compose UI/semantics/accessibility | Case 11/13 |
| Room/network integration/contract | Advanced + Case 05 |
| hardware/device integration | Case 12 |
| migration/upgrade path | Case 03/13/18 |
| cold-start/deep-link/system entry | Case 14/19 |
| Macrobenchmark/Baseline Profile | Case 05/19 |
| OS/OEM/device matrix | Case 13/18 |
| release bundle/split install | Case 16 |
| native ABI/page size/symbol validation | Case 17 |
| minified SDK consumer/API compatibility | Case 20 |

## 13. Performance

Main-thread/ANR/leak, Compose recomposition, R8, startup, Baseline Profile, Macrobenchmark, Perfetto, memory/battery/network và performance budget đã được cover. Case 09 đi sâu event loop/Binder/ART/GC/thread contention; Case 11 cover hot UI paths; Case 13 cover low-memory/thermal/device quality; Case 17 cover native memory/JNI overhead; Case 19 tập trung cold/warm/hot start và startup critical path.

## 14. Security và privacy

Coverage gồm secure config, Credential Manager, WebView boundary, Android Keystore, TLS/Network Security Config, backend authorization, integrity awareness, backup policy, Data Safety/privacy inventory, PendingIntent/exported components, supply-chain dependency risk và native parser/memory-safety awareness. Obfuscation không được xem là secret storage; integrity chỉ là risk signal; external Intent/URI/Binder/native input đều được coi là untrusted.

## 15. Build, Gradle và AGP

Case 15 nâng phần build từ awareness lên production mental model: Gradle vs AGP vs Kotlin plugin; root/settings/module model; build type/product flavor/variant; source-set precedence; manifest/resource merging; dependency configurations; version catalogs; convention plugins; configuration/build cache; Java/Kotlin toolchain; Variant API; D8/R8; signing; reproducibility và CI variant strategy.

Các file Beginner/Master/Deep Dive 04 vẫn giữ build fundamentals và governance, còn Case 15 là nơi đọc sâu khi cần debug hoặc thiết kế build system.

## 16. AAB, packaging và distribution

Case 16 cover APK vs AAB, split APK, `bundletool`, dynamic feature/Play Feature Delivery, install-time/on-demand/conditional delivery, asset/size concern, ABI/language splits, Play App Signing, version metadata, release tracks, staged rollout, mobile rollback limitation, distribution-channel boundary và artifact provenance.

AAB upload size không được nhầm với download/install size thực tế. Dynamic feature chỉ dùng khi delivery benefit bù được install-state complexity.

## 17. Native/NDK/JNI

Case 17 cover `.so`, ABI, JNI static/dynamic registration, local/global references, `JNIEnv` thread affinity, callback, array/direct buffer, native memory, RAII, CMake, prebuilt native libraries, native API levels, file descriptor bridge, symbolication, tombstone, sanitizers, JNI batching và security.

16 KB page-size compatibility được xem như release requirement đối với app có native library, bao gồm cả prebuilt vendor `.so`.

## 18. Android compatibility engineering

Case 18 cover bốn version axes (`minSdk`, `compileSdk`, `targetSdk`, device OS), all-app vs target-gated behavior changes, compatibility framework, API guards/`@RequiresApi`, Jetpack compat abstraction, desugaring, SDK Extensions, updatable system components, non-SDK restrictions, WebView versioning, target-API policy và OS/target migration playbook.

Platform upgrade được tách thành current-app-on-new-OS testing và targetSdk migration, thay vì tăng target rồi sửa lỗi đồng loạt.

## 19. App startup và initialization

Case 19 cover cold/warm/hot start, TTID/TTFD, Application/provider auto-init, AndroidX App Startup, lazy/eager initialization, DI constructor side effects, SplashScreen, startup routing, class loading/static init, Compose first frame, Baseline Profile, Macrobenchmark, Perfetto, StrictMode, SDK initialization governance, DB migration/startup, multi-process init và startup budgets.

Startup được coi là critical path có budget, không phải collection các `init()` call.

## 20. Android library/SDK authoring

Case 20 cover AAR vs pure JVM library, public API surface, source/binary compatibility, Kotlin/Java interop, dependency exposure, resource/manifest contract, Compose library API, threading/coroutine/Flow contract, error model, consumer ProGuard rules, minified consumer test, custom lint, SemVer behavioral compatibility, ABI validation, public inline/data/enum evolution, publishing, sample apps, support matrix, deprecation và privacy/security obligations của SDK.

## 21. Production governance

Master + Deep Dive 04 + Case 05/07/13/15/16 cover observability schema, performance budget, dependency governance/SBOM, ADR, code ownership, flaky-test policy, feature-flag lifecycle, target-SDK cadence, artifact provenance, incident response và rollback compatibility.

## 22. Kotlin Multiplatform

KMP được giữ ở Master thay vì đưa vào Beginner. Coverage tập trung shared business logic, public API, `expect/actual`, platform boundary, threading/serialization và tiêu chí share đúng concern thay vì tối đa hóa phần trăm shared code.

## 23. Offline-first và synchronization

Case 03 cover optimistic write, durable queue, idempotency key, retry/backoff, tombstone, conflict resolution, cursor, Paging/RemoteMediator và schema migration. Đây là production data model chứ không chỉ Room API tutorial.

## 24. Permission, capability và system contract

Case 10 cover hardware capability vs permission, `<uses-feature>`, permission revocation, foreground/background location, Bluetooth/Nearby, local-network protection, notification, camera/mic, Photo Picker/SAF, foreground service, exact alarm, exported component, App Links và target-SDK concerns.

## 25. Device/media/hardware integration

Case 12 cover CameraX, Media3/player/media session/audio focus, microphone, files/media picker, current/continuous location, geofence, BLE/GATT, NFC/sensor, connectivity và WebView. Những integration này được model như external stateful systems có resource ownership, timeout, lifecycle và recovery.

## 26. Accessibility, adaptive UI và advanced Compose

Case 11 cover layout/draw/input pipeline, custom layout/draw, gesture/nested scroll, focus/IME, edge-to-edge, animation, semantics/accessibility, font/RTL, keyboard/mouse và adaptive/foldable strategy. Accessibility được coi là correctness/public semantic contract, không phải polish cuối.

## 27. Production device matrix và app quality

Case 13 cover risk-based OS/OEM/device matrix, fresh install/upgrade path, rollback compatibility, localization/plural/timezone/RTL, font scaling/TalkBack, battery/Doze, slow network/retry storm, low-memory/thermal, privacy inventory, telemetry, feature flags, backup/restore và incident readiness.

## 28. System surfaces ngoài Activity

Case 14 cover started/bound/foreground Service, BroadcastReceiver + `goAsync`, ContentProvider/ContentResolver/URI grant, notification/channel/action, PendingIntent identity/mutability, App Widget, Shortcut, Quick Settings Tile, multi-process awareness, WorkManager coordination và exported-component security.

## 29. Các chủ đề cố ý không biến thành vendor manual

Bộ note không cố trở thành reference manual cho Firebase, từng DI framework, từng HTTP client, Google Maps, Billing SDK, từng ML stack, cloud vendor hay mọi API Play Console. Những sản phẩm đó evolve nhanh. Tài liệu ưu tiên mental model, contract, lifetime, failure, compatibility và integration boundary để tool mới vẫn đặt được vào hệ thống đã hiểu.

## 30. Tiêu chí cho vòng update tiếp theo

Sau Case 20, breadth của Kotlin + Android đã rất rộng. Chapter mới chỉ nên được thêm khi ít nhất một điều đúng:

1. Android/Kotlin có behavior mới làm thay đổi mental model hoặc migration path.
2. Một boundary production quan trọng vẫn chưa được giải thích.
3. Một nhóm legacy code phổ biến chưa có migration strategy.
4. Một failure mode production chưa có recovery/test model.
5. Toolchain/platform policy mới làm ví dụ hiện tại sai.
6. Một domain Android chuyên biệt được quyết định học sâu riêng, ví dụ Wear/TV/Auto/XR, game/graphics hoặc ML on-device; khi đó nên tạo sub-library riêng thay vì nhồi vào core path.

Không mở rộng chỉ để tăng số dòng. Mục tiêu của bộ note là **đủ sâu nhưng có cấu trúc**, để người học biết khái niệm là gì, vì sao tồn tại, khi nào dùng, trade-off ra sao, nó thất bại như thế nào, artifact nào thực sự chạy trên device và cách đặt nó vào một production system có thể build, test, release, quan sát và evolve lâu dài.
