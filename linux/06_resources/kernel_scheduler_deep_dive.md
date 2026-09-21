# Linux Kernel Scheduler: CPU Time, Run Queue và Scheduling Classes

Khi một server có nhiều tiến trình (process) và luồng (thread) hơn số CPU có thể thực thi đồng thời, kernel phải quyết định **ai được chạy trước, chạy trong bao lâu và trên CPU nào**. Cơ chế đó là **bộ lập lịch (scheduler)**.

Hiểu scheduler giúp giải thích những hiện tượng như:

- CPU 100% nhưng throughput không tăng;
- load average cao dù một số CPU vẫn idle;
- một process có nhiều thread nhưng chỉ dùng một core;
- container bị CPU throttling dù host còn CPU;
- latency tăng mạnh khi runnable queue dài;
- nice value thay đổi nhưng application vẫn không đạt behavior kỳ vọng.

## CPU core không chạy vô hạn threads cùng lúc

Một logical CPU tại một thời điểm chỉ thực thi một execution context thông thường. Nếu có 100 runnable threads trên 8 logical CPUs, scheduler phải chia CPU time giữa chúng.

Mental model đơn giản:

```text
runnable tasks
    ↓
run queue
    ↓
scheduler selects tasks
    ↓
logical CPUs execute
```

Các task không runnable vì đang chờ network, disk, lock hoặc timer không cạnh tranh CPU theo cùng cách.

## Runnable khác running

Một task có thể ở nhiều trạng thái.

**Running** nghĩa đang thực thi trên CPU.

**Runnable** nghĩa sẵn sàng chạy nhưng đang chờ CPU.

Nếu runnable tasks tăng nhanh hơn CPU capacity, queue chờ CPU dài hơn và latency tăng.

`vmstat` cung cấp field `r`:

```bash
vmstat 1
```

`r` phản ánh số tasks runnable theo sampling.

Nếu host có 4 CPUs và `r` liên tục 30–40 cùng `%us/%sy` cao, CPU contention là hypothesis đáng chú ý.

## Scheduler không chỉ có một thuật toán

Linux có nhiều **scheduling classes** phục vụ workload khác nhau.

Các nhóm concept thường gặp:

- normal/fair scheduling;
- real-time FIFO;
- real-time round-robin;
- deadline scheduling;
- idle policies.

Application server thông thường chạy trong fair scheduling class. Real-time scheduling cần đặc quyền và hiểu sâu vì có thể starve các tasks khác.

Không nên dùng real-time priority để “làm app nhanh hơn” nếu chưa hiểu system impact.

## CFS và fair scheduling

Trong nhiều năm, Linux normal scheduling được gắn với **CFS — Completely Fair Scheduler**. Kernel versions mới tiếp tục phát triển scheduler implementation, nhưng mental model công bằng theo CPU time vẫn hữu ích.

Mục tiêu không phải chia mỗi thread đúng một lát thời gian bằng nhau trong mọi trường hợp, mà cân bằng execution dựa scheduling weight, runnable tasks và nhiều heuristics khác.

Nice value ảnh hưởng weight của normal scheduling.

## Nice value

Kiểm tra:

```bash
ps -o pid,ni,pri,cmd -p <PID>
```

Chạy process với nice value cao hơn:

```bash
nice -n 10 long-job
```

Nice cao hơn thường nghĩa priority tương đối thấp hơn trong normal scheduler.

Thay đổi process đang chạy:

```bash
renice 10 -p <PID>
```

Nice không phải hard CPU percentage.

Nếu chỉ có một runnable process trên CPU, dù nice thấp ưu tiên hơn hay cao ít ưu tiên hơn, nó vẫn có thể dùng gần toàn bộ CPU vì không có ai cạnh tranh.

Đây là lý do nice value không tương đương cgroup CPU limit.

## Priority là quan hệ tương đối

Giả sử hai CPU-bound processes cùng cạnh tranh một CPU.

Process A có scheduling weight cao hơn B. Scheduler cố cho A tỷ lệ CPU lớn hơn theo policy.

Nhưng nếu B là I/O-bound và ngủ phần lớn thời gian, A vẫn dùng phần CPU còn lại.

Vì vậy priority có ý nghĩa trong **contention context**, không phải quota tuyệt đối.

## Time slice

Scheduler cho task chạy một khoảng thời gian rồi có thể preempt để task khác chạy.

Time slice không nên được hiểu như một con số cố định universal cho mọi Linux kernel/workload.

