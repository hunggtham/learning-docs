# Đường đi của durability: application transaction → MVCC/WAL → filesystem → storage → replication

Khi application nhận `COMMIT OK`, câu hỏi đúng không phải chỉ là “database đã ghi xuống disk chưa?”. Một transaction đi qua nhiều state machine và nhiều failure boundary: application transaction, MVCC/lock state, WAL, buffer pool, kernel page cache hoặc direct-I/O path, filesystem/block layer, controller, non-volatile media và có thể cả replication protocol.

Muốn hiểu **độ bền dữ liệu (durability / 내구성)** phải xác định chính xác invariant nào được giữ tại từng tầng và acknowledgement ở tầng trên được phép phát ra sau evidence nào ở tầng dưới.

## 1. Invariant cốt lõi: acknowledgement không được mạnh hơn state đã đạt

Một durability contract có thể phát biểu như sau:

> Sau khi hệ thống trả success cho một transaction ở durability level X, mọi failure nằm trong failure model của X phải vẫn cho phép recovery một lịch sử chứa transaction đó đúng theo consistency contract.

Điều này quan trọng vì “failure model” khác nhau giữa các mode. Local durable commit có thể chỉ bảo vệ process/host crash với storage còn nguyên. Synchronous replicated commit có thể yêu cầu survive mất leader hoặc cả một failure domain. Async commit có thể chủ động chấp nhận một cửa sổ mất dữ liệu.

Không nên dùng từ `commit` mà bỏ qua phần contract này.

## 2. Transaction visibility và durability là hai trục khác nhau

MVCC trả lời **version nào được phép nhìn thấy**; WAL/recovery trả lời **history nào sống sót sau crash**. Hai subsystem gặp nhau ở transaction identity và commit state.

Một version có thể đã tồn tại trong buffer pool nhưng chưa được transaction khác phép nhìn thấy. Một data page có thể đã được ghi ra storage dù transaction tạo thay đổi trên đó chưa commit; recovery phải dùng WAL/undo/transaction metadata để không biến state vật lý thành state logic hợp lệ một cách sai lầm.

Do đó invariant không phải “disk luôn chỉ chứa committed data”. Invariant là recovery có đủ information và ordering để dựng lại **committed history hợp lệ**.

Đọc sâu hơn tại [MVCC, visibility, WAL và recovery internals](../../05_data_databases/advanced/00_mvcc_visibility_wal_and_recovery_internals.md).

## 3. WAL giải bài toán gì?

**Nhật ký ghi trước (Write-Ahead Logging, WAL)** yêu cầu log chứa đủ information để recovery một thay đổi phải đạt durability cần thiết trước khi data page phụ thuộc vào log đó được coi là an toàn để ghi theo protocol.

Mental model:

```text
log trước
page sau
```

Database không cần flush mọi data page khi commit. Sequential log flush thường rẻ hơn buộc nhiều random data-page writes đồng bộ, vì vậy WAL vừa bảo vệ correctness vừa tạo performance architecture cho storage engine.

## 4. LSN nối log với page state

**Log Sequence Number (LSN)** tạo logical order của log records. Data page có thể mang `pageLSN` cho biết page đã phản ánh log tới đâu. Recovery so sánh log position với page state để quyết định redo nào còn cần thiết.

Đây là một invariant rất cụ thể:

```text
page state không được đi trước durable log state theo cách làm recovery mất khả năng giải thích page đó
```

Nếu write ordering bị phá ở storage stack, WAL protocol có thể mất ý nghĩa dù database code nhìn đúng.

## 5. `write()` success không đồng nghĩa durable

`write()` thường chỉ chứng minh kernel đã nhận bytes. Với buffered I/O, bytes có thể mới nằm trong **bộ đệm trang (page cache)** và page chỉ được đánh dấu dirty.

```text
write() success
≠
non-volatile persistence
```

Primitive như `fsync`, `fdatasync`, `O_DSYNC` hoặc mechanism tương đương truyền durability intent xuống stack. Nhưng guarantee cuối vẫn phụ thuộc filesystem, block layer, driver và device thực hiện đúng contract.

## 6. Page cache và buffer pool tạo hai lớp state

Database thường có buffer pool riêng. OS lại có page cache. Nếu database dùng buffered file I/O, cùng logical data có thể đi qua cả hai lớp cache; direct I/O có thể giảm double caching nhưng không làm crash consistency tự động đúng.

Pressure ở hai tầng cũng tương tác: database dirty-page policy ảnh hưởng writeback burst; kernel reclaim có thể tạo I/O contention; device queue depth và flush latency lại phản hồi ngược lên commit latency.

Vì vậy “DB CPU thấp nhưng commit p99 tăng” vẫn có thể là storage-stack problem.

