# Operating các hệ thống (systems / 시스템들) — lĩnh vực (domain / 도메인) Hub

> **Mạch đọc:** [README](./README.md) là owner của **Operating các hệ thống (systems / 시스템들) — lĩnh vực (domain / 도메인) Hub**. Route học đi từ kernel/syscalls → processes/concurrency → virtual memory/filesystems/IPC → privilege, drivers và advanced systems, để mỗi chapter quay về abstraction, invariant và failure mode của OS.

Foundation nằm tại [`../basic/03_operating_systems/`](../basic/03_operating_systems/): kernel/syscall, tiến trình (process / 프로세스)/luồng thực thi (thread / 스레드), scheduling, synchronization, virtual bộ nhớ (memory / 메모리), filesystem, isolation, IPC và thiết bị (device / 장치) I/O.

Phần [`advanced/`](./advanced/README.md) đi vào kernel thực thi (execution / 실행) paths, scheduler internals, page reclaim, filesystem consistency, async I/O, namespaces/cgroups, eBPF/khả năng quan sát (observability / 관측 가능성) và các tương tác (interaction / 상호작용) giữa OS với hardware/thời gian chạy (runtime / 런타임).

> **Bàn giao:** Sau **Operating các hệ thống (systems / 시스템들) — lĩnh vực (domain / 도메인) Hub**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
