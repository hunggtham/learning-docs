# Linux Kernel Scheduler: CPU thời gian (time / 시간), Run hàng đợi (queue / 큐) và Scheduling Classes

> **Mạch đọc:** Đọc **Linux Kernel Scheduler: CPU thời gian (time / 시간), Run hàng đợi (queue / 큐) và Scheduling Classes** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **CPU cốt lõi (core / 핵심) không chạy vô hạn threads cùng lúc** sang **Runnable khác running**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Khi một máy chủ (server / 서버) có nhiều tiến trình (process / 프로세스) và luồng (thread) hơn số CPU có thể thực thi đồng thời, kernel phải quyết định **ai được chạy trước, chạy trong bao lâu và trên CPU nào**. Cơ chế đó là **bộ lập lịch (scheduler)**.

Hiểu scheduler giúp giải thích những hiện tượng như:

- CPU 100% nhưng thông lượng (throughput / 처리량) không tăng;
- tải (load / 로드) average cao dù một số CPU vẫn idle;
- một tiến trình (process / 프로세스) có nhiều luồng thực thi (thread / 스레드) nhưng chỉ dùng một cốt lõi (core / 핵심);
- bộ chứa (container / 컨테이너) bị CPU throttling dù host còn CPU;
- độ trễ (latency / 지연 시간) tăng mạnh khi runnable hàng đợi (queue / 큐) dài;
- nice giá trị (value / 값) thay đổi nhưng ứng dụng (application / 애플리케이션) vẫn không đạt hành vi (behavior / 동작) kỳ vọng.

## CPU cốt lõi (core / 핵심) không chạy vô hạn threads cùng lúc

Một logical CPU tại một thời điểm chỉ thực thi một thực thi (execution / 실행) ngữ cảnh (context / 맥락) thông thường. Nếu có 100 runnable threads trên 8 logical CPUs, scheduler phải chia CPU thời gian (time / 시간) giữa chúng.

Mô hình tư duy (mental model / 사고 모델) đơn giản:

```text
runnable tasks
    ↓
run queue
    ↓
scheduler selects tasks
    ↓
logical CPUs execute
```

Các tác vụ (task / 작업) không runnable vì đang chờ mạng (network / 네트워크), disk, khóa (lock / 잠금) hoặc timer không cạnh tranh CPU theo cùng cách.

## Runnable khác running

Một tác vụ (task / 작업) có thể ở nhiều trạng thái.

**Running** nghĩa đang thực thi trên CPU.

**Runnable** nghĩa sẵn sàng chạy nhưng đang chờ CPU.

Nếu runnable tasks tăng nhanh hơn CPU sức chứa (capacity / 용량), hàng đợi (queue / 큐) chờ CPU dài hơn và độ trễ (latency / 지연 시간) tăng.

`vmstat` cung cấp trường dữ liệu (field / 필드) `r`:

```bash
vmstat 1
```

`r` phản ánh số tasks runnable theo sampling.

Nếu host có 4 CPUs và `r` liên tục 30–40 cùng `%us/%sy` cao, CPU contention là hypothesis đáng chú ý.

## Scheduler không chỉ có một thuật toán

Linux có nhiều **scheduling classes** phục vụ tải công việc (workload / 워크로드) khác nhau.

Các nhóm concept thường gặp:

- normal/fair scheduling;
- real-time FIFO;
- real-time round-robin;
- deadline scheduling;
- idle policies.

Ứng dụng (application / 애플리케이션) máy chủ (server / 서버) thông thường chạy trong fair scheduling lớp (class / 클래스). Real-time scheduling cần đặc quyền và hiểu sâu vì có thể starve các tasks khác.

Không nên dùng real-time priority để “làm app nhanh hơn” nếu chưa hiểu hệ thống (system / 시스템) impact.

## CFS và fair scheduling

Trong nhiều năm, Linux normal scheduling được gắn với **CFS — Completely Fair Scheduler**. Kernel versions mới tiếp tục phát triển scheduler hiện thực (implementation / 구현), nhưng mô hình tư duy (mental model / 사고 모델) công bằng theo CPU thời gian (time / 시간) vẫn hữu ích.

Mục tiêu không phải chia mỗi luồng thực thi (thread / 스레드) đúng một lát thời gian bằng nhau trong mọi trường hợp, mà cân bằng thực thi (execution / 실행) dựa scheduling weight, runnable tasks và nhiều heuristics khác.

