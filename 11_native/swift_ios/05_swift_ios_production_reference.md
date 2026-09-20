# Swift & iOS — Production Reference & Completion Guide

> File này bổ sung cho bốn level Beginner → Intermediate → Advanced/Senior → Master. Nó không thay thế thứ tự học chính. Mục tiêu là gom những chủ đề xuyên cấp thường chỉ xuất hiện khi một ứng dụng đi từ demo sang production: closure lifetime, numeric correctness, HTTP semantics, tolerant decoding, retry/idempotency, Core Data legacy, background transfer, ownership mới của Swift, build tooling, observability, process boundary, supply-chain security, release recovery và production checklist.

## 1. Closure lifetime: `@escaping`, capture, `@Sendable` và `inout`

Closure là function value, nhưng khi được truyền qua API thật, điều quan trọng không chỉ là syntax mà còn là lifetime và isolation. Closure *non-escaping* phải hoàn thành trước khi function nhận nó return. Closure *escaping* có thể bị lưu lại và chạy về sau, nên parameter phải được đánh dấu `@escaping`. Completion handler của API callback cũ, event callback lưu trong object và một số bridge delegate là ví dụ phổ biến.

```swift
final class Loader {
    private var completion: (() -> Void)?

    func start(completion: @escaping () -> Void) {
        self.completion = completion
    }
}
```

Escaping closure là một nguồn retain cycle vì owner có thể giữ closure, trong khi closure capture owner. `[weak self]` là công cụ phá cycle khi ownership graph thực sự có vòng; nó không phải cú pháp phải thêm vào mọi closure. Nếu callback bắt buộc owner tồn tại để operation có ý nghĩa, đôi khi strong capture mới là semantics đúng.

Trong Swift concurrency, `@Sendable` bổ sung một contract khác: closure có thể được transfer/chạy trong concurrency domain khác. Capture mutable class không thread-safe có thể bị compiler cảnh báo. Fix đúng thường là actor-isolate state, capture immutable snapshot hoặc thay đổi ownership; `@unchecked Sendable` chỉ nên dùng khi bạn tự chứng minh synchronization invariant.

`inout` cho function quyền mutate một value của caller trong phạm vi synchronous call:

```swift
func increment(_ value: inout Int) {
    value += 1
}

var count = 0
increment(&count)
```

`inout` không nên được dùng để giả lập shared reference state. Khi state có lifetime dài hoặc đi qua concurrency boundary, hãy model ownership bằng type/actor/service phù hợp.

## 2. Numeric correctness: overflow, floating point và tiền tệ

Swift ưu tiên arithmetic safety. Integer overflow thông thường sẽ trap thay vì silently wrap. Các operator `&+`, `&-`, `&*` cho phép wraparound có chủ đích, phù hợp low-level algorithm, hashing hoặc binary protocol chứ không nên dùng để “né crash”.

`Double` dùng binary floating-point IEEE 754 nên nhiều số thập phân không thể biểu diễn chính xác. Vì vậy equality trực tiếp cho kết quả tính toán floating-point cần được xem xét theo tolerance, còn dữ liệu tiền tệ nên chọn representation theo invariant domain. Có thể dùng `Decimal` khi cần decimal arithmetic hoặc integer minor unit như cents/won nhỏ nhất khi domain cho phép.

Senior Note: numeric type là một phần domain model. Chọn `Double` cho exchange-rate calculation, `Decimal` cho accounting và integer cho count không phải style preference; nó quyết định precision, rounding và error behavior.

## 3. HTTP semantics trước network abstraction

`URLSession` chỉ là transport API. Một iOS engineer cần hiểu request gồm method, URL, headers và optional body; response gồm status, headers và body. GET thường dùng để đọc, POST thường tạo/action, PUT thường replace theo contract, PATCH partial update và DELETE xóa, nhưng backend contract mới là nguồn semantics cuối cùng.

