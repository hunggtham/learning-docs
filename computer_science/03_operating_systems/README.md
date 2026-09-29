# Operating các hệ thống (systems / 시스템들) — lĩnh vực (domain / 도메인) Hub

> **Mạch đọc:** Đọc **Operating các hệ thống (systems / 시스템들) — lĩnh vực (domain / 도메인) Hub** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Hãy xác định đối tượng và câu hỏi trung tâm trước, rồi dùng phần này để đối chiếu với mục liên quan sau khi đã nắm mô hình tư duy (mental model / 사고 모델) chính.

Foundation nằm tại [`../basic/03_operating_systems/`](../basic/03_operating_systems/): kernel/syscall, tiến trình (process / 프로세스)/luồng thực thi (thread / 스레드), scheduling, synchronization, virtual bộ nhớ (memory / 메모리), filesystem, isolation, IPC và thiết bị (device / 장치) I/O.

Phần [`advanced/`](./advanced/README.md) đi vào kernel thực thi (execution / 실행) paths, scheduler internals, page reclaim, filesystem consistency, async I/O, namespaces/cgroups, eBPF/khả năng quan sát (observability / 관측 가능성) và các tương tác (interaction / 상호작용) giữa OS với hardware/thời gian chạy (runtime / 런타임).

> **Bàn giao:** Sau **Operating các hệ thống (systems / 시스템들) — lĩnh vực (domain / 도메인) Hub**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 kernel syscalls and os abstractions](./00_kernel_syscalls_and_os_abstractions.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
