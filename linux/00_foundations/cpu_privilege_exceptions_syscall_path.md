# CPU privilege, exception và đường đi của system call

Chương [Kernel, không gian người dùng và lời gọi hệ thống](./kernel_userspace_syscalls.md) giải thích vì sao ứng dụng phải đi qua kernel để truy cập tài nguyên. Chương này đi sâu hơn một tầng: **CPU thực sự làm gì khi một chương trình từ user space đi vào kernel, vì sao system call khác interrupt và exception, trạng thái nào được lưu, và tại sao việc “vào kernel” không đồng nghĩa với đổi sang process khác**.

Mục tiêu không phải học assembly để viết kernel. Mục tiêu là có một mô hình đủ chính xác để hiểu các khái niệm như system call overhead, page fault, signal delivery, context switch, privilege ring, CPU exception và kernel stack.

## CPU không biết khái niệm “ứng dụng Java”

Ở tầng phần cứng, CPU không nhìn thấy khái niệm Spring Boot, Python hay shell. CPU chỉ thực thi instruction trong một trạng thái nhất định: thanh ghi, program counter, stack pointer, page table đang hoạt động và mức đặc quyền hiện tại.

Hệ điều hành xây dựng các lớp trừu tượng cao hơn như process, thread, file descriptor và socket bằng cách sử dụng các cơ chế phần cứng này.

Một thread Java đang chạy cuối cùng vẫn là một luồng instruction được CPU thực thi. Khi thread chỉ cộng số hoặc thao tác dữ liệu đã nằm trong bộ nhớ của chính nó, CPU có thể tiếp tục chạy ở **chế độ người dùng (user mode)**. Khi thread cần đọc file, chờ socket hoặc xin thêm mapping bộ nhớ, nó phải đi qua giao diện kernel.

## Mức đặc quyền tồn tại để bảo vệ hệ thống

Kiến trúc CPU cung cấp các mức đặc quyền để giới hạn instruction và vùng bộ nhớ mà mã đang chạy có thể truy cập.

Trên x86 thường nói tới các **ring**. Linux chủ yếu sử dụng ring 3 cho user space và ring 0 cho kernel. Trên ARM có mô hình exception level khác, nhưng ý tưởng nền tảng tương tự: mã ứng dụng không được quyền thực hiện mọi thao tác mà kernel có thể làm.

Không nên đồng nhất Linux với một kiến trúc CPU cụ thể. Điều quan trọng là mô hình:

```text
mức đặc quyền thấp
application / runtime / library
        ↓
ranh giới được CPU kiểm soát
        ↓
mức đặc quyền cao
kernel
```

Nếu user process có thể tùy ý sửa page table, cấu hình interrupt controller hoặc ghi vào memory của kernel thì mọi cơ chế permission phía trên gần như mất ý nghĩa.

## User space và kernel space còn là ranh giới địa chỉ

Mỗi process có không gian địa chỉ ảo riêng. Một phần address space dành cho user process; kernel có vùng riêng được bảo vệ theo thiết kế kiến trúc và cấu hình hệ thống.

CPU kết hợp page table và bit quyền trên page table entry để kiểm soát việc truy cập. Vì vậy một con trỏ trong user process không thể đơn giản trỏ tới kernel memory rồi đọc nội dung.

Nếu process truy cập địa chỉ không hợp lệ, CPU có thể tạo ra một exception như page fault. Kernel nhận sự kiện đó và quyết định:

- ánh xạ trang nếu đây là fault hợp lệ;
- mở rộng mapping nếu semantics cho phép;
- hoặc gửi signal như `SIGSEGV` nếu truy cập không hợp lệ.

Điểm quan trọng là nhiều hành vi mà lập trình viên nhìn thấy ở tầng process thực ra bắt đầu từ exception của CPU rồi được kernel chuyển thành semantics của Unix.

## Ba con đường phổ biến làm CPU đi vào kernel

Có thể chia thành ba nhóm khái niệm lớn.

### System call

Process chủ động yêu cầu kernel thực hiện công việc:

```text
read()
write()
openat()
connect()
mmap()
```

Đây là chuyển giao **đồng bộ và có chủ ý** từ chương trình.

### Exception

Instruction hiện tại tạo ra tình huống CPU phải chuyển quyền điều khiển cho kernel. Ví dụ:

- page fault;
- chia cho 0;
- instruction không hợp lệ;
- breakpoint/debug trap.

