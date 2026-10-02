# Swift & iOS Master ghi chú (note / 노트) — Master

> **Mạch đọc:** [README](./README.md) là owner của **Swift & iOS Master ghi chú (note / 노트) — Master**; dùng nó để xác định đây là chặng kết thúc của lộ trình chuẩn. Đi từ **2.1 Swift 1–2** qua **2.2 Swift 3**, rồi nối lịch sử tiến hóa API với ABI/library evolution, macros, memory-safe systems, offline sync, extensions, StoreKit/CloudKit và release engineering; kết luận của mỗi giai đoạn phải quay về quyết định migration hoặc production ở giai đoạn sau.

> Mục tiêu: từ cấp cao (senior / 시니어) hiện thực (implementation / 구현) tiến tới mastery: hiểu **ngôn ngữ (language / 언어)/nền tảng (platform / 플랫폼) evolution**, di chuyển (migration / 마이그레이션) chiến lược (strategy / 전략), khung phần mềm (framework / 프레임워크)/API stability, phân tán (distributed / 분산) dữ liệu (data / 데이터) tính tương thích (compatibility / 호환성), hiệu năng (performance / 성능)/bảo mật (security / 보안) quản trị (governance / 거버넌스), bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링) và cách giữ một iOS hệ thống (system / 시스템) sống qua nhiều năm.
>
> Baseline cập nhật 21/09/2026: **Xcode 27 + Swift 6.4 + iOS 27 SDK**. Swift 6.4 phát hành chính thức 15/09/2026. Xcode 27.1/27.2 vẫn là beta tại thời điểm cập nhật nên không dùng làm stable baseline.

Master không dạy lại `@State`, actor hay UIKit vòng đời (lifecycle / 생명주기). Nó giả định bạn đã có thể vẽ quyền sở hữu (ownership / 소유권)/tác vụ (task / 작업)/isolation/trạng thái (state / 상태)/mô-đun (module / 모듈) đồ thị (graph / 그래프) từ Advanced và dùng các đồ thị (graph / 그래프) đó để đánh giá di chuyển (migration / 마이그레이션), tính tương thích (compatibility / 호환성) và môi trường vận hành (production / 운영 환경) rủi ro (risk / 위험).

---

# 1. Cách đọc phiên bản (version / 버전): trình biên dịch (compiler / 컴파일러), ngôn ngữ (language / 언어) chế độ (mode / 모드), SDK, OS và gói (package / 패키지) là các trục khác nhau

Một dự án (project / 프로젝트) có ít nhất các phiên bản (version / 버전) axis sau:

- Xcode/toolchain phiên bản (version / 버전);
- Swift trình biên dịch (compiler / 컴파일러) phiên bản (version / 버전);
- Swift ngôn ngữ (language / 언어) chế độ (mode / 모드)/tính năng (feature / 기능) settings;
- iOS SDK dùng lúc compile;
- minimum triển khai (deployment / 배포) mục tiêu (target / 대상);
- Swift gói (package / 패키지) tools/phụ thuộc (dependency / 의존성) versions;
- nhị phân (binary / 이진) SDK/khung phần mềm (framework / 프레임워크) versions;
- backend API/lược đồ (schema / 스키마) phiên bản (version / 버전);
- cục bộ (local / 로컬) persistence lược đồ (schema / 스키마) phiên bản (version / 버전).

“Dùng Swift 6.4” không tự động nghĩa app chỉ chạy iOS 27. “bản dựng (build / 빌드) bằng iOS 27 SDK” cũng không nghĩa được gọi mọi API iOS 27 trên thiết bị iOS 17 mà không availability check.

Phiên bản (version / 버전) debugging phải ghi đủ ngữ cảnh (context / 맥락). Bug report chỉ nói “Swift 6 lỗi” thường thiếu dữ liệu để reproduce.

---

# 2. Swift evolution — thay đổi cách lập trình, không phải danh sách bản phát hành (release / 릴리스) ghi chú (note / 노트)

## 2.1 Swift 1–2: ngôn ngữ mới, ecosystem còn biến động

Các đời đầu đặt nền cho Optional, giá trị (value / 값) types, protocol-oriented thiết kế (design / 설계) và an toàn (safety / 안전), nhưng cú pháp (syntax / 문법)/API thay đổi mạnh. mã (code / 코드) legacy từ thời này ít gặp trực tiếp hơn, nhưng lịch sử giải thích vì sao nhiều API wrapper/blog cũ không compile trên Swift hiện đại.

Bài học: nguồn (source / 소스) tính tương thích (compatibility / 호환성) chưa phải điều mặc định trong giai đoạn đầu; khi đọc mã (code / 코드) rất cũ, đừng cố “sửa từng cú pháp (syntax / 문법)” mà phải hiểu intent rồi map sang hiện đại (modern / 현대적) API.

> **Chuyển mạch:** Swift 1–2 còn ổn định language/ecosystem; Swift 3 chuẩn hóa API design và call-site readability, rồi Swift 4.x đưa Codable vào model boundary type-safe hơn.

## 2.2 Swift 3: API thiết kế (design / 설계) và call-site readability trở thành convention lớn

Swift 3 là bước chuẩn hóa naming/import style rất mạnh. Apple SDK Swift names được thiết kế lại theo API thiết kế (design / 설계) Guidelines, argument labels/call-site trở nên tự nhiên hơn.

Ảnh hưởng lâu dài: Swift mã (code / 코드) hiện đại coi API naming là một phần ngữ nghĩa (semantics / 의미론). hàm (function / 함수) không chỉ “tên + parameter”; lời gọi (call / 호출) site cần đọc rõ hành động và quan hệ (relation / 관계) giữa argument.

> **Chuyển mạch:** Ở chặng này của **Swift & iOS Master ghi chú (note / 노트) — Master**, **2.2 Swift 3: API thiết kế (design / 설계) và call-site readability trở thành convention lớn** đã nêu tiêu chí phân biệt, còn **2.3 Swift 4.x: Codable và mô hình (model / 모델) ranh giới (boundary / 경계) trở nên type-safe hơn** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **2.4 Swift 5.0: ABI stability thay đổi cách phân phối Swift app/khung phần mềm (framework / 프레임워크)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2.3 Swift 4.x: Codable và mô hình (model / 모델) ranh giới (boundary / 경계) trở nên type-safe hơn

`Codable` làm JSON/property-list ánh xạ (mapping / 매핑) phổ biến chuyển từ `[String: Any]`/manual cast sang compiler-checked mô hình (model / 모델). Key đường dẫn (path / 경로) và standard-library improvements tiếp tục khuyến khích strongly typed APIs.

Ảnh hưởng: vận chuyển (transport / 전송) mô hình (model / 모델) có thể được kiểu (type / 타입) hóa dễ hơn, nhưng “Codable được” không có nghĩa vận chuyển (transport / 전송) DTO nên trở thành lĩnh vực (domain / 도메인) mô hình (model / 모델). ranh giới (boundary / 경계) thiết kế (design / 설계) vẫn là kiến trúc (architecture / 아키텍처) concern.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Swift & iOS Master ghi chú (note / 노트) — Master**, **2.3 Swift 4.x: Codable và mô hình (model / 모델) ranh giới (boundary / 경계) trở nên type-safe hơn** đã nêu tiêu chí phân biệt, còn **2.4 Swift 5.0: ABI stability thay đổi cách phân phối Swift app/khung phần mềm (framework / 프레임워크)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **2.5 Swift 5.1 + SwiftUI era: opaque kiểu (type / 타입)/thuộc tính (property / 속성) wrapper/kết quả (result / 결과) builder thay đổi UI style** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2.4 Swift 5.0: ABI stability thay đổi cách phân phối Swift app/khung phần mềm (framework / 프레임워크)

ABI stability trên Apple platforms giảm nhu cầu bundle Swift thời gian chạy (runtime / 런타임) theo cách cũ và tạo nền tảng cho nhị phân (binary / 이진) ecosystem ổn định hơn. Đây không phải lời hứa rằng mọi Swift khung phần mềm (framework / 프레임워크) tự động binary-compatible vĩnh viễn.

Swift 5.x còn là thời kỳ nguồn (source / 소스) tính tương thích (compatibility / 호환성) tốt hơn, làm enterprise codebase có thể sống qua nhiều Xcode generation hơn.

> **Chuyển mạch:** ABI stability thay đổi distribution boundary; Swift 5.1 thêm opaque types/property wrappers/result builders, rồi iOS 13 ghép SwiftUI với Combine thành UI/data-flow stack.

## 2.5 Swift 5.1 + SwiftUI era: opaque kiểu (type / 타입)/thuộc tính (property / 속성) wrapper/kết quả (result / 결과) builder thay đổi UI style

`some View`, thuộc tính (property / 속성) wrappers và result-builder-style DSL tạo điều kiện cho SwiftUI. UI chuyển từ imperative đối tượng (object / 객체) mutation sang declarative state-driven description.

