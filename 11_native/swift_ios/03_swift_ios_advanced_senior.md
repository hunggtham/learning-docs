# Swift & iOS Master Note — Advanced / Senior

> Mục tiêu: hiểu compiler/runtime/concurrency đủ sâu để thiết kế code production, tối ưu hiệu năng, quản lý module, testability, migration, security và architecture ở quy mô lớn.

# 1. Swift memory model, ownership và ARC sâu hơn

ARC chỉ quản lý reference-counted class/object graph, không “quản lý toàn bộ memory”. Struct có thể chứa reference; closure là reference type; collection có heap storage; bridging với Objective-C có semantics riêng.

Retain cycle thường xuất hiện ở closure:

```swift
final class Downloader {
    var onFinish: (() -> Void)?

    func start() {
        onFinish = { [weak self] in
            self?.cleanup()
        }
    }

    private func cleanup() {}
}
```

Không dùng `[weak self]` một cách máy móc. Nếu closure không được giữ lâu hơn `self`, weak có thể làm flow khó hiểu vô ích. Câu hỏi đúng là ownership graph: ai giữ closure, closure sống bao lâu, callback có cần owner tồn tại hay không?

`unowned` phù hợp khi lifetime invariant chứng minh reference luôn tồn tại lâu hơn người giữ reference. Nếu invariant sai, crash.

Swift optimizer có borrow/consume semantics ở mức language evolution ngày càng rõ hơn. Senior cần để ý copying cost của large value, existential boxing, closure allocation và bridging.

---

# 2. Existential, opaque type, primary associated type

`any P` tạo existential container có thể giữ một concrete conforming type. Nó cho runtime polymorphism nhưng có thể mất một số static type information và có cost abstraction.

`some P` giữ concrete type ẩn nhưng compiler vẫn biết type cụ thể nội bộ, phù hợp static dispatch/optimization hơn trong nhiều tình huống.

Primary associated type giúp protocol API ergonomic hơn:

```swift
protocol ImageFetching<Image> {
    associatedtype Image
    func fetch() async throws -> Image
}
```

Hãy tránh type erasure nếu generic/opaque type giải quyết được. Type erasure như `AnyPublisher` từng phổ biến với Combine vì API boundary, nhưng luôn có trade-off.

---

# 3. Dynamic dispatch, static dispatch và protocol witness

Class virtual dispatch, protocol witness table và generic specialization ảnh hưởng behavior/performance. Không cần viết app theo assembly, nhưng senior cần biết vì sao `final`, concrete generic và existential có thể cho optimizer cơ hội khác nhau.

Protocol extension dispatch là nguồn bug tinh tế:

```swift
protocol P {}

extension P {
    func foo() { print("P") }
}

struct S: P {
    func foo() { print("S") }
}

let p: any P = S()
p.foo() // dispatch theo member extension, không phải protocol requirement
```

Nếu polymorphic dispatch là ý định, hãy đưa method vào protocol requirement.

---

# 4. Concurrency trong Swift 6.x ở mức production

## 4.1 Isolation là khái niệm trung tâm

Swift concurrency không chỉ là “async/await”. Compiler track isolation domain để ngăn unsynchronized mutable access.

Main actor:

```swift
@MainActor
final class AppStore {
    private(set) var session: Session?
}
```

Actor riêng:

```swift
actor ImageCache {
    private var cache: [URL: Image] = [:]
}
```

Nonisolated member chỉ nên đọc immutable/sendable state hoặc implementation thật sự safe.

## 4.2 Reentrancy

Actor method có thể bị re-enter tại suspension point:

```swift
actor BankAccount {
    var balance = 100

    func withdraw(_ amount: Int) async throws {
        guard balance >= amount else { throw Error.insufficient }
        await externalCheck()
        // balance có thể đã thay đổi trong lúc suspend
        guard balance >= amount else { throw Error.insufficient }
        balance -= amount
    }
}
```

Không giữ assumption qua `await` nếu actor state có thể thay đổi. Đây là bug class rất quan trọng.

## 4.3 Task lifetime

`Task {}` inherit actor/context ở nhiều trường hợp. `Task.detached` không inherit actor isolation, priority và task-local values theo cùng cách; chỉ dùng khi thực sự muốn unstructured independent task.

Task lưu trong model cần cancel khi operation superseded:

```swift
private var searchTask: Task<Void, Never>?

func search(_ text: String) {
    searchTask?.cancel()
    searchTask = Task {
        try? await Task.sleep(for: .milliseconds(300))
        guard !Task.isCancelled else { return }
        await performSearch(text)
    }
}
```

## 4.4 Continuation bridge

Callback API cũ có thể bridge:

```swift
func load() async throws -> Data {
    try await withCheckedThrowingContinuation { continuation in
        legacyLoad { result in
            continuation.resume(with: result)
        }
    }
}
```

Checked continuation yêu cầu resume đúng một lần. Resume 0 hoặc >1 lần là bug nghiêm trọng.

## 4.5 Swift 6.x default isolation và `@concurrent`

Swift 6.x tiếp tục hướng approachable concurrency: executable/UI target có thể default main-actor isolation, async function có semantics caller-context thuận tự nhiên hơn theo feature setting, và `@concurrent` biểu diễn điểm chủ động chạy concurrent.

Điều này có nghĩa tài liệu Swift 5.7/5.9 cũ về “async function tự động chạy background” hoặc cách sprinkle `nonisolated` có thể không còn là mental model tốt. Hãy đọc compiler diagnostic theo language mode thực tế của target.

---

# 5. Synchronization thấp hơn actor

Không phải mọi synchronization cần actor. Với hot path thấp tầng, Swift có Synchronization APIs như mutex/atomic ở môi trường hỗ trợ. Dùng primitive thấp tầng chỉ khi benchmark chứng minh cần và invariants đơn giản.

Actor ưu tiên correctness và composability. Lock cho phép critical section synchronous nhưng dễ deadlock, lock ordering bug và priority inversion nếu thiết kế kém.

Không giữ lock xuyên `await`.

---

# 6. Performance của SwiftUI

SwiftUI performance thường bị hiểu sai là “body bị gọi nhiều = chậm”. `body` recomputation là thiết kế bình thường; vấn đề thực sự là expensive work, unstable identity, layout thrashing, object churn hoặc dependency quá rộng.

Không làm expensive computation trực tiếp trong `body`:

```swift
var body: some View {
    let sorted = expensiveSort(items) // có thể lặp lại nhiều lần
    ...
}
```

Tách derived data có cache/model khi cần.

Stable identity trong `ForEach` cực kỳ quan trọng. `ForEach(items.indices, id: \.self)` có thể sai khi data mutation/reorder.

Observation hiện đại chỉ invalidates dựa trên property được read, giúp granularity tốt hơn so với broad `objectWillChange` trong nhiều trường hợp.

`EquatableView` hoặc `.equatable()` không phải thuốc chữa mặc định. Đo trước bằng Instruments.

---

# 7. Custom SwiftUI Layout, Preference và Environment

Custom `Layout` phù hợp khi container cần đo nhiều child và tự placement.

PreferenceKey truyền thông tin ngược từ child lên ancestor, nhưng lạm dụng dễ tạo flow khó hiểu.

Environment phù hợp cross-cutting context như locale, dismiss, theme, dependency scoped theo tree. Không dùng Environment để che dependency mà feature thực sự yêu cầu bắt buộc; explicit initializer injection thường rõ hơn ở domain boundary.

---

# 8. UIKit advanced: lifecycle, containment và diffable UI

`UIViewController` containment phải gọi đúng `addChild`, add view, constraints/frame, `didMove(toParent:)`. Sai lifecycle dẫn đến appearance callback/navigation bug.

Collection view compositional layout mô tả layout bằng section/group/item và hỗ trợ adaptive UI mạnh.

Diffable Data Source dựa trên identity; snapshot là state UI. Apply snapshot quá thường xuyên hoặc identity sai có thể tạo animation/glitch/performance issue.

Cell reuse cần reset toàn bộ state hoặc dùng configuration API hiện đại. Async image loading phải cancel khi cell reuse.

---

# 9. Architecture production

## 9.1 Feature boundaries

Module boundary nên dựa trên ownership và dependency direction, không phải chia folder theo “Models/Views/ViewModels” toàn app.

Một cấu trúc modular có thể là:

```text
App
Features/
  Login
  Home
  Profile
Core/
  Networking
  Persistence
  DesignSystem
  Analytics
Domain/
```

Nhưng cấu trúc đúng phụ thuộc team và product. Mục tiêu là build graph hợp lý, compile time kiểm soát được, feature ownership rõ và API surface nhỏ.

