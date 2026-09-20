# Storage engine, WAL, recovery và durability

Một transaction commit cần biến logical change thành bytes trên storage sao cho crash ở bất kỳ thời điểm nào vẫn recover được state hợp lệ. Storage engine giải vấn đề bằng pages, buffers, logs, checksums và recovery protocols.

## Pages là đơn vị quản lý

Database thường quản lý fixed-size pages/blocks chứa rows/index nodes/metadata. Buffer pool cache pages trong RAM. Query operator yêu cầu logical row; storage layer pin/fetch page, parse slots/records.

Page size cân bằng metadata, I/O granularity và fragmentation. Large sequential scans khác random OLTP lookups.

## Buffer pool

Buffer pool giảm device I/O bằng caching pages. Dirty page đã modified nhưng chưa flushed. Eviction policy approximates working-set value, nhưng DB còn phải cân nhắc dirty flush và scan pollution.

Database cache và OS page cache có thể double-cache tùy I/O mode.

## Write-Ahead Logging

WAL (Write-Ahead Log / 미리 쓰기 로그, 선행 기록 로그) principle: log record mô tả change phải đạt durable storage trước data page chứa change được coi durable/allowed flush theo protocol.

Tại commit, system thường cần ensure relevant log records + commit marker durable, không nhất thiết flush all data pages. Sequential log write rẻ hơn random page flush; background checkpoint sau đó write dirty pages.

## REDO và UNDO

Recovery sau crash phân tích log để redo committed changes chưa lên data pages và/hoặc undo uncommitted changes tùy algorithm. ARIES-style recovery dùng WAL + LSN + physiological logging, nhưng engines vary.

MVCC engines có additional version/undo mechanisms. Mental model quan trọng hơn product details: log cung cấp history đủ để reconstruct consistent durable state.

## Checkpoint

Không thể replay log từ ngày đầu. Checkpoint ghi metadata/flush state để giới hạn recovery work, nhưng checkpoint quá aggressive tăng I/O. It is not necessarily “copy whole DB”.

## Torn writes và checksums

Power loss có thể leave partial page writes tùy device guarantees. Page checksums detect corruption. Doublewrite buffer, full-page images, copy-on-write hoặc atomic-sector assumptions mitigate torn pages.

Durability chain đi qua DB → filesystem → kernel cache → device controller → flash media. Mỗi layer phải respect flush/barrier semantics.

## WAL khác replication log

Local WAL phục vụ crash recovery/durability. Replication có thể stream WAL/binlog/oplog tới replicas. Nhưng replication acknowledgements policy quyết định commit durability across node loss.

Async replica có lag; synchronous quorum tăng latency nhưng durability/consistency mạnh hơn tùy protocol.

## LSM tree intuition

Log-Structured Merge Tree tối ưu write throughput bằng append/memtable rồi flush sorted SSTables, background compaction merge levels. Reads có thể cần consult multiple files nhưng Bloom filters/indexes giúp.

B-tree update in-place pages; LSM chuyển random writes thành sequential writes nhưng chịu compaction/write amplification. Storage workload quyết định.

## Backup khác replication

Replica có thể faithfully replicate accidental DELETE; nó không thay backup. Backup needs point-in-time/history/independent failure domain. WAL archiving + base backup có thể support point-in-time recovery.

## Mental Model

> Durability không phải “ghi file”. Nó là **protocol về ordering**: log history phải bền trước khi data pages được phép lag; recovery dùng history đó để biến crash-time partial writes thành committed state.

## Common Misconceptions

**“Commit phải flush mọi changed page.”** WAL cho phép commit bằng durable log trước, data pages flush sau.

**“Replica = backup.”** Replica bảo availability/read scaling; logical corruption có thể replicate ngay.

**“SSD không cần WAL vì nhanh.”** WAL là correctness/recovery mechanism, không chỉ performance workaround.

## Kết nối

[Filesystem durability](../03_operating_systems/04_filesystems_storage_and_io.md) là lower layer; [transactions](./02_transactions_acid_and_concurrency_control.md) là user-visible contract; [replication/consensus](../06_networks_distributed_systems/05_replication_partitioning_and_consensus.md) mở durability từ một machine sang cluster.
