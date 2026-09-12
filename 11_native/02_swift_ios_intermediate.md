# Swift & iOS Master Note — Intermediate

> Mục tiêu: chuyển từ “biết viết màn hình và gọi API” sang “xây được iOS app có cấu trúc, data flow rõ, concurrency đúng, test được và bảo trì được”.

# 1. Swift type system ở mức thực dụng

## 1.1 Value semantics, reference semantics và copy-on-write

`struct`/`enum` có value semantics; `class` có reference semantics. Đây không chỉ là kiến thức phỏng vấn mà ảnh hưởng trực tiếp đến state management, mutation và concurrency.

```swift
struct Profile {
    var name: String
}

var a = Profile(name: "A")
var b = a
b.name = "B"
```

`a` không đổi. Với class thì cả hai reference có thể nhìn thấy mutation của cùng object.

Collection chuẩn như `Array`, `Dictionary`, `String` thường dùng copy-on-write: nhiều value có thể chia sẻ storage cho đến khi một bên mutate. Bạn vẫn phải suy nghĩ theo value semantics; đừng dựa vào implementation detail để viết logic.

## 1.2 `Equatable`, `Hashable`, `Comparable`, `Identifiable`

Các protocol chuẩn này xuất hiện khắp API.

```swift
struct Product: Identifiable, Hashable {
    let id: UUID
    let name: String
}
```

`Hashable` cho phép dùng trong `Set`, key của dictionary và nhiều API navigation. `Identifiable` cung cấp stable identity cho UI/data diffing. Stable identity phải đại diện entity, không phải vị trí hiện tại trong array.

## 1.3 Generic, associated type và opaque type

```swift
protocol Repository {
    associatedtype Entity
    func fetchAll() async throws -> [Entity]
}
```

Protocol có associated type khó dùng như existential trong một số thiết kế; Swift hiện đại hỗ trợ `any Protocol` rõ hơn:

```swift
let service: any AnalyticsService
```

`some Protocol` là opaque type: caller biết có một concrete type ổn định nhưng không biết type nào.

```swift
func makeView() -> some View {
    Text("Hello")
}
```

`any P` và `some P` không tương đương. `any P` là existential box/interface value; `some P` giữ một hidden concrete type.

---

# 2. Advanced Optional, Pattern Matching và Result

Optional là enum về mặt khái niệm:

```swift
enum Optional<Wrapped> {
    case none
    case some(Wrapped)
}
```

Vì vậy pattern matching hoạt động tự nhiên:

```swift
switch value {
case .some(let v):
    print(v)
case .none:
    print("nil")
}
```

`Result<Success, Failure>` biểu diễn success/failure như value:

```swift
let result: Result<User, APIError>
```

Trong async/await code, function `async throws` thường tự nhiên hơn Result. Result hữu ích khi cần lưu kết quả, chuyển qua callback boundary hoặc compose theo kiểu value.

---

# 3. Protocol extension và conditional conformance

```swift
protocol CacheKey {
    var cacheKey: String { get }
}

extension CacheKey {
    var cacheKey: String {
        String(describing: self)
    }
}
```

Protocol extension cung cấp default implementation. Cần hiểu dispatch semantics: method chỉ tồn tại trong extension nhưng không phải requirement của protocol có thể dispatch khác với kỳ vọng khi value được nhìn qua existential.

Conditional conformance:

```swift
extension Array: SomeProtocol where Element: SomeConstraint {
}
```

Đây là nền tảng của nhiều generic API trong standard library.

---

# 4. Property wrapper, result builder và macro

Property wrapper đóng gói behavior của property:

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

SwiftUI dùng rất nhiều wrapper như `@State`, `@Binding`, `@Environment`.

Result builder là cơ chế đứng sau cú pháp declarative kiểu `ViewBuilder`.

Macro là compile-time transformation. `@Observable` và `@Model` là ví dụ quan trọng. Macro giúp sinh code nhưng cũng làm tăng “magic”; khi debug, cần biết macro expansion có thể xem trong Xcode.

---

# 5. Concurrency nền tảng đúng chuẩn Swift 6.x

## 5.1 Structured concurrency

```swift
async let profile = api.profile()
async let messages = api.messages()

let (p, m) = try await (profile, messages)
```

`async let` tạo child task có lifetime gắn với scope. `TaskGroup` dùng khi số task động:

```swift
let values = await withTaskGroup(of: Int.self) { group in
    for id in ids {
        group.addTask {
            await loadValue(id)
        }
    }

    var result: [Int] = []
    for await value in group {
        result.append(value)
    }
    return result
}
```

Structured concurrency giúp cancellation và lifetime dễ reasoning hơn detached task.

## 5.2 Actor

Actor bảo vệ mutable state khỏi data race:

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

Truy cập actor-isolated member từ bên ngoài thường cần `await`.

## 5.3 `@MainActor`

UI state thường thuộc main actor:

```swift
@MainActor
final class HomeModel {
    var items: [Item] = []

    func load() async {
        items = (try? await api.fetchItems()) ?? []
    }
}
```

`@MainActor` là isolation guarantee, không chỉ là “dispatch main queue”.

## 5.4 `Sendable`

`Sendable` biểu diễn value an toàn để transfer giữa concurrency domains. Value type chứa immutable/sendable field thường dễ conform:

```swift
struct UserSnapshot: Sendable {
    let id: UUID
    let name: String
}
```

Class mutable thường khó Sendable. `@unchecked Sendable` là lời hứa thủ công với compiler; dùng sai có thể đưa data race trở lại.

## 5.5 Swift 6.2 approachable concurrency

Swift 6.2 đưa ra hướng “single-threaded by default” thông qua default actor isolation option và cho phép opt-in concurrency rõ ràng hơn với `@concurrent`. Điều quan trọng là project setting ảnh hưởng semantics. Khi migrate project cũ, phải kiểm tra Swift language mode, default isolation và strict concurrency diagnostics thay vì copy annotation từ bài blog cũ.

---

# 6. SwiftUI data flow trung cấp

## 6.1 Ownership trước wrapper

Đừng chọn `@State`, `@Binding`, `@Environment`, `@Observable` theo mẹo ghi nhớ. Hãy hỏi: ai sở hữu dữ liệu? ai được mutate? lifetime thuộc view hay app/domain?

Một view sở hữu local transient state dùng `@State`. Parent sở hữu value nhưng child cần mutate dùng `@Binding`. Shared model có reference semantics có thể dùng `@Observable` và inject rõ ràng.

```swift
@Observable
final class Cart {
    var products: [Product] = []
}

struct RootView: View {
    @State private var cart = Cart()

    var body: some View {
        CartView()
            .environment(cart)
    }
}
```

## 6.2 Derived state

Không lưu state có thể tính được nếu không cần:

```swift
var canCheckout: Bool {
    !cart.products.isEmpty && address != nil
}
```

Duplicate state dễ bị inconsistency.

## 6.3 State machine

Thay vì ba Boolean:

```swift
var isLoading = false
var hasError = false
var isEmpty = false
```

model hóa:

```swift
enum ScreenState {
    case idle
    case loading
    case loaded([Item])
    case empty
    case failed(APIError)
}
```

State machine giảm impossible combinations.

---

# 7. SwiftUI layout sâu hơn

SwiftUI layout là negotiation giữa parent và child. Parent đề xuất size; child trả size; parent đặt child vào bounds. Vì vậy `.frame(width:height:)` không phải lúc nào cũng “ép kích thước” theo cách UIKit frame.

Các container quan trọng: `ScrollView`, `LazyVStack`, `LazyHStack`, `LazyVGrid`, `Grid`, `List`, `Form`.

`GeometryReader` mạnh nhưng hay bị lạm dụng. Dùng API layout mới, alignment guide, container-relative sizing hoặc custom Layout khi phù hợp.

Custom `Layout` cho phép kiểm soát measurement/placement mà không cần hack geometry.

---

# 8. Navigation architecture

`NavigationPath` cho navigation type-erased. Với app phức tạp, route enum giúp centralized navigation:

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

Root:

```swift
NavigationStack(path: $router.path) {
    HomeView()
        .navigationDestination(for: Route.self) { route in
            switch route {
            case .product(let id):
                ProductView(id: id)
            case .settings:
                SettingsView()
            }
        }
}
```

Deep link có thể parse URL → Route. Điều quan trọng là navigation trở thành data, giúp test và restore state tốt hơn.

---

# 9. Networking layer có cấu trúc

Không nên để mọi view tự tạo URLRequest và decode.

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