## 9.2 Clean Architecture có chọn lọc

Entity/use-case/repository abstraction hữu ích nếu domain phức tạp và platform-independent. Với CRUD app nhỏ, 5 lớp wrapper cho một request chỉ tạo ceremony.

Senior design không hỏi “pattern nào đẹp nhất” mà hỏi “độ phức tạp này mua được lợi ích gì?”.

## 9.3 Coordinator/Router

UIKit Coordinator tách navigation khỏi ViewController. SwiftUI router/state-driven navigation cho mục tiêu tương tự.

Navigation layer không nên chứa business logic.

## 9.4 Reducer architecture

Reducer biến `(State, Action) -> State + Effect`. Nó làm event flow explicit, replay/test tốt nhưng có verbosity. Hợp với state machine phức tạp, nhiều effect và team cần convention nhất quán.

---

# 10. Dependency management và modularization

Swift Package Manager nên là lựa chọn đầu tiên cho package mới. Pin version theo strategy có kiểm soát. Tránh dependency explosion.

Binary framework/XCFramework dùng khi phân phối precompiled SDK. Phải quan tâm architecture slice, module stability, signing/privacy manifest và symbol.

`BUILD_LIBRARY_FOR_DISTRIBUTION` liên quan module interface stability khi phân phối binary Swift module; không bật vô lý cho app internal.

---

# 11. Build system và compile time

Compile time có thể tăng mạnh bởi expression type-checking phức tạp, giant SwiftUI view builder, generic chain sâu và module dependency graph kém.

Giải pháp thường là chia expression, giới hạn generic complexity, modularize theo boundary hợp lý, tránh generated code cực lớn và theo dõi build timing.

Debug và Release có optimization khác nhau; bug chỉ xuất hiện Release có thể liên quan undefined behavior ở C bridge, data race hoặc timing, không nên kết luận compiler bug trước.

---

# 12. Instruments và profiling

Các instrument quan trọng: Time Profiler, Allocations, Leaks, Network, Energy Log, Core Animation/hitches và SwiftUI-related instrumentation tùy Xcode.

Workflow performance chuẩn: xác định symptom → tạo reproducible case → đo baseline → tìm hot path → thay đổi một giả thuyết → đo lại.

Không optimize theo trực giác.

Memory leak và memory growth khác nhau. Leak là memory không thể reclaim do reference graph/lost pointer; growth có thể là cache hợp lệ hoặc retained state.

---

# 13. Networking production

HTTP client cần cancellation đúng với task. Nếu user rời màn hình, request không còn cần nên có thể cancel.

Authentication refresh phải single-flight:

```text
request A -> 401
request B -> 401
        \-> một refresh task dùng chung
            -> cập nhật token
            -> retry A/B theo policy
```

Nếu mỗi request tự refresh, có thể race token và gây refresh storm.

Retry dùng exponential backoff + jitter khi hợp lý. Tôn trọng idempotency, server `Retry-After`, network reachability và cancellation.

Certificate pinning có trade-off vận hành lớn; không triển khai chỉ vì “bảo mật hơn” mà không có rotation strategy.

---

# 14. Persistence production

Database schema là API lâu dài với dữ liệu user. Migration phải test bằng database snapshot từ version cũ.

SwiftData/Core Data relationship cần hiểu ownership/delete rule. Cascade delete sai có thể mất dữ liệu.

Không thực hiện heavy fetch/transform trên main actor nếu dataset lớn.

Cache khác source of truth. Hãy xác định dữ liệu authoritative ở server, local DB hay memory. Offline-first cần conflict resolution, sync metadata và retry queue chứ không chỉ lưu response.

---

# 15. Security

Không nhúng secret server-side vào app binary; attacker có thể extract. API secret thực sự phải nằm ở backend.

Keychain dùng cho credential/token. Sensitive file có Data Protection class phù hợp. ATS kiểm soát insecure transport; đừng tắt global ATS vì một endpoint legacy nếu có thể scope exception.

Validate input và response assumptions. Mobile client không phải trust boundary; backend phải enforce authorization.

Jailbreak detection không thể là guarantee security tuyệt đối.

Privacy manifest, permission usage description và data collection declaration là phần của release engineering hiện đại.

---

# 16. Accessibility, internationalization và adaptive UI

