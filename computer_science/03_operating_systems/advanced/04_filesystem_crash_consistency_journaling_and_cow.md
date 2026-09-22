# Filesystem crash consistency, journaling và copy-on-write

Filesystem phải biến một chuỗi writes có thể bị ngắt ở **bất kỳ điểm nào** thành trạng thái sau reboot vẫn hợp lệ hoặc ít nhất có thể recovery một cách xác định. Vấn đề khó không nằm ở việc “ghi bytes xuống disk”, mà ở việc một thao tác logic thường tạo nhiều updates vật lý: directory entry, inode, allocation bitmap/tree, data blocks, journal metadata và cache state.

Mental model trung tâm của chương này là: **crash consistency là một protocol ordering**. Mỗi optimization được phép đổi timing và batching, nhưng không được làm xuất hiện một on-disk state mà recovery protocol không giải thích được.

## 1. Bài toán ban đầu: một operation logic gồm nhiều writes vật lý

Tạo hoặc thay thế một file có thể cần:

```text
allocate inode
allocate data block
write data
link block vào inode
insert directory entry
update free-space metadata
```

Nếu power loss xảy ra sau bất kỳ bước nào, filesystem phải tránh các trạng thái như directory trỏ tới inode chưa hợp lệ, một block vừa được dùng vừa còn nằm trong free list, hoặc metadata nói file dài hơn số data block thực sự tồn tại.

**Crash consistency** hỏi:

> Với mọi crash point nằm trong failure model, on-disk state sau reboot có thuộc tập trạng thái mà recovery có thể đưa về một filesystem hợp lệ không?

Đây là invariant mạnh hơn “write thường hoàn tất”.

## 2. Atomicity, visibility và durability là ba property khác nhau

Một rename có thể atomic về **visibility**: observer thấy tên cũ hoặc tên mới, không thấy trạng thái nửa đổi tên. Nhưng điều đó không tự động nghĩa rename đã **durable** qua power loss.

Tương tự, `write()` có thể trả success vì kernel đã copy bytes vào page cache. Nó không chứng minh bytes đã tới non-volatile media.

Khi reasoning, luôn tách:

```text
atomicity  : observer có thấy partial logical update không?
visibility : process khác được phép thấy state nào?
durability : state nào sống sót failure đã công bố?
```

Một API có thể mạnh ở một trục và yếu ở trục khác.

## 3. Page cache làm `write()` chưa đồng nghĩa persistence

Với buffered I/O, application thường đi qua:

```text
user buffer
→ write()/pwrite()
→ kernel page cache: page trở thành dirty
→ writeback
→ filesystem/block layer
→ device queue/cache
→ non-volatile media
```

`write()` return thường chỉ chứng minh kernel đã nhận data. Dirty page có thể được flush vài giây sau hoặc sớm hơn vì memory pressure.

Primitive như `fsync()`/`fdatasync()` yêu cầu durability mạnh hơn, nhưng exact contract vẫn phụ thuộc filesystem và device stack. Database WAL dựa mạnh vào boundary này, nên “OS sẽ tự flush sớm thôi” không phải correctness argument.

## 4. Invariant write ordering: pointer không được durable trước object nó làm reachable

Một pattern chung của crash-safe structure là tránh làm một object mới **reachable** trước khi object đó đủ hợp lệ.

Ví dụ simplified:

```text
1. ghi block data mới
2. đảm bảo block đủ persistent theo protocol
3. cập nhật metadata/pointer để file trỏ tới block mới
4. đảm bảo metadata durable
```

Nếu step 3 durable trước step 1, recovery có thể thấy pointer tới garbage hoặc incomplete content.

Filesystem journaling, copy-on-write tree và database WAL dùng implementation khác nhau nhưng cùng family invariant: **publication metadata không được vượt quá state mà recovery dựa vào**.

## 5. Journaling biến arbitrary update thành một log protocol có boundary

Journaling ghi transaction metadata hoặc copies/descriptions của updates vào journal trước khi áp dụng chúng vào home locations. Recovery sau crash không cần đoán toàn filesystem; nó xác định journal transaction nào đủ commit boundary để replay hoặc transaction nào phải bỏ.

Simplified state machine:

