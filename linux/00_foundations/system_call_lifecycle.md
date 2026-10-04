# Vòng đời lời gọi hệ thống: từ người dùng (user / 사용자) không gian (space / 공간) vào kernel và quay trở lại

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Vòng đời lời gọi hệ thống: từ người dùng (user / 사용자) không gian (space / 공간) vào kernel và quay trở lại**. Route đi từ userspace/kernel boundary → libc wrapper → syscall entry/argument validation → kernel work, blocking và return path → errno/signals/observability, để system call được đọc như một vòng đời.

Lời gọi hệ thống (system call / 시스템 호출) là một trong những ranh giới quan trọng nhất của Linux. Ứng dụng không trực tiếp đọc đĩa, tạo socket hay ánh xạ bộ nhớ vật lý. Nó yêu cầu kernel thực hiện những thao tác đó thông qua một giao diện được kiểm soát. Vì vậy muốn hiểu Linux sâu, cần hiểu không chỉ tên các lời gọi hệ thống (system call / 시스템 호출) mà còn cả **vòng đời của một lời gọi từ người dùng (user / 사용자) không gian (space / 공간) vào kernel rồi quay lại**.

## Vì sao cần ranh giới lời gọi hệ thống (system call / 시스템 호출)?

Người dùng (user / 사용자) không gian (space / 공간) và kernel không gian (space / 공간) có mức đặc quyền khác nhau. Mã chạy trong người dùng (user / 사용자) không gian (space / 공간) không được phép tự ý truy cập bộ nhớ kernel, cấu hình thiết bị hay thao tác trực tiếp với bảng trang. Nếu cho phép điều đó, một lỗi nhỏ trong ứng dụng có thể phá hỏng toàn bộ hệ thống.

Lời gọi hệ thống (system call / 시스템 호출) tạo ra một cổng giao tiếp có kiểm soát:

```text
application
    ↓
libc / runtime wrapper
    ↓
system call entry
    ↓
kernel validation + policy + implementation
    ↓
return value / errno
    ↓
application
```

Kernel nhận yêu cầu, kiểm tra đối số, quyền, trạng thái tài nguyên và sau đó mới thực hiện thao tác.

> **Nối mạch:** Trong **Vòng đời lời gọi hệ thống: từ người dùng (user / 사용자) không gian (space / 공간) vào kernel và quay trở lại**, **Wrapper của thư viện khác lời gọi hệ thống (system call / 시스템 호출) như thế nào?** nối từ **Vì sao cần ranh giới lời gọi hệ thống (system call / 시스템 호출)?** sang **Điều gì xảy ra khi CPU đi vào kernel?**, vì cơ chế trước tạo đầu vào cho bước sau.

## Wrapper của thư viện khác lời gọi hệ thống (system call / 시스템 호출) như thế nào?

Khi chương trình C gọi:

```c
open("/tmp/a.txt", O_RDONLY);
```

hàm `open()` thường là wrapper trong libc. Wrapper này có thể chuẩn hóa đối số, chọn lời gọi hệ thống (system call / 시스템 호출) phù hợp như `openat()` và chuyển mã lỗi từ giá trị trả về ở kernel thành `errno` ở người dùng (user / 사용자) không gian (space / 공간).

Vì vậy **thư viện (library / 라이브러리) lời gọi (call / 호출)** và **lời gọi hệ thống (system call / 시스템 호출)** không phải luôn là một-một.

Có hàm thư viện không cần lời gọi hệ thống (system call / 시스템 호출), ví dụ một số thao tác chuỗi. Ngược lại một hàm thư viện có thể gọi nhiều lời gọi hệ thống (system call / 시스템 호출) tùy tình huống.

Quan sát bằng:

```bash
strace -e openat,read,close cat /etc/hostname
```

> **Nối mạch:** Ở chặng này của **Vòng đời lời gọi hệ thống: từ người dùng (user / 사용자) không gian (space / 공간) vào kernel và quay trở lại**, **Điều gì xảy ra khi CPU đi vào kernel?** nối từ **Wrapper của thư viện khác lời gọi hệ thống (system call / 시스템 호출) như thế nào?** sang **Lời gọi hệ thống (system call / 시스템 호출) không đồng nghĩa ngữ cảnh (context / 맥락) switch**, vì cơ chế trước tạo đầu vào cho bước sau.

## Điều gì xảy ra khi CPU đi vào kernel?

