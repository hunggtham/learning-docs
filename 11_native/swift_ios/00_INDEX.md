# Swift & iOS thư viện kiến thức (knowledge library / 지식 라이브러리) — chỉ mục (index / 인덱스)

> **Mạch đọc:** [README](./README.md) là owner của **Swift & iOS thư viện kiến thức (knowledge library / 지식 라이브러리) — chỉ mục (index / 인덱스)**; hãy chốt **Baseline — 21/09/2026** trước khi chọn tài liệu. Từ đó đi theo owner path **1. Beginner → 2. Intermediate → 3. Advanced / Senior → 4. Master**, rồi dùng production reference để kiểm tra các giới hạn xuyên cấp; index này giữ vai trò định tuyến, không thay thế nội dung của từng chặng.

Chuẩn gốc (canonical / 정본) lộ trình học (learning path / 학습 경로) của bộ Swift/iOS là:

**01 Beginner → 02 Intermediate → 03 Advanced / cấp cao (senior / 시니어) → 04 Master**

`05_swift_ios_production_reference.md` là tham chiếu (reference / 참조) xuyên cấp sau Master hoặc dùng để tra cứu dạng thất bại (failure mode / 실패 모드) môi trường vận hành (production / 운영 환경); nó **không phải mức (level / 수준) 5** và không thay thế bốn tệp (file / 파일) chuẩn gốc (canonical / 정본).

## Baseline — 21/09/2026

Baseline stable: **Xcode 27 + Swift 6.4 + iOS 27 SDK**. Swift 6.4 phát hành chính thức ngày 15/09/2026. Xcode 27.1/27.2 vẫn ở beta tại thời điểm cập nhật nên không được coi là baseline stable.

Thư viện (library / 라이브러리) vẫn giữ Swift 5.x, UIKit, Combine, cốt lõi (core / 핵심) dữ liệu (data / 데이터) và Objective-C interoperability khi chúng cần thiết để đọc/migrate môi trường vận hành (production / 운영 환경) codebase.

> **Nối mạch:** Baseline cố định toolchain và deployment context; từ đó Beginner đặt vocabulary, còn Intermediate mở rộng ownership và runtime reasoning.

## 1. [Beginner](01_swift_ios_beginner.md)

Nền ngữ nghĩa (semantics / 의미론): Swift/Xcode/phiên bản (version / 버전) axes, values/types, Unicode/collection, điều khiển (control / 제어) luồng (flow / 흐름), hàm (function / 함수)/`inout`, Optional, struct/lớp (class / 클래스)/enum/giao thức (protocol / 프로토콜), initialization, properties, closure thời gian tồn tại (lifetime / 수명), ARC/bộ nhớ (memory / 메모리), lỗi (error / 오류)/generic/Foundation, SwiftUI, quyền sở hữu trạng thái (state ownership / 상태 소유권), điều hướng (navigation / 내비게이션), networking, tính đồng thời (concurrency / 동시성) nhập môn, persistence, UIKit vòng đời (lifecycle / 생명주기), interoperability, testing, SwiftPM và signing.

**Gate:** phải giải thích được giá trị (value / 값)/tham chiếu (reference / 참조) ngữ nghĩa (semantics / 의미론), escaping capture, retain cycle, `weak`/`unowned`, ARC khác dữ liệu (data / 데이터) race, `await` là suspension, `@State`/`@Binding` quyền sở hữu (ownership / 소유권), UIKit vòng đời (lifecycle / 생명주기) cơ bản và triển khai (deployment / 배포) mục tiêu (target / 대상) khác SDK/trình biên dịch (compiler / 컴파일러).

> **Nối mạch:** Beginner đặt vocabulary và ownership nền; Intermediate tiếp theo mở rộng value semantics, concurrency và API contracts trước khi đi vào Advanced/Senior.

## 2. [Intermediate](02_swift_ios_intermediate.md)

Tính năng (feature / 기능) quyền sở hữu (ownership / 소유권)/isolation: generics/existentials, structured tác vụ (task / 작업), `Task`, cancellation, actor/reentrancy, `@MainActor`, `Sendable`/`@Sendable`, AsyncSequence/continuation, `@State`/`@Binding`/`@Observable`/`@Bindable`, môi trường (environment / 환경), định danh (identity / 식별자), `.task(id:)`, networking/thử lại (retry / 재시도)/idempotency/auth, Codable ranh giới (boundary / 경계), SwiftData/cốt lõi (core / 핵심) dữ liệu (data / 데이터) ngữ cảnh (context / 맥락), DI, kiến trúc (architecture / 아키텍처), UIKit cầu nối (bridge / 브리지), background công việc (work / 작업), deterministic kiểm thử (test / 테스트) và ranh giới mô-đun (module boundary / 모듈 경계).