```text
prepare journal records
→ write records
→ persist required journal content
→ persist commit marker / transaction boundary
→ checkpoint/apply updates to home locations
→ reclaim journal space
```

Invariant không phải “home blocks luôn mới nhất”. Invariant là **journal + home state luôn đủ để recovery một history hợp lệ**.

## 6. Metadata journaling và data journaling bảo vệ những thứ khác nhau

Metadata journaling chủ yếu bảo vệ filesystem structure. User data có thể được write theo policy khác, nên sau crash structure vẫn valid nhưng file content mới nhất chưa chắc đúng như application tưởng nếu application không dùng durability protocol thích hợp.

Data journaling có thể log cả user data, tăng guarantee nhưng cũng tăng write amplification và bandwidth cost.

Do đó câu “filesystem có journal nên không mất data” quá mạnh. Phải hỏi journal mode và application đã đặt durability boundary ở đâu.

## 7. Barriers, flush và FUA: ordering phải sống xuống device

Filesystem có thể phát writes theo đúng thứ tự logic nhưng storage stack/device vẫn có queue và volatile write cache. Nếu device reorder hoặc báo completion trước khi data an toàn mà không tôn trọng flush/FUA semantics, upper-layer protocol có thể bị phá.

Causal chain:

```text
filesystem wants A before B
→ block layer schedules requests
→ controller/device caches them
→ power loss
```

Correctness yêu cầu ordering intent phải được truyền đủ qua các layer nằm trong contract. Một filesystem algorithm đúng không cứu được device/firmware vi phạm persistence guarantee mà upper layer dựa vào.

## 8. Torn write và atomic write granularity

Một filesystem block hoặc database page có thể lớn hơn atomic persistence granularity của storage. Power loss giữa write có thể tạo **ghi rách (torn write)**: một phần old, một phần new.

Checksum giúp **detect** corruption nhưng không tự recover. Recovery cần redundant metadata, journal redo, copy-on-write version cũ, mirrored metadata hoặc mechanism tương đương tùy filesystem.

Vì vậy invariant thường không phải “block write là atomic”; invariant là **partial physical update không được âm thầm trở thành logical state được tin là hoàn chỉnh**.

## 9. Copy-on-write: publish root sau khi subtree mới đã tồn tại

Copy-on-write filesystem không overwrite structure đang live. Nó tạo blocks/nodes mới, cập nhật ancestors mới, rồi cuối cùng chuyển root/reference tới version mới.

Simplified:

```text
old root -> old subtree

write new leaf
→ write new parent
→ ...
→ atomically/safely publish new root
```

Nếu crash trước root publication, old tree vẫn authoritative. Nếu crash sau publication boundary, new tree phải đủ complete theo protocol.

COW làm snapshot tự nhiên vì old blocks vẫn còn reachable từ old roots, nhưng trả cost bằng fragmentation, metadata churn và write amplification.

## 10. Rename-based replace: atomic namespace change chưa đủ cho durable replace

Pattern phổ biến:

```text
write temp file
→ fsync(temp)
→ rename(temp, target)
→ fsync(parent directory)   // khi contract/filesystem yêu cầu để persist directory entry
```

Chi tiết exact phụ thuộc platform/filesystem, nhưng mental model phải nhận ra **file data** và **directory metadata** là hai durability objects khác nhau.

Nếu chỉ fsync file rồi rename nhưng crash trước directory update durable, sau reboot tên mới có thể không tồn tại theo contract. “Rename atomic” chỉ trả lời visibility của namespace transition, không tự trả lời toàn bộ power-failure durability.

## 11. Writeback error propagation cũng là một correctness problem

Buffered write có thể return trước khi actual device write xảy ra. Lỗi I/O có thể xuất hiện ở writeback sau đó. Application cần hiểu API nào báo asynchronous writeback errors và điểm nào nó kiểm tra/propagate failure.

Nếu system log “save successful” trước durability boundary, business acknowledgement có thể mạnh hơn storage state thật. Đây là cùng invariant với database commit: **acknowledgement không được mạnh hơn evidence đã đạt**.

## 12. Dirty-page pressure làm timing thay đổi

Ở low load, dirty pages có thể flush nền trơn tru. Khi write rate tăng, dirty set lớn dần, background writer và reclaim bắt đầu cạnh tranh bandwidth. Tới một threshold, foreground writer có thể bị throttle hoặc chờ writeback.

