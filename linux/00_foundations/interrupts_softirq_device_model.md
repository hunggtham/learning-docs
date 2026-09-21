# Interrupt, softirq và mô hình thiết bị trong Linux

Khi một ứng dụng gọi `read()`, gửi gói tin mạng hoặc chờ dữ liệu từ ổ đĩa, CPU không nhất thiết ngồi chờ thiết bị hoàn thành công việc. Phần cứng hoạt động theo tốc độ và cơ chế riêng, còn CPU cần tiếp tục chạy những tác vụ khác. **Ngắt (interrupt)** tồn tại để thiết bị có thể báo cho CPU rằng một sự kiện cần được xử lý.

Hiểu interrupt quan trọng vì nhiều hiện tượng production như CPU cao nhưng tiến trình không nổi bật, mạng nhận gói chậm, packet drop, độ trễ tăng khi tải lớn hoặc một CPU bị quá tải có thể liên quan tới phần việc chạy trong kernel thay vì trực tiếp trong tiến trình ứng dụng.

## Từ polling tới interrupt

Một cách đơn giản để biết thiết bị đã hoàn thành chưa là liên tục hỏi:

```text
CPU -> thiết bị: xong chưa?
CPU -> thiết bị: xong chưa?
CPU -> thiết bị: xong chưa?
```

Cách này gọi là **thăm dò (polling)**. Polling có thể phù hợp trong một số đường xử lý hiệu năng rất cao, nhưng nếu áp dụng mọi nơi sẽ lãng phí CPU.

Interrupt đảo hướng giao tiếp:

```text
CPU giao việc cho thiết bị
        ↓
CPU chạy việc khác
        ↓
thiết bị hoàn thành
        ↓
thiết bị phát interrupt
        ↓
kernel xử lý sự kiện
```

Đây là một ví dụ về thiết kế **hướng sự kiện (event-driven)** ở mức phần cứng.

## Interrupt khác system call

System call bắt đầu từ tiến trình người dùng và đi vào kernel vì tiến trình chủ động yêu cầu một dịch vụ. Interrupt thường đến từ phần cứng hoặc cơ chế hệ thống bất đồng bộ.

```text
system call:
user process -> kernel

hardware interrupt:
device -> CPU/kernel
```

Hai cơ chế đều làm CPU thực thi code kernel, nhưng nguyên nhân và ngữ cảnh khác nhau.

## Interrupt handler phải ngắn

Khi CPU vào **trình xử lý ngắt (interrupt handler)**, hệ thống đang xử lý sự kiện cần phản hồi nhanh. Nếu handler làm công việc quá dài, các interrupt khác và workload bình thường có thể bị trì hoãn.

Vì vậy Linux thường chia xử lý thành hai phần khái niệm:

```text
phần khẩn cấp
    ↓
nhận interrupt, xác nhận thiết bị, lấy trạng thái tối thiểu
    ↓
hoãn phần việc lớn hơn
    ↓
softirq / tasklet / workqueue hoặc cơ chế khác
```

Thiết kế này thường được mô tả bằng ý tưởng **top half** và **bottom half**. Thuật ngữ cụ thể trong kernel đã thay đổi theo subsystem, nhưng mental model vẫn hữu ích: phần interrupt trực tiếp cần rất ngắn, còn phần tốn thời gian được đẩy sang ngữ cảnh có thể xử lý linh hoạt hơn.

## Softirq là gì?

**Softirq** là một cơ chế deferred work trong kernel. Networking là ví dụ rất quan trọng. Khi card mạng nhận packet, interrupt handler không nên xử lý toàn bộ TCP/IP stack ngay trong hard interrupt context. Một phần công việc được chuyển sang softirq.

Có thể xem tổng hợp softirq:

```bash
cat /proc/softirqs
```

Các dòng thường gặp gồm:

```text
NET_RX
NET_TX
TIMER
SCHED
RCU
BLOCK
```

`NET_RX` liên quan xử lý packet nhận vào; `NET_TX` liên quan đường truyền gửi; `BLOCK` có thể liên quan block I/O completion.

## Vì sao `ksoftirqd` xuất hiện?

Nếu softirq phát sinh quá nhiều, kernel không thể dành vô hạn thời gian xử lý chúng ngay trong đường interrupt. Công việc có thể được đẩy sang các thread kernel dạng `ksoftirqd/<CPU>`.

```bash
ps -eLo pid,psr,comm | grep ksoftirqd
```

Nếu `ksoftirqd` dùng nhiều CPU trong lúc lưu lượng mạng cao, không nên vội kết luận ứng dụng Java đang tiêu hết CPU. Một phần CPU đang được dùng để xử lý công việc kernel do traffic tạo ra.

## `/proc/interrupts`

Linux cung cấp số lần interrupt theo CPU:

```bash
cat /proc/interrupts
```

Kết quả có thể giống:

```text
           CPU0       CPU1       CPU2       CPU3
  45:     12031      93211      10221      81120  IR-PCI-MSI  eth0
```

Nếu gần như mọi interrupt của NIC dồn vào một CPU trong hệ thống nhiều core, core đó có thể thành bottleneck dù tổng CPU toàn máy vẫn thấp.

Đây là lý do **phân phối interrupt (IRQ affinity)** quan trọng trên máy chủ throughput cao.

## IRQ affinity

Kernel có thể giới hạn interrupt cụ thể chạy trên tập CPU nào. Thông tin này thường xuất hiện dưới:

```text
/proc/irq/<IRQ>/smp_affinity
/proc/irq/<IRQ>/smp_affinity_list
```

Không nên thay đổi affinity theo mẹo chung trên Internet. Hệ thống hiện đại có thể dùng `irqbalance`, RSS/RPS hoặc cấu hình driver/NIC để phân phối tải. Điều cần hiểu trước tiên là bottleneck nằm ở đâu.

## RSS, RPS và RFS trong networking

Một card mạng tốc độ cao có thể có nhiều receive queue. **Receive Side Scaling (RSS)** cho phép NIC phân phối packet vào nhiều queue, thường gắn với nhiều CPU.

Linux còn có các cơ chế phần mềm như **Receive Packet Steering (RPS)** và **Receive Flow Steering (RFS)** để phân phối xử lý network stack.

Mental model:

```text
NIC queues
    ↓
IRQ / CPU
    ↓
NET_RX softirq
    ↓
IP/TCP processing
    ↓
socket receive queue
    ↓
application thread
```

Nếu chỉ quan sát thread ứng dụng, ta bỏ qua nhiều tầng phía trước.

## NAPI và vấn đề interrupt storm

Nếu NIC phát một interrupt cho từng packet ở tốc độ hàng triệu packet mỗi giây, CPU có thể bị ngập trong interrupt. Linux networking dùng **NAPI (New API)** để kết hợp interrupt với polling có kiểm soát.

Ý tưởng đơn giản:

1. packet đầu tiên kích hoạt interrupt;
2. kernel tạm hạn chế interrupt của queue đó;
3. kernel poll một batch packet;
4. khi queue đã xử lý ổn, interrupt được bật lại.

Đây là một ví dụ cho thấy polling và interrupt không phải hai lựa chọn loại trừ nhau. Kernel kết hợp chúng để giảm overhead trong tải cao.

## Interrupt coalescing

Một số NIC có thể gom nhiều sự kiện trước khi phát interrupt. Điều này giảm số interrupt và tăng throughput, nhưng có thể tăng latency vì packet phải chờ thêm trước khi CPU được báo.

Đây là trade-off quen thuộc:

```text
ít interrupt hơn
    -> overhead thấp hơn
    -> throughput tốt hơn
    -> nhưng có thể tăng latency
```

Không có giá trị tối ưu cho mọi workload. Hệ thống giao dịch nhạy latency có yêu cầu khác server xử lý batch throughput lớn.

## Device driver là lớp nào?

**Trình điều khiển thiết bị (device driver)** là code kernel biết cách làm việc với một loại phần cứng hoặc giao diện thiết bị cụ thể.

Ứng dụng không cần biết thanh ghi của card mạng hay protocol nội bộ của SSD. Thay vào đó:

```text
application
    ↓
system call
    ↓
kernel subsystem
    ↓
device driver
    ↓
hardware
```

Driver chuyển đổi abstraction chung của kernel thành thao tác phù hợp thiết bị.

## `/sys` và mô hình thiết bị

Linux biểu diễn nhiều đối tượng thiết bị qua `sysfs`:

```bash
ls /sys/class/net
ls /sys/class/block
ls /sys/bus/pci/devices
```

`/sys` không phải ổ đĩa chứa bản sao cấu hình tĩnh. Nó là giao diện cho object và thuộc tính kernel.

Ví dụ mạng:

```bash
cat /sys/class/net/eth0/operstate
cat /sys/class/net/eth0/mtu
```

Block device:

```bash
ls -l /sys/class/block
```

## Device node trong `/dev`

Nhiều thiết bị được tiếp cận từ user space thông qua **nút thiết bị (device node)** dưới `/dev`.

Ví dụ:

```text
/dev/sda
/dev/nvme0n1
/dev/null
/dev/random
```

Device node chứa loại thiết bị và major/minor number để kernel ánh xạ thao tác tới driver phù hợp.

```bash
ls -l /dev/null /dev/sda 2>/dev/null
```

Ký tự đầu `c` thường là character device, `b` là block device.

## udev và thiết bị động