## 7. Filesystem ordering và journaling

Filesystem phải bảo vệ metadata/data structure của chính nó qua crash. Journaling hoặc copy-on-write filesystem dùng protocol riêng để giữ filesystem-consistency invariant.

Database WAL và filesystem journal không trùng boundary:

```text
database WAL      -> transaction/recovery semantics
filesystem journal -> filesystem metadata/data-structure consistency
```

Một lớp không tự thay thế lớp kia. Database vẫn cần biết write/flush semantics mà filesystem cung cấp.

## 8. Controller cache, flush và power-loss protection

SSD/HDD có thể có volatile write cache. Nếu controller báo complete trước khi data đến non-volatile media, power loss có thể làm mất write trừ khi device có power-loss protection hoặc firmware thực hiện flush semantics đúng.

Do đó một chuỗi durability thực tế là:

```text
DB WAL flush intent
→ syscall
→ filesystem/block ordering
→ device flush/FUA semantics
→ controller
→ non-volatile media
```

Mỗi boundary là một nơi abstraction có thể leak nếu guarantee bị hiểu sai.

## 9. Torn write và atomicity granularity

Database page có thể lớn hơn atomic write unit của storage. Power loss giữa write có thể tạo **ghi rách (torn write)**: một phần page mới, một phần cũ.

Checksum chỉ giúp phát hiện corruption; recovery cần mechanism như WAL redo, page LSN, double-write buffer hoặc page-image strategy tùy engine. Correctness requirement là crash không được biến partial physical write thành logical state không thể phát hiện/phục hồi.

## 10. Group commit: performance pressure thay đổi timing, không đổi invariant

Nếu mỗi transaction flush storage riêng, flush latency giới hạn throughput. **Commit theo nhóm (group commit)** gom nhiều commit records vào cùng một durable flush.

```text
T1 ─┐
T2 ─┼─> one WAL flush -> acknowledge T1,T2,T3
T3 ─┘
```

Performance behavior thay đổi: một transaction có thể chờ thêm để amortize flush cost, nhưng acknowledgement vẫn chỉ được phát khi durability condition của group đã đạt.

Đây là mẫu reasoning quan trọng: optimization được phép đổi batching/timing, không được âm thầm làm yếu invariant nếu API không đổi contract.

## 11. Checkpoint đổi recovery cost chứ không thay commit truth

Checkpoint giới hạn lượng WAL phải scan/replay sau restart. Fuzzy checkpoint có thể chạy khi workload vẫn hoạt động; nó không nhất thiết đồng nghĩa mọi dirty page đã sạch.

Checkpoint quá thường xuyên tăng write pressure; quá thưa tăng recovery time và WAL retention. Đây là trade-off giữa runtime cost và **mục tiêu thời gian khôi phục (Recovery Time Objective, RTO)**.

## 12. Replication thêm một state machine khác

Replication không đơn giản “copy file sang máy khác”. Log entry có thể đi qua các trạng thái:

```text
created locally
→ written to local log
→ sent to replicas
→ received
→ persisted remotely
→ accepted by quorum/replication rule
→ applied/visible
```

Tùy protocol, client acknowledgement có thể gắn với một mốc khác nhau. Nếu system hứa survive leader loss, ack chỉ sau local persistence có thể chưa đủ. Nếu system hứa synchronous quorum durability, protocol phải chứng minh một committed entry vẫn hiện diện trong quorum có authority sau failover.

Đây là nơi transaction durability nối với consensus/log replication thay vì kết thúc ở local disk.

## 13. Replication không tự động đồng nghĩa durability

Nếu leader và replica đều chỉ giữ write trong volatile cache, một power event chung vẫn có thể làm mất state. Nếu các replica cùng failure domain, “ba bản sao” cũng không bảo vệ khỏi mất cả domain đó.

Durability cần reasoning theo ba chiều độc lập:

```text
local persistence guarantee
×
replication/commit rule
×
failure-domain independence
```

Số replica tự nó không trả lời được ba câu hỏi trên.

## 14. Synchronous replication đổi critical path

Khi commit phải đợi remote quorum, network RTT, remote queue và remote storage flush đều nằm trên critical path. Tail latency có thể tăng mạnh khi một replica chậm hoặc cross-region link dao động.

Protocol tốt phải quyết định replica nào nằm trong quorum, khi nào follower chậm bị loại khỏi critical path, và authority sau failover được xác định thế nào. Đây là nơi durability, consistency và availability gặp nhau.

Đọc thêm [Consensus internals](../../06_networks_distributed_systems/advanced/03_consensus_log_replication_reconfiguration_and_snapshots.md).

