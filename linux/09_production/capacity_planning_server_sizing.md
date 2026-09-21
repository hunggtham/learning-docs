# Capacity Planning, Server Sizing và Headroom trong Production

Một server có thể “chạy được” nhưng vẫn được sizing sai. Nếu sizing quá nhỏ, latency và error rate tăng khi traffic burst. Nếu sizing quá lớn, chi phí cao và bottleneck thật có thể nằm ở database hoặc dependency khác.

**Capacity planning** là quá trình ước lượng và kiểm chứng lượng tài nguyên cần thiết để workload đạt mục tiêu về throughput, latency, reliability và cost.

Đây không phải bài toán chọn “CPU bao nhiêu core, RAM bao nhiêu GB” một lần rồi kết thúc. Capacity là quan hệ giữa workload và toàn bộ chuỗi tài nguyên.

## Bắt đầu từ workload, không bắt đầu từ hardware

Nếu chỉ hỏi:

```text
server nên có bao nhiêu CPU?
```

thì chưa đủ thông tin.

Cần biết:

- request rate;
- request cost;
- concurrency;
- response size;
- database calls/request;
- memory working set;
- traffic burst pattern;
- latency SLO;
- growth rate;
- failure/redundancy requirement.

Hai applications cùng 100 requests/second có thể cần tài nguyên khác nhau hàng chục lần.

## Throughput và latency

**Throughput** là lượng work hoàn thành trên đơn vị thời gian.

Ví dụ:

```text
1000 requests/second
```

**Latency** là thời gian để một unit work hoàn thành.

Ví dụ:

```text
p95 = 120 ms
p99 = 350 ms
```

Capacity planning production thường phải giữ cả hai trong mục tiêu.

Tăng concurrency có thể tăng throughput đến một điểm, sau đó queueing làm latency tăng mạnh.

## Utilization không nên luôn ở 100%

Một batch job có thể tận dụng CPU gần 100% và vẫn ổn.

Một web API cần phản ứng với burst thường cần **headroom**.

Nếu normal traffic đã dùng 95% CPU, một burst nhỏ hoặc GC spike có thể đẩy system vào saturation.

Headroom là phần capacity chưa dùng trong trạng thái bình thường để hấp thụ biến động và failure.

Không có một tỷ lệ headroom universal cho mọi hệ thống.

## Capacity khác với utilization snapshot

Một server CPU 30% lúc 03:00 không chứng minh server dư 70% capacity.

Cần nhìn:

- peak hour;
- daily/weekly pattern;
- p95/p99 utilization;
- burst duration;
- seasonal traffic;
- deployment/backup jobs;
- node failure scenarios.

Capacity planning dựa time series, không dựa một snapshot.

## Little's Law

Trong hệ thống tương đối ổn định:

\[
L = \lambda W
\]

trong đó:

- `L`: số requests/work items trung bình đang ở trong system;
- `λ`: throughput/arrival rate;
- `W`: thời gian trung bình trong system.

Ví dụ nếu service xử lý 1000 request/s và average latency 100 ms:

\[
L = 1000 \times 0.1 = 100
\]

nghĩa trung bình có khoảng 100 requests đang in-flight.

Nếu latency tăng lên 1 giây mà throughput vẫn 1000/s, số in-flight work tăng lên khoảng 1000.

Điều này giải thích tại sao latency degradation kéo theo thread/socket/memory pressure.

## Service time và queueing

Latency có thể tách gần đúng thành:

\[
W = W_q + S
\]

trong đó:

- `Wq`: thời gian chờ queue;
- `S`: thời gian thực sự được phục vụ.

Khi resource utilization gần saturation, queue wait có thể tăng nhanh dù service time không thay đổi nhiều.

Đó là lý do tail latency thường xấu đi mạnh trước khi system hoàn toàn fail.

## CPU sizing

CPU sizing cần biết CPU time/request.

Giả sử benchmark cho thấy mỗi request cần trung bình:

```text
2 ms CPU
```

và target:

```text
2000 requests/s
```

CPU demand gần đúng:

\[
2000 \times 0.002 = 4 CPU-seconds/second
\]

nghĩa workload cần khoảng 4 CPU cores ở 100% utilization lý tưởng.

Nhưng production cần thêm headroom, kernel overhead, GC, uneven traffic và tail behavior.

Có thể target 6–8 vCPU tùy benchmark/architecture thay vì đúng 4.

Đây chỉ là model khởi đầu. CPU architecture và cloud vCPU performance khác nhau.

## vCPU không phải unit performance tuyệt đối

Một vCPU ở cloud instance A không chắc bằng vCPU ở instance B.

