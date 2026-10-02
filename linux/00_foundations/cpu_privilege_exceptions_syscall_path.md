# CPU privilege, exception và đường đi của lời gọi hệ thống (system call / 시스템 호출)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **CPU privilege, exception và đường đi của lời gọi hệ thống (system call / 시스템 호출)**. Route đi từ user/kernel privilege → syscall, interrupt và exception entry → saved state, stack và return → page fault, signal và context switch → overhead/diagnosis, để CPU path nối trực tiếp với hành vi tiến trình.

Chương [Kernel, không gian người dùng và lời gọi hệ thống](./kernel_userspace_syscalls.md) giải thích vì sao ứng dụng phải đi qua kernel để truy cập tài nguyên. Chương này đi sâu hơn một tầng: **CPU thực sự làm gì khi một chương trình từ người dùng (user / 사용자) không gian (space / 공간) đi vào kernel, vì sao lời gọi hệ thống (system call / 시스템 호출) khác interrupt và exception, trạng thái nào được lưu, và tại sao việc “vào kernel” không đồng nghĩa với đổi sang tiến trình (process / 프로세스) khác**.

Mục tiêu không phải học assembly để viết kernel. Mục tiêu là có một mô hình đủ chính xác để hiểu các khái niệm như lời gọi hệ thống (system call / 시스템 호출) overhead, page fault, tín hiệu (signal / 신호) delivery, ngữ cảnh (context / 맥락) switch, privilege ring, CPU exception và kernel ngăn xếp (stack / 스택).

## CPU không biết khái niệm “ứng dụng Java”

Ở tầng phần cứng, CPU không nhìn thấy khái niệm Spring Boot, Python hay shell. CPU chỉ thực thi instruction trong một trạng thái nhất định: thanh ghi, program counter, ngăn xếp (stack / 스택) pointer, bảng trang (page table / 페이지 테이블) đang hoạt động và mức đặc quyền hiện tại.

Hệ điều hành xây dựng các lớp trừu tượng cao hơn như tiến trình (process / 프로세스), luồng thực thi (thread / 스레드), tệp (file / 파일) descriptor và socket bằng cách sử dụng các cơ chế phần cứng này.

Một luồng thực thi (thread / 스레드) Java đang chạy cuối cùng vẫn là một luồng instruction được CPU thực thi. Khi luồng thực thi (thread / 스레드) chỉ cộng số hoặc thao tác dữ liệu đã nằm trong bộ nhớ của chính nó, CPU có thể tiếp tục chạy ở **chế độ người dùng (user mode / 사용자 모드)**. Khi luồng thực thi (thread / 스레드) cần đọc tệp (file / 파일), chờ socket hoặc xin thêm ánh xạ (mapping / 매핑) bộ nhớ, nó phải đi qua giao diện kernel.

> **Chuyển mạch:** Trong **CPU privilege, exception và đường đi của lời gọi hệ thống (system call / 시스템 호출)**, **Mức đặc quyền tồn tại để bảo vệ hệ thống** tiếp nhận điểm tựa từ **CPU không biết khái niệm “ứng dụng Java”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Người dùng (user / 사용자) không gian (space / 공간) và kernel không gian (space / 공간) còn là ranh giới địa chỉ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mức đặc quyền tồn tại để bảo vệ hệ thống

Kiến trúc CPU cung cấp các mức đặc quyền để giới hạn instruction và vùng bộ nhớ mà mã đang chạy có thể truy cập.

Trên x86 thường nói tới các **ring**. Linux chủ yếu sử dụng ring 3 cho người dùng (user / 사용자) không gian (space / 공간) và ring 0 cho kernel. Trên ARM có mô hình exception mức (level / 수준) khác, nhưng ý tưởng nền tảng tương tự: mã ứng dụng không được quyền thực hiện mọi thao tác mà kernel có thể làm.

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

Nếu tiến trình người dùng (user process / 사용자 프로세스) có thể tùy ý sửa bảng trang (page table / 페이지 테이블), cấu hình interrupt controller hoặc ghi vào bộ nhớ (memory / 메모리) của kernel thì mọi cơ chế permission phía trên gần như mất ý nghĩa.