Nice giá trị (value / 값) ảnh hưởng weight của normal scheduling.

## Nice giá trị (value / 값)

Kiểm tra:

```bash
ps -o pid,ni,pri,cmd -p <PID>
```

Chạy tiến trình (process / 프로세스) với nice giá trị (value / 값) cao hơn:

```bash
nice -n 10 long-job
```

Nice cao hơn thường nghĩa priority tương đối thấp hơn trong normal scheduler.

Thay đổi tiến trình (process / 프로세스) đang chạy:

```bash
renice 10 -p <PID>
```

Nice không phải hard CPU percentage.

Nếu chỉ có một runnable tiến trình (process / 프로세스) trên CPU, dù nice thấp ưu tiên hơn hay cao ít ưu tiên hơn, nó vẫn có thể dùng gần toàn bộ CPU vì không có ai cạnh tranh.

Đây là lý do nice giá trị (value / 값) không tương đương cgroup Giới hạn CPU (CPU limit / CPU 제한).

## Priority là quan hệ tương đối

Giả sử hai CPU-bound processes cùng cạnh tranh một CPU.

Tiến trình (process / 프로세스) A có scheduling weight cao hơn B. Scheduler cố cho A tỷ lệ CPU lớn hơn theo chính sách (policy / 정책).

Nhưng nếu B là I/O-bound và ngủ phần lớn thời gian, A vẫn dùng phần CPU còn lại.

Vì vậy priority có ý nghĩa trong **contention ngữ cảnh (context / 맥락)**, không phải quota tuyệt đối.

## Thời gian (time / 시간) slice

Scheduler cho tác vụ (task / 작업) chạy một khoảng thời gian rồi có thể preempt để tác vụ (task / 작업) khác chạy.

Thời gian (time / 시간) slice không nên được hiểu như một con số cố định universal cho mọi Linux kernel/tải công việc (workload / 워크로드).

Scheduler quyết định dựa trên chính sách (policy / 정책) và runnable set.

Điểm quan trọng là nhiều runnable tasks dẫn tới frequent ngữ cảnh (context / 맥락) switching và mỗi tác vụ (task / 작업) nhận CPU theo lượt.

## Preemption

**Preemption** nghĩa kernel có thể dừng một tác vụ (task / 작업) đang chạy để tác vụ (task / 작업) khác được chọn.

Tác vụ (task / 작업) có priority phù hợp hoặc scheduler fairness có thể khiến switch xảy ra.

Linux kernel còn có preemption các mô hình (models / 모델들) khác nhau ảnh hưởng độ trễ (latency / 지연 시간) đặc biệt trong desktop, máy chủ (server / 서버) và real-time kernels.

Môi trường vận hành (production / 운영 환경) backend thường không cần chỉnh kernel preemption mô hình (model / 모델) trừ khi có yêu cầu (requirement / 요구사항) rất đặc thù.

## Ngữ cảnh (context / 맥락) switch

Khi CPU chuyển từ tác vụ (task / 작업) A sang tác vụ (task / 작업) B, hệ thống (system / 시스템) phải lưu/khôi phục thực thi (execution / 실행) ngữ cảnh (context / 맥락).

Ngữ cảnh (context / 맥락) switching có chi phí (cost / 비용):

- registers;
- scheduler bookkeeping;
- CPU bộ nhớ đệm (cache / 캐시) locality;
- TLB/bộ nhớ đệm (cache / 캐시) effects.

Quan sát:

```bash
vmstat 1
```

Trường dữ liệu (field / 필드) `cs` cho ngữ cảnh (context / 맥락) switches theo interval.

`pidstat`:

```bash
pidstat -w 1
```

có thể cho voluntary/nonvoluntary ngữ cảnh (context / 맥락) switches theo tiến trình (process / 프로세스).

Không có universal threshold “ngữ cảnh (context / 맥락) switch bao nhiêu là xấu”. Cần baseline và tải công việc (workload / 워크로드) ngữ cảnh (context / 맥락).

## Voluntary và involuntary ngữ cảnh (context / 맥락) switch

**Voluntary ngữ cảnh (context / 맥락) switch** thường xảy ra khi tác vụ (task / 작업) tự khối (block / 블록)/chờ tài nguyên (resource / 자원).

Ví dụ:

```text
thread → read socket → chưa có data → sleep
```

**Involuntary ngữ cảnh (context / 맥락) switch** có thể xảy ra khi scheduler preempt tác vụ (task / 작업) đang chạy để tác vụ (task / 작업) khác chạy.

