# Tiến trình, luồng, tín hiệu và tác vụ

Chương trình nằm trên đĩa chỉ là mã và dữ liệu tĩnh. Khi được thực thi, Linux tạo một **ngữ cảnh thực thi khi đang chạy (runtime execution context)** gồm không gian địa chỉ, thông tin xác thực, các bộ mô tả tệp đang mở, trạng thái lập lịch và nhiều metadata khác. Đối tượng khi đang chạy đó là **tiến trình (process / 프로세스)**. Hiểu mô hình tiến trình là điều kiện để sử dụng đúng `ps`, `kill`, `top`, `systemctl` và các công cụ JVM.

## Chương trình khác tiến trình

Một tệp `app.jar` có thể được chạy nhiều lần và tạo ra nhiều tiến trình JVM. Ngược lại, một tiến trình có thể dùng `exec` để thay chương trình đang thực thi trong cùng ngữ cảnh tiến trình. Vì vậy **ứng dụng (application)** là khái niệm ở mức nghiệp vụ hoặc triển khai, còn **process** là lớp trừu tượng khi đang chạy do kernel quản lý.

```bash
pgrep -af java
```

`-f` khớp với toàn bộ dòng lệnh, còn `-a` hiển thị dòng lệnh đầy đủ. Cách này thường rõ hơn:

```bash
ps -ef | grep java
```

vì cách thứ hai có thể tự bắt cả tiến trình `grep` và mẫu tìm kiếm thường rộng hơn mức cần thiết.

## PID và PPID

Mỗi tiến trình có **PID (Process ID)** tại một thời điểm và có quan hệ với tiến trình cha thông qua **PPID (Parent Process ID)**.

```bash
ps -p 1234 -o pid,ppid,user,lstart,etime,cmd
pstree -p
```

`PID` không phải danh tính vĩnh viễn. Sau khi tiến trình kết thúc, kernel có thể tái sử dụng số PID đó. Vì vậy trước khi `kill PID` trên production, nên xác minh PID hiện vẫn thuộc đúng tiến trình cần xử lý.

## Tạo tiến trình: `fork`/`clone` và `exec`

Mô hình Unix truyền thống thường được giải thích theo hai bước: tạo một ngữ cảnh thực thi dựa trên tiến trình cha bằng `fork`, sau đó thay ảnh chương trình bằng chương trình mới qua `exec`. Linux hiện đại có `clone`, `clone3` và nhiều chi tiết phức tạp hơn, nhưng mô hình **tạo ngữ cảnh rồi thực thi chương trình mới** vẫn rất hữu ích để suy luận.

Khi shell chạy một câu lệnh bên ngoài, nó phải tạo ngữ cảnh tiến trình, thiết lập môi trường và file descriptor rồi thực thi chương trình đích.

## Luồng là gì?

Các **luồng (thread / 스레드)** trong cùng tiến trình thường chia sẻ không gian địa chỉ và nhiều tài nguyên, nhưng mỗi luồng có trạng thái thực thi và thực thể lập lịch riêng. Một ứng dụng web Java có thể chỉ là một process nhưng chứa hàng trăm thread.

```bash
ps -p <PID> -o pid,nlwp,%cpu,%mem,cmd
```

`NLWP` phản ánh số **tiến trình nhẹ (lightweight process)** hoặc số luồng theo cách Linux báo cáo.

Khi một tiến trình Java dùng CPU cao, số CPU ở mức tiến trình chỉ cho biết JVM đang tiêu thụ CPU. Muốn tìm đường mã gây tải, cần quan sát từng luồng và lấy **bản chụp luồng (thread dump)**:

```bash
pidstat -t -p <PID> 1
jcmd <PID> Thread.print
```

## Bộ lập lịch và các trạng thái tiến trình

Tiến trình hoặc luồng không phải lúc nào cũng "đang chạy" dù vẫn tồn tại. Nó có thể sẵn sàng chạy, đang ngủ chờ sự kiện, bị dừng hoặc ở trạng thái zombie. `ps` và `top` biểu diễn trạng thái bằng các mã như `R`, `S`, `D`, `T`, `Z`.

