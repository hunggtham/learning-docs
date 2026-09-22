# Buffer pool, replacement và dirty-page management

Database không thể giả định toàn bộ data nằm trong RAM. **Buffer pool** là page cache do database quản lý để giữ working set gần CPU, bảo vệ page lifetime khi operators đang dùng, phối hợp dirty data với WAL, và kiểm soát khi foreground workload phải trả I/O cost.

Mental model quan trọng hơn “buffer pool là cache”: **mỗi page có một lifecycle và một durability frontier**. Replacement quyết định page nào mất residency; pin/latch bảo vệ ownership; dirty state nối page với WAL; checkpoint/writeback quyết định recovery debt; memory pressure quyết định khi nào latency chuyển từ hit-dominated sang I/O-dominated.

## 1. Bài toán ban đầu: RAM nhỏ hơn database, nhưng latency storage đắt

Nếu mỗi logical read phải đọc storage, latency/throughput sẽ rất tệ. Buffer pool giữ hot pages resident và dùng locality của workload.

Nhưng cache của DB khác generic key-value cache vì page có thể:

```text
đang được operator dùng
đang bị update
chứa uncommitted bytes
phụ thuộc vào WAL chưa durable
đang được flush
được nhiều sessions cùng reference
```

Replacement vì vậy phải tôn trọng transaction/recovery invariants, không chỉ “evict key ít dùng”.

## 2. Page table nối logical page id với physical frame

Engine thường cần mapping:

```text
(database/file id, page id)
→ buffer frame in RAM
```

Khi lookup hit, query dùng frame hiện có. Khi miss, engine phải chọn victim hoặc free frame, thực hiện I/O và install mapping mới.

Concurrency làm transition này khó hơn: hai threads cùng miss một page không nên đọc hai copies độc lập rồi cùng publish như authoritative frame. Page table/latch/load-state cần bảo đảm một logical page có representation resident nhất quán theo design.

## 3. Pinning giữ residency; latch/lock giải vấn đề khác

**Pin/reference count** thường ngăn replacement lấy frame đang được operation sử dụng.

**Latch** bảo vệ in-memory data structure/page structure trong thời gian rất ngắn.

**Transaction lock/MVCC** bảo vệ logical concurrency semantics lâu hơn.

Ba mechanism dễ bị trộn:

```text
pin    -> page có được evict không?
latch  -> threads có được mutate in-memory structure cùng lúc không?
lock/MVCC -> transaction nào được đọc/ghi logical state nào?
```

Pin leak có thể làm effective pool capacity giảm dần dù configured buffer size không đổi.

## 4. Page lifecycle là một state machine

Một simplified lifecycle:

```text
not resident
→ read requested
→ I/O in flight
→ clean resident
→ pinned/used
→ dirty resident
→ flush eligible when WAL rule satisfied
→ write in flight
→ clean resident
→ victim/evicted
```

Transitions có thể overlap/concurrent tùy implementation. Reasoning theo state machine giúp debug “page vẫn dirty”, “victim không chọn được”, “flush backlog tăng” tốt hơn việc chỉ nhìn hit ratio.

## 5. Replacement policy đang dự đoán future reuse

Pure LRU dễ bị sequential scan lớn pollute working set: hàng triệu pages chỉ đọc một lần đẩy hot OLTP index/root/leaf pages ra ngoài.

Database thường dùng clock, LRU-K, 2Q-like, scan-resistant hoặc engine-specific policy để ước lượng reuse bằng recency/frequency/history.

Không có replacement “best” universal. Workload quyết định:

```text
OLTP random hot set
sequential analytical scan
mixed read/write
index-heavy vs heap-heavy
multi-tenant working sets
```

Policy tốt phải tránh một workload one-shot phá cache của workload latency-sensitive.

## 6. Dirty page là deferred write debt

Khi page bị update, frame trở thành dirty. Engine trì hoãn flush để batch/merge writes và tránh random synchronous I/O mỗi transaction.

Đổi lại, dirty page là **write debt**: trước khi frame bị evict/reused hoặc trước recovery target nào đó, bytes phải được xử lý theo durability protocol.

