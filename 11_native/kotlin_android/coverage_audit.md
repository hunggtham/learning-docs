# Kotlin + Android — Coverage Audit

Tài liệu này kiểm tra bộ note đã cover những lớp kiến thức nào và phần nào thuộc learning spine, deep-dive, production casebook hay depth lab. Đây không phải cheat sheet. Vai trò của nó là tránh hai lỗi khi library lớn dần: **bổ sung trùng lặp** và **bỏ sót một boundary/failure mode quan trọng**.

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
| Java interop/ABI/compiler plugin | Master | Advanced + Case 08 + Case 20 + Depth Lab 07 |

## 2. Coroutine và Flow

| Nhóm | Coverage | Nơi đọc chính |
|---|---|---|
| `suspend`, `launch`, `async`, `withContext` | Đầy đủ | Intermediate |
| structured concurrency/supervision | Đầy đủ + reasoning sâu | Intermediate + Deep Dive 02 + Depth Lab 03 |
| cancellation/exception propagation | Đầy đủ + failure semantics | Intermediate + Advanced + Depth Lab 03 |
| `CoroutineContext`/Job hierarchy | Deep dive | Deep Dive 02 + Depth Lab 03 |
| Flow cold/hot | Đầy đủ + lifetime semantics | Intermediate + Deep Dive 02 + Depth Lab 03 |
| StateFlow/SharedFlow | Đầy đủ | Intermediate + Depth Lab 03 |
| `stateIn`/`shareIn`/SharingStarted | Đầy đủ | Deep Dive 02 + Depth Lab 03 |
| `flowOn`/context preservation | Đầy đủ | Deep Dive 02 + Depth Lab 03 |
| `callbackFlow` | Đầy đủ | Deep Dive 02 + Case 06 + Depth Lab 03 |
| buffer/conflate/collectLatest/backpressure | Senior sâu | Deep Dive 03 + Depth Lab 03 |
| Channel/Mutex/atomic/shared state | Senior sâu | Advanced + Depth Lab 03 |
| dispatcher injection/test scheduler | Senior | Advanced + Deep Dive 02 + Depth Lab 03 |
| main-safety/thread confinement | Production | Case 09 + Depth Lab 03 |
| stale-result/concurrent-session race | Production reasoning | Depth Lab 03 |
| native callback/thread crossing | Production/native | Case 17 + Depth Lab 07 |

## 3. Android runtime và component model

| Nhóm | Coverage | Nơi đọc chính |
|---|---|---|
| Activity/Service/Receiver/Provider | Nền tảng → production | Beginner + Case 14 |
| Context/Application/Activity lifetime | Đầy đủ | Deep Dive 01 + Case 09 |
| Intent/Bundle/Uri | Đầy đủ | Beginner + Deep Dive 01 + Case 14 |
| lifecycle/configuration change | Đầy đủ | Beginner → Advanced + Case 04 |
| process death/SavedStateHandle | Đầy đủ + reconstruction reasoning | Intermediate + Advanced + Case 04/09 + Depth Lab 01/05 |
| Linux process/app sandbox | Platform | Case 09 |
| Looper/MessageQueue/Handler | Platform | Case 09 |
| Binder/IPC/Parcelable transaction | Platform | Case 09 |
| ART/DEX/class loading/runtime memory | Platform | Case 08/09 |
| Service/Receiver/Provider cold entry | Production | Case 14 |
| notification/widget/shortcut/tile | Production | Case 14 |
| startup initialization critical path | Production sâu | Case 19 + Depth Lab 06 |

## 4. Jetpack Compose UI

| Nhóm | Coverage | Nơi đọc chính |
|---|---|---|
| composable/layout/modifier | Đầy đủ | Beginner + Deep Dive 01 |
| state/recomposition/hoisting | Đầy đủ + reasoning sâu | Beginner → Advanced + Deep Dive 02 + Depth Lab 04 |
| remember/rememberSaveable | Đầy đủ | Beginner + Intermediate + Depth Lab 04 |
| effect APIs | Đầy đủ + lifetime semantics | Intermediate + Deep Dive 02 + Case 11 + Depth Lab 04 |
| lazy identity/key | Đầy đủ sâu | Deep Dive 02/03 + Case 11 + Depth Lab 04 |
| Snapshot State/CompositionLocal | Senior sâu | Advanced + Deep Dive 03 + Depth Lab 04 |
| composition/layout/draw phases | Đầy đủ sâu | Deep Dive 03 + Case 11 + Depth Lab 04 |
| constraint/custom layout/draw | Production UI | Case 11 + Depth Lab 04 |
| gestures/nested scroll/input | Production UI | Case 11 + Depth Lab 04 |
| focus/IME/hardware keyboard | Production UI | Case 11 + Depth Lab 04 |
| animation state model | Production UI | Case 11 + Depth Lab 04 |
| semantics/accessibility | Đầy đủ sâu | Master + Deep Dive 04 + Case 11 + Depth Lab 04/05 |
| edge-to-edge/insets | Đầy đủ | Case 11 + Depth Lab 04 |
| adaptive/foldable/window sizes | Đầy đủ | Master + Case 11 |
| first composition/startup cost | Production performance | Case 19 + Depth Lab 06 |
| phase-specific invalidation/performance | Senior/Master reasoning | Depth Lab 04 |

