# Namespace, cgroup, capability và seccomp

Container không phải một cơ chế duy nhất. Nó là kết quả của việc ghép nhiều primitive Linux để tạo ra **góc nhìn riêng, giới hạn tài nguyên và giới hạn quyền** cho một nhóm tiến trình.

Bốn khái niệm cần tách rõ là:

- **namespace** — tiến trình nhìn thấy cái gì;
- **cgroup** — tiến trình được dùng bao nhiêu tài nguyên và được accounting ra sao;
- **capability** — tiến trình có đặc quyền kernel nào;
- **seccomp** — tiến trình được phép gọi những system call nào.

Nếu gộp tất cả thành “container isolation”, việc debug và hardening sẽ rất mơ hồ.

## Namespace: thay đổi góc nhìn

Namespace tạo một view riêng cho một loại resource.

Các loại quan trọng gồm:

- PID namespace;
- mount namespace;
- network namespace;
- UTS namespace;
- IPC namespace;
- user namespace;
- cgroup namespace;
- time namespace trên kernel hỗ trợ.

### PID namespace

Một process có thể có PID khác nhau tùy namespace.

Trong container:

```bash
ps -ef
```

có thể thấy application là PID 1.

Trên host, cùng process có thể là PID 27481.

Điều này không phải duplication của process. Đó là cùng một kernel task nhưng được nhìn qua hai PID namespaces.

Có thể inspect namespace links:

```bash
ls -l /proc/<PID>/ns
```

Ví dụ:

```text
pid -> pid:[4026531836]
net -> net:[4026532001]
mnt -> mnt:[4026531999]
```

Hai processes có namespace inode identifier giống nhau thường đang chia sẻ namespace tương ứng.

## Mount namespace

Mount namespace cho mỗi nhóm process có mount table riêng.

Container có thể nhìn:

```text
/
/app
/data
```

mà không giống mount tree của host.

Do đó khi container báo file không tồn tại, phải hỏi **đường dẫn trong namespace nào**.

Một file tồn tại trên host `/opt/data/file` không có nghĩa container thấy nó nếu chưa bind mount/volume.

## Network namespace

Mỗi network namespace có thể có:

- interfaces;
- routing table;
- firewall context;
- sockets;
- loopback riêng.

Vì vậy `127.0.0.1` trong container thường là loopback của container namespace, không phải host.

Có thể tạo namespace thủ công để học:

```bash
sudo ip netns add lab
sudo ip netns exec lab ip addr
```

Xóa sau khi thử:

```bash
sudo ip netns del lab
```

Đây là cách thấy container networking không phải “phép thuật Docker”; Docker chỉ tự động hóa các primitives này.

## UTS namespace

UTS namespace tách hostname/domain-name view.

Container có thể có hostname riêng dù dùng cùng host kernel.

Điều này giải thích vì sao:

```bash
hostname
```

trong container có thể khác host.

## User namespace

User namespace cho phép remap UID/GID.

Một process có thể là UID 0 **bên trong namespace** nhưng ánh xạ tới UID không đặc quyền trên host.

Điều này giảm rủi ro so với container root ánh xạ trực tiếp host root, nhưng semantics permission với bind mounts trở nên phức tạp hơn.

## Namespace không phải resource limit

Một process trong PID namespace riêng vẫn có thể tiêu rất nhiều CPU/RAM nếu không có cgroup limit.

Namespace chủ yếu giải quyết **visibility/isolation**, không phải capacity control.

Đó là vai trò của cgroup.

# Cgroup: accounting và giới hạn tài nguyên

**Control group (cgroup)** gom processes vào hierarchy để kernel accounting và control resource usage.

Modern distributions ngày càng dùng **cgroup v2** với unified hierarchy.

Kiểm tra:

```bash
mount | grep cgroup
stat -fc %T /sys/fs/cgroup
```

Trên cgroup v2 thường thấy type `cgroup2fs`.

## Memory cgroup