> **Chuyển mạch:** Ở chặng này của **CPU privilege, exception và đường đi của lời gọi hệ thống (system call / 시스템 호출)**, **Người dùng (user / 사용자) không gian (space / 공간) và kernel không gian (space / 공간) còn là ranh giới địa chỉ** tiếp nhận điểm tựa từ **Mức đặc quyền tồn tại để bảo vệ hệ thống** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ba con đường phổ biến làm CPU đi vào kernel** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Người dùng (user / 사용자) không gian (space / 공간) và kernel không gian (space / 공간) còn là ranh giới địa chỉ

Mỗi tiến trình (process / 프로세스) có không gian địa chỉ ảo riêng. Một phần address không gian (space / 공간) dành cho tiến trình người dùng (user process / 사용자 프로세스); kernel có vùng riêng được bảo vệ theo thiết kế kiến trúc và cấu hình hệ thống.

CPU kết hợp bảng trang (page table / 페이지 테이블) và bit quyền trên bảng trang (page table / 페이지 테이블) entry để kiểm soát việc truy cập. Vì vậy một con trỏ trong tiến trình người dùng (user process / 사용자 프로세스) không thể đơn giản trỏ tới kernel bộ nhớ (memory / 메모리) rồi đọc nội dung.

Nếu tiến trình (process / 프로세스) truy cập địa chỉ không hợp lệ, CPU có thể tạo ra một exception như page fault. Kernel nhận sự kiện đó và quyết định:

- ánh xạ trang nếu đây là fault hợp lệ;
- mở rộng ánh xạ (mapping / 매핑) nếu ngữ nghĩa (semantics / 의미론) cho phép;
- hoặc gửi tín hiệu (signal / 신호) như `SIGSEGV` nếu truy cập không hợp lệ.

Điểm quan trọng là nhiều hành vi mà lập trình viên nhìn thấy ở tầng tiến trình (process / 프로세스) thực ra bắt đầu từ exception của CPU rồi được kernel chuyển thành ngữ nghĩa (semantics / 의미론) của Unix.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CPU privilege, exception và đường đi của lời gọi hệ thống (system call / 시스템 호출)**, **Ba con đường phổ biến làm CPU đi vào kernel** tiếp nhận điểm tựa từ **Người dùng (user / 사용자) không gian (space / 공간) và kernel không gian (space / 공간) còn là ranh giới địa chỉ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đường đi khái niệm của một lời gọi hệ thống (system call / 시스템 호출)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ba con đường phổ biến làm CPU đi vào kernel

Có thể chia thành ba nhóm khái niệm lớn.

### Lời gọi hệ thống (system call / 시스템 호출)

Tiến trình (process / 프로세스) chủ động yêu cầu kernel thực hiện công việc:

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
- breakpoint/gỡ lỗi (debug / 디버그) trap.

Exception gắn với luồng instruction đang thực thi.

### Hardware interrupt

Thiết bị hoặc bộ điều khiển báo một sự kiện bất đồng bộ, ví dụ NIC báo có packet hoặc lưu trữ (storage / 저장소) báo I/O hoàn tất.

Interrupt không nhất thiết liên quan trực tiếp tới instruction user-space đang chạy lúc đó.

Ba nhóm đều có thể đưa CPU vào kernel, nhưng nguyên nhân và ngữ nghĩa (semantics / 의미론) rất khác nhau.

Xem thêm [Interrupt, softirq và device model](./interrupts_softirq_device_model.md).

> **Chuyển mạch:** Trong **CPU privilege, exception và đường đi của lời gọi hệ thống (system call / 시스템 호출)**, **Đường đi khái niệm của một lời gọi hệ thống (system call / 시스템 호출)** tiếp nhận điểm tựa từ **Ba con đường phổ biến làm CPU đi vào kernel** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **ABI là hợp đồng giữa nhị phân (binary / 이진) và kernel** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đường đi khái niệm của một lời gọi hệ thống (system call / 시스템 호출)

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

