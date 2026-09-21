# Swift & iOS Master Note — Master

> Mục tiêu: từ Senior implementation tiến tới mastery: hiểu **language/platform evolution**, migration strategy, framework/API stability, distributed data compatibility, performance/security governance, release engineering và cách giữ một iOS system sống qua nhiều năm.
>
> Baseline cập nhật 21/09/2026: **Xcode 27 + Swift 6.4 + iOS 27 SDK**. Swift 6.4 phát hành chính thức 15/09/2026. Xcode 27.1/27.2 vẫn là beta tại thời điểm cập nhật nên không dùng làm stable baseline.

Master không dạy lại `@State`, actor hay UIKit lifecycle. Nó giả định bạn đã có thể vẽ ownership/task/isolation/state/module graph từ Advanced và dùng các graph đó để đánh giá migration, compatibility và production risk.

---

# 1. Cách đọc version: compiler, language mode, SDK, OS và package là các trục khác nhau

Một project có ít nhất các version axis sau:

- Xcode/toolchain version;
- Swift compiler version;
- Swift language mode/feature settings;
- iOS SDK dùng lúc compile;
- minimum deployment target;
- Swift package tools/dependency versions;
- binary SDK/framework versions;
- backend API/schema version;
- local persistence schema version.

“Dùng Swift 6.4” không tự động nghĩa app chỉ chạy iOS 27. “Build bằng iOS 27 SDK” cũng không nghĩa được gọi mọi API iOS 27 trên thiết bị iOS 17 mà không availability check.

Version debugging phải ghi đủ context. Bug report chỉ nói “Swift 6 lỗi” thường thiếu dữ liệu để reproduce.

---

# 2. Swift evolution — thay đổi cách lập trình, không phải danh sách release note

## 2.1 Swift 1–2: ngôn ngữ mới, ecosystem còn biến động

Các đời đầu đặt nền cho Optional, value types, protocol-oriented design và safety, nhưng syntax/API thay đổi mạnh. Code legacy từ thời này ít gặp trực tiếp hơn, nhưng lịch sử giải thích vì sao nhiều API wrapper/blog cũ không compile trên Swift hiện đại.

Bài học: source compatibility chưa phải điều mặc định trong giai đoạn đầu; khi đọc code rất cũ, đừng cố “sửa từng syntax” mà phải hiểu intent rồi map sang modern API.

## 2.2 Swift 3: API design và call-site readability trở thành convention lớn

Swift 3 là bước chuẩn hóa naming/import style rất mạnh. Apple SDK Swift names được thiết kế lại theo API Design Guidelines, argument labels/call-site trở nên tự nhiên hơn.

Ảnh hưởng lâu dài: Swift code hiện đại coi API naming là một phần semantics. Function không chỉ “tên + parameter”; call site cần đọc rõ hành động và relation giữa argument.

## 2.3 Swift 4.x: Codable và model boundary trở nên type-safe hơn

`Codable` làm JSON/property-list mapping phổ biến chuyển từ `[String: Any]`/manual cast sang compiler-checked model. Key path và standard-library improvements tiếp tục khuyến khích strongly typed APIs.

Ảnh hưởng: transport model có thể được type hóa dễ hơn, nhưng “Codable được” không có nghĩa transport DTO nên trở thành domain model. Boundary design vẫn là architecture concern.

## 2.4 Swift 5.0: ABI stability thay đổi cách phân phối Swift app/framework

ABI stability trên Apple platforms giảm nhu cầu bundle Swift runtime theo cách cũ và tạo nền tảng cho binary ecosystem ổn định hơn. Đây không phải lời hứa rằng mọi Swift framework tự động binary-compatible vĩnh viễn.

Swift 5.x còn là thời kỳ source compatibility tốt hơn, làm enterprise codebase có thể sống qua nhiều Xcode generation hơn.

## 2.5 Swift 5.1 + SwiftUI era: opaque type/property wrapper/result builder thay đổi UI style

`some View`, property wrappers và result-builder-style DSL tạo điều kiện cho SwiftUI. UI chuyển từ imperative object mutation sang declarative state-driven description.

