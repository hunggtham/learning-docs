# Software kiến trúc (architecture / 아키텍처) và thiết kế (design / 설계) lập luận (reasoning / 추론)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Software kiến trúc (architecture / 아키텍처) và thiết kế (design / 설계) lập luận (reasoning / 추론)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Kiến trúc (architecture / 아키텍처) như set of consequential decisions** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Chất lượng (quality / 품질) attributes tạo kiến trúc (architecture / 아키텍처)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Kiến trúc (architecture / 아키텍처) không phải sơ đồ boxes đẹp; nó là tập decisions khó thay đổi về boundaries, dữ liệu (data / 데이터) quyền sở hữu (ownership / 소유권), communication, triển khai (deployment / 배포) và chất lượng (quality / 품질) attributes. thiết kế (design / 설계) tốt bắt đầu từ forces/các ràng buộc (constraints / 제약조건들) chứ không từ mẫu (pattern / 패턴) names.

## Kiến trúc (architecture / 아키텍처) như set of consequential decisions

Một quyết định (decision / 결정) “dùng PostgreSQL” có impact khác “trường dữ liệu (field / 필드) này tên `createdAt`”. kiến trúc (architecture / 아키텍처) decisions thường ảnh hưởng nhiều modules/teams và di chuyển (migration / 마이그레이션) chi phí (cost / 비용) cao.

Do đó kiến trúc (architecture / 아키텍처) quyết định (decision / 결정) bản ghi (record / 레코드) (ADR) nên ghi ngữ cảnh (context / 맥락), options, quyết định (decision / 결정) và consequences. Mục tiêu không phải bureaucracy mà giữ lập luận (reasoning / 추론) cho future maintainers.

> **Chuyển mạch:** Trong **Software kiến trúc (architecture / 아키텍처) và thiết kế (design / 설계) lập luận (reasoning / 추론)**, **Chất lượng (quality / 품질) attributes tạo kiến trúc (architecture / 아키텍처)** tiếp nhận điểm tựa từ **Kiến trúc (architecture / 아키텍처) như set of consequential decisions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Coupling và cohesion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chất lượng (quality / 품질) attributes tạo kiến trúc (architecture / 아키텍처)

Availability, độ trễ (latency / 지연 시간), bảo mật (security / 보안), modifiability, scalability và chi phí (cost / 비용) thường xung đột (conflict / 충돌).

Ví dụ synchronous replication tăng durability/consistency nhưng tăng ghi (write / 쓰기) độ trễ (latency / 지연 시간) và giảm availability khi replicas unavailable. kiến trúc (architecture / 아키텍처) chỉ có ý nghĩa khi gắn với chất lượng (quality / 품질) priorities.

> **Chuyển mạch:** Ở chặng này của **Software kiến trúc (architecture / 아키텍처) và thiết kế (design / 설계) lập luận (reasoning / 추론)**, **Coupling và cohesion** tiếp nhận điểm tựa từ **Chất lượng (quality / 품질) attributes tạo kiến trúc (architecture / 아키텍처)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thông tin (information / 정보) hiding** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Coupling và cohesion

Cohesion cao gom hành vi (behavior / 동작)/dữ liệu (data / 데이터) thay đổi cùng nhau. Coupling thấp giảm số các giả định (assumptions / 가정들) xuyên boundaries.

Coupling có nhiều dạng: compile-time, thời gian chạy (runtime / 런타임), dữ liệu (data / 데이터) lược đồ (schema / 스키마), temporal, organizational. Hai services không import mã (code / 코드) nhau nhưng cùng phụ thuộc bản phát hành (release / 릴리스) cửa sổ (window / 윈도우) vẫn bị coupled.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Software kiến trúc (architecture / 아키텍처) và thiết kế (design / 설계) lập luận (reasoning / 추론)**, **Thông tin (information / 정보) hiding** tiếp nhận điểm tựa từ **Coupling và cohesion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Layering** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thông tin (information / 정보) hiding

