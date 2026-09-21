# Swift & iOS Master Note — Intermediate

> Mục tiêu: chuyển từ “biết viết màn hình và gọi API” sang “xây được feature có ownership rõ, concurrency đúng, state flow giải thích được, test được và bảo trì được”.
>
> Prerequisite: đã hiểu Beginner, đặc biệt value/reference semantics, closure escaping/capture, ARC, `async`/`await`, `@State`/`@Binding`, UIKit lifecycle cơ bản và network/persistence failure.

Intermediate không cố biến mọi feature thành architecture nhiều layer. Trọng tâm là **reasoning**: ai sở hữu state, task sống bao lâu, mutable data được isolate ở đâu, side effect bắt đầu/kết thúc khi nào, và boundary nào cần abstraction.

---

# 1. Type system ở mức dùng để thiết kế API

## 1.1 Value semantics, reference semantics và copy-on-write

```swift
struct Profile {
    var name: String
}

var a = Profile(name: "A")
var b = a
b.name = "B"
```

`a` và `b` độc lập về semantics. Collection chuẩn như `Array`, `Dictionary`, `String` có thể chia sẻ storage và copy khi mutation, nhưng đó là optimization; public mental model vẫn là value semantics.

Reference type có identity và shared mutable state. Khi nhiều owner cùng thấy một class instance, bạn phải trả lời cả hai câu hỏi: ai giữ lifetime và ai được phép mutate.

## 1.2 `Equatable`, `Hashable`, `Comparable`, `Identifiable`

```swift
struct Product: Identifiable, Hashable {
    let id: UUID
    let name: String
}
```

`Identifiable.id` phải đại diện stable identity của entity trong khoảng lifetime phù hợp. Nếu ID thay đổi theo vị trí array, diffing/navigation/state restoration có thể gắn state vào sai item.

## 1.3 Generic, `where` và capability-oriented API

```swift
func merge<C1: Collection, C2: Collection>(
    _ lhs: C1,
    _ rhs: C2
) -> [C1.Element]
where C1.Element == C2.Element {
    Array(lhs) + rhs
}
```

Chỉ yêu cầu capability thực sự cần. Nếu function chỉ iterate một lần, `Sequence` có thể phù hợp hơn `Array`; nếu cần random access, constraint mạnh hơn mới có ý nghĩa.

## 1.4 Associated type, `some` và `any`

```swift
protocol Repository {
    associatedtype Entity
    func fetchAll() async throws -> [Entity]
}
```

`some P` là opaque type: API che concrete type nhưng vẫn giữ một concrete type ổn định cho compiler. `any P` là existential value có thể chứa các concrete conformer khác nhau ở runtime.

```swift
func makeView() -> some View {
    Text("Hello")
}

let analytics: any AnalyticsService
```

Đừng dùng existential chỉ vì syntax ngắn. Generic/opaque type giữ nhiều static type information hơn; existential phù hợp khi runtime heterogeneity/substitution là requirement thật.

---

# 2. Optional, Result và error boundary

Optional mô hình hóa “có hoặc không có value”. `Result<Success, Failure>` mô hình hóa success/failure thành value. `async throws` thường tự nhiên hơn `Result` cho async call chain, nhưng Result hữu ích khi cần lưu kết quả, bridge callback hoặc đưa result qua state machine.

```swift
let result: Result<User, APIError>
```

Đừng flatten mọi error thành `Error` quá sớm nếu UI/domain cần phân biệt unauthorized, validation, offline hay server failure. Ngược lại, đừng tạo hàng chục enum error chỉ để “type-safe” nếu caller không có behavior khác nhau.

---

# 3. Protocol extension và dispatch trap

```swift
protocol Named {
    func name() -> String
}

extension Named {
    func name() -> String { "default" }
}
```

Nếu method là protocol requirement, conforming type override được qua protocol witness. Nếu method chỉ tồn tại ở extension nhưng không nằm trong requirement, dispatch qua existential có thể khác kỳ vọng. Khi polymorphism là intent, đưa operation vào protocol contract.

