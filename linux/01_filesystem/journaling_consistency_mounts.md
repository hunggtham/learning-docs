# Journaling, tính nhất quán và cơ chế mount của filesystem

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Journaling, tính nhất quán và cơ chế mount của filesystem**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Vấn đề cơ bản: một thao tác lô-gic (logic / 논리) có thể cần nhiều thao tác vật lý** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Journaling giải quyết điều gì?** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối journaling với tính nhất quán và mount để xác định phần nào được bảo vệ khi thao tác logic bị ngắt giữa chừng.

Một hệ thống tệp (filesystem) không chỉ cần lưu dữ liệu; nó còn phải giữ cấu trúc siêu dữ liệu (metadata / 메타데이터) nhất quán khi hệ thống mất điện, kernel panic hoặc lưu trữ (storage / 저장소) trả lỗi giữa chừng. Nếu một thao tác cập nhật cần sửa nhiều nơi nhưng chỉ hoàn tất một phần, filesystem có thể rơi vào trạng thái khó hiểu: khối (block / 블록) đã được đánh dấu sử dụng nhưng directory entry chưa tồn tại, hoặc inode đã đổi nhưng bitmap chưa khớp.

Đó là lý do cần hiểu **tính nhất quán (consistency)** và **nhật ký giao dịch (journaling)**.

## Vấn đề cơ bản: một thao tác lô-gic (logic / 논리) có thể cần nhiều thao tác vật lý

Giả sử tạo tệp (file / 파일) mới. Ở mức người dùng chỉ có:

```bash
touch report.txt
```

Nhưng filesystem có thể phải:

1. cấp phát inode;
2. cập nhật inode bitmap;
3. tạo directory entry;
4. cập nhật siêu dữ liệu (metadata / 메타데이터) của thư mục;
5. có thể cấp dữ liệu (data / 데이터) khối (block / 블록) nếu tệp (file / 파일) có nội dung;
6. ghi các thay đổi xuống lưu trữ (storage / 저장소).

Nếu máy mất điện ở giữa chuỗi này, một phần đã xuống disk còn phần khác chưa xuống.

Filesystem phải có cách phục hồi để cấu trúc vẫn hợp lệ.

> **Nối mạch:** Trong **Journaling, tính nhất quán và cơ chế mount của filesystem**, **Journaling giải quyết điều gì?** nối từ **Vấn đề cơ bản: một thao tác lô-gic (logic / 논리) có thể cần nhiều thao tác vật lý** sang **Siêu dữ liệu (metadata / 메타데이터) journaling và dữ liệu (data / 데이터) journaling**, vì cơ chế trước tạo đầu vào cho bước sau.

## Journaling giải quyết điều gì?

**Journaling** ghi thông tin về các thay đổi dự định thực hiện vào một vùng nhật ký trước hoặc trong quá trình áp dụng lên cấu trúc chính.

Sau crash, filesystem có thể kiểm tra journal để biết giao dịch (transaction / 트랜잭션) nào hoàn tất và giao dịch (transaction / 트랜잭션) nào cần replay/quay lui (rollback / 롤백) theo ngữ nghĩa (semantics / 의미론) của filesystem.

Điểm quan trọng là journaling chủ yếu giúp **tính nhất quán siêu dữ liệu (metadata / 메타데이터)** và thời gian phục hồi. Nó không có nghĩa mọi byte ứng dụng (application / 애플리케이션) vừa ghi đều chắc chắn đã bền vững trên lưu trữ (storage / 저장소).

> **Nối mạch:** Ở chặng này của **Journaling, tính nhất quán và cơ chế mount của filesystem**, **Journaling giải quyết điều gì?** đặt vấn đề; **Siêu dữ liệu (metadata / 메타데이터) journaling và dữ liệu (data / 데이터) journaling** đối chiếu bằng chứng, rồi **write() không đồng nghĩa dữ liệu đã bền vững** mở rộng hệ quả hoặc giới hạn liên quan.

## Siêu dữ liệu (metadata / 메타데이터) journaling và dữ liệu (data / 데이터) journaling

Các filesystem có thể journal siêu dữ liệu (metadata / 메타데이터) và/hoặc dữ liệu (data / 데이터) theo những chế độ khác nhau.

Ở ext4, các chế độ thường được nhắc đến gồm:

- `data=ordered` — siêu dữ liệu (metadata / 메타데이터) được journal, dữ liệu (data / 데이터) được ghi trước khi siêu dữ liệu (metadata / 메타데이터) liên quan được lần ghi nhận (commit / 커밋) theo thứ tự (ordering / 순서) nhất định;
- `data=writeback` — thứ tự (ordering / 순서) dữ liệu (data / 데이터) yếu hơn;
- `data=journal` — cả dữ liệu (data / 데이터) và siêu dữ liệu (metadata / 메타데이터) đi qua journal, chi phí cao hơn.

Không nên đổi mount chế độ (mode / 모드) chỉ vì thấy benchmark trên internet. sự đánh đổi (trade-off / 트레이드오프) liên quan durability, thông lượng (throughput / 처리량), độ trễ (latency / 지연 시간) và tải công việc (workload / 워크로드).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Journaling, tính nhất quán và cơ chế mount của filesystem**, **Siêu dữ liệu (metadata / 메타데이터) journaling và dữ liệu (data / 데이터) journaling** đặt vấn đề; **write() không đồng nghĩa dữ liệu đã bền vững** đối chiếu bằng chứng, rồi **sync, fsync và flush** mở rộng hệ quả hoặc giới hạn liên quan.

## `write()` không đồng nghĩa dữ liệu đã bền vững

Ứng dụng (application / 애플리케이션) gọi:

```text
write(fd, data, ...)
```

Kernel có thể nhận dữ liệu vào page bộ nhớ đệm (cache / 캐시) và trả success trước khi lưu trữ (storage / 저장소) vật lý hoàn tất ghi.

Để yêu cầu đồng bộ mạnh hơn, ứng dụng (application / 애플리케이션) có thể dùng `fsync()` hoặc các cơ chế tương đương.

Điều này đặc biệt quan trọng với cơ sở dữ liệu (database / 데이터베이스).

> cơ sở dữ liệu (database / 데이터베이스) không thể chỉ tin rằng “lời gọi hệ thống (system call / 시스템 호출) ghi (write / 쓰기) thành công” đồng nghĩa giao dịch (transaction / 트랜잭션) đã an toàn trước power mất mát (loss / 손실).

Các hệ quản trị cơ sở dữ liệu thường có write-ahead log và cơ chế fsync riêng để đạt durability theo ACID.

> **Nối mạch:** Trong **Journaling, tính nhất quán và cơ chế mount của filesystem**, **write() không đồng nghĩa dữ liệu đã bền vững** đặt vấn đề; **sync, fsync và flush** đối chiếu bằng chứng, rồi **Atomic rename** mở rộng hệ quả hoặc giới hạn liên quan.

## `sync`, `fsync` và flush

Command:

```bash
sync
```

đề nghị kernel flush dữ liệu filesystem đang chờ ra lưu trữ (storage / 저장소).

Trong mã (code / 코드), `fsync(fd)` yêu cầu đồng bộ dữ liệu/siêu dữ liệu (metadata / 메타데이터) liên quan descriptor theo ngữ nghĩa (semantics / 의미론) hệ thống.

Nhưng durability cuối cùng còn phụ thuộc lưu trữ (storage / 저장소) controller, drive bộ nhớ đệm (cache / 캐시), hypervisor và cloud lưu trữ (storage / 저장소) hiện thực (implementation / 구현).

Do đó “đã fsync” là một guarantee mạnh ở OS giao diện (interface / 인터페이스), nhưng phần cứng/lưu trữ (storage / 저장소) ngăn xếp (stack / 스택) vẫn phải thực hiện đúng đặc tả hợp đồng (contract / 계약).

> **Nối mạch:** Ở chặng này của **Journaling, tính nhất quán và cơ chế mount của filesystem**, **Atomic rename** nối từ **sync, fsync và flush** sang **Tại sao cross-filesystem rename không giống nhau?**, vì cơ chế trước tạo đầu vào cho bước sau.

## Atomic rename

Mẫu (pattern / 패턴) rất quan trọng trong môi trường vận hành (production / 운영 환경) là ghi tệp (file / 파일) mới rồi rename:

```bash
printf '%s\n' 'new-config' > config.yml.tmp
mv config.yml.tmp config.yml
```

