# Bộ chứa (container / 컨테이너) internals: namespaces, cgroups, capabilities và seccomp

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Bộ chứa (container / 컨테이너) internals: namespaces, cgroups, capabilities và seccomp**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. bộ chứa (container / 컨테이너) không phải một thành phần nguyên thủy (primitive / 기본 요소) duy nhất** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. không gian tên (namespace / 네임스페이스) thay đổi “thế giới nhìn thấy”** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối containers với namespaces, cgroups, capabilities và seccomp, để đánh giá isolation theo từng lớp thay vì gọi container là VM.

Bộ chứa (container / 컨테이너) thường được mô tả như “máy ảo nhẹ”, nhưng mô hình tư duy (mental model / 사고 모델) đó dễ dẫn đến hiểu sai. Một bộ chứa (container / 컨테이너) Linux thông thường **không có kernel riêng**. Các tiến trình (process / 프로세스) trong bộ chứa (container / 컨테이너) vẫn là tiến trình (process / 프로세스) của kernel host; cảm giác “một máy riêng” được tạo bởi nhiều cơ chế kernel phối hợp để thay đổi những gì tiến trình (process / 프로세스) có thể nhìn thấy, sử dụng và thực hiện.

Chapter này nối [kernel execution](./00_kernel_execution_contexts_and_syscall_path.md), [scheduler](./01_scheduler_run_queues_fairness_and_latency.md), [virtual memory](./03_virtual_memory_page_tables_tlb_shootdown_and_huge_pages.md) và [filesystem](./04_filesystem_crash_consistency_journaling_and_cow.md) thành một hệ thống isolation thực tế.

## 1. bộ chứa (container / 컨테이너) không phải một thành phần nguyên thủy (primitive / 기본 요소) duy nhất

Linux không có một syscall kiểu `create_container()`. thời gian chạy (runtime / 런타임) như `runc` hoặc containerd phối hợp nhiều cơ chế:

```text
namespaces     -> thay đổi view của process
cgroups        -> quản lý và giới hạn tài nguyên
capabilities   -> chia nhỏ đặc quyền root
seccomp        -> lọc syscall
filesystem     -> tạo root filesystem riêng
LSM            -> SELinux/AppArmor policy
```

Docker/Kubernetes xây lớp trừu tượng (abstraction / 추상화) cao hơn trên các thành phần nguyên thủy (primitive / 기본 요소) này.

> bộ chứa (container / 컨테이너) là một **hợp đồng cô lập (isolation contract)** được ghép từ nhiều cơ chế kernel, không phải một lớp ảo hóa duy nhất.

> **Chuyển mạch:** Container là tổ hợp namespaces, cgroups và security controls; namespace đổi thế giới nhìn thấy, còn PID 1 nhận trách nhiệm signal/reaping riêng trong không gian đó.

## 2. không gian tên (namespace / 네임스페이스) thay đổi “thế giới nhìn thấy”

**không gian tên (namespace / 네임스페이스)** làm cho cùng một kernel đối tượng (object / 객체) có thể xuất hiện khác nhau với các nhóm tiến trình (process / 프로세스) khác nhau.

PID không gian tên (namespace / 네임스페이스) tạo cây tiến trình (process / 프로세스) riêng. tiến trình (process / 프로세스) có thể thấy mình là PID 1 bên trong bộ chứa (container / 컨테이너) dù kernel host gán PID khác.

Mount không gian tên (namespace / 네임스페이스) cho mỗi nhóm tiến trình (process / 프로세스) một view mount riêng. mạng (network / 네트워크) không gian tên (namespace / 네임스페이스) cung cấp giao diện (interface / 인터페이스), routing bảng (table / 테이블), socket không gian tên (namespace / 네임스페이스) và firewall ngữ cảnh (context / 맥락) riêng. UTS không gian tên (namespace / 네임스페이스) cô lập hostname; IPC không gian tên (namespace / 네임스페이스) cô lập một số IPC đối tượng (object / 객체); người dùng (user / 사용자) không gian tên (namespace / 네임스페이스) ánh xạ UID/GID giữa bên trong và host.

Điểm quan trọng: không gian tên (namespace / 네임스페이스) chủ yếu giải quyết **visibility và naming**, không tự giới hạn lượng CPU/RAM mà tiến trình (process / 프로세스) tiêu thụ.

