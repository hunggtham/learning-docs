# Kernel, không gian người dùng và lời gọi hệ thống

Một chương trình có thể thực hiện phép tính trong các thanh ghi CPU và vùng bộ nhớ đã được cấp mà gần như không cần kernel can thiệp. Nhưng ngay khi nó muốn mở tệp, tạo tiến trình, gửi gói tin mạng, ánh xạ thêm bộ nhớ hoặc truy cập tài nguyên hệ thống, nó phải tương tác với hệ điều hành. Ranh giới giữa ứng dụng và kernel là nền tảng để hiểu cả hiệu năng (performance) lẫn bảo mật (security) của Linux.

## Vì sao phải có ranh giới đặc quyền?

Giả sử mọi chương trình đều có thể ghi trực tiếp vào bất kỳ địa chỉ RAM nào hoặc điều khiển bộ điều khiển đĩa. Một lỗi trong trình soạn thảo văn bản có thể ghi đè bộ nhớ của cơ sở dữ liệu. Mã độc cũng không cần nâng đặc quyền vì ngay từ đầu đã có toàn quyền. Một hệ thống nhiều người dùng gần như không thể vận hành an toàn theo cách đó.

CPU vì vậy hỗ trợ các mức đặc quyền. Linux dùng cơ chế phần cứng này để tách **không gian hạt nhân (kernel space / 커널 공간)** khỏi **không gian người dùng (user space / 사용자 공간)**. Tiến trình người dùng không thể tùy ý thực thi chỉ thị đặc quyền hoặc truy cập bộ nhớ của kernel. Kernel đóng vai trò **bộ quản lý tài nguyên (resource manager)** và điểm thực thi chính sách.

Bảo mật ở đây không chỉ là mật khẩu. Sự cô lập (isolation) bắt đầu từ đặc quyền phần cứng và cơ chế bảo vệ bộ nhớ.

## Lời gọi hệ thống là gì?

**Lời gọi hệ thống (system call / 시스템 호출)** là điểm vào được kiểm soát để chương trình trong không gian người dùng yêu cầu kernel thực hiện một thao tác. Các lời gọi quen thuộc gồm `openat`, `read`, `write`, `close`, `fork`/`clone`, `execve`, `mmap`, `socket`, `connect` và `accept`.

Khi shell chạy:

```bash
cat /etc/os-release
```

`cat` phải mở đường dẫn, nhận bộ mô tả tệp, đọc các byte rồi ghi chúng ra đầu ra chuẩn. Người dùng chỉ nhìn thấy một câu lệnh đơn giản, nhưng phía dưới là một chuỗi tương tác qua ranh giới giữa chương trình và kernel.

Có thể quan sát trực tiếp bằng `strace` nếu máy chủ có công cụ này:

```bash
strace -e openat,read,write,close cat /etc/os-release
```

`strace` hữu ích vì nó cho thấy ứng dụng **đã yêu cầu kernel điều gì và kernel trả về kết quả gì**, thay vì chỉ nhìn thông báo lỗi ở tầng framework.

## Lời gọi thư viện không đồng nghĩa với lời gọi hệ thống

Ứng dụng thường không gọi system call bằng assembly trực tiếp. Nó gọi API của môi trường chạy hoặc thư viện. Chương trình C có thể gọi `printf()`, Java gọi `Files.readString()`, Python gọi `open()`. Môi trường chạy hoặc thư viện sau đó sử dụng một hoặc nhiều system call thích hợp.

Do đó quan hệ không phải lúc nào cũng là 1:1. Một lời gọi thư viện có thể chỉ xử lý bộ đệm (buffer) trong không gian người dùng mà chưa đi vào kernel ngay; ngược lại, một API cấp cao có thể tạo ra nhiều system call.

Điều này quan trọng khi tối ưu hiệu năng: gọi nhiều hàm không tự động có nghĩa là hệ thống thực hiện nhiều lần chuyển ngữ cảnh, và một lần gọi API cấp cao cũng không nhất thiết tương ứng với đúng một system call.