Ảnh hưởng kiến trúc (architecture / 아키텍처): định danh (identity / 식별자)/quyền sở hữu trạng thái (state ownership / 상태 소유권) trở nên quan trọng hơn view-object thời gian tồn tại (lifetime / 수명) kiểu UIKit. Nhưng UIKit không biến mất; hybrid kiến trúc (architecture / 아키텍처) trở thành skill môi trường vận hành (production / 운영 환경).

> **Chuyển mạch:** Ở chặng này của **Swift & iOS Master ghi chú (note / 노트) — Master**, **2.6 iOS 13 era: SwiftUI + Combine** tiếp nhận điểm tựa từ **2.5 Swift 5.1 + SwiftUI era: opaque kiểu (type / 타입)/thuộc tính (property / 속성) wrapper/kết quả (result / 결과) builder thay đổi UI style** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **2.7 Swift 5.5: async/await, structured tính đồng thời (concurrency / 동시성) và actor** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2.6 iOS 13 era: SwiftUI + Combine

SwiftUI và Combine đưa declarative UI/reactive stream vào Apple ecosystem. Nhiều codebase 2019–2022 có `ObservableObject`, `@Published`, `AnyPublisher`, `sink`, scheduler-heavy chuỗi xử lý (pipeline / 파이프라인).

Khi maintain mã (code / 코드) này, không cần rewrite chỉ vì async/await/Observation mới hơn. Xác định ranh giới (boundary / 경계) nào được hưởng lợi từ di chuyển (migration / 마이그레이션) và giữ hành vi (behavior / 동작)/kiểm thử (test / 테스트) trước.

> **Chuyển mạch:** SwiftUI/Combine đặt reactive UI baseline; Swift 5.5 thêm async/await, structured concurrency và actor, rồi 5.7–5.9 làm rõ existential, macros và Observation.

## 2.7 Swift 5.5: async/await, structured tính đồng thời (concurrency / 동시성) và actor

Đây là thay đổi programming mô hình (model / 모델) lớn. Callback pyramid và nhiều Combine use trường hợp (case / 사례) có alternative structured hơn. Actor đưa isolation vào ngôn ngữ (language / 언어) thay vì chỉ convention hàng đợi (queue / 큐)/khóa (lock / 잠금).

Ảnh hưởng: “thread-safe” dần chuyển thành “isolation/sendability correct”. Nhưng API callback/Combine/OperationQueue/GCD vẫn tồn tại ở khung phần mềm (framework / 프레임워크) legacy và cần cầu nối (bridge / 브리지) đúng.

> **Chuyển mạch:** Trong **Swift & iOS Master ghi chú (note / 노트) — Master**, **2.8 Swift 5.7–5.9: existential clarity, macros, Observation** tiếp nhận điểm tựa từ **2.7 Swift 5.5: async/await, structured tính đồng thời (concurrency / 동시성) và actor** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **2.9 Swift 6.0: data-race an toàn (safety / 안전) trở thành language-level di chuyển (migration / 마이그레이션)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2.8 Swift 5.7–5.9: existential clarity, macros, Observation

`any` làm existential intent rõ hơn; generic/opaque/existential sự đánh đổi (trade-off / 트레이드오프) dễ nói chính xác hơn. Macro mở compile-time mã (code / 코드) generation. Observation giảm boilerplate `ObservableObject/@Published` và nhánh học (track / 트랙) phụ thuộc (dependency / 의존성) granular hơn.

SwiftData xuất hiện ở iOS 17 era, giúp persistence Swift-native hơn nhưng không xóa cơ sở dữ liệu (database / 데이터베이스) fundamentals như lược đồ (schema / 스키마)/di chuyển (migration / 마이그레이션)/chỉ mục (index / 인덱스)/giao dịch (transaction / 트랜잭션).

> **Chuyển mạch:** Ở chặng này của **Swift & iOS Master ghi chú (note / 노트) — Master**, **2.9 Swift 6.0: data-race an toàn (safety / 안전) trở thành language-level di chuyển (migration / 마이그레이션)** tiếp nhận điểm tựa từ **2.8 Swift 5.7–5.9: existential clarity, macros, Observation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **2.10 Swift 6.2: approachable tính đồng thời (concurrency / 동시성) và safe các hệ thống (systems / 시스템들) direction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2.9 Swift 6.0: data-race an toàn (safety / 안전) trở thành language-level di chuyển (migration / 마이그레이션)

Swift 6 ngôn ngữ (language / 언어) chế độ (mode / 모드) đưa tính đồng thời (concurrency / 동시성) tính đúng đắn (correctness / 정확성) từ “warning/convention” tới compile-time guarantee mạnh hơn. `Sendable`, actor isolation, toàn cục (global / 전역) actor và closure sendability trở thành Đặc tả API (API contract / API 계약) thực sự.

Typed throws và Synchronization/tooling tiếp tục mở rộng khả năng express đặc tả hợp đồng (contract / 계약).

Ảnh hưởng lớn nhất: API thư viện (library / 라이브러리) giờ phải nghĩ đến isolation/sendability như công khai (public / 공개) surface, không thể coi tính đồng thời (concurrency / 동시성) là hiện thực (implementation / 구현) detail hoàn toàn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Swift & iOS Master ghi chú (note / 노트) — Master**, **2.10 Swift 6.2: approachable tính đồng thời (concurrency / 동시성) và safe các hệ thống (systems / 시스템들) direction** tiếp nhận điểm tựa từ **2.9 Swift 6.0: data-race an toàn (safety / 안전) trở thành language-level di chuyển (migration / 마이그레이션)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **2.11 Swift 6.4: quyền sở hữu (ownership / 소유권), bản dựng (build / 빌드) và cross-platform maturity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2.10 Swift 6.2: approachable tính đồng thời (concurrency / 동시성) và safe các hệ thống (systems / 시스템들) direction

Swift 6.2 làm tính đồng thời (concurrency / 동시성) dễ tiếp cận hơn qua default isolation/cấu hình (configuration / 구성) và tường minh (explicit / 명시적) concurrent thực thi (execution / 실행) intent, đồng thời phát triển `Span`, `InlineArray` và memory-safety tooling.

Ảnh hưởng: mô hình tư duy (mental model / 사고 모델) “mọi async hàm (function / 함수) tự chạy background” càng không còn đúng. Sequential/isolation-first mã (code / 코드) là default hợp lý; tính đồng thời (concurrency / 동시성) được opt-in ở nơi có lợi.

> **Chuyển mạch:** Trong **Swift & iOS Master ghi chú (note / 노트) — Master**, sau nội dung của **2.10 Swift 6.2: approachable tính đồng thời (concurrency / 동시성) và safe các hệ thống (systems / 시스템들) direction**, **2.11 Swift 6.4: quyền sở hữu (ownership / 소유권), bản dựng (build / 빌드) và cross-platform maturity** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **6.1 Inventory** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2.11 Swift 6.4: quyền sở hữu (ownership / 소유권), bản dựng (build / 빌드) và cross-platform maturity

Swift 6.4 là stable baseline hiện tại. Những thay đổi đáng chú ý ở mức direction:

- Swift bản dựng (build / 빌드) trở thành hệ thống dựng (build system / 빌드 시스템) mặc định của SwiftPM;
- quyền sở hữu (ownership / 소유권)/memory-safe hiệu năng (performance / 성능) APIs mở rộng với `Ref`, `MutableRef`, `UniqueBox`, `UniqueArray`, `Iterable` và safe raw-memory truy cập (access / 접근);
- `Span` interop với C++20 `std::span` sâu hơn;
- Observation/testing/gỡ lỗi (debug / 디버그) tooling tiếp tục cải thiện;
- Swift tiếp tục mở rộng Android, WebAssembly, Embedded và máy chủ (server / 서버)/tooling use cases.

Đối với iOS app, không cần thay `Array` bằng `UniqueArray` hay dùng các hệ thống (systems / 시스템들) API chỉ vì mới. Điều cần hiểu là Swift đang dịch chuyển về compile-time quyền sở hữu (ownership / 소유권)/an toàn (safety / 안전) mạnh hơn và bản dựng (build / 빌드)/tooling thống nhất hơn.

---

# 3. UIKit → SwiftUI evolution — vì sao hai mô hình tư duy (mental model / 사고 모델) cùng tồn tại

UIKit dùng đối tượng (object / 객체)/vòng đời (lifecycle / 생명주기)/delegate/target-action/Auto bố cục (layout / 레이아웃). SwiftUI dùng giá trị (value / 값) description/trạng thái (state / 상태)/định danh (identity / 식별자)/phụ thuộc (dependency / 의존성) tracking.

