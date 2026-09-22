# LSM tree, compaction, Bloom filters và write amplification

B+Tree tối ưu cho cập nhật theo page và truy vấn có thứ tự, nhưng workload ghi ngẫu nhiên với tốc độ cao có thể buộc storage engine sửa nhiều page nhỏ ở nhiều vị trí. **Cây hợp nhất có cấu trúc log (Log-Structured Merge Tree, LSM Tree / 로그 구조 병합 트리)** đổi bài toán: ghi mới trước vào cấu trúc dễ append, sau đó dùng công việc nền để hợp nhất dữ liệu thành các run đã sắp thứ tự.

LSM không làm chi phí biến mất. Nó **dời thời điểm và hình dạng của chi phí**: foreground write nhẹ hơn, nhưng read path, space usage và compaction phải trả món nợ tổ chức dữ liệu về sau.

## 1. Bài toán ban đầu và invariant của LSM

Một storage engine cần đồng thời giữ vài invariant. Write đã được acknowledge theo durability contract phải có đường recovery. Khi cùng một key xuất hiện ở nhiều nơi, read phải chọn đúng version theo ordering/visibility rule của engine. File immutable đã được publish không được bị sửa tùy ý. Compaction chỉ được xóa version hoặc tombstone khi chắc chắn việc xóa đó không làm old value sống lại hoặc phá snapshot còn hợp lệ.

Có thể hình dung lifecycle:

```text
mutation
→ WAL
→ memtable
→ immutable memtable
→ SSTable
→ compaction qua các level/run
→ version cũ được reclaim khi safe
```

WAL trả lời durability khi dữ liệu còn ở memory. Memtable tối ưu foreground mutation. SSTable biến state thành file immutable có thứ tự. Compaction duy trì hình dạng lâu dài của tập file.

## 2. Write path: foreground nhanh vì chưa tổ chức xong dữ liệu

Write thường được append vào **nhật ký ghi trước (Write-Ahead Log, WAL / 선행 기록 로그)** rồi cập nhật **memtable** trong RAM. Khi memtable đạt ngưỡng, engine đóng băng nó thành immutable memtable và flush thành **Sorted String Table (SSTable)** hoặc sorted run tương tự.

Flush tuần tự thường thân thiện với block storage hơn việc sửa ngẫu nhiên nhiều page. Nhưng cùng một logical key có thể tồn tại ở memtable, file mới và nhiều file cũ. Vì vậy write latency thấp tại `PUT` không phải toàn bộ cost của write.

Một benchmark chỉ đo “bao nhiêu PUT/s trước khi compaction chạy nặng” dễ đo burst capacity thay vì **sustainable write throughput**.

## 3. Immutable file tạo concurrency đơn giản hơn nhưng cần publication an toàn

SSTable thường immutable sau khi hoàn tất. Reader có thể đọc file mà không phải phối hợp với writer sửa nội dung ngay trong file đó. Compaction tạo file mới rồi cập nhật metadata để publish một tập file mới.

Engine vì thế thường có metadata kiểu **version set / manifest** mô tả SSTable nào thuộc logical state hiện tại. Invariant không chỉ là “file mới đã được ghi”; metadata phải chuyển sang version mới theo crash-safe protocol.

Nếu process crash sau khi tạo output file nhưng trước khi publish manifest, file có thể thành orphan và được cleanup sau. Nếu metadata publish trước khi file cần thiết thực sự durable, recovery có thể trỏ tới state không đầy đủ. Đây là cùng family với filesystem crash consistency: **object phải tồn tại đủ chắc trước khi pointer/metadata tuyên bố nó là live state**.

Đọc thêm [Filesystem crash consistency](../../03_operating_systems/advanced/04_filesystem_crash_consistency_journaling_and_cow.md) và [MVCC/WAL/recovery](./00_mvcc_visibility_wal_and_recovery_internals.md).

## 4. Read path là phép tìm kiếm qua nhiều lớp lịch sử

Một point lookup thường kiểm tra memtable trước, rồi immutable memtable và các SSTable có khả năng chứa key. Nếu nhiều version tồn tại, engine cần chọn version mới nhất hợp lệ theo sequence/transaction metadata của chính nó.

```text
memtable
→ immutable memtable
→ file metadata / key range
→ Bloom filter
→ index block
→ data block
```

Mỗi bước cố loại I/O không cần thiết. **Read amplification** vì vậy không chỉ là “số file đã mở”, mà còn là metadata lookup, cache miss, block read và version filtering cần cho một logical read.

## 5. Bloom filter giải bài toán negative lookup

**Bộ lọc Bloom (Bloom filter / 블룸 필터)** là cấu trúc xác suất cho membership test. Với cấu hình đúng, nó có thể trả lời chắc chắn “key không ở đây”, hoặc “key có thể ở đây”. False positive làm engine đọc thêm file vô ích; false negative không được phép xảy ra theo contract thông thường của filter.

