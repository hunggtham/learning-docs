# Swift & iOS Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)

> **Mạch đọc:** [README](./README.md) là owner của **Swift & iOS Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**; quay lại đó để kiểm tra ranh giới với Intermediate và Master. Bắt đầu ở **1.1 quyền sở hữu (ownership / 소유권) đồ thị (graph / 그래프)**, qua weak/unowned và actor isolation, rồi nối sang hiệu năng, modularization, resilient networking, bảo mật và CI/CD; các quyết định hệ thống phải được giải thích bằng lifetime, dữ liệu và failure mode đã chốt ở phần trước.

> Mục tiêu: từ feature-level tính đúng đắn (correctness / 정확성) tiến tới môi trường vận hành (production / 운영 환경) quyền sở hữu (ownership / 소유권): bộ nhớ (memory / 메모리)/tính đồng thời (concurrency / 동시성) bất biến (invariant / 불변식) rõ, UIKit/SwiftUI vòng đời (lifecycle / 생명주기) đúng, mô-đun (module / 모듈)/kiến trúc (architecture / 아키텍처) có phụ thuộc (dependency / 의존성) direction, hiệu năng (performance / 성능) được đo, di chuyển (migration / 마이그레이션)/bản phát hành (release / 릴리스) không dựa vào may mắn.
>
> Prerequisite: Intermediate — đặc biệt tác vụ (task / 작업) thời gian tồn tại (lifetime / 수명), actor isolation/reentrancy, `Sendable`, Observation quyền sở hữu trạng thái (state ownership / 상태 소유권), HTTP/persistence ranh giới (boundary / 경계) và UIKit ↔ SwiftUI cầu nối (bridge / 브리지) cơ bản.

Senior-level iOS kỹ thuật (engineering / 엔지니어링) không phải biết nhiều API nhất. Đó là khả năng nhìn một hệ thống và giải thích **thời gian tồn tại (lifetime / 수명), quyền sở hữu (ownership / 소유권), isolation, định danh (identity / 식별자), tác động (effect / 효과), ranh giới (boundary / 경계) và tính tương thích (compatibility / 호환성)**; sau đó dùng công cụ (tool / 도구) để kiểm chứng thay vì đoán.

---

# 1. bộ nhớ (memory / 메모리) mô hình (model / 모델) và quyền sở hữu (ownership / 소유권) sâu hơn

ARC chỉ quản lý thời gian tồn tại (lifetime / 수명) của reference-counted đối tượng (object / 객체). Nó không quản lý “toàn bộ bộ nhớ (memory / 메모리)”, không phát hiện cycle và không giải quyết dữ liệu (data / 데이터) race. Struct có thể chứa lớp (class / 클래스) tham chiếu (reference / 참조); closure có tham chiếu (reference / 참조) định danh (identity / 식별자)/thời gian tồn tại (lifetime / 수명); collection có heap-backed lưu trữ (storage / 저장소); Objective-C cầu nối (bridge / 브리지) có autorelease/bridging hành vi (behavior / 동작) riêng.

## 1.1 quyền sở hữu (ownership / 소유권) đồ thị (graph / 그래프) thay vì quy tắc `weak self`

Đoạn code dưới đây là bằng chứng cho khái niệm vừa mở. Hãy đọc từ input và state đến output, ghi lại điều kiện áp dụng và giới hạn trước khi chuyển sang mục kế tiếp.

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

Câu hỏi đúng là: ai giữ `Downloader`, ai giữ closure, closure sống đến khi nào, thao tác (operation / 연산) có cần đơn vị sở hữu (owner / 오너) sống để hoàn tất hay không. Nếu closure synchronous/non-escaping, weak capture thường không cần. Nếu closure được thuộc tính (property / 속성)/dịch vụ (service / 서비스) giữ và closure lại giữ `self`, cycle có thể hình thành.

> **Nối mạch:** Ownership graph giải thích retain cycle; `weak`/`unowned` là lifetime contracts, rồi closure capture tiếp theo phải xét mọi captured value chứ không chỉ `self`.

## 1.2 `weak` và `unowned` là thời gian tồn tại (lifetime / 수명) đặc tả hợp đồng (contract / 계약)

`weak` cho phép mục tiêu (target / 대상) biến mất và vì vậy truy cập (access / 접근) có Optional ngữ nghĩa (semantics / 의미론). `unowned` không retain nhưng giả định mục tiêu (target / 대상) còn sống tại mọi truy cập (access / 접근). `unowned` nên được dùng khi quan hệ (relation / 관계) thời gian tồn tại (lifetime / 수명) là bất biến (invariant / 불변식) của mô hình (model / 모델), không phải để tránh unwrap.

> **Nối mạch:** `weak`/`unowned` đặt lifetime contract cho reference; closure capture tiếp theo phải kiểm kê mọi captured value trước khi vượt sang Objective-C/autorelease boundary.

## 1.3 Closure capture không chỉ là `self`

Capture danh sách (list / 목록) có thể snapshot giá trị (value / 값) hoặc thay quyền sở hữu (ownership / 소유권) của tham chiếu (reference / 참조). Large giá trị (value / 값) capture, existential box, closure allocation và hidden bridging có thể ảnh hưởng bộ nhớ (memory / 메모리)/hiệu năng (performance / 성능) trong đường xử lý nóng (hot path / 핫 패스). Đừng optimize trước khi profile, nhưng khi profile cho thấy allocation pressure, hãy biết closure/generic/existential cũng là nguồn allocation.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Swift & iOS Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **1.3 Closure capture không chỉ là self** đặt tiêu chí; **1.4 Autorelease và Objective-C ranh giới (boundary / 경계)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **1.5 tài nguyên (resource / 자원) quyền sở hữu (ownership / 소유권) ngoài bộ nhớ (memory / 메모리)** mở rộng hệ quả.

## 1.4 Autorelease và Objective-C ranh giới (boundary / 경계)

Swift-native ARC và Objective-C ARC interoperable nhưng Foundation/Objective-C API có thể tạo autoreleased đối tượng (object / 객체). Trong batch vòng lặp (loop / 루프) lớn qua legacy API, autorelease pool phạm vi (scope / 범위) có thể ảnh hưởng peak bộ nhớ (memory / 메모리). Đây là tối ưu hóa (optimization / 최적화) ranh giới (boundary / 경계); đừng rải `autoreleasepool` khắp app nếu Instruments chưa chỉ ra nhu cầu.

> **Nối mạch:** Trong **Swift & iOS Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **1.4 Autorelease và Objective-C ranh giới (boundary / 경계)** đặt tiêu chí; **1.5 tài nguyên (resource / 자원) quyền sở hữu (ownership / 소유권) ngoài bộ nhớ (memory / 메모리)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **4.1 Single-flight thao tác (operation / 연산)** mở rộng hệ quả.

## 1.5 tài nguyên (resource / 자원) quyền sở hữu (ownership / 소유권) ngoài bộ nhớ (memory / 메모리)

