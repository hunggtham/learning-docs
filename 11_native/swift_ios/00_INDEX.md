# Swift & iOS Knowledge Library — Index

Canonical learning path của bộ Swift/iOS là:

**01 Beginner → 02 Intermediate → 03 Advanced / Senior → 04 Master**

`05_swift_ios_production_reference.md` là reference xuyên cấp sau Master hoặc dùng để tra cứu failure mode production; nó **không phải Level 5** và không thay thế bốn file canonical.

## Baseline — 21/09/2026

Baseline stable: **Xcode 27 + Swift 6.4 + iOS 27 SDK**. Swift 6.4 phát hành chính thức ngày 15/09/2026. Xcode 27.1/27.2 vẫn ở beta tại thời điểm cập nhật nên không được coi là baseline stable.

Library vẫn giữ Swift 5.x, UIKit, Combine, Core Data và Objective-C interoperability khi chúng cần thiết để đọc/migrate production codebase.

## 1. [Beginner](01_swift_ios_beginner.md)

Nền semantics: Swift/Xcode/version axes, values/types, Unicode/collection, control flow, function/`inout`, Optional, struct/class/enum/protocol, initialization, properties, closure lifetime, ARC/memory, error/generic/Foundation, SwiftUI, state ownership, navigation, networking, concurrency nhập môn, persistence, UIKit lifecycle, interoperability, testing, SwiftPM và signing.

**Gate:** phải giải thích được value/reference semantics, escaping capture, retain cycle, `weak`/`unowned`, ARC khác data race, `await` là suspension, `@State`/`@Binding` ownership, UIKit lifecycle cơ bản và deployment target khác SDK/compiler.

## 2. [Intermediate](02_swift_ios_intermediate.md)

Feature ownership/isolation: generics/existentials, structured task, `Task`, cancellation, actor/reentrancy, `@MainActor`, `Sendable`/`@Sendable`, AsyncSequence/continuation, `@State`/`@Binding`/`@Observable`/`@Bindable`, Environment, identity, `.task(id:)`, networking/retry/idempotency/auth, Codable boundary, SwiftData/Core Data context, DI, architecture, UIKit bridge, background work, deterministic test và module boundary.

**Gate:** phải chỉ được task owner/cancellation, isolation boundary, Sendable crossing, SwiftUI source of truth/identity, network/persistence boundary, dependency source và test point của một feature thật.

## 3. [Advanced / Senior](03_swift_ios_advanced_senior.md)

Production implementation: ownership/resource lifetime, advanced concurrency invariant, SwiftUI rendering/performance, UIKit lifecycle đầy đủ, containment/navigation/scene/reuse, memory traps, Representable/Coordinator/HostingController, hybrid source-of-truth, migration UIKit ↔ SwiftUI, architecture/module graph, API evolution, Instruments, resilient network/persistence, security/privacy, CI/CD và incident handling.

**Gate:** phải vẽ được ownership graph, UIKit/SwiftUI lifecycle, task/isolation graph, state source-of-truth, data boundary và module dependency graph; đồng thời biết profile, test migration/release artifact và phân tích rollback risk.

## 4. [Master](04_swift_ios_master.md)

System longevity: Swift/iOS evolution theo programming model; Swift 5 → 6.x migration; source/binary/API compatibility; persistence schema và distributed mobile versioning; offline sync; HTTP resilience; architecture governance/ADR; observability; performance/energy budget; threat model/privacy/supply-chain; extension/StoreKit/system integration; release artifacts, staged rollout, rollback và disaster recovery.

**Completion target:** khi toolchain/framework mới xuất hiện, có thể xác định change thuộc compiler/language/SDK/runtime nào, boundary nào bị ảnh hưởng, test/migration nào cần chạy và rollout/recovery như thế nào.

## [Production Reference](05_swift_ios_production_reference.md)

Reference xuyên cấp cho các chủ đề hay xuất hiện khi debug/production audit: closure lifetime, numeric correctness, HTTP semantics, tolerant decoding, retry/backoff/idempotency, Core Data legacy, background transfer, ownership APIs mới, generated code, observability/memory graph, extension process boundary, supply-chain, ADR/version matrix, disaster recovery, release artifact testing và risk-based Definition of Done.

## Dependency rules của learning flow

Không bỏ ARC để nhảy thẳng concurrency; không bỏ task/isolation để nhảy thẳng architecture; không tối ưu SwiftUI khi source-of-truth/identity còn sai; không làm hybrid SwiftUI/UIKit khi lifecycle UIKit chưa chắc; không học version/release governance trước khi hiểu production implementation.

## Version rule

Luôn tách **Xcode version**, **Swift compiler**, **Swift language mode**, **SDK version** và **deployment target**. Runtime API mới dùng availability check; compile-time platform/source selection dùng conditional compilation. Package/library còn có `swift-tools-version`, dependency version và public API availability riêng.