`2xx` thường success, `4xx` là request/client-context error, `5xx` là server-side failure. `URLSession.data(for:)` không throw chỉ vì server trả 404 hoặc 500; transport vẫn có thể thành công. Vì vậy network layer phải kiểm `HTTPURLResponse.statusCode` rồi mới decode success payload.

```swift
let (data, response) = try await session.data(for: request)

guard let http = response as? HTTPURLResponse else {
    throw NetworkError.invalidResponse
}

guard 200..<300 ~= http.statusCode else {
    throw try mapServerError(status: http.statusCode, data: data)
}
```

`401` thường gắn với authentication, `403` thường gắn authorization, nhưng app không nên hard-code UX chỉ dựa trên số status nếu backend định nghĩa error code chi tiết hơn.

## 4. Retry, exponential backoff, jitter và idempotency

Retry chỉ đúng khi failure có khả năng transient và operation an toàn để lặp. Connection reset, timeout hoặc một số `5xx` có thể đáng retry. Validation error, revoked credential hoặc domain conflict thường không.

Exponential backoff tăng thời gian chờ theo lần thử; jitter thêm độ ngẫu nhiên để hàng nghìn client không retry đồng thời. Cancellation phải được kiểm trước/sau sleep để user rời màn hình không còn gây request tiếp tục.

Với mutation như payment/order/create-resource, client-side retry chỉ an toàn khi backend có idempotency semantics hoặc operation vốn idempotent. Một request timeout có thể đã thành công ở server dù client không nhận response; gửi lại mù quáng có thể tạo dữ liệu trùng.

## 5. Codable tolerant và API evolution

Mobile client có release lag nên decoder phải chịu được backend tiến hóa trong compatibility window. Thêm field thường an toàn vì `Decodable` bỏ qua field dư; nhưng enum thêm case có thể làm decode fail nếu client chỉ biết các case cũ.

Với payload có discriminator, custom `init(from:)` giúp decode polymorphic model. Với server enum có thể mở rộng, có thể dùng `unknown(String)` hoặc fallback phù hợp domain thay vì fail toàn response. Tuy nhiên không nên swallow mọi decoding error; schema corruption thật phải observable để team phát hiện contract regression.

Tách DTO khỏi domain model có lợi khi transport schema không ổn định. DTO có thể tolerant với server, còn domain model giữ invariant mạnh hơn.

## 6. Core Data mental model để maintain codebase legacy

Core Data không chỉ là wrapper SQLite. `NSManagedObjectContext` là object graph/unit-of-work context với concurrency rule riêng. Managed object thuộc context; save ghi change theo topology của context/container; merge policy giải quyết conflict; `NSManagedObjectID` là cách an toàn hơn để tham chiếu object qua context boundary.

Background context cho phép fetch/import ngoài main queue, nhưng không nên đưa một `NSManagedObject` trực tiếp sang context khác. Hãy truyền object ID hoặc map thành immutable snapshot. Hiểu model này cũng giúp học SwiftData sâu hơn vì nhiều bài toán persistence—identity, migration, relationship, history, transaction boundary—không biến mất chỉ vì API mới ergonomic hơn.

## 7. Background URLSession và operation sống lâu hơn UI

`View.task` phù hợp work có lifetime gắn với view. Download/upload lớn hoặc operation phải tiếp tục khi app background cần owner khác. Background `URLSessionConfiguration` cho phép hệ thống tiếp tục một số transfer và đánh thức app để giao event theo lifecycle được hỗ trợ.

Điều này dẫn đến một nguyên tắc kiến trúc: task lifetime phải thuộc business owner đúng. Nếu upload phải sống qua navigation hoặc restart, metadata trạng thái cần được persist; không thể chỉ giữ trong `@State` hoặc ViewModel tạm thời.

## 8. UIKit lifecycle và Auto Layout diagnostic

`UIViewController` có các phase như `loadView`, `viewDidLoad`, `viewWillAppear`, `viewDidAppear`, `viewWillDisappear`, `viewDidDisappear`. `viewDidLoad` phù hợp setup view một lần cho view instance, nhưng không có nghĩa controller chỉ xuất hiện một lần trong app.

