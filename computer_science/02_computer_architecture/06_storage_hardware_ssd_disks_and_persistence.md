# Lưu trữ (storage / 저장소) hardware: SSD, disks và persistence

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Lưu trữ (storage / 저장소) hardware: SSD, disks và persistence**. Route đi từ media/latency → HDD/SSD và endurance → persistence, flush và failure modes → filesystem/database guarantees, để “đã ghi” được phân biệt với “sống sót sau mất điện”.

Phần mềm thường nhìn lưu trữ (storage / 저장소) qua tệp (file / 파일), page hoặc khối (block / 블록). Nhưng những abstractions này đứng trên thiết bị vật lý có hình học (geometry / 기하학), độ trễ (latency / 지연 시간) và thất bại (failure / 실패) modes riêng. Hiểu lưu trữ (storage / 저장소) hardware giúp giải thích tại sao sequential I/O khác random I/O, vì sao SSD cần wear leveling, tại sao `fsync` tồn tại và vì sao cơ sở dữ liệu (database / 데이터베이스) không thể coi “đã ghi (write / 쓰기)()” là “đã bền vững”.

## Persistence là một thuộc tính (property / 속성) vật lý rồi mới thành software đặc tả hợp đồng (contract / 계약)

RAM mất dữ liệu khi mất điện; lưu trữ (storage / 저장소) persistent (영구 저장장치) được thiết kế giữ trạng thái (state / 상태) qua power cycle. Nhưng “persistent” không có nghĩa mọi ghi (write / 쓰기) ngay lập tức an toàn. dữ liệu (data / 데이터) có thể đang nằm trong CPU bộ nhớ đệm (cache / 캐시), OS page bộ nhớ đệm (cache / 캐시), controller bộ nhớ đệm (cache / 캐시) hoặc volatile buffer của thiết bị (device / 장치).

Một durability guarantee phải nói rõ ranh giới (boundary / 경계) nào đã được vượt qua.

Persistence bắt đầu từ việc thiết bị giữ được trạng thái sau power cycle. HDD thực hiện điều đó bằng cơ học nên seek và rotational latency chi phối access; SSD dùng flash để đổi latency lấy các giới hạn erase, endurance và translation.

## HDD: cơ học tạo ra độ trễ (latency / 지연 시간) cấu trúc (structure / 구조)

Hard disk drive (HDD / 하드 디스크) có rotating platters và moving heads. Random truy cập (access / 접근) cần seek head + chờ sector quay tới vị trí phù hợp, nên độ trễ (latency / 지연 시간) milliseconds là đáng kể. Sequential truy cập (access / 접근) tránh nhiều seeks và có thông lượng (throughput / 처리량) cao hơn.

Đây là lý do cơ sở dữ liệu (database / 데이터베이스) các hệ thống (systems / 시스템들) historically tối ưu page bố cục (layout / 레이아웃), sequential log và B-tree để giảm random seeks.

HDD phạt random access bằng seek. SSD loại bỏ chuyển động cơ học nhưng vẫn phải quản lý page, block và garbage collection; filesystem cần báo vùng đã bỏ tham chiếu để controller làm việc hiệu quả.

## SSD: không seek nhưng không phải RAM lớn

Solid-state drive (SSD / 솔리드 스테이트 드라이브) dùng NAND flash. Read có thể theo pages, nhưng erase thường theo blocks lớn hơn. Flash cells có giới hạn erase cycles.

Vì không thể overwrite tùy ý như RAM, controller dùng Flash Translation tầng (layer / 계층) (FTL) để map logical khối (block / 블록) addresses sang vật lý (physical / 물리적) locations. Garbage collection gom live pages rồi erase blocks. Wear leveling phân bố writes để không một vùng hỏng sớm.

Do đó logical ghi (write / 쓰기) mẫu (pattern / 패턴) có thể tạo ghi (write / 쓰기) amplification: ứng dụng (application / 애플리케이션) ghi 1 MB nhưng thiết bị (device / 장치) nội bộ phải di chuyển/erase nhiều hơn 1 MB.

TRIM truyền thông tin ownership từ filesystem xuống FTL, nhưng không tự biến SSD thành RAM. Sau khi xét mapping và garbage collection, ta cần nhìn vào giao thức NVMe và cách nhiều request xếp hàng.

## TRIM và free không gian (space / 공간) thông tin (information / 정보)

Khi filesystem xóa tệp (file / 파일), thiết bị (device / 장치) thông thường chỉ thấy logical blocks không còn được tham chiếu (reference / 참조) ở tầng filesystem; nó không tự biết blocks nào thực sự free. TRIM/Discard truyền thông tin này xuống SSD để controller quản lý garbage collection tốt hơn.

Điều này cho thấy lớp trừu tượng (abstraction / 추상화) ranh giới (boundary / 경계) đôi khi cần hint từ tầng trên để tối ưu tầng dưới.

NVMe tăng parallel queues để khai thác SSD nhanh hơn, nhưng queueing chỉ có ý nghĩa khi request được đặt trên các đơn vị mà filesystem và database hiểu đúng. Sector, block, page và alignment quyết định một request chạm bao nhiêu đơn vị vật lý.

## NVMe và queueing

SATA/AHCI được thiết kế trong bối cảnh lưu trữ (storage / 저장소) chậm hơn. NVMe (Non-Volatile memory Express) tận dụng PCIe và hỗ trợ nhiều queues, hàng đợi (queue / 큐) độ sâu (depth / 깊이) lớn, parallel commands để khai thác SSD hiện đại.