## 5. XML/View và legacy interoperability

XML layout, View Binding, Fragment/View lifecycle, RecyclerView, Data Binding awareness và Compose/View interoperability được giữ từ Beginner/Intermediate. Case 06 mở rộng incremental migration Java/XML/Fragment/LiveData/Rx → Kotlin/coroutine/Flow/Compose. Case 11 cover `AndroidView`/`ComposeView` như interoperability boundary. Legacy API được phân loại thành deprecated/historical/still-valid thay vì gắn nhãn “sai” một cách máy móc.

## 6. Architecture và state management

| Nhóm | Coverage | Nơi đọc chính |
|---|---|---|
| ViewModel/UiState/UDF | Đầy đủ | Intermediate + Case 01 |
| repository/data source | Đầy đủ + semantic boundary | Intermediate + Case 01 + Depth Lab 01 |
| source of truth | Đầy đủ + ownership reasoning | Intermediate + Deep Dive 02 + Case 01/03 + Depth Lab 01/02 |
| domain/use-case layer decision | Đầy đủ | Intermediate + Case 01 + Depth Lab 01 |
| offline-first/sync/conflict | Production sâu | Advanced/Master + Case 03 + Depth Lab 02 |
| transaction invariant/outbox/idempotency | Production sâu | Case 03 + Depth Lab 01/02 |
| stale snapshot/ambiguous outcome | Master reasoning | Depth Lab 01/02 |
| multi-module architecture | Senior/Master | Advanced/Master + Case 06/07 |
| dependency direction/API surface | Master | Master + Deep Dive 04 + Case 07/20 + Depth Lab 07 |
| ADR/ownership/governance | Master | Deep Dive 04 + Case 07 + Depth Lab 01 |
| legacy strangler migration | Đầy đủ | Case 06 |
| state reconstruction after cold/system entry | Production | Case 04/14/19 + Depth Lab 01/05 |

## 7. Persistence và storage

Room, DAO, relation, type converter, transaction, migration/schema evolution, DataStore, file/MediaStore/scoped storage, source of truth và backup concern đã được cover từ Intermediate → Senior. Case 03 đi sâu durable mutation queue, tombstone, conflict, pagination, migration và rollback compatibility. Case 12 bổ sung SAF/Photo Picker/MediaStore/content URI. Case 13 bổ sung backup/restore/upgrade-path test. Depth Lab 01–02 đào sâu transaction invariant, cursor atomicity, outbox durability, tombstone semantics và failure after partial commit.

## 8. Networking

Retrofit/serialization nằm ở Intermediate; timeout/error/cancellation ở Deep Dive 02; retry/idempotency/cache/TLS/WebSocket/SSE ở Deep Dive 03; auth/session/token refresh ở Case 02; offline sync ở Case 03; slow/unreliable connectivity ở Case 12/13. Depth Lab 02 đi sâu ambiguous outcome, idempotency key, jitter, retry classification, stale response/version guard và concurrent writer. Error được tách transport → protocol → domain; UI không phụ thuộc transport detail.

## 9. Authentication, authorization và session

Case 02 cover Credential Manager, account/session state, access/refresh token, concurrent `401`, single-flight refresh, logout và secure storage. Case 10 nhấn mạnh OS permission không phải business entitlement. Depth Lab 02–03 bổ sung account isolation, session epoch, in-flight response từ account cũ và single-flight concurrency. Security model không xem client/device là trusted authority.

## 10. Dependency Injection

Constructor injection, Hilt/DI concept, scope/lifetime và large-scale DI đã được cover. DI không được coi là architecture; nó quản lý dependency graph/lifetime. Case 14/19 nhấn mạnh system entry point và startup initialization không được phụ thuộc MainActivity chạy trước. Case 20/Depth Lab 07 cover dependency exposure từ góc SDK author.

