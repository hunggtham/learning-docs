# Swift & iOS Master Note — Beginner

> Phạm vi: Swift căn bản, tư duy lập trình, cấu trúc một ứng dụng iOS, Xcode, Foundation, SwiftUI, UIKit, state, networking, persistence và concurrency ở mức nhập môn.
>
> Baseline thực hành: **Xcode 27 + Swift 6.4 + iOS 27 SDK**. Xcode 27.1/27.2 đang ở beta tại thời điểm cập nhật 21/09/2026 nên không được dùng làm baseline stable.

Tài liệu này không phải cheat sheet. Mục tiêu của Beginner là tạo một mental model đủ chắc để khi sang Intermediate, các chủ đề như actor, `Sendable`, Observation, architecture hay persistence không trở thành những annotation/API phải học thuộc lòng. Hãy đọc theo thứ tự; những phần sau giả định bạn hiểu ownership, Optional, value/reference semantics và closure ở các phần trước.

---

# 0. Swift, iOS, SDK và Xcode là những lớp khác nhau

Swift là ngôn ngữ lập trình. iOS là hệ điều hành. iOS SDK là tập framework và API mà app dùng để tương tác với hệ điều hành. Xcode là IDE/toolchain chính thức chứa compiler, linker, debugger LLDB, build system, Simulator, Instruments, signing integration và các công cụ release.

Các framework nền tảng cần phân biệt sớm. `Swift Standard Library` cung cấp `Int`, `String`, `Array`, `Optional`, collection algorithms và phần lớn primitive của ngôn ngữ. `Foundation` bổ sung `Date`, `URL`, `Data`, `FileManager`, `URLSession`, encoding và nhiều API platform-neutral. `SwiftUI` là framework UI declarative hiện đại. `UIKit` là framework UI imperative/lifecycle-driven truyền thống nhưng vẫn rất quan trọng trong production, SDK integration và codebase legacy.

## 0.1 Swift version, language mode, Xcode, SDK và deployment target

Đây là năm khái niệm liên quan nhưng không đồng nhất. Xcode chứa một Swift compiler cụ thể và các SDK cụ thể. Swift language mode quyết định tập semantics/language rules mà target dùng. SDK version quyết định compiler biết những API platform nào. Deployment target lại là OS thấp nhất app hỗ trợ ở runtime.

Ví dụ, một app có thể build bằng Xcode 27/Swift 6.4 nhưng deployment target là iOS 17. Compiler hiểu cú pháp Swift 6.4, nhưng API chỉ tồn tại từ iOS 27 phải được bảo vệ bằng availability:

```swift
if #available(iOS 27.0, *) {
    // API chỉ dùng khi runtime đủ mới
} else {
    // fallback
}
```

Compile-time condition như `#if DEBUG`, `#if os(iOS)` hoặc `#if canImport(...)` là chuyện khác: nó quyết định source nào được compile, không phải branch runtime.

---

# 1. Làm quen Xcode trước khi viết app

## 1.1 Cài và kiểm tra toolchain

Xcode có thể được cài từ Mac App Store hoặc Apple Developer Downloads. Nếu máy có nhiều Xcode:

```bash
sudo xcode-select -s /Applications/Xcode.app
xcodebuild -version
swift --version
```

Simulator giúp feedback nhanh nhưng không phải thiết bị thật. Camera, push notification, thermal behavior, memory pressure, background execution, Keychain, Bluetooth và performance cần được test trên device phù hợp.

## 1.2 Project, target, scheme và build configuration

Khi tạo `iOS > App`, Xcode tạo project chứa ít nhất một application target. `Target` mô tả một sản phẩm build như app, test bundle, widget hoặc framework. `Scheme` mô tả cách build/run/test/profile/archive target. `Build Configuration` thường có Debug và Release. Debug ưu tiên debuggability; Release bật optimization và là nơi nhiều bug timing/data race chỉ xuất hiện rõ.

`Bundle Identifier` thường có dạng reverse-domain như `com.example.reader`. Nó liên quan đến App ID, signing, push, keychain access group và App Store Connect.

SwiftUI app entry point thường là:

```swift
import SwiftUI

@main
struct ReaderApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
```

`@main` đánh dấu entry point. `App` mô tả lifecycle ở mức ứng dụng; `Scene` mô tả một presentation/window lifecycle.

---

# 2. Values, variables và type system nền tảng

## 2.1 `let`, `var` và type inference

```swift
let appName = "Reader"
var launchCount = 0
launchCount += 1
```

`let` tạo binding không được gán lại; `var` cho phép mutation. Hãy ưu tiên `let` nếu không cần thay đổi vì nó làm invariant rõ hơn cho compiler và người đọc.

