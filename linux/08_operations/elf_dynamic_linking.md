# ELF, Dynamic Linking và cách Linux chạy một chương trình

Khi gõ một lệnh như:

```bash
curl --version
```

người dùng thường hình dung đơn giản rằng shell “mở file `curl` rồi chạy”. Nhưng để một chương trình native thực sự bắt đầu chạy, Linux phải đi qua nhiều lớp: shell tìm executable trong `PATH`, kernel đọc định dạng file, bộ nạp (loader) ánh xạ các đoạn chương trình vào bộ nhớ, bộ liên kết động (dynamic linker) tìm các thư viện dùng chung, xử lý symbol relocation rồi mới chuyển quyền điều khiển tới entry point của chương trình.

Hiểu chuỗi này giúp giải thích các lỗi như:

```text
command not found
No such file or directory
error while loading shared libraries
undefined symbol
Exec format error
```

Những thông báo trên có thể trông giống nhau ở mức “chương trình không chạy”, nhưng nguyên nhân nằm ở các lớp hoàn toàn khác nhau.

## Executable không chỉ là một file có quyền `x`

Quyền thực thi (execute permission) chỉ cho biết tiến trình có được phép yêu cầu kernel thực thi file hay không. Kernel vẫn cần hiểu **định dạng file thực thi (executable format)**.

Trên Linux, định dạng phổ biến cho binary native là **ELF — Executable and Linkable Format**.

Kiểm tra:

```bash
file /usr/bin/curl
```

Kết quả có thể chứa các thông tin như:

```text
ELF 64-bit LSB pie executable, x86-64, dynamically linked, ...
```

Mỗi phần đều mang ý nghĩa:

- `ELF 64-bit`: binary theo định dạng ELF, kiến trúc 64 bit;
- `x86-64`: kiến trúc CPU mà binary được build cho;
- `PIE`: position-independent executable, cho phép load ở địa chỉ khác nhau;
- `dynamically linked`: phụ thuộc thư viện động khi chạy.

Nếu copy một binary ARM sang server x86-64 rồi chạy, kernel có thể báo `Exec format error`. Vấn đề không nằm ở permission mà nằm ở kiến trúc CPU không tương thích.

## ELF chứa những gì?

ELF không chỉ chứa machine code. Nó mô tả cách một chương trình hoặc thư viện nên được tổ chức và ánh xạ vào bộ nhớ.

Hai khái niệm thường gặp là **section** và **segment**.

Section chủ yếu phục vụ linker và tooling. Một số section quen thuộc gồm:

- `.text`: mã máy có thể thực thi;
- `.data`: dữ liệu đã khởi tạo;
- `.bss`: dữ liệu zero-initialized;
- `.rodata`: dữ liệu chỉ đọc;
- `.dynsym`: dynamic symbol table;
- `.rela.*`: relocation information.

Segment gần hơn với cách kernel/loader ánh xạ file vào virtual memory. Một segment có thể chứa nhiều sections.

Xem ELF header:

```bash
readelf -h /usr/bin/curl
```

Xem program headers:

```bash
readelf -l /usr/bin/curl
```

Xem sections:

```bash
readelf -S /usr/bin/curl
```

Mục tiêu không phải ghi nhớ output, mà hiểu rằng executable là một cấu trúc dữ liệu có metadata đủ để kernel và loader tạo process image.

## `execve()` không tạo process mới

Một hiểu lầm phổ biến là `exec` tạo process. Thực tế, trong mô hình Unix, `execve()` thay thế program image của process hiện tại.

Shell thường tạo child process rồi child gọi `execve()` để chạy chương trình mới.

```text
shell
  └─ fork/clone
       └─ child process
            └─ execve("/usr/bin/curl", ...)
```

Sau `execve()`, PID có thể giữ nguyên nhưng code, memory mappings và execution image thay đổi mạnh.

Đây là lý do phân biệt **process** với **program** rất quan trọng.

Xem thêm: [Process, Thread, Signal và Job](../04_process/processes_threads_signals_jobs.md).

## Shebang: script được chạy bằng interpreter như thế nào?

Một shell script:

```bash
#!/usr/bin/env bash

echo hello
```

không phải ELF binary. Dòng đầu `#!` gọi là **shebang**.

Khi kernel thấy file script có shebang, nó hiểu rằng file này cần một interpreter. Về mặt khái niệm:

```text
./script.sh
```

trở thành gần giống:

```text
/usr/bin/env bash ./script.sh
```

Nếu interpreter trong shebang không tồn tại, shell có thể báo lỗi dù script file rõ ràng đang tồn tại.

