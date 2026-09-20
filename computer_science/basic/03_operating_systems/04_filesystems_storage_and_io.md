# Filesystem, storage và buffered I/O

Storage device expose blocks/pages/sectors và failure characteristics, nhưng applications muốn named files, directories, permissions và durable byte streams. Filesystem (파일 시스템 / hệ thống tệp) tạo abstraction này, đồng thời phải giữ metadata nhất quán khi crash có thể xảy ra giữa bất kỳ writes nào.

## File là abstraction, không phải vùng bytes đơn giản

File có data + metadata: size, timestamps, permissions, ownership, block mapping. Directory map names tới file identifiers/inodes-like objects. Path resolution traverse directories và symbolic links theo rules.

Hard link và symbolic link khác nhau: hard link là thêm directory entry tới cùng underlying file object; symlink là file chứa path reference. Delete directory entry không nhất thiết reclaim data nếu còn hard links/open references.

## Blocks, extents và allocation

Filesystem map logical file offsets tới physical/device blocks. Contiguous allocation nhanh nhưng khó grow; block lists linh hoạt nhưng metadata lớn; extents mô tả runs liên tục và cân bằng.

Fragmentation làm sequential logical file thành scattered physical locations, đặc biệt ảnh hưởng HDD seek; SSD giảm seek penalty nhưng vẫn có flash translation/erase behavior riêng.

## Buffer/page cache

OS cache file data trong RAM. `read` có thể hit page cache mà không device I/O. `write` thường copy/mark pages dirty rồi background flush. Vì vậy benchmark lần hai có thể nhanh hơn lần đầu do cache.

Direct I/O hoặc database buffer managers có thể bypass/coordinate page cache để kiểm soát caching, alignment và durability rõ hơn.

## Durability và fsync

Application `write()` success không đồng nghĩa bits đã stable. Data có thể nằm user buffer, kernel cache, device cache. `fsync`/equivalent yêu cầu OS flush theo semantics cụ thể, nhưng real durability còn phụ thuộc device guarantees/power-loss protection.

Ordering quan trọng: nếu metadata nói block allocated trước khi data thật được written, crash có thể expose garbage. Filesystems dùng journaling, copy-on-write hoặc log-structured designs để giữ consistency.

## Journaling

Journaling ghi intended metadata/data changes vào log trước hoặc theo protocol rồi commit, cho phép recovery replay/rollback sau crash. Journal không phải backup; nó chủ yếu bảo vệ filesystem structural consistency.

## SSD và flash

Flash không overwrite arbitrary byte như RAM. Nó program pages và erase larger blocks; controller dùng Flash Translation Layer, wear leveling và garbage collection. Write amplification xuất hiện khi logical writes gây nhiều physical movement.

TRIM cho SSD biết blocks logical không còn cần, giúp GC. Database/storage engines quan tâm alignment/page size/write pattern vì device behavior leak lên performance.

## File locking và concurrent access

Filesystem không tự làm sequence read-modify-write atomic theo business semantics. File locks có advisory/mandatory variations, process scope và platform differences. Atomic rename thường là primitive hữu ích để publish replacement file, nhưng durability ordering vẫn cần fsync directory/file tùy OS.

## Object storage khác filesystem

Cloud object storage expose keys/objects, không POSIX file semantics đầy đủ. Operations, consistency, rename, partial update và listing behavior khác. Mounting object store như filesystem có thể tạo leaky abstraction.

## Mental Model

> Filesystem map **names + byte ranges** xuống **blocks + metadata**, dùng cache và crash-consistency protocol để sống qua failure. “Đã write” và “đã durable” là hai trạng thái khác nhau.

## Common Misconceptions

**“Journaling là backup.”** Nó không bảo vệ khỏi delete logic, ransomware hay device loss.

**“File delete luôn xóa bytes ngay.”** Namespace reference có thể mất trước khi blocks được reclaim/overwrite.

**“SSD chỉ là HDD nhanh hơn.”** Internal erase/program/FTL behavior tạo cost model khác.

## Kết nối

[I/O/DMA](../02_computer_architecture/03_io_interrupts_dma_and_devices.md) là hardware boundary. [Database WAL/recovery](../05_data_databases/04_storage_logs_recovery_and_durability.md) xây durability semantics cao hơn trên filesystem/device. [Version control](../08_software_systems/01_version_control_build_link_and_packages.md) lưu object graphs trên files/storage abstractions.