Tệp (file / 파일) handle, socket, cơ sở dữ liệu (database / 데이터베이스) giao dịch (transaction / 트랜잭션), camera session, security-scoped URL, observer đơn vị từ (token / 토큰) đều có thời gian tồn tại (lifetime / 수명). ARC có thể giúp đơn vị sở hữu (owner / 오너) đối tượng (object / 객체) được deinit, nhưng nghiệp vụ (business / 비즈니스) tính đúng đắn (correctness / 정확성) không nên phụ thuộc vào thời điểm deallocation để lần ghi nhận (commit / 커밋)/save/mạng (network / 네트워크). tài nguyên (resource / 자원) quan trọng cần tường minh (explicit / 명시적) open/close/start/stop chính sách (policy / 정책) khi khung phần mềm (framework / 프레임워크) yêu cầu.

---

# 2. quyền sở hữu (ownership / 소유권) ngôn ngữ (language / 언어) features và safe hiệu năng (performance / 성능)

Swift hiện đại làm quyền sở hữu (ownership / 소유권) tường minh (explicit / 명시적) hơn qua borrowing/consuming và noncopyable types. Mục tiêu là giảm bản sao (copy / 복사) và biểu diễn unique tài nguyên (resource / 자원) mà không rơi xuống raw pointer.

Ứng dụng (application / 애플리케이션) nghiệp vụ (business / 비즈니스) mã (code / 코드) chưa cần annotate mọi giá trị (value / 값). cấp cao (senior / 시니어) cần hiểu để đọc khung phần mềm (framework / 프레임워크)/thư viện (library / 라이브러리) mới và để thiết kế ranh giới (boundary / 경계) thấp tầng.

Swift 6.4 mở rộng nhóm API này với borrow/mutate accessors, `Ref`/`MutableRef`, `UniqueBox`, `UniqueArray`, `Iterable` và memory-safe truy cập (access / 접근) API. Chỉ dùng khi profile/tài nguyên (resource / 자원) ngữ nghĩa (semantics / 의미론) justify; `Array`/ordinary giá trị (value / 값) types vẫn là default tốt cho phần lớn app.

---

# 3. Existential, opaque kiểu (type / 타입) và dispatch chi phí (cost / 비용)

`any P` là existential bộ chứa (container / 컨테이너) cho thời gian chạy (runtime / 런타임) polymorphism; `some P` che concrete kiểu (type / 타입) nhưng giữ static định danh (identity / 식별자) cho trình biên dịch (compiler / 컴파일러).

```swift
protocol ImageFetching<Image> {
    associatedtype Image
    func fetch() async throws -> Image
}
```

Kiểu (type / 타입) erasure mua flexibility nhưng có chi phí (cost / 비용) về kiểu (type / 타입) thông tin (information / 정보), potential boxing/động (dynamic / 동적) dispatch và API độ phức tạp (complexity / 복잡도). Không phải mọi API công khai (public API / 공개 API) phải generic; chọn lớp trừu tượng (abstraction / 추상화) dựa trên use trường hợp (case / 사례) và compile-time/thời gian chạy (runtime / 런타임) sự đánh đổi (trade-off / 트레이드오프).

Giao thức (protocol / 프로토콜) extension dispatch trap:

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

Nếu `foo` không phải giao thức (protocol / 프로토콜) yêu cầu (requirement / 요구사항), động (dynamic / 동적) hành vi (behavior / 동작) có thể không như người đọc kỳ vọng. Khi polymorphism là đặc tả hợp đồng (contract / 계약), khai báo yêu cầu (requirement / 요구사항) rõ.

---

# 4. tính đồng thời (concurrency / 동시성) môi trường vận hành (production / 운영 환경) — bất biến (invariant / 불변식) qua suspension điểm (point / 지점)

Intermediate đã học actor/reentrancy; ở cấp cao (senior / 시니어), trọng tâm là bất biến (invariant / 불변식) và thao tác (operation / 연산) thiết kế (design / 설계).

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

`await` là nơi giả định (assumption / 가정) có thể mất hiệu lực. Nếu thao tác (operation / 연산) cần atomic chuyển tiếp trạng thái (state transition / 상태 전이), hãy giảm suspension bên trong trọng yếu (critical / 중요) ngữ nghĩa (semantic / 의미적) region hoặc lưu/revalidate phiên bản (version / 버전)/trạng thái (state / 상태) sau await.

> **Nối mạch:** Ở chặng này của **Swift & iOS Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **1.5 tài nguyên (resource / 자원) quyền sở hữu (ownership / 소유권) ngoài bộ nhớ (memory / 메모리)** đặt vấn đề; **4.1 Single-flight thao tác (operation / 연산)** đối chiếu bằng chứng, rồi **4.2 tác vụ (task / 작업) quyền sở hữu (ownership / 소유권)** mở rộng hệ quả hoặc giới hạn liên quan.

## 4.1 Single-flight thao tác (operation / 연산)

Auth refresh, expensive bộ nhớ đệm (cache / 캐시) tải (load / 로드) hoặc lược đồ (schema / 스키마) preparation thường cần “một thao tác (operation / 연산) in-flight, nhiều caller chờ chung”. Actor có thể giữ `Task` hiện tại và clear khi hoàn tất. Điều khó không phải cú pháp (syntax / 문법) mà là thất bại (failure / 실패)/cancellation chính sách (policy / 정책): caller cancel có cancel dùng chung (shared / 공유) công việc (work / 작업) không, hay dùng chung (shared / 공유) tác vụ (task / 작업) sống vì caller khác còn cần?

> **Nối mạch:** Đặt trong câu hỏi lớn của **Swift & iOS Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, sau nội dung của **4.1 Single-flight thao tác (operation / 연산)**, **4.2 tác vụ (task / 작업) quyền sở hữu (ownership / 소유권)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **4.3 Cancellation cleanup** mở rộng hệ quả hoặc giới hạn liên quan.

## 4.2 tác vụ (task / 작업) quyền sở hữu (ownership / 소유권)

Tác vụ (task / 작업) thuộc tính (property / 속성) phải có đơn vị sở hữu (owner / 오너)/thời gian tồn tại (lifetime / 수명) chính sách (policy / 정책). Screen tác vụ (task / 작업) có thể cancel khi screen biến mất; upload/background sync có thể thuộc dịch vụ (service / 서비스) khác. tác vụ (task / 작업) không nên sống vô hạn chỉ vì đối tượng (object / 객체) bị singleton giữ.

> **Nối mạch:** Trong **Swift & iOS Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **4.3 Cancellation cleanup** nối từ **4.2 tác vụ (task / 작업) quyền sở hữu (ownership / 소유권)** sang **4.4 Lower-level synchronization**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4.3 Cancellation cleanup

Cancellation-aware thao tác (operation / 연산) cần cleanup idempotent. Nếu giao dịch (transaction / 트랜잭션) đã mutate một phần trạng thái (state / 상태) trước cancellation, quay lui (rollback / 롤백)/compensation phải được thiết kế; `CancellationError` không tự đảo side tác động (effect / 효과).

> **Nối mạch:** Cancellation cleanup phải hoàn tất trước khi hạ xuống lock/atomic synchronization; sau đó view loading và controller lifetime được tách thành lifecycle boundary riêng.

## 4.4 Lower-level synchronization

