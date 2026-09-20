# Kotlin + Android Master Notes

Bộ tài liệu học Kotlin cho Android theo lộ trình:

1. `01_kotlin_beginner.md` — nền tảng Kotlin, Android Studio, Gradle, Android components, Compose và XML/View.
2. `02_kotlin_intermediate.md` — idioms, generics, coroutine/Flow, ViewModel, architecture, Room, network, DI, WorkManager, DataStore và testing.
3. `03_kotlin_advanced_senior.md` — coroutine/Flow internals, Compose runtime, modularization, offline-first, performance, security, Java interop và production design.
4. `04_kotlin_master.md` — Kotlin 1.x→2.x, K2, bytecode awareness, large-scale architecture/build/release, KMP awareness, observability và master heuristics.

## Baseline version

- Kotlin: 2.4.x; current baseline used here: 2.4.20 (2026-09-07).
- Android Studio: Quail 4 / 2026.1.4 Patch 1 stable.
- Android Gradle Plugin baseline: 9.4.1 with Quail 4 Patch 1.
- Android platform reference: Android 17 = API 37; Google Play target requirement from 2026-08-31 is API 36+ for ordinary new apps/updates.
- UI direction: Jetpack Compose for modern development, while XML/View system and important legacy APIs are still covered for maintenance/migration.

## Cách học

Nên đọc theo thứ tự. Không chuyển level chỉ vì đã “đọc hết”; hãy tự viết lại ví dụ, làm mini app và tự giải thích các khái niệm bằng lời của mình. Các file sau giả định bạn đã hiểu file trước, nhưng vẫn giải thích lại các boundary quan trọng khi cần.

## Phạm vi đã cover

Bộ tài liệu không chỉ dạy syntax Kotlin. Nó nối Kotlin language với Android runtime, lifecycle, Compose lẫn XML/View, Gradle/AGP, coroutine/Flow, persistence/networking, DI, navigation, background work, testing, performance, security, build/release, legacy migration và production architecture. Các chương cuối của mỗi level được dùng để lấp những khoảng trống thường bị tutorial cơ bản bỏ qua như process death, Activity Result API, storage/URI, serialization boundary, R8, signing, API-level migration và reliability engineering.
