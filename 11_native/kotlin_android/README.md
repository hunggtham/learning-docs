# Kotlin + Android Master Notes

Bộ tài liệu học Kotlin cho Android theo lộ trình:

1. `01_kotlin_beginner.md` — nền tảng Kotlin, Android Studio, Gradle, Android components, Compose và XML/View.
2. `02_kotlin_intermediate.md` — idioms, generics, coroutine/Flow, ViewModel, architecture, Room, network, DI, WorkManager, DataStore và testing.
3. `03_kotlin_advanced_senior.md` — coroutine/Flow internals, Compose runtime, modularization, offline-first, performance, security, Java interop và production design.
4. `04_kotlin_master.md` — Kotlin 1.x→2.x, K2, bytecode awareness, large-scale architecture/build/release, KMP awareness, observability và master heuristics.

Bốn file chính là **learning spine**: chúng giữ thứ tự Beginner → Intermediate → Advanced/Senior → Master. Các phần bổ sung nằm trong `deep_dive/` để tăng chiều sâu mà không biến file chính thành tài liệu khổng lồ khó đọc. Sau khi đã hiểu từng concept riêng lẻ, `production_casebook/` nối chúng thành các hệ thống end-to-end để người học thấy state, lifecycle, data, network, security, testing và release tương tác với nhau trong production như thế nào.

## Deep dives theo từng level

- [`deep_dive/01_beginner_completion.md`](deep_dive/01_beginner_completion.md) — package/import, equality, range/array, collection transformation, nested/inner class, precondition, data-class identity, Context/Intent/Uri, Compose layout và testing căn bản.
- [`deep_dive/02_intermediate_completion.md`](deep_dive/02_intermediate_completion.md) — CoroutineContext/Job hierarchy, supervision, Flow cold/hot/context, `stateIn`/`shareIn`, `callbackFlow`, resource lifetime, network error model, Room source-of-truth, Compose effect/state, coroutine testing, DI scope và navigation contract.
- [`deep_dive/03_advanced_senior_completion.md`](deep_dive/03_advanced_senior_completion.md) — generic/type-erasure, cancellation safety, Flow backpressure, Compose Snapshot/CompositionLocal/identity, background execution, retry/idempotency/TLS, storage/backup, test layers, benchmark và static analysis.
- [`deep_dive/04_master_completion.md`](deep_dive/04_master_completion.md) — Gradle/build governance, dependency locking/SBOM, ABI/module contract, target-SDK migration, observability, performance budget, security/integrity, privacy, accessibility/adaptive UI, ADR/ownership, release/rollback, KMP và operating model.

[`coverage_audit.md`](coverage_audit.md) là ma trận coverage và checklist dùng cho những vòng update tiếp theo.

## Production Casebook — nối kiến thức thành hệ thống thực tế

Sau level Master, đọc [`production_casebook/README.md`](production_casebook/README.md) và các case theo thứ tự. Casebook không lặp lại syntax/API đã giải thích mà tập trung vào boundary, failure mode và trade-off của một app production.