Actor là default tốt cho dùng chung (shared / 공유) mutable trạng thái (state / 상태). Mutex/atomics phù hợp hot synchronous thành phần nguyên thủy (primitive / 기본 요소) hoặc thư viện (library / 라이브러리) thấp tầng khi benchmark/bất biến (invariant / 불변식) justify. Không giữ khóa (lock / 잠금) xuyên `await`; tránh lock-order cycle và blocking main luồng thực thi (thread / 스레드).

---

# 5. SwiftUI rendering/hiệu năng (performance / 성능) mô hình tư duy (mental model / 사고 모델)

`body` được recompute là bình thường. Bottleneck thường đến từ expensive synchronous công việc (work / 작업), unstable định danh (identity / 식별자), bố cục (layout / 레이아웃) phản hồi (feedback / 피드백), ảnh (image / 이미지) decode, broad observation phụ thuộc (dependency / 의존성) hoặc đối tượng (object / 객체) churn.

```swift
var body: some View {
    // bad nếu expensiveSort thật sự nặng và chạy thường xuyên
    let sorted = expensiveSort(items)
    List(sorted) { item in ... }
}
```

Derived dữ liệu (data / 데이터) có thể chuyển sang mô hình (model / 모델)/bộ nhớ đệm (cache / 캐시) khi cần; nhưng bộ nhớ đệm (cache / 캐시) cũng có vô hiệu hóa (invalidation / 무효화) chi phí (cost / 비용). Đo trước khi thêm độ phức tạp (complexity / 복잡도).

Stable định danh (identity / 식별자) quyết định trạng thái (state / 상태)/tác vụ (task / 작업) continuity. `.id(UUID())` để “refresh” gần như luôn là smell.

Ảnh (image / 이미지) hiệu năng (performance / 성능): mạng (network / 네트워크) bộ nhớ đệm (cache / 캐시) bytes khác decoded bitmap bộ nhớ (memory / 메모리). Feed ảnh lớn cần downsampling theo display kích thước (size / 크기), prefetch có giới hạn và cancellation khi item không còn visible.

---

# 6. SwiftUI bố cục (layout / 레이아웃), Preference và môi trường (environment / 환경) ở mức cấp cao (senior / 시니어)

Custom `Layout` dùng khi bộ chứa (container / 컨테이너) thật sự cần thuật toán measure/place riêng. PreferenceKey là cơ chế child → ancestor communication; dùng được nhưng dễ tạo hidden luồng dữ liệu (data flow / 데이터 흐름)/vòng phản hồi (feedback loop / 피드백 루프) nếu lạm dụng.

Môi trường (environment / 환경) phù hợp cross-cutting tree-scoped ngữ cảnh (context / 맥락). lĩnh vực (domain / 도메인) phụ thuộc (dependency / 의존성) bắt buộc nên tường minh (explicit / 명시적) ở ranh giới (boundary / 경계) thích hợp. Một tính năng (feature / 기능) mà kiểm thử (test / 테스트) không biết phụ thuộc (dependency / 의존성) đến từ đâu thường đã để môi trường (environment / 환경)/dịch vụ (service / 서비스) locator che quá nhiều.

---

# 7. UIKit vòng đời (lifecycle / 생명주기) — chuỗi (sequence / 시퀀스) và responsibility

UIKit vẫn là nền tảng của rất nhiều Apple UI API và môi trường vận hành (production / 운영 환경) codebase. cấp cao (senior / 시니어) phải hiểu vòng đời (lifecycle / 생명주기), không chỉ biết `viewDidLoad`.

Một `UIViewController` đi qua các phase chính:

1. `init`/storyboard decoding tạo controller đối tượng (object / 객체);
2. `loadView()` tạo gốc (root / 루트) view nếu view chưa tải (load / 로드);
3. `viewDidLoad()` chạy sau tải (load / 로드), thường một lần cho thời gian tồn tại (lifetime / 수명) của loaded view;
4. `viewWillAppear(_:)` mỗi lần chuẩn bị xuất hiện;
5. `viewIsAppearing(_:)` trong các SDK hiện đại cho phase appearance với hình học (geometry / 기하학)/trait đã cập nhật hơn;
6. bố cục (layout / 레이아웃) callback như `viewWillLayoutSubviews()`/`viewDidLayoutSubviews()` có thể chạy nhiều lần;
7. `viewDidAppear(_:)` khi đã xuất hiện;
8. `viewWillDisappear(_:)`/`viewDidDisappear(_:)` khi rời màn hình.

Không đặt yêu cầu (request / 요청) one-time vào `viewWillAppear` nếu điều hướng (navigation / 내비게이션) back/forward sẽ gọi lặp ngoài ý muốn. Ngược lại, trạng thái (state / 상태) phải refresh mỗi lần màn hình hiện lại không nên chỉ nằm trong `viewDidLoad`.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Swift & iOS Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **7.1 View loading khác controller thời gian tồn tại (lifetime / 수명)** nối từ **4.4 Lower-level synchronization** sang **7.2 bố cục (layout / 레이아웃) callback không phải nơi làm I/O**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7.1 View loading khác controller thời gian tồn tại (lifetime / 수명)

Controller tồn tại không đồng nghĩa `view` đã tải (load / 로드). Truy cập `view` có thể trigger tải (load / 로드). Dùng `isViewLoaded` khi cần kiểm mà không ép tải (load / 로드).

> **Nối mạch:** Trong **Swift & iOS Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **7.2 bố cục (layout / 레이아웃) callback không phải nơi làm I/O** nối từ **7.1 View loading khác controller thời gian tồn tại (lifetime / 수명)** sang **7.3 Trait và adaptive UI**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7.2 bố cục (layout / 레이아웃) callback không phải nơi làm I/O

`viewDidLayoutSubviews` có thể được gọi rất nhiều lần do ràng buộc (constraint / 제약조건), rotation, safe-area, content-size thay đổi (change / 변경). Không đặt mạng (network / 네트워크)/cơ sở dữ liệu (database / 데이터베이스)/heavy computation tại đây.

> **Nối mạch:** Ở chặng này của **Swift & iOS Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **7.3 Trait và adaptive UI** nối từ **7.2 bố cục (layout / 레이아웃) callback không phải nơi làm I/O** sang **Gate trước khi sang Master**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7.3 Trait và adaptive UI

Kích thước (size / 크기) lớp (class / 클래스), động (dynamic / 동적) kiểu (type / 타입), giao diện (interface / 인터페이스) style và nền tảng (platform / 플랫폼) trait có thể thay đổi trong thời gian tồn tại (lifetime / 수명). Với SDK mới, ưu tiên API trait observation hiện đại khi phù hợp thay vì giả định (assumption / 가정) “setup theme một lần trong viewDidLoad”.

---

# 8. UIKit containment — child controller đúng vòng đời (lifecycle / 생명주기)

Custom bộ chứa (container / 컨테이너) phải tuân giao thức (protocol / 프로토콜) containment:

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

Sai containment có thể làm appearance callbacks, rotation, safe area và child quyền sở hữu (ownership / 소유권) hoạt động không đúng. điều hướng (navigation / 내비게이션) controller/tab bar controller là hệ thống (system / 시스템) bộ chứa (container / 컨테이너); custom bộ chứa (container / 컨테이너) phải tôn trọng vòng đời (lifecycle / 생명주기) tương tự.

