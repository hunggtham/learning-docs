# Swift & iOS Master Note — Advanced / Senior

> Mục tiêu: từ feature-level correctness tiến tới production ownership: memory/concurrency invariant rõ, UIKit/SwiftUI lifecycle đúng, module/architecture có dependency direction, performance được đo, migration/release không dựa vào may mắn.
>
> Prerequisite: Intermediate — đặc biệt task lifetime, actor isolation/reentrancy, `Sendable`, Observation state ownership, HTTP/persistence boundary và UIKit ↔ SwiftUI bridge cơ bản.

Senior-level iOS engineering không phải biết nhiều API nhất. Đó là khả năng nhìn một hệ thống và giải thích **lifetime, ownership, isolation, identity, effect, boundary và compatibility**; sau đó dùng tool để kiểm chứng thay vì đoán.

---

# 1. Memory model và ownership sâu hơn

ARC chỉ quản lý lifetime của reference-counted object. Nó không quản lý “toàn bộ memory”, không phát hiện cycle và không giải quyết data race. Struct có thể chứa class reference; closure có reference identity/lifetime; collection có heap-backed storage; Objective-C bridge có autorelease/bridging behavior riêng.

## 1.1 Ownership graph thay vì quy tắc `weak self`

```swift
final class Downloader {
    var onFinish: (() -> Void)?

    func start() {
        onFinish = { [weak self] in
            self?.cleanup()
        }
    }

    private func cleanup() { }
}
```

Câu hỏi đúng là: ai giữ `Downloader`, ai giữ closure, closure sống đến khi nào, operation có cần owner sống để hoàn tất hay không. Nếu closure synchronous/non-escaping, weak capture thường không cần. Nếu closure được property/service giữ và closure lại giữ `self`, cycle có thể hình thành.

## 1.2 `weak` và `unowned` là lifetime contract

`weak` cho phép target biến mất và vì vậy access có Optional semantics. `unowned` không retain nhưng giả định target còn sống tại mọi access. `unowned` nên được dùng khi relation lifetime là invariant của model, không phải để tránh unwrap.

## 1.3 Closure capture không chỉ là `self`

Capture list có thể snapshot value hoặc thay ownership của reference. Large value capture, existential box, closure allocation và hidden bridging có thể ảnh hưởng memory/performance trong hot path. Đừng optimize trước khi profile, nhưng khi profile cho thấy allocation pressure, hãy biết closure/generic/existential cũng là nguồn allocation.

## 1.4 Autorelease và Objective-C boundary

Swift-native ARC và Objective-C ARC interoperable nhưng Foundation/Objective-C API có thể tạo autoreleased object. Trong batch loop lớn qua legacy API, autorelease pool scope có thể ảnh hưởng peak memory. Đây là optimization boundary; đừng rải `autoreleasepool` khắp app nếu Instruments chưa chỉ ra nhu cầu.

## 1.5 Resource ownership ngoài memory

File handle, socket, database transaction, camera session, security-scoped URL, observer token đều có lifetime. ARC có thể giúp owner object được deinit, nhưng business correctness không nên phụ thuộc vào thời điểm deallocation để commit/save/network. Resource quan trọng cần explicit open/close/start/stop policy khi framework yêu cầu.

---

# 2. Ownership language features và safe performance

Swift hiện đại làm ownership explicit hơn qua borrowing/consuming và noncopyable types. Mục tiêu là giảm copy và biểu diễn unique resource mà không rơi xuống raw pointer.

Application business code chưa cần annotate mọi value. Senior cần hiểu để đọc framework/library mới và để thiết kế boundary thấp tầng.

Swift 6.4 mở rộng nhóm API này với borrow/mutate accessors, `Ref`/`MutableRef`, `UniqueBox`, `UniqueArray`, `Iterable` và memory-safe access API. Chỉ dùng khi profile/resource semantics justify; `Array`/ordinary value types vẫn là default tốt cho phần lớn app.

