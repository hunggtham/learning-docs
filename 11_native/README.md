# Phát triển Di động Bản địa (Native Mobile Engineering — Swift/iOS & Kotlin/Android Master Hub)

Chào mừng bạn đến với **Cổng tri thức Kỹ thuật Di động Bản địa** (`11_native/`). Đây là không gian học tập và tra cứu chuẩn mực, bao phủ toàn diện hai hệ điều hành di động lớn nhất thế giới: **Apple iOS** (ngôn ngữ Swift) và **Google Android** (ngôn ngữ Kotlin).

Thư mục được xây dựng từ nền tảng ngôn ngữ cốt lõi, vòng đời ứng dụng (Lifecycle), quản lý bộ nhớ (Memory Management), luồng giao diện người dùng khai báo hiện đại (SwiftUI & Jetpack Compose), xử lý bất đồng bộ đa luồng (Concurrency & Coroutines), lưu trữ ngoại tuyến (Offline Persistence), đến kỹ thuật tối ưu hóa hiệu năng và đóng gói phát hành ứng dụng quy mô lớn trên App Store và Google Play.

---

## 1. Triết lý Kỹ thuật Bản địa & Ma trận So sánh Hai Hệ điều hành

Kỹ thuật lập trình di động bản địa (Native Mobile Development) là chìa khóa để đạt được hiệu năng tối đa (60-120 FPS mượt mà), thời gian phản hồi tức thì và khả năng khai thác triệt để năng lực phần cứng thiết bị:

| Trục kiến trúc | Hệ sinh thái Apple (iOS / iPadOS) | Hệ sinh thái Google (Android) |
| :--- | :--- | :--- |
| **Ngôn ngữ chuẩn** | **Swift 6** (Swift 6.4 baseline) | **Kotlin 2.x** (K2 Compiler baseline) |
| **Giao diện khai báo** | **SwiftUI** (kết hợp tương thích UIKit) | **Jetpack Compose** (kết hợp tương thích View/XML) |
| **Cơ chế quản lý bộ nhớ** | **ARC** (Automatic Reference Counting: Strong/Weak/Unowned) | **ART GC** (Android Runtime Generational Garbage Collector) |
| **Mô hình Bất đồng bộ** | **Structured Concurrency** (`async`/`await`, `TaskGroup`, `actor`) | **Coroutines & Flow** (`suspend`, `CoroutineScope`, `StateFlow`) |
| **Lưu trữ CSDL cục bộ** | **SwiftData** / **Core Data** / SQLite trực tiếp | **Room Database** / SQLite / DataStore |
| **Cung cấp phụ thuộc** | Environment Values / Swift Dependencies / Constructor Injection | **Hilt** / Dagger 2 / Koin |
| **Công cụ Build & Gói** | **Xcode Build System** + Swift Package Manager (SPM) | **Gradle (Kotlin DSL)** + Android Gradle Plugin (AGP) |
| **Định dạng phát hành** | `.ipa` (App Store Connect / TestFlight) | `.aab` (Android App Bundle - Google Play Console) |

---

## 2. Bản đồ Lộ trình Swift & iOS (Apple Ecosystem)

Toàn bộ giáo trình iOS được đặt tại thư mục chuyên biệt [`swift_ios/`](swift_ios/README.md), bao gồm 4 cấp độ kỹ thuật và tài liệu tham chiếu vận hành:

- **[Lộ trình Nhập môn (Beginner)](swift_ios/01_swift_ios_beginner.md):**
  - Cú pháp Swift từ số 0: Khai báo biến (`let`/`var`), kiểu dữ liệu cơ bản, Optionals (`?`/`!`, `if let`, `guard let`), Enums, Structs và Classes.
  - Môi trường Xcode, cấu trúc thư mục dự án iOS, hệ thống Foundation, Assets Catalog.
  - SwiftUI cơ bản: View modifiers, `@State`, `@Binding`, Stacks (`VStack`, `HStack`, `ZStack`), `List`, `NavigationView`.
  - Mạng cơ bản với `URLSession`, mã hóa/giải mã JSON với `Codable`.
  - Quản lý gói thư viện với Swift Package Manager (SPM).
