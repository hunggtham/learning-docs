# Kotlin + Android Master Notes

Bộ tài liệu học Kotlin cho Android theo lộ trình:

1. `01_kotlin_beginner.md` — nền tảng Kotlin, Android Studio, Gradle, Android components, Compose và XML/View.
2. `02_kotlin_intermediate.md` — idioms, generics, coroutine/Flow, ViewModel, architecture, Room, network, DI, WorkManager, DataStore và testing.
3. `03_kotlin_advanced_senior.md` — coroutine/Flow internals, Compose runtime, modularization, offline-first, performance, security, Java interop và production design.
4. `04_kotlin_master.md` — Kotlin 1.x→2.x, K2, bytecode awareness, large-scale architecture/build/release, KMP awareness, observability và master heuristics.
5. [`05_kotlin_android_version_evolution.md`](05_kotlin_android_version_evolution.md) — bản đồ version Kotlin/Android từ Kotlin 1.x → 2.4, K1 → K2, Compose compiler cũ/mới, legacy → modern API, compatibility matrix và upgrade strategy.

Bốn file đầu là **learning spine theo level**: chúng giữ thứ tự Beginner → Intermediate → Advanced/Senior → Master. File `05_kotlin_android_version_evolution.md` là **version map xuyên suốt**, dùng để hiểu codebase thuộc thế hệ nào, vì sao API/build setup thay đổi theo thời gian và cách migrate giữa các thế hệ. Các phần bổ sung nằm trong `deep_dive/` để tăng chiều sâu mà không biến file chính thành tài liệu khổng lồ khó đọc. Sau khi đã hiểu từng concept riêng lẻ, `production_casebook/` nối chúng thành các hệ thống end-to-end và hạ xuống cả Android platform/runtime/build/distribution để người học thấy state, lifecycle, data, network, security, UI system, hardware capability, process, compiler, native layer và artifact release tương tác với nhau trong production như thế nào.

## Version evolution — đọc project cũ và hiểu toolchain hiện đại

[`05_kotlin_android_version_evolution.md`](05_kotlin_android_version_evolution.md) nên được dùng khi cần trả lời các câu hỏi như:

- project Kotlin 1.3/1.5/1.9 khác project Kotlin 2.x ở đâu;
- K1 và K2 compiler khác nhau về thế hệ như thế nào;
- khi nào JVM IR trở thành mặc định;
- `sealed interface`, value class, `data object`, enum `entries`, context parameters và explicit backing fields xuất hiện/stable ở version nào;
- vì sao Compose compiler trước Kotlin 2.0 cần compatibility mapping nhưng Kotlin 2.0+ dùng plugin cùng Kotlin version;
- khác biệt giữa Kotlin version, `languageVersion`, `apiVersion`, `jvmTarget`, JDK toolchain, KGP, AGP và Gradle;
- khác biệt giữa `minSdk`, `compileSdk`, `targetSdk` và Android OS thực tế;
- cách nhận diện code legacy như synthetic view, `AsyncTask`, LiveData/Rx-heavy, `kotlinOptions {}`, kapt-heavy và cách map sang modern stack mà không rewrite máy móc;
- cách upgrade Kotlin/toolchain theo compatibility matrix, full-variant build, generated-code test và release validation.

Đây là file nên đọc song song với `production_casebook/18_android_compatibility_api_levels_sdk_extensions.md` và `depth_labs/06_build_compatibility_startup_release_forensics.md` khi làm migration thực tế.

## Deep dives theo từng level

- [`deep_dive/01_beginner_completion.md`](deep_dive/01_beginner_completion.md) — package/import, equality, range/array, collection transformation, nested/inner class, precondition, data-class identity, Context/Intent/Uri, Compose layout và testing căn bản.
- [`deep_dive/02_intermediate_completion.md`](deep_dive/02_intermediate_completion.md) — CoroutineContext/Job hierarchy, supervision, Flow cold/hot/context, `stateIn`/`shareIn`, `callbackFlow`, resource lifetime, network error model, Room source-of-truth, Compose effect/state, coroutine testing, DI scope và navigation contract.
- [`deep_dive/03_advanced_senior_completion.md`](deep_dive/03_advanced_senior_completion.md) — generic/type-erasure, cancellation safety, Flow backpressure, Compose Snapshot/CompositionLocal/identity, background execution, retry/idempotency/TLS, storage/backup, test layers, benchmark và static analysis.
- [`deep_dive/04_master_completion.md`](deep_dive/04_master_completion.md) — Gradle/build governance, dependency locking/SBOM, ABI/module contract, target-SDK migration, observability, performance budget, security/integrity, privacy, accessibility/adaptive UI, ADR/ownership, release/rollback, KMP và operating model.

