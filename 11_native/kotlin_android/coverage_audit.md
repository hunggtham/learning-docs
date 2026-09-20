# Kotlin + Android — Coverage Audit

Tài liệu này dùng để kiểm tra bộ note đã cover những lớp kiến thức nào và phần nào thuộc file chính hay deep-dive. Mục tiêu không phải tạo thêm một cheat sheet, mà là tránh hai lỗi thường gặp khi bộ tài liệu lớn dần: bổ sung trùng lặp và bỏ sót một boundary quan trọng.

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
| value class/K2/JVM bytecode/API design | Master coverage | `04_kotlin_master.md` |

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

## 3. Android runtime và component model

| Nhóm | Mức coverage | Nơi đọc chính |
|---|---|---|
| Activity/Service/BroadcastReceiver/ContentProvider | Nền tảng | Beginner |
| Context/Application/Activity lifetime | Bổ sung sâu | Deep Dive 01 |
| Intent/Bundle/Uri | Đầy đủ nền tảng | Beginner + Deep Dive 01 |
| lifecycle/configuration change | Đầy đủ | Beginner → Advanced |
| process death/SavedStateHandle | Đầy đủ | Intermediate + Advanced |
| runtime permission/Activity Result | Đầy đủ | Beginner |
| resource/qualifier/localization | Đầy đủ nền tảng | Beginner |
| API-level compatibility/behavior change | Senior/Master | Advanced + Master |

## 4. UI — Jetpack Compose

| Nhóm | Mức coverage | Nơi đọc chính |
|---|---|---|
| composable/layout/modifier | Đầy đủ nền tảng | Beginner + Deep Dive 01 |
| state/recomposition | Đầy đủ theo level | Beginner → Advanced |
| state hoisting | Đầy đủ | Deep Dive 02 |
| remember/rememberSaveable | Đầy đủ | Beginner + Intermediate |
| effect APIs | Đầy đủ | Intermediate + Deep Dive 02 |
| lazy list identity/key | Đầy đủ | Deep Dive 02/03 |
| Snapshot State | Senior coverage | Advanced + Deep Dive 03 |
| CompositionLocal | Senior coverage | Deep Dive 03 |
| composition/layout/draw phase | Senior coverage | Deep Dive 03 |
| performance/stability/recomposition measurement | Senior coverage | Advanced |
| design system/adaptive UI/accessibility | Master coverage | Master + Deep Dive 04 |

## 5. XML/View legacy interoperability

XML layout, View Binding, Fragment/View lifecycle và Compose/View interoperability được giữ trong Beginner/Intermediate để người học đọc được project cũ. Legacy API không được mô tả như “sai”; tài liệu phân biệt deprecated API, historical pattern và pattern vẫn hợp lệ trong codebase hiện hữu.

## 6. Architecture và state management

| Nhóm | Mức coverage | Nơi đọc chính |
|---|---|---|
| ViewModel/UI state/UDF | Đầy đủ | Intermediate |
| repository/data source | Đầy đủ | Intermediate |
| source of truth | Đầy đủ | Intermediate + Deep Dive 02 |
| offline-first/sync/conflict | Senior coverage | Advanced/Master |
| multi-module architecture | Senior coverage | Advanced/Master |
| dependency direction/API surface | Master coverage | Master + Deep Dive 04 |
| architecture decision/ADR/ownership | Master coverage | Deep Dive 04 |
| legacy migration/strangler approach | Đầy đủ | Advanced/Master |

## 7. Persistence và storage

Room, DAO, transaction, relation, type converter, migration/schema evolution, DataStore, file/MediaStore/scoped storage, local source of truth và backup concern đều đã được cover từ Intermediate đến Senior. Những phần cần đọc chung là `02_kotlin_intermediate.md`, Deep Dive 02, `03_kotlin_advanced_senior.md` và Deep Dive 03.

## 8. Networking

Networking được cover theo nhiều lớp: Retrofit/serialization ở Intermediate; timeout/error model/cancellation ở Deep Dive 02; retry/idempotency/cache/TLS/WebSocket/SSE ở Deep Dive 03; security/integrity/observability ở Master.

Điểm trọng tâm là tách transport error, HTTP protocol error và domain error; không để UI biết chi tiết transport; retry theo idempotency; không trust-all TLS; thiết kế lifecycle/reconnect cho connection lâu sống.