Rename trong cùng filesystem thường là atomic ở không gian tên (namespace / 네임스페이스) mức (level / 수준): observer thấy tên cũ hoặc tên mới, thay vì thấy tệp (file / 파일) bị ghi dở giữa chừng.

Mẫu (pattern / 패턴) an toàn hơn cho nhiều tình huống:

```text
write temporary file
        ↓
fsync temporary file khi cần durability
        ↓
rename temporary -> target
        ↓
fsync directory khi durability của directory entry là yêu cầu nghiêm ngặt
```

Ứng dụng (application / 애플리케이션) updater, trình quản lý gói (package manager / 패키지 관리자) và cấu hình (config / 설정) triển khai (deployment / 배포) thường tận dụng ý tưởng này.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Journaling, tính nhất quán và cơ chế mount của filesystem**, **Tại sao cross-filesystem rename không giống nhau?** nối từ **Atomic rename** sang **Mount điểm (point / 지점) và không gian tên (namespace / 네임스페이스)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Tại sao cross-filesystem rename không giống nhau?

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

```bash
mv /tmp/a /data/a
```

Nếu `/tmp` và `/data` nằm trên hai filesystem khác nhau, kernel không thể chỉ đổi directory entry cùng inode không gian tên (namespace / 네임스페이스). `mv` có thể phải bản sao (copy / 복사) rồi unlink nguồn.

Do đó thao tác không còn có cùng tính atomic như rename nội bộ filesystem.

Kiểm tra:

```bash
findmnt -T /tmp/a
findmnt -T /data
```

> **Nối mạch:** Trong **Journaling, tính nhất quán và cơ chế mount của filesystem**, **Mount điểm (point / 지점) và không gian tên (namespace / 네임스페이스)** nối từ **Tại sao cross-filesystem rename không giống nhau?** sang **Vì sao umount báo busy?**, vì cơ chế trước tạo đầu vào cho bước sau.

## Mount điểm (point / 지점) và không gian tên (namespace / 네임스페이스)

Khi filesystem được mount vào `/data`, nội dung directory `/data` trước đó bị che bởi mount mới trong không gian tên (namespace / 네임스페이스) hiện tại.

Ví dụ:

```bash
mkdir /mnt/test
mount /dev/sdb1 /mnt/test
```

Sau mount, đường dẫn `/mnt/test` resolve vào filesystem mới.

Unmount:

```bash
sudo umount /mnt/test
```

thì nội dung underlying directory lại thấy được.

Điều này giải thích một số tình huống “tệp (file / 파일) biến mất sau mount” nhưng thực ra dữ liệu cũ vẫn nằm ở filesystem bên dưới.

> **Nối mạch:** Ở chặng này của **Journaling, tính nhất quán và cơ chế mount của filesystem**, **Vì sao umount báo busy?** nối từ **Mount điểm (point / 지점) và không gian tên (namespace / 네임스페이스)** sang **Bind mount**, vì cơ chế trước tạo đầu vào cho bước sau.

## Vì sao `umount` báo busy?

Kernel không thể unmount an toàn nếu tài nguyên (resource / 자원) vẫn đang được sử dụng.

Nguyên nhân có thể gồm:

- tiến trình (process / 프로세스) có hiện tại (current / 현재) working directory trong mount;
- tệp (file / 파일) descriptor đang mở;
- filesystem con được mount bên dưới;
- memory-mapped tệp (file / 파일) vẫn tham chiếu.

Điều tra:

```bash
findmnt /data
sudo lsof +f -- /data
sudo fuser -vm /data
```

Không nên dùng forced/lazy unmount như phản xạ đầu tiên trên môi trường vận hành (production / 운영 환경).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Journaling, tính nhất quán và cơ chế mount của filesystem**, **Bind mount** nối từ **Vì sao umount báo busy?** sang **Read-only mount**, vì cơ chế trước tạo đầu vào cho bước sau.

## Bind mount

Bind mount cho phép một phần cây filesystem xuất hiện ở vị trí khác:

```bash
sudo mount --bind /opt/app/data /srv/data
```

Hai pathname khác nhau có thể dẫn đến cùng underlying objects.

Containers sử dụng mount không gian tên (namespace / 네임스페이스) và bind mount rất nhiều để tạo filesystem view riêng.

