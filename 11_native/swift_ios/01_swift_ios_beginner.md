# Swift & iOS Master Note — Beginner

> Phạm vi: Swift căn bản, tư duy lập trình, cấu trúc một ứng dụng iOS, Xcode, SwiftUI, UIKit ở mức nhập môn, Foundation, state, navigation, networking và persistence cơ bản.
>
> Baseline thực hành: Xcode 27 + Swift 6.4. Xcode 27 + Swift 6.4 + iOS 27 SDK là baseline hiện hành. Xcode 27.1/27.2 đang ở beta, vì vậy API chỉ xuất hiện ở các bản beta minor sẽ được đánh dấu riêng.

## 0. Swift, iOS, Xcode và các khái niệm cần phân biệt

Swift là ngôn ngữ lập trình do Apple khởi xướng, được thiết kế để có hiệu năng gần nhóm ngôn ngữ compiled như C/C++, nhưng ưu tiên mạnh vào type safety, memory safety và cú pháp dễ đọc. Swift không đồng nghĩa với iOS. Bạn có thể dùng Swift cho macOS, watchOS, tvOS, visionOS, server, command line, WebAssembly và một số môi trường khác. Trong phạm vi tài liệu này, Swift được học chủ yếu để phát triển ứng dụng iPhone/iPad.

iOS SDK là tập hợp framework, API, compiler support và resource mà Apple cung cấp để ứng dụng tương tác với hệ điều hành. Trong đó, `Foundation` cung cấp các kiểu và API nền tảng như `Date`, `URL`, `Data`, networking, file system và encoding; `SwiftUI` là framework UI declarative hiện đại; `UIKit` là framework UI imperative truyền thống nhưng vẫn cực kỳ quan trọng trong production, đặc biệt khi bảo trì codebase cũ hoặc cần API chưa có wrapper SwiftUI tương đương.

Xcode là IDE chính thức của Apple. Nó chứa Swift compiler, build system, debugger LLDB, Interface Builder, Simulator, Instruments, code signing integration, Test navigator, package manager integration và các công cụ phát hành ứng dụng. Bạn có thể viết Swift bằng editor khác, nhưng để build, sign, chạy Simulator và phát hành iOS app thì Xcode vẫn là trung tâm của workflow.

### 0.1 Version và deployment target

Ba khái niệm phải tách rõ là phiên bản Swift, phiên bản Xcode và deployment target. Swift version quyết định language mode và tính năng ngôn ngữ. Xcode version quyết định toolchain và SDK được cài. Deployment target là phiên bản iOS thấp nhất mà app cho phép cài.

Ví dụ, bạn có thể build bằng Xcode 27 với Swift 6.4 nhưng đặt iOS Deployment Target là iOS 17. Khi đó compiler hiểu Swift 6.4, nhưng code chỉ được gọi API tồn tại từ iOS 17 trở xuống, trừ khi bạn dùng availability check như:

```swift
if #available(iOS 27.0, *) {
    // API mới
} else {
    // fallback cho iOS cũ hơn
}
```

Điều này là nền tảng để hiểu tại sao “code compile được” chưa chắc “chạy được trên mọi thiết bị mà app hỗ trợ”.

---

# 1. Cài đặt và làm quen với Xcode

## 1.1 Cài Xcode

Cài Xcode từ Mac App Store hoặc Apple Developer Downloads. Với nhiều version Xcode trên cùng máy, có thể đổi command line tool bằng:

```bash
sudo xcode-select -s /Applications/Xcode.app
xcodebuild -version
swift --version
```

Lần đầu mở Xcode, IDE có thể yêu cầu cài thêm platform runtime hoặc Simulator. Simulator là môi trường giả lập thiết bị Apple trên Mac; nó không hoàn toàn giống thiết bị thật, đặc biệt với camera, push notification, thermal state, Bluetooth, background execution, keychain behavior và performance.

## 1.2 Tạo project iOS đầu tiên

Trong Xcode chọn `File > New > Project > iOS > App`. Các trường quan trọng gồm Product Name, Team, Organization Identifier, Interface, Language và Testing System.

`Bundle Identifier` thường có dạng reverse-domain, ví dụ `com.example.MyApp`. Nó định danh app trong hệ sinh thái Apple và liên quan đến signing, App ID, push notification, keychain group và App Store Connect.

Nếu chọn SwiftUI, entry point thường giống:

```swift
import SwiftUI

@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
```

`@main` đánh dấu điểm bắt đầu của executable. `App` là protocol của SwiftUI. `Scene` biểu diễn một phần vòng đời UI cấp ứng dụng. `WindowGroup` tạo window chứa view gốc.

## 1.3 Target, Scheme, Configuration và Build Settings

`Target` mô tả một sản phẩm được build, ví dụ iOS app, widget extension, test bundle hoặc framework. `Scheme` mô tả cách build/run/test/profile/archive một hoặc nhiều target. `Build Configuration` thường là Debug và Release. Debug ưu tiên khả năng debug, còn Release bật optimization phù hợp phát hành.

