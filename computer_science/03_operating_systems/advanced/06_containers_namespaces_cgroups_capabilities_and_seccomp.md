# Container internals: namespaces, cgroups, capabilities và seccomp

Container thường được mô tả như “máy ảo nhẹ”, nhưng mental model đó dễ dẫn đến hiểu sai. Một container Linux thông thường **không có kernel riêng**. Các process trong container vẫn là process của kernel host; cảm giác “một máy riêng” được tạo bởi nhiều cơ chế kernel phối hợp để thay đổi những gì process có thể nhìn thấy, sử dụng và thực hiện.

Chapter này nối [kernel execution](./00_kernel_execution_contexts_and_syscall_path.md), [scheduler](./01_scheduler_run_queues_fairness_and_latency.md), [virtual memory](./03_virtual_memory_page_tables_tlb_shootdown_and_huge_pages.md) và [filesystem](./04_filesystem_crash_consistency_journaling_and_cow.md) thành một hệ thống isolation thực tế.

## 1. Container không phải một primitive duy nhất

Linux không có một syscall kiểu `create_container()`. Runtime như `runc` hoặc containerd phối hợp nhiều cơ chế:

```text
namespaces     -> thay đổi view của process
cgroups        -> quản lý và giới hạn tài nguyên
capabilities   -> chia nhỏ đặc quyền root
seccomp        -> lọc syscall
filesystem     -> tạo root filesystem riêng
LSM            -> SELinux/AppArmor policy
```

Docker/Kubernetes xây abstraction cao hơn trên các primitive này.

> Container là một **hợp đồng cô lập (isolation contract)** được ghép từ nhiều cơ chế kernel, không phải một lớp ảo hóa duy nhất.

## 2. Namespace thay đổi “thế giới nhìn thấy”

**Không gian tên (namespace / 네임스페이스)** làm cho cùng một kernel object có thể xuất hiện khác nhau với các nhóm process khác nhau.

PID namespace tạo cây process riêng. Process có thể thấy mình là PID 1 bên trong container dù kernel host gán PID khác.

Mount namespace cho mỗi nhóm process một view mount riêng. Network namespace cung cấp interface, routing table, socket namespace và firewall context riêng. UTS namespace cô lập hostname; IPC namespace cô lập một số IPC object; user namespace ánh xạ UID/GID giữa bên trong và host.

Điểm quan trọng: namespace chủ yếu giải quyết **visibility và naming**, không tự giới hạn lượng CPU/RAM mà process tiêu thụ.

## 3. PID 1 trong container có ý nghĩa đặc biệt

Process đầu tiên của PID namespace trở thành PID 1 trong namespace đó. PID 1 có semantics signal và trách nhiệm thu gom process con khác process bình thường.

Nếu application chạy trực tiếp làm PID 1 nhưng không `wait()` child process đúng cách, zombie có thể tích tụ. Đây là lý do một số image dùng init nhỏ như `tini`.

Vấn đề này cho thấy abstraction container không xóa semantics của OS; ngược lại, application đôi khi tiếp xúc trực tiếp hơn với chúng.

## 4. Mount namespace và root filesystem

Container có thể thấy một filesystem tree khác nhờ mount namespace kết hợp `pivot_root`/`chroot` và layered filesystem. Image layer thường bất biến; writable layer của container nằm phía trên.

**Sao chép khi ghi (copy-on-write / CoW)** cho phép nhiều container chia sẻ layer gốc. Khi một container sửa file, block hoặc file tương ứng được tạo ở writable layer của nó.

Điều này tiết kiệm storage nhưng có chi phí metadata và I/O. Database có workload ghi nặng thường không nên coi writable image layer như storage bền vững chính; volume/bind mount phù hợp hơn.

## 5. Network namespace tạo network stack logic riêng

Một container có thể có interface `eth0` riêng dù đó chỉ là một đầu của cặp `veth`. Đầu kia nằm ở host hoặc namespace khác và thường nối vào bridge.

```text
container eth0
     |
   veth pair
     |
host bridge
     |
physical NIC
```

Packet có thể đi qua routing, NAT, conntrack và firewall rule. Vì vậy “container networking” vẫn là networking Linux; abstraction cao hơn chỉ tự động cấu hình đường đi.

Khi debug latency hoặc packet loss, cần biết packet thực sự đi qua những namespace và rule nào thay vì chỉ nhìn service name của Kubernetes.

## 6. Cgroups giải quyết resource accounting và control

**Nhóm điều khiển (control groups / cgroups / 제어 그룹)** nhóm process để kernel theo dõi và kiểm soát tài nguyên. Cgroup v2 cung cấp hierarchy thống nhất cho CPU, memory, I/O, process count và các controller khác.

Namespace trả lời “process nhìn thấy gì”; cgroup trả lời “process được dùng bao nhiêu”. Hai khái niệm thường xuất hiện cùng container nhưng giải quyết vấn đề khác nhau.

## 7. CPU quota không tương đương CPU riêng

Một container được quota 1 CPU không nhất thiết sở hữu một core vật lý riêng. Scheduler vẫn phân phối runnable task trên CPU host theo cpuset, weight và quota.

Quota có thể được mô hình hóa bằng ngân sách CPU trong một khoảng thời gian. Khi dùng hết ngân sách, cgroup bị **điều tiết (throttling)** cho tới kỳ tiếp theo. Application có thể thấy tail latency tăng dù host chưa đạt 100% CPU trung bình.

Đây là lý do metric `CPU usage` đơn lẻ không đủ. Cần quan sát throttled time, run queue và latency distribution.

## 8. Memory limit và OOM trong container