---

# 3. Existential, opaque type và dispatch cost

`any P` là existential container cho runtime polymorphism; `some P` che concrete type nhưng giữ static identity cho compiler.

```swift
protocol ImageFetching<Image> {
    associatedtype Image
    func fetch() async throws -> Image
}
```

Type erasure mua flexibility nhưng có cost về type information, potential boxing/dynamic dispatch và API complexity. Không phải mọi public API phải generic; chọn abstraction dựa trên use case và compile-time/runtime trade-off.

Protocol extension dispatch trap:

```swift
protocol P { }

extension P {
    func foo() { print("P") }
}

struct S: P {
    func foo() { print("S") }
}

let p: any P = S()
p.foo()
```

Nếu `foo` không phải protocol requirement, dynamic behavior có thể không như người đọc kỳ vọng. Khi polymorphism là contract, khai báo requirement rõ.

---

# 4. Concurrency production — invariant qua suspension point

Intermediate đã học actor/reentrancy; ở Senior, trọng tâm là invariant và operation design.

```swift
actor BankAccount {
    private var balance = 100

    func withdraw(_ amount: Int) async throws {
        guard balance >= amount else { throw AccountError.insufficient }
        await externalCheck()
        guard balance >= amount else { throw AccountError.insufficient }
        balance -= amount
    }
}
```

`await` là nơi assumption có thể mất hiệu lực. Nếu operation cần atomic state transition, hãy giảm suspension bên trong critical semantic region hoặc lưu/revalidate version/state sau await.

## 4.1 Single-flight operation

Auth refresh, expensive cache load hoặc schema preparation thường cần “một operation in-flight, nhiều caller chờ chung”. Actor có thể giữ `Task` hiện tại và clear khi hoàn tất. Điều khó không phải syntax mà là failure/cancellation policy: caller cancel có cancel shared work không, hay shared task sống vì caller khác còn cần?

## 4.2 Task ownership

Task property phải có owner/lifetime policy. Screen task có thể cancel khi screen biến mất; upload/background sync có thể thuộc service khác. Task không nên sống vô hạn chỉ vì object bị singleton giữ.

## 4.3 Cancellation cleanup

Cancellation-aware operation cần cleanup idempotent. Nếu transaction đã mutate một phần state trước cancellation, rollback/compensation phải được thiết kế; `CancellationError` không tự đảo side effect.

## 4.4 Lower-level synchronization

Actor là default tốt cho shared mutable state. Mutex/atomics phù hợp hot synchronous primitive hoặc library thấp tầng khi benchmark/invariant justify. Không giữ lock xuyên `await`; tránh lock-order cycle và blocking main thread.

---

# 5. SwiftUI rendering/performance mental model

`body` được recompute là bình thường. Bottleneck thường đến từ expensive synchronous work, unstable identity, layout feedback, image decode, broad observation dependency hoặc object churn.

```swift
var body: some View {
    // bad nếu expensiveSort thật sự nặng và chạy thường xuyên
    let sorted = expensiveSort(items)
    List(sorted) { item in ... }
}
```

Derived data có thể chuyển sang model/cache khi cần; nhưng cache cũng có invalidation cost. Đo trước khi thêm complexity.

Stable identity quyết định state/task continuity. `.id(UUID())` để “refresh” gần như luôn là smell.

Image performance: network cache bytes khác decoded bitmap memory. Feed ảnh lớn cần downsampling theo display size, prefetch có giới hạn và cancellation khi item không còn visible.

---

# 6. SwiftUI layout, Preference và environment ở mức Senior

Custom `Layout` dùng khi container thật sự cần thuật toán measure/place riêng. PreferenceKey là cơ chế child → ancestor communication; dùng được nhưng dễ tạo hidden data flow/feedback loop nếu lạm dụng.

