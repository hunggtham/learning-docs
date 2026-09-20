# Kotlin + Android — Coverage Audit

Tài liệu này dùng để kiểm tra bộ note đã cover những lớp kiến thức nào và phần nào thuộc file chính, deep-dive hay production casebook. Mục tiêu không phải tạo thêm một cheat sheet, mà là tránh hai lỗi thường gặp khi bộ tài liệu lớn dần: bổ sung trùng lặp và bỏ sót một boundary quan trọng.

## 1. Kotlin language foundations

| Nhóm | Mức coverage | Nơi đọc chính |
|---|---|---|
| syntax, `val`/`var`, type inference | Đầy đủ nền tảng | `01_kotlin_beginner.md` |
| null-safety, smart cast, cast | Đầy đủ nền tảng | `01_kotlin_beginner.md` |
| function/default/named/vararg | Đầy đủ nền tảng | `01_kotlin_beginner.md` |
| class/property/inheritance/interface | Đầy đủ nền tảng | `01_kotlin_beginner.md` |
| data/enum/sealed class | Đầy đủ | Beginner + Intermediate |
| package/import/top-level declaration | Bổ sung sâu | `deep_dive/01_beginner_completion.md` |
| equality/reference identity | Bổ sung sâu | `deep_dive/01_beginner_completion.md` |
| range/progression/array | Bổ sung sâu | `deep_dive/01_beginner_completion.md` |
| collection transformation | Đầy đủ từ cơ bản đến idiom | Beginner + Deep Dive 01 + Intermediate |
| lambda/HOF/scope function | Đầy đủ | Beginner + Intermediate |
| generics/variance/projection/erasure | Đầy đủ theo level | Intermediate + Advanced + Deep Dive 03 |
| delegation/delegated property | Đầy đủ | Intermediate |
| inline/reified/contracts/reflection | Advanced coverage | `03_kotlin_advanced_senior.md` |
| value class/K2/JVM bytecode/API design | Master coverage | Master + Case 08 |
| suspend state machine/lambda capture/boxing | Under-the-hood coverage | Case 08 |
| Java ABI/binary compatibility/compiler plugin | Master coverage | Case 08 |

## 2. Coroutine và Flow

| Nhóm | Mức coverage | Nơi đọc chính |
|---|---|---|
| suspend/launch/async/withContext | Đầy đủ | Intermediate |
| structured concurrency | Đầy đủ | Intermediate |
| CoroutineContext/Job hierarchy | Bổ sung sâu | Deep Dive 02 |
| supervision | Đầy đủ | Intermediate + Deep Dive 02 |
| cancellation/exception propagation | Đầy đủ | Intermediate + Advanced |
| cancellation-safe cleanup | Senior coverage | Deep Dive 03 |
| Flow cold/hot | Đầy đủ | Intermediate + Deep Dive 02 |
| StateFlow/SharedFlow | Đầy đủ | Intermediate |
| `stateIn`/`shareIn`/SharingStarted | Đầy đủ | Deep Dive 02 |
| `flowOn` và context preservation | Đầy đủ | Deep Dive 02 |
| `callbackFlow` | Đầy đủ | Deep Dive 02 |
| buffer/conflate/collectLatest/backpressure | Senior coverage | Deep Dive 03 |
| Channel/Mutex/atomic/shared mutable state | Senior coverage | Advanced |
| dispatcher injection/test scheduler | Senior coverage | Advanced + Deep Dive 02 |
| suspend không đồng nghĩa background thread | Runtime mental model | Case 09 |
| main-safety/thread confinement | Production coverage | Case 09 |

## 3. Android runtime và component model

| Nhóm | Mức coverage | Nơi đọc chính |
|---|---|---|
| Activity/Service/BroadcastReceiver/ContentProvider | Nền tảng + production sâu | Beginner + Case 14 |
| Context/Application/Activity lifetime | Đầy đủ | Deep Dive 01 + Case 09 |
| Intent/Bundle/Uri | Đầy đủ | Beginner + Deep Dive 01 + Case 14 |
| lifecycle/configuration change | Đầy đủ | Beginner → Advanced + Case 04 |
| process death/SavedStateHandle | Đầy đủ | Intermediate + Advanced + Case 04/09 |
| runtime permission/Activity Result | Đầy đủ | Beginner + Case 10 |
| resource/qualifier/localization | Đầy đủ | Beginner + Case 13 |
| API-level compatibility/behavior change | Senior/Master | Advanced + Master + Case 10 |
| Linux process/app sandbox | Platform coverage | Case 09 |
| main thread/Looper/MessageQueue/Handler | Platform coverage | Case 09 |
| Binder/IPC/transaction boundary | Platform coverage | Case 09 |
| ART/DEX/D8/R8/runtime memory | Platform coverage | Case 08/09 |
| Service/Receiver/Provider entry point | Production coverage | Case 14 |
| notification/widget/shortcut/tile | Production coverage | Case 14 |