Chi tiết phụ thuộc kiến trúc CPU, nhưng ý tưởng chung là CPU chuyển từ chế độ ít đặc quyền sang chế độ đặc quyền cao hơn thông qua cơ chế entry được thiết kế cho lời gọi hệ thống (system call / 시스템 호출).

Kernel cần biết:

- số hiệu lời gọi hệ thống (system call / 시스템 호출);
- các đối số;
- ngữ cảnh tiến trình hiện tại;
- nơi trả kết quả về người dùng (user / 사용자) không gian (space / 공간).

Trên x86-64, các thanh ghi được dùng để truyền số lời gọi hệ thống (system call / 시스템 호출) và đối số theo ABI đã định nghĩa. Ứng dụng bình thường không nên viết lô-gic (logic / 논리) phụ thuộc trực tiếp vào chi tiết này nếu libc/thời gian chạy (runtime / 런타임) đã che giấu nó.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Vòng đời lời gọi hệ thống: từ người dùng (user / 사용자) không gian (space / 공간) vào kernel và quay trở lại**, **Lời gọi hệ thống (system call / 시스템 호출) không đồng nghĩa ngữ cảnh (context / 맥락) switch** nối từ **Điều gì xảy ra khi CPU đi vào kernel?** sang **Blocking và sleeping trong lời gọi hệ thống (system call / 시스템 호출)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Lời gọi hệ thống (system call / 시스템 호출) không đồng nghĩa ngữ cảnh (context / 맥락) switch

Đây là một hiểu lầm rất phổ biến.

Khi luồng thực thi (thread / 스레드) gọi lời gọi hệ thống (system call / 시스템 호출), CPU chuyển từ chế độ người dùng (user mode / 사용자 모드) sang kernel chế độ (mode / 모드), nhưng **luồng thực thi (thread / 스레드) vẫn có thể là cùng luồng thực thi (thread / 스레드) đang chạy**. Đây là thay đổi mức đặc quyền, không tự động là ngữ cảnh (context / 맥락) switch sang luồng thực thi (thread / 스레드) khác.

Ngữ cảnh (context / 맥락) switch chỉ xảy ra khi scheduler quyết định đổi tác vụ (task / 작업) đang chạy, ví dụ vì luồng thực thi (thread / 스레드) bị khối (block / 블록) hoặc hết thời gian (time / 시간) slice.

Ví dụ:

```text
read() dữ liệu đã có sẵn trong page cache
→ vào kernel
→ copy dữ liệu
→ quay lại user space
→ có thể không cần chuyển sang task khác
```

Ngược lại:

```text
read() cần chờ disk
→ vào kernel
→ task chuyển sang sleep
→ scheduler chạy task khác
→ I/O hoàn tất
→ task được đánh thức
→ sau đó mới tiếp tục
```

> **Nối mạch:** Trong **Vòng đời lời gọi hệ thống: từ người dùng (user / 사용자) không gian (space / 공간) vào kernel và quay trở lại**, **Blocking và sleeping trong lời gọi hệ thống (system call / 시스템 호출)** nối từ **Lời gọi hệ thống (system call / 시스템 호출) không đồng nghĩa ngữ cảnh (context / 맥락) switch** sang **Bản sao (copy / 복사) dữ liệu giữa người dùng (user / 사용자) không gian (space / 공간) và kernel**, vì cơ chế trước tạo đầu vào cho bước sau.

## Blocking và sleeping trong lời gọi hệ thống (system call / 시스템 호출)

Một lời gọi hệ thống (system call / 시스템 호출) có thể hoàn tất ngay hoặc phải chờ tài nguyên.

Ví dụ `read()` trên tệp (file / 파일) thường có thể trả nhanh nếu dữ liệu đã ở page bộ nhớ đệm (cache / 캐시). Nhưng `read()` trên socket không có dữ liệu có thể làm luồng thực thi (thread / 스레드) ngủ nếu socket ở blocking chế độ (mode / 모드).

Kernel thường không “quay CPU vòng tròn” vô ích. tác vụ (task / 작업) được đưa vào trạng thái chờ, rời run hàng đợi (queue / 큐) và chỉ được đánh thức khi điều kiện cần thiết xảy ra.

Đây là nền tảng để hiểu tại sao một tiến trình có hàng trăm luồng thực thi (thread / 스레드) nhưng CPU không nhất thiết 100%.