Swift suy luận type:

```swift
let name = "Anna"      // String
let age = 30            // Int
let price = 12.5        // Double
let active = true       // Bool
```

Hoặc khai báo rõ:

```swift
let retryCount: Int = 3
let timeout: Double = 30
```

## 2.2 Numeric types và conversion

Các type thường gặp là `Int`, `UInt`, `Double`, `Float`. Trong app thông thường, dùng `Int` cho integer và `Double` cho floating-point trừ khi domain/interop yêu cầu type khác.

Swift không tự chuyển numeric type tùy ý:

```swift
let count = 10
let ratio = 2.5
let result = Double(count) * ratio
```

Floating-point không biểu diễn chính xác mọi số thập phân. Không dùng `Double` làm model tiền nếu domain yêu cầu decimal arithmetic chính xác; `Decimal` hoặc integer minor units thường phù hợp hơn tùy hệ thống.

Overflow integer thường trap trong build bình thường. Swift có overflow operator `&+`, `&-`, `&*`, nhưng chỉ dùng khi wraparound là semantics có chủ đích.

## 2.3 Boolean và comparison

Điều kiện Swift phải là `Bool`; không có kiểu “0 là false, khác 0 là true” như C.

```swift
if items.isEmpty {
    print("No items")
}
```

Các operator so sánh gồm `==`, `!=`, `<`, `<=`, `>`, `>=`; logical operator gồm `!`, `&&`, `||` và short-circuit theo thứ tự expression.

## 2.4 Tuple và `typealias`

Tuple phù hợp với giá trị cục bộ nhỏ:

```swift
let user = (id: 42, name: "Minh")
print(user.name)
```

Nếu dữ liệu có semantic lâu dài, hãy dùng `struct` thay vì lan truyền tuple qua nhiều layer.

`typealias` tạo tên khác cho type, không tạo type mới:

```swift
typealias UserID = UUID
```

Nếu cần compiler phân biệt `UserID` và `OrderID`, hãy tạo wrapper type thay vì hai `typealias UUID`.

---

# 3. String, Character, collection và indexing

## 3.1 String là Unicode, không phải mảng byte

Một ký tự người dùng nhìn thấy có thể chứa nhiều Unicode scalar. Vì vậy `String.Index` không phải `Int`.

```swift
let text = "Swift 👨‍👩‍👧‍👦"
let first = text[text.startIndex]
let next = text.index(after: text.startIndex)
let prefix = text.prefix(5)
```

Nếu cần vị trí `n`:

```swift
let index = text.index(text.startIndex, offsetBy: n)
let character = text[index]
```

Random access theo integer lặp đi lặp lại trên `String` có thể là dấu hiệu data structure sai. Với binary protocol, dùng `Data`/byte-oriented API thay vì ép `String` thành byte array.

## 3.2 Array, Set, Dictionary

```swift
var names = ["An", "Bình", "Chi"]
names.append("Dung")

var tags: Set<String> = ["swift", "ios"]
tags.insert("xcode")

var scores = ["Alice": 90, "Bob": 80]
let bob = scores["Bob"] // Int?
```

`Array` có thứ tự và cho phép duplicate. `Set` giữ phần tử unique và yêu cầu `Hashable`. Dictionary lookup trả Optional vì key có thể không tồn tại.

Truy cập array index ngoài range sẽ trap. Khi identity của UI item là entity identity, không dùng index thay cho ID chỉ vì thuận tiện.

## 3.3 Collection algorithms

```swift
let activeNames = users
    .filter(\.isActive)
    .map(\.name)
    .sorted()

let numbers = ["1", "x", "3"].compactMap(Int.init)
```

`map` transform từng phần tử; `compactMap` transform và bỏ nil; `flatMap` flatten nested sequence; `filter` giữ phần tử thỏa predicate; `reduce` gộp sequence. Không cần biến mọi loop thành functional chain: `for` loop vẫn tốt khi có early exit, mutation hoặc control flow phức tạp.

---

# 4. Control flow và pattern matching

## 4.1 `if`, ternary, `guard`

```swift
if age >= 18 {
    print("Adult")
} else {
    print("Minor")
}

let title = isLoggedIn ? "Home" : "Login"
```

`guard` phù hợp để kiểm precondition rồi thoát sớm:

```swift
func load(userID: String?) {
    guard let userID else { return }
    print(userID)
}
```

## 4.2 `switch` exhaustive

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

Swift không fall through mặc định. Exhaustiveness làm enum/state machine an toàn hơn khi thêm case mới.

## 4.3 `if case`, `guard case`, `for case`

Pattern matching không chỉ tồn tại trong `switch`:

```swift
if case .success(let user) = result {
    print(user)
}

guard case .authenticated(let session) = state else {
    return
}

for case let .success(value) in results {
    print(value)
}
```

Các form này hữu ích khi chỉ quan tâm một pattern mà không cần `switch` đầy đủ.

## 4.4 Loop và range

```swift
for number in 1...5 { }
for number in 1..<5 { }

var retry = 3
while retry > 0 {
    retry -= 1
}
```

`...` là closed range, `..<` là half-open range. Collection code thường dùng half-open range vì upper bound có thể là `endIndex`.

---

# 5. Function, parameter và call-site design

## 5.1 Function và argument label

```swift
func greet(_ person: String, from city: String) -> String {
    "Hello \(person) from \(city)"
}

greet("Minh", from: "Seoul")
```

Argument label là một phần của API readability. Swift API tốt nên đọc gần như một câu ở call site.

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

## 5.2 Function là value

```swift
func add(_ lhs: Int, _ rhs: Int) -> Int { lhs + rhs }
let operation: (Int, Int) -> Int = add
```

Function có thể được truyền vào function khác, lưu trong property hoặc trả về như value. Đây là nền tảng của closure, callback, higher-order function và dependency injection bằng function value.

## 5.3 `inout`

Parameter mặc định là value được truyền vào theo semantics của type. `inout` cho phép function mutate caller storage:

```swift
func increment(_ value: inout Int) {
    value += 1
}

var count = 0
increment(&count)
```

`inout` không có nghĩa “pointer C thông thường”. Swift thực thi exclusivity rule để tránh hai access ghi/đọc xung đột cùng storage.

## 5.4 Overload và ambiguity

Swift cho phép nhiều function cùng tên nếu signature khác nhau. Overload giúp API tự nhiên nhưng quá nhiều overload generic có thể khiến call site/diagnostic khó hiểu. Khi semantic khác nhau rõ rệt, tên khác thường tốt hơn ép compiler đoán.

---

# 6. Optional — mô hình hóa sự vắng mặt trong type system

`String?` là `Optional<String>`, nghĩa là có value hoặc `nil`.

```swift
var nickname: String? = nil
nickname = "Tom"
```

## 6.1 Unwrap

```swift
if let nickname {
    print(nickname)
}

let displayName = nickname ?? "Anonymous"
let length = user.profile?.name.count
```

`guard let` phù hợp với early-exit; nil coalescing `??` phù hợp default value; optional chaining phù hợp chuỗi property/method có thể nil.

## 6.2 Force unwrap

```swift
let value = nickname!
```

`!` là assertion runtime. Nếu value nil, app trap. Chỉ dùng khi invariant thực sự được bảo đảm bởi thiết kế/framework. “Compiler đang báo lỗi” không phải lý do hợp lệ.

Implicitly unwrapped Optional (`String!`) vẫn xuất hiện trong IBOutlet/API Objective-C legacy. Hãy hiểu để maintain code, không dùng làm default cho model mới.

---

# 7. Struct, class, enum và protocol

## 7.1 Struct và value semantics

```swift
struct User {
    let id: UUID
    var name: String
}

var a = User(id: UUID(), name: "A")
var b = a
b.name = "B"
```

Về semantics, `a` và `b` là hai value độc lập. Standard collection như Array/String có thể dùng copy-on-write nội bộ để tránh copy vật lý không cần thiết, nhưng code của bạn vẫn phải reasoning như value semantics.

## 7.2 Class, identity và reference semantics

```swift
final class Session {
    var token: String?
}

let first = Session()
let second = first
print(first === second) // true
```

Nhiều reference có thể trỏ cùng instance. Vì vậy mutation qua một reference có thể được quan sát từ reference khác. `===` kiểm identity, khác `==` là equality semantic.

Nếu không chủ đích thiết kế inheritance, `final class` thường thể hiện intent tốt hơn.

## 7.3 Enum: raw value, associated value và recursive state

```swift
enum Direction: String {
    case north, south, east, west
}

enum LoadState {
    case idle
    case loading
    case success([User])
    case failure(any Error)
}
```

Raw value là giá trị cố định gắn với case. Associated value mang payload khác nhau theo case. Đây là công cụ rất mạnh để loại bỏ trạng thái bất khả thi.

Enum recursive cần `indirect`:

```swift
indirect enum Expression {
    case number(Int)
    case add(Expression, Expression)
}
```

## 7.4 Protocol

```swift
protocol Displayable {
    var title: String { get }
    func displayText() -> String
}
```

Protocol mô tả capability/contract. Không tạo protocol chỉ vì “architecture mẫu có protocol”. Protocol có giá trị khi cần generic constraint, substitution, cross-module contract hoặc test seam thực sự.