- **[Lộ trình Trung cấp (Intermediate)](swift_ios/02_swift_ios_intermediate.md):**
  - Generics, Protocols, Existentials (`any` vs `some`).
  - Structured Concurrency trong Swift 5.5+: `async`/`await`, `Task`, `TaskGroup`, chia sẻ dữ liệu an toàn với `actor` và giao thức `Sendable`.
  - Kiến trúc ứng dụng: MVVM, Clean Architecture, The Composable Architecture (TCA).
  - Quản trị dữ liệu với SwiftData và Core Data: Entity, Relationship, FetchRequest, Migration.
  - Xử lý tác vụ nền (Background Tasks, Push Notifications với APNs).
- **[Lộ trình Nâng cao & Senior (Advanced / Senior)](swift_ios/03_swift_ios_advanced_senior.md):**
  - Quyền sở hữu bộ nhớ trong Swift hiện đại (`consume`, `borrowing`, `copying`).
  - Phân tích và phòng chống Actor reentrancy race conditions.
  - Đo lường và tối ưu hóa hiệu năng bằng Xcode Instruments: Time Profiler, Allocations, Leaks, Energy Log.
  - Kỹ thuật giao tiếp đa ngôn ngữ (Interop): Swift với Objective-C, C, C++.
  - Xây dựng pipeline tự động hóa CI/CD với Fastlane, TestFlight và App Store Connect API.
- **[Lộ trình Chuyên gia (Master)](swift_ios/04_swift_ios_master.md):**
  - Chiến lược di chuyển mã nguồn toàn diện Swift 5 sang Swift 6 (Strict Concurrency Checking).
  - Tiến hóa ABI và tính tương thích nhị phân (Library Evolution, `@frozen`, `@inlinable`).
  - Siêu lập trình với Swift Macros (Attached & Freestanding Macros).
  - Cơ chế đồng bộ dữ liệu ngoại tuyến (Offline-first sync), CRDTs và giải quyết xung đột dữ liệu.
  - Tích hợp thanh toán trong ứng dụng StoreKit 2 và đồng bộ đám mây CloudKit.
- **[Sổ tay Tham chiếu Vận hành Thực tế (Production Reference)](swift_ios/05_swift_ios_production_reference.md):**
  - Mẫu thiết kế chuẩn production, cấu hình Network Layer chống lỗi mạng chờn, Secure Keychain Wrapper.

---

## 3. Bản đồ Lộ trình Kotlin & Android (Google Ecosystem)

Toàn bộ giáo trình Android được đặt tại thư mục chuyên biệt [`kotlin_android/`](kotlin_android/README.md), bao gồm 4 cấp độ bài giảng, 8 phòng thí nghiệm chuyên sâu và 20 case study thực chiến:

- **[Lộ trình Nhập môn (Beginner)](kotlin_android/01_kotlin_beginner.md):**
  - Cú pháp Kotlin từ số 0: Khởi tạo biến, Null-safety (`?`, `?:`, `!!`), Smart Casts, Collections, Lambdas, Higher-order functions.
  - Cấu trúc Android Studio, Gradle build script (`build.gradle.kts`), AndroidManifest.xml.
  - 4 thành phần ứng dụng cốt lõi: Activity, Service, BroadcastReceiver, ContentProvider.
  - Jetpack Compose cơ sở: `@Composable`, `Modifier`, `Column`, `Row`, `Box`, `LazyColumn`, quản lý trạng thái với `remember` và `mutableStateOf`.
- **[Lộ trình Trung cấp (Intermediate)](kotlin_android/02_kotlin_intermediate.md):**
  - Kotlin Coroutines & Asynchronous Flow: `CoroutineScope`, `Dispatchers` (Main, IO, Default), `StateFlow`, `SharedFlow`.
  - Android Jetpack Architecture Components: ViewModel, LiveData/Flow, Repository Pattern.
  - Cơ sở dữ liệu cục bộ Room: Entity, DAO, TypeConverter, Room Migrations.
  - Kết nối mạng RESTful với Retrofit 2, OkHttp Interceptors, Moshi/Kotlinx Serialization.
  - Quản lý phụ thuộc (Dependency Injection) bằng Hilt / Dagger.
  - Tác vụ chạy nền đáng tin cậy với WorkManager và lưu trữ cấu hình Datastore.
