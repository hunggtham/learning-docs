# Process, address space, fork, exec và wait trong Linux

Chương [Tiến trình, luồng, tín hiệu và tác vụ](./processes_threads_signals_jobs.md) cung cấp mô hình tổng quan về process. Chương này đi sâu hơn vào cách Linux thực sự biểu diễn một process/thread, address space của nó gồm những vùng nào, `fork()` tạo process con ra sao, `execve()` thay chương trình thế nào, vì sao zombie tồn tại và cách `wait()` hoàn tất vòng đời process.

Đây là nền tảng để hiểu shell, systemd, container, JVM, signal, memory leak, file descriptor inheritance và nhiều hiện tượng production khác.

## Process không phải chỉ là PID

PID là một mã định danh trong một PID namespace. Bên trong kernel, execution context cần nhiều trạng thái hơn rất nhiều:

- scheduling state;
- CPU register state khi bị deschedule;
- memory mappings;
- credentials;
- file descriptor table;
- signal state;
- namespace membership;
- cgroup membership;
- parent/child relationship;
- accounting information.

Trong Linux source, một khái niệm trung tâm là `task_struct`, đại diện cho task mà scheduler có thể quản lý. Người học không cần thuộc field của cấu trúc này, nhưng mental model quan trọng là:

> Một task là một object kernel nối nhiều subsystem lại với nhau.

## Process và thread trong Linux

Linux có cách nhìn thống nhất hơn nhiều hệ điều hành giáo khoa: thread cũng là một task có thể được scheduler chạy. Nhiều thread trong cùng process chia sẻ một số resource, đặc biệt address space và file descriptor table, tùy cách được tạo bằng `clone()`/`clone3()`.

Vì vậy ranh giới process/thread có thể hiểu bằng câu hỏi:

```text
những tài nguyên nào được chia sẻ?
```

Hai task có thể:

- chia sẻ memory nhưng có stack/register riêng;
- chia sẻ file descriptor table;
- chia sẻ signal handlers;
- cùng thuộc một thread group.

Một JVM process với 200 Java thread tương ứng nhiều scheduling entities ở Linux, không phải một đối tượng CPU duy nhất.

## PID, TID và thread group

Trong thực tế Linux, mỗi thread có một task ID riêng. Main thread thường có ID trùng process ID theo cách user-space nhìn thấy. Các thread cùng process thuộc một **thread group**.

Quan sát:

```bash
ps -L -p <PID> -o pid,tid,psr,stat,comm
```

hoặc:

```bash
ls /proc/<PID>/task
```

Mỗi entry dưới `/proc/<PID>/task/` đại diện một thread/task.

Điều này rất hữu ích khi mapping Java thread dump với Linux thread CPU usage.

## Address space của process

Một process nhìn thấy một không gian địa chỉ ảo riêng.

Có thể quan sát mapping:

```bash
cat /proc/<PID>/maps
pmap -x <PID>
```

Một process điển hình có các vùng:

```text
text / executable code
read-only data
writable data
heap
memory-mapped libraries/files
anonymous mappings
thread stacks
vdso/vvar
```

Không nên coi address space là một mảng RAM vật lý liên tục. Đây là một tập các **VMA (Virtual Memory Area)** có permission và backing khác nhau.

Xem sâu hơn tại [Virtual memory, page fault và reclaim](../06_resources/virtual_memory_page_fault_reclaim_allocator.md).

## Code, data, heap và stack

Mô hình giáo khoa thường chia process thành code/data/heap/stack. Đây vẫn hữu ích nhưng thực tế Linux phức tạp hơn do `mmap()`.

Heap truyền thống có thể tăng qua `brk()`, nhưng allocator hiện đại có thể dùng cả `mmap()` cho allocation lớn.

Thread stack cũng là mapping trong address space.

Shared libraries được map vào address space thông qua dynamic linker.

Do đó nhìn RSS hoặc VSZ mà không hiểu mapping dễ dẫn tới kết luận sai.

## `/proc/<PID>/maps` giải thích gì?