Causal loop:

```text
write rate ↑
→ dirty pages ↑
→ writeback queue ↑
→ device utilization/latency ↑
→ foreground fsync latency ↑
→ request queue ↑
```

Vì vậy storage incident có thể xuất hiện ở API p99 dù CPU thấp. Lower layer thực sự quyết định behavior là dirty writeback + device queue, không phải application handler.

## 13. Journaling/COW có background work và amplification

Journal checkpointing, COW metadata rewrite, snapshot retention, filesystem cleaning/defragmentation hoặc device garbage collection có thể cạnh tranh với foreground I/O.

Optimization tạo throughput tốt ở steady state có thể tạo latency burst khi background debt được trả. Production benchmark cần chạy đủ lâu để quan sát maintenance cycle, không chỉ đo vài giây warm cache.

## 14. Database WAL và filesystem journal là hai protocols xếp chồng

Database WAL bảo vệ transaction/recovery semantics của database. Filesystem journal/COW bảo vệ filesystem metadata/data-structure consistency.

```text
application transaction
→ database WAL/buffer pool
→ file I/O durability primitive
→ filesystem journal/COW
→ block/device persistence
```

Hai logs không duplicate cùng invariant. DB vẫn cần WAL vì filesystem không biết transaction boundary của nhiều database pages; filesystem vẫn cần crash-consistency vì DB file blocks tồn tại trong filesystem namespace/metadata của nó.

Đọc [MVCC, WAL và recovery internals](../../05_data_databases/advanced/00_mvcc_visibility_wal_and_recovery_internals.md) và [durability path xuyên tầng](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).

## 15. Failure injection là cách kiểm tra crash invariant

Happy-path tests không chứng minh crash consistency. Test tốt cần cắt execution ở các boundary có ý nghĩa:

```text
crash trước journal commit
crash sau commit marker nhưng trước home write
crash giữa COW subtree và root publication
kill process trước/sau fsync
inject write error / short write khi harness cho phép
replay recovery nhiều lần
```

Sau mỗi failure, kiểm tra filesystem mount/recovery thành công, namespace không chứa impossible state, data được giữ đúng theo durability contract, và recovery idempotent.

## 16. Production evidence

Evidence hữu ích gồm:

```text
application: fsync/fdatasync latency, write error/ack timing
OS: dirty pages, writeback rate, reclaim/throttling, I/O wait
filesystem: journal/checkpoint activity, filesystem errors, free-space/fragmentation pressure
block/device: latency distribution, queue depth, utilization, flush latency, error counters
```

Một graph “disk utilization 70%” không đủ. Cần nối request/transaction latency với writeback/flush queue và background work để chứng minh mechanism.

## 17. Abstraction nào thực sự quyết định behavior?

Nếu symptom là file biến mất sau reboot, bắt đầu từ application durability protocol rồi xuống rename/directory/fsync semantics. Nếu filesystem structure corrupt, kiểm tra journal/COW recovery path và storage errors. Nếu correctness ổn nhưng p99 spike, kiểm tra dirty/writeback/queue/background maintenance.

Không cần học mọi filesystem implementation để reasoning. Cần xác định **publication point, persistence boundary, recovery metadata và failure model** của implementation đang dùng.

## 18. Mô hình tư duy

> Filesystem crash consistency là một state-transition protocol dưới khả năng interruption tùy ý. `write()` tạo dirty state; journaling/COW tạo recovery structure; barriers/flush đưa ordering intent xuống storage; recovery chọn history hợp lệ sau crash. **Atomic visibility không tự bằng durability, và acknowledgement chỉ an toàn khi tầng dưới đã đạt persistence contract mà tầng trên đang hứa.**

## Kết nối

Ôn [filesystem foundation](../../basic/03_operating_systems/04_filesystems_storage_and_io.md), [storage hardware](../../basic/02_computer_architecture/06_storage_hardware_ssd_disks_and_persistence.md), [MVCC/WAL](../../05_data_databases/advanced/00_mvcc_visibility_wal_and_recovery_internals.md), [buffer pool](../../05_data_databases/advanced/04_buffer_pool_replacement_and_dirty_page_management.md) và [durability path](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).