Không có một ngày “UIKit hết hạn”. Nhiều khung phần mềm (framework / 프레임워크) hệ thống (system / 시스템) vẫn expose UIKit/UIViewController mẫu (pattern / 패턴) hoặc API thấp tầng dễ cầu nối (bridge / 브리지) qua representable. môi trường vận hành (production / 운영 환경) di chuyển (migration / 마이그레이션) nên chọn seam, không chọn ideology.

Mốc nền tảng (platform / 플랫폼) đáng nhớ theo ảnh hưởng lập trình:

- SwiftUI/Combine era: declarative/reactive bắt đầu;
- SwiftUI App/Scene vòng đời (lifecycle / 생명주기): app entry/vòng đời (lifecycle / 생명주기) có declarative surface mới;
- NavigationStack era: tuyến (route / 경로)/state-driven điều hướng (navigation / 내비게이션) thay dần `NavigationView` cho app hiện đại;
- Observation/SwiftData era: trạng thái (state / 상태)/persistence Swift-native hơn;
- Xcode 27/iOS 27: trạng thái (state / 상태)/builder internals, caching/data-flow/tooling tiếp tục tiến hóa.

Mỗi lần nâng khung phần mềm (framework / 프레임워크), regression kiểm thử (test / 테스트) phải tập trung định danh (identity / 식별자)/thời gian tồn tại (lifetime / 수명)/điều hướng (navigation / 내비게이션)/focus/khả năng tiếp cận (accessibility / 접근성) hơn là chỉ compile success.

---

# 4. phiên bản (version / 버전) hỗ trợ (support / 지원) chính sách (policy / 정책) — trước khi viết mã (code / 코드) mới

Mỗi sản phẩm (product / 제품) nên có chính sách (policy / 정책) rõ:

- minimum iOS phiên bản (version / 버전);
- Xcode phiên bản (version / 버전) dùng ở CI/bản phát hành (release / 릴리스);
- Swift ngôn ngữ (language / 언어) chế độ (mode / 모드);
- gói (package / 패키지) cập nhật (update / 업데이트) cadence;
- khoảng backend backward-compatibility;
- số cục bộ (local / 로컬) lược đồ (schema / 스키마) phiên bản (version / 버전) phải hỗ trợ di chuyển (migration / 마이그레이션);
- thời gian app phiên bản (version / 버전) cũ còn được backend hỗ trợ.

Không có chính sách (policy / 정책) thì mỗi engineer tự quyết và tính tương thích (compatibility / 호환성) debt tích lũy âm thầm.

---

# 5. Availability chiến lược (strategy / 전략)

Thời gian chạy (runtime / 런타임) API:

```swift
if #available(iOS 27, *) {
    useNewAPI()
} else {
    useFallback()
}
```

Compile-time nguồn (source / 소스)/nền tảng (platform / 플랫폼):

```swift
#if canImport(UIKit)
import UIKit
#endif
```

Công khai (public / 공개) khung phần mềm (framework / 프레임워크) API có thể dùng `@available` để encode yêu cầu (requirement / 요구사항)/deprecation vào trình biên dịch (compiler / 컴파일러).

Đừng tạo fallback chỉ để “hỗ trợ (support / 지원) phiên bản (version / 버전) cũ” nếu fallback ngữ nghĩa (semantics / 의미론) sai. Đôi khi đúng hơn là disable tính năng (feature / 기능) với UX rõ hoặc nâng triển khai (deployment / 배포) mục tiêu (target / 대상) sau sản phẩm (product / 제품) phân tích (analysis / 분석).

---

# 6. di chuyển (migration / 마이그레이션) Swift 5 → Swift 6.x — ownership-first workflow

Di chuyển (migration / 마이그레이션) tính đồng thời (concurrency / 동시성) tốt không bắt đầu bằng fix trình biên dịch (compiler / 컴파일러) warning ngẫu nhiên.

> **Chuyển mạch:** Ở chặng này của **Swift & iOS Master ghi chú (note / 노트) — Master**, **6.1 Inventory** tiếp nhận điểm tựa từ **2.11 Swift 6.4: quyền sở hữu (ownership / 소유권), bản dựng (build / 빌드) và cross-platform maturity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6.2 Move ranh giới (boundary / 경계) theo batch** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6.1 Inventory

Lập bản đồ:

- toàn cục (global / 전역)/singleton mutable trạng thái (state / 상태);
- UI mô hình (model / 모델)/controller isolation;
- callback/delegate crossing hàng đợi (queue / 큐);
- non-Sendable SDK kiểu (type / 타입);
- closure lưu lâu;
- cơ sở dữ liệu (database / 데이터베이스) ngữ cảnh (context / 맥락)/đối tượng (object / 객체) ranh giới (boundary / 경계);
- GCD/OperationQueue/Combine chuỗi xử lý (pipeline / 파이프라인);
- kiểm thử (test / 테스트) phụ thuộc timing.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Swift & iOS Master ghi chú (note / 노트) — Master**, **6.1 Inventory** đã nêu tiêu chí phân biệt, còn **6.2 Move ranh giới (boundary / 경계) theo batch** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **6.3 Không dùng escape hatch như di chuyển (migration / 마이그레이션) chiến lược (strategy / 전략)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6.2 Move ranh giới (boundary / 경계) theo batch

Migrate mô-đun (module / 모듈)/tính năng (feature / 기능) có kiểm thử (test / 테스트) trước. Giữ lần ghi nhận (commit / 커밋) nhỏ đủ bisect. Khi annotation thay đổi thực thi (execution / 실행) ngữ nghĩa (semantics / 의미론)/thời gian tồn tại (lifetime / 수명), thêm regression kiểm thử (test / 테스트).

> **Chuyển mạch:** Trong **Swift & iOS Master ghi chú (note / 노트) — Master**, **6.2 Move ranh giới (boundary / 경계) theo batch** đã nêu tiêu chí phân biệt, còn **6.3 Không dùng escape hatch như di chuyển (migration / 마이그레이션) chiến lược (strategy / 전략)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **6.4 cầu nối (bridge / 브리지) legacy thay vì rewrite đồng loạt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6.3 Không dùng escape hatch như di chuyển (migration / 마이그레이션) chiến lược (strategy / 전략)

`@unchecked Sendable`, `nonisolated(unsafe)` hoặc toàn cục (global / 전역) `@MainActor` có thể hữu ích ở ranh giới (boundary / 경계) được chứng minh, nhưng nếu dùng để silence trình biên dịch (compiler / 컴파일러) hàng loạt, bạn đã xóa an toàn (safety / 안전) mà di chuyển (migration / 마이그레이션) định đạt được.

> **Chuyển mạch:** Ở chặng này của **Swift & iOS Master ghi chú (note / 노트) — Master**, **6.4 cầu nối (bridge / 브리지) legacy thay vì rewrite đồng loạt** tiếp nhận điểm tựa từ **6.3 Không dùng escape hatch như di chuyển (migration / 마이그레이션) chiến lược (strategy / 전략)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 6.4 cầu nối (bridge / 브리지) legacy thay vì rewrite đồng loạt

Callback → continuation, Combine → async chuỗi (sequence / 시퀀스), GCD-protected store → actor có thể migrate từng seam. Giữ cầu nối (bridge / 브리지) ở ranh giới (boundary / 경계) và xóa khi bên tiêu thụ (consumer / 소비자) mới đã ổn định.

---

# 7. API/thư viện (library / 라이브러리) evolution và nguồn (source / 소스)/nhị phân (binary / 이진) tính tương thích (compatibility / 호환성)

API công khai (public API / 공개 API) là commitment. khung phần mềm (framework / 프레임워크)/gói (package / 패키지) sống lâu phải cân nhắc:

- nguồn (source / 소스) tính tương thích (compatibility / 호환성);
- ngữ nghĩa (semantic / 의미적) tính tương thích (compatibility / 호환성);
- nhị phân (binary / 이진)/mô-đun (module / 모듈) tính tương thích (compatibility / 호환성) nếu phân phối nhị phân (binary / 이진);
- actor/isolation/sendability đặc tả hợp đồng (contract / 계약);
- availability;
- deprecation cửa sổ (window / 윈도우).

ABI stability của Swift thời gian chạy (runtime / 런타임) trên Apple nền tảng (platform / 플랫폼) không tự động làm mọi nhị phân (binary / 이진) khung phần mềm (framework / 프레임워크) future-proof.

Mô-đun (module / 모듈) stability/thư viện (library / 라이브러리) evolution/`.swiftinterface` liên quan bên tiêu thụ (consumer / 소비자) trình biên dịch (compiler / 컴파일러) khác phiên bản (version / 버전). `@frozen` khóa một phần bố cục (layout / 레이아웃)/evolution của công khai (public / 공개) kiểu (type / 타입); dùng sai làm future thay đổi (change / 변경) khó hơn.

SPI/underscored API không nên bị bên tiêu thụ (consumer / 소비자) coi như công khai (public / 공개) stable đặc tả hợp đồng (contract / 계약).

