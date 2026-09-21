# Swift & iOS Knowledge Library

Bộ tài liệu này là lộ trình canonical để học Swift và iOS từ gần như số 0 đến mức có thể ownership một hệ thống production. Đây không phải cheat sheet. Mỗi level cố gắng giải thích theo mạch: khái niệm là gì → vì sao tồn tại → hoạt động thế nào → khi nào dùng → cách dùng → lỗi/edge case → cách người có kinh nghiệm sử dụng trong production.

## Baseline version — cập nhật 21/09/2026

Baseline stable hiện hành là **Xcode 27 + Swift 6.4 + iOS 27 SDK**. Swift 6.4 đã phát hành chính thức ngày 15/09/2026. Xcode 27.1/27.2 vẫn đang ở beta tại thời điểm cập nhật nên không được dùng làm baseline stable của library.

Tài liệu vẫn giữ kiến thức Swift 5.x, UIKit, Combine, Core Data và Objective-C interoperability ở những nơi cần thiết để đọc, migrate và maintain codebase production nhiều thế hệ.

## Canonical learning path

Lộ trình bắt buộc là:

**01 Beginner → 02 Intermediate → 03 Advanced / Senior → 04 Master**

`05_swift_ios_production_reference.md` không phải Level 5 và không thay thế bốn file canonical. Nó là tài liệu tra cứu xuyên cấp sau khi đã có mental model từ 01–04.

### 1. [Beginner](01_swift_ios_beginner.md)

Beginner xây nền semantics. Nội dung đi từ Swift/Xcode/version axes, value/type system, String/collection, control flow, function/parameter, Optional, struct/class/enum/protocol, initialization, properties/access control, closure lifetime, ARC/memory ownership, error/generics/Foundation đến SwiftUI, state ownership, navigation, URLSession, concurrency nhập môn, persistence, UIKit lifecycle, UIKit ↔ SwiftUI interoperability, testing, SwiftPM và signing.

Phần quan trọng nhất không phải thuộc syntax mà là hiểu `struct` khác `class` ở semantics nào, closure escaping ảnh hưởng lifetime ra sao, retain cycle hình thành thế nào, `await` là suspension chứ không phải “background thread”, `@State` sở hữu state ra sao và UIKit controller lifecycle khác app/scene lifecycle như thế nào.

#### Gate Beginner → Intermediate

Chỉ nên chuyển sang Intermediate khi bạn giải thích được value/reference semantics, Optional, closure capture, strong/weak/unowned, ARC vs data race, task cancellation cơ bản, source of truth của `@State`/`@Binding`, sequence cơ bản của `UIViewController`, deployment target khác SDK/compiler version, và có thể dùng breakpoint/test/Memory Graph để kiểm chứng assumption.

### 2. [Intermediate](02_swift_ios_intermediate.md)

Intermediate xây ownership và isolation ở mức feature. Nội dung đi sâu generics/existentials, structured concurrency, `Task`, cancellation, actor isolation, reentrancy, `@MainActor`, `Sendable`/`@Sendable`, AsyncSequence/continuation, SwiftUI state với `@State`, `@Binding`, `@Observable`, `@Bindable`, Environment, view identity và `.task(id:)`, rồi nối sang navigation, networking, retry/idempotency/auth refresh, Codable boundary, SwiftData/Core Data context, dependency injection, architecture, UIKit interoperability, background work, testing, diagnostics và module boundary.

#### Gate Intermediate → Advanced / Senior

Bạn cần nhìn một feature và chỉ ra được task owner, cancellation policy, actor/isolation boundary, dữ liệu crossing boundary và Sendable semantics, SwiftUI source of truth, view identity, network/persistence boundary, dependency source và test point. Nếu compiler concurrency warning chỉ được sửa bằng annotation mà không giải thích được ownership trước/sau, chưa nên sang Advanced.

### 3. [Advanced / Senior](03_swift_ios_advanced_senior.md)

Advanced/Senior chuyển từ feature correctness sang production implementation. Phần này đào sâu ownership/resource lifetime, Swift concurrency invariant, SwiftUI rendering/performance, UIKit lifecycle đầy đủ, custom containment, navigation/presentation, scene/multi-window, collection reuse, memory traps, Representable lifecycle, Coordinator, `UIHostingController`, hybrid source-of-truth, incremental UIKit ↔ SwiftUI migration, architecture theo state/effect ownership, modularization, API evolution, Instruments, networking/persistence reliability, security/privacy, testing, CI/CD và incident handling.

