# Scheduler internals, run queues và fairness/latency trade-offs

Operating system scheduler quyết định thread nào được chạy trên CPU nào, trong bao lâu và khi nào bị preempt. Ở foundation, ta thường thấy các tên như round-robin hoặc priority scheduling. Ở production kernel, vấn đề khó hơn nhiều vì scheduler phải cân bằng **throughput, latency, fairness, cache locality, power và multicore load** cùng lúc.

## Runnable không có nghĩa đang chạy

Một task thường ở một trong các trạng thái rộng: running, runnable, sleeping/blocked hoặc stopped. Runnable task đã sẵn sàng nhưng đang chờ CPU.

Scheduler chủ yếu quản lý tập runnable. Khi một task block vì I/O, mutex hoặc timer, nó rời run queue. Khi event xảy ra, kernel wake nó và đưa lại vào cấu trúc scheduling.

## Per-CPU run queue

Trên multicore, một global queue duy nhất tạo lock contention và phá locality. Kernel hiện đại thường có state scheduling theo CPU.

Per-CPU run queue giảm synchronization và giúp task tiếp tục trên CPU cũ để tận dụng warm caches. Nhưng nếu CPU A quá tải và CPU B rảnh, kernel cần **load balancing / task migration**.

Do đó scheduler luôn đứng giữa hai mục tiêu đối nghịch:

```text
keep task local  <---->  spread runnable work evenly
cache locality           load balance
```

## Fairness là khái niệm theo thời gian

Nếu có nhiều CPU-bound tasks cùng priority, scheduler cần chia CPU sao cho không task nào bị starvation. Một cách reasoning là mỗi task tích lũy lượng CPU time đã nhận; task được phục vụ ít hơn nên có cơ hội chạy tiếp.

Linux CFS lịch sử dùng khái niệm **virtual runtime** để xấp xỉ fairness theo trọng số. Cấu trúc cụ thể có thể thay đổi qua phiên bản kernel, nhưng mental model vẫn quan trọng: scheduler không chỉ quay vòng queue; nó cố theo dõi “ai đã nhận bao nhiêu phần CPU”.

## Interactive latency và CPU throughput

Một batch job compile lớn muốn throughput. UI thread hoặc request handler muốn được wake và chạy nhanh sau event.

Nếu time slice quá dài, context switch ít nhưng interactive latency tệ. Nếu quá ngắn, responsiveness tốt hơn nhưng overhead context switch/cache disruption tăng.

Scheduler phải dùng policy và heuristics để cân bằng, không có một quantum tối ưu cho mọi workload.

## Wake-up path

Khi network packet, disk completion hoặc futex wake đánh thức task, kernel phải chọn CPU và enqueue task.

Nếu CPU target đang chạy task priority thấp hơn hoặc wake-up policy cho rằng task mới cần latency tốt, scheduler có thể trigger preemption sớm.

Wake-up latency vì vậy phụ thuộc không chỉ application code mà còn interrupt handling, run queue state, CPU affinity và scheduler class.

## Context switch cost không chỉ là save registers

Kernel phải đổi execution context, address-space-related state khi cần, accounting và scheduler metadata. Direct register save/restore chỉ là một phần.

Lớn hơn nữa là **indirect cost**: cache working set của task cũ bị thay, branch predictor/TLB behavior thay và pipeline phải warm lại.

Vì vậy hệ thống có hàng nghìn runnable threads có thể chậm dù CPU utilization gần 100%: thời gian bị tiêu vào scheduling/working-set interference chứ không chỉ useful work.

## CPU affinity và pinning

Affinity giới hạn task vào một số CPU. Pinning có thể hữu ích cho latency-sensitive workload, NUMA locality hoặc benchmark ổn định.

Nhưng pinning sai có thể tạo hotspot: một CPU quá tải trong khi CPU khác rảnh. Nó cũng có thể làm scheduler mất khả năng migrate work khi workload thay đổi.

Rule thực tế: affinity là một control mạnh, không phải performance flag mặc định.

## Priority inversion

Task high-priority có thể chờ lock đang giữ bởi low-priority task. Nếu medium-priority tasks liên tục chiếm CPU, low-priority lock holder không được chạy để release lock. High-priority task bị trì hoãn gián tiếp bởi task priority thấp — priority inversion.

Real-time systems dùng cơ chế như **priority inheritance** để tạm nâng priority của lock holder. Đây là ví dụ scheduler và synchronization không thể reasoning tách rời.

## NUMA làm scheduling phức tạp hơn

Task có thể chạy trên CPU node 0 nhưng pages chủ yếu ở memory node 1. Migrate task sang node gần memory hoặc migrate pages về gần task đều có cost.

Scheduler/memory subsystem phải cân nhắc CPU balance và memory locality. Một hệ thống nhìn “CPU đều” nhưng remote memory access cao vẫn có thể latency tệ.

## Run queue saturation trong production

CPU utilization 100% chỉ nói core bận. Nếu mỗi core có nhiều runnable task chờ, queueing delay tăng nhanh.

Metric như run queue length, load average theo semantics của OS, scheduler latency và voluntary/involuntary context switches giúp phân biệt “CPU đang làm useful work” với “CPU đang là bottleneck queue”.

Đây là cầu nối trực tiếp tới queueing theory ở Software Systems.

## Mental Model

> Scheduler là **resource allocator theo thời gian trên nhiều CPU**. Nó không tối ưu một metric duy nhất; mọi quyết định đều trade fairness, response latency, migration cost và locality.

## Common Misconceptions

**“100% CPU nghĩa scheduler hoạt động tối ưu.”** Có thể hàng dài task đang chờ và tail latency rất cao.

**“Context switch cost chỉ vài registers.”** Working-set/cache/TLB disruption thường quan trọng hơn.

**“Pin thread vào CPU luôn nhanh hơn.”** Pinning có thể phá load balance và NUMA behavior nếu dùng thiếu context.

## Kết nối

Tiếp theo đọc [Memory pressure, reclaim và page faults](./02_memory_pressure_reclaim_and_page_faults.md). Ở tầng architecture, cache/NUMA giải thích locality cost; ở tầng software systems, run queue là một queueing system với arrival rate và service capacity.