Một client production phải tách concern: request construction, auth header, transport, status validation, decoding, error mapping, retry/cancellation và logging.

`URLRequest`:

```swift
var request = URLRequest(url: url)
request.httpMethod = "POST"
request.timeoutInterval = 30
request.setValue("application/json", forHTTPHeaderField: "Content-Type")
request.httpBody = try JSONEncoder().encode(body)
```

`URLSessionConfiguration` quyết định cache, timeout, cookies, waitsForConnectivity và nhiều behavior khác.

Không retry mù quáng mọi request. GET idempotent dễ retry hơn POST tạo resource. Với 401, refresh token cần coordination để tránh nhiều request cùng refresh một lúc.

---

# 10. Codable nâng cao

Custom decoder:

```swift
let decoder = JSONDecoder()
decoder.keyDecodingStrategy = .convertFromSnakeCase
decoder.dateDecodingStrategy = .iso8601
```

Nếu server date format khác, dùng custom strategy.

Không expose DTO trực tiếp đến toàn bộ UI nếu API shape thay đổi thường xuyên. Có thể tách:

```swift
struct UserDTO: Decodable { ... }
struct User { ... }

extension User {
    init(dto: UserDTO) { ... }
}
```

Đây là boundary giữa transport model và domain model.

---

# 11. Persistence: SwiftData và Core Data ở mức ứng dụng

SwiftData model:

```swift
@Model
final class TaskItem {
    @Attribute(.unique) var id: UUID
    var title: String
    var isDone: Bool
}
```

Relationship, delete rule, migration và indexing phải được thiết kế như database chứ không chỉ “lưu object”.

SwiftData thuận tiện nhưng không làm mất các vấn đề nền tảng: schema evolution, consistency, transaction boundary, background work và data migration.

Core Data vẫn dùng rộng rãi trong production. Các khái niệm cần biết: `NSManagedObjectContext`, persistent store, fetch request, relationship, merge policy, background context và migration.

Repository có thể tách persistence detail khỏi feature, nhưng đừng tạo abstraction vô nghĩa chỉ để “đúng Clean Architecture”.

---

# 12. Dependency Injection

Constructor injection là default dễ test:

```swift
final class ProductService {
    private let client: any HTTPClient

    init(client: any HTTPClient) {
        self.client = client
    }
}
```

Protocol không phải lúc nào cũng cần. Nếu dependency là concrete stable type và test không cần substitution, concrete injection vẫn tốt.

Environment injection trong SwiftUI phù hợp dependency xuyên hierarchy. Global singleton tiện nhưng làm ownership/test/lifetime khó kiểm soát.

---

# 13. Architecture: MVC, MVVM, unidirectional flow

MVC của UIKit thường đặt ViewController ở trung tâm; dễ thành Massive View Controller nếu business logic dồn vào controller.

MVVM tách View và ViewModel. Với SwiftUI, View vốn là lightweight value description nên ViewModel không phải mandatory cho mọi màn hình. Tạo ViewModel khi cần quản lý state/lifecycle/use case phức tạp, không phải vì template.

Unidirectional data flow mô tả state đi xuống và event đi lên. Reducer architecture là một dạng formal hóa mô hình này.

Một architecture tốt phải trả lời được: state nằm đâu, mutation xảy ra ở đâu, dependency đi vào bằng cách nào, effect/network chạy ở đâu, feature boundary là gì, và test tại lớp nào.

---

# 14. UIKit trung cấp

Auto Layout dùng constraint relation giữa anchor:

```swift
titleLabel.translatesAutoresizingMaskIntoConstraints = false

NSLayoutConstraint.activate([
    titleLabel.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 16),
    titleLabel.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -16),
    titleLabel.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 16)
])
```

Hugging và compression resistance quyết định view co giãn khi constraint cạnh tranh.

`UITableView`/`UICollectionView` hiện đại nên biết diffable data source:

```swift
var snapshot = NSDiffableDataSourceSnapshot<Section, Item.ID>()
snapshot.appendSections([.main])
snapshot.appendItems(items.map(\.id))
dataSource.apply(snapshot, animatingDifferences: true)
```

Delegate pattern phổ biến trong UIKit. Đừng tạo retain cycle: nhiều delegate property được khai báo `weak`.

---

# 15. SwiftUI ↔ UIKit interoperability

Nhúng UIKit:

```swift
struct CameraView: UIViewControllerRepresentable {
    func makeUIViewController(context: Context) -> CameraViewController {
        CameraViewController()
    }

    func updateUIViewController(
        _ uiViewController: CameraViewController,
        context: Context
    ) {
    }
}
```

Coordinator bridge delegate/callback.

Nhúng SwiftUI vào UIKit:

```swift
let controller = UIHostingController(rootView: ProfileView())
```

Khi migration app lớn, incremental adoption thường thực tế hơn rewrite toàn bộ.

---

# 16. App lifecycle và scene lifecycle

SwiftUI app lifecycle dùng `App`/`Scene`. UIKit cũ dùng `UIApplicationDelegate` và `UISceneDelegate`.

Trong SwiftUI vẫn có thể bridge app delegate:

```swift
@UIApplicationDelegateAdaptor(AppDelegate.self)
private var appDelegate
```

Lifecycle event có thể theo dõi:

```swift
@Environment(\.scenePhase) private var scenePhase
```

`active`, `inactive`, `background` không nên bị hiểu như guarantee cho thời lượng background execution. iOS quản lý resource rất chặt.

---

# 17. Background tasks, notifications và deep links

Background execution không phải “app chạy tự do khi đóng”. Tùy use case có BackgroundTasks framework, background URLSession, location, audio và capability tương ứng.

Local notification được schedule trên device; push notification đi qua APNs. Push flow production gồm device token, provider server, APNs credential, payload, user authorization và handling foreground/background behavior.

Deep link có thể dùng custom URL scheme hoặc Universal Links. Universal Links đáng tin cậy hơn cho web-to-app nhưng cần Associated Domains và `apple-app-site-association`.

---

# 18. Testing trung cấp

Test pure domain logic trước vì nhanh và ổn định.

Swift Testing:

```swift
@Suite
struct PriceCalculatorTests {
    @Test(arguments: [
        (100, 0.1, 90),
        (200, 0.2, 160)
    ])
    func discount(input: Int, rate: Double, expected: Int) {
        #expect(calculate(input, rate) == expected)
    }
}
```

Async test:

```swift
@Test
func loadUser() async throws {
    let user = try await service.loadUser()
    #expect(user.id == expectedID)
}
```

UI test dùng accessibility identifier để chọn element ổn định. Không dựa vào sleep cố định nếu có thể chờ expectation/state.

---

# 19. Logging, metrics và error strategy

Phân loại error thành domain/network/auth/decoding/persistence nếu giúp UI và observability.

Không show trực tiếp mọi `localizedDescription` cho user. Error message cho developer và message UX là hai concern khác nhau.

Dùng `OSLog` privacy annotations cho log nhạy cảm. Production nên có crash reporting/analytics phù hợp privacy policy.

---

# 20. Xcode workflow trung cấp

Biết dùng Debug Navigator, Memory Graph, View Hierarchy Debugger, Organizer, Instruments, Test Plans, Scheme environment variables và Build Configuration.

Breakpoints nâng cao gồm symbolic breakpoint và exception breakpoint.

Build phase cần hiểu `Compile Sources`, `Link Binary With Libraries`, `Copy Bundle Resources`, run script. Script build phải deterministic và tránh làm build chậm không cần thiết.

Swift Package Manager là dependency manager ưu tiên trong ecosystem Apple hiện đại. `Package.swift` mô tả package/target/dependency cho Swift package; trong app project, Xcode quản lý package dependency qua UI/project metadata.

---

# 21. Intermediate Senior Notes

Một codebase khỏe mạnh không được đánh giá bằng số pattern nó dùng. Dấu hiệu tốt là dependency flow dễ hiểu, state ownership rõ, side effect có boundary, async task có lifetime rõ, error không bị nuốt, feature test được và build setting có chủ đích.

Đừng tạo `BaseViewModel`, `BaseRepository`, `BaseUseCase` quá sớm. Inheritance abstraction thường làm code Swift khó compose hơn. Protocol + composition hữu ích nhưng chỉ khi giảm coupling thật.

Đừng “async hóa” function chỉ để có thể gọi trong Task. Async nên phản ánh operation có suspension hoặc concurrency semantics thật.

Đừng bắt mọi model thành class observable. Domain value nên ưu tiên struct nếu identity/reference sharing không phải yêu cầu.