Ví dụ một dòng mapping:

```text
7f1234000000-7f1234200000 r-xp ... /usr/lib/libc.so.6
```

Các trường cho biết range địa chỉ, permission và backing file.

Permission thường có:

- `r`: read;
- `w`: write;
- `x`: execute;
- `p`: private mapping;
- `s`: shared mapping.

Mapping `r-x` thường chứa code thực thi. Mapping `rw-` chứa dữ liệu có thể ghi.

Đây là nền tảng để hiểu W^X, ASLR và exploit mitigation.

## ASLR

**Address Space Layout Randomization (ASLR)** làm vị trí nhiều mapping thay đổi giữa các lần chạy để giảm khả năng exploit dự đoán địa chỉ.

```bash
cat /proc/sys/kernel/randomize_va_space
```

ASLR không sửa bug memory safety, nhưng làm một số exploit khó hơn.

PIE binary và shared library có thể phối hợp với ASLR.

Xem thêm [ELF và dynamic linking](../08_operations/elf_dynamic_linking.md).

## Tạo process: `fork()` không copy toàn bộ RAM ngay

Mô hình Unix cổ điển:

```text
parent
  ↓ fork()
parent + child
```

Một hiểu lầm thường gặp là kernel copy toàn bộ memory của parent ngay lập tức. Linux dùng **Copy-on-Write (COW)**.

Sau `fork()`, parent và child có thể tạm thời chia sẻ cùng physical pages dưới permission phù hợp. Khi một bên ghi vào page, page fault xảy ra và kernel tạo bản sao riêng cho bên ghi.

Mental model:

```text
trước fork:
parent -> page A

sau fork, trước write:
parent ─┐
        ├-> page A
child  ─┘

child write:
parent -> page A
child  -> copy page B
```

Nhờ đó `fork()` thường rẻ hơn rất nhiều so với copy toàn bộ memory ngay lập tức.

## COW không có nghĩa fork luôn rẻ

Dù data pages chưa copy, kernel vẫn phải tạo hoặc quản lý metadata như page tables và task state. Process rất lớn có thể khiến fork có chi phí đáng kể.

Nếu child sau đó ghi nhiều memory, COW faults và copy pages tạo thêm chi phí.

Đây là lý do runtime/database lớn có thể quan tâm sâu tới behavior của fork.

## `fork()` và multi-threaded process

Trong process nhiều thread, `fork()` tạo child chỉ với thread gọi fork theo POSIX semantics điển hình. Các lock trong process có thể đang ở trạng thái phức tạp vì thread khác biến mất trong child.

Vì vậy child của multi-threaded process thường cần nhanh chóng `exec()` thay vì tiếp tục chạy logic tùy ý.

Đây là một trong những lý do spawn process trong runtime phức tạp cần implementation cẩn thận.

## `clone()` và Linux thread

Linux sử dụng `clone()`/`clone3()` cho phép caller chọn resource nào được chia sẻ.

Các flag có thể quyết định việc chia sẻ:

- virtual memory;
- filesystem state;
- file descriptor table;
- signal handlers;
- namespace.

Thread có thể được xem như các task tạo bằng clone với tập chia sẻ phù hợp.

Container runtime cũng tận dụng clone/unshare/setns để xây namespace isolation.

## `execve()` không tạo PID mới

Đây là một điểm nền tảng rất quan trọng.

`execve()` **thay program image của process hiện tại**. PID không nhất thiết đổi.

Mental model:

```text
process PID 123
đang chạy shell
    ↓ execve(java,...)
process PID 123
bây giờ chạy Java image
```

Address space cũ được thay bằng mappings của executable/library mới; stack mới được dựng với arguments/environment.

Vì vậy `exec` không có nghĩa “tạo process con”.

## Shell chạy command ngoài thế nào?

Một mô hình đơn giản:

```text
shell
  ↓ fork/clone-like creation
child
  ↓ setup redirection / fd
  ↓ execve("/usr/bin/grep", ...)
grep process
```