Exception gắn với luồng instruction đang thực thi.

### Hardware interrupt

Thiết bị hoặc bộ điều khiển báo một sự kiện bất đồng bộ, ví dụ NIC báo có packet hoặc storage báo I/O hoàn tất.

Interrupt không nhất thiết liên quan trực tiếp tới instruction user-space đang chạy lúc đó.

Ba nhóm đều có thể đưa CPU vào kernel, nhưng nguyên nhân và semantics rất khác nhau.

Xem thêm [Interrupt, softirq và device model](./interrupts_softirq_device_model.md).

## Đường đi khái niệm của một system call

Giả sử chương trình gọi:

```c
read(fd, buffer, 4096)
```

Ở mức khái niệm, đường đi có thể hình dung:

```text
application
    ↓
libc/runtime wrapper
    ↓
đặt syscall number + arguments vào vị trí ABI quy định
    ↓
CPU instruction chuyển vào kernel
    ↓
kernel entry code
    ↓
kiểm tra / dispatch system call
    ↓
VFS / filesystem / socket / subsystem tương ứng
    ↓
trả kết quả hoặc errno
    ↓
CPU quay lại user mode
```

Chi tiết register và instruction phụ thuộc kiến trúc. Trên x86-64 thường có instruction `syscall`; các kiến trúc khác dùng cơ chế tương ứng.

Điều cần hiểu là system call không phải function call bình thường. Nó đi qua một **privilege boundary** với quy tắc ABI và entry/exit riêng.

## ABI là hợp đồng giữa binary và kernel

**Application Binary Interface (ABI)** quy định cách binary giao tiếp ở mức máy: calling convention, register, layout và system call interface.

API là giao diện ở mức source code. ABI là hợp đồng ở mức binary.

Ví dụ chương trình C gọi `read()`. Source code nhìn thấy API của libc. Nhưng libc phải biết ABI kernel để đặt đúng syscall number và arguments.

Đây là lý do binary compatibility khác source compatibility.

## Vì sao thư viện thường đứng trước system call?

Runtime hoặc libc có thể:

- chuẩn hóa API;
- xử lý buffer;
- chuyển đổi lỗi;
- chọn system call phù hợp;
- thực hiện fast path ở user space nếu có thể.

Ví dụ một số thao tác thời gian có thể tận dụng **vDSO (virtual dynamic shared object)** để đọc thông tin mà không cần trap vào kernel ở mọi lần gọi.

Vì thế khi profiling không nên suy luận rằng mọi API hệ thống đều gây một kernel entry thực sự.

## vDSO và ý tưởng tránh system call không cần thiết

Một system call có chi phí. Với những thông tin kernel có thể công bố an toàn qua vùng memory đặc biệt, Linux có thể cung cấp vDSO để user process gọi code được ánh xạ sẵn.

Các API thời gian là ví dụ điển hình trên nhiều hệ thống.

Ý tưởng lớn hơn là: **ranh giới privilege chỉ nên đi qua khi thực sự cần kernel thực hiện thao tác đặc quyền hoặc đồng bộ trạng thái**.

## Kernel stack khác user stack

Mỗi thread có user-space stack dùng khi chạy code ứng dụng. Khi CPU đi vào kernel để xử lý system call hoặc exception, kernel cần vùng stack phù hợp để xử lý kernel code.

Không nên hình dung kernel tiếp tục dùng nguyên user stack như không có ranh giới bảo mật. Kernel duy trì ngữ cảnh riêng để xử lý an toàn.

Khái niệm này giúp hiểu vì sao thread có cả trạng thái user-space lẫn kernel-side state.

## Điều gì phải được bảo toàn khi vào kernel?

CPU và entry code phải giữ đủ trạng thái để sau khi xử lý xong có thể quay lại đúng nơi trong user program.

Khái niệm cần bảo toàn gồm:

- instruction pointer;
- stack pointer;
- flags/status register;
- register cần thiết;
- thông tin privilege trước đó.

Kernel còn phải biết thread nào đang chạy để liên kết system call với credentials, file descriptor table, memory mappings và scheduling state tương ứng.

## System call có luôn chạy ngay đến cuối không?

Không.

`read()` trên dữ liệu đã có trong page cache có thể hoàn tất nhanh. Nhưng `read()` trên socket chưa có dữ liệu có thể phải chờ.

