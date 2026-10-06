# Không gian tên (namespace / 네임스페이스), cgroup, năng lực (capability / 역량) và seccomp

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Không gian tên (namespace / 네임스페이스), cgroup, năng lực (capability / 역량) và seccomp**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Không gian tên (namespace / 네임스페이스): thay đổi góc nhìn** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Mount không gian tên (namespace / 네임스페이스)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối namespaces, cgroups và seccomp, để phân biệt namespace cô lập tên gì, cgroup giới hạn tài nguyên gì và syscall nào bị chặn.

Bộ chứa (container / 컨테이너) không phải một cơ chế duy nhất. Nó là kết quả của việc ghép nhiều thành phần nguyên thủy (primitive / 기본 요소) Linux để tạo ra **góc nhìn riêng, giới hạn tài nguyên và giới hạn quyền** cho một nhóm tiến trình.

Bốn khái niệm cần tách rõ là:

- **không gian tên (namespace / 네임스페이스)** — tiến trình nhìn thấy cái gì;
- **cgroup** — tiến trình được dùng bao nhiêu tài nguyên và được accounting ra sao;
- **năng lực (capability / 역량)** — tiến trình có đặc quyền kernel nào;
- **seccomp** — tiến trình được phép gọi những lời gọi hệ thống (system call / 시스템 호출) nào.

Nếu gộp tất cả thành “bộ chứa (container / 컨테이너) isolation”, việc gỡ lỗi (debug / 디버그) và hardening sẽ rất mơ hồ.

## Không gian tên (namespace / 네임스페이스): thay đổi góc nhìn

Không gian tên (namespace / 네임스페이스) tạo một view riêng cho một loại tài nguyên (resource / 자원).

Các loại quan trọng gồm:

- PID không gian tên (namespace / 네임스페이스);
- mount không gian tên (namespace / 네임스페이스);
- mạng (network / 네트워크) không gian tên (namespace / 네임스페이스);
- UTS không gian tên (namespace / 네임스페이스);
- IPC không gian tên (namespace / 네임스페이스);
- người dùng (user / 사용자) không gian tên (namespace / 네임스페이스);
- cgroup không gian tên (namespace / 네임스페이스);
- thời gian (time / 시간) không gian tên (namespace / 네임스페이스) trên kernel hỗ trợ.

### PID không gian tên (namespace / 네임스페이스)

Một tiến trình (process / 프로세스) có thể có PID khác nhau tùy không gian tên (namespace / 네임스페이스).

Trong bộ chứa (container / 컨테이너):

```bash
ps -ef
```

có thể thấy ứng dụng (application / 애플리케이션) là PID 1.

Trên host, cùng tiến trình (process / 프로세스) có thể là PID 27481.

Điều này không phải duplication của tiến trình (process / 프로세스). Đó là cùng một kernel tác vụ (task / 작업) nhưng được nhìn qua hai PID namespaces.

Có thể inspect không gian tên (namespace / 네임스페이스) links:

```bash
ls -l /proc/<PID>/ns
```

Ví dụ:

```text
pid -> pid:[4026531836]
net -> net:[4026532001]
mnt -> mnt:[4026531999]
```

Hai processes có không gian tên (namespace / 네임스페이스) inode identifier giống nhau thường đang chia sẻ không gian tên (namespace / 네임스페이스) tương ứng.

> **Nối mạch:** Trong **Không gian tên (namespace / 네임스페이스), cgroup, năng lực (capability / 역량) và seccomp**, **Mount không gian tên (namespace / 네임스페이스)** nối từ **Không gian tên (namespace / 네임스페이스): thay đổi góc nhìn** sang **Mạng (network / 네트워크) không gian tên (namespace / 네임스페이스)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Mount không gian tên (namespace / 네임스페이스)

Mount không gian tên (namespace / 네임스페이스) cho mỗi nhóm tiến trình (process / 프로세스) có mount bảng (table / 테이블) riêng.

Bộ chứa (container / 컨테이너) có thể nhìn:

```text
/
/app
/data
```

mà không giống mount cây (tree / 트리) của host.

Do đó khi bộ chứa (container / 컨테이너) báo tệp (file / 파일) không tồn tại, phải hỏi **đường dẫn trong không gian tên (namespace / 네임스페이스) nào**.