Environment phù hợp cross-cutting tree-scoped context. Domain dependency bắt buộc nên explicit ở boundary thích hợp. Một feature mà test không biết dependency đến từ đâu thường đã để environment/service locator che quá nhiều.

---

# 7. UIKit lifecycle — sequence và responsibility

UIKit vẫn là nền tảng của rất nhiều Apple UI API và production codebase. Senior phải hiểu lifecycle, không chỉ biết `viewDidLoad`.

Một `UIViewController` đi qua các phase chính:

1. `init`/storyboard decoding tạo controller object;
2. `loadView()` tạo root view nếu view chưa load;
3. `viewDidLoad()` chạy sau load, thường một lần cho lifetime của loaded view;
4. `viewWillAppear(_:)` mỗi lần chuẩn bị xuất hiện;
5. `viewIsAppearing(_:)` trong các SDK hiện đại cho phase appearance với geometry/trait đã cập nhật hơn;
6. layout callback như `viewWillLayoutSubviews()`/`viewDidLayoutSubviews()` có thể chạy nhiều lần;
7. `viewDidAppear(_:)` khi đã xuất hiện;
8. `viewWillDisappear(_:)`/`viewDidDisappear(_:)` khi rời màn hình.

Không đặt request one-time vào `viewWillAppear` nếu navigation back/forward sẽ gọi lặp ngoài ý muốn. Ngược lại, state phải refresh mỗi lần màn hình hiện lại không nên chỉ nằm trong `viewDidLoad`.

## 7.1 View loading khác controller lifetime

Controller tồn tại không đồng nghĩa `view` đã load. Truy cập `view` có thể trigger load. Dùng `isViewLoaded` khi cần kiểm mà không ép load.

## 7.2 Layout callback không phải nơi làm I/O

`viewDidLayoutSubviews` có thể được gọi rất nhiều lần do constraint, rotation, safe-area, content-size change. Không đặt network/database/heavy computation tại đây.

## 7.3 Trait và adaptive UI

Size class, Dynamic Type, interface style và platform trait có thể thay đổi trong lifetime. Với SDK mới, ưu tiên API trait observation hiện đại khi phù hợp thay vì assumption “setup theme một lần trong viewDidLoad”.

---

# 8. UIKit containment — child controller đúng lifecycle

Custom container phải tuân protocol containment:

```swift
addChild(child)
view.addSubview(child.view)
child.view.translatesAutoresizingMaskIntoConstraints = false
NSLayoutConstraint.activate([
    child.view.leadingAnchor.constraint(equalTo: view.leadingAnchor),
    child.view.trailingAnchor.constraint(equalTo: view.trailingAnchor),
    child.view.topAnchor.constraint(equalTo: view.topAnchor),
    child.view.bottomAnchor.constraint(equalTo: view.bottomAnchor)
])
child.didMove(toParent: self)
```

Removal:

```swift
child.willMove(toParent: nil)
child.view.removeFromSuperview()
child.removeFromParent()
```

Sai containment có thể làm appearance callbacks, rotation, safe area và child ownership hoạt động không đúng. Navigation controller/tab bar controller là system container; custom container phải tôn trọng lifecycle tương tự.

---

# 9. UIKit navigation/presentation lifecycle

`UINavigationController` giữ stack controller. `pushViewController`/`popViewController` thay stack; modal presentation tạo presentation relationship khác.

Không suy luận “viewDidDisappear = controller deinit”. Controller có thể vẫn ở navigation stack, presentation graph hoặc được object khác retain.

Interactive transition có thể cancel. Vì vậy side effect ở `viewWillDisappear` không nên mặc định coi navigation đã chắc chắn hoàn tất. Khi business cần biết route state chính xác, coordinator/router/navigation delegate có thể là nơi phù hợp hơn appearance callback.

---

# 10. Scene lifecycle và multi-window

App lifecycle và view-controller lifecycle là hai tầng khác nhau. Từ scene-based lifecycle, app có thể có nhiều `UIScene`/`UIWindowScene` tùy platform/configuration.