---

# 9. UIKit điều hướng (navigation / 내비게이션)/presentation vòng đời (lifecycle / 생명주기)

`UINavigationController` giữ ngăn xếp (stack / 스택) controller. `pushViewController`/`popViewController` thay ngăn xếp (stack / 스택); modal presentation tạo presentation relationship khác.

Không suy luận “viewDidDisappear = controller deinit”. Controller có thể vẫn ở điều hướng (navigation / 내비게이션) ngăn xếp (stack / 스택), presentation đồ thị (graph / 그래프) hoặc được đối tượng (object / 객체) khác retain.

Interactive chuyển tiếp (transition / 전이) có thể cancel. Vì vậy side tác động (effect / 효과) ở `viewWillDisappear` không nên mặc định coi điều hướng (navigation / 내비게이션) đã chắc chắn hoàn tất. Khi nghiệp vụ (business / 비즈니스) cần biết tuyến (route / 경로) trạng thái (state / 상태) chính xác, coordinator/router/điều hướng (navigation / 내비게이션) delegate có thể là nơi phù hợp hơn appearance callback.

---

# 10. Scene vòng đời (lifecycle / 생명주기) và multi-window

App vòng đời (lifecycle / 생명주기) và view-controller vòng đời (lifecycle / 생명주기) là hai tầng khác nhau. Từ scene-based vòng đời (lifecycle / 생명주기), app có thể có nhiều `UIScene`/`UIWindowScene` tùy nền tảng (platform / 플랫폼)/cấu hình (configuration / 구성).

Một scene có thể active/inactive/background độc lập. toàn cục (global / 전역) singleton UI trạng thái (state / 상태) dễ sai nếu app hỗ trợ nhiều scene/cửa sổ (window / 윈도우). trạng thái (state / 상태) nào thuộc account/app và trạng thái (state / 상태) nào thuộc cửa sổ (window / 윈도우)/scene phải được phân biệt.

Không dựa vào “app sắp terminate” callback để save dữ liệu quan trọng; tiến trình (process / 프로세스) có thể bị kill mà không cho bạn cơ hội cleanup mong muốn.

---

# 11. UIKit danh sách (list / 목록)/reuse/diffable dữ liệu (data / 데이터) nguồn (source / 소스)

Cell reuse là đối tượng (object / 객체) reuse, không phải dữ liệu (data / 데이터) quyền sở hữu (ownership / 소유권). `prepareForReuse()` và cấu hình (configuration / 구성) phải làm cell trở lại trạng thái phù hợp cho item mới.

Async ảnh (image / 이미지)/tác vụ (task / 작업) cần gắn với represented item và cancel khi reuse:

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

Diffable snapshot dùng stable định danh (identity / 식별자). Apply snapshot quá dày hoặc thay ID liên tục làm animation/trạng thái (state / 상태) khó đoán và tốn công việc (work / 작업).

Compositional bố cục (layout / 레이아웃) giúp mô tả section/group/item adaptive; nhưng bố cục (layout / 레이아웃) closure cũng cần nhẹ và deterministic.

---

# 12. UIKit bộ nhớ (memory / 메모리)/thời gian tồn tại (lifetime / 수명) traps

Các cycle thường gặp:

- controller/mô hình (model / 모델) giữ closure, closure giữ controller/mô hình (model / 모델);
- delegate được custom kiểu (type / 타입) khai báo strong thay vì weak khi quyền sở hữu (ownership / 소유권) không thuộc delegate;
- `Timer`/display-link/observer/callback đơn vị sở hữu (owner / 오너) không được invalidate/remove theo vòng đời (lifecycle / 생명주기);
- Combine `AnyCancellable` được đơn vị sở hữu (owner / 오너) giữ trong set, sink closure lại strong-capture đơn vị sở hữu (owner / 오너);
- child controller hoặc hosting controller bị add nhưng không remove đúng quyền sở hữu (ownership / 소유권).

Bộ nhớ (memory / 메모리) đồ thị (graph / 그래프) nên được dùng để đọc retain đường dẫn (path / 경로) cụ thể. “Controller không deinit” không chứng minh nguyên nhân cho đến khi bạn xem ai retain nó.

---

# 13. SwiftUI → UIKit với Representable

`UIViewRepresentable`/`UIViewControllerRepresentable` là adapter vòng đời (lifecycle / 생명주기) giữa declarative trạng thái (state / 상태) và UIKit đối tượng (object / 객체) định danh (identity / 식별자).

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

`make...` tạo UIKit đối tượng (object / 객체) cho representable định danh (identity / 식별자); `update...` đồng bộ SwiftUI đầu vào (input / 입력) mới vào đối tượng (object / 객체) tồn tại; `dismantle...` cleanup tài nguyên (resource / 자원) khi adapter bị tháo.

Đừng khởi động lại camera/player/map controller trong mỗi `update...` nếu đầu vào (input / 입력) không thực sự đổi.

---

# 14. Coordinator — delegate cầu nối (bridge / 브리지) và quyền sở hữu (ownership / 소유권)

Coordinator thường nhận delegate/data-source callback từ UIKit rồi mutate Binding/Observable trạng thái (state / 상태).

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

Coordinator thời gian tồn tại (lifetime / 수명) gắn với representable instance định danh (identity / 식별자) theo SwiftUI cầu nối (bridge / 브리지) ngữ nghĩa (semantics / 의미론). Hãy kiểm retain đồ thị (graph / 그래프): UIKit đối tượng (object / 객체) có retain delegate không, coordinator có retain controller không, closure có capture parent trạng thái (state / 상태) không.

Callback UIKit có thể đến trên hàng đợi (queue / 큐)/framework-defined ngữ cảnh (context / 맥락). Nếu cập nhật MainActor-isolated UI mô hình (model / 모델), cầu nối (bridge / 브리지) isolation rõ thay vì assume main luồng thực thi (thread / 스레드) nếu đặc tả hợp đồng (contract / 계약) không bảo đảm.

---

# 15. UIKit → SwiftUI với UIHostingController

Đoạn code dưới đây là bằng chứng cho khái niệm vừa mở. Hãy đọc từ input và state đến output, ghi lại điều kiện áp dụng và giới hạn trước khi chuyển sang mục kế tiếp.

```swift
let host = UIHostingController(rootView: ProfileView(model: model))
```

Nếu dùng như child controller, áp dụng containment đúng. Nếu `rootView` cần đổi, cập nhật (update / 업데이트) gốc (root / 루트) view hoặc tốt hơn truyền observable mô hình (model / 모델) để trạng thái (state / 상태) thay đổi mà không reconstruct điều hướng (navigation / 내비게이션)/controller đồ thị (graph / 그래프) vô ích.

Self-sizing/Auto bố cục (layout / 레이아웃) cần để hosting view có ràng buộc (constraint / 제약조건) hợp lệ. Safe area và điều hướng (navigation / 내비게이션) bar quyền sở hữu (ownership / 소유권) phải rõ: tránh SwiftUI tự mô tả điều hướng (navigation / 내비게이션) một lần rồi UIKit điều hướng (navigation / 내비게이션) controller lại mô tả thêm một ngăn xếp (stack / 스택) khác mà không có ranh giới (boundary / 경계).