---

# 8. Initialization, extension, nested type và subscript

## 8.1 Initialization

Struct có memberwise initializer nếu điều kiện phù hợp. Class có designated/convenience initializer và inheritance rule riêng. Failable initializer dùng `init?` khi input có thể không tạo được value hợp lệ.

```swift
struct EmailAddress {
    let value: String

    init?(_ value: String) {
        guard value.contains("@") else { return nil }
        self.value = value
    }
}
```

Initializer phải đưa object vào trạng thái hợp lệ trước khi sử dụng `self` tự do. Đừng đẩy object “nửa khởi tạo” ra bên ngoài rồi mong caller nhớ gọi `setup()` nếu invariant có thể đảm bảo ngay trong init.

## 8.2 Extension

```swift
extension String {
    var isBlank: Bool {
        trimmingCharacters(in: .whitespacesAndNewlines).isEmpty
    }
}
```

Extension nhóm behavior/conformance tốt, nhưng đừng rải một type thành hàng chục extension không có boundary rõ ràng.

## 8.3 Nested type

```swift
struct APIRequest {
    enum Method {
        case get, post
    }
}
```

Nested type hữu ích khi type con chỉ có ý nghĩa trong namespace của type cha.

## 8.4 Subscript

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

Subscript nên có semantics truy cập giống collection/index, không nên che một operation đắt đỏ hoặc side effect khó đoán.

---

# 9. Property, method và type-level member

Stored property giữ dữ liệu; computed property tính value:

```swift
struct Rectangle {
    var width: Double
    var height: Double

    var area: Double { width * height }
}
```

Property observer:

```swift
var progress = 0.0 {
    didSet {
        print("\(oldValue) -> \(progress)")
    }
}
```

Struct method cần `mutating` nếu sửa state:

```swift
struct Counter {
    private(set) var value = 0

    mutating func increment() {
        value += 1
    }
}
```

`static` member thuộc type. Class còn có `class` member cho phép subclass override:

```swift
class BaseFormatter {
    class var identifier: String { "base" }
}
```

Ưu tiên `static` nếu không có nhu cầu override.

---

# 10. Access control

Các mức chính: `open`, `public`, `package`, `internal`, `fileprivate`, `private`.

`internal` là mặc định trong module. `package` chia sẻ trong cùng Swift package nhưng không public ra consumer bên ngoài package. `public` expose API ra module khác nhưng không cho subclass/override class member ngoài module; `open` cho phép điều đó.

Nguyên tắc thực dụng: API surface càng nhỏ, invariant càng dễ giữ. Để implementation detail là `private`/`internal` trừ khi consumer thật sự cần.

---

# 11. Closure — lifetime, capture và `@escaping`

Closure là function value không tên:

```swift
let multiply: (Int, Int) -> Int = { lhs, rhs in
    lhs * rhs
}
```

Trailing closure và shorthand:

```swift
let doubled = [1, 2, 3].map { $0 * 2 }
```

## 11.1 Escaping và non-escaping

Closure parameter mặc định là non-escaping: closure phải được gọi trước khi function return. Nếu closure được giữ lại để gọi sau, parameter cần `@escaping`:

```swift
final class Loader {
    private var completion: (() -> Void)?

    func start(completion: @escaping () -> Void) {
        self.completion = completion
    }
}
```

Escaping closure quan trọng vì lifetime dài hơn call stack và có thể tham gia ownership cycle.

## 11.2 Capture list

Closure giữ các value/reference nó dùng. Với class reference, default capture thường là strong:

```swift
service.fetch { [weak self] result in
    guard let self else { return }
    self.handle(result)
}
```

Capture list cũng có thể snapshot một value tại thời điểm closure được tạo:

```swift
var message = "A"
let closure = { [message] in print(message) }
message = "B"
closure() // A
```

Không thêm `[weak self]` máy móc. Hãy hỏi closure được ai giữ, sống bao lâu và operation có nên tiếp tục khi owner biến mất hay không.

## 11.3 `@autoclosure`

`@autoclosure` cho phép caller truyền expression thay vì viết `{ ... }`. Nó phù hợp API như assertion/lazy expression nhưng dễ che control flow; app code hiếm khi cần tự thiết kế API kiểu này.

---

# 12. ARC và memory ownership — mental model bắt buộc

Swift dùng Automatic Reference Counting cho class/reference-counted object. ARC tự chèn retain/release theo lifetime, nhưng ARC không phải garbage collector dò cycle.

## 12.1 Strong reference và object lifetime

```swift
final class Owner {
    let name: String
    init(name: String) { self.name = name }
    deinit { print("released \(name)") }
}

var owner: Owner? = Owner(name: "A")
owner = nil
```

