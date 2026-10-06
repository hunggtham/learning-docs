# Requirements, specification và kỹ nghệ phần mềm (software engineering / 소프트웨어 공학) tiến trình (process / 프로세스)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Requirements, specification và engineering process**. Route đi từ problem/stakeholder goals → functional/non-functional requirements → specification/use cases → acceptance/traceability → volatility và delivery model, để yêu cầu có thể kiểm chứng và theo dõi tới triển khai.

Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학) bắt đầu trước khi mã (code / 코드) xuất hiện. Nếu ta xây đúng thứ đã được mô tả nhưng thứ đó không giải quyết bài toán (problem / 문제) thực, hệ thống (system / 시스템) vẫn thất bại. Vì vậy requirements kỹ thuật (engineering / 엔지니어링) nghiên cứu cách biến nhu cầu mơ hồ của stakeholders thành hành vi (behavior / 동작), các ràng buộc (constraints / 제약조건들) và acceptance criteria đủ rõ để thiết kế (design / 설계), implement và verify.

## Bài toán (problem / 문제) trước solution

Một yêu cầu (requirement / 요구사항) tốt không bắt đầu bằng khung phần mềm (framework / 프레임워크) hay cơ sở dữ liệu (database / 데이터베이스). Nó mô tả actor nào cần đạt goal nào, trong ngữ cảnh (context / 맥락) nào, với các ràng buộc (constraints / 제약조건들) nào.

“Làm màn hình nhanh hơn” mơ hồ. “95% requests hoàn thành dưới 300 ms với 500 concurrent users trên tải công việc (workload / 워크로드) X” có thể đo và kiểm chứng.

Điểm cốt lõi là chuyển adjective mơ hồ thành observable thuộc tính (property / 속성) khi có thể.

> **Nối mạch:** **Functional và non-functional requirements** nối từ **Bài toán (problem / 문제) trước solution** sang **Stakeholder và conflicting goals**, vì cơ chế trước tạo đầu vào cho bước sau.

## Functional và non-functional requirements

Functional yêu cầu (requirement / 요구사항) mô tả hệ thống (system / 시스템) phải làm gì: đăng nhập, chuyển tiền, tìm kiếm, export report.

Non-functional yêu cầu (requirement / 요구사항) mô tả chất lượng (quality / 품질)/ràng buộc (constraint / 제약조건): độ trễ (latency / 지연 시간), availability, bảo mật (security / 보안), compliance, maintainability, portability, dữ liệu (data / 데이터) retention.

Nhưng ranh giới (boundary / 경계) không tuyệt đối. “Không cho người dùng (user / 사용자) khác đọc hồ sơ” vừa là bảo mật (security / 보안) thuộc tính (property / 속성) vừa là functional authorization quy tắc (rule / 규칙). Điều quan trọng là yêu cầu (requirement / 요구사항) có thể dấu vết (trace / 추적) tới thiết kế (design / 설계)/kiểm thử (test / 테스트).

> **Nối mạch:** **Stakeholder và conflicting goals** nối từ **Functional và non-functional requirements** sang **Specification**, vì cơ chế trước tạo đầu vào cho bước sau.

## Stakeholder và conflicting goals

Sản phẩm (product / 제품) muốn tính năng (feature / 기능) nhanh; bảo mật (security / 보안) muốn stricter controls; operations muốn simplicity; finance muốn giảm hạ tầng (infrastructure / 인프라) chi phí (cost / 비용); người dùng (user / 사용자) muốn ít friction.

Kỹ thuật (engineering / 엔지니어링) không loại bỏ xung đột (conflict / 충돌) mà làm sự đánh đổi (trade-off / 트레이드오프) tường minh (explicit / 명시적). Một kiến trúc (architecture / 아키텍처) quyết định (decision / 결정) nên nói yêu cầu (requirement / 요구사항) nào ưu tiên và chi phí (cost / 비용) nào chấp nhận.

> **Nối mạch:** **Specification** nối từ **Stakeholder và conflicting goals** sang **Use trường hợp (case / 사례) và người dùng (user / 사용자) story**, vì cơ chế trước tạo đầu vào cho bước sau.

## Specification

Specification (đặc tả / 명세) mô tả expected hành vi (behavior / 동작) ở mức đủ precise. Nó có thể là prose, Đặc tả API (API contract / API 계약), máy trạng thái (state machine / 상태 머신), lược đồ (schema / 스키마), chuỗi (sequence / 시퀀스) diagram, bất biến (invariant / 불변식) hoặc formal mô hình (model / 모델).

Specification không nhất thiết dài. Quan trọng là loại bỏ ambiguity ở những nơi thất bại (failure / 실패) chi phí (cost / 비용) cao.

Ví dụ payment API cần định nghĩa idempotency, currency precision, hết thời gian chờ (timeout / 타임아웃) ngữ nghĩa (semantics / 의미론) và duplicate yêu cầu (request / 요청) hành vi (behavior / 동작); không chỉ yêu cầu (request / 요청)/phản hồi (response / 응답) fields.

> **Nối mạch:** **Specification** nêu quy tắc; **Use trường hợp (case / 사례) và người dùng (user / 사용자) story** thử quy tắc trong tình huống, rồi **Acceptance criteria** mở rộng hệ quả.

## Use trường hợp (case / 사례) và người dùng (user / 사용자) story

Use trường hợp (case / 사례) mô tả tương tác (interaction / 상호작용) luồng (flow / 흐름) giữa actor và hệ thống (system / 시스템), gồm main đường dẫn (path / 경로) và alternate/lỗi (error / 오류) paths. người dùng (user / 사용자) story kiểu “As a..., I want..., so that...” hữu ích cho conversation nhưng không thay acceptance criteria.

