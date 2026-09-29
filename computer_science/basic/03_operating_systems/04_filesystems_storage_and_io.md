# Filesystem, lưu trữ (storage / 저장소) và buffered I/O

> **Mạch đọc:** Đọc **Filesystem, lưu trữ (storage / 저장소) và buffered I/O** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **tệp (file / 파일) là lớp trừu tượng (abstraction / 추상화), không phải vùng bytes đơn giản** sang **Blocks, extents và allocation**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Lưu trữ (storage / 저장소) thiết bị (device / 장치) expose blocks/pages/sectors và thất bại (failure / 실패) characteristics, nhưng applications muốn named files, directories, permissions và durable byte streams. Filesystem (파일 시스템 / hệ thống tệp) tạo lớp trừu tượng (abstraction / 추상화) này, đồng thời phải giữ siêu dữ liệu (metadata / 메타데이터) nhất quán khi crash có thể xảy ra giữa bất kỳ writes nào.

## Tệp (file / 파일) là lớp trừu tượng (abstraction / 추상화), không phải vùng bytes đơn giản

Tệp (file / 파일) có dữ liệu (data / 데이터) + siêu dữ liệu (metadata / 메타데이터): kích thước (size / 크기), timestamps, permissions, quyền sở hữu (ownership / 소유권), khối (block / 블록) ánh xạ (mapping / 매핑). Directory map names tới tệp (file / 파일) identifiers/inodes-like objects. đường dẫn (path / 경로) resolution traverse directories và symbolic links theo rules.

Hard link và symbolic link khác nhau: hard link là thêm directory entry tới cùng underlying tệp (file / 파일) đối tượng (object / 객체); symlink là tệp (file / 파일) chứa đường dẫn (path / 경로) tham chiếu (reference / 참조). Delete directory entry không nhất thiết reclaim dữ liệu (data / 데이터) nếu còn hard links/open references.


> **Chuyển mạch:** Từ **tệp (file / 파일) là lớp trừu tượng (abstraction / 추상화), không phải vùng bytes đơn giản**, ta sang **Blocks, extents và allocation** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Blocks, extents và allocation

Filesystem map logical tệp (file / 파일) offsets tới vật lý (physical / 물리적)/thiết bị (device / 장치) blocks. Contiguous allocation nhanh nhưng khó grow; khối (block / 블록) lists linh hoạt nhưng siêu dữ liệu (metadata / 메타데이터) lớn; extents mô tả runs liên tục và cân bằng.

Fragmentation làm sequential logical tệp (file / 파일) thành scattered vật lý (physical / 물리적) locations, đặc biệt ảnh hưởng HDD seek; SSD giảm seek penalty nhưng vẫn có flash translation/erase hành vi (behavior / 동작) riêng.


> **Chuyển mạch:** Từ **Blocks, extents và allocation**, ta sang **Buffer/page bộ nhớ đệm (cache / 캐시)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Buffer/page bộ nhớ đệm (cache / 캐시)

OS bộ nhớ đệm (cache / 캐시) tệp (file / 파일) dữ liệu (data / 데이터) trong RAM. `read` có thể hit page bộ nhớ đệm (cache / 캐시) mà không thiết bị (device / 장치) I/O. `write` thường bản sao (copy / 복사)/mark pages dirty rồi background flush. Vì vậy benchmark lần hai có thể nhanh hơn lần đầu do bộ nhớ đệm (cache / 캐시).

Direct I/O hoặc cơ sở dữ liệu (database / 데이터베이스) buffer managers có thể bypass/coordinate page bộ nhớ đệm (cache / 캐시) để kiểm soát caching, alignment và durability rõ hơn.


> **Chuyển mạch:** Từ **Buffer/page bộ nhớ đệm (cache / 캐시)**, ta sang **Durability và fsync** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Durability và fsync

Ứng dụng (application / 애플리케이션) `write()` success không đồng nghĩa bits đã stable. dữ liệu (data / 데이터) có thể nằm người dùng (user / 사용자) buffer, kernel bộ nhớ đệm (cache / 캐시), thiết bị (device / 장치) bộ nhớ đệm (cache / 캐시). `fsync`/equivalent yêu cầu OS flush theo ngữ nghĩa (semantics / 의미론) cụ thể, nhưng real durability còn phụ thuộc thiết bị (device / 장치) guarantees/power-loss protection.

Thứ tự (ordering / 순서) quan trọng: nếu siêu dữ liệu (metadata / 메타데이터) nói khối (block / 블록) allocated trước khi dữ liệu (data / 데이터) thật được written, crash có thể expose garbage. Filesystems dùng journaling, sao chép khi ghi (copy-on-write / 쓰기 시 복사) hoặc log-structured designs để giữ consistency.