> **Nối mạch:** Ở chặng này của **Vòng đời lời gọi hệ thống: từ người dùng (user / 사용자) không gian (space / 공간) vào kernel và quay trở lại**, **Blocking và sleeping trong lời gọi hệ thống (system call / 시스템 호출)** đặt vấn đề; **Bản sao (copy / 복사) dữ liệu giữa người dùng (user / 사용자) không gian (space / 공간) và kernel** đối chiếu bằng chứng, rồi **errno thực sự đến từ đâu?** mở rộng hệ quả hoặc giới hạn liên quan.

## Bản sao (copy / 복사) dữ liệu giữa người dùng (user / 사용자) không gian (space / 공간) và kernel

Kernel không thể tin địa chỉ bộ nhớ do người dùng (user / 사용자) không gian (space / 공간) cung cấp. Một con trỏ có thể không hợp lệ hoặc trỏ tới vùng không được phép.

Các cơ chế như `copy_from_user()` và `copy_to_user()` tồn tại để kiểm tra và sao chép dữ liệu qua ranh giới này theo cách an toàn.

Đây là lý do một lời gọi hệ thống (system call / 시스템 호출) có thể thất bại với `EFAULT` khi vùng nhớ người dùng không hợp lệ.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Vòng đời lời gọi hệ thống: từ người dùng (user / 사용자) không gian (space / 공간) vào kernel và quay trở lại**, **Bản sao (copy / 복사) dữ liệu giữa người dùng (user / 사용자) không gian (space / 공간) và kernel** đặt vấn đề; **errno thực sự đến từ đâu?** đối chiếu bằng chứng, rồi **Lời gọi hệ thống (system call / 시스템 호출) bảng (table / 테이블) và ABI** mở rộng hệ quả hoặc giới hạn liên quan.

## `errno` thực sự đến từ đâu?

Kernel thường trả mã lỗi âm theo quy ước nội bộ. Wrapper ở libc chuyển trạng thái đó thành:

```c
-1
```

và đặt biến thread-local `errno` tương ứng.

Ví dụ:

```c
int fd = open("/missing", O_RDONLY);
if (fd == -1) {
    perror("open");
}
```

`perror()` đọc `errno` và in thông báo dễ hiểu hơn.

Trong `strace` có thể thấy trực tiếp:

```text
openat(..., "/missing", ...) = -1 ENOENT (No such file or directory)
```

> **Nối mạch:** Trong **Vòng đời lời gọi hệ thống: từ người dùng (user / 사용자) không gian (space / 공간) vào kernel và quay trở lại**, **Lời gọi hệ thống (system call / 시스템 호출) bảng (table / 테이블) và ABI** nối từ **errno thực sự đến từ đâu?** sang **vDSO: khi người dùng (user / 사용자) không gian (space / 공간) tránh lời gọi hệ thống (system call / 시스템 호출) thật**, vì cơ chế trước tạo đầu vào cho bước sau.

## Lời gọi hệ thống (system call / 시스템 호출) bảng (table / 테이블) và ABI

Kernel có bảng ánh xạ số lời gọi hệ thống (system call / 시스템 호출) tới hàm xử lý tương ứng. ABI của lời gọi hệ thống (system call / 시스템 호출) cần ổn định vì user-space nhị phân (binary / 이진) đã biên dịch phải tiếp tục chạy qua nhiều phiên bản kernel.

Điều này giải thích tại sao Linux rất thận trọng với backward tính tương thích (compatibility / 호환성) ở ranh giới người dùng (user / 사용자) không gian (space / 공간)/kernel.

Một ứng dụng (application / 애플리케이션) nhị phân (binary / 이진) cũ có thể tiếp tục chạy trên kernel mới miễn ABI cần thiết vẫn được hỗ trợ, dù hiện thực (implementation / 구현) nội bộ kernel đã thay đổi nhiều.

> **Nối mạch:** Ở chặng này của **Vòng đời lời gọi hệ thống: từ người dùng (user / 사용자) không gian (space / 공간) vào kernel và quay trở lại**, **vDSO: khi người dùng (user / 사용자) không gian (space / 공간) tránh lời gọi hệ thống (system call / 시스템 호출) thật** nối từ **Lời gọi hệ thống (system call / 시스템 호출) bảng (table / 테이블) và ABI** sang **Chi phí của lời gọi hệ thống (system call / 시스템 호출)**, vì cơ chế trước tạo đầu vào cho bước sau.

