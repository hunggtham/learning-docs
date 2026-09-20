# Kernel, system call và OS abstractions

Operating System — OS (운영체제 / hệ điều hành) giải quyết một mâu thuẫn cơ bản: nhiều programs muốn dùng cùng CPU, memory, storage và devices, nhưng nếu mỗi program điều khiển hardware trực tiếp thì isolation, portability và sharing gần như không thể quản lý. OS đặt một privileged kernel giữa applications và hardware, rồi cung cấp abstractions ổn định như process, virtual memory, file và socket.

## Kernel là phần có quyền đặc biệt

Kernel (커널) chạy ở CPU privilege level cao, quản lý page tables, interrupts, device drivers, scheduling và protected resources. User applications chạy ở user mode với quyền hạn chế.

Boundary này được hardware enforce. Nếu một process bình thường có thể sửa page table hoặc đọc arbitrary physical memory, process isolation sẽ không tồn tại.

Kernel design có nhiều dạng. Monolithic kernels như Linux đặt nhiều subsystems/drivers trong kernel space. Microkernel philosophy đẩy nhiều services ra user space và giữ kernel nhỏ hơn. Hybrid systems pha trộn. Trade-off liên quan performance, fault isolation và complexity.

## System call

System call (시스템 호출) là controlled entry từ user mode vào kernel để yêu cầu operation privileged: `read`, `write`, `open`, `mmap`, `fork`, `socket`... API language/library có thể wrap syscall; không phải mọi library call đều tạo syscall.

Ví dụ `printf` có thể format hoàn toàn trong user space rồi cuối cùng buffer được flush qua `write`. Memory allocation `malloc` có thể phục vụ từ user-space heap pool và chỉ thỉnh thoảng xin thêm pages từ OS.

System call có overhead vì privilege transition, validation và kernel work, nhưng modern kernels/runtimes tối ưu batching, shared memory và async interfaces để giảm crossings.

## File descriptor và handle

Unix-like OS dùng file descriptor — integer index vào per-process table của open resources. Files, sockets, pipes và devices có thể cùng dùng read/write-like interface. Đây là abstraction mạnh: “everything is a file” không hoàn toàn literal, nhưng uniform I/O interface làm composition dễ hơn.

Windows dùng handles rộng hơn. Principle chung là user code giữ opaque reference thay vì trực tiếp nắm kernel object.

## Process abstraction

Process cho program cảm giác có CPU execution context và address space riêng. Thực tế scheduler multiplex CPU cores giữa many runnable tasks; virtual memory maps private-looking addresses tới physical pages có thể shared/copy-on-write.

OS vì vậy là **resource multiplexer + isolation layer**.

## Virtualization của time và space

CPU virtualization: scheduling làm mỗi process có vẻ đang tiến triển.

Memory virtualization: mỗi process thấy virtual address space riêng.

Storage virtualization: filesystem biến raw blocks thành named hierarchical files.

Network virtualization: sockets cung cấp endpoint abstraction trên NIC packets.

Abstraction biến hardware details thành contracts hữu dụng nhưng không xóa constraints. CPU vẫn finite, RAM vẫn finite, disk/network vẫn có latency.

## User space và kernel space

“Kernel space” có thể nói về privileged address region/execution context; “user space” là environment của ordinary processes. Data crossing boundary thường cần validation/copy hoặc shared mapping.

Zero-copy techniques cố tránh redundant copies bằng mmap, sendfile, DMA buffers hoặc scatter/gather, nhưng semantics và security vẫn cần kiểm soát ownership/lifetime.

## Interrupt, exception và syscall

Cả ba đều có thể chuyển control vào kernel nhưng nguyên nhân khác. Hardware interrupt đến từ device/timer; exception từ instruction hiện tại như page fault; syscall là intentional request của user program theo defined convention.

Phân biệt này giúp debugging: page fault có thể normal demand paging, segmentation fault là policy reaction khi address invalid, còn syscall failure thường trả error code.

## Boot và initialization ở mức mental model

Firmware khởi tạo hardware cơ bản, bootloader load kernel, kernel setup memory/interrupts/drivers rồi start user-space init/service manager. Không cần thuộc chi tiết để hiểu rằng OS itself cũng là software phải được loaded và granted control trước khi applications chạy.

## Mental Model

> OS là **mediator có đặc quyền**. Nó multiplex finite resources, enforce isolation và expose stable abstractions. System call là cửa có kiểm soát qua boundary user ↔ kernel.

## Common Misconceptions

**“Mọi function I/O đều là syscall.”** Runtime/library buffering có thể gom nhiều operations trước khi syscall.

**“Process có CPU riêng.”** Đó là abstraction; scheduler chia cores theo time và policy.

**“Kernel là toàn bộ hệ điều hành.”** OS distribution còn có user-space libraries, daemons, shells, GUI và tools; kernel là privileged core.

## Kết nối

CPU privilege trong [CPU/ISA](../02_computer_architecture/01_cpu_isa_and_instruction_cycle.md) cho kernel quyền enforce. [Process/thread scheduling](./01_processes_threads_and_scheduling.md), [virtual memory](./03_virtual_memory_and_address_spaces.md) và [filesystem](./04_filesystems_storage_and_io.md) là ba abstractions lớn tiếp theo.
