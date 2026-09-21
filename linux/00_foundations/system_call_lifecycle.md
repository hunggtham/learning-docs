# Vòng đời lời gọi hệ thống: từ user space vào kernel và quay trở lại

Lời gọi hệ thống (system call) là một trong những ranh giới quan trọng nhất của Linux. Ứng dụng không trực tiếp đọc đĩa, tạo socket hay ánh xạ bộ nhớ vật lý. Nó yêu cầu kernel thực hiện những thao tác đó thông qua một giao diện được kiểm soát. Vì vậy muốn hiểu Linux sâu, cần hiểu không chỉ tên các system call mà còn cả **vòng đời của một lời gọi từ user space vào kernel rồi quay lại**.

## Vì sao cần ranh giới system call?

User space và kernel space có mức đặc quyền khác nhau. Mã chạy trong user space không được phép tự ý truy cập bộ nhớ kernel, cấu hình thiết bị hay thao tác trực tiếp với bảng trang. Nếu cho phép điều đó, một lỗi nhỏ trong ứng dụng có thể phá hỏng toàn bộ hệ thống.

System call tạo ra một cổng giao tiếp có kiểm soát:

```text
application
    ↓
libc / runtime wrapper
    ↓
system call entry
    ↓
kernel validation + policy + implementation
    ↓
return value / errno
    ↓
application
```

Kernel nhận yêu cầu, kiểm tra đối số, quyền, trạng thái tài nguyên và sau đó mới thực hiện thao tác.

## Wrapper của thư viện khác system call như thế nào?

Khi chương trình C gọi:

```c
open("/tmp/a.txt", O_RDONLY);
```

hàm `open()` thường là wrapper trong libc. Wrapper này có thể chuẩn hóa đối số, chọn system call phù hợp như `openat()` và chuyển mã lỗi từ giá trị trả về ở kernel thành `errno` ở user space.

Vì vậy **library call** và **system call** không phải luôn là một-một.

Có hàm thư viện không cần system call, ví dụ một số thao tác chuỗi. Ngược lại một hàm thư viện có thể gọi nhiều system call tùy tình huống.

Quan sát bằng:

```bash
strace -e openat,read,close cat /etc/hostname
```

## Điều gì xảy ra khi CPU đi vào kernel?

Chi tiết phụ thuộc kiến trúc CPU, nhưng ý tưởng chung là CPU chuyển từ chế độ ít đặc quyền sang chế độ đặc quyền cao hơn thông qua cơ chế entry được thiết kế cho system call.

Kernel cần biết:

- số hiệu system call;
- các đối số;
- ngữ cảnh tiến trình hiện tại;
- nơi trả kết quả về user space.

Trên x86-64, các thanh ghi được dùng để truyền số system call và đối số theo ABI đã định nghĩa. Ứng dụng bình thường không nên viết logic phụ thuộc trực tiếp vào chi tiết này nếu libc/runtime đã che giấu nó.

## System call không đồng nghĩa context switch

Đây là một hiểu lầm rất phổ biến.

Khi thread gọi system call, CPU chuyển từ user mode sang kernel mode, nhưng **thread vẫn có thể là cùng thread đang chạy**. Đây là thay đổi mức đặc quyền, không tự động là context switch sang thread khác.

Context switch chỉ xảy ra khi scheduler quyết định đổi task đang chạy, ví dụ vì thread bị block hoặc hết time slice.

Ví dụ:

```text
read() dữ liệu đã có sẵn trong page cache
→ vào kernel
→ copy dữ liệu
→ quay lại user space
→ có thể không cần chuyển sang task khác
```

Ngược lại:

```text
read() cần chờ disk
→ vào kernel
→ task chuyển sang sleep
→ scheduler chạy task khác
→ I/O hoàn tất
→ task được đánh thức
→ sau đó mới tiếp tục
```

## Blocking và sleeping trong system call

Một system call có thể hoàn tất ngay hoặc phải chờ tài nguyên.