Senior iOS không hard-code screen size theo một iPhone. Hãy thiết kế cho size class, Dynamic Type, localization expansion, split view, rotation nếu app hỗ trợ và accessibility settings.

VoiceOver order, custom actions và semantics phải test thực tế.

Date/number/currency format dùng `FormatStyle`, không tự nối string:

```swift
Text(price, format: .currency(code: "USD"))
```

Locale không đồng nghĩa language; calendar/timezone cũng độc lập.

---

# 17. Testing strategy production

Pyramid không phải luật cứng nhưng pure unit test nhanh nên chiếm phần lớn behavior logic. Integration test xác minh boundary như persistence/network client. UI test chỉ cover critical flows vì chậm và dễ flaky.

Test doubles gồm fake, stub, spy, mock. Đừng gọi tất cả là mock.

Contract test cho API mapping giúp phát hiện server/schema change.

Concurrency test cần tránh sleep tùy tiện. Dùng deterministic dependency/clock nếu có thể.

Snapshot test hữu ích cho UI regression nhưng phải quản lý platform/font/rendering variance.

---

# 18. CI/CD

Một pipeline iOS thường gồm resolve dependency → build → lint/static analysis nếu có → unit/integration test → UI test chọn lọc → archive → sign/export → upload TestFlight/App Store.

Code signing trong CI cần strategy bảo mật certificate/profile hoặc managed signing.

`xcodebuild` là CLI cốt lõi:

```bash
xcodebuild \
  -scheme MyApp \
  -destination 'platform=iOS Simulator,name=iPhone 17' \
  test
```

Không hard-code credential trong repository.

---

# 19. App distribution

Archive khác normal build. Organizer quản lý archive và distribution.

TestFlight hỗ trợ internal/external testing. App Store review còn liên quan privacy, entitlement, guideline, export compliance, age rating và metadata.

Version (`CFBundleShortVersionString`) và build number (`CFBundleVersion`) phục vụ release khác nhau.

Phải test migration từ App Store version hiện tại lên build mới, không chỉ fresh install.

---

# 20. Combine trong codebase hiện hữu

Async/await đã thay thế nhiều use case callback/reactive đơn giản, nhưng Combine vẫn tồn tại nhiều production codebase.

Khái niệm: Publisher, Subscriber, Operator, Scheduler, Cancellable.

```swift
publisher
    .map(transform)
    .removeDuplicates()
    .sink(
        receiveCompletion: { completion in },
        receiveValue: { value in }
    )
    .store(in: &cancellables)
```

Đừng mix Combine và async/await vô tổ chức. Đặt boundary rõ và bridge khi cần.

---

# 21. Objective-C interoperability

Nhiều Apple framework và legacy code là Objective-C runtime-based.

`@objc`, `dynamic`, `NSObject`, selector, KVC/KVO vẫn xuất hiện.

Swift type không phải mọi thứ đều representable trong Objective-C. Generic Swift, enum associated value và nhiều feature Swift-only không expose trực tiếp.

Bridging header cho Swift ↔ Objective-C trong app mixed-language. Module map/framework import cần hiểu ở SDK integration.

---

# 22. C/C++ interoperability

Swift có thể gọi C trực tiếp qua imported module/header. Pointer API là vùng unsafe; lifetime và mutability phải rất rõ.

Swift 6.2 có thêm hướng safe systems programming như `Span`, `InlineArray` và strict memory safety opt-in. Đây không phải API mà mọi iOS app cần, nhưng senior nên biết vì framework thấp tầng, media, crypto hoặc C++ bridge có thể cần.

---

# 23. API design guidelines và coding idioms

Tên Swift ưu tiên call-site readability:

```swift
func remove(_ element: Element)
func move(from source: Index, to destination: Index)
```

Boolean nên đọc như assertion: `isEnabled`, `hasAccess`, `canRetry`.

Prefer value type, immutability và explicit state transitions.

Dùng extension để nhóm conformance/feature, không biến một type thành 2.000 dòng rải extension không ownership.

Không lạm dụng operator custom; code business phải đọc được.

`guard` thích hợp cho precondition/early exit; `if` phù hợp branch thực sự.

Avoid stringly-typed API khi enum/type-safe wrapper khả thi.

---

# 24. Senior Notes: các anti-pattern thường gặp

