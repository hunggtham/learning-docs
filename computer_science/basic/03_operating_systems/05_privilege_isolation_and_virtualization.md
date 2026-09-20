# Privilege, isolation, containers và virtualization

Chạy nhiều workloads an toàn cần giới hạn “ai có thể làm gì” và “resource nào họ nhìn thấy”. CPU privilege, process address spaces, OS permissions, namespaces, cgroups và virtual machines là các layers khác nhau của isolation.

## Protection rings và privilege

CPU có privileged execution modes. Kernel dùng privileged instructions để quản lý memory/devices; user code bị giới hạn. System call là controlled gate.

Privilege separation giảm blast radius: browser tab, database process hay app server không nên có kernel quyền. Nhưng bug trong kernel/driver có thể phá toàn machine vì chạy ở trust level cao.

## User, group và capabilities

OS authorization model có identities và permissions. Unix mode bits chia owner/group/others với read/write/execute; ACLs mở rộng granularity. Root traditionally có rộng quyền, nhưng Linux capabilities tách privileges như bind low port, raw network, admin operations thành units nhỏ hơn.

Principle of least privilege yêu cầu process chỉ có quyền thực sự cần.

## Virtual machines

Hypervisor virtualize hardware để guest OS tưởng có machine riêng. Type-1 hypervisor chạy gần hardware; hosted virtualization có thêm host OS layer tùy architecture.

Hardware virtualization extensions hỗ trợ trap/emulate privileged operations và nested page translation. VM isolation mạnh vì guest có kernel riêng, nhưng footprint/boot overhead lớn hơn process container.

## Containers

Container không phải mini-VM theo nghĩa có kernel riêng. Linux containers chủ yếu dùng namespaces để isolate views (PID, mount, network, user...), cgroups để limit/account resources, capabilities/seccomp/LSM để giảm privileges, cùng filesystem layers.

Containers trên cùng host share kernel. Kernel vulnerability vì vậy có thể cross container boundary nếu controls bị bypass.

## Namespace vs cgroup

Namespace trả lời “process nhìn thấy cái gì?” Cgroup trả lời “process được dùng bao nhiêu resource/được account thế nào?” Hai mechanisms bổ sung nhau.

Memory cgroup limit có thể OOM-kill workload dù host còn memory. CPU quota/throttling làm latency spikes. Production debugging phải nhìn container limits chứ không chỉ host metrics.

## Sandbox

Sandbox giới hạn capabilities của untrusted code bằng process isolation, syscall filters, language/runtime restrictions hoặc VM. Browser renderers, mobile apps và serverless runtimes dùng nhiều layers.

Sandbox security luôn phụ thuộc attack surface của boundary; parser/IPC/kernel bugs có thể escape.

## Virtualization và emulation

Virtualization thường chạy guest instructions trực tiếp hoặc gần trực tiếp trên compatible hardware, trapping sensitive operations. Emulation mô phỏng architecture khác và có thể chạy ISA khác nhưng thường overhead cao hơn. Apple Rosetta-style binary translation nằm giữa: translate instruction sets động/tĩnh.

## Containers không thay thế security design

Image isolation không sửa SQL injection, broken authorization hay secrets leak. Container là one boundary trong defense-in-depth. Workload vẫn cần application security, network policy và identity controls.

## Mental Model

> Isolation được xây bằng nhiều boundaries: **CPU privilege → process/VM address isolation → OS identity/capability → namespace/resource controls → application authorization**. Boundary càng sâu thường càng mạnh nhưng chi phí khác nhau.

## Common Misconceptions

**“Container có kernel riêng.”** Thông thường container share host kernel.

**“VM luôn an toàn tuyệt đối.”** Hypervisor/device emulation cũng có vulnerabilities; isolation mạnh hơn không nghĩa invulnerable.

**“Root trong container = root toàn host.”** User namespaces/capabilities có thể hạn chế, nhưng privileged container hoặc misconfiguration có thể gần host-root; cần xem actual boundary.

## Kết nối

[Kernel privilege](./00_kernel_syscalls_and_os_abstractions.md) và [virtual memory](./03_virtual_memory_and_address_spaces.md) là nền. Security principles ở [threat models](../07_security_reliability/00_threat_models_and_security_principles.md); deployment boundaries ở [software systems](../08_software_systems/03_state_queues_backpressure_and_boundaries.md).