## 4. UI — Jetpack Compose

| Nhóm | Mức coverage | Nơi đọc chính |
|---|---|---|
| composable/layout/modifier | Đầy đủ nền tảng | Beginner + Deep Dive 01 |
| state/recomposition | Đầy đủ theo level | Beginner → Advanced |
| state hoisting | Đầy đủ | Deep Dive 02 |
| remember/rememberSaveable | Đầy đủ | Beginner + Intermediate |
| effect APIs | Đầy đủ | Intermediate + Deep Dive 02 + Case 11 |
| lazy list identity/key | Đầy đủ | Deep Dive 02/03 + Case 11 |
| Snapshot State | Senior coverage | Advanced + Deep Dive 03 |
| CompositionLocal | Senior coverage | Deep Dive 03 |
| composition/layout/draw phase | Đầy đủ sâu | Deep Dive 03 + Case 11 |
| constraint/custom layout | Production UI coverage | Case 11 |
| custom draw/Canvas/draw cache | Production UI coverage | Case 11 |
| gesture/nested scroll/input | Production UI coverage | Case 11 |
| focus/IME/hardware keyboard | Production UI coverage | Case 11 |
| animation state model | Production UI coverage | Case 11 |
| semantics/accessibility | Đầy đủ sâu | Master + Deep Dive 04 + Case 11 |
| edge-to-edge/insets | Đầy đủ sâu | Case 11 |
| adaptive/foldable/window size | Đầy đủ sâu | Master + Case 11 |
| performance/stability/recomposition measurement | Senior coverage | Advanced + Case 05/11 |

## 5. XML/View legacy interoperability

XML layout, View Binding, Fragment/View lifecycle và Compose/View interoperability được giữ trong Beginner/Intermediate để người học đọc được project cũ. Legacy API không được mô tả như “sai”; tài liệu phân biệt deprecated API, historical pattern và pattern vẫn hợp lệ trong codebase hiện hữu. Case 06 mở rộng incremental migration, còn Case 11 cover `AndroidView`/`ComposeView` như interoperability boundary.

## 6. Architecture và state management

| Nhóm | Mức coverage | Nơi đọc chính |
|---|---|---|
| ViewModel/UI state/UDF | Đầy đủ | Intermediate + Case 01 |
| repository/data source | Đầy đủ | Intermediate + Case 01 |
| source of truth | Đầy đủ | Intermediate + Deep Dive 02 + Case 01/03 |
| offline-first/sync/conflict | Đầy đủ production | Advanced/Master + Case 03 |
| multi-module architecture | Senior/Master | Advanced/Master + Case 06/07 |
| dependency direction/API surface | Master coverage | Master + Deep Dive 04 + Case 07/08 |
| architecture decision/ADR/ownership | Master coverage | Deep Dive 04 + Case 07 |
| legacy migration/strangler approach | Đầy đủ | Advanced/Master + Case 06 |
| state reconstruction after system entry | Production coverage | Case 04/14 |

## 7. Persistence và storage

Room, DAO, transaction, relation, type converter, migration/schema evolution, DataStore, file/MediaStore/scoped storage, local source of truth và backup concern đều đã được cover từ Intermediate đến Senior. Case 03 đi sâu durable mutation queue, conflict, tombstone, pagination, migration và rollback compatibility. Case 12 bổ sung SAF, Photo Picker, MediaStore, MIME/content URI và sharing boundary. Case 13 bổ sung backup/restore và upgrade-path testing.

## 8. Networking

Networking được cover theo nhiều lớp: Retrofit/serialization ở Intermediate; timeout/error model/cancellation ở Deep Dive 02; retry/idempotency/cache/TLS/WebSocket/SSE ở Deep Dive 03; auth/session ở Case 02; offline sync ở Case 03; connectivity reality và slow-network behavior ở Case 12/13.

Điểm trọng tâm là tách transport error, HTTP protocol error và domain error; không để UI biết chi tiết transport; retry theo idempotency; không trust-all TLS; thiết kế lifecycle/reconnect cho connection lâu sống; và không nhầm “network available” với “backend request chắc chắn thành công”.

