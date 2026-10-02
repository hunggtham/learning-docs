# Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Tiến trình (process / 프로세스) không phải chỉ là PID** cho thấy đối tượng vận hành qua những bước nào và tạo ra hệ quả gì; sau đó sang **Tiến trình (process / 프로세스) và luồng thực thi (thread / 스레드) trong Linux** để giải thích cách điều kiện hoặc mục tiêu đó vận hành. Mạch này nối address space với fork, exec và wait, để theo dõi tiến trình từ lúc tạo bản sao đến khi thu hồi trạng thái con.

Chương [Tiến trình, luồng, tín hiệu và tác vụ](./processes_threads_signals_jobs.md) cung cấp mô hình tổng quan về tiến trình (process / 프로세스). Chương này đi sâu hơn vào cách Linux thực sự biểu diễn một tiến trình (process / 프로세스)/luồng thực thi (thread / 스레드), address không gian (space / 공간) của nó gồm những vùng nào, `fork()` tạo tiến trình (process / 프로세스) con ra sao, `execve()` thay chương trình thế nào, vì sao zombie tồn tại và cách `wait()` hoàn tất vòng đời tiến trình (process / 프로세스).

Đây là nền tảng để hiểu shell, systemd, bộ chứa (container / 컨테이너), JVM, tín hiệu (signal / 신호), bộ nhớ (memory / 메모리) leak, tệp (file / 파일) descriptor inheritance và nhiều hiện tượng môi trường vận hành (production / 운영 환경) khác.

## Tiến trình (process / 프로세스) không phải chỉ là PID

PID là một mã định danh trong một PID không gian tên (namespace / 네임스페이스). Bên trong kernel, thực thi (execution / 실행) ngữ cảnh (context / 맥락) cần nhiều trạng thái hơn rất nhiều:

- scheduling trạng thái (state / 상태);
- CPU register trạng thái (state / 상태) khi bị deschedule;
- bộ nhớ (memory / 메모리) mappings;
- credentials;
- tệp (file / 파일) descriptor bảng (table / 테이블);
- tín hiệu (signal / 신호) trạng thái (state / 상태);
- không gian tên (namespace / 네임스페이스) membership;
- cgroup membership;
- parent/child relationship;
- accounting thông tin (information / 정보).

Trong Linux nguồn (source / 소스), một khái niệm trung tâm là `task_struct`, đại diện cho tác vụ (task / 작업) mà scheduler có thể quản lý. Người học không cần thuộc trường dữ liệu (field / 필드) của cấu trúc này, nhưng mô hình tư duy (mental model / 사고 모델) quan trọng là:

> Một tác vụ (task / 작업) là một đối tượng (object / 객체) kernel nối nhiều subsystem lại với nhau.

> **Chuyển mạch:** Trong **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **Tiến trình (process / 프로세스) không phải chỉ là PID** xác định đầu vào; **Tiến trình (process / 프로세스) và luồng thực thi (thread / 스레드) trong Linux** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **PID, TID và luồng thực thi (thread / 스레드) group** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tiến trình (process / 프로세스) và luồng thực thi (thread / 스레드) trong Linux

Linux có cách nhìn thống nhất hơn nhiều hệ điều hành giáo khoa: luồng thực thi (thread / 스레드) cũng là một tác vụ (task / 작업) có thể được scheduler chạy. Nhiều luồng thực thi (thread / 스레드) trong cùng tiến trình (process / 프로세스) chia sẻ một số tài nguyên (resource / 자원), đặc biệt address không gian (space / 공간) và tệp (file / 파일) descriptor bảng (table / 테이블), tùy cách được tạo bằng `clone()`/`clone3()`.

Vì vậy ranh giới tiến trình (process / 프로세스)/luồng thực thi (thread / 스레드) có thể hiểu bằng câu hỏi:

```text
những tài nguyên nào được chia sẻ?
```

Hai tác vụ (task / 작업) có thể:

- chia sẻ bộ nhớ (memory / 메모리) nhưng có ngăn xếp (stack / 스택)/register riêng;
- chia sẻ tệp (file / 파일) descriptor bảng (table / 테이블);
- chia sẻ tín hiệu (signal / 신호) handlers;
- cùng thuộc một luồng thực thi (thread / 스레드) group.

Một JVM tiến trình (process / 프로세스) với 200 Java luồng thực thi (thread / 스레드) tương ứng nhiều scheduling entities ở Linux, không phải một đối tượng CPU duy nhất.