Build Settings có rất nhiều option. Người mới cần hiểu trước: `Product Bundle Identifier`, `iOS Deployment Target`, `Swift Language Version`, `Code Signing`, `Architectures`, `Other Swift Flags`, `Optimization Level`, `Info.plist` generation và capability-related settings.

Không nên chỉnh Build Settings ngẫu nhiên. Trong production, một thay đổi nhỏ như sai deployment target, signing team hay `SWIFT_STRICT_CONCURRENCY` có thể ảnh hưởng toàn bộ target.

---

# 2. Cú pháp Swift nền tảng

## 2.1 `let` và `var`

Swift phân biệt constant và variable:

```swift
let appName = "Master Swift"
var launchCount = 0
launchCount += 1
```

`let` không cho gán lại binding sau khi khởi tạo. `var` cho phép thay đổi. Idiom quan trọng của Swift là “prefer `let` by default”: nếu một giá trị không cần mutation, dùng `let` để compiler và người đọc hiểu invariant rõ hơn.

Swift có type inference:

```swift
let name = "Anna"      // String
let age = 30           // Int
let price = 12.5       // Double
let active = true      // Bool
```

Hoặc khai báo type rõ ràng:

```swift
let count: Int = 10
let ratio: Double = 0.75
```

## 2.2 Các kiểu dữ liệu cơ bản

Các numeric type phổ biến là `Int`, `UInt`, `Double`, `Float`. Trong app thông thường, ưu tiên `Int` cho integer và `Double` cho số thực. Không tự động convert giữa numeric types:

```swift
let a = 10
let b = 2.5
let result = Double(a) + b
```

`String` là Unicode-correct collection of `Character`, không nên giả định mỗi ký tự có đúng một byte hoặc một UTF-16 code unit.

```swift
let greeting = "Xin chào"
let message = "\(greeting), Swift!"
```

String interpolation `\(...)` là idiom chính để nhúng expression.

## 2.3 Collection: Array, Set, Dictionary

`Array<Element>` là collection có thứ tự và cho phép phần tử trùng:

```swift
var names = ["An", "Bình", "Chi"]
names.append("Dung")
let first = names[0]
```

Truy cập index ngoài phạm vi gây runtime trap. Khi không chắc index hợp lệ, kiểm tra `indices.contains(index)` hoặc dùng algorithm phù hợp thay vì hard-code index.

`Set<Element>` lưu phần tử unique, không đảm bảo thứ tự logic dùng cho UI:

```swift
var tags: Set<String> = ["swift", "ios"]
tags.insert("xcode")
```

`Dictionary<Key, Value>` ánh xạ key → value:

```swift
var scores = ["Alice": 90, "Bob": 80]
scores["Alice"] = 95
let score = scores["Bob"] // Int?
```

Việc lookup dictionary trả optional vì key có thể không tồn tại.

## 2.4 Tuple

Tuple gom nhiều giá trị tạm thời mà không cần tạo type riêng:

```swift
let user = (id: 1, name: "Minh")
print(user.id)
```

Tuple hữu ích với local return nhỏ. Với model có semantic rõ hoặc tồn tại lâu, nên tạo `struct`.

---

# 3. Control Flow

## 3.1 `if`, `else`, ternary và expression

```swift
if age >= 18 {
    print("Adult")
} else {
    print("Minor")
}
```

Swift không cho dùng integer như Boolean. Điều kiện phải có type `Bool`.

Ternary:

```swift
let status = isLoggedIn ? "Logged In" : "Guest"
```

Nên dùng ternary cho expression ngắn. Logic phức tạp nên dùng `if`.

## 3.2 `switch`

`switch` trong Swift phải exhaustive:

```swift
switch statusCode {
case 200:
    print("OK")
case 400..<500:
    print("Client error")
case 500..<600:
    print("Server error")
default:
    print("Other")
}
```

Swift không fall-through mặc định. Nếu thực sự cần hành vi đó có keyword `fallthrough`, nhưng thường nên tránh.

Pattern matching là sức mạnh lớn của `switch`:

```swift
let point = (2, 0)

switch point {
case (0, 0):
    print("Origin")
case (_, 0):
    print("On X axis")
case (0, _):
    print("On Y axis")
case let (x, y):
    print("\(x), \(y)")
}
```

## 3.3 Loop

```swift
for number in 1...5 {
    print(number)
}

for number in 1..<5 {
    print(number)
}

var n = 3
while n > 0 {
    n -= 1
}
```

`...` là closed range, `..<` là half-open range.

---

# 4. Function và parameter

Function:

```swift
func greet(name: String) -> String {
    "Hello, \(name)"
}
```

Swift có argument label:

```swift
func move(from source: String, to destination: String) { }

move(from: "A", to: "B")
```

Tên đầu tiên trước parameter là argument label, tên thứ hai là local parameter name:

```swift
func greet(_ person: String, from city: String) { }
```

`_` loại bỏ label ở call site.

Default parameter:

```swift
func request(timeout: TimeInterval = 30) { }
```

Variadic:

```swift
func sum(_ numbers: Int...) -> Int {
    numbers.reduce(0, +)
}
```

Function là first-class value:

```swift
func add(_ a: Int, _ b: Int) -> Int { a + b }

let operation: (Int, Int) -> Int = add
```

---

# 5. Optional — phần bắt buộc phải thật sự hiểu

Optional biểu diễn “có value hoặc không có value”. `String?` không phải `String`; nó là `Optional<String>`.

```swift
var nickname: String? = nil
nickname = "Tom"
```

Không được cưỡng ép dùng value optional như non-optional. Có nhiều cách unwrap.

`if let`:

```swift
if let nickname {
    print(nickname)
}
```

`guard let` phù hợp early exit:

```swift
func show(userID: String?) {
    guard let userID else {
        return
    }

    print(userID)
}
```

Nil coalescing:

```swift
let displayName = nickname ?? "Anonymous"
```

Optional chaining:

```swift
let length = user.profile?.name.count
```

Force unwrap `!`:

```swift
let value = nickname!
```

`!` nghĩa là “tôi khẳng định value chắc chắn khác nil”. Nếu sai, app crash. Trong production, force unwrap chỉ hợp lý khi invariant thực sự được đảm bảo bởi thiết kế hoặc framework; nếu chỉ dùng để “làm compiler im lặng” thì đó là code smell.

Implicitly unwrapped optional `String!` thường gặp ở code UIKit/IBOutlet cũ. Hãy hiểu nó nhưng đừng lạm dụng.

---

# 6. Struct, Class, Enum và Protocol

## 6.1 `struct`

```swift
struct User {
    let id: Int
    var name: String

    func displayName() -> String {
        name
    }
}
```

Struct là value type. Khi gán sang biến khác, về mặt semantics nó được copy:

```swift
var a = User(id: 1, name: "A")
var b = a
b.name = "B"

print(a.name) // A
```

Swift standard library dùng value semantics rất nhiều.

## 6.2 `class`

```swift
final class Session {
    var token: String?

    init(token: String? = nil) {
        self.token = token
    }
}
```

Class là reference type. Nhiều reference có thể trỏ cùng một instance. Class hỗ trợ inheritance và identity (`===`).

```swift
let a = Session()
let b = a
print(a === b) // true
```

`final` ngăn subclass. Nếu không thiết kế inheritance, `final class` thường cho intent rõ hơn và có thể giúp compiler optimize.

## 6.3 `enum`

Swift enum mạnh hơn enum kiểu integer truyền thống:

```swift
enum LoadState {
    case idle
    case loading
    case success([User])
    case failure(Error)
}
```

Associated values giúp mô hình hóa state machine:

```swift
switch state {
case .idle:
    break
case .loading:
    ProgressView()
case .success(let users):
    Text("\(users.count)")
case .failure(let error):
    Text(error.localizedDescription)
}
```

## 6.4 Protocol

Protocol định nghĩa capability/contract:

```swift
protocol IdentifiableItem {
    var id: String { get }
    func displayName() -> String
}
```

Type conform:

```swift
struct Product: IdentifiableItem {
    let id: String
    let name: String

    func displayName() -> String {
        name
    }
}
```

Swift dùng protocol-oriented programming rất nhiều. Tuy nhiên “dùng protocol cho mọi thứ” không phải best practice; protocol nên xuất hiện khi thật sự cần abstraction, substitution, generic constraint hoặc test seam.

---

# 7. Property và Method

Stored property lưu dữ liệu. Computed property tính toán value:

```swift
struct Rectangle {
    var width: Double
    var height: Double

    var area: Double {
        width * height
    }
}
```

Property observer:

```swift
var progress: Double = 0 {
    didSet {
        print("Changed from \(oldValue) to \(progress)")
    }
}
```

Type property:

```swift
struct API {
    static let baseURL = URL(string: "https://example.com")!
}
```

Instance method có thể mutate state của class trực tiếp, nhưng method của struct phải dùng `mutating` nếu thay đổi stored property:

```swift
struct Counter {
    private(set) var value = 0

    mutating func increment() {
        value += 1
    }
}
```

---

# 8. Access Control

Các mức chính: `open`, `public`, `package`, `internal`, `fileprivate`, `private`.

`internal` là mặc định trong module. `private` giới hạn mạnh nhất theo lexical scope. `fileprivate` cho phép truy cập trong cùng file. `public` cho module khác dùng nhưng class/method không cho override ngoài module. `open` chỉ áp dụng cho class/class member và cho phép subclass/override từ module khác.

Người mới nên bắt đầu với nguyên tắc: để implementation detail là `private`, chỉ mở API đúng mức cần thiết.

---

# 9. Error Handling

Định nghĩa error:

```swift
enum LoginError: Error {
    case invalidCredentials
    case networkUnavailable
}
```

Function throwing:

```swift
func login() throws -> User {
    throw LoginError.invalidCredentials
}
```

Call:

```swift
do {
    let user = try login()
    print(user)
} catch LoginError.invalidCredentials {
    print("Sai thông tin")
} catch {
    print(error)
}
```

