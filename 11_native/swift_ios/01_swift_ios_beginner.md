# Swift & iOS Master ghi chú (note / 노트) — Beginner

> **Mạch đọc:** Đặt **Swift & iOS Master ghi chú (note / 노트) — Beginner** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **0.1 Swift phiên bản (version / 버전), ngôn ngữ (language / 언어) chế độ (mode / 모드), Xcode, SDK và triển khai (deployment / 배포) mục tiêu (target / 대상)** sang **1.1 Cài và kiểm tra toolchain**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


> Phạm vi: Swift căn bản, tư duy lập trình, cấu trúc một ứng dụng iOS, Xcode, Foundation, SwiftUI, UIKit, trạng thái (state / 상태), networking, persistence và tính đồng thời (concurrency / 동시성) ở mức nhập môn.
>
> Baseline thực hành: **Xcode 27 + Swift 6.4 + iOS 27 SDK**. Xcode 27.1/27.2 đang ở beta tại thời điểm cập nhật 21/09/2026 nên không được dùng làm baseline stable.

Tài liệu này không phải cheat sheet. Mục tiêu của Beginner là tạo một mô hình tư duy (mental model / 사고 모델) đủ chắc để khi sang Intermediate, các chủ đề như actor, `Sendable`, Observation, kiến trúc (architecture / 아키텍처) hay persistence không trở thành những annotation/API phải học thuộc lòng. Hãy đọc theo thứ tự; những phần sau giả định bạn hiểu quyền sở hữu (ownership / 소유권), Optional, giá trị (value / 값)/tham chiếu (reference / 참조) ngữ nghĩa (semantics / 의미론) và closure ở các phần trước.

---

# 0. Swift, iOS, SDK và Xcode là những lớp khác nhau

Swift là ngôn ngữ lập trình. iOS là hệ điều hành. iOS SDK là tập khung phần mềm (framework / 프레임워크) và API mà app dùng để tương tác với hệ điều hành. Xcode là IDE/toolchain chính thức chứa trình biên dịch (compiler / 컴파일러), linker, debugger LLDB, hệ thống dựng (build system / 빌드 시스템), Simulator, Instruments, signing tích hợp (integration / 통합) và các công cụ bản phát hành (release / 릴리스).

Các khung phần mềm (framework / 프레임워크) nền tảng cần phân biệt sớm. `Swift Standard Library` cung cấp `Int`, `String`, `Array`, `Optional`, collection algorithms và phần lớn thành phần nguyên thủy (primitive / 기본 요소) của ngôn ngữ. `Foundation` bổ sung `Date`, `URL`, `Data`, `FileManager`, `URLSession`, encoding và nhiều API platform-neutral. `SwiftUI` là khung phần mềm (framework / 프레임워크) UI declarative hiện đại. `UIKit` là khung phần mềm (framework / 프레임워크) UI imperative/lifecycle-driven truyền thống nhưng vẫn rất quan trọng trong môi trường vận hành (production / 운영 환경), SDK tích hợp (integration / 통합) và codebase legacy.

## 0.1 Swift phiên bản (version / 버전), ngôn ngữ (language / 언어) chế độ (mode / 모드), Xcode, SDK và triển khai (deployment / 배포) mục tiêu (target / 대상)

Đây là năm khái niệm liên quan nhưng không đồng nhất. Xcode chứa một Swift trình biên dịch (compiler / 컴파일러) cụ thể và các SDK cụ thể. Swift ngôn ngữ (language / 언어) chế độ (mode / 모드) quyết định tập ngữ nghĩa (semantics / 의미론)/ngôn ngữ (language / 언어) rules mà mục tiêu (target / 대상) dùng. SDK phiên bản (version / 버전) quyết định trình biên dịch (compiler / 컴파일러) biết những API nền tảng (platform / 플랫폼) nào. triển khai (deployment / 배포) mục tiêu (target / 대상) lại là OS thấp nhất app hỗ trợ ở thời gian chạy (runtime / 런타임).

Ví dụ, một app có thể bản dựng (build / 빌드) bằng Xcode 27/Swift 6.4 nhưng triển khai (deployment / 배포) mục tiêu (target / 대상) là iOS 17. trình biên dịch (compiler / 컴파일러) hiểu cú pháp Swift 6.4, nhưng API chỉ tồn tại từ iOS 27 phải được bảo vệ bằng availability:

```swift
if #available(iOS 27.0, *) {
    // API chỉ dùng khi runtime đủ mới
} else {
    // fallback
}
```

Compile-time điều kiện (condition / 조건) như `#if DEBUG`, `#if os(iOS)` hoặc `#if canImport(...)` là chuyện khác: nó quyết định nguồn (source / 소스) nào được compile, không phải branch thời gian chạy (runtime / 런타임).

---

# 1. Làm quen Xcode trước khi viết app

## 1.1 Cài và kiểm tra toolchain

Xcode có thể được cài từ Mac App Store hoặc Apple nhà phát triển (developer / 개발자) Downloads. Nếu máy có nhiều Xcode:

```bash
sudo xcode-select -s /Applications/Xcode.app
xcodebuild -version
swift --version
```

Simulator giúp phản hồi (feedback / 피드백) nhanh nhưng không phải thiết bị thật. Camera, push notification, thermal hành vi (behavior / 동작), bộ nhớ (memory / 메모리) pressure, background thực thi (execution / 실행), Keychain, Bluetooth và hiệu năng (performance / 성능) cần được kiểm thử (test / 테스트) trên thiết bị (device / 장치) phù hợp.

## 1.2 dự án (project / 프로젝트), mục tiêu (target / 대상), scheme và bản dựng (build / 빌드) cấu hình (configuration / 구성)

Khi tạo `iOS > App`, Xcode tạo dự án (project / 프로젝트) chứa ít nhất một ứng dụng (application / 애플리케이션) mục tiêu (target / 대상). `Target` mô tả một sản phẩm bản dựng (build / 빌드) như app, kiểm thử (test / 테스트) bundle, widget hoặc khung phần mềm (framework / 프레임워크). `Scheme` mô tả cách bản dựng (build / 빌드)/run/kiểm thử (test / 테스트)/profile/archive mục tiêu (target / 대상). `Build Configuration` thường có gỡ lỗi (debug / 디버그) và bản phát hành (release / 릴리스). gỡ lỗi (debug / 디버그) ưu tiên debuggability; bản phát hành (release / 릴리스) bật tối ưu hóa (optimization / 최적화) và là nơi nhiều bug timing/dữ liệu (data / 데이터) race chỉ xuất hiện rõ.

`Bundle Identifier` thường có dạng reverse-domain như `com.example.reader`. Nó liên quan đến App ID, signing, push, keychain truy cập (access / 접근) group và App Store Connect.

SwiftUI app entry điểm (point / 지점) thường là:

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

`@main` đánh dấu entry điểm (point / 지점). `App` mô tả vòng đời (lifecycle / 생명주기) ở mức ứng dụng; `Scene` mô tả một presentation/cửa sổ (window / 윈도우) vòng đời (lifecycle / 생명주기).

---

# 2. Values, variables và hệ kiểu (type system / 타입 시스템) nền tảng

## 2.1 `let`, `var` và kiểu (type / 타입) suy luận (inference / 추론)