Invariant WAL:

> WAL records giải thích page state phải durable đủ trước khi dirty page tương ứng được phép persistent theo write-ahead rule.

Buffer manager vì vậy không thể tách khỏi log manager.

## 7. Dirty-page frontier và WAL frontier phải có ordering

Giả sử page có `pageLSN = 500`. Nếu durable WAL mới tới LSN 450, flush page 500 ra stable storage có thể phá recovery invariant.

Conceptually:

```text
durableWAL >= pageLSN
→ page eligible for safe flush
```

Exact metadata khác engine, nhưng mental model này rất mạnh: page state có một dependency lên log state.

Đọc [MVCC, WAL và recovery internals](./00_mvcc_visibility_wal_and_recovery_internals.md).

## 8. Flush không đồng nghĩa commit và commit không đồng nghĩa page flush

Data page có thể flush trước transaction commit nếu recovery có undo/visibility metadata phù hợp (steal). Ngược lại committed transaction không cần data pages flush ngay nếu WAL đủ để redo (no-force).

Do đó hai graph:

```text
commit latency
page writeback latency
```

có liên hệ nhưng không phải một metric. Commit thường nhạy WAL flush; checkpoint/eviction lại nhạy dirty-page writeback.

## 9. Checkpoint là mechanism trả recovery debt có kiểm soát

Checkpoint giới hạn WAL/history recovery cần scan và thường phối hợp dirty-page flushing.

Nếu checkpoint flush quá aggressive:

```text
background writes burst
→ storage queue sâu
→ foreground WAL/data I/O chậm
→ transaction latency spike
```

Nếu quá lazy:

```text
dirty backlog + WAL retention ↑
→ recovery time/RTO ↑
→ disk space pressure ↑
```

Thiết kế tốt cố smooth writes theo thời gian thay vì tạo cliff định kỳ.

## 10. Background writer và foreground eviction có mục tiêu khác nhau

Background flushing cố biến dirty pages thành clean trước khi foreground thread cần frame. Nếu pool hết clean victims, request miss có thể phải tự chờ flush rồi mới reuse frame.

Đây là transition quan trọng:

```text
healthy: miss → choose clean victim → read page
pressure: miss → all victims dirty/pinned → wait for writeback → read page
```

Tail latency thường tăng mạnh khi system đi vào phase thứ hai dù hit ratio thay đổi ít.

## 11. Sequential scan và admission vào cache

Không phải mọi page đọc vào đều nên có cùng cache priority. Một scan 500 GB có thể có reuse gần zero trong OLTP timeframe.

Scan-resistant policy, separate pools hoặc bypass/admission logic có thể bảo vệ hot set. Câu hỏi design là:

> Page này có xác suất reuse trước khi eviction pressure quay lại đủ cao để đáng chiếm frame không?

Đây là cùng family với cache admission trong software systems.

## 12. Buffer pool và query plan tạo feedback lẫn nhau

Optimizer ước lượng I/O/cost dựa statistics/model, nhưng actual residency làm runtime khác nhau. Index nested-loop có thể tuyệt vời với hot inner pages và tệ với random storage misses.

Ngược lại plan chosen cũng thay cache state: full scan có thể pollute cache; hash join có thể dùng nhiều memory và spill; large sort có thể cạnh tranh buffer memory/I/O.

Do đó benchmark warm cache và cold cache trả lời hai workload khác nhau. Production cần biết working-set evolution chứ không chỉ plan text.

## 13. Double buffering: DB cache và OS page cache có thể cùng giữ data

Với buffered I/O:

```text
DB buffer pool
↔ OS page cache
↔ filesystem/storage
```

cùng block có thể tồn tại ở hai cache layers. Điều này đơn giản hóa một số I/O behavior nhưng duplicate memory và làm engine ít kiểm soát exact write/readahead path hơn.

Direct I/O có thể tránh double caching nhưng engine phải tự lo alignment, async scheduling, readahead và lifetime. Đây là design trade-off, không phải “direct luôn nhanh hơn”.

## 14. Memory pressure phải tính toàn process + OS, không riêng pool

