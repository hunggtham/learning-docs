# Linux như môi trường thực thi production

## 1. Vì sao DevOps phải hiểu Linux dù đang dùng container

Container không loại bỏ hệ điều hành; nó thay cách process nhìn hệ điều hành. Một workload trong container cuối cùng vẫn được kernel schedule, cấp memory, xử lý file descriptor, socket, signal và I/O. Vì vậy khi production có CPU throttling, OOM kill, file descriptor exhaustion hoặc process không nhận signal shutdown, chỉ biết `docker ps` hay `kubectl get pods` là chưa đủ.

Chapter này không viết lại Operating Systems. Mục tiêu là nối các abstraction Linux quan trọng với công việc vận hành. Nền sâu hơn về kernel/syscall xem [canonical OS foundation](../../computer_science/basic/03_operating_systems/00_kernel_syscalls_and_os_abstractions.md), process/thread xem [processes, threads và scheduling](../../computer_science/basic/03_operating_systems/01_processes_threads_and_scheduling.md), filesystem/I/O xem [filesystems, storage và I/O](../../computer_science/basic/03_operating_systems/04_filesystems_storage_and_io.md).

## 2. Process là đơn vị đầu tiên để suy luận

Một service đang chạy không phải “một ứng dụng” theo nghĩa trừu tượng. Ở mức OS, nó là một hoặc nhiều process có PID, address space, open file descriptor, credential, environment, current working directory và set resource limit. Mọi câu hỏi vận hành nên dần quy về các state có thể quan sát này.

Khi service “không chạy”, cần tách ít nhất bốn khả năng. Process chưa được tạo. Process tạo rồi thoát ngay. Process còn sống nhưng không listen. Process listen nhưng request path không tới được. Bốn trạng thái này có biểu hiện bên ngoài gần giống nhau nhưng evidence khác nhau.

Ví dụ, một service Java chạy dưới `systemd` có thể kiểm tra theo chuỗi:

```bash
systemctl status orders.service
journalctl -u orders.service --since "10 min ago"
ps -ef | grep java
ss -lntp
```

Lệnh không phải đáp án; mỗi lệnh kiểm tra một giả thuyết. `systemctl` kiểm tra supervisor state, `journalctl` kiểm tra lifecycle evidence, `ps` kiểm tra process existence, `ss` kiểm tra socket/listener.

## 3. Service manager và supervision

Một process production cần lifecycle manager. `systemd` hoặc container orchestrator làm nhiều hơn “start chương trình”: chúng định nghĩa khi nào restart, environment nào được inject, dependency nào phải có, log đi đâu và signal nào được gửi khi shutdown.

Nếu application tự fork, daemonize và giữ PID file trong khi supervisor cũng mong process chạy foreground, ownership lifecycle bị chia đôi. Production practice hiện đại thường để process chính chạy foreground và để supervisor quản restart, health và shutdown.

Điều cần hiểu là parent/child ownership. Nếu supervisor nghĩ process đã chết trong khi child vẫn còn, có thể xuất hiện orphan hoặc duplicated service. Nếu process PID 1 trong container không forward/reap signal đúng, graceful shutdown và zombie handling có thể hỏng. Đây là lý do “process model” quan trọng hơn câu lệnh start.

## 4. Signal và graceful shutdown

Khi deploy phiên bản mới, orchestrator thường không “tắt điện” ngay. Nó yêu cầu workload dừng bằng signal, cho một khoảng grace period, rồi mới force kill nếu process không thoát. Application production phải coi shutdown là một protocol.

Một sequence tốt thường là: ngừng nhận request mới, cho load balancer/endpoints cập nhật, hoàn tất hoặc hủy request đang xử lý theo deadline, flush state/log cần thiết, đóng connection pool và thoát. Nếu application bắt signal nhưng mất 90 giây trong khi grace period là 30 giây, cuối cùng vẫn bị kill giữa transaction.

Điểm senior cần nhớ: “graceful” phải được chứng minh bằng traffic behavior chứ không phải chỉ có shutdown hook trong code.

## 5. File descriptor và socket là tài nguyên hữu hạn

Linux biểu diễn nhiều I/O resource bằng file descriptor (FD). Socket, file, pipe và nhiều kernel object đều tiêu tốn FD. Một service leak connection có thể vẫn còn CPU và memory nhưng không mở thêm socket/file được.