## 11. Background execution

WorkManager, foreground service/work, notification, exact-alarm awareness, coroutine lifetime và background restriction đã được cover. Deep Dive 03 có decision framework; Case 10 nối foreground execution với permission/system policy; Case 14 phân biệt Service/Receiver/WorkManager theo lifetime/durability; Case 18 đặt chúng vào target-SDK migration. Depth Lab 02 nhấn mạnh WorkManager là scheduler chứ không phải sync correctness engine.

## 12. Testing

| Tầng | Coverage |
|---|---|
| pure Kotlin JVM unit test | Beginner + Intermediate |
| fake/mock/test double | Deep Dive 02 + Depth Lab 05 |
| coroutine virtual-time/Flow test | Intermediate + Deep Dive 02 + Depth Lab 03/05 |
| deterministic race ordering | Senior/Master | Depth Lab 03/05 |
| property-based/invariant testing | Master | Depth Lab 02/05 |
| Robolectric | Deep Dive 03 |
| instrumented Android test | Beginner + Deep Dive 03 |
| Compose UI/semantics/accessibility | Case 11/13 + Depth Lab 04/05 |
| Room/network integration/contract | Advanced + Case 05 + Depth Lab 05 |
| hardware/device integration | Case 12 + Depth Lab 05 |
| migration/upgrade/rollback path | Case 03/13/18 + Depth Lab 05 |
| process-death/cold-entry reconstruction | Case 04/14/19 + Depth Lab 01/05 |
| Macrobenchmark/Baseline Profile | Case 05/19 + Depth Lab 05/06 |
| OS/OEM/device matrix | Case 13/18 + Depth Lab 05/06 |
| release bundle/split install | Case 16 + Depth Lab 06 |
| native ABI/page size/symbol validation | Case 17 + Depth Lab 07 |
| minified SDK consumer/API compatibility | Case 20 + Depth Lab 07 |

## 13. Performance

Main-thread/ANR/leak, Compose recomposition, R8, startup, Baseline Profile, Macrobenchmark, Perfetto, memory/battery/network và performance budget đã được cover. Case 09 đi sâu event loop/Binder/ART/GC/thread contention; Case 11 cover hot UI paths; Case 13 cover low-memory/thermal/device quality; Case 17 cover native memory/JNI overhead; Case 19 tập trung cold/warm/hot start và startup critical path. Depth Lab 04 nhấn mạnh phase-specific invalidation và evidence-based Compose optimization; Depth Lab 05–06 nối benchmark với SLO, release-like build và startup critical path.

## 14. Security và privacy

Coverage gồm secure config, Credential Manager, WebView boundary, Android Keystore, TLS/Network Security Config, backend authorization, integrity awareness, backup policy, Data Safety/privacy inventory, PendingIntent/exported components, supply-chain dependency risk và native parser/memory-safety awareness. Obfuscation không được xem là secret storage; integrity chỉ là risk signal; external Intent/URI/Binder/native input đều được coi là untrusted. Depth Lab 07 bổ sung privacy/logging obligations của SDK consumer-facing.

## 15. Build, Gradle và AGP

Case 15 nâng phần build từ awareness lên production mental model: Gradle vs AGP vs Kotlin plugin; root/settings/module model; build type/product flavor/variant; source-set precedence; manifest/resource merging; dependency configurations; version catalogs; convention plugins; configuration/build cache; Java/Kotlin toolchain; Variant API; D8/R8; signing; reproducibility và CI variant strategy.

Depth Lab 06 đào sâu build theo phase, dependency visibility, generated-code forensic, release-only R8 failure, variant-only issue, merged manifest/resource review, dependency lock và artifact provenance. Các file Beginner/Master/Deep Dive 04 vẫn giữ build fundamentals và governance.

## 16. AAB, packaging và distribution

Case 16 cover APK vs AAB, split APK, `bundletool`, dynamic feature/Play Feature Delivery, install-time/on-demand/conditional delivery, asset/size concern, ABI/language splits, Play App Signing, version metadata, release tracks, staged rollout, mobile rollback limitation, distribution-channel boundary và artifact provenance.

Depth Lab 06 nhấn mạnh final installed artifact có thể khác upload bundle theo device configuration, và release gate phải verify artifact/delivery path chứ không chỉ source. AAB upload size không được nhầm với download/install size thực tế. Dynamic feature chỉ dùng khi delivery benefit bù được install-state complexity.

## 17. Native/NDK/JNI