`D` thường biểu thị trạng thái ngủ không thể ngắt (uninterruptible sleep), hay gặp khi đang chờ một đường I/O trong kernel. Nhiều tác vụ ở `D` cùng độ trễ lưu trữ cao có thể làm tải trung bình (load average) tăng dù CPU chưa dùng hết.

`Z` là **tiến trình zombie**: tiến trình con đã kết thúc nhưng tiến trình cha chưa thu nhận trạng thái kết thúc. Zombie không tiếp tục chạy mã nghiệp vụ nhưng vẫn giữ một mục trong bảng tiến trình. Gửi `kill` trực tiếp cho zombie không xử lý nguyên nhân gốc; cần kiểm tra tiến trình cha và cơ chế thu hồi trạng thái (reaping).

## Tín hiệu: thông báo bất đồng bộ cho tiến trình

**Tín hiệu (signal / 시그널)** là cơ chế kernel dùng để gửi sự kiện hoặc yêu cầu điều khiển tới tiến trình. Tên câu lệnh `kill` dễ gây hiểu nhầm: mặc định nó **gửi tín hiệu**, không đồng nghĩa với việc cưỡng bức tiêu diệt tiến trình.

```bash
kill 1234
```

mặc định gửi `SIGTERM` (15), yêu cầu tiến trình kết thúc theo cách có kiểm soát và cho ứng dụng cơ hội xử lý dọn dẹp nếu có bộ xử lý tín hiệu phù hợp.

```bash
kill -9 1234
```

gửi `SIGKILL`. Kernel không cho tiến trình bắt hoặc bỏ qua `SIGKILL`, vì vậy tiến trình không có cơ hội chạy mã dọn dẹp trước khi bị dừng.

Trong vận hành thực tế, thứ tự hợp lý thường là: `SIGTERM` → chờ và xác minh → `SIGKILL` chỉ khi thật sự cần.

## `SIGTERM`, `SIGKILL`, `SIGHUP`, `SIGINT`

`SIGTERM` thường được dùng cho yêu cầu kết thúc mềm (graceful termination). `SIGKILL` là cưỡng bức kết thúc. `SIGINT` thường được terminal gửi khi nhấn `Ctrl+C`. `SIGHUP` có lịch sử liên quan việc terminal bị ngắt kết nối; nhiều daemon dùng nó như quy ước để nạp lại cấu hình, nhưng hành vi cụ thể phụ thuộc từng chương trình.

Không nên giả định `kill -HUP` luôn có nghĩa "reload". Hãy đọc tài liệu của dịch vụ tương ứng.

## Quyền gửi tín hiệu

Một tiến trình không thể tùy ý gửi signal tới mọi tiến trình khác. Kernel kiểm tra thông tin xác thực và capabilities. Đây là mối liên hệ trực tiếp với [Người dùng, nhóm và quyền truy cập](../03_identity/users_groups_permissions.md).

## Tiền cảnh, hậu cảnh và điều khiển tác vụ

Shell tương tác có khái niệm nhóm tiến trình gắn với terminal. Tác vụ tiền cảnh nhận đầu vào terminal và các signal do terminal tạo ra. `&` đưa câu lệnh xuống hậu cảnh:

```bash
sleep 300 &
jobs -l
```

`Ctrl+Z` thường tạm dừng tác vụ tiền cảnh; `bg` tiếp tục ở hậu cảnh; `fg` đưa về tiền cảnh.

Mã tác vụ như `%1` là khái niệm cục bộ của shell, không phải `PID`.

## `nohup` giải quyết gì và không giải quyết gì?

```bash
nohup java -jar app.jar >app.log 2>&1 &
```

`nohup` làm chương trình bỏ qua `SIGHUP` theo cơ chế của công cụ và chuyển hướng đầu ra khi cần. Nó hữu ích với tác vụ đơn giản nhưng không cung cấp quản lý phụ thuộc, chính sách khởi động lại có cấu trúc, kiểm soát tài nguyên hoặc quản lý vòng đời dịch vụ như systemd.

Với dịch vụ chạy lâu dài trên production, xem [Khởi động, systemd và dịch vụ](../05_system/systemd_boot_services.md).

## Môi trường của tiến trình

