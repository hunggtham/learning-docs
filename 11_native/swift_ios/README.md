# Swift & iOS thư viện kiến thức (knowledge library / 지식 라이브러리)

> **Mạch đọc:** Đọc **Swift & iOS thư viện kiến thức (knowledge library / 지식 라이브러리)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Baseline phiên bản (version / 버전) — cập nhật 21/09/2026** sang **chuẩn gốc (canonical / 정본) lộ trình học (learning path / 학습 경로)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Bộ tài liệu này là lộ trình chuẩn gốc (canonical / 정본) để học Swift và iOS từ gần như số 0 đến mức có thể quyền sở hữu (ownership / 소유권) một hệ thống môi trường vận hành (production / 운영 환경). Đây không phải cheat sheet. Mỗi mức (level / 수준) cố gắng giải thích theo mạch: khái niệm là gì → vì sao tồn tại → hoạt động thế nào → khi nào dùng → cách dùng → lỗi/trường hợp biên (edge case / 경계 사례) → cách người có kinh nghiệm sử dụng trong môi trường vận hành (production / 운영 환경).

## Baseline phiên bản (version / 버전) — cập nhật 21/09/2026

Baseline stable hiện hành là **Xcode 27 + Swift 6.4 + iOS 27 SDK**. Swift 6.4 đã phát hành chính thức ngày 15/09/2026. Xcode 27.1/27.2 vẫn đang ở beta tại thời điểm cập nhật nên không được dùng làm baseline stable của thư viện (library / 라이브러리).

Tài liệu vẫn giữ kiến thức Swift 5.x, UIKit, Combine, cốt lõi (core / 핵심) dữ liệu (data / 데이터) và Objective-C interoperability ở những nơi cần thiết để đọc, migrate và maintain codebase môi trường vận hành (production / 운영 환경) nhiều thế hệ.


> **Chuyển mạch:** Từ **Baseline phiên bản (version / 버전) — cập nhật 21/09/2026**, ta sang **chuẩn gốc (canonical / 정본) lộ trình học (learning path / 학습 경로)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Chuẩn gốc (canonical / 정본) lộ trình học (learning path / 학습 경로)

Lộ trình bắt buộc là:

**01 Beginner → 02 Intermediate → 03 Advanced / cấp cao (senior / 시니어) → 04 Master**

`05_swift_ios_production_reference.md` không phải mức (level / 수준) 5 và không thay thế bốn tệp (file / 파일) chuẩn gốc (canonical / 정본). Nó là tài liệu tra cứu xuyên cấp sau khi đã có mô hình tư duy (mental model / 사고 모델) từ 01–04.

### 1. [Beginner](01_swift_ios_beginner.md)

Beginner xây nền ngữ nghĩa (semantics / 의미론). Nội dung đi từ Swift/Xcode/phiên bản (version / 버전) axes, giá trị (value / 값)/hệ kiểu (type system / 타입 시스템), String/collection, điều khiển (control / 제어) luồng (flow / 흐름), hàm (function / 함수)/parameter, Optional, struct/lớp (class / 클래스)/enum/giao thức (protocol / 프로토콜), initialization, properties/kiểm soát truy cập (access control / 접근 제어), closure thời gian tồn tại (lifetime / 수명), ARC/bộ nhớ (memory / 메모리) quyền sở hữu (ownership / 소유권), lỗi (error / 오류)/generics/Foundation đến SwiftUI, quyền sở hữu trạng thái (state ownership / 상태 소유권), điều hướng (navigation / 내비게이션), URLSession, tính đồng thời (concurrency / 동시성) nhập môn, persistence, UIKit vòng đời (lifecycle / 생명주기), UIKit ↔ SwiftUI interoperability, testing, SwiftPM và signing.

Phần quan trọng nhất không phải thuộc cú pháp (syntax / 문법) mà là hiểu `struct` khác `class` ở ngữ nghĩa (semantics / 의미론) nào, closure escaping ảnh hưởng thời gian tồn tại (lifetime / 수명) ra sao, retain cycle hình thành thế nào, `await` là suspension chứ không phải “background luồng thực thi (thread / 스레드)”, `@State` sở hữu trạng thái (state / 상태) ra sao và UIKit controller vòng đời (lifecycle / 생명주기) khác app/scene vòng đời (lifecycle / 생명주기) như thế nào.

#### Gate Beginner → Intermediate

