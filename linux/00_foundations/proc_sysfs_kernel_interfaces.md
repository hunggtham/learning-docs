# `/proc`, `/sys` và giao diện quan sát kernel

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **/proc, /sys và giao diện quan sát kernel**. Route đi từ pseudo-filesystem rationale → /proc process/kernel state → /sys devices, drivers và uevents → read/write boundaries → observability and safe diagnosis.

Linux có một đặc điểm rất mạnh: nhiều trạng thái của hạt nhân (kernel) và tiến trình (process / 프로세스) được trình bày qua các hệ thống tệp giả (pseudo-filesystem). Điều này khiến việc quan sát hệ thống trở nên thống nhất: thay vì mỗi subsystem cần một giao thức hoàn toàn khác, nhiều thông tin có thể được đọc qua đường dẫn giống như đọc tệp.

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

> **Nối mạch:** Trong **/proc, /sys và giao diện quan sát kernel**, **/proc: trạng thái tiến trình và kernel** nối từ **Tại sao kernel lại trình bày trạng thái qua filesystem?** sang **/proc/<PID>/maps và smaps**, vì cơ chế trước tạo đầu vào cho bước sau.

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

Trước khi chạy hoặc đọc ví dụ dưới đây, hãy xác định câu hỏi vận hành mà nó trả lời, dữ liệu nào sẽ quan sát được và giới hạn của kết quả. Lệnh chỉ có ý nghĩa khi gắn với một giả thuyết về state của hệ thống.

```bash
cat /proc/1234/status
```

Tệp này cho thấy các trường như tên tiến trình, trạng thái, UID/GID, số luồng (threads), bộ nhớ và capability-related trạng thái (state / 상태).

Nó hữu ích khi cần xác minh **trạng thái hiệu lực (effective state)** thay vì tin vào cấu hình mong muốn.

### `/proc/<PID>/cmdline`

Trước khi chạy hoặc đọc ví dụ dưới đây, hãy xác định câu hỏi vận hành mà nó trả lời, dữ liệu nào sẽ quan sát được và giới hạn của kết quả. Lệnh chỉ có ý nghĩa khi gắn với một giả thuyết về state của hệ thống.

```bash
tr '\0' ' ' < /proc/1234/cmdline
```

Command line trong procfs dùng ký tự NUL để phân tách arguments, vì vậy `cat` trực tiếp có thể khó đọc.

Điều này rất hữu ích khi cần biết JVM thực sự được khởi động với option nào.

### `/proc/<PID>/environ`

Trước khi chạy hoặc đọc ví dụ dưới đây, hãy xác định câu hỏi vận hành mà nó trả lời, dữ liệu nào sẽ quan sát được và giới hạn của kết quả. Lệnh chỉ có ý nghĩa khi gắn với một giả thuyết về state của hệ thống.

```bash
tr '\0' '\n' < /proc/1234/environ
```

Cho phép quan sát biến môi trường (environment variables) của tiến trình nếu quyền truy cập cho phép.

Cần đặc biệt cẩn thận vì môi trường có thể chứa đơn vị từ (token / 토큰), mật khẩu hoặc secret. Không nên sao chép toàn bộ đầu ra (output / 출력) vào ticket/chat/log nếu chưa kiểm tra dữ liệu nhạy cảm.

### `/proc/<PID>/fd`

Trước khi chạy hoặc đọc ví dụ dưới đây, hãy xác định câu hỏi vận hành mà nó trả lời, dữ liệu nào sẽ quan sát được và giới hạn của kết quả. Lệnh chỉ có ý nghĩa khi gắn với một giả thuyết về state của hệ thống.

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

> **Nối mạch:** Ở chặng này của **/proc, /sys và giao diện quan sát kernel**, **/proc/<PID>/maps và smaps** nối từ **/proc: trạng thái tiến trình và kernel** sang **/proc/meminfo**, vì cơ chế trước tạo đầu vào cho bước sau.

## `/proc/<PID>/maps` và `smaps`

`maps` cho thấy các vùng ánh xạ bộ nhớ (memory mappings): executable, dùng chung (shared / 공유) libraries, heap-like regions, memory-mapped files.

```bash
less /proc/1234/maps
```

`smaps` chi tiết hơn và chứa các trường accounting như RSS/PSS cho từng ánh xạ (mapping / 매핑).