Nếu involuntary switches tăng mạnh cùng CPU saturation, runnable contention có thể là một hypothesis.

Nếu voluntary switches cao, ứng dụng (application / 애플리케이션) có thể chờ I/O/locks nhiều.

## CPU affinity

Kernel thường có thể di chuyển tasks giữa CPUs để cân bằng tải (load / 로드).

CPU affinity giới hạn tác vụ (task / 작업) vào CPU set:

```bash
taskset -pc <PID>
```

Set affinity:

```bash
taskset -cp 0-3 <PID>
```

Affinity có thể tăng bộ nhớ đệm (cache / 캐시) locality trong một số specialized workloads, nhưng pinning sai có thể làm một vài cores overloaded trong khi cores khác idle.

Không nên pin JVM threads/whole tiến trình (process / 프로세스) chỉ dựa cảm giác.

## Tải (load / 로드) balancing giữa CPU cores

Scheduler cố phân phối runnable tasks giữa CPUs.

Nhưng topology phần cứng không hoàn toàn đồng nhất:

- hyperthreads cùng vật lý (physical / 물리적) cốt lõi (core / 핵심) chia sẻ thực thi (execution / 실행) resources;
- NUMA nodes có bộ nhớ (memory / 메모리) locality khác nhau;
- CPU caches có hierarchy riêng.

Vì vậy “8 CPUs” không luôn nghĩa 8 units có hiệu năng (performance / 성능) độc lập hoàn toàn.

## Hyper-Threading / SMT

**SMT — Simultaneous Multithreading** cho phép một vật lý (physical / 물리적) cốt lõi (core / 핵심) expose nhiều logical CPUs.

Hai sibling logical CPUs chia sẻ một phần resources của cốt lõi (core / 핵심).

Do đó 8 logical CPUs trên 4 vật lý (physical / 물리적) cores không luôn cho thông lượng (throughput / 처리량) gấp đôi 4 cores.

Xem topology:

```bash
lscpu -e
```

hoặc:

```bash
lscpu
```

Fields về cốt lõi (core / 핵심), Socket, luồng thực thi (thread / 스레드) giúp hiểu topology.

## NUMA và scheduling

Trên multi-socket servers, bộ nhớ (memory / 메모리) truy cập (access / 접근) tới cục bộ (local / 로컬) NUMA nút (node / 노드) thường nhanh hơn remote nút (node / 노드).

Scheduler và bộ nhớ (memory / 메모리) allocator cố quan tâm locality, nhưng tác vụ (task / 작업) di chuyển (migration / 마이그레이션) có thể làm working set xa bộ nhớ (memory / 메모리).

Xem:

```bash
numactl --hardware
```

nếu công cụ (tool / 도구) được cài.

NUMA tuning là advanced topic và cần đo đạc. Bind CPU/bộ nhớ (memory / 메모리) sai có thể làm độ trễ (latency / 지연 시간) tệ hơn.

## Real-time scheduling

Linux có scheduling policies như `SCHED_FIFO` và `SCHED_RR`.

Real-time tasks có thể preempt normal tasks mạnh hơn.

Xem scheduling chính sách (policy / 정책):

```bash
chrt -p <PID>
```

Chạy real-time tác vụ (task / 작업) cần quyền phù hợp.

Sai cấu hình real-time có thể làm hệ thống (system / 시스템) khó responsive vì high-priority tác vụ (task / 작업) không chịu nhường CPU.

Backend web thông thường không nên chuyển sang real-time scheduling để “giảm độ trễ (latency / 지연 시간)” nếu chưa có hard real-time yêu cầu (requirement / 요구사항).

## Scheduler và interrupt

CPU không chỉ chạy người dùng (user / 사용자) threads. Kernel còn xử lý interrupts, softirqs và mạng (network / 네트워크)/lưu trữ (storage / 저장소) công việc (work / 작업).

High mạng (network / 네트워크) packet tỷ lệ (rate / 비율) có thể làm `%system` tăng dù ứng dụng (application / 애플리케이션) nghiệp vụ (business / 비즈니스) mã (code / 코드) không tăng nhiều.

Check:

```bash
cat /proc/interrupts
```

Công cụ (tool / 도구) như:

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

Manual IRQ pinning chỉ nên dùng khi có benchmark/low-latency yêu cầu (requirement / 요구사항) rõ ràng.