`try?` chuyển kết quả thành optional. `try!` crash nếu có error. `try!` không nên dùng cho operation có khả năng fail hợp lệ như network hoặc file I/O.

`defer` chạy khi rời scope:

```swift
func work() {
    defer {
        print("cleanup")
    }
    print("work")
}
```

---

# 10. Closure

Closure là function value không tên:

```swift
let multiply: (Int, Int) -> Int = { a, b in
    a * b
}
```

Trailing closure:

```swift
let doubled = [1, 2, 3].map { value in
    value * 2
}
```

Shorthand:

```swift
let doubled = [1, 2, 3].map { $0 * 2 }
```

Các API SwiftUI, networking và async bridge cũ dùng closure rất nhiều.

Capture semantics rất quan trọng với class:

```swift
final class ScreenModel {
    var name = "Home"

    func load() {
        service.fetch { [weak self] result in
            self?.name = "Loaded"
        }
    }
}
```

`[weak self]` giúp tránh retain cycle khi closure được object khác giữ lâu hơn owner.

---

# 11. Memory Management và ARC nhập môn

Swift dùng Automatic Reference Counting (ARC) cho class instance. ARC tăng/giảm reference count và giải phóng object khi strong reference cuối cùng biến mất.

Retain cycle điển hình:

```swift
final class Parent {
    var child: Child?
}

final class Child {
    weak var parent: Parent?
}
```

`weak` luôn là optional vì target có thể bị giải phóng. `unowned` không giữ strong reference nhưng giả định target vẫn tồn tại khi truy cập; truy cập sau deallocation sẽ crash. Vì vậy `weak` an toàn hơn trong nhiều trường hợp.

Value type như struct/enum không được quản lý identity theo ARC giống class, dù storage phía dưới của Array/String có optimization riêng như copy-on-write.

---

# 12. Generic căn bản

Generic cho phép viết code không phụ thuộc một concrete type:

```swift
func first<T>(_ items: [T]) -> T? {
    items.first
}
```

Constraint:

```swift
func contains<T: Equatable>(_ value: T, in values: [T]) -> Bool {
    values.contains(value)
}
```

Bạn sẽ gặp generic khắp SwiftUI, `Result`, collection, `Optional`, networking abstraction và dependency injection.

---

# 13. Foundation cần học sớm

## 13.1 `Date`, `Calendar`, `DateComponents`

`Date` biểu diễn một thời điểm tuyệt đối. Việc “ngày 12/09/2026” phụ thuộc timezone/calendar.

```swift
let now = Date()
let calendar = Calendar.current
let year = calendar.component(.year, from: now)
```

Không tự cộng 24 giờ để ra “ngày mai” nếu logic là calendar date. Dùng `Calendar`:

```swift
let tomorrow = Calendar.current.date(byAdding: .day, value: 1, to: Date())
```

## 13.2 `URL`

Không ghép URL bằng string thủ công nếu có query:

```swift
var components = URLComponents(string: "https://api.example.com/search")!
components.queryItems = [
    URLQueryItem(name: "q", value: "swift ios")
]
let url = components.url!
```

## 13.3 `Codable`

```swift
struct User: Codable {
    let id: Int
    let name: String
}
```

Decode JSON:

```swift
let user = try JSONDecoder().decode(User.self, from: data)
```

Custom key:

```swift
struct User: Decodable {
    let userID: Int

    enum CodingKeys: String, CodingKey {
        case userID = "user_id"
    }
}
```

---

# 14. SwiftUI từ số 0

## 14.1 Declarative UI

UIKit truyền thống thường ra lệnh từng bước “tạo label, set frame, addSubview, update text”. SwiftUI mô tả UI như một function của state:

```swift
struct CounterView: View {
    @State private var count = 0

    var body: some View {
        VStack(spacing: 16) {
            Text("Count: \(count)")
            Button("Increase") {
                count += 1
            }
        }
        .padding()
    }
}
```

Khi `count` thay đổi, SwiftUI xác định phần view dependency cần update. Bạn không “redraw toàn màn hình bằng tay”.

## 14.2 `View` và modifier

`View` là protocol. `body` trả một view description:

```swift
var body: some View {
    Text("Hello")
        .font(.title)
        .foregroundStyle(.primary)
        .padding()
}
```

Modifier thường trả một view mới về mặt value semantics. Thứ tự modifier có thể ảnh hưởng kết quả.

## 14.3 Layout cơ bản

`VStack`, `HStack`, `ZStack` lần lượt bố trí theo trục dọc, ngang, chồng lớp.

```swift
HStack(alignment: .center, spacing: 12) {
    Image(systemName: "person.circle")
    VStack(alignment: .leading) {
        Text("Alice")
        Text("iOS Developer")
            .font(.caption)
    }
}
```

`Spacer()` chiếm khoảng trống linh hoạt. `padding`, `frame`, `alignment`, `layoutPriority`, `fixedSize` là các công cụ chính.

Không nên mang tư duy Auto Layout frame tuyệt đối sang SwiftUI. Hãy hiểu proposed size, ideal size và container layout dần dần.