> **Chuyển mạch:** Ở chặng này của **Bộ chứa (container / 컨테이너) internals: namespaces, cgroups, capabilities và seccomp**, **3. PID 1 trong bộ chứa (container / 컨테이너) có ý nghĩa đặc biệt** tiếp nhận điểm tựa từ **2. không gian tên (namespace / 네임스페이스) thay đổi “thế giới nhìn thấy”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Mount không gian tên (namespace / 네임스페이스) và gốc (root / 루트) filesystem** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. PID 1 trong bộ chứa (container / 컨테이너) có ý nghĩa đặc biệt

Tiến trình (process / 프로세스) đầu tiên của PID không gian tên (namespace / 네임스페이스) trở thành PID 1 trong không gian tên (namespace / 네임스페이스) đó. PID 1 có ngữ nghĩa (semantics / 의미론) tín hiệu (signal / 신호) và trách nhiệm thu gom tiến trình (process / 프로세스) con khác tiến trình (process / 프로세스) bình thường.

Nếu ứng dụng (application / 애플리케이션) chạy trực tiếp làm PID 1 nhưng không `wait()` child tiến trình (process / 프로세스) đúng cách, zombie có thể tích tụ. Đây là lý do một số ảnh (image / 이미지) dùng init nhỏ như `tini`.

Vấn đề này cho thấy lớp trừu tượng (abstraction / 추상화) bộ chứa (container / 컨테이너) không xóa ngữ nghĩa (semantics / 의미론) của OS; ngược lại, ứng dụng (application / 애플리케이션) đôi khi tiếp xúc trực tiếp hơn với chúng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ chứa (container / 컨테이너) internals: namespaces, cgroups, capabilities và seccomp**, **4. Mount không gian tên (namespace / 네임스페이스) và gốc (root / 루트) filesystem** tiếp nhận điểm tựa từ **3. PID 1 trong bộ chứa (container / 컨테이너) có ý nghĩa đặc biệt** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. mạng (network / 네트워크) không gian tên (namespace / 네임스페이스) tạo mạng (network / 네트워크) ngăn xếp (stack / 스택) lô-gic (logic / 논리) riêng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Mount không gian tên (namespace / 네임스페이스) và gốc (root / 루트) filesystem

Bộ chứa (container / 컨테이너) có thể thấy một filesystem cây (tree / 트리) khác nhờ mount không gian tên (namespace / 네임스페이스) kết hợp `pivot_root`/`chroot` và layered filesystem. ảnh (image / 이미지) tầng (layer / 계층) thường bất biến; writable tầng (layer / 계층) của bộ chứa (container / 컨테이너) nằm phía trên.

**Sao chép khi ghi (copy-on-write / CoW)** cho phép nhiều bộ chứa (container / 컨테이너) chia sẻ tầng (layer / 계층) gốc. Khi một bộ chứa (container / 컨테이너) sửa tệp (file / 파일), khối (block / 블록) hoặc tệp (file / 파일) tương ứng được tạo ở writable tầng (layer / 계층) của nó.

Điều này tiết kiệm lưu trữ (storage / 저장소) nhưng có chi phí siêu dữ liệu (metadata / 메타데이터) và I/O. cơ sở dữ liệu (database / 데이터베이스) có tải công việc (workload / 워크로드) ghi nặng thường không nên coi writable ảnh (image / 이미지) tầng (layer / 계층) như lưu trữ (storage / 저장소) bền vững chính; volume/bind mount phù hợp hơn.

> **Chuyển mạch:** Trong **Bộ chứa (container / 컨테이너) internals: namespaces, cgroups, capabilities và seccomp**, **5. mạng (network / 네트워크) không gian tên (namespace / 네임스페이스) tạo mạng (network / 네트워크) ngăn xếp (stack / 스택) lô-gic (logic / 논리) riêng** tiếp nhận điểm tựa từ **4. Mount không gian tên (namespace / 네임스페이스) và gốc (root / 루트) filesystem** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Cgroups giải quyết tài nguyên (resource / 자원) accounting và điều khiển (control / 제어)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. mạng (network / 네트워크) không gian tên (namespace / 네임스페이스) tạo mạng (network / 네트워크) ngăn xếp (stack / 스택) lô-gic (logic / 논리) riêng