## 9. Dependency Injection

Constructor injection, Hilt/DI concept, scope/lifetime và large-scale DI đều đã được cover. Tài liệu không coi DI framework là architecture; DI chỉ quản lý dependency graph/lifetime, còn module boundary, process boundary và state ownership vẫn phải thiết kế riêng. Case 14 nhấn mạnh component có thể được system tạo trực tiếp nên dependency initialization không được phụ thuộc MainActivity chạy trước.

## 10. Background execution

WorkManager, foreground work/service, notification, exact alarm awareness, coroutine lifetime và Android background restriction được cover từ Intermediate tới Senior. Deep Dive 03 tập trung decision framework; Case 10 nối background policy với permission/foreground-service type; Case 14 phân biệt Service, Receiver và WorkManager theo lifetime/durability.

## 11. Testing

| Tầng test | Coverage |
|---|---|
| pure Kotlin/local JVM unit test | Beginner + Intermediate |
| fake/mock/test double | Deep Dive 02 |
| coroutine virtual-time test | Intermediate + Deep Dive 02 |
| Flow test | Deep Dive 02 |
| Robolectric | Deep Dive 03 |
| instrumented Android test | Beginner + Deep Dive 03 |
| Compose UI test | Deep Dive 03 + Case 11 |
| accessibility/manual semantics test | Case 11/13 |
| integration/contract strategy | Advanced + Case 05 |
| hardware/device integration test | Case 12 |
| upgrade/schema migration test | Case 03/13 |
| cold-start notification/widget/deep-link test | Case 14 |
| Macrobenchmark/performance test | Advanced/Master + Case 05 |
| OS/OEM/device matrix | Case 13 |

## 12. Performance

Main-thread/ANR/leak, Compose recomposition, R8, startup architecture, Baseline Profile, Macrobenchmark, Perfetto/measurement mindset, memory/battery/network và performance budget đều đã được cover. Case 09 đi sâu event loop, Binder, ART, heap/native memory, GC và thread contention. Case 11 cover hot draw/layout path. Case 13 mở rộng low-memory, thermal, battery và network quality.

## 13. Security và privacy

Security coverage hiện gồm secure configuration, WebView boundary, Android Keystore, TLS/Network Security Config, client trust model, authorization server-side, Play Integrity awareness, backup policy, Data Safety/privacy inventory, PendingIntent/exported-component boundary và supply-chain dependency risk.

Điểm quan trọng: APK/client không phải trusted environment; obfuscation không phải secret storage; biometric không thay authorization; attestation/integrity chỉ là risk signal; permission/data collection phải theo least privilege; external Intent/URI/Binder input không được coi là trusted chỉ vì chạy trên device.

## 14. Build, Gradle và release engineering

Gradle structure, build variants/flavors, APK/AAB, signing, R8, version matrix, K2/compiler plugin/generated code, modularization, convention plugin, configuration/build cache, dependency locking, reproducibility, staged rollout/rollback và artifact traceability đều đã được cover. Case 13 bổ sung promotion artifact, target-API cadence, device cohort monitoring và rollback compatibility.

Snapshot toolchain hiện tại của bộ note: Kotlin 2.4.20; Android Studio Quail 4 / 2026.1.4 Patch 1; AGP 9.4.1; Android 17 API 37; Compose BOM 2026.09.00.

## 15. Production governance

Master + Deep Dive 04 + Case 05/07/13 cover observability schema, correlation, performance budget, dependency governance/SBOM, ADR, code ownership, flaky-test policy, feature-flag lifecycle, target-SDK cadence, incident response, rollback compatibility và operating model dài hạn.

## 16. Kotlin Multiplatform

KMP được giữ ở Master thay vì đưa vào Beginner để tránh trộn Android foundations với cross-platform architecture. Coverage tập trung vào shared business logic, public API, `expect/actual`, platform boundary, threading/serialization và tiêu chí “share đúng thứ cần share” thay vì tối đa hóa phần trăm shared code.

## 17. Authentication, session và authorization

Case 02 cover Credential Manager, account/session state, access/refresh token, concurrent 401, single-flight refresh, logout, secure storage và phân biệt authentication với backend authorization. Case 10 nhấn mạnh OS permission không phải business entitlement.

## 18. Offline-first và data synchronization

Case 03 cover optimistic write, durable queue, idempotency key, retry/backoff, tombstone, conflict resolution, cursor, Paging/RemoteMediator và schema migration. Đây là coverage production đầy đủ hơn so với note API Room riêng lẻ.