Conditional conformance cho phép type generic conform khi Element thỏa điều kiện; đây là nền tảng của nhiều API standard library.

---

# 4. Property wrapper, result builder và macro

Property wrapper đóng gói storage/access behavior:

```swift
@propertyWrapper
struct Clamped<Value: Comparable> {
    private var value: Value
    let range: ClosedRange<Value>

    var wrappedValue: Value {
        get { value }
        set { value = min(max(newValue, range.lowerBound), range.upperBound) }
    }

    init(wrappedValue: Value, _ range: ClosedRange<Value>) {
        self.range = range
        self.value = min(max(wrappedValue, range.lowerBound), range.upperBound)
    }
}
```

Result builder đứng sau nhiều DSL declarative. Macro là compile-time transformation; `@Observable` và `@Model` là ví dụ quan trọng. Khi diagnostic “magic”, xem macro expansion/generated interface trong Xcode thay vì đoán.

---

# 5. Swift concurrency — mental model trước API

Swift concurrency có bốn trục cần tách:

- **task lifetime**: công việc nào là parent/child, ai cancel ai;
- **suspension**: `await` cho phép task tạm dừng nhưng không đồng nghĩa đổi thread;
- **isolation**: mutable state thuộc actor/global actor nào;
- **sendability**: value nào được phép đi qua isolation boundary.

Nếu bốn trục này rõ, phần lớn compiler diagnostic Swift 6 trở nên có lý do thay vì “annotation ceremony”.

## 5.1 Structured concurrency với `async let`

```swift
async let profile = api.profile()
async let messages = api.messages()

let (p, m) = try await (profile, messages)
```

Child task gắn lifetime với lexical scope. Scope không kết thúc hợp lệ khi child task còn bị bỏ quên; error/cancellation có quan hệ rõ hơn unstructured task.

## 5.2 Dynamic child task với TaskGroup

```swift
let values = try await withThrowingTaskGroup(of: Int.self) { group in
    for id in ids {
        group.addTask {
            try await loadValue(id)
        }
    }

    var output: [Int] = []
    for try await value in group {
        output.append(value)
    }
    return output
}
```

Task group phù hợp fan-out động. Đừng tạo vô hạn task chỉ vì API cho phép; concurrency cần bounded theo resource/backend constraints khi input lớn.

## 5.3 `Task {}` là unstructured task, không phải child scope tự động

```swift
let task = Task {
    await model.refresh()
}
```

`Task {}` hữu ích để bridge synchronous context vào async hoặc tạo task có owner rõ. Nhưng task này không được lexical scope chờ/cancel giống child task của `async let`/group. Nếu lưu task trong model, model phải có policy cancel/supersede.

```swift
private var searchTask: Task<Void, Never>?

func search(_ query: String) {
    searchTask?.cancel()
    searchTask = Task {
        try? await Task.sleep(for: .milliseconds(300))
        guard !Task.isCancelled else { return }
        await performSearch(query)
    }
}
```

## 5.4 `Task.detached` là escape hatch

Detached task không nên là “background thread button”. Nó tách khỏi nhiều context mà `Task {}` kế thừa. Dùng khi thật sự cần independent unstructured work và bạn hiểu priority/task-local/isolation implications. Với app feature bình thường, structured task hoặc `Task {}` có owner rõ thường tốt hơn.

## 5.5 Cancellation là cooperative

`cancel()` không giết code tùy ý. Nó đặt cancellation state; API suspension point hoặc code của bạn cần kiểm:

```swift
try Task.checkCancellation()
```

Cancellation thường không phải “error UX”. Khi user đổi search query hay rời màn hình, task cũ bị cancel là control flow hợp lệ; đừng hiện alert “CancellationError” như server failure.

## 5.6 Priority không phải QoS guarantee tuyệt đối

Task priority là scheduling hint và có inheritance/escalation semantics. Không thiết kế correctness dựa trên assumption “high priority chắc chắn chạy trước low priority”. Correctness phải độc lập scheduler timing.

