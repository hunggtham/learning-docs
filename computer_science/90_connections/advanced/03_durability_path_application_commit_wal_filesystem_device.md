# Đường đi của durability: application commit → WAL → filesystem → thiết bị lưu trữ

Khi application nhận được câu trả lời `COMMIT OK`, người đọc thường hình dung dữ liệu đã “được ghi xuống đĩa”. Thực tế có nhiều tầng cache, buffer và queue nằm giữa application và thiết bị lưu trữ. Muốn hiểu **độ bền dữ liệu (durability / 내구성)** ở mức hệ thống, phải theo dõi toàn bộ đường đi và xác định chính xác tại tầng nào dữ liệu chỉ đang nằm trong memory, tại tầng nào đã được ghi vào log, và tại tầng nào thiết bị thật sự bảo đảm nó sẽ sống sót sau mất điện.

## 1. Durability là một hợp đồng xuyên nhiều tầng

Một transaction database có thể đi qua:

```text
application
  ↓
database transaction layer
  ↓
WAL / redo log
  ↓
OS page cache hoặc direct I/O path
  ↓
filesystem / block layer
  ↓
device queue
  ↓
SSD/HDD controller cache
  ↓
non-volatile media
```

Nếu một tầng báo thành công quá sớm hoặc hiểu sai guarantee của tầng dưới, application có thể nhận `COMMIT OK` nhưng dữ liệu vẫn mất sau crash/power loss.

## 2. WAL giải bài toán gì?

**Nhật ký ghi trước (Write-Ahead Logging, WAL)** yêu cầu thông tin cần để phục hồi thay đổi được ghi durable trước khi data page tương ứng được coi là đã commit theo protocol.

Mental model:

```text
log trước
page sau
```

Database không cần flush mọi data page ngay lúc commit. Nó chỉ cần bảo đảm log chứa đủ thông tin để replay/undo sau crash. Đây là lý do WAL giảm số lượng random write đồng bộ trên đường commit.

## 3. Commit record và fsync

Trong nhiều thiết kế, transaction chỉ được coi là durable sau khi commit record hoặc log record liên quan đã đi qua một primitive đồng bộ như `fsync`, `fdatasync`, `O_DSYNC` hoặc cơ chế tương đương.

Nhưng gọi `write()` thành công chưa đủ. `write()` có thể chỉ copy data từ user space vào page cache của kernel.

```text
write() success
≠ durable on storage media
```

Đây là một trong những boundary quan trọng nhất giữa application/database và OS.

## 4. Page cache

OS thường giữ file data trong **bộ đệm trang (page cache)**. Ghi vào file có thể chỉ làm page cache trở thành “dirty”. Kernel sẽ flush dirty page xuống storage sau đó.

Page cache cải thiện throughput vì gom nhiều write và tránh I/O sync liên tục. Đổi lại, application phải dùng đúng durability primitive khi thật sự cần persistence trước khi trả success.

## 5. Filesystem ordering

Filesystem phải cập nhật nhiều metadata/data structure. Sau crash, nếu các write xuất hiện trên disk theo thứ tự khác dự kiến, cấu trúc có thể không nhất quán.

Journaling hoặc copy-on-write filesystem giải quyết một phần vấn đề bằng protocol riêng. Tuy nhiên database WAL và filesystem journal phục vụ boundary khác nhau:

- database WAL bảo vệ transaction semantics;
- filesystem journal bảo vệ filesystem metadata/data consistency.

Một lớp không tự thay thế lớp kia.

## 6. Barrier và flush

Storage stack có thể reorder write để tối ưu throughput. **Rào ghi (write barrier)** và flush command giúp bảo đảm một số write phải được stable trước write khác.

Nếu database giả định log record A đã durable trước data page B nhưng device reorder ngược lại, crash consistency có thể bị phá.

Do đó durability phụ thuộc protocol ordering từ database xuống block device.

## 7. Device cache

SSD/HDD controller có thể có volatile write cache. Nếu device báo write complete khi data mới chỉ nằm trong RAM của controller và mất điện xảy ra, data có thể biến mất.

Enterprise device có thể dùng capacitor hoặc power-loss protection để flush cache khi mất điện. Consumer device không phải lúc nào cũng có guarantee tương tự.

Vì vậy “fsync xong” vẫn dựa vào device firmware/hardware thực hiện đúng storage contract.

## 8. Torn write

Một page có thể lớn hơn atomic write unit của device. Nếu power loss xảy ra giữa write, page có thể ở trạng thái **ghi rách (torn write)** — một phần mới, một phần cũ.

Database thường dùng checksum, double-write buffer, page LSN hoặc WAL replay để phát hiện/phục hồi tình huống này.

## 9. Group commit

Nếu mỗi transaction riêng lẻ gọi storage flush, throughput thấp vì flush latency cao. **Commit theo nhóm (group commit)** gom nhiều transaction chờ cùng một WAL flush:

```text
T1 commit
T2 commit
T3 commit
   ↓
one log flush
   ↓
ack T1,T2,T3
```

Đây là trade-off latency/throughput. Chờ thêm một khoảng nhỏ có thể tăng throughput mạnh bằng cách amortize flush cost.

## 10. Async commit và durability level

Một số hệ thống cho phép trả success trước khi WAL thật sự durable để giảm latency. Điều này đổi guarantee:

```text
ack nhanh hơn
↔ có cửa sổ mất transaction khi crash
```

Không nên gọi hai mode đều là “commit” mà không giải thích durability semantics. Product requirement quyết định có chấp nhận cửa sổ mất dữ liệu hay không.

## 11. Replication không tự thay thế local durability

Nếu leader gửi log entry sang replica nhưng leader và replica đều chỉ giữ entry trong volatile cache, mất điện đồng thời có thể mất dữ liệu.

Ngược lại, synchronous replication durable trên nhiều failure domain có thể tăng guarantee nhưng thêm network + disk latency.

Durability và replication là hai trục khác nhau:

```text
local persistence
replica count
failure-domain independence
```

## 12. Database page và filesystem page không nhất thiết trùng nhau

Database có page size riêng, filesystem có block/page abstraction riêng, device có sector/page nội bộ riêng. Alignment không phù hợp có thể làm write amplification hoặc read-modify-write.

Direct I/O đôi khi được dùng để database tự quản buffer pool và tránh double caching. Nhưng direct I/O không làm durability tự động đúng; vẫn cần flush/order semantics phù hợp.

## 13. SSD FTL và write amplification

SSD không overwrite NAND page tùy ý như RAM. Firmware dùng **Flash Translation Layer (FTL)** để ánh xạ logical block sang physical location. Garbage collection và wear leveling có thể khiến một logical write tạo nhiều physical write.

Database write pattern, filesystem và SSD internals vì vậy có thể ảnh hưởng nhau. Sequential WAL thường thân thiện hơn random small writes, nhưng device behavior vẫn phụ thuộc firmware và queue depth.

## 14. Crash recovery

Sau restart, database không đơn giản “mở file rồi chạy”. Nó phải xác định:

```text
log record nào durable
transaction nào đã commit
page nào đã phản ánh log tới đâu
redo gì
undo gì
```

LSN hoặc tương đương giúp liên kết page state với log position. Recovery protocol biến durability thành một câu chuyện có thể kiểm chứng sau crash.

## 15. Checkpoint

Nếu replay WAL từ đầu lịch sử mỗi lần restart thì recovery quá lâu. **Checkpoint** ghi lại mốc cho biết phần state nào đã được materialize đủ để recovery bắt đầu gần hơn.

Checkpoint quá thường xuyên tăng I/O; quá thưa làm recovery dài và WAL retention lớn. Đây là trade-off giữa runtime overhead và recovery time objective.

## 16. Durability và latency tail

Storage flush latency có distribution, không phải số cố định. Khi device GC, queue congestion hoặc filesystem writeback xảy ra, p99 commit latency có thể tăng mạnh.

Do đó database latency spike có thể bắt nguồn từ storage layer dù CPU và query plan không thay đổi.

## 17. Virtualization và cloud storage

Trong VM/cloud, đường đi có thể dài hơn:

```text
guest filesystem
→ virtual block device
→ hypervisor
→ host/storage service
→ replicated storage backend
```

Một flush chỉ đáng tin nếu toàn chuỗi virtual layer truyền đúng durability intent. Cloud storage service thường cung cấp contract riêng; cần đọc guarantee của service thay vì suy luận từ local-disk intuition.

## 18. Backup không đồng nghĩa durability

Durability bảo vệ transaction khỏi crash/power loss theo contract hiện tại. Backup bảo vệ khỏi corruption, operator error, ransomware hoặc lỗi logic đã replicate khắp cluster.

Một database có WAL + synchronous replication vẫn có thể cần backup/PITR.

## 19. Kiểm thử crash consistency

Happy-path test không đủ. Hệ thống storage/database cần thử:

```text
kill process giữa write
kill host sau fsync
power-loss simulation
partial write
reorder injection
recovery lặp nhiều lần
```

Mục tiêu là kiểm tra invariant sau mọi interruption point có thể xảy ra.

## Common Misconceptions

**“COMMIT nghĩa là data page đã nằm trên disk.”** Không nhất thiết; thường WAL durable là đủ để transaction recoverable.

**“write() thành công nghĩa là dữ liệu an toàn.”** Không; data có thể chỉ nằm trong page cache.

**“RAID/replication là backup.”** Không; lỗi logic hoặc corruption có thể được replicate.

**“SSD không có seek nên write nào cũng như nhau.”** FTL, GC, erase block và queue behavior vẫn tạo cost khác nhau.

## Mô hình tư duy

> Durability là một chuỗi lời hứa. Mỗi tầng chỉ an toàn nếu hiểu đúng lời hứa của tầng bên dưới và không trả success trước khi invariant của chính nó được bảo đảm.

Khi debug mất dữ liệu hoặc commit latency, hãy đi theo đường: transaction → WAL → syscall → page cache/filesystem → block layer → device → media, rồi quay ngược qua recovery protocol để xác minh guarantee.

Xem thêm: [MVCC/WAL](../../05_data_databases/advanced/00_mvcc_visibility_wal_and_recovery_internals.md), [Filesystem crash consistency](../../03_operating_systems/advanced/04_filesystem_crash_consistency_journaling_and_cow.md), [Storage hardware](../../basic/02_computer_architecture/06_storage_hardware_ssd_disks_and_persistence.md).