Đây là một nguyên nhân khiến thông báo `No such file or directory` gây hiểu nhầm: file script có thể tồn tại, nhưng interpreter mà shebang trỏ tới lại không tồn tại.

## Dynamic linking giải quyết vấn đề gì?

Nếu mỗi binary chứa bản copy riêng của mọi thư viện cần dùng, dung lượng disk và memory sẽ tăng mạnh. Cập nhật một thư viện bảo mật cũng đòi hỏi rebuild toàn bộ chương trình liên quan.

**Liên kết động (dynamic linking)** cho phép nhiều chương trình dùng chung shared libraries như:

```text
libc.so
libssl.so
libz.so
```

Binary chỉ lưu dependency và symbol references cần thiết; khi chạy, dynamic linker tìm library thích hợp và nối các symbol.

Kiểm tra library dependencies:

```bash
ldd /usr/bin/curl
```

Ví dụ:

```text
libcurl.so.4 => /lib/x86_64-linux-gnu/libcurl.so.4
libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6
```

Đây là dependency ở **runtime native layer**, khác với dependency Maven/Gradle ở Java build layer.

## Dynamic linker là chương trình nào?

ELF binary động thường chỉ định một interpreter ELF như:

```bash
readelf -l /usr/bin/curl | grep interpreter
```

Ví dụ có thể thấy:

```text
/lib64/ld-linux-x86-64.so.2
```

Dynamic linker này chạy rất sớm để load libraries và resolve symbols trước khi `main()` được gọi.

Đó là lý do một binary có thể tồn tại, có quyền execute, đúng architecture nhưng vẫn không chạy vì dynamic linker hoặc shared library thiếu.

## Tìm shared library ở đâu?

Dynamic linker có nhiều nguồn để tìm thư viện, tùy distro và binary metadata. Các nguồn có thể gồm:

- đường dẫn mặc định như `/lib`, `/usr/lib`;
- cache của `ldconfig`;
- `RPATH` hoặc `RUNPATH` trong ELF;
- biến môi trường như `LD_LIBRARY_PATH`.

Xem cache:

```bash
ldconfig -p | less
```

Xem RPATH/RUNPATH:

```bash
readelf -d ./app | grep -E 'RPATH|RUNPATH'
```

Nếu application chỉ chạy khi export:

```bash
export LD_LIBRARY_PATH=/opt/app/lib
```

thì cần hiểu đây là thay đổi cơ chế resolution, không phải “fix chung”. Trong production, phụ thuộc mạnh vào `LD_LIBRARY_PATH` có thể tạo khác biệt giữa interactive shell và systemd service.

## `ldd` không phải phép thuật

`ldd` giúp thấy shared-library dependencies, nhưng không nên dùng một cách vô thức với binary không tin cậy trên mọi hệ thống. Một số implementation lịch sử có thể thực thi hoặc tương tác với binary theo cách không phù hợp security analysis.

Với binary đáng tin cậy trên server nội bộ, `ldd` rất hữu ích. Với artifact không tin cậy, nên ưu tiên static inspection như:

```bash
readelf -d ./binary
objdump -p ./binary
```

## Symbol là gì?

Trong quá trình build, source code có tên function/variable như:

```c
printf
malloc
SSL_connect
```

Sau compile/link, những tên cần resolution trở thành **symbol**.

Xem dynamic symbols:

```bash
nm -D /usr/lib/x86_64-linux-gnu/libc.so.6 | head
```

hoặc:

```bash
readelf -Ws /usr/lib/x86_64-linux-gnu/libc.so.6 | less
```

Nếu binary kỳ vọng symbol mà loaded library không cung cấp, có thể gặp:

```text
undefined symbol: XYZ
```

Đây thường là version/ABI mismatch chứ không phải đơn giản “library không tồn tại”.

## ABI quan trọng hơn API ở runtime native

**API** nói cách source code gọi function. **ABI — Application Binary Interface** nói binary-level contract: calling convention, symbol naming, type layout, binary compatibility.

Hai library versions có thể có API gần giống nhưng ABI không tương thích. Khi đó binary build với version A có thể fail khi chạy cùng version B.

Đây là lý do package manager và distro cố quản lý native library versions cẩn thận.

## Static linking và dynamic linking

Static linking đóng code thư viện vào binary lúc build. Dynamic linking giữ dependency tới shared library khi chạy.

Static binary có lợi ở portability trong một số trường hợp, nhưng không có nghĩa “không phụ thuộc hệ thống”. Nó vẫn phụ thuộc kernel ABI, CPU architecture và nhiều assumptions khác.