Một container có thể bị giới hạn 1 GiB dù host có 64 GiB RAM.

Trong cgroup v2, các files như:

```text
memory.current
memory.max
memory.events
```

cho runtime state và limit.

Ví dụ:

```bash
cat /sys/fs/cgroup/memory.current
cat /sys/fs/cgroup/memory.max
cat /sys/fs/cgroup/memory.events
```

Path thực tế có thể khác tùy process cgroup.

Tìm cgroup của PID:

```bash
cat /proc/<PID>/cgroup
```

## Host memory còn nhiều nhưng container vẫn OOM

Nếu `memory.max` là 1 GiB và process vượt giới hạn, cgroup có thể OOM-kill workload dù:

```bash
free -h
```

trên host vẫn còn hàng chục GiB.

Đây là một trong những lỗi debug container phổ biến nhất.

## CPU cgroup

Cgroup có thể kiểm soát CPU quota/weight.

Một container được gán “1 CPU” không nhất thiết sở hữu một core vật lý riêng. Nó thường nhận một quota scheduling tương ứng.

Nếu Java đọc `Runtime.getRuntime().availableProcessors()`, behavior còn phụ thuộc JVM version và container awareness.

Thread pool sizing dựa CPU count vì vậy phải xem runtime/container limit thật.

## CPU throttling

Một service có thể không đạt 100% host CPU nhưng vẫn bị throttled bởi cgroup quota.

Triệu chứng:

- latency tăng;
- runnable work nhiều;
- host còn CPU idle;
- cgroup quota đã dùng hết trong period.

Đây là counterexample quan trọng cho cách nhìn host-level metrics đơn thuần.

## I/O cgroup

Cgroup cũng có thể kiểm soát/account block I/O trên kernel/storage phù hợp.

Hai containers cùng host có thể cạnh tranh disk dù CPU/RAM tách tốt.

Vì vậy multi-tenant performance cần nhìn cả I/O resource domain.

# Linux capabilities: chia nhỏ quyền root

Unix truyền thống có mô hình root rất mạnh. Linux capabilities tách một phần quyền root thành các capability nhỏ hơn.

Ví dụ:

- `CAP_NET_BIND_SERVICE` — bind privileged ports;
- `CAP_NET_ADMIN` — nhiều thao tác network administration;
- `CAP_SYS_ADMIN` — capability rất rộng và nhạy cảm;
- `CAP_SYS_PTRACE` — ptrace một số processes;
- `CAP_CHOWN` — thay ownership theo policy.

Xem capability của process:

```bash
grep '^Cap' /proc/<PID>/status
```

Tool như `capsh` hoặc `getpcaps` có thể diễn giải dễ hơn nếu được cài.

## Vì sao container không nên chạy `--privileged`?

`--privileged` thường cấp capabilities rất rộng và device access lớn hơn, làm nhiều isolation boundary yếu đi.

Nếu application chỉ cần bind port thấp, tốt hơn cấp đúng capability cần thiết thay vì full privilege.

Đây là nguyên tắc đặc quyền tối thiểu (least privilege) ở kernel level.

# Seccomp: giới hạn system call

Seccomp cho phép hạn chế tập system calls process được phép sử dụng.

Container runtime thường dùng seccomp profile mặc định để block một số calls nguy hiểm/hiếm cần.

Nếu application bị block syscall, triệu chứng có thể là `EPERM`, process crash hoặc audit log tùy profile/runtime.

Seccomp không thay thế permission/capability. Nó là một layer khác:

```text
namespace → nhìn thấy gì
cgroup    → dùng bao nhiêu
capability→ có đặc quyền nào
seccomp   → gọi syscall nào
```

## Security boundary là composition

Container security tốt thường kết hợp:

- non-root user;
- user namespace khi phù hợp;
- drop capabilities;
- seccomp profile;
- AppArmor/SELinux;
- read-only root filesystem;
- resource limits;
- network policy;
- image provenance;
- host kernel patching.