## 14.4 List và `ForEach`

```swift
struct Item: Identifiable {
    let id: UUID
    let name: String
}

List(items) { item in
    Text(item.name)
}
```

Identity cực kỳ quan trọng. Không dùng index làm identity nếu danh sách có insert/delete/reorder khiến index thay đổi.

---

# 15. State và data flow trong SwiftUI

## 15.1 `@State`

`@State` dùng cho local mutable state mà view sở hữu:

```swift
@State private var isPresented = false
```

Không truyền `@State` từ parent xuống child như một “reference”. Nếu child cần sửa state của parent, dùng binding.

## 15.2 `@Binding`

```swift
struct ToggleRow: View {
    @Binding var isOn: Bool

    var body: some View {
        Toggle("Enabled", isOn: $isOn)
    }
}
```

Dấu `$` lấy projected value, ở đây là `Binding<Bool>`.

## 15.3 Observation hiện đại

Với iOS 17+, Observation là hướng hiện đại:

```swift
import Observation

@Observable
final class ProfileModel {
    var name = ""
    var isLoading = false
}
```

SwiftUI có thể track property mà `body` thực sự đọc. `ObservableObject`, `@Published`, `@StateObject`, `@ObservedObject` vẫn quan trọng để đọc và duy trì codebase cũ hoặc target cũ hơn.

## 15.4 Environment

Environment truyền dependency/context dọc view hierarchy:

```swift
@Environment(\.dismiss) private var dismiss
```

Custom observable model có thể được đưa vào environment. Nhưng environment không nên biến thành “global dumping ground”; dependency quan trọng nên có ownership rõ.

---

# 16. Navigation và presentation

`NavigationStack` là API chính:

```swift
NavigationStack {
    List(products) { product in
        NavigationLink(value: product) {
            Text(product.name)
        }
    }
    .navigationDestination(for: Product.self) { product in
        ProductDetail(product: product)
    }
}
```

Modal:

```swift
.sheet(isPresented: $showSettings) {
    SettingsView()
}
```

Alert:

```swift
.alert("Error", isPresented: $showError) {
    Button("OK", role: .cancel) {}
} message: {
    Text(message)
}
```

Trong app phức tạp, navigation state nên được model hóa thay vì trải khắp view bằng nhiều Boolean rời rạc.

---

# 17. Networking cơ bản với `URLSession`

Async/await là cách hiện đại:

```swift
struct APIUser: Decodable {
    let id: Int
    let name: String
}

func fetchUsers() async throws -> [APIUser] {
    let url = URL(string: "https://example.com/users")!
    let (data, response) = try await URLSession.shared.data(from: url)

    guard let http = response as? HTTPURLResponse,
          200..<300 ~= http.statusCode else {
        throw URLError(.badServerResponse)
    }

    return try JSONDecoder().decode([APIUser].self, from: data)
}
```

Không chỉ decode JSON rồi coi là thành công. Production network layer phải xử lý status code, server error body, cancellation, timeout, retry policy, authentication, caching và connectivity.

---

# 18. Concurrency nhập môn: `async`, `await`, `Task`

Function async:

```swift
func load() async throws -> User {
    try await api.fetchUser()
}
```

Trong SwiftUI:

```swift
.task {
    do {
        user = try await load()
    } catch {
        errorMessage = error.localizedDescription
    }
}
```

`await` không có nghĩa là “block thread”. Nó đánh dấu suspension point: task có thể tạm dừng và executor có thể làm việc khác.

Cancellation là cooperative:

```swift
try Task.checkCancellation()
```

Đừng tự động tạo `Task.detached` cho mọi việc nền. Structured concurrency là default tốt hơn.

Swift 6.x đặc biệt nhấn mạnh data-race safety. Các khái niệm `Sendable`, actor isolation và `@MainActor` sẽ được học kỹ ở phần Intermediate/Advanced.

---

# 19. Persistence căn bản

## 19.1 `UserDefaults`

Dùng cho preference nhỏ:

```swift
UserDefaults.standard.set(true, forKey: "hasSeenOnboarding")
let value = UserDefaults.standard.bool(forKey: "hasSeenOnboarding")
```

Không dùng UserDefaults như database lớn hoặc nơi lưu token bí mật.

## 19.2 Keychain

Credential/token nhạy cảm nên dùng Keychain. API Keychain C-style khá verbose; trong app có thể bọc bằng service nhỏ hoặc thư viện đáng tin cậy. Phải hiểu access group, accessibility và behavior khi uninstall/reinstall tùy loại item.

## 19.3 SwiftData

SwiftData là framework persistence hiện đại cho các OS mới:

```swift
@Model
final class Note {
    var title: String
    var createdAt: Date

    init(title: String, createdAt: Date = .now) {
        self.title = title
        self.createdAt = createdAt
    }
}
```

Ở view:

```swift
@Query(sort: \Note.createdAt, order: .reverse)
private var notes: [Note]

@Environment(\.modelContext)
private var modelContext
```