Điều cần hiểu là lời gọi hệ thống (system call / 시스템 호출) không phải hàm (function / 함수) lời gọi (call / 호출) bình thường. Nó đi qua một **privilege ranh giới (boundary / 경계)** với quy tắc ABI và entry/exit riêng.

> **Chuyển mạch:** Ở chặng này của **CPU privilege, exception và đường đi của lời gọi hệ thống (system call / 시스템 호출)**, **ABI là hợp đồng giữa nhị phân (binary / 이진) và kernel** tiếp nhận điểm tựa từ **Đường đi khái niệm của một lời gọi hệ thống (system call / 시스템 호출)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao thư viện thường đứng trước lời gọi hệ thống (system call / 시스템 호출)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## ABI là hợp đồng giữa nhị phân (binary / 이진) và kernel

**ứng dụng (application / 애플리케이션) nhị phân (binary / 이진) giao diện (interface / 인터페이스) (ABI)** quy định cách nhị phân (binary / 이진) giao tiếp ở mức máy: calling convention, register, bố cục (layout / 레이아웃) và lời gọi hệ thống (system call / 시스템 호출) giao diện (interface / 인터페이스).

API là giao diện ở mức mã nguồn (source code / 소스 코드). ABI là hợp đồng ở mức nhị phân (binary / 이진).

Ví dụ chương trình C gọi `read()`. mã nguồn (source code / 소스 코드) nhìn thấy API của libc. Nhưng libc phải biết ABI kernel để đặt đúng syscall number và arguments.

Đây là lý do nhị phân (binary / 이진) tính tương thích (compatibility / 호환성) khác nguồn (source / 소스) tính tương thích (compatibility / 호환성).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CPU privilege, exception và đường đi của lời gọi hệ thống (system call / 시스템 호출)**, **Vì sao thư viện thường đứng trước lời gọi hệ thống (system call / 시스템 호출)?** tiếp nhận điểm tựa từ **ABI là hợp đồng giữa nhị phân (binary / 이진) và kernel** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **vDSO và ý tưởng tránh lời gọi hệ thống (system call / 시스템 호출) không cần thiết** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao thư viện thường đứng trước lời gọi hệ thống (system call / 시스템 호출)?

Thời gian chạy (runtime / 런타임) hoặc libc có thể:

- chuẩn hóa API;
- xử lý buffer;
- chuyển đổi lỗi;
- chọn lời gọi hệ thống (system call / 시스템 호출) phù hợp;
- thực hiện fast đường dẫn (path / 경로) ở người dùng (user / 사용자) không gian (space / 공간) nếu có thể.

Ví dụ một số thao tác thời gian có thể tận dụng **vDSO (virtual dynamic shared object)** để đọc thông tin mà không cần trap vào kernel ở mọi lần gọi.

Vì thế khi profiling không nên suy luận rằng mọi API hệ thống đều gây một kernel entry thực sự.

> **Chuyển mạch:** Trong **CPU privilege, exception và đường đi của lời gọi hệ thống (system call / 시스템 호출)**, **vDSO và ý tưởng tránh lời gọi hệ thống (system call / 시스템 호출) không cần thiết** tiếp nhận điểm tựa từ **Vì sao thư viện thường đứng trước lời gọi hệ thống (system call / 시스템 호출)?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kernel ngăn xếp (stack / 스택) khác người dùng (user / 사용자) ngăn xếp (stack / 스택)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## vDSO và ý tưởng tránh lời gọi hệ thống (system call / 시스템 호출) không cần thiết

Một lời gọi hệ thống (system call / 시스템 호출) có chi phí. Với những thông tin kernel có thể công bố an toàn qua vùng bộ nhớ (memory / 메모리) đặc biệt, Linux có thể cung cấp vDSO để tiến trình người dùng (user process / 사용자 프로세스) gọi mã (code / 코드) được ánh xạ sẵn.

Các API thời gian là ví dụ điển hình trên nhiều hệ thống.

Ý tưởng lớn hơn là: **ranh giới privilege chỉ nên đi qua khi thực sự cần kernel thực hiện thao tác đặc quyền hoặc đồng bộ trạng thái**.