Mỗi tiến trình nhận một bản chụp **biến môi trường (environment)** từ tiến trình cha khi được tạo. Thay đổi môi trường trong shell sau đó không tự động thay đổi tiến trình đã chạy.

Có thể quan sát tùy theo quyền:

```bash
tr '\0' '\n' < /proc/<PID>/environ
```

Cần thận trọng vì môi trường có thể chứa bí mật như token hoặc mật khẩu. Không nên sao chép hoặc ghi toàn bộ ra nhật ký một cách vô thức.

## Giới hạn tài nguyên

Tiến trình chịu nhiều giới hạn như số tệp mở tối đa, số tiến trình tối đa hoặc bộ nhớ khóa:

```bash
cat /proc/<PID>/limits
ulimit -a
```

Giới hạn `ulimit` của shell tương tác không đảm bảo dịch vụ systemd có cùng giá trị. Systemd có các thiết lập riêng như `LimitNOFILE=`.

## Tiến trình mồ côi và việc thu hồi trạng thái

Tiến trình cha có trách nhiệm thu nhận trạng thái kết thúc của tiến trình con. Khi tiến trình cha biến mất, kernel và hệ thống init xử lý việc gán lại quan hệ cha-con. `PID 1` có vai trò đặc biệt trong vòng đời hệ thống và việc thu hồi tiến trình con.

Trong vùng tên PID của container, vấn đề này càng rõ: tiến trình mang `PID 1` bên trong container cần xử lý signal và thu hồi tiến trình con đúng cách.

## Tiến trình tồn tại không đồng nghĩa dịch vụ khỏe mạnh

Một tiến trình còn tồn tại chỉ chứng minh kernel vẫn duy trì ngữ cảnh thực thi cho nó. Ứng dụng có thể deadlock, cạn thread pool, mất phụ thuộc hoặc chưa gắn socket cần thiết.

Vì vậy quá trình kiểm tra sức khỏe nên tiếp tục qua nhiều lớp:

```text
trạng thái dịch vụ -> tiến trình -> socket lắng nghe -> yêu cầu nội bộ -> phụ thuộc -> đường truyền bên ngoài
```

Ví dụ:

```bash
pgrep -af 'java.*app'
sudo ss -lntp | grep ':8080'
curl -fsS -v http://127.0.0.1:8080/health
```

## Mô hình tư duy (Mental Model)

Tiến trình là **ngữ cảnh khi đang chạy của một chương trình**: không gian địa chỉ + các luồng + thông tin xác thực + file descriptor + môi trường + trạng thái do kernel quản lý. Signal là kênh điều khiển/sự kiện; `PID` chỉ là một mã định danh tạm thời.

Khi gỡ lỗi, đừng chỉ hỏi "Java có chạy không?". Hãy tách thành các câu hỏi cụ thể: tiến trình có tồn tại không? đang ở trạng thái nào? các luồng đang làm gì? file descriptor và socket ra sao? giới hạn tài nguyên thế nào? endpoint của dịch vụ có khỏe không?

## Những hiểu lầm phổ biến (Common Misconceptions)

**"`kill` nghĩa là `kill -9`."** `kill` mặc định gửi `SIGTERM`; `-9` là biện pháp cưỡng bức.

**"PID xác định ứng dụng vĩnh viễn."** PID có thể được tái sử dụng.

**"Zombie đang ăn CPU."** Zombie đã kết thúc; vấn đề là tiến trình cha chưa thu nhận trạng thái và có thể làm tích tụ mục trong bảng tiến trình nếu số lượng lớn.

**"Chạy nền bằng `&` nghĩa là đã có daemon production."** `&` chỉ thay đổi quan hệ điều khiển tác vụ với shell.

**"Tiến trình tồn tại nghĩa là endpoint khỏe."** Cần xác minh thêm ở tầng ứng dụng và mạng.

## Kết nối kiến thức

Vòng đời tiến trình được systemd quản lý ở mức dịch vụ trong [Khởi động, systemd và dịch vụ](../05_system/systemd_boot_services.md). Cách CPU lập lịch và thực thi luồng được mở rộng tại [CPU, lập lịch và hiệu năng](../06_resources/cpu_scheduling_performance.md).