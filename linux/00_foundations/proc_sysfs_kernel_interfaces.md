# `/proc`, `/sys` và giao diện quan sát kernel

Linux có một đặc điểm rất mạnh: nhiều trạng thái của hạt nhân (kernel) và tiến trình (process) được trình bày qua các hệ thống tệp giả (pseudo-filesystem). Điều này khiến việc quan sát hệ thống trở nên thống nhất: thay vì mỗi subsystem cần một giao thức hoàn toàn khác, nhiều thông tin có thể được đọc qua đường dẫn giống như đọc tệp.

Tuy nhiên `/proc` và `/sys` **không phải thư mục dữ liệu thông thường trên ổ đĩa**. Nội dung của chúng được kernel tạo động dựa trên trạng thái hiện tại.

## Tại sao kernel lại trình bày trạng thái qua filesystem?

Một hệ điều hành phải cung cấp cách để chương trình trong không gian người dùng (user space) hỏi những câu như:

- tiến trình này đang dùng bao nhiêu bộ nhớ;
- có bao nhiêu bộ mô tả tệp đang mở;
- giới hạn tài nguyên hiện tại là gì;
- CPU nào tồn tại;
- thiết bị khối nào đang có mặt;
- tham số kernel hiện tại là gì.

Có thể tạo một API riêng cho từng câu hỏi, nhưng Unix/Linux tận dụng mô hình tên đường dẫn và thao tác đọc/ghi vốn đã quen thuộc.

> **Mô hình tư duy:** `/proc` và `/sys` giống như các “cửa sổ” vào trạng thái của kernel. Bạn đọc một đường dẫn nhưng không nhất thiết đang đọc byte từ ổ đĩa.

## `/proc`: trạng thái tiến trình và kernel

`/proc` ban đầu gắn chặt với thông tin tiến trình. Mỗi tiến trình thường có một thư mục theo PID:

```text
/proc/1
/proc/1234
/proc/9876
```

Một số đường dẫn quan trọng:

```bash
/proc/<PID>/status
/proc/<PID>/cmdline
/proc/<PID>/environ
/proc/<PID>/limits
/proc/<PID>/fd/
/proc/<PID>/maps
/proc/<PID>/smaps
/proc/<PID>/io
```

### `/proc/<PID>/status`

```bash
cat /proc/1234/status
```

Tệp này cho thấy các trường như tên tiến trình, trạng thái, UID/GID, số luồng (threads), bộ nhớ và capability-related state.

Nó hữu ích khi cần xác minh **trạng thái hiệu lực (effective state)** thay vì tin vào cấu hình mong muốn.

### `/proc/<PID>/cmdline`

```bash
tr '\0' ' ' < /proc/1234/cmdline
```

Command line trong procfs dùng ký tự NUL để phân tách arguments, vì vậy `cat` trực tiếp có thể khó đọc.

Điều này rất hữu ích khi cần biết JVM thực sự được khởi động với option nào.

### `/proc/<PID>/environ`

```bash
tr '\0' '\n' < /proc/1234/environ
```

Cho phép quan sát biến môi trường (environment variables) của tiến trình nếu quyền truy cập cho phép.

Cần đặc biệt cẩn thận vì môi trường có thể chứa token, mật khẩu hoặc secret. Không nên sao chép toàn bộ output vào ticket/chat/log nếu chưa kiểm tra dữ liệu nhạy cảm.

### `/proc/<PID>/fd`

```bash
ls -l /proc/1234/fd
```

Thư mục này biểu diễn các bộ mô tả tệp (file descriptors) đang mở.

Ví dụ có thể thấy:

```text
0 -> /dev/null
1 -> /var/log/app.log
2 -> /var/log/app-error.log
10 -> socket:[1234567]
11 -> /opt/app/config.yml
```

Đây là cầu nối trực tiếp giữa mô hình tiến trình và các tài nguyên mà tiến trình đang giữ.

Nếu số lượng entry tăng liên tục:

```bash
ls /proc/1234/fd | wc -l
```

có thể đặt giả thuyết về rò rỉ descriptor, nhưng cần quan sát xu hướng theo thời gian và loại descriptor trước khi kết luận.

## `/proc/<PID>/maps` và `smaps`

`maps` cho thấy các vùng ánh xạ bộ nhớ (memory mappings): executable, shared libraries, heap-like regions, memory-mapped files.

```bash
less /proc/1234/maps
```

`smaps` chi tiết hơn và chứa các trường accounting như RSS/PSS cho từng mapping.

Đây là công cụ quan trọng để hiểu vì sao bộ nhớ tiến trình không chỉ là một “heap”. Với JVM, ngoài Java heap còn có thư viện native, code cache, thread stack, mapped JAR/shared objects và các vùng native khác.

## `/proc/meminfo`

```bash
cat /proc/meminfo
```

`free` và nhiều tool khác đọc/diễn giải thông tin từ kernel. Các trường như `MemTotal`, `MemAvailable`, `Cached`, `SwapTotal`, `SwapFree` giúp quan sát bộ nhớ ở mức hệ thống.

Không nên tự tạo kết luận chỉ từ một trường. Ví dụ `Cached` lớn không có nghĩa memory leak.

Xem thêm: [Bộ nhớ và bộ nhớ ảo](../06_resources/memory_virtual_memory.md).

## `/proc/loadavg`

```bash
cat /proc/loadavg
```

Cho thấy tải trung bình và một số thông tin về runnable tasks/process count.

Tool `uptime` trình bày cùng loại dữ liệu theo cách dễ đọc hơn, nhưng hiểu `/proc/loadavg` giúp thấy tool user-space lấy state từ đâu.

## `/proc/net`

Một phần thông tin mạng cũng được expose dưới `/proc/net`, nhưng trong thực tế nên ưu tiên các tool hiện đại như `ss`, `ip`, `nstat` vì chúng diễn giải netlink/kernel state tốt hơn và ổn định hơn cho người vận hành.

## `/proc/sys`: tham số kernel runtime

Nhiều tham số kernel có thể đọc/ghi qua `/proc/sys`.

Ví dụ:

```bash
cat /proc/sys/net/ipv4/ip_forward
```

Tương ứng có thể đọc qua `sysctl`:

```bash
sysctl net.ipv4.ip_forward
```

`sysctl` cung cấp giao diện thân thiện hơn.

### Thay đổi tạm thời

```bash
sudo sysctl -w net.ipv4.ip_forward=1
```

Thay đổi này ảnh hưởng runtime hiện tại nhưng có thể mất sau reboot nếu không được cấu hình persistent.

### Thay đổi persistent

Thông thường cấu hình nằm trong các file như:

```text
/etc/sysctl.conf
/etc/sysctl.d/*.conf
```

sau đó load bằng cơ chế phù hợp:

```bash
sudo sysctl --system
```

Không nên copy các “kernel tuning” từ internet vào production mà không biết workload, kernel version và trade-off. Một giá trị tốt cho database host có thể không phù hợp với application server hoặc container host.

## `/sys`: mô hình thiết bị và kernel object

`/sys` (sysfs) trình bày các thiết bị và kernel objects theo cấu trúc phân cấp.

Ví dụ:

```bash
ls /sys/class/net
ls /sys/block
ls /sys/devices
```

### Network interface

```bash
cat /sys/class/net/eth0/mtu
cat /sys/class/net/eth0/operstate
```

Có thể nhìn trạng thái và thuộc tính interface.

### Block device

```bash
ls /sys/block/sda
```

Thông tin queue, scheduler và device relationships có thể được expose ở đây.

Các tool như `lsblk`, `udevadm`, `ip` thường dễ dùng hơn, nhưng `/sys` giúp hiểu dữ liệu gốc.

## `/dev`: device nodes và mối quan hệ với kernel