> **Chuyển mạch:** Ở chặng này của **CPU privilege, exception và đường đi của lời gọi hệ thống (system call / 시스템 호출)**, **Kernel ngăn xếp (stack / 스택) khác người dùng (user / 사용자) ngăn xếp (stack / 스택)** tiếp nhận điểm tựa từ **vDSO và ý tưởng tránh lời gọi hệ thống (system call / 시스템 호출) không cần thiết** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Điều gì phải được bảo toàn khi vào kernel?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kernel ngăn xếp (stack / 스택) khác người dùng (user / 사용자) ngăn xếp (stack / 스택)

Mỗi luồng thực thi (thread / 스레드) có user-space ngăn xếp (stack / 스택) dùng khi chạy mã (code / 코드) ứng dụng. Khi CPU đi vào kernel để xử lý lời gọi hệ thống (system call / 시스템 호출) hoặc exception, kernel cần vùng ngăn xếp (stack / 스택) phù hợp để xử lý kernel mã (code / 코드).

Không nên hình dung kernel tiếp tục dùng nguyên người dùng (user / 사용자) ngăn xếp (stack / 스택) như không có ranh giới bảo mật. Kernel duy trì ngữ cảnh riêng để xử lý an toàn.

Khái niệm này giúp hiểu vì sao luồng thực thi (thread / 스레드) có cả trạng thái user-space lẫn kernel-side trạng thái (state / 상태).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CPU privilege, exception và đường đi của lời gọi hệ thống (system call / 시스템 호출)**, **Điều gì phải được bảo toàn khi vào kernel?** tiếp nhận điểm tựa từ **Kernel ngăn xếp (stack / 스택) khác người dùng (user / 사용자) ngăn xếp (stack / 스택)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lời gọi hệ thống (system call / 시스템 호출) có luôn chạy ngay đến cuối không?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Điều gì phải được bảo toàn khi vào kernel?

CPU và entry mã (code / 코드) phải giữ đủ trạng thái để sau khi xử lý xong có thể quay lại đúng nơi trong người dùng (user / 사용자) program.

Khái niệm cần bảo toàn gồm:

- instruction pointer;
- ngăn xếp (stack / 스택) pointer;
- flags/status register;
- register cần thiết;
- thông tin privilege trước đó.

Kernel còn phải biết luồng thực thi (thread / 스레드) nào đang chạy để liên kết lời gọi hệ thống (system call / 시스템 호출) với credentials, tệp (file / 파일) descriptor bảng (table / 테이블), bộ nhớ (memory / 메모리) mappings và scheduling trạng thái (state / 상태) tương ứng.

> **Chuyển mạch:** Trong **CPU privilege, exception và đường đi của lời gọi hệ thống (system call / 시스템 호출)**, **Lời gọi hệ thống (system call / 시스템 호출) có luôn chạy ngay đến cuối không?** tiếp nhận điểm tựa từ **Điều gì phải được bảo toàn khi vào kernel?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Blocking không có nghĩa CPU đứng yên** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lời gọi hệ thống (system call / 시스템 호출) có luôn chạy ngay đến cuối không?

Không.

`read()` trên dữ liệu đã có trong page bộ nhớ đệm (cache / 캐시) có thể hoàn tất nhanh. Nhưng `read()` trên socket chưa có dữ liệu có thể phải chờ.

Nếu luồng thực thi (thread / 스레드) không thể tiếp tục, kernel có thể đặt luồng thực thi (thread / 스레드) vào trạng thái ngủ rồi scheduler chọn luồng thực thi (thread / 스레드) khác chạy.

Do đó một lời gọi hệ thống (system call / 시스템 호출) có hai khả năng rất khác:

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

Đây là điểm nối trực tiếp giữa lời gọi hệ thống (system call / 시스템 호출), wait hàng đợi (queue / 큐) và scheduler.

