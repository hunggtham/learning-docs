# Testing, chất lượng (quality / 품질) và xác minh (verification / 확인) chiến lược (strategy / 전략)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Testing, quality và verification strategy**. Route đi từ quality attributes → unit/integration/E2E → contract/property/fuzzing → mutation/static/formal checks → flaky-test control và testability, để coverage phục vụ risk thay vì chỉ tăng số test.

Testing không thể chứng minh program không có bug chỉ bằng chạy vài cases. Nó là sampling/experimentation trên hành vi (behavior / 동작) không gian (space / 공간). chiến lược (strategy / 전략) tốt chọn kiểm thử (test / 테스트) levels và xác minh (verification / 확인) techniques theo rủi ro (risk / 위험), contracts và thất bại (failure / 실패) modes.

## Chất lượng (quality / 품질) không chỉ là không crash

Software chất lượng (quality / 품질) gồm tính đúng đắn (correctness / 정확성), độ tin cậy (reliability / 신뢰성), usability, bảo mật (security / 보안), hiệu năng (performance / 성능), maintainability và tính tương thích (compatibility / 호환성). Một hệ thống (system / 시스템) chạy đúng đầu ra (output / 출력) nhưng độ trễ (latency / 지연 시간) 30 giây vẫn có thể thất bại (fail / 실패) yêu cầu (requirement / 요구사항).

Do đó kiểm thử (test / 테스트) chiến lược (strategy / 전략) phải derive từ chất lượng (quality / 품질) attributes, không chỉ mã (code / 코드) coverage.

> **Nối mạch:** **Đơn vị (unit / 단위) tests** nối từ **Chất lượng (quality / 품질) không chỉ là không crash** sang **Tích hợp (integration / 통합) tests**, vì cơ chế trước tạo đầu vào cho bước sau.

## Đơn vị (unit / 단위) tests

Đơn vị (unit / 단위) kiểm thử (test / 테스트) cô lập một small đơn vị (unit / 단위) theo hành vi (behavior / 동작) đặc tả hợp đồng (contract / 계약). Nó phản hồi (feedback / 피드백) nhanh và giúp localize regression.

Nhưng đơn vị (unit / 단위) ranh giới (boundary / 경계) không nhất thiết là một hàm (function / 함수)/lớp (class / 클래스). Nếu over-mock nội bộ (internal / 내부) interactions, tests become coupled to hiện thực (implementation / 구현) và refactoring khó.

Kiểm thử (test / 테스트) hành vi (behavior / 동작) có giá trị hơn kiểm thử (test / 테스트) lời gọi (call / 호출) choreography trừ khi tương tác (interaction / 상호작용) chính là đặc tả hợp đồng (contract / 계약).

> **Nối mạch:** **Tích hợp (integration / 통합) tests** nối từ **Đơn vị (unit / 단위) tests** sang **End-to-end tests**, vì cơ chế trước tạo đầu vào cho bước sau.

## Tích hợp (integration / 통합) tests

Kiểm thử tích hợp (integration test / 통합 테스트) xác minh boundaries thật: cơ sở dữ liệu (database / 데이터베이스) queries, serialization, bên ngoài (external / 외부) API adapters, filesystem, message broker.

Nhiều bugs nằm ở mismatched các giả định (assumptions / 가정들) giữa components nên chỉ đơn vị (unit / 단위) tests không đủ.

Testcontainers/ephemeral environments giúp chạy phụ thuộc (dependency / 의존성) thật nhưng tăng thời gian chạy (runtime / 런타임)/operational chi phí (cost / 비용).

> **Nối mạch:** **End-to-end tests** nối từ **Tích hợp (integration / 통합) tests** sang **Đặc tả hợp đồng (contract / 계약) testing**, vì cơ chế trước tạo đầu vào cho bước sau.

## End-to-end tests

E2E đi qua user-relevant luồng (flow / 흐름) và bắt wiring/triển khai (deployment / 배포) issues. Nhưng chậm, flaky và khó gỡ lỗi (debug / 디버그) hơn.

Kiểm thử (test / 테스트) pyramid không phải luật cứng về số lượng; principle là nhiều tests nhanh ở dưới, ít tests đắt ở trên, tùy kiến trúc (architecture / 아키텍처)/rủi ro (risk / 위험).

> **Nối mạch:** **Đặc tả hợp đồng (contract / 계약) testing** nối từ **End-to-end tests** sang **Property-based testing**, vì cơ chế trước tạo đầu vào cho bước sau.

## Đặc tả hợp đồng (contract / 계약) testing

Producer-consumer đặc tả hợp đồng (contract / 계약) kiểm thử (test / 테스트) xác minh API/message tính tương thích (compatibility / 호환성) mà không cần full E2E môi trường (environment / 환경). Nó đặc biệt hữu ích cho independently deployed services.

Lược đồ (schema / 스키마) tính tương thích (compatibility / 호환성) không đủ nếu ngữ nghĩa (semantics / 의미론) đổi. `status: ACTIVE` có thể giữ kiểu (type / 타입) nhưng meaning thay đổi vẫn phá bên tiêu thụ (consumer / 소비자).

> **Nối mạch:** **Property-based testing** nối từ **Đặc tả hợp đồng (contract / 계약) testing** sang **Fuzzing**, vì cơ chế trước tạo đầu vào cho bước sau.

## Property-based testing

Thay vì viết vài examples, property-based testing generate nhiều inputs và kiểm invariants như sorting đầu ra (output / 출력) ordered + permutation đầu vào (input / 입력).

