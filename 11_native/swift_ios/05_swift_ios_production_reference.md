# Swift & iOS — môi trường vận hành (production / 운영 환경) tham chiếu (reference / 참조) & Completion Guide

> **Mạch đọc:** [README](./README.md) là owner của **Swift & iOS — môi trường vận hành (production / 운영 환경) tham chiếu (reference / 참조) & Completion Guide**; quay lại đó khi cần phân biệt tài liệu tham chiếu với bốn mức học chuẩn. Trong file này, nối **1. Closure thời gian tồn tại (lifetime / 수명)** với **2. Numeric tính đúng đắn (correctness / 정확성)**, rồi đi qua HTTP semantics, retry/idempotency, persistence, background transfer, observability và supply-chain; các ví dụ sau là hệ quả vận hành của hợp đồng và dữ liệu ở các mục trước.

> tệp (file / 파일) này bổ sung cho bốn mức (level / 수준) Beginner → Intermediate → Advanced/cấp cao (senior / 시니어) → Master. Nó không thay thế thứ tự học chính. Mục tiêu là gom những chủ đề xuyên cấp thường chỉ xuất hiện khi một ứng dụng đi từ demo sang môi trường vận hành (production / 운영 환경): closure thời gian tồn tại (lifetime / 수명), numeric tính đúng đắn (correctness / 정확성), HTTP ngữ nghĩa (semantics / 의미론), tolerant decoding, thử lại (retry / 재시도)/idempotency, cốt lõi (core / 핵심) dữ liệu (data / 데이터) legacy, background transfer, quyền sở hữu (ownership / 소유권) mới của Swift, bản dựng (build / 빌드) tooling, khả năng quan sát (observability / 관측 가능성), tiến trình (process / 프로세스) ranh giới (boundary / 경계), supply-chain bảo mật (security / 보안), bản phát hành (release / 릴리스) khôi phục (recovery / 복구) và môi trường vận hành (production / 운영 환경) checklist.

## 1. Closure thời gian tồn tại (lifetime / 수명): `@escaping`, capture, `@Sendable` và `inout`

Closure là hàm (function / 함수) giá trị (value / 값), nhưng khi được truyền qua API thật, điều quan trọng không chỉ là cú pháp (syntax / 문법) mà còn là thời gian tồn tại (lifetime / 수명) và isolation. Closure *non-escaping* phải hoàn thành trước khi hàm (function / 함수) nhận nó return. Closure *escaping* có thể bị lưu lại và chạy về sau, nên parameter phải được đánh dấu `@escaping`. Completion handler của API callback cũ, sự kiện (event / 이벤트) callback lưu trong đối tượng (object / 객체) và một số cầu nối (bridge / 브리지) delegate là ví dụ phổ biến.

```swift
final class Loader {
    private var completion: (() -> Void)?

    func start(completion: @escaping () -> Void) {
        self.completion = completion
    }
}
```

Escaping closure là một nguồn retain cycle vì đơn vị sở hữu (owner / 오너) có thể giữ closure, trong khi closure capture đơn vị sở hữu (owner / 오너). `[weak self]` là công cụ phá cycle khi quyền sở hữu (ownership / 소유권) đồ thị (graph / 그래프) thực sự có vòng; nó không phải cú pháp phải thêm vào mọi closure. Nếu callback bắt buộc đơn vị sở hữu (owner / 오너) tồn tại để thao tác (operation / 연산) có ý nghĩa, đôi khi strong capture mới là ngữ nghĩa (semantics / 의미론) đúng.

Trong Swift tính đồng thời (concurrency / 동시성), `@Sendable` bổ sung một đặc tả hợp đồng (contract / 계약) khác: closure có thể được transfer/chạy trong tính đồng thời (concurrency / 동시성) lĩnh vực (domain / 도메인) khác. Capture mutable lớp (class / 클래스) không thread-safe có thể bị trình biên dịch (compiler / 컴파일러) cảnh báo. Fix đúng thường là actor-isolate trạng thái (state / 상태), capture immutable snapshot hoặc thay đổi quyền sở hữu (ownership / 소유권); `@unchecked Sendable` chỉ nên dùng khi bạn tự chứng minh synchronization bất biến (invariant / 불변식).

`inout` cho hàm (function / 함수) quyền mutate một giá trị (value / 값) của caller trong phạm vi synchronous lời gọi (call / 호출):

```swift
func increment(_ value: inout Int) {
    value += 1
}

var count = 0
increment(&count)
```

`inout` không nên được dùng để giả lập dùng chung (shared / 공유) tham chiếu (reference / 참조) trạng thái (state / 상태). Khi trạng thái (state / 상태) có thời gian tồn tại (lifetime / 수명) dài hoặc đi qua tính đồng thời (concurrency / 동시성) ranh giới (boundary / 경계), hãy mô hình (model / 모델) quyền sở hữu (ownership / 소유권) bằng kiểu (type / 타입)/actor/dịch vụ (service / 서비스) phù hợp.

