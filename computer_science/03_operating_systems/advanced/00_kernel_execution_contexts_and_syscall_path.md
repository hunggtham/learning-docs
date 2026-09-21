# Kernel execution contexts và syscall path

Một syscall nhìn từ application như function call đặc biệt, nhưng phía dưới nó là boundary giữa user privilege và kernel privilege. Hiểu đường đi này giúp reasoning latency, blocking, security boundary và vì sao một API tưởng đơn giản có thể kích hoạt scheduler, filesystem, network stack hoặc device driver.

## User mode và kernel mode không phải hai process khác nhau

Khi thread gọi syscall, cùng logical thread chuyển execution privilege và stack/context theo cơ chế architecture/OS. Kernel xử lý request thay mặt thread đó. Nếu operation hoàn tất ngay, execution quay lại user mode; nếu phải chờ I/O hoặc lock, thread có thể sleep và scheduler chạy thread khác.

Vì vậy “kernel đang chạy” không có nghĩa luôn tồn tại một kernel thread riêng cho mỗi syscall.

## Syscall entry

Userspace wrapper chuẩn bị syscall number và arguments theo ABI rồi dùng instruction như `syscall`/`svc` tùy architecture. CPU chuyển privilege, save state cần thiết và nhảy vào entry point do kernel cấu hình.

Kernel entry code phải cẩn thận vì nó xử lý untrusted state từ userspace. Arguments như pointer không thể dereference tùy ý; kernel cần validation và copy helpers vì address có thể invalid hoặc thay đổi do concurrent behavior.

## Từ syscall tới subsystem

Một `read(fd, buf, n)` có thể đi qua:

```text
userspace wrapper
→ syscall entry
→ file descriptor lookup
→ VFS/file operation
→ page cache hoặc filesystem
→ block layer / driver nếu cache miss
→ device completion
→ wakeup
→ copy/return to userspace
```

Đường thực tế phụ thuộc loại file descriptor. Socket, pipe, eventfd và regular file dùng các subsystem khác nhau dù cùng API `read`-like.

## Process context, interrupt context và softirq/workqueue

Kernel code chạy trong nhiều execution contexts. Trong process context, code gắn với current task và thường có thể sleep ở những điểm cho phép. Hardware interrupt context cần phản ứng nhanh, không thể tùy tiện block. Nhiều OS tách work: interrupt handler làm tối thiểu, phần còn lại được defer sang softirq/tasklet/workqueue/threaded interrupt tùy thiết kế.

Networking là ví dụ rõ: NIC interrupt báo packet arrival, driver/NAPI xử lý batch, network stack parse/route, socket queue nhận data, rồi blocked application có thể được wake.

## Blocking syscall và scheduler

Nếu resource chưa sẵn sàng, kernel đặt task vào wait structure, đổi task state và gọi scheduler. Sau event như I/O completion, task được đánh thức và trở lại runnable queue. “Blocking” vì vậy không có nghĩa CPU đứng chờ; logical thread dừng progress trong khi CPU chạy việc khác.

Non-blocking/async API thay đổi contract: caller không muốn thread sleep chỉ vì resource chưa ready. Tuy nhiên kernel vẫn phải quản lý completion, queues và backpressure.

## Context switch cost không chỉ là save registers

Switch task cần save/restore architectural state và làm scheduler bookkeeping, nhưng cost lớn có thể đến từ cache/TLB working-set disruption, branch predictor state và mất locality. Vì vậy số context switches cao đôi khi chỉ là symptom; cần đo cả CPU migrations, run-queue delay, cache misses và I/O wait.

## Security boundary

Syscall interface là attack surface. Kernel phải validate length, integer overflow, pointer lifetime, object permission và race conditions. TOCTOU bugs xuất hiện khi kernel check một state rồi sử dụng lại sau khi state có thể đổi.

Capabilities, seccomp và namespaces thu hẹp những operations/process views được phép, nhưng không thay nhu cầu input validation trong kernel.

## Mental Model

> Một syscall là **controlled privilege transition + subsystem traversal + có thể scheduling**. Để debug latency, hãy xác định thread đang chạy ở context nào, chờ resource nào, và completion nào đưa nó trở lại runnable.

## Kết nối

Ôn [kernel/syscall foundation](../../basic/03_operating_systems/00_kernel_syscalls_and_os_abstractions.md), [process/thread scheduling](../../basic/03_operating_systems/01_processes_threads_and_scheduling.md) và [I/O/interrupt/DMA](../../basic/02_computer_architecture/03_io_interrupts_dma_and_devices.md).