## Softirq và mạng (network / 네트워크) tải (load / 로드)

Linux mạng (network / 네트워크) ngăn xếp (stack / 스택) xử lý nhiều công việc qua softirq.

Xem:

```bash
cat /proc/softirqs
```

Nếu `NET_RX` tăng mạnh trên một CPU, mạng (network / 네트워크) processing có thể là nguồn hệ thống (system / 시스템) CPU.

Đây là lý do CPU bottleneck không luôn nằm trong ứng dụng (application / 애플리케이션) luồng thực thi (thread / 스레드) dump.

## Run hàng đợi (queue / 큐) và độ trễ (latency / 지연 시간)

Giả sử một yêu cầu (request / 요청) cần 5 ms CPU thời gian (time / 시간).

Khi CPU gần idle, yêu cầu (request / 요청) có thể chạy gần như ngay.

Khi hàng chục runnable tasks cạnh tranh, yêu cầu (request / 요청) phải chờ nhiều scheduling rounds.

Nghiệp vụ (business / 비즈니스) mã (code / 코드) vẫn chỉ cần 5 ms CPU, nhưng wall-clock độ trễ (latency / 지연 시간) có thể lớn hơn nhiều.

Đây là lý do CPU saturation thường làm tail độ trễ (latency / 지연 시간) tăng trước khi thông lượng (throughput / 처리량) collapse hoàn toàn.

## Tail độ trễ (latency / 지연 시간)

Average độ trễ (latency / 지연 시간) có thể nhìn ổn trong khi p99 tăng mạnh.

Khi scheduler hàng đợi (queue / 큐) dài, một số requests gặp nhiều wait thời gian (time / 시간) hơn requests khác.

Môi trường vận hành (production / 운영 환경) dịch vụ (service / 서비스) cần theo dõi:

- p50;
- p95;
- p99;
- max;
- CPU saturation;
- runnable hàng đợi (queue / 큐).

Không nên chỉ dùng average CPU/độ trễ (latency / 지연 시간).

## CPU steal thời gian (time / 시간) trong VM

Trong virtual machine, hypervisor có thể không cho VM chạy dù guest có runnable tasks.

Chỉ số (metric / 지표) `steal` (`%st`) phản ánh một phần thời gian CPU bị hypervisor dành cho VM khác.

Xem bằng:

```bash
top
vmstat 1
mpstat 1
```

Nếu `%st` cao, guest tuning có thể không giải quyết host-level contention.

Đây là ví dụ bottleneck nằm ngoài Linux guest.

## CPU quota trong cgroup

Bộ chứa (container / 컨테이너) Giới hạn CPU (CPU limit / CPU 제한) thường dùng cgroup quota/weight.

Một bộ chứa (container / 컨테이너) có thể thấy host có nhiều CPUs nhưng chỉ được quota tương đương 1 CPU.

Nếu ứng dụng (application / 애플리케이션) dùng hết quota, kernel throttles group.

Cgroup v2 có tệp (file / 파일) như:

```text
cpu.max
cpu.stat
```

Tùy đường dẫn (path / 경로)/thời gian chạy (runtime / 런타임).

CPU throttling có thể gây độ trễ (latency / 지연 시간) spikes dù host CPU tổng thể chưa 100%.

## CPU yêu cầu (request / 요청) và limit trong Kubernetes

Kubernetes CPU yêu cầu (request / 요청) ảnh hưởng scheduling; Giới hạn CPU (CPU limit / CPU 제한) thường map tới cgroup quota tùy thời gian chạy (runtime / 런타임)/cấu hình (configuration / 구성).

Một pod Java có limit thấp có thể bị throttled trong burst dù nút (node / 노드) còn idle sức chứa (capacity / 용량) theo cách nhìn tổng.

Đây là lý do cần xem cả nút (node / 노드) CPU và pod cgroup metrics.

## Java luồng thực thi (thread / 스레드) pool và scheduler

Java ứng dụng (application / 애플리케이션) có thể có 200 worker threads trên 4 CPUs.

Nếu tải công việc (workload / 워크로드) CPU-bound, 200 threads không làm 4 CPUs thành 200 CPUs. Chúng chỉ tạo nhiều runnable tasks hơn, tăng switching/queueing.

Nếu tải công việc (workload / 워크로드) I/O-bound, nhiều threads có thể hữu ích vì một số threads ngủ chờ I/O.