> **Chuyển mạch:** Ở chặng này của **CPU privilege, exception và đường đi của lời gọi hệ thống (system call / 시스템 호출)**, **Blocking không có nghĩa CPU đứng yên** tiếp nhận điểm tựa từ **Lời gọi hệ thống (system call / 시스템 호출) có luôn chạy ngay đến cuối không?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngữ cảnh (context / 맥락) switch khác syscall entry** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Blocking không có nghĩa CPU đứng yên

Khi luồng thực thi (thread / 스레드) Java gọi socket read và chưa có dữ liệu, luồng thực thi (thread / 스레드) đó có thể ngủ. CPU không nhất thiết chờ cùng nó; scheduler có thể chạy luồng thực thi (thread / 스레드) khác.

Vì thế “yêu cầu (request / 요청) đang chờ I/O 200 ms” không có nghĩa CPU đã tiêu thụ 200 ms.

Đây là nền tảng để phân biệt:

- wall-clock độ trễ (latency / 지연 시간);
- CPU thời gian (time / 시간);
- off-CPU thời gian (time / 시간).

Xem [Quan sát bằng strace, perf và eBPF](../09_production/observability_tracing_strace_perf.md).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CPU privilege, exception và đường đi của lời gọi hệ thống (system call / 시스템 호출)**, **Ngữ cảnh (context / 맥락) switch khác syscall entry** tiếp nhận điểm tựa từ **Blocking không có nghĩa CPU đứng yên** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Page fault là exception nhưng không luôn là lỗi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngữ cảnh (context / 맥락) switch khác syscall entry

Giả sử luồng thực thi (thread / 스레드) A gọi `getpid()` và kernel trả ngay. CPU có thể:

```text
A user mode
→ A kernel mode
→ A user mode
```

mà không chuyển sang luồng thực thi (thread / 스레드) B.

Đây là **chế độ (mode / 모드) switch**, không phải nhất thiết là **ngữ cảnh (context / 맥락) switch**.

Nếu A gọi `read()` rồi ngủ và scheduler chạy B:

```text
A user
→ A kernel
→ scheduler
→ B
```

lúc này có ngữ cảnh (context / 맥락) switch giữa scheduling entities.

Phân biệt này quan trọng khi đọc metrics ngữ cảnh (context / 맥락) switch và đánh giá syscall overhead.

> **Chuyển mạch:** Trong **CPU privilege, exception và đường đi của lời gọi hệ thống (system call / 시스템 호출)**, **Page fault là exception nhưng không luôn là lỗi** tiếp nhận điểm tựa từ **Ngữ cảnh (context / 맥락) switch khác syscall entry** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tín hiệu (signal / 신호) delivery liên quan gì tới ranh giới kernel?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Page fault là exception nhưng không luôn là lỗi

Tên “fault” dễ gây cảm giác đây là sự cố. Trong virtual bộ nhớ (memory / 메모리), page fault có thể là một phần hoạt động hoàn toàn bình thường.

Ví dụ tiến trình (process / 프로세스) truy cập page được `mmap()` nhưng chưa được đưa vào RAM. CPU phát hiện bảng trang (page table / 페이지 테이블) chưa có ánh xạ (mapping / 매핑) hiện diện và tạo exception. Kernel kiểm tra VMA, lấy page phù hợp rồi cập nhật bảng trang (page table / 페이지 테이블).

Nếu mọi thứ hợp lệ, tiến trình (process / 프로세스) tiếp tục như chưa có lỗi ở tầng ứng dụng.

Chỉ khi địa chỉ hoặc quyền không hợp lệ, kernel mới có thể chuyển thành `SIGSEGV` hoặc lỗi tương ứng.

Xem [Page fault, allocator và reclaim](../06_resources/virtual_memory_page_fault_reclaim_allocator.md).

> **Chuyển mạch:** Ở chặng này của **CPU privilege, exception và đường đi của lời gọi hệ thống (system call / 시스템 호출)**, **Tín hiệu (signal / 신호) delivery liên quan gì tới ranh giới kernel?** tiếp nhận điểm tựa từ **Page fault là exception nhưng không luôn là lỗi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Preemption và việc kernel có thể bị ngắt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tín hiệu (signal / 신호) delivery liên quan gì tới ranh giới kernel?

