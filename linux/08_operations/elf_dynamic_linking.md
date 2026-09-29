# ELF, động (dynamic / 동적) Linking và cách Linux chạy một chương trình

> **Mạch đọc:** Đọc **ELF, động (dynamic / 동적) Linking và cách Linux chạy một chương trình** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Executable không chỉ là một tệp (file / 파일) có quyền x** sang **ELF chứa những gì?**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Khi gõ một lệnh như:

```bash
curl --version
```

người dùng thường hình dung đơn giản rằng shell “mở tệp (file / 파일) `curl` rồi chạy”. Nhưng để một chương trình bản địa (native / 네이티브) thực sự bắt đầu chạy, Linux phải đi qua nhiều lớp: shell tìm executable trong `PATH`, kernel đọc định dạng tệp (file / 파일), bộ nạp (loader) ánh xạ các đoạn chương trình vào bộ nhớ, bộ liên kết động (dynamic linker) tìm các thư viện dùng chung, xử lý symbol relocation rồi mới chuyển quyền điều khiển tới entry điểm (point / 지점) của chương trình.

Hiểu chuỗi này giúp giải thích các lỗi như:

```text
command not found
No such file or directory
error while loading shared libraries
undefined symbol
Exec format error
```

Những thông báo trên có thể trông giống nhau ở mức “chương trình không chạy”, nhưng nguyên nhân nằm ở các lớp hoàn toàn khác nhau.

## Executable không chỉ là một tệp (file / 파일) có quyền `x`

Quyền thực thi (execute permission) chỉ cho biết tiến trình có được phép yêu cầu kernel thực thi tệp (file / 파일) hay không. Kernel vẫn cần hiểu **định dạng tệp (file / 파일) thực thi (executable format)**.

Trên Linux, định dạng phổ biến cho nhị phân (binary / 이진) bản địa (native / 네이티브) là **ELF — Executable and Linkable Format**.

Kiểm tra:

```bash
file /usr/bin/curl
```

Kết quả có thể chứa các thông tin như:

```text
ELF 64-bit LSB pie executable, x86-64, dynamically linked, ...
```

Mỗi phần đều mang ý nghĩa:

- `ELF 64-bit`: nhị phân (binary / 이진) theo định dạng ELF, kiến trúc 64 bit;
- `x86-64`: kiến trúc CPU mà nhị phân (binary / 이진) được bản dựng (build / 빌드) cho;
- `PIE`: position-independent executable, cho phép tải (load / 로드) ở địa chỉ khác nhau;
- `dynamically linked`: phụ thuộc thư viện động khi chạy.

Nếu bản sao (copy / 복사) một nhị phân (binary / 이진) ARM sang máy chủ (server / 서버) x86-64 rồi chạy, kernel có thể báo `Exec format error`. Vấn đề không nằm ở permission mà nằm ở kiến trúc CPU không tương thích.

## ELF chứa những gì?

ELF không chỉ chứa mã máy (machine code / 기계어). Nó mô tả cách một chương trình hoặc thư viện nên được tổ chức và ánh xạ vào bộ nhớ.

Hai khái niệm thường gặp là **section** và **segment**.

Section chủ yếu phục vụ linker và tooling. Một số section quen thuộc gồm:

- `.text`: mã máy có thể thực thi;
- `.data`: dữ liệu đã khởi tạo;
- `.bss`: dữ liệu zero-initialized;
- `.rodata`: dữ liệu chỉ đọc;
- `.dynsym`: động (dynamic / 동적) symbol bảng (table / 테이블);
- `.rela.*`: relocation thông tin (information / 정보).

Segment gần hơn với cách kernel/loader ánh xạ tệp (file / 파일) vào virtual bộ nhớ (memory / 메모리). Một segment có thể chứa nhiều sections.

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

Mục tiêu không phải ghi nhớ đầu ra (output / 출력), mà hiểu rằng executable là một cấu trúc dữ liệu có siêu dữ liệu (metadata / 메타데이터) đủ để kernel và loader tạo tiến trình (process / 프로세스) ảnh (image / 이미지).