Nếu thread không thể tiếp tục, kernel có thể đặt thread vào trạng thái ngủ rồi scheduler chọn thread khác chạy.

Do đó một system call có hai khả năng rất khác:

```text
fast path
user -> kernel -> xử lý nhanh -> user
```

hoặc:

```text
user -> kernel -> phải chờ
                  ↓
            thread sleep
                  ↓
          scheduler chạy thread khác
                  ↓
             sự kiện xảy ra
                  ↓
            thread được wake
                  ↓
              quay về user
```

Đây là điểm nối trực tiếp giữa system call, wait queue và scheduler.

## Blocking không có nghĩa CPU đứng yên

Khi thread Java gọi socket read và chưa có dữ liệu, thread đó có thể ngủ. CPU không nhất thiết chờ cùng nó; scheduler có thể chạy thread khác.

Vì thế “request đang chờ I/O 200 ms” không có nghĩa CPU đã tiêu thụ 200 ms.

Đây là nền tảng để phân biệt:

- wall-clock latency;
- CPU time;
- off-CPU time.

Xem [Quan sát bằng strace, perf và eBPF](../09_production/observability_tracing_strace_perf.md).

## Context switch khác syscall entry

Giả sử thread A gọi `getpid()` và kernel trả ngay. CPU có thể:

```text
A user mode
→ A kernel mode
→ A user mode
```

mà không chuyển sang thread B.

Đây là **mode switch**, không phải nhất thiết là **context switch**.

Nếu A gọi `read()` rồi ngủ và scheduler chạy B:

```text
A user
→ A kernel
→ scheduler
→ B
```

lúc này có context switch giữa scheduling entities.

Phân biệt này quan trọng khi đọc metrics context switch và đánh giá syscall overhead.

## Page fault là exception nhưng không luôn là lỗi

Tên “fault” dễ gây cảm giác đây là sự cố. Trong virtual memory, page fault có thể là một phần hoạt động hoàn toàn bình thường.

Ví dụ process truy cập page được `mmap()` nhưng chưa được đưa vào RAM. CPU phát hiện page table chưa có mapping hiện diện và tạo exception. Kernel kiểm tra VMA, lấy page phù hợp rồi cập nhật page table.

Nếu mọi thứ hợp lệ, process tiếp tục như chưa có lỗi ở tầng ứng dụng.

Chỉ khi địa chỉ hoặc quyền không hợp lệ, kernel mới có thể chuyển thành `SIGSEGV` hoặc lỗi tương ứng.

Xem [Page fault, allocator và reclaim](../06_resources/virtual_memory_page_fault_reclaim_allocator.md).

## Signal delivery liên quan gì tới ranh giới kernel?

Signal là trạng thái do kernel quản lý. Khi cần giao signal cho process/thread, kernel phải sắp xếp để user-space handler chạy trong ngữ cảnh phù hợp.

Signal không phải một function call trực tiếp từ process gửi sang process khác. Process gửi yêu cầu qua kernel; kernel kiểm tra quyền, đánh dấu pending signal và giao theo semantics tương ứng.

Điều này giải thích vì sao `SIGKILL` không thể bị user-space handler bắt: kernel quyết định kết thúc process trước khi user code có cơ hội override semantics đó.

## Preemption và việc kernel có thể bị ngắt

Kernel hiện đại không đơn giản là một đoạn code “chạy xong rồi mới nhường CPU”. Tùy cấu hình và context, kernel có cơ chế preemption, interrupt handling và synchronization phức tạp.

Một CPU đang chạy kernel code có thể vẫn nhận interrupt. Tuy nhiên không phải mọi kernel context đều cho phép sleep hoặc schedule.

Đây là lý do kernel cần nhiều primitive đồng bộ khác nhau thay vì chỉ một loại mutex.

Xem [Đồng thời, khóa và RCU trong kernel](./kernel_concurrency_locking_rcu.md).

## Security: syscall boundary là nơi chính sách gặp yêu cầu

Khi process gọi `openat()`, kernel không chỉ tìm file. Kernel còn xem:

- credentials của task;
- permission mode/ACL;
- namespace;
- mount policy;
- LSM như SELinux/AppArmor;
- seccomp policy nếu có.

Một system call vì vậy là điểm mà **ý định của application** gặp **trạng thái và chính sách của kernel**.

Đây là mental model rất hữu ích khi đọc `EPERM` hoặc `EACCES`: thay vì hỏi “Linux có lỗi không?”, hãy hỏi lớp policy nào đã từ chối operation nào.