Một scene có thể active/inactive/background độc lập. Global singleton UI state dễ sai nếu app hỗ trợ nhiều scene/window. State nào thuộc account/app và state nào thuộc window/scene phải được phân biệt.

Không dựa vào “app sắp terminate” callback để save dữ liệu quan trọng; process có thể bị kill mà không cho bạn cơ hội cleanup mong muốn.

---

# 11. UIKit list/reuse/diffable data source

Cell reuse là object reuse, không phải data ownership. `prepareForReuse()` và configuration phải làm cell trở lại trạng thái phù hợp cho item mới.

Async image/task cần gắn với represented item và cancel khi reuse:

```swift
final class ImageCell: UICollectionViewCell {
    private var imageTask: Task<Void, Never>?

    override func prepareForReuse() {
        super.prepareForReuse()
        imageTask?.cancel()
        imageTask = nil
        imageView.image = nil
    }
}
```

Diffable snapshot dùng stable identity. Apply snapshot quá dày hoặc thay ID liên tục làm animation/state khó đoán và tốn work.

Compositional Layout giúp mô tả section/group/item adaptive; nhưng layout closure cũng cần nhẹ và deterministic.

---

# 12. UIKit memory/lifetime traps

Các cycle thường gặp:

- controller/model giữ closure, closure giữ controller/model;
- delegate được custom type khai báo strong thay vì weak khi ownership không thuộc delegate;
- `Timer`/display-link/observer/callback owner không được invalidate/remove theo lifecycle;
- Combine `AnyCancellable` được owner giữ trong set, sink closure lại strong-capture owner;
- child controller hoặc hosting controller bị add nhưng không remove đúng ownership.

Memory Graph nên được dùng để đọc retain path cụ thể. “Controller không deinit” không chứng minh nguyên nhân cho đến khi bạn xem ai retain nó.

---

# 13. SwiftUI → UIKit với Representable

`UIViewRepresentable`/`UIViewControllerRepresentable` là adapter lifecycle giữa declarative state và UIKit object identity.

```swift
struct CameraView: UIViewControllerRepresentable {
    let configuration: CameraConfiguration

    func makeUIViewController(context: Context) -> CameraViewController {
        CameraViewController(configuration: configuration)
    }

    func updateUIViewController(
        _ controller: CameraViewController,
        context: Context
    ) {
        controller.apply(configuration)
    }

    static func dismantleUIViewController(
        _ controller: CameraViewController,
        coordinator: Coordinator
    ) {
        controller.stopSession()
    }
}
```

`make...` tạo UIKit object cho representable identity; `update...` đồng bộ SwiftUI input mới vào object tồn tại; `dismantle...` cleanup resource khi adapter bị tháo.

Đừng khởi động lại camera/player/map controller trong mỗi `update...` nếu input không thực sự đổi.

---

# 14. Coordinator — delegate bridge và ownership

Coordinator thường nhận delegate/data-source callback từ UIKit rồi mutate Binding/Observable state.

```swift
struct PickerBridge: UIViewControllerRepresentable {
    @Binding var selection: Item?

    func makeCoordinator() -> Coordinator {
        Coordinator(selection: $selection)
    }

    final class Coordinator: NSObject, SomePickerDelegate {
        var selection: Binding<Item?>

        init(selection: Binding<Item?>) {
            self.selection = selection
        }
    }
}
```

Coordinator lifetime gắn với representable instance identity theo SwiftUI bridge semantics. Hãy kiểm retain graph: UIKit object có retain delegate không, coordinator có retain controller không, closure có capture parent state không.

Callback UIKit có thể đến trên queue/framework-defined context. Nếu cập nhật MainActor-isolated UI model, bridge isolation rõ thay vì assume main thread nếu contract không bảo đảm.

---

# 15. UIKit → SwiftUI với UIHostingController