Một tệp (file / 파일) tồn tại trên host `/opt/data/file` không có nghĩa bộ chứa (container / 컨테이너) thấy nó nếu chưa bind mount/volume.

> **Nối mạch:** Ở chặng này của **Không gian tên (namespace / 네임스페이스), cgroup, năng lực (capability / 역량) và seccomp**, **Mạng (network / 네트워크) không gian tên (namespace / 네임스페이스)** nối từ **Mount không gian tên (namespace / 네임스페이스)** sang **UTS không gian tên (namespace / 네임스페이스)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Mạng (network / 네트워크) không gian tên (namespace / 네임스페이스)

Mỗi mạng (network / 네트워크) không gian tên (namespace / 네임스페이스) có thể có:

- interfaces;
- routing bảng (table / 테이블);
- firewall ngữ cảnh (context / 맥락);
- sockets;
- loopback riêng.

Vì vậy `127.0.0.1` trong bộ chứa (container / 컨테이너) thường là loopback của bộ chứa (container / 컨테이너) không gian tên (namespace / 네임스페이스), không phải host.

Có thể tạo không gian tên (namespace / 네임스페이스) thủ công để học:

```bash
sudo ip netns add lab
sudo ip netns exec lab ip addr
```

Xóa sau khi thử:

```bash
sudo ip netns del lab
```

Đây là cách thấy bộ chứa (container / 컨테이너) networking không phải “phép thuật Docker”; Docker chỉ tự động hóa các primitives này.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Không gian tên (namespace / 네임스페이스), cgroup, năng lực (capability / 역량) và seccomp**, **UTS không gian tên (namespace / 네임스페이스)** nối từ **Mạng (network / 네트워크) không gian tên (namespace / 네임스페이스)** sang **Người dùng (user / 사용자) không gian tên (namespace / 네임스페이스)**, vì cơ chế trước tạo đầu vào cho bước sau.

## UTS không gian tên (namespace / 네임스페이스)

UTS không gian tên (namespace / 네임스페이스) tách hostname/domain-name view.

Bộ chứa (container / 컨테이너) có thể có hostname riêng dù dùng cùng host kernel.

Điều này giải thích vì sao:

```bash
hostname
```

trong bộ chứa (container / 컨테이너) có thể khác host.

> **Nối mạch:** Trong **Không gian tên (namespace / 네임스페이스), cgroup, năng lực (capability / 역량) và seccomp**, **Người dùng (user / 사용자) không gian tên (namespace / 네임스페이스)** nối từ **UTS không gian tên (namespace / 네임스페이스)** sang **Không gian tên (namespace / 네임스페이스) không phải tài nguyên (resource / 자원) limit**, vì cơ chế trước tạo đầu vào cho bước sau.

## Người dùng (user / 사용자) không gian tên (namespace / 네임스페이스)

Người dùng (user / 사용자) không gian tên (namespace / 네임스페이스) cho phép remap UID/GID.

Một tiến trình (process / 프로세스) có thể là UID 0 **bên trong không gian tên (namespace / 네임스페이스)** nhưng ánh xạ tới UID không đặc quyền trên host.

Điều này giảm rủi ro so với bộ chứa (container / 컨테이너) gốc (root / 루트) ánh xạ trực tiếp host gốc (root / 루트), nhưng ngữ nghĩa (semantics / 의미론) permission với bind mounts trở nên phức tạp hơn.

> **Nối mạch:** Ở chặng này của **Không gian tên (namespace / 네임스페이스), cgroup, năng lực (capability / 역량) và seccomp**, **Người dùng (user / 사용자) không gian tên (namespace / 네임스페이스)** đặt tiêu chí; **Không gian tên (namespace / 네임스페이스) không phải tài nguyên (resource / 자원) limit** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Bộ nhớ (memory / 메모리) cgroup** mở rộng hệ quả.

## Không gian tên (namespace / 네임스페이스) không phải tài nguyên (resource / 자원) limit

Một tiến trình (process / 프로세스) trong PID không gian tên (namespace / 네임스페이스) riêng vẫn có thể tiêu rất nhiều CPU/RAM nếu không có cgroup limit.