---

# 8. ngữ nghĩa (semantic / 의미적) versioning nội bộ và deprecation

Ngay cả gói (package / 패키지) chỉ dùng nội bộ cũng cần phiên bản (version / 버전)/thay đổi (change / 변경) discipline nếu nhiều mô-đun (module / 모듈)/nhóm (team / 팀) consume.

Breaking thay đổi (change / 변경) có thể:

1. thêm API mới;
2. deprecate API cũ với di chuyển (migration / 마이그레이션) message;
3. migrate bên tiêu thụ (consumer / 소비자);
4. xóa sau cửa sổ (window / 윈도우) đã thống nhất.

```swift
@available(*, deprecated, message: "Use load(request:) instead")
func loadLegacy() { }
```

Đừng giữ tính tương thích (compatibility / 호환성) shim vô hạn; mỗi shim là branch cần kiểm thử (test / 테스트).

---

# 9. Macros và generated mã (code / 코드) quản trị (governance / 거버넌스)

Macro giảm boilerplate nhưng thêm trình biên dịch (compiler / 컴파일러) plugin/tooling phụ thuộc (dependency / 의존성) và generated mã (code / 코드) không thấy trực tiếp ở nguồn (source / 소스).

Môi trường vận hành (production / 운영 환경) checklist:

- expansion có deterministic không;
- diagnostic có readable không;
- compile-time chi phí (cost / 비용) có đo không;
- API công khai (public API / 공개 API) generated có stable không;
- bảo mật (security / 보안)/supply-chain của macro gói (package / 패키지) có được rà soát (review / 검토) không;
- nhà phát triển (developer / 개발자) có biết xem expansion khi gỡ lỗi (debug / 디버그) không.

Nếu ordinary generic/hàm (function / 함수) đủ rõ, macro không nhất thiết tốt hơn.

---

# 10. quyền sở hữu (ownership / 소유권)/memory-safe các hệ thống (systems / 시스템들) ranh giới (boundary / 경계)

Unsafe API chỉ nên nằm ở adapter nhỏ với bất biến (invariant / 불변식) rõ. Với nhị phân (binary / 이진) parser/C/C++ interop:

- validate bounds/alignment;
- document thời gian tồn tại (lifetime / 수명)/quyền sở hữu (ownership / 소유권);
- convert sang Swift-safe biểu diễn (representation / 표현) sớm;
- fuzz untrusted đầu vào (input / 입력);
- bật an toàn (safety / 안전) diagnostics phù hợp.

Swift 6.4 thêm nhiều safe alternative cho use trường hợp (case / 사례) trước đây cần pointer/CoW workaround. Adoption nên theo benchmark và tài nguyên (resource / 자원) ngữ nghĩa (semantics / 의미론), không theo novelty.

---

# 11. dữ liệu (data / 데이터) kiến trúc (architecture / 아키텍처) — nguồn chuẩn (source of truth / 정본) theo loại dữ liệu

Phân biệt:

- presentation/view trạng thái (state / 상태);
- tính năng (feature / 기능) workflow trạng thái (state / 상태);
- lĩnh vực (domain / 도메인) trạng thái (state / 상태);
- cục bộ (local / 로컬) persisted trạng thái (state / 상태);
- máy chủ (server / 서버) authoritative trạng thái (state / 상태);
- bộ nhớ đệm (cache / 캐시);
- derived trạng thái (state / 상태).

“Single nguồn chuẩn (source of truth / 정본)” không có nghĩa toàn app có một toàn cục (global / 전역) store. Nó nghĩa mỗi fact biết authoritative đơn vị sở hữu (owner / 오너) và synchronization quy tắc (rule / 규칙).

Ví dụ, `isFavorite` có thể authoritative ở máy chủ (server / 서버), mirrored cục bộ (local / 로컬) để offline, optimistic UI tạm thời. Ba biểu diễn (representation / 표현) tồn tại nhưng phải có reconciliation chính sách (policy / 정책) rõ.

---

# 12. Persistence lược đồ (schema / 스키마) là công khai (public / 공개) đặc tả hợp đồng (contract / 계약) với dữ liệu người dùng (user / 사용자)

App nhị phân (binary / 이진) có thể quay lui (rollback / 롤백) không dễ, nhưng người dùng (user / 사용자) cơ sở dữ liệu (database / 데이터베이스) phải upgrade forward đáng tin.

Di chuyển (migration / 마이그레이션) chiến lược (strategy / 전략) cần kiểm thử (test / 테스트):

- fresh install;
- N-1 → N;
- các phiên bản (version / 버전) cũ còn thực tế ngoài trường dữ liệu (field / 필드) → N;
- interrupted/crash giữa di chuyển (migration / 마이그레이션) nếu khung phần mềm (framework / 프레임워크)/store có rủi ro (risk / 위험);
- account logout/login;
- corrupted/partial dữ liệu (data / 데이터) chính sách (policy / 정책);
- large real-world dataset hiệu năng (performance / 성능).

SwiftData/cốt lõi (core / 핵심) dữ liệu (data / 데이터) lớp trừu tượng (abstraction / 추상화) không loại bỏ yêu cầu (requirement / 요구사항) này.

---

# 13. cốt lõi (core / 핵심) dữ liệu (data / 데이터)/SwiftData context-isolation mastery

Managed/persisted đối tượng (object / 객체) có ngữ cảnh (context / 맥락)/model-container thời gian tồn tại (lifetime / 수명). Không xem nó như Sendable lĩnh vực (domain / 도메인) DTO tùy ý.

Cross-boundary mẫu (pattern / 패턴) thường tốt hơn:

```text
DB context/model actor
      ↓ map
Sendable immutable snapshot/domain value
      ↓
feature/UI actor
```

Nếu UI cần live observation trực tiếp từ persistence, ranh giới (boundary / 경계) có thể khác nhưng quyền sở hữu (ownership / 소유권)/ngữ cảnh (context / 맥락) quy tắc (rule / 규칙) vẫn phải rõ.

Chỉ mục (index / 인덱스)/truy vấn (query / 쿼리)/predicate shape thường ảnh hưởng hiệu năng (performance / 성능) lớn hơn việc “chạy background” một truy vấn (query / 쿼리) xấu.

---

# 14. Offline-first là sync hệ thống (system / 시스템), không phải bộ nhớ đệm (cache / 캐시)

Một offline-first engine thực sự thường cần:

- durable cục bộ (local / 로컬) nguồn (source / 소스);
- outbox/pending operations;
- idempotency key;
- thử lại (retry / 재시도)/backoff;
- sync cursor/phiên bản (version / 버전);
- giải quyết xung đột (conflict resolution / 충돌 해결);
- tombstone/delete ngữ nghĩa (semantics / 의미론);
- auth/account dữ liệu (data / 데이터) isolation;
- clock-skew awareness;
- khả năng quan sát (observability / 관측 가능성) cho stuck sync.

Last-write-wins chỉ là một xung đột (conflict / 충돌) chính sách (policy / 정책), không phải default đúng cho mọi lĩnh vực (domain / 도메인).

---

# 15. Mobile API tính tương thích (compatibility / 호환성) là phân tán (distributed / 분산) các hệ thống (systems / 시스템들) bài toán (problem / 문제)

Tại cùng một thời điểm có thể tồn tại:

```text
backend N
app N
app N-1
app N-3 offline nhiều ngày
local schema cũ
cache cũ
feature flags khác nhau
```

Máy chủ (server / 서버) phải giữ tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우). máy khách (client / 클라이언트) nên tolerant với additive trường dữ liệu (field / 필드)/enum evolution nếu đặc tả hợp đồng (contract / 계약) yêu cầu. Breaking ngữ nghĩa (semantic / 의미적) thay đổi (change / 변경) cần versioned endpoint/tính năng (feature / 기능) negotiation/di chuyển (migration / 마이그레이션) chiến lược (strategy / 전략) phù hợp.

Không bản phát hành (release / 릴리스) backend và app theo giả định mọi người dùng (user / 사용자) cập nhật đồng thời.

---

# 16. HTTP ngữ nghĩa (semantics / 의미론) và resilience

Thử lại (retry / 재시도) chính sách (policy / 정책) phải dựa trên thao tác (operation / 연산) ngữ nghĩa (semantics / 의미론).

GET/read thường dễ thử lại (retry / 재시도) hơn mutation. POST/payment/thứ tự (order / 순서) có thể đã được máy chủ (server / 서버) lần ghi nhận (commit / 커밋) trước khi máy khách (client / 클라이언트) hết thời gian chờ (timeout / 타임아웃); thử lại (retry / 재시도) mù có thể duplicate side tác động (effect / 효과).

Môi trường vận hành (production / 운영 환경) máy khách (client / 클라이언트) cần nghĩ đến:

- connect/yêu cầu (request / 요청)/tài nguyên (resource / 자원) hết thời gian chờ (timeout / 타임아웃);
- cancellation;
- `Retry-After`;
- 401 refresh single-flight;
- 429/tỷ lệ (rate / 비율) limit;
- idempotency key;
- exponential backoff + jitter;
- bộ nhớ đệm (cache / 캐시) kiểm tra hợp lệ (validation / 검증);
- offline/poor connectivity;
- background transfer.

Reachability không nên được dùng như oracle “yêu cầu (request / 요청) chắc chắn sẽ thành công”. mạng (network / 네트워크) trạng thái (state / 상태) có thể đổi giữa check và yêu cầu (request / 요청).

---

# 17. Background URLSession và recoverable workflow

Nếu download/upload cần tiếp tục khi app bị suspend/terminated theo hệ thống (system / 시스템) chính sách (policy / 정책), background `URLSession` là thành phần nguyên thủy (primitive / 기본 요소) phù hợp hơn giữ `Task` trong tiến trình (process / 프로세스).

Workflow cần persist identifier/trạng thái (state / 상태) đủ để tiến trình (process / 프로세스) mới reconnect/reconcile kết quả (result / 결과). Memory-only progress mô hình (model / 모델) không đủ cho thao tác (operation / 연산) sống qua tiến trình (process / 프로세스) death.

---

# 18. kiến trúc (architecture / 아키텍처) mastery — phụ thuộc (dependency / 의존성) quy tắc (rule / 규칙) theo volatility

Kiến trúc (architecture / 아키텍처) không phải số tầng (layer / 계층). ranh giới (boundary / 경계) nên bảo vệ phần ổn định khỏi phần biến động:

- lĩnh vực (domain / 도메인) quy tắc (rule / 규칙) khỏi REST lược đồ (schema / 스키마);
- tính năng (feature / 기능) trạng thái (state / 상태) khỏi concrete cơ sở dữ liệu (database / 데이터베이스);
- UI khỏi third-party SDK;
- mô-đun (module / 모듈) bên tiêu thụ (consumer / 소비자) khỏi hiện thực (implementation / 구현) helper;
- sản phẩm (product / 제품) hành vi (behavior / 동작) khỏi analytics vendor.

Nếu một SDK thay đổi làm 50 tệp (file / 파일) tính năng (feature / 기능) sửa trực tiếp, SDK kiểu (type / 타입) đã leak quá sâu.

---

# 19. Anti-corruption adapter tại khung phần mềm (framework / 프레임워크)/SDK ranh giới (boundary / 경계)

Third-party payment/analytics/map SDK nên được wrap khi API/kiểu (type / 타입) của nó không nên trở thành lĩnh vực (domain / 도메인) đặc tả hợp đồng (contract / 계약).

Adapter không phải wrapper 1:1 vô nghĩa. Nó map ngữ nghĩa (semantic / 의미적): lĩnh vực (domain / 도메인) sự kiện (event / 이벤트) → vendor lời gọi (call / 호출), vendor kết quả (result / 결과) → lĩnh vực (domain / 도메인) kết quả (result / 결과), và giữ vendor vòng đời (lifecycle / 생명주기)/cấu hình (config / 설정) ở một ranh giới (boundary / 경계).

Điều này tạo exit chiến lược (strategy / 전략) khi vendor thay đổi.

---

# 20. Large-scale modular kiến trúc (architecture / 아키텍처)

Ranh giới mô-đun (module boundary / 모듈 경계) nên cân bằng:

- cohesion;
- bản dựng (build / 빌드) hiệu năng (performance / 성능);
- nhóm (team / 팀) quyền sở hữu (ownership / 소유권);
- testability;
- API công khai (public API / 공개 API) kích thước (size / 크기);
- phụ thuộc (dependency / 의존성) fan-in/fan-out.

Micro-module hóa quá mức tạo gói (package / 패키지) đồ thị (graph / 그래프) phức tạp; mega-module làm mọi thay đổi recompile/ripple. Đo bản dựng (build / 빌드) đồ thị (graph / 그래프) và thay đổi (change / 변경) mẫu (pattern / 패턴) thật.

Kiến trúc (architecture / 아키텍처) quyết định (decision / 결정) bản ghi (record / 레코드) (ADR) hữu ích cho quyết định khó đảo: persistence engine, điều hướng (navigation / 내비게이션) quyền sở hữu (ownership / 소유권), minimum OS, sync chiến lược (strategy / 전략), key bảo mật (security / 보안) chính sách (policy / 정책), modular ranh giới (boundary / 경계).

ADR tốt ghi ngữ cảnh (context / 맥락), alternatives, quyết định (decision / 결정), consequence và trigger để revisit — không phải tài liệu marketing.

---

# 21. thiết kế (design / 설계) hệ thống (system / 시스템) là sản phẩm (product / 제품) API

Thiết kế (design / 설계) hệ thống (system / 시스템) gồm đơn vị từ (token / 토큰), typography, spacing, components, tương tác (interaction / 상호작용) states, khả năng tiếp cận (accessibility / 접근성), localization và theming.

Thành phần (component / 컴포넌트) API nên ngữ nghĩa (semantic / 의미적):

```swift
PrimaryButton(role: .destructive, size: .compact)
```

thay vì nhiều Boolean khó tạo combination hợp lệ.

Thiết kế (design / 설계) hệ thống (system / 시스템) versioning cũng là API evolution: thành phần (component / 컴포넌트) hành vi (behavior / 동작) thay đổi (change / 변경) có thể affect hàng chục tính năng (feature / 기능) và snapshot/khả năng tiếp cận (accessibility / 접근성) kiểm thử (test / 테스트).

---

# 22. khả năng quan sát (observability / 관측 가능성) — từ log đến trường dữ liệu (field / 필드) diagnosis

Ba lớp:

- log: sự kiện (event / 이벤트)/ngữ cảnh (context / 맥락) cục bộ;
- chỉ số (metric / 지표): aggregate trend;
- dấu vết (trace / 추적)/signpost: duration/luồng (flow / 흐름) qua thao tác (operation / 연산).

Mobile-specific tín hiệu (signal / 신호) gồm crash, nonfatal, launch/hang, frame hitch, bộ nhớ (memory / 메모리) footprint, năng lượng (energy / 에너지), mạng (network / 네트워크) độ trễ (latency / 지연 시간)/lỗi (error / 오류), DB độ trễ (latency / 지연 시간) và sync backlog.

Telemetry cần privacy minimization, sampling và stable sự kiện (event / 이벤트) lược đồ (schema / 스키마). Nếu bản phát hành (release / 릴리스) N đổi tên mọi sự kiện (event / 이벤트), so sánh trước/sau bản phát hành (release / 릴리스) khó hơn.

---

# 23. Symbolication và bản phát hành (release / 릴리스) sản phẩm tạo ra (artifact / 산출물) traceability

Crash ngăn xếp (stack / 스택) chỉ hữu ích khi symbolicate đúng bản dựng (build / 빌드). Mỗi bản phát hành (release / 릴리스) cần giữ ánh xạ (mapping / 매핑) giữa:

- app phiên bản (version / 버전)/bản dựng (build / 빌드);
- lần ghi nhận (commit / 커밋) SHA;
- Xcode/toolchain;
- archive;
- dSYM/symbol sản phẩm tạo ra (artifact / 산출물);
- cờ tính năng (feature flag / 기능 플래그)/cấu hình (config / 설정) phiên bản (version / 버전) nếu có.

“Không reproduce được” thường trở nên dễ hơn khi trường dữ liệu (field / 필드) report có đủ sản phẩm tạo ra (artifact / 산출물) định danh (identity / 식별자).

---

# 24. hiệu năng (performance / 성능) kỹ thuật (engineering / 엔지니어링) — ngân sách (budget / 예산) trước micro-optimization

Đặt SLO/ngân sách (budget / 예산) phù hợp sản phẩm (product / 제품):

- cold/warm launch;
- bộ nhớ (memory / 메모리) peak/steady trạng thái (state / 상태);
- scrolling hitch/frame thời gian (time / 시간);
- ảnh (image / 이미지) decode;
- yêu cầu (request / 요청) độ trễ (latency / 지연 시간);
- DB truy vấn (query / 쿼리);
- sync thông lượng (throughput / 처리량);
- năng lượng (energy / 에너지)/background wakeup;
- nhị phân (binary / 이진) kích thước (size / 크기);
- bản dựng (build / 빌드) thời gian (time / 시간).

Tối ưu hóa (optimization / 최적화) workflow: measure → hypothesis → thay đổi (change / 변경) → remeasure. Không chọn `struct`/`final`/manual bộ nhớ đệm (cache / 캐시) chỉ vì “nghe nhanh hơn” nếu bottleneck nằm ở mạng (network / 네트워크)/ảnh (image / 이미지)/bố cục (layout / 레이아웃).

---