Mục này dùng implementation để kiểm tra API contract: input nào được chấp nhận, behavior nào được bảo đảm và boundary nào người gọi vẫn phải chịu trách nhiệm.

```swift
let appName = "Reader"
var launchCount = 0
launchCount += 1
```

`let` tạo binding không được gán lại; `var` cho phép mutation. Hãy ưu tiên `let` nếu không cần thay đổi vì nó làm bất biến (invariant / 불변식) rõ hơn cho trình biên dịch (compiler / 컴파일러) và người đọc.

Swift suy luận kiểu (type / 타입):

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

Các kiểu (type / 타입) thường gặp là `Int`, `UInt`, `Double`, `Float`. Trong app thông thường, dùng `Int` cho integer và `Double` cho floating-point trừ khi lĩnh vực (domain / 도메인)/interop yêu cầu kiểu (type / 타입) khác.

Swift không tự chuyển numeric kiểu (type / 타입) tùy ý:

```swift
let count = 10
let ratio = 2.5
let result = Double(count) * ratio
```

Floating-point không biểu diễn chính xác mọi số thập phân. Không dùng `Double` làm mô hình (model / 모델) tiền nếu lĩnh vực (domain / 도메인) yêu cầu decimal arithmetic chính xác; `Decimal` hoặc integer minor units thường phù hợp hơn tùy hệ thống.

Overflow integer thường trap trong bản dựng (build / 빌드) bình thường. Swift có overflow operator `&+`, `&-`, `&*`, nhưng chỉ dùng khi wraparound là ngữ nghĩa (semantics / 의미론) có chủ đích.

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

Nếu dữ liệu có ngữ nghĩa (semantic / 의미적) lâu dài, hãy dùng `struct` thay vì lan truyền tuple qua nhiều tầng (layer / 계층).

`typealias` tạo tên khác cho kiểu (type / 타입), không tạo kiểu (type / 타입) mới:

```swift
typealias UserID = UUID
```

Nếu cần trình biên dịch (compiler / 컴파일러) phân biệt `UserID` và `OrderID`, hãy tạo wrapper kiểu (type / 타입) thay vì hai `typealias UUID`.

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

Random truy cập (access / 접근) theo integer lặp đi lặp lại trên `String` có thể là dấu hiệu cấu trúc dữ liệu (data structure / 자료구조) sai. Với nhị phân (binary / 이진) giao thức (protocol / 프로토콜), dùng `Data`/byte-oriented API thay vì ép `String` thành byte array.

## 3.2 Array, Set, Dictionary

Mục này biến quy tắc collection thành hành vi có thể quan sát. Hãy đối chiếu kiểu dữ liệu, thứ tự duyệt, mutation và kết quả cuối để biết lựa chọn API nào giữ đúng contract của bài toán.

```swift
var names = ["An", "Bình", "Chi"]
names.append("Dung")

var tags: Set<String> = ["swift", "ios"]
tags.insert("xcode")

var scores = ["Alice": 90, "Bob": 80]
let bob = scores["Bob"] // Int?
```

`Array` có thứ tự và cho phép duplicate. `Set` giữ phần tử unique và yêu cầu `Hashable`. Dictionary lookup trả Optional vì key có thể không tồn tại.

Truy cập array chỉ mục (index / 인덱스) ngoài phạm vi (range / 범위) sẽ trap. Khi định danh (identity / 식별자) của UI item là thực thể (entity / 엔터티) định danh (identity / 식별자), không dùng chỉ mục (index / 인덱스) thay cho ID chỉ vì thuận tiện.

## 3.3 Collection algorithms

Mục này biến quy tắc collection thành hành vi có thể quan sát. Hãy đối chiếu kiểu dữ liệu, thứ tự duyệt, mutation và kết quả cuối để biết lựa chọn API nào giữ đúng contract của bài toán.

```swift
let activeNames = users
    .filter(\.isActive)
    .map(\.name)
    .sorted()

let numbers = ["1", "x", "3"].compactMap(Int.init)
```

`map` transform từng phần tử; `compactMap` transform và bỏ nil; `flatMap` flatten nested chuỗi (sequence / 시퀀스); `filter` giữ phần tử thỏa predicate; `reduce` gộp chuỗi (sequence / 시퀀스). Không cần biến mọi vòng lặp (loop / 루프) thành functional chuỗi (chain / 사슬): `for` vòng lặp (loop / 루프) vẫn tốt khi có early exit, mutation hoặc điều khiển (control / 제어) luồng (flow / 흐름) phức tạp.

---

# 4. điều khiển (control / 제어) luồng (flow / 흐름) và mẫu (pattern / 패턴) matching

## 4.1 `if`, ternary, `guard`

Đoạn code dưới đây là bằng chứng cho khái niệm vừa mở. Hãy đọc từ input và state đến output, ghi lại điều kiện áp dụng và giới hạn trước khi chuyển sang mục kế tiếp.

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

Đoạn code dưới đây là bằng chứng cho khái niệm vừa mở. Hãy đọc từ input và state đến output, ghi lại điều kiện áp dụng và giới hạn trước khi chuyển sang mục kế tiếp.

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

Swift không fall through mặc định. Exhaustiveness làm enum/máy trạng thái (state machine / 상태 머신) an toàn hơn khi thêm trường hợp (case / 사례) mới.

## 4.3 `if case`, `guard case`, `for case`

Mẫu (pattern / 패턴) matching không chỉ tồn tại trong `switch`:

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

Các form này hữu ích khi chỉ quan tâm một mẫu (pattern / 패턴) mà không cần `switch` đầy đủ.

## 4.4 vòng lặp (loop / 루프) và phạm vi (range / 범위)

Mục này biến quy tắc collection thành hành vi có thể quan sát. Hãy đối chiếu kiểu dữ liệu, thứ tự duyệt, mutation và kết quả cuối để biết lựa chọn API nào giữ đúng contract của bài toán.

```swift
for number in 1...5 { }
for number in 1..<5 { }

var retry = 3
while retry > 0 {
    retry -= 1
}
```

`...` là closed phạm vi (range / 범위), `..<` là half-open phạm vi (range / 범위). Collection mã (code / 코드) thường dùng half-open phạm vi (range / 범위) vì upper bound có thể là `endIndex`.

---

# 5. hàm (function / 함수), parameter và call-site thiết kế (design / 설계)

## 5.1 hàm (function / 함수) và argument label

Mục này dùng implementation để kiểm tra API contract: input nào được chấp nhận, behavior nào được bảo đảm và boundary nào người gọi vẫn phải chịu trách nhiệm.

```swift
func greet(_ person: String, from city: String) -> String {
    "Hello \(person) from \(city)"
}

greet("Minh", from: "Seoul")
```

Argument label là một phần của API readability. Swift API tốt nên đọc gần như một câu ở lời gọi (call / 호출) site.

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

## 5.2 hàm (function / 함수) là giá trị (value / 값)

Mục này dùng implementation để kiểm tra API contract: input nào được chấp nhận, behavior nào được bảo đảm và boundary nào người gọi vẫn phải chịu trách nhiệm.

```swift
func add(_ lhs: Int, _ rhs: Int) -> Int { lhs + rhs }
let operation: (Int, Int) -> Int = add
```