## Seccomp lọc system call như thế nào về mặt ý tưởng?

Seccomp có thể hạn chế tập system call hoặc mẫu argument mà process được phép sử dụng tùy policy.

Container runtime thường tận dụng cơ chế này để giảm attack surface. Nếu application không cần một syscall nguy hiểm, việc chặn nó làm giảm khả năng mã bị khai thác dùng syscall đó.

Seccomp không thay thế filesystem permission, capability hay namespace. Nó là thêm một lớp kiểm soát tại syscall boundary.

## Quan sát system call bằng `strace`

Ví dụ:

```bash
strace -tt -T -f -o /tmp/app.strace curl -s http://127.0.0.1:8080/health
```

Một số option:

- `-tt`: timestamp chi tiết;
- `-T`: thời gian ở mỗi syscall;
- `-f`: theo dõi child/thread phù hợp;
- `-o`: ghi ra file.

Không nên đọc `strace` như danh sách ngẫu nhiên. Hãy tìm câu hỏi cụ thể:

```text
đang chờ connect()?
đang lặp openat() vì thiếu file?
read() bị block lâu?
futex() chờ lock?
ENOENT ở path nào?
```

## `strace` có overhead

Tracing system call làm thay đổi timing. Với workload latency-sensitive hoặc throughput cao, attach `strace` có thể tạo overhead đáng kể.

Production diagnosis phải cân bằng lượng evidence với ảnh hưởng quan sát.

Khi cần quan sát nhẹ hơn hoặc aggregate nhiều event, eBPF/perf có thể phù hợp hơn tùy mục tiêu.

## System CPU time nói điều gì?

Trong `top`, `vmstat` hoặc metrics, thời gian CPU thường được chia thành user/system và các nhóm khác.

`system` cao nghĩa CPU đang thực thi kernel code nhiều hơn. Nguyên nhân có thể là:

- syscall rate cao;
- network packet processing;
- filesystem work;
- page fault/reclaim;
- locking/kernel overhead;
- driver/interrupt-related work.

Không nên nhảy thẳng tới kết luận kernel bug.

## Mental Model

Hãy hình dung một thread có hai “mặt” liên tục của cùng một execution context:

```text
user-space execution
        ↓ system call / exception
kernel execution thay mặt thread đó
        ↓ return / wakeup
user-space execution tiếp tục
```

Kernel không phải một process riêng mà application “gửi request” qua network. Kernel code có thể chạy trực tiếp trên CPU trong context của thread đang gọi, hoặc trong interrupt/kernel worker context tùy loại công việc.

## Những hiểu lầm phổ biến

**“System call luôn tạo context switch.”** Không. Nó tạo privilege transition; context switch chỉ xảy ra nếu scheduler đổi scheduling entity.

**“Page fault nghĩa là chương trình lỗi.”** Nhiều page fault là cơ chế demand paging bình thường.

**“Kernel mode nghĩa là chạy PID 0 hoặc process kernel riêng.”** Kernel code có thể chạy trong context của task hiện tại hoặc interrupt/kernel thread context; không nên dùng một mental model duy nhất cho mọi trường hợp.

**“Function C nào đọc file cũng trực tiếp là system call.”** Runtime/library có thể buffer hoặc dùng cơ chế khác; API và syscall không luôn 1:1.

**“System CPU cao chứng minh kernel đang gặp lỗi.”** Nó chỉ chứng minh nhiều CPU time đang ở kernel; cần tìm subsystem tạo công việc đó.

## Knowledge Connection

Chương này nối trực tiếp với:

- [Kernel, user space và system call](./kernel_userspace_syscalls.md) — mô hình tổng quan;
- [Interrupt, softirq và device model](./interrupts_softirq_device_model.md) — đường vào kernel từ phần cứng;
- [Đồng thời và synchronization trong kernel](./kernel_concurrency_locking_rcu.md) — bảo vệ dữ liệu khi kernel chạy song song;
- [Process và address space](../04_process/process_address_space_fork_exec_wait.md) — task mà syscall đang thay mặt;
- [Virtual memory](../06_resources/virtual_memory_page_fault_reclaim_allocator.md) — page fault và mapping;
- [Tracing](../09_production/observability_tracing_strace_perf.md) — quan sát những cơ chế này khi hệ thống đang chạy.
