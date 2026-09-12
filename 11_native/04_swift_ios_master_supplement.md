# Swift & iOS Master Note — Master Supplement

> Đây là phần bổ sung để tiến từ senior implementation sang mastery: language evolution, migration strategy, framework design, package/API stability, performance engineering, production operations và những khác biệt version quan trọng.

# 1. Version map cần ghi nhớ

Tại thời điểm biên soạn, nhánh production ổn định phù hợp để học/thực hành là Xcode 26.6 cùng Swift 6.2. Xcode 27 đã có Release Candidate và đi cùng Swift 6.4/iOS 27 SDK, nhưng RC không nên được coi như baseline ổn định cho tài liệu nền.

Mốc lịch sử hữu ích:

| Mốc | Ý nghĩa chính |
|---|---|
| Swift 5.x | ABI stability era, SwiftUI/Combine/concurrency dần trưởng thành |
| Swift 5.5 | async/await, structured concurrency, actors |
| Swift 5.9 | macro, Observation ecosystem bắt đầu phổ biến |
| Swift 6.0 | strict data-race safety language mode, typed throws, Synchronization |
| Swift 6.1 | tiếp tục cải thiện concurrency diagnostics, `nonisolated` mở rộng |
| Swift 6.2 | approachable concurrency, default isolation option, `@concurrent`, `InlineArray`, `Span`, Observation streams, testing improvements |
| Swift 6.4 / Xcode 27 RC | toolchain thế hệ tiếp theo; cần theo release notes khi lên stable |

Không nên học Swift bằng cách đóng đinh “một syntax từ blog năm X”. Hãy luôn biết language mode của target và deployment target.

---

# 2. Migration Swift 5 → Swift 6

Migration lớn nhất không phải syntax mà là concurrency correctness.

Quy trình tốt:

1. Bật warning/diagnostic theo từng target thay vì đổi toàn workspace một lần.
2. Phân loại warning theo ownership: UI state, shared mutable state, callback crossing isolation, non-Sendable dependency.
3. Đặt isolation đúng nơi thay vì dùng `@unchecked Sendable` để dập compiler.
4. Migrate library boundary trước hoặc sau tùy dependency graph, nhưng giữ build xanh theo từng bước.
5. Test behavior và performance vì isolation change có thể thay scheduling/lifetime.

Các fix phổ biến gồm đưa UI model về `@MainActor`, biến mutable shared singleton thành actor, chuyển snapshot sang Sendable value, bridge delegate callback về actor phù hợp và thay closure escaping không rõ sendability bằng API structured concurrency.

---

# 3. Swift 6.2 approachable concurrency và tác động thiết kế

Swift 6.2 thay đổi cách người mới tiếp cận concurrency: code có thể default vào main actor trong target phù hợp, giúp sequential code an toàn hơn, rồi opt-in concurrency tại nơi cần.

Điều này khuyến khích “progressive disclosure”: đừng biến mọi function thành concurrent. Chỉ đưa CPU-heavy, independent work ra concurrent executor khi có lợi.

`@concurrent` làm intent “chạy concurrent” rõ hơn trong model mới. Nhưng API availability/language mode phải được kiểm tra trong project cụ thể.

Senior migration note: cùng một source file có thể cho diagnostic khác khi build dưới Swift language mode khác hoặc feature flag khác. Vì vậy bug report phải kèm Xcode version, Swift version, language mode, target setting và deployment target.

---

# 4. Memory safety và systems features

Swift luôn tập trung memory safety nhưng vẫn có escape hatch như `UnsafePointer`.

Swift 6.2 thêm `Span` để truy cập contiguous memory có lifetime safety tốt hơn và `InlineArray` cho fixed-size inline storage. Đây là công cụ phù hợp framework thấp tầng, game/media, parsing, interop hoặc performance-sensitive code hơn là CRUD app thông thường.

Nguyên tắc mastery: chỉ dùng unsafe API khi boundary bắt buộc, encapsulate nó trong surface nhỏ, document invariant và viết test/fuzz nếu parsing binary/untrusted input.

Strict memory safety opt-in giúp audit unsafe construct. Với app xử lý dữ liệu security-critical, đây là hướng đáng cân nhắc.

---

# 5. Typed throws

Swift 6 hỗ trợ typed throws:

```swift
enum ParseError: Error {
    case invalidHeader
    case corruptedPayload
}

func parse(_ data: Data) throws(ParseError) -> Model {
    ...
}
```

Typed throws đặc biệt có giá trị với generic/embedded/API muốn express error domain compile-time. Nhưng app layer thường vẫn phải compose nhiều error source, nên `throws(any Error)` vẫn tự nhiên ở nhiều boundary.