## `vDSO`: khi người dùng (user / 사용자) không gian (space / 공간) tránh lời gọi hệ thống (system call / 시스템 호출) thật

Một số thao tác như đọc thời gian được gọi rất thường xuyên. Nếu mỗi lần đều phải chuyển vào kernel, chi phí sẽ đáng kể.

Linux có thể cung cấp **virtual động (dynamic / 동적) dùng chung (shared / 공유) đối tượng (object / 객체) (vDSO)** ánh xạ một số lô-gic (logic / 논리) và dữ liệu vào người dùng (user / 사용자) không gian (space / 공간). Nhờ đó hàm như `clock_gettime()` trong nhiều trường hợp có thể lấy dữ liệu mà không cần lời gọi hệ thống (system call / 시스템 호출) thật.

Có thể quan sát ánh xạ (mapping / 매핑):

```bash
cat /proc/self/maps | grep vdso
```

Điểm quan trọng: không phải mọi API trông giống hệ thống (system / 시스템) API đều nhất thiết gây chế độ (mode / 모드) chuyển tiếp (transition / 전이).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Vòng đời lời gọi hệ thống: từ người dùng (user / 사용자) không gian (space / 공간) vào kernel và quay trở lại**, **Chi phí của lời gọi hệ thống (system call / 시스템 호출)** nối từ **vDSO: khi người dùng (user / 사용자) không gian (space / 공간) tránh lời gọi hệ thống (system call / 시스템 호출) thật** sang **Batch và amortization**, vì cơ chế trước tạo đầu vào cho bước sau.

## Chi phí của lời gọi hệ thống (system call / 시스템 호출)

Lời gọi hệ thống (system call / 시스템 호출) có chi phí do:

- chuyển privilege mức (level / 수준);
- kiểm tra đối số;
- chính sách (policy / 정책)/bảo mật (security / 보안) checks;
- bộ nhớ đệm (cache / 캐시)/TLB effects;
- bản sao (copy / 복사) dữ liệu giữa người dùng (user / 사용자)/kernel;
- có thể khối (block / 블록) hoặc gây scheduling.

Nhưng không nên suy diễn rằng “lời gọi hệ thống (system call / 시스템 호출) luôn chậm”. Chi phí thật phụ thuộc loại thao tác (operation / 연산) và tải công việc (workload / 워크로드).

Một `getpid()` hoặc `clock_gettime()` khác hoàn toàn `fsync()` lên lưu trữ (storage / 저장소) chậm.

> **Nối mạch:** Trong **Vòng đời lời gọi hệ thống: từ người dùng (user / 사용자) không gian (space / 공간) vào kernel và quay trở lại**, **Batch và amortization** nối từ **Chi phí của lời gọi hệ thống (system call / 시스템 호출)** sang **Lời gọi hệ thống (system call / 시스템 호출) và bảo mật**, vì cơ chế trước tạo đầu vào cho bước sau.

## Batch và amortization

Vì ranh giới kernel có overhead, nhiều API cố giảm số lần lời gọi hệ thống (system call / 시스템 호출) hoặc gom nhiều thao tác.

Ví dụ:

- buffered I/O gom nhiều lần ghi nhỏ;
- `readv()`/`writev()` xử lý nhiều buffer;
- `sendmmsg()`/`recvmmsg()` xử lý nhiều message;
- `io_uring` giảm một số vòng submit/completion theo mô hình hàng đợi (queue / 큐).

Tuy nhiên tối ưu kiểu này chỉ có ý nghĩa khi profiling cho thấy lời gọi hệ thống (system call / 시스템 호출) overhead thực sự là bottleneck.

> **Nối mạch:** Ở chặng này của **Vòng đời lời gọi hệ thống: từ người dùng (user / 사용자) không gian (space / 공간) vào kernel và quay trở lại**, **Lời gọi hệ thống (system call / 시스템 호출) và bảo mật** nối từ **Batch và amortization** sang **Gỡ lỗi (debug / 디버그) bằng strace**, vì cơ chế trước tạo đầu vào cho bước sau.

## Lời gọi hệ thống (system call / 시스템 호출) và bảo mật

Ranh giới lời gọi hệ thống (system call / 시스템 호출) là nơi kernel áp dụng nhiều kiểm tra:

```text
credentials
+ file permission / ACL
+ capabilities
+ LSM như SELinux/AppArmor
+ seccomp
+ namespace/cgroup context
→ allow hoặc deny
```

