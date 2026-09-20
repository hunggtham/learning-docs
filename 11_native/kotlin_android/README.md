# Kotlin + Android Master Notes

Bộ tài liệu học Kotlin cho Android theo lộ trình:

1. `01_kotlin_beginner.md` — nền tảng Kotlin, Android Studio, Gradle, Android components, Compose và XML/View.
2. `02_kotlin_intermediate.md` — idioms, generics, coroutine/Flow, ViewModel, architecture, Room, network, DI, WorkManager, DataStore và testing.
3. `03_kotlin_advanced_senior.md` — coroutine/Flow internals, Compose runtime, modularization, offline-first, performance, security, Java interop và production design.
4. `04_kotlin_master.md` — Kotlin 1.x→2.x, K2, bytecode awareness, large-scale architecture/build/release, KMP awareness, observability và master heuristics.

Bốn file chính là **learning spine**: chúng giữ thứ tự Beginner → Intermediate → Advanced/Senior → Master. Các phần bổ sung nằm trong `deep_dive/` để tăng chiều sâu mà không biến file chính thành tài liệu khổng lồ khó đọc.

## Deep dives theo từng level

- [`deep_dive/01_beginner_completion.md`](deep_dive/01_beginner_completion.md) — package/import, equality, range/array, collection transformation, nested/inner class, precondition, data-class identity, Context/Intent/Uri, Compose layout và testing căn bản.
- [`deep_dive/02_intermediate_completion.md`](deep_dive/02_intermediate_completion.md) — CoroutineContext/Job hierarchy, supervision, Flow cold/hot/context, `stateIn`/`shareIn`, `callbackFlow`, resource lifetime, network error model, Room source-of-truth, Compose effect/state, coroutine testing, DI scope và navigation contract.
- [`deep_dive/03_advanced_senior_completion.md`](deep_dive/03_advanced_senior_completion.md) — generic/type-erasure, cancellation safety, Flow backpressure, Compose Snapshot/CompositionLocal/identity, background execution, retry/idempotency/TLS, storage/backup, test layers, benchmark và static analysis.
- [`deep_dive/04_master_completion.md`](deep_dive/04_master_completion.md) — Gradle/build governance, dependency locking/SBOM, ABI/module contract, target-SDK migration, observability, performance budget, security/integrity, privacy, accessibility/adaptive UI, ADR/ownership, release/rollback, KMP và operating model.

- [`coverage_audit.md`](coverage_audit.md) — ma trận coverage và checklist dùng cho những vòng update tiếp theo.

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

Một vòng học hợp lý là:

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
→ architecture/release/security review
```

## Phạm vi đã cover

Bộ tài liệu không chỉ dạy syntax Kotlin. Nó nối Kotlin language với Android runtime, lifecycle, Compose lẫn XML/View, Gradle/AGP, coroutine/Flow, persistence/networking, DI, navigation, background work, testing, performance, security, build/release, legacy migration và production architecture.

Các gap thường bị tutorial bỏ qua đã được cover rõ hơn: process death, Activity Result API, Context lifetime, storage/URI, serialization boundary, coroutine cancellation, Flow backpressure, Compose Snapshot/identity/effect, retry/idempotency, R8/signing, API-level migration, foreground/background policy, database migration, backup/privacy, dependency governance, SBOM, observability, performance budget, rollout/rollback và long-term maintenance.
