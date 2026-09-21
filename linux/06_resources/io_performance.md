# I/O Performance, Latency và Throughput trên Linux

Khi ứng dụng chậm, CPU và memory thường được kiểm tra trước, nhưng nhiều hệ thống backend thực tế bị giới hạn bởi I/O: disk, network storage, database volume hoặc filesystem writeback. “Disk còn trống” không đồng nghĩa storage đang khỏe. Capacity và performance là hai câu hỏi khác nhau.

Chương này tập trung vào cách suy luận về I/O trên Linux: dữ liệu đi qua những lớp nào, latency và throughput khác nhau ra sao, queue hình thành thế nào và dùng `iostat`, `pidstat`, `vmstat` để đọc bằng chứng thay vì đoán.

## I/O là gì trong ngữ cảnh Linux?

I/O (Input/Output) là việc chương trình trao đổi dữ liệu với tài nguyên bên ngoài CPU core, chẳng hạn filesystem, block device, socket hoặc terminal.

Với storage, đường đi đơn giản hóa có thể là:

```text
application
→ system call
→ page cache / filesystem
→ block layer
→ device driver
→ disk / SSD / virtual volume
```

Trong cloud, phía dưới “disk” còn có thể là network storage hoặc hypervisor layer.

Vì có nhiều lớp đệm và queue, thời gian một `write()` trả về không nhất thiết là thời gian byte đã được ghi bền vững xuống thiết bị vật lý.

## Latency, throughput và IOPS

Ba khái niệm thường bị trộn lẫn.

**Latency** là thời gian hoàn thành một operation. Nếu một read mất 5 ms, đó là latency của operation đó.

**Throughput** là lượng dữ liệu xử lý theo thời gian, ví dụ 300 MiB/s.

**IOPS** là số I/O operations mỗi giây.

Một workload đọc file lớn tuần tự có thể cần throughput cao nhưng không cần IOPS cực lớn. Database random access có thể nhạy với latency và IOPS hơn.

Không có một metric duy nhất đại diện cho “disk nhanh”.

## Sequential và random I/O

Sequential I/O truy cập các block gần nhau theo thứ tự, thường tận dụng tốt readahead và đặc tính thiết bị. Random I/O truy cập nhiều vị trí rời rạc, có thể tạo nhiều operations nhỏ.

SSD giảm mạnh penalty random access so với HDD, nhưng queue, controller, network storage và filesystem vẫn tạo latency.

Khi performance test, cần biết pattern thật của workload thay vì chỉ nhìn benchmark copy một file lớn.

## Page cache làm việc ở đâu?

Linux dùng RAM làm page cache. Read có thể được phục vụ từ cache mà không chạm thiết bị. Write cũng có thể đi vào page cache trước rồi kernel ghi xuống storage sau.

Do đó một benchmark ngắn có thể đo chủ yếu RAM/cache thay vì device performance.

Kiểm tra memory và writeback context bằng:

```bash
free -h
vmstat 1
```

Không nên “drop cache” trên production chỉ để benchmark nếu chưa hiểu tác động.

## `iostat`

Tool `iostat` thường nằm trong package `sysstat`:

```bash
iostat -xz 1 10
```

`-x` hiển thị extended statistics, `-z` bỏ device không hoạt động, còn `1 10` lấy mẫu mỗi giây trong 10 lần.

Các field thay đổi theo phiên bản nhưng thường có các nhóm ý nghĩa như số read/write operation, throughput, average request size, queue depth, latency và utilization.

Điều quan trọng không phải học thuộc threshold. Một NVMe có thể xử lý concurrency rất khác một network volume. Hãy so với baseline của chính workload.

## `await`

Trên nhiều phiên bản `iostat`, `await` biểu thị thời gian trung bình I/O request trải qua trong hệ thống block device, thường gồm cả queue và service time.

Nếu `await` tăng mạnh đồng thời application latency tăng, storage trở thành hypothesis đáng kiểm tra hơn.

Tuy nhiên average có thể che tail latency. Một vài request cực chậm có thể gây timeout dù trung bình nhìn vẫn ổn.

## `%util` không luôn có nghĩa “100% là hết khả năng”

Với HDD truyền thống, utilization cao thường là tín hiệu saturation hữu ích. Với modern devices có parallel queues, NVMe hoặc virtual storage, diễn giải `%util` đơn giản như “phần trăm công suất” có thể sai.

Hãy kết hợp queue, latency, throughput và workload behavior thay vì kết luận từ `%util` duy nhất.

## Queueing

Khi request tới nhanh hơn tốc độ service trong đủ lâu, queue tăng. Khi queue tăng, latency tăng dù thiết bị vẫn xử lý cùng throughput.

Đây là cùng mô hình với thread pool, database connection pool và CPU runnable queue.

```text
arrival rate > service capacity
→ queue tăng
→ waiting time tăng
→ latency tăng
→ timeout/retry
→ có thể tạo thêm load
```

Retry không kiểm soát có thể làm I/O bottleneck tệ hơn bằng cách tạo thêm work.

## `vmstat` và I/O

```bash
vmstat 1 10
```

Các field `bi` và `bo` phản ánh block input/output theo đơn vị phụ thuộc implementation. `wa` thường biểu diễn CPU idle time trong khi chờ I/O theo accounting của Linux.

`wa` cao là dấu hiệu cần điều tra I/O, nhưng `wa` thấp không chứng minh storage luôn khỏe. Application có thể blocked theo cách không hiện rõ trong metric này hoặc bottleneck nằm ở remote network storage/database.

