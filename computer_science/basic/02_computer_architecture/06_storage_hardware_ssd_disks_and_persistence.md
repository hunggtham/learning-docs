# Lưu trữ (storage / 저장소) hardware: SSD, disks và persistence

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Lưu trữ (storage / 저장소) hardware: SSD, disks và persistence**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Persistence là một thuộc tính (property / 속성) vật lý rồi mới thành software đặc tả hợp đồng (contract / 계약)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **HDD: cơ học tạo ra độ trễ (latency / 지연 시간) cấu trúc (structure / 구조)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Phần mềm thường nhìn lưu trữ (storage / 저장소) qua tệp (file / 파일), page hoặc khối (block / 블록). Nhưng những abstractions này đứng trên thiết bị vật lý có hình học (geometry / 기하학), độ trễ (latency / 지연 시간) và thất bại (failure / 실패) modes riêng. Hiểu lưu trữ (storage / 저장소) hardware giúp giải thích tại sao sequential I/O khác random I/O, vì sao SSD cần wear leveling, tại sao `fsync` tồn tại và vì sao cơ sở dữ liệu (database / 데이터베이스) không thể coi “đã ghi (write / 쓰기)()” là “đã bền vững”.

## Persistence là một thuộc tính (property / 속성) vật lý rồi mới thành software đặc tả hợp đồng (contract / 계약)

RAM mất dữ liệu khi mất điện; lưu trữ (storage / 저장소) persistent (영구 저장장치) được thiết kế giữ trạng thái (state / 상태) qua power cycle. Nhưng “persistent” không có nghĩa mọi ghi (write / 쓰기) ngay lập tức an toàn. dữ liệu (data / 데이터) có thể đang nằm trong CPU bộ nhớ đệm (cache / 캐시), OS page bộ nhớ đệm (cache / 캐시), controller bộ nhớ đệm (cache / 캐시) hoặc volatile buffer của thiết bị (device / 장치).

Một durability guarantee phải nói rõ ranh giới (boundary / 경계) nào đã được vượt qua.

> **Chuyển mạch:** Trong **Lưu trữ (storage / 저장소) hardware: SSD, disks và persistence**, **HDD: cơ học tạo ra độ trễ (latency / 지연 시간) cấu trúc (structure / 구조)** tiếp nhận điểm tựa từ **Persistence là một thuộc tính (property / 속성) vật lý rồi mới thành software đặc tả hợp đồng (contract / 계약)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SSD: không seek nhưng không phải RAM lớn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## HDD: cơ học tạo ra độ trễ (latency / 지연 시간) cấu trúc (structure / 구조)

Hard disk drive (HDD / 하드 디스크) có rotating platters và moving heads. Random truy cập (access / 접근) cần seek head + chờ sector quay tới vị trí phù hợp, nên độ trễ (latency / 지연 시간) milliseconds là đáng kể. Sequential truy cập (access / 접근) tránh nhiều seeks và có thông lượng (throughput / 처리량) cao hơn.

Đây là lý do cơ sở dữ liệu (database / 데이터베이스) các hệ thống (systems / 시스템들) historically tối ưu page bố cục (layout / 레이아웃), sequential log và B-tree để giảm random seeks.

> **Chuyển mạch:** Ở chặng này của **Lưu trữ (storage / 저장소) hardware: SSD, disks và persistence**, **SSD: không seek nhưng không phải RAM lớn** tiếp nhận điểm tựa từ **HDD: cơ học tạo ra độ trễ (latency / 지연 시간) cấu trúc (structure / 구조)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **TRIM và free không gian (space / 공간) thông tin (information / 정보)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SSD: không seek nhưng không phải RAM lớn

Solid-state drive (SSD / 솔리드 스테이트 드라이브) dùng NAND flash. Read có thể theo pages, nhưng erase thường theo blocks lớn hơn. Flash cells có giới hạn erase cycles.

Vì không thể overwrite tùy ý như RAM, controller dùng Flash Translation tầng (layer / 계층) (FTL) để map logical khối (block / 블록) addresses sang vật lý (physical / 물리적) locations. Garbage collection gom live pages rồi erase blocks. Wear leveling phân bố writes để không một vùng hỏng sớm.

Do đó logical ghi (write / 쓰기) mẫu (pattern / 패턴) có thể tạo ghi (write / 쓰기) amplification: ứng dụng (application / 애플리케이션) ghi 1 MB nhưng thiết bị (device / 장치) nội bộ phải di chuyển/erase nhiều hơn 1 MB.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lưu trữ (storage / 저장소) hardware: SSD, disks và persistence**, **TRIM và free không gian (space / 공간) thông tin (information / 정보)** tiếp nhận điểm tựa từ **SSD: không seek nhưng không phải RAM lớn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **NVMe và queueing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## TRIM và free không gian (space / 공간) thông tin (information / 정보)

Khi filesystem xóa tệp (file / 파일), thiết bị (device / 장치) thông thường chỉ thấy logical blocks không còn được tham chiếu (reference / 참조) ở tầng filesystem; nó không tự biết blocks nào thực sự free. TRIM/Discard truyền thông tin này xuống SSD để controller quản lý garbage collection tốt hơn.

Điều này cho thấy lớp trừu tượng (abstraction / 추상화) ranh giới (boundary / 경계) đôi khi cần hint từ tầng trên để tối ưu tầng dưới.

> **Chuyển mạch:** Trong **Lưu trữ (storage / 저장소) hardware: SSD, disks và persistence**, **NVMe và queueing** tiếp nhận điểm tựa từ **TRIM và free không gian (space / 공간) thông tin (information / 정보)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sector, khối (block / 블록), page và alignment** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## NVMe và queueing