Core Data vẫn cực kỳ quan trọng với codebase hiện hữu và use case cần maturity lâu năm.

---

# 20. UIKit nhập môn và interoperability

UIKit dùng object-oriented, lifecycle-driven UI.

```swift
final class HomeViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemBackground
    }
}
```

Các khái niệm chính gồm `UIViewController`, `UIView`, `UILabel`, `UIButton`, `UITableView`, `UICollectionView`, Auto Layout, delegate/data source, navigation controller và presentation controller.

SwiftUI có thể nhúng UIKit qua `UIViewRepresentable` / `UIViewControllerRepresentable`; UIKit có thể nhúng SwiftUI bằng `UIHostingController`.

Không nên nghĩ “SwiftUI thay thế hoàn toàn UIKit”. Với app production, biết interoperability là kỹ năng thực tế.

---

# 21. Asset, localization và accessibility

Image/resource thường quản lý qua Asset Catalog (`Assets.xcassets`). SF Symbols dùng:

```swift
Image(systemName: "heart.fill")
```

Localization không nên hard-code mọi string. SwiftUI hỗ trợ localized string resources và String Catalog. Hãy thiết kế layout chịu được text dài hơn, pluralization và RTL.

Accessibility phải được xem là chức năng, không phải trang trí. SwiftUI có các modifier như:

```swift
.accessibilityLabel("Favorite")
.accessibilityHint("Marks this item as favorite")
```

Dynamic Type, contrast, VoiceOver, tap target và Reduce Motion đều cần được test.

---

# 22. Debugging trong Xcode

Breakpoint dừng execution tại dòng code. LLDB có các command như:

```text
po object
p expression
bt
thread backtrace
```

Xcode console là công cụ debug, nhưng production logging nên dùng `Logger` từ `OSLog` thay vì `print` tràn lan.

```swift
import OSLog

private let logger = Logger(
    subsystem: "com.example.app",
    category: "network"
)

logger.info("Request started")
```

Không log password, access token hoặc PII nhạy cảm.

---

# 23. Unit test nhập môn

Swift Testing là framework testing hiện đại:

```swift
import Testing

@Test
func totalPrice() {
    let result = 10 + 20
    #expect(result == 30)
}
```

XCTest vẫn rất phổ biến:

```swift
import XCTest

final class PriceTests: XCTestCase {
    func testTotal() {
        XCTAssertEqual(10 + 20, 30)
    }
}
```

Test nên kiểm chứng behavior có giá trị, không chỉ “chạy một dòng để tăng coverage”.

---

# 24. Signing, device và chạy app thật

Để chạy trên iPhone, Xcode phải sign executable bằng certificate và provisioning information hợp lệ. “Automatically manage signing” phù hợp khi học và với nhiều team nhỏ.

Các khái niệm phải phân biệt: Apple ID, Apple Developer Program membership, Team, Certificate, App ID, Provisioning Profile, Entitlement và Capability.

Capability như Push Notifications, Sign in with Apple, Associated Domains hoặc App Groups ảnh hưởng entitlement và thường cần cấu hình cả Apple Developer portal lẫn target.

---

# 25. Checklist kiến thức Beginner

Sau level này, bạn phải tự tạo được project SwiftUI, hiểu target/scheme/deployment target, viết Swift cơ bản không phụ thuộc copy-paste, model dữ liệu bằng struct/enum, xử lý optional/error, gọi REST API bằng async/await, decode Codable, tạo navigation và state đơn giản, lưu preference, debug bằng breakpoint, viết unit test cơ bản, chạy Simulator và thiết bị thật.

Điểm quan trọng hơn syntax là bạn phải hiểu ownership của state, khác biệt value/reference semantics, optional và error là một phần của type system, async không đồng nghĩa thread, và iOS API luôn bị ràng buộc bởi availability/deployment target.

---

# 26. Operator, precedence và range — phần nhỏ nhưng dùng ở mọi nơi

Swift có arithmetic operator như `+`, `-`, `*`, `/`, remainder `%`; comparison operator như `==`, `!=`, `<`, `<=`, `>`, `>=`; logical operator `!`, `&&`, `||`; assignment operator `=` và compound assignment như `+=`, `-=`. Một điểm quan trọng là assignment trong Swift không trả về một value theo kiểu C, vì vậy bạn không thể vô tình viết `if x = y` rồi compiler coi nó là condition.

Nil-coalescing `??` là operator rất thường dùng với Optional. Range operator gồm `...` cho closed range, `..<` cho half-open range và one-sided range như `array[2...]`. Trong collection code, half-open range thường tự nhiên hơn vì upper bound có thể là `endIndex`.

Swift cho phép định nghĩa custom operator và precedence group, nhưng đây là khả năng nên dùng rất thận trọng. Trong application code, operator tự chế dễ làm giảm readability; chúng phù hợp hơn với domain toán học hoặc library có semantics thực sự rõ ràng.

# 27. String, Character, Unicode và indexing đúng cách

