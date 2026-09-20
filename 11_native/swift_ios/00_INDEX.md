# Swift & iOS Knowledge Library — Index

Bộ tài liệu này là lộ trình học Swift và iOS từ gần như số 0 đến mức có thể ownership một hệ thống production. Đây không phải cheat sheet. Mỗi file cố gắng giải thích khái niệm theo mạch “là gì → vì sao tồn tại → hoạt động thế nào → khi nào dùng → cách dùng → lỗi/edge case → production note”.

## Baseline version — cập nhật 20/09/2026

Baseline hiện hành của bộ note là **Xcode 27 + Swift 6.4 + iOS 27 SDK**. Swift 6.4 đã phát hành chính thức ngày 15/09/2026. Xcode 27 hỗ trợ Swift language mode 6, 5, 4.2 và 4, vì vậy tài liệu vẫn giữ các ghi chú migration và legacy cần thiết để đọc codebase cũ. Xcode 27.1/27.2 đang ở beta và không được dùng làm baseline stable.

## Lộ trình

### 1. [Beginner](01_swift_ios_beginner.md)

Học Swift core, type system nền tảng, Optional, collection, struct/class/enum/protocol, ARC, generic, Foundation, Xcode project/build settings, SwiftUI, UIKit nhập môn, state/navigation, URLSession, Codable, SwiftData, file system, SPM, form/focus, gesture/animation, test và signing. Đây là file phải đọc theo thứ tự nếu bắt đầu từ gần như số 0.

### 2. [Intermediate](02_swift_ios_intermediate.md)

Đi sâu generic/existential, property wrapper/macro, structured concurrency, actor/Sendable, AsyncSequence, task cancellation, SwiftUI data flow/layout/navigation, network layer, persistence, dependency injection, architecture, UIKit interoperability, background execution, SPM/module boundary, sanitizers và deterministic testing.

### 3. [Advanced / Senior](03_swift_ios_advanced_senior.md)

Tập trung vào ownership, dispatch, actor reentrancy, performance, UIKit/SwiftUI internals ở mức ứng dụng, production architecture, modularization, build/compile time, Instruments, resilient networking, database concurrency, security, testing strategy, CI/CD, Objective-C/C/C++ interop, noncopyable/borrowing và incident mindset.

### 4. [Master](04_swift_ios_master.md)

Tập trung vào migration Swift 5→6.x, Swift 6.4, ABI/library evolution, macros, systems/memory-safety APIs, rendering identity, offline sync, observability, performance/energy budget, App Extensions, WidgetKit, ActivityKit, App Intents, StoreKit, CloudKit, release engineering, distributed-version migration, multi-platform/cross-platform Swift và production-readiness audit.

### 5. [Production Reference & Completion Guide](05_swift_ios_production_reference.md)

Đây là file tra cứu sau khi đã đi qua lộ trình chính. Nó gom những vấn đề xuyên cấp thường chỉ rõ khi app tiến vào production: escaping/sendable closure, numeric correctness, HTTP semantics, tolerant decoding, retry/backoff/idempotency, Core Data legacy, background URLSession, ownership mới, SwiftPM plugin/generated code, observability, Memory Graph, App Extension process boundary, supply-chain security, ADR/compatibility matrix, disaster recovery, release-artifact testing và Definition of Done theo risk.

## Nguyên tắc version

Một API được compiler biết chưa chắc chạy được trên deployment target cũ. Luôn tách **Xcode version**, **Swift compiler/language mode**, **SDK version** và **deployment target**. Với runtime API mới, dùng availability check; với source khác theo platform/build mode, dùng conditional compilation.

Tài liệu ưu tiên API hiện đại nhưng không xóa UIKit, Combine, Objective-C interop, Core Data và các pattern legacy quan trọng, bởi codebase production thực tế thường tồn tại qua nhiều thế hệ framework.