Một người dùng (user / 사용자) story quá ngắn dễ biến thành placeholder thay vì yêu cầu (requirement / 요구사항). kỹ thuật (engineering / 엔지니어링) cần bổ sung edge cases, permissions, dữ liệu (data / 데이터) vòng đời (lifecycle / 생명주기) và hành vi khi thất bại (failure behavior / 실패 동작).

> **Nối mạch:** **Use trường hợp (case / 사례) và người dùng (user / 사용자) story** nêu quy tắc; **Acceptance criteria** thử quy tắc trong tình huống, rồi **Requirements volatility** mở rộng hệ quả.

## Acceptance criteria

Acceptance criteria biến intent thành testable conditions. Với password reset, cần không chỉ happy đường dẫn (path / 경로) mà đơn vị từ (token / 토큰) expiry, single-use, tỷ lệ (rate / 비율) limit, account enumeration và logged-in session hành vi (behavior / 동작).

Acceptance tests không chứng minh toàn hệ thống (system / 시스템) đúng, nhưng tạo đặc tả hợp đồng (contract / 계약) giữa sản phẩm (product / 제품) intent và hiện thực (implementation / 구현).

> **Nối mạch:** **Requirements volatility** nối từ **Acceptance criteria** sang **Traceability**, vì cơ chế trước tạo đầu vào cho bước sau.

## Requirements volatility

Requirements thay đổi vì thị trường (market / 시장), regulation và học tập (learning / 학습). Quy trình tốt không giả vờ đóng băng mọi thứ; nó quản lý thay đổi (change / 변경) impact.

Kiến trúc (architecture / 아키텍처) nên giữ stable cốt lõi (core / 핵심) invariants trong khi cho phép volatile parts thay đổi. Đây là lý do lớp trừu tượng (abstraction / 추상화)/mô-đun (module / 모듈) boundaries quan trọng.

> **Nối mạch:** **Traceability** nối từ **Requirements volatility** sang **Waterfall, iterative và agile**, vì cơ chế trước tạo đầu vào cho bước sau.

## Traceability

Traceability nối yêu cầu (requirement / 요구사항) → thiết kế (design / 설계) quyết định (decision / 결정) → hiện thực (implementation / 구현) → kiểm thử (test / 테스트) → monitoring. Trong an toàn (safety / 안전)/regulatory domains, traceability rất quan trọng để chứng minh điều khiển (control / 제어) nào đáp ứng yêu cầu (requirement / 요구사항) nào.

Trong sản phẩm (product / 제품) development bình thường, traceability lightweight vẫn hữu ích khi sự cố (incident / 인시던트) xảy ra: “hành vi (behavior / 동작) này là bug hay intended?”

> **Nối mạch:** **Waterfall, iterative và agile** nối từ **Traceability** sang **Risk-driven development**, vì cơ chế trước tạo đầu vào cho bước sau.

## Waterfall, iterative và agile

Waterfall-style phase separation phù hợp khi requirements ổn định và thay đổi (change / 변경) chi phí (cost / 비용) cao, nhưng dễ phản hồi (feedback / 피드백) muộn. Iterative/agile processes giảm batch kích thước (size / 크기) của học tập (learning / 학습) bằng cách deliver/validate thường xuyên.

Agile không có nghĩa không thiết kế (design / 설계), không document hay thay đổi vô hạn. Nó nhấn mạnh short phản hồi (feedback / 피드백) loops và adaptation.

> **Nối mạch:** **Risk-driven development** nối từ **Waterfall, iterative và agile** sang **Dùng chung (common / 공통) Misconceptions**, vì cơ chế trước tạo đầu vào cho bước sau.

## Risk-driven development

Không phải tác vụ (task / 작업) nào cũng nên làm theo nghiệp vụ (business / 비즈니스) priority đơn thuần. Technical bất định (uncertainty / 불확실성) cao có thể cần spike/prototype sớm. bảo mật (security / 보안)/hiệu năng (performance / 성능) bottleneck có thể cần validate trước khi UI hoàn thiện.

Risk-driven planning xử lý unknowns trước khi chúng trở thành late surprise.

> **Nối mạch:** **Dùng chung (common / 공통) Misconceptions** nối từ **Risk-driven development** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Dùng chung (common / 공통) Misconceptions

**“Requirements là việc của PM/BA, nhà phát triển (developer / 개발자) chỉ mã (code / 코드).”** nhà phát triển (developer / 개발자) cần hiểu các ràng buộc (constraints / 제약조건들) để phát hiện ambiguity/impossible các giả định (assumptions / 가정들).

**“Agile nghĩa là không cần specification.”** Chỉ đổi granularity/timing; trọng yếu (critical / 중요) contracts vẫn cần precise.

**“người dùng (user / 사용자) nói gì thì yêu cầu (requirement / 요구사항) là vậy.”** người dùng (user / 사용자) mô tả pain/goal; solution và hidden các ràng buộc (constraints / 제약조건들) cần investigation.

> **Nối mạch:** **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Dùng chung (common / 공통) Misconceptions**; **Kết nối** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> Requirements kỹ thuật (engineering / 엔지니어링) là quá trình biến intent thành falsifiable contracts đủ rõ để thiết kế (design / 설계) và verify, đồng thời chấp nhận rằng understanding sẽ thay đổi qua phản hồi (feedback / 피드백).

> **Nối mạch:** **Kết nối** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Kết nối

Đọc [abstraction/API contracts](../08_software_systems/00_abstraction_modularity_interfaces_and_apis.md), [software architecture](./01_software_architecture_and_design_reasoning.md) và [testing strategy](./02_testing_quality_and_verification_strategy.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