> **Nối mạch:** Trong **Swift & iOS — môi trường vận hành (production / 운영 환경) tham chiếu (reference / 참조) & Completion Guide**, **1. Closure thời gian tồn tại (lifetime / 수명): @escaping, capture, @Sendable và inout** đặt đầu vào cho **2. Numeric tính đúng đắn (correctness / 정확성): overflow, floating điểm (point / 지점) và tiền tệ**, rồi **3. HTTP ngữ nghĩa (semantics / 의미론) trước mạng (network / 네트워크) lớp trừu tượng (abstraction / 추상화)** mở rộng hệ quả hoặc giới hạn liên quan.

## 2. Numeric tính đúng đắn (correctness / 정확성): overflow, floating điểm (point / 지점) và tiền tệ

Swift ưu tiên arithmetic an toàn (safety / 안전). Integer overflow thông thường sẽ trap thay vì silently wrap. Các operator `&+`, `&-`, `&*` cho phép wraparound có chủ đích, phù hợp low-level thuật toán (algorithm / 알고리즘), hashing hoặc nhị phân (binary / 이진) giao thức (protocol / 프로토콜) chứ không nên dùng để “né crash”.

`Double` dùng nhị phân (binary / 이진) floating-point IEEE 754 nên nhiều số thập phân không thể biểu diễn chính xác. Vì vậy equality trực tiếp cho kết quả tính toán floating-point cần được xem xét theo tolerance, còn dữ liệu tiền tệ nên chọn biểu diễn (representation / 표현) theo bất biến (invariant / 불변식) lĩnh vực (domain / 도메인). Có thể dùng `Decimal` khi cần decimal arithmetic hoặc integer minor đơn vị (unit / 단위) như cents/won nhỏ nhất khi lĩnh vực (domain / 도메인) cho phép.

Cấp cao (senior / 시니어) ghi chú (note / 노트): numeric kiểu (type / 타입) là một phần lĩnh vực (domain / 도메인) mô hình (model / 모델). Chọn `Double` cho exchange-rate calculation, `Decimal` cho accounting và integer cho count không phải style preference; nó quyết định precision, rounding và lỗi (error / 오류) hành vi (behavior / 동작).

> **Nối mạch:** Ở chặng này của **Swift & iOS — môi trường vận hành (production / 운영 환경) tham chiếu (reference / 참조) & Completion Guide**, **2. Numeric tính đúng đắn (correctness / 정확성): overflow, floating điểm (point / 지점) và tiền tệ** đặt đầu vào cho **3. HTTP ngữ nghĩa (semantics / 의미론) trước mạng (network / 네트워크) lớp trừu tượng (abstraction / 추상화)**, rồi **4. thử lại (retry / 재시도), exponential backoff, jitter và idempotency** mở rộng hệ quả hoặc giới hạn liên quan.

## 3. HTTP ngữ nghĩa (semantics / 의미론) trước mạng (network / 네트워크) lớp trừu tượng (abstraction / 추상화)

`URLSession` chỉ là vận chuyển (transport / 전송) API. Một iOS engineer cần hiểu yêu cầu (request / 요청) gồm phương thức (method / 메서드), URL, headers và optional body; phản hồi (response / 응답) gồm status, headers và body. GET thường dùng để đọc, POST thường tạo/hành động (action / 동작), PUT thường replace theo đặc tả hợp đồng (contract / 계약), PATCH partial cập nhật (update / 업데이트) và DELETE xóa, nhưng backend đặc tả hợp đồng (contract / 계약) mới là nguồn ngữ nghĩa (semantics / 의미론) cuối cùng.

`2xx` thường success, `4xx` là yêu cầu (request / 요청)/client-context lỗi (error / 오류), `5xx` là server-side thất bại (failure / 실패). `URLSession.data(for:)` không throw chỉ vì máy chủ (server / 서버) trả 404 hoặc 500; vận chuyển (transport / 전송) vẫn có thể thành công. Vì vậy mạng (network / 네트워크) tầng (layer / 계층) phải kiểm `HTTPURLResponse.statusCode` rồi mới decode success payload.

```swift
let (data, response) = try await session.data(for: request)

guard let http = response as? HTTPURLResponse else {
    throw NetworkError.invalidResponse
}

guard 200..<300 ~= http.statusCode else {
    throw try mapServerError(status: http.statusCode, data: data)
}
```

`401` thường gắn với authentication, `403` thường gắn authorization, nhưng app không nên hard-code UX chỉ dựa trên số status nếu backend định nghĩa lỗi (error / 오류) mã (code / 코드) chi tiết hơn.

> **Nối mạch:** HTTP semantics phải rõ trước khi retry; exponential backoff/jitter giảm thundering herd, còn idempotency bảo vệ side effect trước khi API evolution.

## 4. thử lại (retry / 재시도), exponential backoff, jitter và idempotency

Thử lại (retry / 재시도) chỉ đúng khi thất bại (failure / 실패) có khả năng transient và thao tác (operation / 연산) an toàn để lặp. liên kết (connection / 연결) reset, hết thời gian chờ (timeout / 타임아웃) hoặc một số `5xx` có thể đáng thử lại (retry / 재시도). kiểm tra hợp lệ (validation / 검증) lỗi (error / 오류), revoked credential hoặc lĩnh vực (domain / 도메인) xung đột (conflict / 충돌) thường không.