Không gian tên (namespace / 네임스페이스) chủ yếu giải quyết **visibility/isolation**, không phải sức chứa (capacity / 용량) điều khiển (control / 제어).

Đó là vai trò của cgroup.

# Cgroup: accounting và giới hạn tài nguyên

**điều khiển (control / 제어) group (cgroup)** gom processes vào hierarchy để kernel accounting và điều khiển (control / 제어) tài nguyên (resource / 자원) usage.

Hiện đại (modern / 현대적) distributions ngày càng dùng **cgroup v2** với unified hierarchy.

Kiểm tra:

```bash
mount | grep cgroup
stat -fc %T /sys/fs/cgroup
```

Trên cgroup v2 thường thấy kiểu (type / 타입) `cgroup2fs`.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Không gian tên (namespace / 네임스페이스), cgroup, năng lực (capability / 역량) và seccomp**, **Không gian tên (namespace / 네임스페이스) không phải tài nguyên (resource / 자원) limit** đặt tiêu chí; **Bộ nhớ (memory / 메모리) cgroup** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Host bộ nhớ (memory / 메모리) còn nhiều nhưng bộ chứa (container / 컨테이너) vẫn OOM** mở rộng hệ quả.

## Bộ nhớ (memory / 메모리) cgroup

Một bộ chứa (container / 컨테이너) có thể bị giới hạn 1 GiB dù host có 64 GiB RAM.

Trong cgroup v2, các files như:

```text
memory.current
memory.max
memory.events
```

cho thời gian chạy (runtime / 런타임) trạng thái (state / 상태) và limit.

Ví dụ:

```bash
cat /sys/fs/cgroup/memory.current
cat /sys/fs/cgroup/memory.max
cat /sys/fs/cgroup/memory.events
```

Đường dẫn (path / 경로) thực tế có thể khác tùy tiến trình (process / 프로세스) cgroup.

Tìm cgroup của PID:

```bash
cat /proc/<PID>/cgroup
```

> **Nối mạch:** Trong **Không gian tên (namespace / 네임스페이스), cgroup, năng lực (capability / 역량) và seccomp**, **Host bộ nhớ (memory / 메모리) còn nhiều nhưng bộ chứa (container / 컨테이너) vẫn OOM** nối từ **Bộ nhớ (memory / 메모리) cgroup** sang **CPU cgroup**, vì cơ chế trước tạo đầu vào cho bước sau.

## Host bộ nhớ (memory / 메모리) còn nhiều nhưng bộ chứa (container / 컨테이너) vẫn OOM

Nếu `memory.max` là 1 GiB và tiến trình (process / 프로세스) vượt giới hạn, cgroup có thể OOM-kill tải công việc (workload / 워크로드) dù:

```bash
free -h
```

trên host vẫn còn hàng chục GiB.

Đây là một trong những lỗi gỡ lỗi (debug / 디버그) bộ chứa (container / 컨테이너) phổ biến nhất.

> **Nối mạch:** Ở chặng này của **Không gian tên (namespace / 네임스페이스), cgroup, năng lực (capability / 역량) và seccomp**, **CPU cgroup** nối từ **Host bộ nhớ (memory / 메모리) còn nhiều nhưng bộ chứa (container / 컨테이너) vẫn OOM** sang **CPU throttling**, vì cơ chế trước tạo đầu vào cho bước sau.

## CPU cgroup

Cgroup có thể kiểm soát CPU quota/weight.

Một bộ chứa (container / 컨테이너) được gán “1 CPU” không nhất thiết sở hữu một cốt lõi (core / 핵심) vật lý riêng. Nó thường nhận một quota scheduling tương ứng.

Nếu Java đọc `Runtime.getRuntime().availableProcessors()`, hành vi (behavior / 동작) còn phụ thuộc JVM phiên bản (version / 버전) và bộ chứa (container / 컨테이너) awareness.

Luồng thực thi (thread / 스레드) pool sizing dựa CPU count vì vậy phải xem thời gian chạy (runtime / 런타임)/bộ chứa (container / 컨테이너) limit thật.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Không gian tên (namespace / 네임스페이스), cgroup, năng lực (capability / 역량) và seccomp**, **CPU throttling** nối từ **CPU cgroup** sang **I/O cgroup**, vì cơ chế trước tạo đầu vào cho bước sau.