```swift
let host = UIHostingController(rootView: ProfileView(model: model))
```

Nếu dùng như child controller, áp dụng containment đúng. Nếu `rootView` cần đổi, update root view hoặc tốt hơn truyền observable model để state thay đổi mà không reconstruct navigation/controller graph vô ích.

Self-sizing/Auto Layout cần để hosting view có constraint hợp lệ. Safe area và navigation bar ownership phải rõ: tránh SwiftUI tự mô tả navigation một lần rồi UIKit navigation controller lại mô tả thêm một stack khác mà không có boundary.

`UIHostingConfiguration` có thể hữu ích để dùng SwiftUI content trong UIKit list/cell ở OS hỗ trợ, nhưng identity/reuse vẫn phải được hiểu theo host UIKit.

---

# 16. Interoperability data-flow rule

Hybrid code dễ hỏng khi cả UIKit và SwiftUI đều tự nhận mình là source of truth.

Chọn một hướng cho mỗi fact:

```text
Domain/Feature state
        ↓
SwiftUI View ----adapter----> UIKit component
        ↑                         |
        └--------- event ----------┘
```

Hoặc UIKit controller là feature owner và SwiftUI chỉ render Binding/model được inject. Điều phải tránh là UIKit giữ một copy state, SwiftUI giữ copy khác và delegate cố sync hai chiều thủ công không có version/invariant.

---

# 17. Incremental migration UIKit ↔ SwiftUI

Rewrite toàn app hiếm khi là lựa chọn duy nhất. Migration an toàn thường theo seam:

- màn hình mới dùng SwiftUI nhưng host trong UIKit navigation;
- component UIKit đặc thù được wrap vào SwiftUI;
- domain/network/persistence layer được tách framework-neutral trước;
- route/navigation ownership được xác định để tránh hai navigation system tranh quyền;
- observability/analytics/test được giữ tương đương trước khi xóa implementation cũ.

Đo regression về accessibility, keyboard/focus, safe area, rotation, state restoration và performance; không chỉ screenshot happy path.

---

# 18. Architecture production — bắt đầu từ state/effect ownership

Một architecture hữu ích phải cho phép trả lời:

- source of truth của feature là gì;
- event nào mutate state;
- side effect được khởi tạo/cancel ở đâu;
- dependency đi vào từ đâu;
- UI framework type dừng ở boundary nào;
- persistence/network DTO map ở đâu;
- route/deep link được parse ở đâu;
- test behavior nào không cần launch UI.

Nếu sơ đồ layer đẹp nhưng không trả lời được task lifetime và source of truth, architecture vẫn yếu.

---

# 19. Vertical feature boundary

Thay vì toàn app chia `Views/Models/ViewModels/Services`, feature có thể là compile-time/ownership slice:

```text
Features/
  Catalog/
    CatalogView.swift
    CatalogModel.swift
    CatalogRoute.swift
    CatalogService.swift
    CatalogTests/
  Checkout/
  Profile/
Core/
  Networking/
  Persistence/
  DesignSystem/
```

Không phải mọi project cần structure này; lợi ích là code thay đổi cùng feature nằm gần nhau và module API có thể nhỏ.

---

# 20. Domain/Data/Presentation boundary có chọn lọc

Domain model nên tránh phụ thuộc transport/persistence/framework type khi domain sống lâu hơn implementation đó. DTO từ REST và managed object có thể map sang domain value.

Nhưng CRUD app nhỏ có thể dùng model trực tiếp nếu không có domain distinction thật. Abstraction phải trả rent: giảm coupling, tăng testability hoặc bảo vệ compatibility. Nếu chỉ forward method, nó tạo ceremony.

---

# 21. MVVM ở SwiftUI — dùng khi có lý do

SwiftUI `View` là lightweight description. Không cần 1 View = 1 ViewModel như luật.

ViewModel/feature model có giá trị khi:

- state machine/effect phức tạp;
- cần MainActor ownership lâu hơn local scalar state;
- feature được test độc lập view;
- nhiều subview chia shared feature state.

Massive ViewModel cũng là Massive View Controller phiên bản mới nếu nó chứa network, persistence, routing, analytics và mọi business rule.

---

# 22. Coordinator/Router/Reducer — chọn theo problem

Coordinator phù hợp UIKit navigation ownership. Router/state-driven navigation phù hợp SwiftUI khi route là data. Reducer architecture phù hợp state/action/effect phức tạp cần explicit transition/replay/test.

Không trộn ba pattern chỉ để “enterprise”. Với mỗi layer, ghi rõ responsibility và dependency direction.

---

# 23. Dependency Injection và composition root

Composition root dựng concrete dependency graph. Feature không nên tự tìm service qua global container nếu dependency là requirement.

Protocol chỉ cần khi abstraction/substitution thực sự có giá trị. Closure/function dependency, concrete fake hoặc lightweight struct dependency đôi khi đơn giản hơn protocol + mock generator.

Singleton không luôn xấu: system singleton như `URLSession.shared` có use case. Vấn đề là hidden mutable global state không kiểm soát lifetime/test isolation.

---

# 24. Modularization là dependency graph, không phải folder

SwiftPM target/module là compile-time boundary. Public API phải nhỏ; helper giữ `internal`. Tránh mega-Core mà mọi feature import.

Theo dõi cycle và fan-in/fan-out. Module quá nhỏ tạo build/dependency ceremony; module quá lớn mất isolation/ownership. Chọn seam theo team ownership, feature volatility, build bottleneck và reusable capability.

Binary XCFramework cần thêm concern về architecture slices, module stability, signing, privacy manifest và symbols. `BUILD_LIBRARY_FOR_DISTRIBUTION` có ý nghĩa với binary distribution, không phải toggle “tối ưu app”.

---

# 25. API evolution và internal package discipline

Ngay cả package nội bộ có nhiều consumer cũng cần semantic discipline. Breaking change cần migration plan; deprecation shim đôi khi rẻ hơn atomic migration.

```swift
@available(*, deprecated, message: "Use loadNew()")
func loadOld() { }
```

Public API nên document actor/isolation requirement, error semantics và availability, không chỉ parameter names.

---

# 26. Build system và compile-time performance

Compile time tăng bởi giant result builder expression, generic constraint sâu, generated code quá lớn và dependency graph xấu.

Cải thiện bằng cách đo build timing, chia expression hợp lý, thu nhỏ public API/module imports và tránh abstraction generic chỉ để giảm vài dòng code.

Debug/Release khác optimization. Bug chỉ Release có thể là race, lifetime timing hoặc unsafe interop; đừng mặc định compiler bug.

Swift 6.4 dùng Swift Build làm default SwiftPM build system; package/build issue cần xem dependency graph và compiler invocation thay vì chỉ “xóa DerivedData”.

---

# 27. Instruments — workflow đo trước sửa

Các tool quan trọng: Time Profiler, Allocations, Leaks, Network, Energy, Core Animation/hitch và SwiftUI instrumentation tương ứng Xcode version.

Workflow:

1. mô tả symptom bằng metric;
2. tạo reproduction;
3. đo baseline;
4. tìm hot allocation/call stack/layout/network;
5. thay đổi một hypothesis;
6. đo lại trên device/release-like build.

Memory growth không đồng nghĩa leak. Cache có thể hợp lệ nhưng vẫn gây memory pressure; leak có thể nhỏ nhưng tăng theo repeated flow.

---

# 28. Signpost và observability local

Khi một operation xuyên nhiều function nhưng Time Profiler khó nhìn business phase, dùng OSLog signpost/Points of Interest để đo duration có tên. Đừng log payload nhạy cảm chỉ để dễ debug.

Performance instrumentation nên có category/subsystem rõ để CI/lab và production telemetry cùng nói chung một vocabulary.