Hàm (function / 함수) có thể được truyền vào hàm (function / 함수) khác, lưu trong thuộc tính (property / 속성) hoặc trả về như giá trị (value / 값). Đây là nền tảng của closure, callback, higher-order hàm (function / 함수) và phụ thuộc (dependency / 의존성) injection bằng hàm (function / 함수) giá trị (value / 값).

## 5.3 `inout`

Parameter mặc định là giá trị (value / 값) được truyền vào theo ngữ nghĩa (semantics / 의미론) của kiểu (type / 타입). `inout` cho phép hàm (function / 함수) mutate caller lưu trữ (storage / 저장소):

```swift
func increment(_ value: inout Int) {
    value += 1
}

var count = 0
increment(&count)
```

`inout` không có nghĩa “pointer C thông thường”. Swift thực thi exclusivity quy tắc (rule / 규칙) để tránh hai truy cập (access / 접근) ghi/đọc xung đột cùng lưu trữ (storage / 저장소).

## 5.4 Overload và ambiguity

Swift cho phép nhiều hàm (function / 함수) cùng tên nếu signature khác nhau. Overload giúp API tự nhiên nhưng quá nhiều overload generic có thể khiến lời gọi (call / 호출) site/diagnostic khó hiểu. Khi ngữ nghĩa (semantic / 의미적) khác nhau rõ rệt, tên khác thường tốt hơn ép trình biên dịch (compiler / 컴파일러) đoán.

---

# 6. Optional — mô hình hóa sự vắng mặt trong hệ kiểu (type system / 타입 시스템)

`String?` là `Optional<String>`, nghĩa là có giá trị (value / 값) hoặc `nil`.

```swift
var nickname: String? = nil
nickname = "Tom"
```

## 6.1 Unwrap

Mục này dùng ví dụ để phân biệt giá trị có thể thiếu với giá trị đã được kiểm chứng. Hãy theo dõi điều kiện nào cho phép truy cập an toàn, failure mode nào còn lại và vì sao đoạn code không tự thay thế invariant của ứng dụng.

```swift
if let nickname {
    print(nickname)
}

let displayName = nickname ?? "Anonymous"
let length = user.profile?.name.count
```

`guard let` phù hợp với early-exit; nil coalescing `??` phù hợp default giá trị (value / 값); optional chaining phù hợp chuỗi thuộc tính (property / 속성)/phương thức (method / 메서드) có thể nil.

## 6.2 Force unwrap

Mục này dùng ví dụ để phân biệt giá trị có thể thiếu với giá trị đã được kiểm chứng. Hãy theo dõi điều kiện nào cho phép truy cập an toàn, failure mode nào còn lại và vì sao đoạn code không tự thay thế invariant của ứng dụng.

```swift
let value = nickname!
```

`!` là assertion thời gian chạy (runtime / 런타임). Nếu giá trị (value / 값) nil, app trap. Chỉ dùng khi bất biến (invariant / 불변식) thực sự được bảo đảm bởi thiết kế/khung phần mềm (framework / 프레임워크). “trình biên dịch (compiler / 컴파일러) đang báo lỗi” không phải lý do hợp lệ.

Implicitly unwrapped Optional (`String!`) vẫn xuất hiện trong IBOutlet/API Objective-C legacy. Hãy hiểu để maintain mã (code / 코드), không dùng làm default cho mô hình (model / 모델) mới.

---

# 7. Struct, lớp (class / 클래스), enum và giao thức (protocol / 프로토콜)

## 7.1 Struct và giá trị (value / 값) ngữ nghĩa (semantics / 의미론)

Mục này dùng implementation để kiểm tra API contract: input nào được chấp nhận, behavior nào được bảo đảm và boundary nào người gọi vẫn phải chịu trách nhiệm.

```swift
struct User {
    let id: UUID
    var name: String
}

var a = User(id: UUID(), name: "A")
var b = a
b.name = "B"
```

Về ngữ nghĩa (semantics / 의미론), `a` và `b` là hai giá trị (value / 값) độc lập. tiêu chuẩn (standard / 표준) collection như Array/String có thể dùng sao chép khi ghi (copy-on-write / 쓰기 시 복사) nội bộ để tránh bản sao (copy / 복사) vật lý không cần thiết, nhưng mã (code / 코드) của bạn vẫn phải lập luận (reasoning / 추론) như giá trị (value / 값) ngữ nghĩa (semantics / 의미론).

## 7.2 lớp (class / 클래스), định danh (identity / 식별자) và tham chiếu (reference / 참조) ngữ nghĩa (semantics / 의미론)

Mục này dùng implementation để kiểm tra API contract: input nào được chấp nhận, behavior nào được bảo đảm và boundary nào người gọi vẫn phải chịu trách nhiệm.

```swift
final class Session {
    var token: String?
}

let first = Session()
let second = first
print(first === second) // true
```

Nhiều tham chiếu (reference / 참조) có thể trỏ cùng instance. Vì vậy mutation qua một tham chiếu (reference / 참조) có thể được quan sát từ tham chiếu (reference / 참조) khác. `===` kiểm định danh (identity / 식별자), khác `==` là equality ngữ nghĩa (semantic / 의미적).

Nếu không chủ đích thiết kế inheritance, `final class` thường thể hiện intent tốt hơn.

## 7.3 Enum: raw giá trị (value / 값), associated giá trị (value / 값) và recursive trạng thái (state / 상태)

Mục này đặt đoạn code vào câu hỏi state thuộc owner nào và sống qua boundary nào. Hãy theo dõi identity, cập nhật và khôi phục để phân biệt state tạm với dữ liệu cần persistence.

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

Raw giá trị (value / 값) là giá trị cố định gắn với trường hợp (case / 사례). Associated giá trị (value / 값) mang payload khác nhau theo trường hợp (case / 사례). Đây là công cụ rất mạnh để loại bỏ trạng thái bất khả thi.

Enum recursive cần `indirect`:

```swift
indirect enum Expression {
    case number(Int)
    case add(Expression, Expression)
}
```

## 7.4 giao thức (protocol / 프로토콜)

Mục này dùng implementation để kiểm tra API contract: input nào được chấp nhận, behavior nào được bảo đảm và boundary nào người gọi vẫn phải chịu trách nhiệm.

```swift
protocol Displayable {
    var title: String { get }
    func displayText() -> String
}
```

Giao thức (protocol / 프로토콜) mô tả năng lực (capability / 역량)/đặc tả hợp đồng (contract / 계약). Không tạo giao thức (protocol / 프로토콜) chỉ vì “kiến trúc (architecture / 아키텍처) mẫu có giao thức (protocol / 프로토콜)”. giao thức (protocol / 프로토콜) có giá trị khi cần generic ràng buộc (constraint / 제약조건), substitution, cross-module đặc tả hợp đồng (contract / 계약) hoặc kiểm thử (test / 테스트) seam thực sự.

---

# 8. Initialization, extension, nested kiểu (type / 타입) và subscript

## 8.1 Initialization

Struct có memberwise initializer nếu điều kiện phù hợp. lớp (class / 클래스) có designated/convenience initializer và inheritance quy tắc (rule / 규칙) riêng. Failable initializer dùng `init?` khi đầu vào (input / 입력) có thể không tạo được giá trị (value / 값) hợp lệ.

```swift
struct EmailAddress {
    let value: String

    init?(_ value: String) {
        guard value.contains("@") else { return nil }
        self.value = value
    }
}
```