Mô-đun (module / 모듈) nên hide volatile thiết kế (design / 설계) quyết định (decision / 결정) sau stable giao diện (interface / 인터페이스). Một lưu trữ (storage / 저장소) mô-đun (module / 모듈) expose `saveOrder()` thay vì cho callers phụ thuộc bảng (table / 테이블) bố cục (layout / 레이아웃) nếu bố cục (layout / 레이아웃) có khả năng thay đổi.

Thông tin (information / 정보) hiding giảm blast radius của thay đổi (change / 변경).

> **Chuyển mạch:** Trong **Software kiến trúc (architecture / 아키텍처) và thiết kế (design / 설계) lập luận (reasoning / 추론)**, **Layering** tiếp nhận điểm tựa từ **Thông tin (information / 정보) hiding** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hexagonal/ports-and-adapters intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Layering

Tầng (layer / 계층) kiến trúc (architecture / 아키텍처) tạo direction dependencies: presentation → ứng dụng (application / 애플리케이션) → lĩnh vực (domain / 도메인) → hạ tầng (infrastructure / 인프라) tùy style. tầng (layer / 계층) giúp separation nhưng excessive layering có thể tạo pass-through boilerplate.

Tầng (layer / 계층) là công cụ (tool / 도구) cho phụ thuộc (dependency / 의존성) điều khiển (control / 제어), không phải quy tắc (rule / 규칙) rằng mọi yêu cầu (request / 요청) phải đi qua N classes.

> **Chuyển mạch:** Ở chặng này của **Software kiến trúc (architecture / 아키텍처) và thiết kế (design / 설계) lập luận (reasoning / 추론)**, **Hexagonal/ports-and-adapters intuition** tiếp nhận điểm tựa từ **Layering** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kiến trúc (architecture / 아키텍처) patterns và ngữ cảnh (context / 맥락)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hexagonal/ports-and-adapters intuition

Lĩnh vực (domain / 도메인) lô-gic (logic / 논리) phụ thuộc abstractions/ports; bên ngoài (external / 외부) DB/UI/message broker là adapters. Goal là nghiệp vụ (business / 비즈니스) rules không bị hard-wire vào khung phần mềm (framework / 프레임워크) hạ tầng (infrastructure / 인프라).

Nhưng nếu lĩnh vực (domain / 도메인) đơn giản, thêm lớp trừu tượng (abstraction / 추상화) interfaces everywhere có thể overengineering. ranh giới (boundary / 경계) nên bảo vệ volatility thật.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Software kiến trúc (architecture / 아키텍처) và thiết kế (design / 설계) lập luận (reasoning / 추론)**, **Kiến trúc (architecture / 아키텍처) patterns và ngữ cảnh (context / 맥락)** tiếp nhận điểm tựa từ **Hexagonal/ports-and-adapters intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dữ liệu (data / 데이터) quyền sở hữu (ownership / 소유권)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kiến trúc (architecture / 아키텍처) patterns và ngữ cảnh (context / 맥락)

Monolith, microservices, event-driven, CQRS, layered, pipes-and-filters không phải maturity ladder. Mỗi mẫu (pattern / 패턴) giải một set forces và tạo liabilities.

CQRS tách read/ghi (write / 쓰기) các mô hình (models / 모델들) khi needs khác mạnh, nhưng thêm synchronization/evolution độ phức tạp (complexity / 복잡도). sự kiện (event / 이벤트) sourcing cho kiểm tra (audit / 감사)/replay nhưng làm lược đồ (schema / 스키마) evolution và debugging khó hơn.

> **Chuyển mạch:** Trong **Software kiến trúc (architecture / 아키텍처) và thiết kế (design / 설계) lập luận (reasoning / 추론)**, **Kiến trúc (architecture / 아키텍처) patterns và ngữ cảnh (context / 맥락)** nêu điều cần giải thích; **Dữ liệu (data / 데이터) quyền sở hữu (ownership / 소유권)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Phụ thuộc (dependency / 의존성) inversion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dữ liệu (data / 데이터) quyền sở hữu (ownership / 소유권)

Kiến trúc (architecture / 아키텍처) ranh giới (boundary / 경계) mạnh thường cần quyền sở hữu (ownership / 소유권) của trạng thái (state / 상태). dùng chung (shared / 공유) writable cơ sở dữ liệu (database / 데이터베이스) làm services/modules phụ thuộc hidden invariants.