`ulimit -n` cho biết giới hạn ở shell hiện tại nhưng service có thể chạy dưới limit khác do `systemd`, container runtime hoặc policy. Khi thấy lỗi “too many open files”, đừng chỉ tăng limit. Trước hết phải hỏi số FD tăng vì workload hợp lệ hay leak; loại FD nào đang chiếm; connection pool có close đúng không; downstream latency có làm socket sống lâu bất thường không.

Có thể kiểm tra theo PID:

```bash
ls /proc/<pid>/fd | wc -l
lsof -p <pid>
```

`/proc` là nguồn evidence mạnh vì nó cho thấy kernel đang nhìn process như thế nào.

## 6. Memory: RSS không phải toàn bộ câu chuyện

Production thường hiển thị một số “memory usage”, nhưng số đó có thể đại diện RSS, working set, cgroup usage hoặc metric runtime. Page cache, mapped file, heap và native allocation có semantics khác nhau.

Một service có thể bị OOM dù host còn memory nếu cgroup limit đã chạm. Ngược lại, host có memory pressure dù từng container chưa chạm limit. Kernel reclaim, page cache và memory pressure được đào sâu tại [memory pressure, reclaim và page faults](../../computer_science/03_operating_systems/advanced/02_page_faults_reclaim_dirty_pages_and_memory_pressure.md).

Về vận hành, hãy tách ba câu hỏi: application đang giữ memory nào; container/cgroup đang bị giới hạn thế nào; host/node đang chịu pressure ra sao. Nếu chỉ nhìn một dashboard application heap, bạn có thể bỏ sót native memory hoặc kernel pressure.

## 7. CPU usage khác CPU entitlement

`100% CPU` chỉ có nghĩa khi biết đơn vị đo. Trên host nhiều core, một process một-thread có thể dùng đầy một core nhưng chỉ chiếm phần nhỏ tổng host. Trong container, CPU request/limit có thể thêm một tầng entitlement. Khi workload bị CFS throttling, latency có thể tăng dù node chưa “100% CPU”.

Do đó reasoning đúng là: demand bao nhiêu, allocation/limit bao nhiêu, scheduler cho chạy thực tế bao nhiêu, queue/run time tăng ra sao. Nền scheduler xem [scheduler internals](../../computer_science/03_operating_systems/advanced/01_scheduler_run_queues_fairness_and_latency.md).

## 8. Filesystem và “disk full”

“Disk full” có thể là hết block, hết inode, filesystem read-only sau lỗi, quota bị chạm hoặc layer writable của container đầy. `df -h` chỉ trả lời một phần. `df -i` kiểm tra inode; `du` giúp tìm tree sử dụng dung lượng nhưng có thể không thấy file đã xóa mà process còn giữ open FD.

Một tình huống điển hình là log file lớn bị `rm`, nhưng process vẫn giữ FD. Tên file biến mất khỏi directory nhưng block chưa được giải phóng cho tới khi FD đóng. `lsof +L1` có thể lộ trường hợp này. Đây là ví dụ rõ cho việc mental model filesystem quan trọng hơn thao tác xóa file.

## 9. Evidence ladder cho Linux incident

Khi một workload lỗi, nên đi từ evidence ít phá hoại đến sâu hơn. Trước hết xác định symptom và time window. Sau đó kiểm tra process/service state, logs/events, listener/socket, resource pressure, dependency connectivity. Chỉ khi các lớp này không đủ mới đi sâu vào `/proc`, syscall tracing, packet capture hoặc kernel evidence.

Đừng restart quá sớm nếu chưa thu evidence tối thiểu. Restart có thể phục hồi service nhưng đồng thời xóa state quý giá để tìm root cause. Trong incident có user impact lớn, recovery vẫn ưu tiên; nhưng nên có quy ước ai capture evidence nào trước khi restart khi thời gian cho phép.

## 10. Production invariant

Một service vận hành tốt cần có lifecycle rõ ràng: process foreground, supervisor ownership, signal handling, resource boundary, log/telemetry path và health semantics nhất quán. Container hay VM chỉ thay packaging và isolation boundary; invariant này vẫn còn.