---

# 6. Actor isolation — mutable state thuộc về đâu

Actor serialize access tới actor-isolated mutable state theo concurrency model.

```swift
actor TokenStore {
    private var token: String?

    func set(_ token: String?) {
        self.token = token
    }

    func get() -> String? {
        token
    }
}
```

Gọi actor member từ domain khác thường cần `await` vì call có thể suspend để executor chạy actor job.

## 6.1 Actor không phải lock syntax mới

Actor bảo vệ isolation, nhưng method actor có thể suspend. Khi gặp `await`, actor có thể xử lý công việc khác trước khi method tiếp tục. Vì vậy invariant đọc trước `await` có thể không còn đúng sau `await`.

```swift
actor Inventory {
    private var stock = 1

    func reserve() async throws {
        guard stock > 0 else { throw StockError.empty }
        await validateExternally()

        // state có thể đã thay đổi trong lúc suspend
        guard stock > 0 else { throw StockError.empty }
        stock -= 1
    }
}
```

Đây là **actor reentrancy**, không phải data race. Compiler ngăn unsynchronized access nhưng không tự chứng minh business invariant qua suspension point.

## 6.2 `@MainActor`

UI-facing observable state thường thuộc MainActor:

```swift
@MainActor
@Observable
final class HomeModel {
    var items: [Item] = []
    var state: LoadState = .idle

    func load() async {
        state = .loading
        do {
            items = try await api.fetchItems()
            state = .loaded
        } catch is CancellationError {
            // giữ/khôi phục state theo product policy
        } catch {
            state = .failed(error)
        }
    }
}
```

`@MainActor` là isolation contract, không chỉ là synonym của `DispatchQueue.main.async`.

## 6.3 `nonisolated`

Member không cần actor-isolated state có thể được thiết kế `nonisolated` khi semantics cho phép. Không thêm `nonisolated` chỉ để compiler ngừng báo; hãy đảm bảo implementation không lén đọc mutable actor state.

## 6.4 Global actor

`@MainActor` là global actor có sẵn. Custom global actor có thể hợp lý cho một domain isolation đặc biệt, nhưng đừng tạo một actor toàn app để “hết race”; isolation boundary phải phản ánh ownership thật.

---

# 7. `Sendable` và crossing isolation boundary

`Sendable` biểu diễn value có thể transfer giữa concurrency domains an toàn theo model của compiler.

```swift
struct UserSnapshot: Sendable {
    let id: UUID
    let name: String
}
```

Immutable value type gồm field Sendable thường tự nhiên. Mutable class shared reference khó hơn vì hai isolation domain có thể mutate cùng object.

`@unchecked Sendable` là lời hứa của programmer rằng synchronization/invariant bên trong đã đúng. Nó không “làm object thread-safe”; nó tắt một phần kiểm tra compiler. Mỗi `@unchecked Sendable` nên có lý do/invariant được review.

## 7.1 `@Sendable` closure

Closure được chạy ở concurrency context khác có thể cần `@Sendable`. Compiler kiểm capture để tránh closure mang mutable non-Sendable state qua boundary.

```swift
func perform(_ operation: @Sendable @escaping () async -> Void) {
    Task { await operation() }
}
```

Nếu compiler phàn nàn capture, đừng mặc định thêm `@unchecked`. Hãy hỏi capture có thể chuyển thành immutable snapshot/value hay dependency actor-isolated không.

## 7.2 Snapshot pattern

Thay vì gửi mutable reference qua actor boundary, tạo Sendable snapshot:

```swift
struct ProfileSnapshot: Sendable {
    let id: UUID
    let displayName: String
}
```

Pattern này làm data flow dễ reasoning và tách persistence/UI object lifetime khỏi async worker.

---

# 8. Swift 6.x approachable concurrency và project settings