Khi độ trễ (latency / 지연 시간) thiết bị (device / 장치) giảm, software overhead, interrupts, locks và ngữ cảnh (context / 맥락) switching trở thành tỷ lệ lớn hơn. Đây là mẫu (pattern / 패턴) phổ quát: tối ưu một tầng (layer / 계층) làm bottleneck dịch sang tầng (layer / 계층) khác.

Alignment ảnh hưởng số physical units bị đọc hoặc ghi. Nhưng ghi xong một unit vẫn chưa trả lời dữ liệu có sống sót sau crash hay không; câu hỏi đó thuộc về durability, flush và barriers.

## Sector, khối (block / 블록), page và alignment

Hardware sector, filesystem khối (block / 블록) và cơ sở dữ liệu (database / 데이터베이스) page không nhất thiết cùng kích thước. Misalignment có thể khiến một logical ghi (write / 쓰기) chạm nhiều vật lý (physical / 물리적) units.

Cơ sở dữ liệu (database / 데이터베이스) page thường được thiết kế để cân bằng siêu dữ liệu (metadata / 메타데이터) overhead, bộ nhớ đệm (cache / 캐시) hành vi (behavior / 동작) và I/O granularity. B+ cây (tree / 트리) nút (node / 노드) kích thước (size / 크기) thường gần page kích thước (size / 크기) để một nút (node / 노드) truy cập (access / 접근) tương ứng một page I/O.

Durability phụ thuộc vào ranh giới flush và thứ tự ghi, không chỉ vào geometry của storage. Ngay cả dữ liệu đã bền trên một device cũng cần chiến lược availability và recovery riêng, nên RAID phải được phân biệt với backup.

## Durability, flush và barriers

OS có thể acknowledge `write()` sau khi bản sao (copy / 복사) bytes vào page bộ nhớ đệm (cache / 캐시). Để yêu cầu dữ liệu đi tới durable lưu trữ (storage / 저장소), ứng dụng (application / 애플리케이션) dùng mechanisms như `fsync`/`fdatasync`, nhưng actual guarantee còn phụ thuộc filesystem và thiết bị (device / 장치) bộ nhớ đệm (cache / 캐시) hành vi (behavior / 동작).

Ghi (write / 쓰기) thứ tự (ordering / 순서) cũng quan trọng. Nếu siêu dữ liệu (metadata / 메타데이터) nói “tệp (file / 파일) mới tồn tại” được persisted trước dữ liệu (data / 데이터) content, crash có thể để lại trạng thái (state / 상태) inconsistent. Journaling hoặc sao chép khi ghi (copy-on-write / 쓰기 시 복사) filesystems quản lý thứ tự (ordering / 순서)/atomicity để khôi phục (recovery / 복구) có mô hình (model / 모델) rõ hơn.

Durability bảo vệ dữ liệu trước một số kiểu crash; RAID chủ yếu giảm downtime khi một phần hardware hỏng, còn backup giữ lịch sử trước xóa nhầm hoặc corruption. Ba mục tiêu này cần được tách khi kiểm tra các ngộ nhận.

## RAID không phải backup

RAID có thể cải thiện availability hoặc hiệu năng (performance / 성능) bằng striping/mirroring/parity. Nhưng RAID không bảo vệ khỏi accidental deletion, ransomware, logical corruption hay disaster phá cả array.

Backup tạo independent historical bản sao (copy / 복사); replication/RAID chủ yếu giảm downtime do một số hardware failures. Hai mục tiêu khác nhau.

Các ngộ nhận trên đều bỏ qua một lớp buffer, translation hoặc failure boundary. Mô hình tư duy tiếp theo gom các lớp đó thành đường đi của dữ liệu và câu hỏi cần đặt khi đo durability hoặc performance.

## Dùng chung (common / 공통) Misconceptions

**“SSD không có random I/O penalty.”** Penalty nhỏ hơn HDD rất nhiều nhưng vẫn có queueing, FTL, garbage collection và ghi (write / 쓰기) amplification.

**“ghi (write / 쓰기)() thành công nghĩa là dữ liệu (data / 데이터) đã nằm an toàn trên NAND/platter.”** Thường chỉ nghĩa kernel chấp nhận bytes; durability cần tường minh (explicit / 명시적) đặc tả hợp đồng (contract / 계약).

**“NVMe luôn làm app nhanh hơn.”** Nếu bottleneck là CPU, khóa (lock / 잠금), mạng (network / 네트워크) hoặc cơ sở dữ liệu (database / 데이터베이스) plan thì lưu trữ (storage / 저장소) nhanh hơn ít ảnh hưởng.

## Mô hình tư duy (mental model / 사고 모델)

> lưu trữ (storage / 저장소) ngăn xếp (stack / 스택) là chuỗi buffers và translation layers. Muốn lập luận (reasoning / 추론) về durability/hiệu năng (performance / 성능), phải biết dữ liệu (data / 데이터) hiện đang ở tầng (layer / 계층) nào, đơn vị (unit / 단위) I/O là gì và thất bại (failure / 실패) có thể xảy ra ở đâu.

Mỗi claim về storage cần chỉ rõ tầng đang giữ dữ liệu, đơn vị I/O và failure boundary. Kết nối cuối file đưa câu hỏi đó sang memory hierarchy, filesystem và database recovery.

## Kết nối

Đọc cùng [memory hierarchy](./02_memory_hierarchy_and_cache.md), [filesystem/storage I/O](../03_operating_systems/04_filesystems_storage_and_io.md) và [database WAL/recovery](../05_data_databases/04_storage_logs_recovery_and_durability.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