Một bộ chứa (container / 컨테이너) có thể có giao diện (interface / 인터페이스) `eth0` riêng dù đó chỉ là một đầu của cặp `veth`. Đầu kia nằm ở host hoặc không gian tên (namespace / 네임스페이스) khác và thường nối vào cầu nối (bridge / 브리지).

```text
container eth0
     |
   veth pair
     |
host bridge
     |
physical NIC
```

Packet có thể đi qua routing, NAT, conntrack và firewall quy tắc (rule / 규칙). Vì vậy “bộ chứa (container / 컨테이너) networking” vẫn là networking Linux; lớp trừu tượng (abstraction / 추상화) cao hơn chỉ tự động cấu hình đường đi.

Khi gỡ lỗi (debug / 디버그) độ trễ (latency / 지연 시간) hoặc packet mất mát (loss / 손실), cần biết packet thực sự đi qua những không gian tên (namespace / 네임스페이스) và quy tắc (rule / 규칙) nào thay vì chỉ nhìn dịch vụ (service / 서비스) name của Kubernetes.

> **Chuyển mạch:** Ở chặng này của **Bộ chứa (container / 컨테이너) internals: namespaces, cgroups, capabilities và seccomp**, **5. mạng (network / 네트워크) không gian tên (namespace / 네임스페이스) tạo mạng (network / 네트워크) ngăn xếp (stack / 스택) lô-gic (logic / 논리) riêng** nêu điều cần giải thích; **6. Cgroups giải quyết tài nguyên (resource / 자원) accounting và điều khiển (control / 제어)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **7. CPU quota không tương đương CPU riêng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Cgroups giải quyết tài nguyên (resource / 자원) accounting và điều khiển (control / 제어)

**Nhóm điều khiển (control groups / cgroups / 제어 그룹)** nhóm tiến trình (process / 프로세스) để kernel theo dõi và kiểm soát tài nguyên. Cgroup v2 cung cấp hierarchy thống nhất cho CPU, bộ nhớ (memory / 메모리), I/O, tiến trình (process / 프로세스) count và các controller khác.

Không gian tên (namespace / 네임스페이스) trả lời “tiến trình (process / 프로세스) nhìn thấy gì”; cgroup trả lời “tiến trình (process / 프로세스) được dùng bao nhiêu”. Hai khái niệm thường xuất hiện cùng bộ chứa (container / 컨테이너) nhưng giải quyết vấn đề khác nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ chứa (container / 컨테이너) internals: namespaces, cgroups, capabilities và seccomp**, **6. Cgroups giải quyết tài nguyên (resource / 자원) accounting và điều khiển (control / 제어)** nêu điều cần giải thích; **7. CPU quota không tương đương CPU riêng** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **8. giới hạn bộ nhớ (memory limit / 메모리 제한) và OOM trong bộ chứa (container / 컨테이너)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. CPU quota không tương đương CPU riêng

Một bộ chứa (container / 컨테이너) được quota 1 CPU không nhất thiết sở hữu một cốt lõi (core / 핵심) vật lý riêng. Scheduler vẫn phân phối runnable tác vụ (task / 작업) trên CPU host theo cpuset, weight và quota.

Quota có thể được mô hình hóa bằng ngân sách CPU trong một khoảng thời gian. Khi dùng hết ngân sách, cgroup bị **điều tiết (throttling)** cho tới kỳ tiếp theo. ứng dụng (application / 애플리케이션) có thể thấy tail độ trễ (latency / 지연 시간) tăng dù host chưa đạt 100% CPU trung bình.

Đây là lý do chỉ số (metric / 지표) `CPU usage` đơn lẻ không đủ. Cần quan sát throttled thời gian (time / 시간), run hàng đợi (queue / 큐) và độ trễ (latency / 지연 시간) phân phối (distribution / 분포).