`UIHostingConfiguration` có thể hữu ích để dùng SwiftUI content trong UIKit danh sách (list / 목록)/cell ở OS hỗ trợ, nhưng định danh (identity / 식별자)/reuse vẫn phải được hiểu theo host UIKit.

---

# 16. Interoperability data-flow quy tắc (rule / 규칙)

Hybrid mã (code / 코드) dễ hỏng khi cả UIKit và SwiftUI đều tự nhận mình là nguồn chuẩn (source of truth / 정본).

Chọn một hướng cho mỗi fact:

```text
Domain/Feature state
        ↓
SwiftUI View ----adapter----> UIKit component
        ↑                         |
        └--------- event ----------┘
```

Hoặc UIKit controller là tính năng (feature / 기능) đơn vị sở hữu (owner / 오너) và SwiftUI chỉ kết xuất (render / 렌더링) Binding/mô hình (model / 모델) được inject. Điều phải tránh là UIKit giữ một bản sao (copy / 복사) trạng thái (state / 상태), SwiftUI giữ bản sao (copy / 복사) khác và delegate cố sync hai chiều thủ công không có phiên bản (version / 버전)/bất biến (invariant / 불변식).

---

# 17. Incremental di chuyển (migration / 마이그레이션) UIKit ↔ SwiftUI

Rewrite toàn app hiếm khi là lựa chọn duy nhất. di chuyển (migration / 마이그레이션) an toàn thường theo seam:

- màn hình mới dùng SwiftUI nhưng host trong UIKit điều hướng (navigation / 내비게이션);
- thành phần (component / 컴포넌트) UIKit đặc thù được wrap vào SwiftUI;
- lĩnh vực (domain / 도메인)/mạng (network / 네트워크)/persistence tầng (layer / 계층) được tách framework-neutral trước;
- tuyến (route / 경로)/điều hướng (navigation / 내비게이션) quyền sở hữu (ownership / 소유권) được xác định để tránh hai điều hướng (navigation / 내비게이션) hệ thống (system / 시스템) tranh quyền;
- khả năng quan sát (observability / 관측 가능성)/analytics/kiểm thử (test / 테스트) được giữ tương đương trước khi xóa hiện thực (implementation / 구현) cũ.

Đo regression về khả năng tiếp cận (accessibility / 접근성), keyboard/focus, safe area, rotation, trạng thái (state / 상태) restoration và hiệu năng (performance / 성능); không chỉ screenshot happy đường dẫn (path / 경로).

---

# 18. kiến trúc (architecture / 아키텍처) môi trường vận hành (production / 운영 환경) — bắt đầu từ trạng thái (state / 상태)/tác động (effect / 효과) quyền sở hữu (ownership / 소유권)

Một kiến trúc (architecture / 아키텍처) hữu ích phải cho phép trả lời:

- nguồn chuẩn (source of truth / 정본) của tính năng (feature / 기능) là gì;
- sự kiện (event / 이벤트) nào mutate trạng thái (state / 상태);
- side tác động (effect / 효과) được khởi tạo/cancel ở đâu;
- phụ thuộc (dependency / 의존성) đi vào từ đâu;
- UI khung phần mềm (framework / 프레임워크) kiểu (type / 타입) dừng ở ranh giới (boundary / 경계) nào;
- persistence/mạng (network / 네트워크) DTO map ở đâu;
- tuyến (route / 경로)/deep link được parse ở đâu;
- kiểm thử (test / 테스트) hành vi (behavior / 동작) nào không cần launch UI.

Nếu sơ đồ tầng (layer / 계층) đẹp nhưng không trả lời được tác vụ (task / 작업) thời gian tồn tại (lifetime / 수명) và nguồn chuẩn (source of truth / 정본), kiến trúc (architecture / 아키텍처) vẫn yếu.

---

# 19. Vertical tính năng (feature / 기능) ranh giới (boundary / 경계)

Thay vì toàn app chia `Views/Models/ViewModels/Services`, tính năng (feature / 기능) có thể là compile-time/quyền sở hữu (ownership / 소유권) slice:

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

Không phải mọi dự án (project / 프로젝트) cần cấu trúc (structure / 구조) này; lợi ích là mã (code / 코드) thay đổi cùng tính năng (feature / 기능) nằm gần nhau và mô-đun (module / 모듈) API có thể nhỏ.

---

# 20. lĩnh vực (domain / 도메인)/dữ liệu (data / 데이터)/Presentation ranh giới (boundary / 경계) có chọn lọc

Lĩnh vực (domain / 도메인) mô hình (model / 모델) nên tránh phụ thuộc vận chuyển (transport / 전송)/persistence/khung phần mềm (framework / 프레임워크) kiểu (type / 타입) khi lĩnh vực (domain / 도메인) sống lâu hơn hiện thực (implementation / 구현) đó. DTO từ REST và managed đối tượng (object / 객체) có thể map sang lĩnh vực (domain / 도메인) giá trị (value / 값).

Nhưng CRUD app nhỏ có thể dùng mô hình (model / 모델) trực tiếp nếu không có lĩnh vực (domain / 도메인) distinction thật. lớp trừu tượng (abstraction / 추상화) phải trả rent: giảm coupling, tăng testability hoặc bảo vệ tính tương thích (compatibility / 호환성). Nếu chỉ forward phương thức (method / 메서드), nó tạo ceremony.

---

# 21. MVVM ở SwiftUI — dùng khi có lý do

SwiftUI `View` là lightweight description. Không cần 1 View = 1 ViewModel như luật.

ViewModel/tính năng (feature / 기능) mô hình (model / 모델) có giá trị khi:

- máy trạng thái (state machine / 상태 머신)/tác động (effect / 효과) phức tạp;
- cần MainActor quyền sở hữu (ownership / 소유권) lâu hơn cục bộ (local / 로컬) scalar trạng thái (state / 상태);
- tính năng (feature / 기능) được kiểm thử (test / 테스트) độc lập view;
- nhiều subview chia dùng chung (shared / 공유) tính năng (feature / 기능) trạng thái (state / 상태).

Massive ViewModel cũng là Massive View Controller phiên bản mới nếu nó chứa mạng (network / 네트워크), persistence, routing, analytics và mọi nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙).

---

# 22. Coordinator/Router/Reducer — chọn theo bài toán (problem / 문제)

Coordinator phù hợp UIKit điều hướng (navigation / 내비게이션) quyền sở hữu (ownership / 소유권). Router/state-driven điều hướng (navigation / 내비게이션) phù hợp SwiftUI khi tuyến (route / 경로) là dữ liệu (data / 데이터). Reducer kiến trúc (architecture / 아키텍처) phù hợp trạng thái (state / 상태)/hành động (action / 동작)/tác động (effect / 효과) phức tạp cần tường minh (explicit / 명시적) chuyển tiếp (transition / 전이)/replay/kiểm thử (test / 테스트).