## 15. Async replication tạo một failure window có chủ đích

Async replication có thể giảm foreground latency vì leader ack trước khi remote copy đạt durability. Đổi lại có replication lag và **mất dữ liệu tiềm năng (Recovery Point Objective, RPO)** khi failover.

Điều quan trọng là contract phải nói rõ window này, metrics phải đo được lag, và failover procedure phải hiểu replica mới có history tới đâu.

## 16. Virtualization và cloud storage kéo dài chuỗi lời hứa

Trong VM/cloud, path có thể là:

```text
guest filesystem
→ virtual block device
→ hypervisor/host
→ storage network
→ replicated storage service
→ physical media
```

Một guest `fsync` chỉ đáng tin nếu mọi layer truyền durability intent đúng. Với managed storage, guarantee phải lấy từ service contract, không suy luận từ intuition local disk.

## 17. Performance pressure thường lộ qua tail, không qua average

Storage GC, dirty-page writeback, checkpoint burst, queue congestion hoặc replica lag có thể làm p99 commit latency tăng trong khi average vẫn ổn.

Khi throughput tăng gần capacity, group commit có thể cải thiện throughput nhưng queue wait cũng tăng. Khi checkpoint/writeback trùng peak traffic, foreground flush có thể tranh bandwidth với background maintenance.

Performance engineering vì thế phải đo **latency distribution + queue + saturation + background activity** cùng lúc.

## 18. Production evidence theo từng tầng

Application layer cần transaction latency, timeout và acknowledgement semantics. Database layer cần WAL bytes/flush latency, checkpoint activity, dirty pages, lock/MVCC horizon và replication LSN/lag. OS layer cần dirty/writeback pages, I/O wait, block-device latency/queue depth và filesystem errors. Storage layer cần device latency, utilization, error counters và flush behavior nếu telemetry cho phép. Distributed layer cần quorum state, leader term/epoch, replica match/applied positions và failover timeline.

Một graph `DB commit latency` đơn độc không đủ để xác định cơ chế.

## 19. Crash testing là cách kiểm tra invariant, không phải edge-case luxury

Happy-path test chỉ chứng minh path không crash hoạt động. Durability cần fault injection tại interruption points:

```text
kill process trước/sau WAL flush
crash host giữa writeback
force replica lag rồi fail leader
replay recovery nhiều lần
inject partial/reordered write trong test harness nếu stack cho phép
```

Sau mỗi failure phải kiểm tra invariant: committed transaction theo contract còn tồn tại; uncommitted transaction không xuất hiện sai; recovery idempotent; replica mới không phát history trái với commit rule.

## 20. Backup giải bài toán khác

WAL + replication bảo vệ một số crash/failure scenarios. Chúng không tự bảo vệ khỏi operator error, logical corruption, ransomware hoặc bad write đã replicate tới mọi node.

Backup/PITR có retention và trust boundary riêng. Một durability design hoàn chỉnh phải phân biệt **survive crash**, **survive node loss**, **survive region loss** và **recover historical state**.

## Common Misconceptions

**“COMMIT nghĩa data page đã nằm trên disk.”** Không nhất thiết; durable WAL có thể đủ để recovery committed change.

**“`write()` thành công nghĩa data an toàn.”** Không; bytes có thể chỉ ở volatile cache.

**“Ba replicas nghĩa không thể mất dữ liệu.”** Không nếu acknowledgement rule, local persistence hoặc failure-domain independence không đủ mạnh.

**“Replication là backup.”** Không; lỗi logic và corruption có thể được replicate.

**“SSD không seek nên mọi write có cùng cost.”** FTL, garbage collection, erase block, write amplification và queueing vẫn làm latency biến động.

## Mô hình tư duy

> Durability là một chuỗi invariant và acknowledgement. MVCC quyết định history nào được nhìn thấy; WAL/recovery quyết định history nào sống sót crash; filesystem/storage giữ ordering và persistence vật lý; replication quyết định history nào còn authority sau mất node. **Một tầng chỉ được hứa mạnh bằng guarantee đã được chứng minh từ tầng bên dưới.**

## Kết nối

Đọc cùng [MVCC/WAL](../../05_data_databases/advanced/00_mvcc_visibility_wal_and_recovery_internals.md), [Filesystem crash consistency](../../03_operating_systems/advanced/04_filesystem_crash_consistency_journaling_and_cow.md), [Storage hardware](../../basic/02_computer_architecture/06_storage_hardware_ssd_disks_and_persistence.md), [Consensus internals](../../06_networks_distributed_systems/advanced/03_consensus_log_replication_reconfiguration_and_snapshots.md) và [End-to-end latency](./01_end_to_end_latency_browser_edge_service_db_storage.md).