## 19. Android runtime internals

Case 09 bổ sung lớp trước đây còn thiếu: process sandbox, `Application` lifetime, main-thread event loop, Looper/MessageQueue/Handler, Binder IPC, transaction payload, Parcelable boundary, ART/DEX, class loading/startup, managed/native memory, GC, leak, StrictMode, ANR, shared mutable state và runtime debugging bằng trace/heap evidence.

Mục tiêu không phải viết low-level Android thường xuyên, mà biết khi nào abstraction Coroutine/Compose/Room không đủ để giải thích behavior.

## 20. Permission, capability và target-SDK platform contract

Case 10 cover hardware capability vs permission; `<uses-feature>` và Play device availability; permission lifecycle/revocation; location foreground/background; Bluetooth/Nearby; Android 17 local-network protection; notification; camera/mic; Photo Picker/SAF; foreground service; exact alarm; exported component; App Links và target-SDK migration checklist.

Điểm trọng tâm là permission denial được coi như normal user choice và system-mediated picker được ưu tiên khi nó giảm broad access.

## 21. Device/media/hardware integration

Case 12 cover CameraX/use-case/backpressure/rotation; Media3/player/media session/audio focus; microphone; Storage Access Framework/Photo Picker/MediaStore/share; current vs continuous location; geofence; BLE GATT operation/reconnect/protocol; NFC/sensor; connectivity và WebView permission/JS bridge.

Các integration này được model như external stateful system có resource ownership, timeout, lifecycle và recovery thay vì một lời gọi API.

## 22. Accessibility, adaptive UI và advanced Compose

Case 11 bổ sung constraint/layout/draw pipeline, modifier order, custom layout/draw, lazy identity, effect lifetime, pointer/gesture/nested scroll, focus/IME, edge-to-edge/insets, animation, semantics/accessibility, font/RTL, keyboard/mouse và adaptive window/foldable strategy.

Accessibility được coi là correctness và public semantic contract của UI, không phải bước polish cuối.

## 23. Production device matrix và app quality

Case 13 cover risk-based OS/OEM/device matrix, fresh-install vs upgrade path, rollback compatibility, localization/plural/timezone/RTL, font scaling, TalkBack, battery/Doze, slow network, retry storm, low-memory/thermal, privacy inventory, telemetry schema, feature flag lifecycle, AAB/delivery, backup/restore và mobile incident readiness.

Feature được coi là production-ready khi recovery/compatibility/observability đã được cân nhắc, không chỉ khi screenshot đúng design.

## 24. System surfaces ngoài Activity

Case 14 cover started/bound/foreground Service, BroadcastReceiver + `goAsync`, ContentProvider/ContentResolver/URI grant, notification/channel/action, PendingIntent identity/mutability, App Widget, Shortcut, Quick Settings Tile, multi-process awareness, App Startup và exported component security.

Các system surface được thiết kế để hoạt động từ cold process và reconstruct state bằng stable identifier/source of truth thay vì mang giant in-memory object.

## 25. Các chủ đề cố ý không đào sâu thành framework-specific manual

Bộ note không cố trở thành reference manual cho mọi API của Firebase, từng DI framework, từng HTTP client, từng analytics SDK, Google Maps, từng ML stack hoặc từng vendor cloud. Những công cụ đó thay đổi nhanh. Tài liệu ưu tiên concept/contract/lifetime/failure model để khi gặp tool mới, người học có thể đặt nó vào mental model sẵn có.

## 26. Tiêu chí cho vòng update tiếp theo

Một phần mới chỉ nên được thêm khi ít nhất một trong các điều sau đúng: platform/language có behavior mới làm thay đổi mental model; một boundary quan trọng hiện chưa được giải thích; code legacy phổ biến nhưng người đọc chưa có cách nhận diện/migrate; production failure mode chưa có coverage; hoặc version/toolchain thay đổi làm ví dụ hiện tại sai.

Sau vòng platform completion này, các khoảng trống còn lại nên ưu tiên **chiều sâu của case cụ thể hoặc version migration thực tế**, không mở rộng chỉ để tăng số dòng. Nếu thêm chapter mới, cần chứng minh nó bổ sung một mental model/boundary chưa có.

Mục tiêu của bộ note là **đủ sâu nhưng có cấu trúc**, để người học biết khái niệm là gì, vì sao tồn tại, khi nào dùng, trade-off ra sao, nó thất bại như thế nào và cách đặt nó vào một production system hoàn chỉnh.
