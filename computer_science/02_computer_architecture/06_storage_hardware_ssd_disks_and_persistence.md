# Storage hardware: SSD, disks và persistence

Phần mềm thường nhìn storage qua file, page hoặc block. Nhưng những abstractions này đứng trên thiết bị vật lý có geometry, latency và failure modes riêng. Hiểu storage hardware giúp giải thích tại sao sequential I/O khác random I/O, vì sao SSD cần wear leveling, tại sao `fsync` tồn tại và vì sao database không thể coi “đã write()” là “đã bền vững”.

## Persistence là một property vật lý rồi mới thành software contract

RAM mất dữ liệu khi mất điện; storage persistent (영구 저장장치) được thiết kế giữ state qua power cycle. Nhưng “persistent” không có nghĩa mọi write ngay lập tức an toàn. Data có thể đang nằm trong CPU cache, OS page cache, controller cache hoặc volatile buffer của device.

Một durability guarantee phải nói rõ boundary nào đã được vượt qua.

## HDD: cơ học tạo ra latency structure

Hard disk drive (HDD / 하드 디스크) có rotating platters và moving heads. Random access cần seek head + chờ sector quay tới vị trí phù hợp, nên latency milliseconds là đáng kể. Sequential access tránh nhiều seeks và có throughput cao hơn.

Đây là lý do database systems historically tối ưu page layout, sequential log và B-tree để giảm random seeks.

## SSD: không seek nhưng không phải RAM lớn

Solid-state drive (SSD / 솔리드 스테이트 드라이브) dùng NAND flash. Read có thể theo pages, nhưng erase thường theo blocks lớn hơn. Flash cells có giới hạn erase cycles.

Vì không thể overwrite tùy ý như RAM, controller dùng Flash Translation Layer (FTL) để map logical block addresses sang physical locations. Garbage collection gom live pages rồi erase blocks. Wear leveling phân bố writes để không một vùng hỏng sớm.

Do đó logical write pattern có thể tạo write amplification: application ghi 1 MB nhưng device nội bộ phải di chuyển/erase nhiều hơn 1 MB.

## TRIM và free space information

Khi filesystem xóa file, device thông thường chỉ thấy logical blocks không còn được reference ở tầng filesystem; nó không tự biết blocks nào thực sự free. TRIM/Discard truyền thông tin này xuống SSD để controller quản lý garbage collection tốt hơn.

Điều này cho thấy abstraction boundary đôi khi cần hint từ tầng trên để tối ưu tầng dưới.

## NVMe và queueing

SATA/AHCI được thiết kế trong bối cảnh storage chậm hơn. NVMe (Non-Volatile Memory Express) tận dụng PCIe và hỗ trợ nhiều queues, queue depth lớn, parallel commands để khai thác SSD hiện đại.

Khi latency device giảm, software overhead, interrupts, locks và context switching trở thành tỷ lệ lớn hơn. Đây là pattern phổ quát: tối ưu một layer làm bottleneck dịch sang layer khác.

## Sector, block, page và alignment

Hardware sector, filesystem block và database page không nhất thiết cùng kích thước. Misalignment có thể khiến một logical write chạm nhiều physical units.

Database page thường được thiết kế để cân bằng metadata overhead, cache behavior và I/O granularity. B+ tree node size thường gần page size để một node access tương ứng một page I/O.

## Durability, flush và barriers

OS có thể acknowledge `write()` sau khi copy bytes vào page cache. Để yêu cầu dữ liệu đi tới durable storage, application dùng mechanisms như `fsync`/`fdatasync`, nhưng actual guarantee còn phụ thuộc filesystem và device cache behavior.

Write ordering cũng quan trọng. Nếu metadata nói “file mới tồn tại” được persisted trước data content, crash có thể để lại state inconsistent. Journaling hoặc copy-on-write filesystems quản lý ordering/atomicity để recovery có model rõ hơn.

## RAID không phải backup

RAID có thể cải thiện availability hoặc performance bằng striping/mirroring/parity. Nhưng RAID không bảo vệ khỏi accidental deletion, ransomware, logical corruption hay disaster phá cả array.

Backup tạo independent historical copy; replication/RAID chủ yếu giảm downtime do một số hardware failures. Hai mục tiêu khác nhau.

## Common Misconceptions

**“SSD không có random I/O penalty.”** Penalty nhỏ hơn HDD rất nhiều nhưng vẫn có queueing, FTL, garbage collection và write amplification.

**“write() thành công nghĩa là data đã nằm an toàn trên NAND/platter.”** Thường chỉ nghĩa kernel chấp nhận bytes; durability cần explicit contract.

**“NVMe luôn làm app nhanh hơn.”** Nếu bottleneck là CPU, lock, network hoặc database plan thì storage nhanh hơn ít ảnh hưởng.

## Mental Model

> Storage stack là chuỗi buffers và translation layers. Muốn reasoning về durability/performance, phải biết data hiện đang ở layer nào, unit I/O là gì và failure có thể xảy ra ở đâu.

## Kết nối

Đọc cùng [memory hierarchy](./02_memory_hierarchy_and_cache.md), [filesystem/storage I/O](../03_operating_systems/04_filesystems_storage_and_io.md) và [database WAL/recovery](../05_data_databases/04_storage_logs_recovery_and_durability.md).