Khác biệt có thể đến từ:

- CPU generation;
- clock frequency;
- SMT topology;
- noisy neighbor;
- burst credit model;
- virtualization overhead.

Capacity phải benchmark trên instance family thật nếu performance quan trọng.

## CPU saturation signals

Các dấu hiệu:

```bash
mpstat -P ALL 1
vmstat 1
pidstat -u 1
```

Cần xem:

- CPU utilization;
- runnable queue;
- steal time;
- per-core imbalance;
- cgroup throttling.

CPU 80% không tự động nghĩa chỉ còn 20% capacity vì tail latency có thể bắt đầu tăng trước 100%.

## Memory sizing

RAM không nên sizing chỉ bằng heap size.

Với Java service, tổng memory có thể gồm:

```text
Java heap
+ metaspace
+ thread stacks
+ code cache
+ direct buffers
+ native libraries
+ JVM internal structures
+ page cache
+ OS/kernel memory
```

Nếu container limit 4 GiB và `-Xmx4g`, gần như không còn headroom cho native memory.

Đây là cấu hình dễ OOMKill.

## Heap headroom

Giả sử container memory limit:

```text
8 GiB
```

Không nhất thiết set:

```text
-Xmx8g
```

Có thể cần để một phần cho native memory và page cache. Tỷ lệ phù hợp phụ thuộc JVM/workload.

Theo dõi RSS, native memory tracking và cgroup memory thay vì chỉ heap metrics.

## Page cache là capacity hữu ích

Linux sử dụng RAM dư cho page cache.

Một service đọc nhiều files hoặc database local có thể hưởng lợi từ cache.

Sizing RAM quá sát process RSS có thể làm cache bị reclaim liên tục, tăng disk I/O và latency.

Vì vậy RAM headroom không nhất thiết là “lãng phí”.

## Swap trong capacity planning

Swap có thể giúp tránh immediate OOM trong một số workloads, nhưng heavy swap thường gây latency lớn.

Service latency-sensitive không nên dựa swap như normal capacity.

Quan sát:

```bash
vmstat 1
```

Sustained swap in/out (`si/so`) là signal pressure.

## Storage capacity có nhiều dimensions

Disk sizing không chỉ là GB.

Các dimensions:

- capacity (GB/TB);
- IOPS;
- throughput MB/s;
- latency;
- queue depth;
- inode count;
- durability;
- burst credits ở cloud disks.

Một 1 TB disk có thể không đủ performance nếu workload cần nhiều random IOPS.

## IOPS sizing

Nếu một request gây trung bình 5 random storage operations và service cần 1000 requests/s:

```text
~5000 IOPS
```

chưa tính background writes, logs, compaction, backups.

Nếu provisioned disk chỉ 3000 IOPS, storage có thể thành bottleneck dù còn rất nhiều free space.

## Sequential và random I/O

Sequential workload thường tối ưu throughput MB/s.

Random small-block workload thường bị giới hạn IOPS/latency.

Capacity test phải giống workload pattern thật.

`dd` sequential benchmark không đại diện database random I/O đầy đủ.

## Network sizing

Network capacity cần xem:

- requests/s;
- request bytes;
- response bytes;
- protocol overhead;
- replication traffic;
- backup traffic;
- TLS overhead;
- peak burst.

Ví dụ response trung bình 100 KB với 1000 requests/s:

```text
100 MB/s application payload
≈ 800 Mbps trước overhead
```

Một interface 1 Gbps có thể đã gần saturation sau overhead và traffic khác.

## Packet rate cũng quan trọng

Network không chỉ giới hạn bandwidth Mbps/Gbps.

Rất nhiều small packets có thể giới hạn packets per second, interrupt/softirq CPU hoặc conntrack.

Một API trả 1 KB ở 100k req/s có bandwidth không quá lớn nhưng packet rate và connection handling rất cao.

## Connection capacity

Mỗi TCP connection dùng:

- kernel socket structures;
- send/receive buffers;
- file descriptors;
- application state.

Một server có 100k idle connections có resource profile khác 100 active requests.

Cần xem:

```bash
ss -s
cat /proc/sys/fs/file-nr
```

và process limits.

## File descriptor capacity

Nếu service cần nhiều sockets/files đồng thời, `nofile` limit phải đủ.

```bash
cat /proc/<PID>/limits
```

Nhưng tăng FD limit không giải quyết leak. Nếu descriptors tăng vô hạn, root cause là lifecycle bug.

## Thread capacity

Thread count ảnh hưởng:

- memory stack;
- scheduling;
- context switches;
- lock contention.

Một server “còn RAM” không nghĩa có thể tăng thread pool vô hạn.