Phần cứng có thể xuất hiện hoặc biến mất khi hệ thống đang chạy. **udev** xử lý các sự kiện device trong user space và có thể tạo tên, symlink hoặc áp dụng rule.

```bash
udevadm info --query=all --name=/dev/nvme0n1
```

Điều này giải thích vì sao tên thiết bị không chỉ là thứ kernel “ghi cứng”. Có một chuỗi kernel event → udev rule → user-space device naming.

## DMA: thiết bị có cần CPU copy từng byte không?

**Truy cập bộ nhớ trực tiếp (Direct Memory Access - DMA)** cho phép thiết bị truyền dữ liệu tới/từ RAM mà không yêu cầu CPU copy từng byte.

Ví dụ đường nhận packet có thể hình dung:

```text
NIC nhận frame
   ↓
DMA dữ liệu vào RAM
   ↓
NIC báo completion bằng interrupt
   ↓
kernel xử lý descriptor
   ↓
network stack
```

CPU vẫn tham gia điều phối và xử lý protocol, nhưng DMA giảm công việc copy ở mức phần cứng.

## Interrupt và độ trễ production

Một máy có thể có CPU utilization tổng thể chỉ 40%, nhưng một số core bị softirq rất cao. Nếu các flow mạng chủ yếu vào những core đó, tail latency có thể tăng dù dashboard CPU trung bình trông “khỏe”.

Dùng:

```bash
mpstat -P ALL 1
cat /proc/softirqs
cat /proc/interrupts
```

Nếu có `sar`:

```bash
sar -I SUM 1
sar -n DEV 1
```

Cần đọc cùng nhau thay vì dựa vào một metric.

## Softirq và `top`

Trong `top`, CPU time có thể được chia thành các loại như `us`, `sy`, `si`, `hi`, `wa` tùy phiên bản.

- `hi` thường liên quan hard interrupt time;
- `si` thường liên quan softirq time.

Nếu `si` tăng mạnh cùng network traffic, đây là tín hiệu quan trọng.

## Khi packet drop nhưng ứng dụng không thấy gì

Packet có thể bị drop trước khi tới socket ứng dụng vì:

- NIC ring đầy;
- kernel backlog quá tải;
- softirq không xử lý kịp;
- firewall hoặc policy drop;
- socket receive buffer đầy;
- application đọc quá chậm.

Vì vậy “không có log ứng dụng” không chứng minh request chưa bao giờ tới host.

Điều tra có thể dùng:

```bash
ip -s link show dev eth0
ss -s
nstat
ethtool -S eth0 2>/dev/null | head -80
```

Các counter cụ thể phụ thuộc driver.

## Workqueue

Không phải deferred work nào cũng dùng softirq. Kernel có **workqueue** để thực hiện công việc trong context của kernel worker thread, nơi có thể ngủ trong nhiều trường hợp phù hợp hơn so với interrupt context.

Bạn có thể thấy các thread dạng:

```text
kworker/...
```

Nếu `kworker` dùng CPU cao, cần tìm subsystem gây work thay vì kết luận chính thread này là “ứng dụng lỗi”. Nó là worker chung cho nhiều loại công việc kernel.

## Mô hình tư duy

Một request production không chỉ tiêu CPU trong process:

```text
hardware event
   ↓
interrupt
   ↓
softirq / deferred kernel work
   ↓
kernel subsystem
   ↓
socket / file descriptor
   ↓
application thread
```

Do đó CPU time và latency có thể phát sinh ở nhiều tầng trước khi ứng dụng thực sự chạy.

## Những hiểu lầm phổ biến

**“CPU cao luôn phải tìm process cao nhất.”** Một phần tải có thể nằm ở interrupt/softirq/kernel worker.

**“Interrupt càng ít càng tốt.”** Coalescing quá mạnh có thể tăng latency. Mục tiêu là cân bằng overhead và latency.

**“Polling luôn lãng phí.”** NAPI cho thấy polling có kiểm soát rất hữu ích ở throughput cao.

**“`/dev/sda` chính là ổ cứng vật lý.”** Nó là device node đại diện cho thiết bị/block interface mà kernel expose; phía dưới có thể là NVMe, virtual disk, RAID hoặc storage khác.

**“Driver chỉ cần quan tâm khi cài phần cứng.”** Driver quyết định cách kernel giao tiếp với thiết bị và ảnh hưởng trực tiếp tới performance, error counter và observability.

## Kết nối kiến thức

Chương này nối [kernel, user space và system call](./kernel_userspace_syscalls.md) với [I/O performance](../06_resources/io_performance.md), [IP routing/NAT](../07_networking/ip_routing_nat_conntrack.md) và [quan sát production](../09_production/observability_tracing_strace_perf.md). Khi network hoặc storage có throughput cao, interrupt và deferred work là tầng không nên bỏ qua.