Ảnh hưởng architecture: identity/state ownership trở nên quan trọng hơn view-object lifetime kiểu UIKit. Nhưng UIKit không biến mất; hybrid architecture trở thành skill production.

## 2.6 iOS 13 era: SwiftUI + Combine

SwiftUI và Combine đưa declarative UI/reactive stream vào Apple ecosystem. Nhiều codebase 2019–2022 có `ObservableObject`, `@Published`, `AnyPublisher`, `sink`, scheduler-heavy pipeline.

Khi maintain code này, không cần rewrite chỉ vì async/await/Observation mới hơn. Xác định boundary nào được hưởng lợi từ migration và giữ behavior/test trước.

## 2.7 Swift 5.5: async/await, structured concurrency và actor

Đây là thay đổi programming model lớn. Callback pyramid và nhiều Combine use case có alternative structured hơn. Actor đưa isolation vào language thay vì chỉ convention queue/lock.

Ảnh hưởng: “thread-safe” dần chuyển thành “isolation/sendability correct”. Nhưng API callback/Combine/OperationQueue/GCD vẫn tồn tại ở framework legacy và cần bridge đúng.

## 2.8 Swift 5.7–5.9: existential clarity, macros, Observation

`any` làm existential intent rõ hơn; generic/opaque/existential trade-off dễ nói chính xác hơn. Macro mở compile-time code generation. Observation giảm boilerplate `ObservableObject/@Published` và track dependency granular hơn.

SwiftData xuất hiện ở iOS 17 era, giúp persistence Swift-native hơn nhưng không xóa database fundamentals như schema/migration/index/transaction.

## 2.9 Swift 6.0: data-race safety trở thành language-level migration

Swift 6 language mode đưa concurrency correctness từ “warning/convention” tới compile-time guarantee mạnh hơn. `Sendable`, actor isolation, global actor và closure sendability trở thành API contract thực sự.

Typed throws và Synchronization/tooling tiếp tục mở rộng khả năng express contract.

Ảnh hưởng lớn nhất: API library giờ phải nghĩ đến isolation/sendability như public surface, không thể coi concurrency là implementation detail hoàn toàn.

## 2.10 Swift 6.2: approachable concurrency và safe systems direction

Swift 6.2 làm concurrency dễ tiếp cận hơn qua default isolation/configuration và explicit concurrent execution intent, đồng thời phát triển `Span`, `InlineArray` và memory-safety tooling.

Ảnh hưởng: mental model “mọi async function tự chạy background” càng không còn đúng. Sequential/isolation-first code là default hợp lý; concurrency được opt-in ở nơi có lợi.

## 2.11 Swift 6.4: ownership, build và cross-platform maturity

Swift 6.4 là stable baseline hiện tại. Những thay đổi đáng chú ý ở mức direction:

- Swift Build trở thành build system mặc định của SwiftPM;
- ownership/memory-safe performance APIs mở rộng với `Ref`, `MutableRef`, `UniqueBox`, `UniqueArray`, `Iterable` và safe raw-memory access;
- `Span` interop với C++20 `std::span` sâu hơn;
- Observation/testing/debug tooling tiếp tục cải thiện;
- Swift tiếp tục mở rộng Android, WebAssembly, Embedded và server/tooling use cases.

Đối với iOS app, không cần thay `Array` bằng `UniqueArray` hay dùng systems API chỉ vì mới. Điều cần hiểu là Swift đang dịch chuyển về compile-time ownership/safety mạnh hơn và build/tooling thống nhất hơn.

---

# 3. UIKit → SwiftUI evolution — vì sao hai mental model cùng tồn tại

UIKit dùng object/lifecycle/delegate/target-action/Auto Layout. SwiftUI dùng value description/state/identity/dependency tracking.

Không có một ngày “UIKit hết hạn”. Nhiều framework system vẫn expose UIKit/UIViewController pattern hoặc API thấp tầng dễ bridge qua representable. Production migration nên chọn seam, không chọn ideology.

Mốc platform đáng nhớ theo ảnh hưởng lập trình:

- SwiftUI/Combine era: declarative/reactive bắt đầu;
- SwiftUI App/Scene lifecycle: app entry/lifecycle có declarative surface mới;
- NavigationStack era: route/state-driven navigation thay dần `NavigationView` cho app hiện đại;
- Observation/SwiftData era: state/persistence Swift-native hơn;
- Xcode 27/iOS 27: state/builder internals, caching/data-flow/tooling tiếp tục tiến hóa.

Mỗi lần nâng framework, regression test phải tập trung identity/lifetime/navigation/focus/accessibility hơn là chỉ compile success.

---

# 4. Version support policy — trước khi viết code mới

Mỗi product nên có policy rõ:

- minimum iOS version;
- Xcode version dùng ở CI/release;
- Swift language mode;
- package update cadence;
- khoảng backend backward-compatibility;
- số local schema version phải hỗ trợ migration;
- thời gian app version cũ còn được backend hỗ trợ.

Không có policy thì mỗi engineer tự quyết và compatibility debt tích lũy âm thầm.

---

# 5. Availability strategy

Runtime API:

```swift
if #available(iOS 27, *) {
    useNewAPI()
} else {
    useFallback()
}
```

Compile-time source/platform:

```swift
#if canImport(UIKit)
import UIKit
#endif
```

Public framework API có thể dùng `@available` để encode requirement/deprecation vào compiler.

Đừng tạo fallback chỉ để “support version cũ” nếu fallback semantics sai. Đôi khi đúng hơn là disable feature với UX rõ hoặc nâng deployment target sau product analysis.

---

# 6. Migration Swift 5 → Swift 6.x — ownership-first workflow

Migration concurrency tốt không bắt đầu bằng fix compiler warning ngẫu nhiên.

## 6.1 Inventory

Lập bản đồ:

- global/singleton mutable state;
- UI model/controller isolation;
- callback/delegate crossing queue;
- non-Sendable SDK type;
- closure lưu lâu;
- database context/object boundary;
- GCD/OperationQueue/Combine pipeline;
- test phụ thuộc timing.

## 6.2 Move boundary theo batch

Migrate module/feature có test trước. Giữ commit nhỏ đủ bisect. Khi annotation thay đổi execution semantics/lifetime, thêm regression test.

## 6.3 Không dùng escape hatch như migration strategy

`@unchecked Sendable`, `nonisolated(unsafe)` hoặc global `@MainActor` có thể hữu ích ở boundary được chứng minh, nhưng nếu dùng để silence compiler hàng loạt, bạn đã xóa safety mà migration định đạt được.

## 6.4 Bridge legacy thay vì rewrite đồng loạt

Callback → continuation, Combine → async sequence, GCD-protected store → actor có thể migrate từng seam. Giữ bridge ở boundary và xóa khi consumer mới đã ổn định.

---

# 7. API/library evolution và source/binary compatibility

Public API là commitment. Framework/package sống lâu phải cân nhắc:

- source compatibility;
- semantic compatibility;
- binary/module compatibility nếu phân phối binary;
- actor/isolation/sendability contract;
- availability;
- deprecation window.

ABI stability của Swift runtime trên Apple platform không tự động làm mọi binary framework future-proof.

Module stability/library evolution/`.swiftinterface` liên quan consumer compiler khác version. `@frozen` khóa một phần layout/evolution của public type; dùng sai làm future change khó hơn.

SPI/underscored API không nên bị consumer coi như public stable contract.

---

# 8. Semantic versioning nội bộ và deprecation

Ngay cả package chỉ dùng nội bộ cũng cần version/change discipline nếu nhiều module/team consume.

Breaking change có thể:

1. thêm API mới;
2. deprecate API cũ với migration message;
3. migrate consumer;
4. xóa sau window đã thống nhất.

```swift
@available(*, deprecated, message: "Use load(request:) instead")
func loadLegacy() { }
```

Đừng giữ compatibility shim vô hạn; mỗi shim là branch cần test.

---

# 9. Macros và generated code governance

Macro giảm boilerplate nhưng thêm compiler plugin/tooling dependency và generated code không thấy trực tiếp ở source.

Production checklist:

- expansion có deterministic không;
- diagnostic có readable không;
- compile-time cost có đo không;
- public API generated có stable không;
- security/supply-chain của macro package có được review không;
- developer có biết xem expansion khi debug không.