Auto Layout warning cần được đọc như constraint system. *Ambiguous* nghĩa có nhiều nghiệm; *unsatisfiable* nghĩa constraint xung đột. Content hugging nói view không muốn lớn hơn intrinsic content size, còn compression resistance nói view không muốn nhỏ hơn intrinsic size. Priority không nên được chỉnh ngẫu nhiên chỉ để console hết warning; phải phản ánh layout rule mong muốn.

## 9. Ownership mới: borrowing, consuming, noncopyable

Swift hiện đại ngày càng cho phép diễn đạt ownership chính xác. `borrowing` cho phép dùng value mà không chuyển ownership; `consuming` chuyển ownership; noncopyable type (`~Copyable`) cho phép model resource không được copy tùy ý.

Các feature này quan trọng với systems/library code, buffer, handle hoặc resource độc quyền. App business model bình thường vẫn nên ưu tiên type đơn giản. Mastery không phải dùng feature mới khắp nơi mà là nhận ra khi copying/ownership thực sự là constraint.

## 10. SwiftPM plugin, generated code và build determinism

SwiftPM build tool/plugin có thể generate source từ schema, localization, API description hoặc asset pipeline. Generation phải deterministic: cùng input/tool version phải cho cùng output. CI cần pin generator/toolchain và fail nếu generated artifact drift khỏi source-of-truth policy.

Generated code phù hợp boilerplate máy tạo; business logic quan trọng nên vẫn reviewable. Một generator quá “thông minh” có thể khiến debugging và compile-time khó hơn code viết tay.

## 11. Observability: Logger, signpost, Instruments và MetricKit

Logging trả lời “điều gì đã xảy ra”, metric trả lời “xảy ra bao nhiêu/lâu thế nào”, trace/signpost giúp nối flow. `OSLog`/`Logger` nên dùng category/subsystem hợp lý và privacy annotation cho dữ liệu nhạy cảm.

`OSSignposter` hoặc signpost interval hữu ích khi đo flow như tap → fetch → decode → render. Instruments cho lab profiling; MetricKit và telemetry production giúp nhìn crash/hang/launch/CPU-memory-responsiveness trên device thật tùy metric hỗ trợ.

Performance investigation nên có baseline và hypothesis. Không optimize theo trực giác hoặc chỉ nhìn một screenshot profiler.

## 12. Memory graph: retain cycle và cache growth

Khi object không deallocate, Memory Graph giúp truy root strong reference. Common source gồm timer/display link, observer legacy, delegate không weak, service giữ callback, task giữ owner hoặc cache không có eviction.

`[weak self]` không chữa mọi memory growth. Cache giữ dữ liệu chủ đích cũng làm memory tăng nhưng không nhất thiết là leak. Cần phân biệt unbounded retention, cache policy và temporary peak.

## 13. App extension là process boundary

Widget, Share Extension, Notification Service Extension và main app không chia sẻ singleton/memory chỉ vì dùng chung module. Chúng có process/lifecycle/resource budget riêng. Data sharing cần App Group container, Keychain access group hoặc mechanism được platform hỗ trợ.

Do budget chặt, extension nên tránh kéo dependency nặng nếu không cần. Core module dùng chung nên giữ nhẹ, còn SDK hoặc service chỉ main app cần đặt ở composition layer của app.

## 14. Supply-chain security của package và SDK

Mỗi third-party package mở rộng trust boundary. Review không chỉ số star mà còn maintainer, provenance/release process, license, vulnerability history, privacy manifest, transitive dependency và khả năng exit.

Pin/resolved version góp phần reproducible build. Major update không nên tự động ship mà không review. Với SDK analytics/ads/auth/payment, privacy/security review phải tương xứng lượng dữ liệu và quyền truy cập SDK có.

## 15. Make invalid states unrepresentable

Type system nên giúp loại bỏ trạng thái vô nghĩa. Một API nhận `String` mode, optional retry và optional token cho phép nhiều combination sai. Enum/value object có thể biến intent thành compile-time model.