---

# 29. Networking production

Client production cần cancellation, timeout, HTTP semantics, cache policy, auth single-flight, retry/backoff + jitter và idempotency.

```text
request A -> 401
request B -> 401
         \-> shared refresh task
             -> token mới
             -> retry A/B theo policy
```

Certificate pinning có operational cost: cert/key rotation và failure recovery. Chỉ dùng khi threat model justify, không phải checklist security mặc định.

Mobile backend phải support version lag. Client tolerant decode, server backward compatibility và idempotent mutation design là reliability concern chứ không riêng networking code.

---

# 30. Persistence production và database concurrency

Schema là contract lâu dài với dữ liệu user. Test migration từ real/synthetic snapshots của các version cũ, không chỉ fresh database.

SwiftData `ModelActor`/Core Data background context giúp isolation, nhưng query/index/data-model design thường quyết định performance lớn hơn “chạy background”.

Tránh truyền mutable persistence object qua actor/context tùy ý. Object ID hoặc Sendable snapshot/value DTO làm boundary rõ hơn.

Offline-first cần outbox/operation queue, retry, conflict strategy, tombstone/delete semantics và sync cursor/version; cache response đơn thuần chưa phải offline-first.

---

# 31. Security và privacy

Không nhúng server secret vào binary. Client không phải trust boundary; authorization phải enforce ở backend.

Keychain cho credential/token; file nhạy cảm cần Data Protection phù hợp; ATS exception scope nhỏ; permission request theo context. Privacy manifest/disclosure và third-party SDK audit là release concern.

Jailbreak/root detection chỉ tăng signal/cost, không tạo trust tuyệt đối.

Dependency/SDK là supply-chain surface: kiểm maintainer, release cadence, transitive dependency, privacy behavior và exit strategy.

---

# 32. Accessibility, localization và adaptive UI

Senior UI phải chịu Dynamic Type lớn, locale text expansion, RTL, split view/multi-window, accessibility settings và input modality phù hợp platform.

VoiceOver semantic tree có thể khác visual tree. Custom control phải expose role/value/action đúng.

Dùng locale-aware format:

```swift
Text(price, format: .currency(code: "USD"))
```

Language, locale, calendar và timezone là bốn concern khác nhau.

---

# 33. Testing strategy production

Unit test pure behavior; integration test network/persistence boundary; UI test critical flow. Snapshot test hữu ích cho regression nhưng phải quản rendering variance.

Property-based thinking phù hợp parser/serializer/migration: encode→decode giữ invariant, migration giữ record, sort giữ multiset/order invariant. Fuzzing hữu ích cho untrusted/binary parser boundary.

Concurrency test phải ép cancellation/interleaving/single-flight/reentrancy, không chỉ chờ happy path.

---

# 34. CI/CD và release artifact

Pipeline điển hình: resolve dependency → build → static check → unit/integration test → selected UI test → archive → sign/export → upload TestFlight/App Store.

```bash
xcodebuild \
  -scheme MyApp \
  -destination 'platform=iOS Simulator,name=iPhone 17' \
  test
```

Quan trọng: test Debug simulator chưa đủ. Với risk cao, test archive/Release-like artifact, signing/entitlement và migration install từ version đang phát hành.

Không hard-code signing credential/token trong repo/log.

---

# 35. App startup, state restoration và process death

Startup path nên nhỏ: dựng dependency cần thiết, render sớm, defer noncritical work. Static/global initializer có thể chạy sớm ngoài ý định.

State restoration phải phân biệt transient UI/navigation và durable domain data. iOS có thể terminate process bất ngờ; dữ liệu quan trọng phải được persisted theo transaction phù hợp, không chờ callback “sắp terminate”.

---

# 36. Combine và legacy async boundary

Combine vẫn tồn tại nhiều codebase. Publisher/Subscriber/Operator/Scheduler/Cancellable cần hiểu để maintain.