Nếu ordinary generic/function đủ rõ, macro không nhất thiết tốt hơn.

---

# 10. Ownership/memory-safe systems boundary

Unsafe API chỉ nên nằm ở adapter nhỏ với invariant rõ. Với binary parser/C/C++ interop:

- validate bounds/alignment;
- document lifetime/ownership;
- convert sang Swift-safe representation sớm;
- fuzz untrusted input;
- bật safety diagnostics phù hợp.

Swift 6.4 thêm nhiều safe alternative cho use case trước đây cần pointer/CoW workaround. Adoption nên theo benchmark và resource semantics, không theo novelty.

---

# 11. Data architecture — source of truth theo loại dữ liệu

Phân biệt:

- presentation/view state;
- feature workflow state;
- domain state;
- local persisted state;
- server authoritative state;
- cache;
- derived state.

“Single source of truth” không có nghĩa toàn app có một global store. Nó nghĩa mỗi fact biết authoritative owner và synchronization rule.

Ví dụ, `isFavorite` có thể authoritative ở server, mirrored local để offline, optimistic UI tạm thời. Ba representation tồn tại nhưng phải có reconciliation policy rõ.

---

# 12. Persistence schema là public contract với dữ liệu user

App binary có thể rollback không dễ, nhưng user database phải upgrade forward đáng tin.

Migration strategy cần test:

- fresh install;
- N-1 → N;
- các version cũ còn thực tế ngoài field → N;
- interrupted/crash giữa migration nếu framework/store có risk;
- account logout/login;
- corrupted/partial data policy;
- large real-world dataset performance.

SwiftData/Core Data abstraction không loại bỏ requirement này.

---

# 13. Core Data/SwiftData context-isolation mastery

Managed/persisted object có context/model-container lifetime. Không xem nó như Sendable domain DTO tùy ý.

Cross-boundary pattern thường tốt hơn:

```text
DB context/model actor
      ↓ map
Sendable immutable snapshot/domain value
      ↓
feature/UI actor
```

Nếu UI cần live observation trực tiếp từ persistence, boundary có thể khác nhưng ownership/context rule vẫn phải rõ.

Index/query/predicate shape thường ảnh hưởng performance lớn hơn việc “chạy background” một query xấu.

---

# 14. Offline-first là sync system, không phải cache

Một offline-first engine thực sự thường cần:

- durable local source;
- outbox/pending operations;
- idempotency key;
- retry/backoff;
- sync cursor/version;
- conflict resolution;
- tombstone/delete semantics;
- auth/account data isolation;
- clock-skew awareness;
- observability cho stuck sync.

Last-write-wins chỉ là một conflict policy, không phải default đúng cho mọi domain.

---

# 15. Mobile API compatibility là distributed systems problem

Tại cùng một thời điểm có thể tồn tại:

```text
backend N
app N
app N-1
app N-3 offline nhiều ngày
local schema cũ
cache cũ
feature flags khác nhau
```

Server phải giữ compatibility window. Client nên tolerant với additive field/enum evolution nếu contract yêu cầu. Breaking semantic change cần versioned endpoint/feature negotiation/migration strategy phù hợp.

Không release backend và app theo giả định mọi user cập nhật đồng thời.

---

# 16. HTTP semantics và resilience

Retry policy phải dựa trên operation semantics.

GET/read thường dễ retry hơn mutation. POST/payment/order có thể đã được server commit trước khi client timeout; retry mù có thể duplicate side effect.

Production client cần nghĩ đến:

- connect/request/resource timeout;
- cancellation;
- `Retry-After`;
- 401 refresh single-flight;
- 429/rate limit;
- idempotency key;
- exponential backoff + jitter;
- cache validation;
- offline/poor connectivity;
- background transfer.

Reachability không nên được dùng như oracle “request chắc chắn sẽ thành công”. Network state có thể đổi giữa check và request.

---

# 17. Background URLSession và recoverable workflow

Nếu download/upload cần tiếp tục khi app bị suspend/terminated theo system policy, background `URLSession` là primitive phù hợp hơn giữ `Task` trong process.