Đừng tạo 40 error enum chỉ để “type-safe” nếu caller cuối cùng không phân biệt được chúng.

---

# 6. Observation thế hệ mới

`@Observable` khác `ObservableObject`: macro tạo tracking instrumentation và SwiftUI có thể track property read granularly.

```swift
@Observable
final class SearchModel {
    var query = ""
    var results: [ResultItem] = []
}
```

`@ObservationIgnored` loại property khỏi tracking.

Swift 6.2 bổ sung `Observations` như AsyncSequence để stream transactional changes. Đây là bridge quan trọng giữa observation model và async sequence.

Mastery point: observation là dependency tracking, không phải domain event bus. Nếu business cần audit event hoặc workflow explicit, dùng event/action abstraction riêng.

---

# 7. AsyncSequence

`AsyncSequence` là abstraction cho stream async:

```swift
for await value in stream {
    consume(value)
}
```

Nó phù hợp notification stream, bytes, socket messages, sensor events, observation changes.

Cancellation và backpressure semantics phải hiểu theo implementation. Không assume mọi AsyncSequence buffer vô hạn hay replay event.

Có thể viết custom AsyncStream:

```swift
let stream = AsyncStream<Int> { continuation in
    continuation.yield(1)
    continuation.finish()
}
```

Phải quản termination và resource cleanup.

---

# 8. API design cho framework/package

Public API là commitment. Một khi consumer phụ thuộc, rename/break signature có cost.

Thiết kế framework:

- surface nhỏ;
- type semantic rõ;
- avoid leaking third-party types nếu không muốn lock dependency;
- sendability/isolation phải là một phần contract trong Swift 6;
- document availability và thread/actor requirements;
- test binary/source compatibility tùy distribution model.

SPI (`@_spi`) và underscored attribute là implementation detail không nên dùng tùy tiện trong public ecosystem.

---

# 9. Library evolution và ABI

ABI stability cho Swift runtime trên Apple platform không đồng nghĩa mọi framework binary tự động future-proof.

Module stability, library evolution và `.swiftinterface` liên quan consumer build bằng compiler khác version.

`@frozen` cam kết stored layout của public struct/enum không thay đổi theo cách nhất định; sử dụng sai khóa evolution.

Đa số app developer không cần `@frozen`. Framework vendor cần hiểu sâu.

---

# 10. Macros trong production

Macro giúp giảm boilerplate nhưng compile-time toolchain complexity tăng.

Phân loại: freestanding expression/declaration macro và attached macro như member/accessor/conformance-related macro.

Khi chọn macro:

- code generated có predictable không;
- diagnostic có tốt không;
- compile time có chấp nhận được không;
- debugging có rõ không;
- consumer cần compiler/plugin dependency nào.

Không dùng macro để tạo “mini-language” khó discover nếu function/generic thông thường đủ tốt.

---

# 11. SwiftUI rendering mastery

SwiftUI View là description, không phải object UI persistent theo cách UIKit.

Identity quyết định lifetime của state storage. Nếu identity đổi, state có thể reset. Structural identity từ view tree và explicit identity qua `id` cần dùng có chủ đích.

Conditional view:

```swift
if isLoggedIn {
    HomeView()
} else {
    LoginView()
}
```

Hai branch có identity/type structure khác nhau. Đây có thể ảnh hưởng transition/state.

`AnyView` type-erases view nhưng có thể làm mất static structure/optimization và thường không cần với `@ViewBuilder`.

Đừng dùng `.id(UUID())` để “force refresh”; nó phá identity và thường che bug state.

---

# 12. View lifetime và task lifetime

`.task` được gắn với view identity và có cancellation semantics khi view biến mất/identity đổi.

```swift
.task(id: query) {
    await model.search(query)
}
```

Đây là idiom tốt cho task phụ thuộc input. Nhưng service-level work không nên vô tình bị cancel vì view redraw/navigation nếu business yêu cầu tiếp tục; lifetime của task phải thuộc đúng owner.

---

# 13. Data architecture mastery

Phân biệt:

- View state: trạng thái trình bày tạm thời.
- Feature state: state của flow.
- Domain state: business truth.
- Persisted state: dữ liệu lưu dài.
- Server state: dữ liệu remote authoritative.
- Cache: copy tối ưu.
- Derived state: tính từ state khác.

Bug lớn xảy ra khi một giá trị bị lưu ở nhiều lớp mà không có synchronization rule.

Single source of truth không có nghĩa toàn app chỉ có một object global. Nó nghĩa với một fact cụ thể phải biết source authoritative.

---

# 14. Offline-first và sync engine

Một app offline-first thực sự cần:

- local durable store;
- operation queue/outbox;
- sync cursor/version;
- conflict strategy;
- retry/backoff;
- idempotency;
- tombstone/delete semantics;
- account/logout data isolation;
- clock skew awareness.

Last-write-wins chỉ phù hợp một số domain. Collaborative data có thể cần server authority, field-level merge, version vectors hoặc CRDT tùy bài toán.

---

# 15. Design System

Design system production không chỉ là color constant. Nó gồm token, typography, spacing, radius, component state, accessibility, theming, localization và interaction behavior.

SwiftUI environment phù hợp theme token. Component public API không nên expose quá nhiều magic Boolean kiểu:

```swift
ButtonView(isSmall: true, isRed: true, hasIcon: true, ...)
```

Thay vào đó model variant/role semantic.

---

# 16. Feature flags

Feature flag giúp rollout/experiment nhưng có debt. Mỗi flag cần owner, expiry/removal plan và default behavior.

Remote config không được dùng như security authorization. Client flag có thể bị sửa.

Code path cũ sau khi rollout hoàn tất phải xóa để giảm combinatorial state.

---

# 17. Observability

Production mastery cần biết app ngoài đời đang xảy ra gì.

Ba nhóm chính:

- logs: event detail;
- metrics: aggregate trend;
- traces: flow qua operation/service.

Mobile app còn cần crash/nonfatal, launch time, hang, frame hitch, network latency, energy và memory footprint.

Telemetry phải respect privacy và sampling.

---

# 18. Performance budget

Đặt budget thay vì “cố nhanh”:

- cold/warm launch;
- memory peak;
- scroll hitch;
- network request;
- database query;
- package/build time;
- binary size.

Regression performance nên được detect trong CI/lab khi có thể.

---

# 19. Launch performance

Không nhồi synchronous work vào app init hoặc first view.

Deferred initialization, lazy dependency, background-safe work và cache precomputation có thể giúp, nhưng phải đo.

Static initializer/global singleton đôi khi chạy sớm ngoài kỳ vọng.

Dùng Instruments/App launch metrics thay vì đo bằng `Date()` đơn giản.

---

# 20. Memory pressure

iOS có thể terminate app khi memory pressure lớn. Cache phải có eviction strategy. Image bitmap memory thường lớn hơn file compressed.

`NSCache` có behavior phù hợp cache memory hơn dictionary trong nhiều use case.

Downsample image trước khi render nếu source resolution cực lớn.

---

# 21. Networking resilience

Timeout gồm nhiều loại: request/resource/connectivity. `URLSessionConfiguration` phải được hiểu theo behavior.

Background transfer dùng background URLSession, không phải Task sống mãi.

App lifecycle có thể bị suspend/kill; workflow quan trọng cần thiết kế recoverable từ persisted state.

---

# 22. Security mastery

Threat model trước implementation. Xác định asset, attacker capability, trust boundary, attack surface.

Biometric auth qua LocalAuthentication chỉ xác minh local user presence; không thay backend authorization.

Secure Enclave phù hợp key operation nhất định, không phải “nơi lưu mọi secret”.

Keychain accessibility cần chọn theo use case: accessible khi unlocked, after first unlock, device-only variants, v.v.

Certificate pinning chỉ dùng khi threat model justify và có rotation/backup pin strategy.

---

# 23. Privacy và App Store compliance

Permission string phải giải thích đúng mục đích. Request permission đúng thời điểm context, không hỏi tất cả ngay launch.

Data minimization: không collect thứ không cần.

Tracking/analytics SDK third-party là supply-chain/privacy risk. Kiểm soát manifest, disclosure và version.

---

# 24. App Extensions

Widget, Share Extension, Notification Service Extension, Live Activity-related extension có process/lifecycle/resource constraint riêng.

Không giả định extension chia sẻ memory với main app. App Group/container dùng cho data sharing khi phù hợp.

Extension execution time/memory thường hạn chế hơn app chính.

---

# 25. WidgetKit và Live Activities

Widget không phải mini app chạy liên tục. Timeline/provider và system policy quyết định refresh.

Live Activity dùng ActivityKit cho ongoing state trên Lock Screen/Dynamic Island tương ứng device/platform. Update strategy phải tiết kiệm và phù hợp push capability khi remote update.

---

# 26. App Intents

App Intents expose action/entity cho Siri, Shortcuts, Spotlight và system experiences.

Design intent phải ổn định, parameter semantic rõ, query entity hiệu quả và permission đúng.

Đây là một phần ngày càng quan trọng của integration “bên ngoài app UI”.

---

# 27. StoreKit

In-App Purchase production cần hiểu product loading, purchase result, transaction verification, entitlement, restore và server-side validation tùy product.

