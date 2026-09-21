# Block layer, hàng đợi I/O và bộ lập lịch lưu trữ

Khi một ứng dụng ghi dữ liệu xuống tệp, dữ liệu không đi thẳng từ `write()` tới SSD theo một đường duy nhất. Nó đi qua nhiều lớp: page cache, filesystem, block layer, hàng đợi yêu cầu, driver, controller và thiết bị lưu trữ. Vì vậy khi storage chậm, việc chỉ nhìn `iostat` hoặc `df` là chưa đủ; cần hiểu mỗi lớp đang làm gì.

## Từ file I/O tới block I/O

Một đường ghi điển hình:

```text
application
   ↓
write()/pwrite()/fsync()
   ↓
page cache / filesystem
   ↓
block layer
   ↓
request queue
   ↓
device driver
   ↓
controller / storage
```

Filesystem làm việc với file, inode và block logic. Block layer cung cấp abstraction chung cho các thiết bị lưu trữ khối như HDD, SSD, NVMe hoặc virtual disk.

## Tại sao cần block layer?

Nếu mỗi filesystem phải tự biết cách nói chuyện với mọi loại storage controller, hệ thống sẽ rất khó duy trì. Block layer tách hai phía:

- phía trên: filesystem hoặc thành phần phát sinh block I/O;
- phía dưới: driver và thiết bị cụ thể.

Nó còn quản lý hàng đợi, hợp nhất yêu cầu và một số chính sách lập lịch.

## Bio và request

Trong kernel, I/O có thể được biểu diễn bằng các cấu trúc mô tả vùng block cần đọc/ghi. Nhiều thao tác có thể được hợp nhất hoặc xếp thành request trước khi gửi xuống thiết bị.

Mental model:

```text
nhiều thao tác nhỏ
      ↓
block requests
      ↓
queue / merge / dispatch
      ↓
device
```

Điều này giải thích vì sao số system call `write()` không bằng số operation vật lý mà thiết bị thấy.

## Hàng đợi và độ trễ

Mỗi thiết bị chỉ có khả năng xử lý hữu hạn. Khi tốc độ yêu cầu tới vượt tốc độ phục vụ trong thời gian đủ dài, hàng đợi tăng.

Theo trực giác hàng đợi:

```text
arrival rate tăng
    ↓
queue depth tăng
    ↓
waiting time tăng
    ↓
tail latency tăng
```

Đây là lý do storage có thể chưa đạt 100% throughput lý thuyết nhưng latency đã xấu do queueing.

## HDD và SSD khác nhau ở đâu?

HDD có đầu đọc cơ học, nên thứ tự request ảnh hưởng nhiều tới seek time. SSD không có seek cơ học như HDD, nhưng vẫn có controller, flash translation layer, garbage collection và giới hạn song song.

Do đó một I/O scheduler được thiết kế tốt cho HDD chưa chắc tối ưu cho NVMe hiện đại.

## Multi-queue block layer

Linux hiện đại dùng **blk-mq (multi-queue block layer)** để khai thác storage có khả năng song song cao.

Thay vì một queue chung duy nhất, hệ thống có thể có nhiều software queue gắn với CPU và hardware queue phía thiết bị.

```text
CPU0 -> software queue 0 ┐
CPU1 -> software queue 1 ├-> hardware queues -> device
CPU2 -> software queue 2 ┤
CPU3 -> software queue 3 ┘
```

Mục tiêu là giảm contention và tăng khả năng song song trên SSD/NVMe.

## I/O scheduler

Có thể kiểm tra scheduler:

```bash
cat /sys/block/<device>/queue/scheduler
```

Ví dụ:

```text
[mq-deadline] kyber none
```

Tên và scheduler có sẵn phụ thuộc kernel, distribution và thiết bị.

Các scheduler thường cố cân bằng một số mục tiêu như:

- throughput;
- fairness;
- latency;
- starvation avoidance;
- tối ưu pattern request.

Không nên đổi scheduler chỉ vì benchmark của workload khác.

## `none`

Với một số NVMe hiện đại, `none` để block layer can thiệp tối thiểu và dựa nhiều vào khả năng queueing của thiết bị. Điều này không có nghĩa “không có queue”; thiết bị vẫn có hardware queues.

## `mq-deadline`

`mq-deadline` cố hạn chế starvation bằng deadline và vẫn sắp xếp request ở mức phù hợp. Nó có thể hữu ích khi cần latency tương đối ổn định.