Thread pool sizing phải dựa CPU/wait ratio và downstream capacity.

## Database connection pool

Backend capacity thường bị giới hạn bởi DB connections trước CPU.

Giả sử 10 application instances, mỗi instance pool 100:

```text
10 × 100 = 1000 DB connections
```

Nếu database chỉ chịu tốt 300 active connections, scale app horizontal có thể làm DB tệ hơn.

Capacity planning phải end-to-end.

## Dependency budget

Mỗi dependency có capacity riêng:

```text
API instance
 → database
 → Redis
 → downstream API
 → message broker
```

Scale layer A không tự scale B.

Đây là lý do load test phải quan sát toàn graph chứ không chỉ service đang test.

## Horizontal scaling

Thêm instances tăng tổng capacity khi workload có thể phân phối.

Ví dụ:

```text
1 instance = 500 req/s
4 instances ≠ chắc chắn 2000 req/s
```

Có thể bị giới hạn bởi:

- DB;
- shared cache;
- network;
- load balancer;
- lock/global state.

Scale-out efficiency cần đo.

## Vertical scaling

Thêm CPU/RAM cho một server đơn giản hơn về architecture, nhưng có giới hạn hardware và tăng blast radius khi node fail.

Một JVM heap quá lớn cũng làm GC behavior khác.

Vertical và horizontal scaling là trade-off, không phải “cloud luôn scale horizontal”.

## N+1 capacity

Nếu cluster có 4 nodes và cần chịu mất 1 node mà không vi phạm SLO, normal traffic không nên cần 100% tổng capacity 4 nodes.

N+1 planning:

```text
capacity của 3 nodes >= peak required capacity
```

Điều này tạo redundancy headroom.

Nếu normal load mỗi node đã 90%, mất một node sẽ làm ba node còn lại quá tải.

## Availability Zone failure

Multi-AZ architecture cần cân capacity theo failure domain.

Nếu có 3 AZ và requirement chịu mất 1 AZ, hai AZ còn lại phải đủ capacity.

Không chỉ có instance count; database/network dependency cũng cần redundancy tương ứng.

## Autoscaling

Autoscaling thêm/bớt instances dựa metrics.

Nhưng scaling có delay:

```text
metric detects load
 → policy triggers
 → VM/container starts
 → application warms up
 → health check passes
 → receives traffic
```

Nếu traffic spike nhanh hơn startup time, autoscaling phản ứng quá chậm.

Cần baseline capacity/headroom trước khi autoscaling cứu được hệ thống.

## Scale metric

CPU là metric phổ biến nhưng không luôn đúng.

Một service I/O-bound có CPU 20% nhưng thread pool/DB connections exhausted.

Alternative metrics:

- request queue length;
- concurrency;
- latency;
- custom work backlog;
- messages in queue.

Scaling metric nên phản ánh bottleneck/resource demand thật.

## Load testing

Capacity plan chỉ là hypothesis cho tới khi được test.

Load test nên mô phỏng:

- realistic request mix;
- realistic data sizes;
- authentication;
- think time nếu có;
- dependency behavior;
- warm-up;
- cache state;
- ramp-up và burst.

Một benchmark endpoint `/health` không đại diện business API.

## Warm-up

JVM cần thời gian JIT compile, cache warm-up, connection pools và filesystem cache.

Load test ngay từ cold start có thể đo startup behavior thay vì steady-state capacity.

Nhưng production có rolling deploy/cold start, nên cả hai scenarios đều cần test tùy requirement.

## Coordinated omission

Load-testing tools có thể báo latency quá đẹp nếu khi server chậm, tool cũng giảm request generation và bỏ qua requests lẽ ra đã đến.

Hiện tượng này gọi là **coordinated omission**.

Một test tốt phải hiểu traffic model và measurement semantics.

## Percentile thay vì average

Average latency che tail.

Ví dụ:

```text
99 requests = 10 ms
1 request   = 5 s
```

Average vẫn có thể trông không quá lớn, nhưng user bị request 5 giây rất rõ.

Theo dõi p95/p99/p99.9 khi SLO cần.

## SLO và error budget

Capacity không chỉ để “không crash”, mà để đạt Service Level Objective.

Ví dụ:

```text
99.9% requests < 500 ms
availability 99.95%
```

Server có thể vẫn trả response nhưng p99 3s — theo SLO vẫn là capacity problem.

## Growth planning

Nếu traffic tăng 10% mỗi tháng, server đủ hôm nay có thể thiếu sau vài tháng.

Projection đơn giản:

\[
C_{future} = C_{now}(1+g)^n
\]

với `g` là growth rate theo kỳ.