Swift 6.x tăng compile-time data-race checking. Từ Swift 6.2, language/tooling tiếp tục làm concurrency approachable hơn với default actor isolation option và explicit opt-in concurrency ở nơi phù hợp. Điều quan trọng là **language mode và build setting là một phần semantics project**.

Khi migrate code cũ, ghi lại ít nhất: Xcode version, Swift compiler version, Swift language mode, deployment target, default actor isolation setting và các upcoming/strict concurrency feature đang bật. Cùng source có thể cho diagnostic khác khi những setting này khác nhau.

Không “fix migration” bằng cách rải `@MainActor`/`nonisolated`/`@unchecked Sendable` theo compiler error. Phân loại ownership trước rồi annotate boundary tương ứng.

---

# 9. AsyncSequence, AsyncStream và event stream

`AsyncSequence` mô hình hóa nhiều value đến theo thời gian:

```swift
for await event in events {
    guard !Task.isCancelled else { break }
    handle(event)
}
```

`AsyncStream`/`AsyncThrowingStream` hữu ích bridge delegate/callback API. Khi bridge, phải có policy buffering, termination và cleanup producer khi consumer cancel; nếu không producer có thể chạy mãi.

Swift 6.4 tiếp tục tăng integration giữa Observation và async change streams. Dù API mới thuận tiện hơn, event stream và UI observation vẫn là hai abstraction khác nhau: UI dependency tracking không tự nhiên trở thành domain event log.

---

# 10. Continuation — bridge legacy callback có kỷ luật

```swift
func load() async throws -> Data {
    try await withCheckedThrowingContinuation { continuation in
        legacyLoad { result in
            continuation.resume(with: result)
        }
    }
}
```

Continuation phải được resume đúng semantics một lần. Missing resume làm task treo; double resume là bug. Checked continuation giúp phát hiện nhiều lỗi nhưng không thay ownership/cancellation design.

Nếu legacy operation có cancel token, bridge nên propagate cancellation khi có thể thay vì chỉ đổi callback thành `await` về mặt syntax.

---

# 11. SwiftUI state — source of truth trước property wrapper

SwiftUI state bug thường không phải thiếu wrapper, mà do cùng một fact có nhiều owner hoặc view identity không như người viết tưởng.

Hãy phân loại:

- local presentation state: sheet mở, tab chọn, text đang edit;
- feature state: loading/result/filter/navigation của feature;
- domain state: business truth;
- persisted/server state: nguồn dữ liệu durable/remote;
- derived state: tính từ source khác.

Đừng lưu lại derived state nếu có thể tính rẻ và deterministic.

---

# 12. `@State` — storage gắn với view identity

```swift
struct SearchView: View {
    @State private var query = ""
    @State private var model = SearchModel()

    var body: some View { ... }
}
```

`View` struct được tạo lại nhiều lần; `@State` storage được SwiftUI giữ theo view identity. Vì vậy không reasoning “struct bị init lại thì state chắc reset”. State reset khi identity/lifetime của view thay đổi theo tree semantics.

Với Xcode 27, `State` implementation tiếp tục được hiện đại hóa; đừng dựa vào undocumented detail như “initializer expression chắc chạy mỗi body recomputation”. Hãy dựa vào public ownership/lifetime semantics.

---

# 13. `@Binding` — capability mutate state của owner khác

```swift
struct NameField: View {
    @Binding var name: String

    var body: some View {
        TextField("Name", text: $name)
    }
}
```

Binding không copy state và cũng không trở thành owner. Nó là getter/setter projection. Khi binding chain quá sâu, đó có thể là dấu hiệu feature boundary/state ownership cần xem lại.

---

# 14. Observation với `@Observable`

```swift
@Observable
final class CartModel {
    var products: [Product] = []
    var coupon: Coupon?

    var total: Decimal {
        calculateTotal(products, coupon: coupon)
    }
}
```

Observation track property dependency mà view đọc. Điều này giúp invalidation granular hơn broad notification model cũ trong nhiều trường hợp.

Observable reference vẫn là class: ownership/lifetime và shared mutation vẫn cần thiết kế. `@Observable` không biến class thành value type và không tự làm nó concurrency-safe.