Ví dụ `read()` trên file thường có thể trả nhanh nếu dữ liệu đã ở page cache. Nhưng `read()` trên socket không có dữ liệu có thể làm thread ngủ nếu socket ở blocking mode.

Kernel thường không “quay CPU vòng tròn” vô ích. Task được đưa vào trạng thái chờ, rời run queue và chỉ được đánh thức khi điều kiện cần thiết xảy ra.

Đây là nền tảng để hiểu tại sao một tiến trình có hàng trăm thread nhưng CPU không nhất thiết 100%.

## Copy dữ liệu giữa user space và kernel

Kernel không thể tin địa chỉ bộ nhớ do user space cung cấp. Một con trỏ có thể không hợp lệ hoặc trỏ tới vùng không được phép.

Các cơ chế như `copy_from_user()` và `copy_to_user()` tồn tại để kiểm tra và sao chép dữ liệu qua ranh giới này theo cách an toàn.

Đây là lý do một system call có thể thất bại với `EFAULT` khi vùng nhớ người dùng không hợp lệ.

## `errno` thực sự đến từ đâu?

Kernel thường trả mã lỗi âm theo quy ước nội bộ. Wrapper ở libc chuyển trạng thái đó thành:

```c
-1
```

và đặt biến thread-local `errno` tương ứng.

Ví dụ:

```c
int fd = open("/missing", O_RDONLY);
if (fd == -1) {
    perror("open");
}
```

`perror()` đọc `errno` và in thông báo dễ hiểu hơn.

Trong `strace` có thể thấy trực tiếp:

```text
openat(..., "/missing", ...) = -1 ENOENT (No such file or directory)
```

## System call table và ABI

Kernel có bảng ánh xạ số system call tới hàm xử lý tương ứng. ABI của system call cần ổn định vì user-space binary đã biên dịch phải tiếp tục chạy qua nhiều phiên bản kernel.

Điều này giải thích tại sao Linux rất thận trọng với backward compatibility ở ranh giới user space/kernel.

Một application binary cũ có thể tiếp tục chạy trên kernel mới miễn ABI cần thiết vẫn được hỗ trợ, dù implementation nội bộ kernel đã thay đổi nhiều.

## `vDSO`: khi user space tránh system call thật

Một số thao tác như đọc thời gian được gọi rất thường xuyên. Nếu mỗi lần đều phải chuyển vào kernel, chi phí sẽ đáng kể.

Linux có thể cung cấp **virtual dynamic shared object (vDSO)** ánh xạ một số logic và dữ liệu vào user space. Nhờ đó hàm như `clock_gettime()` trong nhiều trường hợp có thể lấy dữ liệu mà không cần system call thật.

Có thể quan sát mapping:

```bash
cat /proc/self/maps | grep vdso
```

Điểm quan trọng: không phải mọi API trông giống system API đều nhất thiết gây mode transition.

## Chi phí của system call

System call có chi phí do:

- chuyển privilege level;
- kiểm tra đối số;
- policy/security checks;
- cache/TLB effects;
- copy dữ liệu giữa user/kernel;
- có thể block hoặc gây scheduling.

Nhưng không nên suy diễn rằng “system call luôn chậm”. Chi phí thật phụ thuộc loại operation và workload.

Một `getpid()` hoặc `clock_gettime()` khác hoàn toàn `fsync()` lên storage chậm.

## Batch và amortization

Vì ranh giới kernel có overhead, nhiều API cố giảm số lần system call hoặc gom nhiều thao tác.

Ví dụ:

- buffered I/O gom nhiều lần ghi nhỏ;
- `readv()`/`writev()` xử lý nhiều buffer;
- `sendmmsg()`/`recvmmsg()` xử lý nhiều message;
- `io_uring` giảm một số vòng submit/completion theo mô hình queue.

Tuy nhiên tối ưu kiểu này chỉ có ý nghĩa khi profiling cho thấy system call overhead thực sự là bottleneck.

## System call và bảo mật

Ranh giới system call là nơi kernel áp dụng nhiều kiểm tra:

```text
credentials
+ file permission / ACL
+ capabilities
+ LSM như SELinux/AppArmor
+ seccomp
+ namespace/cgroup context
→ allow hoặc deny
```

Seccomp có thể giới hạn tập system call mà tiến trình được phép thực hiện. Container runtime thường dùng cơ chế này để giảm bề mặt tấn công.

## Debug bằng `strace`

`strace` quan sát system call nên rất mạnh khi ứng dụng “nói ít hơn những gì kernel thấy”.

Ví dụ chương trình treo:

```bash
sudo strace -tt -T -p <PID>
```

Nếu liên tục thấy:

```text
futex(...)
```

thì thread có thể đang chờ synchronization.

Nếu thấy:

```text
connect(...)
```

mất nhiều giây rồi timeout, trọng tâm điều tra chuyển sang network/dependency.

Nếu thấy lặp:

```text
openat(..., "/missing/config", ...) = -1 ENOENT
```

thì vấn đề có thể đơn giản là path/config.

## `seccomp` và system call surface

Một tiến trình có thể bị chặn system call dù UID và file permission có vẻ đúng. Seccomp filter có thể trả lỗi hoặc giết task tùy policy.

Container thường áp default seccomp profile. Vì vậy tình huống “binary chạy trên host nhưng không chạy trong container” có thể liên quan system call policy, không chỉ filesystem.

## Signal có thể ngắt system call

Một system call đang block có thể bị signal làm gián đoạn. Một số lời gọi trả `EINTR`, một số có thể được tự động restart tùy signal handler và flags như `SA_RESTART`.

Đây là lý do code hệ thống cần xử lý retry đúng cách thay vì giả định mọi `read()` hoặc `wait()` chỉ thất bại vì lỗi vĩnh viễn.

## System call cancellation và timeout

Nhiều system call blocking không có timeout nội tại. Ứng dụng thường kết hợp non-blocking mode, `poll`/`epoll`, timer hoặc API tầng cao để tránh block vô hạn.

Ví dụ socket có thể dùng:

```c
setsockopt(..., SO_RCVTIMEO, ...)
```

hoặc application quản lý timeout ở event loop.

## Mô hình tư duy (Mental Model)

Hãy coi system call như một **request có hợp đồng rõ ràng gửi tới kernel**:

```text
user-space intent
    ↓
ABI + arguments
    ↓
privilege transition
    ↓
validation / policy / resource lookup
    ↓
implementation
    ↓
result hoặc errno
    ↓
resume user-space execution
```

Điểm cần quan sát không chỉ là “system call nào được gọi”, mà còn là nó **block ở đâu, chờ tài nguyên gì, chịu policy nào và có gây scheduling hay không**.

## Những hiểu lầm phổ biến

**“Gọi system call luôn tạo context switch.”** Không. Mode switch và task context switch là hai việc khác nhau.

**“Library call và system call giống nhau.”** Wrapper có thể không gọi system call hoặc gọi system call khác với tên API.

**“System call thành công nghĩa dữ liệu đã xuống thiết bị.”** Với buffered I/O, `write()` thành công chưa đồng nghĩa durability; cần hiểu `fsync()` và storage stack.

**“Ứng dụng treo mà không log thì kernel không biết gì.”** `strace`, `/proc`, scheduler state và socket state vẫn có thể cung cấp bằng chứng.

**“Tối ưu bằng cách giảm system call luôn có lợi.”** Chỉ tối ưu khi đo lường cho thấy đây là bottleneck thật.

## Kết nối kiến thức

System call là điểm nối của gần như toàn bộ thư viện Linux: file descriptor, VFS, process, socket, memory mapping, signal, seccomp và tracing. Đọc tiếp [Tiến trình, luồng, tín hiệu và tác vụ](../04_process/processes_threads_signals_jobs.md), [VFS, page cache và writeback](../01_filesystem/vfs_page_cache_writeback.md) và [Quan sát bằng strace/perf/eBPF](../09_production/observability_tracing_strace_perf.md).