[`coverage_audit.md`](coverage_audit.md) là ma trận coverage và checklist dùng cho những vòng update tiếp theo.

## Depth Labs — tăng độ sâu reasoning

Sau khi đã đọc các file chính và casebook tương ứng, dùng [`depth_labs/README.md`](depth_labs/README.md) để đào sâu correctness ở những boundary khó nhất. Depth Labs không mở thêm domain mới; chúng đi sâu vào invariant, race condition, transaction semantics, cancellation, stale state, consistency, effect lifetime, performance evidence, failure injection, compatibility, artifact forensics và API/ABI evolution.

Các lab hiện có:

1. [`depth_labs/01_architecture_invariants_boundary_reasoning.md`](depth_labs/01_architecture_invariants_boundary_reasoning.md) — architecture invariant, state ownership, stale snapshot, transaction boundary và ambiguous outcome.
2. [`depth_labs/02_offline_sync_consistency_race_conditions.md`](depth_labs/02_offline_sync_consistency_race_conditions.md) — sync correctness, outbox, idempotency, ordering, conflict, cursor, account isolation và failure injection.
3. [`depth_labs/03_coroutine_flow_concurrency_failure_semantics.md`](depth_labs/03_coroutine_flow_concurrency_failure_semantics.md) — Job tree, cancellation, supervision, backpressure, stream lifetime và concurrency race.
4. [`depth_labs/04_compose_runtime_state_performance_semantics.md`](depth_labs/04_compose_runtime_state_performance_semantics.md) — Snapshot state, identity, effect lifetime, phase invalidation, semantics và performance reasoning.
5. [`depth_labs/05_testing_reliability_observability_failure_injection.md`](depth_labs/05_testing_reliability_observability_failure_injection.md) — invariant-based testing, migration/rollback, race test, Macrobenchmark, telemetry, SLI/SLO và rollout guardrail.
6. [`depth_labs/06_build_compatibility_startup_release_forensics.md`](depth_labs/06_build_compatibility_startup_release_forensics.md) — Gradle/variant/R8, API compatibility, startup critical path và release artifact forensics.
7. [`depth_labs/07_sdk_native_boundary_api_evolution_consumer_safety.md`](depth_labs/07_sdk_native_boundary_api_evolution_consumer_safety.md) — public API/ABI, SDK consumer safety, JNI/native ownership, compatibility và publishing evolution.

## Production Casebook — nối kiến thức thành hệ thống thực tế

Sau level Master, đọc [`production_casebook/README.md`](production_casebook/README.md) và các case theo thứ tự. Casebook không lặp lại syntax/API đã giải thích mà tập trung vào boundary, failure mode, system contract và trade-off của một app production.

