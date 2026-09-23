# Backend Core

Backend Core là lớp kiến thức chung đứng trước Java, Spring và Python. Nó mô tả
backend như một hệ thống nhận request, đọc/ghi state, phát side effect và trả
contract có thể quan sát được. Mục tiêu là tạo một canonical owner cho những
quyết định backend không thuộc riêng một ngôn ngữ hay framework.

## Learning flow

```text
request lifecycle
  → HTTP semantics
  → identity/session
  → persistence and transaction
  → cache and invalidation
  → jobs and messaging
  → timeout/retry/idempotency
  → tests and contracts
  → observability and debugging
  → modular monolith and service boundaries
  → production case studies
```

## Chapters

1. [Backend request lifecycle](./00_backend_request_lifecycle.md)
2. [HTTP API semantics](./01_http_api_semantics.md)
3. [Auth, session và identity](./02_auth_session_identity.md)
4. [Persistence, transaction và ORM](./03_persistence_transactions_orm.md)
5. [Caching và invalidation](./04_caching_and_invalidation.md)
6. [Async jobs và messaging](./05_async_jobs_messaging.md)
7. [Timeout, retry và idempotency](./06_timeout_retry_idempotency.md)
8. [Testing, contract và integration](./07_testing_contract_integration.md)
9. [Observability và debugging](./08_observability_and_debugging.md)
10. [Modular monolith và services](./09_modular_monolith_services.md)
11. [Production backend case studies](./10_production_backend_case_studies.md)

12. [Coverage audit và backlog](./COVERAGE_AUDIT.md)

Mỗi chapter tách rõ **contract**, **mechanism**, **failure mode** và **evidence**.
Đây là lớp reasoning để áp dụng vào framework; không phải danh sách API cần học
thuộc lòng.

`COVERAGE_AUDIT.md` là nơi ghi boundary, owner và các chủ đề cố ý không lặp lại
từ Computer Science. Khi thêm chapter mới, cập nhật audit trước để tránh biến
Backend Core thành một bản sao của database, network hoặc framework library.

## Đường đọc nâng cao

Sau vòng đọc đầu tiên, hãy đọc lại theo các trục xuyên chapter thay vì chỉ đi
theo số thứ tự:

1. **Correctness:** identity → transaction → idempotency → contract test.
2. **Latency:** request budget → cache → queue → dependency timeout → trace.
3. **Durability:** commit → outbox → retry → replay → audit evidence.
4. **Change safety:** API compatibility → expand/contract migration → rollout →
   rollback và mixed-version behavior.
5. **Scale:** hot key → pool saturation → backpressure → queue age → capacity
   limit.

Mỗi trục nên kết thúc bằng một design note ngắn: nêu invariant, failure budget,
observability signal và cách test. Nếu một quyết định chỉ được giải thích bằng
tên framework hoặc product, hãy quay lại chapter tương ứng và viết lại ở mức
contract.
