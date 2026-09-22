# MVCC, visibility, WAL và recovery internals

Ở mức foundation, ACID và MVCC thường được mô tả như cơ chế giúp nhiều transactions chạy đồng thời mà ít block nhau. Ở mức advanced, cần tách ba câu hỏi nhưng vẫn nối chúng thành một lifecycle:

```text
Visibility : transaction nào được nhìn thấy version nào?
Durability : history nào sống sót crash?
Reclamation: khi nào history cũ có thể bị quên?
```

Mental model của chương này là: **MVCC, WAL, buffer pool, checkpoint, vacuum/purge và replication đều quản lý các representation khác nhau của cùng logical transaction history. Correctness phụ thuộc vào việc các representation đó không vượt quá authority mà transaction state cho phép.**

## 1. Bài toán ban đầu: concurrency không được phá một lịch sử hợp lệ

Nếu reader luôn block writer và writer luôn block reader, correctness dễ hơn nhưng concurrency thấp. MVCC cho phép nhiều logical versions cùng tồn tại để reader có snapshot ổn định trong khi writer tiếp tục tạo state mới.

Invariant cơ bản:

> Một transaction chỉ được quan sát versions phù hợp với isolation/snapshot contract, và crash recovery không được biến physical bytes chưa có commit authority thành committed history.

Hai nửa của câu này nối visibility với durability.

## 2. MVCC biến một logical row thành version history

Implementation khác nhau giữa engines: tuple versions, undo chain, version store, transaction metadata hoặc combination. Nhưng abstraction hữu ích là:

```text
logical row
→ version v1 created by T1
→ version v2 created by T2
→ version v3 deleted/updated by T3
```

Reader không lấy “version mới nhất theo wall clock”. Nó chạy một **visibility function(snapshot, version, transaction state)**.

Đây là reason hai transactions cùng query một key tại gần cùng thời điểm có thể hợp lệ khi nhìn thấy hai answers khác nhau.

## 3. Snapshot là một contract về transaction order, không phải copy toàn database

Snapshot thường encode đủ information để phân biệt transaction đã commit trước boundary, transaction đang active và transaction bắt đầu sau boundary.

Reasoning generic:

```text
version do transaction nào tạo?
creator đã commit theo snapshot chưa?
version đã bị transaction nào supersede/delete?
transaction đó có visible đối với snapshot không?
```

Một snapshot không nhất thiết materialize mọi row. Nó là metadata/rule để evaluate visibility khi row được đọc.

## 4. Visibility không tự bảo đảm serializability

MVCC giảm read-write blocking nhưng isolation level vẫn quyết định anomalies nào được phép. Snapshot isolation có thể ngăn nhiều dirty/non-repeatable phenomena nhưng không tự động loại mọi write skew hoặc predicate anomaly.

Do đó “DB dùng MVCC” không trả lời transaction correctness. Cần hỏi:

```text
application invariant là gì?
isolation level nào đang active?
write-write conflict được detect thế nào?
predicate/range dependency có được bảo vệ không?
```

Đọc [lock manager, predicate locking và serializable isolation](./01_lock_manager_predicate_locking_and_serializable_isolation.md).

## 5. Update không nhất thiết overwrite state cũ

Một update thường tạo version mới hoặc ghi new state kèm undo information. Old version phải tiếp tục tồn tại nếu snapshot cũ vẫn có quyền đọc nó.

Điều này đổi cost model:

```text
reader ít block writer hơn
↔
engine phải giữ version metadata, old tuples/undo và reclamation work
```

Long-running transaction vì vậy không chỉ “giữ connection lâu”; nó có thể giữ transaction horizon cũ và ngăn cleanup của lượng history lớn.

## 6. Transaction state là authority của version

Bytes của version có thể đã nằm trong buffer pool hoặc thậm chí data page đã được write xuống storage trước commit. Physical existence không đồng nghĩa logical visibility.

Engine phải giữ enough metadata để phân biệt:

```text
uncommitted
committed
aborted
in-progress / unknown until recovery resolves
```

Invariant là **recovery và visibility logic phải cùng hiểu transaction authority**. Nếu crash xảy ra giữa physical write và commit record, page bytes không được tự nhiên biến thành committed row.

## 7. WAL giải durability bằng write-ahead rule

**Write-Ahead Logging (WAL / 선행 기록 로그)** yêu cầu log information đủ để recovery một page change phải đạt durability cần thiết **trước** khi dependent data page được phép persistent theo protocol.