Đây là công cụ quan trọng để hiểu vì sao bộ nhớ tiến trình không chỉ là một “vùng nhớ động (heap / 힙)”. Với JVM, ngoài Java vùng nhớ động (heap / 힙) còn có thư viện bản địa (native / 네이티브), mã (code / 코드) bộ nhớ đệm (cache / 캐시), luồng thực thi (thread / 스레드) ngăn xếp (stack / 스택), mapped JAR/dùng chung (shared / 공유) objects và các vùng bản địa (native / 네이티브) khác.

> **Nối mạch:** Đặt trong câu hỏi lớn của **/proc, /sys và giao diện quan sát kernel**, **/proc/meminfo** nối từ **/proc/<PID>/maps và smaps** sang **/proc/loadavg**, vì cơ chế trước tạo đầu vào cho bước sau.

## `/proc/meminfo`

Trước khi chạy hoặc đọc ví dụ dưới đây, hãy xác định câu hỏi vận hành mà nó trả lời, dữ liệu nào sẽ quan sát được và giới hạn của kết quả. Lệnh chỉ có ý nghĩa khi gắn với một giả thuyết về state của hệ thống.

```bash
cat /proc/meminfo
```

`free` và nhiều công cụ (tool / 도구) khác đọc/diễn giải thông tin từ kernel. Các trường như `MemTotal`, `MemAvailable`, `Cached`, `SwapTotal`, `SwapFree` giúp quan sát bộ nhớ ở mức hệ thống.

Không nên tự tạo kết luận chỉ từ một trường. Ví dụ `Cached` lớn không có nghĩa bộ nhớ (memory / 메모리) leak.

Xem thêm: [Bộ nhớ và bộ nhớ ảo](../06_resources/memory_virtual_memory.md).

> **Nối mạch:** Trong **/proc, /sys và giao diện quan sát kernel**, **/proc/loadavg** nối từ **/proc/meminfo** sang **/proc/net**, vì cơ chế trước tạo đầu vào cho bước sau.

## `/proc/loadavg`

Trước khi chạy hoặc đọc ví dụ dưới đây, hãy xác định câu hỏi vận hành mà nó trả lời, dữ liệu nào sẽ quan sát được và giới hạn của kết quả. Lệnh chỉ có ý nghĩa khi gắn với một giả thuyết về state của hệ thống.

```bash
cat /proc/loadavg
```

Cho thấy tải trung bình và một số thông tin về runnable tasks/tiến trình (process / 프로세스) count.

Công cụ (tool / 도구) `uptime` trình bày cùng loại dữ liệu theo cách dễ đọc hơn, nhưng hiểu `/proc/loadavg` giúp thấy công cụ (tool / 도구) user-space lấy trạng thái (state / 상태) từ đâu.

> **Nối mạch:** Ở chặng này của **/proc, /sys và giao diện quan sát kernel**, **/proc/net** nối từ **/proc/loadavg** sang **/proc/sys: tham số kernel thời gian chạy (runtime / 런타임)**, vì cơ chế trước tạo đầu vào cho bước sau.

## `/proc/net`

Một phần thông tin mạng cũng được expose dưới `/proc/net`, nhưng trong thực tế nên ưu tiên các công cụ (tool / 도구) hiện đại như `ss`, `ip`, `nstat` vì chúng diễn giải netlink/kernel trạng thái (state / 상태) tốt hơn và ổn định hơn cho người vận hành.

> **Nối mạch:** Đặt trong câu hỏi lớn của **/proc, /sys và giao diện quan sát kernel**, **/proc/sys: tham số kernel thời gian chạy (runtime / 런타임)** nối từ **/proc/net** sang **/sys: mô hình thiết bị và kernel đối tượng (object / 객체)**, vì cơ chế trước tạo đầu vào cho bước sau.

## `/proc/sys`: tham số kernel thời gian chạy (runtime / 런타임)

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

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

```bash
sudo sysctl -w net.ipv4.ip_forward=1
```

Thay đổi này ảnh hưởng thời gian chạy (runtime / 런타임) hiện tại nhưng có thể mất sau reboot nếu không được cấu hình persistent.

### Thay đổi persistent

Thông thường cấu hình nằm trong các tệp (file / 파일) như:

```text
/etc/sysctl.conf
/etc/sysctl.d/*.conf
```

sau đó tải (load / 로드) bằng cơ chế phù hợp:

```bash
sudo sysctl --system
```

Không nên bản sao (copy / 복사) các “kernel tuning” từ internet vào môi trường vận hành (production / 운영 환경) mà không biết tải công việc (workload / 워크로드), kernel phiên bản (version / 버전) và sự đánh đổi (trade-off / 트레이드오프). Một giá trị tốt cho cơ sở dữ liệu (database / 데이터베이스) host có thể không phù hợp với ứng dụng (application / 애플리케이션) máy chủ (server / 서버) hoặc bộ chứa (container / 컨테이너) host.