Memory cgroup theo dõi mức dùng bộ nhớ và có thể áp limit. Khi cgroup không thể reclaim đủ memory dưới giới hạn, kernel có thể kích hoạt **OOM trong phạm vi cgroup** thay vì giết process ngẫu nhiên trên toàn host.

Nhưng memory accounting không đơn giản chỉ là heap của application. Page cache, anonymous memory và một số kernel memory cũng ảnh hưởng tùy cấu hình/kernel.

Một JVM đặt heap gần bằng container memory limit có thể vẫn bị OOMKill vì native memory, thread stack, direct buffer, JIT metadata và page cache cần không gian riêng.

## 9. User namespace và root không nhất thiết là host root

User namespace cho phép UID 0 bên trong namespace ánh xạ sang UID không đặc quyền trên host. Điều này giảm hậu quả nếu process thoát khỏi một số boundary.

Tuy nhiên, “rootless” không tự động có nghĩa là an toàn tuyệt đối. Kernel vẫn là shared attack surface và cấu hình namespace/capability/filesystem vẫn quan trọng.

## 10. Linux capabilities chia nhỏ quyền root

Unix truyền thống có mô hình gần như nhị phân: root hoặc không root. **Năng lực đặc quyền (Linux capabilities)** chia quyền root thành các quyền nhỏ hơn như `CAP_NET_BIND_SERVICE`, `CAP_SYS_ADMIN`, `CAP_NET_ADMIN`.

Container nên chỉ giữ capability thực sự cần. `CAP_SYS_ADMIN` đặc biệt rộng và thường được xem như một capability rất nhạy cảm.

Nguyên tắc ở đây là **đặc quyền tối thiểu (least privilege)**: application web không cần quyền quản trị network hoặc mount filesystem chỉ vì nó chạy trong container.

## 11. Seccomp thu hẹp syscall surface

**Seccomp** cho phép lọc syscall mà process được phép gọi. Nếu application không bao giờ cần `ptrace`, `mount` hoặc một syscall nguy hiểm khác, policy có thể chặn chúng.

Điều này không sửa lỗ hổng trong kernel, nhưng giảm tập đường đi mà attacker có thể dùng sau khi chiếm được process. Security thường mạnh hơn khi nhiều lớp độc lập cùng giới hạn attacker:

```text
namespace
+ non-root UID
+ dropped capabilities
+ seccomp
+ AppArmor/SELinux
+ read-only filesystem
```

## 12. Container escape và shared kernel

VM thường đặt guest sau boundary hypervisor và guest kernel riêng. Container chia sẻ kernel host. Nếu attacker khai thác được kernel vulnerability thông qua syscall surface có thể truy cập, namespace không còn là boundary tuyệt đối.

Do đó threat model quyết định isolation technology. Multi-tenant workload không tin cậy có thể cần VM, microVM hoặc sandbox bổ sung thay vì chỉ container tiêu chuẩn.

## 13. Cgroups và Kubernetes requests/limits

Kubernetes `requests` và `limits` cuối cùng phải được chuyển thành primitive của OS/runtime. CPU request chủ yếu ảnh hưởng scheduling/weight; CPU limit có thể thành quota. Memory limit trở thành giới hạn cgroup và có thể dẫn tới OOMKill.

Điều này giải thích tại sao hiểu Kubernetes mà không hiểu scheduler, memory reclaim và cgroups sẽ tạo khoảng trống mental model. YAML chỉ là lớp cấu hình; hành vi cuối cùng xảy ra trong kernel.

## 14. Noisy neighbor

Hai container trên cùng host vẫn chia sẻ nhiều tài nguyên: LLC cache, memory bandwidth, storage queue, NIC, kernel lock và đôi khi NUMA topology. Cgroup giúp kiểm soát một số tài nguyên nhưng không biến host thành các máy vật lý độc lập hoàn toàn.

Một workload có thể không vượt CPU limit nhưng vẫn làm workload khác chậm do memory bandwidth hoặc I/O contention. Đây là **ảnh hưởng hàng xóm ồn (noisy-neighbor effect)**.

## 15. Debug từ container xuống kernel

Khi container “chậm”, cần phân tách các lớp:

```text
application queue
↓
container CPU/memory limit
↓
cgroup throttling / reclaim
↓
host scheduler / run queue
↓
NUMA / cache / memory bandwidth
↓
storage hoặc network
```

`docker stats` hoặc dashboard Kubernetes chỉ là điểm bắt đầu. Production debugging sâu cần nối metric ở orchestration layer với kernel evidence.

## Common Misconceptions

**“Container là VM nhẹ.”** Hữu ích như phép so sánh ban đầu nhưng sai nếu hiểu theo kiến trúc: container thường chia sẻ host kernel.

**“Namespace tạo security boundary hoàn chỉnh.”** Namespace cô lập view; security boundary thực tế cần capability, seccomp, LSM, filesystem permission và kernel security.

**“CPU limit 1 nghĩa là có một CPU riêng.”** Không. Nó thường là quota/weight trên scheduler dùng chung.

**“Memory limit chỉ giới hạn Java heap.”** Không. Runtime còn dùng native memory và hệ thống còn nhiều loại memory accounting khác.

## Mental Model

> Container là một process bình thường được đặt trong một **thế giới quan bị giới hạn**, một **ngân sách tài nguyên**, và một **tập quyền bị thu hẹp**.

Khi abstraction container gây khó hiểu, hãy bóc nó trở lại process, namespace, cgroup, syscall, filesystem và scheduler. Đây cũng là cách reasoning hiệu quả khi debug Docker và Kubernetes.

Xem tiếp: [Kernel synchronization và RCU](./07_kernel_synchronization_rcu_and_lockless_read_paths.md), [Security](../../07_security_reliability/advanced/README.md) và [Architecture](../../02_computer_architecture/advanced/README.md).