Simplified:

```text
modify page in buffer pool
→ append WAL record
→ WAL reaches required durable position
→ dirty data page may be flushed later
```

Data pages không cần flush mỗi commit. Sequential-ish log flush thường rẻ hơn random page flush và cho phép group commit.

## 8. Commit acknowledgement có một boundary cụ thể

Một transaction có thể đi qua:

```text
business logic finished
→ commit record generated
→ WAL buffered
→ WAL flush requested
→ durable boundary reached
→ transaction marked/announced committed
→ client acknowledgement
```

Exact sequence khác engine, nhưng invariant tổng quát là:

> `COMMIT OK` không được mạnh hơn durability policy mà engine đã thực sự đạt.

Nếu policy là asynchronous/local-only, guarantee yếu hơn synchronous replicated durability. Từ “commit” phải luôn đi cùng failure model.

## 9. Steal/no-steal và force/no-force quyết định recovery burden

Nếu dirty page của uncommitted transaction được phép ghi ra disk, policy là **steal** và recovery cần cách undo/ignore effects chưa commit.

Nếu committed pages không bắt buộc flush ngay khi commit, policy là **no-force** và recovery cần redo committed changes chưa tới data file.

High-performance engines thường thích steal + no-force vì sử dụng buffer/storage hiệu quả, đổi lại recovery metadata/logging phức tạp hơn.

## 10. LSN nối logical log order với physical page state

**Log Sequence Number (LSN)** tạo logical order cho WAL records. Data page có thể lưu `pageLSN` cho biết nó đã phản ánh log tới position nào.

Invariant:

```text
durable WAL position phải đủ để giải thích durable page state
```

Recovery có thể so pageLSN với log record LSN để tránh redo update đã reflected.

Đây là connection trực tiếp sang filesystem/device ordering: nếu storage làm page durable nhưng log mà page phụ thuộc chưa thật sự persistent theo contract, WAL invariant bị phá.

## 11. Recovery là một state machine, không phải “load backup”

Nhiều WAL-based systems có conceptual phases tương tự:

```text
xác định transaction/page/log state cần quan tâm
→ redo effects cần tái tạo committed/known history
→ undo/ignore effects không được authority tùy architecture
→ rebuild runtime transaction metadata
```

Không phải mọi engine dùng ARIES hay cùng exact algorithm. Mental model quan trọng là recovery **reconstructs a valid logical history from durable evidence**, không đơn giản đọc data file như final truth.

## 12. Crash scenarios làm invariant rõ hơn

### WAL durable, data page chưa flush

Đây là no-force case bình thường. Recovery redo từ WAL.

### Data page có bytes của uncommitted transaction

Nếu engine cho steal, recovery/visibility metadata phải bảo đảm bytes đó không trở thành committed history.

### Crash sau commit log durable nhưng trước client nhận response

Sau restart transaction có thể đã committed dù client timeout/connection drop. Application retry side effect cần idempotency vì client không biết final outcome.

### Crash quanh checkpoint

Checkpoint metadata có thể incomplete theo moment crash; recovery protocol phải có boundary để xác định checkpoint nào usable và WAL range nào cần scan.

Những case này cho thấy database failure semantics nối trực tiếp với application retry semantics.

## 13. Checkpoint giới hạn recovery debt chứ không định nghĩa commit truth

Checkpoint ghi enough metadata và/hoặc thúc đẩy dirty pages để recovery không phải replay vô hạn WAL history.

**Fuzzy checkpoint** cho phép workload tiếp tục, nên checkpoint không nhất thiết là global instant nơi mọi dirty page sạch.

Trade-off:

```text
checkpoint quá aggressive
→ foreground I/O pressure / latency spikes

checkpoint quá thưa
→ WAL retention + recovery time ↑
```

Đây là balancing giữa steady-state throughput và RTO.

## 14. Group commit đổi timing, không đổi durability invariant

Nếu mỗi transaction tự flush WAL, storage flush latency giới hạn throughput. Group commit gom nhiều commit records vào một persistence operation.

```text
T1 ─┐
T2 ─┼→ durable WAL flush → acknowledge group
T3 ─┘
```

Một transaction có thể chờ thêm để batch, nhưng acknowledgement vẫn chỉ được phát sau boundary policy yêu cầu. Optimization được phép đổi batching/timing, không được âm thầm làm yếu API contract.

## 15. Torn page và page-image strategy

