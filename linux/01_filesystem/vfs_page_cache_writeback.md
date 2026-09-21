# VFS, page cache và writeback trong Linux

Các chương trước đã giải thích đường dẫn, inode, bộ mô tả tệp và journaling. Tuy nhiên, để hiểu đầy đủ việc “đọc một file” hoặc “ghi một file” trong Linux thực sự đi qua những lớp nào, cần thêm một tầng trung gian rất quan trọng: **VFS (Virtual File System)** và **page cache**.

VFS giúp kernel cung cấp một giao diện tương đối thống nhất cho ext4, XFS, tmpfs, procfs, NFS và nhiều filesystem khác. Page cache giúp hệ thống dùng RAM để tránh phải truy cập thiết bị lưu trữ ở mọi lần đọc/ghi. Khi ghép hai khái niệm này với cơ chế ghi ngược (writeback), ta có thể giải thích nhiều hiện tượng production như: file đã ghi nhưng chưa thực sự xuống disk, `free` thấp nhưng hệ thống vẫn khỏe, ghi burst nhanh lúc đầu rồi chậm dần, hoặc application latency tăng khi kernel phải flush dirty pages.

## Vì sao cần VFS?

Nếu mỗi ứng dụng phải biết ext4 dùng cấu trúc inode thế nào, XFS tổ chức metadata ra sao hoặc NFS gửi request qua mạng bằng giao thức gì, API thao tác file sẽ cực kỳ phức tạp. Linux giải quyết bằng một lớp trừu tượng gọi là **VFS (Virtual File System / hệ thống tệp ảo)**.

Ứng dụng gọi các lời gọi hệ thống như:

```text
openat()
read()
write()
stat()
close()
```

Kernel nhận yêu cầu rồi đi qua VFS. Sau đó VFS gọi implementation phù hợp của filesystem thật.

Có thể hình dung:

```text
application
   ↓
system call
   ↓
VFS
   ↓
ext4 / XFS / tmpfs / NFS / procfs / ...
   ↓
block layer hoặc network
```

VFS vì vậy không phải một filesystem lưu dữ liệu riêng. Nó là lớp giao diện và đối tượng chung để kernel thao tác nhiều filesystem theo cùng một mô hình.

## Các đối tượng quan trọng trong VFS

Để hiểu VFS, cần phân biệt vài đối tượng khái niệm:

- **superblock** đại diện cho một filesystem đã mount;
- **inode** đại diện metadata của một filesystem object;
- **dentry (directory entry cache)** đại diện quan hệ giữa tên trong thư mục và object;
- **file object** đại diện trạng thái của một file đang được mở bởi process.

Một pathname như:

```text
/opt/app/config/application.yml
```

không được xử lý như một chuỗi nguyên khối. Kernel resolve từng component trong namespace, sử dụng dentry cache khi có thể, kiểm tra mount boundaries và cuối cùng tới inode/object đích.

## Dentry cache và vì sao path lookup có thể nhanh

Nếu mỗi lần `open()` đều phải đọc lại toàn bộ directory metadata từ disk, việc truy cập file sẽ tốn kém. Linux giữ cache cho pathname lookup gọi là **dentry cache (dcache)**.

Điều này nghĩa là lần truy cập thứ hai vào một path thường có thể nhanh hơn vì một phần metadata cần cho việc phân giải tên đã ở RAM.

Nhưng dentry cache không đảm bảo object luôn còn tồn tại. Namespace có thể thay đổi do rename, unlink hoặc mount. Kernel phải duy trì tính hợp lệ của cache theo semantics của filesystem.

## Page cache là gì?

**Page cache** là vùng RAM được kernel dùng để giữ nội dung file-backed pages. Khi process đọc file thông qua buffered I/O, dữ liệu thường được lấy từ page cache nếu đã có; nếu chưa có, kernel đọc từ storage rồi đưa vào page cache.

Luồng đơn giản:

```text
read(fd)
   ↓
page cache có dữ liệu?
   ├─ có  → copy dữ liệu cho process
   └─ chưa → đọc từ storage → đặt vào page cache → trả cho process
```

Do đó RAM trống thấp không phải luôn xấu. Linux chủ động dùng RAM để giảm I/O.

## Page cache và bộ nhớ của process có phải hai thứ tách rời hoàn toàn?

Không. Một file có thể được đọc bằng `read()` hoặc ánh xạ bằng `mmap()`. Trong cả hai trường hợp, page cache có thể đóng vai trò backing cho dữ liệu file-backed.

Với `mmap()`, process nhìn thấy vùng địa chỉ ảo ánh xạ tới file. Khi truy cập một trang chưa có trong RAM, page fault có thể làm kernel đưa trang tương ứng từ file vào page cache rồi ánh xạ vào process.

Đây là lý do database engine, runtime và hệ thống lưu trữ phải hiểu rõ mối quan hệ giữa page cache của OS và cache riêng của ứng dụng.

## Buffered I/O và direct I/O

Phần lớn thao tác file thông thường dùng **buffered I/O**, tức đi qua page cache.

Một số workload có thể dùng **direct I/O** để giảm hoặc tránh page cache cho các I/O nhất định. Database engine đôi khi dùng cách này để tự kiểm soát cache và ordering tốt hơn.

Direct I/O không tự động nhanh hơn. Nó giảm một số lớp cache nhưng yêu cầu alignment và quản lý I/O cẩn thận. Nếu ứng dụng không có chiến lược cache tốt, bỏ page cache có thể làm hiệu năng tệ hơn.

## Ghi file: vì sao `write()` có thể trả về rất nhanh?

Khi ứng dụng gọi:

```text
write(fd, buffer, size)
```

kernel thường có thể copy dữ liệu vào page cache, đánh dấu các trang là **dirty page**, rồi trả success trước khi storage vật lý hoàn thành ghi.

Mental model:

```text
application write()
       ↓
RAM / page cache
       ↓
dirty pages
       ↓
writeback
       ↓
storage
```

Điều này giúp tăng throughput vì ứng dụng không phải chờ mỗi lần write nhỏ xuống thiết bị.

## Dirty page là gì?

Một trang file-backed được gọi là **dirty** khi nội dung trong RAM mới hơn dữ liệu bền vững trên storage.

Có thể quan sát một số chỉ số hệ thống:

```bash
grep -E 'Dirty|Writeback' /proc/meminfo
```

Ví dụ:

```text
Dirty:       120000 kB
Writeback:    16000 kB
```

`Dirty` cho biết lượng trang đang chờ ghi; `Writeback` cho biết lượng đang trong quá trình ghi xuống storage.

Một giá trị lớn không tự động là lỗi. Cần nhìn xu hướng, tốc độ ghi, latency và workload.

## Writeback diễn ra như thế nào?

Kernel có cơ chế nền để ghi dirty pages xuống storage. Việc ghi có thể được kích hoạt bởi:

- tuổi của dirty page;
- tỷ lệ dirty memory vượt ngưỡng;
- `fsync()` hoặc `sync()`;
- áp lực bộ nhớ;
- cơ chế writeback riêng của filesystem.

Các tham số như sau có thể tồn tại qua `sysctl`:

```bash
sysctl vm.dirty_ratio
sysctl vm.dirty_background_ratio
sysctl vm.dirty_expire_centisecs
sysctl vm.dirty_writeback_centisecs
```

Không nên thay đổi các giá trị này theo bài tuning chung trên Internet. Chúng ảnh hưởng cân bằng giữa throughput, latency burst và lượng dữ liệu chưa xuống storage.

## Khi dirty memory quá nhiều thì chuyện gì xảy ra?

Nếu process ghi nhanh hơn storage có thể hấp thụ, dirty pages tăng dần. Đến một mức, kernel có thể làm process ghi bị throttled hoặc phải tham gia writeback.