SATA/AHCI được thiết kế trong bối cảnh lưu trữ (storage / 저장소) chậm hơn. NVMe (Non-Volatile memory Express) tận dụng PCIe và hỗ trợ nhiều queues, hàng đợi (queue / 큐) độ sâu (depth / 깊이) lớn, parallel commands để khai thác SSD hiện đại.

Khi độ trễ (latency / 지연 시간) thiết bị (device / 장치) giảm, software overhead, interrupts, locks và ngữ cảnh (context / 맥락) switching trở thành tỷ lệ lớn hơn. Đây là mẫu (pattern / 패턴) phổ quát: tối ưu một tầng (layer / 계층) làm bottleneck dịch sang tầng (layer / 계층) khác.

> **Chuyển mạch:** Ở chặng này của **Lưu trữ (storage / 저장소) hardware: SSD, disks và persistence**, **Sector, khối (block / 블록), page và alignment** tiếp nhận điểm tựa từ **NVMe và queueing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Durability, flush và barriers** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sector, khối (block / 블록), page và alignment

Hardware sector, filesystem khối (block / 블록) và cơ sở dữ liệu (database / 데이터베이스) page không nhất thiết cùng kích thước. Misalignment có thể khiến một logical ghi (write / 쓰기) chạm nhiều vật lý (physical / 물리적) units.

Cơ sở dữ liệu (database / 데이터베이스) page thường được thiết kế để cân bằng siêu dữ liệu (metadata / 메타데이터) overhead, bộ nhớ đệm (cache / 캐시) hành vi (behavior / 동작) và I/O granularity. B+ cây (tree / 트리) nút (node / 노드) kích thước (size / 크기) thường gần page kích thước (size / 크기) để một nút (node / 노드) truy cập (access / 접근) tương ứng một page I/O.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lưu trữ (storage / 저장소) hardware: SSD, disks và persistence**, **Durability, flush và barriers** tiếp nhận điểm tựa từ **Sector, khối (block / 블록), page và alignment** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **RAID không phải backup** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Durability, flush và barriers

OS có thể acknowledge `write()` sau khi bản sao (copy / 복사) bytes vào page bộ nhớ đệm (cache / 캐시). Để yêu cầu dữ liệu đi tới durable lưu trữ (storage / 저장소), ứng dụng (application / 애플리케이션) dùng mechanisms như `fsync`/`fdatasync`, nhưng actual guarantee còn phụ thuộc filesystem và thiết bị (device / 장치) bộ nhớ đệm (cache / 캐시) hành vi (behavior / 동작).

Ghi (write / 쓰기) thứ tự (ordering / 순서) cũng quan trọng. Nếu siêu dữ liệu (metadata / 메타데이터) nói “tệp (file / 파일) mới tồn tại” được persisted trước dữ liệu (data / 데이터) content, crash có thể để lại trạng thái (state / 상태) inconsistent. Journaling hoặc sao chép khi ghi (copy-on-write / 쓰기 시 복사) filesystems quản lý thứ tự (ordering / 순서)/atomicity để khôi phục (recovery / 복구) có mô hình (model / 모델) rõ hơn.

> **Chuyển mạch:** Trong **Lưu trữ (storage / 저장소) hardware: SSD, disks và persistence**, **RAID không phải backup** tiếp nhận điểm tựa từ **Durability, flush và barriers** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## RAID không phải backup

RAID có thể cải thiện availability hoặc hiệu năng (performance / 성능) bằng striping/mirroring/parity. Nhưng RAID không bảo vệ khỏi accidental deletion, ransomware, logical corruption hay disaster phá cả array.

Backup tạo independent historical bản sao (copy / 복사); replication/RAID chủ yếu giảm downtime do một số hardware failures. Hai mục tiêu khác nhau.

> **Chuyển mạch:** Ở chặng này của **Lưu trữ (storage / 저장소) hardware: SSD, disks và persistence**, **Dùng chung (common / 공통) Misconceptions** tiếp nhận điểm tựa từ **RAID không phải backup** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“SSD không có random I/O penalty.”** Penalty nhỏ hơn HDD rất nhiều nhưng vẫn có queueing, FTL, garbage collection và ghi (write / 쓰기) amplification.

**“ghi (write / 쓰기)() thành công nghĩa là dữ liệu (data / 데이터) đã nằm an toàn trên NAND/platter.”** Thường chỉ nghĩa kernel chấp nhận bytes; durability cần tường minh (explicit / 명시적) đặc tả hợp đồng (contract / 계약).

**“NVMe luôn làm app nhanh hơn.”** Nếu bottleneck là CPU, khóa (lock / 잠금), mạng (network / 네트워크) hoặc cơ sở dữ liệu (database / 데이터베이스) plan thì lưu trữ (storage / 저장소) nhanh hơn ít ảnh hưởng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lưu trữ (storage / 저장소) hardware: SSD, disks và persistence**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Dùng chung (common / 공통) Misconceptions** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> lưu trữ (storage / 저장소) ngăn xếp (stack / 스택) là chuỗi buffers và translation layers. Muốn lập luận (reasoning / 추론) về durability/hiệu năng (performance / 성능), phải biết dữ liệu (data / 데이터) hiện đang ở tầng (layer / 계층) nào, đơn vị (unit / 단위) I/O là gì và thất bại (failure / 실패) có thể xảy ra ở đâu.

> **Chuyển mạch:** Trong **Lưu trữ (storage / 저장소) hardware: SSD, disks và persistence**, **Kết nối** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc cùng [memory hierarchy](./02_memory_hierarchy_and_cache.md), [filesystem/storage I/O](../03_operating_systems/04_filesystems_storage_and_io.md) và [database WAL/recovery](../05_data_databases/04_storage_logs_recovery_and_durability.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