Exponential backoff tăng thời gian chờ theo lần thử; jitter thêm độ ngẫu nhiên để hàng nghìn máy khách (client / 클라이언트) không thử lại (retry / 재시도) đồng thời. Cancellation phải được kiểm trước/sau sleep để người dùng (user / 사용자) rời màn hình không còn gây yêu cầu (request / 요청) tiếp tục.

Với mutation như payment/thứ tự (order / 순서)/create-resource, client-side thử lại (retry / 재시도) chỉ an toàn khi backend có idempotency ngữ nghĩa (semantics / 의미론) hoặc thao tác (operation / 연산) vốn idempotent. Một yêu cầu (request / 요청) hết thời gian chờ (timeout / 타임아웃) có thể đã thành công ở máy chủ (server / 서버) dù máy khách (client / 클라이언트) không nhận phản hồi (response / 응답); gửi lại mù quáng có thể tạo dữ liệu trùng.

> **Nối mạch:** Retry/idempotency bảo vệ request side effects; Codable tolerant tiếp theo bảo vệ schema evolution, rồi legacy maintenance cần một core data mental model ổn định.

## 5. Codable tolerant và API evolution

Mobile máy khách (client / 클라이언트) có bản phát hành (release / 릴리스) lag nên decoder phải chịu được backend tiến hóa trong tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우). Thêm trường dữ liệu (field / 필드) thường an toàn vì `Decodable` bỏ qua trường dữ liệu (field / 필드) dư; nhưng enum thêm trường hợp (case / 사례) có thể làm decode thất bại (fail / 실패) nếu máy khách (client / 클라이언트) chỉ biết các trường hợp (case / 사례) cũ.

Với payload có discriminator, custom `init(from:)` giúp decode polymorphic mô hình (model / 모델). Với máy chủ (server / 서버) enum có thể mở rộng, có thể dùng `unknown(String)` hoặc fallback phù hợp lĩnh vực (domain / 도메인) thay vì thất bại (fail / 실패) toàn phản hồi (response / 응답). Tuy nhiên không nên swallow mọi decoding lỗi (error / 오류); lược đồ (schema / 스키마) corruption thật phải observable để nhóm (team / 팀) phát hiện đặc tả hợp đồng (contract / 계약) regression.

Tách DTO khỏi lĩnh vực (domain / 도메인) mô hình (model / 모델) có lợi khi vận chuyển (transport / 전송) lược đồ (schema / 스키마) không ổn định. DTO có thể tolerant với máy chủ (server / 서버), còn lĩnh vực (domain / 도메인) mô hình (model / 모델) giữ bất biến (invariant / 불변식) mạnh hơn.

> **Nối mạch:** Ở chặng này của **Swift & iOS — môi trường vận hành (production / 운영 환경) tham chiếu (reference / 참조) & Completion Guide**, **5. Codable tolerant và API evolution** đặt vấn đề; **6. cốt lõi (core / 핵심) dữ liệu (data / 데이터) mô hình tư duy (mental model / 사고 모델) để maintain codebase legacy** đối chiếu bằng chứng, rồi **7. Background URLSession và thao tác (operation / 연산) sống lâu hơn UI** mở rộng hệ quả hoặc giới hạn liên quan.

## 6. cốt lõi (core / 핵심) dữ liệu (data / 데이터) mô hình tư duy (mental model / 사고 모델) để maintain codebase legacy

Cốt lõi (core / 핵심) dữ liệu (data / 데이터) không chỉ là wrapper SQLite. `NSManagedObjectContext` là đối tượng (object / 객체) đồ thị (graph / 그래프)/unit-of-work ngữ cảnh (context / 맥락) với tính đồng thời (concurrency / 동시성) quy tắc (rule / 규칙) riêng. Managed đối tượng (object / 객체) thuộc ngữ cảnh (context / 맥락); save ghi thay đổi (change / 변경) theo topology của ngữ cảnh (context / 맥락)/bộ chứa (container / 컨테이너); merge chính sách (policy / 정책) giải quyết xung đột (conflict / 충돌); `NSManagedObjectID` là cách an toàn hơn để tham chiếu đối tượng (object / 객체) qua ngữ cảnh (context / 맥락) ranh giới (boundary / 경계).

Background ngữ cảnh (context / 맥락) cho phép fetch/import ngoài main hàng đợi (queue / 큐), nhưng không nên đưa một `NSManagedObject` trực tiếp sang ngữ cảnh (context / 맥락) khác. Hãy truyền đối tượng (object / 객체) ID hoặc map thành immutable snapshot. Hiểu mô hình (model / 모델) này cũng giúp học SwiftData sâu hơn vì nhiều bài toán persistence—định danh (identity / 식별자), di chuyển (migration / 마이그레이션), relationship, lịch sử (history / 이력), giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계)—không biến mất chỉ vì API mới ergonomic hơn.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Swift & iOS — môi trường vận hành (production / 운영 환경) tham chiếu (reference / 참조) & Completion Guide**, **6. cốt lõi (core / 핵심) dữ liệu (data / 데이터) mô hình tư duy (mental model / 사고 모델) để maintain codebase legacy** đặt vấn đề; **7. Background URLSession và thao tác (operation / 연산) sống lâu hơn UI** đối chiếu bằng chứng, rồi **8. UIKit vòng đời (lifecycle / 생명주기) và Auto bố cục (layout / 레이아웃) diagnostic** mở rộng hệ quả hoặc giới hạn liên quan.

