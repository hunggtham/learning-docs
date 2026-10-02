# Delivery, cấu hình (configuration / 구성) và operations

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Delivery, configuration và operations**. Route đi từ immutable artifact → configuration/feature flags → CI/CD → deployment strategies/database migration → IaC/runbook → rollback hoặc roll-forward, để thay đổi production có đường kiểm soát và phục hồi.

Mã (code / 코드) chỉ tạo giá trị (value / 값) khi sản phẩm tạo ra (artifact / 산출물) đúng được đưa vào đúng môi trường (environment / 환경) với cấu hình (configuration / 구성) đúng và có thể vận hành/recover. Software delivery nối nguồn (source / 소스) điều khiển (control / 제어), bản dựng (build / 빌드), tests, sản phẩm tạo ra (artifact / 산출물), triển khai (deployment / 배포), thời gian chạy (runtime / 런타임) cấu hình (config / 설정), khả năng quan sát (observability / 관측 가능성) và quay lui (rollback / 롤백) thành một chuỗi (chain / 사슬).

## Bản dựng (build / 빌드) once, promote same sản phẩm tạo ra (artifact / 산출물)

Một principle mạnh là hiện vật bản dựng (build artifact / 빌드 산출물) immutable một lần rồi promote qua environments, thay vì rebuild khác nhau cho staging/môi trường vận hành (production / 운영 환경). Điều này giảm “works in staging sản phẩm tạo ra (artifact / 산출물) khác môi trường vận hành (production / 운영 환경)”.

Environment-specific hành vi (behavior / 동작) nên đến từ cấu hình (configuration / 구성) hoặc injected secrets, không phải nguồn (source / 소스) branch divergent.

> **Chuyển mạch:** Trong **Delivery, cấu hình (configuration / 구성) và operations**, **Cấu hình (configuration / 구성)** tiếp nhận điểm tựa từ **Bản dựng (build / 빌드) once, promote same sản phẩm tạo ra (artifact / 산출물)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tính năng (feature / 기능) flags** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cấu hình (configuration / 구성)

Cấu hình (configuration / 구성) là dữ liệu (data / 데이터) thay đổi triển khai (deployment / 배포)/hành vi thời gian chạy (runtime behavior / 런타임 동작) mà không đổi mã (code / 코드). Nhưng cấu hình (config / 설정) cũng cần lược đồ (schema / 스키마), kiểm tra hợp lệ (validation / 검증), versioning và quyền sở hữu (ownership / 소유권).

Một typo cấu hình (config / 설정) có thể outage như mã (code / 코드) bug. cấu hình (config / 설정) changes nên kiểm tra (audit / 감사)/kiểm thử (test / 테스트)/quay lui (rollback / 롤백) được.

> **Chuyển mạch:** Ở chặng này của **Delivery, cấu hình (configuration / 구성) và operations**, **Tính năng (feature / 기능) flags** tiếp nhận điểm tựa từ **Cấu hình (configuration / 구성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **CI** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tính năng (feature / 기능) flags

Cờ tính năng (feature flag / 기능 플래그) tách deploy mã (code / 코드) khỏi bản phát hành (release / 릴리스) hành vi (behavior / 동작). Nó giúp gradual rollout và emergency disable.

Nhưng flags tạo combinatorial states và technical debt. Mỗi flag nên có đơn vị sở hữu (owner / 오너)/expiry plan; permanent zombie flags làm mã (code / 코드) khó lập luận (reasoning / 추론).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Delivery, cấu hình (configuration / 구성) và operations**, **CI** tiếp nhận điểm tựa từ **Tính năng (feature / 기능) flags** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **CD** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## CI

Continuous tích hợp (integration / 통합) nghĩa developers integrate frequent changes và automated chuỗi xử lý (pipeline / 파이프라인) bản dựng (build / 빌드)/kiểm thử (test / 테스트) chúng. CI goal là detect incompatibility sớm, không chỉ “có Jenkins/GitHub Actions”.

Chuỗi xử lý (pipeline / 파이프라인) phản hồi (feedback / 피드백) càng chậm thì batch kích thước (size / 크기) changes càng lớn và fix chi phí (cost / 비용) tăng.

> **Chuyển mạch:** Trong **Delivery, cấu hình (configuration / 구성) và operations**, **CD** tiếp nhận điểm tựa từ **CI** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Triển khai (deployment / 배포) strategies** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## CD

Continuous Delivery giữ hệ thống (system / 시스템) luôn ở trạng thái deployable, bản phát hành (release / 릴리스) có thể manual gate. Continuous triển khai (deployment / 배포) tự động đưa passed changes tới môi trường vận hành (production / 운영 환경).

Hai terms thường bị dùng lẫn; distinction nằm ở automatic môi trường vận hành (production / 운영 환경) bản phát hành (release / 릴리스).

> **Chuyển mạch:** Ở chặng này của **Delivery, cấu hình (configuration / 구성) và operations**, **Triển khai (deployment / 배포) strategies** tiếp nhận điểm tựa từ **CD** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Triển khai (deployment / 배포) strategies

Rolling cập nhật (update / 업데이트) thay instances dần. Blue-green giữ hai environments và switch traffic. Canary gửi small traffic tới phiên bản (version / 버전) mới rồi tăng dần.

Chiến lược (strategy / 전략) chọn theo quay lui (rollback / 롤백) speed, sức chứa (capacity / 용량) chi phí (cost / 비용), trạng thái (state / 상태)/lược đồ (schema / 스키마) tính tương thích (compatibility / 호환성) và khả năng quan sát (observability / 관측 가능성).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Delivery, cấu hình (configuration / 구성) và operations**, **Triển khai (deployment / 배포) strategies** nêu điều cần giải thích; **Cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Hạ tầng dưới dạng mã (infrastructure as code / 코드형 인프라)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션)

