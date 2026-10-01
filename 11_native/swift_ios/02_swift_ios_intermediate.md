# Swift & iOS Master ghi chú (note / 노트) — Intermediate

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Swift & iOS Master ghi chú (note / 노트) — Intermediate**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1.1 giá trị (value / 값) ngữ nghĩa (semantics / 의미론), tham chiếu (reference / 참조) ngữ nghĩa (semantics / 의미론) và sao chép khi ghi (copy-on-write / 쓰기 시 복사)** chỉ đường quay lại owner và tài liệu chuẩn khi cần đào sâu; sau đó sang **1.2 Equatable, Hashable, Comparable, Identifiable** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

> Mục tiêu: chuyển từ “biết viết màn hình và gọi API” sang “xây được tính năng (feature / 기능) có quyền sở hữu (ownership / 소유권) rõ, tính đồng thời (concurrency / 동시성) đúng, trạng thái (state / 상태) luồng (flow / 흐름) giải thích được, kiểm thử (test / 테스트) được và bảo trì được”.
>
> Prerequisite: đã hiểu Beginner, đặc biệt giá trị (value / 값)/tham chiếu (reference / 참조) ngữ nghĩa (semantics / 의미론), closure escaping/capture, ARC, `async`/`await`, `@State`/`@Binding`, UIKit vòng đời (lifecycle / 생명주기) cơ bản và mạng (network / 네트워크)/persistence thất bại (failure / 실패).

Intermediate không cố biến mọi tính năng (feature / 기능) thành kiến trúc (architecture / 아키텍처) nhiều tầng (layer / 계층). Trọng tâm là **lập luận (reasoning / 추론)**: ai sở hữu trạng thái (state / 상태), tác vụ (task / 작업) sống bao lâu, mutable dữ liệu (data / 데이터) được isolate ở đâu, side tác động (effect / 효과) bắt đầu/kết thúc khi nào, và ranh giới (boundary / 경계) nào cần lớp trừu tượng (abstraction / 추상화).

---

# 1. hệ kiểu (type system / 타입 시스템) ở mức dùng để thiết kế API

## 1.1 giá trị (value / 값) ngữ nghĩa (semantics / 의미론), tham chiếu (reference / 참조) ngữ nghĩa (semantics / 의미론) và sao chép khi ghi (copy-on-write / 쓰기 시 복사)

Đoạn code dưới đây là bằng chứng cho khái niệm vừa mở. Hãy đọc từ input và state đến output, ghi lại điều kiện áp dụng và giới hạn trước khi chuyển sang mục kế tiếp.

```swift
struct Profile {
    var name: String
}

var a = Profile(name: "A")
var b = a
b.name = "B"
```

`a` và `b` độc lập về ngữ nghĩa (semantics / 의미론). Collection chuẩn như `Array`, `Dictionary`, `String` có thể chia sẻ lưu trữ (storage / 저장소) và bản sao (copy / 복사) khi mutation, nhưng đó là tối ưu hóa (optimization / 최적화); công khai (public / 공개) mô hình tư duy (mental model / 사고 모델) vẫn là giá trị (value / 값) ngữ nghĩa (semantics / 의미론).

Tham chiếu (reference / 참조) kiểu (type / 타입) có định danh (identity / 식별자) và dùng chung (shared / 공유) mutable trạng thái (state / 상태). Khi nhiều đơn vị sở hữu (owner / 오너) cùng thấy một lớp (class / 클래스) instance, bạn phải trả lời cả hai câu hỏi: ai giữ thời gian tồn tại (lifetime / 수명) và ai được phép mutate.

> **Chuyển mạch:** Value/reference semantics và copy-on-write quyết định equality behavior; các protocol `Equatable`/`Hashable`/`Identifiable` tiếp theo đưa behavior đó vào collection và API design.

## 1.2 `Equatable`, `Hashable`, `Comparable`, `Identifiable`

Đoạn code dưới đây là bằng chứng cho khái niệm vừa mở. Hãy đọc từ input và state đến output, ghi lại điều kiện áp dụng và giới hạn trước khi chuyển sang mục kế tiếp.

```swift
struct Product: Identifiable, Hashable {
    let id: UUID
    let name: String
}
```

`Identifiable.id` phải đại diện stable định danh (identity / 식별자) của thực thể (entity / 엔터티) trong khoảng thời gian tồn tại (lifetime / 수명) phù hợp. Nếu ID thay đổi theo vị trí array, diffing/điều hướng (navigation / 내비게이션)/trạng thái (state / 상태) restoration có thể gắn trạng thái (state / 상태) vào sai item.

> **Chuyển mạch:** Protocol conformances tạo capability có thể dùng trong collections; generic/`where` tiếp theo biểu diễn constraint, còn associated type/`some`/`any` chọn mức abstraction phù hợp.

## 1.3 Generic, `where` và capability-oriented API

Mục này dùng implementation để kiểm tra API contract: input nào được chấp nhận, behavior nào được bảo đảm và boundary nào người gọi vẫn phải chịu trách nhiệm.

```swift
func merge<C1: Collection, C2: Collection>(
    _ lhs: C1,
    _ rhs: C2
) -> [C1.Element]
where C1.Element == C2.Element {
    Array(lhs) + rhs
}
```

Chỉ yêu cầu năng lực (capability / 역량) thực sự cần. Nếu hàm (function / 함수) chỉ iterate một lần, `Sequence` có thể phù hợp hơn `Array`; nếu cần random truy cập (access / 접근), ràng buộc (constraint / 제약조건) mạnh hơn mới có ý nghĩa.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Swift & iOS Master ghi chú (note / 노트) — Intermediate**, **1.4 Associated kiểu (type / 타입), some và any** tiếp nhận điểm tựa từ **1.3 Generic, where và capability-oriented API** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5.1 Structured tính đồng thời (concurrency / 동시성) với async let** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 1.4 Associated kiểu (type / 타입), `some` và `any`

Mục này dùng implementation để kiểm tra API contract: input nào được chấp nhận, behavior nào được bảo đảm và boundary nào người gọi vẫn phải chịu trách nhiệm.

```swift
protocol Repository {
    associatedtype Entity
    func fetchAll() async throws -> [Entity]
}
```

`some P` là opaque kiểu (type / 타입): API che concrete kiểu (type / 타입) nhưng vẫn giữ một concrete kiểu (type / 타입) ổn định cho trình biên dịch (compiler / 컴파일러). `any P` là existential giá trị (value / 값) có thể chứa các concrete conformer khác nhau ở thời gian chạy (runtime / 런타임).

```swift
func makeView() -> some View {
    Text("Hello")
}

let analytics: any AnalyticsService
```

Đừng dùng existential chỉ vì cú pháp (syntax / 문법) ngắn. Generic/opaque kiểu (type / 타입) giữ nhiều static kiểu (type / 타입) thông tin (information / 정보) hơn; existential phù hợp khi thời gian chạy (runtime / 런타임) heterogeneity/substitution là yêu cầu (requirement / 요구사항) thật.

---

# 2. Optional, kết quả (result / 결과) và lỗi (error / 오류) ranh giới (boundary / 경계)