Massive ViewModel là phiên bản SwiftUI của Massive View Controller. Nếu ViewModel chứa networking, persistence, analytics, routing, mapping và business rule, hãy tách capability/use case.

Singleton service locator che dependency. Nó làm test order-dependent và khó reasoning lifecycle.

Repository-for-everything tạo abstraction ceremony. Repository hữu ích khi che data source hoặc domain boundary thật.

Generic abstraction quá sớm làm compiler error và call site khó hiểu. Hãy bắt đầu concrete, refactor khi duplication/concept lặp lại thực sự xuất hiện.

“Protocol để mock” không phải lý do duy nhất. Với Swift mới, dependency injection bằng closure/function value hoặc concrete fake đôi khi đơn giản hơn.

Async side effect trong initializer thường khó quản lifecycle. Ưu tiên explicit `load()` hoặc `.task`.

Đừng gắn `@MainActor` toàn module để hết warning nếu logic compute/network không thực sự thuộc UI. Fix isolation theo ownership.

---

# 25. Ownership features mới: borrowing, consuming và noncopyable types

Swift hiện đại đang làm ownership ngày càng explicit. `borrowing` cho phép dùng value mà không nhận ownership; `consuming` chuyển ownership. Noncopyable type (`~Copyable`) phù hợp resource cần unique ownership hoặc value không nên bị copy tùy tiện.

Application iOS thông thường chưa cần áp dụng ownership annotation rộng khắp. Giá trị của việc hiểu chúng là bạn có thể đọc standard-library/framework code mới, hiểu vì sao một API tránh copy và thiết kế wrapper cho resource thấp tầng tốt hơn.

Swift 6.4 tiếp tục mở rộng hệ sinh thái này bằng khả năng borrow/mutate accessors, `Ref`/`MutableRef`, `UniqueBox`, `UniqueArray` và `Iterable`, giúp performance-sensitive code tránh copy mà vẫn giữ memory safety tốt hơn so với raw pointer.

# 26. Swift 6.4 interoperability và systems boundary

Swift 6.4 mở rộng interop với C/C++ và Java. Với iOS engineer, C/C++ interop có ý nghĩa thực tế ở SDK media, game engine, crypto, database và thư viện legacy. `Span` có thể bridge với C++20 `std::span`, giảm nhu cầu cặp raw pointer + count thủ công.

Nguyên tắc senior là giữ unsafe/foreign boundary nhỏ. Convert dữ liệu sang Swift-safe representation càng sớm càng tốt, document lifetime và ownership ở adapter, rồi để phần còn lại của app không phải hiểu pointer semantics.

# 27. Continuation thế hệ mới và bridging legacy API

Checked continuation đã giúp bắt double-resume/missing-resume tốt hơn unsafe continuation. Swift 6.4 tiếp tục cải thiện hướng safe continuation với ownership-aware continuation API. Dù dùng loại nào, invariant cốt lõi vẫn là một callback operation phải hoàn thành continuation đúng semantics một lần, cancellation phải propagate nếu legacy API hỗ trợ, và callback có thể chạy trên queue bất kỳ nên isolation crossing phải rõ.

Bridge là boundary migration, không nên biến toàn app async/await thành callback rồi lại bridge qua lại nhiều lần.

# 28. SwiftUI Xcode 27: `State` macro, `ContentBuilder` và migration risk

Xcode 27 thay đổi implementation của hai primitive nền tảng. `State` trở thành macro, cho lazy initialization per view lifetime; nhiều builder chuyên biệt được unified dưới `ContentBuilder` để giảm type-checking cost. Phần lớn app không cần sửa, nhưng code sử dụng reflection, overload hack, custom generic phụ thuộc concrete builder type hoặc assumption rằng initializer expression chạy mỗi lần View struct tạo lại có thể đổi behavior.

Senior migration workflow là tìm các vùng dựa vào side effect trong `@State` initialization, thêm regression test, xem macro expansion nếu diagnostic khó hiểu và không “fix” bằng random annotation.

# 29. SwiftUI performance: image, list, scroll và rendering budget

Image decoding/downsampling thường là nguồn memory/hitch lớn. `AsyncImage` trên iOS 27 có HTTP caching tốt hơn, nhưng cache network bytes không giải quyết mọi vấn đề bitmap memory. Với image lớn, downsample theo display size trước render; với feed dài, prefetch có giới hạn và cancel khi item không còn cần.

