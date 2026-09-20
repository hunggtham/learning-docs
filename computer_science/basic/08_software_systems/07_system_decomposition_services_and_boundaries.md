# System decomposition, services và boundaries

Một system lớn phải được chia thành modules/services vì một team hay một process không thể giữ toàn bộ complexity trong đầu. Nhưng mỗi boundary cũng tạo communication, versioning và failure cost. Architecture tốt không tối đa số services; nó đặt boundaries nơi coupling thấp và invariants có ownership rõ.

## Module trước microservice

Modularity là principle; microservice chỉ là một deployment/distribution form. Một modular monolith có thể có clean boundaries mà không chịu network/operations overhead.

Chia service quá sớm biến function calls thành remote calls: latency, timeout, retry, serialization, auth và partial failure xuất hiện.

## Cohesion và coupling

High cohesion nghĩa một module chứa responsibilities thay đổi cùng nhau. Low coupling nghĩa modules ít biết internal details của nhau.

Coupling không chỉ source imports. Shared database schema, shared release schedule và synchronized business workflows cũng là coupling.

## Bounded context

Trong Domain-Driven Design, bounded context xác định nơi một domain model/ubiquitous language có meaning nhất quán. “Customer” trong billing có thể khác customer trong support.

Boundary hữu ích khi semantics và ownership khác, không phải chỉ vì table khác.

## Shared database trap

Nếu nhiều services trực tiếp sửa cùng tables, deployment độc lập chỉ là illusion. Schema change cần coordination và service B có thể phá invariant service A.

Ownership thường tốt hơn khi một service owns data và expose contract. Nhưng remote read cho mọi field có latency/coupling cost, nên duplication/read models đôi khi hợp lý.

## Synchronous và asynchronous boundaries

Synchronous call dễ reasoning cho immediate result nhưng caller phụ thuộc availability/latency của callee.

Asynchronous event giảm temporal coupling nhưng thêm eventual consistency và operational complexity.

Chọn interaction model theo business invariant chứ không theo fashion.

## Saga và distributed workflow

Nếu workflow trải qua nhiều services, một ACID transaction global thường không practical. Saga chia thành local transactions với compensation hoặc orchestration/choreography.

Compensation không phải rollback time machine. Gửi hàng rồi “compensate” có thể cần return/refund workflow, không xóa sự kiện đã xảy ra.

## API gateway và service mesh

API gateway tập trung north-south concerns như routing/auth/rate limit. Service mesh xử lý east-west service communication features qua proxies/sidecars hoặc node-level data plane.

Centralization giúp policy consistency nhưng thêm infrastructure dependency và debugging layer.

## Conway's Law

System communication structure thường phản chiếu organization communication. Nếu ownership/team boundaries không khớp architecture, APIs dễ trở thành negotiation bottlenecks.

Architecture vì vậy là socio-technical, không chỉ diagram boxes.

## Distributed monolith

Nếu services phải deploy cùng lúc, gọi nhau chatty synchronous chains và chia shared database, ta nhận overhead distributed system nhưng vẫn coupling như monolith.

Microservices không guarantee autonomy; autonomy đến từ boundaries và contracts.

## Common Misconceptions

**“Microservices scale tốt hơn monolith.”** Một monolith stateless vẫn horizontal scale; microservices chủ yếu cho independent scaling/ownership khi boundaries đúng.

**“Mỗi database table nên là một service.”** Boundary nên theo capability/invariant, không CRUD entity mechanical.

**“Event-driven luôn decoupled.”** Consumers phụ thuộc event schema/semantics và operational timing; coupling chỉ đổi hình thức.

## Mental Model

> Architecture decomposition là bài toán đặt ownership boundaries. Boundary tốt gom invariants và change together; boundary xấu biến internal chatter thành remote distributed failure.

## Kết nối

Đọc [modularity/API](./00_abstraction_modularity_interfaces_and_apis.md), [event-driven](./06_event_driven_and_stream_processing.md), [distributed consistency](../06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md) và [software architecture](../09_software_engineering/01_software_architecture_and_design_reasoning.md).