Storage atomic-write granularity có thể nhỏ hơn database page. Power loss giữa page write có thể tạo page một phần old, một phần new.

Checksum detect corruption nhưng recovery cần mechanism bổ sung: WAL redo, full-page image, double-write, COW page hoặc strategy khác tùy engine.

Invariant là **recovery không được tin một partial physical write như logical page hoàn chỉnh**.

## 16. Vacuum/purge là garbage collection của version history

Old version không thể xóa chỉ vì có version mới. Engine cần biết không còn snapshot hợp lệ nào có thể nhìn thấy old state.

Reclamation horizon có thể bị kéo lùi bởi:

```text
long-running transaction
idle transaction holding snapshot
replica/read-only consumer cần old log/history
backup/export snapshot
```

Hậu quả: table/index bloat, undo/version-store growth, more I/O/cache pressure và đôi khi transaction-ID/version metadata pressure tùy engine.

## 17. Replica làm lifecycle kéo dài sang distributed state

Một replica có thể nhận WAL/log nhưng chưa apply; đã persist nhưng chưa visible; hoặc lag phía sau leader.

Do đó cần tách positions:

```text
leader generated
→ sent
→ replica received
→ replica persisted
→ replica replayed/applied
→ read visibility reached
```

Read from replica có consistency contract phụ thuộc position đó. Failover lại phụ thuộc replica nào có authority/history đủ để trở thành leader.

Đọc [multi-region replication và failover](../../06_networks_distributed_systems/advanced/05_multi_region_replication_and_geo_distributed_tradeoffs.md).

## 18. Performance pressure thay đổi behavior theo subsystem

High write rate tăng WAL bytes, dirty pages, checkpoint debt và vacuum work. Long snapshots tăng retained history. Random read miss tăng buffer-pool I/O. Replica lag kéo dài retention hoặc làm failover/read freshness xấu.

Các subsystem tạo feedback:

```text
write load ↑
→ dirty/WAL ↑
→ checkpoint/storage pressure ↑
→ commit/read latency ↑
→ transaction lifetime ↑
→ MVCC horizon older
→ cleanup debt ↑
```

Vì vậy root cause có thể không nằm ở query text đang chậm.

## 19. Production evidence: quan sát history ở nhiều representations

Evidence generic nên gồm:

```text
Transaction/MVCC:
- active/long transaction age
- snapshot horizon / old-version retention
- abort/conflict rate
- table/index/undo/version-store bloat

WAL/recovery:
- WAL generation rate
- flush latency / group size
- checkpoint duration/frequency
- recovery/replay position

Buffer/storage:
- dirty-page count
- buffer hit/miss và eviction pressure
- foreground/background I/O latency

Replication:
- send/receive/persist/apply positions
- replication lag
- failover term/epoch/leader timeline
```

Metric names khác DBMS; mental model là đo **visibility horizon + durable-log frontier + dirty-page frontier + replica frontier**.

## 20. Abstraction nào thực sự quyết định behavior?

Nếu reader thấy stale state, kiểm tra snapshot/isolation/replica position trước khi nghi disk. Nếu committed data mất sau crash, kiểm tra WAL acknowledgment và storage durability path. Nếu DB phình dù traffic nhỏ, kiểm tra old snapshot horizon. Nếu p99 commit spike, kiểm tra WAL flush/checkpoint/storage queue chứ không chỉ CPU.

## 21. Mô hình tư duy

> MVCC quyết định **ai nhìn thấy version nào**; transaction state quyết định **version nào có authority**; WAL/recovery quyết định **history nào sống sót crash**; checkpoint giới hạn **recovery debt**; vacuum/purge quyết định **khi nào history cũ có thể bị quên**; replication kéo cùng history qua nhiều nodes. **Correctness đến từ việc mọi representation tôn trọng cùng transaction authority, còn performance đến từ cách system trì hoãn, batch và reclaim work mà không phá invariant.**

## Kết nối

Ôn [Transactions/ACID](../../basic/05_data_databases/02_transactions_acid_and_concurrency_control.md), [storage/WAL foundation](../../basic/05_data_databases/04_storage_logs_recovery_and_durability.md), đọc [buffer pool](./04_buffer_pool_replacement_and_dirty_page_management.md), [filesystem crash consistency](../../03_operating_systems/advanced/04_filesystem_crash_consistency_journaling_and_cow.md), [distributed transactions](./07_distributed_transactions_2pc_consensus_sagas_and_outbox.md) và [durability path xuyên tầng](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).