Optional mô hình hóa “có hoặc không có giá trị (value / 값)”. `Result<Success, Failure>` mô hình hóa success/thất bại (failure / 실패) thành giá trị (value / 값). `async throws` thường tự nhiên hơn `Result` cho async lời gọi (call / 호출) chuỗi (chain / 사슬), nhưng kết quả (result / 결과) hữu ích khi cần lưu kết quả, cầu nối (bridge / 브리지) callback hoặc đưa kết quả (result / 결과) qua máy trạng thái (state machine / 상태 머신).

```swift
let result: Result<User, APIError>
```

Đừng flatten mọi lỗi (error / 오류) thành `Error` quá sớm nếu UI/lĩnh vực (domain / 도메인) cần phân biệt unauthorized, kiểm tra hợp lệ (validation / 검증), offline hay máy chủ (server / 서버) thất bại (failure / 실패). Ngược lại, đừng tạo hàng chục enum lỗi (error / 오류) chỉ để “type-safe” nếu caller không có hành vi (behavior / 동작) khác nhau.

---

# 3. giao thức (protocol / 프로토콜) extension và dispatch trap

Mục này dùng implementation để kiểm tra API contract: input nào được chấp nhận, behavior nào được bảo đảm và boundary nào người gọi vẫn phải chịu trách nhiệm.

```swift
protocol Named {
    func name() -> String
}

extension Named {
    func name() -> String { "default" }
}
```

Nếu phương thức (method / 메서드) là giao thức (protocol / 프로토콜) yêu cầu (requirement / 요구사항), conforming kiểu (type / 타입) override được qua giao thức (protocol / 프로토콜) witness. Nếu phương thức (method / 메서드) chỉ tồn tại ở extension nhưng không nằm trong yêu cầu (requirement / 요구사항), dispatch qua existential có thể khác kỳ vọng. Khi polymorphism là intent, đưa thao tác (operation / 연산) vào giao thức (protocol / 프로토콜) đặc tả hợp đồng (contract / 계약).

Conditional conformance cho phép kiểu (type / 타입) generic conform khi Element thỏa điều kiện; đây là nền tảng của nhiều API thư viện chuẩn (standard library / 표준 라이브러리).

---

# 4. thuộc tính (property / 속성) wrapper, kết quả (result / 결과) builder và macro

Thuộc tính (property / 속성) wrapper đóng gói lưu trữ (storage / 저장소)/truy cập (access / 접근) hành vi (behavior / 동작):

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

Kết quả (result / 결과) builder đứng sau nhiều DSL declarative. Macro là compile-time transformation; `@Observable` và `@Model` là ví dụ quan trọng. Khi diagnostic “magic”, xem macro expansion/generated giao diện (interface / 인터페이스) trong Xcode thay vì đoán.

---

# 5. Swift tính đồng thời (concurrency / 동시성) — mô hình tư duy (mental model / 사고 모델) trước API

Swift tính đồng thời (concurrency / 동시성) có bốn trục cần tách:

- **tác vụ (task / 작업) thời gian tồn tại (lifetime / 수명)**: công việc nào là parent/child, ai cancel ai;
- **suspension**: `await` cho phép tác vụ (task / 작업) tạm dừng nhưng không đồng nghĩa đổi luồng thực thi (thread / 스레드);
- **isolation**: mutable trạng thái (state / 상태) thuộc actor/toàn cục (global / 전역) actor nào;
- **sendability**: giá trị (value / 값) nào được phép đi qua isolation ranh giới (boundary / 경계).

Nếu bốn trục này rõ, phần lớn trình biên dịch (compiler / 컴파일러) diagnostic Swift 6 trở nên có lý do thay vì “annotation ceremony”.

> **Chuyển mạch:** `some`/`any` chọn abstraction boundary; `async let` tiếp theo chạy child tasks có cấu trúc, còn TaskGroup phục vụ số lượng task động.

## 5.1 Structured tính đồng thời (concurrency / 동시성) với `async let`

Mục này dùng code để làm rõ lifetime và cancellation của công việc bất đồng bộ. Hãy xác định ai sở hữu task, nó chạy ở context nào, khi nào hoàn tất hoặc bị hủy, rồi mới đánh giá cú pháp.

```swift
async let profile = api.profile()
async let messages = api.messages()

let (p, m) = try await (profile, messages)
```

Child tác vụ (task / 작업) gắn thời gian tồn tại (lifetime / 수명) với lexical phạm vi (scope / 범위). phạm vi (scope / 범위) không kết thúc hợp lệ khi child tác vụ (task / 작업) còn bị bỏ quên; lỗi (error / 오류)/cancellation có quan hệ rõ hơn unstructured tác vụ (task / 작업).

> **Chuyển mạch:** Ở chặng này của **Swift & iOS Master ghi chú (note / 노트) — Intermediate**, **5.2 động (dynamic / 동적) child tác vụ (task / 작업) với TaskGroup** tiếp nhận điểm tựa từ **5.1 Structured tính đồng thời (concurrency / 동시성) với async let** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5.3 Task {} là unstructured tác vụ (task / 작업), không phải child phạm vi (scope / 범위) tự động** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5.2 động (dynamic / 동적) child tác vụ (task / 작업) với TaskGroup

Mục này dùng code để làm rõ lifetime và cancellation của công việc bất đồng bộ. Hãy xác định ai sở hữu task, nó chạy ở context nào, khi nào hoàn tất hoặc bị hủy, rồi mới đánh giá cú pháp.

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

Tác vụ (task / 작업) group phù hợp fan-out động. Đừng tạo vô hạn tác vụ (task / 작업) chỉ vì API cho phép; tính đồng thời (concurrency / 동시성) cần bounded theo tài nguyên (resource / 자원)/backend các ràng buộc (constraints / 제약조건들) khi đầu vào (input / 입력) lớn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Swift & iOS Master ghi chú (note / 노트) — Intermediate**, **5.3 Task {} là unstructured tác vụ (task / 작업), không phải child phạm vi (scope / 범위) tự động** tiếp nhận điểm tựa từ **5.2 động (dynamic / 동적) child tác vụ (task / 작업) với TaskGroup** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5.4 Task.detached là escape hatch** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5.3 `Task {}` là unstructured tác vụ (task / 작업), không phải child phạm vi (scope / 범위) tự động

Mục này dùng code để làm rõ lifetime và cancellation của công việc bất đồng bộ. Hãy xác định ai sở hữu task, nó chạy ở context nào, khi nào hoàn tất hoặc bị hủy, rồi mới đánh giá cú pháp.

```swift
let task = Task {
    await model.refresh()
}
```

`Task {}` hữu ích để cầu nối (bridge / 브리지) synchronous ngữ cảnh (context / 맥락) vào async hoặc tạo tác vụ (task / 작업) có đơn vị sở hữu (owner / 오너) rõ. Nhưng tác vụ (task / 작업) này không được lexical phạm vi (scope / 범위) chờ/cancel giống child tác vụ (task / 작업) của `async let`/group. Nếu lưu tác vụ (task / 작업) trong mô hình (model / 모델), mô hình (model / 모델) phải có chính sách (policy / 정책) cancel/supersede.

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

> **Chuyển mạch:** Trong **Swift & iOS Master ghi chú (note / 노트) — Intermediate**, **5.4 Task.detached là escape hatch** tiếp nhận điểm tựa từ **5.3 Task {} là unstructured tác vụ (task / 작업), không phải child phạm vi (scope / 범위) tự động** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5.5 Cancellation là cooperative** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5.4 `Task.detached` là escape hatch