Không trộn ba mẫu (pattern / 패턴) chỉ để “enterprise”. Với mỗi tầng (layer / 계층), ghi rõ responsibility và phụ thuộc (dependency / 의존성) direction.

---

# 23. phụ thuộc (dependency / 의존성) Injection và composition gốc (root / 루트)

Composition gốc (root / 루트) dựng concrete phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프). tính năng (feature / 기능) không nên tự tìm dịch vụ (service / 서비스) qua toàn cục (global / 전역) bộ chứa (container / 컨테이너) nếu phụ thuộc (dependency / 의존성) là yêu cầu (requirement / 요구사항).

Giao thức (protocol / 프로토콜) chỉ cần khi lớp trừu tượng (abstraction / 추상화)/substitution thực sự có giá trị. Closure/hàm (function / 함수) phụ thuộc (dependency / 의존성), concrete fake hoặc lightweight struct phụ thuộc (dependency / 의존성) đôi khi đơn giản hơn giao thức (protocol / 프로토콜) + mock generator.

Singleton không luôn xấu: hệ thống (system / 시스템) singleton như `URLSession.shared` có use trường hợp (case / 사례). Vấn đề là hidden mutable toàn cục (global / 전역) trạng thái (state / 상태) không kiểm soát thời gian tồn tại (lifetime / 수명)/kiểm thử (test / 테스트) isolation.

---

# 24. Modularization là phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프), không phải folder

SwiftPM mục tiêu (target / 대상)/mô-đun (module / 모듈) là compile-time ranh giới (boundary / 경계). API công khai (public API / 공개 API) phải nhỏ; helper giữ `internal`. Tránh mega-Core mà mọi tính năng (feature / 기능) import.

Theo dõi cycle và fan-in/fan-out. mô-đun (module / 모듈) quá nhỏ tạo bản dựng (build / 빌드)/phụ thuộc (dependency / 의존성) ceremony; mô-đun (module / 모듈) quá lớn mất isolation/quyền sở hữu (ownership / 소유권). Chọn seam theo nhóm (team / 팀) quyền sở hữu (ownership / 소유권), tính năng (feature / 기능) volatility, bản dựng (build / 빌드) bottleneck và reusable năng lực (capability / 역량).

Nhị phân (binary / 이진) XCFramework cần thêm concern về kiến trúc (architecture / 아키텍처) slices, mô-đun (module / 모듈) stability, signing, privacy manifest và symbols. `BUILD_LIBRARY_FOR_DISTRIBUTION` có ý nghĩa với nhị phân (binary / 이진) phân phối (distribution / 분포), không phải toggle “tối ưu app”.

---

# 25. API evolution và nội bộ (internal / 내부) gói (package / 패키지) discipline

Ngay cả gói (package / 패키지) nội bộ có nhiều bên tiêu thụ (consumer / 소비자) cũng cần ngữ nghĩa (semantic / 의미적) discipline. Breaking thay đổi (change / 변경) cần di chuyển (migration / 마이그레이션) plan; deprecation shim đôi khi rẻ hơn atomic di chuyển (migration / 마이그레이션).

```swift
@available(*, deprecated, message: "Use loadNew()")
func loadOld() { }
```

API công khai (public API / 공개 API) nên document actor/isolation yêu cầu (requirement / 요구사항), lỗi (error / 오류) ngữ nghĩa (semantics / 의미론) và availability, không chỉ parameter names.

---

# 26. hệ thống dựng (build system / 빌드 시스템) và compile-time hiệu năng (performance / 성능)

Compile thời gian (time / 시간) tăng bởi giant kết quả (result / 결과) builder expression, generic ràng buộc (constraint / 제약조건) sâu, generated mã (code / 코드) quá lớn và phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) xấu.

Cải thiện bằng cách đo bản dựng (build / 빌드) timing, chia expression hợp lý, thu nhỏ API công khai (public API / 공개 API)/mô-đun (module / 모듈) imports và tránh lớp trừu tượng (abstraction / 추상화) generic chỉ để giảm vài dòng mã (code / 코드).

Gỡ lỗi (debug / 디버그)/bản phát hành (release / 릴리스) khác tối ưu hóa (optimization / 최적화). Bug chỉ bản phát hành (release / 릴리스) có thể là race, thời gian tồn tại (lifetime / 수명) timing hoặc unsafe interop; đừng mặc định trình biên dịch (compiler / 컴파일러) bug.

Swift 6.4 dùng Swift bản dựng (build / 빌드) làm default SwiftPM hệ thống dựng (build system / 빌드 시스템); gói (package / 패키지)/bản dựng (build / 빌드) issue cần xem phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) và trình biên dịch (compiler / 컴파일러) invocation thay vì chỉ “xóa DerivedData”.

---

# 27. Instruments — workflow đo trước sửa

Các công cụ (tool / 도구) quan trọng: thời gian (time / 시간) Profiler, Allocations, Leaks, mạng (network / 네트워크), năng lượng (energy / 에너지), cốt lõi (core / 핵심) Animation/hitch và SwiftUI instrumentation tương ứng Xcode phiên bản (version / 버전).

Workflow:

1. mô tả symptom bằng chỉ số (metric / 지표);
2. tạo reproduction;
3. đo baseline;
4. tìm hot allocation/ngăn xếp lời gọi (call stack / 호출 스택)/bố cục (layout / 레이아웃)/mạng (network / 네트워크);
5. thay đổi một hypothesis;
6. đo lại trên thiết bị (device / 장치)/release-like bản dựng (build / 빌드).

Bộ nhớ (memory / 메모리) growth không đồng nghĩa leak. bộ nhớ đệm (cache / 캐시) có thể hợp lệ nhưng vẫn gây bộ nhớ (memory / 메모리) pressure; leak có thể nhỏ nhưng tăng theo repeated luồng (flow / 흐름).

---

# 28. Signpost và khả năng quan sát (observability / 관측 가능성) cục bộ (local / 로컬)

Khi một thao tác (operation / 연산) xuyên nhiều hàm (function / 함수) nhưng thời gian (time / 시간) Profiler khó nhìn nghiệp vụ (business / 비즈니스) phase, dùng OSLog signpost/Points of Interest để đo duration có tên. Đừng log payload nhạy cảm chỉ để dễ gỡ lỗi (debug / 디버그).

Hiệu năng (performance / 성능) instrumentation nên có category/subsystem rõ để CI/lab và môi trường vận hành (production / 운영 환경) telemetry cùng nói chung một vocabulary.

---

# 29. Networking môi trường vận hành (production / 운영 환경)

Máy khách (client / 클라이언트) môi trường vận hành (production / 운영 환경) cần cancellation, hết thời gian chờ (timeout / 타임아웃), HTTP ngữ nghĩa (semantics / 의미론), bộ nhớ đệm (cache / 캐시) chính sách (policy / 정책), auth single-flight, thử lại (retry / 재시도)/backoff + jitter và idempotency.

```text
request A -> 401
request B -> 401
         \-> shared refresh task
             -> token mới
             -> retry A/B theo policy
```

