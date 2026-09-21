# Abstraction, modularity, interface và API contracts

Software lớn không thể được hiểu toàn bộ cùng lúc. Modularity (모듈성 / tính mô-đun) chia system thành boundaries để mỗi phần có thể reasoning, thay đổi và test tương đối độc lập. Nhưng boundary chỉ hữu ích khi interface contract rõ và information hiding đúng.

## Module là unit của responsibility và change

Module có thể là function, class, package, library, service hoặc subsystem. Ranh giới tốt thường gom những decisions có lý do thay đổi cùng nhau và che implementation details khỏi consumers.

High cohesion nghĩa elements trong module phục vụ purpose liên quan. Low coupling nghĩa module phụ thuộc ít assumptions về internals của module khác.

Coupling không thể bằng zero; mục tiêu là dependencies explicit và stable.

## Information hiding

Parnas' principle: module nên hide design decisions likely to change. Encapsulation không chỉ `private` fields; nó che representation và expose operations theo semantic contract.

Ví dụ stack expose push/pop thay vì cho caller sửa internal array index. Database repository expose query intent thay vì leak connection/cursor lifecycle nếu caller không cần.

## Interface vs implementation

Interface (인터페이스) mô tả operations/behavior consumer có thể dựa; implementation có freedom nội bộ. Nhưng interface contract rộng hơn method signature: ordering, nullability, errors, concurrency, idempotency, latency expectations và compatibility đều có thể observable.

Một API trả list nhưng không nói ordering có stable không; client vô tình dựa current order; implementation đổi query plan làm order khác — đó là hidden contract dependency.

## Dependency inversion

High-level policy không nên phụ thuộc trực tiếp low-level volatile details nếu boundary abstraction hợp lý. Dependency inversion đưa interface theo needs của high-level module, implementation adapters implement.

Nhưng tạo interface cho mọi class không tự động decouple; abstraction vô nghĩa chỉ tăng indirection. Interface đáng có khi có genuine boundary/variation/testing ownership.

## API design

Good API làm correct use dễ và misuse khó. Types encode valid states; names match domain; default safe; errors explicit; operations composable.

Backward compatibility là contract evolution problem. Adding optional response field usually easier than removing/renaming required field. Semantic behavior changes can break clients even if schema unchanged.

## Versioning

Semantic Versioning convention major/minor/patch chỉ hữu ích nếu project defines public API and follows semantics. Distributed HTTP APIs may use URL/header versions, additive evolution or capability negotiation.

Version proliferation creates maintenance burden; prefer compatible evolution when possible.

## Local vs remote interface

Remote Procedure Call can look like local function but semantics differ: latency orders of magnitude, timeout, partial failure, retries, serialization and version skew. Treating remote API exactly like local method is a classic leaky abstraction.

A remote call needs timeout, cancellation, idempotency/retry policy and observability. Chatty object-style APIs that are fine in-process may be terrible over network.

## Contract testing

Consumer/provider contract tests verify interaction assumptions without full E2E environment. But contract should focus observable behavior, not freeze internal implementation.

Schemas like OpenAPI/Protobuf capture structural contract; semantic constraints still need documentation/tests.

## Conway's Law intuition

System architecture often mirrors communication structure of organization. Team boundaries influence service/module boundaries because coordination cost is real. Modular design is technical + organizational.

## Mental Model

> A boundary is valuable when it **contains change and preserves a small stable contract**. Ask what assumptions cross boundary, not how many interfaces/classes exist.

## Common Misconceptions

**“More layers = better architecture.”** Layers without distinct responsibility add latency/indirection.

**“Interface means abstraction.”** Interface with one implementation mirroring every internal method may reveal rather than hide design.

**“RPC is just function call across network.”** Remote calls have fundamentally different failure/latency semantics.

## Kết nối

[Abstraction/invariants](../00_computation_information/03_logic_state_abstraction_and_invariants.md) is foundation. [Distributed failure](../06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md) explains remote boundaries. [Version control/build](./01_version_control_build_link_and_packages.md) manages module evolution physically.