App deploy quay lui (rollback / 롤백) không đơn giản nếu lược đồ (schema / 스키마) đã destructive thay đổi (change / 변경). Expand-contract mẫu (pattern / 패턴) thêm compatible lược đồ (schema / 스키마) trước, deploy mã (code / 코드) dùng cả forms, migrate dữ liệu (data / 데이터) rồi mới remove old fields.

Backward/forward tính tương thích (compatibility / 호환성) là yêu cầu (requirement / 요구사항) xuyên nhiều deploy versions.

> **Chuyển mạch:** Trong **Delivery, cấu hình (configuration / 구성) và operations**, **Cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션)** nêu điều cần giải thích; **Hạ tầng dưới dạng mã (infrastructure as code / 코드형 인프라)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Runbook và operational readiness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hạ tầng dưới dạng mã (infrastructure as code / 코드형 인프라)

IaC phiên bản (version / 버전) hóa hạ tầng (infrastructure / 인프라) definitions giúp rà soát (review / 검토)/reproducibility. Nhưng trạng thái (state / 상태) drift, provider hành vi (behavior / 동작) và secrets vẫn cần quản lý.

Declarative cấu hình (config / 설정) mô tả desired trạng thái (state / 상태); controller/công cụ (tool / 도구) reconcile actual trạng thái (state / 상태) với desired trạng thái (state / 상태).

> **Chuyển mạch:** Ở chặng này của **Delivery, cấu hình (configuration / 구성) và operations**, **Runbook và operational readiness** tiếp nhận điểm tựa từ **Hạ tầng dưới dạng mã (infrastructure as code / 코드형 인프라)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quay lui (rollback / 롤백) và roll-forward** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Runbook và operational readiness

Một dịch vụ (service / 서비스) môi trường vận hành (production / 운영 환경) cần biết đơn vị sở hữu (owner / 오너), dashboard, alerts, dependencies, backup/restore, sức chứa (capacity / 용량) các giả định (assumptions / 가정들) và sự cố (incident / 인시던트) procedures.

“Deploy thành công” không phải endpoint; operability là chất lượng (quality / 품질) attribute.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Delivery, cấu hình (configuration / 구성) và operations**, **Quay lui (rollback / 롤백) và roll-forward** tiếp nhận điểm tựa từ **Runbook và operational readiness** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quay lui (rollback / 롤백) và roll-forward

Quay lui (rollback / 롤백) nhanh hữu ích nhưng không luôn possible sau irreversible dữ liệu (data / 데이터) changes. Roll-forward bằng hotfix đôi khi safer.

Bản phát hành (release / 릴리스) thiết kế (design / 설계) nên biết trước khôi phục (recovery / 복구) đường dẫn (path / 경로) thay vì nghĩ sau sự cố (incident / 인시던트).

> **Chuyển mạch:** Trong **Delivery, cấu hình (configuration / 구성) và operations**, **Dùng chung (common / 공통) Misconceptions** tiếp nhận điểm tựa từ **Quay lui (rollback / 롤백) và roll-forward** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“CI/CD là công cụ (tool / 도구).”** công cụ (tool / 도구) chỉ hỗ trợ tiến trình (process / 프로세스); tích hợp (integration / 통합) frequency, automation và khôi phục (recovery / 복구) ngữ nghĩa (semantics / 의미론) mới là cốt lõi (core / 핵심).

**“cờ tính năng (feature flag / 기능 플래그) = cấu hình (config / 설정) boolean vô hại.”** Flags tạo thời gian chạy (runtime / 런타임) trạng thái (state / 상태) không gian (space / 공간) và cần vòng đời (lifecycle / 생명주기).

**“ảnh bộ chứa (container image / 컨테이너 이미지) giống nhau thì environments giống nhau.”** Kernel, mạng (network / 네트워크), secrets, dữ liệu (data / 데이터) và bên ngoài (external / 외부) dependencies vẫn khác.

> **Chuyển mạch:** Ở chặng này của **Delivery, cấu hình (configuration / 구성) và operations**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Dùng chung (common / 공통) Misconceptions** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Delivery là chuyển tiếp trạng thái (state transition / 상태 전이) của socio-technical hệ thống (system / 시스템). Mỗi bản phát hành (release / 릴리스) phải bảo toàn tính tương thích (compatibility / 호환성)/invariants khi old và new versions có thể cùng tồn tại.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Delivery, cấu hình (configuration / 구성) và operations**, **Kết nối** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc [version control/build/packages](../08_software_systems/01_version_control_build_link_and_packages.md), [supply-chain security](../07_security_reliability/08_supply_chain_and_secure_software_lifecycle.md), [reliability/observability](../07_security_reliability/05_fault_tolerance_observability_and_reliability.md) và [maintenance](./04_maintenance_evolution_and_technical_debt.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