Nó phù hợp algorithms, parsers, serialization và dữ liệu (data / 데이터) structures nơi invariants rõ.

> **Nối mạch:** **Fuzzing** nối từ **Property-based testing** sang **Mutation testing**, vì cơ chế trước tạo đầu vào cho bước sau.

## Fuzzing

Fuzzer tạo/mutate inputs để khám phá crashes, hangs hoặc sanitizer violations. Coverage-guided fuzzing dùng thực thi (execution / 실행) phản hồi (feedback / 피드백) để tìm paths mới.

Fuzzing rất mạnh cho parsers/protocols nhưng không tự biết nghiệp vụ (business / 비즈니스) tính đúng đắn (correctness / 정확성) nếu không có oracle/thuộc tính (property / 속성).

> **Nối mạch:** **Mutation testing** nối từ **Fuzzing** sang **Static phân tích (analysis / 분석) và formal xác minh (verification / 확인)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Mutation testing

Mutation testing cố tình đổi mã (code / 코드) nhỏ (đảo condition, thay operator) rồi xem tests có thất bại (fail / 실패) không. Nếu mutant sống, bộ kiểm thử (test suite / 테스트 스위트) có thể không nhạy với hành vi (behavior / 동작) đó.

Coverage đo mã (code / 코드) đã chạy; mutation score đo một phần khả năng tests phát hiện ngữ nghĩa (semantic / 의미적) changes.

> **Nối mạch:** **Static phân tích (analysis / 분석) và formal xác minh (verification / 확인)** nối từ **Mutation testing** sang **Flaky tests**, vì cơ chế trước tạo đầu vào cho bước sau.

## Static phân tích (analysis / 분석) và formal xác minh (verification / 확인)

Static analyzers tìm patterns/data-flow issues mà không execute program. Formal methods có thể prove properties theo mô hình (model / 모델)/specification nhưng chi phí (cost / 비용) cao và phạm vi (scope / 범위) phải rõ.

Không technique nào thay tất cả techniques khác; chúng cover thất bại (failure / 실패) spaces khác nhau.

> **Nối mạch:** **Flaky tests** nối từ **Static phân tích (analysis / 분석) và formal xác minh (verification / 확인)** sang **Testability như thiết kế (design / 설계) thuộc tính (property / 속성)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Flaky tests

Flakiness thường do thời gian (time / 시간), race, trạng thái dùng chung (shared state / 공유 상태), random seed, bên ngoài (external / 외부) dịch vụ (service / 서비스) hoặc môi trường (environment / 환경) phụ thuộc (dependency / 의존성). thử lại (retry / 재시도) flaky kiểm thử (test / 테스트) che tín hiệu (signal / 신호) và làm chuỗi xử lý (pipeline / 파이프라인) unreliable.

Treat kiểm thử (test / 테스트) độ tin cậy (reliability / 신뢰성) như môi trường vận hành (production / 운영 환경) độ tin cậy (reliability / 신뢰성): quyền sở hữu (ownership / 소유권), metrics và root-cause fixes.

> **Nối mạch:** **Testability như thiết kế (design / 설계) thuộc tính (property / 속성)** nối từ **Flaky tests** sang **Dùng chung (common / 공통) Misconceptions**, vì cơ chế trước tạo đầu vào cho bước sau.

## Testability như thiết kế (design / 설계) thuộc tính (property / 속성)

Mã (code / 코드) có tường minh (explicit / 명시적) dependencies, deterministic cốt lõi (core / 핵심) lô-gic (logic / 논리) và clear boundaries dễ kiểm thử (test / 테스트) hơn. Nếu kiểm thử (test / 테스트) phải boot toàn app cho một nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙), kiến trúc (architecture / 아키텍처) có thể quá coupled.

Thiết kế (design / 설계) for testability không có nghĩa expose internals; nó nghĩa contracts/dependencies observable và controllable hợp lý.

> **Nối mạch:** **Dùng chung (common / 공통) Misconceptions** nối từ **Testability như thiết kế (design / 설계) thuộc tính (property / 속성)** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Dùng chung (common / 공통) Misconceptions

**“100% coverage = không bug.”** Coverage chỉ nói lines/branches được execute, không chứng minh assertions đủ.

**“Mock càng nhiều kiểm thử (test / 테스트) càng đơn vị (unit / 단위).”** Over-mocking dễ kiểm thử (test / 테스트) hiện thực (implementation / 구현) chứ không hành vi (behavior / 동작).

**“E2E gần người dùng (user / 사용자) nhất nên quan trọng nhất.”** Nó quan trọng nhưng không scalable cho mọi trường hợp (case / 사례); cần portfolio tests.

> **Nối mạch:** **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Dùng chung (common / 공통) Misconceptions**; **Kết nối** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> xác minh (verification / 확인) là xây nhiều lưới bắt lỗi ở các lớp trừu tượng (abstraction / 추상화) levels khác nhau. Không một lưới nào đủ; chiến lược (strategy / 전략) theo rủi ro (risk / 위험) quan trọng hơn chỉ số (metric / 지표) đơn lẻ.

> **Nối mạch:** **Kết nối** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Kết nối

Xem [testing/debugging foundations](../07_security_reliability/04_testing_verification_and_debugging.md), [requirements](./00_requirements_specification_and_engineering_process.md) và [delivery/operations](./03_delivery_configuration_and_operations.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