Parent shell có thể `wait()` child ở foreground hoặc tiếp tục nếu job chạy background.

Pipeline:

```bash
cat file | grep ERROR | sort
```

đòi hỏi shell tạo pipe, tạo nhiều process, nối file descriptor đúng đầu rồi `exec()` từng command.

Do đó shell syntax cuối cùng dựa trên process lifecycle + file descriptor inheritance.

## File descriptor inheritance

Sau `fork()`, child thường kế thừa file descriptor table semantics từ parent.

Điều này cho phép shell chuẩn bị redirection trước `exec()`:

```text
open output file
fork
child dup2(output_fd, STDOUT)
exec program
```

Program mới không cần biết shell đã setup redirection ra sao. Nó chỉ thấy fd 1 là stdout bình thường.

Đây là sức mạnh của Unix composition.

## `FD_CLOEXEC`

Không phải file descriptor nào cũng nên sống qua `exec()`.

Flag **close-on-exec** yêu cầu kernel đóng descriptor khi exec thành công.

Nếu ứng dụng quên đặt close-on-exec đúng chỗ, child process có thể vô tình giữ socket/file descriptor mà nó không cần.

Hậu quả có thể gồm:

- file không được giải phóng;
- pipe không nhận EOF;
- socket vẫn bị giữ;
- security boundary bị rò resource.

Vì vậy descriptor lifetime là một phần của process lifecycle.

## Environment được đưa vào exec

`execve()` nhận argument vector và environment vector.

Environment không phải database toàn cục. Nó là dữ liệu được truyền vào process image.

Khi shell:

```bash
export APP_ENV=prod
java -jar app.jar
```

child/exec image nhận environment tương ứng.

Process đã chạy không tự thấy các thay đổi environment của parent sau đó.

## Current working directory

Process giữ current working directory như một reference tới filesystem object.

Do đó file relative path được resolve dựa trên cwd của process.

```bash
readlink /proc/<PID>/cwd
```

Một process có thể giữ cwd trong filesystem đang cố unmount, khiến `umount` báo busy.

Đây là ví dụ process state nối trực tiếp với VFS lifetime.

## Root directory của process

Process có khái niệm root directory dùng khi resolve absolute path. `chroot()` có thể thay góc nhìn này, nhưng không phải isolation mạnh tương đương container.

Mount namespace và pivot_root giúp container runtime xây filesystem view riêng sâu hơn.

## Credentials qua fork/exec

Child thường kế thừa credentials từ parent, nhưng exec có thể tương tác với setuid/setgid, capabilities và security policy.

Kernel phải tính effective credentials cẩn thận khi executable có metadata đặc quyền.

Xem [Credentials, capabilities, ACL và MAC](../03_identity/credentials_capabilities_acl_mac.md).

## Signal disposition qua exec

Một số signal disposition thay đổi qua exec theo POSIX semantics. Pending state và mask có quy tắc riêng.

Điểm cần nhớ: exec thay program image nhưng process object không phải “reset mọi thứ về 0”. Một số thuộc tính được giữ, một số được thay.

Đây là lý do semantics của exec là một hợp đồng rất cụ thể.

## Parent-child relationship

Process con có parent. Parent có thể cần biết child kết thúc ra sao.

Khi child exit, kernel giữ một phần exit status để parent thu nhận bằng `wait()`/`waitpid()`.

Khoảng thời gian child đã chết nhưng status chưa được parent thu nhận tạo ra **zombie**.

## Zombie chính xác là gì?

Zombie không còn chạy code và hầu hết resource đã được giải phóng. Kernel vẫn giữ entry tối thiểu gồm PID và exit status để parent có thể wait.

Quan sát:

```bash
ps -eo pid,ppid,stat,cmd | awk '$3 ~ /Z/'
```

Zombie ít thường không tiêu thụ nhiều tài nguyên, nhưng tích tụ lớn có thể làm cạn PID/task table và là dấu hiệu parent không reap child đúng.

## `wait()` làm gì?