Optimal luồng thực thi (thread / 스레드) count phụ thuộc ratio CPU/wait và kiến trúc (architecture / 아키텍처).

## Công thức gần đúng cho luồng thực thi (thread / 스레드) pool I/O-bound

Một heuristic thường được nhắc:

\[
N \approx C \times \left(1 + \frac{W}{S}\right)
\]

trong đó:

- `N`: số threads gần đúng;
- `C`: số CPUs;
- `W`: thời gian chờ;
- `S`: thời gian dùng CPU (service time).

Đây chỉ là mô hình (model / 모델) gần đúng, không phải công thức cấu hình môi trường vận hành (production / 운영 환경) tuyệt đối.

Nếu `W/S` lớn, nhiều threads có thể giúp giữ CPU bận trong khi luồng thực thi (thread / 스레드) khác chờ.

Nhưng cơ sở dữ liệu (database / 데이터베이스) liên kết (connection / 연결) pool, bộ nhớ (memory / 메모리)/luồng thực thi (thread / 스레드) ngăn xếp (stack / 스택) và downstream limits cũng là các ràng buộc (constraints / 제약조건들).

## Luồng thực thi (thread / 스레드) ngăn xếp (stack / 스택) và bộ nhớ (memory / 메모리)

Mỗi Java luồng thực thi (thread / 스레드) có ngăn xếp (stack / 스택) bộ nhớ (memory / 메모리). Tạo quá nhiều threads không chỉ ảnh hưởng scheduler mà còn bộ nhớ (memory / 메모리).

Do đó tuning luồng thực thi (thread / 스레드) pool phải nhìn:

```text
CPU
+ context switches
+ memory/thread stack
+ downstream capacity
+ queue length
```

Không tối ưu một dimension riêng lẻ.

## CPU-bound tải công việc (workload / 워크로드)

Ví dụ ảnh (image / 이미지) compression/encryption/calculation.

Nếu 8 CPU cores và 100 compute threads, runnable hàng đợi (queue / 큐) có thể rất dài.

Thông lượng (throughput / 처리량) thường tốt hơn với tính đồng thời (concurrency / 동시성) gần CPU sức chứa (capacity / 용량) cộng một ít overhead thay vì hàng trăm threads.

ForkJoinPool/work-stealing runtimes cố giải quyết một phần scheduling ở ứng dụng (application / 애플리케이션) tầng (layer / 계층), nhưng kernel vẫn là scheduler cuối cùng cho OS threads.

## I/O-bound tải công việc (workload / 워크로드)

Web backend thường dành nhiều thời gian chờ:

- DB truy vấn (query / 쿼리);
- mạng (network / 네트워크) API;
- disk;
- locks.

Threads sleeping không dùng CPU, vì vậy luồng thực thi (thread / 스레드) count có thể lớn hơn CPU count.

Nhưng nếu downstream chậm, tất cả threads có thể bị occupied và hàng đợi (queue / 큐) incoming requests tăng.

Lúc đó tăng threads có thể chỉ tạo thêm tải (load / 로드) xuống downstream.

## Scheduler và tranh chấp khóa (lock contention / 잠금 경합)

Hai threads tranh cùng mutex có thể bị khối (block / 블록)/wake liên tục.

CPU không nhất thiết 100%, nhưng thông lượng (throughput / 처리량) thấp vì serialization.

Công cụ (tool / 도구) Java luồng thực thi (thread / 스레드) dump có thể thấy many threads `BLOCKED` hoặc waiting locks.

Linux `perf lock`/futex tracing có thể dùng trong advanced diagnosis.

Tranh chấp khóa (lock contention / 잠금 경합) là reminder rằng “luồng thực thi (thread / 스레드) runnable” và “công việc (work / 작업) parallelizable” không giống nhau.

## Futex

Linux **futex (fast userspace mutex)** hỗ trợ nhiều synchronization primitives.

Uncontended khóa (lock / 잠금) có thể xử lý phần lớn ở người dùng (user / 사용자) không gian (space / 공간); contention cần kernel wait/wake.

`strace` có thể thấy:

```text
futex(...)
```

rất nhiều khi ứng dụng (application / 애플리케이션) có khóa (lock / 잠금)/điều kiện (condition / 조건) waits.

Không nên kết luận futex là lỗi chỉ vì xuất hiện nhiều; JVM synchronization naturally dùng futex.

## Gỡ lỗi (debug / 디버그) CPU saturation

Bước đầu:

```bash
uptime
nproc
mpstat -P ALL 1
vmstat 1
```

Xác định:

- all CPUs busy hay một CPU?
- người dùng (user / 사용자)/hệ thống (system / 시스템)/steal?
- runnable hàng đợi (queue / 큐)?

Tiến trình (process / 프로세스) mức (level / 수준):

```bash
pidstat -u 1
```

Luồng thực thi (thread / 스레드) mức (level / 수준):

```bash
pidstat -t -p <PID> 1
```

Java:

```bash
jcmd <PID> Thread.print
```

Bản địa (native / 네이티브) profiling:

```bash
perf top
```

Nếu `%system` cao, cần xem syscalls/mạng (network / 네트워크)/I/O chứ không chỉ Java ngăn xếp (stack / 스택).

## One-core bottleneck

Ứng dụng (application / 애플리케이션) có thể có tiến trình (process / 프로세스) CPU ~100% trên 16-core host. Trên Linux tools, 100% thường tương ứng một logical CPU, tùy công cụ (tool / 도구) convention.

Nếu ứng dụng (application / 애플리케이션) single-threaded đường xử lý nóng (hot path / 핫 패스), tổng host CPU chỉ ~6% nhưng yêu cầu (request / 요청) độ trễ (latency / 지연 시간) vẫn bottleneck.

Xem per-thread/per-CPU thay vì chỉ host aggregate.

## CPU frequency scaling

Hiện đại (modern / 현대적) CPU thay đổi frequency theo power/thermal conditions.

`lscpu`/sysfs/cpupower có thể expose frequency chính sách (policy / 정책).

Thermal throttling hoặc power chính sách (policy / 정책) có thể làm hiệu năng (performance / 성능) khác giữa hai servers cùng cốt lõi (core / 핵심) count.

Sức chứa (capacity / 용량) planning không nên chỉ đếm vCPU.

## Mô hình tư duy (mental model / 사고 모델)

CPU hiệu năng (performance / 성능) nên được nhìn như hệ thống hàng đợi (queue / 큐):

```text
incoming runnable work
      ↓
per-CPU / scheduler run queues
      ↓
logical CPUs
      ↓
completed CPU service
```

Nếu arrival CPU công việc (work / 작업) vượt CPU dịch vụ (service / 서비스) sức chứa (capacity / 용량), hàng đợi (queue / 큐) tăng và độ trễ (latency / 지연 시간) tăng.

Scheduler quyết định **chia CPU như thế nào**, nhưng không thể tạo thêm compute sức chứa (capacity / 용량).

## Những hiểu lầm phổ biến

**“Nice 10 nghĩa chỉ dùng 10% CPU.”** Nice là relative priority/weight, không phải quota.

**“Nhiều threads hơn luôn nhanh hơn.”** Với CPU-bound công việc (work / 작업), quá nhiều threads tăng hàng đợi (queue / 큐)/context-switch chi phí (cost / 비용).

**“CPU tổng 50% nghĩa không thể có CPU bottleneck.”** Một single-thread đường xử lý nóng (hot path / 핫 패스) có thể saturate một cốt lõi (core / 핵심).

**“Host còn CPU thì bộ chứa (container / 컨테이너) không bị Giới hạn CPU (CPU limit / CPU 제한).”** Cgroup quota có thể throttle riêng bộ chứa (container / 컨테이너).

**“tải (load / 로드) average cao luôn nghĩa CPU 100%.”** Linux tải (load / 로드) còn tính một số uninterruptible tasks.

**“ngữ cảnh (context / 맥락) switch cao chắc chắn là lỗi.”** Cần baseline và tải công việc (workload / 워크로드) ngữ nghĩa (semantics / 의미론).

## Xem thêm

Các liên kết này là bước bàn giao sang cơ chế liên quan. Hãy mở chúng theo câu hỏi còn bỏ ngỏ, không coi danh sách link là phần kết luận tự thân.

- [CPU, scheduling và performance](./cpu_scheduling_performance.md)
- [Memory và virtual memory](./memory_virtual_memory.md)
- [I/O performance](./io_performance.md)
- [Namespace, cgroup và seccomp](../09_production/namespaces_cgroups_seccomp.md)
- [Java backend incident playbook](../09_production/java_backend_incident_playbook.md)
- [Capacity planning](../09_production/capacity_planning_server_sizing.md)

> **Bàn giao:** Sau **Xem thêm**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [block layer io scheduler](./block_layer_io_scheduler.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