`String` trong Swift không phải mảng byte hay mảng UTF-16. Một ký tự người dùng nhìn thấy có thể được tạo bởi nhiều Unicode scalar. Vì vậy `String.Index` là index riêng của String, không phải `Int`.

```swift
let text = "Swift 👨‍👩‍👧‍👦"
let first = text[text.startIndex]
let next = text.index(after: text.startIndex)
let prefix = text.prefix(5)
```

Nếu cần ký tự thứ `n`, có thể dùng:

```swift
let index = text.index(text.startIndex, offsetBy: n)
let character = text[index]
```

Nhưng nếu lặp đi lặp lại random access theo integer, hãy xem lại data structure; `String` không được thiết kế như array O(1) theo vị trí user-perceived character. Với parsing protocol/binary, thường bạn sẽ làm việc với `Data`, UTF-8 view hoặc parser phù hợp thay vì ép String thành byte array.

Các API thường dùng gồm `hasPrefix`, `hasSuffix`, `contains`, `split`, `replacingOccurrences`, `trimmingCharacters`, `lowercased`, `uppercased`. Khi so sánh/search nội dung dành cho người dùng, locale và normalization có thể quan trọng; đừng mặc định lowercase thủ công là cách đúng cho mọi ngôn ngữ.

# 28. Initialization, `deinit`, extension và subscript

Struct có memberwise initializer tự sinh nếu bạn không che nó bằng initializer tùy chỉnh trong declaration. Class cần hiểu designated initializer, convenience initializer và inheritance rule. Initializer có thể failable bằng `init?` khi input không tạo được object hợp lệ.

```swift
struct EmailAddress {
    let value: String

    init?(_ value: String) {
        guard value.contains("@") else { return nil }
        self.value = value
    }
}
```

`deinit` chỉ tồn tại trên class và chạy trước khi instance bị giải phóng. Nó thích hợp để cleanup resource có ownership rõ, nhưng không nên phụ thuộc vào `deinit` cho operation async quan trọng như gửi analytics hoặc save network data vì timing deallocation không phải lifecycle business guarantee.

Extension giúp thêm method, computed property, initializer, nested type hoặc protocol conformance mà không sửa declaration gốc:

```swift
extension String {
    var isBlank: Bool {
        trimmingCharacters(in: .whitespacesAndNewlines).isEmpty
    }
}
```

Subscript cho cú pháp `value[index]`. Custom collection hoặc matrix có thể dùng:

```swift
struct Matrix {
    let rows: Int
    let columns: Int
    private var values: [Double]

    subscript(row: Int, column: Int) -> Double {
        get { values[row * columns + column] }
        set { values[row * columns + column] = newValue }
    }
}
```

# 29. Type casting, `Any`, `AnyObject` và tránh mất type safety

`is` kiểm tra runtime type; `as?` cast an toàn và trả Optional; `as!` force cast và crash nếu sai.

```swift
if let viewController = value as? UIViewController {
    // dùng an toàn
}
```

`Any` có thể chứa hầu như mọi Swift value, còn `AnyObject` biểu diễn instance của class/reference-compatible object. Trong application Swift hiện đại, nếu bạn thấy dictionary `[String: Any]` lan rộng trong domain layer, đó thường là dấu hiệu nên model hóa dữ liệu bằng struct/enum/Codable. `Any` rất hữu ích ở boundary động như Objective-C, JSON thô, notification payload hoặc SDK legacy, nhưng không nên trở thành default data model.

# 30. Collection algorithms và tư duy functional vừa đủ

Các method `map`, `compactMap`, `flatMap`, `filter`, `reduce`, `sorted`, `first(where:)`, `contains(where:)`, `allSatisfy`, `prefix`, `dropFirst`, `zip` giúp code diễn đạt transformation trực tiếp.

```swift
let activeNames = users
    .filter(\.isActive)
    .map(\.name)
    .sorted()
```

`compactMap` vừa transform vừa bỏ `nil`, rất phù hợp parsing:

```swift
let numbers = ["1", "x", "3"].compactMap(Int.init)
```

Không cần biến mọi loop thành chuỗi functional dài. Khi transformation nhiều branch, có side effect, cần early exit hoặc performance-sensitive, `for` loop thường dễ đọc hơn.

# 31. Key Path

Key path biểu diễn đường dẫn property như một value có type:

```swift
let namePath: KeyPath<User, String> = \.name
let name = user[keyPath: namePath]
```

Bạn sẽ gặp key path trong sorting, SwiftUI binding, SwiftData query, KVO interop và generic API. Writable key path cho phép mutation khi root/property hỗ trợ.

# 32. Regex hiện đại

Swift có Regex DSL và regex literal trên toolchain hiện đại. Regex phù hợp validation/pattern extraction, nhưng không nên dùng để parse grammar phức tạp hoặc HTML tổng quát.

```swift
let pattern = /[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/
if input.wholeMatch(of: pattern) != nil {
    print("format email hợp lệ ở mức pattern")
}
```

Validation thực tế phải tách “format nhìn hợp lý” khỏi “email tồn tại/thực sự nhận thư được”.

# 33. Swift Package Manager nhập môn