Case 17 cover `.so`, ABI, JNI static/dynamic registration, local/global references, `JNIEnv` thread affinity, callback, array/direct buffer, native memory, RAII, CMake, prebuilt native libraries, native API levels, file descriptor bridge, symbolication, tombstone, sanitizers, JNI batching và security.

Depth Lab 07 đào sâu consumer safety ở JNI boundary: thread ownership, pending Java exception, buffer/reference lifetime, coarse-grained boundary, ABI testing, native symbol provenance và host-process blast radius. 16 KB page-size compatibility được xem như release requirement đối với app/SDK có native library, bao gồm prebuilt vendor `.so`.

## 18. Android compatibility engineering

Case 18 cover bốn version axes (`minSdk`, `compileSdk`, `targetSdk`, device OS), all-app vs target-gated behavior changes, compatibility framework, API guards/`@RequiresApi`, Jetpack compat abstraction, desugaring, SDK Extensions, updatable system components, non-SDK restrictions, WebView versioning, target-API policy và OS/target migration playbook.

Depth Lab 06 bổ sung forensic theo phase, compile migration vs behavior migration, OEM/WebView dimension, dependency/toolchain isolation và exact-variant reproduction. Platform upgrade được tách thành current-app-on-new-OS testing và targetSdk migration, thay vì tăng target rồi sửa lỗi đồng loạt.

## 19. App startup và initialization

Case 19 cover cold/warm/hot start, TTID/TTFD, Application/provider auto-init, AndroidX App Startup, lazy/eager initialization, DI constructor side effects, SplashScreen, startup routing, class loading/static init, Compose first frame, Baseline Profile, Macrobenchmark, Perfetto, StrictMode, SDK initialization governance, DB migration/startup, multi-process init và startup budgets.

Depth Lab 06 đi sâu startup như dependency critical path, phân loại eager/lazy/demand-driven work và tách TTID khỏi TTFD. Startup được coi là critical path có budget, không phải collection các `init()` call.

## 20. Android library/SDK authoring

Case 20 cover AAR vs pure JVM library, public API surface, source/binary compatibility, Kotlin/Java interop, dependency exposure, resource/manifest contract, Compose library API, threading/coroutine/Flow contract, error model, consumer ProGuard rules, minified consumer test, custom lint, SemVer behavioral compatibility, ABI validation, public inline/data/enum evolution, publishing, sample apps, support matrix, deprecation và privacy/security obligations của SDK.

Depth Lab 07 đi sâu source vs binary vs behavioral compatibility, Kotlin/Java ABI ergonomics, dependency leakage, auto-init startup debt, callback/thread/error contract, consumer R8, API dump, old-consumer compatibility test và artifact provenance.

## 21. Production governance

Master + Deep Dive 04 + Case 05/07/13/15/16 cover observability schema, performance budget, dependency governance/SBOM, ADR, code ownership, flaky-test policy, feature-flag lifecycle, target-SDK cadence, artifact provenance, incident response và rollback compatibility. Depth Lab 05 bổ sung SLI/SLO, structured telemetry, staged rollout guardrail, flaky-test debt và postmortem feedback loop.

## 22. Kotlin Multiplatform

KMP được giữ ở Master thay vì đưa vào Beginner. Coverage tập trung shared business logic, public API, `expect/actual`, platform boundary, threading/serialization và tiêu chí share đúng concern thay vì tối đa hóa phần trăm shared code.

## 23. Offline-first và synchronization

Case 03 cover optimistic write, durable queue, idempotency key, retry/backoff, tombstone, conflict resolution, cursor, Paging/RemoteMediator và schema migration. Depth Lab 02 tăng độ sâu bằng consistency model, outbox invariant, idempotency key lifecycle, retry+jitter, mutation compaction, version/conflict, pull/push ordering, checkpoint atomicity, poison mutation, sync debt và account isolation.

## 24. Permission, capability và system contract

Case 10 cover hardware capability vs permission, `<uses-feature>`, permission revocation, foreground/background location, Bluetooth/Nearby, local-network protection, notification, camera/mic, Photo Picker/SAF, foreground service, exact alarm, exported component, App Links và target-SDK concerns. Depth Lab 05 bổ sung permission revoke như failure-injection scenario.

## 25. Device/media/hardware integration

Case 12 cover CameraX, Media3/player/media session/audio focus, microphone, files/media picker, current/continuous location, geofence, BLE/GATT, NFC/sensor, connectivity và WebView. Những integration này được model như external stateful systems có resource ownership, timeout, lifecycle và recovery. Depth Lab 05 bổ sung hardware/device integration test theo risk.