Khi strong reference cuối cùng mất đi, instance có thể deinitialize. `deinit` phù hợp cleanup synchronous/resource ownership rõ, nhưng không phải nơi đáng tin để gửi network request hoặc lưu business data quan trọng.

## 12.2 Retain cycle giữa object

```swift
final class Parent {
    var child: Child?
}

final class Child {
    weak var parent: Parent?
}
```

Nếu cả `Parent.child` và `Child.parent` đều strong, hai object giữ nhau và ARC không thể giảm count về zero. `weak` không giữ object sống và luôn đọc được như Optional vì target có thể biến mất.

`unowned` cũng không retain nhưng biểu diễn invariant mạnh hơn: reference phải còn sống mỗi khi truy cập. Nếu invariant sai, chương trình trap. Chỉ dùng `unowned` khi lifetime relation thực sự được chứng minh, không phải để tránh viết `?`.

## 12.3 Retain cycle với closure

Một cycle phổ biến hơn là `self -> closure property/service -> closure -> self`:

```swift
final class ScreenModel {
    var onChange: (() -> Void)?

    func configure() {
        onChange = { [weak self] in
            self?.refresh()
        }
    }

    private func refresh() { }
}
```

Nếu closure chỉ tồn tại trong một call synchronous và không được giữ, strong capture có thể hoàn toàn đúng. Ownership graph quan trọng hơn quy tắc “closure luôn weak self”.

## 12.4 Value type vẫn có thể giữ reference

Struct không có identity ARC riêng, nhưng field của struct có thể là class reference:

```swift
struct Container {
    var session: Session
}
```

Copy `Container` không nhất thiết tạo `Session` mới. Hai container value có thể vẫn giữ cùng instance. Vì vậy “struct = mọi thứ deep copied” là mental model sai.

## 12.5 Stack, heap và thứ thật sự cần nhớ

Không nên học Swift theo quy tắc đơn giản “struct ở stack, class ở heap”. Compiler có quyền optimize/box/escape value. Điều có ý nghĩa ở source level là value semantics, reference identity, ownership và lifetime. Stack/heap hữu ích khi profiling low-level, nhưng không thay semantics ngôn ngữ.

## 12.6 Debug memory

Khi nghi leak, dùng Xcode Memory Graph để xem retain path; Instruments Allocations/Leaks để quan sát allocation/lifetime. Đừng kết luận mọi memory growth là leak: cache hợp lệ, image decode và object sống lâu có thể tăng resident memory mà không tạo unreachable cycle.

---

# 13. Error handling và cleanup

```swift
enum LoginError: Error {
    case invalidCredentials
    case networkUnavailable
}

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

`try?` biến failure thành nil; `try!` trap nếu error xảy ra. `try!` không phù hợp với network/file I/O vốn có failure hợp lệ.

`defer` đảm bảo code chạy khi rời scope:

```swift
func work() {
    acquireResource()
    defer { releaseResource() }
    performWork()
}
```

---

# 14. Generic căn bản, KeyPath và type casting

Generic tái sử dụng logic mà giữ type safety:

```swift
func first<T>(_ items: [T]) -> T? {
    items.first
}