Chỉ nên chuyển sang Intermediate khi bạn giải thích được giá trị (value / 값)/tham chiếu (reference / 참조) ngữ nghĩa (semantics / 의미론), Optional, closure capture, strong/weak/unowned, ARC vs dữ liệu (data / 데이터) race, tác vụ (task / 작업) cancellation cơ bản, nguồn chuẩn (source of truth / 정본) của `@State`/`@Binding`, chuỗi (sequence / 시퀀스) cơ bản của `UIViewController`, triển khai (deployment / 배포) mục tiêu (target / 대상) khác SDK/trình biên dịch (compiler / 컴파일러) phiên bản (version / 버전), và có thể dùng breakpoint/kiểm thử (test / 테스트)/bộ nhớ (memory / 메모리) đồ thị (graph / 그래프) để kiểm chứng giả định (assumption / 가정).

### 2. [Intermediate](02_swift_ios_intermediate.md)

Intermediate xây quyền sở hữu (ownership / 소유권) và isolation ở mức tính năng (feature / 기능). Nội dung đi sâu generics/existentials, structured tính đồng thời (concurrency / 동시성), `Task`, cancellation, actor isolation, reentrancy, `@MainActor`, `Sendable`/`@Sendable`, AsyncSequence/continuation, SwiftUI trạng thái (state / 상태) với `@State`, `@Binding`, `@Observable`, `@Bindable`, môi trường (environment / 환경), view định danh (identity / 식별자) và `.task(id:)`, rồi nối sang điều hướng (navigation / 내비게이션), networking, thử lại (retry / 재시도)/idempotency/auth refresh, Codable ranh giới (boundary / 경계), SwiftData/cốt lõi (core / 핵심) dữ liệu (data / 데이터) ngữ cảnh (context / 맥락), phụ thuộc (dependency / 의존성) injection, kiến trúc (architecture / 아키텍처), UIKit interoperability, background công việc (work / 작업), testing, diagnostics và ranh giới mô-đun (module boundary / 모듈 경계).

#### Gate Intermediate → Advanced / cấp cao (senior / 시니어)

Bạn cần nhìn một tính năng (feature / 기능) và chỉ ra được tác vụ (task / 작업) đơn vị sở hữu (owner / 오너), cancellation chính sách (policy / 정책), actor/isolation ranh giới (boundary / 경계), dữ liệu crossing ranh giới (boundary / 경계) và Sendable ngữ nghĩa (semantics / 의미론), SwiftUI nguồn chuẩn (source of truth / 정본), view định danh (identity / 식별자), mạng (network / 네트워크)/persistence ranh giới (boundary / 경계), phụ thuộc (dependency / 의존성) nguồn (source / 소스) và kiểm thử (test / 테스트) điểm (point / 지점). Nếu trình biên dịch (compiler / 컴파일러) tính đồng thời (concurrency / 동시성) warning chỉ được sửa bằng annotation mà không giải thích được quyền sở hữu (ownership / 소유권) trước/sau, chưa nên sang Advanced.

### 3. [Advanced / Senior](03_swift_ios_advanced_senior.md)

Advanced/cấp cao (senior / 시니어) chuyển từ tính năng (feature / 기능) tính đúng đắn (correctness / 정확성) sang môi trường vận hành (production / 운영 환경) hiện thực (implementation / 구현). Phần này đào sâu quyền sở hữu (ownership / 소유권)/tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명), Swift tính đồng thời (concurrency / 동시성) bất biến (invariant / 불변식), SwiftUI rendering/hiệu năng (performance / 성능), UIKit vòng đời (lifecycle / 생명주기) đầy đủ, custom containment, điều hướng (navigation / 내비게이션)/presentation, scene/multi-window, collection reuse, bộ nhớ (memory / 메모리) traps, Representable vòng đời (lifecycle / 생명주기), Coordinator, `UIHostingController`, hybrid source-of-truth, incremental UIKit ↔ SwiftUI di chuyển (migration / 마이그레이션), kiến trúc (architecture / 아키텍처) theo trạng thái (state / 상태)/tác động (effect / 효과) quyền sở hữu (ownership / 소유권), modularization, API evolution, Instruments, networking/persistence độ tin cậy (reliability / 신뢰성), bảo mật (security / 보안)/privacy, testing, CI/CD và sự cố (incident / 인시던트) handling.

#### Gate Advanced / cấp cao (senior / 시니어) → Master

Bạn phải có khả năng vẽ được cho một app hybrid thật: đối tượng (object / 객체) quyền sở hữu (ownership / 소유권) đồ thị (graph / 그래프), view/controller vòng đời (lifecycle / 생명주기), tác vụ (task / 작업) đồ thị (graph / 그래프), actor/isolation ranh giới (boundary / 경계), SwiftUI quyền sở hữu trạng thái (state ownership / 상태 소유권), mạng (network / 네트워크)/persistence ranh giới (boundary / 경계) và mô-đun (module / 모듈) phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프). Bạn cũng phải biết đo hiệu năng (performance / 성능) bằng công cụ (tool / 도구), phân tích retain đường dẫn (path / 경로), kiểm thử (test / 테스트) di chuyển (migration / 마이그레이션)/bản phát hành (release / 릴리스) sản phẩm tạo ra (artifact / 산출물) và giải thích quay lui (rollback / 롤백) ràng buộc (constraint / 제약조건) của mobile.