Triệu chứng có thể là:

```text
lúc đầu write rất nhanh
→ dirty pages tăng
→ storage queue tăng
→ kernel bắt đầu writeback mạnh
→ application latency tăng
```

Đây là một ví dụ quan trọng cho thấy benchmark ngắn có thể gây hiểu nhầm. Một workload ghi trong 5 giây có thể đo chủ yếu tốc độ RAM/page cache, không phản ánh sustained storage throughput.

## `fsync()` thay đổi điều gì?

`fsync(fd)` yêu cầu kernel đồng bộ dữ liệu và metadata cần thiết của file theo semantics của hệ thống xuống storage.

Ứng dụng cần durability như database thường không thể chỉ dựa vào `write()`.

Tuy nhiên `fsync()` có chi phí vì nó đưa latency của storage vào critical path.

Do đó database thường dùng kỹ thuật batching hoặc group commit để nhiều transaction cùng chia sẻ chi phí flush.

## `fdatasync()` và sự khác biệt khái niệm

`fdatasync()` tập trung vào dữ liệu và metadata cần thiết để đọc dữ liệu đúng, trong khi `fsync()` có thể có semantics rộng hơn về metadata tùy filesystem.

Điểm cần nhớ không phải thuộc API chi tiết, mà là: **có nhiều mức guarantee khác nhau giữa “đã copy vào RAM” và “đã bền vững trên storage”**.

## Atomicity, visibility và durability là ba khái niệm khác nhau

Một thao tác có thể:

- atomic về namespace;
- visible ngay cho process khác;
- nhưng chưa durable sau power loss.

Ví dụ `rename()` trong cùng filesystem thường atomic về namespace, nhưng muốn bảo đảm trạng thái tồn tại sau crash có thể cần fsync file và directory theo pattern phù hợp.

Không nên đồng nhất “người đọc khác đã thấy file mới” với “file mới đã chắc chắn được ghi bền vững”.

## Copy-on-write có làm page cache biến mất không?

Không. Filesystem dùng copy-on-write như Btrfs có chiến lược ghi metadata/data khác, nhưng page cache vẫn là một phần quan trọng của Linux I/O stack.

Copy-on-write thay đổi cách blocks được cập nhật và giúp snapshot/checksum ở mức filesystem, nhưng không loại bỏ khái niệm cache, writeback hoặc durability.

## Read-ahead

Khi kernel nhận thấy process đọc tuần tự, nó có thể đọc trước các block kế tiếp vào page cache. Cơ chế này gọi là **read-ahead**.

Điều này làm sequential scan nhanh hơn vì I/O được gom và pipeline trước.

Nhưng random access không hưởng lợi giống vậy. Đây là lý do sequential throughput và random IOPS là hai đặc tính rất khác nhau của storage.

## Readahead quá lớn có thể gây tác dụng ngược

Nếu workload đọc ngẫu nhiên nhưng kernel đoán thành tuần tự, read-ahead có thể kéo vào RAM những dữ liệu không dùng tới, gây cache pollution và I/O thừa.

Tuning chỉ nên làm khi có đo lường cụ thể.

## `drop_caches` và vì sao không nên dùng để “tối ưu” production

Linux cho phép yêu cầu kernel thu hồi một số cache:

```bash
sync
echo 3 | sudo tee /proc/sys/vm/drop_caches
```

Lệnh này đôi khi hữu ích trong benchmark kiểm soát, nhưng không phải cách “giải phóng RAM” định kỳ cho production.

Xóa page cache có thể làm lần đọc tiếp theo phải quay lại storage và tăng latency mạnh.

## Page cache và container

Container chia sẻ host kernel, nên page cache là tài nguyên host-level theo semantics kernel, dù accounting trong cgroup có thể phân bổ chi phí memory theo control group.