Seccomp có thể giới hạn tập lời gọi hệ thống (system call / 시스템 호출) mà tiến trình được phép thực hiện. bộ chứa (container / 컨테이너) thời gian chạy (runtime / 런타임) thường dùng cơ chế này để giảm bề mặt tấn công.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Vòng đời lời gọi hệ thống: từ người dùng (user / 사용자) không gian (space / 공간) vào kernel và quay trở lại**, **Gỡ lỗi (debug / 디버그) bằng strace** nối từ **Lời gọi hệ thống (system call / 시스템 호출) và bảo mật** sang **seccomp và lời gọi hệ thống (system call / 시스템 호출) surface**, vì cơ chế trước tạo đầu vào cho bước sau.

## Gỡ lỗi (debug / 디버그) bằng `strace`

`strace` quan sát lời gọi hệ thống (system call / 시스템 호출) nên rất mạnh khi ứng dụng “nói ít hơn những gì kernel thấy”.

Ví dụ chương trình treo:

```bash
sudo strace -tt -T -p <PID>
```

Nếu liên tục thấy:

```text
futex(...)
```

thì luồng thực thi (thread / 스레드) có thể đang chờ synchronization.

Nếu thấy:

```text
connect(...)
```

mất nhiều giây rồi hết thời gian chờ (timeout / 타임아웃), trọng tâm điều tra chuyển sang mạng (network / 네트워크)/phụ thuộc (dependency / 의존성).

Nếu thấy lặp:

```text
openat(..., "/missing/config", ...) = -1 ENOENT
```

thì vấn đề có thể đơn giản là đường dẫn (path / 경로)/cấu hình (config / 설정).

> **Nối mạch:** Trong **Vòng đời lời gọi hệ thống: từ người dùng (user / 사용자) không gian (space / 공간) vào kernel và quay trở lại**, **seccomp và lời gọi hệ thống (system call / 시스템 호출) surface** nối từ **Gỡ lỗi (debug / 디버그) bằng strace** sang **Tín hiệu (signal / 신호) có thể ngắt lời gọi hệ thống (system call / 시스템 호출)**, vì cơ chế trước tạo đầu vào cho bước sau.

## `seccomp` và lời gọi hệ thống (system call / 시스템 호출) surface

Một tiến trình có thể bị chặn lời gọi hệ thống (system call / 시스템 호출) dù UID và tệp (file / 파일) permission có vẻ đúng. Seccomp filter có thể trả lỗi hoặc giết tác vụ (task / 작업) tùy chính sách (policy / 정책).

Bộ chứa (container / 컨테이너) thường áp default seccomp profile. Vì vậy tình huống “nhị phân (binary / 이진) chạy trên host nhưng không chạy trong bộ chứa (container / 컨테이너)” có thể liên quan lời gọi hệ thống (system call / 시스템 호출) chính sách (policy / 정책), không chỉ filesystem.

> **Nối mạch:** Ở chặng này của **Vòng đời lời gọi hệ thống: từ người dùng (user / 사용자) không gian (space / 공간) vào kernel và quay trở lại**, **Tín hiệu (signal / 신호) có thể ngắt lời gọi hệ thống (system call / 시스템 호출)** nối từ **seccomp và lời gọi hệ thống (system call / 시스템 호출) surface** sang **Lời gọi hệ thống (system call / 시스템 호출) cancellation và hết thời gian chờ (timeout / 타임아웃)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Tín hiệu (signal / 신호) có thể ngắt lời gọi hệ thống (system call / 시스템 호출)

Một lời gọi hệ thống (system call / 시스템 호출) đang khối (block / 블록) có thể bị tín hiệu (signal / 신호) làm gián đoạn. Một số lời gọi trả `EINTR`, một số có thể được tự động restart tùy tín hiệu (signal / 신호) handler và flags như `SA_RESTART`.

Đây là lý do mã (code / 코드) hệ thống cần xử lý thử lại (retry / 재시도) đúng cách thay vì giả định mọi `read()` hoặc `wait()` chỉ thất bại vì lỗi vĩnh viễn.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Vòng đời lời gọi hệ thống: từ người dùng (user / 사용자) không gian (space / 공간) vào kernel và quay trở lại**, **Lời gọi hệ thống (system call / 시스템 호출) cancellation và hết thời gian chờ (timeout / 타임아웃)** nối từ **Tín hiệu (signal / 신호) có thể ngắt lời gọi hệ thống (system call / 시스템 호출)** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Lời gọi hệ thống (system call / 시스템 호출) cancellation và hết thời gian chờ (timeout / 타임아웃)