Configured buffer pool quá lớn có thể làm OS thiếu memory cho page tables, stacks, filesystem metadata, network buffers, runtime heap/off-heap hoặc background tools.

Khi kernel reclaim/swapping bắt đầu, latency có thể tăng phi tuyến. Database nhìn “buffer pool hit cao” nhưng host vẫn thrash do tổng working set vượt RAM.

Lower-layer evidence cần gồm host memory/reclaim, không chỉ DB cache metrics.

## 15. NUMA và locality ảnh hưởng in-memory DB behavior

Trên multi-socket host, buffer frames có physical NUMA placement. Threads trên socket khác truy cập remote memory tốn latency/bandwidth interconnect.

Một shared/global buffer metadata lock hoặc hot page cũng có thể tạo cache-line contention dù storage không tham gia.

Khi data đã hot trong RAM, lower abstraction quyết định p99 có thể là NUMA/coherence chứ không phải SSD.

## 16. Multi-tenant noisy neighbor trong buffer pool

Hai tenants cùng pool có thể cạnh tranh working set. Một tenant scan lớn hoặc burst write có thể:

```text
evict tenant khác
consume dirty-page budget
consume I/O queue
increase checkpoint pressure
```

Fairness cần gắn với resource thật: cache admission/quota, I/O scheduling, workload classes hoặc separate pools khi cần. “Tenant priority” trong request metadata không đủ nếu buffer/I/O layer không enforce.

Đây là connection từ buffer manager sang system-level isolation.

## 17. Performance pressure làm behavior đổi phase

Một useful phase model:

```text
Phase A: working set fits → hits dominate
Phase B: misses increase → storage reads visible
Phase C: dirty/victim pressure → foreground waits for flush
Phase D: memory/I/O saturation → queue + checkpoint/reclaim feedback
```

Average latency ở phase A không dự đoán phase C/D. Capacity test phải tăng load/working set đủ để tìm knee.

## 18. Production evidence

Evidence nên đo state machine thay vì một hit ratio:

```text
Residency:
- buffer hit/miss by object/workload
- resident pages / free frames
- pinned/busy frames
- eviction/victim scan cost

Dirty/writeback:
- dirty-page count/ratio
- flush rate and latency
- checkpoint age/duration
- foreground flush/wait events

WAL/storage:
- durable WAL frontier / flush latency
- storage read/write latency distribution
- queue depth/utilization

Host:
- memory pressure/reclaim/swap
- NUMA local/remote memory khi relevant
```

Một hit ratio 99% vẫn có thể che 1% misses cực đắt nằm trên critical path của p99 requests.

## 19. Failure reasoning theo abstraction layer

Nếu query cold chậm, kiểm tra miss/storage path. Nếu latency spike theo chu kỳ, correlate checkpoint/writeback. Nếu buffer pool lớn hơn mà throughput giảm, kiểm tra host reclaim/double caching/NUMA. Nếu commit p99 tăng, đừng mặc định buffer pool; tách WAL flush khỏi data-page writeback. Nếu one tenant gây incident, tìm cache/I/O ownership boundary.

## 20. Mô hình tư duy

> Buffer pool là **working-memory và write-debt manager** của storage engine. Replacement dự đoán reuse; pin/latch giữ page lifetime và in-memory correctness; dirty state nối page với WAL; checkpoint/background writer trả recovery debt; memory/storage pressure quyết định khi foreground bắt đầu chờ. **Hit ratio chỉ là một symptom-level metric; page lifecycle và resource frontier mới giải thích behavior.**

## Kết nối

Ôn [database storage foundation](../../basic/05_data_databases/04_storage_logs_recovery_and_durability.md), đọc [MVCC/WAL](./00_mvcc_visibility_wal_and_recovery_internals.md), [B+Tree pages](./02_bplus_tree_pages_splits_merges_and_latch_coupling.md), [OS memory pressure](../../03_operating_systems/advanced/02_page_faults_reclaim_dirty_pages_and_memory_pressure.md), [filesystem crash consistency](../../03_operating_systems/advanced/04_filesystem_crash_consistency_journaling_and_cow.md) và [durability path](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).