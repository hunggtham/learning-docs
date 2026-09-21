# Java Backend Incident Playbook trên Linux

Khi một Java backend trên Linux gặp sự cố, việc chạy ngẫu nhiên `top`, `tail -f` rồi restart thường chỉ giúp khôi phục tạm thời mà không cho biết nguyên nhân. Một playbook tốt phải nối được ba lớp: **JVM**, **Linux process/resource**, và **network/dependency**.

Chương này không thay thế tài liệu JVM chuyên sâu. Mục tiêu là xây một quy trình thực tế để một backend developer đang SSH vào server có thể đi từ symptom tới evidence có cấu trúc.

## Bắt đầu từ thời điểm và phạm vi ảnh hưởng

Trước mọi command, xác định:

```text
lỗi bắt đầu lúc nào?
bao nhiêu request/user bị ảnh hưởng?
chỉ một instance hay toàn bộ service?
có deployment/config/package change gần đó không?
```

Sau đó ghi lại context của host:

```bash
date '+%F %T %Z %z'
hostname
uptime
```

Timestamp rất quan trọng vì log, metrics và deployment event phải được ghép trên cùng timeline.

## Bước 1: systemd nghĩ service đang ở trạng thái nào?

```bash
systemctl status app --no-pager
systemctl show app -p MainPID -p User -p Group -p ExecStart -p ActiveEnterTimestamp
journalctl -u app -n 300 --no-pager
```

Ba command này cho biết service manager nhìn thấy process nào, chạy bằng identity nào, command thực tế là gì và log gần nhất ra sao.

Nếu service `failed`, đừng restart ngay nếu có thể lấy thêm evidence trước.

## Bước 2: xác định đúng JVM

```bash
pgrep -af 'java.*app'
```

hoặc:

```bash
jps -lv
```

Không dựa vào PID được ghi lại từ incident cũ vì PID có thể được tái sử dụng.

Sau khi xác định PID:

```bash
PID=12345
ps -p "$PID" -o pid,ppid,user,%cpu,%mem,rss,vsz,nlwp,etime,cmd
```

Điều này tạo snapshot ban đầu về CPU, memory, thread count và thời gian chạy.

## Bước 3: process tồn tại có nghĩa application healthy không?

Không. Kiểm tra socket:

```bash
sudo ss -lntp | grep ':8080'
```

Sau đó local health:

```bash
curl -fsS -v http://127.0.0.1:8080/health
```

Có bốn tình huống cơ bản:

```text
không process
process nhưng không listener
listener nhưng health fail/hang
local health tốt nhưng external request fail
```

Mỗi trường hợp dẫn tới nhánh điều tra khác.

## Process biến mất

Nếu JVM không còn tồn tại, cần biết nó tự exit, bị systemd stop, bị OOM kill hay bị signal.

```bash
journalctl -u app --since '30 minutes ago'
journalctl -k --since '30 minutes ago' | grep -i -E 'oom|out of memory|killed process|segfault'
```

Nếu thấy OOM killer, application log có thể chỉ dừng đột ngột mà không có Java exception cuối cùng.

## CPU cao

Trước hết xác nhận CPU high là sustained hay chỉ spike:

```bash
pidstat -p "$PID" 1 10
```

Sau đó xem thread:

```bash
pidstat -t -p "$PID" 1
```

Lấy thread dump:

```bash
jcmd "$PID" Thread.print > /tmp/thread-$(date +%s).txt
```

Một snapshot thread dump đôi khi chưa đủ. Nếu incident kéo dài, lấy 3 dump cách nhau vài giây để xem cùng thread có tiếp tục chạy cùng stack hay không.

```bash
for i in 1 2 3; do
  jcmd "$PID" Thread.print > "/tmp/thread-$i.txt"
  sleep 5
done
```

Nếu một thread dùng CPU cao liên tục và stack lặp lại cùng code path, hypothesis về hot loop/hot method mạnh hơn.

## CPU cao do GC

CPU cao không nhất thiết là business code. JVM có thể dành nhiều thời gian garbage collection.

```bash
jcmd "$PID" GC.heap_info
jstat -gcutil "$PID" 1000 10
```

Tool availability phụ thuộc JDK. Nếu old generation gần full và full GC lặp lại, cần liên hệ heap pressure, allocation rate và GC logs.

Không tăng `-Xmx` ngay khi chưa biết host/container memory limit; heap lớn hơn có thể đẩy process vào cgroup/host OOM.

## Memory tăng

Linux view:

```bash
ps -p "$PID" -o pid,rss,vsz,%mem,etime,cmd
free -h
cat /proc/$PID/status | grep -E 'VmRSS|VmSize|Threads'
```

JVM view:

```bash
jcmd "$PID" GC.heap_info
jcmd "$PID" VM.flags
```

Nếu heap ổn nhưng RSS tăng, hãy nghĩ tới direct buffers, metaspace, thread stacks, native library hoặc mapped memory.

Java process memory không bằng `-Xmx`.

## Nghi memory leak

Không kết luận leak từ một snapshot. Cần trend theo thời gian và workload.

Một heap histogram có thể cung cấp evidence:

```bash
jcmd "$PID" GC.class_histogram > /tmp/histo.txt
```

Heap dump có thể rất lớn và gây I/O/storage pressure, vì vậy không tạo bừa trên filesystem gần đầy. Trước khi dump:

```bash
df -h /tmp
```

Với production, heap dump procedure cần dự tính pause và disk capacity.

## Too many open files

Nếu log có:

```text
Too many open files
```

kiểm tra limit:

```bash
cat /proc/$PID/limits | grep -i 'open files'
```

đếm descriptor:

```bash
ls /proc/$PID/fd | wc -l
```

xem loại resource:

```bash
sudo lsof -p "$PID" | head -100
```

Nếu count tăng liên tục, có thể là file/socket/resource leak. Tăng limit chỉ kéo dài thời gian trước failure nếu lifecycle bug vẫn còn.

## Thread count tăng

```bash
ps -p "$PID" -o pid,nlwp,cmd
```

Nếu thread count tăng không giảm, kiểm tra thread dump để xem pool nào tạo nhiều threads.

Mỗi thread tiêu thụ stack/native resources; hàng nghìn threads có thể gây memory pressure và scheduling overhead ngay cả khi heap không lớn.

## Request hang nhưng CPU thấp

CPU thấp không nghĩa khỏe. Threads có thể đang chờ database, HTTP downstream, lock hoặc connection pool.

Thread dump giúp phân biệt:

```text
RUNNABLE nhưng đang socket read
WAITING/TIMED_WAITING ở pool/lock
BLOCKED trên monitor
```

Sau đó nối với Linux network:

```bash
ss -antp | grep "$PID"
```

và dependency test:

```bash
nc -vz db.internal 5432
curl -v https://downstream.example.com/health
```

Không dùng dependency test có side effect nếu endpoint không an toàn.

## Connection pool exhaustion

Một application có thể healthy process/socket nhưng request chờ vì JDBC hoặc HTTP pool hết connection.

JVM metrics/log thường là evidence tốt nhất, nhưng Linux có thể bổ sung bằng số TCP connections:

```bash
ss -antp | grep ':5432' | wc -l
```

Con số này không đồng nghĩa trực tiếp pool size vì có thể có nhiều process/states, nhưng nó giúp kiểm tra hypothesis.

## Database chậm

Nếu thread dump cho thấy nhiều request chờ JDBC, bước tiếp theo không phải restart JVM ngay. Cần xem DB latency, lock, connection count, slow query và network path.

Từ app host:

```bash
nc -vz db.internal 5432
```

hoặc port phù hợp. TCP success chỉ chứng minh connect layer, không chứng minh query nhanh.

## Network external fail nhưng localhost tốt

Nếu:

```bash
curl -fsS http://127.0.0.1:8080/health
```

thành công nhưng user vẫn lỗi, kiểm tra:

```bash
sudo ss -lntp | grep ':8080'
dig +short api.example.com
curl -v https://api.example.com/health
```

Nếu app bind `127.0.0.1` nhưng proxy kỳ vọng private IP, đó là bind mismatch. Nếu proxy gọi localhost trên cùng host thì bind đó có thể hoàn toàn đúng. Kiến trúc quyết định.

## Disk full và Java

Disk full có thể làm log writer, temp file, upload, database local hoặc JVM diagnostic fail.

```bash
df -h
df -i
sudo du -xhd1 /var 2>/dev/null | sort -hr
sudo lsof +L1
```

Deleted log vẫn được JVM giữ open có thể làm `df` đầy nhưng `du` không thấy.

## I/O chậm

Nếu app latency tăng nhưng CPU thấp và thread dump có file I/O:

```bash
iostat -xz 1 10
pidstat -d -p "$PID" 1
```

Nếu backend dùng network filesystem hoặc cloud volume, local device metrics có thể chưa đủ; xem mount source:

```bash
findmnt /path/to/data
```

## File/config permission