> **Nối mạch:** Trong **/proc, /sys và giao diện quan sát kernel**, **/sys: mô hình thiết bị và kernel đối tượng (object / 객체)** nối từ **/proc/sys: tham số kernel thời gian chạy (runtime / 런타임)** sang **/dev: thiết bị (device / 장치) nodes và mối quan hệ với kernel**, vì cơ chế trước tạo đầu vào cho bước sau.

## `/sys`: mô hình thiết bị và kernel đối tượng (object / 객체)

`/sys` (sysfs) trình bày các thiết bị và kernel objects theo cấu trúc phân cấp.

Ví dụ:

```bash
ls /sys/class/net
ls /sys/block
ls /sys/devices
```

### Mạng (network / 네트워크) giao diện (interface / 인터페이스)

Trước khi chạy hoặc đọc ví dụ dưới đây, hãy xác định câu hỏi vận hành mà nó trả lời, dữ liệu nào sẽ quan sát được và giới hạn của kết quả. Lệnh chỉ có ý nghĩa khi gắn với một giả thuyết về state của hệ thống.

```bash
cat /sys/class/net/eth0/mtu
cat /sys/class/net/eth0/operstate
```

Có thể nhìn trạng thái và thuộc tính giao diện (interface / 인터페이스).

### Khối (block / 블록) thiết bị (device / 장치)

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

```bash
ls /sys/block/sda
```

Thông tin hàng đợi (queue / 큐), scheduler và thiết bị (device / 장치) relationships có thể được expose ở đây.

Các công cụ (tool / 도구) như `lsblk`, `udevadm`, `ip` thường dễ dùng hơn, nhưng `/sys` giúp hiểu dữ liệu gốc.

> **Nối mạch:** Ở chặng này của **/proc, /sys và giao diện quan sát kernel**, **/dev: thiết bị (device / 장치) nodes và mối quan hệ với kernel** nối từ **/sys: mô hình thiết bị và kernel đối tượng (object / 객체)** sang **udev và thiết bị động**, vì cơ chế trước tạo đầu vào cho bước sau.

## `/dev`: thiết bị (device / 장치) nodes và mối quan hệ với kernel

`/dev` chứa thiết bị (device / 장치) nodes, không phải thiết bị vật lý theo nghĩa “tệp (file / 파일) nằm trên disk”. thiết bị (device / 장치) nút (node / 노드) là giao diện để user-space tương tác với driver/kernel subsystem.

Ví dụ:

```text
/dev/null
/dev/zero
/dev/random
/dev/sda
/dev/tty
```

`/dev/null` không lưu dữ liệu. `/dev/tty` đại diện terminal phù hợp với tiến trình. `/dev/sda` đại diện khối (block / 블록) thiết bị (device / 장치) nếu hệ thống đặt tên như vậy.

Đây là lý do câu “everything is a tệp (file / 파일)” nên được hiểu là **nhiều tài nguyên (resource / 자원) có thể dùng giao diện file-like**, không phải mọi thứ đều là regular tệp (file / 파일).

> **Nối mạch:** Đặt trong câu hỏi lớn của **/proc, /sys và giao diện quan sát kernel**, **udev và thiết bị động** nối từ **/dev: thiết bị (device / 장치) nodes và mối quan hệ với kernel** sang **Khi nào nên đọc trực tiếp /proc hoặc /sys?**, vì cơ chế trước tạo đầu vào cho bước sau.

## udev và thiết bị động

Linux hiện đại thường dùng `udev` để quản lý thiết bị (device / 장치) events và tạo các thiết bị (device / 장치) nodes/symlinks phù hợp trong `/dev`.

Khi gắn USB/lưu trữ (storage / 저장소)/mạng (network / 네트워크) thiết bị (device / 장치), kernel phát hiện hardware, driver tạo kernel thiết bị (device / 장치) đối tượng (object / 객체), rồi user-space thiết bị (device / 장치) manager xử lý chính sách (policy / 정책)/naming.

Có thể quan sát:

```bash
udevadm info --query=all --name=/dev/sda
```

hoặc monitor events:

```bash
udevadm monitor
```

Không nên chạy monitor vô thời hạn trên môi trường vận hành (production / 운영 환경) nếu chỉ cần một kiểm tra ngắn; nó có thể tạo rất nhiều đầu ra (output / 출력).