`/dev` chứa device nodes, không phải thiết bị vật lý theo nghĩa “file nằm trên disk”. Device node là giao diện để user-space tương tác với driver/kernel subsystem.

Ví dụ:

```text
/dev/null
/dev/zero
/dev/random
/dev/sda
/dev/tty
```

`/dev/null` không lưu dữ liệu. `/dev/tty` đại diện terminal phù hợp với tiến trình. `/dev/sda` đại diện block device nếu hệ thống đặt tên như vậy.

Đây là lý do câu “everything is a file” nên được hiểu là **nhiều resource có thể dùng giao diện file-like**, không phải mọi thứ đều là regular file.

## udev và thiết bị động

Linux hiện đại thường dùng `udev` để quản lý device events và tạo các device nodes/symlinks phù hợp trong `/dev`.

Khi gắn USB/storage/network device, kernel phát hiện hardware, driver tạo kernel device object, rồi user-space device manager xử lý policy/naming.

Có thể quan sát:

```bash
udevadm info --query=all --name=/dev/sda
```

hoặc monitor events:

```bash
udevadm monitor
```

Không nên chạy monitor vô thời hạn trên production nếu chỉ cần một kiểm tra ngắn; nó có thể tạo rất nhiều output.

## Khi nào nên đọc trực tiếp `/proc` hoặc `/sys`?

Các tool chuẩn thường nên được ưu tiên vì dễ đọc hơn:

```bash
ps
ss
ip
free
lsblk
systemctl
```

Nhưng `/proc` và `/sys` trở nên rất giá trị khi:

- tool không hiển thị trường bạn cần;
- cần xác minh trạng thái thật của một PID cụ thể;
- viết diagnostic script nhẹ;
- muốn hiểu tool user-space đang lấy dữ liệu ở đâu;
- container/minimal image không có nhiều tiện ích.

## Ví dụ: điều tra tiến trình Java bị nghi rò rỉ file descriptor

Bước đầu không cần restart ngay.

```bash
PID=$(pgrep -f 'java.*app.jar' | head -1)
ls /proc/$PID/fd | wc -l
cat /proc/$PID/limits | grep 'open files'
```

Sau đó xem loại descriptor:

```bash
sudo lsof -p "$PID" | head -100
```

Nếu số descriptor tăng qua mỗi lần đo, hãy phân loại: socket, file, pipe hay deleted file.

Chỉ khi có evidence về xu hướng mới chuyển sang code/runtime analysis.

## Những hiểu lầm phổ biến

**“`/proc` là thư mục thật trên ổ đĩa.”** Không. Nó là pseudo-filesystem do kernel sinh động.

**“Sửa file trong `/proc/sys` là persistent.”** Thường không. Muốn giữ qua reboot cần cấu hình sysctl persistent.

**“Có thể chỉnh sysctl để tăng hiệu năng mà không có rủi ro.”** Sai. Kernel tuning luôn có trade-off và phụ thuộc workload.

**“`/sys` chỉ dành cho kernel developer.”** Không. Operator vẫn có thể dùng nó để hiểu device state, nhưng nên ưu tiên tool cấp cao khi có.

**“Mọi thứ dưới `/proc/<PID>` luôn đọc được.”** Quyền, security policy và kernel settings có thể hạn chế truy cập.

## Mô hình tư duy

Hãy xem `/proc` và `/sys` như hai bản đồ khác nhau của cùng hệ thống:

- `/proc` nhấn mạnh **tiến trình và trạng thái runtime**;
- `/sys` nhấn mạnh **thiết bị và mô hình kernel object**;
- `/dev` cung cấp **điểm tương tác với device/resource**.

Ba khu vực này tạo một cầu nối quan trọng giữa lý thuyết kernel và công việc vận hành thực tế.

Xem thêm: [Kernel, user space và system calls](./kernel_userspace_syscalls.md), [Process, thread và signal](../04_process/processes_threads_signals_jobs.md), [Storage và filesystem](../06_resources/storage_filesystems.md).