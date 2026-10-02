# Interrupt, softirq và mô hình thiết bị trong Linux

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Interrupt, softirq và mô hình thiết bị trong Linux**. Route đi từ polling → hardware interrupt → top/bottom halves và softirq → device model, driver và network/storage path → CPU load, latency và packet/drop diagnosis.

Khi một ứng dụng gọi `read()`, gửi gói tin mạng hoặc chờ dữ liệu từ ổ đĩa, CPU không nhất thiết ngồi chờ thiết bị hoàn thành công việc. Phần cứng hoạt động theo tốc độ và cơ chế riêng, còn CPU cần tiếp tục chạy những tác vụ khác. **Ngắt (interrupt)** tồn tại để thiết bị có thể báo cho CPU rằng một sự kiện cần được xử lý.

Hiểu interrupt quan trọng vì nhiều hiện tượng môi trường vận hành (production / 운영 환경) như CPU cao nhưng tiến trình không nổi bật, mạng nhận gói chậm, packet drop, độ trễ tăng khi tải lớn hoặc một CPU bị quá tải có thể liên quan tới phần việc chạy trong kernel thay vì trực tiếp trong tiến trình ứng dụng.

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

> **Chuyển mạch:** Trong **Interrupt, softirq và mô hình thiết bị trong Linux**, **Interrupt khác lời gọi hệ thống (system call / 시스템 호출)** tiếp nhận điểm tựa từ **Từ polling tới interrupt** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Interrupt handler phải ngắn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Interrupt khác lời gọi hệ thống (system call / 시스템 호출)

Lời gọi hệ thống (system call / 시스템 호출) bắt đầu từ tiến trình người dùng và đi vào kernel vì tiến trình chủ động yêu cầu một dịch vụ. Interrupt thường đến từ phần cứng hoặc cơ chế hệ thống bất đồng bộ.

```text
system call:
user process -> kernel

hardware interrupt:
device -> CPU/kernel
```

Hai cơ chế đều làm CPU thực thi mã (code / 코드) kernel, nhưng nguyên nhân và ngữ cảnh khác nhau.

> **Chuyển mạch:** Ở chặng này của **Interrupt, softirq và mô hình thiết bị trong Linux**, **Interrupt handler phải ngắn** tiếp nhận điểm tựa từ **Interrupt khác lời gọi hệ thống (system call / 시스템 호출)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Softirq là gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Interrupt handler phải ngắn

Khi CPU vào **trình xử lý ngắt (interrupt handler)**, hệ thống đang xử lý sự kiện cần phản hồi nhanh. Nếu handler làm công việc quá dài, các interrupt khác và tải công việc (workload / 워크로드) bình thường có thể bị trì hoãn.

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

Thiết kế này thường được mô tả bằng ý tưởng **top half** và **bottom half**. Thuật ngữ cụ thể trong kernel đã thay đổi theo subsystem, nhưng mô hình tư duy (mental model / 사고 모델) vẫn hữu ích: phần interrupt trực tiếp cần rất ngắn, còn phần tốn thời gian được đẩy sang ngữ cảnh có thể xử lý linh hoạt hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Interrupt, softirq và mô hình thiết bị trong Linux**, **Softirq là gì?** tiếp nhận điểm tựa từ **Interrupt handler phải ngắn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao ksoftirqd xuất hiện?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Softirq là gì?

**Softirq** là một cơ chế deferred công việc (work / 작업) trong kernel. Networking là ví dụ rất quan trọng. Khi card mạng nhận packet, interrupt handler không nên xử lý toàn bộ TCP/IP ngăn xếp (stack / 스택) ngay trong hard interrupt ngữ cảnh (context / 맥락). Một phần công việc được chuyển sang softirq.

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

`NET_RX` liên quan xử lý packet nhận vào; `NET_TX` liên quan đường truyền gửi; `BLOCK` có thể liên quan khối (block / 블록) I/O completion.