- **[Lộ trình Nâng cao & Senior (Advanced / Senior)](kotlin_android/03_kotlin_advanced_senior.md):**
  - Cơ chế bên trong của Coroutines: Continuation-passing style, CoroutineContext, Cancellation & Exception Handling.
  - Tối ưu hóa Jetpack Compose Runtime: Phân tích Recomposition, Bỏ qua kết xuất (Stability, `@Immutable`, `@Stable`), DerivedStateOf.
  - Đóng gói và bảo vệ mã nguồn: R8 Compiler, ProGuard rules, obfuscation, thu nhỏ kích thước file APK/AAB.
  - Quản lý vòng đời tiến trình ứng dụng (App Process Death & Restoration với `SavedStateHandle`).
- **[Lộ trình Chuyên gia (Master)](kotlin_android/04_kotlin_master.md):**
  - Kiến trúc trình biên dịch Kotlin 2.x K2 Compiler và Java bytecode optimizations.
  - Kỹ thuật chia mô-đun ứng dụng quy mô lớn (Large-Scale Multi-module Architecture: Feature, Core, Domain, Data layers).
  - Đo lường và tối ưu hiệu năng cao cấp: Android Macrobenchmark, Baseline Profiles, JankStats, Memory leak detection với LeakCanary.
  - Nhập môn kiến trúc đa nền tảng Kotlin Multiplatform (KMP).
- **[Tiến hóa Phiên bản Android & Quy định Google Play](kotlin_android/05_kotlin_android_version_evolution.md):**
  - Cập nhật thay đổi hành vi từ Android 14 (API 34), Android 15 (API 35) đến Android 16/17 (API 36-37).
  - Đáp ứng chính sách hạn chót nâng cấp Target SDK của Google Play Store.

### Hệ sinh thái Chuyên sâu: Depth Labs & Production Casebook

- **[Phòng Thí nghiệm Kỹ thuật Chuyên sâu (8 Depth Labs)](kotlin_android/depth_labs/README.md):**
  - [Lab 01: Bất biến Kiến trúc & Ranh giới Suy luận](kotlin_android/depth_labs/01_architecture_invariants_boundary_reasoning.md)
  - [Lab 02: Đồng bộ Ngoại tuyến, Tính nhất quán & Race Conditions](kotlin_android/depth_labs/02_offline_sync_consistency_race_conditions.md)
  - [Lab 03: Ngữ nghĩa Thất bại trong Coroutine & Concurrency](kotlin_android/depth_labs/03_coroutine_flow_concurrency_failure_semantics.md)
  - [Lab 04: Compose Runtime, Trạng thái & Hiệu năng](kotlin_android/depth_labs/04_compose_runtime_state_performance_semantics.md)
  - [Lab 05: Kiểm thử Độ tin cậy & Tiêm lỗi Thử nghiệm (Failure Injection)](kotlin_android/depth_labs/05_testing_reliability_observability_failure_injection.md)
  - [Lab 06: Tương thích Build, Khởi động Ứng dụng & Pháp y Phát hành](kotlin_android/depth_labs/06_build_compatibility_startup_release_forensics.md)
  - [Lab 07: Ranh giới Native SDK & An toàn Người dùng API](kotlin_android/depth_labs/07_sdk_native_boundary_api_evolution_consumer_safety.md)
  - [Lab 08: Pháp y Di chuyển Mã nguồn & Tương thích Phiên bản](kotlin_android/depth_labs/08_version_compatibility_migration_forensics.md)
- **[Tuyển tập Tình huống Sản xuất Thực chiến (20 Production Cases)](kotlin_android/production_casebook/README.md):**
  - Bao quát 20 bài toán hóc búa nhất: Xác thực phiên và xoay token, Khôi phục sau Process Death, Tối ưu khởi động ứng dụng (Cold/Warm Start), Xử lý Camera & Cảm biến phần cứng, NDK/JNI Native C++ Memory management.

---

## 4. Điều hướng Liên kết Hệ thống

- [Quay về Trang chủ Repository](../README.md)
- [Cổng Danh mục Toàn diện CATALOG](../CATALOG.md)
- [Thư viện Kiến thức Phát triển Giao diện Web (10_frontend)](../10_frontend/README.md)
- [Thư viện Kiến thức Phát triển Phía Máy chủ (10_backend)](../10_backend/README.md)
- [Thư viện Khoa học Máy tính Nền tảng (computer_science)](../computer_science/README.md)