Workflow cần persist identifier/state đủ để process mới reconnect/reconcile result. Memory-only progress model không đủ cho operation sống qua process death.

---

# 18. Architecture mastery — dependency rule theo volatility

Architecture không phải số layer. Boundary nên bảo vệ phần ổn định khỏi phần biến động:

- domain rule khỏi REST schema;
- feature state khỏi concrete database;
- UI khỏi third-party SDK;
- module consumer khỏi implementation helper;
- product behavior khỏi analytics vendor.

Nếu một SDK thay đổi làm 50 file feature sửa trực tiếp, SDK type đã leak quá sâu.

---

# 19. Anti-corruption adapter tại framework/SDK boundary

Third-party payment/analytics/map SDK nên được wrap khi API/type của nó không nên trở thành domain contract.

Adapter không phải wrapper 1:1 vô nghĩa. Nó map semantic: domain event → vendor call, vendor result → domain result, và giữ vendor lifecycle/config ở một boundary.

Điều này tạo exit strategy khi vendor thay đổi.

---

# 20. Large-scale modular architecture

Module boundary nên cân bằng:

- cohesion;
- build performance;
- team ownership;
- testability;
- public API size;
- dependency fan-in/fan-out.

Micro-module hóa quá mức tạo package graph phức tạp; mega-module làm mọi thay đổi recompile/ripple. Đo build graph và change pattern thật.

Architecture Decision Record (ADR) hữu ích cho quyết định khó đảo: persistence engine, navigation ownership, minimum OS, sync strategy, key security policy, modular boundary.

ADR tốt ghi context, alternatives, decision, consequence và trigger để revisit — không phải tài liệu marketing.

---

# 21. Design System là product API

Design system gồm token, typography, spacing, components, interaction states, accessibility, localization và theming.

Component API nên semantic:

```swift
PrimaryButton(role: .destructive, size: .compact)
```

thay vì nhiều Boolean khó tạo combination hợp lệ.

Design system versioning cũng là API evolution: component behavior change có thể affect hàng chục feature và snapshot/accessibility test.

---

# 22. Observability — từ log đến field diagnosis

Ba lớp:

- log: event/context cục bộ;
- metric: aggregate trend;
- trace/signpost: duration/flow qua operation.

Mobile-specific signal gồm crash, nonfatal, launch/hang, frame hitch, memory footprint, energy, network latency/error, DB latency và sync backlog.

Telemetry cần privacy minimization, sampling và stable event schema. Nếu release N đổi tên mọi event, so sánh trước/sau release khó hơn.

---

# 23. Symbolication và release artifact traceability

Crash stack chỉ hữu ích khi symbolicate đúng build. Mỗi release cần giữ mapping giữa:

- app version/build;
- commit SHA;
- Xcode/toolchain;
- archive;
- dSYM/symbol artifact;
- feature flag/config version nếu có.

“Không reproduce được” thường trở nên dễ hơn khi field report có đủ artifact identity.

---

# 24. Performance engineering — budget trước micro-optimization

Đặt SLO/budget phù hợp product:

- cold/warm launch;
- memory peak/steady state;
- scrolling hitch/frame time;
- image decode;
- request latency;
- DB query;
- sync throughput;
- energy/background wakeup;
- binary size;
- build time.

Optimization workflow: measure → hypothesis → change → remeasure. Không chọn `struct`/`final`/manual cache chỉ vì “nghe nhanh hơn” nếu bottleneck nằm ở network/image/layout.

---

# 25. Launch performance

Startup critical path phải nhỏ. Tránh synchronous DB migration/network/SDK initialization hàng loạt trên main actor trước first meaningful UI.

Có thể lazy/defer noncritical service, nhưng deferred work vẫn cần owner và error handling. Đừng biến “defer” thành task storm ngay sau first frame.

Global/static initializer có thể làm work sớm ngoài ý định; profile launch stack để thấy sự thật.

---

# 26. Memory pressure và cache economics

iOS có thể terminate process khi memory pressure. Cache phải có eviction/size policy; decoded image có thể lớn hơn file compressed rất nhiều.

`NSCache` phù hợp cho nhiều in-memory cache use case vì có eviction behavior, nhưng không phải persistence/source of truth.