## 11. Load average không đồng nghĩa CPU utilization

`load average` trên Linux gần với số task đang muốn chạy hoặc đang ở một số trạng thái chờ không ngắt được, chứ không phải phần trăm CPU. Vì vậy load cao có thể đến từ CPU run queue lớn, nhưng cũng có thể đến từ I/O hoặc kernel wait. Một máy 16 CPU với load 8 có ý nghĩa khác máy 2 CPU với load 8.

Khi latency tăng cùng load average, đừng kết luận “thiếu CPU” trước khi xem run queue, CPU utilization, I/O wait và pressure. Đây là ví dụ điển hình của việc một metric tổng hợp chỉ là đầu mối, không phải diagnosis.

## 12. Pressure Stall Information giúp đo thời gian workload bị thiếu tài nguyên

Pressure Stall Information (PSI) cho biết trong một khoảng thời gian, task đã phải chờ vì thiếu CPU, memory hoặc I/O bao lâu. Đây là góc nhìn khác utilization. CPU có thể chưa 100% trung bình nhưng một workload latency-sensitive vẫn chịu pressure do cgroup quota hoặc run queue. Memory usage có thể chưa chạm limit nhưng reclaim liên tục làm task stall.

Trong incident, PSI hữu ích vì nó hỏi trực tiếp: “workload có đang bị trì hoãn bởi resource contention không?”. Sau đó mới đi sâu xem contention đến từ cgroup boundary, node overcommit, reclaim, storage latency hay workload khác.

## 13. Cgroup v2: resource control là hierarchy chứ không chỉ một con số limit

Trong hệ thống dùng cgroup v2, CPU, memory và nhiều resource được quản theo một hierarchy thống nhất. Workload có thể chịu constraint từ chính cgroup của nó và từ ancestor. Vì vậy “container limit là X” chưa đủ nếu node hoặc parent slice đang có policy khác.

Memory control cũng không chỉ có hard limit. Các ngưỡng như `memory.high` có thể tạo reclaim/throttling pressure trước khi `memory.max` dẫn tới OOM. Về operational reasoning, điều quan trọng là phân biệt **pressure** với **hard failure**: service có thể chậm nghiêm trọng trước khi bị kill.

## 14. OOM phải xác định scope: process, cgroup hay host

Một dòng log “OOM” chưa nói rõ failure domain. Có trường hợp process/runtime tự ném lỗi vì heap limit. Có trường hợp cgroup OOM kill vì workload vượt memory boundary. Có trường hợp host chịu global memory pressure và kernel chọn victim.

Ba trường hợp cần evidence khác nhau. Runtime heap metrics trả lời câu hỏi bên trong process. Cgroup events trả lời workload có chạm boundary không. Kernel log/node pressure trả lời host có thiếu memory toàn cục không. Chỉ tăng heap hoặc tăng pod limit mà không xác định scope có thể chuyển failure sang tầng khác.

## 15. Senior walkthrough: latency tăng nhưng CPU dashboard chỉ 45%

Giả sử `orders-api` p99 tăng từ 200 ms lên 2 giây, node CPU trung bình 45%. Kết luận “CPU không phải vấn đề” là quá sớm. Hãy kiểm tra CPU quota/throttling của workload, run queue/PSI, số thread runnable, GC và dependency wait.

Nếu throttling tăng đúng lúc latency tăng, workload có thể đang đòi nhiều CPU hơn entitlement dù host còn idle capacity. Nếu không throttling nhưng PSI I/O tăng, nguyên nhân có thể là storage. Nếu cả hai bình thường nhưng thread dump cho thấy nhiều thread chờ connection pool, bottleneck chuyển sang downstream.

Cách reasoning này giữ nguyên nguyên tắc của chapter: một metric ở một layer không phủ định pressure ở layer khác.

## 16. Dirty page và writeback có thể tạo latency trước khi disk “đầy”

Khi process ghi file, nhiều write không lập tức đi thẳng xuống storage; dữ liệu có thể đi vào page cache rồi kernel flush dần xuống thiết bị. Điều này làm write bình thường nhìn rất nhanh, nhưng nếu tốc độ dirty data cao hơn tốc độ writeback lâu đủ, kernel phải throttle writer hoặc application gặp burst latency khi flush/fsync.