Bloom filter đặc biệt có giá trị khi lookup hỏi key không tồn tại hoặc key chỉ nằm trong một trong nhiều runs. Nhưng filter không miễn phí: nó chiếm memory/storage và cần hash work.

Bits-per-key quá thấp làm false-positive rate tăng và read amplification quay lại dưới dạng I/O. Dành quá nhiều memory cho filters lại có thể làm cache data/index blocks thiếu. Đây là trade-off trong cùng một memory budget.

## 6. Compaction là cơ chế trả nợ, không phải housekeeping phụ

**Hợp nhất nền (compaction / 컴팩션)** đọc nhiều sorted runs, merge chúng theo key/version order, ghi output mới rồi chuyển metadata sang tập file mới. Trong quá trình này engine có thể loại version bị supersede, reclaim tombstone đã an toàn và giảm overlap giữa files.

Compaction tiêu CPU, memory buffer, read bandwidth và write bandwidth. Nếu ingest tạo debt nhanh hơn compaction trả được, số runs/level overlap tăng. Read amplification, space amplification và background I/O cùng tăng.

Đến một điểm engine phải throttle hoặc stall foreground writes để không tích debt vô hạn. Vì vậy `write stall time`, pending compaction bytes và level size thường quan trọng hơn một con số write latency trung bình.

## 7. Leveled và size-tiered tối ưu các amplification khác nhau

**Leveled compaction** cố giảm overlap giữa files trong một level. Point read có thể cần kiểm tra ít candidate hơn, nhưng một byte có thể bị rewrite nhiều lần khi được đẩy qua các level.

**Size-tiered compaction** hoặc các chiến lược tiered giữ nhiều runs cùng cỡ rồi merge theo batch. Cách này thường giảm write amplification nhưng có thể tăng số runs mà read phải xét và giữ duplicate versions lâu hơn.

Không có strategy tốt tuyệt đối. Workload read-heavy với strict p99 lookup khác ingest-heavy; range scan khác point lookup. Quyết định compaction là quyết định về **read amplification × write amplification × space amplification**.

## 8. Ba amplification tạo một tam giác chi phí

Một logical byte có thể được ghi nhiều lần qua WAL, flush và compaction: đó là **khuếch đại ghi (write amplification / 쓰기 증폭)**. Một logical read có thể kiểm tra nhiều runs/blocks: **read amplification**. Dữ liệu cũ, tombstone và overlapping runs làm physical bytes lớn hơn live logical dataset: **space amplification**.

Giảm một trục thường đẩy chi phí sang trục khác. Compaction aggressive làm read/space tốt hơn nhưng tăng background writes. Compaction lười giảm rewrite ngắn hạn nhưng giữ nhiều file/version hơn.

Trên SSD còn có amplification bên dưới: Flash Translation Layer có thể tự garbage-collect và rewrite erase blocks. Storage-engine write amplification nhân với device-level amplification có thể làm bandwidth và endurance xấu hơn trực giác “SSD rất nhanh”.

## 9. Tombstone tồn tại để delete đi cùng append-only write path

Delete trong LSM thường không đi tìm và xóa ngay mọi bản sao cũ. Engine ghi **tombstone** để nói từ sequence/version này trở đi key được coi là deleted.

Tombstone chỉ được loại khi engine biết không còn nơi nào old value có thể tái xuất hiện sau khi tombstone biến mất. Nếu compaction drop tombstone ở level trên nhưng old value còn ở level dưới, lookup sau đó có thể “hồi sinh” dữ liệu đã xóa.

Snapshot cũ, long-running read, replica lag, backup/PITR retention hoặc range tombstone có thể kéo dài reclamation horizon. “Xóa logical” và “reclaim physical bytes” là hai sự kiện khác nhau.

## 10. Worked example: một key đi qua nhiều versions

Giả sử:

```text
SSTable cũ:       user:42 = "A"   seq=10
SSTable mới:      user:42 = "B"   seq=20
memtable:         tombstone        seq=30
```

Reader ở snapshot sau `seq=30` phải thấy key đã bị xóa. Reader ở snapshot hợp lệ tại `seq=25` vẫn có thể cần thấy `"B"`. Vì vậy compaction không thể đơn giản “giữ record mới nhất theo wall clock”. Nó phải tôn trọng visibility/reclamation rules của engine.

Khi không còn snapshot nào cần `seq<30`, và compaction đã bao phủ mọi nơi có thể chứa version cũ, tombstone mới có thể được reclaim an toàn.

Ví dụ này nối trực tiếp LSM với MVCC: immutable sorted files chỉ là physical representation; correctness vẫn do transaction/version semantics quyết định.

## 11. Range scan làm lộ merge cost