# 25. Launch hiệu năng (performance / 성능)

Startup đường găng (critical path / 임계 경로) phải nhỏ. Tránh synchronous DB di chuyển (migration / 마이그레이션)/mạng (network / 네트워크)/SDK initialization hàng loạt trên main actor trước first meaningful UI.

Có thể lazy/defer noncritical dịch vụ (service / 서비스), nhưng deferred công việc (work / 작업) vẫn cần đơn vị sở hữu (owner / 오너) và lỗi (error / 오류) handling. Đừng biến “defer” thành tác vụ (task / 작업) storm ngay sau first frame.

Toàn cục (global / 전역)/static initializer có thể làm công việc (work / 작업) sớm ngoài ý định; profile launch ngăn xếp (stack / 스택) để thấy sự thật.

---

# 26. bộ nhớ (memory / 메모리) pressure và bộ nhớ đệm (cache / 캐시) economics

iOS có thể terminate tiến trình (process / 프로세스) khi bộ nhớ (memory / 메모리) pressure. bộ nhớ đệm (cache / 캐시) phải có eviction/kích thước (size / 크기) chính sách (policy / 정책); decoded ảnh (image / 이미지) có thể lớn hơn tệp (file / 파일) compressed rất nhiều.

`NSCache` phù hợp cho nhiều in-memory bộ nhớ đệm (cache / 캐시) use trường hợp (case / 사례) vì có eviction hành vi (behavior / 동작), nhưng không phải persistence/nguồn chuẩn (source of truth / 정본).

Downsample ảnh theo display mục tiêu (target / 대상), cancel decode/prefetch không còn cần và profile resident bộ nhớ (memory / 메모리) trên thiết bị (device / 장치).

---

# 27. năng lượng (energy / 에너지)/thermal là hiệu năng (performance / 성능) yêu cầu (requirement / 요구사항)

CPU/GPU/mạng (network / 네트워크)/location/background wakeups tiêu pin và sinh nhiệt. Polling, thử lại (retry / 재시도) vòng lặp (loop / 루프), location high accuracy, animation liên tục có thể làm hệ thống (system / 시스템) throttle.

Measure bằng Instruments/trường dữ liệu (field / 필드) metrics; Simulator không phản ánh đầy đủ thermal/năng lượng (energy / 에너지) hành vi (behavior / 동작).

---

# 28. Threat modeling trước bảo mật (security / 보안) điều khiển (control / 제어)

Xác định:

- asset cần bảo vệ;
- attacker năng lực (capability / 역량);
- trust ranh giới (boundary / 경계);
- entry điểm (point / 지점);
- hậu quả compromise;
- mitigation chi phí (cost / 비용).

Không mọi app cần certificate pinning/Secure Enclave/custom crypto. điều khiển (control / 제어) không match threat mô hình (model / 모델) có thể thêm operational rủi ro (risk / 위험) mà không giảm attack đáng kể.

---

# 29. Keychain, biometrics và Secure Enclave

Keychain khả năng tiếp cận (accessibility / 접근성) option quyết định khi item truy cập được và có migrate/backup/device-only hay không tùy option. Chọn theo use trường hợp (case / 사례), không bản sao (copy / 복사) snippet mặc định.

LocalAuthentication xác minh người dùng (user / 사용자) presence/biometry chính sách (policy / 정책) ở thiết bị (device / 장치); nó không thay authorization backend.

Secure Enclave phù hợp protected key operations nhất định; không phải generic cơ sở dữ liệu (database / 데이터베이스) để bỏ mọi secret.

---

# 30. Secret, vận chuyển (transport / 전송) và trust ranh giới (boundary / 경계)

Secret server-side không thể được giấu an toàn vĩnh viễn trong máy khách (client / 클라이언트) nhị phân (binary / 이진). API key có privilege cao phải nằm backend.

ATS giúp enforce secure vận chuyển (transport / 전송); exception nên phạm vi (scope / 범위) nhỏ và có lý do. Certificate pinning cần key/cert rotation/khôi phục (recovery / 복구) plan trước khi ship.

Máy khách (client / 클라이언트) kiểm tra hợp lệ (validation / 검증) cải thiện UX/hardening nhưng máy chủ (server / 서버) vẫn phải enforce authorization/nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙).

---

# 31. Privacy và supply-chain bảo mật (security / 보안)

Chỉ collect dữ liệu (data / 데이터) cần cho sản phẩm (product / 제품)/thao tác (operation / 연산). Permission yêu cầu (request / 요청) đúng ngữ cảnh (context / 맥락); purpose string phải phản ánh usage thật.

Third-party SDK có thể thêm mạng (network / 네트워크) endpoint, dữ liệu (data / 데이터) collection, nhị phân (binary / 이진) kích thước (size / 크기) và vulnerability surface. rà soát (review / 검토) transitive phụ thuộc (dependency / 의존성), privacy manifest/disclosure, maintainer/bản phát hành (release / 릴리스) cadence và cập nhật (update / 업데이트) chiến lược (strategy / 전략).

Phụ thuộc (dependency / 의존성) pin quá cứng có thể giữ vulnerability; auto-update không rà soát (review / 검토) có thể đưa breaking/malicious thay đổi (change / 변경). Cần chính sách (policy / 정책) cân bằng.

---

# 32. App Extension/tiến trình (process / 프로세스) ranh giới (boundary / 경계)

Widget, Share Extension, Notification dịch vụ (service / 서비스) Extension, Live Activity-related thành phần (component / 컴포넌트) có tiến trình (process / 프로세스)/tài nguyên (resource / 자원)/vòng đời (lifecycle / 생명주기) riêng. Không giả định main app và extension share in-memory singleton.

Dữ liệu (data / 데이터) sharing qua App Group/bộ chứa (container / 컨테이너) hoặc system-defined cơ chế (mechanism / 메커니즘) cần consistency/bảo mật (security / 보안) chính sách (policy / 정책). Extension ngân sách (budget / 예산) thường khắt khe hơn app chính; heavy công việc (work / 작업) phải được thiết kế lại, không bản sao (copy / 복사) nguyên dịch vụ (service / 서비스) đồ thị (graph / 그래프).

---

# 33. StoreKit và entitlement trạng thái (state / 상태)

Purchase success UI callback không phải nguồn duy nhất. StoreKit 2 giao dịch (transaction / 트랜잭션) updates/xác minh (verification / 확인) và entitlement reconstruction cần xử lý across launch/thiết bị (device / 장치)/account.

Subscription có grace period, billing thử lại (retry / 재시도), revoked/refunded trạng thái (state / 상태). Server-side xác minh (verification / 확인) có thể cần khi entitlement liên quan backend dịch vụ (service / 서비스)/giá trị (value / 값).

Idempotency đặc biệt quan trọng khi fulfillment/reward có side tác động (effect / 효과).

---

# 34. WidgetKit, ActivityKit và App Intents

Widget refresh do hệ thống (system / 시스템) chính sách (policy / 정책); không phải mini-app timer. Live Activity cũng có cập nhật (update / 업데이트)/ngân sách (budget / 예산)/vòng đời (lifecycle / 생명주기) riêng.

App Intents expose lĩnh vực (domain / 도메인) hành động (action / 동작)/thực thể (entity / 엔터티) cho Shortcuts/Siri/Spotlight/hệ thống (system / 시스템) experience. API intent là public-like đặc tả hợp đồng (contract / 계약) với hệ thống (system / 시스템); naming/parameter/thực thể (entity / 엔터티) truy vấn (query / 쿼리) cần stable ngữ nghĩa (semantic / 의미적).

Đừng để extension/intent trực tiếp import toàn app mô-đun (module / 모듈) nếu chỉ cần lĩnh vực (domain / 도메인)/dịch vụ (service / 서비스) subset.

---

# 35. CloudKit và sync choice

CloudKit phù hợp Apple ecosystem sync use trường hợp (case / 사례) nhất định, nhưng không tự động phù hợp cross-platform/backend analytics/truy vấn (query / 쿼리) yêu cầu (requirement / 요구사항).

Khi chọn sync backend, đánh giá định danh (identity / 식별자), sharing, xung đột (conflict / 충돌), offline, di chuyển (migration / 마이그레이션), khả năng quan sát (observability / 관측 가능성) và vendor lock-in — không chỉ “không cần dựng máy chủ (server / 서버)”.

---

# 36. khả năng tiếp cận (accessibility / 접근성)/localization là bản phát hành (release / 릴리스) cổng chất lượng (quality gate / 품질 게이트)

VoiceOver cây (tree / 트리), động (dynamic / 동적) kiểu (type / 타입) cực lớn, Reduce Motion, Differentiate Without Color, contrast và custom hành động (action / 동작) phải được kiểm thử (test / 테스트) ở trọng yếu (critical / 중요) luồng (flow / 흐름).