### 4. [Master](04_swift_ios_master.md)

Master tập trung vào longevity của hệ thống. Nội dung giải thích evolution Swift/iOS theo tác động đến programming mô hình (model / 모델), từ Swift 1–3, Codable/Swift 4, ABI/Swift 5, SwiftUI/Combine, async/await/actors, macros/Observation/SwiftData, Swift 6 data-race an toàn (safety / 안전), Swift 6.2 approachable tính đồng thời (concurrency / 동시성) đến Swift 6.4 quyền sở hữu (ownership / 소유권)/bản dựng (build / 빌드) evolution.

Từ đó tài liệu đi vào version-support chính sách (policy / 정책), Swift 5 → 6.x di chuyển (migration / 마이그레이션), nguồn (source / 소스)/nhị phân (binary / 이진)/API tính tương thích (compatibility / 호환성), lược đồ (schema / 스키마) di chuyển (migration / 마이그레이션), offline sync, phân tán (distributed / 분산) mobile versioning, HTTP resilience, large-scale kiến trúc (architecture / 아키텍처), ADR, khả năng quan sát (observability / 관측 가능성), hiệu năng (performance / 성능)/năng lượng (energy / 에너지) budgets, threat modeling, privacy/supply-chain, App Extensions, StoreKit, bản phát hành (release / 릴리스) artifacts, staged rollout, quay lui (rollback / 롤백) và disaster khôi phục (recovery / 복구).

#### Completion mục tiêu (target / 대상)

Sau Master, mục tiêu không phải “thuộc toàn bộ Apple SDK”. Bạn phải có mô hình tư duy (mental model / 사고 모델) đủ mạnh để khi Swift/Xcode/iOS thay đổi, có thể xác định cái gì thực sự đổi, ranh giới (boundary / 경계) nào bị ảnh hưởng, di chuyển (migration / 마이그레이션)/kiểm thử (test / 테스트) nào cần chạy và bản phát hành (release / 릴리스) thế nào để không biến môi trường vận hành (production / 운영 환경) người dùng (user / 사용자) thành di chuyển (migration / 마이그레이션) kiểm thử (test / 테스트).


> **Chuyển mạch:** Từ **chuẩn gốc (canonical / 정본) lộ trình học (learning path / 학습 경로)**, ta sang **môi trường vận hành (production / 운영 환경) tham chiếu (reference / 참조) — không phải mức (level / 수준) tiếp theo** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Môi trường vận hành (production / 운영 환경) tham chiếu (reference / 참조) — không phải mức (level / 수준) tiếp theo

### [Production Reference & Completion Guide](05_swift_ios_production_reference.md)

Dùng tệp (file / 파일) này sau Master hoặc khi cần tra cứu một dạng thất bại (failure mode / 실패 모드) xuyên cấp. Nó gom closure thời gian tồn tại (lifetime / 수명)/`@Sendable`, numeric tính đúng đắn (correctness / 정확성), HTTP ngữ nghĩa (semantics / 의미론), tolerant decoding, thử lại (retry / 재시도)/backoff/idempotency, cốt lõi (core / 핵심) dữ liệu (data / 데이터) legacy, background transfer, quyền sở hữu (ownership / 소유권) APIs mới, generated mã (code / 코드), khả năng quan sát (observability / 관측 가능성), bộ nhớ (memory / 메모리) đồ thị (graph / 그래프), extension tiến trình (process / 프로세스) ranh giới (boundary / 경계), supply-chain bảo mật (security / 보안), ADR/phiên bản (version / 버전) ma trận (matrix / 행렬), disaster khôi phục (recovery / 복구), release-artifact testing và Definition of Done theo rủi ro (risk / 위험).

Không đọc 05 thay cho 01–04. tham chiếu (reference / 참조) cố tình cross-cutting và giả định bạn đã có vocabulary về quyền sở hữu (ownership / 소유권), isolation, trạng thái (state / 상태), vòng đời (lifecycle / 생명주기) và tính tương thích (compatibility / 호환성).


> **Chuyển mạch:** Từ **môi trường vận hành (production / 운영 환경) tham chiếu (reference / 참조) — không phải mức (level / 수준) tiếp theo**, ta sang **Những phụ thuộc (dependency / 의존성) kiến thức không nên bỏ qua** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Những phụ thuộc (dependency / 의존성) kiến thức không nên bỏ qua