Point lookup có Bloom filter để skip nhiều files. Range scan lại thường phải merge iterators từ nhiều runs vì filter membership không giải quyết ordering của cả khoảng.

Nếu workload scan lớn, nhiều overlapping runs có thể làm CPU merge, decompression và block reads tăng đáng kể dù point-read benchmark đẹp. Compaction strategy phải phản ánh workload thật thay vì tối ưu duy nhất `GET(key)`.

## 12. Hot key, skew và compaction locality

Traffic hiếm khi uniform. Một key range nóng có thể nhận phần lớn writes, khiến một số SSTable/level bị rewrite liên tục trong khi dữ liệu khác gần như lạnh.

Partitioning có thể chia compaction work, nhưng skew vẫn có thể tạo hotspot trên một shard, storage device hoặc CPU group. “Cluster còn 50% capacity” không giúp nếu partition chứa hot range đã saturate compaction bandwidth.

## 13. Foreground và background I/O tranh cùng resource

Compaction gọi là background task nhưng dùng thật CPU và storage bandwidth. Nếu nó chiếm toàn device queue, foreground reads/commits tăng tail latency. Nếu throttle quá mạnh, debt tăng và cuối cùng dẫn tới write stall.

Controller phải cân bằng:

```text
ingest rate
compaction debt
foreground latency
available I/O bandwidth
space headroom
```

Đây là feedback-control problem tương tự queue/backpressure: trì hoãn maintenance quá lâu chỉ biến maintenance thành burst lớn hơn. Đọc [Queueing, tail latency và backpressure](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md).

## 14. Corruption và checksums thay đổi failure mode

Immutable file giúp recovery reasoning dễ hơn nhưng không làm storage corruption biến mất. SSTable thường có checksum hoặc block-level integrity metadata để phát hiện bit corruption/truncated block.

Checksum phát hiện không đồng nghĩa tự sửa. Repair có thể cần replica, backup hoặc rebuild từ source khác. Nếu compaction đọc corrupted input rồi phát output mới mà không detect đúng, corruption có thể lan sang state mới.

## 15. Production evidence: đo cả foreground lẫn debt phía sau

Một LSM engine khỏe không thể được đánh giá chỉ bằng request throughput. Evidence hữu ích gồm compaction backlog/pending bytes, số run/file theo level, bytes read/write bởi compaction, logical-vs-physical write amplification, disk utilization/queue latency, space amplification, tombstone/version retention, Bloom-filter behavior, block-cache hit rate, write stall/throttle time và latency distribution của point read/range scan/write.

Cần đọc các metric như causal chain:

```text
ingest tăng
→ L0 files tăng
→ compaction debt tăng
→ background I/O saturate
→ read latency tăng
→ write throttle/stall
```

Nếu chỉ thấy “disk 100%” rồi tăng hardware mà không biết bytes đến từ foreground hay compaction, ta chưa xác định mechanism.

## 16. Debugging theo lower abstraction

Nếu point lookup chậm nhưng storage I/O thấp, cost có thể nằm ở CPU merge/filter/decompression hoặc cache behavior. Nếu compaction backlog tăng khi device throughput đã đầy, storage bandwidth là lower constraint. Nếu write amplification tăng sau workload skew, compaction selection/layout mới là owner của behavior. Nếu tombstone không reclaim, hãy tìm snapshot/replica/retention horizon trước khi kết luận “compaction bị lỗi”.

## Common Misconceptions

**“LSM write chỉ là append nên write amplification thấp.”** Foreground path append-friendly, nhưng compaction có thể rewrite cùng byte nhiều lần.

**“Bloom filter làm read O(1).”** Filter chỉ loại candidate files; lookup vẫn cần index/data block và version semantics.

**“Delete xong là disk space giảm ngay.”** Tombstone phải sống tới khi old versions có thể bị loại an toàn.

**“Compaction là background nên không ảnh hưởng request.”** Nó tranh CPU, memory và I/O với foreground và có thể quyết định p99 latency.

## Mental Model

> LSM Tree biến random mutation thành **append + immutable runs + background merge**. Invariant khó nhất không phải sort file, mà là giữ đúng history khi một key tồn tại ở nhiều nơi và chỉ reclaim dữ liệu khi safe. Performance phải được reasoning bằng ba amplification — read, write, space — cùng compaction debt và storage bandwidth. Fast foreground write chỉ bền vững khi background maintenance theo kịp.

## Kết nối

Đọc cùng [MVCC, WAL và recovery internals](./00_mvcc_visibility_wal_and_recovery_internals.md), [Buffer pool và dirty-page management](./04_buffer_pool_replacement_and_dirty_page_management.md), [B+Tree internals](./02_bplus_tree_pages_splits_merges_and_latch_coupling.md), [Filesystem crash consistency](../../03_operating_systems/advanced/04_filesystem_crash_consistency_journaling_and_cow.md) và [Queueing/backpressure](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md).