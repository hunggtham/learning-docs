# Privilege, isolation, containers và virtualization

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Privilege, isolation, containers và virtualization**. Route đi từ protection rings/capabilities → user/group/namespace → container boundary → hypervisor/VM và threat model, để “isolation” được đánh giá bằng quyền có thể vượt qua.

Chạy nhiều workloads an toàn cần giới hạn “ai có thể làm gì” và “tài nguyên (resource / 자원) nào họ nhìn thấy”. CPU privilege, tiến trình (process / 프로세스) address spaces, OS permissions, namespaces, cgroups và virtual machines là các layers khác nhau của isolation.

## Protection rings và privilege

CPU có privileged thực thi (execution / 실행) modes. Kernel dùng privileged instructions để quản lý bộ nhớ (memory / 메모리)/devices; người dùng (user / 사용자) mã (code / 코드) bị giới hạn. lời gọi hệ thống (system call / 시스템 호출) là controlled gate.

Privilege separation giảm blast radius: trình duyệt (browser / 브라우저) tab, cơ sở dữ liệu (database / 데이터베이스) tiến trình (process / 프로세스) hay app máy chủ (server / 서버) không nên có kernel quyền. Nhưng bug trong kernel/driver có thể phá toàn machine vì chạy ở trust mức (level / 수준) cao.

> **Nối mạch:** **Người dùng (user / 사용자), group và capabilities** nối từ **Protection rings và privilege** sang **Virtual machines**, vì cơ chế trước tạo đầu vào cho bước sau.

## Người dùng (user / 사용자), group và capabilities

OS authorization mô hình (model / 모델) có identities và permissions. Unix chế độ (mode / 모드) bits chia đơn vị sở hữu (owner / 오너)/group/others với read/ghi (write / 쓰기)/execute; ACLs mở rộng granularity. gốc (root / 루트) traditionally có rộng quyền, nhưng Linux capabilities tách privileges như bind low cổng (port / 포트), raw mạng (network / 네트워크), admin operations thành units nhỏ hơn.

Principle of least privilege yêu cầu tiến trình (process / 프로세스) chỉ có quyền thực sự cần.

> **Nối mạch:** **Virtual machines** nối từ **Người dùng (user / 사용자), group và capabilities** sang **Containers**, vì cơ chế trước tạo đầu vào cho bước sau.

## Virtual machines

Hypervisor virtualize hardware để guest OS tưởng có machine riêng. Type-1 hypervisor chạy gần hardware; hosted virtualization có thêm host OS tầng (layer / 계층) tùy kiến trúc (architecture / 아키텍처).

Hardware virtualization extensions hỗ trợ trap/emulate privileged operations và nested page translation. VM isolation mạnh vì guest có kernel riêng, nhưng footprint/boot overhead lớn hơn tiến trình (process / 프로세스) bộ chứa (container / 컨테이너).

> **Nối mạch:** **Containers** nối từ **Virtual machines** sang **Không gian tên (namespace / 네임스페이스) vs cgroup**, vì cơ chế trước tạo đầu vào cho bước sau.

## Containers

Bộ chứa (container / 컨테이너) không phải mini-VM theo nghĩa có kernel riêng. Linux containers chủ yếu dùng namespaces để isolate views (PID, mount, network, user...), cgroups để limit/account resources, capabilities/seccomp/LSM để giảm privileges, cùng filesystem layers.

Containers trên cùng host share kernel. Kernel vulnerability vì vậy có thể cross bộ chứa (container / 컨테이너) ranh giới (boundary / 경계) nếu controls bị bypass.

> **Nối mạch:** **Không gian tên (namespace / 네임스페이스) vs cgroup** nối từ **Containers** sang **Sandbox**, vì cơ chế trước tạo đầu vào cho bước sau.

## Không gian tên (namespace / 네임스페이스) vs cgroup

Không gian tên (namespace / 네임스페이스) trả lời “tiến trình (process / 프로세스) nhìn thấy cái gì?” Cgroup trả lời “tiến trình (process / 프로세스) được dùng bao nhiêu tài nguyên (resource / 자원)/được account thế nào?” Hai mechanisms bổ sung nhau.