1. [`production_casebook/01_architecture_end_to_end.md`](production_casebook/01_architecture_end_to_end.md) — requirement → UiState/UDF → ViewModel → repository → Room/network source of truth → DI/module boundary.
2. [`production_casebook/02_auth_session_network_security.md`](production_casebook/02_auth_session_network_security.md) — Credential Manager, authentication vs authorization, session, access/refresh token, single-flight refresh, logout, secure storage và network security.
3. [`production_casebook/03_offline_first_sync_and_database.md`](production_casebook/03_offline_first_sync_and_database.md) — optimistic write, durable mutation queue, idempotency, WorkManager sync, conflict, tombstone, cursor, Paging/RemoteMediator, Room migration và rollback compatibility.
4. [`production_casebook/04_navigation_lifecycle_process_death.md`](production_casebook/04_navigation_lifecycle_process_death.md) — type-safe Navigation Compose, deep/App Link, notification navigation, lifecycle, SavedStateHandle, adaptive layout và process recreation.
5. [`production_casebook/05_testing_performance_release.md`](production_casebook/05_testing_performance_release.md) — test strategy, coroutine/Flow/Room/network/Compose test, static analysis, Macrobenchmark, Baseline Profile, Perfetto, R8, signing, CI/CD, staged rollout và rollback.
6. [`production_casebook/06_legacy_migration_and_modularization.md`](production_casebook/06_legacy_migration_and_modularization.md) — Java/XML/Fragment/callback/LiveData/Rx/SharedPreferences/SQLite legacy migration, interoperability, strangler pattern, feature flag và modularization.
7. [`production_casebook/07_reference_app_blueprint.md`](production_casebook/07_reference_app_blueprint.md) — blueprint ghép module graph, source of truth, session, sync, navigation, test, observability, security và release thành một project production thống nhất.
8. [`production_casebook/08_kotlin_jvm_compiler_runtime.md`](production_casebook/08_kotlin_jvm_compiler_runtime.md) — Kotlin/JVM/K2 internals: suspend state machine, inline/reified, type erasure, boxing/value class, lambda capture, annotation target, Java interop, KSP/KAPT/compiler plugin, R8 và binary compatibility.

## Baseline version

- Kotlin: **2.4.20** stable (2026-09-07).
- Android Studio: **Quail 4 / 2026.1.4 Patch 1** stable.
- Android Gradle Plugin baseline: **9.4.1** với Quail 4 Patch 1.
- Compose stable BOM snapshot: **2026.09.00**.
- Android platform reference: **Android 17 = API 37**.
- Google Play target requirement từ 2026-08-31: app/update Android thông thường phải target **Android 16 / API 36+**, với ngoại lệ riêng cho một số form factor.
- UI direction: Jetpack Compose cho code hiện đại; XML/View system và API legacy quan trọng vẫn được cover để đọc, maintain và migrate project cũ.

Version ở đây là snapshot để đọc project tại thời điểm biên soạn, không phải con số phải copy cứng mãi mãi. Khi upgrade cần đọc compatibility matrix và release notes của Kotlin, Android Studio/AGP, Android platform và từng Jetpack library.

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
→ deep_dive/04
→ Production Casebook 01 → 08
→ tự thiết kế một production blueprint và giải thích các trade-off
```

Khi học Casebook, không nên chỉ copy code. Với mỗi case hãy tự trả lời: state owner là ai; source of truth ở đâu; failure nào retry được; process death phục hồi thế nào; dữ liệu nào nhạy cảm; operation nào cần idempotency; test nào chứng minh invariant; release gặp lỗi thì rollback hoặc disable bằng cách nào. Khi gặp issue “magic” ở Kotlin/Gradle/runtime, dùng Case 08 để hạ xuống tầng compiler/JVM/R8 thay vì đoán.

## Phạm vi đã cover

Bộ tài liệu không chỉ dạy syntax Kotlin. Nó nối Kotlin language với Android runtime, lifecycle, Compose lẫn XML/View, Gradle/AGP, coroutine/Flow, persistence/networking, DI, navigation, background work, testing, performance, security, build/release, legacy migration và production architecture.

Các gap thường bị tutorial bỏ qua đã được cover rõ hơn: process death, Activity Result API, Context lifetime, storage/URI, serialization boundary, coroutine cancellation, Flow backpressure, Compose Snapshot/identity/effect, retry/idempotency, token refresh race, R8/signing, API-level migration, foreground/background policy, database migration, offline mutation queue, conflict resolution, backup/privacy, dependency governance, SBOM, observability, performance budget, staged rollout/rollback, Kotlin/JVM abstraction leak và long-term maintenance.

Mục tiêu cuối cùng của bộ note không phải để người đọc nhớ mọi API, mà để khi gặp một requirement mới có thể tự suy luận theo các trục **lifetime → ownership → source of truth → concurrency → failure → compatibility → security → observability → release**, và khi cần có thể hạ xuống tầng compiler/runtime để giải thích behavior thay vì dựa vào “magic”.