func contains<T: Equatable>(_ value: T, in values: [T]) -> Bool {
    values.contains(value)
}
```

KeyPath là đường dẫn property có type:

```swift
let path: KeyPath<User, String> = \.name
let name = user[keyPath: path]
```

Runtime cast:

```swift
if let viewController = value as? UIViewController {
    // cast thành công
}
```

`is` kiểm type; `as?` trả Optional; `as!` trap nếu sai. `Any` hữu ích ở boundary động/legacy nhưng nếu `[String: Any]` lan vào domain model thì thường nên thay bằng struct/enum/Codable.

---

# 15. Regex hiện đại

Swift hỗ trợ Regex và regex literal trên toolchain hiện đại:

```swift
let pattern = /[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/

if input.wholeMatch(of: pattern) != nil {
    print("format looks valid")
}
```

Regex phù hợp pattern matching/extraction, không phải parser cho grammar phức tạp hay HTML tổng quát. Validation format cũng không chứng minh resource tồn tại; email nhìn hợp lệ chưa có nghĩa mailbox thật.

---

# 16. Foundation cần học sớm

## 16.1 `Date`, `Calendar`, timezone

`Date` biểu diễn một instant. “Ngày/tháng/năm” là cách diễn giải theo calendar/timezone.

```swift
let now = Date()
let calendar = Calendar.current
let year = calendar.component(.year, from: now)
let tomorrow = calendar.date(byAdding: .day, value: 1, to: now)
```

Nếu logic là “ngày mai theo lịch”, không tự cộng 86.400 giây vì DST/calendar có thể làm assumption sai.

## 16.2 URL và URLComponents

```swift
var components = URLComponents(string: "https://api.example.com/search")!
components.queryItems = [
    URLQueryItem(name: "q", value: "swift ios")
]
let url = components.url!
```

Không tự nối query string vì escaping/encoding dễ sai.

## 16.3 `Codable`

```swift
struct APIUser: Codable {
    let id: Int
    let name: String
}
```

```swift
let user = try JSONDecoder().decode(APIUser.self, from: data)
```

Custom key:

```swift
struct APIUser: Decodable {
    let userID: Int

    enum CodingKeys: String, CodingKey {
        case userID = "user_id"
    }
}
```

DTO từ server và domain model không bắt buộc là một type. Khi API shape khác domain semantics, mapping riêng làm boundary rõ hơn.

---

# 17. SwiftUI: UI là function của state

SwiftUI declarative nghĩa là bạn mô tả UI tương ứng với state hiện tại:

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

`View` là value description. Đừng mang mental model “View object sống cố định và tôi mutate label.text” từ UIKit sang SwiftUI.

## 17.1 Modifier và order

```swift
Text("Hello")
    .font(.title)
    .padding()
    .background(.thinMaterial)
```

Modifier trả về view description mới; thứ tự có thể thay đổi layout/visual effect.

## 17.2 Layout

`VStack`, `HStack`, `ZStack`, `Spacer`, `frame`, `padding`, alignment và layout priority là primitive chính. SwiftUI layout là negotiation: parent propose size, child chọn size phù hợp, parent đặt child. `frame` không đơn giản là UIKit frame assignment.

## 17.3 List và identity

```swift
struct Item: Identifiable {
    let id: UUID
    let title: String
}

List(items) { item in
    Text(item.title)
}
```

Identity phải ổn định qua insert/delete/reorder. `ForEach(items.indices, id: \.self)` không phải replacement cho entity ID khi collection thay đổi.

---

# 18. SwiftUI state và ownership

Trước khi chọn wrapper, hỏi: **ai sở hữu value, ai được mutate, lifetime thuộc đâu?**

## 18.1 `@State`

```swift
@State private var isPresented = false
```

Dùng cho local mutable state mà view identity sở hữu. `@State` không phải cách biến mọi property thành mutable; derived value nên được tính từ source state thay vì lưu trùng.

## 18.2 `@Binding`

```swift
struct ToggleRow: View {
    @Binding var isOn: Bool

    var body: some View {
        Toggle("Enabled", isOn: $isOn)
    }
}
```

Binding không sở hữu value; nó là read/write projection tới state do nơi khác sở hữu.

## 18.3 Observation hiện đại

```swift
import Observation

@Observable
final class ProfileModel {
    var name = ""
    var isLoading = false
}
```

SwiftUI theo dõi property observable mà view đọc. `ObservableObject`, `@Published`, `@StateObject`, `@ObservedObject` vẫn cần biết để maintain target cũ/code legacy.

## 18.4 Environment

```swift
@Environment(\.dismiss) private var dismiss
```

Environment phù hợp context/dependency theo view tree, nhưng không nên trở thành global service locator. Dependency business bắt buộc nên có ownership rõ ở composition root/initializer khi phù hợp.

---

# 19. Navigation và presentation

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
    Button("OK", role: .cancel) { }
} message: {
    Text(errorMessage)
}
```

Màn hình phức tạp nên model navigation state thay vì tích lũy nhiều Boolean không thể cùng đúng/sai hợp lý.

---

# 20. Networking căn bản với URLSession

```swift
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

Network success không chỉ là “request không throw”. Phải kiểm HTTP status, decode error, cancellation và error body khi cần. Intermediate sẽ mở rộng sang request construction, auth, retry, cache và idempotency.

---

# 21. Concurrency nhập môn — task, suspension và cancellation

```swift
func loadUser() async throws -> User {
    try await api.fetchUser()
}
```

`await` đánh dấu suspension point. Nó **không** có nghĩa “chuyển sang background thread”. Task có thể suspend để executor chạy công việc khác.

Trong SwiftUI:

```swift
.task {
    do {
        user = try await loadUser()
    } catch is CancellationError {
        // task bị cancel; thường không cần hiện lỗi cho user
    } catch {
        errorMessage = error.localizedDescription
    }
}
```

Cancellation là cooperative. `Task.cancel()` đánh dấu task; code hoặc API cần quan sát cancellation:

```swift
try Task.checkCancellation()
```

Đừng dùng `Task.detached` như cách mặc định để “chạy background”. Structured concurrency giữ lifetime/cancellation/priority relationship dễ reasoning hơn. Intermediate sẽ nối mental model này sang actors, isolation và `Sendable`.

Quan trọng: **ARC giải quyết lifetime của reference; concurrency giải quyết access đồng thời.** Object không leak vẫn có thể data race; object actor-isolated vẫn có thể bị giữ quá lâu. Hai bài toán khác nhau.

---

# 22. Persistence căn bản

## 22.1 UserDefaults

Dùng cho preference nhỏ:

```swift
UserDefaults.standard.set(true, forKey: "hasSeenOnboarding")
let value = UserDefaults.standard.bool(forKey: "hasSeenOnboarding")
```

Không dùng UserDefaults làm database lớn hoặc nơi lưu secret.

## 22.2 Keychain

Credential/token nhạy cảm nên nằm trong Keychain thay vì UserDefaults/plain file. Cần hiểu access group và accessibility option khi lên Intermediate/Senior.

## 22.3 SwiftData

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

```swift
@Query(sort: \Note.createdAt, order: .reverse)
private var notes: [Note]

@Environment(\.modelContext)
private var modelContext
```

SwiftData làm persistence ergonomic nhưng không loại bỏ schema/migration/query/concurrency problems. Core Data vẫn quan trọng trong production legacy và sẽ được học ở level sau.

## 22.4 File system sandbox

Documents, Application Support, Caches có mục đích khác nhau. User-generated data cần backup không nên nằm trong Caches; dữ liệu tái tạo được không nên làm phình backup.

```swift
let documents = FileManager.default.urls(
    for: .documentDirectory,
    in: .userDomainMask
).first!
```

Dùng URL API thay vì nối path string thủ công.

---

# 23. UIKit lifecycle — cần biết ngay cả khi học SwiftUI trước

UIKit là object/lifecycle-driven. Một view controller tối thiểu:

```swift
final class HomeViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemBackground
    }
}
```

Các callback chính:

`loadView()` tạo root view nếu bạn tự quản view hierarchy. `viewDidLoad()` chạy sau khi view load và thường chỉ một lần trong lifetime controller; phù hợp setup view, binding/delegate. `viewWillAppear(_:)`/`viewDidAppear(_:)` chạy mỗi lần màn hình chuẩn bị/đã hiện. `viewWillDisappear(_:)`/`viewDidDisappear(_:)` chạy khi rời màn hình. Đừng đặt one-time setup vào `viewWillAppear` nếu nó sẽ bị lặp vô ý.

Controller lifecycle khác app/scene lifecycle. App vào background không đồng nghĩa mọi view controller đều `viewDidDisappear` theo một quy luật đơn giản.

Auto Layout constraint mô tả quan hệ layout; safe area tránh system bars/notch. `UITableView`/`UICollectionView` dùng cell reuse, nên cell phải reset/configure đầy đủ state khi reuse.

---

# 24. UIKit ↔ SwiftUI interoperability

SwiftUI có thể wrap UIKit bằng `UIViewRepresentable`/`UIViewControllerRepresentable`. UIKit có thể host SwiftUI bằng `UIHostingController`.

```swift
let controller = UIHostingController(rootView: ProfileView())
```

Representable có hai phase quan trọng: `makeUIView`/`makeUIViewController` tạo object UIKit, còn `updateUIView`/`updateUIViewController` đồng bộ state SwiftUI mới vào object đang tồn tại. Đừng tạo lại heavy controller trong `update...` mỗi lần state đổi.

Delegate/callback từ UIKit thường bridge qua `Coordinator`. Coordinator phải được thiết kế ownership cẩn thận để không tạo cycle giữa representable, coordinator và UIKit object.

Migration app lớn thường nên incremental: feature mới có thể SwiftUI trong `UIHostingController`, hoặc một control UIKit chưa có SwiftUI wrapper có thể được represent trong SwiftUI. “Rewrite toàn bộ” hiếm khi là requirement kỹ thuật mặc định.

---

# 25. Form, focus, gesture và animation

Control thường dùng: `TextField`, `SecureField`, `Toggle`, `Picker`, `DatePicker`, `Slider`, `Stepper`.

```swift
enum Field: Hashable { case email, password }
@FocusState private var focusedField: Field?