> **Nối mạch:** Trong **/proc, /sys và giao diện quan sát kernel**, **Khi nào nên đọc trực tiếp /proc hoặc /sys?** nối từ **udev và thiết bị động** sang **Ví dụ: điều tra tiến trình Java bị nghi rò rỉ tệp (file / 파일) descriptor**, vì cơ chế trước tạo đầu vào cho bước sau.

## Khi nào nên đọc trực tiếp `/proc` hoặc `/sys`?

Các công cụ (tool / 도구) chuẩn thường nên được ưu tiên vì dễ đọc hơn:

```bash
ps
ss
ip
free
lsblk
systemctl
```

Nhưng `/proc` và `/sys` trở nên rất giá trị khi:

- công cụ (tool / 도구) không hiển thị trường bạn cần;
- cần xác minh trạng thái thật của một PID cụ thể;
- viết diagnostic script nhẹ;
- muốn hiểu công cụ (tool / 도구) user-space đang lấy dữ liệu ở đâu;
- bộ chứa (container / 컨테이너)/minimal ảnh (image / 이미지) không có nhiều tiện ích.

> **Nối mạch:** Ở chặng này của **/proc, /sys và giao diện quan sát kernel**, **Khi nào nên đọc trực tiếp /proc hoặc /sys?** nêu quy tắc; **Ví dụ: điều tra tiến trình Java bị nghi rò rỉ tệp (file / 파일) descriptor** thử quy tắc trong tình huống, rồi **Những hiểu lầm phổ biến** mở rộng hệ quả.

## Ví dụ: điều tra tiến trình Java bị nghi rò rỉ tệp (file / 파일) descriptor

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

Nếu số descriptor tăng qua mỗi lần đo, hãy phân loại: socket, tệp (file / 파일), pipe hay deleted tệp (file / 파일).

Chỉ khi có bằng chứng (evidence / 증거) về xu hướng mới chuyển sang mã (code / 코드)/thời gian chạy (runtime / 런타임) phân tích (analysis / 분석).

> **Nối mạch:** Đặt trong câu hỏi lớn của **/proc, /sys và giao diện quan sát kernel**, **Ví dụ: điều tra tiến trình Java bị nghi rò rỉ tệp (file / 파일) descriptor** nêu quy tắc; **Những hiểu lầm phổ biến** thử quy tắc trong tình huống, rồi **Mô hình tư duy** mở rộng hệ quả.

## Những hiểu lầm phổ biến

**“`/proc` là thư mục thật trên ổ đĩa.”** Không. Nó là pseudo-filesystem do kernel sinh động.

**“Sửa tệp (file / 파일) trong `/proc/sys` là persistent.”** Thường không. Muốn giữ qua reboot cần cấu hình sysctl persistent.

**“Có thể chỉnh sysctl để tăng hiệu năng mà không có rủi ro.”** Sai. Kernel tuning luôn có sự đánh đổi (trade-off / 트레이드오프) và phụ thuộc tải công việc (workload / 워크로드).

**“`/sys` chỉ dành cho kernel nhà phát triển (developer / 개발자).”** Không. Operator vẫn có thể dùng nó để hiểu thiết bị (device / 장치) trạng thái (state / 상태), nhưng nên ưu tiên công cụ (tool / 도구) cấp cao khi có.

**“Mọi thứ dưới `/proc/<PID>` luôn đọc được.”** Quyền, bảo mật (security / 보안) chính sách (policy / 정책) và kernel settings có thể hạn chế truy cập.

> **Nối mạch:** Trong **/proc, /sys và giao diện quan sát kernel**, **Mô hình tư duy** tổng hợp từ **Những hiểu lầm phổ biến** thành một kết luận có thể mang sang phần kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Mô hình tư duy

Hãy xem `/proc` và `/sys` như hai bản đồ khác nhau của cùng hệ thống:

- `/proc` nhấn mạnh **tiến trình và trạng thái thời gian chạy (runtime / 런타임)**;
- `/sys` nhấn mạnh **thiết bị và mô hình kernel đối tượng (object / 객체)**;
- `/dev` cung cấp **điểm tương tác với thiết bị (device / 장치)/tài nguyên (resource / 자원)**.

Ba khu vực này tạo một cầu nối quan trọng giữa lý thuyết kernel và công việc vận hành thực tế.

Xem thêm: [Kernel, user space và system calls](./kernel_userspace_syscalls.md), [Process, thread và signal](../04_process/processes_threads_signals_jobs.md), [Storage và filesystem](../06_resources/storage_filesystems.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