> **Chuyển mạch:** Ở chặng này của **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **Tiến trình (process / 프로세스) và luồng thực thi (thread / 스레드) trong Linux** xác định đầu vào; **PID, TID và luồng thực thi (thread / 스레드) group** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Address không gian (space / 공간) của tiến trình (process / 프로세스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## PID, TID và luồng thực thi (thread / 스레드) group

Trong thực tế Linux, mỗi luồng thực thi (thread / 스레드) có một tác vụ (task / 작업) ID riêng. Main luồng thực thi (thread / 스레드) thường có ID trùng tiến trình (process / 프로세스) ID theo cách user-space nhìn thấy. Các luồng thực thi (thread / 스레드) cùng tiến trình (process / 프로세스) thuộc một **luồng thực thi (thread / 스레드) group**.

Quan sát:

```bash
ps -L -p <PID> -o pid,tid,psr,stat,comm
```

hoặc:

```bash
ls /proc/<PID>/task
```

Mỗi entry dưới `/proc/<PID>/task/` đại diện một luồng thực thi (thread / 스레드)/tác vụ (task / 작업).

Điều này rất hữu ích khi ánh xạ (mapping / 매핑) Java luồng thực thi (thread / 스레드) dump với Linux luồng thực thi (thread / 스레드) CPU usage.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **PID, TID và luồng thực thi (thread / 스레드) group** xác định đầu vào; **Address không gian (space / 공간) của tiến trình (process / 프로세스)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Mã (code / 코드), dữ liệu (data / 데이터), vùng nhớ động (heap / 힙) và ngăn xếp (stack / 스택)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Address không gian (space / 공간) của tiến trình (process / 프로세스)

Một tiến trình (process / 프로세스) nhìn thấy một không gian địa chỉ ảo riêng.

Có thể quan sát ánh xạ (mapping / 매핑):

```bash
cat /proc/<PID>/maps
pmap -x <PID>
```

Một tiến trình (process / 프로세스) điển hình có các vùng:

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

Không nên coi address không gian (space / 공간) là một mảng RAM vật lý liên tục. Đây là một tập các **VMA (Virtual memory Area)** có permission và backing khác nhau.

Xem sâu hơn tại [Virtual memory, page fault và reclaim](../06_resources/virtual_memory_page_fault_reclaim_allocator.md).

> **Chuyển mạch:** Trong **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, cơ chế trong **Address không gian (space / 공간) của tiến trình (process / 프로세스)** cần được kiểm chứng bằng dấu vết cụ thể; **Mã (code / 코드), dữ liệu (data / 데이터), vùng nhớ động (heap / 힙) và ngăn xếp (stack / 스택)** đưa dữ liệu và nguồn vào đúng điểm đó. Từ đây, **/proc/<PID>/maps giải thích gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mã (code / 코드), dữ liệu (data / 데이터), vùng nhớ động (heap / 힙) và ngăn xếp (stack / 스택)

Mô hình giáo khoa thường chia tiến trình (process / 프로세스) thành mã (code / 코드)/dữ liệu (data / 데이터)/vùng nhớ động (heap / 힙)/ngăn xếp (stack / 스택). Đây vẫn hữu ích nhưng thực tế Linux phức tạp hơn do `mmap()`.

Vùng nhớ vùng nhớ động (heap / 힙) truyền thống có thể tăng qua `brk()`, nhưng allocator hiện đại có thể dùng cả `mmap()` cho allocation lớn.

Luồng thực thi (thread / 스레드) ngăn xếp (stack / 스택) cũng là ánh xạ (mapping / 매핑) trong address không gian (space / 공간).

Dùng chung (shared / 공유) libraries được map vào address không gian (space / 공간) thông qua động (dynamic / 동적) linker.

Do đó nhìn RSS hoặc VSZ mà không hiểu ánh xạ (mapping / 매핑) dễ dẫn tới kết luận sai.

> **Chuyển mạch:** Ở chặng này của **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **Mã (code / 코드), dữ liệu (data / 데이터), vùng nhớ động (heap / 힙) và ngăn xếp (stack / 스택)** nêu điều cần giải thích; **/proc/<PID>/maps giải thích gì?** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **ASLR** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `/proc/<PID>/maps` giải thích gì?

Ví dụ một dòng ánh xạ (mapping / 매핑):

```text
7f1234000000-7f1234200000 r-xp ... /usr/lib/libc.so.6
```

Các trường cho biết phạm vi (range / 범위) địa chỉ, permission và backing tệp (file / 파일).

Permission thường có:

- `r`: read;
- `w`: ghi (write / 쓰기);
- `x`: execute;
- `p`: private ánh xạ (mapping / 매핑);
- `s`: dùng chung (shared / 공유) ánh xạ (mapping / 매핑).

Ánh xạ (mapping / 매핑) `r-x` thường chứa mã (code / 코드) thực thi. ánh xạ (mapping / 매핑) `rw-` chứa dữ liệu có thể ghi.

Đây là nền tảng để hiểu W^X, ASLR và exploit mitigation.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **ASLR** tiếp nhận điểm tựa từ **/proc/<PID>/maps giải thích gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tạo tiến trình (process / 프로세스): fork() không bản sao (copy / 복사) toàn bộ RAM ngay** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## ASLR

**Address không gian (space / 공간) bố cục (layout / 레이아웃) Randomization (ASLR)** làm vị trí nhiều ánh xạ (mapping / 매핑) thay đổi giữa các lần chạy để giảm khả năng exploit dự đoán địa chỉ.

```bash
cat /proc/sys/kernel/randomize_va_space
```

ASLR không sửa bug bộ nhớ (memory / 메모리) an toàn (safety / 안전), nhưng làm một số exploit khó hơn.

PIE nhị phân (binary / 이진) và dùng chung (shared / 공유) thư viện (library / 라이브러리) có thể phối hợp với ASLR.

Xem thêm [ELF và dynamic linking](../08_operations/elf_dynamic_linking.md).

> **Chuyển mạch:** Trong **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **ASLR** xác định đầu vào; **Tạo tiến trình (process / 프로세스): fork() không bản sao (copy / 복사) toàn bộ RAM ngay** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **COW không có nghĩa fork luôn rẻ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tạo tiến trình (process / 프로세스): `fork()` không bản sao (copy / 복사) toàn bộ RAM ngay

Mô hình Unix cổ điển:

```text
parent
  ↓ fork()
parent + child
```

Một hiểu lầm thường gặp là kernel bản sao (copy / 복사) toàn bộ bộ nhớ (memory / 메모리) của parent ngay lập tức. Linux dùng **sao chép khi ghi (copy-on-write / 쓰기 시 복사) (COW)**.

Sau `fork()`, parent và child có thể tạm thời chia sẻ cùng vật lý (physical / 물리적) pages dưới permission phù hợp. Khi một bên ghi vào page, page fault xảy ra và kernel tạo bản sao riêng cho bên ghi.

Mô hình tư duy (mental model / 사고 모델):

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

Nhờ đó `fork()` thường rẻ hơn rất nhiều so với bản sao (copy / 복사) toàn bộ bộ nhớ (memory / 메모리) ngay lập tức.

> **Chuyển mạch:** Ở chặng này của **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **Tạo tiến trình (process / 프로세스): fork() không bản sao (copy / 복사) toàn bộ RAM ngay** xác định đầu vào; **COW không có nghĩa fork luôn rẻ** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **fork() và multi-threaded tiến trình (process / 프로세스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## COW không có nghĩa fork luôn rẻ

Dù dữ liệu (data / 데이터) pages chưa bản sao (copy / 복사), kernel vẫn phải tạo hoặc quản lý siêu dữ liệu (metadata / 메타데이터) như page tables và tác vụ (task / 작업) trạng thái (state / 상태). tiến trình (process / 프로세스) rất lớn có thể khiến fork có chi phí đáng kể.

Nếu child sau đó ghi nhiều bộ nhớ (memory / 메모리), COW faults và bản sao (copy / 복사) pages tạo thêm chi phí.

Đây là lý do thời gian chạy (runtime / 런타임)/cơ sở dữ liệu (database / 데이터베이스) lớn có thể quan tâm sâu tới hành vi (behavior / 동작) của fork.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **COW không có nghĩa fork luôn rẻ** xác định đầu vào; **fork() và multi-threaded tiến trình (process / 프로세스)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **clone() và Linux luồng thực thi (thread / 스레드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `fork()` và multi-threaded tiến trình (process / 프로세스)

Trong tiến trình (process / 프로세스) nhiều luồng thực thi (thread / 스레드), `fork()` tạo child chỉ với luồng thực thi (thread / 스레드) gọi fork theo POSIX ngữ nghĩa (semantics / 의미론) điển hình. Các khóa (lock / 잠금) trong tiến trình (process / 프로세스) có thể đang ở trạng thái phức tạp vì luồng thực thi (thread / 스레드) khác biến mất trong child.

Vì vậy child của multi-threaded tiến trình (process / 프로세스) thường cần nhanh chóng `exec()` thay vì tiếp tục chạy lô-gic (logic / 논리) tùy ý.

Đây là một trong những lý do spawn tiến trình (process / 프로세스) trong thời gian chạy (runtime / 런타임) phức tạp cần hiện thực (implementation / 구현) cẩn thận.

> **Chuyển mạch:** Trong **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **fork() và multi-threaded tiến trình (process / 프로세스)** xác định đầu vào; **clone() và Linux luồng thực thi (thread / 스레드)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **execve() không tạo PID mới** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `clone()` và Linux luồng thực thi (thread / 스레드)

Linux sử dụng `clone()`/`clone3()` cho phép caller chọn tài nguyên (resource / 자원) nào được chia sẻ.

Các flag có thể quyết định việc chia sẻ:

- virtual bộ nhớ (memory / 메모리);
- filesystem trạng thái (state / 상태);
- tệp (file / 파일) descriptor bảng (table / 테이블);
- tín hiệu (signal / 신호) handlers;
- không gian tên (namespace / 네임스페이스).

Luồng thực thi (thread / 스레드) có thể được xem như các tác vụ (task / 작업) tạo bằng clone với tập chia sẻ phù hợp.

Bộ chứa (container / 컨테이너) thời gian chạy (runtime / 런타임) cũng tận dụng clone/unshare/setns để xây không gian tên (namespace / 네임스페이스) isolation.

> **Chuyển mạch:** Ở chặng này của **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **execve() không tạo PID mới** tiếp nhận điểm tựa từ **clone() và Linux luồng thực thi (thread / 스레드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Shell chạy command ngoài thế nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `execve()` không tạo PID mới

Đây là một điểm nền tảng rất quan trọng.

`execve()` **thay program ảnh (image / 이미지) của tiến trình (process / 프로세스) hiện tại**. PID không nhất thiết đổi.

Mô hình tư duy (mental model / 사고 모델):

```text
process PID 123
đang chạy shell
    ↓ execve(java,...)
process PID 123
bây giờ chạy Java image
```

Address không gian (space / 공간) cũ được thay bằng mappings của executable/thư viện (library / 라이브러리) mới; ngăn xếp (stack / 스택) mới được dựng với arguments/môi trường (environment / 환경).

Vì vậy `exec` không có nghĩa “tạo tiến trình (process / 프로세스) con”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **Shell chạy command ngoài thế nào?** tiếp nhận điểm tựa từ **execve() không tạo PID mới** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tệp (file / 파일) descriptor inheritance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Chuỗi xử lý (pipeline / 파이프라인):

```bash
cat file | grep ERROR | sort
```

đòi hỏi shell tạo pipe, tạo nhiều tiến trình (process / 프로세스), nối tệp (file / 파일) descriptor đúng đầu rồi `exec()` từng command.

Do đó shell cú pháp (syntax / 문법) cuối cùng dựa trên tiến trình (process / 프로세스) vòng đời (lifecycle / 생명주기) + tệp (file / 파일) descriptor inheritance.

> **Chuyển mạch:** Trong **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **Tệp (file / 파일) descriptor inheritance** tiếp nhận điểm tựa từ **Shell chạy command ngoài thế nào?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **FDCLOEXEC** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tệp (file / 파일) descriptor inheritance

Sau `fork()`, child thường kế thừa tệp (file / 파일) descriptor bảng (table / 테이블) ngữ nghĩa (semantics / 의미론) từ parent.

Điều này cho phép shell chuẩn bị redirection trước `exec()`:

```text
open output file
fork
child dup2(output_fd, STDOUT)
exec program
```

Program mới không cần biết shell đã setup redirection ra sao. Nó chỉ thấy fd 1 là stdout bình thường.

Đây là sức mạnh của Unix composition.

> **Chuyển mạch:** Ở chặng này của **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **FDCLOEXEC** tiếp nhận điểm tựa từ **Tệp (file / 파일) descriptor inheritance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Môi trường (environment / 환경) được đưa vào exec** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `FD_CLOEXEC`

Không phải tệp (file / 파일) descriptor nào cũng nên sống qua `exec()`.

Flag **close-on-exec** yêu cầu kernel đóng descriptor khi exec thành công.

Nếu ứng dụng quên đặt close-on-exec đúng chỗ, child tiến trình (process / 프로세스) có thể vô tình giữ socket/tệp (file / 파일) descriptor mà nó không cần.

Hậu quả có thể gồm:

- tệp (file / 파일) không được giải phóng;
- pipe không nhận EOF;
- socket vẫn bị giữ;
- ranh giới bảo mật (security boundary / 보안 경계) bị rò tài nguyên (resource / 자원).

Vì vậy descriptor thời gian tồn tại (lifetime / 수명) là một phần của tiến trình (process / 프로세스) vòng đời (lifecycle / 생명주기).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **Môi trường (environment / 환경) được đưa vào exec** tiếp nhận điểm tựa từ **FDCLOEXEC** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hiện tại (current / 현재) working directory** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Môi trường (environment / 환경) được đưa vào exec

`execve()` nhận argument véc-tơ (vector / 벡터) và môi trường (environment / 환경) véc-tơ (vector / 벡터).

Môi trường (environment / 환경) không phải cơ sở dữ liệu (database / 데이터베이스) toàn cục. Nó là dữ liệu được truyền vào tiến trình (process / 프로세스) ảnh (image / 이미지).

Khi shell:

```bash
export APP_ENV=prod
java -jar app.jar
```

child/exec ảnh (image / 이미지) nhận môi trường (environment / 환경) tương ứng.

Tiến trình (process / 프로세스) đã chạy không tự thấy các thay đổi môi trường (environment / 환경) của parent sau đó.

> **Chuyển mạch:** Trong **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **Hiện tại (current / 현재) working directory** tiếp nhận điểm tựa từ **Môi trường (environment / 환경) được đưa vào exec** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Gốc (root / 루트) directory của tiến trình (process / 프로세스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hiện tại (current / 현재) working directory

Tiến trình (process / 프로세스) giữ hiện tại (current / 현재) working directory như một tham chiếu (reference / 참조) tới filesystem đối tượng (object / 객체).

Do đó tệp (file / 파일) relative đường dẫn (path / 경로) được resolve dựa trên cwd của tiến trình (process / 프로세스).

```bash
readlink /proc/<PID>/cwd
```

Một tiến trình (process / 프로세스) có thể giữ cwd trong filesystem đang cố unmount, khiến `umount` báo busy.

Đây là ví dụ tiến trình (process / 프로세스) trạng thái (state / 상태) nối trực tiếp với VFS thời gian tồn tại (lifetime / 수명).

> **Chuyển mạch:** Ở chặng này của **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **Hiện tại (current / 현재) working directory** xác định đầu vào; **Gốc (root / 루트) directory của tiến trình (process / 프로세스)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Credentials qua fork/exec** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Gốc (root / 루트) directory của tiến trình (process / 프로세스)

Tiến trình (process / 프로세스) có khái niệm gốc (root / 루트) directory dùng khi resolve absolute đường dẫn (path / 경로). `chroot()` có thể thay góc nhìn này, nhưng không phải isolation mạnh tương đương bộ chứa (container / 컨테이너).

Mount không gian tên (namespace / 네임스페이스) và pivot_root giúp bộ chứa (container / 컨테이너) thời gian chạy (runtime / 런타임) xây filesystem view riêng sâu hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **Gốc (root / 루트) directory của tiến trình (process / 프로세스)** xác định đầu vào; **Credentials qua fork/exec** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Tín hiệu (signal / 신호) disposition qua exec** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Credentials qua fork/exec

Child thường kế thừa credentials từ parent, nhưng exec có thể tương tác với setuid/setgid, capabilities và bảo mật (security / 보안) chính sách (policy / 정책).

Kernel phải tính effective credentials cẩn thận khi executable có siêu dữ liệu (metadata / 메타데이터) đặc quyền.

Xem [Credentials, capabilities, ACL và MAC](../03_identity/credentials_capabilities_acl_mac.md).

> **Chuyển mạch:** Trong **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **Tín hiệu (signal / 신호) disposition qua exec** tiếp nhận điểm tựa từ **Credentials qua fork/exec** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Parent-child relationship** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tín hiệu (signal / 신호) disposition qua exec

Một số tín hiệu (signal / 신호) disposition thay đổi qua exec theo POSIX ngữ nghĩa (semantics / 의미론). Pending trạng thái (state / 상태) và mask có quy tắc riêng.

Điểm cần nhớ: exec thay program ảnh (image / 이미지) nhưng tiến trình (process / 프로세스) đối tượng (object / 객체) không phải “reset mọi thứ về 0”. Một số thuộc tính được giữ, một số được thay.

Đây là lý do ngữ nghĩa (semantics / 의미론) của exec là một hợp đồng rất cụ thể.

> **Chuyển mạch:** Ở chặng này của **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **Parent-child relationship** tiếp nhận điểm tựa từ **Tín hiệu (signal / 신호) disposition qua exec** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Zombie chính xác là gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Parent-child relationship

Tiến trình (process / 프로세스) con có parent. Parent có thể cần biết child kết thúc ra sao.

Khi child exit, kernel giữ một phần exit status để parent thu nhận bằng `wait()`/`waitpid()`.

Khoảng thời gian child đã chết nhưng status chưa được parent thu nhận tạo ra **zombie**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **Zombie chính xác là gì?** tiếp nhận điểm tựa từ **Parent-child relationship** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **wait() làm gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Zombie chính xác là gì?

Zombie không còn chạy mã (code / 코드) và hầu hết tài nguyên (resource / 자원) đã được giải phóng. Kernel vẫn giữ entry tối thiểu gồm PID và exit status để parent có thể wait.

Quan sát:

```bash
ps -eo pid,ppid,stat,cmd | awk '$3 ~ /Z/'
```

Zombie ít thường không tiêu thụ nhiều tài nguyên, nhưng tích tụ lớn có thể làm cạn PID/tác vụ (task / 작업) bảng (table / 테이블) và là dấu hiệu parent không reap child đúng.

> **Chuyển mạch:** Trong **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **wait() làm gì?** tiếp nhận điểm tựa từ **Zombie chính xác là gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Orphan khác zombie** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `wait()` làm gì?

Parent gọi `wait()` hoặc `waitpid()` để:

- lấy exit status;
- xác nhận child kết thúc;
- cho kernel giải phóng zombie entry.

Mô hình tư duy (mental model / 사고 모델):

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

> **Chuyển mạch:** Ở chặng này của **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **Orphan khác zombie** tiếp nhận điểm tựa từ **wait() làm gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **PID 1 và subreaper** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Orphan khác zombie

**Orphan** là child còn sống nhưng parent đã chết.

**Zombie** là child đã chết nhưng parent chưa reap.

Hai khái niệm hoàn toàn khác nhau.

Khi parent biến mất, orphan được reparent theo ngữ nghĩa (semantics / 의미론) không gian tên (namespace / 네임스페이스)/init/subreaper.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **PID 1 và subreaper** tiếp nhận điểm tựa từ **Orphan khác zombie** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Exit status** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## PID 1 và subreaper

PID 1 có vai trò đặc biệt trong tiến trình (process / 프로세스) cây (tree / 트리). Trong bộ chứa (container / 컨테이너), tiến trình (process / 프로세스) làm PID 1 cần xử lý tín hiệu (signal / 신호)/reaping đúng.

Systemd và các init hệ thống (system / 시스템) quản lý child vòng đời (lifecycle / 생명주기) rất chặt.

Linux còn có khái niệm **child subreaper**, cho phép tiến trình (process / 프로세스) nhận orphan descendant trong một số mô hình supervision.

Đây là cơ sở cho tiến trình (process / 프로세스) supervisor/bộ chứa (container / 컨테이너) init.

> **Chuyển mạch:** Trong **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **Exit status** tiếp nhận điểm tựa từ **PID 1 và subreaper** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tiến trình (process / 프로세스) group và session** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Exit status

Tiến trình (process / 프로세스) kết thúc với exit mã (code / 코드) hoặc do tín hiệu (signal / 신호).

Shell dùng `$?` để xem status của command trước:

```bash
some-command
echo $?
```

Convention thường dùng 0 là thành công và khác 0 là lỗi, nhưng nghĩa cụ thể phụ thuộc chương trình.

Nếu tiến trình (process / 프로세스) chết do tín hiệu (signal / 신호), shell/thời gian chạy (runtime / 런타임) có thể mã hóa status theo convention riêng để báo lại.

> **Chuyển mạch:** Ở chặng này của **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **Exit status** xác định đầu vào; **Tiến trình (process / 프로세스) group và session** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Controlling terminal** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tiến trình (process / 프로세스) group và session

Job điều khiển (control / 제어) cần thêm lớp trừu tượng (abstraction / 추상화) ngoài PID.

**tiến trình (process / 프로세스) group** gom nhiều tiến trình (process / 프로세스), ví dụ chuỗi xử lý (pipeline / 파이프라인).

**Session** gom tiến trình (process / 프로세스) group và liên hệ controlling terminal.

Khi nhấn `Ctrl+C`, terminal driver thường gửi `SIGINT` tới foreground tiến trình (process / 프로세스) group, không phải chỉ một PID ngẫu nhiên.

Đây là lý do chuỗi xử lý (pipeline / 파이프라인) foreground có thể bị dừng cùng nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **Tiến trình (process / 프로세스) group và session** xác định đầu vào; **Controlling terminal** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Daemonization cổ điển** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Controlling terminal

Interactive shell có controlling terminal. Foreground tiến trình (process / 프로세스) group có quyền đọc đầu vào (input / 입력) terminal.

Background tiến trình (process / 프로세스) cố đọc terminal có thể bị tín hiệu (signal / 신호) như `SIGTTIN`.

Job điều khiển (control / 제어) vì vậy là collaboration giữa shell, tiến trình (process / 프로세스) groups, session và terminal driver trong kernel.

> **Chuyển mạch:** Trong **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **Daemonization cổ điển** tiếp nhận điểm tựa từ **Controlling terminal** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tiến trình (process / 프로세스) trạng thái (state / 상태) R, S, D, T, Z** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Daemonization cổ điển

Trước systemd, daemon thường dùng mẫu (pattern / 패턴):

```text
fork
setsid
fork again
redirect stdio
change cwd
```

Mục tiêu là tách khỏi controlling terminal và session cũ.

Với systemd, double-fork thường không cần cho dịch vụ (service / 서비스) `Type=simple`; systemd muốn theo dõi foreground main tiến trình (process / 프로세스) trực tiếp.

Hiểu lịch sử này giúp giải thích vì sao một số daemon cũ có option `--foreground`.

> **Chuyển mạch:** Ở chặng này của **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **Daemonization cổ điển** xác định đầu vào; **Tiến trình (process / 프로세스) trạng thái (state / 상태) R, S, D, T, Z** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Sleeping không phải “tiến trình (process / 프로세스) không làm gì” theo nghĩa vô ích** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tiến trình (process / 프로세스) trạng thái (state / 상태) `R`, `S`, `D`, `T`, `Z`

Các trạng thái `ps` là biểu diễn rút gọn của scheduling/tác vụ (task / 작업) trạng thái (state / 상태).

- `R`: running hoặc runnable;
- `S`: interruptible sleep;
- `D`: uninterruptible sleep;
- `T`: stopped/traced;
- `Z`: zombie.

`D` thường liên quan tác vụ (task / 작업) đang chờ I/O/kernel điều kiện (condition / 조건) mà tín hiệu (signal / 신호) thông thường chưa làm nó rời wait ngay.

Nhiều tác vụ (task / 작업) `D` có thể làm tải (load / 로드) average cao dù CPU idle đáng kể.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **Tiến trình (process / 프로세스) trạng thái (state / 상태) R, S, D, T, Z** xác định đầu vào; **Sleeping không phải “tiến trình (process / 프로세스) không làm gì” theo nghĩa vô ích** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Luồng thực thi (thread / 스레드) ngăn xếp (stack / 스택) và bộ nhớ (memory / 메모리) chi phí (cost / 비용)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sleeping không phải “tiến trình (process / 프로세스) không làm gì” theo nghĩa vô ích

Sleep là cách kernel biểu diễn tác vụ (task / 작업) đang chờ sự kiện (event / 이벤트). Đây là trạng thái hiệu quả: tác vụ (task / 작업) không chiếm CPU trong thời gian chờ.

Ứng dụng (application / 애플리케이션) máy chủ (server / 서버) blocking I/O có thể có hàng trăm luồng thực thi (thread / 스레드) sleeping. Vấn đề chỉ xuất hiện khi luồng thực thi (thread / 스레드) count, ngăn xếp (stack / 스택) bộ nhớ (memory / 메모리) hoặc wakeup contention vượt giới hạn hợp lý.

> **Chuyển mạch:** Trong **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **Sleeping không phải “tiến trình (process / 프로세스) không làm gì” theo nghĩa vô ích** xác định đầu vào; **Luồng thực thi (thread / 스레드) ngăn xếp (stack / 스택) và bộ nhớ (memory / 메모리) chi phí (cost / 비용)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Ngữ cảnh (context / 맥락) switch lưu gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Luồng thực thi (thread / 스레드) ngăn xếp (stack / 스택) và bộ nhớ (memory / 메모리) chi phí (cost / 비용)

Mỗi luồng thực thi (thread / 스레드) cần ngăn xếp (stack / 스택) ánh xạ (mapping / 매핑) và kernel tác vụ (task / 작업) trạng thái (state / 상태).

Trong JVM, `-Xss` ảnh hưởng Java luồng thực thi (thread / 스레드) ngăn xếp (stack / 스택) kích thước (size / 크기). Hàng nghìn luồng thực thi (thread / 스레드) có thể tiêu tốn nhiều virtual bộ nhớ (memory / 메모리) và resident bộ nhớ (memory / 메모리) dù vùng nhớ động (heap / 힙) chưa đầy.

Vì vậy sức chứa (capacity / 용량) planning luồng thực thi (thread / 스레드) count phải nối với bộ nhớ (memory / 메모리) mô hình (model / 모델).

> **Chuyển mạch:** Ở chặng này của **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **Ngữ cảnh (context / 맥락) switch lưu gì?** tiếp nhận điểm tựa từ **Luồng thực thi (thread / 스레드) ngăn xếp (stack / 스택) và bộ nhớ (memory / 메모리) chi phí (cost / 비용)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **exec() và triển khai (deployment / 배포)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngữ cảnh (context / 맥락) switch lưu gì?

Khi scheduler chuyển từ tác vụ (task / 작업) A sang B, kernel phải bảo toàn CPU thực thi (execution / 실행) trạng thái (state / 상태) đủ để A tiếp tục sau đó.

Chi phí không chỉ là lưu register. bộ nhớ đệm (cache / 캐시)/TLB locality cũng có thể bị ảnh hưởng.

Nếu hàng nghìn runnable luồng thực thi (thread / 스레드) cạnh tranh ít CPU, độ trễ (latency / 지연 시간) tăng dù mọi luồng thực thi (thread / 스레드) “đang hoạt động”.

Xem [Kernel scheduler deep dive](../06_resources/kernel_scheduler_deep_dive.md).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **exec() và triển khai (deployment / 배포)** tiếp nhận điểm tựa từ **Ngữ cảnh (context / 맥락) switch lưu gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tiến trình (process / 프로세스) không gian tên (namespace / 네임스페이스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `exec()` và triển khai (deployment / 배포)

Khi systemd start dịch vụ (service / 서비스):

```text
systemd
  ↓ fork/clone-like spawn
  ↓ setup credentials/cgroup/fd/env
  ↓ execve application
application process
```

Do đó đơn vị (unit / 단위) cấu hình (configuration / 구성) cuối cùng biến thành tiến trình (process / 프로세스) attributes trước khi exec.

Môi trường (environment / 환경), WorkingDirectory, người dùng (user / 사용자), limits và tệp (file / 파일) descriptors đều có thể ảnh hưởng ứng dụng (application / 애플리케이션) trước khi dòng Java đầu tiên chạy.

> **Chuyển mạch:** Trong **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **exec() và triển khai (deployment / 배포)** xác định đầu vào; **Tiến trình (process / 프로세스) không gian tên (namespace / 네임스페이스)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **/proc/<PID> là cửa sổ tiến trình (process / 프로세스) mô hình (model / 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tiến trình (process / 프로세스) không gian tên (namespace / 네임스페이스)

PID không gian tên (namespace / 네임스페이스) làm cùng một tác vụ (task / 작업) có thể có PID khác nhau tùy viewpoint.

Host có thể thấy PID 32100, còn bộ chứa (container / 컨테이너) thấy PID 1.

Vì vậy PID là tên trong không gian tên (namespace / 네임스페이스), không phải định danh (identity / 식별자) tuyệt đối toàn hệ thống.

Xem [Namespace, cgroup và seccomp](../09_production/namespaces_cgroups_seccomp.md).

> **Chuyển mạch:** Ở chặng này của **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **Tiến trình (process / 프로세스) không gian tên (namespace / 네임스페이스)** xác định đầu vào; **/proc/<PID> là cửa sổ tiến trình (process / 프로세스) mô hình (model / 모델)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Tiến trình (process / 프로세스) thời gian tồn tại (lifetime / 수명) và tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명) không luôn giống nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `/proc/<PID>` là cửa sổ tiến trình (process / 프로세스) mô hình (model / 모델)

Một số tệp (file / 파일) hữu ích:

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

Thay vì coi `/proc` là danh sách lệnh phải nhớ, hãy map từng entry vào tài nguyên (resource / 자원) mà tiến trình (process / 프로세스) đang giữ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **/proc/<PID> là cửa sổ tiến trình (process / 프로세스) mô hình (model / 모델)** nêu điều cần giải thích; **Tiến trình (process / 프로세스) thời gian tồn tại (lifetime / 수명) và tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명) không luôn giống nhau** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tiến trình (process / 프로세스) thời gian tồn tại (lifetime / 수명) và tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명) không luôn giống nhau

Một tệp (file / 파일) có thể bị unlink nhưng vẫn tồn tại vì tiến trình (process / 프로세스) còn giữ tệp (file / 파일) descriptor.

Một dùng chung (shared / 공유) bộ nhớ (memory / 메모리) đối tượng (object / 객체) có thể được tiến trình (process / 프로세스) khác giữ.

Một socket liên kết (connection / 연결) có peer trạng thái (state / 상태) bên ngoài host.

Vì vậy “tiến trình (process / 프로세스) đã chết” không luôn đồng nghĩa mọi hệ quả bên ngoài lập tức biến mất.

Conversely, kernel sẽ tự bản phát hành (release / 릴리스) nhiều tài nguyên (resource / 자원) gắn quyền sở hữu (ownership / 소유권) trực tiếp với tiến trình (process / 프로세스) khi tiến trình (process / 프로세스) exit.

> **Chuyển mạch:** Trong **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **Tiến trình (process / 프로세스) thời gian tồn tại (lifetime / 수명) và tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명) không luôn giống nhau** nêu điều cần giải thích; **Mô hình tư duy (mental model / 사고 모델)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Hãy xem tiến trình (process / 프로세스) như một **bộ chứa (container / 컨테이너) lô-gic (logic / 논리) của thực thi (execution / 실행) trạng thái (state / 상태) và references**:

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

`fork()` tạo thực thi (execution / 실행) ngữ cảnh (context / 맥락) mới với nhiều trạng thái (state / 상태) kế thừa/chia sẻ theo ngữ nghĩa (semantics / 의미론). `exec()` thay program ảnh (image / 이미지). `exit()` kết thúc thực thi (execution / 실행). `wait()` hoàn tất quan hệ vòng đời (lifecycle / 생명주기) với parent.

> **Chuyển mạch:** Ở chặng này của **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, **Những hiểu lầm phổ biến** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến

**“fork bản sao (copy / 복사) toàn bộ RAM ngay.”** COW giúp parent/child chia sẻ pages cho tới khi ghi.

**“exec tạo tiến trình (process / 프로세스) mới.”** Exec thay program ảnh (image / 이미지) của tiến trình (process / 프로세스) hiện tại.

**“Zombie vẫn chạy và ăn CPU.”** Zombie đã kết thúc; nó chỉ còn exit bản ghi (record / 레코드) chờ parent reap.

**“Orphan và zombie là một.”** Orphan còn sống nhưng mất parent; zombie đã chết nhưng chưa được wait.

**“PID là định danh (identity / 식별자) ổn định.”** PID có thể tái sử dụng và thay đổi theo PID không gian tên (namespace / 네임스페이스).

**“Một Java tiến trình (process / 프로세스) là một scheduling thực thể (entity / 엔터티).”** Mỗi bản địa (native / 네이티브) luồng thực thi (thread / 스레드) là tác vụ (task / 작업) scheduler có thể quản lý riêng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tiến trình (process / 프로세스), address không gian (space / 공간), fork, exec và wait trong Linux**, sau nội dung của **Những hiểu lầm phổ biến**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Nên nối chương này với:

- [CPU privilege và syscall path](../00_foundations/cpu_privilege_exceptions_syscall_path.md);
- [File descriptor](../01_filesystem/files_streams_descriptors.md);
- [Virtual memory](../06_resources/virtual_memory_page_fault_reclaim_allocator.md);
- [IPC](./interprocess_communication.md);
- [Scheduler](../06_resources/kernel_scheduler_deep_dive.md);
- [Systemd service lifecycle](../05_system/systemd_units_dependencies_resources.md);
- [Container isolation](../09_production/namespaces_cgroups_seccomp.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