Localization cần pluralization/ngữ cảnh (context / 맥락), không concatenate sentence fragment nếu grammar có thể đổi thứ tự (order / 순서). Pseudo-localization bắt clipping/hard-code trước khi translation thật.

Khả năng tiếp cận (accessibility / 접근성)/localization regression nên nằm trong Definition of Done của thành phần (component / 컴포넌트)/luồng (flow / 흐름) có user-facing UI, không phải phase “sau khi mã (code / 코드) xong”.

---

# 37. cờ tính năng (feature flag / 기능 플래그) quản trị (governance / 거버넌스)

Flag cần:

- đơn vị sở hữu (owner / 오너);
- purpose;
- default;
- rollout audience;
- chỉ số (metric / 지표) success/thất bại (failure / 실패);
- kill-switch ngữ nghĩa (semantics / 의미론) nếu có;
- expiry/removal ticket.

Flag không phải authorization. máy khách (client / 클라이언트) flag có thể bị manipulate. Khi rollout xong, xóa dead branch để giảm state-space kiểm thử (test / 테스트).

---

# 38. bản phát hành (release / 릴리스) kỹ thuật (engineering / 엔지니어링) — hiện vật bản dựng (build artifact / 빌드 산출물) là sản phẩm

Chuỗi xử lý (pipeline / 파이프라인) không kết thúc ở đơn vị (unit / 단위) kiểm thử (test / 테스트). bản phát hành (release / 릴리스) sản phẩm tạo ra (artifact / 산출물) cần:

1. reproducible phụ thuộc (dependency / 의존성)/toolchain cấu hình (config / 설정);
2. archive bản phát hành (release / 릴리스) cấu hình (configuration / 구성);
3. signing/entitlement xác minh (verification / 확인);
4. di chuyển (migration / 마이그레이션) install/upgrade kiểm thử (test / 테스트);
5. trọng yếu (critical / 중요) UI/background/push/deep-link smoke kiểm thử (test / 테스트);
6. symbol upload;
7. TestFlight/staged rollout chính sách (policy / 정책);
8. monitoring/quay lui (rollback / 롤백)/kill-switch readiness.

Fresh install pass không chứng minh upgrade từ môi trường vận hành (production / 운영 환경) phiên bản (version / 버전) pass.

---

# 39. Mobile chiến lược quay lui (rollback strategy / 롤백 전략)

App Store nhị phân (binary / 이진) không quay lui (rollback / 롤백) tức thì cho toàn bộ người dùng (user / 사용자). Vì vậy mitigation hierarchy thường gồm:

- disable tính năng (feature / 기능) qua máy chủ (server / 서버)/flag nếu được thiết kế;
- backend tính tương thích (compatibility / 호환성) fix;
- hotfix nhị phân (binary / 이진);
- staged rollout pause;
- dữ liệu (data / 데이터) repair/di chuyển (migration / 마이그레이션) nếu cần.

Quay lui (rollback / 롤백) plan phải được nghĩ trước khi bản phát hành (release / 릴리스) tính năng (feature / 기능) có di chuyển (migration / 마이그레이션)/destructive side tác động (effect / 효과).

---

# 40. Disaster khôi phục (recovery / 복구) và dữ liệu (data / 데이터) repair

Nếu di chuyển (migration / 마이그레이션)/sync bug làm dữ liệu sai, cần biết:

- có backup/máy chủ (server / 서버) authority không;
- có kiểm tra (audit / 감사) lịch sử (history / 이력)/sự kiện (event / 이벤트) log không;
- repair có idempotent không;
- app phiên bản (version / 버전) cũ có tiếp tục làm hỏng dữ liệu (data / 데이터) không;
- kill switch nào chặn writer;
- communication/rollout chuỗi (sequence / 시퀀스) nào tránh race giữa repair và máy khách (client / 클라이언트).

Đây là nơi khả năng quan sát (observability / 관측 가능성), lược đồ (schema / 스키마) phiên bản (version / 버전) và cờ tính năng (feature flag / 기능 플래그) gặp nhau.

---

# 41. Xcode 27 / iOS 27 hiện tại (current / 현재) notes

Baseline stable của thư viện (library / 라이브러리) là Xcode 27/Swift 6.4/iOS 27 SDK. Minor Xcode 27.1/27.2 vẫn beta tại thời điểm cập nhật nên hành vi (behavior / 동작) chỉ có ở beta không được viết như môi trường vận hành (production / 운영 환경) baseline.

Xcode 27 generation tiếp tục thay đổi SwiftUI trạng thái (state / 상태)/builder hiện thực (implementation / 구현), caching/data-flow/tooling và coding-agent tích hợp (integration / 통합). Khi hành vi (behavior / 동작) thay đổi giữa Xcode 26 → 27:

- đọc bản phát hành (release / 릴리스) notes;
- tìm Đặc tả API (API contract / API 계약) thay vì dựa vào hiện thực (implementation / 구현) detail;
- chạy UI trạng thái (state / 상태)/định danh (identity / 식별자) regression;
- profile bản dựng (build / 빌드)/thời gian chạy (runtime / 런타임) nếu trình biên dịch (compiler / 컴파일러)/builder thay đổi (change / 변경) liên quan;
- kiểm thử (test / 테스트) archive, không chỉ Preview.

AI coding tác nhân (agent / 에이전트) có thể viết/refactor/kiểm thử (test / 테스트), nhưng trình biên dịch (compiler / 컴파일러) green không chứng minh vòng đời (lifecycle / 생명주기), entitlement, bảo mật (security / 보안) hay di chuyển (migration / 마이그레이션) tính đúng đắn (correctness / 정확성).

---

# 42. bản dựng (build / 빌드) technology và debugging evolution

Swift 6.4 dùng Swift bản dựng (build / 빌드) làm default trong SwiftPM, giúp bản dựng (build / 빌드) hành vi (behavior / 동작) cross-platform thống nhất hơn.

Master-level bản dựng (build / 빌드) debugging cần đọc:

- gói (package / 패키지) resolution;
- mục tiêu (target / 대상)/mô-đun (module / 모듈) đồ thị (graph / 그래프);
- trình biên dịch (compiler / 컴파일러) invocation;
- tường minh (explicit / 명시적) mô-đun (module / 모듈) phụ thuộc (dependency / 의존성);
- linker lỗi (error / 오류);
- kiến trúc (architecture / 아키텍처) slice;
- generated giao diện (interface / 인터페이스);
- gỡ lỗi (debug / 디버그) symbol/mô-đun (module / 모듈) siêu dữ liệu (metadata / 메타데이터).

Xóa DerivedData chỉ là troubleshooting step, không phải root-cause phân tích (analysis / 분석).

Swift 6.4 cũng tiếp tục cải thiện mô-đun (module / 모듈) tracking trong gỡ lỗi (debug / 디버그) info, giúp LLDB tìm đúng mô-đun (module / 모듈) phụ thuộc (dependency / 의존성) chính xác hơn. Nếu `po`/expression evaluator lỗi, chưa chắc thời gian chạy (runtime / 런타임) đối tượng (object / 객체) sai; bản dựng (build / 빌드)/gỡ lỗi (debug / 디버그) siêu dữ liệu (metadata / 메타데이터) cũng là một tầng (layer / 계층) cần kiểm tra.

---

# 43. Documentation kỹ thuật (engineering / 엔지니어링) với DocC

Công khai (public / 공개)/dùng chung (shared / 공유) mô-đun (module / 모듈) nên document:

- ngữ nghĩa (semantics / 의미론)/bất biến (invariant / 불변식);
- quyền sở hữu (ownership / 소유권)/thời gian tồn tại (lifetime / 수명);
- actor/luồng thực thi (thread / 스레드) yêu cầu (requirement / 요구사항);
- lỗi (error / 오류)/cancellation;
- availability;
- side tác động (effect / 효과);
- usage example;
- di chuyển (migration / 마이그레이션)/deprecation.

DocC cho phép API tham chiếu (reference / 참조)/article/tutorial nằm gần nguồn (source / 소스). Nếu rất khó giải thích lớp trừu tượng (abstraction / 추상화) bằng vài đoạn rõ ràng, lớp trừu tượng (abstraction / 추상화) có thể đang ôm quá nhiều responsibility.

---

# 44. ADR và technical quản trị (governance / 거버넌스)

ADR phù hợp quyết định khó đảo hoặc ảnh hưởng nhiều nhóm (team / 팀): minimum OS, Swift ngôn ngữ (language / 언어) chế độ (mode / 모드), kiến trúc (architecture / 아키텍처) ranh giới (boundary / 경계), persistence/sync, điều hướng (navigation / 내비게이션) quyền sở hữu (ownership / 소유권), bảo mật (security / 보안) chính sách (policy / 정책), khả năng quan sát (observability / 관측 가능성) vendor.

Template tối thiểu:

```text
Context
Constraints
Options considered
Decision
Consequences / trade-offs
Migration plan
Revisit trigger
```