## 7. Background URLSession và thao tác (operation / 연산) sống lâu hơn UI

`View.task` phù hợp công việc (work / 작업) có thời gian tồn tại (lifetime / 수명) gắn với view. Download/upload lớn hoặc thao tác (operation / 연산) phải tiếp tục khi app background cần đơn vị sở hữu (owner / 오너) khác. Background `URLSessionConfiguration` cho phép hệ thống tiếp tục một số transfer và đánh thức app để giao sự kiện (event / 이벤트) theo vòng đời (lifecycle / 생명주기) được hỗ trợ.

Điều này dẫn đến một nguyên tắc kiến trúc: tác vụ (task / 작업) thời gian tồn tại (lifetime / 수명) phải thuộc nghiệp vụ (business / 비즈니스) đơn vị sở hữu (owner / 오너) đúng. Nếu upload phải sống qua điều hướng (navigation / 내비게이션) hoặc restart, siêu dữ liệu (metadata / 메타데이터) trạng thái cần được persist; không thể chỉ giữ trong `@State` hoặc ViewModel tạm thời.

> **Nối mạch:** Trong **Swift & iOS — môi trường vận hành (production / 운영 환경) tham chiếu (reference / 참조) & Completion Guide**, **7. Background URLSession và thao tác (operation / 연산) sống lâu hơn UI** đặt đầu vào cho **8. UIKit vòng đời (lifecycle / 생명주기) và Auto bố cục (layout / 레이아웃) diagnostic**, rồi **9. quyền sở hữu (ownership / 소유권) mới: borrowing, consuming, noncopyable** mở rộng hệ quả hoặc giới hạn liên quan.

## 8. UIKit vòng đời (lifecycle / 생명주기) và Auto bố cục (layout / 레이아웃) diagnostic

`UIViewController` có các phase như `loadView`, `viewDidLoad`, `viewWillAppear`, `viewDidAppear`, `viewWillDisappear`, `viewDidDisappear`. `viewDidLoad` phù hợp setup view một lần cho view instance, nhưng không có nghĩa controller chỉ xuất hiện một lần trong app.

Auto bố cục (layout / 레이아웃) warning cần được đọc như ràng buộc (constraint / 제약조건) hệ thống (system / 시스템). *Ambiguous* nghĩa có nhiều nghiệm; *unsatisfiable* nghĩa ràng buộc (constraint / 제약조건) xung đột. Content hugging nói view không muốn lớn hơn intrinsic content kích thước (size / 크기), còn compression resistance nói view không muốn nhỏ hơn intrinsic kích thước (size / 크기). Priority không nên được chỉnh ngẫu nhiên chỉ để console hết warning; phải phản ánh bố cục (layout / 레이아웃) quy tắc (rule / 규칙) mong muốn.

> **Nối mạch:** Ở chặng này của **Swift & iOS — môi trường vận hành (production / 운영 환경) tham chiếu (reference / 참조) & Completion Guide**, **8. UIKit vòng đời (lifecycle / 생명주기) và Auto bố cục (layout / 레이아웃) diagnostic** đặt đầu vào cho **9. quyền sở hữu (ownership / 소유권) mới: borrowing, consuming, noncopyable**, rồi **10. SwiftPM plugin, generated mã (code / 코드) và bản dựng (build / 빌드) determinism** mở rộng hệ quả hoặc giới hạn liên quan.

## 9. quyền sở hữu (ownership / 소유권) mới: borrowing, consuming, noncopyable

Swift hiện đại ngày càng cho phép diễn đạt quyền sở hữu (ownership / 소유권) chính xác. `borrowing` cho phép dùng giá trị (value / 값) mà không chuyển quyền sở hữu (ownership / 소유권); `consuming` chuyển quyền sở hữu (ownership / 소유권); noncopyable kiểu (type / 타입) (`~Copyable`) cho phép mô hình (model / 모델) tài nguyên (resource / 자원) không được bản sao (copy / 복사) tùy ý.

Các tính năng (feature / 기능) này quan trọng với các hệ thống (systems / 시스템들)/thư viện (library / 라이브러리) mã (code / 코드), buffer, handle hoặc tài nguyên (resource / 자원) độc quyền. App nghiệp vụ (business / 비즈니스) mô hình (model / 모델) bình thường vẫn nên ưu tiên kiểu (type / 타입) đơn giản. Mastery không phải dùng tính năng (feature / 기능) mới khắp nơi mà là nhận ra khi copying/quyền sở hữu (ownership / 소유권) thực sự là ràng buộc (constraint / 제약조건).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Swift & iOS — môi trường vận hành (production / 운영 환경) tham chiếu (reference / 참조) & Completion Guide**, **10. SwiftPM plugin, generated mã (code / 코드) và bản dựng (build / 빌드) determinism** nối từ **9. quyền sở hữu (ownership / 소유권) mới: borrowing, consuming, noncopyable** sang **11. khả năng quan sát (observability / 관측 가능성): Logger, signpost, Instruments và MetricKit**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. SwiftPM plugin, generated mã (code / 코드) và bản dựng (build / 빌드) determinism