## `kyber`

Kyber tập trung kiểm soát latency bằng cách điều tiết số request đang đi qua một số lớp queue. Tính phù hợp phụ thuộc workload và kernel.

## Queue depth

Queue depth cho biết bao nhiêu operation có thể đang chờ hoặc xử lý đồng thời. NVMe thường hỗ trợ queue depth lớn, nhưng “càng lớn càng tốt” là hiểu lầm.

Queue sâu có thể tăng throughput tới một mức, nhưng cũng tăng thời gian chờ của từng request.

Nếu workload nhạy latency, queue quá sâu có thể làm p99 xấu.

## Đọc `iostat` đúng hơn

```bash
iostat -x 1
```

Các trường cụ thể thay đổi theo phiên bản, nhưng thường cần quan tâm:

- `r/s`, `w/s`: số request đọc/ghi mỗi giây;
- throughput đọc/ghi;
- `await`: thời gian trung bình request chờ + xử lý;
- queue size trung bình;
- `%util`: mức bận của thiết bị theo semantics của công cụ.

Không nên diễn giải `%util=100` trên NVMe giống hệt HDD. Thiết bị đa queue có thể xử lý song song nhiều operation.

## `await` và service time

Một request thấy tổng latency gồm thời gian đợi trong queue và thời gian thiết bị thực sự xử lý.

```text
request latency
   = queue wait
   + service time
```

Nếu `await` tăng khi throughput chưa tăng nhiều, có thể queue hoặc storage backend đang có vấn đề.

## I/O size

Hai workload đều 1000 IOPS nhưng hoàn toàn khác nếu một bên dùng 4 KiB và bên kia 1 MiB.

Throughput gần đúng:

```text
throughput ≈ IOPS × average I/O size
```

Ví dụ:

```text
10,000 IOPS × 4 KiB ≈ 39 MiB/s
```

Trong khi:

```text
1,000 IOPS × 1 MiB ≈ 1 GiB/s
```

Vì vậy không thể đánh giá storage chỉ bằng IOPS.

## Random và sequential I/O

Sequential I/O thường dễ tối ưu hơn vì có tính liên tục. Random I/O tạo pattern truy cập phân tán.

Với HDD, khác biệt này rất lớn do seek. Với SSD vẫn có khác biệt vì internal parallelism, write amplification và cache behavior.

Database thường tạo workload có nhiều random access hơn log append tuần tự.

## Read-ahead

Kernel có thể đọc trước dữ liệu dự đoán ứng dụng sắp cần.

```bash
blockdev --getra /dev/<device>
```

Read-ahead tốt cho truy cập tuần tự nhưng có thể lãng phí I/O và cache nếu workload ngẫu nhiên.

## Writeback và dirty throttling

Ứng dụng có thể ghi nhanh vào page cache trong một thời gian. Nếu lượng trang bẩn (dirty pages) tăng quá nhiều, kernel phải tăng tốc writeback hoặc throttle tiến trình tạo dirty data.

Do đó một ứng dụng có thể đột nhiên thấy `write()` chậm dù trước đó rất nhanh. Lý do không nhất thiết thiết bị vừa hỏng; có thể ứng dụng đã chạm ngưỡng dirty throttling.

Quan sát:

```bash
grep -E 'Dirty|Writeback' /proc/meminfo
```

Các tham số liên quan:

```bash
sysctl vm.dirty_background_ratio
sysctl vm.dirty_ratio
```

Trên một số hệ thống có thể dùng các biến dạng byte thay vì ratio.

Không nên chỉnh các tham số này nếu chưa hiểu workload.

## `fsync()` và latency spike

Một hệ thống ghi log có thể thấy throughput cao vì write đi vào page cache, nhưng khi database hoặc application gọi `fsync()`, nó phải chờ durability contract mạnh hơn.

Nếu storage backend có tail latency cao, `fsync` latency có thể trực tiếp xuất hiện thành transaction latency.

Đây là lý do database benchmark cần quan tâm durability mode, không chỉ số transaction mỗi giây.

## I/O scheduler không thay thế application design

Nếu application phát hàng nghìn synchronous small writes, scheduler không thể biến workload đó thành một workload lý tưởng hoàn toàn. Batch, buffering và write-ahead log ở tầng ứng dụng có thể có ảnh hưởng lớn hơn.

## Direct I/O