## CPU throttling

Một dịch vụ (service / 서비스) có thể không đạt 100% host CPU nhưng vẫn bị throttled bởi cgroup quota.

Triệu chứng:

- độ trễ (latency / 지연 시간) tăng;
- runnable công việc (work / 작업) nhiều;
- host còn CPU idle;
- cgroup quota đã dùng hết trong period.

Đây là counterexample quan trọng cho cách nhìn host-level metrics đơn thuần.

> **Nối mạch:** Trong **Không gian tên (namespace / 네임스페이스), cgroup, năng lực (capability / 역량) và seccomp**, **I/O cgroup** nối từ **CPU throttling** sang **Vì sao bộ chứa (container / 컨테이너) không nên chạy --privileged?**, vì cơ chế trước tạo đầu vào cho bước sau.

## I/O cgroup

Cgroup cũng có thể kiểm soát/account khối (block / 블록) I/O trên kernel/lưu trữ (storage / 저장소) phù hợp.

Hai containers cùng host có thể cạnh tranh disk dù CPU/RAM tách tốt.

Vì vậy multi-tenant hiệu năng (performance / 성능) cần nhìn cả I/O tài nguyên (resource / 자원) lĩnh vực (domain / 도메인).

# Linux capabilities: chia nhỏ quyền gốc (root / 루트)

Unix truyền thống có mô hình gốc (root / 루트) rất mạnh. Linux capabilities tách một phần quyền gốc (root / 루트) thành các năng lực (capability / 역량) nhỏ hơn.

Ví dụ:

- `CAP_NET_BIND_SERVICE` — bind privileged ports;
- `CAP_NET_ADMIN` — nhiều thao tác mạng (network / 네트워크) administration;
- `CAP_SYS_ADMIN` — năng lực (capability / 역량) rất rộng và nhạy cảm;
- `CAP_SYS_PTRACE` — ptrace một số processes;
- `CAP_CHOWN` — thay quyền sở hữu (ownership / 소유권) theo chính sách (policy / 정책).

Xem năng lực (capability / 역량) của tiến trình (process / 프로세스):

```bash
grep '^Cap' /proc/<PID>/status
```

Công cụ (tool / 도구) như `capsh` hoặc `getpcaps` có thể diễn giải dễ hơn nếu được cài.

> **Nối mạch:** Ở chặng này của **Không gian tên (namespace / 네임스페이스), cgroup, năng lực (capability / 역량) và seccomp**, **Vì sao bộ chứa (container / 컨테이너) không nên chạy --privileged?** nối từ **I/O cgroup** sang **Ranh giới bảo mật (security boundary / 보안 경계) là composition**, vì cơ chế trước tạo đầu vào cho bước sau.

## Vì sao bộ chứa (container / 컨테이너) không nên chạy `--privileged`?

`--privileged` thường cấp capabilities rất rộng và thiết bị (device / 장치) truy cập (access / 접근) lớn hơn, làm nhiều isolation ranh giới (boundary / 경계) yếu đi.

Nếu ứng dụng (application / 애플리케이션) chỉ cần bind cổng (port / 포트) thấp, tốt hơn cấp đúng năng lực (capability / 역량) cần thiết thay vì full privilege.

Đây là nguyên tắc đặc quyền tối thiểu (least privilege) ở kernel mức (level / 수준).

# Seccomp: giới hạn lời gọi hệ thống (system call / 시스템 호출)

Seccomp cho phép hạn chế tập hệ thống (system / 시스템) calls tiến trình (process / 프로세스) được phép sử dụng.

Bộ chứa (container / 컨테이너) thời gian chạy (runtime / 런타임) thường dùng seccomp profile mặc định để khối (block / 블록) một số calls nguy hiểm/hiếm cần.

Nếu ứng dụng (application / 애플리케이션) bị khối (block / 블록) syscall, triệu chứng có thể là `EPERM`, tiến trình (process / 프로세스) crash hoặc nhật ký kiểm tra (audit log / 감사 로그) tùy profile/thời gian chạy (runtime / 런타임).