SwiftPM bản dựng (build / 빌드) công cụ (tool / 도구)/plugin có thể generate nguồn (source / 소스) từ lược đồ (schema / 스키마), localization, API description hoặc asset chuỗi xử lý (pipeline / 파이프라인). Generation phải deterministic: cùng đầu vào (input / 입력)/công cụ (tool / 도구) phiên bản (version / 버전) phải cho cùng đầu ra (output / 출력). CI cần pin generator/toolchain và thất bại (fail / 실패) nếu generated sản phẩm tạo ra (artifact / 산출물) drift khỏi source-of-truth chính sách (policy / 정책).

Generated mã (code / 코드) phù hợp boilerplate máy tạo; lô-gic nghiệp vụ (business logic / 비즈니스 로직) quan trọng nên vẫn reviewable. Một generator quá “thông minh” có thể khiến debugging và compile-time khó hơn mã (code / 코드) viết tay.

> **Nối mạch:** Deterministic build giúp telemetry có version trace; observability tiếp theo nối Logger/signpost/Instruments/MetricKit với memory graph để tìm retain cycle và cache growth.

## 11. khả năng quan sát (observability / 관측 가능성): Logger, signpost, Instruments và MetricKit

Logging trả lời “điều gì đã xảy ra”, chỉ số (metric / 지표) trả lời “xảy ra bao nhiêu/lâu thế nào”, dấu vết (trace / 추적)/signpost giúp nối luồng (flow / 흐름). `OSLog`/`Logger` nên dùng category/subsystem hợp lý và privacy annotation cho dữ liệu nhạy cảm.

`OSSignposter` hoặc signpost interval hữu ích khi đo luồng (flow / 흐름) như tap → fetch → decode → kết xuất (render / 렌더링). Instruments cho lab profiling; MetricKit và telemetry môi trường vận hành (production / 운영 환경) giúp nhìn crash/hang/launch/CPU-memory-responsiveness trên thiết bị (device / 장치) thật tùy chỉ số (metric / 지표) hỗ trợ.

Hiệu năng (performance / 성능) investigation nên có baseline và hypothesis. Không optimize theo trực giác hoặc chỉ nhìn một screenshot profiler.

> **Nối mạch:** Ở chặng này của **Swift & iOS — môi trường vận hành (production / 운영 환경) tham chiếu (reference / 참조) & Completion Guide**, **12. bộ nhớ (memory / 메모리) đồ thị (graph / 그래프): retain cycle và bộ nhớ đệm (cache / 캐시) growth** nối từ **11. khả năng quan sát (observability / 관측 가능성): Logger, signpost, Instruments và MetricKit** sang **13. App extension là tiến trình (process / 프로세스) ranh giới (boundary / 경계)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. bộ nhớ (memory / 메모리) đồ thị (graph / 그래프): retain cycle và bộ nhớ đệm (cache / 캐시) growth

Khi đối tượng (object / 객체) không deallocate, bộ nhớ (memory / 메모리) đồ thị (graph / 그래프) giúp truy gốc (root / 루트) strong tham chiếu (reference / 참조). dùng chung (common / 공통) nguồn (source / 소스) gồm timer/display link, observer legacy, delegate không weak, dịch vụ (service / 서비스) giữ callback, tác vụ (task / 작업) giữ đơn vị sở hữu (owner / 오너) hoặc bộ nhớ đệm (cache / 캐시) không có eviction.

`[weak self]` không chữa mọi bộ nhớ (memory / 메모리) growth. bộ nhớ đệm (cache / 캐시) giữ dữ liệu chủ đích cũng làm bộ nhớ (memory / 메모리) tăng nhưng không nhất thiết là leak. Cần phân biệt unbounded retention, bộ nhớ đệm (cache / 캐시) chính sách (policy / 정책) và temporary peak.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Swift & iOS — môi trường vận hành (production / 운영 환경) tham chiếu (reference / 참조) & Completion Guide**, **12. bộ nhớ (memory / 메모리) đồ thị (graph / 그래프): retain cycle và bộ nhớ đệm (cache / 캐시) growth** đặt tiêu chí; **13. App extension là tiến trình (process / 프로세스) ranh giới (boundary / 경계)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **14. Supply-chain bảo mật (security / 보안) của gói (package / 패키지) và SDK** mở rộng hệ quả.

## 13. App extension là tiến trình (process / 프로세스) ranh giới (boundary / 경계)