Đây chỉ là model nếu growth tương đối ổn định. Product launch/event có thể tạo step change.

## Capacity trend

Theo dõi:

```text
peak CPU
peak memory
request rate
p99 latency
DB connections
IOPS
network bandwidth
error rate
```

theo tuần/tháng giúp phát hiện approaching limit trước incident.

## Saturation metric

USE method thường gợi ý xem mỗi resource theo:

- Utilization;
- Saturation;
- Errors.

Ví dụ CPU:

```text
utilization → % busy
saturation  → run queue
errors      → hiếm theo nghĩa hardware/system
```

Disk:

```text
utilization → busy time
saturation  → queue/await
errors      → I/O errors
```

Mental model này tốt hơn chỉ một metric utilization.

## RED method ở service layer

Với request-driven service, RED thường nhìn:

- Rate;
- Errors;
- Duration.

Kết hợp RED ở service layer với USE ở resource layer giúp nối symptom business với bottleneck Linux.

## Capacity worksheet thực tế

Một worksheet có thể gồm:

```text
Peak request rate:
Average / p95 request CPU time:
Average response bytes:
Peak concurrency:
DB queries/request:
DB connection pool:
Heap steady-state:
RSS peak:
Disk IOPS peak:
Network peak:
Required failure tolerance:
Growth 6 months:
Target headroom:
```

Sau đó kiểm chứng bằng load test và production metrics.

## Case: Java API CPU 70%, p99 tăng

Không nên kết luận ngay cần thêm CPU.

Kiểm tra:

```bash
vmstat 1
mpstat -P ALL 1
pidstat -t -p <PID> 1
```

Nếu runnable queue cao và CPUs đều busy, CPU contention mạnh.

Nếu CPU 70% nhưng thread dump cho thấy nhiều threads chờ DB, bottleneck có thể là connection pool/database.

Capacity planning cần đúng resource.

## Case: RAM luôn 90%

Nếu 90% bao gồm page cache và `MemAvailable` còn tốt, chưa chắc memory pressure.

Nếu cgroup memory gần limit, swap/reclaim mạnh hoặc OOM events xuất hiện, capacity mới thực sự nguy hiểm.

Không dùng “RAM used %” đơn lẻ.

## Case: Scale từ 2 lên 8 app instances nhưng throughput không tăng

Potential shared bottleneck:

- database CPU/locks;
- DB max connections;
- Redis single-thread hotspot;
- downstream API rate limit;
- load balancer limit;
- storage IOPS.

Scale application chỉ tăng load xuống bottleneck chung.

## Cost-performance

Capacity tốt không đồng nghĩa resource tối đa.

Mục tiêu có thể là:

```text
cost per 1000 requests
```

hoặc:

```text
throughput per vCPU
```

Profiling/tuning application có thể rẻ hơn tăng instance count.

Nhưng optimization engineering cũng có cost. Cần balance.

## Mô hình tư duy (Mental Model)

Capacity planning là bài toán dòng chảy:

```text
workload arrival
      ↓
queues
      ↓
CPU / memory / I/O / network
      ↓
dependencies
      ↓
completed work
```

Mỗi resource có capacity và saturation point.

Khi một resource đạt giới hạn, queue/latency/error thường tăng trước khi toàn hệ thống “down”.

## Những hiểu lầm phổ biến

**“CPU trung bình 50% nghĩa server dư một nửa.”** Peak, tail latency và single-core bottleneck có thể khác.

**“RAM dùng cao là thiếu RAM.”** Page cache và reclaimable memory phải được tính.

**“Scale app instances luôn tăng throughput tuyến tính.”** Shared dependencies có thể trở thành bottleneck.

**“Autoscaling loại bỏ nhu cầu capacity planning.”** Scaling có delay và vẫn phụ thuộc upstream limits.

**“Disk đủ GB nghĩa storage đủ capacity.”** IOPS, throughput và latency cũng là capacity dimensions.

**“Load test một endpoint là đủ.”** Request mix và dependency behavior phải đại diện production.

**“Server không crash nghĩa sizing đúng.”** SLO về latency/error có thể đã bị vi phạm từ lâu.

## Xem thêm

- [Kernel scheduler deep dive](../06_resources/kernel_scheduler_deep_dive.md)
- [Memory và virtual memory](../06_resources/memory_virtual_memory.md)
- [I/O performance](../06_resources/io_performance.md)
- [Reverse proxy và load balancing](../07_networking/reverse_proxy_load_balancing.md)
- [Java backend incident playbook](./java_backend_incident_playbook.md)
- [Production troubleshooting](./production_troubleshooting.md)