**Gate:** phải chỉ được tác vụ (task / 작업) đơn vị sở hữu (owner / 오너)/cancellation, isolation ranh giới (boundary / 경계), Sendable crossing, SwiftUI nguồn chuẩn (source of truth / 정본)/định danh (identity / 식별자), mạng (network / 네트워크)/persistence ranh giới (boundary / 경계), phụ thuộc (dependency / 의존성) nguồn (source / 소스) và kiểm thử (test / 테스트) điểm (point / 지점) của một tính năng (feature / 기능) thật.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Swift & iOS thư viện kiến thức (knowledge library / 지식 라이브러리) — chỉ mục (index / 인덱스)**, **3. Advanced / Senior** nối từ **2. Intermediate** sang **4. Master**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. [Advanced / Senior](03_swift_ios_advanced_senior.md)

Môi trường vận hành (production / 운영 환경) hiện thực (implementation / 구현): quyền sở hữu (ownership / 소유권)/tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명), advanced tính đồng thời (concurrency / 동시성) bất biến (invariant / 불변식), SwiftUI rendering/hiệu năng (performance / 성능), UIKit vòng đời (lifecycle / 생명주기) đầy đủ, containment/điều hướng (navigation / 내비게이션)/scene/reuse, bộ nhớ (memory / 메모리) traps, Representable/Coordinator/HostingController, hybrid source-of-truth, di chuyển (migration / 마이그레이션) UIKit ↔ SwiftUI, kiến trúc (architecture / 아키텍처)/mô-đun (module / 모듈) đồ thị (graph / 그래프), API evolution, Instruments, resilient mạng (network / 네트워크)/persistence, bảo mật (security / 보안)/privacy, CI/CD và sự cố (incident / 인시던트) handling.

**Gate:** phải vẽ được quyền sở hữu (ownership / 소유권) đồ thị (graph / 그래프), UIKit/SwiftUI vòng đời (lifecycle / 생명주기), tác vụ (task / 작업)/isolation đồ thị (graph / 그래프), trạng thái (state / 상태) source-of-truth, dữ liệu (data / 데이터) ranh giới (boundary / 경계) và mô-đun (module / 모듈) phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프); đồng thời biết profile, kiểm thử (test / 테스트) di chuyển (migration / 마이그레이션)/bản phát hành (release / 릴리스) sản phẩm tạo ra (artifact / 산출물) và phân tích quay lui (rollback / 롤백) rủi ro (risk / 위험).

> **Nối mạch:** Advanced/Senior nối runtime ownership và concurrency; Master tổng hợp evolution/architecture, rồi Production Reference chuyển mental model đó thành release và operations guidance.

## 4. [Master](04_swift_ios_master.md)

Hệ thống (system / 시스템) longevity: Swift/iOS evolution theo programming mô hình (model / 모델); Swift 5 → 6.x di chuyển (migration / 마이그레이션); nguồn (source / 소스)/nhị phân (binary / 이진)/API tính tương thích (compatibility / 호환성); persistence lược đồ (schema / 스키마) và phân tán (distributed / 분산) mobile versioning; offline sync; HTTP resilience; kiến trúc (architecture / 아키텍처) quản trị (governance / 거버넌스)/ADR; khả năng quan sát (observability / 관측 가능성); hiệu năng (performance / 성능)/năng lượng (energy / 에너지) ngân sách (budget / 예산); threat mô hình (model / 모델)/privacy/supply-chain; extension/StoreKit/hệ thống (system / 시스템) tích hợp (integration / 통합); bản phát hành (release / 릴리스) artifacts, staged rollout, quay lui (rollback / 롤백) và disaster khôi phục (recovery / 복구).

