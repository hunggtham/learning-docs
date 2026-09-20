# Software architecture và design reasoning

Architecture không phải sơ đồ boxes đẹp; nó là tập decisions khó thay đổi về boundaries, data ownership, communication, deployment và quality attributes. Design tốt bắt đầu từ forces/constraints chứ không từ pattern names.

## Architecture như set of consequential decisions

Một decision “dùng PostgreSQL” có impact khác “field này tên `createdAt`”. Architecture decisions thường ảnh hưởng nhiều modules/teams và migration cost cao.

Do đó Architecture Decision Record (ADR) nên ghi context, options, decision và consequences. Mục tiêu không phải bureaucracy mà giữ reasoning cho future maintainers.

## Quality attributes tạo architecture

Availability, latency, security, modifiability, scalability và cost thường conflict.

Ví dụ synchronous replication tăng durability/consistency nhưng tăng write latency và giảm availability khi replicas unavailable. Architecture chỉ có ý nghĩa khi gắn với quality priorities.

## Coupling và cohesion

Cohesion cao gom behavior/data thay đổi cùng nhau. Coupling thấp giảm số assumptions xuyên boundaries.

Coupling có nhiều dạng: compile-time, runtime, data schema, temporal, organizational. Hai services không import code nhau nhưng cùng phụ thuộc release window vẫn bị coupled.

## Information hiding

Module nên hide volatile design decision sau stable interface. Một storage module expose `saveOrder()` thay vì cho callers phụ thuộc table layout nếu layout có khả năng thay đổi.

Information hiding giảm blast radius của change.

## Layering

Layer architecture tạo direction dependencies: presentation → application → domain → infrastructure tùy style. Layer giúp separation nhưng excessive layering có thể tạo pass-through boilerplate.

Layer là tool cho dependency control, không phải rule rằng mọi request phải đi qua N classes.

## Hexagonal/ports-and-adapters intuition

Domain logic phụ thuộc abstractions/ports; external DB/UI/message broker là adapters. Goal là business rules không bị hard-wire vào framework infrastructure.

Nhưng nếu domain đơn giản, thêm abstraction interfaces everywhere có thể overengineering. Boundary nên bảo vệ volatility thật.

## Architecture patterns và context

Monolith, microservices, event-driven, CQRS, layered, pipes-and-filters không phải maturity ladder. Mỗi pattern giải một set forces và tạo liabilities.

CQRS tách read/write models khi needs khác mạnh, nhưng thêm synchronization/evolution complexity. Event sourcing cho audit/replay nhưng làm schema evolution và debugging khó hơn.

## Data ownership

Architecture boundary mạnh thường cần ownership của state. Shared writable database làm services/modules phụ thuộc hidden invariants.

Ownership không đồng nghĩa không chia sẻ data; nó nghĩa một component có authority update và others truy cập qua contract/copy phù hợp.

## Dependency inversion

High-level policy không nên phụ thuộc concrete low-level implementation khi volatility/coupling cần tách. Dependency inversion dùng interfaces/abstractions để direction source dependency phục vụ stability.

Nhưng interface chỉ có một implementation và không có volatility không tự động hữu ích.

## Architecture fitness functions

Một architecture intent có thể degrade theo thời gian. Automated checks như dependency rules, API compatibility tests, latency SLO, security policy scans có thể đóng vai fitness functions để phát hiện drift.

Architecture vì vậy không chỉ là initial design; nó cần continuous verification.

## Common Misconceptions

**“Architecture là chọn framework.”** Framework là implementation decision; architecture lớn hơn là boundaries và quality trade-offs.

**“Pattern nổi tiếng nghĩa là best practice.”** Pattern chỉ hợp khi forces tương ứng tồn tại.

**“Clean architecture càng nhiều layers càng clean.”** Indirection không có purpose làm system khó hiểu hơn.

## Mental Model

> Architecture là cách phân bố responsibilities và constraints sao cho những thay đổi/failures quan trọng bị giới hạn trong boundaries hợp lý.

## Kết nối

Đọc [system decomposition/services](../08_software_systems/07_system_decomposition_services_and_boundaries.md), [requirements](./00_requirements_specification_and_engineering_process.md) và [maintenance/technical debt](./04_maintenance_evolution_and_technical_debt.md).