**ARC trước tính đồng thời (concurrency / 동시성).** Nếu chưa phân biệt đối tượng (object / 객체) thời gian tồn tại (lifetime / 수명) với synchronized truy cập (access / 접근), bạn dễ nhầm retain cycle với dữ liệu (data / 데이터) race hoặc dùng actor như công cụ quản bộ nhớ (memory / 메모리).

**tác vụ (task / 작업)/isolation trước kiến trúc (architecture / 아키텍처).** kiến trúc (architecture / 아키텍처) diagram không có giá trị nếu không chỉ ra async tác động (effect / 효과) sống ở đâu, ai cancel và mutable trạng thái (state / 상태) thuộc isolation nào.

**SwiftUI trạng thái (state / 상태) trước hiệu năng (performance / 성능).** Tối ưu rendering khi định danh (identity / 식별자)/nguồn chuẩn (source of truth / 정본) còn sai thường chỉ che bug.

**UIKit vòng đời (lifecycle / 생명주기) trước hybrid di chuyển (migration / 마이그레이션).** Representable/HostingController chỉ dễ hiểu khi bạn đã nắm vòng đời (lifecycle / 생명주기) và quyền sở hữu (ownership / 소유권) của hai khung phần mềm (framework / 프레임워크).

**môi trường vận hành (production / 운영 환경) hiện thực (implementation / 구현) trước phiên bản (version / 버전) quản trị (governance / 거버넌스).** Master giả định bạn đã biết hiện thực (implementation / 구현) hoạt động; lúc đó mới đánh giá di chuyển (migration / 마이그레이션), tính tương thích (compatibility / 호환성), rollout và khôi phục (recovery / 복구) có ý nghĩa.


> **Chuyển mạch:** Từ **Những phụ thuộc (dependency / 의존성) kiến thức không nên bỏ qua**, ta sang **phiên bản (version / 버전) principles** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Phiên bản (version / 버전) principles

Luôn tách **Xcode phiên bản (version / 버전)**, **Swift trình biên dịch (compiler / 컴파일러) phiên bản (version / 버전)**, **Swift ngôn ngữ (language / 언어) chế độ (mode / 모드)**, **SDK phiên bản (version / 버전)** và **triển khai (deployment / 배포) mục tiêu (target / 대상)**. Một API trình biên dịch (compiler / 컴파일러) biết chưa chắc chạy được trên triển khai (deployment / 배포) mục tiêu (target / 대상) cũ.

Thời gian chạy (runtime / 런타임) availability dùng `#available`; compile-time nguồn (source / 소스)/nền tảng (platform / 플랫폼) selection dùng `#if`, `canImport`, `os(...)` hoặc mục tiêu (target / 대상) môi trường (environment / 환경) phù hợp. Với gói (package / 패키지)/thư viện (library / 라이브러리), còn phải theo dõi `swift-tools-version`, phụ thuộc (dependency / 의존성) phiên bản (version / 버전) và API công khai (public API / 공개 API) availability.

Khi tài liệu/blog cũ mâu thuẫn hành vi (behavior / 동작) của toolchain đang dùng, ưu tiên Swift.org/Swift Evolution, Apple nhà phát triển (developer / 개발자) Documentation và Xcode bản phát hành (release / 릴리스) notes chính thức.


> **Chuyển mạch:** Từ **phiên bản (version / 버전) principles**, ta sang **dự án (project / 프로젝트) progression đề xuất** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dự án (project / 프로젝트) progression đề xuất

Ở Beginner, xây một Reading danh sách (list / 목록) để nối ngôn ngữ (language / 언어) → ARC → UI → async → persistence. Ở Intermediate, mở rộng thành danh mục (catalog / 카탈로그)/tìm kiếm (search / 검색) có cancellation, auth mock, pagination, bộ nhớ đệm (cache / 캐시) và deep link. Ở Advanced/cấp cao (senior / 시니어), refactor app đó thành hybrid/mô-đun (module / 모듈) rõ, dùng Instruments, di chuyển (migration / 마이그레이션) kiểm thử (test / 테스트) và CI/CD. Ở Master, giả lập nâng Swift/Xcode/minimum iOS, thay backend/lược đồ (schema / 스키마), rollout cờ tính năng (feature flag / 기능 플래그) và viết ADR/quay lui (rollback / 롤백) plan.

Cách học này biến bốn tệp (file / 파일) thành một hệ thống liên tục thay vì bốn tập kiến thức độc lập.

> **Bàn giao:** Sau **dự án (project / 프로젝트) progression đề xuất**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 INDEX](./00_INDEX.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