Widget, Share Extension, Notification dịch vụ (service / 서비스) Extension và main app không chia sẻ singleton/bộ nhớ (memory / 메모리) chỉ vì dùng chung mô-đun (module / 모듈). Chúng có tiến trình (process / 프로세스)/vòng đời (lifecycle / 생명주기)/tài nguyên (resource / 자원) ngân sách (budget / 예산) riêng. dữ liệu (data / 데이터) sharing cần App Group bộ chứa (container / 컨테이너), Keychain truy cập (access / 접근) group hoặc cơ chế (mechanism / 메커니즘) được nền tảng (platform / 플랫폼) hỗ trợ.

Do ngân sách (budget / 예산) chặt, extension nên tránh kéo phụ thuộc (dependency / 의존성) nặng nếu không cần. cốt lõi (core / 핵심) mô-đun (module / 모듈) dùng chung nên giữ nhẹ, còn SDK hoặc dịch vụ (service / 서비스) chỉ main app cần đặt ở composition tầng (layer / 계층) của app.

> **Nối mạch:** Trong **Swift & iOS — môi trường vận hành (production / 운영 환경) tham chiếu (reference / 참조) & Completion Guide**, **13. App extension là tiến trình (process / 프로세스) ranh giới (boundary / 경계)** đặt tiêu chí; **14. Supply-chain bảo mật (security / 보안) của gói (package / 패키지) và SDK** dùng tiêu chí đó để kiểm tra ranh giới, rồi **15. Make invalid states unrepresentable** mở rộng hệ quả.

## 14. Supply-chain bảo mật (security / 보안) của gói (package / 패키지) và SDK

Mỗi third-party gói (package / 패키지) mở rộng trust ranh giới (boundary / 경계). rà soát (review / 검토) không chỉ số star mà còn maintainer, provenance/quy trình phát hành (release process / 릴리스 프로세스), license, vulnerability lịch sử (history / 이력), privacy manifest, transitive phụ thuộc (dependency / 의존성) và khả năng exit.

Pin/resolved phiên bản (version / 버전) góp phần reproducible bản dựng (build / 빌드). Major cập nhật (update / 업데이트) không nên tự động ship mà không rà soát (review / 검토). Với SDK analytics/ads/auth/payment, privacy/bảo mật (security / 보안) rà soát (review / 검토) phải tương xứng lượng dữ liệu và quyền truy cập SDK có.

> **Nối mạch:** Ở chặng này của **Swift & iOS — môi trường vận hành (production / 운영 환경) tham chiếu (reference / 참조) & Completion Guide**, **15. Make invalid states unrepresentable** nối từ **14. Supply-chain bảo mật (security / 보안) của gói (package / 패키지) và SDK** sang **16. ADR và tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. Make invalid states unrepresentable

Hệ kiểu (type system / 타입 시스템) nên giúp loại bỏ trạng thái vô nghĩa. Một API nhận `String` chế độ (mode / 모드), optional thử lại (retry / 재시도) và optional đơn vị từ (token / 토큰) cho phép nhiều combination sai. Enum/giá trị (value / 값) đối tượng (object / 객체) có thể biến intent thành compile-time mô hình (model / 모델).

```swift
enum Authentication {
    case anonymous
    case bearer(Token)
}

struct RetryPolicy {
    let maximumAttempts: Int
}
```

Nhưng đừng wrapper mọi thành phần nguyên thủy (primitive / 기본 요소) vô điều kiện. Hãy tạo kiểu (type / 타입) khi nó mang bất biến (invariant / 불변식)/ngữ nghĩa (semantic / 의미적) đáng bảo vệ.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Swift & iOS — môi trường vận hành (production / 운영 환경) tham chiếu (reference / 참조) & Completion Guide**, **16. ADR và tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬)** nối từ **15. Make invalid states unrepresentable** sang **17. Disaster khôi phục (recovery / 복구) và mobile quay lui (rollback / 롤백)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. ADR và tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬)

Kiến trúc (architecture / 아키텍처) quyết định (decision / 결정) bản ghi (record / 레코드) (ADR) ghi ngữ cảnh (context / 맥락), quyết định, alternative và consequence cho quyết định đáng kể như minimum iOS phiên bản (version / 버전), SwiftData vs cốt lõi (core / 핵심) dữ liệu (data / 데이터), mô-đun (module / 모듈) chiến lược (strategy / 전략) hoặc thử lại (retry / 재시도) chính sách (policy / 정책). Mục tiêu là lưu *lý do*, không phải tạo tài liệu dài.

Nhóm (team / 팀) môi trường vận hành (production / 운영 환경) cũng nên có tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬): Xcode/toolchain được phép, Swift ngôn ngữ (language / 언어) chế độ (mode / 모드), minimum triển khai (deployment / 배포) mục tiêu (target / 대상), OS/thiết bị (device / 장치) kiểm thử (test / 테스트) set, backend tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우) và gói (package / 패키지) chính sách (policy / 정책). Encode phần quan trọng vào CI để tránh cục bộ (local / 로컬)/CI drift.