## 9. Dependency Injection

Constructor injection, Hilt/DI concept, scope/lifetime và large-scale DI đều đã được cover. Tài liệu không coi DI framework là architecture; DI chỉ quản lý dependency graph/lifetime, còn module boundary và state ownership vẫn phải thiết kế riêng.

## 10. Background execution

WorkManager, foreground work/service, notification, exact alarm awareness, coroutine lifetime và Android background restriction được cover từ Intermediate tới Senior. Deep Dive 03 tập trung vào decision framework: durable hay không, exact-time hay không, user-visible hay không, constraint gì và process death có được phép làm mất work hay không.

## 11. Testing

| Tầng test | Coverage |
|---|---|
| pure Kotlin/local JVM unit test | Beginner + Intermediate |
| fake/mock/test double | Deep Dive 02 |
| coroutine virtual-time test | Intermediate + Deep Dive 02 |
| Flow test | Deep Dive 02 |
| Robolectric | Deep Dive 03 |
| instrumented Android test | Beginner + Deep Dive 03 |
| Compose UI test | Deep Dive 03 |
| integration/contract strategy | Advanced |
| Macrobenchmark/performance test | Advanced/Master |

## 12. Performance

Main-thread/ANR/leak, Compose recomposition, R8, startup architecture, Baseline Profile, Macrobenchmark, Perfetto/measurement mindset, memory/battery/network và performance budget đều đã được cover. Master nhấn mạnh performance engineering phải bắt đầu bằng metric và measurement, không bằng micro-optimization theo cảm giác.

## 13. Security và privacy

Security coverage hiện gồm secure configuration, WebView boundary, Android Keystore, TLS/Network Security Config, client trust model, authorization server-side, Play Integrity awareness, backup policy, Data Safety/privacy inventory và supply-chain dependency risk.

Điểm quan trọng: APK/client không phải trusted environment; obfuscation không phải secret storage; biometric không thay authorization; attestation/integrity chỉ là risk signal; permission/data collection phải theo least privilege.

## 14. Build, Gradle và release engineering

Gradle structure, build variants/flavors, APK/AAB, signing, R8, version matrix, K2/compiler plugin/generated code, modularization, convention plugin, configuration/build cache, dependency locking, reproducibility, staged rollout/rollback và artifact traceability đều đã được cover.

Snapshot toolchain hiện tại của bộ note: Kotlin 2.4.20; Android Studio Quail 4 / 2026.1.4 Patch 1; AGP 9.4.1; Android 17 API 37; Compose BOM 2026.09.00.

## 15. Production governance

Master + Deep Dive 04 cover những phần thường không có trong tutorial: observability schema, correlation, performance budget, dependency governance/SBOM, ADR, code ownership, flaky-test policy, feature-flag lifecycle, target-SDK cadence, incident response, rollback compatibility và operating model dài hạn.

## 16. Kotlin Multiplatform

KMP được giữ ở Master thay vì đưa vào Beginner để tránh trộn Android foundations với cross-platform architecture. Coverage tập trung vào shared business logic, public API, `expect/actual`, platform boundary, threading/serialization và tiêu chí “share đúng thứ cần share” thay vì tối đa hóa phần trăm shared code.

## 17. Các chủ đề cố ý không đào sâu thành framework-specific manual

Bộ note không cố trở thành reference manual cho mọi API của Firebase, từng DI framework, từng HTTP client, từng analytics SDK hoặc từng vendor cloud. Những công cụ đó thay đổi nhanh. Tài liệu ưu tiên concept/contract/lifetime/failure model để khi gặp tool mới, người học có thể đặt nó vào mental model sẵn có.

## 18. Tiêu chí cho vòng update tiếp theo

Một phần mới chỉ nên được thêm khi ít nhất một trong các điều sau đúng: platform/language có behavior mới làm thay đổi mental model; một boundary quan trọng hiện chưa được giải thích; code legacy phổ biến nhưng người đọc chưa có cách nhận diện/migrate; production failure mode chưa có coverage; hoặc version/toolchain thay đổi làm ví dụ hiện tại sai.

Không mở rộng chỉ để tăng số dòng. Mục tiêu của bộ note là **đủ sâu nhưng có cấu trúc**, để người học biết vì sao, khi nào và trade-off của từng khái niệm.