## `execve()` không tạo tiến trình (process / 프로세스) mới

Một hiểu lầm phổ biến là `exec` tạo tiến trình (process / 프로세스). Thực tế, trong mô hình Unix, `execve()` thay thế program ảnh (image / 이미지) của tiến trình (process / 프로세스) hiện tại.

Shell thường tạo child tiến trình (process / 프로세스) rồi child gọi `execve()` để chạy chương trình mới.

```text
shell
  └─ fork/clone
       └─ child process
            └─ execve("/usr/bin/curl", ...)
```

Sau `execve()`, PID có thể giữ nguyên nhưng mã (code / 코드), bộ nhớ (memory / 메모리) mappings và thực thi (execution / 실행) ảnh (image / 이미지) thay đổi mạnh.

Đây là lý do phân biệt **tiến trình (process / 프로세스)** với **program** rất quan trọng.

Xem thêm: [Process, Thread, Signal và Job](../04_process/processes_threads_signals_jobs.md).

## Shebang: script được chạy bằng trình thông dịch (interpreter / 인터프리터) như thế nào?

Một shell script:

```bash
#!/usr/bin/env bash

echo hello
```

không phải ELF nhị phân (binary / 이진). Dòng đầu `#!` gọi là **shebang**.

Khi kernel thấy tệp (file / 파일) script có shebang, nó hiểu rằng tệp (file / 파일) này cần một trình thông dịch (interpreter / 인터프리터). Về mặt khái niệm:

```text
./script.sh
```

trở thành gần giống:

```text
/usr/bin/env bash ./script.sh
```

Nếu trình thông dịch (interpreter / 인터프리터) trong shebang không tồn tại, shell có thể báo lỗi dù script tệp (file / 파일) rõ ràng đang tồn tại.

Đây là một nguyên nhân khiến thông báo `No such file or directory` gây hiểu nhầm: tệp (file / 파일) script có thể tồn tại, nhưng trình thông dịch (interpreter / 인터프리터) mà shebang trỏ tới lại không tồn tại.

## Động (dynamic / 동적) linking giải quyết vấn đề gì?

Nếu mỗi nhị phân (binary / 이진) chứa bản bản sao (copy / 복사) riêng của mọi thư viện cần dùng, dung lượng disk và bộ nhớ (memory / 메모리) sẽ tăng mạnh. Cập nhật một thư viện bảo mật cũng đòi hỏi rebuild toàn bộ chương trình liên quan.

**Liên kết động (dynamic linking)** cho phép nhiều chương trình dùng chung dùng chung (shared / 공유) libraries như:

```text
libc.so
libssl.so
libz.so
```

Nhị phân (binary / 이진) chỉ lưu phụ thuộc (dependency / 의존성) và symbol references cần thiết; khi chạy, động (dynamic / 동적) linker tìm thư viện (library / 라이브러리) thích hợp và nối các symbol.

Kiểm tra thư viện (library / 라이브러리) dependencies:

```bash
ldd /usr/bin/curl
```

Ví dụ:

```text
libcurl.so.4 => /lib/x86_64-linux-gnu/libcurl.so.4
libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6
```

Đây là phụ thuộc (dependency / 의존성) ở **thời gian chạy (runtime / 런타임) bản địa (native / 네이티브) tầng (layer / 계층)**, khác với phụ thuộc (dependency / 의존성) Maven/Gradle ở Java bản dựng (build / 빌드) tầng (layer / 계층).

## Động (dynamic / 동적) linker là chương trình nào?

ELF nhị phân (binary / 이진) động thường chỉ định một trình thông dịch (interpreter / 인터프리터) ELF như:

```bash
readelf -l /usr/bin/curl | grep interpreter
```

Ví dụ có thể thấy:

```text
/lib64/ld-linux-x86-64.so.2
```

Động (dynamic / 동적) linker này chạy rất sớm để tải (load / 로드) libraries và resolve symbols trước khi `main()` được gọi.

Đó là lý do một nhị phân (binary / 이진) có thể tồn tại, có quyền execute, đúng kiến trúc (architecture / 아키텍처) nhưng vẫn không chạy vì động (dynamic / 동적) linker hoặc dùng chung (shared / 공유) thư viện (library / 라이브러리) thiếu.