Parent gọi `wait()` hoặc `waitpid()` để:

- lấy exit status;
- xác nhận child kết thúc;
- cho kernel giải phóng zombie entry.

Mental model:

```text
child exit
  ↓
kernel giữ exit record
  ↓
parent wait()
  ↓
exit status returned
  ↓
record được giải phóng
```

## Orphan khác zombie

**Orphan** là child còn sống nhưng parent đã chết.

**Zombie** là child đã chết nhưng parent chưa reap.

Hai khái niệm hoàn toàn khác nhau.

Khi parent biến mất, orphan được reparent theo semantics namespace/init/subreaper.

## PID 1 và subreaper

PID 1 có vai trò đặc biệt trong process tree. Trong container, process làm PID 1 cần xử lý signal/reaping đúng.

Systemd và các init system quản lý child lifecycle rất chặt.

Linux còn có khái niệm **child subreaper**, cho phép process nhận orphan descendant trong một số mô hình supervision.

Đây là cơ sở cho process supervisor/container init.

## Exit status

Process kết thúc với exit code hoặc do signal.

Shell dùng `$?` để xem status của command trước:

```bash
some-command
echo $?
```

Convention thường dùng 0 là thành công và khác 0 là lỗi, nhưng nghĩa cụ thể phụ thuộc chương trình.

Nếu process chết do signal, shell/runtime có thể mã hóa status theo convention riêng để báo lại.

## Process group và session

Job control cần thêm abstraction ngoài PID.

**Process group** gom nhiều process, ví dụ pipeline.

**Session** gom process group và liên hệ controlling terminal.

Khi nhấn `Ctrl+C`, terminal driver thường gửi `SIGINT` tới foreground process group, không phải chỉ một PID ngẫu nhiên.

Đây là lý do pipeline foreground có thể bị dừng cùng nhau.

## Controlling terminal

Interactive shell có controlling terminal. Foreground process group có quyền đọc input terminal.

Background process cố đọc terminal có thể bị signal như `SIGTTIN`.

Job control vì vậy là collaboration giữa shell, process groups, session và terminal driver trong kernel.

## Daemonization cổ điển

Trước systemd, daemon thường dùng pattern:

```text
fork
setsid
fork again
redirect stdio
change cwd
```

Mục tiêu là tách khỏi controlling terminal và session cũ.

Với systemd, double-fork thường không cần cho service `Type=simple`; systemd muốn theo dõi foreground main process trực tiếp.

Hiểu lịch sử này giúp giải thích vì sao một số daemon cũ có option `--foreground`.

## Process state `R`, `S`, `D`, `T`, `Z`

Các trạng thái `ps` là biểu diễn rút gọn của scheduling/task state.

- `R`: running hoặc runnable;
- `S`: interruptible sleep;
- `D`: uninterruptible sleep;
- `T`: stopped/traced;
- `Z`: zombie.

`D` thường liên quan task đang chờ I/O/kernel condition mà signal thông thường chưa làm nó rời wait ngay.

Nhiều task `D` có thể làm load average cao dù CPU idle đáng kể.

## Sleeping không phải “process không làm gì” theo nghĩa vô ích

Sleep là cách kernel biểu diễn task đang chờ event. Đây là trạng thái hiệu quả: task không chiếm CPU trong thời gian chờ.

Application server blocking I/O có thể có hàng trăm thread sleeping. Vấn đề chỉ xuất hiện khi thread count, stack memory hoặc wakeup contention vượt giới hạn hợp lý.

## Thread stack và memory cost

Mỗi thread cần stack mapping và kernel task state.

Trong JVM, `-Xss` ảnh hưởng Java thread stack size. Hàng nghìn thread có thể tiêu tốn nhiều virtual memory và resident memory dù heap chưa đầy.

Vì vậy capacity planning thread count phải nối với memory model.

## Context switch lưu gì?

Khi scheduler chuyển từ task A sang B, kernel phải bảo toàn CPU execution state đủ để A tiếp tục sau đó.