> **Chuyển mạch:** Trong **Interrupt, softirq và mô hình thiết bị trong Linux**, **Vì sao ksoftirqd xuất hiện?** tiếp nhận điểm tựa từ **Softirq là gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **/proc/interrupts** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao `ksoftirqd` xuất hiện?

Nếu softirq phát sinh quá nhiều, kernel không thể dành vô hạn thời gian xử lý chúng ngay trong đường interrupt. Công việc có thể được đẩy sang các luồng thực thi (thread / 스레드) kernel dạng `ksoftirqd/<CPU>`.

```bash
ps -eLo pid,psr,comm | grep ksoftirqd
```

Nếu `ksoftirqd` dùng nhiều CPU trong lúc lưu lượng mạng cao, không nên vội kết luận ứng dụng Java đang tiêu hết CPU. Một phần CPU đang được dùng để xử lý công việc kernel do traffic tạo ra.

> **Chuyển mạch:** Ở chặng này của **Interrupt, softirq và mô hình thiết bị trong Linux**, **/proc/interrupts** tiếp nhận điểm tựa từ **Vì sao ksoftirqd xuất hiện?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **IRQ affinity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Nếu gần như mọi interrupt của NIC dồn vào một CPU trong hệ thống nhiều cốt lõi (core / 핵심), cốt lõi (core / 핵심) đó có thể thành bottleneck dù tổng CPU toàn máy vẫn thấp.

Đây là lý do **phân phối interrupt (IRQ affinity)** quan trọng trên máy chủ thông lượng (throughput / 처리량) cao.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Interrupt, softirq và mô hình thiết bị trong Linux**, **IRQ affinity** tiếp nhận điểm tựa từ **/proc/interrupts** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **RSS, RPS và RFS trong networking** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## IRQ affinity

Kernel có thể giới hạn interrupt cụ thể chạy trên tập CPU nào. Thông tin này thường xuất hiện dưới:

```text
/proc/irq/<IRQ>/smp_affinity
/proc/irq/<IRQ>/smp_affinity_list
```

Không nên thay đổi affinity theo mẹo chung trên Internet. Hệ thống hiện đại có thể dùng `irqbalance`, RSS/RPS hoặc cấu hình driver/NIC để phân phối tải. Điều cần hiểu trước tiên là bottleneck nằm ở đâu.

> **Chuyển mạch:** Trong **Interrupt, softirq và mô hình thiết bị trong Linux**, **RSS, RPS và RFS trong networking** tiếp nhận điểm tựa từ **IRQ affinity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **NAPI và vấn đề interrupt storm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## RSS, RPS và RFS trong networking

Một card mạng tốc độ cao có thể có nhiều receive hàng đợi (queue / 큐). **Receive Side Scaling (RSS)** cho phép NIC phân phối packet vào nhiều hàng đợi (queue / 큐), thường gắn với nhiều CPU.

Linux còn có các cơ chế phần mềm như **Receive Packet Steering (RPS)** và **Receive luồng (flow / 흐름) Steering (RFS)** để phân phối xử lý mạng (network / 네트워크) ngăn xếp (stack / 스택).

Mô hình tư duy (mental model / 사고 모델):

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

Nếu chỉ quan sát luồng thực thi (thread / 스레드) ứng dụng, ta bỏ qua nhiều tầng phía trước.

> **Chuyển mạch:** Ở chặng này của **Interrupt, softirq và mô hình thiết bị trong Linux**, **NAPI và vấn đề interrupt storm** tiếp nhận điểm tựa từ **RSS, RPS và RFS trong networking** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Interrupt coalescing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## NAPI và vấn đề interrupt storm

Nếu NIC phát một interrupt cho từng packet ở tốc độ hàng triệu packet mỗi giây, CPU có thể bị ngập trong interrupt. Linux networking dùng **NAPI (New API)** để kết hợp interrupt với polling có kiểm soát.

Ý tưởng đơn giản:

1. packet đầu tiên kích hoạt interrupt;
2. kernel tạm hạn chế interrupt của hàng đợi (queue / 큐) đó;
3. kernel poll một batch packet;
4. khi hàng đợi (queue / 큐) đã xử lý ổn, interrupt được bật lại.

