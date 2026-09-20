# Maintenance, evolution và technical debt

Phần lớn chi phí software xảy ra sau lần release đầu. Requirements thay đổi, dependencies update, teams đổi, data lớn lên và assumptions cũ hết đúng. Maintainability không phải “code đẹp”; nó là khả năng thay đổi system với risk/cost kiểm soát được.

## Software không hao mòn vật lý nhưng môi trường thay đổi

Một binary có thể không đổi bit nào nhưng ecosystem đổi: OS deprecate API, certificate root thay, browser behavior đổi, regulation đổi, traffic tăng.

Software aging phần lớn là mismatch giữa system assumptions và evolving environment.

## Corrective, adaptive, perfective, preventive maintenance

Corrective sửa bugs. Adaptive thích nghi platform/environment. Perfective cải thiện functionality/performance. Preventive giảm future risk như refactor hoặc dependency cleanup.

Thực tế categories overlap nhưng giúp thấy maintenance không đồng nghĩa bug fixing.

## Technical debt

Technical debt là metaphor: chọn solution nhanh/đơn giản hôm nay có thể tạo interest dưới dạng future change cost.

Debt không luôn xấu. Intentional debt có thể rational khi deadline/value quan trọng, miễn cost được hiểu và repayment plan hợp lý.

Gọi mọi code xấu là debt làm mất meaning; một accidental design flaw không phải decision trade-off có chủ đích.

## Change amplification

Nếu một business change yêu cầu sửa 17 modules, 8 schemas và 5 deploy pipelines, architecture có high change amplification.

Metrics như lead time, change failure rate và code ownership patterns có thể phản ánh maintainability tốt hơn subjective “clean code”.

## Refactoring

Refactoring thay internal structure mà giữ externally observable behavior. Tests/contracts giúp bảo vệ invariant khi refactor.

Refactor lớn kiểu rewrite toàn hệ thống có risk cao; incremental strangler pattern có thể migrate capability dần.

## Legacy systems

Legacy không chỉ nghĩa “cũ”. Một system trở thành legacy khi knowledge/tests/contracts thiếu đến mức change rất rủi ro.

Chiến lược đầu tiên thường là tạo characterization tests, observability và mapping dependencies trước khi “modernize”.

## Dependency evolution

Library upgrade có breaking changes, security patches và transitive effects. Pin forever tăng security debt; auto-update without tests tăng breakage risk.

Healthy system có automated compatibility tests và regular upgrade cadence để tránh mega-jumps.

## Data migration như irreversible state change

Code có thể checkout old commit; production data đã migrate không dễ quay lại. Vì vậy schema/data evolution cần backups, reversible transformations khi possible và validation.

Data is often the most durable part of system architecture.

## Knowledge debt

Nếu chỉ một engineer hiểu critical subsystem, bus factor thấp. Documentation, code review, rotation và runbooks là mechanisms phân phối knowledge.

Knowledge debt gây outage recovery chậm dù code “clean”.

## Sunsetting

Feature/service không còn value vẫn có maintenance/security cost. Decommissioning cần dependency discovery, traffic observation, data retention và stakeholder communication.

Delete code an toàn là một engineering capability.

## Common Misconceptions

**“Rewrite sạch hơn refactor.”** Rewrite mất hidden requirements encoded trong bugs/workarounds/data behavior và có migration risk lớn.

**“Technical debt phải trả hết.”** Một số debt không đáng trả nếu component sắp sunset hoặc change frequency thấp.

**“Legacy = ngôn ngữ cũ.”** Modern stack không có tests/ownership cũng có thể trở thành legacy nhanh.

## Mental Model

> Maintainability là option value: architecture/code/process tốt giữ chi phí của future unknown changes thấp và recovery path rõ.

## Kết nối

Đọc [architecture](./01_software_architecture_and_design_reasoning.md), [delivery](./03_delivery_configuration_and_operations.md), [system decomposition](../08_software_systems/07_system_decomposition_services_and_boundaries.md) và [abstraction/leaky abstractions](../90_connections/04_abstraction_layers_and_leaky_abstractions.md).