#### Gate Advanced / Senior → Master

Bạn phải có khả năng vẽ được cho một app hybrid thật: object ownership graph, view/controller lifecycle, task graph, actor/isolation boundary, SwiftUI state ownership, network/persistence boundary và module dependency graph. Bạn cũng phải biết đo performance bằng tool, phân tích retain path, test migration/release artifact và giải thích rollback constraint của mobile.

### 4. [Master](04_swift_ios_master.md)

Master tập trung vào longevity của hệ thống. Nội dung giải thích evolution Swift/iOS theo tác động đến programming model, từ Swift 1–3, Codable/Swift 4, ABI/Swift 5, SwiftUI/Combine, async/await/actors, macros/Observation/SwiftData, Swift 6 data-race safety, Swift 6.2 approachable concurrency đến Swift 6.4 ownership/build evolution.

Từ đó tài liệu đi vào version-support policy, Swift 5 → 6.x migration, source/binary/API compatibility, schema migration, offline sync, distributed mobile versioning, HTTP resilience, large-scale architecture, ADR, observability, performance/energy budgets, threat modeling, privacy/supply-chain, App Extensions, StoreKit, release artifacts, staged rollout, rollback và disaster recovery.

#### Completion target

Sau Master, mục tiêu không phải “thuộc toàn bộ Apple SDK”. Bạn phải có mental model đủ mạnh để khi Swift/Xcode/iOS thay đổi, có thể xác định cái gì thực sự đổi, boundary nào bị ảnh hưởng, migration/test nào cần chạy và release thế nào để không biến production user thành migration test.

## Production Reference — không phải level tiếp theo

### [Production Reference & Completion Guide](05_swift_ios_production_reference.md)

Dùng file này sau Master hoặc khi cần tra cứu một failure mode xuyên cấp. Nó gom closure lifetime/`@Sendable`, numeric correctness, HTTP semantics, tolerant decoding, retry/backoff/idempotency, Core Data legacy, background transfer, ownership APIs mới, generated code, observability, Memory Graph, extension process boundary, supply-chain security, ADR/version matrix, disaster recovery, release-artifact testing và Definition of Done theo risk.

Không đọc 05 thay cho 01–04. Reference cố tình cross-cutting và giả định bạn đã có vocabulary về ownership, isolation, state, lifecycle và compatibility.

## Những dependency kiến thức không nên bỏ qua

**ARC trước concurrency.** Nếu chưa phân biệt object lifetime với synchronized access, bạn dễ nhầm retain cycle với data race hoặc dùng actor như công cụ quản memory.

**Task/isolation trước architecture.** Architecture diagram không có giá trị nếu không chỉ ra async effect sống ở đâu, ai cancel và mutable state thuộc isolation nào.

**SwiftUI state trước performance.** Tối ưu rendering khi identity/source of truth còn sai thường chỉ che bug.

**UIKit lifecycle trước hybrid migration.** Representable/HostingController chỉ dễ hiểu khi bạn đã nắm lifecycle và ownership của hai framework.

**Production implementation trước version governance.** Master giả định bạn đã biết implementation hoạt động; lúc đó mới đánh giá migration, compatibility, rollout và recovery có ý nghĩa.

## Version principles

Luôn tách **Xcode version**, **Swift compiler version**, **Swift language mode**, **SDK version** và **deployment target**. Một API compiler biết chưa chắc chạy được trên deployment target cũ.

Runtime availability dùng `#available`; compile-time source/platform selection dùng `#if`, `canImport`, `os(...)` hoặc target environment phù hợp. Với package/library, còn phải theo dõi `swift-tools-version`, dependency version và public API availability.

Khi tài liệu/blog cũ mâu thuẫn behavior của toolchain đang dùng, ưu tiên Swift.org/Swift Evolution, Apple Developer Documentation và Xcode release notes chính thức.

## Project progression đề xuất

Ở Beginner, xây một Reading List để nối language → ARC → UI → async → persistence. Ở Intermediate, mở rộng thành Catalog/Search có cancellation, auth mock, pagination, cache và deep link. Ở Advanced/Senior, refactor app đó thành hybrid/module rõ, dùng Instruments, migration test và CI/CD. Ở Master, giả lập nâng Swift/Xcode/minimum iOS, thay backend/schema, rollout feature flag và viết ADR/rollback plan.

Cách học này biến bốn file thành một hệ thống liên tục thay vì bốn tập kiến thức độc lập.