Đây là một ví dụ cho thấy polling và interrupt không phải hai lựa chọn loại trừ nhau. Kernel kết hợp chúng để giảm overhead trong tải cao.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Interrupt, softirq và mô hình thiết bị trong Linux**, **Interrupt coalescing** tiếp nhận điểm tựa từ **NAPI và vấn đề interrupt storm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trình điều khiển thiết bị (device driver / 장치 드라이버) là lớp nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Interrupt coalescing

Một số NIC có thể gom nhiều sự kiện trước khi phát interrupt. Điều này giảm số interrupt và tăng thông lượng (throughput / 처리량), nhưng có thể tăng độ trễ (latency / 지연 시간) vì packet phải chờ thêm trước khi CPU được báo.

Đây là sự đánh đổi (trade-off / 트레이드오프) quen thuộc:

```text
ít interrupt hơn
    -> overhead thấp hơn
    -> throughput tốt hơn
    -> nhưng có thể tăng latency
```

Không có giá trị tối ưu cho mọi tải công việc (workload / 워크로드). Hệ thống giao dịch nhạy độ trễ (latency / 지연 시간) có yêu cầu khác máy chủ (server / 서버) xử lý batch thông lượng (throughput / 처리량) lớn.

> **Chuyển mạch:** Trong **Interrupt, softirq và mô hình thiết bị trong Linux**, **Trình điều khiển thiết bị (device driver / 장치 드라이버) là lớp nào?** tiếp nhận điểm tựa từ **Interrupt coalescing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **/sys và mô hình thiết bị** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trình điều khiển thiết bị (device driver / 장치 드라이버) là lớp nào?

**trình điều khiển thiết bị (device driver / 장치 드라이버)** là mã (code / 코드) kernel biết cách làm việc với một loại phần cứng hoặc giao diện thiết bị cụ thể.

Ứng dụng không cần biết thanh ghi của card mạng hay giao thức (protocol / 프로토콜) nội bộ của SSD. Thay vào đó:

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

Driver chuyển đổi lớp trừu tượng (abstraction / 추상화) chung của kernel thành thao tác phù hợp thiết bị.

> **Chuyển mạch:** Ở chặng này của **Interrupt, softirq và mô hình thiết bị trong Linux**, **/sys và mô hình thiết bị** tiếp nhận điểm tựa từ **Trình điều khiển thiết bị (device driver / 장치 드라이버) là lớp nào?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thiết bị (device / 장치) nút (node / 노드) trong /dev** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `/sys` và mô hình thiết bị

Linux biểu diễn nhiều đối tượng thiết bị qua `sysfs`:

```bash
ls /sys/class/net
ls /sys/class/block
ls /sys/bus/pci/devices
```

`/sys` không phải ổ đĩa chứa bản sao cấu hình tĩnh. Nó là giao diện cho đối tượng (object / 객체) và thuộc tính kernel.

Ví dụ mạng:

```bash
cat /sys/class/net/eth0/operstate
cat /sys/class/net/eth0/mtu
```

Khối (block / 블록) thiết bị (device / 장치):