Initializer phải đưa đối tượng (object / 객체) vào trạng thái hợp lệ trước khi sử dụng `self` tự do. Đừng đẩy đối tượng (object / 객체) “nửa khởi tạo” ra bên ngoài rồi mong caller nhớ gọi `setup()` nếu bất biến (invariant / 불변식) có thể đảm bảo ngay trong init.

## 8.2 Extension

Mục này dùng implementation để kiểm tra API contract: input nào được chấp nhận, behavior nào được bảo đảm và boundary nào người gọi vẫn phải chịu trách nhiệm.

```swift
extension String {
    var isBlank: Bool {
        trimmingCharacters(in: .whitespacesAndNewlines).isEmpty
    }
}
```

Extension nhóm hành vi (behavior / 동작)/conformance tốt, nhưng đừng rải một kiểu (type / 타입) thành hàng chục extension không có ranh giới (boundary / 경계) rõ ràng.

## 8.3 Nested kiểu (type / 타입)

Mục này dùng implementation để kiểm tra API contract: input nào được chấp nhận, behavior nào được bảo đảm và boundary nào người gọi vẫn phải chịu trách nhiệm.

```swift
struct APIRequest {
    enum Method {
        case get, post
    }
}
```

Nested kiểu (type / 타입) hữu ích khi kiểu (type / 타입) con chỉ có ý nghĩa trong không gian tên (namespace / 네임스페이스) của kiểu (type / 타입) cha.

## 8.4 Subscript

Đoạn code dưới đây là bằng chứng cho khái niệm vừa mở. Hãy đọc từ input và state đến output, ghi lại điều kiện áp dụng và giới hạn trước khi chuyển sang mục kế tiếp.

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

Subscript nên có ngữ nghĩa (semantics / 의미론) truy cập giống collection/chỉ mục (index / 인덱스), không nên che một thao tác (operation / 연산) đắt đỏ hoặc side tác động (effect / 효과) khó đoán.

---

# 9. thuộc tính (property / 속성), phương thức (method / 메서드) và type-level member

Stored thuộc tính (property / 속성) giữ dữ liệu; computed thuộc tính (property / 속성) tính giá trị (value / 값):

```swift
struct Rectangle {
    var width: Double
    var height: Double

    var area: Double { width * height }
}
```

Thuộc tính (property / 속성) observer:

```swift
var progress = 0.0 {
    didSet {
        print("\(oldValue) -> \(progress)")
    }
}
```

Struct phương thức (method / 메서드) cần `mutating` nếu sửa trạng thái (state / 상태):

```swift
struct Counter {
    private(set) var value = 0

    mutating func increment() {
        value += 1
    }
}
```

`static` member thuộc kiểu (type / 타입). lớp (class / 클래스) còn có `class` member cho phép subclass override:

```swift
class BaseFormatter {
    class var identifier: String { "base" }
}
```

Ưu tiên `static` nếu không có nhu cầu override.

---

# 10. kiểm soát truy cập (access control / 접근 제어)

Các mức chính: `open`, `public`, `package`, `internal`, `fileprivate`, `private`.

`internal` là mặc định trong mô-đun (module / 모듈). `package` chia sẻ trong cùng Swift gói (package / 패키지) nhưng không công khai (public / 공개) ra bên tiêu thụ (consumer / 소비자) bên ngoài gói (package / 패키지). `public` expose API ra mô-đun (module / 모듈) khác nhưng không cho subclass/override lớp (class / 클래스) member ngoài mô-đun (module / 모듈); `open` cho phép điều đó.

Nguyên tắc thực dụng: API surface càng nhỏ, bất biến (invariant / 불변식) càng dễ giữ. Để hiện thực (implementation / 구현) detail là `private`/`internal` trừ khi bên tiêu thụ (consumer / 소비자) thật sự cần.

---

# 11. Closure — thời gian tồn tại (lifetime / 수명), capture và `@escaping`

Closure là hàm (function / 함수) giá trị (value / 값) không tên:

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

Closure parameter mặc định là non-escaping: closure phải được gọi trước khi hàm (function / 함수) return. Nếu closure được giữ lại để gọi sau, parameter cần `@escaping`:

```swift
final class Loader {
    private var completion: (() -> Void)?

    func start(completion: @escaping () -> Void) {
        self.completion = completion
    }
}
```

Escaping closure quan trọng vì thời gian tồn tại (lifetime / 수명) dài hơn ngăn xếp lời gọi (call stack / 호출 스택) và có thể tham gia quyền sở hữu (ownership / 소유권) cycle.

## 11.2 Capture danh sách (list / 목록)

Closure giữ các giá trị (value / 값)/tham chiếu (reference / 참조) nó dùng. Với lớp (class / 클래스) tham chiếu (reference / 참조), default capture thường là strong:

```swift
service.fetch { [weak self] result in
    guard let self else { return }
    self.handle(result)
}
```

Capture danh sách (list / 목록) cũng có thể snapshot một giá trị (value / 값) tại thời điểm closure được tạo:

```swift
var message = "A"
let closure = { [message] in print(message) }
message = "B"
closure() // A
```

Không thêm `[weak self]` máy móc. Hãy hỏi closure được ai giữ, sống bao lâu và thao tác (operation / 연산) có nên tiếp tục khi đơn vị sở hữu (owner / 오너) biến mất hay không.

## 11.3 `@autoclosure`

`@autoclosure` cho phép caller truyền expression thay vì viết `{ ... }`. Nó phù hợp API như assertion/lazy expression nhưng dễ che điều khiển (control / 제어) luồng (flow / 흐름); app mã (code / 코드) hiếm khi cần tự thiết kế API kiểu này.

---

# 12. ARC và bộ nhớ (memory / 메모리) quyền sở hữu (ownership / 소유권) — mô hình tư duy (mental model / 사고 모델) bắt buộc

Swift dùng Automatic tham chiếu (reference / 참조) Counting cho lớp (class / 클래스)/reference-counted đối tượng (object / 객체). ARC tự chèn retain/bản phát hành (release / 릴리스) theo thời gian tồn tại (lifetime / 수명), nhưng ARC không phải garbage collector dò cycle.

## 12.1 Strong tham chiếu (reference / 참조) và đối tượng (object / 객체) thời gian tồn tại (lifetime / 수명)

Mục này dùng implementation để kiểm tra API contract: input nào được chấp nhận, behavior nào được bảo đảm và boundary nào người gọi vẫn phải chịu trách nhiệm.

```swift
final class Owner {
    let name: String
    init(name: String) { self.name = name }
    deinit { print("released \(name)") }
}

var owner: Owner? = Owner(name: "A")
owner = nil
```

Khi strong tham chiếu (reference / 참조) cuối cùng mất đi, instance có thể deinitialize. `deinit` phù hợp cleanup synchronous/tài nguyên (resource / 자원) quyền sở hữu (ownership / 소유권) rõ, nhưng không phải nơi đáng tin để gửi mạng (network / 네트워크) yêu cầu (request / 요청) hoặc lưu nghiệp vụ (business / 비즈니스) dữ liệu (data / 데이터) quan trọng.

## 12.2 Retain cycle giữa đối tượng (object / 객체)

Mục này dùng implementation để kiểm tra API contract: input nào được chấp nhận, behavior nào được bảo đảm và boundary nào người gọi vẫn phải chịu trách nhiệm.