---

# 15. `@Bindable` — tạo Binding vào Observable model

Khi child cần binding trực tiếp tới property của observable model, `@Bindable` tạo projected binding surface:

```swift
struct ProfileEditor: View {
    @Bindable var model: ProfileModel

    var body: some View {
        TextField("Name", text: $model.name)
    }
}
```

`@Bindable` không sở hữu model. Owner vẫn phải được quyết định ở parent/composition root.

---

# 16. Environment và dependency scope

```swift
@Environment(CartModel.self) private var cart
```

Environment phù hợp dependency/context scoped theo view subtree. Nhưng nếu một domain object không thể hoạt động thiếu API client, constructor injection thường thể hiện invariant tốt hơn giấu dependency trong environment global.

Một pattern tốt: App/composition root dựng concrete dependency; feature root nhận dependency; environment chỉ dùng cho những thứ thực sự hợp với tree scope.

---

# 17. Legacy SwiftUI wrapper mapping

Codebase cũ có thể dùng:

- `ObservableObject` + `@Published`;
- `@StateObject` để view sở hữu reference object;
- `@ObservedObject` khi object do nơi khác sở hữu;
- `@EnvironmentObject` cho shared object qua tree.

Đừng migrate chỉ bằng search-replace. Chuyển sang Observation cần giữ nguyên ownership/lifetime. Mental model cũ “StateObject owns / ObservedObject borrows” vẫn hữu ích để đọc legacy, nhưng API mới biểu diễn bằng `@State` + observable reference và các projection phù hợp.

---

# 18. Derived state và state machine

Bad state:

```swift
var isLoading = false
var hasError = false
var isEmpty = false
```

Có nhiều combination vô nghĩa. Enum state machine làm invariant explicit:

```swift
enum ScreenState {
    case idle
    case loading
    case loaded([Item])
    case empty
    case failed(APIError)
}
```

Nếu `canCheckout` luôn tính từ cart/address, hãy để computed property thay vì lưu thêm Boolean phải sync thủ công.

---

# 19. View identity, conditional tree và `.id`

State lifetime phụ thuộc identity. Hai branch conditional có thể tạo identity/lifetime khác:

```swift
if isLoggedIn {
    HomeView()
} else {
    LoginView()
}
```

`.id(...)` thay identity chủ động và có thể reset state/task. Đừng dùng `.id(UUID())` như “force refresh”; nó thường che data-flow bug và phá state continuity.

List/ForEach identity cũng phải là domain-stable ID, không phải index nếu data reorder/insert/delete.

---

# 20. `.task` và task lifetime theo view

```swift
.task {
    await model.load()
}

.task(id: query) {
    await model.search(query)
}
```

Task modifier gắn work vào view lifetime/identity và có cancellation semantics khi view/task identity đổi. Đây là idiom tốt cho screen-scoped load/search.

Nhưng business operation cần sống lâu hơn screen không nên vô tình bị sở hữu bởi view. Ví dụ upload phải tiếp tục khi user rời màn hình có thể cần service/background URLSession owner khác.

---

# 21. SwiftUI layout sâu hơn

SwiftUI layout là negotiation parent → child → placement. `frame` tham gia proposal/constraint chứ không đơn giản mutate frame như UIKit.

Container quan trọng: `ScrollView`, `LazyVStack`, `LazyHStack`, `LazyVGrid`, `Grid`, `List`, `Form`.

`GeometryReader` không phải default solution. Ưu tiên layout protocol, alignment, container-relative sizing và built-in adaptive container khi phù hợp.

Custom `Layout` hữu ích khi parent cần đo/place nhiều child theo thuật toán riêng.

---

# 22. Navigation là state

```swift
enum Route: Hashable {
    case product(UUID)
    case settings
}

@Observable
final class Router {
    var path: [Route] = []
}
```