Vì vậy một service ghi log, temporary file hoặc local database có thể xuất hiện p99 latency tăng trong khi disk usage vẫn còn nhiều. Evidence cần nối application write latency, I/O PSI, device latency/queue và dirty/writeback behavior. “Disk chưa đầy” chỉ loại trừ capacity theo dung lượng, không loại trừ saturation theo throughput/latency.

Operational lesson là storage có ít nhất hai loại headroom: còn bao nhiêu bytes và còn bao nhiêu service rate cho I/O. Hai thứ không thay thế nhau.

## 17. Listen socket có queue trước khi application `accept()` connection

Một process có thể đang `LISTEN` nhưng vẫn không theo kịp connection mới. Kernel giữ state cho connection setup và hàng đợi connection đã hoàn thành chờ application `accept()`. Nếu application event loop/thread pool bị stall hoặc accept rate thấp hơn arrival rate, queue có thể đầy và client thấy timeout/reset dù process vẫn sống và port vẫn mở.

Do đó `ss -lntp` xác nhận listener tồn tại nhưng chưa chứng minh listener đang phục vụ đủ nhanh. Khi có connect failure dưới load, cần nối socket backlog/accept behavior với application thread state, CPU throttling và event-loop latency.

Đây là cùng mental model queueing: kernel queue hấp thụ burst, nhưng queue không tạo thêm service capacity. Nếu producer connection đến nhanh hơn application nhận lâu đủ, failure cuối cùng vẫn xuất hiện.

## 18. Resource limit có nhiều tầng và effective limit là tầng chặt nhất

Một process có thể chịu `RLIMIT_NOFILE`, `systemd` unit limit, cgroup boundary, container runtime setting và node-level pressure cùng lúc. Operator thường nhìn một tầng rồi nghĩ đó là “limit thực”. Thực tế effective behavior đến từ constraint chặt nhất trên đường thực thi.

Ví dụ shell tương tác báo `ulimit -n` rất cao nhưng service unit có `LimitNOFILE` thấp hơn; hoặc container memory limit 4 GiB nhưng parent cgroup của cả workload class đang bị pressure. Vì vậy evidence phải lấy từ context của chính process/service, không lấy từ shell khác rồi suy diễn.

Mental model này áp dụng rộng hơn Linux: production abstraction thường là composition của nhiều policy; giá trị hiển thị ở một layer chỉ có nghĩa trong boundary đó.

## 19. Clock là dependency production dù không tiêu CPU đáng kể

Nhiều protocol và hệ thống phụ thuộc thời gian: TLS certificate validity, token expiry, distributed trace ordering, lease, cron/scheduler, cache TTL và log correlation. Nếu clock skew lớn, service có thể fail authentication hoặc tạo timeline điều tra sai dù CPU/memory/network đều khỏe.

Không nên dùng wall clock như một nguồn ordering tuyệt đối cho distributed event. Trong incident, timestamp giữa hai host lệch nhau có thể làm causal chain nhìn đảo ngược. NTP/time-sync health vì vậy là operational dependency; còn ordering/causality sâu hơn thuộc Distributed Systems canonical docs.

Khi failure gắn với “token chưa có hiệu lực”, “certificate chưa hợp lệ” hoặc event dường như xảy ra trước cause, hãy kiểm tra clock/source-time assumption trước khi invent một race condition phức tạp.

## 20. Senior walkthrough: API timeout tăng cùng log burst nhưng CPU và DB đều bình thường

Giả sử sau khi bật debug log, request p99 tăng mạnh. CPU chỉ 35%, DB latency không đổi, network bình thường. Node cho thấy I/O PSI tăng và device write latency xuất hiện burst; application thread dump có nhiều thread chờ flush/logging path.

Causal chain hợp lý là log volume làm dirty data tăng, writeback/storage bắt đầu stall writer, request thread bị giữ lâu hơn, concurrency tăng và tail latency khuếch đại. Tăng CPU replica có thể không giúp nếu tất cả replica cùng ghi vào bottleneck storage/log path.

Mitigation có thể giảm log verbosity, chuyển logging sang buffered/asynchronous path có backpressure hợp lý hoặc tăng I/O capacity. Long-term fix là coi logging pipeline như dependency có budget, không phải side effect “miễn phí” của application.