Nếu service startup báo `Permission denied`, xác nhận service user:

```bash
systemctl show app -p User -p Group
```

rồi path:

```bash
namei -l /opt/app/config/application.yml
```

Không `chmod -R 777` để thử. Parent directory traverse, ACL, SELinux/AppArmor hoặc read-only mount cũng có thể là nguyên nhân.

## Chạy tay được nhưng systemd fail

Đây là case rất phổ biến. Interactive shell có environment khác service.

```bash
systemctl show app -p User -p Group -p WorkingDirectory -p Environment -p ExecStart
systemctl cat app
```

Kiểm tra absolute path của Java:

```bash
command -v java
readlink -f "$(command -v java)"
```

Đưa đường dẫn rõ vào `ExecStart` tốt hơn phụ thuộc PATH của SSH shell.

## `jcmd` không attach được

Attach có thể phụ thuộc user, JVM configuration, namespace/container và permission.

Hãy thử bằng cùng service user khi phù hợp:

```bash
sudo -u appuser jcmd "$PID" VM.version
```

Không đổi ownership `/tmp` hoặc process files một cách ngẫu nhiên để làm attach hoạt động.

## Containerized Java

Nếu JVM chạy trong container, host PID và container PID có thể khác; memory limit nằm ở cgroup.

Host `free -h` còn nhiều không loại trừ container OOM.

Cần biết command đang chạy ở host namespace hay container namespace trước khi diễn giải PID, localhost, mount hoặc network.

## Trước restart nên capture gì?

Nếu SLA cho phép vài chục giây thu thập evidence:

```bash
date '+%F %T %Z %z'
systemctl status app --no-pager
journalctl -u app -n 300 --no-pager
ps -p "$PID" -o pid,ppid,user,%cpu,%mem,rss,vsz,nlwp,etime,cmd
jcmd "$PID" Thread.print > /tmp/thread-before-restart.txt
jcmd "$PID" GC.heap_info > /tmp/heap-before-restart.txt
ss -antp > /tmp/ss-before-restart.txt
free -h
df -h
```

Không phải incident nào cũng cần tất cả. Chọn evidence theo symptom và tránh command nặng khi server đang critical.

## Sau restart phải verify gì?

```bash
systemctl status app --no-pager
sudo ss -lntp | grep ':8080'
curl -fsS http://127.0.0.1:8080/health
journalctl -u app -n 100 --no-pager
```

Nếu có endpoint version:

```bash
curl -fsS http://127.0.0.1:8080/version
```

để xác minh artifact mong muốn đang chạy.

## Recovery khác root cause

Restart có thể làm thread pool, connection pool, heap và sockets trở về trạng thái sạch. Điều đó giải thích vì sao service “hết lỗi”, nhưng không cho biết cái gì đã tạo trạng thái xấu.

Sau recovery, dùng evidence đã capture để xác định causal chain.

## Mô hình tư duy (Mental Model)

Một Java service trên Linux có thể nhìn như:

```text
systemd
  ↓
JVM process
  ├─ Java heap / native memory
  ├─ threads / scheduler
  ├─ file descriptors
  ├─ listening sockets
  └─ outbound dependency sockets
       ↓
Linux kernel
       ↓
CPU / memory / storage / network
```

Incident investigation là tìm layer đầu tiên không còn đáp ứng expectation.

## Những hiểu lầm phổ biến

**“Java process còn là app còn khỏe.”** Process có thể deadlock, pool exhaustion hoặc chưa listen.

**“CPU thấp nghĩa app không có vấn đề.”** Nhiều lỗi là waiting/blocking.

**“Xmx 4 GB nghĩa JVM chỉ dùng 4 GB RAM.”** Native/off-heap/thread stack/metaspace còn nằm ngoài heap.

**“Restart hết lỗi nghĩa JVM bug.”** Restart reset rất nhiều state ở app và OS; cần evidence trước restart.

**“Too many open files chỉ cần tăng ulimit.”** Nếu có descriptor leak, tăng limit chỉ trì hoãn lỗi.

## Kết nối kiến thức

Playbook này kết hợp [Processes và Signals](../04_process/processes_threads_signals_jobs.md), [Memory](../06_resources/memory_virtual_memory.md), [CPU](../06_resources/cpu_scheduling_performance.md), [I/O Performance](../06_resources/io_performance.md), [TCP/HTTP/TLS](../07_networking/tcp_http_tls.md), [systemd](../05_system/systemd_boot_services.md) và [Production Troubleshooting](./production_troubleshooting.md).