TextField("Email", text: $email)
    .focused($focusedField, equals: .email)
```

Animation state change:

```swift
withAnimation(.spring) {
    isExpanded.toggle()
}
```

Transition:

```swift
if isVisible {
    DetailView()
        .transition(.opacity.combined(with: .move(edge: .bottom)))
}
```

Gesture có thể cạnh tranh với system gesture; cần test trên OS/device thật, đặc biệt với selection, scroll và accessibility interaction.

---

# 26. Resource, localization và accessibility

Asset Catalog quản image/color/resource. SF Symbols:

```swift
Image(systemName: "heart.fill")
```

Localization không chỉ là thay text. Layout phải chịu được string dài, pluralization, RTL, locale-specific date/number.

Accessibility là chức năng:

```swift
.accessibilityLabel("Favorite")
.accessibilityHint("Marks this item as favorite")
```

Test Dynamic Type, VoiceOver, contrast, tap target và Reduce Motion. UI đẹp ở default font size nhưng vỡ ở accessibility size vẫn là bug.

---

# 27. Debugging, test và memory tools

Breakpoint, exception breakpoint, LLDB:

```text
po object
p expression
bt
thread backtrace
```

Production logging dùng `Logger`/OSLog thay vì `print` tràn lan; không log access token/password/PII.

Swift Testing:

```swift
import Testing