Detached tác vụ (task / 작업) không nên là “background luồng thực thi (thread / 스레드) button”. Nó tách khỏi nhiều ngữ cảnh (context / 맥락) mà `Task {}` kế thừa. Dùng khi thật sự cần independent unstructured công việc (work / 작업) và bạn hiểu priority/task-local/isolation implications. Với app tính năng (feature / 기능) bình thường, structured tác vụ (task / 작업) hoặc `Task {}` có đơn vị sở hữu (owner / 오너) rõ thường tốt hơn.

> **Chuyển mạch:** Ở chặng này của **Swift & iOS Master ghi chú (note / 노트) — Intermediate**, **5.5 Cancellation là cooperative** tiếp nhận điểm tựa từ **5.4 Task.detached là escape hatch** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5.6 Priority không phải QoS guarantee tuyệt đối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5.5 Cancellation là cooperative

`cancel()` không giết mã (code / 코드) tùy ý. Nó đặt cancellation trạng thái (state / 상태); API suspension điểm (point / 지점) hoặc mã (code / 코드) của bạn cần kiểm:

```swift
try Task.checkCancellation()
```

Cancellation thường không phải “lỗi (error / 오류) UX”. Khi người dùng (user / 사용자) đổi tìm kiếm (search / 검색) truy vấn (query / 쿼리) hay rời màn hình, tác vụ (task / 작업) cũ bị cancel là điều khiển (control / 제어) luồng (flow / 흐름) hợp lệ; đừng hiện alert “CancellationError” như máy chủ (server / 서버) thất bại (failure / 실패).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Swift & iOS Master ghi chú (note / 노트) — Intermediate**, **5.6 Priority không phải QoS guarantee tuyệt đối** tiếp nhận điểm tựa từ **5.5 Cancellation là cooperative** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6.1 Actor không phải khóa (lock / 잠금) cú pháp (syntax / 문법) mới** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5.6 Priority không phải QoS guarantee tuyệt đối

Tác vụ (task / 작업) priority là scheduling hint và có inheritance/escalation ngữ nghĩa (semantics / 의미론). Không thiết kế tính đúng đắn (correctness / 정확성) dựa trên giả định (assumption / 가정) “high priority chắc chắn chạy trước low priority”. tính đúng đắn (correctness / 정확성) phải độc lập scheduler timing.

---

# 6. Actor isolation — mutable trạng thái (state / 상태) thuộc về đâu

Actor serialize truy cập (access / 접근) tới actor-isolated mutable trạng thái (state / 상태) theo tính đồng thời (concurrency / 동시성) mô hình (model / 모델).

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

Gọi actor member từ lĩnh vực (domain / 도메인) khác thường cần `await` vì lời gọi (call / 호출) có thể suspend để executor chạy actor job.

> **Chuyển mạch:** Trong **Swift & iOS Master ghi chú (note / 노트) — Intermediate**, **6.1 Actor không phải khóa (lock / 잠금) cú pháp (syntax / 문법) mới** tiếp nhận điểm tựa từ **5.6 Priority không phải QoS guarantee tuyệt đối** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6.2 @MainActor** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6.1 Actor không phải khóa (lock / 잠금) cú pháp (syntax / 문법) mới

Actor bảo vệ isolation, nhưng phương thức (method / 메서드) actor có thể suspend. Khi gặp `await`, actor có thể xử lý công việc khác trước khi phương thức (method / 메서드) tiếp tục. Vì vậy bất biến (invariant / 불변식) đọc trước `await` có thể không còn đúng sau `await`.

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

Đây là **actor reentrancy**, không phải dữ liệu (data / 데이터) race. trình biên dịch (compiler / 컴파일러) ngăn unsynchronized truy cập (access / 접근) nhưng không tự chứng minh nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식) qua suspension điểm (point / 지점).

> **Chuyển mạch:** Ở chặng này của **Swift & iOS Master ghi chú (note / 노트) — Intermediate**, **6.2 @MainActor** tiếp nhận điểm tựa từ **6.1 Actor không phải khóa (lock / 잠금) cú pháp (syntax / 문법) mới** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6.3 nonisolated** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6.2 `@MainActor`

UI-facing observable trạng thái (state / 상태) thường thuộc MainActor:

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

`@MainActor` là isolation đặc tả hợp đồng (contract / 계약), không chỉ là synonym của `DispatchQueue.main.async`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Swift & iOS Master ghi chú (note / 노트) — Intermediate**, **6.3 nonisolated** tiếp nhận điểm tựa từ **6.2 @MainActor** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6.4 toàn cục (global / 전역) actor** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6.3 `nonisolated`

Member không cần actor-isolated trạng thái (state / 상태) có thể được thiết kế `nonisolated` khi ngữ nghĩa (semantics / 의미론) cho phép. Không thêm `nonisolated` chỉ để trình biên dịch (compiler / 컴파일러) ngừng báo; hãy đảm bảo hiện thực (implementation / 구현) không lén đọc mutable actor trạng thái (state / 상태).

> **Chuyển mạch:** Trong **Swift & iOS Master ghi chú (note / 노트) — Intermediate**, **6.4 toàn cục (global / 전역) actor** tiếp nhận điểm tựa từ **6.3 nonisolated** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7.1 @Sendable closure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6.4 toàn cục (global / 전역) actor

`@MainActor` là toàn cục (global / 전역) actor có sẵn. Custom toàn cục (global / 전역) actor có thể hợp lý cho một lĩnh vực (domain / 도메인) isolation đặc biệt, nhưng đừng tạo một actor toàn app để “hết race”; isolation ranh giới (boundary / 경계) phải phản ánh quyền sở hữu (ownership / 소유권) thật.

---

# 7. `Sendable` và crossing isolation ranh giới (boundary / 경계)

`Sendable` biểu diễn giá trị (value / 값) có thể transfer giữa tính đồng thời (concurrency / 동시성) domains an toàn theo mô hình (model / 모델) của trình biên dịch (compiler / 컴파일러).

```swift
struct UserSnapshot: Sendable {
    let id: UUID
    let name: String
}
```

Immutable giá trị (value / 값) kiểu (type / 타입) gồm trường dữ liệu (field / 필드) Sendable thường tự nhiên. Mutable lớp (class / 클래스) dùng chung (shared / 공유) tham chiếu (reference / 참조) khó hơn vì hai isolation lĩnh vực (domain / 도메인) có thể mutate cùng đối tượng (object / 객체).

`@unchecked Sendable` là lời hứa của programmer rằng synchronization/bất biến (invariant / 불변식) bên trong đã đúng. Nó không “làm đối tượng (object / 객체) thread-safe”; nó tắt một phần kiểm tra trình biên dịch (compiler / 컴파일러). Mỗi `@unchecked Sendable` nên có lý do/bất biến (invariant / 불변식) được rà soát (review / 검토).