StoreKit 2 dùng async sequence cho transaction updates. Không chỉ dựa vào UI callback một lần.

Subscription state có grace period, billing retry, revoked/refunded state.

---

# 28. CloudKit

CloudKit phù hợp một số app Apple ecosystem muốn sync mà không dựng backend đầy đủ.

Cần hiểu container, public/private/shared database, record zone, subscription và sync error.

Không chọn CloudKit nếu requirement cross-platform/backend query không phù hợp.

---

# 29. Core Location, MapKit, camera và permission-heavy frameworks

Framework hệ thống có lifecycle/permission/energy constraint riêng.

Location accuracy, background location và “always” permission phải có business reason mạnh.

Camera capture pipeline có thread/performance consideration; SwiftUI thường bridge UIKit/AVFoundation ở layer thấp.

---

# 30. Metal và rendering

Đa số app không cần Metal trực tiếp. Nhưng custom rendering/game/video/compute có thể cần.

Core Animation/UIKit/SwiftUI đã sử dụng GPU pipeline bên dưới. Đừng nhảy sang Metal để tối ưu UI bình thường.

---

# 31. Accessibility mastery

VoiceOver semantic tree có thể khác visual tree. Custom component phải expose role/value/action đúng.

Dynamic Type test ở size cực lớn, không chỉ default.

Reduced Motion/Transparency, Bold Text, Differentiate Without Color và contrast cần được cân nhắc.

Accessibility automation không thay test người dùng hoàn toàn.

---

# 32. Localization mastery

String Catalog giúp quản translation/pluralization. `String(localized:)` và localized resource phải dùng đúng context/comment.

Không concatenate localized fragments nếu grammar có thể đổi thứ tự.

Date/number/list formatting dùng locale-aware formatter/style.

Pseudo-localization giúp phát hiện clipping và hard-code.

---

# 33. Release engineering

Mỗi release nên có:

- build reproducible;
- changelog/release note;
- migration test;
- feature flag plan;
- observability;
- rollback/kill switch nếu backend/feature cho phép;
- symbol upload cho crash symbolication;
- staged rollout khi phù hợp.

Mobile rollback khác web: user có thể giữ version cũ lâu. Backend phải backward compatible với nhiều app version trong window hỗ trợ.

---

# 34. Xcode 27 / iOS 27 preview notes

Xcode 27 RC đi cùng Swift 6.4 và SDK iOS 27. Vì đang ở RC, production app nên kiểm release notes cuối cùng trước adoption.

SwiftUI thế hệ Xcode 27 giới thiệu thêm API về toolbar, document, reorderable containers và performance/data flow. Một số thay đổi như AsyncImage caching mặc định hoặc State macro/lazy initialization có thể ảnh hưởng assumption cũ, nên migration phải có regression test.

Xcode 27 còn mở rộng coding agent integration. AI coding assistant không thay code review, test, security review hay understanding framework lifecycle.

---

# 35. Master-level learning strategy

Master Swift/iOS không có nghĩa thuộc toàn bộ SDK. SDK quá lớn và thay đổi mỗi năm.

Mastery thực tế là:

1. Đọc được API contract và availability.
2. Hiểu type system, ownership, isolation, lifecycle.
3. Thiết kế state/dependency boundary rõ.
4. Debug từ symptom xuống runtime/network/database.
5. Đo performance thay vì đoán.
6. Migrate framework/version mà không phá production.
7. Viết API dễ dùng đúng và khó dùng sai.
8. Biết khi nào không nên dùng abstraction/pattern mới.
9. Có release, monitoring và incident mindset.
10. Có khả năng đọc release notes/Swift Evolution và cập nhật mental model.

---

# 36. Bản đồ chủ đề để tra cứu sâu sau khi hoàn thành 4 note

Ngôn ngữ: generics, existentials, opaque types, protocol dispatch, ownership, macros, concurrency, Sendable, actors, typed throws, memory safety.

UI: SwiftUI layout, identity, Observation, navigation, animation, accessibility, UIKit interoperability, collection view.

Data: URLSession, Codable, cache, SwiftData/Core Data, sync/offline, Keychain.

Platform: notification, deep links, background task, StoreKit, WidgetKit, ActivityKit, App Intents, CloudKit, Core Location, AVFoundation.

Engineering: SPM, modularization, architecture, testing, CI/CD, signing, release, observability, performance, security/privacy.

Tooling: Xcode, Simulator, LLDB, Instruments, Organizer, `xcodebuild`, Test Plans, package resolution, build settings.

Nếu bạn có thể giải thích và triển khai các nhóm trên mà không chỉ copy sample code, bạn đã vượt qua mức “biết Swift” và đang ở mức iOS engineer có khả năng ownership production system.