Nhiều lời gọi hệ thống (system call / 시스템 호출) blocking không có hết thời gian chờ (timeout / 타임아웃) nội tại. Ứng dụng thường kết hợp non-blocking chế độ (mode / 모드), `poll`/`epoll`, timer hoặc API tầng cao để tránh khối (block / 블록) vô hạn.

Ví dụ socket có thể dùng:

```c
setsockopt(..., SO_RCVTIMEO, ...)
```

hoặc ứng dụng (application / 애플리케이션) quản lý hết thời gian chờ (timeout / 타임아웃) ở vòng lặp sự kiện (event loop / 이벤트 루프).

> **Nối mạch:** Trong **Vòng đời lời gọi hệ thống: từ người dùng (user / 사용자) không gian (space / 공간) vào kernel và quay trở lại**, **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Lời gọi hệ thống (system call / 시스템 호출) cancellation và hết thời gian chờ (timeout / 타임아웃)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những hiểu lầm phổ biến** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

Hãy coi lời gọi hệ thống (system call / 시스템 호출) như một **yêu cầu (request / 요청) có hợp đồng rõ ràng gửi tới kernel**:

```text
user-space intent
    ↓
ABI + arguments
    ↓
privilege transition
    ↓
validation / policy / resource lookup
    ↓
implementation
    ↓
result hoặc errno
    ↓
resume user-space execution
```

Điểm cần quan sát không chỉ là “lời gọi hệ thống (system call / 시스템 호출) nào được gọi”, mà còn là nó **khối (block / 블록) ở đâu, chờ tài nguyên gì, chịu chính sách (policy / 정책) nào và có gây scheduling hay không**.

> **Nối mạch:** Ở chặng này của **Vòng đời lời gọi hệ thống: từ người dùng (user / 사용자) không gian (space / 공간) vào kernel và quay trở lại**, **Những hiểu lầm phổ biến** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối kiến thức** mở rộng hệ quả hoặc giới hạn liên quan.

## Những hiểu lầm phổ biến

**“Gọi lời gọi hệ thống (system call / 시스템 호출) luôn tạo ngữ cảnh (context / 맥락) switch.”** Không. chế độ (mode / 모드) switch và tác vụ (task / 작업) ngữ cảnh (context / 맥락) switch là hai việc khác nhau.

**“thư viện (library / 라이브러리) lời gọi (call / 호출) và lời gọi hệ thống (system call / 시스템 호출) giống nhau.”** Wrapper có thể không gọi lời gọi hệ thống (system call / 시스템 호출) hoặc gọi lời gọi hệ thống (system call / 시스템 호출) khác với tên API.

**“lời gọi hệ thống (system call / 시스템 호출) thành công nghĩa dữ liệu đã xuống thiết bị.”** Với buffered I/O, `write()` thành công chưa đồng nghĩa durability; cần hiểu `fsync()` và lưu trữ (storage / 저장소) ngăn xếp (stack / 스택).

**“Ứng dụng treo mà không log thì kernel không biết gì.”** `strace`, `/proc`, scheduler trạng thái (state / 상태) và socket trạng thái (state / 상태) vẫn có thể cung cấp bằng chứng.

**“Tối ưu bằng cách giảm lời gọi hệ thống (system call / 시스템 호출) luôn có lợi.”** Chỉ tối ưu khi đo lường cho thấy đây là bottleneck thật.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Vòng đời lời gọi hệ thống: từ người dùng (user / 사용자) không gian (space / 공간) vào kernel và quay trở lại**, **Kết nối kiến thức** nối từ **Những hiểu lầm phổ biến** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Kết nối kiến thức

Lời gọi hệ thống (system call / 시스템 호출) là điểm nối của gần như toàn bộ thư viện Linux: tệp (file / 파일) descriptor, VFS, tiến trình (process / 프로세스), socket, bộ nhớ (memory / 메모리) ánh xạ (mapping / 매핑), tín hiệu (signal / 신호), seccomp và tracing. Đọc tiếp [Tiến trình, luồng, tín hiệu và tác vụ](../04_process/processes_threads_signals_jobs.md), [VFS, page cache và writeback](../01_filesystem/vfs_page_cache_writeback.md) và [Quan sát bằng strace/perf/eBPF](../09_production/observability_tracing_strace_perf.md).

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