@Test
func totalPrice() {
    #expect(10 + 20 == 30)
}
```

XCTest vẫn phổ biến trong codebase hiện hữu.

Memory Graph giúp xem retain path/cycle. Instruments sẽ được học sâu hơn ở Advanced.

---

# 28. Swift Package Manager và module nhập môn

SwiftPM/SPM quản package/dependency. Manifest:

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

Swift 6.4 đưa Swift Build thành build system mặc định của SwiftPM. Beginner chỉ cần hiểu package tạo module/dependency boundary thật; Intermediate sẽ học modularization và public API surface.

---

# 29. Signing và chạy trên device

Để chạy/phát hành app, executable phải được code signed. Phân biệt Apple Developer Program membership, Team, Certificate, App ID, Provisioning Profile, Entitlement và Capability.

`Automatically manage signing` phù hợp cho học tập và nhiều project nhỏ. Capability như Push Notifications, Associated Domains, App Groups hoặc Sign in with Apple có thể cần cả target entitlement lẫn portal/server configuration.

---

# 30. Xcode 27 / Swift 6.4 notes cho Beginner

Swift 6.4 là release stable ngày 15/09/2026. Với iOS app, phần quan trọng không phải học mọi proposal mới mà là nhận biết language/tooling đang tiếp tục tăng memory safety, ownership expressiveness, observation và build portability.

Xcode 27 đi với Swift 6.4/iOS 27 SDK. SwiftUI `State` implementation và builder internals tiếp tục tiến hóa; source app thông thường phần lớn không nên phụ thuộc implementation detail của wrapper/builder.

`AsyncImage`/network caching behavior và các API system có thể đổi theo SDK. Vì vậy khi tutorial cũ mâu thuẫn với release notes/API contract, ưu tiên documentation của toolchain đang build project.

---

# 31. Capstone Beginner — nối language → memory → UI → async → persistence

Hãy xây app “Reading List” có danh sách, chi tiết và form thêm/sửa. Model entity bằng `struct`/`enum`; `NavigationStack` cho navigation; local UI state dùng `@State`; shared observable model dùng Observation; REST bằng `URLSession`; decode Codable; bookmark bằng SwiftData; preference bằng UserDefaults; credential giả lập qua Keychain service.

Bắt buộc tự kiểm tra các failure path: server trả non-2xx, decode fail, task bị cancel, record không tồn tại, form invalid. Dùng Memory Graph để xác nhận một screen/model được giải phóng khi navigation pop nếu nó không còn owner.

## Checklist trước khi sang Intermediate

Bạn cần giải thích được, không chỉ viết được syntax:

1. Vì sao `struct` và `class` có semantics khác nhau; copy một struct chứa class reference có ý nghĩa gì.
2. Optional khác default value như thế nào; khi nào `guard let`, `??`, optional chaining phù hợp.
3. Closure escaping sống lâu hơn call stack ra sao; capture list tham gia retain cycle thế nào.
4. ARC giải quyết object lifetime nhưng không giải quyết data race như thế nào.
5. Vì sao `await` là suspension point chứ không phải synonym của background thread.
6. Ai sở hữu `@State`; `@Binding` khác ownership ra sao; Observable model khác local state thế nào.
7. UIKit controller có các lifecycle callback nào và vì sao `viewDidLoad` không tương đương `viewWillAppear`.
8. Deployment target khác SDK/compiler version thế nào.
9. Network/persistence có failure là trạng thái bình thường chứ không phải exception hiếm.
10. Cách dùng Xcode breakpoint, test và Memory Graph để xác minh assumption thay vì đoán.

Nếu các câu trên còn mơ hồ, hãy quay lại section tương ứng trước khi học actor, `Sendable`, architecture và advanced state management ở Intermediate.