> **Chuyển mạch:** Từ **Durability và fsync**, ta sang **Journaling** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Journaling

Journaling ghi intended siêu dữ liệu (metadata / 메타데이터)/dữ liệu (data / 데이터) changes vào log trước hoặc theo giao thức (protocol / 프로토콜) rồi lần ghi nhận (commit / 커밋), cho phép khôi phục (recovery / 복구) replay/quay lui (rollback / 롤백) sau crash. Journal không phải backup; nó chủ yếu bảo vệ filesystem structural consistency.


> **Chuyển mạch:** Từ **Journaling**, ta sang **SSD và flash** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## SSD và flash

Flash không overwrite arbitrary byte như RAM. Nó program pages và erase larger blocks; controller dùng Flash Translation tầng (layer / 계층), wear leveling và garbage collection. ghi (write / 쓰기) amplification xuất hiện khi logical writes gây nhiều vật lý (physical / 물리적) movement.

TRIM cho SSD biết blocks logical không còn cần, giúp GC. cơ sở dữ liệu (database / 데이터베이스)/lưu trữ (storage / 저장소) engines quan tâm alignment/page kích thước (size / 크기)/ghi (write / 쓰기) mẫu (pattern / 패턴) vì thiết bị (device / 장치) hành vi (behavior / 동작) leak lên hiệu năng (performance / 성능).


> **Chuyển mạch:** Từ **SSD và flash**, ta sang **tệp (file / 파일) locking và concurrent truy cập (access / 접근)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Tệp (file / 파일) locking và concurrent truy cập (access / 접근)

Filesystem không tự làm chuỗi (sequence / 시퀀스) read-modify-write atomic theo nghiệp vụ (business / 비즈니스) ngữ nghĩa (semantics / 의미론). tệp (file / 파일) locks có advisory/mandatory variations, tiến trình (process / 프로세스) phạm vi (scope / 범위) và nền tảng (platform / 플랫폼) differences. Atomic rename thường là thành phần nguyên thủy (primitive / 기본 요소) hữu ích để publish replacement tệp (file / 파일), nhưng durability thứ tự (ordering / 순서) vẫn cần fsync directory/tệp (file / 파일) tùy OS.


> **Chuyển mạch:** Từ **tệp (file / 파일) locking và concurrent truy cập (access / 접근)**, ta sang **đối tượng (object / 객체) lưu trữ (storage / 저장소) khác filesystem** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Đối tượng (object / 객체) lưu trữ (storage / 저장소) khác filesystem

Cloud đối tượng (object / 객체) lưu trữ (storage / 저장소) expose keys/objects, không POSIX tệp (file / 파일) ngữ nghĩa (semantics / 의미론) đầy đủ. Operations, consistency, rename, partial cập nhật (update / 업데이트) và listing hành vi (behavior / 동작) khác. Mounting đối tượng (object / 객체) store như filesystem có thể tạo leaky lớp trừu tượng (abstraction / 추상화).


> **Chuyển mạch:** Từ **đối tượng (object / 객체) lưu trữ (storage / 저장소) khác filesystem**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> Filesystem map **names + byte ranges** xuống **blocks + siêu dữ liệu (metadata / 메타데이터)**, dùng bộ nhớ đệm (cache / 캐시) và crash-consistency giao thức (protocol / 프로토콜) để sống qua thất bại (failure / 실패). “Đã ghi (write / 쓰기)” và “đã durable” là hai trạng thái khác nhau.


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“Journaling là backup.”** Nó không bảo vệ khỏi delete lô-gic (logic / 논리), ransomware hay thiết bị (device / 장치) mất mát (loss / 손실).

**“tệp (file / 파일) delete luôn xóa bytes ngay.”** không gian tên (namespace / 네임스페이스) tham chiếu (reference / 참조) có thể mất trước khi blocks được reclaim/overwrite.

**“SSD chỉ là HDD nhanh hơn.”** nội bộ (internal / 내부) erase/program/FTL hành vi (behavior / 동작) tạo chi phí (cost / 비용) mô hình (model / 모델) khác.


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

[I/O/DMA](../02_computer_architecture/03_io_interrupts_dma_and_devices.md) là hardware ranh giới (boundary / 경계). [Database WAL/recovery](../05_data_databases/04_storage_logs_recovery_and_durability.md) xây durability ngữ nghĩa (semantics / 의미론) cao hơn trên filesystem/thiết bị (device / 장치). [Version control](../08_software_systems/01_version_control_build_link_and_packages.md) lưu đối tượng (object / 객체) graphs trên files/lưu trữ (storage / 저장소) abstractions.

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 kernel syscalls and os abstractions](./00_kernel_syscalls_and_os_abstractions.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