Downsample ảnh theo display target, cancel decode/prefetch không còn cần và profile resident memory trên device.

---

# 27. Energy/thermal là performance requirement

CPU/GPU/network/location/background wakeups tiêu pin và sinh nhiệt. Polling, retry loop, location high accuracy, animation liên tục có thể làm system throttle.

Measure bằng Instruments/field metrics; Simulator không phản ánh đầy đủ thermal/energy behavior.

---

# 28. Threat modeling trước security control

Xác định:

- asset cần bảo vệ;
- attacker capability;
- trust boundary;
- entry point;
- hậu quả compromise;
- mitigation cost.

Không mọi app cần certificate pinning/Secure Enclave/custom crypto. Control không match threat model có thể thêm operational risk mà không giảm attack đáng kể.

---

# 29. Keychain, biometrics và Secure Enclave

Keychain accessibility option quyết định khi item truy cập được và có migrate/backup/device-only hay không tùy option. Chọn theo use case, không copy snippet mặc định.

LocalAuthentication xác minh user presence/biometry policy ở device; nó không thay authorization backend.

Secure Enclave phù hợp protected key operations nhất định; không phải generic database để bỏ mọi secret.

---

# 30. Secret, transport và trust boundary

Secret server-side không thể được giấu an toàn vĩnh viễn trong client binary. API key có privilege cao phải nằm backend.

ATS giúp enforce secure transport; exception nên scope nhỏ và có lý do. Certificate pinning cần key/cert rotation/recovery plan trước khi ship.

Client validation cải thiện UX/hardening nhưng server vẫn phải enforce authorization/business rule.

---

# 31. Privacy và supply-chain security

Chỉ collect data cần cho product/operation. Permission request đúng context; purpose string phải phản ánh usage thật.

Third-party SDK có thể thêm network endpoint, data collection, binary size và vulnerability surface. Review transitive dependency, privacy manifest/disclosure, maintainer/release cadence và update strategy.

Dependency pin quá cứng có thể giữ vulnerability; auto-update không review có thể đưa breaking/malicious change. Cần policy cân bằng.

---

# 32. App Extension/process boundary

Widget, Share Extension, Notification Service Extension, Live Activity-related component có process/resource/lifecycle riêng. Không giả định main app và extension share in-memory singleton.

Data sharing qua App Group/container hoặc system-defined mechanism cần consistency/security policy. Extension budget thường khắt khe hơn app chính; heavy work phải được thiết kế lại, không copy nguyên service graph.

---

# 33. StoreKit và entitlement state

Purchase success UI callback không phải nguồn duy nhất. StoreKit 2 transaction updates/verification và entitlement reconstruction cần xử lý across launch/device/account.

Subscription có grace period, billing retry, revoked/refunded state. Server-side verification có thể cần khi entitlement liên quan backend service/value.

Idempotency đặc biệt quan trọng khi fulfillment/reward có side effect.

---

# 34. WidgetKit, ActivityKit và App Intents

Widget refresh do system policy; không phải mini-app timer. Live Activity cũng có update/budget/lifecycle riêng.

App Intents expose domain action/entity cho Shortcuts/Siri/Spotlight/system experience. API intent là public-like contract với system; naming/parameter/entity query cần stable semantic.

Đừng để extension/intent trực tiếp import toàn app module nếu chỉ cần domain/service subset.

---

# 35. CloudKit và sync choice

CloudKit phù hợp Apple ecosystem sync use case nhất định, nhưng không tự động phù hợp cross-platform/backend analytics/query requirement.

Khi chọn sync backend, đánh giá identity, sharing, conflict, offline, migration, observability và vendor lock-in — không chỉ “không cần dựng server”.

---

# 36. Accessibility/localization là release quality gate

VoiceOver tree, Dynamic Type cực lớn, Reduce Motion, Differentiate Without Color, contrast và custom action phải được test ở critical flow.

Localization cần pluralization/context, không concatenate sentence fragment nếu grammar có thể đổi order. Pseudo-localization bắt clipping/hard-code trước khi translation thật.