```swift
final class Parent {
    var child: Child?
}

final class Child {
    weak var parent: Parent?
}
```

Nếu cả `Parent.child` và `Child.parent` đều strong, hai đối tượng (object / 객체) giữ nhau và ARC không thể giảm count về zero. `weak` không giữ đối tượng (object / 객체) sống và luôn đọc được như Optional vì mục tiêu (target / 대상) có thể biến mất.

`unowned` cũng không retain nhưng biểu diễn bất biến (invariant / 불변식) mạnh hơn: tham chiếu (reference / 참조) phải còn sống mỗi khi truy cập. Nếu bất biến (invariant / 불변식) sai, chương trình trap. Chỉ dùng `unowned` khi thời gian tồn tại (lifetime / 수명) quan hệ (relation / 관계) thực sự được chứng minh, không phải để tránh viết `?`.

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

Nếu closure chỉ tồn tại trong một lời gọi (call / 호출) synchronous và không được giữ, strong capture có thể hoàn toàn đúng. quyền sở hữu (ownership / 소유권) đồ thị (graph / 그래프) quan trọng hơn quy tắc “closure luôn weak self”.

## 12.4 giá trị (value / 값) kiểu (type / 타입) vẫn có thể giữ tham chiếu (reference / 참조)

Struct không có định danh (identity / 식별자) ARC riêng, nhưng trường dữ liệu (field / 필드) của struct có thể là lớp (class / 클래스) tham chiếu (reference / 참조):

```swift
struct Container {
    var session: Session
}
```

Bản sao (copy / 복사) `Container` không nhất thiết tạo `Session` mới. Hai bộ chứa (container / 컨테이너) giá trị (value / 값) có thể vẫn giữ cùng instance. Vì vậy “struct = mọi thứ deep copied” là mô hình tư duy (mental model / 사고 모델) sai.

## 12.5 ngăn xếp (stack / 스택), vùng nhớ động (heap / 힙) và thứ thật sự cần nhớ

Không nên học Swift theo quy tắc đơn giản “struct ở ngăn xếp (stack / 스택), lớp (class / 클래스) ở vùng nhớ động (heap / 힙)”. trình biên dịch (compiler / 컴파일러) có quyền optimize/box/escape giá trị (value / 값). Điều có ý nghĩa ở nguồn (source / 소스) mức (level / 수준) là giá trị (value / 값) ngữ nghĩa (semantics / 의미론), tham chiếu (reference / 참조) định danh (identity / 식별자), quyền sở hữu (ownership / 소유권) và thời gian tồn tại (lifetime / 수명). ngăn xếp (stack / 스택)/vùng nhớ động (heap / 힙) hữu ích khi profiling low-level, nhưng không thay ngữ nghĩa (semantics / 의미론) ngôn ngữ.

## 12.6 gỡ lỗi (debug / 디버그) bộ nhớ (memory / 메모리)

Khi nghi leak, dùng Xcode bộ nhớ (memory / 메모리) đồ thị (graph / 그래프) để xem retain đường dẫn (path / 경로); Instruments Allocations/Leaks để quan sát allocation/thời gian tồn tại (lifetime / 수명). Đừng kết luận mọi bộ nhớ (memory / 메모리) growth là leak: bộ nhớ đệm (cache / 캐시) hợp lệ, ảnh (image / 이미지) decode và đối tượng (object / 객체) sống lâu có thể tăng resident bộ nhớ (memory / 메모리) mà không tạo unreachable cycle.

---

# 13. lỗi (error / 오류) handling và cleanup

Đoạn code dưới đây là bằng chứng cho khái niệm vừa mở. Hãy đọc từ input và state đến output, ghi lại điều kiện áp dụng và giới hạn trước khi chuyển sang mục kế tiếp.

```swift
enum LoginError: Error {
    case invalidCredentials
    case networkUnavailable
}

func login() throws -> User {
    throw LoginError.invalidCredentials
}
```

Lời gọi (call / 호출):

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

`try?` biến thất bại (failure / 실패) thành nil; `try!` trap nếu lỗi (error / 오류) xảy ra. `try!` không phù hợp với mạng (network / 네트워크)/tệp (file / 파일) I/O vốn có thất bại (failure / 실패) hợp lệ.

`defer` đảm bảo mã (code / 코드) chạy khi rời phạm vi (scope / 범위):

```swift
func work() {
    acquireResource()
    defer { releaseResource() }
    performWork()
}
```

---

# 14. Generic căn bản, KeyPath và kiểu (type / 타입) casting

Generic tái sử dụng lô-gic (logic / 논리) mà giữ kiểu (type / 타입) an toàn (safety / 안전):

```swift
func first<T>(_ items: [T]) -> T? {
    items.first
}

func contains<T: Equatable>(_ value: T, in values: [T]) -> Bool {
    values.contains(value)
}
```

KeyPath là đường dẫn thuộc tính (property / 속성) có kiểu (type / 타입):

```swift
let path: KeyPath<User, String> = \.name
let name = user[keyPath: path]
```

Thời gian chạy (runtime / 런타임) cast:

```swift
if let viewController = value as? UIViewController {
    // cast thành công
}
```

`is` kiểm kiểu (type / 타입); `as?` trả Optional; `as!` trap nếu sai. `Any` hữu ích ở ranh giới (boundary / 경계) động/legacy nhưng nếu `[String: Any]` lan vào lĩnh vực (domain / 도메인) mô hình (model / 모델) thì thường nên thay bằng struct/enum/Codable.

---

# 15. Regex hiện đại

Swift hỗ trợ Regex và regex literal trên toolchain hiện đại:

```swift
let pattern = /[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/

if input.wholeMatch(of: pattern) != nil {
    print("format looks valid")
}
```

Regex phù hợp mẫu (pattern / 패턴) matching/extraction, không phải parser cho grammar phức tạp hay HTML tổng quát. kiểm tra hợp lệ (validation / 검증) format cũng không chứng minh tài nguyên (resource / 자원) tồn tại; email nhìn hợp lệ chưa có nghĩa mailbox thật.

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

Nếu lô-gic (logic / 논리) là “ngày mai theo lịch”, không tự cộng 86.400 giây vì DST/calendar có thể làm giả định (assumption / 가정) sai.

## 16.2 URL và URLComponents

Đoạn code dưới đây là bằng chứng cho khái niệm vừa mở. Hãy đọc từ input và state đến output, ghi lại điều kiện áp dụng và giới hạn trước khi chuyển sang mục kế tiếp.

```swift
var components = URLComponents(string: "https://api.example.com/search")!
components.queryItems = [
    URLQueryItem(name: "q", value: "swift ios")
]
let url = components.url!
```

Không tự nối truy vấn (query / 쿼리) string vì escaping/encoding dễ sai.

## 16.3 `Codable`

Đoạn code dưới đây là bằng chứng cho khái niệm vừa mở. Hãy đọc từ input và state đến output, ghi lại điều kiện áp dụng và giới hạn trước khi chuyển sang mục kế tiếp.

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

DTO từ máy chủ (server / 서버) và lĩnh vực (domain / 도메인) mô hình (model / 모델) không bắt buộc là một kiểu (type / 타입). Khi API shape khác lĩnh vực (domain / 도메인) ngữ nghĩa (semantics / 의미론), ánh xạ (mapping / 매핑) riêng làm ranh giới (boundary / 경계) rõ hơn.