> **Nối mạch:** Trong **Journaling, tính nhất quán và cơ chế mount của filesystem**, **Read-only mount** nối từ **Bind mount** sang **noexec, nosuid, nodev**, vì cơ chế trước tạo đầu vào cho bước sau.

## Read-only mount

Mount có thể được đặt chỉ đọc:

```bash
mount -o remount,ro /mountpoint
```

Một tiến trình (process / 프로세스) dù có UID gốc (root / 루트) hoặc tệp (file / 파일) chế độ (mode / 모드) `777` vẫn không thể ghi theo cách bình thường nếu filesystem được mount read-only.

Đây là ví dụ rõ rằng permission bits chỉ là một tầng (layer / 계층) trong quyết định truy cập (access / 접근).

> **Nối mạch:** Ở chặng này của **Journaling, tính nhất quán và cơ chế mount của filesystem**, **noexec, nosuid, nodev** nối từ **Read-only mount** sang **ext4, XFS và lựa chọn filesystem**, vì cơ chế trước tạo đầu vào cho bước sau.

## `noexec`, `nosuid`, `nodev`

Mount options có thể thay đổi chính sách (policy / 정책):

- `noexec` hạn chế thực thi nhị phân (binary / 이진) theo ngữ nghĩa (semantics / 의미론) mount;
- `nosuid` vô hiệu hóa tác dụng setuid/setgid trong nhiều trường hợp;
- `nodev` không diễn giải thiết bị (device / 장치) nodes trên filesystem đó.

Các option này thường dùng trong hardening, nhưng có thể phá ứng dụng (application / 애플리케이션) nếu áp dụng mà không hiểu nhu cầu.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Journaling, tính nhất quán và cơ chế mount của filesystem**, **ext4, XFS và lựa chọn filesystem** nối từ **noexec, nosuid, nodev** sang **Filesystem check**, vì cơ chế trước tạo đầu vào cho bước sau.

## ext4, XFS và lựa chọn filesystem

Không có filesystem “tốt nhất” cho mọi tải công việc (workload / 워크로드).

ext4 phổ biến, ổn định và dễ dùng. XFS mạnh ở quy mô (scale / 규모) lớn và parallel I/O trong nhiều tải công việc (workload / 워크로드). Btrfs/ZFS-style các hệ thống (systems / 시스템들) cung cấp các tính năng như sao chép khi ghi (copy-on-write / 쓰기 시 복사), snapshot hoặc checksum với sự đánh đổi (trade-off / 트레이드오프) khác.

Lựa chọn nên dựa trên:

- tải công việc (workload / 워크로드);
- phân phối (distribution / 분포) hỗ trợ (support / 지원);
- operational expertise;
- backup/restore chiến lược (strategy / 전략);
- hiệu năng (performance / 성능) characteristics;
- tính năng (feature / 기능) requirements.

> **Nối mạch:** Trong **Journaling, tính nhất quán và cơ chế mount của filesystem**, **Filesystem check** nối từ **ext4, XFS và lựa chọn filesystem** sang **Crash consistency không bằng ứng dụng (application / 애플리케이션) consistency**, vì cơ chế trước tạo đầu vào cho bước sau.

## Filesystem check

Một số filesystem có công cụ (tool / 도구) kiểm tra/repair như `fsck`, `xfs_repair`.

Không nên chạy repair công cụ (tool / 도구) tùy tiện trên mounted môi trường vận hành (production / 운영 환경) filesystem.

Ví dụ ext filesystem:

```bash
sudo fsck /dev/sdXN
```

thường yêu cầu filesystem unmounted hoặc boot vào maintenance ngữ cảnh (context / 맥락) phù hợp.

Trước repair phải hiểu lưu trữ (storage / 저장소) topology và có backup nếu có thể.

> **Nối mạch:** Ở chặng này của **Journaling, tính nhất quán và cơ chế mount của filesystem**, **Crash consistency không bằng ứng dụng (application / 애플리케이션) consistency** nối từ **Filesystem check** sang **Mối liên hệ với ảnh bộ chứa (container image / 컨테이너 이미지)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Crash consistency không bằng ứng dụng (application / 애플리케이션) consistency

Filesystem có thể hoàn toàn nhất quán sau crash nhưng ứng dụng (application / 애플리케이션) dữ liệu (data / 데이터) vẫn sai lô-gic (logic / 논리).

Ví dụ:

```text
account A đã trừ tiền
account B chưa cộng tiền
```