Accessibility/localization regression nên nằm trong Definition of Done của component/flow có user-facing UI, không phải phase “sau khi code xong”.

---

# 37. Feature flag governance

Flag cần:

- owner;
- purpose;
- default;
- rollout audience;
- metric success/failure;
- kill-switch semantics nếu có;
- expiry/removal ticket.

Flag không phải authorization. Client flag có thể bị manipulate. Khi rollout xong, xóa dead branch để giảm state-space test.

---

# 38. Release engineering — build artifact là sản phẩm

Pipeline không kết thúc ở unit test. Release artifact cần:

1. reproducible dependency/toolchain config;
2. archive Release configuration;
3. signing/entitlement verification;
4. migration install/upgrade test;
5. critical UI/background/push/deep-link smoke test;
6. symbol upload;
7. TestFlight/staged rollout policy;
8. monitoring/rollback/kill-switch readiness.

Fresh install pass không chứng minh upgrade từ production version pass.

---

# 39. Mobile rollback strategy

App Store binary không rollback tức thì cho toàn bộ user. Vì vậy mitigation hierarchy thường gồm:

- disable feature qua server/flag nếu được thiết kế;
- backend compatibility fix;
- hotfix binary;
- staged rollout pause;
- data repair/migration nếu cần.

Rollback plan phải được nghĩ trước khi release feature có migration/destructive side effect.

---

# 40. Disaster recovery và data repair

Nếu migration/sync bug làm dữ liệu sai, cần biết:

- có backup/server authority không;
- có audit history/event log không;
- repair có idempotent không;
- app version cũ có tiếp tục làm hỏng data không;
- kill switch nào chặn writer;
- communication/rollout sequence nào tránh race giữa repair và client.

Đây là nơi observability, schema version và feature flag gặp nhau.

---

# 41. Xcode 27 / iOS 27 current notes

Baseline stable của library là Xcode 27/Swift 6.4/iOS 27 SDK. Minor Xcode 27.1/27.2 vẫn beta tại thời điểm cập nhật nên behavior chỉ có ở beta không được viết như production baseline.

Xcode 27 generation tiếp tục thay đổi SwiftUI state/builder implementation, caching/data-flow/tooling và coding-agent integration. Khi behavior thay đổi giữa Xcode 26 → 27:

- đọc release notes;
- tìm API contract thay vì dựa vào implementation detail;
- chạy UI state/identity regression;
- profile build/runtime nếu compiler/builder change liên quan;
- test archive, không chỉ Preview.

AI coding agent có thể viết/refactor/test, nhưng compiler green không chứng minh lifecycle, entitlement, security hay migration correctness.

---

# 42. Build technology và debugging evolution

Swift 6.4 dùng Swift Build làm default trong SwiftPM, giúp build behavior cross-platform thống nhất hơn.

Master-level build debugging cần đọc:

- package resolution;
- target/module graph;
- compiler invocation;
- explicit module dependency;
- linker error;
- architecture slice;
- generated interface;
- debug symbol/module metadata.

Xóa DerivedData chỉ là troubleshooting step, không phải root-cause analysis.

Swift 6.4 cũng tiếp tục cải thiện module tracking trong debug info, giúp LLDB tìm đúng module dependency chính xác hơn. Nếu `po`/expression evaluator lỗi, chưa chắc runtime object sai; build/debug metadata cũng là một layer cần kiểm tra.

---

# 43. Documentation engineering với DocC

Public/shared module nên document:

- semantics/invariant;
- ownership/lifetime;
- actor/thread requirement;
- error/cancellation;
- availability;
- side effect;
- usage example;
- migration/deprecation.

DocC cho phép API reference/article/tutorial nằm gần source. Nếu rất khó giải thích abstraction bằng vài đoạn rõ ràng, abstraction có thể đang ôm quá nhiều responsibility.

---

# 44. ADR và technical governance

ADR phù hợp quyết định khó đảo hoặc ảnh hưởng nhiều team: minimum OS, Swift language mode, architecture boundary, persistence/sync, navigation ownership, security policy, observability vendor.

Template tối thiểu:

```text
Context
Constraints
Options considered
Decision
Consequences / trade-offs
Migration plan
Revisit trigger
```