Chi phí không chỉ là lưu register. Cache/TLB locality cũng có thể bị ảnh hưởng.

Nếu hàng nghìn runnable thread cạnh tranh ít CPU, latency tăng dù mọi thread “đang hoạt động”.

Xem [Kernel scheduler deep dive](../06_resources/kernel_scheduler_deep_dive.md).

## `exec()` và deployment

Khi systemd start service:

```text
systemd
  ↓ fork/clone-like spawn
  ↓ setup credentials/cgroup/fd/env
  ↓ execve application
application process
```

Do đó unit configuration cuối cùng biến thành process attributes trước khi exec.

Environment, WorkingDirectory, User, limits và file descriptors đều có thể ảnh hưởng application trước khi dòng Java đầu tiên chạy.

## Process namespace

PID namespace làm cùng một task có thể có PID khác nhau tùy viewpoint.

Host có thể thấy PID 32100, còn container thấy PID 1.

Vì vậy PID là tên trong namespace, không phải identity tuyệt đối toàn hệ thống.

Xem [Namespace, cgroup và seccomp](../09_production/namespaces_cgroups_seccomp.md).

## `/proc/<PID>` là cửa sổ process model

Một số file hữu ích:

```text
/proc/<PID>/status
/proc/<PID>/stat
/proc/<PID>/maps
/proc/<PID>/smaps
/proc/<PID>/fd/
/proc/<PID>/task/
/proc/<PID>/limits
/proc/<PID>/cgroup
/proc/<PID>/ns/
/proc/<PID>/cwd
/proc/<PID>/exe
```

Thay vì coi `/proc` là danh sách lệnh phải nhớ, hãy map từng entry vào resource mà process đang giữ.

## Process lifetime và resource lifetime không luôn giống nhau

Một file có thể bị unlink nhưng vẫn tồn tại vì process còn giữ file descriptor.

Một shared memory object có thể được process khác giữ.

Một socket connection có peer state bên ngoài host.

Vì vậy “process đã chết” không luôn đồng nghĩa mọi hệ quả bên ngoài lập tức biến mất.

Conversely, kernel sẽ tự release nhiều resource gắn ownership trực tiếp với process khi process exit.

## Mental Model

Hãy xem process như một **container logic của execution state và references**:

```text
process/task
├── address space
├── threads
├── credentials
├── file descriptors
├── cwd/root
├── signals
├── namespaces
├── cgroups
└── parent/child lifecycle
```

`fork()` tạo execution context mới với nhiều state kế thừa/chia sẻ theo semantics. `exec()` thay program image. `exit()` kết thúc execution. `wait()` hoàn tất quan hệ lifecycle với parent.

## Những hiểu lầm phổ biến

**“fork copy toàn bộ RAM ngay.”** COW giúp parent/child chia sẻ pages cho tới khi ghi.

**“exec tạo process mới.”** Exec thay program image của process hiện tại.

**“Zombie vẫn chạy và ăn CPU.”** Zombie đã kết thúc; nó chỉ còn exit record chờ parent reap.

**“Orphan và zombie là một.”** Orphan còn sống nhưng mất parent; zombie đã chết nhưng chưa được wait.

**“PID là identity ổn định.”** PID có thể tái sử dụng và thay đổi theo PID namespace.

**“Một Java process là một scheduling entity.”** Mỗi native thread là task scheduler có thể quản lý riêng.

## Knowledge Connection

Nên nối chương này với:

- [CPU privilege và syscall path](../00_foundations/cpu_privilege_exceptions_syscall_path.md);
- [File descriptor](../01_filesystem/files_streams_descriptors.md);
- [Virtual memory](../06_resources/virtual_memory_page_fault_reclaim_allocator.md);
- [IPC](./interprocess_communication.md);
- [Scheduler](../06_resources/kernel_scheduler_deep_dive.md);
- [Systemd service lifecycle](../05_system/systemd_units_dependencies_resources.md);
- [Container isolation](../09_production/namespaces_cgroups_seccomp.md).