**Completion mục tiêu (target / 대상):** khi toolchain/khung phần mềm (framework / 프레임워크) mới xuất hiện, có thể xác định thay đổi (change / 변경) thuộc trình biên dịch (compiler / 컴파일러)/ngôn ngữ (language / 언어)/SDK/thời gian chạy (runtime / 런타임) nào, ranh giới (boundary / 경계) nào bị ảnh hưởng, kiểm thử (test / 테스트)/di chuyển (migration / 마이그레이션) nào cần chạy và rollout/khôi phục (recovery / 복구) như thế nào.

> **Nối mạch:** Ở chặng này của **Swift & iOS thư viện kiến thức (knowledge library / 지식 라이브러리) — chỉ mục (index / 인덱스)**, sau nội dung của **4. Master**, **Production Reference** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Phụ thuộc (dependency / 의존성) rules của mạch học (learning flow / 학습 흐름)** mở rộng hệ quả hoặc giới hạn liên quan.

## [Production Reference](05_swift_ios_production_reference.md)

Tham chiếu (reference / 참조) xuyên cấp cho các chủ đề hay xuất hiện khi gỡ lỗi (debug / 디버그)/môi trường vận hành (production / 운영 환경) kiểm tra (audit / 감사): closure thời gian tồn tại (lifetime / 수명), numeric tính đúng đắn (correctness / 정확성), HTTP ngữ nghĩa (semantics / 의미론), tolerant decoding, thử lại (retry / 재시도)/backoff/idempotency, cốt lõi (core / 핵심) dữ liệu (data / 데이터) legacy, background transfer, quyền sở hữu (ownership / 소유권) APIs mới, generated mã (code / 코드), khả năng quan sát (observability / 관측 가능성)/bộ nhớ (memory / 메모리) đồ thị (graph / 그래프), extension tiến trình (process / 프로세스) ranh giới (boundary / 경계), supply-chain, ADR/phiên bản (version / 버전) ma trận (matrix / 행렬), disaster khôi phục (recovery / 복구), bản phát hành (release / 릴리스) sản phẩm tạo ra (artifact / 산출물) testing và risk-based Definition of Done.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Swift & iOS thư viện kiến thức (knowledge library / 지식 라이브러리) — chỉ mục (index / 인덱스)**, **Production Reference** đặt đầu vào cho **Phụ thuộc (dependency / 의존성) rules của mạch học (learning flow / 학습 흐름)**, rồi **Phiên bản (version / 버전) quy tắc (rule / 규칙)** mở rộng hệ quả hoặc giới hạn liên quan.

## Phụ thuộc (dependency / 의존성) rules của mạch học (learning flow / 학습 흐름)

Không bỏ ARC để nhảy thẳng tính đồng thời (concurrency / 동시성); không bỏ tác vụ (task / 작업)/isolation để nhảy thẳng kiến trúc (architecture / 아키텍처); không tối ưu SwiftUI khi source-of-truth/định danh (identity / 식별자) còn sai; không làm hybrid SwiftUI/UIKit khi vòng đời (lifecycle / 생명주기) UIKit chưa chắc; không học phiên bản (version / 버전)/bản phát hành (release / 릴리스) quản trị (governance / 거버넌스) trước khi hiểu môi trường vận hành (production / 운영 환경) hiện thực (implementation / 구현).

> **Nối mạch:** Trong **Swift & iOS thư viện kiến thức (knowledge library / 지식 라이브러리) — chỉ mục (index / 인덱스)**, **Phụ thuộc (dependency / 의존성) rules của mạch học (learning flow / 학습 흐름)** xác định đầu vào; **Phiên bản (version / 버전) quy tắc (rule / 규칙)** giải thích bước vận hành tạo ra kết quả kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Phiên bản (version / 버전) quy tắc (rule / 규칙)

Luôn tách **Xcode phiên bản (version / 버전)**, **Swift trình biên dịch (compiler / 컴파일러)**, **Swift ngôn ngữ (language / 언어) chế độ (mode / 모드)**, **SDK phiên bản (version / 버전)** và **triển khai (deployment / 배포) mục tiêu (target / 대상)**. thời gian chạy (runtime / 런타임) API mới dùng availability check; compile-time nền tảng (platform / 플랫폼)/nguồn (source / 소스) selection dùng conditional compilation. gói (package / 패키지)/thư viện (library / 라이브러리) còn có `swift-tools-version`, phụ thuộc (dependency / 의존성) phiên bản (version / 버전) và API công khai (public API / 공개 API) availability riêng.

> **Bàn giao:** Sau **Phiên bản (version / 버전) quy tắc (rule / 규칙)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