## Tìm process tạo I/O

`pidstat` có thể xem I/O theo process:

```bash
pidstat -d 1
```

Hoặc theo PID:

```bash
pidstat -d -p 1234 1
```

Điều này trả lời câu hỏi “device đang bận” từ góc process nào đang tạo read/write.

`iotop` cũng hữu ích nếu có:

```bash
sudo iotop
```

Nhưng tool availability và permission phụ thuộc distro/kernel.

## File descriptor và I/O path

Nếu cần biết process đang mở file nào:

```bash
sudo lsof -p 1234
```

Hoặc:

```bash
ls -l /proc/1234/fd
```

Kết hợp process I/O rate với file descriptors giúp nối “PID nào ghi nhiều” với “nó đang ghi vào file/device nào”.

## Sync, flush và durability

Application có thể ghi vào cache nhưng chưa chắc dữ liệu đã durable. `fsync()` yêu cầu kernel đồng bộ dữ liệu cần thiết xuống storage theo semantics của filesystem/device.

Database engine rất quan tâm vấn đề này vì transaction commit cần durability. Storage có cache hoặc virtual layer không honoring flush đúng cách có thể phá giả định của database.

Không nên dùng `sync` như một “tối ưu performance”; nó là operation thúc đẩy writeback và có thể tạo I/O burst.

## Direct I/O

Một số database hoặc workload dùng direct I/O để giảm hoặc tránh page cache cho dữ liệu cụ thể. Điều này không tự động nhanh hơn. Nó chuyển trách nhiệm caching/alignment sang application và phù hợp với workload có buffer manager riêng.

Database thường là ví dụ điển hình vì engine đã có cache pages riêng.

## Read-ahead

Kernel có thể đọc trước block tiếp theo khi phát hiện sequential access. Điều này cải thiện throughput cho scan tuần tự nhưng không giúp nhiều với random access.

Đây là một lý do cùng storage có thể cho performance rất khác giữa backup file lớn và database random query.

## I/O scheduler

Linux block layer có I/O schedulers khác nhau tùy kernel/device. Với modern SSD/NVMe, lựa chọn mặc định của distro thường đã được tối ưu hợp lý.

Không đổi scheduler production theo một bài blog chung chung. Trước tiên cần benchmark đúng workload, hiểu device type và có rollback plan.

## Network storage

NFS, EBS-like volumes, SAN hoặc distributed filesystem thêm network và remote service vào I/O path.

Khi local `iostat` không giải thích đủ, cần kiểm tra network latency, provider limits, burst credits, throughput caps hoặc server-side storage metrics.

Một path `/data` nhìn như local filesystem không có nghĩa dữ liệu nằm trên local disk.

```bash
findmnt /data
```

luôn hữu ích để biết source/fstype.

## Java backend và I/O

Java API có thể high latency với CPU thấp nếu threads đang block ở JDBC, file I/O hoặc network.

Thread dump có thể cho thấy nhiều threads ở native/socket/file read. Linux tools sau đó giúp phân biệt local storage, TCP dependency hay resource limit.

Một flow thực tế:

```bash
jcmd <PID> Thread.print > /tmp/thread.txt
pidstat -d -p <PID> 1
iostat -xz 1 10
ss -antp
```

Không nên nhìn từng tool riêng; cần nối thread state với OS resource state.

## Benchmark bằng `fio`

`fio` là công cụ mạnh để benchmark storage với pattern kiểm soát. Nhưng benchmark sai có thể gây tải lớn hoặc làm đầy disk.

Không chạy destructive `fio` job trên production volume khi chưa hiểu file/device target. Benchmark nên dùng test file/dedicated environment và workload pattern gần thực tế.

## Phân biệt capacity incident và performance incident

Capacity incident:

```bash
df -h
df -i
du -xhd1 /var
```

Performance incident:

```bash
iostat -xz 1 10
pidstat -d 1
vmstat 1 10
```

Hai nhóm liên quan nhưng không giống nhau. Disk 40% dung lượng vẫn có thể latency rất cao.

## Mô hình tư duy (Mental Model)

Khi nghi I/O bottleneck, hãy hỏi theo chuỗi:

```text
application đang chờ gì?
→ process nào tạo I/O?
→ file/mount/device nào?
→ queue và latency trên device ra sao?
→ device local hay remote?
→ workload là random hay sequential?
→ bottleneck là capacity, latency, IOPS hay throughput?
```

Mỗi câu hỏi thu hẹp một layer.

## Những hiểu lầm phổ biến

**“Disk chưa đầy thì disk không phải bottleneck.”** Capacity không phản ánh latency/IOPS.

**“`%util=100` luôn có nghĩa device đạt 100% công suất.”** Với modern parallel devices, cách hiểu này có thể quá đơn giản.

**“CPU iowait cao nghĩa CPU bị lỗi.”** CPU đang có thời gian chờ liên quan I/O; cần tìm nguồn I/O.

**“Write xong là dữ liệu đã nằm bền vững trên disk.”** Buffering và cache có nhiều lớp; durability cần semantics như `fsync`.

**“Benchmark copy file là đại diện database workload.”** Access pattern có thể hoàn toàn khác.

## Kết nối kiến thức

Chương này mở rộng [Storage và Filesystems](./storage_filesystems.md), liên kết với [Memory](./memory_virtual_memory.md) qua page cache, [CPU và Scheduling](./cpu_scheduling_performance.md) qua waiting/queueing, và [Production Troubleshooting](../09_production/production_troubleshooting.md).