1. [`production_casebook/01_architecture_end_to_end.md`](production_casebook/01_architecture_end_to_end.md) — requirement → UiState/UDF → ViewModel → repository → Room/network source of truth → DI/module boundary.
2. [`production_casebook/02_auth_session_network_security.md`](production_casebook/02_auth_session_network_security.md) — Credential Manager, authentication vs authorization, session, access/refresh token, single-flight refresh, logout, secure storage và network security.
3. [`production_casebook/03_offline_first_sync_and_database.md`](production_casebook/03_offline_first_sync_and_database.md) — optimistic write, durable mutation queue, idempotency, WorkManager sync, conflict, tombstone, cursor, Paging/RemoteMediator, Room migration và rollback compatibility.
4. [`production_casebook/04_navigation_lifecycle_process_death.md`](production_casebook/04_navigation_lifecycle_process_death.md) — type-safe Navigation Compose, deep/App Link, notification navigation, lifecycle, SavedStateHandle, adaptive layout và process recreation.
5. [`production_casebook/05_testing_performance_release.md`](production_casebook/05_testing_performance_release.md) — test strategy, coroutine/Flow/Room/network/Compose test, static analysis, Macrobenchmark, Baseline Profile, Perfetto, R8, signing, CI/CD, staged rollout và rollback.
6. [`production_casebook/06_legacy_migration_and_modularization.md`](production_casebook/06_legacy_migration_and_modularization.md) — Java/XML/Fragment/callback/LiveData/Rx/SharedPreferences/SQLite legacy migration, interoperability, strangler pattern, feature flag và modularization.
7. [`production_casebook/07_reference_app_blueprint.md`](production_casebook/07_reference_app_blueprint.md) — blueprint ghép module graph, source of truth, session, sync, navigation, test, observability, security và release thành một project production thống nhất.
8. [`production_casebook/08_kotlin_jvm_compiler_runtime.md`](production_casebook/08_kotlin_jvm_compiler_runtime.md) — Kotlin/JVM/K2 internals: suspend state machine, inline/reified, type erasure, boxing/value class, lambda capture, annotation target, Java interop, KSP/KAPT/compiler plugin, R8 và binary compatibility.
9. [`production_casebook/09_android_runtime_process_thread_binder.md`](production_casebook/09_android_runtime_process_thread_binder.md) — Linux process/app sandbox, main thread event loop, Looper/MessageQueue/Handler, Binder IPC, ART, DEX, memory/GC, ANR, process death và thread safety.
10. [`production_casebook/10_permissions_capabilities_system_contracts.md`](production_casebook/10_permissions_capabilities_system_contracts.md) — hardware capability, runtime permission, location, Bluetooth, Android 17 local-network permission, notification, storage picker, foreground service, exported component và target-SDK migration.
11. [`production_casebook/11_compose_ui_graphics_input_accessibility.md`](production_casebook/11_compose_ui_graphics_input_accessibility.md) — Compose composition/layout/draw phases, constraint/modifier, custom layout/draw, gesture/focus/IME, animation, semantics, accessibility, edge-to-edge và adaptive UI.
12. [`production_casebook/12_media_camera_location_bluetooth_files.md`](production_casebook/12_media_camera_location_bluetooth_files.md) — CameraX, Media3/media session, audio focus, microphone, SAF/Photo Picker/MediaStore, location/geofence, BLE/GATT, NFC/sensor, WebView và device-resource ownership.
13. [`production_casebook/13_production_quality_device_matrix.md`](production_casebook/13_production_quality_device_matrix.md) — device/OS/OEM matrix, upgrade/rollback testing, localization/timezone/RTL/font scale, battery/network/thermal, privacy, observability, feature flag và release readiness.
14. [`production_casebook/14_system_surfaces_services_receivers_widgets.md`](production_casebook/14_system_surfaces_services_receivers_widgets.md) — Service, BroadcastReceiver, ContentProvider, notification/PendingIntent, App Widget, shortcut, Quick Settings Tile, cold-start entry point và exported-component security.
15. [`production_casebook/15_gradle_agp_build_system_variants.md`](production_casebook/15_gradle_agp_build_system_variants.md) — Gradle/AGP/Kotlin plugin, build type/flavor/variant, source-set precedence, manifest/resource merge, dependency visibility, convention plugin, configuration/build cache, D8/R8, signing và CI build governance.
16. [`production_casebook/16_aab_play_delivery_distribution.md`](production_casebook/16_aab_play_delivery_distribution.md) — AAB, split APK, `bundletool`, dynamic feature/Play Feature Delivery, app size, signing, rollout/rollback, distribution channel và artifact provenance.
17. [`production_casebook/17_ndk_jni_abi_native_memory.md`](production_casebook/17_ndk_jni_abi_native_memory.md) — NDK/JNI, ABI, native `.so`, CMake, reference/thread ownership, native memory, symbolication/sanitizer, 16 KB page size và native release validation.
18. [`production_casebook/18_android_compatibility_api_levels_sdk_extensions.md`](production_casebook/18_android_compatibility_api_levels_sdk_extensions.md) — `minSdk`/`compileSdk`/`targetSdk`, all-app vs target-gated behavior changes, compatibility framework, API guard, desugaring, SDK Extensions, non-SDK restrictions và platform migration playbook.
19. [`production_casebook/19_app_startup_initialization_cold_start.md`](production_casebook/19_app_startup_initialization_cold_start.md) — cold/warm/hot start, Application/provider initialization, lazy/eager work, SplashScreen, App Startup, Compose first frame, Baseline Profile, Macrobenchmark, Perfetto và startup budget.
20. [`production_casebook/20_android_library_sdk_authoring.md`](production_casebook/20_android_library_sdk_authoring.md) — AAR/library/SDK authoring, public API/ABI, Java/Kotlin interop, resource/manifest contract, consumer R8 rules, lint, publishing, SemVer và migration compatibility.

## Baseline version

- Kotlin: **2.4.20** stable (2026-09-07).
- Android Studio: **Quail 4 / 2026.1.4 Patch 1** stable.
- Android Gradle Plugin baseline: **9.4.1** với Quail 4 Patch 1.
- Compose stable BOM snapshot: **2026.09.00**.
- Android platform reference: **Android 17 = API 37**.
- Google Play target requirement từ 2026-08-31: app/update Android thông thường phải target **Android 16 / API 36+**, với ngoại lệ riêng cho một số form factor.
- UI direction: Jetpack Compose cho code hiện đại; XML/View system và API legacy quan trọng vẫn được cover để đọc, maintain và migrate project cũ.