## Chuyển ngữ cảnh và chuyển chế độ

Khi CPU chuyển từ chế độ người dùng sang chế độ kernel để xử lý system call, mức đặc quyền thay đổi. Tuy nhiên không nên đồng nhất mọi system call với việc đổi sang một tiến trình khác.

**Chuyển ngữ cảnh (context switch)** thường nói đến việc CPU chuyển ngữ cảnh thực thi giữa các luồng hoặc tiến trình, cần lưu và phục hồi trạng thái và có thể ảnh hưởng bộ nhớ đệm CPU. **Chuyển chế độ (mode switch)** chỉ nói đến việc thay đổi mức đặc quyền. Hai khái niệm có liên quan nhưng không giống nhau.

## Mã lỗi và `errno`

Thao tác của kernel có thể thất bại vì trạng thái thực tế không đáp ứng yêu cầu. Tệp có thể không tồn tại, tiến trình không đủ quyền, cổng mạng không có tiến trình lắng nghe hoặc giới hạn tài nguyên đã bị chạm. Trong lập trình Unix/POSIX, system call thường báo thất bại và thư viện cung cấp nguyên nhân qua `errno`.

Một số tên thường gặp:

- `ENOENT`: thành phần hoặc đường dẫn cần thiết không tồn tại;
- `EACCES`: chính sách quyền truy cập từ chối thao tác;
- `ECONNREFUSED`: kết nối tới điểm cuối nhưng không có dịch vụ chấp nhận theo điều kiện hiện tại;
- `ENOMEM`: hệ thống không thể đáp ứng yêu cầu bộ nhớ.

Điều quan trọng không phải học thuộc số `errno`, mà là đọc lỗi như một bằng chứng về lớp nào trong hệ thống đang từ chối hoặc không thể thực hiện yêu cầu.

## `/proc` và `/sys`: cửa sổ nhìn vào trạng thái kernel

Linux trình bày nhiều trạng thái khi đang chạy thông qua các **hệ thống tệp giả (pseudo-filesystem)**. `/proc` không phải thư mục dữ liệu thông thường nằm trên đĩa; nó trình bày thông tin về tiến trình và kernel dưới giao diện giống tệp.

Ví dụ:

```bash
cat /proc/$$/status
cat /proc/$$/limits
ls -l /proc/$$/fd
```

`$$` trong shell là `PID` của shell hiện tại. Qua `/proc`, ta có thể xem danh tính, thông tin bộ nhớ, giới hạn tài nguyên và các bộ mô tả tệp đang mở.

`/sys` hay `sysfs` trình bày mô hình của thiết bị, trình điều khiển và các đối tượng kernel. Đây là một ví dụ mạnh cho triết lý đưa trạng thái hệ thống vào một vùng tên phân cấp để các công cụ không gian người dùng có thể quan sát và thao tác tương đối thống nhất.

## Mô-đun kernel và trình điều khiển

Kernel cần mã để điều khiển phần cứng và cung cấp các hệ thống con. Một phần được biên dịch trực tiếp vào kernel; phần khác có thể tồn tại dưới dạng **mô-đun kernel có thể nạp (loadable kernel module / 커널 모듈)**.

```bash
lsmod
modinfo <module>
```

Không nên nạp hoặc gỡ mô-đun trên production chỉ để thử nghiệm. Mô-đun chạy trong ngữ cảnh kernel, vì vậy một lỗi ở đây có phạm vi ảnh hưởng khác hẳn lỗi của một tiến trình thông thường.

## Lời gọi hệ thống như một ranh giới bảo mật

Một tiến trình không thể tự quyết định rằng nó được đọc `/etc/shadow`. Nó yêu cầu kernel mở tệp; kernel kiểm tra thông tin xác thực, quyền của hệ thống tệp và có thể áp dụng thêm chính sách như SELinux hoặc AppArmor trước khi cho phép.