Certificate pinning có operational chi phí (cost / 비용): cert/key rotation và thất bại (failure / 실패) khôi phục (recovery / 복구). Chỉ dùng khi threat mô hình (model / 모델) justify, không phải checklist bảo mật (security / 보안) mặc định.

Mobile backend phải hỗ trợ (support / 지원) phiên bản (version / 버전) lag. máy khách (client / 클라이언트) tolerant decode, máy chủ (server / 서버) backward tính tương thích (compatibility / 호환성) và idempotent mutation thiết kế (design / 설계) là độ tin cậy (reliability / 신뢰성) concern chứ không riêng networking mã (code / 코드).

---

# 30. Persistence môi trường vận hành (production / 운영 환경) và cơ sở dữ liệu (database / 데이터베이스) tính đồng thời (concurrency / 동시성)

Lược đồ (schema / 스키마) là đặc tả hợp đồng (contract / 계약) lâu dài với dữ liệu người dùng (user / 사용자). kiểm thử (test / 테스트) di chuyển (migration / 마이그레이션) từ real/synthetic snapshots của các phiên bản (version / 버전) cũ, không chỉ fresh cơ sở dữ liệu (database / 데이터베이스).

SwiftData `ModelActor`/cốt lõi (core / 핵심) dữ liệu (data / 데이터) background ngữ cảnh (context / 맥락) giúp isolation, nhưng truy vấn (query / 쿼리)/chỉ mục (index / 인덱스)/data-model thiết kế (design / 설계) thường quyết định hiệu năng (performance / 성능) lớn hơn “chạy background”.

Tránh truyền mutable persistence đối tượng (object / 객체) qua actor/ngữ cảnh (context / 맥락) tùy ý. đối tượng (object / 객체) ID hoặc Sendable snapshot/giá trị (value / 값) DTO làm ranh giới (boundary / 경계) rõ hơn.

Offline-first cần outbox/thao tác (operation / 연산) hàng đợi (queue / 큐), thử lại (retry / 재시도), xung đột (conflict / 충돌) chiến lược (strategy / 전략), tombstone/delete ngữ nghĩa (semantics / 의미론) và sync cursor/phiên bản (version / 버전); bộ nhớ đệm (cache / 캐시) phản hồi (response / 응답) đơn thuần chưa phải offline-first.

---

# 31. bảo mật (security / 보안) và privacy

Không nhúng máy chủ (server / 서버) secret vào nhị phân (binary / 이진). máy khách (client / 클라이언트) không phải trust ranh giới (boundary / 경계); authorization phải enforce ở backend.

Keychain cho credential/đơn vị từ (token / 토큰); tệp (file / 파일) nhạy cảm cần dữ liệu (data / 데이터) Protection phù hợp; ATS exception phạm vi (scope / 범위) nhỏ; permission yêu cầu (request / 요청) theo ngữ cảnh (context / 맥락). Privacy manifest/disclosure và third-party SDK kiểm tra (audit / 감사) là bản phát hành (release / 릴리스) concern.

Jailbreak/gốc (root / 루트) detection chỉ tăng tín hiệu (signal / 신호)/chi phí (cost / 비용), không tạo trust tuyệt đối.

Phụ thuộc (dependency / 의존성)/SDK là supply-chain surface: kiểm maintainer, bản phát hành (release / 릴리스) cadence, transitive phụ thuộc (dependency / 의존성), privacy hành vi (behavior / 동작) và exit chiến lược (strategy / 전략).

---

# 32. khả năng tiếp cận (accessibility / 접근성), localization và adaptive UI

Cấp cao (senior / 시니어) UI phải chịu động (dynamic / 동적) kiểu (type / 타입) lớn, locale văn bản (text / 텍스트) expansion, RTL, split view/multi-window, khả năng tiếp cận (accessibility / 접근성) settings và đầu vào (input / 입력) modality phù hợp nền tảng (platform / 플랫폼).

VoiceOver ngữ nghĩa (semantic / 의미적) cây (tree / 트리) có thể khác visual cây (tree / 트리). Custom điều khiển (control / 제어) phải expose role/giá trị (value / 값)/hành động (action / 동작) đúng.

Dùng locale-aware format:

```swift
Text(price, format: .currency(code: "USD"))
```

Ngôn ngữ (language / 언어), locale, calendar và timezone là bốn concern khác nhau.

---

# 33. Testing chiến lược (strategy / 전략) môi trường vận hành (production / 운영 환경)

Đơn vị (unit / 단위) kiểm thử (test / 테스트) pure hành vi (behavior / 동작); kiểm thử tích hợp (integration test / 통합 테스트) mạng (network / 네트워크)/persistence ranh giới (boundary / 경계); UI kiểm thử (test / 테스트) trọng yếu (critical / 중요) luồng (flow / 흐름). Snapshot kiểm thử (test / 테스트) hữu ích cho regression nhưng phải quản rendering variance.

Property-based thinking phù hợp parser/serializer/di chuyển (migration / 마이그레이션): encode→decode giữ bất biến (invariant / 불변식), di chuyển (migration / 마이그레이션) giữ bản ghi (record / 레코드), sort giữ multiset/thứ tự (order / 순서) bất biến (invariant / 불변식). Fuzzing hữu ích cho untrusted/nhị phân (binary / 이진) parser ranh giới (boundary / 경계).

Tính đồng thời (concurrency / 동시성) kiểm thử (test / 테스트) phải ép cancellation/interleaving/single-flight/reentrancy, không chỉ chờ happy đường dẫn (path / 경로).

---

# 34. CI/CD và bản phát hành (release / 릴리스) sản phẩm tạo ra (artifact / 산출물)

Chuỗi xử lý (pipeline / 파이프라인) điển hình: resolve phụ thuộc (dependency / 의존성) → bản dựng (build / 빌드) → static check → đơn vị (unit / 단위)/kiểm thử tích hợp (integration test / 통합 테스트) → selected UI kiểm thử (test / 테스트) → archive → sign/export → upload TestFlight/App Store.

```bash
xcodebuild \
  -scheme MyApp \
  -destination 'platform=iOS Simulator,name=iPhone 17' \
  test
```

Quan trọng: kiểm thử (test / 테스트) gỡ lỗi (debug / 디버그) simulator chưa đủ. Với rủi ro (risk / 위험) cao, kiểm thử (test / 테스트) archive/Release-like sản phẩm tạo ra (artifact / 산출물), signing/entitlement và di chuyển (migration / 마이그레이션) install từ phiên bản (version / 버전) đang phát hành.

Không hard-code signing credential/đơn vị từ (token / 토큰) trong repo/log.

---

# 35. App startup, trạng thái (state / 상태) restoration và tiến trình (process / 프로세스) death

Startup đường dẫn (path / 경로) nên nhỏ: dựng phụ thuộc (dependency / 의존성) cần thiết, kết xuất (render / 렌더링) sớm, defer noncritical công việc (work / 작업). Static/toàn cục (global / 전역) initializer có thể chạy sớm ngoài ý định.

