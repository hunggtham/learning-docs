# Native Mobile — source ledger và platform/SDK version boundary

> **Owner:** `11_native/` (canonical Swift/iOS và Kotlin/Android content). Ledger này tách language semantics, OS SDK API, device behavior, app-store policy và observed lab evidence.

**Lần kiểm tra cổng nguồn:** 2026-10-09 (Asia/Seoul).

## Source ledger

| Source ID | Cơ quan/chủ thể | Claim type được phép | URL | Version/date | Currentness boundary | Owner/used in |
|---|---|---|---|---|---|---|
| NAT-APPLE-01 | Apple Developer Documentation | Swift/iOS SDK, lifecycle, privacy, signing, distribution và platform API | https://developer.apple.com/documentation/ | SDK/Xcode/OS version phải ghi; portal kiểm tra 2026-10-09 | API availability, entitlement, device behavior và review policy phụ thuộc OS/SDK/device; không suy từ simulator | `swift_ios/` |
| NAT-SWIFT-01 | Swift project | Swift language, concurrency, standard library và ABI/module evolution | https://docs.swift.org/swift-book/documentation/the-swift-programming-language/ | Swift toolchain/version phải ghi | Language semantics tách khỏi Apple SDK; Swift 5/6 strict concurrency và compiler diagnostics có thể khác | Swift track |
| NAT-ANDROID-01 | Android Developers | Android SDK, lifecycle, permissions, Jetpack và platform behavior | https://developer.android.com/docs | API level/Android Studio/Jetpack version phải ghi | API level, OEM, targetSdk, permission policy và background limits có thể đổi; ghi device/API evidence | `kotlin_android/` |
| NAT-KOTLIN-01 | Kotlin documentation | Kotlin language, coroutines, multiplatform và compiler behavior | https://kotlinlang.org/docs/home.html | Kotlin/compiler/library version phải ghi | Coroutine/library behavior và generated code phụ thuộc version; không suy Android lifecycle từ Kotlin docs | Kotlin track |
| NAT-OWASP-01 | OWASP Mobile Application Security | mobile threat model, MASVS/MASWE controls và security verification guidance | https://mas.owasp.org/ | MASVS/MASWE release phải ghi; kiểm tra 2026-10-09 | Guidance không thay threat model, platform policy hoặc penetration evidence của app cụ thể | security/release |

## Claim chưa đủ nguồn

| Claim ID | Trạng thái | Ranh giới an toàn | Owner/next verification |
|---|---|---|---|
| NAT-API-01 | `NEEDS_SOURCE` | API/lifecycle/permission claim cần OS API level, SDK, targetSdk và device context; “Android/iOS” không đủ specificity. | Owner platform track |
| NAT-PERF-01 | `NEEDS_SOURCE` | Battery, memory, startup, rendering và network performance cần device/OS/build/workload/measurement window. | Owner production lab |
| NAT-STORE-01 | `NEEDS_SOURCE` | App review, privacy, entitlement, signing và store policy cần policy/version/jurisdiction hiện hành; không dùng guide cũ như guarantee. | Owner release chapter |
| NAT-SECURITY-01 | `REVIEW_REQUIRED` | Security claim phải nối threat model → control → device/runtime test → release evidence; checklist không phải proof. | Owner security track |
| NAT-LEGACY-01 | `REVIEW_REQUIRED` | Claim về Swift 5/UIKit/Objective-C hoặc Android legacy cần nêu deployment target và migration boundary; không trộn với baseline hiện tại. | Owner migration chapters |

## Quy trình refresh

1. Ghi language/compiler, Xcode/Android Studio, SDK/API level, OS/device và build configuration.
2. Tách language semantics, OS framework, OEM/device behavior, store policy và app-specific evidence.
3. Với release/migration, chạy lại sample trên simulator lẫn device nếu claim liên quan lifecycle/performance/security.
4. Khi policy hoặc API đổi, đánh dấu `REVIEW_REQUIRED` cho chapter liên quan cho đến khi có evidence mới.