## Tìm dùng chung (shared / 공유) thư viện (library / 라이브러리) ở đâu?

Động (dynamic / 동적) linker có nhiều nguồn để tìm thư viện, tùy distro và nhị phân (binary / 이진) siêu dữ liệu (metadata / 메타데이터). Các nguồn có thể gồm:

- đường dẫn mặc định như `/lib`, `/usr/lib`;
- bộ nhớ đệm (cache / 캐시) của `ldconfig`;
- `RPATH` hoặc `RUNPATH` trong ELF;
- biến môi trường như `LD_LIBRARY_PATH`.

Xem bộ nhớ đệm (cache / 캐시):

```bash
ldconfig -p | less
```

Xem RPATH/RUNPATH:

```bash
readelf -d ./app | grep -E 'RPATH|RUNPATH'
```

Nếu ứng dụng (application / 애플리케이션) chỉ chạy khi export:

```bash
export LD_LIBRARY_PATH=/opt/app/lib
```

thì cần hiểu đây là thay đổi cơ chế resolution, không phải “fix chung”. Trong môi trường vận hành (production / 운영 환경), phụ thuộc mạnh vào `LD_LIBRARY_PATH` có thể tạo khác biệt giữa interactive shell và systemd dịch vụ (service / 서비스).

## `ldd` không phải phép thuật

`ldd` giúp thấy shared-library dependencies, nhưng không nên dùng một cách vô thức với nhị phân (binary / 이진) không tin cậy trên mọi hệ thống. Một số hiện thực (implementation / 구현) lịch sử có thể thực thi hoặc tương tác với nhị phân (binary / 이진) theo cách không phù hợp bảo mật (security / 보안) phân tích (analysis / 분석).

Với nhị phân (binary / 이진) đáng tin cậy trên máy chủ (server / 서버) nội bộ, `ldd` rất hữu ích. Với sản phẩm tạo ra (artifact / 산출물) không tin cậy, nên ưu tiên static inspection như:

```bash
readelf -d ./binary
objdump -p ./binary
```

## Symbol là gì?

Trong quá trình bản dựng (build / 빌드), mã nguồn (source code / 소스 코드) có tên hàm (function / 함수)/variable như:

```c
printf
malloc
SSL_connect
```

Sau compile/link, những tên cần resolution trở thành **symbol**.

Xem động (dynamic / 동적) symbols:

```bash
nm -D /usr/lib/x86_64-linux-gnu/libc.so.6 | head
```

hoặc:

```bash
readelf -Ws /usr/lib/x86_64-linux-gnu/libc.so.6 | less
```

Nếu nhị phân (binary / 이진) kỳ vọng symbol mà loaded thư viện (library / 라이브러리) không cung cấp, có thể gặp:

```text
undefined symbol: XYZ
```

Đây thường là phiên bản (version / 버전)/ABI mismatch chứ không phải đơn giản “thư viện (library / 라이브러리) không tồn tại”.

## ABI quan trọng hơn API ở thời gian chạy (runtime / 런타임) bản địa (native / 네이티브)

**API** nói cách mã nguồn (source code / 소스 코드) gọi hàm (function / 함수). **ABI — ứng dụng (application / 애플리케이션) nhị phân (binary / 이진) giao diện (interface / 인터페이스)** nói binary-level đặc tả hợp đồng (contract / 계약): calling convention, symbol naming, kiểu (type / 타입) bố cục (layout / 레이아웃), nhị phân (binary / 이진) tính tương thích (compatibility / 호환성).

Hai thư viện (library / 라이브러리) versions có thể có API gần giống nhưng ABI không tương thích. Khi đó nhị phân (binary / 이진) bản dựng (build / 빌드) với phiên bản (version / 버전) A có thể thất bại (fail / 실패) khi chạy cùng phiên bản (version / 버전) B.

Đây là lý do trình quản lý gói (package manager / 패키지 관리자) và distro cố quản lý bản địa (native / 네이티브) thư viện (library / 라이브러리) versions cẩn thận.