Dynamic linking tiết kiệm space và cho phép update shared libraries, nhưng làm runtime dependency graph phức tạp hơn.

Không có lựa chọn tốt tuyệt đối cho mọi workload.

## PIE, ASLR và security

**PIE — Position Independent Executable** cho phép binary được load ở nhiều virtual addresses khác nhau. Cùng với **ASLR — Address Space Layout Randomization**, hệ thống làm vị trí memory khó đoán hơn đối với attacker.

Kiểm tra ASLR:

```bash
cat /proc/sys/kernel/randomize_va_space
```

Đây là ví dụ security được xây từ compiler/linker + kernel memory management chứ không chỉ firewall hoặc permission.

## Diagnosing một binary không chạy

Khi binary fail, thay vì thử reinstall ngay, có thể đi theo chuỗi:

```bash
file ./app
```

Xác nhận format/architecture.

```bash
ls -l ./app
```

Xác nhận execute permission.

```bash
readelf -l ./app | grep interpreter
```

Kiểm tra ELF interpreter.

```bash
ldd ./app
```

Tìm library `not found`.

```bash
strace -f ./app
```

Quan sát file open/system call failures.

Nếu service chạy bằng systemd, phải thực hiện diagnosis trong đúng environment/identity của service thay vì chỉ shell hiện tại.

## Case: chạy tay được nhưng systemd fail

Giả sử binary phụ thuộc:

```bash
LD_LIBRARY_PATH=/opt/app/lib
```

Bạn export biến này trong SSH shell rồi chạy thành công:

```bash
./app
```

Nhưng systemd không tự kế thừa environment của shell. Service có thể fail với:

```text
error while loading shared libraries
```

Vấn đề thực sự là runtime dependency resolution khác nhau.

Cách đúng là khai báo dependency/environment rõ trong unit hoặc packaging thay vì dựa vào shell profile.

## Case: copy binary từ server khác

Copy một executable đơn lẻ sang server mới thường thất bại vì:

- architecture khác;
- dynamic linker khác;
- shared library versions khác;
- ABI khác;
- configuration/data paths không tồn tại.

Đây là lý do “binary chạy ở máy A” không chứng minh “binary tự chứa mọi thứ”.

## Connection với Java

Java bytecode không phải ELF application code theo cùng cách, nhưng JVM executable (`java`) bản thân là ELF native binary trên Linux. JVM tiếp tục load native libraries qua JNI/JNA và có thể gặp lỗi `.so` tương tự.

Ví dụ:

```text
java.lang.UnsatisfiedLinkError
```

có thể liên quan native library path hoặc ABI mismatch.

Vì vậy backend Java vẫn không hoàn toàn tách khỏi ELF/native runtime.

## Connection với container

Container image đóng gói user-space libraries, giúp application có runtime dependency tương đối ổn định. Nhưng binary trong container vẫn phải tương thích CPU architecture và host kernel.

Một image `linux/amd64` không tự nhiên chạy native trên ARM host nếu không có emulation phù hợp.

Container giảm một phần dependency drift, không xoá khái niệm ABI.

## Mô hình tư duy (Mental Model)

Khi một chương trình native chạy, hãy hình dung chuỗi:

```text
shell resolution
    ↓
executable path
    ↓
permission
    ↓
ELF / shebang format
    ↓
CPU architecture
    ↓
kernel execve()
    ↓
dynamic linker
    ↓
shared libraries
    ↓
symbol relocation
    ↓
program entry point
```

Một lỗi “không chạy được” phải được đặt vào đúng tầng của chuỗi này.

## Những hiểu lầm phổ biến

**“Có quyền `x` thì chắc chắn chạy được.”** Không. Kernel còn phải hiểu format, architecture và interpreter.

**“`No such file or directory` luôn nghĩa file executable không tồn tại.”** Interpreter hoặc dynamic loader được chỉ định cũng có thể thiếu.

**“Có file `.so` là đủ.”** Version và symbol ABI phải tương thích.

**“Java không liên quan ELF.”** JVM và native libraries vẫn chạy trên native executable/runtime.

**“Container giải quyết mọi dependency.”** Container đóng gói user space nhưng vẫn phụ thuộc CPU architecture và host kernel interface.

## Xem thêm

- [Kernel, user space và system calls](../00_foundations/kernel_userspace_syscalls.md)
- [Process, thread và signal](../04_process/processes_threads_signals_jobs.md)
- [Package, software và shared libraries](./packages_software_libraries.md)
- [Namespace, cgroup và seccomp](../09_production/namespaces_cgroups_seccomp.md)
- [Tracing với strace và perf](../09_production/observability_tracing_strace_perf.md)