Swift Package Manager, thường viết tắt là SwiftPM hoặc SPM, quản dependency và package Swift. Trong Xcode có thể thêm package qua `File > Add Package Dependencies`. Một package thuần Swift có manifest `Package.swift`.

```swift
// swift-tools-version: 6.4
import PackageDescription

let package = Package(
    name: "CoreKit",
    platforms: [.iOS(.v17)],
    products: [
        .library(name: "CoreKit", targets: ["CoreKit"])
    ],
    targets: [
        .target(name: "CoreKit"),
        .testTarget(name: "CoreKitTests", dependencies: ["CoreKit"])
    ]
)
```

Trong Swift 6.4, Swift Build trở thành build system mặc định của Swift Package Manager. Với người làm iOS, ý nghĩa thực tế là package ecosystem và build behavior giữa Apple platform và cross-platform ngày càng thống nhất hơn.

# 34. File system, sandbox và `FileManager`

iOS app chạy trong sandbox. Các vị trí như Documents, Library/Application Support và Caches có mục đích khác nhau. User-generated data cần backup không nên đặt vào Caches; dữ liệu có thể tái tạo nên tránh làm phình backup.

```swift
let documents = FileManager.default.urls(
    for: .documentDirectory,
    in: .userDomainMask
).first!
```

Khi ghi file, cân nhắc atomic write, error handling, file protection và migration. Không xây path bằng nối string; dùng `URL.appendingPathComponent` hoặc API URL hiện đại.

# 35. SwiftUI form, input, focus và keyboard

Các control thường dùng gồm `TextField`, `SecureField`, `Toggle`, `Picker`, `DatePicker`, `Slider`, `Stepper`. Form dài nên tổ chức bằng `Form`/`Section` khi semantics phù hợp.

`@FocusState` quản focus:

```swift
enum Field: Hashable { case email, password }

@FocusState private var focusedField: Field?

TextField("Email", text: $email)
    .focused($focusedField, equals: .email)
```

Validation nên phân biệt format error, server validation và transient typing state. Đừng hiện lỗi đỏ ngay khi user mới gõ ký tự đầu tiên nếu UX không yêu cầu.

# 36. Gesture và animation cơ bản

SwiftUI animation có hai lớp cần phân biệt: animation của state change và transition khi view xuất hiện/biến mất.

```swift
withAnimation(.spring) {
    isExpanded.toggle()
}
```

```swift
if isVisible {
    DetailView()
        .transition(.opacity.combined(with: .move(edge: .bottom)))
}
```

Gesture gồm tap, long press, drag, magnification và rotation tùy platform/API. Khi kết hợp gesture, cần hiểu precedence giữa `.gesture`, `.highPriorityGesture` và `.simultaneousGesture`. Với iOS 27, một số system gesture như text selection có thể cạnh tranh với custom gesture, vì vậy hãy test behavior trên SDK/OS thật mà app hỗ trợ.

# 37. Xcode Preview và workflow UI

`#Preview` giúp render view với dữ liệu mẫu mà không chạy full app:

```swift
#Preview("Logged in") {
    ProfileView(user: .preview)
}
```

Preview là công cụ feedback nhanh, không thay Simulator/device test. API liên quan camera, push, keychain, background task, memory pressure hoặc animation timing vẫn cần môi trường runtime phù hợp.

# 38. Những thay đổi Xcode 27 người mới cần biết

Xcode 27 đi cùng Swift 6.4 và iOS 27 SDK. `@State` trong SwiftUI được triển khai bằng macro mới; expression khởi tạo class lưu trong state được đánh giá lazy theo view lifetime thay vì bị đánh giá lặp mỗi lần value-type View được tái tạo. Result builder trong SwiftUI cũng được thống nhất theo `ContentBuilder`, giúp cải thiện type-checking/build time. Phần lớn source code cũ tương thích, nhưng code dựa vào implementation detail của property wrapper/result builder có thể cần migration.

`AsyncImage` trên SDK mới hỗ trợ HTTP caching mặc định theo cache header của server và có API để kiểm soát `URLRequest`, `URLSession`/`URLCache` chi tiết hơn. Điều này không có nghĩa mọi image loader custom trở nên vô dụng; production vẫn có thể cần transform pipeline, disk cache policy, prefetch, placeholder strategy hoặc authenticated request.

# 39. Bài tập tổng hợp Beginner

Hãy tự xây một app “Reading List” có ba màn hình: danh sách sách, chi tiết và form thêm/sửa. Model bằng `struct`/`enum`; dùng `NavigationStack`; local UI state dùng `@State`; model chia sẻ dùng Observation; gọi một REST endpoint bằng `URLSession`; decode bằng Codable; lưu bookmark bằng SwiftData; preference nhỏ bằng UserDefaults; token giả lập qua service Keychain; thêm ít nhất ba unit test và một error state rõ ràng.

Nếu hoàn thành mà không copy nguyên sample, bạn sẽ buộc phải nối các khái niệm language → state → UI → async → persistence → test, chính là bước cần thiết trước khi lên Intermediate.
