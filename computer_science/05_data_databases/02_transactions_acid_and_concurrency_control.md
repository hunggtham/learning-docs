# Transactions, ACID và concurrency control

Database transaction (트랜잭션) giải quyết một vấn đề sâu: business operation thường gồm nhiều reads/writes, trong khi crash hoặc concurrent transactions có thể xảy ra giữa bất kỳ bước nào. Ta muốn một higher-level state transition với guarantees rõ ràng thay vì các writes độc lập.

## Atomicity

Atomicity nghĩa transaction effects được coi như all-or-nothing theo contract. Transfer 100 từ A sang B không được debit A rồi crash trước credit B mà để state nửa chừng.

Atomicity thường dựa log/recovery hoặc copy-on-write techniques, không phải hardware thực hiện mọi writes cùng một nanosecond.

## Consistency trong ACID

Consistency ở ACID thường nghĩa transaction đưa database từ state thỏa constraints/invariants sang state thỏa constraints nếu transaction logic đúng. Nó khác “consistency” trong distributed systems/CAP, nơi term nói về views/ordering giữa replicas.

DB không tự biết mọi business invariant. Nếu invariant không encoded hoặc transaction code sai, ACID không cứu logic.

## Isolation

Isolation điều khiển concurrent transactions được phép quan sát nhau đến mức nào. Nếu serializable, outcome tương đương một serial ordering nào đó. Weaker isolation tăng concurrency nhưng cho anomalies.

Dirty read: đọc uncommitted data. Non-repeatable read: cùng row đọc hai lần cho values khác do commit khác. Phantom: predicate query trả thêm/bớt rows. Write skew có thể xảy ra dưới snapshot isolation khi two transactions đọc common snapshot rồi update disjoint rows, phá cross-row invariant.

Isolation-level names trong SQL standards và DB products có implementation differences; cần đọc engine docs.

## Durability

Commit success hứa effects survive defined failures. WAL/redo logs, fsync/device guarantees và replication policy quyết định durability strength. Async replication có thể lose acknowledged data khi primary dies trước replica receive, tùy system.

## Locks

Two-phase locking family dùng shared/exclusive locks để control conflicts. Lock granularity row/page/table ảnh hưởng overhead/contention. Predicate/range locks cần để bảo vệ phantoms ở serializable schemes.

Locks có thể deadlock; DB detect wait-for cycles và abort một transaction. Application phải sẵn sàng retry transaction bị deadlock victim.

## MVCC

Multi-Version Concurrency Control giữ multiple row versions để readers và writers ít block nhau. Transaction đọc snapshot theo visibility rules; update tạo new version.

MVCC không “loại locks hoàn toàn”. Writes/constraints/metadata vẫn cần coordination, và old versions cần vacuum/garbage collection.

## Optimistic concurrency

Optimistic scheme cho work tiến hành rồi validate version/timestamp trước commit. Nếu conflict, retry. Hợp khi conflicts hiếm; khi hot contention cao, retries có thể waste work.

Application pattern `UPDATE ... WHERE id=? AND version=?` là simple compare-and-swap at DB level.

## Serializability

Serializability là correctness criterion: concurrent execution equivalent về effect với một serial schedule. Conflict serializability có thể analyze precedence graph; cycle chỉ non-serializable schedule.

Serializable Snapshot Isolation dùng dependency tracking để abort dangerous structures thay vì lock mọi read theo classic 2PL.

## Transaction boundary

Transaction quá lớn giữ versions/locks lâu, tăng contention và recovery cost. Quá nhỏ làm business invariant split. Boundary nên match atomic invariant, không phải mỗi repository method mặc định.

Remote API call bên trong DB transaction nguy hiểm vì latency/failure kéo dài locks. Saga/outbox patterns giải cross-service workflows với weaker atomicity và compensations.

## Mental Model

> Transaction là **một state transition có contract dưới concurrency và crash**. ACID không phải bốn checkbox độc lập; implementation phối hợp isolation + logging + constraints để giữ invariants.

## Common Misconceptions

**“ACID consistency = CAP consistency.”** Hai khái niệm khác context.

**“MVCC nghĩa không có blocking.”** Writes, DDL, constraints và cleanup vẫn có conflicts.

**“READ COMMITTED đủ vì không dirty read.”** Cross-row invariants và lost-update/write-skew patterns vẫn cần review.

## Kết nối

[Concurrency/deadlock](../03_operating_systems/02_concurrency_synchronization_and_deadlock.md) là same family problem ở shared memory. [WAL/recovery](./04_storage_logs_recovery_and_durability.md) hiện thực atomicity/durability. Cross-node transactions gặp [distributed consistency/consensus](../06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md).