```swift
NavigationStack(path: $router.path) {
    HomeView()
        .navigationDestination(for: Route.self) { route in
            switch route {
            case .product(let id): ProductView(id: id)
            case .settings: SettingsView()
            }
        }
}
```

Route-as-data giúp deep link, restoration và test. Router không nên trở thành nơi chứa business logic.

---

# 23. Networking layer có cấu trúc

View không nên tự build URL, auth header, status mapping và decode lặp lại.

```swift
struct Endpoint<Response: Decodable> {
    let path: String
    let method: HTTPMethod
}

protocol HTTPClient {
    func send<Response: Decodable>(
        _ endpoint: Endpoint<Response>
    ) async throws -> Response
}
```

Client production phân tách request construction, transport, HTTP validation, decoding, auth, retry/cancellation, cache và logging.

```swift
var request = URLRequest(url: url)
request.httpMethod = "POST"
request.timeoutInterval = 30
request.setValue("application/json", forHTTPHeaderField: "Content-Type")
request.httpBody = try JSONEncoder().encode(body)
```

`URLSessionConfiguration` quyết định cache, cookie, timeout, connectivity behavior và nhiều policy khác.

---

# 24. Retry, idempotency và authentication coordination

Không retry mù quáng mọi failure. Network offline, timeout, HTTP 429, HTTP 500 và validation 400 có policy khác nhau.

GET thường idempotent; POST tạo resource có thể duplicate nếu retry sau timeout khi server đã xử lý request đầu. Với mutation quan trọng, backend/client nên có idempotency strategy nếu hệ thống hỗ trợ.

Token refresh phải tránh refresh storm. Nếu 10 request cùng nhận 401, thường chỉ nên có một refresh in-flight và các request khác chờ kết quả thay vì 10 refresh độc lập.

---

# 25. Codable và tolerant boundary

```swift
let decoder = JSONDecoder()
decoder.keyDecodingStrategy = .convertFromSnakeCase
decoder.dateDecodingStrategy = .iso8601
```

Tách transport DTO khỏi domain model khi server schema và business semantics khác nhau:

```swift
struct UserDTO: Decodable { ... }
struct User { ... }
```

Server enum có thể thêm case trong tương lai. Nếu API contract cho phép forward evolution, client cần unknown/fallback strategy thay vì crash/decode fail toàn payload khi gặp giá trị mới.

---

# 26. Persistence: SwiftData và Core Data mental model

SwiftData:

```swift
@Model
final class TaskItem {
    @Attribute(.unique) var id: UUID
    var title: String
    var isDone: Bool
}
```

Persistence phải nghĩ như database: schema, unique/index, relationship, delete rule, transaction, migration, query shape và concurrency.

Core Data vẫn rất phổ biến. Các khái niệm cần nắm: persistent container/store, `NSManagedObjectContext`, managed object identity, fetch request, relationship, merge policy, background context và migration.

Đừng truyền managed object mutable tùy ý giữa queue/context. Khi crossing boundary, object ID hoặc immutable snapshot thường an toàn hơn.

---

# 27. SwiftData query/observation và boundary

`@Query` ergonomic cho UI đơn giản. Nhưng feature có sync/domain rule phức tạp không nên để persistence query tràn khắp view tree.

SwiftData mới tiếp tục mở rộng query/index/history/observation capability. API tiện hơn không thay requirement xác định source of truth và migration policy.

Repository/store abstraction chỉ có giá trị nếu nó che data-source/domain boundary thật; đừng tạo repository chỉ để mỗi method forward thẳng một call rồi tăng ceremony.

---

# 28. Dependency injection và composition root

```swift
final class ProductService {
    private let client: any HTTPClient

    init(client: any HTTPClient) {
        self.client = client
    }
}
```

Constructor injection làm dependency bắt buộc explicit. Không phải dependency nào cũng cần protocol; concrete type có thể inject/test bằng fake wrapper/function nếu đơn giản hơn.

Composition root là nơi app dựng concrete implementation và nối graph. Nếu mỗi feature tự đọc singleton global, dependency flow trở nên ẩn và test/lifetime khó kiểm soát.