> **Nối mạch:** Trong **Swift & iOS — môi trường vận hành (production / 운영 환경) tham chiếu (reference / 참조) & Completion Guide**, **17. Disaster khôi phục (recovery / 복구) và mobile quay lui (rollback / 롤백)** nối từ **16. ADR và tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬)** sang **18. hiệu năng (performance / 성능) mô hình (model / 모델) từ thuật toán (algorithm / 알고리즘) đến frame ngân sách (budget / 예산)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. Disaster khôi phục (recovery / 복구) và mobile quay lui (rollback / 롤백)

Mobile nhị phân (binary / 이진) không quay lui (rollback / 롤백) tức thời. người dùng (user / 사용자) có thể giữ phiên bản (version / 버전) lỗi dù nhóm (team / 팀) đã phát hành hotfix. Do đó tính năng (feature / 기능) rủi ro nên có mitigation phù hợp: backend backward tính tương thích (compatibility / 호환성), remote kill switch/cờ tính năng (feature flag / 기능 플래그) nơi hợp lý, khả năng quan sát (observability / 관측 가능성) và di chuyển (migration / 마이그레이션) chiến lược (strategy / 전략) không phá dữ liệu.

Không phải mọi tính năng (feature / 기능) cần remote flag. Flag cũng tạo combinatorial độ phức tạp (complexity / 복잡도) và phải có đơn vị sở hữu (owner / 오너)/expiry. Rigor phải tỷ lệ với hậu quả khi tính năng (feature / 기능) sai.

> **Nối mạch:** Ở chặng này của **Swift & iOS — môi trường vận hành (production / 운영 환경) tham chiếu (reference / 참조) & Completion Guide**, **18. hiệu năng (performance / 성능) mô hình (model / 모델) từ thuật toán (algorithm / 알고리즘) đến frame ngân sách (budget / 예산)** nối từ **17. Disaster khôi phục (recovery / 복구) và mobile quay lui (rollback / 롤백)** sang **19. bảo mật (security / 보안) rà soát (review / 검토) theo luồng dữ liệu (data flow / 데이터 흐름)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. hiệu năng (performance / 성능) mô hình (model / 모델) từ thuật toán (algorithm / 알고리즘) đến frame ngân sách (budget / 예산)

Hiệu năng (performance / 성능) không có một bottleneck duy nhất. thuật toán (algorithm / 알고리즘) O(n²) có thể vô hại với 20 item nhưng nguy hiểm với 100.000. ảnh (image / 이미지) decode trên main luồng thực thi (thread / 스레드) có thể gây hitch dù thuật toán (algorithm / 알고리즘) O(n). cơ sở dữ liệu (database / 데이터베이스) thiếu chỉ mục (index / 인덱스) có thể chậm hơn mọi micro-optimization Swift.

Trước khi tối ưu, xác định tài nguyên (resource / 자원) giới hạn: CPU, GPU, bộ nhớ (memory / 메모리), I/O, mạng (network / 네트워크), tranh chấp khóa (lock contention / 잠금 경합), actor serialization hay main-thread công việc (work / 작업). Sau đó chọn công cụ đo tương ứng.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Swift & iOS — môi trường vận hành (production / 운영 환경) tham chiếu (reference / 참조) & Completion Guide**, **18. hiệu năng (performance / 성능) mô hình (model / 모델) từ thuật toán (algorithm / 알고리즘) đến frame ngân sách (budget / 예산)** đặt vấn đề; **19. bảo mật (security / 보안) rà soát (review / 검토) theo luồng dữ liệu (data flow / 데이터 흐름)** đối chiếu bằng chứng, rồi **20. kiểm thử (test / 테스트) bản phát hành (release / 릴리스) sản phẩm tạo ra (artifact / 산출물), không chỉ gỡ lỗi (debug / 디버그) nguồn (source / 소스)** mở rộng hệ quả hoặc giới hạn liên quan.

## 19. bảo mật (security / 보안) rà soát (review / 검토) theo luồng dữ liệu (data flow / 데이터 흐름)

Keychain chỉ bảo vệ một phần dữ liệu. bảo mật (security / 보안) rà soát (review / 검토) tốt vẽ luồng dữ liệu (data flow / 데이터 흐름): credential vào từ đâu, nằm bộ nhớ (memory / 메모리) bao lâu, có ghi disk/log không, yêu cầu (request / 요청) đi endpoint nào, extension/SDK nào đọc được, logout có xóa đúng không.

Threat mô hình (model / 모델) phải gắn asset và attacker: đơn vị từ (token / 토큰) theft, reverse kỹ thuật (engineering / 엔지니어링), MITM, compromised thiết bị (device / 장치) và unauthorized backend hành động (action / 동작) là threat khác nhau. máy khách (client / 클라이언트) hardening không thay backend authorization.

> **Nối mạch:** Trong **Swift & iOS — môi trường vận hành (production / 운영 환경) tham chiếu (reference / 참조) & Completion Guide**, cơ chế trong **19. bảo mật (security / 보안) rà soát (review / 검토) theo luồng dữ liệu (data flow / 데이터 흐름)** cần được kiểm chứng bằng dấu vết cụ thể; **20. kiểm thử (test / 테스트) bản phát hành (release / 릴리스) sản phẩm tạo ra (artifact / 산출물), không chỉ gỡ lỗi (debug / 디버그) nguồn (source / 소스)** đưa dữ liệu và nguồn vào đúng điểm đó. Từ đây, **21. Definition of Done theo rủi ro (risk / 위험)** mở rộng hệ quả hoặc giới hạn liên quan.

