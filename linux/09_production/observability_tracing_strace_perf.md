# Quan sát sâu hệ thống: strace, perf và tracing

Khi log ứng dụng không đủ, bước tiếp theo không nhất thiết là thêm `DEBUG` rồi restart. Linux cung cấp nhiều cơ chế để quan sát một tiến trình đang làm gì ở ranh giới kernel, đang tiêu CPU ở đâu và đang chờ loại tài nguyên nào.

Các công cụ như `strace`, `perf`, `pidstat`, `lsof`, `ss` và eBPF-based tools mở rộng khả năng quan sát mà không cần sửa code ngay lập tức.

## Tracing khác logging như thế nào?

Logging là dữ liệu ứng dụng chủ động phát ra. Tracing cấp hệ điều hành có thể quan sát hành vi ngay cả khi application không log.

Ví dụ application chỉ báo:

```text
request timeout
```

Nhưng tracing có thể giúp phân biệt:

- process đang `connect()` mãi tới dependency;
- đọc file config bị `EACCES`;
- gọi `futex()` nhiều vì lock contention;
- liên tục `stat()` hàng nghìn file;
- `read()` từ socket trả chậm;
- CPU đang bị consume trong một function cụ thể.

## `strace`: quan sát lời gọi hệ thống

`strace` theo dõi system calls và signals của process.

Chạy một command dưới strace:

```bash
strace ls /tmp
```

Output khá dài vì một chương trình đơn giản vẫn cần load libraries, inspect locale, mở directory và ghi output.

Do đó nên filter.

### Theo dõi file-related calls

```bash
strace -e trace=file cat /etc/hosts
```

Hoặc cụ thể:

```bash
strace -e openat,read,write,close cat /etc/hosts
```

### Theo dõi network

```bash
strace -e trace=network curl -s https://example.com >/dev/null
```

Có thể thấy `socket()`, `connect()`, `sendto()`, `recvfrom()` hoặc calls liên quan.

## Attach vào tiến trình đang chạy

```bash
sudo strace -p 1234
```

Điều này attach debugger-like observer vào process hiện tại.

Cần thận trọng trên production. `strace` có overhead, đặc biệt với process có syscall rate cao.

Nên:

- trace trong thời gian ngắn;
- filter syscalls;
- ghi output ra file;
- tránh attach hàng loạt threads nếu không cần.

Ví dụ:

```bash
sudo timeout 10s strace -tt -T -p 1234 -e trace=network -o /tmp/strace-net.txt
```

`-tt` thêm timestamp chi tiết. `-T` cho thời gian syscall. `timeout` giới hạn tracing 10 giây.

## `-f` và multi-thread/process

```bash
strace -f command
```

`-f` theo child processes/threads phù hợp theo implementation.

Với Java, output có thể rất lớn vì JVM có nhiều threads. Chỉ dùng khi thực sự cần và nên filter mạnh.

## Đọc lỗi syscall

Ví dụ:

```text
openat(..., "/opt/app/config.yml", O_RDONLY) = -1 EACCES (Permission denied)
```

Đây là evidence rất trực tiếp: kernel từ chối open với `EACCES`.

Nếu application framework chỉ báo “failed to load configuration”, strace giúp xuống đúng layer.

Các errno thường gặp:

- `ENOENT` — object/path component không tồn tại;
- `EACCES` — bị từ chối quyền;
- `ECONNREFUSED` — kết nối bị từ chối;
- `ETIMEDOUT` — timeout;
- `EMFILE` — process hết file descriptor limit;
- `ENOSPC` — không còn space/resource tương ứng.

## Khi strace cho thấy `futex()` rất nhiều

`futex` là primitive kernel thường được runtime sử dụng để xây mutex/condition synchronization.

Nếu Java process bị hang và strace chỉ thấy nhiều `futex`, điều đó không tự động nghĩa kernel lỗi. Có thể threads đang chờ lock/condition.

Bước tiếp theo thường là thread dump:

```bash
jcmd <PID> Thread.print
```

Hệ điều hành cho thấy “đang chờ synchronization”; JVM cho biết Java monitor/stack nào liên quan.

Đây là ví dụ kết hợp hai tầng observability.

## `perf`: quan sát CPU execution

`perf` dùng kernel performance subsystem để thu thập hardware/software counters và sampling profiles.

Các command cơ bản:

```bash
perf stat command
```

có thể báo CPU cycles, instructions, context switches và counters khác tùy quyền/hardware.

Sampling process:

```bash
sudo perf top -p 1234
```

hoặc record:

```bash
sudo perf record -F 99 -p 1234 -g -- sleep 30
sudo perf report
```

`-F 99` sampling khoảng 99 Hz. `-g` cố thu call graph.

## Sampling thay vì trace mọi event

`strace` có thể observe gần như từng syscall, còn `perf` thường sampling CPU instruction execution.

Sampling chấp nhận không thấy mọi event để đổi lấy overhead thấp hơn và profile thống kê.

Đây là cùng tư duy với statistics: không cần đo mọi instruction để biết phần lớn CPU time tập trung ở đâu.

## Java và perf

JIT làm Java profiling ở OS level phức tạp hơn native binary vì code được sinh runtime. Tooling như async-profiler thường phù hợp hơn cho JVM và có thể dùng perf events bên dưới.

Khi Java high CPU, một workflow tốt có thể là:

```text
pidstat/top xác định PID
    ↓
pidstat -t xác định thread
    ↓
JVM thread dump / async-profiler
    ↓
perf nếu cần OS/native-level evidence
```

Không nên bắt đầu bằng tool phức tạp nhất.

## `pidstat`: bridge giữa metrics và tracing

```bash
pidstat -p 1234 1
pidstat -t -p 1234 1
pidstat -d -p 1234 1
pidstat -w -p 1234 1
```

Tùy version, các option cho CPU, thread, I/O và context-switch view.

`pidstat` có overhead thấp và rất phù hợp làm bước đầu trước `strace`/`perf`.

## `lsof`: object relationship tracing

`lsof` không phải performance tracer nhưng cực kỳ hữu ích để trả lời “process đang giữ cái gì?”

```bash
sudo lsof -p 1234
```

Có thể thấy:

- files;
- sockets;
- pipes;
- shared libraries;
- current working directory;
- deleted-open files.

Đây là cách nối process model với filesystem/network model.

## `ss`: trạng thái socket

```bash
sudo ss -antp
```

Cho thấy TCP states và process association khi đủ quyền.

Khi application báo connection pool exhaustion, nhìn số `ESTAB`, `CLOSE-WAIT`, `SYN-SENT` có thể tạo thêm hypothesis.

## `/proc/<PID>/stack` và kernel stack

Trong một số điều kiện/quyền:

```bash
sudo cat /proc/1234/stack
```

có thể cho kernel stack của task.

Nếu process ở `D` state, kernel stack đôi khi cho thấy nó đang chờ block I/O, NFS hoặc driver path nào.

Đây là diagnostic nâng cao, cần hiểu symbol/kernel context trước khi kết luận.

## eBPF là gì?

**eBPF (extended Berkeley Packet Filter)** cho phép chạy các chương trình được kernel kiểm chứng tại các hook points khác nhau để thu thập/biến đổi telemetry với overhead tương đối thấp trong nhiều use case.

Các toolsets như BCC hoặc bpftrace có thể quan sát:

- syscall latency;
- block I/O latency;
- TCP retransmission;
- scheduler latency;
- file opens;
- function probes.

Ví dụ bpftrace syntax có thể giống:

```bash
sudo bpftrace -e 'tracepoint:syscalls:sys_enter_openat { @[comm] = count(); }'
```

Nhưng availability phụ thuộc kernel, permissions và package.

## Vì sao eBPF mạnh nhưng không nên dùng mù quáng?

Nó cho visibility sâu, nhưng:

- cần quyền cao;
- có version/kernel dependencies;
- query sai có thể tạo overhead;
- output dễ bị diễn giải sai nếu không hiểu kernel path.

Senior không phải người luôn dùng eBPF; senior chọn **công cụ ít phức tạp nhất đủ để phân biệt giả thuyết**.

## Off-CPU analysis

CPU profiling chỉ cho nơi process chạy. Nhưng latency có thể đến từ nơi process **không chạy** vì đang chờ lock, disk, network hoặc scheduler.

Off-CPU analysis quan sát thời gian thread bị blocked/sleeping.

Đây là lý do API latency cao nhưng CPU thấp không nên kết luận “server còn khỏe”.

Một hệ thống có thể dành 95% thời gian chờ database và chỉ 5% CPU.

## Flame graph

Flame graph là cách trực quan hóa stack samples.

Chiều ngang biểu diễn tỷ lệ samples; chiều dọc là call stack depth. Một vùng rộng nghĩa function/path xuất hiện trong nhiều samples.

Không nên đọc chiều ngang như timeline. Flame graph truyền thống là distribution, không phải trình tự thời gian.

## Tracing trong distributed systems

OS tracing cho biết process/kernel behavior trên một host. Distributed tracing như OpenTelemetry cho biết request path giữa services.

Hai loại bổ sung nhau:

```text
Distributed trace: request chậm ở service B
                     ↓
Host tracing: service B chậm vì network connect / disk / CPU / lock
```

## Methodology: từ rẻ đến sâu

Một quy trình tốt thường đi từ low-overhead tới high-detail:

```text
metrics/logs
↓
ps / ss / lsof / pidstat
↓
/proc inspection
↓
strace ngắn và filtered
↓
perf / JVM profiler
↓
eBPF / kernel-level deep tracing
```

Không phải incident nào cũng cần xuống cuối.

## Ví dụ: Java service latency cao nhưng CPU thấp

Bắt đầu:

```bash
pidstat -p <PID> 1
sudo ss -antp | grep <PID>
jcmd <PID> Thread.print
```

Nếu nhiều threads chờ socket read tới DB, có thể trace network syscalls ngắn:

```bash
sudo timeout 5s strace -tt -T -f -p <PID> -e trace=network -o /tmp/net.trace
```

Nếu evidence cho thấy `connect()` hoặc `recvfrom()` delay, chuyển investigation sang dependency/network path thay vì tăng JVM CPU.

## Những hiểu lầm phổ biến

**“strace không thấy application function nên vô dụng.”** Nó nhìn syscall boundary, rất mạnh để phân biệt filesystem/network/permission/resource issues.

**“perf luôn nhẹ và an toàn.”** Sampling vẫn có overhead; call graph/unwind có thể tăng chi phí.

**“Nhiều futex nghĩa kernel bug.”** Thường đó là synchronization behavior của runtime/application.

**“CPU profile giải thích mọi latency.”** Không. Off-CPU waiting có thể chiếm phần lớn thời gian.

**“eBPF là công cụ phải dùng nếu muốn được coi là senior.”** Sai. Tool choice phải dựa trên câu hỏi và information gain.

## Mô hình tư duy

Quan sát hệ thống có nhiều độ sâu:

```text
application logs        → application nói gì
metrics                 → hệ thống đang thay đổi ra sao
/proc, ss, lsof         → runtime objects đang ở trạng thái nào
strace                  → process đang yêu cầu kernel điều gì
perf/profile            → CPU đang chạy code ở đâu
eBPF/kernel tracing     → event path sâu trong kernel/runtime
```

Chọn layer đủ để trả lời câu hỏi hiện tại, không chọn tool vì nó “nâng cao”.

Xem thêm: [Production troubleshooting](./production_troubleshooting.md), [Java backend incident playbook](./java_backend_incident_playbook.md), [`/proc` và `/sys`](../00_foundations/proc_sysfs_kernel_interfaces.md).