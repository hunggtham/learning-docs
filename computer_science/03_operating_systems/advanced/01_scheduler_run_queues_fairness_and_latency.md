# Scheduler internals, run queue và fairness/latency trade-offs

Scheduler của operating system không đơn giản là “chọn process tiếp theo”. Nó phân phối một tài nguyên không thể dùng đồng thời trên cùng CPU core — **execution time** — giữa nhiều runnable tasks có mục tiêu khác nhau: throughput, interactive latency, fairness, deadline và energy efficiency.

## Runnable không có nghĩa đang chạy

Task có thể đang running, runnable nhưng chờ CPU, sleeping vì chờ I/O, hoặc blocked trên synchronization primitive. Scheduler chủ yếu lựa chọn trong tập **runnable tasks**.

Một **run queue (실행 대기열)** biểu diễn các task có thể chạy. Trên multiprocessor, hệ điều hành thường duy trì scheduling state theo CPU để giảm contention và tăng locality. Điều này sinh thêm bài toán load balancing: CPU A có thể quá tải trong khi CPU B rảnh.

## Fairness là một policy, không phải định luật

Round-robin chia time slice đều là mental model dễ hiểu nhưng production scheduler cần tinh vi hơn. Interactive task thường chạy ngắn rồi sleep chờ user/I/O; batch task có thể muốn dùng CPU liên tục. Nếu mọi task được đối xử hoàn toàn giống nhau theo từng quantum, latency cảm nhận và cache locality có thể không tối ưu.

Linux CFS truyền thống dùng khái niệm **virtual runtime** để xấp xỉ “CPU công bằng”: task đã nhận nhiều CPU time hơn sẽ có virtual runtime lớn hơn và ít ưu tiên hơn. Nice value thay đổi trọng số chứ không đơn giản là cộng một mức priority cố định.

Scheduler hiện đại có thể thay đổi implementation, nhưng invariant cần hiểu là policy cố gắng phân phối service theo trọng số trong khi vẫn giới hạn scheduling overhead và latency.

## Context switch có nhiều loại cost

Context switch cần lưu/khôi phục architectural state, nhưng chi phí lớn hơn có thể đến từ cache/TLB locality bị phá. Chuyển sang task khác làm working set mới cạnh tranh cache với working set cũ. Vì vậy quantum quá nhỏ tăng responsiveness nhưng có thể giảm throughput.

Ngược lại, quantum quá lớn làm interactive task chờ lâu. Đây là trade-off nền tảng giữa **latency** và **amortized scheduling overhead**.

## CPU affinity và locality

Di chuyển task sang core khác có thể giúp cân tải nhưng mất cache warmth và trong NUMA system còn có thể khiến task chạy xa memory mà nó thường truy cập. Scheduler vì vậy cân bằng giữa fairness toàn hệ thống và locality.

**CPU affinity (CPU 친화성)** có thể hữu ích cho workload latency-sensitive hoặc benchmark, nhưng pin task tùy tiện có thể làm load imbalance tệ hơn. Affinity là constraint lên scheduler, không phải universal optimization.

## Wakeup latency

Server request thường trải qua pattern: thread ngủ chờ socket, packet đến, interrupt/network stack đánh thức thread, task trở thành runnable, scheduler chọn thời điểm chạy. Latency từ wakeup tới execution có thể trở thành phần đáng kể của tail latency khi CPU saturated.

Điều này giải thích tại sao CPU utilization gần 100% không chỉ ảnh hưởng throughput. Khi run queue dài, request mới phải xếp hàng trước khi application code thậm chí bắt đầu chạy.

## Priority và priority inversion

Nếu high-priority task cần lock đang bị low-priority task giữ, trong khi medium-priority tasks liên tục preempt low-priority holder, high-priority task có thể bị chặn lâu. Đây là **priority inversion (우선순위 역전)**.

Các hệ thống real-time có thể dùng **priority inheritance**: lock holder tạm thời nhận priority cao hơn để hoàn thành critical section và giải phóng resource. Bài học rộng hơn là scheduling policy và synchronization không thể reasoning tách rời.

## Real-time khác với “nhanh”

Real-time scheduling quan tâm tới bounded latency và deadline guarantee, không đơn thuần average performance. Một task hoàn thành trung bình 1 ms nhưng đôi lúc 100 ms có thể tệ hơn task ổn định 5 ms trong hệ thống có deadline 10 ms.

Soft real-time chấp nhận một số deadline miss; hard real-time yêu cầu guarantee nghiêm ngặt hơn và cần kiểm soát scheduler, interrupt, allocation, locking và I/O path.

## Production diagnosis

Khi service chậm, CPU usage một mình không đủ. Cần phân biệt CPU thực sự execute application, runnable queue dài, steal time trong VM, throttling do cgroup, frequency scaling, lock contention hay I/O wait. Scheduler metrics phải được đọc cùng tracing và application-level latency.

## Mental model

> Scheduler là một resource allocator theo thời gian. Nó không “làm task nhanh hơn”; nó quyết định task nào được quyền dùng CPU, khi nào bị preempt và cost của fairness/locality/deadline được phân phối ra sao. Khi CPU saturated, scheduling queue trở thành queueing system và tail latency tăng trước khi throughput sụp hoàn toàn.