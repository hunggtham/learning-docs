# Journaling, tính nhất quán và cơ chế mount của filesystem

Một hệ thống tệp (filesystem) không chỉ cần lưu dữ liệu; nó còn phải giữ cấu trúc metadata nhất quán khi hệ thống mất điện, kernel panic hoặc storage trả lỗi giữa chừng. Nếu một thao tác cập nhật cần sửa nhiều nơi nhưng chỉ hoàn tất một phần, filesystem có thể rơi vào trạng thái khó hiểu: block đã được đánh dấu sử dụng nhưng directory entry chưa tồn tại, hoặc inode đã đổi nhưng bitmap chưa khớp.

Đó là lý do cần hiểu **tính nhất quán (consistency)** và **nhật ký giao dịch (journaling)**.

## Vấn đề cơ bản: một thao tác logic có thể cần nhiều thao tác vật lý

Giả sử tạo file mới. Ở mức người dùng chỉ có:

```bash
touch report.txt
```

Nhưng filesystem có thể phải:

1. cấp phát inode;
2. cập nhật inode bitmap;
3. tạo directory entry;
4. cập nhật metadata của thư mục;
5. có thể cấp data block nếu file có nội dung;
6. ghi các thay đổi xuống storage.

Nếu máy mất điện ở giữa chuỗi này, một phần đã xuống disk còn phần khác chưa xuống.

Filesystem phải có cách phục hồi để cấu trúc vẫn hợp lệ.

## Journaling giải quyết điều gì?

**Journaling** ghi thông tin về các thay đổi dự định thực hiện vào một vùng nhật ký trước hoặc trong quá trình áp dụng lên cấu trúc chính.

Sau crash, filesystem có thể kiểm tra journal để biết transaction nào hoàn tất và transaction nào cần replay/rollback theo semantics của filesystem.

Điểm quan trọng là journaling chủ yếu giúp **tính nhất quán metadata** và thời gian phục hồi. Nó không có nghĩa mọi byte application vừa ghi đều chắc chắn đã bền vững trên storage.

## Metadata journaling và data journaling

Các filesystem có thể journal metadata và/hoặc data theo những chế độ khác nhau.

Ở ext4, các chế độ thường được nhắc đến gồm:

- `data=ordered` — metadata được journal, data được ghi trước khi metadata liên quan được commit theo ordering nhất định;
- `data=writeback` — ordering data yếu hơn;
- `data=journal` — cả data và metadata đi qua journal, chi phí cao hơn.

Không nên đổi mount mode chỉ vì thấy benchmark trên internet. Trade-off liên quan durability, throughput, latency và workload.

## `write()` không đồng nghĩa dữ liệu đã bền vững

Application gọi:

```text
write(fd, data, ...)
```

Kernel có thể nhận dữ liệu vào page cache và trả success trước khi storage vật lý hoàn tất ghi.

Để yêu cầu đồng bộ mạnh hơn, application có thể dùng `fsync()` hoặc các cơ chế tương đương.

Điều này đặc biệt quan trọng với database.

> Database không thể chỉ tin rằng “system call write thành công” đồng nghĩa transaction đã an toàn trước power loss.

Các hệ quản trị cơ sở dữ liệu thường có write-ahead log và cơ chế fsync riêng để đạt durability theo ACID.

## `sync`, `fsync` và flush

Command:

```bash
sync
```

đề nghị kernel flush dữ liệu filesystem đang chờ ra storage.

Trong code, `fsync(fd)` yêu cầu đồng bộ dữ liệu/metadata liên quan descriptor theo semantics hệ thống.

Nhưng durability cuối cùng còn phụ thuộc storage controller, drive cache, hypervisor và cloud storage implementation.

Do đó “đã fsync” là một guarantee mạnh ở OS interface, nhưng phần cứng/storage stack vẫn phải thực hiện đúng contract.

## Atomic rename

Pattern rất quan trọng trong production là ghi file mới rồi rename:

```bash
printf '%s\n' 'new-config' > config.yml.tmp
mv config.yml.tmp config.yml
```

Rename trong cùng filesystem thường là atomic ở namespace level: observer thấy tên cũ hoặc tên mới, thay vì thấy file bị ghi dở giữa chừng.

Pattern an toàn hơn cho nhiều tình huống:

```text
write temporary file
        ↓
fsync temporary file khi cần durability
        ↓
rename temporary -> target
        ↓
fsync directory khi durability của directory entry là yêu cầu nghiêm ngặt
```

Application updater, package manager và config deployment thường tận dụng ý tưởng này.

## Tại sao cross-filesystem rename không giống nhau?

```bash
mv /tmp/a /data/a
```

Nếu `/tmp` và `/data` nằm trên hai filesystem khác nhau, kernel không thể chỉ đổi directory entry cùng inode namespace. `mv` có thể phải copy rồi unlink nguồn.

Do đó thao tác không còn có cùng tính atomic như rename nội bộ filesystem.

Kiểm tra:

```bash
findmnt -T /tmp/a
findmnt -T /data
```

## Mount point và namespace