Scheduler quyết định dựa trên policy và runnable set.

Điểm quan trọng là nhiều runnable tasks dẫn tới frequent context switching và mỗi task nhận CPU theo lượt.

## Preemption

**Preemption** nghĩa kernel có thể dừng một task đang chạy để task khác được chọn.

Task có priority phù hợp hoặc scheduler fairness có thể khiến switch xảy ra.

Linux kernel còn có preemption models khác nhau ảnh hưởng latency đặc biệt trong desktop, server và real-time kernels.

Production backend thường không cần chỉnh kernel preemption model trừ khi có requirement rất đặc thù.

## Context switch

Khi CPU chuyển từ task A sang task B, system phải lưu/khôi phục execution context.

Context switching có cost:

- registers;
- scheduler bookkeeping;
- CPU cache locality;
- TLB/cache effects.

Quan sát:

```bash
vmstat 1
```

field `cs` cho context switches theo interval.

`pidstat`:

```bash
pidstat -w 1
```

có thể cho voluntary/nonvoluntary context switches theo process.

Không có universal threshold “context switch bao nhiêu là xấu”. Cần baseline và workload context.

## Voluntary và involuntary context switch

**Voluntary context switch** thường xảy ra khi task tự block/chờ resource.

Ví dụ:

```text
thread → read socket → chưa có data → sleep
```

**Involuntary context switch** có thể xảy ra khi scheduler preempt task đang chạy để task khác chạy.

Nếu involuntary switches tăng mạnh cùng CPU saturation, runnable contention có thể là một hypothesis.

Nếu voluntary switches cao, application có thể chờ I/O/locks nhiều.

## CPU affinity

Kernel thường có thể di chuyển tasks giữa CPUs để cân bằng load.

CPU affinity giới hạn task vào CPU set:

```bash
taskset -pc <PID>
```

Set affinity:

```bash
taskset -cp 0-3 <PID>
```

Affinity có thể tăng cache locality trong một số specialized workloads, nhưng pinning sai có thể làm một vài cores overloaded trong khi cores khác idle.

Không nên pin JVM threads/whole process chỉ dựa cảm giác.

## Load balancing giữa CPU cores

Scheduler cố phân phối runnable tasks giữa CPUs.

Nhưng topology phần cứng không hoàn toàn đồng nhất:

- hyperthreads cùng physical core chia sẻ execution resources;
- NUMA nodes có memory locality khác nhau;
- CPU caches có hierarchy riêng.

Vì vậy “8 CPUs” không luôn nghĩa 8 units có performance độc lập hoàn toàn.

## Hyper-Threading / SMT

**SMT — Simultaneous Multithreading** cho phép một physical core expose nhiều logical CPUs.

Hai sibling logical CPUs chia sẻ một phần resources của core.

Do đó 8 logical CPUs trên 4 physical cores không luôn cho throughput gấp đôi 4 cores.

Xem topology:

```bash
lscpu -e
```

hoặc:

```bash
lscpu
```

Fields về Core, Socket, Thread giúp hiểu topology.

## NUMA và scheduling

Trên multi-socket servers, memory access tới local NUMA node thường nhanh hơn remote node.

Scheduler và memory allocator cố quan tâm locality, nhưng task migration có thể làm working set xa memory.

Xem:

```bash
numactl --hardware
```

nếu tool được cài.

NUMA tuning là advanced topic và cần đo đạc. Bind CPU/memory sai có thể làm latency tệ hơn.

## Real-time scheduling

Linux có scheduling policies như `SCHED_FIFO` và `SCHED_RR`.

Real-time tasks có thể preempt normal tasks mạnh hơn.

Xem scheduling policy:

```bash
chrt -p <PID>
```

Chạy real-time task cần quyền phù hợp.

Sai cấu hình real-time có thể làm system khó responsive vì high-priority task không chịu nhường CPU.

Backend web thông thường không nên chuyển sang real-time scheduling để “giảm latency” nếu chưa có hard real-time requirement.

## Scheduler và interrupt

CPU không chỉ chạy user threads. Kernel còn xử lý interrupts, softirqs và network/storage work.

High network packet rate có thể làm `%system` tăng dù application business code không tăng nhiều.

Check:

```bash
cat /proc/interrupts
```

Tool như:

```bash
mpstat -P ALL 1
```

cũng giúp thấy per-CPU usage.