Hai tệp (file / 파일)/cơ sở dữ liệu (database / 데이터베이스) pages đều structurally valid, nhưng nghiệp vụ (business / 비즈니스) giao dịch (transaction / 트랜잭션) incomplete.

Đó là lý do cơ sở dữ liệu (database / 데이터베이스) giao dịch (transaction / 트랜잭션) tầng (layer / 계층) tồn tại trên filesystem tầng (layer / 계층).

Filesystem bảo vệ cấu trúc lưu trữ; cơ sở dữ liệu (database / 데이터베이스) bảo vệ invariants cấp dữ liệu.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Journaling, tính nhất quán và cơ chế mount của filesystem**, **Mối liên hệ với ảnh bộ chứa (container image / 컨테이너 이미지)** nối từ **Crash consistency không bằng ứng dụng (application / 애플리케이션) consistency** sang **Mô hình tư duy**, vì cơ chế trước tạo đầu vào cho bước sau.

## Mối liên hệ với ảnh bộ chứa (container image / 컨테이너 이미지)

Layered bộ chứa (container / 컨테이너) filesystems thường dùng sao chép khi ghi (copy-on-write / 쓰기 시 복사) (CoW). Khi tệp (file / 파일) trong lower ảnh (image / 이미지) tầng (layer / 계층) bị sửa, thời gian chạy (runtime / 런타임) có thể bản sao (copy / 복사) dữ liệu vào writable tầng (layer / 계층).

Điều này có thể làm I/O hành vi (behavior / 동작) khác host filesystem trực tiếp, đặc biệt với cơ sở dữ liệu (database / 데이터베이스) tải công việc (workload / 워크로드). Vì vậy cơ sở dữ liệu (database / 데이터베이스) persistent dữ liệu (data / 데이터) thường được đặt trên volume riêng thay vì writable bộ chứa (container / 컨테이너) tầng (layer / 계층).

> **Nối mạch:** Trong **Journaling, tính nhất quán và cơ chế mount của filesystem**, **Mô hình tư duy** tổng hợp từ **Mối liên hệ với ảnh bộ chứa (container image / 컨테이너 이미지)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những hiểu lầm phổ biến** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy

Có thể hình dung durability ngăn xếp (stack / 스택):

```text
application
   ↓
runtime/library buffering
   ↓
kernel page cache
   ↓
filesystem + journal
   ↓
block layer
   ↓
controller / virtual disk
   ↓
physical or remote storage
```

Một lời gọi ghi chỉ đi qua từng tầng (layer / 계층) theo đặc tả hợp đồng (contract / 계약) tương ứng. Khi đánh giá “dữ liệu đã an toàn chưa?”, phải hỏi an toàn tới tầng (layer / 계층) nào.

> **Nối mạch:** Ở chặng này của **Journaling, tính nhất quán và cơ chế mount của filesystem**, **Những hiểu lầm phổ biến** tổng hợp từ **Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Những hiểu lầm phổ biến

**“Filesystem có journal thì không thể mất dữ liệu.”** Journal chủ yếu giúp consistency; durability của ứng dụng (application / 애플리케이션) còn phụ thuộc flush/fsync và lưu trữ (storage / 저장소) ngăn xếp (stack / 스택).

**“`mv` luôn atomic.”** Rename cùng filesystem có ngữ nghĩa (semantics / 의미론) mạnh; cross-filesystem `mv` có thể trở thành bản sao (copy / 복사) + unlink.

**“Permission đúng thì chắc chắn ghi được.”** Read-only mount hoặc bảo mật (security / 보안) chính sách (policy / 정책) vẫn có thể chặn.

**“`df` đầy là do tệp (file / 파일) visible.”** Deleted-open files, reserved blocks và siêu dữ liệu (metadata / 메타데이터) cũng ảnh hưởng.

**“fsck có thể chạy bất kỳ lúc nào.”** Repair filesystem đang mounted có thể nguy hiểm; phải theo hướng dẫn filesystem cụ thể.

Xem thêm: [Filesystem, path, inode và link](./filesystem_paths_inodes_links.md), [Storage và filesystem](../06_resources/storage_filesystems.md), [Backup và khôi phục](../08_operations/backup_restore_disaster_recovery.md).

> **Bàn giao:** Sau **Những hiểu lầm phổ biến**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