```swift
enum Authentication {
    case anonymous
    case bearer(Token)
}

struct RetryPolicy {
    let maximumAttempts: Int
}
```

Nhưng đừng wrapper mọi primitive vô điều kiện. Hãy tạo type khi nó mang invariant/semantic đáng bảo vệ.

## 16. ADR và compatibility matrix

Architecture Decision Record (ADR) ghi context, quyết định, alternative và consequence cho quyết định đáng kể như minimum iOS version, SwiftData vs Core Data, module strategy hoặc retry policy. Mục tiêu là lưu *lý do*, không phải tạo tài liệu dài.

Team production cũng nên có compatibility matrix: Xcode/toolchain được phép, Swift language mode, minimum deployment target, OS/device test set, backend compatibility window và package policy. Encode phần quan trọng vào CI để tránh local/CI drift.

## 17. Disaster recovery và mobile rollback

Mobile binary không rollback tức thời. User có thể giữ version lỗi dù team đã phát hành hotfix. Do đó feature rủi ro nên có mitigation phù hợp: backend backward compatibility, remote kill switch/feature flag nơi hợp lý, observability và migration strategy không phá dữ liệu.

Không phải mọi feature cần remote flag. Flag cũng tạo combinatorial complexity và phải có owner/expiry. Rigor phải tỷ lệ với hậu quả khi feature sai.

## 18. Performance model từ algorithm đến frame budget

Performance không có một bottleneck duy nhất. Algorithm O(n²) có thể vô hại với 20 item nhưng nguy hiểm với 100.000. Image decode trên main thread có thể gây hitch dù algorithm O(n). Database thiếu index có thể chậm hơn mọi micro-optimization Swift.

Trước khi tối ưu, xác định resource giới hạn: CPU, GPU, memory, I/O, network, lock contention, actor serialization hay main-thread work. Sau đó chọn công cụ đo tương ứng.

## 19. Security review theo data flow

Keychain chỉ bảo vệ một phần dữ liệu. Security review tốt vẽ data flow: credential vào từ đâu, nằm memory bao lâu, có ghi disk/log không, request đi endpoint nào, extension/SDK nào đọc được, logout có xóa đúng không.

Threat model phải gắn asset và attacker: token theft, reverse engineering, MITM, compromised device và unauthorized backend action là threat khác nhau. Client hardening không thay backend authorization.

## 20. Test release artifact, không chỉ Debug source

Unit test Debug Simulator xanh chưa đảm bảo archive Release đúng. Pipeline production nên build/archive configuration thật và kiểm entitlement/signing/resource/configuration. Khi khả thi, smoke test artifact hoặc build gần release artifact trên device/arm64.

Optimization-sensitive race, missing resource, wrong environment endpoint, entitlement khác Debug hoặc package/device architecture issue thường chỉ lộ gần release.

## 21. Definition of Done theo risk

Một feature production hoàn thành khi behavior happy/error/cancel được định nghĩa, accessibility/localization hợp lý, test critical logic, availability/deployment target đúng, persistence/migration impact được xem xét, telemetry đủ cho risk và rollout strategy phù hợp.

Definition of Done không nên nặng như nhau cho mọi feature. Một local toggle và payment flow có hậu quả khác nhau. Senior/master skill nằm ở việc scale rigor theo risk.

## 22. Capstone audit

Để kiểm tra toàn bộ bộ note, hãy xây một app mẫu có login, feed phân trang, search debounce, upload/download, local persistence, offline mode, deep link, push notification, background work và purchase giả lập. Với từng feature, tự trả lời: source of truth ở đâu; state owner là ai; task lifetime là gì; actor isolation ở đâu; cancellation/retry thế nào; migration ra sao; backward compatibility với backend thế nào; test gì; metric gì; và fallback ra sao khi API mới không tồn tại trên deployment target cũ.

Nếu có thể trả lời nhất quán mà không cần viện tên pattern như một đáp án, bạn đã chuyển từ “biết Swift/iOS API” sang có khả năng ownership một hệ thống iOS production.