Một NIC interrupt tập trung vào một CPU có thể tạo imbalance.

## IRQ affinity

Interrupt handling có affinity riêng trong một số configurations.

Hệ thống thường có `irqbalance` để phân phối interrupts.

```bash
systemctl status irqbalance
```

Manual IRQ pinning chỉ nên dùng khi có benchmark/low-latency requirement rõ ràng.

## Softirq và network load

Linux network stack xử lý nhiều công việc qua softirq.

Xem:

```bash
cat /proc/softirqs
```

Nếu `NET_RX` tăng mạnh trên một CPU, network processing có thể là nguồn system CPU.

Đây là lý do CPU bottleneck không luôn nằm trong application thread dump.

## Run queue và latency

Giả sử một request cần 5 ms CPU time.

Khi CPU gần idle, request có thể chạy gần như ngay.

Khi hàng chục runnable tasks cạnh tranh, request phải chờ nhiều scheduling rounds.

Business code vẫn chỉ cần 5 ms CPU, nhưng wall-clock latency có thể lớn hơn nhiều.

Đây là lý do CPU saturation thường làm tail latency tăng trước khi throughput collapse hoàn toàn.

## Tail latency

Average latency có thể nhìn ổn trong khi p99 tăng mạnh.

Khi scheduler queue dài, một số requests gặp nhiều wait time hơn requests khác.

Production service cần theo dõi:

- p50;
- p95;
- p99;
- max;
- CPU saturation;
- runnable queue.

Không nên chỉ dùng average CPU/latency.

## CPU steal time trong VM

Trong virtual machine, hypervisor có thể không cho VM chạy dù guest có runnable tasks.

Metric `steal` (`%st`) phản ánh một phần thời gian CPU bị hypervisor dành cho VM khác.

Xem bằng:

```bash
top
vmstat 1
mpstat 1
```

Nếu `%st` cao, guest tuning có thể không giải quyết host-level contention.

Đây là ví dụ bottleneck nằm ngoài Linux guest.

## CPU quota trong cgroup

Container CPU limit thường dùng cgroup quota/weight.

Một container có thể thấy host có nhiều CPUs nhưng chỉ được quota tương đương 1 CPU.

Nếu application dùng hết quota, kernel throttles group.

Cgroup v2 có file như:

```text
cpu.max
cpu.stat
```

Tùy path/runtime.

CPU throttling có thể gây latency spikes dù host CPU tổng thể chưa 100%.

## CPU request và limit trong Kubernetes

Kubernetes CPU request ảnh hưởng scheduling; CPU limit thường map tới cgroup quota tùy runtime/configuration.

Một pod Java có limit thấp có thể bị throttled trong burst dù node còn idle capacity theo cách nhìn tổng.

Đây là lý do cần xem cả node CPU và pod cgroup metrics.

## Java thread pool và scheduler

Java application có thể có 200 worker threads trên 4 CPUs.

Nếu workload CPU-bound, 200 threads không làm 4 CPUs thành 200 CPUs. Chúng chỉ tạo nhiều runnable tasks hơn, tăng switching/queueing.

Nếu workload I/O-bound, nhiều threads có thể hữu ích vì một số threads ngủ chờ I/O.

Optimal thread count phụ thuộc ratio CPU/wait và architecture.

## Công thức gần đúng cho thread pool I/O-bound

Một heuristic thường được nhắc:

\[
N \approx C \times \left(1 + \frac{W}{S}\right)
\]

trong đó:

- `N`: số threads gần đúng;
- `C`: số CPUs;
- `W`: thời gian chờ;
- `S`: thời gian dùng CPU (service time).

Đây chỉ là model gần đúng, không phải công thức cấu hình production tuyệt đối.

Nếu `W/S` lớn, nhiều threads có thể giúp giữ CPU bận trong khi thread khác chờ.

Nhưng database connection pool, memory/thread stack và downstream limits cũng là constraints.

## Thread stack và memory

Mỗi Java thread có stack memory. Tạo quá nhiều threads không chỉ ảnh hưởng scheduler mà còn memory.

Do đó tuning thread pool phải nhìn:

```text
CPU
+ context switches
+ memory/thread stack
+ downstream capacity
+ queue length
```

Không tối ưu một dimension riêng lẻ.

## CPU-bound workload

Ví dụ image compression/encryption/calculation.

Nếu 8 CPU cores và 100 compute threads, runnable queue có thể rất dài.