Quyền sở hữu (ownership / 소유권) không đồng nghĩa không chia sẻ dữ liệu (data / 데이터); nó nghĩa một thành phần (component / 컴포넌트) có authority cập nhật (update / 업데이트) và others truy cập qua đặc tả hợp đồng (contract / 계약)/bản sao (copy / 복사) phù hợp.

> **Chuyển mạch:** Ở chặng này của **Software kiến trúc (architecture / 아키텍처) và thiết kế (design / 설계) lập luận (reasoning / 추론)**, **Dữ liệu (data / 데이터) quyền sở hữu (ownership / 소유권)** nêu điều cần giải thích; **Phụ thuộc (dependency / 의존성) inversion** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Kiến trúc (architecture / 아키텍처) fitness functions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phụ thuộc (dependency / 의존성) inversion

High-level chính sách (policy / 정책) không nên phụ thuộc concrete low-level hiện thực (implementation / 구현) khi volatility/coupling cần tách. phụ thuộc (dependency / 의존성) inversion dùng interfaces/abstractions để direction nguồn (source / 소스) phụ thuộc (dependency / 의존성) phục vụ stability.

Nhưng giao diện (interface / 인터페이스) chỉ có một hiện thực (implementation / 구현) và không có volatility không tự động hữu ích.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Software kiến trúc (architecture / 아키텍처) và thiết kế (design / 설계) lập luận (reasoning / 추론)**, **Kiến trúc (architecture / 아키텍처) fitness functions** tiếp nhận điểm tựa từ **Phụ thuộc (dependency / 의존성) inversion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kiến trúc (architecture / 아키텍처) fitness functions

Một kiến trúc (architecture / 아키텍처) intent có thể degrade theo thời gian. Automated checks như phụ thuộc (dependency / 의존성) rules, API tính tương thích (compatibility / 호환성) tests, độ trễ (latency / 지연 시간) SLO, bảo mật (security / 보안) chính sách (policy / 정책) scans có thể đóng vai fitness functions để phát hiện drift.

Kiến trúc (architecture / 아키텍처) vì vậy không chỉ là initial thiết kế (design / 설계); nó cần continuous xác minh (verification / 확인).

> **Chuyển mạch:** Trong **Software kiến trúc (architecture / 아키텍처) và thiết kế (design / 설계) lập luận (reasoning / 추론)**, **Dùng chung (common / 공통) Misconceptions** tiếp nhận điểm tựa từ **Kiến trúc (architecture / 아키텍처) fitness functions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“kiến trúc (architecture / 아키텍처) là chọn khung phần mềm (framework / 프레임워크).”** khung phần mềm (framework / 프레임워크) là hiện thực (implementation / 구현) quyết định (decision / 결정); kiến trúc (architecture / 아키텍처) lớn hơn là boundaries và chất lượng (quality / 품질) trade-offs.

**“mẫu (pattern / 패턴) nổi tiếng nghĩa là best practice.”** mẫu (pattern / 패턴) chỉ hợp khi forces tương ứng tồn tại.

**“Clean kiến trúc (architecture / 아키텍처) càng nhiều layers càng clean.”** Indirection không có purpose làm hệ thống (system / 시스템) khó hiểu hơn.

> **Chuyển mạch:** Ở chặng này của **Software kiến trúc (architecture / 아키텍처) và thiết kế (design / 설계) lập luận (reasoning / 추론)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Dùng chung (common / 공통) Misconceptions** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> kiến trúc (architecture / 아키텍처) là cách phân bố responsibilities và các ràng buộc (constraints / 제약조건들) sao cho những thay đổi/failures quan trọng bị giới hạn trong boundaries hợp lý.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Software kiến trúc (architecture / 아키텍처) và thiết kế (design / 설계) lập luận (reasoning / 추론)**, **Kết nối** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc [system decomposition/services](../08_software_systems/07_system_decomposition_services_and_boundaries.md), [requirements](./00_requirements_specification_and_engineering_process.md) và [maintenance/technical debt](./04_maintenance_evolution_and_technical_debt.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