Seccomp không thay thế permission/năng lực (capability / 역량). Nó là một tầng (layer / 계층) khác:

```text
namespace → nhìn thấy gì
cgroup    → dùng bao nhiêu
capability→ có đặc quyền nào
seccomp   → gọi syscall nào
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **Không gian tên (namespace / 네임스페이스), cgroup, năng lực (capability / 역량) và seccomp**, **Vì sao bộ chứa (container / 컨테이너) không nên chạy --privileged?** đặt tiêu chí; **Ranh giới bảo mật (security boundary / 보안 경계) là composition** dùng tiêu chí đó để kiểm tra ranh giới, rồi **systemctl status và cgroup** mở rộng hệ quả.

## Ranh giới bảo mật (security boundary / 보안 경계) là composition

Bộ chứa (container / 컨테이너) bảo mật (security / 보안) tốt thường kết hợp:

- non-root người dùng (user / 사용자);
- người dùng (user / 사용자) không gian tên (namespace / 네임스페이스) khi phù hợp;
- drop capabilities;
- seccomp profile;
- AppArmor/SELinux;
- read-only gốc (root / 루트) filesystem;
- tài nguyên (resource / 자원) limits;
- chính sách mạng (network policy / 네트워크 정책);
- ảnh (image / 이미지) provenance;
- host kernel patching.

Không có một flag đơn lẻ biến bộ chứa (container / 컨테이너) thành sandbox tuyệt đối.

# Cgroup và systemd

Systemd sử dụng cgroups để quản lý units.

Có thể xem cây:

```bash
systemd-cgls
```

Tài nguyên (resource / 자원) settings trong đơn vị (unit / 단위):

```ini
[Service]
MemoryMax=1G
CPUQuota=100%
TasksMax=512
```

Điều này cho phép dùng cgroup controls ngay cả khi không chạy bộ chứa (container / 컨테이너).

Dịch vụ (service / 서비스) Linux truyền thống và bộ chứa (container / 컨테이너) cùng dùng kernel primitives nền tảng.

> **Nối mạch:** Trong **Không gian tên (namespace / 네임스페이스), cgroup, năng lực (capability / 역량) và seccomp**, **Ranh giới bảo mật (security boundary / 보안 경계) là composition** đặt tiêu chí; **systemctl status và cgroup** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Vì sao docker exec dễ dùng hơn?** mở rộng hệ quả.

## `systemctl status` và cgroup

`systemctl status` thường hiển thị `CGroup:` và tiến trình (process / 프로세스) cây (tree / 트리) của dịch vụ (service / 서비스).

Điều này giúp hiểu dịch vụ (service / 서비스) đơn vị (unit / 단위) không chỉ là một PID đơn lẻ; systemd theo dõi một cgroup chứa nhiều child processes.

# Không gian tên (namespace / 네임스페이스) debugging bằng `nsenter`

`nsenter` cho phép chạy command trong namespaces của tiến trình (process / 프로세스) khác.

Ví dụ vào mạng (network / 네트워크) không gian tên (namespace / 네임스페이스):

```bash
sudo nsenter -t <PID> -n ip addr
```

Vào mount không gian tên (namespace / 네임스페이스):

```bash
sudo nsenter -t <PID> -m mount
```

Kết hợp nhiều namespaces:

```bash
sudo nsenter -t <PID> -m -n -p sh
```

Cần rất thận trọng vì bạn đang thay đổi góc nhìn thời gian chạy (runtime / 런타임), và shell với privilege cao có thể tác động môi trường vận hành (production / 운영 환경) tải công việc (workload / 워크로드).

> **Nối mạch:** Ở chặng này của **Không gian tên (namespace / 네임스페이스), cgroup, năng lực (capability / 역량) và seccomp**, **Vì sao docker exec dễ dùng hơn?** nối từ **systemctl status và cgroup** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Vì sao `docker exec` dễ dùng hơn?

Bộ chứa (container / 컨테이너) thời gian chạy (runtime / 런타임) biết không gian tên (namespace / 네임스페이스)/cgroup/filesystem ngữ cảnh (context / 맥락) và tạo tiến trình (process / 프로세스) mới trong bộ chứa (container / 컨테이너) ngữ cảnh (context / 맥락).

`docker exec` hay `kubectl exec` là lớp trừu tượng (abstraction / 추상화) cao hơn; `nsenter` cho thấy thành phần nguyên thủy (primitive / 기본 요소) Linux bên dưới.

# Gỡ lỗi (debug / 디버그) một bộ chứa (container / 컨테이너) “localhost works nhưng host không vào được”

Bắt đầu từ bộ chứa (container / 컨테이너) không gian tên (namespace / 네임스페이스):

```bash
ss -lntp
```

Nếu app bind:

```text
127.0.0.1:8080
```

thì nó chỉ listen loopback trong bộ chứa (container / 컨테이너) không gian tên (namespace / 네임스페이스).

Nếu bind:

```text
0.0.0.0:8080
```

thì tiếp tục kiểm tra bộ chứa (container / 컨테이너) cổng (port / 포트) publishing, veth/cầu nối (bridge / 브리지)/NAT/firewall.

Không nên kết luận “Docker mạng (network / 네트워크) lỗi” trước khi xác nhận bind address.

# Gỡ lỗi (debug / 디버그) bộ chứa (container / 컨테이너) OOM

Luồng (flow / 흐름):

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

Các bằng chứng (evidence / 증거) có thể gồm:

```bash
cat /proc/<PID>/cgroup
journalctl -k | grep -i -E 'oom|killed process'
```

Trong Docker/Kubernetes dùng thời gian chạy (runtime / 런타임)/orchestrator-specific status để xem OOMKilled.

# Những hiểu lầm phổ biến

**“không gian tên (namespace / 네임스페이스) giới hạn CPU/RAM.”** Không. Cgroup làm tài nguyên (resource / 자원) accounting/điều khiển (control / 제어).

**“bộ chứa (container / 컨테이너) gốc (root / 루트) luôn bằng host gốc (root / 루트).”** Không nếu người dùng (user / 사용자) không gian tên (namespace / 네임스페이스) remapping được dùng; nhưng nhiều triển khai (deployment / 배포) vẫn có direct gốc (root / 루트) ánh xạ (mapping / 매핑) nên phải kiểm tra.

**“Cgroup Giới hạn CPU (CPU limit / CPU 제한) nghĩa bộ chứa (container / 컨테이너) có cốt lõi (core / 핵심) riêng.”** Thường là scheduling quota/weight, không phải hardware quyền sở hữu (ownership / 소유권).

**“Host còn RAM thì bộ chứa (container / 컨테이너) không thể OOM.”** Sai nếu cgroup giới hạn bộ nhớ (memory limit / 메모리 제한) nhỏ hơn.

**“Seccomp và SELinux là cùng một thứ.”** Không. Seccomp filter syscalls; SELinux/AppArmor áp mandatory truy cập (access / 접근) chính sách (policy / 정책).

**“Privileged bộ chứa (container / 컨테이너) chỉ thêm vài quyền.”** Nó có thể mở rất rộng nhiều kernel/thiết bị (device / 장치) boundaries.

# Mô hình tư duy

Khi gỡ lỗi (debug / 디버그) isolation, hỏi bốn câu riêng:

1. **Tôi đang ở không gian tên (namespace / 네임스페이스) nào?**
2. **Cgroup nào đang giới hạn tải công việc (workload / 워크로드)?**
3. **tiến trình (process / 프로세스) có capabilities nào?**
4. **Syscall/bảo mật (security / 보안) chính sách (policy / 정책) nào có thể chặn thao tác (operation / 연산)?**

Phân tách bốn câu này biến “bộ chứa (container / 컨테이너) permission/mạng (network / 네트워크)/tài nguyên (resource / 자원) issue” thành một bài toán (problem / 문제) có cấu trúc.

Xem thêm: [Linux và containers](./linux_containers.md), [Bộ nhớ và virtual memory](../06_resources/memory_virtual_memory.md), [Networking](../07_networking/networking_dns_sockets_ports.md), [Security hardening](../08_operations/security_hardening.md).

> **Bàn giao:** Sau **Vì sao docker exec dễ dùng hơn?**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