---

# 29. Architecture: chọn boundary, không sưu tầm pattern

MVC có thể tốt nếu controller nhỏ. MVVM hữu ích khi presentation state/effect đủ phức tạp; SwiftUI view không bắt buộc có ViewModel 1:1. Reducer/unidirectional architecture phù hợp state machine nhiều action/effect và team cần convention explicit.

Một architecture tốt trả lời được:

- source of truth ở đâu;
- mutation xảy ra ở đâu;
- async effect do ai sở hữu;
- dependency vào feature bằng cách nào;
- navigation thuộc layer nào;
- persistence/network DTO được map ở boundary nào;
- test behavior ở đâu.

Nếu phải tạo `BaseViewModel`, `BaseUseCase`, `BaseRepository` chỉ để mọi file “đúng template”, architecture đang phục vụ pattern thay vì product.

---

# 30. UIKit trung cấp — layout, reuse và lifecycle consequences

Auto Layout:

```swift
titleLabel.translatesAutoresizingMaskIntoConstraints = false
NSLayoutConstraint.activate([
    titleLabel.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 16),
    titleLabel.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -16),
    titleLabel.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 16)
])
```

Content hugging/compression resistance giải quyết conflict khi intrinsic size cạnh tranh.

Diffable data source dùng stable identity:

```swift
var snapshot = NSDiffableDataSourceSnapshot<Section, Item.ID>()
snapshot.appendSections([.main])
snapshot.appendItems(items.map(\.id))
dataSource.apply(snapshot, animatingDifferences: true)
```

Cell reuse yêu cầu cancel/reset async image/task và mọi visual state không còn hợp lệ khi cell được reuse.

---

# 31. SwiftUI ↔ UIKit interoperability trung cấp

```swift
struct CameraView: UIViewControllerRepresentable {
    func makeUIViewController(context: Context) -> CameraViewController {
        CameraViewController()
    }

    func updateUIViewController(
        _ uiViewController: CameraViewController,
        context: Context
    ) {
        // sync SwiftUI state -> UIKit object
    }

    func makeCoordinator() -> Coordinator {
        Coordinator()
    }
}
```

Coordinator thường bridge delegate/callback UIKit → SwiftUI state. Đừng để `update...` tạo lại controller/resource nặng; `make...` tạo object, `update...` đồng bộ thay đổi.

UIKit host SwiftUI:

```swift
let host = UIHostingController(rootView: ProfileView())
```

Nếu add child controller thủ công, phải tuân view-controller containment lifecycle. Advanced sẽ đi sâu.

---

# 32. App lifecycle, scene lifecycle và background work

SwiftUI app dùng `App`/`Scene`; UIKit legacy dùng `UIApplicationDelegate`/`UISceneDelegate`.

```swift
@Environment(\.scenePhase) private var scenePhase
```

`active`, `inactive`, `background` là lifecycle state, không phải lời hứa app được chạy bao lâu khi background.

BackgroundTasks, background URLSession, location/audio có rule/capability khác nhau. Nếu operation cần survive process suspension/termination, thiết kế phải dựa đúng system API, không chỉ giữ một `Task` trong memory.

---

# 33. Notification và deep link

Local notification được schedule trên device; remote push đi qua APNs/provider server. Permission, token lifecycle, foreground handling và user action routing là concern riêng.

Universal Link thường phù hợp web-to-app hơn custom URL scheme, nhưng cần Associated Domains và `apple-app-site-association` đúng. Parse deep link thành typed route/command sớm thay vì truyền raw string xuyên feature.

---

# 34. Testing async/state có tính deterministic

Test pure logic nhanh trước. Swift Testing:

```swift
@Suite
struct PriceTests {
    @Test(arguments: [
        (100, 0.1, 90),
        (200, 0.2, 160)
    ])
    func discount(input: Int, rate: Double, expected: Int) {
        #expect(calculate(input, rate) == expected)
    }
}
```

Async:

```swift
@Test
func loadUser() async throws {
    let user = try await service.loadUser()
    #expect(user.id == expectedID)
}
```

Inject time/UUID/random/filesystem/network dependency nếu behavior phụ thuộc chúng. Test không nên sleep vài giây để “chờ async”; dùng controllable dependency/clock/expectation/state transition.

Concurrency test cần có case cancellation, duplicate request, refresh single-flight và actor reentrancy, không chỉ happy path.

---

# 35. Diagnostics và sanitizer

Xcode Memory Graph tìm retain path. Address Sanitizer hữu ích đặc biệt ở unsafe/C/C++ boundary. Thread Sanitizer phát hiện runtime race ở các đường code thực thi; Swift 6 isolation checking ngăn nhiều race ở compile time. Hai lớp bổ sung nhau.

Main Thread Checker vẫn hữu ích cho UIKit/legacy API. Với code Swift concurrency mới, actor isolation là mental model chính.

---

# 36. Logging và error strategy

Dùng `Logger`/OSLog theo category/subsystem; không log token/password/PII. Error developer cần diagnostic detail; error user cần actionable message. Đừng đưa raw `localizedDescription` của mọi infrastructure error thẳng lên UI.

Metrics/crash reporting là production concern; Advanced sẽ đi vào signpost, Instruments và field telemetry.

---

# 37. SwiftPM và module boundary

Package target tạo compile-time module boundary thật. Tránh dependency cycle và “Core” mega-module mà mọi feature import.

Một module khỏe mạnh có cohesion rõ, public API nhỏ, dependency direction có chủ đích. Swift 6.4 dùng Swift Build làm default SwiftPM build system; package đa nền tảng cần `platforms`, conditional dependency và `#if canImport` chỉ ở boundary phù hợp.

---

# 38. Availability và conditional compilation

```swift
#if DEBUG
let endpoint = URL(string: "https://staging.example.com")!
#endif

if #available(iOS 27, *) {
    // runtime API mới
}
```

`#if` chọn source lúc compile; `#available` chọn branch runtime. Đừng dùng compile-time condition để giả lập runtime availability.

---

# 39. Intermediate capstone — feature có ownership hoàn chỉnh

Hãy xây một feature Catalog/Search đủ các path: list + detail + search debounce + pagination + cache/persistence + login token mock + deep link.

Yêu cầu architecture không phải số layer mà là bạn phải chỉ được trên code:

1. owner của observable feature state;
2. task search nào bị cancel khi query đổi;
3. state nào actor-isolated và vì sao;
4. data nào crossing actor boundary và có Sendable semantics ra sao;
5. UI state nào derived, state nào persisted/server source of truth;
6. network retry/auth refresh nằm ở đâu;
7. SwiftData/Core Data object có crossing context/isolation không;
8. UIKit bridge nếu có, coordinator/lifetime nằm ở đâu;
9. test cancellation, error, duplicate request và state transition thế nào.

Một cấu trúc feature có thể theo chiều dọc:

```text
FeatureCatalog/
  CatalogView.swift
  CatalogModel.swift
  CatalogRoute.swift
  CatalogService.swift
  CatalogRepository.swift   // chỉ nếu data-source abstraction có giá trị
  Models/
  Tests/
```

## Checklist trước khi sang Advanced/Senior

Bạn phải giải thích được sự khác nhau giữa structured child task, `Task {}` và detached task; actor reentrancy; MainActor isolation; `Sendable`/`@Sendable`; cancellation; `@State` ownership; `@Binding` projection; `@Bindable`; observable reference lifetime; view identity; `.task(id:)`; persistence context boundary; HTTP retry/idempotency; và vì sao architecture tốt làm state/effect/dependency flow rõ chứ không chỉ nhiều protocol.

Nếu một compiler concurrency warning chỉ được “sửa” bằng annotation mà bạn không giải thích được ownership/isolation trước và sau thay đổi, hãy xem đó là kiến thức chưa hoàn thành chứ không phải compiler khó tính.