Không có một flag đơn lẻ biến container thành sandbox tuyệt đối.

# Cgroup và systemd

Systemd sử dụng cgroups để quản lý units.

Có thể xem cây:

```bash
systemd-cgls
```

Resource settings trong unit:

```ini
[Service]
MemoryMax=1G
CPUQuota=100%
TasksMax=512
```

Điều này cho phép dùng cgroup controls ngay cả khi không chạy container.

Service Linux truyền thống và container cùng dùng kernel primitives nền tảng.

## `systemctl status` và cgroup

`systemctl status` thường hiển thị `CGroup:` và process tree của service.

Điều này giúp hiểu service unit không chỉ là một PID đơn lẻ; systemd theo dõi một cgroup chứa nhiều child processes.

# Namespace debugging bằng `nsenter`

`nsenter` cho phép chạy command trong namespaces của process khác.

Ví dụ vào network namespace:

```bash
sudo nsenter -t <PID> -n ip addr
```

Vào mount namespace:

```bash
sudo nsenter -t <PID> -m mount
```

Kết hợp nhiều namespaces:

```bash
sudo nsenter -t <PID> -m -n -p sh
```

Cần rất thận trọng vì bạn đang thay đổi góc nhìn runtime, và shell với privilege cao có thể tác động production workload.

## Vì sao `docker exec` dễ dùng hơn?

Container runtime biết namespace/cgroup/filesystem context và tạo process mới trong container context.

`docker exec` hay `kubectl exec` là abstraction cao hơn; `nsenter` cho thấy primitive Linux bên dưới.

# Debug một container “localhost works nhưng host không vào được”

Bắt đầu từ container namespace:

```bash
ss -lntp
```

Nếu app bind:

```text
127.0.0.1:8080
```

thì nó chỉ listen loopback trong container namespace.

Nếu bind:

```text
0.0.0.0:8080
```

thì tiếp tục kiểm tra container port publishing, veth/bridge/NAT/firewall.

Không nên kết luận “Docker network lỗi” trước khi xác nhận bind address.

# Debug container OOM

Flow:

```text
process biến mất
↓
container exit reason
↓
cgroup memory events
↓
host kernel log
↓
JVM/container memory configuration
```

Các evidence có thể gồm:

```bash
cat /proc/<PID>/cgroup
journalctl -k | grep -i -E 'oom|killed process'
```

Trong Docker/Kubernetes dùng runtime/orchestrator-specific status để xem OOMKilled.

# Những hiểu lầm phổ biến

**“Namespace giới hạn CPU/RAM.”** Không. Cgroup làm resource accounting/control.

**“Container root luôn bằng host root.”** Không nếu user namespace remapping được dùng; nhưng nhiều deployment vẫn có direct root mapping nên phải kiểm tra.

**“Cgroup CPU limit nghĩa container có core riêng.”** Thường là scheduling quota/weight, không phải hardware ownership.

**“Host còn RAM thì container không thể OOM.”** Sai nếu cgroup memory limit nhỏ hơn.

**“Seccomp và SELinux là cùng một thứ.”** Không. Seccomp filter syscalls; SELinux/AppArmor áp mandatory access policy.

**“Privileged container chỉ thêm vài quyền.”** Nó có thể mở rất rộng nhiều kernel/device boundaries.

# Mô hình tư duy

Khi debug isolation, hỏi bốn câu riêng:

1. **Tôi đang ở namespace nào?**
2. **Cgroup nào đang giới hạn workload?**
3. **Process có capabilities nào?**
4. **Syscall/security policy nào có thể chặn operation?**

Phân tách bốn câu này biến “container permission/network/resource issue” thành một problem có cấu trúc.

Xem thêm: [Linux và containers](./linux_containers.md), [Bộ nhớ và virtual memory](../06_resources/memory_virtual_memory.md), [Networking](../07_networking/networking_dns_sockets_ports.md), [Security hardening](../08_operations/security_hardening.md).