List/scroll performance phụ thuộc stable identity, view complexity, expensive modifier, geometry feedback loop và synchronous work. Một item view nhỏ nhưng chạy formatter/parser/database fetch trong `body` vẫn có thể gây hitch.

# 30. Database concurrency và model actor

SwiftData có `ModelActor` để tổ chức access theo concurrency model. Nhưng “đưa mọi DB operation sang background actor” không tự động đúng: query result, model lifetime, context boundary và UI observation vẫn cần thiết kế nhất quán. Tránh truyền mutable model object tự do qua actor boundary; snapshot/value DTO thường dễ reasoning hơn.

Với data lớn, batch fetch, pagination, index và predicate shape quan trọng hơn việc thêm nhiều task. Database optimization bắt đầu từ query plan/data model, không phải concurrency trước.

# 31. Network protocol design và API compatibility

Mobile app có release lag: backend hôm nay phải phục vụ nhiều app version đã cài từ trước. Vì vậy API evolution cần backward compatibility window. Thêm field thường an toàn hơn đổi nghĩa field; enum từ server nên có unknown fallback nếu backend có thể thêm case.

Client request mutation quan trọng nên có idempotency key nếu backend hỗ trợ. Retry mobile network không được vô tình tạo hai payment/order/resource.

# 32. Feature modularization và compile-time architecture

Module không nên chỉ là folder được đổi thành package. Module là compile-time dependency boundary. Một feature module chỉ nên expose entry point/model cần cho consumer. Internal helper để `internal` thay vì `public` cho tiện.

Theo dõi dependency graph. Nếu mọi feature import một mega-module chứa networking, design system, database, analytics và domain, modularization không thật sự giảm coupling.

# 33. API resilience và semantic versioning cho internal package

Ngay cả package nội bộ cũng nên có compatibility discipline nếu nhiều team/feature cùng dùng. Breaking change cần migration plan. Public API docs, deprecation annotation và changelog giúp consumer nâng version có kiểm soát.

`@available(*, deprecated, message:)` cho compiler hướng dẫn migration. Khi thay API, đôi khi giữ shim một release rẻ hơn ép atomic migration toàn repo.

# 34. Advanced testing: property, fuzz, performance và concurrency

Ngoài example-based unit test, parser/serializer và algorithm có thể hưởng lợi từ property-based thinking: encode rồi decode phải giữ invariant; sort output phải có thứ tự và cùng multiset; migration phải bảo toàn record.

Fuzzing đặc biệt hữu ích cho binary/parser boundary. Performance test cần baseline ổn định và đo statistic đủ ý nghĩa, không assert thời gian quá chặt trên CI nhiễu.

Concurrency test nên kiểm cancellation, actor reentrancy, racing request và single-flight behavior. Bug async thường nằm ở interleaving, không ở happy path.

# 35. App startup, scene restoration và resilience

State restoration cần phân biệt navigation/UI transient state với domain persisted state. App có thể bị terminate bất ngờ; đừng dựa vào callback “app sắp chết” để save dữ liệu quan trọng.

Startup path nên deterministic và nhỏ: load config cần thiết, dựng dependency graph, render UI sớm, defer việc không critical. Nếu authentication/session cần check async, model hóa splash/loading state rõ thay vì block main thread.

# 36. Production incident mindset

Khi crash rate hoặc latency tăng, senior không sửa bằng phỏng đoán. Hãy xác định release/version/device/OS bị ảnh hưởng, compare rollout, xem symbolicated stack, log/metric, tạo reproduction nhỏ nhất, sau đó mới patch.

Mobile có đặc thù rollback chậm vì binary đã nằm trên thiết bị. Remote kill switch/feature flag cho tính năng rủi ro và backend backward compatibility là công cụ vận hành, nhưng phải có governance để không biến app thành rừng flag.

# 37. Review checklist cho code Swift/iOS cấp Senior

Một review tốt kiểm tra semantics trước style: ownership state, optional/error path, actor isolation, cancellation, identity, lifetime, API availability, backward compatibility, security/privacy và test. Sau đó mới tới naming/formatting.

Nếu một PR “đúng” nhưng reviewer mất 30 phút mới xác định data flow, đó là tín hiệu architecture/readability cần cải thiện. Code production tối ưu cho thay đổi an toàn trong tương lai, không chỉ compile hôm nay.