## 26. Accessibility, adaptive UI và advanced Compose

Case 11 cover layout/draw/input pipeline, custom layout/draw, gesture/nested scroll, focus/IME, edge-to-edge, animation, semantics/accessibility, font/RTL, keyboard/mouse và adaptive/foldable strategy. Depth Lab 04 tăng độ sâu ở identity, Snapshot dependency tracking, effect key, stability, phase-specific state read, semantics tree và evidence-based optimization. Accessibility được coi là correctness/public semantic contract, không phải polish cuối.

## 27. Production device matrix và app quality

Case 13 cover risk-based OS/OEM/device matrix, fresh install/upgrade path, rollback compatibility, localization/plural/timezone/RTL, font scaling/TalkBack, battery/Doze, slow network/retry storm, low-memory/thermal, privacy inventory, telemetry, feature flags, backup/restore và incident readiness. Depth Lab 05–06 nối device matrix với release SLO, failure injection và exact-artifact forensic.

## 28. System surfaces ngoài Activity

Case 14 cover started/bound/foreground Service, BroadcastReceiver + `goAsync`, ContentProvider/ContentResolver/URI grant, notification/channel/action, PendingIntent identity/mutability, App Widget, Shortcut, Quick Settings Tile, multi-process awareness, WorkManager coordination và exported-component security.

## 29. Depth Labs — reasoning depth coverage

`depth_labs/` không mở thêm breadth mà làm sâu bảy trục đã có:

| Depth Lab | Trọng tâm độ sâu |
|---|---|
| 01 Architecture | invariant, ownership, stale snapshot, transaction boundary, ambiguous outcome, timeline review |
| 02 Offline Sync | consistency, durable outbox, idempotency, ordering, conflict, cursor atomicity, account isolation |
| 03 Coroutine/Flow | Job tree, cancellation, supervision, shared-state race, backpressure, stream lifetime, deterministic test |
| 04 Compose | Snapshot identity, effect lifetime, phase invalidation, stability, semantics, measured performance |
| 05 Reliability | invariant-based test, migration/rollback, failure injection, SLI/SLO, telemetry, rollout/incident loop |
| 06 Build/Compatibility | build phase forensic, R8/variant failure, target migration, startup critical path, artifact provenance |
| 07 SDK/Native | public API/ABI, dependency leakage, consumer safety, JNI lifetime/threading, compatibility evolution |

Depth Labs được dùng khi người học đã biết API và cần giải thích **tại sao hệ thống vẫn đúng khi execution order không lý tưởng**.

## 30. Các chủ đề cố ý không biến thành vendor manual

Bộ note không cố trở thành reference manual cho Firebase, từng DI framework, từng HTTP client, Google Maps, Billing SDK, từng ML stack, cloud vendor hay mọi API Play Console. Những sản phẩm đó evolve nhanh. Tài liệu ưu tiên mental model, contract, lifetime, failure, compatibility và integration boundary để tool mới vẫn đặt được vào hệ thống đã hiểu.

## 31. Tiêu chí cho vòng update tiếp theo

Sau Case 20 + Depth Labs, breadth của Kotlin + Android đã rất rộng và các boundary chính đã có reasoning sâu. Chapter/lab mới chỉ nên được thêm khi ít nhất một điều đúng:

1. Android/Kotlin có behavior mới làm thay đổi mental model hoặc migration path.
2. Một boundary production quan trọng vẫn chưa được giải thích hoặc invariant chưa được chứng minh.
3. Một nhóm legacy code phổ biến chưa có migration strategy.
4. Một failure mode production chưa có recovery/test model.
5. Toolchain/platform policy mới làm ví dụ hiện tại sai.
6. Một domain Android chuyên biệt được quyết định học sâu riêng, ví dụ Wear/TV/Auto/XR, game/graphics hoặc ML on-device; khi đó nên tạo sub-library riêng thay vì nhồi vào core path.
7. Một chapter hiện có còn quá tóm tắt; trong trường hợp đó ưu tiên **đào sâu chapter/lab hiện hữu** thay vì tạo thêm title mới.

Không mở rộng chỉ để tăng số dòng. Mục tiêu của bộ note là **đủ sâu nhưng có cấu trúc**, để người học biết khái niệm là gì, vì sao tồn tại, khi nào dùng, trade-off ra sao, invariant nào phải giữ, nó thất bại như thế nào, artifact nào thực sự chạy trên device và cách đặt nó vào một production system có thể build, test, release, quan sát và evolve lâu dài.