Version ở đây là snapshot để đọc project tại thời điểm biên soạn, không phải con số phải copy cứng mãi mãi. Khi upgrade cần đọc compatibility matrix và release notes của Kotlin, Android Studio/AGP, Android platform, Google Play policy và từng Jetpack/library dependency. Timeline và migration reasoning chi tiết nằm trong [`05_kotlin_android_version_evolution.md`](05_kotlin_android_version_evolution.md).

## Cách học

Nên đọc theo thứ tự. Không chuyển level chỉ vì đã “đọc hết”; hãy tự viết lại ví dụ, làm mini app và tự giải thích các khái niệm bằng lời của mình. Sau mỗi file chính, đọc deep-dive cùng level trước khi chuyển sang level kế tiếp nếu mục tiêu là hiểu sâu thay vì chỉ làm tutorial.

Một vòng học hoàn chỉnh là:

```text
01 Beginner
→ deep_dive/01
→ mini app nhỏ
→ 02 Intermediate
→ deep_dive/02
→ app có ViewModel + Flow + Room + network
→ 03 Advanced/Senior
→ deep_dive/03
→ profiling/testing/migration exercise
→ 04 Master
→ 05 Version Evolution: Kotlin 1.x → 2.x + Android/toolchain version map
→ deep_dive/04
→ Production Casebook 01 → 08: architecture + compiler/runtime
→ Production Casebook 09 → 14: Android platform + device/system integration
→ Production Casebook 15 → 20: build + distribution + native + compatibility + startup + SDK authoring
→ Depth Labs 01 → 07: invariant + race + failure + compatibility reasoning
→ tự thiết kế, build, package, release và giải thích trade-off của một production app
```

Khi học Casebook và Depth Labs, không nên chỉ copy code. Với mỗi case hãy tự trả lời: state owner là ai; source of truth ở đâu; process/thread/lifecycle nào đang chạy; invariant nào bắt buộc luôn đúng; failure nào retry được; result nào có thể stale; operation nào có ambiguous outcome; permission/capability nào có thể biến mất; artifact nào thật sự tới device; native/resource/build boundary nào có thể leak; dữ liệu nào nhạy cảm; operation nào cần idempotency; test nào chứng minh invariant; release gặp lỗi thì rollback hoặc disable bằng cách nào. Khi gặp issue “magic” ở Kotlin/Gradle/runtime, dùng Case 08–09, 15–18, file Version Evolution và Depth Labs để hạ xuống tầng compiler/JVM/ART/Binder/build/artifact/platform contract thay vì đoán.

## Phạm vi đã cover

Bộ tài liệu không chỉ dạy syntax Kotlin. Nó nối Kotlin language với Android runtime, lifecycle, Compose lẫn XML/View, Gradle/AGP, coroutine/Flow, persistence/networking, DI, navigation, background work, testing, performance, security, build/release, AAB/delivery, native NDK/JNI, platform compatibility, startup, library authoring, legacy migration, system components, hardware capability và production architecture.

Các gap thường bị tutorial bỏ qua đã được cover rõ hơn: process death, Activity Result API, Context lifetime, storage/URI, serialization boundary, coroutine cancellation, Flow backpressure, Compose Snapshot/identity/effect, retry/idempotency, token refresh race, R8/signing, source-set/manifest merge, API-level migration, foreground/background policy, database migration, offline mutation queue, conflict resolution, backup/privacy, dependency governance, SBOM, observability, performance budget, staged rollout/rollback, Kotlin/JVM abstraction leak, Android process/Binder/MessageQueue, permission/capability migration, adaptive/accessibility UI, camera/media/BLE integration, cold-start system surface, split delivery, ABI/page-size compatibility, startup critical path, SDK binary compatibility, architecture invariant, stale-state race, ambiguous network outcome, sync consistency, deterministic failure injection, Kotlin version evolution, legacy/modern API mapping và long-term maintenance.

Mục tiêu cuối cùng của bộ note không phải để người đọc nhớ mọi API, mà để khi gặp một requirement mới có thể tự suy luận theo các trục **invariant → lifetime → ownership → source of truth → execution context → capability → build variant → artifact → concurrency → ordering → failure → compatibility → security → observability → distribution/release**, và khi cần có thể hạ xuống tầng compiler/runtime/platform/native/build system để giải thích behavior thay vì dựa vào “magic”.