Tín hiệu (signal / 신호) là trạng thái do kernel quản lý. Khi cần giao tín hiệu (signal / 신호) cho tiến trình (process / 프로세스)/luồng thực thi (thread / 스레드), kernel phải sắp xếp để user-space handler chạy trong ngữ cảnh phù hợp.

Tín hiệu (signal / 신호) không phải một hàm (function / 함수) lời gọi (call / 호출) trực tiếp từ tiến trình (process / 프로세스) gửi sang tiến trình (process / 프로세스) khác. tiến trình (process / 프로세스) gửi yêu cầu qua kernel; kernel kiểm tra quyền, đánh dấu pending tín hiệu (signal / 신호) và giao theo ngữ nghĩa (semantics / 의미론) tương ứng.

Điều này giải thích vì sao `SIGKILL` không thể bị user-space handler bắt: kernel quyết định kết thúc tiến trình (process / 프로세스) trước khi người dùng (user / 사용자) mã (code / 코드) có cơ hội override ngữ nghĩa (semantics / 의미론) đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CPU privilege, exception và đường đi của lời gọi hệ thống (system call / 시스템 호출)**, **Preemption và việc kernel có thể bị ngắt** tiếp nhận điểm tựa từ **Tín hiệu (signal / 신호) delivery liên quan gì tới ranh giới kernel?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bảo mật (security / 보안): syscall ranh giới (boundary / 경계) là nơi chính sách gặp yêu cầu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Preemption và việc kernel có thể bị ngắt

Kernel hiện đại không đơn giản là một đoạn mã (code / 코드) “chạy xong rồi mới nhường CPU”. Tùy cấu hình và ngữ cảnh (context / 맥락), kernel có cơ chế preemption, interrupt handling và synchronization phức tạp.

Một CPU đang chạy kernel mã (code / 코드) có thể vẫn nhận interrupt. Tuy nhiên không phải mọi kernel ngữ cảnh (context / 맥락) đều cho phép sleep hoặc schedule.

Đây là lý do kernel cần nhiều thành phần nguyên thủy (primitive / 기본 요소) đồng bộ khác nhau thay vì chỉ một loại mutex.

Xem [Đồng thời, khóa và RCU trong kernel](./kernel_concurrency_locking_rcu.md).

> **Chuyển mạch:** Trong **CPU privilege, exception và đường đi của lời gọi hệ thống (system call / 시스템 호출)**, **Preemption và việc kernel có thể bị ngắt** đã nêu tiêu chí phân biệt, còn **Bảo mật (security / 보안): syscall ranh giới (boundary / 경계) là nơi chính sách gặp yêu cầu** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Seccomp lọc lời gọi hệ thống (system call / 시스템 호출) như thế nào về mặt ý tưởng?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bảo mật (security / 보안): syscall ranh giới (boundary / 경계) là nơi chính sách gặp yêu cầu

Khi tiến trình (process / 프로세스) gọi `openat()`, kernel không chỉ tìm tệp (file / 파일). Kernel còn xem:

- credentials của tác vụ (task / 작업);
- permission chế độ (mode / 모드)/ACL;
- không gian tên (namespace / 네임스페이스);
- mount chính sách (policy / 정책);
- LSM như SELinux/AppArmor;
- seccomp chính sách (policy / 정책) nếu có.

Một lời gọi hệ thống (system call / 시스템 호출) vì vậy là điểm mà **ý định của ứng dụng (application / 애플리케이션)** gặp **trạng thái và chính sách của kernel**.

Đây là mô hình tư duy (mental model / 사고 모델) rất hữu ích khi đọc `EPERM` hoặc `EACCES`: thay vì hỏi “Linux có lỗi không?”, hãy hỏi lớp chính sách (policy / 정책) nào đã từ chối thao tác (operation / 연산) nào.

