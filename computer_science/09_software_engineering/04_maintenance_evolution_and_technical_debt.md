# Maintenance, evolution và technical debt

> **Mạch đọc:** Đặt **Maintenance, evolution và technical debt** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Software không hao mòn vật lý nhưng môi trường thay đổi** sang **Corrective, adaptive, perfective, preventive maintenance**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Phần lớn chi phí software xảy ra sau lần bản phát hành (release / 릴리스) đầu. Requirements thay đổi, dependencies cập nhật (update / 업데이트), teams đổi, dữ liệu (data / 데이터) lớn lên và các giả định (assumptions / 가정들) cũ hết đúng. Maintainability không phải “mã (code / 코드) đẹp”; nó là khả năng thay đổi hệ thống (system / 시스템) với rủi ro (risk / 위험)/chi phí (cost / 비용) kiểm soát được.

## Software không hao mòn vật lý nhưng môi trường thay đổi

Một nhị phân (binary / 이진) có thể không đổi bit nào nhưng ecosystem đổi: OS deprecate API, certificate gốc (root / 루트) thay, trình duyệt (browser / 브라우저) hành vi (behavior / 동작) đổi, regulation đổi, traffic tăng.

Software aging phần lớn là mismatch giữa hệ thống (system / 시스템) các giả định (assumptions / 가정들) và evolving môi trường (environment / 환경).

## Corrective, adaptive, perfective, preventive maintenance

Corrective sửa bugs. Adaptive thích nghi nền tảng (platform / 플랫폼)/môi trường (environment / 환경). Perfective cải thiện functionality/hiệu năng (performance / 성능). Preventive giảm future rủi ro (risk / 위험) như refactor hoặc phụ thuộc (dependency / 의존성) cleanup.

Thực tế categories overlap nhưng giúp thấy maintenance không đồng nghĩa bug fixing.

## Technical debt

Technical debt là metaphor: chọn solution nhanh/đơn giản hôm nay có thể tạo interest dưới dạng future thay đổi (change / 변경) chi phí (cost / 비용).

Debt không luôn xấu. Intentional debt có thể rational khi deadline/giá trị (value / 값) quan trọng, miễn chi phí (cost / 비용) được hiểu và repayment plan hợp lý.

Gọi mọi mã (code / 코드) xấu là debt làm mất meaning; một accidental thiết kế (design / 설계) flaw không phải quyết định (decision / 결정) sự đánh đổi (trade-off / 트레이드오프) có chủ đích.

## Thay đổi (change / 변경) amplification

Nếu một nghiệp vụ (business / 비즈니스) thay đổi (change / 변경) yêu cầu sửa 17 modules, 8 schemas và 5 deploy pipelines, kiến trúc (architecture / 아키텍처) có high thay đổi (change / 변경) amplification.

Metrics như lead thời gian (time / 시간), thay đổi (change / 변경) thất bại (failure / 실패) tỷ lệ (rate / 비율) và mã (code / 코드) quyền sở hữu (ownership / 소유권) patterns có thể phản ánh maintainability tốt hơn subjective “clean mã (code / 코드)”.

## Refactoring

Refactoring thay nội bộ (internal / 내부) cấu trúc (structure / 구조) mà giữ externally observable hành vi (behavior / 동작). Tests/contracts giúp bảo vệ bất biến (invariant / 불변식) khi refactor.

Refactor lớn kiểu rewrite toàn hệ thống có rủi ro (risk / 위험) cao; incremental strangler mẫu (pattern / 패턴) có thể migrate năng lực (capability / 역량) dần.

## Legacy các hệ thống (systems / 시스템들)

Legacy không chỉ nghĩa “cũ”. Một hệ thống (system / 시스템) trở thành legacy khi kiến thức (knowledge / 지식)/tests/contracts thiếu đến mức thay đổi (change / 변경) rất rủi ro.

Chiến lược đầu tiên thường là tạo characterization tests, khả năng quan sát (observability / 관측 가능성) và ánh xạ (mapping / 매핑) dependencies trước khi “modernize”.

## Phụ thuộc (dependency / 의존성) evolution

Thư viện (library / 라이브러리) upgrade có breaking changes, bảo mật (security / 보안) patches và transitive effects. Pin forever tăng bảo mật (security / 보안) debt; auto-update without tests tăng breakage rủi ro (risk / 위험).

Healthy hệ thống (system / 시스템) có automated tính tương thích (compatibility / 호환성) tests và regular upgrade cadence để tránh mega-jumps.

## Dữ liệu (data / 데이터) di chuyển (migration / 마이그레이션) như irreversible trạng thái (state / 상태) thay đổi (change / 변경)

Mã (code / 코드) có thể checkout old lần ghi nhận (commit / 커밋); môi trường vận hành (production / 운영 환경) dữ liệu (data / 데이터) đã migrate không dễ quay lại. Vì vậy lược đồ (schema / 스키마)/dữ liệu (data / 데이터) evolution cần backups, reversible transformations khi possible và kiểm tra hợp lệ (validation / 검증).

Dữ liệu (data / 데이터) is often the most durable part of hệ thống (system / 시스템) kiến trúc (architecture / 아키텍처).

## Kiến thức (knowledge / 지식) debt

Nếu chỉ một engineer hiểu trọng yếu (critical / 중요) subsystem, bus factor thấp. Documentation, rà soát mã (code review / 코드 리뷰), rotation và runbooks là mechanisms phân phối kiến thức (knowledge / 지식).

Kiến thức (knowledge / 지식) debt gây outage khôi phục (recovery / 복구) chậm dù mã (code / 코드) “clean”.

## Sunsetting

Tính năng (feature / 기능)/dịch vụ (service / 서비스) không còn giá trị (value / 값) vẫn có maintenance/bảo mật (security / 보안) chi phí (cost / 비용). Decommissioning cần phụ thuộc (dependency / 의존성) discovery, traffic observation, dữ liệu (data / 데이터) retention và stakeholder communication.

Delete mã (code / 코드) an toàn là một kỹ thuật (engineering / 엔지니어링) năng lực (capability / 역량).

## Dùng chung (common / 공통) Misconceptions

**“Rewrite sạch hơn refactor.”** Rewrite mất hidden requirements encoded trong bugs/workarounds/dữ liệu (data / 데이터) hành vi (behavior / 동작) và có di chuyển (migration / 마이그레이션) rủi ro (risk / 위험) lớn.

**“Technical debt phải trả hết.”** Một số debt không đáng trả nếu thành phần (component / 컴포넌트) sắp sunset hoặc thay đổi (change / 변경) frequency thấp.

**“Legacy = ngôn ngữ cũ.”** hiện đại (modern / 현대적) ngăn xếp (stack / 스택) không có tests/quyền sở hữu (ownership / 소유권) cũng có thể trở thành legacy nhanh.

## Mô hình tư duy (mental model / 사고 모델)

> Maintainability là option giá trị (value / 값): kiến trúc (architecture / 아키텍처)/mã (code / 코드)/tiến trình (process / 프로세스) tốt giữ chi phí của future unknown changes thấp và khôi phục (recovery / 복구) đường dẫn (path / 경로) rõ.

## Kết nối

Đọc [architecture](./01_software_architecture_and_design_reasoning.md), [delivery](./03_delivery_configuration_and_operations.md), [system decomposition](../08_software_systems/07_system_decomposition_services_and_boundaries.md) và [abstraction/leaky abstractions](../90_connections/04_abstraction_layers_and_leaky_abstractions.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 requirements specification and engineering process](./00_requirements_specification_and_engineering_process.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