---

# 17. SwiftUI: UI là hàm (function / 함수) của trạng thái (state / 상태)

SwiftUI declarative nghĩa là bạn mô tả UI tương ứng với trạng thái (state / 상태) hiện tại:

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

`View` là giá trị (value / 값) description. Đừng mang mô hình tư duy (mental model / 사고 모델) “View đối tượng (object / 객체) sống cố định và tôi mutate label.văn bản (text / 텍스트)” từ UIKit sang SwiftUI.

## 17.1 Modifier và thứ tự (order / 순서)

Đoạn code dưới đây là bằng chứng cho khái niệm vừa mở. Hãy đọc từ input và state đến output, ghi lại điều kiện áp dụng và giới hạn trước khi chuyển sang mục kế tiếp.

```swift
Text("Hello")
    .font(.title)
    .padding()
    .background(.thinMaterial)
```

Modifier trả về view description mới; thứ tự có thể thay đổi bố cục (layout / 레이아웃)/visual tác động (effect / 효과).

## 17.2 bố cục (layout / 레이아웃)

`VStack`, `HStack`, `ZStack`, `Spacer`, `frame`, `padding`, alignment và bố cục (layout / 레이아웃) priority là thành phần nguyên thủy (primitive / 기본 요소) chính. SwiftUI bố cục (layout / 레이아웃) là negotiation: parent propose kích thước (size / 크기), child chọn kích thước (size / 크기) phù hợp, parent đặt child. `frame` không đơn giản là UIKit frame assignment.

## 17.3 danh sách (list / 목록) và định danh (identity / 식별자)

Đoạn code dưới đây là bằng chứng cho khái niệm vừa mở. Hãy đọc từ input và state đến output, ghi lại điều kiện áp dụng và giới hạn trước khi chuyển sang mục kế tiếp.

```swift
struct Item: Identifiable {
    let id: UUID
    let title: String
}

List(items) { item in
    Text(item.title)
}
```

Định danh (identity / 식별자) phải ổn định qua insert/delete/reorder. `ForEach(items.indices, id: \.self)` không phải replacement cho thực thể (entity / 엔터티) ID khi collection thay đổi.

---

# 18. SwiftUI trạng thái (state / 상태) và quyền sở hữu (ownership / 소유권)

Trước khi chọn wrapper, hỏi: **ai sở hữu giá trị (value / 값), ai được mutate, thời gian tồn tại (lifetime / 수명) thuộc đâu?**

## 18.1 `@State`

Mục này đặt đoạn code vào câu hỏi state thuộc owner nào và sống qua boundary nào. Hãy theo dõi identity, cập nhật và khôi phục để phân biệt state tạm với dữ liệu cần persistence.

```swift
@State private var isPresented = false
```

Dùng cho cục bộ (local / 로컬) mutable trạng thái (state / 상태) mà view định danh (identity / 식별자) sở hữu. `@State` không phải cách biến mọi thuộc tính (property / 속성) thành mutable; derived giá trị (value / 값) nên được tính từ nguồn (source / 소스) trạng thái (state / 상태) thay vì lưu trùng.

## 18.2 `@Binding`

Mục này đặt đoạn code vào câu hỏi state thuộc owner nào và sống qua boundary nào. Hãy theo dõi identity, cập nhật và khôi phục để phân biệt state tạm với dữ liệu cần persistence.

```swift
struct ToggleRow: View {
    @Binding var isOn: Bool

    var body: some View {
        Toggle("Enabled", isOn: $isOn)
    }
}
```

Binding không sở hữu giá trị (value / 값); nó là read/ghi (write / 쓰기) projection tới trạng thái (state / 상태) do nơi khác sở hữu.

## 18.3 Observation hiện đại

Mục này đặt đoạn code vào câu hỏi state thuộc owner nào và sống qua boundary nào. Hãy theo dõi identity, cập nhật và khôi phục để phân biệt state tạm với dữ liệu cần persistence.

```swift
import Observation

@Observable
final class ProfileModel {
    var name = ""
    var isLoading = false
}
```

SwiftUI theo dõi thuộc tính (property / 속성) observable mà view đọc. `ObservableObject`, `@Published`, `@StateObject`, `@ObservedObject` vẫn cần biết để maintain mục tiêu (target / 대상) cũ/mã (code / 코드) legacy.

## 18.4 môi trường (environment / 환경)

Đoạn code dưới đây là bằng chứng cho khái niệm vừa mở. Hãy đọc từ input và state đến output, ghi lại điều kiện áp dụng và giới hạn trước khi chuyển sang mục kế tiếp.

```swift
@Environment(\.dismiss) private var dismiss
```

Môi trường (environment / 환경) phù hợp ngữ cảnh (context / 맥락)/phụ thuộc (dependency / 의존성) theo view cây (tree / 트리), nhưng không nên trở thành toàn cục (global / 전역) dịch vụ (service / 서비스) locator. phụ thuộc (dependency / 의존성) nghiệp vụ (business / 비즈니스) bắt buộc nên có quyền sở hữu (ownership / 소유권) rõ ở composition gốc (root / 루트)/initializer khi phù hợp.

---

# 19. điều hướng (navigation / 내비게이션) và presentation

Mục này đặt đoạn code vào câu hỏi state thuộc owner nào và sống qua boundary nào. Hãy theo dõi identity, cập nhật và khôi phục để phân biệt state tạm với dữ liệu cần persistence.

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

Màn hình phức tạp nên mô hình (model / 모델) điều hướng (navigation / 내비게이션) trạng thái (state / 상태) thay vì tích lũy nhiều Boolean không thể cùng đúng/sai hợp lý.

---

# 20. Networking căn bản với URLSession

Mục này nối khái niệm với một cấu trúc có thể kiểm tra trong project. Hãy đọc code theo ownership, failure mode và bằng chứng runtime, rồi đối chiếu xem nó giải quyết câu hỏi kiến trúc nào.

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

Mạng (network / 네트워크) success không chỉ là “yêu cầu (request / 요청) không throw”. Phải kiểm HTTP status, decode lỗi (error / 오류), cancellation và lỗi (error / 오류) body khi cần. Intermediate sẽ mở rộng sang yêu cầu (request / 요청) construction, auth, thử lại (retry / 재시도), bộ nhớ đệm (cache / 캐시) và idempotency.

---

# 21. tính đồng thời (concurrency / 동시성) nhập môn — tác vụ (task / 작업), suspension và cancellation

Mục này dùng code để làm rõ lifetime và cancellation của công việc bất đồng bộ. Hãy xác định ai sở hữu task, nó chạy ở context nào, khi nào hoàn tất hoặc bị hủy, rồi mới đánh giá cú pháp.

```swift
func loadUser() async throws -> User {
    try await api.fetchUser()
}
```

`await` đánh dấu suspension điểm (point / 지점). Nó **không** có nghĩa “chuyển sang background luồng thực thi (thread / 스레드)”. tác vụ (task / 작업) có thể suspend để executor chạy công việc khác.

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

Cancellation là cooperative. `Task.cancel()` đánh dấu tác vụ (task / 작업); mã (code / 코드) hoặc API cần quan sát cancellation:

```swift
try Task.checkCancellation()
```