Không biến ADR thành approval bureaucracy cho mọi refactor nhỏ.

---

# 45. Production Definition of Done theo risk

Definition of Done không cần giống nhau cho mọi change. Một label text và migration database không có risk ngang nhau.

Risk cao có thể yêu cầu:

- unit/integration/UI regression;
- migration fixture;
- performance baseline;
- accessibility check;
- threat/privacy review;
- feature flag/rollback plan;
- observability metric;
- staged rollout.

Risk-based rigor tốt hơn checklist enterprise áp cho mọi commit.

---

# 46. Master audit matrix

Trước khi gọi một system production-ready, trả lời được:

| Trục | Câu hỏi bắt buộc |
|---|---|
| Language | language mode/toolchain nào, unsafe/ownership boundary ở đâu? |
| Memory | object/resource lifetime và retain graph có rõ không? |
| Concurrency | task owner, cancellation, isolation, reentrancy, Sendable contract? |
| UI | SwiftUI identity/state owner, UIKit lifecycle/interop boundary? |
| Data | server/local/cache authority và reconciliation? |
| Persistence | schema migration/context isolation/repair plan? |
| Network | timeout/retry/idempotency/auth refresh/background transfer? |
| Architecture | dependency direction/module API/vendor boundary? |
| Performance | budget + measurement trên release-like device? |
| Security | threat model, key/secret/transport/privacy controls? |
| Release | archive/signing/migration/staged rollout/symbols/rollback? |
| Operations | log/metric/trace/crash + incident/runbook? |

Không phải app nhỏ phải triển khai mọi enterprise mechanism. Nhưng các trục có rủi ro thật phải có câu trả lời có chủ đích.

---

# 47. Learning flow hoàn chỉnh Beginner → Master

**Beginner** xây semantics: value/reference, Optional, closure/ARC, SwiftUI state, async suspension, UIKit lifecycle và interop cơ bản.

**Intermediate** xây ownership/isolation: structured/unstructured task, actor/reentrancy, Sendable, Observation state ownership, network/persistence boundary và feature architecture.

**Advanced/Senior** xây production implementation: UIKit/SwiftUI hybrid lifecycle, modularization, API resilience, Instruments, persistence/network reliability, security, CI/CD và incident reasoning.

**Master** xây longevity: version evolution, source/binary/schema/API compatibility, governance, threat/performance budget, release/rollback/disaster recovery.

Nếu một khái niệm Master không nối được về graph ở Advanced hoặc semantics ở Beginner/Intermediate, quay lại level trước thay vì học thêm tool mới.

---

# 48. Cách tự cập nhật kiến thức sau khi tài liệu này lỗi thời

Không tài liệu Swift/iOS nào giữ đúng mãi. Workflow cập nhật:

1. đọc Swift.org release post + Swift Evolution proposal liên quan;
2. đọc Xcode release notes/system requirements;
3. đọc Apple framework API availability/documentation;
4. xác định change thuộc language, compiler, SDK hay runtime;
5. mapping vào mental model: type/ownership/isolation/state/lifecycle/boundary/compatibility;
6. viết reproduction nhỏ;
7. migration trên một feature trước;
8. đo build/runtime/test trước khi rollout toàn repo.

Tutorial/blog/community post hữu ích cho implementation idea, nhưng khi mâu thuẫn với API contract/release note của toolchain thực tế, ưu tiên nguồn chính thức.

---

# 49. Nguồn chính thức nên theo dõi

Ưu tiên Swift.org và Swift Documentation/Evolution cho language/compiler; Apple Developer Documentation cho UIKit/SwiftUI/Foundation/SwiftData/StoreKit và platform framework; Xcode Release Notes/System Requirements cho toolchain/SDK; WWDC sessions cho design intent/migration examples.

Mục tiêu Master không phải thuộc toàn bộ SDK. Mục tiêu là có mental model và production discipline đủ mạnh để khi Swift 6.5/7.x hoặc iOS thế hệ sau thay đổi API, bạn biết **cái gì thật sự đổi**, **boundary nào bị ảnh hưởng**, **test nào cần chạy** và **release thế nào để không biến user thành migration test**.