Khi filesystem được mount vào `/data`, nội dung directory `/data` trước đó bị che bởi mount mới trong namespace hiện tại.

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

Điều này giải thích một số tình huống “file biến mất sau mount” nhưng thực ra dữ liệu cũ vẫn nằm ở filesystem bên dưới.

## Vì sao `umount` báo busy?

Kernel không thể unmount an toàn nếu resource vẫn đang được sử dụng.

Nguyên nhân có thể gồm:

- process có current working directory trong mount;
- file descriptor đang mở;
- filesystem con được mount bên dưới;
- memory-mapped file vẫn tham chiếu.

Điều tra:

```bash
findmnt /data
sudo lsof +f -- /data
sudo fuser -vm /data
```

Không nên dùng forced/lazy unmount như phản xạ đầu tiên trên production.

## Bind mount

Bind mount cho phép một phần cây filesystem xuất hiện ở vị trí khác:

```bash
sudo mount --bind /opt/app/data /srv/data
```

Hai pathname khác nhau có thể dẫn đến cùng underlying objects.

Containers sử dụng mount namespace và bind mount rất nhiều để tạo filesystem view riêng.

## Read-only mount

Mount có thể được đặt chỉ đọc:

```bash
mount -o remount,ro /mountpoint
```

Một process dù có UID root hoặc file mode `777` vẫn không thể ghi theo cách bình thường nếu filesystem được mount read-only.

Đây là ví dụ rõ rằng permission bits chỉ là một layer trong quyết định access.

## `noexec`, `nosuid`, `nodev`

Mount options có thể thay đổi policy:

- `noexec` hạn chế thực thi binary theo semantics mount;
- `nosuid` vô hiệu hóa tác dụng setuid/setgid trong nhiều trường hợp;
- `nodev` không diễn giải device nodes trên filesystem đó.

Các option này thường dùng trong hardening, nhưng có thể phá application nếu áp dụng mà không hiểu nhu cầu.

## ext4, XFS và lựa chọn filesystem

Không có filesystem “tốt nhất” cho mọi workload.

ext4 phổ biến, ổn định và dễ dùng. XFS mạnh ở scale lớn và parallel I/O trong nhiều workload. Btrfs/ZFS-style systems cung cấp các tính năng như copy-on-write, snapshot hoặc checksum với trade-off khác.

Lựa chọn nên dựa trên:

- workload;
- distribution support;
- operational expertise;
- backup/restore strategy;
- performance characteristics;
- feature requirements.

## Filesystem check

Một số filesystem có tool kiểm tra/repair như `fsck`, `xfs_repair`.

Không nên chạy repair tool tùy tiện trên mounted production filesystem.

Ví dụ ext filesystem:

```bash
sudo fsck /dev/sdXN
```

thường yêu cầu filesystem unmounted hoặc boot vào maintenance context phù hợp.

Trước repair phải hiểu storage topology và có backup nếu có thể.

## Crash consistency không bằng application consistency

Filesystem có thể hoàn toàn nhất quán sau crash nhưng application data vẫn sai logic.

Ví dụ:

```text
account A đã trừ tiền
account B chưa cộng tiền
```

Hai file/database pages đều structurally valid, nhưng business transaction incomplete.

Đó là lý do database transaction layer tồn tại trên filesystem layer.

Filesystem bảo vệ cấu trúc lưu trữ; database bảo vệ invariants cấp dữ liệu.

## Mối liên hệ với container image

Layered container filesystems thường dùng copy-on-write (CoW). Khi file trong lower image layer bị sửa, runtime có thể copy dữ liệu vào writable layer.

Điều này có thể làm I/O behavior khác host filesystem trực tiếp, đặc biệt với database workload. Vì vậy database persistent data thường được đặt trên volume riêng thay vì writable container layer.

## Mô hình tư duy

Có thể hình dung durability stack:

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

Một lời gọi ghi chỉ đi qua từng layer theo contract tương ứng. Khi đánh giá “dữ liệu đã an toàn chưa?”, phải hỏi an toàn tới layer nào.

## Những hiểu lầm phổ biến

**“Filesystem có journal thì không thể mất dữ liệu.”** Journal chủ yếu giúp consistency; durability của application còn phụ thuộc flush/fsync và storage stack.

**“`mv` luôn atomic.”** Rename cùng filesystem có semantics mạnh; cross-filesystem `mv` có thể trở thành copy + unlink.

**“Permission đúng thì chắc chắn ghi được.”** Read-only mount hoặc security policy vẫn có thể chặn.

**“`df` đầy là do file visible.”** Deleted-open files, reserved blocks và metadata cũng ảnh hưởng.

**“fsck có thể chạy bất kỳ lúc nào.”** Repair filesystem đang mounted có thể nguy hiểm; phải theo hướng dẫn filesystem cụ thể.

Xem thêm: [Filesystem, path, inode và link](./filesystem_paths_inodes_links.md), [Storage và filesystem](../06_resources/storage_filesystems.md), [Backup và khôi phục](../08_operations/backup_restore_disaster_recovery.md).