Trạng thái (state / 상태) restoration phải phân biệt transient UI/điều hướng (navigation / 내비게이션) và durable lĩnh vực (domain / 도메인) dữ liệu (data / 데이터). iOS có thể terminate tiến trình (process / 프로세스) bất ngờ; dữ liệu quan trọng phải được persisted theo giao dịch (transaction / 트랜잭션) phù hợp, không chờ callback “sắp terminate”.

---

# 36. Combine và legacy async ranh giới (boundary / 경계)

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

Nếu `self` giữ cancellables và sink closure strong-capture `self`, hãy xem retain đồ thị (graph / 그래프). Đặt ranh giới (boundary / 경계) rõ khi cầu nối (bridge / 브리지) Combine ↔ async/await; đừng chuyển qua lại nhiều lần trong cùng tính năng (feature / 기능).

---

# 37. Objective-C thời gian chạy (runtime / 런타임) interoperability

`NSObject`, `@objc`, `dynamic`, selector, KVC/KVO vẫn xuất hiện ở UIKit/legacy SDK. Không phải mọi Swift kiểu (type / 타입) expose sang Objective-C được; generic Swift và enum associated giá trị (value / 값) là ví dụ.

Mixed-language app dùng bridging header/mô-đun (module / 모듈) import tùy hướng. thời gian chạy (runtime / 런타임) động (dynamic / 동적) tính năng (feature / 기능) có sự đánh đổi (trade-off / 트레이드오프): ít static checking hơn, hành vi (behavior / 동작) phụ thuộc selector/KVC key và Objective-C thời gian tồn tại (lifetime / 수명) conventions.

---

# 38. C/C++ ranh giới (boundary / 경계)

Pointer/count API là unsafe ranh giới (boundary / 경계); thời gian tồn tại (lifetime / 수명), alignment, mutability và quyền sở hữu (ownership / 소유권) phải document. Swift 6.x tiếp tục thêm memory-safe các hệ thống (systems / 시스템들) API như `Span` và Swift 6.4 mở rộng interop với C++20 `std::span`.

Giữ foreign/unsafe adapter nhỏ; convert sang Swift-safe giá trị (value / 값) càng sớm càng tốt. Parser nhị phân (binary / 이진)/untrusted đầu vào (input / 입력) cần bounds kiểm tra hợp lệ (validation / 검증)/fuzzing.

---

# 39. Xcode 27 / Swift 6.4 di chuyển (migration / 마이그레이션) rủi ro (risk / 위험)

Xcode 27 + Swift 6.4 là baseline hiện tại của thư viện (library / 라이브러리). SwiftUI trạng thái (state / 상태)/builder internals và observation/tooling tiếp tục tiến hóa; mã (code / 코드) không nên phụ thuộc undocumented reflection/result-builder hiện thực (implementation / 구현).

Swift 6.4 tiếp tục mở rộng quyền sở hữu (ownership / 소유권), interop, testing và bản dựng (build / 빌드) tooling. cấp cao (senior / 시니어) adoption chiến lược (strategy / 전략) là đọc bản phát hành (release / 릴리스) notes + Swift Evolution proposal liên quan, chạy di chuyển (migration / 마이그레이션)/kiểm thử (test / 테스트)/hiệu năng (performance / 성능) baseline, rồi bật tính năng (feature / 기능) có chủ đích. “trình biên dịch (compiler / 컴파일러) mới nên bật mọi thứ cùng lúc” không phải di chuyển (migration / 마이그레이션) plan.

---

# 40. sự cố (incident / 인시던트) mindset và quay lui (rollback / 롤백) ràng buộc (constraint / 제약조건) của mobile

Khi crash/độ trễ (latency / 지연 시간) tăng, phân đoạn theo app phiên bản (version / 버전), OS, thiết bị (device / 장치), cờ tính năng (feature flag / 기능 플래그), endpoint; xem symbolicated ngăn xếp (stack / 스택)/chỉ số (metric / 지표)/log; reproduce nhỏ nhất; rồi patch.

Mobile quay lui (rollback / 롤백) chậm hơn web vì nhị phân (binary / 이진) cũ nằm trên thiết bị (device / 장치). Backend backward tính tương thích (compatibility / 호환성), remote kill switch/cờ tính năng (feature flag / 기능 플래그) cho rủi ro (risk / 위험) cao và staged rollout giúp giảm blast radius. Flag phải có đơn vị sở hữu (owner / 오너)/expiry; không để codebase thành tổ hợp hàng chục flag vĩnh viễn.

---

# 41. cấp cao (senior / 시니어) rà soát (review / 검토) checklist

Rà soát (review / 검토) ngữ nghĩa (semantics / 의미론) trước style:

- trạng thái (state / 상태)/nguồn chuẩn (source of truth / 정본) có một đơn vị sở hữu (owner / 오너) rõ không;
- closure/tham chiếu (reference / 참조) đồ thị (graph / 그래프) có cycle/thời gian tồn tại (lifetime / 수명) bất thường không;
- tác vụ (task / 작업) có đơn vị sở hữu (owner / 오너)/cancellation chính sách (policy / 정책) không;
- bất biến (invariant / 불변식) có bị giữ qua `await` mà không revalidate không;
- Sendable/isolation annotation có phản ánh quyền sở hữu (ownership / 소유권) thật không;
- SwiftUI định danh (identity / 식별자) có ổn định không;
- UIKit vòng đời (lifecycle / 생명주기) callback có dùng đúng responsibility không;
- containment/representable/hosting quyền sở hữu (ownership / 소유권) có cleanup đúng không;
- mạng (network / 네트워크) mutation có thử lại (retry / 재시도)/idempotency rủi ro (risk / 위험) không;
- persistence di chuyển (migration / 마이그레이션)/ngữ cảnh (context / 맥락) ranh giới (boundary / 경계) có kiểm thử (test / 테스트) không;
- API availability/backward tính tương thích (compatibility / 호환성) có fallback không;
- bảo mật (security / 보안)/privacy/logging có leak secret/PII không;
- hiệu năng (performance / 성능) claim có đo lường (measurement / 측정) không;
- bản phát hành (release / 릴리스) sản phẩm tạo ra (artifact / 산출물)/di chuyển (migration / 마이그레이션) đường dẫn (path / 경로) có được kiểm thử (test / 테스트) không.

Nếu reviewer phải mất rất lâu mới xác định trạng thái (state / 상태)/tác động (effect / 효과)/phụ thuộc (dependency / 의존성) luồng (flow / 흐름), mã (code / 코드) có thể compile nhưng kiến trúc (architecture / 아키텍처) chưa đạt mức cấp cao (senior / 시니어) maintainability.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Swift & iOS Master ghi chú (note / 노트) — Advanced / cấp cao (senior / 시니어)**, **Gate trước khi sang Master** nối từ **7.3 Trait và adaptive UI** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Gate trước khi sang Master

Bạn phải có khả năng lấy một hybrid app SwiftUI + UIKit thật và vẽ được: object ownership graph, view/controller lifecycle, task graph, actor/isolation boundary, state source-of-truth, network/persistence boundary và module dependency graph. Master sẽ không dạy lại các graph này; nó dùng chúng để giải quyết version evolution, ABI/library evolution, large-scale reliability, performance/security/release governance.

> **Bàn giao:** Sau **Gate trước khi sang Master**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
