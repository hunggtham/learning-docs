# Delivery, configuration và operations

Code chỉ tạo value khi artifact đúng được đưa vào đúng environment với configuration đúng và có thể vận hành/recover. Software delivery nối source control, build, tests, artifact, deployment, runtime config, observability và rollback thành một chain.

## Build once, promote same artifact

Một principle mạnh là build artifact immutable một lần rồi promote qua environments, thay vì rebuild khác nhau cho staging/production. Điều này giảm “works in staging artifact khác production”.

Environment-specific behavior nên đến từ configuration hoặc injected secrets, không phải source branch divergent.

## Configuration

Configuration là data thay đổi deployment/runtime behavior mà không đổi code. Nhưng config cũng cần schema, validation, versioning và ownership.

Một typo config có thể outage như code bug. Config changes nên audit/test/rollback được.

## Feature flags

Feature flag tách deploy code khỏi release behavior. Nó giúp gradual rollout và emergency disable.

Nhưng flags tạo combinatorial states và technical debt. Mỗi flag nên có owner/expiry plan; permanent zombie flags làm code khó reasoning.

## CI

Continuous Integration nghĩa developers integrate frequent changes và automated pipeline build/test chúng. CI goal là detect incompatibility sớm, không chỉ “có Jenkins/GitHub Actions”.

Pipeline feedback càng chậm thì batch size changes càng lớn và fix cost tăng.

## CD

Continuous Delivery giữ system luôn ở trạng thái deployable, release có thể manual gate. Continuous Deployment tự động đưa passed changes tới production.

Hai terms thường bị dùng lẫn; distinction nằm ở automatic production release.

## Deployment strategies

Rolling update thay instances dần. Blue-green giữ hai environments và switch traffic. Canary gửi small traffic tới version mới rồi tăng dần.

Strategy chọn theo rollback speed, capacity cost, state/schema compatibility và observability.

## Database migration

App deploy rollback không đơn giản nếu schema đã destructive change. Expand-contract pattern thêm compatible schema trước, deploy code dùng cả forms, migrate data rồi mới remove old fields.

Backward/forward compatibility là requirement xuyên nhiều deploy versions.

## Infrastructure as Code

IaC version hóa infrastructure definitions giúp review/reproducibility. Nhưng state drift, provider behavior và secrets vẫn cần quản lý.

Declarative config mô tả desired state; controller/tool reconcile actual state với desired state.

## Runbook và operational readiness

Một service production cần biết owner, dashboard, alerts, dependencies, backup/restore, capacity assumptions và incident procedures.

“Deploy thành công” không phải endpoint; operability là quality attribute.

## Rollback và roll-forward

Rollback nhanh hữu ích nhưng không luôn possible sau irreversible data changes. Roll-forward bằng hotfix đôi khi safer.

Release design nên biết trước recovery path thay vì nghĩ sau incident.

## Common Misconceptions

**“CI/CD là tool.”** Tool chỉ hỗ trợ process; integration frequency, automation và recovery semantics mới là core.

**“Feature flag = config boolean vô hại.”** Flags tạo runtime state space và cần lifecycle.

**“Container image giống nhau thì environments giống nhau.”** Kernel, network, secrets, data và external dependencies vẫn khác.

## Mental Model

> Delivery là state transition của socio-technical system. Mỗi release phải bảo toàn compatibility/invariants khi old và new versions có thể cùng tồn tại.

## Kết nối

Đọc [version control/build/packages](../08_software_systems/01_version_control_build_link_and_packages.md), [supply-chain security](../07_security_reliability/08_supply_chain_and_secure_software_lifecycle.md), [reliability/observability](../07_security_reliability/05_fault_tolerance_observability_and_reliability.md) và [maintenance](./04_maintenance_evolution_and_technical_debt.md).