Bộ nhớ (memory / 메모리) cgroup limit có thể OOM-kill tải công việc (workload / 워크로드) dù host còn bộ nhớ (memory / 메모리). CPU quota/throttling làm độ trễ (latency / 지연 시간) spikes. môi trường vận hành (production / 운영 환경) debugging phải nhìn bộ chứa (container / 컨테이너) limits chứ không chỉ host metrics.

> **Nối mạch:** **Sandbox** nối từ **Không gian tên (namespace / 네임스페이스) vs cgroup** sang **Virtualization và emulation**, vì cơ chế trước tạo đầu vào cho bước sau.

## Sandbox

Sandbox giới hạn capabilities của untrusted mã (code / 코드) bằng tiến trình (process / 프로세스) isolation, syscall filters, ngôn ngữ (language / 언어)/thời gian chạy (runtime / 런타임) restrictions hoặc VM. trình duyệt (browser / 브라우저) renderers, mobile apps và serverless runtimes dùng nhiều layers.

Sandbox bảo mật (security / 보안) luôn phụ thuộc attack surface của ranh giới (boundary / 경계); parser/IPC/kernel bugs có thể escape.

> **Nối mạch:** **Virtualization và emulation** nối từ **Sandbox** sang **Containers không thay thế bảo mật (security / 보안) thiết kế (design / 설계)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Virtualization và emulation

Virtualization thường chạy guest instructions trực tiếp hoặc gần trực tiếp trên compatible hardware, trapping sensitive operations. Emulation mô phỏng kiến trúc (architecture / 아키텍처) khác và có thể chạy ISA khác nhưng thường overhead cao hơn. Apple Rosetta-style nhị phân (binary / 이진) translation nằm giữa: translate instruction sets động/tĩnh.

> **Nối mạch:** **Containers không thay thế bảo mật (security / 보안) thiết kế (design / 설계)** nối từ **Virtualization và emulation** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Containers không thay thế bảo mật (security / 보안) thiết kế (design / 설계)

Ảnh (image / 이미지) isolation không sửa SQL injection, broken authorization hay secrets leak. bộ chứa (container / 컨테이너) là one ranh giới (boundary / 경계) trong defense-in-depth. tải công việc (workload / 워크로드) vẫn cần ứng dụng (application / 애플리케이션) bảo mật (security / 보안), chính sách mạng (network policy / 네트워크 정책) và định danh (identity / 식별자) controls.

> **Nối mạch:** **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Containers không thay thế bảo mật (security / 보안) thiết kế (design / 설계)**; **Dùng chung (common / 공통) Misconceptions** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> Isolation được xây bằng nhiều boundaries: **CPU privilege → tiến trình (process / 프로세스)/VM address isolation → OS định danh (identity / 식별자)/năng lực (capability / 역량) → không gian tên (namespace / 네임스페이스)/tài nguyên (resource / 자원) controls → ứng dụng (application / 애플리케이션) authorization**. ranh giới (boundary / 경계) càng sâu thường càng mạnh nhưng chi phí khác nhau.

> **Nối mạch:** **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)**; **Kết nối** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Dùng chung (common / 공통) Misconceptions

**“bộ chứa (container / 컨테이너) có kernel riêng.”** Thông thường bộ chứa (container / 컨테이너) share host kernel.

**“VM luôn an toàn tuyệt đối.”** Hypervisor/thiết bị (device / 장치) emulation cũng có vulnerabilities; isolation mạnh hơn không nghĩa invulnerable.

**“gốc (root / 루트) trong bộ chứa (container / 컨테이너) = gốc (root / 루트) toàn host.”** người dùng (user / 사용자) namespaces/capabilities có thể hạn chế, nhưng privileged bộ chứa (container / 컨테이너) hoặc misconfiguration có thể gần host-root; cần xem actual ranh giới (boundary / 경계).

> **Nối mạch:** **Kết nối** tổng hợp từ **Dùng chung (common / 공통) Misconceptions**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Kết nối

[Kernel privilege](./00_kernel_syscalls_and_os_abstractions.md) và [virtual memory](./03_virtual_memory_and_address_spaces.md) là nền. bảo mật (security / 보안) principles ở [threat models](../07_security_reliability/00_threat_models_and_security_principles.md); triển khai (deployment / 배포) boundaries ở [software systems](../08_software_systems/03_state_queues_backpressure_and_boundaries.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