Một số database dùng **direct I/O** để giảm hoặc tránh page cache của kernel cho dữ liệu chính, vì database tự quản lý cache riêng.

Điều này tránh double caching nhưng làm application chịu trách nhiệm nhiều hơn về I/O pattern và alignment.

Không nên suy ra rằng direct I/O luôn nhanh hơn buffered I/O.

## Async I/O và io_uring

Synchronous I/O khiến thread có thể chờ operation hoàn thành. Linux cung cấp nhiều mô hình bất đồng bộ. `io_uring` là một interface hiện đại giúp submit/completion I/O với overhead thấp hơn trong nhiều use case.

Mental model:

```text
submit nhiều operation
       ↓
kernel/device xử lý song song
       ↓
completion events
       ↓
application nhận kết quả
```

Điều này đặc biệt hữu ích khi workload cần concurrency cao mà không muốn một thread blocking cho mỗi operation.

## NVMe

NVMe được thiết kế cho storage flash tốc độ cao với nhiều queue và queue depth lớn. Nó giảm nhiều giới hạn từ giao thức storage cũ hơn.

Kiểm tra thiết bị:

```bash
lsblk -o NAME,TYPE,SIZE,ROTA,MODEL
```

`ROTA=0` thường gợi ý thiết bị không quay cơ học.

Nếu có công cụ NVMe:

```bash
nvme list
```

## Virtual disk và cloud storage

Trong VM/cloud, `/dev/vda` hay `/dev/nvme...` không cho bạn toàn bộ sự thật về phần cứng cuối cùng. Phía dưới có thể là network-attached storage, distributed block storage hoặc lớp giới hạn IOPS của cloud provider.

Do đó guest OS có thể thấy queueing mà nguyên nhân thật nằm ngoài VM.

## Cgroup I/O control

Cgroup v2 có thể giới hạn hoặc ưu tiên I/O cho workload.

Các file có thể gồm:

```text
io.stat
io.max
io.weight
```

Nếu container chậm storage dù host còn khả năng, cần kiểm tra policy cgroup.

## Khi `iowait` cao

`iowait` không phải phần trăm thời gian “ổ đĩa bận”. Nó là cách accounting CPU idle trong một số tình huống có outstanding I/O.

Một hệ thống có storage bottleneck vẫn có thể có iowait không quá cao nếu CPU bận làm việc khác. Ngược lại iowait cao không tự động chỉ ra thiết bị nào có vấn đề.

## Quy trình điều tra storage latency

Một trình tự hữu ích:

```text
1. xác nhận symptom ở ứng dụng
2. kiểm tra latency/throughput I/O ở host
3. xác định device/mount thực tế
4. kiểm tra queue và error kernel
5. đối chiếu workload khác trên cùng device
6. kiểm tra cgroup/VM/cloud limit
7. kiểm tra filesystem và durability pattern
```

Câu lệnh thường dùng:

```bash
iostat -x 1
pidstat -d 1
lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS
findmnt
journalctl -k | grep -i -E 'error|timeout|reset|nvme|blk'
```

## Mô hình tư duy

Storage performance là bài toán pipeline và queue:

```text
application rate
    ↓
page cache / filesystem
    ↓
block queue
    ↓
device queue
    ↓
storage service rate
```

Bottleneck xuất hiện khi tốc độ đưa việc vào vượt khả năng phục vụ hoặc khi tail latency phía dưới tăng.

## Những hiểu lầm phổ biến

**“SSD không cần I/O scheduler.”** Block layer và queueing vẫn tồn tại; scheduler phù hợp tùy thiết bị và workload.

**“Queue depth lớn luôn tốt.”** Nó có thể tăng throughput nhưng cũng tăng latency.

**“`%util=100` luôn nghĩa ổ đĩa đã hết khả năng.”** Cách diễn giải phụ thuộc thiết bị, đặc biệt với multi-queue NVMe.

**“`write()` nhanh nghĩa dữ liệu đã xuống disk.”** Buffered I/O có thể chỉ mới vào page cache.

**“iowait cao chính là phần trăm disk utilization.”** Hai metric mô tả khái niệm khác nhau.

## Kết nối kiến thức

Đọc cùng [VFS, page cache và writeback](../01_filesystem/vfs_page_cache_writeback.md), [I/O performance](./io_performance.md) và [journaling/consistency](../01_filesystem/journaling_consistency_mounts.md). Với database, các cơ chế này quyết định trực tiếp latency của WAL, checkpoint và transaction commit.