```bash
ls -l /sys/class/block
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Interrupt, softirq và mô hình thiết bị trong Linux**, **Thiết bị (device / 장치) nút (node / 노드) trong /dev** tiếp nhận điểm tựa từ **/sys và mô hình thiết bị** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **udev và thiết bị động** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thiết bị (device / 장치) nút (node / 노드) trong `/dev`

Nhiều thiết bị được tiếp cận từ người dùng (user / 사용자) không gian (space / 공간) thông qua **nút thiết bị (device node)** dưới `/dev`.

Ví dụ:

```text
/dev/sda
/dev/nvme0n1
/dev/null
/dev/random
```

Thiết bị (device / 장치) nút (node / 노드) chứa loại thiết bị và major/minor number để kernel ánh xạ thao tác tới driver phù hợp.

```bash
ls -l /dev/null /dev/sda 2>/dev/null
```

Ký tự đầu `c` thường là character thiết bị (device / 장치), `b` là khối (block / 블록) thiết bị (device / 장치).

> **Chuyển mạch:** Trong **Interrupt, softirq và mô hình thiết bị trong Linux**, **udev và thiết bị động** tiếp nhận điểm tựa từ **Thiết bị (device / 장치) nút (node / 노드) trong /dev** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **DMA: thiết bị có cần CPU bản sao (copy / 복사) từng byte không?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## udev và thiết bị động

Phần cứng có thể xuất hiện hoặc biến mất khi hệ thống đang chạy. **udev** xử lý các sự kiện thiết bị (device / 장치) trong người dùng (user / 사용자) không gian (space / 공간) và có thể tạo tên, symlink hoặc áp dụng quy tắc (rule / 규칙).

```bash
udevadm info --query=all --name=/dev/nvme0n1
```

Điều này giải thích vì sao tên thiết bị không chỉ là thứ kernel “ghi cứng”. Có một chuỗi kernel sự kiện (event / 이벤트) → udev quy tắc (rule / 규칙) → user-space thiết bị (device / 장치) naming.

> **Chuyển mạch:** Ở chặng này của **Interrupt, softirq và mô hình thiết bị trong Linux**, **DMA: thiết bị có cần CPU bản sao (copy / 복사) từng byte không?** tiếp nhận điểm tựa từ **udev và thiết bị động** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Interrupt và độ trễ môi trường vận hành (production / 운영 환경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## DMA: thiết bị có cần CPU bản sao (copy / 복사) từng byte không?

**Truy cập bộ nhớ trực tiếp (Direct memory Access - DMA)** cho phép thiết bị truyền dữ liệu tới/từ RAM mà không yêu cầu CPU bản sao (copy / 복사) từng byte.

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

CPU vẫn tham gia điều phối và xử lý giao thức (protocol / 프로토콜), nhưng DMA giảm công việc bản sao (copy / 복사) ở mức phần cứng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Interrupt, softirq và mô hình thiết bị trong Linux**, **Interrupt và độ trễ môi trường vận hành (production / 운영 환경)** tiếp nhận điểm tựa từ **DMA: thiết bị có cần CPU bản sao (copy / 복사) từng byte không?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Softirq và top** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Interrupt và độ trễ môi trường vận hành (production / 운영 환경)

Một máy có thể có CPU utilization tổng thể chỉ 40%, nhưng một số cốt lõi (core / 핵심) bị softirq rất cao. Nếu các luồng (flow / 흐름) mạng chủ yếu vào những cốt lõi (core / 핵심) đó, tail độ trễ (latency / 지연 시간) có thể tăng dù dashboard CPU trung bình trông “khỏe”.

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

Cần đọc cùng nhau thay vì dựa vào một chỉ số (metric / 지표).

> **Chuyển mạch:** Trong **Interrupt, softirq và mô hình thiết bị trong Linux**, **Softirq và top** tiếp nhận điểm tựa từ **Interrupt và độ trễ môi trường vận hành (production / 운영 환경)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khi packet drop nhưng ứng dụng không thấy gì** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Softirq và `top`

Trong `top`, CPU thời gian (time / 시간) có thể được chia thành các loại như `us`, `sy`, `si`, `hi`, `wa` tùy phiên bản.

- `hi` thường liên quan hard interrupt thời gian (time / 시간);
- `si` thường liên quan softirq thời gian (time / 시간).

Nếu `si` tăng mạnh cùng mạng (network / 네트워크) traffic, đây là tín hiệu quan trọng.

> **Chuyển mạch:** Ở chặng này của **Interrupt, softirq và mô hình thiết bị trong Linux**, **Khi packet drop nhưng ứng dụng không thấy gì** tiếp nhận điểm tựa từ **Softirq và top** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Workqueue** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khi packet drop nhưng ứng dụng không thấy gì

Packet có thể bị drop trước khi tới socket ứng dụng vì:

- NIC ring đầy;
- kernel backlog quá tải;
- softirq không xử lý kịp;
- firewall hoặc chính sách (policy / 정책) drop;
- socket receive buffer đầy;
- ứng dụng (application / 애플리케이션) đọc quá chậm.

Vì vậy “không có log ứng dụng” không chứng minh yêu cầu (request / 요청) chưa bao giờ tới host.

Điều tra có thể dùng:

```bash
ip -s link show dev eth0
ss -s
nstat
ethtool -S eth0 2>/dev/null | head -80
```

Các counter cụ thể phụ thuộc driver.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Interrupt, softirq và mô hình thiết bị trong Linux**, **Workqueue** tiếp nhận điểm tựa từ **Khi packet drop nhưng ứng dụng không thấy gì** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Workqueue

Không phải deferred công việc (work / 작업) nào cũng dùng softirq. Kernel có **workqueue** để thực hiện công việc trong ngữ cảnh (context / 맥락) của kernel worker luồng thực thi (thread / 스레드), nơi có thể ngủ trong nhiều trường hợp phù hợp hơn so với interrupt ngữ cảnh (context / 맥락).

Bạn có thể thấy các luồng thực thi (thread / 스레드) dạng:

```text
kworker/...
```

Nếu `kworker` dùng CPU cao, cần tìm subsystem gây công việc (work / 작업) thay vì kết luận chính luồng thực thi (thread / 스레드) này là “ứng dụng lỗi”. Nó là worker chung cho nhiều loại công việc kernel.

> **Chuyển mạch:** Trong **Interrupt, softirq và mô hình thiết bị trong Linux**, **Mô hình tư duy** gom các mảnh từ **Workqueue** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

Một yêu cầu (request / 요청) môi trường vận hành (production / 운영 환경) không chỉ tiêu CPU trong tiến trình (process / 프로세스):

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

Do đó CPU thời gian (time / 시간) và độ trễ (latency / 지연 시간) có thể phát sinh ở nhiều tầng trước khi ứng dụng thực sự chạy.

> **Chuyển mạch:** Ở chặng này của **Interrupt, softirq và mô hình thiết bị trong Linux**, **Những hiểu lầm phổ biến** gom các mảnh từ **Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến

**“CPU cao luôn phải tìm tiến trình (process / 프로세스) cao nhất.”** Một phần tải có thể nằm ở interrupt/softirq/kernel worker.

**“Interrupt càng ít càng tốt.”** Coalescing quá mạnh có thể tăng độ trễ (latency / 지연 시간). Mục tiêu là cân bằng overhead và độ trễ (latency / 지연 시간).

**“Polling luôn lãng phí.”** NAPI cho thấy polling có kiểm soát rất hữu ích ở thông lượng (throughput / 처리량) cao.

**“`/dev/sda` chính là ổ cứng vật lý.”** Nó là thiết bị (device / 장치) nút (node / 노드) đại diện cho thiết bị/khối (block / 블록) giao diện (interface / 인터페이스) mà kernel expose; phía dưới có thể là NVMe, virtual disk, RAID hoặc lưu trữ (storage / 저장소) khác.

**“Driver chỉ cần quan tâm khi cài phần cứng.”** Driver quyết định cách kernel giao tiếp với thiết bị và ảnh hưởng trực tiếp tới hiệu năng (performance / 성능), lỗi (error / 오류) counter và khả năng quan sát (observability / 관측 가능성).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Interrupt, softirq và mô hình thiết bị trong Linux**, **Kết nối kiến thức** tiếp nhận điểm tựa từ **Những hiểu lầm phổ biến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối kiến thức

Chương này nối [kernel, user space và system call](./kernel_userspace_syscalls.md) với [I/O performance](../06_resources/io_performance.md), [IP routing/NAT](../07_networking/ip_routing_nat_conntrack.md) và [quan sát production](../09_production/observability_tracing_strace_perf.md). Khi mạng (network / 네트워크) hoặc lưu trữ (storage / 저장소) có thông lượng (throughput / 처리량) cao, interrupt và deferred công việc (work / 작업) là tầng không nên bỏ qua.

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