> **Chuyển mạch:** Ở chặng này của **CPU privilege, exception và đường đi của lời gọi hệ thống (system call / 시스템 호출)**, **Bảo mật (security / 보안): syscall ranh giới (boundary / 경계) là nơi chính sách gặp yêu cầu** đã nêu tiêu chí phân biệt, còn **Seccomp lọc lời gọi hệ thống (system call / 시스템 호출) như thế nào về mặt ý tưởng?** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Quan sát lời gọi hệ thống (system call / 시스템 호출) bằng strace** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Seccomp lọc lời gọi hệ thống (system call / 시스템 호출) như thế nào về mặt ý tưởng?

Seccomp có thể hạn chế tập lời gọi hệ thống (system call / 시스템 호출) hoặc mẫu argument mà tiến trình (process / 프로세스) được phép sử dụng tùy chính sách (policy / 정책).

Bộ chứa (container / 컨테이너) thời gian chạy (runtime / 런타임) thường tận dụng cơ chế này để giảm attack surface. Nếu ứng dụng (application / 애플리케이션) không cần một syscall nguy hiểm, việc chặn nó làm giảm khả năng mã bị khai thác dùng syscall đó.

Seccomp không thay thế filesystem permission, năng lực (capability / 역량) hay không gian tên (namespace / 네임스페이스). Nó là thêm một lớp kiểm soát tại syscall ranh giới (boundary / 경계).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CPU privilege, exception và đường đi của lời gọi hệ thống (system call / 시스템 호출)**, **Quan sát lời gọi hệ thống (system call / 시스템 호출) bằng strace** tiếp nhận điểm tựa từ **Seccomp lọc lời gọi hệ thống (system call / 시스템 호출) như thế nào về mặt ý tưởng?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **strace có overhead** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quan sát lời gọi hệ thống (system call / 시스템 호출) bằng `strace`

Ví dụ:

```bash
strace -tt -T -f -o /tmp/app.strace curl -s http://127.0.0.1:8080/health
```

Một số option:

- `-tt`: timestamp chi tiết;
- `-T`: thời gian ở mỗi syscall;
- `-f`: theo dõi child/luồng thực thi (thread / 스레드) phù hợp;
- `-o`: ghi ra tệp (file / 파일).

Không nên đọc `strace` như danh sách ngẫu nhiên. Hãy tìm câu hỏi cụ thể:

```text
đang chờ connect()?
đang lặp openat() vì thiếu file?
read() bị block lâu?
futex() chờ lock?
ENOENT ở path nào?
```

> **Chuyển mạch:** Trong **CPU privilege, exception và đường đi của lời gọi hệ thống (system call / 시스템 호출)**, **strace có overhead** tiếp nhận điểm tựa từ **Quan sát lời gọi hệ thống (system call / 시스템 호출) bằng strace** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hệ thống (system / 시스템) CPU thời gian (time / 시간) nói điều gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `strace` có overhead

Tracing lời gọi hệ thống (system call / 시스템 호출) làm thay đổi timing. Với tải công việc (workload / 워크로드) latency-sensitive hoặc thông lượng (throughput / 처리량) cao, attach `strace` có thể tạo overhead đáng kể.

Môi trường vận hành (production / 운영 환경) diagnosis phải cân bằng lượng bằng chứng (evidence / 증거) với ảnh hưởng quan sát.

Khi cần quan sát nhẹ hơn hoặc aggregate nhiều sự kiện (event / 이벤트), eBPF/perf có thể phù hợp hơn tùy mục tiêu.

> **Chuyển mạch:** Ở chặng này của **CPU privilege, exception và đường đi của lời gọi hệ thống (system call / 시스템 호출)**, **Hệ thống (system / 시스템) CPU thời gian (time / 시간) nói điều gì?** tiếp nhận điểm tựa từ **strace có overhead** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hệ thống (system / 시스템) CPU thời gian (time / 시간) nói điều gì?

Trong `top`, `vmstat` hoặc metrics, thời gian CPU thường được chia thành người dùng (user / 사용자)/hệ thống (system / 시스템) và các nhóm khác.

`system` cao nghĩa CPU đang thực thi kernel mã (code / 코드) nhiều hơn. Nguyên nhân có thể là:

- syscall tỷ lệ (rate / 비율) cao;
- mạng (network / 네트워크) packet processing;
- filesystem công việc (work / 작업);
- page fault/reclaim;
- locking/kernel overhead;
- driver/interrupt-related công việc (work / 작업).

Không nên nhảy thẳng tới kết luận kernel bug.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **CPU privilege, exception và đường đi của lời gọi hệ thống (system call / 시스템 호출)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Hệ thống (system / 시스템) CPU thời gian (time / 시간) nói điều gì?** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Hãy hình dung một luồng thực thi (thread / 스레드) có hai “mặt” liên tục của cùng một thực thi (execution / 실행) ngữ cảnh (context / 맥락):

```text
user-space execution
        ↓ system call / exception
kernel execution thay mặt thread đó
        ↓ return / wakeup
user-space execution tiếp tục
```

Kernel không phải một tiến trình (process / 프로세스) riêng mà ứng dụng (application / 애플리케이션) “gửi yêu cầu (request / 요청)” qua mạng (network / 네트워크). Kernel mã (code / 코드) có thể chạy trực tiếp trên CPU trong ngữ cảnh (context / 맥락) của luồng thực thi (thread / 스레드) đang gọi, hoặc trong interrupt/kernel worker ngữ cảnh (context / 맥락) tùy loại công việc.

> **Chuyển mạch:** Trong **CPU privilege, exception và đường đi của lời gọi hệ thống (system call / 시스템 호출)**, **Những hiểu lầm phổ biến** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến

**“lời gọi hệ thống (system call / 시스템 호출) luôn tạo ngữ cảnh (context / 맥락) switch.”** Không. Nó tạo privilege chuyển tiếp (transition / 전이); ngữ cảnh (context / 맥락) switch chỉ xảy ra nếu scheduler đổi scheduling thực thể (entity / 엔터티).

**“Page fault nghĩa là chương trình lỗi.”** Nhiều page fault là cơ chế demand paging bình thường.

**“Kernel chế độ (mode / 모드) nghĩa là chạy PID 0 hoặc tiến trình (process / 프로세스) kernel riêng.”** Kernel mã (code / 코드) có thể chạy trong ngữ cảnh (context / 맥락) của tác vụ (task / 작업) hiện tại hoặc interrupt/kernel luồng thực thi (thread / 스레드) ngữ cảnh (context / 맥락); không nên dùng một mô hình tư duy (mental model / 사고 모델) duy nhất cho mọi trường hợp.

**“hàm (function / 함수) C nào đọc tệp (file / 파일) cũng trực tiếp là lời gọi hệ thống (system call / 시스템 호출).”** thời gian chạy (runtime / 런타임)/thư viện (library / 라이브러리) có thể buffer hoặc dùng cơ chế khác; API và syscall không luôn 1:1.

**“hệ thống (system / 시스템) CPU cao chứng minh kernel đang gặp lỗi.”** Nó chỉ chứng minh nhiều CPU thời gian (time / 시간) đang ở kernel; cần tìm subsystem tạo công việc đó.

> **Chuyển mạch:** Ở chặng này của **CPU privilege, exception và đường đi của lời gọi hệ thống (system call / 시스템 호출)**, sau nội dung của **Những hiểu lầm phổ biến**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Chương này nối trực tiếp với:

- [Kernel, user space và system call](./kernel_userspace_syscalls.md) — mô hình tổng quan;
- [Interrupt, softirq và device model](./interrupts_softirq_device_model.md) — đường vào kernel từ phần cứng;
- [Đồng thời và synchronization trong kernel](./kernel_concurrency_locking_rcu.md) — bảo vệ dữ liệu khi kernel chạy song song;
- [Process và address space](../04_process/process_address_space_fork_exec_wait.md) — tác vụ (task / 작업) mà syscall đang thay mặt;
- [Virtual memory](../06_resources/virtual_memory_page_fault_reclaim_allocator.md) — page fault và ánh xạ (mapping / 매핑);
- [Tracing](../09_production/observability_tracing_strace_perf.md) — quan sát những cơ chế này khi hệ thống đang chạy.

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