> **Chuyển mạch:** Ở chặng này của **Swift & iOS Master ghi chú (note / 노트) — Intermediate**, **7.1 @Sendable closure** tiếp nhận điểm tựa từ **6.4 toàn cục (global / 전역) actor** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7.2 Snapshot mẫu (pattern / 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7.1 `@Sendable` closure

Closure được chạy ở tính đồng thời (concurrency / 동시성) ngữ cảnh (context / 맥락) khác có thể cần `@Sendable`. trình biên dịch (compiler / 컴파일러) kiểm capture để tránh closure mang mutable non-Sendable trạng thái (state / 상태) qua ranh giới (boundary / 경계).

```swift
func perform(_ operation: @Sendable @escaping () async -> Void) {
    Task { await operation() }
}
```

Nếu trình biên dịch (compiler / 컴파일러) phàn nàn capture, đừng mặc định thêm `@unchecked`. Hãy hỏi capture có thể chuyển thành immutable snapshot/giá trị (value / 값) hay phụ thuộc (dependency / 의존성) actor-isolated không.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Swift & iOS Master ghi chú (note / 노트) — Intermediate**, **7.2 Snapshot mẫu (pattern / 패턴)** tiếp nhận điểm tựa từ **7.1 @Sendable closure** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Checklist trước khi sang Advanced/cấp cao (senior / 시니어)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7.2 Snapshot mẫu (pattern / 패턴)

Thay vì gửi mutable tham chiếu (reference / 참조) qua actor ranh giới (boundary / 경계), tạo Sendable snapshot:

```swift
struct ProfileSnapshot: Sendable {
    let id: UUID
    let displayName: String
}
```

Mẫu (pattern / 패턴) này làm luồng dữ liệu (data flow / 데이터 흐름) dễ lập luận (reasoning / 추론) và tách persistence/UI đối tượng (object / 객체) thời gian tồn tại (lifetime / 수명) khỏi async worker.

---

# 8. Swift 6.x approachable tính đồng thời (concurrency / 동시성) và dự án (project / 프로젝트) settings

Swift 6.x tăng compile-time data-race checking. Từ Swift 6.2, ngôn ngữ (language / 언어)/tooling tiếp tục làm tính đồng thời (concurrency / 동시성) approachable hơn với default actor isolation option và tường minh (explicit / 명시적) opt-in tính đồng thời (concurrency / 동시성) ở nơi phù hợp. Điều quan trọng là **ngôn ngữ (language / 언어) chế độ (mode / 모드) và bản dựng (build / 빌드) setting là một phần ngữ nghĩa (semantics / 의미론) dự án (project / 프로젝트)**.

Khi migrate mã (code / 코드) cũ, ghi lại ít nhất: Xcode phiên bản (version / 버전), Swift trình biên dịch (compiler / 컴파일러) phiên bản (version / 버전), Swift ngôn ngữ (language / 언어) chế độ (mode / 모드), triển khai (deployment / 배포) mục tiêu (target / 대상), default actor isolation setting và các upcoming/strict tính đồng thời (concurrency / 동시성) tính năng (feature / 기능) đang bật. Cùng nguồn (source / 소스) có thể cho diagnostic khác khi những setting này khác nhau.

Không “fix di chuyển (migration / 마이그레이션)” bằng cách rải `@MainActor`/`nonisolated`/`@unchecked Sendable` theo trình biên dịch (compiler / 컴파일러) lỗi (error / 오류). Phân loại quyền sở hữu (ownership / 소유권) trước rồi annotate ranh giới (boundary / 경계) tương ứng.

---

# 9. AsyncSequence, AsyncStream và sự kiện (event / 이벤트) stream

`AsyncSequence` mô hình hóa nhiều giá trị (value / 값) đến theo thời gian:

```swift
for await event in events {
    guard !Task.isCancelled else { break }
    handle(event)
}
```

`AsyncStream`/`AsyncThrowingStream` hữu ích cầu nối (bridge / 브리지) delegate/callback API. Khi cầu nối (bridge / 브리지), phải có chính sách (policy / 정책) buffering, termination và cleanup producer khi bên tiêu thụ (consumer / 소비자) cancel; nếu không producer có thể chạy mãi.

Swift 6.4 tiếp tục tăng tích hợp (integration / 통합) giữa Observation và async thay đổi (change / 변경) streams. Dù API mới thuận tiện hơn, sự kiện (event / 이벤트) stream và UI observation vẫn là hai lớp trừu tượng (abstraction / 추상화) khác nhau: UI phụ thuộc (dependency / 의존성) tracking không tự nhiên trở thành lĩnh vực (domain / 도메인) sự kiện (event / 이벤트) log.

---

# 10. Continuation — cầu nối (bridge / 브리지) legacy callback có kỷ luật

Đoạn code dưới đây là bằng chứng cho khái niệm vừa mở. Hãy đọc từ input và state đến output, ghi lại điều kiện áp dụng và giới hạn trước khi chuyển sang mục kế tiếp.

```swift
func load() async throws -> Data {
    try await withCheckedThrowingContinuation { continuation in
        legacyLoad { result in
            continuation.resume(with: result)
        }
    }
}
```

Continuation phải được resume đúng ngữ nghĩa (semantics / 의미론) một lần. Missing resume làm tác vụ (task / 작업) treo; double resume là bug. Checked continuation giúp phát hiện nhiều lỗi nhưng không thay quyền sở hữu (ownership / 소유권)/cancellation thiết kế (design / 설계).

Nếu legacy thao tác (operation / 연산) có cancel đơn vị từ (token / 토큰), cầu nối (bridge / 브리지) nên propagate cancellation khi có thể thay vì chỉ đổi callback thành `await` về mặt cú pháp (syntax / 문법).

---

# 11. SwiftUI trạng thái (state / 상태) — nguồn chuẩn (source of truth / 정본) trước thuộc tính (property / 속성) wrapper

SwiftUI trạng thái (state / 상태) bug thường không phải thiếu wrapper, mà do cùng một fact có nhiều đơn vị sở hữu (owner / 오너) hoặc view định danh (identity / 식별자) không như người viết tưởng.

Hãy phân loại:

- cục bộ (local / 로컬) presentation trạng thái (state / 상태): sheet mở, tab chọn, văn bản (text / 텍스트) đang edit;
- tính năng (feature / 기능) trạng thái (state / 상태): loading/kết quả (result / 결과)/filter/điều hướng (navigation / 내비게이션) của tính năng (feature / 기능);
- lĩnh vực (domain / 도메인) trạng thái (state / 상태): nghiệp vụ (business / 비즈니스) truth;
- persisted/máy chủ (server / 서버) trạng thái (state / 상태): nguồn dữ liệu durable/remote;
- derived trạng thái (state / 상태): tính từ nguồn (source / 소스) khác.

Đừng lưu lại derived trạng thái (state / 상태) nếu có thể tính rẻ và deterministic.

---

# 12. `@State` — lưu trữ (storage / 저장소) gắn với view định danh (identity / 식별자)

Mục này đặt đoạn code vào câu hỏi state thuộc owner nào và sống qua boundary nào. Hãy theo dõi identity, cập nhật và khôi phục để phân biệt state tạm với dữ liệu cần persistence.

```swift
struct SearchView: View {
    @State private var query = ""
    @State private var model = SearchModel()

    var body: some View { ... }
}
```

`View` struct được tạo lại nhiều lần; `@State` lưu trữ (storage / 저장소) được SwiftUI giữ theo view định danh (identity / 식별자). Vì vậy không lập luận (reasoning / 추론) “struct bị init lại thì trạng thái (state / 상태) chắc reset”. trạng thái (state / 상태) reset khi định danh (identity / 식별자)/thời gian tồn tại (lifetime / 수명) của view thay đổi theo cây (tree / 트리) ngữ nghĩa (semantics / 의미론).

Với Xcode 27, `State` hiện thực (implementation / 구현) tiếp tục được hiện đại hóa; đừng dựa vào undocumented detail như “initializer expression chắc chạy mỗi body recomputation”. Hãy dựa vào công khai (public / 공개) quyền sở hữu (ownership / 소유권)/thời gian tồn tại (lifetime / 수명) ngữ nghĩa (semantics / 의미론).

---

# 13. `@Binding` — năng lực (capability / 역량) mutate trạng thái (state / 상태) của đơn vị sở hữu (owner / 오너) khác

Mục này đặt đoạn code vào câu hỏi state thuộc owner nào và sống qua boundary nào. Hãy theo dõi identity, cập nhật và khôi phục để phân biệt state tạm với dữ liệu cần persistence.

```swift
struct NameField: View {
    @Binding var name: String

    var body: some View {
        TextField("Name", text: $name)
    }
}
```

Binding không bản sao (copy / 복사) trạng thái (state / 상태) và cũng không trở thành đơn vị sở hữu (owner / 오너). Nó là getter/setter projection. Khi binding chuỗi (chain / 사슬) quá sâu, đó có thể là dấu hiệu tính năng (feature / 기능) ranh giới (boundary / 경계)/quyền sở hữu trạng thái (state ownership / 상태 소유권) cần xem lại.

---

# 14. Observation với `@Observable`

Mục này đặt đoạn code vào câu hỏi state thuộc owner nào và sống qua boundary nào. Hãy theo dõi identity, cập nhật và khôi phục để phân biệt state tạm với dữ liệu cần persistence.

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

Observation nhánh học (track / 트랙) thuộc tính (property / 속성) phụ thuộc (dependency / 의존성) mà view đọc. Điều này giúp vô hiệu hóa (invalidation / 무효화) granular hơn broad notification mô hình (model / 모델) cũ trong nhiều trường hợp.

Observable tham chiếu (reference / 참조) vẫn là lớp (class / 클래스): quyền sở hữu (ownership / 소유권)/thời gian tồn tại (lifetime / 수명) và dùng chung (shared / 공유) mutation vẫn cần thiết kế. `@Observable` không biến lớp (class / 클래스) thành giá trị (value / 값) kiểu (type / 타입) và không tự làm nó concurrency-safe.

---

# 15. `@Bindable` — tạo Binding vào Observable mô hình (model / 모델)

Khi child cần binding trực tiếp tới thuộc tính (property / 속성) của observable mô hình (model / 모델), `@Bindable` tạo projected binding surface:

```swift
struct ProfileEditor: View {
    @Bindable var model: ProfileModel

    var body: some View {
        TextField("Name", text: $model.name)
    }
}
```

`@Bindable` không sở hữu mô hình (model / 모델). đơn vị sở hữu (owner / 오너) vẫn phải được quyết định ở parent/composition gốc (root / 루트).

---

# 16. môi trường (environment / 환경) và phụ thuộc (dependency / 의존성) phạm vi (scope / 범위)

Đoạn code dưới đây là bằng chứng cho khái niệm vừa mở. Hãy đọc từ input và state đến output, ghi lại điều kiện áp dụng và giới hạn trước khi chuyển sang mục kế tiếp.

```swift
@Environment(CartModel.self) private var cart
```

Môi trường (environment / 환경) phù hợp phụ thuộc (dependency / 의존성)/ngữ cảnh (context / 맥락) scoped theo view subtree. Nhưng nếu một lĩnh vực (domain / 도메인) đối tượng (object / 객체) không thể hoạt động thiếu API máy khách (client / 클라이언트), constructor injection thường thể hiện bất biến (invariant / 불변식) tốt hơn giấu phụ thuộc (dependency / 의존성) trong môi trường (environment / 환경) toàn cục (global / 전역).

Một mẫu (pattern / 패턴) tốt: App/composition gốc (root / 루트) dựng concrete phụ thuộc (dependency / 의존성); tính năng (feature / 기능) gốc (root / 루트) nhận phụ thuộc (dependency / 의존성); môi trường (environment / 환경) chỉ dùng cho những thứ thực sự hợp với cây (tree / 트리) phạm vi (scope / 범위).

---

# 17. Legacy SwiftUI wrapper ánh xạ (mapping / 매핑)

Codebase cũ có thể dùng:

- `ObservableObject` + `@Published`;
- `@StateObject` để view sở hữu tham chiếu (reference / 참조) đối tượng (object / 객체);
- `@ObservedObject` khi đối tượng (object / 객체) do nơi khác sở hữu;
- `@EnvironmentObject` cho dùng chung (shared / 공유) đối tượng (object / 객체) qua cây (tree / 트리).

Đừng migrate chỉ bằng search-replace. Chuyển sang Observation cần giữ nguyên quyền sở hữu (ownership / 소유권)/thời gian tồn tại (lifetime / 수명). mô hình tư duy (mental model / 사고 모델) cũ “StateObject owns / ObservedObject borrows” vẫn hữu ích để đọc legacy, nhưng API mới biểu diễn bằng `@State` + observable tham chiếu (reference / 참조) và các projection phù hợp.

---

# 18. Derived trạng thái (state / 상태) và máy trạng thái (state machine / 상태 머신)

Bad trạng thái (state / 상태):

```swift
var isLoading = false
var hasError = false
var isEmpty = false
```

Có nhiều combination vô nghĩa. Enum máy trạng thái (state machine / 상태 머신) làm bất biến (invariant / 불변식) tường minh (explicit / 명시적):

```swift
enum ScreenState {
    case idle
    case loading
    case loaded([Item])
    case empty
    case failed(APIError)
}
```

Nếu `canCheckout` luôn tính từ cart/address, hãy để computed thuộc tính (property / 속성) thay vì lưu thêm Boolean phải sync thủ công.

---

# 19. View định danh (identity / 식별자), conditional cây (tree / 트리) và `.id`

Trạng thái (state / 상태) thời gian tồn tại (lifetime / 수명) phụ thuộc định danh (identity / 식별자). Hai branch conditional có thể tạo định danh (identity / 식별자)/thời gian tồn tại (lifetime / 수명) khác:

```swift
if isLoggedIn {
    HomeView()
} else {
    LoginView()
}
```

`.id(...)` thay định danh (identity / 식별자) chủ động và có thể reset trạng thái (state / 상태)/tác vụ (task / 작업). Đừng dùng `.id(UUID())` như “force refresh”; nó thường che data-flow bug và phá trạng thái (state / 상태) continuity.

Danh sách (list / 목록)/ForEach định danh (identity / 식별자) cũng phải là domain-stable ID, không phải chỉ mục (index / 인덱스) nếu dữ liệu (data / 데이터) reorder/insert/delete.

---

# 20. `.task` và tác vụ (task / 작업) thời gian tồn tại (lifetime / 수명) theo view

Mục này dùng code để làm rõ lifetime và cancellation của công việc bất đồng bộ. Hãy xác định ai sở hữu task, nó chạy ở context nào, khi nào hoàn tất hoặc bị hủy, rồi mới đánh giá cú pháp.

```swift
.task {
    await model.load()
}

.task(id: query) {
    await model.search(query)
}
```

Tác vụ (task / 작업) modifier gắn công việc (work / 작업) vào view thời gian tồn tại (lifetime / 수명)/định danh (identity / 식별자) và có cancellation ngữ nghĩa (semantics / 의미론) khi view/tác vụ (task / 작업) định danh (identity / 식별자) đổi. Đây là idiom tốt cho screen-scoped tải (load / 로드)/tìm kiếm (search / 검색).

Nhưng nghiệp vụ (business / 비즈니스) thao tác (operation / 연산) cần sống lâu hơn screen không nên vô tình bị sở hữu bởi view. Ví dụ upload phải tiếp tục khi người dùng (user / 사용자) rời màn hình có thể cần dịch vụ (service / 서비스)/background URLSession đơn vị sở hữu (owner / 오너) khác.

---

# 21. SwiftUI bố cục (layout / 레이아웃) sâu hơn

SwiftUI bố cục (layout / 레이아웃) là negotiation parent → child → placement. `frame` tham gia proposal/ràng buộc (constraint / 제약조건) chứ không đơn giản mutate frame như UIKit.

Bộ chứa (container / 컨테이너) quan trọng: `ScrollView`, `LazyVStack`, `LazyHStack`, `LazyVGrid`, `Grid`, `List`, `Form`.

`GeometryReader` không phải default solution. Ưu tiên bố cục (layout / 레이아웃) giao thức (protocol / 프로토콜), alignment, container-relative sizing và built-in adaptive bộ chứa (container / 컨테이너) khi phù hợp.

Custom `Layout` hữu ích khi parent cần đo/place nhiều child theo thuật toán riêng.

---

# 22. điều hướng (navigation / 내비게이션) là trạng thái (state / 상태)

Mục này đặt đoạn code vào câu hỏi state thuộc owner nào và sống qua boundary nào. Hãy theo dõi identity, cập nhật và khôi phục để phân biệt state tạm với dữ liệu cần persistence.

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

Route-as-data giúp deep link, restoration và kiểm thử (test / 테스트). Router không nên trở thành nơi chứa lô-gic nghiệp vụ (business logic / 비즈니스 로직).

---

# 23. Networking tầng (layer / 계층) có cấu trúc

View không nên tự bản dựng (build / 빌드) URL, auth header, status ánh xạ (mapping / 매핑) và decode lặp lại.

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

Máy khách (client / 클라이언트) môi trường vận hành (production / 운영 환경) phân tách yêu cầu (request / 요청) construction, vận chuyển (transport / 전송), HTTP kiểm tra hợp lệ (validation / 검증), decoding, auth, thử lại (retry / 재시도)/cancellation, bộ nhớ đệm (cache / 캐시) và logging.

```swift
var request = URLRequest(url: url)
request.httpMethod = "POST"
request.timeoutInterval = 30
request.setValue("application/json", forHTTPHeaderField: "Content-Type")
request.httpBody = try JSONEncoder().encode(body)
```

`URLSessionConfiguration` quyết định bộ nhớ đệm (cache / 캐시), cookie, hết thời gian chờ (timeout / 타임아웃), connectivity hành vi (behavior / 동작) và nhiều chính sách (policy / 정책) khác.

---

# 24. thử lại (retry / 재시도), idempotency và authentication coordination

Không thử lại (retry / 재시도) mù quáng mọi thất bại (failure / 실패). mạng (network / 네트워크) offline, hết thời gian chờ (timeout / 타임아웃), HTTP 429, HTTP 500 và kiểm tra hợp lệ (validation / 검증) 400 có chính sách (policy / 정책) khác nhau.

GET thường idempotent; POST tạo tài nguyên (resource / 자원) có thể duplicate nếu thử lại (retry / 재시도) sau hết thời gian chờ (timeout / 타임아웃) khi máy chủ (server / 서버) đã xử lý yêu cầu (request / 요청) đầu. Với mutation quan trọng, backend/máy khách (client / 클라이언트) nên có idempotency chiến lược (strategy / 전략) nếu hệ thống hỗ trợ.

Đơn vị từ (token / 토큰) refresh phải tránh refresh storm. Nếu 10 yêu cầu (request / 요청) cùng nhận 401, thường chỉ nên có một refresh in-flight và các yêu cầu (request / 요청) khác chờ kết quả thay vì 10 refresh độc lập.

---

# 25. Codable và tolerant ranh giới (boundary / 경계)

Đoạn code dưới đây là bằng chứng cho khái niệm vừa mở. Hãy đọc từ input và state đến output, ghi lại điều kiện áp dụng và giới hạn trước khi chuyển sang mục kế tiếp.

```swift
let decoder = JSONDecoder()
decoder.keyDecodingStrategy = .convertFromSnakeCase
decoder.dateDecodingStrategy = .iso8601
```

Tách vận chuyển (transport / 전송) DTO khỏi lĩnh vực (domain / 도메인) mô hình (model / 모델) khi máy chủ (server / 서버) lược đồ (schema / 스키마) và nghiệp vụ (business / 비즈니스) ngữ nghĩa (semantics / 의미론) khác nhau:

```swift
struct UserDTO: Decodable { ... }
struct User { ... }
```

Máy chủ (server / 서버) enum có thể thêm trường hợp (case / 사례) trong tương lai. Nếu Đặc tả API (API contract / API 계약) cho phép forward evolution, máy khách (client / 클라이언트) cần unknown/fallback chiến lược (strategy / 전략) thay vì crash/decode thất bại (fail / 실패) toàn payload khi gặp giá trị mới.

---

# 26. Persistence: SwiftData và cốt lõi (core / 핵심) dữ liệu (data / 데이터) mô hình tư duy (mental model / 사고 모델)

SwiftData:

```swift
@Model
final class TaskItem {
    @Attribute(.unique) var id: UUID
    var title: String
    var isDone: Bool
}
```

Persistence phải nghĩ như cơ sở dữ liệu (database / 데이터베이스): lược đồ (schema / 스키마), unique/chỉ mục (index / 인덱스), relationship, delete quy tắc (rule / 규칙), giao dịch (transaction / 트랜잭션), di chuyển (migration / 마이그레이션), truy vấn (query / 쿼리) shape và tính đồng thời (concurrency / 동시성).

Cốt lõi (core / 핵심) dữ liệu (data / 데이터) vẫn rất phổ biến. Các khái niệm cần nắm: persistent bộ chứa (container / 컨테이너)/store, `NSManagedObjectContext`, managed đối tượng (object / 객체) định danh (identity / 식별자), fetch yêu cầu (request / 요청), relationship, merge chính sách (policy / 정책), background ngữ cảnh (context / 맥락) và di chuyển (migration / 마이그레이션).

Đừng truyền managed đối tượng (object / 객체) mutable tùy ý giữa hàng đợi (queue / 큐)/ngữ cảnh (context / 맥락). Khi crossing ranh giới (boundary / 경계), đối tượng (object / 객체) ID hoặc immutable snapshot thường an toàn hơn.

---

# 27. SwiftData truy vấn (query / 쿼리)/observation và ranh giới (boundary / 경계)

`@Query` ergonomic cho UI đơn giản. Nhưng tính năng (feature / 기능) có sync/lĩnh vực (domain / 도메인) quy tắc (rule / 규칙) phức tạp không nên để persistence truy vấn (query / 쿼리) tràn khắp view cây (tree / 트리).

SwiftData mới tiếp tục mở rộng truy vấn (query / 쿼리)/chỉ mục (index / 인덱스)/lịch sử (history / 이력)/observation năng lực (capability / 역량). API tiện hơn không thay yêu cầu (requirement / 요구사항) xác định nguồn chuẩn (source of truth / 정본) và di chuyển (migration / 마이그레이션) chính sách (policy / 정책).

Repository/store lớp trừu tượng (abstraction / 추상화) chỉ có giá trị nếu nó che data-source/lĩnh vực (domain / 도메인) ranh giới (boundary / 경계) thật; đừng tạo repository chỉ để mỗi phương thức (method / 메서드) forward thẳng một lời gọi (call / 호출) rồi tăng ceremony.

---

# 28. phụ thuộc (dependency / 의존성) injection và composition gốc (root / 루트)

Đoạn code dưới đây là bằng chứng cho khái niệm vừa mở. Hãy đọc từ input và state đến output, ghi lại điều kiện áp dụng và giới hạn trước khi chuyển sang mục kế tiếp.

```swift
final class ProductService {
    private let client: any HTTPClient

    init(client: any HTTPClient) {
        self.client = client
    }
}
```

Constructor injection làm phụ thuộc (dependency / 의존성) bắt buộc tường minh (explicit / 명시적). Không phải phụ thuộc (dependency / 의존성) nào cũng cần giao thức (protocol / 프로토콜); concrete kiểu (type / 타입) có thể inject/kiểm thử (test / 테스트) bằng fake wrapper/hàm (function / 함수) nếu đơn giản hơn.

Composition gốc (root / 루트) là nơi app dựng concrete hiện thực (implementation / 구현) và nối đồ thị (graph / 그래프). Nếu mỗi tính năng (feature / 기능) tự đọc singleton toàn cục (global / 전역), phụ thuộc (dependency / 의존성) luồng (flow / 흐름) trở nên ẩn và kiểm thử (test / 테스트)/thời gian tồn tại (lifetime / 수명) khó kiểm soát.

---

# 29. kiến trúc (architecture / 아키텍처): chọn ranh giới (boundary / 경계), không sưu tầm mẫu (pattern / 패턴)

MVC có thể tốt nếu controller nhỏ. MVVM hữu ích khi presentation trạng thái (state / 상태)/tác động (effect / 효과) đủ phức tạp; SwiftUI view không bắt buộc có ViewModel 1:1. Reducer/unidirectional kiến trúc (architecture / 아키텍처) phù hợp máy trạng thái (state machine / 상태 머신) nhiều hành động (action / 동작)/tác động (effect / 효과) và nhóm (team / 팀) cần convention tường minh (explicit / 명시적).

Một kiến trúc (architecture / 아키텍처) tốt trả lời được:

- nguồn chuẩn (source of truth / 정본) ở đâu;
- mutation xảy ra ở đâu;
- async tác động (effect / 효과) do ai sở hữu;
- phụ thuộc (dependency / 의존성) vào tính năng (feature / 기능) bằng cách nào;
- điều hướng (navigation / 내비게이션) thuộc tầng (layer / 계층) nào;
- persistence/mạng (network / 네트워크) DTO được map ở ranh giới (boundary / 경계) nào;
- kiểm thử (test / 테스트) hành vi (behavior / 동작) ở đâu.

Nếu phải tạo `BaseViewModel`, `BaseUseCase`, `BaseRepository` chỉ để mọi tệp (file / 파일) “đúng template”, kiến trúc (architecture / 아키텍처) đang phục vụ mẫu (pattern / 패턴) thay vì sản phẩm (product / 제품).

---

# 30. UIKit trung cấp — bố cục (layout / 레이아웃), reuse và vòng đời (lifecycle / 생명주기) consequences

Auto bố cục (layout / 레이아웃):

```swift
titleLabel.translatesAutoresizingMaskIntoConstraints = false
NSLayoutConstraint.activate([
    titleLabel.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 16),
    titleLabel.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -16),
    titleLabel.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 16)
])
```

Content hugging/compression resistance giải quyết xung đột (conflict / 충돌) khi intrinsic kích thước (size / 크기) cạnh tranh.

Diffable dữ liệu (data / 데이터) nguồn (source / 소스) dùng stable định danh (identity / 식별자):

```swift
var snapshot = NSDiffableDataSourceSnapshot<Section, Item.ID>()
snapshot.appendSections([.main])
snapshot.appendItems(items.map(\.id))
dataSource.apply(snapshot, animatingDifferences: true)
```

Cell reuse yêu cầu cancel/reset async ảnh (image / 이미지)/tác vụ (task / 작업) và mọi visual trạng thái (state / 상태) không còn hợp lệ khi cell được reuse.

---

# 31. SwiftUI ↔ UIKit interoperability trung cấp

Đoạn code dưới đây là bằng chứng cho khái niệm vừa mở. Hãy đọc từ input và state đến output, ghi lại điều kiện áp dụng và giới hạn trước khi chuyển sang mục kế tiếp.

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

Coordinator thường cầu nối (bridge / 브리지) delegate/callback UIKit → SwiftUI trạng thái (state / 상태). Đừng để `update...` tạo lại controller/tài nguyên (resource / 자원) nặng; `make...` tạo đối tượng (object / 객체), `update...` đồng bộ thay đổi.

UIKit host SwiftUI:

```swift
let host = UIHostingController(rootView: ProfileView())
```

Nếu add child controller thủ công, phải tuân view-controller containment vòng đời (lifecycle / 생명주기). Advanced sẽ đi sâu.

---

# 32. App vòng đời (lifecycle / 생명주기), scene vòng đời (lifecycle / 생명주기) và background công việc (work / 작업)

SwiftUI app dùng `App`/`Scene`; UIKit legacy dùng `UIApplicationDelegate`/`UISceneDelegate`.

```swift
@Environment(\.scenePhase) private var scenePhase
```

`active`, `inactive`, `background` là vòng đời (lifecycle / 생명주기) trạng thái (state / 상태), không phải lời hứa app được chạy bao lâu khi background.

BackgroundTasks, background URLSession, location/audio có quy tắc (rule / 규칙)/năng lực (capability / 역량) khác nhau. Nếu thao tác (operation / 연산) cần survive tiến trình (process / 프로세스) suspension/termination, thiết kế phải dựa đúng hệ thống (system / 시스템) API, không chỉ giữ một `Task` trong bộ nhớ (memory / 메모리).

---

# 33. Notification và deep link

Cục bộ (local / 로컬) notification được schedule trên thiết bị (device / 장치); remote push đi qua APNs/provider máy chủ (server / 서버). Permission, đơn vị từ (token / 토큰) vòng đời (lifecycle / 생명주기), foreground handling và người dùng (user / 사용자) hành động (action / 동작) routing là concern riêng.

Universal Link thường phù hợp web-to-app hơn custom URL scheme, nhưng cần Associated Domains và `apple-app-site-association` đúng. Parse deep link thành typed tuyến (route / 경로)/command sớm thay vì truyền raw string xuyên tính năng (feature / 기능).

---

# 34. Testing async/trạng thái (state / 상태) có tính deterministic

Kiểm thử (test / 테스트) pure lô-gic (logic / 논리) nhanh trước. Swift Testing:

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

Inject thời gian (time / 시간)/UUID/random/filesystem/mạng (network / 네트워크) phụ thuộc (dependency / 의존성) nếu hành vi (behavior / 동작) phụ thuộc chúng. kiểm thử (test / 테스트) không nên sleep vài giây để “chờ async”; dùng controllable phụ thuộc (dependency / 의존성)/clock/expectation/chuyển tiếp trạng thái (state transition / 상태 전이).

Tính đồng thời (concurrency / 동시성) kiểm thử (test / 테스트) cần có trường hợp (case / 사례) cancellation, duplicate yêu cầu (request / 요청), refresh single-flight và actor reentrancy, không chỉ happy đường dẫn (path / 경로).

---

# 35. Diagnostics và sanitizer

Xcode bộ nhớ (memory / 메모리) đồ thị (graph / 그래프) tìm retain đường dẫn (path / 경로). Address Sanitizer hữu ích đặc biệt ở unsafe/C/C++ ranh giới (boundary / 경계). luồng thực thi (thread / 스레드) Sanitizer phát hiện thời gian chạy (runtime / 런타임) race ở các đường mã (code / 코드) thực thi; Swift 6 isolation checking ngăn nhiều race ở compile thời gian (time / 시간). Hai lớp bổ sung nhau.

Main luồng thực thi (thread / 스레드) Checker vẫn hữu ích cho UIKit/legacy API. Với mã (code / 코드) Swift tính đồng thời (concurrency / 동시성) mới, actor isolation là mô hình tư duy (mental model / 사고 모델) chính.

---

# 36. Logging và lỗi (error / 오류) chiến lược (strategy / 전략)

Dùng `Logger`/OSLog theo category/subsystem; không log đơn vị từ (token / 토큰)/password/PII. lỗi (error / 오류) nhà phát triển (developer / 개발자) cần diagnostic detail; lỗi (error / 오류) người dùng (user / 사용자) cần actionable message. Đừng đưa raw `localizedDescription` của mọi hạ tầng (infrastructure / 인프라) lỗi (error / 오류) thẳng lên UI.

Metrics/crash reporting là môi trường vận hành (production / 운영 환경) concern; Advanced sẽ đi vào signpost, Instruments và trường dữ liệu (field / 필드) telemetry.

---

# 37. SwiftPM và ranh giới mô-đun (module boundary / 모듈 경계)

Gói (package / 패키지) mục tiêu (target / 대상) tạo compile-time ranh giới mô-đun (module boundary / 모듈 경계) thật. Tránh phụ thuộc (dependency / 의존성) cycle và “cốt lõi (core / 핵심)” mega-module mà mọi tính năng (feature / 기능) import.

Một mô-đun (module / 모듈) khỏe mạnh có cohesion rõ, API công khai (public API / 공개 API) nhỏ, phụ thuộc (dependency / 의존성) direction có chủ đích. Swift 6.4 dùng Swift bản dựng (build / 빌드) làm default SwiftPM hệ thống dựng (build system / 빌드 시스템); gói (package / 패키지) đa nền tảng cần `platforms`, conditional phụ thuộc (dependency / 의존성) và `#if canImport` chỉ ở ranh giới (boundary / 경계) phù hợp.

---

# 38. Availability và conditional compilation

Đoạn code dưới đây là bằng chứng cho khái niệm vừa mở. Hãy đọc từ input và state đến output, ghi lại điều kiện áp dụng và giới hạn trước khi chuyển sang mục kế tiếp.

```swift
#if DEBUG
let endpoint = URL(string: "https://staging.example.com")!
#endif

if #available(iOS 27, *) {
    // runtime API mới
}
```

`#if` chọn nguồn (source / 소스) lúc compile; `#available` chọn branch thời gian chạy (runtime / 런타임). Đừng dùng compile-time điều kiện (condition / 조건) để giả lập thời gian chạy (runtime / 런타임) availability.

---

# 39. Intermediate capstone — tính năng (feature / 기능) có quyền sở hữu (ownership / 소유권) hoàn chỉnh

Hãy xây một tính năng (feature / 기능) danh mục (catalog / 카탈로그)/tìm kiếm (search / 검색) đủ các đường dẫn (path / 경로): danh sách (list / 목록) + detail + tìm kiếm (search / 검색) debounce + pagination + bộ nhớ đệm (cache / 캐시)/persistence + login đơn vị từ (token / 토큰) mock + deep link.

Yêu cầu kiến trúc (architecture / 아키텍처) không phải số tầng (layer / 계층) mà là bạn phải chỉ được trên mã (code / 코드):

1. đơn vị sở hữu (owner / 오너) của observable tính năng (feature / 기능) trạng thái (state / 상태);
2. tác vụ (task / 작업) tìm kiếm (search / 검색) nào bị cancel khi truy vấn (query / 쿼리) đổi;
3. trạng thái (state / 상태) nào actor-isolated và vì sao;
4. dữ liệu (data / 데이터) nào crossing actor ranh giới (boundary / 경계) và có Sendable ngữ nghĩa (semantics / 의미론) ra sao;
5. UI trạng thái (state / 상태) nào derived, trạng thái (state / 상태) nào persisted/máy chủ (server / 서버) nguồn chuẩn (source of truth / 정본);
6. mạng (network / 네트워크) thử lại (retry / 재시도)/auth refresh nằm ở đâu;
7. SwiftData/cốt lõi (core / 핵심) dữ liệu (data / 데이터) đối tượng (object / 객체) có crossing ngữ cảnh (context / 맥락)/isolation không;
8. UIKit cầu nối (bridge / 브리지) nếu có, coordinator/thời gian tồn tại (lifetime / 수명) nằm ở đâu;
9. kiểm thử (test / 테스트) cancellation, lỗi (error / 오류), duplicate yêu cầu (request / 요청) và chuyển tiếp trạng thái (state transition / 상태 전이) thế nào.

Một cấu trúc tính năng (feature / 기능) có thể theo chiều dọc:

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

> **Chuyển mạch:** Trong **Swift & iOS Master ghi chú (note / 노트) — Intermediate**, **Checklist trước khi sang Advanced/cấp cao (senior / 시니어)** tiếp nhận điểm tựa từ **7.2 Snapshot mẫu (pattern / 패턴)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Checklist trước khi sang Advanced/cấp cao (senior / 시니어)

Bạn phải giải thích được sự khác nhau giữa structured child tác vụ (task / 작업), `Task {}` và detached tác vụ (task / 작업); actor reentrancy; MainActor isolation; `Sendable`/`@Sendable`; cancellation; `@State` quyền sở hữu (ownership / 소유권); `@Binding` projection; `@Bindable`; observable tham chiếu (reference / 참조) thời gian tồn tại (lifetime / 수명); view định danh (identity / 식별자); `.task(id:)`; persistence ngữ cảnh (context / 맥락) ranh giới (boundary / 경계); HTTP thử lại (retry / 재시도)/idempotency; và vì sao kiến trúc (architecture / 아키텍처) tốt làm trạng thái (state / 상태)/tác động (effect / 효과)/phụ thuộc (dependency / 의존성) luồng (flow / 흐름) rõ chứ không chỉ nhiều giao thức (protocol / 프로토콜).

Nếu một compiler concurrency warning chỉ được “sửa” bằng annotation mà bạn không giải thích được ownership/isolation trước và sau thay đổi, hãy xem đó là kiến thức chưa hoàn thành chứ không phải compiler khó tính.

> **Bàn giao:** Sau **Checklist trước khi sang Advanced/cấp cao (senior / 시니어)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
