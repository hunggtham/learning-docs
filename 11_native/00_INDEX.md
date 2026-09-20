# Native Mobile Development — Index

Thư mục `11_native` chứa các bộ tài liệu native mobile theo hệ sinh thái. Mỗi bộ được tổ chức theo lộ trình từ nền tảng đến production/master, đồng thời giữ các công nghệ legacy quan trọng để có thể đọc và maintain codebase thực tế.

## Swift & iOS

Bộ Swift/iOS được đặt riêng trong [`swift_ios/`](swift_ios/README.md), sử dụng baseline hiện hành **Xcode 27 + Swift 6.4 + iOS 27 SDK** và vẫn giữ phần migration/legacy để đọc codebase Swift 5.x, UIKit, Combine, Core Data và Objective-C interop.

1. [Beginner](swift_ios/01_swift_ios_beginner.md): Swift core từ số 0, Xcode, Foundation, SwiftUI/UIKit nhập môn, state/navigation, networking, persistence, SPM, file system, form/focus, animation/gesture, testing và signing.
2. [Intermediate](swift_ios/02_swift_ios_intermediate.md): generics/existentials, structured concurrency, actor/Sendable/AsyncSequence, data flow, networking layer, SwiftData/Core Data, architecture, background execution, module boundaries, sanitizers và deterministic testing.
3. [Advanced / Senior](swift_ios/03_swift_ios_advanced_senior.md): ownership, actor reentrancy, performance, modularization, Instruments, resilient networking, database concurrency, security, CI/CD, Objective-C/C/C++ interop, production design và incident mindset.
4. [Master](swift_ios/04_swift_ios_master.md): Swift 5→6.x migration, Swift 6.4, ABI/library evolution, macros, memory-safe systems APIs, offline sync, observability, App Extensions, StoreKit, CloudKit, release engineering và production-readiness audit.

## Kotlin & Android

Bộ Kotlin được đặt riêng trong [`kotlin_android/`](kotlin_android/README.md) để không trộn file Android với iOS.

1. [Beginner](kotlin_android/01_kotlin_beginner.md): Kotlin từ số 0, Android Studio/Gradle, OOP, null-safety, collection/lambda, Android components, Compose, XML/View, resource, permission và Activity Result API.
2. [Intermediate](kotlin_android/02_kotlin_intermediate.md): Kotlin idioms/generics, coroutine/Flow, ViewModel, repository, Room, network, DI, WorkManager, DataStore, serialization, storage, deep link và testing.
3. [Advanced / Senior](kotlin_android/03_kotlin_advanced_senior.md): coroutine/Flow internals, Compose runtime, modularization, offline-first, performance, R8, security, signing/release, API compatibility và production design.
4. [Master](kotlin_android/04_kotlin_master.md): Kotlin 1.x→2.x/K2, JVM/build internals, large-scale architecture, compatibility, reliability, observability, performance engineering, release/rollback và KMP awareness.

## Version baseline của Kotlin/Android

Tại lần cập nhật 2026-09-20, bộ Kotlin dùng Kotlin 2.4.20; Android Studio Quail 4 / 2026.1.4 Patch 1; Android Gradle Plugin 9.4.1. Android 17 tương ứng API 37. Với Google Play, app mới và app update Android thông thường từ 2026-08-31 phải target Android 16 / API 36 trở lên.
