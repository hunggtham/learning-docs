# Native Mobile Development — Index

Thư mục `11_native` chứa các bộ tài liệu native mobile theo hệ sinh thái. Mỗi bộ được tổ chức theo lộ trình từ nền tảng đến production/master, đồng thời giữ các công nghệ legacy quan trọng để có thể đọc và maintain codebase thực tế.

## Swift & iOS

1. [Beginner](01_swift_ios_beginner.md): Swift core, Xcode, SwiftUI/UIKit nhập môn, Foundation, networking, persistence, testing, signing.
2. [Intermediate](02_swift_ios_intermediate.md): type system sâu hơn, concurrency, data flow, networking layer, architecture, UIKit/SwiftUI interoperability, testing và Xcode workflow.
3. [Advanced / Senior](03_swift_ios_advanced_senior.md): isolation, actor reentrancy, performance, architecture production, security, CI/CD, Objective-C/C/C++ interop và senior idioms.
4. [Master Supplement](04_swift_ios_master_supplement.md): version/migration, library evolution, macros, systems features, SwiftUI identity, offline sync, observability và release engineering.

## Kotlin & Android

Bộ Kotlin được đặt riêng trong [`kotlin_android/`](kotlin_android/README.md) để không trộn file Android với iOS.

1. [Beginner](kotlin_android/01_kotlin_beginner.md): Kotlin từ số 0, Android Studio/Gradle, OOP, null-safety, collection/lambda, Android components, Compose, XML/View, resource, permission và Activity Result API.
2. [Intermediate](kotlin_android/02_kotlin_intermediate.md): Kotlin idioms/generics, coroutine/Flow, ViewModel, repository, Room, network, DI, WorkManager, DataStore, serialization, storage, deep link và testing.
3. [Advanced / Senior](kotlin_android/03_kotlin_advanced_senior.md): coroutine/Flow internals, Compose runtime, modularization, offline-first, performance, R8, security, signing/release, API compatibility và production design.
4. [Master](kotlin_android/04_kotlin_master.md): Kotlin 1.x→2.x/K2, JVM/build internals, large-scale architecture, compatibility, reliability, observability, performance engineering, release/rollback và KMP awareness.

## Version baseline của Kotlin/Android

Tại lần cập nhật 2026-09-20, bộ Kotlin dùng Kotlin 2.4.20; Android Studio Quail 4 / 2026.1.4 Patch 1; Android Gradle Plugin 9.4.1. Android 17 tương ứng API 37. Với Google Play, app mới và app update Android thông thường từ 2026-08-31 phải target Android 16 / API 36 trở lên.