Đừng dùng `Task.detached` như cách mặc định để “chạy background”. Structured tính đồng thời (concurrency / 동시성) giữ thời gian tồn tại (lifetime / 수명)/cancellation/priority relationship dễ lập luận (reasoning / 추론) hơn. Intermediate sẽ nối mô hình tư duy (mental model / 사고 모델) này sang actors, isolation và `Sendable`.

Quan trọng: **ARC giải quyết thời gian tồn tại (lifetime / 수명) của tham chiếu (reference / 참조); tính đồng thời (concurrency / 동시성) giải quyết truy cập (access / 접근) đồng thời.** đối tượng (object / 객체) không leak vẫn có thể dữ liệu (data / 데이터) race; đối tượng (object / 객체) actor-isolated vẫn có thể bị giữ quá lâu. Hai bài toán khác nhau.

---

# 22. Persistence căn bản

## 22.1 UserDefaults

Dùng cho preference nhỏ:

```swift
UserDefaults.standard.set(true, forKey: "hasSeenOnboarding")
let value = UserDefaults.standard.bool(forKey: "hasSeenOnboarding")
```

Không dùng UserDefaults làm cơ sở dữ liệu (database / 데이터베이스) lớn hoặc nơi lưu secret.

## 22.2 Keychain

Credential/đơn vị từ (token / 토큰) nhạy cảm nên nằm trong Keychain thay vì UserDefaults/plain tệp (file / 파일). Cần hiểu truy cập (access / 접근) group và khả năng tiếp cận (accessibility / 접근성) option khi lên Intermediate/cấp cao (senior / 시니어).

## 22.3 SwiftData

Đoạn code dưới đây là bằng chứng cho khái niệm vừa mở. Hãy đọc từ input và state đến output, ghi lại điều kiện áp dụng và giới hạn trước khi chuyển sang mục kế tiếp.

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

SwiftData làm persistence ergonomic nhưng không loại bỏ lược đồ (schema / 스키마)/di chuyển (migration / 마이그레이션)/truy vấn (query / 쿼리)/tính đồng thời (concurrency / 동시성) problems. cốt lõi (core / 핵심) dữ liệu (data / 데이터) vẫn quan trọng trong môi trường vận hành (production / 운영 환경) legacy và sẽ được học ở mức (level / 수준) sau.

## 22.4 tệp (file / 파일) hệ thống (system / 시스템) sandbox

Documents, ứng dụng (application / 애플리케이션) hỗ trợ (support / 지원), Caches có mục đích khác nhau. User-generated dữ liệu (data / 데이터) cần backup không nên nằm trong Caches; dữ liệu tái tạo được không nên làm phình backup.

```swift
let documents = FileManager.default.urls(
    for: .documentDirectory,
    in: .userDomainMask
).first!
```

Dùng URL API thay vì nối đường dẫn (path / 경로) string thủ công.

---

# 23. UIKit vòng đời (lifecycle / 생명주기) — cần biết ngay cả khi học SwiftUI trước

UIKit là đối tượng (object / 객체)/lifecycle-driven. Một view controller tối thiểu:

```swift
final class HomeViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemBackground
    }
}
```

Các callback chính:

`loadView()` tạo gốc (root / 루트) view nếu bạn tự quản view hierarchy. `viewDidLoad()` chạy sau khi view tải (load / 로드) và thường chỉ một lần trong thời gian tồn tại (lifetime / 수명) controller; phù hợp setup view, binding/delegate. `viewWillAppear(_:)`/`viewDidAppear(_:)` chạy mỗi lần màn hình chuẩn bị/đã hiện. `viewWillDisappear(_:)`/`viewDidDisappear(_:)` chạy khi rời màn hình. Đừng đặt one-time setup vào `viewWillAppear` nếu nó sẽ bị lặp vô ý.

Controller vòng đời (lifecycle / 생명주기) khác app/scene vòng đời (lifecycle / 생명주기). App vào background không đồng nghĩa mọi view controller đều `viewDidDisappear` theo một quy luật đơn giản.

Auto bố cục (layout / 레이아웃) ràng buộc (constraint / 제약조건) mô tả quan hệ bố cục (layout / 레이아웃); safe area tránh hệ thống (system / 시스템) bars/notch. `UITableView`/`UICollectionView` dùng cell reuse, nên cell phải reset/configure đầy đủ trạng thái (state / 상태) khi reuse.

---

# 24. UIKit ↔ SwiftUI interoperability

SwiftUI có thể wrap UIKit bằng `UIViewRepresentable`/`UIViewControllerRepresentable`. UIKit có thể host SwiftUI bằng `UIHostingController`.

```swift
let controller = UIHostingController(rootView: ProfileView())
```

Representable có hai phase quan trọng: `makeUIView`/`makeUIViewController` tạo đối tượng (object / 객체) UIKit, còn `updateUIView`/`updateUIViewController` đồng bộ trạng thái (state / 상태) SwiftUI mới vào đối tượng (object / 객체) đang tồn tại. Đừng tạo lại heavy controller trong `update...` mỗi lần trạng thái (state / 상태) đổi.

Delegate/callback từ UIKit thường cầu nối (bridge / 브리지) qua `Coordinator`. Coordinator phải được thiết kế quyền sở hữu (ownership / 소유권) cẩn thận để không tạo cycle giữa representable, coordinator và UIKit đối tượng (object / 객체).

Di chuyển (migration / 마이그레이션) app lớn thường nên incremental: tính năng (feature / 기능) mới có thể SwiftUI trong `UIHostingController`, hoặc một điều khiển (control / 제어) UIKit chưa có SwiftUI wrapper có thể được represent trong SwiftUI. “Rewrite toàn bộ” hiếm khi là yêu cầu (requirement / 요구사항) kỹ thuật mặc định.

---

# 25. Form, focus, gesture và animation

Điều khiển (control / 제어) thường dùng: `TextField`, `SecureField`, `Toggle`, `Picker`, `DatePicker`, `Slider`, `Stepper`.

```swift
enum Field: Hashable { case email, password }
@FocusState private var focusedField: Field?

TextField("Email", text: $email)
    .focused($focusedField, equals: .email)
```

Animation trạng thái (state / 상태) thay đổi (change / 변경):

```swift
withAnimation(.spring) {
    isExpanded.toggle()
}
```

Chuyển tiếp (transition / 전이):

```swift
if isVisible {
    DetailView()
        .transition(.opacity.combined(with: .move(edge: .bottom)))
}
```

Gesture có thể cạnh tranh với hệ thống (system / 시스템) gesture; cần kiểm thử (test / 테스트) trên OS/thiết bị (device / 장치) thật, đặc biệt với selection, scroll và khả năng tiếp cận (accessibility / 접근성) tương tác (interaction / 상호작용).

---

# 26. tài nguyên (resource / 자원), localization và khả năng tiếp cận (accessibility / 접근성)

Asset danh mục (catalog / 카탈로그) quản ảnh (image / 이미지)/color/tài nguyên (resource / 자원). SF Symbols:

```swift
Image(systemName: "heart.fill")
```

Localization không chỉ là thay văn bản (text / 텍스트). bố cục (layout / 레이아웃) phải chịu được string dài, pluralization, RTL, locale-specific date/number.

Khả năng tiếp cận (accessibility / 접근성) là chức năng:

```swift
.accessibilityLabel("Favorite")
.accessibilityHint("Marks this item as favorite")
```

Kiểm thử (test / 테스트) động (dynamic / 동적) kiểu (type / 타입), VoiceOver, contrast, tap mục tiêu (target / 대상) và Reduce Motion. UI đẹp ở default font kích thước (size / 크기) nhưng vỡ ở khả năng tiếp cận (accessibility / 접근성) kích thước (size / 크기) vẫn là bug.

---

# 27. Debugging, kiểm thử (test / 테스트) và bộ nhớ (memory / 메모리) tools

Breakpoint, exception breakpoint, LLDB:

```text
po object
p expression
bt
thread backtrace
```

Môi trường vận hành (production / 운영 환경) logging dùng `Logger`/OSLog thay vì `print` tràn lan; không log truy cập (access / 접근) đơn vị từ (token / 토큰)/password/PII.

Swift Testing:

```swift
import Testing

@Test
func totalPrice() {
    #expect(10 + 20 == 30)
}
```

XCTest vẫn phổ biến trong codebase hiện hữu.

Bộ nhớ (memory / 메모리) đồ thị (graph / 그래프) giúp xem retain đường dẫn (path / 경로)/cycle. Instruments sẽ được học sâu hơn ở Advanced.

---

# 28. Swift trình quản lý gói (package manager / 패키지 관리자) và mô-đun (module / 모듈) nhập môn

SwiftPM/SPM quản gói (package / 패키지)/phụ thuộc (dependency / 의존성). Manifest:

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

Swift 6.4 đưa Swift bản dựng (build / 빌드) thành hệ thống dựng (build system / 빌드 시스템) mặc định của SwiftPM. Beginner chỉ cần hiểu gói (package / 패키지) tạo mô-đun (module / 모듈)/phụ thuộc (dependency / 의존성) ranh giới (boundary / 경계) thật; Intermediate sẽ học modularization và API công khai (public API / 공개 API) surface.

---

# 29. Signing và chạy trên thiết bị (device / 장치)

Để chạy/phát hành app, executable phải được mã (code / 코드) signed. Phân biệt Apple nhà phát triển (developer / 개발자) Program membership, nhóm (team / 팀), Certificate, App ID, Provisioning Profile, Entitlement và năng lực (capability / 역량).

`Automatically manage signing` phù hợp cho học tập và nhiều dự án (project / 프로젝트) nhỏ. năng lực (capability / 역량) như Push Notifications, Associated Domains, App Groups hoặc Sign in with Apple có thể cần cả mục tiêu (target / 대상) entitlement lẫn portal/máy chủ (server / 서버) cấu hình (configuration / 구성).

---

# 30. Xcode 27 / Swift 6.4 notes cho Beginner

Swift 6.4 là bản phát hành (release / 릴리스) stable ngày 15/09/2026. Với iOS app, phần quan trọng không phải học mọi proposal mới mà là nhận biết ngôn ngữ (language / 언어)/tooling đang tiếp tục tăng bộ nhớ (memory / 메모리) an toàn (safety / 안전), quyền sở hữu (ownership / 소유권) expressiveness, observation và bản dựng (build / 빌드) portability.

Xcode 27 đi với Swift 6.4/iOS 27 SDK. SwiftUI `State` hiện thực (implementation / 구현) và builder internals tiếp tục tiến hóa; nguồn (source / 소스) app thông thường phần lớn không nên phụ thuộc hiện thực (implementation / 구현) detail của wrapper/builder.

`AsyncImage`/mạng (network / 네트워크) caching hành vi (behavior / 동작) và các API hệ thống (system / 시스템) có thể đổi theo SDK. Vì vậy khi tutorial cũ mâu thuẫn với bản phát hành (release / 릴리스) notes/Đặc tả API (API contract / API 계약), ưu tiên documentation của toolchain đang bản dựng (build / 빌드) dự án (project / 프로젝트).

---

# 31. Capstone Beginner — nối ngôn ngữ (language / 언어) → bộ nhớ (memory / 메모리) → UI → async → persistence

Hãy xây app “Reading danh sách (list / 목록)” có danh sách, chi tiết và form thêm/sửa. mô hình (model / 모델) thực thể (entity / 엔터티) bằng `struct`/`enum`; `NavigationStack` cho điều hướng (navigation / 내비게이션); cục bộ (local / 로컬) UI trạng thái (state / 상태) dùng `@State`; dùng chung (shared / 공유) observable mô hình (model / 모델) dùng Observation; REST bằng `URLSession`; decode Codable; bookmark bằng SwiftData; preference bằng UserDefaults; credential giả lập qua Keychain dịch vụ (service / 서비스).

Bắt buộc tự kiểm tra các thất bại (failure / 실패) đường dẫn (path / 경로): máy chủ (server / 서버) trả non-2xx, decode thất bại (fail / 실패), tác vụ (task / 작업) bị cancel, bản ghi (record / 레코드) không tồn tại, form invalid. Dùng bộ nhớ (memory / 메모리) đồ thị (graph / 그래프) để xác nhận một screen/mô hình (model / 모델) được giải phóng khi điều hướng (navigation / 내비게이션) pop nếu nó không còn đơn vị sở hữu (owner / 오너).

## Checklist trước khi sang Intermediate

Bạn cần giải thích được, không chỉ viết được cú pháp (syntax / 문법):

1. Vì sao `struct` và `class` có ngữ nghĩa (semantics / 의미론) khác nhau; bản sao (copy / 복사) một struct chứa lớp (class / 클래스) tham chiếu (reference / 참조) có ý nghĩa gì.
2. Optional khác default giá trị (value / 값) như thế nào; khi nào `guard let`, `??`, optional chaining phù hợp.
3. Closure escaping sống lâu hơn ngăn xếp lời gọi (call stack / 호출 스택) ra sao; capture danh sách (list / 목록) tham gia retain cycle thế nào.
4. ARC giải quyết đối tượng (object / 객체) thời gian tồn tại (lifetime / 수명) nhưng không giải quyết dữ liệu (data / 데이터) race như thế nào.
5. Vì sao `await` là suspension điểm (point / 지점) chứ không phải synonym của background luồng thực thi (thread / 스레드).
6. Ai sở hữu `@State`; `@Binding` khác quyền sở hữu (ownership / 소유권) ra sao; Observable mô hình (model / 모델) khác cục bộ (local / 로컬) trạng thái (state / 상태) thế nào.
7. UIKit controller có các vòng đời (lifecycle / 생명주기) callback nào và vì sao `viewDidLoad` không tương đương `viewWillAppear`.
8. triển khai (deployment / 배포) mục tiêu (target / 대상) khác SDK/trình biên dịch (compiler / 컴파일러) phiên bản (version / 버전) thế nào.
9. mạng (network / 네트워크)/persistence có thất bại (failure / 실패) là trạng thái bình thường chứ không phải exception hiếm.
10. Cách dùng Xcode breakpoint, kiểm thử (test / 테스트) và bộ nhớ (memory / 메모리) đồ thị (graph / 그래프) để xác minh giả định (assumption / 가정) thay vì đoán.

Nếu các câu trên còn mơ hồ, hãy quay lại section tương ứng trước khi học actor, `Sendable`, architecture và advanced state management ở Intermediate.
