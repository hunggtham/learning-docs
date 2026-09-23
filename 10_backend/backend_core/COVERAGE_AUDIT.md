# Backend Core — coverage audit

Ngày audit: 2026-09-23. Audit này kiểm tra **coverage của reasoning**, không đếm
số keyword hay số dòng. Một chủ đề được coi là covered khi có contract, invariant,
failure mode và cách thu evidence; API/tool cụ thể có thể nằm ở implementation
track.

## Coverage matrix

| Năng lực | Owner | Trạng thái | Evidence trong library |
|---|---|---|---|
| request admission và lifecycle | `00` | covered | state machine, timeout/cancellation, admission control |
| HTTP contract và compatibility | `01` | covered | status/error, idempotency, ETag, version matrix |
| identity/session/authorization | `02` | covered | subject/tenant, rotation, revocation, async policy |
| persistence/transaction/ORM | `03` | covered | transaction matrix, lost update, migration |
| cache/invalidation | `04` | covered | staleness budget, key schema, stampede |
| jobs/messaging | `05` | covered | delivery, outbox, ordering, replay, lease |
| timeout/retry/idempotency | `06` | covered | retry topology, unknown result, deadline |
| testing/contracts | `07` | covered | invariant tests, fault injection, test matrix |
| observability/debugging | `08` | covered | causal graph, sampling, cardinality, mitigation |
| architecture boundaries | `09` | covered | module ownership, extraction fitness, read model |
| production reasoning | `10` | covered | 8 cases + capstone |
| configuration/secrets lifecycle | `00`/`02` | covered at core level | source, precedence, validation, rotation, access và drift |
| load/performance/capacity testing | `06`/`07`/`08` | covered | pool/backpressure, workload model, SLO và saturation |
| API security headers/CORS/rate policy | `01`/`02` | covered | limiter contract, CORS boundary, validation, auth |
| privacy/data retention/erasure | `02`/`03`/`08` | covered at core level | lifecycle, deletion scope, redaction và telemetry classification |

## Boundary cố ý không duplicate

- Database internals (MVCC, WAL, indexes, query optimizer) thuộc
  [`computer_science/05_data_databases/`](../../computer_science/05_data_databases/).
- TCP/TLS/DNS, queue internals, ordering và distributed consensus thuộc
  [`computer_science/06_networks_distributed_systems/`](../../computer_science/06_networks_distributed_systems/).
- Process, memory, filesystem và resource isolation thuộc các chapter systems
  trong [`computer_science/`](../../computer_science/README.md).
- Threat model, cryptography và secure software lifecycle thuộc
  [`computer_science/07_security_reliability/`](../../computer_science/07_security_reliability/).
- Java/Python runtime semantics và Spring API thuộc các track implementation
  bên cạnh, không trở thành prerequisite ngầm của Backend Core.

## Backlog có thứ tự

1. Bổ sung một design worksheet cho configuration/secrets lifecycle nếu các
   implementation track bắt đầu dùng chung một policy.
2. Tạo thêm case về multi-region/data residency chỉ khi repository có owner rõ
   cho deployment và legal boundary; không kéo topic này vào core quá sớm.
3. Chỉ tạo chapter riêng khi các phần trên đủ lớn và có invariant khác biệt;
   không tách file chỉ để tăng số lượng.

## Tiêu chí hoàn tất một update

Mỗi update mới cần:

1. chỉ rõ canonical owner và boundary;
2. thêm ít nhất một failure mode hoặc trade-off, không chỉ thêm định nghĩa;
3. nối design với test và telemetry;
4. có case hoặc bài tập để kiểm tra causal reasoning;
5. chạy link/whitespace check trước khi merge.