## Static linking và động (dynamic / 동적) linking

Static linking đóng mã (code / 코드) thư viện vào nhị phân (binary / 이진) lúc bản dựng (build / 빌드). động (dynamic / 동적) linking giữ phụ thuộc (dependency / 의존성) tới dùng chung (shared / 공유) thư viện (library / 라이브러리) khi chạy.

Static nhị phân (binary / 이진) có lợi ở portability trong một số trường hợp, nhưng không có nghĩa “không phụ thuộc hệ thống”. Nó vẫn phụ thuộc kernel ABI, CPU kiến trúc (architecture / 아키텍처) và nhiều các giả định (assumptions / 가정들) khác.

Động (dynamic / 동적) linking tiết kiệm không gian (space / 공간) và cho phép cập nhật (update / 업데이트) dùng chung (shared / 공유) libraries, nhưng làm thời gian chạy (runtime / 런타임) phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) phức tạp hơn.

Không có lựa chọn tốt tuyệt đối cho mọi tải công việc (workload / 워크로드).

## PIE, ASLR và bảo mật (security / 보안)

**PIE — Position Independent Executable** cho phép nhị phân (binary / 이진) được tải (load / 로드) ở nhiều virtual addresses khác nhau. Cùng với **ASLR — Address không gian (space / 공간) bố cục (layout / 레이아웃) Randomization**, hệ thống làm vị trí bộ nhớ (memory / 메모리) khó đoán hơn đối với attacker.

Kiểm tra ASLR:

```bash
cat /proc/sys/kernel/randomize_va_space
```

Đây là ví dụ bảo mật (security / 보안) được xây từ trình biên dịch (compiler / 컴파일러)/linker + kernel bộ nhớ (memory / 메모리) management chứ không chỉ firewall hoặc permission.

## Diagnosing một nhị phân (binary / 이진) không chạy

Khi nhị phân (binary / 이진) thất bại (fail / 실패), thay vì thử reinstall ngay, có thể đi theo chuỗi:

```bash
file ./app
```

Xác nhận format/kiến trúc (architecture / 아키텍처).

```bash
ls -l ./app
```

Xác nhận execute permission.

```bash
readelf -l ./app | grep interpreter
```

Kiểm tra ELF trình thông dịch (interpreter / 인터프리터).

```bash
ldd ./app
```

Tìm thư viện (library / 라이브러리) `not found`.

```bash
strace -f ./app
```

Quan sát tệp (file / 파일) open/lời gọi hệ thống (system call / 시스템 호출) failures.

Nếu dịch vụ (service / 서비스) chạy bằng systemd, phải thực hiện diagnosis trong đúng môi trường (environment / 환경)/định danh (identity / 식별자) của dịch vụ (service / 서비스) thay vì chỉ shell hiện tại.

## Trường hợp (case / 사례): chạy tay được nhưng systemd thất bại (fail / 실패)

Giả sử nhị phân (binary / 이진) phụ thuộc:

```bash
LD_LIBRARY_PATH=/opt/app/lib
```

Bạn export biến này trong SSH shell rồi chạy thành công:

```bash
./app
```

Nhưng systemd không tự kế thừa môi trường (environment / 환경) của shell. dịch vụ (service / 서비스) có thể thất bại (fail / 실패) với:

```text
error while loading shared libraries
```

Vấn đề thực sự là thời gian chạy (runtime / 런타임) phụ thuộc (dependency / 의존성) resolution khác nhau.

Cách đúng là khai báo phụ thuộc (dependency / 의존성)/môi trường (environment / 환경) rõ trong đơn vị (unit / 단위) hoặc packaging thay vì dựa vào shell profile.

## Trường hợp (case / 사례): bản sao (copy / 복사) nhị phân (binary / 이진) từ máy chủ (server / 서버) khác

Bản sao (copy / 복사) một executable đơn lẻ sang máy chủ (server / 서버) mới thường thất bại vì:

- kiến trúc (architecture / 아키텍처) khác;
- động (dynamic / 동적) linker khác;
- dùng chung (shared / 공유) thư viện (library / 라이브러리) versions khác;
- ABI khác;
- cấu hình (configuration / 구성)/dữ liệu (data / 데이터) paths không tồn tại.

Đây là lý do “nhị phân (binary / 이진) chạy ở máy A” không chứng minh “nhị phân (binary / 이진) tự chứa mọi thứ”.

## Liên kết (connection / 연결) với Java

Java bytecode không phải ELF ứng dụng (application / 애플리케이션) mã (code / 코드) theo cùng cách, nhưng JVM executable (`java`) bản thân là ELF bản địa (native / 네이티브) nhị phân (binary / 이진) trên Linux. JVM tiếp tục tải (load / 로드) bản địa (native / 네이티브) libraries qua JNI/JNA và có thể gặp lỗi `.so` tương tự.

Ví dụ:

```text
java.lang.UnsatisfiedLinkError
```

có thể liên quan bản địa (native / 네이티브) thư viện (library / 라이브러리) đường dẫn (path / 경로) hoặc ABI mismatch.

Vì vậy backend Java vẫn không hoàn toàn tách khỏi ELF/bản địa (native / 네이티브) thời gian chạy (runtime / 런타임).

## Liên kết (connection / 연결) với bộ chứa (container / 컨테이너)

Ảnh bộ chứa (container image / 컨테이너 이미지) đóng gói user-space libraries, giúp ứng dụng (application / 애플리케이션) có thời gian chạy (runtime / 런타임) phụ thuộc (dependency / 의존성) tương đối ổn định. Nhưng nhị phân (binary / 이진) trong bộ chứa (container / 컨테이너) vẫn phải tương thích CPU kiến trúc (architecture / 아키텍처) và host kernel.

Một ảnh (image / 이미지) `linux/amd64` không tự nhiên chạy bản địa (native / 네이티브) trên ARM host nếu không có emulation phù hợp.

Bộ chứa (container / 컨테이너) giảm một phần phụ thuộc (dependency / 의존성) drift, không xoá khái niệm ABI.

## Mô hình tư duy (mental model / 사고 모델)

Khi một chương trình bản địa (native / 네이티브) chạy, hãy hình dung chuỗi:

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

**“Có quyền `x` thì chắc chắn chạy được.”** Không. Kernel còn phải hiểu format, kiến trúc (architecture / 아키텍처) và trình thông dịch (interpreter / 인터프리터).

**“`No such file or directory` luôn nghĩa tệp (file / 파일) executable không tồn tại.”** trình thông dịch (interpreter / 인터프리터) hoặc động (dynamic / 동적) loader được chỉ định cũng có thể thiếu.

**“Có tệp (file / 파일) `.so` là đủ.”** phiên bản (version / 버전) và symbol ABI phải tương thích.

**“Java không liên quan ELF.”** JVM và bản địa (native / 네이티브) libraries vẫn chạy trên bản địa (native / 네이티브) executable/thời gian chạy (runtime / 런타임).

**“bộ chứa (container / 컨테이너) giải quyết mọi phụ thuộc (dependency / 의존성).”** bộ chứa (container / 컨테이너) đóng gói người dùng (user / 사용자) không gian (space / 공간) nhưng vẫn phụ thuộc CPU kiến trúc (architecture / 아키텍처) và host kernel giao diện (interface / 인터페이스).

## Xem thêm

Các liên kết này là bước bàn giao sang cơ chế liên quan. Hãy mở chúng theo câu hỏi còn bỏ ngỏ, không coi danh sách link là phần kết luận tự thân.

- [Kernel, user space và system calls](../00_foundations/kernel_userspace_syscalls.md)
- [Process, thread và signal](../04_process/processes_threads_signals_jobs.md)
- [Package, software và shared libraries](./packages_software_libraries.md)
- [Namespace, cgroup và seccomp](../09_production/namespaces_cgroups_seccomp.md)
- [Tracing với strace và perf](../09_production/observability_tracing_strace_perf.md)

> **Bàn giao:** Sau **Xem thêm**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [backup restore disaster recovery](./backup_restore_disaster_recovery.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