```swift
publisher
    .map(transform)
    .removeDuplicates()
    .sink(
        receiveCompletion: { _ in },
        receiveValue: { value in }
    )
    .store(in: &cancellables)
```

Nếu `self` giữ cancellables và sink closure strong-capture `self`, hãy xem retain graph. Đặt boundary rõ khi bridge Combine ↔ async/await; đừng chuyển qua lại nhiều lần trong cùng feature.

---

# 37. Objective-C runtime interoperability

`NSObject`, `@objc`, `dynamic`, selector, KVC/KVO vẫn xuất hiện ở UIKit/legacy SDK. Không phải mọi Swift type expose sang Objective-C được; generic Swift và enum associated value là ví dụ.

Mixed-language app dùng bridging header/module import tùy hướng. Runtime dynamic feature có trade-off: ít static checking hơn, behavior phụ thuộc selector/KVC key và Objective-C lifetime conventions.

---

# 38. C/C++ boundary

Pointer/count API là unsafe boundary; lifetime, alignment, mutability và ownership phải document. Swift 6.x tiếp tục thêm memory-safe systems API như `Span` và Swift 6.4 mở rộng interop với C++20 `std::span`.

Giữ foreign/unsafe adapter nhỏ; convert sang Swift-safe value càng sớm càng tốt. Parser binary/untrusted input cần bounds validation/fuzzing.

---

# 39. Xcode 27 / Swift 6.4 migration risk

Xcode 27 + Swift 6.4 là baseline hiện tại của library. SwiftUI state/builder internals và observation/tooling tiếp tục tiến hóa; code không nên phụ thuộc undocumented reflection/result-builder implementation.

Swift 6.4 tiếp tục mở rộng ownership, interop, testing và build tooling. Senior adoption strategy là đọc release notes + Swift Evolution proposal liên quan, chạy migration/test/performance baseline, rồi bật feature có chủ đích. “Compiler mới nên bật mọi thứ cùng lúc” không phải migration plan.

---

# 40. Incident mindset và rollback constraint của mobile

Khi crash/latency tăng, phân đoạn theo app version, OS, device, feature flag, endpoint; xem symbolicated stack/metric/log; reproduce nhỏ nhất; rồi patch.

Mobile rollback chậm hơn web vì binary cũ nằm trên device. Backend backward compatibility, remote kill switch/feature flag cho risk cao và staged rollout giúp giảm blast radius. Flag phải có owner/expiry; không để codebase thành tổ hợp hàng chục flag vĩnh viễn.

---

# 41. Senior review checklist

Review semantics trước style:

- state/source of truth có một owner rõ không;
- closure/reference graph có cycle/lifetime bất thường không;
- task có owner/cancellation policy không;
- invariant có bị giữ qua `await` mà không revalidate không;
- Sendable/isolation annotation có phản ánh ownership thật không;
- SwiftUI identity có ổn định không;
- UIKit lifecycle callback có dùng đúng responsibility không;
- containment/representable/hosting ownership có cleanup đúng không;
- network mutation có retry/idempotency risk không;
- persistence migration/context boundary có test không;
- API availability/backward compatibility có fallback không;
- security/privacy/logging có leak secret/PII không;
- performance claim có measurement không;
- release artifact/migration path có được test không.

Nếu reviewer phải mất rất lâu mới xác định state/effect/dependency flow, code có thể compile nhưng architecture chưa đạt mức senior maintainability.

## Gate trước khi sang Master

Bạn phải có khả năng lấy một hybrid app SwiftUI + UIKit thật và vẽ được: object ownership graph, view/controller lifecycle, task graph, actor/isolation boundary, state source-of-truth, network/persistence boundary và module dependency graph. Master sẽ không dạy lại các graph này; nó dùng chúng để giải quyết version evolution, ABI/library evolution, large-scale reliability, performance/security/release governance.