## 20. kiểm thử (test / 테스트) bản phát hành (release / 릴리스) sản phẩm tạo ra (artifact / 산출물), không chỉ gỡ lỗi (debug / 디버그) nguồn (source / 소스)

Đơn vị (unit / 단위) kiểm thử (test / 테스트) gỡ lỗi (debug / 디버그) Simulator xanh chưa đảm bảo archive bản phát hành (release / 릴리스) đúng. chuỗi xử lý (pipeline / 파이프라인) môi trường vận hành (production / 운영 환경) nên bản dựng (build / 빌드)/archive cấu hình (configuration / 구성) thật và kiểm entitlement/signing/tài nguyên (resource / 자원)/cấu hình (configuration / 구성). Khi khả thi, smoke kiểm thử (test / 테스트) sản phẩm tạo ra (artifact / 산출물) hoặc bản dựng (build / 빌드) gần bản phát hành (release / 릴리스) sản phẩm tạo ra (artifact / 산출물) trên thiết bị (device / 장치)/arm64.

Optimization-sensitive race, missing tài nguyên (resource / 자원), wrong môi trường (environment / 환경) endpoint, entitlement khác gỡ lỗi (debug / 디버그) hoặc gói (package / 패키지)/thiết bị (device / 장치) kiến trúc (architecture / 아키텍처) issue thường chỉ lộ gần bản phát hành (release / 릴리스).

> **Nối mạch:** Ở chặng này của **Swift & iOS — môi trường vận hành (production / 운영 환경) tham chiếu (reference / 참조) & Completion Guide**, **20. kiểm thử (test / 테스트) bản phát hành (release / 릴리스) sản phẩm tạo ra (artifact / 산출물), không chỉ gỡ lỗi (debug / 디버그) nguồn (source / 소스)** đặt vấn đề; **21. Definition of Done theo rủi ro (risk / 위험)** đối chiếu bằng chứng, rồi **22. Capstone kiểm tra (audit / 감사)** mở rộng hệ quả hoặc giới hạn liên quan.

## 21. Definition of Done theo rủi ro (risk / 위험)

Một tính năng (feature / 기능) môi trường vận hành (production / 운영 환경) hoàn thành khi hành vi (behavior / 동작) happy/lỗi (error / 오류)/cancel được định nghĩa, khả năng tiếp cận (accessibility / 접근성)/localization hợp lý, kiểm thử (test / 테스트) trọng yếu (critical / 중요) lô-gic (logic / 논리), availability/triển khai (deployment / 배포) mục tiêu (target / 대상) đúng, persistence/di chuyển (migration / 마이그레이션) impact được xem xét, telemetry đủ cho rủi ro (risk / 위험) và rollout chiến lược (strategy / 전략) phù hợp.

Definition of Done không nên nặng như nhau cho mọi tính năng (feature / 기능). Một cục bộ (local / 로컬) toggle và payment luồng (flow / 흐름) có hậu quả khác nhau. cấp cao (senior / 시니어)/master skill nằm ở việc quy mô (scale / 규모) rigor theo rủi ro (risk / 위험).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Swift & iOS — môi trường vận hành (production / 운영 환경) tham chiếu (reference / 참조) & Completion Guide**, **22. Capstone kiểm tra (audit / 감사)** nối từ **21. Definition of Done theo rủi ro (risk / 위험)** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## 22. Capstone kiểm tra (audit / 감사)

Để kiểm tra toàn bộ bộ ghi chú (note / 노트), hãy xây một app mẫu có login, feed phân trang, tìm kiếm (search / 검색) debounce, upload/download, cục bộ (local / 로컬) persistence, offline chế độ (mode / 모드), deep link, push notification, background công việc (work / 작업) và purchase giả lập. Với từng tính năng (feature / 기능), tự trả lời: nguồn chuẩn (source of truth / 정본) ở đâu; trạng thái (state / 상태) đơn vị sở hữu (owner / 오너) là ai; tác vụ (task / 작업) thời gian tồn tại (lifetime / 수명) là gì; actor isolation ở đâu; cancellation/thử lại (retry / 재시도) thế nào; di chuyển (migration / 마이그레이션) ra sao; backward tính tương thích (compatibility / 호환성) với backend thế nào; kiểm thử (test / 테스트) gì; chỉ số (metric / 지표) gì; và fallback ra sao khi API mới không tồn tại trên triển khai (deployment / 배포) mục tiêu (target / 대상) cũ.

Nếu có thể trả lời nhất quán mà không cần viện tên mẫu (pattern / 패턴) như một đáp án, bạn đã chuyển từ “biết Swift/iOS API” sang có khả năng quyền sở hữu (ownership / 소유권) một hệ thống iOS môi trường vận hành (production / 운영 환경).

> **Bàn giao:** Sau **22. Capstone kiểm tra (audit / 감사)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