Hai container đọc cùng một file backing có thể trong một số tình huống tận dụng cache chung ở kernel layer.

Điều này cũng làm memory accounting phức tạp hơn việc chỉ nhìn RSS của từng process.

## Page cache và Java

Java application thường đọc JAR, config, static resources và log thông qua filesystem. Khi đọc lại dữ liệu, page cache có thể làm I/O nhanh hơn.

Một JVM có heap ổn định nhưng host memory “used” tăng không nhất thiết là leak; page cache có thể tăng do workload đọc file.

Ngược lại, khi memory pressure cao, kernel reclaim page cache và application có thể thấy I/O latency tăng vì cache hit rate giảm.

## Quan sát thực tế

Một bộ công cụ cơ bản:

```bash
free -h
grep -E 'Cached|Dirty|Writeback' /proc/meminfo
vmstat 1
iostat -xz 1
pidstat -d 1
```

Nếu cần xem process đang đọc/ghi file nào:

```bash
sudo lsof -p <PID>
```

Nếu muốn nhìn system call I/O:

```bash
sudo strace -p <PID> -e trace=read,write,pread64,pwrite64,fsync,fdatasync
```

`strace` có overhead, nên chỉ dùng có mục tiêu và trong khoảng thời gian cần thiết.

## Một case production: log burst làm API chậm

Giả sử Java service bình thường nhưng một lỗi upstream gây retry liên tục và tạo log lớn.

Chuỗi nhân quả có thể là:

```text
upstream lỗi
→ retry storm
→ log write rate tăng mạnh
→ dirty pages tăng
→ writeback mạnh
→ storage queue dài
→ fsync hoặc metadata I/O chậm
→ application threads chờ I/O
→ API latency tăng
```

Nếu chỉ nhìn CPU có thể thấy CPU vẫn thấp và kết luận sai rằng server còn khỏe.

Cần correlate log rate, `Dirty`, `iostat`, thread state và application latency.

## Một case khác: deploy xong lần đầu chậm, lần sau nhanh

Sau reboot hoặc deploy sang host mới, page cache còn lạnh. Lần đầu đọc JAR/config/static files phải lấy từ storage. Sau đó các pages ở cache nên lần truy cập kế tiếp nhanh hơn.

Đây là **cache warming** tự nhiên.

Một benchmark cần kiểm soát cache state nếu muốn so storage thay vì đo cache.

## Mô hình tư duy

Có thể hình dung I/O file thông thường như:

```text
pathname
  ↓
VFS / dentry / inode
  ↓
page cache
  ↓
filesystem implementation
  ↓
block layer
  ↓
device / network storage
```

Khi đọc, page cache cố tránh đi xuống các lớp dưới. Khi ghi, page cache cho phép tách thời điểm ứng dụng ghi với thời điểm storage thực sự hoàn thành.

## Những hiểu lầm phổ biến

**“`write()` trả về nghĩa dữ liệu đã nằm trên disk.”** Không nhất thiết; dữ liệu có thể mới ở page cache.

**“RAM dùng cho cache là RAM bị lãng phí.”** Ngược lại, cache giúp giảm I/O và có thể được reclaim.

**“`drop_caches` giúp production nhanh hơn.”** Thường làm mất dữ liệu cache hữu ích và tăng latency lần đọc sau.

**“Benchmark ghi 2 giây phản ánh tốc độ SSD.”** Có thể chủ yếu phản ánh page cache nếu chưa buộc flush.

**“Atomic rename đồng nghĩa dữ liệu durable.”** Atomicity và durability là hai guarantee khác nhau.

## Kết nối kiến thức

Đọc thêm [Journaling, tính nhất quán và mount](./journaling_consistency_mounts.md) để hiểu durability sau crash, [I/O performance](../06_resources/io_performance.md) để hiểu queue/latency, và [Bộ nhớ ảo](../06_resources/memory_virtual_memory.md) để nối page cache với memory reclaim.