Tương tự, container thông thường không tạo kernel riêng. Tiến trình trong container vẫn gọi system call vào kernel Linux của máy chủ, nhưng kernel nhìn chúng qua các ràng buộc khác về vùng tên (namespace), nhóm điều khiển (cgroup) và bảo mật. Xem thêm [Linux và container](../09_production/linux_containers.md).

## Liên hệ với hiệu năng

Ứng dụng thiên về vào/ra (I/O-heavy) thường dành nhiều thời gian chờ kernel, phần cứng hoặc mạng hơn là thực thi phép tính của chính ứng dụng. Khối lượng công việc thiên về CPU (CPU-heavy) lại chủ yếu dùng thời gian để tính toán trong không gian người dùng. Các công cụ như `top`, `pidstat`, `vmstat` giúp phân tách một phần thời gian CPU thành `user`, `system`, `idle`, `iowait` để hỗ trợ phân tích.

Nếu `%system` tăng mạnh, không nên kết luận ngay rằng kernel "bị lỗi". Có thể ứng dụng đang tạo rất nhiều system call hoặc tải mạng/hệ thống tệp lớn. Cần đối chiếu với tiến trình, I/O và hành vi system call trước khi kết luận.

## Mô hình tư duy (Mental Model)

Hãy coi kernel như một **bộ môi giới tài nguyên đáng tin cậy (trusted resource broker)**. Tiến trình người dùng không tự lấy tài nguyên; nó gửi yêu cầu qua giao diện được kiểm soát. Kernel kiểm tra danh tính, trạng thái, giới hạn và mức tài nguyên còn khả dụng rồi thực hiện hoặc từ chối.

Mô hình này giúp đọc lỗi theo hướng: yêu cầu nào đã được gửi? đối tượng nào được yêu cầu? chính sách hoặc trạng thái nào của kernel có thể khiến yêu cầu thất bại?

## Những hiểu lầm phổ biến (Common Misconceptions)

**"System call là gọi một câu lệnh Linux."** Không. `ls` là chương trình trong không gian người dùng; bên trong nó mới sử dụng các system call.

**"Vào kernel mode nghĩa là đổi tiến trình."** Không nhất thiết. Chuyển chế độ và chuyển ngữ cảnh do bộ lập lịch thực hiện là hai khái niệm khác nhau.

**"Container có kernel riêng như máy ảo."** Container Linux thông thường chia sẻ kernel của máy chủ; sự cô lập chủ yếu dựa trên các cơ chế kernel như namespace và cgroup.

**"Root có thể đọc mọi thứ bất kể cơ chế nào."** `root` có thể bỏ qua nhiều quyền truy cập tùy ý (discretionary permission), nhưng vẫn có thể bị giới hạn bởi namespace, capability, SELinux/AppArmor, trạng thái bất biến, lưu trữ mã hóa hoặc những ràng buộc khác của kernel.

## Thực hành quan sát

Không cần viết mã kernel để hiểu ranh giới này. Có thể bắt đầu bằng:

```bash
strace -f -o /tmp/trace.txt curl -s http://127.0.0.1:8080/health
less /tmp/trace.txt
```

`-f` yêu cầu `strace` theo dõi thêm tiến trình hoặc luồng con khi phù hợp; `-o` ghi kết quả ra tệp. Hãy tìm `socket`, `connect`, `read`, `write`, `close`. Một yêu cầu HTTP ở tầng cao cuối cùng vẫn được xây trên các cơ chế nền tảng của kernel.

Tiếp theo nên đọc [Hệ thống tệp, đường dẫn, inode và liên kết](../01_filesystem/filesystem_paths_inodes_links.md) và [Tiến trình, luồng, tín hiệu và tác vụ](../04_process/processes_threads_signals_jobs.md), vì đối tượng hệ thống tệp và tiến trình là hai nhóm lớp trừu tượng lớn mà system call thao tác.