Throughput thường tốt hơn với concurrency gần CPU capacity cộng một ít overhead thay vì hàng trăm threads.

ForkJoinPool/work-stealing runtimes cố giải quyết một phần scheduling ở application layer, nhưng kernel vẫn là scheduler cuối cùng cho OS threads.

## I/O-bound workload

Web backend thường dành nhiều thời gian chờ:

- DB query;
- network API;
- disk;
- locks.

Threads sleeping không dùng CPU, vì vậy thread count có thể lớn hơn CPU count.

Nhưng nếu downstream chậm, tất cả threads có thể bị occupied và queue incoming requests tăng.

Lúc đó tăng threads có thể chỉ tạo thêm load xuống downstream.

## Scheduler và lock contention

Hai threads tranh cùng mutex có thể bị block/wake liên tục.

CPU không nhất thiết 100%, nhưng throughput thấp vì serialization.

Tool Java thread dump có thể thấy many threads `BLOCKED` hoặc waiting locks.

Linux `perf lock`/futex tracing có thể dùng trong advanced diagnosis.

Lock contention là reminder rằng “thread runnable” và “work parallelizable” không giống nhau.

## Futex

Linux **futex (fast userspace mutex)** hỗ trợ nhiều synchronization primitives.

Uncontended lock có thể xử lý phần lớn ở user space; contention cần kernel wait/wake.

`strace` có thể thấy:

```text
futex(...)
```

rất nhiều khi application có lock/condition waits.

Không nên kết luận futex là lỗi chỉ vì xuất hiện nhiều; JVM synchronization naturally dùng futex.

## Debug CPU saturation

Bước đầu:

```bash
uptime
nproc
mpstat -P ALL 1
vmstat 1
```

Xác định:

- all CPUs busy hay một CPU?
- user/system/steal?
- runnable queue?

Process level:

```bash
pidstat -u 1
```

Thread level:

```bash
pidstat -t -p <PID> 1
```

Java:

```bash
jcmd <PID> Thread.print
```

Native profiling:

```bash
perf top
```

Nếu `%system` cao, cần xem syscalls/network/I/O chứ không chỉ Java stack.

## One-core bottleneck

Application có thể có process CPU ~100% trên 16-core host. Trên Linux tools, 100% thường tương ứng một logical CPU, tùy tool convention.

Nếu application single-threaded hot path, tổng host CPU chỉ ~6% nhưng request latency vẫn bottleneck.

Xem per-thread/per-CPU thay vì chỉ host aggregate.

## CPU frequency scaling

Modern CPU thay đổi frequency theo power/thermal conditions.

`lscpu`/sysfs/cpupower có thể expose frequency policy.

Thermal throttling hoặc power policy có thể làm performance khác giữa hai servers cùng core count.

Capacity planning không nên chỉ đếm vCPU.

## Mô hình tư duy (Mental Model)

CPU performance nên được nhìn như hệ thống queue:

```text
incoming runnable work
      ↓
per-CPU / scheduler run queues
      ↓
logical CPUs
      ↓
completed CPU service
```

Nếu arrival CPU work vượt CPU service capacity, queue tăng và latency tăng.

Scheduler quyết định **chia CPU như thế nào**, nhưng không thể tạo thêm compute capacity.

## Những hiểu lầm phổ biến

**“Nice 10 nghĩa chỉ dùng 10% CPU.”** Nice là relative priority/weight, không phải quota.

**“Nhiều threads hơn luôn nhanh hơn.”** Với CPU-bound work, quá nhiều threads tăng queue/context-switch cost.

**“CPU tổng 50% nghĩa không thể có CPU bottleneck.”** Một single-thread hot path có thể saturate một core.

**“Host còn CPU thì container không bị CPU limit.”** Cgroup quota có thể throttle riêng container.

**“Load average cao luôn nghĩa CPU 100%.”** Linux load còn tính một số uninterruptible tasks.

**“Context switch cao chắc chắn là lỗi.”** Cần baseline và workload semantics.

## Xem thêm

- [CPU, scheduling và performance](./cpu_scheduling_performance.md)
- [Memory và virtual memory](./memory_virtual_memory.md)
- [I/O performance](./io_performance.md)
- [Namespace, cgroup và seccomp](../09_production/namespaces_cgroups_seccomp.md)
- [Java backend incident playbook](../09_production/java_backend_incident_playbook.md)
- [Capacity planning](../09_production/capacity_planning_server_sizing.md)