Không biến ADR thành approval bureaucracy cho mọi refactor nhỏ.

---

# 45. môi trường vận hành (production / 운영 환경) Definition of Done theo rủi ro (risk / 위험)

Definition of Done không cần giống nhau cho mọi thay đổi (change / 변경). Một label văn bản (text / 텍스트) và di chuyển (migration / 마이그레이션) cơ sở dữ liệu (database / 데이터베이스) không có rủi ro (risk / 위험) ngang nhau.

Rủi ro (risk / 위험) cao có thể yêu cầu:

- đơn vị (unit / 단위)/tích hợp (integration / 통합)/UI regression;
- di chuyển (migration / 마이그레이션) fixture;
- hiệu năng (performance / 성능) baseline;
- khả năng tiếp cận (accessibility / 접근성) check;
- threat/privacy rà soát (review / 검토);
- cờ tính năng (feature flag / 기능 플래그)/quay lui (rollback / 롤백) plan;
- khả năng quan sát (observability / 관측 가능성) chỉ số (metric / 지표);
- staged rollout.

Risk-based rigor tốt hơn checklist enterprise áp cho mọi lần ghi nhận (commit / 커밋).

---

# 46. Master kiểm tra (audit / 감사) ma trận (matrix / 행렬)

Trước khi gọi một hệ thống (system / 시스템) production-ready, trả lời được:

| Trục | Câu hỏi bắt buộc |
|---|---|
| ngôn ngữ (language / 언어) | ngôn ngữ (language / 언어) chế độ (mode / 모드)/toolchain nào, unsafe/quyền sở hữu (ownership / 소유권) ranh giới (boundary / 경계) ở đâu? |
| bộ nhớ (memory / 메모리) | đối tượng (object / 객체)/tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명) và retain đồ thị (graph / 그래프) có rõ không? |
| tính đồng thời (concurrency / 동시성) | tác vụ (task / 작업) đơn vị sở hữu (owner / 오너), cancellation, isolation, reentrancy, Sendable đặc tả hợp đồng (contract / 계약)? |
| UI | SwiftUI định danh (identity / 식별자)/trạng thái (state / 상태) đơn vị sở hữu (owner / 오너), UIKit vòng đời (lifecycle / 생명주기)/interop ranh giới (boundary / 경계)? |
| dữ liệu (data / 데이터) | máy chủ (server / 서버)/cục bộ (local / 로컬)/bộ nhớ đệm (cache / 캐시) authority và reconciliation? |
| Persistence | lược đồ (schema / 스키마) di chuyển (migration / 마이그레이션)/ngữ cảnh (context / 맥락) isolation/repair plan? |
| mạng (network / 네트워크) | hết thời gian chờ (timeout / 타임아웃)/thử lại (retry / 재시도)/idempotency/auth refresh/background transfer? |
| kiến trúc (architecture / 아키텍처) | phụ thuộc (dependency / 의존성) direction/mô-đun (module / 모듈) API/vendor ranh giới (boundary / 경계)? |
| hiệu năng (performance / 성능) | ngân sách (budget / 예산) + đo lường (measurement / 측정) trên release-like thiết bị (device / 장치)? |
| bảo mật (security / 보안) | threat mô hình (model / 모델), key/secret/vận chuyển (transport / 전송)/privacy controls? |
| bản phát hành (release / 릴리스) | archive/signing/di chuyển (migration / 마이그레이션)/staged rollout/symbols/quay lui (rollback / 롤백)? |
| Operations | log/chỉ số (metric / 지표)/dấu vết (trace / 추적)/crash + sự cố (incident / 인시던트)/runbook? |

Không phải app nhỏ phải triển khai mọi enterprise cơ chế (mechanism / 메커니즘). Nhưng các trục có rủi ro thật phải có câu trả lời có chủ đích.

---

# 47. mạch học (learning flow / 학습 흐름) hoàn chỉnh Beginner → Master

**Beginner** xây ngữ nghĩa (semantics / 의미론): giá trị (value / 값)/tham chiếu (reference / 참조), Optional, closure/ARC, SwiftUI trạng thái (state / 상태), async suspension, UIKit vòng đời (lifecycle / 생명주기) và interop cơ bản.

**Intermediate** xây quyền sở hữu (ownership / 소유권)/isolation: structured/unstructured tác vụ (task / 작업), actor/reentrancy, Sendable, Observation quyền sở hữu trạng thái (state ownership / 상태 소유권), mạng (network / 네트워크)/persistence ranh giới (boundary / 경계) và tính năng (feature / 기능) kiến trúc (architecture / 아키텍처).

**Advanced/cấp cao (senior / 시니어)** xây môi trường vận hành (production / 운영 환경) hiện thực (implementation / 구현): UIKit/SwiftUI hybrid vòng đời (lifecycle / 생명주기), modularization, API resilience, Instruments, persistence/mạng (network / 네트워크) độ tin cậy (reliability / 신뢰성), bảo mật (security / 보안), CI/CD và sự cố (incident / 인시던트) lập luận (reasoning / 추론).

**Master** xây longevity: phiên bản (version / 버전) evolution, nguồn (source / 소스)/nhị phân (binary / 이진)/lược đồ (schema / 스키마)/API tính tương thích (compatibility / 호환성), quản trị (governance / 거버넌스), threat/hiệu năng (performance / 성능) ngân sách (budget / 예산), bản phát hành (release / 릴리스)/quay lui (rollback / 롤백)/disaster khôi phục (recovery / 복구).

Nếu một khái niệm Master không nối được về đồ thị (graph / 그래프) ở Advanced hoặc ngữ nghĩa (semantics / 의미론) ở Beginner/Intermediate, quay lại mức (level / 수준) trước thay vì học thêm công cụ (tool / 도구) mới.

---

# 48. Cách tự cập nhật kiến thức sau khi tài liệu này lỗi thời

Không tài liệu Swift/iOS nào giữ đúng mãi. Workflow cập nhật:

1. đọc Swift.org bản phát hành (release / 릴리스) post + Swift Evolution proposal liên quan;
2. đọc Xcode bản phát hành (release / 릴리스) notes/hệ thống (system / 시스템) requirements;
3. đọc Apple khung phần mềm (framework / 프레임워크) API availability/documentation;
4. xác định thay đổi (change / 변경) thuộc ngôn ngữ (language / 언어), trình biên dịch (compiler / 컴파일러), SDK hay thời gian chạy (runtime / 런타임);
5. ánh xạ (mapping / 매핑) vào mô hình tư duy (mental model / 사고 모델): kiểu (type / 타입)/quyền sở hữu (ownership / 소유권)/isolation/trạng thái (state / 상태)/vòng đời (lifecycle / 생명주기)/ranh giới (boundary / 경계)/tính tương thích (compatibility / 호환성);
6. viết reproduction nhỏ;
7. di chuyển (migration / 마이그레이션) trên một tính năng (feature / 기능) trước;
8. đo bản dựng (build / 빌드)/thời gian chạy (runtime / 런타임)/kiểm thử (test / 테스트) trước khi rollout toàn repo.

Tutorial/blog/community post hữu ích cho hiện thực (implementation / 구현) idea, nhưng khi mâu thuẫn với Đặc tả API (API contract / API 계약)/bản phát hành (release / 릴리스) ghi chú (note / 노트) của toolchain thực tế, ưu tiên nguồn chính thức.

---

# 49. Nguồn chính thức nên theo dõi

Ưu tiên Swift.org và Swift Documentation/Evolution cho ngôn ngữ (language / 언어)/trình biên dịch (compiler / 컴파일러); Apple nhà phát triển (developer / 개발자) Documentation cho UIKit/SwiftUI/Foundation/SwiftData/StoreKit và nền tảng (platform / 플랫폼) khung phần mềm (framework / 프레임워크); Xcode bản phát hành (release / 릴리스) Notes/hệ thống (system / 시스템) Requirements cho toolchain/SDK; WWDC sessions cho thiết kế (design / 설계) intent/di chuyển (migration / 마이그레이션) examples.

Mục tiêu Master không phải thuộc toàn bộ SDK. Mục tiêu là có mô hình tư duy (mental model / 사고 모델) và môi trường vận hành (production / 운영 환경) discipline đủ mạnh để khi Swift 6.5/7.x hoặc iOS thế hệ sau thay đổi API, bạn biết **cái gì thật sự đổi**, **ranh giới (boundary / 경계) nào bị ảnh hưởng**, **kiểm thử (test / 테스트) nào cần chạy** và **bản phát hành (release / 릴리스) thế nào để không biến người dùng (user / 사용자) thành di chuyển (migration / 마이그레이션) kiểm thử (test / 테스트)**.

> **Bàn giao:** Sau **6.4 cầu nối (bridge / 브리지) legacy thay vì rewrite đồng loạt**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