> **Chuyển mạch:** Trong **Bộ chứa (container / 컨테이너) internals: namespaces, cgroups, capabilities và seccomp**, **7. CPU quota không tương đương CPU riêng** đã nêu tiêu chí phân biệt, còn **8. giới hạn bộ nhớ (memory limit / 메모리 제한) và OOM trong bộ chứa (container / 컨테이너)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **9. người dùng (user / 사용자) không gian tên (namespace / 네임스페이스) và gốc (root / 루트) không nhất thiết là host gốc (root / 루트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. giới hạn bộ nhớ (memory limit / 메모리 제한) và OOM trong bộ chứa (container / 컨테이너)

Bộ nhớ (memory / 메모리) cgroup theo dõi mức dùng bộ nhớ và có thể áp limit. Khi cgroup không thể reclaim đủ bộ nhớ (memory / 메모리) dưới giới hạn, kernel có thể kích hoạt **OOM trong phạm vi cgroup** thay vì giết tiến trình (process / 프로세스) ngẫu nhiên trên toàn host.

Nhưng bộ nhớ (memory / 메모리) accounting không đơn giản chỉ là vùng nhớ động (heap / 힙) của ứng dụng (application / 애플리케이션). Page bộ nhớ đệm (cache / 캐시), anonymous bộ nhớ (memory / 메모리) và một số kernel bộ nhớ (memory / 메모리) cũng ảnh hưởng tùy cấu hình/kernel.

Một JVM đặt vùng nhớ động (heap / 힙) gần bằng bộ chứa (container / 컨테이너) giới hạn bộ nhớ (memory limit / 메모리 제한) có thể vẫn bị OOMKill vì bản địa (native / 네이티브) bộ nhớ (memory / 메모리), luồng thực thi (thread / 스레드) ngăn xếp (stack / 스택), direct buffer, JIT siêu dữ liệu (metadata / 메타데이터) và page bộ nhớ đệm (cache / 캐시) cần không gian riêng.

> **Chuyển mạch:** Ở chặng này của **Bộ chứa (container / 컨테이너) internals: namespaces, cgroups, capabilities và seccomp**, **8. giới hạn bộ nhớ (memory limit / 메모리 제한) và OOM trong bộ chứa (container / 컨테이너)** đã nêu tiêu chí phân biệt, còn **9. người dùng (user / 사용자) không gian tên (namespace / 네임스페이스) và gốc (root / 루트) không nhất thiết là host gốc (root / 루트)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **10. Linux capabilities chia nhỏ quyền gốc (root / 루트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. người dùng (user / 사용자) không gian tên (namespace / 네임스페이스) và gốc (root / 루트) không nhất thiết là host gốc (root / 루트)

Người dùng (user / 사용자) không gian tên (namespace / 네임스페이스) cho phép UID 0 bên trong không gian tên (namespace / 네임스페이스) ánh xạ sang UID không đặc quyền trên host. Điều này giảm hậu quả nếu tiến trình (process / 프로세스) thoát khỏi một số ranh giới (boundary / 경계).

Tuy nhiên, “rootless” không tự động có nghĩa là an toàn tuyệt đối. Kernel vẫn là dùng chung (shared / 공유) attack surface và cấu hình không gian tên (namespace / 네임스페이스)/năng lực (capability / 역량)/filesystem vẫn quan trọng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ chứa (container / 컨테이너) internals: namespaces, cgroups, capabilities và seccomp**, **10. Linux capabilities chia nhỏ quyền gốc (root / 루트)** tiếp nhận điểm tựa từ **9. người dùng (user / 사용자) không gian tên (namespace / 네임스페이스) và gốc (root / 루트) không nhất thiết là host gốc (root / 루트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Seccomp thu hẹp syscall surface** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Linux capabilities chia nhỏ quyền gốc (root / 루트)

Unix truyền thống có mô hình gần như nhị phân: gốc (root / 루트) hoặc không gốc (root / 루트). **Năng lực đặc quyền (Linux capabilities)** chia quyền gốc (root / 루트) thành các quyền nhỏ hơn như `CAP_NET_BIND_SERVICE`, `CAP_SYS_ADMIN`, `CAP_NET_ADMIN`.

Bộ chứa (container / 컨테이너) nên chỉ giữ năng lực (capability / 역량) thực sự cần. `CAP_SYS_ADMIN` đặc biệt rộng và thường được xem như một năng lực (capability / 역량) rất nhạy cảm.

Nguyên tắc ở đây là **đặc quyền tối thiểu (least privilege)**: ứng dụng (application / 애플리케이션) web không cần quyền quản trị mạng (network / 네트워크) hoặc mount filesystem chỉ vì nó chạy trong bộ chứa (container / 컨테이너).

> **Chuyển mạch:** Trong **Bộ chứa (container / 컨테이너) internals: namespaces, cgroups, capabilities và seccomp**, **11. Seccomp thu hẹp syscall surface** tiếp nhận điểm tựa từ **10. Linux capabilities chia nhỏ quyền gốc (root / 루트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. bộ chứa (container / 컨테이너) escape và dùng chung (shared / 공유) kernel** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Seccomp thu hẹp syscall surface

**Seccomp** cho phép lọc syscall mà tiến trình (process / 프로세스) được phép gọi. Nếu ứng dụng (application / 애플리케이션) không bao giờ cần `ptrace`, `mount` hoặc một syscall nguy hiểm khác, chính sách (policy / 정책) có thể chặn chúng.

Điều này không sửa lỗ hổng trong kernel, nhưng giảm tập đường đi mà attacker có thể dùng sau khi chiếm được tiến trình (process / 프로세스). bảo mật (security / 보안) thường mạnh hơn khi nhiều lớp độc lập cùng giới hạn attacker:

```text
namespace
+ non-root UID
+ dropped capabilities
+ seccomp
+ AppArmor/SELinux
+ read-only filesystem
```

> **Chuyển mạch:** Ở chặng này của **Bộ chứa (container / 컨테이너) internals: namespaces, cgroups, capabilities và seccomp**, **12. bộ chứa (container / 컨테이너) escape và dùng chung (shared / 공유) kernel** tiếp nhận điểm tựa từ **11. Seccomp thu hẹp syscall surface** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Cgroups và Kubernetes requests/limits** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. bộ chứa (container / 컨테이너) escape và dùng chung (shared / 공유) kernel

VM thường đặt guest sau ranh giới (boundary / 경계) hypervisor và guest kernel riêng. bộ chứa (container / 컨테이너) chia sẻ kernel host. Nếu attacker khai thác được kernel vulnerability thông qua syscall surface có thể truy cập, không gian tên (namespace / 네임스페이스) không còn là ranh giới (boundary / 경계) tuyệt đối.

Do đó threat mô hình (model / 모델) quyết định isolation technology. Multi-tenant tải công việc (workload / 워크로드) không tin cậy có thể cần VM, microVM hoặc sandbox bổ sung thay vì chỉ bộ chứa (container / 컨테이너) tiêu chuẩn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ chứa (container / 컨테이너) internals: namespaces, cgroups, capabilities và seccomp**, **12. bộ chứa (container / 컨테이너) escape và dùng chung (shared / 공유) kernel** đã nêu tiêu chí phân biệt, còn **13. Cgroups và Kubernetes requests/limits** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **14. Noisy neighbor** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Cgroups và Kubernetes requests/limits

Kubernetes `requests` và `limits` cuối cùng phải được chuyển thành thành phần nguyên thủy (primitive / 기본 요소) của OS/thời gian chạy (runtime / 런타임). CPU yêu cầu (request / 요청) chủ yếu ảnh hưởng scheduling/weight; Giới hạn CPU (CPU limit / CPU 제한) có thể thành quota. giới hạn bộ nhớ (memory limit / 메모리 제한) trở thành giới hạn cgroup và có thể dẫn tới OOMKill.

Điều này giải thích tại sao hiểu Kubernetes mà không hiểu scheduler, bộ nhớ (memory / 메모리) reclaim và cgroups sẽ tạo khoảng trống mô hình tư duy (mental model / 사고 모델). YAML chỉ là lớp cấu hình; hành vi cuối cùng xảy ra trong kernel.

> **Chuyển mạch:** Trong **Bộ chứa (container / 컨테이너) internals: namespaces, cgroups, capabilities và seccomp**, **13. Cgroups và Kubernetes requests/limits** đã nêu tiêu chí phân biệt, còn **14. Noisy neighbor** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **15. gỡ lỗi (debug / 디버그) từ bộ chứa (container / 컨테이너) xuống kernel** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Noisy neighbor

Hai bộ chứa (container / 컨테이너) trên cùng host vẫn chia sẻ nhiều tài nguyên: LLC bộ nhớ đệm (cache / 캐시), bộ nhớ (memory / 메모리) bandwidth, lưu trữ (storage / 저장소) hàng đợi (queue / 큐), NIC, kernel khóa (lock / 잠금) và đôi khi NUMA topology. Cgroup giúp kiểm soát một số tài nguyên nhưng không biến host thành các máy vật lý độc lập hoàn toàn.

Một tải công việc (workload / 워크로드) có thể không vượt Giới hạn CPU (CPU limit / CPU 제한) nhưng vẫn làm tải công việc (workload / 워크로드) khác chậm do bộ nhớ (memory / 메모리) bandwidth hoặc I/O contention. Đây là **ảnh hưởng hàng xóm ồn (noisy-neighbor effect)**.

> **Chuyển mạch:** Ở chặng này của **Bộ chứa (container / 컨테이너) internals: namespaces, cgroups, capabilities và seccomp**, **15. gỡ lỗi (debug / 디버그) từ bộ chứa (container / 컨테이너) xuống kernel** tiếp nhận điểm tựa từ **14. Noisy neighbor** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. gỡ lỗi (debug / 디버그) từ bộ chứa (container / 컨테이너) xuống kernel

Khi bộ chứa (container / 컨테이너) “chậm”, cần phân tách các lớp:

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

`docker stats` hoặc dashboard Kubernetes chỉ là điểm bắt đầu. môi trường vận hành (production / 운영 환경) debugging sâu cần nối chỉ số (metric / 지표) ở orchestration tầng (layer / 계층) với kernel bằng chứng (evidence / 증거).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ chứa (container / 컨테이너) internals: namespaces, cgroups, capabilities và seccomp**, **Dùng chung (common / 공통) Misconceptions** tiếp nhận điểm tựa từ **15. gỡ lỗi (debug / 디버그) từ bộ chứa (container / 컨테이너) xuống kernel** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“bộ chứa (container / 컨테이너) là VM nhẹ.”** Hữu ích như phép so sánh ban đầu nhưng sai nếu hiểu theo kiến trúc: bộ chứa (container / 컨테이너) thường chia sẻ host kernel.

**“không gian tên (namespace / 네임스페이스) tạo ranh giới bảo mật (security boundary / 보안 경계) hoàn chỉnh.”** không gian tên (namespace / 네임스페이스) cô lập view; ranh giới bảo mật (security boundary / 보안 경계) thực tế cần năng lực (capability / 역량), seccomp, LSM, filesystem permission và kernel bảo mật (security / 보안).

**“Giới hạn CPU (CPU limit / CPU 제한) 1 nghĩa là có một CPU riêng.”** Không. Nó thường là quota/weight trên scheduler dùng chung.

**“giới hạn bộ nhớ (memory limit / 메모리 제한) chỉ giới hạn Java vùng nhớ động (heap / 힙).”** Không. thời gian chạy (runtime / 런타임) còn dùng bản địa (native / 네이티브) bộ nhớ (memory / 메모리) và hệ thống còn nhiều loại bộ nhớ (memory / 메모리) accounting khác.

> **Chuyển mạch:** Trong **Bộ chứa (container / 컨테이너) internals: namespaces, cgroups, capabilities và seccomp**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Dùng chung (common / 공통) Misconceptions** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> bộ chứa (container / 컨테이너) là một tiến trình (process / 프로세스) bình thường được đặt trong một **thế giới quan bị giới hạn**, một **ngân sách tài nguyên**, và một **tập quyền bị thu hẹp**.

Khi lớp trừu tượng (abstraction / 추상화) bộ chứa (container / 컨테이너) gây khó hiểu, hãy bóc nó trở lại tiến trình (process / 프로세스), không gian tên (namespace / 네임스페이스), cgroup, syscall, filesystem và scheduler. Đây cũng là cách lập luận (reasoning / 추론) hiệu quả khi gỡ lỗi (debug / 디버그) Docker và Kubernetes.

Xem tiếp: [Kernel execution contexts](./00_kernel_execution_contexts_and_syscall_path.md), [Security](../../07_security_reliability/advanced/README.md) và [Architecture](../../02_computer_architecture/advanced/README.md).

> **Bàn giao:** Giữ lại bốn boundary trước khi rời chapter: namespace chỉ cô lập view, cgroup phân bổ ngân sách, capability/seccomp thu hẹp quyền và kernel vẫn là shared substrate. Sang [Kernel execution contexts](./00_kernel_execution_contexts_and_syscall_path.md) để theo dõi syscall/privilege, hoặc [Security advanced](../../07_security_reliability/advanced/README.md) khi câu hỏi chuyển sang threat boundary; quay về [README](./README.md) để xác nhận owner.
